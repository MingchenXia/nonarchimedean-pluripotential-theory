# Build report

Date: 20 September 2026

Status: final live integration, full-book build, and visual inspection passed.

## Final live integration

- Base commit before integration:
  `bdb805a09eeb9f14d9c525bb5c7c5813378a8c79`.
- Final principal statement/proof SHA-256:
  `8b9c6605c4016b4c69e489e5165d214360a8d5d3a34bf08b8f96419acde97e15` /
  `452530d86fbc979d2e6f95e2c8a489a24fa87a2ba466477933455cd68cea3d94`.
- Strict Mingchen writing audit: 0 errors and 0 warnings.
- Open-problem inventory: 46 active atoms in 14 formal problem
  environments; tier vector `(0,5,8,16,17)`.
- Reference check: 369 files in the build closure, 11,381 labels, zero
  multiply defined labels, and zero dangling references.
- `git diff --check`: passed.
- Full-book `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`:
  passed and converged.
- Final full-book PDF: 3,359 physical pages and 17,787,919 bytes.
- Final full-book PDF SHA-256:
  `eaa5fd4b41b4b846c09c5bd661148ba57d65d0ac1a349c14d261c916b9c4d3c4`.
- Final full-book log SHA-256:
  `a9f9465b1a5f96ecaa8654a7e4cae1732b4002fb99c1de951378aea9a3f8bcac`.
- The new result is Theorem 16.2.13 on printed page 808 (physical PDF page
  876).  Its statement and proof occupy physical pages 876--884.
- The hierarchy ledger on physical page 803, the scope ledger on physical
  page 908, and the Chapter 72 status text on physical pages 3179--3180 were
  rendered and inspected together with all theorem/proof pages.  No clipping,
  collision, malformed formula, or illegible text was found.

The remaining bad-box warnings in the final log are pre-existing and are not
attached to the new candidate inputs or their inserted ledger paragraphs.

## Historical minimal theorem build (2026-09-13 bytes)

- Engine: pdfLaTeX through latexmk.
- Scope: exact `STATEMENT.tex` and `PROOF.tex`, with the two dependency
  labels supplied by the harness.
- Final PDF: 9 pages and 213224 bytes.
- Final PDF SHA-256:
  `71b0c1e07ae59c971f81a86881aaed74944eb95e21b4715096c14055b4275a89`.
- Final log SHA-256:
  `4643f74d9f048acafd7b03546d3557dd275b3ab3d49d4c292f837d7729d48c55`.
- The final log contains no warning, undefined reference, overfull box,
  underfull box, or LaTeX error.
- Strict Mingchen writing audit: 0 errors and 0 warnings.
- All nine pages were rendered and visually inspected without clipping,
  collisions, or illegible mathematics.

## Historical isolated full-book integration rehearsal

- Base commit:
  `94531c9a03ade9f6a2e2e3e7e523ecac8cfe2eab`.
- Scope: the candidate inputs, the Chapter 16 thirteen-case ledger, and the
  corresponding Chapter 72 and atomic-inventory P07.1 scope updates.
- `git diff --check`: passed.
- Open-problem inventory: 48 active atoms; tier vector `(0,5,9,17,17)`.
- Full-book `latexmk` run: passed and converged, with no fatal TeX error,
  undefined control sequence, unresolved citation or reference, or multiply
  defined label in the final log.
- Final full-book PDF: 3668 physical pages and 17,435,401 bytes.
- Final full-book PDF SHA-256:
  `32d047de3ad888a8de03972266ea70d7f9a50300cf27f2e1d236f5ca31c76bc6`.
- Final full-book log SHA-256:
  `a9af7fe0580674bb97fb7df06612496c70dd3d3988b56c6bb6c06679c6faa0b8`.
- The new result resolved as Theorem 16.2.13 on printed page 745.
- The candidate theorem and proof on physical PDF pages 813--820, the
  surrounding scope ledger on physical page 826, and the Chapter 72 insertion
  on physical page 3457 were rendered and inspected after the final locality
  and endpoint error-ledger repairs.  No clipping, collision, malformed
  formula, or new bad box was found.

The complete rehearsal ledger and the separation from unrelated live-tree
work are recorded in `INTEGRATION_REHEARSAL.md`.
