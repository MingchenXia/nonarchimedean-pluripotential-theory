from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat();previous=G/'push-receipt-continuation152.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='6b3084cdb1eb974e6b5f80271c2ce3a0551b2a84'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation152.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D53=R/'deliverables/scoped-P16.5-all-big-surfaces';b53=json.loads((D53/'publication-binding.json').read_text())
assert b53['pages']==42 and b53['review_verdict']=='PASS' and b53['accepted_paper_count']==53 and b53['actual_visual_pages']==[1,20,42]
assert b53['all_proof_body_bytes_unchanged_except_theorem_label'] and not b53['original_closed']
P191=K/'public-P16.5-continuation191-relative-floor-closure-reader';b191=json.loads((P191/'publication-binding.json').read_text())
assert b191['pages']==4 and b191['whole_final_tex_separately_root_read'] and b191['actual_visual_pages']==[1,3,4] and not b191['independent_review']
for b in [b53,b191]:
    assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256']
    assert b['overfull']==b['undefined']==b['warnings']==0
accept=K/'P16.5-round142-surface-acceptance-and-original-scope-record-20261006.json';a=json.loads(accept.read_text());assert a['accepted_papers_after']==53
partial=K/'P19.2-round140-completed-partial-scope-record-20261006.json';p140=json.loads(partial.read_text());assert not p140['candidate'] and p140['whole_four_canonical_notes_root_read']
S=K/'current-small-batch143145-20261006-continuation154';S.mkdir(exist_ok=False);items=[]
for n,label in [(143,'P16.5-entire-exceptional-big-equation-independent-review-retry1'),(145,'P16.5-original-big-class-relative-floor-closure-and-entire-equation-research-retry1')]:
    C=R/f'campaigns/round-{n}'/label;f=json.loads((C/'freeze.json').read_text());launch=json.loads((C/'launch-record.json').read_text())
    for name,key in [('task.json','task_sha256'),('settings.json','settings_sha256'),('argument.md','argument_sha256') if n==143 else ('input.json','input_sha256')]:assert sha(C/name)==f[key]
    status=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    ps=subprocess.run(['ps','-o','stat=,comm=','-p',str(launch['pid'])],capture_output=True,text=True).stdout.strip();alive=bool(ps) and not ps.startswith('Z')
    assert status['status'] in ['running','completed']
    if status['status']=='running':assert alive and status['calls']['admitted']==1
    p=S/f'round{n}-public-native-status.json';save(p,status)
    lp=C/'launch-public-native-status.json'
    if not lp.exists():save(lp,status)
    items.append({'round':n,'atom':'P16.5','directory':str(C),'database':'work.sqlite','observed_status':status['status'],'observed_utc':status['observedAt'],
       'native_controller_process_observed_alive':alive,'process_state':ps,'public_status':str(p),'public_status_sha256':sha(p),
       'launch_record':launch,'frozen_metadata':f,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'author_research_only':n==145,'scoped_review_only':n==143,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False})
for n in [140,142]:
    C=next((R/f'campaigns/round-{n}').iterdir());status=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert status['status']=='completed';save(S/f'round{n}-completed-public-native-status.json',status)
