"""Render selected bound primary pages; never execute supplied programs."""
from pathlib import Path
import json, subprocess, hashlib

ROOT = Path('/workspace/research/campaigns/round-240/P12.2-original-geometric-primary-model-and-full-conductor-independent-whole-review')
bindings = json.loads((ROOT / 'private-primary-packet-bindings.json').read_text())
pages = [('Swanson-Huneke-author-book.pdf', 20, 'book-6'),
         ('Swanson-Huneke-author-book.pdf', 154, 'book-140'),
         ('BFJ-valuations-psh.pdf', 27, 'bfj-475')]
Path('source-pixels').mkdir(exist_ok=True)
results = []
for name, page, label in pages:
    entry = next(x for x in bindings if Path(x['path']).name == name)
    data = Path(entry['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == entry['sha256']
    argv = ['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile',
            '-scale-to', '1800', '-png', entry['path'], 'source-pixels/' + label]
    run = subprocess.run(argv, capture_output=True, text=True, check=False)
    results.append({'argv': argv, 'returncode': run.returncode,
                    'stdout': run.stdout, 'stderr': run.stderr})
    assert run.returncode == 0
Path('source-pixel-commands.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps({'rendered': len(results), 'returncodes': [r['returncode'] for r in results]}))
