from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-189').iterdir());D=K/'public-P16.4-continuation227-genus-zero-equation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round189-settled-inspection-LOCALONLY.json').read_text());ca=x['campaign'];k=ca['result']
assert ca['status']=='completed' and ca['error'] is None and k['verdict']=='PASS'
req=next(t['data']['payload'] for t in x['records'] if t['kind']=='xean.call.request')
msg=next(t['data']['message'] for t in x['records'] if t['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    t=json.loads(line)
    if t.get('type')=='item.completed' and t.get('item',{}).get('type')=='agent_message':
        try:n=json.loads(t['item']['text'])
        except (ValueError,TypeError):continue
        if isinstance(n,dict) and set(n)=={'verdict','report','premises','passages'}:finals.append(n)
assert len(finals)==1;n=finals[0]
assert all(k[q]==n[q] for q in ('verdict','report','premises'))
assert len(k['premises'])==7 and len(k['passages'])==len(n['passages'])==13
normalization=[]
for i,(a,b) in enumerate(zip(n['passages'],k['passages'])):
    assert {q:b[q] for q in ('premise','url','quote')}==a
    assert b['id']==k['operationId']+'/'+str(i) and 0<=b['premise']<7 and b['statement']==k['premises'][b['premise']]
    normalization.append(dict(index=i,id=b['id'],unchanged_model_fields=['premise','url','quote'],kernel_added_fields=['id','statement']))
coverage=[]
for i,p in enumerate(k['premises']):
    ps=[z for z in k['passages'] if z['premise']==i and z['url'].startswith(('https://','http://'))];assert ps
    coverage.append(dict(premise_index=i,exact_statement=p,external_passage_ids=[z['id'] for z in ps],urls=sorted({z['url'] for z in ps})))
prompt=json.loads(req['prompt']);assert set(prompt)=={'task','argument'}
argument=(C/'argument.md').read_text()
assert prompt['task']==json.loads((C/'task.json').read_text()) and prompt['argument']==argument
assert req['model']=='gpt-6.1-sol' and req['reasoning']=='xhigh' and req['sandbox']=='read-only' and req['shell'] is False
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
entries=json.loads((C/'mathematical-data-bindings.json').read_text());lines=argument.splitlines()
for item in entries:
    p=Path(item['source']);lo,hi=item['argument_inclusive_lf']
    assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
    assert '\n'.join(lines[lo-1:hi])==p.read_text().rstrip('\n')
assert sha(D/'P16.4-paper.tex')=='bf78e6188aea85eb34c06fa6d6152900259207318d843037f2e29e2cca712f57'
assert sha(D/'P16.4-paper.pdf')=='1f003191231e97df194a2051eb271504ba47add24d14cfd60bb08fc433eb0f12'
r=json.loads((D/'root-reproduction-binding-20261007.json').read_text());ar=json.loads((D/'root-whole-argument-read-addendum-20261007.json').read_text());v=json.loads((D/'root-limited-pdf-visual-addendum-20261007.json').read_text());co=json.loads((D/'native-compiler-success-final-source-addendum-20261007.json').read_text())
assert r['whole_saved_source_root_read'] and r['whole_four_notes_root_read'] and r['fresh_final_local_builds']==2 and r['root_finite_check_rerun']
assert ar['whole_native_argument_separately_root_read'] and ar['argument_sha256']==sha(D/'P16.4-argument.md')
assert co['source_sha256']==sha(D/'P16.4-paper.tex') and co['native_result']['kind']=='success'
assert v['pdf_sha256']==sha(D/'P16.4-paper.pdf') and v['root_visual_pages_read']==[1,11]
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ('active-work.json','checklist-current.json'):
    j=json.loads((R/name).read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==75 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
canonical=K/'P16.4-round189-actual-canonical-independent-review-20261007.json'
native=K/'P16.4-round189-native-model-final-review-20261007.json'
binding=K/'P16.4-round189-whole-genus-zero-review-binding-20261007.json'
accept=D/'whole-partial-paper-acceptance189-20261007.json';clar=D/'harmless-reader-clarifications189-20261007.json'
assert not any(p.exists() for p in (canonical,native,binding,accept,clar))
now=datetime.now(timezone.utc).isoformat()
scope='Every actual smooth geometrically integral projective GENUS-ZERO curve over every complete characteristic-zero/residue-characteristic-zero real-valued non-Archimedean field, actual ample rational L with raw mass degL: actual finite polarized splitting, finite Gauss orbit and actual typeII circumcenter, genuine continuous single-atom norming reference, exact intrinsic all-E1 integrability/finite continuous-dual/unit-cost equivalence and sublinear coercivity; ACTUAL equation existence for arbitrary positive Radon target support, every-solution all-point uniqueness modulo finite constants, exact energy/dual attainment and reference corrections. Trivial fields use wholeT; nontrivial nonsplit/nondiscrete/non-AC fields descend actual solutions from wholeQ through wholeD after verified invariance, with no singular averaging or field-degree factor. Includes a concrete complete Hahn field R((t^Q)) anisotropic conic and genuine two-orbit atom example. Entire11-page source851LF accepted relative only to six complete grants and all clarifications.'
gaps='OriginalP16.4 positive-genus curves and dimension>=2 prescribed-target existence, actual attainment and every-solution all-point uniqueness remain open. P16.3/P16.7 and nonample/singular/proper-nonprojective/nonalgebraizable axes are separate.'
canonical.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
b=dict(recorded_utc=now,round=189,continuation=227,atom='P16.4',verdict='PASS',operation_id=k['operationId'],reported_at=k['reportedAt'],canonical_review=str(canonical),canonical_review_sha256=sha(canonical),native_model_final=str(native),native_model_final_sha256=sha(native),entire_report_all_premises_and_passages_root_read=True,premises=7,passages=13,all_zero_based_exact_statement_bindings_verified=True,external_coverage=coverage,passage_normalization=normalization,task_only_passages_excluded_from_external_coverage=[],unindexed_caller_grants_excluded_from_external_coverage=['O217','D214','N220','T171','Q222','C218'],kernel_report_premises_and_quotes_equal_native_final=True,exact_decoded_native_task_and_argument_equal_entire_frozen_inputs=True,all_whole_math_data_bodies_equal_frozen_sources=True,whole_math_data_bodies=len(entries),native_prompt_sha256=hashlib.sha256(req['prompt'].encode()).hexdigest(),frozen_task_sha256=f['task_sha256'],frozen_argument_sha256=f['argument_sha256'],frozen_settings_sha256=f['settings_sha256'],model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],caller_grants=['O217','D214','N220','T171','Q222','C218'],accepted_partial_scope=scope,whole_partial_manuscript_accepted=True,original_closed=False,new_accepted_scoped_paper=True,residual_original_gaps=gaps,root_recursive_primary_proof_reading_claimed=False,private_active_output_read=False,hot_feedback_sent=False,protected_editor_unchanged=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
a=dict(recorded_utc=now,atom='P16.4',continuation=227,independent_review_round=189,verdict='PASS',cumulative_accepted_paper_number=76,source=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),source_lf_lines=851,pdf=str(D/'P16.4-paper.pdf'),pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=11,review_binding=str(binding),review_binding_sha256=sha(binding),accepted_scope=scope,only_caller_grants=['O217','D214','N220','T171','Q222','C218'],whole_final_saved_source_root_read=True,whole_native_argument_separately_root_read=True,whole_independent_report_all_premises_and_passages_root_read=True,fresh_final_local_builds=2,local_warnings=r['local_warnings'],native_compiler_success=True,root_visual_pages_read=[1,11],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,fully_solved_original_atoms_count=9,original_closed=False,residual_original_scope=gaps,protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
accept.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
clar.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=189,source_sha256=sha(D/'P16.4-paper.tex'),exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,clarifications=['Inversion includes the equality boundary r=|b|: zeta(b,r)=zeta(0,r) there, and inversion gives zeta(0,1/r).','Subdivide finite arcs at meeting disks before treating pieces as nested disk paths.','For a cleared degree-ma bundle, divide the ENTIRE degree-ma monomial Fubini-Study expression by m.','Residual equation gaps refer to the nontrivially valued scope; wholeT already grants the trivial-field boundary.']),ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());j.update(historical_reviewed_scoped_papers=76,updated_utc=now,P16_4_accepted_genus_zero189=a,goal_state='9/42 originals independently accepted;33open;76 cumulative independently accepted scoped/supporting papers. Whole all-original-field genus-zero equation accepted189; positive-genus and higher-dimensional original scope remains open. Continue batches of at most two and verified regular GitHub pushes.',next_work='Native195 actual direct formal-FS/residual-curvature author active on unchanged originalP16.4; native194 settled with unregistered support-label error and candidate=false full10-page PA contact draft requiring whole reading/reproduction/review. No hot feedback to195.')
    if name=='checklist-current.json':
        for target in j['targets']:
            if target['id']=='P16.4':
                assert not target['fully_solved'] and target['closure']=='open'
                target.update(research_status='all_original_field_genus_zero_equation_accepted_positive_genus_and_higher_dimensions_open',current_focus='Whole227 PASS189 with six complete grants; native195 investigates actual all-genus formalFS bridge. Full original remains open.')
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as fh:
    reader=csv.DictReader(fh,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['ID']=='P16.4':row['Research']='all_original_field_genus_zero_equation_accepted_positive_genus_and_higher_dimensions_open'
with table.open('w',newline='') as fh:
    writer=csv.DictWriter(fh,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=76,review_round=189,originals_solved=9,originals_open=33,acceptance_record=str(accept),acceptance_sha256=sha(accept),review_binding_sha256=sha(binding)),indent=2))
