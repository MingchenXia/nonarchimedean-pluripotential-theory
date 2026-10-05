"""Recover the116 preparation parse error; original helper remains preserved.
The original unmatched closing bracket failed before any script execution.
Only this syntax correction changes the preparation; mathematics stays frozen.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
D=G/'continuation116-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation115.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='2ff4b749b71408289b6f18f033f4d2476b47e0e3'
assert sha(G/'upload-manifest-continuation115.json')==receipt['manifest_sha256']
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
    'focus':'Full-original P16.5 and P16.2 independent reviews; new clarifications are unreviewed.'}
save(D/'current-small-batch-observation.json',batch)
bindings=[K/'P16-continuation122-analytic-frame-and-weighted-local-binding.json',
          K/'P16-continuation123-full-big-domain-and-growth-binding.json']
notes=[]
for p in bindings:
    b=json.loads(p.read_text());assert sha(b['note'])==b['note_sha256'] and not b['original_closed']
    assert b.get('entire_saved_note_root_read',b.get('entire_final_saved_note_root_read'))
    for source in b['sources']:assert sha(source['path'])==source['sha256']
    notes.append(Path(b['note']))
save(D/'mathematical-and-source-reading-observation.json',{
    'recorded_utc':now,'bindings':[str(p) for p in bindings],
    'new_proofs':'Analytic frame invariance in the precise generated local category; integrable actual local weights; every actual big rational bundle and equivalence of numerical and section-growth definitions.',
    'fresh_primary_reading':'Stacks0BFP,01Q3,0B5T,0BEM,0BEV,0BJ8; published Ducros3.2 complete selected statement/proof, and full printed erratum body.',
    'Ducros_first_fetch_failed_retry_succeeded':True,
    'Ducros_norm_image_and_density_application_does_not_use_the_erroneous2_8_argument':True,
    'whole_Ducros57_page_primary_work_read':False,'all_recursive_background_read':False,
    'whole_third_party_PDFs_or_full_erratum_body_published':False,
    'frozen_reviews114_115_modified':False,'original_counts_incremented':False,
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':36,'historical_reviewed_scoped_papers':44,
    'editor':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_replaced_or_new_tab_opened':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=now;data['current_small_batch']=batch
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']='Checkpoint116: analytic-frame/local-weight proof122, full-big-domain proof123, precise primary-source reading and erratum observations; unchanged independent original reviews114/115; no new acceptance.'
    for no in [114,115]:data['prepared_full_original_review'+str(no)]['status']=items[no-114]['observed_status']
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl','.pdf'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation116/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in bindings+notes+[previous,G/'prepare_checkpoint_continuation116.py',
    G/'prepare_checkpoint_continuation116_parse_recovery.py',
    R/'record_verified115_20261005.py',R/'bind122_and_record_independent_bad_fiber_source_20261005.py',
    R/'record_independent_Ducros_density_and_erratum_20261005.py',
    R/'bind123_and_record_independent_big_growth_sources_20261005.py',
    K/'P16.2-root-independent-0BFP-response-20261005.json',
    K/'P16.2-root-independent-bad-fiber-source-observation-20261005.json',
    K/'P16-root-independent-Ducros-density-and-erratum-observation-20261005.json',
    K/'P16-root-independent-big-growth-01Q3-0B5T-0BEM-response-20261005.json',
    K/'P16-root-independent-positive-ample-degree-0BEV-0BJ8-response-20261005.json']:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation116.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':36,
    'historical_reviewed_scoped_papers':44,
    'commit_message':'Check analytic metric frames and the entire actual big-bundle domain',
    'scope':'Unreviewed local-frame and integrable-weight proof122; full-big rational-domain algebraic equivalence123 with precise primary proof sources and Ducros erratum observation. Public full-original reviews114/115. Six originals solved,36 open,44 scoped; editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['round'],i['atom'],i['observed_status']) for i in items]},indent=2))
