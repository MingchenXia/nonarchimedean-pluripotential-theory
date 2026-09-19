# Sources and dependency map

Date: 20 September 2026

No new external theorem or bibliographic citation is introduced by this
packet.  Its inputs are results already proved and integrated in the book.

## Book-local dependencies

- `prop:p213-residual-picard-smooth-curve`: the residual-Picard criterion for
  continuous zero-current functions on the curve base.
- `prop:p062-open-disc-descent`: descent across one strict open-disc factor.
- `thm:p062-open-polyannulus-products-over-curves`: local decomposition over a
  curve into a base term and locally constant annular slopes times
  logarithmic coordinates.
- `prop:p062-mixed-exact-bundle-tower-transfer`: unique descent through a
  finite tower of open-polydisc, projective-space, smooth proper split-toric,
  and proper smooth connected-curve bundles.
- `lem:ch15-log-smooth`: ordinary CLD smoothness and zero smooth Hessian of the
  logarithm of an invertible analytic function.
- `prop:cld-form-pullback`: functorial pullback for ordinary CLD forms and both
  differentials.
- `cor:ch16-smooth-h`: Bedford--Taylor invariance under an ordinary CLD-smooth
  zero-Hessian difference.
- `prob:frontier-cross-fan-upstairs`: the P21.3 target whose unresolved frontier
  is narrowed by this packet.

The exact source statements needed by the verifier are copied into
`DEPENDENCIES_STATEMENT.tex`.  That file is a self-contained materialization
for verification, not a replacement for the canonical statements in the
manuscript.
