#!/usr/bin/env python3
"""Assemble the canonical draft notes from the complete fresh argument."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent
argument = (root/'P02.1-argument.md').read_text()
curve_statement = argument.split('**Curve assertion A.**',1)[1].split('\n\n**Projective-bundle assertion B.**',1)[0]
bundle_statement = argument.split('**Projective-bundle assertion B.**',1)[1].split('\n\nIn both assertions',1)[0]
curve_proof = argument.split('# Checked published foundations',1)[1].split('# Projective fibres, descent, and proof of assertion B',1)[0]
bundle_proof = argument.split('# Projective fibres, descent, and proof of assertion B',1)[1].split('# Necessity statements, counterexamples to shortcuts, and remaining obligations',1)[0]
remaining = argument.split('# Necessity statements, counterexamples to shortcuts, and remaining obligations',1)[1]
build = json.loads((root/'diagnostics/build-diagnostics.json').read_text())
artifact = json.loads((root/'diagnostics/artifact-checks.json').read_text())
graph = json.loads((root/'diagnostics/graph-output.json').read_text())
evidence = '\n\nActual execution evidence: all seven supplied PDF/text hash pairs matched; '
evidence += str(artifact['literal_pages_verified'])+' retained literal pages were byte-checked. '
evidence += 'The input SHA-256 is '+build['artifact_sha256']['input.json']+'. '
evidence += 'input-original.json is byte-identical; assignment-original.txt retains the exact '
evidence += 'assignment string and task-original.json retains the task object. status.json '
evidence += 'has exactly id, status, exact_result, proof_file, concrete_gaps, with status partial. '
evidence += 'The final pdfLaTeX passes returned '+str([p['exit_code'] for p in build['tex_passes']])+'. '
evidence += 'Their actual diagnostic lines were '+json.dumps([p['diagnostic_lines'] for p in build['tex_passes']])+'. '
evidence += 'The first-build records are retained in diagnostics/initial-build. '
evidence += 'The eight exact-rational finite graph examples all passed. The first record is '
evidence += json.dumps(graph['records'][0])+', and the last record is '+json.dumps(graph['records'][-1])+'. '
evidence += 'These finite examples exhaust their specified piecewise-affine breakpoints only, '
evidence += 'and do not establish the general mathematical theorem. Python 3.12.14, Pandoc 3.1.11.1, '
evidence += 'pdfTeX 3.141592653-2.6-1.40.26 and the existing TeX Live 2025/dev/Debian environment were used. '
evidence += 'No external worker/model, installation, network work or resource-heavy computation was used. '
evidence += 'The requested native-model configuration is recorded but not independently attested by local tools. '
evidence += 'Rerun, in this directory: python retain_input.py; python retain_sources.py; python rerun.py; '
evidence += 'python verify_artifacts.py; python assemble_notes.py. Canonical notes are retained in final-notes.json. '
evidence += 'No source hash, finite diagnostic, artifact check or successful build is a mathematical correctness certificate.'

notes = [
    {'id':'n1',
     'summary':'Draft strict real-PL decreasing sequence for arbitrary classical psh on separated smooth boundaryless second-countable strict curves; real mesh correction and finite Galois descent avoid the invalid lisse/strict-PL identification. No sharp curve range claimed.',
     'detailedSummary':'Over every complete nontrivially valued field, the proof starts with arbitrary '
        'curve-test psh, including permitted -infinity values. On one compact strict domain Y and '
        'ordinary interior W, Thuillier supplies a decreasing lisse family f_S. Rational-sublevel '
        'Lindelof extraction gives f_n without assuming continuity of the target. Finite separable '
        'roots make replacement mesh and star coordinates actual value-group values. Convex chords '
        'give f_n <= g_n <= f_n+2^-n, weighted-slope positivity, and integral formal-model star '
        'bases prove actual strict real-PL membership. Galois averaging and GJR Corollary 5.12 '
        'descend to K. q_n=g_n+2^-n is semipositive and decreasing because q_(n+1)<=f_(n+1)+2^-n<=q_n; '
        'q_n-f_n<=2^(1-n) proves convergence also at -infinity points. Genus, residue torsion, '
        'perfection and residue characteristic restrictions are not added; boundarylessness '
        'and second countability are genuine hypotheses of this sufficient statement. '
        'The result is an unverified draft proof, not the original higher-dimensional characterization.',
     'text':'Draft mathematical proof; no independent correctness certificate is claimed.\n\nCurve assertion A.'+curve_statement+
        '\n\nChecked published foundations'+curve_proof+
        '\n\nThe full argument is P02.1-argument.md and its standalone embedding is P02.1-paper.tex. '
        'For source evidence rerun python retain_sources.py; for the finite formula diagnostics and '
        'two TeX passes rerun python rerun.py. The next note uses this curve result for a '
        'higher-dimensional sector; this note does not solve original P02.1.',
     'support':[]},
    {'id':'n2',
     'summary':'Draft higher-dimensional sector: every arbitrary classical psh on a full projective bundle over a smooth curve with second-countable analytification descends along compact projective fibres, hence has local decreasing strict semipositive real-PL pullbacks. Saturated domains are essential to this argument.',
     'detailedSummary':'For complete nontrivially valued K with a countable dense subset, smooth '
        'connected separated algebraic curve C0, ordinary open Omega in C0^an, and algebraic '
        'E of rank r+1>=2, every classical psh u on X=P(E)^an restricted to Omega is h composed '
        'with the bundle projection. Classical scalar/curve pullback and the published local '
        'maximum principle prove constancy on compact connected boundaryless projective '
        'H(b)-fibres. Trivialization sections prove classical psh descent and exact overlap '
        'agreement. n1 then supplies one fixed ordinary W and q_n; v_n=q_n composed with p '
        'is globally strict real-PL and semipositive on p^-1(W), and decreases pointwise to u. '
        'All analytic scalar extensions preserve this same sequence, even if their spaces '
        'are nonmetrizable. The examples are smooth normal unibranch spaces of dimension '
        'r+1 and include a proper projective factor. No result for every psh germ on '
        'nonsaturated open fibre charts, or for arbitrary normal/unibranch spaces, follows.',
     'text':'Draft projective-bundle assertion B.'+bundle_statement+
        '\n\nProjective fibres, descent, and proof of assertion B'+bundle_proof+
        '\n\nThis uses the curve construction and checked foundations of n1. The whole proof '
        'is retained in P02.1-argument.md, with standalone TeX in P02.1-paper.tex. '
        'Rerun python retain_sources.py and python rerun.py in the workspace. '
        'It is an unrestricted starting-function sector on the displayed saturated domain, '
        'not a characterization of all arbitrary higher-dimensional classical psh germs.',
     'support':['n1']},
    {'id':'n3',
     'summary':'Original P02.1 remains open here. Proved necessary F_sigma sublevels and retraction tests; strict real-PL maxima and nonsaturated/projective-boundary shortcuts can fail, but no sharp analytic regularization counterexample is supplied. Required artifacts and two-pass builds are retained.',
     'detailedSummary':'Every sequential decreasing finite continuous regularization forces '
        '{u<a}=union_(n,k){v_n<=a-1/k}, hence F_sigma strict sublevels. Regularization '
        'passes to analytic retracts by pullback, so projective fibres do not eliminate '
        'the curve test. GJR Example 5.3 supplies a membership counterexample to arbitrary '
        'real maxima at irrational tropical corners, not a failure of regularization. '
        'log|z1| on an affine projective-fibre chart invalidates the constancy/descent '
        'shortcut when fibres are incomplete; a closed disc invalidates boundaryless '
        'compact constancy when its actual relative boundary is retained. General '
        'higher-dimensional germ constructions, sharp necessity/failure, singular '
        'normalization descent and non-second-countable extraction remain unresolved. '
        'All seven source hash pairs and 57 literal pages were checked; eight finite '
        'rational graph diagnostics passed. Final TeX passes exit 0, each with one underfull '
        'hbox diagnostic and no label warnings; the initial build label warning was resolved. '
        'These observations do not certify mathematics; candidate is false.',
     'text':'Original-atom limitations and diagnostic evidence\n\n'+remaining+evidence,
     'support':['n1','n2']},
]
(root/'final-notes.json').write_text(json.dumps({'notes':notes,'candidate':False},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'notes':[n['id'] for n in notes], 'candidate':False,
                  'authoritative_text_characters':[len(n['text']) for n in notes]}))
