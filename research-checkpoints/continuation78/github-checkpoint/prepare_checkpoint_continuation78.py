"""Freeze the fourth accepted original paper and the next two-problem batch."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'continuation78-publication-records'
assert not D.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
receipt=json.loads((G/'push-receipt-continuation77.json').read_text())
assert receipt['commit_sha']=='2cd633554884b5c407d005dc35d756a2c419fd6f'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
P=R/'deliverables/original-P13.1'
closure=json.loads((P/'original-closure.json').read_text())
assert closure['fully_solved_original_atom'] and closure['verdict']=='PASS'
assert sha(closure['source'])==closure['source_sha256']=='11914edb12d9725765d0da6a62bcb2cf8b2e223c6049d719b0539e474c8e97e0'
assert sha(closure['pdf'])==closure['pdf_sha256']=='7289a1aa5dff5dbffb5e8e44b3f31be0553b6a364f9fbb48025e3ecfb65178af'
assert sha(closure['review'])==closure['review_sha256']=='96836626c52285d8f98450a974cd9a737a81eb13543b174008c9b7b8cc46b61e'
assert closure['pages']==17 and closure['local_two_pass_compilation']=='SUCCESS'
review=json.loads(Path(closure['review']).read_text())
assert len(review['premises'])==24 and len(review['passages'])==55
task=json.loads((P/'P13.1-original-review-task.json').read_text());covered=set()
for i,e in enumerate(review['passages']):
    assert e['id']==review['operationId']+'/'+str(i) and e['statement']==review['premises'][e['premise']]
    if e['url']=='urn:xean:task':assert e['quote'] in task['problem']+'\n'+task['completionCriteria']
    else:assert e['url'].startswith('https://')
    covered.add(e['premise'])
assert covered==set(range(24))
closure['native_compilation']='Pending built-in compile cell78 for this exact source; no native success asserted. Earlier candidate compile cell2711 disappeared after environment switch and remains unverified.'
closure['first_and_last_pages_visually_read']=True
closure['visual_checks']={k:{'path':str(P/'build'/k),'sha256':sha(P/'build'/k)} for k in ['first-page.png','last-page.png']}
write(P/'original-closure.json',closure)
now=datetime.now(timezone.utc).isoformat();D.mkdir()
write(D/'P13.1-publication-followup.json',{'recorded_utc':now,'original_closed':True,
    'review_operation_id':review['operationId'],'entire_actual_review_report_premises_passages_root_read':True,
    'all_zero_based_premise_bindings_reproduced':True,'exact_task_quotes_verified':True,
    'publication_diff_root_read':True,'new_substantive_mathematics':False,
    'publication_tex_sha256':closure['source_sha256'],'publication_pdf_sha256':closure['pdf_sha256'],
    'local_compilation':'Two passes successful','first_and_last_pages_root_visually_read':True,
    'native_compilation':closure['native_compilation'],'native_editor_source_preserved':'/workspace/research/root-checks/public-P16-round-46-final-reader/P16.4-paper.tex'})
items=[]
for atom,roundno,stem,session in [
    ('P16.1',70,'P16.1-public-source-smooth-weak-globalization-open-trace-and-unibranch-equation',24247),
    ('P13.2',71,'P13.2-public-source-accepted-Reeb-comparison-and-genuine-realization',67760)
]:
    c=R/'campaigns'/('round-'+str(roundno))/stem
    manifest=json.loads((c/'input-manifest.json').read_text())
    assert sha(c/'input.json')==manifest['input_sha256'] and sha(c/'settings.json')==manifest['settings_sha256']
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'campaign.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    p=D/(atom+'-native-status.json');p.write_text(proc.stdout)
    items.append({'atom':atom,'round':roundno,'role':'author','directory':str(c),'tool_session_id':session,
        'observed_status':json.loads(proc.stdout)['status'],'status':str(p),'status_sha256':sha(p),
        'input_sha256':manifest['input_sha256'],'settings_sha256':manifest['settings_sha256'],'accepted':False})
assert len([i for i in items if i['observed_status']=='running'])<=2
batch={'recorded_utc':now,'active_items':[i for i in items if i['observed_status']=='running'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'completed_original_atoms':['P13.1','P15.1','P15.2','P16.6'],'hot_feedback_sent':False}
write(D/'current-small-batch-observation.json',batch)
C=R/'campaigns/round-71/P13.2-public-source-accepted-Reeb-comparison-and-genuine-realization'
m=json.loads((C/'input-manifest.json').read_text());inp=json.loads((C/'input.json').read_text())
assert len(m['public_sources'])==11 and len(m['embedded_context'])==3 and inp['notes']==[]
assert inp['task']==json.loads((R/'campaigns/round-51/P13.2-public-source-fixed-Reeb-image/input.json').read_text())['task']
for s in m['public_sources']:assert sha(s['pdf'])==s['pdf_sha256'] and sha(s['literal_extract'])==s['extract_sha256']
for b in m['embedded_context']:assert sha(b['path'])==b['sha256'] and Path(b['path']).read_text() in inp['assignment']
launch={'round':71,'directory':str(C),'input_sha256':m['input_sha256'],'settings_sha256':m['settings_sha256'],
    'source_count':11,'accepted_mathematical_support':'Original P13.1 full reviewed proof and actual PASS',
    'accepted_supporting_review_sha256':m['accepted_supporting_review_sha256'],
    'saved_entire_new_prefix_settings_and_unchanged_completion_criteria_root_read':True,
    'original_task_unchanged':True,'launched':True,'tool_session_id':67760,'P13.2_original_closed':False}
write(D/'P13.2-round71-launch-and-input-bindings.json',launch)
write(D/'P16.1-round68-native-compile-pending.json',{'recorded_utc':now,'cell_id':53,
    'path':str(R/'root-checks/public-P16.1-round-68-final-reader/P16.1-paper.tex'),
    'status':'Still pending after bounded wait; no diagnostics or native success returned.'})
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
solved=['P13.1','P15.1','P15.2','P16.6']
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==solved
assert sum(len(t['reviewed_papers']) for t in c['targets'])==40
next(t for t in c['targets'] if t['id']=='P13.1')['original_solution_paper']=closure
a['full_solutions']=[closure if s.get('atom')=='P13.1' else s for s in a['full_solutions']]
assert sorted(s['atom'] for s in a['full_solutions'])==solved
write(D/'four-original-closures.json',{'recorded_utc':now,'catalogue_atoms':42,
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,
    'historical_reviewed_scoped_papers':40,'closures':a['full_solutions'],
    'review_limit':'Computational original-scope independent reconstruction, not formal proof certification or a priority claim.'})
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint78: fourth original closure P13.1, actual original review and standalone paper; active P13.2 round71 and P16.1 round70.'
a['current_small_batch']=batch;a['selected_atoms']=['P13.2','P16.1']
a['P13.1_round63_actual_original_review']['publication_source_native_compile']=closure['native_compilation']
a['P13.1_round63_actual_original_review']['publication_first_and_last_pages_visually_read']=True
a['prepared_P13.2_round71']=launch
a['next_work']='Complete the active P13.2 image/realization and P16.1 singular weak/envelope/equation originals; read actual completed outputs fully, independently review complete candidates, then move to the next few open original problems. Continue until all42 originals are solved.'
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch']=batch
c['active_atoms']=[i['atom'] for i in batch['active_items']]
next(t for t in c['targets'] if t['id']=='P13.2')['current_focus']='Original author round71 running using accepted full P13.1 comparison and uniform outer derivative. Genuine image/realization remains open.'
write(R/'active-work.json',a);write(R/'checklist-current.json',c)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
files=[]
def add(path,remote=None):
    p=Path(path);assert p.is_file()
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation78/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,P]:
    for p in sorted(directory.rglob('*')):
        if p.is_file():add(p)
for n in ['input.json','settings.json','input-manifest.json']:add(C/n)
for p in [R/'prepare_public_P13_2_accepted_comparison_realization_20261005.py',
    R/'prepare_original_P13_1_publication_20261005.py',R/'root-checks/P13.1-round63-actual-original-review-20261005.json',
    G/'push-receipt-continuation77.json',G/'prepare_checkpoint_continuation78.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
p=G/'upload-manifest-continuation78.json';assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':40,
    'current_native_batch':items,'commit_message':'Complete original nonproportional Reeb comparison and start genuine image realization',
    'scope':'Original P13.1 full PASS with24 premises/55 bound passages, exact reviewed proof,17-page clarified standalone paper and63 primary units. Four original closures; next two-problem native batch P13.2/P16.1. Native publication compile pending. No book edits, private transcripts, SQL, auth or Git database.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items],'fully_solved_originals':4},indent=2))
