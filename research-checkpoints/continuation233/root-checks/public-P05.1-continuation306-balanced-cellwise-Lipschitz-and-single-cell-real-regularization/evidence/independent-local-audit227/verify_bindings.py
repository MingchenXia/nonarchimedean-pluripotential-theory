"""Own immutable binding verification; no historical program is executed.

Usage: python verify_bindings.py FRESH_REPORT.json
All inputs are the three supplied immutable packet manifests. No unbound path is followed.
"""
import hashlib
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
base = root.parent.parent
names = {'math': 'mathematical-packet-bindings.json',
         'evidence': 'historical-own-evidence-bindings.json',
         'primary': 'private-primary-packet-bindings.json'}
inputs = root / 'inputs'
inputs.mkdir(exist_ok=True)
rows = []
manifests = []
for kind, name in names.items():
    b = (base / name).read_bytes()
    target = inputs / name
    if not target.exists():
        target.write_bytes(b)
    else:
        assert target.read_bytes() == b
    manifests.append({'kind': kind, 'filename': name, 'bytes': len(b),
                      'sha256': hashlib.sha256(b).hexdigest()})
    for index, r in enumerate(json.loads(b)):
        data = Path(r['path']).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        match = len(data) == r['bytes'] and digest == r['sha256']
        rows.append({'kind': kind, 'index': index, 'path': r['path'],
                     'bytes': len(data), 'sha256': digest,
                     'literal_LF': data.count(b'\n'), 'match': match})
out = Path(sys.argv[1])
with out.open('x') as f:
    json.dump({'manifests': manifests, 'all_match': all(r['match'] for r in rows),
               'counts': {k: sum(r['kind'] == k for r in rows) for k in names},
               'rows': rows}, f, indent=2)
    f.write('\n')
print('bindings', len(rows), 'matching', sum(r['match'] for r in rows))
