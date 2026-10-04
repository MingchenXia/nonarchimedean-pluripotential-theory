#!/usr/bin/env python3
"""Make canonical notes from the independently written argument.

The full proofs are embedded in the notes, not replaced by artifact pointers.
"""
import json
from pathlib import Path

proof = Path('P03.3-argument.md').read_text()


def between(start, end=None):
    i = proof.index(start)
    j = proof.index(end, i + len(start)) if end else len(proof)
    return proof[i:j].strip()


notes = [
    {
        'id': 'n1',
        'summary': 'Finite metric-graph obstacle theorem: the graph-affine subharmonic minorants have a greatest element, harmonic off contact and touching each designated boundary vertex. Exact contact-set computations pass on eight supplied graphs. This is a finite graph result, not an analytic P03.3 theorem.',
        'detailedSummary': 'For a nonempty finite connected metric graph with positive lengths, affine-on-edges finite obstacle, and any designated boundary subset $B$, the feasible vectors $u\\leq g$ with outgoing-slope sums nonnegative outside $B$ have a greatest element $p$. Maximum closure plus compact sum maximization proves existence and greatestness; perturbation proves boundary contact and interior contact/harmonic complementarity. Empty $B$ forces $p$ to be the constant minimum. An exact Dirichlet contact-set enumeration algorithm is proved exhaustive for this finite problem. Eight exact-rational examples pass, with 44 original contact systems and 44 translated systems. These execution facts do not verify any analytic identification or sharp classification.',
        'text': 'This note proves an independent finite graph lemma used by n2. It does not assert a new continuity theorem on an analytic domain.\n\n' + between('# 1. A finite graph obstacle problem', '# 2. A compact-skeleton criterion') + '\n\n' + between('# 6. Reproducibility and evidence'),
        'support': []
    },
    {
        'id': 'n2',
        'summary': 'Full-family continuity criterion under a finite harmonic skeleton presentation: global realizability of graph-subharmonic lifts, harmonic lifting, comparison for every competitor, and uniform density of skeletal obstacles. Comparison proves all-family majorization; obstacle stability gives continuity without a common competitor modulus. Analytic realization and comparison gates remain unverified.',
        'detailedSummary': 'For compact connected Hausdorff $X$ with finite designated boundary $D$, an entire continuous competitor class $\\mathcal C$ yields continuous raw envelopes for all finite continuous obstacles if it is translation invariant, contains constants and every globally lifted graph-subharmonic function, has harmonic comparison on relatively compact open sets, and is supported by dense finite skeletal obstacles whose graph-harmonic lifts are locally harmonic. By n1 the graph obstacle solution $q$ is harmonic off contact. For any $h\\leq g$, a positive superlevel of $h-q$ is compact away from contact and boundary; comparison forces $h\\leq q$. Thus $P_{\\mathcal C}g=q$ for the full family. The operator satisfies $\\|P_{\\mathcal C}f-P_{\\mathcal C}g\\|_\\infty\\leq\\|f-g\\|_\\infty$, giving uniform convergence and continuity for arbitrary obstacles. A finite-cover lattice argument proves a separate density lemma. An interval example has arbitrarily steep competitors and no common modulus. This is a structural sufficient criterion, not a sharp classification, and no new analytic domain is verified to satisfy its exact full-union hypotheses.',
        'text': 'The graph greatest-element and complementarity assertions used here are proved in n1. All other arguments below are supplied in this note. The exact analytic application to P03.3 is conditional: global real-PL realization, harmonic lifting, and comparison of every member of the literal locally-Fubini--Study/semipositive-real-PL union have not been independently verified on a new positive-dimensional analytic class.\n\n' + between('# 2. A compact-skeleton criterion', '# 4. Proper fibres') + '\n\nThe entire proof is stored in P03.3-argument.md and in the standalone P03.3-paper.tex. Rerun the recorded finite evidence with python finite_graph_envelope.py --input finite-graph-input.json --output finite-graph-output.json. Run bash render-paper.sh and python build-paper.py to render and build the paper twice. These execution checks do not certify this mathematical criterion or its analytic applications.',
        'support': ['n1']
    },
    {
        'id': 'n3',
        'summary': 'Exact full-family proper-fibre reduction for arbitrary continuous obstacles under open/closed projection, compact fibres, a class-preserving section, and fibrewise-constant competitors. Identifies unproved analytic, scalar-extension, branch, boundary, and sharp-necessity obligations. P03.3 remains unsolved; candidate=false.',
        'detailedSummary': 'A continuous closed open surjection $p:Y\\to X$ with nonempty compact fibres and a continuous section gives a continuous fibre-minimum obstacle $g(x)=\\min_{p^{-1}(x)}f$. If exact competitor classes pull back along $p$ and the section and all upstairs competitors are fibrewise constant, they are in bijection with downstairs competitors; hence $P_{\\mathcal C_Y}f=P_{\\mathcal C_X}g\\circ p$, including empty families. Together with n2 this conditionally gives all-obstacle continuity upstairs. The proof of openness/closedness effects on $g$ and competitor bijection is supplied in full. An independent scalar transfer follows by uniform stability if exact skeletal envelope pullback identities are separately proved. Proposed rational-affinoid and proper-factor applications remain unverified: global semipositive-real-PL realization, comparison for the full union, retractions/density including type-4 points, scalar identities, fibre Liouville over completed residue fields, and projection openness are genuine gaps. No necessity theorem or sharp classification is claimed; positivity and continuity remain distinct.',
        'text': between('# Result and exact scope', '# 1. A finite graph obstacle problem') + '\n\nThe only earlier proved envelope result used below is the compact-skeleton criterion and its uniform-stability argument in n2.\n\n' + between('# 4. Proper fibres', '# 6. Reproducibility and evidence') + '\n\nArtifacts: P03.3-argument.md contains the complete proof and scope; P03.3-paper.tex is a standalone readable paper; source-provenance.json records actual retrieval attempts and no primary theorem applications; status.json has exactly id,status,exact_result,proof_file,concrete_gaps. The original input artifacts are preserved. Rerun bash render-paper.sh, python build-paper.py, and python verify-artifacts.py. Both recorded TeX passes succeeded. Eight small exact graph examples passed; neither fact proves the analytic gates. No heavy compute, installations, external messages, or other model/worker invocations were used. The literal original target is not solved.',
        'support': ['n2']
    }
]
Path('notes.json').write_text(json.dumps({'notes': notes, 'candidate': False}, ensure_ascii=False, indent=2) + '\n')
print('Wrote 3 canonical notes; candidate=false.')
