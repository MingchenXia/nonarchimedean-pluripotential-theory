# P06.2 integral polyannulus monodromy v64: live audit

## Claim boundary

The revision upgrades the overlap matrices from
`GL_s(R)` to `GL_s(Z)`.  It does so by proving the missing one-dimensional
unit lemma and then testing each matrix entry on a coordinate slice after a
complete algebraically closed extension of the fibre residue field.

The integral conclusion concerns only the linear monodromy.  The translation
terms remain arbitrary continuous zero-current real functions.  The result
does not trivialize the lattice local system, choose compatible global
annular coordinates, or identify the bundle with a global product.

## Proof ledger

1. On every strict closed subannulus, the Laurent--Gauss formula makes
   `-log|f|` concave piecewise affine with integral slopes.
2. Applying the same statement to the inverse unit makes the negative
   function concave as well; the radial function is therefore integral
   affine.
3. The maximum inequality for the unit and its inverse turns both
   inequalities into equality, extending the radial formula from the
   skeleton to the entire closed subannulus.
4. Dense value-group radii exhaust an open annulus over an algebraically
   closed nontrivially valued field; overlap uniqueness gives one global
   integer slope.
5. After extending a fibre residue field to a complete algebraically closed
   field and freezing all but one annular coordinate, each entry of the real
   overlap matrix is the slope of an analytic unit on an open annulus, hence
   an integer.
6. The reverse coordinate change is integer-valued too.  The already proved
   inverse identity therefore places the transition matrix in `GL_s(Z)`.
7. Triple-overlap uniqueness and the coefficient comparison from v63 then
   give the integral lattice local system, the real affine translation
   cocycle, and the parallel dual-real slope section.

## Model-verifier audit

The first frozen submission returned `wrong` with zero critical errors and
four gaps.  Every gap concerned unavailable dependency context: the exact
statements of the closed-annulus skeleton proposition, the log-smooth lemma,
the open-polyannulus product theorem, and the bundle hypotheses.  No
mathematical counterexample or failed inference was reported.  The repaired
packet spells out the bundle hypotheses in the principal statement, makes
the preservation of invertibility under pullback explicit, and supplies
verbatim book-local statements in `VERIFIER_DEPENDENCIES_LIVE.tex`.  The
original request and response remain archived without alteration.

The repaired frozen submission returned `correct`: one proof item checked,
zero critical errors, and zero gaps.  Its proof digest is
`1ab2003537c0eb427d88b8705672bde5089dd81899c9276a87ce0196a47af8ca`.
The repaired request, response, and safe response headers are archived in
`VERIFICATION_RUN_REPAIRED_20260920/`.

## Rejected inapplicable mechanism

The `real-to-integer-exponential-correction` method was checked and not used.
It starts with integral degree-two Cech cocycles, relatively compact real
degree-one primitives, and the vanishings
`H^2(-,R)=0` and `H^1(-,R/Z)=0`; it then corrects fractional primitives by
bounded vertex phases.  None of those hypotheses or operations occurs here.
The required integrality comes instead from Laurent exponents of analytic
units on annuli.

## Residual boundary

P06.2 remains open for arbitrary analytic germs, annular fibrations without
the displayed local product charts, strict-core-only equations, and the
other recorded residual cases.  The active-atom count is unchanged.
