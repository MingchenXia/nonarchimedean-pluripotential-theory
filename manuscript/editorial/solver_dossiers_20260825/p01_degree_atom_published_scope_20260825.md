# P01 degree--atom step: published-scope boundary

## Disposition

This note does **not** repair or resubmit the rejected P01 global converse.
It records the strongest source-backed frameworks found for the missing
curve degree--atom step and isolates what would still have to be proved for
the lifted curve produced in Gubler--Rabinoff, Theorem 5.3.

The controlling primary sources checked were:

- Gubler--Rabinoff, *On semipositive piecewise linear functions in
  non-archimedean analytic geometry*, arXiv:2503.05513v1, primary PDF
  SHA-256
  `2ac2d4bd2016c1692271b1a124013585c903288f5d182081dcdaaf824095eb1b`;
- Chambert--Loir--Ducros, *Formes diff\'erentielles r\'eelles et courants
  sur les espaces de Berkovich*, arXiv:1204.6277v2 dated 25 July 2025,
  primary PDF SHA-256
  `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.

No novelty or priority assertion is made.

## The maximally general published sign theorem on curves

Gubler--Rabinoff, Proposition 5.1 has exactly the following ambient scope:

- the ground field is an arbitrary complete nontrivially valued
  non-Archimedean field `k`;
- `X` is a **smooth, strictly `k`-analytic curve**;
- `u` is an arbitrary real PL function.

It proves that `u` is subharmonic at a point if and only if its residue line
bundle there is nef.  Thus the strongest published curve-level **sign
equivalence** found is already over arbitrary `k` and for real coefficients,
but it requires a smooth strict analytic curve.  The proof uses Wanner's
equivalence between subharmonicity and positivity of the CLD current on a
smooth curve.

For arbitrary `k`, the final paragraph of the proof passes to the completion
of an algebraic closure.  Nefness is checked after base change by GJR,
Proposition 7.6(2), and subharmonicity is checked after base change using
Thuillier's definition and preservation of harmonic functions.  This proves
the sign equivalence; it is not, by itself, an explicit coefficient-descent
formula at a specified point of the original curve.

## The exact published coefficient computation

The explicit atom calculation appears inside the algebraically closed part
of the proof of Gubler--Rabinoff, Proposition 5.1.  Its safe hypotheses are:

1. `k` is algebraically closed and complete;
2. `X` is a smooth strict analytic curve;
3. on a compact strict analytic neighbourhood `U`, the real PL function is
   represented by a formal model `(mathcal U, mathcal L)`;
4. the special fibre of `mathcal U` is reduced.

For each irreducible component `Y` of the reduced special fibre, there is a
unique analytic point `xi_Y` reducing to its generic point, and the proof
states that the discrete measure

```text
d'd''[u]|_U
```

has coefficient `deg_mathcal L(Y)` at `xi_Y`.  The paper cites CLD Section
6.9 for the more general current statement.  In this framework no unnamed
analytic multiplicity is needed: the reduced-model normalization makes the
coefficient exactly the residual degree in the stated convention.

Consequently, the safest published hypothesis for the **literal atom equals
degree** sentence used in the rejected packet is: algebraically closed
ground field, smooth strict curve, and a reduced-special-fibre formal model,
with the atom the unique component point `xi_Y`.  A stronger arbitrary-field
or nonreduced-model coefficient formula was not found in the cited source.

## What Theorem 5.3 does and does not provide

Gubler--Rabinoff, Theorem 5.3 starts with a good strict analytic space of
arbitrary dimension and lifts a proper residual curve to an irreducible
one-dimensional Zariski-closed analytic subspace `C`.  Its formal closure
has an irreducible residual component `Y'` which is proper and maps finitely
and surjectively to the original residual curve.  The proof applies GJR,
Lemma 7.4 to the **assumed semipositivity** of `h|_C` and then uses the
projection formula.

It does not assert that the lifted `C` is rig-smooth or smooth, and it does
not compute an atom of `d'd''[h|_C]` on this possibly singular curve.  Thus
Theorem 5.3 cannot be combined with Proposition 5.1 merely by identifying
both objects as curves.

Gubler--Rabinoff, Corollary 5.4 supplies a nearby but insufficient route.
After extending to an algebraically closed analytic field, it normalizes a
reduced curve; the normalization is rig-smooth because the ground field is
perfect, and semipositivity descends through the finite surjective
normalization.  To use this route from ambient current positivity one would
first need positivity to pull back to the normalization.  That pullback
stability is part of the very current-positivity problem under study, so
using it here would be circular.

## Integral and rational PL metrics

CLD Corollary 18.8.8 gives a different endpoint.  On a boundaryless analytic
space, for a line bundle with an **integral parlinear metric**, the following
are equivalent near a point:

1. the metrized line bundle is psh;
2. its first Chern current is positive;
3. its residual line bundle is numerically effective.

The equivalence of current positivity and residual numerical effectivity is
CLD Theorem 18.8.4.  Rational parlinear metrics reduce to the integral case
after a common positive tensor power.  This already closes the converse in
the integral/rational PL scope and does not require the lifted-curve route.
It does not cover a general real PL metric: there need not be a common tensor
power clearing its real coefficients.

## Exact unresolved bridge for the rejected candidate

The rejected rig-smooth ambient argument would become source-backed only
after one of the following genuinely additional inputs were established:

- prove that the particular lifted curve is smooth near the detecting point,
  then apply the arbitrary-field sign form of Gubler--Rabinoff,
  Proposition 5.1, with all point/base-change identifications checked; or
- after algebraically closed base change, prove that normalization preserves
  the positivity supplied by the ambient complete-intersection slice and
  descends the resulting sign to the original residual component; or
- provide a model-current formula for singular analytic curves over
  arbitrary complete fields and possibly nonreduced formal models, with an
  explicitly defined strictly positive multiplicity compatible with the
  finite projection formula.

None of these bridges is contained in the rejected packet or in the cited
statements above.  Therefore no revised global converse is submitted.

## Superseding source addendum, 25 August 2026

The preceding note records the sources known at the time of the rejected
packet.  A later audit of the 25 July 2025 CLD version located Theorem 18.4.7.
In pure dimension one its model-current formula applies to singular and
nonreduced analytic curves and identifies the current coefficient with the
corresponding residual degree, with the analytic-cycle multiplicities built
into the statement.  Thus the third bridge listed above is available in the
pure one-dimensional CLD framework.

This source correction does not validate the rejected global proof: a
rejected packet remains rejected.  The eventual solution of P01 uses the
independent ample-order-unit argument recorded in
`p01_current_positive_complete_intersection_slicing.md` and passed exact
production run `20260825T080059Z_80f35689475f`.  No novelty or priority
claim is made.
