#!/usr/bin/env python3
"""Audit only the seven supplied primary-source caches and retain literal pages."""
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'input-original.json').read_text())
assignment = data['assignment']
start = assignment.index('[\n', assignment.index('Read-only published source caches:'))
sources, _ = json.JSONDecoder().raw_decode(assignment[start:])

SPECS = {
    'GJR-2111.05741': {
        'pages': [31, 32, 33, 45, 46, 47, 50, 51, 63, 64, 65, 66, 67, 68,
                  70, 71, 72, 75, 76, 77, 78, 79, 80, 81],
        'checks': [
            ['5.1 and Example 5.3', 'Strict G-topology; arbitrary real bends need not be strict real-PL. No all-domain lisse-to-strict-PL inference is used.'],
            ['7.5, 7.6; 8.1--8.2', 'Real harmonic germs use integer harmonic tuples; morphism and arbitrary analytic scalar pullback preserve those tuples.'],
            ['10.3--10.10, 10.17', 'Weak smoothness is harmonic-tropicalization smoothness, sheafified on ordinary opens. Pullbacks use the composed harmonic tuple; joint-chart equality handles overlaps.'],
            ['11.1, 11.3; 12.4--12.5', 'Positive Hessians are integrated with nonnegative tropical weights; current differentiation uses Stokes only on boundaryless pure-dimensional domains.'],
            ['14.2 and its complete proof', 'Finite Galois invariant forms descend. For functions built by averaging, descent preserves their numerical values.'],
            ['14.5 and its complete proof', 'The scalar-extension integral equality has NO degree multiplier. It is used for finite Galois auxiliary extensions only.'],
            ['15.7 and its complete proof', 'Thuillier real harmonic functions on rig-smooth curves are harmonic in the GJR sense. Used only on harmonic pieces.'],
            ['15.9--15.11 and complete 15.11 proof', 'PDF visually checked: 15.11 says decreasing NET for arbitrary subharmonic targets on relatively compact ordinary opens in a smooth boundaryless curve. The ending sequence is for a piecewise real-linear target. Arbitrary subdivisions are explicitly not claimed to be formal-model skeletons.']
        ]
    },
    'GR-2506.13548v2-20261004': {
        'pages': [6, 7, 8, 10, 11, 12, 13, 14, 19, 20, 21, 22, 23, 30, 31, 33, 34],
        'checks': [
            ['2.7, 2.9, 2.11', 'Analytic fibres and scalar projections; finite morphisms have no relative boundary; boundary composition is equality over a locally separated target.'],
            ['3.4, 3.4.1; 3.5(3); 4.1 and 4.1.2', 'Original arbitrary starting class includes minus infinity. Interior-to-whole-curve extension is applied to the explicitly USC Gauss spike. Classical definition includes ALL analytic extensions and curve tests.'],
            ['3.9 and its complete proof', 'Perfect field is required for rig-smooth normalization. Finitely many rigid branch points, normalization quotient, local component separation and local constancy at rigid points are checked. No general weak-smooth finite descent is inferred.'],
            ['4.2 and its complete proof', 'Ordinary sheafiness, scalar stability, pullback and finite-surjective CLASSICAL descent; no weak-smooth descent assertion follows from this proposition.'],
            ['6.1 and its complete proof', 'Maximum principle at analytic interior points. Applied to compact connected proper fibres over H(c), not to arbitrary nonsaturated affine fibres.'],
            ['6.5 and its complete proof', 'Pointwise limits of nets need an USC limit. Used for convex continuous compositions, whose USC is explicit.']
        ]
    },
    'GR-2503.05513-20261004': {
        'pages': [14, 15, 16, 17],
        'checks': [['Section 5 curve comparison', 'Audited diagnostic foundation only. Its strict real-PL comparison is not used to infer weak smoothness of arbitrary classical functions or all-domain lisse functions.']]
    },
    'Thuillier-tel-00010990v1': {
        'pages': [33, 34, 75, 76, 81, 82, 83, 84, 103, 104, 105, 106],
        'checks': [
            ['2.1.1 sites, printed 19--20 / PDF 33--34', 'X_G all-domain and X_R strict rigid sites are explicitly different.'],
            ['3.1.5, printed 62 / PDF 76', 'Thuillier excludes an identically minus-infinity connected component; GR adds it. We use constants on that component.'],
            ['3.2.1, printed 68 / PDF 82', 'Lisse is all-domain local harmonic, not ordinary CLD smooth, and not automatically strict GJR real-PL.'],
            ['3.4.2 and complete proof, printed 89--90 / PDF 103--104', 'Finite-subset directed family gives a net. Our sequence requires the separate countable extraction proof.'],
            ['3.4.3--3.4.6', 'Curvewise Laplacian positivity and scalar stability are consistent with the GJR smoothing description; no new general higher-dimensional positivity equivalence is asserted.']
        ]
    },
    'CD-1204.6277v2-20261004': {
        'pages': [22, 23, 24, 25, 195, 196, 197, 198, 199, 200, 201, 421, 422, 423],
        'checks': [
            ['1.2.10--1.2.11', 'Lagerberg positive cones coincide in degrees (1,1) and (n-1,n-1); linear pullback preserves positivity.'],
            ['8.1.1, 8.1.4--8.1.6 and proofs', 'Actual saved v2 numbering: ordinary smooth positive generators, successive decreasing-sequence stages, stage-preserving pullback. It does not prove the arbitrary classical starting class lies at stage one.'],
            ['8.3.1 and complete proof', 'On a boundaryless tropical space, local integrability is required; ordinary smooth psh and positive curvature current are equivalent there. Not a theorem equating all weakly smooth classical and current notions.'],
            ['15.1.1--15.1.2 and proof', 'Actual saved v2 analytic ordinary-smooth chart description. Our boundary sequence has explicitly invertible logarithmic coordinates away from zeros and is constant near zeros.']
        ]
    },
    'Wanner-1801.04713v3-20261004': {
        'pages': [1, 2, 3, 4, 25, 28, 29, 30, 31],
        'checks': [
            ['Terminology', 'Complete, algebraically closed, nontrivially valued ground field.'],
            ['4.6 regularized maximum', 'Convex, smooth, coordinatewise nondecreasing and equals max away from the strip; our explicit convolution proves the bounds we actually use.'],
            ['Lemma 5.2 complete proof; Corollary 5.4 complete proof', 'Corollary requires finite continuous current-psh targets on opens of smooth proper algebraic curves and the stated residue/projective-line/Mumford alternatives. Its arbitrary-target intermediate object is a net; continuity allows compact Dini selection. Not imposed on the original class.']
        ]
    },
    'Berkovich-PMIHES-1993-78-5': {
        'pages': [],
        'checks': [['Proposition 1.5.5', 'Boundary composition source as explicitly restated in GR 2.11. Selected literal PDF pages are located dynamically by the numbered statement.']]
    }
}

