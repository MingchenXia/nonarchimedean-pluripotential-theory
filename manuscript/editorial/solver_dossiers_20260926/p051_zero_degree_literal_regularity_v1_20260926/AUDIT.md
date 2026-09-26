# P05.1 zero-degree literal regularity: audit

Date: 26 September 2026

## Claim audited

Let `X` be a finite one-dimensional balanced rational polyhedral space and
let `gamma` be a literal integral-slope polyhedrally convex reference that is
positive at infinity.  Then `deg(gamma)=0` exactly when `X` is compact.  In
that case every polyhedrally convex function is constant on each connected
component, and every literal obstacle has the exact componentwise envelope

```text
min_C(gamma + u).
```

This minimum is rational, so the envelope itself belongs to the literal
polyhedrally convex piecewise-affine class.  The pair therefore has the
literal regularity property.

## Mathematical audit

1. After a finite refinement, each bounded edge contributes two opposite
   weighted slopes to the total graph Laplacian.  These cancel.  Each
   unbounded end contributes its positive weight times its recession slope.
   Positivity at infinity makes every such summand strictly positive.
2. A finite polyhedral structure is compact exactly when it has no unbounded
   edge.  The end formula therefore proves the degree/compactness
   equivalence, including disconnected spaces.
3. On a compact connected component, a continuous convex edge restriction
   has a maximum at a vertex.  For every sufficiently small common parameter
   `t`, the balancing weights express that vertex as the barycentre of the
   incident points at distance `t`.
4. The Jensen inequality and the global maximum force equality at every one
   of those incident points.  One-variable convexity then propagates the
   maximum along each entire edge, and graph connectivity propagates it
   through the component.
5. The reference is consequently a rational constant on each component.  A
   literal obstacle reaches its minimum at a rational vertex of a common
   finite subdivision, so that minimum is rational.
6. Every envelope competitor is componentwise constant and bounded by the
   corresponding minimum; those componentwise minima themselves form a
   literal admissible competitor.  This proves the exact envelope formula
   and the regularity conclusion.

## Boundary audit

The theorem closes the zero-degree one-dimensional branch.  It does not
classify the remaining positive-degree case.  Combining it with the
strict-vertex obstruction shows that any unresolved finite-graph pair must
have a higher-dimensional local relation cone at every positive-mass vertex,
with the reference slope vector on a proper face of the corresponding dual
cone.  P05.1 therefore remains active.

The official arXiv record for BMPS26 was rechecked on 26 September 2026.  It
still lists only version 1, submitted on 9 March 2026, and no journal
reference.  The source-audit warning is therefore reviewed rather than
silenced.

No model-verifier result is claimed for this packet.

## Result

The statement, proof, exceptional cases, and status boundary pass the second
audit.  The active inventory remains 42 atoms in 12 formal problem
environments, with tiers `(0,3,7,15,17)`.
