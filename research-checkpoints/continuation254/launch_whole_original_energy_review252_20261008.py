from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-252').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
names=['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']
for name in names:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
notes=json.loads((C/'input.json').read_text())['notes'];assert [n['id'] for n in notes]==['G331','B341']
for n,e in zip(notes,json.loads((C/'qualified-imported-note-bindings.json').read_text())):assert hashlib.sha256(n['text'].encode()).hexdigest()==e['text_sha256']
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
states=[];active=[]
for rnd in [250,251]:
    old=next((R/f'campaigns/round-{rnd}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status']=='completed' and st['calls']['unsettled']==0;states.append(dict(round=rnd,public_status=st))
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=json.loads((R/name).read_text());assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==94 and x['github_pending_checkpoint'] is None
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);active.append(252);now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=252,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='Independent entire original P12.5 plus ROOT346 Borel/nonpolar/capacity/comparison reconstruction',frozen_input_sha256=f['input_sha256'],only_grants=['G331','B341'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],whole_context_files=f['whole_context_files'],private_primary_files=f['private_primary_files'],maximum_concurrent_campaigns=2,prior_public_states=states,current_active_batch=active,new_accepted_paper=False,original_closed=False,hot_feedback_sent=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=active,P12_5_original_whole_review252=dict(round=252,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=['G331','B341'],original_closed=False),P12_5_candidate250=dict(round=250,status='Completed candidateTRUE; all9actual FINAL fields and entire NEW TeXcore physically ROOTread; completequalifiedgrants byte-matched; whole source/scope/coverage/decision read;33own104input matches; original NOTaccepted',paper_directory=str(R/'root-checks/public-P12.5-continuation347-original-finite-energy-and-decreasing-net-candidate'),original_closed=False),P12_4_original_whole_review251_status='COMPLETED candidateTRUE; actual FINAL captured; full ROOT review pending, no original closure',next_work='Read entire completed251 P12.4 independent review; native252 independently reconstructs entire originalP12.5 plus new346. Push254 complete candidate347/frozen252 launch/full251 review when read.13solved29OPEN94papers unchanged.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=252,pid=pid,current_active_batch=active,input_sha256=f['input_sha256']),indent=2))
