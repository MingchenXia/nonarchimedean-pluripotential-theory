# Resistance, tau and tropical moments — integration audit

Date: 6 October 2026. Baseline work commit:
`a58604541705054e03d1afade88210c52ea6746f`.
Baseline main commit: `00957114db21b627e97369563032ceda9cea09c7`.

Chapter 8.1.5 now connects its Green-function calculus with effective
resistance, the tau invariant, tropical Jacobian moments and Wang's
new uniform positivity theorem. Appendix L.59 records exact editions,
source restrictions and auxiliary formula issues. This is an attributed
integration of known results and checked proof mechanisms. It does not
admit an original theorem or certify the entire external proof chain.

## Mathematical scope and normalization

The conductance matrix is `Q = partial D_L^{-1} partial^T`, with sign
opposite to the book's outgoing-slope Laplacian. Resistance is the
minimum energy of a unit flow. With the normalized potential satisfying
`Delta h = delta_p - delta_q`, resistance is `h(q) = D(h)`.
Tau is one quarter of the resistance-function energy; its source-point
independence is attributed to the cited primary results.

The edge Foster coefficient is `F(e)=1-r(e^- ,e^+)/L_e`, zero for a
bridge and one for a loop. Its sum is the cycle rank. The source formula
`tau=A/12+B/4` is stated with a source that is a model vertex. The
cycle lattice uses integral homology and the edge-length quadratic form.
Its moment is the full averaged squared norm on the Voronoi cell, with
no half-factor: `I=ell/8-tau/2`. A tree has `tau=ell/4` and `I=0`;
a circle has `tau=I=ell/12`. The circle's Euclidean Jacobian
circumference is `sqrt(ell)`. These quantities scale linearly with graph
lengths; they must not be confused with the lattice circumference.

Wang's preprint supplies a positive constant `c_-`, the root in
`(0,1/12)` of `c(1-4c)^2=4/(27 pi^2 e^2)`, approximately
`0.002065443945`. The bound is
`tau >= c_-(ell-b)+b/4`, where `b` is total bridge length. The explained
mechanism combines the dual-lattice moment bound, the cographic rank
formula, Edmonds' three-set partition and Hölder's inequality. Isolated
vertices are retained when counting components. Bridge deletion and
two-edge-cut reduction retain their separate effects; the latter keeps
new loops and preserves the cycle lattice, total length, moment and tau.
The tree case is handled before any division by a reduced graph length.

The cubic family is described with its vertices, triangles and
connectors. It has `6M^2` vertices, `9M^2` edges and total length
`15M^2` for `M>=3`. Its two exact Foster coefficients, triangle-to-star
energy comparison and limiting normalized tau `59/7260` are attributed
to the checked source. This is below `1/108`; the source gives finite
counterexamples for `M>=300`. The best universal constant remains open,
with the stated lower and upper bounds. This related direction is not
a new admission to the canonical 42-atom inventory.

The height application is restricted to semistable geometrically
connected smooth projective curves of genus at least two over a number
field. The geometric dual graphs of minimal regular models have the
specified unit lengths. The finite correction is
`[k:Q]^{-1} sum_v I(Jac(Gamma_v)) log N(v)`, with `N(v)` explicitly
the residue-field cardinality. The height paper's half-moment convention
and coefficient two cancel. Uniformizer-normalized valuations, the
arithmetic logarithmic weights and archimedean terms remain distinct.
Appendix A's incidence matrix is distinguished from the scalar tau
energy notation.

## Exact primary-source reading reused

The [preceding source review](tau_invariant_source_review_20261006.md)
and [its manifest](tau_invariant_source_review_manifest_20261006.json)
freeze 108 physical pages read and displayed in 56 sheets. This
integration reuses those exact records and claims **zero fresh primary
pages**. The reading comprises all fifteen pages of Wang
`2610.04994v1`; all 31 published tropical-moment pages, twenty published
Rayleigh pages, six Edmonds partition pages and thirteen Cinkir v3
pages; thirteen of 33 physical pages of the published height PDF; and
ten of 47 physical pages of Baker--Rumely v2. Unselected pages,
unread journal editions and further external antecedents remain unread.

Seven new bibliography keys identify these exact versions. Published
editions and arXiv versions are not silently identified. The source
manifest SHA-256 is
`4b340eefd83165d3d9d655f763404a137e4cfb0a76752ab2661bfb38491b75e7`.

