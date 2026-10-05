# Cohomologically tropical source integration, 5 October 2026

This checkpoint adds a source-checked cohomological comparison to Appendix G,
a connection from Chapter 66, and provenance in Appendix L. The controlling
source is the published paper by Edvard Aksnes, Omid Amini, Matthieu Piquerez
and Kris Shaw, *Cohomologically tropical varieties*, Journal of the Institute
of Mathematics of Jussieu 24(6) (2025), 2543--2572,
[DOI 10.1017/S1474748025101114](https://doi.org/10.1017/S1474748025101114).
It was published online on 5 September 2025. The live arXiv history of
[2307.02945](https://arxiv.org/abs/2307.02945) ends at v2, revised 27 August
2025. A secondary 2026 search date is not treated as a new version.

Baseline work commit: `abb7b40a8131db451c24d4a8268438e444f2bd36`.
All work remains in the authorized cloud environment. Xean is suspended.
The user has authorized periodic ordinary GitHub publication and incoming
research integration; this checkpoint targets `work` and the existing draft
PR #2. No main-branch publication or merge is performed.

## Primary evidence and reading scope

The official Cambridge PDF was acquired successfully and checked as a
30-page PDF. Its SHA-256 is
`7f8e426fe55b39741a21d1e1d0ec25a61e019965317359a528c71dd047c1e2f9`.
The extracted text was read in full, lines 1--1754, in eight bounded ranges.
The initially truncated first aggregate was reread in two separate ranges.
This is a full text reading, not a claim that all 30 pages were visually
inspected or that all dependencies were independently reproved.

Eleven actual published pages were viewed: physical pages
1, 3, 4, 11, 13, 19, 20, 21, 22, 23 and 24, corresponding to printed pages
2543, 2545, 2546, 2553, 2555 and 2561--2566. They cover metadata, definitions,
the main comparison proof, the family statement and its proof, and the
necessary-condition examples. The manifest pins the images and records
each successful actual view. Truncated tool output is not counted as a view.

The acquired 26-page arXiv v2 PDF has SHA-256
`bb4fa20b4caf2ae019596d8aa43a41d3af75a6ddbdc0ca981ec53f47a84f6608`.
Only targeted definitions and statement ranges were compared, including
text lines 96--220 and 1030--1075. No fresh full reading of v2 or complete
proof-by-proof version comparison is claimed. The published version
controls the integration. Acquisition records, primary text files, live
metadata snapshots and bounded related searches are separately pinned.

## Imported content and exact boundary

All cohomology groups in the new discussion use rational coefficients.
For a closed subvariety of a specified complex torus with trivial valuation,
choose a unimodular fan supported on its tropicalization and the associated
toric and canonical tropical compactifications. The comparison uses total
tropical degree. On the diagonal it passes through the rational Chow group
of the toric variety, the cycle-class map and restriction; it sends
off-diagonal classes to zero. Cohomological tropicality requires an
isomorphism on every closed stratum, including the zero-cone stratum.

The load-bearing published anchors are:

| Input | Locator and page | Use in the book |
| --- | --- | --- |
| Cohomologically tropical definition | Definition 1.1, printed 2545, physical 3; Definition 3.1, printed 2555, physical 13 | Comparison on every closed stratum |
| Wunderschön definition | Definition 1.2, printed 2546, physical 4; Section 2.1 | Nonsingularity, connectedness and pure weight `2k` of each open stratum |
| Tropical homology manifold | Definition 2.6, printed 2553, physical 11 | Local cap-product duality for every open subset |
| Fan independence | Theorem 4.4, printed 2558, physical 16; Theorem 4.5, printed 2560, physical 18 | Independence of the chosen unimodular fan; these named results remain source inputs |
| Main equivalence | Theorem 6.1, printed 2561, physical 19 | For schön varieties, cohomological tropicality iff wunderschönness and local tropical duality |
| Open-stratum comparison | Theorem 6.2, printed 2562, physical 20 | Ordinary total cohomology on the open strata |
| Semistable family comparison | Theorem 7.1, printed 2563, physical 21; proof through printed 2564, physical 22 | Even weight-graded limiting cohomology, vanishing odd weight pieces and nearby Hodge numbers |
| Necessary-condition examples | Sections 8.1.1, 8.1.2 and 8.1.4, printed 2565--2566, physical 23--24 | Four-punctured smooth curve, generic conic and nodal cross |
| Positive arrangement class | Section 8.2, printed 2566, physical 24 | Essential projective hyperplane arrangement complements in their arrangement torus embeddings |

The four-punctured curve is wunderschön but its tropical coordinate cross
fails local duality; the canonical compactification has tropical total
degree-two dimension two against algebraic dimension one. The generic
conic has six punctures and a three-ray tropical line of weight two. Its
whole-compactification comparison is an isomorphism over `Q`, but each
algebraic boundary stratum has `H^0=Q^2`, against tropical `Q`. This is why
checking the whole compactification alone is insufficient. The nodal
coordinate cross is cohomologically tropical but not schön and does not
have the asserted local tropical duality. These are source examples, not
new counterexamples to a book theorem.

The family paragraph explicitly assumes a torically embedded semistable
extension with regular total space and reduced simple-normal-crossing
central fibre, smooth projective general fibres, the stated unimodular
triangulation and torus embeddings of its open central strata. The extended
tropicalization must be a tropical homology manifold and every open central
stratum must be wunderschön in that embedding. Under these assumptions the
published Theorem 7.1 gives
`H_trop^(p,q)(Z) = Gr_(2p)^W H_lim^(p+q)` and
`h^(p,q)(V_t) = dim_Q H_trop^(p,q)(Z)` as comparison statements.
No automatic existence assertion for such an extension in every family is
imported. The statement is about weight-graded limiting groups, not an
unfiltered identification of the entire limiting mixed Hodge structure.

The Chapter 66 bridge requires checking these extra hypotheses in addition
to its residue-measure hypotheses. Problems P05 and P19 still need a
polarization, an operator domain, admissible lifts and a measure comparison.
The cohomological results do not prove envelope regularity, orthogonality,
metric convergence or a general Monge--Ampère theorem. Section 8.4's
announced differential-calculus sequel is not a book input.

## Admission and source preservation

The controlling [verification protocol](rethlas_verification_protocol.md)
states: “Imported results, definitions, explanatory reformulations, and
direct formal consequences that are explicitly identified as such remain
subject to the ordinary mathematical and source audits, but are not
described as new results.” This checkpoint uses that explicit exception
for identified published results, definitions and examples. It adds no new
formal result environment and makes no novelty claim.

Three active TeX inputs change: Appendix G, Appendix L and Chapter 66.
Their 27, 4 and 42 existing formal blocks, respectively, including every
proof, remain byte-identical. Existing labels retain their relative order;
two new section labels are added. The other 422 active TeX inputs are
unchanged. The bibliography appends exactly one entry and preserves its
previous bytes. No independent production-model call or receipt is claimed,
and no earlier receipt is extended to this edition. The BJ22 Siu and general
algebraic decreasing-closure proof boundaries remain in place.

The inventory source and all 42 atom statuses are unchanged, with 12 families
and tier totals `(0, 3, 7, 15, 17)`. The standalone catalogue source and PDF
are byte-identical to the preceding compact-category edition; its 86-page
cloud build and prior seven-page actual review are reused only in that exact
scope. This checkpoint does not edit the open editor document or request
a replacement tab. The earlier native-editor compilation requests returned
no diagnostics before termination; native compilation remains unconfirmed.

## Build, navigation and actual release review

The full native book build passes with 4,259 physical pages and SHA-256
`a419eef4e159c8f9fb6a6fb3535a8e64be584bccd8eb48299cdc2632ba0a18ea`.
There are no TeX errors, package/pdfTeX warnings, unresolved references or
citations, rerun requests or overfull boxes. The 954 underfull diagnostics
retain the preceding edition's count; this does not assert their locations
are identical. BibTeX and makeindex report no warnings or rejected entries.

Source checks cover 425 active TeX inputs, 12,598 unique labels, 583 available
bibliography keys and 284 cited keys. The book has 21,448 named destinations,
46,216 internal links, 163 URI links and 2,438 outline entries. Every checked
internal, outline and index destination is valid. The index accepts 730
entries and has 729 page groups over 397 distinct numeric destinations.
All 108 protected Appendix M/N inputs remain unchanged.

Thirteen actual release pages were viewed in seven contact sheets:
64, 66, 3518--3520, 3908--3911, 4026--4028 and 4247. They cover the contents,
Chapter 66 insertion and neighboring text, the complete new Appendix G
section and its normalization-table seam, Appendix L and its following
page, and the new bibliography entry. Equations, diacritics, cross-references,
stratum conditions and page seams were checked. This is a scoped release
review, not a new whole-book visual reading or raster-identity comparison.

The integration manifest pins the active closure, sources, source snapshots,
build checks and actual reviews. A distinct frozen book PDF, thirteen-page
review PDF and current source ZIP are exported. Every archive member is
checked against the current filesystem and the complete active closure is
included. A fresh isolated compilation of the ZIP is not claimed. Earlier
dated audits, source archives and PDFs retain their original bytes and scopes.

## Related research check and next direction

A bounded arXiv search and live histories checked the related Amini--Piquerez
papers 2405.05718, 2405.05014, 2007.07826 and 2310.15367. Their metadata alone
does not authenticate their proofs; no fresh full reading or new result from
those papers is imported. The search is not an exhaustive claim about all
recent literature or the absence of an unpublished sequel.

The next candidate is Aksnes's *Tropicalization of curve arrangement
complements and arroids*, arXiv 2404.14380v3, revised 27 August 2025 and
published in Mathematica Scandinavica 131 (2025), no. 2,
[DOI 10.7146/math.scand.a-156674](https://doi.org/10.7146/math.scand.a-156674).
At this checkpoint only its live metadata has been inspected. Its full
primary paper must be acquired and read before any new integration;
pairwise-transversality hypotheses must not be replaced by tangency examples
from a different source. Continue cloud research and inspect incoming author
updates before each verified work-branch milestone.
