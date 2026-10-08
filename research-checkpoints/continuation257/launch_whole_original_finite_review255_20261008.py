from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-255').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
notes=json.loads((C/'input.json').read_text())['notes'];assert [n['id'] for n in notes]==['G331','G345']
for n,e in zip(notes,json.loads((C/'qualified-imported-note-bindings.json').read_text())):assert hashlib.sha256(n['text'].encode()).hexdigest()==e['text_sha256']
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research']) and s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
states={}
for round_id in [253,254]:
    old=next((R/f'campaigns/round-{round_id}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed'];states[round_id]=st
assert states[253]['status']=='completed' and states[253]['calls']['unsettled']==0
active=[254] if states[254]['calls']['unsettled'] else []
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=json.loads((R/name).read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);active.append(255);assert len(active)<=2;now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=255,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='Independent ENTIRE originalP12.6 proof/source/scope review and completion',frozen_input_sha256=f['input_sha256'],only_grants=['G331','G345'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],whole_context_files=f['whole_context_files'],private_primary_files=f['private_primary_files'],maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=active,new_accepted_paper=False,original_closed=False,hot_feedback_sent=False,private_ACTIVE254_output_read_or_supplied=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=active,P12_6_whole_original_review255=dict(round=255,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=['G331','G345'],original_closed=False),next_work='At most2 native:254normalP12.3 envelope and255wholeP12.6 independentreconstruction of352/new349/351. Push257 full frozen newpackets/candidate. Read completed whole math/source/scope before acceptance;15solved27OPEN96papers; builtin1010pending, protectededitor OPENUNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=255,pid=pid,current_active_batch=active,input_sha256=f['input_sha256']),indent=2))
