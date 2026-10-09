from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, time
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
C=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status():return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
before=status(); assert before['status']=='running' and not before['error'] and before['calls']['admitted']==before['calls']['unsettled']==0 and before['pendingSignals']==1
log=(C/'controller-output-LOCALONLY.log').read_text(); assert 'EPERM' in log and 'listen' in log and '.sock' in log
f=load(C/'freeze.json'); assert f['input_sha256']=='36d6d13f18dcf92d18faa9e8cc1c371acb80841cdd45ee661d7dab4e51ca6141'
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert load(C/'input.json')['notes']==[]
s=load(C/'settings.json'); assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert not os.environ.get('XEAN_CODEX_COMMAND') and not os.environ.get('OPENAI_BASE_URL') and not os.environ.get('CODEX_BASE_URL')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
r=load(G/'push-receipt-continuation279.json'); assert r['commit_sha']=='d638f663706a2d640cdf9e2ce8f32ce20a2ab127'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
x=load(R/'active-work.json'); assert x['current_active_batch']==[] and x['github_pending_checkpoint'] is None
args=['bash','scripts/cloud.sh','xean','--records','resume',str(C/'work.sqlite')]
with (C/'resume-controller-output-LOCALONLY.log').open('xb') as out:
    proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
deadline=time.monotonic()+12; st=status()
while st['calls']['admitted']==0 and proc.poll() is None and time.monotonic()<deadline:
    time.sleep(0.4); st=status()
assert proc.poll() is None and st['status']=='running' and not st['error'] and st['calls']['admitted']==1 and st['calls']['unsettled']==1
now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=275,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=[],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],public_status=st,initialization_before_resume=before,recovery='Initial sandbox Unix-socket EPERM before ANY model admission; resume SAME initialized database with additional process permission. No frozen input or auth/proxy/CA/runtime change, no duplicate model call.',failed_initialization_log_sha256=sha(C/'controller-output-LOCALONLY.log'),current_active_batch=[275],maximum_concurrent_campaigns=2,verified_prior_checkpoint=r['commit_sha'],provider_path='Existing signed-in native Codex path unchanged',source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True,original_closed=False,new_accepted_paper=False)
write(C/'launch-record.json',record)
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,current_active_batch=[275],native275_general_E1=dict(directory=str(C),pid=proc.pid,status='RUNNING one admitted call after same-database socket recovery',input_sha256=f['input_sha256'],only_grants=[]),next_work='Native275 independent390388389/generalE1 operator. ROOT whole native274 proof/source/scope review and formal Noether-different/source investigation, then nextP12.3 campaign, at mostTWO. Publish launch/recovery next280.16solved26OPEN97accepted unchanged; protected editor OPEN UNCHANGED.'); write(p,x)
print(json.dumps(dict(round=275,pid=proc.pid,status=st['status'],admitted_calls=st['calls']['admitted'],unsettled_calls=st['calls']['unsettled'],current_active_batch=[275],same_database_resumed=True),indent=2))
