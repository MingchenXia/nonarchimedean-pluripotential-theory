# Chapter quality programme

Date: 26 September 2026

## Priority

The active editorial priority is the quality of every chapter of the book.
Independent research on the open problems in Chapter 72 is paused. An open
problem may still be edited when a chapter needs an exact boundary statement,
but it is not the driver of the present pass.

Completion goal set on 1 October 2026: finish the whole manuscript under this
programme, continuing through Chapters 46--72 in reading order, then the
appendices and front matter, followed by the final whole-book consistency,
reference, build, and rendered-page review. Commit and push verified units
and keep the progress records current. Individual chapter checkpoints are
milestones toward that goal, rather than the end of the continuation. This
goal does not change the paused independent-research scope: unresolved
frontiers remain explicitly identified rather than asserted as solved.

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
- **Part III, Chapters 20--31:** complete. All twelve chapters have passed the
  semantic, mathematical, structural, mechanical, and rendered-page gates.
- **Part IV, Chapters 32--50:** complete. All nineteen chapters have passed
  the sequential quality gates.
- **Part V, Chapters 51--62:** complete. All twelve chapters have passed
  the sequential quality gates.
- **Part VI, Chapters 63--72:** complete. All ten chapters have passed the
  sequential quality gates.
- **Appendices and front matter:** active. Appendices A--N are complete.
  Front matter is next, followed by final whole-book checks.

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

### Chapter 22

The pass separated the characteristic-free fixed-skeleton estimate from the
global compactness theorem, whose topology additionally needs cofinal SNC
models and skeletal reconstruction. The norm and path-metric discussion now
states the correct refinement invariant: new lower-dimensional cells may
carry different compatible norms, while every fixed finite refinement gives
bi-Lipschitz equivalent path metrics. The simplex lemma explicitly verifies
that its directional hypothesis descends to every facet before invoking
induction.

The slope proof was rebuilt around the actual dimension of the dual complex,
with noncircular constants and a dense-good-point extension that no longer
uses the desired bound before it is constructed. A direct audit of the
original BFJ source confirms that display (6.3) prints one too few powers of
the ample class: since $\dim E_J=n+1-|J|$, pullback positivity requires
$n-|J|$ powers. The corrected exponent is now justified in the proof, the
source note, and Appendix L, including the decisive curve-case check.

The compactness limit is now verified against an arbitrary model by passing
to a common domination. The countable-blind-spot example likewise tests
centres on a common model, and the cusp discussion states the precise
fixed-exponent scope of the Hara--Yoshida comparison. The chapter's imported
geometric inputs, topological toolkit, characteristic ledger, and theorem
labels are now mutually consistent.

The scoped writing audit has zero errors; its fifty-two remaining warnings
are reviewed label namespaces and descriptive titles. The project-wide
reference check, checker tests, full build, automatic second pass, two
continuous source reads, and rendered-page inspection all pass. Exact
evidence is recorded in `chapter_status.md`. Chapter 23 is next.

### Chapter 23

The pass now separates three operators throughout: the raw all-psh obstacle
envelope, the real-model obstacle envelope used in the BFJ setting, and the
rational-model envelope used by Gubler--Jell--K\"unnemann--Martin. Direct
inspection of GJKM19, Definition 2.8, Theorem 8.2, and Section 9 confirms that
its positive-characteristic theorem first proves continuity for the
rational-model envelope and identifies it with the all-psh envelope only
later, under the additional SNC/cofinality framework. The theorem, hypothesis
atlas, dictionary, and source notes now preserve that order.

The BFJ reduction to base ideals was repaired at the level where rationality
and positivity interact. The model obstacle is chosen rationally; the
perturbed class is required only to have ample generic class rather than the
unsupported stronger property of relative ampleness; and an explicit
$\varepsilon^2$ class approximation with $t_\varepsilon=\varepsilon$ makes
the convex curvature correction converge. The formal class-continuity
argument now works on one fixed higher model with a uniform ample
neighborhood. The fixed-model comparison is asserted only when the relevant
largest elements exist.

The topological scope was tightened as well. Retraction convergence for a
bounded obstacle is no longer called uniform, the standing hypotheses no
longer imply second countability or a countably cofinal model system, and the
fixed-skeleton selection records explicitly that its Lipschitz constant and
chosen sequence depend on the model. The upper-semicontinuous-obstacle proof
now uses exactly its stated hypotheses instead of citing a lower-boundedness
lemma that does not apply. The closing envelope comparison table was rebuilt
so that these hypotheses remain visible and the rendered page no longer
overflows.

All 1,582 legacy inline delimiters were normalized to the book convention.
The scoped writing audit has zero errors; its twenty-seven remaining warnings
are reviewed chapter-label and descriptive-title conventions. The
project-wide reference check, checker tests, full build, automatic second
pass, two continuous chapter reads, and rendered inspection of all fifty
chapter pages pass. Exact evidence is recorded in `chapter_status.md`.
Chapter 24 is next.

### Chapter 24

