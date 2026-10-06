from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation140.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='a2470baf155c17d754b55974e6e799276c82eb41'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation140.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
note=K/'P19.1-general-exponential-floor-criterion-and-remaining-maximal-branch-20261006-continuation177.md'
C=R/'campaigns/round-130/P19.1-original-arbitrary-ray-entropy-counterexample-independent-review'
freeze=json.loads((C/'freeze.json').read_text())
assert freeze['prepared_only'] and freeze['original_scope_comparison_requested']
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==freeze[key]
S=K/'current-small-batch125-129-20261006-continuation141';S.mkdir(exist_ok=False)
observed={}
for n,label in [(125,'P16.5-entire-nef-big-variational-equation-independent-review'),
                (129,'P16.5-original-entire-general-big-equation-independent-review')]:
    c=R/f'campaigns/round-{n}'/label
    p=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(p.stdout);assert status['status'] in ['running','completed']
    dest=S/f'P16.5-round{n}-public-native-status.json';save(dest,status)
    observed[n]={'observed_status':status['status'],'observed_utc':status['observedAt'],'public_status':str(dest),'public_status_sha256':sha(dest)}
now=datetime.now(timezone.utc).isoformat()
binding={'recorded_utc':now,'proof':str(note),'proof_sha256':sha(note),'whole_final_supplement_root_read':True,
 'new_scope':'Any compact Kahler manifold: fixed all-exponent integrable singular floor plus a nonzero bounded negative weak ray forces trivial actual NA datum and infinite entropy slope. Separately records established nonmaximal-ray and infinite-NA-entropy branches and leaves transcendental maximal finite-entropy upper recovery open.',
 'independently_accepted':False,'original_closed':False,'prepared130':freeze,
 'prepared130_contains_new177':False,'active_native_batch_modified_or_feedback_sent':False,'existing_editor_unchanged':True}
B=K/'P19.1-continuation177-and-prepared130-root-binding-20261006.json';save(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==49
    data.update({'updated_utc':now,'P19_1_general_floor_criterion_continuation177':binding,
                 'github_pending_checkpoint':'continuation141 frozen'})
    for item in data['current_small_batch']['items']:item.update(observed[item['round']])
    data['current_small_batch']['active_items']=[i for i in data['current_small_batch']['items'] if i['observed_status']=='running']
    data['current_small_batch']['recorded_utc']=now
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
D=G/'continuation141-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,'historical_reviewed_scoped_papers':49,
 'prepared130_launched':False,'new177_reviewed':False,'original_closed':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.pdf','.stdout','.stderr','.out'}
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation141/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in [note,B,C/'freeze.json',C/'mathematical-data-bindings.json',previous,R/'record_verified140_20261006.py',
          R/'prepare_original_P19_1_polar_ray_review130_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation141.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
 'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':49,
 'commit_message':'Prove general exponential-floor entropy criterion and freeze original P19.1 review',
 'scope':binding['new_scope']+' New deductions unreviewed; original counts unchanged;130 not launched as two reviews remain active.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),'native_status':observed,'originals_solved':7,'accepted_scoped_papers':49},indent=2))
