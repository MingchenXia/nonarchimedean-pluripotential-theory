from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, urllib.request, fitz

D=Path('/workspace/research/root-checks/continuation253-formal-comparison-primary-LOCALONLY')
assert not D.exists(); D.mkdir()
sources=[('RaynaudGruson1971-publisher','https://link.springer.com/content/pdf/10.1007/BF01390094.pdf'),('Berkovich1993-publisher','https://www.numdam.org/item/PMIHES_1993__78__5_0.pdf')]
def retrieve(pair):
    name,url=pair
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Codex mathematical primary-source reading'})
        with urllib.request.urlopen(req,timeout=45) as response:
            data=response.read(); resolved=response.geturl(); ctype=response.headers.get('Content-Type')
        assert data.startswith(b'%PDF-')
        p=D/(name+'.pdf'); p.write_bytes(data)
        q=subprocess.run(['pdftotext','-layout',str(p),str(D/(name+'.txt'))],capture_output=True)
        (D/(name+'-pdftotext.stderr')).write_bytes(q.stderr); assert q.returncode==0
        t=D/(name+'.txt')
        return dict(name=name,literal_url=url,resolved_url=resolved,content_type=ctype,pdf_path=str(p),pdf_bytes=len(data),pdf_sha256=hashlib.sha256(data).hexdigest(),pdf_pages=len(fitz.open(p)),text_path=str(t),text_bytes=t.stat().st_size,text_sha256=hashlib.sha256(t.read_bytes()).hexdigest(),pdftotext_exit_code=q.returncode,pdftotext_diagnostics=q.stderr.decode(errors='replace'),retrieved=True)
    except Exception as e:
        return dict(name=name,literal_url=url,retrieved=False,error=type(e).__name__+': '+str(e))
with ThreadPoolExecutor(max_workers=2) as pool: results=list(pool.map(retrieve,sources))
j=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),purpose='Independent198 missing immediate primary units14/15 for direct formal H0 GAGA. Retrieval only; no proof or applicability certified.',sources=results,source_proofs_read=False,full_primary_files_published=False,no_auth_account_runtime_environment_changed=True,no_hot_feedback=True)
(D/'retrieval-binding.json').write_text(json.dumps(j,indent=2)+'\n')
print(json.dumps(j,indent=2))
