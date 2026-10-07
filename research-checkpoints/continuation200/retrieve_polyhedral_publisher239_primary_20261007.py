from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,urllib.request
R=Path('/workspace/research');D=R/'root-checks/continuation239-polyhedral-publisher-primary-LOCALONLY'
assert not D.exists();D.mkdir()
url='https://link.springer.com/content/pdf/10.1007/s00209-021-02869-6.pdf'
record=dict(attempted_utc=datetime.now(timezone.utc).isoformat(),literal_url=url,source='BBGS Convex analysis on polyhedral spaces, version of record2022, DOI10.1007/s00209-021-02869-6',authentication_or_environment_changed=False,full_primary_bytes_published=False)
try:
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as response:
        raw=response.read();record['response_url']=response.url
    assert raw.startswith(b'%PDF')
    p=D/'BBGS2022-publisher.pdf';p.write_bytes(raw)
    t=D/'BBGS2022-publisher.txt';subprocess.run(['pdftotext','-layout',str(p),str(t)],check=True)
    record.update(status='retrieved',files=[dict(path=str(f),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in (p,t)])
except Exception as e:
    record.update(status='failed',error_type=type(e).__name__,error=str(e))
(D/'retrieval-record-LOCALONLY.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
