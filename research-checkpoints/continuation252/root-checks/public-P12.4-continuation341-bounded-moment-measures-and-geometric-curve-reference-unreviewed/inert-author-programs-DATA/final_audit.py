#!/usr/bin/env python3
"""Own artifact/support audit only; not a mathematical checker."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parent
native = json.loads((ROOT / 'native-notes.json').read_text())
seen = {'G331'}
assert native['candidate'] is False
for note in native['notes']:
    assert note['id'] not in seen
    assert set(note) == {'id','summary','detailedSummary','text','support'}
    assert set(note['support']) <= seen
    assert note['text'] == (ROOT/(note['id']+'.md')).read_text()
    seen.add(note['id'])
required = ['P12.4-paper.tex','P12.4-paper.pdf','argument.md','source-application-ledger.md',
            'exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md',
            'native-notes.json','bounded-evidence-input.json','audit_inputs.py','exact_diagnostics.py',
            'build_delivery.py','final_audit.py','reports/environment.json','reports/input-hashes.json',
            'reports/exact-diagnostics.json','reports/build-results.json']
for name in required:
    assert (ROOT/name).is_file(), name
retention = json.loads((ROOT/'reports/input-hashes.json').read_text())
for record in retention['records']:
    data = (ROOT/record['local']).read_bytes()
    assert len(data) == record['expected_bytes']
    assert hashlib.sha256(data).hexdigest() == record['expected_sha256']
assert json.loads((ROOT/'reports/build-results.json').read_text())['all_success']
assert json.loads((ROOT/'reports/exact-diagnostics.json').read_text())['status'] == 'PASS'
report = {'status':'PASS', 'notes':len(native['notes']), 'candidate':False,
          'bound_input_files':len(retention['records']), 'required_artifacts':required,
          'checks':['required files exist','earlier-only declared supports','full texts match own notes',
                    'retained inputs match bindings','build command success','declared finite observations pass'],
          'limits':'No mathematical verification, whole-original completion, or independent acceptance is asserted.'}
(ROOT/'reports/final-audit.json').write_text(json.dumps(report,indent=2)+'\n')
skip = {'reports/own-bindings.json'}
bindings = []
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or any(part.startswith('.') for part in path.relative_to(ROOT).parts):
        continue
    local = str(path.relative_to(ROOT))
    if local in skip:
        continue
    body = path.read_bytes()
    bindings.append({'path':local,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest()})
(ROOT/'reports/own-bindings.json').write_text(json.dumps({'files':bindings,
    'self_exclusion':'This manifest excludes itself to avoid a recursive hash binding.',
    'mathematical_status':'Unverified drafts; candidate=false.'},indent=2)+'\n')
print(json.dumps({'status':'PASS','notes':len(native['notes']),'candidate':False,'bound_inputs':len(retention['records'])}))
