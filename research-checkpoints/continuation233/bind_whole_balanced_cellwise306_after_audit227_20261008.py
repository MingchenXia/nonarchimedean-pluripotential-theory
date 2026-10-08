from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil

R=Path('/workspace/research');K=R/'root-checks'
D=K/'public-P05.1-continuation306-balanced-cellwise-Lipschitz-and-single-cell-real-regularization'
C=R/'campaigns/round-227/P05.1-balanced-cellwise-Lipschitz-and-single-cell-real-majorants-independent-whole-source-audit'
A=C/'artifacts/codex-zqyqgO'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,j:Path(p).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
rep=json.loads((D/'ROOT-reproduction-binding-20261008.json').read_text())
assert sha(D/'P05.1-paper.tex')==rep['source_sha256']=='121e25eeb7b89371cc89d54c1bce1b4f1037be9d4a6e38e037c45d8041fec737'
assert sha(D/'P05.1-paper.pdf')==rep['ROOT_pdf_sha256'] and rep['ROOT_pdf_pages']==18
assert all(rep[k] for k in ['all_six_actual_FINAL_notes_physically_ROOT_read','entire_authoritative_TeX_physically_ROOT_read','entire_source_ledger_and_scope_physically_ROOT_read','copied_safe_checker_and_input_physically_ROOT_read_before_execution','finite_checks_exact_author_match','exact_original_Markdown_to_TeX_reproduced'])
assert rep['safe_checker_executions']==1 and rep['final_pass_warnings']==[]
actual=K/'round227-actual-native-final.json';final=json.loads(actual.read_text());saved=json.loads((A/'notes.json').read_text())
assert sha(actual)=='2e2b5250a7d68b16e1adaa672dcdabb4670c7ebb61d36e0a7b87271f1ccb4ad8'
assert not final['candidate'] and len(final['notes'])==len(saved['notes'])==6
comparison=[]
for x,y in zip(final['notes'],saved['notes']):
    assert x['id']==y['id'] and x['support']==y['support']
    comparison.append(dict(id=x['id'],equal_fields=[k for k in x if x[k]==y.get(k)],differing_fields=[k for k in x if x[k]!=y.get(k)]))
for filename,count in [('mathematical-packet-bindings.json',33),('historical-own-evidence-bindings.json',98),('private-primary-packet-bindings.json',4)]:
    rows=json.loads((C/filename).read_text());assert len(rows)==count
    for e in rows:assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
own=json.loads((A/'own-artifact-hashes.json').read_text())['artifacts'];assert len(own)==61
for e in own:
    p=A/e['filename'];assert p.is_relative_to(A) and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
ar=json.loads((A/'reproduction-report.json').read_text())
assert ar['checker_executions']==1 and ar['checker_exact_ROOT_output'] and ar['exact_Markdown_to_TeX'] and ar['TeX_sha256']==rep['source_sha256']
assert [e['exit_code'] for e in ar['build']]==[0,0,0] and ar['build'][-1]['warnings']==[]
assert sha(A/'reproduction/build/P05.1-paper.pdf')==ar['PDF_sha256']
assert (A/'reproduction/generated-paper.tex').read_bytes()==(D/'P05.1-paper.tex').read_bytes()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
sourcefix=D/'source-and-presentation-qualifications-after-audit227-20261008.json'
reader=D/'reader-qualifications-after-whole-audit227-20261008.json'
binding=K/'P05.1-round227-whole-balanced-cellwise306-mathematical-source-binding-20261008.json'
accept=D/'whole-mathematical-paper-acceptance-after-audit227-20261008.json'
pub=D/'evidence/independent-local-audit227'
assert not any(p.exists() for p in [sourcefix,reader,binding,accept,pub])
write(sourcefix,dict(recorded_utc=now,source_sha256=rep['source_sha256'],source_unchanged=True,qualifications=[
 'The abstract word polyhedrally-concave is a presentation error: the printed inequalities, theorem and complete proof use convexity/printed-PC. Read the abstract subject to those exact definitions; no sign-reversed theorem is accepted.',
 'The unchanged paper uses MAXIMUM facet violation. The audit task also requested SUM. The independent reconstruction proves both; only the maximum is part of the unchanged source, and the sum is an additional audit observation.',
 'Auditor source ledger calls 3209/2420 literal LF bytes; these are newline CHARACTER COUNTS in the complete BMPS/BBGS text, not total file sizes. Total sizes are231317/148757bytes. Literal LF split preserves form feeds.',
 'BMPS formal weights are rational; actual positive REAL extension is separately proved. BBGS signed/zero REAL product uses negative unit-normal derivative, with -f and EVERY-dimensional saturated covolumes converting to the primitive positive convention.',
 'Full BBGS3.15 ends at literal LF670. Old604-667 locators and original S291 source/combined FAIL, historical INCONCLUSIVE remain unchanged. Essential current source applications PASS does not certify those old reading acts.'
 ],original_closed=False))
