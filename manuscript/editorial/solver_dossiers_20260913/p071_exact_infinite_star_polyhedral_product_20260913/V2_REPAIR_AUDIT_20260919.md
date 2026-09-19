# P07.1 V2 repair audit

Date: 19 September 2026 (Asia/Shanghai)

Status: both V1 gaps repaired and independently accepted by the local
`gpt-6-astra`/`xhigh` verifier.  V2 returned final `correct`, zero critical
errors, and zero gaps, and is eligible for theorem promotion subject to the
ordinary manuscript integration gates.

## Gap-to-repair map

1. The finite-product proof no longer imports the disputed smoothing step.
   For each sampled scalar profile it derives the Farkas compatibility
   inequalities directly from junction tuples.  A separating-hyperplane
   alternative yields a common ambient covector below all first branch
   slopes.  The proof then defines the regularized maximum by convolution,
   records its quantitative sandwich and exact-coordinate property, and
   obtains a common ambient affine node collar on the finite star.
2. The finite exact-star insertion lemma replaces the single truncation by
   a sequence `K_j` decreasing to negative infinity below `min(phi)`.  Since
   the Jensen measure has finite support, both sides pass monotonically to
   the required extended-real inequality atom by atom.

## Local gates

- the nine-page compact-core feasibility harness compiles in two passes;
- the whole 3718-page book compiles after the finite-product repair;
- the reference audit reports 10995 labels, zero multiply defined labels,
  and zero dangling references;
- the Chapter 72 inventory audit reports 46 active atoms and passes;
- the automatic house-style audit reports no violation in either newly
  written repair block; the surrounding legacy files retain their pre-existing
  `\\(...\\)` inline-math convention;
- book pages 733--736 containing the finite-star repair were rendered at
  140 dpi and visually inspected; formulas, tags, margins, and page breaks
  are clean;
- `git diff --check` passes;
- the seven overfull boxes in the full book are pre-existing and none is in
  either repaired proof block.

The V2 hashes and exact packet order are frozen in
`SUBMISSION_MANIFEST_V2_20260919.md`.  The required final `correct` verdict
with zero critical errors and zero gaps was received on 19 September 2026.
The archived request, response, headers, and their hashes are recorded in
`VERIFICATION_RECEIPT_ASTRA_V2_20260919.md`.
