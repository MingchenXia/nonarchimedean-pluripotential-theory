# P09.2 partial-reduction live-integration receipt — 25 August 2026

## Scope and mathematical disposition

This receipt controls the exact live integration of a source-derived reduction
of the ordinary delta-metricity question for canonical cubical metrics.  Over
an algebraically closed, complete, nontrivially valued field, and for a fixed
abelian variety `A`, it proves the following.

1. Every cubical metric on every rigidified line bundle in `Pic^0(A)` is an
   ordinary delta-metric in the algebraic tropical-chart sense of
   Gubler--Künnemann.
2. The directly induced symmetric and antisymmetric factors `L_+` and `L_-`
   are cubical, `L_-` lies in `Pic^0(A)`, and evaluation gives the metric
   isometry `L^{\otimes 2} \simeq L_+ \otimes L_-`.  Hence the original
   cubical metric is ordinary delta if and only if its symmetric factor is.
3. On `A`, universal ordinary delta-metricity for cubical metrics is
   equivalent to ordinary delta-metricity for cubical metrics on ample
   symmetric rigidified line bundles.

This does **not** settle P09.2.  Its remaining range is the ample-symmetric
case in non-isotrivial mixed reduction.  No novelty or priority claim is
made.

## Controlling production verification

The exact source-aware statement and proof passed production Rethlas run
`20260825T145229Z_b37e13478cc7`, item
`pi_10f6228b6e69e780dad8b17b`, with verifier `gpt-5.6-sol` at `xhigh`.
The final disposition is `correct`, with 1/1 item checked, zero critical
errors, and zero gaps.  The item consumed 400.207 seconds and reported 168
tokens used.

The exact packet hashes are:

| file | SHA-256 |
|---|---|
| `p09p2_reduction_statement_exact_20260825.tex` | `b37e13478cc753ff1ba131540dda18ab93f421b047e04cb9b4673370ce466655` |
| `p09p2_reduction_source_aware_proof_exact_20260825.tex` | `3967095b314a63a2dd805a5205fbe8904e998b5284dfe350a4fa6ed6f755a919` |
| `p09p2_reduction_source_aware_request_20260825.json` | `e6164af868a3b0e2f513e57044e18ab197599ee0957fae1e9e0a4b58c6cc4485` |
| `p09p2_reduction_source_aware_response_20260825.json` | `7a6c014ec0fc108ddc7467e86907887549ce37fc99be9bc31773af5254251105` |
| `p09p2_reduction_source_aware_headers_20260825.json` | `8851a52b519d7a50a85954112374aab39ffc7926a639350b3786c1ed45bfbebf` |

The copied run artifacts are preserved under
`p09p2_reduction_run_20260825/`.  Their hashes are:

| artifact | SHA-256 |
|---|---|
| `aggregate/manifest.json` | `7b3f96192a93452b78e6d8e96e071872da716c6f1fc41ce444eb5412ab985f98` |
| `aggregate/verification.json` | `c9dadfd0703a3ab2b00d82c422e1ba794c29b5eebdef12473679289ab9f62440` |
| `item/log.md` | `d8e6fbc209f20e332153e214709d27feaf5ade41561609ef33e70c91939535ff` |
| `item/process_child_guard.json` | `8d72524143a41c2b81cb304f4086b680507cabd9b9b32ec1b7f83d0db5ceee3e` |
| `item/process_guard.json` | `8bb859d826106a130060cd569c363936be044f449fbea304022386e1749e6cf2` |
| `item/verification.json` | `954c950bc23f92b1992a5b34df013ad114a2e0ab3848869f9cce60677ea78dfa` |

The audited local production-verifier checkout was at Git commit
`60ca1e612f9779466621094efccb474fb4d22432`.  The recorded production code
hashes are `88692d...` for the server, `e08278...` for proof context,
`0adabc...` for contracts, and `17313b...` for process supervision; the full
values remain in the preserved run manifest.

## Source audit and exact live-byte integration

The dependency audit is preserved in
`p09p2_reduction_source_audit_20260825.tex`.  The proof consumes the precise
recognition, closure, and algebraicity statements in Gubler--Künnemann,
Gubler's 2010 canonical-measure paper, the cubical-metric lemmas of
Chambert--Loir--Ducros, Milne's Picard and inversion identities, and the
specified Stacks Project ampleness lemmas.  It uses neither weak smoothness
nor harmonic tropicalizability as a substitute for ordinary delta-metricity.

`parts/part2/ch19_cld_examples.tex` inputs the frozen statement and proof
files without transcription.  The live chapter, Chapter 72, Appendix L, the
atomic inventory, the research ledger, the theorem-provenance ledger, and
the build status all record the same reduced frontier.  P09.2 remains active,
so the inventory counts are unchanged: 57 atoms, with
`T1=0`, `T2=8`, `T3=15`, `T4=17`, and `T5=17`.

The production-source closure has 107 files.  Its controlling ledger is
`editorial/current_source_closure_20260825.sha256`, with SHA-256
`f5dfe4a980d732371d2ca0212779f744ee17acd73c1079c4fe40c4dc08d9ee87`.
The two new dependencies have the exact statement/proof hashes printed
above.  The dated 24 August release ledger was not changed.

## Build, static, and visual gates

The converged command

```sh
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex
```

produced `book.pdf` with 3,139 pages and 15,134,244 bytes.

- PDF SHA-256:
  `47ae41330b4683f15903c3f2b9c604f4d880492b7f198458b8c4d69c65c90a3f`.
- Log SHA-256:
  `e81d0c6aaa5d664bd53f23987da578805d6ce6fda2fa0759399118a26e915ee7`.
- No TeX error, undefined control sequence, fatal or emergency stop,
  undefined reference or citation, multiply defined label, duplicate
  destination, or overfull box was found.
- There is no exercise environment and no optional name on a theorem, lemma,
  proposition, corollary, or claim.
- The author field is empty and the acknowledgements have no body text.
- `git diff --check` passed.

Rendered visual inspection passed for the scope record on printed page 874,
the theorem and proof on printed pages 876--878, the Chapter 19 synthesis on
printed page 904, and the Chapter 72 residual-problem record on printed pages
2892--2893.  No clipping, overlap, malformed link, or unreadable display was
observed.

This receipt records verification and integration only; it does not assert
publication, novelty, or priority.
