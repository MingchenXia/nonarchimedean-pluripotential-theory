"""Read a bounded whole original unit using LF numbering; extracts stay local."""
import argparse,json,hashlib
from pathlib import Path
BASE=Path('/workspace/research/campaigns/round-221/P05.1-arbitrary-dependent-common-subspace-pages-joint-dual-global-real-regularization-paper')
p=argparse.ArgumentParser();p.add_argument('index',type=int,choices=[1,3]);p.add_argument('start',type=int);p.add_argument('end',type=int);a=p.parse_args()
z=json.loads((BASE/'private-primary-packet-bindings.json').read_text())[a.index];raw=Path(z['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==z['sha256'];lines=raw.decode().split('\n');assert 1<=a.start<=a.end<=len(lines);assert a.end-a.start<240
out=f"PRIMARY {z['label']} LF {a.start}..{a.end} SHA256 {z['sha256']}\n"+'\n'.join(f'{j}: {lines[j-1]}' for j in range(a.start,a.end+1))
print(out);Path('LOCALONLY').mkdir(exist_ok=True);Path(f"LOCALONLY/{z['label']}-LF-{a.start}-{a.end}.txt").write_text(out+'\n')
with Path('primary-unit-coverage.jsonl').open('a') as f:f.write(json.dumps({'index':a.index,'label':z['label'],'path':z['path'],'sha256':z['sha256'],'LF_start':a.start,'LF_end':a.end})+'\n')
