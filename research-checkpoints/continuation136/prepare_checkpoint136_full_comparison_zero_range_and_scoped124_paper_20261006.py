from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
import fitz

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation135.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='9a91bd4e888bb1280f127f34866cf0f2de8a61c8'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation135.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'public-P16.5-round124-final-reader';review=json.loads((P/'canonical-independent-review.json').read_text())
assert review['verdict']=='PASS' and review['operationId']=='17bacb62-99e4-4d2d-ae29-f4aaec3874d7'
assert sha(P/'P16.5-paper.tex')=='22a7a84c7d66aef720c13986b5025459bde2388c56105514843bac29b5c0e15a'
assert sha(P/'P16.5-paper.pdf')=='b796876a43d860d3fafaa7b367431e44e013ed1ee05cff4300608321ddeb75cf'
assert len(fitz.open(P/'P16.5-paper.pdf'))==24
log=(P/'P16.5-paper.log').read_text()
assert 'Output written on P16.5-paper.pdf' in log and 'Overfull' not in log and 'Undefined' not in log
C=R/'campaigns/round-129/P16.5-original-entire-general-big-equation-independent-review'
freeze=json.loads((C/'freeze.json').read_text())
for n,key in [('argument.md','argument_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/n)==freeze[key]
assert not (C/'review.sqlite').exists()
C128=R/'campaigns/round-128/P16.5-general-big-entire-genuine-E1-operator-independent-review'
assert sha(C128/'argument.md')=='aea004b853460b8fb5b2709ebda3fc47982b0dc1bff70429ddf88add287e40e4'
assert not (C128/'review.sqlite').exists()
notes=[]
for n in [169,170,171]:
    matches=list(K.glob(f'*continuation{n}.md'));assert len(matches)==1;notes.append(matches[0])
S=K/'current-small-batch125-126-20261006-continuation136';S.mkdir(exist_ok=False)
public={}
for n,label,db in [(125,'P16.5-entire-nef-big-variational-equation-independent-review','review.sqlite'),
                  (126,'P16.5-original-general-big-relative-operator-and-equation-research','work.sqlite')]:
    path=R/f'campaigns/round-{n}'/label/db
    result=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(path)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(result.stdout)
    assert status['status']=='running' and status['work']['active']==1 and status['work']['completed']==0
    assert status['calls']['byModel'][0]['model']=='gpt-6.1-sol'
    p=S/f'P16.5-round{n}-public-native-status.json';save(p,status)
    public[n]={'path':str(p),'sha256':sha(p),'observed_utc':status['observedAt']}
now=datetime.now(timezone.utc).isoformat()
layout={'recorded_utc':now,'scoped_verdict':'PASS','original_closed':False,
    'canonical_sha256':sha(P/'canonical-independent-review.json'),'argument_sha256':sha(P/'P16.5-argument.md'),
    'final_source_sha256':sha(P/'P16.5-paper.tex'),'final_pdf_sha256':sha(P/'P16.5-paper.pdf'),'PDF_pages':24,
    'all_whole_final_constituent_math_root_read':True,'whole_assembled_argument_separately_root_read':False,
    'whole_generated_tex_separately_root_read':False,'whole_canonical_report_premises_and_passages_root_read':True,
    'final_PDF_visual_pages_checked':[1,12,24],'two_final_local_builds_succeeded':True,'final_overfull_undefined_diagnostics':0,
    'formatting_changes':'Raw Unicode mathematical symbols converted to explicit LaTeX; long path/hash made breakable; one inline support inequality displayed; one floor estimate split; no mathematical change.',
    'native_compiler_request_final_cell':1889,'native_compiler_success_observed':False,'native_compiler_status':'PENDING',
    'existing_P16_4_editor_modified_or_new_tab_opened':False}
save(P/'root-reading-and-layout-binding-20261006.json',layout)
meta=json.loads((P/'publication-preparation.json').read_text())
meta.update({'source_sha256':layout['final_source_sha256'],'pdf_sha256':layout['final_pdf_sha256'],'PDF_pages':24,
             'PDF_layout_checked':True,'visual_pages':[1,12,24],'local_export_compilation_verified':True,
             'native_compiler_success_asserted':False,'native_compiler_final_cell':1889})
(P/'publication-preparation.json').write_text(json.dumps(meta,indent=2)+'\n')
T=R/'deliverables/scoped-P16.5-round124';T.mkdir(exist_ok=False)
publish_names=['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','canonical-independent-review.json',
               'source-application-ledger.json','publication-preparation.json','root-reading-and-layout-binding-20261006.json']
for n in publish_names:shutil.copyfile(P/n,T/n)
accepted={'recorded_utc':now,'atom':'P16.5','round':124,'verdict':'PASS','operation_id':review['operationId'],
    'scope':'Entire intrinsic nef operator, common-class mixed/weighted arbitrary decreasing nets, both outer signs, weak energy, intrinsic dual condition and coercivity. No inverse theorem or original closure.',
    'canonical_report':str(P/'canonical-independent-review.json'),'canonical_sha256':sha(P/'canonical-independent-review.json'),
    'whole_actual_report_premises_and_passages_root_read':True,'premises_count':7,'passages_count':12,
    'paper_source':str(T/'P16.5-paper.tex'),'paper_source_sha256':sha(T/'P16.5-paper.tex'),
    'paper_pdf':str(T/'P16.5-paper.pdf'),'paper_pdf_sha256':sha(T/'P16.5-paper.pdf'),'pages':24,
    'original_closed':False,'sole_equation_grant_scope':'Exact actual AMPLE G0 only.','all_recursive_foundations_reproved':False,
    'native_compiler_success_observed':False,'local_export_compilation_verified':True}
binding={'recorded_utc':now,'new_own_proofs':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
    'scope':'Own169 original continuous L1 approximation along bounded-cost model-output weak limits gives relative weighted and nonlinear Lipschitz limits. Own170 original rooftop energy variation proves model strict-winning atomic inequalities and passes them to full genuine maximum measure and strict-set mass comparison. Own171 separate numerically trivial actual rational bundles have constants as genuine cone, zero energy and raw target mass, and the zero equation unique modulo constants.',
    'new_math_independently_accepted':False,'original_closed':False,'prepared_original129':freeze,
    'whole_matching_primary_Corollary4_24_and_proof_root_read':'BJ arXiv1801.08229v4, local literal LF2501--2507; source SHA659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0.',
    'active_native_batch':[125,126],'next_native_launch_order':[128,129],
    'active_or_frozen_native_inputs_modified':False,'hot_feedback_sent':False,'existing_editor_unchanged':True}
B=K/'P16.5-root-continuation169-171-full-comparison-zero-range-and-original-review-binding-20261006.json';save(B,binding)
for n in ['active-work.json','checklist-current.json']:
    p=R/n;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==47
    assert [i['round'] for i in data['current_small_batch']['items']]==[125,126]
    data.update({'updated_utc':now,'historical_reviewed_scoped_papers':48,'P16_5_actual_scoped124':accepted,
                 'continuation169_171_general_big_comparison_and_zero_candidate':binding,
                 'prepared_original_general_big_equation_review129':freeze,'next_native_launch_order':[128,129],
                 'github_pending_checkpoint':'continuation136 frozen'})
    data.pop('round124_scoped_pass_pending_public_reader',None)
    for item in data['current_small_batch']['items']:
        s=public[item['round']];item.update({'public_status':s['path'],'public_status_sha256':s['sha256'],'observed_utc':s['observed_utc'],'observed_status':'running'})
    data['current_small_batch']['active_items']=list(data['current_small_batch']['items'])
    data['current_small_batch']['recorded_utc']=now
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        cols=line.split('\t');cols[2]='Original123 PARTIAL. Scoped independent124 PASS and 24-page paper published; 125/126 active. General-big143--171 unreviewed full candidate: genuine entire operator, intrinsic targets, all-target existence/all-solution uniqueness, comparison/domination, relative weighted continuity and actual completeness; separate numerically trivial zero-volume equation. Exact-original129 full packet frozen; operator128 next. Mixed nonnef products and general nonbig nonzero classes not asserted. Original remains open pending exact reconstruction.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation136-publication-records';D.mkdir(exist_ok=False)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':35,'historical_reviewed_scoped_papers':48,'newly_accepted_scoped_review':124,
    'current_native_small_batch':[125,126],'prepared_next_native_launch_order':[128,129],
    'original_closed':False,'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'} and 'LOCALONLY' not in p.name
    if p.suffix=='.pdf':assert p==T/'P16.5-paper.pdf'
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation136/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(T.iterdir()):add(p)
for p in notes+[B,previous,R/'record_verified135_20261006.py',R/'prepare_intrinsic_nef_scoped_reader124_20261006.py',R/'prepare_original_general_big_full_equation_review129_20261006.py',Path(__file__)]:add(p)
for n in ['task.json','settings.json','freeze.json','mathematical-data-bindings.json']:add(C/n)
for p in sorted(S.iterdir()):add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation136.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':48,
    'commit_message':'Publish reviewed intrinsic nef paper and candidate full big comparison with zero-mass equation range',
    'scope':binding['scope']+' New full general-big mathematics unreviewed. Scoped124 PASS. Seven originals solved,35open,48 independently accepted scoped papers.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'originals_solved':7,'originals_open':35,
                  'reviewed_scoped_papers':48,'current_batch':[125,126],'next_launches':[128,129]},indent=2))
