# Intermediate Calabi–Yau limits and comparison metrics — 4 October 2026

This checkpoint follows the complete reading of `2505.11087v1` and the
fixed-matrix repair candidate. Six primary PDFs have now been read in full
as extracted text: Li–Tosatti `2511.04651v2` (1,118 lines), Li's intermediate
limit `2305.02258v1` (2,171), its published Inventiones edition (2,198),
uniform Skoda `2006.16961v1` (630), its published Analysis & PDE edition
(652), and Li–Tosatti's diameter `2006.13068v2` (593). The 7,362-line total
includes references and publisher matter. Forty-two selected actual primary
PDF pages were viewed: fourteen for recent generic regularity, eight for
the old intermediate preprint, nine for its published edition, seven for
published Skoda, and four for diameter. These are source pages, not a fresh
visual review of book pages. The companion manifest pins each acquisition,
reading scope and image; no historical audit is widened retrospectively.

## Controlling editions and statement boundaries

Li, *Intermediate complex structure limit for Calabi-Yau metrics*,
Invent. Math. **240** (2025), 459–496, DOI
`10.1007/s00222-024-01314-9`, is the controlling baseline. The publisher PDF
was obtained from the actual Crossref PDF link. It concerns a smooth Fano
manifold M of dimension n+1, an ample L, positive integers d_i with
−K_M=(sum d_i)L, and sufficiently generic sections F_i of L^{d_i} and F of
−K_M with smooth divisors and transverse intersections. The family is
F_0⋯F_m+tF=0, with 1≤m≤n−1. Its essential skeleton is the m-simplex.
Theorem 1.1 and Proposition 6.13 give global C⁰ hybrid convergence of the
norms raised to 1/|log|t||, after suitable normalization, for this family.
This source does not establish that statement for every meromorphic
Calabi–Yau degeneration.

The published Lemma 4.7 proves smoothness on each open transport chamber
Δ_k, using Figalli–Jhaveri's locally doubling regularity results. The old
preprint instead excluded a closed null set. The published Hilbert-series
identities in Lemma 3.1 also correct the reciprocal-factor displays of v1.
A new Remark 5.2 changes the subsequent numbering: the ansatz is
Proposition 5.3, uniform approximation Proposition 5.4, hybrid extension
Corollary 5.5, generic volume approximation Proposition 5.6, total variation
Corollary 5.7 and the non-Archimedean Calabi–Yau metric Corollary 5.9.
Proposition 6.13 retains its number. These changes matter when following
citations in recent work.

Li–Tosatti, *Generic regularity of intermediate complex structure limits*,
`2511.04651v2`, updated 28 January 2026, is read as that exact arXiv version.
Metadata also reports J. Reine Angew. Math. **836** (2026), 285–302, DOI
`10.1515/crelle-2026-0013`; that journal PDF has not been acquired here.
Theorem 1.1 upgrades the preceding potential description to relative C⁰
metric convergence on generic regions for the same Fano hypersurface
family. Its proof uses the published baseline's Proposition 6.13 for global
potential convergence and Proposition 5.6 for the volume calculation.

The usable quantifiers are: fix a discarded probability mass δ>0; choose
compact subsets of the open transport chambers and fixed neighborhoods;
for sufficiently small t their lifted union U_{t,δ} has normalized
Calabi–Yau measure greater than 1−δ and the relative metric error tends to
zero there. Constants and the smallness threshold may depend on δ. An
appropriate diagonal choice yields the introductory description of regions
whose mass tends to one. Corollary 5.1 gives higher regularity after local
torus unwrapping and the stated coordinate stretching. The class of both
unscaled metrics is c₁(L|X_t); the relative tensor norm is invariant under
common metric scaling. The volume measure in the mass assertion is a
probability measure, whereas raw Monge–Ampère mass is (Lⁿ).

The chamber limit solves the weighted real Monge–Ampère transport problem,
with W(p)=(1+sum d_i p_i)^{n−m}; it is not the unweighted equation of the
maximally degenerate case. Derivative statements must retain their varying
coordinates. The assertions do not identify the metric near chamber walls
or prove a global Gromov–Hausdorff limit or a coisotropic fibration. The last
is explicitly a further question in Remark 1.4 of v2.

