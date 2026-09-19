# Sources and dependency map

Date: 20 September 2026

No new external theorem or bibliographic citation is introduced by this
packet.  Its inputs are results already proved, cited, and integrated in the
book.  The source-scoped Wanner statement needed by the verifier is copied
verbatim at theorem-statement granularity into the supplemental dependency
file; it does not add a new claim to the manuscript.

## Book-local dependencies

- `prop:p062-rigid-base-open-polyannulus-product`: chartwise classical
  pluriharmonicity, logarithmic decomposition, and first-current rigidity for
  an open-polyannulus product over a base with the corresponding rigidity
  hypotheses.
- `prop:p213-residual-picard-smooth-curve`: ordinary CLD smoothness and zero
  smooth Hessian for continuous zero-current functions on the residual-Picard
  curve.
- `cor:p213-residual-picard-wanner`: Wanner's theorem applied to identify
  continuous zero-current functions on that curve as classically
  pluriharmonic.
- `lem:p062-curve-first-current-rigidity`: vanishing Hessian and first current
  force local constancy on the curve base.
- `prop:p062-mixed-exact-bundle-tower-transfer`: transfer through finite
  towers of open-polydisc, projective-space, smooth proper split-toric, and
  proper smooth connected-curve bundles.
- `lem:ch15-log-smooth`: ordinary CLD smoothness and zero smooth Hessian of the
  logarithm of an invertible analytic function.
- `prop:cld-form-pullback`: functorial pullback for ordinary CLD forms and
  their differentials.
- `cor:ch16-smooth-h`: Bedford--Taylor invariance under an ordinary
  CLD-smooth zero-Hessian difference.
- `prob:frontier-cross-fan-upstairs`: the P21.3 target narrowed by this packet.

The previously materialized dependency packet is incorporated into the
verifier request.  `DEPENDENCIES_EXTRA_STATEMENT.tex` records the additional
exact source statement whose omission caused the initial context gap.

## Method-selection note

The available logarithmic Reinhardt Hessian-transfer method concerns a
complex real-Hessian determinant identity.  It was audited and not imported:
the present claim instead needs Berkovich/CLD locality, logarithmic smoothness,
and current rigidity, so that method would not discharge the open-subset
heredity obstruction.
