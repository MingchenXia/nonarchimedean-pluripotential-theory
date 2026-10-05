"""Freeze whole-read author drafts and the two real partial mathematical reviews."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research')
G=R/'github-checkpoint'
D=G/'continuation85-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
receipt=json.loads((G/'push-receipt-continuation84.json').read_text())
assert receipt['commit_sha']=='a66b7d2daf3d5e45790661997be74330419b0e3c'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation84.json')==receipt['manifest_sha256']
prep=json.loads((R/'partial-mathematical-review80-81-preparation-20261005.json').read_text())
readers=[R/'root-checks/public-P16.1-round-77-final-reader',R/'root-checks/public-P13.2-round-79-final-reader']
for P in readers:
    f=json.loads((P/'root-preservation-and-read-state-continuation85.json').read_text())
    assert f['whole_argument_root_read'] and f['entire_four_mathematical_notes_root_read']
    assert f['whole_unit_application_and_limit_index_root_read'] and not f['original_closed']
    for b in f['primary_file_bindings']: assert sha(b['authorized'])==sha(b['local'])==b['sha256']
assert json.loads((readers[0]/'root-preservation-and-read-state-continuation85.json').read_text())['native_result_accepted_by_runtime']
assert not json.loads((readers[1]/'root-preservation-and-read-state-continuation85.json').read_text())['native_result_accepted_by_runtime']
now=datetime.now(timezone.utc).isoformat()
D.mkdir()
items=[]
for it,session in zip(prep['items'],[82517,75571]):
    C=Path(it['directory'])
    f=json.loads((C/'freeze.json').read_text())
    for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
        assert sha(C/name)==f[key]==it[key]
    for b in f['embedded_context']: assert sha(b['path'])==b['sha256']
    assert not f['author_new_mathematics_granted'] and not f['original_closed']
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'review.sqlite')],
        cwd='/workspace/xean',capture_output=True,text=True,check=True)
    p=D/f"{it['atom']}-round{it['round']}-native-status.json"
    p.write_text(proc.stdout)
    state=json.loads(proc.stdout)
    assert state['status'] in {'running','completed'}
    q=D/f"round-{it['round']}-review-inputs"
    q.mkdir()
    for name in ['task.json','argument.md','settings.json','freeze.json']: shutil.copyfile(C/name,q/name)
    items.append({**it,'role':'review','tool_session_id':session,'observed_status':state['status'],
        'status':str(p),'status_sha256':sha(p),'saved_exact_task_and_settings_root_read':True,
        'whole_embedded_mathematical_author_arguments_and_notes_root_read':True,
        'source_and_context_bindings_reproduced':True,'hot_feedback_sent':False,'original_closed':False})
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'scope':'Two precise new partial mathematical reviews, preserving unchanged original targets.',
    'author77':'Completed native partial; candidate=false; full mathematical argument and four actual native notes read.',
    'author79':'Authored partial and full mathematical notes read; native publication rejected unknown support. History unchanged; no synthesized native result.',
    'grant_registration_in_review81':'Exact accepted P13.1 and round73 bodies are explicit task background. Authored support strings are conceptual citations, not imported runtime notes.',
    'fully_solved_original_atoms':['P13.1','P15.1','P15.2','P16.6'],'remaining_open_atoms':38,
    'hot_feedback_sent':False}
write(D/'current-small-batch-observation.json',batch)
solved=batch['fully_solved_original_atoms']
a=json.loads((R/'active-work.json').read_text())
c=json.loads((R/'checklist-current.json').read_text())
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==solved
assert sum(len(t['reviewed_papers']) for t in c['targets'])==41
a['updated_utc']=c['updated_utc']=now
a['current_small_batch']=c['current_small_batch']=batch
c['active_atoms']=[i['atom'] for i in batch['active_items']]
a['completed_actual_round77_and_failed_author79_readers']={
    'P16.1':str(readers[0]),'P13.2':str(readers[1]),
    'new_math_independently_accepted':False,'originals_closed':False}
a['github_checkpoint']=c['latest_verified_github_checkpoint']=receipt
a['github_pending_checkpoint']=c['github_pending_checkpoint']='Checkpoint85: full read/preservation of actual77 and rejected authored79 partials; exact independent reviews80/81 running.'
write(R/'active-work.json',a)
write(R/'checklist-current.json',c)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
    p=Path(path)
    assert p.is_file() and not p.is_symlink()
    assert p.suffix not in {'.sqlite','.jsonl'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in p.relative_to(R).parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation85/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for P in [D,*readers]:
    for p in sorted(P.rglob('*')):
        if p.is_file(): add(p)
for p in [R/'freeze_round77_79_and_prepare_partial_reviews80_81_20261005.py',
    R/'partial-mathematical-review80-81-preparation-20261005.json',G/'prepare_checkpoint_continuation85.py',
    G/'push-receipt-continuation84.json']: add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation85.json'
assert not manifest.exists()
write(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':41,
    'commit_message':'Preserve smooth-gate and actual-realization drafts for independent review',
    'scope':'Actual native77 unreviewed12-page contact/IBP/mass/smooth-gate partial and rejected authored79 unchanged8-page all-Reeb smooth-quotient actual-realization partial. Full mathematical arguments/notes root-read;23+42 primary bindings and43+13 literal units independently reproduced. Native79 remains rejected, with no synthesized result. Precise partial reviews80/81 running. Four originals solved,38 open; no new acceptance, SQL, private transcripts, auth, Git databases or book edits.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['atom'],i['round'],i['observed_status']) for i in items]},indent=2))
