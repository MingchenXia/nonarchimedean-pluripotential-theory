from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-246').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for n,k in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:assert sha(C/n)==f[k]
for n in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/n).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
inp=json.loads((C/'input.json').read_text());assert [n['id'] for n in inp['notes']]==['G331']
e=json.loads((C/'qualified-imported-note-bindings.json').read_text())[0];assert hashlib.sha256(inp['notes'][0]['text'].encode()).hexdigest()==e['text_sha256']
states=[];active=[]
for number in [242,244,245]:
    old=next((R/f'campaigns/round-{number}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if number in [242,244]:assert st['status']=='completed' and st['calls']['unsettled']==0
    else:
        assert st['status'] in ['running','completed'] and not st['error']
        if st['calls']['unsettled']:active.append(number)
    states.append(dict(round=number,public_status=st))
assert len(active)<=1
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    x=json.loads((R/n).read_text());assert x['current_active_batch']==[245] and len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);active.append(246);now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=246,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='Entire original P12.4 actual bounded geometric products with model independence, intersection comparison, locality and continuity',frozen_input_sha256=f['input_sha256'],only_grants=['G331'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=active,new_accepted_paper=False,original_closed=False,ROOT338_conditional_DATA_not_product_grant=True,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=active,P12_4_original_bounded_products246=dict(round=246,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=['G331'],original_closed=False),next_work='Small batch max2: independent P12.3 proof/source/scope review245 and original P12.4 bounded geometric products246. Native242/244 completed candidatefalse remain separate unpublished drafts pending review.13solved29OPEN91accepted unchanged; regular verified GitHub checkpoints.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=246,pid=pid,current_active_batch=active,input_sha256=f['input_sha256']),indent=2))
