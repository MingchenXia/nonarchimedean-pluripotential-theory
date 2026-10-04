"""Freeze the complete unibranch candidate; acceptance remains pending."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research')
G=R/'github-checkpoint'
D=G/'continuation62-publication-records'
D.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
receipt=json.loads((G/'push-receipt-continuation61.json').read_text())
assert receipt['commit_sha']=='b93881af63150d578be494bbc4eebd1e95dd5bf1'
assert receipt['all_file_blob_bindings_verified_remote']
items=[]
for atom,number,stem,session in [
 ('P13.1',52,'P13.1-public-source-new-unibranch-envelope-Reeb-calculus-review',48433),
 ('P13.2',51,'P13.2-public-source-fixed-Reeb-image-review-v2',3702),
]:
 directory=R/'campaigns'/('round-'+str(number))/stem
 q=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(directory/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 p=D/(atom+'-native-status.json');p.write_text(q.stdout)
 items.append({'atom':atom,'round':number,'role':'correctness review','directory':str(directory),'tool_session_id':session,
  'observed_status':json.loads(q.stdout)['status'],'status':str(p),'status_sha256':sha(p),
  'argument_sha256':sha(directory/'argument.md'),'settings_sha256':sha(directory/'settings.json'),'accepted':False})
launch=D/'current-small-batch-observation.json'
launch.write_text(json.dumps({'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','items':items,'hot_feedback_sent':False},indent=2)+'\n')
P=R/'root-checks/public-P16.1-round-53-final-reader'
read=json.loads((P/'complete-root-read.json').read_text())
assert read['entire_argument_read'] and read['all_four_actual_canonical_notes_read']
assert read['literal_primary_units']==23 and read['root_tex_pass_returncodes']==[0,0]
assert read['first_and_last_pages_visually_root_read'] and not read['original_atom_solved']
review=R/'campaigns/round-53/P16.1-public-source-unibranch-finite-energy-equation-review'
f=json.loads((review/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(review/name)==f[key]
assert not (review/'review.sqlite').exists()
(D/'P16.1-complete-candidate-pending-review.json').write_text(json.dumps({
 'reader':str(P),'reader_record_sha256':sha(P/'complete-root-read.json'),'candidate':True,
 'exact_retained_domain':'Every reduced irreducible geometrically unibranch projective variety over every algebraically closed trivially valued characteristic-zero field, every ample line bundle and claimed ample real numerical Cartier class; genuine mixed E1 operator, raw mass V, arbitrary finite-dual-energy support, one constant uniqueness.',
 'whole_proof_and_all_four_notes_root_read':True,'literal_units':23,'root_tex_pass_returncodes':[0,0],
 'independent_correctness_verdict':None,'original_closed':False,'pages':15,
 'review_directory':str(review),'review_freeze_sha256':sha(review/'freeze.json'),'review_submitted':False,
 'source_basis':'BJ v4 and Lyuhui Wu v1; source-based proof, not independent certification or novelty. Local logarithmic growth convention explicitly assigned to review.',
},indent=2)+'\n')
a=json.loads((R/'active-work.json').read_text())
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint62: complete unibranch candidate and exact queued review; active P13.1/P13.2 reviews; cold source normalization/growth audits. No new original closure.'
a['current_small_batch']={'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','active_items':items,'completed_original_atoms':['P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
a['selected_atoms']=['P13.1','P13.2']
a['P16.1_round53_author_completion']['native_compile']='UNVERIFIED_NO_RETURNED_DIAGNOSTICS'
a['P16.1_round53_author_completion']['first_and_last_pages_visually_root_read']=True
assert a['fully_solved_original_atoms']==['P15.1','P15.2','P16.6']
(R/'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==39
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
c['updated_utc']=now;c['active_atoms']=['P13.1','P13.2'];c['current_small_batch_launch']=str(launch);c['current_small_batch_launch_sha256']=sha(launch)
for t in c['targets']:
 if t['id']=='P13.1':t['current_review_round52']=items[0]
 if t['id']=='P13.2':t['current_review_round51']=items[1]
 if t['id']=='P16.1':t['current_completed_campaign_round53']=a['P16.1_round53_author_completion']
(R/'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
with (R/'checklist-current.tsv').open('w',newline='') as h:
 w=csv.writer(h,delimiter='\t');w.writerow(['ID','Closure','Research','Reviewed_papers','Title'])
 for t in c['targets']:w.writerow([t['id'],t['closure'],t['research_status'],len(t['reviewed_papers']),t['title']])
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
 p=Path(path);assert p.is_file();files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation62/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
def add_directory(directory):
 for p in sorted(directory.rglob('*')):
  if p.is_file() and p.suffix in {'.tex','.pdf','.json','.md','.log','.txt','.png','.py','.html','.stdout','.stderr'}:add(p)
for d in [D,P,R/'root-checks/continuation62-additional-source-reads']:add_directory(d)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for name in ['task.json','argument.md','settings.json','freeze.json']:add(review/name)
for p in sorted((R/'shared-sources').glob('*-20261004-continuation62.*')):add(p)
for p in [R/'root-checks/P16.1-logarithmic-growth-convention-audit-20261004-continuation62.md',
 R/'root-checks/P13.1-corrected-energy-normalization-route-20261004-continuation62.md',
 R/'root-checks/P16.1-round53-native-compile-unverified-20261004.json',
 R/'prepare_public_P16_1_unibranch_review_20261004.py',G/'push-receipt-continuation61.json',G/'prepare_checkpoint_continuation62.py']:add(p)
assert len({x['path'] for x in files})==len(files)
payload={'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
 'files':files,'file_count':len(files),'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,
 'historical_reviewed_scoped_papers':39,'current_native_batch':items,
 'commit_message':'Checkpoint complete unibranch equation candidate for independent original-domain review',
 'scope':'Unreviewed P16.1 complete retained-domain candidate, all four notes and23 exact source units, two root builds, queued exact review, active two-item Reeb reviews; cold source convention/factor audits with stated limits. No new original accepted. No private transcripts, SQL, credentials, Git databases, generated book-source or complete uploaded PDF.'}
m=G/'upload-manifest-continuation62.json';assert not m.exists();m.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(m),'sha256':sha(m),'files':len(files),'originals_solved':3,'candidate_not_accepted':'P16.1','reviews':[(x['atom'],x['observed_status']) for x in items]},indent=2))
