# P05.1 noncompact literal nonregularity: integration audit

Date: 26 September 2026

## Integrated result

Chapter 72 now contains
`thm:frontier-polyhedral-noncompact-literal-nonregularity`.  For every
noncompact rational polyhedral space admitting a finite embedded structure
and every literal integral-slope convex reference positive at infinity, it
constructs a bounded literal obstacle whose exact envelope has a
nonintegral slope on a primitive rational segment.  The envelope is
quantitatively separated from every literal convex PA approximant.

The proof truncates the reference by `phi=max(gamma,C)`, sets
`D=phi-gamma`, and chooses the rational combination `P=gamma+D/N`.  On a
finite rational simplicial refinement, ambient integral lattice norms based
at the vertices produce finitely many cones that majorize `D/N`.  The
minimum of these cones with `D` is a bounded literal obstacle, equals `D/N`
at every vertex, and vanishes on every unbounded cell.  Convexity on bounded
cells and the obstacle inequality on unbounded cells force the exact
envelope identity.  A nonzero integral slope of `D`, divided by a larger
integer `N`, gives the uniform separation.

## Editorial effect

- Literal regularity is now disproved on every noncompact finite rational
  polyhedral space in every dimension, without balancing, weights, purity,
  degree, or local-relation hypotheses.
- In particular, the source's literal complete-affine regularity assertion
  fails in every positive dimension.  The positive complete-affine theorem
  retained by the book is explicitly in the real-scalar PA category.
- Together with the one-dimensional compact theorem, this closes the
  noncompact literal part of P05.1 in every dimension.
- P05.1 remains active for the compact higher-dimensional literal case, the
  higher-dimensional real-PA classification, arbitrary nonseparable product
  obstacles, and source coefficient-convention repair.
- P05.2 remains active outside its one-dimensional real-PA classification.
- The book-wide inventory remains 42 active atoms in 12 environments, with
  tiers `(0,3,7,15,17)`.

The live chapter, README, book plan, research ledger, attempt ledger, atomic
inventory, and chronological chapter status have been updated consistently.
Historical verification records are not retroactively extended.

## Verification

- Scoped Mingchen-writing audit: zero errors and one reviewed warning that
  `BMPS26` remains arXiv-only.
- Minimal packet: 3 pages, 136,953 bytes, SHA-256
  `da9f2d8cfb585cb4d71b45097b95484ea32bdb134d7152cf5ad8932e4681ff06`.
- Full source closure: 423 files and 11,884 unique labels; zero missing
  inputs, duplicate labels, dangling references, or structural failures.
- Inventory checker: 42 atoms across 12 Chapter 72 environments with the
  declared tier totals.
- All 6 available checker tests pass.
- Full book: 4,100 pages, 19,505,879 bytes, SHA-256
  `97e82fc6d2c5ceb3622e50292aebf1b0866958bffdea8e9ae7a83fa6b1e61775`.
- Final log: no unresolved references or citations, rerun requests, missing
  files, horizontal or vertical overflows, emergency stops, or fatal errors.
  The 13 inherited Chapter 70 duplicate destinations are unchanged.
- All 3 minimal pages and full-book physical pages 3815--3819 were rendered
  and inspected without visual defects.

No model-verifier result is claimed for this theorem.
