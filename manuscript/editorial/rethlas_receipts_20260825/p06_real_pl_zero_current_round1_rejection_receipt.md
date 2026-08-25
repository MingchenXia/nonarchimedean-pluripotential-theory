# P06.2 real-PL zero-current converse: round-1 rejection receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)
**Status:** **PRESERVED `FINAL/WRONG` PROOF OBJECT; DO NOT INTEGRATE**
**Verifier:** production Rethlas at `127.0.0.1:8091`
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

## Run identity

- Run: `20260825T031243Z_1603e0a83037`.
- Item: `pi_ef4b8ab22822f1ccc0242d30`.
- Started: `2026-08-25T03:12:43.866473+00:00`.
- Elapsed: `741.776` seconds.
- Process return code: `0`; output validated.
- Verdict: `final/wrong`.
- Proof digest:
  `143681464cd8fc40882f4e2fbdc806d5555cdbcb544559ad6deebcb7cb5ba1f4`.
- Process-guard command digest:
  `7f6619e92e647cc7de73196ba44d70730339ea92ddef8350cdf33a15f9121983`.

## Exact rejected packet

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p06_real_pl_zero_current_statement_exact_20260825.tex` | 1818 | 31 | `1603e0a830373ef43ed844da1f8ac6b9397b215f9307758ea0e519860e077df7` |
| `../rethlas_packets_20260825/p06_real_pl_zero_current_source_aware_proof_exact_20260825.tex` | 10358 | 207 | `143681464cd8fc40882f4e2fbdc806d5555cdbcb544559ad6deebcb7cb5ba1f4` |
| `../rethlas_packets_20260825/p06_real_pl_zero_current_source_aware_request_20260825.json` | 12723 | 5 | `1525608851810769263f641b05110cf861591da438b3773a820f827f4dc13779` |

## Exact rejection

The proof claimed that the construction used in GJR Proposition 9.6
separates the entire compact support of an arbitrary `(n-1,n-1)` test form
from the analytic boundary.  The cited construction separates a chosen
full-dimensional Abhyankar point.  It does not apply to arbitrary support
points of tropical dimension `n-1`; in dimension one an arbitrary `(0,0)`
test function may include rigid points.  The resulting target form compactly
supported in `G(U) minus G(boundary U)` was therefore unjustified, so the
argument did not prove vanishing of the individual integral curvature
currents.

The complete machine-readable rejection and both completed process guards
are preserved under the prefix
`p06_real_pl_zero_current_round1_` in this directory.

## Historical relation to round 2

The later skeletal-current proof in run
`20260825T032958Z_3a27f19be958` returned `final/correct`.  That result does
not repair this proof object and does not license the rejected
boundary-separation step; it uses CLD skeletal-current calibrations instead.
