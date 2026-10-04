#!/usr/bin/env python3
"""Rerun the authorized lightweight checks, generate TeX, and build twice."""
import hashlib
import json
import platform
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BUILD = ROOT/'build'
BUILD.mkdir(exist_ok=True)

def run(label, argv):
    result = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True)
    (BUILD/f'{label}.stdout.txt').write_text(result.stdout)
    (BUILD/f'{label}.stderr.txt').write_text(result.stderr)
    record = {'command': argv, 'cwd': str(ROOT), 'returncode': result.returncode,
              'stdout_file': f'build/{label}.stdout.txt',
              'stderr_file': f'build/{label}.stderr.txt'}
    (BUILD/f'{label}.command.json').write_text(json.dumps(record, indent=2)+'\n')
    print(label, 'returncode', result.returncode)
    return record

versions = {}
for exe, flag in [('pdflatex','--version'), ('pandoc','--version'), ('pdftotext','-v')]:
    loc = shutil.which(exe)
    if loc:
        r = subprocess.run([loc,flag],capture_output=True,text=True)
        versions[exe] = {'path': loc, 'version_output': r.stdout+r.stderr}
    else:
        versions[exe] = {'path': None}
env = {'platform': platform.platform(), 'python': sys.version,
       'executables': versions, 'cwd': str(ROOT),
       'execution': 'No external model, worker, subagent, network request, installation, or heavy computation. Only authorized source caches and fresh workspace files were read.',
       'supervised_compute': 'Not needed for these lightweight text, exact-arithmetic and TeX operations.'}
(ROOT/'environment.json').write_text(json.dumps(env,indent=2)+'\n')

records = []
records.append(run('sources', [sys.executable, 'audit_sources.py']))
records.append(run('finite-tree', [sys.executable, 'finite_tree_checks.py']))
records.append(run('pandoc', ['pandoc','P16.4-argument.md', '--standalone',
                              '--from=markdown+tex_math_dollars', '--to=latex',
                              '--output=P16.4-paper.tex']))
for passno in [1,2]:
    records.append(run(f'tex-pass-{passno}',
                       ['pdflatex','-no-shell-escape','-interaction=nonstopmode',
                        '-halt-on-error','-file-line-error','-output-directory=build',
                        'P16.4-paper.tex']))
    for ext in ['log','aux','out']:
        src=BUILD/f'P16.4-paper.{ext}'
        if src.exists():
            shutil.copyfile(src, BUILD/f'tex-pass-{passno}.{ext}')
pdf = BUILD/'P16.4-paper.pdf'
if pdf.exists():
    shutil.copyfile(pdf, ROOT/pdf.name)
    records.append(run('pdfinfo', ['pdfinfo', 'P16.4-paper.pdf']))

inp=(ROOT/'input.json').read_bytes()
orig=(ROOT/'input-original.json').read_bytes()
original=json.loads(orig)
retained=json.loads((ROOT/'task-original.json').read_text())
assert retained == original['task']
assert (ROOT/'assignment-original.txt').read_text() == original['assignment']
checks={'input_original_byte_identical':inp == orig,
        'input_sha256':hashlib.sha256(inp).hexdigest(),
        'task_semantically_identical':True, 'assignment_string_identical':True,
        'commands':records,
        'all_commands_successful':all(r['returncode']==0 for r in records),
        'candidate':False,
        'evidence_class': 'File integrity, exact finite observations and actual build diagnostics; not mathematical certification.'}
(ROOT/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')

status={'id':'P16.4', 'status':'partial',
        'exact_result':'Unverified partial proof: over algebraically closed complete nontrivially real-valued non-Archimedean K of residue characteristic zero, X=P^1_K and L=O(d), d>=1, the genuine finite-energy operator is constructed for all-support positive Radon measures of raw mass d and dual energy J=I/2<infinity. Existence and uniqueness modulo constants, decreasing continuity, reference independence, energy differentiation and comparison are proved by the rooted Green kernel. General smooth projective varieties and arbitrary non-algebraically-closed fields remain unresolved here.',
        'proof_file':'P16.4-argument.md',
        'concrete_gaps':[
            'Identify actual unbounded psh potentials and approximation-independent full-mass genuine mixed MA measures in the general nondiscrete field setting.',
            'Supply normalized potential compactness and extraction of finite-energy actual maximizing metrics, beyond weak/quasi-metric compactness of measures.',
            'Supply envelope/obstacle regularity or a proved alternative, and link available synthetic orthogonality to actual unbounded potentials.',
            'Prove unbounded energy differentiation and obstacle variations against all continuous tests for that actual operator.',
            'Prove finite-energy comparison/domination or equivalent injectivity estimates in the general field setting.',
            'Prove any field-extension/descent steps preserving the polarization, raw mass, psh, energy, derivatives and comparison; none are asserted here.'
        ]}
assert set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}
(ROOT/'status.json').write_text(json.dumps(status,indent=2)+'\n')

artifacts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='artifact-manifest.json' and not p.is_relative_to(ROOT/'.git'):
        artifacts.append({'file':str(p.relative_to(ROOT)), 'bytes':p.stat().st_size,
                          'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'artifact-manifest.json').write_text(json.dumps(artifacts,indent=2)+'\n')
print('Byte-identical original:',checks['input_original_byte_identical'])
print('All commands successful:',checks['all_commands_successful'])
print('Mathematical status: partial; candidate=false.')
if not checks['all_commands_successful']:
    raise SystemExit(1)
