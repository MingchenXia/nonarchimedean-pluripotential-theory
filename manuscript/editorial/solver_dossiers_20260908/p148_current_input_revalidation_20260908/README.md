# P14.8 live-source rebase audit

## Scope

This dossier records a current-working-tree source-location rebase of the immutable
P14.8 v2 candidate at
`../../solver_dossiers_20260901/p148_zero_mass_reconstruction_candidate_v2_20260901`.
It does not
modify that candidate, its hostile audit, Chapter 51, Chapter 72, or the
open-problem inventory.

The purpose is narrow: before any future source-complete review, determine
whether the candidate's frozen Chapter 51 extracts still agree with the
present manuscript state.  Their recorded line numbers have shifted, but the
three dependent text blocks remain byte-identical at their mapped current
locations.  This is evidence about input freshness, not a new mathematical
theorem or a production verdict.

## Current candidate identity

| Input | SHA-256 |
| --- | --- |
| `PROPOSED_STATEMENT.tex` | `9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715` |
| `PROOF.tex` | `adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9` |
| retained candidate PDF | `ac9d232c28470112332b687d7ba47e3ac0a266ba84dfdf64c8d4f5e2a25abc78` |

The candidate's independently audited mathematical verdict remains a PASS
for the stated dichotomy only.  Its exact v2 input is current-source rebased
and still requires a fresh source-complete production review before
integration or retirement.

## What the rebase establishes

`check_candidate.zsh` verifies the candidate's SHA ledger, its exact
v1-to-v2 patch, scope firewalls, retained build diagnostics, and then
compares each of the following frozen source spans against the live Chapter
51 file:

- lines 3240--3288: realizable `I`-projection construction;
- lines 3707--3829: polar Cantor, Green, and nonpluripolar-mass argument;
- lines 3898--3917: one-class all-mass family.

The old line-range checks fail solely because a 51-line `I`-calculus block
was inserted before the envelope subsection.  `REBASE_MAP.md` records the
new exact locations.  `check_rebased_inputs.zsh` is a read-only version of
the frozen checker that uses those locations while retaining its ledger,
patch, scope, and retained-build checks.  The exact run is recorded in
`VALIDATION.md`.
