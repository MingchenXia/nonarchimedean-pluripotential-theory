import hashlib,json,pathlib,platform,sys
ROOT=pathlib.Path('/workspace/research/campaigns/round-259/P12.6-entire-original-candidate362-independent-proof-source-and-scope-review')
OUT=pathlib.Path.cwd(); (OUT/'evidence').mkdir(exist_ok=True); (OUT/'read-data').mkdir(exist_ok=True)
def digest(b):return hashlib.sha256(b).hexdigest()
sets={}; rows=[]
for name in ['mathematical-packet-bindings','private-primary-packet-bindings','book-context-bindings']:
 entries=json.loads((ROOT/(name+'.json')).read_text());sets[name]=entries
 for i,e in enumerate(entries):
  p=pathlib.Path(e['path']);b=p.read_bytes();rows.append({'set':name,'index':i,'path':str(p),'bytes':len(b),'sha256':digest(b),'matches':len(b)==e['bytes'] and digest(b)==e['sha256']})
(OUT/'evidence/input-audit.json').write_text(json.dumps({'environment':{'python':sys.version,'platform':platform.platform(),'cwd':str(OUT)},'entries':rows},indent=2))
mat=sets['mathematical-packet-bindings']
for index,label in [(50,'expanded'),(51,'actual')]:
 data=json.loads(pathlib.Path(mat[index]['path']).read_text())
 for note in data['notes']:
  (OUT/'read-data'/f'{label}-{note["id"]}.json').write_text(json.dumps(note,ensure_ascii=False,indent=2))
 (OUT/'read-data'/f'{label}-nontext.json').write_text(json.dumps({k:v for k,v in data.items() if k!='notes'},indent=2))
a=json.loads(pathlib.Path(mat[51]['path']).read_text());e=json.loads(pathlib.Path(mat[50]['path']).read_text())
compare={'actual_local_expanded_is_not_FINAL':pathlib.Path(mat[50]['path']).read_bytes()==pathlib.Path(mat[52]['path']).read_bytes(),'actual_count':len(a['notes']),'expanded_count':len(e['notes']),'fields':[{'id':x['id'],'equal':{k:x.get(k)==y.get(k) for k in set(x)|set(y)}} for x,y in zip(a['notes'],e['notes'])]}
(OUT/'evidence/FINAL-comparison.json').write_text(json.dumps(compare,indent=2))
paper=pathlib.Path(mat[48]['path']).read_bytes()
contain=[{'index':i,'name':pathlib.Path(mat[i]['path']).name,'literal_contained':pathlib.Path(mat[i]['path']).read_bytes() in paper} for i in range(14)]
(OUT/'evidence/grant-containment.json').write_text(json.dumps(contain,indent=2))
print('Files:',len(rows),'matching:',sum(x['matches'] for x in rows));print(json.dumps(compare,indent=2));print(json.dumps(contain,indent=2))
