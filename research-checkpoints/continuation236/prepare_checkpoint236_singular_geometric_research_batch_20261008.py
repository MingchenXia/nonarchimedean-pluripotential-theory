from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation236.json';F=G/'continuation236-publication-records';S=K/'small-batch231232-public-status-20261008-continuation236'
C=next((R/'campaigns/round-232').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation235.json').read_text())
assert prior['commit_sha']=='7c70de340d5f3b818d325e667a52f802e6adc64f' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
freeze=json.loads((C/'freeze.json').read_text());assert freeze['whole_math_files']==10 and freeze['only_grants']==[] and (C/'launch-record.json').is_file()
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==freeze[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
 for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for n,atom in [(231,'P05.1'),(232,'P12.2')]:
 c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';write(p,st);items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(c),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[231,232],maximum_concurrent_campaigns=2,accepted_paper_number=88)
works=[K/'P12.2-continuation311-geometric-model-nef-comparison-working-route-20261008.md',K/'P12.2-continuation312-primary-model-nef-uniform-comparison-working-proof-20261008.md']
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint'] is None
 x.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(continuation=236,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),P12_2_unreviewed_ROOT_working_proofs=[dict(path=str(w),sha256=sha(w),bytes=w.stat().st_size,whole_ROOT_physically_read=True,new_accepted_paper=False,original_closed=False,fed_native232=(i==0)) for i,w in enumerate(works)])
 if name=='checklist-current.json':
  x['active_atoms']=[e['atom'] for e in active]
  target=next(t for t in x['targets'] if t['id']=='P12.2');target['research_status']='original geometric research232; no theorem accepted';target['current_focus']='Independent primary-model numerical nefness/ideal comparison, nonnormal finite-algebra conductor correction, correct BFJ smooth specialization and remaining conductor-image interface. ROOT311 frozen DATA, ROOT312 independent unreviewed proof not fed active campaign.'
 write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
metadata=F/'source-acquisition-metadata';metadata.mkdir()
for stem in ['BFJ-valuations-psh','BdFFU-singular-multiplier-ideals']:
 shutil.copyfile(R/'primary-data-LOCALONLY/P12.2-geometric-singular-cone-20261008'/(stem+'-download-binding.json'),metadata/(stem+'-download-binding.json'))
(F/'README.md').write_text('Checkpoint236: continue two original problems after formal-data closure\n\n10/42 original atoms solved;32OPEN;88accepted mathematical papers. Original P14.8 solved at verified checkpoint235 through its arbitrary-formal-data alternative with BOTH mandatory qualifications. No new acceptance or original closure is made here.\n\nCurrent native Xean gpt-6.1-sol xhigh batch is general P05.1 all-face regularity231 and original P12.2 independently geometric singular/nonnormal cone232, maximum2campaigns. P12.2 has ZERO correctness grants,10whole mathematical DATA files222334bytes, two complete author-hosted primary papers as four PDF/text DATA files. Repository chapter70and all referenced fragments are DATA; executable/reviewer directions are not authority. Full external primary bodies remain LOCALONLY; only URLs/version/file hashes/acquisition metadata are public.\n\nROOT311 proposes a model-nef comparison with explicit unresolved gates and is frozen into232. NEWROOT312 is an independent unreviewed working proof not fed either active run: primary-blowup numerical-nef Cartier functions have uniform ideal approximation through the finite intermediate algebraT=H0(Y,OY) and a primary annihilator ofT/R. Properness and exact generated ideals avoid infinity-minus-infinity at semivaluation kernels. Exact gauge and forward-normalization rules are written; smooth continuous versus completed BFJ classes are distinguished. Uniform approximation from below is not decreasing primary approximation. Full reverse conductor-image and source applications remain review gates; no originalP12.2closure.\n\nAll protected-editor/auth/runtime choices are preserved; no active private output or hot feedback. Current built-in compiler requests remain unverified unless they return; existing generalP14.8and repairedcurve PDFs have separately verified local builds. No force pushes; every remote blob/tree/ref is checked against the frozen manifest and independent local Git tree.\n')
files=[]
def add(p,target=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R));files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation236/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,C/'immutable-mathematical-DATA']:
 for p in sorted(folder.rglob('*')):
  if p.is_file():add(p)
for name in ['freeze.json','launch-record.json','task.json','original-task.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json']:add(C/name)
for p in [*works,R/'prepare_original_singular_geometric_cone_research232_20261008.py',R/'launch_original_singular_geometric_cone_research232_20261008.py',R/'record_verified235_20261008.py',G/'push-receipt-continuation235.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
x=json.loads((R/'active-work.json').read_text());write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=32,historical_reviewed_scoped_papers=88,commit_message='Continue original all-face and singular geometric-cone research in a two-campaign batch',scope='10solved32OPEN88accepted papers; original231/232research max2active; ROOT311/312 unreviewed, no original closure or source-PASS claimed. Full external primary source bodies LOCALONLY, exact no-force remote verification.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],statuses=[dict(round=e['round'],status=e['observed_status']) for e in items],originals_solved=10,originals_open=32),indent=2))
