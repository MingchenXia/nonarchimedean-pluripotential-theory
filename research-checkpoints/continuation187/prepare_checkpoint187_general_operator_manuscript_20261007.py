from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation187.json';F=G/'continuation187-publication-records';S=K/'small-batch178179-public-status-20261007-continuation187'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S)); prior=json.loads((G/'push-receipt-continuation186.json').read_text())
assert prior['commit_sha']=='b1d2a49004fda1d3092f6b26072874f4ddacd0ed' and all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir();S.mkdir();items=[]
for n in (178,179):
 c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
 items.append(dict(round=n,atom='P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),items=items,active_items=active,maximum_concurrent_campaigns=2,focus='Whole216 direct all-field curve E1 operator independently178 and whole217 direct arbitrary-dimensional all-field mixed operator independently179. Both inputs frozen, no caller grants and no hot feedback. Previously accepted scoped papers67; original atoms9/42 unchanged.')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==67 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch)
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open';t['research_status']='whole_all_field_operator_partial_reviews_active'
    t['current_focus']='Previously accepted arbitrary-trivial-ground-field genuine equation paper171 and completed-closure descent214 remain in their exact domains. Entire2167-page curve operator and entire2178-page arbitrary-dimensional mixed-operator/all-test-integrability/joint-weighted-net manuscript are independently178179 active with no caller grants. Both nativeSUCCESS and two clean final local builds; only first/last pages visually checked. No original target equation closure, strict locality/comparison, general normalized compactness or EP/orthogonality/outer derivative is accepted from these drafts.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=67,new_original_closure=None,new_accepted_partial_paper=None,new_unreviewed_manuscript_continuation=217,active_batch=[x['round'] for x in active],no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation187/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P16.4-continuation217-general-E1-mixed-operator'):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
C=next((R/'campaigns/round-179').iterdir())
for name in ('task.json','argument.md','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'):add(C/name)
for name in ('prepare_general_mixed_operator217_review179_20261007.py','launch_frozen_partial_review179_20261007.py','record_verified186_20261007.py'):add(R/name)
add(G/'push-receipt-continuation186.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=datetime.now(timezone.utc).isoformat(),repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=67,commit_message='Add full arbitrary-field mixed-operator manuscript for independent audit',scope='New complete eight-page unreviewed217 direct all-dimensional finite-energy mixed operator: ordered PL energy estimates, actual endpoint curvature limits, positive polarization, every-E1-test integrability, uniform singular-test error, arbitrary joint weighted nets, genuine energy and affine derivative, reference/field covariance. All622 source lines ROOT read; nativeSUCCESS and two clean final local builds, first/last visual only. Whole independent179 frozen and active alongside178 under two-slot guard. No caller grants or original closure;accepted67,originals9/42 unchanged. No private active streams/runtime/account/protected-editor alterations or full third-party PDF copying.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=67,originals_solved=9),indent=2))
