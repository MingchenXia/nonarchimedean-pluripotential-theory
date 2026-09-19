# P06.2 polyannulus coefficient monodromy v63: build report

Date: 20 September 2026

Status: full-book integration passed after the automatic second pass.

## Integrated result

Proposition 18.8.28 identifies the intrinsic coefficient data of every
analytically locally trivial rank-$s$ strict open-polyannulus bundle over the
published curve domain.  Logarithmic coordinates on two product charts differ
by a locally constant invertible real matrix and a vector of continuous
zero-current base functions.  The linear and translation terms satisfy the
affine Cech cocycle law.  They therefore define a rank-$s$ real local system
and an affine zero-current translation cocycle, while the chartwise slope
vectors of every continuous zero-current function glue as a parallel section
of the dual local system.

The result does not assert integral monodromy, global annular coordinates, or
global product structure.  P06.2 remains open outside the recorded locally
trivial curve-polyannulus range, and the active-atom count is unchanged.

## Proof and scope audit

- `lem:ch15-log-smooth` makes the logarithmic absolute value of every overlap
  coordinate an admissible zero-current function.
- `thm:p062-open-polyannulus-products-over-curves` gives its unique base and
  slope coefficients in the other chart.
- Applying the same construction to the inverse transition proves matrix
  invertibility; comparison on triple overlaps proves the two cocycle laws.
- Applying uniqueness to a general zero-current function gives the dual slope
  transition and translated base-coefficient law.
- The union of two atlases gives the canonical comparison under refinement or
  replacement.
- No external theorem or model-backed verifier was used.  The inspected
  `integral-logarithm-cocycle-line-bundle-absorption` mechanism was rejected as
  inapplicable because its complex Stein/logarithm-branch cohomology
  hypotheses do not occur here.

## Automatic second pass

The second pass replaced an overbroad claim that the failure of a global
formula was "completely recorded" by the precise statement that the cocycle
records the failure of the chartwise coefficient data to glue in the chosen
coordinates.  It also made the non-integrality firewall explicit and
propagated the result into the Chapter 18 comparison table and the Chapter 72
current-results summary.  All audits and the full build were rerun after these
changes.

## Mechanical verification

- Forced first full-book build: PASS.
- Post-second-pass full-book `latexmk` build: PASS and converged.
- Output: `book.pdf`, 3333 pages, 17,674,884 bytes, PDF 1.5.
- Reference closure: 355 files, 11,324 labels, 0 multiply defined labels,
  0 dangling references, and no per-file structural error.
- Final log scan: no undefined citation, undefined reference, multiply defined
  label, or unresolved rerun diagnostic.
- Strict Mingchen audit of the live statement and proof: 0 errors and
  0 warnings; the bibliography-aware pass has the same result.
- Atomic inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms in 14
  formal problem environments, with tier vector `(0,5,8,16,17)`.
- `git diff --check`: PASS.

## Visual audit

Rendered and inspected after the second pass:

- Proposition 18.8.28 and its proof: physical PDF pages 1289--1290, printed
  pages 1221--1222;
- Chapter 18 synthesis: physical page 1323, printed page 1255;
- Chapter 18 comparison table: physical page 1354, printed page 1286;
- Chapter 72 detailed P06.2 update: physical page 3149, printed page 3081;
- Chapter 72 current-results summary: physical page 3177, printed page 3109.

The statement, four displays, proof, prose integrations, and table row are
legible.  No clipping, collision, malformed formula, or obscuring overfull box
appears on the affected pages.

## Exact hashes

- `STATEMENT_LIVE.tex`:
  `f88234e125282350fffda764e3825003b33e41e9e210d2a3d9d8e98170d9b843`.
- `PROOF_LIVE.tex`:
  `3beed16ac5cc401f83813a3c4e9a3cfdd0ff5313bc56ef90429239f5b5f4d650`.
- `AUDIT_LIVE.md`:
  `d91ce345e13a3ff7f0f0b8db55b09e5861cfdd4fdd940bb31e7bf25fa2d9c270`.
- `SOURCES_LIVE.md`:
  `25b2c0d1a56ae1f080cdba6a37d65d90c4aa10d1a6414d04c2a4ac0252a1ce6d`.
- `ch18_delta_forms.tex`:
  `10eddd1af54ce395216de1af90f269c618a5d42cc74e047f1dc2082342f9faa9`.
- `ch72_major_open_problems.tex`:
  `a6e2057814e17ca09befe26149b16828a9daa9d1b9f1b0135cce6c46363ba517`.
- `open_problem_atomic_inventory_20260824.md`:
  `2e50a26147db8bef5e9d3e588bb108812223a36191c768b47a17254fdd82be9b`.
- `book.pdf`:
  `7045fe612e7967a7811bddbb1e407fbe0f9e45ab8ea5be1226507c2db32770e4`.
- `book.log`:
  `18915c8cfa8610fb1c84edc10e68effd351a8876afc44c78e54249ed093e8df9`.
