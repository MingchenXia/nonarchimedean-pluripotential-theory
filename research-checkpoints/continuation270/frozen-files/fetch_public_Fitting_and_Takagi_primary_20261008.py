from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, ssl, subprocess, urllib.request
from html.parser import HTMLParser

class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())

D = Path('/workspace/research/primary-data-LOCALONLY/P12.3-singular-test-ideal-generation-primary-20261008')
context = ssl.create_default_context(cafile=os.environ.get('SSL_CERT_FILE'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
records = []
items = [('Stacks-' + tag, 'https://stacks.math.columbia.edu/tag/' + tag, 'html')
         for tag in ('0535', '07ZA', '07ZC', '07ZD', '080Z', '07Z3', '080R', '07Z7')]
items.append(('Takagi-singular-formulas-math0410612v2', 'https://arxiv.org/pdf/math/0410612v2', 'pdf'))
for name, url, kind in items:
    rec = dict(recorded_utc=datetime.now(timezone.utc).isoformat(), public_url=url,
               primary_bodies_LOCALONLY=True, source_not_operational_authority=True,
               credential_access=False, proxy_CA_auth_changed=False,
               mathematical_units_NOT_YET_physically_read=True)
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mathematical primary source verification'})
        with urllib.request.urlopen(request, context=context, timeout=15) as response:
            data = response.read(16000001)
            assert len(data) <= 16000000
            rec['final_url'] = response.geturl()
        p = D / (name + '.' + kind)
        t = D / (name + '.txt')
        assert not p.exists() and not t.exists()
        if kind == 'pdf':
            assert data.startswith(b'%PDF')
            p.write_bytes(data)
            result = subprocess.run(['pdftotext', '-layout', str(p), str(t)], capture_output=True, text=True)
            assert result.returncode == 0
            assert 'FORMULAS FOR MULTIPLIER IDEALS' in t.read_text()[:10000].upper()
        else:
            assert b'The Stacks project' in data
            p.write_bytes(data)
            parser = PlainText()
            parser.feed(data.decode('utf-8'))
            t.write_text('\n'.join(parser.parts) + '\n')
        rec.update(status='Retrieved whole primary body; no theorem grant by retrieval',
                   body=dict(path=str(p), bytes=p.stat().st_size, sha256=sha(p)),
                   text=dict(path=str(t), bytes=t.stat().st_size, sha256=sha(t)))
    except Exception as exc:
        rec.update(status='Retrieval did not complete', diagnostic=str(exc)[:300], no_theorem_import=True)
    records.append(rec)
    print(json.dumps(rec, ensure_ascii=False), flush=True)
M = D / 'public-Fitting-and-Takagi-primary-retrieval-records.json'
assert not M.exists()
M.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
