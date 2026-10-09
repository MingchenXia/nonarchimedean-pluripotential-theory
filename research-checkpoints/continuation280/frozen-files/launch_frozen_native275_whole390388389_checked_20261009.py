from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, time
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
C=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(c):return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=load(C/'freeze.json'); assert f['input_sha256']=='36d6d13f18dcf92d18faa9e8cc1c371acb80841cdd45ee661d7dab4e51ca6141'
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
receipt=load(G/'push-receipt-continuation279.json'); assert receipt['manifest_sha256']=='130f69720aef3ceec75c8682a80b058fedbf30f52da5881c1d23d47de54c3746'
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not receipt['force_update']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==279 and x['latest_verified_github_checkpoint']['commit']==receipt['commit_sha']
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
states={}
for n,dirname in [(273,'P16.7-whole385387-full-bounded-dual-and-intrinsic-E1'),(274,'P12.3-whole386-Jensen-completion-and-original-residual')]:
    states[n]=status(R/'campaigns'/('round-%d'%n)/dirname)
    assert states[n]['status']=='completed' and not states[n]['error'] and states[n]['calls']['unsettled']==0
assert load(R/'active-work.json')['current_active_batch']==[]
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
deadline=time.monotonic()+12
while not (C/'work.sqlite').exists() and proc.poll() is None and time.monotonic()<deadline:time.sleep(0.2)
assert (C/'work.sqlite').exists() and proc.poll() is None,'Native initialization failed; bounded public diagnostics separately'
st=status(C); assert st['status']=='running' and not st['error']; active=[275]
now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=275,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=[],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],work_database_created=True,public_status=st,prior_completed_campaign_public_status=states,current_active_batch=active,maximum_concurrent_campaigns=2,verified_prior_checkpoint=receipt['commit_sha'],user_authorization=['Use gpt-6.1-sol xhigh through Xean native Codex path','Move on','Choose a few at a time'],provider_path='Existing signed-in native Codex path; inherited auth/proxy/CA unchanged',source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True,original_closed=False,new_accepted_paper=False)
write(C/'launch-record.json',record)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=active,native275_general_E1=dict(directory=str(C),pid=proc.pid,status='RUNNING initialized native campaign',input_sha256=f['input_sha256'],only_grants=[]),next_work='Native275 independently reviews390388389 and advances generalE1 operator. ROOT whole native274 review, formal Noether-different/subadditivity source investigation, then nextP12.3 campaign. Publish275launch next280 with complete274 paper if reviewed. At mostTWO;16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.'); write(p,x)
print(json.dumps(dict(round=275,pid=proc.pid,status=st['status'],database_exists=True,input_sha256=f['input_sha256'],current_active_batch=active),indent=2))
