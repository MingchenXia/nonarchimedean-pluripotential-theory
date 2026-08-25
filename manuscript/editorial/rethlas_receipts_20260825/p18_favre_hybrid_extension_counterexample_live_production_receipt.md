# P18.1 Favre hybrid-extension counterexample: exact live-byte production receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)
**Status:** **EXACT LIVE THEOREM AND PROOF VERIFIED**
**Verifier:** production Rethlas at `127.0.0.1:8107`
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

After integration into Chapter 66, the exact current theorem-and-proof bytes
were frozen and submitted again.  The response has
`verification_status = final` and `verdict = correct`.  Rethlas checked one
proof item, with zero failed or blocked items, zero critical errors, zero
gaps, and no request for an expanded proof.

## Run identity and verdict

* Run: `20260825T033425Z_387f7c3e1c73`.
* Proof item: `pi_fa774e5700653dc53c78b02d`.
* Item title: `theorem synthetic:main`.
* Started: `2026-08-25T03:34:25.813979+00:00`.
* Item elapsed time: `191.688` seconds.
* Reported token count: `126`.
* Adaptive round: `0`; no expanded proof was requested.
* Verifier process: completed with return code `0`; output validated.
* Process-guard command SHA-256:
  `dd67f6317580bae0e561247ba5f083d35a7a46d877b41fb068509babd2af814d`.
* HTTP result: `200 OK`.

The item-level verification summary is:

> The proof is complete and correct. The scalar construction,
> logarithmic-growth and zero-Lelong estimates, non-Archimedean metric
> computation, hybrid discontinuity argument, and Favre uniformity comparison
> are valid; the cited results and their hypotheses match their uses.

## Exact submitted live bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_live_statement_exact_20260825.tex` | 2232 | 57 | `387f7c3e1c73180c9bab030374d534397be07e7498273ab588735c46a41aa555` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_live_theorem_proof_exact_20260825.tex` | 11713 | 325 | `9076a405f6b2cd5c2ff31bcd0f77bc0deea3a78f2f1ed94aa9d77e01a3f505dc` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_counterexample_live_source_aware_request_20260825.json` | 15164 | 5 | `94edb6dd939e62449483a2078c0aed163ce52b50ee7129d6d4fbbd311f1b396e` |

Decoding the request fields with `jq -j '.statement'` and
`jq -j '.proof'` reproduces the frozen live statement and theorem/proof byte
for byte; both `cmp` checks returned zero.  The request deadline was
`2026-08-25T06:00:00+00:00`.

## Returned digests

* Proof digest:
  `9076a405f6b2cd5c2ff31bcd0f77bc0deea3a78f2f1ed94aa9d77e01a3f505dc`.
* Aggregate context digest:
  `96cc035c8c5dfab155b2d2841b43d914055b4b30937d55e0a89550ae5df686da`.
* Adaptive context digest:
  `471501de7f0a143330429598660b415cd9ee6727d1368577e258f1a8c17d91ae`.
* Item context digest:
  `30d3fcb75e6aebdebeffafcdfebf2c5dea2126d057755aca2b18a512cdae3076`.

## Preserved production artifacts

| Preserved artifact | SHA-256 |
|---|---|
| `p18_favre_hybrid_extension_counterexample_live_api_response_20260825.json` | `673511240482eb80b11e6e2cdcc23d9e9a59260f58918ca496bac080181589b4` |
| `p18_favre_hybrid_extension_counterexample_live_http_headers_20260825.txt` | `9415741529542f5b3d40dd3f1ec8cad409bbf51c5bd1eba4f383735c335d92dd` |
| `p18_favre_hybrid_extension_counterexample_live_run_manifest_20260825.json` | `f91d31294f65a90f4b7f864a0d8ae0975f832cd2e9573b417f4f5650bfed6692` |
| `p18_favre_hybrid_extension_counterexample_live_run_verification_20260825.json` | `6c3add3651ef615aef459a83a3d36cb6e698911432e6a94f041bb255a2ba6797` |
| `p18_favre_hybrid_extension_counterexample_live_item_verification_20260825.json` | `cb3740f12951bf5c19fb4d9ef03acb5ba20dff4310e57fb7db4fcd596edf0b52` |
| `p18_favre_hybrid_extension_counterexample_live_item_log_20260825.md` | `1babc65f57fad05ab21152bc72a9b0040348ef1a2691a3ea29b89610c7f8113d` |
| `p18_favre_hybrid_extension_counterexample_live_process_guard_20260825.json` | `51754c84bd982d4aa528e523ae412d57450e130db718f3aee7ea51f9d5aa843e` |
| `p18_favre_hybrid_extension_counterexample_live_process_child_guard_20260825.json` | `8e58984d567953fc3d66a9cd94744a5d9a4b718a5c7f413894769a1c61ab6fe1` |

The API response and all six JSON/Markdown service artifacts are exact copies
of the production response or production result directory.  Both process
guards finish in state `completed`.

## Scope controlled by this receipt

This gate verifies the exact Chapter 66 theorem and proof as integrated at
the time of freezing.  It establishes the negative answer to the literal
unnormalized Pille-Schneider/Favre continuity question in precisely the scope
stated there.  It does not attest to any later change, nor to the separately
formulated normalized residual problem in Chapter 72.  A stronger normalized
construction must be frozen and verified as a new proof object before it is
integrated.

## Later controlling addendum

That stronger normalized construction was subsequently frozen and verified.
Production run `20260825T035945Z_070e264c3ef1`, item
`pi_db89dd432acabcf33a3f2272`, returned final `correct`, zero critical
errors, and zero gaps.  The Chapter 66 theorem has now been strengthened and
the Chapter 72 normalized residual retired.  This receipt remains the exact
historical gate for the earlier scalar live bytes; it does not control the
newly adapted bytes.
