# Ballaÿ–Sombra: published adelic approximation and small-point equidistribution

Controlling source: François Ballaÿ and Martín Sombra, *Approximation of
adelic divisors and equidistribution of small points*, Inventiones
mathematicae, version of record published 5 October 2026,
DOI 10.1007/s00222-026-01456-y. PDF SHA256:
`6be58154779c6b26cf1ec6ccf1a3645100409f9b218994a2d42b9690f00ca5be`.
All 99 physical pages were read in 50 ordered matching text/image displays.
This is a complete reading of this paper, not a recursive proof audit of
its references, a new whole-book reading, or an independent-model receipt.
The arXiv 2407.14978v2 pagination does not control these locators.

## Category and normalization

Sections 3–9 concern normal integral projective varieties X over a number
field K, dimension d>=1. Geometric integrality is not assumed throughout;
constant-field reductions must be kept where used. At a place v the
analytic field is the completed algebraic closure C_v. The weights
n_v=[K_v:Q_v]/[K:Q] obey the product formula and sum to one over the
Archimedean places. The Green function is minus log norm, not minus log
squared norm. A continuous adelic R-divisor has one model outside finitely
many places. This space is not an unrestricted adelic or singular E1
completion. The source's equivalence symbol means R-linear equivalence.

Semipositive means locally continuous psh with geometrically nef divisor;
adelic nef also requires nonnegative absolute minimum. Geometric bigness
and arithmetic bigness are distinct. Arithmetic intersections have d+1
factors; geometric intersections have d. The Archimedean unit divisor
[infinity] has geometric divisor zero and Green function one at each
Archimedean place. The source writes Dbar(t)=Dbar-t[infinity].

For a zero-geometric-divisor test 0bar^phi at v, its point height is n_v
times the orbit average of phi. The mixed arithmetic intersection is n_v
times the integral of phi against the unnormalized local MA measure.
Its total mass is Q^d, and its probability normalization is Q^d, even when
the approximating masses tend to zero. The place weight cancels when
recovering the orbit probability measure from the derivative.

## Main projective result and proof mechanism

The geometric inradius is r(P;A)=sup{lambda:P-lambda A big}. For big P,A
it is finite and positive. Reference changes are comparable by constants
independent of P (Lemma 3.2, physical 13). For big nef P,A, Lemma 3.3
(physical 14) gives the geometric intersection estimates used to control
the radius. It is neither the volume nor an arbitrary metric distance.

Definition 6.7 and Theorem 6.9 (physical 36; proof physical 43–49) use
normal modifications phi_n and semipositive adelic Qbar_n with big Q_n
and pseudoeffective phi_n*Dbar-Qbar_n. Put mu=mu_ess(Dbar) and
delta_n=mu-mu_abs(Qbar_n). The hypothesis is

    delta_n / r(Q_n;phi_n*D) -> 0.

The target Dbar need not be semipositive. All-direction Gateaux
differentiability follows, with derivative in direction Ebar equal to

    lim_n [(Qbar_n^d.phi_n*Ebar)
           -d mu (Q_n^(d-1).phi_n*E)] / Q_n^d.

Every generic small sequence equidistributes at every place to the weak
limit of the pushed-forward normalized approximant MA measures. Generic
means eventual avoidance of every proper closed subset; small means
height tends to the essential minimum. It does not mean absolute-minimum
smallness. Countability of the algebraic closure of a number field enables
the diagonal small-sequence construction (Lemma 6.2); this is not a
countably cofinal model argument over arbitrary fields.

