# Common subsolutions, compactness and direct gradients

**Known source argument and conditional explanation.** The baseline is
`7f3b70d2f403749700e6e1cdca01566eec796b26`. Chapter 68.9.6 explains
Guo--Song's compactness route to a gradient bound; Appendix L.57 records
the precise editions, potential convention and dependency boundaries.
Two analytic source estimates remain explicit inputs. No original
theorem or complete repaired external proof chain is admitted.

## Mathematics and scope

Fix a connected compact Hermitian manifold of complex dimension n>=2,
a smooth real background chi, and an open convex symmetric cone
Gamma_n contained in Gamma contained in Gamma_1. The spectral function
f is smooth, positive, elliptic and concave in Gamma, continuous and
zero on its boundary, and tends to infinity along each positive radial
ray. Neither homogeneity nor a positive lower bound for the product of
its first partial derivatives on the entire cone is required. Chi need
not be positive or closed.

The family consists of given smooth admissible solutions, normalized
by inf u=0, with prescribed densities 0<h<=H0 and uniformly bounded
grad h. One fixed smooth admissible subsolution has a common positive
gap between its asymptotic f-infinity and each h. Separate subsolutions
without common radii and smooth data would not supply this hypothesis.
The common gap supplies the quantitative radii used in the oscillation
bound. The first explicit analytic input is Guo--Song Proposition 2.8:
the uniform difference of two potentials is bounded by a fixed multiple
of the density sup difference and the potential L1 difference.

The auxiliary Monge--Ampere equation on a fixed Hermitian metric alpha
is (alpha+ddc psi)^n=c rho alpha^n, sup psi=0. Average-one densities
with a positive lower bound and an Lq bound, q>1, give the required
potential and normalizer bounds through the selected Guo--Phong
entropy estimate and mass lower bound. The maximum of psi bounds c
above. The constant c is retained, since a general Hermitian metric
has no Kähler total-mass identity. In the stability argument the peak
of the auxiliary density is fixed before shrinking its high-value
support; this order gives a common L2 bound.

The second explicit input is Guo--Song Proposition 3.1. For one fixed
eta>0 and C, if a smooth admissible comparison v is uniformly eta-close
to u, then grad u is bounded by C(1+||grad v||^2). Eta and C are fixed
before v; other derivatives or distance of v to the cone boundary do
not enter those constants. The source uses Székelyhidi Proposition 6
on a fixed positive-level strip and admissibility of the subsolution
on the remaining small levels. This explanation does not certify the
entire proof chain of either imported estimate.

Oscillation and Gamma contained in Gamma_1 give a uniform potential
bound and a fixed-Laplacian lower bound Delta u>=-C0. Its smooth
positive invariant adjoint measure mu satisfies integral Delta w=0.
Applying this to u^2 gives integral |partial u|^2=-integral u Delta u
<=C0 integral u. Rellich gives L1 subsequential compactness. The
prescribed density gradient bound gives uniform density convergence
along a further subsequence; Proposition 2.8 makes the potentials
uniformly Cauchy. C0 precompactness thus precedes the gradient estimate.
If gradients were unbounded, select one fixed smooth member sufficiently
late in that subsequence. Its finite gradient and Proposition 3.1 bound
every later gradient, giving the source's contradiction. No uniform
gradient estimate for the comparison sequence is assumed, and this
argument does not supply an explicit formula for the final constant.

The source potential is the book potential divided by 2 pi. This fixed
factor is absorbed in the comparison tolerance and constants. By
contrast, the preceding auxiliary Hessian density has a root of the
form b(x) exp((u_j-v_j+f(x,v_j))/m). Its derivative contains grad u_j
and grad v_j; uniform convergence of v_j alone does not control these.
An unbounded penalty parameter likewise changes density bounds. The
prescribed-density theorem therefore does not automatically settle
those weak auxiliary estimates.

Full second-order regularity additionally requires a positive lower
bound for h and uniform C2 density data, as in Guo--Song Corollary 1.2.
Its constants are not asserted uniform when that lower bound tends to
zero. The separate Green proof uses Kähler geometry, closed chi,
Gamma contained in Gamma_2, trace growth, localized normalized
ellipticity and refined concavity. These hypotheses are not a substitute
for the missing uniform auxiliary bounds. No bounded-solution
continuity, original-equation existence or uniqueness, canonical problem
solution or general non-Archimedean Siu/closure repair follows here.

## Primary readings reused

The preceding [source review](Guo_Song_direct_gradient_source_review_20261006.md)
read and displayed 68 fresh physical pages in 35 sheets:

- Guo--Song [2609.39726v1](https://arxiv.org/abs/2609.39726v1),
  submitted 30 September 2026 at 13:36:58 UTC: all 28 actual pages,
  including proofs and references. The fixed subsolution is on 1--3,
  radii and oscillation on 4--6, auxiliary mass and L1 compactness on
  7--8, stability on 8--10, comparison gradient on 11--17, compactness
  completion on 17, and the separate Green argument on 20--27.
  PDF SHA-256:
  `f16b733e920504b82a67b6c61774cf74e12a5e0fd61317ea1d7ea7300ac7573a`.
- Guo--Phong [2204.12549v3](https://arxiv.org/abs/2204.12549v3),
  revised 28 February 2023 at 03:45:55 UTC: actual 1--4 and 9--19,
  fifteen pages of thirty-two. Theorem 1, its local and compact proof,
  and Corollary 1's entropy mass lower bound are included. The other
  applications and Annals publication PDF are not claimed read.
  PDF SHA-256:
  `985bdc1a7f39b0229072534afafa697babbf76eed34381745723abf7568dbd6f`.
- Székelyhidi [1501.02762v3](https://arxiv.org/abs/1501.02762v3),
  revised 23 April 2015: actual 3--10, eight fresh pages. Earlier
  selected 1--2 and 11--28 retain their separately frozen record.
  The cumulative scope is 1--28 of thirty-four, not a full-paper or
  journal-PDF reading. PDF SHA-256:
  `0b8a8f819c99eda19c8041d3a02d6e2202a5f99a3958d79041cd4758b4d3b3dd`.
- Dong--Zhang [2603.19045v1](https://arxiv.org/abs/2603.19045v1),
  submitted 19 March 2026 at 15:41:19 UTC: actual 1--17 of twenty-four.
  The selected refined-concavity proof keeps its external algebraic
  antecedents. PDF SHA-256:
  `c133961581ce3f6755fe155569cfe37badb091463c3eb8ac94baedc88e9ba5e8`.

The main and dependency reading-record SHA-256 values are
`7f268d06da6d10d1c7721710564f2bf0e7f65be926f69f33648f62dda2b14561`
and `a1d1a3c98d66fcb49f02661bc9e7b3f9df26df09d5e7a924deee8b6d984c78a5`.
The frozen source-review manifest is
`26a67c8e431b25071f62dffcc0a56eedcb360bae9085ec5870980ffb0abe37a9`.
Four literal diagnostics concern a preceding cone construction,
square-free derivative multi-indices, omitted complex conjugates and
discarding a negative remainder. Four apparent objections were cleared.
Neither the quantitative alternative's statement nor the main
Guo--Song theorem is refuted. A complete refined-concavity proof repair
is not certified. This integration reads zero fresh primary pages and
adds three version-specific bibliography entries.

## Final validation and PDF review

The final book has **4,398 pages**, 20,435,281 bytes and SHA-256
`e37c01b4b303859bf24ab1e083c17220866516d547b13cdac65b5e930faac333`.
TeX errors, package/pdfTeX warnings, missing glyphs, overfull boxes,
unresolved references/citations and rerun requests are zero. The 954
nonfatal underfull diagnostics equal the preceding build's count.
The first build stopped on an unprotected bibliography accent; it is
retained as a failed attempt, followed by successful v2. PDF reading
then replaced an inappropriate determinant notation for scalar f by
the product of first partial derivatives. The final source, build and
PDF gate are v3; earlier v2 views are not reused as final-v3 reading.

The post-render reference check finds 425 active inputs and 12,856
unique labels, with zero missing inputs, duplicate labels or dangling
references. There are 381 cited entries among 676 bibliography keys
and no bibliography warning. Five labels and three explicit equation
tags are new; all 144 Chapter 68 equation numbers are unique. No index
entry is added. The index accepts 764 entries, rejects zero, and has
1,012 lines, 763 page groups and 419 valid numeric destinations.
Navigation has 21,970 named destinations, 47,063 internal links, 171
external URL links, 2,566 contents entries and six parts; invalid links,
destinations and contents pages are zero.

All **39 matching final-v3 PDF pages** were individually displayed and
their complete extracted text read in twenty sheets: actual 61, 68,
3622--3625, 4159--4163 and 4371--4398. They cover the affected contents,
new text with both neighboring transitions, the provenance transition,
following appendix, and complete index and bibliography. The frozen
view manifest SHA-256 is
`8911634e1821260c251067028c8235ad78606ec9e089723210db475d35335a1b`.
This checkpoint does not claim a fresh reading of all 4,398 pages.
Existing bibliography typography visible in the unchanged entries
(for example the 2005 Mustaţă accent and Fornæss spacing) is recorded
for a later general bibliography polish; it does not affect the three
new entries or source claims in this integration.

## Preservation and publication

Chapter 68 and Appendix L are the two changed active inputs. All 423
others and all 108 protected inputs retain baseline bytes. The edited
files preserve all 34 existing statement/explanatory blocks and twelve
proof blocks, 46 in total, with no new formal environment. The
non-Archimedean bibliography is unchanged. README and the research
programme record this completed integration.

All 67 prior frozen manifests, 55 integrations and twelve source reviews,
and all 121 prior exports retain their bytes. The other 5,054 tracked
baseline files remain unchanged. The canonical inventory passes with
42 atoms, twelve families and tier counts 0/3/7/15/17. Complete status
rows, the inactive toric candidate and native catalogue source and PDF
retain their bytes. The native editor stays open without editing,
recompilation or tab change.

The release consists of the full PDF, a 39-page review PDF and a source
archive with 666 byte-verified members and a passing CRC check. All 425
active inputs and both bibliographies are included. No fresh isolated
archive compilation is claimed. The integration manifest, closure and
artifact record pin the edition. Main and work are explicitly fetched
before publication on the existing work branch and draft PR. Routine
GitHub synchronization follows standing user authorization and retains
platform permission checks.

No original result, independent production model call, verification
receipt, canonical solved status or general Siu/closure repair is added.
Continue with Chu--Liu's alternative gradient proof, the claimed
Hermitian Hessian Lp range, and the remaining precise weak auxiliary
inputs before any broader regularity admission.
