from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, shutil, subprocess, time

R=Path('/workspace/research'); K=R/'root-checks'
Old=R/'campaigns/round-260/P12.3-whole365-and-general-normal-finite-correction364-independent-completion'
C=R/'campaigns/round-261/P12.3-whole365-finite-correction364'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not C.exists() and not (Old/'work.sqlite').exists()
diagnostic=(Old/'controller-output-LOCALONLY.log').read_text()
assert '/settings/usagePrefix: must not have more than 91 characters' in diagnostic
oldlaunch=load(Old/'launch-record.json');pstat=Path('/proc')/str(oldlaunch['pid'])/'stat'
assert not pstat.exists() or pstat.read_text().split()[2]=='Z'
f=load(Old/'freeze.json')
names=['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']
for name in names:assert sha(Old/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['active-work.json','checklist-current.json']:
 x=load(R/name);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 assert x['github_pending_checkpoint'] is None and x['current_active_batch']==[260]
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert not os.environ.get('XEAN_CODEX_COMMAND') and not os.environ.get('OPENAI_BASE_URL') and not os.environ.get('CODEX_BASE_URL')
prior={}
for q in [258,259]:
 P=next((R/f'campaigns/round-{q}').iterdir())
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(P/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert st['status']=='completed' and not st['error'] and st['calls']['unsettled']==0;prior[q]=st
C.mkdir(parents=True);T=C/'immutable-mathematical-DATA';T.mkdir();math=[]
for e in load(Old/'mathematical-packet-bindings.json'):
 p=Path(e['path']);assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
 dst=T/p.name;shutil.copyfile(p,dst);ne=dict(e,path=str(dst),retry_origin=str(p));math.append(ne)
assert len(math)==49 and sum(e['bytes'] for e in math)==1073558
for name in ['original-task.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
 shutil.copyfile(Old/name,C/name)
for name in ['book-context-bindings.json','private-primary-packet-bindings.json']:
 for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
task=load(Old/'task.json');task={k:v.replace(str(Old),str(C)) if isinstance(v,str) else v for k,v in task.items()}
inp=load(Old/'input.json');inp['task']=task
write(C/'task.json',task);write(C/'input.json',inp);write(C/'mathematical-packet-bindings.json',math)
s=load(Old/'settings.json');s['codex']['workspace']=str(C/'artifacts');s['usagePrefix']='catalogue-20261003/r261/P12.3-whole365-finite-correction364'
assert len(s['usagePrefix'])<=91 and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
write(C/'settings.json',s)
nf=dict(f,prepared_utc=datetime.now(timezone.utc).isoformat(),round=261,directory=str(C),retry_of_preinitialization_failure=260,
 settings_fix='usagePrefix shortened below schema91-character maximum; old frozen files and diagnostic preserved',
 fully_solved_originals_at_retry=16,remaining_OPEN_originals_at_retry=26,accepted_papers_at_retry=97)
for name in names:nf[name.replace('.json','').replace('-','_')+'_sha256']=sha(C/name)
write(C/'freeze.json',nf)
failure=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=260,status='FAILED BEFORE CAMPAIGN INITIALIZATION',
 old_launch_record=str(Old/'launch-record.json'),diagnostic=diagnostic,work_database_created=False,provider_called=False,
 native_math_output_created=False,old_frozen_files_preserved=True,replacement_round=261)
write(K/'native260-preinitialization-usagePrefix-schema-failure-and-retry261-20261008.json',failure)
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
 proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
deadline=time.monotonic()+12
while not (C/'work.sqlite').exists() and proc.poll() is None and time.monotonic()<deadline:time.sleep(0.2)
assert (C/'work.sqlite').exists() and proc.poll() is None, (C/'controller-output-LOCALONLY.log').read_text()[:1800]
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status']=='running' and not st['error']
now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=261,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',
 frozen_input_sha256=nf['input_sha256'],usagePrefix=s['usagePrefix'],usagePrefix_length=len(s['usagePrefix']),
 retry_of_preinitialization_failure=260,work_database_created=True,public_status=st,prior_completed_status=prior,
 only_grants=nf['only_grants'],whole_math_files=49,whole_math_bytes=1073558,maximum_concurrent_campaigns=2,
 provider_path='Existing Xean native signed-in Codex gpt-6.1-sol xhigh, inherited authentication/proxy/CA; no endpoint override',
 user_authorization=['Use gpt-6.1-sol xhigh through Xean’s native Codex path','授权你上传任何材料'],
 supplied_programs_executed=False,hot_feedback_sent=False,other_ACTIVE_math_read=False,protected_editor_open_unchanged=True)
write(C/'launch-record.json',record)
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);x.update(updated_utc=now,current_active_batch=[261],native260_preinitialization_failure=failure,
 native261_whole_original_independent_completion=dict(directory=str(C),pid=proc.pid,status='RUNNING initialized native campaign',input_sha256=nf['input_sha256'],only_grants=nf['only_grants']),
 next_work='Push262 accepted wholeP12.6 F366/paper97 and fullunreviewed365/363364 with initialized native261 retry, retain260 schema failure.16solved26OPEN97papers; atmost2; protected editor OPEN UNCHANGED.')
 write(p,x)
print(json.dumps(dict(round=261,pid=proc.pid,status=st['status'],database_exists=True,
 input_sha256=nf['input_sha256'],usagePrefix_length=len(s['usagePrefix']),current_active_batch=[261]),indent=2))
