"""Owned byte-only audit and literal attachment preparation. No supplied imports."""
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import sys

BASE = Path('/workspace/research/campaigns/round-249/P12.4-original-supported-Cartier-products-and-bounded-locality')
OUT = Path(__file__).resolve().parent

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    (OUT / 'reports').mkdir(exist_ok=True)
    (OUT / 'attachments').mkdir(exist_ok=True)
    (OUT / 'inputs' / 'mathematical').mkdir(parents=True, exist_ok=True)
    (OUT / 'inputs' / 'primary').mkdir(parents=True, exist_ok=True)
    rows = []
    for manifest_name in ('mathematical-packet-bindings.json', 'private-primary-packet-bindings.json'):
        manifest = BASE / manifest_name
        data = json.loads(manifest.read_text())
        shutil.copyfile(manifest, OUT / 'attachments' / manifest_name)
        for entry in data:
            p = Path(entry['path'])
            kind = 'mathematical' if manifest_name == 'mathematical-packet-bindings.json' else 'primary'
            local = OUT / 'inputs' / kind / p.name
            shutil.copyfile(p, local)
            actual = {'path': str(p), 'bytes': p.stat().st_size, 'sha256': digest(p)}
            actual['local_path'] = str(local)
            actual['local_sha256'] = digest(local)
            actual['match'] = actual['bytes'] == entry['bytes'] and actual['sha256'] == entry['sha256']
            rows.append(actual)
        if manifest_name == 'mathematical-packet-bindings.json':
            for entry in data[:4]:
                shutil.copyfile(entry['path'], OUT / 'attachments' / Path(entry['path']).name)
    report = {'files': rows, 'all_match': all(x['match'] for x in rows),
              'environment': {'python': sys.version, 'platform': platform.platform(), 'cwd': str(OUT)},
              'supplied_programs_executed': False, 'compilation_run': False,
              'supervised_compute_available': False, 'resource_heavy_work_needed': False}
    (OUT / 'reports' / 'input-audit.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'files': len(rows), 'all_match': report['all_match']}))

if __name__ == '__main__':
    main()
