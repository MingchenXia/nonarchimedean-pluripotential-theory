# P18.1: normalized Favre--Pille-Schneider hybrid continuity

**Audit date:** 25 August 2026
**Current verdict:** production `final/correct`, zero errors and gaps
**Live status:** integrated in Chapters 66 and 72; exact-current gate passed
run `20260825T043840Z_d77f7f93aeb0`, final `correct`, 0/0

## Exact problem decided

The residual problem fixes a continuous model metric
\(\phi_{\mathcal L}\), assumes a continuous semipositive metric \(\phi\)
with logarithmic growth and continuous \(\phi^{\mathrm{NA}}\), and imposes
\[
 \sup_{X_t}(\phi_t-\phi_{\mathcal L,t})=0,
 \qquad
 \sup_{X_{\mathbf C((t))}^{\mathrm{an}}}
 (\phi^{\mathrm{NA}}-\phi_{\mathcal L}^{\mathrm{NA}})=0.
\]
It asks whether the canonical hybrid psh metric is continuous.  The frozen
packet gives a negative answer already on
\(\mathbf P^1_{\mathbf C}\times\mathbb D^*\) with the product
Fubini--Study model metric.

## Construction

Reuse the verified scalar subharmonic function \(u\leq0\) with
\[
 \nu_0(u)=0,
 \qquad
 u(\rho_m)=-s_m+O(1),
 \qquad
 u(-\rho_m)=O(1),
 \qquad
 \log|\rho_m|=-s_m.
\]
Instead of adding \(u\) as a base scalar, define the homogeneous metric
weight
\[
 \phi([Z_0:Z_1],t)
 =\frac12\log\bigl(|Z_0|^2+\exp(2u(t))|Z_1|^2\bigr).
\]
Its relative potential is
\[
 \psi=\frac12\log
 \frac{|Z_0|^2+\exp(2u)|Z_1|^2}{|Z_0|^2+|Z_1|^2}.
\]
Then \(u\leq\psi\leq0\), with equality \(\psi=0\) at \([1:0]\) and
\(\psi=u\) at \(p_*=[0:1]\).

## Hostile audit

### Psh extension versus continuity

On \(Z_1\ne0\) and \(Z_0\ne0\), respectively, the local weights are
\[
 F_1=\frac12\log(|z|^2+\exp(2u)),
 \qquad
 F_0=\frac12\log(1+\exp(2u)|w|^2).
\]
Writing
\(\chi(x,y)=\tfrac12\log(\exp(2x)+\exp(2y))\), one has
\(F_1=\chi(\log|z|,u)\) and
\(F_0=\chi(0,u+\log|w|)\).  The function \(\chi\) is convex and
coordinatewise nondecreasing, hence preserves psh tuples.  Since \(u\) is
finite everywhere, both weights are finite everywhere and obey the correct
transition law.  Their failure to be continuous at \((p_*,0)\) is allowed:
the source definition of a psh metric on the model requires psh local
weights, not continuity or local boundedness below.

### Every higher-model divisor

For a prime vertical divisor \(E\) on any dominating model, at its general
point \(t=\zeta^{b_E}h\) with \(h\) a unit, so
\[
 \nu_E(u\circ\pi)=b_E\nu_0(u)=0.
\]
If the general point is read in the \(Z_0\ne0\) chart, then \(F_0\geq0\),
so \(\nu_E(F_0)=0\).  In the \(Z_1\ne0\) chart, \(F_1\geq u\circ\pi\),
and Lelong monotonicity gives
\(0\leq\nu_E(F_1)\leq\nu_E(u\circ\pi)=0\).  Thus every generic Lelong
number of \(\phi\) is zero.  The smooth Fubini--Study reference also has
zero generic Lelong numbers.  In Pille-Schneider's exact normalization,
\[
 \psi^{\mathrm{NA}}(v_E)
 =\frac{\log r_0}{b_E}\nu_E(\phi)=0.
\]
The uniqueness clause of Theorem 3.10 therefore gives the full equality
\(\phi^{\mathrm{NA}}=\phi_{\mathrm{FS}}^{\mathrm{NA}}\), rather than
only equality on a selected skeleton.

### Normalization and discontinuity

The inequalities for \(\psi\), together with \(\psi([1:0],t)=0\), give
\(\sup_{X_t}\psi_t=0\) for every \(t\ne0\).  Equality of the
non-Archimedean metrics gives the endpoint normalization.  Along the
constant section \(p_*=[0:1]\), the hybrid difference is
\[
 \frac{\log r_0}{\log|t|}\psi(p_*,t)
 =\frac{\log r_0}{\log|t|}u(t).
\]
The two sequences \(t=\rho_m\) and \(t=-\rho_m\) converge to the same
non-Archimedean section point, but the displayed quantity tends to
\(\log r_0\) and \(0\).  Pille-Schneider's Theorem 3.13 ensures that this
is the canonical hybrid psh gluing; no arbitrary set-theoretic gluing is
used.

## Boundary and ill-posedness tests

* At \([1:0]\), the relative potential is identically zero; this is the
  point that enforces the complex-fibre normalization.
* At \([0:1]\), the relative potential is exactly \(u\); this is the point
  that detects discontinuity.
* At a point with both homogeneous coordinates nonzero, the deep-well
  value of \(\psi\) stays bounded, so this particular section does not
  detect the jump.  The theorem only claims the two limits at \([0:1]\).
* The metric is smooth on the punctured total space, so no continuity
  ambiguity occurs in the hypotheses.
* Differences of two metrics are global functions, so the fibrewise
  suprema are frame independent.  The non-Archimedean difference is zero,
  hence its supremum is unambiguous.
* The logarithmic radial endpoint skill does not apply: there is no kernel,
  absolute-value estimate, or Hölder endpoint.  No conclusion from that
  skill is imported.

## Authenticated source dependencies

1. L. Pille-Schneider, *Global pluripotential theory on hybrid spaces*,
   arXiv:2209.04879v2.  Local primary PDF SHA-256:
   `55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7`.
   Used: Proposition 2.25, Definition 3.9, Theorems 3.10 and 3.13, and
   Question 3.18.
2. C. Favre, *Degeneration of endomorphisms of the complex projective
   space in the hybrid space*, arXiv:1611.08490v2.  Local primary PDF
   SHA-256:
   `137ddb0245b4f09ff8b7a4a2880bd3846f146cd013f2ce9563d7f90f45ea1a5f`.
   Used: Definition 4.1 and its following remark, and Question 1.

## Frozen production object

* statement SHA-256:
  `070e264c3ef1d1e6c436eb7215ee50e1801bfeab667159234e7d755bc69a52f8`;
* proof SHA-256:
  `0e9c8fdf755a714eccc2c3bc0215d8c43ad05c04ab664077205bfa552dd1ef90`;
* request SHA-256:
  `93a684c37e273851661762bb7af2827ad41cdbc512538136ba6dd2fe4b213b4f`;
* run `20260825T035945Z_070e264c3ef1`;
* item `pi_db89dd432acabcf33a3f2272`.

Production returned `final/correct`, with zero critical errors and zero gaps,
after 518.835 seconds.  The normalized family stage is now integrated in
Chapter 66, and the residual problem has been removed from Chapter 72.  At
that integration stage, the book-wide inventory was 19 problem environments
and 60 active atoms.  The
adapted exact-current theorem and proof subsequently passed production run
`20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`, with final verdict `correct`, zero critical
errors, and zero gaps; their exact proof SHA-256 is
`992a686618355605e4f889564c402f5b2c6ff18db70762daed2dbcf4d09fdbad`.
