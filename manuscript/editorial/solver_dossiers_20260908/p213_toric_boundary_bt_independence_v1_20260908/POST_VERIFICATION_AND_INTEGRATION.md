# Post-verification and integration audit

Date: 8 September 2026.

## Superseded V1 receipt

The first source-aware verifier run returned `wrong` with no critical error
and one audit gap. It required the final smooth-factor product rule to be
supplied rather than cited only by a live-book label. This was a dependency
recording defect, not a mathematical counterexample. Its artifacts remain in
`VERIFICATION_RUN_V1_20260908/` for traceability.

## Controlling V2 receipt

The repaired proof writes the graded Leibniz calculation directly. The local
model-backed verifier returned final verdict **`correct`** for item
`pi_96813b21562d920cf411c5a0`, with zero critical errors and zero gaps.

| Artifact | SHA-256 |
| --- | --- |
| frozen statement | `f79f31d38b07846d19d55cf3cc93a878795aa5a0d83052ffeb50af0b3a88c60d` |
| frozen proof | `281f6d955ca75016af6d10f4848da1078fb9745673a6dcee3a1058b749c419ea` |
| frozen verifier context | `f4cb1c8f174a98ecf5852609daa234d655ee7d30817c9e648d34a3ba6f3d9694` |
| V2 request | `fcc12171e52054b3a0f32480c14aacc57961c0be5596c467ccb02962d614ac87` |
| V2 response | `690f03509067c9c7815f17115d317eea85238ea347024c2739a120fb8f74b745` |
| V2 safe headers | `cf58bde784cd5f611f0df9a2bd9032caad996f344a1584f362cc7b1df31b79a5` |

The verifier reported proof digest
`7d0181f4f479ccc7952f94bd9dbb7b4d18b7d960d58434450d74edb97a3e7c8d`,
context digest
`b72757a38b7c9c8a37cabd522a211b8a4d64127b6c7b275331b14ab3173a71a4`,
and final item-context digest
`93daabb2eee2e3d3f3e253bca679f2517c9b17bfc03fb1bf66500d34539d119e`.

## Live integration scope

The verified boundary extension is integrated in Chapter 16 under the
pre-existing reference label
`prop:p213-invariant-split-toric-continuous-pairs-candidate`, so every prior
cross-reference continues to resolve. Chapters 69 and 72, and the controlling
atomic inventory, now record that the invariant split-toric result includes
open inverse images meeting toric boundary strata.

P21.3 remains active and the active-atom count remains 48. The result still
requires a split toric inverse image and finite continuous
maximal-compact-torus-invariant potentials; it does not settle nonsplit,
noninvariant, arbitrary toroidal, or general analytic higher-dimensional
cases.
