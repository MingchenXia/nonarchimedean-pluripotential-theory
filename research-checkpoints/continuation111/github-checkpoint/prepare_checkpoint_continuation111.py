"""Freeze actual108 FAIL, incomplete109, new proofs and the repaired native batch."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');G=R/'github-checkpoint'
D=G/'continuation111-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

assert not D.exists()
previous=G/'push-receipt-continuation110.json'
receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='88d50f04372a24810d2fa779adcd05c7e964d8bb'
assert sha(G/'upload-manifest-continuation110.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D.mkdir()
items=[];campaigns=[]
for no,atom,stem,session in [
    (110,'P16.5','P16.5-original-direct-foundation-repair-research',21088),
    (111,'P16.2','P16.2-original-local-operator-and-source-repair-research',22414),
    (112,'P16.5','P16.5-original-direct-foundation-length-repair-research',59577),
    (113,'P16.2','P16.2-original-local-operator-length-repair-research',43638)]:
    C=R/f'campaigns/round-{no}'/stem
    frozen=json.loads((C/'freeze.json').read_text())
    for name,key in [('input.json','input_sha256'),('task-original.json','task_sha256'),
                     ('assignment-original.txt','assignment_sha256'),('settings.json','settings_sha256')]:
        assert sha(C/name)==frozen[key]
    result=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'campaign.sqlite')],
                          cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(result.stdout)
    assert status['calls']['admitted']==1
    if no in [110,111]:
        assert status['status']=='blocked' and '1048576' in status['error']
    p=D/f'{atom}-round{no}-native-status.json';p.write_text(result.stdout)
    items.append({'round':no,'atom':atom,'directory':str(C),'tool_session_id':session,
        'observed_status':status['status'],'public_status':str(p),'public_status_sha256':sha(p),
        'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
    campaigns.append(C)
now=datetime.now(timezone.utc).isoformat()
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Fresh full-original112 P16.5 direct nonample foundation and113 P16.2 genuine local operator; oversized110/111 immutable failures.'}
save(D/'current-small-batch-observation.json',batch)
review=R/'root-checks/P16.5-round108-actual-full-original-fail-review-20261005.json'
assert json.loads(review.read_text())['verdict']=='FAIL'
P=R/'root-checks/public-P16.2-round109-final-reader'
assert json.loads((P/'canonical-native-result.json').read_text())['candidate'] is False
assert json.loads((P/'status.json').read_text())['status']=='incomplete'
reading=R/'root-checks/P16.2-round109-complete-paper-and-premises-root-reading-20261005.json'
assert json.loads(reading.read_text())['entire667_LF_paper_root_read']
bindings=[R/'root-checks/P16.2-continuation112-resolution-primary/binding.json',
          R/'root-checks/P16.2-continuation113-primary-binding.json',
          R/'root-checks/P16.5-continuation114-direct-foundation-binding.json']
for p in bindings:
    b=json.loads(p.read_text());assert sha(b['note'])==b['note_sha256'] and not b['original_closed']
    for u in b.get('units',[]):assert sha(u['path'])==u['sha256']
save(D/'actual-results-and-foundation-observation.json',{
    'recorded_utc':now,'actual108_verdict':'FAIL','actual108_report':str(review),
    'actual109_candidate':False,'actual109_reader':str(P),'actual109_pdf_pages':18,
    'new_unreviewed_bindings':[{'path':str(p),'sha256':sha(p)} for p in bindings],
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_originals':36,
    'historical_reviewed_scoped_papers':44,'counts_incremented':False,
    'whole_primary_works_root_read':False,
    'source_publication':'Original proofs, selected literal evidence and selected source responses in native packets, source citations and bindings; whole downloaded third-party primary works remain local.',
    'editor':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_or_replaced':False,'native_compiler_cells_pending':[815,831,885],
    'native_compilation_success_asserted':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=now;data['current_small_batch']=batch
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']='Checkpoint111: actual108 full-original FAIL, actual109 incomplete18-page paper, direct nonample foundation114 and source/section proofs112/113, repaired small native batch112/113. No new acceptance.'
    data['P16_5_actual_original_review108']={'verdict':'FAIL','report':str(review),'sha256':sha(review),'original_closed':False}
    data['P16_2_actual_author109']={'candidate':False,'reader':str(P),'reading':str(reading),'paper_pages':18,'original_closed':False}
    data['continuation114_unreviewed_direct_foundation']={'binding':str(bindings[-1]),'sha256':sha(bindings[-1]),'original_closed':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink()
    rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation111/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in sorted(P.rglob('*')):
    if p.is_file():add(p)
for C in campaigns:
    for name in ['input.json','task-original.json','assignment-original.txt','settings.json','freeze.json','mathematical-data-bindings.json']:
        add(C/name)
for p in bindings:
    add(p);add(json.loads(p.read_text())['note'])
for p in [review,R/'root-checks/P16.5-round108-actual-fail-root-reading-binding-20261005.json',reading,
          R/'root-checks/fresh-original-repairs110-111-preparation-20261005.json',
          R/'root-checks/native-length-recovery112-113-preparation-20261005.json',
          R/'prepare_fresh_original_repairs110_111_20261005.py',
          R/'prepare_native_length_recovery112_113_20261005.py',
          R/'preserve_actual108_and_completed109_20261005.py',
          R/'root-checks/P16.2-continuation112-resolution-primary/bind_selected_units112.py',
          R/'root-checks/bind_P16_2_continuation113_reused_primary_20261005.py',
          G/'prepare_checkpoint_continuation111.py',previous]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation111.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':36,
    'historical_reviewed_scoped_papers':44,
    'commit_message':'Repair nonample foundations after failed audit and continue two original tasks',
    'scope':'Actual108 FAIL preserved; incomplete10918-page draft and actual notes, direct single-net nonample/homogeneous/zero-class proofs114, source/finite-section proofs112/113, immutable length failures110/111 and fresh full-original native authors112/113. Six originals solved,36 open,44 reviewed scoped; existing editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
                  'statuses':[(i['round'],i['atom'],i['observed_status']) for i in items]},indent=2))
