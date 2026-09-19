# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new result is Corollary 18.8.10 on printed page 1091.
- Pointwise analytic toric charts that split after a complete algebraic
  extension may now be combined with an arbitrary finite product of good
  strict analytic curves and a final factor with quasi-smooth reduction.
- Every classically pluriharmonic function in this range is real-PL and
  Gubler--Jell--Rabinoff harmonic, including on analytic local models.
- The theorem does not construct splitting charts, allow merely
  nonalgebraic splitting extensions, or treat nonproduct singular germs.
  P06.1 remains open, and the active-atom count is unchanged.

## Validation

- Strict Mingchen writing audit on `STATEMENT.tex` and `PROOF.tex`, against
  `bibliography/NonArchimedean.bib`: 0 errors and 0 warnings.
- `git diff --check`: passed.
- Reference and structure check: 305 files in the closure, 11,061 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  unresolved citation or reference, or multiply defined label in the final
  log.
- Final full-book PDF: 3,750 physical pages and 17,906,542 bytes.
- Final PDF SHA-256:
  `cfca788032f70588d270eb3f995d8f19871bd34c3c573a8543f9906970210554`.
- Final log SHA-256:
  `8399771fab37e2660f21c0bd5649d4b31ecdf70d20583394fd5cd3a6a6d06b73`.
- The corollary and proof on physical PDF page 1159, the Chapter 18 overview
  on physical page 1160, and the Chapter 72 update on physical pages
  3512--3513 were rendered and visually inspected.  No clipping, collision,
  malformed formula, or anomalous line break was found.
