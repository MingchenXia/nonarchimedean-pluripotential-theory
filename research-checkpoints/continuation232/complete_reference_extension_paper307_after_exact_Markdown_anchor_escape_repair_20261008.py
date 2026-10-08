from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, re

R = Path('/workspace/research'); K = R / 'root-checks'
C = R / 'campaigns/round-225/P05.1-compatible-reference-extensions-and-sharp-uniform-target-extension-obstruction-paper'
A = C / 'artifacts/codex-i0eUzs'
D = K / 'public-P05.1-continuation307-compatible-affine-reference-extension-and-sharp-global-restriction-distance'
E = D / 'evidence'; S = E / 'ROOT-reproduction'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, v: Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
protected = K / 'public-P16-round-46-final-reader/P16.4-paper.tex'
protected_hash = '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert not (D / 'ROOT-reproduction-binding-20261008.json').exists()
assert sha(S / 'P05.1-paper.tex') == sha(A / 'P05.1-paper.tex') == '258fac9a3a5e9eb7e0cb6419653ac8239cdf6fe5d389da08226eef2e5462ed61'
assert (S / 'exact-output.json').read_bytes() == (A / 'exact-output.json').read_bytes()
assert (A / 'native-notes.json').read_bytes() == (K / 'round225-actual-native-final.json').read_bytes() + b'\n'
final_log = (S / 'pdflatex-pass2.tex.log').read_text()
warnings = [line for line in final_log.splitlines() if re.search(r'Warning|Overfull|Underfull|Undefined', line)]
assert not warnings
pages = int(re.search(r'^Pages:\s+(\d+)', (S / 'pdfinfo.txt').read_text(), re.M).group(1)); assert pages == 16
commands = [dict(argv=['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-output-directory=build', 'P05.1-paper.tex'], exit_code=0, log=f'pdflatex-pass{n}.stdout.log') for n in [1, 2]]
write(E / 'ROOT-first-presentation-reproduction-failure-and-repair.json', dict(recorded_utc=datetime.now(timezone.utc).isoformat(), failed_helper=str(R / 'reproduce_reference_extension_and_sharp_obstruction_paper307_20261008.py'), failed_helper_sha256=sha(R / 'reproduce_reference_extension_and_sharp_obstruction_paper307_20261008.py'), actual_failure='AssertionError in exact source-body Markdown comparison, after successful checker and two clean TeX passes', cause='ROOT anchor replacement omitted the literal backslashes before quotes retained by the author Markdown converter', source_and_author_artifacts_unchanged=True, repair='Preserve literal anchor quote escapes in ROOT conversion; resume presentation checks and publication only', safe_checker_and_TeX_build_not_reexecuted=True, no_mathematical_failure_inferred=True))
# Independently reproduce the disclosed body-only presentation transformation.
# This is ROOT code; the supplied make_argument.py is never executed/imported.
raw = (S / 'P05.1-paper.tex').read_bytes(); body = raw.decode().split('\\begin{abstract}', 1)[1].split('\\begin{thebibliography}', 1)[0]
body = body.replace('\\end{abstract}', '\n')
body = re.sub(r'\\section\{([^{}]*)\}', r'\n## \1\n', body)
body = re.sub(r'\\label\{([^{}]*)\}', r' <a id=\"\1\"></a>', body)
body = re.sub(r'\\ref\{([^{}]*)\}', r'[\1](#\1)', body)
body = re.sub(r'\\begin\{(theorem|lemma|proposition)\}(?:\[([^\]]*)\])?', lambda m: '\n**' + m[1].title() + (': ' + m[2] if m[2] else '') + '.** ', body)
body = re.sub(r'\\end\{(?:theorem|lemma|proposition)\}', '\n', body)
body = body.replace('\\begin{proof}', '\n**Proof.** ').replace('\\end{proof}', ' ∎\n')
body = body.replace('\\begin{align*}', '$$\n\\begin{aligned}').replace('\\end{align*}', '\\end{aligned}\n$$').replace('\\[', '$$').replace('\\]', '$$')
for name, replacement in [('R', r'\mathbb{R}'), ('Q', r'\mathbb{Q}'), ('Z', r'\mathbb{Z}'), ('PA', r'\mathrm{PA}'), ('PC', r'\mathrm{PC}')]:
    body = re.sub(r'\\' + name + r'(?![A-Za-z])', lambda m, value=replacement: value, body)
