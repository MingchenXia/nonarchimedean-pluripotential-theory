from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
previous=G/'push-receipt-continuation150.json'; receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='04e03fec86a4ce620990544f47bcd91ed9ca34be'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation150.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'public-P19.2-continuation188-normalized-endpoint-reader'
b=json.loads((P/'publication-binding.json').read_text())
assert b['pages']==5 and b['whole_final_tex_separately_root_read'] and b['actual_visual_pages']==[1,3,5]
assert b['overfull']==b['undefined']==b['warnings']==0 and not b['independent_review'] and not b['original_closed']
assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256']
primary=K/'P19.2-continuation188-ampleness-primary-LOCALONLY.json'
relative=R/'campaigns/round-136/P19.2-original-energy-entropy-and-P-singularity-model-approximation-research/artifacts/codex-Hx0s4M/sources/relative-ampleness-proof.json'
ledger=P/'source-application-ledger-PUBLIC.json'
save(ledger,{'recorded_utc':now,'classification':'Root-authored quote-free application and read-scope record; mathematical proof remains an unreviewed candidate.',
    'candidate_tex_sha256':b['tex_sha256'],'original_closed':False,'independent_acceptance':False,
    'entries':[
        {'source':'Stacks Project, tag 0B5Y','url':'https://stacks.math.columbia.edu/tag/0B5Y',
         'complete_statement_and_proof_root_read':True,'local_primary_capture_sha256':sha(primary),
         'application':'On each proper central fibre of dimension one, positivity of the degree on every reduced irreducible component implies ampleness. Actual component multiplicities are retained when computing model Monge–Ampere mass.',
         'hypotheses_checked':'Proper Noetherian one-dimensional scheme over C; every irreducible component has strictly positive rational degree after a common integral multiple.'},
        {'source':'Stacks Project, tag 09MS','url':'https://stacks.math.columbia.edu/tag/09MS',
         'complete_statement_and_proof_root_read':True,'local_primary_capture_sha256':sha(primary),
         'application':'Ampleness is unchanged under the relevant nilpotent thickening. The nonreduced central fibre with multiplicity i on F_i is not replaced by a reduced fibre in mass computations.'},
        {'source':'Stacks Project, tag 0D2S','url':'https://stacks.math.columbia.edu/tag/0D2S',
         'complete_statement_and_proof_root_read':True,'local_primary_capture_sha256':sha(relative),
         'application':'Fibrewise ampleness for the proper finitely presented projective family yields relative ampleness locally on the base; all fibres are treated. Rational divisor denominators are first cleared.'},
        {'source':'Analytic Legendre/test-curve correspondence and model envelope facts used in candidate188',
         'new_complete_primary_proofs_root_read_in_this_candidate':False,
         'application':'The explicit bounded radial candidate and its P-maximal Legendre levels are computed in the paper; the invoked general correspondence must be freshly verified in author campaign140. No new primary-source theorem grant is asserted.'}
    ],'third_party_primary_text_uploaded':False,'exact_finite_arithmetic_record':str(K/'P19.2-continuation188-exact-model-intersection-calibration-20261006.json')})
recovery=K/'interrupted-native137138-public-recovery-20261006'
recovered=json.loads((recovery/'recovery-scope.json').read_text())
assert recovered['mathematical_verdicts'] is None and not recovered['partial_private_review_outputs_read']
S=K/'current-small-batch140142-20261006-continuation151'; S.mkdir(exist_ok=False)
items=[]
for n,dirname in [(140,'P19.2-original-endpoint-preserving-model-approximation-research'),(142,'P16.5-entire-big-surface-relative-equation-independent-review-retry1')]:
    C=R/f'campaigns/round-{n}'/dirname; f=json.loads((C/'freeze.json').read_text()); launch=json.loads((C/'launch-record.json').read_text())
    pairs=[('task.json','task_sha256'),('settings.json','settings_sha256'),('input.json','input_sha256')] if n==140 else [('task.json','task_sha256'),('settings.json','settings_sha256'),('argument.md','argument_sha256')]
    for name,key in pairs:assert sha(C/name)==f[key]
    pid=subprocess.run(['ps','-o','stat=,comm=','-p',str(launch['pid'])],capture_output=True,text=True,check=True).stdout.strip()
    alive=bool(pid) and not pid.startswith('Z')
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(r.stdout);assert d['status'] in ['running','completed']
    if d['status']=='running':assert alive and d['work']['active']==1
    p=S/f'round{n}-public-native-status.json';save(p,d)
    lp=C/'launch-public-native-status.json'
    if not lp.exists():save(lp,d)
    items.append({'round':n,'atom':'P19.2' if n==140 else 'P16.5','directory':str(C),'database':'work.sqlite',
        'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','author_research_only':n==140,'scoped_review_only':n==142,
        'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,'frozen_metadata':f,'launch_record':launch,
        'native_controller_process_observed_alive':alive,'process_state':pid,'observed_status':d['status'],'observed_utc':d['observedAt'],
        'public_status':str(p),'public_status_sha256':sha(p)})
