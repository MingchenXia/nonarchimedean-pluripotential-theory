# P21 upstairs-cross curve obstruction: production receipt

**Date:** 25 August 2026 (Asia/Shanghai)

**Status:** frozen production verification; no live chapter integration was
performed by this run.

## Verdict

- Guarded run: `20260825T034743Z_ea6194f07e86`.
- Checked item: `pi_19c9aad210847a2875a0fe4a`.
- Model and effort: `gpt-5.6-sol`, `xhigh`.
- Verification status and verdict: `final/correct`.
- Critical errors and gaps: zero.
- Proof digest: `2426acd5e1662ed5aad826597b389884ef925c42258538c86184ab7dd7817a11`.
- Aggregate context digest:
  `656100319e83005aaf4a2f4afaf92f2fc5cf423a83731ca4479606e3fbb45a7f`.
- Adaptive context digest:
  `dce19a1128694422460018e070eb41f8fbfb8565ccafe667419d9cdacc5cfe4e`.
- The process guard and child-process guard both terminated in state
  `completed`; the wrapper return code was zero.

An earlier same-byte run `20260825T034007Z_ea6194f07e86` also returned
`final/correct`, but its older service did not emit process guards.  The
guarded run above is the controlling receipt.

## Exact verified scope

Let
`X=(P^1_K\{a,b,c,d})^an`, where the four punctures have pairwise distinct
residue classes at the standard type-2 Gauss point.  For

```text
f=(z-a)/(z-b),  g=(z-c)/(z-d),
(s,t)=(-log|f|,-log|g|),
U=2|s|,  V=|s|+|t|,
```

the frozen packet proves that the tropical image is the full cross, that
`U,V` are continuous CLD-psh, and that their CLD and delta-current
curvatures agree upstairs and equal `4 delta_q`.

It also proves that the proposed positive closed order-zero current with
horizontal weights two and vertical weights one does not exist.  The
mandatory refinement by `k=(z-a)/(z-c)` has primitive rays

```text
(1,0,1), (-1,0,0), (0,1,-1), (0,-1,0).
```

Closedness forces
`(w_a-w_b,w_c-w_d,w_a-w_c)=0`, hence all four weights are equal.  The
desired calibration `(2,2,1,1)` has refined balancing defect `(0,0,1)`.
Restriction to smooth test forms gives the same obstruction for a positive
closed delta-current with those visible weights.

This verifies a negative theorem for this exact four-punctured smooth-curve
candidate.  It does not solve `prob:frontier-cross-fan-upstairs` for
higher-dimensional CLD currents or non-PL potentials, and it does not assert
the global classification of all positive closed currents on arbitrary
connected analytic curves.

## Frozen artifact hashes

| Artifact | SHA-256 |
|---|---|
| statement | `ea6194f07e869610c427c326311d7a0bea38ca15e8c0050e396d3c9b5b92a596` |
| source-aware proof | `2426acd5e1662ed5aad826597b389884ef925c42258538c86184ab7dd7817a11` |
| solver dossier | `eea7936ea15df9d2660c30fb683873d8c06eed3a957be5653e293dabd7063bdb` |
| aggregate response | `6f70e83f6fb855e3f75c2027d93d4e19492414cb80c643b44848533fc8f987fc` |
| aggregate manifest | `c1b9065e15eeaa25ba1b9b17714156dab05056a0a9afdfc95c504ce5dbaf7eb9` |
| item verification | `748f2d033586244efc1f1d41df51d8f1406953a4d2e5b8e50f919b37e6d2fce9` |
| item log | `a06df0c7a0dc1fac0716a3f4901357dfbdfcd3f3db471a3bc2c45d859b24c69c` |
| process guard | `1cb66afccce31bafab1dc5a1e5abd80485f3227e04c39ec93b0631be5e1f731a` |
| child-process guard | `afcc269f7d2d4a25841ee2dbcf1a8168260ecf288f1ee38908a3d220a51bfee2` |

The full aggregate and item-level run artifacts are preserved under
`p21_upstairs_cross_curve_obstruction_run_20260825/`.
