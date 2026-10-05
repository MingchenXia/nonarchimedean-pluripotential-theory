"""Freeze the closed proper-nonprojective draft and the two full-original reviews."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
D=G/'continuation114-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation113.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='bc70815f2502f7232c0648f6ee6c42226c6200d0'
assert sha(G/'upload-manifest-continuation113.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert not D.exists();D.mkdir()
items=[];campaigns=[]
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
    campaigns.append(C)
now=datetime.now(timezone.utc).isoformat()
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'focus':'Complete original114 P16.5 review and115 P16.2 review; both closed native authors112/113 returned candidate=false.'}
save(D/'current-small-batch-observation.json',batch)
P=K/'public-P16.2-round113-final-reader'
observation=json.loads((P/'root-terminal-reader-observation.json').read_text())
assert observation['entire478_LF_paper_root_read'] and observation['entire_actual3_canonical_notes_root_read']
assert observation['candidate'] is False and not observation['original_closed']
for f in observation['copied_artifacts']:assert sha(P/f['path'])==f['sha256']
binding=K/'P16.2-continuation119-continuous-canonical-reference-binding.json';b=json.loads(binding.read_text())
assert sha(b['note'])==b['note_sha256'] and not b['original_closed']
V=campaigns[1];f=json.loads((V/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('task-original.json','original_task_sha256'),
                 ('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(V/name)==f[key]
assert f['unchanged_original_task'] and f['review_original_full_task']
save(D/'full-original113-draft-and115-review-observation.json',{
    'recorded_utc':now,'reader':str(P),'author_candidate':False,'native_result_returned':True,
    'entire_paper_and_canonical_notes_root_read':True,'all22_exact_premise_statements_root_read':True,
    'actual_PDF_pages':17,'native_note_reported_PDF_pages':16,'actual_PDF_bytes':153263,
    'original_continuous_canonical_reference_proof119':str(binding),
    'full_original_review115_freeze':str(V/'freeze.json'),'exact_original_task_unchanged':True,
    'whole_primary_works_root_read':False,'recursive_background_all_read':False,
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_originals':36,
    'historical_reviewed_scoped_papers':44,'original_counts_incremented':False,
    'editor':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_or_replaced':False,'whole_third_party_PDFs_published':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=now;data['current_small_batch']=batch
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']='Checkpoint114: complete closed native113 candidate=false17-page P16.2 manuscript and actual notes, canonical-reference/frame proof119, unchanged full-original review115 and public small-batch114/115 state; no new acceptance.'
    for no in [114,115]:data['prepared_full_original_review'+str(no)]['status']=items[no-114]['observed_status']
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation114/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in sorted(P.rglob('*')):
    if p.is_file():add(p)
for name in ['task.json','task-original.json','argument.md','settings.json','freeze.json','mathematical-data-bindings.json']:add(V/name)
for p in [binding,Path(b['note']),R/'record_verified113_and_bind119_20261005.py',
          R/'preserve113_prepare_original_review115_20261005.py',
          G/'prepare_checkpoint_continuation114.py',previous]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation114.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':36,
    'historical_reviewed_scoped_papers':44,
    'commit_message':'Audit original local equation on every proper nonprojective carrier',
    'scope':'Closed native11317-page candidate=false manuscript, actual3notes and exact22premises; original canonical-reference continuity and signed frame proof119; fresh full-original115 review with complete common-collar proof117; small batch114/115. Six originals solved,36 open,44 scoped; editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['round'],i['atom'],i['observed_status']) for i in items]},indent=2))
