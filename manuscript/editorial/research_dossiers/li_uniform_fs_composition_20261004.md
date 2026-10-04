# Composing the conditional estimates into uniform FS approximation

Date: 4 October 2026. This book-external derivation composes the fixed
matrix, Bergman, generic Fourier and uniform domination estimates.
Their geometric hypotheses remain explicit. It supplies the order of
limits and bounds for the FS coefficients, without promoting a general
CY theorem, changing a problem status or claiming a verifier receipt.

## Exact fibrewise inputs

Fix a smooth projective polarized family of dimension \(n\geq1\)
with connected complex fibres.
Let \(T=-\log|t|\geq1\), let \(h\) be a fixed model reference metric on
the punctured family, and set \(\theta_t=i\Theta_h|_{X_t}\).
Use \(dd^c=i\partial\bar\partial\), so a norm potential \(\varphi_t\)
has curvature \(\theta_t+2dd^c\varphi_t\). Write
\(\omega_t=\theta_t/(2T)\), \(u_t=\varphi_t/T\).
Assume \(\omega_t\) is Kähler, \(\varphi_t\) is smooth,
\(u_t\in\operatorname{PSH}(X_t,\omega_t)\), and

\[
 \sup u_t=0,\quad
 \mu_t=\frac{(\omega_t+dd^cu_t)^n}{\int_{X_t}\omega_t^n}
 \text{ is absolutely continuous},\quad
 \int e^{-\alpha v}d\mu_t\leq A
 \quad(v\in\operatorname{PSH}(X_t,\omega_t),\ \sup v=0),     \tag{1}
\]

with fixed \(\alpha,A>0\). The fixed factor two relates this convention
to references using norm rather than squared-norm potentials.
The preceding stability/truncation derivation gives
\(-C_\varphi\leq u_t\leq0\).

At every sufficiently large **fixed** degree \(l\), assume:

1. The section module has finitely many convergent meromorphic chamber
   bases \(s_i^{(k)}\), \(1\leq i\leq d_l\), and spans the whole fibre
   section space on one small punctured disc. That degree is globally
   generated there. Their coefficient rows in a reference basis form
   one fixed meromorphic matrix \(A_l(t)\).
2. For every sufficiently small \(\eta>0\), there are measurable disjoint
   chamber parts \(U_k\), with union \(U\) and
   \(\mu_t(U)\geq1-\eta\), on which the weighted estimate is

\[
 I_t(s):=\frac1{2l}\log\int|s|_{h^l}^2e^{-2l\varphi_t}d\nu_t
 \geq\frac1l\log|a_i^{(k)}s_i^{(k)}(\zeta)|_{h^l}
          -\varphi_t(\zeta)-E_{l,\eta}(t)
 \quad(\zeta\in U_k),                                    \tag{2}
\]

   uniformly in the section and its coefficient tuple.
   Here \(E_{l,\eta}(t)/T\to0\) after fixing \(l,\eta\).
   The parent-cover derivation gives \(E=C_{l,\eta}\sqrt T\).
3. For every \(z\in X_t\), a section \(s\) with \(s(z)\ne0\) satisfies

\[
 I_t(s)\leq\frac1l\log|s(z)|_{h^l}-\varphi_t(z)
                     +C_BT/l,                           \tag{3}
\]

   with \(C_B\) independent of \(l,t,z\). This is the Bergman input with
   its projective-model, meromorphic-volume and oscillation hypotheses.

The measure in (2)–(3) is the same positive smooth raw volume
\(d\nu_t\) on each fibre; it is not
silently replaced by \(\mu_t\). All fixed-degree radii may depend on
\(l,\eta\). The uniform Skoda constants in (1) do not.

## Fixed inverse-minor family and inactive chamber rows

For each nonzero maximal minor of \(A_l\), take its inverse columns,
viewed as meromorphic global sections \(S_\alpha\). These give a fixed
finite family, independent of \(U,\eta,t,z\). It contains a basis of
the section space, so has no common zero on each sufficiently small
globally generated fibre.

Empty or zero-\(\mu_t\)-mass chamber parts can be omitted from \(U\).
This does not change the mass estimate. Retain the coefficient rows
for every positive-mass \(U_k\). At least one such part exists for
\(\eta\leq1/2\), and its full basis of rows makes this active submatrix
have rank \(d_l\). Thus the inverse-minor replacement also applies if
some chamber parts disappear:

- minimize the minor-order expression over minors using active rows;
- take the candidate from the same full fixed family;
- use the same finite collection of Cramer unit bounds.

All active row subsets form a finite set. The bound \(C_l\) and common
punctured radius can therefore be fixed in advance for all of them.
An unconstrained row is omitted, rather than assigned an infinite real
weight. Because a nonzero holomorphic section has a zero set of
absolutely continuous measure zero, the suprema below are finite on
every positive-mass part.

## Potential upper bound from replacement

Choose the Bergman section at \(z\), and put
\[
 b=\frac1l\log|s(z)|_{h^l}-\varphi_t(z),\qquad
 F_{ik}=\sup_{U_k}\left(\frac1l\log|s_i^{(k)}|_{h^l}
                                      -\varphi_t\right).
\]

Equations (2)–(3) imply on all active rows
\[
 |a_i^{(k)}|
 \leq\exp\{lb+C_BT+lE_{l,\eta}(t)-lF_{ik}\}.               \tag{4}
\]

