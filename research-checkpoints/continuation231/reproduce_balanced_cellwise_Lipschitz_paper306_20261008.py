from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, re

R = Path('/workspace/research'); K = R / 'root-checks'
C = R / 'campaigns/round-224/P05.1-finite-balanced-cellwise-Lipschitz-and-single-cell-real-regularization-paper'
A = C / 'artifacts/codex-X5OM2t'
D = K / 'public-P05.1-continuation306-balanced-cellwise-Lipschitz-and-single-cell-real-regularization'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, v: Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
assert not D.exists()
protected = K / 'public-P16-round-46-final-reader/P16.4-paper.tex'
protected_hash = '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
assert sha(protected) == protected_hash
assert sha(A / 'P05.1-paper.tex') == '121e25eeb7b89371cc89d54c1bce1b4f1037be9d4a6e38e037c45d8041fec737'
bindings = json.loads((A / 'artifact-bindings.json').read_text())
assert len(bindings['artifacts']) == 160
for e in bindings['artifacts']:
    p = A / e['filename']
    assert p.is_file() and p.stat().st_size == e['bytes'] and sha(p) == e['sha256']
for key, name, count in [('mathematical', 'mathematical-packet-bindings.json', 28), ('primary', 'private-primary-packet-bindings.json', 4)]:
    entries = json.loads((C / name).read_text())
    assert len(entries) == count and len(bindings['bound_input_identities'][key]) == count
    for e, b in zip(entries, bindings['bound_input_identities'][key]):
        assert Path(e['path']).stat().st_size == e['bytes'] == b['bytes']
        assert sha(e['path']) == e['sha256'] == b['sha256']
actual = json.loads((K / 'round224-actual-native-final.json').read_text())
saved = json.loads((A / 'native-notes.json').read_text())
assert actual['candidate'] is False and saved['candidate'] is False and len(actual['notes']) == len(saved['notes']) == 6
comparison = []
for a, b in zip(actual['notes'], saved['notes']):
    assert a['id'] == b['id'] and a['support'] == b['support']
    comparison.append(dict(id=a['id'], fields={k: dict(equal=a.get(k) == b.get(k), actual_chars=len(str(a.get(k))), saved_chars=len(str(b.get(k)))) for k in sorted(set(a) | set(b))}))
D.mkdir(); E = D / 'evidence'; E.mkdir()
S = E / 'ROOT-reproduction'; S.mkdir()
for name in ['code', 'inputs', 'reports', 'build']: (S / name).mkdir()
for name in ['code/checks.py', 'inputs/check-input.json']: shutil.copyfile(A / name, S / name)
with (S / 'reports/checks.stdout.json').open('wb') as out:
    p = subprocess.run(['python', str(S / 'code/checks.py')], cwd=S, stdout=out, stderr=subprocess.PIPE)
(S / 'reports/checks.stderr.txt').write_bytes(p.stderr)
assert p.returncode == 0
assert (S / 'reports/exact-checks.json').read_bytes() == (A / 'reports/exact-checks.json').read_bytes()
shutil.copyfile(A / 'argument.md', S / 'argument.md')
commands = []
def run(argv, log):
    p = subprocess.run(argv, cwd=S, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (S / log).write_bytes(p.stdout)
    commands.append(dict(argv=argv, exit_code=p.returncode, log=log))
    assert p.returncode == 0, str(S / log)
run(['pandoc', 'argument.md', '--standalone', '--number-sections', '--table-of-contents', '--top-level-division=section', '--variable', 'colorlinks=true', '-o', 'P05.1-paper.tex'], 'reports/pandoc.log')
assert (S / 'P05.1-paper.tex').read_bytes() == (A / 'P05.1-paper.tex').read_bytes()
for n in [1, 2, 3]:
    run(['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-output-directory=build', 'P05.1-paper.tex'], f'reports/pdflatex-pass{n}.stdout.log')
    shutil.copyfile(S / 'build/P05.1-paper.log', S / f'reports/pdflatex-pass{n}.tex.log')
assert sha(S / 'P05.1-paper.tex') == sha(A / 'P05.1-paper.tex')
final_log = (S / 'reports/pdflatex-pass3.tex.log').read_text()
warnings = [line for line in final_log.splitlines() if re.search(r'Warning|Overfull|Underfull|Undefined', line)]
assert not warnings, warnings
run(['pdfinfo', 'build/P05.1-paper.pdf'], 'reports/pdfinfo.txt')
pdfinfo = (S / 'reports/pdfinfo.txt').read_text()
pages = int(re.search(r'^Pages:\s+(\d+)', pdfinfo, re.M).group(1))
for name in ['P05.1-paper.tex', 'argument.md', 'source-application-ledger.md', 'scope-and-gaps.md', 'README.md']:
    shutil.copyfile(A / name, D / name)
shutil.copyfile(S / 'build/P05.1-paper.pdf', D / 'P05.1-paper.pdf')
for name in ['round224-actual-native-final.json', 'round224-actual-final-extraction-binding-20261008.json', 'round224-registered-native-result.json']:
    shutil.copyfile(K / name, E / name)
for name in ['native-notes.json', 'artifact-bindings.json', 'logs/initial-observations.md', 'reports/build-report.json', 'reports/proof-coverage.json', 'reports/deliverable-validation.json']:
    dst = E / 'author-evidence' / name; dst.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(A / name, dst)
write(E / 'actual-vs-expanded-saved-fields.json', dict(actual_FINAL_controls=True, all_six_field_comparisons=comparison, whole_saved_prose_ROOT_read_claimed=False))
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), author_round=224, continuation=306, status='Complete unreviewed scoped draft and ROOT local reproduction; independent mathematical review pending', verified_author_artifacts=160, verified_whole_math_bindings=28, verified_primary_bindings=4, all_six_actual_FINAL_notes_physically_ROOT_read=True, entire_authoritative_TeX_physically_ROOT_read=True, entire_source_ledger_and_scope_physically_ROOT_read=True, copied_safe_checker_and_input_physically_ROOT_read_before_execution=True, safe_checker_executions=1, finite_checks_exact_author_match=True, exact_original_Markdown_to_TeX_reproduced=True, commands=commands, retained_initial_warnings=True, final_pass_warnings=warnings, source_sha256=sha(D / 'P05.1-paper.tex'), ROOT_pdf_sha256=sha(D / 'P05.1-paper.pdf'), ROOT_pdf_pages=pages, author_pdf_identity_not_claimed=True, author_six_distinct_build_directories_preserved_at_original_location=True, author_builders_binders_audits_not_executed=True, mathematical_acceptance=False, new_accepted_paper=False, candidate=False, original_closed=False, original_P05_1='OPEN', original_P05_2='OPEN', cumulative_accepted_papers=85, remaining_gap='Whole shared-face traces and common ambient supports for PA approximants across an arbitrary finite balanced complex', protected_editor_unchanged_open=True, private_active_output_read=False)
write(D / 'ROOT-reproduction-binding-20261008.json', record)
assert sha(protected) == protected_hash
print(json.dumps(dict(directory=str(D), ROOT_pdf_pages=pages, source_sha256=record['source_sha256'], exact_checks=True, unchanged_TeX=True, new_accepted_paper=False), indent=2))
