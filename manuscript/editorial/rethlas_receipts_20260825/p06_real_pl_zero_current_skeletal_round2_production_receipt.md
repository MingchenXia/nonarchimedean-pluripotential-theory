# P06.2 real-PL zero-current converse: production Rethlas receipt

**Receipt date:** 25 August 2026 (Asia/Shanghai)
**Status:** **VERIFIED FROZEN REAL-PL PROPOSITION; NOT YET INTEGRATED**
**Verifier:** production Rethlas at `127.0.0.1:8091`
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`

The exact skeletal-current proposition and proof returned
`verification_status = final` and `verdict = correct`.  One synthetic proof
item was checked, with zero failed or blocked items, zero critical errors,
zero gaps, and no request for expanded proofs.

This receipt preserves, but does not erase, production round 1
`20260825T031243Z_1603e0a83037`, which returned `final/wrong`.  Round 1
incorrectly extended a boundary-separation construction from
full-dimensional Abhyankar points to the support of an arbitrary test form.
The accepted round-2 proof does not use that step.

## Run identity

- Run: `20260825T032958Z_3a27f19be958`.
- Proof item: `pi_f2130d5e31ef3d5934410c10`.
- Item title: `theorem synthetic:main`.
- Started: `2026-08-25T03:29:58.219005+00:00`.
- Item elapsed time: `618.241` seconds.
- Reported token count: `177`.
- Adaptive round: `0`; no expanded proof was requested.
- Verifier process: completed with return code `0`; output validated.
- Process-guard command SHA-256:
  `25fc2c569160c48514eb51202fa2870127e13d557fe5f11ba014e63997d85bdf`.
- Both parent and child process guards have state `completed`.

## Exact submitted bytes

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `../rethlas_packets_20260825/p06_real_pl_zero_current_skeletal_round2_statement_exact_20260825.tex` | 1937 | 33 | `3a27f19be9582f1082a17cbce819042f68cf5f37c8f2702fbcded89e7a616ab7` |
| `../rethlas_packets_20260825/p06_real_pl_zero_current_skeletal_round2_proof_exact_20260825.tex` | 9427 | 184 | `c37af7bb8acbc388056f90ca97009f80b30cbea36ebaf10927400ef29364cbda` |
| `../rethlas_packets_20260825/p06_real_pl_zero_current_skeletal_round2_request_20260825.json` | 11837 | 5 | `ab90e06b9159ca8b835b176a8c18268b9f38cd0d1df271c205a61b0d3645e851` |

Decoding the request with `jq -j '.statement'` and `jq -j '.proof'`
reproduced the frozen statement and proof byte for byte; both `cmp` checks
returned zero.

## Verified mathematical scope

Let `K` be complete and nontrivially valued, and let `X` be good,
separated, boundaryless, strict, and pure of dimension at least one.  If
`h` is real PL and its CLD current satisfies

```text
d'd''[h] = 0,
```

then `h` is GJR harmonic; equivalently, every residual class `L_h(x)` is
numerically trivial.  By the Gubler--Rabinoff real-PL comparison theorem,
`h` is classically pluriharmonic.

The accepted proof:

- writes `h` locally as a sum of integral PL functions with
  Q-linearly independent real coefficients;
- regards their curvature currents as CLD skeletal currents;
- refines the calibrated analytic skeleton simultaneously by the PL tuple
  and by the tropical chart of each arbitrary compactly supported test
  form;
- uses integral, or equivalently rational in primitive lattice
  normalization, codimension-one calibrations to separate the coefficients
  cell by cell;
- applies CLD Theorem 18.8.4 with `d=1` to the resulting integral summands;
  and
- applies GJR residue harmonicity and GR Theorem 4.3.

The item-level mathematical summary is:

> The context is complete and untruncated, and the current item matches the
> expected id. Every deduction and external citation was checked. The local
> Q-linearly independent integral-PL decomposition is supported by
> Gubler--Jell--Rabinoff; the CLD skeletal-current construction yields
> coefficients in a common rational lattice (indeed integral after
> primitive normalization), so Q-linear independence separates the summand
> currents. Common refinements with arbitrary test-form charts establish
> the full current identities. CLD Theorem 18.8.4 then gives numerical
> triviality of each residual class, and the cited definitions and
> Gubler--Rabinoff Theorem 4.3 give harmonicity and classical
> pluriharmonicity. No erroneous boundary-separation or
> arbitrary-continuous-function claim is used.

## Returned digests and preserved artifacts

- Proof digest:
  `c37af7bb8acbc388056f90ca97009f80b30cbea36ebaf10927400ef29364cbda`.
- Aggregate context digest:
  `95c28bea5c3fc57956f232fbee91aaedee1aff920b2636fbdaf3dcde2c6008c3`.
- Adaptive context digest:
  `6125a96b500f9f2cb6de5c654ed3136d7acbf324c50881a2c1bb322caa1721dd`.
- Item context digest:
  `a43de08e8cb4abf1b97d2bc8b6bf525f0b6190735f43ae9686ef38edd06002d5`.

| Preserved artifact | SHA-256 |
|---|---|
| `p06_real_pl_zero_current_skeletal_round2_api_response_20260825.json` | `f1678f496645d5d12419d29fd3cdf66d71609b2e5a8d19da93ead1cc4482829c` |
| `p06_real_pl_zero_current_skeletal_round2_run_manifest_20260825.json` | `294166c3066a95292c39fe3bc4e03115b684aa666ad04bf663e2d555c06206f8` |
| `p06_real_pl_zero_current_skeletal_round2_run_verification_20260825.json` | `28829ed6b0d8cd412157c4deff189f049dbc4fb61fb3907284a431020e151dc2` |
| `p06_real_pl_zero_current_skeletal_round2_item_verification_20260825.json` | `7a263e73a5fec304241226119b85d240e6f4778305bf6c18664886c25c1a8cfe` |
| `p06_real_pl_zero_current_skeletal_round2_item_log_20260825.md` | `427329f2d6ed98be0c26bf83721fd74d751d67cb5408ba6f356e17fd70a5ab4e` |
| `p06_real_pl_zero_current_skeletal_round2_process_guard_20260825.json` | `5e8cb3f00e88accae46ea65ec2f69a32ea892da977213032924c40bd18579ea5` |
| `p06_real_pl_zero_current_skeletal_round2_process_child_guard_20260825.json` | `322c5d297fc886a71ab26c65c5b2a40db1397ad5998d7d0e1d3bd35537aeb32a` |

## Release firewall

- Do not edit the frozen statement, proof, request, response, logs, guards,
  or this receipt.  Any byte change creates a new proof object.
- Do not use the round-1 boundary-separation argument.
- Do not drop goodness, strictness, separation, boundarylessness, pure
  dimensionality, or nontriviality of the valuation without a separate
  proof.
- Do not infer the result for arbitrary continuous functions.  That scope
  remains open outside the published curve comparison cases.
- Do not infer positivity of a real-PL current implies semipositivity; the
  proof uses equality to zero and Q-linear coefficient separation.
- No novelty or priority claim is made.
