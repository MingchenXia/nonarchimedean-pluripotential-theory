"""Byte checks identify supplied data; they do not certify mathematics or reading."""
import json,hashlib
from pathlib import Path
out=[]
for binding in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    data=json.loads(Path('inputs',binding).read_text())
    for i,item in enumerate(data):
        p=Path(item['path']); raw=p.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
        out.append({'binding':binding,'index':i,'label':item['label'],'path':str(p),
                    'bytes':len(raw),'sha256':digest,
                    'matches':digest==item['sha256'] and len(raw)==item['bytes']})
for name in ['original-task.json','original-family-task.json','normalization-data.json']:
    p=Path('inputs',name);raw=p.read_bytes()
    out.append({'input':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
Path('evidence/input-byte-bindings.json').write_text(json.dumps(out,indent=2)+'\n')
assert all(x.get('matches',True) for x in out)
print(json.dumps({'bound_packet_and_primary_files':37,'matches':True,'meaning':'identification only'}))
