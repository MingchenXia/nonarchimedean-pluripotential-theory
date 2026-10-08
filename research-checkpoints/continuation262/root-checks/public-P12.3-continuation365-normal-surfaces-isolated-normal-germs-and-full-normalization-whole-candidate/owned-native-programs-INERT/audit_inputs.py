"""Retain explicitly bound bytes as DATA; never import or execute supplied code."""
from pathlib import Path
import hashlib, json, platform, shutil, sys

BASE = Path('/workspace/research/campaigns/round-258/P12.3-whole-normal-surface-isolated-envelope-and-full-normalization-independent-completion')
records = []
for prefix, name in [('m','mathematical-packet-bindings.json'),('p','private-primary-packet-bindings.json'),('c','book-context-bindings.json')]:
    manifest = BASE/name
    target = Path('inputs/manifests')/name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(manifest, target)
    for i, item in enumerate(json.loads(manifest.read_text())):
        src = Path(item['path'])
        data = src.read_bytes()
        dst = Path('inputs')/prefix/(f'{prefix}{i:02d}-'+src.name)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        digest = hashlib.sha256(data).hexdigest()
        records.append(dict(item, key=f'{prefix}{i:02d}', local=str(dst), actual_bytes=len(data), actual_sha256=digest, match=len(data)==item['bytes'] and digest==item['sha256']))
Path('reports').mkdir(exist_ok=True)
Path('reports/input-hashes.json').write_text(json.dumps(records, indent=2)+'\n')
Path('reports/environment.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'cwd':str(Path.cwd()),'managed_status_tool_available':False,'network_used':False,'supervised_compute':'not supplied; no resource-heavy work launched'},indent=2)+'\n')
print(json.dumps({'records':len(records),'matched':sum(r['match'] for r in records)}))
