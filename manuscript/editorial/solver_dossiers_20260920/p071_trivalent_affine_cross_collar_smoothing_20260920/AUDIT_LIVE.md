# P07.1 affine cross-collar smoothing audit

Date: 20 September 2026

Status: verified and integrated into the live book.

## Claim boundary

The packet proves a first-stage approximation result for continuous finite
convex piecewise-affine functions on a trivalent--trivalent product which
agree with one ambient affine function on a fixed cross-collar of the two
node axes.  It allows independent finite polyhedral mixed terms on all nine
branch rectangles away from that collar.

It does not prove that every function satisfying the one-axis and
double-node Jensen conditions can be reduced to this form.  It therefore
does not settle P07.1.

## Proof ledger

1. The collar affine function is a global minorant of every convex branch
   restriction because the difference has zero as a subgradient at an
   interior collar point.
2. Each convex piecewise-affine branch restriction is a finite maximum of
   affine minorants.
3. A raised copy of the common affine minorant dominates all branch-specific
   affine pieces on the entire fixed cross-collar.
4. Exact regularized maxima therefore produce smooth jointly convex branch
   functions which equal one ambient affine function near both axes.
5. The trivalent vector identities make both balance sums vanish.
6. A summable tail converts uniformly accurate upper approximants into one
   pointwise decreasing sequence on a fixed neighbourhood.

## Verification

The exact current statement and proof passed the local `gpt-6-astra`
verifier at `xhigh`, final `correct`, with zero critical errors and zero
gaps.  The strict exact-current receipt audit also passed.  A complete
second reading found no mathematical defect.  The full-book visual pass
repaired one mistyped inequality command and one duplicated cross-reference
word; the corrected exact proof was then resubmitted and again returned
final `correct` with zero critical errors and zero gaps.