write(reader,dict(recorded_utc=now,source_sha256=rep['source_sha256'],source_unchanged=True,clarifications=[
 'Accepted WHOLE scoped mathematics: finite pure globally EMBEDDED rational complex including ALL closed faces, actual strictly positive REAL top weights balanced at every codimension-one face, fixed refinement carrying continuous actual real CELLWISE AFFINE gamma, continuous finite printed-PC f with |f-gamma|<=C. Gamma need not PC, proper or positive-growth for the Lipschitz theorem. Constants depend on finite geometry and gradient boundG; cellwise norm <=A_X C+B_X G. Incident ambient supports hold on ENTIRE closed incident cells. Intrinsic polygonal path bound does not imply ambient distance control between nonincident components.',
 'Single-cell majorants require an explicit global cell Lipschitz constant and actual affine reference with strictly positive recession on that cell. Whole actual closed conjugate polytope, rational SPATIAL carriers with REAL heights, exact recession and unshifted finite contacts are essential. Dyadic shifts decrease strictly but lose exact contacts. NonPA extensions/intermediates receive no MA.',
 'UNBALANCED orthant diagnostic has exact REAL-PA error floor1/2 and no finite positive-axis subgradient. It violates the balancing hypothesis and does not refute the original balanced regularization problem.',
 'Exactly six whole qualified grants A224/B225/R230/S262/S272/S291 were available to the independent worker; both existing source and reader qualifications remain. R230 actual ALL-C_b envelope continuity supplies endpoints; it does not supply PA density or shared-face trace/common-support gluing. Global vague uniformity, ordinary weak/net continuity, fixed-C-only uniform weak/BL, signed/zero and zero-mass operator domains remain separate.',
 'ROOT previously physically read authoritative62588-byteTeX, source ledger/scope, all six author224 actualFINAL and safe6001-bytechecker/input, and reproduced it. Current ROOT read all six auditor227 actualFINAL, ENTIRE reconstructed-proof30176bytes, audit report8540, source ledger13027, evidence report11604 and coverageMD13348, plus complete compact reproduction/validation metadata. ROOT does NOT claim a new whole reading of every33math/98historical body or the88874-bytecoverageJSON merely from matching hashes/flags. Auditor whole-body/delta-reading claims remain its own bounded evidence.',
 'Saved auditor62637-byte notes differ in prose from actual43115-byteFINAL. IDs/supports agree; compact field comparison is bound. ROOT has read actual notes and metadata, not all saved expanded prose. Auditor did separately read author224 actual/saved expansions by lossless methods; this does not rewrite the old ROOT whole-saved-prose false flag.',
 '135 frozen and61 own artifacts match. Historical author160 inventory has only73 entries supplied to this audit,87 unavailable. Universal retrospective operations/read acts and external provider/model certification stay INCONCLUSIVE. Two ROOT exploratory aggregate metadata outputs were oversized/truncated; compact reports repaired identification/counts only, not whole semantic reading claims.',
 'ROOT and auditor each inspected/copied/executed the safe checker ONCE in their separate sessions; finite578/121/4/1/11/67/7 loops are not continuum proofs. Markdown -> standaloneTeX is exact with numbered sections, TOC/colorlinks. Distinct three-pass no-shell ROOT/auditor builds finish clean18p and preserve earlier label warnings. Six author build histories remain distinct; run002 overfull warnings retained. No new checker/compiler execution for acceptance. Builtin54 pending is unverified. No PDFpixel or fullsource historical claim, no protected editor/tab edit.',
 'This accepts the entire scoped mathematical paper as supporting paper86; original P05.1/P05.2 remain OPEN. Direct shared-face trace/common ambient support gluing and full classification remain unresolved. No automatic/canonical review or original closure is claimed.'
 ],original_closed=False))
