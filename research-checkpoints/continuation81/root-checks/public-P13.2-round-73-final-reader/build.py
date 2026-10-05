import hashlib
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def run(label,args):
    result=subprocess.run(args,cwd=ROOT,capture_output=True)
    (ROOT/(label+'.stdout')).write_bytes(result.stdout)
    (ROOT/(label+'.stderr')).write_bytes(result.stderr)
    return {'label':label,'command':args,'returncode':result.returncode}

def main():
    environment={'platform':platform.platform(),'python':sys.version,'cwd':str(ROOT),'tools':{}}
    for name in ['pandoc','pdflatex','pdfinfo']:
        binary=shutil.which(name)
        assert binary,name
        arg='-v' if name=='pdfinfo' else '--version'
        r=subprocess.run([binary,arg],capture_output=True,text=True)
        environment['tools'][name]={'path':binary,'version':(r.stdout+r.stderr).split('\n')[0]}
    (ROOT/'environment.json').write_text(json.dumps(environment,indent=2)+'\n')
    outcomes=[]
    outcomes.append(run('pandoc',['pandoc','P13.2-argument.md','--standalone','--from=markdown+tex_math_dollars','--to=latex','--output=P13.2-paper.tex']))
    assert outcomes[-1]['returncode']==0,outcomes[-1]
    for i in [1,2]:
        outcomes.append(run('tex-pass-'+str(i),['pdflatex','-interaction=nonstopmode','-halt-on-error','P13.2-paper.tex']))
        if (ROOT/'P13.2-paper.log').exists():
            shutil.copyfile(ROOT/'P13.2-paper.log',ROOT/f'tex-pass-{i}.log')
        assert outcomes[-1]['returncode']==0,outcomes[-1]
    outcomes.append(run('pdfinfo',['pdfinfo','P13.2-paper.pdf']))
    outputs={n:{'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest(),'bytes':(ROOT/n).stat().st_size}
             for n in ['P13.2-argument.md','P13.2-paper.tex','P13.2-paper.pdf','tex-pass-1.log','tex-pass-2.log']}
    report={'status':'compiled','commands':outcomes,'artifacts':outputs,
            'limitation':'Two successful compilation passes are execution observations, not mathematical validation.'}
    (ROOT/'build-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'compiled','returncodes':[x['returncode'] for x in outcomes]},indent=2))

if __name__=='__main__':main()
