# Live build report

Date: 19 September 2026

## Integrated files

- `STATEMENT.tex`
  - SHA-256:
    `21c36f85677e4350d83d6077e93c70b0f56a1aa3f6755686e04963541ab335fe`
- `PROOF.tex`
  - SHA-256:
    `c86066298ff2191824e856a1691da13591642c03b4c0b31aa81fbd5ac520e58c`

The two files are included from Chapter 15.  Matching scope summaries were
added to Chapter 72 and the atomic open-problem inventory.

## Final checks

- Strict Mingchen TeX audit: 0 errors.  Its sole warning is that
  `GR25Classical` is still represented by the pinned arXiv v2 entry; the
  versioned primary-source PDF and hash are recorded in `SOURCES_LIVE.md`.
- Reference checker: 321 files in the build closure, 11,110 labels, 0
  multiply defined labels, 0 dangling references, and all per-file structure
  checks clean.
- Open-problem inventory checker: PASS; 46 active atoms in 14 Chapter 72
  problem environments, with tiers T1=0, T2=5, T3=8, T4=16, T5=17.
- `git diff --check`: clean.
- Full book build: PASS with `latexmk -pdf -interaction=nonstopmode
  -halt-on-error book.tex`.
- Final PDF: 3,281 pages, 17,446,439 bytes.
- Final PDF SHA-256:
  `09f724f338abc70e8c3e5c9e76eee4ebe57b0501b755e4b758d52b072cccb5dc`.
- Final log scan: no undefined citations, no undefined references, and no
  multiply defined labels.

## Visual audit

Rendered Chapter 15 book pages 678--681 and Chapter 72 page 2987 were
inspected after the full build.  The new definition, two theorems,
counterexample proposition, three proofs, transition paragraphs, displayed
equations, and cross-references are legible and remain inside the text block.
No clipping, overlap, orphaned proof heading, or new local overfull box was
observed.

The automatic second pass made no further TeX change, so the final
up-to-date build and visual state coincide with the audited pages.
