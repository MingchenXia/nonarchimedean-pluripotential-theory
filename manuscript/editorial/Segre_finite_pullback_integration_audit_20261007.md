# Segre degrees, integral dependence and finite pullbacks: integration audit

Date: 7 October 2026. Baseline: work commit
`a4f38584d6c7bc7fe4ccf7396ed24fdd12e169a9`; observed main
`00957114db21b627e97369563032ceda9cea09c7`.

## Result and source scope

The book now connects ideal singularities, global intersection data and
local hypersurface invariants in Appendices C.9, F.9, H.19 and L.77.
The final build has 4,518 pages, 20,981,582 bytes, SHA-256
`1d27bdefa89d276f7bef6f912b3755e75769321c65a8bae86ff4ee446698573a`.
The separately frozen [primary-source review](Segre_finite_pullback_source_review_20261007.md)
and [source manifest](Segre_finite_pullback_source_review_manifest_20261007.json)
are reused exactly. They cover 131 distinct PDF/page pairs in 70
individually displayed sheets: thirteen PDFs, five complete and eight
partial readings. There is no fresh primary-page reading at this
integration checkpoint. All primary versions, physical/printed page
locators, acquisition hashes and actual reading notes belong to that
preceding source record; uninspected journal versions are not substituted.

The controlling global source is Yairon Cid-Ruiz, *Segre classes and
integral dependence*, Math. Ann. 395, article 101 (2026), DOI
10.1007/s00208-026-03532-3, published online 6 July 2026. All 23 pages
of its published PDF were read. The arXiv 2512.08863 version history
is metadata only. The controlling local source is Jelonek, Jorge Pérez
and Araújo dos Santos, *Finite holomorphic pullbacks, Segre numbers,
and generic Lê numbers*, arXiv:2610.07528v1, submitted 5 October 2026,
23:51:22 UTC; all seventeen physical pages were read. The source
manifest records the exact scopes of the other eleven inputs.

## Mathematical integration

C.9 imports the published Theorem A/4.3 for an equidimensional
projective scheme over a field, an ample line bundle and nested closed
subschemes W contained in Z. The reversed ideal inclusion is explicit.
Integral dependence is equivalent to the specified Segre-class
equalities and equality of every polarized Segre degree. Codimension
indices and signed global degrees are distinguished from local generic
Segre numbers. The proof roadmap retains the source's Rees comparison,
Vogel/residual cycles, Snapper growth and positive-growth obstruction.
The intersection-theoretic, Kleiman–Thorup and multigraded vanishing
inputs are imported, without a recursive independent proof claim.

C.9.1 imports Corollary 5.2 for nested homogeneous ideals: equality of
the stabilized Segre zeta functions is equivalent to equality of
integral closures. The argument needs projective dimension above the
generator counts, equality of saturated **integral closures**, the
associated-prime height bound and faithful-flat contraction. One Segre
class in the original projective space need not detect the vertex.

F.9 works through published Example 4.7. Blow up a point of projective
three-space, then a line in its exceptional plane. The pullback of
O(1) is big and nef. Distinct divisorial ideals of E and kE, k at
least two, remain integrally closed with orders one and k, while their
Segre degrees for that polarization vanish. The surface intersections
use the trivial restriction of the line bundle; the zero-cycle term
also needs the degree-zero normal bundle of the line. The displayed
normal exact sequence does not assert splitting. Thus ampleness in
C.9 cannot be silently replaced by a nef model polarization.

H.19 explains the local analytic setting, including its exception to
the appendix's compact-Kähler default. It uses ambient Jacobian ideals
at critical points and writes e_j = c_(n-j), with generic Lê number
lambda^i = e_(n-i). Smooth finite germs give componentwise extension
bounds between e_j(Q) and degree times e_j(Q); only the top invariant
has the stated exact degree formula. Integral-closure invariance deals
with unit changes of defining functions.

For a reduced target equation whose pullback is a unit times h^r,
the chain rule controls h^(r-1)J_h. Multiplicity one gives the cited
lexicographic ideal comparison. Isolated singularities have the known
Milnor comparison for every multiplicity; the stronger degree factor
is stated only for multiplicity one. The cyclic-cover trace is localized
over a smooth cover and has degree d/r. Wells' injection is for proper
equal-dimensional smooth manifolds over complex cohomology. The selected
Stacks differential trace requires finite syntomic maps. None of these
inputs licenses arbitrary singular-origin module traces or integral
cohomology surjectivity.

