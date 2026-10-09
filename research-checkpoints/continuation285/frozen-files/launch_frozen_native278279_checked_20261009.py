from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, time
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
C={278:R/'campaigns/round-278/P12.3-whole396-corrected-formal-CE-and-original-residual',279:R/'campaigns/round-279/P16.7-whole397394395-full-uniqueness-and-compactness'}
old=[R/'campaigns/round-276/P12.3-whole391392-formal-BIG-diagonal-and-original-residual',R/'campaigns/round-277/P16.7-whole393-intrinsic-compactness-and-equation']
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p: json.loads(Path(p).read_text())
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(c): return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not os.environ.get('XEAN_CODEX_COMMAND') and not os.environ.get('OPENAI_BASE_URL') and not os.environ.get('CODEX_BASE_URL')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
receipt=load(G/'push-receipt-continuation284.json')
assert receipt['commit_sha']=='d2a8d1809109dbe2cfc92e69b30fb625d0c80ec7' and not receipt['force_update']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
for o in old:
    st=status(o); assert st['status']=='completed' and not st['error'] and st['calls']['unsettled']==0 and st['work']['active']==0
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==284 and x['current_active_batch']==[]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
active=[]; results=[]
for n,c in C.items():
    assert not (c/'work.sqlite').exists() and not (c/'launch-record.json').exists()
    f=load(c/'freeze.json')
    for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
        assert sha(c/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
    for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
        for e in load(c/name): assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
    s=load(c/'settings.json'); assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
    assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
    assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
    assert [x['id'] for x in load(c/'input.json')['notes']]==f['only_grants']
    active=[m for m in active if status(C[m])['status']=='running']; assert len(active)<2
    args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(c/'input.json'),str(c/'work.sqlite'),str(c/'settings.json')]
    with (c/'controller-output-LOCALONLY.log').open('xb') as out:
        proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
    now=datetime.now(timezone.utc).isoformat()
    record=dict(recorded_utc=now,round=n,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=f['only_grants'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],maximum_concurrent_campaigns=2,verified_prior_checkpoint=receipt['commit_sha'],provider_path='Existing signed-in native Codex path unchanged; exact authorized worker with local process permissions',source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_OPEN_UNCHANGED=True,original_closed=False,new_accepted_paper=False,initialization_pending=True)
    write(c/'launch-record.json',record)
    deadline=time.monotonic()+15
    while not (c/'work.sqlite').exists() and proc.poll() is None and time.monotonic()<deadline: time.sleep(0.2)
    assert (c/'work.sqlite').exists() and proc.poll() is None,'Initialization failed; preserved launch/log; do not duplicate call'
    st=status(c)
    while st['calls']['admitted']==0 and proc.poll() is None and time.monotonic()<deadline: time.sleep(0.3); st=status(c)
    record.update(public_status=st,initialization_pending=False); write(c/'launch-record.json',record)
    assert proc.poll() is None and st['status']=='running' and not st['error'] and st['calls']['admitted']==st['calls']['unsettled']==1,'Inspect preserved state, no duplicate worker'
    active.append(n); record['current_active_batch']=active[:]; write(c/'launch-record.json',record)
    for name in ['active-work.json','checklist-current.json']:
        p=R/name; x=load(p); x.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_active_batch=active[:],next_work='Two native278 corrected formalCE and279 full analytic uniqueness/compactness. ROOT independent remaining proof/source work. Publish whole396397 and frozen launches next285. No active math read/hot feedback, at mostTWO; counts unchanged, protected editor OPEN UNCHANGED.')
        x[f'native{n}_current']=dict(directory=str(c),pid=proc.pid,status='RUNNING one admitted native call',input_sha256=f['input_sha256'],only_grants=f['only_grants']); write(p,x)
    results.append(dict(round=n,pid=proc.pid,status=st['status'],admitted=1,unsettled=1))
print(json.dumps(dict(results=results,current_active_batch=active,model='gpt-6.1-sol',reasoning='xhigh'),indent=2))
