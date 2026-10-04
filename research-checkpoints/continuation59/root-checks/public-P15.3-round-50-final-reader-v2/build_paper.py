#!/usr/bin/env python3
"""Run exactly two actual TeX builds, retaining separate diagnostic streams."""
from pathlib import Path
import hashlib
import json
import subprocess
import time

root = Path(__file__).resolve().parent
records = []
for attempt in (1, 2):
    command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', 'P15.3-paper.tex']
    started = time.time()
    result = subprocess.run(command, cwd=root, capture_output=True)
    (root/f'build-{attempt}.stdout').write_bytes(result.stdout)
    (root/f'build-{attempt}.stderr').write_bytes(result.stderr)
    log = root/'P15.3-paper.log'
    if log.exists():
        (root/f'build-{attempt}.log').write_bytes(log.read_bytes())
    records.append(dict(build=attempt, command=command, cwd=str(root),
                        returncode=result.returncode, elapsed_seconds=time.time()-started,
                        stdout=f'build-{attempt}.stdout',stderr=f'build-{attempt}.stderr',
                        tex_log=f'build-{attempt}.log'))
    print(f'build {attempt}: returncode={result.returncode}, stdout={len(result.stdout)} bytes, stderr={len(result.stderr)} bytes')
pdf = root/'P15.3-paper.pdf'
payload = dict(builds=records, mathematical_verification=False,
               pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.exists() else None)
(root/'build-results.json').write_text(json.dumps(payload,indent=2)+'\n')
raise SystemExit(0 if all(r['returncode']==0 for r in records) else 1)
