# P14.3 V3 production verification receipt

## Result

The frozen V3 source-bound conditional bridge was submitted to the isolated
model-backed production verifier on 9 September 2026.  The service-authored
run log records `gpt-5.6-sol` at `xhigh`; the HTTP receipt is final
`correct` for its single item, with zero critical errors and zero gaps.

This is evidence for the precise conditional bridge in V3.  It does not
discharge P14.2 upper semicontinuity, establish the finite-energy
divisorial-normalization premise, prove general MP positivity, or retire
P14.3.

| Field | Value |
| --- | --- |
| Item | `pi_75b42272e15105bb6be0525c` |
| HTTP status | `200` |
| Verification status | `final` |
| Verdict | `correct` |
| Critical errors / gaps | `0 / 0` |
| Model / effort | `gpt-5.6-sol` / `xhigh` |
| Service run start | `2026-09-09T06:19:03.160888+00:00` |

## Exact archived bytes

| Artifact | SHA-256 |
| --- | --- |
| `STATEMENT_V3.md` | `6f2be66bab98808476c7c5cefa3a101cb4ef902f83a3e2738ca15b7feb61bd96` |
| `PROOF_V3.md` | `3c93f9e96d040465b3e54673df49114617e9a889429fffb50e52ecb5c798ab46` |
| `VERIFICATION_RUN_SOL_PRODUCTION_20260909/request.json` | `6e627abf22ec6619b78e953f9f88e13f12d370846554521c0de401d072db4207` |
| `VERIFICATION_RUN_SOL_PRODUCTION_20260909/response.json` | `7aab0bd0207aa6f18d86ceb125f4fae69f444d4290ac1fb2556051632db62d11` |
| `VERIFICATION_RUN_SOL_PRODUCTION_20260909/headers.json` | `9f0475220d1d483763ba320bebc42661b542c60e3385937e04eb6284ea91c6a4` |

`audit_strict_rethlas_receipt.py` accepts these exact archived bytes against
the production verifier source, including item coverage and the adaptive
context digest.  That audit verifies the receipt protocol and byte identity;
it does not enlarge the mathematical scope of V3.

## Boundary retained

V3 proves the domination-preserving rational-divisorial approximation and
the resulting all-point comparison only under its named P14.2
upper-semicontinuity and Chapter 71 finite-energy divisorial-normalization
premises.  The appended MP24 and DXZ23 extracts identify the cited inputs,
but do not supply general MP positivity at arbitrary nondivisorial points.
Those exclusions keep P14.3 active.
