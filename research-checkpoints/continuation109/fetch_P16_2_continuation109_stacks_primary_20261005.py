"""Preserve the primary Chow, Stein and birational-locus statements/proofs."""
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import urllib.request

D = Path('/workspace/research/root-checks/P16.2-continuation109-stacks-primary')
assert not D.exists()
D.mkdir()


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
records = []
for tag, opening in [('0200', 'Lemma 30.18.1.'), ('0201', 'Remark 30.18.2.'),
                     ('0AY8', 'Lemma 37.53.6.'), ('0BFP', 'Lemma 33.17.3.')]:
    url = 'https://stacks.math.columbia.edu/tag/' + tag
    raw = urllib.request.urlopen(url, timeout=45).read()
    p = D / (tag + '.html')
    p.write_bytes(raw)
    parser = Parser()
    parser.feed(raw.decode())
    transformed = ''.join(parser.parts)
    start = transformed.index(opening)
    end = transformed.index('Comments (', start)
    t = D / (tag + '-mathematical-body.txt')
    t.write_text(transformed[start:end].strip() + '\n')
    records.append({'tag': tag, 'url': url, 'retrieved_utc': datetime.now(timezone.utc).isoformat(),
                    'raw_html': str(p), 'raw_html_sha256': sha(p),
                    'selected_mathematical_body': str(t), 'body_sha256': sha(t),
                    'text_rule': 'HTMLParser character-reference decoding; omit script/style; concatenate data in document order; slice exact opening to Comments (; strip boundaries and append one LF.',
                    'opening': opening, 'whole_raw_page_root_read': False,
                    'selected_body_root_read': False})
(D / 'retrieval-manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps([{'tag': r['tag'], 'body': r['selected_mathematical_body']} for r in records], indent=2))
