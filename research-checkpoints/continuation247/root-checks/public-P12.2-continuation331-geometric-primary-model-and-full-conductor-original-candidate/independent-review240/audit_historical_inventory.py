"""Hash precisely inventoried historical files as bytes, including programs as DATA."""
from pathlib import Path
import hashlib, json

ROOT = Path('/workspace/research/campaigns/round-240/P12.2-original-geometric-primary-model-and-full-conductor-independent-whole-review')
EVIDENCE = ROOT / 'immutable-own-evidence'
AUTHOR = Path('/workspace/research/campaigns/round-238/P12.2-original-geometric-source-completion-and-whole-conductor-reconstruction/artifacts/codex-2eREYM')
results = []
for group, records, base in [
    ('author-own', json.loads((EVIDENCE / 'own-hashes.json').read_text())['artifacts'], AUTHOR),
    ('author-input', json.loads((EVIDENCE / 'input-hashes.json').read_text()), None),
]:
    for item in records:
        path = (base / item['path']) if base else Path(item['path'])
        row = {'group': group, 'path': str(path), 'expected_sha256': item['sha256']}
        try:
            raw = path.read_bytes()
            row.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
            row['matches'] = row['sha256'] == item['sha256'] and ('bytes' not in item or len(raw) == item['bytes'])
        except OSError as error:
            row.update(matches=False, error=str(error))
        results.append(row)
Path('historical-inventory-rehash.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps({'author_own': sum(r['group'] == 'author-own' for r in results),
                  'author_input': sum(r['group'] == 'author-input' for r in results),
                  'failures': [r for r in results if not r['matches']]}))
