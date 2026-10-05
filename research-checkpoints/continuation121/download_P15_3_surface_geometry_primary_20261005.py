from pathlib import Path
import hashlib, json, subprocess, urllib.request

R = Path('/workspace/research'); S = R / 'shared-sources'
items = []
for title, url, stem in [
    ('Deng, Transcendental Morse Inequality and Generalized Okounkov Bodies, arXiv1503.00112v1',
     'https://arxiv.org/pdf/1503.00112v1', 'P15.3-Deng-1503.00112v1-20261005'),
    ('Demailly--Paun, Numerical characterization of the Kahler cone, Annals159(2004),1247--1274',
     'https://annals.math.princeton.edu/wp-content/uploads/annals-v159-n3-p05.pdf', 'P15.3-Demailly-Paun-Annals-2004-20261005')]:
    pdf = S / (stem + '.pdf'); extract = S / (stem + '.txt')
    assert not pdf.exists() and not extract.exists()
    request = urllib.request.Request(url, headers={'User-Agent': 'Research source verification'})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read(); final_url = response.url
    assert data.startswith(b'%PDF-') and len(data) < 5000000
    pdf.write_bytes(data)
    subprocess.run(['pdftotext', '-layout', str(pdf), str(extract)], check=True)
    items.append({'title': title, 'public_url': url, 'final_url': final_url,
        'local_only_PDF': str(pdf), 'PDF_bytes': len(data), 'PDF_sha256': hashlib.sha256(data).hexdigest(),
        'local_only_literal_extract': str(extract), 'extract_bytes': extract.stat().st_size,
        'extract_sha256': hashlib.sha256(extract.read_bytes()).hexdigest(),
        'line_coordinate_convention': 'LF split, retaining form feeds within lines',
        'whole_work_read': False, 'whole_work_upload_authorized_as_own_work': False})
out = R / 'root-checks/P15.3-surface-geometry-public-primary-download-binding-20261005.json'
assert not out.exists(); out.write_text(json.dumps(items, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(items, ensure_ascii=False, indent=2))
