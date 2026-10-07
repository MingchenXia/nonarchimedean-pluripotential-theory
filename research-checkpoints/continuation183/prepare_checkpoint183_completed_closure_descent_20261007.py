from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation183.json'; F=G/'continuation183-publication-records'
S=K/'small-batch173175-public-status-20261007-continuation183'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation182.json').read_text())
assert prior['commit_sha']=='ed2e88eb55104f193343cac718d3c8ee339c2fec'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir();S.mkdir();items=[]
for n,atom in ((173,'P16.4'),(175,'P14.4')):
 c=next((R/f'campaigns/round-{n}').iterdir())
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
 items.append({'round':n,'atom':atom,'directory':str(c),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'unsettled_calls':st['calls']['unsettled'],'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
C=next((R/'campaigns/round-176').iterdir());freeze=json.loads((C/'freeze.json').read_text())
assert freeze['prepared_only'] and not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
batch={'recorded_utc':datetime.now(timezone.utc).isoformat(),'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'next_prepared_review':freeze,'focus':'173/175 entire partial-paper reviews continue;176 prepared only for complete214 completed-algebraic-closure singular psh/extended-energy/continuous-test-dual descent. No original closure or new acceptance.'}
D=K/'public-P16.4-continuation214-completed-closure-descent'
repro=json.loads((D/'root-reproduction-and-publication-binding-20261007.json').read_text())
assert sha(D/'P16.4-paper.tex')==repro['source_sha256'] and sha(D/'P16.4-paper.pdf')==repro['pdf_sha256']
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text())
 assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==64 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch)
 j['P16_4_unreviewed_completed_closure_descent214']={'reader_directory':str(D),'reproduction':repro,'prepared_independent_review':freeze,'original_closed':False,'new_accepted_paper':False}
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open'
    t['current_focus']='Complete12-page171 arbitrary-trivial-ground-field equation draft independent173 running. New8-page214 all-complete-char0-field completed-closure singular-psh/extended-energy/continuous-test-dual descent draft source-read,2 clean local exports; entire independent176 prepared only, awaits active slot. No arbitrary-field unbounded mixed operator or full-original equation closure.'
   if t['id']=='P16.5':
    assert t['fully_solved']
    t['current_focus']='Entire original big rational bundle equation accepted by independently reconstructed whole-original167 PASS. Corrected18-page original210 retained vertical correction and source/native bindings published180. Original closure recorded; no nontrivially-valued field grant.'
   if t['id']=='P19.2':
    assert not t['fully_solved']
    t['current_focus']='Whole original170 review INCONCLUSIVE fully read and bound, published181: usual-data/NA-energy/interior-P-raw-mass Fatou obstruction verified for the audited maximal/I-maximal ray categories. Exact original target signature and arbitrary normal-model Perron extension remain unresolved. Original arbitrary nonmaximal-ray/P-profile branches remain open.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),'originals_solved':9,'originals_open':33,'cumulative_independently_accepted_research_papers':64,'new_original_closure':None,'214_independently_accepted':False,'176_prepared_not_admitted':True,'native_final_source_compile_pending':True,'protected_editor_unchanged_open':True,'no_hot_feedback':True},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation183/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S,D):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
for name in ('task.json','argument.md','original-task.json','settings.json','freeze.json','mathematical-data-bindings.json'):add(C/name)
add(K/'P16.4-continuation213-continuous-scalar-envelope-application-20261007.json')
for name in ('record_verified182_20261007.py','record_field_envelope_source_boundary213_20261007.py','prepare_completed_closure_descent214_review176_20261007.py'):add(R/name)
add(G/'push-receipt-continuation182.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps({'generated_utc':datetime.now(timezone.utc).isoformat(),'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':j['fully_solved_original_atoms'],'remaining_open_atoms':33,'historical_reviewed_scoped_papers':64,'commit_message':'Record completed-closure singular metric descent draft and frozen independent audit','scope':'Complete unreviewed8-page214 all-complete-characteristic-zero-field singular PSH/extended-energy/continuous-test-dual descent. Entire source read;2 clean local exports;only first/last visual pages;native compiler pending.176 entire-paper independent review prepared only, waiting for a173/175 active slot.213 continuous scalar envelope primary application recorded. No new accepted paper/original closure. Correct stale P16.5 andP19.2 focus descriptions to already bound published conclusions. No third-party source PDF/private streams/credentials uploaded;no auth/runtime change;protected editor unchanged/open;counts9/42,64 cumulative accepted papers.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'listed_files':len(files),'active_batch':[x['round'] for x in active]},indent=2))
