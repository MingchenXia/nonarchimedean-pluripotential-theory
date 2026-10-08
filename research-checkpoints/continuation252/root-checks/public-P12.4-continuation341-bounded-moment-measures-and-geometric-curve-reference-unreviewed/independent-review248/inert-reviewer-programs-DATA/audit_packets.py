"""Fresh data-only binding audit. Never imports or executes supplied code."""
import hashlib
import json
import platform
import shutil
import sys
from pathlib import Path

BASE = Path('/workspace/research/campaigns/round-248/P12.4-bounded-moment-and-geometric-curve-whole-paper-independent-review')
ROOT = Path(__file__).resolve().parent
def digest(b):
    return hashlib.sha256(b).hexdigest()

def main():
    reports = ROOT / 'reports'
    reports.mkdir(exist_ok=True)
    records = []
    for group, name in [('mathematical', 'mathematical-packet-bindings.json'),
                        ('primary', 'private-primary-packet-bindings.json'),
                        ('historical', 'historical-own-evidence-bindings.json')]:
        manifest = BASE / name
        data = manifest.read_bytes()
        dest = ROOT / 'inputs' / group
        dest.mkdir(parents=True, exist_ok=True)
        (dest / name).write_bytes(data)
        entries = json.loads(data)
        for i, entry in enumerate(entries):
            source = Path(entry['path'])
            body = source.read_bytes()
            target = dest / (f'{i:02d}-' + source.name if group == 'primary' else source.name)
            target.write_bytes(body)
            records.append({'group': group, 'source': str(source),
                            'local': str(target.relative_to(ROOT)), 'bytes': len(body),
                            'sha256': digest(body), 'size_match': len(body) == entry['bytes'],
                            'hash_match': digest(body) == entry['sha256'],
                            'treatment': 'retained bytes, not executed and not a reading claim'})
    (reports / 'input-bindings.json').write_text(json.dumps(records, indent=2) + '\n')
    environment = {'python': sys.version, 'platform': platform.platform(),
                   'cwd': str(ROOT), 'tools': {x: shutil.which(x) for x in
                   ['python', 'pdftotext', 'pdfinfo', 'pdftoppm', 'pdflatex']},
                   'environment_dump': False, 'supplied_code_executed': False,
                   'agents_used': False, 'heavy_compute_used': False}
    (reports / 'environment.json').write_text(json.dumps(environment, indent=2) + '\n')
    math = ROOT / 'inputs' / 'mathematical'
    actual = json.loads((math / '07-actual-native-FINAL.json').read_text())
    expanded = json.loads((math / '06-native-notes.json').read_text())
    for kind, document in [('actual', actual), ('expanded', expanded)]:
        directory = ROOT / 'review-data' / kind
        directory.mkdir(parents=True, exist_ok=True)
        for note in document['notes']:
            (directory / (note['id'] + '.json')).write_text(json.dumps(note, indent=2) + '\n')
    comparison = [{'id': a['id'], 'actual_text_bytes': len(a['text'].encode()),
                   'expanded_text_bytes': len(e['text'].encode()),
                   'identical_text': a['text'] == e['text'],
                   'actual_support': a['support'], 'expanded_support': e['support']}
                   for a, e in zip(actual['notes'], expanded['notes'])]
    (reports / 'note-body-comparison.json').write_text(json.dumps(comparison, indent=2) + '\n')
    print(json.dumps({'records': len(records), 'all_hashes_match': all(r['hash_match'] for r in records),
                      'all_sizes_match': all(r['size_match'] for r in records),
                      'actual_notes': len(actual['notes']), 'expanded_notes': len(expanded['notes'])}))

if __name__ == '__main__':
    main()
