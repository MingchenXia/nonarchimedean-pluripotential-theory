"""Freeze two unreviewed mathematical continuations and public native review status."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
D=G/'continuation115-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation114.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='1f36b4819cef7942581cbba13f2030d27f3a6b22'
assert sha(G/'upload-manifest-continuation114.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
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
    'focus':'Independent full-original P16.5 and P16.2 reviews; no verdict presumed.'}
save(D/'current-small-batch-observation.json',batch)
bindings=[K/'P16.2-continuation120-finite-supremum-cone-binding.json',
          K/'P16-continuation121-intrinsic-model-reference-binding.json']
notes=[]
for p in bindings:
    b=json.loads(p.read_text());assert sha(b['note'])==b['note_sha256']
    assert b['entire_saved_note_root_read'] and not b['original_closed']
    for source in b['sources']:assert sha(source['path'])==source['sha256']
    notes.append(Path(b['note']))
layout=K/'P16.2-round113-root-layout-read/root-layout-observation.json'
lo=json.loads(layout.read_text());assert sha(lo['paper_PDF'])==lo['paper_PDF_sha256']
assert lo['pages_rendered_and_root_visually_read']==[1,17] and lo['actual_PDF_pages']==17
save(D/'unreviewed-mathematics-and-layout-observation.json',{
    'recorded_utc':now,'continuation120':'Entire genuine divisor cone via normalized finite ample maxima and compact subnet',
    'continuation121':'Intrinsic model-reference envelope in the entire original genuine cone',
    'proofs_require_independent_reconstruction':True,'bindings':[str(p) for p in bindings],
    'actual_closed113_PDF_pages':17,'closed113_first_and_last_PDF_pages_root_visually_read':True,
    'all113_PDF_pages_visually_read':False,'whole_primary_works_root_read':False,
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':36,'historical_reviewed_scoped_papers':44,
    'original_counts_incremented':False,'frozen_reviews114_115_modified':False,
    'editor':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_replaced_or_new_tab_opened':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=now;data['current_small_batch']=batch
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']='Checkpoint115: unreviewed finite-maxima whole-cone proof120, intrinsic model-reference proof121, closed113 PDF layout observation and public original reviews114/115; no new acceptance.'
    for no in [114,115]:data['prepared_full_original_review'+str(no)]['status']=items[no-114]['observed_status']
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl','.pdf'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation115/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in bindings+notes+[layout,R/'record_verified114_and_bind120_20261005.py',
                        R/'bind121_and_record113_layout_20261005.py',
                        G/'prepare_checkpoint_continuation115.py',previous]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation115.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':36,
    'historical_reviewed_scoped_papers':44,
    'commit_message':'Compute retained model envelopes in the complete original metric cones',
    'scope':'Unreviewed whole-cone finite-maxima argument120 and intrinsic model-reference identity121; closed11317-page PDF layout observation; public full-original independent reviews114/115. Six originals solved,36 open,44 scoped; editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['round'],i['atom'],i['observed_status']) for i in items]},indent=2))
