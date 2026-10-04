#!/usr/bin/env python3
"""Reproduce the two TeX runs and finite artifact/arithmetic checks.

These checks are not mathematical proof verification.
"""
import hashlib
import json
import math
import platform
import shutil
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKS = ROOT / 'checks'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def determinant(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    return sum(((-1) ** j) * a[0][j] * determinant([r[:j] + r[j+1:] for r in a[1:]]) for j in range(n))

def main():
    CHECKS.mkdir(exist_ok=True)
    previous = [p for p in CHECKS.iterdir() if p.is_file()]
    if previous:
        number = 1
        while (CHECKS / f'prior-check-run-{number}').exists():
            number += 1
        archive = CHECKS / f'prior-check-run-{number}'
        archive.mkdir()
        for path in previous:
            shutil.copyfile(path, archive / path.name)
    commands = []
    results = {'warning': 'Finite arithmetic, provenance, and compilation checks do not verify mathematics.', 'checks': [], 'tex_runs': []}

    def check(name, passed, detail):
        results['checks'].append({'name': name, 'passed': bool(passed), 'detail': detail})
        if not passed:
            raise AssertionError(name)

    b = (ROOT / 'input.json').read_bytes()
    original = json.loads(b)
    check('byte-identical-input', b == (ROOT / 'input-original.json').read_bytes(), {'sha256': sha(b), 'bytes': len(b)})
    check('unchanged-assignment-string', (ROOT / 'assignment-original.txt').read_text() == original['assignment'], 'Exact decoded string, with no added newline.')
    check('unchanged-task-object', json.loads((ROOT / 'task-original.json').read_text()) == original['task'], 'Object equality; no task redefinition.')
    status = json.loads((ROOT / 'status.json').read_text())
    check('exact-status-keys', set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}, list(status))
    check('status-remains-incomplete', status['id'] == 'P13.2' and status['status'] == 'incomplete' and bool(status['concrete_gaps']), status['status'])

    cmd = [sys.executable, 'build_provenance.py']
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True)
    (CHECKS / 'provenance.stdout.txt').write_bytes(proc.stdout)
    (CHECKS / 'provenance.stderr.txt').write_bytes(proc.stderr)
    commands.append({'argv': cmd, 'cwd': str(ROOT), 'returncode': proc.returncode})
    check('source-provenance-build', proc.returncode == 0, proc.stdout.decode('utf-8', errors='replace'))
    provenance = json.loads((ROOT / 'source-extracts/source-provenance.json').read_text())
    excerpt_count = 0
    for src in provenance['sources']:
        raw = (ROOT / ('source-extracts/' + src['id'] + '-literal.txt')).read_bytes()
        check(src['id'] + '-local-literal-hash', sha(raw) == src['extract_sha256'], src['saved_version'])
        lines = raw.decode('utf-8').split('\n')
        for part in src['literal_statements_and_relevant_proof_bodies']:
            literal = '\n'.join(lines[part['LF_start']-1:part['LF_end']])
            artifact = (ROOT / part['artifact']).read_bytes()
            assert literal == part['literal'] and artifact == literal.encode('utf-8')
            assert sha(artifact) == part['sha256']
            excerpt_count += 1
    check('LF-excerpt-identity', excerpt_count == 31, {'source_count': len(provenance['sources']), 'excerpts': excerpt_count, 'method': "split('\\n'), inclusive one-based ranges"})

    c = F(3, 2)
    shifts = []
    bounds = []
    for n in range(1, 8):
        # The truncated-simplex average is n/(n+1) times a constant slice weight.
        truncated = c * F(n, n+1)
        printed_slice = c / (n+1)
        shifts.append({'cone_dimension': n, 'genuine_constant_shift_energy': str(c), 'truncated_degree_S': str(truncated), 'printed_slice_energy': str(printed_slice), 'discrepancies': [str(c-truncated), str(c-printed_slice)]})
        assert truncated != c and printed_slice != c
        coefficient = F(math.factorial(n-1), n**(n+1))
        bound = F(n**(n+1), math.factorial(n-1))
        assert coefficient * bound == 1
        bounds.append({'n': n, 'repaired_coefficient': str(coefficient), 'inverse_bound': str(bound)})
    check('finite-constant-shift-counterchecks', True, shifts)
    check('finite-repaired-bound-coefficients', True, bounds)

    s = F(5, 3)
    check('A2-sign-counterexample-arithmetic', F(0) < s/2 < s, {'s': str(s), 'left_integral': '0', 'genuine_energy': str(s/2), 'right_integral': str(s), 'printed_reverse_inequality_is_false': True, 'limitation': 'Arithmetic check only; the current calculation is proved in the draft.'})

    determinants = []
    for p, q in [(F(2), F(3)), (F(3,2), F(7,4)), (F(5), F(11))]:
        matrix = [[F(-1), F(0), F(0)], [F(1), -1/p, F(0)], [F(1), F(0), -1/q]]
        det = abs(determinant(matrix))
        volume = 1/(p*q)
        assert det == volume and det / volume == 1
        determinants.append({'p': str(p), 'q': str(q), 'absolute_coordinate_determinant': str(det), 'volume': str(volume), 'normalized_mass': '1'})
    check('finite-local-determinant-normalizers', True, {'rational_samples': determinants, 'limitation': 'The irrational identity and rational-rank assertion are algebraic arguments in the draft, not numerical verification.'})

    environment = {'python': sys.version, 'platform': platform.platform(), 'cwd': str(ROOT), 'tools': {}}
    for tool in ('pdflatex', 'latexmk', 'pdftotext'):
        exe = shutil.which(tool)
        version_argv = [exe, '-v' if tool == 'pdftotext' else '--version'] if exe else None
        p = subprocess.run(version_argv, capture_output=True, text=True) if exe else None
        environment['tools'][tool] = {'executable': exe, 'version_argv': version_argv, 'version_returncode': p.returncode if p else None, 'version_stdout': p.stdout if p else '', 'version_stderr': p.stderr if p else ''}
    (ROOT / 'environment.json').write_text(json.dumps(environment, indent=2) + '\n')

    for pass_number in (1, 2):
        cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'P13.2-paper.tex']
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True)
        stdout_name = f'checks/tex-pass-{pass_number}.stdout.txt'
        stderr_name = f'checks/tex-pass-{pass_number}.stderr.txt'
        log_name = f'checks/P13.2-paper.pass-{pass_number}.log'
        (ROOT / stdout_name).write_bytes(p.stdout)
        (ROOT / stderr_name).write_bytes(p.stderr)
        if (ROOT / 'P13.2-paper.log').exists():
            shutil.copyfile(ROOT / 'P13.2-paper.log', ROOT / log_name)
        entry = {'pass': pass_number, 'argv': cmd, 'cwd': str(ROOT), 'returncode': p.returncode, 'stdout': stdout_name, 'stderr': stderr_name, 'tex_log': log_name}
        commands.append(entry)
        results['tex_runs'].append(entry)

    pdf = ROOT / 'P13.2-paper.pdf'
    check('two-compiler-runs', len(results['tex_runs']) == 2, [r['returncode'] for r in results['tex_runs']])
    check('two-successful-compiler-runs', all(r['returncode'] == 0 for r in results['tex_runs']), [r['returncode'] for r in results['tex_runs']])
    check('standalone-pdf-created', pdf.exists() and pdf.stat().st_size > 0, {'bytes': pdf.stat().st_size if pdf.exists() else 0, 'sha256': sha(pdf.read_bytes()) if pdf.exists() else None})
    last_log = (ROOT / results['tex_runs'][-1]['tex_log']).read_text(errors='replace')
    warnings = [line for line in last_log.split('\n') if 'Warning' in line or 'Overfull' in line or 'Underfull' in line]
    results['second_pass_warnings'] = warnings
    results['all_checks_passed'] = all(x['passed'] for x in results['checks'])
    (CHECKS / 'commands.json').write_text(json.dumps(commands, indent=2) + '\n')
    (CHECKS / 'check-report.json').write_text(json.dumps(results, indent=2) + '\n')
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name != 'artifact-manifest.json')
    manifest = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())} for p in files]
    (ROOT / 'artifact-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({'all_checks_passed': results['all_checks_passed'], 'artifact_checks': len(results['checks']), 'source_excerpts': excerpt_count, 'tex_returncodes': [r['returncode'] for r in results['tex_runs']], 'second_pass_warnings': warnings, 'pdf_bytes': pdf.stat().st_size, 'mathematical_status': status['status']}, indent=2))

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(type(exc).__name__ + ': ' + str(exc), file=sys.stderr)
        raise
