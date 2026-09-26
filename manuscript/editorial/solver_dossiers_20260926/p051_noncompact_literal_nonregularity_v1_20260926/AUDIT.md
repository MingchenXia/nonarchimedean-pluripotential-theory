# P05.1 noncompact literal nonregularity: audit

Date: 26 September 2026

## Claim audited

For every finite embedded noncompact rational polyhedral space and every
literal integral-slope polyhedrally convex reference positive at infinity,
one bounded literal obstacle has an exact envelope with a nonintegral slope
on a rational segment.  The envelope is uniformly separated from every
literal convex PA function, so literal regularity fails in every dimension.

## Mathematical audit

1. The rational truncation `phi=max(gamma,C)` is literal and polyhedrally
   convex.  Positive recession slopes make `D=phi-gamma` nonnegative,
   bounded and compactly supported.
2. Cutting the finite complex by `gamma=C` and taking a rational simplicial
   refinement makes `D` affine on every cell.  Its nonzero region is
   bounded on each original unbounded cell, so every refined unbounded cell
   has `D=0`.
3. Choosing `C>gamma(x)` in a noncompact connected component makes `D`
   positive at `x` and zero near infinity in that component.  Thus `D` is
   nonconstant and has a nonzero integral linear part on a bounded
   positive-dimensional cell.
4. The ambient lattice norm
   `rho_v(y)=max_j |m_j(y-v)|` is literal PA, nonnegative and vanishes only at
   the rational vertex `v`.  Compact support and local PA Lipschitz control
   give an integer `A_v` for which `d(v)+A_v rho_v` majorizes `d=D/N`
   globally.
5. The minimum of `D` and all vertex cones is again literal PA after a
   finite rational refinement.  Every term majorizes `d`; the cone based at
   `v` gives equality at `v`; and the `D` term makes the obstacle bounded
   and zero on unbounded cells.
6. The rational convex combination `P=gamma+D/N` is a convex envelope
   competitor.  Any other competitor is bounded by `P` at every vertex.
   Ordinary convexity and barycentric coordinates give the bound on bounded
   cells, while equality of the obstacle with `P` gives it directly on
   unbounded cells.  Hence the envelope identity is exact.
7. On a primitive rational segment in a cell where `D` has nonzero linear
   part `k`, choosing `N>|k(w)|` makes the target slope an integer plus the
   nonzero fraction `k(w)/N`.  The midpoint left derivative of every literal
   convex PA function is integral.  The floor/ceiling alternatives give the
   uniform separation `L*dist(q,Z)/4`.
8. Uniform separation excludes every literal regularization, including
   every decreasing uniform approximation.  The constructed bounded literal
   obstacle therefore disproves regularity.

## Exceptional cases and scope

- A rational simplicial refinement supplies vertices even when an initial
  affine or lineal structure has none.
- Disconnected spaces cause no issue: the truncation is chosen nonconstant
  on one noncompact component and remains compactly supported globally.
- The proof does not use balancing, weights, degree, or local relation cones.
- Compact higher-dimensional literal regularity, high-dimensional real-PA
  regularity, and P05.2 orthogonality remain outside the theorem.

No model-verifier result is claimed.

## Verification record

- Scoped Mingchen-writing audit: zero errors and one reviewed warning that
  `BMPS26` remains arXiv-only.
- Minimal compile: 3 pages, 136,953 bytes, with no unresolved reference,
  citation, rerun, overflow, missing-file, emergency-stop, or fatal-error
  diagnostic.
- Full source closure: 423 files and 11,884 unique labels, with zero missing
  inputs, duplicate labels, dangling references, or structural failures.
- Inventory checker: 42 active atoms in 12 environments, tiers
  `(0,3,7,15,17)`; all 6 checker tests pass.
- Full book: 4,100 pages, 19,505,879 bytes, SHA-256
  `97e82fc6d2c5ceb3622e50292aebf1b0866958bffdea8e9ae7a83fa6b1e61775`.
- The final log has no unresolved references or citations, rerun requests,
  missing inputs, horizontal or vertical overflows, emergency stops, or
  fatal errors.  The 13 inherited Chapter 70 duplicate destinations remain.
- All 3 minimal pages and full-book physical pages 3815--3819 were rendered
  and visually inspected without defects.
