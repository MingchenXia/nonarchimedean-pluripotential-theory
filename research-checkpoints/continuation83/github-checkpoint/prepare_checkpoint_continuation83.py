"""Freeze the new reviewed cone partial, actual author75, and two original continuations."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research'); G=R/'github-checkpoint'; D=G/'continuation83-publication-records'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
receipt=json.loads((G/'push-receipt-continuation82.json').read_text())
assert receipt['commit_sha']=='0f03d367933eccde1de155d25b5b0f0876f48102'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation82.json')==receipt['manifest_sha256']
P=R/'deliverables/scoped-P13.2-round73'; pub=json.loads((P/'publication-preparation.json').read_text())
assert pub['verdict']=='PASS' and not pub['fully_solved_original_atom']
for path,key in [('P13.2-paper.tex','source_sha256'),('P13.2-paper.pdf','pdf_sha256'),('P13.2-correctness-review.json','review_sha256')]: assert sha(P/path)==pub[key]
assert pub['premises']==6 and pub['passages']==17 and pub['local_two_pass_return_codes']==[0,0]
V=R/'root-checks/public-P16.1-round-75-final-reader'
v=json.loads((V/'root-preservation-and-read-state-continuation83.json').read_text())
assert v['whole_argument_root_read'] and v['entire_actual_four_notes_root_read'] and not v['original_closed']
assert len(v['primary_file_bindings'])==23 and len(v['literal_units'])==50
F=R/'root-checks/P16.1-fixed-bundle-rational-metric-and-exact-Gauss-cutoff-20261005-continuation83.md'
S=R/'root-checks/continuation83-fixed-bundle-metric-source-reads'
s=json.loads((S/'source-read-record.json').read_text()); assert sha(F)==s['proposal_sha256']
assert s['whole_saved_proposal_root_read'] and not s['accepted_dependency']
for u in s['units']:
    assert sha(u['source'])==u['source_sha256'] and sha(u['literal_file'])==u['literal_sha256']
    first,last=u['inclusive_one_based_LF']
    assert Path(u['literal_file']).read_bytes().decode()=='\n'.join(Path(u['source']).read_bytes().decode().split('\n')[first-1:last])
now=datetime.now(timezone.utc).isoformat(); D.mkdir(); items=[]; directories=[]
for atom,no,stem,session in [
    ('P16.1',77,'P16.1-public-source-compact-IBP-and-smooth-weak-global-equation',66863),
    ('P13.2',79,'P13.2-public-source-actual-finite-energy-realization',10689)]:
    c=R/'campaigns'/f'round-{no}'/stem; m=json.loads((c/'input-manifest.json').read_text())
    for name,key in [('input.json','input_sha256'),('settings.json','settings_sha256'),('assignment-new-prefix.txt','prefix_sha256')]: assert sha(c/name)==m[key]
    for b in m['embedded_context']: assert sha(b['path'])==b['sha256']
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'campaign.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    q=D/f'{atom}-round{no}-native-status.json'; q.write_text(proc.stdout); j=json.loads(proc.stdout)
    items.append({'atom':atom,'round':no,'role':'author','directory':str(c),'tool_session_id':session,
        'observed_status':j['status'],'status':str(q),'status_sha256':sha(q),
        'input_sha256':m['input_sha256'],'settings_sha256':m['settings_sha256'],
        'saved_prefix_settings_exact_task_root_read':True,'source_and_context_bindings_reproduced':True,
        'model':'gpt-6.1-sol','reasoning':'xhigh','hot_feedback_sent':False,'original_closed':False})
    target=D/f'round-{no}-launch'; target.mkdir()
    for name in ['input.json','settings.json','input-manifest.json','assignment-new-prefix.txt']: shutil.copyfile(c/name,target/name)
    directories.append(target)
assert len([i for i in items if i['observed_status']=='running'])<=2
failed=R/'campaigns/round-78/P13.2-public-source-reviewed-estimate-to-actual-finite-energy-realization'
assert not (failed/'campaign.sqlite').exists()
failure=json.loads((failed/'prelaunch-validation-failure.json').read_text()); assert not failure['worker_started'] and not failure['auth_failure']
target=D/'round-78-prelaunch-rejection'; target.mkdir()
for name in ['input.json','settings.json','input-manifest.json','assignment-new-prefix.txt','prelaunch-validation-failure.json']: shutil.copyfile(failed/name,target/name)
solved=['P13.1','P15.1','P15.2','P16.6']
batch={'recorded_utc':now,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'active_items':[i for i in items if i['observed_status']=='running'],'all_items':items,
    'hot_feedback_sent':False,'completed_actual_author_round75':False,'completed_actual_review_round76':'PASS',
    'completed_author_round75_candidate':False,'new_review_is_partial_only':True,'fully_solved_original_atoms':solved,
    'prelaunch_failure_round78':failure,'same_mathematical_input_relaunched_as_round79':True}
batch['completed_actual_author_round75']=True
write(D/'current-small-batch-observation.json',batch)
write(D/'reviewed-partial-publication.json',{'recorded_utc':now,'publication':str(P),
    'publication_preparation_sha256':sha(P/'publication-preparation.json'),'verdict':'PASS',
    'scope':pub['scope'],'author_round':73,'review_round':76,'premises':6,'passages':17,
    'original_closed':False,'entire_report_premises_and_passages_root_read':True,
    'exact_original_partial_task_unchanged':True,'previous_round74_verdict':'INCONCLUSIVE'})
write(D/'completed-unreviewed-author75.json',{'recorded_utc':now,'reader':str(V),
    'actual_result_sha256':sha(V/'canonical-native-result.json'),'whole_argument_and_all_four_notes_root_read':True,
    'source_binding_checks':23,'literal_unit_checks':50,'author_pdf_pages':14,'author_two_pass_compile':'SUCCESS',
    'candidate':False,'original_closed':False,'new_mathematics_independently_reviewed':False})
write(D/'native-compile-followup.json',{'recorded_utc':now,'new_publication_tex':str(P/'P13.2-paper.tex'),
    'invocation_cell':266,'state':'Pending; latest wait returned running without diagnostics.',
    'local_author_two_pass_compile':'SUCCESS','pages':11,'native_success_asserted':False,
    'current_editor_source_preserved':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex',
    'prior_original_P13_1_native_result':'No handler registered for tool: codex_app.compile_latex_document'})
a=json.loads((R/'active-work.json').read_text()); c=json.loads((R/'checklist-current.json').read_text())
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==solved
assert sum(len(t['reviewed_papers']) for t in c['targets'])==41
assert sorted(t['atom'] for t in a['full_solutions'])==solved
a['updated_utc']=now; a['current_small_batch']=batch; a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint83: accepted P13.2 partial and actual round75 unreviewed draft; root83 fixed-bundle reconstruction; original continuations77/79 active. Original solved count unchanged.'
a['native_publication_compile_addendum_continuation83']=str(D/'native-compile-followup.json')
c['updated_utc']=now; c['current_small_batch']=batch; c['active_atoms']=[i['atom'] for i in batch['active_items']]
c['latest_verified_github_checkpoint']=receipt
for i in items: next(t for t in c['targets'] if t['id']==i['atom'])['continuation83_active_native_item']=i
write(R/'active-work.json',a); write(R/'checklist-current.json',c)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
    p=Path(path); assert p.is_file() and not p.is_symlink()
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','campaign.sqlite','review.sqlite','run.json'} for x in p.relative_to(R).parts)
    assert p.suffix not in {'.sqlite','.jsonl'}
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation83/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,V,S]:
    for p in sorted(directory.rglob('*')):
        if p.is_file(): add(p)
for p in sorted(P.rglob('*')):
    if p.is_file(): add(p,'manuscript/editorial/xean_research_20261003/deliverables/scoped-P13.2-round73/'+str(p.relative_to(P)))
for p in [F,R/'publish_P13_2_partial_and_freeze_round75_root83_20261005.py',
    R/'prepare_round77_78_exact_original_continuations_20261005.py',R/'prepare_round79_after_prelaunch_validation_20261005.py',
    G/'prepare_checkpoint_continuation83.py',G/'push-receipt-continuation82.json']: add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation83.json'; assert not manifest.exists()
write(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':41,
    'current_native_batch':items,'commit_message':'Publish reviewed fixed-Reeb target estimate and continue actual realization',
    'scope':'Unchanged 11-page P13.2 partial with actual six-premise17-passage PASS; completed root-read round75 partial14-page draft; unreviewed root83 fixed-bundle metric and exact Gauss descent; two exact-original native authors77/79. Pre-worker label rejection78 preserved and repaired without mathematical/runtime/auth changes. Four original problems solved,38 open,41 scoped papers. No book edits, private transcripts, SQL, authentication or Git database.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['atom'],i['round'],i['observed_status']) for i in items],'originals_solved':4,'scoped_papers':41},indent=2))
