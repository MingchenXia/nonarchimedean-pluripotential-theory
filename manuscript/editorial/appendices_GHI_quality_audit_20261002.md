# Appendices G--I quality audit

Date: 2 October 2026. This is a direct mathematical, source, editorial and
rendered-page pass under the sequential whole-book programme. It supplies
no new independent solver/verifier verdict and changes no archived receipt.

## Complete source scope

All three complete sources, including their proofs, examples, warnings,
tables and source notes, were read. G supplies tropical algebra and the
calibrated analytic interface; H supplies the precise complex reference
formulas; I records algebraic dependencies at their actual hypotheses.

| Appendix | Lines | Labels | Labelled headings | Reusable environments | Assertions/proofs |
|---|---:|---:|---:|---:|---:|
| G | 767 | 62 | 12 | 26 | 5/5 |
| H | 918 | 35 | 15 | 18 | 8/8 |
| I | 817 | 41 | 34 | 7 | 0/0 |

The 2,502-line scope has 138 labels, 61 headings, 51 reusable environments
and 13 assertion/proof pairs. Every reusable environment and heading has a
semantic label. No appendix input fragment is changed. The other 119 files
in the appendix closure are preserved: 113 match the entry baseline and
six match their completed A--F gates. All 108 frozen input fragments remain
unchanged, as do the research inventory and archival receipts.

## Mathematical repairs

G proves the natural-order axioms, includes the fraction-field support
hypothesis, and proves character continuity using finite minima. Its
initial-form rule now distinguishes cancellation in the old degree from a
possibly nonzero initial form in the new degree. The Laurent-polynomial
construction retains collected nonzero coefficients and uses a weighted
graded algebra without assuming the real weights are realized in the
ground field.

Analytic calibration uses the convenient cells and finite flat local degree
of CLD Section 14.3.2. The local degree is an integer; the coefficient after
an inverse real lattice map need not be. The map's topological compactness
and the target calibration's local finiteness are stated explicitly.
Global pushforward additionally requires properness on the support.
Balancing is restricted to boundaryless preimages of the relevant faces.
Primitive normals point into incident cells. For a top-degree superform,
pullback contributes the square of the determinant and ordinary change of
variables removes one factor, leaving the lattice index. New examples
check the cancellation of degree two against inverse index two and show
why an infinite target fibre obstructs a locally finite calibration.

H defines ordinary singularity equivalence by mutual inequalities, avoiding
subtraction at a common pole. The log-log example checks subharmonicity,
zero Lelong number and dimension-one full mass. The nonpluripolar section
distinguishes restricted truncation currents from the closed limiting
current, and pairs mixed products with a complementary Kähler power when
discussing mass. Modification invariance is stated as a pushforward identity.
Decreasing continuity uses a big class and the common singularity type,
including the limit; increasing-net continuity has its separate import.

Relative energy is defined without silently translating away the energy
constant. Its proof uses relative nonpluripolar integration by parts and
the precise mixed-integrability and tail estimates. Relative d1 completeness,
energy continuity and the pointwise monotone convergence criterion are
distinguished from the singularity-type metric dS. Domination is a separate
positive-mass import, not a formal consequence of comparison. Model-envelope
and ideal-envelope results retain their different hypotheses and proofs.
The multiplier-ideal reconstruction is local at a germ with one uniform
positive margin for every divisor over that neighbourhood. Quasi-equisingular
approximation records limiting scaled ideals, not exact equality of every
individual approximant's ideals. The relative geodesic equation uses the
nonpluripolar product; its metric assertion follows from Busemann convexity
and the triangle inequality. Test-curve maximality and parameter upper
semicontinuity remain required in the ray correspondence, including the
ample case.

I labels all 21 principal tag entries and four dependency chains, and adds
57 compiled-source entries with stable links, hypothesis signatures and
first source owners. The principal ledger records principal applications;
it does not misrepresent these as the earliest textual occurrences. The
discovery scan found 81 apparent identifiers: 0417 and 0642 are decimal
fragments in numerical examples, not tag citations; 0DSV is an explicitly
rejected Picard citation, not an imported theorem. Thus 78 dependency tags
are catalogued, including the inherited separatedness input, and the
rejected identifier is explained separately. Tag 0B90 supplies vanishing;
the preserved curve argument separately invokes Riemann--Roch. Section
tags 01PR and 0C5Q name the particular proposition/item used. The scheme
boundary and the algebraic-space theorem used only for schemes are explicit.

## Primary source witnesses

Seven PDFs were read at 41 selected physical pages and visually inspected
in fourteen contact sheets. The two tropical witnesses were downloaded
for this unit; the five complex witnesses reuse the previously acquired
Chapter 51 source files. These checks corroborate the precise imported
statements and selected proofs; they do not claim a fresh complete proof
audit of every source book or paper.

