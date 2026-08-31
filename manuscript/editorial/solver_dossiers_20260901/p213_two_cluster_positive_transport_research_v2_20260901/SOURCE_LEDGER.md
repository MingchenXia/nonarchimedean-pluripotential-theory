# Exact source and premise ledger: two-cluster positive transport

Date: 1 September 2026. Author: /root/p082_independent_reaudit.
This is an authored conditional research packet, not an independent acceptance report.

## 1. Exact current-theoretic premises

All paths below are absolute in the companion manifest. The common editorial root is
/private/tmp/nappt_p071_20260827/manuscript/editorial/.

| Input | Exact principal bytes | What is used | What is not imported |
|---|---|---|---|
| L: solver_dossiers_20260831/p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md | SHA256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a | Sections 2-5: full coordinate-tube properness and canonical degree; all exponents zero is allowed. All applications here have K unchanged, m=1 and formal unit 1. | A current on a full tube is not fabricated from its restriction to W; no alteration or current base change. |
| O: solver_dossiers_20260831/p213_ordinary_open_outer_collar_research_20260831/RESEARCH_NOTE.md | SHA256 f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b | Sections 1 and 6-8: local collar coefficient at a Q-independent normal germ; finite principal-divisor test compactly supported inside the current's actual W. Sections 1-2 supply the actual model/tube hypotheses. | No whole-tube V current conclusion. No R theorem or arbitrary-cell capture. |
| Q: solver_dossiers_20260901/p213_proper_target_open_comparison_20260901/RESEARCH_NOTE.md | SHA256 35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec | Sections 2-4, read completely: current on full inverse image of any connected ordinary target open in L's positive slice; displayed R gives source rather than aggregate coefficients and arbitrary compact source multipliers. | Not applied directly to arbitrary signed u. The new note translates each bounded-below torus region into the exact positive slice and proves overlap consistency. |
| Displayed R: solver_dossiers_20260831/p213_skeletal_packets_20260831/skeletal_representation/statement.tex | SHA256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a | ONLY the displayed source-multiplier identity eq:p213-source-cell-formula, no lower-cell residual, for the explicit moments and ordinary restrictions in the new note. Statement read directly. | Neither its proposed proof nor unverified local-affine-separation language is certified. No CLD 7.5 theorem is used to establish R. |

The R proof, SHA256 27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a, is pinned for provenance only, not as a theorem proved or re-audited here. Prior independent reviews of L and O do not verify the new assembly. O is author-related; its use remains explicit.

All three principal divisors in the new proof are on actual k-rational projective lines. Thus the only degree values needed are one. General Riemann-Roch, non-geometric-connectedness, ramified residue degrees, and nonreduced multiplicity formulas are not new claims here.

## 2. Primary algebraic sources checked directly

The following primary Stacks pages were read on 1 September 2026.

