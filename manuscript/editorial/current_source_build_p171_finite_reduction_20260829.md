# Current-source whole-book build after the P17.1 finite reduction — 29 August 2026

This record concerns the current working source after the finite-level
closed-immersion reduction for P17.1 was independently audited,
production-verified, and integrated into Chapter 72 and Appendix L.  It
supersedes earlier current-source build records for release decisions about
this source state while preserving them as dated evidence.

- Result: forced clean, converged whole-book build.
- Command: `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error
  book.tex` from `manuscript/`.
- PDF: `manuscript/book.pdf`, 3,284 pages, 15,777,763 bytes.
- PDF SHA-256:
  `9f302df535bb1d92e58c8f7ef731866c3797e10eb3c4169d5509f6a3b41a8867`.
- Log: `manuscript/book.log`.
- Log SHA-256:
  `cde80c6e0a9dd91f167cd965ae3e8ddee97a5e29da28528b390dfc6e70a9d6c7`.
- Final-log audit: zero TeX or package errors, undefined control sequences,
  fatal or emergency stops, undefined references or citations, changed-label
  or rerun requests, duplicate labels or destinations, and overfull
  horizontal or vertical boxes.
- The log has 992 underfull-box notices from the established long-table and
  monograph layout.  The only class warning is the historical local-path
  identity warning for `style/svmono`.
- The PDF title is `Non-Archimedean Pluripotential Theory`; its author
  metadata is empty.
- `git diff --check`: passed before this record was written.

## Exact integration

The live statement and proof have SHA-256
`9be78feb5c4b76ae9f8ec7ec05d26dbaffebab602993dec7b37dcc8668819f81`
and
`ebb4c34fc1d06909ff2dfc7c0c0d918d1d548222b092e1b5e0472d2eecc4b603`.
The final `book.fls` records both exact paths and no quarantined variant.
Production Rethlas item `pi_9d4f5f4d6c4a36b32834c0a5`, using
`gpt-5.6-sol` at `xhigh`, returned final `correct`, zero critical errors,
and zero gaps, with the exact proof digest.  An independent exact-byte audit
and a standalone two-pass compile also passed.

The result removes the apparent need to generalize a resultant construction
from closed immersions to arbitrary basepoint-free systems at finite level.
It does not prove the continuity of the resulting relative Chow/Deligne
weights; P17.1 remains open precisely at that residual bridge.  The active
inventory remains 15 formal problem environments and 54 atoms, with tier
counts `(0,6,14,17,17)`.

## Visual inspection

The final PDF was rendered with Poppler at 144 dpi and inspected as page
images.

- Physical pages 3,099--3,104 cleanly render the Chapter 72 transition,
  complete statement, equations (72.35)--(72.38), full proof, exact
  verification record, scope firewall, and neighbouring problem.
- Physical pages 3,258--3,260 cleanly render the corresponding Appendix L
  provenance record and its neighbouring entries.

No inspected page has clipping, overlap, malformed display, missing glyph,
unreadable text, or margin intrusion.  Headers, footers, page numbers,
hyperlinks, and section hierarchy are consistent.

This is build and integration evidence; it makes no novelty or priority
claim.
