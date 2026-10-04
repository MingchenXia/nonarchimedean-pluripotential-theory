#!/usr/bin/env python3
"""Turn the complete argument into a standalone TeX paper, without dependencies."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'P16.1-argument.md').read_text()

def escape(s):
    subst = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
             '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
             '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(subst.get(c, c) for c in s)

def inline(s):
    parts = re.split(r'(\$[^$]*\$|`[^`]*`)', s)
    output = []
    for p in parts:
        if p.startswith('$') and p.endswith('$'):
            output.append(p)
        elif p.startswith('`') and p.endswith('`'):
            output.append(r'\texttt{' + escape(p[1:-1]) + '}')
        else:
            output.append(escape(p))
    return ''.join(output)

lines = source.split('\n')
body = []
para = []
display = []
in_display = False

def flush():
    if para:
        body.append(inline(' '.join(para)) + '\n\n')
        para.clear()

for line in lines:
    if in_display:
        display.append(line)
        if line.strip() == r'\]':
            body.append('\n'.join(display) + '\n\n')
            display.clear()
            in_display = False
    elif line.strip() == r'\[':
        flush()
        display.append(line)
        in_display = True
    elif line.startswith('# '):
        flush()
        # The title is placed in the standalone preamble.
    elif line.startswith('## '):
        flush()
        body.append(r'\section*{' + inline(line[3:]) + '}\n')
    elif not line.strip():
        flush()
    else:
        para.append(line)
flush()
if in_display:
    raise ValueError('Unclosed display equation')

preamble = r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\hypersetup{colorlinks=true,urlcolor=blue,linkcolor=blue}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\setlength{\emergencystretch}{3em}
\title{P16.1: A Proved Curve Sector and the Remaining Singular-Variety Problem}
\author{Unverified research draft}
\date{4 October 2026}
\begin{document}
\maketitle
'''
(ROOT / 'P16.1-paper.tex').write_text(preamble + ''.join(body) + '\\end{document}\n')
print('Wrote standalone P16.1-paper.tex from the complete argument.')
