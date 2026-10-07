from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';M=G/'upload-manifest-continuation194.json';F=G/'continuation194-publication-records';S=K/'small-batch189190-public-status-20261007-continuation194'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation192.json').read_text());assert prior['commit_sha']=='6a398e2542629e55e59fd63b5202e305dd84ddcf' and all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
old=G/'upload-manifest-continuation193.json';assert sha(old)=='9e6b6c74e7993b1de2187cd1b91333d7b79b2305c075e30e35684c3707d83e79' and not (G/'push-receipt-continuation193.json').exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (186,187,188,189,190):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n');items.append(dict(round=n,atom='P16.4' if n in (186,189) else 'P05.2',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,focus='Entire224/225 independently PASS187/188, accepted papers73/74. Eleven-page native186 genus-zero equation including nonsplit conics completed candidate=false and frozen under independent189 six-grant review. Full originalP05.2 author190 continues with whole accepted224/225 and unproved226 data. Originals9/42 unchanged.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==74 and j['remaining_open_original_atoms']==33
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=194,status='prepared_for_authorized_push'));p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
sup=dict(recorded_utc=now,superseded_prepared_checkpoint=193,superseded_manifest_sha256=sha(old),previous_snapshot_preserved=True,previous_helper_not_rerun=True,previous_checkpoint_uploaded=False,new_checkpoint=194,reason='Before upload, corrected publication scope metadata from164 to the actual163 source lines for225 and recorded completed186 rather than describing it as continuing. Whole225 now independentlyPASS188; source/math remained unchanged. New194 also records frozen189/190 and whole227 reproduction.',source_or_math_rewritten=False,new_original_closed=False)
(F/'unuploaded193-supersession.json').write_text(json.dumps(sup,indent=2)+'\n')
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=74,new_original_closure=None,new_accepted_partial_reviews=[187,188],active_batch=[x['round'] for x in active],new_unreviewed_genus_zero_paper=227,genus_zero_source_lf_lines=851,genus_zero_pdf_pages=11,genus_zero_whole_source_root_read=True,genus_zero_native_argument_separately_root_read=False,balanced_support_source_lf_lines=163,unproved_envelope_observation=226,no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[];remote_seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
    remote=remote or 'research-checkpoints/continuation194/'+str(p.relative_to(R));assert remote not in remote_seen;remote_seen.add(remote)
    files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P05.2-continuation224-strict-growth-obstruction',K/'public-P05.2-continuation225-balanced-support-maximum-principle',K/'public-P16.4-continuation227-genus-zero-equation'):
    for p in sorted(folder.iterdir()):
        if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py'):add(p)
add(K/'public-P16.4-continuation227-genus-zero-equation/evidence/root-finite-check.json')
for n in (187,188):
    for label in ('actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding'):add(K/f'P05.2-round{n}-{label}-20261007.json')
for label in ('completed-actual-author-result','native-model-final-partial-author','settled-partial-author-binding'):add(K/f'P16.4-round186-{label}-20261007.json')
add(K/'P05.2-continuation226-rational-endpoint-continuous-envelope-working-observation-20261007.json')
for n in (188,189,190):
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ('task.json','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'):add(c/name)
    add(c/('input.json' if n==190 else 'argument.md'))
    if n==190:add(c/'original-family-representation-binding.json')
for name in ('bind_completed_review187_20261007.py','accept_polyhedral_obstruction224_review187_20261007.py','prepare_balanced_support225_review188_20261007.py','launch_frozen_partial_review188_20261007.py','bind_completed_review188_20261007.py','accept_balanced_support225_review188_20261007.py','write_polyhedral_continuous_envelope_working_observation226_20261007.py','bind_completed_partial_author186_20261007.py','reproduce_genus_zero_equation227_20261007.py','finalize_genus_zero_equation227_reproduction_20261007.py','prepare_genus_zero227_review189_20261007.py','launch_frozen_partial_review189_20261007.py','prepare_original_polyhedral190_after_balancing_and_obstruction_20261007.py','launch_frozen_original_polyhedral190_20261007.py','record_verified192_20261007.py','prepare_checkpoint193_polyhedral_obstruction_and_maximum_review_20261007.py'):add(R/name)
add(G/'push-receipt-continuation192.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=74,commit_message='Accept balanced-support maximum principle and review genus-zero equations',scope='Entire224 strict-growth contact obstruction and entire225 positive balancing/continuous PCC maximum principle independently PASS187/188, accepted papers73/74, all exact native/source/frozen/review bindings and clarifications retained. Actual225 source163 lines; printed PCC automatic-continuity counterexample and continuous-only compact-envelope scope explicit. Whole native186 candidate-false eleven-page genus-zero equation source851 lines/4notes/JSONledger ROOT read; native argument not separately read in full. Finite checks rerun and two local builds succeeded with one recorded underfull box; exact native compiler SUCCESS; first/last PDF only inspected. Entire227 frozen under independent189 with six whole accepted O/D/N/T/Q/C grants, including nonsplit conics and residue-characteristic-zero domain. Full originalP05.2 author190 retains unchanged original/dossier and two accepted224/225 grants, unproved226 plan data. Unuploaded193 superseded before any Git write; its immutable manifest/helper preserved. No new original closure:9/42 solved,33 open,max2campaigns. No private active output, full third-party source upload, auth/runtime or protected-editor change.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=74,originals_solved=9),indent=2))
