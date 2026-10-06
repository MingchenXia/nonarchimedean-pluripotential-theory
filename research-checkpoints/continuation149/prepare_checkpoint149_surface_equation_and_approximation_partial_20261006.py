from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
previous=G/'push-receipt-continuation148.json'; receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='b842b5c822534ba689804316589e5197d669e253'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation148.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
S=K/'current-small-batch137138-20261006-continuation149'; S.mkdir(exist_ok=False)
labels={136:'P19.2-original-energy-entropy-and-P-singularity-model-approximation-research',
        137:'P16.5-entire-exceptional-big-class-equation-independent-review',
        138:'P16.5-entire-big-surface-relative-equation-independent-review'}
observed={}; items=[]
for n,label in labels.items():
    C=R/f'campaigns/round-{n}'/label
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(r.stdout); assert d['status'] in ['running','completed']
    if n==136: assert d['status']=='completed'
    p=S/f'round{n}-public-native-status.json'; save(p,d)
    observed[n]={'observed_status':d['status'],'observed_utc':d['observedAt'],'public_status':str(p),'public_status_sha256':sha(p)}
    if n==136: continue
    f=json.loads((C/'freeze.json').read_text())
    for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==f[key]
    items.append({'round':n,'atom':'P16.5','directory':str(C),'database':'work.sqlite',
                  'tool_session_id':51940 if n==137 else 62856,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
                  'author_research_only':False,'scoped_review_only':True,'original_closed':False,
                  'private_active_output_read':False,'hot_feedback_sent':False,'freeze':f,**observed[n]})
assert sum(x['observed_status']=='running' for x in items)<=2
C=R/'campaigns/round-138'/labels[138]; f=json.loads((C/'freeze.json').read_text())
save(C/'launch-record.json',{'recorded_utc':now,'round':138,'role':'independent-review','tool_session_id':62856,
                           'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','scoped_only':True,
                           'maximum_concurrent_campaigns':2,'frozen_task_sha256':f['task_sha256'],
                           'frozen_argument_sha256':f['argument_sha256'],'frozen_settings_sha256':f['settings_sha256'],
                           'launch_after136_completed':True})
shutil.copyfile(S/'round138-public-native-status.json',C/'launch-public-native-status.json')
I=K/'P19.2-round136-completed-native-inspection-LOCALONLY.json'; native=json.loads(I.read_text())
assert native['campaign']['status']=='completed'
result=native['campaign']['result']; assert result['kind']=='notes' and result['candidate'] is False and len(result['notes'])==3
N=K/'P19.2-round136-completed-author-result-PUBLIC-20261006.json'; save(N,result)
summary={'recorded_utc':now,'round':136,'canonical_author_result':str(N),'canonical_author_result_sha256':sha(N),
         'completed_native_inspection_sha256':sha(I),'whole_all_three_canonical_notes_root_read':True,
         'standalone_argument_whole_root_read':False,'standalone_ledger_whole_root_read':False,
         'candidate':False,'status':'PARTIAL','original_closed':False,'accepted_count_change':0,
         'exact_result':'Simultaneous usual-datum energy/entropy recovery with interior Legendre P-level mass and singularity-metric control; calibrated P1 endpoint-loss example and nonmaximal energy-defect obstruction.',
         'remaining_gap':'Full residual prescribed P endpoints, zero-mass levels, singular-start entropy and log-discrepancy-model approximation are not established. Failure of a chosen approximating sequence does not refute existence.',**observed[136]}
save(K/'P19.2-round136-completed-partial-scope-record-20261006.json',summary)
P=K/'public-P16.5-continuation186-entire-surface-equation-reader'; b=json.loads((P/'publication-binding.json').read_text())
assert b['pages']==42 and b['actual_visual_pages']==[1,4,20,42]
for name in ['markdown','tex','pdf']: assert sha(b[name])==b[name+'_sha256']
assert b['whole_new_relative_proof_root_read'] and not b['independent_review'] and not b['original_closed']
assert b['accepted_count_change']==0 and b['overfull']==b['undefined']==b['warnings']==0
Q=K/'public-P16.5-round135-partial-surface-research-reader'; q=json.loads((Q/'publication-binding.json').read_text())
assert q['whole_mathematical_argument_root_read'] and q['pages']==14 and q['actual_visual_pages']==[1,7,14]
for x in q['files']: assert sha(x['path'])==x['sha256']
batch={'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],
       'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Scoped entire exceptional big-family equation137 and entire big-surface equation138 independent reviews. P19.2 research136 completed PARTIAL; original nonample and residual hybrid problems remain open.'}
