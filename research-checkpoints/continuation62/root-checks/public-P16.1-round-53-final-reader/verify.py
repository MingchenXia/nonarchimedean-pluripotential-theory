#!/usr/bin/env python3
"""Finite artifact/provenance checks, not a mathematical correctness verifier."""
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
def read_json(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))
checks = []
def check(name, condition, evidence):
    checks.append({'check': name, 'passed': bool(condition), 'evidence': evidence})
request = read_json('input.json')
check('byte-identical preserved input', (ROOT/'input.json').read_bytes()==(ROOT/'input-original.json').read_bytes(), hashlib.sha256((ROOT/'input.json').read_bytes()).hexdigest())
check('exact original assignment text', (ROOT/'assignment-original.txt').read_text()==request['assignment'], 'text equality')
check('original task object', read_json('task-original.json')==request['task'], 'JSON structural equality')
provenance = read_json('source-extracts/source-provenance.json')
literal_count = 0
for source in provenance['sources']:
    for kind, item in source['files'].items():
        data = (ROOT/item['local_path']).read_bytes()
        check(source['id']+' '+kind+' cache bytes', hashlib.sha256(data).hexdigest()==item['expected_sha256']==item['actual_sha256'], {'bytes': len(data), 'sha256': item['actual_sha256']})
    lines = (ROOT/source['files']['extract']['local_path']).read_bytes().decode('utf-8').split('\n')
    for excerpt in source['excerpts']:
        literal = '\n'.join(lines[excerpt['start_line']-1:excerpt['end_line']])
        check(source['id']+' literal '+excerpt['id'], literal==excerpt['literal_text'] and hashlib.sha256(literal.encode()).hexdigest()==excerpt['literal_sha256'], [excerpt['start_line'],excerpt['end_line']])
        literal_count += 1
status = read_json('status.json')
check('exact status fields', set(status)=={'id','status','exact_result','proof_file','concrete_gaps'}, sorted(status))
build = read_json('build-results.json')
check('conversion and both TeX runs succeeded', len(build)==3 and all(item['returncode']==0 for item in build), [item['returncode'] for item in build])
check('separate actual TeX logs', all((ROOT/f'tex-run-{i}.log').is_file() for i in (1,2)), 'tex-run-1.log and tex-run-2.log')
check('standalone paper and compiled PDF', (ROOT/'P16.1-paper.tex').read_text().startswith('\\documentclass') and (ROOT/'P16.1-paper.pdf').read_bytes().startswith(b'%PDF-'), 'standalone LaTeX source and PDF signature')
summary = {'epistemic_scope': 'These checks establish preservation, literal extraction replay, schema and execution success; they do not establish mathematical correctness, novelty, or independent source certification.', 'literal_excerpt_count': literal_count, 'checks': checks, 'all_passed': all(c['passed'] for c in checks)}
(ROOT/'checks.json').write_text(json.dumps(summary,indent=2)+'\n')
hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.rglob('*')) if p.is_file() and not any(part.startswith('.') for part in p.relative_to(ROOT).parts) and p.name != 'artifact-hashes.json'}
(ROOT/'artifact-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'literal_excerpts':literal_count,'all_passed':summary['all_passed'],'hashed_artifacts':len(hashes)},indent=2))
if not summary['all_passed']:
    raise SystemExit(1)
