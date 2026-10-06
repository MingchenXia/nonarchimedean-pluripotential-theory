from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 assert not p.exists(),str(p)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation146.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='188b4e05af21282bd151433e76d7f6d913f46b21'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation146.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
P=R/'deliverables/original-P19.1';binding=json.loads((P/'publication-binding.json').read_text())
assert binding['fully_solved_original_atom'] and binding['accepted_paper_number']==52
assert binding['whole_final_tex_separately_root_read'] and binding['whole_review_report_and_all_evidence_root_read']
assert binding['actual_visual_pages']==[1,4,8,11] and sha(binding['tex'])==binding['tex_sha256'] and sha(binding['pdf'])==binding['pdf_sha256']
projection=json.loads((P/'P19.1-original-scope-review-PUBLIC.json').read_text())
assert projection['verdict']=='PASS' and projection['whole_original_P19_1_scope_independently_accepted']
assert len(projection['premises'])==24 and len(projection['passages'])==33
assert {x['premise'] for x in projection['passages']}==set(range(24))
L=K/'public-P16.5-continuation184-entire-exceptional-reader';candidate=json.loads((L/'publication-binding.json').read_text())
assert candidate['whole_final_tex_root_read'] and candidate['actual_visual_pages']==[1,3,5]
assert sha(candidate['tex'])==candidate['tex_sha256'] and sha(candidate['pdf'])==candidate['pdf_sha256']
S=K/'current-small-batch135136-20261006-continuation147';S.mkdir(exist_ok=False)
labels={134:'P19.1-original-all-starting-points-calibrated-entropy-independent-review',
 135:'P16.5-original-entire-big-cone-surface-and-filtered-ideal-research',
 136:'P19.2-original-energy-entropy-and-P-singularity-model-approximation-research'}
items=[];observed={}
for n,label in labels.items():
 C=R/f'campaigns/round-{n}'/label
 r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 d=json.loads(r.stdout);assert d['status'] in ['running','completed']
 if n==134:assert d['status']=='completed'
 p=S/f'round{n}-public-native-status.json';save(p,d)
 observed[n]={'observed_status':d['status'],'observed_utc':d['observedAt'],'public_status':str(p),'public_status_sha256':sha(p)}
 if n==134:continue
 freeze=json.loads((C/'freeze.json').read_text())
 for f,key in [('input.json','input_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/f)==freeze[key]
 items.append({'round':n,'atom':'P16.5' if n==135 else 'P19.2','directory':str(C),'database':'work.sqlite',
   'tool_session_id':72521 if n==135 else 8407,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
   'author_research_only':True,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,
   'freeze':freeze,**observed[n]})
assert sum(x['observed_status']=='running' for x in items)<=2
C=R/'campaigns/round-136'/labels[136];freeze=json.loads((C/'freeze.json').read_text())
save(C/'launch-record.json',{'recorded_utc':now,'round':136,'role':'codex','tool_session_id':8407,
 'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','unchanged_original_task':True,'maximum_concurrent_campaigns':2,
 'frozen_input_sha256':freeze['input_sha256'],'frozen_task_sha256':freeze['task_sha256'],'frozen_settings_sha256':freeze['settings_sha256']})
shutil.copyfile(S/'round136-public-native-status.json',C/'launch-public-native-status.json')
batch={'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],
 'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'focus':'P16.5 original actual-cone closure research135 and P19.2 simultaneous energy/entropy/P-singularity approximation research136; whole original P19.1 independently solved134.'}
for name in ['active-work.json','checklist-current.json']:
 p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==8 and d['historical_reviewed_scoped_papers']==52 and d['remaining_open_original_atoms']==34
 d['current_small_batch']=batch;d['updated_utc']=now;d['github_pending_checkpoint']='continuation147 frozen'
 d['P16_5_entire_big_exceptional_candidate184']=candidate
 d['completed_original_entropy_review134']={'verdict':'PASS','operation_id':projection['operationId'],'reported_utc':projection['reportedAt'],
  'original_closed':True,'publication_binding':str(P/'publication-binding.json'),'publication_binding_sha256':sha(P/'publication-binding.json'),**observed[134]}
 if name=='checklist-current.json':
  t=next(t for t in d['targets'] if t['id']=='P19.2');assert t['closure']=='open' and not t['fully_solved']
  t['research_status']='original_energy_entropy_P_singularity_approximation136_running'
  t['current_native_research']=next(x for x in items if x['round']==136)
  t['current_remaining_gaps']=['Construct admissible residual model approximations preserving the prescribed finer P-envelope data together with energy and entropy.',
   'Determine and prove the exact required singularity and hybrid approximation signature beyond ordinary NA strong recovery, without confusing P-maximal test curves with NA-maximal rays.']
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';rows=tsv.read_text().splitlines()
for i,line in enumerate(rows):
 f=line.split('\t')
 if f[0]=='P19.2':f[2]='Original residual model approximation136 running: jointly energy,entropy and finer P singularity data; older smooth entropy diagnostics remain PARTIAL. Uses complete accepted originalP19.1 proof134 in exact scope.'
 rows[i]='\t'.join(f)
tsv.write_text('\n'.join(rows)+'\n')
D=G/'continuation147-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'historical_reviewed_scoped_papers':52,
 'new_original_closure':'P19.1','whole_original_review':'PASS','premises':24,'passages':33,
 'candidate184_independently_accepted':False,'other_P19_atoms_closed':False,'active_batch':[x['round'] for x in items if x['observed_status']=='running']})
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
 if p.suffix=='.pdf':assert p.parent in {P,L}
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation147/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(S.iterdir()):add(p)
for p in [Path(binding['tex']),Path(binding['pdf']),P/'publication-binding.json',P/'P19.1-original-scope-review-PUBLIC.json',
 K/'P19.1-round134-original-closure-and-publication-record-20261006.json',Path(candidate['tex']),Path(candidate['pdf']),L/'publication-binding.json',
 previous,R/'record_verified146_20261006.py',R/'prepare_original_entropy134_accepted_publication_20261006.py',
 R/'accept_original_entropy134_and_prepare_singularity_approximation136_20261006.py',
 R/'finish_prepared_approximation136_after_review_settings_key_20261006.py',Path(__file__)]:add(p)
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json','prelaunch-preparation-repair.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
for name in ['P19.1-paper.tex','P19.1-paper.pdf','publication-binding.json','P19.1-original-scope-review-PUBLIC.json']:add(P/name,'manuscript/editorial/xean_research_20261003/original-P19.1/'+name)
manifest=G/'upload-manifest-continuation147.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
 'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],
 'remaining_open_atoms':34,'historical_reviewed_scoped_papers':52,
 'commit_message':'Solve original arbitrary-ray entropy classification P19.1 and continue model approximation and big-cone closure research',
 'scope':'P19.1 whole-original review134 PASS:24 exact premises,33 valid evidence bindings,all E1 starts and arbitrary compact Kahler weak rays. Formal11-page accepted paper includes the harmless wording fixes and explicit strong-openness citation requested by the review. Originals now8/42,34 open,52 accepted papers. Candidate184 is an unreviewed5-page entire exceptional-big-cone structural theorem only. Two active native author campaigns135/136 use unchanged original tasks.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),'native_status':observed,'originals_solved':8,'accepted_papers':52},indent=2))
