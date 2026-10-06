# Hessian operators and integral comparison: exact-source audit

Recorded 6 October 2026. Baseline: `62209e077e790b7e45608c0206ef00cb0ee8eca4`.
This checkpoint reviews Dinew--Myga--Sroka's new preprint and selected
dependencies. It changes no active TeX, bibliography, canonical problem
status, original-result verification tier, or general Siu/envelope closure.

## Decision and reading scope

The useful mechanism is the divergence-free Newton tensor **of a Hessian
field**, combined with ellipticity along the segment joining two admissible
Hessians. The literal classification statements need additional normalization
and domain qualifications, and their displayed necessity proof needs
regularity and fourth-jet corrections. Consequently the general classification
is not admitted to the book as an unqualified theorem at this checkpoint.
This is a source diagnostic, not an independently certified replacement proof.

Read complete selected text and actually displayed **44 physical pages in
22 sheets** across four exact PDFs:

| Source | Acquired copy | Actual pages read | Scope |
| --- | --- | --- | --- |
| S. Dinew, S. Myga, M. Sroka, *Hessian operators, null Lagrangians and the integral comparison principle*, `2610.06313v1`, submitted 5 October 2026, 13:30:52 UTC | 12 pages | 1--12 | Entire v1, including references and affiliations |
| P. Guan, *Curvature measures, isoperimetric type inequalities and fully nonlinear PDEs* | 42-page course-hosted lecture-note layout | 1--6 | Introduction, geometric setting and Lemma 2.1 with its proof; not the pagination of the 2014 CIME publication |
| S. Dinew, *m-subharmonic and m-plurisubharmonic functions: on two problems of Sadullaev*, AFST 31(3), 995--1009 (2022), DOI `10.5802/afst.1711` | 16 physical pages | 1--16 | Publisher cover plus the complete fifteen-page published article |
| J. M. Ball, *Differentiability properties of symmetric and isotropic functions*, Duke Math. J. 51(3), 699--728 (1984), DOI `10.1215/S0012-7094-84-05134-2` | Author-hosted 29-image scan | 1--10, printed 699--708 | Introduction, extension lemma, invariant-coordinate theorem statements and beginning of their proof; nineteen remaining images unread |

Ball's scanned text was read as OCR checked against the controlling images.
No full Ball-proof reading is claimed. Guan's course-note Lemma 2.1 is
identified within the acquired layout; no claim of byte identity with the
published CIME chapter is made. The acquisition record for each PDF remains
distinct from its completed reading record.

PDF SHA-256 pins:

- Dinew--Myga--Sroka v1: `5de7d515cf10b0f90df267eb3d9c129708e72cd6d77604e286f140ec9ef61790`.
- Guan course notes: `d3ae902b1cb864aa809c98d74dabfbda53e2fbf8b5f606355c6a8a8a91f8adbc`.
- Dinew published 2022: `de792b48f65e920a4b8dd349716b839b73eeee966101ffa5afe41d7ef27926d4`.
- Ball author-hosted scan: `2b9655bf2f374a3ac7e2372b0e5eea77550a1e4a12fa552b7d93ae7c2533acae`.

