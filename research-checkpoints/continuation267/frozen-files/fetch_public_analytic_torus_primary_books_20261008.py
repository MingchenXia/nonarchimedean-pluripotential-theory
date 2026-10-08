from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,ssl,subprocess,urllib.request

D=Path('/workspace/research/primary-data-LOCALONLY/P16.7-period-algebraization-primary-20261008');D.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
context=ssl.create_default_context(cafile=os.environ.get('SSL_CERT_FILE'))
items=[('Lutkebohmert-RigidCurvesJacobians','https://math.bu.edu/people/yangzhe/Lutkebohmert_RigidCurvesJacobians.pdf','Rigid Geometry of Curves'),('Fresnel-van-der-Put-RigidGeometryApplications','https://math.bu.edu/people/yangzhe/FvdP_RigidGeometryApplications.pdf','Rigid Analytic Geometry')]
records=[]
for name,url,title in items:
 record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),public_url=url,source_purpose='Read complete applied period classification/ampleness and algebraization proofs for future independent P16.7 research; not active feedback',credential_access=False,proxy_CA_auth_changed=False,primary_bodies_LOCALONLY=True)
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mathematical primary source verification'})
  with urllib.request.urlopen(req,context=context,timeout=20) as response:
   data=response.read(32000001);assert len(data)<=32000000 and data.startswith(b'%PDF');final=response.geturl()
  P=D/(name+'.pdf');assert not P.exists();P.write_bytes(data);T=P.with_suffix('.txt')
  r=subprocess.run(['pdftotext','-layout',str(P),str(T)],capture_output=True,text=True);assert r.returncode==0
  text=T.read_text();assert title.lower() in text[:16000].lower(),'Downloaded title has not authenticated the expected primary book'
  record.update(status='Public university-hosted whole primary book retrieved; mathematical applied units NOT YET read',final_url=final,pdf=dict(path=str(P),bytes=P.stat().st_size,sha256=sha(P)),text=dict(path=str(T),bytes=T.stat().st_size,sha256=sha(T)),title_check=title)
 except Exception as exc:record.update(status='Public whole primary retrieval did not complete',error_type=type(exc).__name__,diagnostic=str(exc)[:300],no_theorem_import=True)
 records.append(record);print(json.dumps(record,ensure_ascii=False,indent=2),flush=True)
(D/'public-primary-retrieval-records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
