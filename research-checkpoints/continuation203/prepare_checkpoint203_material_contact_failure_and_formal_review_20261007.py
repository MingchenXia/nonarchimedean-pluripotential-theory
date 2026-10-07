from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation203.json';F=G/'continuation203-publication-records'
S=K/'small-batch197198-public-status-20261007-continuation203'
D=K/'public-P16.4-continuation250-direct-formal-recognition-and-target-bounds'
P=K/'public-P05.2-continuation247-finite-PA-contact-circuits-and-plane-counterexample'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation202.json').read_text())
assert prior['commit_sha']=='b5a63d3f7b6ec8f5b7e2dce86b51d9c3d9c8cfc1' and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['source_sha256']==sha(D/'P16.4-paper.tex') and b['root_pdf_sha256']==sha(D/'P16.4-paper.pdf')
assert b['root_local_build_exit_codes']==[0,0] and not b['root_local_final_warnings']
fail=K/'P05.2-round196-whole-finite-contact-FAIL-review-binding-20261007.json'
assert json.loads(fail.read_text())['verdict']=='FAIL'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (194,195,196,197,198):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n in (194,196,197) else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[i for i in items if i['unsettled_calls']>0];assert len(active)<=2
assert all(i['unsettled_calls']==0 for i in items if i['round'] in (194,195,196))
visual=D/'root-visual-and-builtin-request-scope-addendum-20261007.json'
assert not visual.exists()
visual.write_text(json.dumps(dict(recorded_utc=now,source_sha256=sha(D/'P16.4-paper.tex'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=18,root_actual_visual_read_pages=[1,18],whole_pdf_visually_read=False,source_preserved=True,root_local_build_exit_codes=[0,0],root_local_final_warnings=[],builtin_compiler_requested=True,builtin_request_cell='22',builtin_diagnostics_returned_at_checkpoint=False,builtin_success_claimed=False,independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,protected_editor_unchanged_open=True),indent=2)+'\n')
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,focus='197 unchanged original P05.2 after explicit material hypothesis correction and genuinely coupled endpoint construction;198 independent WHOLE18-page250 direct formal recognition/target-bound reader. Preserved196 FAIL; no new accepted paper or original closure.',native195_candidate=False,native195_continuation=250,completed196_verdict='FAIL')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==76 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,
        P16_4_latest_unreviewed_native195_paper=dict(continuation=250,directory=str(D),source_sha256=sha(D/'P16.4-paper.tex'),source_lf_lines=1320,argument_lf_lines=440,pdf_pages=18,exact_native_final_notes=6,all69_artifact_hashes_valid=True,all22_primary_bindings_valid=True,whole_root_read=True,local_build_exit_codes=[0,0],local_warnings=[],builtin_compilation_unverified=True,independent_reader_round=198,independent_verdict=None,new_accepted_paper=False,original_closed=False),
        P05_2_latest_material_repair249=dict(record=str(K/'P05.2-continuation249-PC-hypothesis-repair-and-coupled-plane-counterexample-working-proof-20261007.json'),source_sha256=sha(K/'P05.2-continuation249-PC-hypothesis-repair-and-coupled-plane-counterexample-working-proof-20261007.json'),status='Unreviewed explicit PC-hypothesis correction and genuinely coupled endpoint with proposed raw masses12,6,6/reference24/contact-3; failed247 source and196 verdict preserved.',author_round=197,mathematical_grant=False,new_accepted_paper=False,original_closed=False),
        P16_4_latest_degree_slope_M0_working248=dict(record=str(K/'P16.4-continuation248-degree-slope-M0-and-original-reference-working-proof-20261007.json'),sha256=sha(K/'P16.4-continuation248-degree-slope-M0-and-original-reference-working-proof-20261007.json'),status='Unreviewed curve degree-slope and conditional initial-reference/common-incidence M0 route; initial upstream primary application still pending.',mathematical_grant=False,new_accepted_paper=False,original_closed=False),
        github_pending_checkpoint=dict(continuation=203,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint203: material contact failure preserved; whole direct-formal manuscript under independent review\n\n9/42 originals solved,33 open,76 independently accepted partial/supporting papers. No new acceptance. Independent196 returned FAIL on unchanged247: strict affine floor omitted the PC hypothesis, and the endpoint was separable on cross times z. Preserve exact native/canonical review and failed source. ROOT249 explicitly changes the hypothesis and constructs a new coupled endpoint/reference, with raw candidate masses12,6,6/reference24/contact-3. Author197 must independently reconstruct it and continue the full original classification.\n\nNative195 candidate=false produced whole18-page250 paper. Complete1320-line TeX,440-line argument,73-line ledger and six exact registered notes read; all69 native hashes and22 original primary bindings valid. Fresh exact-source finite checks match and two local builds have no warnings. Root visually inspected only PDF pages1/18. Built-in compiler requested but no diagnostics at this checkpoint. Entire independent198 reader launched with exactly six whole accepted grants and all unchanged clarifications. General positive-genus and higher-dimensional original equations remain open.\n\nROOT248 degree-slope/conditional M0 and actual original-reference working route is unreviewed. Full third-party primary files, original dossier bodies, private inspection/stdout/SQLite and active streams remain private. At most two native61xhigh campaigns; protected current editor and native authentication retained.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation203/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.md','finite_checks.py','finite-checks.json','root-reproduction-binding-20261007.json','root-visual-and-builtin-request-scope-addendum-20261007.json','README.md'):add(D/name)
for p in sorted((D/'evidence').iterdir()):add(p)
for name in ('P16.4-round195-actual-registered-partial-author-result-20261007.json','P16.4-round195-exact-native-model-final-partial-author-20261007.json','P16.4-round195-whole-direct-formal-author-binding-20261007.json','P05.2-round196-actual-canonical-independent-FAIL-review-20261007.json','P05.2-round196-native-model-final-FAIL-review-20261007.json','P05.2-round196-whole-finite-contact-FAIL-review-binding-20261007.json','P05.2-continuation249-PC-hypothesis-repair-and-coupled-plane-counterexample-working-proof-20261007.json','P16.4-continuation248-degree-slope-M0-and-original-reference-working-proof-20261007.json'):add(K/name)
for name in ('independent-whole-paper-FAIL196-20261007.json','builtin-public-source-unverified-request-addendum-20261007.json'):add(P/name)
for n in (197,198):
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ('freeze.json','mathematical-data-bindings.json','launch-record.json'):add(c/name)
for name in ('bind_whole_finite_contact_FAIL196_20261007.py','write_coupled_contact_counterexample249_20261007.py','write_degree_slope_and_initial_reference248_20261007.py','retrieve_initial_residual_primary248_20261007.py','bind_and_reproduce_direct_formal250_20261007.py','prepare_original_polyhedral197_after_material_contact_repair_20261007.py','launch_frozen_original_polyhedral197_20261007.py','prepare_direct_formal250_review198_20261007.py','launch_frozen_direct_formal_review198_20261007.py','record_verified202_20261007.py'):add(R/name)
add(G/'push-receipt-continuation202.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=76,commit_message='Preserve contact proof failure and review direct formal recognition manuscript',scope='Whole196 independent FAIL with exact native/canonical/input bindings; explicit material PC hypothesis and genuinely coupled endpoint repair249 remains unreviewed. OriginalP05.2 author197 launched with three whole grants/all clarifications and4 private original primary files. Native195 candidate=false whole18-page250 direct same-bundle formal FS recognition, target estimates and alternative genus-zero equation preserved;1320LF Tex/440LF argument/73LF ledger/six exact native notes completely ROOT-read;69 native hashes and22 frozen primary bindings valid; exact finite checks reproduced, two clean local builds, ROOTPDF1/18 only visually read, builtin request unverified. Whole independent198 reader launched with six complete grants/all clarifications. Unreviewed248 degree-slope/conditional M0/original-reference route, pending upstream application. Full third-party files/original dossiers/private inspection/stdout/SQLite/active streams excluded.9/42originals solved33open76accepted, no new acceptance or original closure. Native61xhigh max2, no hot feedback, native auth/runtime and protected editor retained.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[i['round'] for i in active],accepted_papers=76),indent=2))
