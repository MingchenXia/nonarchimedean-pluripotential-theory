# Live build report

Date: 20 September 2026

## Static gates

- The strict Mingchen TeX audit of `STATEMENT_LIVE.tex` and
  `PROOF_LIVE.tex` returned 0 errors and 0 warnings.
- The Chapter 72 inventory checker returned 46 active atoms in 14 formal
  problem environments, with tiers `(0, 5, 8, 16, 17)`.
- The build-closure reference checker inspected 373 files and 11,385 labels,
  with 0 multiply defined labels, 0 dangling references, and clean per-file
  structure.
- `git diff --check` passed.

## Full book build

The final second-pass command

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

completed successfully and converged.  The resulting `book.pdf` has 3,363
pages and 17,803,831 bytes.  Its SHA-256 digest is

```text
62ac3c41ea8806670160927029f579e5d5c5e403ba343d64921d3a79ebe97bdd
```

The final `book.log` SHA-256 digest is

```text
674647ecd0695ee7ddf019e3d23c972c45b8c4fecadeadec613994b104c07660
```

The final log contains no undefined reference, undefined citation,
multiply-defined-label, or rerun warning.

## Rendered-page inspection

The final PDF was rendered at 144 dpi and inspected at the following physical
pages:

- page 804 (printed page 736), including the corrected count of seventeen
  positive cases;
- page 904 (printed page 836), containing the new corollary statement;
- page 3184 (printed page 3116), containing the Chapter 72 seventeenth-case
  status entry.

No clipping, overlap, broken formula, unresolved cross-reference, or bad
transition was observed on these pages.
