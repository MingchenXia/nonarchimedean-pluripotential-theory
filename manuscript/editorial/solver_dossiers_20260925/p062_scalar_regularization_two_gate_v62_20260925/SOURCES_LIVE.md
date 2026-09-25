# P06.2 scalar regularization two-gate reduction: sources

## External source

- Walter Gubler and Joseph Rabinoff, *Classically psh and pluriharmonic
  functions on Berkovich spaces*, arXiv:2506.13548v2.
  Proposition 7.2(6), checked in the archived PDF
  `manuscript/editorial/rethlas_packets_20260830/p031_perfected_unibranch_curve_envelope_20260830/sources/Gubler_Rabinoff_2506.13548v2.pdf`,
  states that a function is pluriharmonic if and only if its pullback under
  an arbitrary analytic extension of scalars is pluriharmonic.

## Internal dependencies

- `prop:cld-psh-positive-current`: a locally integrable CLD-psh function
  has positive Hessian current; the converse is proved there only in the
  smooth case.
- `thm:cld-to-classical-psh`: every CLD-psh function is classically psh.
- `prop:classical-psh-calculus`: a real-valued function is classically
  pluriharmonic exactly when both signs are classically psh.
- `thm:supplied-p061-singular-pluriharmonic`: on the spaces in P06.2,
  classical pluriharmonicity implies local real-PL regularity.
- `thm:p01-real-pl-positive-current-candidate`: on a pure-dimensional
  space in the displayed P06.2 setting, positivity of the Hessian current
  of a real-PL function is equivalent to GJR semipositivity.  Applied to
  both signs of a zero-current function, this gives GJR harmonicity.

## Scope boundary

The proposition does not assert automatic pullback of the current
`d'd''[h]` under scalar extension and does not assert the converse
“positive current implies CLD-psh.”  Those are the two separate hypotheses
whose simultaneous validity yields the conclusion.