Arithmetic Siu and Hodge estimates lead to a quadratic error of size
kappa*lambda^2/r. Normalize Qtilde_n=Qbar_n-mu_abs(Qbar_n)[infinity] so
that Qtilde_n is adelic nef. The error after dividing by lambda is
delta_n/lambda+O(lambda/r_n). With gamma_n=delta_n/r_n when positive
and gamma_n=1/n otherwise, lambda_n=r_n sqrt(gamma_n) makes both errors
vanish. The boundedness of r_n also makes lambda_n tend to zero.
The finite-dimensional or toric elementary checks here do not recursively
verify arithmetic Hodge/Siu, Fujita approximation, or the original local
intersection construction. Arithmetic Siu in this argument is distinct
from the unresolved BJ22 homogeneous Siu decomposition.

The intrinsic sufficient condition is Theorem 6.17 (physical 40):

    liminf_(t upward to mu, t<mu) (mu-t)/rho(Dbar(t)) = 0,

where rho is the supremum of geometric inradii of adelic nef
approximants. It yields the full one-sided limit of normalized arithmetic
positive intersections, not merely the subsequence in the liminf.
The denominator is the filtered geometric volume vol(R^t(Dbar)), which
may be smaller than vol(D). A fixed finite-essential-minimum constant
shift keeps the endpoint strictly below mu when necessary.

## Toric content suitable for the book

For a split torus, the moment polytope Delta has lattice-covolume-one
measure and vol(D)=d!vol(Delta). Local roofs theta_v use the concave
Legendre transform inf_u(<u,x>-psi_v(u)); the global roof is
theta=sum_v n_v theta_v. The essential minimum is max theta, and for
semipositive metrics the absolute minimum is min theta. Zhang's normalized
intersection lower bound is the average roof. Upper-level sets
Gamma_t={theta>=t} control the inradius criterion.

Theorem 8.7 (physical 63–65) uses a wide global roof without requiring
the original local metrics to be semipositive. Theorem 8.10 (physical
67–68) gives equivalence of wideness, differentiability, and equidistribution
when the toric adelic divisor is semipositive. Proposition A.3 and
Definition A.6 (physical 93–95) say that wideness means

    (mu-t)/width(Gamma_t) -> 0,

equivalently the inradius version, equivalently zero IS a vertex of the
sup-differential at a maximum. Balanced local sup-gradients u_v satisfy
sum_v n_v u_v=0 and are unique under wideness (Proposition A.8).
The limiting measures are translated compact-torus Haar measure at
Archimedean places and the toric Gauss Dirac measure at a finite place.
The latter is not Haar measure on rigid points of a non-Archimedean unit
circle. For an arbitrary geometric test divisor the principal correction
is retained by Corollary 8.9; metric averaging alone is insufficient.

A direct worked example on P1/Q with O(1) has Archimedean roof
theta(x)=1-(x-1/2)^2 on [0,1], and canonical finite roofs zero.
This is continuous and concave and defines a semipositive toric metric
by the source's metric/roof dictionary. Essential minimum=1, absolute
minimum=3/4, roof average=11/12 and arithmetic top intersection=11/6.
Zhang's lower bound is strict. For 0<delta=1-t<1/4, Gamma_t has width
and inradius relative to [0,1] equal to 2 sqrt(delta), so
delta/r=sqrt(delta)/2 tends to zero. The unique balanced slopes are
zero; the limits are unit-circle Haar at infinity and the unit Gauss
Dirac at every finite place. These elementary computations illustrate
an imported theorem; they do not constitute a new mathematical result.

## Literal-source diagnostics and scope restrictions

The following are kept separate from the intended main theorems.
No mathematical-theorem counterexample is inferred solely from a
printing defect or an omitted intermediate justification.

1. Remark 6.8 (physical 36) prints the approximant mass as vol(D).
   It must be vol(Q). Canonical O(2) and its O(1) approximant on P1
   have masses 2 and 1; the main formulas correctly divide by Q^d.
2. Lemma 6.18 reverse direction (physical 41) can set t_n=mu exactly,
   although the intrinsic expression is defined for strict t<mu.
   Use t_n=mu_abs(Qbar_n)-epsilon_n with epsilon_n/r_n->0,
   epsilon_n>0; epsilon_n=r_n/n suffices. Preparation notes are unchanged.
