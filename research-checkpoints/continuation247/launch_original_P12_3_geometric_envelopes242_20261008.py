from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-242').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists()and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256']and Path(e['path']).stat().st_size==e['bytes']
inp=json.loads((C/'input.json').read_text());assert [n['id']for n in inp['notes']]==['G331']
e=json.loads((C/'qualified-imported-note-bindings.json').read_text())[0];assert hashlib.sha256(inp['notes'][0]['text'].encode()).hexdigest()==e['text_sha256']
states=[]
for number in [240,241]:
    old=next((R/f'campaigns/round-{number}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert st['status']=='completed'and st['calls']['unsettled']==0;states.append(dict(round=number,public_status=st))
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol'and s[k]['reasoning']=='xhigh'for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol'and s['profiles']['default']['reasoning']=='xhigh'
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=json.loads((R/name).read_text());assert x['current_active_batch']==[]and len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with(C/'controller-output-LOCALONLY.log').open('xb')as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);now=datetime.now(timezone.utc).isoformat()
r=dict(recorded_utc=now,round=242,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='entire originalP12.3 geometric singular/nonnormal envelope research',frozen_input_sha256=f['input_sha256'],only_grants=['G331'],whole_math_files=13,whole_math_bytes=f['whole_math_bytes'],private_primary_files=23,maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=[242],new_accepted_paper=False,original_closed=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(r,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=[242],P12_3_original_geometric_envelope242=dict(round=242,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=['G331'],original_closed=False),next_work='Continue originalP12.3 geometric envelope research242, max2 campaigns;13 solved29 OPEN91accepted; verify checkpoint247 regular publication; all remaining original problems still authorized.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=242,pid=pid,current_active_batch=[242],input_sha256=f['input_sha256']),indent=2))
