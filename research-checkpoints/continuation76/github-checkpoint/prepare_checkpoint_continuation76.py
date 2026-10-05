"""Freeze the new shared-collar proposal and its unlaunched exact-task successor."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'continuation76-publication-records'
assert not D.exists()
receipt=json.loads((G/'push-receipt-continuation75.json').read_text())
assert receipt['commit_sha']=='1eb2ffd6227c99de361da256bb07c578f06138cd'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat();D.mkdir()
C=R/'campaigns/round-69/P16.1-public-source-shared-collar-weighted-mass-and-unibranch-equation'
m=json.loads((C/'input-manifest.json').read_text())
assert sha(C/'input.json')==m['input_sha256'] and sha(C/'settings.json')==m['settings_sha256']
assert not (C/'campaign.sqlite').exists() and len(m['public_sources'])==10 and len(m['embedded_context'])==12
data=json.loads((C/'input.json').read_text());old=R/'campaigns/round-68/P16.1-public-source-BE-exact-PL-local-mass-and-unibranch-equation'
assert data['task']==json.loads((old/'input.json').read_text())['task'] and data['notes']==[]
for s in m['public_sources']:assert sha(s['pdf'])==s['pdf_sha256'] and sha(s['literal_extract'])==s['extract_sha256']
for b in m['embedded_context']:assert sha(b['path'])==b['sha256'] and Path(b['path']).read_text() in data['assignment']
S=Path(m['new_source_read_record']).parent
sr=json.loads((S/'source-read-record.json').read_text());assert len(sr['units'])==5
for u in sr['units']:
    src=Path(u['source']);assert sha(src)==u['source_sha256'] and sha(u['literal_file'])==u['literal_sha256']
    first,last=u['inclusive_one_based_LF'];assert '\n'.join(src.read_bytes().decode().split('\n')[first-1:last])==Path(u['literal_file']).read_text()
items=[]
for atom,roundno,stem,role,db,session in [
    ('P13.1',63,'P13.1-public-source-eleven-body-semigroup-and-uniform-differentiation-original-review','complete original correctness review','review.sqlite',58323),
    ('P16.1',68,old.name,'author','campaign.sqlite',48580)
]:
    c=R/'campaigns'/('round-'+str(roundno))/stem
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    p=D/(atom+'-native-status.json');p.write_text(proc.stdout)
    items.append({'atom':atom,'round':roundno,'role':role,'directory':str(c),'tool_session_id':session,
        'observed_status':json.loads(proc.stdout)['status'],'status':str(p),'status_sha256':sha(p),
        'settings_sha256':sha(c/'settings.json'),'accepted':False})
assert len([i for i in items if i['observed_status']=='running'])<=2
write(D/'current-small-batch-observation.json',{'recorded_utc':now,'items':items,
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','hot_feedback_sent':False})
prepared={'round':69,'directory':str(C),'input_sha256':m['input_sha256'],'settings_sha256':m['settings_sha256'],
    'source_count':10,'embedded_context_count':12,'new_literal_source_units':5,'launched':False,
    'saved_new_prefix_settings_and_unchanged_completion_criteria_root_read':True,
    'inherited_prefix_byte_identical_to_previous_root_read':True,'new_proposal_whole_root_read':True,
    'new_proposal_independently_reviewed':False,'original_task_unchanged':True}
write(D/'prepared-P16.1-round69-input-bindings.json',prepared)
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint76: unreviewed shared-collar/weighted mass and model-atom domination proposal, five actual BJ units and unlaunched69. No new accepted original.'
a['prepared_P16.1_round69']=prepared
a['continuation76_unreviewed_root_proposal']={'path':m['embedded_context'][-1]['path'],
    'sha256':m['embedded_context'][-1]['sha256'],'source_read_record':str(S/'source-read-record.json'),
    'independently_reviewed':False,'originals_solved':[]}
a['current_small_batch']['recorded_utc']=now;a['current_small_batch']['active_items']=[i for i in items if i['observed_status']=='running']
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch']=a['current_small_batch']
write(R/'active-work.json',a);write(R/'checklist-current.json',c)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
files=[]
def add(path,remote=None):
    p=Path(path);assert p.is_file()
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation76/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,S]:
    for p in sorted(directory.rglob('*')):
        if p.is_file():add(p)
for n in ['input.json','settings.json','input-manifest.json']:add(C/n)
for p in [Path(m['embedded_context'][-1]['path']),R/'prepare_public_P16_1_shared_collar_mass_repair_20261005.py',
    R/'root-checks/P13.1-round63-native-compile-unverified-after-environment-switch-20261005.json',
    G/'push-receipt-continuation75.json',G/'prepare_checkpoint_continuation76.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
p=G/'upload-manifest-continuation76.json';assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,
    'historical_reviewed_scoped_papers':40,'current_native_batch':items,
    'commit_message':'Preserve shared-collar weighted mass and model-atom domination repair',
    'scope':'One unreviewed root proposal, five exact primary units, unlaunched69, actual compiler unverified followup and current two-item batch. No new accepted original, private transcripts, SQL, auth, Git database or book edits.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items],'fully_solved_originals':3},indent=2))
