#!/usr/bin/env python3
"""Fresh builder for the own proof notes, JSON, and LaTeX/PDF artifacts."""
from pathlib import Path
import json, subprocess

ROOT = Path(__file__).resolve().parent
metadata = [
('n1', 'Exact bounded geometric input domain from qualified G331; full supports and conductor fibres retained, n-1 arity, degree-n component convention, no product grant.',
 'Fixes proper primary reference data, defines bounded inputs in the actual decreasing completion, admits zero and mixed-zero inputs belonging to that class, and excludes all bottom/unbounded inputs. Uses only the supplied independent cone/comparison, compact topology, density, and full descent. Dimension zero is empty and curves have zero potential entries.', ['G331']),
('n2', 'Proves the all-support primary mixed-multiplicity kernel and positivity at arbitrary field/characteristic; no geometric intersection or locality conclusion.',
 'Proves symmetry, product/power linearity, single-slot inclusion monotonicity via simultaneous superficial choices, integral-closure invariance via a finite graded algebra/ray-polynomial argument, and full-boundary valuative well-definedness. Exact current Swanson--Huneke immediate units and finite residue-field transfer are qualified. Unit slots have zero moments, lower-dimensional components contribute zero by convention.', ['G331','n1']),
('n3', 'Constructs positive bounded moment measures for real C and actual bounded D inputs, with representation independence and weak descending-net continuity; these are not yet actual geometric products.',
 'Gives mass and negative-shift error bounds, extends rational moments to real continuous tuples and then every bounded actual decreasing-net completion tuple, without increasing closure or flattening. Proves additivity, order on ideal moments, majorant supremum formula, and weak descending-net convergence for a common bounded net with a specified limit in D. Does not prove measure-order monotonicity, total variation convergence, independent Cartier comparison, or locality.', ['G331','n1','n2']),
('n4', 'Exact one-factor primary-gauge change and residue-degree normalization for moment measures; full bounded BFJ comparison only in its published smooth characteristic-zero closed-germ range.',
 'Proves nu_b=T_*[v_a(b) nu_a], coefficient-wise normalization over actual top-dimensional normal centres with residue-degree weights and no vertical generic degree, and equality with the published BFJ operator on all bounded inputs/all semivaluations at smooth affine closed germs over algebraically closed characteristic-zero fields. Neither singular Cartier comparison nor locality is imported from BFJ Section 4.', ['G331','n1','n2','n3']),
('n5', 'Actual geometric curve zero-potential reference measure, Cartier comparison and model independence, with locality/continuity at zero arity and exact residue/gauge weights.',
 'For every excellent reduced curve proves mu=sum f_q ord_q(a) delta_(ord_q/ord_q(a)), and independent real Cartier degree comparison on every actual primary model using a finite normalization graph and a local snake-sequence length proof. Gives exact branch class and singleton conductor fibres, direct DVR and empty cases, and a generic-degree-one normalization whose residue degree d gives mass d. This is not a positive-arity higher-dimensional theorem.', ['G331','n1','n2','n3','n4']),
('n6', 'Exact nilpotent-data obstruction, lower-dimensional top-degree degeneracy, and a toy counterexample to deriving locality from positivity/continuity alone.',
 'Identical reduced boundary/gauge data can have unreduced Samuel multiplicity one or two, so nilpotent lengths require extra data. In a dimension-two surface/curve fibre product a nonzero curve-only bounded geometric input has zero degree-two moment measure. A two-point positive additive continuous map fails locality; it does not satisfy the actual kernel and is not a counterexample to P12.4. Small exact finite arithmetic evidence is separated from the universal arguments.', ['G331','n1','n2','n3','n4','n5']),
('n7', 'Entire original P12.4 remains unresolved: higher-dimensional independent Cartier comparison and actual locality are not proved; complete partial-proof deliverables retained, candidate=false.',
 'Records the exact partial results, zero-arity geometric curve range, actual bounded moment domain, smooth specialization and gauges/normalization, and the two outstanding geometric obligations. No impossibility claim for reduced P12.4, no energy/general finite-map result, and no promotion of moment measures to geometric products. Provides rerun artifacts and separates mathematical drafts from finite/build/hash consistency evidence.', ['G331','n1','n2','n3','n4','n5','n6'])
]
notes = []
for ident, summary, detail, support in metadata:
    notes.append({'id': ident, 'summary': summary, 'detailedSummary': detail,
                  'text': (ROOT / (ident+'.md')).read_text(), 'support': support})
native = {'notes': notes, 'candidate': False}
(ROOT / 'native-notes.json').write_text(json.dumps(native, ensure_ascii=False, indent=2)+'\n')
intro = '''# Bounded local moment measures and the geometric curve reference case

Partial progress on original P12.4. This manuscript does **not** claim a complete singular/nonnormal geometric Monge--Ampere construction. It proves an algebraic bounded moment extension and an actual geometric zero-potential curve reference case. Independent higher-dimensional Cartier intersection comparison and open-set locality remain unproved. The final candidate flag is false.

The mathematical arguments, published-source applications, finite observations, and artifact integrity checks are distinct. The only incoming grant is qualified G331. Its complete source, mandatory annotation, ledger, and exact scope are retained unchanged locally. No supplied executable or unreviewed route is a theorem premise.

'''
(ROOT / 'argument.md').write_text(intro+'\n\n'.join(n['text'] for n in notes))
report = {'commands': [], 'note': 'Successful compilation does not verify the mathematical claims.'}
command = ['pandoc', 'argument.md', '--standalone', '--to=latex', '--output=P12.4-paper.tex',
           '--metadata=title:Bounded local moment measures and the geometric curve reference case',
           '--metadata=author:Fresh partial reconstruction of original P12.4',
           '--metadata=date:8 October 2026', '--variable=geometry:margin=1in',
           '--variable=fontsize:11pt', '--toc']
proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
report['commands'].append({'argv': command, 'exit_code': proc.returncode,
                           'stdout': proc.stdout, 'stderr': proc.stderr})
if proc.returncode == 0:
    for attempt in range(3):
        command = ['pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','P12.4-paper.tex']
        proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        report['commands'].append({'argv': command, 'attempt': attempt+1, 'exit_code': proc.returncode,
                                   'stdout': proc.stdout, 'stderr': proc.stderr})
        if proc.returncode:
            break
report['all_success'] = all(c['exit_code'] == 0 for c in report['commands'])
(ROOT / 'reports' / 'build-results.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'notes':len(notes), 'candidate':False, 'build_success':report['all_success']}))
if not report['all_success']:
    raise SystemExit(1)
