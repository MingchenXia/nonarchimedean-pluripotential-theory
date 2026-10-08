"""Own static deliverable checks only, never a mathematical certificate."""
from pathlib import Path
import json,hashlib
r=Path.cwd();o=json.loads((r/'native-notes.json').read_text());seen={'G331','B341','E350'};checks=[]
for n in o['notes']:
    assert set(n)=={'id','summary','detailedSummary','text','support'}
    assert n['id'] not in seen and all(s in seen for s in n['support'])
    assert n['text']==(r/(n['id']+'.md')).read_text()
    assert n['text'] in (r/'argument.md').read_text()
    assert n['summary'] and n['detailedSummary'];seen.add(n['id']);checks.append(n['id'])
assert not o['candidate'] and not json.loads((r/'acceptance-decision.json').read_text())['candidate']
for x in json.loads((r/'reports/own-artifacts.json').read_text()):
    b=(r/x['file']).read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'];checks.append(x['file'])
assert hashlib.sha256((r/'original-task.json').read_bytes()).hexdigest()=='d524b816c1462a6909a85bd0e39b84ab34ca04be27ec99eccbfde7ffcc0316a8'
assert all(x['match'] for x in json.loads((r/'reports/input-audit.json').read_text()))
assert json.loads((r/'reports/bounded-diagnostics.json').read_text())['status']=='PASS'
t=(r/'P12.3-paper.tex').read_text();assert t.count(r'\begin{document}')==t.count(r'\end{document}')==1
assert t.count(r'\[')==t.count(r'\]')
result={'status':'PASS','static_checks':len(checks)+6,'legal_support_order':True,'candidate':False,'scope':'Artifact consistency only; no mathematical or compilation certification','compilation_performed':False}
(r/'reports/final-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
