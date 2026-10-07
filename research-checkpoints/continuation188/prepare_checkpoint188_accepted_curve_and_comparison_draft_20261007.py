from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation188.json';F=G/'continuation188-publication-records';S=K/'small-batch179180-public-status-20261007-continuation188'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S));prior=json.loads((G/'push-receipt-continuation187.json').read_text())
assert prior['commit_sha']=='22d0f7ad9ade0a5f326795c0a87d2306a6031e7e' and all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir();S.mkdir();items=[]
for n in (178,179,180):
 c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
 items.append(dict(round=n,atom='P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),items=items,active_items=active,maximum_concurrent_campaigns=2,focus='Whole216 curve operator independentlyPASS178, exact bindings verified, accepted scoped paper68. Whole217 general mixed operator independently179 and original field-equation author180 run within two slots. Complete2186-page strict locality/comparison draft conditional on whole217 remains unreviewed. Original atoms9/42 unchanged.')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==68 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch)
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':t['current_focus']+=' Original-equation author180 active, exact171/214/216 grants;217/218 remain unreviewed data and no179 feedback is supplied. Complete2186-page locality/comparison derivation compiled cleanly but is conditional on entire217 and awaits a review slot.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=68,new_original_closure=None,new_accepted_partial_review=178,new_unreviewed_manuscript_continuation=218,active_batch=[x['round'] for x in active],no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation188/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P16.4-continuation216-all-field-curve-operator',K/'public-P16.4-continuation218-strict-locality-comparison'):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
for label in ('actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding'):add(K/f'P16.4-round178-{label}-20261007.json')
for name in ('round178-completed-inspection-retrieval-observation-20261007.json','P16.4-continuation218-strict-locality-comparison-proof-plan-20261007.json'):add(K/name)
C=next((R/'campaigns/round-180').iterdir())
for name in ('task.json','input.json','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'):add(C/name)
for name in ('bind_completed_review178_20261007.py','accept_curve_operator216_review178_20261007.py','prepare_original_field_equation180_20261007.py','launch_frozen_original_field_equation180_20261007.py','record_verified187_20261007.py'):add(R/name)
add(G/'push-receipt-continuation187.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=datetime.now(timezone.utc).isoformat(),repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=68,commit_message='Accept all-field curve operator and add strict-locality comparison draft',scope='Entire216 curve operator independentlyPASS178; report/all7premises/16passages ROOT read and exact native/frozen/source bindings verified. Accepted scoped paper68, originals9/42 unchanged. Source-preserving harmless clarifications recorded. Publish entire2186-page unreviewed conditional strict Borel locality/open locality/mixed and pure comparison, full CLD unit-reading ledger, nativeSUCCESS/two clean local final builds and first/last visual-only checks. Whole217 independent179 and original full-equation author180 run with frozen exact grants/unreviewed data under two slots. No hot feedback/private active streams/runtime/account/protected-editor changes or full third-party source PDFs copied.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=68,originals_solved=9),indent=2))
