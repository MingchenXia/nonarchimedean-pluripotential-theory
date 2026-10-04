#!/usr/bin/env python3
"""Read-only source audit. LF means byte 0x0a, not Python splitlines()."""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SOURCE_ROOT = pathlib.Path('/workspace/research/shared-sources')
assignment = (ROOT / 'assignment-original.txt').read_text()
records = []
annex = ['# Immutable primary-source bodies\n',
         'The following are literal LF ranges from the read-only supplied sources. '
         'The supplied range hashes use LF joins without an added final LF. '
         'Form feeds, extraction defects and printed mathematical defects are retained.\n']
for match in re.finditer(r'Source ([^,\n]+), LF(\d+)--(\d+); raw SHA256 ([0-9a-f]+)\.', assignment):
    name, start, end, expected = match.groups()
    path = SOURCE_ROOT / name
    raw = b'\n'.join(path.read_bytes().split(b'\n')[int(start)-1:int(end)])
    observed = hashlib.sha256(raw).hexdigest()
    records.append(dict(file=str(path), lf_start=int(start), lf_end=int(end),
                        supplied_sha256=expected, observed_sha256=observed,
                        match=(observed == expected)))
    annex.append(f'## {name}, LF{start}--{end}\n\nSHA256 `{observed}`; supplied pin matches: {observed == expected}.\n\n```text\n')
    annex.append(raw.decode('utf-8'))
    annex.append('\n```\n')

# Additional directly consulted, essential foundations, beyond the supplied units.
extra = [('BEGZ-0812.3674v2-20261004.txt', 323, 477),
         ('DDNL18-2049-2087-20261004.txt', 350, 369),
         ('Vu-2005.13241v3-20261004.txt', 64, 87)]
for name, start, end in extra:
    path = SOURCE_ROOT / name
    raw = b'\n'.join(path.read_bytes().split(b'\n')[start-1:end])
    observed = hashlib.sha256(raw).hexdigest()
    records.append(dict(file=str(path), lf_start=start, lf_end=end,
                        supplied_sha256=None, observed_sha256=observed, match=None))
    annex.append(f'## Additional foundation: {name}, LF{start}--{end}\n\nSHA256 `{observed}`.\n\n```text\n')
    annex.append(raw.decode('utf-8'))
    annex.append('\n```\n')

(ROOT / 'source-audit.json').write_text(json.dumps(records, indent=2)+'\n')
(ROOT / 'source-bodies.md').write_text('\n'.join(annex))
assert all(r['match'] for r in records if r['supplied_sha256'] is not None)
print('All 14 supplied LF-range SHA256 pins match; 3 extra foundation ranges recorded.')
print('No source file was modified. Printed defects remain in the literal source bodies.')
