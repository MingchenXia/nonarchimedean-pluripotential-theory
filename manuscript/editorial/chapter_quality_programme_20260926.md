# Chapter quality programme

Date: 26 September 2026

## Priority

The active editorial priority is the quality of every chapter of the book.
Independent research on the open problems in Chapter 72 is paused. An open
problem may still be edited when a chapter needs an exact boundary statement,
but it is not the driver of the present pass.

## Chapter gate

Each chapter is processed in reading order and must pass the following gates:

1. **Mathematical architecture.** Check the chapter's purpose, dependency
   order, hypotheses, conventions, and compatibility with later uses.
2. **Proof and example integrity.** Check every numbered assertion for a proof
   or an exact source, and verify the computations that carry explanatory
   weight.
3. **Exposition.** Repair misleading structure, undefined notation, vague
   transitions, and statements whose scope is wider than their proof.
4. **Navigation and provenance.** Give reusable objects semantic labels and
   check cross-references, citations, and historical attributions.
5. **Mechanical verification.** Run the scoped writing audit, the project-wide
   reference checker, and a full book build.
6. **Rendered verification.** Inspect the changed pages of the compiled book,
   then repeat the scoped audit and reference check as an automatic second
   pass.

The pass preserves established project-wide conventions unless a convention
itself causes a mathematical or navigational defect. Descriptive example
titles and the existing `chap:` label namespace are therefore reviewed rather
than mechanically rewritten.

## Order and progress

- **Part I, Chapters 1--8:** complete. All eight chapters have passed the
  semantic, mathematical, structural, mechanical, and rendered-page gates.
- **Part II, Chapters 9--19:** complete. All eleven chapters have passed the
  semantic, mathematical, structural, mechanical, and rendered-page gates.
- **Part III, Chapters 20--31:** active. Chapters 20--21 are complete; Chapter
  22 is next.
- **Parts IV--VI, Chapters 32--72:** queued in reading order after Part III.
- **Appendices and front matter:** final consistency pass after the chapters,
  with earlier intervention when a chapter depends on them.

### Chapter 1

The chapter now presents four entrances---complex, model, differential, and
homogeneous---with valuations explicitly identified as their common
substrate. This removes the former five-item reading of a chapter titled
“Four entrances.” The pass also repaired delimiter usage, labeled the
normalization warning, and replaced an imprecise continuity claim by the
exact internal theorem governing uniform convergence of measures.

### Chapter 2

The pass added semantic labels to sixteen definitions, examples, and remarks,
standardized inline mathematics, and removed two unused approximation claims
that were neither proved nor sourced. The scoped writing audit for Chapters 1
and 2 now has zero errors; its remaining warnings concern reviewed descriptive
example titles and the established chapter-label namespace.

Build and rendered-page evidence for this milestone is recorded in
`chapter_status.md` after the full verification gate.

### Chapter 3

The pass corrected the intersection-theoretic level at which vertical
projection is proved. A vertical Cartier divisor now acts first as a class
with support on the special fibre; only its pushforward to the total space is
the ordinary first-Chern-class action. The projection formula is consequently
applied first to the supported divisor class and then to the remaining Chern
classes. This also explains without contradiction why the principal special
fibre has zero pushforward in the total-space Chow group but a generally
nonzero relative degree.

The common-domination statement now includes the general finite-presentation
conclusion proved later in the section, and its properness argument is reduced
to base change plus a closed immersion. Fourteen previously unlabelled reusable
definitions and remarks now have semantic labels, and the degree-conservation
proposition has a proposition-prefixed label throughout the live manuscript.
The scoped writing audit has zero errors; the remaining twelve warnings are
reviewed descriptive example titles and the established chapter-label
namespace. Full build and rendered-page evidence is recorded in
`chapter_status.md`.

### Chapter 4

