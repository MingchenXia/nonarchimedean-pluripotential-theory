# P14.8 v4 local validation

## Frozen inputs

| Artifact | SHA-256 |
| --- | --- |
| `VERIFICATION_STATEMENT.md` | `e1646df417434ddc96cf46220aa0cd0f65cf3db03c5e0f8c62c4b0d42315ebcd` |
| `VERIFICATION_PROOF.md` | `3539f68cd263df959ae9a2d99112ec3023c06c7f4dcce43347970ee0ccc26db5` |
| `VERIFICATION_SOURCE_PACKAGE.md` | `606e596b4364f0c8113c352cc06e9ea27a0dfd29904cc047d5bea2ebf151d069` |
| Boucksom source text | `4a3fa01a21b1cc66fe174460732fe80a29914f26279c04d2824223fc7d9ab0a4` |
| BEGZ source text | `890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7` |

## Source-interface replay

The local Boucksom copy contains the exact sequential Lelong statement at
Lemma 2.6, the very-general generic-Lelong statement at Lemma 10.5, and the
valuative multiplier-ideal criterion at Corollary 10.18. The local BEGZ copy
states that nonpluripolar products put no mass on pluripolar subsets and gives
the degree-one construction used in the curve calculation.

The v4 proof uses these interfaces only. It neither repeats nor imports the
five false Chapter 51 claims and two gaps recorded in the v3 verifier receipt.
The Cantor arithmetic remains the exact v3 repair: $\ell_0=1$,
$\ell_m=\exp(-4^m)$ for $m\ge1$, the first child-fit inequality is separate,
and the divergent capacity sum starts at $m=1$.

## Boundary

This is a local source and byte audit.  The exact v4 packet was subsequently
reviewed by the explicitly authorized model-backed verifier, which returned
`correct` with zero critical errors and zero gaps; see
`VERIFICATION_RESULT.md` and `VERIFICATION_RUN_20260908/`.  Neither that
review nor this audit is a source-complete production verdict or P14.8
retirement evidence.
