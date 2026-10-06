# Hessian regularization and quantitative Hölder continuity: current source review

**Source-only checkpoint.** The baseline is
`cf74c7118d64868a5bd96fe75c48140fbbc55b16`, following the completed
bounded-background and continuity readings. The checked book remains
the 4,394-page continuous-Hessian edition. This review reads Xu's current
regularization preprint in full, checks selected smooth-solvability
dependencies and records six elementary diagnostics. It does not admit
the complete bounded Hermitian regularity chain, certify a repaired
external proof or change active TeX or canonical problem statuses.

## Exact versions and actual reading

Yulun Xu, *Regularization and Hölder continuity for complex Hessian
equations on Hermitian manifolds*,
[arXiv:2608.15552v3](https://arxiv.org/abs/2608.15552v3), was revised
24 August 2026 at 21:30:21 UTC. Its acquired PDF has **42 actual pages**,
526,369 bytes and SHA-256
`63531e7df3c8cfb32ee28dfb9217c525dc97e8cae84de09b8932fe36c64712f4`.
All 42 pages, including proofs, references and author end matter, were
individually displayed in 21 sheets and their full extracted text read.
The arXiv metadata says forty pages; that count is not substituted for
the acquired PDF's actual count. The title page separately says
26 August 2026, whereas the arXiv version margin and submission history
say 24 August. No explanation of that difference is claimed.
Text extraction reported a font-type mismatch; the individual rendered
pages were also read. The full-reading record SHA-256 is
`d3f41cfc304281edf39b8906db9b2f80c6d42b81bb79701c3275f508054a9361`;
its actual view manifest SHA-256 is
`33736539794b9521cc1fb7075b1b6dee9fc75411ff859f1a689b9dafb2144376`.

Jingrui Cheng--Yulun Xu, *Viscosity solution to complex Hessian equations
on compact Hermitian manifolds*,
[arXiv:2406.00953v2](https://arxiv.org/abs/2406.00953v2), was revised
23 January 2025 at 20:28:45 UTC. The acquired PDF has 42 actual pages,
436,472 bytes and SHA-256
`864416544df035861f63bb4100110e7c62afc926f5f7192f3555773c19681560`.
Actual **1--12 and 19**, thirteen pages, were read and individually
displayed. This includes the entire printed Section 3 smooth-solvability
argument, Lemma 2.4 and the statement of Lemma 4.10. The remaining
29 pages are unread. The JFA 289 (2025) article 110936 is Xu's cited
published reference; this checkpoint does not claim acquisition or
reading of that separate published PDF. The title page's date,
27 January 2025, is also separate from the version submission date.

Bin Guo--Duong H. Phong, *Uniform L-infinity estimates: subsolutions to
fully nonlinear partial differential equations*,
[arXiv:2401.11572v1](https://arxiv.org/abs/2401.11572v1), was submitted
21 January 2024 at 19:32:42 UTC. All fourteen actual pages, including
references, were read and individually displayed. Its PDF has
220,579 bytes and SHA-256
`607166fa6cb090a6d4e53d9288e11a4455ce206e8b39e3c4eb393cd11f23429c`.
The dependency reading record SHA-256 is
`be4842651eff731ca1b35bb8f1405b8a87f26fac26434b4a7ab2743d8d332f39`.
It covers 27 pages in fourteen sheets, with the supplementary Cheng--Xu
page 12 counted once. Thus this checkpoint has **69 new physical pages
and 35 individually displayed sheets**, rather than three full papers.

The preceding complete published Kołodziej--Nguyen background-form
reading and selected Székelyhidi Liouville reading remain frozen. Their
previously read scope is reused, not counted as freshly reread here.
Current metadata checks confirm the acquired Xu v3 and Cheng--Xu v2
as the latest listed versions, and Guo--Phong as v1 only.

## The cone and the operator hypotheses

Xu fixes a compact connected Hermitian manifold, a smooth real form chi
strictly inside a symmetric open convex eigenvalue cone Gamma, and
Gamma_n contained in Gamma contained in Gamma_1. The spectral operator
is positive, strictly elliptic and concave, continuous with zero boundary
value. Its assumptions are distinct:

- Assumption 1.1 gives the cone and structural properties.
- Assumption 1.2 is degree-one homogeneity.
- Assumption 1.3 is a **uniform lower bound for the determinant of the
  spectral linearization throughout the admissible cone**.

The main continuous-viscosity Hölder theorem uses 1.1 and 1.3; its
original operator need not be homogeneous. The obstacle penalty estimate
uses 1.1 and 1.2 for a smooth solution that is assumed to exist. Smooth
penalty existence and the canonical cone construction also use the
determinant condition. These hypotheses must not be collapsed into
one interchangeable list. The Hessian quotient operators are explicitly
excluded from the determinant condition; this proof does not give their
Lp Hölder theory.

The displayed matrix convention on actual 2 is
`A_i^j=g^(i bar k)(chi_(j bar k)+u_(j bar k))`, with
`omega=i g_(j bar k) dz_j wedge dbar z_k`. The Chern Laplacian on actual
9 is explicitly `tr_omega(i partial bar-partial q)`. A standalone explicit
assignment of ddc was not found in this full Xu reading. Cheng--Xu v2
does explicitly assign ddc=i partial bar-partial on actual 4. A future
import must match the displayed matrix and the book's normalization;
it must not silently attribute a different ddc convention to Xu.

Definitions 3.4--3.6 must retain the canonical representative. Merely
requiring USC, L1 and distributional mixed linear inequalities does
not fix values on null sets. Canonical local subharmonicity and the
viscosity upper-test definition exclude upward point spikes. The bounded
pluripotential Hessian statement concerns that canonical class, not all
USC representatives of a distribution. A diagnostic below makes the
distinction explicit without claiming a main-theorem counterexample.

## Heat smoothing, the obstacle and the gradient estimate

Actual 9--12 use the Chern heat semigroup, whose positive kernel fixes
constants. The scalar consequence of admissibility is
`Delta_Ch u + C_chi >= 0`, with `C_chi=sup tr_omega chi`. Thus the
proposed obstacle is `h_t=H_t u+C_chi t`. The weighted Gauduchon adjoint
density supplies an invariant measure; this is appropriate for the
possibly non-self-adjoint heat operator. It gives the L1 error of order
t without replacing the fixed Hessian reference metric by a different
Gauduchon metric. Heat smoothing alone need not preserve Gamma.

The written heat proof passes from smooth to **continuous** u using
uniform `H_epsilon u -> u`. The advertised regularization theorem is
for bounded admissible u. Applying that proof in the larger class needs
the canonical pointwise heat-limit argument; uniform convergence cannot
be invoked before continuity is proved. This is a representative and
proof-domain qualification, not a counterexample in the canonical class.

Actual 12--18 solve the obstacle penalty
`f(lambda(chi+ddc u_(beta,h)))=exp(beta(u_(beta,h)-h))`. They separate
the elementary min/max u estimate, the derivative-dependent upper
bound for the density, the complex Hessian estimate and the gradient
blow-up. The second-order bound is uniform for sufficiently large beta
and has the form
`|complex Hessian u| <= C_B(1+|gradient u|^2+D_h)`, where
`D_h=1+|gradient h|^2+|real Hessian h|` and B bounds the oscillation of h.
The positive beta term and the fixed interior margin of chi replace
the C-subsolution alternative in the cited maximum-principle argument.
This does not say a general RHS-dependent Hessian estimate loses all
derivatives of its prescribed data.

The gradient proof on actual 15--17 **does use the Gamma-Liouville
theorem**: rescale at the maximal gradient, obtain bounded Lipschitz
entire Gamma-solutions with nonzero gradient, and contradict
Székelyhidi's theorem. The cited exact v3 Liouville proof was read in
the preceding dependency checkpoint. Xu's method is not the direct
gradient method advertised by the more recent Guo--Song preprint.

Actual 17--18 compare the penalty to the envelope using a strictly
admissible convex combination with a constant competitor, homogeneity
and concavity. The uniform error is bounded by a constant depending
on h times log(beta)/beta. Complex-Hessian and gradient bounds give
W2p compactness through the fixed scalar elliptic operator, and then
C1alpha convergence. The conclusion is bounded **complex Hessian**;
it is not a real C1,1 conclusion for every cone. The stronger real
Hessian estimate for Gamma_m is a separate Chu--McCleerey import.

Theorem 1.4 then proposes smooth admissible u_t with L1 error O(t),
`u_t>=u-t`, bounded sup norm and gradient O(t^(-1/2)). It does not
provide monotone regularization or a theorem for arbitrary unbounded
potentials. The paper explicitly leaves the unbounded problem for
future work.

## Canonical cone construction and determinant domination

Actual 18--22 use the trace average for Gamma_1. For a proper symmetric
cone they use the dual cone's characteristic integral
`Phi_Gamma(lambda)=integral_(Gamma*) exp(-lambda.y) dy` and
`f_Gamma=(Phi_Gamma(e)/Phi_Gamma(lambda))^(1/n)`. The cross-section
Jacobian is `r^(n-1)/sqrt(n)`; the corresponding Gamma(n)/sqrt(n)
factor cancels in the quotient. Homogeneity and log concavity give
concavity. The full-dimensional dual supplies strictly positive
coordinate derivatives. A translated dual cylinder gives boundary
blow-up of Phi and zero boundary value of f_Gamma.

The positive-cone majorization follows by bounding the integral by
the positive-orthant integral. Cheng--Xu Lemma 2.4, actual 6, contains
the entire concavity/Euler/AM--GM proof converting this majorization
to the uniform derivative-product bound. That selected proof has now
been read, so the cited conversion is no longer just an abstract-level
dependency. The resulting operator is chosen to regularize the cone;
it need not equal the original equation's operator.

## Stability, the exponent and the bounded identification step

Actual 23--31 establish one-sided stability first for a **continuous
viscosity solution with positive continuous density** and a smooth
exactly admissible competitor. The auxiliary Hermitian Monge--Ampère
equation retains its solvability scalar b_j; it is not set to zero.
The smooth density is normalized in Lkappa, kappa>1, and the proof
uses a lower bound for b_j. The smooth lower test is checked to remain
strictly in the eigenvalue cone before the supersolution inequality
is applied. The auxiliary positive endomorphism is built from omega,
not from chi. These distinctions are necessary in the non-Kähler case.

The exponential moment bound, Hölder interpolation and De Giorgi
recurrence give the exponent gamma<1/(1+n q0), for
`exp(nG) in Lp0` and `q0=p0/(p0-1)`. The heat/penalty gradient estimate
then bootstraps via `T_gamma(alpha)=4 gamma/(4 gamma+2-alpha)`.
The smaller fixed point is
`1+2 gamma-sqrt(1+4 gamma^2)`. The strict endpoint in Theorem 1.1 is
therefore the stated
`1+2/(1+n q0)-sqrt(1+4/(1+n q0)^2)`. Direct symbolic substitution
clears the fixed-point and dimensional-exponent objections.

For the normalized Hessian root
`f_k=(sigma_k/binomial(n,k))^(1/k)`, a density g in Lp0 with
**p0>n/k** gives `r0=p0 k/n>1` for exp(nG). Corollary 1.1 concerns
a **given bounded canonical pluripotential solution**, allows g>=0
and uses the strict exponent with
`D=(kp0-n)/(kp0(n+1)-n)`: `1+2D-sqrt(1+4D^2)`. It does not state
existence or uniqueness of the original Hessian equation.

Actual 33--39 avoid original-equation uniqueness. They set h=exp(-u)g,
smoothly approximate it by positive h_l, and solve
`H_(chi,k)(u_l)=exp(u_l) h_l omega^n`. A noncollapse condition on
the integral of h_l^(1/k), a Green-kernel Lq bound and Jensen's
inequality give an upper bound on sup u_l. A uniform normalized
Hölder bound then supplies compactness. A hypothetical sup u_l
tending to minus infinity yields a zero-Hessian limit; global bounded
domination rules it out. Uniform Hessian-measure continuity and
uniqueness of the **positive-exponent auxiliary equation** identify
the final limit with the given u.

The bounded global domination proof in Lemma 9.3 is a substantive
newly read source argument. It perturbs tb in a coordinate ball and
uses a sequence approaching the global infimum of a-tb, so it need
not assume that this rough difference attains its infimum. Its final
local comparison uses Lemmas 9.1--9.2. Those lemmas invoke the global
and background extensions of the published Kołodziej--Nguyen results.
The full previously read Section 9 retains the nonclosed remainder
chi-ddc rho and states transfer of local results; its separate local
background Dirichlet proof is omitted. Xu's Lemma 9.2 switches between
m-omega-subharmonic language and H_(chi,m). The exact canonical
background class and comparison transfer remain explicit inputs here.

## What the smooth and L-infinity references actually say

Cheng--Xu Section 3 uses a continuity path. Its linearization has a
strictly negative zeroth-order coefficient for an increasing RHS.
The openness argument uses a Gauduchon factor for the linearized
metric, Fredholm/elliptic estimates and the maximum principle. Its
closedness invokes the cited C-subsolution estimate and proves
boundedness of shifted positive-cone level sets using determinant
majorization. The general printed Theorem 3.1(1) states only G_u>0,
whereas the proof on actual 12 also uses an endpoint barrier. Strict
increase alone is insufficient; both endpoint controls hold for
the affine positive-exponent auxiliary functions actually used by Xu.
This restricted applicability does not certify every step of the
published smooth-existence argument, whose exact PDF was not read.
The printed Theorem 3.2 says convex where its cited elliptic estimate
requires concavity; the standing f and the earlier source are concave.

Guo--Phong's Hermitian Theorem 3.1, actual 8--11, concerns **C2
solutions** with a quantitative (delta,R)-C-subsolution and fixed
two-sided form bounds. Its constants depend on delta and R. It is
not directly a radius-free estimate in terms of an Lp density norm,
or a theorem for all bounded pluripotential solutions. Xu's citations
to it in (124) and at the beginning of Corollary 1.1 need an additional
uniform-radius argument or the appropriate determinant-based
Lp estimate and a weak-solution extension. The normalized Hölder
compactness of u_l also needs uniform oscillation. The simple
level-vector check below shows why an Lp bound by itself cannot
remove R from this particular cited theorem. This is a citation/input
gap, not a counterexample to the Hölder conclusion.

Further primary inputs still not freshly read in this checkpoint
include Porper--Eidel'man heat-kernel derivative estimates, the exact
Kołodziej--Nguyen Hermitian Monge--Ampère lower-normalizer lemma,
the published Cheng--Xu article, and the determinant-based Lp estimate
appropriate to the weak class. Lemma 4.10's exponential-integrability
statement was read; its cited original proof was not newly read.

## Six literal diagnostics and one cleared objection

The frozen diagnostic record SHA-256 is
`074ba1fca06279b059f0cb2aef32c027ba41fabd790792d723f7f5040122d0ea`.

1. **Representative:** an upward point spike on a compact two-torus
   satisfies the literal distributional mixed inequalities but fails
   canonical/viscosity admissibility and the claimed pointwise heat
   majorization. This demonstrates the need to fix the representative.
2. **Penalty extreme:** on a flat one-torus take u=cos(x), beta=2 and
   `h=u-(1/2)log(1-(1/4)cos(x))`. The smooth penalty equation holds,
   but at the maximum of u-h the operator is 5/4, whereas f(chi)=1.
   The proof's comparison removes the Hessian of h incorrectly. The
   stated bounds on extrema of u have their separate direct argument.
3. **General smooth existence:** `G(u)=arctan(u)` is strictly increasing.
   With the determinant root and chi=10 omega, a minimum contradicts
   the equation; with chi=omega/10, a maximum does. The literal
   general Cheng--Xu statement lacks endpoint range conditions. Xu's
   affine positive-exponent auxiliary equations have those conditions.
4. **Test direction:** the printed Cheng--Xu supersolution definition
   says touching from above. Even the smooth constant solution fails
   that wording under a positive quadratic upper test. Supersolutions
   need lower tests, as Xu's actual stability argument correctly uses.
5. **Radius:** for the trace cone and chi=omega, the admissible level
   vector exp(G) times the all-ones vector forces
   `R>=sqrt(n) exp(G)` at a density peak. Normalized densities in complex
   dimension two have uniformly bounded L2 norm while these peaks
   diverge. The diagnostic constructs no Hessian solution and does
   not refute the determinant-based Lp theory.
6. **Intermediate beta:** the first gradient differentiation on Xu's
   actual 14 drops beta from one negative product. Beta=4, u_p=1/2
   and h_p=1 make the printed intermediate lower bound false. The
   final bound on the same display restores beta through beta K;
   the subsequent estimate uses that weighted expression.

The fixed-point and p0*k/n substitution agree exactly. No incorrect
Hölder exponent or missing dimensional normalization is asserted.
These are literal definition/formula/input checks. They do not
constitute a counterexample to Xu's main regularity theorem, an
independently verified complete proof repair or a new book theorem.

## Preservation and next work

All 425 active inputs, 108 protected inputs, 65 prior frozen manifests
(55 integrations and ten separate source reviews), 121 prior exports,
the checked 4,394-page book, every generated book file, the complete
42-atom canonical statuses and the native catalogue retain their bytes.
The current open editor is unchanged. No unchanged-book rebuild,
fresh final-book PDF review, native compilation, original admission,
independent model call or verifier receipt is claimed.

Continue with the [Guo--Song direct gradient preprint](https://arxiv.org/abs/2609.39726v1),
whose metadata advertises a stability/comparison argument avoiding the
Liouville blow-up. Its proof is not yet read. Also check the appropriate
determinant-based weak Lp bound and the exact background local comparison
before promoting arbitrary bounded Hermitian regularity. None of these
complex estimates resolves the general non-Archimedean Siu/closure
problem or changes the book's qualified treatment of BJ22 Theorem 6.21.
