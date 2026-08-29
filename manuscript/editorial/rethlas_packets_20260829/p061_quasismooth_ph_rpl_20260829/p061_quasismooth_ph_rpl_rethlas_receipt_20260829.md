# P06.1 production Rethlas receipt

Date: 29 August 2026

## Frozen inputs

- Statement SHA-256: `0b1b4d161e3b85d342d7be88234a8ed27bfe74be4d24a639ff0456373a7a39e9`
- Proof SHA-256: `fdc6abcc4988644656892172fbdbda4178cb86ca710fd0122a90947e598b0b8b`
- Archived request SHA-256: `2bb46b0881e5b42bfabeb33aa6c29ab158572819b25b60d96e7d169f619eb761`

The request archive contains the exact UTF-8 bytes of the frozen statement
and proof.  The proof digest in both the response and the authoritative
service manifest agrees with the proof hash above.

## Independent audit

The theorem, rigid-etale descent lemma, coefficient firewall, and annular
counterexample passed an independent source-and-scope audit before
production submission.  Two earlier counterexample drafts were rejected:
one used analytic-stalk invariance at a relative-boundary point, and one
incorrectly inferred the existence of a standard subannulus from relative
interiority.  The frozen proof uses neither claim.  It invokes the local
integral-slope theorem for analytic units on quasi-smooth curves, sourced to
Thuillier, Proposition 2.2.24(i), after local semistable reduction.

## Production result

- Service run: `20260829T043457Z_0b1b4d161e3b`
- Item round: `20260829T043457Z_0b1b4d161e3b__0001_pi_7cd35ebd8__round_0`
- Checked item: `pi_7cd35ebd843cf80a7cd696bb`
- Model: `gpt-5.6-sol`
- Reasoning effort: `xhigh`
- Verification status: `final`
- Verdict: `correct`
- Critical errors: `0`
- Gaps: `0`
- Process return code: `0`
- Verifier output status: `validated`

The service manifest records the exact proof digest.  The item log records
the model, reasoning effort, elapsed time, process status, and validated
output.  The process guard and child guard both record state `completed`.

The HTTP helper's compact response omits a `run_id`; this is an API response
field omission, not missing run evidence.  The authoritative service result,
item-round log, process guards, request, response, and headers are archived
under `p061_quasismooth_ph_rpl_run_20260829/`.  The initial HTTP 429 response,
issued while an unrelated verifier job occupied the single local slot, is
also retained there as `busy_attempt1_*`; it did not dispatch a model.

## Scope

The clean verdict covers the exact rigid-etale descent lemma, the theorem
that classically pluriharmonic functions on good strict quasi-smooth spaces
are real-PL and GJR harmonic, the irrational-slope counterexample to a
rational or integral PL strengthening, and all printed proofs.  It does not
extend the theorem to non-quasi-smooth points in analytic dimension at least
two.  That singular higher-dimensional residual remains open.
