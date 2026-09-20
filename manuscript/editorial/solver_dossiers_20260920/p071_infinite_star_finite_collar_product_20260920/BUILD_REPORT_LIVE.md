# P07.1 exact infinite-star × finite-collar product: live build report

Date: 2026-09-20

## Mathematical and editorial checks

- Final repaired dependency-closed verifier result: `correct`, with `0`
  critical errors and `0` gaps.
- Checked item: `pi_dab08cd0ade65f20ea9867b4`.
- Strict Mingchen-writing audit on the principal statement and proof: `0`
  errors and `0` warnings.
- Principal statement SHA-256:
  `55480e4cfcb6f0aff57af1644b3b7d7974cbeb2b25054bbc8579569879eede9c`.
- Principal proof SHA-256:
  `004b9441221acb56c5dba3c098d9fcb8140eadb7c6f5925b36e55608921aa0cd`.
- The two rejected requests and their exact responses remain archived; the
  repair history is summarized in `REPAIR_LEDGER_LIVE.md`.

## Structural checks

- Open-problem inventory audit:
  `PASS_OPEN_PROBLEM_INVENTORY`; `46` active atoms across `14` Chapter 72
  environments, with tiers `T1=0`, `T2=5`, `T3=8`, `T4=16`, `T5=17`.
- Build-closure reference audit: `377` files, `11404` labels, `0` multiply
  defined labels, `0` dangling references, and all per-file structures clean.
- `git diff --check`: clean.

## Full-book build and visual inspection

- Full `latexmk` PDF build completed successfully with no fatal errors.
- Output: `book.pdf`, `3373` pages, `17840530` bytes, PDF version `1.5`.
- The build-log block for the new statement and proof contains no overfull
  box warning.
- Rendered and visually inspected PDF pages `884` and `885` (printed pages
  `816` and `817`), containing the integration paragraph, Theorem 16.2.14,
  and the beginning of its proof.
- Rendered and visually inspected PDF page `3190` (printed page `3122`),
  containing the new Chapter 72 scope and verification record.
- All inspected pages have legible mathematics and citations, with no
  clipping, overlap, or margin overflow in the new material.
