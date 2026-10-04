#!/usr/bin/env python3
"""Read only the seven authorized caches; retain literal selected statements/proofs."""
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'input-original.json').read_bytes())
assignment = DATA['assignment']
sources = json.loads(assignment[assignment.index('[\n  {\n    "public_source"'):])
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)

# Inclusive, one-based lines in the supplied literal caches. No normalized OCR.
selections = {
    'GR-2506.13548v2-20261004.txt': [
        ('GR-ordinary-psh-classical-comparison', 84, 112),
        ('GR-curve-definition-properties', 453, 546),
        ('GR-boundary-proof', 669, 782),
        ('GR-classical-definition-pullbacks', 1108, 1185),
        ('GR-local-maximum-proof', 1618, 1653),
    ],
    'GR-2503.05513-20261004.txt': [
        ('GR-PL-curve-comparison', 798, 846),
        ('GR-piecewise-smooth-positivity', 1250, 1278),
    ],
    'Thuillier-tel-00010990v1.txt': [
        ('Thuillier-all-domain-strict-sites', 1428, 1465),
        ('Thuillier-Picard-proof', 3587, 3722),
        ('Thuillier-lisse-domains', 4105, 4217),
        ('Thuillier-regularization-proof', 5284, 5317),
        ('Thuillier-scalar-proof', 5353, 5375),
    ],
    'GJR-2111.05741.txt': [
        ('GJR-15.9-15.11-proofs', 4047, 4118),
    ],
    'CD-1204.6277v2-20261004.txt': [
        ('CD-positive-pullback-proof', 994, 1025),
        ('CD-ordinary-positive-representative-proof', 7337, 7356),
        ('CD-stage-0-stage-1-pullback', 9724, 9792),
        ('CD-uniform-sequence-proof', 9817, 9864),
        ('CD-convex-composition-proof', 9885, 9928),
        ('CD-current-positivity-boundaryless', 9993, 10025),
        ('CD-ordinary-open-chart-proof', 21540, 21578),
        ('CD-scalar-integration-proof', 22153, 22170),
    ],
    'Wanner-1801.04713v3-20261004.txt': [
        ('Wanner-field-conventions', 166, 181),
        ('Wanner-lisse-regularization-net', 250, 269),
        ('Wanner-5.2-proof-5.4-proof-5.5', 1628, 1778),
    ],
}

checks = [
    {'claim': 'arbitrary classical curve target -> Thuillier subharmonic or -infinity',
     'source': 'GR v2 Definition 3.4, 3.4.2 and 4.1.2',
     'application': 'Only on connected smooth strictly analytic boundaryless curve neighborhoods. The identically -infinity case uses constant approximants.'},
    {'claim': 'lisse regularization', 'source': 'Thuillier Theorem 3.4.2, literal proof retained',
     'application': 'Provides a net, not a sequence. Restrict its continuous terms to one strictly affinoid Y inside the relatively compact open supplied by the theorem.'},
    {'claim': 'ordinary smoothing of a lisse term', 'source': 'Wanner Lemma 5.2, complete literal proof retained',
     'application': 'K is complete, algebraically closed and nontrivially valued; C smooth proper algebraic; H_C subset ordinary C-infinity. Each selected finite lisse term on the same strictly affinoid Y is subharmonic on Y minus boundary. Obtain a continuous approximant on Y, ordinary smooth and psh on that same interior, uniformly within epsilon_j.'},
    {'claim': 'verified concrete sufficient H_C conditions', 'source': 'Wanner Corollary 5.4 proof; Thuillier Theorem 2.3.21 proof',
     'application': 'Residue field algebraic over a finite field, or C=P1, or C Mumford. Corollary 5.4 itself only treats finite continuous functions; arbitrary-target extension is proved here using the net and countability.'},
    {'claim': 'weakly smooth regularization limitation', 'source': 'GJR Proposition 15.11 and its proof',
     'application': 'The conclusion is a decreasing NET of WEAKLY smooth psh functions. The last proof sentence obtains a sequence for a fixed lisse term, not for the original net. Not used as an ordinary smooth regularization theorem.'},
    {'claim': 'strict versus all-domain site', 'source': 'Thuillier 2.1.7, Definition 3.2.1, Proposition 3.2.4; GJR 15.8-15.9',
     'application': 'Do not infer strict R-PL membership from all-domain lisse membership. The curve argument uses Wanner Lemma 5.2 directly on a strictly affinoid domain, never such a PL identification.'},
    {'claim': 'ordinary smoothness and smooth positivity', 'source': 'saved CD v2 Proposition 15.1.1(b), Corollary 15.1.2; Lemma 8.1.4(a); Proposition 8.1.5; Lemma 1.2.11',
     'application': 'Use ordinary OPEN charts and local invertible analytic functions. Stage 0 is d-prime d-double-prime >=0; pullback preserves this form positivity. CD Lemma 6.5.1 gives positive tropical representatives, whose pulled images lie in the same paralinéaire support, including after scalar extension. Stage 2 is not substituted for stage 1.'},
    {'claim': 'current positivity', 'source': 'saved CD v2 section 8.3 assumption and Proposition 8.3.1; Stokes section 7.7',
     'application': 'Assert positive currents on the boundaryless curve interiors and boundaryless proper-fibre products only. Boundary-spike approximants have nonnegative d-prime d-double-prime as forms; no unqualified boundary current positivity assertion is made.'},
    {'claim': 'classical boundary spike and pullback', 'source': 'GR v2 Proposition 3.5(3), full proof; 4.1.2; Proposition 4.2(5,6)',
     'application': 'A USC spike at the sole boundary point of the disc is zero on its interior, hence classically psh including all analytic field extensions. Pullback to a product is classical psh. This is not a harmonic nonsmoothness argument.'},
    {'claim': 'proper fibre constancy', 'source': 'GR v2 Theorem 6.1, full proof',
     'application': 'Apply over H(z) to P^m: compact, connected and boundaryless. USC functions attain their maximum; the finite maximum locus is nonempty, closed, and open by Theorem 6.1. Then use a rational section to descend all targets on the saturated domain.'},
    {'claim': 'normalization application', 'source': 'GR v2 Proposition 4.2(6); CD ordinary charts',
     'application': 'New proof is limited to a finite normalization which is an isomorphism away from one K-rational singular point and has exactly one point over it. Closed bijection -> homeomorphism. Each ordinary smooth term is constant near the rational preimage, so descends as ordinary smooth; no general smooth descent along finite maps is claimed.'},
    {'claim': 'Picard/genus limitation', 'source': 'Thuillier Theorem 2.3.21/Lemma 2.3.22; GJR Remark 15.10; Wanner Remark 5.5',
     'application': 'Under the precise semistable type-2 setup H_x/F_x = Pic^0(C_x) tensor_Z R. This measures failure of harmonic ordinary smoothness, not failure of decreasing psh approximation. Positive genus alone does not imply nonzero quotient.'},
]

