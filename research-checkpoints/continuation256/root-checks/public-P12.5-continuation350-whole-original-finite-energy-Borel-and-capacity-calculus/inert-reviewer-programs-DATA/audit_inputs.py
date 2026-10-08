import json,hashlib,pathlib,shutil,platform,sys,datetime
ROOT=pathlib.Path('/workspace/research/campaigns/round-252/P12.5-whole-original-energy-and-Borel-calculus-independent-review')
OUT=pathlib.Path.cwd(); (OUT/'evidence').mkdir(exist_ok=True)
result=[]
for name,folder in [('mathematical-packet-bindings.json','mathematical'),('book-context-bindings.json','context'),('historical-own-evidence-bindings.json','history'),('private-primary-packet-bindings.json','primary-LOCALONLY')]:
 records=json.loads((ROOT/name).read_text()); dest=OUT/'inputs'/folder;dest.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(ROOT/name,OUT/'inputs'/name)
 for i,r in enumerate(records):
  p=pathlib.Path(r['path']); row=dict(r); row['category']=folder
  if p.is_file():
   b=p.read_bytes(); row.update(actual_bytes=len(b),actual_sha256=hashlib.sha256(b).hexdigest());row['match']=row['actual_bytes']==r['bytes'] and row['actual_sha256']==r['sha256'];local=dest/(f'{i:02d}-'+p.name); local.write_bytes(b);row['local_path']=str(local)
  else:row['available']=False; row['match']=False
  result.append(row)
(OUT/'evidence'/'input-bindings.json').write_text(json.dumps(result,indent=2))
(OUT/'evidence'/'environment.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'cwd':str(OUT),'provided_supervised_compute':False,'heavy_compute_used':False,'supplied_code_executed':False,'compilation':False},indent=2))
# Grant-body matching: full supplied prose components compared with exact bound files, no historical reading inferred.
incoming=json.loads((OUT/'input.json').read_text());notes={n['id']:n for n in incoming['notes']}
markers={'G331':[('BEGIN ENTIRE P12.2-paper.tex\n','\nEND ENTIRE P12.2-paper.tex',0),('BEGIN ENTIRE mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json\n','\nEND ENTIRE mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json',1),('BEGIN ENTIRE source-application-ledger.md\n','\nEND ENTIRE source-application-ledger.md',2),('BEGIN ENTIRE exact-scope.md\n','\nEND ENTIRE exact-scope.md',3)]}
math=json.loads((ROOT/'mathematical-packet-bindings.json').read_text()); matches=[]
for note,entries in markers.items():
 t=notes[note]['text']
 for start,end,i in entries:
  s=t.split(start,1)[1].split(end,1)[0];b=pathlib.Path(math[i]['path']).read_text(); matches.append({'grant':note,'component':i,'exact_match':s==b,'match_ignoring_framing_newlines':s.strip('\n')==b.strip('\n'),'provided_bytes':len(s.encode()),'bound_bytes':len(b.encode())})
t=notes['B341']['text'];ids=[5,6,7,8,9,10,11];parts=t.split('===== ENTIRE QUALIFIED B341 COMPONENT: ')[1:]
for i,part in zip(ids,parts):
 heading,s=part.split(' =====\n',1);b=pathlib.Path(math[i]['path']).read_text();matches.append({'grant':'B341','component':i,'name':heading,'exact_match':s==b,'match_ignoring_framing_newlines':s.strip('\n')==b.strip('\n'),'provided_bytes':len(s.encode()),'bound_bytes':len(b.encode())})
(OUT/'evidence'/'incoming-grant-component-matches.json').write_text(json.dumps(matches,indent=2))
# Retain all actual FINAL fields separately, and all expanded fields separately, as data.
for i,tag in [(19,'actual-FINAL'),(18,'expanded-native')]:
 d=json.loads(pathlib.Path(math[i]['path']).read_text());target=OUT/'review-data'/tag;target.mkdir(parents=True,exist_ok=True)
 for n in d['notes']:(target/(n['id']+'.json')).write_text(json.dumps(n,ensure_ascii=False,indent=2))
print(json.dumps({'bound_records':len(result),'matches':sum(r['match'] for r in result),'grant_components':matches},indent=2))
