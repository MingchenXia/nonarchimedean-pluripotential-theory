from pathlib import Path
import subprocess, shutil, json, hashlib, platform, sys

root=Path(__file__).resolve().parent
logs=root/'build-logs';logs.mkdir(exist_ok=True)
environment={'python':sys.version,'platform':platform.platform(),'cwd':str(root),'tools':{}}
for name in ['pandoc','pdflatex']:
    exe=shutil.which(name)
    assert exe, 'Existing required tool unavailable: '+name
    ver=subprocess.run([exe,'--version'],capture_output=True,text=True)
    environment['tools'][name]={'path':exe,'version':ver.stdout.splitlines()[:3],'returncode':ver.returncode}
    (logs/(name+'-version.stdout')).write_text(ver.stdout)
    (logs/(name+'-version.stderr')).write_text(ver.stderr)
Path('environment.json').write_text(json.dumps(environment,indent=2)+'\n')
commands=[('pandoc',[environment['tools']['pandoc']['path'],'P16.1-argument.md','--standalone','--from=markdown+tex_math_dollars','--to=latex','--output=P16.1-paper.tex']),
          ('tex-pass-1',[environment['tools']['pdflatex']['path'],'-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex']),
          ('tex-pass-2',[environment['tools']['pdflatex']['path'],'-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex'])]
results=[]
for label,cmd in commands:
    process=subprocess.run(cmd,cwd=root,capture_output=True)
    (logs/(label+'.stdout')).write_bytes(process.stdout)
    (logs/(label+'.stderr')).write_bytes(process.stderr)
    if label.startswith('tex') and (root/'P16.1-paper.log').exists():
        shutil.copyfile(root/'P16.1-paper.log',logs/(label+'.log'))
    results.append({'label':label,'command':cmd,'returncode':process.returncode,
                    'stdout':str((logs/(label+'.stdout')).relative_to(root)),
                    'stderr':str((logs/(label+'.stderr')).relative_to(root)),
                    'pass_log':str((logs/(label+'.log')).relative_to(root)) if label.startswith('tex') else None})
    Path('build-report.json').write_text(json.dumps({'results':results},indent=2)+'\n')
    if process.returncode:
        print(process.stdout.decode(errors='replace')[-7000:]);print(process.stderr.decode(errors='replace')[-2000:])
        raise SystemExit(process.returncode)
artifacts={p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in [root/'P16.1-paper.tex',root/'P16.1-paper.pdf']}
Path('build-report.json').write_text(json.dumps({'results':results,'artifacts':artifacts},indent=2)+'\n')
print(json.dumps({'all_passes_succeeded':True,'artifacts':artifacts}))
