import json, pathlib, hashlib, platform, sys
ROOT=pathlib.Path('/workspace/research/campaigns/round-255/P12.6-whole-original-finite-transfer-independent-reconstruction')
OUT=pathlib.Path.cwd(); (OUT/'evidence').mkdir(exist_ok=True); (OUT/'review-data-LOCALONLY').mkdir(exist_ok=True)
records=[]
for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
 manifest=json.loads((ROOT/name).read_text())
 for row in manifest:
  p=pathlib.Path(row['path']); data=p.read_bytes(); h=hashlib.sha256(data).hexdigest()
  records.append(dict(manifest=name,path=str(p),bytes=len(data),sha256=h,match=len(data)==row['bytes'] and h==row['sha256']))
(OUT/'evidence'/'input-audit.json').write_text(json.dumps({'files':records,'environment':{'python':sys.version,'platform':platform.platform(),'cwd':str(OUT)},'success_is_not_mathematical_proof':True},indent=2))
math=json.loads((ROOT/'mathematical-packet-bindings.json').read_text()); proof=pathlib.Path(math[18]['path']).read_text(); reader=pathlib.Path(math[17]['path']).read_text()
comparison={'proof_entirely_in_reader':proof in reader,'grant_bodies_entirely_in_reader':[],'native_notes':[],'actual_final':[]}
for row in math[:14]: comparison['grant_bodies_entirely_in_reader'].append({'name':pathlib.Path(row['path']).name,'contained':pathlib.Path(row['path']).read_text() in reader})
for label,index in [('expanded',20),('actual',21)]:
 packet=json.loads(pathlib.Path(math[index]['path']).read_text()); notes=packet.get('notes',packet) if isinstance(packet,dict) else packet
 for n in notes:
  dest=OUT/'review-data-LOCALONLY'/f'{label}-{n["id"]}.txt'; dest.write_text(json.dumps(n,ensure_ascii=False,indent=2))
  comparison['native_notes' if label=='expanded' else 'actual_final'].append({'id':n['id'],'text_bytes':len(n['text'].encode()),'whole_text_in_proof':n['text'] in proof,'keys':list(n)})
(OUT/'evidence'/'duplicate-body-comparison.json').write_text(json.dumps(comparison,indent=2))
print(json.dumps({'files':len(records),'mismatches':[r['path'] for r in records if not r['match']],'comparison':comparison},indent=2))
