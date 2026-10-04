from pathlib import Path
from datetime import datetime, timezone
import hashlib
import html
import json
import re
import subprocess
import urllib.request

root = Path('/workspace/research/shared-sources')
ids = ['1201.0187', '1201.0188', '1805.01016', '1801.08229', '2307.01697', '2209.04879']
manifest = root / 'P16-public-primary-cache-20261004.json'
assert not manifest.exists()
records = []
for paper_id in ids:
    prefix = root / ('P16-arxiv-' + paper_id + '-20261004')
    abstract = Path(str(prefix) + '.html')
    pdf = Path(str(prefix) + '.pdf')
    extract = Path(str(prefix) + '.txt')
    assert not any(p.exists() for p in (abstract, pdf, extract))
    page_url = 'https://arxiv.org/abs/' + paper_id
    req = urllib.request.Request(page_url, headers={'User-Agent': 'Mathematical-source-cache/1.0'})
    with urllib.request.urlopen(req, timeout=45) as response:
        page_bytes = response.read()
        actual_page_url = response.geturl()
    page = page_bytes.decode('utf-8')
    title_match = re.search(r'<title>(.*?)</title>', page, re.S)
    version_match = re.search(r'<meta property="og:url" content="https://arxiv.org/abs/([0-9.]+v[0-9]+)"', page)
    assert title_match and version_match
    version = version_match.group(1)
    assert version.startswith(paper_id + 'v')
    pdf_url = 'https://arxiv.org/pdf/' + version
    with urllib.request.urlopen(urllib.request.Request(pdf_url, headers={'User-Agent': 'Mathematical-source-cache/1.0'}), timeout=45) as response:
        pdf_bytes = response.read()
        actual_pdf_url = response.geturl()
    assert pdf_bytes.startswith(b'%PDF-')
    abstract.write_bytes(page_bytes)
    pdf.write_bytes(pdf_bytes)
    built = subprocess.run(['pdftotext', '-layout', str(pdf), str(extract)], capture_output=True, text=True)
    assert built.returncode == 0, built.stderr
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    records.append({'arxiv_id': paper_id, 'saved_version': version,
        'title': html.unescape(title_match.group(1)), 'public_source': pdf_url,
        'abstract_url': page_url, 'actual_abstract_url': actual_page_url,
        'actual_pdf_url': actual_pdf_url, 'abstract_html': str(abstract), 'abstract_sha256': sha(abstract),
        'pdf': str(pdf), 'pdf_sha256': sha(pdf), 'pdf_bytes': len(pdf_bytes),
        'literal_extract': str(extract), 'extract_sha256': sha(extract),
        'extract_bytes': extract.stat().st_size,
        'pdftotext_returncode': built.returncode,
        'origin': 'Publicly available primary mathematical source; no generated research payload.'})
    print(json.dumps({'saved_version': version, 'title': records[-1]['title'], 'pdf_bytes': len(pdf_bytes)}), flush=True)
manifest.write_text(json.dumps({'cached_utc': datetime.now(timezone.utc).isoformat(),
    'sources': records, 'mathematical_correctness_claimed': False}, indent=2) + '\n')
print(json.dumps({'manifest': str(manifest), 'sha256': hashlib.sha256(manifest.read_bytes()).hexdigest()}))
