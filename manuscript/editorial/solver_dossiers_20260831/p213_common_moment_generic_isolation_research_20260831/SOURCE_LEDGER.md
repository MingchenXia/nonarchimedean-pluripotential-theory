# Source ledger: generic source isolation for an actual common moment

Date: 31 August 2026. Author: `/root/p082_independent_reaudit`.

## Primary source and exact version

Antoine Chambert-Loir and Antoine Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025, 608 pages. The official primary record was reopened in this task: <https://arxiv.org/abs/1204.6277v2>.

- `/private/tmp/CLD25.pdf`: SHA-256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
- `/private/tmp/CLD25.txt`: SHA-256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

Exact mathematical source text was read locally, including complete passages and proofs identified below. No source PDF was edited and no new PDF rendering or source-page visual QA is claimed for this packet.

| Exact source | What it supplies, and what is not inferred |
| --- | --- |
| Section 3.1.3, printed pp.73-74 | Tropical dimension at a source point is the infimum of dimensions of images of compact domain-neighbourhoods. This proves monotonicity under an affine projection, hence S_F,S_G subset S_H. |
| Definition 5.2.1, p.123, including the closedness paragraph | Definition and closedness of the maximal-variation source set. It is not replaced by the full target tropicalization. |
| Proposition 5.2.5(a)-(b), pp.124-125, complete proof | Maximal-variation source sets are pure n-dimensional PL spaces; the moment is an immersion by pieces. Restriction to an ordinary open U gives the same source trace, since that trace remains pure n-dimensional. |
| Remark 5.4.2, p.129 | A source subset carried homeomorphically onto an n-cell by a tropical chart lies in the maximal-variation source set. The new note independently spells out the neighbourhood-dimension argument for its already PL H-cell. |
| Section 5.3.1, Remark 5.3.2, Lemma 5.3.4 and Proposition 5.3.6, pp.127-129, including proofs | A top-degree J-pullback is strongly supported on S_J; a nonzero restriction to a source n-cell is incompatible with ordinary vanishing near that cell. These statements are used as an explicit source-support check, not as a source-representation theorem for T. |
| Example 5.5.7, p.132, complete text reread | Records S_(p H) subset S_H by tropical-dimension monotonicity and the role of noncontracted top cells. These are known source-geometric ingredients, not a priority claim. Its pleasantness/properness assumptions for target calibrated pushforward are not imported or needed for the source argument here. |
| Sections 2.2.2 and 2.2.4-2.2.8, pp.64-65, including Lemma 2.2.8 and proof | Cell boundaries are lower-dimensional; the locally finite cell interiors partition the PL space; the relative interior of a top cell is open in a pure n-dimensional cell complex. This is the step that permits ordinary source isolation after using closedness of S_H in V. |
| Lemma 3.2.8(a)-(d), pp.76-77, complete proof | PL structures of contained source subsets are compatible, and their intersections are genuine PL subspaces. This controls C intersect lower-dimensional F/G cells without substituting tropical-image overlap for source intersection. |
| Corollary 2.2.14 and its proof, pp.67-68, with Proposition 2.2.13 read for the finite construction | A finite family of compact PL source subsets and coordinate maps on compact C admits an adapted finite decomposition. This is used only on the fixed compact H-cell C. |
| Theorem 12.8.2, pp.356-357, and Sections 12.9.1-12.9.5, pp.358-359, complete relevant statements/proofs | Identify maximal variation with the n-dimensional part of the analytic characteristic skeleton and establish the analytic G-tropical skeletal setting. The note keeps maximal-variation notation explicit rather than treating compact boundary domains as ordinary open domains. |
| Corollary 15.2.5, p.424, with local holomorphic-separation discussion p.423 | Ordinary smooth compact source cutoffs. They are chosen only after an actual ordinary open U has been obtained. |
| Section 14.3.2 and Definition 14.3.5, pp.407-408 | Canonical source calibration and its restriction compatibility. The proof comparison uses the same chosen coordinates for the current and canonical coefficients. |
| Definition 7.5.1 and Proposition 7.5.7, printed pp.172-175, with the intervening statements and complete proof read | Related existing theorem: skeletal-current descriptions compare on mutually noncontracted loci through an actual concatenated moment. Its literal hypothesis includes local affine separation; Section 15.2.4 gives local differential separation for the analytic setting. This note neither equates those hypotheses nor applies Proposition 7.5.7. Instead it assumes its own displayed actual-source formula (R) and proves the required comparison directly. |

