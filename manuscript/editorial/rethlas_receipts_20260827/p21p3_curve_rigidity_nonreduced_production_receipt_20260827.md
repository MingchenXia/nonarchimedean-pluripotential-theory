# P21.3 reduction invariance and nonreduced curve extension: production receipt

**Date:** 27 August 2026

**Local archive label:** `20260827T133151Z_3ee099341ca1`

**Model:** `gpt-5.6-sol`

**Reasoning effort:** `xhigh`

**Verdict:** `correct`

**Critical errors:** `0`

**Gaps:** `0`

The production endpoint assigned no run identifier, item identifier, or
verification-status field.  The label above is the verifier service's local
archive address and is not presented as an endpoint-assigned identifier.

## Exact mathematical bytes

| Artifact | SHA-256 |
|---|---|
| Frozen statement | `3ee099341ca1ba77d806082ca2903320fd9db25c448b48f3dab9c2bb607a777e` |
| Frozen proof | `b8aac711aafa611750c56a960177182ff1b7b8f78b489d7b43575d03b28b7f43` |
| Standalone compile driver | `6beb6e228af8a1112253f539754ab398d71f3c72cbd4711ac71aa2f4794051ac` |
| Minimal frozen cross-reference data | `dcdd7be33e6309a70373e92c83b4c658332d01f4f821650e8a4e0529d1dd6965` |
| Standalone compiled PDF | `96ceb3a464104c400d0c76e99ee2f5d73597b434d6f967f13438a057e1cb94ad` |
| Standalone compile log | `7323c34992ee11588335ef99cc19b282596e5797d6c208b973738b064c45ca95` |
| Frozen packet manifest | `21c8dd25839754b56528f66bb91b922ceb33678f2f9d45a09f243de7bc774640` |

The standalone wrapper inputs the exact statement and proof, imports only
the eight pre-existing book labels on which they depend, and uses the book
bibliography.  It compiles to five pages with no TeX error, undefined
reference or citation, rerun request, or box warning.  Every entry of the
frozen packet manifest verifies.

## Exact request and response

| Artifact | SHA-256 |
|---|---|
| Endpoint request | `3b5f6e32a1de8954d0bfb4827f79ec7f43f85949e4b2ac8e42531da28f28e5cf` |
| Endpoint response | `50bb1132de3b5d9d4a9c95de23c671107615979abc4b739596ac5be4bbb8f1f5` |
| Endpoint headers | `e3cc7aed80b56f668bda8f20ce282303abf06989118645ae125e0ed6653ef83d` |

The archived request contains the complete exact statement and proof.  The
response says that the proof is correct and records zero critical errors and
zero gaps.  The production supervisor invoked `gpt-5.6-sol` at `xhigh` and
recorded 183,635 tokens used.

## Mathematical conclusion

Let (X) be a good separated strict pure one-dimensional boundaryless
analytic space over an algebraically closed complete nontrivially valued
field, without assuming that (X) is reduced, and suppose that the
normalizations of the irreducible components of (X_{\mathrm{red}}) are
rig-smooth.  Passage to the reduction preserves ordinary CLD forms and their
compact-test topology, currents and their weak topology, positivity,
closedness, the stated smooth and Borel products, the CLD psh filtrations,
and (G)-forms.  It does not preserve the integration current:

\[
             \delta_X=\sum_i m_i\delta_i,
             \qquad
             \iota_*\delta_{X_{\mathrm{red}}}=\sum_i\delta_i.
\]

Every positive closed current of bidegree ((0,0)) has a unique locally
finite expression \(\sum_i c_i\delta_i\), with \(c_i\geq0\).  Equality of
the curvature currents defined using \(\delta_X\) is equivalent to equality
using \(\delta_{X_{\mathrm{red}}}\), and every such positive closed current
is Bedford--Taylor.

The key no-cancellation step separates the normalization branches away from
the locally finite conductor/intersection locus and then uses the previously
verified zero-atom lemma at type-1 points.  Hence the generic multiplicities
cannot hide a curvature difference at a component intersection.

## Independent audits and exact scope

Three independent exact-byte audits passed before production verification.
They separately checked the compact-test final topology, current duality and
bidegrees, positive-current Borel multiplication and decomposition
independence, the transfinite psh filtrations, every cited CLD locator, the
fundamental-cycle multiplicities, the open-set restrictions, the zero-atom
argument, and the Bedford--Taylor predicate.  No audit requested a repair.

The theorem removes only reducedness from the previously verified curve
classification.  It does not relax algebraic closedness, completeness,
nontriviality of the valuation, goodness, separatedness, strictness,
boundarylessness, pure dimension one, or rig-smoothness of the reduced
component normalizations.  It does not address analytic dimension at least
two.  Thus P21.3 remains one active T2 atom, and the inventory remains at
sixteen formal problem environments and fifty-five active atoms, with tier
counts 0/7/14/17/17.  No novelty or priority claim is made.
