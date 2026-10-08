from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-214/P16.4-unchanged-higher-dimensional-stability-independent-native-local-source-audit'
A=C/'artifacts/codex-ZBkDrk'
D=K/'public-P16.4-continuation279-higher-dimensional-stability-and-maximizing-output-limits'
S=K/'round214-root-reproduction-LOCALONLY';E=D/'evidence/independent-local-audit214'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not S.exists() and not E.exists()
x=load(K/'round214-settled-inspection-LOCALONLY.json')
assert x['campaign']['status']=='completed' and x['campaign']['error'] is None
req=next(q['data']['payload'] for q in x['records'] if q['kind']=='xean.call.request')
msg=next(q['data']['message'] for q in x['records'] if q['kind']=='xean.call.settled')
assert msg['exitCode']==0 and not msg['failed'] and not msg['isCanceled']
assert (req['model'],req['reasoning'],req['sandbox'],req['shell'],req['webSearch'])==('gpt-6.1-sol','xhigh','workspace-write',True,'disabled')
inp=load(C/'input.json');prompt=json.loads(req['prompt'])
assert all(prompt[k]==inp[k] for k in ['task','notes','assignment'])
assert {k:v for k,v in prompt.items() if k!='workspace'}==load(A/'input.json')==inp
assert prompt['workspace']==str(A)
f=load(C/'freeze.json')
for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256'),('private-primary-packet-bindings.json','private_primary_packet_bindings_sha256')]:assert sha(C/name)==f[key]
for name,count in [('mathematical-packet-bindings.json',31),('historical-own-evidence-bindings.json',87),('private-primary-packet-bindings.json',62)]:
    rows=load(C/name);assert len(rows)==count
    for e in rows:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
frozen=load(A/'frozen-file-bindings.json');assert isinstance(frozen,list) and len(frozen)==184
for e in frozen:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
native_path=K/'P16.4-round214-exact-native-model-final-whole-stability279-local-audit-20261008.json'
n=load(native_path);saved=load(A/'native-notes.json');registered=x['campaign']['result']
assert n!=saved and not n['candidate'] and not saved['candidate'] and not registered['candidate']
ids=set();differences=[]
for p,q,s in zip(n['notes'],registered['notes'],saved['notes']):
    assert all(v in ids for v in p['support']);ids.add(p['id'])
    assert all(p[k]==q[k] for k in ['id','summary','detailedSummary','support'])
    assert q['text']==p['text']+'\n\nArtifacts: '+str(A)
    differences.append(dict(id=p['id'],different_saved_fields=[k for k in p if p[k]!=s[k]],saved_draft_not_exact_FINAL=True))
assert len(ids)==4
report=load(A/'audit-report.json');apps=load(A/'source-application-audit.json');prem=load(A/'premise-coverage.json');units=load(A/'proof-unit-coverage.json');history=load(A/'historical-evidence-audit.json')
assert report['verdict']==report['mathematical_reconstruction_verdict']==apps['verdict']=='PASS'
assert report['original_P16_4_status']=='OPEN' and not report['candidate'] and not report['automatic_acceptance'] and not report['proof_modified']
assert report['decisive_reasoning']==[{k:p[k] for k in ['id','text','support']} for p in saved['notes']]
assert report['premise_coverage']['grants']==prem['grants']==apps['grants'] and len(apps['grants'])==9
assert report['premise_coverage']['ordinary_foundations']==prem['ordinary_premises']==apps['ordinary_foundations']
assert report['premise_coverage']['essential']==prem['analytic_grants_used']==['O217','M257']
assert report['whole_proof_coverage']==units and units['named_units']==5 and len(units['numbered_equations'])==15 and len(units['proof_and_unnumbered_units'])==64 and units['explicit_unnumbered_claim_count']==41
assert report['source_applications']['granted']==apps['essential_granted_applications'] and len(apps['essential_granted_applications'])==10
assert report['source_applications']['primary']==apps['ordinary_primary_applications'] and len(apps['ordinary_primary_applications'])==4
assert report['historical_execution_sector']['evidence']==history
primary_units=[]
for e in apps['ordinary_primary_applications']:
    assert sha(e['source_binding']['path'])==e['source_binding']['sha256']
    assert sha(e['original_pdf_binding']['path'])==e['original_pdf_binding']['sha256']
    assert sha(e['LOCALONLY_artifact'])==e['LOCALONLY_sha256']
    primary_units.append({k:e[k] for k in ['id','source_binding','original_pdf_binding','source_units','exact_immediate_literal_LF','exact_application_and_hypotheses','recursive_boundary']})
