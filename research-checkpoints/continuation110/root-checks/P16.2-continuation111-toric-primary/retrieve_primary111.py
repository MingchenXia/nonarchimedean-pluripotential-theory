from pathlib import Path
import hashlib, json, subprocess, urllib.request
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
specs = [
    ('Rohrer-dissertation', 'https://fredrohrer.ch/wp-content/uploads/2020/06/diss.pdf'),
    ('Rohrer-geometry-1207.0605v2', 'https://arxiv.org/pdf/1207.0605v2'),
    ('Fujino-Sato-wSato', 'https://www.math.kyoto-u.ac.jp/~fujino/wSato.pdf'),
]
records = []
for label, url in specs:
    pdf = root / (label + '.pdf')
    txt = root / (label + '.txt')
    if pdf.exists() or txt.exists():
        raise RuntimeError('Refusing to overwrite primary source: ' + label)
    request = urllib.request.Request(url, headers={'User-Agent':'research-source-audit/1.0'})
    with urllib.request.urlopen(request, timeout=60) as response:
        body = response.read()
        final_url = response.geturl()
        content_type = response.headers.get('Content-Type')
    if not body.startswith(b'%PDF'):
        raise RuntimeError('Response is not PDF: ' + url)
    pdf.write_bytes(body)
    subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)], check=True)
    text_body = txt.read_bytes()
    records.append({'url':url, 'final_url':final_url, 'content_type':content_type,
                    'pdf':str(pdf), 'pdf_sha256':hashlib.sha256(body).hexdigest(),
                    'literal_text':str(txt), 'literal_text_sha256':hashlib.sha256(text_body).hexdigest(),
                    'entire_source_root_read':False})
    print(json.dumps({'source':label, 'bytes':len(body), 'text_bytes':len(text_body)}))
(root/'retrieval-manifest.json').write_text(json.dumps({'retrieved_utc':datetime.now(timezone.utc).isoformat(),
                                                     'records':records}, indent=2)+'\n')
