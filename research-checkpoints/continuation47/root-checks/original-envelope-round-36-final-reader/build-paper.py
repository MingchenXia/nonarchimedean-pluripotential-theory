#!/usr/bin/env python3
"""Build twice using existing TeX, recording actual commands and diagnostics."""
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

engine = shutil.which('pdflatex')
record = {'engine': engine, 'runs': [], 'installed_anything': False}
if engine is not None:
    for run in (1, 2):
        cmd = [engine, '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'P03.3-paper.tex']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        log_name = f'build-pass-{run}.stdout.txt'
        Path(log_name).write_text(result.stdout + result.stderr)
        tex_log_name = f'build-pass-{run}.tex.log'
        if Path('P03.3-paper.log').exists():
            shutil.copyfile('P03.3-paper.log', tex_log_name)
        record['runs'].append({'run': run, 'command': cmd, 'exit_code': result.returncode,
                               'stdout_stderr_file': log_name, 'tex_log_file': tex_log_name,
                               'diagnostics': [line for line in (result.stdout + result.stderr).splitlines()
                                               if any(x in line for x in ['Warning', 'Overfull', 'Underfull', 'Error', 'Output written'])]})
    record['both_passes_succeeded'] = all(r['exit_code'] == 0 for r in record['runs'])
else:
    record['both_passes_succeeded'] = False
    record['missing_facility'] = 'No existing pdflatex; no installation attempted.'
Path('build-record.json').write_text(json.dumps(record, indent=2) + '\n')
environment = {'python': sys.version, 'platform': platform.platform(),
               'tools': {n: shutil.which(n) for n in ['python','pandoc','pdflatex','pdftotext']},
               'execution': 'small local exact-rational finite graphs; no resource-heavy compute',
               'environment_settings_changed': False, 'external_model_or_worker_invocations': 0}
for tool in ['pandoc', 'pdflatex']:
    p = shutil.which(tool)
    if p:
        r = subprocess.run([p, '--version'], capture_output=True, text=True, timeout=10)
        environment[tool + '_version'] = r.stdout.splitlines()[0]
Path('environment.json').write_text(json.dumps(environment, indent=2) + '\n')
print(json.dumps(record, indent=2))
if engine and not record['both_passes_succeeded']:
    sys.exit(1)
