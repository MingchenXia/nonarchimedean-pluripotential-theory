"""Own read-only bound-packet verifier and redundant whole-body coverage check."""
import hashlib
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

BASE = Path('/workspace/research/campaigns/round-217/P05.1-isolated-affine-crossings-all-continuous-global-regularization-paper')
records = []
for name in ['mathematical-packet-bindings.json', 'private-primary-packet-bindings.json']:
    for i, entry in enumerate(json.loads((BASE / name).read_text())):
        data = Path(entry['path']).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        records.append({'binding': name, 'index': i, 'label': entry['label'], 'path': entry['path'],
                        'expected_sha256': entry['sha256'], 'actual_sha256': digest,
                        'expected_bytes': entry.get('bytes'), 'actual_bytes': len(data),
                        'hash_match': digest == entry['sha256'],
                        'size_match': len(data) == entry.get('bytes', len(data))})
assert all(x['hash_match'] and x['size_match'] for x in records)
Path('input-verification.json').write_text(json.dumps(records, indent=2) + '\n')
Path('environment.json').write_text(json.dumps({'python': sys.version, 'platform': platform.platform(),
    'cwd': str(Path.cwd()), 'network_used': False, 'subagents_used': False,
    'runtime_model_independently_verified': False, 'heavy_compute_facility_exposed': False}, indent=2) + '\n')
entries = json.loads((BASE / 'mathematical-packet-bindings.json').read_text())
reports = []
def normalize(s):
    s = re.sub(r'\\label\{[^}]*\}|\\tag\{[^}]*\}|\\notag', '', s)
    s = re.sub(r'\[(?:[0-9]+|\\\[[^\n]*?\\\])\]\(#[^)]+\)\{reference-type="[^"]*" reference="[^"]*"\}', 'REF', s)
    s = re.sub(r'\([0-9]+\)', 'REF', s)
    s = re.sub(r'\b(Lemma|Proposition|Theorem)\s+[0-9]+\.?', r'\1 REF', s)
    s = s.replace('REF .', 'REF').replace('REF.', 'REF')
    return re.sub(r'\s+', ' ', s).strip()
for ti, mi in [(6, 7), (12, 13)]:
    args = ['pandoc', '-f', 'latex', '-t', 'markdown']
    if ti == 12:
        args += ['--wrap=none']
    args += [entries[ti]['path']]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    md = Path(entries[mi]['path']).read_text()
    md = md[md.find('# '):]
    if ti == 6:
        x, y = result.stdout, md
        eq = x == y
        method = 'whole body exact bytes after separately read metadata'
    else:
        x = normalize(result.stdout[:result.stdout.find('::: thebibliography')])
        y = normalize(md[:md.find('# References')])
        eq = x == y
        method = 'whole body whitespace/labels/resolved-reference normalization; bibliography and metadata separately read'
    assert eq
    reports.append({'tex_index': ti, 'md_index': mi, 'equality': eq, 'method': method,
                    'left_sha256': hashlib.sha256(x.encode()).hexdigest(),
                    'right_sha256': hashlib.sha256(y.encode()).hexdigest(), 'warnings': result.stderr})
Path('whole-grant-body-comparison.json').write_text(json.dumps(reports, indent=2) + '\n')
print('23 of 23 bound files match hashes and sizes; both whole redundant grant bodies agree by the disclosed comparisons.')
