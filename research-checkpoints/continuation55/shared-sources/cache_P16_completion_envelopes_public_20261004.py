from pathlib import Path
from datetime import datetime, timezone
import hashlib
import html
import json
import re
import subprocess
import urllib.request

root = Path('/workspace/research/shared-sources')
paper_ids = ['2012.07972', '1712.00980']
manifest = root / 'P16-completion-envelopes-public-cache-20261004.json'
assert not manifest.exists()
records = []
for paper_id in paper_ids:
    prefix = root / ('P16-completion-envelopes-arxiv-' + paper_id + '-20261004')
    abstract, pdf, extract = (Path(str(prefix) + suffix) for suffix in ('.html', '.pdf', '.txt'))
    assert not any(path.exists() for path in (abstract, pdf, extract))
    page_url = 'https://arxiv.org/abs/' + paper_id
    request = urllib.request.Request(page_url, headers={'User-Agent': 'Mathematical-source-cache/1.0'})
    with urllib.request.urlopen(request, timeout=45) as response:
        page_bytes, actual_page_url = response.read(), response.geturl()
    page = page_bytes.decode('utf-8')
    title_match = re.search(r'<title>(.*?)</title>', page, re.S)
    version_match = re.search(r'<meta property="og:url" content="https://arxiv.org/abs/([0-9.]+v[0-9]+)"', page)
    assert title_match and version_match
    version = version_match.group(1)
    assert version.startswith(paper_id + 'v')
    pdf_url = 'https://arxiv.org/pdf/' + version
    request = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mathematical-source-cache/1.0'})
    with urllib.request.urlopen(request, timeout=45) as response:
        pdf_bytes, actual_pdf_url = response.read(), response.geturl()
    assert pdf_bytes.startswith(b'%PDF-')
    abstract.write_bytes(page_bytes)
    pdf.write_bytes(pdf_bytes)
    built = subprocess.run(['pdftotext', '-layout', str(pdf), str(extract)], capture_output=True, text=True)
    assert built.returncode == 0, built.stderr
    sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    records.append({
        'arxiv_id': paper_id, 'saved_version': version,
        'title': html.unescape(title_match.group(1)), 'public_source': pdf_url,
        'abstract_url': page_url, 'actual_abstract_url': actual_page_url,
        'actual_pdf_url': actual_pdf_url, 'abstract_html': str(abstract),
        'abstract_sha256': sha(abstract), 'pdf': str(pdf), 'pdf_sha256': sha(pdf),
        'pdf_bytes': len(pdf_bytes), 'literal_extract': str(extract),
        'extract_sha256': sha(extract), 'extract_bytes': extract.stat().st_size,
        'pdftotext_returncode': built.returncode,
        'origin': 'Public primary mathematical source; no generated research payload.',
        'whole_paper_read': False, 'mathematical_application_verified': False
    })
    print(json.dumps({'saved_version': version, 'title': records[-1]['title'], 'pdf_bytes': len(pdf_bytes)}), flush=True)
manifest.write_text(json.dumps({
    'cached_utc': datetime.now(timezone.utc).isoformat(), 'sources': records,
    'purpose': 'Local source checking only; frozen active author inputs remain unchanged.',
    'mathematical_correctness_claimed': False
}, indent=2) + '\n')
print(json.dumps({'manifest': str(manifest), 'sha256': hashlib.sha256(manifest.read_bytes()).hexdigest()}))
