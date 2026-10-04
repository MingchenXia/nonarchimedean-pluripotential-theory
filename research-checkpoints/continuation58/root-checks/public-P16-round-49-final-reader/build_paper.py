#!/usr/bin/env python3
"""Generate a standalone TeX rendition and save two actual diagnostic streams/logs."""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / 'build'
BUILD.mkdir(exist_ok=True)
if (BUILD / 'build-results.json').exists():
    previous = BUILD / 'previous'
    previous.mkdir(exist_ok=True)
    dest = previous / ('run' + str(len(list(previous.iterdir()))+1))
    dest.mkdir()
    for name in ('pass1.stdout.txt','pass1.stderr.txt','pass1.tex.log',
                 'pass2.stdout.txt','pass2.stderr.txt','pass2.tex.log',
                 'build-results.json','P16.3-paper.pdf'):
        path = BUILD / name
        if path.exists():
            shutil.copyfile(path, dest / name)
    shutil.copyfile(ROOT / 'P16.3-paper.tex', dest / 'P16.3-paper.tex')

def escape(text):
    subs = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
            '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}', '<': r'\textless{}', '>': r'\textgreater{}'}
    return ''.join(subs.get(c, c) for c in text)

def inline(text):
    parts = re.split(r'(\$\$.*?\$\$|\$[^$]*\$|`[^`]*`|\*\*.*?\*\*)', text, flags=re.S)
    out = []
    for part in parts:
        if part.startswith('$$'):
            out.append('\\[\n' + part[2:-2].strip() + '\n\\]')
        elif part.startswith('$'):
            out.append(part)
        elif part.startswith('`'):
            code = part[1:-1]
            # Breakable monospace keeps long hashes and paths inside the margins.
            code_tex = r'\allowbreak{}'.join(escape(code[i:i+8]) for i in range(0,len(code),8))
            out.append(r'\texttt{' + code_tex + '}')
        elif part.startswith('**'):
            out.append(r'\textbf{' + escape(part[2:-2]) + '}')
        else:
            out.append(escape(part))
    return ''.join(out)

md = (ROOT / 'P16.3-argument.md').read_text()
blocks = md.split('\n\n')
title = blocks.pop(0).removeprefix('# ').strip()
body = []
for block in blocks:
    if block.startswith('## '):
        # Markdown has explicit section numbers; TeX creates the same sequence.
        name = re.sub(r'^\d+\.\s*', '', block[3:].strip())
        body.append(r'\section{' + escape(name) + '}')
    elif block.startswith('### '):
        body.append(r'\subsection{' + escape(block[4:].strip()) + '}')
    else:
        body.append(inline(block))

tex = r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{hyperref}
\hypersetup{hidelinks}
\setlength{\emergencystretch}{3em}
\title{''' + escape(title) + r'''}
\author{Public primary-source reconstruction}
\date{4 October 2026}
\begin{document}
\maketitle
''' + '\n\n'.join(body) + '\n\\end{document}\n'
paper = ROOT / 'P16.3-paper.tex'
paper.write_text(tex)
results = []
for number in (1, 2):
    command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', '-output-directory=build', 'P16.3-paper.tex']
    result = subprocess.run(command, cwd=ROOT, capture_output=True)
    (BUILD / f'pass{number}.stdout.txt').write_bytes(result.stdout)
    (BUILD / f'pass{number}.stderr.txt').write_bytes(result.stderr)
    logfile = BUILD / 'P16.3-paper.log'
    if logfile.exists():
        (BUILD / f'pass{number}.tex.log').write_bytes(logfile.read_bytes())
    results.append({'pass': number, 'command': command, 'returncode': result.returncode,
                    'stdout': f'build/pass{number}.stdout.txt',
                    'stderr': f'build/pass{number}.stderr.txt',
                    'tex_log': f'build/pass{number}.tex.log'})
summary = {'tex_sha256': hashlib.sha256(paper.read_bytes()).hexdigest(), 'passes': results,
           'both_passes_successful': all(r['returncode']==0 for r in results),
           'mathematical_validation': False}
pdf = BUILD / 'P16.3-paper.pdf'
if pdf.exists():
    summary['pdf_sha256'] = hashlib.sha256(pdf.read_bytes()).hexdigest()
    summary['pdf_bytes'] = pdf.stat().st_size
(BUILD / 'build-results.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps(summary, indent=2))
