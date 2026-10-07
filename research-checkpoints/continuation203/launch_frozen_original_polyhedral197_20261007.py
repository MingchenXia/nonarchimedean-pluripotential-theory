from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess
R=Path('/workspace/research'); C=next((R/'campaigns/round-197').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for n,k in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/n)==f[k]
assert sha(C/'private-primary-packet-bindings.json')==f['private_primary_packet_bindings_sha256']
for e in json.loads((C/'private-primary-packet-bindings.json').read_text()):
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert 'P05.2' not in json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms']
s=json.loads((C/'settings.json').read_text())
assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh'
assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
states=[]
for n in (189,190,191,192,193,194,195,196):
    c=next((R/f'campaigns/round-{n}').iterdir())
    p=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    st=json.loads(p.stdout)
    if st['status']=='blocked':assert st['calls']['unsettled']==st['work']['active']==st['work']['queued']==0
    states.append(dict(round=n,public_status=st))
assert sum(x['public_status']['calls']['unsettled'] for x in states)<=1
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
r=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=197,pid=pid,argv=args,
    role='original-author-research',scope='Entire unchanged P05.2 after preserved whole196 FAIL, explicit PC hypothesis and genuinely coupled endpoint repair; three complete accepted grants and all clarifications;14 whole mathematical units and4 private original primary files.',
    route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,
    frozen_task_sha256=f['task_sha256'],frozen_math_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
    only_mathematical_grants=f['only_complete_grants'],original_closed=False,private_active_output_read=False,hot_feedback_sent=False,
    account_auth_runtime_environment_changed=False,parent_execution_permissions='require_escalated for exact authorized native initialization preserving workspace-write child research sandbox',
    prior_public_states=states,reserved_current_batch=[x['round'] for x in states if x['public_status']['calls']['unsettled']>0]+[197])
(C/'launch-record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(round=197,pid=pid,input_sha256=f['input_sha256'],maximum_concurrent_campaigns=2),indent=2))
