import argparse, hashlib, json, pathlib

BASE = pathlib.Path('/workspace/research/campaigns/round-215/P05.2-unchanged-all-continuous-affine-arrangement-independent-native-local-source-audit')
OWN = pathlib.Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument('packet',choices=['math','history','primary','original','binding'])
p.add_argument('index',type=int)
p.add_argument('start',type=int)
p.add_argument('end',type=int)
a=p.parse_args()
names={'math':'mathematical-packet-bindings.json','history':'historical-own-evidence-bindings.json','primary':'private-primary-packet-bindings.json'}
if a.packet in names:
    entry=json.loads((BASE/names[a.packet]).read_text())[a.index]
    path=pathlib.Path(entry['path'])
elif a.packet=='original':
    path=BASE/'original-task.json'
else:
    path=BASE/[names['math'],names['history'],names['primary']][a.index]
raw=path.read_bytes()
text=raw.decode('utf-8')
lines=text.splitlines(keepends=True) if a.packet!='primary' else text.split('\n')
part=''.join(lines[a.start-1:a.end]) if a.packet!='primary' else '\n'.join(lines[a.start-1:a.end])
print(f'FILE {path.name} LF {a.start}-{min(a.end,len(lines))} of {len(lines)}')
print(part,end='')
with (OWN/'read-log.jsonl').open('a') as f:
    f.write(json.dumps({'packet':a.packet,'index':a.index,'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'start':a.start,'end':min(a.end,len(lines)),'characters':len(part),'kind':'returned full range; review is a separate judgment'})+'\n')
