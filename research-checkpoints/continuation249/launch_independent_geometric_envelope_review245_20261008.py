from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess
R=Path('/workspace/research');C=next((R/'campaigns/round-245').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for n,k in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256'),('author-reader-qualifications.json','author_reader_qualifications_sha256')]:assert sha(C/n)==f[k]
for n in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json']:
    for e in json.loads((C/n).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
inp=json.loads((C/'input.json').read_text());assert [n['id'] for n in inp['notes']]==['G331']
e=json.loads((C/'qualified-imported-note-bindings.json').read_text())[0];assert hashlib.sha256(inp['notes'][0]['text'].encode()).hexdigest()==e['text_sha256']
states=[]
for number in [242,244]:
    old=next((R/f'campaigns/round-{number}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert st['status']=='completed' and st['calls']['unsettled']==0;states.append(dict(round=number,public_status=st))
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    x=json.loads((R/n).read_text());assert x['current_active_batch']==[] and len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=245,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='Independent entire native242 P12.3 plus separate ROOT335 conductor criterion proof/source/scope review',frozen_input_sha256=f['input_sha256'],only_grants=['G331'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],own_evidence_files=f['own_evidence_files'],private_primary_files=f['private_primary_files'],maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=[245],author_original_candidate=False,independent_original_scope_verdict_pending=True,new_accepted_paper=False,original_closed=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=[245],P12_3_geometric_envelope_review245=dict(round=245,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=['G331'],original_closed=False),next_work='Independent whole P12.3 proof/source/scope review245 and supplementary ROOT335 criterion; max2 campaigns;13solved29OPEN91accepted. Continue next small mathematical batch and regular verified GitHub checkpoints.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=245,pid=pid,current_active_batch=[245],input_sha256=f['input_sha256']),indent=2))
