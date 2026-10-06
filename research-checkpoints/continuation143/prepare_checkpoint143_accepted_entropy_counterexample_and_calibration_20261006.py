from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation142.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='5cd145d313fe2df073103151207e1e818578af6c'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation142.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
P=K/'public-P19.1-round130-final-reader'
binding=json.loads((P/'source-application-and-publication-binding.json').read_text())
assert binding['verdict']=='PASS' and binding['accepted_scoped_paper_number']==50 and not binding['original_closed']
assert binding['whole_final_mathematical_argument_root_read'] and binding['actual_visual_pages']==[1,5,9]
for name,key in [('P19.1-argument.md','argument_sha256'),('P19.1-paper.tex','tex_sha256'),('P19.1-paper.pdf','pdf_sha256')]:assert sha(P/name)==binding[key]
L=K/'public-P19.1-continuation179-calibration-reader'
calibration=json.loads((L/'publication-binding.json').read_text())
assert calibration['pages']==3 and len(calibration['local_builds'])==2 and all(x['returncode']==0 for x in calibration['local_builds'])
assert sha(calibration['tex'])==calibration['tex_sha256'] and sha(calibration['pdf'])==calibration['pdf_sha256']
calibration['actual_visual_pages']=[1,3]
(L/'publication-binding.json').write_text(json.dumps(calibration,ensure_ascii=False,indent=2)+'\n')
audit={'recorded_utc':now,'status':'Unreviewed root source-application diagnostic; no original or scoped acceptance',
    'primary_url':'https://arxiv.org/pdf/2605.30063v2',
    'primary_pdf_sha256':sha(R/'shared-sources/Trusiani-2605.30063v2-20261006-LOCALONLY.pdf'),
    'primary_text_sha256':sha(R/'shared-sources/Trusiani-2605.30063v2-20261006-LOCALONLY.txt'),
    'complete_literal_units_root_read':[[569,692],[961,1028]],
    'source_proof_under_check':'Analytic proof of Proposition3.1, specifically positivity in the normal direction at a generic Rees divisor; AppendixA.1 gives a separate algebraic proof.',
    'own_exact_counterexample_to_normal_injectivity':{
        'base':'The smooth affine surface with coordinates x,y; ideal a=(x^3,y^2).',
        'normalized_blowup_chart':'On the blowup chart r=x^3/y^2 with r invertible, the normalization has coordinates s,r, x=s^2 r, y=s^3 r.',
        'normalization_verification':'s=y/x is in the fraction field and satisfies s^2=x/r. The ring C[s,r,r^(-1)] is finite over the blowup chart ring, has the same fraction field and is normal.',
        'exceptional_divisor':'F={s=0}; ord_F(x)=2, ord_F(y)=3, ord_F(a)=6.',
        'differential':'dp=[[2sr,s^2],[3s^2r,s^3]], zero on F, including the normal direction.',
        'jacobian':'det(dp)=-s^4 r; the relative canonical coefficient is4.',
        'regularized_potential':'log(|x^3|^2+|y^2|^2) pulls back to6 log|s|^2+2 log|r|^2+log(1+|r|^2).',
        'residual_current':'For any smooth positive base form omega, eta=p*omega+ddc log(1+|r|^2) has a positive tangent restriction to F but zero normal coefficient on F.',
        'volume_orders':'For standard omega and r away from0, eta^2 has positive leading order |s|^2, whereas p*(omega^2) has order |s|^8. Their ratio has order |s|^6, not |s|^8 times a smooth positive unit.',
        'conclusion':'The asserted normal injectivity and the ensuing smooth volume-ratio step do not hold for this actual normalized blowup.'},
    'theorem_refuted':False,
    'remaining_repair':'Check a valid analytic-local replacement for the Rees discrepancy estimate, for example an exact relative Nadel argument. The independent algebraic AppendixA.1 is not silently promoted to every nonprojective analytic setting.',
    'new_Trusiani_Kahler_input':'arXiv:2609.31089v1 Proposition4.1 transfers the earlier analytic argument; its precise supporting chain remains under examination.',
    'native131_132_inputs_modified_or_hot_feedback_sent':False,'original_closed':False,'accepted_count_change':0}
