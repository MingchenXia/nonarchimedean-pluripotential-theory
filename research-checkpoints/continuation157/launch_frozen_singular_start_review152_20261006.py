from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,os
R=Path('/workspace/research');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
other=next((R/'campaigns/round-151').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(other/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert st['status'] in ('running','completed','blocked','failed')
if st['status']!='running':assert st['calls']['unsettled']==0
C=next((R/'campaigns/round-152').iterdir());f=json.loads((C/'freeze.json').read_text());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
args=['bash','scripts/cloud.sh','xean','--records','review',str(C/'task.json'),str(C/'argument.md'),str(C/'work.sqlite'),str(C/'settings.json')]
out=C/'controller-output-LOCALONLY.log'
with out.open('xb') as log:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
d={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':152,'pid':pid,'argv':args,'role':'independent-review','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'scoped_review_only':True,'original_closed':False,'frozen_task_sha256':f['task_sha256'],'frozen_math_input_sha256':f['argument_sha256'],'frozen_settings_sha256':f['settings_sha256'],'private_active_output_read':False,'hot_feedback_sent':False,'account_auth_runtime_environment_changed':False,'other_round151_public_status':st}
(C/'launch-record.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'round':152,'pid':pid,'role':'independent-review','other_round151_status':st['status']},indent=2))
