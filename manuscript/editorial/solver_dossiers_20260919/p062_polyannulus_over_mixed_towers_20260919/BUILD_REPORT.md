# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new result is Corollary 18.8.27 on printed page 1158.
- Over the boundaryless top of a finite mixed exact tower from
  `thm:p062-mixed-bundle-towers-over-curves`, every continuous zero-current
  function on a globally coordinated finite standard strict open-polyannulus
  product has a unique coefficient formula.
- The zero-current base coefficient and every locally constant annular slope
  coefficient descend uniquely to the original published curve.
- The total function is classically pluriharmonic, locally real-PL, and
  Gubler--Jell--Rabinoff harmonic.
- Locally twisted annulus bundles, annular stages inside the tower, arbitrary
  fibrations, and nonproduct germs remain outside the statement.  P06.2
  remains open and the active-atom count is unchanged.

## Validation

- Strict Mingchen writing audit on `STATEMENT.tex` and `PROOF.tex`:
  0 errors and 0 warnings.
- `git diff --check`: passed.
- Reference and structure check: 292 files in the closure, 11,038 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  undefined control sequence, unresolved citation or reference, or multiply
  defined label in the final log.
- Final full-book PDF: 3,736 physical pages and 17,842,839 bytes.
- Final PDF SHA-256:
  `3bd2b71c679749ec49a0796ad8d81c556029ada03e1941c321af8dfc905dc2ef`.
- Final log SHA-256:
  `737b0ecd927281616f46a729e3a65efc6eda26e3531af4388bd6afdfa078a163`.
- The corollary and proof on physical PDF pages 1226--1227, the Chapter 18
  comparison-table row on physical page 1274, and the Chapter 72 insertion
  on physical page 3510 were rendered and visually inspected.  No clipping,
  collision, malformed formula, or new bad box was found.
