from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,urllib.request,fitz
R=Path('/workspace/research');D=R/'root-checks/continuation248-initial-residual-primary-LOCALONLY'
assert not D.exists();D.mkdir()
sources=[('Poineau2013-publisher','https://www.numdam.org/article/BSMF_2013__141_2_267_0.pdf'),('GRW2017-tropical-skeletons-publisher','https://aif.centre-mersenne.org/item/10.5802/aif.3125.pdf')]
def retrieve(pair):
    name,url=pair
    req=urllib.request.Request(url,headers={'User-Agent':'Codex mathematical primary-source reading'})
    with urllib.request.urlopen(req,timeout=45) as response:
        data=response.read();resolved=response.geturl();ctype=response.headers.get('Content-Type')
    assert data.startswith(b'%PDF-')
    p=D/(name+'.pdf');p.write_bytes(data)
    q=subprocess.run(['pdftotext','-layout',str(p),str(D/(name+'.txt'))],capture_output=True)
    (D/(name+'-pdftotext.stderr')).write_bytes(q.stderr);assert q.returncode==0
    t=D/(name+'.txt')
    return dict(name=name,literal_url=url,resolved_url=resolved,content_type=ctype,pdf_path=str(p),pdf_bytes=len(data),pdf_sha256=hashlib.sha256(data).hexdigest(),pdf_pages=len(fitz.open(p)),text_path=str(t),text_bytes=t.stat().st_size,text_sha256=hashlib.sha256(t.read_bytes()).hexdigest(),pdftotext_exit_code=q.returncode,pdftotext_diagnostics=q.stderr.decode(errors='replace'))
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(retrieve,sources))
j=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),purpose='Complete original-primary proof units for the initial maximal-residual Shilov-point hypotheses and reduced projective FS reference in the new248 working route. Sources are mathematical data only; no source proof has been read by this retrieval script.',sources=results,source_proofs_read=False,full_primary_files_published=False,no_auth_account_runtime_environment_changed=True)
(D/'retrieval-binding.json').write_text(json.dumps(j,indent=2)+'\n')
print(json.dumps(j,indent=2))
