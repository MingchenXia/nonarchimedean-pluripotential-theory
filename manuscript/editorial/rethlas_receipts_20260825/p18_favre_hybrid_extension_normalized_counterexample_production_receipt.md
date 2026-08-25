# P18.1 normalized hybrid-continuity counterexample: production receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)
**Status:** **VERIFIED MATHEMATICAL PACKET; LATER EXACT-LIVE GATE PASSED**
**Verifier:** production Rethlas at `127.0.0.1:8107`
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The exact source-aware zero-supremum theorem and proof returned
`verification_status = final` and `verdict = correct`.  Rethlas checked one
proof item, with zero failed or blocked items, zero critical errors, zero
gaps, and no request for an expanded proof.  This packet strengthens the
earlier base-scalar counterexample and controls the mathematical integration
that retires the normalized P18 residual.

## Run identity and verdict

* Run: `20260825T035945Z_070e264c3ef1`.
* Proof item: `pi_db89dd432acabcf33a3f2272`.
* Item title: `theorem synthetic:main`.
* Started: `2026-08-25T03:59:45.498567+00:00`.
* Item elapsed time: `518.835` seconds.
* Reported token count: `109`.
* Adaptive round: `0`; no expanded proof was requested.
* Verifier process: completed with return code `0`; output validated.
* Process-guard command SHA-256:
  `b8a689aec63c23903d03952cf6267753fcbc9228a622452b52d5409ed9d9cf84`.
* HTTP result: `200 OK`.

The item-level verification summary is:

> The complete proof is logically sound. The scalar subharmonic
> construction, logarithmic bounds, psh metric construction, divisorial
> Lelong-number computation, non-Archimedean identification, hybrid
> noncontinuity, and Favre non-uniformity argument all check out. The cited
> statements from Pille-Schneider and Favre match their authoritative arXiv
> sources and are applied with the required hypotheses.

## Exact submitted bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_normalized_counterexample_statement_exact_20260825.tex` | 2553 | 68 | `070e264c3ef1d1e6c436eb7215ee50e1801bfeab667159234e7d755bc69a52f8` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_normalized_counterexample_source_aware_proof_exact_20260825.tex` | 15292 | 416 | `0e9c8fdf755a714eccc2c3bc0215d8c43ad05c04ab664077205bfa552dd1ef90` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_normalized_counterexample_source_aware_request_20260825.json` | 19313 | 5 | `93a684c37e273851661762bb7af2827ad41cdbc512538136ba6dd2fe4b213b4f` |

The theorem copied from the proof is byte-identical to the statement file.
Decoding the request fields with `jq -j '.statement'` and
`jq -j '.proof'` reproduces the statement and proof byte for byte.  An
isolated `pdflatex` syntax check passed.  The request deadline was
`2026-08-25T08:00:00+00:00`.

## Returned digests

* Proof digest:
  `0e9c8fdf755a714eccc2c3bc0215d8c43ad05c04ab664077205bfa552dd1ef90`.
* Aggregate context digest:
  `c75bc6d4fed19f22d493544092f6dc6cd07ec8230699b03df3e1e82ef35e111d`.
* Adaptive context digest:
  `c16c28bb40f15767e4a1e1fee5c6e3404cf15a8e5f79206ffd81f03b591277e4`.
* Item context digest:
  `a5bb9b0b7b001ac8164bb7fb824739e309b5fe1e8092f01c047ee8cb3ea7cc59`.

## Preserved production artifacts

| Preserved artifact | SHA-256 |
|---|---|
| `p18_favre_hybrid_extension_normalized_counterexample_api_response_20260825.json` | `71f6855a7587ee0d1500f31e7d88391da69ffec322d1d7ef2505f15f4d54075b` |
| `p18_favre_hybrid_extension_normalized_counterexample_http_headers_20260825.txt` | `016713786045af4a7b9551cdf00c70f283d3987ccf3d14a18cd7de3f39facb2f` |
| `p18_favre_hybrid_extension_normalized_counterexample_run_manifest_20260825.json` | `a08d863b14c5839d430fe4ba127a0ca6c23a71aab28cfcd36d0bb925cbb7ea9e` |
| `p18_favre_hybrid_extension_normalized_counterexample_run_verification_20260825.json` | `418e842ee1b065f2a0ba996dc3378cc788f78032768366278260944a4cc73266` |
| `p18_favre_hybrid_extension_normalized_counterexample_item_verification_20260825.json` | `abdcf64db3e3225179c28a2dea9cdeba1a9c55b578f5bf0a657987dcae1a4d5a` |
| `p18_favre_hybrid_extension_normalized_counterexample_item_log_20260825.md` | `5b7d561fd77ef0aabe1b556d495b72a0c8705a9e857db1d0799becb92f32a744` |
| `p18_favre_hybrid_extension_normalized_counterexample_process_guard_20260825.json` | `fe6ed23c347f62cb8eef87631e12fa70e9c5ce82eea4b77286657bd381c27407` |
| `p18_favre_hybrid_extension_normalized_counterexample_process_child_guard_20260825.json` | `cb22e0e0b0245d8d79a4b0ab776bbfe2342886c559431ce35bfab8d7f337cf94` |

The API response and all service artifacts are exact copies of the production
response or production result directory.  Both process guards finish in
state `completed`.

## Exact verified scope and integration consequence

The metric is a smooth semipositive metric on the smooth trivial degeneration
\(\mathbf P^1_{\mathbf C}\times\mathbb D^*\).  It extends as an everywhere
finite psh metric on the product model, has the continuous product
Fubini--Study metric as its non-Archimedean endpoint, and satisfies
zero-supremum normalization relative to Fubini--Study on every complex fibre
and on the non-Archimedean fibre.  Its canonical hybrid psh extension is
nevertheless discontinuous.  Thus both the literal
Favre--Pille-Schneider endpoint question and the former normalized residual
are false.

The live Chapter 66 integration keeps the verified scalar-well stage and
adapts the verified normalized family stage only in equation tags,
`\mathrm{NA}`/`\NA` notation, citations, labels, and prose cross-references.
Chapter 72 removes the normalized problem environment.  The active inventory
therefore changes from 20 to 19 formal problem environments book-wide and
from 61 to 60 atoms.  This receipt controls the frozen mathematical packet.

## Later exact-live byte-identity gate

The adapted current Chapter 66 theorem and proof were subsequently frozen
verbatim.  Their proof SHA-256 is
`992a686618355605e4f889564c402f5b2c6ff18db70762daed2dbcf4d09fdbad`.
Production run `20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`, using `gpt-5.6-sol` at `xhigh`, returned
`verification_status = final`, `verdict = correct`, zero critical errors,
and zero gaps.  The separate live-integration receipt preserves the exact
submitted bytes, response, service artifacts, and hashes.  Thus the earlier
adaptation caveat is discharged for the displayed theorem-and-proof block;
this frozen-packet receipt remains part of the audit history.
