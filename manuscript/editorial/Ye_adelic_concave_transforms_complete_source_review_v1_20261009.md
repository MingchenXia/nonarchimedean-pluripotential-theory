# Ye: complete concave-transform source review, 9 October 2026

All 23 physical pages of Yuxing Ye, *Concave transforms and volumes of
adelic line bundles*, arXiv:2609.23722v1, posted 20 September 2026, were
actually read in twelve ordered complete-text/matching-image views.
The internal title date is 22 September 2026. This is the pinned preprint,
not a later edition or journal proof. Acquisition/preparation are mechanical;
the twelve chained notes and receipts record actual reading separately.

## Signature and normalizations

The base is a number field K. The construction specifies a regular
K-rational point x0, a local parameter system, a local generator of L,
and the full section algebra of a geometrically big line bundle. Curve
statements mean smooth geometrically integral projective curves, positive
degree d and genus g≥1. The higher-dimensional statement adds smooth X,
ample L and a complete smooth flag ending in such a curve.

The local discrete transform F_v is minus the logarithm of the infimum
sup norm among sections with a specified lexicographic order and leading
coefficient one. Its interior limit c_v is summed with the source weights
n_v=2 at complex places and 1 otherwise. The paper explicitly uses
adelic degrees [K:Q] times the Boucksom–Chen normalization. Finite-place
absolute-value conventions must be converted together with these weights;
one cannot replace n_v alone by local-degree weights. Define c_norm=c/[K:Q]
and vol_chi,norm=vol_chi/[K:Q] when using normalized arithmetic heights.

Characteristic volume uses TOTAL signed degree (or log adelic unit-ball
volume/covolume), with denominator m^(n+1)/(n+1)!. Arithmetic volume uses
positive degree. The discrepancy is

    D_raw(L,flag)=integral_Delta c_raw − vol_chi,raw(L)/(n+1)!.

The flag-quotient degrees in F are not HN slopes. In the compatible toric
case c_norm equals the global roof and the filtered transform; equality
for arbitrary flags or metrics is not asserted. The HN transform cannot
be replaced by a sum of local monic Chebyshev transforms in a χ formula.

## Boundary and metric independence: Sections 2–3

The total discrete-sum χ identity and existence/regularity of the interior
Chebyshev limit are imported from Yuan09/Nyström14. Eventual full-lattice
saturation on compact interior bodies needs the full section series and
the rational-point lattice normalization. Fixed-size degree blocks and
controlled partial-sum rounding yield a uniform interior lower bound.
Leading-monic multiplication gives the required superadditivity exactly.
The uniform upper bound follows by powers and concavity.

The defect is the limiting negative discrete sum in a shrinking boundary
strip, equivalently its positive part. Interior dominated convergence
does not discard this strip. Changing a continuous adelic metric changes
F by O(m); the strip has vanishing normalized lattice volume. Thus D is
metric independent AT FIXED FLAG. It may change with x0/parameters.

Lemma 2.1 uses relative effectivity, bounded algebraic degree of base
points, finite bad places, and compact X(F) after placing bounded-degree
local extensions in a common finite extension. It does not use compactness
of all C_v-valued points. Product-facet rounding in Remark 3.2 needs
simplex-aware rounding or the alternative product-metric argument.

## Curve result: Sections 4–5

The paper's Theorem 1.2 identifies

    D_raw(L,x0)=[K:Q] hhat_theta(L−d x0).

Here hhat_theta is half the canonical height for the symmetric divisor
theta_x0+[-1]^*theta_x0 on the Jacobian. Consequently vanishing means
L−d x0 is torsion, or equality in Pic(C) tensor Q, rather than necessarily
an integral isomorphism L=O(d x0).

For the lower inequality, Riemann–Roch supplies exactly g+1 top
valuation leaves. Sup/L2 comparison changes their total by O(log m).
Norm comparison with the fixed-degree Picard fibre is O(m), using the
ordered zero divisor over an extension of degree at most (2g)! and
the relative-effective-divisor lemma. The determinant Picard class is
−theta_x0. Its fibre degree at mQ has quadratic leading term
−[K:Q]m²hhat(Q). A good integral model plus compactness at finitely many
bad places gives uniform O(1) comparison with a genuine Weil height.
The positive-part boundary sum then gives the lower inequality.

For the upper inequality, homogeneity and addition of x0 reduce to a
degree-one bundle mL0+x0. A uniform F bound gives an O(m) integral.
Admissible arithmetic-surface metrics, Faltings' arithmetic Riemann–Roch,
unit-ball estimates and Gromov comparison give vol_chi≥(mL0+S)^2.
The n-power limit is taken with m FIXED. Only then divide by m² and let
m grow. Arithmetic Hodge index gives −L0²/2=[K:Q]hhat(Q).

These steps have been read and their signs, rank, degree and order of
limits audited here. Yuan09, Moret–Bailly85, Faltings84, Gillet–Soulé92,
Yuan–Guo25 and Yuan–Zhang26 remain imported dependencies, without new
complete recursive reading credit. This review does not certify their
precise measure conventions by reference-list inspection alone.

## Higher dimension and product calculation: Section 6

Positive lambda_i satisfy lambda_i L|X_i−O(X_(i+1)) nef. Approximate
from above if rational coefficients are needed. A fixed large N absorbs
all rounding/canonical-bundle errors; Kodaira vanishing yields the jet
surjectivity in the weighted-simplex range. Norm losses are O(m).
The g+1 highest curve leaves give a boundary lower bound. Summing
O(m) errors over O(m^(n−1)) tuples and dividing by m^(n+1) removes them.
Uniform Weil-height comparison handles both bounded-height and growing
points, before converting the lattice sum to a quadratic-height integral.

The reported bound is [K:Q]/product(lambda_i) times the integral over
the standard simplex of hhat(u−sum(alpha_i/lambda_i)v_i). It is strictly
positive if some u or v_i is nontorsion. For a cubic flag on P², v=3u
and lambda=3; the factor is (1/3) integral_0^1(1−a)^2 da=1/9.
For C×P^(n−1) with the curve parameter last, the reported equality is
D(L)=b^(n−1)D(M)/(n−1)!. The projective monomial count and uniform
O(m) comparison explain that factorial. These are not statements for
arbitrary flags or arbitrary proper adelic curves.

## Literal precision and status

Corollary 4.3 on page 11 prints unprimed W0, whereas its use on page 12
is the primed fixed-degree Picard-fibre space. Propositions 4.1–4.2
give the intended consequence; the discrepancy is retained in note06.
The nonarchimedean instruction on page 17 to rescale to norm exactly one
can require an extension or a valuation ceiling at a nonreduced special
fibre. A bounded ceiling loss fits the lemma's +1; smooth good models
give the no-loss conclusion outside finitely many places.

No counterexample to the intended main results is claimed. The paper's
new results are currently source-reported, pending controlling dependency
and normalization checks for book integration. No original result first
proved in this book is proposed, and no independent promotion receipt is
claimed. Exact arithmetic/model calibrations are diagnostics, not a proof
of Picard-bundle or arithmetic Riemann–Roch inputs.

The active 4,685-page book and existing native catalogue/editor are
unchanged by this source audit. All 42 canonical atoms, twelve formal
problems and tiers (0,3,7,15,17) remain unchanged. BJ22 general homogeneous
Siu and the general envelope questions remain OPEN; LPWZ density remains
UNVERIFIED. Evidence upload adds no proof or reading credit. Only authored
notes, records, audits and frozen helpers are redistributed, excluding the
paper PDF, full text and rendered primary pages.
