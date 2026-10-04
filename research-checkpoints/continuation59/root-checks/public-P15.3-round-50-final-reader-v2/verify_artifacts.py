#!/usr/bin/env python3
"""Documentary checks only: no claim of mathematical verification."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

frozen = json.loads((root/'input-preservation.json').read_text())
for name in ['input.json','input-original.json','assignment-original.txt','task-original.json']:
    assert sha(root/name) == frozen[name], name
assert (root/'input.json').read_bytes() == (root/'input-original.json').read_bytes()
original = json.loads((root/'input.json').read_bytes())
assert (root/'assignment-original.txt').read_bytes() == original['assignment'].encode('utf-8')
assert json.loads((root/'task-original.json').read_bytes()) == original['task']
print('PASS: four frozen inputs; input copy byte-identical; assignment exact; task semantically exact.')

provenance = json.loads((root/'source-extracts/source-provenance.json').read_text())
for source in provenance['sources']:
    full_path = root/source['byte_identical_local_extract']
    assert sha(full_path) == source['extract_sha256']
    assert sha(Path(source['supplied_extract_location'])) == source['extract_sha256']
    assert sha(Path(source['pdf_location'])) == source['pdf_sha256']
    lines = full_path.read_text().split('\n')
    assert len(lines) == source['source_line_count']
    for passage in source['passages']:
        literal = '\n'.join(lines[passage['first_line']-1:passage['last_line']])
        assert literal == passage['literal']
        assert (root/passage['local_file']).read_bytes() == literal.encode('utf-8')
        assert sha(root/passage['local_file']) == passage['sha256']
    print(f"PASS: {source['id']} {source['exact_arxiv_version']}; {len(lines)} LF lines; {len(source['passages'])} literal passages; PDF/text hashes.")

status = json.loads((root/'status.json').read_text())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id'] == 'P15.3' and status['status'] == 'partial'
assert (root/status['proof_file']).is_file()
assert len(status['concrete_gaps']) == 6
print('PASS: exact five-field status schema; partial status; six concrete general gaps.')

builds = json.loads((root/'build-results.json').read_text())
assert len(builds['builds']) == 2
assert not builds['mathematical_verification']
for build in builds['builds']:
    assert build['returncode'] == 0
    for key in ['stdout','stderr','tex_log']:
        assert (root/build[key]).is_file()
    log = (root/build['tex_log']).read_text(errors='replace')
    assert 'Output written on P15.3-paper.pdf' in log
    warnings = [line for line in log.split('\n') if re.search(r'Warning|Overfull|Underfull',line)]
    print(f"PASS: build {build['build']} exit 0; preserved stdout/stderr/TeX log; diagnostic warnings={len(warnings)}.")
    for warning in warnings:
        print('  '+warning)
assert sha(root/'P15.3-paper.pdf') == builds['pdf_sha256']

artifacts = []
for p in sorted(root.rglob('*')):
    if not p.is_file() or any(part.startswith('.') for part in p.relative_to(root).parts):
        continue
    if p.name in ['artifact-manifest.json','verification.stdout','verification.stderr']:
        continue
    artifacts.append(dict(file=str(p.relative_to(root)),bytes=p.stat().st_size,sha256=sha(p)))
(root/'artifact-manifest.json').write_text(json.dumps(dict(mathematical_verification=False,artifacts=artifacts),indent=2)+'\n')
print(f'PASS: manifest records {len(artifacts)} visible artifact hashes; verification streams excluded to avoid self-reference.')
print('Mathematical status: unverified draft; restricted theorem only; original P15.3 remains unresolved; candidate=false.')
