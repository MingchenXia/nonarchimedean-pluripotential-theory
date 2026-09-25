# Build report

Date: 25 September 2026.

- The scoped Mingchen-writing audit of `STATEMENT_LIVE.tex` and
  `PROOF_LIVE.tex` reports zero errors and one reviewed warning: BMPS26 is an
  arXiv preprint.  The bibliography now has the required compound-author
  label `BMPS`.
- The minimal packet compiles to five pages.  Its final log has no unresolved
  reference or citation, rerun request, horizontal overflow or vertical
  overflow.
- The reference checker covers 403 build-closure files and 11,845 unique
  labels, with no missing input, duplicate label, dangling reference or
  structural error.  Its six unit tests pass.
- The inventory checker passes with 42 active atoms in 12 Chapter 72 problem
  environments and tiers `(0,3,7,15,17)`.
- The final full build produces `book.pdf` with 4,078 pages and 19,413,171
  bytes, SHA-256
  `c4995111acb2f92c645f296816179de5ac103fce925272c64454e6f09ad67bd6`.
- The final book log has no unresolved reference or citation, rerun request,
  horizontal overflow or vertical overflow.  The 13 inherited duplicate
  Chapter 70 equation destinations are unchanged.
- Physical PDF pages 3793--3798, 4054--4055 and 4076 were rendered and
  visually inspected.  They cover the convention repair, theorem, three
  proofs, scope boundary, provenance record and bibliography entry.  No
  clipping, collision or broken line was found.

The author PDF was independently rendered and all three pages were visually
inspected before adaptation.  The original remains byte-identical to the
supplied file.
