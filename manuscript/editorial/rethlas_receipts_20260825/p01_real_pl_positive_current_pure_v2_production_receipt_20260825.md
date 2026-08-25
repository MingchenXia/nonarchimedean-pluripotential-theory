# P01 positive real-PL current: controlling production receipt

Date: 25 August 2026.

## Controlling object

The exact pure-dimensional theorem and proof inserted in Chapter 18 are
frozen in:

- `../rethlas_packets_20260825/p01_real_pl_positive_current_residue_nef_pure_statement_exact_v2_20260825.tex`;
- `../rethlas_packets_20260825/p01_real_pl_positive_current_residue_nef_pure_proof_exact_v2_20260825.tex`;
- `../rethlas_packets_20260825/p01_real_pl_positive_current_residue_nef_pure_candidate_v2_20260825.tex`;
- `../rethlas_packets_20260825/p01_real_pl_positive_current_residue_nef_pure_request_v2_20260825.json`.

Their SHA-256 digests are:

| object | SHA-256 |
|---|---|
| statement | `80f35689475f6c9d566536c11b7dbe03fdd779ce0e6de5924ba33c2cbcbc602b` |
| proof | `de228d94fe5d5e310001fcddc5565d81e6feb1ce8d339e44a770abc03c790c1b` |
| combined candidate | `d1722ba7df364dfd7a3bd77bb0ca6d3b8967884252d76cfcdb94a5c9eed2f57c` |
| request | `94c4902c8e2fd97df1cd9e080bbf898c3ea15e7b44d990be78faaebc36d863df` |

## Production verification

- run: `20260825T080059Z_80f35689475f`;
- item: `pi_33f9d15994f62f668065256e`;
- model: `gpt-5.6-sol`;
- reasoning effort: `xhigh`;
- status/verdict: `final` / `correct`;
- critical errors: `0`;
- gaps: `0`;
- proof digest reported by the verifier:
  `de228d94fe5d5e310001fcddc5565d81e6feb1ce8d339e44a770abc03c790c1b`;
- elapsed verifier time: `503.065` seconds.

The raw production artifacts are preserved in
`p01_real_pl_positive_current_pure_v2_run_20260825/`.  Selected artifact
digests are:

| object | SHA-256 |
|---|---|
| aggregate manifest | `e35140cf31697410df6e29237ba8c88dc590798ceadf910f2445fce6f46a4517` |
| aggregate verification | `49e01f8be4d9a24e68885ef42cd8f4391d2910b860c1edc30698e953fb8d0324` |
| item log | `afcb27023bebff53d353136603499a1e1eef397b9457c1475231c8d554e30fad` |
| item verification | `4fff739ebd0f827a18dc384d9f8664d275eec30f4c3784ce07bac41ee5ddce87` |

The report states that the proof was checked deduction by deduction, that
the cited results match the authoritative sources and their hypotheses, and
that the rational approximation and limiting-nefness arguments are valid.

## Exact-live gate

After integration, the theorem and proof were independently extracted from
`parts/part2/ch18_delta_forms.tex` and compared with `cmp` against the two
frozen exact files above.  Both comparisons returned status `0`.  At this
gate the complete Chapter 18 source had SHA-256
`06e05b3fd3a521bd9fb6779c16adbe67d44dd5c5e9387e7d435d0d8432209c87`.
The transition paragraphs surrounding the exact block are editorial prose
and are outside the verified bytes.

## Scope and historical firewall

The controlling theorem concerns good, separated, strict,
pure-dimensional analytic spaces; the global statement is boundaryless and
the boundary statement is made on the relative interior.  It proves the
equivalence between positive CLD current, residue-nefness, and GJR
semipositivity for real PL functions.  It does not define a fixed-bidegree
CLD current on an arbitrary non-pure space.

An earlier broader wording passed run
`20260825T075050Z_235cca2fd59b`, but that run is noncontrolling because its
scope did not respect the pure-dimensional `n`-space formulation of the CLD
source.  Its raw artifacts are preserved in
`p01_real_pl_positive_current_general_scope_run_20260825/`; its item
verification has SHA-256
`f590eaf7fd3d11ea56ca5044e0e85def15fbdc2ab914fe7bfcd1346d53132cd8`.

The former curve-lifting attempt and its negative verdict remain rejected.
The successful proof is different: it uses an ample residual order unit and
does not pull a positive current back to a curve.  No novelty or priority
claim is made.
