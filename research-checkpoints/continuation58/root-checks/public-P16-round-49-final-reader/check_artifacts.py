#!/usr/bin/env python3
"""Requested provenance/format checks only; explicitly not mathematical validation."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
original = (root/'input.json').read_bytes()
data = json.loads(original)
assert original == (root/'input-original.json').read_bytes()
assert (root/'assignment-original.txt').read_text() == data['assignment']
assert json.loads((root/'task-original.json').read_bytes()) == data['task']
status = json.loads((root/'status.json').read_bytes())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id'] == 'P16.3' and status['status'] == 'partial'
assert len(status['concrete_gaps']) == 3
provenance = json.loads((root/'source-extracts/source-provenance.json').read_bytes())
assert len(provenance['sources']) == 11
count = 0
for source in provenance['sources']:
    textfile = next(f for f in source['files'] if f['kind']=='literal_extract')
    source_text = Path(textfile['path']).read_text()
    source_lines = source_text.split('\n')
    for extract in source['literal_extracts']:
        payload = (root/extract['filename']).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == extract['sha256']
        assert payload.decode() == extract['literal_text']
        expected = '\n'.join(source_lines[extract['source_line_first']-1:extract['source_line_last']])+'\n'
        assert expected == extract['literal_text']
        assert extract['literal_text'] in source_text
        count += 1
build = json.loads((root/'build/build-results.json').read_bytes())
assert len(build['passes']) == 2
assert all(p['returncode']==0 for p in build['passes'])
assert hashlib.sha256((root/'P16.3-paper.tex').read_bytes()).hexdigest() == build['tex_sha256']
assert hashlib.sha256((root/'build/P16.3-paper.pdf').read_bytes()).hexdigest() == build['pdf_sha256']
assert (root/'P16.3-paper.tex').read_text().count('\\section{') == 11
assert '\\input{' not in (root/'P16.3-paper.tex').read_text()
for p in build['passes']:
    assert (root/p['stdout']).exists() and (root/p['stderr']).exists() and (root/p['tex_log']).exists()
    log = (root/p['tex_log']).read_text()
    assert 'Output written on' in log
    assert 'Overfull \\hbox' not in log
result = {'input_original_byte_identical': True, 'decoded_inputs_match': True,
          'status_keys_exact': True, 'source_count': 11, 'literal_extracts_checked': count,
          'tex_pass_returncodes': [p['returncode'] for p in build['passes']],
          'standalone_tex_sections': 11, 'overfull_boxes': 0,
          'mathematical_correctness_verified': False, 'candidate': False}
(root/'artifact-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
