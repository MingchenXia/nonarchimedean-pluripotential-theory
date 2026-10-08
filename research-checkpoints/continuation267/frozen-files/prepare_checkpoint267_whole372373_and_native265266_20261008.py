from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation267-publication-records';M=G/'upload-manifest-continuation267.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation266.json')
assert prior['commit_sha']=='9997cf100c282b298c3adeb5026ea7370a5decb4'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
 x=load(R/n);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==266
 assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
proofs=[
 (K/'public-P21.3-continuation372-middle-cone-repair-and-logarithmic-analytic-trace-removability-whole-candidate', 'P21.3-review-paper.tex','e79447669e2993eaada48dbd563c1cf862cee1ac1ed72afbef36844294aae8a0','whole-proof.md','a29472f1d9dcb2d4e9c4c12d0f75071735bc4eef51245b4c477b03d551777307',K/'P21.3-round263-whole-candidate372-ROOT-proof-source-scope-and-binding-20261008.json','b3a04b9dabd91b4adc1a86732e058af5242081a739068216167952510ef29cdd'),
 (K/'public-P16.7-continuation373-explicit-analytic-torus-bounded-products-and-off-skeleton-atom-whole-candidate','P16.7-paper.tex','6dd117429234c002108ba2d03a36d878242561965022fab98ef72feb966895ec','whole-proof.md','ae4ff5a5c77ae98b0bb980d5388ed37a018ce87e860c794e2620570dc862c15a',K/'P16.7-round264-whole-candidate373-ROOT-proof-source-scope-and-binding-20261008.json','5766d79cf35898c09a255ee88ce126bb85e08e642c2e57ff5e757e5aad65edd4')]
for d,t,ts,p,ps,b,bs in proofs:assert sha(d/t)==ts and sha(d/p)==ps and sha(b)==bs
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
def freeze(p):
 p=Path(p);rel=p.relative_to(R)
 assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True)
 assert not dst.exists();shutil.copyfile(p,dst);assert sha(dst)==sha(p)
