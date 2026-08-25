# P18.1 frozen-packet manifest

Frozen: 2026-08-25 (Asia/Shanghai).

Status: **production Rethlas final/correct**; **not yet integrated into live
chapters at the time of this packet freeze**.

## Files and exact hashes

| File | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `p18_favre_hybrid_extension_counterexample_statement_exact_20260825.tex` | 2189 | 57 | `13e01361eefff7ef85c003aded9deb9609f5025db0373e14d9cbf71532a0bed3` |
| `p18_favre_hybrid_extension_counterexample_source_aware_proof_exact_20260825.tex` | 12805 | 349 | `c52e050011f568bc928e39f43cca784839c4820112505efbe55141eaf187e823` |
| `p18_favre_hybrid_extension_counterexample_source_aware_request_20260825.json` | 16230 | 5 | `ba915ea1b53bd8e6310a67c048b1f6b775e3e680f919a950b4980480e7bc65ad` |
| `../solver_dossiers_20260825/p18_favre_hybrid_extension_counterexample.md` | 16174 | 418 | `1c952fd47d2fb7c43ef0fd78a6edd8207ad4ab95dabb5e2389b2b66dd32428a7` |

The theorem environment extracted from the source-aware proof is byte-for-byte
identical to the exact statement file (`diff -u` returned no output).

## Authenticated sources

| Source | Local file | SHA-256 |
|---|---|---|
| Pille-Schneider, arXiv:2209.04879v2 | `tmp/pdfs/ps23_hybrid.pdf` | `55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7` |
| extracted Pille-Schneider text | `tmp/pdfs/ps23_hybrid.txt` | `dc7672bad7443db5a757a3fd3d34897c9ee89dbb6f749d33bd26e58e74391326` |
| Favre, arXiv:1611.08490v2 | `tmp/pdfs/Favre20_arxiv1611.08490_primary.pdf` | `137ddb0245b4f09ff8b7a4a2880bd3846f146cd013f2ce9563d7f90f45ea1a5f` |

## Local checks

* Isolated TeX compilation with `pdflatex` through `latexmk`: PASS,
  five-page PDF, no unresolved references after the second pass.
* Exact-statement extraction comparison: PASS.
* Construction checked in the proof:
  smooth subharmonicity on the punctured disk, finite psh extension,
  zero Lelong number, logarithmic-growth lower bound, two distinct
  normalized limits, all vertical generic Lelong numbers zero, hybrid
  convergence along a constant section, and Favre non-uniformity.
* External theorem verification: PASS after explicit user authorization.
  Production run `20260825T030402Z_13e01361eeff`, item
  `pi_e8a9764e8fb295f8ff4cefbb`, returned `final/correct`, with zero
  critical errors, zero gaps, and no expanded-proof request.  The returned
  proof digest equals the frozen proof SHA-256.
* Controlling receipt:
  `../rethlas_receipts_20260825/p18_favre_hybrid_extension_counterexample_production_receipt.md`,
  SHA-256
  `54622ec2e782df67010e92c4176fce42563ec943fa71d8868f70b251249479af`.

## Scope restrictions to retain in any verification request

1. The example refutes the literal Pille-Schneider Question 3.18 and the
   exact live problem, but is a base-scalar obstruction.
2. It separately refutes the reverse implication in Favre's literal
   Question 1; no equivalence of the two formulations is assumed.
3. It does not refute Theorem 3.13 (the glued metric remains psh),
   Proposition 3.16, the canonically polarized case, the abelian case, or
   continuity under Favre uniformity.
4. It does not settle a strengthened question modulo base scalars or with
   a uniform scalar normalization.
