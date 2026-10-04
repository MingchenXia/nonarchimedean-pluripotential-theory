#!/usr/bin/env python3
"""Read only the five explicitly supplied caches; save literal LF-indexed evidence."""
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'input.json').read_text())
marker = 'Read-only published source caches:'
sources = json.JSONDecoder().raw_decode(data['assignment'].split(marker, 1)[1].lstrip())[0]
ranges = {
    '2406.13684v1': [(127, 146, 'Outlook: missing uniform differentiability'),
        (169, 246, 'Cone, rational quotient, torus action and carrier'),
        (255, 273, 'Valuative T and cumulative S conventions'),
        (274, 399, 'FS, denominator approximation, CPSH and proportional addition'),
        (400, 515, 'Density claim, positive mixed operator and Hodge index proof'),
        (522, 612, 'Probability energy and first/second variations'),
        (615, 657, 'I and J signs'),
        (762, 779, 'PSH definitions and decreasing FS approximation'),
        (937, 958, 'Extended energy and decreasing continuity'),
        (964, 1144, 'Actual finite-energy mixed operator proof and integration passage'),
        (1206, 1283, 'Dual energy, concavity sign and n+1/n normalization')],
    '2106.13395v2': [(44, 148, 'Volume, jumping averages, FS and stated main theorem'),
        (351, 374, 'Stokes and psh-approachability background'),
        (470, 502, 'Nonnegative filtration and finite type norm definitions'),
        (584, 754, 'S existence, continuity proof and rational normalization'),
        (890, 1044, 'FS formula, proof and homogeneous mixed measure vanishing'),
        (1046, 1197, 'Actual model measure support proof'),
        (1198, 1372, 'Energy, quotient embedding and Theorem 5.15 with proof'),
        (1441, 1473, 'Toric S/energy formula')],
    '1801.08229v4': [(2797, 2893, 'Envelope property and unibranch issue'),
        (2894, 2975, 'Envelopes and decreasing/increasing obstacle limits'),
        (4684, 4839, 'Extended energy definitions and limiting assertions'),
        (4841, 4964, 'Uniform differentiability Theorem 8.5 and complete relevant proof'),
        (5320, 5364, 'Global polarization comparison'),
        (6304, 6360, 'Orthogonality Theorem 13.1 and proof')],
    '2307.01697v1': [(234, 344, 'Synthetic fixed compact space and additive positive forms'),
        (570, 664, 'Commensurability estimate and proof'),
        (1008, 1118, 'Orthogonality and uniform derivative error equivalence'),
        (1542, 1604, 'Twisted energy setup'),
        (1755, 1854, 'Theorem 4.8 and relevant derivative proof')],
    '2609.27610v1': [(1, 86, 'Author, version, abstract and introduction statements'),
        (479, 511, 'Envelope definition and Lemma 2.20'),
        (567, 633, 'Connected fibre descent Proposition 2.24 and proof'),
        (635, 684, 'Tropical convexity Lemma 3.4 and APW imports'),
        (1488, 1535, 'Domination and local/global psh equivalence proof'),
        (1838, 1959, 'Weak psh, Theorems 6.3 and 6.5 with proof'),
        (1960, 2692, 'Complete remaining Section 6 proof route, including Lemma 6.6'),
        (2694, 2747, 'Body Theorem 7.1 and entire proof, including countability removal'),
        (2829, 2833, 'Literal APW26a/b bibliography entries')]
}
checks = {
    '2406.13684v1': [
        'Definitions 2.9, 3.1, 5.1 used for actual homogeneous FS/CPSH/PSH; root transport is proved directly.',
        'Theorem 3.5 full-link separation is not used: homogeneous tests factor through torification. A direct carrier-only separation proof replaces it.',
        'MA uses n-1 potential factors and one d\'d\'\' max(phi_xi,0), divided by vol(xi); energy has factor 1/(n vol(xi)).',
        'Fixed-Reeb decreasing continuity does not imply continuity for two varying polarizations or uniform tails.',
        'Proposition 7.3 inequality at LF 1249 has the wrong concavity direction as printed. Correct direction is independently derived.',
        'Lemma 6.4 LF 1015-1017 sign chain is not used; a corrected positive mixed estimate is derived in the argument.'
    ],
    '2106.13395v2': [
        'Theorem 3.12/Corollary 3.13 provide existence of S for a nonnegative linearly bounded multiplicative T-invariant filtration; quantitative comparison is proved by weight-subspace inclusions.',
        'A constant shift on A^2 gives S=2/3 and probability-normalized E=1. Thus Theorem 5.15 E=S is incompatible with the displayed definitions.',
        'Lemma 3.16(b) already displays S=n/(n+1) times the degreewise average. No claimed general corrected energy identity is silently substituted.',
        'Rational quotient FS and measure correspondence is checked only at a fixed rational Reeb; its target changes with the grading.'
    ],
    '1801.08229v4': [
        'Theorem 8.5 is on one projective variety and a fixed ample class; n there is projective dimension, one less than cone dimension.',
        'Its proof uses an actual positive mixed measure on omega+epsilon omega-prime and mixed intersection masses. Root transport is nonlinear and does not provide that additive structure.',
        'Theorem 13.1 requires the envelope property and uses Theorem 8.5/Corollary 8.6 in its proof; using orthogonality to prove differentiability needs an independent cone argument.'
    ],
    '2307.01697v1': [
        'The setup needs a common dense test vector space, additive ordered closed forms, integration by parts, positive mixed products and Hodge negativity.',
        'Theorem 4.8 assumes orthogonality and submean properties established earlier. These axioms have not been verified for varying Reeb fields on the cone carrier.'
    ],
    '2609.27610v1': [
        'Lyuhui Wu is distinct from Yueqiao Wu; this is a September 2026 v1 preprint, with no independent acceptance assumed.',
        'Body Theorem 7.1 covers geometrically unibranch projective varieties; the complete-field convention appears in setup and Theorem 6.5.',
        'Theorem 6.5 first requires a countable dense subfield. Over a trivial valuation this means a countable field. Section 7 separately treats unrestricted cardinality.',
        'Proof route: 7.1 -> 6.5 -> 6.3 -> 6.9, 6.14 and singular-locus induction -> strict psh barrier 6.6/6.7 -> APW26b Proposition 5.7, Lemma 5.11, and Lemma 3.4 APW imports.',
        'APW26a/b are only listed as Preprint (2026); no IDs or proof texts are supplied. Their indispensable imported local assertions are retained as unresolved dependencies, not replaced by this audit.',
        '6.5 LF 1942 reduces an arbitrary ample semipositive model form to a trivial embedding form without giving the reference-change/reduction argument there; not independently supplied here.',
        '7.1 LF 2731 must be read with psi a psh PL competitor below f; the literal unrestricted PL quantifier cannot be valid.',
        '7.1 base-change step requires MA pushforward compatibility, positivity, orthogonality and domination. The displayed support equality at LF 2742-2743 only needs, and generally gives, an inclusion.',
        'Rational cone quotient is normal, hence geometrically unibranch in this algebraically closed char-zero setting. The actual ample rational datum is checked via an integral Veronese, preserving the residual torus.',
        'Conditional rational carrier envelope transfer and quantitative irrational envelope transfer are proved in the argument. No finite-energy energy/MA limiting passage follows from this envelope theorem alone.'
    ]
}

