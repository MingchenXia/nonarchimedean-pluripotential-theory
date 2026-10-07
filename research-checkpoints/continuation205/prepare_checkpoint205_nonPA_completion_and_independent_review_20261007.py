from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation205.json'; F=G/'continuation205-publication-records'
S=K/'small-batch199200-public-status-20261007-continuation205'
D=K/'public-P05.2-continuation255-coupled-nonPA-and-regularizable-raw-completion'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation204.json').read_text())
assert prior['commit_sha']=='1654908be98f945cdfbeda44cc44f8768b8595c6' and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert sha(D/'P05.2-paper.tex')==b['source_sha256'] and sha(D/'P05.2-paper.pdf')==b['root_pdf_sha256']
assert b['root_local_build_exit_codes']==[0,0] and not b['root_local_warnings'] and b['own_checker_reproduced']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat(); F.mkdir(); S.mkdir(); items=[]
for n in (197,198,199,200):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json'; p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n in (197,200) else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0]; assert len(active)<=2
assert all(e['unsettled_calls']==0 for e in items if e['round'] in (197,198))
alternate=[K/'P16.4-continuation254-bounded-Tate-normalization-and-finite-reference-fibres-working-proof-20261007.json',K/'P16.4-continuation254-domain-component-dominance-addendum-20261007.json']
recovery=dict(recorded_utc=now,environment_starting_observation_recovered=True,same197199_campaign_files_and_original_pids_observed_after_recovery=True,existing_native_campaigns_not_relaunched=True,no_auth_or_runtime_change=True,previous250_builtin_request_no_diagnostics_obtained=True,previous_functions_cell_unavailable_after_recovery=True,old_cell_number_must_not_be_confused_with_new255_request=True,new255_builtin_source=str(D/'P05.2-paper.tex'),new255_source_sha256=sha(D/'P05.2-paper.tex'),new255_builtin_request_cell_after_recovery='22',new255_builtin_diagnostics_returned_at_checkpoint=False,new255_builtin_success_claimed=False,source_preserved=True,protected_editor_unchanged_open=True)
(F/'environment-and-builtin-request-scope.json').write_text(json.dumps(recovery,indent=2)+'\n')
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,focus='Original199 P16.4 general reference moment/target criterion after material coercivity repair, and whole independent200 review of20-page255 P05.2 coupled PA/non-PA examples/local jet realization/genuine regularizable raw completion/literal antecedent. No new independent acceptance.',completed197_candidate=False,completed198_verdict='FAIL',new_accepted_paper=False,original_closed=False)
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==76 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,P05_2_latest_unreviewed_native197_paper=dict(continuation=255,directory=str(D),source_sha256=sha(D/'P05.2-paper.tex'),logical_source_lines=1367,source_LF_separators=1366,argument_lines=1371,ledger_lines=50,pdf_pages=20,exact_registered_notes=7,all61_native_artifact_hashes_valid=True,all14_frozen_math_units_valid=True,all4_private_primary_bindings_valid=True,whole_source_argument_ledger_material_changes_and_final_notes_root_read=True,saved_notes_differ_from_exact_native_final=True,saved_notes_not_used_as_grants=True,exact_checker_reproduced=True,local_build_exit_codes=[0,0],local_warnings=[],root_visual_pages=[1,14,16,20],builtin_compilation_unverified=True,independent_reader_round=200,independent_verdict=None,new_accepted_paper=False,original_closed=False),P16_4_alternate_initial_reference254=dict(records=[dict(path=str(p),sha256=sha(p)) for p in alternate],status='Unreviewed explicit bounded Tate division/preparation/Noetherianity/factoriality/normalization, normal-base going-down and finite Gauss-fibre norming. Domain-component dominance clarified in unchanged-base addendum. Actual model/chart and geometric/source antecedents still require review. Not sent to active199.',mathematical_grant=False,new_accepted_paper=False,original_closed=False),next_work='Continue native199/200 at maximum two, inspect settled results completely, independently reconstruct/review new mathematics, pursue full original scopes and keep regular verified GitHub pushes.',github_pending_checkpoint=dict(continuation=205,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n'); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint205: genuine regularizable completion and a coupled non-PA manuscript\n\n9/42 originals solved,33 open,76 independently accepted partial/supporting papers. No new acceptance. Native197 completed candidate=false with20-page255. Full1367 logical TeX lines (1366 LF separators),1371 argument lines,50 quote-free ledger lines,material changes and seven exact canonical final notes ROOT-read.61 native artifact entries,14 frozen math units and4 private primary bindings valid. Saved notes differ from native FINAL and are not grants. Exact checker reproduced; two clean local builds; only PDF1/14/16/20 ROOT visually read. Built-in new255 request has no diagnostics yet.\n\nNew unreviewed scope: corrected finite PA floor/contact criterion; genuinely coupled PA masses12,6,6/reference24/contact-3; real local-jet realization with actual rational reference; sequence-independent genuine raw mixed completion on the stated regularizable domain; explicit non-PA segment/parabola measure and contact-3, with literal gap3/64; reconstructed literal noncompact antecedent obstruction. Full all-reference/all-obstacle/non-PA contact classification remains open. Whole independent200 launched with three complete grants and all unchanged clarifications.\n\nOriginal199 P16.4 continues general-dimensional criterion and inverse equation. ROOT254 supplies an unreviewed alternate bounded-Tate/going-down/finite-Gauss-fibre initial-reference proof and separate component-dominance clarification. A253 private retrieval obtained the158-page original Berkovich1993 source, not yet proof-read; Raynaud-Gruson publisher attempt failed to return PDF. No full source files or third-party images are published. Native campaigns and files survived environment recovery; no duplicate launch/account/runtime/editor changes. Old250 built-in request is unverified and its old cell number differs from the new post-recovery255 request despite the reused number22.\n')
files=[]
def add(p,target=None):
    p=Path(p); assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation205/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for name in ('P05.2-paper.tex','P05.2-paper.pdf','argument.md','source-application-ledger.md','material-changes.md','check_certificates.py','certificate-input.json','root-reproduction-binding-20261007.json','root-visual-and-builtin-request-scope-addendum-20261007.json','README.md'):add(D/name)