manifest = {'sources': [], 'application_checks': checks, 'pdf_visual_checks': []}
for src in sources:
    entry = dict(src)
    for kind in ['pdf', 'extract']:
        filename = src['pdf' if kind == 'pdf' else 'literal_extract']
        actual = hashlib.sha256(Path(filename).read_bytes()).hexdigest()
        entry[kind + '_actual_sha256'] = actual
        if actual != src[kind + '_sha256']:
            raise ValueError(f'hash mismatch for {filename}')
    p = Path(src['literal_extract'])
    lines = p.read_bytes().splitlines(keepends=True)
    entry['selected_literal_extracts'] = []
    for label, first, last in selections.get(p.name, []):
        dest = OUT / (label + '.txt')
        # Python bytes.splitlines only splits on LF/CR, preserving PDF form feeds.
        # Match the line numbers used by sed/rg: count only LF.
        raw_lines = p.read_bytes().split(b'\n')
        selected = b'\n'.join(raw_lines[first-1:last]) + b'\n'
        dest.write_bytes(selected)
        entry['selected_literal_extracts'].append({
            'file': str(dest.relative_to(ROOT)), 'first_line': first,
            'last_line': last, 'sha256': hashlib.sha256(selected).hexdigest()})
    manifest['sources'].append(entry)

# Resolve damaged-font OCR against the actual primary PDFs, locally.
import fitz
visuals = [
    ('Thuillier-tel-00010990v1.pdf', 72, 'Thuillier-PDF-p72'),
    ('Thuillier-tel-00010990v1.pdf', 73, 'Thuillier-PDF-p73'),
    ('GJR-2111.05741.pdf', 80, 'GJR-PDF-p80'),
]
for basename, page, label in visuals:
    source = next(x for x in sources if Path(x['pdf']).name == basename)
    with fitz.open(source['pdf']) as doc:
        p = doc[page-1]
        png = OUT / (label + '.png')
        txt = OUT / (label + '-fresh-pdf-text.txt')
        p.get_pixmap(matrix=fitz.Matrix(1.35, 1.35)).save(str(png))
        txt.write_text(p.get_text())
    review = {
        'Thuillier-PDF-p72': 'Direct visual inspection confirms H_x/F_x = Pic^0(C_x) tensor_Z R, in the geometrically connected proper semistable type-2 setup; theorem conditions are residue field algebraic over a finite field or geometric local P1.',
        'Thuillier-PDF-p73': 'Direct visual inspection confirms the Picard quotient and the torsion criterion. The PDF really says the group is finite in its final bullet; that stronger claim is not used. The needed torsion assertion follows because each individual point is defined over a finite field and belongs to its finite rational-point group.',
        'GJR-PDF-p80': 'Direct visual inspection confirms Proposition 15.11 says decreasing net of weakly smooth psh functions, not a sequence and not ordinary smooth.',
    }[label]
    manifest['pdf_visual_checks'].append({'source': source['public_source'],
        'pdf_page_one_based': page, 'image': str(png.relative_to(ROOT)),
        'fresh_text': str(txt.relative_to(ROOT)),
        'review': review})

(OUT / 'source-provenance.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
env = {'python': sys.version, 'platform': platform.platform(),
       'commands': {}}
for command in [['pdflatex','--version'],['pdftotext','-v']]:
    r = subprocess.run(command, text=True, capture_output=True)
    env['commands'][' '.join(command)] = {'returncode': r.returncode,
        'stdout': r.stdout, 'stderr': r.stderr}
env['execution_constraints'] = {
    'fresh_workspace_only': True, 'network_used': False, 'installed_software': False,
    'subagents_or_other_models': False, 'heavy_computation': False,
    'runtime_status_tool': 'not exposed among available tools; no runtime changes attempted'}
(ROOT / 'environment.json').write_text(json.dumps(env, indent=2)+'\n')
summary = f'Verified {len(sources)} PDF/extract pairs; retained {sum(len(x["selected_literal_extracts"]) for x in manifest["sources"])} literal extracts and {len(visuals)} PDF pages.'
(ROOT/'source-verification-output.txt').write_text(summary+'\n')
print(summary)
