# Primary source ledger for the mixed-branch independent audit

Date: 31 August 2026. Reviewer: `/root/p082_independent_reaudit`.

## Exact primary version

Antoine Chambert-Loir and Antoine Ducros, *Formes differentielles reelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025, 608 pages. The official version record was reopened for this audit: <https://arxiv.org/abs/1204.6277v2>.

- Local PDF `/private/tmp/CLD25.pdf`: `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
- Exact extracted text `/private/tmp/CLD25.txt`: `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`.

The primary mathematical passages below were read directly in that text during this audit. There is no fresh PDF rendering or candidate PDF visual claim.

| Exact passage | Audited use |
| --- | --- |
| Section 7.1.11, printed p.159 | Proper pullback of compact target supports is required when defining a target current. The candidate verifies compact preimages directly on both domains and proves compact support of the connecting primitive separately. |
| Section 7.2.6 and Proposition 7.2.8 with its proof, pp.161-162; Proposition 7.2.9, p.162 | Positivity and a fixed-compact-support sup-norm bound give the scalar Radon functional used in the proof. This is not an assertion that the full analytic bidegree-(0,0) current is a measure. |
| Opening convention of Section 12.6, printed p.350 | An analytic space of level n is topologically separated of dimension at most n. No geometric smoothness or separability convention is hidden in the canonical-calibration setup used here. |
| Section 14.3.2, printed p.407, including the complete construction and independence paragraph | Canonical calibration is computed from local degree and the primitive coordinate volume. The coordinate moments on the displayed L-torus domains have local degree one. The separate common-moment argument in this source is not imported as a representation theorem for an arbitrary current. |
| Remark 14.4.3, printed p.410, complete statement | The canonical calibration of the same finite-extension analytic space viewed over the base field is multiplied by the full extension degree. It includes finite inseparable and ramified extensions; no ordinary-sheet decomposition is asserted. |
| Proposition 15.1.1(b) and Corollary 15.1.2, pp.421-422 | Ordinary forms and logarithms of analytic units use actual moments on ordinary open sets. These passages were also directly read in the preceding source audits; no G-cover-to-ordinary-cover inference is being added. |
| Section 18.1.2, printed p.501, complete paragraph | The source explicitly says logarithms of analytic units are smooth and have d'd'' equal to zero, as used in differentiating the primitive. This is not merely a curvature-current assertion with an omitted smooth-form step. |

Only these basic interfaces are attributed to CLD. The particular coefficient equality is established by the candidate's explicit source-supported calculation; neither novelty nor prior literature coverage of that equality was adjudicated here.

## Standalone versus optional predecessor

The standalone proof does not depend on any prior P21.3 research theorem or on the source-calibration representation. It needs only the displayed analytic domains, elementary norm identities, positive scalar distributions, closedness, and the canonical degree formula.

The optional application in SOURCE_INTERFACE.md invokes the following frozen predecessor, all relative to `../p213_product_current_separation_research_20260831/`:

| File | SHA-256 |
| --- | --- |
| `RESEARCH_NOTE.md` | `d4f1458e0849164c1a45d168238467c13222ccae427493069ed97f43cd789b81` |
| `SOURCE_LEDGER.md` | `568f7a92f88e18821d3698c8fd35499440f3bcffc106dfb3fffc32f19b8de578` |
| `MANIFEST.json` | `2afe7e91903a021751d59da7c02c7be1826dc3dc223a87f256a1482e7f58a440` |

This reviewer authored that predecessor. The present report therefore checks only the logical substitution from its explicit source isomorphism and B_T(p,N)=N b_T(p), not a purported fresh independent proof of those authored premises. Its Section 5.2 rank obstruction is preserved, not retracted: the new coefficient identity is obtained by an additional closedness test. The parent and another agent have separately reviewed the predecessor; their conclusions are not used as a replacement for this audit of the new standalone core.

The actual-common-moment supplement and its representation premise play no role in the candidate's new coefficient equality. No all-moment support/separation assertion is accepted by this audit.

## Preservation and evidence

The audit manifest pins the report, this ledger, the frozen candidate manifest and all of its 21 recorded entries, retaining their original roles. The manifest and SHA256SUMS are integrity evidence only. The candidate's original source code, complete native build logs, formatting-history files, and all predecessor packets were left untouched. No new TeX/PDF build was performed and no production submission or git operation was made.