rep=load(D/'root-reproduction-binding-20261007.json')
for key in ['source','argument','pdf']:assert sha(rep[key])==rep[key+'_sha256']
assert rep['finite_reproduction_exact'] and rep['markdown_to_tex_exact'] and rep['local_build_exit_codes']==[0,0] and not rep['local_diagnostics']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
binding=K/'P16.4-round214-whole-stability279-local-source-audit-and-ROOT-mathematical-binding-20261008.json'
accept=D/'whole-mathematical-paper-acceptance-after-audit214-20261008.json';clar=D/'harmless-reader-clarifications-after-audit214-20261008.json'
assert not any(p.exists() for p in [binding,accept,clar])
for name in ['active-work.json','checklist-current.json']:
    j=load(R/name);assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==80 and j['github_pending_checkpoint'] is None
S.mkdir();shutil.copyfile(A/'independent_coefficients.py',S/'independent_coefficients.py')
run=subprocess.run(['python','independent_coefficients.py'],cwd=S,capture_output=True,text=True)
assert run.returncode==0
for name in ['inputs.json','outputs.json']:
    assert (S/'reproduction/independent-coefficients'/name).read_bytes()==(A/'reproduction/independent-coefficients'/name).read_bytes()
E.mkdir(parents=True)
for name in ['audit-report.json','source-application-audit.json','frozen-file-bindings.json','premise-coverage.json','proof-unit-coverage.json','historical-evidence-audit.json','native-notes.json','independent_coefficients.py','read-events.jsonl','environment.json','validation-output.json']:
    shutil.copyfile(A/name,E/name)
for src in (A/'reproduction').rglob('*'):
    if src.is_file() and src.suffix in ['.py','.json','.txt','.stdout','.stderr']:
        dst=E/'native-reproduction'/src.relative_to(A/'reproduction');dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
