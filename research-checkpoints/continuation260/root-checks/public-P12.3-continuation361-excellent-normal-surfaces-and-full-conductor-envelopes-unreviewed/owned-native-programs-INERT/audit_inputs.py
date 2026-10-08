import json,hashlib,pathlib,platform,sys
BASE=pathlib.Path('/workspace/research/campaigns/round-257/P12.3-excellent-normal-surfaces-and-whole-residual-envelope-completion')
ROOT=pathlib.Path.cwd(); (ROOT/'reports').mkdir(exist_ok=True)
rows=[]
for kind,name in [('mathematical','mathematical-packet-bindings.json'),('primary-LOCALONLY','private-primary-packet-bindings.json'),('context-LOCALONLY','book-context-bindings.json')]:
 raw=(BASE/name).read_bytes(); dst=ROOT/'inputs'/kind; dst.mkdir(parents=True,exist_ok=True)
 (ROOT/'inputs'/name).write_bytes(raw)
 for i,r in enumerate(json.loads(raw)):
  p=pathlib.Path(r['path']); data=p.read_bytes(); h=hashlib.sha256(data).hexdigest()
  local=dst/(f'{i:02d}-'+p.name); local.write_bytes(data)
  rows.append({**r,'kind':kind,'index':i,'local':str(local.relative_to(ROOT)),'actual_bytes':len(data),'actual_sha256':h,'match':len(data)==r['bytes'] and h==r['sha256']})
(ROOT/'reports/input-audit.json').write_text(json.dumps(rows,indent=2)+'\n')
(ROOT/'reports/environment.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'cwd':str(ROOT),'network_used':False,'supplied_programs_executed':False,'supervised_compute':'not supplied; not needed'},indent=2)+'\n')
print(json.dumps({'records':len(rows),'matched':sum(x['match'] for x in rows),'bytes':sum(x['actual_bytes'] for x in rows)}))