Fourteen source diagnostics remain in the frozen source review. The
moment interpolation is restricted to a vertex source; the unequal-edge
derivative requires the correct denominator; the random-tree diagonal
sum is distinguished from the off-diagonal convention. Parallel edges
and loops require suitable models rather than an unqualified simple
matrix formula. The grounded-inverse average requires centering to give
Moore--Penrose. A rank-one single-edge contraction cannot use arbitrary
charges inside that open edge. The checked main proof uses the separate
valid inputs. These auxiliary errors do not constitute counterexamples
to Wang's main conclusions or the final tropical-moment identity.

## Source preservation and validation

The two edited active inputs are Chapter 8 and Appendix L. All 99
existing formal/proof blocks retain their exact baseline bytes: 77
statement/explanatory blocks and 22 proof blocks. No new formal
environment is added. Ten tags `8.8a` through `8.8j` give distinct
equation numbers and PDF anchors while preserving the existing Green
equations. Twelve labels and seven bibliography keys are added.

Reference checking passes for 425 active inputs and 12,874 unique
labels, with no missing inputs, duplicate labels or dangling references.
There are 391 cited entries and 686 unique bibliography keys. The final
compile has zero TeX errors, package warnings, PDF warnings, missing
glyphs, overfull boxes, unresolved references or rerun requests. Its
954 underfull boxes equal the preceding release's count.

The index accepts 767 entries and rejects none, with zero warnings and
420 valid numeric destinations. Navigation has 22,010 named destinations,
47,116 internal links, 171 URL links and 2,570 TOC entries; all tested
internal links and destinations resolve. All six parts are present.

All 423 other active inputs, 108 protected inputs, 74 prior frozen
manifests and 127 prior exports preserve their baseline bytes. The other
bibliography is unchanged. Canonical inventory checking passes with
42 atoms in twelve families and tier counts `0/3/7/15/17`; complete
status rows are byte-preserved. The inactive toric entropy candidate
remains OPEN. The native catalogue source, 86-page PDF and open editor
are unchanged and are not freshly compiled or reviewed here.

## Rendered review and release scope

The final v3 book has **4,407 pages**, 20,480,968 bytes, SHA-256
`986de5227d4ef10979674897c4830867e5e09826a78c2d3d247c2e138bb91c79`.
All 43 selected matching physical pages were read as complete extracted
text and displayed as original page images in 22 sheets:
`12, 69, 327, 328, 335--340, 4168--4171, 4379--4407`.
They cover affected contents, the chapter roadmap, Green-to-tau-to-slope
transitions, the full new subsection, Appendix L transitions, the entire
ten-page index and the entire nineteen-page bibliography. The source
and notation corrections are legible in the final render. Newly added
index destinations and the seven cited editions match their text.

This is not a fresh whole-book rereading. The earlier ordered reading
of all 72 chapters, Appendices A--N and nine front-matter files remains
the separately frozen second-reading checkpoint. Here, v1 compiled but
had 34 duplicate anchors and received **zero** PDF page review. After
anchor repair, v2 received **only fourteen** pages in seven sheets;
its remaining index and bibliography were not reviewed. The final v3
also corrects the chapter's self-contained dependency claim, the
residue-cardinality definition and the incidence-matrix notation.
Only v3 receives the complete 43-page review claim.

Frozen final source-gate SHA-256:
`5ea6b63f79d27dbe3c7e2f60650749d9cf1efa59d99c0471ad7f042aa0e6a180`.
Final release-gate SHA-256:
`dce9e34996497f127a6e248cb6fae2159f75006f9c41b0bde4a26dcacde655fd`.
Final reading-record SHA-256:
`a7bb2d1d22084e627ab4d1f50d4abe32fb00eb5d29a0e8bde8a1c9d738b4c09f`.
Final view-manifest SHA-256:
`7da8ebdc5a7b2b0aa417bc53d3c96491766a85e8c1fa956b91ab80a03e082394`.

The release manifest and artifact record pin the complete book, the
43-page review PDF and a 684-member source archive. Every archive member
is byte-compared with its saved source; all 425 active inputs and both
bibliographies are included. No fresh isolated archive compilation is
claimed. Frozen preceding artifacts and the native catalogue are reused
without overwrite.

Routine GitHub synchronization is already authorized. Fetch both main
and work and integrate any incoming author work before publication on
work; retain the existing draft PR. This checkpoint adds no original
result, independent model call, production receipt, canonical solved
status or general BJ22 Siu/closure repair. Next perform usage-aware
bibliography polish while preserving distinct editions and historical
verification packets.
