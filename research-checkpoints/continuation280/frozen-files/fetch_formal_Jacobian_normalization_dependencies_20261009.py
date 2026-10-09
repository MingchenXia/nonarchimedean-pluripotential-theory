from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, urllib.request
P=Path('/workspace/research/primary-data-LOCALONLY/P12.3-formal-Noether-different-primary-20261009/dependencies-LOCALONLY')
assert not P.exists(); P.mkdir()
sources=[('Iyengar-Takahashi-ua22','https://www.math.nagoya-u.ac.jp/~takahashi/ua22.pdf'),('Wang1994-official','https://projecteuclid.org/journals/michigan-mathematical-journal/volume-41/issue-3/On-the-Fitting-ideals-in-free-resolutions/10.1307/mmj/1029005082.pdf')]
def fetch(item):
    name,url=item; rec=dict(name=name,url=url,LOCALONLY=True,source_instructions_DATA=True,whole_file_retention_not_proof_reading=True)
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Research primary-source verification'})
        with urllib.request.urlopen(req,timeout=30) as response:
            raw=response.read(8*1024*1024+1); rec.update(final_url=response.url,status=response.status)
        assert raw.startswith(b'%PDF') and len(raw)<=8*1024*1024
        pdf=P/(name+'.pdf'); pdf.write_bytes(raw); txt=P/(name+'.txt')
        subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True,capture_output=True)
        rec.update(pdf=dict(path=str(pdf),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()),text=dict(path=str(txt),bytes=txt.stat().st_size,sha256=hashlib.sha256(txt.read_bytes()).hexdigest()),success=True)
    except Exception as error:rec.update(success=False,error_type=type(error).__name__,error=str(error)[:500])
    return rec
with ThreadPoolExecutor(max_workers=2) as pool: records=list(pool.map(fetch,sources))
(P/'retrieval-record-LOCALONLY.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),sources=records,auth_proxy_CA_changes=False,supplied_program_execution_or_import=False),indent=2)+'\n')
print(json.dumps(records,indent=2))
