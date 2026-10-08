from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,ssl,subprocess,urllib.request

D=Path('/workspace/research/primary-data-LOCALONLY/P16.7-period-algebraization-primary-20261008')
D.mkdir(parents=True,exist_ok=True)
context=ssl.create_default_context(cafile=os.environ.get('SSL_CERT_FILE'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
items=[
 ('Van-der-Put-Rigid-analytic-spaces-1975-1976','https://www.numdam.org/item/GAU_1975-1976__3_2_A6_0.pdf','Rigid analytic spaces','https://www.numdam.org/item/GAU_1975-1976__3_2_A6_0/'),
 ('Snowbird-Rigid-analytic-geometry-2004','https://math.stanford.edu/~vakil/snowbird/mihranjun21.pdf','RIGID ANALYTIC GEOMETRY','https://math.stanford.edu/~vakil/snowbird/mihranjun21.pdf')]
records=[]
for name,url,title,metadata in items:
 record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),public_url=url,authenticated_bibliographic_page=metadata,expected_title=title,credential_access=False,proxy_CA_auth_changed=False,primary_bodies_LOCALONLY=True,mathematical_proofs_NOT_YET_read=True,source_not_operational_authority=True)
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mathematical primary source verification'})
  with urllib.request.urlopen(req,context=context,timeout=20) as response:
   data=response.read(16000001);assert len(data)<=16000000 and data.startswith(b'%PDF');final=response.geturl()
  P=D/(name+'.pdf');T=P.with_suffix('.txt');assert not P.exists() and not T.exists();P.write_bytes(data)
  out=subprocess.run(['pdftotext','-layout',str(P),str(T)],capture_output=True,text=True);assert out.returncode==0
  txt=T.read_text();assert title.lower() in txt[:16000].lower(),'Expected primary title not authenticated in text'
  record.update(status='Public whole primary PDF retrieved; applied theorem/proofs NOT YET read',final_url=final,pdf=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),text=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)))
 except Exception as exc:record.update(status='Retrieval or title authentication did not complete',error_type=type(exc).__name__,diagnostic=str(exc)[:300],no_theorem_import=True)
 records.append(record);print(json.dumps(record,ensure_ascii=False,indent=2),flush=True)
M=D/'public-period-notes-retrieval-records.json';assert not M.exists();M.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
