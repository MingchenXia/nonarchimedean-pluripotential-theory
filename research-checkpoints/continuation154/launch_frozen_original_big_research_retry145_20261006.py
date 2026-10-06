from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,os
R=Path('/workspace/research');C=R/'campaigns/round-145/P16.5-original-big-class-relative-floor-closure-and-entire-equation-research-retry1';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
f=json.loads((C/'freeze.json').read_text());assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
s=json.loads((C/'settings.json').read_text());assert s['codex']['workspace']==str(C/'artifacts') and s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh'
for n in [140,142,144]:
    old=next((R/f'campaigns/round-{n}').iterdir());d=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert d['work']['active']==0 and d['status']==('blocked' if n==144 else 'completed')
old=next((R/'campaigns/round-143').iterdir());d=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert d['status'] in ['running','completed']
if d['status']=='running':
    l=json.loads((old/'launch-record.json').read_text());ps=subprocess.run(['ps','-o','stat=','-p',str(l['pid'])],capture_output=True,text=True,check=True).stdout.strip();assert ps and not ps.startswith('Z')
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')];output=C/'controller-output-LOCALONLY.log'
with output.open('xb') as log:p=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
os.kill(p.pid,0)
d={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':145,'pid':p.pid,'argv':args,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'role':'author-research','scoped_review_only':False,'unchanged_original_task':True,'original_closed':False,'maximum_concurrent_campaigns':2,
    'private_active_output_read':False,'hot_feedback_sent':False,'retry_of_pre_model_configuration_failure144':True,'mathematical_input_byte_identical':True,
    'launch_method':'Native cloud.sh controller in its own process session; standard Tini cleanup retained and successful existing author-worker configuration used. No global runtime/account/authentication changes.',
    'controller_output':str(output),'frozen_task_sha256':f['task_sha256'],'frozen_settings_sha256':f['settings_sha256'],'frozen_math_input_sha256':f['input_sha256']}
(C/'launch-record.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:d[k] for k in ['round','pid','role','route','model','reasoning']},indent=2))
