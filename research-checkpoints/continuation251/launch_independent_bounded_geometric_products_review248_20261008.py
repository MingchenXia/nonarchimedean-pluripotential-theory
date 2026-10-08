from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-248').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for n,k in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256'),('qualified-imported-note-bindings.json','qualified_imported_note_bindings_sha256')]:assert sha(C/n)==f[k]
for n in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','historical-own-evidence-bindings.json']:
    for e in json.loads((C/n).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
inp=json.loads((C/'input.json').read_text());assert [n['id'] for n in inp['notes']]==['G331']
entry=json.loads((C/'qualified-imported-note-bindings.json').read_text())[0];assert hashlib.sha256(inp['notes'][0]['text'].encode()).hexdigest()==entry['text_sha256']
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
states=[];active=[]
for number in [246,247]:
    old=next((R/f'campaigns/round-{number}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error']
    if number==246:assert st['status']=='completed' and st['calls']['unsettled']==0
    else:
        assert st['status'] in ['running','completed']
        if st['calls']['unsettled']:active.append(number)
    states.append(dict(round=number,public_status=st))
assert len(active)<=1
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    x=json.loads((R/n).read_text());assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==93
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);active.append(248);now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=248,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='Independent ENTIRE native246 bounded-moment and actual geometric curve paper proof/source/scope review',frozen_input_sha256=f['input_sha256'],only_grants=['G331'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],own_evidence_files=f['own_evidence_files'],maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=active,new_accepted_paper=False,original_closed=False,ROOT339_or_active247_output_supplied=False,private_active_output_read=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=json.loads(p.read_text())
    x.update(updated_utc=now,current_active_batch=active,
        P12_4_native246_whole_paper_review248=dict(round=248,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=['G331'],original_closed=False),
        P12_4_native246_completed_candidate=dict(round=246,public_directory='/workspace/research/root-checks/public-P12.4-continuation341-bounded-moment-measures-and-geometric-curve-reference-unreviewed',status='completed; actual7FINAL notes, whole53kTeX and complete source/scope ROOT read; builtin compile SUCCESS; UNREVIEWED',candidate=False,original_closed=False),
        next_work='Small batch max2: independent ROOT338/339 moment proof review247 and ENTIRE native246 bounded-moment/actual geometric curve paper review248.13solved29OPEN93accepted. Continue higher-dimensional actual Cartier comparison/locality research and regular verified checkpoints.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=248,pid=pid,current_active_batch=active,input_sha256=f['input_sha256']),indent=2))
