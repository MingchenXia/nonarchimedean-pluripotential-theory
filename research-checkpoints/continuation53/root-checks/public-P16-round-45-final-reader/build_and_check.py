#!/usr/bin/env python3
"""Build twice with existing TeX; retain actual diagnostics and artifact checks."""
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
build = ROOT / 'build'
build.mkdir(exist_ok=True)
commands = []

def run(cmd, label):
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    (build / (label + '.stdout.txt')).write_text(result.stdout)
    (build / (label + '.stderr.txt')).write_text(result.stderr)
    commands.append({'argv': cmd, 'cwd': str(ROOT), 'returncode': result.returncode,
                     'stdout': str((build / (label + '.stdout.txt')).relative_to(ROOT)),
                     'stderr': str((build / (label + '.stderr.txt')).relative_to(ROOT))})
    return result

first = run([sys.executable, 'make_paper.py'], 'make-paper')
if first.returncode:
    raise RuntimeError(first.stderr)
tex_command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', '-output-directory=build', 'P16.1-paper.tex']
tex_results = []
for i in [1, 2]:
    result = run(tex_command, f'tex-pass-{i}')
    log = build / 'P16.1-paper.log'
    if log.exists():
        (build / f'tex-pass-{i}.log').write_bytes(log.read_bytes())
    tex_results.append(result)

arithmetic = run([sys.executable, 'curve_checks.py'], 'curve-checks')
status = json.loads((ROOT / 'status.json').read_text())
expected = {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert set(status) == expected
original_equal = (ROOT / 'input.json').read_bytes() == (ROOT / 'input-original.json').read_bytes()
assert original_equal
parsed = json.loads((ROOT / 'input.json').read_text())
assert (ROOT / 'assignment-original.txt').read_text() == parsed['assignment']
assert json.loads((ROOT / 'task-original.json').read_text()) == parsed['task']
assert (ROOT / status['proof_file']).is_file()
provenance = json.loads((ROOT / 'source-extracts/source-provenance.json').read_text())
assert len(provenance['inventory']) == 10
assert all(c['matches_supplied'] for r in provenance['inventory'] for c in r['checks'].values())
assert all(r.returncode == 0 for r in tex_results)
assert arithmetic.returncode == 0

files = ['input.json', 'input-original.json', 'assignment-original.txt', 'task-original.json',
         'P16.1-argument.md', 'P16.1-paper.tex', 'build/P16.1-paper.pdf',
         'source-extracts/source-provenance.json', 'status.json', 'curve-checks.json']
report = {'kind': 'Reproducibility and finite arithmetic checks, not mathematical validation.',
          'input_byte_identical': original_equal, 'assignment_exact': True, 'task_exact': True,
          'status_exact_keys': sorted(status), 'tex_build_returncodes': [r.returncode for r in tex_results],
          'arithmetic_returncode': arithmetic.returncode, 'authorized_cache_hashes_match': True,
          'python': sys.version, 'platform': platform.platform(),
          'commands': commands, 'files': {name: {'bytes': (ROOT / name).stat().st_size,
               'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest()} for name in files}}
(ROOT / 'checks.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in ['files', 'commands']}, indent=2))
