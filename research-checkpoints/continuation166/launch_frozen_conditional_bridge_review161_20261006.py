from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research')
C=R/'campaigns/round-161/P16.5-conditional-attainment-negligible-Borel-mixed-independent-review'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
states=[]
for n in (158,160):
    c=next((R/f'campaigns/round-{n}').iterdir())
    s=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    states.append({'round':n,'public_status':s})
assert states[1]['public_status']['status']=='completed' and states[1]['public_status']['calls']['unsettled']==0
assert sum(s['public_status']['calls']['unsettled'] for s in states)<=1
f=json.loads((C/'freeze.json').read_text());s=json.loads((C/'settings.json').read_text())
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name)==f[key]
assert f['argument_sha256']=='2fdbcdb87a1921b0478c49abb47a92b9c54002b06802cb63c20bfccb588ac1f1'
assert s['research']['model']=='gpt-6.1-sol' and s['research']['reasoning']=='xhigh' and s['limits']=={'concurrency':1,'attempts':1,'providerCalls':1}
args=['bash','scripts/cloud.sh','xean','--records','review',str(C/'task.json'),str(C/'argument.md'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':161,'pid':pid,'argv':args,'role':'independent-review','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'whole_review_papers':[159,160,201,202],'whole_pages':40,'original_closed':False,'frozen_task_sha256':f['task_sha256'],'frozen_math_input_sha256':f['argument_sha256'],'frozen_settings_sha256':f['settings_sha256'],'private_active_output_read':False,'hot_feedback_sent':False,'account_auth_runtime_environment_changed':False,'parent_execution_permissions':'require_escalated for native-directory initialization, retaining native child sandbox','prior_public_states':states,'reserved_current_batch':[158,161]}
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'round':161,'pid':pid,'frozen_argument_sha256':f['argument_sha256'],'maximum_concurrent_campaigns':2},indent=2))
