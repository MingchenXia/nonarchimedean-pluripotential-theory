from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation263-publication-records'; M=G/'upload-manifest-continuation263.json'
P=K/'P21.3-continuation367-closed-smooth-multipliers-working-paper-20261008.tex'
B=K/'P21.3-continuation367-ROOT-whole-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def bound(p):
 p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not M.exists() and not F.exists() and not B.exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
prior=load(G/'push-receipt-continuation262.json')
assert prior['commit_sha']=='c21d636c36c7a1e09639bbf264dad6f37ee4f06d'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
for name in ['active-work.json','checklist-current.json']:
 x=load(R/name);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==262
 assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
source=K/'public-P16.1-round-68-final-reader/sources'
assert sha(source/'CLD-pdf.pdf')=='5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719'
assert sha(source/'CLD-literal_extract.txt')=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
now=datetime.now(timezone.utc).isoformat()
write(B,dict(recorded_utc=now,atom='P21.3',whole_working_paper=bound(P),status='WHOLE ROOT working proof; independent reconstruction pending; no correctness grant',
 ROOT_reading=dict(entire_final_tex_physically_read=True,method='Whole final manuscript printed completely after scalar signed-measure proof repair; earlier whole print in overlapping bounded chunks retained as history.',
 mathematical_review='Scalar signed-Radon-measure uniqueness proves smooth wedge/continuous multiplier associativity and annihilator inheritance. General current Leibniz, including nonclosed hT, eliminates both first-order cross terms and Da term using double closedness of aT. Fixed-current locally uniform NET limit tested against each compact D omega. Actual Q_p analytic torus gives nonzero calibrated integral; its weighted current is NOT doubly closed and is NOT a P21.3 counterexample.'),
 private_primary_sources=[bound(source/'CLD-pdf.pdf'),bound(source/'CLD-literal_extract.txt')],
 source_identity='Locally preserved authentic complete arXiv1204.6277v2 PDF/text, header25July2025/body29July2025; no fresh retrieval or pixel-reading claim.',
 whole_immediate_primary_units_read=['CLD5.8.1--5.8.6 statements/constructions/proofs','CLD6.2.5--6.2.8 statements and entire immediate proofs, recursive appendix background disclosed',
 'CLD7.2.9--7.2.12 whole positivity proof/function-current/measure multiplication','CLD7.3.1 integration construction','CLD7.7.1--7.7.7 complete differential identities and immediate proofs',
 'CLD8.6.1--8.6.7 definition/locality/integration/smooth-closed-factor/weak-limit/literal flawed unrestricted multiplier assertion',
 'CLD14.3.1--14.3.5 entire canonical calibration/positive proof','CLD14.5.3 entire degree calibration statement/proof through before14.5.4',
 'CLD15.7.1 entire immediate analytic-to-tropical theorem/proof'],
 whole_book_DATA=bound(R/'book-source/manuscript/parts/part2/ch16_bedford_taylor.tex'),
 existing_book_warning='Chapter16 already restricts multiplier corollary to nonnegative LOCALLY CONSTANT and warns literal CLD8.6.7 lacks closedness; explicit detecting analytic test adds detail but is not a new original counterexample.',
 exact_theorem_scope='ANY restriction-compatible prescribed class of finite continuous potentials; no identification classical psh with locally uniformly generated CPsh. Initial T explicitly BT. For smooth a>=0, aT BT IFF aT doubly closed IFF d\u2032a wedge T=d\u2032\u2032a wedge T=0. Continuous conclusion requires local uniform approximants EACH of whose a_iT is closed.',
 exclusions=['No recognition/density theorem for arbitrary positive doubly closed current','No construction of closed smooth approximants for arbitrary continuous closed multiplier','No product of two nonsmooth current factors','No global inverse-image or nonpure current counterexample','No original P21.3 closure','No accepted-paper/count increase','No successful compilation or formal-verification claim'],
 original_closed=False,new_accepted_paper=False,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
 future_independent_reconstruction_only=True,active_native262_input_unchanged=True,new_math_sent_to_ACTIVE_campaign=False,
 source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,primary_bodies_pixels_LOCALONLY=True,protected_editor_open_unchanged=True))
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
for q in [261,262]:
 C=next((R/f'campaigns/round-{q}').iterdir());f=load(C/'freeze.json')
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
  assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
 for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
  for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed']
 p=S/f'round{q}-public-native-status.json';write(p,st)
 items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
