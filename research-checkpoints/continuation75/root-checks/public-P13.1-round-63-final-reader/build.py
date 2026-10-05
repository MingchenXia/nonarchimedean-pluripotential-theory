from pathlib import Path
import subprocess,json,hashlib,shutil
root=Path.cwd();records=[]
def run(name,cmd):
 p=subprocess.run(cmd,text=True,capture_output=True)
 Path(name+'.stdout').write_text(p.stdout);Path(name+'.stderr').write_text(p.stderr)
 records.append({'command':cmd,'returncode':p.returncode,'stdout':name+'.stdout','stderr':name+'.stderr'})
 if p.returncode:print(p.stdout[-3500:],p.stderr[-2000:]);raise RuntimeError(cmd)
 return p
try:
 run('pandoc',['pandoc','P13.1-argument.md','--standalone','--to=latex','--output=P13.1-paper.tex'])
 for i in (1,2):
  run(f'tex-pass-{i}',['pdflatex','-interaction=nonstopmode','-halt-on-error','P13.1-paper.tex'])
  shutil.copyfile('P13.1-paper.log',f'tex-pass-{i}.log')
 run('pdfinfo',['pdfinfo','P13.1-paper.pdf'])
finally:
 versions={}
 for tool in ['pandoc','pdflatex']:
  versions[tool]=subprocess.run([tool,'--version'],text=True,capture_output=True).stdout.split('\n')[0]
 outputs={x:hashlib.sha256(Path(x).read_bytes()).hexdigest() for x in ['P13.1-argument.md','P13.1-paper.tex','P13.1-paper.pdf'] if Path(x).exists()}
 Path('build-report.json').write_text(json.dumps({'commands':records,'versions':versions,'outputs_sha256':outputs,'input_preserved':Path('input.json').read_bytes()==Path('input-original.json').read_bytes()},indent=2)+'\n')
print(json.dumps({'commands_succeeded':len(records),'pdf':'P13.1-paper.pdf'}))
