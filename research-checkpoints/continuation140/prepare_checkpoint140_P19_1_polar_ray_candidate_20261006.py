from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation139.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='552bfc9e1eaed5bed7b85b332684dd9263783bef'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation139.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
M=K/'P19.1-arbitrary-bounded-rays-trivial-NA-infinite-entropy-counterexample-candidate-20261006-continuation176.md'
D=K/'public-P19.1-continuation176-candidate-reader'
binding=json.loads((D/'source-application-and-publication-binding.json').read_text())
assert sha(M)==sha(D/'P19.1-argument.md')==binding['argument_sha256']
assert sha(D/'P19.1-paper.tex')==binding['tex_sha256']
assert sha(D/'P19.1-paper.pdf')==binding['pdf_sha256']
assert binding['actual_visual_pages']==[1,5,9] and binding['PDF_pages']==9
assert not binding['independently_accepted'] and not binding['original_closed']
S=K/'current-small-batch125-129-20261006-continuation140';S.mkdir(exist_ok=False)
observed={}
for n,label in [(125,'P16.5-entire-nef-big-variational-equation-independent-review'),
                (129,'P16.5-original-entire-general-big-equation-independent-review')]:
    c=R/f'campaigns/round-{n}'/label
    p=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(p.stdout);assert status['status'] in ['running','completed']
    dest=S/f'P16.5-round{n}-public-native-status.json';save(dest,status)
    observed[n]={'observed_status':status['status'],'observed_utc':status['observedAt'],'public_status':str(dest),'public_status_sha256':sha(dest)}
now=datetime.now(timezone.utc).isoformat()
candidate={'recorded_utc':now,'proof':str(M),'proof_sha256':sha(M),'reader':str(D),
           'scope':binding['scope'],'whole_final_mathematical_argument_root_read':True,
           'independently_accepted':False,'original_closed':False,'root_source_ledger':str(D/'source-application-and-publication-binding.json'),
           'native_small_batch_modified_or_feedback_sent':False,'native_compiler_pending_cell_id':'1997'}
for n in ['active-work.json','checklist-current.json']:
    p=R/n;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==49
    data.update({'updated_utc':now,'P19_1_polar_ray_candidate_continuation176':candidate,
                 'github_pending_checkpoint':'continuation140 frozen'})
    for item in data['current_small_batch']['items']:item.update(observed[item['round']])
    data['current_small_batch']['active_items']=[i for i in data['current_small_batch']['items'] if i['observed_status']=='running']
    data['current_small_batch']['recorded_utc']=now
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
P=G/'continuation140-publication-records';P.mkdir(exist_ok=False)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,P/n)
save(P/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,'historical_reviewed_scoped_papers':49,
 'new_P19_1_candidate_reviewed':False,'original_closed':False,'existing_P16_4_editor_unchanged':True})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p==D/'P19.1-paper.pdf'
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation140/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(P.iterdir()):add(p)
for p in [M,previous,R/'record_verified139_20261006.py',R/'prepare_P19_1_polar_ray_candidate_reader176_20261006.py',Path(__file__)]:add(p)
for name in ['P19.1-argument.md','P19.1-paper.tex','P19.1-paper.pdf','source-application-and-publication-binding.json','README.md']:add(D/name)
for p in sorted(S.iterdir()):add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(P/n,'manuscript/editorial/xean_research_20261003/'+n)
manifest=G/'upload-manifest-continuation140.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
 'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':49,
 'commit_message':'Write explicit polar weak-ray entropy counterexample in arbitrary Kahler products',
 'scope':binding['scope']+' Nine-page candidate unreviewed; all original closure counts unchanged; active reviews125129 remain independent.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),'native_status':observed,'originals_solved':7,'accepted_scoped_papers':49},indent=2))
