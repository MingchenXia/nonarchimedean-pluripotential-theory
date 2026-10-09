# Yuan: complete Chebyshev/chi-volume dependency review

All nineteen physical pages of Xinyi Yuan, *On Volumes of Arithmetic
Line Bundles II*, arXiv:0909.3680v1, were actually read in ten ordered
matching complete-text/rendered-image views. The arXiv margin and metadata
give 21 September 2009; the internal title date is November 21, 2018.
Both observations are retained. Current arXiv metadata lists only v1.
Acquisition and mechanical preparation supplied no reading credit.

## Controlling mathematical dictionary

The base is a number field; X is projective with a smooth rational point,
chosen local parameters and a local generator. L is geometrically big.
The FULL section algebra, not an arbitrary graded subseries, gives the
valuation semigroup. Lattice index one and boundedness of the geometric
Okounkov body are required in the lattice approximation. Continuous
metrics here are interpreted in the usual analytic sense, with bounded
comparison to model metrics on proper Berkovich spaces at finite places.

Yuan's convex discrete transform is F_v=inf log||s|| on a monic leaf.
Ye's concave convention is its negative. With ordinary extensions of the
standard absolute values on Q, use weights

    w_v=[K_v:Q_v]/[K:Q].

The normalized global concave transform is minus sum w_v F_v. One may
instead absorb the finite local-degree weights into finite absolute
values, and use the real/complex weights 1/2 before division by [K:Q],
provided norms and Haar scaling are changed consistently. In particular,
a complex hermitian norm contributes twice its logarithm to raw degree.

Characteristic volume uses signed TOTAL degree, or the equivalent leading
χ(unit-ball/covolume) asymptotic, with denominator m^(n+1)/(n+1)!.
Positive arithmetic volume uses positive degree. The intended normalized
concave formula is

    integral c_Ch >= vol_chi/(n+1)!,

with equality under the uniform all-leaf bound |F_m(alpha)|<=C m.
The convex version has the reverse sign. The raw version multiplies both
sides by [K:Q]. Local flag-leaf degrees are not HN slopes; equality of
integrals does not itself identify the functions pointwise.

## Reconstruction of the proof

Lemma 2.3 uses a monic coefficient on a local polydisc/Gauss norm for a
linear lower bound; boundedness of the Okounkov body gives F_v/m bounds.
Good integral models outside finitely many places give F_v>=0 in the
convex convention. For a fixed rational valuation direction, choose
monic sections over K at finitely many generators of its additive degree
semigroup. Product norms give uniform finite-place vanishing along it.
An interior rational polytope then gives local finite-place vanishing and
continuity of the global transform on compact interior sets.

The finite-generation/conductor argument for lattice saturation must
include generators of the FULL lattice, and the limiting directions
must lie in the INTERIOR of the chosen cone so that the conductor
translation is absorbed. These choices repair the terse proof of
Corollary 2.2 and Proposition 2.5. The imported LM/Khovanskii statements
are identified in the bibliography; no new complete recursive reading
of them is claimed.

In Section 2.3, unitriangular changes from a fixed monic basis to local
minimizers preserve determinant. L2 minimizers are orthogonal; finite
unit-ball minimizers allow successive ultrametric coefficient elimination.
This compares the determinant degree with the sum of monic leaf degrees.
Smooth archimedean metrics give the cited polynomial Gromov error, and
rank O(m^n) plus Stirling gives O(m^n log m). General continuous metrics
require smooth approximation/subexponential Bernstein–Markov estimates;
the leading o(m^(n+1)) comparison suffices for the corrected integral
argument. Metric approximation changes all local F and signed degrees
by at most epsilon m times rank, uniformly in valuations.

Section 2.4 compares the total signed-degree sum with Riemann sums on
compact interior bodies to prove the inequality and integrability. The
full integral equality uses uniformly bounded step functions on a common
bounded support and almost-everywhere convergence. The boundary has
Lebesgue measure zero, but a missing UNIFORM bound near it cannot be
replaced by this measure-zero observation. The all-leaf bound is metric
independent at fixed flag, since changes of metrics alter F_m/m by a
uniform constant. It is valid for the standard projective-space flag
with arbitrary compatible metrics and for any FULL finitely generated
valuation-degree semigroup. Finite generation of the section algebra
alone is a different condition.

## Literal issues retained rather than silently cited

* Pages 4–5 and 17 print n!, although the explicit χ-volume definition
  on page 5 and the discrete-sum equation on page 17 require (n+1)!.
  Ye's preprint explicitly points out this same factorial issue.
* The unrestricted product printed for the adele ring must be the
  restricted product. The quotient product used in its volume calculation
  is a measured fundamental domain, not a canonical topological product.
* Page 7's extra norm-value-group hypothesis is real. A normal model
  with a nonreduced special fibre can give fractional sup valuations;
  model metrics do not automatically satisfy that condition without
  a reduced-fibre qualification. Valuation ceilings add O(rank) errors
  at fixed bad places, harmless for the leading asymptotic.
* Page 10 chooses a K_v section while then varying v; choose a K section.
  Two rational endpoints cannot contain every real interior point in
  dimension >=2; use a rational simplex. The needed nonnegativity citation
  is (2b), not merely (1b).
* Page 12's polynomial Gromov rate requires metric regularity. Continuous
  toric potentials (1/alpha)log(1+|z|^alpha), alpha<1, give a faster
  L2 decay for x0^m and refute that literal uniform polynomial bound.
  Ye works with smooth archimedean metrics before invoking this estimate.
* Pages 13–14 omit the complex degree weight; the complex ellipsoid
  volume is det(Gram)^(-1)V(2N), not det(Gram)V(2N). Discriminant
  covolumes and unit balls need the same complex Haar normalization.
  A rank-one error bound uses N log(N+1), or excludes N=1.
* Page 15's orthogonality argument needs a perturbation with SMALLER
  norm, not greater. The finite degree comparison also retains the
  stated absolute-value/Haar convention.
* Page 17 reverses the effect of multiplying norms by exp(-a). Powers
  give a subadditive normalized limit, not monotonicity for every k.
  The comparison with c is made on the interior where c is defined.

These are version-specific reconstruction records. No refutation of the
intended leading integral theorem under its boundedness hypothesis is
claimed. Exact diagnostic examples check signs, ellipsoid Jacobians,
factorials, fractional model valuations and the continuous-metric rate;
they are not an independent verifier receipt or a new book theorem.

## Safe scope for book integration

The imported explanatory dictionary can use the corrected normalizations,
the distinction from HN filtration and the need for boundary control.
For P¹ with canonical quotient metrics and a constant global shift a,
the monic transform is F_m=ma, the concave limit is a on [0,1], signed
χ-volume is 2a and positive arithmetic volume is 2max(a,0). Cauchy/Gauss
coefficient bounds give the monic infimum; the standard rank and constant
shift asymptotics give the volumes. These are classical worked cases.

Ye's curve/Jacobian and higher-dimensional formulas remain separately
source-reported recent directions; this dependency reading does not
recursively read the Picard/Hodge/Faltings inputs. The active 4,685-page
book and native catalogue/editor have not yet been changed by this audit.
All 42 atoms, twelve formal problems and tiers (0,3,7,15,17) are preserved.
General BJ22 homogeneous Siu and envelope questions remain OPEN, LPWZ
density UNVERIFIED. Source upload supplies no additional reading credit.
