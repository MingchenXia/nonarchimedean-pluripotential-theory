from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
previous=G/'push-receipt-continuation149.json'; receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='f3a957fb293464aa8e05d72cf5fda2433f8323e2'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation149.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'public-P19.2-continuation187-singular-start-reader'; b=json.loads((P/'publication-binding.json').read_text())
assert b['pages']==4 and b['whole_final_tex_separately_root_read'] and b['actual_visual_pages']==[1,3,4]
assert b['overfull']==b['undefined']==b['warnings']==0 and not b['independent_review'] and not b['original_closed']
assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256']
Q=K/'public-P19.2-round136-partial-approximation-reader'; q=json.loads((Q/'publication-binding.json').read_text())
assert q['pages']==14 and q['whole_mathematical_argument_root_read'] and q['whole_canonical_ledger_root_read'] and q['actual_visual_pages']==[1,7,14]
for x in q['files']:assert sha(x['path'])==x['sha256']
C=R/'campaigns/round-139/P19.2-original-prescribed-endpoint-and-singular-start-approximation-research'
f=json.loads((C/'freeze.json').read_text())
for name,key in [('input.json','input_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
assert f['unchanged_original_task'] and f['prepared_only']
S=K/'current-small-batch137138-20261006-continuation150'; S.mkdir(exist_ok=False)
items=[]
for n in [137,138]:
    A=next((R/f'campaigns/round-{n}').iterdir()); freeze=json.loads((A/'freeze.json').read_text())
    for name,key in [('argument.md','argument_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(A/name)==freeze[key]
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(A/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(r.stdout);assert d['status'] in ['running','completed']
    p=S/f'round{n}-public-native-status.json';save(p,d)
    items.append({'round':n,'atom':'P16.5','directory':str(A),'database':'work.sqlite','tool_session_id':51940 if n==137 else 62856,
                  'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','author_research_only':False,'scoped_review_only':True,
                  'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,'freeze':freeze,
                  'observed_status':d['status'],'observed_utc':d['observedAt'],'public_status':str(p),'public_status_sha256':sha(p)})
batch={'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],
       'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Scoped equation reviews137/138; full original P19.2 endpoint and singular-start research139 prepared to launch only when a slot frees.'}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==8 and d['remaining_open_original_atoms']==34 and d['historical_reviewed_scoped_papers']==52
    d.update({'updated_utc':now,'current_small_batch':batch,'github_pending_checkpoint':'continuation150 frozen',
              'P19_2_singular_start_joint_entropy_candidate187':b,'completed_approximation_research136_reader':q,
              'prepared_original_approximation_research139':f,
              'current_exceptional_equation_review137':items[0],'current_surface_equation_review138':items[1]})
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
D=G/'continuation150-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':52,
                              'new_original_closure':None,'new_paper187':'Unreviewed partial singular finite-entropy start extension,4 pages',
                              'round136':'Completed PARTIAL,14 pages; whole mathematical paper and ledger read',
                              'round139':'Prepared original research; not launched',
                              'active_batch':[x['round'] for x in items if x['observed_status']=='running']})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink() and 'LOCALONLY' not in p.name
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent in [P,Q]
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation150/'+str(p.relative_to(R)),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(S.iterdir()):add(p)
for p in [Path(b['tex']),Path(b['pdf']),P/'publication-binding.json',previous,R/'record_verified149_20261006.py',
          R/'publish_completed_partial_approximation136_reader_20261006.py',
          R/'prepare_original_P19_2_endpoint_and_singular_start_research139_20261006.py',Path(__file__)]:add(p)
for x in q['files']:add(x['path'])
for name in ['publication-binding.json','source-application-ledger-PUBLIC.json']:add(Q/name)
for name in ['freeze.json','mathematical-data-bindings.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation150.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
        'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],
        'remaining_open_atoms':34,'historical_reviewed_scoped_papers':52,
        'commit_message':'Add singular-start joint entropy candidate and complete residual approximation reader',
        'scope':'Whole4-page unreviewed singular finite-entropy start candidate187 and whole14-page PARTIAL original research136 with full application ledger; unchanged original endpoint research139 prepared, not launched. Scoped equation reviews137/138 remain frozen. Counts8/42 solved,34 open,52 accepted papers; no new original closure.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'statuses':[{k:x[k] for k in ['round','observed_status','observed_utc']} for x in items]},indent=2))
