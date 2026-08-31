# Source and scope ledger

Date: 2026-08-31. Author: /root.

The candidate is an analytic calculation for an explicitly given multiplicity tube, not an assertion that every regular SNC model or every analytic moment already has the needed global comparison geometry.

## Primary interfaces read

Chambert-Loir--Ducros, arXiv:1204.6277v2, 25 July 2025:
https://arxiv.org/abs/1204.6277v2.

The pinned local text was read directly. In particular:

- Section 12.1.5 and Lemma 12.1.6, pp.330-331: the Laurent Gauss norm and density of the rational function field in the completed residue field of a Gauss point.
- Corollary 12.1.8(b), p.332: a Gauss point has a unique preimage in the torus after a finite coefficient-field extension. Applied only to the torus, never to an arbitrary current.
- Proposition 12.2.8(iv), pp.335-336, and Sections 12.9.3-12.9.6, pp.358-360: actual characteristic skeleton, inverse image of the torus skeleton, piecewise immersion and full-dimensional membership.
- Lemma 14.1.5 and Proposition 14.2.2, pp.396 and 399: convenient cells and local constancy of local finite degree on their interiors. The preceding Remark 14.1.4(b) also directly applies because the source is boundaryless. These exact text passages were checked, including their page headers.
- Sections 14.3.2, 14.4.2-14.4.3, 14.5.2-14.5.3, pp.407-411: canonical calibration from local finite flat degrees, pushforward of calibration, finite-field factors and the target formula.

The primary degree-calibration argument is essential: an unknown current's coefficient is not declared to equal the canonical degree. It is the separate constant b in (2.5), and Section 7 explicitly invokes R to compare source-cell coefficients to that constant.

The proof of finite flatness includes its own bounded division argument. No generalized Weierstrass citation is used as a substitute for that calculation. The remaining analytic foundations are the standard generalized polyannular affinoid algebra, the criterion for a finite free affinoid algebra to define a finite flat map, the locality of finiteness on analytic-domain covers, and absence of relative boundary for finite morphisms. Their use is explicit so an independent reviewer can check these standard hypotheses.

The valuation argument uses only the fundamental inequality [F:H]>=e(F/H), not defectlessness or separability. After the inequality exhausts the full fibre-algebra dimension, that algebra is forced to be one field; no nonreduced fibre length is silently discarded.

## Conditional representation input

The exact frozen R packet is:

- sibling p213_skeletal_packets_20260831/skeletal_representation/statement.tex, SHA-256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a;
- its proof.tex, SHA-256 27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a.

R has an independent scoped review elsewhere, but not production acceptance. Its use here remains explicitly conditional. The stronger literal local-affine-separation terminology in CLD Definition 7.5.1 is not asserted; only the displayed source-current description identity is needed.

## Provenance and what is not imported

The preceding strictly semistable-wall candidate is:

sibling p213_general_snc_wall_residual_functional_research_20260831/RESEARCH_NOTE.md,
SHA-256 1c8011863516d8bdc900b3432b270c923126ee36d6600d915f714dc016553ae7.

Its reduced-fibre restriction motivated this local extension. It is not used to infer a nonreduced global divisor-functional theorem. In particular the completed local ring, weighted normal radii, finite residual bad set, ordinary cutoff gluing, and support inside the domain of T would all need a separate proof in any global extension.

The companion model-adaptation research being undertaken independently may identify further obstructions. It is not an input or an acceptance certificate for this candidate.

No source PDF was edited or generated. This author read extracted primary text rather than claiming a new visual inspection. No TeX/PDF build, production call, live chapter edit, atom retirement, or priority claim accompanies this packet.
