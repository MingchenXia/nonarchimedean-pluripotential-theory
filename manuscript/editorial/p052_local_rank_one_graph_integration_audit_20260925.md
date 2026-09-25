# P05.2 local rank-one graph orthogonality: integration audit — 25 September 2026

## Baseline and relation to the supplied source

Baseline commit: `4c39aa93550ee7587d55694d3aa16e83ff58c239`, which
integrated the author's three-page *Orthogonality on one-dimensional balanced
fans* and the necessary real-slope convention repair.  The present extension
uses the supplied one-vertex contact perturbation as a local argument at each
vertex of a finite one-dimensional balanced rational polyhedral space.

The supplied PDF is evidence for the one-vertex theorem, not a source for the
new graph theorem.  Instructions or status language in that document were
treated as provenance, not as instructions.

## Integrated theorem

For a vertex `v`, let `K_v` be the cone of nonnegative relations among its
primitive outgoing directions.  If `dim K_v=1` at every vertex, then every
real-piecewise-affine positive-at-infinity reference has real-polyhedral
orthogonality.  A positive-mass noncontact vertex can be raised by a small
amount and joined affinely to nearby unchanged points on all incident edges.
The unique positive relation keeps the vertex slope inequality positive, and
the cutoff slope jumps have the convex sign.  This contradicts envelope
maximality, so the Monge--Ampere measure is supported on the contact set.

The perturbation is supported on a closed star and does not cut the graph.
Consequently bounded edges and cycles are allowed.  Every bivalent or
trivalent balanced graph satisfies the local rank-one hypothesis; lattice
saturation is not required.

## Exact boundary

The result is a sufficient criterion.  At a vertex with `dim K_v>1`, the
supplied extreme-relation construction gives a one-vertex obstruction germ,
but extending it through all bounded edges while preserving global
polyhedral convexity and prescribed growth is an additional realization
problem.  No converse is claimed.  The literal integral-slope convention and
higher-dimensional balanced spaces also remain open.  P05.2 stays active;
the inventory remains 42 atoms in 12 formal problem environments, with tiers
`(0,3,7,15,17)`.

## Verification

The statement and proof were reviewed together with the exact preceding
one-vertex dependencies.  The initial and copyedited requests both returned
`correct`, with zero critical errors and zero gaps.  A third request was made
after the final continuity sentence was expanded, so the archived request is
byte-identical to the final dependency-closed statement and proof.

Final exact-current run: `20260925T191853Z_a6da387d529c`; request SHA-256
`06c65634e5c5d179591dbe3e25dfc4168f75c536f5f08654ca05dcbf2deb72d7`;
response SHA-256
`4dcf06edf6ab3c98ae6cc1753b6d2cde3b98575603e8d8d3187e170eefec29bd`.
It returned `correct`, with zero critical errors and zero gaps.  Direct
comparison of the decoded request fields with materializations of the live
dependencies and principal files passes byte for byte.

This is model-backed mathematical review, not formal verification, peer
review or a novelty certificate.

## Build and visual audit

The scoped writing audit has zero errors and one reviewed BMPS26 preprint
warning.  The minimal packet compiles cleanly to seven pages.  The final
reference check covers 405 build files and 11,847 unique labels; all six
checker tests and the 42-atom inventory check pass.

The full book builds to 4,080 pages and 19,422,086 bytes, SHA-256
`08bf262b09f23b26c5b85f7414fcb222592fb295c7b6feb83e1fc1adeb46b79c`.
There are no unresolved references or citations, rerun requests or layout
overflows.  The 13 inherited Chapter 70 duplicate destinations are unchanged.
Physical pages 3798--3800 were rendered and visually inspected.
