# Primary interfaces

This is a source-interface check, not an independent recertification of the cited papers. The proof is for a connected compact Kähler manifold. No projectivity or rationality assumption is imported from the algebraic subsection of Xia's paper.

| Source and exact locator | Interface used and scope check |
| --- | --- |
| Xia, *Operations on transcendental non-Archimedean metrics*, arXiv:2312.17150v3, §3.2, Definition 3.2 | Prime test curves consist of decreasing concave normalized I-model levels with a finite endpoint. This definition does not assume positive mass. The section's setting is a reduced irreducible unibranch compact Kähler space, hence includes our connected smooth X. |
| Same, Definition 3.5, formula (3.4) | Defines the full space as the inverse limit of prime spaces over all Kähler forms, with normalized I-envelope transitions and reversed perturbation order. This is the definition used directly in the flattening proof. |
| Same, Lemma 3.7 and equation (3.5) | Identifies the positive-mass inverse system, the full space, and the inverse system of full spaces; gives natural full-space injections under Kähler perturbation. The candidate expands the latter idempotence into a choice-independent component construction. It does not assert that every isolated prime curve is positive-mass. |
| Same, Definition 3.9 and Lemma 3.10 | The mass is the decreasing perturbation limit. The zero-class example uses the definition. Lemma 3.10's recovery requires positive limiting mass and is explicitly **not used** in the theorem. |
| Same, §4.1, Definition 4.1 and Lemma 4.2 | The DXZ order is compatible with class injections and is reflected by divisorial values. The proof may instead read off order from its explicit components. Section 4 again states the compact Kähler setting. |
| Darvas–Xia–Zhang, arXiv:2302.02541v3, introduction, pp. 2–3 | Explicitly identifies the spaces for theta and theta+ddc h and treats the result as a cohomological invariant. This existing change-of-representative identification is an input. |
| Same, §2.1, I-envelope paragraph; §3.3, formulas (39)–(40) and following paragraph | The normalized I-envelope preserves the multiplier ideals (there attributed to DX22 Proposition 2.18(ii)). The candidate explains why subtracting smooth h leaves every ideal unchanged; the normalized representative must be re-enveloped, not merely shifted. Equality of all ideals makes raw equality literal at all semivaluations. The source's subsequent algebraic bijection is **not** invoked for transcendental nef classes. |
| Mesquita-Piccione, arXiv:2409.06221v2, Definitions 4.1.2 and 4.3.1 | Positivity of a PL function is relative nefness of gamma_X+D; general Kähler-class psh functions are decreasing model limits. Adding a pullback nef class preserves positivity of the **same** model function. Hence cone monotonicity, with both endpoint classes Kähler. This use does not extend MP's own standing Kähler hypothesis to boundary classes by notation. |

Primary text was read from the exact local files in `INPUTS.json`. Xia's v3 HTML was also opened at <https://arxiv.org/html/2312.17150v3> on 31 August 2026. No PDF creation or visual-source review is claimed in this packet.

## Dependency direction

1. Existing DXZ prime/full systems, transitions, cohomological identification and order.
2. Existing MP Kähler model definition and its immediate same-model monotonicity consequence.
3. Conditional full Kähler raw comparison from the separate `p143_kahler_truncation_research_20260831` packet.
4. New expanded inverse-limit diagonal plus uniqueness-based coherence yields the conditional nef-intersection comparison.

Step 3 is not proved by Step 4. Neither boundary-class fixed-model density nor positive-volume recovery is fed back into the Kähler theorem. The raw-USC and dominated-divisorial candidates enter only through the explicitly conditional Kähler dependency.

## Reference changes and positivity

For a Kähler class, a chosen representative `theta+epsilon*omega` need not be a positive form. It is transported to a positive representative by the source's standard DXZ identification before the conditional Kähler theorem is applied. The raw transform is unchanged because the transition preserves ideals and a smooth summand is locally bounded. This avoids an implicit semipositivity assumption on the original representative.

No energy normalization from the Kähler theorem is used in the present deduction. No normalized or unnormalized energy is assigned at zero volume.