These are finite real power constraints, since \(|t|=e^{-T}\).
Apply the fixed-matrix replacement to (4), with evaluation at \(z\).
It produces \(R=c|t|^\nu S_\alpha\), with the same nonzero value at \(z\),
and active coefficients bounded by \(C_l\) times (4). The scalar
\(|t|^\nu\) is a comparison factor at the fibre, not a meromorphic
function being added to the fixed family.
The triangle inequality, (4) and the definition of \(F_{ik}\) give
\[
 \sup_U\left(\frac1l\log|R|_{h^l}-\varphi_t\right)
 \leq b+C_BT/l+E_{l,\eta}(t)+\log(d_lC_l)/l.
\]

At \(z\), \(R(z)=s(z)\). Cancel the nonzero scalar \(c|t|^\nu\) from
both sides and set
\[
 c_\alpha(t)=\sup_U\left(\frac1{lT}\log|S_\alpha|_{h^l}-u_t\right),
 \qquad
 \psi_{l,\eta,t}
   =\max_\alpha\left\{\frac1l\log|S_\alpha|_{h^l}-Tc_\alpha(t)\right\}.
                                                               \tag{5}
\]

The family has no common zero; hence this is continuous and
\(\psi_{l,\eta,t}/T\) is \(\omega_t\)-psh. Its definition gives
\(\varphi_t\geq\psi_{l,\eta,t}\) on \(U\). Choosing the replacement
at each point proves
\[
 \frac{\varphi_t-\psi_{l,\eta,t}}T
 \leq C_B/l+E_{l,\eta}(t)/T+\log(d_lC_l)/(lT).             \tag{6}
\]

The lower bound supplied by the preceding max-truncation/strict-sublevel
proof is
\[
 \frac{\varphi_t-\psi_{l,\eta,t}}T\geq-C_D\eta^{1/(2n)},    \tag{7}
\]

for \(\eta\) below a fixed threshold depending only on (1) and \(n\).
Its constant does not acquire degree dependence through an assumed
comparison-potential lower bound.

## Order of limits

For each fixed large \(l\), choose \(0<\eta_l\leq1/2\) below that
threshold with \(C_D\eta_l^{1/(2n)}\leq1/l\).
Then choose \(T_l\) sufficiently large that the fixed-degree bases,
generic estimates and matrix bounds hold, and
\[
 E_{l,\eta_l}(t)/T\leq1/l,\qquad
 \log(d_lC_l)/(lT)\leq1/l.
\]

If the logarithm is negative, its upper bound already suffices; one
may instead use its positive part. From (6)–(7),
\[
 \sup_{X_t}|u_t-\psi_{l,\eta_l,t}/T|
      \leq C_*/l\qquad(T\geq T_l),                        \tag{8}
\]

with one \(C_*\) independent of \(l,t\).
The radii \(r_l=e^{-T_l}\) may decrease with degree. The argument
never requires a radius uniform over all degrees. Wall deletions,
chart choices and Fourier constants are settled before shrinking
that degree's radius. This is the required conditional uniform FS
approximation.

## Bounded coefficients at every fixed degree

Write \(f_{\alpha,t}=(lT)^{-1}\log|S_\alpha|_{h^l}\) and
\(M_{\alpha,t}=\sup_{X_t}f_{\alpha,t}\).
The singular test \(f_{\alpha,t}-M_{\alpha,t}\) is \(\omega_t\)-psh
with zero supremum. Applying (1) on \(U\) yields
\[
 \sup_U f_{\alpha,t}
 \geq M_{\alpha,t}-\alpha^{-1}\log\frac{A}{\mu_t(U)}
 \geq M_{\alpha,t}-\alpha^{-1}\log(2A).
\]

Since \(-C_\varphi\leq u_t\leq0\), (5) gives
\[
 M_{\alpha,t}-\alpha^{-1}\log(2A)
 \leq c_\alpha(t)\leq M_{\alpha,t}+C_\varphi.              \tag{9}
\]

This avoids an unsupported lower bound for the section on every point
of a generic region; its zero locus is permitted.

The fixed meromorphic-model section input also bounds \(M_{\alpha,t}\).
More precisely, suppose a power \(h^k\) extends as a smooth metric on
a model bundle \(\mathcal A\), and \(S_\alpha^k\) is meromorphic as a
section of \(\mathcal A^l\), with poles only over zero. Multiplication
by some \(t^p\) makes it holomorphic on the compact model region,
giving a polynomial upper bound on its fibre supremum. For a lower
bound, choose a generic smooth point of a central component, away
from the other components and horizontal zeros. Locally its nonzero
section has form \(z_0^a f(z_0,w)\), \(f(0,w_0)\ne0\), and
\(t=z_0^{b_0}\) after absorbing a unit. Points with \(w=w_0\) and
any root \(z_0^{b_0}=t\) give a lower bound by a fixed positive
multiple of \(|t|^{a/b_0-p}\). Taking the \(k\)-th root transfers
this to \(|S_\alpha|_{h^l}\).

Thus \(M_{\alpha,t}\), and by (9) \(c_\alpha(t)\), are bounded
for every fixed \(l,\alpha\). No bound uniform over degrees is needed.
Along any scalar sequence \(t_j\to0\), a diagonal subsequence makes
all coefficients converge, since there are finitely many per degree
and countably many degrees. This is compactness in real coefficient
spaces, not sequential compactness of the NA central fibre.

The hybrid FS weight at zero is **\(lc_\alpha(0)\)** in the
degree-\(l\) max convention:
\[
 v_{l,0}=\max_\alpha\left\{\frac1l\log\|S_\alpha\|_{\rm NA}
                                         -c_\alpha(0)\right\}.
\]

Equating the degree-\(l\) weight to \(c_\alpha(0)\) instead would lose
a factor \(l\). Hybrid continuity, MA passage and uniqueness still
require their separate topological and primary-source inputs.
All stated geometric gates, the active book and the 42 statuses are
preserved. No external verifier or finite computation is claimed.
