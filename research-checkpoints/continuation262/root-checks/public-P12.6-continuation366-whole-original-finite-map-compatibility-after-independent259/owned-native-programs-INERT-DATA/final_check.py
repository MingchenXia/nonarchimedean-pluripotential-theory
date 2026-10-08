"""Owned reproducibility/support/artifact audit; mathematical validity is not inferred."""
import hashlib,json,pathlib,platform,sys
root=pathlib.Path.cwd()
data=json.loads((root/'actual-FINAL.json').read_text())
native=json.loads((root/'native-notes.json').read_text())
paper=(root/'P12.6-review-paper.tex').read_bytes()
proof=(root/'whole-proof.md').read_text()
legal={'G331','G345'};support_rows=[]
for n in data['notes']:
    body=(root/'sections'/(n['id']+'.md')).read_text()
    assert n['text']==body and body.encode() in paper and body in proof
    assert all(s in legal for s in n['support']), (n['id'],n['support'],legal)
    assert n['id'] not in legal
    assert not any('/' in s or '.' in s for s in n['support'])
    support_rows.append({'id':n['id'],'support':n['support'],'complete_body_in_paper':True})
    legal.add(n['id'])
assert data==native and data['candidate'] is True and len(data['notes'])==10
assembly=json.loads((root/'evidence/assembly.json').read_text())
for e in assembly['literal_grants']:
    b=(root/e['file']).read_bytes()
    assert b in paper and hashlib.sha256(b).hexdigest()==e['sha256']
assert all(e['in_current_paper'] and e['in_argument'] for e in assembly['current_sections'])
assert assembly['all_actual_texts_differ'] and assembly['captured_FINAL_is_distinct'] and assembly['local_expanded_pair_equal']
inputs=json.loads((root/'evidence/input-audit.json').read_text())
assert len(inputs['entries'])==119 and all(e['matches'] for e in inputs['entries'])
diagnostics=json.loads((root/'evidence/bounded-diagnostics.json').read_text())
assert diagnostics['status']=='PASS' and not diagnostics['failures']
decision=json.loads((root/'acceptance-decision.json').read_text())
assert decision['review_complete'] and not decision['external_acceptance_performed'] and not decision['compiler_run']
required=['P12.6-review-paper.tex','whole-proof.md','whole-source-application-ledger.md',
 'whole-proof-coverage.md','exact-scope.md','original-scope-and-noncircularity-decision.md',
 'acceptance-decision.json','native-notes.json','actual-FINAL.json','diagnostic-input.json',
 'review_inputs.py','bounded_diagnostics.py','assemble_review.py','final_check.py']
hashes=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.relative_to(root).parts[0] not in ('read-data','LOCALONLY') and p.name!='final-audit.json':
        b=p.read_bytes();hashes.append({'file':str(p.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
assert all((root/f).is_file() for f in required)
out={'status':'PASS_ARTIFACT_AND_SUPPORT_CHECKS_ONLY','environment':{'python':sys.version,'platform':platform.platform(),'cwd':str(root)},
 'input_matches':119,'new_notes':10,'qualified_literal_components':14,'supports':support_rows,
 'finite_diagnostics':diagnostics['counts'],'own_files':hashes,
 'candidate':True,'mathematical_verification':False,'compiler_run':False,'external_acceptance':False,
 'actual_native256_vs_expanded_qualification_preserved':True,
 'limitations':'Hash/support/body equality and finite diagnostic success are not mathematical proofs.'}
(root/'evidence/final-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('own_files','supports')},indent=2))
