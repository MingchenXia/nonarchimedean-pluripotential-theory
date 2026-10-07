from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation201.json';F=G/'continuation201-publication-records';S=K/'small-batch189194-public-status-20261007-continuation201'
D=K/'public-P16.4-continuation243-target-integrability-incidence-and-local-formal-bridge'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation200.json').read_text())
assert prior['commit_sha']=='5e6fdea76cec0e68fcbd237dd8aafd48862b17da' and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['source_sha256']==sha(D/'P16.4-paper.tex') and b['root_pdf_sha256']==sha(D/'P16.4-paper.pdf') and b['root_local_build_exit_codes']==[0,0]
assert b['candidate'] is False and b['new_accepted_paper'] is False and b['original_closed'] is False and b['native_artifact_hash_count']==66
C=next((R/'campaigns/round-194').iterdir());launch=json.loads((C/'launch-record.json').read_text());assert launch['model']=='gpt-6.1-sol' and launch['reasoning']=='xhigh'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (189,193,194):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n==194 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[i for i in items if i['unsettled_calls']>0];assert len(active)<=2
assert next(i for i in items if i['round']==193)['unsettled_calls']==0
visual=D/'root-visual-reading-scope-addendum-20261007.json';assert not visual.exists()
visual.write_text(json.dumps(dict(recorded_utc=now,source_sha256=sha(D/'P16.4-paper.tex'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=15,root_actual_visual_read_pages=[1],root_rendered_but_not_yet_visually_read_pages=[15],whole_pdf_visually_read=False,root_exact_native_builtin_compilation_unverified=True,root_local_build_exit_codes=[0,0],warnings=b['root_local_final_warnings'],source_not_modified=True,independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False),indent=2)+'\n')
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,completed193_candidate=False,completed193_continuation=243,focus='Whole189 independent genus-zero reader remains active if unsettled;194 original P05.2 author now launched after193 settled. Completed193 gives unreviewed whole15-page target/incidence/local-formal draft, original remains open. ROOT242 supplies actual-model/horizontal-bundle repair data and explicit correction of reference-only strict-positivity wording in238/241. No active private output or hot feedback.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==75 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    assert j['prepared_next_original_campaign']['round']==194
    j['prepared_next_original_campaign'].update(prepared_only=False,launched=True,launch_record=str(C/'launch-record.json'),launch_record_sha256=sha(C/'launch-record.json'))
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=201,status='prepared_for_authorized_push'))
    j['P16_4_latest_unreviewed_native193_paper']=dict(continuation=243,directory=str(D),source_sha256=sha(D/'P16.4-paper.tex'),source_lf_lines=1084,argument_lf_lines=361,pdf_pages=15,native_final_notes=6,whole_root_read=True,local_build_exit_codes=[0,0],builtin_compilation_unverified=True,independent_verdict=None,new_accepted_paper=False,original_closed=False)
    j['P16_4_latest_unreviewed_actual_geometry_routes'].update(actual_model_and_horizontal_bundle=242,strict_positive_margin_correction=242,sent_to_active193=False)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/n,F/n)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_accepted_papers=75,new_original_closure=None,new_independent_verdict=None,active_batch=[i['round'] for i in active],completed193_candidate=False,new_unreviewed_paper243_pages=15,whole1084tex361argument_six_canonical_notes_and_ledger_read=True,all66_native_artifact_hashes_verified=True,registered_native_final_exactly_bound=True,saved_long_notes_artifact_is_distinct_and_reproduced_from_whole_argument=True,finite_checks_only=True,builtin_compilation_unverified=True,root_visual_pdf_pages=[1],unreviewed_actual_model242=True,reference_only_strict_positivity_shortcut_explicitly_corrected=True,protected_editor_unchanged_open=True,full_third_party_sources_published=False),indent=2)+'\n')
files=[];seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and 'frozen-primary-data-LOCALONLY' not in p.parts
    remote=remote or 'research-checkpoints/continuation201/'+str(p.relative_to(R));assert remote not in seen;seen.add(remote)
    files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for d in (F,S):
    for p in sorted(d.iterdir()):add(p)
for n in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','notes.json','source-application-ledger.md','source-application-ledger.json','finite_checks.py','finite-check-output.json','README.md','root-reproduction-binding-20261007.json','root-visual-reading-scope-addendum-20261007.json'):add(D/n)
for p in sorted((D/'evidence').iterdir()):add(p)
for n in ('P16.4-round193-completed-actual-author-result-20261007.json','P16.4-round193-native-model-final-partial-author-20261007.json','P16.4-round193-settled-partial-author-binding-20261007.json','P16.4-continuation242-actual-models-horizontal-bundle-and-positive-margin-working-route-20261007.json'):add(K/n)
add(C/'launch-record.json')
for n in ('bind_and_reproduce_actual_target_and_incidence243_20261007.py','write_actual_semistable242_and_positive_margin_correction_20261007.py','record_verified200_20261007.py'):add(R/n)
add(G/'push-receipt-continuation200.json');add(Path(__file__))
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/n,'manuscript/editorial/xean_research_20261003/'+n)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=75,commit_message='Preserve actual incidence and target proofs and repair curve model positivity',scope='Completed native193 exact61xhigh workspace-write one-call original-author. Whole15-page1084LF TeX/361LF argument, six canonical/native-final notes and whole235LF quote-free ledger ROOT-read;66 native artifacts and16 frozen primary bindings verified. Registered final/canonical exact binding; saved notes.json contains distinct long paper-section notes, independently reproduced via fully read emitter with writes disabled, explicitly not claimed equal to condensed native final. Finite81 interpolation/1995 scaling/16 raw-mass/100 nilpotence cases reproduced; two local builds pass with harmless underfull warnings; built-in compilation unverified after request failed to return diagnostics, only PDF1/15 visually read. New actual target/unit-bound, scaling/conditional coercivity, actual common generic-Gauss field/curve points with explicit hypotheses, graph positivity, local Cartier and conditional FS-lifting paper remains unreviewed candidate=false, no M0 or prescribed-target attainment or unconditional all-genus equation. ROOT242 actual admissible-chart flat/fp reductions, properness on arbitrary nil thickenings, adapted vertex/puncture models, prospective horizontal same-bundle extension, and exact correction: reference-only mixing does not make newly added zero-degree components positive;235 entire-vertex mixture plus upward bends is required. Native194 now launched originalP05.2 after193 settled; public statuses only, max2.9/42originals solved33open75accepted, no new closure or acceptance. Protected editor and login/runtime unchanged.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[i['round'] for i in active],completed193_candidate=False,accepted_papers=75),indent=2))
