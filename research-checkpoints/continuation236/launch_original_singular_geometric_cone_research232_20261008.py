from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-232').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
 for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
other=next((R/'campaigns/round-231').iterdir())
status=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(other/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert status['calls']['unsettled']<=1 and status['status'] in ['running','completed']
settings=json.loads((C/'settings.json').read_text());assert settings['codex']['model']=='gpt-6.1-sol' and settings['codex']['reasoning']=='xhigh' and settings['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert f['only_grants']==[] and f['whole_math_files']==10
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
argv=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(argv,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
active=([231] if status['calls']['unsettled'] else [])+[232]
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=232,pid=pid,argv=argv,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=[],whole_math_files=10,whole_math_bytes=f['whole_math_bytes'],private_primary_files=4,maximum_concurrent_campaigns=2,prior_public_state231=status,current_active_batch=active,ROOT311_unreviewed=True,original_closed=False,new_accepted_paper=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==10 and x['historical_reviewed_scoped_papers']==88 and x['github_pending_checkpoint'] is None
 x.update(updated_utc=record['recorded_utc'],original_singular_geometric_research232=dict(directory=str(C),freeze=str(C/'freeze.json'),freeze_sha256=sha(C/'freeze.json'),launch=str(C/'launch-record.json'),launch_sha256=sha(C/'launch-record.json'),model='gpt-6.1-sol',reasoning='xhigh',original_closed=False),next_work='Continue original P05.1 all-face compatibility and original P12.2 independently geometric singular cone in a maximum-two native batch.10/42 originals solved,32OPEN,88accepted papers; P14.8 completed by the general formal-data alternative. Regular verified GitHub checkpoints; preserve current native auth and protected editor.')
 if name=='checklist-current.json':x['active_atoms']=['P05.1','P12.2']
 p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=232,pid=pid,current_active_batch=active,input_sha256=f['input_sha256']),indent=2))