for q,expected_input in [(265,'9a7d672ec1a4ca88ef10dc0226bc7b37a18155feabacd6c085fb4f42ab89bae3'),(266,'76d391127e7b462226c723dccd7e9a7f2b42108a5ae551b669a9470799bb335d')]:
 C=next((R/f'campaigns/round-{q}').iterdir());assert sha(C/'input.json')==expected_input
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed']
 write(S/f'round{q}-public-native-status.json',st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
 for p in sorted(C.glob('*.json')):freeze(p)
 for p in sorted((C/'immutable-mathematical-DATA').rglob('*')):
  if p.is_file():freeze(p)
 if (C/'whole-book-context-DATA').exists():
  for p in sorted((C/'whole-book-context-DATA').rglob('*')):
   if p.is_file():freeze(p)
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for d,t,ts,p,ps,b,bs in proofs:
 for f in sorted(d.rglob('*')):
  if f.is_file():freeze(f)
 freeze(b)
helpers=['capture_completed_native263264_20261008.py','stage_completed_native263_whole372_ROOT_20261008.py','stage_completed_native264_whole373_ROOT_20261008.py','prepare_native265_whole370_and_test_ideal371_20261008.py','launch_frozen_native265_whole370371_checked_initialization_20261008.py','prepare_native266_original_P02_1_classical_regularization_20261008.py','launch_frozen_native266_original_P02_1_checked_initialization_20261008.py','record_verified_checkpoint266_20261008.py','fetch_public_analytic_torus_primary_books_20261008.py']
for n in helpers:freeze(R/n)
freeze(G/'push-receipt-continuation266.json');freeze(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py');freeze(Path(__file__))
retrieval=R/'primary-data-LOCALONLY/P16.7-period-algebraization-primary-20261008/public-primary-retrieval-records.json'
shutil.copyfile(retrieval,F/'public-period-book-retrieval-metadata.json')
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
 whole372='ENTIRE native263 actual FINAL ALL4fields, whole72653byteTex/71103byteproof and complete ROOT proof/source/scope binding; all31source application metadata. MiddlePSD cone repairs old367/368 strong-cone domination gap. Entire new logarithmic analytic trace removability proof still assumes off-locus ordinary smooth zero Hessian and local smooth zero-Hessian trace on ordinary analytic Z. Original arbitrary continuous psh pair/arbitrary positive closed T remains OPEN.',
 whole373='ENTIRE native264 actual FINAL ALL4fields, whole35934byteTex/35317byteproof/source ledger/verdict and complete ROOT binding. Explicit strict proper analytic torus period obstruction, restricted bounded products/comparison, off-skeleton actual atom mass1, separable circle solutions/envelopes/duality. Period symmetry obstruction is not nonalgebraizability without full classification/ampleness/algebraization proof. Full intrinsic psh/E1/finite-energy arbitrary measure equation unresolved; original P16.7 OPEN.',
 qualifications='ROOT independently physically read ENTIRE372/373 proof/Tex/actual final/source application metadata. ROOT freshly read CLD1.2.6 and1.2.11--13 complete immediate proofs for372, CLD8.5.1 andB6 full immediate explanatory unit for373. Other native whole source readings attributed native, retained hashes not new ROOT reading. MIDDLE6.5.2 required in arbitrary ambient moment dimension; analytic dimension2 alone does not imply ambient strong/middle coincidence. Historical367/368 strong cone step needs repair, preserved originals remain unaccepted.',
 campaigns='TWO Xean signed-in native Codex gpt-6.1-sol xhigh independent campaigns:265 ENTIRE370/371 source/scope reconstruction and actual smooth PRIMARY model gate;266 ONE original P02.1 arbitrary classical psh realPL regularization with whole older qualified data and exact original. No ACTIVE mathematical output read or hot feedback. Entire frozen mathematical packets/tasks/settings/input/launch metadata published; primary bodies/pixels LOCALONLY.',
 compiler='Requests125/370,146/371,178/372 pending with NO diagnostics or success;373 source preserved unverified. Protected P16.4 editor OPEN UNCHANGED, no new tab or replacement PDF.',
 no_acceptance_or_count_increase=True,primary_bodies_pixels_LOCALONLY=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,protected_editor_open_unchanged=True)
write(F/'publication-qualification.json',qual)
(F/'README.md').write_text('''Checkpoint267: whole middle-cone and analytic-torus working papers; two independent campaigns

16/42 original problems solved,26OPEN,97 accepted papers. No new original closure or paper acceptance.

Entire372 reconstructs all prior P21.3 proofs after replacing the invalid strong-cone domination step by the middle positive cone. Its new analytic trace removability proof applies to an ordinary analytic closed locus with an ordinary smooth zero-Hessian trace and an ordinary smooth zero-Hessian function away from the locus. This does not yet cover all arbitrary continuous psh differences and all positive double-closed currents of originalP21.3. Historical367/368 originals remain preserved and unaccepted; their strong-cone step needs the disclosed repair.

Entire373 gives an explicit strict proper analytic two-torus, a period symmetry obstruction, a restricted bounded product/comparison theory, an actual off-skeleton Monge--Ampere atom of mass1, and separable circle solutions/envelopes/duality. It does not yet prove nonalgebraizability by complete polarization classification/algebraization, or full intrinsic psh/finite-energy existence and uniqueness for arbitrary analytic measures. P16.7 remains OPEN. Public book retrieval attempts failed; no unavailable theorem imported. Both entire mathematical papers and source/scope/ROOT bindings are retained; full primary bodies and PDF pixels stay LOCALONLY.

Two signed-in Xean native Codex gpt-6.1-sol xhigh campaigns continue:265 independently reconstructs ENTIRE370 and371 and tests actual smooth primary model construction;266 addresses ONE originalP02.1 arbitrary classical curve-test psh realPL regularization. Their entire frozen mathematical packets, tasks, input/settings and launch metadata accompany this checkpoint. No active mathematical output reading or hot feedback, at most TWO campaigns, supplied programs inert DATA never executed/imported. No successful compiler diagnostics yet. Protected P16.4 editor remains OPEN UNCHANGED. Authorized regular NONFORCE checkpoint requires independent Git tree/all blob/fresh reference verification.
''')
for n in ['active-work.json','checklist-current.json']:
 p=R/n;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=267,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint267 whole372/373 and frozen265/266. Continue TWO native265/P12.3 and266/P02.1; inspect ONLY settled COMPLETE outputs. Next freed slot ENTIRE372 or373 independent reconstruction, authenticate complete period classification/ampleness/algebraization proof.16solved26OPEN97papers; protected editor OPEN UNCHANGED; no active output reading/hot feedback.');write(p,x);shutil.copyfile(p,F/n)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
 if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation267/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:
 p=F/n;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+n,bytes=p.stat().st_size,sha256=sha(p)))
assert len({x['path'] for x in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole middle-cone and analytic-torus proofs with two independent campaigns',scope='16solved26OPEN97papers. Entire372/373 mathematical papers/actual finals/source metadata/ROOT bindings remain unreviewed. Strong cone gap repaired by middlePSD; analytic trace hypothesis explicit. Period obstruction not yet nonalgebraizability or full finite-energy equation. Whole frozen265/266 launch/input/math tasks, maxTWO; source bodies/pixelsLOCALONLY. No count increase/hot feedback.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
