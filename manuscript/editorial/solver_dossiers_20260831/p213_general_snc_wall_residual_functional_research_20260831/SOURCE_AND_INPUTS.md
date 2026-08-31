# Source, input, and scope ledger

Date: 2026-08-31. Author: /root/p213_skeletal_hostile.
This is provenance for an authored research candidate, not an independent audit.

## Primary sources checked

1. Chambert-Loir--Ducros, arXiv:1204.6277v2, 25 July 2025:
   https://arxiv.org/abs/1204.6277v2
   PDF /private/tmp/CLD25.pdf
   SHA256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
   Text /private/tmp/CLD25.txt
   SHA256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

2. Gubler--Rabinoff--Werner, “Skeletons and tropicalizations,” arXiv:1404.7044v3, 28 February 2016:
   https://arxiv.org/abs/1404.7044v3
   PDF /private/tmp/grw1404.7044v3_p213_residual.pdf
   SHA256 f7a909a8508032d8e2e0a0c6f9cd14b06f36cfa465c3e83fa5d40be6033678ad.
   Text /private/tmp/grw1404.7044v3_p213_residual.txt
   SHA256 851b1820299b758f96db87f37da1ce786b6d169597dc9bebb0f5e3208b1079af.

3. Stacks Project Lemma10.153.7, Tag04GK:
   https://stacks.math.columbia.edu/tag/04GK
   Read directly for the equivalence between finite étale extensions of a henselian local ring and finite étale residue algebras. Here it supplies the unramified R_p with residue κ(p), because k is perfect. The completed local presentation also uses the defining infinitesimal lifting property of an étale map with identical residue fields, explained in the proof rather than an assertion of ordinary-open sheets.

The current official arXiv version records were checked. No literature claim of novelty or priority is made.

## Exact primary interfaces and use boundaries

| Source | Exact use |
| --- | --- |
| CLD7.1.11, p.159 | Proper pullback sends compact test forms to compact test forms and defines a current pushforward. The needed properness of q_p is proved directly using the actual polyannulus; this paragraph is not misquoted as a general properness theorem for arbitrary moments. |
| CLD14.4.3, p.410 | Canonical calibration on one finite-coefficient-field analytic domain, viewed over the original field, is multiplied by the full field degree. |
| CLD14.6.2, pp.412--417, especially the statement on p.412 | Checked for its algebraically closed, norm-one, full-tropical-dimension hypotheses and canonical-cone conclusion. It is NOT used to restrict T to a residual curve. |
| CLD14.7.1--14.7.3, pp.417--420 | Checked for compactness, (S_d), regular base, pure relative dimension, rigid reference point, and canonical finite-flat degree conclusion. Not a product isomorphism or unknown-current transport theorem. |
| CLD15.1.1, pp.421--422 | Ordinary smooth forms versus G-local data; formal Zariski charts are not used as an ordinary open cover. |
| CLD17.7.2, p.493 | Formal frames give a continuous metric and norm-one transition functions. Used for the continuous model radii U_i, not to declare them ordinary smooth or globally differentiate them. |
| GRW1.1,3.1--3.2, pp.1,8--9 | Exact algebraically closed global scope and relation to DVR semistable models. The new theorem explicitly starts with its original DVR model. |
| GRW4.14--4.15, pp.15--16 | Actual completed formal-fibre/torus analysis under the source hypotheses. The new original-field tube computation retains R_p and residue degrees. |
| GRW6.3--6.7, pp.20--22 | Proper residual curve, normal-component intersection degrees, alpha terms, and corrected slopes. |
| GRW6.9--6.10, pp.23--25 | Canonical principal-divisor intersection identity, not an arbitrary-T divisor functional. The new weighted identity is proved by a compact primitive instead. |

The relevant extracted text was read directly. The PDF skill was read and used for read-only page inspection. New images of printed CLD pp.412,418 and GRW pp.21,23,24 were rendered in /private/tmp/p213_snc_wall_source_visual.rdKz3V and all five were viewed. The renderer reported a font-cache write warning on one call but exited successfully; the resulting page was present, complete, and legible. No permissions were weakened and no alternative cache location was introduced. No source PDF was modified.

Two available atomic skills concerning index-zero cancellation and graph-component isolation were inspected with their complete reference cards. Their hypotheses concern respectively a global signature-index inequality and limits of degree-one complex graph cycles, neither present here. They were not used as mathematical inputs.

## Preserved earlier work and authorship

All paths below are under manuscript/editorial/solver_dossiers_20260831.

- p213_annular_torsor_residual_functional_research_20260831/statement.tex:
  19baf4828b51e2b36370a2ececd41ad5802f01e3cf41c90f00df9b8bacec773a.
- Its proof.tex:
  f851830312841ef4d8825ba4b049a718a16820ef3888263721278bf7a06c99fe.
- Its CURVATURE_AND_EXAMPLES.md:
  b88523c7d72f143f2093d3803d6b64886ac7d8ff0d872a4f30678df41a543c0a.
- p213_annular_torsor_residual_functional_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md:
  96d669f15ee36f83cb423b674a3203b24b0545c76fcd268fbed71536c1cf7d45.

The same author wrote the torsor and present proofs; their relationship is disclosed. The torsor audit is a separate review by p081. The present proof reconstructs its current argument in the new geometry and is not independently certified by that old audit.

The source-calibration representation remains the explicit input R only for the last interpretation:

- p213_skeletal_packets_20260831/skeletal_representation/statement.tex:
  5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a.
- Its proof.tex:
  27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a.

The genuine common-moment comparison is preserved separately:

- p213_product_common_moment_supplement_20260831/COMMON_MOMENT_SUPPLEMENT.md:
  8036569f181c1c6f8a2e94f052328d9821e67b4852c73b17983fb8f36edafb6a.

This packet does not assume that its same-source isolation hypotheses automatically hold for every analytic moment.

Root's pre-draft feedback supplied two important checks: use generators of Cartier ideals in O_{𝒳,η_C}, not just component-order vectors; and distinguish the chosen C-tube from the tube of the entire intersection. The proof incorporates them explicitly. The bounded candidate itself is authored here, and a fresh independent review is still required.

## New result versus unresolved geometry

Established within the supplied written argument, pending independent audit:

- actual original-field p-tube coefficient construction in dimension n;
- uniform valuation domination of deformation terms after bounding ALL normal radii below;
- compact ordinary primitive on the whole proper residual-curve tube;
- annihilation of every residual principal divisor and b_T(p)=c[κ(p):k].

Conditional only:

- interpretation as source-calibration ratios using R;
- transfer to a different moment when an independently justified common-source comparison is available.

Not proved:

- realization of arbitrary analytic walls by such an original-field model;
- current slicing, pullback through alterations, all-cell accessibility, or full P21.3;
- a general theorem for non-discrete fields or nonreduced/non-strict semistable models.

No frozen input, live manuscript, production service, or git state was changed. No TeX or PDF artifact was compiled for this Markdown research packet.

