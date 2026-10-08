from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess

R=Path('/workspace/research');C=next((R/'campaigns/round-254').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
notes=json.loads((C/'input.json').read_text())['notes'];assert [n['id'] for n in notes]==['G331','B341','E350']
for n,e in zip(notes,json.loads((C/'qualified-imported-note-bindings.json').read_text())):assert hashlib.sha256(n['text'].encode()).hexdigest()==e['text_sha256']
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research']) and s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
old=next((R/'campaigns/round-253').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not st['error'] and st['status'] in ['running','completed'];active=[253] if st['calls']['unsettled'] else []
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=json.loads((R/name).read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==256
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);active.append(254);assert len(active)<=2;now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=254,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',native_role='Solve residual whole ORIGINAL P12.3 normal excellent envelope positivity/regularity after full energy/capacity calculus',frozen_input_sha256=f['input_sha256'],only_grants=['G331','B341','E350'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],whole_context_files=f['whole_context_files'],private_primary_files=f['private_primary_files'],maximum_concurrent_campaigns=2,prior_public_state253=st,current_active_batch=active,new_accepted_paper=False,original_closed=False,hot_feedback_sent=False,private_ACTIVE253_output_read_or_supplied=False,account_auth_runtime_environment_changed=False,protected_editor_unchanged_open=True)
(C/'launch-record.json').write_text(json.dumps(record,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=active,P12_3_original_normal_envelope_solve254=dict(round=254,directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=['G331','B341','E350'],original_closed=False),next_work='At most2native:253wholeP12.6+348 frozen and254wholeP12.3 normalenvelope afterentirequalifiedE350. New349forindependentP12.6 review onlyafter253complete, nohotfeedback.15solved27OPEN96papers, verifiedGitHub256; compiler1010unverified; protectedP16editorOPENUNCHANGED.')
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=254,pid=pid,current_active_batch=active,input_sha256=f['input_sha256']),indent=2))
