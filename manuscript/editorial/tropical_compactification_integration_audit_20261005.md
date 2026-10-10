# Recession-fan compactification integration, 5 October 2026

Appendix G now introduces the polyhedral boundary data before the existing
complex cohomology comparison. The source is Kastner--Shaw--Winz,
*Tropical compactification via Ganter's algorithm*, Discrete & Computational
Geometry 73 (2025), 264--292,
[DOI 10.1007/s00454-023-00581-2](https://doi.org/10.1007/s00454-023-00581-2),
published online 14 October 2023. It imports known definitions, the
recession-fan complex theorem and identified source examples. It does not
import Lee's tropical Schubert preprint or the original projection diagnostic.

The new section explains why the boundary is additional data: the ambient
fan, projected stratum faces, closures of faces and signed incidence maps
all enter a compact cellular calculation. It retains a finite rational
complex and pointed recession cones. The polyhedral complex assertion uses
the recession fan itself, not an arbitrary coarser ambient fan or merely a
subdivision of the support. This precedes the separate local tropical
duality and algebraic hypotheses in the AAPS comparison. Appendix L records
the scope. All old formal statement and proof blocks remain unchanged.

## Primary acquisition and reading

The 29-page published online-first PDF was acquired from the German National
Library's article copy, `https://d-nb.info/1313135917/34`, HTTP 200, with PDF
magic verified. SHA-256:
`ab75e66fa3dd8b7e8c0318081041fd4446c9a70833cc84950ff48f536d5637ae`.
Its extracted text was read in full, lines 1--1519, in successful ranges
1--220, 221--440, 441--660, 661--880, 881--1100, 1101--1320 and
1321--1519. This copy has the journal/DOI but lacks final printed page
numbers. Its final publication year and pagination are authenticated by the
publisher page and the subsequently acquired final article.

The controlling final paginated PDF was acquired from Springer at
`https://link.springer.com/content/pdf/10.1007/s00454-023-00581-2.pdf`,
HTTP 200, PDF magic verified, 29 pages, SHA-256
`5f591cedf7307d45f3becc62a220ecd2a5bda50324ec3dad01ed7eeb873918eb`.
Its header states the 2025 volume and pages; its first page records the
online publication date. The acquisition log preserves the returned final
URL, including its query parameters, without interpreting those parameters
as a failed download.

Both extracted texts have 1519 lines. A complete line comparison records
178 raw differences. After normalizing whitespace and removing running
headers, footers and publication-date metadata, the two 1091-line bodies
differ only in the order/position of the extracted two-part end-of-proof
glyph at the end of Lemma 3.17. The complete normalized diff was inspected.
This is an extracted-text comparison, not PDF raster identity or a claim
that every final page was separately reread as an image. Sixteen actual
final pages were viewed in eight image sheets: physical 1, 2, 4, 5, 7,
9--11, 14--17 and 20--23, corresponding to printed 264, 265, 267, 268,
270, 272--274, 277--280 and 283--286. The actual final formulas confirm
the nonempty-intersection signs lost in the extracted text.

The arXiv page lists 2012.12161v1, submitted 22 December 2020. No fresh full
reading of that preprint or underlying external dependency papers is
claimed. The controlling imported locators below are from the final
published article, not inferred from an abstract or an earlier version.

| Imported item | Final printed pages | Physical pages | Scope |
| --- | --- | --- | --- |
| Definitions 2.1 and 2.2 | 267 | 4 | Tropical toric strata and the ambient fan's compatibility/compactifying conditions relative to each recession cone |
| Definitions 3.1 and 3.8 | 270, 272 | 7, 9 | Faces of the compactification are closures of stratum faces; a complex must satisfy both stratum and global face-incidence conditions |
| Propositions 3.24 and 3.25 | 277 | 14 | Vertex description for a single polyhedron compactified in its own pointed recession-cone fan |
| Example 3.27 | 277 | 14 | Refining the ambient compactifying fan can change the boundary vertices; it is not equivalent to just subdividing the original complex |
| Lemma 3.31 and Theorem 3.32, including proof | 279--280 | 16--17 | A finite complex with recession fan has the stated stratumwise projected complex and its canonical compactified face complex |
| Theorem 4.8 and relevant closure construction | 283--284 | 20--21 | Face-poset computation from the original data; no fresh implementation run is claimed |
| Definitions 5.1 and 5.2, Proposition 5.4 | 285--286 | 22--23 | Signed incidence cancellation for cellular complexes, in addition to coefficient maps |
| Example 6.1 | 286 | 23 | The positive ray acquires one endpoint at infinity |

## Mathematical and admission boundaries

The ambient compatibility condition is quantified over each polyhedron and
each cone of the chosen ambient fan. The compactifying condition expresses
each recession cone as a union of ambient cones. In the canonical case the
ambient fan is the recession fan of the complex, so these conditions hold
in the sense used by the source. The new complex assertion is confined to
that case. The source's proof uses the common recession face to identify
intersections of projected polyhedra; that hypothesis is retained.

The positive-ray explanation is the source's Example 6.1, expressed as an
interval with a finite and an infinite endpoint. The vertex criterion is
quoted only for a single polyhedron compactified in its own recession-cone
fan. The source's refined-fan example is used only to explain the dependence
of the boundary on the ambient fan. Neither presentation claims that a
subdivision in a fixed compactification necessarily changes cohomology.

Computing a face poset is distinguished from computing tropical cohomology:
one also needs incidence signs and the coefficient maps. The known
compactification theorem supplies geometric boundary data, not local
Poincaré duality, a comparison with singular cohomology, a Monge--Ampère
regularity theorem, a metric limit or a solution of P05/P19.

The separate Lee audit finds a general projected-collection candidate
outside active TeX. It does not refute the specific matroid cohomology
theorems. The new book discussion uses the established recession-fan
construction; neither that candidate nor a proposed general repair is
promoted here. Lee's matroid-specific incidence remains a research task.

The repository protocol says: "Imported results, definitions, explanatory
reformulations, and direct formal consequences that are explicitly
identified as such remain subject to the ordinary mathematical and source
audits, but are not described as new results." This section is such an
ordinary import. It adds no formal theorem, proposition, lemma, corollary
or proof environment, makes no priority claim and has no new independent
production-model receipt. No old receipt is extended to the changed prose.

## Source and release gates

The baseline is work commit `0f0a66beea1954e19572890b2930473182663ba6`.
Exactly two of 425 active TeX inputs change: Appendix G and Appendix L.
Their existing 27 and 4 formal blocks, including proofs, remain
byte-identical and their old label order is preserved. Two new section
labels give 12,600 unique labels. A single bibliography entry is appended
after the preserved old bytes, yielding 584 keys and 285 cited keys.
The reference closure, all reference ranges and inventory checker pass.
All 108 protected Appendix M--N inputs remain byte-identical. The 42
complete problem status strings and the standalone catalogue source/PDF
are unchanged. The currently open catalogue editor is not changed or
reopened for this separate book-project edit.

The full native book build, bibliography/index/navigation checks and
selected actual book-page review are recorded in the accompanying release
manifest. They concern the new book edition. The older 4,259-page edition,
its thirteen-page cohomology review and frozen source archive retain their
separate dated scope. All earlier exports and manifests are preserved;
no old artifact is overwritten. Ordinary work-branch publication is
authorized, with incoming research checked first and no force push.
