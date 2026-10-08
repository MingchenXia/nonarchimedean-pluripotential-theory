"""Owned Markdown-to-TeX builder; preserves the independently written math body."""
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def escape(s):
    return ''.join({'\\':r'\textbackslash{}', '_':r'\_', '&':r'\&', '%':r'\%',
                    '#':r'\#', '$':r'\$', '{':r'\{', '}':r'\}', '~':r'\textasciitilde{}',
                    '^':r'\textasciicircum{}'}.get(c,c) for c in s)

def paragraph(s):
    parts = re.split(r'(\\\(.*?\\\)|`[^`]*`)', s, flags=re.S)
    result = []
    for part in parts:
        if part.startswith(r'\('):
            result.append(part)
        elif part.startswith('`'):
            result.append(r'\texttt{'+escape(part[1:-1])+'}')
        else:
            result.append(escape(part))
    return ''.join(result)

def main():
    body = (ROOT/'argument.md').read_text()
    blocks = re.split(r'(\\\[.*?\\\])', body, flags=re.S)
    converted = []
    for block in blocks:
        if block.startswith(r'\['):
            converted.append(block)
            continue
        for line in block.splitlines():
            if line.startswith('# '):
                continue
            if line.startswith('## '):
                converted.append(r'\section*{'+escape(line[3:])+'}')
            else:
                converted.append(paragraph(line))
    header = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[margin=25mm]{geometry}
\usepackage{hyperref}
\setlength{\emergencystretch}{3em}
\title{P03.1: a category bound for the full envelope\\and an unresolved analytic step}
\author{Owned research draft; original classification incomplete}
\date{8 October 2026}
\begin{document}
\maketitle
'''
    target = ROOT/'P03.1-paper.tex'
    target.write_text(header+'\n'.join(converted)+'\n\\end{document}\n')
    (ROOT/'evidence').mkdir(exist_ok=True)
    runs = []
    for number in [1,2]:
        cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', target.name]
        run = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=60)
        (ROOT/'evidence'/f'tex-pass-{number}.txt').write_text(run.stdout+run.stderr)
        runs.append({'command':cmd, 'exit_code':run.returncode,
                     'output':f'evidence/tex-pass-{number}.txt'})
        if run.returncode:
            print(json.dumps(runs))
            sys.exit(run.returncode)
    (ROOT/'evidence'/'build.json').write_text(json.dumps({'runs':runs,
              'source':'argument.md', 'output':'P03.1-paper.tex',
              'meaning':'Compilation evidence only; no correctness verdict.'},indent=2)+'\n')
    print(json.dumps({'tex_passes':len(runs), 'exit_codes':[r['exit_code'] for r in runs],
                      'pdf_bytes':(ROOT/'P03.1-paper.pdf').stat().st_size}))

if __name__ == '__main__':
    main()
