import json,sys
from pathlib import Path
base=Path('/workspace/research/campaigns/round-220/P05.1-unchanged-isolated-affine-crossings-whole-independent-native-local-source-audit')
a=json.loads((base/'private-primary-packet-bindings.json').read_text());obj=a[int(sys.argv[1])];lines=Path(obj['path']).read_text().splitlines();lo,hi=map(int,sys.argv[2:4]);t='\n'.join(f'{i}: {lines[i-1]}' for i in range(lo,min(hi,len(lines))+1))
print(Path(obj['path']).name,'LF',lo,hi);print(t)
Path('LOCALONLY').mkdir(exist_ok=True);Path(f'LOCALONLY/{Path(obj["path"]).stem}-{lo}-{hi}.txt').write_text(t+'\n')
with Path('primary-read-log.jsonl').open('a') as f:f.write(json.dumps({'id':'p'+sys.argv[1],'LF_start':lo,'LF_end':min(hi,len(lines))})+'\n')
