# Toeplitz envelopes and full-support density candidates — 5 October 2026

This research checkpoint follows commit
77d2e9e980567fa0a85a9e6e589dc2ff46519b87. It completes the primary
reading deferred in the preceding big-quantization audit and writes
three explicit diagnostics. They are research candidates, without
independent production receipts. No source-counterexample verdict is
promoted into the book, no theorem environment is added, and all 42
active problem statuses retain their existing scope.

## Controlling text and what was actually checked

Siarhei Finski, *Small eigenvalues of Toeplitz operators, Lebesgue
envelopes and Mabuchi geometry*,
[arXiv:2502.01554v1](https://arxiv.org/abs/2502.01554v1), submitted
3 February 2025 at 17:34:28 UTC. Current metadata lists only v1,
math.CV, 32 pages. The actual PDF was acquired on 5 October 2026
at 14:47:55.871749 UTC, HTTP 200, 434,313 bytes, SHA-256
76717824c1541c9a0041f4b8b5d6233d0caaf4ee2d989a17df9ccc46ba442af5.
All 1,715 split lines were read in eight contiguous ranges, including
references. Eighteen actual controlling pages were inspected:
2–5, 14–21, 24–29. Three additional actual BBWN published pages,
13 and 16–17, check definitions, the exponential-integral continuity
input and its correct locator. The BBWN PDF is the same frozen
27-page published file pinned in the preceding audit, not an
unacquired edition. There are 21 fresh primary-page inspections in
eleven sheets. BBWN remains a selective dependency reading.

The first metadata search returned noisy secondary material as well
as primary sources. Only the acquired primary PDFs control this
record. Gupta's related metric paper was located, but has not yet
been acquired here and supplies no proof input. No exhaustive search,
priority or independent model-verification claim is made.

## The comparison theorem does not use support alone

The ambient category is a smooth complex projective manifold with
an ample line bundle. The paper begins with a smooth positive metric
and a nonzero nonnegative bounded symbol; its standing essential
infimum zero ensures nonnegativity. For continuous initial metrics
it defines the non-negligible psh envelope by an almost-everywhere
constraint. At the level of its full squared-metric potentials,

\[
 \varphi_\mu=\sup\{\psi\in\operatorname{PSH}(X,\omega):
                              \psi\leq\varphi\quad\mu\text{-a.e.}\}.
\]

This envelope depends on the measure class, and can differ from
the envelope constrained on the closed support. Theorem 7.1 requires
\(h_\mu\geq h_0\), with \(h_0\) continuous, before giving the
subexponential lower bound for the weighted L2 norm against the
sup-norm of \(h_0\). In potential notation the requirement is
\(\varphi_0\geq\varphi_\mu\), not merely that the support is all X.
Its proof replaces the potentially non-usc functional
\(\sup(\psi-\varphi_\mu)\) by the smaller usc functional
\(\sup(\psi-\varphi_0)\), and uses compactness and a decreasing
usc Dini argument. The exponential-integral continuity input is
BBWN **Lemma 1.15**, and the determining/psh-weight equivalence is
BBWN **Theorem 1.14**. The numerical citations to Lemma 1.14 and
Theorem 1.13 on page 21 of the controlling text are not their
actual published locators.

Theorem 5.3 compares the norms for a bounded density to those of
the Lebesgue envelope of its *nonzero set*, in finite p. An operator
norm conclusion retains continuity of that envelope. Its argument
approximates that envelope by smooth positive metrics and uses
known distance quantization. A fixed factor of two in distance
units does not change a zero asymptotic equivalence, but numerical
distance identities must use consistent units. The initial point
in the main Toeplitz velocity formula is smooth and positive;
the continuous corner example in the preceding audit does not
target that formula.

The source explicitly discusses positive-measure zero sets inside
the essential support. Its nonpathological Corollary 1.4 requires
that those zero sets have measure zero. The construction below
has a positive-measure zero set and is compatible with that
restriction. It tests the later big paper's Proposition 2.18,
whose stated density hypothesis is only full essential support.

## A direct full-support L2/sup-norm candidate

This strengthens the earlier determining-measure diagnostic. It
proves a norm gap directly from explicit sections, without inferring
ordinary section Bernstein–Markov failure from nondetermining alone,
and without using the Toeplitz quantization theorems as inputs.

**Geometry and normalization.** On
\(X=\mathbf P^1_{\mathbf C}\), \(L=\mathcal O(1)\), let h be the
smooth positive Fubini–Study squared metric and let omega be its
probability curvature. Choose distinct points q_i, i>=1, forming
a countable dense subset of P1. For each choose a linear section
ell_i, normalized so that its h-norm is chordal distance to q_i.
Put \(g_i=\log|\ell_i|_h\). Then

\[
 g_i\leq0,\qquad dd^cg_i=\delta_{q_i}-\omega,
                     \qquad \int g_i\,\omega=-\tfrac12.
\]

The integral follows from unitary invariance: squared chordal
distance to a fixed point is uniform on [0,1], and the integral
of one half of log x on that interval is -1/2.

**A dense open set.** Set

\[
 v=\sum_{i\geq1}2^{-i}g_i,\qquad \psi=1+v,
                         \qquad O=\{\psi<0\}.
\]

The partial sums decrease and are omega-psh. Their negative L1
integrals stay bounded because the coefficients sum to one.
Consequently the limit is omega-psh, not identically minus infinity,
and has omega integral -1/2. Each q_i is a pole. Upper
semicontinuity therefore makes O open, and the dense sequence of
poles makes O dense. It has positive measure. Also
\(\int\psi\,\omega=1/2\) and \(\psi\leq1\), so
\(\{\psi>0\}\) has positive omega measure. O is not conull.

**Sections of rapidly growing degree.** Let ell_0=ell_1,
\(k_n=2^n\), and

\[
 s_n=e^{k_n}\,\ell_0\prod_{i=1}^n\ell_i^{2^{n-i}}
                                      \in H^0(X,k_nL).
\]

The total degree is \(1+\sum_{i=1}^n2^{n-i}=2^n\).
With

\[
 \psi_n=\frac1{k_n}\log|s_n|_{h^{k_n}}
            =1+\sum_{i=1}^n2^{-i}g_i+2^{-n}g_0,
\]

the curvature mass is that of a genuine degree-k_n section,
\(\int\psi_n\,\omega=1/2\), and
\(\sup_X\psi_n\geq1/2\). Thus

\[
       N_\infty(s_n)\geq e^{k_n/2}.
\]

Outside q_0, the final term tends to zero and the partial sum
tends to v, including the possible limit minus infinity. At q_0
all the sections vanish. Hence at every point of O the norms
\(|s_n|_{h^{k_n}}\) tend to zero and are at most one for all
sufficiently large n, with the threshold depending on the point.

**One fixed density, not a varying measure.** Define the
measurable nonnegative series

\[
 F(x)=\sum_{n\geq1}2^{-n}|s_n(x)|_{h^{k_n}}^2,
 \qquad
 \rho(x)=
 \begin{cases}(1+F(x))^{-1},&x\in O,\\0,&x\notin O.\end{cases}
\]

F is finite on O, by the pointwise eventual bound just proved.
Thus \(0\leq\rho\leq1\), and rho is strictly positive at every
point of O. Every nonempty open set meets O in a nonempty open
set of positive area, so rho has full essential support X. Its
integral is positive, and it vanishes on a set of positive area.
It is a *single fixed* bounded density for all n; the construction
does not change the density after choosing a degree.

The n-th nonnegative summand in F gives, everywhere on O,
\(\rho|s_n|^2\leq2^n\). Outside O the weighted integrand is zero.
Therefore

\[
 \|s_n\|_{L^2(h^{k_n},\rho\omega)}^2\leq2^n,
 \qquad
 \frac{\|s_n\|_{L^2(h^{k_n},\rho\omega)}}{N_\infty(s_n)}
       \leq \exp\left(\frac{n\log2}{2}-\frac{2^n}{2}\right).
\]

The degree-normalized logarithm has limsup at most -1/2.
No positive constant can repair a subexponential comparison.
In particular, taking epsilon=1/4 diagnoses the literal conclusion
of Proposition 2.18 in 2512.10466v1 for arbitrarily large degrees,
despite every stated density hypothesis holding. Normalizing rho
to a probability density only adds a degree-independent factor.

This derivation remains a research counterexample candidate until
the required independent audit. It does not alter the statement's
scope in the active book or assign a `DISPROVED` ledger verdict.
It also does not target smooth positive densities, or the densities
coming from a nonzero holomorphic section, which are positive
almost everywhere. Those are the actual cases used in the big
paper's main arguments.

**Toeplitz consistency check.** The Fubini–Study evaluation kernel
in degree k has constant value k+1, so
\(N_\infty(s)\leq\sqrt{k+1}\|s\|_{L^2(h^k,\omega)}\).
The Rayleigh quotient of s_n consequently gives

\[
 \lambda_{\min}(T_{k_n}(\rho))
       \leq k_n(k_n+1)e^{-k_n}.
\]

This is a positive, nonzero symbol with essential support X and
a positive-area zero set. It fits the pathological case explicitly
excluded from the source's support criterion, and gives an
independent check of the exponential gap. Neither the derivative
formula nor a source spectral-convergence theorem was needed.

## Circular caps test the local-comparison statement

This is an auxiliary candidate against the literal Corollary 1.6
in 2502.01554v1, not against its main logarithmic quantization
theorem. Put \(p=|z|^2/(1+|z|^2)\), so the Fubini–Study
probability measure is \(dp\,d\theta/(2\pi)\), and set
\(f_a=\mathbf1_{\{p\leq a\}}\), \(0<a<1\).
The support K_a is a closed smooth disk; it has no positive-area
zero set inside its support and is Lebesgue pluriregular. The
regularity is the usual smooth-domain case, checked in BBWN
Corollary 1.7 and in the controlling source's Proposition 4.3.

The standard Fubini–Study orthonormal monomials have squared
pointwise norms \((k+1)\binom kj p^j(1-p)^{k-j}\).
Rotational invariance makes the cap Toeplitz operator diagonal,
with eigenvalues

\[
 \lambda_{k,j}(a)
  =(k+1)\binom kj\int_0^a p^j(1-p)^{k-j}\,dp
  =\sum_{\ell=j+1}^{k+1}\binom{k+1}{\ell}
                        a^\ell(1-a)^{k+1-\ell}.
\]

The last equality follows by differentiating the binomial tail
and comparing the value at zero. These tails decrease strictly
in j for 0<a<1, so the smallest eigenvalue is exactly
\(\lambda_{k,k}(a)=a^{k+1}\). Its exponential rate is -log a.

Take a=1/4 and a'=3/4 on the same X,L,h. Choosing U=U'=X and
the identity biholomorphism satisfies every displayed geometric
condition of Corollary 1.6 as printed: the line bundle and metric
are preserved. The statement does not require preservation of
K or NZ. Yet the two smallest-eigenvalue rates differ. This
tests even the regular, nonpathological case of its second
assertion. Its proof on page 26 cannot identify endpoint envelopes
from the metric biholomorphism alone. A corrected local comparison
would require appropriate support/constraint compatibility, and
pathological interior zero sets would need separate treatment.
No corrected general theorem is claimed here.

## A disk plus an isolated point tests weak versus psh-weight BM

This candidate addresses Corollary 5.7 without adding regularity
silently. Let D={p<=1/2}, q=infinity, K=D union {q}, and use
the probability measure \(\mu=2\mathbf1_D\omega\). Multiplying
the unnormalized Lebesgue measure on K by two does not affect a
weak-BM limit, because the log-volume change divided by k times
dimension is O(1/k).

Write H_k for the L2 norm of mu, N_D for the sup-norm on D,
and N_K for the sup-norm on K. The preceding cap eigenvalues
give an elementary bound on the reproducing kernel of H_k.
For j<=k/2, \(\lambda_{k,j}(1/2)\geq1/2\). For j>k/2 the
monomial squared norm increases on [0,1/2] and

\[
 \lambda_{k,j}(1/2)\geq
          \binom{k+1}{j+1}2^{-k-1}\geq\binom kj2^{-k-1}.
\]

Every summand of the H_k reproducing kernel on D is therefore
at most k+1, and the full kernel is at most (k+1)^2. Hence
\(H_k\leq N_D\leq(k+1)H_k\).

Only the top monomial is nonzero at q, and its evaluation-dual
norm squared for H_k is \((k+1)2^k\). Define the Hermitian norm
\(R_k(s)^2=H_k(s)^2+|s(q)|_{h^k}^2\). It follows that

\[
 R_k/\sqrt2\leq N_K\leq(k+1)R_k,
 \qquad
 \frac{\operatorname{vol}(R_k)}{\operatorname{vol}(H_k)}
          =\frac1{1+(k+1)2^k},
\]

where volume is ordinary real volume of the complex unit balls.
Since N_K>=H_k, these bounds give

\[
 0\leq\log\frac{\operatorname{vol}(H_k)}{\operatorname{vol}(N_K)}
  \leq\log(1+(k+1)2^k)+2(k+1)\log(k+1).
\]

After division by k(k+1) the upper bound tends to zero. This
proves weak section Bernstein–Markov behavior directly in this
candidate, without importing Corollary 5.7 or Proposition 5.5.

On the other hand the bounded continuous omega-psh potential
with local weight

\[
 \Phi_D(r)=
 \begin{cases}\tfrac12\log(1+e^{2r}),&r\leq0,\\
                 r+\tfrac12\log2,&r\geq0
 \end{cases}
\]

is zero relative to Fubini–Study on D and has relative value
\(\tfrac12\log2>0\) at q. It thus satisfies the obstacle
mu-almost everywhere but not on K. This violates BBWN's
determining/psh-weight criterion. More directly, its exponential
integral against mu is one while its supremum on K grows as
\(e^{p\log2/2}\), contradicting the psh-weight BM estimate for
epsilon<log2/2. Full-potential conventions simply multiply both
constants by two. The isolated point is the nonregular boundary;
the earlier regular-set BBWN Question 1.11 is not contradicted.
This record makes no claim that a historical question remains
open today.

The source's Proposition 5.5 separates the weak criterion from
its stronger conclusion under pluriregularity. Corollary 5.7 as
printed drops that regularity. The candidate is kept outside
active TeX pending independent review.

## Additional normalization and scope diagnostics

Actual pages confirm the following literal issues. They do not
individually refute the main Toeplitz or envelope statements.

- Equations (1.7), (5.5)–(5.6), (5.17) and (8.1) mix a full
  squared-metric potential u with ordinary vector norm ratios.
  For h_1=e^{-c}h_0 the L2 norm scales by e^{-kc/2}, whereas
  the potential distance is |c|. Thus (5.17) needs the factor
  1/2 with ordinary induced norms.
- The transfer operator in Section 6 compares squared inner
  products through exp(-T). Consequently the right side of
  (6.1) needs 2 d_p with the ordinary-norm definition. The
  asymptotic equivalence conclusion survives the fixed factor.
- With ordinary real complex-ball volume, (5.14), (5.15)
  and (9.5) need twice the sum/mean of ordinary log norm
  ratios. The John-ellipsoid estimate (5.13) also needs its
  dimension factor. After normalization by k times dimension,
  the ellipsoid error still vanishes; no volume-equivalence
  theorem is refuted by this arithmetic issue alone.
- Under the full-potential convention (1.7), substituting a
  section in (7.2) uses psi=(2/k)log|s| and p=k. The printed
  psi=(1/k)log|s|, p=2k does not give the displayed weighted
  section integral with that convention.
- The generalized moment equations on pages 27 and 29 write
  a p-th moment equal to d_p rather than d_p^p. A constant
  metric displacement tests the power. The displayed eta_k
  also contains a limit although it names the finite sequence.
  No unrestricted generalized theorem is admitted here.
- Absolute-value bars in (5.12), (5.13) and (6.3)–(6.7) are
  present in the actual PDF. Their extraction loss is not a
  mathematical gap. The limit i->0 in (6.2) and the repeated
  h_1^i on both sides of (6.4) are auxiliary typographical
  issues; their intended approximation direction is explicit
  in the surrounding argument.

The preceding frozen audit remains an accurate record of what
had been checked at its own checkpoint. The new fixed-density
construction advances the ordinary section test that it had
left pending. None of these source candidates repairs the BJ22
critical Siu division, constructs compatible Chow minimizers,
proves Yao A4, or solves a remaining P19 atom.

## Finite verification and continuation

The accompanying rational checker compares beta-polynomial
integration with independently accumulated binomial tails, checks
the cap minimum, the half-cap kernel bound and the rank-one
determinant, and checks the dyadic section degrees. It does not
numerically construct the infinite density or independently
certify its analytic proof. All candidate proofs, assumptions
and this limit are stated above; no model receipt is fabricated.

Next inspect Gupta's actual current metric source for the endpoint
velocity regularity restriction, and the primary formulations of
joint velocity/curvature measures under approximation. Keep all
active manuscript, bibliography, catalogue, protected Appendix
M–N files and frozen book artifacts unchanged until an import
has the required source and verification clearance.
