# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- Corollaries 18.8.37--18.8.39 appear on printed pages 1167--1168.
- A globally coordinated curve-polyannulus product may now be the bottom of
  an arbitrary finite mixed exact tower while retaining its unique
  logarithmic coefficient formula.
- Locally trivial curve-polyannulus and mixed curve-polycylinder bundles may
  likewise be the bottom, retaining classical pluriharmonicity, local
  real-PL regularity, and GJR harmonicity without a global formula.
- The results do not interleave annular stages arbitrarily.  P06.2 remains
  open and the active-atom count is unchanged.

## Validation

- Strict Mingchen writing audit on `RESULTS.tex`: 0 errors and 0 warnings.
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
- The three corollaries on physical PDF pages 1235--1236, the Chapter 18
  comparison-table row on physical pages 1277--1278, and the Chapter 72
  insertion on physical page 3514 were rendered and visually inspected.
  No clipping, collision, malformed formula, or new bad box was found.
