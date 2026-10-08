import json,pathlib,hashlib,re
root=pathlib.Path.cwd();records=[]
def check(name,ok):records.append({'check':name,'pass':bool(ok)})
notes=json.loads((root/'native-notes.json').read_text());seen={'G331','G345'};proof=(root/'proof.tex').read_text();paper=(root/'P12.6-paper.tex').read_text()
for n in notes['notes']:
 check(n['id']+' legal supports',all(s in seen for s in n['support']));seen.add(n['id'])
 check(n['id']+' full body in paper',(root/'sections'/f'{n["id"]}.tex').read_text() in paper)
 check(n['id']+' fields complete',all(isinstance(n[k],str) and n[k] for k in ['summary','detailedSummary','text']))
for p in sorted((root/'attachments').iterdir()):check(p.name+' unchanged entire appendix',p.read_text() in paper)
check('whole NEW proof in manuscript',proof in paper)
for env in ['equation','align','proof','theorem','proposition']:
 check('new proof balanced '+env,proof.count('\\begin{'+env+'}')==proof.count('\\end{'+env+'}'))
check('no control characters',not any(ord(c)<32 and c not in '\n\t\r' for c in proof))
check('new349 domain included','EVERY full' in (root/'sections/n7.tex').read_text() and 'T_RH' in (root/'sections/n7.tex').read_text())
check('new351 both positive envelopes included','BOTH ends' in (root/'sections/n4.tex').read_text())
check('independent source gauge trace slot','H_{\\mathfrak c}(w)/\\lambda' in proof)
check('candidate false',notes['candidate'] is False and json.loads((root/'acceptance-decision.json').read_text())['candidate'] is False)
check('all current bound files match',all(r['match'] for r in json.loads((root/'evidence/input-audit.json').read_text())['files']))
check('diagnostic success only finite',json.loads((root/'evidence/bounded-checks.json').read_text())['failures']==0)
required=['P12.6-paper.tex','whole-proof.md','proof.tex','argument.md','whole-source-application-ledger.md','whole-proof-coverage.md','exact-scope.md','original-scope-and-noncircularity-decision.md','acceptance-decision.json','native-notes.json']
for name in required:check('deliverable '+name,(root/name).stat().st_size>0)
result={'checks':records,'count':len(records),'failures':sum(not r['pass'] for r in records),'artifact_consistency_not_mathematical_verification':True,'compiler_run':False}
(root/'evidence/final-audit.json').write_text(json.dumps(result,indent=2))
files=[]
for name in required+['audit_inputs.py','bounded_checks.py','build_delivery.py','final_audit.py','bounded-evidence-input.json']:
 data=(root/name).read_bytes();files.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(root/'evidence/output-hashes.json').write_text(json.dumps(files,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2));print('failed:',[r['check'] for r in records if not r['pass']])
