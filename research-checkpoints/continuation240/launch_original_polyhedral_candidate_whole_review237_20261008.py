from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-237').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:assert sha(C/name)==f[key]
for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
notes=json.loads((C/'input.json').read_text())['notes'];assert len(notes)==5 and {n['id']for n in notes}=={'B225','R230','S306','S307','S298'}
oldnotes=json.loads((next((R/'campaigns/round-235').iterdir())/'input.json').read_text())['notes'];assert notes==oldnotes
states=[];active=[]
for n in [235,236]:
    old=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if n==235:assert st['status']=='completed' and st['calls']['unsettled']==0
    if st['calls']['unsettled']>0:active.append(n)
    states.append(dict(round=n,public_status=st))
assert len(active)<=1
s=json.loads((C/'settings.json').read_text());assert s['codex']['model']=='gpt-6.1-sol' and s['codex']['reasoning']=='xhigh' and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with(C/'controller-output-LOCALONLY.log').open('xb')as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0)
r=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=237,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='independent entire original P05.1 candidate proof/source/scope review',frozen_input_sha256=f['input_sha256'],only_grants=f['only_grants'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],own_evidence_files=17,private_primary_files=4,maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=active+[237],author_original_candidate=True,independent_original_scope_verdict_pending=True,new_accepted_paper=False,original_closed=False,active236_data_not_fed=True,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(round=237,pid=pid,current_active_batch=active+[237],input_sha256=f['input_sha256']),indent=2))
