# P07.1 exact infinite-star × finite-collar product: repair ledger

## Standalone rejection

The first request supplied only the new statement and proof.  The verifier
returned final `wrong`, with no critical error and two gaps: the three cited
prior theorems and the construction underlying the monotone-coordinate
refinement were not present as verifiable premises.

## First dependency-closed rejection

The second request added the exact infinite-star, finite-collar, and
star--Euclidean statements and proofs.  The verifier again returned final
`wrong`, with no critical error and two gaps:

1. the star--Euclidean proof itself invoked the Stone--Euclidean theorem,
   whose statement and proof had not been materialized; and
2. the final clamp estimate asked for a standard star core even when the
   point lay in a branch-only or terminal neighbourhood.

The proof was repaired by distinguishing the node star core, compact
ordinary branch interval, and compact terminal interval.  The
Stone--Euclidean statement and proof were added to the dependency closure.

## Accepted repair

The repaired four-dependency request returned final `correct`, with zero
critical errors and zero gaps.  The checked item is
`pi_dab08cd0ade65f20ea9867b4`.
