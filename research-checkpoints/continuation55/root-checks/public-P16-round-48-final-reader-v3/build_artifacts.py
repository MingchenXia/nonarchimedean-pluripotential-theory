#!/usr/bin/env python3
"""Generate a standalone TeX manuscript, render source checks, compile exactly twice."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def literal(text):
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$',
                    '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
                    '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(replacements.get(ch, ch) for ch in text)

def inline(text):
    parts = re.split(r'(\\\(.*?\\\)|`[^`]*`)', text)
    output = []
    for part in parts:
        if part.startswith(r'\('):
            output.append(part)
        elif part.startswith('`') and part.endswith('`'):
            output.append(r'\texttt{' + literal(part[1:-1]) + '}')
        else:
            output.append(literal(part))
    return ''.join(output)

def manuscript():
    lines = (ROOT / 'P16.6-argument.md').read_text(encoding='utf-8').splitlines()
    title = lines[0][2:]
    body = []
    math = False
    for line in lines[1:]:
        if line.strip() == r'\[':
            math = True
            body.append(line)
        elif line.strip() == r'\]':
            math = False
            body.append(line)
        elif math:
            body.append(line)
        elif line.startswith('## '):
            body.append(r'\section*{' + inline(line[3:]) + '}')
        else:
            body.append(inline(line))
    if math:
        raise RuntimeError('Unclosed display math')
    preamble = r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usepackage{mathrsfs}
\usepackage[margin=1in]{geometry}
\usepackage{microtype}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\allowdisplaybreaks
'''
    tex = preamble + r'\title{' + literal(title) + '}\n'
    tex += r'\author{Public-source audit and partial theorem; unverified draft}' + '\n'
    tex += r'\date{October 4, 2026}' + '\n' + r'\begin{document}' + '\n' + r'\maketitle' + '\n'
    tex += '\n'.join(body) + '\n' + r'\end{document}' + '\n'
    (ROOT / 'P16.6-paper.tex').write_text(tex, encoding='utf-8')

def main():
    commands = []
    for source, page, basename in [
        ('/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.pdf', 25, 'synthetic-page25'),
        ('/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf', 27, 'bfj-v1-page27'),
        ('/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf', 28, 'bfj-v1-page28'),
        ('/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf', 122, 'bj-v4-page122'),
    ]:
        command = ['pdftoppm', '-f', str(page), '-l', str(page), '-scale-to', '1600',
                   '-png', '-singlefile', source, str(ROOT / 'source-extracts' / basename)]
        p = subprocess.run(command, capture_output=True)
        (ROOT / 'source-extracts' / (basename + '-render.stdout')).write_bytes(p.stdout)
        (ROOT / 'source-extracts' / (basename + '-render.stderr')).write_bytes(p.stderr)
        commands.append({'command': command, 'returncode': p.returncode})
        if p.returncode:
            raise RuntimeError('Source-page render failed')
    # Regenerate provenance after rendering so inspection-image hashes are current.
    p = subprocess.run(['python3', 'audit_sources.py'], cwd=ROOT, capture_output=True)
    (ROOT / 'source-audit-output.txt').write_bytes(p.stdout + p.stderr)
    if p.returncode:
        raise RuntimeError('Source audit failed')
    manuscript()
    build_root = ROOT / 'build'
    build_root.mkdir(exist_ok=True)
    results = []
    for number in [1, 2]:
        out = build_root / f'pass{number}'
        out.mkdir(exist_ok=True)
        if number == 2:
            for extension in ['aux', 'out']:
                previous = build_root / 'pass1' / ('P16.6-paper.' + extension)
                if previous.exists():
                    shutil.copyfile(previous, out / previous.name)
        command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                   '-file-line-error', '-output-directory=' + str(out), 'P16.6-paper.tex']
        p = subprocess.run(command, cwd=ROOT, capture_output=True)
        (out / 'diagnostics.stdout').write_bytes(p.stdout)
        (out / 'diagnostics.stderr').write_bytes(p.stderr)
        (out / 'command.json').write_text(json.dumps({'command': command, 'cwd': str(ROOT),
                                                     'returncode': p.returncode}, indent=2) + '\n')
        log = out / 'P16.6-paper.log'
        pdf = out / 'P16.6-paper.pdf'
        result = {'pass': number, 'command': command, 'returncode': p.returncode,
                  'stdout_file': str((out / 'diagnostics.stdout').relative_to(ROOT)),
                  'stderr_file': str((out / 'diagnostics.stderr').relative_to(ROOT)),
                  'log_file': str(log.relative_to(ROOT)),
                  'log_sha256': digest(log) if log.exists() else None,
                  'pdf_sha256': digest(pdf) if pdf.exists() else None}
        logtext = log.read_text(errors='replace') if log.exists() else ''
        result['warnings'] = re.findall(r'^.*(?:Warning|Overfull|Underfull).*$', logtext, re.M)
        results.append(result)
        print('TeX pass', number, 'exit', p.returncode, 'warnings', len(result['warnings']))
    report = {'source_render_commands': commands,
              'tex_source_sha256': digest(ROOT / 'P16.6-paper.tex'),
              'argument_sha256': digest(ROOT / 'P16.6-argument.md'),
              'passes': results,
              'mathematical_validation': 'None. Compilation, execution and hashes do not verify mathematics.'}
    (build_root / 'build-report.json').write_text(json.dumps(report, indent=2) + '\n')
    if all(r['returncode'] == 0 for r in results):
        shutil.copyfile(build_root / 'pass2' / 'P16.6-paper.pdf', ROOT / 'P16.6-paper.pdf')
        p = subprocess.run(['pdftotext', '-layout', 'P16.6-paper.pdf', 'build/manuscript-from-pdf.txt'], cwd=ROOT, capture_output=True)
        (build_root / 'manuscript-pdftotext.stdout').write_bytes(p.stdout)
        (build_root / 'manuscript-pdftotext.stderr').write_bytes(p.stderr)
        if p.returncode:
            raise RuntimeError('Manuscript PDF extraction failed')
    else:
        raise RuntimeError('At least one of the two TeX builds failed; see actual retained diagnostics')

if __name__ == '__main__':
    main()
