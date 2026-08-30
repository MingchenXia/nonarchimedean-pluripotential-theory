# Independent exact-byte hostile/source audit

## Frozen-byte binding

This audit binds exactly the following candidate bytes:

- `statement.tex`: `dfd8c7cc9d6d26f50260707975ff62d4f292627f084400bcd37b32253c876cdc`
- `proof.tex`: `9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6`

The hashes were computed before the audit and rechecked after it.  The
candidate statement and proof were not edited, and the candidate was not
submitted to production Rethlas as part of this audit.

## Numbered verdict

1. **SHA/freeze: PASS.**  Both exact SHA-256 values match the frozen-byte
   binding above.

2. **CLD source legality: PASS.**  Local compactness together with the
   clopen-basis hypothesis gives a compact-clopen local base, hence the
   topological hypothesis of CLD Section 3.1.1.  Taking every locally closed
   subset as a domain satisfies all four axioms in Section 3.1.2.  Locally
   constant functions satisfy G-gluing and all the parlinear axioms in
   Section 3.1.3; on a compact domain their image is finite, hence is a legal
   compact polyhedron for the standing `(Q,R)` parameters.  Taking the
   affine presheaf equal to the parlinear sheaf satisfies Section 6.1.1, and
   the product is the legal CLD product of Sections 9.1.1--9.1.4.

3. **Product smooth/psh characterization: PASS.**  Product affine
   coordinates split locally into a locally constant term in `Z` and an
   affine term in the Euclidean variable.  After an ordinary, equivalently
   clopen, shrinking in `Z`, the former is constant.  Definition 6.2.1 then
   gives precisely the functions locally independent of `Z` and smooth in
   the Euclidean variable; the identity chart on the Euclidean factor gives
   the converse.  The positivity condition is exactly positive
   semidefiniteness of the Euclidean Hessian, with the `d=0` case vacuous.

4. **Comparison sheaf and minimality: PASS.**  The factorization condition
   is local and therefore defines a genuine subsheaf.  It contains every
   smooth psh generator after a clopen shrinking.  Once sequential closure
   is proved, the minimality in CLD Definition 8.1.1 yields the claimed
   inclusion from the full psh sheaf.

5. **Countable Stone quotient construction: PASS.**  For each row,
   compactness of the common core gives a finite product cover by local
   factorizations.  Across the countably many rows, the resulting clopen
   generators generate a countable Boolean algebra.  Its evaluation map has
   compact, metrizable, zero-dimensional image.  Membership in the recorded
   clopens and separation by each local quotient's countable clopen base
   prove that every row is constant on the fibres of the common
   `q x id` map.

6. **Upper-semicontinuity descent: PASS.**  A decreasing limit of the local
   upper-semicontinuous rows has open strict sublevel sets.  For a point of a
   descended strict sublevel, compactness of the fibre gives a finite family
   of product neighbourhoods.  Their union/intersection construction and
   closedness of the compact-to-Hausdorff map `q` produce a product
   neighbourhood downstairs.  Thus joint upper semicontinuity is proved
   without assuming, unsupportedly, that `q x id` is automatically a
   quotient map.

7. **Extended convex dichotomy and passage to the limit: PASS.**  The local
   midpoint argument makes both the finite locus and the `-infinity` locus
   open.  Connectedness of the ball gives the dichotomy, and segment
   subdivision globalizes local convexity.  Convex inequalities pass through
   a decreasing finite-convex sequence; if the limit has one polar value, a
   slightly extended segment propagates it to every point.

8. **Sup-envelope monotonicity and convergence: PASS.**  Refinement of the
   nested clopen partitions, decrease of the radii, and decrease of the
   floors from `-k` to `-(k+1)` give exact cross-level monotonicity.  Mesh
   convergence together with joint upper semicontinuity identifies the
   pointwise limit at both finite and polar points.  In the finite-value case
   one also takes `k` large enough that the floor lies below the selected
   upper level; this is immediate and is merely an implicit phrase, not a
   proof gap.

9. **Euclidean mollification and tail correction: PASS.**  Each envelope
   branch is finite continuous convex.  Compact containment and finiteness of
   each partition give one mollification scale for that level.  Jensen's
   inequality supplies the lower error bound and uniform convergence supplies
   the upper one.  With
   `c_k = sum_{j >= k+1} eta_j`, the index identity
   `c_k = eta_{k+1} + c_{k+1}` converts almost monotonicity into
   `g_{k+1} <= g_k`; mollification errors and tails both vanish, so the limit
   is the required function.

10. **The case `d=0`: PASS.**  The partition envelopes are finite locally
    constant functions, hence smooth psh for the stated affine structure.
    Refinement and the floors make them decreasing, and upper
    semicontinuity plus shrinking mesh gives the asserted limit without
    convolution.

11. **Nonmetrizable cubes: PASS.**  For every index set `Lambda`, the cube
    `{0,1}^Lambda` is compact Hausdorff and zero-dimensional.  The proof never
    assumes that `Z` itself is metrizable: it explicitly constructs the
    countable metrizable quotient needed by each generated psh function.

12. **Scope firewall: PASS.**  The result concerns only the exact product
    with locally constant affine structure in the parameter direction.  It
    makes no inference for nontrivial affine parameter directions,
    polyhedral face gluings, or arbitrary affine G-tropical spaces.  It
    therefore narrows P07.1 but does not retire that open problem.

## Final audit status

**PASS: zero critical errors and zero unresolved proof/source gaps.**

This was an independent fail-closed audit of the exact bytes identified
above.  No priority claim was assessed.  The frozen candidate statement and
proof were not edited, and no production submission was made.
