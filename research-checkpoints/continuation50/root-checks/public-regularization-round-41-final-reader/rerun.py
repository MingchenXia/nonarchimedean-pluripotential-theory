#!/usr/bin/env python3
"""Regenerate standalone TeX and retain both actual TeX build diagnostics."""
from pathlib import Path
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / 'build'
DIAG = ROOT / 'diagnostics'
BUILD.mkdir(exist_ok=True)
DIAG.mkdir(exist_ok=True)

def run(command, output):
    result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True)
    (DIAG / output).write_text(result.stdout)
    return {'command':command, 'exit_code':result.returncode,
            'output_file':str(Path('diagnostics')/output)}

assert (ROOT/'input.json').read_bytes() == (ROOT/'input-original.json').read_bytes()
original_input = json.loads((ROOT/'input.json').read_bytes())
assert (ROOT/'assignment-original.txt').read_text() == original_input['assignment']
assert json.loads((ROOT/'task-original.json').read_text()) == original_input['task']
versions = {'python':sys.version, 'platform':platform.platform()}
for executable in ['pdflatex', 'pandoc', 'pdftotext', 'pdfinfo']:
    versions[executable+'_path'] = shutil.which(executable)
    flag = '-v' if executable in ['pdftotext','pdfinfo'] else '--version'
    p = subprocess.run([executable,flag],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    versions[executable+'_version'] = p.stdout.splitlines()[:3]

diag_run = run([sys.executable, 'graph_diagnostic.py'], 'graph-run.txt')
assert diag_run['exit_code'] == 0
conversion = run(['pandoc','P02.1-argument.md','--standalone','--from=markdown+tex_math_dollars',
                  '--to=latex','--pdf-engine=pdflatex','-V','geometry:margin=1in',
                  '-V','fontsize:11pt','-o','P02.1-paper.tex'], 'pandoc-output.txt')
assert conversion['exit_code'] == 0
command = ['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
           '-output-directory=build','P02.1-paper.tex']
passes = []
for number in [1,2]:
    info = run(command, f'tex-pass-{number}.txt')
    logfile = BUILD / 'P02.1-paper.log'
    if logfile.exists():
        retained = DIAG / f'tex-pass-{number}.log'
        shutil.copyfile(logfile, retained)
        log = logfile.read_text(errors='replace')
        info['retained_log'] = str(retained.relative_to(ROOT))
        info['diagnostic_lines'] = [s for s in log.splitlines()
                                    if re.search(r'Warning|Overfull|Underfull|^!|^Output written',s)]
    passes.append(info)
pdfinfo = run(['pdfinfo','build/P02.1-paper.pdf'], 'pdfinfo.txt') if (BUILD/'P02.1-paper.pdf').exists() else None
hashes = {}
for filename in ['input.json','input-original.json','assignment-original.txt','task-original.json',
                 'P02.1-argument.md','P02.1-paper.tex','build/P02.1-paper.pdf']:
    p = ROOT / filename
    if p.exists(): hashes[filename] = hashlib.sha256(p.read_bytes()).hexdigest()
report = {'environment':versions, 'input_byte_identity':True,
          'graph_diagnostic':diag_run, 'pandoc':conversion, 'tex_passes':passes,
          'pdfinfo':pdfinfo, 'artifact_sha256':hashes,
          'requested_model':'Native Codex gpt-6.1-sol/xhigh was requested in the assignment; '
                            'the execution environment exposes no local model attestation, '
                            'and no model/worker was invoked.',
          'runtime_status':'cloud environment_status tool was not exposed; no runtime configuration was changed.',
          'compute':'Only short local source handling, exact small finite diagnostics, and TeX builds. '
                    'No resource-heavy computation required or launched.',
          'limits':'Execution and build success are not mathematical verification.'}
(DIAG/'build-diagnostics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'pandoc_exit':conversion['exit_code'],
                  'tex_passes':[{'exit':p['exit_code'],'diagnostics':p.get('diagnostic_lines',[])} for p in passes],
                  'input_byte_identity':True},indent=2))
if any(p['exit_code'] for p in passes): raise SystemExit(1)
