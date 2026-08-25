# P06.2 real-PL zero-current converse: repaired exact-live production receipt

Date: 25 August 2026 (Asia/Shanghai)

Status: exact current Chapter 18 statement and proof verified; this receipt
supersedes the earlier live-integration control record without deleting its
history.

## Controlling verdict

- Run: `20260825T061351Z_655e7f503e5d`.
- Item: `pi_eea98ea0a54108cae4e076be`.
- Model / scrutiny: `gpt-5.6-sol` / `xhigh`.
- Verification status / verdict: `final/correct`.
- Critical errors / gaps: `0/0`.
- Statement SHA-256:
  `655e7f503e5db0cee8e0c94fdc765b6923aeebb7b89c7b5b98ad7827fa6e2421`.
- Proof SHA-256:
  `7ad130bab1d9dd61ecbac818005c4b80fe405c3d9710a6bb588fea6fa30a856a`.
- Request SHA-256:
  `29704a697a6f17c1a6bf15a578a028126e322059a08353d1acc76cd6921ebef7`.
- Aggregate context digest:
  `4f8f605440ff8a55d3d65a3f9d698c1aa78679d4ec805c557b9f4a04e54ee436`.
- Item context digest:
  `789b04d308266ae6d531080a2cd0ded8b0160a3528ab036d0963382ae0bf67c2`.

The statement and proof decoded from the request and compared byte for byte
with the current live proposition and proof in Chapter 18.  All four `cmp`
checks returned zero.

## Verified scope

Let `K` be complete and nontrivially valued, and let `X` be a good,
separated, boundaryless, strict analytic space that is pure of positive
dimension.  If a real-PL function `h` has zero CLD
`d'd''`-current, then `h` is GJR harmonic, all residual classes `L_h(x)` are
numerically trivial, and `h` is classically pluriharmonic.  The proof uses
rational calibrated coefficients on source-side skeletal cells and
`Q`-linear independence.  It does not cover arbitrary continuous functions.

## Repairs controlled by this run

The exact-live proof first obtains the simultaneous smooth tropicalization
G-locally at the chosen point and only then chooses a compact strict affinoid
inside its domain.  One fixed chart is therefore defined on the neighbourhood
where all arbitrary compactly supported tests are localized.  CLD
Proposition 14.3.1 and Section 14.3.2 give rational, not asserted integral,
calibrated coefficients; rationality is sufficient for the coefficient
separation.  A compact patch inside a source-side codimension-one cell is
isolated by a smooth cutoff from CLD Corollary 6.2.4.  CLD Corollary 6.2.8
and Lemma 7.2.5 supply the compact-support localized test decomposition.
Finally, GR Theorem 4.3 is cited directly for the classical-psh comparison.

## Preserved non-controlling history

- Run `20260825T032958Z_3a27f19be958` was a valid production check of its
  frozen skeletal packet, but it no longer controls the adapted live proof.
  A later live audit required the common-domain, rational-calibration,
  source-side-cutoff, and localized-test refinements above.
- Run `20260825T054033Z_655e7f503e5d` was stopped before an item or aggregate
  verdict existed.  It is an aborted, non-controlling run.
- Run `20260825T055921Z_655e7f503e5d`, item
  `pi_9699db6066f137872b49e98d`, returned `final/wrong`, with zero critical
  errors and two gaps: the affinoid had been chosen before the G-local common
  chart, and the final comparison used an internal cross-reference absent
  from the exact packet.  The full rejection artifacts are preserved under
  `p06_real_pl_zero_current_live_scope_arithmetic_v2_rejection_run_20260825/`.
- The v3 files were never submitted.  They are a pre-final snapshot; v4
  corrects the locator for CLD 14.3.2, which is a sectioned construction and
  not a proposition.
- The earlier target-side boundary-separator rejection
  `20260825T031243Z_1603e0a83037` remains quarantined and is not used.

## Preserved controlling artifacts

The raw run directory
`p06_real_pl_zero_current_live_scope_arithmetic_v4_run_20260825/` contains
the aggregate manifest and verification, item log and verification, and both
completed process guards.  Their SHA-256 values are, respectively,
`2579ddd4...`, `8fa2cfdf...`, `ecd35a65...`, `684c1714...`,
`30ff0055...`, and `9bf052d1...`.

The combined six-page minimal compile succeeded.  Its PDF SHA-256 is
`3a3c81b3395be8f423bb41d0e1f94335d6e7b160fda68744d6ae6f9da48f13b7`;
its log SHA-256 is
`26920c536e0bdbb3bb485954bf7ca6182125295f2f1f94ac1970ce3fd8303167`.

No novelty or priority claim is made.
