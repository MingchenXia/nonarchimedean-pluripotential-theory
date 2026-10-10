# A cyclic height-one local model — 4 October 2026

Chapter 5 adds Example 5.5.6 after the Sylvester model and the IDP
obstruction. It gives an explicit positive comparison: the known cyclic
quotient `1/15(1,2,4,8)` has a projective smooth toric subdivision whose
central fibre remains reduced over the original parameter. Appendix L
records the precise local scope; one version-pinned bibliography entry
is appended. The current full book has **4,253 pages**.

## Mathematical and primary-source boundary

The controlling known example is Sato--Sato,
[arXiv:2004.03522v4](https://arxiv.org/abs/2004.03522v4), Example 3.10,
physical page 12, revised 10 September 2020. The source's Theorem 3.1
concerns its Fujiki--Oka procedure; Proposition 3.9's iterated-term
nonexistence conclusion is explicitly toric. Neither is expanded to
every resolution procedure or a nontoric obstruction. The displayed
stars are checked directly without identifying their order with every
implementation of that algorithm.

The [source audit](fujiki_oka_and_two_parameter_source_audit_20261004.md)
and [source manifest](fujiki_oka_and_two_parameter_source_manifest_20261004.json)
give the fresh version, text and actual-page scopes. Ten Sato--Sato
source pages, all six single-author Sato pages, and seventeen selected
Dais--Haus--Henk preprint pages were actually viewed. These are separate
bounded scopes. The final Dais journal proof and every algorithmic or
Hilbert-basis antecedent have not been freshly cleared. Its inspected
support-function gluing requires a height-compatibility choice not
spelled out in the selected proof; this does not disprove the main
classification. None of that unclosed gluing is used in the new example.

The lattice is `N=Z^4+Z(1,2,4,8)/15`, with primitive height character
`h=x1+x2+x3+x4`. The normal affine family is flat over `C[tau]` and has
generic three-dimensional torus. Its original cone has index fifteen
and a reduced central fibre. Four specified global star subdivisions
produce 4, 7, 11 and 15 maximal cones; each final determinant has
ordinary absolute value `1/15`, hence lattice multiplicity one.
All eight primitive rays have height one.

The [rational calculation](research_calculations/fujiki_oka_height_one_20261004.py)
and [finite certificate](research_calculations/fujiki_oka_height_one_20261004.json)
record every cone, stage volume and source remainder term. The explicit
lifting assigns heights zero to the original rays, then
`1, 1/8+2^-10, 1/4+2^-20, 1/2+2^-30` to the four added rays.
All 120 support-plane inequalities are checked exactly, with equality
precisely at each cell's four vertices. Scaling the homogeneous lifting
by `2^30` gives integral dual-lattice slopes and verifies projectivity.

On each regular maximal chart the parameter is `tau=z1*z2*z3*z4`.
Completion over `C[[tau]]` is a strictly semistable local model without
changing the parameter. No compact-family gluing, arbitrary-field
classification, new general theorem, open-problem solution or
independent production-model receipt is deduced. The BJ22 critical Siu
input and its dependent general-envelope boundary remain conditional.

## Build, preservation and actual-page gates

The changed book sources are Chapter 5, Appendix L and
NonArchimedean.bib. All old theorem, proposition, lemma, corollary,
definition, example, remark and proof blocks in the two changed TeX
sources remain byte-identical, with their label order preserved. One
known-source example and one label are added. The other 423 of 425
active TeX inputs, including all 108 protected Appendix M--N inputs,
are unchanged relative to the preceding checked Siu edition `de9515a`.
Historical receipts and all 42 research statuses are preserved.

The first required full build exposed one overfull lifting display.
It was split into two lines and a justified corrective full build passed.
The final log has zero TeX errors, LaTeX/package warnings, overfull
boxes, unresolved references/citations or rerun requests. The 954
underfull diagnostics remain recorded. All six reference-checker
regressions pass. There are 12,591 unique labels, 173 valid reference
ranges, 5,474 citation groups and 5,718 citation uses. All 282 cited
keys resolve among 581 bibliography keys; BibTeX reports zero warnings.
MakeIndex accepts 727 entries, rejects none, and writes 967 lines with
zero warnings.

All **64 selected actual pages in sixteen contact sheets** were viewed.
The new example occupies physical pages 211--212 and its provenance
record is on 3982. The selection covers the adjacent comparisons and
cofinality discussion, Chapter 5 source notes, changed-unit seams,
scoped contents including Chapter 5, retained Siu-conditional provenance,
all index pages 4231--4240, and all reference pages 4241--4253.
No clipping, collision or unresolved citation was observed. This is a
scoped gate, not a fresh whole-book or whole-chapter visual review.

Navigation finds zero invalid targets among 21,432 named destinations,
46,135 internal links and 2,433 contents/bookmark entries. All 726
index page groups resolve. The 163 external URL links are counted;
remote target health is not asserted. Post-render references, inventory,
exact source hashes and whitespace checks pass. The active inventory
remains 42 atoms in twelve families with tier totals 0/3/7/15/17.
The separate 86-page catalogue is unchanged from the Siu correction.

The [integration manifest](fujiki_oka_height_one_integration_manifest_20261004.json)
and [active-source ledger](fujiki_oka_height_one_integration_source_closure_20261004.sha256)
pin the final build and scoped actual views. The full PDF, final
64-page review and source archive are saved separately under
`/workspace/book-completion-drafts/research-integration/`.
Earlier dated PDFs and archives remain historical. Archive byte checks
do not claim a fresh build from the archive or font portability.
Normal work-branch publication, incoming-research checks, and related
research continue in the cloud.
