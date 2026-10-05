"""Freeze actual original-carrier majorants, Radon lifting and a proper toric test."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, shutil, subprocess

R=Path('/workspace/research')
G=R/'github-checkpoint'
D=G/'continuation110-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

assert not D.exists()
previous=G/'push-receipt-continuation109.json'
receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='6c479cb43325976f9bb0ad13fc391ff495c125e2'
assert sha(G/'upload-manifest-continuation109.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
bindings=[R/'root-checks/P16.2-continuation110-primary-units/binding.json',
          R/'root-checks/P16.2-continuation111-toric-primary/binding.json']
for p in bindings:
    b=json.loads(p.read_text())
    assert sha(b['note'])==b['note_sha256']
    assert not b['original_closed'] and not b['independent_review_performed']
    for u in b['units']:
        assert sha(u['path'])==u['sha256']
D.mkdir()
items=[]
for atom,role,no,stem,session,db in [
    ('P16.5','review',108,'P16.5-original-full-big-reference-independent-review',93046,'review.sqlite'),
    ('P16.2','codex',109,'P16.2-original-proper-nonprojective-input-repair-research',25239,'campaign.sqlite')]:
    C=R/f'campaigns/round-{no}'/stem
    result=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/db)],
                          cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(result.stdout)
    assert status['calls']['admitted']==1
    p=D/f'{atom}-round{no}-native-status.json'
    p.write_text(result.stdout)
    items.append({'atom':atom,'role':role,'round':no,'directory':str(C),'tool_session_id':session,
                  'observed_status':status['status'],'status':str(p),'status_sha256':sha(p),
                  'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
now=datetime.now(timezone.utc).isoformat()
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Two full-original tasks108/109; new conditional original majorant/Radon proof110 and toric properness/source proof111 are unreviewed.'}
save(D/'current-small-batch-observation.json',batch)
save(D/'new-original-carrier-proofs-observation.json',{
    'recorded_utc':now,'new_bindings':[{'path':str(p),'sha256':sha(p)} for p in bindings],
    'entire_new_notes_root_read':True,'all_selected_new_source_units_root_read':True,
    'whole_primary_works_root_read':False,'original_acceptance_count_incremented':False,
    'scoped_acceptance_count_incremented':False,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':36,'historical_reviewed_scoped_papers':44,
    'P16_5_terminal105_pdf_pages_independently_checked_with_pdfinfo':14,
    'P16_5_terminal105_native_canonical_result_returned':False,
    'source_publication':'Citation URLs, hashes and exact local extraction coordinates; downloaded third-party whole works and web/screenshot bodies remain local.',
    'editor':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_or_replaced':False,'native_compiler_cells_pending':[815,831,885],
    'native_compilation_success_asserted':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':
        assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=now
    data['current_small_batch']=batch
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']='Checkpoint110: original continuous-majorant outer energy and Radon lifting proofs, actual all-field proper nonprojective toric test and exact source-use bindings. No new acceptance; six originals solved,36 open,44 reviewed scoped papers.'
    data['continuation110_unreviewed_P16_2']={'binding':str(bindings[0]),'sha256':sha(bindings[0]),'original_closed':False}
    data['continuation111_unreviewed_P16_2']={'binding':str(bindings[1]),'sha256':sha(bindings[1]),'original_closed':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p)
    assert p.is_file() and not p.is_symlink()
    rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation110/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in bindings:
    add(p)
    add(json.loads(p.read_text())['note'])
for p in [R/'bind_continuation110_and_record_verified109_20261005.py',
          R/'root-checks/P16.2-continuation111-toric-primary/retrieve_primary111.py',
          R/'root-checks/P16.2-continuation111-toric-primary/bind_selected_units111.py',
          R/'root-checks/P16.2-continuation111-toric-primary/retrieval-manifest.json',
          G/'prepare_checkpoint_continuation110.py',previous]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation110.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':36,
    'historical_reviewed_scoped_papers':44,
    'commit_message':'Prove original continuous majorants and Radon lifting for proper carriers',
    'scope':'Unreviewed conditional P16.2 original outer energy and Radon inverse, all-field proper nonprojective Miyake-Oda test with direct wall degree proof and precise primary-source bindings; actual public status108/109. No original or scoped closure; existing editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
                  'statuses':[(i['atom'],i['round'],i['observed_status']) for i in items]},indent=2))