The pass now keeps four distinct Monge--Amp\`ere products visible from the
outset: model, continuous, bounded, and finite-energy. Their construction
mechanisms, domains, and continuity statements are separated in the opening
table and reinforced by reusable warnings at the points where a formal
passage would be invalid. The two central constructions---the mixed model
measure and the mixed energy pairing---now have semantic definition labels,
and the special fibre's different roles as a cycle and as a line-bundle class
are isolated explicitly so that the mass computation cannot be confused with
the vanishing of its first Chern class.

The bounded extension proof has been tightened at both analytic interfaces.
The dense-test lemma now constructs a bounded positive functional before
invoking Riesz representation, and the locality proof first passes to one
common model determining both potentials, their maximum, and the reference
form before using facewise affineness. The supporting-vertex reduction is
stated at exactly the strength proved. The comparison theorem now says in its
statement what its proof establishes: on the model locus the BFJ intersection
measure, the Chambert--Loir measure, and the CLD product agree, and on the
continuous locus the three corresponding continuous products agree, including
mixed products. The four excluded singular extensions are collected in a
single labeled scope warning and linked from the dictionary.

A direct check of BFJ15 confirms that its Theorem 3.1 is precisely the full
weighted continuity statement along simultaneous decreasing nets used here;
the notes now say explicitly that this is the cited theorem itself, not a
formal consequence of weak convergence. All 1,134 legacy inline delimiters
were normalized to the book convention. The scoped writing audit has zero
errors; its remaining warnings are reviewed project conventions and
descriptive titles. The project-wide reference check, checker tests, full
build, automatic second pass, two continuous chapter reads, and rendered-page
inspection all pass. Exact evidence is recorded in `chapter_status.md`.
Chapter 25 is next.

### Chapter 25

The capacity chapter now uses the correct analytic mechanism throughout its
quasicontinuity arguments. A continuous approximant minus an upper
semicontinuous limit is lower semicontinuous, and ordinary monotone
convergence is unavailable for an arbitrary net. The fundamental estimate,
bounded quasicontinuity, diagonal sequential regularization, and decreasing
convergence in capacity therefore invoke the weighted decreasing-net
continuity established in Chapter 24. The warning on increasing
regularizations also separates the fixed-measure monotone theorem from the
weighted theorem with a moving Monge--Amp\`ere measure.

Quasicontinuity is now formulated for extended-real-valued maps with the order
topology, and convergence in capacity uses the Chapter 7 metric on
$\overline{\mathbf R}$. Truncations consequently converge without assigning a
value to the undefined expression $(-\infty)-(-\infty)$. The universal
$O(T^{-1})$ sublevel estimate already proves quasicontinuity for every
$\theta$-psh function, so the former forward dependency on finite-energy
theory has been removed; Chapter 26 supplies a sharper tail estimate instead.
The positive-characteristic scope discussion now lists all of the required
inputs rather than treating regularization alone as sufficient.

The source audit checked BFJ15 Theorem 3.1 and Proposition 4.3 directly for
the weighted decreasing-net argument, and rechecked Thuillier's Proposition
3.4.10 and Theorem 3.6.11 for the curve statements. All 1,849 legacy inline
delimiters were normalized to the book convention. The scoped writing audit
has zero errors and eighty-two reviewed convention warnings. The project-wide
reference check, checker tests, full build, automatic second pass, two
continuous source reads, and inspection of all sixty rendered chapter pages
pass. Exact evidence is recorded in `chapter_status.md`. Chapter 26 is next.

### Chapter 26

The energy chapter now distinguishes finite energy from full Monge--Amp\`ere
mass at its point of entry and follows that distinction through truncations,
nonpluripolar products, compactness, and the worked examples. The extended
energy proof treats endpoint values and product-directed decreasing nets
explicitly, and its continuity statement no longer imports an argument that
depends on the concavity currently being proved. The finite-energy tail
estimate is derived directly from the bounded cocycle formula and identifies
the precise step that forces full mass.

The singular theory has been tightened at each limiting interface. Strict
superlevel sets are used only as Borel sets, mixed products are constructed
with a uniform tail estimate before weak convergence, and arbitrary nets are
kept distinct from sequences. The normalized-superlevel compactness
corollary now tracks the varying constants in a compact product and chooses a
subnet realizing the original energy limsup. A new slope-tower example on the
non-Archimedean projective line proves concretely that full mass is strictly
weaker than finite energy, complementing the polar example where mass is
lost.

The scope and provenance sections now separate the original residue-
characteristic-zero BFJ inputs from later positive-characteristic
replacements, and distinguish Thuillier's finite-energy measure space on a
curve from the book's class of finite-energy potentials. All 1,742 legacy
inline delimiters were normalized to the book convention. The scoped writing
audit has zero errors and eighty-eight reviewed convention warnings. The
project-wide reference check, checker tests, clean full build, automatic
second pass, two continuous chapter reads, and rendered inspection of the
whole chapter pass. Exact evidence is recorded in `chapter_status.md`.
Chapter 27 is next.

### Chapter 27

The differentiability chapter now keeps its four variational objects separate:
energy along a segment in $\mathcal E^1$, energy after projection of a
continuous obstacle, the associated linearized functional, and the
Euler--Lagrange functional.  The dependency ledger follows those distinctions
through the energy sandwich, the superdifferential, orthogonality, projected
differentiability, finite-energy variations, and the existence theorem of
Chapter 28.  In particular, the singleton-supergradient corollary now appears
only after continuous-direction differentiability has been proved; its former
position silently applied the model-direction theorem to an arbitrary
continuous base obstacle.

The two limiting arguments have been made exact.  The continuous-direction
proof uses a sequence of model approximants and therefore does not require a
non-countably-cofinal net, whereas the finite-energy projected variation does.
For the latter, continuity in the real parameter is now proved by the full
subsequence criterion: every subsequence admits a further summable subsequence
with the required limit.  This closes the former gap between convergence along
one chosen subsequence and convergence of the original sequence.

The primary-source audit also repaired the historical route.  In BGGJKM20,
Theorem 5.4.3 is the differentiability input, Theorem 6.3.2 turns a continuous
semipositive envelope into metric orthogonality, and Theorem 6.3.3 records the
residue-characteristic-zero BFJ statement.  Equal-characteristic-$p$
orthogonality uses this later volume route after the GJKM test-ideal continuity
theorem and the required resolution hypotheses; it is not an extension of the
original algebraizable asymptotic route.  The BFJ segment, projected-energy,
and finite-energy-variation locators were checked directly as well.

All 1,807 legacy inline delimiters were normalized to the book convention and
four reusable remarks and examples received semantic labels.  The scoped
writing audit has zero errors and thirty-nine reviewed convention warnings.
The project-wide reference check, checker tests, full build, automatic second
pass, continuous chapter read, primary-source audit, and rendered inspection
of all sixty-four chapter pages pass.  Exact evidence is recorded in
`chapter_status.md`. Chapter 28 is next.

### Chapter 28

The finite-energy-measure chapter now keeps duality, completion, attainment,
and regularity logically separate. Its admissibility discussion no longer
claims that the admissible and solvable classes are incomparable: under
orthogonality admissibility implies solvability, while the chapter's
unbounded curve example proves that the converse fails. The rational-point
counterexample has also been narrowed to the statement its calculation
actually proves---a positive type-1 atom forces infinite dual energy---without
making the unsupported stronger assertion about measures merely charging all
neighbourhoods of that point.

The curve theory has been rebuilt at the exact level of its hypotheses. The
general uniqueness proof now uses the harmonic maximum principle directly and
therefore does not import geometric connectedness, semistable reduction, or a
cofinal retraction argument. The quantitative graph subsection separately
states the geometrically connected semistable hypotheses it really needs. A
new Green--Dirichlet lemma proves finite edge energy for arbitrary Radon data
before the derivative integral is used; it yields the sharp estimates
$D_\Gamma(u_1-u_2)\leq L(\Gamma)\lVert\mu_1-\mu_2\rVert^2/4$ and
$\lVert u_1-u_2\rVert_\infty\leq
L(\Gamma)\lVert\mu_1-\mu_2\rVert/2$. The one-edge example shows that the
second coefficient is sharp and stable under subdivision. The graph formula
for the dual energy now passes through atomic approximation and strong
derivative convergence instead of treating uniform convergence as control of
Dirichlet energy.

The source audit checked the precise finite-energy-measure completion
locators: Theorems 2.23, 2.24, and 2.26 of Boucksom--Jonsson together form the
quoted Theorem A. All 2,842 legacy inline delimiters were normalized to the
book convention. The scoped writing audit has zero errors and fifty-six
reviewed convention warnings. The project-wide reference check, checker
tests, full build, automatic second pass, two continuous chapter reads, and
rendered inspection of all fifty-four chapter pages and the Chapter 29 seam
pass. Exact evidence is recorded in `chapter_status.md`. Chapter 29 is next.

### Chapter 29

The continuity chapter now separates envelope continuity, continuity of an
individual Monge--Amp\`ere solution, and continuity of the solution map
without asserting a bare implication among them. The supported regularity
proof has been shortened to its actual mechanism: decreasing model
regularization, Dini convergence on the fixed supporting skeleton, and the
capacity domination lemma. A redundant global normalization step and its
second Dini application were removed, while the passage from a uniform net to
a uniform sequence now chooses a genuinely increasing chain of indices.

The historical and field-theoretic scope has also been tightened. The
completion in the BFJ algebraizability hypothesis is correctly identified as
the fraction field of the completed local ring, the role of a proper global
base is deferred to compactification, and the residue-characteristic-zero,
equal-characteristic-$p$, arbitrary-field curve, and conditional
mixed-characteristic routes remain separate. The chapter's curve theorem is
no longer followed by a self-contained proof reconstruction whose descent and
semipositivity steps were explicitly unresolved. It now has an exact source
boundary at GJKM19 Theorems 1.1 and 3.1 and Propositions 1.2, 3.5, 3.7, and
3.8. The slope criterion retained for later use is source-exact, and the
backward caller in Chapter 23 now cites GJKM19 Proposition 3.10 directly.

All 1,186 legacy inline delimiters were normalized to the book convention.
The scoped writing audit has zero errors and fifty-six reviewed convention
warnings. The project-wide reference check, checker tests, clean full build,
automatic second pass, continuous chapter read, primary-source audit, and
rendered inspection of all forty-eight physical pages pass. Exact evidence
is recorded in `chapter_status.md`. Chapter 30 is next.

### Chapter 30

The functoriality chapter now separates three constructions that had been
allowed to drift together: a morphism over a fixed ground field, the ordinary
analytic projection attached to an extension of complete valued fields, and
the additional Gauss section available for $k\subset k((t))$ when $k$ is
trivially valued. In particular, the Gauss section is no longer described as
though it were the base-change projection or were induced by a morphism of
schemes. The projection formula ledger also distinguishes the degree factor
for a finite morphism from the degree-one birational formula, while recording
that the latter leaves the ample cone and therefore has a different analytic
scope.

The Gauss construction has been repaired at the proof level. Semivaluations
are allowed to take values in $\mathbf R\cup\{+\infty\}$; a finite-dimensional
coefficient-space bound proves that the defining minimum is attained; and a
local bound on a finite basis proves continuity, replacing the former false
global assertion that every coefficient has norm at most one. The same
coefficient bound controls the infinite Laurent-series truncation. The
descent theorem now covers singular psh potentials by decreasing model
regularization, finite-group averaging, model descent, and decreasing
stability. Ramified and infinite extensions are kept at their proved scope:
skeletal compatibility is not presented as model-and-Cartier descent, and no
quotient after completion is asserted without an inverse-limit theorem.

The chapter now keeps model, continuous, bounded, and finite-energy
functoriality distinct and narrows its exceptional-mass warning to a model
function and its model Monge--Amp\`ere measure. The official BJ22 publication
record and the section-level Gauss attribution were checked, while the
chapter continues to avoid identifying the full psh theories over the
trivially and nontrivially valued fields. All 2,230 legacy inline delimiters
were normalized, one reusable remark received a semantic label, and three
bibliography family labels were made house-compliant.

The scoped writing audit has zero errors and sixty-five reviewed convention
warnings. The project-wide reference check, checker tests, open-problem
inventory check, full build, log scan, and rendered inspection of all
sixty-two physical pages pass. Exact evidence is recorded in
`chapter_status.md`. Chapter 31 is next.

### Chapter 31

The examples chapter now functions as a checked synthesis of Part III rather
than as a second survey. Its curve computations state the split regular
semistable hypotheses actually used, the Green-kernel estimate is proved by
unit current and Kirchhoff's law, and rational graph approximation is kept at
the exact discrete-valuation scope where it produces model functions. The
toric section no longer applies a compact-graph proposition to a noncompact
skeleton, and rational polyhedral data are realized by clearing denominators
rather than by an unsupported field extension.

The divisorial-pole discussion now matches BFJ15 Lemma 8.5 and Proposition
8.6 exactly: the finite-pole theorem is stated for divisorial points, its
normalization and zero locus are correct, and the type-1 analogue is recorded
as an infinite envelope off the pole rather than a finite Green function. The
finite-dimensional programme gives the precise energy derivative used for
its Lagrange multipliers. The abelian example now obtains semipositive model
approximants from convex rational polyhedral Mumford data; the same repair was
propagated to Chapter 19. This replaces an arbitrary interpolation step that
did not preserve convexity.

The BFJ--CLD tables were recomputed row by row. They now distinguish a missing
CLD counterpart from a collapse of hypotheses, record the nonsplit
residue-degree weights, and give the corrected census of four exact
agreements, four one-way implications, and eight rows with no counterpart.
The field hypotheses separate the discretely valued BFJ theory from the more
general CLD abelian statement, and the Part III synthesis now presents a
dependency chain and a transport diagnostic instead of unsupported claims of
formal equivalence. All 1,712 legacy inline delimiters were normalized.

The scoped writing audit has zero errors and seventy-three reviewed convention
warnings. The project-wide reference check, checker tests, open-problem
inventory check, full build, log scan, primary-source check, and rendered
inspection of the entire chapter and both adjoining seams pass. Exact evidence
is recorded in `chapter_status.md`. Part III is complete; Chapter 32 is next.

### Chapter 32

The opening chapter of Part IV now distinguishes the topology of the trivially
valued analytification from the valuation-theoretic structures that are special
to it. The affine-line classification separates type III from type IV points,
and the curve discussion uses the general smooth-projective-curve
classification rather than importing the special description of the projective
line. Finite-surjective analytification is justified through completed residue
fields, while the discussion of proper support states precisely which compact
global arguments fail on the proper-support locus alone.

The divisorial and quasimonomial sections have been repaired at their two main
interfaces. The converse divisorial criterion now invokes the
Zariski--Abhyankar theorem rather than the inequality alone. The normal cone is
described on the normalized blowup by all of its Rees valuations, with their
multiplicities, instead of being assigned a single exceptional component. The
quasimonomial cone is the quotient of closed orthants glued along faces;
continuity at a face follows from Dickson's lemma, and the divisorial rays are
exactly the rational rays represented by primitive positive integral weights.
The affine-plane table and discrepancy computation use the same normalization.

The Gauss comparison now separates rescaling of the ground-field norm from the
scaling action on the trivially valued space and records the exact identity
$\sigma(tv)=t\sigma_{1/t}(v)$. Its extension-of-scalars warning says only that
new divisorial points may appear. Redundant roadmaps and repeated summary
tables were removed, while the final dictionary now points to the precise
results proved in the chapter. The official BJ22 text was checked at the
relevant sections and appendix, and all 2,871 legacy inline delimiters were
normalized to the book convention.

The scoped writing audit has zero errors and ninety-seven reviewed convention
warnings. The project-wide reference check, checker tests, open-problem
inventory check, full build, automatic second pass, log scan, source audit, and
rendered inspection of all fifty-six chapter pages and both adjoining seams
pass. Exact evidence is recorded in `chapter_status.md`. Chapter 33 is next.

### Chapter 33

The test-configuration chapter now states the dictionary at the exact level
where each arrow is valid. Flatness makes the central fibre Cartier and rules
out vertical irreducible components, but embedded points are excluded only by
the vertical $S_2$ condition. Weight decompositions are used on invariant
affine charts. Integral closure in the generic fibre is distinguished from
normalization, and the direction of the morphism from a dominating model to
the blowup is fixed throughout.

The filtration side now separates character twists, raw base change, integral
closure after base change, and Veronese restriction. A Veronese filtration of
$R(X,rL)$ carries the old degree-$rm$ weights in new degree $m$, so its
Duistermaat--Heckman measure is dilated by $r$ unless the weights retain their
actual-degree normalization. Degree-specific base ideals are kept until a
generating Veronese is chosen; after that choice their integral closures
propagate with exponent $\ell$, not $r\ell$. The central-fibre weight proof,
finite-generation criterion, and semigroup argument now state their precise
coherence, continuity, saturation, and integral-closure hypotheses.

The Boucksom--Chen concave transform is treated as intrinsically upper
semicontinuous, with probability, unnormalized, and Okounkov-body measures
kept separate. The product, deformation-to-the-normal-cone, non-finitely
generated, and toric examples now test all signs and normalization rules
numerically. The complex geodesic material is deferred to Chapter 65 behind
the existing erratum firewall, while the final table distinguishes genuine
equivalences from one-way constructions and coarse invariants. Exact source
locators were added for the BJ22, BHJ17, and BC11 inputs, and all 1,840 legacy
inline delimiters were normalized.

The scoped writing audit, project-wide reference check, checker tests,
open-problem inventory check, full build, automatic second pass, continuous
chapter read, source audit, log scan, and rendered inspection of all forty-eight
chapter pages and both adjoining seams pass. Exact evidence is recorded in
`chapter_status.md`. Chapter 34 is next.

### Chapter 34

The chapter now keeps four function classes separate from the outset:
Fubini--Study functions, rational PL functions, real PL functions, and psh
functions.  Their closure operations and approximation topologies are stated
at the level at which they are valid.  Scaling rays acquire at $t=0$ the
trivial semivaluation of the closure of the centre, rather than an arbitrary
proper-support endpoint.  The maximum principle, convexity along rays, and
decreasing-limit closure are recorded together from the published
Boucksom--Jonsson source.

The dual-complex description now indexes a face by a connected component of a
stratum, so repeated components no longer collapse.  Affineness on a face is
proved using real-linearity of valuations on real Cartier divisors, without
clearing irrational coefficients.  In arbitrary characteristic the
test-configuration comparison uses equivariant graph closure rather than an
unavailable equivariant resolution.  Closedness of the real PL-positive cone
is cited from the exact source instead of placing an arbitrary convergent
family on one model.

The main regularization statement has been corrected to its full scope: for
every real ample class, each psh function decreases from
$\mathcal H_{\mathrm{dom}}(\omega)$, with no envelope or unibranch hypothesis.
This changes the logical architecture downstream.  Chapters 45--48 now use
Chapter 34 for fixed-class approximation and reserve the envelope theorem for
obstacle operators, compactness, increasing-envelope calculus, and
variational attainment; Chapter 49 follows the repaired generic-constancy
label.  The energy homogeneity proof in Chapter 46 and the dual-energy test
class in Chapter 47 were rewritten so that this distinction is visible in the
proof itself.

The official published source was checked directly at Corollary 3.22,
Proposition 4.12, and Theorem 4.15.  Bibliographic records were repaired, the
entire chapter was read continuously after revision, and all 1,812 legacy
inline delimiters were normalized.  The scoped writing audit, project-wide
reference check, checker tests, open-problem inventory check, two full builds,
log scan, and rendered-page inspection pass.  Exact evidence is recorded in
`chapter_status.md`. Chapter 35 is next.

### Chapter 35

The homogeneity chapter now begins from three sharply separated descriptions:
scaling on the trivially valued analytification, Legendre slices, and numerical
b-divisors.  Redundant roadmaps and two dense dictionary tables were replaced
by a compact mechanism-level orientation and readable term-by-term ledgers.
The scaling argument handles the trivial-valuation endpoint through closure,
and the polyhedral elimination proof now uses Fenchel--Moreau on the correct
function, commutes the relevant infima at coordinates equal to minus infinity,
and justifies the boundary value at zero.

The divisorial comparison and Legendre-reconstruction arguments were repaired
at their limiting steps.  Uniform density of PL functions replaces an invalid
rational-scaling reduction; the identically minus-infinity case is explicit;
and finite orbit functions are continuous before Fenchel--Moreau is applied.
Finite attainment is proved on the normalized blowup using the coherent
fractional ideal from the published argument.  The strict homogeneous Siu
decomposition is distinguished from the imported endpoint theorem, and the
raw backward Legendre transform is no longer claimed to be psh without the
necessary upper-semicontinuity and endpoint conditions.

The Cartier and nef b-divisor dictionaries now keep relative semiampleness,
fractional ideals, modelwise finite support, and the curve case visible.  In
particular, monotone approximation uses decreasing Cartier approximants whose
base traces converge rather than being termwise equal.  The published BJ22
text was checked directly at the complete chain of results used in Sections
2 and 6, the chapter was read continuously twice, and all 2,624 legacy inline
math spans were normalized.  The scoped writing audit, project-wide reference
check, checker tests, open-problem inventory check, full build, log scan, and
rendered inspection of all fifty-five chapter pages pass.  Exact evidence is
recorded in `chapter_status.md`. Chapter 36 is next.

### Chapter 36

The historical envelope chapter now separates four operations that had been
easy to conflate: decreasing limits, increasing nets, arbitrary families via
finite maxima, and obstacle envelopes before they are known to be psh.  The
PL-obstacle criterion and continuity-of-envelopes criterion have complete
proofs, and the implication from the envelope property in one ample class to
unibranchness follows the normalization argument with its birational pullback
input visible.

The former broad claim that sequences never suffice was replaced by the exact
cofinality theorem for the directed set of nonempty finite subsets.  This
corrects the downstream discussion in Chapter 45 without excluding special
sequential reductions.  The two published smooth cases now distinguish the
nef theorem from the addendum's all-class theorem; the Fubini--Study envelope
$Q_L$, the divisibility order, the multiplier/test-ideal inclusions, and the
weak-envelope energy statement are all kept separate from the all-psh
obstacle envelope $P_L$.

The published BJ22 paper, its addendum, and the GJKM19 positive-characteristic
inputs were checked directly at the precise results used.  The chapter was
read continuously twice, all 251 legacy inline math spans were normalized,
and the scoped writing audit, project-wide reference check, checker tests,
open-problem inventory check, two full builds, log scans, and rendered-page
inspection pass.  Exact evidence is recorded in `chapter_status.md`. Chapter
37 is next.

### Chapter 37

The envelope-theorem statement chapter now separates the exact roles of its
hypotheses.  Unibranchness is the geometric condition and is known to be
necessary in an ample class; nonemptiness and one common upper bound are
family-level admissibility conditions; and the ambient field and projectivity
assumptions delimit the theory proved in Part IV without being advertised as
a sharp list for every extension.  The nonempty-family hypothesis forces the
class to be pseudoeffective but not nef, while the envelope-property statement
for a non-pseudoeffective class is vacuous.

The boundedness discussion now proves that, inside one psh class, a family
bounded at every analytic point is already uniformly bounded, because the
trivial valuation controls the maximum.  The projective-line example is
anchored to the explicit Fubini--Study function computed in Chapter 34 and
tests what actually fails when the common bound is dropped.  Normalizing the
members separately is no longer conflated with bounding a prescribed family.
The real-class paragraph records the oriented rational-big approximation
$\theta_j-\theta\in\operatorname{Amp}(X)$ and the exact
$c_1(L)+m^{-1}c_1(A)$ drift used by the proof.

The source note now distinguishes the unpublished supplied-manuscript proof
of unibranch sufficiency from the published comparison theorem, increasing-net
equivalence, ample-class converse, historical conjecture, and smooth partial
result.  The node--cusp example is explicitly only a diagnosis of the
normalization-reflection mechanism.  Four semantic labels were added, all 147
legacy inline math spans were normalized, the chapter was read continuously
twice, and the scoped audit, project-wide reference check, checker tests,
open-problem inventory check, full builds, log scans, and rendered inspection
of every chapter page and both adjoining seams pass.  Exact evidence is
recorded in `chapter_status.md`. Chapter 38 is next.

### Chapter 38

The Cartier-realization chapter now exposes the exact proof mechanism without
using the envelope theorem: one fixed-pole activation, an ample buffer, ordered
rational stages whose class drift is oriented below the target, a decreasing
limit in one psh class, and homogeneous Siu division.  The activation scaling
is integral so that the auxiliary divisor stays rational; the buffer statement
agrees with relative-to-absolute ampleness; and the non-nef target-class
example is reconciled with the bounded-psh nefness criterion.

The analytic and extended-real interfaces were tightened throughout.
Coefficient functions are evaluated on the full-support locus before
realization, while values at proper-support points come only from the realized
psh function and psh divisorial determination.  The pole-removal identity is
kept as a global sum and never converted into an undefined difference of two
minus-infinite values.  A concrete two-line example demonstrates that no
pointwise convention can repair that subtraction.  The final dictionary now
distinguishes equivalences, canonical extensions, the book's theorem, and
later results not proved in the chapter.

The relevant published BJ22 results were checked directly, the boundary
between the supplied envelope manuscript and published inputs is explicit,
all 2,220 legacy inline math spans were normalized, and the chapter was read
continuously twice.  The scoped audit, project-wide reference check, checker
tests, open-problem inventory check, full builds, log scan, and rendered scan
of all fifty chapter pages pass; key proof and seam pages were inspected at
full resolution.  Exact evidence is recorded in `chapter_status.md`. Chapter
39 is next.

### Chapter 39

The birational-reflection chapter now separates three layers that were
previously too easy to conflate: unconditional homogeneous reflection,
reflection of a psh carrier already living in the same numerical class, and
the envelope-property descent argument.  Its dependency diagram records that
the bijection of psh spaces does not by itself imply the envelope property;
one still needs the increasing-net closure supplied by the envelope property
upstairs.

The fixed-class psh space is now described as an ordered convex set rather
than a cone, the class-monotonicity argument uses an oriented ample
perturbation, and the Fubini--Study monotonicity proof no longer assumes that
one section is nonzero everywhere.  The polar-locus discussion distinguishes
the linear locus from proper-support and non-linear points and does not pass a
finite-stage polar formula automatically to a psh limit.  In the blowup
example, coefficientwise convergence on the determining model now yields the
entire divisorial trace, including divisors on higher models, before
divisorial determination is invoked.

The BJ22 comparison, regularization, and Siu-division inputs were checked
directly, the published and supplied-manuscript boundaries were made
explicit, all 1,938 legacy inline math spans were normalized, and the chapter
was read continuously twice.  The scoped audit, project-wide reference
check, checker tests, open-problem inventory check, full build, log scan, and
rendered scan of all forty-nine chapter pages and both adjoining seams pass.
Exact evidence is recorded in `chapter_status.md`. Chapter 40 is next.

### Chapter 40

The smooth-envelope chapter now presents its characteristic-zero and
positive-characteristic arguments as two genuinely different ideal engines
with the same four outputs, rather than suggesting that reduction modulo
$p$ identifies them.  The rational approximation classes and the finite
stage classes are both oriented above the target in nef order; what differs
is their limiting mechanism.  The former duplicate roadmap was removed, so
the opening six-task map now carries the chapter by itself.

The cusp calculation has been corrected at the only prime detected by the
chosen exponent: at exponent $4/5$ it separates multiplier and test ideals in
characteristic $5$, while for every prime $p>5$ with $p\equiv2\pmod3$ the
$F$-pure threshold is still greater than $4/5$.  The exact threshold formula
is now attributed to Musta\c{t}\u{a}--Takagi--Watanabe, Example 4.3.  The text
also distinguishes the wider theory of ideals on singular schemes from the
boundary-free regular package actually used in the proof, and the final
envelope identity now states correctly that the raw supremum already equals
the upper-semicontinuous limit.

The primary-source audit separates the supplied manuscript's
arbitrary-dimensional positive-characteristic theorem from the published
characteristic-zero or dimension-at-most-two result.  Musta\c{t}\u{a}'s
Proposition 3.1 and Theorem 4.1 were checked for the test-ideal architecture,
and the comparison, cusp, and smooth-envelope sources were checked at the
precise results cited.  All 1,948 legacy inline math spans were normalized,
and the chapter was read continuously twice.  The scoped audit,
project-wide reference check, checker tests, open-problem inventory check,
full build, log scan, and rendered scan of all fifty chapter pages and both
adjoining seams pass.  Exact evidence is recorded in `chapter_status.md`.
Chapter 41 is next.

### Chapter 41

The finite-descent chapter now identifies the analytic fibre weight at its
correct generality: it is the dimension of the local Artinian fibre factor
over the completed residue field, equivalently the sum of geometric Artin
lengths after algebraic closure.  The unconditional identity separates this
Artin length from the completed residue-field degree, while the familiar
ramification-index times residue-degree formula is confined to the defectless
case.  The chapter therefore no longer suppresses inseparability or defect.

The double-cover example has also been repaired.  Its two weight-one lifts
exist on the split étale locus, not at every analytic point away from the
branch divisor; a nonsplit analytic fibre may instead be one point of weight
two.  The global averaging formula is now proved with the determinant norm
and an explicit identification of the norm line, so it does not depend on the
split-fibre picture.  The projection-formula discussion likewise separates
the generic-degree identity from the finite-local-freeness required for the
norm-divisor identity.

The source audit checked the flattening, quotient, residue-field, universal-
homeomorphism, finite-locally-free, and determinant-norm inputs against the
Stacks Project, and the norm-law provenance against Ferrand and Roby.  The
source note now credits Roby's original polynomial-law formalism.  All 2,264
legacy inline math spans were normalized, and the chapter was read
continuously twice.  The scoped audit, project-wide reference check, checker
tests, open-problem inventory check, full build, log scan, and rendered scan
of all fifty-four chapter pages and both adjoining seams pass.  Exact evidence
is recorded in `chapter_status.md`.  Chapter 42 is next.

### Chapter 42

The alteration chapter now presents its main transport statement as the exact
assembly of the already proved birational and finite descent mechanisms.  The
Stein factorization is constructed with its normal integral projective middle
term, the birational factor is used before the finite factor, and the class
ledger shows explicitly that the generic degree enters only at the finite
stage.  The family-level proof now pulls an arbitrary family from the base all
the way to the alteration source before invoking the envelope property there.

The geometric scope has been tightened throughout.  Generic finiteness is
equivalent to a finite function-field extension and zero-dimensional generic
fibre, while finiteness over a nonempty open is asserted under properness.
De Jong's theorem is stated with its finite ground-field extension and
strict-normal-crossings boundary visible; over the present perfect field a
generically étale choice is available, but neither the descent theorem nor its
examples assume separability.  The characteristic-two quadratic-cone
calculation now exhibits a purely inseparable rank-two finite factor, a
vanishing trace, and a determinant norm whose mixed coefficient disappears
without damaging the maximum formula.  A separate varying-class family shows
why one cannot average directly over the positive-dimensional fibres of an
alteration.

The de Jong paper and the relative-normalization and finiteness inputs in the
Stacks Project were checked directly.  All 1,529 legacy inline math spans were
normalized, and the chapter was read continuously twice.  The scoped audit,
project-wide reference check, checker tests, open-problem inventory check,
full build, log scan, and rendered inspection of all forty-seven chapter pages
and both adjoining seams pass.  Exact evidence is recorded in
`chapter_status.md`.  Chapter 43 is next.

### Chapter 43

The universal-homeomorphism chapter now separates three assertions that the
older presentation allowed to blur: the elementwise Stacks Project
criterion, the common exponent needed for one Fubini--Study presentation,
and the stronger morphism-level exponent valid on every affine open.  The
last statement is recorded as useful uniform structure rather than as a
logical necessity for reflection, since stage-dependent common exponents
would already suffice.  The analytic homeomorphism is proved at all support
primes, including proper-support semivaluations, and no singleton
topological fibre is confused with a reduced scheme fibre or with the
normal-target averaging theorem.

The class-promotion argument now handles arbitrary directed nets by an
explicit cofinal reindexing, preserves the function and its common-zero
locus exactly, and distinguishes numerical convergence from actual
line-bundle descent.  In positive characteristic the uniform Frobenius
exponent also yields the rational Picard-group isomorphism; the chapter
records this as an alternative route, while retaining the
characteristic-free ample-buffer proof used by the main argument.  The
reflection theorem, its nef consequence and its failure boundaries now
state precisely where finiteness, radiciality, characteristic, projectivity,
integrality, normality and birationality enter.  The Frobenius example also
distinguishes identification through the analytic homeomorphism from the
separate fixed-coordinate identification under which the map is a scaling.

The source audit checked Stacks Project Tags `01S4`, `04DF`, `0CNF`, and
`035S`, separated the supplied unpublished manuscript from the published
Boucksom--Jonsson inputs, and marked the rational Picard consequence as a
derived observation rather than an imported theorem.  All 1,743 legacy
inline math spans were normalized, and the chapter was read continuously
twice.  The scoped audit, project-wide reference check, checker tests,
open-problem inventory check, full build, log scan, and rendered inspection
of all fifty chapter pages and both adjoining seams pass.  Exact evidence is
recorded in `chapter_status.md`.  Chapter 44 is next.

### Chapter 44

The characteristic-zero subintegral-normalization chapter now separates the
finite universal-homeomorphism criterion, the Roberts--Singh additive-power
system, and the global reflection argument instead of allowing their scopes
to overlap.  In characteristic zero the residue extensions are trivial, while
the cited Stacks Project base-change lemma applies to the elementary
square--cube steps rather than supplying the additive-power theorem.  The
proof also records that birationality is automatic for a finite universal
homeomorphism between integral varieties in this setting, and that source
normality is not used by the reflection theorem.

The algebraic and analytic interfaces have been tightened.  The Gauss
construction is stated for semivaluations and finitely generated ideals, the
uniform cutoffs are derived from coherence rather than from an unsupported
uniform Roberts--Singh length, and the extended-real formulas exclude the
ambiguous product $0(\pm\infty)$.  The example
$k[t^2,t^5]\subset k[t]$ now has its minimal correction length and
coefficients computed correctly, and its quotient filtration is proved using
actual elements of the square of the maximal ideal.  The final psh assembly
uses generic finiteness of the limit instead of asserting that every
approximant vanishes at the trivial valuation.  A branch-asymmetric nodal
example now gives the promised failure beyond universal homeomorphisms.

The source audit checked the Roberts--Singh theorem and its finite-difference
inputs, the Reid--Roberts--Singh background, Stacks Project Tags `0CND` and
`0EUH`, and the published Boucksom--Jonsson inputs, while keeping the supplied
unpublished manuscript visibly separate.  All 2,033 legacy inline math spans
were normalized, and the chapter was read continuously twice.  The scoped
audit, project-wide reference check, checker tests, open-problem inventory
check, full build, log scan, and rendered inspection of all fifty-eight
chapter pages and both adjoining seams pass.  Exact evidence is recorded in
`chapter_status.md`.  Chapter 45 is next.

### Chapter 45 — complete

The first revision checkpoint removes the duplicate six-task list and
roadmap, reconciles the seven input groups with the non-circularity audit,
and explicitly audits upper-semicontinuous regularization under the
normalization homeomorphism. It restores the book's rational-multiple
definition of $X^{\divis}$, corrects the alteration-degree and curve
monotonicity explanations, and states the obstacle-calculus hypotheses at
the proposition. The dependency-attribution table and chapter dictionary
have been recast for legible rendered pages. Legacy inline mathematics has
been normalized to the current house style.

The scoped house audit, reference checker, checker tests, inventory check,
full build, log scan, and inspection of the altered pages and both chapter
seams pass; details are in `chapter_status.md`. This is a verified editorial
checkpoint, **not** the completed Chapter 45 gate. Next: inspect each
numbered assertion and worked example against its proof, then audit the
external-source interfaces and remaining rendered pages before advancing
to Chapter 46.

The second checkpoint audited the monotone-obstacle, lattice, and curve-example
sections at statement-to-proof scale. The cuspidal-cubic example now produces
an explicit global section for each denominator $m\ge2$, distinguishes
generically finite Fubini--Study presentations from finite-valued ones, and
does not infer a characteristic-zero GF-space bijection from psh reflection.
The redundant node/cusp recap has been removed. The reducible-scheme boundary
now cites the exact published componentwise and connected-case statement,
Boucksom--Jonsson Remark 5.15. Scoped source, reference, inventory, full-build,
and changed-page checks pass; details are in `chapter_status.md`. The chapter
remains in progress: the earlier proof blocks, the remaining external-source
interfaces, and the uninspected rendered pages still need the complete gate.

The third checkpoint corrects the domain of the increasing-obstacle theorem:
only the cofinal tail with a known competitor has a psh envelope. It also
distinguishes raw envelopes of arbitrary obstacles from the admissible
operator, makes the proper-support endpoint explicit in the raw-supremum
example, and narrows the perturbation and non-projective scope claims. The
Chapter 40 rational-approximation input now separates a possibly irrational
ample difference from the rational ample class used for integral multiples.
The full build and changed-page inspection pass; the remaining Chapter 45
gate is the uncompleted external-source and whole-chapter rendered audit.

The completion pass of 1 October 2026 resolves those outstanding gates.
Every formal assertion and worked example was reviewed against its proof,
and the published Boucksom--Jonsson paper, its addendum, and the normalization
source were checked directly. The pass separates normal-target descent
hypotheses from the definition of generic degree, corrects the direction of
sequential indexing, supplies the scaling step in the converse, and states
the curve criterion on its full function domain. A two-element slope-budget
example replaces the unnecessary uncountability argument. The cusp-envelope
discussion now identifies its direct maximality proof, and the historical
note distinguishes the addendum's all-class theorem from the supplied
manuscript's extensions of singularity and characteristic scope.

The manual house review and scoped mechanical checks, project-wide reference
check, six checker tests, open-problem inventory check, full build, log scan,
whole-chapter rendered review, and automatic second pass all pass. The legacy
standalone writing-audit executable is unavailable in this environment; no
legacy warning count is asserted. All fifty chapter pages and both adjoining
seams were inspected, with late changes re-rendered from the final PDF.
Chapter 45 has no overfull boxes or LaTeX warnings. The full build records
twenty-four overfull boxes outside this chapter and thirteen duplicate
destinations in Chapter 70; these are recorded rather than described as a
globally clean layout. Exact scope, source locators, and checksums are in
[`ch45_quality_audit_20261001.md`](ch45_quality_audit_20261001.md) and
`chapter_status.md`. Chapter 46 is next.

### Chapter 46 — complete

The pairing and mixed-measure chapter now distinguishes relative nefness from
global nefness, proves the fixed-model measure formula by projection, and
uses the finite divisorial maximum formula in the monotone extension.
Locality uses the exact weighted-convergence input, with Borel comparison
sets and almost-everywhere integrability. Irrational scaling, homogeneous
truncation limits, proper-support masses, and the b-class and Legendre
dictionaries now retain their actual domains. Curve and toric computations
carry the probability normalization explicitly. The redundant task list and
legacy inline delimiters were removed, and the tables and two long displays
were repaired for the rendered page.

All 28 formal assertions and 68 reusable environments pass the proof and
label review. Direct source interfaces, 20,184 exact arithmetic comparisons,
the scoped manual and mechanical reviews, project references, six checker
tests, inventory, full build, all 56 rendered pages, adjoining seams, and
automatic second pass pass. Chapter 46 has no overfull boxes or LaTeX/package
warnings; 23 whole-book overfull boxes outside the chapter and 13 duplicate
destinations in Chapter 70 remain recorded. The unavailable legacy audit
executable's warning counts are not claimed. Exact evidence is in
[`ch46_quality_audit_20261001.md`](ch46_quality_audit_20261001.md) and
`chapter_status.md`. Chapter 47 is next; the whole-book goal continues.

### Chapter 47 — complete

The finite-energy and variational chapter now keeps its probability
normalization and extended-real domains explicit. The Bernstein/Dirichlet
argument supplies the concavity constant, the projective-space example
verifies the sharp I/J factors, and the curve proof uses a fixed slope
inner product. Differentiability, domination, fixed-measure pairing
continuity, general strong completeness, and lower-semicontinuous contact
have exact published interfaces. The logarithmic, toric-product,
infinite-energy, restriction, and normalization examples were repaired;
trivially valued non-Q-PL Green examples have the correct source locators.

All 40 formal assertions have proofs and all 73 reusable environments have
labels. The 17,317 exact-rational checks, reference checker, six regression
tests, unchanged research inventory, full build, all-page scan, and automatic
second pass pass. Chapter 47 has no overfull boxes or LaTeX/package warnings.
The full book retains 23 overfull boxes elsewhere and 13 duplicate PDF
destinations in Chapter 70. Evidence and hashes are in
[`ch47_quality_audit_20261001.md`](ch47_quality_audit_20261001.md).
Chapter 48 is next; the whole-book goal continues. Commits remain local
while explicit remote-push approval is pending.


### Chapter 48 — complete

The strong-topology and capacity chapter now proves completeness with the
correct fixed-measure continuity input and supplies the measure-completeness
argument. The gauge/d1 distinction, fixed-range capacity, quasicontinuity,
outer-capacity convergence, negligible sets, and arbitrary obstacle limits
retain their actual domains and exact source interfaces. Curve examples
separate open and closed tails, graph measures and finite-energy MA, and
inner and outer capacity. Scope and historical claims were narrowed to the
proved or published statements.

All 31 formal assertions have proofs; all 64 reusable environments have
labels. The 33,815 exact-rational comparisons, scoped and reference checks,
six checker tests, inventory, full build, all 58 rendered pages, adjoining
seams, and automatic second pass pass. Chapter 48 has no overfull boxes or
LaTeX/package warnings. The book retains 20 overfull boxes elsewhere and 13
duplicate PDF destinations in Chapter 70. Evidence and hashes are in
[`ch48_quality_audit_20261001.md`](ch48_quality_audit_20261001.md).
Chapter 49 is next; the whole-book goal continues. Verified commits remain
local while explicit remote-push approval is pending.


### Chapter 49 — complete

The linear-growth and toric chapter now supplies the exact section/potential
exhaustion identity, conductor descent in the divisorial threshold proof,
the general Green height and sup-norm isometry, and the all-characteristic
pointwise topology argument. SNC scope, approximation from below and closed-
face equicontinuity have precise source interfaces. Toric invariant
approximation, real MA limits, energy variation and arbitrary-net strong/L1
convergence retain their correct domains and proofs or explicit imports.
The blowup, transcendental-branch and conic examples were repaired. A small
Chapter 34 dependency correction separates smooth SNC cofinality from the
resolution-free flag-ideal restriction proof.

All 40 formal assertions have proofs; all 77 reusable environments have
labels. The 39,110 exact-rational comparisons, scoped and reference checks,
six checker tests, unchanged inventory, full build, all 64 rendered pages,
adjoining seams, dependency pages and automatic second pass pass. Chapter 49
has no overfull boxes or LaTeX/package warnings. The book retains 20 overfull
boxes elsewhere and 13 duplicate destinations in Chapter 70. Evidence and
hashes are in [`ch49_quality_audit_20261001.md`](ch49_quality_audit_20261001.md).
Chapter 50 is next; the whole-book goal continues. Verified commits remain
local while explicit remote-push approval is pending.

### Chapter 50 — complete

The norms and stability chapter now separates raw and regularized FS,
homogenization, finite-type and rational model domains, and compatible
metrics and quasi-metrics. Discrepancy extension, entropy recovery and
strong derivative continuity retain their exact scopes. The sharp J/L1
argument, threshold deduction, exact Fano divisorial threshold, DNC,
toric and harmonic examples have been repaired and checked. An explicit
normal model with central fibre of multiplicity two verifies the DF/Mabuchi
correction. The source ledger distinguishes the foundational and later
literature without asserting numerical equality of ordinary and divisorial
K thresholds.

All 40 formal assertions have proofs or explicit source interfaces, and
all 99 reusable environments have labels. Seven primary PDFs and twenty
rendered source pages were checked. The 321,388 calculation checks, scoped
and project reference checks, six checker tests, unchanged inventory,
full build, all 72 rendered pages, adjoining seams and automatic second
pass pass. Chapter 50 has no overfull boxes or LaTeX/package warnings.
Nineteen overfull boxes elsewhere and thirteen duplicate PDF destinations
in Chapter 70 remain recorded. Evidence and hashes are in
[`ch50_quality_audit_20261001.md`](ch50_quality_audit_20261001.md).
Part IV is complete; Chapter 51 is next and the whole-book goal continues.
Verified commits remain local pending explicit remote-push approval.


### Chapter 51 — complete

The complex prerequisites now give locally finite nonpluripolar products,
precise Lelong and multiplier-ideal conventions, correctly ordered
quasi-equisingular recovery, and a noncircular projection argument. The
big-class zero-mass extension is distinguished from positive-mass
domination. The half-pole and Cantor examples have full calculations and
proofs; background changes, convergence and import boundaries are explicit.

All 31 formal assertions and two separately numbered foundational inputs
have proofs or exact source boundaries. All 84 reusable environments have
labels. Eight primary PDFs and 32 rendered source pages were checked.
The 119,417 calculation checks, scoped and project reference checks, six
checker tests, unchanged inventory, full build, all 70 rendered chapter
pages, 32 distinct chapter detail pages, adjoining seams and automatic
second pass pass. Chapter 51 has no overfull boxes or LaTeX/package warnings.
Nineteen overfull boxes elsewhere and thirteen duplicate PDF destinations
in Chapter 70 remain recorded. Evidence and hashes are in
[`ch51_quality_audit_20261001.md`](ch51_quality_audit_20261001.md).
Chapter 52 is next; the whole-book goal continues. Verified commits remain
local pending explicit remote-push approval.


### Chapter 52 — complete

The rays and test-curves chapter now supplies exact relative Perron and
linear-supremum inputs, an explicit relative-energy definition, and precise
normalization and parameter translations. Ideal-envelope monotonicity,
concavity and increasing-net continuity have proofs or exact interfaces.
The big-line-bundle filtration construction identifies its ideal-goodness
and ideal-volume inputs. The hyperplane example controls arbitrary sections
by monomials, handles endpoints and interface mass, and directly computes
the product and truncated-ray energies.

All eleven formal assertions have proofs or exact imports; all 25 reusable
environments have labels. Three primary PDFs and 42 rendered source pages
were checked. The 199,941 symbolic, rational and numerical checks, scoped
and reference checks, six checker tests, unchanged inventory, full build,
all twenty chapter pages at detail size, both seams and automatic second
pass pass. Chapter 52 has no overfull boxes or LaTeX/package warnings.
Nineteen overfull boxes elsewhere and thirteen duplicate PDF destinations
in Chapter 70 remain recorded. Evidence and hashes are in
[`ch52_quality_audit_20261001.md`](ch52_quality_audit_20261001.md).
Chapter 53 is next; the whole-book goal continues. Verified commits remain
local pending explicit remote-push approval.


### Chapter 53

The inverse system now has an explicit componentwise order and a proof that
one component detects order. Positive-volume recovery identifies the actual
limiting masses, verifies model normalization, and uses positive-mass
divisorial continuity to recover every original component. The homogeneous
volume proof handles zero mass separately. Birational invariance imports
the exact semipositive-component extension and proves the pullback/descent
composites and volume comparison without a false cofinality argument.

All thirteen assertions and three examples were reviewed against the exact
source interfaces. Three primary PDFs and 21 rendered source pages were
checked; 2,172 symbolic/exact-rational checks pass. The full build, all
fourteen chapter pages and both seams, post-render scoped checks, reference
checker and six regression tests pass. Evidence is recorded in
`ch53_quality_audit_20261001.md` and `chapter_status.md`. Chapter 54 is next;
the whole-book completion goal continues.


### Chapter 54

The pass checks component compatibility for addition, maximum, translation,
suprema and positive scaling, and uses one-component uniqueness for Choquet
reduction. The decreasing mass floor and volume-drop example retain their
correct limiting domains. Analytic trace keeps its smooth-ambient
approximation, normal target, positive mass floor, P-valued output and
exact decreasing-net hypotheses. Ideal saturation treats all codimensions.
The metric trace proof now identifies the target base class before forming
its inverse system, and ambient and point traces give two explicit examples.
Exact source interfaces, the full build and rendered-page evidence are in
`ch54_quality_audit_20261001.md` and `chapter_status.md`.


### Chapter 55

The partial-body construction now gives its counting-completion interface,
valuation lattice, source boundary and pole example. Transcendental
approximation keeps its strict margin and scaled comparisons. Convex duality
and extended energy have full proofs; intrinsic tails prove flag independence
and the weak-limit argument retains its mass and tightness hypotheses. The
DH mass conversion is explicit and checked on a product square and an
infinite-energy example. Validated mixed-volume and toric proofs retain their
scope and frozen receipts. Six primary PDFs and 81 source pages were checked.
All 23 assertions, eight examples, 93,604 calculation checks, full build,
32 rendered chapter pages and both seams, post-render scoped and reference
checks pass. Evidence is in `ch55_quality_audit_20261001.md` and
`chapter_status.md`. Chapter 56 is next; the whole-book goal continues.


### Chapter 56

Valuative analytification now gives the extended-real asymptotic proof,
exact divisorial bounds and ideal-equivalence domain. The published relative
curve convention is distinguished from maximal curves. Concavification has
its correct initial maximum and a full two-pole calculation. Affine
compatibility proves the PL formula on proper supports; fixed-potential and
family generation retain exact source versions. Zero-mass metrics use
positive rational components and explicit common-background comparison.
Six primary PDFs and 33 source pages were checked. All fourteen assertions,
four examples, 9,228 calculation checks, full build, fourteen rendered
chapter pages and both seams, post-render scoped and reference checks pass.
Evidence is in `ch56_quality_audit_20261002.md` and `chapter_status.md`.
Chapter 57 is next; the whole-book goal continues.


### Chapter 57

The projective comparison now states operation classes, the fixed-family
supremum domain and the exact envelope theorem. The weighted-section example
computes its full curve, multiplier ideals and mass floor. Increasing volume
continuity gives the uniform-error squeeze. The perturbed-family criterion
starts without a compatibility assumption and proves its divisorial converse
in any real background before taking the common rational-base extension.
Trace notation retains rational prime rays and its separate trivial cutoff.
Existing detailed order, decreasing-net and trace proofs retain their domains.
Four primary PDFs and 32 source pages were checked. All eleven assertions,
five examples, 4,242 calculation checks, full build, sixteen rendered chapter
pages and both seams, post-render scoped and reference checks pass. Evidence
is in `ch57_quality_audit_20261002.md` and `chapter_status.md`. Chapter 58 is
next; the whole-book goal continues.


### Chapter 58

The tropical-spectrum foundations now prove compact reduction by nilpotent
ideals and give the dual-number calculation. PL density supplies the ideal
product identity, rational difference lattice and uniform-closure argument.
Support, local truncation and full-support modification proofs retain their
extended-real domains. Proper algebraic recovery names exact proper GAGA and
all three Stacks interfaces; its ideal-function bridge keeps the later
positivity theorem separate. Two primary PDFs, thirteen source pages and
three fresh Stacks interfaces were checked. All fourteen assertions, five
examples, 1,504 calculation checks, full build, eighteen chapter pages and
both seams, post-render scoped and reference checks pass. Evidence is in
`ch58_quality_audit_20261002.md` and `chapter_status.md`. Chapter 59 is next;
the whole-book goal continues.


### Chapter 59

The model section now exposes the order of flag evaluation, Cartier data,
density, retraction and inverse limit. Rational PL density cites the proved
lattice identities and checks its uniform closure. The Stein blowup is a
labelled example with the invertible-ideal endpoint. Entropy now records the
actual finite measure mass and has a curve calculation, including infinite
entropy and zero mass. Existing full-support, integral-closure, monomial,
Stein, divisor, retraction and discrepancy proofs retain their exact domains.
Eight primary PDFs, 47 source pages and four fresh Stacks interfaces were
checked. All seventeen assertions, twelve examples, 15,136 calculation checks,
full build, thirty chapter pages and both seams, post-render scoped and
reference checks pass. Evidence is in `ch59_quality_audit_20261002.md` and
`chapter_status.md`. Chapter 60 is next; the whole-book goal continues.


### Chapter 60

The probability convention now has an explicit conversion to the book's
unnormalized measures, energies and distances. A new arbitrary-volume
curve example checks both conventions, the nef interval, endpoint atoms
and the entropy mass shift. The rational scaling calculation has its
correct ideal exponent. Thirteen labelled subsections expose the model,
completion, ray, mixed-slope, entropy and stability dependencies; all
63 reusable environments are labelled. Exact author-version citations
replace two imprecise source keys.

The complete proof review retains the precise imported analytic inputs,
net arguments, finite-energy differences, terminal test-curve convention,
reduced entropy and normalized-model boundary. Ten primary PDFs and
64 rendered source pages, plus the Stacks fiber-ampleness statement and
proof, were checked. Exact calculations pass 42,871 checks. All 54
chapter pages and both seams were inspected at detail size, including
the final repairs that keep compact statements and warnings together.
Build, scoped structure and post-render reference checks pass; evidence
is in `ch60_quality_audit_20261002.md` and `chapter_status.md`.
Chapter 61 is next, and the whole-book goal continues.


### Chapter 61

The chapter now exposes the compactness, duality, envelope, strong-topology,
variational and approximation dependencies in eleven labelled subsections.
Rational envelope translations stay in the model class. The weak/strong curve
counterexample derives its model potentials explicitly, and the interval
example computes a continuous non-PL solution, exact dyadic errors, energies
and entropy. General locality retains its full imported scope and explains
the stronger weighted limit needed by the algebraic proof. The verified
whole-complex boundary argument remains byte-identical.

All twenty formal assertions and 32 reusable environments were reviewed.
Four primary PDFs and 46 rendered source pages, 6,374 calculation checks,
the full build, all 26 chapter pages and both seams, post-render scoped and
reference checks pass. Evidence is in `ch61_quality_audit_20261002.md` and
`chapter_status.md`. Chapter 62 is next; the whole-book goal continues.


### Chapter 62

The chapter has passed the full sequential quality gate. Its eight numbered
sections and twelve subsections separate raw big-model invariants,
normalized envelopes, completion, fixed-measure beta, mass and threshold
derivatives, volume and radial slopes. The continuous-measure example now
computes the rational-test ratios and exact entropy; the toric P2 example
computes positive dual energy and zero beta. The prior coefficient correction
is byte-identical. All fourteen formal assertions and 28 labelled reusable
environments were reviewed against the full chapter and seven prior audits.

Six primary PDFs and forty rendered source pages were inspected; six recent
announcement pages have their limited claim/hypothesis scope recorded.
The exact supplement passes 11,194 checks in 41 families. The full build,
all 26 chapter pages and both seams, scoped review, post-render references,
six checker tests, inventory and diff check pass. Exact evidence is in
[ch62_quality_audit_20261002.md](ch62_quality_audit_20261002.md) and
chapter_status.md. Part V is complete; Chapter 63 is next and the whole-book
goal continues. Verified commits remain local pending remote-push approval.


### Chapter 63

The master dictionary now fixes the exact domains, generic reference
metrics, valuation units and typed function maps. Rational PL and positive
FS correspondences are separated. BFJ skeletal recovery includes both
membership clauses; common continuous measures use an explicit rapidly
decreasing sequence. Local and Reeb interfaces retain their additional
boundary data. Raw contact duality keeps the class and potential fixed,
and the ray comparison fixes its initial weight. The curve and O(d)
product-action examples compute the unit, mass and energy conversions.

All seven formal assertions, eighteen reusable environments and 66 labels
passed review. Eight primary PDFs and 39 selected source pages were checked;
the exact supplement passes 17,279 checks in 24 families. The full build
has 4,138 pages and 19,302,055 bytes. All 22 chapter pages and both seams
were visually verified, with zero chapter overflow or warning. Post-render
references pass for 425 inputs and 12,262 labels; six checker tests and the
unchanged 42-atom inventory pass. The precise source and preservation record
is [ch63_quality_audit_20261002.md](ch63_quality_audit_20261002.md).
Chapter 64 is next, and the whole-book goal continues. Work remains local
pending explicit remote-push approval.


### Chapter 64

The comparison now fixes valuation units and rational presentations in the
model product, states the exact connected BFJ signature, and separates BJ
compactified energy from the divisorial coefficient dictionary. A false
homogeneous intersection assertion is replaced by the exact scaling theorem
and a conditional full-limit statement. A new curve example computes full
limiting mass with infinite energy. First variation has its precise model
segment scope. DH tail, moment and algebraic comparison proofs retain their
initial mass and terminal atom. The mixed truncation estimate includes the
Borel maximum rule, independent cutoffs and the raw energy constant.

All twelve formal assertions, 21 reusable environments and 77 labels passed
review. Six primary PDFs and 35 selected pages were checked. The exact
supplement passes 10,835 checks in 25 families. The full build has 4,140 pages
and 19,307,224 bytes. All twenty chapter pages and both seams were inspected;
all final changed pages were reinspected. There is no chapter overflow or
warning. Post-render references pass for 425 inputs and 12,275 labels; six
checker tests and the unchanged 42-atom inventory pass. The precise evidence
is [ch64_quality_audit_20261002.md](ch64_quality_audit_20261002.md).
Chapter 65 is next; the whole-book goal continues. Work remains local pending
explicit remote-push approval.


### Chapter 65

The filtration/ray comparison now tracks the differential operator alongside
weights and time. The logarithmic slope proof uses raw boundary Deligne
pairings when restricted volume vanishes, with a complete big-nef blowup
example. The norm-error example is a reusable labelled calculation, and the
terminal-atom example explicitly tests a moving threshold. The inverse
Legendre formula and all section interfaces have semantic labels. The
algebraic square, birational mass proof, spectral tails, radial energy and
BHJ erratum ledger retain their exact hypotheses and normalization.

All seventeen formal assertions, thirty reusable environments and 108
labels passed review. Nine primary PDFs and 63 selected pages were checked;
Hisamoto's current proof check is explicitly the v3 preprint rather than a
fresh publisher PDF. The supplement passes 81,126 exact and 312 numerical
checks in 33 families. The full build has 4,142 pages and 19,313,995 bytes.
All 34 chapter pages and both adjoining seams were inspected; every final
changed image was reinspected. Chapter overflow and warning counts are zero.
Post-render references pass for 425 inputs and 12,295 labels; six checker
tests and the unchanged 42-atom inventory pass. The precise evidence is
[ch65_quality_audit_20261002.md](ch65_quality_audit_20261002.md). Chapter 66 is
next; the whole-book goal continues. Work remains local pending explicit
remote-push approval.


### Chapter 66

The hybrid base, metric unpowering and valuation units are explicit.
Coordinate-rate convergence is separated from analytic convergence; psh
extension uses the synchronized corrected decreasing approximation. Model
Monge--Ampere convergence fixes its approximants before the fibre limit.
Volume-form convergence includes its residual boundary, simplex-preserving
Jacobian and all-model passage to the full hybrid space. Canonical metric
regularity precedes its measure limit; stable-curve weights count self-nodes.
Energy and weak-ray E/J slopes retain their exact reference and filtration
interfaces. Entropy lower semicontinuity assumes weak convergence of both
measures, and a worked concentration example disproves entropy equality.
The historical counterexample and all eleven Banach proof fragments are
byte-identical.

All 26 formal assertions, 47 reusable environments and 240 closure labels
passed review. Five primary PDFs and 79 selected pages were checked; the
Favre proof check explicitly uses its dated v2 preprint. The supplement
passes 22,509 exact and 768 numerical checks in 25 families. The full build
has 4,146 pages and 19,333,673 bytes. All 64 chapter pages and both seams
were inspected; all three final changed pages were reinspected. Chapter
overflow and warning counts are zero. Post-render references pass for 425
inputs and 12,316 labels; six checker tests and the unchanged 42-atom
inventory pass. Exact evidence and preservation exceptions are recorded in
[ch66_quality_audit_20261002.md](ch66_quality_audit_20261002.md). Chapter 67
is next; the whole-book goal continues. Work remains local pending explicit
remote-push approval.


### Chapter 67

Birational multiplier transformation now covers arbitrary quasi-psh weights
by a Jacobian integrability proof. Pulled-back positive currents descend;
nonpluripolar mass is preserved under modification. Determinant norms include
residue degree and prove continuity through coalescing fibres. The base-change
operator scales the valuation argument as well as the value. Analytic trace
uses the exact rational interface, while product and retraction limits keep
positive mass and the I-to-P uniqueness theorem. Worked blowup, branched-cover,
radicial, coalescing and logarithmic-product examples make the distinctions
explicit. Unibranch trace and general Dirichlet scope remain open.

All eleven formal assertions, thirty reusable environments and 86 labels
passed review. Four primary PDFs and forty selected pages were checked;
the source versions and rationality restriction are recorded explicitly.
The supplement passes 6,021 exact and 1,518 numerical checks in 24 families.
The full build has 4,148 pages and 19,351,391 bytes. All sixteen chapter pages
and both seams were inspected; every final changed image was reviewed or
matched to an inspected image. Chapter overflow and warning counts are zero.
Post-render references pass for 425 inputs and 12,333 labels; six checker
tests and the unchanged 42-atom inventory pass. Exact evidence is recorded in
[ch67_quality_audit_20261002.md](ch67_quality_audit_20261002.md). Chapter 68
is next; the whole-book goal continues. Work remains local pending explicit
remote-push approval.


### Chapter 68

Chapter 68 now uses the half-entropy normalization required by its Mabuchi
variation and BHJ slope source, with explicit Ricci energy and translation
formulas. The base-change correction distinguishes homogeneous M from DF;
the Fano converse follows BBJ's model approximation argument. Smooth and
weak-ray interfaces, normalized versus all-big-model stability, finite
automorphisms and the frozen 2026 claim cutoff retain their exact domains.
Three worked examples compute the Fano cutoff, P1 entropy/Ricci cancellation
and a normal quotient with nonreduced central fibre.

All twelve formal assertions, thirty reusable environments and 75 labels
were reviewed. Nine PDFs and 65 selected source pages were checked. The
example supplement passes 11,733 exact arithmetic and 58 numerical checks.
Two full builds pass; the final PDF has 4,150 pages and 19,363,795 bytes.
All sixteen chapter pages and both seams were inspected, including all
fifteen changed final images. Chapter overflow/warnings, unresolved
references, missing glyphs and rerun requests are zero. Eighteen inherited
overfull boxes and thirteen Chapter 70 duplicate destinations remain.
Post-render scope and references, all six checker tests, the unchanged
42-atom inventory and whitespace gates pass. Exact evidence is recorded in
[ch68_quality_audit_20261002.md](ch68_quality_audit_20261002.md).
Chapter 69 is next; the whole-book goal continues. Work remains local
pending explicit remote-push approval.


### Chapter 69

Chapter 69 now distinguishes all ten outcomes and analytic equality upstairs
from equality after tropical pushforward. The five receipt-linked live
baseline proof blocks remain byte-identical. Fixed-complex weak limits are
shown to remain in the compact image. The trace quotient uses its exact
I-input/P-output interface, and the split proof supplies uniform positivity,
Fubini pullback and the canonical P_I approximation limit. The no-go proof
constructs its potential with a normalized Green kernel. The segment and
nonsmooth PL examples now expose the volume and Dirac-curvature calculations.
Exact regularization source locators and all boundary restrictions remain
explicit.

Seventeen formal assertions, 33 labelled reusable environments and 108
labels pass. Eight PDFs and 61 selected pages pass the text/interface and
visual checks, with documented reuse of recent Xia/BEGZ text checks. The
supplement passes 11,863 exact and 90 numerical checks. Two full builds pass;
all 26 final chapter pages and two seams were visually inspected. The scoped
post-render audit, 425-input/12,354-label reference check, six tests,
open-problem inventory and whitespace gates pass. Exact evidence is in
[ch69_quality_audit_20261002.md](ch69_quality_audit_20261002.md).
Chapter 70 is next; the whole-book goal continues. Work remains local
pending explicit remote-push approval.


### Chapter 70

Chapter 70 now distinguishes the full affine-cone link from its invariant
retract. A complete density proof on the invariant carrier and a full-link
counterexample correct the source's broader density wording. Finite-energy
measures keep invariant support, and the rational projective comparison
uses invariant metrics. The excellent-ring and curve calculus retains its
conductor, tower and radial scopes; the Gauss core remains a subset of the
shell. The finite-mass positivity bound and exact strong-openness interface
are explicit. Two receipt-linked live blocks and six frozen inputs remain
byte-identical. Tagged display repairs remove all thirteen duplicate PDF
destinations.

The nine-file review covers 31 formal assertions/proofs and one separately
typeset foundational import, 54 reusable environments and 192 labels. Seven
PDFs, 85 selected pages and nineteen Stacks tag interfaces were checked.
The supplement passes 20,915 exact and 240 numerical checks. Two full builds
pass; all 68 chapter pages and two seams were inspected, with the sole final
changed page separately reviewed. Chapter warning/overflow counts are zero.
Post-render references pass for 425 inputs and 12,371 labels; all six tests,
the unchanged 42-atom inventory and scoped/whitespace gates pass. Eighteen
inherited overfull boxes remain for the whole-book pass. Exact evidence is
in [ch70_quality_audit_20261002.md](ch70_quality_audit_20261002.md).
Chapter 71 is next; the whole-book goal continues. Work remains local
pending explicit remote-push approval.


### Chapter 71

Chapter 71's opening, comparison ladder and ledger now state the full
compact-Kähler DXZ--MP order isomorphism already proved in the chapter.
Finite-energy comparison uses the source class volume. The relative
radial/DH functional uses initial mass and is explicitly distinguished
from source DXZ energy: at smaller initial mass, source energy is minus
infinity even when relative energy is finite. Proper-support and finite-grid
worked calculations expose the extended-real values and ordered limits.
The finite ideal limit holds on every semivaluation by the monotone-parameter
lemma. General non-nef and zero-volume boundaries remain explicit.

The review covers 23 assertions/proofs, 37 reusable environments and 136
labels. Twenty-eight receipt-linked chunks, 60,397 bytes, remain identical
to the entry baseline. Eleven PDFs, 87 selected pages and four Stacks tags
were checked. Sixteen exact-calculation families pass 35,379 checks. Four
full builds pass; the final 36 chapter pages and two seams were inspected.
Chapter warnings/overflows and duplicate PDF destinations are zero.
Post-render references pass for 425 inputs and 12,388 labels; six checker
tests, the unchanged 42-atom inventory and scoped/whitespace gates pass.
Eighteen inherited overfull boxes remain for the whole-book pass. Evidence
is in [ch71_quality_audit_20261002.md](ch71_quality_audit_20261002.md).
Chapter 72 is next; the whole-book goal continues. Work remains local
pending explicit remote-push approval.


### Chapter 72

Chapter 72 now matches the live twelve-group, 42-atom inventory and dates its
historical checkpoints. Singular PL regularity and the supplied P07.1/P08.1
negative answers retire their former targets. The P05.3 live proof now uses
a genuine real-PL/generated-psh bridge under an explicit logarithmic
value-group hypothesis; general fields retain the abstract operator-domain
assumption. Mixed boundary nullity uses an integral sum of references,
avoiding the invalid average in the literal integral-slope class. Toric
extended continuity, invariant affine-cone support, full compact-Kahler
comparison and residual current compatibility keep their precise domains.

The full forty-file closure contains 51 assertions/proofs, 69 labelled
reusable environments and 207 labels. All 36 frozen inputs and 32 protected
main-source objects remain unchanged. Five PDFs, 73 selected source pages
and twenty source contact sheets were reviewed. Twenty calculation families
pass 1,872 exact checks. The full build passes with 4,156 pages; all 144
chapter pages and two seams were inspected in 37 contact sheets. Chapter
warning/overflow counts and duplicate PDF destinations are zero. Post-render
references pass for 425 inputs and 12,411 labels; six checker tests, the
42-atom inventory and scoped/whitespace gates pass. Eighteen inherited
overfull boxes remain for the whole-book pass. The P05.3 scope correction
does not claim a new independent-verifier receipt. Evidence is in
[ch72_quality_audit_20261002.md](ch72_quality_audit_20261002.md).
All 72 chapters are complete under this programme; Appendix A is next.
Work remains local pending explicit remote-push approval.


### Appendices A--C

The complete quality pass repairs valuation and normalized-Rees hypotheses,
line-bundle norms and projective alteration scope. Multiplier/test-ideal
inputs now distinguish real-exponent Skoda, subadditivity, geometric
discrepancy and characteristic comparison at their exact scopes. The
full-support graded limit has a complete proof and a supported-point
counterexample. The analytic one-pole example displays the floor and
integral-exponent boundary. All sources, examples, labels, references and
rendered pages pass the documented gates. Evidence is recorded in
`appendices_ABC_quality_audit_20261002.md` and `chapter_status.md`.
Appendix D is the active next unit.


### Appendices D--F

The complete pass repairs affine-minorant separation, dual-lattice volume
conventions and homogeneous-current dilation, and adds an explicit
triangle factorial check. Net topology distinguishes pointwise sequential
closure from closed-set sequentiality; the countable-spikes example shows
why Choquet regularizations need not agree pointwise. The intersection
appendix now uses line-bundle Chern operators when divisor equations vanish
on the image, proves its non-Cartier example on infinitely many point
blowups, and limits numerical transitions to smooth models.

All 40 assertions/proofs, 74 reusable environments, 35 headings and 169
labels were reviewed. Two PDFs and 35 source pages were read and visually
reviewed; two precise Stacks lemmas were read. Eight finite calculation
families pass 18,225 exact checks. The 4,160-page build passes; all 34
appendix pages and two seams were visually reviewed in nine sheets.
Post-render references pass for 425 inputs and 12,445 labels; six checker
tests, the unchanged research inventory and scoped/whitespace gates pass.
No scoped overflow remains. The other 119 appendix files are preserved.
Evidence is in [appendices_DEF_quality_audit_20261002.md](appendices_DEF_quality_audit_20261002.md).
G--I are the next active unit. Work remains local pending explicit
remote-push approval; the whole-book completion goal continues.


### Appendices G--I

The complete pass repairs initial-degree cancellation and calibrated
analytic pushforward, including local finiteness, integer local degree and
the determinant for top-degree superforms. The complex reference sheet now
uses exact relative-energy, metric, domination, multiplier-ideal and ray
inputs, with a local uniform valuative margin and separate continuity
hypotheses. The Stacks supplement records 57 additional dependency tags;
a rejected Picard citation and two decimal false matches are excluded.

All 13 assertion/proof pairs, 51 reusable environments, 61 headings and
138 labels were reviewed. Seven PDFs and 41 source pages were read and
viewed in fourteen sheets. All 78 catalogued tag statements were checked
at their actual imported scope; a complete proof review of every external
source is not claimed. Twelve finite calculation families pass 118,721
example checks. The 4,164-page build passes; all 46 appendix pages and
two seams were viewed in twelve sheets. Post-render references pass for
425 inputs and 12,488 labels; six checker tests, the unchanged research
inventory, scope preservation and whitespace checks pass. No scoped
overflow remains. Evidence is in
[appendices_GHI_quality_audit_20261002.md](appendices_GHI_quality_audit_20261002.md).
J--N and front matter are next; the whole-book completion goal continues.
Work remains local pending explicit remote-push approval.


### Appendices J--L

The complete pass repairs calibrated orientation, model mass and energy
normalizations, and the order-preserving ray transforms. It adds the worked
two-length edge calculation. The provenance ledger distinguishes historical
receipts from current statements, reconciles appendix source locators and
records the current 42-atom inventory without extending a verifier verdict.

All 4,614 source lines, 122 labels, 64 headings and seven reusable
environments were reviewed. Six finite example families pass 3,298 checks.
The other 119 appendix files, including 108 frozen input fragments, and
archival receipt hashes are preserved. The 4,166-page full build passes;
all 78 appendix pages and two seams were viewed in twenty sheets.
Post-render references pass for 425 inputs and 12,508 labels; six checker
tests, unchanged inventory, scope and whitespace gates pass. No scoped
overflow remains. Evidence is in
[appendices_JKL_quality_audit_20261002.md](appendices_JKL_quality_audit_20261002.md).
M--N and front matter are next; the whole-book completion goal continues.
Work remains local pending explicit remote-push approval.


### Appendices M--N

The complete pass reconciles the full supplied pluriharmonic theorem with
M's earlier specialized proofs and both hypothesis ledgers. The arbitrary
continuous zero-current residual remains explicit. Source notes distinguish
the CLD core, later extensions and further descent dependencies. N adds a
reader route and a precise boundary for its four archived comparison proofs.

Both complete roots were read: 4,557 lines, 82 labels, twelve labelled
headings, 46 labelled reusable environments and 40 assertion/proof pairs.
N's four unchanged proof files, 1,291 lines and nine proofs, were freshly
read in full. M's 104 unchanged fragments reuse the completed Chapter 18
source/proof gates; no fresh complete reading of those fragments is claimed.
All 108 included fragments, 120 other appendix files and archival hashes
remain unchanged. The 4,166-page build passes; all 208 appendix pages and
two seams were viewed in 53 sheets. Post-render references pass for 425
inputs and 12,514 labels; six checker tests, unchanged inventory, scope,
semantic-label, delimiter and whitespace gates pass. No scoped overflow
remains. Evidence is in
[appendices_MN_quality_audit_20261002.md](appendices_MN_quality_audit_20261002.md).
All Chapters 1--72 and Appendices A--N are complete under the programme.
Front matter and final whole-book checks are next. Work remains local
pending explicit remote-push approval; the completion goal continues.
