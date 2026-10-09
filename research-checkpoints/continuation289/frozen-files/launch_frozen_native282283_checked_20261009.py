from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,time,sys
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
n=int(sys.argv[1]);assert n in [282,283]
labels={282:'P16.7-whole402403404-generated-uniqueness-and-compactness',283:'P12.3-whole405-contact-and-arbitrary-envelope-residual'}
C=R/f'campaigns/round-{n}'/labels[n];expected_batch=[] if n==282 else [282];grants=[] if n==282 else ['G331']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(c):return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not os.environ.get('XEAN_CODEX_COMMAND') and not os.environ.get('OPENAI_BASE_URL') and not os.environ.get('CODEX_BASE_URL')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
receipt=load(G/'push-receipt-continuation288.json');assert receipt['commit_sha']=='b1a3de693bbfae52f95de50e2bfc5285b6bcf63a' and not receipt['force_update']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
if n==283:
    st=status(R/'campaigns/round-282'/labels[282]);assert st['status']=='running' and st['calls']['admitted']==st['calls']['unsettled']==1 and st['work']['active']==1 and not st['error']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert x['current_active_batch']==expected_batch and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==288
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
assert not C.joinpath('work.sqlite').exists() and not C.joinpath('launch-record.json').exists()
f=load(C/'freeze.json')
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(Path(e['path']))==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
s=load(C/'settings.json');assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
assert [note['id'] for note in load(C/'input.json')['notes']]==f['only_grants']==grants
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with C.joinpath('controller-output-LOCALONLY.log').open('xb') as out:proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
rec=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=n,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=grants,whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],maximum_concurrent_campaigns=2,verified_prior_checkpoint=receipt['commit_sha'],provider_path='Existing user-authorized signed-in native Codex path; authentication/proxy/CA/source-frozen runtime unchanged',source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_OPEN_UNCHANGED=True,original_closed=False,new_accepted_paper=False,initialization_pending=True)
write(C/'launch-record.json',rec);deadline=time.monotonic()+15
while not C.joinpath('work.sqlite').exists() and proc.poll() is None and time.monotonic()<deadline:time.sleep(.2)
assert C.joinpath('work.sqlite').exists() and proc.poll() is None,'Preserved launch/log; inspect initialization; never duplicate call'
st=status(C)
while st['calls']['admitted']==0 and proc.poll() is None and time.monotonic()<deadline:time.sleep(.3);st=status(C)
rec.update(public_status=st,initialization_pending=False);write(C/'launch-record.json',rec)
assert proc.poll() is None and st['status']=='running' and not st['error'] and st['calls']['admitted']==st['calls']['unsettled']==1,'Inspect preserved state; no duplicate worker'
batch=expected_batch+[n];assert len(batch)<=2;rec['current_active_batch']=batch;write(C/'launch-record.json',rec)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_active_batch=batch,next_work='Native282 independently audits whole revised402403 generated uniqueness/point atoms and404 finite-extension/probe control; continue actual compactness/existence. Native283 independently audits whole405 and advances arbitrary P12.3 envelopes. ROOT independent original-residual mathematics and regular verified NONFORCE publication. At mostTWO, no hot feedback/count change; protected editor OPEN UNCHANGED.')
    x[f'native{n}_current']=dict(directory=str(C),pid=proc.pid,status='RUNNING one admitted native call',input_sha256=f['input_sha256'],only_grants=grants);write(p,x)
print(json.dumps(dict(round=n,pid=proc.pid,status=st['status'],admitted=1,unsettled=1,current_active_batch=batch,model='gpt-6.1-sol',reasoning='xhigh'),indent=2))
