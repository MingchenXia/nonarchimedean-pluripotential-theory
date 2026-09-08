# Post-verification and integration audit

Date: 8 September 2026.

## Superseded V1 receipt

The first local model-backed verdict was **`correct`** for
item `pi_71c69891fbcc189b3eaf5aef`, with zero critical errors and zero gaps.
It was obtained for a packet whose statement used the local macro `\an`.
That macro is not defined in the live book, which uses `\An`; the first
receipt therefore does not control the production integration.  Its proof
digest was
`2d41a8f672c46af235049e3d569180899af9a0c05abcc9276ec174a299853dce`,
and its context digest was
`a719007d265c21bcb8b4830c22b52f749f61d301a09d1e5fb21481f16c16db2f`,
with final item-context digest
`98894fd6cccafc22f58360fb23c722a3705222ce12c95cbee373f24bad479a40`.

## Controlling V2 receipt

After replacing `\an` by the live-book macro `\An` in the exact statement,
the local model-backed verifier returned final verdict **`correct`** for
item `pi_9b5ecb53f97997b14013cd54`, with zero critical errors and zero gaps.
The unchanged proof has digest
`2d41a8f672c46af235049e3d569180899af9a0c05abcc9276ec174a299853dce`;
the revised source context has digest
`60eb7969c0d4a8099139e6dc1491bb91372bdd2df54ffdd23b86f4718b10206b`,
and the final item-context digest is
`8e7b50668eb5e07225005bb27f7f209f160862088a46c32f0a7345be892b050d`.

The controlling V2 artifacts have these SHA-256 values:

| Artifact | SHA-256 |
| --- | --- |
| request | `11c3a2e0f9c145b206ef954846b799db016bb16ff1ec128482f8538f66fba769` |
| response | `9b1c4ac0ef4e640e34d9014108e8a8c559162c3b5cc49a805d41490d5d69f63e` |
| safe headers | `74aad809f0c1529ebb2eaa86743f92ab980423ea264ddc16d824d5488df299f5` |

## Live integration scope

The V2-verified statement and proof are now integrated in Chapter 16 as
`prop:p213-invariant-split-toric-continuous-pairs-candidate`.  Chapter 69,
Chapter 72, and the controlling open-problem inventory record the same
narrowing.  P21.3 remains active and the count remains 48: the result applies
only to maximal-compact-torus-invariant continuous psh pairs on an open
inverse image in a split dense torus.

The exact live source was reread after integration.  The complete book then
built successfully to a 3,522-page PDF with no TeX errors.  No claim in this
dossier settles the non-invariant, boundary, nonsplit, or general analytic
residual of P21.3.
