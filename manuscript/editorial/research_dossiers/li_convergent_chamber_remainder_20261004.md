# Analytic remainder on a compact chamber from convergent sections

Date: 4 October 2026. This book-external derivation supplies the analytic
leading-remainder estimate for a fixed convergent chamber basis on a
fixed chart. It separates the monomial weight from the possibly vanishing
leading coefficient function. No general CY theorem, status change,
finite numerical certificate or external verifier is claimed.

## Local signature

Fix a regular SNC chart with \(t=\prod_{i=0}^m z_i^{b_i}\),
\(b_i>0\), and a connected transverse polydisc \(W\).
Let \(W_c\Subset W\) be the transverse compact region used for
integration. At one fixed tensor degree there are finitely many
convergent meromorphic sections. In a nonvanishing model frame,
each local coefficient is

\[
 G(z,w)=z^\gamma H(z,w),\qquad
 H(z,w)=\sum_{\beta\in\mathbb N^{m+1}}f_\beta(w)z^\beta, \tag{1}
\]

where \(\gamma\in\mathbb Z^{m+1}\), \(H\) is holomorphic on a
fixed product neighborhood, and the series converges there.
Clearing a power of \(t\) provides this form for the meromorphic
sections in the preceding module construction.

Let \(\Sigma\) be a compact subset of the relative interior of one
full-dimensional chamber in the weighted simplex
\(\Delta_b=\{x_i\geq0:\sum b_ix_i=1\}\). Suppose the fixed section
has the unique leading exponent \(\alpha=\gamma+\beta_0\) throughout
that chamber. Thus, for every other exponent in its nonzero support,

\[
              (\beta-\beta_0)\cdot x>0\quad(x\in\Sigma). \tag{2}
\]

The finite-common-chamber proof supplies this uniqueness for each
section of a chamber-orthogonal basis. Since \(\Sigma\) stays away
from the simplex boundary, fix \(\delta>0\) with \(x_i\geq\delta\)
there. All constants below may depend on the fixed degree, section,
chart, transverse compactum and chamber margin, but not on \(t\).

## Uniform gap, including the infinite support

Choose \(\rho\in(0,1)\) such that a closed \(z\)-polydisc of radius
\(\rho\), times \(W_c\), lies in the holomorphy neighborhood of
\(H\). Cauchy's estimate gives one \(M\) with

\[
             \sup_{W_c}|f_\beta|\leq M\rho^{-|\beta|_1}. \tag{3}
\]

Set \(B_0=\max_{x\in\Sigma}\beta_0\cdot x\). For every exponent,

\[
 d_\beta(x):=(\beta-\beta_0)\cdot x
                       \geq\delta|\beta|_1-B_0.         \tag{4}
\]

Choose an integer \(N\geq4\) with \(N\geq4B_0/\delta\).
For the finitely many nonleading support exponents with
\(|\beta|_1\leq N\), their strictly positive continuous differences
in (2) have a common positive minimum \(g\) on \(\Sigma\).
If this finite set is empty, set \(g=1\). Choose
\(0<\eta\leq\min\{g/2,\delta/4\}\).
For \(|\beta|_1>N\), (4) gives

\[
 d_\beta(x)\geq\tfrac34\delta|\beta|_1
             \geq\eta+\tfrac14\delta|\beta|_1.          \tag{5}
\]

This proves a uniform positive leading gap over the whole infinite
support. Checking only a finite list of low-order terms would not
have supplied the tail estimate.

## Pointwise remainder bound

Write \(T=-\log|t|\) and consider chart points with
\(x_i=-\log|z_i|/T\in\Sigma\), \(w\in W_c\).
The monomial chart equation gives \(\sum b_ix_i=1\).
For sufficiently large \(T\), all \(|z_i|\leq e^{-\delta T}\)
lie inside the fixed convergence radius. Dividing the remainder by
the nonzero monomial \(z^\alpha\) gives

\[
 \frac{|G-f_{\beta_0}(w)z^\alpha|}{|z^\alpha|}
 \leq\sum_{\beta\ne\beta_0}|f_\beta(w)|e^{-Td_\beta(x)}.\tag{6}
\]

The finite part is bounded by \(C e^{-2\eta T}\), by (3) and
the choice of \(g\). For the tail, (3),(5) give

