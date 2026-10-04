"""Snapshot the new continuation and exact root-read records."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess

root=Path('/workspace/research')
checkpoint=root/'github-checkpoint'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
active_path=root/'active-work.json'
active=json.loads(active_path.read_text())
assert active['github_checkpoint']['commit_sha']=='1f9d0ec4caafe7cbd3813ff1e832d60f0f564a2b'
assert active['selected_atoms']==['P06.2','P05.2'] and not active['full_solutions']
active['updated_utc']=now
active['turn_checkpoint']='Both new P05 every-fixed-real-reference and P06 finite-Galois all-pure-dimensional full proof drafts/all canonical notes read; independent reviews still running. Fresh completed-algebraic ALL-complementary-form all-pure-dimensional P06 continuation running with fallible reconstructed predecessors. All42original open; goal active.'
active['pending_real_reference_publication']={
    'script':str(root/'prepare_round20_real_reference_source.py'),
    'state':'Prepared script only, never executed. Source/PDF not created; requires fully read and bound exact-scope independent PASS.'}
active['next_work']='Read both independent review results when committed; publish accepted exact scopes in the native LaTeX editor, repair any substantive defects through fresh campaigns, continue completed-algebraic form transport and the remaining original tasks in small batches, and push regular checkpoints.'
active_path.write_text(json.dumps(active,ensure_ascii=False,indent=2)+'\n')
refresh=root/'refresh_checklist.py'
s=refresh.read_text()
needle='fresh finite-Galois all-pure-dimensions complementary-test ascent draft completed, independent review running and no new grant.'
assert needle in s
s=s.replace(needle,needle+' New completed-algebraic ALL-complementary-test all-pure-dimensional continuation running; finite-Galois draft and earlier scalar-test proof supplied as fallible evidence, no grant.')
refresh.write_text(s)
subprocess.run(['python3',str(refresh)],check=True,capture_output=True)
snapshot=checkpoint/'continuation25-uploaded-live-records'
snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/'
files=[]
def add(path,target,mutable=False):
    path=Path(path);assert path.is_file(),path
    if mutable:
        destination=snapshot/(str(len(files))+'-'+path.name)
        shutil.copyfile(path,destination);path=destination
    files.append({'local':str(path),'path':prefix+target,
                  'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})

directory=root/'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-continuation'
for name in ['input.json','settings.json','input-manifest.json']:
    add(directory/name,'continuation-inputs/all-dimensional-completed-algebraic/'+name)
for name in ['prepare_all_dimensional_completed_algebraic.py','review_all_dimensional_completed_algebraic_after_completion.py','prepare_round20_real_reference_source.py']:
    add(root/name,'checkpoint-scripts/'+name)
add(root/'deliverables/round-20-publication-preparation-pending.json','records/round-20-publication-preparation-pending.json')
for round_number,label,name in [
    ('19','general-finite-galois','P06.2-general-finite-galois-review'),
    ('20','fixed-real-reference-graph-products','P05.2-fixed-real-reference-review')]:
    add(root/('campaigns/round-'+round_number)/name/'root-draft-read-record.json',
        'pending-reviews/'+label+'/root-draft-read-record.json')
add(root/'campaigns/round-17/P06.2-recognition-source-proof-repair/root-draft-read-progress.json',
    'incomplete-research/curve-recognition-source-proof-repair/root-draft-read-progress.json')
for name in ['root-check.json','real-sum-diagnostic.py','real-sum-output.json']:
    add(root/'root-checks/fixed-real-reference-graph-products'/name,
        'root-checks/fixed-real-reference-graph-products/'+name)
add(checkpoint/'push-receipt-continuation24.json','records/push-receipt-continuation24.json')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py']:
    add(root/name,name,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
summary=snapshot/'CHECKPOINT.txt'
summary.write_text('Checkpoint25: Both new partial proof drafts and all canonical notes are fully read. P06 includes all33 exact primary body bindings; P05 includes a recomputed exact quadratic-field sum diagnostic. Both independent reviews remain running and neither new claim is granted. The incomplete curve-recognition repair core/all5notes are read, with full assembled source appendix not freshly read and no recognition theorem. Fresh all-dimensional completed-algebraic complementary-form transport is active via Xean native gpt-6.1-sol xhigh; all predecessors are fallible evidence for reconstruction. The future real-reference publication script is never executed and creates no paper before a read/bound PASS. Only P05/P06original atoms active; all42original problems remain open and goal active.\n')
add(summary,'CHECKPOINT.txt')
manifest={'generated_utc':now,'repository':'MingchenXia/nonarchimedean-pluripotential-theory',
          'branch':'codex/xean-research-20261003',
          'expected_previous_checkpoint':'1f9d0ec4caafe7cbd3813ff1e832d60f0f564a2b',
          'files':files,'scope':'Exact root reads and fresh unaccepted completed-algebraic continuation; latest accepted paper round19; all42original open.'}
p=checkpoint/'upload-manifest-continuation25.json';assert not p.exists()
p.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
s=(checkpoint/'push_checkpoint_continuation24.py').read_text().replace('continuation24','continuation25')
s=s.replace('Checkpoint completed partial drafts and independent review inputs','Checkpoint proof reads and completed algebraic continuation')
p=checkpoint/'push_checkpoint_continuation25.py';assert not p.exists();p.write_text(s)
print(json.dumps({'files':len(files),'manifest':str(checkpoint/'upload-manifest-continuation25.json')}))
