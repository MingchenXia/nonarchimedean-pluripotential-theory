from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';M=G/'upload-manifest-continuation195.json';F=G/'continuation195-publication-records';S=K/'small-batch189190-public-status-20261007-continuation195'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S));prior=json.loads((G/'push-receipt-continuation194.json').read_text())
assert prior['commit_sha']=='14230bd5f978442a529081a705d61c443e3a7a1b' and prior['files']==98 and all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
C=next((R/'campaigns/round-191').iterdir());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in (189,190):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n');items.append(dict(round=n,atom='P16.4' if n==189 else 'P05.2',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,prepared_next_round=191,prepared_next_round_launched=False,focus='Independent189 whole genus-zero review and full originalP05.2 author190. New unreviewed general-curve model/finite-orbit route228 and failed product-obstruction observation229; no grants, accepts or original closure. Native191 full original field equation input prepared with six prior accepted grants only, queued until a slot frees.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==74 and j['remaining_open_original_atoms']==33
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=195,status='prepared_for_authorized_push'));p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_accepted_papers=74,new_original_closure=None,new_independent_verdict=None,active_batch=[x['round'] for x in active],prepared_only_next_round=191,new_unreviewed_working_observations=[228,229],own_finite_graph_proof_is_not_actual_curve_realization=True,new_primary_PDFs_retained_locally_only=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[];seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
    remote=remote or 'research-checkpoints/continuation195/'+str(p.relative_to(R));assert remote not in seen;seen.add(remote);files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for d in (F,S):
    for p in sorted(d.iterdir()):add(p)
for name in ('P16.4-continuation228-general-curve-convex-model-and-finite-orbit-working-observation-20261007.json','P16.4-continuation228-BL85-whole-unit-and-limited-scan-reading-addendum-20261007.json','P05.2-continuation229-product-tripod-failed-obstruction-working-observation-20261007.json'):add(K/name)
add(K/'public-P16.4-continuation227-genus-zero-equation/root-whole-argument-read-addendum-20261007.json')
for name in ('task.json','original-task.json','input.json','settings.json','freeze.json','mathematical-data-bindings.json'):add(C/name)
for name in ('write_general_curve_model_route228_20261007.py','record_curve_primary_and_product_failure_20261007.py','prepare_original_field_equation191_after_convex_model_route_20261007.py','launch_frozen_original_field_equation191_20261007.py','record_verified194_20261007.py'):add(R/name)
add(G/'push-receipt-continuation194.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=74,commit_message='Record convex model realization route and preserve failed product obstruction',scope='Unreviewed228 gives a complete working finite-graph Poisson/positive-margin/value-group two-slope interpolation argument on cycles and prospective ACTUAL all-genus curve model/FS/target/finite-orbit descent route. It is DATA, not an accepted theorem or actual metric recognition grant. Literal GHv2/BPRv1/KRZBv3 PDFs freshly downloaded privately; full pertinent proof units checked with recursive geometry dependencies explicitly open. BL85 whole pertinent OCR proof units and only four selected scanned pages checked; elementary omitted P1 subdivision and earlier dependencies remain. Unreviewed229 rejects an attempted product-tripod obstruction by an explicit larger admissible competitor; no exact envelope/MA/classification claim. Whole227 native argument327 lines now separately ROOT read; historical earlier false reading flag preserved in its prior record. Full original191 native input prepared ONLY, six prior whole accepted grants and228 unreviewed data; no active inputs changed/hot feedback. Active189/190 public status only. No original closure/new accepted paper:9/42 solved,33 open,74 accepted,max2campaigns. Protected editor/auth/runtime unchanged; full third-party sources remain private.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],prepared_only_next_round=191,accepted_papers=74),indent=2))
