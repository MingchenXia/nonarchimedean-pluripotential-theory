# Audit: residual-Picard towers with a locally twisted open-polycylinder bottom

Date: 20 September 2026

## Scope and claim boundary

This packet proves a new P21.3 subcase.  The bottom of the tower is only
*analytically locally* a product of a residual-Picard curve with finitely many
standard strict open annuli and, optionally, finitely many strict open discs.
A finite mixed exact tower of the four already established bundle types may be
placed above it.  The conclusion is ordinary CLD smoothness with zero smooth
Hessian, followed by the whole-space, cover, and basis Bedford--Taylor
consequences.

The result deliberately does not assert a global logarithmic coefficient
formula.  It assumes neither compatibility of the annular coordinates on
overlaps, nor vanishing of integral monodromy, nor vanishing of the zero-current
radiance class.  It therefore narrows P21.3 without retiring that open problem;
the atomic inventory remains at 46 active atoms.

## Proof ledger

1. Apply the mixed exact-bundle tower transfer to descend the zero-current
   function uniquely to the bottom space.
2. On a bottom chart, successively remove the open-disc factors by open-disc
   descent; the statement includes the empty disc product when `r=0`.
3. Apply the polyannulus-over-a-curve theorem to obtain a curve term plus
   locally constant annular slopes multiplying `log|T_i|`.
4. Use the residual-Picard curve criterion on the curve term and logarithmic
   smoothness on each invertible annular coordinate.
5. Pull ordinary CLD smoothness and the zero smooth Hessian back through the
   chart and then through the upper tower.
6. Apply the established smooth-zero-Hessian Bedford--Taylor invariance
   corollary; localization gives the cover and basis forms.

All intermediate product bases used during disc descent are explicitly good,
topologically separated, pure, strict, and positive-dimensional.  The cases
`ell=0`, `r=0`, and disconnected charts with merely locally constant slope
functions are accounted for.

## Model-backed verification history

- Initial principal-only packet: verdict `wrong`, 0 critical errors and 7 gaps.
  Every gap requested a materialized dependency statement; no mathematical
  contradiction was reported.  Checked item:
  `pi_fc1116220314a912c78ae2b6`.
- Dependency-repaired packet: verdict `correct`, 0 critical errors and 0 gaps.
  Checked item: `pi_c959df3e8b6f425f0f50d62e`.
- Final polished packet, after the edge-case and presentation edits: verdict
  `correct`, 0 critical errors and 0 gaps.  Checked item:
  `pi_98845d03220a289bf9c33f9a`; proof digest
  `d5ca1f381c3b5ca4de2d9582adb199e37d9069611dfa1d73c42da7ffd3da55dc`.

The request, response, and HTTP-header records for all three runs are retained
beside this audit.
