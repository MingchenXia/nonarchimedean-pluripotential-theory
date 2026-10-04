"""Freeze the reviewed Reeb partial and the current two native reviews."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research')
G=R/'github-checkpoint'
D=G/'continuation63-publication-records'
assert not D.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
receipt=json.loads((G/'push-receipt-continuation62.json').read_text())
assert receipt['commit_sha']=='5b1282b7e174a9886d5efb32f61a2c6980e77fc3'
assert receipt['all_file_blob_bindings_verified_remote']
P=R/'deliverables/scoped-P13.1-round52'
pub=json.loads((P/'publication-preparation.json').read_text())
assert pub['verdict']=='PASS' and not pub['fully_solved_original_atom']
assert pub['premises']==9 and pub['passages']==11
assert pub['local_two_pass_return_codes']==[0,0]
assert sha(P/'P13.1-paper.tex')==pub['source_sha256']
assert sha(P/'P13.1-paper.pdf')==pub['pdf_sha256']
assert sha(P/'P13.1-correctness-review.json')==pub['review_sha256']
D.mkdir()
items=[]
for atom,number,stem,session in [
 ('P16.1',53,'P16.1-public-source-unibranch-finite-energy-equation-review',91390),
 ('P13.2',51,'P13.2-public-source-fixed-Reeb-image-review-v2',3702),
]:
 directory=R/'campaigns'/('round-'+str(number))/stem
 q=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(directory/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 p=D/(atom+'-native-status.json');p.write_text(q.stdout)
 items.append({'atom':atom,'round':number,'role':'correctness and original-domain review' if atom=='P16.1' else 'correctness review','directory':str(directory),'tool_session_id':session,
  'observed_status':json.loads(q.stdout)['status'],'status':str(p),'status_sha256':sha(p),
  'argument_sha256':sha(directory/'argument.md'),'settings_sha256':sha(directory/'settings.json'),'accepted':False})
launch=D/'current-small-batch-observation.json'
launch.write_text(json.dumps({'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','items':items,'hot_feedback_sent':False},indent=2)+'\n')
review=R/'campaigns/round-53/P16.1-public-source-unibranch-finite-energy-equation-review'
f=json.loads((review/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(review/name)==f[key]
assert sha(review/'freeze.json')=='805f3c1e2b10e2b8b2d4b037d4b9caa9e437eef0354824d5cc3f863af43ef008'
round54=R/'campaigns/round-54/P13.1-public-source-signed-energy-uniform-Reeb-differentiation'
assert sha(round54/'input.json')=='7b4d507d689d393291fd7c15c5c89ed167a26e1dc0801b1ab3bf9ae01cc4247c'
assert sha(round54/'settings.json')=='65473d4f00063931d4d5a1c7fd3330a2a6094e8723664b84f42dcd415825bd04'
assert not (round54/'campaign.sqlite').exists()
a=json.loads((R/'active-work.json').read_text())
c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==39
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
entry={'scope':pub['scope'],'source':pub['source'],'source_sha256':pub['source_sha256'],
 'pdf':pub['pdf'],'pdf_sha256':pub['pdf_sha256'],'pages':pub['pages'],
 'argument':str(P/'P13.1-argument.md'),'review':pub['review'],'review_sha256':pub['review_sha256'],
 'publication_preparation':str(P/'publication-preparation.json'),'publication_preparation_sha256':sha(P/'publication-preparation.json'),
 'verdict':'PASS','operation_id':pub['operation_id'],'reported_utc':pub['reported_utc'],
 'premises':9,'passages':11,'all_zero_based_exact_statement_bindings_verified':True,
 'full_original_atom_solved':False,'conditional_envelope_premise_established':False}
for t in c['targets']:
 if t['id']=='P13.1':
  t['reviewed_papers'].append(entry)
  t['research_status']='all_Reeb_PSH_and_S_comparison_reviewed_partial_original_E1_and_derivative_open'
  t['current_focus']='Signed finite-type energy identity, uniform E1 comparison, moving mixed-measure tails and genuine obstacle-energy differentiation. Conditional envelope remains explicit in the reviewed round52 proof.'
  t['current_review_round52']['observed_status']='completed'
  t['current_review_round52']['verdict']='PASS';t['current_review_round52']['accepted']=True
  t['current_review_round52']['fully_solved_original_atom']=False
  t['current_reviewed_partial_round52']=entry
 if t['id']=='P13.2':t['current_review_round51']=items[1]
 if t['id']=='P16.1':t['current_review_round53']=items[0]
assert sum(len(t['reviewed_papers']) for t in c['targets'])==40
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint63: reviewed P13.1 partial; active P16.1 original-domain and P13.2 correctness reviews; cold signed-energy route. No new original closure.'
a['current_small_batch']={'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','active_items':items,'completed_original_atoms':['P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
a['selected_atoms']=['P16.1','P13.2']
a['P13.1_round52_reviewed_partial']=entry
a['P16.1_round53_author_completion']['state']='Complete retained-domain candidate; exact independent original-domain correctness review running. No original accepted yet.'
a['prepared_P16.1_round53_review']['state']='Launched through Xean native Codex; awaiting exact review.'
a['prepared_P16.1_round53_review']['tool_session_id']=91390
a['goal_state']='3/42 unchanged original problems solved;39 remain open;40 reviewed scoped papers. Continue until the original goal is fulfilled.'
assert a['fully_solved_original_atoms']==['P15.1','P15.2','P16.6']
c['updated_utc']=now;c['active_atoms']=['P16.1','P13.2']
c['current_small_batch_launch']=str(launch);c['current_small_batch_launch_sha256']=sha(launch)
c['historical_reviewed_scoped_papers']=40
(R/'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
(R/'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
with (R/'checklist-current.tsv').open('w',newline='') as h:
 w=csv.writer(h,delimiter='\t');w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
 for t in c['targets']:w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
 p=Path(path);assert p.is_file();files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation63/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
def add_directory(directory,remote_prefix=None):
 for p in sorted(directory.rglob('*')):
  if p.is_file() and p.suffix in {'.tex','.pdf','.json','.md','.log','.txt','.png','.py','.html','.stdout','.stderr'}:
   add(p,remote_prefix+'/'+str(p.relative_to(directory)) if remote_prefix else None)
add_directory(D)
add_directory(P,'manuscript/editorial/xean_research_20261003/deliverables/scoped-P13.1-round52')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for name in ['task.json','argument.md','settings.json','freeze.json']:add(review/name)
for name in ['input.json','settings.json','input-manifest.json']:
 p=round54/name
 if p.exists():add(p)
for p in [R/'root-checks/P13.1-signed-finite-type-density-and-E1-route-20261004-continuation63.md',
 R/'root-checks/BJ-Lemma8-7-actual-page-20261004-continuation63.png',
 R/'root-checks/P13.1-round52-actual-correctness-review.json',
 R/'prepare_public_P13_1_signed_energy_20261004.py',R/'publish_scoped_P13_1_round52_20261004.py',
 G/'push-receipt-continuation62.json',G/'prepare_checkpoint_continuation63.py']:add(p)
for p in sorted((R/'root-checks').glob('*-20261004-continuation63.json')):add(p)
assert len({x['path'] for x in files})==len(files)
payload={'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
 'files':files,'file_count':len(files),'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,
 'historical_reviewed_scoped_papers':40,'current_native_batch':items,
 'commit_message':'Publish independently reviewed all-Reeb PSH comparison partial and checkpoint equation reviews',
 'scope':'Exact P13.1 partial correctness PASS,9 premises11 bound passages,10p clarified reviewed paper and two local builds. Two active independent reviews; prepared cold signed-energy author task; unreviewed new root route with explicit projective remainder constants. No new original accepted. No private transcripts, SQL, credentials, Git databases, generated book-source or complete uploaded PDF.'}
m=G/'upload-manifest-continuation63.json';assert not m.exists();m.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(m),'sha256':sha(m),'files':len(files),'originals_solved':3,'reviewed_scoped_papers':40,'reviews':[(x['atom'],x['observed_status']) for x in items]},indent=2))
