import json, pathlib, hashlib, platform, sys
ROOT=pathlib.Path('/workspace/research/campaigns/round-256/P12.6-specified-regularized-geometric-envelope-whole-original-completion')
OUT=pathlib.Path(__file__).resolve().parent
rows=[]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
 data=json.loads((ROOT/name).read_text())
 for i,e in enumerate(data):
  p=pathlib.Path(e['path']);b=p.read_bytes();h=hashlib.sha256(b).hexdigest()
  rows.append(dict(packet=name,index=i,path=str(p),bytes=len(b),sha256=h,match=len(b)==e['bytes'] and h==e['sha256']))
(OUT/'evidence/input-audit.json').write_text(json.dumps(dict(files=rows,all_match=all(r['match'] for r in rows),python=sys.version,platform=platform.platform(),heavy_compute='No supervised facility exposed; none needed or launched',environment_status_tool='Not exposed in callable tool metadata'),indent=2))
for name in ['original-task.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json','qualified-imported-note-bindings.json']:
 (OUT/'LOCALONLY'/name).write_bytes((ROOT/name).read_bytes())
math=json.loads((ROOT/'mathematical-packet-bindings.json').read_text())
for i in range(14):
 p=pathlib.Path(math[i]['path']);(OUT/'grants'/p.name).write_bytes(p.read_bytes())
# Extract every actual and expanded field as inert text, never execute supplied code.
for i in [20,21,35,36]:
 data=json.loads(pathlib.Path(math[i]['path']).read_text())
 for n in data['notes']:
  (OUT/'LOCALONLY'/f'{i}-{n["id"]}-all-fields.json').write_text(json.dumps(n,ensure_ascii=False,indent=2))
# Remove literal duplicates from large reader bodies, recording each exact replacement.
previous=[];comps=[]
for i in [0,1,2,3,5,6,7,8,9,10,11,12,13,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47]:
 s=pathlib.Path(math[i]['path']).read_text();previous.append((i,s))
for i in [17,33]:
 s=pathlib.Path(math[i]['path']).read_text();removed=[]
 for j,t in sorted(previous,key=lambda x:-len(x[1])):
  if t and t in s:
   k=s.count(t);s=s.replace(t,f'\n[ENTIRE EXACT DUPLICATE of bound index {j}; {len(t)} characters]\n');removed.append([j,k,len(t)])
 (OUT/'LOCALONLY'/f'reader-{i}-fresh.txt').write_text(s);comps.append(dict(index=i,removed=removed,remaining_characters=len(s)))
# Proof markdown literal wrappers versus complete proof bodies.
for a,b in [(42,43),(18,19)]:
 x=pathlib.Path(math[a]['path']).read_text();y=pathlib.Path(math[b]['path']).read_text()
 comps.append(dict(indices=[a,b],whole_first_contained=x in y))
(OUT/'evidence/duplicate-comparison.json').write_text(json.dumps(comps,indent=2))
print(json.dumps(dict(files=len(rows),all_match=all(r['match'] for r in rows),reader_fresh=comps),indent=2))