for name in ['conv', 'cone', 'epi', 'rec', 'aff', 'ri', 'dist']:
    value = r'\operatorname{' + ('relint' if name == 'ri' else name) + '}'
    body = re.sub(r'\\' + name + r'(?![A-Za-z])', lambda m, value=value: value, body)
body = re.sub(r'\\emph\{([^{}]*)\}', r'*\1*', body)
body = re.sub(r'\\texttt\{([^{}]*)\}', lambda m: '`' + m[1].replace(r'\_', '_') + '`', body)
body = body.replace('~', ' ').replace('--', '–')
header = '# Compatible references and sharp uniform restriction obstruction\n\nOwn source-derived proof manuscript. Unreviewed; original P05.1/P05.2 remain OPEN; candidate=false.\n\nDerived from `P05.1-paper.tex`, SHA256 `' + hashlib.sha256(raw).hexdigest() + '`, by `python3 make_argument.py`. All theorem/proof prose and mathematical displays in the body are retained. Markdown conversion is presentation, not an independent correctness certificate.\n\n'
derived = (header + body.strip() + '\n').encode()
assert derived == (A / 'argument.md').read_bytes(); (S / 'derived-argument.md').write_bytes(derived)
for name in ['P05.1-paper.tex', 'argument.md', 'source-application-ledger.md', 'scope-and-gaps.md', 'README.md', 'execution-history.md']: shutil.copyfile(A / name, D / name)
shutil.copyfile(S / 'build/P05.1-paper.pdf', D / 'P05.1-paper.pdf')
for name in ['round225-actual-native-final.json', 'round225-actual-final-extraction-binding-20261008.json', 'round225-registered-native-result.json']: shutil.copyfile(K / name, E / name)
for name in ['native-notes.json', 'artifact-bindings.json', 'input-bindings.json', 'snapshot-bindings.json', 'build-report.json', 'source-binding-report.json', 'primary-units.json', 'primary-read-coverage.jsonl', 'whole-read-coverage.jsonl', 'exact-output.json']:
    dst = E / 'author-evidence' / name; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(A / name, dst)
for p in sorted((A / 'build').rglob('*.log')):
    dst = E / 'author-evidence' / p.relative_to(A); dst.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p, dst)
shutil.copyfile(A / 'build/history-001/build-report.json', E / 'author-evidence/build/history-001/build-report.json')
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), author_round=225, continuation=307, status='Complete unreviewed scoped paper and ROOT reproduction; independent proof/source review pending', verified_author_artifacts=98, verified_bound_inputs=36, verified_matching_local_input_snapshots=36, all_four_actual_FINAL_notes_physically_ROOT_read=True, saved_notes_exact_actual_plus_terminal_LF=True, entire_57663_byte_authoritative_TeX_physically_ROOT_read=True, entire_source_ledger_scope_execution_history_and_final_build_report_physically_ROOT_read=True, safe_5091_byte_checker_and_281_byte_input_physically_ROOT_read_before_execution=True, copied_safe_checker_executions=1, exact_author_output_match=True, finite_assertions=1577, finite_diagnostic_cost='-1/4', independent_source_body_to_Markdown_transformation_exact=True, source_body_conversion_excludes_preamble_and_bibliography=True, author_conversion_emitter_not_executed=True, source_sha256=sha(D / 'P05.1-paper.tex'), argument_sha256=sha(D / 'argument.md'), ROOT_pdf_sha256=sha(D / 'P05.1-paper.pdf'), ROOT_pdf_pages=pages, commands=commands, retained_first_pass_warnings=True, final_pass_warnings=warnings, author_historical_build_logs_preserved=True, mathematical_acceptance=False, new_accepted_paper=False, candidate=False, original_closed=False, original_P05_1='OPEN', original_P05_2='OPEN', cumulative_accepted_papers=85, statement='Compatible actual-affine positive-growth reference extensions; sharp GLOBAL restriction distance (A-1)/2 from an already PA-PC UNBALANCED partial target to ALL finite continuous PC complete-book competitors', remaining_gap='Direct original balanced all-face compatible PA approximation', private_active_output_read=False, hot_feedback_sent=False, protected_editor_unchanged_open=True)
write(D / 'ROOT-reproduction-binding-20261008.json', record)
assert sha(protected) == protected_hash
print(json.dumps(dict(directory=str(D), ROOT_pdf_pages=pages, source_sha256=record['source_sha256'], exact_finite_output=True, exact_body_Markdown=True, new_accepted_paper=False), indent=2))
