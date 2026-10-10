# Norm rays, maximal apartments and relative-volume dependencies

9 October 2026. This is a qualified audit of selected primary pages, with
complete extracted text and nineteen individually displayed matching images.
It resolves version-specific citation interfaces needed by the preceding
Reboulet and Reboulet–Witt Nyström audits. It does not certify those papers'
main theorems recursively or change any canonical open-problem status.

## Exact sources and reading scope

| Source | Pinned edition | Selected physical pages | Scope |
| --- | --- | --- | --- |
| Finski, *Submultiplicative norms and filtrations on section rings* | PLMS 2025, DOI 10.1112/plms.70077, author copy of published PDF, 47 pages | 1–24 | Partial |
| Parreau, *Immeubles affines* | 41-page author PDF; its pagination is not identified with journal pagination | 21–26 | Partial |
| Boucksom–Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry* | Advances in Mathematics 378 (2021), 107501, 125-page published PDF | 87–94, printed 86–93 | Partial |

The current selection contains 38 distinct source/page pairs. Compared with
the explicitly pinned older records, it adds 22 Finski pages, five Parreau
pages and six BE21 pages: 33 newly selected pairs in that comparison.
Finski physical pages 1 and 15, Parreau page 26, and BE21 pages 87 and 88
overlap those records. The resulting named checkpoint unions are respectively
26/47, 28/41 and 64/125. The last count is the earlier BE21 four-checkpoint
union plus this selection, not an aggregate of every historical BE21 record.
Other older selections exist. None of the three whole PDFs is claimed read.

The final comparison corrects the sentence in frozen note 16 suggesting all
eight BE21 selected pages were new. The addendum preserves that old note
and its receipt intact. Preparation, extraction, export and upload contribute
zero reading credit. Source hashes, chronological notes and receipt hashes
are in the manifest and evidence archive.

## The controlling Finski locators

The older RWN25 citation numbers do not occur with those numbers in this
published edition. The substantive published interfaces are **Lemma 2.6**,
physical 11–12, for the filtration-envelope/Hermitian-ray comparison, and
**Corollary 3.5**, physical 20, for the finite-p graded FS isometry. This is
a statement mapping between editions, not proof that an older version's
numbers were erroneous. RWN25's Fin22 arXiv identifier 2210.03039 also differs
from the Fin22 key used in Reboulet 2508 v2; keys do not identify an edition.

The complex norm convention on published page 7 is

\[
d_p(\eta,\xi)=2\left(N^{-1}\sum_i|\lambda_i|^p\right)^{1/p},
\qquad d_\infty=2\max_i|\lambda_i|,
\]

where the relative slopes are logarithms of ordinary norm lengths. This
matches squared metric potentials, whose constant shift c multiplies
degree-k norm lengths by exp(-kc/2). A minimal norm-comparison exponent
is therefore d-infinity/2. Some subsequent printed formulas omit that
factor; equation (2.8)'s Hermitian trace version also omits the pth power
inside the trace. A rank-one logarithm 4 and p=2 gives 4 after the correct
pth power, versus 2 from the printed expression. These are calibration
diagnostics; constants used merely to prove vanishing can be enlarged.

Lemma 2.4 explicitly assumes existence of each relevant normalized pairwise
d1 distance limit. Its passage of a finite ordered-distance identity to a
graded limit cannot justify addition of arbitrary limsups. Two alternating
nonnegative terms can have limsup of their sum 1 and sum of limsups 2.
The actual published premise supplies the missing distinction in RWN25's
arbitrary-sequence discussion.

## The sum envelope is not a Hermitian norm

For a finite-dimensional complex norm eta and a filtration/trivial-valued
norm F, the sum envelope is the largest genuine norm below eta(v)F(v).
The adapted Hermitian ray H is a different construction. In a Hermitian
adapted basis the direct comparison is

\[
H(v)\le A(v)\le\sqrt{N}\,H(v).
\]

The first inequality follows because H is a norm below the product gauge;
the second follows from the coordinate decomposition and Cauchy–Schwarz.
Thus the published factor-2 distance is at most log N. Lemma 2.6's displayed
weaker lower bound H/N <= A and its upper bound A <= sqrt(N)H alone would
only give 2 log N; the stronger direct lower bound supplies the stated
estimate. For arbitrary reference norms add the base comparison error.

Exact equality is false. On C² take eta(a,b)=sqrt(|a|²+|b|²) and F=1 on
the first coordinate line, sqrt(2) elsewhere. At (1,1) the product gauge
gives upper bound 2, and the functional a+b dominated by that gauge gives
lower bound 2 for every decomposition. Hence A(1,1)=2, while the adapted
quadratic norm is sqrt(3). The analogous values at (1,-1), (2,0),(0,2)
violate the parallelogram identity for A. This supports the preceding
RWN25 correction without refuting the intended asymptotic comparison.

