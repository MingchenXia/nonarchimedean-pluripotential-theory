#!/usr/bin/env python3
"""Bind final artifact bytes after tee has closed the recorded build output."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
paths = sorted(p for p in root.rglob('*') if p.is_file()
               and p.name != 'artifact-manifest.json' and '.git' not in p.parts)
records = [dict(artifact=str(p.relative_to(root)), bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths]
(root / 'evidence/artifact-manifest.json').write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + '\n')
for record in records:
    data = (root / record['artifact']).read_bytes()
    assert len(data) == record['bytes']
    assert hashlib.sha256(data).hexdigest() == record['sha256']
