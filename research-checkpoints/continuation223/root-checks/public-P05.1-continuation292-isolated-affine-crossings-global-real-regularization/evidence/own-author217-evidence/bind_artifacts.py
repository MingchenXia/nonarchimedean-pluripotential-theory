"""Bind all own artifacts, including local-only excerpts, without copying source bytes."""
import hashlib
import json
from pathlib import Path

root = Path.cwd()
excluded = {'artifact-bindings.json', 'artifact-bindings.sha256'}
records = []
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name not in excluded:
        data = p.read_bytes()
        name = str(p.relative_to(root))
        records.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                        'distribution': 'LOCALONLY' if name.startswith('LOCALONLY/') else 'own-author-artifact'})
manifest = {'kind': 'own complete artifact bindings; hashes are provenance only', 'candidate': False,
            'root': str(root), 'files': records,
            'self_binding': 'artifact-bindings.sha256 binds the manifest; the two binding files are excluded from recursive self-hashing'}
path = Path('artifact-bindings.json')
path.write_text(json.dumps(manifest, indent=2) + '\n')
Path('artifact-bindings.sha256').write_text(hashlib.sha256(path.read_bytes()).hexdigest() + '  artifact-bindings.json\n')
print('Bound', len(records), 'own files, including explicitly LOCALONLY excerpts.')
