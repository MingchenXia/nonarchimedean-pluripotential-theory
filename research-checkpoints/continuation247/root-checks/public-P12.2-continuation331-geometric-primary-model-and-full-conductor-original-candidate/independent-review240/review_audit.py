"""Fresh, read-only packet integrity audit. Never imports candidate programs."""
from pathlib import Path
import hashlib
import json
import platform
import sys

BASE = Path('/workspace/research/campaigns/round-240/P12.2-original-geometric-primary-model-and-full-conductor-independent-whole-review')
OUT = Path(__file__).resolve().parent

def digest(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def main():
    records = []
    for manifest in ('mathematical-packet-bindings.json', 'private-primary-packet-bindings.json', 'historical-own-evidence-bindings.json'):
        records.append(dict(digest(BASE / manifest), category='binding'))
        for expected in json.loads((BASE / manifest).read_text()):
            actual = digest(Path(expected['path']))
            actual.update(category=manifest, expected_bytes=expected['bytes'], expected_sha256=expected['sha256'],
                          match=actual['bytes'] == expected['bytes'] and actual['sha256'] == expected['sha256'])
            records.append(actual)
    for path in (BASE / 'original-task.json', OUT / 'input.json'):
        records.append(dict(digest(path), category='task'))
    actual = json.loads((BASE / 'immutable-mathematical-DATA/09-round238-actual-native-final.json').read_text())
    saved = json.loads((BASE / 'immutable-mathematical-DATA/08-native-notes.json').read_text())
    comparison = {
        'ids_equal': [n['id'] for n in actual['notes']] == [n['id'] for n in saved['notes']],
        'supports_equal': [n['support'] for n in actual['notes']] == [n['support'] for n in saved['notes']],
        'candidate_equal': actual['candidate'] == saved['candidate'],
        'prose_equal_by_note': {n['id']: {k: n[k] == m[k] for k in ('summary', 'detailedSummary', 'text')}
                               for n, m in zip(actual['notes'], saved['notes'])},
    }
    (OUT / 'exact-input-hashes.json').write_text(json.dumps(records, indent=2) + '\n')
    (OUT / 'actual-versus-expanded.json').write_text(json.dumps(comparison, indent=2) + '\n')
    (OUT / 'review-environment.json').write_text(json.dumps({'python': sys.version, 'platform': platform.platform(),
        'cwd': str(OUT), 'activity': 'local read-only hashing and text/PDF inspection; fresh review writing',
        'network': False, 'supplied_code_executed_or_imported': False, 'agents': False,
        'heavy_compute': False, 'supervised_compute_facility': 'not provided; not needed'}, indent=2) + '\n')
    failures = [r for r in records if r.get('match') is False]
    print(json.dumps({'bound_records': sum('match' in r for r in records), 'failures': failures,
                      'actual_versus_expanded': comparison}, indent=2))

if __name__ == '__main__':
    main()
