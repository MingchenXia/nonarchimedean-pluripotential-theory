from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-215/P05.2-unchanged-all-continuous-affine-arrangement-independent-native-local-source-audit'
A=C/'artifacts/codex-5hrV64'
D=K/'public-P05.2-continuation282-all-continuous-affine-spaces-and-affine-arrangements'
E=D/'evidence/independent-local-audit215'
binding=K/'P05.2-round215-whole-affine282-local-source-audit-INCONCLUSIVE-and-ROOT-mathematical-binding-20261008.json'
accept=D/'whole-mathematical-paper-acceptance-after-audit215-20261008.json'
clar=D/'harmless-reader-clarifications-after-audit215-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [E,binding,accept,clar])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
f=load(C/'freeze.json');inspection=load(K/'round215-settled-inspection-LOCALONLY.json')
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==f[key]
assert f['only_grants']==['A224','B225','R230','S262','S272'] and f['all_clarifications_retained']
assert inspection['campaign']['status']=='completed'
requests=[e['data']['payload'] for e in inspection['records'] if e['kind']=='xean.call.request'];assert len(requests)==1
req=requests[0];assert req['model']=='gpt-6.1-sol' and req['reasoning']=='xhigh' and req['sandbox']=='workspace-write' and req['shell'] is True and req['webSearch']=='disabled'
actual_input=json.loads(req['prompt']);assert actual_input.pop('workspace')==str(A);assert actual_input==load(C/'input.json')
native=K/'P05.2-round215-exact-native-model-final-whole-affine282-local-audit-20261008.json'
notes=load(native);assert len(notes['notes'])==5 and notes['candidate'] is False
assert native.read_bytes()==(A/'native-notes.json').read_bytes()
registered=inspection['campaign']['result'];assert registered['candidate'] is False and len(registered['notes'])==5
for x,y in zip(registered['notes'],notes['notes']):
    assert {k:v for k,v in x.items() if k!='text'}=={k:v for k,v in y.items() if k!='text'}
    assert x['text']==y['text']+'\n\nArtifacts: '+str(A)
for fname,count in [('mathematical-packet-bindings.json',27),('historical-own-evidence-bindings.json',46),('private-primary-packet-bindings.json',4)]:
    data=load(C/fname);assert len(data)==count
    for e in data:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for fname,count in [('frozen-file-bindings.json',81),('own-artifact-manifest.json',40)]:
    data=load(A/fname);assert len(data)==count
    for e in data:
        p=Path(e['path']) if 'path' in e else A/e['file'];assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
report=load(A/'audit-report.json')
assert report['overall_verdict']=='INCONCLUSIVE' and report['mathematical_reconstruction_verdict']=='PASS' and report['conditional_on_exactly_five_whole_grants']
assert report['ordinary_premises_and_complete_reasoning']==notes['notes']
for key,fname in [('coverage','premise-and-wholeproof-coverage.json'),('source_audit','source-application-audit.json'),('historical_comparison','historical-comparison.json'),('finite_evidence','finite-output.json'),('build_evidence','build-output.json')]:assert report[key]==load(A/fname)
cov=report['coverage'];assert cov['exact_grant_group_count']==5 and len(cov['body_coverage'])==27 and len(cov['paper_sections'])==12 and len(cov['numbered_statement_proofs'])==12 and len(cov['numbered_equations'])==4
covered=set()
for e in cov['paper_sections']:
    assert e['verdict']=='PASS';covered.update(range(e['LF'][0],e['LF'][1]+1))
assert covered==set(range(1,745))
rep=load(D/'root-reproduction-binding-20261008.json')
for key in ['source','argument','pdf']:assert sha(rep[key])==rep[key+'_sha256']
assert rep['source_LF_lines']==744 and rep['pdf_pages']==11 and rep['local_build_exit_codes']==[0,0]
assert rep['latex_to_markdown_exact'] and not rep['markdown_to_latex_reversibility_claimed']
scratch=K/'round215-root-reproduction-LOCALONLY';assert (scratch/'finite_check.py').read_bytes()==(A/'finite_check.py').read_bytes()
assert (scratch/'certificate-input.json').read_bytes()==(A/'certificate-input.json').read_bytes()
assert (scratch/'finite-output.json').read_bytes()==(A/'finite-output.json').read_bytes()
source_audit=report['source_audit'];assert len(source_audit['applications'])==12
for e in source_audit['sources']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
prior_source=K/'P05.2-round210-whole-local-source-audit-INCONCLUSIVE-and-ROOT-mathematical-binding-20261007.json'
assert sha(prior_source)=='87a70a9902c400f09addbef6a3e8f08fa9da761f6c4ac4b9b1d392d048635d62'
extra=load(K/'round215-additional-original-unit-read-ranges-LOCALONLY.json')
assert sum(e['LF'][1]-e['LF'][0]+1 for e in extra)==66
old=load(prior_source)
for e in source_audit['applications']:
    covered=set()
    for o in old['actual_source_units']:
        if o['path']==e['text_path'] and o['sha256']==e['text_sha256']:covered.update(range(o['LF_range'][0],o['LF_range'][1]+1))
    for o in extra:
        if o['path']==e['text_path'] and o['sha256']==e['text_sha256']:covered.update(range(o['LF'][0],o['LF'][1]+1))
    for lo,hi in e['literal_LF_ranges']:assert set(range(lo,hi+1))<=covered
