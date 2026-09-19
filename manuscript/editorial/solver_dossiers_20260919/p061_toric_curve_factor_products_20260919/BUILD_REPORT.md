# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new result is Corollary 18.8.9 on printed pages 1089--1091.
- A split toric factor may now occur simultaneously with an arbitrary finite
  product of good strict analytic curves and a final good strict factor with
  quasi-smooth reduction.
- The same conclusion holds for analytic local product models and for toric
  forms split by a complete extension obtained by completing an algebraic
  extension.
- Every classically pluriharmonic function in this range is real-PL and
  Gubler--Jell--Rabinoff harmonic.
- Higher-dimensional reduced singular factors outside the toric factor,
  nonsplit forms without the stated algebraic splitting extension, and
  nonproduct singular germs remain outside the result.  P06.1 remains open,
  and the active-atom count is unchanged.

## Validation

- Strict Mingchen writing audit on `STATEMENT.tex` and `PROOF.tex`, against
  `bibliography/NonArchimedean.bib`: 0 errors and 0 warnings.
- `git diff --check`: passed.
- Reference and structure check: 303 files in the closure, 11,060 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Forced full-book `latexmk` run: passed and converged, with no fatal TeX
  error, unresolved citation or reference, or multiply defined label in the
  final log.
- Final full-book PDF: 3,750 physical pages and 17,901,499 bytes.
- Final PDF SHA-256:
  `b62d1ad71a48df21fca52bea553503c5ccfc83b407a01fb20747963f2e463b38`.
- Final log SHA-256:
  `ea454af3beac0871945e5d44c50f2eb5c124f274aa3dba9b86dec554a3d8662f`.
- The corollary and proof on physical PDF pages 1157--1159 and the Chapter
  72 update on physical page 3512 were rendered and visually inspected.  No
  clipping, collision, malformed formula, or anomalous line break was found.
