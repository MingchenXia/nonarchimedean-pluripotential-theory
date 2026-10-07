from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-212').iterdir());sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists();f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==f[key]
for filename in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/filename).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
s=json.loads((C/'settings.json').read_text());assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
states=[]
for n in [210,211]:
    old=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);states.append(dict(round=n,public_status=st))
assert sum(e['public_status']['calls']['unsettled'] for e in states)<=1 and next(e for e in states if e['round']==210)['public_status']['status']=='completed'
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
d=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=212,pid=pid,argv=args,route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],only_mathematical_grants=f['only_mathematical_grants'],whole_math_files=f['whole_math_files'],new_working276277278_not_grants=True,private_primary_files=4,maximum_concurrent_campaigns=2,prior_public_states=states,reserved_current_batch=[e['round'] for e in states if e['public_status']['calls']['unsettled']>0]+[212],original_closed=False,new_accepted_paper=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True,parent_execution_permissions='Authorized native initialization only; supported worker child retains workspace-write/native shell and may write only own fresh artifacts')
(C/'launch-record.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(dict(round=212,pid=pid,reserved_current_batch=d['reserved_current_batch'],input_sha256=f['input_sha256']),indent=2))
