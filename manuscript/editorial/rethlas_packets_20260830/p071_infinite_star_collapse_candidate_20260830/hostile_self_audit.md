# Hostile self-audit: CLD infinite-star collapse candidate

This document records the pre-submission self-audit.  Its provisional gate
warning was discharged on 30 August 2026.  The repaired exact statement and
proof identified in rethlas_receipt.md passed three independent hostile
audits and production Rethlas with final/correct, zero critical errors, and
zero gaps.  The two false endpoint assertions in the earlier draft were
repaired before the frozen proof was submitted.

## Imported structural facts

The proof uses exactly the structure stated by Chambert--Loir--Ducros in
Section 6.7.3 for `X_B`:

1. an open centre neighbourhood contains every full branch except finitely
   many;
2. a smooth function has only finitely many branches that fail to be full
   and constant;
3. its endpoint derivatives have finite support and sum to zero;
4. positivity of `d'd''` is ordinary convexity on each branch.

The theorem restates these inputs explicitly.  It does not replace the CLD
topology by the quotient topology, and it never takes a countable
intersection of centre neighbourhoods.

## Checks against the likely failure modes

### Restriction and gluing

When a smaller neighbourhood truncates additional full branches `E`, those
branches move from the left side of the finite-point inequality to the right
with the opposite sign.  Conversely, when an inequality is known only on a
smaller neighbourhood, convex secant-slope monotonicity moves its sample
points toward the centre and then moves `E cap F` back to the left.  The
remaining `E` terms are nonpositive because those branches are full in the
larger neighbourhood.  This proves both restriction and gluing; it is not an
assertion that a coupled Jensen condition is automatically local.

### Decreasing limits with extended-real values

At finite centre value, a sampled exceptional value cannot fall to
`-infinity`, because the right side of the finite-point inequality would
fall to `-infinity` while the left side is nonnegative.  A sampled full value
cannot fall to `-infinity`, because the left side would diverge to
`+infinity` while the finite exceptional right side is bounded above.
This makes termwise passage legitimate.  Exact endpoint traces pass by a
separate monotone argument.

### Countable activity

Countable activity is not assumed.  The finite-point inequalities imply a
uniform bound on all finite sums of nonnegative full-branch endpoint slopes.
Positive support of such a family is countable.  A full branch of zero
endpoint slope is constant, because every centre-ending secant slope lies
between zero and that endpoint slope.

### Finite harmonic smoothing

Chordal endpoint slopes are no larger than the target endpoint derivatives,
so their total remains nonpositive.  The missing positive derivative is
inserted by a convex boundary layer.  Its derivative can be arbitrarily
large while its amplitude is arbitrarily small, because the support collar
can be shortened.  The layer is constant to the left and therefore respects
the full-branch constant-collar requirement.  Exact regularized maxima keep
the final affine pieces unchanged at the centre, so the derivative ledger is
not perturbed by corner smoothing.

### Monotonicity after smoothing

The finite harmonic smoothing is only a two-sided uniform approximation; it
need not preserve order.  The proof inserts the scalar gap `2^{-n}` before
smoothing and chooses errors `2^{-(n+4)}`.  The difference of consecutive
scalar gaps is strictly larger than the sum of consecutive smoothing errors,
so the final smooth functions decrease pointwise on the entire fixed
neighbourhood.

### Singular endpoints and centre value

All branch targets are truncated before uniform smoothing, so every finite
stage is real-valued and continuous even when the target equals `-infinity`
at a full endpoint.  When the centre value itself is `-infinity`, full
branches are identically `-infinity`, and convexity forces the same conclusion
on smaller exceptional collars.  Constants then give the stage-one
approximation.

## Verification discharge and scope

1. Independent source-aware verification confirmed the explicit smoothness,
   topology, positivity, and derivative orientation from CLD Section 6.7.3.
2. Three independent hostile audits passed the exact repaired bytes.
3. Production Rethlas checked item pi_00f6c73303087d94da9eb724 and returned
   final/correct, with zero critical errors and zero gaps.
4. Any later edit to the frozen mathematical bytes requires a new gate.
5. The result settles the exact CLD star X_B; it does not settle arbitrary
   higher-dimensional affine tropical spaces or every nonambient smooth
   structure.