A=K/'P19.1-special-Fujita-Rees-normal-direction-source-application-diagnostic-20261006-continuation180.json'
save(A,audit)
S=K/'current-small-batch131-132-20261006-continuation143';S.mkdir(exist_ok=False)
observed={}
for n,label in [(131,'P19.1-original-transcendental-entropy-recovery-and-ray-normalization-research'),
                (132,'P16.5-original-genuine-Fubini-Study-decreasing-closure-and-compactness-research')]:
    C=R/f'campaigns/round-{n}'/label
    p=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(p.stdout);assert status['status'] in ['running','completed']
    dest=S/f'round{n}-public-native-status.json';save(dest,status)
    observed[n]={'observed_status':status['status'],'observed_utc':status['observedAt'],
        'public_status':str(dest),'public_status_sha256':sha(dest)}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==50
    assert [i['round'] for i in data['current_small_batch']['items']]==[131,132]
    data.update({'updated_utc':now,'P19_1_actual_scoped_counterexample130':binding,
        'P19_1_actual_nonzero_entropy_model_calibration179':calibration,
        'P19_1_Rees_source_application_diagnostic180':{'path':str(A),'sha256':sha(A),
            'unreviewed':True,'theorem_refuted':False,'original_closed':False},
        'github_pending_checkpoint':'continuation143 frozen'})
    for item in data['current_small_batch']['items']:item.update(observed[item['round']])
    data['current_small_batch']['active_items']=[i for i in data['current_small_batch']['items'] if i['observed_status']=='running']
    data['current_small_batch']['recorded_utc']=now
    if name=='checklist-current.json':
        t=next(t for t in data['targets'] if t['id']=='P19.1')
        assert t['closure']=='open' and not t['fully_solved']
        t['research_status']='counterexample130_scoped_PASS_original_transcendental_maximal_ray_research131_running'
        t['reviewed_papers'].append({'round':130,'verdict':'PASS','scope':binding['scope'],
            'paper':str(P/'P19.1-paper.tex'),'PDF':str(P/'P19.1-paper.pdf'),'original_closed':False})
        t['current_native_research']=next(i for i in data['current_small_batch']['items'] if i['round']==131)
        t['current_remaining_gaps']=['Full transcendental maximal-ray entropy upper recovery and coherent slope conventions.',
            'Verify special Fujita approximation source dependencies in the actual compact-Kahler model setting.',
            'Compare the complete ray theorem and starting-point hypotheses with the unchanged original residual task.']
        t=next(t for t in data['targets'] if t['id']=='P16.5')
        assert t['closure']=='open' and not t['fully_solved']
        t['research_status']='original129_FAIL_foundational_genuine_closure_research132_running'
        t['current_native_research']=next(i for i in data['current_small_batch']['items'] if i['round']==132)
        t['current_remaining_gaps']=['Actual all-point genuine Fubini-Study decreasing-net closure and normalized-cone compactness without the false abstract lemma.',
            'Reconstruct dependent whole-big variational equation, comparison and intrinsic target claims after repairing this gate.',
            'Retain nonbig nonzero numerical scope and prohibit normalization of zero top mass.']
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';rows=tsv.read_text().splitlines()
for i,line in enumerate(rows):
    fields=line.split('\t')
    if fields[0]=='P19.1':
        fields[2]='Scoped130 PASS:9-page actual bounded polar-ray counterexample with zero usual NA datum and infinite entropy slope, including nonprojective products. Original maximal transcendental-ray question remains open; native131 researching entropy recovery and normalization.';fields[3]='1'
    if fields[0]=='P16.5':
        fields[2]='Original129 FAIL: imported abstract decreasing-closure lemma false; actual genuine nonample closure and compactness require repair. Native132 targets this gate.125 official INCONCLUSIVE despite raw model PASS due invalid evidence index. Earlier128 scoped PASS preserved historically; full original open.'
    rows[i]='\t'.join(fields)
tsv.write_text('\n'.join(rows)+'\n')
D=G/'continuation143-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,
    'historical_reviewed_scoped_papers':50,'new_accepted_scoped_paper':130,
    'calibration179_independently_reviewed':False,'source_diagnostic180_independently_reviewed':False,
    'active_batch':[131,132],'original_closed':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent in {P,L}
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation143/'+str(rel),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for name in ['P19.1-argument.md','P19.1-paper.tex','P19.1-paper.pdf','independent-review-public-projection.json',
             'source-application-and-publication-binding.json','README.md']:add(P/name)
for p in [Path(calibration['tex']),Path(calibration['pdf']),L/'publication-binding.json',A,
          previous,R/'record_verified142_20261006.py',R/'prepare_accepted_P19_1_counterexample_reader130_and_live_batch_20261006.py',
          R/'prepare_original_entropy131_and_genuine_closure132_research_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for item in json.loads((R/'active-work.json').read_text())['current_small_batch']['items']:
    C=Path(item['directory'])
    for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation143.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
    'historical_reviewed_scoped_papers':50,
    'commit_message':'Publish accepted9-page bounded-ray entropy counterexample, actual slope calibration, and131-132 research batch',
    'scope':'Originals remain7/42 solved.130 PASS accepts the precise analytic counterexample, not fullP19.1.179 is an unreviewed3-page model calibration;180 records an unreviewed source proof-step issue without refuting the discrepancy theorem. Two native original research campaigns131/132.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'native_status':observed,'originals_solved':7,'accepted_scoped_papers':50},indent=2))
