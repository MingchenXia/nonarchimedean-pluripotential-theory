"""Read only supplied primary caches; save literal, inclusive LF excerpts."""
import json
import sys
from pathlib import Path

manifest = {r['id']: r for r in json.loads(Path('source-manifest.json').read_text())}
out = Path('source-extracts')
out.mkdir(exist_ok=True)
registry = out / 'ranges.json'
rows = json.loads(registry.read_text()) if registry.exists() else []
for spec in sys.argv[1:]:
    sid, bounds = spec.split(':')
    lo, hi = map(int, bounds.split('-'))
    lines = Path(manifest[sid]['literal_extract']).read_text(encoding='utf-8').split('\n')
    assert 1 <= lo <= hi <= len(lines)
    literal = '\n'.join(lines[lo-1:hi])
    name = f'{sid}-LF{lo}-{hi}.txt'
    (out / name).write_text(literal, encoding='utf-8')
    row = {'source': sid, 'start_LF': lo, 'end_LF': hi, 'literal': literal,
           'artifact': name, 'index_rule': "inclusive one-based text.split('\\n')"}
    if not any((r['source'], r['start_LF'], r['end_LF']) == (sid, lo, hi) for r in rows):
        rows.append(row)
    print(f'\nSOURCE {sid} LF{lo}--{hi}')
    print('\n'.join(f'{i}: {lines[i-1]}' for i in range(lo, hi+1)))
registry.write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
