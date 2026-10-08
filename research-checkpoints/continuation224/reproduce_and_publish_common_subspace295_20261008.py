from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, re

R = Path('/workspace/research'); K = R / 'root-checks'
C = R / 'campaigns/round-219/P05.1-common-subspace-independent-normal-pages-all-continuous-real-regularization-paper'
A = C / 'artifacts/codex-PGL6Sy'
D = K / 'public-P05.1-continuation295-independent-common-subspace-pages-global-real-regularization'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not D.exists()
assert sha(A / 'P05.1-paper.tex') == '0692441d4438c95b2904942c6b826271a6aafe35b3d62f444831e3946d24208f'
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('original-task.json', 'original_task_sha256'), ('input.json', 'input_sha256'), ('settings.json', 'settings_sha256'), ('mathematical-packet-bindings.json', 'mathematical_packet_bindings_sha256'), ('private-primary-packet-bindings.json', 'private_primary_packet_bindings_sha256')]:
    assert sha(C / name) == f[key]
for name in ['mathematical-packet-bindings.json', 'private-primary-packet-bindings.json']:
    for e in json.loads((C / name).read_text()):
        assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
m = json.loads((A / 'artifact-bindings.json').read_text())
assert len(m['artifacts']) == 61
for e in m['artifacts']:
    assert Path(e['name']).name == e['name'] and 'LOCALONLY' not in e['name']
    assert sha(A / e['name']) == e['sha256'] and (A / e['name']).stat().st_size == e['bytes']
exact = K / 'round219-actual-native-final.json'
assert json.loads((A / 'native-notes.json').read_text()) == json.loads(exact.read_text())
assert json.loads((A / 'input.json').read_text()) == json.loads((C / 'input.json').read_text())
source = (A / 'P05.1-paper.tex').read_text()
assert not re.search(r'\\(?:input|include|write18|openin|openout)\b', source)
D.mkdir()
E = D / 'evidence'; E.mkdir()
H = E / 'own-author219-evidence'; H.mkdir()
for e in m['artifacts']:
    shutil.copy2(A / e['name'], H / e['name'])
for name in ['artifact-bindings.json', 'artifact-binding-output.txt', 'validation-output.txt']:
    shutil.copy2(A / name, H / name)
for name in ['P05.1-paper.tex', 'argument.md', 'source-application-ledger.md', 'proof-source-coverage.md', 'scope-and-gaps.md', 'clarification-control.md', 'execution-history.md', 'README-reproduce.md']:
    shutil.copy2(A / name, D / name)
shutil.copy2(exact, E / 'exact-native-final.json')
shutil.copy2(K / 'round219-registered-native-result.json', E / 'registered-native-worker-result.json')
shutil.copy2(K / 'round219-actual-final-extraction-binding-20261008.json', E / 'actual-final-extraction-binding.json')
W = E / 'ROOT-reproduction'; W.mkdir()
for name in ['exact_checks.py', 'exact-check-input.json', 'P05.1-paper.tex']:
    shutil.copy2(A / name, W / name)
root_runs = []
def run(label, args, expected=0):
    p = subprocess.run(args, cwd=W, capture_output=True)
    (W / f'{label}.stdout.txt').write_bytes(p.stdout)
    (W / f'{label}.stderr.txt').write_bytes(p.stderr)
    root_runs.append(dict(label=label, command=args, exit_code=p.returncode))
    (W / 'runs.json').write_text(json.dumps(root_runs, indent=2) + '\n')
    assert p.returncode == expected, (label, p.returncode)
    return p
out = run('exact-check', ['python', 'exact_checks.py'])
assert out.stdout == (A / 'exact-check-output.txt').read_bytes()
for i in [1, 2, 3]:
    run(f'latex-pass-{i}', ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'P05.1-paper.tex'])
    shutil.copy2(W / 'P05.1-paper.log', W / f'latex-pass-{i}.tex.log')
    assert sha(W / 'P05.1-paper.tex') == sha(A / 'P05.1-paper.tex')
run('markdown', ['pandoc', 'P05.1-paper.tex', '--from=latex', '--to=gfm', '--standalone', '--output=argument.md'])
assert (W / 'argument.md').read_bytes() == (A / 'argument.md').read_bytes()
final_log = (W / 'latex-pass-3.tex.log').read_text()
assert not re.search(r'undefined references|Rerun to get|Overfull \\hbox|Underfull \\hbox', final_log, re.I)
pi = run('pdfinfo', ['pdfinfo', 'P05.1-paper.pdf']).stdout.decode()
assert re.search(r'^Pages:\s+14\s*$', pi, re.M)
shutil.copy2(W / 'P05.1-paper.pdf', D / 'P05.1-paper.pdf')
b = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), continuation=295, native_author_round=219, source=str(D / 'P05.1-paper.tex'), source_sha256=sha(D / 'P05.1-paper.tex'), source_bytes=len(source.encode()), source_LF_lines=source.count('\n'), argument_sha256=sha(D / 'argument.md'), pdf_sha256=sha(D / 'P05.1-paper.pdf'), pdf_pages=14, actual_FINAL_notes=6, all6_actual_FINAL_and_entire_source_ROOT_read=True, whole_ledger_scope_coverage_execution_ROOT_read=True, saved_native_notes_equal_FINAL_after_parsing=True, saved_native_notes_byte_equality_not_claimed=True, registered_result_only_artifacts_suffix=True, all61_own_artifact_bindings_verified=True, all25_math_and4_primary_bindings_verified=True, primary_PDF_whole_ROOT_read_not_claimed=True, primary_text_immediate_units_previously_ROOT_read=True, parent_child_inputs_semantically_equal=True, safe_exact_checker_and_input_whole_ROOT_read_before_execution=True, supplied_emitters_audits_builders_bindings_orchestration_not_executed=True, copied_safe_checker_executed_once=True, finite_output_byte_exact=True, finite_checks_not_continuum_proof=True, source_to_standalone_GFM_bytes_exact=True, local_build_exit_codes=[0,0,0], initial_reference_warnings_preserved=True, final_only_disabled_shell_package_warning=True, native_initial_macro_failure_and_source_reconstruction_preserved=True, builtin_compilation_success_not_claimed=True, independent_audit_not_yet_started=True, native_role='ordinary native Codex scoped author, NOT independent acceptance', candidate=False, new_accepted_paper=False, original_closed=False, protected_editor_unchanged_open=True)
(D / 'root-reproduction-binding-20261008.json').write_text(json.dumps(b, indent=2) + '\n')
print(json.dumps(b, indent=2))
