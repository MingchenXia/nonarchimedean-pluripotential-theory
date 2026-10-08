#!/usr/bin/env python3
"""Owned deterministic note/manuscript assembler and bounded local TeX build."""
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
META = [
    ('n1',
     'For the qualified G331 class, every continuous-obstacle raw D envelope equals the C supremum and is bounded lsc; it is positive iff continuous. No universal envelope property is assumed.',
     'Registers G331 exactly, including its geometric Cartier-degree core, C/D comparison, full conductor descent, all-support and smooth-hypothesis qualifications. Compact directed-cover arguments prove continuous D functions lie in C, P_D=P_C for finite continuous obstacles, the equivalence of continuity and actual class membership/greatestness, and raw uniform norm nonexpansiveness. No increasing closure, Hartogs theorem or nested-net flattening is used.'),
    ('n2',
     'Exact counterexample in the G331 cone: a continuous [-2,-1] obstacle on the excellent nonnormal surface xy=0 has no maximal geometric minorant; its raw supremum and usc regularization are not psh.',
     'On R=k[x,y,z]_(x,y,z)/(xy), the two smooth normalization boundaries identify the line-support conductor points. A fibre-compatible continuous obstacle is -1 on A and -3+min(w(y),2) on B. The primary-ideal order inequality forces every B minorant <=-2. Positively descended tuples from J_n=(x^n,xz^(n-1),z^(2n)) and the B constant -2 increase to the exact supremum: -1 on A outside its line point, -2 there and throughout B. Monomial valuations (L,1) converge to the identified nonminimal support, proving failure of usc. Finite maxima strictly improve every admissible D minorant, so none is maximal. Usc regularization raises the common value to -1 and violates the B order inequality. This is not the earlier literal-radial counterexample.'),
    ('n3',
     'At published smooth affine closed BFJ germs over algebraically closed characteristic zero, every finite continuous obstacle has an actual continuous geometric envelope.',
     'Applies complete BFJ 3.18 at its actual smooth hypotheses to dual-complex determining obstacles. A bounded coefficient supremum is weak-nef; closed-simplex continuity and all-retraction infima establish obstacle domination on all supports. Primary ideals from L-infinity(tW) yield f_t<=H<=t/(t+c) f_t and the uniform error c/(t+c)(M+1/t). Thus H lies in C before positivity is interpreted. It is greatest among D minorants by the granted BFJ comparison. Published PA density plus the proved raw Lipschitz bound extends to arbitrary continuous obstacles. No singular/positive-characteristic multiplier estimate is imported.'),
    ('n4',
     'On a separately proved continuous-envelope domain, every bounded-above extended usc obstacle has a greatest D_geom minorant, constructed by one actual decreasing C-net.',
     'A complete compact-Hausdorff cutoff argument produces the downward-directed net of finite continuous strict majorants F with inf F=phi. Already positive continuous envelopes P F decrease; their inf is in the original D by definition, below phi, and dominates every admissible D function. More generally P(inf phi_i)=inf P(phi_i) for a decreasing continuous obstacle net whose envelopes have been established in C. Guaranteed extended usc regularity, all-zero/bottom and mixed/partial-bottom patterns are retained. This hypothesis fails in the surface example and is not assumed for all excellent germs.'),
    ('n5',
     'Exact primary-gauge and fibre-constrained normalization envelope rules; complete geometric clipping on all excellent reduced curves and positive bijective-normalization sectors.',
     'Order-bijective homogeneous gauge changes commute with raw suprema and preserve positivity and regularity. G331 positive descent identifies downstairs admissible families with all full-fibre-constant upstairs minorants; unconstrained upstairs envelopes need not descend. Bijective normalization boundaries with continuous-envelope centres give complete positive sectors. On every excellent reduced curve the conductor is primary and normalization centres are DVRs, so the link is the finite branch set. Positive descent gives C_geom=(-infinity,0]^r, and actual decreasing clipped tuples give D_geom=[-infinity,0]^r. Only then min(phi,0) is proved to be the greatest geometric minorant for all extended obstacles, including mixed zero and partial bottom.'),
    ('n6',
     'Candidate=false: unrestricted original envelope positivity is refuted for G331 by the conductor surface; complete positive sectors and all requested proof/source artifacts are delivered.',
     'Retains the exact entire original task/family/scope. The continuous nonnormal counterexample blocks a universal greatest-minorant or regularized-supremum positive envelope on the unchanged cone. No altered cone or deleted support is substituted. Smooth BFJ, all excellent reduced curves and bijective-normalization sectors are complete; general excellent normal singular continuity remains unresolved here. P12.4--6, arbitrary-model cofinality and products/energy are unclaimed. Records input matches, local commands/environment/build and artifact/support consistency without treating execution as proof.')
]

