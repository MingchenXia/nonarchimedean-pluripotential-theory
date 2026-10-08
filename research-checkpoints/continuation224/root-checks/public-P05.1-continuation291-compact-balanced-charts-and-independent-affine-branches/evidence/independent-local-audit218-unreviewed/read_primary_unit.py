"""Own read-only original-unit extraction; original excerpts stay LOCALONLY."""
from pathlib import Path
import argparse,hashlib,json
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser()
ap.add_argument('source',choices=['BMPS','BBGS'])
ap.add_argument('first',type=int)
ap.add_argument('last',type=int)
ap.add_argument('--display',action='store_true')
args=ap.parse_args()
manifest=json.loads((root/'inputs/private-primary-packet-bindings.json').read_text())
entry=next(e for e in manifest if e['label']==args.source and e['format']=='txt')
raw=Path(entry['path']).read_bytes()
assert hashlib.sha256(raw).hexdigest()==entry['sha256']
lines=raw.decode().split('\n')
assert 1<=args.first<=args.last<=len(lines)
body='\n'.join(f'{i}: {lines[i-1]}' for i in range(args.first,args.last+1))+'\n'
path=root/'LOCALONLY'/f'{args.source}-{args.first}-{args.last}.txt'
path.parent.mkdir(exist_ok=True)
path.write_text(body)
print(json.dumps(dict(source=args.source,LF=[args.first,args.last],sha256=entry['sha256'],
                      output=str(path.relative_to(root)),displayed=args.display)))
if args.display:
    assert len(body)<=17500,'Choose bounded whole-unit chunks for display.'
    print(body)
