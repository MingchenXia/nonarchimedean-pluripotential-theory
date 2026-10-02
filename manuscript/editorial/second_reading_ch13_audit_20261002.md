# Chapter 13: second reading audit

Date: 2 October 2026. The complete original 2,498-line source,
`parts/part2/ch13_forms.tex`, was freshly read continuously. It has no
active fragments. The revised source has 2,573 lines, preserves all 92
labels and 67 formal environments, and leaves 37 environments byte-identical.
Thirty environments change. The complete mathematical diff and the final
edited contexts were checked.

The introduction retains finite polyhedral images for compact domains and
local image germs in general. Its import list now includes the measure
construction, test-form topology and their published compatibilities;
it no longer claims that only four analytic inputs are imported.

Chart morphisms are restrictions to their polyhedral support. Ambient
integer-affine extensions agreeing on that support are identified, and
their pullbacks agree on tangent spaces. Thus the compact-domain
equalizer is an actual equality of morphisms. The noncompact warning
distinguishes existence of the category and its functor from the
filteredness established by the compact argument. Equality of two
representatives is tested on the actual product tropical image, rather
than on the larger auxiliary Cartesian product of supports.

The surjective-pullback proof does not assume local finiteness of the
family of images of source cells. A locally finite Euclidean source
complex has countably many cells. On a fixed target cell, the images
whose intersections have smaller dimension form a countable null union;
the full-dimensional intersections cover a dense subset. Tangent lifts
there and continuity give the kernel condition on the whole target
cell. Dimension zero is handled directly. The nonsurjective warning
uses the inclusion of a point into an interval, with explicit killed
functions and positive-degree forms.

The discrete example from CLD25 Remark 3.4.3 is identified as an abstract
G-tropical example. It is not used to claim a Berkovich counterexample.
Ordinary stalks are computed using compact analytic neighbourhoods with
the point in their ordinary interior. Such neighbourhoods can be finite
affinoid unions; goodness is not needed. Restricting their moments to
ordinary interiors identifies the ordinary germ system, without replacing
ordinary stalks by arbitrary G-domain germs. A local skeleton is no longer
given as an example of an analytic domain.

The radial annulus has explicit positive finite radii. The type-two
tripod example treats discs attached along every arm: off the tripod,
the disc radius is less than both distances to 0 and 1. The positive-
bidegree form chi d''x1 vanishes on collapsed residue branches and on the
vertical arm, although its coefficient function may remain nonzero there.
Its compact support is contained in an explicitly bounded affinoid
domain and is not an ordinary open neighbourhood of the vertex. The
unbalanced comparison is a weighted polyhedral test, rather than a
purported interior analytic example forbidden by harmony.

The differential-kernel proof defines its previously missing Omega and
uses relative cell interiors and density at faces. Derivative coefficients
are finite signed sums. Ambient differentiation followed by the quotient
agrees with tangent differentiation. Normal variation alone does not make
a form zero, as the two axis examples show. Rank-one differential forms
in higher dimension are not confined to the top-level skeleton.

Module linearity is described through the Leibniz commutator. A radial
annulus coordinate exhibits its failure; a nonconstant locally constant
function on a disconnected space does not. Dimension vanishing uses a
bound on the chosen source image germ. A closed analytic subspace of
dimension below max(p,q) is disjoint from the ambient support of a smooth
form, since the completed residue field is unchanged and its graded
dimension is bounded by the subspace dimension. This repairs the earlier
contrary support statement and matches CLD25 Proposition 15.2.1(b).
The base-extension pullback proof still uses surjectivity of the tropical
image, without invoking equality of full skeleton inverse images.
Pullback failures use point inclusion and an annulus structural map;
unsupported blanket spectral-sequence assertions are removed.

Test-form coefficient seminorms use each cell's own tangent coordinates,
so they are defined on the quotient of ambient forms. Each stage carries
its C-infinity topology before the locally convex colimit is taken. The
text does not identify this final topology with the supremum of final
finite-order topologies. The locators are corrected to CLD25 Sections
3.6--3.7 and 6.4, with the skeletal description in 5.2. The continuous
inclusion into G-forms is retained without the contradictory coarser-
topology comparison. Derivative estimates have the coordinate constant
required for coefficient sums. Proper pullback may shrink the actual
tropical image, so its continuity uses affine seminorm bounds rather
than literal equality of every seminorm.

Positivity is G-local on polyhedral supports and is tested on their cell
tangent spaces. It does not require an ambient positive extension in every
chosen target. Reflection through compact surjective projections uses
piecewise affine sections, as in CLD25 Lemma 3.5.3. The curve coefficient
and toric Hessian computations retain their stated scopes.

