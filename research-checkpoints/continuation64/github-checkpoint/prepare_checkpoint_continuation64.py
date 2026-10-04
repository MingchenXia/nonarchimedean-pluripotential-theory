"""Preserve the exact failed proof review and launch one concrete repair."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint'
D=G/'continuation64-publication-records';assert not D.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads((G/'push-receipt-continuation63.json').read_text())
assert receipt['commit_sha']=='c4c618ec09532f7e8a49763363abc844a8a287e0'
assert receipt['all_file_blob_bindings_verified_remote']
now=datetime.now(timezone.utc).isoformat()
failed=R/'root-checks/P16.1-round53-failed-review-bindings-20261004-continuation64.json'
binding=json.loads(failed.read_text());assert binding['verdict']=='FAIL'
assert binding['entire_report_premises_and_passages_root_read'] and binding['all_zero_based_exact_statement_bindings_verified']
assert sha(binding['actual_review'])==binding['actual_review_sha256']
D.mkdir()
items=[]
for atom,roundno,stem,role,db,session in [
 ('P16.1',56,'P16.1-public-source-noncircular-local-extension-unibranch-equation','author repair','campaign.sqlite',56950),
 ('P13.2',51,'P13.2-public-source-fixed-Reeb-image-review-v2','correctness review','review.sqlite',3702),
]:
 directory=R/'campaigns'/('round-'+str(roundno))/stem
 q=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(directory/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 p=D/(atom+'-native-status.json');p.write_text(q.stdout)
 items.append({'atom':atom,'round':roundno,'role':role,'directory':str(directory),'tool_session_id':session,'observed_status':json.loads(q.stdout)['status'],'status':str(p),'status_sha256':sha(p),
 'input_or_argument_sha256':sha(directory/('input.json' if role=='author repair' else 'argument.md')),'settings_sha256':sha(directory/'settings.json'),'accepted':False})
launch=D/'current-small-batch-observation.json'
launch.write_text(json.dumps({'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','items':items,'hot_feedback_to_active_reviewers_sent':False},indent=2)+'\n')
C=R/'campaigns/round-56/P16.1-public-source-noncircular-local-extension-unibranch-equation'
m=json.loads((C/'input-manifest.json').read_text())
assert sha(C/'input.json')==m['input_sha256']=='df5b38d352c82e0ba6d4f0368d10700047deb394fcef55774933d9181ddce54e'
assert sha(C/'settings.json')==m['settings_sha256']=='dfb16f0378ec5cc2e1f1cf295f0954ed2cfb40c2647a14fc78fadcb8a46092b2'
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint64: actual P16.1 correctness FAIL with full bindings; concrete original-domain repair launched; additional primary energy sources and unreviewed root routes. No new original closure.'
a['selected_atoms']=['P16.1','P13.2']
a['current_small_batch']={'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','active_items':items,'completed_original_atoms':['P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
a['P16.1_round53_author_completion']['independent_correctness_verdict']='FAIL'
a['P16.1_round53_author_completion']['state']='Author candidate rejected by exact independent mathematical review; indispensable local regularization chain requires repair. Original remains open.'
a['P16.1_round53_failed_review']=binding
a['prepared_P16.1_round53_review']['state']='Completed FAIL; actual full review and exact premise bindings retained.'
a['P16.1_round56_repair']={**items[0],'full_saved_task_assignment_settings_and_embedded_context_root_read':True,'earlier_context_and_public_sources_reproduced_exactly':True,'fully_solved_original_atom':False}
for t in c['targets']:
 if t['id']=='P16.1':
  t['research_status']='complete_candidate_rejected_local_regularization_repair_active_original_open'
  t['current_focus']='Noncircular upper-growth smooth affine extension and regularization; rebuild singular induction and the genuine geometrically unibranch envelope antecedent before equation surjectivity.'
  t['current_completed_campaign_round53']=a['P16.1_round53_author_completion']
  t['current_review_round53']['observed_status']='completed';t['current_review_round53']['verdict']='FAIL';t['current_review_round53']['accepted']=False
  t['current_failed_review_round53']=binding;t['current_repair_round56']=a['P16.1_round56_repair']
 if t['id']=='P13.2':t['current_review_round51']=items[1]
c['updated_utc']=now;c['active_atoms']=['P16.1','P13.2'];c['current_small_batch_launch']=str(launch);c['current_small_batch_launch_sha256']=sha(launch)
(R/'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
(R/'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
with (R/'checklist-current.tsv').open('w',newline='') as h:
 w=csv.writer(h,delimiter='\t');w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
 for t in c['targets']:w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
 p=Path(path);assert p.is_file();files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation64/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
def add_directory(directory):
 for p in sorted(directory.rglob('*')):
  if p.is_file() and p.suffix in {'.tex','.pdf','.json','.md','.log','.txt','.png','.py','.html','.stdout','.stderr'}:add(p)
add_directory(D);add_directory(R/'root-checks/continuation64-primary-energy-bridge-reads')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for name in ['input.json','settings.json','input-manifest.json']:add(C/name)
for p in sorted((R/'shared-sources').glob('*-20261004-continuation64.*')):add(p)
for p in sorted((R/'root-checks').glob('*-20261004-continuation64.*')):add(p)
for p in [R/'root-checks/P16.1-round53-actual-correctness-review.json',R/'prepare_public_P16_1_noncircular_repair_20261004.py',G/'push-receipt-continuation63.json',G/'prepare_checkpoint_continuation64.py']:add(p)
assert len({x['path'] for x in files})==len(files)
payload={'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,'historical_reviewed_scoped_papers':40,'current_native_batch':items,
 'commit_message':'Preserve exact unibranch proof rejection and start noncircular regularization repair',
 'scope':'Actual P16.1 mathematical FAIL,15 premises18 exact bound passages; no original closure. Native original-domain repair plus fixed-Reeb image review. Three additional public primary source versions,26 selected source units and unreviewed exact finite-type/energy/obstacle/local-extension routes. No private transcripts, SQL, credentials, Git databases, generated book-source or complete uploaded PDF.'}
p=G/'upload-manifest-continuation64.json';assert not p.exists();p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),'originals_solved':3,'reviewed_scoped_papers':40,'reviews':[(x['atom'],x['observed_status']) for x in items]},indent=2))
