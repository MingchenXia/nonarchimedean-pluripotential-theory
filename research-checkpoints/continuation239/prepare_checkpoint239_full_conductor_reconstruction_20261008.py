from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation239.json'; F=G/'continuation239-publication-records'
S=K/'small-batch235236-public-status-20261008-continuation239'
C=next((R/'campaigns/round-236').iterdir())
D=K/'public-P12.2-continuation321-smooth-recovery-and-conductor-saturation-unreviewed'
B=K/'round234-whole-draft-ROOT-reading-and-full-conductor-continuation-binding-20261008.json'
N=K/'P12.2-conductor-primary-acquisition-and-ROOT-reading-metadata-20261008.json'
W=[K/'P12.2-continuation319-strictly-negative-unbounded-conductor-descent-working-proof-20261008.md',K/'P12.2-continuation320-zero-branch-dichotomy-and-full-decreasing-descent-working-proof-20261008.md']
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation238.json').read_text())
assert prior['commit_sha']=='bf52ec01e609718b38b5c84bda2304642066644a' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f=json.loads((C/'freeze.json').read_text()); assert (C/'launch-record.json').is_file()
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]: assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()): assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert f['structured_imported_notes_count']==0 and f['whole_math_files']==31 and f['private_primary_files']==11
assert sha(D/'P12.2-paper.tex')=='48a8c8e3b90a5cd264fe5c1aeae413392586147166b64049c654f744c615355b'
assert sha(D/'P12.2-paper.pdf')=='966824c5548f9db251398093acf20d1ef27adf56a4a0bc0e108d8b02c28e5db7'
F.mkdir(); S.mkdir(); now=datetime.now(timezone.utc).isoformat(); items=[]
for n,atom in [(234,'P12.2'),(235,'P05.1'),(236,'P12.2')]:
    old=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(old),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0]; assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[235,236],maximum_concurrent_campaigns=2,accepted_paper_number=88)
p=D/'ROOT-public-draft-status-20261008.json';x=json.loads(p.read_text());x.update(built_in_compiler_status='requested once; completion unverified at checkpoint freeze',built_in_compile_cell=403,editor_new_tab_not_opened=True);write(p,x)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(continuation=239,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),P12_2_completed_smooth_conductor_native234=dict(public_draft=str(D),reading_binding=str(B),actual_FINAL=str(K/'round234-actual-native-final.json'),native_registration_valid=True,candidate=False,whole_ROOT_paper_and_six_notes_read=True,own_hashes_verified=43,frozen_math_and_primary_hashes_verified=24,new_accepted_paper=False,original_closed=False),P12_2_original_full_conductor_reconstruction236=dict(directory=str(C),only_grants=[],whole_math_files=31,whole_math_bytes=f['whole_math_bytes'],private_primary_files=11,native234_and_ROOT317319320_unreviewed_DATA=True,model='gpt-6.1-sol',reasoning='xhigh',original_closed=False),P12_2_new_full_descent_working319320=dict(proposals=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,whole_ROOT_physically_read=True) for p in W],unreviewed=True,strictnegative_and_mixedzero_unbounded_general_descent_proposed=True,primary_metadata=str(N),all_background_application_gates_need_independent_check=True,source_grants=[],new_accepted_paper=False,original_closed=False))
    if name=='checklist-current.json':
        x['active_atoms']=[e['atom'] for e in active]
        t=next(t for t in x['targets'] if t['id']=='P12.2');t['research_status']='full original reconstruction active; proposed closure unreviewed';t['current_focus']='Native236: reconstruct independent numerical Cartier/ideal comparison, FULL smooth BFJ all-semivaluation specialization, ROOT317 bounded conductor + ROOT319 strictnegative unbounded insertion + ROOT320 normal-branch zero dichotomy and clopen active indicator descent.31wholeDATA,11privateprimaryfiles,ZEROgrants; all original gates remain OPEN pending independent proof/review.'
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint239: full conductor reconstruction\n\n10/42 original atoms solved;32OPEN;88accepted mathematical papers. No new acceptance or original closure.\n\nNative234 completed candidatefalse with a15-page paper321: full smooth BFJ recovery (zero/unit/bottom qualified), intrinsic numerical Cartier/ideal uniform comparison, general continuous conductor saturation and nonisolated cusp strict separation from the ENTIRE finite REAL raw downstairs cone. ROOT read the entire author TeX, allsixactualFINAL notes and complete source/scope/coverage; verified43own+24frozen bindings. Paper321 is UNREVIEWED; author checks/builds are not ROOT mathematical certification. Builtincompile403 requestedonce, completion unverified at freeze; protectedP16.4 stays open unchanged.\n\nNew ROOT319 proposes everywhere strictly negative unbounded conductor/finite-injection descent by dimension induction and continuous strict-majorant insertion. ROOT320 proposes full mixedzero descent: characteristic-free general Izumi--Rees yields a normal-branch zero dichotomy; direct Rees-divisor density includes nonminimal semivaluation supports; a fiber-constant active-branch indicator must descend via ROOT317 bounded comparison; insertion then constructs an ACTUAL decreasing continuous net, exactly zero on inactive points. No increasing-limit closure or psh-min claim. Corrected ROOT319 real-scaled profiles and ROOT317 rational-lattice/uniform-real-lattice distinction are mandatory. ALL proposals UNREVIEWED, no grants.\n\nNative236 independently reconstructs the entire originalP12.2 geometric class and proposed full conductor theorem from31whole mathematicalDATA and11privateprimaryfiles, ZERO supporting grants. Newly acquired exact Swanson--Huneke authorPDF/current2024-created bytes, Swanson survey, arXiv1404.4885v1 and officialStacks0C23 are LOCALONLY. Complete immediate units were ROOT-read and bound; no historical Rees1989 proof inspection or full-source reading is asserted. Exact published/background applications must be independently checked, including units in the Izumi order inequality. Native235 originalP05.1 coefficient-separated classification continues with its own frozen5qualifiednotes; no private ACTIVE outputs/hotfeedback are shared. Max2active native campaigns.\n\nFull external primary PDF/text/images/HTML remain LOCALONLY; public metadata, owned papers/proofs and frozen task inputs are included. All uploads authorized; no force update; exact remote file/tree/ref verification follows.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation239/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for name in ['freeze.json','launch-record.json','task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json']:add(C/name)
for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):add(e['path'])
for p in W+[B,N,K/'round234-actual-native-final.json',G/'push-receipt-continuation238.json',R/'record_verified238_20261008.py',R/'capture_completed_unbounded_geometric_research234_20261008.py',R/'prepare_original_full_conductor_reconstruction236_20261008.py',R/'launch_original_full_conductor_reconstruction236_20261008.py',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=32,historical_reviewed_scoped_papers=88,commit_message='Preserve smooth recovery and full conductor descent proposals for independent reconstruction',scope='10solved32OPEN88accepted; new15p321draft and ROOT319320 unreviewed; native235236max2active,31wholeDATA11privateprimaryZEROgrants for originalP12.2.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],statuses=[dict(round=e['round'],status=e['observed_status']) for e in items],originals_solved=10,originals_open=32),indent=2))
