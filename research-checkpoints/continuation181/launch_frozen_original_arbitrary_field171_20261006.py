from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-171').iterdir());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
front=json.loads((R/'active-work.json').read_text());assert 'P16.4' not in front['fully_solved_original_atoms'] and 'P16.5' in front['fully_solved_original_atoms']
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
s=json.loads((C/'settings.json').read_text());assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']=={'concurrency':1,'attempts':1,'providerCalls':1}
states=[]
for n in (167,169,170):
 o=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(o/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 if st['status']=='blocked':assert st['calls']['unsettled']==st['work']['active']==st['work']['queued']==0
 states.append({'round':n,'public_status':st})
assert sum(x['public_status']['calls']['unsettled'] for x in states)<=1
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':171,'pid':pid,'argv':args,'role':'original-author-research','scope':'Entire unchanged originalP16.4 arbitrary complete valued-field equation, general field descent and higher-dimensional operator gaps retained.','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'frozen_task_sha256':f['task_sha256'],'frozen_math_input_sha256':f['input_sha256'],'frozen_settings_sha256':f['settings_sha256'],'only_mathematical_grants':f['only_complete_grants'],'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,'account_auth_runtime_environment_changed':False,'parent_execution_permissions':'require_escalated for exact authorized native initialization, preserving native workspace-write research sandbox','prior_public_states':states,'reserved_current_batch':[x['round'] for x in states if x['public_status']['calls']['unsettled']>0]+[171]}
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'round':171,'pid':pid,'input_sha256':f['input_sha256'],'maximum_concurrent_campaigns':2},indent=2))
