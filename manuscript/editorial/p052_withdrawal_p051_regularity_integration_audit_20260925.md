# Withdrawn P05.2 source and P05.1 regularity repair: integration audit — 25 September 2026

## Source status

The supplied replacement PDF is the three-page *Withdrawn draft:
Orthogonality on one-dimensional balanced fans*.  It is preserved byte for
byte at
`manuscript/author_sources_20260925/one-vertex-polyhedral-orthogonality.pdf`,
252,482 bytes, SHA-256
`0ad51074108eb2202d4b624637c035610d275c67fd8456dab59282d543d5f5fb`.
The earlier source bytes, SHA-256
`b69aacb76afd056894811f8ac73932c7b82176ba7d9934d1e2d7386f7869f8d8`,
remain recoverable from Git history.

A subsequently supplied copy was compared byte for byte with the preserved
withdrawal version and has the same SHA-256 value.  The source-directory
checksum ledger now records the replacement bytes rather than the superseded
pre-withdrawal digest.

The replacement withdraws its positive theorem because its literal
integral-slope class conflicts with the real-affine envelope used in the
proof.  Chapter 72 now records that status and does not cite the retained body
as a positive theorem.  The bibliography and provenance ledger likewise mark
the source as withdrawn.

## Book-local repair

Chapter 72 now separates two coefficient categories.

1. In the real scalar extension, every one-dimensional balanced rational
   polyhedral space admitting a finite structure has polyhedral regularity.
   The proof replaces an envelope edgewise by endpoint chords on bounded
   edges and by reference-parallel lines on unbounded edges, then checks that
   all vertex-centred Jensen inequalities survive the simultaneous
   replacement.
2. In the literal integral-slope category, regularity already fails on the
   complete affine line with reference `|x|`.  A bounded integral-slope
   obstacle has envelope slopes `-1`, `1/2`, and `1`; every integral-slope
   convex PA function stays at uniform distance at least `1/4` from that
   envelope.

A later same-day strengthening, recorded in its own integration audit,
replaces item 2 by a universal one-vertex theorem.  For every
positive-at-infinity literal reference on every one-vertex balanced rational
fan, every chosen ray and every integer `N>=2` give a bounded integral-slope
obstacle whose envelope has initial slope `g_j-1/N` and remains at uniform
distance at least `(N-1)/(2N)` from every literal convex PA approximant.  The
affine-line example above is its `N=2` special case.  This addendum does not
alter the release evidence below, which records the earlier integration
checkpoint.

The one-vertex and finite-graph orthogonality criteria remain book-local
results in the explicit real category.  Their source preambles and evidence
records no longer attribute the theorem to the withdrawn note.  The complete
affine-space theorem is also stated in the real category in every dimension.
The former boundedly-conical regularity corollary was removed because the
cited source remark only regularizes conical functions.  The Bergman-fan
example is replaced by a rigorous dichotomy: either its envelope is not
real-regularizable, or it has a noncontact atom and orthogonality fails.

P05.1 remains active because higher-dimensional regularity is unresolved;
P05.2 remains active because the literal integral-slope and
higher-dimensional singular-fan problems remain unresolved.  The inventory
therefore stays at 42 active atoms in 12 formal environments, tiers
`(0,3,7,15,17)`.

## Verification boundary

Historical P05.2 gpt-6-astra/xhigh receipts remain archived against their
exact dependency-closed packets.  They do not cover the replacement-source
status edits, the new P05.1 theorem, or the later affine and Bergman-fan
repairs.  No new model-verifier result is claimed for this integration.

## Mechanical and visual checks

- Scoped Mingchen-writing audit: zero errors and one reviewed BMPS26
  arXiv-preprint warning.
- P05.1 minimal packet: 3 pages, 135,751 bytes, clean log.
- Revised P05.2 minimal packet: 4 pages, 146,475 bytes, clean log.
- Reference checker: 409 build-closure files, 11,854 unique labels, zero
  missing inputs, duplicate labels, dangling references, or structural
  errors.
- Unit tests: all six pass.
- Inventory checker: pass, 42 atoms, 12 environments, tiers
  `(0,3,7,15,17)`.
- Full book: 4,084 pages, 19,443,419 bytes, SHA-256
  `05c0b1e154fd57c570068a49e6cbb5a221193f6351019b8735eaddfd469c5407`.
- Full-book log: no unresolved reference or citation, rerun request, overflow,
  or fatal error; the 13 inherited duplicate Chapter 70 destinations are
  unchanged.
- Visual audit: all three pages of the replacement source and physical book
  pages 3793, 3796, 3806, 3809, and 4061 were inspected.  The sampled pages
  cover the new theorem and counterexample, withdrawal transition,
  complete-affine theorem, Bergman-fan correction, and provenance ledger; no
  clipping, collision, or broken line was found.
