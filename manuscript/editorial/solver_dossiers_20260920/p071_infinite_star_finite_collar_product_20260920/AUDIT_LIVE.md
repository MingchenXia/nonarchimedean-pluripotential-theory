# P07.1 exact infinite-star × finite-collar product: live audit

Date: 2026-09-20

## Scope

The packet proves first-stage collapse for the product of the exact CLD
infinite star with the finite constant-collar endpoint.  It retains mixed
branch--interval Hessian terms on the finite stratum and does not claim the
corresponding theorem at the endpoint at `-infinity`, for two branched
factors, for non-CLD stars, or with nonconstant affine directions on an
additional Stone factor.

## Proof mechanism

1. The endpoint comparison germ is extended by `s -> max(s,0)` to the
   already verified exact star--Euclidean comparison class.
2. The partial-Legendre proof is refined by taking supporting covectors with
   nonnegative endpoint-coordinate slope.  Scalar star smoothing and
   regularized maxima preserve that monotonicity.
3. A nested family `h_a(s)=a phi(s/a)` of smooth convex nondecreasing clamps
   is exactly constant near zero and decreases to the identity.
4. Composing the monotone Euclidean approximants with these clamps preserves
   joint convexity, finite activity, the star balance law, and exact
   full-branch collars.
5. Uniform continuity is applied on the correct compact core for each
   stratum: a standard star core at the node, a compact branch interval at
   an ordinary point, and a compact terminal interval at a full endpoint.

## Verification history

- Strict Mingchen-writing audit of the final statement and proof: `0` errors
  and `0` warnings.
- Standalone verifier request: final `wrong`, `0` critical errors and `2`
  gaps, both caused by absent dependency records.
- First dependency-closed request: final `wrong`, `0` critical errors and
  `2` gaps.  It identified the missing Stone--Euclidean dependency and the
  overbroad phrase “standard star core” at non-node strata.
- Repaired four-dependency request: final `correct`, `0` critical errors and
  `0` gaps; checked item `pi_dab08cd0ade65f20ea9867b4`.

The rejected requests and responses are retained as part of the repair
history.  No novelty or priority claim is made.
