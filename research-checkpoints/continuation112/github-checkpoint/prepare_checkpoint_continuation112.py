"""Freeze compatible centers and the new original local common-collar proof."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'continuation112-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation111.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='fe9bf711957bc25366b945248332fd79369241dc'
assert sha(G/'upload-manifest-continuation111.json')==receipt['manifest_sha256']
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert not D.exists();D.mkdir()
items=[]
for no,atom,stem,session in [
    (112,'P16.5','P16.5-original-direct-foundation-length-repair-research',59577),
    (113,'P16.2','P16.2-original-local-operator-length-repair-research',43638)]:
    C=R/f'campaigns/round-{no}'/stem
    out=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'campaign.sqlite')],
                       cwd='/workspace/xean',capture_output=True,text=True,check=True)
    s=json.loads(out.stdout);assert s['calls']['admitted']==1
    p=D/f'{atom}-round{no}-native-status.json';p.write_text(out.stdout)
    items.append({'round':no,'atom':atom,'directory':str(C),'tool_session_id':session,
        'observed_status':s['status'],'status':str(p),'status_sha256':sha(p),
        'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
now=datetime.now(timezone.utc).isoformat()
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Two unchanged full-original native authors112/113; new115 centers and117 common-collar operator repair remain unreviewed and have not been sent as hot feedback.'}
save(D/'current-small-batch-observation.json',batch)
bindings=[R/'root-checks/P16.2-continuation115-valuative-primary/binding.json',
          R/'root-checks/P16.2-continuation116-local-operator-binding.json',
          R/'root-checks/P16.2-continuation117-local-operator-binding.json']
for p in bindings:
    b=json.loads(p.read_text());assert sha(b['note'])==b['note_sha256'] and not b['original_closed']
    for u in b.get('units',[])+b.get('reused_selected_local_primary_units',[]):assert sha(u['path'])==u['sha256']
    if 'complete_selected_original_contact_and_collar_proof' in b:
        u=b['complete_selected_original_contact_and_collar_proof'];assert sha(u['path'])==u['sha256']
save(D/'new-original-local-operator-proof-observation.json',{
    'recorded_utc':now,'bindings':[{'path':str(p),'sha256':sha(p)} for p in bindings],
    'entire_saved_new_proof_notes_root_read':True,'selected_original_contact_and_collar_body_root_read':True,
    'six_new_Stacks_selected_statement_and_printed_proof_units_root_read':True,
    'whole_primary_works_root_read':False,'independent_review_performed':False,
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_originals':36,
    'historical_reviewed_scoped_papers':44,'counts_incremented':False,
    'scope':'Locally generated actual section/contact metrics, common ordinary neighborhoods, one actual ample projective collar, bounded local approximation independence, original E1 reference-floor nonpluripolar and mixed/weighted compatibility. No arbitrary classical-psh/current density claim.',
    'editor':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'editor_modified_or_replaced':False,'native_compiler_cells_polled_still_running':[815,831,885],
    'native_compilation_success_asserted':False})
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text());assert len(data['fully_solved_original_atoms'])==6
    if name=='checklist-current.json':assert data['historical_reviewed_scoped_papers']==44
    data['updated_utc']=now;data['current_small_batch']=batch
    data['github_checkpoint' if name=='active-work.json' else 'latest_verified_github_checkpoint']=receipt
    data['github_pending_checkpoint']='Checkpoint112: actual proper centers/canonical metric and local-factorial source audit115; original section local product construction116 and explicit common-ample-collar generated-local operator repair117. No new original acceptance.'
    data['continuation116_117_unreviewed_original_local_operator']={'bindings':[str(p) for p in bindings[1:]],'original_closed':False}
    data['native_compiler_poll_continuation112']={'recorded_utc':now,'cells_still_running':[815,831,885],'success_asserted':False,'editor_modified':False}
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,D/name)
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in rel.parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation112/'+str(rel),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):
    if p.is_file():add(p)
for p in bindings:
    add(p);b=json.loads(p.read_text());add(b['note'])
    for u in b.get('units',[]):add(u['path'])
unit=json.loads(bindings[-1].read_text())['complete_selected_original_contact_and_collar_proof'];add(unit['path'])
for p in [R/'bind_continuation115_and_record_verified111_20261005.py',
          R/'bind_original_local_operator116_117_20261005.py',G/'prepare_checkpoint_continuation112.py',previous]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation112.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':36,
    'historical_reviewed_scoped_papers':44,
    'commit_message':'Construct common ample collars for original generated local products',
    'scope':'Unreviewed proper-center/canonical-metric source audit115, actual original-section local products116, explicit common actual ample collar117 with rational/real constants, arbitrary nets and correct reference; public native112/113 status; six originals solved,36 open,44 reviewed scoped, existing editor unchanged.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
                  'statuses':[(i['round'],i['atom'],i['observed_status']) for i in items]},indent=2))
