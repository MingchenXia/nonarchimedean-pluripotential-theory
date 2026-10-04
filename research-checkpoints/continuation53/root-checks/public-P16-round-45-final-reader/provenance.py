#!/usr/bin/env python3
"""Retain literal, line-located extracts from the ten authorized public caches."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
SOURCE = Path('/workspace/research/shared-sources')
OUT = ROOT / 'source-extracts'
OUT.mkdir(exist_ok=True)

selections = [
 ('bj-curve-topology', 'P16-arxiv-1801.08229-20261004.txt', 622, 655,
  'Section 1.1.6, pp. 13-14',
  'Only the curve topology is used. The analytic normalization homeomorphism in the unibranch case is proved independently in the argument.'),
 ('bj-flag-ray-generators', 'P16-arxiv-1801.08229-20261004.txt', 968, 1028,
  'Definition 2.1, Example 2.5, Example 2.6, pp. 21-22',
  'Example 2.5 allows any ideal on a projective variety; the point ideal on singular X is therefore allowed. The spanning claim in Example 2.6 is applied only to smooth normalization Y. The new proof uses the ramification integer e_p to descend every generator.'),
 ('bj-model-nef-descent-proof', 'P16-arxiv-1801.08229-20261004.txt', 1610, 1692,
  'Definition 3.2 and Proposition 3.6 with proof, pp. 34-35',
  'Proposition 3.6(vi) applies to an already descended PL function. Normalization is finite, projective and surjective; the argument first proves the necessary PL descent and separately explains nef reflection via degrees of vertical curves.'),
 ('bj-pl-approximation', 'P16-arxiv-1801.08229-20261004.txt', 1707, 1742,
  'Proposition 3.10 with proof, p. 36',
  'The fixed class is ample on actual X. Descended nef PL functions are uniformly approximable by Hdom(X,L); a decreasing diagonal approximation is given explicitly in the argument.'),
 ('bj-curve-psh-and-regularization', 'P16-arxiv-1801.08229-20261004.txt', 2387, 2436,
  'Example 4.13 and Theorem 4.15, pp. 49-50',
  'The convex ray and slope-budget criterion is applied to smooth connected Y only. Theorem 4.15(iii) is applied on both X and Y after verifying their ample polarizations.'),
 ('bj-envelope-compactness-proof', 'P16-arxiv-1801.08229-20261004.txt', 2812, 2840,
  'Theorem 5.11 with proof, p. 58',
  'This is not invoked to obtain psh descent. Once the psh cones are identified, the weak topology and normalized cone are transported, without assuming compactness on singular X.'),
 ('bj-unibranch-gap', 'P16-arxiv-1801.08229-20261004.txt', 2843, 2895,
  'Theorem 5.12, Lemma 5.13 with proof, Conjecture 5.14 and Remark 5.15, pp. 58-59',
  'Lemma 5.13 assumes envelope properties on the target. It cannot prove those properties on that target by normalization. The curve proof avoids this circularity. Conjecture 5.14 is reported as a conjecture in this exact source version, not as a current impossibility theorem.'),
 ('bj-continuous-envelopes', 'P16-arxiv-1801.08229-20261004.txt', 2909, 2954,
  'Lemma 5.17 with proof, p. 60',
  'Applied after the envelope property is proved by homeomorphism and psh-cone descent. It identifies continuity of envelopes with that property.'),
 ('bj-smooth-envelope-input', 'P16-arxiv-1801.08229-20261004.txt', 2976, 2991,
  'Theorem 5.20 and Corollary 5.21, p. 61',
  'Only smooth, connected, projective Y over algebraically closed trivially valued k of characteristic zero is used. Pullback of an ample line bundle by the finite normalization is ample, not merely nef.'),
 ('bj-monotone-energy-proof', 'P16-arxiv-1801.08229-20261004.txt', 3650, 3731,
  'Theorem 7.1 with proof and Proposition 7.2, pp. 74-76',
  'The energy extension is available on possibly singular projective X. The equation (7.5) is used only for psh potentials already defined on X, before the onto descent theorem is established.'),
 ('bj-operator-and-pushforward-proof', 'P16-arxiv-1801.08229-20261004.txt', 3980, 4061,
  'Theorem 7.18 with proof and Proposition 7.19 with proof, pp. 81-82',
  'These construct genuine intersection-theoretic MA on finite-energy functions of actual X, including raw mass and normalization pushforward. The formula (7.18) is not an inverse-measure construction.'),
 ('bj-curve-laplacian', 'P16-arxiv-1801.08229-20261004.txt', 4060, 4073,
  'Example 7.20, p. 83',
  'The raw curve Laplacian formula is applied on Y and transported only after proving exact psh/energy descent. Its endpoint term vanishes for finite energy, which the argument also proves from the L2 slope condition.'),
 ('bj-comparison-proof', 'P16-arxiv-1801.08229-20261004.txt', 4530, 4603,
  'Theorem 7.40 and Theorem 7.44 with proofs, pp. 91-92',
  'These results have ample-class and finite-energy hypotheses but no smoothness hypothesis in this source. In the curve result their applications are checked using the constructed actual-X operator. Multiplying the probability inequality by V gives the raw comparison inequality.'),
 ('bj-differentiation-proof', 'P16-arxiv-1801.08229-20261004.txt', 4841, 4958,
  'Theorem 8.5 and Corollary 8.6 with proofs, pp. 97-99',
  'They differentiate E-down on singular X without assuming envelope regularity. Replacing E-down by E composed with P requires the envelope property, supplied here by the curve descent proof. The text extraction of the corollary proof contains sign/epsilon typos; the argument uses the correct bound |f-f_m| <= epsilon_m, and retains the literal text without correcting it.'),
 ('bj-surjectivity-and-node-proof', 'P16-arxiv-1801.08229-20261004.txt', 6089, 6157,
  'Theorem 12.8 with proof and Example 12.11, pp. 121-123',
  'Surjectivity is equivalent to the envelope property on irreducible projective X over algebraically closed trivially valued k. The proof cites Corollary 5.21 for compactness although the general applicable result is Theorem 5.11; our application uses Theorem 5.11. The node obstruction is proved explicitly in the new argument.'),
 ('bfj-v1-retained-hypotheses', 'P16-arxiv-1201.0188-20261004.txt', 62, 116,
  'Introduction and Theorem A, pp. 2-3; PDF watermark v1',
  'The saved v1 assumes smoothness, completeness, discrete valuation, residue characteristic zero, projectivity, ample L, function-field algebraizability of X and dual-complex support. It is not cited as a theorem for arbitrary finite-energy measures.'),
 ('be-not-pluripotential-paper', 'P16-arxiv-1805.01016-20261004.txt', 114, 170,
  'Theorem A and Corollary B, pp. 3-4',
  'Boucksom-Eriksson concerns spaces of norms and continuous psh metrics. It gives no general finite-energy singular equation theorem. The conditional continuity-of-envelopes hypothesis is retained.'),
 ('be-energy-projection-proof', 'P16-arxiv-1805.01016-20261004.txt', 3545, 3590,
  'Proposition 9.14 with proof, pp. 74-75',
  'Only a background projection-formula check is retained. The actual-X curve proof uses BJ Proposition 7.2, which covers the decreasing finite-energy extension, rather than silently extending this continuous-metric proposition.'),
 ('synthetic-measure-completion', 'P16-arxiv-2307.01697-20261004.txt', 53, 157,
  'Introduction and Theorem A, pp. 2-3',
  'Theorem A completes the space of measures and makes test-MA image dense. It does not identify that completion with an actual finite-energy psh potential space on a singular X. No such implication is used.'),
 ('ps-arbitrary-field-warning', 'P16-arxiv-2209.04879-20261004.txt', 1977, 1996,
  'Theorem 4.3 and Remarks 4.4-4.5, p. 35',
  'Continuous-metric operator over arbitrary fields is distinguished from the finite-energy operator. Remark 4.4 is reported with its own characteristic-zero wording; it is not used to weaken BFJ residue-characteristic hypotheses.'),
 ('gr-no-ma-claim', 'GR-2506.13548v2-20261004.txt', 67, 86,
  'Introduction, p. 2',
  'The September 2025 v2 treats singular analytic curves and classically psh functions but explicitly does not construct the Monge-Ampere operator in this paper. Thus its local theory is not used as the missing global equation theorem.'),
]

inventory = json.loads((OUT / 'source-inventory.json').read_text())
records = []
for ident, name, first, last, loc, application in selections:
    source = SOURCE / name
    lines = source.read_text().split('\n')
    literal = '\n'.join(lines[first-1:last]) + '\n'
    dest = OUT / (ident + '.txt')
    dest.write_text(literal)
    # Newline-only splitting agrees with rg's numbering, retaining form feeds.
    full = source.read_text()
    start = full.find(literal)
    if start < 0:
        raise ValueError((ident, 'not literal'))
    rec = {'id': ident, 'source': str(source), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
           'selection_method': 'Newline-only splitting; inclusive 1-based bounds (same as rg)',
           'line_start': first, 'line_end': last, 'character_start': start,
           'source_locator': loc,
           'pdf_page_range_from_formfeeds': [full[:start].count('\f') + 1,
                    full[:start + len(literal)].count('\f') + 1],
           'literal_file': str(dest.relative_to(ROOT)),
           'literal_sha256': hashlib.sha256(dest.read_bytes()).hexdigest(),
           'literal_extract': literal, 'application_check': application}
    records.append(rec)

pdf_rechecks = []
for ident, pdf_name, first_page, last_page in [
    ('BFJ-equation-first-page', 'P16-arxiv-1201.0188-20261004.pdf', 1, 1),
    ('BJ-page35-from-pdf', 'P16-arxiv-1801.08229-20261004.pdf', 35, 35),
    ('BJ-page75-from-pdf', 'P16-arxiv-1801.08229-20261004.pdf', 75, 75),
    ('BJ-page82-from-pdf', 'P16-arxiv-1801.08229-20261004.pdf', 82, 82),
    ('BJ-page98-from-pdf', 'P16-arxiv-1801.08229-20261004.pdf', 98, 98),
]:
    dest = OUT / (ident + '.txt')
    command = ['pdftotext', '-f', str(first_page), '-l', str(last_page), '-layout',
               str(SOURCE / pdf_name), str(dest)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    pdf_rechecks.append({'id': ident, 'pdf': str(SOURCE / pdf_name),
                         'pdf_pages': [first_page, last_page], 'argv': command,
                         'returncode': result.returncode, 'literal_file': str(dest.relative_to(ROOT)),
                         'literal_extract': dest.read_text(),
                         'check': 'Fresh extraction from the supplied PDF, retaining the displayed theorem statements and formulas rather than relying on the cache title or OCR alone.'})

(OUT / 'source-provenance.json').write_text(json.dumps({
    'scope': 'Only the ten user-authorized public primary-source caches and fresh workspace files.',
    'inventory': inventory, 'extracts': records, 'pdf_rechecks': pdf_rechecks,
    'evidence_limit': 'Hashes establish byte identity, not correctness. Extracts are literal published mathematical data; application checks and the new proofs remain unverified drafts.'
}, ensure_ascii=False, indent=2) + '\n')
print(f'Retained {len(records)} literal extracts; inspected {len(inventory)} authorized caches.')
