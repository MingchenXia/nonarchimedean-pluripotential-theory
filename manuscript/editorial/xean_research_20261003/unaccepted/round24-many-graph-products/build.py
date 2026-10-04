"""Standalone TeX rendering and two compilation passes; no network."""
from pathlib import Path
import hashlib, json, os, subprocess
render=['pandoc','P05.2-argument.md','--from=markdown+tex_math_single_backslash',
 '--to=latex','--standalone','--variable=documentclass:article','--variable=fontsize:11pt',
 '--variable=geometry:margin=1in','--variable=monofont:DejaVu Sans Mono',
 '--include-in-header=build-header.tex','--output=P05.2-partial.tex']
compile_command=['xelatex','-interaction=nonstopmode','-halt-on-error','P05.2-partial.tex']
cache=Path('.cache').resolve();cache.mkdir(exist_ok=True)
env=dict(os.environ,XDG_CACHE_HOME=str(cache));runs=[]
for name,command in [('render',render),('compile-1',compile_command),('compile-2',compile_command)]:
 r=subprocess.run(command,capture_output=True,env=env)
 Path('build-'+name+'.stdout.txt').write_bytes(r.stdout+r.stderr)
 if name.startswith('compile') and Path('P05.2-partial.log').exists():
  Path('build-'+name+'.log').write_bytes(Path('P05.2-partial.log').read_bytes())
 runs.append({'name':name,'command':command,'exit_code':r.returncode})
 if r.returncode:break
pdf=Path('P05.2-partial.pdf')
evidence={'runs':runs,'two_successful_compilations':len(runs)==3 and all(x['exit_code']==0 for x in runs),
 'font_cache_environment':{'XDG_CACHE_HOME':str(cache)},
 'pdf_bytes':pdf.stat().st_size if pdf.exists() else None,
 'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest() if pdf.exists() else None,
 'interpretation':'Compilation is reproducibility evidence, not mathematical verification.'}
Path('build-evidence.json').write_text(json.dumps(evidence,indent=2)+'\n')
print(json.dumps(evidence,indent=2))
if not evidence['two_successful_compilations']:raise SystemExit(1)
