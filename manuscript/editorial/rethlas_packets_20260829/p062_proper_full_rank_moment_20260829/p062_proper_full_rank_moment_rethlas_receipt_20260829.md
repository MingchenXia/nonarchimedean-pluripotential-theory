# P06.2 production Rethlas receipt

Date: 29 August 2026

## Frozen inputs

- Statement SHA-256: `75e9cb498ce4cb7b036f8a15f7da87b187c189e2bb1566aa7bda9027b947327c`
- Proof SHA-256: `0ed2c67ee5120b044bef273f75f11f45d8a04577cd385da1069d9e6f1d01a440`
- Archived request SHA-256: `2f2ddb60665e42a1e15b5514834f8088b9be88d26119e95d736a6101844dc8aa`

The request archive contains the exact UTF-8 bytes of the frozen statement
and proof.  Its recorded proof digest agrees with the proof hash above.

## Production result

- Service run: `20260829T031126Z_75e9cb498ce4`
- Item round: `20260829T031126Z_75e9cb498ce4__0001_pi_f96fe9f89__round_0`
- Checked item: `pi_f96fe9f8904943602779f274`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`
- Process return code: `0`
- Verifier output status: `validated`

The service manifest records the statement-derived run prefix and the exact
proof digest.  The item log records the model, reasoning effort, elapsed
time, process status, and validated output.  The process guard and child
guard both record state `completed`.

The HTTP helper's compact response omits a `run_id`; this is an API response
field omission, not missing run evidence.  The authoritative service result,
item-round log, process guards, request, response, and headers are archived
under `p062_proper_full_rank_moment_run_20260829/`.

## Scope

The clean verdict covers the exact proposition, its boundaryless converse,
the automatic-calibration corollary, the scope remark, and their printed
proofs.  It does not broaden the theorem to arbitrary continuous functions,
lower-rank or singular tropical images, nonproper moment factors, or the
unrestricted higher-dimensional P06.2 problem.
