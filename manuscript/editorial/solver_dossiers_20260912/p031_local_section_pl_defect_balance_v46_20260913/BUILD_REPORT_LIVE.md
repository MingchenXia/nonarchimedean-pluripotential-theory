# Live build report

Date: 19 September 2026

## Integrated files

- `STATEMENT_LIVE.tex`
  - SHA-256:
    `e34449548777e03cd016818b7bc1ac768d85244b5fc55f066df9bdb67d45a4cb`
- `PROOF_LIVE.tex`
  - SHA-256:
    `e12263388566e69c1c45e76d3c75ccf5de999c7cd436062cd31fa6ca60030e7b`

The two live files are included from Chapter 15.  Matching scope summaries
were added to Chapter 72 and the atomic open-problem inventory.  The original
research `STATEMENT.tex` and `PROOF.tex` remain quarantined and are not in the
book build closure.

## Final checks

- Strict Mingchen TeX audit of the live statement and proof: 0 errors and 0
  warnings.
- Reference checker: 327 files in the build closure, 11,150 labels, 0
  multiply defined labels, 0 dangling references, and all per-file structure
  checks clean.
- Open-problem inventory checker: PASS; 46 active atoms in 14 Chapter 72
  problem environments, with tiers T1=0, T2=5, T3=8, T4=16, T5=17.
- `git diff --check`: clean.
- Full book build: PASS with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error book.tex`.
- Final PDF: 3,289 pages, 17,482,828 bytes.
- Final PDF SHA-256:
  `fd1e167336594f4ec5372796d79caf8cf1fdef140a7f06214a2b61d41deef3b0`.
- Final log scan: no undefined citations, no undefined references, and no
  multiply defined labels.

## Visual audit

Rendered Chapter 15 printed pages 686--689 (physical PDF pages 754--757) and
Chapter 72 printed page 2995 (physical PDF page 3063) were inspected after the
automatic second-pass repair.  The definitions, theorems, corollaries,
proofs, transition paragraphs, displayed equations, and cross-references are
legible and remain inside the text block.  No clipping, overlap, orphaned
result heading, or new local overfull box was observed.

The final full build is the build used for this visual audit.
