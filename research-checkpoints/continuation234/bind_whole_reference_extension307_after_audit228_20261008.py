from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research'); K=R/'root-checks'
D=K/'public-P05.1-continuation307-compatible-affine-reference-extension-and-sharp-global-restriction-distance'
C=R/'campaigns/round-228/P05.1-compatible-affine-reference-extension-and-sharp-distance-independent-whole-source-audit'
A=C/'artifacts/codex-7kEr2u'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,j:Path(p).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
rep=json.loads((D/'ROOT-reproduction-binding-20261008.json').read_text())
assert sha(D/'P05.1-paper.tex')==rep['source_sha256']=='258fac9a3a5e9eb7e0cb6419653ac8239cdf6fe5d389da08226eef2e5462ed61'
assert sha(D/'P05.1-paper.pdf')==rep['ROOT_pdf_sha256'] and rep['ROOT_pdf_pages']==16
assert rep['copied_safe_checker_executions']==1 and rep['exact_author_output_match'] and rep['independent_source_body_to_Markdown_transformation_exact'] and rep['final_pass_warnings']==[]
actual=K/'round228-actual-native-final.json'; final=json.loads(actual.read_text())
assert sha(actual)=='13caadeeef9e93a90543cae849d2a62310d2bad23669a82cd8dc7b650289123b' and not final['candidate'] and len(final['notes'])==4
for filename,count in [('mathematical-packet-bindings.json',9),('historical-own-evidence-bindings.json',51),('private-primary-packet-bindings.json',4)]:
    rows=json.loads((C/filename).read_text()); assert len(rows)==count
    for e in rows: assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
own=json.loads((A/'artifact-bindings.json').read_text())['files']; assert len(own)==134
for e in own:
    p=A/e['path']; assert p.is_relative_to(A) and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
