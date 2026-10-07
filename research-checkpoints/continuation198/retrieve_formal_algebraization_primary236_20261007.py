from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,urllib.request
K=Path('/workspace/research/root-checks/continuation236-formal-algebraization-primary-LOCALONLY')
assert not K.exists(); K.mkdir()
url='https://arxiv.org/pdf/1308.4734v5'
with urllib.request.urlopen(url,timeout=45) as response:
    data=response.read(); status=response.status; headers=dict(response.headers)
assert data.startswith(b'%PDF-')
p=K/'Fujiwara-Kato2017-v5.pdf'; p.write_bytes(data)
t=K/'Fujiwara-Kato2017-v5.txt'
q=subprocess.run(['pdftotext','-layout',str(p),str(t)],capture_output=True)
assert q.returncode==0 and t.is_file()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
j=dict(retrieved_utc=datetime.now(timezone.utc).isoformat(),url=url,status=status,headers=headers,pdf=str(p),pdf_bytes=len(data),pdf_sha256=sha(p),text=str(t),text_bytes=t.stat().st_size,text_sha256=sha(t),literal_version='arXiv1308.4734v5,28February2017',original_pdf_bytes=True,whole_primary_read=False,mathematical_grant=False,full_source_published=False,auth_runtime_environment_changed=False,bibliographic_distinction='This Fujiwara-Kato2017 primary is an ALTERNATIVE, not GJKM FK88. GJKM FK88 is Freitag-Kiehl1988, Etale cohomology and the Weil conjecture.')
(K/'retrieval-binding.json').write_text(json.dumps(j,indent=2)+'\n')
print(json.dumps({q:j[q] for q in ('url','pdf_bytes','pdf_sha256','text_sha256','bibliographic_distinction')},indent=2))
