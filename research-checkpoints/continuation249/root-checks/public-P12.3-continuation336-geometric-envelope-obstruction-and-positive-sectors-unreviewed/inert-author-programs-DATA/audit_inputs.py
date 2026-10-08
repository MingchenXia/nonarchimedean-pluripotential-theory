#!/usr/bin/env python3
"""Owned read-only input binding audit; never imports or executes packet files."""
import hashlib
import json
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = Path('/workspace/research/campaigns/round-242/P12.3-original-geometric-singular-envelope-positivity-and-regularity')

def binding(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def main():
    (HERE / 'evidence').mkdir(exist_ok=True)
    rows = []
    manifests = []
    for name in ['mathematical-packet-bindings.json', 'private-primary-packet-bindings.json']:
        p = BASE / name
        manifests.append(binding(p))
        for entry in json.loads(p.read_text()):
            actual = binding(Path(entry['path']))
            actual['manifest'] = name
            actual['expected_bytes'] = entry['bytes']
            actual['expected_sha256'] = entry['sha256']
            actual['match'] = actual['bytes'] == entry['bytes'] and actual['sha256'] == entry['sha256']
            rows.append(actual)
    incoming = json.loads((HERE / 'input.json').read_text())
    (HERE / 'original-task.json').write_text(json.dumps(incoming['task'], ensure_ascii=False, indent=2) + '\n')
    (HERE / 'G331-qualified-grant.json').write_text(json.dumps(incoming['notes'][0], ensure_ascii=False, indent=2) + '\n')
    result = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'manifests': manifests,
              'incoming': binding(HERE / 'input.json'), 'records': rows,
              'all_match': all(r['match'] for r in rows),
              'policy': 'Only exact manifest path fields read. Origin/source references not traversed. No supplied program executed or imported.'}
    (HERE / 'input-bindings.json').write_text(json.dumps(result, indent=2) + '\n')
    env = {'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(),
           'cwd': str(HERE), 'pdflatex': shutil.which('pdflatex'),
           'pdflatex_version': subprocess.run(['pdflatex', '--version'], capture_output=True, text=True).stdout.splitlines()[0],
           'compute': 'No operator-supervised compute service available or needed; no resource-heavy computation launched.',
           'runtime_status': 'Skill read; no environment_status tool exposed. No network work or runtime mutation.',
           'provider': 'Caller requested gpt-6.1-sol/xhigh/native Codex. No provider/model attestation performed.'}
    (HERE / 'evidence' / 'environment.json').write_text(json.dumps(env, indent=2) + '\n')
    print(json.dumps({'bound_records': len(rows), 'matched': sum(r['match'] for r in rows), 'all_match': result['all_match']}))
    return 0 if result['all_match'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
