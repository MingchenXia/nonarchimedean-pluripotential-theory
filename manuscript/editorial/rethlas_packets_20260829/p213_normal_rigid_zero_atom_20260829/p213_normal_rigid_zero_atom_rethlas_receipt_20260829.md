# Production Rethlas receipt: P21.3 local normal rigid zero atom

Date: 29 August 2026

## Frozen mathematical bytes

- Statement SHA-256: `469024d04e8eb5e08900b9caea6480057398c743ca0b46076b524f2109cf80ac`
- Proof SHA-256: `661100a4b25e82297c5b2b2712775e9c9501c337d619a64280f2d49922a4bcc2`
- Independent exact-byte audit: `PASS`

## Production result

- Service evidence run: `20260829T060048Z_469024d04e8e`
- Checked item: `pi_0d4235a44db2b33950f8dd55`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`
- Failed or blocked items: `0`
- Adaptive round: `0`
- Codex return code: `0`
- Service output validation: `validated`

The response proof digest is exactly the frozen proof SHA-256.  The service
item report states that the local DVR reduction, finite-flat neighborhood,
radial cutoff estimate, positivity argument, limiting step, and cited source
uses are logically complete.

The direct HTTP wrapper reports `run_id: null`; no endpoint-assigned run
identifier is inferred.  The service-evidence directory name above is the
durable local archive identifier.

## Archived transport and service evidence

- `request.json`: `d22ccfd99fab0116b73d72a2252a182ac0f195ae884c21cd51f2c615276b0d61`
- `response.json`: `8fa1c1a18d8ea0ed64e989ebf4b79d49e9158392366398e1cf8007bfb944d78f`
- `headers.json`: `d2dfb0f8b5c45382a88a8be6f04c50b42adbfaf644a32deb8a56d0b04db53b40`
- `service_manifest.json`: `b705b7a80fde8baef59a7e6971d1850cd5b76dd30896bc6ff544994151aa2c26`
- `service_verification.json`: `0672c0258fcb45c1a8c75e854c1189e662048b256f87b9bf2574faac90730ed4`
- `service_item_log.md`: `078fdf3550cfa7a125afbdaabab8a9d3013c7548e060d18729fa458eb8c6d69c`
- `service_item_verification.json`: `1f95fa9a4b49da775d6cdd52b208b53db976d190c1dc4c3efdc612ba2b1cbcde`
- `service_process_guard.json`: `a7e3e66346b7e196558dde8f5ea25fe5b4e46b7dba7d166f0f9e79eb0ddb56a6`
- `service_process_child_guard.json`: `d1ed6ee2f94619ceff2c72d8427ce3aec6af41ed3199eb752bb648e05b7d1d09`

Two earlier attempts returned HTTP 429 because the first local service was
already processing another authorized verification.  They dispatched no
model for this packet and are retained in the two `busy_attempt` directories
as noncontrolling transport evidence.
