# Differential forms and formal symplectic rigidity — 6 October 2026

Four subsections in Chapter 68.8 and Appendix L.45 explain existing
results connecting normalized-volume minimizers to non-degenerate
differential forms. This extends the preceding
[finite-degree integration](finite_degree_normalized_volume_audit_20261006.md)
from baseline `f0ead9cc084f865117351d288d040f02bbc2a6d9`.
The current scope is a normal complex algebraic klt germ of dimension
at least two with zero boundary. Isolation and the analytic domains
used for the earlier integrability comparison are unnecessary here.

## Mathematical content

The logarithmic order of a reflexive p-form is homogeneous, independent
of the adapted log-smooth model, and locally linear after principalizing
its coefficient ideal. If its n/p-th wedge trivializes the canonical
sheaf, the wedge inequality gives A_X/n >= A_sigma/p. A weighted
affine-four-space example exhibits both loss and preservation of
non-degeneracy. Preservation by itself does not characterize a
normalized-volume minimizer; the explicit unequal weight vector has
larger normalized volume than equal weights.

The Kollár component retains its effective different even though the
ambient boundary is zero. The adapted cotangent canonical extension has
rank n and negative slope, with cover slopes divided by the cover degree.
Its maximal slope is bounded by the global log Fano delta invariant.
The unstable case uses an actual K-semistable boundary perturbation and
the corresponding cotangent inclusion. Guenancia's general-boundary
semistability result and the dual tangent convention in Druel–Guenancia–Păun
are identified separately.

The strict transform of the form and this slope bound supply the
form-discrepancy inequality. Nearby scaled Kollár valuations with delta
approaching one give equality at the normalized-volume minimizer.
Local linearity and the wedge inequality extend equality to suitable
nearby divisorial approximations with the same associated graded variety.
The Rees specialization criterion then preserves non-degeneracy;
relative differentiation preserves closedness. Rational degeneration
gradings and possibly irrational minimizing Reeb vectors remain distinct.

In the closed symplectic case the formal isomorphism has a separate
Poisson-deformation input. The scale-up family retains the negative
parameter weight, positive symplectic-form weight, negative bracket
weight, conical central fiber, vertex section and orbit condition.
The positive-weight universal deformation base, together with corrected
equivariant lifting and uniqueness, forces every equivariant Artinian
classifying map to be constant. Namikawa–Odaka's completion comparison
is required before restricting at t=1. Parameter completion alone does
not prove a formal isomorphism of the two pointed fibers.

This imports formal symplectic conicality. It does not construct a global
cone action on arbitrary affine neighborhoods or a hyperKähler cone
metric. The nilpotent and hypertoric applications and the analytic
algebraization arguments remain separate follow-up directions.

## Sources and proof boundaries

The controlling main source is Xu–Zhuang, with Guenancia's appendix,
arXiv:2606.02401v2, revised 22 June 2026: 54 pages and 3,513 extracted
text lines. The entire paper, both appendices and bibliography were read.
All 54 actual pages were displayed, comprising eight pages reused from
the preceding selected reading and 46 additional pages. The historical
selected-reading record is preserved.

Seven additional sources were acquired and checked. Forty selected
actual pages were displayed. The 13-page Namikawa correction was read
in full; the other six readings are explicitly selected sections or
statements. Their precise ranges, hashes, URLs and actual views are
recorded in the integration manifest.

