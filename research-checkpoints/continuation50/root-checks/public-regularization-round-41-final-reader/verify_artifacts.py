#!/usr/bin/env python3
"""Artifact/schema checks only, explicitly excluding mathematical validation."""
from pathlib import Path
import hashlib
import json
import fitz

root = Path(__file__).resolve().parent
status = json.loads((root/'status.json').read_text())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id'] == 'P02.1' and status['status'] == 'partial'
raw = (root/'input.json').read_bytes()
assert raw == (root/'input-original.json').read_bytes()
original = json.loads(raw)
assert original['assignment'] == (root/'assignment-original.txt').read_text()
assert original['task'] == json.loads((root/'task-original.json').read_text())
provenance = json.loads((root/'source-extracts/source-provenance.json').read_text())
literal_count = 0
for source in provenance['sources']:
    if not source['selected_pdf_pages']:
        continue
    selected = fitz.open(root/'source-extracts'/(source['id']+'-selected-pages.pdf'))
    assert len(selected) == len(source['selected_pdf_pages'])
    raw_pages = Path(source['source_literal_extract']).read_bytes().split(b'\x0c')
    for page in source['literal_page_files']:
        data = (root/'source-extracts'/page['literal_file']).read_bytes()
        assert data == raw_pages[page['original_pdf_page']-1]
        assert hashlib.sha256(data).hexdigest() == page['literal_sha256']
        literal_count += 1
build = json.loads((root/'diagnostics/build-diagnostics.json').read_text())
assert all(x['exit_code']==0 for x in build['tex_passes'])
assert len(build['tex_passes'])==2
pdf = fitz.open(root/'build/P02.1-paper.pdf')
assert len(pdf)==11
text = ' '.join(' '.join(p.get_text().split()) for p in pdf)
for phrase in ['The original higher-dimensional characterization remains open',
               'Every analytic scalar extension', 'finite', 'second',
               'Successful extraction', 'network operation is used']:
    if phrase == 'Every analytic scalar extension':
        assert 'every analytic scalar extension' in text.lower()
    else:
        assert phrase in text, phrase
report = {'kind':'artifact consistency only', 'input_byte_identity':True,
          'assignment_string_identity':True,'task_object_identity':True,
          'status_exact_keys':list(status),'literal_pages_verified':literal_count,
          'source_hash_matches':len(provenance['sources']),
          'tex_pass_exit_codes':[p['exit_code'] for p in build['tex_passes']],
          'pdf_pages':len(pdf), 'pdf_text_scope_statements_retained':True,
          'limits':'These checks do not establish mathematical correctness.'}
(root/'diagnostics/artifact-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