The formula for the pulled-back ordered (n,n)-form is checked directly: the determinant occurs once in each differential block, giving its square, while change of Lebesgue coordinates contributes its absolute value. This is elementary exterior algebra, not an imported claim that ordinary F- and G-pullback forms agree near a skeleton.

Accordingly, the packet is detailed source-aware proof support for the present reduction, not a new-priority assertion about skeletal functoriality. Its explicit ordinary-open neighbourhood and coefficient normalization clarify the former S1 premise; they do not certify the separate representation theorem or upgrade differential separation to affine separation.

## Explicit representation premise and provenance

The representation packet is relative to the sibling directory `../p213_skeletal_packets_20260831/skeletal_representation/`:

| File | SHA-256 |
| --- | --- |
| `statement.tex` | `5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a` |
| `proof.tex` | `27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a` |

The statement is assumed in its actual-source form, including arbitrary source multipliers and no lower-cell residual coefficient measure. No claim of a fresh independent audit or reproof of (R) is made. The new geometry does not need it; the coefficient conclusion does. Choose coefficient-constant cell presentations for both T and the canonical calibration, refining as necessary. This does not assume shared-source isolation.

This author wrote the earlier actual-H supplement and supplied the new argument here after the parent's proposed question. Any review of the new packet must therefore be by another reviewer. Prior independent reviews do not automatically certify this new statement.

## Revalidated frozen historical inputs

At the start of this task, all eleven checksums in `../p213_product_common_moment_supplement_20260831/SHA256SUMS` passed. This includes its principal note and ledger, the historical branch note, both historical manifests, the representation bytes, and the two CLD source files. These inputs were not edited.

| Historical file | SHA-256 |
| --- | --- |
| `../p213_product_common_moment_supplement_20260831/COMMON_MOMENT_SUPPLEMENT.md` | `8036569f181c1c6f8a2e94f052328d9821e67b4852c73b17983fb8f36edafb6a` |
| `../p213_product_common_moment_supplement_20260831/SOURCE_AND_INPUTS.md` | `cc999ff9e57e27b245974098da34b26f627909ee4efb5238d06fb1108e5b089c` |
| `../p213_product_common_moment_supplement_20260831/MANIFEST.json` | `daf71d19d289cceacb0ce18f974f7acdaeec7484c8618cc291b40c2da9eb5491` |
| `../p213_product_common_moment_supplement_20260831/SHA256SUMS` | `335257105092b27c2df570acf37af59b033ee97ca25fcbee00ebb5322b9aea80` |
| `../p213_product_current_separation_research_20260831/RESEARCH_NOTE.md` | `d4f1458e0849164c1a45d168238467c13222ccae427493069ed97f43cd789b81` |
| `../p213_product_current_separation_research_20260831/MANIFEST.json` | `2afe7e91903a021751d59da7c02c7be1826dc3dc223a87f256a1482e7f58a440` |

The independent audit of those historical packets is preserved as history, not imported as acceptance of the new generic-isolation argument. No edit to its original wording is made. The new note is a separate general-n candidate rather than a retrospective change of scope.

## Limits and freeze evidence

The note asserts generic shared-source isolation only on a top H-cell with full-rank projection(s), and transfers coefficients there only under (R). Rank-drop H-top cells are not included in the lower-dimensional presentation exception. No canonical-calibration theorem is converted into a proof about arbitrary-current source representation, and no target-overlap theorem is converted into source overlap.

The packet has no new TeX/PDF build; byte/control-character checks and checksum verification are preservation evidence only. The freeze manifest pins the new note and ledger together with the representation, historical supplement/note, and primary-source files. No live manuscript or inventory change, git operation, or production call was performed.
