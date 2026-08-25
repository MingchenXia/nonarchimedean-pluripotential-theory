# P06.3 ordinary CLD-smooth harmonic nonregularization: exact-live receipt

Date: 25 August 2026 (Asia/Shanghai)

Status: exact current Chapter 19 statement and proof verified and released for
live integration.

## Controlling verdict

- Run: `20260825T055907Z_b5c8f0719b60`.
- Item: `pi_d80993bb01a748f0422ae6a5`.
- Model / scrutiny: `gpt-5.6-sol` / `xhigh`.
- Verification status / verdict: `final/correct`.
- Critical errors / gaps: `0/0`.
- Statement SHA-256:
  `b5c8f0719b606707b8055f0ead8c1baa96b5d9732cccf51a0e86ec02c5e64f24`.
- Proof SHA-256:
  `ba402983b6d88c03437c79af66dfd541c5a37b89c0bb2a6a67438ac84120565b`.
- Request SHA-256:
  `2b564db26e52284aeafa88e0f8ed3ef39aed3a016c3a21716fdf80e437dd959f`.
- Aggregate context digest:
  `171cddbcc75aa45baa78c50b913c3bb34aeb35c0053ef17b62e99b9fce450e69`.
- Item context digest:
  `a2a16ed71fcc1cf6c7b1d96a7376a46b9f978dac29d3f0d3eb0beb88e7dd68b0`.

The request fields decoded byte-identically to the controlling statement and
proof, which in turn compared byte-identically with the live Chapter 19
proposition and proof.

## Exact conclusion and firewall

On a smooth proper curve from GJR Section 17 there is an integral PL harmonic
function on a relatively compact three-arm neighbourhood which is weakly
smooth with zero weakly smooth `d'd''`, but is not a locally uniform limit of
ordinary CLD-smooth harmonic functions.  In particular it is not a decreasing
pointwise limit of such harmonic functions.

This result refutes only the literal request for ordinary CLD-smooth
**harmonic** approximants.  It does not refute decreasing approximation by
ordinary CLD-smooth **psh** functions: positive curvature destroys the fixed
slope closure argument.  P06.3 remains active in precisely this psh scope,
and the authoritative counts remain 18 formal problem environments and 59
active atoms.

## Global model and source precision

The live proof uses the globally defined model function `F composed with tau`
constructed in the proof of GJR Proposition 17.4, then restricts it to a short
value-group-rational three-arm affinoid on which Proposition 15.9 gives
harmonicity.  It does not extend a merely local germ to the inverse image of a
graph star.  Thuillier Proposition 2.3.3 supplies model-independence on the
fixed inner strict affinoid.

The displayed direction ordering in the statement of GJR Proposition 17.4
and the coordinate formulas in its Section 17.2 are not propagated.  The
proof needs only that the three slopes are a permutation of `1,-1,0`, hence
balanced, and separately uses the explicit residual class `[z]-[x]` computed
in the same construction.  Reader-facing prose makes no claim about a source
error.

## Preserved history

- Source-aware run `20260825T045723Z_331edb5358e4` passed its frozen packet,
  but did not control the later adapted live bytes.
- Exact-live run `20260825T054030Z_b5c8f0719b60` also returned
  `final/correct`, but its proof used the local lift `T-tilde_1` on a larger
  inverse-image star than the cited source explicitly supplied.  Human audit
  found that domain mismatch, so the run is preserved as stale and
  non-controlling.  The current global-model proof was independently gated.
- The source-aware round-one rejection
  `20260825T044433Z_331edb5358e4` remains preserved in its existing receipt.

## Preserved controlling artifacts

The raw run directory
`p06_cld_smooth_harmonic_nonregularization_live_run_20260825/` contains the
aggregate manifest and verification, item log and verification, and both
completed process guards.  Their full SHA-256 values are recorded by the
repository artifact audit.

The combined six-page minimal compile succeeded, with PDF SHA-256
`3a3c81b3395be8f423bb41d0e1f94335d6e7b160fda68744d6ae6f9da48f13b7`.

No novelty or priority claim is made.
