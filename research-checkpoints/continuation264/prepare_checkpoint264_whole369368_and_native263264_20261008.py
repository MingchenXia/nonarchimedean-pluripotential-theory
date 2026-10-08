from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation264-publication-records';M=G/'upload-manifest-continuation264.json'
D=K/'public-P21.3-continuation369-arbitrary-current-cutoff-and-analytic-locus-removability-whole-candidate'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bound(p):return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation263.json')
assert prior['commit_sha']=='d29dda3225f257f7a728dcc56e6cf945313d4da7'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 x=load(R/name);assert x['current_active_batch']==[263,264] and x['github_pending_checkpoint'] is None
 assert x['latest_verified_github_checkpoint']['continuation']==263
 assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
assert sha(D/'actual-native262-final.json')=='49b00d775106e0878d30573db2282ca2b280b9e648e0ac9684fce1326b8ec308'
assert load(D/'actual-native262-final.json')['candidate'] is False
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[];campaigns=[]
for q in [263,264]:
 C=next((R/f'campaigns/round-{q}').iterdir());f=load(C/'freeze.json');campaigns.append(C)
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
  assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
 for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
  for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
 assert load(C/'input.json')['notes']==[]
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed']
 p=S/f'round{q}-public-native-status.json';write(p,st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
 whole369='Native262 completed original P21.3 candidateFALSE. Whole paper/proof, ALL3 actual FINAL fields and separate ALL3 differing expanded fields, full source-application metadata and scope/coverage preserved. ROOT physically read ENTIRE proof/Tex/actual/expanded/source application and exact CLD6.5.2/15.2.1 immediate source proofs; other source reading accurately attributed native. Whole literal16-unit primary evidence remains LOCALONLY. No original closure or new accepted paper.',
 whole368='Whole unreviewed ROOT relative smooth form factor proof; actual gamma wedge T must be positive/doublyclosed. Full measure compatibility and graded Leibniz, cross-term elimination, fixed-current/common-chart closed-approximation NET proof. No arbitrary-current recognition or nonsmooth form wedge theorem.',
 native263='Whole independent reconstruction of ALL369/367/368 plus ENTIRE unchanged P21.3;50math942138bytes39privateprimary4bookcontexts,ZERO grants.',
 native264='Original P16.7 nonalgebraizable analytic finite-energy equation theory, unchanged whole family10 literal task;21math508797bytes22privateprimary17wholebookcontexts,ZERO grants. Genuinely nonalgebraizable datum/all-support operator and all variational inputs required. Invariant skeleton endpoint insufficient.',
 native261='Completed candidateFALSE, ALL14 actual FINAL fields captured and ROOT read. Full expanded proof/Tex review ongoing; not yet accepted or supplied to ACTIVE campaigns.',
 compilation='ROOT367 asynchronous built-in compiler remains unresolved; source changed after initial submission, so no compilation success is asserted for frozen final version. No new tabs.',
 primary_bodies_pixels_LOCALONLY=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=264,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint264 full369/368 and frozen native263/264 inputs. Finish whole native261/P12.3 ROOT review, no original/count increase. At most TWO campaigns, no active math/hot feedback; protected editor OPEN UNCHANGED.')
 for field in ['native261_whole_original_independent_completion','native262_original_P21_3_research']:
  if field in x:x[field]['status']='COMPLETED settled candidateFALSE; whole output read/reconstruction status tracked separately'
 write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('''Checkpoint264: full arbitrary-current removability draft and next small batch

16/42 original problems solved,26OPEN,97 accepted papers. No new acceptance/count increase in this checkpoint.

Full native262/P21.3 manuscript369 gives a compact middle-positive coefficient-measure estimate, weighted cutoff criterion, and ordinary analytic-locus removability under the exact strict dimension bound dim Z<n-p-1 AND smooth zero-Hessian off Z. Neither arbitrary pair/current cutoff exhaustion nor unrestricted original P21.3 is proved. All actual returned3notes differ from3expanded local notes: both entire versions are preserved separately. Full proof/Tex/application/scope/coverage were ROOT read, and CLD6.5.2/15.2.1 whole immediate source proofs checked; other native source reading is accurately attributed. Whole literal primary bodies/pixels remain LOCALONLY.

Whole ROOT368 treats relative smooth(r,r)-form factors gamma: for an explicitly BT initial T, gamma wedge T is BT exactly when the ACTUAL product is positive and doubly closed. The full proof supplies continuous scalar compatibility, annihilator inheritance and both graded cross-term cancellations, plus coefficient-NET closure for smooth limits. It does not construct arbitrary-current closed approximation. Whole ROOT367 already frozen at263 is supplied with368/369 to the next independent reconstruction.

Native263 independently reconstructs ALL three entire manuscripts and attempts ENTIRE original P21.3. Native264 starts ORIGINAL P16.7 on genuinely nonalgebraizable analytic spaces with explicit positivity and intrinsic/all-support finite-energy operator/equation. Restricting to an invariant skeleton alone cannot complete P16.7. Both use the existing signed-in Xean native Codex gpt-6.1-sol xhigh path with ZERO incoming grants, at most TWO concurrent campaigns. Full immutable math/original/task/source bindings/settings/launch records are published. Active math/output unread and no hot feedback. Native261 has settled candidateFALSE and its complete14actual FINAL fields have been read; expanded whole draft review continues separately.

No successful compilation or formal proof certification claimed. Protected P16.4 editor OPEN UNCHANGED, no new tabs. Supplied programs inert DATA never executed/imported. Authorized regular NONFORCE publication verified by independent native Git tree, all blob bindings and fresh remote reference.
''')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 target=target or 'research-checkpoints/continuation264/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for p in sorted(F.rglob('*')):
 if p.is_file():add(p)
for p in sorted(D.rglob('*')):
 if p.is_file():add(p)
for name in ['P21.3-round262-whole-candidate369-ROOT-proof-source-scope-and-binding-20261008.json','P21.3-continuation368-relative-closed-smooth-form-factor-whole-working-proof-20261008.txt','P21.3-continuation368-ROOT-whole-proof-source-scope-and-binding-20261008.json']:add(K/name)
for C in campaigns:
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:add(C/name)
 for e in load(C/'mathematical-packet-bindings.json'):add(e['path'])
for name in ['prepare_native263_whole_removability369_and_closed_factors367368_20261008.py','launch_frozen_native263_whole369_and_closed_factors_checked_initialization_20261008.py','prepare_native264_original_P16_7_nonalgebraizable_20261008.py','launch_frozen_native264_original_P16_7_checked_initialization_20261008.py','capture_completed_native262_20261008.py','stage_completed_native262_whole_removability369_ROOT_20261008.py','record_verified_checkpoint263_and_bind_whole_relative_factor368_20261008.py']:add(R/name)
add(G/'push-receipt-continuation263.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=load(R/'active-work.json');write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole P21.3 removability draft and native P21.3/P16.7 small batch',scope='16solved26OPEN97papers. ENTIRE unreviewed369/368, separately preserved actual and expanded FINAL, full frozen263/264 original/math/zero grants and launches. No active feedback or original/count increase. Primary bodies/pixels LOCALONLY.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),current_active_batch=active,solved=16,open=26,papers=97),indent=2))