Acquisition URLs are the versioned
[`2610.06313v1` PDF](https://arxiv.org/pdf/2610.06313v1),
[Guan course notes](https://math.jhu.edu/~js/Math742/pguan.curvature.measures.notes.pdf),
[Dinew's published PDF](https://www.numdam.org/item/AFST_2022_6_31_3_995_0.pdf),
and [Ball's author copy](https://people.maths.ox.ac.uk/ball/Papers/Ball%20Duke%20Mathe%20Journal%201984.pdf).
The first author-publications lookup failed because a title crossed an HTML
line break; it produced no acquired Ball PDF. A subsequent normalized lookup
located the public author-hosted link and downloaded the scan successfully.

## What the new preprint actually considers

Definition 1.1, physical 2, asks for the **unweighted Lebesgue integral**
comparison

`integral_{u<v} F(D^2 v) <= integral_{u<v} F(D^2 u)`

for every admissible smooth pair with relatively compact comparison set.
The operator is a constant-coefficient spectral function of a real symmetric
or complex Hermitian Hessian. Definition 2.1 and the surrounding discussion,
physical 5--6, use an open, connected, permutation-invariant eigenvalue domain;
convexity and being a cone are separate properties. No maximality of the
ellipticity domain is required there. Definition 2.7, physical 7, uses the
linearization for ellipticity, while Definition 2.8's positive-matrix
monotonicity needs an additional domain-stability assumption.

The definition of weak admissibility by decreasing smooth approximants,
physical 6, is not a construction of a nonlinear measure on those limits.
Smooth integral comparison alone supplies neither approximation independence
nor monotone continuity, local mass bounds, capacities or a nonpluripolar
extension. Spatially varying coefficients, curved Hermitian backgrounds and
non-Archimedean envelopes are outside this classification's stated setting.

## Sufficiency: the applicable Newton identity

Proposition 3.1, physical 7, says that the Newton tensor is divergence free
for *any* smooth symmetric matrix-valued field. Guan's actual Lemma 2.1,
course-note physical 5--6, instead assumes a **Codazzi tensor**. In Euclidean
space the Hessian of a smooth function has precisely the required symmetry
of third derivatives. An arbitrary matrix field does not.

For example, in dimension two take `A(x)=diag(1,x_1)`. The derivative of
`sigma_2` is `T_1(A)=diag(x_1,1)`, whose first row has divergence one.
This elementary check contradicts the arbitrary-field wording. It does
not contradict the Hessian version used in the subsequent sufficiency proof.

For `F=c_0+sum_{k=1}^n c_k sigma_k`, set
`w_t=t u+(1-t)v`. Every `D^2 w_t` is a Hessian field. Provided the whole
segment is admissible and the linearization of F there is positive
semidefinite, integration by parts turns the difference of the two integrals
into the boundary flux in (3.2), physical 8. On a regular comparison boundary,
the outward normal derivative of `u-v` is nonnegative, giving the required
sign. Convexity of the spectral matrix domain provides the segment condition.
Remark 3.2, physical 9, explicitly retains the segment condition when the
domain itself is not convex. Individual coefficient signs need not be positive
if ellipticity holds on the chosen branch.

The introduction's direct use of Sard's theorem for arbitrary C2 differences
requires care in dimension at least three. A smooth-pair presentation avoids
this issue; a C2 statement needs its approximation/regular-level reduction
written explicitly. No such missing reduction is certified by this audit.

## Necessity: affine normalization, regularity and jets

Theorem 1.2 and Corollary 1.3, physical 3, print a sum starting at `k=1`.
There is no normalization eliminating constants in the definitions. Adding
`c_0` to an operator changes both integrals on the same comparison set by
`c_0` times its volume, and changes no linearization. Thus `trace(A)+1`
on the positive definite cone is an immediate literal obstruction to the
zero-constant formula. Restricting to `A=t I` shows it cannot equal a
polynomial in elementary symmetric functions with no constant term on an
open interval. The proof itself ends by saying that its invariant-coordinate
function is **affine**, physical 9, which allows this constant.

Proposition 1.4, physical 3, additionally asserts `Gamma=Gamma_k` for the
homogeneous case. The stated hypotheses do not require a maximal branch.
For `F=trace(A)` in dimension two, comparison remains valid after restricting
admissibility to the positive definite cone `Gamma_2`; this proper cone is
not `Gamma_1={trace>0}`. The vector `(-1,2)` belongs only to the latter.
Consequently branch equality needs a maximality or other selection condition.
This does not refute the homogeneous operator formula on an appropriate branch.

The compact nonnegative perturbation in (3.3)--(3.6), physical 8, gives the
necessary distributional sign

`sum_{i,j} partial_i partial_j F^{ij}(D^2 u) <= 0`.

Its subsequent pointwise expansion (3.7) differentiates the invariant
function three times and the test potential four times. Yet Remark 2.9,
physical 7, only declares F differentiable. Ball's Theorem 3.2 and Corollary
3.3, printed 705, distinguish finite differentiability, with derivative loss
at multiple eigenvalues, from the smooth case. They do not turn an arbitrary
differentiable operator into a three-times differentiable invariant function.
Away from repeated eigenvalues the invariant-coordinate map has a smooth
local inverse, as discussed on printed 706. That fact still preserves the
given differentiability; it does not create missing derivatives. A classical
jet proof must state sufficient regularity, or provide a separate weak
argument. Neither a C1 classification proof nor an independent repair receipt
is supplied here.

There are two further numerical points in (3.8)--(3.10), physical 8--9:

1. The real quadratic `x^T D x` has Hessian `2D`, rather than `D`.
   Use `x^T D x/2` when prescribing D. On a domain not stable under scaling,
   this factor also affects admissibility.
2. For the real quartic
   `epsilon/2 * (sum_i a_i x_i^2/2)^2`, the diagonal fourth jet is
   `3 epsilon a_i^2`, while the off-diagonal jet is `epsilon a_i a_j`.
   The printed contraction in (3.9) has diagonal ratio two. The actual
   contraction of a symmetric coefficient matrix C is proportional to
   `a^T C a + 2 sum_i C_ii a_i^2`. Varying all real a and both signs of
   epsilon can still force C=0, but the coefficient comparison must be
   performed; merely deleting the diagonal term does not justify (3.10).

The complex quartic in Remark 3.3 has a different calculation:
`partial_i^2 partial_bar_i^2` gives `epsilon a_i^2/2` and the mixed
`partial_i partial_bar_i partial_j partial_bar_j` jet gives
`epsilon a_i a_j/4`. Its diagonal ratio is two. The real numerical correction
must not be copied into the complex calculation.

Lemma 3.4's simple-spectrum invariant Jacobian, physical 9--10, has the
expected Vandermonde invertibility. Exact dimension-two and dimension-three
symbolic checks agree. These finite checks do not certify the global C1
argument, nor its extension through the repeated-spectrum locus.

## Examples and branch selection

The set written `{M_p>0}` in (2.3), physical 5--6, is not in general the
intended convex positive-sum branch: for n=2, p=1 it includes both `(1,1)`
and `(-1,-1)` but not their midpoint. The intended admissibility condition
requires every p-eigenvalue sum to be positive. Whole product positivity
must not be used to define that branch.

Example 4.1, physical 10, treats the complex dimension-four operator
`sigma_3-sigma_1`. Its positive elliptic component containing `(1,1,1,1)`
is described by the intersection, over j, of

`sum_{i!=j} lambda_i > sqrt(2+sum_{i!=j} lambda_i^2)`.

These inequalities define convex sets, so the selected component has the
segment property needed by the Newton-flux sufficiency argument. This
establishes a smooth comparison input on that branch, rather than a completed
weak potential theory or a theorem on every elliptic component.

Example 4.2, physical 10, uses `sigma_3-sigma_1` in real dimension three
on two disconnected elliptic components. With epsilon=1/10, the quadratic
pair has values `F(D^2u)=-1969/1000`, `F(D^2v)=1969/1000`, and strictly
positive linearization eigenvalue `21/100`. Its compact comparison set is
a ball of squared radius `10/11`; integral comparison fails. Both functions
are on different components, so this does not contradict the connected
convex-branch sufficiency.

Example 4.3, physical 11, gives `sigma_3+sigma_1` with ellipticity conditions
`lambda_i lambda_j>-1`. Its locus is star shaped but not convex. For instance,
`(-4,-4,-2)` and `(0,0,4)` satisfy those inequalities, while their midpoint
`(-2,-2,1)` has a pair product -2. Examples 4.2 and 4.3 both occur in this
exact v1; there is no missing-example cross-reference diagnostic.

For a Hessian quotient, rewriting a **fixed equation** as
`sigma_n-c sigma_(n-k)=0` changes the operator being integrated. A comparison
principle for that polynomial on a selected branch does not automatically
give the same unweighted integral principle for the raw quotient. Neither
statement by itself constructs a weak quotient measure.

## The independently published product-operator obstruction

Dinew 2022 defines p-plurisubharmonicity by positivity of the sum of the
p smallest complex Hessian eigenvalues, printed 996. This is distinct from
the standard m-subharmonic Gårding conditions. Its product operator is

`M_m=product_{|I|=m}(sum_{i in I} lambda_i)`.

Theorem 4.1, printed 1004--1008, says that universal integral comparison
for `M_m^alpha`, alpha>0, requires alpha=1 and m=1 or n. Claim 4.3, printed
1005--1006, sends large positive diagonal entries to infinity and uses a
boundary-flat negative perturbation to obtain alpha>=1. Claim 4.4, printed
1006--1007, compares an explicit radial family to its quadratic limit to
obtain `alpha<=1/binomial(n-1,m-1)`. Bernoulli's strict inequality gives
the contradiction in the intermediate cases. The endpoints are complex
Monge--Ampère and Laplacian comparison. The full proof was read in the
published edition; it need not rely on the new preprint's incomplete
classification statement.

The published article has narrow literal typos worth avoiding: its displayed
definition of comparison, printed 1004, repeats v on both sides; the intended
inequality is determined by Question 1.2 and the following proof. On printed
1000 the range of symmetric invariants is written `1,...,m`, although the
same paragraph's n=3,m=2 identity is `M_2=sigma_1 sigma_2-sigma_3`.
Use all n elementary invariants in that general algebraic assertion.
The unrelated A/B-classification theorem and its proof were read as part of
the whole article but are not selected for book integration here.

Remark 4.5's radial-only comparison exponent has a different scope from
universal comparison. Failure of this particular unweighted integral
principle is not a proof that all viscosity theories or every alternative
potential-theoretic construction fail. The introduction, printed 998,
explicitly leaves a viscosity approach possible.

## Verification and next integration boundary

`literal_diagnostics_v1_20261006.json` contains twelve elementary exact
formula/scope checks, including symbolic quadratic and quartic jets,
Newton divergence, invariant Jacobians and the printed examples. These
are source diagnostics, not an original theorem or an independent model
review. No gpt-6.1-sol xhigh receipt is claimed.

The accompanying manifest pins the four PDFs, acquisition records, all
displayed-sheet/text hashes, frozen reading records, diagnostic helper,
baseline and preservation checks. All 425 active inputs, all 108 protected
inputs, the current book and native catalogue, 88 prior frozen manifests
and 154 prior exported artifacts are preserved byte for byte. This
source-only checkpoint requires no new book build and no native editor
compilation. The current book remains the 4,432-page reference-polished
edition pinned by the preceding release.

A later expository integration can use the attributed Hessian/Codazzi
Newton identity, explicitly admissible segments, and Dinew's published
product-operator obstruction. The new general classification, uniqueness
of a maximal branch, a quotient weak measure, and non-Archimedean closure
remain separate proof obligations. In particular nothing here repairs or
bypasses the reported Boucksom--Jonsson 2022 Theorem 6.21 Siu proof gap.
