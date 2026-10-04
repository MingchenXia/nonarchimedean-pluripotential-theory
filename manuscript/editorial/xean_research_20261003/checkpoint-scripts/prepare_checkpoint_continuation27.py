"""Freeze fresh graph research and an unaccepted completed-algebraic proof draft."""
from pathlib import Path
import datetime,hashlib,json,shutil

root=Path('/workspace/research');checkpoint=root/'github-checkpoint'
parent='df6cad1c1bea96b8261a13663421481dbf219e80'
active=json.loads((root/'active-work.json').read_text())
assert active['github_checkpoint']['commit_sha']==parent
assert active['selected_atoms']==['P06.2','P05.2'] and not active['full_solutions']
snapshot=checkpoint/'continuation27-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[]
def add(path,target,mutable=False):
    path=Path(path);assert path.is_file(),path
    if mutable:
        copy=snapshot/(str(len(files))+'-'+path.name);shutil.copyfile(path,copy);path=copy
    assert prefix+target not in {f['path'] for f in files}
    files.append({'local':str(path),'path':prefix+target,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
d=root/'campaigns/round-22/P05.2-arbitrary-graph-product-continuation'
for name in ('input.json','settings.json','input-manifest.json'):
    add(d/name,'continuation-inputs/arbitrary-graph-product/'+name)
for name in ('prepare_arbitrary_graph_products.py','review_arbitrary_graph_products_after_completion.py','audit_completed_algebraic_draft.py'):
    add(root/name,'checkpoint-scripts/'+name)
add(root/'P05.2-higher-relation-graph-product-proposal.md','root-proposals/P05.2-higher-relation-graph-product-proposal.md')
for name in ('complete_plane_atoms.py','output.json','root-check.json'):
    add(root/'root-checks/higher-relation-graph-product'/name,'root-checks/higher-relation-graph-product/'+name)
d=root/'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-continuation'
campaign=json.loads((d/'run.json').read_text())['campaign']
assert campaign['status']=='completed' and not campaign['result']['candidate']
w=Path(campaign['result']['workspace'])
add(d/'run.json','pending-research/all-dimensional-completed-algebraic/run.json')
for name in ('P06.2-argument.md','proof-core.md','status.json','self-audit.md','research-evidence.md','source-evidence.md','artifact-checks.json','embed_sources.py'):
    add(w/name,'pending-research/all-dimensional-completed-algebraic/'+name)
for name in ('manifest.json','primary-units.json'):
    add(w/'sources'/name,'pending-research/all-dimensional-completed-algebraic/sources/'+name)
review=root/'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-review'
for name in ('task.json','settings.json','argument.md','freeze.json','source-artifact-binding.json','root-draft-read-record.json','root-read-record-preparation-failure.json'):
    add(review/name,'pending-reviews/all-dimensional-completed-algebraic/'+name)
add(checkpoint/'push-receipt-continuation26.json','records/push-receipt-continuation26.json')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):
    add(root/name,name,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
push=checkpoint/'push_checkpoint_continuation27.py';assert not push.exists()
text=(checkpoint/'push_checkpoint_continuation26.py').read_text().replace('continuation26','continuation27')
text=text.replace('Publish reviewed real-reference graph products and finite Galois current transport',
                  'Checkpoint arbitrary graph research and algebraic completion draft')
push.write_text(text);add(push,'checkpoint-scripts/'+push.name)
summary=snapshot/'CHECKPOINT.txt'
summary.write_text('Checkpoint27: Latest accepted papers are rounds20and21, already pushed. New completed-algebraic ALL-dimensional ordinary-current transport/ALL-bidegree compact-test-descent draft is committed but UNACCEPTED, independent review running. New993line core/all2canonical notes read; all33primary bodies exactly rebound to prior fully read authentic bodies, with fresh scope applications assessed and full-new-appendix-fresh-read explicitlyfalse. Fresh P05arbitraryfinitegraphproduct each-real-reference campaign running. Root higher-relation diagnostic counts19mergedvertices,totalmass16 and fullcontact-1/2 on one explicit cross-times-line example, not a universal proof or accepted new theorem; not injected into frozen campaign. All42original atoms remain open; onlyP05/P06selected, goal active.\n')
add(summary,'CHECKPOINT.txt')
manifest={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003',
    'expected_previous_checkpoint':parent,'files':files,
    'scope':'Fresh arbitrary-graph research and UNACCEPTED completed-algebraic draft; independent review running; all42originalopen.'}
path=checkpoint/'upload-manifest-continuation27.json';assert not path.exists()
path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