| Input | Controlling version and locators | Reading scope |
| --- | --- | --- |
| klt extension of forms | GKKP, arXiv:1003.2913v4, 31 October 2011; Theorem 1.4 and Remark 1.4.1, pp. 3–4 | Known statement import; the 72-page arXiv and published editions remain distinct |
| boundary perturbation | Liu–Xu–Zhuang, Annals 196 (2022), 507–566; Theorem 1.8, Theorems 5.1–5.2 and 5.4, Lemma 5.5 | Selected statements and complete relevant proof sections, including pp. 48–51 |
| tangent extension precursor | Druel–Guenancia–Păun, C. R. Math. 362 (2024), 93–118; Section 3, actual pp. 11–15 | Complete selected extension, curvature and slope argument |
| formal scale-up rigidity | Namikawa–Odaka, arXiv:2503.15791v4, 6 February 2026; Definition 3.1, Theorems 3.3 and 3.5, Lemmas 3.8–3.9 and 3.11, actual pp. 12–17 | Selected complete formal argument; metric results not imported |
| positive universal-base weights | Namikawa, arXiv:math/0609741v7, 15 February 2010; Corollary 2.5, Theorem 5.1, Section 5.4 | Selected proof sections; affine prorepresentability retains H^1(X^an,C)=0 |
| equivariant corrections | Namikawa, arXiv:2601.01131v2, 11 January 2026; Theorem 2.1, Proposition 2.3, Corollary 2.4 and Lemma 3.1 | Entire 873-line text; eight selected actual pages displayed |
| original Poisson argument | Namikawa, PRIMS 44 (2008), 259–314; Lemmas 20–21, actual pp. 29–30 | Selected argument used together with the 2026 corrections |

Two steps in Xu–Zhuang's displayed self-contained proof of Lemma 4.3
need further justification as written: codimension-three Cohen–Macaulay
vanishing alone gives H^1, and a de Rham comparison requires its precise
topology and hypotheses. The book uses the separately checked scale-up
Poisson route. No counterexample to the formal rigidity theorem is
claimed. Namikawa's earlier codimension-four argument is kept distinct.

Appendix B's final boundary perturbation uses
K+Delta_epsilon = (1-m epsilon)(K+Delta) when H_0 lies in
|-m(K+Delta)|. The correct proportionality replaces the printed
negative 1+epsilon factor before taking the semistable limit.
The resulting limiting slope statement is unchanged.

These are known imports and explanatory consequences under the
repository verification protocol. No new production-model call,
independent verification receipt or original priority claim is made.
General non-Archimedean Siu/closure, spectral and A2–A4 questions retain
their previous status; BJ22 Theorem 6.21's proof gap remains explicit.

## Validation and preservation

The final book has 4,351 pages. The 425-input closure has 12,767 unique
labels, no missing inputs, duplicate labels or dangling references.
The bibliography has 650 available keys and 355 used entries, with no
BibTeX warnings. MakeIndex accepts 753 entries, rejects none and reports
no warnings. All 411 distinct numeric index destinations are valid.
PDF checks find 21,805 named destinations, 46,815 internal links,
171 external URL links and 2,532 contents entries across six parts,
with no invalid destinations.

TeX errors, unresolved citations, package/pdfTeX warnings, missing
characters, overfull boxes and rerun requests are zero. The 954
underfull notices match the preceding build. Thirty-nine matching final
pages were displayed in twenty sheets: the changed contents and opening,
all new content and its transitions, the complete ten-page index, and
the complete seventeen-page bibliography. This is a scoped release
review, following the completed whole-book second reading.

All 46 old formal blocks in the two changed TeX files are byte-preserved,
as are their old label order, the dated claims ledger and all preceding
local content. The only opening edit explains the additional form route.
The 108 protected inputs and 423 other active TeX inputs are unchanged.
Seven bibliography entries are appended; one existing main-source note
is updated to describe its expanded checked scope.

The 43 preceding frozen integration manifests and the previous exports
are preserved. The native 86-page LaTeX open-problem catalogue stays
in the same editor with its source and PDF unchanged. All 42 complete
canonical status rows, twelve families and tiers 0/3/7/15/17 are
preserved. The research-only toric entropy candidate and its record
remain unchanged and OPEN.

Routine GitHub synchronization continues on `work` under the user's
standing authorization, with platform permission checks retained.
The next reading examines analytic conicality and metric hypotheses,
and the separate nilpotent and hypertoric examples before further import.
