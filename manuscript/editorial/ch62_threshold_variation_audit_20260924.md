# Chapter 62: finite constraints, contact and threshold derivatives

Date: 24 September 2026.
Baseline: `f2640ef78082d949dc4c1a3831861a926d277357`.
Scope: one proposition and its consequences before the volume theorem,
and one extension of the existing two-point curve example.

These are consequences of established envelope, energy and measure inputs.
No research-frontier question is retired. No novelty, independent-agent
review or production-verifier verdict is claimed. The imported geometric
inputs retain that status.

## Thresholds and auxiliary vertices

The standing setting is a connected compact Kähler manifold of positive
dimension, a Kähler class, and finitely many distinct divisorial points
represented on a common model. Thresholds range over all of R^ell.
The existing finite-constraint lemma gives continuous finite-energy
envelopes for all of them; no sign assumption on the thresholds is needed.

Translation and monotonicity of the constraint sets prove the uniform
contraction bound for the potentials. Energy monotonicity and translation
then prove the same Lipschitz bound for their energies. Convex combinations
of the two potentials are candidates for the combined thresholds; energy
concavity gives concavity of the finite-dimensional value function.

For contact and measure support, fix one snc model containing the prescribed
points as vertices. Use the existing full-vertex obstacle construction,
but assign t_1+T(v_1)+1 at every auxiliary vertex. The divisor coefficients
are the assigned values multiplied by the central-fibre multiplicities.
Every candidate has supremum at most t_1+T(v_1), so the larger auxiliary
values do not change the candidate set. The resulting envelope lies strictly
below its obstacle at each auxiliary vertex.

After adding a constant to put the obstacle in PL_{>=1}, the imported
restricted-volume formula supports its measure on the full vertex set of
this same model. The envelope and obstacle translate together and the
measure is unchanged. Orthogonality eliminates every auxiliary vertex.
The remaining mass vector is a probability vector and satisfies
xi_i(t)(t_i-phi_t(v_i))=0. This proof does not infer that a PL envelope's
measure lies at prescribed vertices merely from its divisoriality.
It also does not confuse zero mass with a strict constraint gap.

## Continuous masses, first variation and the inverse minimum

Fixed PL nodal functions on the chosen model read off the individual
masses. The uniform contraction and the cited uniform-to-weak continuity
of Monge--Ampère show that each mass is continuous in the thresholds.
Testing a fixed continuous function is essential: weak convergence of
arbitrary measures alone would not imply convergence of a singleton mass.
Here all measures lie on the same fixed finite set.

The auxiliary obstacle depends affinely on the thresholds. In a direction
a, its variation has vertex values a_i at prescribed points and a_1 at
auxiliary points. Both the obstacle and direction are continuous PL
functions. The already proved continuous-obstacle first-variation formula
applies for both signs of its real parameter. The auxiliary masses vanish,
so the derivative is sum a_i xi_i(t). Continuous partial derivatives prove
C^1 regularity on all of R^ell, including changes of contact. No derivatives
of restricted volumes or of the volume integral are taken.

The Legendre inequality gives f(t)<=g(eta)+eta.t for every probability
vector eta. The actual constraint mass vector gives equality, using contact
and the dual-energy identity. Equality for another vector makes t a
Legendre maximizer, so the preceding maximizing-set proposition identifies
its measure with MA(phi_t). Distinctness of the support points gives
uniqueness of the minimizing mass vector. Conversely, evaluating the
normalized solution for any real probability vector produces a threshold
vector with precisely that measure. Thus the gradient maps onto the closed
simplex. Translation leaves the gradient fixed; its coordinates sum to one.

The model, divisorial points and class stay fixed throughout. An empty
auxiliary vertex set causes no difficulty. For ell=1 the simplex consists
of the single mass one and the value function is affine, as the earlier
one-divisor example already states. No strict positivity of every mass,
strict concavity of a normalized slice, C^2 regularity or injectivity of
the threshold-to-mass map is asserted.

## Independent curve calculation

On the projective line with unit class, the derivative with respect to the
second normalized threshold b is one for b<=-1, (1-b)/2 for -1<=b<=1,
and zero for b>=1. Its endpoint values agree, while its one-sided slopes
jump at both endpoints. This checks C^1 regularity and the failure of C^2.
At b=1 both constraints are attained but the mass at infinity is zero;
for b>1 that constraint becomes strict and the envelope stays the same.
The restriction to t_1=0 therefore need not be strictly concave.

