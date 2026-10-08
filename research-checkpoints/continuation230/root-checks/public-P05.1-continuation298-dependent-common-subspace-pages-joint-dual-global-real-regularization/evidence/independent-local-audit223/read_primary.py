"""Literal LF source unit extraction, local-only excerpts."""
import json
import sys
from pathlib import Path
rows=json.loads(Path('frozen-private-primary-packet-bindings.json').read_text())
label=sys.argv[1]
lo,hi=map(int,sys.argv[2:])
r=next(x for x in rows if x['label']==label and x['format']=='txt')
lines=Path(r['path']).read_text().split('\n')
assert 1<=lo<=hi<=len(lines)
body='\n'.join(f'{i}: {lines[i-1]}' for i in range(lo,hi+1))+'\n'
assert len(body)<=20000
Path('LOCALONLY').mkdir(exist_ok=True)
Path(f'LOCALONLY/{label}-LF-{lo}-{hi}.txt').write_text(body)
with Path('primary-display-requests.jsonl').open('a') as f:
    f.write(json.dumps(dict(label=label,first_LF=lo,last_LF=hi,source_sha256=r['sha256'],status='requested display; inspect for truncation'))+'\n')
print(body)
