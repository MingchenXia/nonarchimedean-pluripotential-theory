# P07.1 v16 build report

Date: 20 September 2026

Status: full-book integration passed.

## Result

- Corollary 16.2.2 appears on printed page 835, physical PDF page 903.
- It records that the verified Stone--exact-star--polyhedral sheaf identity,
  specialized to `P = R^d`, restricts to every Euclidean open set.
- Hence a locally constant Stone parameter, an arbitrary exact CLD infinite
  star, and an active open Euclidean factor may occur simultaneously.
- Chapter 72 records this as the sixteenth positive P07.1 case and removes
  the obsolete simultaneous-Stone exclusion.
- P07.1 remains open, and the inventory stays at 46 active atoms in 14
  problem environments with tier vector `(0,5,8,16,17)`.

## Verification and validation

- Final dependency-closed local `gpt-6-astra`/`xhigh` verification:
  `correct`, zero critical errors, zero gaps, checked item
  `pi_145beff1ee11983825be4ef2`.
- Strict Mingchen audit on the exact statement and proof: zero errors and
  zero warnings.
- Required second pass repaired the Chapter 16 overview count from fifteen
  to sixteen positive cases.
- Reference audit: 371 files in the build closure, 11,383 labels, no
  multiply defined label, no dangling reference, and no per-file structural
  error.
- Inventory audit: `PASS_OPEN_PROBLEM_INVENTORY`.
- `git diff --check`: passed.
- Full-book `latexmk` build: passed and converged, with no unresolved
  reference or citation and no multiply defined label in the final log.
- Final PDF: 3,361 pages and 17,793,503 bytes.
- Final PDF SHA-256:
  `18df46c92c27b48878f389a22e4d797d53827c31bce86f719afd5153fded4b53`.
- Final log SHA-256:
  `61c9c6fa013b5fa573ef49d56a6104914ad66cb592769bc40a6b1efee8f9bd32`.

## Visual inspection

Rendered physical pages 802--804, 898--905, 908--910, and 3181--3184 were
inspected from the final PDF.  These cover the Chapter 16 overview, the new
corollary and proof, the surrounding scope remark, and the Chapter 72 status
update.  The corrected count was re-rendered on physical page 804.  No
clipping, overlap, malformed formula, broken reference, bad page transition,
or new layout defect was found.
