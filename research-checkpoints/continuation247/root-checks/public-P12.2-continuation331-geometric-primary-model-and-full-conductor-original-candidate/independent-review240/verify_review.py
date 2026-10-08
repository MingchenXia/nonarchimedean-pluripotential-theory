"""Fresh structural/integrity checks only, not a theorem verifier."""
from pathlib import Path
import json, hashlib

HERE = Path(__file__).resolve().parent
delivery = json.loads((HERE / 'native-review-notes.json').read_text())
seen = set()
for i, note in enumerate(delivery['notes'], 1):
    assert set(note) == {'id','summary','detailedSummary','text','support'}
    assert note['id'] == f'n{i}' and note['id'] not in seen
    assert all(s in seen for s in note['support'])
    assert all(note[k] for k in ('summary','detailedSummary','text'))
    assert note['text'] == (HERE / f'n{i}.md').read_text().strip()
    seen.add(note['id'])
assert len(seen)==12 and delivery['candidate'] is True
assert set(delivery['notes'][-1]['support']) == {f'n{i}' for i in range(1,12)}
required = ['whole-proof.md','whole-source-application-ledger.md','whole-proof-coverage.md',
 'original-scope-and-noncircularity.md','original-scope-decision.md','bounded-evidence-report.json',
 'exact-input-hashes.json','historical-inventory-rehash.json','per-note-verdicts.json','review-environment.json']
assert all((HERE / name).is_file() for name in required)
inputs = json.loads((HERE / 'exact-input-hashes.json').read_text())
for row in inputs:
    raw = Path(row['path']).read_bytes()
    assert len(raw) == row['bytes'] and hashlib.sha256(raw).hexdigest() == row['sha256']
observations = {'status':'PASS', 'scope':'JSON structure, earlier LOCAL supports, artifact presence and current input integrity only',
 'notes':12,'current_input_records':len(inputs),'mathematical_correctness_verified_by_program':False}
(HERE / 'fresh-check-output.json').write_text(json.dumps(observations, indent=2)+'\n')
files=[]
for path in sorted(HERE.rglob('*')):
    if not path.is_file() or path.name=='own-hashes.json' or any(p.startswith('.') for p in path.relative_to(HERE).parts):
        continue
    raw=path.read_bytes()
    files.append({'path':str(path.relative_to(HERE)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(HERE / 'own-hashes.json').write_text(json.dumps({'algorithm':'SHA-256','excluded_self':'own-hashes.json','artifacts':files},indent=2)+'\n')
print(json.dumps(observations))
