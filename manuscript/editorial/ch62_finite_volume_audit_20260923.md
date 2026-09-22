# Chapter 62: finite constraints and the volume formula — 23 September 2026

## Corrected proof obligations

The finite-constraint envelope now has an explicit continuous PL obstacle.
The earlier one-line appeal to MPWN Lemma 7.1.5 concealed the extra vertices
of a common snc model. Assigning zero at those vertices can impose unintended
constraints. The revised argument uses the already proved finite point bound
sup(phi) <= t_1 + T(v_1), assigns that bound to all unprescribed vertices,
and uses the coefficients b_j a_j in the vertical divisor. Convexity on
faces and the retraction majorant identify the two candidate sets.
Envelope continuity therefore preserves the prescribed inequalities.

The Legendre reduction is proved in both directions directly from energy
monotonicity and the variational definition. It does not assume that every
constraint is saturated. Attainment uses the continuous Calabi--Yau solution
and domination. Translation allows t_1 = 0; the former assertion of
"exactly one" redundant direction is removed because inactive constraints
can create more maximizing parameters. Zero weights contribute nothing
to the linear term but may still affect the fixed-parameter envelope.
Distinct divisors and a nonempty list are explicit. Repeated valuations in
a measure presentation are combined before applying the formula.

The volume proof now includes a finite pseudoeffective threshold.
Pairing the residual class with a Kähler (n-1)-power gives a quantity that
is eventually negative, since every prime divisor has strictly positive
degree. Monotonicity and closedness give a closed parameter interval.
Convexity of the positive-part coefficients proves bigness below its
endpoint; the endpoint is nonbig by openness. This also covers n = 1
and exceptional divisors on the chosen smooth Kähler modification.

Siu decomposition and descent of currents in the pullback class identify
the nonempty Lelong-constraint locus with that interval. After removal
of the prescribed divisorial current, a minimal residual potential supplies
a candidate and proves minimal singularities of the envelope's residual.
Non-pluripolar mass is therefore the volume of the residual class.
The test-curve/ray identification remains an explicit source input.
The energy integrand is zero on a lower half-line and bounded on the
remaining finite interval. The endpoint has zero volume, and its value
at a single parameter does not affect the integral. The lower integration
constant cancels exactly.

The one-divisor specialization now follows from translation and the
Legendre formula, with a separate elementary saturation argument.
The beta formula differentiates the optimized value at fixed divisors
and weights; no derivative/supremum or derivative/integral interchange
is asserted.

## Curve check

For the two points 0 and infinity on degree-one P1, the residual mass is

    (1 - lambda_+ - (lambda-b)_+)_+.

Its integral gives

    f(0,b) = b+1/2                        if b <= -1,
             1/4+b/2-b^2/4              if -1 <= b <= 1,
             1/2                        if b >= 1.

For weights (p,1-p), the maximum of f(0,b)-(1-p)b is
(p^2+(1-p)^2)/2. For 0 < p < 1 the optimizer is b = 2p-1;
at p = 1 the full half-line b >= 1 maximizes, and at p = 0 the
half-line b <= -1 does. The one-point constraint is genuinely inactive
when b > 1. The independent tree calculation has slopes -p and -(1-p)
on the two unit segments and gives the same dual energy.

Exact rational arithmetic checked 65 parameter values across both break
points, and 17 weights including both zero-weight endpoints. Direct
piecewise integration agrees with the stated polynomial; the separate
tree energy agrees with the Legendre value. These computations check
the illustrative example and do not replace the general proof.

## Exact sources and verification limits

[MPWN25, arXiv version 1](https://arxiv.org/html/2509.09442v1):
Lemma 7.1.5 supplies the finite-constraint assertion; Section 10.1,
Lemma 10.1.1, Theorem 10.1.2, and Corollaries 10.1.3--10.1.4 supply
the ray identification, volume formula and variational application.
The explicit treatment of unprescribed vertices fills in the obstacle
construction; no claim is made that assigning zero there would suffice.

The [published DXZ article](https://ems.press/content/serial-article-files/50355?nt=1),
Comment. Math. Helv. 100 (2025), 269--322, DOI 10.4171/CMH/586,
was checked at equation (5), page 279, and Theorem 2.6(iii), page 282
with its proof on page 283. The rendered theorem page confirms the
positive starting-mass and finite-energy hypotheses. With theta = omega
and starting potential zero, the starting mass is V and the identity has
the exact normalization used here. The existing bibliography key DXZ23
already points to this published 2025 article and is retained.

Publisher PDF SHA-256:
`467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e`.
The downloaded article is held only in temporary storage.

This is a local proof reconstruction and source audit. It does not
constitute a new production Rethlas gate or an independent-agent audit.
The general Kähler radial correspondence and test-curve identification
remain imported inputs; no research-frontier question is closed.
The normalized-model stability scope is unchanged.

## Second pass and final validation

The second mathematical pass checked the complete vertex set,
multiplicities, nonempty candidate sets, both variational inequalities,
attainment, zero weights, the single-divisor saturation, finite threshold,
minimal residual singularities, endpoint mass, and fixed-measure class
variation. It made bigness below the threshold explicit and clarified
that a zero weight removes only the linear term. Visual review removed
an introductory sentence stranded before its formula on the next page.

The actual final edited section passes the strict writing audit with
zero errors and zero warnings. The full source closure has 389 TeX
files and 11,511 unique labels, with no missing input, duplicate label,
dangling reference or structural defect. The open-problem inventory
remains 46 active atoms in 14 environments, with tiers (0,5,8,16,17).

Both full-book builds passed. The final PDF has 3,925 pages and
18,632,053 bytes, with no unresolved reference or citation and no
horizontal or vertical overflow. Final physical pages 3358--3362
(printed 3290--3294) were rendered and inspected, covering the whole
revised section and the following section boundary. The source diff
is whitespace-clean.

PDF SHA-256:
`f79dbaa9cf4d613079e21f496fb1ff3d2bda5a8d9fcfaf921e5fd73056116aba`

Chapter 62 SHA-256:
`7933c3be3f19f45eb4367851e39c963d106fde62297236228389df78006835b5`

The whole Chapter 62 source outside the revised section is byte-identical
to its pre-edit version. The frozen factor-n block retains SHA-256
`204ca71038019e4ca4b24aba3b89e54965ef8586fe433a511619e4a54933ee25`.
The author's CURVE_PSH.tex is byte-identical to the supplied download
and retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.
No other chapter, frozen research packet, verifier record, bibliography
database or dated release artifact was changed. The current generated
PDF remains an ignored local build artifact.
