# Production verification receipt

Date: 30 August 2026

## Verdict

The source-aware production request returned `verdict: correct`, with zero
critical errors and zero gaps.  The verifier summary confirms the exact
product affine G-tropical scope, the zero-dimensional Stone parameter
structure, closure of the metrizable-factor comparison sheaf, and the
fixed-neighbourhood decreasing smooth-convex re-selection, including the
polar and `d=0` cases.

The local production service was launched with `CODEX_MODEL=gpt-5.6-sol`
and `CODEX_REASONING_EFFORT=xhigh`.  The direct HTTP endpoint assigned no
run or item identifier, so the exact request, response, headers, and hashes
below are the controlling receipt.

## Frozen principal bytes

| role | file | SHA-256 |
|---|---|---|
| statement | `statement.tex` | `dfd8c7cc9d6d26f50260707975ff62d4f292627f084400bcd37b32253c876cdc` |
| proof | `proof.tex` | `9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6` |

The decoded request statement has the same SHA-256 as `statement.tex`.
The decoded request proof, after prepending the source matrix, hostile
audit, and independent exact-byte audit in the documented dependency
order, has SHA-256
`628dc40e22ce5b3f30e2f2da57b008d77cd444910f48837873cda55111eadbef`.
The frozen `proof.tex` occurs as the final exact principal block in that
materialized proof.

## Production archive

| file | SHA-256 |
|---|---|
| `production_run_20260830/request.json` | `ac70562c588dbf8f22925086bc85dc327585f026809563a71c79feb29787ca23` |
| `production_run_20260830/response.json` | `ef9be00d4ed1462f11068a2b99a2c7fbe366af2b3bd180850b6763db541c3d6a` |
| `production_run_20260830/headers.json` | `f43595e1f578464a6fe7270d977bcee667b0d78d836e76633ce6e8b31321c5f7` |

The HTTP status was 200.  The response contains no repair hint, critical
error, or unresolved gap.

## Scope consequence

The theorem is authorized for live-book integration.  It does not retire
P07.1: affine directions in the parameter factor, general polyhedral face
gluing, and arbitrary affine G-tropical local models remain outside its
scope.  It does remove nonmetrizability of a locally constant Stone
parameter and arbitrary Euclidean dimension as obstructions in the exact
product structure of the statement.
