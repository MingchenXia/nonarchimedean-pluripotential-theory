# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new result is Theorem 18.8.20 on printed pages 1161--1163.
- A finite tower over a published curve may now interleave globally
  coordinated standard strict open-polyannulus product stages arbitrarily
  with all three exact bundle types.
- Every continuous zero-current function on the tower top has a unique
  formula containing one logarithmic term for every annular coordinate
  introduced anywhere in the tower.  Its zero-current base coefficient and
  all locally constant slope coefficients live on the original curve.
- The function is classically pluriharmonic, locally real-PL, and
  Gubler--Jell--Rabinoff harmonic.
- Locally twisted annular monodromy remains outside the theorem.  P06.2
  remains open and the active-atom count is unchanged.

## Validation

- Strict Mingchen writing audit on `STATEMENT.tex` and `PROOF.tex`: 0 errors
  and 0 warnings.  The chapter-level integration prose was reviewed in its
  compiled context rather than counting unrelated legacy diagnostics from
  the full chapter files as part of this packet.
- `git diff --check`: passed.
- Reference and structure check: 297 files in the closure, 11,043 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  unresolved citation or reference, or multiply defined label in the final
  log.
- Final full-book PDF: 3,744 physical pages and 17,869,145 bytes.
- Final PDF SHA-256:
  `cb756d3fac065ea1ba379aadac9cf4579da04a0876bb7a0c0c0a3f744de4adea`.
- Final log SHA-256:
  `bf427eaa6dcf17132c89d0e36e2cdb382d7287abf3a007b684c30a8e0be66477`.
- The theorem and proof on physical PDF pages 1229--1231, the Chapter 18
  comparison-table row on physical page 1279, and the Chapter 72 detailed
  and summary updates on physical pages 3516 and 3554 were rendered and
  visually inspected.  No clipping, collision, malformed formula, or new
  bad box was found.
