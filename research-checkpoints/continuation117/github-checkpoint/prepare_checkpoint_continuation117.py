from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
D=G/'continuation117-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation116.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='ebe44098c616f64c4caa5ac4686c81cb3e18138a'
assert sha(G/'upload-manifest-continuation116.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
binding=K/'P16.5-continuation124-explicit-big-nonnef-reference-binding.json'
b=json.loads(binding.read_text())
assert sha(b['note'])==b['note_sha256'] and b['entire_final_saved_note_root_read']
assert not b['original_closed']
response=Path(b['actual_native_source_response']['path'])
assert sha(response)==b['actual_native_source_response']['sha256']
cld=K/'P16-root-independent-CLD-analytic-frame-application-observation-20261005.json'
c=json.loads(cld.read_text())
assert sha(c['native_response']['path'])==c['native_response']['sha256']
assert not c['reading_limits']['original_closed']
assert not D.exists();D.mkdir()
items=[]
for no,atom,stem,session in [
    (114,'P16.5','P16.5-original-direct-foundation-and-local-operator-independent-review',12418),
    (115,'P16.2','P16.2-original-common-collar-and-canonical-reference-independent-review',4069)]:
    C=R/f'campaigns/round-{no}'/stem
    out=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'review.sqlite')],
                       cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(out.stdout);assert status['calls']['admitted']==1
    p=D/f'{atom}-round{no}-native-status.json';p.write_text(out.stdout)
    items.append({'round':no,'atom':atom,'directory':str(C),'tool_session_id':session,
        'observed_status':status['status'],'public_status':str(p),'public_status_sha256':sha(p),
        'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
now=datetime.now(timezone.utc).isoformat()
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'focus':'Two full-original reviews; explicit nonample reference/mass check remains unreviewed.'}
save(D/'current-small-batch-observation.json',batch)
save(D/'mathematical-and-source-reading-observation.json',{
    'recorded_utc':now,'binding':str(binding),'binding_sha256':sha(binding),
    'new_proof':'One actual big nonnef L on a blowup surface: section volume1, arbitrary rational ample-plus-effective presentations, distinct nested prescribed types, and their conditional raw masses1-epsilon^2.',
    'CLD_reading_observation':str(cld),'CLD_reading_observation_sha256':sha(cld),
    'full_CLD_native_response_uploaded':False,
    'primary_0AGQ_entire_printed_statement_and_proof_root_read':True,
    'all_recursive_background_read':False,'new_local_operator_acceptance':False,
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':36,'historical_reviewed_scoped_papers':44,
    'frozen_reviews114_115_modified':False,'original_counts_incremented':False,
    'editor_modified_replaced_or_new_tab_opened':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=now;data['current_small_batch']=batch
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']='Checkpoint117: explicit big nonnef reference/mass proof124, independent finite-stage CLD frame application reading, native compiler availability observation; full-original reviews114/115 unchanged; no new acceptance.'
    for no in [114,115]:data['prepared_full_original_review'+str(no)]['status']=items[no-114]['observed_status']
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl','.pdf'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation117/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in [binding,Path(b['note']),response,cld,previous,
          G/'prepare_checkpoint_continuation117.py',
          R/'record_verified116_20261005.py',
          R/'bind124_and_record_CLD_frame_sources_and_compiler_availability_20261005.py']:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation117.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':36,
    'historical_reviewed_scoped_papers':44,
    'commit_message':'Check prescribed masses on an actual big nonnef bundle',
    'scope':'Unreviewed explicit reference/mass proof124 and independent CLD finite-stage analytic frame application reading. Public full-original reviews114/115. Six originals solved,36 open,44 scoped; editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['round'],i['atom'],i['observed_status']) for i in items]},indent=2))

