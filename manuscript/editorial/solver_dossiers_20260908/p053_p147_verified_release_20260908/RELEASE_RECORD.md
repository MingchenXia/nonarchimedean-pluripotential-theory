# P05.3--P05.4 and P14.7 verified release record

Date: 8 September 2026.

## Scope

This release integrates and records only three retired atomic questions:

- P05.3, the recursive polyhedral-to-CLD Monge--Ampere comparison;
- P05.4, its algebraic-chart delta-form realization; and
- P14.7, raw maximality of strict-interior DXZ filtration slices.

It leaves P05.5 open: a proper polarized realization, global semipositive
lifts, exact mass matching, and componentwise intersection calibration still
have to be constructed.  It also leaves P14.8 open: the P14.7 terminal
left-limit corollary is not reconstruction of arbitrary zero-mass data.

## P05.3--P05.4 evidence

The exact P05.3--P05.4 statement and proof passed source-closed production
run `20260901T070930Z_773fc66f34a8_35b1bb24`, with verdict `correct`, zero
critical errors, and zero gaps.  Its immutable target hashes are:

```text
statement  773fc66f34a898049afb01c89957718d8c0a2b911bec29a4cc9fa28576e83702
proof      58e50d8c09f31030e6a1fd360214fa0163f147be92fb8884873be97252082ee9
```

The live fragment is a book-style adaptation of that payload: it removes the
scratch-only comments and uses ordinary proof headings, without changing the
statement, proof, source interfaces, or scope.  The accepted conditional
P05.5 mass and model-measure comparison is also included solely to delimit
the remaining construction and calibration gates; it does not retire P05.5.

## P14.7 evidence

The P14.7 v2 source-closed production run
`20260901T115233Z_d6fca0374675_41a5ca54` was accepted with verifier verdict
`correct`, zero critical errors, and zero gaps.  The independently audited
statement and proof hashes are:

```text
statement  d6fca037467563e9af28d2ca97917eb1d2f5697c0b36d36f6a6217439bdd444c
proof      bca8ae5fb0a9c184a9b6b89c4e6cadb33acdc536418fa92d9477f75c503012cb
```

The Chapter 71 raw-filtration section is byte-identical to the audited
postimage between its section boundary and the following big-non-nef
boundary.  It proves raw maximality at every strict-interior filtration
parameter, without finite generation, and treats the DXZ terminal left limit
separately.

## Release checks

- The full working-tree book build completed without errors, undefined
  references, or undefined citations (3,522 pages).
- The active-atom ledger changes from 51 to 48, with tier totals
  `(0,5,9,17,17)` for T1 through T5.
- No claim here changes the active status of P05.5 or P14.8.