def escape(s):
    table = {'\\': r'\textbackslash{}', '_': r'\_', '&': r'\&', '%': r'\%',
             '#': r'\#', '$': r'\$', '{': r'\{', '}': r'\}', '^': r'\textasciicircum{}',
             '~': r'\textasciitilde{}'}
    return ''.join(table.get(c, c) for c in s)

BT = chr(96)
TOKEN = re.compile(r'(\\\[.*?\\\]|\\\(.*?\\\)|' + BT + '[^' + BT + ']*' + BT + ')', re.S)

def prose(s):
    bits = TOKEN.split(s)
    out = []
    for b in bits:
        if b.startswith(r'\[') or b.startswith(r'\('):
            out.append(b)
        elif b.startswith(BT):
            out.append(r'\texttt{' + escape(b[1:-1]) + '}')
        else:
            out.append(escape(b))
    return ''.join(out)

def latex_md(s):
    lines = s.splitlines()
    out, i, display = [], 0, False
    while i < len(lines):
        line = lines[i]
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+', c) for c in cells):
                    rows.append(cells)
                i += 1
            cols = len(rows[0])
            width = (15.8 - 0.8 * cols) / cols
            out.append(r'\small\begin{longtable}{' + ''.join('p{%.2fcm}' % width for _ in range(cols)) + '}')
            for j, cells in enumerate(rows):
                assert len(cells) == cols
                out.append(' & '.join(prose(c) for c in cells) + r' \\')
                if j == 0:
                    out.append(r'\hline')
            out.append(r'\end{longtable}\normalsize')
            continue
        if line.startswith('# '):
            out.append(r'\section{' + prose(line[2:]) + '}')
        elif line.startswith('## '):
            out.append(r'\subsection{' + prose(line[3:]) + '}')
        elif display:
            out.append(line)
            if r'\]' in line:
                display = False
        elif r'\[' in line:
            display = True
            out.append(line)
        else:
            out.append(prose(line))
        i += 1
    return '\n'.join(out)

def extract_grant(g):
    text = g['text']
    for label, output in [
        ('mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json', 'G331-mandatory-source-scope.json'),
        ('source-application-ledger.md', 'G331-source-application-ledger.md'),
        ('exact-scope.md', 'G331-exact-scope.md')]:
        start = 'BEGIN ENTIRE ' + label + '\n'
        end = '\nEND ENTIRE ' + label
        content = text.split(start, 1)[1].split(end, 1)[0]
        (HERE / output).write_text(content)

