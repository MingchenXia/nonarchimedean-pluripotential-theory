from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, fitz
R=Path('/workspace/research'); K=R/'root-checks'; D=K/'public-P16.4-continuation227-genus-zero-equation'
A=Path(json.loads((K/'P16.4-round186-completed-actual-author-result-20261007.json').read_text())['workspace'])
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not (D/'root-reproduction-binding-20261007.json').exists()
assert sha(D/'P16.4-paper.tex')==sha(A/'P16.4-paper.tex')=='bf78e6188aea85eb34c06fa6d6152900259207318d843037f2e29e2cca712f57'
assert len((D/'P16.4-paper.tex').read_text().splitlines())==851
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for i in (1,2):
    raw=(D/f'evidence/root-latex-pass{i}.stdout').read_bytes()
    assert b'Output written on P16.4-paper.pdf (11 pages' in raw
    assert b'Fatal error' not in raw
warnings=re.findall(r'.*(?:Warning|Overfull|Underfull|undefined|^!).*',(D/'P16.4-paper.log').read_text(errors='replace'),re.M)
assert warnings==['Underfull \\hbox (badness 2237) in paragraph at lines 790--798']
assert json.loads((D/'evidence/root-finite-check.json').read_text())['status'].startswith('PASS')
now=datetime.now(timezone.utc).isoformat()
b=dict(recorded_utc=now,atom='P16.4',continuation=227,native_author_round=186,native_workspace=str(A),source_sha256=sha(D/'P16.4-paper.tex'),source_lf_lines=851,source_equal_complete_native_source=True,whole_saved_source_root_read=True,whole_four_notes_root_read=True,whole_source_application_json_ledger_root_read=True,whole_native_argument_separately_root_read=False,fresh_final_local_builds=2,local_warnings=warnings,root_finite_check_rerun=True,finite_checks_only=True,pdf_sha256=sha(D/'P16.4-paper.pdf'),pdf_pages=len(fitz.open(D/'P16.4-paper.pdf')),all_pdf_pages_visually_root_read=False,root_visual_pages_read=[],independent_mathematical_verdict=None,new_accepted_paper=False,original_closed=False,protected_editor_unchanged_open=True,no_active_private_output_read=True,native_compiler_success=True,prior_helper_stopped_after_successful_builds='UTF-8 decoding of raw TeX log failed at a non-UTF8 byte; original outputs and helper retained; no rerun or source change',log_scan_decode_policy='errors=replace for diagnostic scan only; raw log and raw pass outputs preserved')
(D/'root-reproduction-binding-20261007.json').write_text(json.dumps(b,indent=2)+'\n')
(D/'native-compiler-success-final-source-addendum-20261007.json').write_text(json.dumps(dict(recorded_utc=now,path=str(D/'P16.4-paper.tex'),source_sha256=sha(D/'P16.4-paper.tex'),native_result=dict(path=str(D/'P16.4-paper.tex'),kind='success',message="The current source compiled successfully with the desktop editor's compiler."),source_unchanged_since_applicable_compile_request=True,mathematical_acceptance_implied=False,protected_editor_unchanged_open=True),indent=2)+'\n')
pdf=fitz.open(D/'P16.4-paper.pdf')
for i in (0,len(pdf)-1): pdf[i].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(str(D/f'evidence/root-visual-page{i+1}.png'))
(D/'README.md').write_text('P16.4 continuation227: genus-zero equation over the original field\n\nEleven-page unreviewed native186 manuscript, including non-split conics, over complete characteristic-zero fields with residue characteristic zero. Six complete accepted grants O217/D214/N220/T171/Q222/C218; every new splitting, finite Galois tree center, actual norming metric, equation and every-solution uniqueness application requires independent review. No full original closure.\n\nWhole851-line source, all four notes and JSON source ledger read by ROOT; native argument not separately read in full. Finite checks rerun, two local builds succeeded with one recorded underfull box; exact native compiler SUCCESS. Raw logs retained after UTF8 diagnostic decoding issue. Protected existing editor remains open and unchanged.\n')
print(json.dumps(b,indent=2))
