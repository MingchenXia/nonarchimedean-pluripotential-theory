#!/usr/bin/env python3
"""Use existing programs only. Preserve real stdout, stderr and both TeX logs."""
import json
import pathlib
import platform
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
def run(args, stem):
    process = subprocess.run(args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (ROOT / (stem+'.stdout.txt')).write_bytes(process.stdout)
    (ROOT / (stem+'.stderr.txt')).write_bytes(process.stderr)
    return {'command': args, 'cwd': str(ROOT), 'returncode': process.returncode, 'stdout_file': stem+'.stdout.txt', 'stderr_file': stem+'.stderr.txt'}

env = {'python': sys.version, 'platform': platform.platform(), 'tools': {}, 'model_identity': 'The API model identity/effort is not observable from the permitted workspace and tool API; no model was invoked or delegated.', 'resources': 'Only small local text, hashing and TeX operations; no supervised compute service needed or available for heavy computation.', 'read_scope': 'input.json, fresh workspace, and the six explicitly authorized primary source cache files only'}
for tool in ['pandoc','pdflatex']:
    env['tools'][tool] = {'path': shutil.which(tool), 'version': subprocess.run([tool,'--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.splitlines()[:2]}
(ROOT / 'environment.json').write_text(json.dumps(env, indent=2)+'\n')
records = []
records.append(run(['pandoc','P16.1-argument.md','--from=markdown+tex_math_dollars','--to=latex','--standalone','--template=paper-template.tex','--output=P16.1-paper.tex'], 'pandoc-run'))
if records[-1]['returncode'] == 0:
    for number in (1,2):
        stem = f'tex-run-{number}'
        record = run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','P16.1-paper.tex'], stem)
        texlog = ROOT / 'P16.1-paper.log'
        if texlog.exists():
            shutil.copyfile(texlog, ROOT / (stem+'.log'))
            record['tex_log_file'] = stem+'.log'
        records.append(record)
(ROOT / 'build-results.json').write_text(json.dumps(records, indent=2)+'\n')
print(json.dumps(records, indent=2))
sys.exit(0 if len(records)==3 and all(r['returncode']==0 for r in records) else 1)
