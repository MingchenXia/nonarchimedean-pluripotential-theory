# Audit: residual-Picard curves with interleaved annular stages

Date: 20 September 2026

## Scope and claim boundary

This packet proves a new P21.3 subcase in which standard strict
open-polyannulus product stages may occur at arbitrary levels among the four
previously established exact bundle types.  A single analytic open cover of
the residual-Picard curve base must coordinate every annular stage after base
change.  The radii, coordinates, and product trivializations may depend on the
cover member and need not agree on overlaps.

The conclusion is ordinary CLD smoothness with zero smooth Hessian for every
continuous zero-current function on the tower top.  It yields whole-space,
specified-cover, and every-open basis versions of Bedford--Taylor
independence against every positive closed ordinary CLD current.

The theorem does not cover annular charts available only over unrelated opens
of intermediate tower levels, does not remove the residual-Picard condition,
and does not assert a global logarithmic coefficient formula.  It narrows
P21.3 without retiring that atom; the inventory remains at 46 active atoms.

## Proof ledger

1. Restrict the zero-current equation to the inverse image of a member of the
   fixed analytic cover of the curve base.
2. Apply the verified interleaved-tower theorem to obtain the unique local
   formula consisting of a curve coefficient and logarithmic terms from all
   annular stages.
3. Use the residual-Picard criterion to make the curve coefficient ordinary
   CLD-smooth with zero smooth Hessian.
4. Use logarithmic smoothness and functorial CLD pullback to give the same
   property to every annular term, including all later pullbacks through the
   tower.  Locally constant slope coefficients add no derivative terms.
5. Glue only the local regularity assertion, not the coordinate formulas.
6. Apply the established smooth-zero-Hessian Bedford--Taylor criterion;
   ordinary covers and bases give the two localized consequences.

The empty set of annular stages is handled by interpreting the double sum as
zero.  No compatibility of local coefficients or coordinates is used.

## Model-backed verification

- First dependency-closed packet: verdict `correct`, 0 critical errors and
  0 gaps; checked item `pi_d060e218e820092ced6f15ba`.
- Final polished packet, after the explicit empty-annular-stage convention:
  verdict `correct`, 0 critical errors and 0 gaps; checked item
  `pi_2d2fe2ff46ca42941728201a`, proof digest
  `7388bb4c50e8a688e70730bacace7d7b7d366729870ab2b419441b1f8699e7cf`.

The exact requests, responses, and HTTP headers for both runs are retained in
this dossier.
