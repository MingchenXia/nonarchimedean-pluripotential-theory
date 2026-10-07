from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv

R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-204').iterdir())
D=K/'public-P05.2-continuation262-corrected-raw-uniformities-and-all-continuous-graph-contact'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x=json.loads((K/'round204-settled-inspection-LOCALONLY.json').read_text());k=x['campaign']['result']
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None and k['verdict']=='PASS'
req=next(z['data']['payload'] for z in x['records'] if z['kind']=='xean.call.request')
msg=next(z['data']['message'] for z in x['records'] if z['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
finals=[]
for line in msg['stdout'].splitlines():
    z=json.loads(line)
    if z.get('type')=='item.completed' and z.get('item',{}).get('type')=='agent_message':
        try:n=json.loads(z['item']['text'])
        except (ValueError,TypeError):continue
        if isinstance(n,dict) and set(n)=={'verdict','report','premises','passages'}:finals.append(n)
assert len(finals)==1;n=finals[0]
assert n==json.loads((K/'round204-exact-native-FINAL-for-root-LOCALONLY.json').read_text())
assert all(k[q]==n[q] for q in ('verdict','report','premises'))
assert len(k['premises'])==3 and len(k['passages'])==len(n['passages'])==14
normalization=[]
for i,(a,b) in enumerate(zip(n['passages'],k['passages'])):
    assert {q:b[q] for q in ('premise','url','quote')}==a
    assert b['id']==k['operationId']+'/'+str(i)
    assert isinstance(b['premise'],int) and 0<=b['premise']<3 and b['statement']==k['premises'][b['premise']]
    normalization.append(dict(index=i,id=b['id'],unchanged_model_fields=['premise','url','quote'],kernel_added_fields=['id','statement']))
coverage=[]
for i,p in enumerate(k['premises']):
    ps=[z for z in k['passages'] if z['premise']==i and z['url'].startswith(('https://','http://'))];assert ps
    coverage.append(dict(premise_index=i,exact_statement=p,external_passage_ids=[z['id'] for z in ps],urls=sorted({z['url'] for z in ps})))
prompt=json.loads(req['prompt']);assert set(prompt)=={'task','argument'}
argument=(C/'argument.md').read_text()
assert prompt['task']==json.loads((C/'task.json').read_text()) and prompt['argument']==argument
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'])==('gpt-6.1-sol','xhigh','read-only',False)
f=json.loads((C/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
entries=json.loads((C/'mathematical-data-bindings.json').read_text());assert len(entries)==20
for e in entries:
    p=Path(e['source']);lo,hi=e['argument_inclusive_lf']
    assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
    assert argument.splitlines()[lo-1:hi]==p.read_text().splitlines()
r=json.loads((D/'root-reproduction-binding-20261007.json').read_text());v=json.loads((D/'root-visual-and-builtin-request-scope-addendum-20261007.json').read_text())
unavailable=json.loads((D/'root-builtin-unavailable-addendum-20261007.json').read_text())
assert r['whole1953_tex_root_read'] and r['whole1878_native_argument_separately_root_read'] and r['whole_eight_exact_canonical_final_notes_root_read']
assert r['whole57_ledger_root_read'] and r['whole_material_change_record_root_read'] and r['own_checker_reproduced'] and r['whole_markdown_exact_pandoc_conversion_reproduced']
assert r['root_local_build_exit_codes']==[0,0] and not r['root_local_warnings']
assert sha(D/'P05.2-paper.tex')==r['source_sha256']=='b756af20301a93fba71af139b24b5bc8fd264b57a54a1d941aa05392d97f33f7'
assert sha(D/'argument.md')==r['argument_sha256'] and sha(D/'P05.2-paper.pdf')==r['root_pdf_sha256']
assert v['root_actual_visual_read_pages']==[1,14,21,24,27] and not v['all_pdf_pages_visually_read']
assert unavailable['returned_result']=='No handler registered for tool: codex_app.compile_latex_document' and not unavailable['builtin_success']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ('active-work.json','checklist-current.json'):
    j=json.loads((R/name).read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==77 and j['github_pending_checkpoint'] is None
canonical=K/'P05.2-round204-actual-canonical-independent-review-20261007.json'
native=K/'P05.2-round204-native-model-final-review-20261007.json'
binding=K/'P05.2-round204-whole-graph-contact-review-binding-20261007.json'
accept=D/'whole-partial-paper-acceptance204-20261007.json';clar=D/'harmless-reader-clarifications204-20261007.json'
assert not any(p.exists() for p in (canonical,native,binding,accept,clar))
now=datetime.now(timezone.utc).isoformat()
scope=('ENTIRE27-page continuation262: all19 results/unnumbered applications,1953TeX/1878Markdown/57ledger/material record and EIGHT exact notes accepted relative to precisely THREE complete A224/B225/R230 grants and ALL clarifications. Primitive/unit raw recursion, all finite PA cone/contact criteria and coupled12,6,6/raw24/contact-3 actual examples; real rational-reference jet gluing and actual mixed completion; material uniformity repair retaining ordinary weak C_b continuity/global vague uniformity and weak/BL uniformity ONLY on each fixed-C family with exact K_C for ALL completed tuples; genuine quadratic nonPA raw measure, literal gap3/64, noncompact literal obstruction/dimension-zero branch. NEW complete all-continuous REAL finite embedded graph theory on rational geometry, arbitrary actual real reference coefficients/positive weights: edge/vertex derivative and support criterion, genuine shared-rational-mesh regularization before operator, primitive/Stieltjes raw completion including irrational reference, ALLC_b envelope membership and exact all-obstacle contact iff each local relation cone equals the actual weight ray. Finite tests/builds and old favorable failed discussions are not grants.')
gaps=('Full original P05.2 remains OPEN: higher-dimensional all-obstacle/nonPA regularization and contact sufficiency, arbitrary-irrational-reference mixed completion and a complete necessary/sufficient geometric classification. Old247/196 and255/200 remain FAIL; material PC-floor hypothesis, coupled endpoint replacement and fixed-C weak/BL restrictions are retained.')
canonical.write_text(json.dumps(k,ensure_ascii=False,indent=2)+'\n');native.write_text(json.dumps(n,ensure_ascii=False,indent=2)+'\n')
b=dict(recorded_utc=now,round=204,continuation=262,atom='P05.2',verdict='PASS',operation_id=k['operationId'],reported_at=k['reportedAt'],
       canonical_review=str(canonical),canonical_review_sha256=sha(canonical),native_model_final=str(native),native_model_final_sha256=sha(native),
       entire_report_all3_premises_and_all14_passages_root_read=True,all_zero_based_exact_statement_bindings_verified=True,
       external_coverage=coverage,passage_normalization=normalization,task_only_passages_excluded_from_external_coverage=[k['passages'][13]['id']],
       unindexed_caller_grants_excluded_from_external_coverage=['A224','B225','R230'],
       kernel_report_premises_and_quotes_equal_native_final=True,exact_decoded_native_task_and_argument_equal_entire_frozen_inputs=True,
       all20_whole_math_data_bodies_and_lf_bindings_equal_frozen_sources=True,
       native_prompt_sha256=hashlib.sha256(req['prompt'].encode()).hexdigest(),frozen_task_sha256=f['task_sha256'],frozen_argument_sha256=f['argument_sha256'],frozen_settings_sha256=f['settings_sha256'],
       model=req['model'],reasoning=req['reasoning'],child_sandbox=req['sandbox'],shell=req['shell'],caller_grants=f['only_mathematical_grants'],
       accepted_partial_scope=scope,whole_partial_manuscript_accepted=True,original_closed=False,new_accepted_scoped_paper=True,
       residual_original_gaps=gaps,root_recursive_primary_proof_reading_claimed=False,
       private_active_output_read=False,hot_feedback_sent=False,protected_editor_unchanged_open=True)
binding.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
a=dict(recorded_utc=now,atom='P05.2',continuation=262,grant_label='S262',independent_review_round=204,verdict='PASS',cumulative_accepted_paper_number=78,
       source=str(D/'P05.2-paper.tex'),source_sha256=sha(D/'P05.2-paper.tex'),source_lf_lines=1953,argument_sha256=sha(D/'argument.md'),
       pdf=str(D/'P05.2-paper.pdf'),pdf_sha256=sha(D/'P05.2-paper.pdf'),pdf_pages=27,review_binding=str(binding),review_binding_sha256=sha(binding),
       accepted_scope=scope,only_caller_grants=f['only_mathematical_grants'],whole_source_argument_ledger_material_eight_exact_notes_root_read=True,
       whole_independent_report_all_premises_passages_root_read=True,local_build_exit_codes=r['root_local_build_exit_codes'],local_warnings=r['root_local_warnings'],
       builtin_compiler_requested=True,builtin_compiler_available=False,builtin_compiler_returned_result=unavailable['returned_result'],builtin_compiler_success_claimed=False,
       root_visual_pages_read=[1,14,21,24,27],all_pdf_pages_visually_root_read=False,exact_reviewed_source_preserved=True,
       fully_solved_original_atoms_count=9,original_closed=False,residual_original_scope=gaps,protected_editor_unchanged_open=True,no_active_private_streams_read=True,no_hot_feedback_sent=True)
accept.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
clar.write_text(json.dumps(dict(recorded_utc=now,independent_review_round=204,source_sha256=a['source_sha256'],exact_reviewed_source_preserved=True,
       substantial_mathematical_repair=False,material_PC_floor_coupled_replacement_and_fixed_C_weak_BL_hypotheses_retained=True,
       clarifications=['BBGS Proposition3.19 commuting reference is3.15; already disclosed.','Decreasing means nonincreasing where appropriate.','Divisor-support assertions use a common PA carrying structure.','The dyadic final half-jump includes j=N.','YZsheet vertex counts exclude the additional horizontal origin; full cycle counts include it.','Graph Stieltjes measures lie on edge interiors; endpoint derivatives enter vertex coefficients.']),indent=2)+'\n')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());j.update(historical_reviewed_scoped_papers=78,updated_utc=now,P05_2_accepted_all_continuous_graph204=a,
       goal_state='9/42 originals independently solved;33open;78 cumulative accepted scoped/supporting papers. Entire corrected raw uniformities/all-continuous graph theory accepted204; higher-dimensional original classification remains open.',
       next_work='Original205 actual all-genus/general-dimensional P16.4 equation active. Next P05.2 original author receives FOUR whole A/B/R/S262 grants and ALL clarifications; advance complete higher-dimensional all-obstacle classification. Continue few campaigns and verified GitHub publication.')
    j['P05_2_corrected_graph_paper'].update(independent_verdict='PASS',new_mathematical_grant=True,grant_label='S262',original_closed=False)
    if name=='checklist-current.json':
        for target in j['targets']:
            if target['id']=='P05.2':
                assert not target['fully_solved'] and target['closure']=='open'
                target.update(research_status='all_continuous_real_graph_contact_and_corrected_raw_completion_accepted_general_classification_open',current_focus='Whole262 PASS204; arbitrary real graph reference/allC_b contact classified, material fixed-C weak/BL restriction retained. Complete higher-dimensional all-obstacle/nonPA/arbitrary-reference classification OPEN.')
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
table=R/'checklist-current.tsv'
with table.open(newline='') as fh:reader=csv.DictReader(fh,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['ID']=='P05.2':row['Research']='all_continuous_real_graph_contact_and_corrected_raw_completion_accepted_general_classification_open'
with table.open('w',newline='') as fh:writer=csv.DictWriter(fh,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=78,review_round=204,originals_solved=9,originals_open=33,acceptance_record=str(accept),acceptance_sha256=sha(accept),review_binding_sha256=sha(binding)),indent=2))
