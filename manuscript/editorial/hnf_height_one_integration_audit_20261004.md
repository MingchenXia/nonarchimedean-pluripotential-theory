# Height-one obstruction book integration — 4 October 2026

Chapter 5 now contains Example 5.5.5, immediately after the Sylvester
model. It applies the published Firla–Ziegler obstruction to a normal
affine toric family, showing why reducedness and integer decomposition
do not guarantee a smooth reduced toric subdivision at the original
height. Appendix L gives the exact provenance, and the bibliography
adds the published paper and the version-pinned September HNF preprint.
The current full book has **4,249 pages**. The 42 open statuses stay fixed.

## Mathematical and primary-source boundary

The controlling obstruction is Firla–Ziegler, Discrete Comput. Geom.
21 (1999), 205–216, DOI 10.1007/PL00009416, actual Example 10 on
printed page 213 and physical page 9. Its cone has a height-one
Hilbert basis and no Hilbert partition. Section 4, printed page 212,
describes the integer-program/CPLEX method; no independently checkable
infeasibility certificate for this example is reproduced here.
The nonexistence statement is explicitly imported as a published result.

The coordinate identification is also in actual Examples 6.4–6.5 of
Liu–Tang–Tao–Zhang, arXiv:2609.36818v1, physical pages 31–32. Its
Theorem 1.4 supplies the final constant-coordinate comparison; the
actual proof on pages 19–27 is checked in the
[source audit](hnf_height_one_source_audit_20261004.md). The source
acknowledges earlier two-parameter classifications, whose primary
proofs have not been freshly cleared. The complete HNF extracted text
is covered cumulatively, with 24 selected actual page views, and the
published Firla–Ziegler paper has a complete text and twelve-page
actual visual reading. Those scopes do not assert verification of
every imported antecedent or admission of the preprint's Ehrhart claims.

The example displays the integral map and its inverse, identifies the
homogenized cone of conv(0,e_1,e_2,(34,31,39)), and transfers the
published height-one/Hilbert-partition conclusions. Degree-one generation
gives IDP in every degree. The affine normal toric ring is flat over
C[tau], its generic fibre is a three-dimensional torus, and its
parameter ideal is the intersection of the four ray-prime ideals,
so the central fibre is reduced. Its primitive ray span has index 39.
A smooth toric subdivision with reduced central fibre over the same
parameter would slice to an excluded unimodular triangulation.
The conclusion is explicitly toric and at the original parameter;
it asserts no nontoric or after-base-change impossibility. A projective
subdivision would additionally require coherence.

The recent constant-coordinate IDP/coherent-triangulation equivalence
retains every dimension and parameter hypothesis and its earlier
provenance. It is not extended to arbitrary HNF simplices. This is
a known-source application and direct local calculation, with no new
formal theorem or independent production-model receipt. The separate
[exact finite enumeration](hnf_firla_ziegler_exact_enumeration_20261004.json)
clears IDP and the twelve-generator/161-candidate counts for this one
simplex; it is not a nonexistence certificate and is not substituted
for the precisely imported published result.

## Build, preservation and actual-page gates

The changed active book files are Chapter 5, Appendix L and
NonArchimedean.bib. The example adds one semantic label. Every old
theorem, proposition, lemma, corollary, definition, example, remark
and proof block in the two changed TeX sources remains byte-identical,
with its old label order preserved. The other 423 of 425 active TeX
inputs, including all 108 protected Appendix M–N inputs, remain
hash-identical to the preceding checked edition. Historical research
receipts and the current 42-atom inventory are preserved.

One required full build passes. The final log has zero TeX errors,
LaTeX/package warnings, overfull boxes, unresolved references/citations
or rerun requests. The 954 underfull diagnostics remain recorded.
All six reference-checker regressions pass. There are 12,582 unique
labels, 172 valid reference ranges, 5,464 citation groups and 5,708
citation uses. All 281 cited keys resolve among 580 bibliography keys;
BibTeX reports zero warnings. MakeIndex accepts 725 entries, rejects
none and writes 964 lines with zero warnings.

All **70 selected actual pages in eighteen contact sheets** were
viewed. The new example occupies physical pages 207–209, its source
notes are on 228–229, and its provenance record is on 3977. The
selection includes the adjacent Sylvester example and cofinality
discussion, changed-unit seams, affected contents, all index pages
4227–4236 and all reference pages 4237–4249. No clipping or collision
was observed. This is a scoped visual gate, not a fresh whole-book
or whole-Chapter-5 visual reading.

Navigation checks find zero invalid targets among 21,423 named
destinations, 46,098 internal links and 2,433 contents/bookmark entries.
All 724 index page groups resolve. The 163 external URL links are
counted; remote target health is not claimed. Post-render references,
exact source hashes, inventory and whitespace checks pass. There
remain 42 atoms in twelve families with tier totals 0/3/7/15/17.

The [manifest](hnf_height_one_integration_manifest_20261004.json)
and [active-source ledger](hnf_height_one_integration_source_closure_20261004.sha256)
pin the checked source, full build and actual-page scopes. A full PDF,
selected-page review and source archive are saved separately under
`/workspace/book-completion-drafts/research-integration/`; the earlier
4,246-page artifacts stay historical. Exact archive input-byte checks
are separate from a fresh build from that archive or font portability.
Normal publication to work and incoming-user-research fetches continue.
Further related-paper research and remaining global model inputs stay
in the cloud, with Xean setup suspended.
