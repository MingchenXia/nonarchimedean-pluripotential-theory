from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, time

R=Path('/workspace/research'); K=R/'root-checks'
C=R/'campaigns/round-272/P16.7-whole383-intrinsic-E1-and-actual-branch-Dirac'
Other=R/'campaigns/round-271/P12.3-whole382380381-independent-proof-and-original-residual'
Done=R/'campaigns/round-270/P16.7-whole378-polyannulus-Picard-and-intrinsic-E1'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(c):return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=load(C/'freeze.json'); assert f['input_sha256']=='d98824a4c86633e8ff598cd649c90b03966b4ea9c515b5da1c0899b3e1a8bd3c'
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert load(C/'input.json')['notes']==[]
s=load(C/'settings.json'); assert len(s['usagePrefix'])<=91 and s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
assert not os.environ.get('XEAN_CODEX_COMMAND') and not os.environ.get('OPENAI_BASE_URL') and not os.environ.get('CODEX_BASE_URL')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
receipt=load(R/'github-checkpoint/push-receipt-continuation272.json')
assert receipt['commit_sha']=='06e845d734fa4d48a49a8bfea49c0faeef62c836'
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not receipt['force_update']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==272
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
done=status(Done); assert done['status']=='completed' and not done['error'] and done['calls']['unsettled']==0
prior=status(Other); assert not prior['error'] and prior['status'] in ['running','completed']
active=[271] if prior['calls']['unsettled'] else []; assert len(active)<2
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
deadline=time.monotonic()+12
while not (C/'work.sqlite').exists() and proc.poll() is None and time.monotonic()<deadline:time.sleep(0.2)
assert (C/'work.sqlite').exists() and proc.poll() is None,(C/'controller-output-LOCALONLY.log').read_text()[:1800]
st=status(C); assert st['status']=='running' and not st['error']; active.append(272); assert len(active)<=2
now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=272,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=[],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],usagePrefix_length=len(s['usagePrefix']),work_database_created=True,public_status=st,other_campaign_public_status=prior,completed270_public_status=done,current_active_batch=active,maximum_concurrent_campaigns=2,user_authorization=['Use gpt-6.1-sol xhigh through Xean native Codex path','Move on','Choose a few at a time'],provider_path='Existing signed-in native Codex path; inherited auth/proxy/CA; no endpoint/runtime override',source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True,original_closed=False,new_accepted_paper=False)
write(C/'launch-record.json',record)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=active,native272_whole383_P16_7=dict(directory=str(C),pid=proc.pid,status='RUNNING initialized native campaign',input_sha256=f['input_sha256'],only_grants=[]),next_work='TWO maximum nativegpt6.1solxhigh:271 independent whole382380381/HH proof and originalP12.3;272 independent whole383 finitePicard/nonalgebraization/constantbranchenergy then intrinsicE1 and finite-depth analyticDirac. ROOT publish273 entire383/frozen272 and271launch. No active mathematics feedback.16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.'); write(p,x)
print(json.dumps(dict(round=272,pid=proc.pid,status=st['status'],database_exists=True,input_sha256=f['input_sha256'],current_active_batch=active),indent=2))
