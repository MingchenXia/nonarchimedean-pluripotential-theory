from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research'); K=R/'root-checks'
D=K/'public-P05.1-continuation292-isolated-affine-crossings-global-real-regularization'
C=R/'campaigns/round-220/P05.1-unchanged-isolated-affine-crossings-whole-independent-native-local-source-audit'
A=C/'artifacts/codex-1hUbdP'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
rep=json.loads((D/'root-reproduction-binding-20261008.json').read_text())
assert sha(D/'P05.1-paper.tex')==rep['source_sha256']=='4ece9622c0d97a861dde051ec6a31c0bd0416781bd4c43c0b4aaa0f498ffe11c'
assert sha(D/'argument.md')==rep['argument_sha256']=='1fd6dcb5810cbb3163158543b2643266bfbb5e92748552a0357135f83fdaffbc'
assert rep['ROOT_source_whole_read'] and rep['ROOT_exact_FINAL_all6_whole_read'] and rep['ROOT_safe_exact_checker_whole_read'] and rep['ROOT_finite_output_exact']
assert rep['local_build_exit_codes']==[0,0] and rep['latex_to_markdown_exact'] and rep['initial_GFM_formatter_mismatch_failure_preserved']
exact=K/'round220-actual-native-final.json'; final=json.loads(exact.read_text())
assert final['candidate'] is False and len(final['notes'])==6
assert sha(exact)=='469a3cc961906962702f2e0092cbe51dbfd6ac95ae17d7b4fb2d83f7927040f6'
assert (A/'native-notes.json').read_bytes()==exact.read_bytes()+b'\n'
aliases=[]
for name in ['source-application-audit.md','audit-report.md','historical-evidence-audit.md']:
    remaining=(A/name).read_text(); matches=[]
    for note in final['notes']:
        for number, paragraph in enumerate(note['text'].split('\n\n')):
            if paragraph in remaining:
                remaining=remaining.replace(paragraph,'',1)
                matches.append(dict(note=note['id'],paragraph=number,sha256=hashlib.sha256(paragraph.encode()).hexdigest()))
    assert all(line.strip().startswith('#') for line in remaining.splitlines() if line.strip())
    aliases.append(dict(path=str(A/name),sha256=sha(A/name),exact_FINAL_paragraph_aliases=matches,whole_unique_remainder=remaining))
for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):
        assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for e in json.loads((A/'frozen-file-bindings.json').read_text()):
    assert e['matches'] and sha(e['path'])==e['sha256']==e['actual_sha256'] and Path(e['path']).stat().st_size==e['bytes']==e['actual_bytes']