The componentwise Segre and generic Lê conjectures are equivalent
formulations of one open comparison, and include arbitrary multiplicity.
Their weaker lexicographic frontier has its known multiplicity-one
and isolated cases. Generic and merely prepolar coordinates are
separated: in critical dimension one, coordinate excess adds the same
nonnegative amount to the two Lê numbers. The identity-map example with
different coordinate choices tests this distinction, not the generic
conjecture. The source's Example 7.3 has transverse Milnor number one
on both sides, with tuples (0,1,8) and (0,1,24). A finite map in the
singular direction keeps the tuple (0,2,0), excluding a blanket degree
factor for every nonisolated coordinate. Higher-multiplicity slicing
requires the stated compatible smooth finite cuts and pulled-cut
multiplicity conditions. The Massey perturbation theorem concerns one
germ with its coefficient/exponent threshold, not an automatic nonlinear
pullback comparison. The forward hypersurface-to-foliation/Koszul
smoothness route remains separate from the reverse trace-first-integral
nonconstancy interface. L.77 records these boundaries and exact sources.

## Preservation and statement status

Only four active TeX inputs and ComplexGeometry.bib change. The other
421 active inputs, all 108 protected inputs, 113 preceding frozen
manifests and 190 prior exports remain byte-identical. Every preexisting
line in the four changed appendices remains in order. All 84 old formal
blocks and all 39 old proof blocks are byte-preserved. The two new
unnamed formal blocks are an attributed published theorem and an
attributed published example; there is no new proof block or original
result. Twenty-four labels, five index entries and twelve version-specific
bibliography keys are added. Fourteen new explicit equation tags
C.31–C.34, F.18–F.20 and H.80–H.86 preserve all 131 legacy equation
numbers, including C.18a–C.18e.

The 42 canonical atomic statuses and the native 86-page open-problem
catalogue remain unchanged. The open editor is neither modified nor
reopened. No new canonical problem or solved status, new independent
model call, production receipt or extension of a historical receipt is
claimed. The user-specified independent gpt-6.1-sol xhigh verification
gate remains applicable to future original candidates. The unverified
elliptic density diagnostic is unused. BJ22 Theorem 6.21's changing
coefficient residual problem and critical input (SD)_k remain unresolved;
these Segre imports do not repair the general Siu/envelope route.

## Validation and actual final reading

The final required command
`TEXMFHOME=/workspace/.texlive scripts/validate-manuscript.sh` completed
with exit code zero, including refcheck, the 42-problem inventory,
refcheck unit tests and the complete latexmk build. The final log has
no TeX errors, package/pdfTeX warnings, missing characters, overfull
boxes, unresolved references/citations or rerun requests. The 954
preexisting underfull boxes are unchanged. Bibliography: 510 cited
entries, 803 keys, zero warnings. Index: 811 accepted entries, zero
rejections or warnings, 810 page groups and 440 numeric destinations.
Navigation: 22,513 named destinations, 47,893 internal links, 171 URL
links, no invalid destinations or internal links, 2,662 contents entries
and six parts. All new and legacy equation destinations are checked.

All 67 selected final physical pages are covered by complete matching
text and image reading in 34 sheets: 51 pages/26 sheets freshly read
in the final PDF and 16 pages/eight sheets admitted by exact whole
selected-text and matching-image identity with preceding actual notes.
The selection includes all inserted C/F/H/L sections, openings/seams,
selected contents entries and the complete index and bibliography.
The repaired H opening is freshly read. The final reading record hash
is `9fff80b99bc7ff865e3688c7a10f773f00651e0567874f1ee81631b6e4eaee90`.
No pending repair remains. This is a scoped final review, not a new
4,518-page whole-book reread or recursive certification of all primary
proof chains.

Diagnostics remain separate immutable records: the first source-gate
helper assumed consecutive old C tags and was corrected to include
C.18a–C.18e; the first layout had one long-word overfull box, repaired
before final reading; the first view selector matched the wrong preceding
dependency-map heading and was corrected before use. Eighteen pages
were actually read in the second PDF before the H opening scope omission
was found. That partial record retains the repair and remaining unread
pages. The third PDF, fourth source gate and third release gate are the
final identities. Earlier diagnostics and prepared unread views are not
silently relabeled as final evidence.

The first packaging helper stopped before writing any release output
because it treated nested source-record pins as flat records. The preserved
diagnostic and second helper verify the actual record/content schema;
no source, build or reading evidence was changed by that repair.

## Artifacts and publication

The [integration manifest](Segre_finite_pullback_integration_manifest_20261007.json)
pins the source/build gates, actual reading notes, preservation inventories
and helper sources. The [artifact record](Segre_finite_pullback_integration_artifacts_20261007.json)
pins the full book, selected-review PDF and source archive. The
[source closure](Segre_finite_pullback_integration_source_closure_20261007.sha256)
contains all 425 active inputs and two bibliography files. Every source
archive member is checked against current bytes; this does not claim a
fresh compilation from an isolated archive. Publication uses the existing
work branch and draft PR 2 with an expected-parent, non-force update.
The standing GitHub authorization applies; any incoming author changes
must be reconciled before publication. Subsequent remote publication
records remain distinct from this immutable prepublication release.