The published text itself says the sum envelope has monotonicity and
submultiplicativity advantages, while multiplicativity of the Hermitian
ray is unclear. Multiplying two approximate decompositions requires the
sum over all pairs of pieces, then factorization of that double sum.
One cannot omit those sums or replace the envelope by a quadratic norm.
Polynomial rank growth makes log(rank)/degree vanish; it does not make
the finite norms equal.

For the semigroup proof, an arbitrary norm need not admit a contractive
orthogonal projection. The Euclidean projection of (1,1) onto span(1,2)
has infinity norm 6/5 rather than 1. For nested filtration levels, the
low-level pieces can instead be grouped: their sum lies in the target
level, and the triangle inequality controls its cheaper weight. Flatten
finite approximate decompositions and allocate epsilon per piece. The
divisor example's sup-norm 'projection' can be understood as a minimum-norm
quotient representative and justified by a supporting functional.

## Scope of the FS isometry and its remaining dependencies

Published Corollary 3.5 assumes bounded submultiplicative graded complex
norms on the full section ring of an ample line bundle. For finite p it
compares them with their **regularized** FS metrics. For infinity it
requires continuity of both raw FS limits. Boundedness uses a genuine
metric/reference class, not an arbitrary existential graded comparator.

Theorem 1.1 controls sufficiently large multiples of one degree, then
handles finitely many residue classes; its input is a continuous positive
FS limit. The finite-p Theorem 1.3 uses a dyadic monotone subsequence and
a commonly bounded limit. It does not assert monotonicity of all normalized
degree terms. Pointwise Fekete convergence and uniform convergence remain
distinct. Degree-one generation is simplified only when all required
multiplication maps are surjective; very ampleness alone should not be
used as projective normality.

The central tensor classification, Theorem 3.1, is stated on page 18 but
proved in Sections 3.3 and 4, outside this selection. The original
Darvas–Lu–Rubinstein quantization theorem and other Finski multiplicative-
generation estimates also remain external dependencies. Reading their
statements and downstream proof paragraphs does not recursively certify
the whole classification theorem.

Proposition 3.6's rare Hermitian direction illustrates why omitting
submultiplicativity destroys finite-p FS isometry even with continuous
uniform FS limits. The printed kernel formulas need squared coordinates
and a reciprocal correction. With A=|a|² and S=|a|²+|b|² the kernels are
(k+1)S^k and 2^k A^k+(k+1)S^k; the normalized length ratio tends to
S/max(2A,S). The qualitative different continuous limit persists.
Proposition 3.8 is a separate genuinely submultiplicative infinity-endpoint
example based on truncated divisor vanishing. Its use of a BJ graded-norm
example is unrelated to the disputed Siu decomposition theorem.

The pluripotential recap's statement that the finite-energy spaces have
a vector-space structure cannot mean closure under arbitrary scaling in
the fixed omega-psh class. Its displayed intersection of all finite-p
energy spaces with the bounded class must not be imported literally.
The local depth log(t), t=-log|z|, has all finite moments against dt/t²,
since their integrals are Gamma(p+1), although the depth is unbounded.
This checkpoint does not claim a fully certified global patched example;
compact omega-psh, full-mass and energy conditions are separate inputs.

The generic-submanifold extension statements preserve the pluripolar
noncontact set and its hull. Their dichotomy needs a connected submanifold
or application to each component. Finite-p generic equivalence and the
stronger endpoint condition of empty noncontact intersection remain
different. The original analytic extension and pluripolarity proofs have
not all been read recursively here.

## Parreau: the maximal system matters

Proposition 2.17 on author page 22 constructs the unique maximal apartment
system containing a given one. It consists of segment-type-preserving
model-space isometries, equivalently inductive apartment limits that agree
with original apartments on each bounded subset. Proposition 2.18 on that
same page proves equivalence of maximality with containment of every
geodesic ray and line in an apartment.

The proof builds compatible apartments through longer points of the ray,
fixing an opposite chamber region. Their compatible restrictions exhaust
the model space; closure under these inductive limits produces an apartment
of the maximal system. It is stronger than merely finding an apartment
for each finite segment. Its converse uses a regular two-sided line whose
Weyl hull exhausts the model space.

Proposition 2.21 equates a geometric Kleiner–Leeb formulation with the Tits
formulation **with a maximal system**. Proposition 2.25's entire Euclidean
flat containment is introduced after maximality is expressly assumed.
Its Euclidean CAT(0) argument should not be transferred verbatim to a
non-strictly-convex L1 metric. The subsequent chamber-preservation results
add thickness assumptions. Corollary 2.19 retains the trivial Euclidean
factor in a nonessential building; omitting the scalar direction when
identifying a full norm space with an SL quotient is incorrect already
in rank one.

