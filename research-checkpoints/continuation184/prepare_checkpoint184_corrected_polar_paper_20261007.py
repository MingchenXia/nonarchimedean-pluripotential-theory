from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation184.json';F=G/'continuation184-publication-records'
S=K/'small-batch173176-public-status-20261007-continuation184'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation183.json').read_text())
assert prior['commit_sha']=='2172fcf78d2a07d688989902e89d0e5f9617d890'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir();S.mkdir();items=[]
for n,atom in ((173,'P16.4'),(175,'P14.4'),(176,'P16.4')):
 c=next((R/f'campaigns/round-{n}').iterdir())
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
 items.append({'round':n,'atom':atom,'directory':str(c),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'unsettled_calls':st['calls']['unsettled'],'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
C=next((R/'campaigns/round-177').iterdir());freeze=json.loads((C/'freeze.json').read_text())
assert freeze['prepared_only'] and not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
review=json.loads((K/'P14.4-round175-whole-partial-review-binding-20261007.json').read_text());assert review['verdict']=='FAIL'
D=K/'public-P14.4-continuation215-corrected-polar-reader'
repro=json.loads((D/'root-reproduction-and-publication-binding-20261007.json').read_text())
assert sha(D/'P14.4-paper.tex')==repro['source_sha256'] and sha(D/'P14.4-paper.pdf')==repro['pdf_sha256']
batch={'recorded_utc':datetime.now(timezone.utc).isoformat(),'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'next_prepared_review':freeze,'focus':'175 complete172 partial audit FAIL on missing primitive coordinate continuity hypotheses; entire geometric/tower core checked. New complete215 corrected10-page paper frozen for177 whole-paper review, prepared only.173 whole171 and176 whole214 audits continue; no active private outputs read or hot feedback.'}
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text())
 assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==64 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch)
 j['P14_4_complete_partial_review175']=review
 j['P14_4_unreviewed_corrected_partial215']={'reader_directory':str(D),'reproduction':repro,'prepared_review':freeze,'native_final_source_compiler_success':True,'new_accepted_paper':False,'original_closed':False}
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P14.4':
    assert not t['fully_solved'] and t['closure']=='open'
    t['research_status']='partial_review_FAIL_scope_repaired_entire_reaudit_prepared'
    t['current_focus']='Whole175 audit FAIL: total variation alone does not imply primitive L1 continuity without a,kappa convergence; geometric sector/full-tower obstruction checked. New215 entire10-page corrected paper adds coordinate convergence and complete estimate; source read,2 clean local builds,nativeSUCCESS. Entire177 independently frozen/prepared only. Old172 unregistered-support publication failure and175 FAIL preserved. Original arbitrary-big-transcendental/nonprojective construction remains open.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),'originals_solved':9,'originals_open':33,'cumulative_independently_accepted_research_papers':64,'new_original_closure':None,'175_verdict':'FAIL','215_independently_accepted':False,'177_prepared_not_admitted':True,'171_172_214_215_native_compile_success':True,'protected_editor_unchanged_open':True,'no_hot_feedback':True},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation184/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S,D):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
for name in ('task.json','argument.md','original-task.json','settings.json','freeze.json','mathematical-data-bindings.json'):add(C/name)
add(next((R/'campaigns/round-176').iterdir())/'launch-record.json')
for atom,name in (('P16.4','public-P16.4-round171-partial-reader'),('P14.4','public-P14.4-round172-partial-reader'),('P16.4','public-P16.4-continuation214-completed-closure-descent')):
 add(K/name/'native-compiler-success-final-source-addendum-20261007.json')
for name in ('P14.4-round175-actual-canonical-independent-review-20261007.json','P14.4-round175-native-model-final-review-20261007.json','P14.4-round175-whole-partial-review-binding-20261007.json'):add(K/name)
for name in ('record_verified183_20261007.py','bind_completed_review175_20261007.py','launch_frozen_partial_review176_20261007.py','prepare_P14_4_corrected_primitive_topology215_20261007.py','prepare_corrected_polar215_review177_20261007.py'):add(R/name)
add(G/'push-receipt-continuation183.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps({'generated_utc':datetime.now(timezone.utc).isoformat(),'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':j['fully_solved_original_atoms'],'remaining_open_atoms':33,'historical_reviewed_scoped_papers':64,'commit_message':'Preserve failed polar-paper audit and publish complete corrected primitive-continuity draft','scope':'Complete175 FAIL report/native/canonical/source bindings preserved: generalized primitive L1 continuity missed state-coordinate convergence. Full corrected215 ten-page draft and new amendment proof published;whole source read,2clean final local builds,nativeSUCCESS;first/last visual only.177 independent entire corrected manuscript review prepared only;only completeB grant,no earlier verdict in frozen math input.176 complete214 review launched under two-campaign guard.171/172/214 native-success addenda preserve historical pending records. No new acceptance/original closure;counts9/42,64. No active private streams/auth/runtime/protected-editor changes or fullthird-party PDF copying.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'listed_files':len(files),'active_batch':[x['round'] for x in active]},indent=2))
