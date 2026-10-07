from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation186.json'; F=G/'continuation186-publication-records'; S=K/'small-batch178-public-status-20261007-continuation186'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation185.json').read_text())
assert prior['commit_sha']=='02e8f998ba555e2dd03c972d2bf136c781db2cc0'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir(); S.mkdir(); items=[]
for n,atom in ((176,'P16.4'),(177,'P14.4'),(178,'P16.4')):
 c=next((R/f'campaigns/round-{n}').iterdir())
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json'; p.write_text(json.dumps(st,indent=2)+'\n')
 items.append(dict(round=n,atom=atom,directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0]; assert len(active)<=2
batch=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),items=items,active_items=active,maximum_concurrent_campaigns=2,focus='Entire214 descent and entire215 corrected polar-tower papers independently PASS176177, exact native/source/input bindings verified and accepted papers66/67. Whole216 direct all-field curve operator independently178 active. ROOT217 proposed higher-dimensional operator proof plan is unreviewed, not a grant. Original atoms remain9/42.')
for name in ('active-work.json','checklist-current.json'):
 p=R/name; j=json.loads(p.read_text()); assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==67 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch)
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4': t['current_focus']+=' Whole216 seven-page direct all-field curve operator independently178 active; ROOT217 proposed general finite-energy mixed-operator proof is unreviewed.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'): shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=67,new_original_closure=None,new_accepted_partial_reviews=[176,177],active_batch=[x['round'] for x in active],proposed_general_operator_plan_independently_accepted=False,no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p); assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation186/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P16.4-continuation214-completed-closure-descent',K/'public-P14.4-continuation215-corrected-polar-reader',K/'public-P16.4-continuation216-all-field-curve-operator'):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'): add(p)
for n,atom in ((176,'P16.4'),(177,'P14.4')):
 for label in ('actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding'): add(K/f'{atom}-round{n}-{label}-20261007.json')
C=next((R/'campaigns/round-178').iterdir())
for name in ('task.json','argument.md','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'): add(C/name)
add(K/'P16.4-continuation217-general-E1-operator-proof-plan-20261007.json')
for name in ('bind_and_accept_reviews176177_20261007.py','prepare_all_field_curve_operator216_review178_20261007.py','launch_frozen_partial_review178_20261007.py','record_verified185_20261007.py'):add(R/name)
add(G/'push-receipt-continuation185.json'); add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=datetime.now(timezone.utc).isoformat(),repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=67,commit_message='Accept completed-closure descent and corrected polar-sector papers after independent audits',scope='Entire214/215 independently PASS176177; complete reports/premises/passages ROOT read and exact native/frozen-source bindings verified. Accepted scoped papers66/67, originals9/42 unchanged. Publish source/PDF/compiler/acceptance sidecars, harmless source-preserving clarifications and entire216 unreviewed direct curve operator with frozen review178. ROOT217 general-operator proof plan remains unreviewed, not a mathematical grant. Two-active-campaign limit preserved; no private active streams/auth/runtime/protected-editor changes or full third-party PDFs copied.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=67,originals_solved=9),indent=2))