\[
 M e^{-\eta T}\sum_{\beta\in\mathbb N^{m+1}}
     \left(\rho^{-1}e^{-\delta T/4}\right)^{|\beta|_1}
 =M e^{-\eta T}
       \left(1-\rho^{-1}e^{-\delta T/4}\right)^{-m-1}.    \tag{7}
\]

Choose \(T\) so the quantity in parentheses before summing is at
most \(1/2\). The last factor is bounded by \(2^{m+1}\).
Combining (6)–(7) proves

\[
 |G-f_{\beta_0}(w)z^\alpha|
                       \leq C e^{-\eta T}|z^\alpha|.     \tag{8}
\]

Finitely many basis sections have a common positive \(\eta\), common
constant and common radius by taking minima/maxima. Multiplying both
sides of (8) by the frame norm transfers it to the section norms,
with monomial weight \(|z^\alpha\tau|_{h^l}\). This pointwise step
does not need a bound on that frame norm near the central fibre.

The denominator in (6),(8) is the **monomial weight**, not
\(|f_{\beta_0}(w)z^\alpha|\). The coefficient function can have
zeros on \(W_c\); a relative estimate dividing by that function is
not claimed. Its within-class independence is used later through
a positive Gram matrix, as in the dyadic/Fourier proof.

## Full cores and arbitrary coefficient tuples

Choose the chamber margin so an enlarged compact chamber region
contains the log vectors of all full dyadic cores in use. Fixed dyadic
radial factors change these vectors by \(O(1/T)\), so this inclusion
holds after shrinking the fixed-degree radius. Use (8) on that enlarged
region. If \(W_i\) denotes the leading monomial times frame norm at a
reference point of a core, assume the reference has the meromorphic-model
comparison already used in the metric bridge. Its frame norm is a
fixed vertical monomial times a positive bounded unit, permitting
rational exponents for a rational model metric. Its norm everywhere
on the full core is then comparable to \(W_i\), with fixed-degree
constants. A smooth reference on this same model bundle is a special
case. Eliminating \(z_0\) makes the coordinate monomial's weight
\(|t|^{\alpha_0/b_0}\prod_{j=1}^m R_j^{\alpha_j-b_j\alpha_0/b_0}\),
which is multiplied by the frame norm at the reference point to give
the section weight. The phase/root choice does not affect the
coordinate monomial's absolute value.

Assume the core's raw volume has the bounded total mass specified in
the preceding dyadic proof. For arbitrary complex coefficients \(a_i\),
the triangle inequality and finite-dimensional Cauchy–Schwarz yield

\[
 \left\|\sum_i a_i\operatorname{Rem}_i\right\|_{L^2(\nu)}^2
       \leq C e^{-2\eta T}\sum_i|a_i|^2W_i^2.           \tag{9}
\]

Thus the error is uniform over coefficient tuples; it is not merely
a bound for each normalized individual section.
If the separate full-core Fourier/Gram argument gives
\(\|\sum_i a_i\operatorname{Lead}_i\|_{L^2(\nu)}^2
\geq c\sum_i|a_i|^2W_i^2\), choose \(T\) so
\(\sqrt C e^{-\eta T}\leq\sqrt c/2\).
The norm triangle inequality then gives

\[
 \left\|\sum_i a_iG_i\right\|_{L^2(\nu)}^2
                  \geq\tfrac c4\sum_i|a_i|^2W_i^2.     \tag{10}
\]

The raw-volume hypothesis and Fourier lower bound are separate here.
Pointwise Taylor convergence does not by itself establish either of
them, nor the probability mass of the selected union.

## Relation to the remaining geometric gates

For supplied convergent meromorphic bases and compact interior chamber
regions, ordinary analytic convergence now gives the uniform leading
remainder previously listed as an extra local input. The formal basis
construction alone would not give this estimate: both convergence
and the positive chamber/boundary margin were used.

The pointwise argument allows arbitrary positive SNC multiplicities
and zero transverse dimension. This does not extend the earlier
reduced-SNC dyadic Fourier/measure argument to repeated components.
It claims no uniform estimate as the chamber wall or simplex boundary
is approached, and no constant uniform over tensor degrees.
If there is no nonleading support, the remainder is zero and the
estimates hold immediately. All-zero coefficient tuples are included
in (9)–(10). The active book and all 42 statuses are unchanged.
