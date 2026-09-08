# P14.3 dominated-divisorial extended-arithmetic repair

## Scope

This is a precise post-freeze patch for the 31 August P14.3
dominated-divisorial research candidate.  It leaves the theorem statement,
the domination argument, its hypotheses, and its conclusion unchanged.

The patch fixes two formal issues in the proof:

1. divisor-value sums that may contain an infinite valuation now explicitly
   omit zero coefficients, so they never form the undefined expression
   (0\cdot(+\infty)); and
2. the final net is explicitly indexed by finite ideal sets and accuracy
   parameters, rather than being described only informally.

The patch is not an independent mathematical audit, source-closed production
verification, live-manuscript integration, or P14.3 retirement evidence.

## Verification boundary

`P143_V1_TO_V2.patch` must apply with zero fuzz to the frozen v1 proof.  Its
postimage remains a new candidate and must receive a fresh exact-byte
mathematical audit and production verification before it can be promoted.
