#!/usr/bin/env python3
"""Produce standalone TeX, then run exactly two real pdflatex passes."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
md = (ROOT/'P16.3-argument.md').read_text()

def escape(s):
    table = {'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$',
             '#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}',
             '^':r'\textasciicircum{}'}
    return ''.join(table.get(c,c) for c in s)

def inline(s):
    # Preserve deliberately authored mathematical LaTeX; escape every prose token.
    out=[]; pos=0
    token=re.compile(r'\\\([\s\S]*?\\\)|`[^`]*`|\*\*[^*]*\*\*')
    for m in token.finditer(s):
        out.append(escape(s[pos:m.start()]))
        t=m.group()
        if t.startswith(r'\('): out.append(t)
        elif t.startswith('`'):
            code=t[1:-1]
            if re.fullmatch(r'[0-9a-f]{64}',code):
                chunks=[code[i:i+8] for i in range(0,64,8)]
                out.append(r'\texttt{'+r'\allowbreak{}'.join(chunks)+'}')
            else: out.append(r'\texttt{'+escape(code)+ '}')
        else: out.append(r'\textbf{'+inline(t[2:-2])+ '}')
        pos=m.end()
    out.append(escape(s[pos:]))
    return ''.join(out)

header=r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage[margin=1in]{geometry}
\usepackage{microtype}
\usepackage[hidelinks]{hyperref}
\newcommand{\MA}{\operatorname{MA}}
\newcommand{\PSH}{\operatorname{PSH}}
\setlength{\emergencystretch}{2em}
\title{P16.3: Mixed-characteristic inputs, model-level progress,\\and unresolved full scope}
\author{Research draft from the frozen assignment and authorized primary sources}
\date{5 October 2026}
\begin{document}
\maketitle
'''
out=[header]; para=[]; mode=None
def flush():
    if para:
        out.append(inline(' '.join(para))+'\n\n')
        para.clear()

for line in md.splitlines():
    if line.startswith('# '): continue
    if line == '$$':
        flush()
        if mode == 'math': out.append('\\]\n\n'); mode=None
        else: out.append('\\[\n'); mode='math'
        continue
    if line.startswith('```'):
        flush()
        if mode=='code': out.append('\\end{verbatim}\n\n'); mode=None
        else: out.append('\\begin{verbatim}\n'); mode='code'
        continue
    if mode in ['math','code']:
        out.append(line+'\n'); continue
    if line.startswith('## '):
        flush();out.append('\\section*{'+inline(line[3:])+'}\n\n');continue
    if not line.strip(): flush();continue
    if line.startswith('- '):
        flush();out.append('\\noindent '+inline(line[2:])+'\n\n');continue
    if re.match(r'^\d+\. ',line):
        flush();out.append('\\noindent '+inline(line)+'\n\n');continue
    para.append(line)
flush();assert mode is None
out.append('\\end{document}\n')
tex=ROOT/'P16.3-paper.tex'
tex.write_text(''.join(out))

build=ROOT/'build';build.mkdir(exist_ok=True)
if (build/'build-results.json').exists():
    previous_root=build/'previous';previous_root.mkdir(exist_ok=True)
    counter=1
    while (previous_root/f'run-{counter:03d}').exists(): counter+=1
    previous=previous_root/f'run-{counter:03d}';previous.mkdir()
    names=['build-results.json','P16.3-paper.pdf','P16.3-paper.log','P16.3-paper.aux','P16.3-paper.out']
    names += [f'pass{p}.{tail}' for p in [1,2] for tail in ['stdout.txt','stderr.txt','tex.log']]
    for name in names:
        path=build/name
        if path.exists(): shutil.copy2(path,previous/name)

results=[]
for i in [1,2]:
    command=['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',
             '-output-directory=build','P16.3-paper.tex']
    r=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
    (build/f'pass{i}.stdout.txt').write_text(r.stdout)
    (build/f'pass{i}.stderr.txt').write_text(r.stderr)
    log=build/'P16.3-paper.log'
    if log.exists(): shutil.copy2(log,build/f'pass{i}.tex.log')
    results.append({'pass':i,'command':command,'cwd':str(ROOT),'returncode':r.returncode,
                    'stdout':f'pass{i}.stdout.txt','stderr':f'pass{i}.stderr.txt',
                    'tex_log':f'pass{i}.tex.log'})

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
pdf=build/'P16.3-paper.pdf'
pdfinfo=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True) if pdf.exists() else None
if pdfinfo:
    (build/'pdfinfo.stdout.txt').write_text(pdfinfo.stdout)
    (build/'pdfinfo.stderr.txt').write_text(pdfinfo.stderr)
report={'passes':results,'tex_sha256':sha(tex),'pdf_sha256':sha(pdf) if pdf.exists() else None,
        'pdfinfo_returncode':pdfinfo.returncode if pdfinfo else None,
        'mathematical_force':'Compilation and hashes have no mathematical force.'}
(build/'build-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if any(r['returncode']!=0 for r in results): raise SystemExit(1)
