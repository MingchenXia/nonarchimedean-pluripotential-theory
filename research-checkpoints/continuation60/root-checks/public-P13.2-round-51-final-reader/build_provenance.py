#!/usr/bin/env python3
"""Read only the four supplied public caches; keep exact LF-indexed extracts."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CACHE = Path('/workspace/research/shared-sources')
SPECS = [
    ('Wu24', '2406.13684v1', 'Yueqiao Wu, Some non-Archimedean pluripotential theory on polarized affine cones',
     'P13-Wu-arxiv-2406.13684v1-20261004',
     '559cdb77b76167498a2935e52d39f4eafbcb266df963eef30d59c101ac13f790',
     '91cb6971ff8f4d1ccb2be1c7a7cabfabe250e39b0df8f8e4d32405c510485cd7',
     [
         ('main-theorem-and-outlook', 109, 150, 'Extension and comparison on the image only; the Outlook explicitly reports missing uniform differentiability and a future local equation.'),
         ('geometry-and-invariant-carrier', 194, 251, 'Rational quotient can be singular; the torus-invariant link is explicitly defined. No smooth quotient hypothesis follows.'),
         ('model-measure-normalization', 277, 332, 'Use n-1 potential factors, one radial factor, and division by vol(xi). The printed carrier is already X0^T here.'),
         ('same-ray-calculus-and-density', 344, 448, 'Addition compares a*xi and b*xi only. Correct Theorems 3.5 and 3.6 to the torified domain; an independent corrected separation proof is supplied.'),
         ('hodge-and-energy', 469, 614, 'Use the invariant difference space for Hodge; the intermediate second derivative at LF 595-600 is wrong, while LF 605-610 gives the correct expression.'),
         ('I-J-estimates', 615, 761, 'Use pairwise I-J bounds and quasi-triangle on a fixed ray; no assertion of completeness follows.'),
         ('psh-and-topology-proofs', 762, 959, 'These prove decreasing-net stability and topology properties. They do not prove bounded normalized PSH compactness or arbitrary envelope closure.'),
         ('finite-energy-MA-proof', 964, 1146, 'Decreasing-net mixed-MA construction applies on the corrected carrier. Lemma 6.4 has an omitted -E and an invalid displayed inequality; an explicit repaired continuous bound is proved in the argument.'),
         ('finite-energy-I-J', 1147, 1205, 'Pairwise estimates and uniform midpoint concavity suffice for Cauchy maximizing sequences, without existence of their limits.'),
         ('dual-energy-and-image-comparison', 1206, 1330, 'Repair the reversed inequality in Proposition 7.3 before using duality. Lemma 7.2 is justified independently using Radon monotone convergence. Corollary 7.8 compares outputs, not all targets.'),
     ]),
    ('Wu21', '2106.13395v2', 'Yueqiao Wu, Volume and Monge-Ampere energy on polarized affine varieties',
     'P13-Wu-arxiv-2106.13395v2-20261004',
     'db0aefd5af531344820303b517ec770f5558842332a0c4a39019658963308970',
     '30f6d5974548449381c1b3109173444269aa96cb7138b08dbdf4dcb1400f41ab',
     [
         ('volume', 201, 212, 'Volume is n! times the asymptotic count below Reeb degree m, divided by m^n.'),
         ('invariance-proof', 269, 297, 'Use the homogeneous-component criterion, with its character-matrix proof.'),
         ('filtration-normalizations', 588, 731, 'S uses all degrees <=m; for a rational quotient Lemma 3.16 gives S=n/(n+1)*S_tilde. Do not silently equate them.'),
         ('model-support-proof', 942, 1200, 'Proposition 5.5 has vanishing top wedge off the vertex; Corollary 5.7 constructs finite atomic support, then uses finite support plus divisibility of T(k) to establish pointwise torus invariance. The general Hessian is singular, not identically zero. Lemma 5.8 incorrectly uses full hyperplanes instead of active facets: max(x,y) and a test near (0,1) disprove the literal formula. The argument uses restricted oriented boundary facets and convex-gradient convergence, not that full-hyperplane identity.'),
         ('rational-quotient-measure-proof', 1235, 1355, 'Equal-degree homogeneous sections and the quotient embedding identify model measures for primitive rational xi. This does not prove all quotient psh functions are T-invariant, or quotient smoothness.'),
         ('energy-normalization-conflicts', 1356, 1379, 'Theorem 5.15(1), printed E=S, conflicts with Corollary 5.14 and Lemma 3.16. Constant homogeneous filtrations exhibit the conflict; this identity is not applied.'),
         ('toric-formula-and-proof', 1381, 1472, 'Printed Theorem 6.3 with its stated slice-volume convention fails a constant-shift test. No toric energy normalization is imported from it.'),
     ]),
    ('BJ22', '1801.08229v4', 'Sebastien Boucksom and Mattias Jonsson, Global pluripotential theory over a trivially valued field',
     'P16-arxiv-1801.08229-20261004',
     '8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52',
     '659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0',
     [
         ('main-theorem', 188, 206, 'Dense projective image is distinct from surjectivity; the stated smoothness/characteristic hypothesis is checked.'),
         ('envelope-compactness-proof', 2797, 2845, 'Theorem 5.11 identifies compactness with the envelope property, rather than deriving it from pointwise bounds alone.'),
         ('continuous-envelopes', 2894, 2935, 'Lemma 5.17 assumes projective psh classes; normality alone is not a proof of the envelope property.'),
         ('smooth-envelope-theorem', 2977, 3064, 'Theorem 5.20 assumes a smooth projective variety; a general normal quotient does not meet this assumption automatically.'),
         ('radon-net-monotone-convergence', 3956, 3980, 'The net lemma is proved independently in this argument for the actual compact carrier, so no projective-domain transfer is needed.'),
         ('uniform-differentiability-full-proof', 4841, 4964, 'Theorem 8.5 and Lemmas 8.7-8.8 use projective section norms, addition of polarizations, and a relative-volume comparison. These are not automatically affine-cone estimates.'),
         ('maximizing-nets-and-euler-lagrange', 5115, 5170, 'Theorem 9.11 and Corollary 9.12 require Theorem 8.5. Their conclusion cannot be transferred from concavity alone.'),
         ('integration-continuity-proof', 5245, 5270, 'Proposition 9.19 uses uniform approximation of the target by model-MA measures, via Lemma 9.17. It is not merely dominated convergence.'),
         ('completeness-surjectivity-full-proof', 6080, 6148, 'Theorem 12.8 assumes a projective ample class, and its existence implication uses compactness and Proposition 9.19. Theorem 12.9 assumes smoothness.'),
     ]),
    ('BJ23', '2307.01697v1', 'Sebastien Boucksom and Mattias Jonsson, Measures of finite energy in pluripotential theory: a synthetic approach',
     'P16-arxiv-2307.01697-20261004',
     '979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1',
     '8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4',
     [
         ('scope-and-main-theorem', 55, 171, 'Theorem A requires orthogonality, gives density and completeness of measures, and explicitly does not investigate finite-energy potentials.'),
         ('formalism-hypotheses', 280, 338, 'The ordered vector space of forms and positivity axioms must be realized, not assumed from notation; synthetic dimension would be cone dimension minus one.'),
         ('orthogonality-and-differentiability-proof', 1005, 1120, 'Definition 2.15 and Proposition 2.19 require an actual orthogonality limit. Max stability alone does not supply it.'),
         ('density-full-proof', 1121, 1170, 'Theorem 2.23 obtains weak and strong target convergence from uniform differentiation and orthogonality.'),
         ('measure-completion-full-proof', 1171, 1300, 'Theorems 2.24 and 2.26 complete the measure space under orthogonality; there is no theorem realizing every completed object as a Wu E1 potential.'),
     ]),
]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    out = ROOT / 'source-extracts'
    out.mkdir(exist_ok=True)
    result = {'line_convention': "one-based inclusive LF ranges in UTF-8 text.split('\\n'); form feeds do not start additional LF lines", 'sources': []}
    for sid, version, title, stem, expected_pdf, expected_txt, selections in SPECS:
        pdf = CACHE / (stem + '.pdf')
        txt = CACHE / (stem + '.txt')
        raw = txt.read_bytes()
        pdf_hash = sha(pdf.read_bytes())
        txt_hash = sha(raw)
        assert pdf_hash == expected_pdf, (sid, 'PDF hash mismatch')
        assert txt_hash == expected_txt, (sid, 'extract hash mismatch')
        (out / (sid + '-literal.txt')).write_bytes(raw)
        lines = raw.decode('utf-8').split('\n')
        src = {'id': sid, 'title': title, 'saved_version': version, 'public_source': 'https://arxiv.org/pdf/' + version,
               'pdf': str(pdf), 'pdf_sha256': pdf_hash, 'extract': str(txt), 'extract_sha256': txt_hash,
               'pdf_bytes': pdf.stat().st_size, 'extract_bytes': len(raw), 'LF_split_count': len(lines),
               'hash_matches_supplied': True, 'literal_statements_and_relevant_proof_bodies': []}
        for name, lo, hi, check in selections:
            assert 1 <= lo <= hi <= len(lines)
            literal = '\n'.join(lines[lo-1:hi])
            filename = sid + '-' + name + '.txt'
            (out / filename).write_bytes(literal.encode('utf-8'))
            src['literal_statements_and_relevant_proof_bodies'].append({
                'id': name, 'LF_start': lo, 'LF_end': hi, 'literal': literal,
                'artifact': 'source-extracts/' + filename, 'sha256': sha(literal.encode('utf-8')),
                'precise_application_check': check})
        result['sources'].append(src)
    path = out / 'source-provenance.json'
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'sources_verified': len(result['sources']), 'excerpts_preserved': sum(len(s['literal_statements_and_relevant_proof_bodies']) for s in result['sources']), 'provenance': str(path.relative_to(ROOT))}, indent=2))

if __name__ == '__main__':
    main()
