"""Launch exactly one frozen, explicitly authorized official native worker."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys,time

R=Path('/workspace/research');K=R/'root-checks';number=int(sys.argv[1]);assert number in [300,301]
suffixes={298:'P12.3-whole429430-normal-finite-cover-envelope-transfer',299:'P16.7-whole432-two-point-mass-and-whole-dirac',300:'P12.3-whole435-normal-nonisolated-and-conductor-classification',301:'P16.7-whole434436437-isotropic-dirac-and-actual-recognition'}
campaign=lambda n:R/f'campaigns/round-{n}'/suffixes[n]
C=campaign(number)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(c):
    return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not any(os.environ.get(k) for k in ['XEAN_CODEX_COMMAND','OPENAI_BASE_URL','CODEX_BASE_URL'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
receipt=load(R/'github-checkpoint/push-receipt-continuation310.json')
assert receipt['commit_sha']=='4a6c9682257ba9124490e399b631c6b2435a8526' and not receipt['force_update']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
previous=[]
for n in [298,299]+([300] if number==301 else []):
    st=status(campaign(n));assert not st['error'] and st['status'] in ['running','completed']
    if n in [298,299]:assert st['status']=='completed' and st['calls']['unsettled']==0 and st['work']['active']==0
    previous.append(dict(round=n,status=st))
assert sum(e['status']['work']['active'] for e in previous)<=1
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name);assert y['current_active_batch']==([] if number==300 else [300]) and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==310
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
assert not (C/'work.sqlite').exists() and not (C/'launch-record.json').exists()
f=load(C/'freeze.json')
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
s=load(C/'settings.json');assert s['limits']==dict(concurrency=1,attempts=1,providerCalls=1)
assert all(s[k]['model']=='gpt-6.1-sol' and s[k]['reasoning']=='xhigh' for k in ['codex','research'])
assert s['profiles']['default']['model']=='gpt-6.1-sol' and s['profiles']['default']['reasoning']=='xhigh'
assert [n['id'] for n in load(C/'input.json')['notes']]==(['G331'] if number==300 else [])==f['only_grants']
args=['bash','scripts/cloud.sh','xean','--records','role','codex',str(C/'input.json'),str(C/'work.sqlite'),str(C/'settings.json')]
with (C/'controller-output-LOCALONLY.log').open('xb') as out:
    proc=subprocess.Popen(args,cwd='/workspace/xean',stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
rec=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=number,pid=proc.pid,argv=args,model='gpt-6.1-sol',reasoning='xhigh',frozen_input_sha256=f['input_sha256'],only_grants=f['only_grants'],whole_math_files=f['whole_math_files'],whole_math_bytes=f['whole_math_bytes'],private_primary_files=f['private_primary_files'],whole_context_files=f['whole_context_files'],maximum_concurrent_campaigns=2,verified_prior_checkpoint=receipt['commit_sha'],previous_campaign_compact_statuses=previous,provider_path='User-authorized signed-in official OpenAI Codex CLI through Xean native Bun controller',user_authorization='Use gpt-6.1-sol xhigh through Xean nativeCodex path; user authorized uploading ANYmaterials: 授权你上传任何材料; continue a few at a time.',authentication_proxy_CA_and_native_workspace_write_sandbox_preserved=True,source_documents_and_programs_DATA=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_OPEN_UNCHANGED=True,original_closed=False,new_accepted_paper=False,current434435436437_compilation_UNVERIFIED=True,initialization_pending=True)
write(C/'launch-record.json',rec)
deadline=time.monotonic()+15
while not (C/'work.sqlite').exists() and proc.poll() is None and time.monotonic()<deadline:time.sleep(.2)
assert (C/'work.sqlite').exists() and proc.poll() is None,'Preserve failed initialization; NO duplicate worker'
st=status(C)
while st['calls']['admitted']==0 and proc.poll() is None and time.monotonic()<deadline:time.sleep(.3);st=status(C)
active=[e['round'] for e in previous if e['status']['status']=='running']+[number]
rec.update(public_status=st,initialization_pending=False,current_active_batch=active);write(C/'launch-record.json',rec)
assert proc.poll() is None and st['status']=='running' and not st['error'] and st['calls']['admitted']==st['calls']['unsettled']==1,'Inspect retained evidence; NO duplicate calls'
assert len(active)<=2
for name in ['active-work.json','checklist-current.json']:
    p=R/name;y=load(p);y.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_active_batch=active,active_atoms=['P12.3','P16.7'],next_work='Native300301smallbatch official6.1solxhigh; NORMALnonisolated/conductor andOLDisotropicwholeDirac/actualrecognition. Noactive math/hotfeedback. PublishNONFORCE311 WHOLE434435436437 andfrozen300301 usingboundedsegmentedtransport. Continueindependentresearch; counts/editorunchanged,originalsOPEN,compilerunverified.')
    y[f'native{number}_current']=dict(directory=str(C),pid=proc.pid,status='RUNNING one admitted nativecall',input_sha256=f['input_sha256'],only_grants=f['only_grants']);write(p,y)
print(json.dumps(dict(round=number,pid=proc.pid,status=st['status'],admitted=1,unsettled=1,current_active_batch=active,model='gpt-6.1-sol',reasoning='xhigh'),indent=2))
