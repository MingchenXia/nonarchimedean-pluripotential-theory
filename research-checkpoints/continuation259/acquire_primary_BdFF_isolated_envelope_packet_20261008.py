from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,urllib.request

R=Path('/workspace/research');P=R/'primary-data-LOCALONLY/P12.3-BdFF-isolated-envelope-20261008'
assert not P.exists();P.mkdir()
url='https://sebastien.boucksom.perso.math.cnrs.fr/publis/BdFF.pdf'
req=urllib.request.Request(url,headers={'User-Agent':'Mathematical-source-check/1.0'})
with urllib.request.urlopen(req,timeout=45) as response:body=response.read();final=response.geturl()
assert body.startswith(b'%PDF') and len(body)<16000000
pdf=P/'BdFF-volume-isolated-singularity-author-published.pdf';pdf.write_bytes(body)
txt=P/'BdFF-volume-isolated-singularity-author-published.txt'
subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True,capture_output=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record=dict(acquired_utc=datetime.now(timezone.utc).isoformat(),url=url,final_url=final,title='The volume of an isolated singularity',authors=['Sebastien Boucksom','Tommaso de Fernex','Charles Favre'],role='PRIMARY source DATA for future independent application; no theorem grant, not whole source reading',pdf_path=str(pdf),pdf_bytes=pdf.stat().st_size,pdf_sha256=sha(pdf),text_path=str(txt),text_bytes=txt.stat().st_size,text_sha256=sha(txt),LOCALONLY=True,no_local_file_upload=True,no_auth_or_proxy_CA_change=True,not_given_to_ACTIVE_native256257=True)
(P/'acquisition-records.json').write_text(json.dumps([record],indent=2)+'\n')
print(json.dumps(record,indent=2))
