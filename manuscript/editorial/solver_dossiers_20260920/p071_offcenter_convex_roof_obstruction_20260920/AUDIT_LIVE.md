# P07.1 off-centre convex-roof obstruction audit

Date: 20 September 2026

Status: verified and integrated into the live book.

## Claim boundary

The packet gives one smooth quadratic member of the displayed two-star
generator class and one exact five-atom ambient barycentre at which ordinary
Jensen inequality fails.  It rules out an unrestricted ambient-convex-roof
characterization and that proof route.

It does **not** contradict the mixed inequality centred at the double node,
does not claim that the current stratified comparison conditions are
insufficient, and does not retire P07.1.

## Exact checks

1. Every row and column of the mixed-coefficient matrix sums to zero.
2. The nine Hessian determinants form the displayed nonnegative matrix;
   their diagonal entries are positive.
3. The atom weights sum to one.
4. The grouped first moments have equal excess on branches one and three
   and leave exactly `(1/4) v_2`.
5. The grouped second moments leave exactly `2 w_2`.
6. The five exact values and their weighted sum give the positive defect
   `7169/688`.
7. All radii lie in the stated collar because `R>13/4`.

## Scope warning

The violated inequality is centred away from both node axes.  It is an
unrestricted ambient-barycentric inequality, not one of the already proved
mixed double-node inequalities.  The distinction is essential: the example
is itself a stage-zero generator.