The pass now separates the chapter's elementary constructions from its
imported analytic-space inputs with exact interfaces. Support-surjectivity
reuses the valuation-extension results proved in Chapter 2, properness is
cited separately in the nontrivially and trivially valued cases, and the
base-change, fibre, and GAGA statements carry precise Berkovich--Temkin
locators. The Newton--Puiseux and completed-algebraic-closure inputs in the
explicit type-IV example, together with the real-tree topology of the
Berkovich projective line, now have exact sources.

The proof architecture was also tightened internally: continuity of the
support map is proved by an explicit inverse-image formula, the
countable-cofinal reduction in spherical completeness is written out, and
the polydisc-extension argument uses the uniform seminorm inequality needed
to pass to the completion. Nine reusable definitions, examples, and remarks
now have semantic labels, and inline mathematics follows the book
convention. The scoped writing audit has zero errors; its remaining
twenty-three warnings are reviewed project conventions and descriptive
titles. Full build and rendered-page evidence is recorded in
`chapter_status.md`.

### Chapter 5

The pass repaired the algebra behind the monomial-minorant inequality: the
descent from the localized monomial ideal now uses the finite
\(\mathfrak q\)-adic filtration and the freeness of its surviving monomial
pieces, rather than the false assertion that the quotient itself is free.
The retraction discussion now distinguishes forgetting residue directions
from collapsing an entire residue class to one point, and the connectedness
of the dual complex is deduced through Stein factorization and the special
fibre rather than through an invalid clopen-cell argument.

Cross-model polyhedral claims are now stated at their correct strength.
Arbitrary higher models induce compatible piecewise-affine structures only
after common rational refinement; literal subdivision of every old cell is
reserved for projective toroidal modifications. The corresponding summary
in Chapter 21 was synchronized. The canonical-weight section now uses the
model-independent Mustaţă--Nicaise weight function, allows horizontal zeroes
to create bends, and separates model skeleta from the essential skeleton.
Exact source interfaces were added for Berkovich deformation retractions,
BFJ compatibility, canonical weight functions, and dlt minimal skeleta. The
Hesse cubic example now proves, via adjunction and the Poincaré residue, that
every pluricanonical minimum locus is the whole circle.

Reusable definitions and remarks received semantic labels, inline
mathematics follows the book convention, and the unsupported projection of
arbitrary bent PL functions onto model functions was removed. The scoped
writing audit has zero errors; its remaining thirty-two warnings are
reviewed project conventions and descriptive titles. Full build and
rendered-page evidence is recorded in `chapter_status.md`.

### Chapter 6

The pass now separates the integral and rational levels of the metric
dictionary. Integral algebraic, formal, and PL metrics agree on proper
schemes; algebraic model, Q-formal, and Q-PL metrics agree only after
Q-linearization; arbitrary real-weight Fubini--Study metrics are uniform
limits rather than automatically model metrics. The formal discussion is
correspondingly restricted to the possibly nondiscrete rank-one setting.

The descent of relative nefness no longer relies on repeated hyperplane cuts:
it uses the closure of a closed point of the generic fibre to produce a
finite multisection over the test curve. The maximum and pointwise-closedness
results now carry exact Gubler--Martin locators, while the model-measure proof
checks independence from both the model and the chosen extension. The
continuous Chambert--Loir theorem now states all of its data and explains why
the internal density-and-Riesz argument does not require Chambert--Loir's
auxiliary metrizability hypothesis. Change-of-reference and constant-shift
formulas have also been separated and normalized.

Reusable definitions, examples, and remarks received semantic labels, inline
mathematics follows the book convention, and the scoped writing audit has
zero errors. Its twenty-one remaining warnings are reviewed project
conventions and descriptive titles. Full build and rendered-page evidence is
recorded in `chapter_status.md`.

### Chapter 7

