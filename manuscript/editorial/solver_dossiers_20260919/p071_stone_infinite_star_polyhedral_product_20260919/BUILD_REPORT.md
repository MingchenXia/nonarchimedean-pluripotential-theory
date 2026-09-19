# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new result is Theorem 16.2.14 on printed pages 763--767 and physical
  PDF pages 831--835.
- It identifies the first-stage, full generated, and explicit comparison
  sheaves on the product of a locally constant Stone parameter, an arbitrary
  exact CLD infinite star, and one active convex polyhedron.
- Every germ has one decreasing generator sequence on a fixed smaller
  product neighbourhood.
- P07.1 remains open outside the theorem's exact CLD, locally constant
  Stone, jointly convex, single-polyhedron scope.  The active-atom count is
  unchanged.

## Validation

- Strict Mingchen writing audit on `STATEMENT.tex` and `PROOF.tex`: 0 errors
  and 0 warnings.  The chapter-level integration prose was reviewed in its
  compiled context rather than counting unrelated legacy diagnostics from
  the full chapter files as part of this packet.
- A second prose and formula pass found and repaired two spacing corruptions
  before the final build: the relative-closure superscript and the product
  in the metric regularization formula.
- `git diff --check`: passed.
- Reference and structure check: 301 files in the closure, 11,059 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  unresolved citation or reference, or multiply defined label in the final
  log.
- Final full-book PDF: 3,748 physical pages and 17,895,146 bytes.
- Final PDF SHA-256:
  `962c360decb07d50164ff6aff26f0ed2bf102732789f56f9bf12707c9bd1153e`.
- Final log SHA-256:
  `a0cb7eca70b52d2123df52801e45bcc678f129a64198b69442f187eab0690e52`.
- The theorem and proof on physical PDF pages 831--835, the Chapter 16
  overview on physical page 840, and the Chapter 72 updates on physical
  pages 3527--3529 were rendered and visually inspected.  The repaired
  formulas were re-rendered from the final PDF on physical pages 833--834.
  No clipping, collision, malformed formula, or new bad box was found.
