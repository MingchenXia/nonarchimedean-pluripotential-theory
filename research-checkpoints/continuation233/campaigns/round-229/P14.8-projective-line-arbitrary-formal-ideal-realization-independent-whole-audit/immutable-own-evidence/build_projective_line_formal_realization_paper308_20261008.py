from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, shutil, re

R = Path('/workspace/research'); K = R / 'root-checks'
D = K / 'public-P14.8-continuation308-arbitrary-formal-ideal-realization-on-projective-line'
S = D / 'evidence/ROOT-build'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not S.exists() and not (D / 'ROOT-working-proof-and-build-binding-20261008.json').exists()
protected = K / 'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(protected) == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
source = D / 'P14.8-paper.tex'; source_hash = sha(source)
S.mkdir(parents=True)
commands = []
for n in [1, 2]:
    argv = ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-output-directory=' + str(S), source.name]
    p = subprocess.run(argv, cwd=D, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (S / f'pass{n}.stdout.log').write_bytes(p.stdout)
    if (S / 'P14.8-paper.log').exists(): shutil.copyfile(S / 'P14.8-paper.log', S / f'pass{n}.tex.log')
    commands.append(dict(argv=argv, exit_code=p.returncode, log=str(S / f'pass{n}.stdout.log')))
    assert p.returncode == 0
assert sha(source) == source_hash
final_warnings = [s for s in (S / 'pass2.tex.log').read_text().splitlines() if re.search(r'Warning|Overfull|Underfull|Undefined', s)]
assert not final_warnings, final_warnings
info = subprocess.run(['pdfinfo', str(S / 'P14.8-paper.pdf')], capture_output=True, text=True, check=True)
(S / 'pdfinfo.txt').write_text(info.stdout)
pages = int(re.search(r'^Pages:\s+(\d+)', info.stdout, re.M).group(1))
shutil.copyfile(S / 'P14.8-paper.pdf', D / 'P14.8-paper.pdf')
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), author='ROOT independent working proof, not a native campaign result', continuation=308, atom='P14.8', whole_authoritative_TeX_physically_ROOT_read=True, source_bytes=source.stat().st_size, literal_LF_lines=source.read_bytes().count(b'\n'), source_sha256=source_hash, local_PDF_sha256=sha(D / 'P14.8-paper.pdf'), local_PDF_pages=pages, commands=commands, final_pass_warnings=final_warnings, first_pass_warnings_retained=True, proof_units=['Local multiplier ideal floor including critical exponents via atom removal, Jensen and Holder', 'Data-only necessity from curvature atom budget and integer-order supremum', 'Explicit countable chordal kernel sufficiency with exact L1 size and curvature', 'Formal budget and parameter-pattern obstructions; representative nonuniqueness'], ordinary_analytic_premises=['Logarithmic distributional fundamental solution', 'Positive-curvature distribution has its subharmonic representative', 'Weyl lemma for harmonic distributions', 'Elementary measure integration and Hölder/Jensen inequalities'], caller_grants=[], mathematical_acceptance=False, new_accepted_paper=False, candidate=False, original_closed=False, original_general_P14_8='OPEN', cumulative_accepted_papers=85, scope='Arbitrary formal nonzero coherent ideal arrays on complex P1 for theta=V*normalizedFS, all actual real c>0 and V>=0', native226227_outputs_not_read_or_fed=True, protected_editor_unchanged_open=True, built_in_compile_cell='90', built_in_result_not_received=True)
(D / 'ROOT-working-proof-and-build-binding-20261008.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(directory=str(D), pages=pages, source_sha256=source_hash, mathematical_acceptance=False, original_closed=False), indent=2))
