# Primary-source and dependency ledger

Date: 2026-08-31. Reviewer: /root/p081_weighted_repair_fresh.

This is a source-interface record for the exact torsor audit, not a new source-calibration proof. The local primary text was read directly. No PDF pages were rendered or visually inspected by this reviewer. The PDF hash records identity only; the author's separate visual-inspection log is not adopted as work performed by this reviewer.

## Primary source identity

Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025.

- Official version locator: https://arxiv.org/abs/1204.6277v2
- Local PDF: /private/tmp/CLD25.pdf; 4659053 bytes; SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- Local primary-source text: /private/tmp/CLD25.txt; 2150944 bytes; SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

The audit uses the 2025 version's actual locators, not transplanted numbering from the earlier preprint.

## Directly checked interfaces

| Locator (printed pages) | Audit use and scope check |
|---|---|
| §7.1.11 (159) | Support condition for current operations; the candidate proves analytic compactness of all pulled-back tests and primitives itself. |
| Proposition 7.2.8 and proof (161–162) | Positive functional to Radon-measure argument. In the candidate this is applied on the Euclidean target rectangle with an explicit cutoff bound, not as a claim that every bidegree-(0,0) current is an analytic-space measure. |
| Remark 14.4.3 (410) | Finite constant-field restriction multiplies canonical calibration by the extension degree. No ordinary-sheet assertion is part of this use. |
| Proposition 15.1.1 and Corollary 15.1.2 (421–422) | Ordinary-open versus G-local forms; actual unit functions on ordinary opens give the required smooth pullbacks. |
| §17.7.2 and Example 17.7.3 (493) | Formal orthonormal frames and continuous norm; explicit \(\mathcal O(1)\) metric formula. |
| §§18.1.1–18.1.3 (501) | Curvature defined from continuous local metric potentials modulo analytic log-units; tautological-section identity and sign. |
| §§18.1.5–18.1.6 (502) | Meromorphic section and Poincaré–Lelong sign. The model metric is continuous, and the section is nonzero meromorphic on the smooth curve, so the hypotheses apply. |
| Proposition 18.5.1 and Example 18.5.2 (527–528) | Proper relatively normal model, irreducible special fibre. No nefness assumption. Dimension-one formula and the \(\mathcal O(1)\) example. |

The auxiliary citations to §§17.1.2 and 17.1.4–17.1.5 in the candidate are not separately counted as direct fresh source readings by this audit. The needed formal-metric assertion was read in §17.7.2, including its continuity and frame-independence construction.

## Algebraic and elementary arguments checked in the candidate

The finite unramified coefficient extension and completed smooth local presentation, convergence on the disc exhaustion, compactness by projective-bundle compactification, normalization at the generic special-fibre DVR, finite horizontal-divisor specializations, dominant reduced monomial calculation, and Riemann–Roch positivity argument were checked in the actual proof. They are not attributed to a stronger theorem in the CLD citations. The case of an arbitrary line bundle is not reduced to a nef bundle.

## Predecessor and conditional dependencies

The product predecessor's statement/proof and its independent audit were read as context. Its exact hashes are independently checked in EXACT_BYTE_CHECKS.json. The current proof repeats the relevant collar, finite-support and principal-function arguments and adds the line-bundle normalization, radial support estimate, and shear calculation. This review does not use a predecessor acceptance label as a replacement for those checks.

The separate source-calibration statement was read to check the interface and its limits. Its statement SHA-256 is 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a, and its proof SHA-256 is 27a344a15fa7d22b2e88c07837aacfca0c978758c5bae5871c5af2d30e47999a. The latter is hash-checked as a frozen conditional input, not newly audited or accepted. Only the final interpretation on each displayed source Gauss plane uses that representation. No general current-separation statement, scalar rigidity, slice, pullback of an arbitrary current, or wedge with a curvature current is imported.

No source or candidate is promoted to production by this ledger.

