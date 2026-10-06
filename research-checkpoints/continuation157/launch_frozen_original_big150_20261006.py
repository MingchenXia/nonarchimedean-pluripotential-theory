from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,os
R=Path('/workspace/research');sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for n in (145,148):
 c=next((R/f'campaigns/round-{n}').iterdir());s=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert s['status']=='completed' and s['calls']['unsettled']==0
other=next((R/'campaigns/round-149').iterdir());s=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(other/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert s['status'] in ('running','completed','failed','blocked')
if s['status'] in ('failed','blocked'):assert s['calls']['unsettled']==0
C=next((R/'campaigns/round-150').iterdir());f=json.loads((C/'freeze.json').read_text());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
for name,key in [('task.json','task_sha256'),('settings.json','settings_sha256'),('input.json','input_sha256')]:assert sha(C/name)==f[key]
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
out=C/'controller-output-LOCALONLY.log'
with out.open('xb') as log:p=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
os.kill(p.pid,0)
d={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':150,'pid':p.pid,'argv':args,'role':'author-research','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'scoped_review_only':False,'author_research_only':True,'original_closed':False,'unchanged_original_task':True,'controller_output':str(out),'private_active_output_read':False,'hot_feedback_sent':False,'launch_method':'Native cloud.sh controller in its own process session; standard Tini retained; no account, authentication, runtime or environment changes.','frozen_task_sha256':f['task_sha256'],'frozen_settings_sha256':f['settings_sha256'],'frozen_math_input_sha256':f['input_sha256'],'other_round149_public_status':s}
(C/'launch-record.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'round':150,'pid':p.pid,'role':'author-research','model':'gpt-6.1-sol','reasoning':'xhigh','other_round149_status':s['status']},indent=2))
