#!/usr/bin/env python3
"""Bounded local rerun; preserve two actual compiler runs and their logs."""
import hashlib
import json
import shutil
import subprocess
import time
from pathlib import Path

root = Path(__file__).resolve().parent
runs = []
def run(cmd, tag):
    started = time.time()
    p = subprocess.run(cmd, cwd=root, capture_output=True)
    (root / f'{tag}.stdout.txt').write_bytes(p.stdout)
    (root / f'{tag}.stderr.txt').write_bytes(p.stderr)
    rec = {'command':cmd,'cwd':str(root),'returncode':p.returncode,
           'elapsed_seconds':round(time.time()-started,6),
           'stdout':f'{tag}.stdout.txt','stderr':f'{tag}.stderr.txt'}
    runs.append(rec)
    return p

for cmd, tag in [(['python3','audit_sources.py'],'source-audit'),
                 (['python3','check_partial_results.py'],'partial-checks')]:
    p = run(cmd,tag)
    if p.returncode:
        raise RuntimeError(f'{tag} failed; preserved actual stdout/stderr')

for i in [1,2]:
    p = run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P13.1-paper.tex'],f'tex-build-{i}')
    log = root / 'P13.1-paper.log'
    if log.exists():
        shutil.copyfile(log,root / f'tex-build-{i}.log')
        runs[-1]['actual_TeX_log'] = f'tex-build-{i}.log'
    if p.returncode:
        (root/'run-results.json').write_text(json.dumps(runs,indent=2)+'\n')
        raise RuntimeError(f'TeX run {i} failed; actual output preserved')

(root/'run-results.json').write_text(json.dumps(runs,indent=2)+'\n')
status = {'id':'P13.1','status':'partial',
    'exact_result':'Direct presentation-independent order bijections of actual H/CPSH/PSH spaces for all Reeb fields, explicit pointwise and fixed-measure bounds, quantitative nonnegative cumulative-filtration S comparison, carrier-only density, and a conditional quantified envelope transfer. Finite-energy cross-Reeb control and uniform energy differentiation are not proved.',
    'proof_file':'P13.1-argument.md',
    'concrete_gaps':[
        'No proof that root transport preserves E^1 or any cross-Reeb energy estimate independent of bounded truncation.',
        'No uniformly integrable moving mixed-MA tails or actual cross-Reeb finite-energy limiting passage.',
        'No established cone obstacle orthogonality/energy extension with the required uniform derivative remainder.',
        'Projective envelope transfer depends on unestablished indispensable imports and proof reductions in Lyuhui Wu 2609.27610v1, including APW26b local assertions and the unrestricted-field base-change step.'
    ]}
(root/'status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
assert (root/'input.json').read_bytes()==(root/'input-original.json').read_bytes()
d=json.loads((root/'input.json').read_text())
assert (root/'assignment-original.txt').read_text()==d['assignment']
assert json.loads((root/'task-original.json').read_text())==d['task']
manifest=[]
for path in sorted(root.rglob('*')):
    if path.is_file() and not any(x.startswith('.') for x in path.relative_to(root).parts) and path.name!='artifact-manifest.json':
        raw=path.read_bytes()
        manifest.append({'file':str(path.relative_to(root)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
(root/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':status['status'],'input_original_byte_identical':True,
    'source_audit_exit':runs[0]['returncode'],'partial_checks_exit':runs[1]['returncode'],
    'TeX_exit_codes':[r['returncode'] for r in runs[2:]],
    'pdf_bytes':(root/'P13.1-paper.pdf').stat().st_size,
    'mathematical_correctness_verified_by_execution':False},indent=2))