E.mkdir(parents=True)
for name in ['audit-report.json','source-application-audit.json','premise-and-wholeproof-coverage.json','historical-comparison.json','frozen-file-bindings.json','own-artifact-manifest.json','native-notes.json','finite_check.py','certificate-input.json','finite-output.json','build-output.json','verification-output.json','read-log.jsonl','read_packet.py','verify_inputs.py','build_own.py','assemble_audit.py','own-pandoc.stderr.log','own-pandoc.stdout.log','own-pass1.stderr.log','own-pass1.stdout.log','own-pass2.stderr.log','own-pass2.stdout.log']:
    shutil.copyfile(A/name,E/name)
shutil.copyfile(native,E/'exact-native-final.json');write(E/'registered-native-worker-result.json',registered)
for name in ['certificate-input.json','finite-output.json','stdout.txt','stderr.txt']:shutil.copyfile(scratch/name,E/('ROOT-independent-'+name))
now=datetime.now(timezone.utc).isoformat()
scope='ENTIRE unchanged744-LF11-page282 mathematical sector: ALL continuous convex relative endpoints on complete rational affine d-spaces, ALL dimensions d>=1, ACTUAL arbitrary REAL PA positive-growth references on rational geometry, genuine GLOBAL decreasing same-reference regularization before raw MA; finite-obstacle epigraph recognition, raw flat-lineality contact, legal finite PCC/Bellman trees, localized signed-TV completed-domain continuity and fixed-C tightness, ALL C_b raw affine contact; strictly saturated determinant atom and positive complete-subcycle transverse obstruction; finite affine-plane arrangements with positive REAL weights have simultaneous all-C_b domain/contact iff pairwise disjoint. Exactly5whole grants/allclarifications; no inverse/Alexandrov replacement.'
gaps='OriginalP05.2 remains OPEN: general singular all-obstacle completed-domain membership, non-PA contact sufficiency, complete necessary-and-sufficient structural classification over all pairs/refinements, and abstract/glued/compact categories; literal coefficient conventions stay separate. Scoped arrangement classification does not close the original.'
proof_clarification='The brief rational-box sentence at sourceLF160-164 is NOT permission to coarsen a required carrier. Use the complete inherited-complex argument: on each closed rational cell, rational endpoints and rational barycentric centers in its feasible face are dense, so continuity and legal same-cell PCC give convexity. A rational-endpoint segment crosses rational faces at rational parameters; its finitely many intervals lie in cells. At each crossing the minimal center face is a face of both incident endpoint cells; nearby rational opposite endpoints give a legal midpoint inequality, forcing the left convex secant/derivative not to exceed the right. Thus convexity glues along every rational segment. Density of rational endpoint pairs and continuity give every real segment. This proves the stated equivalence without any coarsening or assumption of automatic continuity for unrestricted competitors. R230 still handles those competitors.'
b=dict(recorded_utc=now,round=215,continuation=282,atom='P05.2',native_whole_evidence_verdict='INCONCLUSIVE',native_mathematical_sector_verdict='PASS',ROOT_mathematical_verdict='PASS',canonical_xean_review_role=False,automatic_acceptance=False,operation_id=req['operationId'],model=req['model'],reasoning=req['reasoning'],native_final=str(native),native_final_sha256=sha(native),own_native_FINAL_equals_own_saved_prose_byte_for_byte=True,registered_notes_match_exact_FINAL_plus_only_artifact_suffix=True,all_five_exact_FINAL_notes_ROOT_read=True,whole_master_report_unique_contents_ROOT_read=True,repeated_master_sections_exactly_equal_entire_ROOT_read_separate_reports=True,all12_named_proofs4_equations12_sections_and_every_unnumbered_claim_ROOT_read=True,all27_math46_ownhistory4_primary81_auditorbindings40_ownartifact_bindings_verified=True,all4_whole_primaries_ROOT_read_claimed=False,whole_original_application_units=source_audit['applications'],prior_whole22_original_unit_read_binding=str(prior_source),prior_whole22_original_unit_read_binding_sha256=sha(prior_source),new_original_LF_ranges_ROOT_read=extra,new_original_LF_lines_ROOT_read=66,all12_whole_wider_source_application_units_covered=True,recursive_foundations_not_all_freshly_reconstructed=True,whole744_tex700_argument34_ledger17_scope4_author_FINAL_and4_separate_saved_drafts_ROOT_read=True,author213_all4_saved_notes_differ_from_exact_FINAL_retained=True,ROOT_read_independent_auditor_checker_before_own_copy_execution=True,ROOT_independent_finite_output_exact_860B_input2120B_output=True,finite_execution_not_continuum_proof=True,prior_root_exact_conversion_and_two_clean_final_local_build_reproduction_retained=True,source_preserved=True,whole_mathematical_sector_accepted=True,whole_historical_evidence_PASS_claimed=False,historical_execution_sector=report['historical_execution_verdict'],universal_past_read_or_negative_operation_assertions_certified=False,full_inherited_carrier_convexity_clarification=proof_clarification,builtin_request_cell249_tracking_lost_after_environment_transition=True,builtin_final_diagnostics_or_success_or_failure_not_observed=True,accepted_scope=scope,residual_original_scope=gaps,original_closed=False,no_private_ACTIVE_output_read=True,no_hot_feedback=True,protected_editor_unchanged_open=True,no_new_tab=True)
write(binding,b)
a=dict(recorded_utc=now,atom='P05.2',continuation=282,grant_label='S282',independent_native_audit_round=215,native_whole_evidence_verdict='INCONCLUSIVE',native_mathematical_verdict='PASS',ROOT_mathematical_verdict='PASS',canonical_xean_review_role=False,automatic_acceptance=False,cumulative_accepted_paper_number=82,source=rep['source'],source_sha256=rep['source_sha256'],source_LF_lines=744,argument=rep['argument'],argument_sha256=rep['argument_sha256'],pdf=rep['pdf'],pdf_sha256=rep['pdf_sha256'],pdf_pages=11,review_binding=str(binding),review_binding_sha256=sha(binding),accepted_scope=scope,only_caller_grants=['A224','B225','R230','S262','S272'],all_clarifications_retained=True,exact_reviewed_source_preserved=True,builtin_compiler_success_claimed=False,builtin_request_cell249_tracking_lost=True,all11_pdf_pages_visually_ROOT_read_claimed=False,originals_solved=9,originals_open=33,original_closed=False,residual_original_scope=gaps,protected_editor_unchanged_open=True)
write(accept,a)
write(clar,dict(recorded_utc=now,source_sha256=rep['source_sha256'],exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,clarifications=[proof_clarification,'Native215 WHOLE historical-evidence INCONCLUSIVE remains unchanged. Mathematics and finite/conversion/build sectors PASS; ROOT independently accepts only the whole scoped mathematical sector. Historical universal read/no-operation claims are not analytic premises.','Auditor215 own saved output equals its exact5-note FINAL byte-for-byte. Author213 saved4-note draft differs in all prose fields from its exact FINAL; both were fully ROOT-read and preserved. Registered results add only their bound Artifacts suffixes.','First local/native LaTeX pass retains undefined-reference/rerun warnings; final pass is clean. Source-to-Markdown equivalence is exact; no reverse Markdown-to-TeX claim is made. Finite arithmetic illustrates the continuum proof, never certifies it.','Previously queued builtin249/204/27 handles became unavailable across the environment transition. This is loss of diagnostic tracking, not evidence of compiler success or failure; no duplicate request or protected editor action was made.','Only5whole grants/allqualifications are premises; working ROOT drafts are independently reconstructed or unused. Full source applications retain REAL/signed/zero cycle calibration and explicit excluded automatic-continuity/literal-density/AR10 routes. Original general classification stays OPEN.'],all_prior_caller_clarifications_preserved=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=load(p);assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==81 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,historical_reviewed_scoped_papers=82,P05_2_accepted_all_continuous_affine282_after215=a,goal_state='9/42 original problems solved;33 open;82 accepted scoped/supporting mathematical papers. S282 all-continuous affine regularization/contact and arrangement contact criterion accepted; general originals stay open.',next_work='Continue original216 P05.1 classification and217 independently reconstruct288 isolated-crossing regularization paper, exactlytwo native61xhigh campaigns. ROOT can progress independent math; no private ACTIVE reads or hotfeedback. NewS282 whole scoped mathematics is accepted with every clarification and nativewholeINCONCLUSIVE preserved. All33 original goals and regular verified pushes persist.')
    if name=='checklist-current.json':
        t=next(q for q in j['targets'] if q['id']=='P05.2');assert not t['fully_solved'] and t['closure']=='open'
        t.update(research_status='all_continuous_affine_and_arrangement_contact_mathematics_accepted_general_classification_open',current_focus='Whole282 scoped mathematics accepted after independent215 and ROOT fullmath/source/evidence/exactfinite review; nativewholehistoricalINCONCLUSIVE preserved. General singular domain/nonPAcontact/fullstructural classification OPEN.')
    write(p,j)
table=R/'checklist-current.tsv'
with table.open(newline='') as fh:reader=csv.DictReader(fh,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['ID']=='P05.2':row['Research']='all_continuous_affine_and_arrangement_contact_mathematics_accepted_general_classification_open'
with table.open('w',newline='') as fh:writer=csv.DictWriter(fh,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=82,continuation=282,native_whole_evidence='INCONCLUSIVE',native_mathematical_verdict='PASS',ROOT_mathematical_verdict='PASS',acceptance_sha256=sha(accept),review_binding_sha256=sha(binding),originals_solved=9,originals_open=33),indent=2))