Applying these propositions to a chosen basis-norm atlas still requires
identification of that atlas with the maximal system, or a separate direct
ray containment argument. The general building proposition alone does
not prove this over every valued field. The norm-construction setup on
author page 26 only assumes a real-valued valuation and finite-dimensional
V, without imposing discreteness, completeness, spherical completeness
or nontriviality there. Precise later norm results retain their own field
conditions. No such condition is replaced by a generic CAT(0) slogan.

## BE21: what the relative-volume limit establishes

Section 9 assumes a complete valued field and geometrically reduced
projective X of dimension n. Definition 9.1 requires submultiplicativity
and d-infinity distance O(m) from the sup norms of a fixed bounded metric.
Theorem 9.5 adds **geometric integrality**, with arbitrary L. If L is not
big, rank=o(m^n) and the O(m rank) signed volume bound gives limit zero.

For big L, Lemma 9.4 permits a complete algebraically closed extension:
scalar extension preserves graded boundedness and changes total volume
by o(m^(n+1)). This uses the sup-norm extension error from Theorem 6.6
and the determinant rank-log-rank defect, rather than an exact arbitrary
sup-norm identity. Geometric integrality is preserved. A regular rational
point can then be selected, with Cohen local parameters and one-dimensional
initial-term leaves. Full lattice generation and linear valuation growth
are explicit Okounkov inputs, not automatic for every abstract semigroup.

The two negative leaf-log functions are separately superadditive. Their
difference is uniformly linearly bounded but need not itself be
superadditive. Their determinant sum is compared with the CM15 convergence
theorem. Excluded critical thresholds in that theorem do not obstruct its
mean/integral consequence under the bounded difference; they do obstruct
an assertion of closed-tail convergence at every level.

The final printed coefficient estimate takes suprema on classical
K-points of a polydisc. For a trivially valued field and radius r<1, that
disc has only the origin; f=z has classical supremum zero, not at least r.
A nontrivially valued complete extension via the already available
Lemma 9.4, or a Berkovich Gauss-polydisc formulation, supplies a repair
route. The printed proof does not explicitly make the additional
nontrivial-valuation reduction in that paragraph. This is a local proof
qualification, not a claimed counterexample to the intended theorem.

Definition 9.6 normalizes total signed determinant volume by n!/m^(n+1).
A probability spectral mean normalizes by 1/(m N_m). The conversion is
n!N_m/m^n -> vol(L). On P1,O(2), a constant slope c gives limiting BE
volume 2c and probability mean c. Existence of this signed first-moment
limit does not imply every absolute p-moment or full spectral law converges.

Theorem 9.8 covers metric volumes on geometrically reduced X via leading-
order component decomposition. Its Lemma 9.9 proof's zero-start injection
into sections of only top-dimensional components needs purity. On P1
disjoint union a point it has a one-dimensional kernel. Including all
components and bounding lower-dimensional terms, or retaining that kernel,
repairs the leading-order argument. The asymptotic statement is not
refuted by this finite-degree injection defect.

Proposition 9.11 gives cocycle, monotonicity, scaling by vol(L)c, Lipschitz
continuity and birational invariance with lower-order determinant error.
Semiample envelope invariance uses equality of section sup norms and does
not assert envelope continuity. A nonbig line bundle gives zero relative
metric volume, not a nondegenerate probability distance. The preceding
finite-flat envelope seam additionally requires coherent pullback data
(L on X for f:Y->X) and weighted fiber norms; its uniform averaging
argument is not arbitrary nonflat or infinite-cover descent.

## Integration boundary and continuation

These readings supply reliable version-specific locators, calibrated
finite-dimensional comparisons and explicit signatures for attributed
explanations. Suitable book material includes the two different ray
constructions, the factor-two bridge, strong versus finite-p topology,
maximal-atlas scope and the signed-volume/probability normalization.
Any added explanatory examples must remain distinguishable from an
independently verified original general theorem.

The current 4,661-page book, both bibliographies and the native open-problem
editor remain unchanged at this source checkpoint. The canonical 42 active
atoms and twelve formal problems retain their statuses. BJ22 critical
homogeneous Siu and general-envelope bridges remain OPEN; the warning
about Theorem 6.21's proof remains binding; LPWZ density remains UNVERIFIED.
No independent hostile-model verification receipt exists for this checkpoint.
The last complete ordered book pass remains 4 October, not these source
selections. Continue cloud-only, stage useful verified explanations with
appropriate compilation and actual changed-page review, monitor incoming
author research, and publish the authored evidence regularly. Xean remains
suspended under the user's instruction.
