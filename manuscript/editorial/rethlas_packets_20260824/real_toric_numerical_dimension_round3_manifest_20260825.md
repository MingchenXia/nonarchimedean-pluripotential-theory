# Manifest: real toric numerical dimension, production round 3

**Snapshot date:** 25 August 2026 (Asia/Shanghai)
**Packet status:** frozen exact statement/proof/request passed production
Rethlas with `final/correct`, zero critical errors, and zero gaps
**Live integration status:** not yet integrated

| File | Role | Bytes | Lines | SHA-256 |
|---|---|---:|---:|---|
| `real_toric_numerical_dimension_round3_statement_exact_20260825.tex` | exact submitted statement | 1398 | 33 | `99edb45c54cb8bae89f5f5dc34abc718ca965a2ac7f1d7bef1693ab4dab372fa` |
| `real_toric_numerical_dimension_round3_source_aware_proof_exact_20260825.tex` | exact submitted full source-aware proof | 15125 | 339 | `e2e16296fa3420e6a40739016a6dccabb9628e17ea2c6ec47ec890e9dfaebfad` |
| `real_toric_numerical_dimension_round3_source_aware_request_20260825.json` | exact submitted request | 17650 | 5 | `799eb4aaee0db33d97e208fa9859cdd099ffa4932d3f356e98ac1390f37de46d` |

The statement and proof freezes are byte-identical to
`real_toric_numerical_dimension_statement_exact.tex` and
`real_toric_numerical_dimension_source_aware_proof_exact.tex`. Decoding the
request with `jq -j` reproduces the frozen statement and proof byte for byte;
both `cmp` checks returned zero.

## Controlling result

- Run: `20260825T011636Z_99edb45c54cb`.
- Item: `pi_9bb081dd3b5d36a64cbc59af`.
- Model / scrutiny: `gpt-5.6-sol` / `xhigh`.
- Verdict: `final/correct`.
- Critical errors / gaps: `0 / 0`.
- Proof digest:
  `e2e16296fa3420e6a40739016a6dccabb9628e17ea2c6ec47ec890e9dfaebfad`.
- Aggregate context digest:
  `403e74073fa5632def83ed0953304dd8dc02d9f192f4996ef353d073f8fb66a9`.
- Adaptive context digest:
  `90b45288aceb61a31858534ea63407bc26d92faf7d2c8254e6267d43b4da055a`.
- Item context digest:
  `120379ca2b11d73484acc922076280676bd5e381e4baee3f9f0649e2f8f52162`.
- Controlling receipt:
  `../rethlas_receipts_20260825/real_toric_numerical_dimension_round3_production_receipt.md`.
- Exact API response:
  `../rethlas_receipts_20260825/real_toric_numerical_dimension_round3_api_response_20260825.json`,
  SHA-256
  `ad5250ac8d2b41fc62d1f16b815631c9b6bd4bd74f16ca9e159eff375d311278`.

## Historical artifacts

The round-1 `final/wrong` response and the round-2 timeout artifacts remain
frozen alongside this manifest. Round 1 identified and round 3 repairs the
factor-two multiplier-ideal convention mismatch. Round 2 supplied no
mathematical verdict. They are diagnostic history and do not control the
theorem.

## Scope lock

The verified result is current-level, not class-level; it uses the closed
Newton body
\(\overline{\operatorname{dom}F_T^*}\); it covers pseudoeffective real toric
classes, with irrational real divisor classes as the genuinely new scope;
and it declares both degree-zero products equal to \(1\). These clauses may
not be dropped during live integration.
