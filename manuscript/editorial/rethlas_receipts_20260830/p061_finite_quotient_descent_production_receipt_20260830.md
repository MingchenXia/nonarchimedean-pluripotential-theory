# P06.1 finite-quotient descent: production receipt

**Date:** 30 August 2026  
**Production run:** `20260829T235341Z_e1daa4b3e3ef`  
**Model:** `gpt-5.6-sol`  
**Reasoning effort:** `xhigh`  
**Verdict:** `correct`  
**Critical errors:** 0  
**Gaps:** 0  
**Endpoint status:** HTTP 200  
**Endpoint item identifier:** none assigned

The frozen proposition proves that real-PL regularity descends through the
analytic quotient of a separated strict affinoid space by a finite constant
group.  It allows nonfree, nonflat, wild, nonreduced, and nonnormal quotients.
The proof repairs the G-topology defect in the superseded candidate by using
the ordinary-open decomposition of a real-PL function into finitely many
integral model functions.  It then constructs a common equivariant formal
model, applies tensor induction, descends invariant frames through the formal
coarse quotient, and averages only in the real coefficient space.

A source-aware hostile audit and a second independent exact-byte hostile
audit passed before production submission.  The production verifier checked
the clean stabilizer slice, strict-affinoid intersection, equivariant common
model, quasi-projective special fibre, Zavyalov quotient hypotheses,
nonflat line-bundle descent, pullback identity, and final localization.

## Frozen hashes

- statement:
  `e1daa4b3e3efd64fcc8f0ce05b9c1d5d6cb69b28686b939b48535fc56b0ccc07`
- proof:
  `a6c24d1686c726dc72aebe55a1e83eb8d4fe1ed4025d4a8d7166da59123ce30e`
- source-aware hostile audit:
  `335c46c4e3e264bc23e4c43c8ae001b74bcd79d6ee9fb878ebd18f87036e6fa9`
- independent exact-byte hostile audit:
  `8f349b75bd8fe4af854cb4b8025c7de70d504f219955677149456d1c07794aee`
- archived request:
  `14972425dca44c5358c777eb5278abe31c273a813a70ee80e8e2562b7318d502`
- archived response:
  `8965726ad18c2ba5b14227a4d0dd7cd88feeb966a10b8dde14c5bef41500b7f8`
- archived safe headers:
  `8fe13b355155d1a9c1a9cef26ccb3769e328fb99f7b4c01fcd5f1282f66a19be`
- service verification:
  `e8877adbe7b5b83f0c982dc168e4208c530d9a06fab2f7cbab82b2071fe0351f`
- final service log:
  `ae750c9da5d0d83bbf8b19683c41c865198ea4bd280802836bf74c62e5a2214d`

The controlling service log begins with the command-line provenance
`-m gpt-5.6-sol --config model_reasoning_effort=xhigh` and ends with a
schema-valid final verdict.  The endpoint response and service verification
both report `correct`, no critical error, and no gap.

## Integration scope

Chapter 18 inputs the exact frozen statement and proof and records the
primary-source anchors.  Chapter 72 records the corresponding finite-quotient
range.  Since classical pluriharmonicity is stable under pullback, the theorem
settles finite constant-group quotients of all previously verified separated
strict affinoid P06.1 source scopes.  It does not construct a quotient
uniformization for an arbitrary singular germ, does not cover nonconstant
finite group schemes or infinite groups, and does not retire P06.1.  The
inventory remains 53 atoms in 14 formal problem environments.
