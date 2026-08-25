# P07 CLD hierarchy: toric and finite-curve production receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)  
**Status:** **VERIFIED FROZEN PACKET; INTEGRATED WITH SCOPE FIREWALL**  
**Verifier:** isolated production Rethlas at `127.0.0.1:8111`  
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The exact source-aware packet returned `verification_status = final` and
`verdict = correct`.  Rethlas checked one synthetic proof item, with zero
critical errors, zero gaps, and no request for expanded proofs.  This
receipt controls only the exact bytes listed below.  No live chapter was
edited during the verification run.  After the pass was returned, the
verified result was integrated into Chapter 16 as recorded below; the
frozen packet and all returned artifacts remain unchanged.

## Controlling run

- Run: `20260825T024707Z_d1b8d7eaf79e`.
- Item: `pi_ccfb83de7a7be82ef602cd72`.
- Item title: `theorem synthetic:main`.
- Started: `2026-08-25T02:47:07.544257+00:00`.
- Elapsed time: `314.967` seconds.
- Reported token count: `145`.
- Adaptive round: `0`; no expanded proof was requested.
- Codex process: return code `0`, status `completed`, output `validated`.
- Supervisor command SHA-256:
  `f43198cc400c2d201e80439d139398be1406c4de2fd6c25c45f0ae1771ccb367`.
- Both process guards have state `completed`.

## Exact submitted bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p07_cld_hierarchy_toric_curve_statement_exact.tex` | 1148 | 29 | `d1b8d7eaf79e155ecf7b347e4fcc1717c72d5a8090e346b2cb2fc9c9a0996e63` |
| `../rethlas_packets_20260825/p07_cld_hierarchy_toric_curve_exact.tex` | 15505 | 352 | `316a774fbb4eda54150b63cae0c9f23a1edab17a75b89beeee6d56d402f8c4a0` |
| `../rethlas_packets_20260825/p07_cld_hierarchy_toric_curve_request_exact_20260825.json` | 17512 | 5 | `9490d443d40011c15fbd146e3b3b740876006752f75a5698fd1972da1b7940dd` |

Decoding the JSON fields with `jq -j '.statement'` and `jq -j '.proof'`
reproduces the two TeX files byte for byte; both `cmp` checks returned zero.

## Returned digests and preserved artifacts

- Proof digest:
  `316a774fbb4eda54150b63cae0c9f23a1edab17a75b89beeee6d56d402f8c4a0`.
- Aggregate context digest:
  `af11336981b7d302ae5eb6f5db89f002af58f1a3099576c7f41e887ac1c591f4`.
- Adaptive context digest:
  `81e6d2876ebcb649e3525fc3742e547d3546e9bc0415d55d5a3ed9e92ad9b5b9`.
- Item context digest:
  `e25f9d8e5d493bfd350ca4f3b6a446082c5e0d5b569b2090b2d98668772fb119`.

| Preserved artifact | SHA-256 |
|---|---|
| `p07_cld_hierarchy_toric_curve_round2_api_response_20260825.json` | `845e300dbcd6921129e5353a2f778e90ed59e781eb0c82fb65ee958386b1584d` |
| `p07_cld_hierarchy_toric_curve_round2_run_manifest_20260825.json` | `2180fdd2e4314744d75e5cb128fce00f7c50af9f40a48bf36618a2847e6920cb` |
| `p07_cld_hierarchy_toric_curve_round2_run_verification_20260825.json` | `42855b64b598eef4ef78199f64e7c23e34c5ce7be43cbceced6eacedef09b698` |
| `p07_cld_hierarchy_toric_curve_round2_item_verification_20260825.json` | `d8d49926fc4a68a3e6f8564b5ac3cb6068902610a466e3365b59bdd5ca1882bb` |
| `p07_cld_hierarchy_toric_curve_round2_item_log_20260825.md` | `afd1bd521dd1e1ade32820089d5bf3449c124e5e6c024957bee2bd52c74a6be6` |
| `p07_cld_hierarchy_toric_curve_round2_process_guard_20260825.json` | `faf0ec826b79e9fafe8a6e74273fde86b53c8a280525fa91ab605e9a96c5c59e` |
| `p07_cld_hierarchy_toric_curve_round2_process_child_guard_20260825.json` | `ac42843d632e2f5ed93cf8c61c141ecd6475a06dcf6186cffa52ded7417e8385` |

## Production implementation identity

Port `8107` was already occupied, so an isolated service was started on
`8111` from the hydrated audited tree
`/Users/mingchen/Documents/ChatGPT/Yethlas/Rethlas_arxiv191209719_20260824`
with runtime
`runtime/rethlas-arxiv191209719-venv-20260824`.  Git commit:
`60ca1e612f9779466621094efccb474fb4d22432`.

Controlling implementation hashes were:

- `api/server.py`:
  `88692d76aba48cdace485bf4dabbba721d9a7f6e73b4169d1add42ec5fc182ef`;
- `api/proof_context.py`:
  `e0827870ee974f40a74328e59c9d61461623d611cbaf67a13e3c6057fd157279`;
- `api/contracts.py`:
  `0adabc3ac87da4a7a44f1d9e9f96f44471c31c11fec815d34ccd6cbca42c86f5`;
