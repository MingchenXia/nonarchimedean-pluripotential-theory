# P14.8 V7 production verification receipt

## Result

The frozen V7 conditional exact-text comparison was submitted to the isolated
model-backed production verifier on 9 September 2026.  The service-authored
run log records `gpt-5.6-sol` at `xhigh`; the HTTP receipt is final
`correct`, for its single item, with zero critical errors and zero gaps.

This is evidence for the precise conditional comparison in V7.  It is not an
independent proof of every cited result, an authentication of an arbitrary
working tree, or a retirement of P14.8.

| Field | Value |
| --- | --- |
| Item | `pi_c2863cf20cfa0c4bba834a16` |
| HTTP status | `200` |
| Verification status | `final` |
| Verdict | `correct` |
| Critical errors / gaps | `0 / 0` |
| Model / effort | `gpt-5.6-sol` / `xhigh` |
| Service run start | `2026-09-09T05:59:20.210552+00:00` |

## Exact archived bytes

| Artifact | SHA-256 |
| --- | --- |
| `AUDIT_STATEMENT.md` | `c5988b934da459fec971c1708cb713e8a2d5ef196067edc6c930578db9c8a13e` |
| `AUDIT_PROOF_CONTEXT.md` | `070f7bfe1b17a716313ee65cd0b7310fbcef8fc5e78452ed6bfc917b0c582cc4` |
| `VERIFICATION_RUN_SOL_PRODUCTION_20260909/request.json` | `01147c3784ebad480426195d5e746dcb5c9cf3e6f996091aacb7d6b0c00e0c5b` |
| `VERIFICATION_RUN_SOL_PRODUCTION_20260909/response.json` | `291eba73c05df24c1a2049557418f0615e2a74adc91e86d37c849a115f428c68` |
| `VERIFICATION_RUN_SOL_PRODUCTION_20260909/headers.json` | `49b912ec95dfbd2a71ab209cba3707783b7ae8d2ded4bf5f86d577a620048dc8` |

`audit_strict_rethlas_receipt.py` accepts these exact archived bytes against
the production verifier source, including item coverage and the adaptive
context digest.  `check_packet.py` separately validates the V7 release pin
and its extracted source ranges.  The two checks have different scopes and
are both required for this receipt's stated provenance.

## Boundary retained

V7 is pinned to commit `ff333ee24648faa9ae23cf8d87a4bea1ec62e961` and
compares its frozen V6 target only with the listed Chapter 51 construction
and the then-live Chapter 72/inventory boundary.  It neither realizes
arbitrary formal ideal data, proves an all-semivaluation formula, supplies a
new zero-mass interval for the DXZ filtration, nor reconstructs a raw
representative or its raw mass.  Those exclusions keep P14.8 active.