for name in ['active-work.json','checklist-current.json']:
    p=R/name; d=json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms'])==8 and d['remaining_open_original_atoms']==34 and d['historical_reviewed_scoped_papers']==52
    d.update({'current_small_batch':batch,'updated_utc':now,'github_pending_checkpoint':'continuation149 frozen',
              'goal_state':'8/42 originals solved;34 open;52 independently accepted papers. Continue small batches.',
              'next_work':'Read complete P19.2 partial136 and investigate genuine prescribed P endpoints and log-discrepancy-model approximation. Review137/138 do not close arbitrary-dimensional P16.5.',
              'completed_original_approximation_research136':summary,'P16_5_entire_surface_equation_candidate186':b,
              'completed_surface_research135_reader':q,
              'current_exceptional_equation_review137':next(x for x in items if x['round']==137),
              'current_surface_equation_review138':next(x for x in items if x['round']==138)})
    if name=='checklist-current.json':
        for atom in ['P16.5','P19.2']:
            t=next(x for x in d['targets'] if x['id']==atom); assert not t['fully_solved'] and t['closure']=='open'
            t['research_status']='entire_surface_and_exceptional_big_equations_under_scoped_reviews137138' if atom=='P16.5' else 'original136_PARTIAL_interior_P_levels_entropy_and_endpoint_defects'
            if atom=='P19.2': t['completed_original_research136']=summary
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
t=R/'checklist-current.tsv'; lines=t.read_text().splitlines()
for i,line in enumerate(lines):
    cols=line.split('\t')
    if cols[0]=='P16.5': cols[2]='Original open. Entire exceptional big-family equation137 and entire big-surface equation138 under independent review;42-page surface candidate186. Surface research135 PARTIAL; arbitrary-dimensional closure unresolved.'
    if cols[0]=='P19.2': cols[2]='Original136 completed PARTIAL: joint energy/entropy recovery and interior P levels; endpoint-loss example is not a nonexistence proof. Prescribed endpoints, singular starts and residual log-discrepancy-model signature unresolved.'
    lines[i]='\t'.join(cols)
t.write_text('\n'.join(lines)+'\n')
D=G/'continuation149-publication-records'; D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'historical_reviewed_scoped_papers':52,
                              'new_original_closure':None,'candidate186_independently_accepted':False,'round136':'PARTIAL',
                              'active_batch':[x['round'] for x in items if x['observed_status']=='running']})
files=[]
def add(p,remote=None):
    p=Path(p); assert p.is_file() and not p.is_symlink()
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf': assert p.parent in [P,Q]
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation149/'+str(p.relative_to(R)),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()): add(p)
for p in sorted(S.iterdir()): add(p)
for p in [Path(b['markdown']),Path(b['tex']),Path(b['pdf']),P/'publication-binding.json',
          K/'P16.5-entire-big-surface-relative-equation-proof-unit-20261006-continuation186.md',
          N,K/'P19.2-round136-completed-partial-scope-record-20261006.json',previous,R/'record_verified148_20261006.py',
          R/'compose_entire_big_surface_equation_candidate186_20261006.py',
          R/'repair_big_surface186_unicode_and_long_bindings_20261006.py',
          R/'prepare_entire_big_surface_equation_review138_20261006.py',
          R/'publish_completed_partial_surface135_reader_20261006.py',Path(__file__)]: add(p)
for x in q['files']: add(x['path'])
for name in ['publication-binding.json','source-application-ledger-PUBLIC.json']: add(Q/name)
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']: add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation149.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
        'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
        'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],
        'remaining_open_atoms':34,'historical_reviewed_scoped_papers':52,
        'commit_message':'Preserve complete big-surface equation candidate and residual approximation results',
        'scope':'Unreviewed42-page entire big-surface equation186 with all proof appendices; scoped reviews137/138 active. Complete14-page135 partial reader and canonical136 approximation results. No original closure or accepted-count change:8/42 solved,34 open,52 papers. All active frozen mathematical inputs unchanged; only public status inspected.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'native_status':observed},indent=2))