for version in ['2406.13684v1', '2106.13395v2', '1801.08229v4', '2307.01697v1']:
    ranges[version].insert(0, (1, 20, 'Literal title, authors and arXiv version/date header'))

out = ROOT / 'source-extracts'
out.mkdir(exist_ok=True)
records = []
for src in sources:
    version = src['saved_version']
    rec = dict(src)
    rec['verified_files'] = []
    for key, expected_key in [('pdf', 'pdf_sha256'), ('literal_extract', 'extract_sha256'), ('abstract_html', 'abstract_sha256')]:
        if key in src:
            path = Path(src[key])
            raw = path.read_bytes()
            sha = hashlib.sha256(raw).hexdigest()
            assert sha == src[expected_key], (path, sha, src[expected_key])
            rec['verified_files'].append({'kind': key, 'bytes': len(raw), 'sha256': sha, 'matches_supplied': True})
    raw = Path(src['literal_extract']).read_bytes()
    lines = raw.decode('utf-8').split('\n')
    rec['LF_line_convention'] = "1-based inclusive indices into UTF-8 text.split('\\n'); no splitlines or form-feed normalization"
    rec['LF_line_count'] = len(lines)
    rec['excerpts'] = []
    for a, b, label in ranges[version]:
        literal = '\n'.join(lines[a-1:b])
        filename = f'{version}-LF-{a}-{b}.txt'
        (out / filename).write_text(literal, encoding='utf-8')
        rec['excerpts'].append({'LF_start': a, 'LF_end': b, 'description': label, 'artifact': filename, 'literal_text': literal, 'sha256': hashlib.sha256(literal.encode()).hexdigest()})
    rec['new_application_checks_and_limitations'] = checks[version]
    records.append(rec)
result = {'scope': 'Only five user-listed public primary caches; read-only sources. Draft audit, not a correctness verdict.', 'sources': records}
(out / 'source-provenance.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
env = {'python': sys.version, 'platform': platform.platform(), 'cwd': str(ROOT), 'sources_checked': len(records), 'input_sha256': hashlib.sha256((ROOT/'input.json').read_bytes()).hexdigest(), 'input_original_sha256': hashlib.sha256((ROOT/'input-original.json').read_bytes()).hexdigest()}
env['pdflatex_version'] = subprocess.run(['pdflatex', '--version'], text=True, capture_output=True).stdout
(ROOT / 'environment.json').write_text(json.dumps(env, indent=2)+'\n')
print(json.dumps({'sources': len(records), 'excerpt_count': sum(len(r['excerpts']) for r in records), 'all_supplied_hashes_match': True, 'input_original_byte_identical': (ROOT/'input.json').read_bytes() == (ROOT/'input-original.json').read_bytes()}, indent=2))
