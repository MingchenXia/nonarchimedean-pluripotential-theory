from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys

R=Path('/workspace/research');q=int(sys.argv[1]);assert q==258
C=next((R/f'campaigns/round-{q}').iterdir());sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=json.loads((C/'freeze.json').read_text())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
 for e in json.loads((C/name).read_text()):assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
notes=json.loads((C/'input.json').read_text())['notes'];assert [n['id'] for n in notes]==f['only_grants']
for n,e in zip(notes,json.loads((C/'qualified-imported-note-bindings.json').read_text())):assert hashlib.sha256(n['text'].encode()).hexdigest()==e['text_sha256']
s=json.loads((C/'settings.json').read_text());assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research']) and s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
states={};active=[]
for oldq in [256,257]:
 old=next((R/f'campaigns/round-{oldq}').iterdir())
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed'];states[oldq]=st
 if oldq in [256,257]:assert st['status']=='completed' and st['calls']['unsettled']==0
 if st['calls']['unsettled']:active.append(oldq)
assert len(active)<2
assert not os.environ.get('XEAN_CODEX_COMMAND') and not os.environ.get('OPENAI_BASE_URL') and not os.environ.get('CODEX_BASE_URL')
assert Path('/opt/codex/bin/codex').is_file()
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 x=json.loads((R/name).read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:pid=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True).pid
os.kill(pid,0);active.append(q);assert len(active)<=2;now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=q,pid=pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=f['only_grants'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],maximum_concurrent_campaigns=2,prior_public_status=states,current_active_batch=active,user_authorization=['Use gpt-6.1-sol xhigh through Xean’s native Codex path','授权你上传任何材料','Choose a few to solve at a time instead of doing them all together'],provider_path='Existing Xean cloud-codex native /opt/codex/bin/codex exec through signed-in OpenAI account; inherited authentication/proxy/CA, no endpoint override or third-party recipient',payload_scope='Whole research math and publicly acquired primary literature. LOCALONLY means source-body/pixel exclusion from GitHub; no credentials or auth file content read/copied/included.',account_auth_runtime_environment_changed=False,original_closed=False,new_accepted_paper=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True)
(C/'launch-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=active,next_work='At most2: native258 wholeP12.3 normalSURFACE/isolatedchar0/fullnormalization and remainingnormaldim>=3; ROOTreadcompleted256wholecandidateP12.6 andprepareindependentreview. Verifyregularcheckpoint;15solved27OPEN96papers; protectededitorOPENUNCHANGED.');x[f'native{q}_whole_original_independent_completion']=dict(directory=str(C),pid=pid,status='launched_native_gpt-6.1-sol_xhigh',input_sha256=f['input_sha256'],only_grants=f['only_grants'],original_closed=False);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(round=q,pid=pid,current_active_batch=active,input_sha256=f['input_sha256']),indent=2))