shutil.copyfile(native_path,E/'exact-native-final.json');write(E/'registered-native-worker-result.json',registered)
for name in ['inputs.json','outputs.json']:shutil.copyfile(S/'reproduction/independent-coefficients'/name,E/('ROOT-independent-coefficients-'+name))
(E/'ROOT-independent-checker.stdout.txt').write_text(run.stdout);(E/'ROOT-independent-checker.stderr.txt').write_text(run.stderr)
now=datetime.now(timezone.utc).isoformat()
scope='ENTIRE unchanged279 mathematical sector, actual original complete characteristic/residue-characteristic-zero fields, all smooth geometrically integral projective ample rational bundles and n>=2: signed nonordered singular Dirichlet/real-PL stability, exact all-n energy-defect coefficients and mixed-measure fibre rigidity, known-output dual stability, canonical intrinsic Radon weak output limits for ALL maximizing nets and mixed tuples, selected-reference finite-U quantitative energy/test bounds, reference covariance and competitor-only Euler equivalence. Exactly nine whole caller grants/all clarifications, O/M only analytic premises; ordinary recursive foundations explicitly retained.'
gaps='Original P16.4 remains OPEN: actual E1 maximizing-potential attainment, lambda_mu=mu for every intrinsic target, and every-solution/every-point uniqueness modulo one finite constant including poles. Measure limits and zero-defect measure equivalence do not prove these.'
b=dict(recorded_utc=now,round=214,continuation=279,atom='P16.4',native_whole_mathematical_verdict='PASS',ROOT_mathematical_verdict='PASS',canonical_xean_review_role=False,automatic_acceptance=False,operation_id=req['operationId'],model=req['model'],reasoning=req['reasoning'],native_final=str(native_path),native_final_sha256=sha(native_path),registered_suffix_only=True,four_exact_FINAL_and_four_saved_draft_notes_ROOT_read=True,saved_draft_note_differences=differences,master_report_full_unique_contents_ROOT_read=True,repeated_master_sections_exactly_bound_to_entire_ROOT_read_separate_reports=True,whole_5_results_15_equations_64_units_41_unnumbered_claims_9_grants_4_foundations_10_granted_4_original_applications_ROOT_read=True,all31_math87_historical62_primary_and184_auditor_inventory_byte_bindings_match=True,whole_62_primaries_ROOT_read_claimed=False,whole_original_BE_units_ROOT_read_prior_turn_and_additional_LF2282_2332_THISturn=True,primary_units=primary_units,recursive_foundations_not_all_freshly_reconstructed=True,ROOT_read_independent_checker_before_own_copy_execution=True,ROOT_independent528_coefficients_exact_reproduction=True,finite_execution_not_continuum_proof=True,prior136_coefficients1089_formal_tuples_exact_conversion_and_local_build_reproduction_retained=True,source_preserved=True,whole_mathematical_sector_accepted=True,historical_execution_sector=report['historical_execution_sector']['assessment'],universal_historical_negative_operations_certified=False,first_ROOT_pass_had_rerun_warning=True,final_ROOT_pass_clean=True,accepted_scope=scope,residual_original_scope=gaps,original_closed=False,protected_editor_unchanged_open=True,no_new_tab=True,no_hot_feedback=True)
write(binding,b)
a=dict(recorded_utc=now,atom='P16.4',continuation=279,grant_label='S279',independent_native_audit_round=214,native_mathematical_verdict='PASS',ROOT_mathematical_verdict='PASS',canonical_xean_review_role=False,automatic_acceptance=False,cumulative_accepted_paper_number=81,source=rep['source'],source_sha256=rep['source_sha256'],source_LF_lines=588,argument=rep['argument'],argument_sha256=rep['argument_sha256'],pdf=rep['pdf'],pdf_sha256=rep['pdf_sha256'],pdf_pages=9,review_binding=str(binding),review_binding_sha256=sha(binding),accepted_scope=scope,only_caller_grants=f['only_grants'],all_clarifications_retained=True,exact_reviewed_source_preserved=True,builtin_compiler_success_claimed=False,builtin_request_cell_id='204',root_visual_pages_read=[1,4,6,9],all9_pdf_pages_visually_ROOT_read=False,originals_solved=9,originals_open=33,original_closed=False,residual_original_scope=gaps,protected_editor_unchanged_open=True)
write(accept,a)
write(clar,dict(recorded_utc=now,source_sha256=rep['source_sha256'],exact_reviewed_source_preserved=True,substantial_mathematical_repair=False,clarifications=['Two successful ROOT local passes with a clean FINAL build; first fresh pass has a cross-reference rerun warning, so both are not individually warning-free.','Initial pandoc returned zero but made unusable TeX; first TeX pass returned one. Intermediate overfull warnings and eventual clean final build are retained.','Auditor214 saved four-note draft differs from actual FINAL; both are preserved and ROOT-read. Master report decisive reasoning matches the saved draft, while registered text matches exact FINAL plus its Artifacts suffix. No substitution is made.','Absent child-visible backend-selection service is a visibility limit; operator native Xean invocation was verified separately. Historical universal no-operation assertions are not mathematical premises.','Zero I is measure rigidity only; lambda=target holds only after an actual known solution. All three original higher-dimensional gaps stay open.'],all_prior_caller_clarifications_preserved=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=load(p);j.update(updated_utc=now,historical_reviewed_scoped_papers=81,P16_4_accepted_stability279_after214=a,goal_state='9/42 original problems solved;33 open;81 accepted scoped/supporting mathematical papers. S279 higher-dimensional stability and maximizing-output limits accepted; original high-dimensional equation remains open.',next_work='Continue independent215 whole unchanged282 audit; select next original continuation in at most one additional61xhigh campaign after reading its exact full original scope. NewS279 is a whole accepted premise only in its scope/allclarifications. Full P16.4 still needs actual inverse/attainment/everypoint uniqueness; fullP05.2 general singular domain/contact/structural classification stays open. Regular verified pushes and no private ACTIVE reads/hotfeedback.')
    if name=='checklist-current.json':
        for target in j['targets']:
            if target['id']=='P16.4':
                assert not target['fully_solved'] and target['closure']=='open'
                target.update(research_status='all_genus_curves_and_higher_dimensional_stability_accepted_general_equation_open',current_focus='Whole279 accepted after independent214 and ROOT mathematical/source/evidence audit. General equation inverse, actual potential attainment and every-point uniqueness remain OPEN.')
    write(p,j)
table=R/'checklist-current.tsv'
with table.open(newline='') as fh:reader=csv.DictReader(fh,delimiter='\t');columns=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['ID']=='P16.4':row['Research']='all_genus_curves_and_higher_dimensional_stability_accepted_general_equation_open'
with table.open('w',newline='') as fh:writer=csv.DictWriter(fh,fieldnames=columns,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
print(json.dumps(dict(accepted_supporting_paper=81,continuation=279,native_mathematical_verdict='PASS',ROOT_mathematical_verdict='PASS',acceptance_sha256=sha(accept),review_binding_sha256=sha(binding),originals_solved=9,originals_open=33,independent_checker_exit=run.returncode),indent=2))
