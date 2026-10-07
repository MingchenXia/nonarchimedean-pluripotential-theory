from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-209').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
assert sha(C/'unchanged-whole-mathematical-argument.md')==f['unchanged_review_argument_sha256']==f['original_review_argument_sha256']
pb=C/'private-primary-packet-bindings.json';assert sha(pb)==f['private_primary_packet_bindings_sha256']
for e in json.loads(pb.read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
lines=(C/'unchanged-whole-mathematical-argument.md').read_text().splitlines()
for e in json.loads((C/'unchanged-mathematical-data-bindings.json').read_text()):
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['argument_inclusive_lf'];assert lines[lo-1:hi]==Path(e['source']).read_text().splitlines()
s=json.loads((C/'settings.json').read_text())
assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh'
assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
states=[]
for n in [205,206,207,208]:
    old=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if st['status']=='blocked':assert st['calls']['unsettled']==st['work']['active']==st['work']['queued']==0
    states.append(dict(round=n,public_status=st))
assert sum(e['public_status']['calls']['unsettled'] for e in states)<=1
assert next(e for e in states if e['round']==207)['public_status']['calls']['settled']==1
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
d=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=209,pid=pid,argv=args,
role='Independent whole local-source audit through supported native Codex worker, NOT canonical Xean research review',
scope='Exact unchanged269 all-genus curve source/whole33mathunits with EIGHTwholeO/D/N/T/Q/C/G/Mgrants and ALLclarifications;62immutable original files accessible through native file/shell tools. Whole preceding207 INCONCLUSIVE preserved; not supplied as a grant/verdict bias. Whole mathargument EXACTunchanged. No new273274275premises/sourceedit.',
route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,
frozen_task_sha256=f['task_sha256'],frozen_math_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],
only_mathematical_grants=f['only_mathematical_grants'],complete_math_units=33,private_primary_files=62,
original_closed=False,new_accepted_paper=False,private_active_output_read=False,hot_feedback_sent=False,
account_auth_runtime_environment_changed=False,research_role_runtime_unchanged=True,
parent_execution_permissions='require_escalated only for exact authorized native initialization; supported worker child remains workspace-write with shell enabled, writes ONLY its own new audit artifacts',
prior_public_states=states,reserved_current_batch=[e['round'] for e in states if e['public_status']['calls']['unsettled']>0]+[209])
(C/'launch-record.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(dict(round=209,pid=pid,input_sha256=f['input_sha256'],reserved_current_batch=d['reserved_current_batch']),indent=2))
