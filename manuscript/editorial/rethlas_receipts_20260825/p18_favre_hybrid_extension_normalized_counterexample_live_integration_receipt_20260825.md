# P18 normalized hybrid counterexample: exact-live integration receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)
**Status:** **EXACT LIVE THEOREM AND PROOF VERIFIED**
**Verifier:** production Rethlas at `127.0.0.1:8107`
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The strengthened theorem under the retained label
`thm:hybrid-endpoint-continuity-counterexample` was integrated into Chapter
66.  It uses the fibrewise log-sum-exp Fubini--Study metric, has zero relative
supremum on every complex fibre and on the non-Archimedean fibre, and is
discontinuous along the two scalar-well sequences over the single section
`p_*=[0:1]`.  Chapter 72 retains the source question only as disproved
history.  At this integration stage, the Chapter 72 count was 18, the
book-wide count was 19, and the active atomic count was 60.

## Exact submitted live bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_normalized_counterexample_live_statement_exact_20260825.tex` | 2580 | 68 | `d77f7f93aeb01c9b29d0ffa170ea5301811f685e2b95f6d54b4151a9a0aad6ff` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_normalized_counterexample_live_theorem_proof_exact_20260825.tex` | 14138 | 390 | `992a686618355605e4f889564c402f5b2c6ff18db70762daed2dbcf4d09fdbad` |
| `../rethlas_packets_20260825/p18_favre_hybrid_extension_normalized_counterexample_live_source_aware_request_20260825.json` | 18168 | 5 | `19d16bbc6a657e921616e90e8652a1a420857c218b7083ab69bb7365272f69a2` |

The theorem extracted from the proof is byte-identical to the statement
file.  Decoding the request's `statement` and `proof` fields reproduces both
files byte for byte.  The submitted request deadline was
`2026-08-25T09:30:00+00:00`.

## Run identity and verdict

- Run: `20260825T043840Z_d77f7f93aeb0`.
- Proof item: `pi_b7f015a6ad5570f431769a71`.
- Item title: `theorem synthetic:main`.
- Started: `2026-08-25T04:38:40.974405+00:00`.
- Elapsed: `143.697` seconds; reported token count: `87`.
- Adaptive round: `0`; no expanded proof was requested.
- Verdict: `final/correct`; zero critical errors and zero gaps.
- Process guard: completed with return code `0`.
- Process-guard command SHA-256:
  `dc138d81edc3115aee611c272d39629df970b6cd8051f54998c439bf82abe206`.
- HTTP result: `200 OK`.

The item verification summary is:

> The construction and all deductions are valid. The cited definitions and
> theorems from Pille-Schneider and Favre match their stated uses, and the two
> hybrid limits establish the claimed discontinuity and non-uniformity.

## Returned digests

- Proof:
  `992a686618355605e4f889564c402f5b2c6ff18db70762daed2dbcf4d09fdbad`.
- Aggregate context:
  `dde0ce2934edb95ac1288c2f244b67eb869a9d4c1ed540c00e5f467627eadae6`.
- Adaptive context:
  `509b88906c2d4ccebb4f2e0097f88d734fc3982ff98d2706d9ff1f81931fc26f`.
- Item context:
  `15d05b7b33cd90b9d25fa2b7791b345bc3e162d4d4d5c18df457a56b9e8c7ab1`.

## Preserved production artifacts

| Artifact | SHA-256 |
|---|---|
| `p18_favre_hybrid_extension_normalized_counterexample_live_api_response_20260825.json` | `808cdd678193fa0632e312e4e11ff35e3da8095462702d61082214f106867a6f` |
| `p18_favre_hybrid_extension_normalized_counterexample_live_http_headers_20260825.txt` | `d9506db4dfeab79969ed65c17378ebc0acc6683cb764d440b92369cf119ae619` |
| `p18_favre_hybrid_extension_normalized_counterexample_live_run_manifest_20260825.json` | `ee0329e1e4d86d5580609a34ec1b3dfc48cb651a3f59c5f4aeaf83a78ac3174d` |
| `p18_favre_hybrid_extension_normalized_counterexample_live_run_verification_20260825.json` | `b1382e83541c53d97fcd70af4e4ea2333333e8ab35dcf4eee306662c71c713fb` |
| `p18_favre_hybrid_extension_normalized_counterexample_live_item_verification_20260825.json` | `5f70fea21328829a24c2861aaea203915e8fd30eab7417501cb444440222254e` |
| `p18_favre_hybrid_extension_normalized_counterexample_live_item_log_20260825.md` | `17e5de5cd8e3075a5e5bb6436a8f3ea52fe03974b16200a7da6a54414200042b` |
| `p18_favre_hybrid_extension_normalized_counterexample_live_process_guard_20260825.json` | `5f0cf601432708f718fc3c460817fb5bf3c858d3a0d19503c12f28e2eea019c1` |
| `p18_favre_hybrid_extension_normalized_counterexample_live_process_child_guard_20260825.json` | `87a77991ec7937466f2ddb4f7f9df0c1658ceeee45f39a72b1e13bfb62c46828` |

## Integration and checks

- The former normalized `problem` environment and its active atom were
  removed; the literal and normalized formulations are both disproved.
- `git diff --check` passed.
- Static counting at this integration stage found 18 `problem` environments
  in Chapter 72 and 19 in Chapters 71--72 together.
- A focused Chapter 66+72 build passed and produced a 60-page PDF.  Its
  SHA-256 is
  `47c5fe3222e69029ebfed3b124a787733890d4f74da59f82978829a5d6baab1f`;
  the log SHA-256 is
  `829748ec8819b80af70980631e0592d36e3d17339c6c68913e1f7955445caa6a`.
  The focused log has no unresolved P18 theorem/equation reference and no
  unresolved `PS23Hybrid` or `Favre20Hybrid` citation; its remaining
  cross-reference warnings are expected references to chapters omitted from
  the slice.
- No exercise was added, no optional conventional theorem name was supplied,
  and the new proof uses `\mathrm d`, `\exp`, `\cref`, and `\eqref`
  consistently with the book conventions.

The earlier scalar exact-live receipt and the earlier normalized frozen
packet receipt remain preserved as historical stages.  This receipt is the
controlling byte-identity gate for the current strengthened theorem and
proof.
