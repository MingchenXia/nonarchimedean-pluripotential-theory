from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation237.json';F=G/'continuation237-publication-records';S=K/'small-batch233234-public-status-20261008-continuation237'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation236.json').read_text());assert prior['commit_sha']=='8b7750a07a9f54d7a20ff7f552671994bcb8ae1c' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
campaigns=[]
for n in [233,234]:
 C=next((R/f'campaigns/round-{n}').iterdir());f=json.loads((C/'freeze.json').read_text());assert (C/'launch-record.json').is_file()
 for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==f[key]
 for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
  for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
 if n==233:assert f['structured_imported_notes_count']==5 and [x['id'] for x in json.loads((C/'input.json').read_text())['notes']]==f['only_grants']
 else:assert f['only_grants']==[] and f['whole_math_files']==20
 campaigns.append(C)
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for n,atom in [(231,'P05.1'),(232,'P12.2'),(233,'P05.1'),(234,'P12.2')]:
 C=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';write(p,st);items.append(dict(round=n,atom=atom,observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(C),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[233,234],maximum_concurrent_campaigns=2,accepted_paper_number=88)
drafts=[next(K.glob('public-P05.1-continuation313-*')),next(K.glob('public-P12.2-continuation316-*'))]
works=[K/'P12.2-continuation314-completion-and-smooth-specialization-interface-working-proof-20261008.md',K/'P05.1-continuation315-costed-dual-and-all-carrier-multiplier-working-proof-20261008.md']
for D,cell in zip(drafts,[332,333]):
 p=D/'ROOT-public-draft-status-20261008.json';x=json.loads(p.read_text());x.update(built_in_compiler_status='requested; completion unverified at checkpoint freeze',built_in_compile_cell=cell,editor_new_tab_not_opened=True);write(p,x)
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['remaining_open_original_atoms']==32 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint'] is None
 x.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(continuation=237,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),unreviewed_new_original_drafts_313_316=[dict(path=str(D),source_status=str(D/'ROOT-public-draft-status-20261008.json'),new_accepted_paper=False,original_closed=False) for D in drafts],native233_registered_qualified_support_count=5,native234_zero_grants=True,unreviewed_new_ROOT_working_proofs_314_315=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,whole_ROOT_physically_read=True,fed_native234=(i==0),fed_native233=False,new_accepted_paper=False,original_closed=False) for i,p in enumerate(works)])
 if name=='checklist-current.json':
  x['active_atoms']=[e['atom'] for e in active]
  for atom,focus in [('P05.1','Original simultaneous all-face feasibility/classification research233 with FIVE FULL qualified imported Notes. Unregistered231 draft313 is DATA; ROOT315 costed Banach-dual/carrier multiplier route is unreviewed and not fed active233.'),('P12.2','Original unbounded geometric class/full smooth BFJ and general conductor research234, ZERO grants. Completed232 bounded comparison draft316 remains unreviewed; corrected zero/unit and conductor topology retained. ROOT312/314 are frozen unreviewed DATA.')]:
   t=next(t for t in x['targets'] if t['id']==atom);t['research_status']='original research active; latest draft unreviewed';t['current_focus']=focus
 write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint237: registered support and substantive original continuations\n\n10/42 original atoms solved;32OPEN;88accepted mathematical papers. No acceptance or original closure is made here.\n\nP05.1 native231 produced a complete13-page scoped draft but its Xean role was BLOCKED because ROOT omitted the accepted supporting Notes from input.notes. Preserve the actual FINAL and failed history. Native233 now registers FIVE complete trusted scoped Note bodies with ALL mandatory annotations, checks=[] without invented modelPASS; its new research targets simultaneous all-face feasibility/classification. Draft313 remains UNREVIEWED DATA.\n\nP12.2 native232 completed valid registration and produced a14-page bounded numerical-Cartier/ideal comparison and isolated descent draft316, candidatefalse. ROOT physically read its entire authoritative source, actual fourFINAL notes, source/scope/coverage/decision and verified44ownhashes. This is not independent mathematical acceptance. Mandatory correction: only the infinite-conductor-value stratum is closed; the finite-value complement is open. Native234 uses ZERO grants to advance the full unbounded geometric class, corrected BFJ zero/unit smooth specialization and general conductor image.\n\nROOT314 independently gives the proposed primary completion homeomorphism and corrected smooth decreasing-class comparison; it is frozen UNREVIEWED DATA into234. ROOT315 gives a costed weak-star PCC cone and finite all-carrier multiplier criterion for REAL regularization, retaining allC_b/nonseparable duals; it is UNREVIEWED and not fed active233. Neither is counted as an original solution.\n\nMaximum2nativecampaigns; public statuses only during active work, no hot feedback or private active output. ProtectedP16.4 editor unchanged and kept open; new313/316builtincompile requests332/333 remain unverified at freeze. Full external primary PDF/text/page images LOCALONLY. All uploaded materials are user-authorized. No force update; exact remote blob/tree/ref verification follows the frozen manifest.\n')
files=[]
def add(p,target=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R));files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation237/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,*drafts]:
 for p in sorted(folder.rglob('*')):
  if p.is_file():add(p)
for C in campaigns:
 for name in ['freeze.json','launch-record.json','task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
  add(C/name)
 if (C/'qualified-imported-note-bindings.json').is_file():add(C/'qualified-imported-note-bindings.json')
 for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):add(e['path'])
extras=[*works,K/'round231-unregistered-actual-native-final.json',K/'round231-unregistered-final-and-reference-failure-binding-20261008.json',K/'round231-whole-draft-ROOT-reading-and-next-research-20261008.json',K/'round232-actual-native-final.json',K/'round232-whole-draft-ROOT-reading-binding-and-qualifications-20261008.json',G/'push-receipt-continuation236.json']
for name in ['extract_unregistered_native231_and_bind_reference_failure_20261008.py','prepare_original_balanced_simultaneous_research233_20261008.py','launch_original_balanced_simultaneous_research233_20261008.py','capture_completed_singular_geometric_research232_20261008.py','prepare_original_singular_unbounded_descent_research234_20261008.py','launch_original_singular_unbounded_descent_research234_20261008.py','stage_unreviewed_all_face313_and_numerical316_20261008.py','record_verified236_20261008.py']:extras.append(R/name)
for p in [*extras,Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
x=json.loads((R/'active-work.json').read_text());write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=32,historical_reviewed_scoped_papers=88,commit_message='Register full qualified supports and continue original all-face and unbounded singular-cone research',scope='10solved32OPEN88accepted; draft313/316 unreviewed, native231 failed registration retained, native233/234 max2active; ROOT314/315 working proofs, no source-PASS or new original closure.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],statuses=[dict(round=e['round'],status=e['observed_status']) for e in items],originals_solved=10,originals_open=32),indent=2))
