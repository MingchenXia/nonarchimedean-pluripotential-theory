from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,os,subprocess,time
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
C=R/'campaigns/round-277/P16.7-whole393-intrinsic-compactness-and-equation'
C276=R/'campaigns/round-276/P12.3-whole391392-formal-BIG-diagonal-and-original-residual'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(c):return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=load(C/'freeze.json');assert f['input_sha256']=='dd50b01adf7dbd181765b9128d6f16e04545df85b96fc291bdb689ef125f83b7'
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert load(C/'input.json')['notes']==[]
s=load(C/'settings.json');assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
assert not os.environ.get('XEAN_CODEX_COMMAND') and not os.environ.get('OPENAI_BASE_URL') and not os.environ.get('CODEX_BASE_URL')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
r=load(G/'push-receipt-continuation282.json');assert r['manifest_sha256']=='3a02bd8ebd104c99be5cfa77cd3dcaec9d8fa3acb1d367c54079265fff85a084' and r['commit_sha']=='8fdefde6823413db47641042e3f7ce87c7f24dc8'
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not r['force_update']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==282 and x['current_active_batch']==[276]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
other=status(C276);assert other['status'] in ['running','completed'] and not other['error'] and other['calls']['admitted']==1
active=([276] if other['status']=='running' else [])+[277];assert len(active)<=2
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
deadline=time.monotonic()+12
while not (C/'work.sqlite').exists() and proc.poll() is None and time.monotonic()<deadline:time.sleep(0.2)
assert (C/'work.sqlite').exists() and proc.poll() is None,'Native initialization failed; preserve log, no duplicate model call'
st=status(C)
while st['calls']['admitted']==0 and proc.poll() is None and time.monotonic()<deadline:time.sleep(0.4);st=status(C)
assert proc.poll() is None and st['status']=='running' and not st['error'] and st['calls']['admitted']==st['calls']['unsettled']==1
now=datetime.now(timezone.utc).isoformat()
record=dict(recorded_utc=now,round=277,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=[],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],strict_support_ID_policy=f['strict_support_ID_policy'],public_status=st,other_public_status=other,current_active_batch=active,maximum_concurrent_campaigns=2,verified_prior_checkpoint=r['commit_sha'],provider_path='Existing signed-in native Codex path unchanged; local Unixsocket process permission',source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True,original_closed=False,new_accepted_paper=False)
write(C/'launch-record.json',record)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=now,current_active_batch=active,native277_intrinsic_equation=dict(directory=str(C),pid=proc.pid,status='RUNNING one admitted native call',input_sha256=f['input_sha256'],only_grants=[]),next_work='TWO independent native276 formalBIG and277 intrinsicE1 equation. ROOT direct curve/current source and actual compactness/uniqueness replacements, no hotfeedback or active math read. Publish launch/new substantive work next283. Counts unchanged, protected editor OPEN UNCHANGED.');write(p,x)
print(json.dumps(dict(round=277,pid=proc.pid,status=st['status'],admitted=1,unsettled=1,current_active_batch=active),indent=2))
