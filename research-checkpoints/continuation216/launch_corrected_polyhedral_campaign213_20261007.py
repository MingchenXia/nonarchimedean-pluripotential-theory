from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-213').iterdir());sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('unmodified-round212-task.json','unmodified_round212_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('normalization-data.json','normalization_data_sha256')]:assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(next((R/'campaigns/round-211').iterdir())/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status']=='completed' and st['calls']['unsettled']==0
old=next((R/'campaigns/round-212').iterdir());assert not (old/'work.sqlite').exists()
s=json.loads((C/'settings.json').read_text());assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=213,pid=pid,argv=args,route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',frozen_task_sha256=f['task_sha256'],frozen_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],only_mathematical_grants=f['only_mathematical_grants'],whole_math_files=f['whole_math_files'],unreviewed_working_data_not_grants=True,private_primary_files=4,maximum_concurrent_campaigns=2,prior211_public_status=st,prior212_failed_before_provider=True,reserved_current_batch=[213],original_closed=False,new_accepted_paper=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(round=213,pid=pid,input_sha256=f['input_sha256']),indent=2))