ar=json.loads((A/'fresh-build/build-report.json').read_text())
assert [e['exit_code'] for e in ar['passes']]==[0,0] and ar['passes'][-1]['warnings']==[] and ar['pages']==16
assert ar['source_sha256_before']==ar['source_sha256_after']==ar['immutable_source_sha256_after']==rep['source_sha256']
assert sha(A/'fresh-build/build/P05.1-paper.pdf')==ar['pdf_sha256']
assert (A/'fresh-build/P05.1-paper.tex').read_bytes()==(D/'P05.1-paper.tex').read_bytes()
fr=json.loads((A/'finite-check-report.json').read_text()); pr=json.loads((A/'presentation-and-FINAL-report.json').read_text())
assert fr['executions_this_audit']==1 and fr['exit_code']==0 and fr['total_assertions']==1577 and fr['diagnostic_cost']=='-1/4'
assert fr['output_exact_ROOT'] and fr['output_exact_author'] and fr['stdout_exact_ROOT'] and fr['stdout_exact_author']
assert sha(A/'finite-check/exact-output.json')==fr['output_sha256']=='7de3cbcf63f782f96d9ee946cf7c52c1408263b8bf2f79973f654f71e26d1e3a'
assert pr['exact_markdown_match'] and pr['exact_ROOT_markdown_match'] and pr['source_unchanged']
assert sha(A/'own-derived-argument.md')==rep['argument_sha256']==pr['output_sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
sourcefix=D/'source-metadata-qualifications-after-audit228-20261008.json'
reader=D/'reader-qualifications-after-whole-audit228-20261008.json'
binding=K/'P05.1-round228-whole-reference-extension307-mathematical-source-binding-20261008.json'
accept=D/'whole-mathematical-paper-acceptance-after-audit228-20261008.json'
pub=D/'evidence/independent-local-audit228'
assert not any(p.exists() for p in [sourcefix,reader,binding,accept,pub])
write(sourcefix,dict(recorded_utc=now,source_sha256=rep['source_sha256'],source_unchanged=True,qualifications=[
 'Immutable source ledger LF75: BMPS886-894 is bounded-relative Definition3.14 and only the start of unused Lemma3.15, rather than a properness/positive-growth definition.',
 'Immutable source ledger LF76: BMPS1741-1746 is slope positivity-at-infinity Definition4.15. Divisor/PAPC positivity is Definition3.1 at691-695 in the already read689-847 unit. The complete independently reconstructed formulas are unchanged; the narrow descriptor metadata FAIL is harmless to essential current applications.',
 'BMPS literal cycle weights are rational; endpoints rational and PCC weights real. Real balancing and finite REAL matching are separately proved. BBGS real endpoints, negative Euclidean unit-normal concavity sign and primitive positive-convex tangent corrections retain distinct domains. General density is not imported.',
 'Full BBGS3.15 ends at literal LF670, distinct from3.12. Older S291 source/combined FAIL and historical INCONCLUSIVE records remain historical; current source PASS does not recertify old reading acts.'
 ],original_closed=False))
write(reader,dict(recorded_utc=now,source_sha256=rep['source_sha256'],source_unchanged=True,clarifications=[
 'Accepted whole scoped E/G/N/D mathematics: anisotropic entire-cell extension with explicit GLOBAL cell Lipschitz constant, whole affine-face trace and bounded identical supports preserved ONLY on actual tau; actual AFFINE proper positive-recession reference extensions to dependent complete pages sharing exactly ONE pairwise H; and sharp GLOBAL original-restriction distance(A-1)/2, attained, for all finite continuous printed-PC full-book competitors.',
 'The legal independent-gluing PCC has cost-1/4. The sharp family target is already partial PC-PA and its original support is UNBALANCED. These obstruct exact/arbitrary-accuracy extension followed by restriction; they prove no original balanced regularization counterexample. Multiple overlaps, general nonlinear target extension, shared-face approximation and original P05.1/P05.2 remain OPEN.',
 'Common affine reference extension uses a single actual p0, ambient primal G, exact whole trace g>=ell_tau, page norms dominating BOTH h_G and ell_i, and page hulls above BOTH. It supplies common ambient supports at EVERY H point and rational spatial carriers with REAL heights; an arbitrary real affine maximum is not silently rational-carrier PA.',
 'Whole-affine majorants use the entire actual closed conjugate polytope including irrational boundary vertices, rational PRIMAL sample positions, exact recession and finite unshifted contacts. Rational shifts give strict dyadic descent but lose contacts and provide no synchronized face gluing. No MA is assigned to nonPA or failed intermediates.',
 'ROOT read all four actual auditor228 FINAL notes and the complete unique audit report, reconstructed proof33039bytes, source ledger9480, bounded evidence8472 and proof-coverageMD10515; coverage was reread after an outer exec aggregate output truncation. ROOT does not claim fresh whole semantic reading of all nine historical mathematical or51own-evidence bodies or large coverage/equation JSON from hashes alone; author225/ROOT307 earlier whole source readings remain their bounded records.',
 'ROOT and auditor independently inspected/copied/executed their safe checker ONCE in separate sessions,1577 finite assertions/-1/4. No checker/build repeated for acceptance. Two no-shell unchanged ROOT/auditor builds finish clean16p and preserve first-pass warnings. SourceBODY -> Markdown excludes preamble/bibliography, exactly preserves literal anchor quote escapes; it is not Markdown -> TeX/Pandoc. ROOT previous anchor comparison failure and presentation-only repair are preserved.',
 '64 frozen/134 own artifact identities verified. Native225 actual43398bytes equals its saved bytes minus oneLF; auditor228 controlling actualFINAL33197bytes is bound separately and no nonexistent auditor saved-notes equality is assumed. Historical author98/36 verification, read70records/66unique pairs, source/PDF pixel claims and universal operations are not newly certified. One current ROOT historical-log metadata display also truncated; compact inventory repaired counts/identities only, not full historical semantic reading.',
 'Narrow source-descriptor metadata FAIL remains separate from mathematical/essential-source PASS. Universal past operations, did-read truth, provider/model/single-call certification stay INCONCLUSIVE. Builtin81 pending is unverified; protected editor remains unchanged/open. This is ordinary independent mathematical review, not canonical automatic acceptance.',
 'This accepts supporting paper87 as S307 WITH BOTH annotations. Exactly nine original atoms remain solved and33open; no original closure is asserted.'
 ],original_closed=False))
pub.mkdir(); copies=[]
for e in own:
    name=e['path']
    if e['local_only'] or name.endswith(('.pdf','.aux','.out','.toc')) or name.startswith(('decoded-math-','fresh-build/build/')) or name in ['input.json','input-bindings.json','own-derived-argument.md','fresh-build/P05.1-paper.tex']: continue
    dst=pub/name; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(A/name,dst); copies.append(e)
for p in [A/'artifact-bindings.json',actual,K/'round228-registered-native-result.json',K/'round228-actual-final-extraction-binding-20261008.json']: shutil.copyfile(p,pub/p.name)
write(pub/'ROOT-publication-binding.json',dict(recorded_utc=now,all134_own_bindings_verified=True,copied_safe_own_files=copies,third_party_full_sources_not_copied=True,supplied_programs_not_executed=True,actual_FINAL_controlling=True,original_closed=False))
write(binding,dict(recorded_utc=now,continuation=307,source_sha256=rep['source_sha256'],ROOT_pdf_sha256=rep['ROOT_pdf_sha256'],pages=16,native_round=228,native_mathematical_verdict='PASS entire scoped paper',native_essential_source_verdict='PASS',source_descriptor_metadata_verdict='FAIL narrowly and harmlessly, corrected by mandatory annotation',native_bounded_evidence_verdict='PASS',universal_history='INCONCLUSIVE retained',ROOT_mathematical_verdict='PASS WHOLE scoped mathematics WITH BOTH annotations',actual_native_FINAL_sha256=sha(actual),all4_auditor_actual_FINAL_ROOT_physically_read=True,whole_unique_audit_proof_source_evidence_and_coverage_MD_ROOT_physically_read=True,frozen_bindings_verified=64,own_bindings_verified=134,source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),source_unchanged=True,no_checker_or_build_repeated_for_acceptance=True,ordinary_native_audit_not_canonical_review=True,original_closed=False,protected_editor_unchanged_open=True))
write(accept,dict(recorded_utc=now,grant_label='S307',cumulative_accepted_paper_number=87,continuation=307,mathematical_verdict='PASS WHOLE scoped mathematics with BOTH annotations',source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=rep['ROOT_pdf_sha256'],pages=16,review_binding=str(binding),review_binding_sha256=sha(binding),source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),both_annotations_required_on_import=True,scope='Exact cell/affine-face extension with explicit GLOBAL L; compatible actual-AFFINE reference extensions on dependent complete pages with ONE H; all-continuous-competitor sharp GLOBAL restriction distance(A-1)/2. No balanced original counterexample or all-face PA gluing.',automatic_acceptance=False,canonical_research_review=False,originals_solved=9,originals_open=33,original_closed=False,builtin_compiler_success_claimed=False))
for filename in ['active-work.json','checklist-current.json']:
    p=R/filename; j=json.loads(p.read_text()); assert j['historical_reviewed_scoped_papers']==86 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,historical_reviewed_scoped_papers=87,P05_1_accepted_reference_extension307_after228=json.loads(accept.read_text()))
    j['new307_unreviewed_paper'].update(new_accepted_paper=True,whole_scoped_math_accepted_after228=True,both_annotations_required=True)
    launch=R/'campaigns/round-229/P14.8-projective-line-arbitrary-formal-ideal-realization-independent-whole-audit/launch-record.json'
    j['prepared_P1_formal_ideal_audit229'].update(launched=True,launch_record=str(launch),launch_record_sha256=sha(launch))
    j['current_small_batch']['accepted_paper_number']=87; write(p,j)
p=R/'checklist-current.tsv'; lines=p.read_text().splitlines(); changed=0
for i,line in enumerate(lines):
    f=line.split('\t')
    if f[0]=='P05.1': assert f[1]=='open'; f[3]=str(int(f[3])+1); lines[i]='\t'.join(f); changed+=1
assert changed==1; p.write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(accepted_scoped_paper=87,grant='S307',originals_solved=9,originals_open=33,binding_sha256=sha(binding),acceptance_sha256=sha(accept)),indent=2))
