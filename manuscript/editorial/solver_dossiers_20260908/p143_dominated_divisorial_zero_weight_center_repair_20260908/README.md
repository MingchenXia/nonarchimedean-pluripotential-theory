# P14.3 zero-weight component repair

## Scope

This is a precise post-freeze repair to the v2 P14.3 proof postimage created
by the extended-arithmetic patch. It changes only one explanatory step in
the finite-ideal approximation argument.

The v2 wording inferred that a zero-weight divisor cannot contain the selected
stratum from simple-normal-crossing geometry. The v3 wording instead uses the
central variety already present in the proof: if such a divisor contained the
stratum, its ideal would be contained in the positive central ideal, forcing
its semivaluation weight to be positive.

This repair preserves the theorem statement, the rational divisorial
approximation claim, and every conclusion. It is not by itself an independent
mathematical audit, a source-closed production verdict, live-book integration,
or P14.3 retirement evidence. A later source-aligned live-book integration is
recorded separately in `LIVE_INTEGRATION.md`.

## Exact boundary

V2_TO_V3.patch must apply with zero fuzz to the v2 proof postimage whose
SHA-256 is recorded in the extended-arithmetic repair dossier. Its resulting
v3 proof must receive a fresh byte check and draft build before it may be
considered for independent review.

## 8 September validation

The patch applies exactly to the v2 postimage and the resulting v3 proof has
a clean isolated draft build. See VALIDATION.md for the exact postimage and
log hashes. `VERIFICATION_STATEMENT.md`, `VERIFICATION_PROOF.md`, and
`LOCAL_SOURCE_AUDIT.md` are the refreshed v3 review materials.  The
explicitly authorized model-backed review subsequently returned `correct`
with zero critical errors and zero gaps; its immutable HTTP-200 receipt is
archived in `VERIFICATION_RUN_20260908/` and summarized in
`VERIFICATION_RESULT.md`.  This review did not itself supply a source-closed
production verdict, live-book integration, or P14.3 retirement.  The later
Chapter 71/72 integration is recorded in `LIVE_INTEGRATION.md`; its
source-closed production-verification record remains incomplete, and P14.3
remains active beyond the finite-energy Kähler conclusion.
