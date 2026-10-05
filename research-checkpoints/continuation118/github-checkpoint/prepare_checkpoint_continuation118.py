from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
D=G/'continuation118-publication-records';P=R/'deliverables/original-P16.2'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation117.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='356b309610962137233ff2f0e76ff0c4518555ca'
assert sha(G/'upload-manifest-continuation117.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
closure=json.loads((P/'P16.2-original-closure.json').read_text())
assert closure['fully_solved_original_atom'] and closure['verdict']=='PASS'
for key in ['source','pdf','argument','review']:
    assert sha(closure[key])==closure[key+'_sha256']
assert closure['pages']==28
assert not D.exists();D.mkdir()
items=[]
for no,atom,stem,session in [
    (114,'P16.5','P16.5-original-direct-foundation-and-local-operator-independent-review',12418),
    (115,'P16.2','P16.2-original-common-collar-and-canonical-reference-independent-review',4069)]:
    C=R/f'campaigns/round-{no}'/stem
    out=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'review.sqlite')],
        cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(out.stdout);assert status['calls']['admitted']==1
    f=D/f'{atom}-round{no}-native-status.json';f.write_text(out.stdout)
    items.append({'round':no,'atom':atom,'directory':str(C),'tool_session_id':session,
        'observed_status':status['status'],'public_status':str(f),'public_status_sha256':sha(f),
        'original_closed':no==115,'private_active_output_read':False,'hot_feedback_sent':False})
now=datetime.now(timezone.utc).isoformat()
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'focus':'Complete original P16.2 accepted and published; P16.5 full-original review continues; one slot free for next small batch.'}
save(D/'current-small-batch-observation.json',batch)
save(D/'accepted-original-and-publication-observation.json',{'recorded_utc':now,
    'atom':'P16.2','exact_scope':closure['exact_scope'],'canonical_operation_id':closure['operation_id'],
    'canonical_sha256':closure['review_sha256'],'premises':32,'passages':54,
    'all_report_premises_passage_objects_root_read':True,
    'standalone_pdf_pages':28,'local_two_pass_build':'SUCCESS','native_compiler_success_asserted':False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,
    'fully_solved_original_atoms':sorted(receipt['fully_solved_original_atoms']+['P16.2']),
    'remaining_open_originals':35,'historical_reviewed_scoped_papers':44,
    'unreviewed120_125_proofs_imported_into_accepted_paper':False,
    'whole_third_party_papers_or_images_uploaded':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;a=json.loads(p.read_text());assert len(a['fully_solved_original_atoms'])==7
    if name=='checklist-current.json':assert a['historical_reviewed_scoped_papers']==44
    a['updated_utc']=now;a['current_small_batch']=batch
    a['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    a['github_pending_checkpoint']='Checkpoint118: full-original P16.2 accepted PASS115 with complete 28-page standalone proof and publication/source bindings;7 originals solved,35 open.'
    a['prepared_full_original_review114']['status']=items[0]['observed_status']
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'}
    if p.suffix=='.pdf':assert p==P/'P16.2-paper.pdf'
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation118/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in sorted(P.iterdir()):
    if p.is_file() and (p.suffix in {'.md','.tex','.json','.patch','.pdf'}):add(p)
for p in [K/'P16.2-round115-actual-full-original-review-20261005.json',
          K/'P16.2-round115-canonical-reading-and-publication-binding-20261005.json',
          K/'P16.2-original-scope-closure-20261005.json',previous,
          R/'record_verified117_20261005.py',
          R/'prepare_original_P16_2_review115_publication_20261005.py',
          R/'edit_and_build_original_P16_2_publication_20261005.py',
          R/'repair_original_P16_2_set_difference_typography_20261005.py',
          R/'record_original_P16_2_publication_and_closure_20261005.py',
          G/'prepare_checkpoint_continuation118.py']:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation118.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':sorted(receipt['fully_solved_original_atoms']+['P16.2']),
    'remaining_open_atoms':35,'historical_reviewed_scoped_papers':44,
    'commit_message':'Publish full-original proper nonprojective equation proof P16.2',
    'scope':'Full original retained-datum P16.2 canonical PASS115 with all32 premises and54 passages read/bound, integrated 28-page standalone paper and publication records;7 originals solved,35 open,44 scoped. P16.5 full-original review114 continues. Existing P16.4 editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['round'],i['atom'],i['observed_status']) for i in items]},indent=2))
