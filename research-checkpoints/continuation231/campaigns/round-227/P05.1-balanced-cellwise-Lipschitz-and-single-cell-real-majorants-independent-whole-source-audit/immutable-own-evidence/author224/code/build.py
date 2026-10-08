#!/usr/bin/env python3
"""Own local standalone TeX build; commands are argument lists, no shell."""
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys

HERE=pathlib.Path(__file__).resolve().parent.parent

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def run(command,path):
    p=subprocess.run(command,cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    path.write_text(p.stdout)
    return {'command':command,'exit_code':p.returncode,'output_log':str(path.relative_to(HERE))}

def main():
    (HERE/'build').mkdir(exist_ok=True);(HERE/'reports').mkdir(exist_ok=True)
    runno=1
    while (HERE/f'build/run-{runno:03d}').exists():runno+=1
    rundir=HERE/f'build/run-{runno:03d}'
    rundir.mkdir()
    if (HERE/'P05.1-paper.tex').exists():
        shutil.copyfile(HERE/'P05.1-paper.tex',rundir/'prior-paper.tex')
    shutil.copyfile(HERE/'argument.md',rundir/'input-argument.md')
    report={'build':'own Pandoc conversion and unchanged no-shell-escape pdfLaTeX passes',
            'input_markdown_sha256':sha(HERE/'argument.md'),'commands':[],
            'run_directory':str(rundir.relative_to(HERE)),
            'initial_logs_retained':'build/pass1.log and build/pass2.log; later runs have distinct directories'}
    pandoc=shutil.which('pandoc');tex=shutil.which('pdflatex')
    if not pandoc or not tex:
        report['status']='missing local TeX facility; no install attempted'
        (HERE/'reports/build-report.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(report,indent=2));return 1
    command=[pandoc,'argument.md','--standalone','--number-sections','--table-of-contents',
             '--top-level-division=section','--variable','colorlinks=true','-o','P05.1-paper.tex']
    result=run(command,rundir/'pandoc.log');report['commands'].append(result)
    if result['exit_code']:
        report['status']='conversion failed; original failure retained'
    else:
        before=sha(HERE/'P05.1-paper.tex');report['tex_sha256_before_build']=before
        for passno in [1,2,3]:
            command=[tex,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error',
                     '-output-directory='+str(rundir.relative_to(HERE)),'P05.1-paper.tex']
            result=run(command,rundir/f'pdflatex-pass{passno}.stdout.log')
            report['commands'].append(result)
            for suffix in ['log','aux','toc','out']:
                p=rundir/f'P05.1-paper.{suffix}'
                if p.exists():shutil.copyfile(p,rundir/f'pass{passno}.{suffix}')
            if result['exit_code']:break
        after=sha(HERE/'P05.1-paper.tex');assert before==after
        report['tex_sha256_after_build']=after
        if result['exit_code']:
            report['status']='TeX failure; all initial logs retained'
        else:
            shutil.copyfile(rundir/'P05.1-paper.pdf',HERE/'P05.1-paper.pdf')
            report['pdf_sha256']=sha(HERE/'P05.1-paper.pdf')
            report['status']='local build succeeded; not mathematical acceptance'
            pdfinfo=shutil.which('pdfinfo')
            if pdfinfo:
                info=run([pdfinfo,'P05.1-paper.pdf'],HERE/'reports/pdfinfo.txt')
                report['commands'].append(info)
        warnings=[]
        for passno in [1,2,3]:
            p=rundir/f'pass{passno}.log'
            if p.exists():
                for i,line in enumerate(p.read_text(errors='replace').split('\n'),1):
                    if any(t in line for t in ['Warning','Overfull','Underfull','!']):
                        warnings.append({'pass':passno,'log_line':i,'text':line})
        report['warnings']=warnings
        report['final_pass_warnings']=[w for w in warnings if w['pass']==3]
    assert report['input_markdown_sha256']==sha(HERE/'argument.md')
    (HERE/'reports/build-report.json').write_text(json.dumps(report,indent=2)+'\n')
    (rundir/'build-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return 0 if report['status'].startswith('local build succeeded') else 1

if __name__=='__main__':sys.exit(main())
