#!/usr/bin/env python3
"""Render the complete argument body to a standalone, input-free TeX document."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / 'P02.3-argument.md').read_text()

def text_tex(s):
    # Preserve all authored TeX math; escape only prose segments.
    chunks = re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])', s, flags=re.S)
    for i in range(0, len(chunks), 2):
        p = chunks[i]
        p = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', p)
        p = re.sub(r'`([^`]*)`', lambda m: r'\texttt{' + m[1].replace('_',r'\_') + '}', p)
        p = p.replace('&',r'\&').replace('%',r'\%').replace('#',r'\#')
        chunks[i] = p
    return ''.join(chunks)

parts = []
for line in source.splitlines():
    if line.startswith('# '):
        continue
    if line.startswith('## '):
        title = re.sub(r'^\d+\. ', '', line[3:])
        parts.append(r'\section{' + text_tex(title) + '}')
    elif line.startswith('### '):
        title = re.sub(r'^\d+\.\d+\. ', '', line[4:])
        parts.append(r'\subsection{' + text_tex(title) + '}')
    else:
        parts.append(line)
# Convert whole paragraphs, not individual math lines.
body = text_tex('\n'.join(parts))
header = r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{lmodern}
\setlength{\emergencystretch}{3em}
\title{P02.3: Weakly Smooth Decreasing Regularization, Singular Curves, and an Analytic Boundary Obstruction}
\author{Unverified research draft}
\date{4 October 2026}
\begin{document}
\maketitle
'''
trailer = '\n\\end{document}\n'
paper = header + body + trailer
(ROOT / 'P02.3-paper.tex').write_text(paper)
(ROOT / 'paper-generation.json').write_text(json.dumps({
    'markdown_sha256': hashlib.sha256(source.encode()).hexdigest(),
    'tex_sha256': hashlib.sha256(paper.encode()).hexdigest(),
    'complete_body_embedded': True,
    'generator': 'make_paper.py',
    'external_inputs_required': False
}, indent=2) + '\n')
print('Generated standalone P02.3-paper.tex from the complete argument.')
