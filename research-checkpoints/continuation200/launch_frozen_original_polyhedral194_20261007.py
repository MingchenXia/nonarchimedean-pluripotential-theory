from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-194').iterdir());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
front=json.loads((R/'active-work.json').read_text());assert 'P05.2' not in front['fully_solved_original_atoms']
f=json.loads((C/'freeze.json').read_text())
for n,k in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/n)==f[k]
pb=C/'private-primary-packet-bindings.json';assert sha(pb)==f['private_primary_packet_bindings_sha256']
for e in json.loads(pb.read_text()):assert sha(Path(e['path']))==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
s=json.loads((C/'settings.json').read_text());assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']=={'concurrency':1,'attempts':1,'providerCalls':1}
states=[]
for n in (173,175,176,177,178,179,180,181,182,184,185,186,187,188,189,190,191,192,193):
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if st['status']=='blocked':assert st['calls']['unsettled']==st['work']['active']==st['work']['queued']==0
    states.append(dict(round=n,public_status=st))
assert sum(e['public_status']['calls']['unsettled'] for e in states)<=1
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=194,pid=pid,argv=args,role='original-author-research',scope='Entire unchanged originalP05.2 contact classification after three whole acceptedA224/B225/R230 grants and all clarifications; exact original family mathematical dossier, unreviewed failed ansatz229, four frozen read-only original primary files. General coefficient/regularizable-operator/growth/all-obstacle antecedents retained.',route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,frozen_task_sha256=f['task_sha256'],frozen_math_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],only_mathematical_grants=f['only_complete_grants'],original_closed=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,parent_execution_permissions='require_escalated for exact authorized native initialization preserving workspace-write child research sandbox',prior_public_states=states,reserved_current_batch=[e['round'] for e in states if e['public_status']['calls']['unsettled']>0]+[194])
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(dict(round=194,pid=pid,input_sha256=f['input_sha256'],maximum_concurrent_campaigns=2),indent=2))
