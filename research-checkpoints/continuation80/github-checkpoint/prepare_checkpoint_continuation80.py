"""Freeze conditional fiber and finite-data descent with the existing small batch."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'continuation80-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
receipt=json.loads((G/'push-receipt-continuation79.json').read_text())
assert receipt['commit_sha']=='66a594419d3c262648e293282ecdf75f3c955568'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation79.json')==receipt['manifest_sha256']
P=R/'root-checks/P16.1-fiberwise-zero-class-and-finite-data-envelope-descent-20261005-continuation80.md'
S=R/'root-checks/continuation80-fiberwise-and-finite-data-descent-source-reads'
s=json.loads((S/'source-read-record.json').read_text())
assert sha(P)==s['proposal_sha256']=='68ec10718968af4c9c656425142fecbd1069338c8287475ce3ee3c09ecec5e2e'
assert s['whole_saved_proposal_root_read'] and len(s['units'])==12 and not s['accepted_dependency']
for u in s['units']:
    assert sha(u['source'])==u['source_sha256'] and sha(u['literal_file'])==u['literal_sha256']
    first,last=u['inclusive_one_based_LF']
    assert Path(u['literal_file']).read_bytes().decode('utf-8')=='\n'.join(Path(u['source']).read_bytes().decode('utf-8').split('\n')[first-1:last])
now=datetime.now(timezone.utc).isoformat();D.mkdir();items=[]
for atom,no,stem,session in [
    ('P16.1',72,'P16.1-public-source-explicit-strict-barrier-and-complete-unibranch-Runge-equation',40898),
    ('P13.2',73,'P13.2-public-source-normal-envelope-realization-and-fixed-ray-axioms',20042),
]:
    c=R/'campaigns'/('round-'+str(no))/stem;m=json.loads((c/'input-manifest.json').read_text())
    assert sha(c/'input.json')==m['input_sha256'] and sha(c/'settings.json')==m['settings_sha256']
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'campaign.sqlite')],
        cwd='/workspace/xean',capture_output=True,text=True,check=True)
    p=D/(atom+'-native-status.json');p.write_text(proc.stdout);status=json.loads(proc.stdout)['status']
    items.append({'atom':atom,'round':no,'role':'author','directory':str(c),
        'tool_session_id':session,'observed_status':status,'status':str(p),'status_sha256':sha(p),
        'input_sha256':m['input_sha256'],'settings_sha256':m['settings_sha256'],
        'source_count':len(m['public_sources']),'original_task_unchanged':True,
        'saved_entire_new_prefix_settings_and_unchanged_completion_criteria_root_read':True,
        'source_and_context_bindings_reproduced':True,'new_generated_mathematics_accepted':False,
        'original_closed':False,'launched':True})
assert len([i for i in items if i['observed_status']=='running'])<=2
batch={'recorded_utc':now,'active_items':[i for i in items if i['observed_status']=='running'],
    'all_items':items,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'hot_feedback_sent':False,'fully_solved_original_atoms':['P13.1','P15.1','P15.2','P16.6']}
write(D/'current-small-batch-observation.json',batch)
proposal={'recorded_utc':now,'path':str(P),'sha256':sha(P),'whole_saved_root_body_read':True,
    'source_read_record':str(S/'source-read-record.json'),
    'source_read_record_sha256':sha(S/'source-read-record.json'),'literal_units':12,
    'accepted_dependency':False,'original_closed':False,'conditional_antecedents':s['conditional_antecedents'],
    'new_mathematics':'Bounded zero-class fiber constancy via actual values after extension and strict smooth curves; proper birational minimum usc descent; finite Hdom competitor descent, positive actual MA pushforward/contact integral, and compact majorants for arbitrary-cardinality EP.',
    'remaining_requirements':'Actual metric/curve compatibility, singular countable Runge and global equality, finite geometric/model nef-data descent, actual operator identification and orthogonality/domination. Full original variational realization remains open.'}
write(D/'new-unreviewed-fiber-and-envelope-descent.json',proposal)
write(D/'native-compile-followup.json',{'recorded_utc':now,
    'P13_1_retry_cell':134,'P13_1_retry_state':'Still pending; bounded wait returned no diagnostics.',
    'local_P13_1_two_pass_compile':'SUCCESS','native_success_asserted':False,
    'source_and_editor_preserved':True,'fresh_compile_invocation_added':False})
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
solved=['P13.1','P15.1','P15.2','P16.6']
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==solved
assert sorted(t['atom'] for t in a['full_solutions'])==solved
assert sum(len(t['reviewed_papers']) for t in c['targets'])==40
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint80: conditional fiberwise zero class and finite-data arbitrary-cardinality EP descent; original authors72/73 remain unaccepted.'
a['current_small_batch']=batch;a['continuation80_unreviewed_root_proposal']=proposal
a['native_publication_compile_addendum_continuation80']=str(D/'native-compile-followup.json')
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch']=batch
c['active_atoms']=[i['atom'] for i in batch['active_items']]
for atom in ['P16.1','P13.2']:
    t=next(t for t in c['targets'] if t['id']==atom)
    t['continuation80_supporting_descent_proposal']=proposal
write(R/'active-work.json',a);write(R/'checklist-current.json',c)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
files=[]
def add(path,remote=None):
    p=Path(path);assert p.is_file()
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation80/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [S,D]:
    for p in sorted(directory.rglob('*')):
        if p.is_file():add(p)
for p in [P,R/'prepare_continuation80_source_reads_20261005.py',G/'prepare_checkpoint_continuation80.py',G/'push-receipt-continuation79.json']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
p=G/'upload-manifest-continuation80.json';assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':40,
    'current_native_batch':items,'commit_message':'Reconstruct bounded fiber constancy and finite-data envelope descent',
    'scope':'Whole root-read new conditional proposal and12 actual primary LF units with frozen bindings. Bounded zero-class fibers, birational divisorial descent, positive MA contact pushforward and finite competitor/compact-majorant extension. Existing original authors72/73 remain active or awaiting actual result read. Four originals closed,38 open; no new acceptance. No book edits, private transcripts, SQL, auth or Git database.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items],'fully_solved_originals':4},indent=2))
