# Local mathematical audit

Date: 20 September 2026

## Claim boundary

The corollary is local.  It assumes, rather than derives, a two-sided
identification of every complete generator germ with the generator sheaf on
a relatively open convex subset of one polyhedron.  It therefore allows
global nonconvexity, monodromy, arbitrary cell incidence, and failure of
local finiteness, but it does not include a branched or singular-link germ
without such a convex development.

The Stone factor still carries only locally constant affine functions, and
the star is the exact CLD star used by the ambient theorem.  No claim is made
for separately convex generators, non-CLD stars, or nonambient star smooth
structures.

## Proof obligations

1. The chart identifies complete product generator sheaves in both
   directions.  This is part of the stated generator-preserving hypothesis
   and the corresponding product construction.
2. Restriction commutes with every hierarchy stage.  The proof records the
   successor and limit steps of the transfinite induction, rather than
   relying only on minimality of the full sheaf.
3. The ambient theorem applies after the chart has landed in a relatively
   open convex subset of its polyhedron.  The theorem is a sheaf identity,
   so its restriction supplies the desired equality.
4. The fixed-neighbourhood and common-activity conclusions are local outputs
   of the ambient theorem and survive transport through the chart.
5. Chartwise comparison sheaves agree on overlaps because each is equal to
   the same intrinsic full generated sheaf there.

The Mingchen TeX audit returned zero errors and zero warnings for the live
statement and proof before model-backed submission.
