#!/usr/bin/env python3
import hashlib, json, pathlib, platform, shutil, subprocess, sys
ROOT=pathlib.Path(__file__).resolve().parent
LOG=ROOT/'build-logs';LOG.mkdir(exist_ok=True)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(cmd,name):
    proc=subprocess.run(cmd,cwd=ROOT,capture_output=True)
    (LOG/(name+'.stdout')).write_bytes(proc.stdout)
    (LOG/(name+'.stderr')).write_bytes(proc.stderr)
    (LOG/(name+'.command.json')).write_text(json.dumps(cmd,indent=2)+'\n')
    rec={'command':cmd,'returncode':proc.returncode,'stdout':str((LOG/(name+'.stdout')).relative_to(ROOT)),
         'stderr':str((LOG/(name+'.stderr')).relative_to(ROOT))}
    assert proc.returncode==0,(cmd,proc.stderr.decode(errors='replace')[-2000:])
    return rec

def main():
    env={'cwd':str(ROOT),'python':sys.version,'platform':platform.platform(),
         'pandoc_path':shutil.which('pandoc'),'pdflatex_path':shutil.which('pdflatex'),
         'execution_configuration':'Existing process configuration retained; requested routing/model setting not independently inspected or altered.',
         'supervised_compute':'No such facility exposed; no resource-heavy work required or launched.'}
    for tool in ['pandoc','pdflatex']:
        p=subprocess.run([tool,'--version'],capture_output=True,check=True)
        env[tool+'_version']=p.stdout.decode(errors='replace').splitlines()[0]
    (ROOT/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
    reports=[]
    reports.append(run(['pandoc','P16.1-argument.md','--standalone','--to=latex','--output=P16.1-paper.tex'],'pandoc'))
    for j in (1,2):
        reports.append(run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P16.1-paper.tex'],f'tex-pass-{j}'))
        shutil.copyfile(ROOT/'P16.1-paper.log',LOG/f'tex-pass-{j}.log')
    out={'commands':reports,'artifacts':{p:sha(ROOT/p) for p in ['P16.1-argument.md','P16.1-paper.tex','P16.1-paper.pdf']},
         'limit':'Successful compilation and artifact hashes do not validate mathematics.'}
    (ROOT/'build-report.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'pandoc_returncode':reports[0]['returncode'],'tex_pass_returncodes':[r['returncode'] for r in reports[1:]],
                      'pdf_sha256':out['artifacts']['P16.1-paper.pdf']}))

if __name__=='__main__':main()