write(F/'publication-qualification.json',dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
 native262='Entire original P21.3 byte-identical to historical104, ZERO correctness grants,21whole math637990bytes/38privateprimary/4wholebookcontexts. Native signed-in gpt-6.1-sol xhigh initialized with database/public status. Active output unread; complete immutable original/task/math/launch published here.',
 ROOT367='ENTIRE unreviewed ROOT working paper, whole proof/source/scope binding. Exact closed smooth weighting criterion and fixed-current closed-approximation NET closure plus explicit analytic torus failure of unrestricted weighting. Original remains OPEN. Kept for FUTURE independent reconstruction; not supplied to ACTIVE262.',
 counts='16solved26OPEN97accepted; existing P05.2/paper90 stale target flag reconciled without any new acceptance/count increase.',
 compiler='New367 compiler submitted asynchronously; no success result and source repaired after initial submission, so no compilation success is asserted for this final frozen manuscript. Prior366 compiler handle lost across environment transition; unverified.',
 primary_bodies_pixels_LOCALONLY=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,protected_editor_open_unchanged=True))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);x.update(updated_utc=now,current_active_batch=active,
 current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),
 ROOT367_unreviewed_closed_multiplier=dict(whole_paper=bound(P),whole_proof_source_scope_binding=bound(B),original_closed=False,new_accepted_paper=False,held_for_future_independent_reconstruction=True,no_ACTIVE_feedback=True),
 github_pending_checkpoint=dict(continuation=263,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),
 next_work='Verify regular NONFORCE checkpoint263 whole frozen262 original/math/zero grants and whole unreviewed367. Continue261/262, inspect only settled complete outputs, future independent reconstruction of367, max TWO campaigns.16solved26OPEN97papers; protected editor unchanged; compiler unverified.')
 write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('''Checkpoint263: arbitrary-current P21.3 research and closed smooth weighting

16/42 original problems solved,26OPEN,97 accepted papers. Entire original P12.6 was accepted at checkpoint262. P05.2/paper90 metadata target flag is reconciled with its existing full acceptance; no new count increase.

Native262 is initialized on the signed-in Xean Codex gpt-6.1-sol xhigh path. Its entire P21.3 original is unchanged from historical104; no correctness grants are supplied. The full21mathematical files637990bytes and immutable original/task/input/settings/source bindings/launch are published. Complete CLD and other primary source bodies remain LOCALONLY. Current native261 continues the general normal positive-envelope P12.3 problem. At most TWO campaigns; no active mathematical output reading or feedback.

Whole unreviewed ROOT367 proves the smooth nonnegative multiplier criterion for an explicitly BT initial current: aT is BT exactly when aT is doubly closed. The complete signed-measure and distributional calculation does not approximate nonsmooth h or assume hT is closed. A locally uniform NET result requires EVERY smooth approximant times the FIXED current to be closed. A real Q_p analytic torus with a=2+(-log|T1|)^2 has a compact calibrated test giving 2 times a positive Lebesgue integral; the resulting a delta_X is not doubly closed and is therefore NOT a counterexample to original P21.3. The book already notes the unrestricted multiplier source defect. This paper supplies no arbitrary-current recognition/density, no universal closed approximation, no original closure, and no accepted-paper increase. It is frozen for a FUTURE independent reconstruction and has not been fed to ACTIVE262.

No successful compilation/formal verification claim. Protected P16.4 editor stays OPEN UNCHANGED, no new tabs. Source and supplied programs are DATA; supplied programs never executed. User-authorized regular NONFORCE publication verified by independent native Git tree, all blob bindings, and fresh remote reference.
''')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R)
 assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 target=target or 'research-checkpoints/continuation263/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for p in sorted(F.rglob('*')):
 if p.is_file():add(p)
add(P);add(B);add(K/'existing-P05.2-original332-flag-reconciliation-after-checkpoint262-20261008.json')
C=next((R/'campaigns/round-262').iterdir())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:add(C/name)
for e in load(C/'mathematical-packet-bindings.json'):add(e['path'])
for name in ['prepare_native262_entire_original_P21_3_arbitrary_current_20261008.py','launch_frozen_native262_P21_3_original_checked_initialization_20261008.py',
 'record_verified_checkpoint262_and_reconcile_existing_P05_2_flag_20261008.py']:add(R/name)
add(G/'push-receipt-continuation262.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
 fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,
 commit_message='Checkpoint whole arbitrary-current P21.3 campaign and closed smooth multiplier working proof',
 scope='16solved26OPEN97papers. Full immutable262 original/math with zero grants; entire unreviewed367 conditional proof and source scope. No active feedback, no original closure/count increase. Source bodies/pixels LOCALONLY.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),whole_working_paper=bound(P),active_rounds=active,solved=16,open=26,papers=97),indent=2))
