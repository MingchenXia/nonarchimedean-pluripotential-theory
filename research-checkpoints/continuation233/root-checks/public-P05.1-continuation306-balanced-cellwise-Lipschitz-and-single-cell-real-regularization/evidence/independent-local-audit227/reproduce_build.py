"""Own rerun of Markdown -> unchanged standalone TeX -> three no-shell-escape passes.

Does not run the finite checker. Outputs go to a new directory, preserving this audit.
Usage: python reproduce_build.py FRESH_OUTPUT_DIRECTORY
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent
out = Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=False)
(out / 'build').mkdir()
for name in ('argument.md', 'P05.1-paper.tex'):
    shutil.copyfile(root / 'reproduction' / name, out / name)
commands = []
args = ['pandoc', 'argument.md', '--standalone', '--number-sections', '--table-of-contents',
        '--top-level-division=section', '--variable', 'colorlinks=true', '-o', 'generated-paper.tex']
jobs = [('pandoc', args)] + [(f'pass{p}', ['pdflatex', '-no-shell-escape',
         '-interaction=nonstopmode', '-halt-on-error', '-output-directory=build',
         'P05.1-paper.tex']) for p in range(1, 4)]
for name, argv in jobs:
    p = subprocess.run(argv, cwd=out, capture_output=True)
    (out / f'{name}.stdout').write_bytes(p.stdout)
    (out / f'{name}.stderr').write_bytes(p.stderr)
    commands.append({'name': name, 'argv': argv, 'exit_code': p.returncode})
    if name.startswith('pass'):
        shutil.copyfile(out / 'build' / 'P05.1-paper.log', out / f'{name}.tex.log')
    if p.returncode:
        break
exact = (out / 'generated-paper.tex').exists() and (
    out / 'generated-paper.tex').read_bytes() == (out / 'P05.1-paper.tex').read_bytes()
record = {'commands': commands, 'exact_Markdown_to_TeX': exact,
          'TeX_sha256': hashlib.sha256((out / 'P05.1-paper.tex').read_bytes()).hexdigest()}
(out / 'rerun-report.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record))
