"""Freeze actual completed partials, the new Runge proposal and the next two authors."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'continuation79-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists();receipt=json.loads((G/'push-receipt-continuation78.json').read_text())
assert receipt['commit_sha']=='689cf5fb7851418b1c83151cd181ccc2cacba4d2'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation78.json')==receipt['manifest_sha256']
now=datetime.now(timezone.utc).isoformat();D.mkdir();completed=[]
readers=[]
for atom,no in [('P16.1',70),('P13.2',71)]:
    reader=R/'root-checks'/('public-'+atom+'-round-'+str(no)+'-final-reader');readers.append(reader)
    p=reader/'root-preservation-and-read-state-continuation79.json';s=json.loads(p.read_text())
    assert s['whole_argument_root_read'] and s['entire_actual_four_canonical_notes_root_read']
    assert s['all_source_application_limits_and_excerpt_index_root_read']
    assert not s['candidate'] and not s['original_closed']
    assert sha(reader/(atom+'-argument.md'))==s['argument_sha256']
    assert sha(reader/'canonical-native-result.json')==s['actual_result_sha256']
    completed.append({'atom':atom,'round':no,'status':'COMPLETED_PARTIAL','candidate':False,
        'actual_result_sha256':s['actual_result_sha256'],'reader':str(reader),
        'root_record':str(p),'root_record_sha256':sha(p),'argument_sha256':s['argument_sha256'],
        'pages':s['author_pdf_pages'],'author_local_two_pass_compile':'SUCCESS',
        'primary_file_bindings':len(s['primary_file_bindings']),
        'literal_excerpt_bindings':len(s['literal_excerpt_bindings']),
        'whole_argument_and_actual_notes_root_read':True,'independently_accepted':False})
write(D/'completed-round70-71-actual-results.json',{'recorded_utc':now,'items':completed,
    'original_solutions_added':0,'historical_reviewed_scoped_papers_added':0})
items=[]
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
        'source_count':len(m['public_sources']),
        'saved_entire_new_prefix_settings_and_unchanged_completion_criteria_root_read':True,
        'original_task_unchanged':True,'source_and_context_bindings_reproduced':True,
        'new_generated_mathematics_accepted':False,'original_closed':False,'launched':True})
assert len([i for i in items if i['observed_status']=='running'])<=2
batch={'recorded_utc':now,'active_items':[i for i in items if i['observed_status']=='running'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','hot_feedback_sent':False,
    'fully_solved_original_atoms':['P13.1','P15.1','P15.2','P16.6']}
write(D/'current-small-batch-launch-and-bindings.json',batch)
P=R/'root-checks/P16.1-explicit-strict-potential-localized-hull-and-Runge-reconstruction-20261005-continuation79.md'
S=R/'root-checks/continuation79-explicit-strict-potential-and-Runge-source-reads'
s=json.loads((S/'source-read-record.json').read_text())
assert sha(P)==s['proposal_sha256']=='999eb1c6e7b10c842b9adcb92b70a8e127b36251ab12449edab02f0747a5a665'
assert s['whole_saved_proposal_root_read'] and len(s['units'])==12 and not s['accepted_dependency']
for u in s['units']:
    assert sha(u['source'])==u['source_sha256'] and sha(u['literal_file'])==u['literal_sha256']
    first,last=u['inclusive_one_based_LF']
    assert Path(u['literal_file']).read_bytes().decode('utf-8')=='\n'.join(Path(u['source']).read_bytes().decode('utf-8').split('\n')[first-1:last])
write(D/'new-unreviewed-Runge-reconstruction.json',{'recorded_utc':now,'path':str(P),
    'sha256':sha(P),'whole_saved_root_body_read':True,'source_read_record':str(S/'source-read-record.json'),
    'source_read_record_sha256':sha(S/'source-read-record.json'),'literal_units':12,
    'accepted_dependency':False,'original_closed':False,
    'applications':'Explicit multinomial strict potential, real-support individual floors/generators, actual nonnormal pole orders, repaired local hull hypothesis, locally constant integer trace, gamma=1, strict Hartogs domains, projection and singular inductions. G1-G4 remain to reconstruct.'})
write(D/'native-compile-followup.json',{'recorded_utc':now,
    'cancelled_before_diagnostics':[{'cell_id':78,'path':str(R/'deliverables/original-P13.1/P13.1-paper.tex')},
                                  {'cell_id':53,'path':str(R/'root-checks/public-P16.1-round-68-final-reader/P16.1-paper.tex')}],
    'tool_response':'dynamic tool call was cancelled before receiving a response',
    'P13_1_retry_cell':134,'P13_1_retry_state':'Pending; no diagnostics or native success returned.',
    'local_P13_1_two_pass_compile':'SUCCESS','native_success_asserted':False,
    'source_and_editor_preserved':True})
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
solved=['P13.1','P15.1','P15.2','P16.6']
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==solved
assert sorted(s['atom'] for s in a['full_solutions'])==solved
assert sum(len(t['reviewed_papers']) for t in c['targets'])==40
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint79: actual round70/71 partial papers, root79 Runge reconstruction, active original authors round72/73.'
a['current_small_batch']=batch;a['selected_atoms']=['P13.2','P16.1']
a['completed_actual_round70_71_partials']={'record':str(D/'completed-round70-71-actual-results.json'),'items':completed}
a['prepared_P16.1_round72']=items[0];a['prepared_P13.2_round73']=items[1]
a['continuation79_unreviewed_root_proposal']={'path':str(P),'sha256':sha(P),'accepted':False,'original_closed':False}
a['native_publication_compile_addendum_continuation79']=str(D/'native-compile-followup.json')
a['next_work']='Continue original P16.1 singular Runge/envelope/equation and P13.2 normal envelope/actual realization. Read completed native outputs fully, independently review complete original candidates, then continue the next few open original problems until all42 originals are solved.'
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch']=batch
c['active_atoms']=[i['atom'] for i in batch['active_items']]
for atom,focus,gaps in [
    ('P16.1','Original author round72 active: full strict-potential/localized-hull/Runge reconstruction after actual round70 smooth weak and finite trace partial. Original equation remains open.',
     ['Full singular weak Runge/globalization and countable rational EP must be independently reconstructed.','Arbitrary-cardinality EP, onto normalization and actual variational existence on the unchanged unibranch domain remain unproved.']),
    ('P13.2','Original author round73 active: normal rational envelope base and fixed-ray actual realization after round71 finite-energy target and I-Cauchy approximate solutions. Original image sufficiency remains open.',
     ['Actual E1 completeness or an independently reconstructed normal projective envelope base is missing.','Fixed irrational-Reeb compactness/realization must preserve actual classes; nonlinear roots do not imply I completeness.']),
]:
    t=next(t for t in c['targets'] if t['id']==atom)
    t['current_focus']=focus;t['current_concrete_gaps']=gaps
    t['research_status']='original_open_completed_partial_new_author_active'
    t.setdefault('local_unaccepted_drafts',[]).append(next(d for d in completed if d['atom']==atom))
write(R/'active-work.json',a);write(R/'checklist-current.json',c)
text='ID\tClosure\tResearch\tReviewed_papers\tTitle\n'
for t in c['targets']:text+='\t'.join([t['id'],t['closure'],t['research_status'],str(len(t['reviewed_papers'])),t['title'].replace('\t',' ').replace('\n',' ')])+'\n'
(R/'checklist-current.tsv').write_text(text)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
files=[]
def add(path,remote=None):
    p=Path(path);assert p.is_file()
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation79/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in readers+[S,D]:
    for p in sorted(directory.rglob('*')):
        if p.is_file():add(p)
add(P)
for i in items:
    for n in ['input.json','settings.json','input-manifest.json']:add(Path(i['directory'])/n)
for p in [R/'root-checks/P16.1-round70-actual-result-20261005.json',R/'root-checks/P13.2-round71-actual-result-20261005.json',
    R/'prepare_continuation79_source_reads_20261005.py',R/'prepare_round70_71_final_readers_20261005_continuation79.py',
    R/'prepare_public_P16_1_complete_Runge_equation_20261005.py',R/'prepare_public_P13_2_normal_envelope_realization_20261005.py',
    G/'push-receipt-continuation78.json',G/'prepare_checkpoint_continuation79.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
p=G/'upload-manifest-continuation79.json';assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':40,
    'current_native_batch':items,'commit_message':'Reconstruct strict potentials and Runge gates after smooth trace and cone realization partials',
    'scope':'Fully root-read actual round70/71 partial proofs and four notes each,14/10-page papers,83 excerpt bindings and53 primary bindings. New root79 unreviewed Runge reconstruction and12 read literal units. Fresh original author batch72/73. Four originals closed,38 open; no new acceptance. Native compile cancellation and retry preserved. No book edits, private transcripts, SQL, auth or Git database.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items],'fully_solved_originals':4},indent=2))
