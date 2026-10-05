from pathlib import Path
import json, hashlib, shutil, platform, subprocess

ROOT = Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(path,obj): (ROOT/path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
b=(ROOT/'input.json').read_bytes(); inp=json.loads(b)
(ROOT/'input-original.json').write_bytes(b)
dump('task-original.json',inp['task'])
(ROOT/'assignment-original.txt').write_text(inp['assignment'],encoding='utf-8')
a=inp['assignment']; lines=a.split('\n')
head='# Authorized primary-source cache catalogue and retained literal proof bodies'
p=a.index(head); start=a.index('{',p)
catalogue,end=json.JSONDecoder().raw_decode(a[start:])
dump('source-catalogue-input.json',catalogue)
(ROOT/'sources').mkdir(exist_ok=True); (ROOT/'source-extracts').mkdir(exist_ok=True)
checks=[]
for s in catalogue['sources']:
 for f in s['files']:
  src=Path(f['authorized_path']); data=src.read_bytes()
  actual=sha(data); assert actual==f['expected_sha256'],src
  dst=ROOT/f['local_copy']; dst.parent.mkdir(exist_ok=True); dst.write_bytes(data)
  checks.append({'source':s['id'],'version':s['version'],'url':s['public_source'],'file':f['local_copy'],'bytes':len(data),'sha256':actual})
units=[]
extra={'S2':[(911,1017),(1603,1730),(1731,1814),(1815,1885),(1886,1964),(1965,2017),(2018,2108),(2372,2510),(2511,2696),(2697,2755)],'S6':[(3730,3741),(3783,3945),(3825,3842)]}
for s in catalogue['sources']:
 fs=[f for f in s['files'] if f['local_copy'].endswith('.txt')]
 if not fs: continue
 f=fs[0]; raw=(ROOT/f['local_copy']).read_bytes(); ls=raw.decode('utf-8').split('\n')
 ranges=set(tuple(u['inclusive_LF']) for u in catalogue['units'] if u['source']==s['id'])
 ranges.update(extra.get(s['id'],[]))
 for lo,hi in sorted(ranges):
  literal='\n'.join(ls[lo-1:hi]); path=f'source-extracts/{s["id"]}-LF{lo}-{hi}.txt'
  (ROOT/path).write_text(literal,encoding='utf-8')
  units.append({'source':s['id'],'version':s['version'],'url':s['public_source'],'source_sha256':sha(raw),'inclusive_one_based_LF':[lo,hi],'literal_file':path,'literal_sha256':sha(literal.encode())})
dump('source-extracts/source-provenance.json',{'coordinate_rule':"UTF8 bytes decode; split('\\n'); inclusive one-based LF",'files':checks,'units':units,'retention_is_not_validation':True})
(ROOT/'embedded').mkdir(exist_ok=True)
headers=[(i,l) for i,l in enumerate(lines) if l.startswith('# ')]
for j,(i,l) in enumerate(headers):
 hi=headers[j+1][0] if j+1<len(headers) else len(lines)
 if 'TASK-GRANTED' in l or 'Exact scope' in l or 'Binding harmless' in l or 'New UNREVIEWED' in l or 'Direct curve' in l or 'Countable-field' in l:
  (ROOT/'embedded'/f'input-LF{i+1}-{hi}.txt').write_text('\n'.join(lines[i:hi]),encoding='utf-8')
versions={}
for cmd in [['python3','--version'],['pandoc','--version'],['pdflatex','--version']]:
 r=subprocess.run(cmd,capture_output=True,text=True); versions[cmd[0]]=(r.stdout+r.stderr).split('\n')[:2]
dump('environment.json',{'python':platform.python_version(),'platform':platform.platform(),'versions':versions,'supervised_compute_service':'No operator-provided supervised compute service exposed; no resource-heavy work launched.','cloud_environment_status':'Tool absent from enabled metadata; no credential or runtime configuration inspected or mutated.','input_bytes':len(b),'input_sha256':sha(b),'input_preserved':(ROOT/'input-original.json').read_bytes()==b})
print(json.dumps({'input_bytes':len(b),'input_sha256':sha(b),'source_files_checked':len(checks),'literal_units_retained':len(units)}))
