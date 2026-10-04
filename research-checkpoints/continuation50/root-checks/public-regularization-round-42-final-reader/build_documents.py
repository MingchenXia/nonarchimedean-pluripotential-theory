"""Embed the complete argument in standalone TeX and compile twice, without installs."""
from pathlib import Path
import json,re,subprocess,hashlib

def escape(s):
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%',
       '$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}',
       '~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in s)

def inline(s):
    parts=re.split(r'(`[^`]*`|\$[^$]*\$)',s)
    out=[]
    for part in parts:
        if part.startswith('$') and part.endswith('$'): out.append(part)
        elif part.startswith('`') and part.endswith('`'):
            out.append(r'{\small\texttt{'+escape(part[1:-1])+'}}')
        else: out.append(escape(part))
    return ''.join(out)

argument=Path('P02.2-argument.md').read_text()
lines=argument.splitlines(); title=lines[0][2:]
body=[]
for line in lines[1:]:
    if line.startswith('## '): body.append(r'\section*{'+escape(line[3:])+'}')
    elif line.strip().startswith('$$'):
        formula=line.strip()[2:-2].strip()
        body.append(r'\['+formula+r'\]')
    else: body.append(inline(line))
tex=r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{hyperref}
\hypersetup{hidelinks}
\setlength{\emergencystretch}{3em}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\title{'''+escape(title)+r'''}
\author{Unverified research draft}
\date{4 October 2026}
\begin{document}
\maketitle
'''+ '\n'.join(body)+ '\n\\end{document}\n'
Path('P02.2-paper.tex').write_text(tex)
passes=[]
for number in (1,2):
    command=['pdflatex','-interaction=nonstopmode','-halt-on-error','P02.2-paper.tex']
    run=subprocess.run(command,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    Path(f'tex-build-pass-{number}.stdout.txt').write_text(run.stdout)
    log=Path('P02.2-paper.log').read_text(errors='replace') if Path('P02.2-paper.log').exists() else ''
    Path(f'tex-build-pass-{number}.log').write_text(log)
    diagnostic=[line for line in log.splitlines() if any(token in line for token in
        ['Warning','Overfull','Underfull','!','Output written','Fatal error'])]
    passes.append(dict(pass_number=number,command=command,exit_code=run.returncode,diagnostics=diagnostic))
result=dict(argument_sha256=hashlib.sha256(argument.encode()).hexdigest(),
    tex_sha256=hashlib.sha256(tex.encode()).hexdigest(),passes=passes,
    proof_warning='Compilation certifies typesetting execution only, not mathematical correctness.')
Path('tex-build-diagnostics.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if any(p['exit_code'] for p in passes): raise SystemExit(1)
