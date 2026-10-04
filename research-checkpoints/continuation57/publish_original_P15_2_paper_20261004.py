"""Publish an original-scope paper without altering frozen author/reviewer evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
source = R / 'campaigns/round-32/P15.2-minimum-reference-full-mass-operator/artifacts/codex-UNkbGs/P15.2-partial.tex'
review = R / 'root-checks/P15.2-round32-original-scope-actual-review.json'
assert hashlib.sha256(source.read_bytes()).hexdigest() == 'acf53110f1e934c0012e8351a3e518c30f12096d7fe316951efe985a82d66739'
assert hashlib.sha256(review.read_bytes()).hexdigest() == '48060692b8f3896a96076463c01058d112feb048227024cff2c3aca96d4452a5'
a = json.loads(review.read_text())
assert a['verdict'] == 'PASS'
assert len(a['premises']) == 10 and len(a['passages']) == 18
assert {p['premise'] for p in a['passages']} == set(range(10))
assert all(p['statement'] == a['premises'][p['premise']] for p in a['passages'])
D = R / 'deliverables/original-P15.2'
D.mkdir(exist_ok=True)
target = D / 'P15.2-paper.tex'
assert not target.exists(), 'Preserve any already published paper.'
s = source.read_text()
def replace(old, new):
    global s
    assert s.count(old) == 1, old[:100]
    s = s.replace(old, new)

replace(r'\author{}' + '\n' + r'\date{}', r'\title{Path-independent zero-volume Monge--Amp\`ere operators' + '\n' + r'with minimum necessary reference data}' + '\n' + r'\author{}' + '\n' + r'\date{4 October 2026}')
replace('\\section{P15.2: common full-mass domain and minimum full-form operator\ndata}\\label{p15.2-common-full-mass-domain-and-minimum-full-form-operator-data}\n\nAuthor: native Codex execution in the fresh assigned workspace. Date: 4\nOctober 2026. Status: \\textbf{partial}; unverified mathematical draft.\nThe original P15.2 atom remains open. Only this atom is investigated;\nenergy integrability is used solely to specify a common operator\nsubdomain.', r'''\maketitle

\begin{abstract}
For every pseudoeffective zero-volume class on a smooth compact connected
K\"ahler manifold, we construct an unnormalized Monge--Amp\`ere operator
after retaining an actual bounded singularity type and the minimum
necessary auxiliary-form datum for its operator family. Its carrier is
the original manifold. The degree comes from the nonpluripolar masses
of the actual reference current. A common relative full-mass domain,
decreasing continuity of the bare product currents, and extension of the
bounded-family reference kernel yield a presentation-independent
operator with explicit positive raw mass. We prove joint continuity in
a quotient norm and two specified perturbation limits. A product
example computes an infinite-dimensional reference quotient and shows
why auxiliary cohomology alone does not determine this operator.
\end{abstract}

\textbf{The question and the construction.} P15.2 asks for a
path-independent zero-volume Monge--Amp\`ere theory with carrier,
dimension, mass and reference choices stated explicitly. Here the
geometric carrier is \(X\), of complex dimension \(n\). Given an actual
reference \(P=\theta+dd^c\psi\), let \(d<n\) be its highest nonzero
nonpluripolar degree and set \(m=n-d\). For every input in the common
full-mass domain \(\mathcal H_\psi\), the operator is
\[
  \operatorname{MA}_{[\psi],q_W(\omega^m)}(u)
    =\langle(\theta+dd^cu)^d\rangle\wedge\omega^m.
\]
Its reference quotient \(W/N\), raw mass, domains and continuity
conditions are defined and proved below. The operator is defined
directly; the perturbation theorems give two proved representations of
it under their stated hypotheses. No probability normalization is used.''')
replace('The new work is the scalar-deficit common-domain theorem, bare-current\nreconstruction, extension of the reference kernel to all full-mass\ninputs, quotient continuity and the explicit infinite-dimensional\ngeometric-kernel example. Published foundations are cited with\nhypotheses and checked applications. Earlier supplied author/review\nverdicts are evidence to reconstruct, not theorem grants.', 'The proofs establish the scalar-deficit common-domain theorem,\nbare-current reconstruction, extension of the reference kernel to all\nfull-mass inputs, quotient continuity and an explicit\ninfinite-dimensional kernel example. Published foundations are cited\nwith hypotheses and checked applications. The four proof sections are\nself-contained relative to those stated foundations.')
replace('\\textbf{Scope.} This is a partial P15.2 result, independently\nreconstructed from the stated literature foundations. No earlier proof\nor review verdict is an assumption. Only P15.2 is investigated. The\nenergy integrability condition below specifies a useful operator domain;\nno P15.1 energy theorem is claimed.', '\\textbf{Scope.} The retained actual singularity type and reference\nquotient are part of the operator data. The whole common relative\nfull-mass domain is its domain; the energy integrability condition below\nalso specifies a useful subdomain. The approximation hypotheses in\n(P2) and (P4) are explicit. Only P15.2 is treated here; no P15.1 energy\ntheorem is claimed.')
replace(r'Condition (\emph{)', r'Condition \((*)\)')
replace(r'Condition (})', r'Condition \((*)\)')
replace('\\section{n4. Perturbation limits, obstruction and residual\nscope}', '\\section{n4. Perturbation limits and necessary reference data}')
start = s.index("Original P15.2 remains open in the dossier's residual scope.")
end = s.index('\\end{document}', start)
s = s[:start] + r'''\textbf{Completion with the stated data.} The construction applies to
every pseudoeffective zero-volume class after an actual reference type
is selected. Its carrier \(X\), geometric dimension \(n\), current
bidegree \((d,d)\), positive unnormalized mass (Q5), common full-mass
domain and minimum sufficient reference quotient \(W/N\) are explicit.
Equality of the quotient datum is necessary and sufficient for equality
of the whole fixed-type operator family. The construction is invariant
under bounded-equivalent anchors, smooth background gauges, and every
presentation of the same quotient datum. The proved paths are (P2),
with a full-mass limit and convergent class and quotient data, and (P4),
with bounded reference type, smooth auxiliary convergence and
\(o(\varepsilon)\) potential error. These conditions form part of the
path-independent theory and are not suppressed.

This reference minimum concerns the specified operator family. It need
not be finite dimensional or depend only on cohomology. The carrier
has not been identified with an intrinsic \(d\)-dimensional space, and
\(d\) need not be the class numerical dimension. Neither unrestricted
varying-background unbounded-path convergence nor increasing-sequence
or varying-unbounded-weight continuity is asserted. Such stronger
statements are separate questions. In a disconnected compact setting,
the construction may be made on each of the finitely many components,
retaining its component degree, domain and quotient data and then adding
the measures.

\textbf{Verification record.} The proofs were developed through Xean's
native Codex path with \texttt{gpt-6.1-sol} and \texttt{xhigh} reasoning.
A separate source-aware review reconstructed all four sections against
the unchanged original P15.2 wording and returned PASS. The review,
literal primary-source annex and publication bindings accompany this
paper. This is a computational mathematical audit, not a formal proof
certificate or a literature-priority claim.

\end{document}
''' 
target.write_text(s)
shutil.copyfile(review, D / 'P15.2-original-scope-review.json')
annex = source.parent / 'source-annex.md'
shutil.copyfile(annex, D / 'P15.2-source-annex.md')
record = {'created_utc': datetime.now(timezone.utc).isoformat(), 'atom': 'P15.2', 'state': 'Final original-scope paper saved; native compilation and publication closure bookkeeping pending.', 'source_tex': str(source), 'source_tex_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'final_tex': str(target), 'final_tex_sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'review': str(review), 'review_sha256': hashlib.sha256(review.read_bytes()).hexdigest(), 'review_verdict': a['verdict'], 'root_complete_review_read': True, 'premises': 10, 'passages': 18, 'all_zero_based_passage_statement_bindings_verified': True, 'proof_changes': 'No changes to n1-n4 mathematics; historical status paragraphs replaced by the independently audited original-scope conclusion; malformed Condition (*) formatting corrected.', 'native_editor': 'Existing P16.4 editor stays open; no replacement or different tab opened.', 'source_annex_sha256': hashlib.sha256(annex.read_bytes()).hexdigest()}
(D / 'publication-preparation.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
