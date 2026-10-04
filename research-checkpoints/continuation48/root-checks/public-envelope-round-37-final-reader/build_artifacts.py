#!/usr/bin/env python3
"""Embed the whole authored argument in standalone TeX, then build it twice."""
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

SOURCE = Path('P03.1-argument.md')
TARGET = Path('P03.1-paper.tex')
raw = SOURCE.read_text()

def text_escape(s):
    replacements = {'\\':r'\textbackslash{}', '{':r'\{', '}':r'\}',
                    '&':r'\&', '%':r'\%', '$':r'\$', '#':r'\#',
                    '_':r'\_', '~':r'\textasciitilde{}', '^':r'\textasciicircum{}'}
    return ''.join(replacements.get(c,c) for c in s)

def inline(s):
    parts = re.split(r'(\\\(.*?\\\)|`[^`]+`)',s,flags=re.S)
    ans=[]
    for p in parts:
        if p.startswith(r'\('): ans.append(p)
        elif p.startswith('`'): ans.append(r'\texttt{\detokenize{'+p[1:-1]+'}}')
        else: ans.append(text_escape(p))
    return ''.join(ans)

lines=raw.splitlines()
body=[]
in_math=False
in_list=False
for line in lines[1:]:
    if line.startswith(r'\['):
        if in_list:body.append(r'\end{itemize}');in_list=False
        in_math=True;body.append(line);continue
    if in_math:
        body.append(line)
        if r'\]' in line:in_math=False
        continue
    if line.startswith('* '):
        if not in_list:body.append(r'\begin{itemize}');in_list=True
        body.append(r'\item '+inline(line[2:]));continue
    # Indented text/math after a Markdown bullet belongs to the same item.
    if in_list and line.startswith('  '):
        if line.lstrip().startswith(r'\['):
            in_math=True;body.append(line.strip())
        else:body.append(inline(line.strip()))
        continue
    if in_list and line:
        body.append(r'\end{itemize}');in_list=False
    if line.startswith('### '):body.append(r'\subsection*{'+inline(line[4:])+'}')
    elif line.startswith('## '):body.append(r'\section*{'+inline(line[3:])+'}')
    else:body.append(inline(line))
if in_list:body.append(r'\end{itemize}')
assert not in_math,'unclosed display'

preamble=r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[margin=25mm]{geometry}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue}
\setlength{\emergencystretch}{3em}
\title{Full obstacle envelopes on curve bases with projective fibers}
\author{Native Codex research draft}
\date{4 October 2026}
\begin{document}
\maketitle
'''
TARGET.write_text(preamble+'\n'.join(body)+'\n'+r'\end{document}'+'\n')

engine=shutil.which('pdflatex')
execution={'cwd':str(Path.cwd()),'python':sys.version,'platform':platform.platform(),
           'commands':[], 'tex_engine':engine,
           'input_sha256':hashlib.sha256(Path('input.json').read_bytes()).hexdigest(),
           'argument_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
           'tex_sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
           'mathematical_verification':False,
           'additional_models_or_workers_invoked':False,
           'compute':'No resource-heavy computation; no supervised compute was needed.'}
for i in [1,2]:
    if engine:
        cmd=[engine,'-interaction=nonstopmode','-halt-on-error','P03.1-paper.tex']
        result=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        output=result.stdout;rc=result.returncode
    else:
        cmd=['pdflatex','-interaction=nonstopmode','-halt-on-error','P03.1-paper.tex']
        output='TeX engine unavailable; no software was installed.\n';rc=None
    file=Path(f'build-pass-{i}.txt');file.write_text(output)
    execution['commands'].append({'argv':cmd,'exit_code':rc,'diagnostics_file':str(file)})
    print('pass',i,'exit',rc)
    print('\n'.join(output.splitlines()[-5:]))
pdf=Path('P03.1-paper.pdf')
if pdf.exists():execution['pdf_sha256']=hashlib.sha256(pdf.read_bytes()).hexdigest()
Path('execution.json').write_text(json.dumps(execution,indent=2)+'\n')
print('Standalone TeX embeds all',len(lines),'argument lines.')
