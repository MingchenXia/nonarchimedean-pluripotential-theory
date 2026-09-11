# P14.8 current-source release V2

This dossier records the 11 September 2026 production verification of the
exact P14.8 dichotomy already integrated in Chapter 51.  It is bound to Git
commit `01ba38fbd824f75ba4150f1913150950f9d4c19d`, after correction of the
divisorial approximation error to `A(E)/m`.  The corresponding Chapter 51
source has SHA-256
`7f2b4890d6332d042113d89bfa921f0f58bbfcbd63c5a18a9eff21469a0fc40b`.

The verified claim is deliberately narrow.  For complete multiplier-ideal
data realized by an actual theta-psh potential, the normalized canonical
I-model representative is uniquely determined without a positive-mass
assumption.  The raw representative and its raw nonpluripolar mass are not
determined: the pinned projective-line Cantor family supplies the obstruction.
This does not realize arbitrary formal data, prove an all-semivaluation
reconstruction formula, produce a second zero-mass strict-interior DXZ
interval, or retire the broader atom P14.8.

## Release gates

- Source-stage checker and test suite: PASS, 197 tests.
- Independent `gpt-6-astra`/`xhigh` source-and-boundary audit: PASS, zero
  critical errors and zero material gaps.
- Frozen final-path long smoke: PASS in 346.386529957992 seconds, including
  one 310-second wait and 24 process samples; no errors.
- Independent hostile receipt replay: PASS, zero critical errors and zero
  material gaps.
- Accepted production run: `20260911T121602Z_4e4256d738ec_e04ebb78`,
  `gpt-5.6-sol`/`xhigh`, verdict `correct`, zero critical errors and zero gaps.

The two earlier attempts are retained as rejected evidence and were not used
in the accepted result.  V1 run
`20260911T114723Z_4e4256d738ec_9f2458d4` paired an over-broad BEGZ search hit
with the Proposition 1.4 range and was correctly rejected.  The first V2 run
`20260911T121337Z_4e4256d738ec_fd2f8c1d` emitted a model preamble before its
first required MCP call and was correctly rejected without a mathematical
verdict.  The bounded same-release retry is the accepted run above.

`RELEASE_BINDING/` contains the exact target, runtime contract, and release
pins.  `FINAL_PATH_SMOKE/` contains the long-smoke receipt and logs.  The three
run directories preserve client and server evidence.  `PRODUCTION_RECEIPT.md`
summarizes the accepted ledger, `AUDIT_RESULT.json` gives a machine-readable
boundary record, and `SHA256SUMS` binds this complete dossier.
