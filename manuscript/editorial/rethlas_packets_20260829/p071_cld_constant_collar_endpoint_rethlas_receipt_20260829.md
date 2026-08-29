# Production Rethlas receipt: P07.1 finite constant-collar endpoint

Date: 29 August 2026

Status: **PASS** for the exact staging statement and proof identified below.
This receipt verifies the isolated finite-endpoint result.  It does not by
itself retire the unrestricted P07.1 atom, and it is not evidence for an
infinite star, a higher-dimensional tropical space, or a nonambient smooth
structure.

## Exact submitted bytes

- Statement:
  `69f04be69f70be0abfdb720fa6aceaad799240421046d14333cfd542e2e56498`
- Proof:
  `5e7d96e8badf030b64d063b26fb353aa4be097438ae267cdd72911907c2a5c7c`
- Archived request:
  `aa41133b41bf70cd5dd852d0f6a135d761c788ace396b4ff0a9f2e53d6f7e6d1`

Extracting `.statement` and `.proof` from the archived request without
adding bytes reproduces the statement and proof hashes exactly.

## Verifier identity and verdict

- Service run: `20260829T002250Z_69f04be69f70`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Started at: `2026-08-29T00:22:50.739392+00:00`
- Verification deadline: `2026-08-29T01:17:50.577603+00:00`
- HTTP status: `200`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`

The archived verifier log records the exact model and reasoning
configuration.  The verifier validated the strict output schema before
writing the final report.

## Verification records

- Sequential statement records: `10`; all passed.
- Primary-source reference records: `6`; all passed.
- Failed-check records: `0`.
- Primary source checked: Chambert--Loir--Ducros,
  arXiv:1204.6277v2.

Artifact hashes:

- Archived response:
  `0a92f306f070402e79c1bfa18a182c3a2d12e4dc61cb8da56c9a74bd2146f621`
- Archived safe headers:
  `03637da2cc7a40cef266305ab4225e07306073642240bc5a69a4fad09a3eb393`
- Archived service `verification.json`:
  `330e43d242bb0be971e8e1c71a15cdf154464b913a49287ed0396cd4c43d0f66`
- Archived verifier log:
  `8684ad12b7d3274cea93708bef43c37a10f8868355057899f03da74107e7ffc8`
- Statement checks:
  `6b9fecb43f0bfb1490812b9eb719f875a7ada024266d2a6bae05bff9f4bb0fb4`
- Reference checks:
  `e60ac17cafc9069bd60140fe80e61c2d66a742f4b033cf4794db62d2ef4d39b2`
- Failed checks:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Verification-report memory:
  `7e6cdfefce89c5fbb0e7ef46cba1bcb91efcb4f0bfc3ed7f03f175ed35b9b9ba`
- Event memory:
  `61f34c90e845002a1bfcf6c140c63cc80650b7e24185c149456d0416bba5a1c9`

The submission helper displayed `checked_items: 0` because the service
response intentionally has no top-level `checked_item_ids` field.  The
authoritative service memory contains the ten statement records and six
reference records counted above.

## Mathematical scope confirmed

On a finite half-interval with the constant-collar smooth structure, the
generated CLD psh sheaf equals the sheaf of intervalwise extended-real convex
functions satisfying the endpoint-minimum condition, and the hierarchy
collapses at its first decreasing-limit stage.  The verifier also confirmed
the fixed-domain decreasing regularization, the uniform finite-trace case,
the identically `-infinity` alternative, and the exact finite-endpoint use of
CLD Example 6.7.2.

The verification expressly excludes the infinite endpoint of the CLD
interval, including the open-unit-disc realization.  That case is governed
by a separate statement and a separate production run.
