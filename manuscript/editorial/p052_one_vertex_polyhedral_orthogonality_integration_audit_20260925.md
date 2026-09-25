# P05.2 one-vertex polyhedral orthogonality: integration audit — 25 September 2026

## Baseline and superseding withdrawal

Baseline commit: `4ab75e05a227b8a85ca478861562c43410bb0628` on synchronized
`main`.  The author first supplied the three-page PDF *Orthogonality on
one-dimensional balanced fans*, SHA-256
`b69aacb76afd056894811f8ac73932c7b82176ba7d9934d1e2d7386f7869f8d8`.
Later on 25 September 2026 the author supplied a replacement titled
*Withdrawn draft: Orthogonality on one-dimensional balanced fans*.  The
replacement is preserved byte for byte as
`manuscript/author_sources_20260925/one-vertex-polyhedral-orthogonality.pdf`,
with SHA-256
`0ad51074108eb2202d4b624637c035610d275c67fd8456dab59282d543d5f5fb`.
The earlier bytes remain recoverable from Git history and are no longer the
current source artifact.

The replacement says that the positive theorem and derived examples in its
retained body must not be cited as results, because the proof uses a
real-affine envelope while the stated source class has integral slopes.  The
book treats this status language as source provenance, not as an instruction,
but respects the mathematical withdrawal: Chapter 72 no longer cites the
note as support for a positive theorem.

## Source convention found during verification

Direct inspection of BMPS v1 confirms that Definition 2.28 literally uses
integral slopes and rational constants.  Later convexity arguments treat PA
as a real vector space, and Proposition 6.13 claims that one-dimensional
envelopes remain piecewise affine.  The literal integral claim fails already
on the real line: for `gamma(x)=|x|` and the bounded integral-slope obstacle
with values `0`, `1-x`, and `-1` on the intervals cut by `1` and `2`, the
envelope has slope `1/2` on `[0,2]`.

Chapter 72 defines the real scalar extension `PA_R`, proves independently
that every finite one-dimensional balanced space has real-PA regularity,
uses the weighted one-dimensional Laplacian as the real-linear
Monge--Ampere measure, and proves the orthogonality criterion only there.
It also proves that the slope-`1/2` envelope stays at uniform distance at
least `1/4` from every literal integral-slope convex PA function.  Thus the
literal affine-line pair already fails regularity.

## Integrated theorem and scope

The book-local theorem says that, for a balanced rational fan consisting of
finitely many primitive rays from one vertex, real-polyhedral orthogonality
holds exactly when the cone of nonnegative balancing relations is
one-dimensional, equivalently when the ray directions have real rank `r-1`.
In higher relation rank, an extreme relation with proper support gives a
bounded real-PA obstacle whose envelope has positive noncontact vertex mass
and a strictly negative orthogonality integral.  Bounded reference shift
extends the criterion from raywise-affine references to every finite
real-piecewise-affine polyhedrally convex reference positive at infinity.

The book-local nonsaturated weighted tripod shows that lattice saturation is
not necessary in this repaired category.  At this integration stage, the
literal integral-slope source formulation, graphs with bounded edges and
higher-dimensional singular fans remained open.  The later same-day
[local rank-one graph audit](p052_local_rank_one_graph_integration_audit_20260925.md)
records the subsequent book-local extension across bounded edges and cycles.
P05.2 stays active, and the inventory remains 42 atoms in 12 formal problem
environments, with tiers `(0,3,7,15,17)`.

## Verification history

The initial gpt-6-astra/xhigh response returned `wrong` with five gaps and
caused the definitions, primitive normalization, finite-subdivision input
and bounded-shift argument to be made explicit.  The next response returned
`wrong` with one critical error and identified the integral-slope
counterexample above.  After the real-PA repair, two historical responses
returned `correct` with zero critical errors and zero gaps.  Their last
checked item is `pi_60bf598a8e3322e961b1d97a`, with request/response SHA-256
values
`26d67209c7c5350a1d34aa08ecaca0a440954a9b90f2b586e1d5cb9ca9573fef`
and
`d28e0bfde39434ef8bee5aeea31408730fea2d2fbb9147ab45d12739dbd5ee40`.
All requests, responses and safe HTTP headers are preserved.

Those receipts cover the archived dependency-closed packet, not the later
source-withdrawal edits to the live preamble or the new P05.1 theorem.  No
new model-verifier result is claimed.  The historical checks are not formal
verification, peer review, or novelty certificates.

## Build and visual audit

The scoped writing audit has zero errors and one reviewed BMPS26 preprint
warning.  The revised minimal packet compiles cleanly to four pages.  The final
reference check covers 409 build files and 11,854 unique labels; the six
checker tests and the 42-atom inventory check pass.

The full book builds to 4,084 pages and 19,443,419 bytes, SHA-256
`05c0b1e154fd57c570068a49e6cbb5a221193f6351019b8735eaddfd469c5407`.
There are no unresolved references or citations, rerun requests or layout
overflows.  The 13 inherited Chapter 70 duplicate equation destinations are
unchanged.  Physical pages 3793, 3796, 3806, 3809, and 4061 were rendered and
visually inspected, together with all three pages of the supplied replacement
source.  No clipping, collision, or broken line was found.
