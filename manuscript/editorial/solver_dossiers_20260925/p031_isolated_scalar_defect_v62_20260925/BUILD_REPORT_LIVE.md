# Build report

Date: 25 September 2026.

- Scoped Mingchen-writing audit of `STATEMENT_LIVE.tex` and
  `PROOF_LIVE.tex`: zero errors and zero warnings.
- Minimal packet: 2 pages, 101,960 bytes, with no LaTeX error, unresolved
  reference, rerun request, or horizontal or vertical overflow.
- Reference checker: 413 files in the build closure, 11,861 unique labels,
  and zero missing inputs, duplicate labels, dangling references, or
  structural errors.
- Reference-checker unit tests: all 6 pass.
- Inventory checker: 42 active atoms in 12 Chapter 72 problem environments,
  with tier counts `(0,3,7,15,17)`.
- Full book: 4,088 pages, 19,457,895 bytes, SHA-256
  `829513bdac32cc938a513c16e1a6797b9768f60cf1167243e7dcb3e1692b32a6`.
- Full-book log: no LaTeX error, unresolved reference or citation, rerun
  request, or horizontal or vertical overflow.  The 13 inherited duplicate
  Chapter 70 destinations are unchanged.
- Visual audit: physical book pages 795--797 and 3773--3776 were inspected
  during integration; physical page 796 and both minimal-packet pages were
  rendered again after the last proof clarification.  No clipping,
  collision, broken line, or malformed display was found.

No model-verifier result is claimed for this packet.
