import sys,json,hashlib
from pathlib import Path
BASE=Path('/workspace/research/campaigns/round-220/P05.1-unchanged-isolated-affine-crossings-whole-independent-native-local-source-audit')
NAMES={'m':'mathematical-packet-bindings.json','h':'historical-own-evidence-bindings.json','p':'private-primary-packet-bindings.json'}
if sys.argv[1]=='inventory':
 out=[]
 for k,n in NAMES.items():
  data=json.loads((BASE/n).read_text())
  for i,x in enumerate(data):
   b=Path(x['path']).read_bytes();out.append(dict(id=f'{k}{i}',**x,actual_sha256=hashlib.sha256(b).hexdigest(),actual_bytes=len(b),actual_LF_lines=b.count(b'\n'),matches=hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['bytes']))
 Path('frozen-file-bindings.json').write_text(json.dumps(out,indent=2)+'\n')
 print(len(out),'bound objects;',sum(x['matches'] for x in out),'identity matches')
 print('original task exists:',(BASE/'original-task.json').is_file())
elif sys.argv[1]=='read':
 k=sys.argv[2][0];i=int(sys.argv[2][1:]);x=json.loads((BASE/NAMES[k]).read_text())[i];s=Path(x['path']).read_text();a=int(sys.argv[3]);b=min(int(sys.argv[4]),len(s))
 print(f"OBJECT {k}{i}: {Path(x['path']).name}; characters [{a},{b}) of {len(s)}; LF lines {s[:a].count(chr(10))+1}-{s[:b].count(chr(10))+1}")
 print(s[a:b])
 with Path('bounded-read-log.jsonl').open('a') as f:f.write(json.dumps({'id':f'{k}{i}','start':a,'end':b,'total':len(s),'LF_start':s[:a].count(chr(10))+1,'LF_end':s[:b].count(chr(10))+1})+'\n')
