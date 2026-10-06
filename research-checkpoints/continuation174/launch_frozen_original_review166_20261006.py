from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R = Path('/workspace/research')
C = next((R / 'campaigns/round-166').iterdir())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
states = []
for n in (158,163):
    c = next((R / f'campaigns/round-{n}').iterdir())
    s = json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    states.append({'round':n,'public_status':s})
assert all(x['public_status']['status'] in ('running','completed') for x in states)
assert states[1]['public_status']['status'] == 'completed'
assert sum(x['public_status']['calls']['unsettled'] for x in states) <= 1
canonical = json.loads((R/'root-checks/P16.5-round163-actual-canonical-author-result-20261006.json').read_text())
assert canonical['candidate'] is True
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
freeze = json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name) == freeze[key]
settings = json.loads((C/'settings.json').read_text())
assert settings['research']['model'] == 'gpt-6.1-sol' and settings['research']['reasoning'] == 'xhigh'
assert settings['limits'] == {'concurrency':1,'attempts':1,'providerCalls':1}
args = ['bash','scripts/cloud.sh','xean','--records','review',str(C/'task.json'),str(C/'argument.md'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    pid = subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record = {'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':166,'pid':pid,'argv':args,'role':'independent-review','scope':'Entire standalone16-page original P16.5 proof and all five canonical notes under unchanged complete original task','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'frozen_task_sha256':freeze['task_sha256'],'frozen_math_input_sha256':freeze['argument_sha256'],'frozen_settings_sha256':freeze['settings_sha256'],'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,'account_auth_runtime_environment_changed':False,'parent_execution_permissions':'require_escalated for native-directory initialization, retaining native child research sandbox','prior_public_states':states,'reserved_current_batch':[x['round'] for x in states if x['public_status']['status']=='running']+[166],'prepared_support_review165_not_launched':True}
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'round':166,'pid':pid,'frozen_argument_sha256':freeze['argument_sha256'],'maximum_concurrent_campaigns':2,'originals_solved':8},indent=2))
