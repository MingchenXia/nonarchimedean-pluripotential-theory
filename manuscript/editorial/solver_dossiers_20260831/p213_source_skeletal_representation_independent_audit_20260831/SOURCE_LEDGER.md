# Primary-source interface ledger

Date: 2026-08-31. For the exact independent audit of the sibling source-skeletal representation packet.

## Version and identity

Primary: Antoine Chambert-Loir and Antoine Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277, version dated 25 July 2025.

- /private/tmp/CLD25.pdf — 4659053 bytes — SHA-256 5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719.
- /private/tmp/CLD25.txt — 2150944 bytes — SHA-256 021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e.

The direct local text was read at every interface below. Whole-page PDF inspection covered printed/source PDF pages 68, 76, 77, 108, 127, 128, 129, 173, 464, and 465; see VISUAL_QA.json. The PDF has 608 pages. Source quotations in this ledger are kept to short identifying phrases; the mathematical descriptions below are paraphrases.

## Interfaces

| CLD25 locator | Use and checked scope |
| --- | --- |
| §1.2.2–1.2.6; Proposition1.2.13 | Positive/symmetric/strongly-positive cone distinctions; the positive cone has an interior reference form in the symmetric vector space. Do not replace this by a false strongly-positive spanning assertion. |
| §1.5.1–1.5.5, pp.33–35 | Interleaved coordinate top forms and positive volume integration conventions; no hidden orientation sign in b_C≥0. |
| §2.2.2–2.2.15, especially Lemma2.2.8, Remark2.2.12, Proposition2.2.15, pp.65–68 | A top-cell interior is open in a pure n-dimensional locally finite decomposition. Paracompact PL spaces admit locally finite compact chart domains and compatible compact-cell decompositions. Subordination preserves injectivity of a piecewise immersion. |
| Lemma3.2.8(c)–(d), pp.76–77 | A compact ambient domain intersects a PL subset in a PL domain; ambient PL coordinates restrict to PL functions. PL-in-a-PL-subset gives ambient PL. This is the bridge to ALL G-tropical charts. |
| §3.5.1–3.5.5 | Positivity of forms and its compatibility with pullback/restriction and appropriate wedge products. |
| Definition4.5.1 and Example4.5.2, pp.108–109 | Arbitrary constant per-top-cell volume calibrations glue to a G-locally constant calibration. Intersections of dimension<n carry no n-calibration data. Nonnegative includes zero. |
| Definition5.2.1 and Proposition5.2.5, pp.123–125 | Closedness, purity and piecewise immersion for the maximal-variation skeleton. Used on the analytic G-tropical vertebrated space. |
| §5.3.1, Lemma5.3.4, Proposition5.3.6, pp.127–129 | Strong support for F-tropical forms with max(p,q)=n; module/wedge/differential stability; restriction to the strong-support skeleton detects vanishing. These give source cutoff cancellation and tangentiality, not just measure support. |
| §6.1.1–6.1.6; §6.2.3 | Affine functions form a smaller ordinary-local sheaf within PL functions; affine separation implies differential separation, not conversely by definition. Both local notions are distinguished. |
| §7.1.9–7.1.11, pp.158–159 | Current support, continuous action on forms meeting support compactly, and pushforward for compactly supported currents. This justifies F_*(χT), not unrestricted pushforward of T under a nonproper F. The packet's construction can equally be read directly through the compact-source test formula. |
| Propositions7.2.8–7.2.9 and §7.2.11, pp.161–163 | Positive current/positive form coefficient measures, order-zero bounds, and local differences for general coefficients. Smooth density yields uniqueness. |
| Definition7.5.1, pp.172–173 | Exact displayed description uses arbitrary compact smooth source multipliers. Literal opening assumes local affine separation; the packet verifies differential separation only. The audit accepts its directly proved formula, not an unproved stronger separation assertion. |
| Examples7.5.2–7.5.3, p.173 | The source itself uses differential separation in Example7.5.2 and omits the stronger adjective in Example7.5.3. These illustrate the terminology variation; the audit does not declare an erratum or use it to invent an implication. |
| §12.9.2–12.9.5 | The relevant analytic PL/skeletal structure gives the analytic space the G-tropical vertebrated structure needed in Chapter5. No semistable model or smoothness is required. |
| Proposition15.1.1 and Corollary15.1.2, pp.421–422 | Ordinary versus G-local tropicalization of forms/functions; the proof uses ordinary charts for source cutoffs and all G-charts only for the negligibility quantifier. |
| §15.2.2, Corollary15.2.4, p.423 | Good separated analytic spaces are locally holomorphically separated and hence locally differentially separated. This does not state local affine separation. |
| Corollary15.2.5, Theorem15.2.6, Corollary15.2.7, p.424 | Compact smooth cutoffs and approximation of continuous compactly supported functions with support control. No global properness or smoothness of V is added. |
| Theorem15.7.1, p.432 | A topologically separated analytic space pure of dimension n carries the tropical-space structure of level n used for ordinary currents. |
| Definition16.8.3, p.464 | Closed-set tropical H^p-negligibility quantifies over every G-tropical chart on every compact domain. A single F-image check would not satisfy it. |
| Theorem16.8.5 and its proof, pp.464–465 | Nontrivial valued base, boundaryless analytic space, positive closed bidimension-(p,p) current, and a closed tropically H^p-negligible set. Then every coefficient measure T∧α gives that set zero mass. Here p=n. Signed total-variation nullity can be obtained from local positive decompositions. |

## Dependencies not used

No scalar extension of an arbitrary current, current slicing, common semistable model, canonical-coefficient propagation theorem, cross-refinement conclusion, Rethlas verdict, or previous audit pass is an input to this proof review.

The general Euclidean fact that a measure with all first distributional derivatives zero is a constant multiple of Lebesgue measure is proved by convolution in the candidate and checked directly in the audit; no unmentioned tropical regularization theorem is needed.

## Freeze record

FROZEN_PAUSED.md contains five exact candidate hash records and explicitly says the ordinary source manifest was unfinished. All five were checked. Only the skeletal_representation statement and proof receive the new mathematical verdict. The cross_refinement pair and remaining_gap.tex are identity-only checks. No pre-existing completed manifest is fabricated in this dossier.

