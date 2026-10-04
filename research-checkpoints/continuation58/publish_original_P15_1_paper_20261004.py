"""Publish the completely audited original energy construction, preserving frozen history."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R=Path('/workspace/research')
source=R/'campaigns/round-31/P15.1-minimum-reference-finite-energy/artifacts/codex-7YBaVo/P15.1-partial.tex'
review=R/'root-checks/P15.1-round31-original-scope-actual-review.json'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='7806e70e013dc5dce55ea2add346fe37c57fd6550f9a7241ddfeae7ff1aff37e'
assert hashlib.sha256(review.read_bytes()).hexdigest()=='c9c966b3bce353171df891bb23f3861df9cfa8808082af86e010161aae430dfb'
v=json.loads(review.read_text());assert v['verdict']=='PASS'
assert len(v['premises'])==10 and len(v['passages'])==19
assert all(p['statement']==v['premises'][p['premise']] for p in v['passages'])
assert {p['premise'] for p in v['passages']}==set(range(10))
D=R/'deliverables/original-P15.1';D.mkdir(exist_ok=True)
target=D/'P15.1-paper.tex';assert not target.exists()
s=source.read_text()
def replace(old,new):
    global s
    assert s.count(old)==1,old[:100]
    s=s.replace(old,new)
replace('P15.1: minimum references on a common finite-energy domain','Path-independent unnormalized energy at zero volume') if False else None
s=s.replace('P15.1: minimum references on a common finite-energy domain','Path-independent unnormalized energy at zero volume')
replace('\\section{P15.1: minimum auxiliary references on a common genuine\nfinite-energy\ndomain}\\label{p15.1-minimum-auxiliary-references-on-a-common-genuine-finite-energy-domain}\n\nAuthoritative single-worker research draft, 4 October 2026. Status:\npartial; original atom remains open.',r'''\begin{abstract}
For every pseudoeffective zero-volume class on a smooth compact connected
K\"ahler manifold, we construct a path-independent unnormalized energy
after choosing an actual reference singularity type and its energy
origin. The actual reference current determines a degree \(d<n\).
A common relative full-mass domain and a genuine finite-energy domain
are independent of the auxiliary K\"ahler form. The energy extends from
bounded comparison type to this whole domain by finite mixed integrals
and relative truncations. We prove its cocycle, monotonicity, concavity,
decreasing continuity, gauge invariance and exact anchor transformation.
A finite-dimensional quotient of complementary cohomology powers is
the necessary and sufficient minimum auxiliary-reference datum for the
entire energy family. Constants retain positive raw mass. The bounded
perturbation limit and the stated iterated finite-energy limit recover
this construction; a concentration example rules out an unrestricted
joint moving-form limit.
\end{abstract}

\textbf{The question and the construction.} Original P15.1 asks for a
path-independent unnormalized energy with minimum necessary reference
scale and independence of its stated perturbation choices. Here its
carrier is \(X\), of complex dimension \(n\). Given
\(P=\theta+dd^c\psi\), put \(m=n-d\). The direct construction is
\[
 E_{\psi,q(\lambda^m)}(u)=\frac1{d+1}\sum_{a=0}^d
 \int_X(u-\psi)\langle T_u^aP^{d-a}\rangle\omega^m,
 \qquad \lambda=[\omega],\quad u\in\mathcal F^1_\psi.
\]
The common domain, finite integrals and minimum quotient are constructed
below. The anchor chooses the energy origin; changing it uses the proved
cocycle. The denominator in the perturbation limit is
\(\binom nd\varepsilon^m\). The leading actual reference mass term is
\(\binom nd M_d\varepsilon^m\), so the construction retains \(M_d\)
without probability normalization. Genuinely unbounded inputs are
possible, as a later example proves; they need not occur for every
reference type.''')
replace('This is an unverified mathematical draft addressing only P15.1. No prior\nreview verdict or prior note is a hypothesis. The bounded construction\nis reconstructed here because it is indispensable to the new results in\nn2 and n3; reconstruction alone is not claimed as substantive progress\non the original atom.', 'This paper addresses P15.1 with precisely retained actual singularity\ndata and approximation hypotheses. The bounded construction is\nreconstructed because it is indispensable to the common-domain and\nreference results in n2 and n3. The proof uses the explicitly stated\npublished foundations; no earlier draft or review verdict is a\nmathematical hypothesis.')
replace('required for n3. These are partial results for P15.1; the actual anchor\ntype remains fixed.', 'required for n3. The actual anchor type remains fixed, with the anchor\ntransformation subsequently proved by the cocycle.')
replace('reference criterion in proposals 1--3. The minimum is for this specified\nanchored prescribed-type energy family. It is not an independent\ngeometric classification or a claim that P15.1 is closed.', 'reference criterion for the preceding construction. The minimum is for\nthis entire anchored prescribed-type energy family. It is not an\nindependent geometric classification.')
replace('\\subsection{What is proved and what remains for the original\natom}', '\\subsection{Completion with the stated data and path hypotheses}')
replace('Proposals 1--3 are proved, with the stipulated actual-type degree and', 'The common-domain and reference statements are proved, with the stipulated actual-type degree and')
replace("original catalogue's broader choice and path requirements are not\nthereby resolved.", 'unchanged original question requires these choices to be explicit and\nall claimed paths to be justified; it does not require an intrinsic\n\\(d\\)-dimensional carrier or a minimum across every conceivable theory.')
replace('Alternative controls, restrictions or an iterated truncation\nprescription would need to be stated and proved rather than silently\nadded to the original atom. For example the already proved iterated\nprescription first takes the bounded leading limit at fixed L and then L\nto infinity; it gives (8), but is not asserted equal to every joint or\nreversed limit.', 'The finite-energy perturbation prescription used here first takes the\nproved bounded leading limit at fixed L and then lets L tend to\ninfinity. It gives (8), independently of the stated bounded\napproximations and reference presentations. No equality with every\njoint or reversed limit is asserted.')
start=s.index('Thus this is a new scoped partial theorem, not a complete solution or a')
s=s[:start]+r'''\textbf{Completion.} The construction exists for every pseudoeffective
zero-volume class after its actual reference type is selected. The
minimum quotient determines the whole finite-energy family and retains
raw mass; the direct mixed-integral definition and its cocycle establish
path independence. All claimed perturbation choices satisfy the proved
bounded leading limit or the explicitly chosen iterated truncation
prescription. The common domain, carrier, dimension, energy origin and
reference changes are stated. No uncontrolled simultaneous unbounded
limit is used to define the theory.

For a disconnected compact manifold there are finitely many components.
The same construction applies componentwise, retaining each degree,
scale, domain and origin, and the energy is their sum. Independent
componentwise inputs give the product minimum-reference criterion.

\subsection{Verification and literal source evidence}

The complete proof and literal primary-source annex accompany the
paper. The proof was developed through Xean's native Codex path with
\texttt{gpt-6.1-sol} and \texttt{xhigh} reasoning. A separate source-aware
review reconstructed n1--n4 against the unchanged original P15.1
statement and returned PASS. Its complete report, ten checked
foundations and nineteen source passages are preserved. The source
normalization, gradient half factor, cutoff nonzero locus and bounded
product-factor hypotheses are checked explicitly in n1. The historical
author and earlier scoped reviews remain unchanged.

These computational mathematical audits are not formal proof
certificates or literature-priority claims. The actual TeX compilation
and source hashes establish reproducibility, not mathematical truth.

\end{document}
'''
target.write_text(s)
shutil.copyfile(review,D/'P15.1-original-scope-review.json')
shutil.copyfile(source.parent/'source-annex.md',D/'P15.1-source-annex.md')
record={'created_utc':datetime.now(timezone.utc).isoformat(),'atom':'P15.1','state':'Final original-scope paper saved; compilation and closure bookkeeping pending.','source_tex':str(source),'source_tex_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'final_tex':str(target),'final_tex_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'review':str(review),'review_sha256':hashlib.sha256(review.read_bytes()).hexdigest(),'verdict':'PASS','entire_actual_report_premises_passages_root_read':True,'all_zero_based_exact_statement_bindings_verified':True,'source_quote_OCR_nonmatches_checked':7,'proof_changes':'n1--n4 mathematics unchanged; historical scope labels replaced by the separately audited original conclusion. Three harmless reviewer clarifications: actual coefficient versus rescaling denominator, cocycle anchor origin, and possible rather than universal unbounded inputs.','editor':'Existing P16.4 round46 editor preserved.'}
(D/'publication-preparation.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
