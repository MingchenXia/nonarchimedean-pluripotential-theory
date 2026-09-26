# P05.1 one-dimensional literal regularity classification: integration audit

Date: 26 September 2026

## Integrated result

Chapter 72 now contains
`thm:frontier-polyhedral-one-dimensional-literal-classification`.  For a
finite one-dimensional balanced rational polyhedral space and a literal
reference positive at infinity, it proves the equivalence

```text
literal regularity  <=>  degree zero  <=>  compactness.
```

The positive-degree direction is global and does not use the local relation
cones.  Starting from `phi=max(gamma,C)`, it realizes the rational convex
combination `(1-1/N)gamma+(1/N)phi` as the exact envelope of a bounded
literal obstacle.  The obstacle is formed by integral-slope concave roofs on
the edge cells.  A nonintegral slope of the envelope supplies an explicit
uniform separation from every literal convex PA approximant.

## Editorial effect

- The former positive-degree higher-rank proper-face boundary is closed in
  dimension one.
- The earlier one-vertex and strict-vertex theorems remain useful local and
  quantitative special cases, but are no longer the limit of the
  one-dimensional classification.
- P05.1 remains active for higher-dimensional real-PA and literal
  classification, arbitrary nonseparable product obstacles, and the source
  coefficient-convention repair.
- P05.2 remains active outside its one-dimensional real-PA classification.
- The book-wide inventory remains 42 active atoms in 12 environments, with
  tiers `(0,3,7,15,17)`.

The live chapter, README, book plan, research ledger, open-problem programme,
and atomic inventory have been updated consistently.  Historical status
entries remain chronological records of the narrower bounds available when
they were written.

## Verification

- Scoped Mingchen-writing audit: zero errors and zero warnings.
- Minimal packet: 3 pages, 125,831 bytes, SHA-256
  `02ffaf8ffb0ea10aed538d951c0124e325b331cf7887c1c425ce69c064a6dc20`.
- Full source closure: 421 files and 11,877 unique labels; zero missing
  inputs, duplicate labels, dangling references, or structural failures.
- Inventory checker: 42 atoms across 12 Chapter 72 environments with the
  declared tier totals.
- All 6 available checker tests pass.
- Full book: 4,098 pages, 19,494,764 bytes, SHA-256
  `c28a0be795db2faa104ac080b91bf3f699a78b1e0910233fb478b48b76f141b4`.
- Final log: no unresolved references or citations, rerun requests, missing
  files, horizontal or vertical overflows, emergency stops, or fatal errors.
  The 13 inherited Chapter 70 duplicate destinations are unchanged.
- All three minimal pages and full-book physical pages 3812--3818 were
  rendered and inspected without visual defects.

No model-verifier result is claimed for this theorem.
