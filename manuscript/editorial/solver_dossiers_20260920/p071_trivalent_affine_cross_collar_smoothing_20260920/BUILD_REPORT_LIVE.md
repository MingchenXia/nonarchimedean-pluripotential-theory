# Build report

Date: 20 September 2026

## Result and verification

- Result: affine cross-collar smoothing on a trivalent two-star product.
- Scope: arbitrary finite convex polyhedral mixed coupling is allowed away
  from the two node axes, provided one ambient affine germ is already fixed
  on a cross-collar.  The collar hypothesis is not derived, so P07.1 remains
  active.
- Local verifier: `gpt-6-astra` at `xhigh`.
- Final verdict: `correct`; zero critical errors and zero gaps.
- Checked item: `pi_725a917f37c426b97fa2db13`.
- Principal statement SHA-256:
  `2e538f70b29d2ce359902f5ff16931d750112dc4e6a81903075c08e604b1296e`.
- Principal proof SHA-256:
  `396d2be290d6262c68468c0b1e0490bf919ec3e504f4c79edd7797d29593f922`.
- Strict exact-current receipt audit against the independently inspected
  verifier source: `PASS`.

## Editorial and structural checks

- The automatic second reading found no mathematical defect.
- The first full-book visual pass exposed one mistyped inequality command
  and one duplicated cross-reference word.  Both were repaired, and the
  corrected exact proof was resubmitted before integration was finalized.
- Strict Mingchen-writing audit of the final statement and proof: zero
  errors and zero warnings.
- Full build-closure reference check: 389 files, 11,470 labels, zero
  multiply defined labels, zero dangling references, and all per-file
  structures clean.
- Open-problem inventory: `PASS_OPEN_PROBLEM_INVENTORY`; 46 active atoms in
  14 formal problem environments, with tier counts
  `T1=0`, `T2=5`, `T3=8`, `T4=16`, `T5=17`.
- Final log scan: no undefined citation, undefined reference,
  multiply-defined-label, or unresolved rerun diagnostic.
- `git diff --check`: `PASS`.

## Full-book build and visual inspection

- Full `latexmk` build: passed.
- Final PDF: 3,393 pages and 17,938,551 bytes.
- Final PDF SHA-256:
  `7c6ed3fe9fda0e0215cd53f874984e0971f81c5187c72b5c344b413109177241`.
- Final log SHA-256:
  `7e69d2f182678ce63b4a7349c18c5611f8bd5d33cc2e5dfc41b9b4b16167023a`.
- The Chapter 16 insertion was inspected on physical PDF pages 904--908
  (printed pages 836--840), including the transition into the next result.
- The Chapter 72 ledger was inspected on physical pages 3211--3213
  (printed pages 3143--3145).
- The Appendix L provenance record was inspected on physical pages
  3362--3364 (printed pages 3294--3296).
- After the two typographic repairs, physical pages 905, 908, 3212, and
  3363 were rendered again and rechecked from the final PDF.
