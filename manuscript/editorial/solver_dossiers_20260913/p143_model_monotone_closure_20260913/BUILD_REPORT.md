# P14.3 final build report

Date: 2026-09-19

## Frozen packet

- Strict Mingchen audit: 0 errors, 0 warnings.
- Minimal compile: successful, 2 pages, 184407 bytes.
- Minimal PDF SHA-256:
  `e161ce1aa9ef384e7f8368a11671e5ba163dfc3b35c405f72a13b8f9d83a9381`.

## Integrated monograph

- Command: `latexmk -g -pdf -interaction=nonstopmode -halt-on-error book.tex`.
- Result: successful after three convergence passes from regenerated build
  metadata.
- Output: 3716 pages, 17750551 bytes.
- Book PDF SHA-256:
  `979480720c08855d40b392e20ea5a067cff99b1301452f2b93dc6747d92f8a40`.
- Undefined references: 0.
- Undefined citations: 0.
- Undefined control sequences or fatal errors: 0.
- Remaining overfull boxes: 7.  These are pre-existing equation/layout
  warnings outside the P14.3 theorem.  The 153.56 pt overflow caused by an
  unbreakable Chapter 72 source hash was repaired with invisible permitted
  breakpoints.

The P14.3 theorem and its proof were also inspected in the integrated PDF on
printed pages 3346--3347; the cross-page endpoint argument is legible and no
local layout defect was found.
