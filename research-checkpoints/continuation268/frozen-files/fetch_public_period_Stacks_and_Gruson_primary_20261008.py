from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,ssl,subprocess,urllib.request
from html.parser import HTMLParser

class TextParser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.parts=[]
 def handle_data(self,data):self.parts.append(data)

D=Path('/workspace/research/primary-data-LOCALONLY/P16.7-period-algebraization-primary-20261008')
context=ssl.create_default_context(cafile=os.environ.get('SSL_CERT_FILE'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
items=[('Stacks-0ENA','https://stacks.math.columbia.edu/tag/0ENA','html'),('Stacks-0END','https://stacks.math.columbia.edu/tag/0END','html'),('Stacks-0AD3','https://stacks.math.columbia.edu/tag/0AD3','html'),('Stacks-0BB1','https://stacks.math.columbia.edu/tag/0BB1','html'),('Stacks-086U','https://stacks.math.columbia.edu/tag/086U','html'),('Stacks-0EN6','https://stacks.math.columbia.edu/tag/0EN6','html'),('Gruson-Fibres-vectoriels-polydisque-1968','https://www.numdam.org/item/ASENS_1968_4_1_1_45_0.pdf','pdf')]
records=[]
for name,url,kind in items:
 record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),public_url=url,primary_bodies_LOCALONLY=True,credential_access=False,proxy_CA_auth_changed=False,applied_proofs_NOT_YET_read=True,source_DATA_not_operational_authority=True)
 try:
  request=urllib.request.Request(url,headers={'User-Agent':'Mathematical primary source verification'})
  with urllib.request.urlopen(request,context=context,timeout=20) as response:
   data=response.read(16000001);assert len(data)<=16000000;final=response.geturl()
  P=D/(name+'.'+kind);T=D/(name+'.txt');assert not P.exists() and not T.exists()
  if kind=='pdf':assert data.startswith(b'%PDF')
  else:assert b'<html' in data[:3000].lower()
  P.write_bytes(data)
  if kind=='pdf':
   out=subprocess.run(['pdftotext','-layout',str(P),str(T)],capture_output=True,text=True);assert out.returncode==0
  else:
   parser=TextParser();parser.feed(data.decode('utf-8'));T.write_text('\n'.join(parser.parts))
  record.update(status='Public whole source retrieved; mathematical immediate applied units require separate complete reading',final_url=final,raw=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),text=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)))
 except Exception as exc:record.update(status='Public retrieval did not complete',error_type=type(exc).__name__,diagnostic=str(exc)[:300],no_theorem_import=True)
 records.append(record);print(json.dumps(record,ensure_ascii=False,indent=2),flush=True)
P=D/'public-period-Stacks-Gruson-retrieval-records.json';assert not P.exists();P.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