out = ROOT / 'source-extracts'
out.mkdir(exist_ok=True)
records = []
for src in sources:
    stem = Path(src['literal_extract']).stem
    spec = SPECS[stem]
    raw = Path(src['literal_extract']).read_bytes()
    pdf_hash = hashlib.sha256(Path(src['pdf']).read_bytes()).hexdigest()
    extract_hash = hashlib.sha256(raw).hexdigest()
    if pdf_hash != src['pdf_sha256'] or extract_hash != src['extract_sha256']:
        raise ValueError('Supplied source hash mismatch: ' + stem)
    # Splitting bytes preserves the literal page bytes, including OCR/control characters.
    pages = raw.split(b'\x0c')
    chosen = list(spec['pages'])
    if not chosen:
        for i, page in enumerate(pages):
            if b'1.5.5.' in page or b'1.5.5 ' in page:
                chosen.extend(range(max(1, i), min(len(pages), i + 3)))
        chosen = sorted(set(chosen))
        if not chosen:
            raise ValueError('Cannot locate Berkovich 1.5.5')
    excerpt = b'\x0c'.join(pages[p-1] for p in chosen)
    name = stem + '-selected-literal-pages.txt'
    (out / name).write_bytes(excerpt)
    records.append({**src, 'pdf_hash_matches': True, 'extract_hash_matches': True,
                    'selected_pdf_pages_1_based': chosen,
                    'selected_literal_file': 'source-extracts/' + name,
                    'selected_literal_sha256': hashlib.sha256(excerpt).hexdigest(),
                    'application_checks': [{'statement': st, 'exact_application': app}
                                           for st, app in spec['checks']]})

provenance = {
    'id': 'P02.3',
    'sources': records,
    'pdf_visual_check': {'pages': ['GJR PDF 80', 'GJR PDF 81'],
                        'artifacts': ['pdf-checks/GJR-page-80.png', 'pdf-checks/GJR-page-81.png'],
                        'finding': 'The proposition says net; the final sequence is for a PL target; arbitrary subdivisions are expressly not formal-model skeletons.'},
    'primary_pdf_layout_checks': ['pdf-checks/Thuillier-103-104-layout.txt',
                                  'pdf-checks/CD-195-201-layout.txt'],
    'new_applications_proved_in': 'P02.3-argument.md',
    'evidence_type': 'Source-byte observations and draft mathematical proofs; no exhaustive computation or machine proof verification.',
    'missing_heavy_compute_facility': 'Not needed; no resource-heavy computation performed.',
    'execution_configuration': {'requested': 'Xean native Codex gpt-6.1-sol/xhigh',
                                'observed': 'Used current native Codex session only; model identity is not independently exposed by the local shell. No other model, subagent, installation, account or runtime change.'}
}
(out / 'source-provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')
env = {'python': sys.version, 'platform': platform.platform(), 'cwd': str(ROOT),
       'tex': subprocess.run(['pdflatex','--version'], capture_output=True, text=True).stdout.splitlines()[:2],
       'source_cache_access': 'Read only the supplied seven paths; no network retrieval.',
       'source_count': len(records)}
(ROOT / 'environment.json').write_text(json.dumps(env, indent=2) + '\n')
print(json.dumps({'sources': len(records), 'all_supplied_hashes_match': True,
                  'literal_pages_retained': sum(len(r['selected_pdf_pages_1_based']) for r in records)}, indent=2))
