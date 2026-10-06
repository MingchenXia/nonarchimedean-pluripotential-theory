from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
previous=G/'push-receipt-continuation151.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='1d16e9b67dc3b913d97c79959c4e43e33f238be6'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation151.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'public-P19.2-continuation189-endpoint-preserving-toric-reader';b=json.loads((P/'publication-binding.json').read_text())
assert b['pages']==6 and b['whole_final_tex_separately_root_read'] and b['actual_visual_pages']==[1,3,6]
assert b['overfull']==b['undefined']==b['warnings']==0 and not b['independent_review'] and not b['original_closed']
assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256']
A=K/'P19.2-continuation189-exact-arbitrary-rational-fan-calibration-20261006.json';a=json.loads(A.read_text())
assert a['candidate_tex_sha256']==b['tex_sha256'] and len(a['rows'])==3
assert all(row['all_degrees_strictly_positive'] and row['actual_monomial_min_orders_verified'] and row['intersection_energy_equals_roof_area'] for row in a['rows'])
S=K/'current-small-batch140142-20261006-continuation152';S.mkdir(exist_ok=False);items=[]
for n,dirname in [(140,'P19.2-original-endpoint-preserving-model-approximation-research'),(142,'P16.5-entire-big-surface-relative-equation-independent-review-retry1')]:
    C=R/f'campaigns/round-{n}'/dirname;f=json.loads((C/'freeze.json').read_text());launch=json.loads((C/'launch-record.json').read_text())
    for name,key in [('task.json','task_sha256'),('settings.json','settings_sha256'),('input.json','input_sha256') if n==140 else ('argument.md','argument_sha256')]:assert sha(C/name)==f[key]
    d=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    pid=subprocess.run(['ps','-o','stat=,comm=','-p',str(launch['pid'])],capture_output=True,text=True).stdout.strip();alive=bool(pid) and not pid.startswith('Z')
    if d['status']=='running':assert alive
    p=S/f'round{n}-public-native-status.json';save(p,d)
    items.append({'round':n,'atom':'P19.2' if n==140 else 'P16.5','directory':str(C),'observed_status':d['status'],'observed_utc':d['observedAt'],
        'native_controller_process_observed_alive':alive,'process_state':pid,'launch_record':launch,'frozen_metadata':f,
        'public_status':str(p),'public_status_sha256':sha(p),'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
        'author_research_only':n==140,'scoped_review_only':n==142,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
batch={'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],'maximum_concurrent_campaigns':2,
       'focus':'Original approximation author140 and whole-surface scoped review retry142. New constructive paper189 is separate frozen mathematical work and has not been sent to either active worker.'}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==8 and d['remaining_open_original_atoms']==34 and d['historical_reviewed_scoped_papers']==52
    d.update({'updated_utc':now,'current_small_batch':batch,'github_pending_checkpoint':'continuation152 frozen',
              'P19_2_constructive_closed_toric_profile_candidate189':b,'original_approximation_research140':items[0],'current_surface_equation_review142':items[1]})
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
D=G/'continuation152-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':52,'new_original_closure':None,
    'new_paper189':'6-page unreviewed constructive model approximation with uniform closed P profile, including zero-mass endpoint; fixed one-branch toric P1 and zero start.',
    'arithmetic':'Three arbitrary rational regular fans, with 14,12,16 actual central components; finite checks, not a universal certificate.',
    'active_batch':[x['round'] for x in items if x['observed_status']=='running'],'new_math_sent_to_active_workers':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink() and 'LOCALONLY' not in p.name
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent==P
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation152/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,S]:
    for p in sorted(directory.iterdir()):add(p)
for p in [Path(b['tex']),Path(b['pdf']),P/'publication-binding.json',A,
          R/'check_candidate189_exact_regular_fans_20261006.py',previous,R/'record_verified151_20261006.py',
          K/'native-compiler-public-unavailability-observation-20261006-0704.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation152.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
    'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],
    'remaining_open_atoms':34,'historical_reviewed_scoped_papers':52,
    'commit_message':'Add constructive actual model approximation preserving the entire closed toric profile',
    'scope':'Whole6-page unreviewed constructive one-branch toric approximation candidate189 and exact arbitrary-rational fan checks. Closed P profile and zero-mass endpoint are controlled explicitly. Original author140 and scoped surface review142 remain frozen; no new feedback. Counts8/42 solved,34 open,52 accepted papers; no new original closure.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'statuses':[{k:x[k] for k in ['round','observed_status','observed_utc']} for x in items]},indent=2))
