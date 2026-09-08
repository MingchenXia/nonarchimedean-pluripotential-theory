# P14.3 dominated-divisorial candidate: reproducibility audit

## Status and scope

This is a new, read-only reproducibility audit of the frozen 31 August P14.3
research candidate.  It does not modify that candidate's statement, proof, or
diagnostic; it does not assert an independent mathematical audit, a production
verification, a live-manuscript integration, or retirement of P14.3.

The original candidate checker became non-reproducible because four of its
inputs were addressed through a deleted `/private/tmp/nappt_p071_20260827`
snapshot, while the two primary-source text files were addressed through
deleted `/private/tmp/mp24.txt` and `/private/tmp/dxz23.txt` paths.  The
replacement checker resolves only byte-identical durable copies already in
this repository.  It does not substitute a later version of either primary
source, and it deliberately does not pin the mutable live Chapter 71 or
Chapter 72 files as evidence for the frozen claim.

## Bound inputs

`check_current_candidate.mjs` binds:

- the P14.3 statement, proof, and diagnostic bytes;
- the frozen P14.2 statement, proof, and manifest on which the conditional
  finite-energy conclusion depends; and
- the exact MP v2 and DXZ v3 source texts used by the candidate.

It also checks the candidate's internal labels and references.  Its output is
evidence that the frozen candidate can be inspected against present durable
inputs; it is not evidence that the new dominated-density theorem has passed
independent or source-closed production review.

## Promotion boundary

Before any live promotion, the unchanged mathematical bytes still require an
independent exact-byte mathematical audit and a source-closed production
verification.  In particular, P14.2's current production-verification
boundary remains a dependency of the conditional finite-energy corollary.

## Chapter 72 interface

On 8 September 2026, Chapter 72 and the atomic inventory were updated to
describe this exact finite-energy K\"ahler reduction and its remaining gates.
The update leaves P14.3 active, does not alter any count or tier, and does not
present the candidate as a theorem of the book.  A full-book build completed
successfully after that reader-facing clarification.
