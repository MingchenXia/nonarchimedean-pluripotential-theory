# Source interfaces checked independently

Date: 31 August 2026. This ledger records the precise interfaces used in the conditional audit, not an audit of every proof in the cited works.

## MP

Primary: [arXiv:2409.06221v2](https://arxiv.org/abs/2409.06221v2), 18 September 2025. Read from /private/tmp/mp24.txt, SHA-256 0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62.

Checked Definition 2.3.1 (trivial valuation included), Definition 4.3.1 and following closure properties, Theorems 4.3.3 and 4.3.8, §4.4 including Definition 4.4.3, Theorems 5.1.4 and 5.1.7, §5.2, and Lemma 5.3.1 with its proof. The psh cone is a decreasing continuous-model completion; finite maxima and translations are allowed; divisorial points have finite values; comparison against an arbitrary usc majorant is available. Energy is monotone and normalized on constants. The finite-energy correspondence is used as an existing external input.

Lemma 5.3.1 is stated using normalized integrals. Its proof explicitly inserts the uniform sup–mean bound, so the supremum-slope use in the candidate is justified. The complete normalized bridge is written in CONDITIONAL_AUDIT.md.

## Xia operations

Primary: [arXiv:2312.17150v3](https://arxiv.org/html/2312.17150v3), version dated 22 October 2024; version-pinned HTML passages accessed on 31 August 2026. No local source-file hash is asserted for this web reading.

Checked §3.2, Definition 3.9, Lemma 3.10 and its recovery formula, the opening scope paragraph of §4, Lemma 4.2, Definition 4.7, Corollary 4.8, Definition 4.9 and Lemma 4.10. Section 4 explicitly uses compact Kähler spaces, not the preceding projective comparison scope. Maximum and decreasing-infimum formulas include endpoints. The infimum requires a finite lower endpoint bound. Positive-mass recovery is invoked only after the truncation mass is explicitly computed; its formula is the decreasing limit of perturbation levels.

## DXZ

Primary: [arXiv:2302.02541v3](https://arxiv.org/abs/2302.02541v3), 17 July 2024. Read from /private/tmp/dxz23.txt, SHA-256 7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244.

Checked §2.2 definitions, Lemma 2.4, Theorem 2.6, Definition 3.3 and transition formulas, §3.4 formula (43), and Theorem 3.17. The literal Legendre supremum is usc. Finite energy is defined from the recovered test curve and its normalized mass integral, with value −∞ outside the designated finite-energy domain.

## New assumptions and contextual inputs

A1 and A2 are assumed, not independently proved here. The reviewer authored the separate A2 candidate; see the disclosure in CONDITIONAL_AUDIT.md. The eight author-pinned parent inputs were hash-checked, not each advertised as fully mathematically audited. The source argument used here is the conditional proof itself plus the exact primary interfaces above. No source is being cited as already stating the unrestricted transcendental DXZ–MP conclusion.