The pass reconciled the main text and Appendix E on directed preorders,
tail-cofinal order-preserving subnets, and compact-set exhaustion. The weak
limit argument for moving Dirac masses now proves that a multiplicative limit
measure is itself Dirac, while the Riesz and pushforward interfaces distinguish
nonnegative Borel functions from genuinely integrable signed ones. Weak,
vague, and narrow convergence are now separated according to their compact,
compact-support, and bounded-continuous test-function regimes.

Convergence in capacity is formulated for metric-valued maps, with an explicit
order-topology metric for extended-real potentials. The quasicontinuity
calculus consequently has well-defined sum, product, and uniform-limit
clauses. The Duistermaat--Heckman section distinguishes closed and strict
tails, records atoms as their jumps, and gives the correct one-dimensional
density monotonicity. The extended-real ledger now supplies a complete case
split for the limsup-of-sums inequality and explains why no convention for
zero times infinity is compatible with both pointwise and regularized limits.

Twelve missing semantic labels were supplied. The scoped writing audit has
zero errors; its thirty remaining warnings are reviewed project conventions
and descriptive titles. The project-wide reference check, full build,
automatic second pass, and rendered-page inspection all pass. Exact evidence
is recorded in `chapter_status.md`.

### Chapter 8

The pass repaired the normalized-link discreteness proof over a trivially
valued curve by separating analytic support from the centre of a valuation.
It now constructs a single affine-open test function that isolates every
normalized order valuation, including valuations centred at the deleted pole
set. The ideal-potential proposition now gives the global divisor formula on
a smooth projective curve and proves continuity at both the common vertex and
the proper-support endpoints.

The projective-line branching proof now includes type-IV points explicitly,
and the residue-field discussion correctly lists the point at infinity over a
finite field. The graph Poisson statement is restricted to graph potentials;
the additional integral or rational slope and support conditions required by
model metrics are recorded separately. In the toric continuous comparison,
vague and narrow convergence are distinguished and compactly supported tests
are extended across the toric boundary before the full-mass argument excludes
boundary loss. The potentially-good elliptic example now uses the
integer-normalized extension valuation to prove that ramification index six
is minimal.

Nineteen reusable definitions, examples, and remarks received semantic
labels. The scoped writing audit has zero errors; its forty-five warnings are
reviewed project conventions and descriptive titles. The project-wide
reference check, full build, automatic second pass, and rendered-page
inspection all pass. Exact evidence is recorded in `chapter_status.md`.

### Chapter 9

The pass separated the infinite-dimensional space of smooth superforms from
its finite-dimensional constant-coefficient fibre. The doubled exterior
algebra, coefficient matrices, complementary pairing, and positivity cones
now use the fibre notation consistently, and the algebra structure is
introduced by transporting the exterior product rather than presupposed in
the vector-space identification.

Positivity is now defined pointwise from the outset. This removes the former
contradiction between a local smooth-decomposition definition and the later
statement that no such decomposition is asserted. The decomposable cone is
closed by its Plücker equations, the duality discussion states exactly which
cones are canonically self-dual or exchange under duality, and an unused
higher-dimensional strictness claim has been removed rather than left
unproved.

The distributional convexity proof now supplies the local approximate-
identity argument and a diagonal almost-everywhere subsequence. Most
importantly, the invalid midpoint argument for excluding a value of minus
infinity has been replaced by a null-set contradiction under a
positive-measure homothety. The Lagerberg source is cited directly, the CLD
involution translation is stated at the attribution point, and the two
previously unlabelled reusable items now have semantic labels. The scoped
writing audit has zero errors; its fifteen remaining warnings are reviewed
project conventions and descriptive titles. The project-wide reference
check, full build, automatic second pass, and rendered-page inspection all
pass. Exact evidence is recorded in `chapter_status.md`.

### Chapter 10

The pass made forms on a polyhedral support intrinsic: they are now germs in
ambient neighbourhoods, organized by a direct limit, rather than quotients
depending on one undeclared neighbourhood. The sheaf proof constructs a
locally finite ambient refinement and uses a partition of unity there; the
cellwise boundary condition and pullback scope are stated explicitly.

