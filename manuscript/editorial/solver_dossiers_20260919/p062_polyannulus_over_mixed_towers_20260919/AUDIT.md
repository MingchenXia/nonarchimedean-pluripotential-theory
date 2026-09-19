# P06.2 polyannuli over mixed towers — dependency audit

Date: 19 September 2026

## Claim boundary

The corollary treats a globally coordinated finite product of standard
strict open annuli over the boundaryless top of a finite mixed exact tower
from `thm:p062-mixed-bundle-towers-over-curves`.  It gives a unique
coefficient formula whose base function and locally constant slope
coefficients live on the original published curve.

It does not treat a locally twisted annulus bundle, annular stages inside
the tower, arbitrary fibrations, or nonproduct germs.  Boundarylessness of
the tower top is imposed exactly where the rigid-base polyannulus theorem
requires it.

## Proof ledger

1. The mixed-tower theorem makes every continuous zero-current function on
   the tower top classically pluriharmonic.
2. The strengthened first-current conclusions in the three exact descent
   propositions, followed by curve first-current rigidity, give the second
   base hypothesis of `prop:p062-open-polyannulus-rigid-base`.
3. That proposition supplies the unique coefficient formula over the tower
   top and makes all slope coefficients locally constant.
4. The zero-current coefficient descends by the mixed-tower theorem.
   Connected fibres make each locally constant slope coefficient fibrewise
   constant.  The displayed fibres have rational points, so the local
   trivializations supply sections and hence a unique locally constant
   descent through the tower.
5. Harmonic pullback, harmonicity of logarithms of units, and the sheaf
   property give GJR harmonicity and local real-PL regularity.

No scalar extension of a current, residual-Picard vanishing, joint
trivialization of the mixed tower, or locally twisted annular coordinate is
used.  P06.2 remains open.
