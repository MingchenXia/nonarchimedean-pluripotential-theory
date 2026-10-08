from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-240').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ('mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json'):
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert json.loads((C/'input.json').read_text())['notes']==[]
states=[]
for number in (238,239):
    old=next((R/f'campaigns/round-{number}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert st['status']=='completed' and st['calls']['unsettled']==0;states.append(dict(round=number,public_status=st))
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh'for k in ('codex','research'))
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with(C/'controller-output-LOCALONLY.log').open('xb')as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);now=datetime.now(timezone.utc).isoformat()
r=dict(recorded_utc=now,round=240,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='independent entire originalP12.2 geometric/conductor proof/source/scope review',frozen_input_sha256=f['input_sha256'],only_grants=[],whole_math_files=10,whole_math_bytes=f['whole_math_bytes'],own_evidence_files=f['own_evidence_files'],private_primary_files=23,maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=[240],author_original_candidate=True,independent_original_scope_verdict_pending=True,new_accepted_paper=False,original_closed=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(r,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==11 and x['remaining_open_original_atoms']==31 and x['historical_reviewed_scoped_papers']==89
    x.update(updated_utc=now,current_active_batch=[240],P12_2_original_whole_review240=dict(round=240,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=[],original_closed=False),next_work='Independent whole originalP12.2 review240; read completed P05.2 candidate239 and prepare its independent review. At most2 native campaigns,11 solved31 OPEN89 accepted, regular verified GitHub checkpoints.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=240,pid=pid,current_active_batch=[240],input_sha256=f['input_sha256']),indent=2))
