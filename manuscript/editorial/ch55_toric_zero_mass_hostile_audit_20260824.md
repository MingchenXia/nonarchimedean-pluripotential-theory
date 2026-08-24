# Hostile audit of the toric zero-mass proof in Chapters 55 and 69

**Superseded-stage notice.**  This document records the first hostile pass and
its three must-fix findings.  The repairs passed the separate post-repair
hostile audit, the source-attested exact Chapter 55 block passed production
run `20260824T052605Z_703e3b501202`, and the exact-current Chapter 69
integration passed `20260824T070302Z_d706dc98ccca`; both production verdicts
are final `correct`, with zero critical errors and zero gaps.  The verdict
below is retained only as the pre-repair audit trail.

**Date:** 24 August 2026  
**Chapter 55 source audited:** `parts/part5/ch55_okounkov_dh.tex`  
**Chapter 55 SHA-256:** `751257293aaf92c94371b90a1e930579f108565d8d404dd526deb8f2523a4512`  
**Chapter 69 source audited:** `parts/part6/ch69_verified_extensions.tex`  
**Chapter 69 SHA-256:** `f1601df23220675cddfe594b78b594a1939fb6c2b815e5208ec163225fb8258a`

## Verdict

**NOT YET PASS: three local but genuine interface repairs are required.**

No counterexample was found to the theorem
\(\nu_{\mathrm{Cao}}(T)=\dim\Delta(T)\) in the stated smooth projective
toric integral/rational setting.  Once the three items below are made
explicit, the character count, convex squeeze, use of Cao's criterion, and
tube exponent form a valid proof.  In its present form, however, the proof
contradicts the book's fixed multiplier-ideal normalization and applies
Guenancia's monomial criterion before checking that the local character
coefficient is holomorphic.  Those are not optional stylistic details in a
proof whose purpose is to close precisely these interfaces.

Chapter 69 delegates its character calculation to Chapter 55 and is
otherwise synchronized correctly.  It inherits the repairs below and should
say explicitly that the normalization conversion and holomorphicity check
are the ones made in Chapter 55.

## Must-fix items

### M1. The assertion that Guenancia uses the "same" weight normalization is false

Chapter 55, lines 1378--1382, says that Guenancia's criterion is being used
"in the same \(e^{-2\varphi}\) normalization" for
\(\mathcal I(m\varphi)\).  The book has fixed the different squared-norm
convention in Chapter 51:

\[
 \mathcal I_{\mathrm{book}}(\Phi)
 =\{f:|f|^2\exp(-\Phi)\in L^1_{\mathrm{loc}}\}.
\]

Guenancia defines
\(\mathscr I_{\mathrm G}(\psi)\) by integrability of
\(|f|^2\exp(-2\psi)\).  Therefore the correct conversion is

\[
 \psi_\sigma=\frac{1}{2}\Phi_\sigma,
 \qquad
 \mathcal I_{\mathrm{book}}(m\Phi_\sigma)
 =\mathscr I_{\mathrm G}(m\psi_\sigma).
\]

This factor cannot be left implicit.  The one-variable unit test is
decisive: for the book weight
\(\Phi=\lambda\log|z|^2\), one has
\(\mathcal I_{\mathrm{book}}(\Phi)=(z^{\lfloor\lambda\rfloor})\); feeding
the same function, rather than \(\Phi/2\), into an
\(\exp(-2\psi)\)-definition would instead produce the threshold
\(\lfloor2\lambda\rfloor\).

The repair should introduce the local squared-norm weight
\(\Phi_\sigma\), set \(\psi_\sigma=\Phi_\sigma/2\), and define the global
convex weight \(F_T\) as the corresponding **norm** weight with logarithmic
coordinates.  Equivalently, one may use the squared-norm weight with
log-squared coordinates, but that coordinate conversion must be stated.
With either consistent choice, Guenancia's local Newton set has the desired
lattice scale and no factor two occurs in \(K-d_\sigma+\sigma^\vee\).

