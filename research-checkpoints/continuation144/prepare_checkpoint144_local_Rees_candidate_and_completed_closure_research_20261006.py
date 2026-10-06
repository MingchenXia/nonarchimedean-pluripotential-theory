from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation143.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='3b5e173c0f701705727e20d4212147cb67269a68'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation143.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
P=K/'public-P19.1-continuation181-Rees-candidate-reader'
binding=json.loads((P/'publication-binding.json').read_text())
assert binding['whole_final_tex_root_read'] and binding['actual_visual_pages']==[1,2,3]
assert not binding['independent_review'] and not binding['original_closed']
assert sha(binding['tex'])==binding['tex_sha256'] and sha(binding['pdf'])==binding['pdf_sha256']
C=R/'campaigns/round-133/P19.1-analytic-local-Rees-discrepancy-independent-review'
freeze=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==freeze[key]
assert json.loads((C/'mathematical-data-bindings.json').read_text())['whole_assembled_front_and_argument_separately_root_read']
S=K/'current-small-batch131-133-20261006-continuation144';S.mkdir(exist_ok=False)
observed={}
labels={131:'P19.1-original-transcendental-entropy-recovery-and-ray-normalization-research',
        132:'P16.5-original-genuine-Fubini-Study-decreasing-closure-and-compactness-research',
        133:'P19.1-analytic-local-Rees-discrepancy-independent-review'}
