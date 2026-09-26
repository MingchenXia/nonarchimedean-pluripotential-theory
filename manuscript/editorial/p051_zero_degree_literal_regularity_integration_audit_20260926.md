# P05.1 zero-degree literal regularity: integration audit — 26 September 2026

## Result integrated

Chapter 72 now settles the zero-degree branch of literal one-dimensional
polyhedral regularity.  For a finite balanced graph and a reference positive
at infinity, bounded-edge slope contributions cancel in the total degree,
whereas every unbounded end contributes a strictly positive weighted
recession slope.  Thus degree zero is equivalent to compactness.

On a compact connected balanced graph, choose a vertex where a polyhedrally
convex function reaches its maximum.  The balancing weights express that
vertex as the barycentre of equally distant points on all incident germs.
The Jensen inequality forces equality at every such point.  Edge convexity
and graph connectivity then force the function to be constant on the entire
component.

It follows that, for every bounded literal piecewise-affine obstacle `u`,
the envelope is the componentwise minimum of `gamma+u`.  This minimum occurs
at a rational vertex and is rational, so the envelope itself belongs to the
literal polyhedrally convex piecewise-affine class.  Literal regularity holds
in degree zero.

## Updated P05.1 boundary

The theorem removes the zero-degree case from the open part of P05.1.  The
strict-vertex theorem already gives nonregularity whenever some local
reference slope vector is strictly positive on the nonzero relation cone.
Consequently the remaining finite-graph problem has positive degree and, at
every positive-mass vertex, a higher-dimensional local relation cone with
the reference slope vector on a proper face of its dual cone.

P05.1 remains active, and the inventory remains 42 active atoms in 12 formal
problem environments, with tiers `(0,3,7,15,17)`.

The proof is book-local.  The official arXiv record for BMPS26 was rechecked
on 26 September 2026 and still contains only version 1, submitted on 9 March
2026, without a journal reference.  No model-verifier result is claimed.

## Release gates

- Scoped Mingchen-writing audit: zero errors and one reviewed BMPS26
  arXiv-only warning.
- Minimal packet: 2 pages, 119,748 bytes, SHA-256
  `d96a60269733125378a6c7b28853932e16887db2a256c449baf20e93fd44baf8`;
  the final log is clean and both pages were visually inspected.
- Reference graph: 419 build-closure files and 11,873 unique labels; zero
  missing inputs, multiply defined labels, dangling references, or structural
  errors.  All six checker tests pass.
- Inventory: 42 active atoms in 12 formal problem environments, tiers
  `(0,3,7,15,17)`.
- Full book: 4,096 pages, 19,484,300 bytes, SHA-256
  `e8a719af038ed6d6f836c5c7b15b9d4eda6777feebc0e97eea7033ff2ff94cc8`.
- Full-book log: no unresolved reference or citation, rerun request, missing
  input, horizontal or vertical overflow, or fatal error.  The 13 inherited
  Chapter 70 duplicate destinations are unchanged.
- Visual audit: physical pages 3811--3815, corresponding to printed pages
  3743--3747, and both minimal-packet pages were inspected after the final
  build.  No clipping, collision, or malformed display was found.

Exact packet-level evidence is preserved in
`solver_dossiers_20260926/p051_zero_degree_literal_regularity_v1_20260926`.
