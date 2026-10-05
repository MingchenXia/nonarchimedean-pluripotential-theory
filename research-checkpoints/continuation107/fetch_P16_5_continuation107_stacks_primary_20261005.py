"""Preserve public Stacks primary pages and deterministic mathematical text."""
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import urllib.request

D = Path('/workspace/research/root-checks/P16.5-continuation107-stacks-primary')
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
for tag, opening, closing in [
    ('01Q3', 'Proposition 28.27.13.', 'Comments ('),
    ('0B5T', 'Lemma 30.16.1.', 'Comments ('),
    ('0BEM', 'Lemma 33.45.1.', 'Comments ('),
    ('0B3Q', 'Lemma 31.16.1.', 'Lemma 31.16.2.'),
]:
    url = 'https://stacks.math.columbia.edu/tag/' + tag
    raw = urllib.request.urlopen(url, timeout=45).read()
    p = D / (tag + '.html')
    p.write_bytes(raw)
    parser = Parser()
    parser.feed(raw.decode())
    transformed = ''.join(parser.parts)
    start = transformed.index(opening)
    end = transformed.index(closing, start)
    body = transformed[start:end].strip() + '\n'
    t = D / (tag + '-mathematical-body.txt')
    t.write_text(body)
    records.append({'tag': tag, 'url': url, 'retrieved_utc': datetime.now(timezone.utc).isoformat(),
                    'raw_html': str(p), 'raw_html_sha256': sha(p),
                    'selected_mathematical_body': str(t), 'body_sha256': sha(t),
                    'text_rule': 'HTMLParser character-reference decoding; omit script/style data; concatenate data in document order; slice from exact opening to before exact closing; strip boundary whitespace and add one LF.',
                    'opening': opening, 'closing': closing,
                    'whole_raw_page_root_read': False, 'selected_body_root_read': False})
(D / 'retrieval-manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps([{'tag': r['tag'], 'body': r['selected_mathematical_body']} for r in records], indent=2))
