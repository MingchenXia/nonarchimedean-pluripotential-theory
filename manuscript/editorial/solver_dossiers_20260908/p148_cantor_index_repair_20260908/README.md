# P14.8 Cantor-index repair

## Scope

This is a post-v2 proof repair for the P14.8 exact-dichotomy candidate.  The
v2 proof wrote `ell_m=exp(-4^m)` while using the standard generalized-Cantor
normalization `ell_0=1`.  Taken together, those two statements conflict at
`m=0`.

The v3 patch fixes the initial index explicitly: `ell_0=1` and
`ell_m=exp(-4^m)` for `m>=1`.  It proves the first child-fit inequality
separately, proves the remaining ratio bound, and starts the capacity
divergence sum at `m=1`.  No theorem statement, reconstruction argument,
nonpluripolar-mass computation, or scope firewall changes.

This dossier is an authored repair and local validation record.  It is not an
independent mathematical audit, a source-complete production verdict, live
integration, or evidence for retiring P14.8.

## Exact boundary

The zero-context `V2_TO_V3.patch` applies with `git apply --unidiff-zero` to
v2 `PROOF.tex` with SHA-256
`adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9` and
produces the v3 proof postimage recorded in `VALIDATION.md`.  The matching
corrected Cantor convention is also present in the preserved P14.8
source-stage packet; the live Chapter 51 source itself is not changed here.
