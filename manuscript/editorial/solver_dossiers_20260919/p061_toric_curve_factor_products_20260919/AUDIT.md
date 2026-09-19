# P06.1 toric products with arbitrary curve factors — dependency audit

Date: 19 September 2026

## Claim boundary

The corollary treats ordinary open analytic subspaces of a product of a
split toric variety, an arbitrary finite family of good strict analytic
curves, and a final good strict factor whose reduction is quasi-smooth.  It
also treats analytic local models of such products and toric forms that
split after a complete extension obtained by completing an algebraic field
extension.

The conclusion is local real piecewise linearity and
Gubler--Jell--Rabinoff harmonicity for every classically pluriharmonic
function.  It does not cover a higher-dimensional reduced singular factor
outside the toric factor, a toric form without the stated algebraic
splitting extension, or a nonproduct singular germ.

## Proof ledger

1. At an arbitrary toric orbit, `eq:p061-orbit-product-chart` writes a
   principal open as a pointed transverse toric factor times the split orbit
   torus.
2. Regroup the orbit torus with the final factor.  On strict affinoid charts,
   `lem:p061-product-factor-reduction` gives a nilpotent closed immersion
   from the orbit torus times the reduction of the final factor.  The source
   is quasi-smooth and therefore reduced, so it is the reduction of the
   regrouped factor.
3. Apply `prop:p061-parameterized-toric-fixed-fibre`.  After shrinking to a
   product neighbourhood, the original function is pulled back from a
   classically pluriharmonic function on the product of the curve factors
   and the regrouped final factor.
4. `thm:p061-arbitrary-curve-factors-ph-rpl` makes that parameter function
   real-PL and harmonic.  Pullback stability gives both conclusions for the
   original function.
5. For an algebraic-split toric form, scalar extension reaches the split
   case.  Gubler--Jell--Rabinoff ground-field descent returns the real-PL
   function to the ground field, and the established two-sign comparison
   returns harmonicity.

This is a new verified positive range, not a closure of P06.1.  The problem
and the 46-active-atom inventory count remain unchanged.