3. Lemma 7.6 (physical 47–48) shifts nef Abar down to make Dbar-Abar
   arithmetically big, which can lose adelic neffness. A consistent
   explanatory normalization scales the original nef Abar by fixed
   epsilon so D-epsilon A is big, then shifts Dbar and every Qbar_n
   UP by the same fixed c[infinity]. The remainder, delta_n, all
   geometric data and Qtilde_n are unchanged, epsilon Abar stays nef,
   and Lemma 4.12 makes the target difference arithmetically big.
   No independent production verification of a new repair is claimed.
4. Lemma 4.17 (physical 24) needs finite mu_abs where a zero geometric
   cycle mass occurs; literal 0 times minus infinity is undefined.
   The asymptotic main application has finite normalized minima.
5. Corollary 6.13 (physical 39) has endpoint filtered-volume language
   stronger than the integral argument controls; strict t<mu is safe.
6. Lemma 7.5 (physical 47) has an intermediate geometric d+1-factor
   typography issue; the adjacent correct term uses Q^(d-1).E.
7. The pseudo-effectivity equivalence in Section 8.1 (physical 59)
   cannot require every local roof to dominate separately. On P1/Q,
   let Ebar be canonical O(1), Dbar=Ebar+[infinity]+principal(3).
   Dbar-Ebar is nef with constant point height one, but its infinite
   local roof is 1-log(3)<0 while the 3-adic roof is log(3).
   The product formula gives global roof one. Local roof domination
   is a sufficient comparison, not the stated necessary condition.
   The toric proof's actual use is of the sufficient comparison.
8. The domain homothety inclusion on physical 59 needs an interior
   homothety centre; the literal origin inclusion fails for [1,2].
9. Remark 8.12 (physical 68) says zero is not a vertex; Proposition
   A.3 and Theorem 8.10 require zero IS a vertex. A constant roof
   has singleton interior sup-differential {0} and equidistributes.
10. The finite set S in Section 8.3 (physical 64) must include the
    noncanonical places of Dbar as well as Ebar, all Archimedean
    places and nonzero slopes; enlarging S is harmless and necessary.
11. Proposition 9.2's alternative section proof (physical 71) writes
    real graded degrees e q^k although the section ring is integrally
    graded. The finite-pullback essential-minimum proof avoids this.
12. The canonical uniqueness description at physical 71 uses K*
    where a non-geometrically-integral variety can have a larger
    constant field. Retain the constant-field reduction.
13. Theorem 9.9 proof (physical 77) divides by restricted volume on
    a subvariety for big semiample D; that volume can be zero on an
    exceptional subvariety. A suitable zero-mass argument is needed;
    the ample specialization avoids this issue.
14. Remark 9.12 (physical 79–80) claims the stronger volume criterion
    fails for r>=2. Its displayed ratio is actually
    -mu_abs(Dbar)*ell^((r-2)n)/D^(r+g). Failure needs mu_abs(Dbar)<0.
    If that minimum is zero, the ratio is identically zero; split
    products with nonnegative canonical height provide this case.
15. Lemma 10.7 (physical 87) makes a literal representative effective
    by scaling and a constant metric shift. Negative horizontal
    coefficients persist under those operations; an effective
    linearly equivalent representative/principal correction is needed.
16. Theorem 10.11 proof (physical 89–91) ends with compactly supported
    continuous tests on noncompact U. That proves vague convergence;
    tightness/full mass must also be justified to obtain the stated
    weak probability convergence. delta_n on R is a general measure
    illustration of the distinction, not an adelic counterexample.
17. The Appendix (physical 92–95) assumes merely finite concavity but
    uses compact upper-level sets, fibre supremum attainment and
    continuity at boundary points. Upper semicontinuity/continuous
    roofs supply these properties. f(0)=0, f(x)=1 for x>0 on [0,1]
    is finite concave and has nonclosed positive upper-level sets.
    The worked quadratic roof has all requisite regularity.