def main():
    (HERE / 'evidence').mkdir(exist_ok=True)
    notes = []
    for ident, summary, detail in META:
        full = (HERE / (ident + '.md')).read_text()
        supports = re.search(r'^Support: (.+)\.$', full, re.M).group(1).split(', ')
        notes.append({'id': ident, 'summary': summary, 'detailedSummary': detail,
                      'text': full, 'support': supports})
    result = {'notes': notes, 'candidate': False}
    (HERE / 'native-notes.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    synopsis = (
        'The unrestricted positive greatest-minorant envelope requirement is obstructed for the unchanged qualified G331 cone. '
        'An explicit bounded continuous obstacle on an excellent nonnormal surface has no maximal geometric minorant. '
        'Complete positive theorems are proved at the published smooth BFJ hypotheses, on all excellent reduced curves, '
        'and on stated bijective-normalization sectors. Every positivity claim follows established class membership. '
        'This is an unverified draft with candidate=false; products, energy and P12.6 full operators remain separate.'
    )
    (HERE / 'argument.md').write_text('# P12.3: conductor obstruction and complete envelope sectors\n\n' + synopsis +
                                    '\n\n' + '\n\n'.join(n['text'] for n in notes))
    grant = json.loads((HERE / 'G331-qualified-grant.json').read_text())
    extract_grant(grant)
    annotation = json.loads((HERE / 'G331-mandatory-source-scope.json').read_text())
    annotation_md = '# Exact imported G331 mandatory annotation\n\n'
    for k, v in annotation.items():
        annotation_md += k + ': ' + (json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v) + '\n\n'
    (HERE / 'evidence' / 'imported-annotation-render.md').write_text(annotation_md)
    preamble = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,array,longtable}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\emergencystretch=4em
\title{Obstacle envelopes for the independently geometric singular cone\\
A conductor obstruction and complete positive sectors}
\author{Local mathematical draft for independent review}
\date{8 October 2026}
\begin{document}
\maketitle
\begin{abstract}
""" + prose(synopsis) + r"""
\end{abstract}
\tableofcontents
\newpage
"""
    paper = preamble + '\n\n'.join(latex_md(n['text']) for n in notes)
    paper += '\n\\appendix\n'
    for name in ['source-application-ledger.md', 'exact-scope.md', 'whole-proof-coverage.md',
                 'original-scope-and-noncircularity-decision.md']:
        paper += '\n' + latex_md((HERE / name).read_text()) + '\n'
    paper += '\n' + latex_md(annotation_md)
    paper += r"""
\begin{thebibliography}{9}
\bibitem{BFJ}
S. Boucksom, C. Favre and M. Jonsson,
\emph{Valuations and Plurisubharmonic Singularities},
Publ. RIMS 44 (2008), 449--494. Exact authorized local PDF/text binding
and complete immediate applications are stated in the source ledger.
\bibitem{G331}
Qualified caller grant G331, \emph{A geometric valuative psh cone on
excellent local germs}, with its entire mandatory source/scope annotation
and source ledger. Retained unchanged in the accompanying grant record.
It supplies the cone/comparison, not an envelope theorem.
\end{thebibliography}
\end{document}
"""
    (HERE / 'P12.3-paper.tex').write_text(paper)
    commands = []
    for attempt in [1, 2]:
        cmd = ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', 'P12.3-paper.tex']
        r = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
        output = r.stdout + r.stderr
        (HERE / 'evidence' / ('pdflatex-attempt-%d.txt' % attempt)).write_text(output)
        commands.append({'argv': cmd, 'attempt': attempt, 'exit_code': r.returncode,
                         'stdout_stderr_file': 'evidence/pdflatex-attempt-%d.txt' % attempt})
        if r.returncode:
            break
    (HERE / 'evidence' / 'build.json').write_text(json.dumps({
        'recorded_utc': datetime.now(timezone.utc).isoformat(), 'commands': commands,
        'status': 'pass' if all(c['exit_code'] == 0 for c in commands) and len(commands) == 2 else 'fail',
        'meaning': 'Artifact compilation only; no mathematical certification.'}, indent=2) + '\n')
    print(json.dumps({'notes': len(notes), 'candidate': False, 'build_exit_codes': [c['exit_code'] for c in commands],
                      'paper_bytes': (HERE / 'P12.3-paper.tex').stat().st_size}))
    return 0 if len(commands) == 2 and all(c['exit_code'] == 0 for c in commands) else 1

if __name__ == '__main__':
    raise SystemExit(main())
