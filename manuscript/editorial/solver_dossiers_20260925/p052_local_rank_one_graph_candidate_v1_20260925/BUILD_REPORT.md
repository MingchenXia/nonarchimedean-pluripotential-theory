# Build report

Date: 25 September 2026.

- The scoped Mingchen-writing audit of `STATEMENT.tex` and `PROOF.tex`
  reports zero errors and one reviewed warning: BMPS26 is currently cited as
  an arXiv preprint.
- The minimal dependency-closed packet compiles cleanly to seven pages.  Its
  final log has no unresolved reference or citation, rerun request,
  horizontal overflow or vertical overflow.
- The final source-graph check covers 405 build-closure files and 11,847
  unique labels, with no missing input, duplicate label, dangling reference
  or structural error.  Its six unit tests pass.
- The inventory checker passes with 42 active atoms in 12 Chapter 72 problem
  environments and tiers `(0,3,7,15,17)`.
- The full build produces `book.pdf` with 4,080 pages and 19,422,086 bytes,
  SHA-256
  `08bf262b09f23b26c5b85f7414fcb222592fb295c7b6feb83e1fc1adeb46b79c`.
- The final book log has no unresolved reference or citation, rerun request,
  horizontal overflow or vertical overflow.  The 13 inherited duplicate
  Chapter 70 destinations are unchanged.
- Physical PDF pages 3798--3800 were rendered and visually inspected.  They
  cover the new theorem, its graph-level contact proof, the
  bivalent/trivalent corollary and the exact remaining-scope paragraph.  No
  clipping, collision or broken line was found.

The full build, reference check, inventory check, unit tests, warning scan and
visual inspection were repeated after the final prose revision.
