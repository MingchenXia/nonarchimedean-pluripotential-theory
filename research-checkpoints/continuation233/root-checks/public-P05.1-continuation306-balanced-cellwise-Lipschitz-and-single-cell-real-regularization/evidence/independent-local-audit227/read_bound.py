"""Fresh read-only bounded reader: literal LF coordinates, no supplied execution."""
import argparse, hashlib, json, pathlib

BASE = pathlib.Path('/workspace/research/campaigns/round-227/P05.1-balanced-cellwise-Lipschitz-and-single-cell-real-majorants-independent-whole-source-audit')
FILES = {'math': 'mathematical-packet-bindings.json', 'evidence': 'historical-own-evidence-bindings.json', 'primary': 'private-primary-packet-bindings.json'}
parser = argparse.ArgumentParser()
parser.add_argument('kind', choices=FILES)
parser.add_argument('index', type=int)
parser.add_argument('start', type=int, nargs='?', default=0)
parser.add_argument('end', type=int, nargs='?', default=20000)
parser.add_argument('--lf', action='store_true')
a = parser.parse_args()
row = json.loads((BASE / FILES[a.kind]).read_text())[a.index]
b = pathlib.Path(row['path']).read_bytes()
assert hashlib.sha256(b).hexdigest() == row['sha256']
assert len(b) == row['bytes']
if a.lf:
    lines = b.split(b'\n')
    part = b'\n'.join(lines[a.start-1:a.end])
else:
    part = b[a.start:a.end]
print(f"BOUND {a.kind}:{a.index} {pathlib.Path(row['path']).name} sha256={row['sha256']} range={a.start}:{a.end} {'LF' if a.lf else 'bytes'}")
print(part.decode('utf-8', errors='replace'))
with pathlib.Path('reader-ranges.jsonl').open('a') as out:
    out.write(json.dumps({'kind':a.kind,'index':a.index,'start':a.start,'end':a.end,'coordinate':'LF' if a.lf else 'byte','length':len(part),'sha256':row['sha256']})+'\n')
