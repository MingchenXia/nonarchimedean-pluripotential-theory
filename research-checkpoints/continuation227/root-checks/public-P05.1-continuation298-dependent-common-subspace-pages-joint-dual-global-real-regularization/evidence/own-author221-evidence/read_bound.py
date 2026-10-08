"""Read only an explicitly bound input, in bounded line/character chunks."""
import argparse, hashlib, json
from pathlib import Path
BASE=Path('/workspace/research/campaigns/round-221/P05.1-arbitrary-dependent-common-subspace-pages-joint-dual-global-real-regularization-paper')
p=argparse.ArgumentParser();p.add_argument('packet',choices=['math','primary']);p.add_argument('index',type=int);p.add_argument('start',type=int);p.add_argument('stop',type=int);a=p.parse_args()
manifest=BASE/('mathematical-packet-bindings.json' if a.packet=='math' else 'private-primary-packet-bindings.json')
z=json.loads(manifest.read_text())[a.index];path=Path(z['path']);raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==z['sha256']
assert z.get('format')!='pdf','Use the bound text for bounded statement/proof reading.'
s=raw.decode();assert 0<=a.start<a.stop<=len(s);assert a.stop-a.start<=42000
print(f"BOUND {a.packet}:{a.index} {path.name} CHARS [{a.start},{a.stop})/{len(s)} LF {s[:a.start].count(chr(10))+1}..{s[:a.stop].count(chr(10))+1}")
print(s[a.start:a.stop])
with Path('read-coverage.jsonl').open('a') as f:f.write(json.dumps({'packet':a.packet,'index':a.index,'path':str(path),'sha256':z['sha256'],'start':a.start,'stop':a.stop,'characters':len(s),'start_LF':s[:a.start].count(chr(10))+1,'end_LF':s[:a.stop].count(chr(10))+1})+'\n')
