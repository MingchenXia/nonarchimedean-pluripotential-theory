# Source ledger: zero-extension derivative-degree diagnostic

Date: 31 August 2026. Author: `/root/p082_independent_reaudit`.

## Primary source and exact scope

Antoine Chambert-Loir and Antoine Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025, 608 pages. Official version record reopened in this task: <https://arxiv.org/abs/1204.6277v2>.

- `/private/tmp/CLD25.pdf`, 4,659,053 bytes: SHA-256 `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
- `/private/tmp/CLD25.txt`, 2,150,944 bytes: SHA-256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

| Passage actually checked | Use and qualification |
| --- | --- |
| Definition 7.1.1 and Sections 7.1.4-7.1.13, pp.155-160 | Bidimension is the test degree; restriction, proper-support pairings, proper pushforward, the exact extension definition, and fixed-degree removability. The unqualified final differential sentence of 7.1.12 is the object of the diagnostic, not an input theorem. The complementary-index inconsistency printed in the proof of 7.1.13 is recorded separately. |
| Proposition 15.2.1, p.423 | Ambient G-form support avoids a closed analytic subset of dimension less than max(r,s). This is stronger than only the vanishing of a restricted form. The proof uses d_trop<=d_K and the dimension-vanishing proposition 3.3.6. |
| Sections 7.7.1-7.7.3, pp.186-187 | Differential signs, lowering of bidimension, anticommutation, and the boundaryless form-to-current identity. Restriction and proper pushforward commutation are also checked directly on compact tests, independently of 7.1.12. |
| Sections 16.7.1-16.7.4, p.460 | Defines the unique extension of the logarithm current, states d'd''[log|f|]=delta_div(f) for a regular meromorphic function on a boundaryless analytic n-space, and proves the curvature vanishes on its invertibility locus. Applied only to the regular coordinate z on the smooth analytic affine line. |
| Proposition 7.2.8-7.2.9 and Sections 7.2.11-7.2.12, pp.161-163 | Positive currents give Radon coefficient measures; locally bounded Borel multiplication is defined. The diagnostic uses only finite continuous functions and supplies the continuous projection-formula proof via measures. No statement that an arbitrary order-zero current is a Radon measure is needed. |
| Corollaries 15.2.4-15.2.7, pp.423-424 | Local differential separation in the analytic setting, smooth compact cutoffs, and density in continuous compact tests. These suffice for the cutoff detecting delta_0 and for equality of coefficient Radon measures. No local affine-separation hypothesis or skeletal representation theorem is used. |

The bounded logarithm example and degree table were checked directly, including the positive sign and rational degree of delta_0. The safe modification transport proof is an explicit consequence of the fixed-degree support theorem and actual-isomorphism restriction, not a cited general pullback theorem. Continuous-product formula (7) in the note is proved by Radon coefficient measures and proper pushforward. Formula (9), the potentially stronger zero-extension identity in derivative degree, is explicitly not established in the divisor case.

## Printed-page visual check

The PDF skill was read and used for read-only primary-source inspection. System Poppler rendered four complete pages, and all four images were opened and checked:

- `/private/tmp/p213_zero_extension_pdfqa_hOf3h1/cld-159.png`: Section 7.1.12 is visibly unqualified; no missing extraction symbol or line supplies the needed differential-degree restriction.
- `/private/tmp/p213_zero_extension_pdfqa_hOf3h1/cld-160.png`: Lemma 7.1.13 and its displayed test-space indices are visibly present.
- `/private/tmp/p213_zero_extension_pdfqa_hOf3h1/cld-423.png`: Proposition 15.2.1(b) is a statement about AMBIENT support, not only pullback vanishing.
- `/private/tmp/p213_zero_extension_pdfqa_hOf3h1/cld-460.png`: Sections 16.7.2-16.7.4 visibly give the logarithmic extension convention, the positive Poincare--Lelong sign, and vanishing on the invertibility locus.

Physical PDF page numbers equal printed numbers for these pages. No source PDF was edited or re-exported, and no new PDF artifact is claimed. The rendering directory is temporary QA material, not a production output or a mathematical dependency separate from the pinned primary PDF.

## Manuscript input and precise boundaries

Live source inspected read-only:

`/private/tmp/nappt_p071_20260827/manuscript/parts/part2/ch14_currents.tex`

SHA-256 at inspection: `4dc28ea36f841d71ff6f082a6e458d8c9fec3d150c802f241d5430c37dc9a1c7`.

Reviewed in particular: lines 350-485 (support pairing, extension lemma, rigid-invisibility corollary and differential convention), 2190-2251 (restriction warning and support theorem), 2280-2355 (proper pushforward calculus), and 2350-2455 (the existing general-pullback firewall). The frozen numbered excerpt contains the task-relevant lines 380-457, 2190-2251 and 2280-2355; no text in the live chapter was changed.

The cited Chapter 12 proposition `prop:analytic-tropical-dimension`, lines 1493 onward, was read to check that the Chapter 14 support proof's citation is not itself the direct ambient-support statement. This is a locator/scope finding only; no broad Chapter 12 audit is included.

The parent supplied the initial punctured-line challenge. This diagnostic independently verifies that challenge and supplies the safe degree-qualified formulations. It does not establish an authors' erratum, assume unpublished corrections, audit all uses of extension in the manuscript, or retire P21.3. Earlier frozen current-transfer and representation packets remain untouched and are not imported as acceptance. No live, git or production operation was performed.
