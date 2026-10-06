from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation147.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='50e1703956ad10903d683b4531f0297b686b85d5'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation147.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
P=K/'public-P16.5-continuation185-exceptional-equation-reader'
b=json.loads((P/'publication-binding.json').read_text())
assert b['whole_final_tex_root_read'] and b['actual_visual_pages']==[1,5,9]
assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256']
assert b['pages']==9 and not b['independent_review'] and not b['original_closed']
assert b['accepted_count_change']==0 and all(p['whole_unit_root_read'] for p in b['proof_units'])
S=K/'current-small-batch136137-20261006-continuation148';S.mkdir(exist_ok=False)
labels={135:'P16.5-original-entire-big-cone-surface-and-filtered-ideal-research',
        136:'P19.2-original-energy-entropy-and-P-singularity-model-approximation-research',
        137:'P16.5-entire-exceptional-big-class-equation-independent-review'}
observed={};items=[]
for n,label in labels.items():
    C=R/f'campaigns/round-{n}'/label
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(r.stdout);assert d['status'] in ['running','completed']
    if n==135:assert d['status']=='completed'
    p=S/f'round{n}-public-native-status.json';save(p,d)
    observed[n]={'observed_status':d['status'],'observed_utc':d['observedAt'],'public_status':str(p),'public_status_sha256':sha(p)}
    if n==135:continue
    f=json.loads((C/'freeze.json').read_text())
    field='input' if n==136 else 'argument'
    for file,key in [(field+'.'+('json' if n==136 else 'md'),field+'_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/file)==f[key]
    items.append({'round':n,'atom':'P19.2' if n==136 else 'P16.5','directory':str(C),'database':'work.sqlite',
                  'tool_session_id':8407 if n==136 else 51940,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
                  'author_research_only':n==136,'scoped_review_only':n==137,'original_closed':False,
                  'private_active_output_read':False,'hot_feedback_sent':False,'freeze':f,**observed[n]})
assert sum(x['observed_status']=='running' for x in items)<=2
C=R/'campaigns/round-137'/labels[137];f=json.loads((C/'freeze.json').read_text())
save(C/'launch-record.json',{'recorded_utc':now,'round':137,'role':'independent-review','tool_session_id':51940,
                           'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','scoped_only':True,
                           'maximum_concurrent_campaigns':2,'frozen_task_sha256':f['task_sha256'],
                           'frozen_argument_sha256':f['argument_sha256'],'frozen_settings_sha256':f['settings_sha256']})
shutil.copyfile(S/'round137-public-native-status.json',C/'launch-public-native-status.json')
I=K/'P16.5-round135-completed-native-inspection-LOCALONLY.json'
native=json.loads(I.read_text());assert native['campaign']['status']=='completed'
result=native['campaign']['result'];assert result['kind']=='notes' and result['candidate'] is False and len(result['notes'])==4
N=K/'P16.5-round135-completed-author-result-PUBLIC-20261006.json';save(N,result)
summary={'recorded_utc':now,'round':135,'canonical_author_result':str(N),'canonical_author_result_sha256':sha(N),
         'completed_native_inspection_sha256':sha(I),'whole_all_four_canonical_notes_root_read':True,
         'standalone_argument_whole_root_read':False,'standalone_ledger_whole_root_read':False,
         'candidate':False,'status':'PARTIAL','original_closed':False,'accepted_count_change':0,
         'exact_result':'Entire genuine pseudoeffective rational surface cone, reference and volume; rigid zero-volume equations; fixed smooth-center ideal and linear weighted section gates.',
         'remaining_gap':'Arbitrary-dimensional big closure and entire positive-volume nonample finite-energy equation are not established.',**observed[135]}
save(K/'P16.5-round135-completed-partial-scope-record-20261006.json',summary)
batch={'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],
       'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Original P19.2 simultaneous energy/entropy/P-singularity approximation research136 and scoped entire exceptional nonnef big equation independent review137; original P16.5 remains open.'}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text())
    assert len(d['fully_solved_original_atoms'])==8 and d['remaining_open_original_atoms']==34 and d['historical_reviewed_scoped_papers']==52
    d.update({'current_small_batch':batch,'updated_utc':now,'github_pending_checkpoint':'continuation148 frozen',
              'completed_original_big_surface_research135':summary,'P16_5_entire_exceptional_equation_candidate185':b,
              'current_exceptional_equation_review137':next(x for x in items if x['round']==137)})
    if name=='checklist-current.json':
        t=next(x for x in d['targets'] if x['id']=='P16.5');assert not t['fully_solved'] and t['closure']=='open'
        t['research_status']='scoped_entire_exceptional_big_equation137_under_independent_review'
        t['completed_original_surface_research135']=summary
        t['current_scoped_review']=next(x for x in items if x['round']==137)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
D=G/'continuation148-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'historical_reviewed_scoped_papers':52,
                              'new_original_closure':None,'candidate185_independently_accepted':False,
                              'round135':'PARTIAL; complete surface cone result does not establish positive-volume equation',
                              'active_batch':[x['round'] for x in items if x['observed_status']=='running']})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent==P
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation148/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(S.iterdir()):add(p)
for p in [Path(b['tex']),Path(b['pdf']),P/'publication-binding.json',K/'P16.5-exceptional-relative-equation-proof-unit-20261006-continuation185.txt',
          N,K/'P16.5-round135-completed-partial-scope-record-20261006.json',previous,R/'record_verified147_20261006.py',
          R/'compose_exceptional_entire_equation_candidate185_20261006.py',
          R/'repair_exceptional_equation185_numbering_and_main_statement_20261006.py',
          R/'prepare_entire_exceptional_equation_review137_20261006.py',Path(__file__)]:add(p)
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation148.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
        'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
        'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],
        'remaining_open_atoms':34,'historical_reviewed_scoped_papers':52,
        'commit_message':'Submit entire exceptional big-class equation for review and preserve completed surface-cone research',
        'scope':'Unreviewed9-page whole exceptional nonnef big-family equation185; scoped native review137 and original P19.2 author136 active. Native135 completed PARTIAL with entire pseudoeffective surface cone and explicitly unproved positive-volume equation. No original closure or accepted-count change:8/42 solved,34 open,52 papers. Frozen active mathematical inputs unchanged; only public status inspected.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'native_status':observed},indent=2))
