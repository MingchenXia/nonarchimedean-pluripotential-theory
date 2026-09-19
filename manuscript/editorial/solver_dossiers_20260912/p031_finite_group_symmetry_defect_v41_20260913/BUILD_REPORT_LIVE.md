# Live build report

Date: 19 September 2026

## Integrated files

- `STATEMENT_LIVE.tex`
  - SHA-256:
    `c1ee6f5a4fbc7597f3fbd849d6f24f526af8f4279a4455ac060d502bdce415e4`
- `PROOF_LIVE.tex`
  - SHA-256:
    `7bf3e088c19885237b36aef78c65583b600cc023befc10bab80770233651a21c`

The two live files are included from Chapter 15.  Matching scope summaries
were added to Chapter 72 and the atomic open-problem inventory.  The original
research `STATEMENT.tex` and `PROOF.tex` remain quarantined and are not in the
book build closure.

## Final checks

- Strict Mingchen TeX audit: 0 errors and 0 warnings.
- Reference checker: 323 files in the build closure, 11,124 labels, 0
  multiply defined labels, 0 dangling references, and all per-file structure
  checks clean.
- Open-problem inventory checker: PASS; 46 active atoms in 14 Chapter 72
  problem environments, with tiers T1=0, T2=5, T3=8, T4=16, T5=17.
- `git diff --check`: clean.
- Full book build: PASS with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error book.tex`.
- Final PDF: 3,283 pages, 17,459,091 bytes.
- Final PDF SHA-256:
  `807cc67e9a109bf6675856c6ddf47e7e4a4a2e54358543178edfd03b541c2463`.
- Final log scan: no undefined citations, no undefined references, and no
  multiply defined labels.

## Visual audit

Rendered Chapter 15 pages 681--683 and Chapter 72 page 2989 were inspected
after the full build.  The new definition, two theorems, two proofs,
transition paragraphs, displayed equations, and cross-references are legible
and remain inside the text block.  No clipping, overlap, orphaned proof
heading, or new local overfull box was observed.

The automatic second pass made no further TeX change, so the final
up-to-date build and visual state coincide with the audited pages.