The tropical-space definition now fixes a pure dimension, signed transition
weights produce signed densities rather than positive measures, and
calibrations are separated cleanly into oriented top-lattice multiplicities
and signed cycle weights. The formerly false global count of two
orientation--weight pairs is corrected to two choices per facet, independent
from facet to facet. The circle non-embedding argument is now proved directly
from balancing, without a forward dependency on Chapter 11.

Subdivision invariance and pushforward functoriality have single consolidated
proofs, stable-intersection and Gysin edge cases have their correct scope, and
the Bergman-fan discussion no longer turns nonrealizability as a linear space
into a stronger unsupported claim. Six reusable definitions, examples, and
remarks received semantic labels. The scoped writing audit has zero errors;
its forty-seven remaining warnings are reviewed project conventions and
descriptive titles. The project-wide reference check, full build, automatic
second pass, and rendered-page inspection all pass. Exact evidence is recorded
in `chapter_status.md`.

### Chapter 11

The pass rebuilt the integration layer around an intrinsic unsigned
top-degree integral. It now explains why a change of lattice basis contributes
the square of its determinant, and the subdivision proof correctly reduces a
locally finite refinement to the finitely many cells meeting the compact
support. Boundary traces, the two Stokes signs, the Green identities, and the
Dirichlet sign are stated with one consistent normalization; redundant proofs
and unnecessary orientation hypotheses were removed.

The affine regularization argument now uses integer-affine equations, rather
than falsely treating an arbitrary affine subspace as linear. Pushforward
functoriality has the properness hypothesis actually needed for the second
map. The zero-dimensional stable-intersection proof no longer assumes that
the set-theoretic intersection is finite: it clusters displaced transverse
points around the finite stable cycle and derives weak convergence from the
local displacement weights. The accompanying examples now distinguish cycles
from their associated currents, and the scope of the imported global CLD
Stokes theorem is explicit.

Two reusable items received semantic labels. The scoped writing audit has zero
errors; its forty-three remaining warnings are reviewed project conventions
and descriptive titles. The project-wide reference check, full build,
automatic second pass, and rendered-page inspection all pass. Exact evidence
is recorded in `chapter_status.md`.

### Chapter 12

The pass now distinguishes an analytic space from the polyhedral subspaces
and local skeleta on which tropical calibrations actually live. The chapter's
opening, gluing theorem, and final dictionary consequently state that the CLD
calculus is transported chartwise, rather than identifying the analytic space
itself with a calibrated tropical space. The compact tropical-image theorem is
imported at its exact strength, and multiplicities are introduced only after
the analytic degree and calibration machinery has been built.

The local dimension criterion now uses the full graded transcendence degree
of the moment functions. This replaces the false claim that value-group
rational rank alone detects a top-dimensional tropical germ; the revised
discussion explains how residue transcendence at type-II points and value
rank at type-III points give complementary contributions. The proper-image
argument over a maximal-dimensional cell now obtains one target neighbourhood
from compactness of the fibre, instead of assuming a uniform source
neighbourhood without proof.

Canonical scalar weights are integral relative to the saturated tangent
lattice. Nonreduced generic length is incorporated in the analytic degree and
does not by itself create fractional canonical weights; rational coefficients
arise only from noncanonical lattice normalizations or rational analytic
cycles. Cycle pushforwards now state the required properness on skeletal
support. The analytic boundary is no longer conflated with the Shilov
boundary, and the smooth partition-of-unity theorem is stated with its exact
good, separated, paracompact hypotheses and source. Seven reusable objects
received semantic labels.

The scoped writing audit has zero errors; its sixty remaining warnings are
reviewed label namespaces and descriptive titles. The project-wide reference
check, checker tests, full build, automatic second pass, and rendered-page
inspection all pass. Exact evidence is recorded in `chapter_status.md`.