own=json.loads((A/'artifact-bindings.json').read_text())['files'];assert len(own)==55
for e in own:assert sha(A/e['path'])==e['sha256'] and (A/e['path']).stat().st_size==e['bytes']
rootproof=D/'evidence/ROOT-reproduction'
assert (A/'own-reproduction/certificate-output.json').read_bytes()==(rootproof/'certificate-output.json').read_bytes()
assert (A/'own-reproduction/check_certificates.py').read_bytes()==(rootproof/'check_certificates.py').read_bytes()
assert (A/'own-reproduction/certificate-input.json').read_bytes()==(rootproof/'certificate-input.json').read_bytes()
repro=json.loads((A/'reproduction-evidence.json').read_text())
assert repro['finite_output_byte_equal'] and repro['markdown_byte_equal'] and repro['source_unchanged'] and repro['pdf_pages']==17 and repro['diagnostics'][-1]==[]
assert (A/'own-reproduction/argument.md').read_bytes()==(D/'argument.md').read_bytes()
now=datetime.now(timezone.utc).isoformat()
reader=D/'harmless-reader-clarifications-after-whole-audit220-20261008.json'
binding=K/'P05.1-round220-whole-isolated-crossings292-mathematical-and-source-binding-20261008.json'
accept=D/'whole-mathematical-paper-acceptance-after-audit220-20261008.json'
pub=D/'evidence/independent-local-audit220'
assert not any(p.exists() for p in [reader,binding,accept,pub])
clarifications=[
 'Entire unchanged454-LF17-page TeX, entire mathematical sector in the parallel source conversion, all6 controlling author217 FINAL, and all6 actual independent220 FINAL are assessed. The auditor saved JSON differs from its actual FINAL only by a terminal file newline. Its report bodies exactly repeat FINAL paragraphs; the complete remaining headings and the separate whole41-display/17-contiguous-unit premise coverage were read. Hashes/read logs do not prove mathematics.',
 'Source locator convention must be explicit: auditor220 read_primary.py uses Python splitlines(), which also splits PDF form-feed characters. Its labels LF actually count these extracted records. For the exact bound BBGS text, record390-410 corresponds to literal newline lines383-403 (Definitions2.14/2.15), record542-604 to533-594 (whole3.12), record615-682 to604-670 (whole3.15), and record687-716 to675-704 (whole3.18/3.19). ROOT freshly read all these complete contents and the literal-LF604-670 proof ending. The earlier whole291 literal-LF604-670 source correction remains correct. BMPS literal-LF418-443 contains whole2.18-2.20. Preserve native/source bodies and frozen packets; this clarification changes no proof and certifies no past reading act.',
 'Exactly5whole caller grants A224/B225/R230/S262/S272 with ALL qualifications; proposals287/288 remain reconstructed data, and newer S282/S291 are not added as premises. BMPS formal weights/cycles are rational; actual REAL/signed/zero primitive recursion and every-dimensional covolume conversion are independently reconstructed using the separate BBGS domain and its whole commutation/refinement/balance chain. No delegated AR10, broad printed-PC continuity or unproved density/source equivalence is imported.',
 'Actual domain: finitely many COMPLETE rational equal-dimensional affine planes, pairwise empty or singleton intersection, arbitrary positive REAL weights and admitted actual REAL PC positive-growth reference. Branch convexity plus one common ambient support at each isolated meeting is equivalent to continuous PC on EVERY inherited/refined rational carrier. Shared values alone fail for dependent branches. All finite prescribed rational contacts are retained by unshifted above-majorants; the common dyadic shift then gives GLOBAL decreasing convergence, not retained exact contact with the target.',
 'The ACTUAL envelope over every raw finite-valued printed-PC relative upper-bounded competitor is supplied by R230 for ALL continuous bounded obstacles. It enters the genuine uniform relative REAL-PA-PC domain through the new construction BEFORE any completed MA is applied. The discontinuous rational-zero/irrational-minus-one example is not claimed regular. Literal-excluded endpoints receive no MA. Optional S272 moment/common-mass/global-vague/ordinary-weak-net/fixed-C-only weak-BL qualifications persist.',
 'Every crossing has an actual-reference finite-PA negative contact witness; unrestricted roof equality is proved for even discontinuous raw competitors BEFORE measuring. The saturated coefficient formula is unit branch weight, multiplied by the actual weight. The harmless literal qquad separator remains unchanged. Finite5matrix13permutation40word27repeat-zero checks and mesh checks are observations, not continuum certificates. ROOT initial wrong-GFM failure is preserved; correct standalone Markdown is exact, two local builds return0/0, first reference warnings remain and final diagnostics are clean17pages. Builtin cell94 remains pending, no success or duplicate request claimed.',
 'Native220 mathematical/source PASS and required reproduction PASS are retained as independent draft verdicts. Retrospective universal did-read/no-operation assertions remain INCONCLUSIVE. ROOT whole mathematical acceptance is separate from native/canonical acceptance and original closure. Positive-dimensional overlaps, arbitrary general singular supports/nonseparable products, broader abstract compact structures, full literal classification, and non-PA contact sufficiency remain unresolved; original P05.1/P05.2 stay OPEN.'
]
write(reader,dict(recorded_utc=now,source_sha256=rep['source_sha256'],clarifications=clarifications,source_and_native_outputs_unchanged=True,locator_record_count_distinguished_from_literal_LF=True,original_closed=False))
pub.mkdir()
copied=[]
for e in own:
    if e.get('distribution')=='LOCALONLY' or e['path'].startswith('LOCALONLY/') or e['path'].endswith('.pdf'):continue
    dest=pub/e['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(A/e['path'],dest)
    copied.append(dict(path=e['path'],bytes=e['bytes'],sha256=e['sha256']))
for p in [A/'artifact-bindings.json',A/'artifact-bindings.sha256',exact,K/'round220-registered-native-result.json',K/'round220-actual-final-extraction-binding-20261008.json']:
    shutil.copy2(p,pub/p.name)
write(pub/'ROOT-publication-binding.json',dict(recorded_utc=now,original_directory=str(A),all55_own_identities_verified=True,copied_safe_files=copied,LOCALONLY_original_excerpts_not_copied=True,duplicate_auditor_PDF_not_copied=True,supplied_programs_not_executed=True,actual_FINAL_controlling=True,original_closed=False))
b=dict(recorded_utc=now,original='P05.1',continuation=292,source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument_sha256=rep['argument_sha256'],pdf_sha256=rep['pdf_sha256'],pdf_pages=17,native_audit_round=220,native_role='ordinary worker local-source audit, NOT canonical research review',native_mathematical_verdict='PASS',native_source_application_verdict='PASS with explicit record-index/literal-LF locator clarification',native_concrete_historical_reproduction='PASS',native_universal_retrospective_history='INCONCLUSIVE',ROOT_mathematical_verdict='PASS whole scoped sector',actual_native_FINAL_sha256=sha(exact),all6_actual_FINAL_whole_ROOT_read=True,all6_saved_notes_equivalent_except_terminal_file_newline=True,whole_source_history_report_unique_contents_ROOT_read=True,exact_report_paragraph_alias_bindings=aliases,whole_coverage17_units41_displays_ROOT_read=True,all93_frozen_bindings_verified=True,all55_own_artifact_bindings_verified=True,reader_clarifications=str(reader),reader_clarifications_sha256=sha(reader),immediate_BBGS_named_whole_units_and_BMPS_formal_definitions_ROOT_freshly_read=True,primary_other_immediate_units_previously_ROOT_read=True,whole_primary_PDF_ROOT_read_not_claimed=True,ROOT_prior_safe_checker_exec_once_and_auditor_same_code_input_output_exact=True,whole_finite_output_ROOT_read=True,finite_not_continuum_proof=True,ROOT_local_two_passes=[0,0],source_conversion_exact=True,initial_formatter_failure_preserved=True,supplied_auditor_emitters_builders_binders_orchestration_not_executed=True,source_unchanged=True,original_closed=False,protected_editor_unchanged_open=True)
write(binding,b)
scope='ENTIRE unchanged454-LF17-page292 scoped mathematics: finite unions of complete rational equal-dimensional affine planes with pairwise empty or singleton intersections, including arbitrarily dependent branches and multiple distinct meetings, arbitrary actual positive REAL weights and REAL PC positive-growth reference. Continuous PC iff branch convexity plus common ambient supports at each meeting on ALL inherited/refined carriers. Full-affine global above-majorants with rational spatial/REAL lifted geometry, whole-boundary compact-dual continuity, exact actual recession and ANY finite rational contacts yield finite-carrier glued GLOBAL decreasing genuine REAL-PA-PC regularization of ALL continuous relative-PC functions and ALL-C_b ACTUAL envelopes BEFORE S272 MA. Full signed/zero primitive recursion, every-dimensional saturated covolume/refinement/commutation/balance/positivity/mass/IBP, determinant2^d*d! atoms and dependent diagnostics reconstructed. EVERY crossing/every actual reference has finite-PA common-jet/collar/roof negative-contact witness with unrestricted raw competitors. EXACT5whole grants/allqualifications; scope and topology limits retained.'
write(accept,dict(recorded_utc=now,grant_label='S292',cumulative_accepted_paper_number=84,continuation=292,mathematical_verdict='PASS whole scoped sector',accepted_mathematical_scope=scope,source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument=str(D/'argument.md'),argument_sha256=rep['argument_sha256'],pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=rep['pdf_sha256'],pdf_pages=17,review_binding=str(binding),review_binding_sha256=sha(binding),reader_clarifications=str(reader),reader_clarifications_sha256=sha(reader),native_universal_history_INCONCLUSIVE_retained=True,automatic_acceptance=False,canonical_research_review=False,builtin_compiler_success_claimed=False,all_PDF_pages_visual_ROOT_read_claimed=False,originals_solved=9,originals_open=33,original_closed=False,residual_original_scope='General positive-dimensional overlaps and singular supports, nonseparable product obstacles, broader abstract compact/literal categories and full classification remain unresolved; P05.1/P05.2 OPEN.',protected_editor_unchanged_open=True))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers']==83 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,historical_reviewed_scoped_papers=84,P05_1_accepted_isolated_crossings292_after220=json.loads(accept.read_text()))
    j['new292_unreviewed_paper'].update(new_accepted_paper=True,whole_scoped_math_accepted_after220=True,whole_independent_audit_ROOT_checked=True,native_universal_history_INCONCLUSIVE_retained=True)
    j['prepared_whole295_audit222'].update(launched=True,launch_record=str(R/'campaigns/round-222/P05.1-unchanged-independent-common-subspace-pages-whole-native-local-source-audit/launch-record.json'))
    j['current_small_batch']['accepted_paper_number']=84
    write(p,j)
p=R/'checklist-current.tsv';lines=p.read_text().splitlines();changed=0
for i,line in enumerate(lines):
    fields=line.split('\t')
    if fields[0]=='P05.1':
        assert fields[1]=='open';fields[3]=str(int(fields[3])+1);lines[i]='\t'.join(fields);changed+=1
assert changed==1;p.write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(accepted_whole_mathematical_paper=84,grant='S292',binding_sha256=sha(binding),acceptance_sha256=sha(accept),source_unchanged=True,native_universal_history_INCONCLUSIVE_retained=True,originals_solved=9,originals_open=33),indent=2))
