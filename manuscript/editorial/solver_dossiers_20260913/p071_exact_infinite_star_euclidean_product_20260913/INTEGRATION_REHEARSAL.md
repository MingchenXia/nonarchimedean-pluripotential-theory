# P07.1 exact infinite-star--Euclidean integration rehearsal

Date: 2026-09-20 (Asia/Shanghai)

Status: historical isolated rehearsal passed; final live integration and
model-backed verification passed on 2026-09-20.

## Final live result

The house-style final statement/proof hashes are
`8b9c6605c4016b4c69e489e5165d214360a8d5d3a34bf08b8f96419acde97e15` /
`452530d86fbc979d2e6f95e2c8a489a24fa87a2ba466477933455cd68cea3d94`.
Dependency-closed `gpt-6-astra` verification at `xhigh` returned final
`correct`, zero critical errors, and zero gaps.  Live integration against
base commit `bdb805a09eeb9f14d9c525bb5c7c5813378a8c79` passed the inventory,
reference, writing, and whitespace checks.  The full book converged at 3,359
physical pages with PDF SHA-256
`eaa5fd4b41b4b846c09c5bd661148ba57d65d0ac1a349c14d261c916b9c4d3c4`.
All affected pages were rendered and visually inspected without defect.

## Frozen candidate bytes used in the rehearsal

- `STATEMENT.tex` SHA-256:
  `f7ef3beac8e0b79651c5572f976acaff9551300311c2e402d55b51489145b044`
- `PROOF.tex` SHA-256:
  `e123fc870cb30085eb64d4b6d34cdef7d61d8c8309c78409ddfbbe1eef3a68b6`

The files copied into the isolated tree were rehashed after the build and
matched these live-dossier bytes exactly.

## Rehearsed integration

The rehearsal started from commit
`94531c9a03ade9f6a2e2e3e7e523ecac8cfe2eab` in a no-hardlink clone.  It
included the statement and proof after Theorem 16.2.12, extended the Chapter
16 positive-case ledger from twelve to thirteen cases, and inserted the
corresponding P07.1 scope update in Chapter 72 and the atomic inventory.  The
inventory continued to report 48 active atoms with tier vector
`(0,5,9,17,17)`.

The rehearsal deliberately did not alter the live Chapter 16 or Chapter 72
files.  The live Chapter 72 and inventory files contain unrelated user work,
so eventual integration must apply only the rehearsed P07.1 hunks.

## Checks

- `git diff --check`: passed.
- Strict audit of `STATEMENT.tex` and `PROOF.tex`: 0 errors, 0 warnings.
- Full-book `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`:
  passed and converged.
- Full-book output: 3668 physical pages, 17,435,401 bytes.
- Full-book PDF SHA-256:
  `32d047de3ad888a8de03972266ea70d7f9a50300cf27f2e1d236f5ca31c76bc6`.
- Final full-book log SHA-256:
  `a9af7fe0580674bb97fb7df06612496c70dd3d3988b56c6bb6c06679c6faa0b8`.
- No fatal TeX error, undefined control sequence, undefined citation or
  reference, or multiply defined label was present in the final log.
- The new theorem resolved as Theorem 16.2.13 on printed page 745
  (physical PDF page 813).
- The candidate theorem and proof occupy physical pages 813--820; the
  surrounding scope ledger was inspected on physical page 826, and the
  Chapter 72 insertion was inspected on physical page 3457.
- Visual inspection found no clipping, collision, malformed formula, or new
  bad box in the candidate or its ledger insertions.  The final rendered pass
  includes the explicit ledger for newly exceptional branches under
  restriction and the repaired finite-sampling error budget at both the node
  and every full endpoint.  It also includes the explicit fixed Euclidean core
  and the sequential-Dini argument making terminal continuity uniform in all
  sufficiently negative branch parameters.

The final log still contains pre-existing bad-box warnings elsewhere in the
book, including the long-hash ledger line in Chapter 72; none is attached to
the new candidate inputs or their inserted text.

## Closed gate

The dependency-closed P07.1 packet was submitted under the user's explicit
authorization.  The final response, transport hashes, checked item, and
digests are frozen in `VERIFICATION_RECEIPT.md`.  All staged-verification
wording has been replaced, and the live-tree audits and full-book build have
been repeated successfully.
