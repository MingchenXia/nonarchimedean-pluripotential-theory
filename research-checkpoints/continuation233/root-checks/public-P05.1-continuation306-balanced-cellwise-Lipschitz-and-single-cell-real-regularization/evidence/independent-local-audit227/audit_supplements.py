"""Fresh, read-only, bounded-packet comparisons; never follows historical paths."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = json.loads((ROOT / 'frozen-bindings-verified.json').read_text())

def body(kind, index):
    row = next(r for r in rows if r['kind'] == kind and r['index'] == index)
    b = Path(row['path']).read_bytes()
    assert len(b) == row['bytes']
    assert hashlib.sha256(b).hexdigest() == row['sha256']
    return b

inventory = json.loads(body('evidence', 2))['artifacts']
bound_author = {}
for r in rows:
    marker = '/immutable-own-evidence/author224/'
    if r['kind'] == 'evidence' and marker in r['path']:
        bound_author[r['path'].split(marker, 1)[1]] = r
comparisons = []
for a in inventory:
    r = bound_author.get(a['filename'])
    if r:
        comparisons.append({'filename': a['filename'], 'supplied': True,
                            'match': a['sha256'] == r['actual_sha256'] and a['bytes'] == r['actual_bytes']})
    else:
        comparisons.append({'filename': a['filename'], 'supplied': False,
                            'match': None})
(ROOT / 'historical-inventory-subset.json').write_text(json.dumps({
    'historical_entries': len(inventory),
    'supplied_entries': sum(a['supplied'] for a in comparisons),
    'matches': sum(a['match'] is True for a in comparisons),
    'unsupplied_entries_not_opened': sum(not a['supplied'] for a in comparisons),
    'comparisons': comparisons}, indent=2) + '\n')

# Exact paragraph dictionary for the separately supplied expanded saved notes.
# Each referenced string was already displayed in full when its source was read.
actual = json.loads(body('math', 32))
saved = json.loads(body('evidence', 1))
dictionary = {'argument': body('math', 29).decode(),
              'source-ledger': body('math', 30).decode(),
              'actual-texts': '\n\n'.join(n['text'] for n in actual['notes'])}
notes = []
for n in saved['notes']:
    parts = []
    for p in n['text'].split('\n\n'):
        for name, source in dictionary.items():
            at = source.find(p)
            if at >= 0:
                parts.append({'source': name, 'start': at, 'end': at + len(p)})
                break
        else:
            parts.append({'literal': p})
    rebuilt = '\n\n'.join(p['literal'] if 'literal' in p else
                           dictionary[p['source']][p['start']:p['end']] for p in parts)
    assert rebuilt == n['text']
    notes.append({'id': n['id'], 'summary': n['summary'],
                  'detailedSummary': n['detailedSummary'], 'support': n['support'],
                  'text_parts': parts, 'exact_string_reconstruction': True})
(ROOT / 'saved-six-lossless-reader.json').write_text(json.dumps({
    'method': 'Exact already-displayed substrings plus all literal paragraphs; no semantic normalization',
    'notes': notes, 'candidate': saved['candidate']}, indent=2, ensure_ascii=False) + '\n')

# Verify the parallel body readers preserve every token AND original whitespace.
delta_checks = []
for index in (7, 13, 19):
    d = json.loads((ROOT / f'delta-math-{index:02}.json').read_text())
    delta_checks.append({k: d[k] for k in ('base_index', 'target_index', 'whole_tokens',
                         'exact_referenced_tokens', 'literal_tokens', 'byte_exact_reconstruction')})
(ROOT / 'lossless-reading-checks.json').write_text(json.dumps({
    'parallel_bodies': delta_checks, 'saved_notes_exactly_reconstructed': len(notes),
    'limitation': 'Machine byte equality does not itself prove that a display was read. Whole displays and repaired spans are recorded separately.'}, indent=2) + '\n')
print('inventory', len(inventory), 'supplied', sum(a['supplied'] for a in comparisons),
      'matching', sum(a['match'] is True for a in comparisons))
print('saved notes exact reconstructions', len(notes), 'parallel bodies', len(delta_checks))
