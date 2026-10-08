#!/usr/bin/env python3
"""Fresh artifact consistency audit, not a mathematics checker or TeX compiler."""
import hashlib, json, re
from pathlib import Path
HERE=Path(__file__).resolve().parent
required=['P12.4-bounded-moment-paper.tex','independent-review.md','whole-proof.md',
          'whole-source-application-ledger.md','whole-proof-coverage.md',
          'original-scope-and-noncircularity.md','acceptance-decision.json','native-notes.json']
for name in required:
    assert (HERE/name).is_file(),name
native=json.loads((HERE/'native-notes.json').read_text())
assert native['candidate'] is False
seen={'G331'}
for note in native['notes']:
    assert note['id'] not in seen
    assert all(support in seen for support in note['support']),note['id']
    assert all(note[key] for key in ['summary','detailedSummary','text'])
    seen.add(note['id'])
whole=(HERE/'whole-proof.md').read_text()
parts=re.split(r'^## n(\d+)\. (.+)\n',whole,flags=re.M)
for i in range(1,len(parts),3):
    note=native['notes'][int(parts[i])-1]
    body=re.sub(r'^\*\*Support: .+?\.\*\*\s*','',parts[i+2].strip())
    assert note['text']==parts[i+1]+'\n\n'+body
paper=(HERE/'P12.4-bounded-moment-paper.tex').read_bytes()
grants=[]
for path in sorted((HERE/'inputs/G331').iterdir()):
    raw=path.read_bytes()
    assert raw in paper,path.name
    grants.append({'file':path.name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'literal_paper_inclusion':True})
assert len(grants)==5
text=paper.decode()
without_verbatim=re.sub(r'\\begin\{Verbatim\}.*?\\end\{Verbatim\}','',text,flags=re.S)
assert len(re.findall(r'\\documentclass',without_verbatim))==1
assert len(re.findall(r'\\begin\{document\}',without_verbatim))==1
assert len(re.findall(r'\\end\{document\}',without_verbatim))==1
assert not re.search(r'\\(?:input|include)\s*\{',without_verbatim)
assert text.count('\\begin{Verbatim}')==text.count('\\end{Verbatim}')
decision=json.loads((HERE/'acceptance-decision.json').read_text())
assert not decision['original_P12_4_complete']
assert not decision['compilation_performed']
assert all(record['matches'] for record in json.loads((HERE/'evidence/input-audit.json').read_text()))
diagnostics=json.loads((HERE/'evidence/finite-diagnostics.json').read_text())
assert diagnostics['status']=='PASS finite diagnostics only'
assert (HERE/'evidence/failed-finite-diagnostics-early-window.py').is_file()
task_input=json.loads((HERE/'evidence/local-task-input.json').read_text())
raw=(HERE/'input.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()==task_input['sha256']
result={'status':'PASS artifact consistency only','required_deliverables':required,
        'notes':len(native['notes']),'supports_valid':True,'native_proofs_match_whole_proof':True,
        'complete_G331_literal_inclusions':grants,'standalone_TeX_external_inputs':False,
        'candidate':False,'compilation':False,'local_task_input_unchanged':True,'finite_counts':diagnostics['counts'],
        'limitations':'No check in this program verifies mathematics, source application correctness, geometric comparison, locality or TeX compilation.'}
(HERE/'evidence/final-audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'notes':result['notes'],'candidate':False,'compilation':False,'required_deliverables':len(required)}))
