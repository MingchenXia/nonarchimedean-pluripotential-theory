"""Read only enumerated bound data, in bounded character chunks; no execution."""
import argparse, hashlib, json
from pathlib import Path

BASE = Path('/workspace/research/campaigns/round-219/P05.1-common-subspace-independent-normal-pages-all-continuous-real-regularization-paper')
ap = argparse.ArgumentParser()
ap.add_argument('packet', choices=['math', 'primary', 'original'])
ap.add_argument('index', type=int)
ap.add_argument('start', type=int)
ap.add_argument('stop', type=int)
args = ap.parse_args()
if args.packet == 'original':
    path = BASE / 'original-task.json'
else:
    name = 'mathematical-packet-bindings.json' if args.packet == 'math' else 'private-primary-packet-bindings.json'
    entries = json.loads((BASE / name).read_text())
    path = Path(entries[args.index]['path'])
data = path.read_bytes()
if args.packet != 'original':
    assert hashlib.sha256(data).hexdigest() == entries[args.index]['sha256']
txt = data.decode('utf-8')
assert 0 <= args.start <= args.stop <= len(txt)
assert args.stop - args.start <= 28000
print(json.dumps({'packet': args.packet, 'index': args.index, 'chars': [args.start, args.stop], 'total_chars': len(txt), 'first_LF': txt[:args.start].count('\n') + 1, 'last_LF': txt[:args.stop].count('\n') + 1}))
print(txt[args.start:args.stop])
with Path('read-coverage.jsonl').open('a') as out:
    out.write(json.dumps({'packet': args.packet, 'index': args.index, 'start': args.start, 'stop': args.stop, 'sha256': hashlib.sha256(data).hexdigest()}) + '\n')
