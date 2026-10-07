from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-204').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256'),('original-task.json','original_task_sha256')]:assert sha(C/name)==f[key]
lines=(C/'argument.md').read_text().splitlines()
for e in json.loads((C/'mathematical-data-bindings.json').read_text()):
 assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
 lo,hi=e['argument_inclusive_lf'];assert lines[lo-1:hi]==Path(e['source']).read_text().splitlines()
s=json.loads((C/'settings.json').read_text());assert s['research']['model']=='gpt-6.1-sol' and s['research']['reasoning']=='xhigh'
assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
states=[]
for n in (198,199,200,201,202,203):
 c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);states.append(dict(round=n,public_status=st))
assert sum(e['public_status']['calls']['unsettled'] for e in states)<=1
assert next(e for e in states if e['round']==202)['public_status']['calls']['settled']==1
args=['bash','scripts/cloud.sh','xean','--records','review',str(C/'task.json'),str(C/'argument.md'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
 pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=204,pid=pid,argv=args,role='independent-partial-review',scope='ENTIRE27-page262 corrected raw topology/all-continuous graph contact paper:19results/1953TeX/1878Markdown/57ledger/material/eight exact final notes. Three complete A/B/R grants and every clarification only. Full original higher-dimensional all-obstacle/nonPA/arbitrary-reference classification OPEN.',route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,frozen_task_sha256=f['task_sha256'],frozen_math_input_sha256=f['argument_sha256'],frozen_settings_sha256=f['settings_sha256'],only_mathematical_grants=['A224','B225','R230'],original_closed=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,parent_execution_permissions='require_escalated for authorized native initialization; child remains read-only with shell disabled',prior_public_states=states,reserved_current_batch=[e['round'] for e in states if e['public_status']['calls']['unsettled']>0]+[204])
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(round=204,pid=pid,argument_sha256=f['argument_sha256'],reserved_current_batch=record['reserved_current_batch']),indent=2))
