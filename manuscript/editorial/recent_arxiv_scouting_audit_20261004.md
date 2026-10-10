# Recent arXiv scouting after the completed second reading

Date: 4 October 2026. Baseline: `eec0c60462541ea583f4e11de94ebbc86216b85c`.

The ordered second reading of Chapters 1–72, Appendices A–N and the nine
front-matter files is complete. This checkpoint begins the authorized
related-direction literature phase. It changes no active TeX, theorem,
open-problem status or verifier receipt.

## Search and reading scope

The [manifest](recent_arxiv_scouting_manifest_20261004.json) preserves three
arXiv API queries, request times, response hashes, identifiers, authors,
publication/revision timestamps and version links. Each query is capped at
20 entries, sorted by submission date, with a submission window from
1 January 2025 through 4 October 2026. The queries returned 20, 9 and 17
metadata entries, including overlap between queries. All 46 titles and
identifiers were scanned; only the six selected abstracts listed below were
freshly read. This is targeted scouting, not an exhaustive current-literature
review. A separate search by update date is still required to cover recent
revisions of older submissions.

| Source | Connection to the book | Actual reading at this checkpoint |
| --- | --- | --- |
| Lyuhui Wu, [2609.27610v1](https://arxiv.org/abs/2609.27610v1) | Local/global psh comparison and singular envelope regularity, Chapters 15–19, 23 and 72 | All 2,966 extracted text lines, including proofs, appendix and references; eleven selected PDF pages visually checked |
| Chenying Lin, [2609.12969v1](https://arxiv.org/abs/2609.12969v1) | Toric metrics restricted to subvarieties, weighted tropical Monge–Ampère measures, Chapters 19 and 64 | Abstract and introductory text lines 1–230 of 2,243; remaining proofs unread at this checkpoint |
| Fang–Ma–Wu, [2609.24078v1](https://arxiv.org/abs/2609.24078v1) | Capacity estimates, big classes and nonlinear elliptic equations | Selected abstract only |
| Oren Ben-Bassat, [2610.01694v1](https://arxiv.org/abs/2610.01694v1) | Non-Archimedean norms, CAT(0) minimization and stability | Selected abstract only |
| Sébastien Boucksom, [2510.10239v2](https://arxiv.org/abs/2510.10239v2) | Hybrid spaces and degeneration of pluripotential theory, Chapter 66 | Selected abstract only |
| Truong Dinh Dat, [2610.00361v1](https://arxiv.org/abs/2610.00361v1) | Polarized Calabi–Yau compactness and capacity arguments | Selected abstract only; explicitly conditional programme, not an established finiteness theorem |

The two acquired PDFs and their text exports are cached outside the active
TeX closure in the ignored `source_material/recent_arxiv_20261004` directory.
Their byte counts, page counts and SHA-256 hashes are in the manifest. The
source pins, not an unversioned arXiv link, control this checkpoint.
Full textual reading does not mean all mathematical claims or dependencies
have passed verification, or that every PDF page has been visually reviewed.

## Wu: precise claims and definition boundaries

The paper's main text states more than the abstract's normal-variety case:
Theorem 7.1, physical page 51, claims the envelope property for a
geometrically unibranch projective variety over a complete discretely or
trivially valued field of equicharacteristic zero. Normality is sufficient
by Remark 7.2. Theorem 6.5 additionally assumes a countable dense subfield
and an ample class for comparison with weakly psh functions. These
hypotheses cannot be dropped when describing what this particular source
claims. General non-discrete fields and mixed characteristic are outside
the advertised new theorem's range.

Definition 3.8 generates local psh functions through local decreasing
sequences of tropically convex rational PL functions and excludes functions
identically minus infinity on a connected component. Appendix A introduces
a particular smooth-approximation class and explicitly discusses how its
definition differs from the closure in CLD25. Theorem A.3 concerns these
specific approximation classes. It does not, just by its title or abstract,
settle every curve-test, current-positive or general CLD closure comparison
in the book's P02 family.

The proof of Theorem A.3 cites APW26b, Proposition 5.22 and Proposition
5.20, and APW26a, Theorem 6.13. The bibliography lists both as 2026
preprints without a persistent identifier or a retrievable edition in this
checkpoint. Neither dependency has been obtained and checked. Their
locators therefore have no primary-source clearance here.

## Wu: unresolved printed-source concerns

The following are ordinary source-audit diagnostics. They are not a
production verifier's verdict on Theorem 7.1, and no claim is made that
the principal envelope theorem has been disproved. Some displayed issues
may be typographical, but an intended correction cannot silently become a
proved input to the book.

1. **Growth direction.** On physical page 16, Definition 3.15(2) prints
   `u <= v + O(1)` for an FS function `u` and a purported logarithmic-growth
   psh function `v`. The arguments in Lemma 3.24 and Proposition 4.19 use
   the upper-growth direction instead. Definition 6.1(2), page 37,
   explicitly uses that upper direction for weakly psh functions. A common
   definition must be established before importing the regularization and
   extension statements that connect these classes.
2. **Missing contact in convexity.** Definition 3.1(3), page 14, prints
   `u(x)=l(x)+C` and `u(x')>=l(x')` with an unrestricted extra constant
   `C`. This does not require the affine minorant to touch the function at
   `x`. For example, a continuous nonconvex function on a relatively compact
   real neighbourhood can satisfy the printed condition by taking a
   constant lower minorant and choosing `C` afterwards. The supporting
   affine condition in Appendix A, page 53, does require contact. The
   discrepancy cannot be carried into the book's convexity definitions.
3. **Degenerate limit.** Proposition 2.21, page 11, omits the generic
   finiteness assumption present in Theorem 2.12. Constants `phi_j=-j`
   form a bounded-above psh sequence for a semipositive model class and have
   pointwise and usc-regularized limit identically minus infinity. That
   function is excluded by the paper's Definition 2.7. The literal limit
   statement thus needs a hypothesis or an enlarged class. Corollary
   4.18(4) carries the same missing restriction.
4. **Locality variable.** Theorem 4.11(1), page 27, prints `MA(v)` on
   the set `u>v` although the maximum agrees with `u` there. Its global
   counterpart 4.11(2) uses the matching variable. The local formula cannot
   be imported as printed.
5. **Gluing potential.** On page 22, the FS expression defining the model
   metric includes `log|s_0|`. After subtracting this same term, its potential
   therefore includes zero in the maximum. The proof then omits that zero
   and asserts the potential is strictly negative at the chosen point.
   The displayed expressions need consistent normalization before this
   gluing step can serve as a load-bearing proof input.

A topological clarification is separate from these printed discrepancies.
Theorem 4.17, page 30, chooses continuous decreasing sequential majorants
with the abbreviated justification that the function is usc. On an
arbitrary compact Hausdorff space, usc alone gives nets. Here the paper's
*local sequence-generated class* supplies additional information: use a
finite open cover with local continuous decreasing majorants, cap them by
a common upper bound for the bounded function, and take a continuous
partition of unity whose supports lie inside the chosen opens. The finite
weighted sums extend continuously and decrease to the function. Thus this
particular step has a direct finite-cover justification and is not recorded
as a counterexample to the comparison theorem. In contrast, a sequence of
divisorial points converging to a prescribed point, as selected in
Proposition 6.2 on page 37, does not follow merely from the limsup formula
without another topological argument. Nets preserve the book's general
conventions. No claim that every sequence assertion in the paper is valid
has been made.

All eleven selected source pages—11, 14, 16, 22, 27, 30, 31, 37, 51, 53
and 54—were actually viewed as full-page images. In particular the growth,
contact, limit and locality discrepancies above were confirmed in the PDF,
not inferred solely from a text extractor. Page-image hashes are recorded.

**Decision:** keep Wu's paper as a relevant research lead outside the active
manuscript. Preserve the book's existing dated envelope results, definition
hierarchy and all 42 open-problem atoms. Check the cited dependencies and
any corrected version before using the comparison or envelope claim as a
new load-bearing source.

## Lin: next primary-source audit

The introduction suggests a useful addition: a toric metric restricted to
a proper subvariety has a measure described through a *weighted tropical
germ*, not merely the Hessian of its restriction to a lower-dimensional
face. The introductory Theorem A, Corollary B, Example 10.1 and Remark
9.8 will be checked against their complete proofs, lattice normalizations
and hypotheses. No statement from this introduction has yet been
integrated into Chapters 19 or 64.

## Publication and retained evidence

The pre-checkpoint fetch found remote main at `00957114` and remote work
at the baseline `eec0c604`. No new user mathematical research appeared
between the preceding publication and this fetch. Future checkpoints
continue checking incoming work before integrating it.

This editorial-only checkpoint reuses the completed second reading's build,
reference, inventory and rendered-page evidence for the unchanged active
manuscript. It runs no new book build, Rethlas verifier, Xean campaign or
local-machine model call. The manuscript remains at the completed
second-reading edition while source checking continues in the cloud.
