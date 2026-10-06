from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation141.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='0664cf10ed1692ec315992a3c875468489cb15e8'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation141.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
D=G/'continuation142-publication-records';D.mkdir(exist_ok=False)
S=K/'completed125-129-and-live130-20261006-continuation142';S.mkdir(exist_ok=False)
completed={}
for n in [125,129]:
    rawpath=K/f'P16.5-round{n}-completed-native-inspection-LOCALONLY.json'
    inspection=json.loads(rawpath.read_text());result=inspection['campaign']['result']
    assert inspection['campaign']['status']=='completed'
    expected='INCONCLUSIVE' if n==125 else 'FAIL';assert result['verdict']==expected
    projection={k:v for k,v in result.items() if k!='passages'}
    projection['source_evidence_bindings']=[{'premise':p['premise'],'url':p['url'],
        'quote_sha256':hashlib.sha256(p['quote'].encode()).hexdigest()} for p in result['passages']]
    projection.update({'native_inspection_sha256':sha(rawpath),
        'source_quotations_removed_for_publication':True,'historical_result_modified':False,
        'root_read_scope':'Complete verdict and report; not every source passage in this inspection.',
        'original_closed':False,'independently_accepted':False})
    public=S/f'P16.5-round{n}-completed-review-public-projection.json';save(public,projection)
    completed[n]={'round':n,'atom':'P16.5','verdict':expected,'operation_id':result['operationId'],
        'reported_utc':result['reportedAt'],'public_result':str(public),'public_result_sha256':sha(public),
        'original_closed':False,'independently_accepted':False}
raw125=K/'P16.5-round125-actual-native-model-result-LOCALONLY.json'
model=json.loads(raw125.read_text());assert model['verdict']=='PASS'
invalid=[p for p in model['passages'] if not 0<=p['premise']<len(model['premises'])]
assert len(model['premises'])==18 and len(model['passages'])==19 and len(invalid)==1
assert invalid[0]['premise']==18 and invalid[0]['url']=='urn:xean:task'
diagnostic={'recorded_utc':now,'round':125,'native_verdict':'INCONCLUSIVE','raw_model_verdict':'PASS',
    'raw_model_result_sha256':sha(raw125),'premise_count':18,'model_passage_count':19,
    'invalid_passage':{'premise':18,'url':'urn:xean:task','quote_sha256':hashlib.sha256(invalid[0]['quote'].encode()).hexdigest()},
    'format_cause':'The extra task passage indexes premise18, outside the valid0-through17 range; the strict adapter discards it and rejects the PASS evidence binding.',
    'manual_promotion':False,'historical_result_or_validator_modified':False,
    'next_action':'Obtain a fresh correctly bound review if this scoped theorem is needed; retain the original dual verdicts.',
    'original_closed':False,'accepted_scoped_count_change':0}
save(S/'round125-native-model-dual-verdict-format-diagnostic.json',diagnostic)
observed={}
for n,label in [(125,'P16.5-entire-nef-big-variational-equation-independent-review'),
                (129,'P16.5-original-entire-general-big-equation-independent-review'),
                (130,'P19.1-original-arbitrary-ray-entropy-counterexample-independent-review')]:
    c=R/f'campaigns/round-{n}'/label
    p=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(p.stdout);assert status['status'] in ['running','completed']
    dest=S/f'round{n}-public-native-status.json';save(dest,status)
    observed[n]={'observed_status':status['status'],'observed_utc':status['observedAt'],
        'public_status':str(dest),'public_status_sha256':sha(dest)}
C=R/'campaigns/round-130/P19.1-original-arbitrary-ray-entropy-counterexample-independent-review'
correction=json.loads((C/'launch-settings-correction1.json').read_text())
assert sha(C/'settings-launch1.json')==correction['launch_settings_sha256']
assert sha(C/'task.json')==correction['task_sha256'] and sha(C/'argument.md')==correction['argument_sha256']
active130={'round':130,'atom':'P19.1','directory':str(C),'database':'review.sqlite','tool_session_id':70831,
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'scoped_review_only':False,'original_scope_review':True,'original_closed':False,
    'private_active_output_read':False,'hot_feedback_sent':False,**observed[130]}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==49
    data.update({'updated_utc':now,'P16_5_actual_scoped125':completed[125],
        'P16_5_original_review129_failed_proof_chain':completed[129],
        'P16_5_round125_format_diagnostic':diagnostic,'launched_original_P19_1_review130':active130,
        'current_small_batch':{'recorded_utc':now,'items':[active130],
            'active_items':[active130] if observed[130]['observed_status']=='running' else [],
            'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
            'focus':'P19.1 actual counterexample independent review; prepare a second candidate only after resolving its conventions.'},
        'next_work':'Repair actual big-class genuine decreasing closure and compactness; audit transcendental entropy recovery and ray normalizations; original count unchanged.',
        'github_pending_checkpoint':'continuation142 frozen'})
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,
    'historical_reviewed_scoped_papers':49,'completed125_native_verdict':'INCONCLUSIVE',
    'completed129_verdict':'FAIL','review130_status':observed[130]['observed_status'],
    'published_candidate178':False,'original_closed':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.pdf','.stdout','.stderr','.out'}
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation142/'+str(rel),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(S.iterdir()):add(p)
for p in [C/'launch-settings-correction1.json',C/'freeze.json',C/'mathematical-data-bindings.json',
          previous,R/'record_verified141_20261006.py',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation142.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
    'historical_reviewed_scoped_papers':49,
    'commit_message':'Preserve125 inconclusive evidence and129 foundational closure failure; record live130 review',
    'scope':'No new accepted solution. Preserve dual125 verdicts, failed129 proof chain, and130 unchanged original-task native review;7/42 originals solved,49 scoped papers.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'native_status':observed,'originals_solved':7,'accepted_scoped_papers':49},indent=2))