- `api/process_supervisor.py`:
  `17313bce42e099b41eea64b812a18d158f35e0ed927f5094e2abc62698d818b0`;
- `AGENTS.md`:
  `a2e3a36733c644514fe8f1eea8587d26d7ba06e37dece206ac1e60c71eab2067`;
- output schema:
  `d0a94d41d06dc286fad022f72d430cc9b2052c8b478bb1c07ecfad202b61995f`.

The isolated service was shut down cleanly after preservation of the run.

## Exact mathematical scope

The verified packet proves two statements.

1. On every tropical toric partial compactification `N_Sigma` with its
   standard Lagerberg smooth structure, on every open subset,
   `Psh_CLD,1 = Psh_CLD = Psh_tor`.  This is a source synthesis from BGJKK
   Theorem 3.3.4 and the two sheaf minimality/stability directions.
2. On a one-dimensional boundaryless affine tropical space locally modeled,
   with calibration and ambient-induced smooth structure, on a finite
   balanced one-dimensional polyhedral complex, `Psh_X,1 = Psh_X`.
   First-stage membership is proved on one fixed open neighbourhood.

The curve proof includes the following load-bearing points in the verified
bytes: explicit interior-edge regularization; sheaf locality of the
junction-Jensen inequalities by scaling and convex propagation; treatment
of `-infinity`; a full Farkas condition for all nonnegative ray relations;
an ambient support covector; chordal approximation; a truncated regularized
maximum that is exactly one ambient affine function near the vertex; and
uniform-to-monotone conversion on a fixed open star.

This does **not** settle unrestricted P07.1.  Higher-dimensional arbitrary
balanced polyhedral spaces, tropical boundary points, and infinite-valence
CLD stars remain outside the theorem.  The higher-dimensional obstruction is
the missing face-compatible polyhedral and CLD-smooth regularization in that
generality.

## Live integration after PASS

The result is integrated only in
`manuscript/parts/part2/ch16_bedford_taylor.tex`, immediately after
`rem:ch16-collapse-euclidean` and before `sec:ch16-composition`, under the
new subsection label `sec:ch16-collapse-positive-cases`.  The principal
live labels are:

- `prop:ch16-collapse-tropical-toric`;
- `lem:ch16-farkas-ray-support`;
- `thm:ch16-collapse-finite-tropical-curves`;
- `ex:ch16-collapse-weighted-tripod`;
- `rem:ch16-collapse-scope-firewall`.

The live proof retains every load-bearing element of the exact passing
packet: explicit interior-edge smoothing on one fixed interval, sheaf
locality of the junction inequalities, the finite and identically
`-infinity` alternatives, all nonnegative ray relations, a common ambient
support covector, exact affine gluing by the truncated regularized maximum,
and uniform-to-decreasing conversion on one fixed star.  It additionally
spells out the elementary Farkas alternative by finite-dimensional
separation and gives a weighted-tripod illustration.  These additions do
not enlarge the verified theorem's scope.

All new live labels were unique at audit time, and targeted
`git diff --check` passed.  A full `latexmk` run parsed the integrated
Chapter 16 without a TeX error and proceeded through Chapter 68.  The run
then stopped at the unrelated undefined command `\an` in the concurrently
modified Chapter 69, so no whole-book success is claimed by this receipt.

## Primary-source clearance

- The local CLD v2 PDF, arXiv:1204.6277v2, has SHA-256
  `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
  Definitions 8.1.1 and 8.1.13 and Lemmas 8.1.2, 8.1.4, and 8.1.10 were
  checked in the extracted text.  The official record says v2 was revised
  25 July 2025.
- BGJKK, arXiv:2102.07392, Definition 3.1.2, Proposition 3.1.3, Theorems
  3.1.4 and 3.3.4 were checked at official arXiv full-text level.
- Botero--Mazzon--Pille-Schneider, arXiv:2603.08664v1, Definition 3.20,
  Theorem 6.4, Remark 6.6, and Proposition 6.13 were checked at official
  arXiv full-text level.  The arXiv record says submitted 9 March 2026; the
  displayed manuscript date is 24 August 2026.

## Verification history

Round 1 is intentionally retained.  Run
`20260825T022650Z_d1b8d7eaf79e`, item
`pi_fa5c5878187fdb2ee1a7f1b5`, checked proof SHA-256
`63d98be6f65dd00ebf56c0ce25e901140012ffa15f325f70e6a97bd8da3fdfb1`
and returned `final/wrong`, zero critical errors, and two gaps: the
interior-edge case was only called usual, and the sheaf locality of the
junction condition was only asserted.  The exact failed proof, statement,
request, response, manifests, log, and guards are preserved under the
`p07_cld_hierarchy_toric_curve_round1_gap_` prefix.  Round 2 repaired exactly
these two points and is the sole controlling pass.

## Release firewall

- Do not alter the frozen statement, proof, request, response, manifests,
  log, or guards.  Any byte change requires a new receipt.
- Do not erase the Round 1 rejection.
- Do not claim unrestricted CLD hierarchy collapse.
- Do not extend the curve theorem across tropical boundary or infinite
  stars without a separate proof.
- Live integration must preserve the verified hypotheses and the fixed-open-
  neighbourhood conclusion.  The first integration audit is recorded above;
  any later scope enlargement requires a new exact verification packet.
