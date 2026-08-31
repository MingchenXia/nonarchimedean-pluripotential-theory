# Primary-source recheck and input ledger

Date: 31 August 2026. Independent reviewer: /root/p213_skeletal_hostile.

## CLD version and provenance

Antoine Chambert-Loir and Antoine Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2. The official version record was independently reopened: [arXiv version record](https://arxiv.org/abs/1204.6277v2). It identifies version 2 as 25 July 2025 and states 608 pages.

The mathematical source inspected is the pinned local PDF, not the abstract:

- /private/tmp/CLD25.pdf — 4659053 bytes, SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- /private/tmp/CLD25.txt — 2150944 bytes, SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

The PDF skill was read completely and used for read-only source inspection. Four existing page renderings from the candidate were independently viewed, not merely accepted from its author: printed pages 159, 160, 423 and 460. Their exact hashes occur in VALIDATION.json and the audit manifest. These are source QA images, not a new mathematical dependency or newly authored PDF output.

## Passages directly checked

| Source passage | Exact use in this audit |
| --- | --- |
| 1.1.2, p.22; 1.2.2-1.2.4, pp.22-23 | CLD's normalized J and top-degree symmetry/positivity; no raw Lagerberg swap sign. |
| 6.5.2, p.148 | Compact symmetric forms decompose into compact positive forms. Its support hypotheses hold for compactly supported forms in the good analytic setting; no global paracompactness assumption was silently added. |
| 7.1.1, p.155; 7.1.6-7.1.10, pp.156-159 | Test-degree convention, restriction, support and pairings whose support intersection is compact. |
| 7.1.11-7.1.13, pp.159-160 | Proper and proper-support pushforward; the literal degree-specific zero-extension definition; the unqualified differential sentence being challenged; fixed-degree extension uniqueness. |
| 7.2.1-7.2.12, pp.160-163 | Positive-current convention, positivity of pushforward, scalar Radon measures and coefficient measures, locally bounded Borel multiplication. |
| 7.2.14, p.163 | Explicit warning that arbitrary order-zero currents need not arise from measures; positivity must not be silently discarded from the Radon correspondence. No broader classification of currents is used. |
| 7.7.1-7.7.3, pp.186-187 | Signed transposition, derivative degree, anticommutation and boundaryless form-to-current identities. |
| 15.2.1-15.2.7, pp.423-424 | Ambient support avoidance; local differential separation; compact smooth cutoffs; density of smooth compact scalar tests. The analytic-subset support proof uses d_trop <= d_K and d_K <= dim(Z), not an intrinsic/ambient equality. |
| 16.7.1-16.7.4, p.460 | Current divisor degree, exact logarithm extension convention and positive Poincare--Lelong formula for a regular meromorphic function on a boundaryless analytic n-space; affine unit-log vanishing. |

The visual check confirms two literal matters: the last sentence of 7.1.12 has no displayed proper-support/output-degree restriction, and the proof of 7.1.13 contains complementary test-space indices inconsistent with its immediately preceding degree convention. The audit relies on the well-typed fixed-degree support proof and does not treat the unqualified commutation sentence as an input.

## Manuscript review scope

Chapter 14 input, read-only:

/private/tmp/nappt_p071_20260827/manuscript/parts/part2/ch14_currents.tex

160088 bytes; SHA-256 4dc28ea36f841d71ff6f082a6e458d8c9fec3d150c802f241d5430c37dc9a1c7.

The 216 exact numbered lines in the candidate's frozen excerpt were independently compared to the current source with no discrepancy: 380-457, 2190-2251 and 2280-2355. The complete frozen excerpt was read. The report treats only these bounded extension/support/proper-pushforward points, not the whole chapter.

Chapter 12 citation-scope input, read-only:

/private/tmp/nappt_p071_20260827/manuscript/parts/part2/ch12_tropicalization.tex

173808 bytes; SHA-256 44583781d3b66b217c7007bdaadb26ad5a88917416c4dcae7d26c2d48070f459.

The relevant proposition and proof around lines 1493-1520 were read to determine whether they supply the direct ambient-support theorem; the comparison is a locator/scope check only. This audit does not certify or replace the whole tropicalization chapter.

## Independence and exclusions

The diagnostic author is /root/p082_independent_reaudit; the initial example was supplied by /root. The present reviewer did not author the diagnostic and made no candidate edits. Earlier product, torsor, skeletal-representation or wall packets are not imported as inputs.

Mathematical acceptance here is confined to the exact note's degree/sign diagnostic, sufficient commutation conditions, positive closed-(0,0) modification correspondence and continuous-product proper-pushforward formulas. The all-current measure shorthand in the live Chapter 14 excerpt is expressly not endorsed. No intrinsic/ambient tropical-dimension equivalence, derivative-degree divisor removability, scalar rigidity, P21.3 conclusion, general-current pullback or production acceptance is claimed.

