from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, urllib.request

D = Path('/workspace/research/root-checks/continuation244-completion-and-GAGA-primary-LOCALONLY')
assert not D.exists()
D.mkdir()
sources = [
    ('Conrad1999-publisher', 'https://www.numdam.org/article/AIF_1999__49_2_473_0.pdf', 'Irreducible components of rigid spaces, AIF49(1999),473-541'),
    ('Conrad2006-publisher', 'https://www.numdam.org/item/10.5802/aif.2207.pdf', 'Relative ampleness in rigid geometry, AIF56(2006),1049-1126'),
]
def retrieve(item):
    label, url, identity = item
    record = dict(label=label, literal_url=url, identity=identity, attempted_utc=datetime.now(timezone.utc).isoformat(), full_source_published=False, authentication_or_environment_changed=False)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=45) as response:
            raw=response.read()
            record['response_url']=response.url
        assert raw.startswith(b'%PDF')
        pdf=D/(label+'.pdf'); pdf.write_bytes(raw)
        txt=D/(label+'.txt')
        subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True)
        info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
        record.update(status='retrieved',pdf_info=info,files=[dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in (pdf,txt)])
    except Exception as error:
        record.update(status='failed',error_type=type(error).__name__,error=str(error))
    return record
with ThreadPoolExecutor(max_workers=2) as executor:
    records=list(executor.map(retrieve,sources))
(D/'retrieval-record-LOCALONLY.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
