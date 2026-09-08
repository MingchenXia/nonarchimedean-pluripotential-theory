# Current-source binding — P14.2

Checked on 8 September 2026 against the working tree and `HEAD`.

The live Chapter 71 file has SHA-256
`749a376fe598e7a994bf5d1f2bc38de18b5b2deaea96c87ff87e38a52a5b8456`.
Its whole-file digest differs from `HEAD` because the working tree contains
later raw-filtration material after the P14.2 subsection.  That provenance
difference makes a historical whole-file pin fail closed, as it should.

It does not indicate a change to P14.2:

- the live P14.2 block, source lines 608--930, has SHA-256
  `97040d5ea986144b29667c0d7a2cb2ab092118b9a0fba2b848d999ed35998b96`;
- the same line range from `HEAD` has the identical digest;
- the uncommitted Chapter 71 diff contains no P14.2 label or
  upper-semicontinuity/finite-ideal change.

This is a narrow current-source observation.  It does not supersede the
source-closed release’s frozen manifest, furnish an independent production
audit, or authorize a Chapter 72 status change.
