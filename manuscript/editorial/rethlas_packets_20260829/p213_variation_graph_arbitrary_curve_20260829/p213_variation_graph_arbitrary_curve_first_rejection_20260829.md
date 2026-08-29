# First production rejection: arbitrary-valuation variation graph packet

Date: 29 August 2026

This file preserves a noncontrolling failed verification.  None of the
theorem bytes in this first packet may be integrated into the live book.

## Exact rejected inputs

- principal statement SHA-256:
  `7b7348ff83ee2d9f4560b868bf30a5cbda28bc374940aff885305a060b593d0c`;
- principal proof SHA-256:
  `5ea911448a4044ae71243dcac1617f7307fff6c73b84bce01881fa7a91eeac5a`;
- dependency-closed statement SHA-256:
  `606f024b7939c5220fb6e1cbc61913d4b7d7d33e7ae4f1122f5f408e424dd1bf`;
- dependency-closed proof SHA-256:
  `a4278958a698445c46a426a4ac3a109d3728c3c12fe6fda6ab951a6510705027`.

The archived production response in
`p213_variation_graph_arbitrary_curve_run_20260829_8108` is final and has
verdict `wrong`, with one critical error and three gaps.  Its checked item is
`pi_e1bbb88b0d58f077ad3ef8eb`.

## Mathematical defects found

1. The proof conflated the derivative for the canonical graph metric with
   Ducros's normalized integer branch slope.  If the metric dilation ratio
   is `r`, the latter includes the factor
   `epsilon * r * [s(b):k]`.  The stated divisibility, greatest-common-divisor,
   primitive-tangent, and calibration arguments therefore did not follow.
2. The asserted ambient target tube did not exclude a subtree on which the
   separator block is initially constant but a boundary coordinate varies
   farther from the selected arm.  Properness alone does not prevent its
   tropical image from accumulating on the selected segment.  Hence the
   branch coefficient and divisor-functional construction was not proved.
3. The nonsmooth-locus dichotomy did not justify its additional conclusion
   about normalization.

The repair must use one consistently normalized integral slope vector and a
genuine source-local pushforward construction, or else narrow the statement.
It must also prove or delete the normalization assertion.  The earlier source
and hostile audits remain archived as evidence that those audits missed these
points; they are not controlling gates.

## Archive hashes

The request, response, and sanitized-header files have SHA-256 values

```text
969696ab540e42a471c64c4655058bdd6e5e09883e418f95acaaa6b70f2d267c
cc33b2fc9a396717e7e633b337b5b43e63ebb1a8802b8df2e6d6c2b2f5c083c4
f5852b29bf4ac273a59070e42687b1109cb9b8e17f79e552d4e99553175ed27b
```
