# Metric entropy of Kähler potentials: primary-source review

Date: 8 October 2026. Scope: a source checkpoint for a proposed complex
reference-sheet increment. At this checkpoint the increment is in an isolated
cloud preview, not the active book or a GitHub commit. No canonical research
verdict changes, original-result promotion, or independent model receipt is
claimed.

Tomoyuki Hisamoto, *Metric entropy of Kähler potentials*,
[arXiv:2609.29002v1](https://arxiv.org/abs/2609.29002v1), submitted
24 September 2026, is the controlling primary source. Its 49-page PDF was
read in full, with complete selected text and 25 individually displayed
matching images. Eight primary dependencies were read in selected portions.
The combined actual records contain 177 distinct source-file/page pairs and
90 displayed images. Preparation, metadata searches, repeated views, and
the acquired but unexamined source tarball receive no additional reading
credit. The separate manifest pins the controlling PDF bytes and the actual
selected pages; the accompanying notes preserve the chronological readings.

## Imports and hypotheses

Hisamoto's Theorem 1.1 estimates the logarithmic covering number of smooth
supremum-zero Kähler potentials, and their normalized psh closure, in the
background probability-volume L1 metric. The small-radius exponent is the
complex dimension n. The manifold is compact and connected, n is positive,
and no polarization is needed for this theorem. The Green-potential argument
uses degree-two moment cancellation, including the real two-dimensional
logarithmic kernel, and a multiscale radius allocation. The lower bound uses
disjoint smooth bumps and a constant-weight separated code.

Theorem 1.2 uses the probability Monge–Ampère measure, ordinary relative
entropy bounded by B, and the probability-normalized finite-energy d1
metric. Its upper bound is C(1+B)^(n+1) epsilon^(-n), for
0 < epsilon < 1/2, and requires a positive Hermitian polarization. Its
lower bound requires only the compact Kähler geometry, B > 0, and the
source's small-radius cutoff proportional to min(1,sqrt(B)); the coefficient
is c min(1,B^(n/2)). The same estimates apply to the smooth class and the
finite-energy class with internal centers, after harmless geometric constant
changes. The fixed-budget closure uses heat smoothing of densities,
entropy contraction, strong compactness and normalized solution uniqueness.
Energy-bounded weak compactness alone is insufficient. At B = 0 the
supremum-normalized class is the singleton zero potential.

Theorem 1.3 retains the polarized toric setting and changes the constant
normalization to zero mean of the symplectic potential over probability
Lebesgue measure on the moment polytope. Its upper exponent is n/2; its
lower cutoff and coefficient retain min(1,sqrt(B)). The gradient transport
identity, common Haar conditionals and probability normalization identify
the relevant relative entropies. Interior finiteness and L1 integrability
permit infinite boundary values. The convex approximation used for covering
and recentering does not assert preservation of the entropy budget at each
intermediate convex approximation.

For each fixed positive budget, the small-radius exponents are sharp. The
displayed dependence on B is not asserted optimal. Covering entropy is the
natural logarithm of the internal open-ball covering number; it is distinct
from relative entropy. Ordinary relative entropy is twice H_omega in the
book's Chapter 68 convention.

## Quantization and information estimates

The upper-rate proof uses degree m = k + ell sections and an exponential
weight exp(-k u) against the fixed reference probability volume. The fixed
twist satisfies ell omega + Ric(nu) >= omega. This is not the same operator
as the qualitative fixed-input Hilbert–Fubini–Study convergence theorem in
Darvas–Lu–Rubinstein. Full mass, zero Lelong numbers and fixed-degree
exponential integrability justify the Hilbert form for finite-energy inputs.
Product positivity and the adjoint direct-image hypothesis are retained.

Energy comparisons alone do not control distance for an unordered pair.
The source additionally uses the maximum potential, entropy duality and
the two-endpoint d1 comparison. The unshifted auxiliary Bergman potential
has a uniform error C(1+B)/k on the entropy sublevel.

The reduction to n+1 Gaussian sections controls the absolute error at both
endpoint measures. At the random endpoint, the Gamma(n+1) density and the
Monge–Ampère Jacobian cancel to exp(-t); integrability of |log(t)| against
that density is the necessary endpoint estimate. An expected-current
identity is not a substitute. Generic random outputs are smooth and
semipositive, without a claim that their entropy stays below the input B.

Fixed-probability balanced forms give determinantal sampling with the
prescribed Monge–Ampère marginals. The normalizer N!/N^N and integer-rounded
joint observations are essential in the localized KL estimate. The testing
bound on strict packings, dyadic refinement, and internal recentering
produce the final entropy bound. The exact finite determinant fixtures
check normalization and marginals; they do not independently certify the
general identity, whose proof is the source's orthogonality expansion.

Finite-dictionary statements count bits for the dictionary index. They do
not bound coefficient storage, dictionary construction or nearest-entry
search. Common-degree smooth Fubini–Study dictionaries may have centers
outside the input entropy sublevel. Supremum-normalizing this particular
auxiliary Bergman operator costs an additional log(k)/k term: the source's
projective-line flat-region example and strictly positive approximants with
a uniform entropy budget prevent dropping that cost uniformly. This is
not an obstruction to all other dictionary constructions.

## Dependency conventions and corrections

- Darvas, arXiv:1409.2072v2, and the survey arXiv:1902.01982v2, supply the
  finite-energy metric and strong topology. The survey's Finsler definition
  already divides by volume. Later raw-integral displays do not authorize
  dividing that metric a second time. The preview uses a dimensional
  endpoint-comparison constant, with both measures consistently normalized.
- Darvas–Lu–Rubinstein, arXiv:1806.03800v1, supplies Theorem 4.1 and
  Proposition 2.12 in this edition. The selected text includes the
  fixed-input approximation proof, changed-background membership and
  product positivity. The complete distance-quantization proof is not
  independently closed: its terminal-slope Lemma 4.5 is outside the pages
  read here. The printed repeated endpoint in Theorem 4.4 is not copied.
- The author-hosted 63-page BBEGZ ahead-of-print file supplies Theorem 2.17
  and Corollary 2.19. The entropy-Orlicz density integrals are taken against
  the reference measure, correcting two displayed measure choices. The
  printed Pinsker coefficient does not match the full total-variation norm;
  the two-point fixture detects that numerical discrepancy. Neither issue
  replaces the strong entropy-sublevel compactness theorem.
- BBGZ, arXiv:0907.4490v1, is the controlling 54-page regenerated file.
  Its dd^c and half-weight conventions are converted, and its Section 2
  volume is one. Proposition 6.2's energy pushforward requires 1/(n+1),
  as a constant family shows; the vanishing-product affineness remains
  valid. Its general unbounded Bedford–Taylor product-limit sentence is
  excluded. In the fixed-probability case of Lemma 7.4 the intermediate
  Hilbert–Fubini–Study trace is N, while the normalized critical ratio and
  final fixed point are consistent. Unnormalized canonical/anticanonical
  measures require a compatible mass or scalar convention, so their
  literal exact-fixed-point equivalences are not imported.
- Coman–Guedj–Sahin–Zeriahi, arXiv:1804.03387v1, supplies Theorem 3.6,
  Corollary 3.7 and the p = 1 content of Proposition 3.9. Its real
  Monge–Ampère measure has density n! det Hess(F). The raw distance display
  omits the matching n!, and its d2 citation alone does not establish an
  all-p identity. Probability normalization and Hisamoto's separate d1
  Legendre-geodesic proof are used in the preview.
- Abreu, arXiv:math/0004122v1, supplies Theorems 2.5 and 2.8: logarithmic
  facet terms, a smooth correction and the positive smooth determinant
  factor for a smooth Delzant reference. Interior Hessian positivity alone
  does not replace these boundary conditions. Broad projectivity wording
  does not establish integrality of an arbitrary Kähler class. The source's
  2018 regenerated footer is not a version date.
- Gao–Wellner's author-hosted journal file uses Theorem 1(ii), rather than
  the arXiv numbering Theorem 1.1(ii). The fixed-polytope L1 import has
  controlling exponent r = 1 + 1/(2n) > 1 and unspecified geometric
  constants. Auxiliary boxing, bracket-radius and triangulation displays
  are not copied literally; consistent radius allocation suffices for
  the asserted fixed-polytope exponent.

Hisamoto's page 23 covariance-component indices are transposed for a row
g = z H^(-1/2). The matrix identity E(g* g) = H^(-1), and the later Gaussian
law and KL argument, use the consistent orientation. The exact Hermitian
two-by-two fixture confirms the component discrepancy; it does not reject
the main covering theorem. On page 46, the lower display (10.5) has
-n log(k) + C where its proof supplies -(n log(k) + C). The preview uses
only the weaker proof-supplied estimate. This sign discrepancy is not a
counterexample to a possible stronger estimate.

An early reading note provisionally named Guntuboyina–Sen without a source
anchor. That attribution was retracted in primary note 19 and replaced by
Gao–Wellner in note 24 after bibliography inspection. Chronological notes
are preserved; the corrected attribution controls this review.

## Boundaries of this checkpoint

The selected-source reading is not a recursive independent proof
certificate for classical inputs: Skoda integrability, point extension,
Bergman asymptotics, smooth Monge–Ampère solvability, weak-geodesic theory
and underlying real transport remain attributed. Unread pages and earlier
preparation records are identified in the manifest and are not converted
into reading credit. Thirteen exact diagnostic groups address local
algebra, constants and scaling, not new global theorems or model receipts.

The proposed increment has three unnamed numbered attributed statements
and thirteen new manual equations H.120–H.132. It does not prove entropy
convergence along degenerations, a non-Archimedean entropy slope formula,
or entropy-to-J control for all models. Numerical canonical-metric uses
still require an independently justified entropy budget, coercivity and
regularity. The general BJ22 Theorem 6.21 critical homogeneous Siu-division
and envelope input remains OPEN; the LPWZ density candidate remains
UNVERIFIED. The canonical inventory remains 42 atoms in 12 problem
environments. The native open-problem catalogue is preserved.
