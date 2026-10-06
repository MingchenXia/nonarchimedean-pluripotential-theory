from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-168').iterdir());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('input.json','input_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
assert f['input_sha256']=='16862f135d05608a734623a38d5e2d7b953e34747d6f356d2e1d6b724fde1fae'
assert f['task_sha256']=='ab34124f46c030751e42bac4aed0e9ac214303cf3415ffc7b2588cae8f8559f8'
s=json.loads((C/'settings.json').read_text());assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']=={'concurrency':1,'attempts':1,'providerCalls':1}
assert 'P19.2' not in json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms']
states=[]
for n in (158,166,167):
 other=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(other/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert st['status'] in ('running','completed','blocked')
 if st['status']=='blocked':assert st['calls']['unsettled']==0 and st['work']['active']==0 and st['work']['queued']==0
 states.append({'round':n,'public_status':st})
assert sum(x['public_status']['calls']['unsettled'] for x in states)<=1,'Two campaigns are already active.'
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':168,'pid':pid,'argv':args,'role':'original-author-research','scope':'Entire unchanged original P19.2, with closed finer relative P data and arbitrary actual weak rays.','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'frozen_task_sha256':f['task_sha256'],'frozen_math_input_sha256':f['input_sha256'],'frozen_settings_sha256':f['settings_sha256'],'only_mathematical_grants':['R','T','C','S','E'],'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,'account_auth_runtime_environment_changed':False,'parent_execution_permissions':'require_escalated for exact authorized native-directory initialization, preserving native worker sandbox','prior_public_states':states,'reserved_current_batch':[x['round'] for x in states if x['public_status']['calls']['unsettled']>0]+[168]}
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'round':168,'pid':pid,'input_sha256':f['input_sha256'],'maximum_concurrent_campaigns':2},indent=2))