Two normalized auxiliary displays, (4.42) and (4.51), deserve separate
care: the printed bound for w_k−Q'_k contains (ηr_k)^{2+α}, although
w_k=(ψ−Q̃_k)/r_k^{2+α}. Rescaling the intended error for ψ gives
η^{2+α} for this normalized difference. Equations (4.49) and the subsequent
rescaling confirm the normalization. This elementary display issue is
recorded outside the book; the displays will not be copied into the
exposition. It is not a counterexample to Theorem 1.1. The Savin and
elliptic-estimate dependencies have not all been independently re-proved or
freshly checked in their own primary sources. Any book insertion is a
precisely scoped import, not a new independent theorem certification.

## Uniform Skoda and the diameter comparison

The controlling Skoda source is Li, Anal. PDE **17** (2024), 2247–2256,
DOI `10.2140/apde.2024.17.2247`, obtained from the publisher's actual
`citation_pdf_url`. Theorem 1.3 uses a polarized algebraic Calabi–Yau
degeneration with normalized potentials and the background form scaled by
1/|log|t||. Theorem 2.9 states the broader local SNC measure hypotheses:
nonnegative local exponents with minimum zero, the zero-discrepancy stratum
dimension m, and the specified |log|t||^{-m} density bound. Theorem 3.1
derives a uniform C⁰ estimate from the uniform Skoda bound for normalized
smooth Monge–Ampère solutions. Constants depend on the stated data.

The published proof of Lemma 2.6 uses a blow-up creating the barycentre
vertex and Proposition 2.4 there. The old v1's appeal to boundary
convexity alone should not be used as the full lower-bound proof. The
published barycentre argument resolves that version-specific concern.
Changing a fixed Fubini–Study background by an O(|log|t||) potential changes
the scaled bound by O(1), as the source explains.

Li–Tosatti `2006.13068v2`, Proposition 3.1, provides a relevant genuine
comparison metric in a polarized meromorphic Calabi–Yau degeneration with
semistable SNC reduction and m>0: in the class |log|t||^{-1}c₁(L), it
dominates |log|t||^{-2} times the logarithmic directions on the chosen
maximal-stratum region. Multiplying by |log|t|| gives the corresponding
unscaled lower bound. The proof uses finite adapted projective charts and
toric metrics. This is an independently located related source; it does
not authenticate the unresolved `[?, Proposition 3.1]` citation printed in
`2505.11087v1`. Metadata reports the later JDG publication, but its journal
PDF has not been read. The diameter theorem gives two-sided bounds at its
specified scale and does not by itself identify a Gromov–Hausdorff limit.

## Conditional global-metric repair outside the manuscript

The separate [dossier](research_dossiers/li_global_metric_repair_20261004.md)
constructs a comparison form by integrating globally smooth logarithmic
divisor profiles. It assumes a smooth reduced-SNC model and a fixed
line-bundle metric uniformly positive against a model Kähler form on the
nearby fibres. That extra uniform positivity is explicitly not inferred
from generic ampleness on an arbitrary modification. The form stays in
c₁(L), has potential oscillation O(|log|t||), dominates the ordinary
transverse and |log|t||^{-1} logarithmic directions on the correctly defined
compact simplex regions, and yields the desired O(|log|t||) integrated
gradient estimate for any smooth background-psh potential with that
oscillation bound.

The universal conditional argument is written in the dossier. Its separate
scalar calculation passes three exact symbolic identities, 255 interior
parameter cases (170 meet the stated threshold), and twenty boundary or
exterior checks at 350-digit precision. Finite checks do not replace a
geometric proof. The construction supplies neither convergent chamber
bases nor approximate domination nor the global Bergman/hybrid argument
for an arbitrary degeneration. No new independent model receipt, novelty
claim, principal-theorem admission or solved problem is recorded. The
active book at this checkpoint remains the checked 4,240-page edition.

The next integration is the known, specialized intermediate-limit result
in Chapter 66, with published baseline numbering, version-pinned recent
regularity, explicit probability normalization and generic-region
quantifiers. All 42 current problem statuses remain unchanged.
