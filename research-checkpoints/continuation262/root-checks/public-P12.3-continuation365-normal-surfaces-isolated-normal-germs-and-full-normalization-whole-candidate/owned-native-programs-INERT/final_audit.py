"""Owned static integrity audit. Its success is not a mathematical verdict."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    checks.append({'check':name,'passed':bool(value)})
    if not value:raise AssertionError(name)

names=['P12.3-paper.md','P12.3-paper.tex','argument.md',
       'whole-source-application-ledger.md','whole-proof-coverage.md',
       'exact-scope.md','original-scope-and-noncircularity-decision.md',
       'acceptance-decision.json','native-notes.json','actual-FINAL.json',
       'original-task.json','audit_inputs.py','reading_audit.py',
       'bounded_diagnostics.py','build_delivery.py','final_audit.py',
       'inputs/diagnostic-input.json','reports/environment.json',
       'reports/input-hashes.json','reports/reading-bindings.json',
       'reports/current-eleven-body-bindings.json','reports/bounded-diagnostics.json']
for name in names:check('required '+name,(ROOT/name).is_file())
notes=json.loads((ROOT/'native-notes.json').read_text())
check('candidate false',notes['candidate'] is False)
check('actual FINAL exact duplicate',(ROOT/'native-notes.json').read_bytes()==(ROOT/'actual-FINAL.json').read_bytes())
legal={'G331','B341','E350'}
argument=(ROOT/'argument.md').read_text();paper=(ROOT/'P12.3-paper.md').read_text()
for n in notes['notes']:
    check('legal earlier supports '+n['id'],set(n['support'])<=legal)
    check('exact complete body '+n['id'],n['text']==(ROOT/(n['id']+'.md')).read_text())
    check('body in argument '+n['id'],n['text'] in argument)
    check('body in standalone paper '+n['id'],n['text'] in paper)
    legal.add(n['id'])
for r in json.loads((ROOT/'reports/input-hashes.json').read_text()):
    data=(ROOT/r['local']).read_bytes()
    check('retained immutable '+r['key'],len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'])
orig=next(r for r in json.loads((ROOT/'reports/input-hashes.json').read_text()) if r['key']=='m21')
check('exact original object',(ROOT/'original-task.json').read_bytes()==(ROOT/orig['local']).read_bytes())
binding=json.loads((ROOT/'reports/reading-bindings.json').read_text())
check('current eleven count',len(binding['current_eleven'])==11)
check('current expanded exact',all(r['exact_expanded_in_argument'] and r['exact_expanded_note_file'] for r in binding['current_eleven']))
check('historical qualification',binding['historical_reading_duplicates_is_seven_254_not_current_eleven_257'])
diag=json.loads((ROOT/'reports/bounded-diagnostics.json').read_text())
check('finite diagnostics successful',diag['all_passed'])
decision=json.loads((ROOT/'acceptance-decision.json').read_text())
check('no compilation',decision['compilation_performed'] is False)
check('normal residual explicit',any('nonisolated' in s for s in decision['residual']))
check('USC formula limitation','NO unconditional fibre-maximum formula' in (ROOT/'n7.md').read_text())
check('all-field surface scope','mixed characteristic' in (ROOT/'n2.md').read_text())
check('correct diagnostic energy sign','E(u_j)=-1/(2j)' in (ROOT/'n10.md').read_text())
check('no forced closure','candidate=false' in (ROOT/'n11.md').read_text().lower())
tex=(ROOT/'P12.3-paper.tex').read_text()
check('source document balance',tex.count('\\begin{document}')==tex.count('\\end{document}')==1)
outputs={}
for p in ROOT.iterdir():
    if p.is_file():
        data=p.read_bytes();outputs[p.name]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
(ROOT/'reports/own-artifacts.json').write_text(json.dumps(outputs,indent=2)+'\n')
(ROOT/'reports/final-audit.json').write_text(json.dumps({'checks':checks,'passed':len(checks),
    'mathematical_verification':False,'compilation':False},indent=2)+'\n')
(ROOT/'reports/commands.json').write_text(json.dumps({
 'rerun':['python audit_inputs.py','python reading_audit.py','python bounded_diagnostics.py',
          'python build_delivery.py','python final_audit.py'],
 'reader':'python read_data.py KEY START END; supplied bytes interpreted as data only',
 'source_pixels':'Supplied local p43-p46 viewed with view_image; no source conversion executed',
 'observed':{'input_matches':139,'diagnostic_counts':diag['counts'],'static_checks':len(checks)},
 'scope':'Own bounded standard-library programs; no supplied import/execution or compiler'},indent=2)+'\n')
print(json.dumps({'static_checks_passed':len(checks),'mathematical_verification':False,'candidate':False}))
