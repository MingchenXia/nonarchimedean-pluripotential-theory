"""Publish the exact round63 candidate, actual v3 review, and next two-item batch."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess

R = Path('/workspace/research')
G = R / 'github-checkpoint'
D = G / 'continuation75-publication-records'
V = R / 'root-checks/public-P13.2-round-51-mathematical-v3-review-reader'
F = R / 'root-checks/public-P13.1-round-63-final-reader'
assert not D.exists() and not V.exists()
receipt = json.loads((G / 'push-receipt-continuation74.json').read_text())
assert receipt['commit_sha'] == '9e0b62dbeefedaafd53a4ff8600641bf4590d6da'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
now = datetime.now(timezone.utc).isoformat()
D.mkdir()
V.mkdir()
old = R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-mathematical-review-v3'
actual_file = R / 'root-checks/P13.2-round51-mathematical-v3-actual-review-20261005.json'
actual = json.loads((old / 'run.json').read_text())['campaign']['result']
assert actual == json.loads(actual_file.read_text()) and actual['verdict'] == 'INCONCLUSIVE'
assert actual['kind'] == 'codex-report' and len(actual['premises']) == 11 and len(actual['passages']) == 25
for name, expected in [
    ('task.json','6386ca87975bb0cf426ecaa7c8e4a908aa482004135bac8075aa64dcac3ba083'),
    ('argument.md','0e1c85e69253114ed35deb2d5a67fe5e5f564a229077d1d9ba04cf4f9af1ed19'),
    ('settings.json','46ff76b55d2600cb2e535fa45442e860675b618b7132e2012ea2bb4b4e1553f4')
]:
    assert sha(old / name) == expected
    shutil.copyfile(old / name, V / name)
shutil.copyfile(actual_file, V / 'actual-review.json')
(V / 'report.txt').write_text(actual['report'])
write(V / 'premises.json', actual['premises'])
write(V / 'passages.json', actual['passages'])
assert sorted({p['premise'] for p in actual['passages']}) == list(range(11))
prov = json.loads((F / 'source-extracts/source-provenance.json').read_text())
texts = {s['public_source']:next(f['path'] for f in s['files'] if f['kind']=='literal_extract') for s in prov['sources']}
quote_checks = []
for p in actual['passages']:
    src = Path(texts[p['url']])
    quote_checks.append({'passage_id':p['id'],'premise_index':p['premise'],'url':p['url'],
        'local_literal_extract':str(src),'source_sha256':sha(src),
        'exact_quote_present_in_raw_extract':p['quote'] in src.read_bytes().decode(),
        'all_relevant_source_context_independently_root_read_this_round':False})
write(V / 'root-exact-binding-and-read-state-continuation75.json', {
    'recorded_utc':now,'actual_verdict':'INCONCLUSIVE','whole_actual_report_root_read':True,
    'all_11_exact_premises_and_all_25_retained_passages_root_read':True,
    'actual_review_sha256':sha(actual_file),'argument_sha256':sha(V/'argument.md'),
    'task_sha256':sha(V/'task.json'),'settings_sha256':sha(V/'settings.json'),
    'all_11_premise_indices_have_retained_evidence':True,
    'binding_implementation_file':'/workspace/xean/packages/core/src/solve/research.ts',
    'binding_implementation_sha256':sha('/workspace/xean/packages/core/src/solve/research.ts'),
    'binding_implementation_whole_root_read':True,
    'evidence_limit':'The filtered public result has evidence for every listed premise. The binding code additionally requires every submitted passage to survive. At least one submitted passage did not survive; its private raw content was not inspected. Preserve INCONCLUSIVE without override.',
    'raw_quote_checks':quote_checks,'accepted_scoped_paper':False,'original_P13_2_solved':False})
q = R / 'campaigns/round-63/P13.1-public-source-eleven-body-semigroup-and-uniform-differentiation-original-review'
f = json.loads((q/'freeze.json').read_text())
for key,name in [('argument_sha256','argument.md'),('task_sha256','task.json'),('settings_sha256','settings.json')]:
    assert sha(q/name)==f[key]
items = []
for atom,roundno,stem,role,db,session in [
    ('P13.1',63,q.name,'complete original correctness review','review.sqlite',58323),
    ('P16.1',68,'P16.1-public-source-BE-exact-PL-local-mass-and-unibranch-equation','author','campaign.sqlite',48580)
]:
    c=R/'campaigns'/('round-'+str(roundno))/stem
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    p=D/(atom+'-native-status.json');p.write_text(proc.stdout)
    items.append({'atom':atom,'round':roundno,'role':role,'directory':str(c),
        'tool_session_id':session,'observed_status':json.loads(proc.stdout)['status'],
        'status':str(p),'status_sha256':sha(p),'settings_sha256':sha(c/'settings.json'),'accepted':False})
assert len([i for i in items if i['observed_status']=='running'])<=2
write(D/'current-small-batch-observation.json',{'recorded_utc':now,'items':items,
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','hot_feedback_sent':False})
readstate=json.loads((F/'root-preservation-and-read-state-continuation75.json').read_text())
assert readstate['candidate'] and readstate['whole_argument_root_read'] and not readstate['original_problem_solved']
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
assert len(c['targets'])==42 and sum(len(t['reviewed_papers']) for t in c['targets'])==40
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==['P15.1','P15.2','P16.6']
a['updated_utc']=now;a['github_checkpoint']=receipt
a['github_pending_checkpoint']='Checkpoint75: exact round63 complete candidate reader, independent original review, and actual P13.2 v3 INCONCLUSIVE; no new accepted original.'
a['current_small_batch']['recorded_utc']=now
a['current_small_batch']['active_items']=[i for i in items if i['observed_status']=='running']
a['P13.1_round63_author_completion']={'candidate':True,'reader':str(F),'review_directory':str(q),
    'argument_sha256':sha(F/'P13.1-argument.md'),'actual_result_sha256':readstate['actual_result_sha256'],
    'original_problem_solved':False,'independent_original_review_observed_status':items[0]['observed_status']}
a['P13.2_round51_mathematical_v3_actual_review']={'verdict':'INCONCLUSIVE','reader':str(V),
    'actual_result_sha256':sha(actual_file),'whole_actual_result_root_read':True,'accepted':False,'original_solved':False}
a['prepared_P16.1_round68']['launched']=True
a['prepared_P16.1_round68']['native_session_id']=48580
c['updated_utc']=now;c['latest_verified_github_checkpoint']=receipt;c['current_small_batch']=a['current_small_batch']
for t in c['targets']:
    if t['id']=='P13.1':t['current_focus']='Round63 complete original candidate, whole argument and all actual notes root-read; independent exact original review running. Not accepted or closed.'
    if t['id']=='P13.2':t['current_focus']='Mathematical-only v3 partial audit actual INCONCLUSIVE after evidence binding; whole report/premises/passages root-read. Original image and existence characterization remains open.'
    if t['id']=='P16.1':t['current_focus']='Round68 author running on unchanged original: actual BE same-class PL descent, bounded local mass/comparison and singular unibranch equation. Earlier partials unreviewed; original open.'
write(R/'active-work.json',a);write(R/'checklist-current.json',c)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
    p=Path(path);assert p.is_file()
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation75/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,V,F]:
    for p in sorted(directory.rglob('*')):
        if p.is_file():add(p)
for name in ['task.json','argument.md','settings.json','freeze.json']:add(q/name)
for p in [R/'prepare_public_P13_1_round63_original_review_20261005.py',
    R/'root-checks/P13.1-round63-actual-result-20261005.json',actual_file,
    G/'record_verified_checkpoint74.py',G/'push-receipt-continuation74.json',G/'prepare_checkpoint_continuation75.py']:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
p=G/'upload-manifest-continuation75.json';assert not p.exists()
write(p,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':['P15.1','P15.2','P16.6'],'remaining_open_atoms':39,
    'historical_reviewed_scoped_papers':40,'current_native_batch':items,
    'commit_message':'Preserve complete P13.1 candidate and independent original review; continue two-item batch',
    'scope':'Exact unreviewed round63 author reader and paper, independent original review input, actual P13.2 v3 INCONCLUSIVE and current two-item batch. No new accepted original, private transcripts, SQL, credentials, Git databases or book-source edits.'})
print(json.dumps({'manifest':str(p),'sha256':sha(p),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items],'fully_solved_originals':3},indent=2))
