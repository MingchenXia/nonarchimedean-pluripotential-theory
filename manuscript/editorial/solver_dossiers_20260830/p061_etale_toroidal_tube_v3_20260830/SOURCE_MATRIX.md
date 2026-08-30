# Source matrix

All file hashes identify the exact local bytes inspected.  PDF page numbers
refer to the frozen PDF files.

| Use | Exact locator | Frozen source and SHA-256 | Scope check |
|---|---|---|---|
| Scalar extension and arbitrary analytic pullback preserve classical pluriharmonicity | Gubler--Rabinoff, Proposition 7.2(6),(7), PDF p. 34 | `../../rethlas_packets_20260830/p031_perfected_unibranch_curve_envelope_20260830/sources/Gubler_Rabinoff_2506.13548v2.pdf`, `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726` | Used only in directions explicitly stated by the proposition. |
| Affinoid maximum and minimum occur on the Shilov boundary | Gubler--Rabinoff, Proposition 7.3, PDF p. 35 | same PDF and hash | Applied after scalar extension to each actual completed residue field, not only to rigid fibres. |
| Real-PL pullback stability | Gubler--Jell--Rabinoff, Lemma 5.4(1), PDF p. 31 | `../p061_etale_toroidal_tube_candidate_20260830/sources/Gubler_Jell_Rabinoff_2111.05741.pdf`, `572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42` | Section 5 assumes a nontrivially valued field and good strict spaces.  Those hypotheses appear only in the separate v3 real-PL corollary. |
| Classical psh real-PL equals semipositive | Gubler--Rabinoff, Theorem 4.3, PDF p. 22 | GR PDF and hash above | Applied to both signs only after real-PL regularity is established, on good strict affinoids. |
| GJR harmonicity | Gubler--Jell--Rabinoff, Definition 7.2, PDF p. 45 | GJR PDF and hash above | Both signs semipositive is exactly the invoked definition. |
| Etale morphism has a standard-etale chart after shrinking | Stacks Project, *Etale Morphisms of Schemes*, Theorem 12.3, Tag 025C, PDF p. 15 | `../p061_etale_toroidal_tube_candidate_20260830/sources/Stacks_Etale.pdf`, `cfe0581a0bfe38522726f6a233ab4cd30d5f283bef86c4f136fc2ee34c8ecc99` | The theorem supplies an open immersion into `R[T]_{G'}/(G)`.  V3 explicitly chooses a principal open inside its image and constructs the bounded analytic domain; it does not read an analytic product from Tag 025C. |
| Classical PH on good strict quasi-smooth spaces is real-PL and GJR harmonic | theorem label `thm:p061-quasismooth-ph-rpl`; exact ranges and hashes in `DEPENDENCY_PROVENANCE.md` | full statement/proof hashes `0b1b...39e9` / `fdc6...b8b`; production response `2ee6...ce7e` | Only theorem and its descent proof are isolated.  The unrelated counterexample is excluded. |
| Product-open tube, cofinal weighted domains, and all-orbit monoid localization | labels `lem:p061-product-open-tube`, `prop:p061-parameterized-toric-fixed-fibre`, `thm:p061-split-toric-all-orbits` | statement/proof `05bda...e60` / `21c44...b03`; response `71804...f7d` | Production verdict is `correct`, zero errors and gaps. |

## Arguments proved in v3 rather than imported

1. The four Banach root problems use one fixed radius and explicit strict
   contraction constants.  The two exact-root uniqueness statements are
   invoked in the two composites.
2. Tag 025C is converted to an actual strict source affinoid by a principal
   source shrink, a bounded relative disc, a rational inverse bound,
   rescaling by (c,d\in K^\times), and quotient Gauss norms.
3. Every deeper base change remains an ordinary neighbourhood of the chosen
   point because the fixed toric point and the two variable inequalities are
   interior points.
4. Toric rank zero is separated before the semigroup-generator estimate:
   `S={0}`, `q=0`, `R_k=K`, `A=A_n=B`, and `J=0`, so every coefficient
   error is identically zero and no empty-family maximum is used.  The
   positive-rank augmentation ideal and its decay are computed in the
   normalized semigroup Gauss algebra.
5. The all-orbits corollary identifies the dense torus orbit with the
   rank-zero transverse pointed factor, so that orbit is covered by the
   explicit branch rather than by a tacit empty-family convention.
6. Singleton-Shilovness after every completed residue-field extension is
   proved from multiplicativity of the semigroup Gauss norm and the domain
   property of the residue semigroup algebra.

The exact independent v2 audit that required item 4 has SHA-256
`d884005655ff604eea9e45d90c243f8751ed8505d92700033d90ac2ef8ae4d10`.