Dimension-zero integration is separated from boundary formulas, which use
n at least one. Scalar-extension compatibility of top-dimensional Borel
and Radon measures is Proposition 15.3.1; Proposition 15.3.2 is the
corresponding boundary-form result. The analytic tropical-space theorem
retains its exact published scope. The harmony discussion uses the
published theorem and its degree mechanism, without claiming a second
arbitrary-dimensional proof from the curve comparison.

Boundary integrals are first defined by the intrinsic boundary Radon
measure of the calibrated tropical structure. Stokes is the exact
published import and needs no global smooth partition. The finite
defect formula is a computational description when its chart and
partition data exist. Localized supports lie in relative Int(V_i/X),
which removes the artificial relative boundaries and still allows
points of the analytic boundary of X. The proof sums local integrals
using restriction and zero extension, then identifies them with the
intrinsic Stokes integral. Absolute-interior support would discard the
boundary being computed and is not imposed. Stokes and Green retain
general topologically separated pure-dimensional scope. Green's
closed complementary form is also symmetric; mixed cancellation is
on n-dimensional cell spans, not on every ambient form.

Annulus degrees are computed relative to the target analytic annulus,
with the constant interior calibration extending to endpoints. Changing
the valuation and defining coefficient t-squared anew chooses a new
form: the two numerical Stokes values use their respective conventions.
They are not an invariance claim for arbitrary valuation rescaling.
The coordinate chart and its form do extend to ambient Gm in this
example; restriction to the closed annulus still retains its boundary.
The degree-m cover keeps two differential factors and one measure
cancellation, leaving the index exactly once.

The lower-bidegree counterexample now satisfies the chart premise:
the constant moment map on a compact curve domain represents function
1 but has empty level-one skeleton. A fixed radial skeleton may also
miss forms in other branches. Tate skeleton-generated smooth forms are
distinguished from all smooth forms. Discrete-valuation model comparisons
state the ground field and uniformizer normalization; node lengths are
m v(pi). The punctured open-disc skeleton is proper onto its image but
not into ambient R, with a missing finite endpoint at radius 1.
Fineness supplies no Poincare lemma by itself, and local exactness is
kept separate from global cohomological comparisons.

Fresh local primary checks used CLD25 PDF SHA-256
`5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
Ten rendered physical pages were inspected: 82 (3.4.1--3.4.4),
85 (3.5.1--3.5.3), 87 (3.6.1--3.6.4), 93 (3.7.5--3.7.7),
146 (6.4.1--6.4.4), 300 (11.1.7--11.1.8), 422 (15.1.2--15.1.3),
431--432 (15.6.3), and 433 (15.7.2--15.7.3); page 432 also contains
15.7.1. Additional text checks covered 3.3.1--3.3.8, 3.5.3--3.5.5,
11.1.15, 15.2.1--15.2.10 and 15.3.1--15.4.3. The already checked
Stokes and boundary-measure evidence from Chapter 11 is reused.
There is no new network literature search or fresh Jell source audit.

These are classical definition, proof, example and exact published-import
repairs. No original research result, independent verifier verdict or
solved open-problem status is claimed. Semantic, dependency, delimiter
and structural checks replace the unavailable legacy writer.

The final full-book build has 4,174 pages and 19,493,460 bytes, with zero
TeX errors, LaTeX/package warnings, overfull boxes, unresolved references
or citations, and rerun requests. There are 866 nonfatal underfull boxes.
All Chapter 13 physical pages 569--608 and seams 568/609 were viewed in
eleven contact sheets. One overwide dictionary row was shortened; final
sheet 10 was viewed again, and the other ten sheets are byte-identical
to the already viewed baseline. Formulas, warnings, tables and seams
have no clipping, collision or detached heading. The long warning on
page 595 has body text with its heading and continues normally on 596.
Post-render references pass for 425 active files and 12,564 unique labels.
The inventory remains 42 atoms in twelve families with tiers (0,3,7,15,17).
Exact hashes and gates are recorded in
[the manifest](second_reading_ch13_manifest_20261002.json).

The review PDF is
`/workspace/book-completion-drafts/second-reading/Ch13_Review_2026-10-02.pdf`.
Chapter 13 passes this reading gate. Chapter 14 has been freshly read
through lines 1--1320 of its 4,073-line source. Its two active proof inputs
have not yet been freshly read; there are no edits. Its remaining reading,
scope and rendered-page gates remain open. The full-book goal continues
in the cloud.
