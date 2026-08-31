# Independent source-interface ledger

Date: 2026-08-31. Reviewer: /root/p081_weighted_repair_fresh.

This records primary statements actually inspected for the frozen wall-functional audit. Historical pass labels are not sources for the new proof.

## Local CLD primary source

Chambert-Loir--Ducros, arXiv:1204.6277v2 (25 July 2025), provided local PDF and extraction:

- /private/tmp/CLD25.pdf; 4659053 bytes; SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- /private/tmp/CLD25.txt; 2150944 bytes; SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

Directly read the following exact interfaces:

- 7.1.11, p.159: the abstract tropical-space proper pushforward construction. It relies on continuous pullback of compact tests and topological properness. In the candidate, actual moment pullbacks are ordinary smooth and properness is independently proved; no theorem asserting arbitrary moments are proper is cited.
- Chapter15 introduction and Proposition15.1.1/Corollary15.1.2, pp.421-422: ordinary forms use an ordinary open moment cover; G-forms instead use a G-cover. These distinguish the actual unit-log cutoffs from formal local functions. They do not license ordinary gluing solely from a formal Zariski cover.
- Remark14.4.3, p.410: viewing a finite-extension analytic space over the original field multiplies its canonical calibration by the full extension degree. It does not pull back an arbitrary current.
- Theorem14.6.2, p.412, and its opening proof: algebraically closed complete base; boundaryless, generically quasi-smooth pure n-dimensional germ; d_k(x)=n; norm-one analytic functions. The calibrated-cone equality requires full tropical dimension n and concerns canonical calibrations. This source is used to verify the exclusion, not as a slicing theorem.
- Theorem14.7.2 and Lemma14.7.3, pp.418-419: compact source satisfying (S_d), regular d-dimensional base, pure relative dimension, rigid reference point. The canonical fibre-tropicalization and finite-flat-degree conclusions do not compare unknown current coefficients.
- 17.7.1-17.7.2, pp.492-493: formal frames define a continuous metric; transition matrices and inverses are power bounded. This justifies continuous U_i and unit invariance, not their ordinary smoothness.

Full-page visual inspection: pp.159,410,412,418,421,422,493. Source text was additionally used for context and continuation.

## Local GRW primary source

Gubler--Rabinoff--Werner, Skeletons and tropicalizations, arXiv:1404.7044v3 (28 February 2016):

- /private/tmp/grw1404.7044v3_p213_residual.pdf; 679624 bytes; SHA-256 f7a909a8508032d8e2e0a0c6f9cd14b06f36cfa465c3e83fa5d40be6033678ad.
- /private/tmp/grw1404.7044v3_p213_residual.txt; 219817 bytes; SHA-256 851b1820299b758f96db87f37da1ce786b6d169597dc9bebb0f5e3208b1079af.

Read Sections1.1,3.1-3.4,4.14-4.15,6.3-6.10, including the principal-divisor/intersection proof through (6.10.6).

The standing complete algebraically closed field and proper strictly semistable-pair scope are retained. The completed-fibre/torus analysis motivates the local model but does not suppress original-field residue degrees. Section6.4 defines the alpha values as residual-curve line-bundle degrees. Definition6.7 includes the normal/tangential corrections; Remark6.7.5 warns that the higher-dimensional slopes need not be integers. Theorem6.9 restricts the rational divisor support to the chosen boundary. Its proof is a canonical intersection-degree argument, not an arbitrary-current weighted principal-divisor formula.

Full-page visual inspection: pp.16,21,22,23,24. The adjoining statements/proof continuation were read in the extraction. This is a scope check, not a fresh audit of all GRW.

## Stacks primary pages read online on 2026-08-31

[Tag04GK, Lemma10.153.7](https://stacks.math.columbia.edu/tag/04GK) gives the finite-étale lifting equivalence over a henselian local ring. Applied to κ(p)/k finite separable, it supplies the finite unramified DVR R_p. Its rank equals the residue degree. The candidate's residue-compatible map into the completed local ring also follows from Hensel's simple-root lifting. No algebraically closed residue field is required.

[Tag0AGX, Lemma15.44.9](https://stacks.math.columbia.edu/tag/0AGX), also read in [Section15.44](https://stacks.math.columbia.edu/tag/07NU), states the completion isomorphism for a flat local noetherian map with extended maximal ideal and identical residue fields. A local étale map with identical residue fields meets these hypotheses. After the coefficient extension, it verifies the completed standard-chart description. It is not by itself a global analytic product theorem; the convergent complete-ring maps give the actual tube identification.

[Section33.44, Degrees on curves](https://stacks.math.columbia.edu/tag/0AYQ), especially Definition33.44.1 and Lemmas33.44.9-33.44.12, uses Euler characteristics and point degrees over the given field. It handles the finite constant-field extension of a connected proper curve explicitly. A nonzero section of a line bundle gives an effective Cartier divisor. These facts support the candidate's degree factorization without assuming geometric connectedness or a degree-one point.

Only these bounded primary interfaces are asserted checked. No external literature priority or novelty determination is made.

## Independence and gate boundary

The new candidate reconstructs its argument in the actual strictly semistable neighborhood. The prior product/torsor work and representation/common-moment material were not substituted for missing steps. The reviewer authored the earlier torsor audit, not the present wall-functional candidate. (R) remains assumed only for the final source-coefficient interpretation. Actual comparison for arbitrary moments and general accessibility are not certified by this report.

No production service, git command, or live manuscript operation was used.

