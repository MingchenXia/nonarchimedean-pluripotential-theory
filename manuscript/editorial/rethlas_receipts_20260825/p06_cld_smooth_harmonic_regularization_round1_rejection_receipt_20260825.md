# P06.3 literal harmonic approximation: round-1 rejection receipt

Date: 25 August 2026 (Asia/Shanghai)

Status: preserved production rejection; not a mathematical rejection of the
closure argument and not authority for live integration.

## Run identity and verdict

- Run: `20260825T044433Z_331edb5358e4`.
- Item: `pi_e275a3a501893b2701482bb7`.
- Model / scrutiny: `gpt-5.6-sol` / `xhigh`.
- Verdict: `final/wrong`.
- Critical errors: one; gaps: zero.
- Statement SHA-256:
  `331edb5358e4d1e9dd9ec543c4c8183b09838d43f515bc3d4d0ec6a837b8f195`.
- Proof SHA-256:
  `a5eb47b2763172fb578a84e67607bc38791792a4d2ccf6c148d17f26ac1a73d6`.
- Aggregate context digest:
  `2cd744eff178fac179a2e8dba9624461fac7aeefc732c63eb9f34bd9f8eaa774`.
- Adaptive context digest:
  `f607b210ff4fd1d8a87db0fac332c078978a91144309c1239f51982219a3226d`.
- Parent and child process guards both ended in state `completed`, and the
  wrapper return code was zero.

## Exact rejection

The verifier found no gap in the finite-support/Picard-closure proof.  It
rejected the packet because source-scope item 1 gave the wrong exact CLD
pinpoint: arXiv:1204.6277v2, Section 3.1.3 defines paralinéaire functions,
not smooth `(0,0)`-forms and their local pullback description.  It requested
CLD Sections 3.1.7 and 3.4.7 and Wanner Definitions 3.9--3.12 instead.

The source-aware proof must receive a new hash after this correction.  This
round and all six raw run artifacts are preserved in
`p06_cld_smooth_harmonic_regularization_round1_rejection_run_20260825/`.
No live text may cite this round as a successful verification.
