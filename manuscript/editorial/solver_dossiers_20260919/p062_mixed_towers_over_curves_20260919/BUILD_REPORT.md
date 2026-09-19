# Build report

Date: 19 September 2026

Status: full-book integration passed.

## Result

- The new result is Theorem 18.8.19 on printed page 1157.
- It gives unique descent of every continuous zero-current function through
  a finite tower whose stages, in arbitrary order, are locally trivial
  standard strict open-polydisc bundles, projective-space bundles, or proper
  smooth connected curve bundles over a published curve.
- The conclusion is classical pluriharmonicity, local real-PL regularity,
  and Gubler--Jell--Rabinoff harmonicity on the top space.
- Every stage retains the full hypotheses of its source descent proposition;
  no arbitrary fibration, annular fibre, or nonproduct germ is claimed.
  Consequently P06.2 remains open and the active-atom count is unchanged.

## Validation

- Strict Mingchen source audit on `STATEMENT.tex` and `PROOF.tex`:
  0 errors and 0 style warnings.  The bibliography-aware pass records the
  existing freshness warning that `GR25Classical` is still catalogued as an
  arXiv-only source; the cited pullback proposition is already used by the
  three source corollaries being iterated here.
- `git diff --check`: passed.
- Reference and structure check: 290 files in the closure, 11,037 labels,
  no multiply defined label, no dangling reference, and no per-file
  structural error.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms
  across 14 problem environments, with tier vector `(0,5,8,16,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  undefined control sequence, unresolved citation or reference, or multiply
  defined label in the final log.
- Final full-book PDF: 3,734 physical pages and 17,835,427 bytes.
- Final PDF SHA-256:
  `f105e46501c9a850c3befe3e07db104e12e9109e8a1d7a71eb84121c5607e684`.
- Final log SHA-256:
  `7dc7cd7be245a8435d15cee24e7c147a4c02ae2f96616a5496b31b8baa62af4e`.
- The theorem and proof on physical PDF pages 1225--1226, the Chapter 18
  comparison-table row on physical page 1273, and the Chapter 72 insertion
  on physical pages 3507--3508 were rendered and visually inspected.  No
  clipping, collision, malformed formula, or new bad box was found.
