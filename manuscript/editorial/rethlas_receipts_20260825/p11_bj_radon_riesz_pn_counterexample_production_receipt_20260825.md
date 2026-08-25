# P11 projective-space Radon--Riesz counterexample: production receipt

Date: 25 August 2026

## Verdict

- Production run: `20260825T044839Z_326e2035bbb9`
- Item: `pi_9e222887262acc5d9fbc740a`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Checked items: 1 of 1
- Critical errors: 0
- Gaps: 0
- Adaptive round: 0
- Wrapper return code: 0
- Wrapper guard: `completed`
- Child guard: `completed`

The item verification confirms that the transverse-initial-form
specialization proves pointwise weak convergence, the section computations
give both exhaustion values, and the exact Boucksom--Jonsson section formula
gives the uniform strong gap.

## Exact frozen input

- Statement SHA-256:
  `326e2035bbb9dd6b3d705f085c19d293da2e58b2998f3452b654c2d75d6d42f3`
- Proof SHA-256:
  `7c9317bce0cb53b5767eb63e053c4f0e94ab23b88292e17cb481a1cdba914585`
- Request SHA-256:
  `d186c1e5b96ebb91370a15155b5d6b8f4e355b04740db69bd4ccf60b1ed0b2f7`
- Authenticated source PDF SHA-256:
  `8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52`

The request's `statement` and `proof` strings were compared byte-for-byte
with the frozen TeX files before submission.  The returned proof digest is
exactly the frozen proof SHA-256 above.

## Exact scope

The theorem works on `P^n` for every `n >= 2`, over an algebraically closed
trivially valued field of arbitrary characteristic.  The center is a linear
line `C = P^1`.  For `n >= 3`, the limit valuation is the exceptional
valuation of the blowup along `C`; for `n = 2`, the center is Cartier and the
limit valuation is explicitly `ord_C`.  The dimension-one center is what
makes the bad locus of each transverse initial form finite.

The earlier `P^2` final/correct run remains a separately preserved verified
baseline.  The rejected first `P^2` proof also remains quarantined and is not
used.

## Preflight

A minimal wrapper containing only the exact statement and proof compiled
twice under `pdflatex -halt-on-error -interaction=nonstopmode`.  The final
pass had no TeX warning, fatal error, undefined reference, overfull box, or
underfull box.  The rendered two-page result was visually inspected.

## Preserved production artifacts

- API response SHA-256:
  `2ee2e7d40932474b6a195dc88b5bdebe7eaa6c19022756778ea051f205cd15b9`
- Run manifest SHA-256:
  `e800c4ccc11493e7b379044c621bd281ca9c4659349dd20359300b3a4938916c`
- Run verification SHA-256:
  `828b844a5edbf81c8d5d4d62f680ae3392522544ea792571bda4bb87ec566c45`
- Item verification SHA-256:
  `51bc5e3f6c57e8f87719bc6e83892b6b4704f5f44da535741eaa32a45a7391d6`
- Item log SHA-256:
  `5aa1f88cad30316f11948810a33a41aedb33f256e1c19123c4c2e08371ffb41c`
- Wrapper guard SHA-256:
  `2fa85afdb785f325463402af24c57184f8e80947dbad1e25cbb6bf1f2ffd073c`
- Child guard SHA-256:
  `4d519ab5cdd02329b0e5babcdac58302b5c327f4be13551eb9cf28e64f2add17`

All copied run, item, log, and guard files were compared byte-for-byte with
the verifier result files.

## Live-edit firewall

No live chapter, appendix, global ledger, status count, or output packet was
edited during this generalization audit or submission.  The receipt controls
the frozen pre-integration packet, not future live bytes.