- [Strict normal crossings, tag 0CBN](https://stacks.math.columbia.edu/tag/0CBN), Definition 41.21.1 and Lemmas 41.21.2-3: parameter description, regular closed intersections of the expected codimension, and smooth base change. Used to identify the selected whole connected curve and the product model. Regular intersections have disjoint irreducible components; an exceptional P1 component cannot meet another curve component inside that same regular intersection.
- [Blowing up, tag 01OF](https://stacks.math.columbia.edu/tag/01OF), Lemmas 31.33.2, .4, .9, .13: Rees charts, isomorphism away from the center, integrality, and projectivity for a finite ideal. These justify actual proper vertical modifications. The new note gives the two coordinate substitutions and SNC check itself.
- [Regular local rings, tag 00NN](https://stacks.math.columbia.edu/tag/00NN), Lemmas 10.106.1-3: associated graded polynomial ring, domain, and regular quotients by parameter subsequences. These are the commutative-algebra ingredients for the two-parameter center calculation.
- [Blow up formula, tag 0FVA](https://stacks.math.columbia.edu/tag/0FVA), ONLY the beginning of the proof: for a regular immersion the associated graded normal algebra is the symmetric algebra of the conormal bundle; hence its Proj, the exceptional divisor, is the corresponding projective bundle. No Gysin formula is used. In rank two, the fibre above the tracked k-point is the whole P1.
- [Torsion-free modules, tag 0539](https://stacks.math.columbia.edu/tag/0539), Lemma 15.22.10: torsion-free over a valuation ring implies flat. Applied to integral R-models retaining a nonempty generic fibre.

Scope check: Stacks Lemma 37.17.3 (0FUT), also encountered during source search, assumes a closed immersion of schemes both smooth over the same base. It is NOT used to claim that a semistable model is smooth over R. The proof here instead uses actual regular coordinate centers and Rees charts. No resolution theorem, alteration theorem, root extraction, or original-field semistable-reduction assertion is needed.

The exceptional whole-curve calculation in Section 6 is explicit: other selected divisors are transverse to the center, so their pullbacks cut the exceptional projective bundle down to the full P1 fibre over the tracked point. The next center is at its zero section, avoiding the old infinity section. This is an actual global closed-intersection argument, not merely the local equation z-c=pi*zeta.

## 3. Primary analytic source checked directly

Chambert-Loir and Ducros, arXiv:1204.6277v2, 25 July 2025:
[primary arXiv record](https://arxiv.org/abs/1204.6277).

Exact local files:
- /private/tmp/CLD25.pdf, SHA256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- /private/tmp/CLD25.txt, SHA256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

The current turn directly read the extracted primary text at:
- 12.1.6 and 12.1.9, printed pp331-332: torus Gauss skeleton and its tropical parameterization.
- 12.1.10-12.1.12, printed p333: relative Shilov/Gauss section into the ACTUAL analytic product and its continuity. The new proof gives the seminorm formula and does not identify all product points with pairs.
- Proposition 14.2.2, printed p399: convenient source-cell canonical degree. Here the coordinate analytic maps are degree-one torus coordinate charts. The canonical coefficient one also follows directly from the explicitly assumed L/Q specialization.
- Corollary 15.2.5, printed p424: compact ordinary smooth cutoff equal to one near a prescribed compact inside an ordinary open. Good algebraic analytifications are locally holomorphically separated, so it applies on all domains used here.

The affine source identities in the new note hold on entire ordinary domains. No form is transported using only equality of tropical images. Q already contains the dense-Gauss-source isolation argument needed to read individual represented coefficients.

No new PDF was generated or rendered in this task. Source text inspection and structural Markdown checks are not described as visual PDF QA. No TeX compile is claimed; this packet is a complete mathematical Markdown proof-support note.

## 4. Frozen diagnostic preserved, not used as a coefficient theorem

The predecessor
solver_dossiers_20260901/p213_common_constant_propagation_diagnostic_20260901/DIAGNOSTIC.md,
SHA256 0961f3f5b771605e7acf580e490dc404a95f95447b3291b55fcc10b4a97b304f,
is unchanged.

It proves the fixed-F source separation and exhibits H's rank-drop strips, but gives no equality of current coefficients there. Sections 4-8 of the NEW note now build three actual proper residual curves and the finite compact forms that establish those particular equalities, conditionally on L/O/Q/R. We do not replace the predecessor's warning by a general connectedness claim.

The frozen generic-common-moment and arbitrary-source-cell capture packets are not new theorem premises here. All moment changes used in this proof are given by the explicit full-source affine identities (2.4) and (8.4).

## 5. Provenance and boundaries

The author wrote O and the earlier diagnostic, so this is a new authored assembly rather than independent certification. Root supplied the task and the warning about Q's positive target slice; the detailed coordinate model chain, overlap tests, infinity chart, and finite comparison proof were written in this packet. A different reviewer must audit it.

A skill named degree-topform-graph-component-isolation was inspected completely with its required research card. Its actual setting is limiting complex-analytic graph cycles, not the present current problem; it was explicitly rejected as inapplicable and contributes no mathematical premise or conclusion.

No broad current-representation theorem, all-moment comparison, arbitrary-source-cell accessibility, general-K statement, priority claim, or P21.3 resolution is asserted. Only new files in this exclusive dossier are authored.


## Version-2 correction provenance

The frozen v1 Section 8 derivative wording was independently flagged by /root/p213_skeletal_hostile and corrected in this separate version. The reviewer approved the exact proposed replacement before freeze. Section 5 receives only the parallel chi'(t)=0 clarification. See REVISION_RECORD.md for the exact old/new text and unchanged-v1 pins. All primary sources and L/O/Q/displayed-R premises above are unchanged; no new source theorem is imported.

