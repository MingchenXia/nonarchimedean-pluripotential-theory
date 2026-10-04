"""Publish the independently checked support-axis theorem with explicit retained fields."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
source = R / 'root-checks/public-P16-round-48-final-reader-v3/P16.6-paper.tex'
correctness = R / 'root-checks/P16.6-round48-actual-correctness-review.json'
scope = R / 'root-checks/P16.6-round48-original-scope-actual-review.json'
assert hashlib.sha256(source.read_bytes()).hexdigest() == '6600e95c3834074ecbb1c73930ddca92ece56f80972d5712086c0533fc8487f5'
assert hashlib.sha256(correctness.read_bytes()).hexdigest() == '56c9a68797ab7e9479d39c7a0f267a1f0c5f0fc9204f35e8e9075f85bb2c0089'
assert hashlib.sha256(scope.read_bytes()).hexdigest() == 'ea7efd8dde5743fe190dbd6b03769567e2c388dbd01334354d1fb80cf7075e41'
c = json.loads(correctness.read_text())
q = json.loads(scope.read_text())
assert c['verdict'] == q['verdict'] == 'PASS'
assert len(c['premises']) == 16 and len(c['passages']) == 18
assert {p['premise'] for p in c['passages']} == set(range(16))
assert all(p['statement'] == c['premises'][p['premise']] for p in c['passages'])
assert not q['premises'] and not q['passages']
D = R / 'deliverables/original-P16.6'
D.mkdir(exist_ok=True)
target = D / 'P16.6-paper.tex'
assert not target.exists()
s = source.read_text()
def replace(old, new):
    global s
    assert s.count(old) == 1, old[:100]
    s = s.replace(old, new)

replace(r'\title{P16.6: arbitrary-support finite-energy targets at two established field endpoints}', r'\title{Genuine finite-energy Monge--Amp\`ere equations with arbitrary measure support}')
replace(r'\author{Public-source audit and partial theorem; unverified draft}', r'\author{}')
replace('This is a partial result for the original atom, not a solution of its entire residual scope. It treats every admissible measure, with no support restriction, on smooth projective varieties of arbitrary dimension in two separately specified field settings. The trivial-field theorem is source-established. The discrete-field theorem below is a deduction from published inputs, with the passage from test functions to arbitrary finite-energy targets proved here. No claim of novelty is made. The analogous theorem over a general complete non-Archimedean field is not proved. Candidate status is false.', r'''\begin{abstract}
We establish the genuine finite-energy Monge--Amp\`ere operator and
existence and uniqueness modulo constants for every admissible positive
Radon measure, without a support restriction, in two explicitly retained
field settings. The variety is smooth, projective and ample in arbitrary
positive dimension. The field is either algebraically closed and
trivially valued of characteristic zero, or complete, nontrivially
discretely valued with residue characteristic zero. The raw mass is the
top self-intersection of the ample line bundle; the measure condition is
finite dual energy. The trivial-field theorem is source-established.
For the discrete field we prove the passage from model tests to
arbitrary finite-energy targets and combine it with published operator,
compactness, envelope and comparison inputs. No torus action, skeletal
support or function-field algebraizability is assumed.
\end{abstract}

The original P16.6 support axis permits stating the hypotheses retained
from the other axes. The two theorems below remove every support
restriction within their stated fields. The extension to arbitrary
complete, potentially nondiscrete fields is the separate P16.4 question.
No literature-priority claim is made.''')
replace('The proof uses only the supplied primary sources and their explicitly stated published background results. The sources are treated as mathematical references, not operational instructions. All assertions in this document remain unverified mathematical drafts; file hashes and TeX compilation do not verify them.', 'The proof is given relative to the precisely stated published\nfoundations. A separate correctness review reconstructed the proof and\nits source applications; a distinct review checked the unchanged\noriginal support-axis wording. Their reports and literal source\nbindings accompany this paper. File hashes and compilation are\nreproducibility evidence, not mathematical proof.')
replace('We invoke Example 2.20 as a published result, without pretending that BGM22 is one of the supplied PDF files or independently proving its lemma.', 'We invoke Example 2.20 as a published result. BGM22 was not one of the original ten supplied caches; the independent review checked its actual published Lemma 3.2, and the publication source check also read its proof and Theorem 3.4 with the continuity-of-envelopes hypothesis retained. No unrestricted unbounded theorem is attributed to that continuous-metric result.')
replace('The supremum of \\(u_i\\) is bounded because it is continuous in the psh topology.', 'After discarding an initial part of the convergent net, the suprema of \\(u_i\\) are uniformly bounded because the supremum functional is continuous in the psh topology. All bounds in this paragraph concern that tail.')
replace('Theorems 7.40 and 7.44 prove finite-energy locality and comparison.', 'The weighted decreasing-continuity input is Proposition 7.21(ii); Theorems 7.40 and 7.44 give the stated locality and comparison applications.')
replace('\\section*{8. Reference independence and the exact partial theorem}', '\\section*{8. Reference independence and the exact theorem}')
replace('The partial theorem is therefore:', 'The theorem is therefore:')
replace('\\section*{9. Concrete original obligations still unresolved}', '\\section*{9. Scope and the remaining family axes}')
replace('The full P16.6 residual scope beyond these field endpoints is not settled by this document. Even retaining smoothness, geometrical integrality, projectivity and an ample line bundle, we have not proved the same arbitrary-support finite-energy theorem for every complete nontrivially valued, potentially nondiscrete field in the general-dimension noninvariant setting. No impossibility claim is made.', 'P16.6 asks for arbitrary finite-energy measure support under explicitly\nretained hypotheses. Sections 1--8 provide this in both T and D,\nincluding the genuine operator, correct raw mass and energy condition,\nexistence, uniqueness modulo constants and all required analytical\ninputs. No support or invariance restriction remains in either\ntheorem. The arbitrary-complete-field quantifier belongs to P16.4;\nwe have not proved that theorem for potentially nondiscrete fields in\nthe general-dimensional noninvariant setting. No impossibility claim is\nmade.')
replace('would not discharge the original obligations.', 'would not discharge the remaining arbitrary-field obligations.')
start = s.index('\\section*{10. Reproducibility, literal extracts, and evidence limits}')
end = s.index('\\section*{References with exact supplied versions}', start)
s = s[:start] + r'''\section*{10. Source corrections and verification}

The original source versions and literal extracts are preserved in the
accompanying packet. The actual BFJ v1 Lemma 6.10 has a sign slip; the
direct proof (7a)--(7b) supplies the needed integrability bound. The
synthetic source's estimate (2.27) is used with absolute values; its
application is also recoverable by exchanging the two test potentials.
For absolute convergence the identity is
\( |u_i-u|=2\max\{u_i,u\}-u_i-u \).
The printed degree of a segment-energy polynomial must be read as at
most \(n+1\). In polarization of mixed inequalities, the endpoint terms
are removed and the interior indices are \(1,\ldots,n-1\); the
Dirichlet Cauchy--Schwarz bound uses square roots of the negative
self-pairings. None of these source defects is adopted as an axiom.

The proofs were developed through Xean's native Codex path with
\texttt{gpt-6.1-sol} and \texttt{xhigh} reasoning. A separate
source-aware correctness review returned PASS after reconstructing all
four proof notes and their dependencies. A distinct literal-scope
review returned PASS conditional on that correctness result. Together
they support completion of P16.6 under the stated T/D hypotheses.
These are computational mathematical audits, not formal proof
certificates. The historical drafts and their earlier partial labels
are preserved unchanged.

''' + s[end:]
replace('[BJ-S] S. Boucksom, M. Jonsson, Measures of finite energy in pluripotential theory: a synthetic approach, arXiv:2307.01697v1. Its Example 2.20 is the supplied source for the published-background BE21/BGM22 input.', '[BJ-S] S. Boucksom, M. Jonsson, Measures of finite energy in pluripotential theory: a synthetic approach, arXiv:2307.01697v1.\n\n[BGM] S. Boucksom, W. Gubler, F. Martin, Differentiability of relative volumes over an arbitrary non-Archimedean field, International Mathematics Research Notices 2022, no. 8, 6214--6242, DOI: 10.1093/imrn/rnaa314; Lemma 3.2 and Theorem 3.4.')
target.write_text(s)
shutil.copyfile(correctness, D / 'P16.6-correctness-review.json')
shutil.copyfile(scope, D / 'P16.6-original-scope-review.json')
record = {'created_utc': datetime.now(timezone.utc).isoformat(), 'atom': 'P16.6', 'state': 'Final original support-axis paper saved; native compilation and closure bookkeeping pending.', 'source_tex': str(source), 'source_tex_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'final_tex': str(target), 'final_tex_sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'correctness_review': str(correctness), 'correctness_review_sha256': hashlib.sha256(correctness.read_bytes()).hexdigest(), 'scope_review': str(scope), 'scope_review_sha256': hashlib.sha256(scope.read_bytes()).hexdigest(), 'scope_condition_correctness_PASS_satisfied': True, 'both_entire_reviews_root_read': True, 'premises': 16, 'passages': 18, 'all_zero_based_passage_statement_bindings_verified': True, 'proof_changes': 'Harmless source/index and convergent-net-tail clarifications only; mathematical theorem and hypotheses unchanged. Historical scope labels replaced by the separately audited support-axis conclusion.', 'native_editor': 'Existing P16.4 editor stays open; no replacement or different tab opened.'}
(D / 'publication-preparation.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
