# Big quantization and an endpoint-measure candidate — 5 October 2026

This is a research checkpoint, not an admission to the monograph. The
controlling text has been read in full. Its distance and graded-norm
results may be relevant to Chapter 68, but a single compatible graded
family is an essential hypothesis. The endpoint spectral-measure
formula is being tested separately. No open-problem atom is closed,
no original result receives theorem typography, and no independent
model receipt is asserted.

The baseline is work-branch commit
c1faa462bd469e9b638234dd08ae4a1e3cb90b1c. The book, its bibliography,
the complete inventory, the open native catalogue and the preceding
frozen exports are byte preserved. GitHub work and main were fetched
on 5 October; no author commits arrived at this checkpoint.

## Primary sources and reading scope

Siarhei Finski, *Geometric quantization on big line bundles*,
[arXiv:2512.10466v1](https://arxiv.org/abs/2512.10466v1), submitted
11 December 2025 at 09:42:39 UTC. The current metadata exposes only
version one. The PDF has 61 physical pages, including references,
and was acquired on 5 October 2026 at 14:08:45.172537 UTC, HTTP 200:
519,473 bytes, SHA-256
14098ff77b4acf6a52b4bc1f9fb0ee8fd6eff481f83a98da3332c1c9e7116c19.
All 3,363 extracted split lines were read in fifteen contiguous ranges.
Twenty-one actual pages were viewed: 2, 4–7, 18–19, 21–26,
30, 33–35, 43 and 55–57. Actual views settle the displayed formulas
below; text extraction alone did not control the conclusions.

Three dependencies were acquired and selectively read:

- Berman–Boucksom–Witt Nyström, *Fekete points and convergence towards
  equilibrium measures on complex manifolds*, Acta Math. 207 (2011),
  1–27, DOI [10.1007/s11511-011-0067-x](https://doi.org/10.1007/s11511-011-0067-x).
  The published 27-page PDF is preserved from an academic archive,
  279,873 bytes, SHA-256
  7ef4f3f8fd403e8d7351a139ff837d7da67892788cb859ff975d8e584b770856.
  Extracted lines 590–720 and actual pages 14–15 check Proposition
  1.12, Theorem 1.14 and Question 1.11.
- Finski, *Submultiplicative norms and filtrations on section rings*,
  Proc. Lond. Math. Soc. 131 (2025), e70077, DOI
  [10.1112/plms.70077](https://doi.org/10.1112/plms.70077).
  The author's linked copy is the 47-page publisher PDF, not the
  older arXiv text: 511,672 bytes, SHA-256
  1d0c7c19f3d5bf36aada5ac7f2530c9b1bafb8de0264ad1ddad84edd7260b740.
  Extracted lines 1–65, 814–861 and 2088–2189 and actual pages
  1, 15 and 35–36 check the initial regularity, factors and
  Theorem 6.4. The article records acceptance on 17 July 2025.
- The earlier [arXiv:2210.03039v3](https://arxiv.org/abs/2210.03039v3),
  revised 30 July 2024 at 00:02:49 UTC, has 44 pages,
  590,579 bytes, SHA-256
  f5979bfa791781fa706bedce12af066a3c497718aa082738e4b41c77a563172b.
  Extracted lines 1705–1785 and actual pages 31–32 check the
  smooth-positive initial restriction preceding Theorem 5.4.

There are 29 actual primary-page inspections in fifteen sheets.
The dependency PDFs were not read in full. Acquisition records,
extracted text, metadata and viewed-page records live in ignored
source caches and are byte pinned by the accompanying manifest.
No priority or exhaustive literature-search claim is made.

## What the quantization results require

The ambient category in 2512.10466v1 is a smooth complex projective
manifold with a big line bundle. Theorem 1.1 compares volume-normalized
Mabuchi distances of envelopes of continuous metrics with section
sup-norm distances divided by degree. Theorem 1.3 assumes one
submultiplicative graded norm and bounds it on both sides by section
sup-norms of fixed continuous metrics. Its finite-p conclusion is
asymptotic equivalence to the sup-norm of the regularized limiting
Fubini–Study metric. Theorem 1.5 interpolates the norms of two fixed
metrics. The big-line-bundle convergence there is outside a pluripolar
set; it is not a global uniform convergence assertion.

These inputs do not yet supply Yao's minimizer-convergence assumption
A4. Independently minimizing Chow directions in each degree, even
after degreewise saturation SN(FS(chi_k))=chi_k, does not establish
the required cross-degree inequality

\[
  \chi_{k+\ell}(ss')\geq\chi_k(s)+\chi_\ell(s').
\]

A compatible graded filtration, or a quantitative replacement for
that compatibility controlling the varying minimizers, still has to
be constructed. The paper's statistical limits also do not establish
the general entropy slopes or hybrid continuity in the remaining
P19 atoms. Chapter 68's A2, general A3 and A4 remain assumptions.

The source's metric convention is
\(h=h_{\mathrm{ref}}e^{-2\varphi}\). A Hermitian vector-space
distance expressed using eigenvalues of the *squared* inner-product
comparison has a factor 1/2 in equation (2.65). The ordinary norm
ratios in (2.67) do not have this additional factor. These conventions
must be reconciled with the book's existing radial clock before any
future import.

## Complete P1 endpoint candidate

The target is the literal definition (1.18) and Theorem 1.7 for an
arbitrary continuous initial metric. The following derivation is a
research candidate; it is not a verified theorem-counterexample
receipt. It uses the source's norm-ray construction directly, so
the auxiliary distance or volume issues below are not inputs.

**Ambient space and initial metric.** Take
\(X=\mathbf P^1_{\mathbf C}\), \(L=\mathcal O(1)\), affine coordinate
\(z\), and \(r=\log|z|\). In the standard local frame set

\[
 \Phi_0(r)=\max\{0,r\},\qquad h_0=e^{-2\Phi_0}.
\]

Relative to the smooth Fubini–Study local weight
\(\Phi_{\mathrm{FS}}=\tfrac12\log(1+|z|^2)\), the potential
\(\Phi_0-\Phi_{\mathrm{FS}}\) extends continuously over both charts.
It is bounded and psh relative to the Fubini–Study curvature. With
the source's Poincaré–Lelong normalization, its curvature measure
is Haar probability on \(|z|=1\): the radial derivative jumps from
0 to 1 at \(r=0\). Thus \(\operatorname{vol}(L)=1\), and the
envelope of this psh initial metric is the metric itself.

**Filtration.** Identify \(R_k\) with polynomials of degree at most
\(k\), and set

\[
 \mathcal F^\lambda R_k
   =\operatorname{span}\{z^j:0\leq j\leq k,\ j\geq\lambda\}.
\]

This is decreasing, left continuous, multiplicative and linearly
bounded. Products add monomial orders; no cross-degree hypothesis
is left implicit. The jumps, as a multiset, are \(0,1,\ldots,k\).
Consequently

\[
 \mu_k=\frac1{k+1}\sum_{j=0}^{k}\delta_{j/k}
       \ \rightharpoonup\ \mathbf1_{[0,1]}\,dx.
\]

The mean is exactly 1/2 in every positive degree. The second moment
is \((2k+1)/(6k)\), and the variance is \((k+2)/(12k)\), tending
to 1/12. The limiting p-th integer moment is \(1/(p+1)\).

**Direct determination of the ray.** The initial sup-norm is

\[
 N_{k,0}(f)=\sup_z\frac{|f(z)|}{\max\{1,|z|\}^k}
          =\sup_{|z|=1}|f(z)|.
\]

The equality follows by applying the maximum principle to \(f\)
inside the unit disk and to \(f(z)/z^k\) on its exterior, including
infinity. This graded norm is submultiplicative. Use precisely
equation (5.15):

\[
 N_{k,t}(s)=\inf_{s=\sum_i f_i,\ f_i\in\mathcal F^{\mu_i}R_k}
              \sum_i e^{-t\mu_i}N_{k,0}(f_i),\qquad t\geq0.
\]

For any such summand, Fourier coefficients satisfy
\(|a_j|\leq N_{k,0}(f_i)\), and a nonzero coefficient has
\(j\geq\mu_i\). Put \(q=e^t|z|\). Since \(t\geq0\),
\(e^{t\mu_i}|z|^j\leq q^j\), so

\[
 |f_i(z)|\leq (k+1)\max\{1,q^k\}
                e^{-t\mu_i}N_{k,0}(f_i).
\]

Summing and taking the infimum gives the same evaluation bound
for \(s\). On the other hand the single-summand decompositions give
\(N_{k,t}(1)\leq1\) and \(N_{k,t}(z^k)\leq e^{-tk}\).
The evaluation-functional definition (2.54) therefore yields

\[
 \max\{0,r+t\}\leq\Phi_{k,t}(r)
    \leq\max\{0,r+t\}+\frac{\log(k+1)}k.
\]

The same estimate holds at 0 and, after changing frame, infinity.
It identifies the uniform limit and its regularization without an
appeal to Theorem 1.1, Theorem 1.3 or Theorem 1.7:

\[
 \Phi_t(r)=\max\{0,r+t\},\qquad h_t=e^{-2\Phi_t}.
\]

The toric Legendre roof on \([0,1]\) is \(-tx\). Equivalently, the
joint convex function is the maximum of two affine functions in
\((r,t)\). Its homogeneous Monge–Ampère measure on a finite strip
vanishes: a convex smooth approximation depending only on \(r+t\)
has Hessian of rank at most one, and the bounded Bedford–Taylor
limit has the same property. The local expressions extend at the
two divisors, where one branch is constant on a neighborhood of
each finite strip. These observations check the weak-geodesic
interpretation independently of the spectral identity.

**Endpoint comparison.** At every point of the initial circle
\(r=0\), the pointwise right derivative is
\(\partial_t^+\Phi_t|_{t=0}=1\). In the source's squared-metric
notation this is \(-\dot h_0/2=1\). Hence the literal pushforward
in (1.18) is \(\delta_1\), whereas the empirical limit is uniform
on \([0,1]\). Their means, 1 and 1/2, already differ.

Subtracting a character does not remove the discrepancy. If the
jumps are \(j-ck\), the ray weight is
\(\max\{0,r+t\}-ct\); the empirical limit is uniform on
\([-c,1-c]\), and the pointwise initial pushforward is
\(\delta_{1-c}\).

There is an energy check that uses only the dimension-one energy
difference identity. The initial curvature is on \(r=0\), the
time-t curvature is on \(r=-t\), and the weight difference on
those circles is respectively \(t\) and 0. Thus

\[
 E(h_t)-E(h_0)=\tfrac12\int(\Phi_t-\Phi_0)
                         (c_1(L,h_0)+c_1(L,h_t))=t/2.
\]

This agrees with the mean of the jumping distribution. The
pointwise derivative at this nonsmooth initial metric cannot be
substituted into a regular-endpoint Finsler formula.

**Regularity and a noncommuting limit.** A smooth positive toric
approximation is obtained with integer \(n\geq1\),
\(\eta_n=1/(n+1)\), and

\[
 \Phi_n(r)=\frac{1-\eta_n}{2n}\log(1+e^{2nr})
             +\frac{\eta_n}{2}\log(1+e^{2r}).
\]

The first summand is smooth and semipositive on both charts, and
the second supplies strict positivity. These weights converge
uniformly to \(\Phi_0\), with error at most
\((1-\eta_n)\log2/(2n)+\eta_n\log2/2\).
For the translated smooth ray \(\Phi_n(r+t)\), the derivative
\(a_n(r)=\Phi_n'(r)\) is strictly increasing from 0 to 1 and the
radial curvature measure is \(da_n\). The elementary change of
variables \(x=a_n(r)\) gives

\[
  (a_n)_*c_1(L,h_{n,0})=\mathbf1_{[0,1]}\,dx
\]

in every n. Nevertheless the uniformly limiting ray has the
pointwise right derivative 1 on the limiting initial curvature
circle. Thus uniform convergence of initial metrics or rays does
not justify this derivative-plus-curvature pushforward limit.
This diagnostic is compatible with the smooth-positive PLMS
Theorem 6.4 and the smooth-positive seed used in Chapter 65.

**Admission boundary.** Equation (2.44) in the big paper explicitly
assumes \(u_0=P_\theta(f)\) for \(f\in C^2(X)\). The proof on
page 57 invokes it after choosing an arbitrary continuous initial
metric and does not establish that additional hypothesis. The
candidate targets that extension of the initial pushforward, not
the existence of jumping-measure limits and not the PLMS
smooth-positive result. Its complete derivation and finite checks
are preserved for later adversarial verification. No fresh
independent production receipt exists, so it is not promoted to
`DISPROVED` in the book or the open-problem ledger.

## Auxiliary literal diagnostics

These checks identify formulas or proof steps requiring repair.
They do not individually refute the main distance, graded-norm or
regular-endpoint statements. Actual controlling pages were viewed.

| Locator | Diagnostic | Scope |
| --- | --- | --- |
| (2.38)–(2.40), p. 18 | I_p is an unrooted p-th integral. Comparing it directly to d_p with a constant uniform in all potentials fails the constant-shift scaling for p>1. | A root or p-th power is needed; no Lemma 2.13 statement refutation. |
| (2.42), p. 19 | With the volume-normalized norm (2.22), scaling theta,u,v by a positive t scales d_p by t. | The displayed identity omits that factor; Q-line-bundle proof uses need consistent units. |
| (2.51), p. 21 | The printed set with some nonvanishing section is the complement of the usual base locus. | Following discussion uses the usual base locus; the literal set definition is excluded. |
| Proposition 2.18 proof, p. 22 | Full essential support of a nonnegative bounded density does not imply positivity almost everywhere or measure-class equivalence. BBWN Proposition 1.12 is a determining criterion; Theorem 1.14 concerns the stronger psh-weight Bernstein–Markov property. | The printed proof does not establish its measure-class step. Nondetermining alone is not treated here as a counterexample to the section-norm conclusion. The separate cited Toeplitz Theorem 7.1 has not yet been checked. |
| After (2.65), pp. 24–25 | All Hermitian norms include a determinant direction. | The full symmetric space is GL/U; SL/SU requires determinant one. |
| Lemma 2.22 (2.75), p. 26 | Ordinary real volume of complex balls gives twice the sum of ordinary log norm ratios. | A factor 1/2 is missing under ordinary real-volume convention; no unusual volume convention is silently imposed. |
| Construction 2 / Proposition 3.2, p. 30 | Merely theta-psh algebraic singularities do not ensure ampleness after divisor subtraction. For X=Bl_p P2, L=pi*O(1), theta=pi*omega_FS, psi=0, the identity resolution has E=0 and the resulting L is big and nef but not ample. | The main distance proof chooses a *strictly* theta-psh potential. The boundary example diagnoses the broader construction as printed. |
| Theorem 1.1 proof, pp. 33–34 | Proposition 2.5 takes beta in the negative exceptional-divisor class, but the later metric on the positive exceptional line bundle is assigned that curvature. The singular divisor of psi+b psi_E is E+b E(b), whereas the displayed A subtracts E+E(b). | Both signs and the b coefficient require consistent correction before importing that proof literally. |
| Proposition 4.6 proof, p. 43 | The pure degree-p monomial map used as b is not injective for p>1, by roots of unity; arbitrary continuous G cannot descend by the asserted closed-embedding argument. | The printed auxiliary argument is excluded. This does not refute the underlying birational regularizability statement. |
| (5.17), p. 55 | Bounds for a ray built with e^{-t mu} require a t in the exponential Ck bounds. | For each fixed t a bound still follows; the displayed time-independent constant is not adopted. |
| Proof of Theorem 1.7, p. 57 | h_t>=h_0 gives nonnegative log-metric derivative, not the stated nonpositive one. After shifting weights negative, x^p is not real defined for every real p>=1. | The sign can be repaired; nonnegative absolute moments or positive integer moments suffice. Neither repair supplies the missing endpoint regularity. |

The actual pages also confirm absolute-value bars in (3.32), (3.33),
(3.37), (3.41), (5.19) and (5.21). Their loss during extraction
does not establish a one-sided-error gap, and no such claim is kept.

## A determining-measure diagnostic, with the narrower conclusion

On P1 let omega be Fubini–Study probability curvature and choose a
countable dense sequence q_i. Let g_i be log chordal distance to q_i,
normalized so that g_i<=0, dd^c g_i=delta_q_i-omega and
the omega integral of g_i is -1/2. For a_i=2^{-i-1}, i>=1, put

\[
 u=\sum_{i\geq1}a_i g_i,\qquad \psi=u+1.
\]

The sum of the coefficients is 1/2. The decreasing partial sums
are omega-psh and have bounded L1 norms; their limit is not
identically minus infinity, has omega integral -1/4, and is
omega-psh. Every q_i is a pole. Hence O={psi<0} is open and
dense, while the integral of psi is 3/4, so {psi>0} has positive
omega measure. The normalized density
rho=1_O/(integral_O omega) is bounded and has full essential
support, but vanishes on a set of positive omega measure.

For mu=rho omega, psi<=0 mu-almost everywhere and psi>0 somewhere.
BBWN Proposition 1.12(ii), with the smooth reference weight,
therefore diagnoses failure of the determining property. It also
demonstrates the failed measure-class inference in Proposition
2.18's printed proof. BBWN's ordinary section Bernstein–Markov
property is weaker than its psh-weight version; the 2011 source
explicitly asks about the converse in Question 1.11. This record
does not assert that the question remains open today, and does
not infer failure of the ordinary section conclusion from this
diagnostic alone. Further study must inspect the alternative
Toeplitz theorem before deciding the scope of Proposition 2.18.

## Verification and next work

The exact checker tests discrete moments in 240 positive degrees,
the first nine powers by an independently assembled Stirling
power-sum identity, the mean and variance, shifted distributions,
the corner derivative, the dimension-one energy check and the
complex-ball volume factor. These are finite consistency tests,
not independent certificates for analytic limit or weak-geodesic
statements. The accompanying manifest records that distinction.

Next inspect the current primary Toeplitz theorem underlying
Proposition 2.18, then inspect primary regularity results for
initial velocity measures and possible joint-measure formulations.
Keep the exact current monograph and catalogue intact while
these candidates undergo research audit. The BJ22 general Siu
and envelope issues are unrelated to the new candidate and
remain conditional in their existing scope.
