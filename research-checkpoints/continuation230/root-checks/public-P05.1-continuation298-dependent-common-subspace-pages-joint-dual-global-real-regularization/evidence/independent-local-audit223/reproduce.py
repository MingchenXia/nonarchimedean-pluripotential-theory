"""Own fresh reproduction; supplied scripts except inspected bounded copy never run."""
import hashlib
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def run(argv, name):
    p=subprocess.run(argv,capture_output=True,text=True)
    Path(name+'.stdout.log').write_text(p.stdout)
    Path(name+'.stderr.log').write_text(p.stderr)
    return {'argv':argv,'returncode':p.returncode,
            'stdout':name+'.stdout.log','stderr':name+'.stderr.log'}

source=sha('P05.1-paper.tex')
report={'source_sha256_before':source,'python':sys.version,
        'platform':platform.platform(),'commands':[]}
for exe in ['python','pdflatex','pandoc','pdfinfo']:
    report[exe+'_path']=shutil.which(exe)
for exe in ['pdflatex','pandoc']:
    report['commands'].append(run([exe,'--version'],exe+'-version'))
report['commands'].append(run([sys.executable,'finite_check.py'],'finite'))
report['commands'].append(run(['pandoc','-f','latex','-t','markdown','P05.1-paper.tex','-o','argument.md'],'conversion'))
for i in range(1,4):
    r=run(['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P05.1-paper.tex'],f'tex-pass-{i}')
    if Path('P05.1-paper.log').exists():
        shutil.copyfile('P05.1-paper.log',f'tex-pass-{i}.engine.log')
    out=Path(r['stdout']).read_text()
    r['warning_lines']=[line for line in out.split('\n') if any(x in line for x in ['Warning','Overfull','Underfull','undefined'])]
    report['commands'].append(r)
report['commands'].append(run(['pdfinfo','P05.1-paper.pdf'],'pdfinfo'))
report['source_sha256_after']=sha('P05.1-paper.tex')
report['source_unchanged']=source==report['source_sha256_after']
Path('own-reproduction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
