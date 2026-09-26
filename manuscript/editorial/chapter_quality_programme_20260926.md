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
- **Part III, Chapters 20--31:** active. Chapters 20--27 are complete; Chapter
  28 is next.
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
