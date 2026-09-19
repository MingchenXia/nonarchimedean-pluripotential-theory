# Build and verification report

Date: 20 September 2026

## Result

- Full `latexmk` build: passed.
- Final PDF: 3,345 pages, 17,718,906 bytes.
- Mingchen TeX audit of statement, proof, and materialized dependencies:
  0 errors, 0 warnings.
- Full build-closure reference check: 361 files, 11,344 labels,
  0 multiply defined labels, 0 dangling references.
- Open-problem inventory check: 46 active atoms across 14 Chapter 72
  environments; tier counts `T1=0`, `T2=5`, `T3=8`, `T4=16`, `T5=17`.
- Final gpt-6-astra/xhigh verification: `correct`, 0 critical errors, 0 gaps.
- Final log scan: no undefined references, undefined citations, or rerun request.
  The new Chapter 18 source interval emits no overfull box warning.
- Visual inspection: physical PDF pages 1313--1316 (printed pages 1245--1248)
  after the final build; theorem, formulas, proof headings, page breaks, and
  margins are clean.  The Chapter 72 status paragraph was also inspected in
  the preceding final-content build.

## SHA-256 ledger

- `STATEMENT_LIVE.tex`:
  `1a69d3538cb2294f087bbcb55ca74f8d89b873016ec9cddb12f34b145b0db753`
- `PROOF_LIVE.tex`:
  `d5ca1f381c3b5ca4de2d9582adb199e37d9069611dfa1d73c42da7ffd3da55dc`
- `DEPENDENCIES_STATEMENT.tex`:
  `9a79a94da2205e63885802399b8e7697596252448928abd21ef29c71db7c8c4e`
- `manuscript/parts/part2/ch18_delta_forms.tex`:
  `c5d39ea1525cde802de08280dd62eef2f6d8b13054744694b2a9703c8926a074`
- `manuscript/parts/part6/ch72_major_open_problems.tex`:
  `066258973d6f79ee677bf8afcfa64b66835d31458ebc16bc4d36a8825c645f43`
- `manuscript/editorial/open_problem_atomic_inventory_20260824.md`:
  `cfae61b1f500445ac429cc9351c439ce2fb7c7921216baa28e1d4113e0baa688`
- `manuscript/book.pdf`:
  `8e320ef5807c5d846e2ccc6748533948db96ed1a9379e4511ca19ef053096dc1`
- `manuscript/book.log`:
  `1504ab45a0744c9345a1aa9af9b3e7b854887143ec3d717366bbf5091b42dd23`
- Initial verifier request / response / headers:
  `83ab3530ec86ca90e374c8285c285e4d3dddfc8966fb113125d0e43eb6891937`,
  `f7d6585dd0cae336c3069744972572129653a5395dbb93f029aa0882c59c9a29`,
  `731ef1ae8503fdf18465aa796d93e7b876f305c0762b58dd276b5a3403036412`.
- Repaired verifier request / response / headers:
  `69afefe451944a6fec93db2ee700fb28e0e44c08a8a54c6923d49505e0fd22ce`,
  `eaaa20483e92f3229a70171458e2829eeca2323c44d9572279d8efb3243e737a`,
  `47913b08e5e575c7b614dc34f012e8b77774ddc28f3a9f31bc16500fbc906788`.
- Final polished verifier request / response / headers:
  `ed3656aa76aa05e498ff455ceb11fee8d20aa9431fa60b4b13dd0fe4b342fe1a`,
  `fcd30ccb3093a6c456f91d6d62db78324cca164139646c4c3b6d17edcafaf9fd`,
  `42a021c168cfc867b9750fd4a44e21b9fc48e2242bdbd86520327c5dede3294c`.
