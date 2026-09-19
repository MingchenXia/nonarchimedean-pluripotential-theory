# P06.2 smooth proper split-toric mixed towers v62: live build report

Date: 2026-09-20

## Integration

Chapter 18 now admits analytically locally trivial smooth proper split-toric
bundles as a fourth exact stage in every mixed-tower result driven by unique
zero-current descent, first-current rigidity, connected fibres, and local
sections.  This includes the tower over a published curve, the coordinated
annular-top and annular-bottom consequences, and the fully interleaved
coordinated-annular theorem.  The same formal extension is integrated into
the P21.3 endpoint and residual-Picard mixed-tower classifications.  Chapter
72 and the atomic inventory record the enlarged range and its unchanged
scope firewalls.  P06.2 and P21.3 remain active, and the inventory remains at
46 active atomic questions in 14 formal problem environments.

The dated September 19 and v61 build reports remain historical snapshots.
This report supersedes their temporary references to three exact stage types
or to a split-toric result isolated at one bundle level.

## Exact hashes

- `p062_mixed_exact_tower_transfer_20260919/STATEMENT.tex`:
  `957c30f3a69cfaf7bdb8a11b86cd994b365c10001a75949e426ca7375187f8f9`
- `p062_mixed_exact_tower_transfer_20260919/PROOF.tex`:
  `db3bb4fa39ded8cbef4e315524826cdf4a9639f099d1bd0426eb198317f8206c`
- `p062_mixed_towers_over_curves_20260919/STATEMENT.tex`:
  `2ee519b55bbd2ab69d39a4b95a47f9f8733877b655ed757735105c38a3be86f4`
- `p062_polyannulus_over_mixed_towers_20260919/PROOF.tex`:
  `668ef5932822c8355b2aaf59e4fc03bcdca364d4d37376e0a6126ac80ee52eea`
- `p062_interleaved_polyannulus_mixed_towers_20260919/STATEMENT.tex`:
  `43c52e88574a46779a0ef68d1f9ce3f1509117aa80ec0c8e1f99491450e8b9f8`
- `p062_interleaved_polyannulus_mixed_towers_20260919/PROOF.tex`:
  `1756c432c8964368188bc81fd9e5a26a2697e8cf0744dc366fe903c362be894c`
- `p213_residual_picard_mixed_towers_20260911/MIXED_TOWER.tex`:
  `d3b4b702c2655cc20c01b454d188ea30595d93936a733c6e11460bfa1b6d0672`
- `p213_endpoint_mixed_towers_20260911/STATEMENT.tex`:
  `6728ba06c8539fb76a02516a85b5c441cae63cf5a26cbca945ba33b8fe3754a6`
- `p213_endpoint_mixed_towers_20260911/PROOF.tex`:
  `dec23edddf46f31a9b97a69dcc7813f9b2af752a2a9598298917625e9d71215f`
- `ch18_delta_forms.tex`:
  `ebd08b1b1973ece28628eda73fa296f8ac5e25214da387c70fa76f880a5e63be`
- `ch72_major_open_problems.tex`:
  `4bd0b6a90fd730204bf791a58eab8da538e23f6989cd1bc17dd7caf1c7dc3b34`
- `book.pdf`:
  `02655c6e8822cb82dbbcd3bf3d4ee37370fc3bfe8e10b411792bbfc17f81f5bd`

## Proof and scope checks

- The new exact stage invokes
  `prop:p062-smooth-proper-split-toric-bundle-descent`, including its
  strengthened first-current conclusion, without changing any hypothesis.
- Smooth proper split-toric fibres are connected.  In each bundle chart the
  identity of the dense split torus supplies a local section, so locally
  constant annular slopes descend.  Transition maps need not preserve that
  section because fibrewise constancy already forces overlap agreement.
- Algebraic closedness is still imposed only by a proper smooth curve stage
  or by the published-curve base.  The split-toric stage itself works over
  every complete nontrivially valued ground field.
- The endpoint and residual-Picard extensions descend the function before
  applying the bottom classification; they introduce no pullback of a
  nonsmooth current.
- Singular, nonsplit, nonproper, and non-locally-trivial toric fibres,
  arbitrary fibrations, and locally unrelated annular coordinates remain
  outside the statements.

## Mechanical checks

- Forced full-book build and the automatic second full pass: PASS.
- Output: 3331 pages, 17,665,893 bytes, PDF 1.5.
- Build-closure reference audit: 353 files, 11,319 labels, zero multiply
  defined labels, zero dangling references, and clean per-file structure.
- Open-problem inventory audit: PASS; tiers
  T1=0, T2=5, T3=8, T4=16, T5=17.
- Final log scan: no undefined citation, undefined reference,
  multiply-defined-label, label-change, or rerun warning.
- Strict `mingchen-writing` audit on the exact P06.2 source files: zero
  errors and zero warnings.  The bibliography-aware run retains the single
  pre-existing freshness warning for `GR25Classical`; no source claim or
  citation was added in v62.
- A diagnostic run on the older P21.3 source files reports their pre-existing
  legacy inline-delimiter and optional-title style findings.  Every new v62
  line uses the current house style, and this propagation patch introduces
  no new finding.
- `git diff --check`: PASS.

## Automatic second pass and visual review

The second pass rechecked the four exact stage descriptions, field
hypotheses, connectedness, local sections, overlap descent, annular-stage
indexing, endpoint and residual-Picard dependency order, and all excluded
scopes.  It also converted the v61 single-bundle disclaimer into an explicit
historical note and removed stale three-type language from the live
synthesis and status records.

The final PDF was inspected on physical pages 1297, 1299--1300, 1303--1304,
and 1313 (printed pages 1229, 1231--1232, 1235--1236, and 1245), together with
physical pages 3146, 3171, and 3175 (printed pages 3078, 3103, and 3107).
The four-type statements, annular coefficient descent, downstream P21.3
theorems, and Chapter 72 summaries are complete and visually clean.

No model-backed verifier was used for v62; this version is a formally closed
propagation of the source-checked and already integrated v61 descent theorem.
