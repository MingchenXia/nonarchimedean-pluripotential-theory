"""Extract bound HTML as inert text, ignoring scripts/styles; no script execution."""
from pathlib import Path
from html.parser import HTMLParser
import json

ROOT = Path('/workspace/research/campaigns/round-240/P12.2-original-geometric-primary-model-and-full-conductor-independent-whole-review')
class Reader(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip += 1
        if tag in ('p', 'div', 'li', 'h1', 'h2', 'h3', 'br'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip -= 1
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

Path('source-html-text').mkdir(exist_ok=True)
for row in json.loads((ROOT / 'private-primary-packet-bindings.json').read_text()):
    p = Path(row['path'])
    if p.suffix == '.html':
        r = Reader(); r.feed(p.read_text()); r.close()
        lines = [s.strip() for s in ''.join(r.parts).split('\n') if s.strip()]
        out = Path('source-html-text') / (p.stem + '.txt')
        out.write_text('\n'.join(lines) + '\n')
        print(str(out), len(lines))
