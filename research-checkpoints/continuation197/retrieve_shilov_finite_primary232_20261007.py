from pathlib import Path
from datetime import datetime,timezone
from urllib.request import Request,urlopen
import hashlib,json,subprocess
P=Path('/workspace/research/root-checks/continuation232-shilov-finite-primary-LOCALONLY');assert not P.exists();P.mkdir()
url='https://arxiv.org/pdf/2511.21835v1'
with urlopen(Request(url,headers={'User-Agent':'Research source verification'}),timeout=45) as r:
    data=r.read(); final_url=r.geturl(); content_type=r.headers.get('Content-Type')
assert data.startswith(b'%PDF')
pdf=P/'Fang2511.21835v1.pdf';pdf.write_bytes(data)
txt=P/'Fang2511.21835v1.txt';subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
j=dict(retrieved_utc=datetime.now(timezone.utc).isoformat(),literal_requested_url=url,final_url=final_url,content_type=content_type,pdf_bytes=len(data),pdf_sha256=sha(pdf),text_sha256=sha(txt),route='Standard-library HTTPS with authorized parent network access; existing proxy/auth/CA untouched',full_source_published=False,mathematical_grant=False)
(P/'retrieval-binding.json').write_text(json.dumps(j,indent=2)+'\n');print(json.dumps(j,indent=2))
