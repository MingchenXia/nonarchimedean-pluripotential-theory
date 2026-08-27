# P21.3 arbitrary-field virtual-annulus bridge: production receipt

**Date:** 28 August 2026

**Local archive label:** `20260827T233539Z_c833fc37ac44`

**Model:** `gpt-5.6-sol`

**Reasoning effort:** `xhigh`

**Verdict:** `correct`

**Critical errors:** `0`

**Gaps:** `0`

The production endpoint returned no run identifier, item identifier, or
verification-status identifier.  The label above is the verifier service's
local archive address and is not presented as an endpoint-assigned
identifier.

## Exact mathematical bytes

| Artifact | SHA-256 |
|---|---|
| Frozen statement | `c833fc37ac443d5a6fa50c31337e0c3d4ac1cc9d6c0a1ee1a450f1cb93ef8bd6` |
| Frozen proof | `e07b064754753073d1be8cd3b78fa71bb4d7878d096671f9e2783eb24539fb13` |
| Standalone compile driver | `add39a0f89a07d1c557b340d851464e6b5da8d1962ed11bacf9f0fe27c7c2cb9` |
| Standalone compiled PDF | `75d98d31005b77b1441aa1f467f50045d48a2e33cd23669ecb8e10edeb771d92` |
| Standalone compile log | `ebfd4cfdd1235b21031906f59973d35cbc90efcbb1ac084b462c19b293a029d4` |
| Source-aware audit | `32e4c0ca87578fe3733cd3c5ea08d20f159886d9ac606ed8c56a04123d870de9` |
| Frozen packet manifest | `5a53ead0ae9718ae97202f615de78ce5afa98df07d3069522cf75f596246d1fe` |

The standalone artifact has four pages.  It has no TeX error, undefined
reference or citation, relevant warning, overfull box, or missing local
label.  All thirteen local labels and reference targets close internally.
Every entry in the nine-file frozen packet manifest verifies.

## Production request and response

| Artifact | SHA-256 |
|---|---|
| Successful endpoint request | `55fee6b56b8ba4843be2702755d457c3fdd5c9911ac169de34c9061290418c3d` |
| Endpoint response | `4b0640e5f316ef1b8422ce913dcf4a2661a62aec74f96286d2b641b835f487c6` |
| Endpoint headers | `201e1db444bf04e7321f328348854b1c92b303e76c5460b420891ab271947625` |

The request contains exactly the complete statement, complete proof, and a
dynamic UTC deadline.  Decoding its strings reproduces the frozen statement
and proof hashes byte-for-byte.  The response says that the proof is correct
and records zero critical errors and zero gaps.  The production supervisor
invoked `gpt-5.6-sol` at `xhigh` and recorded 182,009 tokens used.

An earlier request with SHA-256
`b2b319d769a07a33540857a9aa774c28a37dc806d70691a798165af1d60d0082`
ended in a transport timeout after the model network became unavailable.
That attempt produced no response, verification report, failed check, or
mathematical verdict; its local service archive label was
`20260827T150130Z_c833fc37ac44`.  The request is retained as failed-transport
evidence and is not counted as a verification.  The local service was then
restarted with the same model and reasoning configuration before the
successful request above was sent.

## Verified mathematical conclusion

At an interior type-2 point of a good strict rig-smooth curve over an
arbitrary complete nontrivially valued non-Archimedean field, a branch
corresponds to a closed point of the normal projective integral residual
curve.  A norm-one lift of a residue uniformizer identifies its refined
branch-order quotient with `Z`.  On a cofinal virtual-annular collar, every
finite analytic moment has an exact Euclidean ray whose saturated primitive
tangent is the vector of these branch orders.  After a finite splitting
extension, all split-annulus exponents acquire one common positive expansion
index; residue degree and inseparability do not introduce a second tangent
factor.

Finite residue weak approximation supplies analytic units that separate any
prescribed finite set of branch rays from one another and from every other
outgoing branch.  Under the statement's explicit source-separated
localization hypothesis, the localized CLD target one-cell is exactly the
image of the corresponding virtual-annular collar, and the scalar balancing
coordinate of a lifted residue function is its closed-point order.  The
current remains over the original field throughout; scalar extension is used
only to certify the norm-slope formula.  Ordinary-current and canonical
calibrated fluxes acquire the same expansion factor under tropical
pushforward.

## Scope firewall and next gate

This production result verifies the narrow bridge proposition, including its
explicitly assumed source-separated localization.  It does not prove that
such a localization exists for every test summand, does not by itself prove
the full arbitrary-field curve-current classification, does not close P21.3,
and is not integrated into the live book.

A separate hostile audit found that the older full-dossier phrase “append
moments tropicalizing smooth plateaus” is false if read literally.  The legal
replacement writes a retained smooth cutoff as
`chi = Phi o H_trop` and concatenates the analytic moment `H`, never the
cutoff itself.  That source-localization lemma and the repaired full theorem
remain outside the live book pending their own production Rethlas gate.
Consequently the open-problem inventory and all theorem counts are unchanged
by this receipt.  No novelty or priority claim is made.
