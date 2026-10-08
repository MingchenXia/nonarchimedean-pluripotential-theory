from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, urllib.request

S=Path('/workspace/research/primary-data-LOCALONLY/P12.3-HH02-Jacobian-normalization-primary-20261008')
assert not S.exists(); S.mkdir()
url='https://arxiv.org/pdf/math/0211174v1'
req=urllib.request.Request(url,headers={'User-Agent':'Research primary-source reader/1.0'})
with urllib.request.urlopen(req,timeout=35) as response:
    data=response.read(8*1024*1024+1)
    final_url=response.geturl()
assert len(data)<=8*1024*1024 and data.startswith(b'%PDF-')
p=S/'HH02-symbolic-ordinary-math0211174v1.pdf'; p.write_bytes(data)
t=p.with_suffix('.txt')
subprocess.run(['pdftotext','-layout',str(p),str(t)],check=True)
sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest()
record=dict(retrieved_utc=datetime.now(timezone.utc).isoformat(),requested_url=url,final_url=final_url,
    files=[dict(path=str(q),bytes=q.stat().st_size,sha256=sha(q),LOCALONLY=True) for q in [p,t]],
    status='Retained complete public primary PDF and text; theorem/proof physical reading follows, no correctness grant or full-PDF reading claimed.',
    executable_or_instruction_authority=False,protected_editor_unchanged=True)
(S/'public-HH02-retrieval-metadata.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
