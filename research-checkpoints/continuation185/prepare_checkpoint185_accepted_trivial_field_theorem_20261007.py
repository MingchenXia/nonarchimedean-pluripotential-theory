from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation185.json';F=G/'continuation185-publication-records';S=K/'small-batch176177-public-status-20261007-continuation185'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation184.json').read_text());assert prior['commit_sha']=='5f47319803bed86628375cc6a98b0fdae6160946'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir();S.mkdir();items=[]
for n,atom in ((176,'P16.4'),(177,'P14.4')):
 c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
 items.append({'round':n,'atom':atom,'directory':str(c),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'unsettled_calls':st['calls']['unsettled'],'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch={'recorded_utc':datetime.now(timezone.utc).isoformat(),'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'176 entire214 completed-closure singular-metric descent and177 entire215 corrected polar/tower paper independently review.173 whole171 trivial-ground-field genuine equation PASS fully bound;accepted paper65,no original closure.175 FAIL preserved;177 receives no earlier verdict.'}
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==65 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch)
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P14.4':
    assert not t['fully_solved'];t['research_status']='partial_review_FAIL_scope_repaired_entire_reaudit_active'
    t['current_focus']='Whole175 FAIL preserved for omitted primitive-coordinate continuity hypotheses. Entire corrected21510-page polar sector and full smooth-modification tower paper now independently177 running;full coordinate-plus-TV estimate and oscillating-constant counterexample supplied. NativeSUCCESS and2cleanlocalexports;no new acceptance or arbitrary-big-transcendental/nonprojective original closure.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),'originals_solved':9,'originals_open':33,'cumulative_independently_accepted_research_papers':65,'new_original_closure':None,'new_accepted_partial_paper':'171 complete arbitrary trivially valued char0 field equation theorem, independent173 PASS','active_batch':[x['round'] for x in active],'no_hot_feedback':True,'protected_editor_unchanged_open':True},indent=2)+'\n')
D=K/'public-P16.4-round171-partial-reader'
clarification=D/'harmless-reader-clarifications173-20261007.json';assert not clarification.exists()
clarification.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(D/'P16.4-paper.tex'),'independent_review_round':173,'source_preserved_exactly':True,'clarifications':['Every-solution uniqueness means u=v+c at every point; no subtraction of negative infinities at common poles is evaluated.','The n2 wording about n1 complete B grant refers to the actual caller task B grant.','n3 reported scripts/grid/provenance were not independently authenticated and are nonessential observations, not theorem premises.'],'mathematical_scope_unchanged':True,'original_closed':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation185/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S,D):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
for name in ('P16.4-round173-actual-canonical-independent-review-20261007.json','P16.4-round173-native-model-final-review-20261007.json','P16.4-round173-whole-partial-review-binding-20261007.json'):add(K/name)
add(next((R/'campaigns/round-177').iterdir())/'launch-record.json')
for name in ('bind_completed_review173_20261007.py','launch_frozen_partial_review177_20261007.py','record_verified184_and_accept_partial173_20261007.py'):add(R/name)
add(G/'push-receipt-continuation184.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps({'generated_utc':datetime.now(timezone.utc).isoformat(),'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':j['fully_solved_original_atoms'],'remaining_open_atoms':33,'historical_reviewed_scoped_papers':65,'commit_message':'Accept complete arbitrary trivial-ground-field equation theorem after independent audit','scope':'Whole17112-page all-dimensional arbitrary trivially valued char0 field genuine ample E1 equation independently173PASS relative only completeB. Full report/all8premises/12passages read;native/canonical/frozen input/source bindings exact;source/PDF preserved,nativeSUCCESS,2cleanlocalbuilds,first/last visual only. Accepted cumulative paper65,not full P16.4 closure;originals9/42 unchanged.176 entire214 completed-closure descent and177 entire215 corrected polar/tower review active under2slotguard;175FAIL retained,no earlier verdict in177mathinput. No private active streams/auth/runtime/protectededitorchanges or fullthird-partyPDF copying.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'listed_files':len(files),'active_batch':[x['round'] for x in active],'accepted_papers':65,'originals_solved':9},indent=2))
