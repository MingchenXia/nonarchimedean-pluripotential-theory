from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-233').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
 for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
x=json.loads((C/'input.json').read_text());assert [n['id'] for n in x['notes']]==f['only_grants'] and len(x['notes'])==5
for n,b in zip(x['notes'],json.loads((C/'qualified-imported-note-bindings.json').read_text())):
 assert n['id']==b['id'] and hashlib.sha256(n['text'].encode()).hexdigest()==b['text_sha256'] and n['imported'] and n['verified'] and not n['dead'] and not n['checks']
states=[];active=[]
for number in [231,232]:
 old=next((R/f'campaigns/round-{number}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 if number==231:assert st['status']=='blocked' and st['calls']['unsettled']==0 and st['error']=='Unknown, dead, or forward support: S306'
 if st['status']=='running':active.append(number)
 states.append(dict(round=number,public_status=st))
assert len(active)<=1
s=json.loads((C/'settings.json').read_text());assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=233,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role=f['native_role'],frozen_input_sha256=f['input_sha256'],only_grants=f['only_grants'],structured_imported_notes_count=5,whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=4,maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=active+[233],native231_registration_failure_preserved=True,native231_only_unreviewed_DATA=True,active232_math_outputs_not_fed=True,original_closed=False,new_accepted_paper=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(round=233,pid=pid,current_active_batch=active+[233],input_sha256=f['input_sha256'],registered_support_IDs=f['only_grants']),indent=2))
