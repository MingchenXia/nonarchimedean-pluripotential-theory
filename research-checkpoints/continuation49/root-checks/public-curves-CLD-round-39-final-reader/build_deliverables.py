#!/usr/bin/env python3
"""Embed the entire argument in standalone TeX and compile twice without installs."""
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def run(cmd, name):
    try:
        r=subprocess.run(cmd,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=60)
        (ROOT/name).write_text(r.stdout)
        return {'command':cmd,'exit_code':r.returncode,'stdout_file':name}
    except (FileNotFoundError,subprocess.TimeoutExpired) as e:
        (ROOT/name).write_text(str(e)+'\n')
        return {'command':cmd,'exit_code':None,'stdout_file':name,'error':str(e)}

def main():
    env={'python':sys.version,'platform':platform.platform(),'cwd':str(ROOT),
         'tools':{k:shutil.which(k) for k in ['pandoc','pdflatex','pdftotext','pdftoppm','latexmk']},
         'activity':'Local source reads, artifact generation, PDF inspection and light TeX builds. No installation, worker, model invocation, network or auth changes.',
         'managed_environment_status_tool':'Not exposed in current callable tool metadata.',
         'model_route':'Requested native gpt-6.1-sol/xhigh; no independent model/account inspection performed.'}
    for tool in ['pandoc','pdflatex']:
        if shutil.which(tool):
            env[tool+'_version']=subprocess.run([tool,'--version'],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=10).stdout.splitlines()[:2]
    (ROOT/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
    d={'mathematical_certificate':False,'steps':[]}
    d['steps'].append(run(['pandoc','P03.2-argument.md','--from=markdown+tex_math_dollars','--to=latex','--standalone',
                          '--variable=fontsize:11pt','--variable=geometry:margin=1in',
                          '--include-in-header=tex-header.tex','--output=P03.2-paper.tex'],'pandoc.stdout.txt'))
    if d['steps'][-1]['exit_code']==0:
        for n in [1,2]:
            d['steps'].append(run(['pdflatex','-interaction=nonstopmode','-halt-on-error','P03.2-paper.tex'],f'build-pass{n}.stdout.txt'))
            p=ROOT/'P03.2-paper.log'
            if p.exists(): shutil.copyfile(p,ROOT/f'build-pass{n}.log')
    d['actual_warning_lines']=[line for step in d['steps'] for line in (ROOT/step['stdout_file']).read_text().splitlines()
                               if any(w in line for w in ['Warning','Overfull','Underfull']) or line.startswith('! ')]
    d['pdf_exists']=(ROOT/'P03.2-paper.pdf').exists()
    d['all_steps_succeeded']=len(d['steps'])==3 and all(s['exit_code']==0 for s in d['steps'])
    d['proof_limit']='Source hashes and successful conversion/TeX compilation do not establish mathematical correctness.'
    (ROOT/'build-diagnostics.json').write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps({'all_steps_succeeded':d['all_steps_succeeded'],'pdf_exists':d['pdf_exists'],'warning_count':len(d['actual_warning_lines'])}))

if __name__=='__main__': main()
