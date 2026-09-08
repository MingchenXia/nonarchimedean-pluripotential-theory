# P14.3 finite-energy Kähler live integration — 8 September 2026

## Scope

The reviewed P14.3 v3 argument is now integrated into Chapter 71 as:

- `thm:p143-dominated-divisorial-density`, which refines rational
  divisorial density to a net `q <= v` on every coherent ideal; and
- `cor:p143-all-point-kahler-comparison`, which applies that refinement to
  the upper-semicontinuous raw transform in the finite-energy Kähler domain.
  Its immediate consequence `cor:p141-finite-energy-raw-image` identifies
  the raw-transform image in that same domain with the finite-energy MP cone.

The corollary identifies the literal raw ideal-valuative transform with the
corresponding MP finite-energy potential at every semivaluation.  It does
not assert MP positivity for arbitrary pseudoeffective, non-nef, or
genuinely transcendental compact Kähler classes, construct a new
Monge--Ampère theory, or retire P14.1 or P14.3.

## Review binding

The exact v3 review response remains `correct`, with zero critical errors
and zero gaps.  Its immutable receipt is:

| Artifact | SHA-256 |
| --- | --- |
| Request | `1b9f142379c905a2d07517ed552316a9cdf94e9295c73f3b198a21ae8cd1352d` |
| Response | `daba7ab28e131bf8235ff45278c87022625d5d5bf37a83f39983cda98c9a0bde` |
| Headers | `45433060083533745bdadd7f0ba0df0d7eb0e095f0cb904823169d54831ed6b4` |

The current source retains the v3 proof's two safeguards: the
annihilator argument gives domination on all coherent ideals, and the
central-ideal argument handles zero-weight components without forming
`0*(+infinity)`.

## Current-source and build checks

The integrated labels begin at source lines 1107 and 1239 in
`parts/part6/ch71_pseudoeffective_mp_dxz.tex`; the inclusive source window
1100--1265 has SHA-256
`1f57fb4a81eb177fa701d063dd5be0c52d5e24a80e6da64b8e3d0f9584d76d20`.

The full then-current working tree was rebuilt with

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

and completed successfully with 3,522 pages.  The final log has no LaTeX
errors, undefined control sequences, undefined references or citations, or
multiply defined labels.  The P14.3 source hunks were separately checked by
`git diff --cached --check`; their staged SHA-256 values, plus the working-tree
PDF built at the integration checkpoint, are:

| Artifact | SHA-256 |
| --- | --- |
| staged `parts/part6/ch71_pseudoeffective_mp_dxz.tex` | `dfe67cf748bd603ddd3ebc23b0e5e107d4a0c66fe5bdec54a69022fcb97a73d2` |
| staged `parts/part6/ch72_major_open_problems.tex` | `cd9d515bb435979ecd1be2d607930013285f6f927e0f21118d99897806a6882b` |
| staged `editorial/open_problem_atomic_inventory_20260824.md` | `a7d75805818b48c54b3ff2c7626b30bb863e8560b879f152de30483e629f2c5a` |
| working-tree `book.pdf` | `e0a14a9ece93d0e94a045e5640b661cad9890c498a32c53177d36607328e0c35` |

## Status boundary

This integration narrows P14.3 to its actual residual generality.  The
separate source-closed production-verification record remains incomplete,
and Chapter 72 and the atomic inventory therefore retain P14.3 as an active
T4 problem.  No atom count or tier count changes here.
