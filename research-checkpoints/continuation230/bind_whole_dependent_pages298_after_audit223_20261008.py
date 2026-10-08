from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research');K=R/'root-checks'
D=K/'public-P05.1-continuation298-dependent-common-subspace-pages-joint-dual-global-real-regularization'
C=R/'campaigns/round-223/P05.1-unchanged-dependent-common-subspace-pages-whole-independent-native-local-source-audit'
A=C/'artifacts/codex-i8oL7C'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
rep=json.loads((D/'root-reproduction-binding-20261008.json').read_text())
assert sha(D/'P05.1-paper.tex')==rep['source_sha256']=='738b023af49002450cac0a3df5aa2a62fc1a3e21ff750b2aa572cfb141647603'
assert sha(D/'argument.md')==rep['argument_sha256']=='e148bc1921900df673254f2ec04c10873509c66854612d70a791e2909f8bf9a0'
assert sha(D/'P05.1-paper.pdf')==rep['pdf_sha256']
assert all(rep[k] for k in ['ROOT_source_whole_read','ROOT_exact_FINAL_all7_whole_read','ROOT_safe_exact_checker_whole_read','ROOT_safe_checker_copied_and_exec_once','ROOT_finite_output_exact','latex_to_markdown_exact'])
assert rep['local_build_exit_codes']==[0,0,0] and rep['local_build_diagnostics'][-1]==[]
exact=K/'round223-actual-native-final.json';final=json.loads(exact.read_text());saved=json.loads((A/'native-notes.json').read_text())
assert sha(exact)=='bbea74bc48402335afe6ab10a62a8c82c99a54916c7acf298d1c7287f2c16037'
assert final['candidate'] is False and saved['candidate'] is False and len(final['notes'])==len(saved['notes'])==4
note_comparison=[]
for a,b in zip(final['notes'],saved['notes']):
    assert a['id']==b['id'] and a['support']==b['support']
    note_comparison.append(dict(id=a['id'],fields_equal={k:a[k]==b[k] for k in a},field_hashes={k:dict(actual=hashlib.sha256(json.dumps(a[k],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),saved=hashlib.sha256(json.dumps(b[k],ensure_ascii=False,sort_keys=True).encode()).hexdigest()) for k in a}))
assert all(not e['fields_equal']['text'] for e in note_comparison)
for name,count in [('mathematical-packet-bindings.json',33),('historical-own-evidence-bindings.json',122),('private-primary-packet-bindings.json',4)]:
    entries=json.loads((C/name).read_text());assert len(entries)==count
    for e in entries:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
own=json.loads((A/'artifact-bindings.json').read_text());assert len(own)==76
for e in own:assert sha(A/e['filename'])==e['sha256'] and (A/e['filename']).stat().st_size==e['bytes']
coverage=json.loads((A/'body-coverage.json').read_text());history=json.loads((A/'historical-body-coverage.json').read_text())
assert len(coverage)==33 and all(e['whole_display_assessed'] for e in coverage)
assert len(history)==122 and all(e['entire_bound_content_accounted'] for e in history)
rootproof=D/'evidence/ROOT-reproduction'
assert (A/'finite_check.py').read_bytes()==(rootproof/'check_exact.py').read_bytes()
assert (A/'exact-input.json').read_bytes()==(rootproof/'exact-input.json').read_bytes()
assert (A/'exact-output.json').read_bytes()==(rootproof/'exact-output.json').read_bytes()
assert (A/'P05.1-paper.tex').read_bytes()==(D/'P05.1-paper.tex').read_bytes()
assert (A/'argument.md').read_bytes()==(D/'argument.md').read_bytes()
ar=json.loads((A/'own-reproduction.json').read_text());assert ar['source_unchanged']
tex=[e for e in ar['commands'] if e['argv'][0]=='pdflatex' and '-no-shell-escape' in e['argv']]
assert len(tex)==3 and [e['returncode'] for e in tex]==[0,0,0] and tex[-1]['warning_lines']==[]
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
sourcefix=D/'harmless-source-metadata-corrections-after-audit223-20261008.json'
reader=D/'reader-qualifications-after-whole-audit223-20261008.json'
binding=K/'P05.1-round223-whole-dependent-pages298-mathematical-and-source-binding-20261008.json'
accept=D/'whole-mathematical-paper-acceptance-with-source-metadata-corrections-after-audit223-20261008.json'
pub=D/'evidence/independent-local-audit223'
assert not any(p.exists() for p in [sourcefix,reader,binding,accept,pub])
write(sourcefix,dict(recorded_utc=now,source_sha256=rep['source_sha256'],corrections=[dict(location='NEW298 source-application-ledger, BMPS literal LF1741-1748 adjacent unused unit',printed_metadata='Definition4.16',correct_metadata='Proposition4.16 at literal LF1747',essential_application=False,proof_changed=False),dict(location='Older S262/S272/S282 source-ledger references to whole BBGS3.15',printed_metadata='literal LF604-667 called whole proof',correct_metadata='whole proof ends at literal LF670; actual NEW298 and auditor whole unit LF604-704 includes ending',past_reader_omission_proven=False,proof_changed=False)],literal_LF_uses_split_newline_not_splitlines=True,source_and_native_outputs_unchanged=True,native_exhaustive_source_metadata_FAIL_retained=True,essential_source_application_PASS_retained=True,original_closed=False))
clarifications=[
 'ENTIRE unchanged493-LF18-page TeX and all7 controlling author221 FINAL were previously ROOT physically read, as were whole ledger/scope/coverage/execution and inspected safe finite code/input/output. Current ROOT separately read all4 controlling actual auditor223 FINAL and entire audit-report, independent-reconstruction, source-application-audit, whole-proof-coverage and historical-audit, with bounded complete displays. ROOT checked coverage inventory counts/flags and bindings; it does NOT claim a fresh whole read of all33 mathematical or122 historical bodies merely from flags/hashes. Auditor accounts for all bound bodies by the explicit whole canonical/alias/complete difference/PDF-text methods, not raw redisplay of every duplicate or PDF pixels.',
 'Exactly6 WHOLE grants A224/B225/R230/S262/S272/S282 with ALL qualifications are dependencies. Whole working293/294 including embedded289 are reconstructed DATA, not grants. S291/S292/295/296297 and other excluded native outcomes supplied no author/auditor premise. S282 regularity AND contact classification is not a regularity iff disjointness statement. Native210/native215 historical INCONCLUSIVE and author213 saved/actual discrepancy remain supplied historical DATA.',
 'Exact mathematical domain is a finite union of distinct COMPLETE rational equal-dimensional affine pages with EVERY pairwise intersection ONE rational affine H, including H=0 and dependent quotient directions; arbitrary actual positive REAL page weights and admitted actual REAL PA PC positive-growth reference. Several different overlaps, extra nonincident pages, general singular/glued/abstract categories and full literal classification are excluded. Whole-page convexity plus ONE ambient support at EVERY real H point is equivalent to continuous printed-PC on inherited/refined carriers. Shared trace alone is insufficient.',
 'Joint compact polyhedral dual fibers attain SAME ambient minimizers for ALL pages including boundary. Simultaneous dual lowering preserves all whole-trace fibers and common supports at EVERY real point. Exact whole unbounded rational-spatial REAL-PA trace is retained by appending ALL trace generators/recession, followed by rational ambient common refinement. Common dyadic shifts give GLOBAL strictly decreasing uniform convergence with actual recession unchanged; shifted contacts need not stay exact. Intermediate nonPA functions are unmeasured.',
 'ALL continuous bounded-relative PC functions and ALL C_b ACTUAL unrestricted envelopes are covered. R230 supplies actual envelope continuity FIRST; new construction proves genuine REAL-PA-PC domain SECOND; S272 completion applies THIRD. No broad raw printed-PC automatic continuity or irrational PA max closure is imported. Positive/signed/zero primitive recursion and every-dimensional saturated covolume conversion retain the exact source chain. General measure/Radon foundations remain whole qualified grants. Actual-reference common-jet/collar/roof negative contact uses effective balanced residual and SAME germ in ALL positive reference summands; nonPA contact classification excluded.',
 'Native223 scoped mathematics PASS and essential source applications PASS are preserved separately from exhaustive source-metadata FAIL and universal historical INCONCLUSIVE. BOTH source metadata corrections accompany whole mathematical acceptance. No evidence establishes past reader omission at BBGS667 or repairs a universal history assertion. Original-task body was not bound in223, only its freeze hash; task/input body was bound and read. Whole original closure is not claimed.',
 'ALL7 author221 saved prose differs from controlling FINAL in summary/detailedSummary/text, IDs/supports agree. Auditor independently read both whole versions. Prior ROOT oversized character-difference truncation was repaired ONLY by complete field-summary, no whole saved ROOT read. ALL4 auditor223 saved text likewise differs from actual FINAL; current ROOT read actual FINAL, saved summaries/details and complete field-equality/hash comparisons, not whole saved prose. Initial attempt to print auditor-saved full differences was oversized and TRUNCATED; the later compact field summary repairs identification only. No byte or semantic saved/FINAL identity claimed. Actual FINAL controls.',
 'ROOT safe checker was fully inspected/copied/executed ONCE earlier. Auditor identical code/input/output is verified without repeat execution:8vertices/35triples, legal -3/64,26961tuples,33tracepoints,44orders/6matrices are finite observations, not continuum proof. ROOT and auditor separate three-pass no-shell builds0/0/0 preserve first warnings and finish clean18p; author initial and later extra clean rerun remain distinct. Source-to-nonstandalone Markdown is exact. Pending builtin cell217 is no compiler result; no duplicate/newtab/protected editor modification. Supplied auditor emitters/builders/binders/orchestrators were not executed.',
 'This is explicit ROOT acceptance of WHOLE scoped mathematics with source metadata annotations, cumulative supporting paper85, not automatic/canonical acceptance and not an original solution. Original P05.1/P05.2 and33 remaining originals stay OPEN. Direct all-face gluing/general classification remains unresolved; future results must prove compatibility on their actual original support.'
]
write(reader,dict(recorded_utc=now,source_sha256=rep['source_sha256'],clarifications=clarifications,source_and_native_outputs_unchanged=True,original_closed=False))
pub.mkdir();copied=[]
for e in own:
    name=e['filename']
    if 'LOCALONLY' in name or name.endswith(('.pdf','.aux','.out','.toc')) or name.startswith('historical-pdf-text-') or name in ['P05.1-paper.tex','argument.md']:continue
    dest=pub/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(A/name,dest);copied.append(dict(path=name,bytes=e['bytes'],sha256=e['sha256']))
for p in [A/'artifact-bindings.json',exact,K/'round223-registered-native-result.json',K/'round223-actual-final-extraction-binding-20261008.json']:
    assert p.is_file();shutil.copy2(p,pub/p.name)
write(pub/'ROOT-publication-binding.json',dict(recorded_utc=now,original_directory=str(A),all76_own_bindings_verified=True,copied_safe_files=copied,original_long_excerpts_LOCALONLY_not_copied=True,duplicate_auditor_PDF_and_PDF_text_not_copied=True,supplied_programs_not_executed=True,actual_FINAL_controlling=True,original_closed=False))
b=dict(recorded_utc=now,original='P05.1',continuation=298,source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument_sha256=rep['argument_sha256'],pdf_sha256=rep['pdf_sha256'],pdf_pages=18,native_audit_round=223,native_role='ordinary local-source worker audit, NOT canonical review',native_mathematical_verdict='PASS scoped whole theorem',native_essential_source_applications='PASS',native_exhaustive_source_metadata='FAIL two metadata errors, retained',native_universal_retrospective_history='INCONCLUSIVE',ROOT_mathematical_verdict='PASS WHOLE scoped mathematics WITH BOTH metadata/reader annotations',actual_native_FINAL_sha256=sha(exact),all4_actual_auditor_FINAL_whole_ROOT_physically_read=True,all7_actual_author_FINAL_previously_whole_ROOT_physically_read=True,whole_unique_audit_reconstruction_source_coverage_history_reports_ROOT_read=True,all159_frozen_bindings_verified=True,all76_own_bindings_verified=True,auditor_saved_vs_actual_note_comparison=note_comparison,auditor_saved_whole_ROOT_read_claimed=False,initial_oversized_auditor_saved_diff_output_truncated=True,compact_complete_field_summary_repaired_identification_only=True,author_saved_whole_ROOT_read_not_claimed=True,auditor_all33_and122_assessed_report_retained=True,source_metadata_corrections=str(sourcefix),source_metadata_corrections_sha256=sha(sourcefix),reader_qualifications=str(reader),reader_qualifications_sha256=sha(reader),ROOT_safe_checker_previously_exec_once_auditor_same_code_input_output=True,no_repeat_checker_or_build=True,ROOT_and_auditor_distinct_no_shell_builds=[0,0,0],source_conversion_exact=True,finite_not_continuum_proof=True,source_unchanged=True,supplied_emitters_builders_binders_orchestration_not_executed=True,original_closed=False,protected_editor_unchanged_open=True)
write(binding,b)
scope='WHOLE unchanged493-LF18-page298 scoped mathematics: COMPLETE rational equal-d affine pages with ALL pairwise intersections ONE rational affine H of any dimension, arbitrary dependent quotient directions, actual positive REAL weights and admitted actual REAL PA PC positive-growth reference. Continuous PC iff whole-page convexity plus ONE ambient support at EVERY real H point on inherited/refined carriers. Joint compact dual boundary fibers, simultaneous minimizers/lowering, full rational-spatial REAL-height trace epigraph and genuine common carrier yield GLOBAL strictly decreasing uniform REAL-PA-PC regularization of ALL continuous relative-PC targets with exact actual recession. ALL C_b ACTUAL unrestricted envelope via R230 belongs to genuine domain BEFORE S272 MA. Full primitive signed/zero covolume/refinement/commutation/balance/positivity/mass/IBP and determinant2^d*d!; every crossing/actual reference negative contact with SAME germs/roof against unrestricted competitors under whole qualified S272/S282 premises. Exactly6wholegrants/allqualifications; source metadata errors separately corrected without changing source or native verdicts.'
write(accept,dict(recorded_utc=now,grant_label='S298',cumulative_accepted_paper_number=85,continuation=298,mathematical_verdict='PASS WHOLE scoped mathematics with metadata/reader annotations',accepted_mathematical_scope=scope,source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument=str(D/'argument.md'),argument_sha256=rep['argument_sha256'],pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=rep['pdf_sha256'],pdf_pages=18,review_binding=str(binding),review_binding_sha256=sha(binding),source_metadata_corrections=str(sourcefix),source_metadata_corrections_sha256=sha(sourcefix),reader_qualifications=str(reader),reader_qualifications_sha256=sha(reader),native_source_metadata_FAIL_and_history_INCONCLUSIVE_retained=True,both_annotations_required_on_import=True,automatic_acceptance=False,canonical_research_review=False,builtin_compiler_success_claimed=False,all_PDF_pages_visual_ROOT_read_claimed=False,originals_solved=9,originals_open=33,original_closed=False,residual_original_scope='Several different positive-dimensional overlaps, general singular supports and direct all-face approximation/full classification remain unresolved; P05.1/P05.2 OPEN.',protected_editor_unchanged_open=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==84 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,historical_reviewed_scoped_papers=85,P05_1_accepted_dependent_pages298_after223=json.loads(accept.read_text()))
    j['new298_unreviewed_paper'].update(new_accepted_paper=True,whole_scoped_math_accepted_after223=True,native_source_metadata_FAIL_and_history_INCONCLUSIVE_retained=True,both_annotations_required=True)
    j['current_small_batch']['accepted_paper_number']=85
    write(p,j)
p=R/'checklist-current.tsv';lines=p.read_text().splitlines();changed=0
for i,line in enumerate(lines):
    fields=line.split('\t')
    if fields[0]=='P05.1':assert fields[1]=='open';fields[3]=str(int(fields[3])+1);lines[i]='\t'.join(fields);changed+=1
assert changed==1;p.write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(accepted_whole_scoped_mathematical_paper=85,grant='S298',binding_sha256=sha(binding),acceptance_sha256=sha(accept),source_unchanged=True,native_source_metadata_FAIL_and_history_INCONCLUSIVE_retained=True,originals_solved=9,originals_open=33),indent=2))
