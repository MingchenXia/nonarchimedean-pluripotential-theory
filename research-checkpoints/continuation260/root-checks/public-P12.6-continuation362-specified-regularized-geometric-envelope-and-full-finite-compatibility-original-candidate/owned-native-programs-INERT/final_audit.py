import json,hashlib,re,sys
from pathlib import Path
obj=json.loads(Path('native-notes.json').read_text());actual=json.loads(Path('actual-FINAL.json').read_text())
errors=[];seen={'G331','G345'};paper=Path('P12.6-paper.tex').read_text()
if obj!=actual:errors.append('actual/expanded mismatch')
for note in obj['notes']:
 if set(note)!={'id','summary','detailedSummary','text','support'}:errors.append('unexpectedfields '+note['id'])
 if any(s not in seen for s in note['support']):errors.append('illegal support '+note['id'])
 if note['text']!=Path('sections/'+note['id']+'.tex').read_text():errors.append('body mismatch '+note['id'])
 if note['text'] not in paper:errors.append('missingwholebody '+note['id'])
 if any(ord(c)<32 and c not in '\n\r\t' for c in note['text']):errors.append('controlchars '+note['id'])
 # Only OWN bodies; grants may intentionally contain quoted code/comments.
 if note['text'].count('\\[')!=note['text'].count('\\]'):errors.append('display imbalance '+note['id'])
 if note['text'].count('$')%2:errors.append('math delimiter imbalance '+note['id'])
 depth=0
 for k,c in enumerate(note['text']):
  if k and note['text'][k-1]=='\\':continue
  if c=='{':depth+=1
  if c=='}':depth-=1
  if depth<0:errors.append('brace underflow '+note['id']);break
 if depth:errors.append('brace imbalance '+note['id'])
 seen.add(note['id'])
gr=[]
for p in sorted(Path('grants').iterdir()):
 if p.read_text() not in paper:errors.append('missing literal grant '+p.name)
 gr.append({'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'entire_body_in_paper':p.read_text() in paper})
required=['P12.6-paper.tex','argument.md','whole-source-application-ledger.md','whole-proof-coverage.md','exact-scope.md','original-scope-and-noncircularity-decision.md','acceptance-decision.json','native-notes.json','actual-FINAL.json','audit_inputs.py','bounded_checks.py','inspect_source.py','build_delivery.py','final_audit.py','bounded-input.json']
art=[]
for f in required:
 p=Path(f)
 if not p.exists():errors.append('missing '+f)
 else:art.append({'file':f,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
checks=json.loads(Path('evidence/bounded-checks.json').read_text())
if checks['failure_count']:errors.append('finitechecks failed')
inputs=json.loads(Path('evidence/input-audit.json').read_text())
if any(not r['match'] for r in inputs['files']):errors.append('inputmismatch')
out={'errors':errors,'note_count':len(obj['notes']),'candidate':obj['candidate'],'legal_support_order':not any('support' in e for e in errors),'actual_expanded_fields_equal':obj==actual,'own_full_proof_bodies_in_paper':True,'entire_grant_bodies':gr,'artifacts':art,'bound_inputs':len(inputs['files']),'finite_arithmetic_checks':sum(checks['counts'].values()),'compilation_run':False,'formal_verification':False,'independent_acceptance':False,'interpretation':'Artifact consistency audit only; no mathematical correctness is inferred.'}
Path('evidence/final-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['artifacts','entire_grant_bodies']},indent=2))
sys.exit(bool(errors))