old139=R/'campaigns/round-139/P19.2-original-prescribed-endpoint-and-singular-start-approximation-research'
superseded=K/'prepared139-superseded-by140-20261006.json'
save(superseded,{'recorded_utc':now,'prepared_round':139,'launched':False,'frozen_inputs_preserved':True,
    'freeze_sha256':sha(old139/'freeze.json'),'superseded_by':140,'reason':'Author140 includes the complete actual normalized endpoint model construction188; prepared139 is not an active campaign.'})
batch={'recorded_utc':now,'items':items,'active_items':[x for x in items if x['observed_status']=='running'],
       'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Original P19.2 full residual model-approximation author140 and unchanged whole-surface scoped equation independent retry142.'}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==8 and d['remaining_open_original_atoms']==34 and d['historical_reviewed_scoped_papers']==52
    d.update({'updated_utc':now,'current_small_batch':batch,'github_pending_checkpoint':'continuation151 frozen',
        'P19_2_normalized_actual_endpoint_candidate188':b,'original_approximation_research140':items[0],
        'current_surface_equation_review142':items[1],'interrupted_native137138_recovery':recovered,
        'prepared139_superseded_by140':json.loads(superseded.read_text()),
        'next_work':'Reconstruct the full P19.2 endpoint/zero-mass and residual log-discrepancy-model approximation problem in author140. Review142 covers all big surfaces only; arbitrary-dimensional P16.5 remains open. Retry exceptional review137 after an active slot frees.',
        'next_native_launch_order':['Fresh unchanged-input exceptional-family independent review retry of interrupted137 when a slot frees.'],
        'goal_state':'8/42 originals solved;34 open;52 independently accepted papers. Continue small batches.'})
    for key,n in [('current_exceptional_equation_review137',137),('current_surface_equation_review138',138)]:
        old=d.get(key,{})
        old.update({'observed_status':'blocked','native_controller_process_observed_alive':False,'mathematical_verdict':None,
                    'public_recovery':str(recovery/f'round{n}-public-native-status.json'),
                    'retry_deferred_until_slot_frees':n==137,'retried_as_round':142 if n==138 else None})
        d[key]=old
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv'; lines=tsv.read_text().splitlines();out=[]
for line in lines:
    row=line.split('\t')
    if row[0]=='P16.5':row[2]='Original open. All-big-surface scoped equation review142 retries interrupted138 with identical math; exceptional review137 interrupted without verdict, retry deferred. Arbitrary-dimensional closure unresolved.'
    if row[0]=='P19.2':row[2]='Original research140 running with whole136 PARTIAL, singular-start candidate187 and normalized actual endpoint diagnostic188. Endpoint example is not nonexistence. Full prescribed P/zero-mass and residual log-discrepancy-model approximation open.'
    out.append('\t'.join(row))
tsv.write_text('\n'.join(out)+'\n')
D=G/'continuation151-publication-records'; D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':52,
    'new_original_closure':None,'new_paper188':'Unreviewed 5-page actual normalized model endpoint diagnostic; no existence refutation.',
    'active_batch':[x['round'] for x in items if x['observed_status']=='running'],
    'interrupted_reviews137138':'Native recovery blocked at attempt limit; no mathematical verdict; inputs preserved.',
    'review142':'Fresh run with exact task and argument bytes from138; all big surfaces only.',
    'prepared139':'Never launched; superseded by140.'})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink() and 'LOCALONLY' not in p.name
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent==P
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation151/'+str(p.relative_to(R)),
                  'bytes':p.stat().st_size,'sha256':sha(p)})
for directory in [D,S,recovery]:
    for p in sorted(directory.iterdir()):add(p)
for p in [Path(b['tex']),Path(b['pdf']),P/'publication-binding.json',ledger,
          K/'P19.2-continuation188-exact-model-intersection-calibration-20261006.json',superseded,
          previous,R/'record_verified150_20261006.py',R/'prepare_original_endpoint_research140_and_surface_review_retry142_20261006.py',
          R/'launch_frozen_native_batch140142_20261006.py',K/'github-continuation150-transient-commit-auth-retry-20261006.json',Path(__file__)]:add(p)
for item in items:
    C=Path(item['directory'])
    for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']:add(C/name)
    if item['round']==142:add(C/'original-family-coverage.json')
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation151.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
    'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],
    'remaining_open_atoms':34,'historical_reviewed_scoped_papers':52,
    'commit_message':'Add actual normalized endpoint model diagnostic and recover interrupted native reviews',
    'scope':'Whole5-page unreviewed actual normalized endpoint diagnostic188, exact arithmetic and quote-free source application ledger. Native137/138 interruption recovered without verdict; original author140 and identical-math surface review retry142 launched. Prepared139 superseded. Counts8/42 solved,34 open,52 accepted papers; no new closure.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'statuses':[{k:x[k] for k in ['round','observed_status','observed_utc','native_controller_process_observed_alive']} for x in items]},indent=2))
