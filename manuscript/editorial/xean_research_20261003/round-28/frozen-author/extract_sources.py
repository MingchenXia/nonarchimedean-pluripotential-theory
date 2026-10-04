#!/usr/bin/env python3
"""Preserve the supplied input/proposal and exact LF primary bodies locally."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
input_bytes = (root / 'input.json').read_bytes()
data = json.loads(input_bytes)
(root / 'original-input.json').write_bytes(input_bytes)
for name, string in [
    ('original-problem.txt', data['task']['problem']),
    ('original-completion-criteria.txt', data['task']['completionCriteria']),
    ('original-assignment.txt', data['assignment']),
]:
    (root / name).write_text(string)
proposal = Path('/workspace/research/P15-zero-volume-fibration-proposal.md')
(root / 'operator-proposal-original.md').write_bytes(proposal.read_bytes())
source = Path('/workspace/research/shared-sources/BEGZ-0812.3674v2-20261004.txt')
raw = source.read_bytes()
lines = raw.split(b'\n')  # Deliberately not splitlines(): formfeeds are retained.
blocks = []
for first, last, tag in [
    (175,188,'bounded'), (189,242,'nonpluripolar'), (249,322,'properties'),
    (626,762,'ibp'), (810,840,'nef'), (1120,1222,'energy'),
    (2520,2540,'bibliography'),
]:
    body = b'\n'.join(lines[first-1:last])
    name = f'BEGZ-LF{first}-{last}-{tag}.txt'
    (root / name).write_bytes(body)
    blocks.append({'file': name, 'source': str(source), 'first_LF_line': first,
                   'last_LF_line': last, 'sha256': hashlib.sha256(body).hexdigest(),
                   'extraction': 'bytes.split(b"\\n")[first-1:last], joined by LF, no appended terminal LF; formfeeds retained'})
pdf = Path('/workspace/research/shared-sources/BEGZ-0812.3674v2-20261004.pdf')
manifest = {
    'primary_text': {'path': str(source), 'sha256': hashlib.sha256(raw).hexdigest()},
    'primary_pdf': {'path': str(pdf), 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest()},
    'excerpts': blocks,
    'proposal_sha256': hashlib.sha256(proposal.read_bytes()).hexdigest(),
    'original_input_sha256': hashlib.sha256(input_bytes).hexdigest(),
}
(root / 'source-provenance.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'extracted_bodies': len(blocks), 'supplied_units': 6,
                  'method': 'literal LF bytes; no appended terminal LF',
                  'writes': 'assigned workspace only'}, indent=2))