### Chapter 13

The pass reorganized the CLD differential-form calculus around explicit local
models and functorial interfaces. Pullback, wedge product, differential,
support, and integration statements now expose the hypotheses actually used,
while reusable constructions have semantic labels and exact source locators.
The chapter's proof order now follows the dependency chain from local moments
to global forms and integration, and its conventions agree with Chapters
9--12 and the current theory of Chapter 14.

### Chapter 14

The pass tightened the topology and functoriality of currents. Test-form
spaces, weak convergence, positivity, support, differential operators,
integration currents, and proper pushforward now have compatible scopes and
normalizations. Compactness and approximation arguments were separated from
purely formal current calculus, and the interfaces used by Poincar\'e--Lelong
and Bedford--Taylor theory now point to precise internal statements.

### Chapter 15

The pass rebuilt the divisor and psh layer around exact regularity and source
boundaries. Poincar\'e--Lelong, extension across polar sets, envelope
operations, and the comparison among smooth, continuous, PL, and classical
psh notions now state the hypotheses needed by later chapters. Examples and
warnings distinguish genuine theorems from tempting but false local-to-global
inferences, and the chapter's reusable objects carry semantic labels.

### Chapter 16

The pass streamlined the Bedford--Taylor construction from local psh
potentials through mixed dpsh products. Symmetry, locality, continuity,
skeletal support, and vanishing above the relevant dimension are now arranged
in dependency order, with exact interfaces for the metrized-bundle products
of Chapter 17. Redundant exposition was removed, the local/global boundary was
made explicit, and the worked tropical computations were checked against the
book's normalization ledger.

### Chapter 17

The pass now begins with the universal base-change-compatible definition of a
continuous metric and makes the higher-rank smoothness obstruction an exact
orthogonalization-and-Dirac-mass argument. The four parlinear classes agree
with the CLD definitions; formal, residual, and dimension-of-definition data
are kept distinct; and the rank-two and type-III examples have the correct
orthogonality and value-group scope.

The curvature section now cleanly separates construction, psh criteria,
mixed products, residual intersection masses, and recovery of
Chambert--Loir measures. The curve total-mass proof is componentwise, the
global-dpsh decomposition uses the actual parlinear theorem, and the two
counterexamples answer the two source questions without exposing editorial
verification machinery in the reader-facing text. Exact provenance replaces
priority language, reusable definitions have semantic labels, and the
Chapter 72 references were synchronized with the final proposition names.

### Chapter 18

The pass separates the chapter's two genuine enlargements of the CLD
calculus. Delta-forms retain ordinary tropical charts while adjoining
polyhedral current coefficients; weakly smooth forms retain smooth
coefficients while allowing harmonic tropicalizations. The opening route,
the regularity bridge, and the closing scope firewall now keep these
constructions distinct and state exactly where model metrics, classical psh
functions, and continuous zero-current functions enter.

The core chapter retains the wall-curvature calculation, tropical cycles and
delta-preforms, delta-forms and currents, Poincar\'e--Lelong, Chern
delta-forms, positivity, harmonic tropicalizations, weakly smooth forms, and
the model comparison. Four reusable definitions received semantic labels.
The extensive regularity catalogue, transfer lemmas, counterexamples,
hypothesis tables, source notes, and verification records are preserved
verbatim at the mathematical-content level in the new Appendix M rather than
interrupting the core exposition. Cross-references now provide the interface
between the chapter and that catalogue.

The scoped writing audit has zero errors; its remaining warnings are reviewed
label namespaces and descriptive titles. The project-wide reference check,
checker tests, full build, automatic second pass, and rendered-page inspection
all pass. Exact evidence is recorded in `chapter_status.md`.

### Chapter 19