Primary-source check: Guenancia defines his ideal by
\(|f|^2e^{-2\psi}\) and gives the \(+\mathbf 1\) strict-interior criterion
in the toric theorem; see
[arXiv:1011.3162v2, Section 1.3](https://arxiv.org/abs/1011.3162).

### M2. Passing from Guenancia's possibly nonclosed Newton set to the closed body needs one sentence

Lines 1368--1382 identify a **closed** local Newton body

\[
 \overline{P(\psi_\sigma)}
 =K-d_\sigma+\sigma^\vee
\]

and then apply Guenancia's criterion using the interior of that closed set.
Guenancia's effective Newton set is not asserted to be closed in general.
The step is correct here, but the proof must say why: the local set is convex,
its closure contains the full-dimensional cone \(\sigma^\vee\) up to
translation, and hence

\[
 \operatorname{int}P(\psi_\sigma)
 =\operatorname{int}\overline{P(\psi_\sigma)}
 =\operatorname{int}(K-d_\sigma+\sigma^\vee).
\]

This also makes clear that "closed effective domain" means closure of the
effective domain, not an unsupported assertion that the effective domain is
already closed.

### M3. Guenancia's theorem concerns holomorphic monomials; the proof starts with an arbitrary character

For a character \(\chi^u\), lines 1362--1367 give the local Laurent exponent

\[
 \alpha_\sigma=u-md_\sigma-m\varepsilon a_\sigma.
\]

Guenancia's theorem applies to a holomorphic monomial, so initially it only
applies when \(\alpha_\sigma\in\sigma^\vee\cap M\).  Lines 1383--1398
claim an equivalence for every \(u\in M\) without imposing or recovering
this condition.

The missing check is short.  Positivity of the invariant metric gives

\[
 K\subset P_D\subset d_\sigma+\sigma^\vee,
 \qquad
 Q\subset a_\sigma+\sigma^\vee.
\]

Thus
\(m(K-d_\sigma)+\sigma^\vee\subset\sigma^\vee\).  If
\(\alpha_\sigma+\kappa_\sigma\) lies in the interior of this local Newton
set, then, in the smooth chart basis,
\(\alpha_{\sigma,j}+1>0\) for every \(j\).  Since the coordinates are
integers, \(\alpha_{\sigma,j}\geq0\), so the Laurent monomial is in fact
holomorphic.  This proves that the displayed strict-interior condition
automatically includes the ordinary toric section condition.  Alternatively,
the proof may first restrict \(u\) to the usual polytope of
\(mD+m\varepsilon A\) and then show the same redundancy.  One of these
arguments must appear before the equality
\(\dim W_{m,\varepsilon}=\#E_{m,\varepsilon}\).

## Checks that pass

### Cartier data and the sign of the local exponent

With the standard convention

\[
 D|_{U_\sigma}=\operatorname{div}(\chi^{-d_\sigma}),
\]

the local frame of \(\mathcal O_X(D)\) is \(\chi^{d_\sigma}\).  Hence the
coefficient of \(\chi^u\) in
\(\mathcal O_X(mD+m\varepsilon A)\) has exponent
\(u-md_\sigma-m\varepsilon a_\sigma\), exactly as written.  Subtracting
the Cartier linear term translates the local Newton set by
\(-d_\sigma\), so the sign in
\(K-d_\sigma+\sigma^\vee\) is also correct.

### The Guenancia shift and the cancellation

For the smooth chart coordinates
\(z_j=\chi^{e_{\sigma,j}}\), the Jacobian shift is
\(\kappa_\sigma=\sum_j e_{\sigma,j}\), with a plus sign.  After the
normalization repair M1, the condition is

\[
 \alpha_\sigma+\kappa_\sigma
 \in\operatorname{int}\bigl(m(K-d_\sigma)+\sigma^\vee\bigr).
\]

Cancelling \(md_\sigma\) and using
\(Q+\sigma^\vee=a_\sigma+\sigma^\vee\) gives exactly

\[
 u+\kappa_\sigma
 \in\operatorname{int}\bigl(m(K+\varepsilon Q)+\sigma^\vee\bigr).
\]

No sign or factor of \(m\varepsilon\) is missing.

### Newton body under the ample perturbation

For norm weights, addition of currents adds convex weights.  Convex
conjugation turns this into lower-semicontinuous infimal convolution.  After
taking closures of effective domains, compactness gives

\[
 \Delta(T+\varepsilon\omega_A)=K+\varepsilon Q.
\]

The use of closures is essential but sufficient; no extra closure is needed
on the right because \(K\) and \(Q\) are compact.

### Global intersection identity

The identity

\[
 B=\bigcap_{\sigma\in\Sigma(n)}(B+\sigma^\vee)
\]

is valid for every compact convex \(B\) and every complete fan.  The stated
separation proof has the correct orientation: choose
\(v\) with
\(\langle x,v\rangle<\min_B\langle -,v\rangle\), then choose a maximal
cone containing \(v\); elements of its dual cone pair nonnegatively with
\(v\).

### Uniform boundedness and the inner/outer squeeze

The shifted intersections \(C_{m,\varepsilon}\) are uniformly bounded.
For a fixed basis \(v_1,\ldots,v_n\) of \(N_{\mathbf R}\), choose maximal
cones containing \(v_i\) and \(-v_i\); the corresponding two inequalities
bound \(\langle x,v_i\rangle\) from both sides, uniformly for the
\(O(m^{-1})\) shifts.  Any bounded sequence in the intersections has every
limit point in all closed sets \(B_\varepsilon+\sigma^\vee\), hence in
\(B_\varepsilon\).  Conversely, every compact subset of
\(\operatorname{int}B_\varepsilon\) has a positive margin from all finitely
many complements and is eventually contained in the shifted intersections.
This proves precisely the inner/outer squeeze used in the manuscript.

### Lattice normalization, subsequences, and the absence of \(n!\)

The measure \(\lambda_M\) has lattice covolume one.  Therefore

\[
 \#(mC\cap M)/m^n\longrightarrow\lambda_M(C)
\]

for a bounded full-dimensional convex body, including along the subsequence
on which \(m\varepsilon\in\mathbf Z\).  Squeezing between a fixed homothetic
inner body and a fixed outer parallel body proves an actual limit for the
varying open sets \(C_{m,\varepsilon}\).  The leading coefficient of the
normalized character count is \(\lambda_M\), whereas the algebraic volume
would be \(n!\lambda_M\); the manuscript correctly has no \(n!\) in the
quantity used by Cao.

### Rational scaling

Replacing \((D,T,\varphi,K)\) by
\((qD,qT,q\varphi,qK)\) clears denominators.  The affine dimension of the
body is unchanged, and Cao's cohomological products are homogeneous, so
their vanishing degrees are unchanged.  Chapter 69 states this point
explicitly.  The divisibility condition \(m\varepsilon\in\mathbf Z\) is the
correct one after the reduction to an integral divisor.

### Cao's inner limsup and ordinary multiplier ideal

Cao's Proposition 4.4 uses

\[
 \lim_{\varepsilon\to0}
 \frac{\log\bigl(\varlimsup_m h^0/m^n\bigr)}{\log\varepsilon}
 =n-\operatorname{nd}(D,\varphi)
\]

with the ordinary multiplier ideal.  This is reproduced correctly in
Chapter 69.  In the toric situation the preceding lattice calculation proves
that the inner limsup is an actual positive limit, so Chapter 55 is entitled
to replace that limsup by its computed limit.  Cao also compares the
upper-regularized ideal used in the proof with the ordinary ideal.  See
[arXiv:1210.5692v1, Proposition 4.4](https://arxiv.org/abs/1210.5692).

### Tube exponent

If \(d=\dim K\), a relative \(d\)-ball in \(K\) and an ambient
\(n\)-ball in \(Q\) give the lower bound
\(c\varepsilon^{n-d}\).  Bounding \(K\) in its affine \(d\)-plane and
\(Q\) in an ambient box gives the upper bound
\(C\varepsilon^{n-d}\).  The argument covers \(d=0\) and \(d=n\).
Consequently

\[
 \log\lambda_M(K+\varepsilon Q)
 =(n-d)\log\varepsilon+O(1),
\]

and Cao's criterion yields \(\nu_{\mathrm{Cao}}(T)=d\).

## Safe disposition

Retain both theorems, but do not mark the current snapshot PASS.  Insert the
half-weight conversion, the closure/interior equality, and the automatic
holomorphicity argument in Chapter 55; add a short synchronization phrase in
Chapter 69.  Then resubmit the exact repaired theorem-and-proof source to
Rethlas.  No change is required to the global gluing identity, the lattice
normalization, Cao's limsup, or the tube estimate.
