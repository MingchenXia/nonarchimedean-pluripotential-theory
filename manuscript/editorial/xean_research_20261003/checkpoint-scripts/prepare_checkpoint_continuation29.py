"""Freeze fresh curve repair inputs and unaccepted graph-product proof."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint';parent='3d45acdaf0fca3582020a3b1428d38307210a28d'
a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent
assert a['selected_atoms']==['P06.2','P05.2'] and not a['full_solutions']
snapshot=c/'continuation29-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[]
def add(path,target,mutable=False):
    path=Path(path);assert path.is_file(),path
    if mutable:
        cp=snapshot/(str(len(files))+'-'+path.name);shutil.copyfile(path,cp);path=cp
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(path),'path':prefix+target,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
d=r/'campaigns/round-23/P06.2-curve-two-sign-source-repair'
for n in ('input.json','settings.json','input-manifest.json'):add(d/n,'continuation-inputs/curve-two-sign-source-repair/'+n)
for n in ('prepare_curve_two_sign_source_repair.py','review_curve_two_sign_source_repair_after_completion.py','audit_arbitrary_graph_draft.py'):add(r/n,'checkpoint-scripts/'+n)
d=r/'campaigns/round-22/P05.2-arbitrary-graph-product-continuation';campaign=json.loads((d/'run.json').read_text())['campaign'];assert campaign['status']=='completed' and not campaign['result']['candidate'];w=Path(campaign['result']['workspace'])
add(d/'run.json','pending-research/arbitrary-graph-product/run.json')
for n in ('P05.2-argument.md','P05.2-partial.tex','status.json','higher-relation-proof.md','intrinsic-graph-proof.md','author-self-audit.md','research-notes.md','checks.json','source-hashes.json','compose_argument.py','snapshot_sources.py','build-evidence.json','diagnostic-evidence.json','higher-relation-diagnostic.py','higher-relation-input.json','higher-relation-output.json'):
    add(w/n,'pending-research/arbitrary-graph-product/'+n)
v=d.parent/'P05.2-arbitrary-graph-product-review'
for n in ('argument.md','task.json','settings.json','freeze.json','source-artifact-binding.json','root-draft-read-record.json'):add(v/n,'pending-reviews/arbitrary-graph-product/'+n)
for n in ('higher-relation-diagnostic.py','higher-relation-input.json','higher-relation-output.json','root-check.json'):add(r/'root-checks/arbitrary-graph-product-draft'/n,'root-checks/arbitrary-graph-product-draft/'+n)
add(c/'push-receipt-continuation28.json','records/push-receipt-continuation28.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):add(r/n,n,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation29.py';assert not p.exists();s=(c/'push_checkpoint_continuation28.py').read_text().replace('continuation28','continuation29').replace('Publish reviewed completed-algebraic transport and curve source evidence','Checkpoint arbitrary graph proof and fresh curve source repair');p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt';p.write_text('Checkpoint29: Accepted13-page paper22 already pushed3d45acd. New arbitrary finite-graph product each-real-reference classification draft is UNACCEPTED with independent review running. All new proof/source text directly read, every reused block exactly bound to prior full direct reading, all3canonical notes fully read, all14sources exact-bound. Fresh3-input local-fan diagnostic rerun identical; only finite arithmetic, no universal-proof certification. Fresh curve ordinary two-sign source/scope repair running using authenticated primary texts and algebraically closed-only algebraization; earlier INCONCLUSIVE/incomplete attempts remain unchanged. No new regularization theorem accepted. All42originalsopen, P05.2/P06.2only, goalactive.\n');add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,'scope':'Unaccepted arbitrary graph proof under independent review and fresh curve source/scope repair; all42originalsopen.'}
p=c/'upload-manifest-continuation29.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'files':len(files),'manifest':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
