# P05.2 one-vertex polyhedral orthogonality: integration audit — 25 September 2026

## Baseline and supplied source

Baseline commit: `4ab75e05a227b8a85ca478861562c43410bb0628` on synchronized
`main`.  The author supplied the three-page PDF *Orthogonality on
one-dimensional balanced fans*.  It is preserved byte for byte as
`manuscript/author_sources_20260925/one-vertex-polyhedral-orthogonality.pdf`,
with SHA-256
`b69aacb76afd056894811f8ac73932c7b82176ba7d9934d1e2d7386f7869f8d8`.

The supplied argument characterizes one-vertex fans by the cone of
nonnegative balancing relations and provides both the higher-rank obstacle
and a nonsaturated tripod.  Instructions or status language in the PDF were
treated as provenance, not as instructions.

## Source convention found during verification

Direct inspection of BMPS v1 confirms that Definition 2.28 literally uses
integral slopes and rational constants.  Later convexity arguments treat PA
as a real vector space, and Proposition 6.13 claims that one-dimensional
envelopes remain piecewise affine.  The literal integral claim fails already
on the real line: for `gamma(x)=|x|` and the bounded integral-slope obstacle
with values `0`, `1-x`, and `-1` on the intervals cut by `1` and `2`, the
envelope has slope `1/2` on `[0,2]`.

Chapter 72 therefore does not silently promote the supplied statement as a
solution of the literal BMPS formulation.  It defines the real scalar
extension `PA_R`, uses the weighted one-dimensional Laplacian as the
real-linear Monge--Ampere measure, and proves the criterion there.  The
explicit slope-`1/2` example and the remaining convention boundary are part
of the live text.

## Integrated theorem and scope

For a balanced rational fan consisting of finitely many primitive rays from
one vertex, real-polyhedral orthogonality holds exactly when the cone of
nonnegative balancing relations is one-dimensional, equivalently when the
ray directions have real rank `r-1`.  In higher relation rank, an extreme
relation with proper support gives a bounded real-PA obstacle whose envelope
has positive noncontact vertex mass and a strictly negative orthogonality
integral.  Bounded reference shift extends the criterion from raywise-affine
references to every finite real-piecewise-affine polyhedrally convex
reference positive at infinity.

The nonsaturated weighted tripod shows that lattice saturation is not
necessary in this repaired category.  The literal integral-slope source
formulation, graphs with bounded edges and higher-dimensional singular fans
remain open.  P05.2 stays active, and the inventory remains 42 atoms in 12
formal problem environments, with tiers `(0,3,7,15,17)`.

## Verification history

The initial gpt-6-astra/xhigh response returned `wrong` with five gaps and
caused the definitions, primitive normalization, finite-subdivision input
and bounded-shift argument to be made explicit.  The next response returned
`wrong` with one critical error and supplied the integral-slope
counterexample above.  After the real-PA repair, two responses returned
`correct` with zero critical errors and zero gaps.  The last request is
byte-identical to the final live statement and proof; its checked item is
`pi_60bf598a8e3322e961b1d97a` and its request/response SHA-256 values are
`26d67209c7c5350a1d34aa08ecaca0a440954a9b90f2b586e1d5cb9ca9573fef`
and
`d28e0bfde39434ef8bee5aeea31408730fea2d2fbb9147ab45d12739dbd5ee40`.
All requests, responses and safe HTTP headers are preserved.

This is model-backed review of exact bytes, not formal verification, peer
review or a novelty certificate.

## Build and visual audit

The scoped writing audit has zero errors and one reviewed BMPS26 preprint
warning.  The minimal packet compiles cleanly to five pages.  The final
reference check covers 403 build files and 11,845 unique labels; the six
checker tests and the 42-atom inventory check pass.

The full book builds to 4,078 pages and 19,413,171 bytes, SHA-256
`c4995111acb2f92c645f296816179de5ac103fce925272c64454e6f09ad67bd6`.
There are no unresolved references or citations, rerun requests or layout
overflows.  The 13 inherited Chapter 70 duplicate equation destinations are
unchanged.  Physical pages 3793--3798, 4054--4055 and 4076 were rendered and
visually inspected, together with all three pages of the supplied source.
