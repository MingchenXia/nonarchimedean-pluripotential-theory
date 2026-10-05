from pathlib import Path
import subprocess,json,hashlib,platform,sys,shutil
ROOT=Path(__file__).resolve().parent;logs=ROOT/'build-logs';logs.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
versions={}
for name,cmd in [('python',[sys.executable,'--version']),('pandoc',['pandoc','--version']),('pdftex',['pdflatex','--version'])]:
 p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
 versions[name]={'command':cmd,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
(ROOT/'environment.json').write_text(json.dumps({'cwd':str(ROOT),'platform':platform.platform(),'python_executable':sys.executable,'versions':versions,'execution_constraints':'Native existing Python, Pandoc and pdfTeX. No network, installations, workers, external messages, runtime changes or resource-heavy compute.'},indent=2)+'\n')
commands=[['pandoc','P13.2-argument.md','--standalone','--from=markdown+tex_math_single_backslash','--to=latex','--output=P13.2-paper.tex']]+[['pdflatex','-interaction=nonstopmode','-halt-on-error','P13.2-paper.tex'] for _ in range(2)]
results=[]
for i,cmd in enumerate(commands):
 label='pandoc' if i==0 else f'tex-pass-{i}'
 p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
 (logs/f'{label}.stdout').write_text(p.stdout);(logs/f'{label}.stderr').write_text(p.stderr)
 if i>0 and (ROOT/'P13.2-paper.log').exists():shutil.copyfile(ROOT/'P13.2-paper.log',logs/f'{label}.log')
 results.append({'label':label,'command':cmd,'cwd':str(ROOT),'returncode':p.returncode,'stdout':str((logs/f'{label}.stdout').relative_to(ROOT)),'stderr':str((logs/f'{label}.stderr').relative_to(ROOT))})
 if p.returncode:
  (ROOT/'build-report.json').write_text(json.dumps({'commands':results,'status':'failed'},indent=2)+'\n')
  print(p.stdout[-4000:]);raise SystemExit(p.returncode)
report={'commands':results,'status':'two pdfTeX passes succeeded','artifacts':{n:{'sha256':sha(ROOT/n),'bytes':(ROOT/n).stat().st_size} for n in ['P13.2-argument.md','P13.2-paper.tex','P13.2-paper.pdf']},'limits':'Compilation success is an observation, not mathematical validation.'}
(ROOT/'build-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
