from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-203').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
pb=C/'private-primary-packet-bindings.json';assert sha(pb)==f['private_primary_packet_bindings_sha256']
for e in json.loads(pb.read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
lines=json.loads((C/'input.json').read_text())['assignment'].splitlines()
for e in json.loads((C/'mathematical-data-bindings.json').read_text()):
    assert sha(e['source'])==e['sha256'] and Path(e['source']).stat().st_size==e['bytes']
    lo,hi=e['assignment_inclusive_lf'];assert lines[lo-1:hi]==Path(e['source']).read_text().splitlines()
j=json.loads((R/'active-work.json').read_text());assert j['historical_reviewed_scoped_papers']==77 and 'P16.4' not in j['fully_solved_original_atoms']
s=json.loads((C/'settings.json').read_text())
assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
states=[]
for n in [189,190,191,192,193,194,195,196,197,198,199,200,201,202]:
    old=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if st['status']=='blocked':assert st['calls']['unsettled']==st['work']['active']==st['work']['queued']==0
    states.append(dict(round=n,public_status=st))
assert sum(e['public_status']['calls']['unsettled'] for e in states)<=1
assert next(e for e in states if e['round']==201)['public_status']['calls']['settled']==1
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
r=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=203,pid=pid,argv=args,role='original-author-research',scope='Entire unchanged original P16.4. Eight WHOLE grants/all clarifications, including newly accepted general-moment/intrinsic-target M257. Reconstruct ACTUAL positive-genus original-bundle formal pair, horizontal Cartier sections, relative ampleness, formalFS recognition and genuine raw coefficients, then advance actual all-genus/general-dimensional prescribed-target attainment and every-point uniqueness. Whole250/198 materialFAIL retained; no favorable failed-review grants.',route='Xean native Codex',model='gpt-6.1-sol',reasoning='xhigh',maximum_concurrent_campaigns=2,frozen_task_sha256=f['task_sha256'],frozen_math_input_sha256=f['input_sha256'],frozen_settings_sha256=f['settings_sha256'],only_mathematical_grants=f['only_complete_grants'],complete_math_units=f['complete_mathematical_units'],private_primary_files=f['private_primary_packet_files'],original_closed=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,parent_execution_permissions='require_escalated for exact authorized native initialization preserving workspace-write child research sandbox',prior_public_states=states,reserved_current_batch=[e['round'] for e in states if e['public_status']['calls']['unsettled']>0]+[203])
(C/'launch-record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(round=203,pid=pid,input_sha256=f['input_sha256'],maximum_concurrent_campaigns=2),indent=2))
