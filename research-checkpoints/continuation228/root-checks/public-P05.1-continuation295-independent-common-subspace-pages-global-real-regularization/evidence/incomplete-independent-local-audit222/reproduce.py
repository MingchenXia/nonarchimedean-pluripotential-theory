#!/usr/bin/env python3
"""Fresh driver. Only the inspected bounded arithmetic is copied/executed.
The unchanged inspected TeX is copied; no supplied builder is loaded.
"""
import json,pathlib,hashlib,subprocess,sys,platform,shutil
HERE=pathlib.Path(__file__).resolve().parent
bindings=json.loads((HERE/'frozen-bindings.json').read_text())
SCRATCH=HERE/'own-scratch'
def digest(b): return hashlib.sha256(b).hexdigest()
def copy(group,index,name):
    row=bindings[group][index]; data=pathlib.Path(row['path']).read_bytes()
    assert digest(data)==row['sha256']
    target=SCRATCH/name; target.write_bytes(data)
    return {'file':name,'sha256':digest(data),'bytes':len(data)}
def main():
    if '--prepare' in sys.argv:
        assert not SCRATCH.exists()
        SCRATCH.mkdir()
        copied=[copy('history',27,'exact_checks.py'),copy('history',26,'exact-check-input.json'),copy('math',25,'P05.1-paper.tex')]
        (HERE/'prepared-copy.json').write_text(json.dumps(copied,indent=2)+'\n')
        print(json.dumps(copied)); return
    assert SCRATCH.exists() and not (SCRATCH/'run-0.stdout.txt').exists(), 'One execution only.'
    copied=json.loads((HERE/'prepared-copy.json').read_text())
    for row in copied: assert digest((SCRATCH/row['file']).read_bytes())==row['sha256']
    # These commands use argument arrays, no shell and no environment mutations.
    commands=[['python3','exact_checks.py']]
    commands += [['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','P05.1-paper.tex'] for _ in range(3)]
    commands += [['pandoc','P05.1-paper.tex','--from=latex','--to=gfm','--standalone','--output=argument.md'],['pdfinfo','P05.1-paper.pdf']]
    runs=[]
    for i,argv in enumerate(commands):
        r=subprocess.run(argv,cwd=SCRATCH,capture_output=True,timeout=60)
        (SCRATCH/f'run-{i}.stdout.txt').write_bytes(r.stdout)
        (SCRATCH/f'run-{i}.stderr.txt').write_bytes(r.stderr)
        if argv[0]=='pdflatex' and (SCRATCH/'P05.1-paper.log').exists():
            shutil.copyfile(SCRATCH/'P05.1-paper.log',SCRATCH/f'run-{i}.tex.log')
        runs.append({'argv':argv,'returncode':r.returncode,'stdout_sha256':digest(r.stdout),'stderr_sha256':digest(r.stderr)})
        if r.returncode: break
    exact=(SCRATCH/'run-0.stdout.txt').read_bytes()
    expected=pathlib.Path(bindings['history'][28]['path']).read_bytes()
    argument=SCRATCH/'argument.md'
    result={'copied':copied,'runs':runs,'exact_output_bytes_equal':exact==expected,
        'markdown_bytes_equal':argument.exists() and argument.read_bytes()==pathlib.Path(bindings['math'][26]['path']).read_bytes(),
        'finite_only':True,'environment':{'python':sys.version,'platform':platform.platform()},
        'versions':{}}
    for name in ['pdflatex','pandoc','pdfinfo']:
        argv=[name,'--version'] if name!='pdfinfo' else [name,'-v']
        v=subprocess.run(argv,capture_output=True,timeout=10)
        result['versions'][name]=(v.stdout+v.stderr).decode(errors='replace').split('\n')[0]
    (HERE/'own-build-finite-records.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
