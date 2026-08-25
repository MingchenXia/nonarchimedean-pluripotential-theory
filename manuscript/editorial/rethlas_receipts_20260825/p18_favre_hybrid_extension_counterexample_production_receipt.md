# P18.1 Favre hybrid-extension counterexample: production receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)  
**Status:** **VERIFIED FROZEN PACKET; NOT YET INTEGRATED INTO A LIVE CHAPTER**  
**Verifier:** production Rethlas at `127.0.0.1:8107`  
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The exact source-aware theorem and proof returned
`verification_status = final` and `verdict = correct`.  Rethlas checked one
proof item, with zero failed or blocked items, zero critical errors, zero
gaps, and no request for an expanded proof.  This receipt controls only the
frozen bytes listed below.

## Run identity and verdict

* Run: `20260825T030402Z_13e01361eeff`.
* Proof item: `pi_e8a9764e8fb295f8ff4cefbb`.
* Item title: `theorem synthetic:main`.
* Started: `2026-08-25T03:04:02.888418+00:00`.
* Item elapsed time: `294.525` seconds.
* Reported token count: `109`.
* Adaptive round: `0`; no expanded proof was requested.
* Verifier process: completed with return code `0`; output validated.
* Process-guard command SHA-256:
  `4f3d8f771a3339394f5a9bb52082197893b51e810a02f3f120c7cfb71c0daf87`.
* HTTP result: `200 OK`.

The item-level verification summary is:

> The context is complete and untruncated. Every deduction in the scalar
> construction, its extension to the polarized product family, the
> non-Archimedean metric computation, the hybrid discontinuity argument, and
> the independent verification of Favre's three conditions is valid. The
> cited statements from Pille-Schneider and Favre match their authoritative
> arXiv sources and are applied with compatible hypotheses and normalizations.

## Exact submitted bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_statement_exact_20260825.tex` | 2189 | 57 | `13e01361eefff7ef85c003aded9deb9609f5025db0373e14d9cbf71532a0bed3` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_source_aware_proof_exact_20260825.tex` | 12805 | 349 | `c52e050011f568bc928e39f43cca784839c4820112505efbe55141eaf187e823` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_source_aware_request_20260825.json` | 16230 | 5 | `ba915ea1b53bd8e6310a67c048b1f6b775e3e680f919a950b4980480e7bc65ad` |

Decoding the request fields with `jq -j '.statement'` and
`jq -j '.proof'` reproduces the frozen statement and proof byte for byte;
both `cmp` checks returned zero.  The request deadline was
`2026-08-25T06:00:00+00:00`.

## Returned digests

* Proof digest:
  `c52e050011f568bc928e39f43cca784839c4820112505efbe55141eaf187e823`.
* Aggregate context digest:
  `e1fdf6b7c94902a14bad3a9d16deb2f29b23419c8eb72e9ca595d6288f8da374`.
* Adaptive context digest:
  `340d0318dbf76a2c75624fd40f2e41610ad2914007116f209d52dc0b1d379714`.
* Item context digest:
  `aa93a48faac6b3d6d360ef50c7ab47db237bc966eba23ef1bcc6e8b29b5ff30a`.

## Preserved service artifacts

| Preserved artifact | SHA-256 |
|---|---|
| `p18_favre_hybrid_extension_counterexample_api_response_20260825.json` | `142e3d9bb5d7d6886c3e867edaa3336d0298fcd64b38fd997c070e870e447cae` |
| `p18_favre_hybrid_extension_counterexample_http_headers_20260825.txt` | `06dcaee73c53cf2e19cddb7be0182a2dce24d5ec0536aea7bde7673f16a6d003` |
| `p18_favre_hybrid_extension_counterexample_run_manifest_20260825.json` | `ba5be99e93369a93de7583512eca2aac61872298ea69230270ff12db44a00d66` |
| `p18_favre_hybrid_extension_counterexample_run_verification_20260825.json` | `549adc7e3ae00f7264867233a19b95805c2f1b35699914b5f8fda521860cde69` |
| `p18_favre_hybrid_extension_counterexample_item_verification_20260825.json` | `c90533fb6b91cc147f788a81a5eab85074f4827714af21b23f81d3ffb18bbaaf` |
| `p18_favre_hybrid_extension_counterexample_item_log_20260825.md` | `1c4cdf68939a3589099e1010f332aa0f6e17cf8dfd27936fe360b2cc2188c71b` |
| `p18_favre_hybrid_extension_counterexample_process_guard_20260825.json` | `9f3089b6e1970f2ca0c29df1f53acef598db8ca545d5fbcb2b79076523c47350` |
| `p18_favre_hybrid_extension_counterexample_process_child_guard_20260825.json` | `38889d7a5771b96046ad02c7f4e45e3e86bc6abf275d652f07aef9ea230fad06` |

The API response and all six JSON/Markdown service artifacts are exact copies
of the production response or production result directory.  Both process
guards finish in state `completed`.

## Exact verified mathematical scope

The verified packet proves a counterexample on the smooth trivial
degeneration
\[
       \mathbf P^1_{\mathbf C}\times\mathbb D^*
       \longrightarrow\mathbb D^*.
\]
The punctured metric is smooth and semipositive, extends as an everywhere
finite psh metric on the product model, has logarithmic growth, and has the
continuous Fubini--Study model metric as its associated non-Archimedean
metric.  Its canonical hybrid psh extension is nevertheless discontinuous.
Thus Pille-Schneider's Question 3.18, and the exact live problem reproducing
it, have a negative answer as literally formulated.

The same construction separately satisfies all three intrinsic conditions in
Favre's Question 1 but is not uniform.  This proves that the reverse
implication in Favre's literal question is false without assuming equivalence
with the Pille-Schneider formulation.

## Scope firewalls

1. This is a base-scalar obstruction.  It does not decide a strengthened
   problem modulo pullbacks from the base or with a normalization controlling
   those scalars.
2. It does not contradict Pille-Schneider's Theorem 3.13: the glued metric is
   psh; only continuity fails.
3. It does not contradict Proposition 3.16, the canonically polarized case,
   the abelian case, or continuity under Favre uniformity.
4. No live chapter has yet been edited.  Integration must remove the literal
   question from the open-problem ledger while retaining the normalized
   residual problem explicitly.
5. Do not alter the frozen statement, proof, request, response, logs, or
   guards.  Any byte change creates a new proof object and requires a new
   receipt.

