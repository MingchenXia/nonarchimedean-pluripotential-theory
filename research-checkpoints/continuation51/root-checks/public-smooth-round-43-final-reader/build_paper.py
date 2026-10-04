#!/usr/bin/env python3
"""Run the existing TeX installation twice and retain actual diagnostics."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parent
command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
           '-file-line-error', 'P02.3-paper.tex']
history_path = ROOT / 'build-history.json'
history = json.loads(history_path.read_text()) if history_path.exists() else []
previous = ROOT / 'build-diagnostics.json'
if previous.exists():
    attempt = len(history) + 1
    old = json.loads(previous.read_text())
    for r in old['builds']:
        for key in ('stdout_file', 'log_file'):
            path = ROOT / r[key]
            if path.exists():
                saved = f'build-attempt-{attempt}-' + r[key]
                shutil.copyfile(path, ROOT / saved)
                r[key] = saved
    history.append(old)
    history_path.write_text(json.dumps(history, indent=2) + '\n')
records = []
for stage in (1, 2):
    before = time.monotonic()
    p = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True, timeout=60)
    (ROOT / f'build-{stage}.stdout.txt').write_text(p.stdout)
    logpath = ROOT / 'P02.3-paper.log'
    log = logpath.read_text(errors='replace') if logpath.exists() else ''
    if logpath.exists():
        shutil.copyfile(logpath, ROOT / f'build-{stage}.log')
    diagnostics = [line for line in log.splitlines()
                   if re.search(r'Warning|Error|^!|Overfull|Underfull|Undefined control|Fatal error|^\./.*:\d+:', line)]
    page = re.search(r'Output written on .*?\((\d+) pages?', log)
    records.append({'pass': stage, 'command': command, 'returncode': p.returncode,
                    'elapsed_seconds': round(time.monotonic()-before, 3),
                    'pages': int(page[1]) if page else None,
                    'diagnostics': diagnostics,
                    'stdout_file': f'build-{stage}.stdout.txt',
                    'log_file': f'build-{stage}.log'})
    print(json.dumps(records[-1], indent=2))
(ROOT / 'build-diagnostics.json').write_text(json.dumps({
    'builds': records,
    'both_successful': all(r['returncode'] == 0 for r in records),
    'mathematical_correctness_established': False
}, indent=2) + '\n')
