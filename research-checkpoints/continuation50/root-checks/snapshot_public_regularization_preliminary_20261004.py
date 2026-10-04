from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

R=Path('/workspace/research')
for n,atom,stem,worker in [(41,'P02.1','P02.1-public-source-decreasing-real-PL','codex-RyjJ79'),
                          (42,'P02.2','P02.2-public-source-decreasing-LFS','codex-gsYJxq')]:
    source=R/'campaigns'/f'round-{n}'/stem/'artifacts'/worker
    dest=R/'root-checks'/f'public-regularization-round-{n}-preliminary-reader'; dest.mkdir(exist_ok=False)
    records=[]
    for name in [f'{atom}-argument.md',f'{atom}-paper.tex','status.json','source-extracts/source-provenance.json']:
        p=source/name
        if not p.is_file(): continue
        data=p.read_bytes(); q=dest/name; q.parent.mkdir(parents=True,exist_ok=True); q.write_bytes(data)
        records.append({'origin':str(p),'file':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                        'LF_lines':len(data.decode().split('\n'))})
    (dest/'snapshot.json').write_text(json.dumps({'created_utc':datetime.now(timezone.utc).isoformat(),
        'state':'Preliminary sequential artifact snapshot; author still running; not a final or atomic campaign result.',
        'files':records,'feedback_sent':False,'mathematical_acceptance':False},indent=2)+'\n')
    print(json.dumps({'round':n,'files':records},ensure_ascii=False))
