"""Render essential ambiguous primary formulas as data; never compile TeX."""
from pathlib import Path
import json
import subprocess

OUT = Path(__file__).resolve().parent
BOOK = Path('/workspace/research/primary-data-LOCALONLY/P12.2-conductor-integral-dependence-20261008/Swanson-Huneke-author-book')
BFJ = Path('/workspace/research/campaigns/round-232/P12.2-original-excellent-singular-geometric-cone-and-model-nef-comparison/frozen-primary-data-LOCALONLY/BFJ-valuations-psh')
QUERIES = [(BOOK, 'Lemma 17.2.4', 'book-superficial'),
           (BOOK, 'Definition 17.4.3', 'book-mixed-definition'),
           (BOOK, 'Theorem 17.4.6', 'book-mixed-reduction'),
           (BFJ, '(4.3)', 'bfj-ideal-comparison'),
           (BFJ, 'Let us prove upper semicontinuity.', 'bfj-net-proof')]

def main():
    dest = OUT / 'reports' / 'source-images'
    dest.mkdir(parents=True, exist_ok=True)
    rows = []
    for stem, phrase, name in QUERIES:
        pages = stem.with_suffix('.txt').read_text().split('\f')
        page = next(i+1 for i, p in enumerate(pages) if phrase in p)
        prefix = dest / name
        cmd = ['pdftoppm', '-f', str(page), '-l', str(page), '-scale-to', '1800', '-png', '-singlefile', str(stem.with_suffix('.pdf')), str(prefix)]
        done = subprocess.run(cmd, capture_output=True, text=True)
        rows.append({'phrase': phrase, 'pdf_page': page, 'command': cmd,
                     'exit_code': done.returncode, 'stderr': done.stderr,
                     'image': str(prefix.with_suffix('.png'))})
        if done.returncode:
            raise RuntimeError(done.stderr)
    (OUT / 'reports' / 'primary-image-log.json').write_text(json.dumps(rows, indent=2)+'\n')
    print(json.dumps([{'name': Path(r['image']).name, 'page': r['pdf_page']} for r in rows]))

if __name__ == '__main__':
    main()
