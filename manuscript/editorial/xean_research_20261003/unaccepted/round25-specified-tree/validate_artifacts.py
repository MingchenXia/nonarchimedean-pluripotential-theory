#!/usr/bin/env python3
"""Integrity and packaging checks, never a mathematical verifier."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent

def sha(b):
    return hashlib.sha256(b).hexdigest()

for m in json.loads((root/'evidence/input-inventory.json').read_text()):
    assert sha(Path(m['path']).read_bytes()) == m['sha256'], m['path']
canonical = json.loads((root/'evidence/round23-canonical-notes.json').read_text())
assert len(canonical) == 3
run = json.loads(Path('/workspace/research/campaigns/round-23/P06.2-curve-two-sign-source-repair/run.json').read_text())
assert canonical == run['campaign']['result']['notes']
for m in json.loads((root/'evidence/source-selections.json').read_text()):
    data = Path(m['source']).read_bytes()
    assert sha(data) == m['source_sha256']
    body = b'\n'.join(data.split(b'\n')[m['first_lf_line']-1:m['last_lf_line']])
    assert sha(body) == m['body_sha256']
    assert body == (root/m['local_selection']).read_bytes()
status = json.loads((root/'status.json').read_text())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert status['id'] == 'P06.2' and status['status'] == 'partial'
assert status['proof_file'] == 'P06.2-argument.md'
notes = json.loads((root/'notes.json').read_text())
assert not notes['candidate'] and len(notes['notes']) == 3
for i,n in enumerate(notes['notes'],1):
    assert set(n) == {'id','summary','detailedSummary','text','support'}
    assert n['id'] == f'n{i}'
    assert all(s in [f'n{j}' for j in range(1,i)] for s in n['support'])
argument = (root/'P06.2-argument.md').read_text()
assert (root/'P06.2-partial.tex').read_text() in argument
for passno in (1,2):
    log = (root/f'build/pass{passno}.stdout').read_text()
    assert 'Output written on build/P06.2-partial.pdf' in log
    assert not re.search(r'LaTeX Error|Emergency stop|Fatal error',log)
    if passno == 2:
        assert 'undefined' not in log
pdf = root/'P06.2-partial.pdf'
assert pdf.read_bytes().startswith(b'%PDF-')
result = dict(immutable_input_hashes_unchanged=True,
              canonical_round23_notes=3,
              selected_body_hashes_match=True,
              exact_five_key_status=True,
              candidate=False,
              full_new_paper_body_in_authoritative_argument=True,
              successful_pdf_passes=2,
              missing_mathematical_verifier=True,
              mathematical_correctness_certified=False)
(root/'evidence/validation-output.json').write_text(json.dumps(result,indent=2)+'\n')
paths = sorted(p for p in root.rglob('*') if p.is_file()
               and '.git' not in p.parts
               and p != root/'evidence/artifact-hashes.json')
hashes = {str(p.relative_to(root)):sha(p.read_bytes()) for p in paths}
(root/'evidence/artifact-hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(json.dumps(result,indent=2))
