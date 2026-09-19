# P03.1 v59 live build report

Date: 2026-09-20

## Integration

The continuous-section theorem, the canonical scalar-section corollary, and
the terminal-carrier application are integrated in Chapter 15.  Chapter 72
and the atomic inventory record the new canonical-lift range and its exact
firewall.  The Poineau source is recorded in the live bibliography.  P03.1
remains active; the inventory remains at 46 active atomic questions in 14
formal problem environments.

## Exact hashes

- `STATEMENT_LIVE.tex`:
  `2e3009274c0a8fcc1a8935c4b1aaf0cb87d1b8479364ec08447bb8ec9d2708d1`
- `PROOF_LIVE.tex`:
  `707f5624ff74d430feae867f391e017620054defc3b6d22e02c40665fb2f3a8a`
- `book.pdf`:
  `fd09152f362563f698f7fac0ce0e6b22633eaa2f2d48f743f4ccfec8d12872a3`

## Source checks

- The official arXiv final-version PDF of Poineau's paper was inspected at
  Definition 3.2, Corollary 3.7, Remark 3.13, and Corollary 3.14; its SHA-256
  is recorded in `SOURCES_LIVE.md`.
- The published metadata was checked independently against the Crossref DOI
  record `10.24033/bsmf.2648`.
- The live theorem imports only the existence and continuity of the canonical
  section.  No Shilov-boundary, analyticity, or psh-preservation assertion was
  imported.

## Mechanical checks

- Forced full-book `latexmk` build and post-second-pass rebuild: PASS.
- Output: 3325 pages, 17,640,414 bytes, PDF 1.5.
- Build-closure reference audit: 349 files, 11,310 labels, zero multiply
  defined labels, zero dangling references, and clean per-file structure.
- Open-problem inventory audit: PASS; tiers
  T1=0, T2=5, T3=8, T4=16, T5=17.
- Final log scan: no undefined citation, undefined reference,
  multiply-defined-label, label-change, or rerun warning.
- Strict `mingchen-writing` audit on the exact new statement and proof: zero
  errors and zero warnings before and after the second pass.
- `git diff --check`: PASS.

## Automatic second pass and visual review

The second pass replaced an ambiguous reference to the ``section of every
root point'' by the exact section image of every base point and normalized
the Chapter 72 cross-reference.  The final PDF was inspected on physical
pages 788--791 (printed pages 720--723) and physical page 3099 (printed page
3031).  The statement, citation, formulas, proofs, Chapter 15 synthesis, and
Chapter 72 status paragraph are complete and visually clean.  The two changed
pages were re-rendered after the second pass.

No model-backed verifier was used for this version.
