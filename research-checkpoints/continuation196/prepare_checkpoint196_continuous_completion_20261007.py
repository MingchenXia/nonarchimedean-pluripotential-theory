from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation196.json'; F=G/'continuation196-publication-records'
S=K/'small-batch189191-public-status-20261007-continuation196'
D=K/'public-P05.2-continuation230-continuous-completion-and-envelope'
C=next((R/'campaigns/round-192').iterdir()); A=next((R/'campaigns/round-191').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation195.json').read_text())
assert prior['commit_sha']=='113664f5ec69c5d3296f6aba72ec2c410114e61a' and prior['files']==27
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
assert (A/'launch-record.json').exists()
assert sha(D/'P05.2-paper.tex')=='ffadbcedcb0eb49c893ae81f3d7696ef4cba25a9df6179644eedb7b51286cc3a'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (189,190,191):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n==190 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
assert next(x for x in items if x['round']==190)['observed_status']=='completed'
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,prepared_next_round=192,prepared_next_round_launched=False,focus='Independent189 whole genus-zero review and full-original191 actual field equation author. Settled190 new whole continuous-completion/envelope manuscript230 remains unreviewed; own checks/compiler/provenance reproduced. Exactly two complete accepted A224/B225 grants prepared for whole192 independent review, queued until a slot frees. No active input modified; no original closure.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==74 and j['remaining_open_original_atoms']==33
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=196,status='prepared_for_authorized_push'))
    j['continuation230_unreviewed_continuous_completion']=dict(native_author_round=190,reader=str(D),source_sha256=sha(D/'P05.2-paper.tex'),source_lines=337,argument_lines=467,pdf_pages=13,whole_source_argument_notes_and_ledger_root_read=True,independent_review_round=192,independent_review_prepared_only=True,original_closed=False)
    j['current_original_field_author191']=dict(launch_record=str(A/'launch-record.json'),launch_record_sha256=sha(A/'launch-record.json'),full_original_scope_retained=True,only_mathematical_grants=['O217','D214','N220','T171','Q222','C218'],original_closed=False)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_accepted_papers=74,new_original_closure=None,new_independent_verdict=None,active_batch=[x['round'] for x in active],prepared_only_next_round=192,new_unreviewed_paper=230,paper_scope='Continuous completion of every finite-valued rational-endpoint PC function on finite positive balanced spaces, without boundedness premise; continuous unrestricted envelope for every bounded continuous obstacle. No general PA approximation/extended operator/contact classification.',primary_scope_diagnostic=231,full_third_party_sources_retained_locally_only=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[];seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
    remote=remote or 'research-checkpoints/continuation196/'+str(p.relative_to(R));assert remote not in seen;seen.add(remote)
    files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for d in (F,S):
    for p in sorted(d.iterdir()):add(p)
for name in ('P05.2-round190-completed-actual-author-result-20261007.json','P05.2-round190-native-model-final-partial-author-20261007.json','P05.2-round190-settled-partial-author-binding-20261007.json','P16.4-continuation231-relative-volume-whole-unit-scope-reading-20261007.json'):add(K/name)
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','notes.json','source-application-ledger.md','proof-audit.md','star-input.json','check_star_estimates.py','README.md','root-reproduction-binding-20261007.json','native-compiler-success-final-source-addendum-20261007.json','root-limited-pdf-visual-addendum-20261007.json'):add(D/name)
for name in ('native-artifact-provenance.json','native-star-check-output.json','star-check-output.json','native-build-summary.json'):add(D/'evidence'/name)
for name in ('task.json','original-task.json','argument.md','settings.json','freeze.json','mathematical-data-bindings.json'):add(C/name)
add(A/'launch-record.json')
for name in ('bind_and_reproduce_continuous_completion230_20261007.py','prepare_continuous_completion230_review192_20261007.py','launch_frozen_partial_review192_20261007.py','record_completion230_and_volume_scope231_20261007.py','record_verified195_20261007.py'):add(R/name)
add(G/'push-receipt-continuation195.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=74,commit_message='Preserve continuous PC completion and all-obstacle envelope draft',scope='Whole unreviewed native190 continuation230 thirteen-page paper: every finite-valued rational-endpoint PC function on every finite positive balanced rational space has a dominating continuous representative and exact usc hull; every actual continuous reference/bounded continuous obstacle unrestricted envelope is continuous, including nonseparable obstacles. Full337-line source,467-line argument, all3 canonical notes, ledger/proof audit read; exact native request/frozen input/source and all38 artifact hashes bound. Exact finite rational1035/2070 checks reproduced, two clean local builds, exact public native compiler SUCCESS, only pages1/13 visually read. No continuum certification from execution and no general PA/MA/contact/original closure. Whole independent192 review prepared/frozen ONLY with exactly two whole accepted A224/B225 grants and all clarifications. Full-original191 author launched after190 settled, only six older accepted grants and228 unreviewed data, max2active189/191. Primary231 whole BGMv1 application proof units confirm CE and singleton regularity antecedents remain; original higher-dimensional existence gaps open. No active private streams/DB reads or hot feedback.9/42 originals solved,33 open,74 accepted. Protected editor/auth/runtime unchanged; full third-party PDF bytes remain private.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],prepared_only_next_round=192,accepted_papers=74),indent=2))
