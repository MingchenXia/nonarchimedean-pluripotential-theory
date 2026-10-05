# Revision-sensitive arXiv search and FGK mixed-characteristic check

Date: 5 October 2026. This search complements the earlier
[recent-submission scouting](recent_arxiv_scouting_audit_20261004.md) by
including older papers with recent revisions. It is a bounded literature
check, not an exhaustive bibliography or erratum search.

## Search and triage scope

The arXiv identifier API returned HTTP 200 at 01:52:45 UTC for
`(all:"non-Archimedean" OR all:"nonarchimedean") AND
(all:"envelope" OR all:"Siu" OR all:"plurisubharmonic" OR all:"pluripotential")`,
sorted by `lastUpdatedDate` descending, with `start=0`, `max_results=30`
and no original-submission date restriction. The returned total is 39;
only the first thirty records are covered. The XML SHA-256 is
`a2b1953ac84a1d0a04aaac67d33ecd6a4920f77d8b88538d6844909fff966900`.
All thirty titles/metadata and the eleven abstracts updated since
1 January 2025 were read. Xia's 2024 revision abstract was also checked.
Abstract inspection is not proof verification.

| Pinned returned revision | Last updated | Disposition at this check |
| --- | --- | --- |
| Wu, `2609.27610v1` | 23 September 2026 | Local psh and normal-envelope claims; retain the earlier source-audit boundaries, with no new admission here. |
| Botero–Mazzon–Pille-Schneider, `2603.08664v1` | 9 March 2026 | Already in the recent-source programme and Lin coefficient check. |
| Fang–Gubler–Künnemann, `2203.12282v3` | 8 December 2025 | Newly read in full and compared below with the book-cited publication. |
| Yao, `2511.16401v1` | 20 November 2025 | Maximal Chow/K destabilizers; the abstract expressly assumes idealistic hypotheses. Candidate only; no full-paper check or integration here. |
| Boucksom, `2510.10239v2` | 16 October 2025 | Hybrid analytic lecture notes, already a related candidate in the earlier scouting. |
| Boucksom–Jonsson, `2509.15016v1` | 18 September 2025 | Weighted cscK/YTD source already present as `BJ25WeightedYTD`. |
| Mesquita-Piccione–Witt Nyström, `2509.09442v1` | 11 September 2025 | Already used with its established transcendental scope as `MPWN25`. |
| Chambert-Loir–Ducros, `1204.6277v2` | 25 July 2025 | The revised source is already present as `CLD25`; the original submission is from 2012. |
| Buss–Garcia–Mukherjee, `2403.04046v3` | 24 March 2025 | Operator-algebra search hit; not selected for the book's psh/envelope question. |
| Jokela, `2502.13235v1` | 18 February 2025 | Ordered-semigroup search hit; not selected for integration. |
| Pille-Schneider, `2210.05578v2` | 5 January 2025 | Hybrid toric/SYZ direction already represented by `PS23Hybrid`; no new version-equivalence claim here. |

Xia, `2312.17150v3`, *Operations on transcendental non-Archimedean
metrics*, was updated on 22 October 2024. Its abstract and the existing
Chapter 53 source cache identify it as an established book source, not a
new topic discovered by this query. None of this triage changes a problem
status or upgrades an abstract to a theorem.

## Full FGK v3 reading and comparison

The newly acquired arXiv PDF is
[2203.12282v3](https://arxiv.org/pdf/2203.12282v3), requested at
01:55:59 UTC, HTTP 200, 431,275 bytes, thirteen physical pages,
SHA-256 `5c803025992dc2a35231e111c336fb518b25cf9ad371e9db8026378cc5bbfcd8`.
All 740 extracted text lines, including references, were read without an
omitted interval, and all thirteen actual pages were viewed. The arXiv
version stamp says 8 December 2025; the document's own date says
9 December 2025. They are different metadata fields.

The book's controlling citation remains the published Nagoya Math. J.
259 (2025), 548–561 article, DOI
[10.1017/nmj.2025.8](https://doi.org/10.1017/nmj.2025.8).
Its cached fourteen-page PDF is 348,358 bytes, SHA-256
`3744214371ba978e8696784ef246a6a2419129dbfaf0b148f7ed50613efd9623`.
Fresh published-text comparison covered lines 99–150, 174–204 and
571–700. Nine actual published pages were viewed: physical pages
2, 3, 4, 6, 7, 10, 11, 12 and 13. Earlier published-paper readings remain
dated evidence. This is not a fresh complete published-paper reading or
a claim that both versions are byte-identical.

The compared principal statements retain the same relevant boundaries:

1. Theorem 1.1(i) concerns a model metric on an ample line bundle on a
   smooth projective variety over a complete discretely valued field of
   mixed characteristic. The inducing model is regular, and the generic
   ample line bundle must have an ample extension on that same model.
   Theorem 5.1 supplies uniform approximation of the zero envelope under
   this model hypothesis.
2. Theorems 1.1(ii) and 7.1 assume resolution for **projective** models,
   as defined in Definition 6.1. Lemma 6.4 supplies a dominating regular
   model with an ample extension after a positive tensor power. These
   statements do not require the additional embedded-resolution
   assumption merely to conclude continuity of the metric envelope.
3. Theorems 1.2 and 8.1 additionally assume embedded resolution for
   regular projective models, Definition 6.3, to supply the SNC framework.
   The positive Radon measure has the prescribed total degree and is
   supported on an SNC skeleton. The solution is continuous semipositive
   and unique up to metric scaling (or an additive potential constant).
   This is not an arbitrary-measure, arbitrary-field assertion.
4. Global `+` test-ideal subadditivity is still Conjecture 3.6. The proof
   uses **perturbation friendly** test ideals with the cited subadditivity
   and effective generation properties in Theorem 4.2 and Theorem 4.7.
   It does not claim that the original conjecture has been proved.

The paper's envelope starts from rational model functions. Its field,
model, class and resolution framework does not supply critical
homogeneous Siu division on an arbitrary normal variety over a trivially
valued field. The complete arXiv reading checks the paper's printed
argument and imported steps; it is not a new independent verification of
every deep antecedent in BFJ or mixed-characteristic test-ideal theory.

Both inspected PDFs print `P_(t theta)(t theta)` on the left of (2.2),
while its right side is `t P_theta(u)`. The obstacle should be `t u`;
`theta` is a curvature form rather than an obstacle function. This is a
local notation defect, not a claimed counterexample to the main theorem.
Chapter 23 already writes the well-typed identity with obstacle `t f`
and separately retains the model-resolution and embedded-resolution
boundaries. No active theorem, citation key or bibliography change is
needed for this version check. Chapter 23's separate Siu-scope prose
correction belongs to the downstream audit, not to a stronger FGK result.

The [manifest](revision_sensitive_arxiv_manifest_20261005.json) pins the
query, primary files, reading and actual-page scope. No independent model
call, proof admission, general envelope/Siu repair or solved research atom
is recorded. Continue the primary-source investigation of potentially
relevant normal-envelope arguments and the remaining related candidates.