pub.mkdir();copies=[]
for e in own:
    name=e['filename']
    if name.endswith(('.pdf','.aux','.out','.toc')) or name.startswith(('inputs/','delta-math-','reader-ranges')) or name in ['reproduction/P05.1-paper.tex','reproduction/argument.md','reproduction/generated-paper.tex']:continue
    dst=pub/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(A/name,dst);copies.append(e)
for p in [A/'own-artifact-hashes.json',actual,K/'round227-registered-native-result.json',K/'round227-actual-final-extraction-binding-20261008.json']:shutil.copyfile(p,pub/p.name)
write(pub/'ROOT-publication-binding.json',dict(recorded_utc=now,all61_own_bindings_verified=True,copied_safe_own_files=copies,third_party_full_sources_not_copied=True,supplied_programs_not_executed=True,actual_FINAL_controlling=True,original_closed=False))
b=dict(recorded_utc=now,continuation=306,source_sha256=rep['source_sha256'],ROOT_pdf_sha256=rep['ROOT_pdf_sha256'],pages=18,native_round=227,native_mathematical_verdict='PASS entire scoped paper',native_essential_source_verdict='PASS with preserved qualifications',native_bounded_evidence_verdict='PASS',universal_history='INCONCLUSIVE retained',ROOT_mathematical_verdict='PASS whole scoped mathematics WITH BOTH annotations',actual_native_FINAL_sha256=sha(actual),all6_auditor_actual_FINAL_ROOT_physically_read=True,whole_audit_unique_reconstruction_source_evidence_report_and_coverage_MD_ROOT_physically_read=True,frozen_bindings_verified=135,own_bindings_verified=61,auditor_saved_vs_actual_comparison=comparison,auditor_saved_whole_prose_ROOT_read=False,source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),source_unchanged=True,no_checker_or_build_repeated_for_acceptance=True,ordinary_native_audit_not_canonical_review=True,original_closed=False,protected_editor_unchanged_open=True)
write(binding,b)
write(accept,dict(recorded_utc=now,grant_label='S306',cumulative_accepted_paper_number=86,continuation=306,mathematical_verdict='PASS WHOLE scoped mathematics with BOTH annotations',source=str(D/'P05.1-paper.tex'),source_sha256=rep['source_sha256'],argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=rep['ROOT_pdf_sha256'],pages=18,review_binding=str(binding),review_binding_sha256=sha(binding),source_annotation=str(sourcefix),source_annotation_sha256=sha(sourcefix),reader_annotation=str(reader),reader_annotation_sha256=sha(reader),both_annotations_required_on_import=True,scope='Finite positive-real all-face-balanced embedded rational complexes: closed-cell Lipschitz/entire-incident-cell supports; explicit single-cell exact extension and global rational-spatial REAL-PA majorants; sharp unbalanced orthant diagnostic. Qualified actual envelope consequences, no all-face PA gluing.',automatic_acceptance=False,canonical_research_review=False,originals_solved=9,originals_open=33,original_closed=False,builtin_compiler_success_claimed=False))
for filename in ['active-work.json','checklist-current.json']:
    p=R/filename;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==85 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,historical_reviewed_scoped_papers=86,P05_1_accepted_balanced_cellwise306_after227=json.loads(accept.read_text()))
    j['new306_unreviewed_paper'].update(new_accepted_paper=True,whole_scoped_math_accepted_after227=True,both_annotations_required=True)
    j['current_small_batch']['accepted_paper_number']=86;write(p,j)
p=R/'checklist-current.tsv';lines=p.read_text().splitlines();changed=0
for i,line in enumerate(lines):
    f=line.split('\t')
    if f[0]=='P05.1':assert f[1]=='open';f[3]=str(int(f[3])+1);lines[i]='\t'.join(f);changed+=1
assert changed==1;p.write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(accepted_scoped_paper=86,grant='S306',originals_solved=9,originals_open=33,binding_sha256=sha(binding),acceptance_sha256=sha(accept)),indent=2))
