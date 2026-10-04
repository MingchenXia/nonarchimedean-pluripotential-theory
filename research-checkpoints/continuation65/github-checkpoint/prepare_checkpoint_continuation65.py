"""Freeze new exact source audits and the next unlaunched small-batch task."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint'
D=G/'continuation65-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipt=json.loads((G/'push-receipt-continuation64.json').read_text())
assert receipt['commit_sha']=='95864197cbc4698b1b25467744daff8ea1d2fd52'
assert receipt['all_file_blob_bindings_verified_remote'] and receipt['remote_ref_verified']
assert not D.exists()
C=R/'campaigns/round-55/P13.1-public-source-expanded-signed-energy-uniform-Reeb-differentiation'
m=json.loads((C/'input-manifest.json').read_text())
assert sha(C/'input.json')==m['input_sha256']=='fde0115749ccffb7791ccc494ad69284b2f96848cdf68add58978e575aa8cef0'
assert sha(C/'settings.json')==m['settings_sha256']=='e84fcfe271b2e983ffa0c1ccef6fed71c641c96f0b744e7d8c7bf6c3cd8b9c06'
assert not (C/'campaign.sqlite').exists()
for s in m['public_sources']:
 assert sha(s['pdf'])==s['pdf_sha256']
 assert sha(s['literal_extract'])==s['extract_sha256']
reads=R/'root-checks/continuation65-primary-calibration-and-localization-reads'
record=json.loads((reads/'source-read-record.json').read_text())
assert len(record['units'])==12
for u in record['units']:
 assert sha(u['source'])==u['source_sha256']
 a,b=u['LF_one_based_inclusive']
 assert '\n'.join(Path(u['source']).read_text().split('\n')[a-1:b])==Path(u['extract']).read_text()
 assert sha(u['extract'])==u['extract_sha256']
 assert u['exact_selected_body_root_read'] and not u['whole_primary_source_root_read']
D.mkdir()
items=[]
for atom,roundno,stem,role,db,session in [
 ('P16.1',56,'P16.1-public-source-noncircular-local-extension-unibranch-equation','author repair','campaign.sqlite',56950),
 ('P13.2',51,'P13.2-public-source-fixed-Reeb-image-review-v2','correctness review','review.sqlite',3702),
]:
 directory=R/'campaigns'/('round-'+str(roundno))/stem
 q=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(directory/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 p=D/(atom+'-native-status.json');p.write_text(q.stdout)
 items.append({'atom':atom,'round':roundno,'role':role,'directory':str(directory),'tool_session_id':session,'observed_status':json.loads(q.stdout)['status'],'status':str(p),'status_sha256':sha(p),'settings_sha256':sha(directory/'settings.json'),'accepted':False})
now=datetime.now(timezone.utc).isoformat()
observation=D/'current-small-batch-observation.json'
observation.write_text(json.dumps({'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','items':items,'next_prepared_round':55,'next_task_launched':False,'hot_feedback_sent':False},indent=2)+'\n')
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint65: additional primary-source calibration and local-extension audits, explicit unreviewed repairs, prepared expanded-source P13.1 task. No new original closure.'
a['current_small_batch']={'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','active_items':items,'completed_original_atoms':['P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
a['continuation65_unreviewed_root_audits']={'paths':[str(p) for p in sorted((R/'root-checks').glob('*-20261004-continuation65.md'))],'source_read_record':str(reads/'source-read-record.json'),'newly_proved_original_atoms':[],'mathematical_status':'Unreviewed proposed repairs and exact source diagnostics; not accepted dependencies.'}
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch_launch']=str(observation);c['current_small_batch_launch_sha256']=sha(observation)
(R/'active-work.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
(R/'checklist-current.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
 p=Path(path);assert p.is_file()
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation65/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,reads]:
 for p in sorted(directory.rglob('*')):
  if p.is_file():add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for name in ['input.json','settings.json','input-manifest.json']:add(C/name)
for p in sorted((R/'root-checks').glob('*-20261004-continuation65.md')):add(p)
for p in sorted((R/'root-checks').glob('*-continuation65.png')):add(p)
for p in [R/'prepare_public_P13_1_expanded_energy_20261004.py',G/'push-receipt-continuation64.json',G/'prepare_checkpoint_continuation65.py']:add(p)
assert len({f['path'] for f in files})==len(files)
payload={'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,'historical_reviewed_scoped_papers':40,'current_native_batch':items,'commit_message':'Record primary calibration and localization repairs and prepare expanded Reeb energy task','scope':'Three unreviewed mathematical root audits;12 exact literal source units;3 actual source-page images; frozen eight-source-only P13.1 task prepared but unlaunched. Active native author repair and independent image review retained. No private transcripts, SQL, credentials, Git databases or book-source changes.'}
p=G/'upload-manifest-continuation65.json';assert not p.exists();p.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),'originals_solved':3,'reviewed_scoped_papers':40,'observed_native_statuses':[(x['atom'],x['observed_status']) for x in items]},indent=2))
