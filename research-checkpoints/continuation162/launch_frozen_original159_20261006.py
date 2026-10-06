from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=R/'campaigns/round-159/P16.5-original-equation-after-arbitrary-target-output-approximation';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();states=[]
for n in (157,158):
    c=next((R/f'campaigns/round-{n}').iterdir());s=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);states.append({'round':n,'public_status':s})
assert states[0]['public_status']['status']=='completed' and states[0]['public_status']['calls']['unsettled']==0
assert sum(x['public_status']['calls']['unsettled'] for x in states)<=1
f=json.loads((C/'freeze.json').read_text());s=json.loads((C/'settings.json').read_text());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
for name,key in [('input.json','input_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
assert f['input_sha256']=='69d2e32c57002618751412da2d80cf574833a501dfa4479c70e80d0ac9f58f8c' and f['task_sha256']=='2e9b9fcb3a4615a698c16190bf7b0a0bc6ef37660faa4be371fb58ed25e06989'
assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']=={'concurrency':1,'attempts':1,'providerCalls':1}
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':159,'pid':pid,'argv':args,'role':'original-author-research','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'original_closed':False,'unchanged_original_task':True,'frozen_task_sha256':f['task_sha256'],'frozen_math_input_sha256':f['input_sha256'],'frozen_settings_sha256':f['settings_sha256'],'private_active_output_read':False,'hot_feedback_sent':False,'account_auth_runtime_environment_changed':False,'parent_execution_permissions':'require_escalated for native-directory initialization, retaining native child sandbox','prior_public_states':states,'reserved_current_batch':[158,159]};(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'round':159,'pid':pid,'frozen_input_sha256':f['input_sha256'],'maximum_concurrent_campaigns':2},indent=2))
