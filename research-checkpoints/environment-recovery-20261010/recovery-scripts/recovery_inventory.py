from pathlib import Path
import json, hashlib
repo = Path('/workspace/recovered-research-repository')
base = repo / 'manuscript/editorial/xean_research_20261003'
manifests = sorted(base.glob('UPLOAD_MANIFEST*.json'))
summary = []
for path in manifests:
    data = json.loads(path.read_text())
    summary.append({'name': path.name, 'keys': list(data), 'files': len(data.get('files', [])), 'array_keys': {k: len(v) for k, v in data.items() if isinstance(v, list)}})
out = Path('/workspace/research/recovery-manifest-inventory.json')
out.write_text(json.dumps(summary, indent=2) + '\n')
latest = json.loads((base / 'UPLOAD_MANIFEST-continuation312.json').read_text())
print(json.dumps({'manifest_count': len(summary), 'latest_keys': list(latest), 'latest_array_samples': {k: v[:1] for k, v in latest.items() if isinstance(v,list) and k != 'files'}}, indent=2)[:10000])
print('inventory', str(out), hashlib.sha256(out.read_bytes()).hexdigest())