batch={'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],'maximum_concurrent_campaigns':2,
    'focus':'Entire exceptional big-family scoped retry143 and unchanged original full arbitrary-dimensional big-class equation author145 with unreviewed closure repair191.'}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==8 and d['remaining_open_original_atoms']==34 and d['historical_reviewed_scoped_papers']==53
    d.update({'updated_utc':now,'current_small_batch':batch,'github_pending_checkpoint':'continuation154 frozen',
        'P16_5_accepted_surface_final_paper142':b53,'P16_5_relative_floor_closure_candidate191':b191,
        'completed_approximation_research140':p140,'current_exceptional_equation_review143':items[0],
        'original_full_big_equation_research145':items[1],
        'next_native_launch_order':['Independent review if144 supplies a complete original theorem; otherwise repair its precise mathematical gaps.'],
        'next_work':'Reconstruct the new actual FS relative-floor closure and whole general-big equation in original author145; exceptional scoped retry143 continues. Preserve the full original P19.2 residual signature after completed partial140.',
        'original144_pre_model_configuration_failure':json.loads((K/'original144-pre-model-configuration-failure-public-20261006/failure-scope.json').read_text()),
        'goal_state':'8/42 originals solved;34 open;53 independently accepted papers. Continue small batches.'})
    old=d.get('current_surface_equation_review142',{});old.update({'observed_status':'completed','review_verdict':'PASS','acceptance_record':str(accept),'original_closed':False});d['current_surface_equation_review142']=old
    old=d.get('current_exceptional_equation_review137',{});old.update({'retry_deferred_until_slot_frees':False,'retried_as_round':143,'observed_status':'blocked'});d['current_exceptional_equation_review137']=old
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';out=[]
for line in tsv.read_text().splitlines():
    row=line.split('\t')
    if row[0]=='P16.5':row[2]='Whole all-big-rational SURFACE theorem PASS142, final42-page paper. Arbitrary-dimensional original author145 running with actual relative-floor closure repair191; exceptional scoped retry143 running. Original open.';row[3]='5'
    out.append('\t'.join(row))
tsv.write_text('\n'.join(out)+'\n')
D=G/'continuation154-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':53,
    'new_original_closure':None,'accepted_supporting_paper':'All actual big rational SURFACES, whole equation and rigid-zero extra range; review142 PASS,42-page final paper.',
    'unreviewed191':'4-page actual-FS relative-floor closure repair; original author145 reconstructs it and the entire arbitrary-dimensional equation.',
    'completed_original_author140':'PARTIAL; whole4 canonical notes read, native14-page artifact argument not yet wholly root-read.',
    'active_batch':[x['round'] for x in items if x['observed_status']=='running']})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink() and 'LOCALONLY' not in p.name
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent in [D53,P191]
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation154/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,S,K/'original144-pre-model-configuration-failure-public-20261006']:
    for p in sorted(directory.iterdir()):add(p)
for b,directory in [(b53,D53),(b191,P191)]:
    for p in [Path(b['tex']),Path(b['pdf']),directory/'publication-binding.json']:add(p)
for p in [accept,K/'P16.5-round142-actual-scoped-independent-review-20261006.json',
          K/'P19.2-round140-completed-author-result-PUBLIC-20261006.json',partial,P191/'source-application-ledger-PUBLIC.json',
          K/'prepared-checkpoint153-unuploaded-supersession-20261006.json',
          R/'prepare_original_big_research_retry145_after_config144_20261006.py',R/'launch_frozen_original_big_research_retry145_20261006.py',
          previous,R/'accept_surface142_and_prepare_exceptional_retry143_20261006.py',R/'launch_frozen_exceptional_review_retry143_20261006.py',
          R/'publish_accepted_surface142_final_paper_20261006.py',R/'prepare_original_big_closure_and_equation_research144_20261006.py',
          R/'launch_frozen_original_big_research144_20261006.py',Path(__file__)]:add(p)
for item in items:
    C=Path(item['directory'])
    for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation154.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
    'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],
    'remaining_open_atoms':34,'historical_reviewed_scoped_papers':53,
    'commit_message':'Publish accepted entire big-surface equation and recover original big-class author configuration',
    'scope':'Review142 PASS for all actual big rational surfaces,42-page final paper; accepted papers52 to53 with originals8/42 unchanged. Original author140 completed PARTIAL. Native144 failed before any provider call because the author-worker configuration was omitted;145 repeats identical math with the established successful author configuration. Prepared153 was never uploaded and is superseded. New4-page unreviewed relative-floor closure191, full arbitrary-dimensional original author145 and unchanged exceptional-family retry143 launched. No active private outputs or runtime/account changes.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'statuses':[{k:x[k] for k in ['round','observed_status','observed_utc']} for x in items]},indent=2))
