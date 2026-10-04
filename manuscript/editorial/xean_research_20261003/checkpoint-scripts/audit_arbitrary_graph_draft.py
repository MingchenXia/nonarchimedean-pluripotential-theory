"""Bind newly read mathematics and exact prior fully read portions."""
from pathlib import Path
import datetime,difflib,hashlib,json
r=Path('/workspace/research');d=r/'campaigns/round-22/P05.2-arbitrary-graph-product-continuation';v=d.parent/'P05.2-arbitrary-graph-product-review'
c=json.loads((d/'run.json').read_text())['campaign'];assert c['status']=='completed' and not c['result']['candidate'];w=Path(c['result']['workspace'])
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
main=w/'P05.2-argument.md';old=r/'campaigns/round-20/P05.2-fixed-real-reference-continuation/artifacts/codex-UZmUll/P05.2-argument.md';prior=r/'campaigns/round-20/P05.2-fixed-real-reference-review/root-draft-read-record.json';pr=json.loads(prior.read_text());assert pr['full_main_argument_read'] and pr['main_argument_sha256']==sha(old)
a=old.read_text().split('\n');b=main.read_text().split('\n')
direct=[(1,202),(357,446),(449,449),(571,626),(870,1273),(1543,2230)]
read_lines={i for x,y in direct for i in range(x,y+1)};reused=[];changes=[]
for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if tag=='equal':
        body='\n'.join(b[k:l]);assert body=='\n'.join(a[i:j]);reused.append({'old_lines':[i+1,j],'new_lines':[k+1,l],'body_sha256':hashlib.sha256(body.encode()).hexdigest()})
    else:
        assert set(range(k+1,l+1))<=read_lines,(tag,k+1,l)
        changes.append({'kind':tag,'old_lines':[i+1,j],'new_lines':[k+1,l]})
origins=json.loads((w/'source-hashes.json').read_text())
for item in origins:
    p=w/item['file'];o=Path(item['origin']);assert p.read_bytes()==o.read_bytes() and sha(p)==item['sha256']
argument=(v/'argument.md').read_text();assert argument.startswith(main.read_text())
f=json.loads((v/'freeze.json').read_text());binding=json.loads((v/'source-artifact-binding.json').read_text())
assert sha(main)==f['main_argument_sha256']==binding['main_argument_sha256']
assert sha(v/'argument.md')==f['argument_sha256']==binding['review_argument_sha256']
assert sha(w/'P05.2-partial.tex')==f['source_tex_sha256']==binding['source_tex_sha256']
assert sha(w/'status.json')==f['source_status_sha256']==binding['source_status_sha256']
record={'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_workspace':str(w),'main_argument_sha256':sha(main),'full_main_argument_read':True,'full_main_fresh_read':False,'read_method':'All new text directly read, including the full newly appended comparison-source proofs and complete existing one-dimensional dossier; every reused portion is exact-text bound to the prior full direct read. New mathematical applications assessed independently; earlier verdicts provide no theorem grant.','direct_line_ranges':direct,'prior_full_read_record':str(prior),'prior_full_read_record_sha256':sha(prior),'prior_main_sha256':sha(old),'exact_reused_blocks':reused,'all_changed_blocks':changes,'all_canonical_notes_fully_read':True,'canonical_note_ids':[n['id'] for n in c['result']['notes']],'canonical_run_sha256':sha(d/'run.json'),'canonical_text_sha256':{n['id']:hashlib.sha256(n['text'].encode()).hexdigest() for n in c['result']['notes']},'author_audit_fully_read':True,'research_notes_fully_read':True,'source_snapshots_all_exact_bound':True,'source_snapshot_count':len(origins),'review_argument_sha256':sha(v/'argument.md'),'freeze_sha256':sha(v/'freeze.json'),'source_artifact_binding_sha256':sha(v/'source-artifact-binding.json'),'independent_review_pending':True,'publish_allowed':False,'original_atom_solved':False,'observations':'Supported rational-coordinate PCC pinning and rational same-face extension repair the informal irrational-endpoint proposal. Both primitive-normal axis families are present. Complete contact follows from every other old atom having zero bump and every new refinement atom having zero inherited mass. No general balanced-space theorem or literal-coefficient claim.'}
p=v/'root-draft-read-record.json';assert not p.exists();p.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'root_read_record':str(p),'sha256':sha(p),'reused_blocks':len(reused),'changed_blocks':len(changes),'sources':len(origins)}))
