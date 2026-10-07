from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation193.json'; F=G/'continuation193-publication-records'; S=K/'small-batch186188-public-status-20261007-continuation193'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation192.json').read_text()); assert prior['commit_sha']=='6a398e2542629e55e59fd63b5202e305dd84ddcf'
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
accept=json.loads((K/'public-P05.2-continuation224-strict-growth-obstruction/whole-partial-paper-acceptance187-20261007.json').read_text()); assert accept['verdict']=='PASS' and accept['cumulative_accepted_paper_number']==73
now=datetime.now(timezone.utc).isoformat(); F.mkdir(); S.mkdir(); items=[]
for n in (186,187,188):
    c=next((R/f'campaigns/round-{n}').iterdir()); st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json'; p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P16.4' if n==186 else 'P05.2',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0]; assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,focus='Entire224 strict-growth U(3,4) fan obstruction independentlyPASS187, accepted paper73, exact source/native/frozen bindings preserved. New five-page225 geometric compact-support/fan convex-hull/continuous maximum principle and rational-endpoint continuity counterexample under independent188 review, no grants. Full originalP16.4 author186 continues unchanged. Working observation226 proposes a continuous envelope representative proof, unproved data. Originals9/42 unchanged.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text()); assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==73 and j['remaining_open_original_atoms']==33
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=193,status='prepared_for_authorized_push')); p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=73,new_original_closure=None,new_accepted_partial_review=187,active_batch=[x['round'] for x in active],new_unreviewed_geometric_paper=225,new_unproved_envelope_observation=226,no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[]
def add(p,remote=None):
    p=Path(p); assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
    files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation193/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P05.2-continuation224-strict-growth-obstruction',K/'public-P05.2-continuation225-balanced-support-maximum-principle'):
    for p in sorted(folder.iterdir()):
        if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py'):add(p)
for label in ('actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding'):add(K/f'P05.2-round187-{label}-20261007.json')
add(K/'P05.2-continuation226-rational-endpoint-continuous-envelope-working-observation-20261007.json')
c=next((R/'campaigns/round-188').iterdir())
for name in ('task.json','argument.md','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'):add(c/name)
for name in ('bind_completed_review187_20261007.py','accept_polyhedral_obstruction224_review187_20261007.py','prepare_balanced_support225_review188_20261007.py','launch_frozen_partial_review188_20261007.py','write_polyhedral_continuous_envelope_working_observation226_20261007.py','record_verified192_20261007.py'):add(R/name)
add(G/'push-receipt-continuation192.json'); add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=73,commit_message='Accept strict-growth contact obstruction and audit balanced-support maximum principle',
    scope='Entire224 nine-page U(3,4) strict-growth contact obstruction and separate literal nonregularity independentlyPASS187; whole9188-char report/all8premises/10passages ROOT read and exact native/frozen/source bindings verified. Accepted paper73 with source-preserving PA intersection/tangent-span/active-strictness clarifications. Whole225 five-page covolume divergence, compact-support obstruction, positive fan linear cone hull, continuous PCC maximum principle and literal rational-endpoint continuity counterexample unreviewed under frozen188 no-grant independent review. ROOT read entire final164-source-line paper, two clean final local builds7/8, exact native compiler SUCCESS, first/last final PDF pages only. Working observation226 proposes a continuous rational-data representative/envelope proof and structural local tight-face question; neither is granted or accepted. Full originalP16.4 author186 continues unchanged. No new original closure:9/42 solved,33 open,max2 campaigns. No private active outputs, full third-party sources, auth/runtime/protected-editor changes.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=73,originals_solved=9),indent=2))