| Witness | Selected physical pages | Checked input |
|---|---|---|
| CLD, arXiv:1204.6277v2, 608 pages | 1, 405--410, 429--433 | Sections 14.3--14.5, Theorem 15.6.1 and the compact-support/global distinctions |
| Mikhalkin--Rau, November 2018, 261 pages | 1, 10--15, 30--32, 102--104 | Integral-affine conventions, saturated lattices and balanced cycles |
| Xia supplied book, 549 pages | 87, 117, 124, 126, 136, 154, 160, 166, 169, 174, 311 | Relative domination; energy tails and variation; relative geodesics, d1 and Busemann convexity; Theorem 9.2.1 |
| DDNL, arXiv:1705.05796, 38 pages | 7 | Theorem 2.3 capacity convergence with the mass condition |
| BEGZ, arXiv:0812.3674v2, 54 pages | 7--8 | Proposition 1.6 mass bound and Theorem 1.8 closedness |
| Boucksom notes, 48 pages | 46 | Corollary 10.18, including the uniform margin and normalization conversion |
| PSWZ26, 59 pages | 4 | Theorem 1.2, big-class idempotence also at zero mass |

The relative-energy imports were checked against Xia Proposition 3.1.3,
Proposition 3.1.14, Lemma 3.1.3 (3.32), Corollary 3.1.6, Proposition
3.1.18 (3.40)--(3.43), Proposition 3.1.19 and Lemma 3.1.11. The metric
locators are Lemma 4.3.1, Theorems 4.3.2--4.3.3, Lemma 4.3.5 and
Propositions 4.3.3/4.3.5. The ray import is Theorem 9.2.1 (9.19)--(9.21).
Temkin's graded-reduction background and the older classical references
remain precise source imports; no fresh complete PDF review is claimed.

All 81 discovered Stacks pages were retrieved with byte digests. The exact
statements of all 21 principal and 57 supplemental entries, and the rejected
0DSV statement, were read, together with their compiled application scopes.
The two numerical false matches were excluded. Full statement extraction
uses each page's main article, including Theorem and Proposition headings,
rather than accidentally starting at its first referenced lemma. Selected
proofs were also read; a complete proof review of all 78 imports is not
claimed. In particular, Tags 03H0, 0815 and 0CND retain their theorem or
proposition statements; 02K9 and 01OF retain their exact lemma signatures.

## Calculation and mechanical gates

Twelve finite calculation families pass 118,721 checks: tropical order and
distributivity, min/max conversion, degree/index cancellation, top-form
determinants, finite partial sums in the infinite-fibre example, balancing,
initial-degree cancellation, one-pole integer thresholds, a uniform
valuation margin, radial log-log derivatives, the ordered-rooftop distance
and finite witnesses for the endpoint-drop example. These are checks of
the explanatory examples, not certificates of the general analytic imports
or of an infinite limit.

The final full build succeeds with 4,164 pages and 19,445,205 bytes. The
appendix scope has no overfull box. Five underfull table paragraphs in G
were inspected and are readable. Eighteen inherited overfull boxes elsewhere
and the inherited class-path warning remain for the whole-book pass.
There are no missing references, citation warnings, missing glyphs or
duplicate PDF destinations.

All 46 appendix pages and two seams were visually reviewed in twelve sheets:
G physical 3813--3824 (printed 3743--3754), H 3825--3840 (3755--3770),
I 3841--3858 (3771--3788), plus 3812 and 3859. A final navigation wording
change in I was rebuilt and its affected sheets inspected again. Terminal
blank pages are intentional chapter alignment. Warning boxes, equations,+the sign table and all supplemental table continuations are readable.

Post-render references pass for 425 inputs and 12,488 labels, with no
missing input, duplicate label or dangling reference. Six checker tests,
the unchanged 42-atom/12-environment research inventory, the scoped
label/delimiter/preservation substitute for the unavailable legacy audit,
and whitespace checks pass.

## Exact artifacts and continuation

Source SHA-256 digests:

- G: c08da1c4a1c407f48d80cfae8003eb6cc3eaa7ea29e693cec54da9d02735ef8b
- H: c441da04d04a55aa05d79f2bd73ba8e62e9269b17c55cf651eaa7cb8a07c72f8
- I: 9962150005429669f453dddbede81248041495114d385f5c7a8321707df09955

PDF SHA-256: 2d7bc147fb4d435c0834613e25f60659213228633e48514edc8db82af30fdd3d.
Review copy: /workspace/book-completion-drafts/Appendices_GHI_Final_Review_2026-10-02.pdf.
Local scope, source and render manifests are
`/tmp/appendices_GHI_scope_20261002.json`,
`/tmp/appendices_GHI_primary_20261002/manifest.json`,
`/tmp/appendices_I_primary_fetch_20261002.json`, and
`/tmp/appendices_GHI_render_20261002/manifest.json`.

Appendices A--I are complete under this programme. J--N and front matter
are next, followed by the final whole-book gates. Work remains local
pending explicit remote-push approval; independent research remains paused.
