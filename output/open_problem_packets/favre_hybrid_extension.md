# Favre--Pille-Schneider hybrid continuity: negative solution

**25 August 2026 controlling update.**  Both the literal packet and its
zero-supremum normalized strengthening are solved negatively.  The smooth
product counterexample in
`thm:hybrid-endpoint-continuity-counterexample` passed production Rethlas
first as a base-scalar packet in run
`20260825T030402Z_13e01361eeff`.  Its stronger fibre-dependent log-sum-exp
form passed run `20260825T035945Z_070e264c3ef1`, item
`pi_db89dd432acabcf33a3f2272`; the adapted live theorem-and-proof bytes then
passed run `20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`.  All returned `final/correct`, zero critical
errors, and zero gaps.  The stronger form has zero supremum relative to the
product Fubini--Study metric on every complex fibre and on the
non-Archimedean fibre.  It also satisfies Favre's three intrinsic conditions
while failing to be uniform, so the two source formulations are refuted
separately rather than identified without proof.

Address the metric problem in Pille-Schneider, *Global pluripotential theory
on hybrid spaces*, Question 3.18, which the source says is taken from Favre's
Question 1.  Favre's literal Question 1 asks whether a function is uniform
if and only if it is continuous near \(\overline X_r\), its curvature on
\(X_r\) is represented by a positive closed \((1,1)\)-current \(T\), and the
generic-Lelong function \(g_T\) extends continuously to
\(X_{\mathbf C((t))}^{\mathrm{an}}\).  Do not identify that intrinsic
characterization with the following metric formulation without proving their
equivalence.  In Pille-Schneider's metric formulation, let
\((X,L)\to\mathbb D^*\) be a polarized projective degeneration.  Let \(\phi\)
be a continuous semipositive metric with logarithmic growth, and assume that
its associated non-Archimedean metric \(\phi^{\mathrm{NA}}\) is continuous.
The answer is no: even for
\(\mathbf P^1_{\mathbf C}\times\mathbb D^*\), a smooth semipositive metric
can have logarithmic growth and continuous Fubini--Study non-Archimedean
endpoint while its canonical hybrid psh extension is discontinuous.

The psh property of the glued metric is already Pille-Schneider Theorem 3.13;
continuity was the additional assertion asked there and is false in this
generality.  Theorem 5.1 concerns the particular
family of fibrewise Kähler--Einstein metrics on a degeneration of canonically
polarized manifolds admitting semistable reduction; it is not a continuity
theorem for every semipositive metric on such a degeneration.  Theorem 4.11
then gives weak continuity of the diagonal Monge--Ampère measures in the
smooth, relatively ample hybrid setting for one continuous hybrid psh metric.
Do not present any of these restricted theorems as the general continuity
statement.

The former replacement fixed a continuous model reference metric and imposed
zero-supremum normalization on every complex fibre and on the
non-Archimedean fibre.  The stronger example satisfies exactly those
hypotheses: if
\[
 \phi=\frac12\log\bigl(|Z_0|^2+\exp(2u(t))|Z_1|^2\bigr),
\]
then its relative potential lies between \(u\) and \(0\), equals \(0\) at
\([1:0]\), and equals \(u\) at \([0:1]\).  Hence the fibrewise suprema are
zero while the two verified scalar-well sequences still give distinct
hybrid limits.  The normalized environment and atom are therefore retired;
there is no active P18 replacement.

Keep the psh gluing theorem, canonically polarized positive case, the two
counterexample scopes, and weak continuity of
Monge--Ampère measures logically separate.
