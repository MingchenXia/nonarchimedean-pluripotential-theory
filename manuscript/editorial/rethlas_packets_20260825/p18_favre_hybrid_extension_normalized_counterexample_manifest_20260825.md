# P18.1 normalized hybrid-continuity counterexample: frozen packet manifest

**Freeze date:** 25 August 2026 (Asia/Shanghai)
**Live-chapter status at freeze:** not integrated
**Production verifier:** `127.0.0.1:8107`, `gpt-5.6-sol`, `xhigh`

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `p18_favre_hybrid_extension_normalized_counterexample_statement_exact_20260825.tex` | 2553 | 68 | `070e264c3ef1d1e6c436eb7215ee50e1801bfeab667159234e7d755bc69a52f8` |
| `p18_favre_hybrid_extension_normalized_counterexample_source_aware_proof_exact_20260825.tex` | 15292 | 416 | `0e9c8fdf755a714eccc2c3bc0215d8c43ad05c04ab664077205bfa552dd1ef90` |
| `p18_favre_hybrid_extension_normalized_counterexample_source_aware_request_20260825.json` | 19313 | 5 | `93a684c37e273851661762bb7af2827ad41cdbc512538136ba6dd2fe4b213b4f` |

The theorem copied from the proof is byte-identical to the statement file.
The decoded `statement` and `proof` request fields are byte-identical to the
two TeX files.  An isolated `pdflatex` syntax check completed successfully.
The request deadline is `2026-08-25T08:00:00+00:00`.

Production submission identity:

* run `20260825T035945Z_070e264c3ef1`;
* item `pi_db89dd432acabcf33a3f2272`;
* proof digest `0e9c8fdf755a714eccc2c3bc0215d8c43ad05c04ab664077205bfa552dd1ef90`;
* item context digest `a5bb9b0b7b001ac8164bb7fb824739e309b5fe1e8092f01c047ee8cb3ea7cc59`;
* process-guard command digest
  `b8a689aec63c23903d03952cf6267753fcbc9228a622452b52d5409ed9d9cf84`.

The run completed after 518.835 seconds with `verification_status = final`,
`verdict = correct`, zero critical errors, zero gaps, and no expanded-proof
request.  The returned proof digest is identical to the frozen proof digest.
The controlling receipt is
`../rethlas_receipts_20260825/p18_favre_hybrid_extension_normalized_counterexample_production_receipt.md`.

The verified result has been adapted into Chapter 66 and the normalized
residual has been removed from Chapter 72.  This manifest remains the record
of the pre-integration frozen bytes.

The adapted live statement, theorem-and-proof block, and request were then
frozen with respective SHA-256 digests
`d77f7f93aeb01c9b29d0ffa170ea5301811f685e2b95f6d54b4151a9a0aad6ff`,
`992a686618355605e4f889564c402f5b2c6ff18db70762daed2dbcf4d09fdbad`,
and
`19d16bbc6a657e921616e90e8652a1a420857c218b7083ab69bb7365272f69a2`.
Production run `20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`, returned final `correct`, zero critical
errors, and zero gaps.  It is the exact-current byte-identity gate recorded
in the separate live-integration receipt.

The original exact packet and the later exact-live packet must both remain
unchanged.