for p in sorted((D/'evidence').iterdir()):add(p)
for name in ('P05.2-round197-actual-registered-partial-author-result-20261007.json','P05.2-round197-exact-native-model-final-partial-author-20261007.json','P05.2-round197-whole-coupled-nonPA-author-binding-20261007.json'):add(K/name)
for p in alternate:add(p)
add(K/'continuation253-formal-comparison-primary-LOCALONLY/retrieval-binding.json','research-checkpoints/continuation205/primary-retrieval-metadata/formal-comparison253.json')
C=next((R/'campaigns/round-200').iterdir())
for name in ('freeze.json','mathematical-data-bindings.json','launch-record.json'):add(C/name)
for name in ('bind_and_reproduce_coupled_nonPA255_20261007.py','prepare_coupled_nonPA255_review200_20261007.py','launch_frozen_coupled_nonPA_review200_20261007.py','write_bounded_normalization_reference254_20261007.py','retrieve_formal_comparison_primary253_20261007.py','record_verified204_20261007.py'):add(R/name)
add(G/'push-receipt-continuation204.json'); add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=76,commit_message='Review genuine raw completion and explicit coupled non-PA contact obstruction',scope='Native197 candidate=false whole20-page255 read/reproduced: explicit material PC-floor repair, coupled PA contact-3, actual rational-reference real jet realization and finite-PA criterion, genuine raw completion only on proved regularizable domain, non-PA segment/parabola measure/contact-3 and literal gap3/64, literal noncompact regularity antecedent. Exact7 native final notes,61 artifacts,14 frozen units,4 private primary bindings verified; saved notes differ and not grants; two local builds clean,ROOTvisual1/14/16/20, builtin unverified. Whole200 independent review launched with three WHOLE grants/all clarifications. Original199 P16.4 continues, unreviewed alternate254 initial-reference proof/addendum retained;253 retrieval metadata only.9/42 originals solved33open76accepted; no new acceptance or original closure. Environment recovery preserved campaigns/auth/editor; no hot feedback/duplicate calls; full third-party/dossier/private inspection/stdout/SQLite/active streams excluded.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],accepted_papers=76),indent=2))
