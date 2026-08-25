# P06.3 literal harmonic approximation: guarded production receipt

Date: 25 August 2026 (Asia/Shanghai)

Status: verified frozen proposition and proof; live integration intentionally
deferred until the root coordinator clears the concurrent P11 integration.

## Verdict

- Guarded run: `20260825T045723Z_331edb5358e4`.
- Checked item: `pi_b86fec7e60fb3e22e3bafaae`.
- Model / scrutiny: `gpt-5.6-sol` / `xhigh`.
- Verification status / verdict: `final/correct`.
- Critical errors and gaps: zero.
- Adaptive round: zero; no expanded proof requested.
- Item elapsed time: `531.589` seconds.
- Reported token count: `143`.
- Proof digest:
  `6f2bc79ba25bf254d2f0ec20f6459bf593b0ad376ef9d40a750f0b7ea709fd6f`.
- Aggregate context digest:
  `ae43c0a4d465f6c143fc5a8922229960e6710087f6406615d4a428df628cad8c`.
- Adaptive context digest:
  `03f4160db7697d2ad1f63ef85f3b1b807589df821d1c292bd0d8ebcd7a0c94f0`.
- Item context digest:
  `7ff992a2896c04afa485e1ed7177ccbabff6a57536251e54303d40bad5020669`.
- Process-guard command SHA-256:
  `193701ea01872438c0a9df6761f0a4ee3ba1f1c1bde2f90445f610f07f15eed8`.
- Parent and child guards both ended in state `completed`; wrapper return
  code was zero and the model output was validated.

## Exact verified scope

There exist a complete algebraically closed nontrivially valued field, a
smooth proper connected Berkovich curve, a type-2 point, a relatively
compact connected open three-arm neighbourhood, and an integral PL harmonic
function `h` such that `h` is weakly smooth with zero weakly smooth
`d'd''`, but `h` is not a locally uniform limit of ordinary CLD-smooth
harmonic functions.  Consequently it is not a decreasing pointwise limit
of such functions.

The proof uses the GJR Section 17 theta-curve example.  The residual elliptic
curve carries a nonzero class `[z]-[x]` in `Pic^0(E) tensor R`.  On a fixed
inner semistable three-arm star, model-independence of Thuillier's harmonic
space forces every harmonic function to factor through that skeleton, so
its residual slope divisor has fixed three-point support.  Ordinary
CLD-smooth harmonic germs have zero residual Picard class.  Their divisors
therefore lie in a closed subspace of the finite-dimensional three-point
divisor space.  Uniform convergence controls the three arm slopes by
endpoint values, contradicting the nonzero target class.  Net-Dini turns a
decreasing pointwise net into uniform convergence on the compact inner star.

This theorem refutes only the literal request for ordinary CLD-smooth
**harmonic** approximants.  It does not refute decreasing approximation by
ordinary CLD-smooth **psh** functions.  Positive curvature invalidates the
fixed-arm slope convergence, and the unrestricted psh regularization problem
left open by Wanner Remark 5.5 remains open.  P06.3 must therefore be
re-scoped, not deleted, and the authoritative totals of `18` formal problem
environments and `59` active atoms must not change.

## Frozen input objects

| Artifact | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| statement | 1284 | 27 | `331edb5358e4d1e9dd9ec543c4c8183b09838d43f515bc3d4d0ec6a837b8f195` |
| source-aware proof | 10781 | 219 | `6f2bc79ba25bf254d2f0ec20f6459bf593b0ad376ef9d40a750f0b7ea709fd6f` |
| round-2 request | 12590 | 5 | `1b1f143be87f35d902a96f3ef7838f9ec6de36f83be9629a8f4b09d388f96ea0` |
| solver dossier | -- | -- | `ee0064d76d9f20e4fc79278eccf17bfcfc554affdbb89bb7c5c3b35d16505fda` |
| hostile audit | -- | -- | `8553e31e4edea730c4cfdc6bb1bdc757a58fc409befab3f4c0de479c6e1b56ab` |
| integration plan | -- | -- | `457c70784d7808aa9843188189ba6faf0d30802cdf886f9d1b27f2a60ee5449b` |

Decoding `.statement` and `.proof` from the round-2 request reproduced the
two frozen TeX files byte for byte; both `cmp` checks returned zero.

## Preserved run artifacts

All artifacts are frozen under
`p06_cld_smooth_harmonic_regularization_round2_run_20260825/`.

| Artifact | SHA-256 |
|---|---|
| aggregate manifest | `4de68348076bb6639e4d8a5b8f1f911fe4c0068a4bd499cfa6f6930048c2646d` |
| aggregate verification | `509feb76066c6ffcecd2736cea3da4b955a5627c8955328b55d62a30ac17a661` |
| item verification | `cef5ac2e3081e00631d2240c5bbce3b06d983b32ab25e441254e5f2507ed2975` |
| item log | `6780cfce7426ee9da80b6db1063b4c60a3432830da2d56ac6ec4c8c34484725d` |
| process guard | `cb54fcbf7e5a8c9b03cde070e0b8e04eb52a9e180ec4c4ff95c90273240adc31` |
| child-process guard | `85bb5da28944953c190c2b777326df67cd23d5a0fc21b819c3bbdc24ff43af3f` |

The minimal TeX compilation succeeded with no error or unresolved reference.
Its PDF SHA-256 is
`3ca416a8c697dde97737740b55db9976cc6003f48cdaf5c0b2c7b4ede926a0be`;
the log SHA-256 is
`1447484b46a7f119866bb0dda0ca0a35a12e9bda6f363dc30c3bd1ec596049d9`.
The three overfull-box warnings are caused by unbreakable packet-only hashes
and the packet-only problem identifier.

## Preserved rejection history

Round 1, `20260825T044433Z_331edb5358e4`, item
`pi_e275a3a501893b2701482bb7`, returned `final/wrong`, with one critical
source-location error and zero gaps.  It rejected the pinpoint to CLD 3.1.3
and requested CLD 3.1.7 and 3.4.7 plus Wanner Definitions 3.9--3.12.  Its
proof digest was
`a5eb47b2763172fb578a84e67607bc38791792a4d2ccf6c148d17f26ac1a73d6`.
The corrected round changed only that source line.  The rejection receipt has
SHA-256
`e5e2bfc138a465247af6bc0e4a93e9c5cc7f4424c4a89fba6ce71ebc2279ea96`,
and all raw round-1 guards and responses remain preserved.

## Release firewall

- Do not modify the frozen round-2 statement, proof, request, run artifacts,
  or this receipt.  A byte change creates a new proof object.
- Do not claim a counterexample to ordinary CLD-smooth psh approximation.
- Do not infer the result for arbitrary continuous zero-current functions or
  higher-dimensional analytic spaces.
- Do not delete P06.3 or change the authoritative `18/59` problem/atom totals;
  re-scope it to the genuine psh question.
- Do not edit live chapters or ledgers until the root coordinator explicitly
  clears the concurrent P11 integration.
- Give any live proposition no conventional name and make no novelty or
  priority claim.
