from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-217/P05.1-isolated-affine-crossings-all-continuous-global-regularization-paper';A=C/'artifacts/codex-ybo6Ea'
D=K/'public-P05.1-continuation292-isolated-affine-crossings-global-real-regularization';E=D/'evidence';W=E/'ROOT-reproduction'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert D.exists() and not (D/'root-reproduction-binding-20261008.json').exists()
assert sha(D/'P05.1-paper.tex')==sha(W/'P05.1-paper.tex')==sha(A/'P05.1-paper.tex')=='4ece9622c0d97a861dde051ec6a31c0bd0416781bd4c43c0b4aaa0f498ffe11c'
assert (W/'certificate-output.json').read_bytes()==(A/'certificate-output.json').read_bytes()
assert (W/'argument.md').read_bytes()!=(A/'argument.md').read_bytes()
initial=W/'argument-initial-gfm.md';assert not initial.exists();shutil.copyfile(W/'argument.md',initial)
write(W/'initial-formatter-discrepancy.json',dict(recorded_utc=datetime.now(timezone.utc).isoformat(),helper=str(R/'reproduce_isolated_crossings292_20261008.py'),helper_sha256=sha(R/'reproduce_isolated_crossings292_20261008.py'),actual_exit_code=1,failure='AssertionError at whole source-to-Markdown byte comparison',reason='ROOT initially used non-standalone GFM; author used standalone Pandoc markdown. This is a formatter mismatch, not a mathematical source change.',initial_conversion=str(initial),initial_conversion_sha256=sha(initial),source_unchanged=True,finite_checker_and_both_local_build_passes_already_succeeded=True,no_repeated_finite_checks_or_TeX_builds=True))
args=['pandoc','-s','-f','latex','-t','markdown','--wrap=none','P05.1-paper.tex']
p=subprocess.run(args,cwd=W,capture_output=True,text=True);(W/'logs/pandoc-corrected.log').write_text(p.stderr);assert p.returncode==0
(W/'argument.md').write_text(p.stdout)
assert (W/'argument.md').read_bytes()==(A/'argument.md').read_bytes()==(D/'argument.md').read_bytes()
commands=[];diagnostics=[]
for i in [1,2]:
    log=W/f'logs/build-pass-{i}.log';text=log.read_text();assert 'Output written on P05.1-paper.pdf' in text
    commands.append(dict(argv=['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex'],exit_code=0,log=str(log)))
    diagnostics.append([line for line in text.splitlines() if any(k in line for k in ['Warning','Overfull','Underfull','undefined','Error'])])
assert not diagnostics[-1]
shutil.copyfile(W/'P05.1-paper.pdf',D/'P05.1-paper.pdf')
info=subprocess.run(['pdfinfo',str(D/'P05.1-paper.pdf')],capture_output=True,text=True,check=True).stdout;(W/'logs/pdfinfo.txt').write_text(info)
assert 'Pages:           17' in info
out=json.loads((W/'certificate-output.json').read_text());assert len(out['matrices'])==5 and sum(len(x['ordered_permutations']) for x in out['matrices'])==13 and sum(x['all_words'] for x in out['matrices'])==40 and sum(x['repeated_words_zero'] for x in out['matrices'])==27
source=(D/'P05.1-paper.tex').read_text()
binding=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),original='P05.1',continuation=292,source=str(D/'P05.1-paper.tex'),source_sha256=sha(D/'P05.1-paper.tex'),source_LF_lines=source.count('\n'),argument=str(D/'argument.md'),argument_sha256=sha(D/'argument.md'),pdf=str(D/'P05.1-paper.pdf'),pdf_sha256=sha(D/'P05.1-paper.pdf'),pdf_pages=17,exact_FINAL=str(E/'exact-native-final.json'),exact_FINAL_sha256=sha(E/'exact-native-final.json'),exact_FINAL_candidate=False,exact_FINAL_notes=6,exact_FINAL_saved_native_notes_byte_equal=True,expanded_saved_draft_preserved_not_exact_FINAL=True,registered_result_only_Artifacts_suffix=True,parent_child_input_semantically_equal=True,author_artifact_bindings_verified=len(json.loads((A/'artifact-bindings.json').read_text())['files']),math_bindings_verified=19,primary_bindings_verified=4,ROOT_source_whole_read=True,ROOT_ledger_scope_coverage_execution_whole_read=True,ROOT_exact_FINAL_all6_whole_read=True,ROOT_safe_exact_checker_whole_read=True,ROOT_finite_output_exact=True,finite_matrix_cases=5,finite_permutations=13,finite_words=40,repeated_factor_zeros=27,finite_scope_only=True,latex_to_markdown_exact=True,correct_conversion_argv=args,initial_GFM_formatter_mismatch_failure_preserved=True,no_repeated_finite_checks_or_builds=True,local_build_exit_codes=[0,0],local_build_diagnostics=diagnostics,source_unchanged=True,retained_presentation_typo='Source equation contains literal qquad after sum_i w_i=0; intended separator is clear in exact FINAL prose. Source remains unchanged.',only_grants=['A224','B225','R230','S262','S272'],all_clarifications_retained=True,new_ROOT289290293294_excluded_from_author=True,new_S282_acceptance_not_a_grant=True,mathematical_acceptance=False,original_closed=False,protected_editor_unchanged_open=True)
write(D/'root-reproduction-binding-20261008.json',binding);print(json.dumps(binding,indent=2))
