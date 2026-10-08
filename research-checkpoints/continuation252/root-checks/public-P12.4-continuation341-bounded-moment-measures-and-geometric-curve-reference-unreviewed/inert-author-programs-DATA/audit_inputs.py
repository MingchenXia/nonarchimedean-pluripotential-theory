#!/usr/bin/env python3
"""Fresh data-only retention/audit; never executes or imports supplied files."""
from pathlib import Path
import hashlib, json, platform, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parent
PACKET = ROOT.parents[1]
REPORT = ROOT / 'reports'
REPORT.mkdir(exist_ok=True)
records = []
for manifest_name, category in [('mathematical-packet-bindings.json', 'mathematical'),
                                ('private-primary-packet-bindings.json', 'primary')]:
    source = PACKET / manifest_name
    local = ROOT / 'inputs' / manifest_name
    local.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, local)
    for entry in json.loads(source.read_text()):
        original = Path(entry['path'])
        data = original.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        dest = ROOT / 'inputs' / category / original.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        records.append({'original': str(original), 'local': str(dest.relative_to(ROOT)),
                        'url': entry.get('requested_url', entry.get('url')),
                        'bytes': len(data), 'sha256': digest,
                        'expected_bytes': entry['bytes'], 'expected_sha256': entry['sha256'],
                        'matches': len(data) == entry['bytes'] and digest == entry['sha256']})
result = {'records': records, 'all_match': all(r['matches'] for r in records),
          'note': 'Byte retention is not source reading, theorem verification, or a grant.'}
(REPORT / 'input-hashes.json').write_text(json.dumps(result, indent=2) + '\n')
environment = {'python': sys.version, 'platform': platform.platform(), 'cwd': str(ROOT),
               'pdflatex': subprocess.run(['pdflatex', '--version'], text=True,
                                        capture_output=True).stdout.splitlines()[0],
               'pandoc': subprocess.run(['pandoc', '--version'], text=True,
                                      capture_output=True).stdout.splitlines()[0],
               'heavy_compute': 'No supervised facility supplied; none needed or launched.',
               'model_attestation': 'Caller requests gpt-6.1-sol xhigh; no independent runtime attestation.'}
(REPORT / 'environment.json').write_text(json.dumps(environment, indent=2) + '\n')
print(json.dumps({'bound_files': len(records), 'all_match': result['all_match']}))
if not result['all_match']:
    raise SystemExit(1)
