# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new general result is Proposition 18.8.31 on printed pages
  1157--1158.
- It separates the common exact mixed-tower mechanism from the earlier
  curve-specific theorem and transfers unique descent, classical
  pluriharmonicity, real-harmonicity, and first-current rigidity from any
  admissible bottom space.
- The proof of `thm:p062-mixed-bundle-towers-over-curves` now invokes this
  general transfer proposition.
- Arbitrary fibrations and stages without the stated local trivializations
  remain outside the conclusion.  P06.2 remains open and the active-atom
  count is unchanged.

## Validation

- Strict Mingchen writing audit on `STATEMENT.tex` and `PROOF.tex`: 0 errors
  and 0 warnings.
- `git diff --check`: passed.
- Reference and structure check: 295 files in the closure, 11,042 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  unresolved citation or reference, or multiply defined label in the final
  log.
- Final full-book PDF: 3,740 physical pages and 17,856,283 bytes.
- Final PDF SHA-256:
  `32ce0090db94948c999eddb0ed1cac9616bfc251e525aedc9535037e3e07a9a1`.
- Final log SHA-256:
  `5a7b03f368dd453963fb053195acb2867aa260d21a4e84a10919c6fefcbcdca9`.
- The proposition and proof on physical PDF pages 1225--1226 were rendered
  and visually inspected.  No clipping, collision, malformed formula, or
  new bad box was found.
