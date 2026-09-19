# P06.2 smooth proper split-toric bundle descent v61: live build report

This is the historical v61 build snapshot.  The v62 mixed-tower report
supersedes the temporary single-bundle limitation recorded below.

Date: 2026-09-20

## Integration

Chapter 18 now proves exact descent of continuous zero-current functions
through analytically locally trivial bundles with smooth proper split toric
fibre.  The proof exhausts the regular maximal-cone affine charts by strict
open polydiscs and uses the identity of the dense split torus as their common
point.  The new curve corollary gives classical pluriharmonicity, local
real-PL regularity, and Gubler--Jell--Rabinoff harmonicity without an
invariance hypothesis.  Chapter 72 and the atomic inventory record the new
range and its scope firewall.  P06.2 remains active, and the inventory
remains at 46 active atomic questions in 14 formal problem environments.

## Exact hashes

- `STATEMENT_LIVE.tex`:
  `7f86361608ec8c0299363bc4313caaa1749db7f5f0c91b5bce8a8f5a2ad0ba11`
- `PROOF_LIVE.tex`:
  `4a5878825079b6b68cd9697d17573e291bf18d5ca6102a36bbb5d86cda149a17`
- `book.pdf`:
  `00e31f8605d14803b783a8a3cc0f8b8c9be023700b7d3902e6f7036e03e9526a`

## Source and scope checks

- Cox--Little--Schenck, *Toric Varieties*, Example 1.2.21 and Theorems
  3.1.19 and 3.4.1 supply the exact regular-chart, smooth-fan, and
  proper/complete-fan locators used in the proof.
- The proof uses only the already integrated strict open-disc descent and
  current-sheaf gluing results after the toric affine-chart reduction.
- The common-point argument uses the split-torus identity and imposes no
  invariance on the function.
- Singular, nonsplit, nonproper, and non-locally-trivial toric fibres remain
  outside the claim.  The new stage was not silently added to the older
  mixed-tower statements.

## Mechanical checks

- Forced full-book build before the automatic second pass and full rebuild
  after the second pass: PASS.
- Output: 3331 pages, 17,664,744 bytes, PDF 1.5.
- Build-closure reference audit: 353 files, 11,319 labels, zero multiply
  defined labels, zero dangling references, and clean per-file structure.
- Open-problem inventory audit: PASS; tiers
  T1=0, T2=5, T3=8, T4=16, T5=17.
- Final log scan: no undefined citation, undefined reference,
  multiply-defined-label, label-change, or rerun warning.
- Strict `mingchen-writing` audit on the exact new statement and proof: zero
  errors and zero warnings before and after the second pass.
- `git diff --check`: PASS.

## Automatic second pass and visual review

The second pass rechecked the fan hypotheses, strict-radius exhaustion,
positive-dimensional iterated bases, common-point gluing, overlap gluing,
curve pullback, citation locators, and all excluded scopes.  It also revised
the synthesis prose to make clear that the older mixed-tower theorem admits
the projective-space and proper-curve stages, while this new toric stage is
currently a single-bundle result.  The final PDF was inspected on physical
pages 1293--1295 and 1320 (printed pages 1225--1227 and 1252), and physical
pages 3146--3148 (printed pages 3078--3080).  The statement, proof,
corollary, synthesis paragraph, and Chapter 72 status prose are complete and
visually clean.

No model-backed verifier was used for this version.
