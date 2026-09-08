# P14.8 v3 model-backed verification result

## Outcome

The explicitly authorized model-backed verifier returned **`wrong`** for the
frozen P14.8 v3 packet.  The verifier's local run identifier was
`20260908T064943Z_8887cb1fdb96`.  It reports five critical errors and two
gaps in the attached Chapter 51 support material.

The verifier separately found the P14.8 v3 terminal theorem and its
$\mathbf P^1$ Green-potential family viable when the standard
increasing-envelope, valuative multiplier-ideal, and nonpluripolar-product
results are invoked correctly.  That is not an acceptance: the review rule
requires zero findings for the complete supplied packet.

The critical findings concern the source support rather than the Cantor
initial-index repair:

1. a pointwise Demailly $n/m$ estimate is incorrectly applied to arbitrary
   divisors, where the error is controlled by $A(E)/m$;
2. a global truncation bound lacks its semipositivity reduction;
3. restricted truncations are incorrectly asserted to be closed;
4. levelwise multilinearity of the truncation construction is incorrectly
   asserted; and
5. unrestricted mixed-mass monotonicity is incorrectly attributed to BEGZ10
   rather than the later general result.

The two recorded gaps concern passing from an increasing net to the required
sequential/mean-value argument and proving the one-sided
$\mathcal I$-preorder equivalence directly.

## Exact receipt

| Artifact | SHA-256 |
| --- | --- |
| Submitted request | `22691714d0c6821fbb41482f0bebd5beb65b1c2307b729e0d6b5a61b864d2b72` |
| HTTP response | `7c100683c41927cfbb0b53aefdb29b1716b3c60e71f2cc88eedd8da5cba68f02` |
| Response headers | `f3709ce412a77d7f42812f1d3878492c747267c26627cfb3ecb3e66f516fbd11` |

The canonical archived bytes are `VERIFICATION_RUN_20260908/request.json`,
`response.json`, and `headers.json`.  The HTTP status is 200.  The full
machine-readable diagnoses and repair hints reside in `response.json`.

## Production boundary

P14.8 remains open and unintegrated.  This receipt rejects the exact review
packet; it does not authorize a repair, amend Chapter 51, alter Chapter 72,
or convert the verifier's limited viability observation into a theorem
acceptance.
