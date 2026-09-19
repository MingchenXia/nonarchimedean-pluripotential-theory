# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new result is Corollary 18.8.28 on printed page 1163.
- Globally coordinated annular product stages in a mixed tower may now be
  replaced by curve-locally coordinated stages: one analytic open cover of
  the original curve makes the whole base-changed tower satisfy the
  interleaved theorem.
- Annular radii, coordinates, and product trivializations may have monodromy
  across the cover.  Every continuous zero-current function remains
  classically pluriharmonic, locally real-PL, and GJR harmonic.
- No global coefficient formula is asserted.  Arbitrary intermediate-base
  local annular charts remain outside the result.  P06.2 remains open and
  the active-atom count is unchanged.

## Validation

- Strict Mingchen writing audit on `STATEMENT.tex` and `PROOF.tex`: 0 errors
  and 0 warnings.
- `git diff --check`: passed.
- Reference and structure check: 299 files in the closure, 11,044 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  unresolved citation or reference, or multiply defined label in the final
  log.
- Final full-book PDF: 3,744 physical pages and 17,873,369 bytes.
- Final PDF SHA-256:
  `48ce1844b134e699b286cd06eceb68b3f028fe33847d1f6cab6d15d66ab5c426`.
- Final log SHA-256:
  `cd4e83967f81bfb244f06101d2028c9fbc0e55dcb5daba81dbad1ec73d0712f5`.
- The corollary on physical PDF page 1231, the Chapter 18 comparison-table
  row on physical page 1280, and the Chapter 72 detailed and summary updates
  on physical pages 3516--3517 and 3554 were rendered and visually
  inspected.  No clipping, collision, malformed formula, or new bad box was
  found.