Logarithmic tests also require care: Theorem 7.13 (physical 52–53)
needs equality between the directional derivative in an effective-divisor
direction and the sum of limiting local Green integrals. Mere weak
convergence plus integrability of the limit does not imply convergence
for logarithmic tests. Corollary 7.15 (physical 54) assumes eventual
equality of all approximating local measures, uniformly in the place,
as well as the normalized cycle-height gap. The model probability
sequence (1-1/n)delta_1+(1/n)delta_(exp(-n)) converges weakly to delta_1
but integrates -log(x) to one rather than zero.

## Related open directions: exact descriptions and state of knowledge

These are source research directions, not additions to the canonical
42-atom/twelve-problem register. No canonical closure or tier changes.

### Necessity of the intrinsic approximation criterion

Question 6.21 (physical 43) asks whether Gateaux differentiability of
mu_ess at a continuous adelic divisor with big geometry implies
liminf_(t upward to mu) (mu-t)/rho(Dbar(t))=0, and more optimistically
whether all-place equidistribution implies it. The target is a necessity
statement: sufficiency is Theorems 6.9 and 6.17. Proposition 7.17
(physical 55–56) proves an equivalence under the extra existence of a
semipositive dominating metric on the same divisor satisfying Zhang
equality at the same essential minimum. Theorem 8.10 gives the toric
semipositive equivalence. Neither removes the general extra hypotheses.
This Question 6.21 is unrelated to the BJ22 Theorem 6.21 warning.

### Removing stabilization from logarithmic equidistribution

Remark 7.16 (physical 54) asks whether Corollary 7.15 extends without
eventual constancy of the local normalized MA measures. Keep the
approximation and normalized effective-cycle-height gap; prove the
necessary limiting Green integral equality or uniform logarithmic-tail
control. Theorem 7.13 supplies the exact sufficient derivative equality.
Weak convergence alone is insufficient by the elementary sequence above.
The source does not resolve the unstabilized case.

### Explicit finite-place measures for general semiabelian varieties

Remark 9.11 (physical 79) suggests an explicit convex-geometric formula
for the non-Archimedean semiabelian equilibrium measure. Theorem 9.10
gives the normalized mixed canonical MA characterization; the analogous
abelian description is attributed to Gubler 2010. A 9 October metadata
search found Wei Xue, arXiv:2608.08262, *Equidistribution for semiabelian
varieties over number fields*, with an indicated v2 revision. That
candidate has not been acquired or read here. Its abstract discusses
monocritical arithmetically T-effective toric metrics; it does not by
itself settle this explicit-measure question. Current universal openness
must not be asserted before the candidate is checked.

The subsequent arithmetic-Okounkov characterization announced in Section
1.5 and the Biswas comparison suggested on physical 92 are further reading
directions, not results proved by this article.

## Integration boundary and publication

Suitable integration: a short projective arithmetic counterpart to the
variational equation, exact derivative/probability conventions, and the
quadratic roof example. Do not import the quasi-projective statement
without addressing the completion, strong-nef convention and tightness
gap, or present logarithmic convergence for arbitrary effective divisors.
No new theorem, independent-model receipt, full BJ22 repair, LPWZ density
certificate or whole-book rereading is supplied. BJ22 critical Siu and
general envelopes remain OPEN; LPWZ density remains UNVERIFIED.

The original paper states CC BY 4.0 on physical 97:
https://creativecommons.org/licenses/by/4.0/ . Original PDF bytes remain
unchanged. Authored notes, diagnostics and any book exposition are separate
adaptations with attribution. This unit uploads authored records; the
full original-PDF/text/image evidence is preserved in the cloud archive.
Every exported member is compared byte-for-byte. Export/upload adds zero
reading credit. The active 4,671-page book and the native 86-page open
catalogue/editor remain unchanged in this source-only checkpoint.
