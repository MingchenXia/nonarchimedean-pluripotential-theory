# P14.8 v3 current-source validation

## Exact current source inputs

The current Chapter 51 excerpts have the following SHA-256 values:

| Role | Current lines | SHA-256 |
| --- | ---: | --- |
| `I`-envelope/projection | 3291--3339 | `54e4d6b864e81429549753d781a3e1c859cb5235a0d138b556196214611dbaa0` |
| Cantor/Green construction | 3758--3882 | `a8bc5f2e381328f4c9cd878b4c9b42af7de3486b8d459b6938598ed8af35f3ea` |
| all-mass family | 3951--3970 | `047d2f1f25d4c7d9d88b4a3f492d753fa530044170cd902fa667199aada41282` |

The first and third values are exactly the frozen v2 source-extract hashes.
Applying `V2_CANTOR_SOURCE_TO_V3.patch` with
`git apply --unidiff-zero` to the v2 Cantor extract produces the second hash
byte-for-byte.  Its content is exactly the current Chapter 51 range
3758--3882.

## Relation to the v3 proof

The source patch and the v3 proof patch make the same mathematical repair:
they set `ell_0=1`, use `ell_m=exp(-4^m)` only for `m>=1`, treat the first
ratio separately, and retain divergence from the `m>=1` summands.  The proof
postimage and its isolated build are independently recorded in
`../p148_cantor_index_repair_20260908/VALIDATION.md`.

## Boundary

This verification establishes exact source alignment for the stated current
spans.  It does not validate all remaining source dependencies, replace the
required independent review of v3, or authorize integration or retirement.
