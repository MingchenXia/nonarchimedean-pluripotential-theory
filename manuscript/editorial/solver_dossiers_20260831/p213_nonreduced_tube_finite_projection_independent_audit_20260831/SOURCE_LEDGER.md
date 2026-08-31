# Independent source and scope ledger

Date: 2026-08-31. Reviewer: /root/p081_weighted_repair_fresh.

## Pinned primary source

Chambert-Loir--Ducros, arXiv:1204.6277v2 (25 July 2025):

- /private/tmp/CLD25.pdf, 4659053 bytes, SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- /private/tmp/CLD25.txt, 2150944 bytes, SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

The following source interfaces were read directly, with relevant surrounding hypotheses and proofs.

| Locator | Exact role and checked limitation |
| --- | --- |
| 7.1.10-7.1.11, pp.158-159; ordinary-form framework 15.1.1 | Compact-support pairing and continuous pullback/pushforward. The candidate independently proves q proper, and uses actual moment pullbacks on the original analytic source. |
| 11.4.1-11.4.6, pp.310-312 | Boundary under composition; finite Banach algebras; G-local finiteness; finite maps have no relative boundary; analytic flatness and analytic-domain locality. In particular the quotient must have the finite-module Banach topology. The written bounded division proves this stronger condition. |
| 12.1.5-12.1.6, pp.330-331 | Laurent Gauss formula, graded-coordinate independence, and density of the rational function field in a Gauss completed residue field. |
| 12.1.8(b), p.332 | Under algebraic graded-residue extension, the torus Gauss point has one preimage and the completed tensor product is its residue field. Every finite coefficient extension used here meets the source hypothesis. It is not a current-base-change statement. |
| 12.2.8(iv), pp.335-336; 12.9.3-12.9.6, pp.358-360 | For the n-coordinate moment, actual characteristic-skeleton membership is inverse image of the torus skeleton; boundaryless full-rank membership and piecewise immersion. This is stronger than merely having the same tropical coordinates. |
| 14.1.4(b),14.1.5,14.1.7, pp.395-396 | Convenient cells on a boundaryless source, permitted decompositions, and the definition of a pleasant moment. Here properness of q and its polyhedral image Q verify the latter condition; g need not be proper to the entire torus outside B. |
| 14.2.1-14.2.2, p.399 | Local finite-flat degree is constant on each convenient top-cell interior, including in nonreduced analytic spaces under the stated level/dimension assumptions. |
| 14.3.2, p.407; 14.4.2-14.4.3, pp.409-410 | Source canonical coefficients are local finite-flat degrees; canonical pushforward; viewing the same analytic space over a finite smaller coefficient field multiplies calibration by the full field degree. |
| 14.5.2-14.5.3, pp.410-411 | Target calibration from the actual finite-flat map at Gauss points. The canonical coefficient m is not assumed to be the unknown current's coefficient b. |
| 15.2.2-15.2.5, pp.423-424 | Good separated analytic spaces are locally holomorphically separated and admit ordinary smooth compact cutoffs equal to one near a prescribed compact set. Used for the final same-test application of R, not the stronger local-affine-separation adjective. |

Ten complete source pages were rendered and viewed in this audit: 311,312,331,332,359,396,399,407,410,411. Other passages were read in the pinned extraction. The resulting visual record is in SOURCE_VISUAL_QA.json. No source PDF was changed.

## Analytic and valuation interface checks

The standard polyannular Banach algebra permits arbitrary positive endpoint radii. The upper radii <1 bound the formal unit's higher coefficients uniformly. The written division shows a continuous finite-free quotient, which is exactly the finite Banach-algebra condition in CLD11.4.4, and completed affinoid base change preserves that finite-free module.

The valuation bound in Section 6 can be checked directly without assuming defectlessness: the powers 1,x,...,x^{m-1} have distinct value-group cosets over H and are linearly independent. Together with the TOTAL fibre-algebra dimension m this excludes both other factors and nilpotent length. No source theorem concerning separability or tame ramification is imported.

As an ancillary read-only cross-check, [Temkin's Introduction to Berkovich analytic spaces](https://math.huji.ac.il/~temkin/papers/Introduction_to_Berkovich_Spaces.pdf), arXiv:1010.2235v2, Example/Exercise4.2.4.2(iii), printed p.30, also states that finite analytic morphisms are proper. This was consulted online on 2026-08-31. The audit does not depend on a new theorem from that overview: the needed finite-map interfaces were located directly in the pinned CLD source above. No local copy or visual inspection of that supplementary PDF is claimed.

## Conditional dependencies and authorship

Root authored the entire new finite-projection note. The reviewer had no role in its argument. The reviewer previously audited the separate reduced-model wall result and the representation/common-moment inputs; those earlier verdicts are not proof of the new statement.

R is explicitly assumed only for the individual-source coefficient identity in Section 7. The coefficient normalization is the ordinary q-coordinate volume. The stronger literal affine-separation terminology in the source is neither required nor certified.

No global nonreduced-SNC divisor functional, ordinary-W locality, arbitrary analytic wall realization, all-cell accessibility, full P21.3, or production acceptance follows from this audit. No priority claim is made.