for n,label in labels.items():
    campaign=R/f'campaigns/round-{n}'/label
    p=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(campaign/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(p.stdout);assert d['status'] in ['running','completed']
    dest=S/f'round{n}-public-native-status.json';save(dest,d)
    observed[n]={'observed_status':d['status'],'observed_utc':d['observedAt'],
                 'public_status':str(dest),'public_status_sha256':sha(dest)}
assert observed[132]['observed_status']=='completed'
assert sum(x['observed_status']=='running' for x in observed.values())<=2
launch={'launched_utc':now,'round':133,'tool_session_id':14899,'role':'review',
        'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
        'frozen_task_sha256':freeze['task_sha256'],'frozen_argument_sha256':freeze['argument_sha256'],
        'frozen_settings_sha256':freeze['settings_sha256'],'maximum_concurrent_campaigns':2,
        'slot_freed_by_completed_round':132,'no_hot_feedback_to131_or132':True}
save(C/'launch-record.json',launch);shutil.copyfile(S/'round133-public-native-status.json',C/'launch-public-native-status.json')
complete=json.loads((K/'P16.5-round132-completed-native-inspection-LOCALONLY.json').read_text())
result=complete['campaign']['result'];assert result['candidate'] is False
W=Path(result['workspace']);status=json.loads((W/'status.json').read_text());assert status['status']=='PARTIAL'
save(S/'round132-completed-public-summary.json',{
    'recorded_utc':now,'round':132,'native_result_kind':result['kind'],'candidate':False,
    'status':status,'notes':result['notes'],'whole_paper_root_read':False,
    'argument_sha256':sha(W/'P16.5-argument.md'),'tex_sha256':sha(W/'P16.5-paper.tex'),
    'independent_acceptance':False,'original_closed':False,'accepted_count_change':0,
    'source_ledger_whole_root_read':True})
audit={'recorded_utc':now,'unreviewed_candidate':True,'original_closed':False,
       'accepted_count_change':0,'own_paper':binding,'supporting_independent_review_round':133,
       'primary_sources':[{
           'url':'https://www.math.stonybrook.edu/~dror/paper-jump.pdf',
           'pdf_sha256':sha(R/'shared-sources/ELSV-jumping-coefficients-author-pdf-20261006-LOCALONLY.pdf'),
           'text_sha256':sha(R/'shared-sources/ELSV-jumping-coefficients-author-pdf-20261006-LOCALONLY.txt'),
           'complete_literal_units_root_read':[[1000,1155]],
           'exact_application':'Definition4.1, Theorem4.2(i) and complete Lemma4.3 proof; codimension>=2 retained for exponent-one Jacobian inclusion. Local proof is written in own paper.'},{
           'url':'https://arxiv.org/pdf/2605.30063v2',
           'pdf_sha256':sha(R/'shared-sources/Trusiani-2605.30063v2-20261006-LOCALONLY.pdf'),
           'text_sha256':sha(R/'shared-sources/Trusiani-2605.30063v2-20261006-LOCALONLY.txt'),
           'complete_literal_units_root_read':[[569,692],[961,1028]],
           'exact_application':'Analytic Proposition3.1 and separate algebraic AppendixA.1 distinguished. Own determinant proof replaces the normal-injectivity step without a global projective vanishing claim.'}],
       'whole_own_tex_root_read':True,'native131_132_inputs_modified_or_hot_feedback_sent':False}
A=K/'P19.1-analytic-local-Rees-source-application-ledger-20261006-continuation181.json';save(A,audit)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==7 and d['historical_reviewed_scoped_papers']==50
    old={i['round']:i for i in d['current_small_batch']['items']};assert 131 in old and 132 in old
    old[132].update(observed[132]);d['completed_native132_closure_research']={'public_summary':str(S/'round132-completed-public-summary.json'),'sha256':sha(S/'round132-completed-public-summary.json'),'status':'PARTIAL','original_closed':False}
    new={'round':133,'atom':'P19.1','directory':str(C),'database':'work.sqlite','tool_session_id':14899,
         'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','author_research_only':False,
         'scoped_supporting_review_only':True,'original_closed':False,'private_active_output_read':False,
         'hot_feedback_sent':False,'freeze':freeze,**observed[133]}
    old[131].update(observed[131]);items=[old[131],new]
    d['current_small_batch']={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Full originalP19.1 ray research131 and independent local analytic Rees discrepancy gate review133; completed132 remains partial.'}
    d['P19_1_local_Rees_candidate181']={'publication_binding':str(P/'publication-binding.json'),'source_application_ledger':str(A),'independently_reviewed':False,'original_closed':False}
    d['updated_utc']=now;d['github_pending_checkpoint']='continuation144 frozen'
    if name=='checklist-current.json':
        t=next(t for t in d['targets'] if t['id']=='P16.5');assert not t['fully_solved'];t['research_status']='original129_FAIL_research132_PARTIAL_nef_closure_only_full_nonnef_open';t['current_native_research']=old[132]
        t['current_remaining_gaps']=status['concrete_gaps']
        t=next(t for t in d['targets'] if t['id']=='P19.1');assert not t['fully_solved'];t['supporting_review133']=new
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';rows=tsv.read_text().splitlines()
for i,line in enumerate(rows):
    fields=line.split('\t')
    if fields[0]=='P16.5':fields[2]='Original129 FAIL foundational closure; native132 PARTIAL gives nef and fixed-gauge structural repair, full big nonnef closure and equation unresolved.125 official INCONCLUSIVE; earlier scoped128 PASS retained historically.'
    rows[i]='\t'.join(fields)
tsv.write_text('\n'.join(rows)+'\n')
D=G/'continuation144-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,'historical_reviewed_scoped_papers':50,
     'newly_accepted':False,'candidate181_independently_accepted':False,'research132_status':'PARTIAL',
     'active_batch':[131,133],'original_closed':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent==P
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation144/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(S.iterdir()):add(p)
for p in [Path(binding['tex']),Path(binding['pdf']),P/'publication-binding.json',A,previous,R/'record_verified143_20261006.py',
          R/'prepare_scoped_analytic_Rees_discrepancy_review133_20261006.py',Path(__file__)]:add(p)
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation144.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
    'files':files,'file_count':len(files),'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
    'historical_reviewed_scoped_papers':50,'commit_message':'Checkpoint local analytic Rees discrepancy candidate, independent review133, and partial closure research132',
    'scope':'No new original or scoped acceptance.181 is an unreviewed3-page local analytic proof candidate.132 completedPARTIAL: nef/fixed-gauge closure results only; full nonnef big gate remains open. At most two native campaigns active.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),'native_status':observed,'originals_solved':7,'accepted_scoped_papers':50},indent=2))
