# P03.1 v60 live build report

Date: 2026-09-20

## Integration

The canonical scalar section and the compact-fiber maximum formula are
combined into an exact continuous-retraction normal form.  For arbitrary
locally bounded-above data, the canonical retraction realizes the whole
fiber maximum and identifies the strict scalar regularization defect with
failure of retraction invariance.  For the affine Perron family, the same
identity reduces classical psh-ness exactly to subharmonicity of the
retracted pullbacks on all extended smooth strict curves.  Chapter 72 and the
atomic inventory record the sharpened residual obligation.  P03.1--P03.3
remain active, and the inventory remains at 46 active atomic questions in 14
formal problem environments.

## Exact hashes

- `STATEMENT_LIVE.tex`:
  `ce4b65de2f3094389557b2134ef6a30feb71a610bcc0bbe8c1b9d78fd8d24e91`
- `PROOF_LIVE.tex`:
  `8bb379143fb408776a8283008031407b4b81a2357b27bf56b0ec520767349ed1`
- `book.pdf`:
  `c2b40c81c16c9650aa00bb60266171f7df2a1816dd15792541fa8f13d7e1204c`

## Source and scope checks

- No new external theorem is imported.  The proof uses only the already
  audited canonical-section regularization formula, the already audited
  compact-fiber maximum formula, and the affine Perron curve-test interface.
- The quarantined v5 Shilov-boundary uniqueness claim is not used.
- No analyticity of the retraction and no psh-preservation under composition
  with it is asserted.  The defect is expressed as a strict inequality locus,
  avoiding subtraction at the value `-infinity`.

## Mechanical checks

- Forced full-book `latexmk` build and post-second-pass rebuild: PASS.
- Output: 3327 pages, 17,649,515 bytes, PDF 1.5.
- Build-closure reference audit: 351 files, 11,317 labels, zero multiply
  defined labels, zero dangling references, and clean per-file structure.
- Open-problem inventory audit: PASS; tiers
  T1=0, T2=5, T3=8, T4=16, T5=17.
- Final log scan: no undefined citation, undefined reference,
  multiply-defined-label, label-change, or rerun warning.
- Strict `mingchen-writing` audit on the exact new statement and proof: zero
  errors and zero warnings before and after the second pass.
- `git diff --check`: PASS.

## Automatic second pass and visual review

The second pass checked all hypotheses, the `-infinity` edge case, the four
equivalent compatibility conditions, the all-extensions curve-test
quantifiers, and the scope firewall.  It replaced the ambiguous phrase
``the same section'' by ``the canonical scalar section''.  The final PDF was
inspected on physical pages 791--794 (printed pages 723--726) and physical
page 3101 (printed page 3033).  The statements, formulas, proofs, Chapter 15
synthesis, and Chapter 72 status paragraph are complete and visually clean.

No model-backed verifier was used for this version.
