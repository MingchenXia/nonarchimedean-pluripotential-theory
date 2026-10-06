from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
import fitz

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation137.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='4cecab1b7810fc8d3eb0d12e3e9a7b71c18786ed'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation137.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'public-P16.5-round128-final-reader'
review=json.loads((P/'independent-review-public-projection.json').read_text())
assert review['verdict']=='PASS' and review['operationId']=='5b9f3e61-d5c0-4963-8ca5-dbc93261bae9'
pub=json.loads((P/'publication-preparation.json').read_text())
assert pub['scoped_independent_verdict']=='PASS' and not pub['original_closed']
assert pub['overfull_diagnostics']==0 and pub['undefined_diagnostics']==0
assert len(fitz.open(P/'P16.5-paper.pdf'))==20
for n,key in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(P/n)==pub[key]
pub.update({'actual_visual_pages':[1,11,20],'native_compiler_request_cell':1959,'native_compiler_status':'PENDING'})
(P/'publication-preparation.json').write_text(json.dumps(pub,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
layout={**pub,'whole_actual_report_premises_and_all_passages_root_read':True,
        'whole_matching_complete_section_limit_primary_units_root_read':True,
        'matching_primary':'Lazarsfeld--Mustata, published ENS2009 author PDF, Section2.1 conditions and complete Proposition2.1 proof; Section2.2 complete Lemma2.2 and Theorem2.3 proof; browser labels717--842 read in full. Normal geometric background and Khovanskii semigroup input remain named foundations.',
        'primary_url':'https://www.math.stonybrook.edu/robert.lazarsfeld/Reprints/Laz.Mustata.CBALS.pdf',
        'extended_primary_transcripts_uploaded':False,'native_compiler_success_observed':False}
save(P/'root-reading-and-layout-binding-20261006.json',layout)
T=R/'deliverables/scoped-P16.5-round128';T.mkdir(exist_ok=False)
names=['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','independent-review-public-projection.json',
       'source-application-ledger.json','publication-preparation.json','root-reading-and-layout-binding-20261006.json']
for n in names:shutil.copyfile(P/n,T/n)
accepted={'recorded_utc':now,'atom':'P16.5','round':128,'verdict':'PASS','operation_id':review['operationId'],
          'reported_utc':review['reportedAt'],'canonical_raw_sha256':pub['canonical_raw_sha256'],
          'whole_actual_report_premises_and_all_passages_root_read':True,'external_premises_count':11,'passages_count':248,
          'scope':'All actual big rational classes on smooth integral projective original X, arbitrary positive dimension and algebraically closed trivially valued characteristic-zero k of arbitrary cardinality: entire genuine reference-relative energy, positive raw-volume-mass operator, both continuous-direction outer signs, model-majorant independence and arbitrary decreasing/weak-plus-energy continuity. No mixed, weighted, pole, comparison or inverse conclusions.',
          'paper_source':str(T/'P16.5-paper.tex'),'source_sha256':sha(T/'P16.5-paper.tex'),
          'paper_pdf':str(T/'P16.5-paper.pdf'),'pdf_sha256':sha(T/'P16.5-paper.pdf'),'pages':20,
          'original_closed':False,'sole_equation_grant_scope':'Exact actual AMPLE G0 only.',
          'local_export_compilation_verified':True,'native_compiler_success_observed':False}
notes=[]
for n in [173,174]:
    matches=list(K.glob(f'*continuation{n}.md'));assert len(matches)==1;notes.append(matches[0])
C=R/'campaigns/round-129/P16.5-original-entire-general-big-equation-independent-review'
freeze=json.loads((C/'freeze.json').read_text())
for n,key in [('argument.md','argument_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/n)==freeze[key]
S=K/'current-small-batch125-129-after-scoped128-20261006-continuation138';S.mkdir(exist_ok=False)
items=[]
for n,label,pty in [(125,'P16.5-entire-nef-big-variational-equation-independent-review',47713),
                     (129,'P16.5-original-entire-general-big-equation-independent-review',33727)]:
    c=R/f'campaigns/round-{n}'/label
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(r.stdout);assert status['status'] in ['running','completed']
    assert status['calls']['byModel'][0]['model']=='gpt-6.1-sol'
    p=S/f'P16.5-round{n}-public-native-status.json';save(p,status)
    items.append({'round':n,'atom':'P16.5','directory':str(c),'database':'review.sqlite','tool_session_id':pty,
                  'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','scoped_review_only':n==125,
                  'original_scope_review':n==129,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,
                  'observed_status':status['status'],'observed_utc':status['observedAt'],'public_status':str(p),'public_status_sha256':sha(p)})
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Independent125 entire nef-big equation and exact-original129 entire general-big equation; operator128 scoped PASS and20-page paper published.'}
launch={'recorded_utc':now,'round':129,'launched':True,'prepared_only':False,'tool_session_id':33727,
        'freeze':freeze,'first_public_observation':next(i for i in items if i['round']==129),
        'original_task_unchanged':True,'no_third_concurrent_campaign':True,'hot_feedback_sent':False,
        'own172_173_174_not_added_to_frozen_argument':True}
save(S/'round129-launch-and-input-binding.json',launch);save(S/'current-batch.json',batch)
binding={'recorded_utc':now,'new_proofs':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
         'scope':'Own173 proves joint convex strong continuity and uniform intrinsic output pairing convergence on energy sublevels. Own174 defines a finite intrinsic unit-cost target metric, proves solution-cost bounds, and derives equivalence of target-metric convergence with genuine strong solution convergence. Both conditional on the reconstructed general-big candidate chain.',
         'independently_accepted':False,'original_closed':False,'active_or_frozen_native_inputs_modified':False,
         'current_native_batch':[i['round'] for i in batch['active_items']],'existing_editor_unchanged':True}
B=K/'P16.5-root-continuation173-174-strong-stability-and-scoped128-publication-binding-20261006.json';save(B,binding)
for n in ['active-work.json','checklist-current.json']:
    p=R/n;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==48
    data.update({'updated_utc':now,'current_small_batch':batch,'historical_reviewed_scoped_papers':49,
                 'P16_5_actual_scoped128':accepted,'launched_original_general_big_equation_review129':launch,
                 'continuation173_174_strong_stability_candidate':binding,'next_native_launch_order':[],
                 'goal_state':'7/42 originals solved;35 open;49 independently accepted scoped papers. Continue small batches.',
                 'github_pending_checkpoint':'continuation138 frozen'})
    if n=='active-work.json':data['next_work']='Read completed125 and129 reports in full; complete exact original proof obligations. New general-big operator paper reviewed128 accepted; relative weighted and target stability supplements remain unreviewed. Push regular checkpoints.'
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        cols=line.split('\t');assert cols[1]=='open';cols[3]='4'
        cols[2]='Scoped128 PASS:20-page entire genuine general-big operator/energy/outer/continuity paper. Exact-original129 full equation and scoped125 nef-big equation active. Original126 PARTIAL narrower point-blowup paper. Own143--174 full general-big equation/comparison/weighted/strong-stability chain remains unreviewed beyond128 scope; original open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation138-publication-records';D.mkdir(exist_ok=False)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':35,'historical_reviewed_scoped_papers':49,'newly_accepted_scoped_review':128,
    'current_native_small_batch':[i['round'] for i in batch['active_items']],'original_closed':False,
    'extended_primary_transcripts_private_native_state_or_raw_source_quotes_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr'} and 'LOCALONLY' not in p.name
    if p.suffix=='.pdf':assert p==T/'P16.5-paper.pdf'
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation138/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(T.iterdir()):add(p)
for p in notes+[B,previous,R/'record_verified137_20261006.py',R/'prepare_entire_general_big_operator_scoped_reader128_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation138.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':49,
    'commit_message':'Publish independently reviewed entire big-class operator paper and candidate intrinsic target stability',
    'scope':accepted['scope']+' New stability supplements unreviewed; exact-original129 active. Seven originals solved,35open.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'originals_solved':7,'originals_open':35,
                  'reviewed_scoped_papers':49,'current_batch':[i['round'] for i in batch['active_items']]},indent=2))
