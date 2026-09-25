# Build report

Date: 25 September 2026.

- The scoped Mingchen-writing audit of `STATEMENT_LIVE.tex` and
  `PROOF_LIVE.tex` reports zero errors and one reviewed warning: BMPS26 is an
  arXiv preprint.  The bibliography now has the required compound-author
  label `BMPS`.
- The revised minimal packet compiles to four pages.  Its final log has no unresolved
  reference or citation, rerun request, horizontal overflow or vertical
  overflow.
- The reference checker covers 409 build-closure files and 11,854 unique
  labels, with no missing input, duplicate label, dangling reference or
  structural error.  Its six unit tests pass.
- The inventory checker passes with 42 active atoms in 12 Chapter 72 problem
  environments and tiers `(0,3,7,15,17)`.
- The final full build produces `book.pdf` with 4,084 pages and 19,443,419
  bytes, SHA-256
  `05c0b1e154fd57c570068a49e6cbb5a221193f6351019b8735eaddfd469c5407`.
- The final book log has no unresolved reference or citation, rerun request,
  horizontal overflow or vertical overflow.  The 13 inherited duplicate
  Chapter 70 equation destinations are unchanged.
- Physical PDF pages 3793, 3796, 3806, 3809, and 4061 were rendered and
  visually inspected.  They cover the convention repair, withdrawal
  transition, theorem, later affine and Bergman-fan corrections, and
  provenance record.  No clipping, collision, or broken line was found.

The original author PDF was independently rendered and all three pages were
visually inspected before adaptation.  It was later replaced by an explicit
withdrawal; the current source artifact and current-book build are audited in
the withdrawal/P05.1 integration record.
