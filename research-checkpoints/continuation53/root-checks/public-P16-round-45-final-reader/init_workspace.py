#!/usr/bin/env python3
"""Preserve input and inventory only the ten authorized public source caches."""
from pathlib import Path
import hashlib
import json
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
p = ROOT / 'input.json'
data = json.loads(p.read_text())
original = ROOT / 'input-original.json'
if original.exists():
    assert p.read_bytes() == original.read_bytes(), 'The retained original input must not be overwritten.'
else:
    shutil.copyfile(p, original)
(ROOT / 'assignment-original.txt').write_text(data['assignment'])
(ROOT / 'task-original.json').write_text(json.dumps(data['task'], ensure_ascii=False, indent=2) + '\n')
sources = json.loads(data['assignment'].split('Read-only published source caches:\n', 1)[1])
assert len(sources) == 10
out = ROOT / 'source-extracts'
out.mkdir(exist_ok=True)
records = []
for source in sources:
    r = dict(source)
    r['checks'] = {}
    for key in ['pdf', 'literal_extract', 'abstract_html']:
        if key not in source:
            continue
        b = Path(source[key]).read_bytes()
        digest = hashlib.sha256(b).hexdigest()
        expected_key = {'literal_extract': 'extract_sha256', 'abstract_html': 'abstract_sha256'}.get(key, 'pdf_sha256')
        r['checks'][key] = {'bytes': len(b), 'sha256': digest,
                            'matches_supplied': digest == source[expected_key]}
        assert r['checks'][key]['matches_supplied']
    result = subprocess.run(['pdfinfo', source['pdf']], text=True, capture_output=True)
    r['pdfinfo'] = result.stdout
    r['pdfinfo_returncode'] = result.returncode
    records.append(r)
(out / 'source-inventory.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
environment = {
    'python': sys.version, 'platform': platform.platform(), 'cwd': str(ROOT),
    'tex': subprocess.run(['pdflatex', '--version'], text=True, capture_output=True).stdout,
    'pdftotext': subprocess.run(['pdftotext', '-v'], text=True, capture_output=True).stderr,
    'compute': 'No heavy computation needed or launched; no supervised compute service used.',
    'network': 'No network calls; only the ten authorized read-only public caches read.',
    'agents': 'No other model calls or subagents invoked.',
    'requested_native_execution': 'User requests native Codex gpt-6.1-sol/xhigh. The providing runtime model and effort cannot be independently queried or changed through the available execution tools; no alternative model was invoked.'
}
(ROOT / 'environment.json').write_text(json.dumps(environment, ensure_ascii=False, indent=2) + '\n')
print('Preserved byte-identical input, exact assignment/task content, and checked all ten authorized source caches.')
