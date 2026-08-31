# Primary-source and interface checks

Date: 1 September 2026. Reviewer: /root/p213_skeletal_hostile.

## Exact source identity

Primary PDF: /private/tmp/CLD25.pdf
SHA-256: 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719
Bytes: 4659053. PDF has 608 physical pages; the relevant physical and printed page numbers agree.

Extracted text: /private/tmp/CLD25.txt
SHA-256: 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e
Bytes: 2150944.

The PDF skill was used read-only. Printed pages 332, 357, 359, 396, 399, and 424 were rendered with pdftoppm and individually viewed in full. Their displays were legible, complete, and consistent with the extracted formulas and hypotheses. This is source QA, not a rendered-candidate or production typesetting check. No source PDF was modified or re-exported.

## Source-to-claim matrix

| Candidate interface | Primary passage checked | Exact scope consequence |
| --- | --- | --- |
| K-Gauss to L-Gauss uniqueness | Corollary 12.1.8(b), p.332; text lines 16635-16686 | Algebraic graded residue extension gives unique Gauss lift and the completed tensor/residue-field identity. Finite L/K satisfies this. The value-group constraint needed for the tube's m-fold degree is separately from L's unramified hypothesis. |
| R maximal-variation skeleton versus characteristic skeleton | Corollaries 12.8.3 and 12.8.4, p.357; text around 18095-18110 | On boundaryless D_Omega the two source skeletons coincide; there is no extra lower-dimensional characteristic part. |
| Closedness and actual Gauss preimage | Theorem 12.9.4 proof (a)-(b), p.359; text lines 18174ff | For an n-coordinate moment the characteristic skeleton is the inverse image of the closed torus Gauss skeleton and behaves correctly on an analytic-domain restriction. |
| Cell convenience and refinement | Definition 14.1.3; Remark 14.1.4(b), Lemma 14.1.5, Corollary 14.1.6, pp.395-396; text 20089-20138 | On a boundaryless source the cells in the skeleton decomposition are convenient; the paracompact locally finite interface fits R. |
| Local degree on one source cell | Proposition 14.2.2 with complete proof, p.399; text 20288-20318 | The local finite-flat degree is constant on the convenient top-cell interior. It does not assert that all nearby analytic source points form one ordinary sheet. |
| Compact cutoff on the actual domain | Section 15.2.2, Corollaries 15.2.4-15.2.5, pp.423-424; text 21555-21603 | Good separated source is locally holomorphically separated and admits a smooth compact cutoff equal to one near the compact inverse image. No current extension is required. |

Additional extracted-text passages read for the interface include Proposition 12.2.8(iv), pp.335-336, and Sections 12.9.3-12.9.6, pp.358-360. The audit's use of intrinsic source skeletons is tied to these actual analytic moment results; it is not an ambient dimensional heuristic.

## Conditional project premises

L note:
3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a.
Its geometric Sections 2-4, canonical degree in Section 5, and single-source assertions in Sections 6-7 are explicit premises. The whole-domain arbitrary-current conclusion is NOT applied to T on D_Omega; the candidate reconstructs that conclusion on the actual proper restriction.

R statement:
5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a.
R proof:
27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a.

Only the displayed formula with arbitrary compact source multiplier, constant nonnegative top-cell coefficients, and no lower-cell residual is assumed. The stronger local-affine-separation wording is neither used nor freshly certified. R is required on D_Omega itself. No claim that a current extends from D_Omega to D is needed.

The exact primary bytes, candidate files, dependencies, and six source-QA PNGs are recorded in INPUT_CHECKS.json and the audit manifest. The candidate freeze script was inspected, not used to alter any candidate bytes.