The pass now presents curves, toric varieties, model measures, and abelian
varieties as one uninterrupted sequence of worked comparison tests. Four long
proofs concerning residual Picard obstructions, ordinary smooth curve
regularization, reduction of cubical delta-metricity, and the product--Gauss
criterion have been moved to the new Appendix N. Their statements remain in
Chapter 19 where they are used, and direct forward references keep the proof
interfaces explicit. This removes 1,291 lines of proof from the chapter's
reading path without removing any mathematical content from the book.

The multiplicity-two special-fibre example no longer asserts the impossible
existence of such a model for $\mathbf P^1$. It is now a conditional
normalization calculation for a proper curve with special fibre $2Y$, with
$2e=d$ and the honest-line-bundle parity constraint stated explicitly. The
Tate-curve interpolation argument now obtains a decreasing approximation only
along nested subdivisions, while retaining convergence for arbitrary
$N\to\infty$. The abelian transfer corollary now states the ampleness needed
for the canonical Haar-measure conclusion, and the mass ledger has been
synchronized with the corrected example.

The scoped writing audit has zero errors; its remaining warnings are reviewed
label namespaces and descriptive titles. The project-wide reference check,
checker tests, full build, automatic second pass, and rendered-page inspection
all pass. Exact evidence is recorded in `chapter_status.md`.

### Chapter 20

The pass now draws the exact boundary between rational and real model
functions. Rational theta-psh model functions are stable under finite maxima,
whereas their real span need not be: an explicit blowup of the projective line
produces a maximum with an irrational breakpoint. A fixed-form rational
approximation lemma replaces the false real maximum assertion and proves that,
in an ample generic class, real maxima are uniformly approximable by rational
theta-psh model functions. The model-envelope theorem consequently uses the
rational subfamily for directedness and proves that it computes the same
supremum as the full real family.

The exact-sequence proof was also reconciled with the primary BFJ source. Its
fixed-regular-model strengthening is retained, while Künnemann's
correspondence now uses the pushforward from the auxiliary curve product back
to the original variety. Thus the constructed class already lies on the
original model and no unsupported descent step remains. The positive-
representative argument now identifies the single place where semipositivity
enters, and the correction-size example distinguishes an explicit size-two
repair from the sharp lower bound one. The opening of Chapter 21 was
synchronized so that its real case passes through fixed-form rational
approximation rather than the false real maximum closure.

The scoped writing audit has zero errors; its remaining warnings are reviewed
label namespaces and descriptive titles. The project-wide reference check,
checker tests, full build, automatic second pass, and rendered-page inspection
all pass. Exact evidence is recorded in `chapter_status.md`.

### Chapter 21

The pass rebuilt the chapter's curve interface with the two weights required
by the model intersection formula: special-fibre multiplicities and node
residue degrees. The psh criterion, model measure, Laplacian, flux argument,
and worked examples now distinguish the general weighted theory from the
unit-weight examples. The curve retraction theorem is restricted to regular
SNC models and its single-attachment geometry is proved by factorization of a
birational map of regular surfaces into point blowups. The proof also uses
real model-PL functions directly, rather than silently replacing them by
rational Cartier data.

The global definition was tightened at the same time. Its two clauses are
shown to be logically independent by an example that works on the full model
system, the no-cofinal-sequence result is no longer overextended to arbitrary
nets, and the toric retraction inequality is separated from facewise
convexity. The hypothesis ledger now records both uses of residue
characteristic zero and the additional uses of ampleness. Language comparing
the global BFJ class with the local CLD sheaf has been made exact.

The weighted interface was propagated to the curve-capacity calculation in
Chapter 25, the Chapter 26 graph example, and the Chapter 28 curve-uniqueness
argument. The scoped Chapter 21 writing audit has zero errors; its remaining
warnings are reviewed label namespaces and descriptive titles. The
project-wide reference check, checker tests, full build, automatic second
pass, and rendered-page inspection all pass. Exact evidence is recorded in
`chapter_status.md`. Chapter 22 is next.
