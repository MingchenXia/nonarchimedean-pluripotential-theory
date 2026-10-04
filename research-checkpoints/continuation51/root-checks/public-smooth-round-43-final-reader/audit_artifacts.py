#!/usr/bin/env python3
"""Check the required deliverable structure, not mathematical validity."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

inp = json.loads((ROOT / 'input-original.json').read_text())
status = json.loads((ROOT / 'status.json').read_text())
generation = json.loads((ROOT / 'paper-generation.json').read_text())
build = json.loads((ROOT / 'build-diagnostics.json').read_text())
checks = {
    'input_byte_identical': (ROOT/'input.json').read_bytes() == (ROOT/'input-original.json').read_bytes(),
    'assignment_exact': (ROOT/'assignment-original.txt').read_text() == inp['assignment'],
    'task_semantically_exact': json.loads((ROOT/'task-original.json').read_text()) == inp['task'],
    'status_exact_keys': set(status) == {'id','status','exact_result','proof_file','concrete_gaps'},
    'markdown_synchronized': digest(ROOT/'P02.3-argument.md') == generation['markdown_sha256'],
    'tex_synchronized': digest(ROOT/'P02.3-paper.tex') == generation['tex_sha256'],
    'standalone_tex': r'\input{' not in (ROOT/'P02.3-paper.tex').read_text(),
    'two_actual_builds': len(build['builds']) == 2,
    'both_builds_successful': build['both_successful'],
    'seven_source_hashes_match': all(r['pdf_hash_matches'] and r['extract_hash_matches']
                                    for r in json.loads((ROOT/'source-extracts/source-provenance.json').read_text())['sources'])
}
result = {'checks': checks, 'all_passed': all(checks.values()),
          'evidence_scope': 'Artifact structure, exact input preservation, source-byte checks and TeX execution only. This is not proof verification.'}
(ROOT/'artifact-audit.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
if not result['all_passed']:
    raise SystemExit(1)