Exact rational-arithmetic checks used 25 pairs of thresholds: all contact
identities and dual equalities, 425 dual inequalities, 125 first-order
remainders and 625 midpoint-concavity/contraction comparisons. Potential
contraction was also checked at 13 radii on both branches, including the
constant tails. These are independent checks of the curve example, not
substitutes for the general proof.

## Primary sources and preserved scope

The [MP--Witt Nystrom version 1 PDF](https://arxiv.org/pdf/2509.09442v1)
was checked at printed/physical pp. 11--12, 17--18 and 27; all five pages
were rendered and visually inspected. Proposition 2.3.2 gives uniform-to-
weak continuity. Proposition 4.2.2 gives the vertex-supported measure after
the PL_{>=1} normalization. The proof of Theorem 1.5.1 gives orthogonality.
Lemma 7.1.5 is the source antecedent of the finite-constraint construction;
the book's explicit full-vertex values and multiplicities are retained.
The first variation is the book's direct deduction in (61.17), not an
unlocated extra source assertion. The new threshold proposition is proved
as a consequence of these inputs.

The checked PDF has 689,695 bytes and SHA-256
`54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`.
The [author's publication page](https://pietropic.github.io/publications/)
still lists this work as a preprint; the current check did not establish a
published replacement. Bibliography files and exact-version keys are unchanged.

## Two local passes and validation

The first complete statement/proof/source/notation pass produced a full
build of 3,999 pages and 19,034,305 bytes. Physical pages 3427--3433 were
rendered and inspected. The second pass checked the strict auxiliary gap,
central multiplicities, PL normalization before using the source formula,
continuity via fixed test functions, both signs of the variation and the
unique-minimizer argument. It consolidated the gradient statement, separated
scalar and vector parameters, and stated failure of strict concavity on the
actual slice t_1=0. The inverse-minimum and curve-derivative displays were kept together
with their introductions after the page review. The full build and scoped page
review were repeated.

Final full build: **3,999 pages, 19,034,201 bytes**. Physical pages
3427--3433 were rendered and inspected, covering the new proposition,
its preceding mass-variation boundary, the unchanged volume theorem, the
curve example and the following section. This is scoped visual review,
not a new whole-book audit. Both passes were built in a temporary export
of the baseline. The delivered sources and ignored PDF are the checked bytes.

- Reference/structure check: 390 TeX inputs and 11,687 unique labels;
  no missing input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved reference/citation, multiply defined label,
  rerun request, horizontal overflow or vertical overflow. Existing
  underfull and class warnings remain.
- Scoped house audit: zero errors and one reviewed MPWN25 preprint warning;
  normal audit exits 0 and strict audit exits 1 for that warning.
- Open-problem inventory: PASS, 45 active atoms in 14 environments,
  tiers (0,5,8,15,17).
- Removing only the two additions recovers the complete baseline Chapter 62.
  The factor-n verifier block, earlier mass/rational tests and full volume
  theorem/proof are unchanged. All other chapter sources are unchanged.
- Only five reviewed source/progress files are staged. The current PDF is
  ignored; frozen packets, verifier receipts and dated releases are preserved.

Final Chapter 62 SHA-256: `0f4ed122d63f88c188c4c6be00944a07af698e8372c67a9c147e004cc25edb90`.
Final PDF SHA-256: `e0e6105f2e0e8f1af9b9127f075e114a4ef38ea6d8687883dedde8a565fd25c5`.
Preserved Chapter 61 SHA-256:
`1bc2e7024230c6c32c22a855af30a152e4f4c1567ab0984eb4c8b05c2c3264fd`.
Preserved Chapter 60 SHA-256:
`0fdb5f601274ccf7df48afd5112a1bf3e452e3aff9df5a459c5c6a08e611ac93`.
Preserved P12.1 fragment SHA-256:
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The author's supplied normalized-links PDF and its archived copy retain
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`;
the supplied CURVE_PSH.tex retains
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
P12.1 integration/provenance and P12.2--P12.6 residuals are unchanged.
