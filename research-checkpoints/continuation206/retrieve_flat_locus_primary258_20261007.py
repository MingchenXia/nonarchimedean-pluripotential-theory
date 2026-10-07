from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, urllib.request, subprocess, fitz

D=Path('/workspace/research/root-checks/continuation258-flat-locus-primary-LOCALONLY')
assert not D.exists()
D.mkdir()
url='https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0013/PPN356556735_0013.pdf'
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'literal_url':url,'purpose':'Original 1971 Inventiones13 journal scan for Raynaud-Gruson Premiere partie3.4.6; retrieval only; no proof read or certified','full_primary_published':False,'no_runtime_or_account_change':True}
try:
 req=urllib.request.Request(url,headers={'User-Agent':'Codex mathematical primary-source reading'})
 with urllib.request.urlopen(req,timeout=45) as response:
  data=response.read(); record.update(resolved_url=response.geturl(),content_type=response.headers.get('Content-Type'))
 assert data.startswith(b'%PDF-')
 pdf=D/'Inventiones1971-volume13-original.pdf'; pdf.write_bytes(data)
 txt=D/'Inventiones1971-volume13-original.txt'
 r=subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],capture_output=True)
 (D/'pdftotext.stderr').write_bytes(r.stderr)
 assert r.returncode==0
 record.update(retrieved=True,pdf_path=str(pdf),pdf_bytes=len(data),pdf_sha256=hashlib.sha256(data).hexdigest(),pdf_pages=len(fitz.open(pdf)),text_path=str(txt),text_bytes=txt.stat().st_size,text_sha256=hashlib.sha256(txt.read_bytes()).hexdigest(),pdftotext_exit_code=r.returncode,pdftotext_diagnostics=r.stderr.decode(errors='replace'))
except Exception as e:
 record.update(retrieved=False,error=type(e).__name__+': '+str(e))
(D/'retrieval-binding.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
