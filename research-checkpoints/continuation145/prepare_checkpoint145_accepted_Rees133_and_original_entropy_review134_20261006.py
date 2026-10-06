from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 assert not p.exists(),str(p)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation144.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='88133a2226e0456a6d8ffa3b471128718cce5ba9'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation144.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
P=K/'public-P19.1-round133-final-reader';p=P/'publication-binding.json';binding=json.loads(p.read_text())
assert binding['verdict']=='PASS' and binding['accepted_scoped_paper_number']==51
assert binding['whole_final_tex_separately_root_read'] and binding['whole_review_report_and_all_evidence_root_read']
assert sha(binding['tex'])==binding['tex_sha256'] and sha(binding['pdf'])==binding['pdf_sha256']
binding['actual_visual_pages']=[1,2,3];p.write_text(json.dumps(binding,indent=2)+'\n')
L=K/'public-P19.1-continuation182-all-ray-candidate-reader';candidate=json.loads((L/'publication-binding.json').read_text())
assert candidate['whole_final_tex_root_read'] and candidate['actual_visual_pages']==[1,4,8,11]
assert sha(candidate['tex'])==candidate['tex_sha256'] and sha(candidate['pdf'])==candidate['pdf_sha256']
S=K/'current-small-batch134-20261006-continuation145';S.mkdir(exist_ok=False)
labels={131:'P19.1-original-transcendental-entropy-recovery-and-ray-normalization-research',
 132:'P16.5-original-genuine-Fubini-Study-decreasing-closure-and-compactness-research',
 133:'P19.1-analytic-local-Rees-discrepancy-independent-review',
 134:'P19.1-original-all-starting-points-calibrated-entropy-independent-review'}
observed={}
for n,label in labels.items():
 C=R/f'campaigns/round-{n}'/label
 r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
 d=json.loads(r.stdout);assert d['status'] in ['running','completed']
 dest=S/f'round{n}-public-native-status.json';save(dest,d)
 observed[n]={'observed_status':d['status'],'observed_utc':d['observedAt'],'public_status':str(dest),'public_status_sha256':sha(dest)}
assert all(observed[n]['observed_status']=='completed' for n in [131,132,133])
assert sum(x['observed_status']=='running' for x in observed.values())<=2
C=R/'campaigns/round-134'/labels[134];freeze=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==freeze[key]
assert json.loads((C/'mathematical-data-bindings.json').read_text())['whole_assembled_front_and_argument_separately_root_read']
launch={'recorded_utc':now,'round':134,'role':'review','tool_session_id':46101,'route':'Xean native Codex','model':'gpt-6.1-sol',
 'reasoning':'xhigh','unchanged_original_task':True,'maximum_concurrent_campaigns':2,'frozen_task_sha256':freeze['task_sha256'],
 'frozen_argument_sha256':freeze['argument_sha256'],'frozen_settings_sha256':freeze['settings_sha256']}
save(C/'launch-record.json',launch);shutil.copyfile(S/'round134-public-native-status.json',C/'launch-public-native-status.json')
native=json.loads((K/'P19.1-round131-completed-native-inspection-LOCALONLY.json').read_text());result=native['campaign']['result']
assert native['campaign']['status']=='completed' and result['candidate'] is False
W=Path(result['workspace']);status=json.loads((W/'status.json').read_text());assert status['status']=='PARTIAL'
save(S/'round131-completed-public-summary.json',{'recorded_utc':now,'round':131,'status':status,'notes':result['notes'],'candidate':False,
 'whole_paper_root_read':False,'argument_sha256':sha(W/'P19.1-argument.md'),'tex_sha256':sha(W/'P19.1-paper.tex'),
 'pdf_sha256':sha(W/'P19.1-paper.pdf'),'original_closed':False,'accepted_count_change':0})
item={'round':134,'atom':'P19.1','directory':str(C),'database':'work.sqlite','tool_session_id':46101,'route':'Xean native Codex',
 'model':'gpt-6.1-sol','reasoning':'xhigh','author_research_only':False,'whole_original_review':True,'original_closed':False,
 'private_active_output_read':False,'hot_feedback_sent':False,'freeze':freeze,**observed[134]}
for name in ['active-work.json','checklist-current.json']:
 p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==7 and d['historical_reviewed_scoped_papers']==51
 d['current_small_batch']={'recorded_utc':now,'items':[item],'active_items':[item] if item['observed_status']=='running' else [],
 'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'focus':'Whole originalP19.1 all-starting-points calibrated entropy independent review134; local Rees supporting theorem133 PASS; research131/132 completedPARTIAL.'}
 d['completed_native131_entropy_research']={'summary':str(S/'round131-completed-public-summary.json'),'sha256':sha(S/'round131-completed-public-summary.json'),'status':'PARTIAL','original_closed':False}
 d['P19_1_original_entropy_candidate182']=candidate;d['accepted_local_Rees_supporting_paper133']['publication_binding']=str(P/'publication-binding.json')
 d['accepted_local_Rees_supporting_paper133']['PDF']=binding['pdf'];d['updated_utc']=now;d['github_pending_checkpoint']='continuation145 frozen'
 if name=='checklist-current.json':
  t=next(t for t in d['targets'] if t['id']=='P19.1');assert not t['fully_solved'] and t['closure']=='open'
  t['research_status']='original_entropy_candidate182_whole_original_review134_running_local_Rees133_scoped_PASS'
  t['current_native_review']=item;t['current_remaining_gaps']=['Independent whole-original review of calibrated model/mixed slopes, special Fujita application and entropy recovery.',
   'Verify complete arbitrary-initial-point datum/maximalization, difference-integrability, slice classification and original scope.']
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';rows=tsv.read_text().splitlines()
for i,line in enumerate(rows):
 fields=line.split('\t')
 if fields[0]=='P19.1':fields[2]='Scoped130 bounded-ray counterexample PASS and scoped133 analytic Rees supporting theorem PASS. Whole original remains open;11-page all-starting-points calibrated entropy candidate182 under independent original review134.131 completedPARTIAL.';fields[3]='2'
 rows[i]='\t'.join(fields)
tsv.write_text('\n'.join(rows)+'\n')
D=G/'continuation145-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,'historical_reviewed_scoped_papers':51,
 'new_accepted_scoped_paper':133,'candidate182_original_independently_accepted':False,'research131_132':'PARTIAL','active_batch':[134]})
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
 if p.suffix=='.pdf':assert p.parent in {P,L}
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation145/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(S.iterdir()):add(p)
for p in [Path(binding['tex']),Path(binding['pdf']),P/'publication-binding.json',P/'independent-review-public-projection.json',
 Path(candidate['tex']),Path(candidate['pdf']),L/'publication-binding.json',previous,R/'record_verified144_20261006.py',
 R/'accept_scoped_Rees133_and_prepare_original_entropy_review134_20261006.py',Path(__file__)]:add(p)
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation145.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
 'files':files,'file_count':len(files),'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
 'historical_reviewed_scoped_papers':51,'commit_message':'Publish accepted analytic Rees discrepancy paper and complete calibrated entropy candidate under original review134',
 'scope':'Originals remain7/42 solved.133 scopedPASS accepts the local analytic discrepancy bound only, paper51.182 is an independently unaccepted11-page all-starting-points entropy candidate.131/132 completedPARTIAL. Whole original review134 uses unchanged original task.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),'native_status':observed,'originals_solved':7,'accepted_scoped_papers':51},indent=2))
