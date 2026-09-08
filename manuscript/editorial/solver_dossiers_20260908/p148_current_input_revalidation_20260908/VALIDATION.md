# P14.8 live-source rebase validation

## Frozen-check failure and its meaning

On 8 September 2026, from the frozen candidate directory, the command

```text
zsh check_candidate.zsh
```

completed with exit status **one**.  Its SHA-256 phase reported `OK` for
every manifested candidate object, including the statement, proof, fixed
Chapter 51 extracts, source ledger, v1-to-v2 patch, build report, harness,
and retained PDF.  It then stopped at the first live-source comparison:

```text
LIVE_I_PROJECTION_EXACT.tex != current Chapter 51 lines 3240--3288
```

The first frozen block is the `I`-envelope definition and projection theorem,
whereas the old current range contains the inserted `I`-calculus proposition
and begins the envelope subsection.  Independent `cmp` checks similarly fail
at the two further *old* recorded ranges:

```text
LIVE_P1_CANTOR_CONSTRUCTION_EXACT.tex != current Chapter 51 lines 3707--3829
LIVE_P1_ZERO_MASS_FAMILY_EXACT.tex    != current Chapter 51 lines 3898--3917
```

This failure is a locator failure, not yet evidence of changed dependency
content.  `REBASE_MAP.md` tests the three frozen files against their current
counterparts and finds exact byte equality at lines 3291--3339,
3758--3880, and 3949--3968, respectively.

## Rebased current gate

`check_rebased_inputs.zsh` repeats the frozen candidate's SHA ledger,
zero-difference v1-to-v2 patch replay, scope/style firewalls, retained-build
diagnostic scan, and the three Chapter 51 comparisons with the rebased
locations.  A successful run proves that the production target has not
changed and that its mapped live dependencies are exactly current.  It does
not re-run or replace the independent hostile mathematical audit.

On 8 September 2026, the rebased checker completed with exit status zero and
its terminal marker was

```text
P14.8 v2 rebased current-input checks: PASS_NOT_PRODUCTION_ACCEPTED
```

Thus the old locator failure is resolved by the documented map, not hidden or
waived.  The candidate's exact statement/proof, frozen-source hashes,
parent/audit hashes, patch replay, scope firewalls, and retained-build scan
all passed in the current replay.

## Boundary

No candidate file, live Chapter 51 or Chapter 72 file, inventory file, or
production-service state was changed by this replay.  In particular, it does
not provide the required exact-byte source-complete model-backed verdict,
does not authorize integration, and does not change P14.8's active status.

The statement/proof hashes in `README.md` identify the audited v2 candidate.
The old line-range ledger must not be used; `REBASE_MAP.md` and the rebased
checker provide the current source map.  Any eventual production review must
still bind the then-current live integration preimage separately.
