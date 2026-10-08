from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,ssl,subprocess,urllib.request

D=Path('/workspace/research/primary-data-LOCALONLY/P12.3-test-ideal-uniform-approximation-20261008');D.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
context=ssl.create_default_context(cafile=os.environ.get('SSL_CERT_FILE'))
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),purpose='Public source verification of Mustata test-ideal statements for ROOT371 and future independent reconstruction; no active feedback',credential_access=False,proxy_CA_auth_changed=False,primary_bodies_LOCALONLY=True)
def get(url,limit):
 req=urllib.request.Request(url,headers={'User-Agent':'Mathematical source verification'})
 with urllib.request.urlopen(req,context=context,timeout=20) as response:
  data=response.read(limit+1);assert len(data)<=limit;return data,response.geturl()
try:
 data,final=get('https://arxiv.org/abs/1109.3825',1000000)
 text=data.decode('utf-8');assert 'The non-nef locus in positive characteristic' in text,'Public candidate identifier did not authenticate the expected title; do not download or cite it'
 (D/'Mustata-1109.3825-abstract-LOCALONLY.html').write_bytes(data)
 data,finalpdf=get('https://arxiv.org/pdf/1109.3825',32000000);assert data.startswith(b'%PDF')
 P=D/'Mustata-non-nef-locus-public.pdf';P.write_bytes(data)
 T=P.with_suffix('.txt');r=subprocess.run(['pdftotext','-layout',str(P),str(T)],capture_output=True,text=True);assert r.returncode==0
 record.update(status='downloaded public primary, mathematical units NOT YET read',abstract_final_url=final,pdf_final_url=finalpdf,pdf=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),text=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)))
except Exception as exc:
 record.update(status='public source retrieval did not complete',error_type=type(exc).__name__,diagnostic=str(exc)[:300],no_theorem_import=True)
(D/'public-retrieval-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(json.dumps(record,ensure_ascii=False,indent=2))
