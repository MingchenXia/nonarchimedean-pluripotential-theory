# Independently checked source matrix

Date: 31 August 2026. Reviewer: /root/p082_independent_reaudit.

The audit's own reasoning is in INDEPENDENT_EXACT_BYTE_AUDIT.md. This matrix separates primary source support from conditional research inputs. No author's self-check is used as acceptance.

## Primary algebraic geometry

| Exact primary source | Passage read | Audited interface |
| --- | --- | --- |
| [Stacks 0CBN](https://stacks.math.columbia.edu/tag/0CBN) | Definition 41.21.1 and Lemma 41.21.2, including proof | SNC SUPPORT supplies actual regular component parameters and regular intersections of expected codimension. |
| [Stacks 04GK](https://stacks.math.columbia.edu/tag/04GK) | Lemma 10.153.7 and proof | Henselian finite-etale residue lifting. The candidate separately constructs the map into Ahat_p by a simple-root lift. |
| [Stacks 07NU](https://stacks.math.columbia.edu/tag/07NU) | Lemmas 15.44.1 and 15.44.4 with proofs | Completion preserves the local dimension and regularity used in the presentation argument. |
| [Stacks 00NN](https://stacks.math.columbia.edu/tag/00NN) | Lemmas 10.106.1-10.106.4 with proofs | Regular local domains, parameter quotients, and the equal-dimension surjection argument. |
| [Stacks 0B5B](https://stacks.math.columbia.edu/tag/0B5B) | Equations 53.5.0.1-53.5.0.3 and Lemma 53.5.2 | Euler characteristic/degree formula over the given field; no geometric-connectedness hypothesis is smuggled into the divisor functional. |

These pages were read directly on 31 August 2026. No raw-HTML local hash is claimed. The regular power-series source ring over the DVR and the explicit successive-approximation surjection are also checked directly in the audit.

## Formal completion and the actual tube

Vladimir G. Berkovich, Vanishing cycles for formal schemes. II, Inventiones Mathematicae 125 (1996), 367-390. [Author-hosted PDF](https://www.wisdom.weizmann.ac.il/~vova/Inven_1996_125_formalII.pdf).

Read the complete-DVR standing hypothesis, Section 1 generic-fibre construction for special formal power-series quotients, and Proposition 1.3 with proof, printed pp.369-372. The construction includes open unit-polydisc variables; the proposition identifies completion along a closed subscheme with its actual analytic tube. It does not assume reduced special fibre or a semistable chart. The distinction between generic fibres of formal opens and ordinary tubes is retained.

The web reader returned the relevant text. Its two screenshot requests returned textual references without inspectable image content; no remote-PDF visual QA or local byte hash is asserted.

As a corroborating exposition, I read Michael Temkin's existing local Introduction to Berkovich analytic spaces, preliminary 2010 summer-school lecture notes: Section 5.2.4, especially Fact 5.2.16, and the preceding special-formal generic-fibre construction. Local files are /private/tmp/Temkin_lecture_notes.pdf and /private/tmp/Temkin_lecture_notes.txt, pinned in the manifest. This preliminary exposition is supplementary; the Berkovich primary proposition is the source interface above.

## CLD primary version

Antoine Chambert-Loir and Antoine Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, [arXiv:1204.6277v2](https://arxiv.org/abs/1204.6277v2), 25 July 2025.

- /private/tmp/CLD25.pdf: SHA256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- /private/tmp/CLD25.txt: SHA256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

| Passage independently checked | Exact scope |
| --- | --- |
| Remark 14.4.3, p.410 | Restriction of scalars multiplies canonical calibration by the full finite degree; no ordinary-sheet interpretation. |
| Sections 14.5.2-14.5.3, pp.410-411 | Calibration from actual finite flat degree; the global theorem imports this through L. |
| Corollary 15.2.5, p.424 | Compact ordinary smooth source cutoffs in the locally holomorphically separated setting. |
| Sections 17.7.1-17.7.4, pp.492-493 | Continuous formal metrics, norm-one frame changes, and tensor compatibility; no global smoothness of model radii. |

The current argument uses compact test-form extension and closedness, not the unqualified zero-extension/differentiation sentence of 7.1.12. No stronger source-representation theorem was read into these passages.

The PDF skill was read fully for read-only inspection. Independently viewed existing complete renders:
- /private/tmp/p213_nonreduced_wall_source_visual.OehlD5/cld-410.png;
- /private/tmp/p213_nonreduced_wall_source_visual.OehlD5/cld-493.png.

Their bytes are checked against the author's frozen manifest and pinned in this audit. The extracted text and visible degree/metric formulas agree. No new PDF was authored or re-exported, and no TeX build of the Markdown note was attempted.

## Conditional research interfaces, not primary-source replacements

L is p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md, SHA256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a. I checked the exact analytic statement and the added Sections 6-7 hypotheses. The global proof uses Sections 2-5 for finite projection and proper target pushforward, and Sections 6-7 only for the final cell interpretation. L is assumed here, not independently reproved.

R is the displayed source representation in p213_skeletal_packets_20260831/skeletal_representation:
- statement.tex: 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a;
- proof.tex: 27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a.

R remains explicit and unverified by this audit. The source-isolation/no-lower-cell formula needed by L is not replaced by a claim that arbitrary analytic chart refinements are accessible.

The earlier reduced-wall proof is provenance, not a black box for multiplicities. The reviewer's model-adaptation note is not a mathematical input to this candidate or audit.
