# Chapter 60: rays, Lelong normalization and truncation — 22 September 2026

## Joint positivity and normalized divisorial data

The ray definition now imposes joint pullback-omega positivity on the
punctured product, in agreement with Chapter 52 and
[MP24 arXiv version 2, Section 5.1.1](https://arxiv.org/html/2409.06221v2).
Spatial psh slices alone do not imply this: the constant-in-space family
sin(s) is not convex in s. Linear growth is expressed as an upper affine
bound for large s; restriction to a smaller disc suffices for the germ
construction at its center.

Adding a log|tau|^2 to U makes it bounded above near the central fibre
and allows its psh extension there. For the normalized Gauss divisor
b_E^(-1) ord_E, the signed normalized number is

`nu_v(U) = nu_E((U + a log|tau|^2) o mu) / b_E - a`.

The formula explicitly proves independence of a and of the representing
model. It distinguishes the nonnegative ordinary generic Lelong number
from the possibly negative normalized ray number. For U_s = c s it gives
U^NA = c for every real c and every central multiplicity b_E. Both
definitions now appear in one aligned display. The squared-norm and
radial conventions of Chapter 51 are preserved.

## Exhausting the logarithmic cutoff

The checked proof of MP24 arXiv version 2, Theorem 5.1.4 uses the fixed
cutoff max(V_m, log|tau|) and then asserts the full divisorial limit. A
fixed cutoff instead truncates a normalized Lelong number at its slope.
The book now supplies the missing exhaustion step, without claiming a
new proof of the analytic regularization theorem.

Normalize V <= 0 and set V^(k) = max(V, k log|tau|^2). Its multiplier
ideal at scale m contains tau^(mk), as follows directly from the
integrability definition with weight exp(-m V^(k)). The resulting
invariant ideals are flag ideals and their model functions lie in [-k,0].
For each fixed k and lambda > 1, the curvature-loss regularization input
from the proof of MP24 Theorem 5.1.4 gives model (lambda alpha)-psh
functions for all sufficiently large m. Relative nefness after resolving
the ideal uses the bounded-potential argument of MP24 Lemma 5.1.3.
That analytic input remains explicitly imported. Attempts to inspect the
separate Demailly 1992 PDF on both official Grenoble hostnames timed out;
no independently checked Demailly proposition locator is claimed here.

Multiplier-ideal subadditivity supplies dyadic monotonicity. The imported
multiplier-ideal Lelong formula already recorded in Chapter 51 identifies
the divisorial limit as max(-nu_v(V), -k), making the effect of the cutoff
explicit. The model functions are independent of lambda, so division by
rational lambda_j = 1 + 1/j and decreasing stability recover positivity
in alpha. Finally k tends to infinity. Ideal inclusions give monotonicity
on the whole spectrum, and finiteness at the trivial valuation excludes
the identically -infinity limit. Adding back the growth slope a and using
divisorial comparison complete the deduction.

## Correction to the earlier maximum proof

The normalization audit also found an error in the maximum proof added
in commit 38506d9: its complex potentials used log|s| although the book's
ddc convention gives dd^c log|s| = [div(s)]/2 minus half the curvature.
They now use log|s|^2, and the residual potential subtracts log|f_H|^2.
The displayed curvature identity is explicit. Thus the resolved nef
class subtracts H with coefficient one, as the proof requires. This is
a correction to the earlier new exposition, not a pre-existing-source
recovery or a change to the statement of maximum stability.

## Validation and next work

The second pass checked the joint positivity condition, removable
extension, sign of the growth correction, all b_E factors, both signs of
the affine-ray slope, the multiplier-ideal convention, the two cutoff
limits, dyadic ideal inclusion, the original-background limit and
noncollapse. It also corrected a typesetting escape in the squared ideal.
The new ray and normalization text passes the strict writing audit with
zero errors or warnings.

The final scoped build has 90 pages, no overfull box or unresolved
citation, and the same three external Chapter 71 reference occurrences.
Physical pages 60–61 and 72–74 were rendered and inspected after the
last revision. The source closure has 388 files and 11,432 labels,
with no duplicate or structural defects. The missing Chapter 70 file
and its thirteen unresolved file/label pairs are unchanged. The exact
open-problem inventory and whitespace checks pass; this is not a full
book build or a research retirement.

Next checks include the maximal-ray existence argument and its use of
sequential approximation and energy equality. A related concrete issue
was also found in Chapter 46, especially rem:ch46-zeroth-slot: increasing
a pulled-back ample background does not make an arbitrary PL function
psh on its model. The difference-of-positive-model-pairs construction
now written in Chapter 60 provides the route to audit and repair it.
