# Live build report

Date: 19 September 2026

## Integrated files

- `STATEMENT_LIVE.tex`
  - SHA-256:
    `16c8fe4500185bbb98e7fc3b5bf818b134f4a480a44ab6c27b3aaa11274c6700`
- `PROOF_LIVE.tex`
  - SHA-256:
    `15c6063487911b58dda63a330da956d144d12bf2b09923c14d3ed27ec58ad625`

The two live files are included from Chapter 15.  Matching scope summaries
were added to Chapter 72 and the atomic open-problem inventory.  The original
research `STATEMENT.tex` and `PROOF.tex` remain quarantined and are not in the
book build closure.

## Final checks

- Strict Mingchen TeX audit: 0 errors and 0 warnings.
- Reference checker: 325 files in the build closure, 11,132 labels, 0
  multiply defined labels, 0 dangling references, and all per-file structure
  checks clean.
- Open-problem inventory checker: PASS; 46 active atoms in 14 Chapter 72
  problem environments, with tiers T1=0, T2=5, T3=8, T4=16, T5=17.
- `git diff --check`: clean.
- Full book build: PASS with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error book.tex`.
- Final PDF: 3,285 pages, 17,468,633 bytes.
- Final PDF SHA-256:
  `e75d6f477cdcf434afc0eab297990321d5b782bab691baeb4ee6e09cb627b02a`.
- Final log scan: no undefined citations, no undefined references, and no
  multiply defined labels.

## Visual audit

Rendered Chapter 15 pages 683--686 and Chapter 72 page 2991 were inspected
after the full build.  The definition, theorem, two corollaries, three
proofs, transition paragraphs, displayed equations, and cross-references are
legible and remain inside the text block.  No clipping, overlap, orphaned
proof heading, or new local overfull box was observed.

The automatic second pass made no further TeX change, so the final
up-to-date build and visual state coincide with the audited pages.
