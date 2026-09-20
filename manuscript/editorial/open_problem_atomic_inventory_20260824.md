# Atomic crosswalk for the active problem environments

**Inventory date:** 20 September 2026
**Literature cutoff:** 19 September 2026; targeted P14.7/P14.8 source update on 31 August, P05/P12/P13/P14/P15/P16 source updates on 10 September, P14.8 current-source production verification and P21.3 residual-Picard source audit on 11 September, and repaired exact-current P14.2 V15 plus unconditional P14.3 production verification on 19 September 2026
**Source scope:** the formal `problem` environments in Chapter 72

This file is an editorial crosswalk for solving, verifying, and retiring the
problems that are formally displayed in the book.  It is not an exercise
list, and it is not a claim that the displayed problems form a complete list
of the open problems in non-Archimedean pluripotential theory or in the
surrounding literature.

## Counting method

The current source contains exactly fourteen formal problem environments,
all in Chapter 72.  A compound environment is
split below into independently auditable theorem or construction targets.
Equivalent reformulations are counted only once.  The compatibility axioms
that make a construction meaningful---for example model independence,
monotone continuity, locality, and functoriality for a local
Monge--Amp\`ere product---are acceptance conditions for that construction,
not artificial extra atoms.  Known boundary cases and counterexamples are
reported in the status notes but are not counted as active atoms.

After deletion of the unrestricted Gubler--Jell--Rabinoff cohomological
isomorphism question, which is negatively answered in the book, the
generalized-Lelong separation question, which is proved in
`thm:local-generalized-lelong-separation`, and the real-toric current-level
question, which is proved in `thm:ok-toric-real-products`, and retirement of
the two original cross-fan realization atoms, and retirement of both the
literal and zero-supremum normalized Favre endpoint-continuity atoms,
retirement of the global Boucksom--Jonsson Radon--Riesz atom, and retirement
of the real-PL current--residue atom after
`thm:p01-real-pl-positive-current-candidate`, and retirement of the
semipositive integral-decomposition atom after the verified signed theorem
and positive-cone counterexample, and retirement of the cubical
delta-metricity atom after the verified product--Gauss criterion, and
retirement of the ordinary CLD-smooth curve-regularization atom after
`thm:p063-current-psh-ordinary-regularization`, and retirement of the
projective ample-class full-cone atom P00.1 after the source-explicit
Mesquita--Piccione--Boucksom--Jonsson comparison described below, and
retirement of P17.1 after the exact-live Banach-family Monge--Amp\`ere
continuity theorem, retirement of P07.2 after the universal
\(\omega_1\)-stage theorem, and retirement of P08.2 after the formal-twistor
counterexample, and retirement of P05.3 and P05.4 after the recursive
CLD/delta projection comparison and its algebraic-chart realization, and
retirement of P14.7 after the strict-interior raw-filtration maximality
theorem, retirement of P14.3 after the exact-current unconditional full Kähler
truncation verification, and retirement of P14.2 after its repaired V15
production pass,
the exact count is

```text
14 formal problem environments = 46 active atomic research questions.
Tier counts: (T1,T2,T3,T4,T5) = (0,5,8,16,17).
```

The read-only command `python3 manuscript/editorial/tools/check_open_problem_inventory.py`
mechanically checks these two declarations, the exact active identifiers and
their placement, and the fourteen Chapter 72 problem labels.

The active identifiers listed below form an editorial addressing scheme.
Their prefixes record the corresponding formal environments, not theorem
numbers in the book; retired and historically skipped identifiers are not
reassigned.

## Atomic inventory

### `prob:frontier-classical-regularization` --- 4 atoms

- **P02.1** `[T3; open]` Characterize the higher-dimensional spaces on which
  every classical psh function is locally a decreasing limit of semipositive
  real PL functions.
- **P02.2** `[T3; open]` Do the same with locally Fubini--Study
  approximants.
- **P02.3** `[T3; open]` Do the same with weakly smooth psh approximants.
- **P02.4** `[T4; open]` Do the same with CLD-smooth psh approximants.

The curve and real-PL boundary cases recorded in the chapter are known; the
four unrestricted higher-dimensional targets remain open.

There is now a source-scoped P02.1 companion on every ordinary open set
compactly contained in a split-toric convex chamber.  If its inverse image
is good and strictly analytic, every
finite continuous maximal-compact-torus-invariant current-psh function there
is a locally uniform decreasing limit of invariant semipositive real-PL
functions.  Finite tangent-plane maxima approximate gently shifted radial
convex smoothings from above, and their positive interstage gaps enforce
monotonicity.  Each explicit polyhedral pullback is CLD-psh and therefore
classically psh; the good-strict real-PL comparison gives semipositivity
without a separatedness, boundarylessness, or pure-dimensionality condition.
This begins with the invariant current-psh class and supplies only the
real-PL conclusion by itself; the distinct companion arguments below add the
locally Fubini--Study and weakly smooth conclusions.  It does not alter any
P02 atom or count.

There is now a source-scoped P02.2 companion on the same type of split-toric
relatively compact ordinary open set.  It approximates the finitely many supporting planes of
successive convex smoothings directly, from above, by affine functions with
one common character denominator.  Their finite maxima pull back to locally
Fubini--Study functions on the same fixed open set, and the prescribed positive
gaps retain monotonicity.  This starts with the invariant current-psh class,
not an arbitrary classically psh function, and does not alter any P02 atom or
count.

There is now a source-scoped P02.4 companion on the inverse image of every
ordinary open set compactly contained in a convex tropical chamber in a split
torus.  Every finite
continuous maximal-compact-torus-invariant current-psh function there is a
locally decreasing limit of invariant ordinary CLD-smooth psh functions:
it descends to a finite convex tropical potential, whose radial
mollifications decrease, and smooth tropical pullback preserves CLD
smoothness and positivity.  This starts with the invariant current-psh
class, not an arbitrary classically psh function, and does not alter any
P02 atom or count.

The very same source-scoped invariant-toric sequence is also a P02.3
companion.  The ordinary CLD-smooth approximants are weakly smooth by
Gubler--Jell--Rabinoff Proposition 10.14, while their psh property remains
the already proved positivity of their CLD Hessian currents.  This changes
neither the finite-continuous invariant starting class nor the relatively
compact ordinary-open scope, supplies no local-Fubini--Study conclusion, and does not alter any
P02 atom or count.

The apparent convex-chamber restriction in these four companions is only
global notation.  On an arbitrary ordinary open tropical domain in a split
torus, every finite continuous maximal-compact-torus-invariant current-psh
function has the locally Fubini--Study, weakly smooth psh, and CLD-smooth psh
decreasing approximations around every tropical fibre: choose nested convex
balls compactly contained in the given open set and apply the corresponding
chamber theorem after restriction.  When the smaller inverse image is good
and strictly analytic, the semipositive real-PL conclusion localizes in the
same way.  This is the germwise result
`cor:p02-invariant-toric-germwise-regularization`; it neither treats
noninvariant functions nor changes a P02 atom or the total count.

### `prob:frontier-unibranch-local-envelope` --- 3 atoms

- **P03.1** `[T2; open]` Classify the normal or geometrically unibranch
  higher-dimensional hypotheses, and determine sharp necessity, under which
  usc regularization of every upper-semicontinuous local
  FS/semipositive-PL obstacle envelope is classically psh.  The
  perfected-unibranch reduced strict curve range is settled positively by
  `thm:p031-perfected-unibranch-curve-envelope`.
- **P03.2** `[T3; open]` Determine the additional hypotheses under which the
  regularized envelope is CLD-v2 psh for every such obstacle.
- **P03.3** `[T3; open]` For continuous finite obstacles, determine the
  additional hypotheses under which the regularized envelope is continuous.

The empty-family case is harmless for the book's extended classical-psh
convention: for the obstacle `f = -infinity`, the raw envelope and its usc
regularization are identically `-infinity`, which is subharmonic under
Gubler--Rabinoff Definition 3.4 and §3.4.1.  Nonempty families are required
only by particular family-level sufficient conditions that explicitly say so.

The continuous obstacle on the reduced strict nodal affinoid curve in
`prop:ch15-nodal-local-envelope` disproves all three unconditional universal
assertions.  Its exact statement and proof passed production run
`20260825T094005Z_10ac70696f69`, item
`pi_31f95353b7e94f3cb98b09b6`, final `correct`, with zero critical errors
and zero gaps.  If the raw envelope is already usc, the classical-psh
conclusion remains valid.  The exact perfected-unibranch curve
statement/proof, SHA-256
`e30033eea96e7d59310a1e67402dc73dbdc1a9463b7ab14fc6f28e271ea0397f` /
`59535602b2f29c7c34bb4b4df79be1e2f72c0fa4fa61f1467b3e1c75723a1c71`,
passed production run `20260829T233220Z_e30033eea96e` using
`gpt-5.6-sol` at `xhigh`, final `correct`, zero critical errors and zero
gaps.  It covers every reduced separated strict curve whose normalization
is bijective after completed perfect closure and reduction, including
relative boundary.  The production-verified product obstruction
`prop:p031-nodal-product-envelope-obstruction-candidate` shows that the same
classical-psh and CLD-v2 failures occur on reduced strict pure-dimensional
spaces of every dimension at least two: take the nodal curve times a closed
strict polydisc and test the zero section against the singleton-Shilov branch
disc.  Its exact statement/proof SHA-256 digests are
`cd22f9b56b743506054ad5c9a5f0f64f9a284385509c27cc1c23c85f76b0b5d6` /
`93ea55ab2a14a152ec7ea6008ca84d6984b6ca92fb1a1527af257da11d6974a8`;
production Rethlas returned `correct`, zero critical errors and zero gaps.
It makes no higher-dimensional continuity claim.  P03.1 and P03.2 therefore
remain active only beyond the reducible and pointwise-unibranch nonsplit-node
product obstructions and, for P03.1, beyond the perfected-unibranch curve
range; P03.3 is unchanged.  The nonsplit-node strict-surface obstruction in
`prop:p031-nonsplit-node-open-disc-envelope-obstruction` shows that mere
pointwise bijectivity of normalization is not product-stable, even for an
irreducible curve; the residual natural range is normal or geometrically
unibranch.  At the
earlier verification checkpoint the total was 53 active atoms in 14 formal
problem environments;
the later P07.2 and P08.2 retirements gave a total of 51 at that checkpoint.
The subsequent P05.3 and P05.4 retirements gave 49, the P14.7 retirement
gave 48, the P14.3 retirement gave 47, and the P14.2 retirement gives the
current total of 46.

For a fixed nonempty competitor family, the separate source-scoped
proposition `prop:p031-modulus-controlled-envelope-candidate` settles the
classical-psh and continuity conclusions whenever the functions are
finite-valued, their pointwise supremum is finite, and they have a common
local modulus. It passed independent verification as
`pi_2640874e3c1d992c29bd2646` with final `correct`, zero critical errors, and
zero gaps. This is not an automatic property of the full local-FS/PL
minorant family and makes no CLD-v2 assertion, so it narrows none of the
three P03 atoms beyond that stated family-level regime.

The affine graph-tube theorem
`thm:p031-affine-ground-field-perron` gives a complementary
higher-dimensional advance with no common-modulus hypothesis.  On every
ordinary open subset of analytic affine space, the usc regularization of
the supremum of any nonempty locally upper-bounded family of classically
psh functions passes all smooth strict curve tests defined over the ground
field.  Hence `cor:p031-affine-obstacle-ground-field` applies to the full
local-FS/semipositive-real-PL obstacle family on every such chart.  The
proof uses the finite relative-Gauss boundary of a small graph tube, the
affinoid maximum principle, and local openness of its quasi-smooth
boundaryless projection.  After scalar extension it controls the
regularization of the pulled-back raw supremum.  Full classical psh-ness
still requires that regularization to equal the pullback of the original
regularization.  `prop:p031-scalar-openness-failure` records that general
scalar projections need not be open, so this compatibility does not follow
from topology alone.  No particular psh envelope is shown to violate it,
and no CLD-v2 or continuity conclusion is obtained.  Thus P03.1--P03.3 and
the total inventory count remain unchanged.

The compact-fiber formula `cor:p031-scalar-fiber-maximum` makes the
remaining compatibility condition geometric.  For
`v_{K'} := (s∘π_{K'/K})^*`, closedness and surjectivity of scalar
projection together with compactness of its fibers give
`s^*∘π(y) = max_{z∈π^{-1}(π(y))} v_{K'}(z)`.  Hence the exact
upgrade holds precisely when `v_{K'}` is constant on each scalar fiber.
The graph-tube theorem already proves the extended-field curve tests for
`v_{K'}`; what remains is fiberwise constancy or a direct psh theorem for
its fiberwise maximum.  The open-map characterization
`prop:p031-open-map-characterization` and the type-4 example
`prop:p031-type-four-topological-defect` show that strict defects occur for
general bounded binary raw data.  They do not construct a psh family or a
P03.1 counterexample.  The P03 atoms and total count therefore remain
unchanged.

The completed-algebraic-closure theorem
`thm:p031-completed-algebraic-closure-reduction` removes the first scalar
step from this obstruction.  For `L = completion(K^alg)`, the scalar map on
the affine open set is open, so
`s^*∘π_{L/K} = (s∘π_{L/K})^*`; classical psh-ness of that envelope is
equivalent before and after passage to `L`.  Thus the stronger
arbitrary-family affine Perron route may assume that the ground field is
complete and algebraically closed, and its residual issue begins with
further analytic extensions.  The theorem does not identify the full
local-FS/semipositive-real-PL obstacle families across scalar extension, so
it retires no P03 atom and does not change the total inventory count.

The defect-localization theorem `thm:p031-usc-defect-localization` further
shows that the regularized supremum is classically psh away from the closure
of its strict raw-supremum gap.  The corollary
`cor:p031-completed-algebraic-closure-defect-support` proves that this gap
and its closure pull back exactly to `completion(K^alg)`.  Hence the
residual affine obstruction is supported on that closed set and is
unchanged by the first scalar step.  No size or removability theorem is
proved for the support, and no statement is made for further analytic
extensions, so the P03 atoms and total count remain unchanged.

The full-real LFS subfamily also has an exact descent theorem for
ordinary-locally-split finite analytic covers.  The fiberwise maximum theorem
`thm:p031-lfs-fiber-maximum` sends every LFS cover function to an LFS base
function, and `thm:p031-lfs-envelope-pullback` therefore makes the raw LFS
envelope of every pulled-back obstacle equal to the pullback of the base
envelope, with simultaneous emptiness of the two competitor families.  The
input is an explicit ordinary-local disjoint union of analytic isomorphisms;
no such splitting is deduced for general finite flat, finite etale, or scalar
maps, and the result does not cover every semipositive real-PL competitor.
Thus it retires no P03 atom and leaves the total count unchanged.

Finite symmetry supplies a complementary partial descent theorem.  Under an
explicit finite analytic orbit presentation---a finite flat surjection with a
finite group acting over the base and transitively on every set-theoretic
fiber---`thm:p031-orbit-fiber-maximum` descends fiberwise maxima of
semipositive rational PL functions and sends LFS functions to semipositive
real-PL functions on the base.  Therefore
`thm:p031-orbit-envelope-comparison` gives exact pullback compatibility for
the raw semipositive rational-PL envelope and a four-term LFS/real-PL
sandwich.  Proposition `prop:p031-real-pl-fiber-maximum-failure` shows that
the rational restriction is genuine: a two-sheet fold presentation has a
semipositive real-PL input whose fiberwise maximum has an irrational bend and
is not real PL.  The result neither produces an orbit presentation for
scalar extension nor descends LFS functions as LFS functions, so it retires
no P03 atom and leaves the total count unchanged.

The full real-PL branch also has an exact finite-orbit defect formula.
Theorem `thm:p031-invariant-real-pl-descent` identifies base semipositive
real-PL competitors with invariant cover competitors and shows that group
averaging stays in this subfamily.  Under nonemptiness,
`thm:p031-centered-symmetry-defect` identifies the full P03 pullback defect
with a finite nonnegative function that is constant on every orbit fiber.  Its
centered formula charges each competitor's asymmetry against the remaining
headroom of its group average, and bounds the defect by the supremal orbit
oscillation.  This is an exact cofinality criterion, not a vanishing theorem;
it supplies neither regularity nor a scalar-extension orbit presentation.
Thus it retires no P03 atom and leaves the total count unchanged.

The finite-cover defect vanishes when a global section palette exists.
Theorem `thm:p031-section-palette-envelope-descent` restricts each cover
competitor along a palette section through the chosen cover point and thereby
proves exact pullback compatibility for both the semipositive real-PL
envelope and the full P03 union envelope.  One global section suffices in a
finite analytic orbit presentation, since its group translates cover every
fiber.  Corollary `cor:p031-fold-envelope-without-maximum-closure` shows that
the fold example has exact envelope descent although its fiberwise maximum
is not real PL.  The theorem does not produce a section palette for scalar
extension or for a general finite flat cover, and it proves no envelope
regularity.  It therefore retires no P03 atom and leaves the total count
unchanged.

At an analytically sectioned cover point, the local obstruction vanishes
without any finite, flat, or orbit hypothesis.  Theorem
`thm:p031-sectioned-local-pl-pullback` identifies the two local raw
semipositive real-PL envelopes.  Theorem
`thm:p031-sectioned-globalization-balance` then writes the global PL
pullback gain as the base globalization defect minus the cover globalization
defect.  For a finite orbit presentation, one local section and its group
translates section the whole central fiber; zero base globalization defect
forces both the cover defect and the symmetry-breaking defect to vanish
there.  No local section is constructed for scalar extension or for a
general finite flat cover, and no base local-to-global cofinality theorem is
proved.  Thus no P03 atom is retired and the total count is unchanged.

At every interior point, Theorem `thm:p031-local-pl-lfs-cofinality` proves
that the local semipositive real-PL and LFS envelopes agree, including empty
families.  Theorem `thm:p031-pl-lfs-defect-split` consequently decomposes the
LFS globalization defect as the sum of the PL globalization defect and the
global PL--LFS branch gap.  Zero LFS globalization defect therefore collapses
all four envelopes.  In a locally sectioned finite orbit presentation this
closes the entire fiber, and everywhere-local splitting plus base LFS
local-to-global cofinality closes the cover globally.  Neither local sections
for scalar projection nor the required base globalization theorem is
constructed, so no P03 atom is retired and the total count is unchanged.

For a finite flat surjection between separated good strict analytic spaces,
Theorem `thm:p031-rational-lfs-fiber-maximum` proves that fiberwise maximum
preserves the rational LFS subclass by a characteristic-polynomial spectral
formula.  Proposition `prop:p031-local-rational-lfs-cofinality` proves that
this subclass is locally cofinal from below in the full real-coefficient LFS
class.  Theorem `thm:p031-finite-flat-local-envelope-pullback` therefore
gives exact local LFS pullback whenever an LFS baseline is available near the
complete fiber, and exact local PL pullback on boundaryless spaces.  Theorem
`thm:p031-finite-flat-pl-defect-balance` removes the local-section hypothesis
from the defect-contraction formula; in the finite-orbit range the resulting
four-defect identity holds at every cover point.  No base local-to-global
cofinality theorem or general scalar-extension presentation is supplied, so
no P03 atom is retired and the total count is unchanged.

With a global rational LFS minorant, Theorem
`thm:p031-rational-defect-conservation` gives a three-level conservation
ledger.  The rational LFS globalization defect is exactly invariant under
finite flat pullback.  The full LFS gain is the increase of the global
rational-coefficient gap, and the PL/full-P03 gain is the increase of that
gap plus the PL--LFS branch gap.  Hence full compatibility is equivalent to
preservation of the total two-stage global gap; vanishing of the base
rational defect collapses every defect and gap on the complete fiber.  The
theorem supplies no mechanism forcing that vanishing and no scalar-extension
presentation, so all P03 atoms and the total count remain unchanged.

The conservation ledger is also additive in finite flat towers.  Theorem
`thm:p031-finite-flat-tower-defect-additivity` expresses each composite LFS
or full-P03 gain as a sum of nonnegative stage gains, and Corollary
`cor:p031-finite-flat-tower-no-cancellation` shows that composite exactness is
equivalent to exactness at every stage.  Thus a later cover cannot hide an
intermediate globalization defect.  This is a constraint on tower-based
scalar-extension reductions, not a construction of the required tower or a
vanishing theorem for the base rational defect; all P03 atoms and the count
remain unchanged.

Theorem `thm:p031-rational-collar-minimax` now gives an exact geometric
formula for that base rational defect.  The excess of any local rational LFS
minorant over the global rational envelope is the infimum of its maximum
boundary excess over all global rational minorants and all sufficiently small
relatively compact domains.  Corollary `cor:p031-rational-collar-absorption`
therefore characterizes zero rational defect by arbitrarily accurate
boundary absorption of every local rational competitor.  Definition
`def:p031-rational-boundary-saturation` imposes the stronger, obstacle-level
condition that the obstacle itself can be approximated from below on one
such surrounding boundary in every neighborhood.  Corollary
`cor:p031-rational-boundary-saturation-collapse` then annihilates the
rational, LFS, and PL defects and both global branch gaps at the central
point; Corollary `cor:p031-rational-boundary-saturation-tower-collapse`
propagates the six-envelope equality through every finite flat tower.  This
is a precise characterization and a concrete sufficient condition, but no
theorem makes arbitrary normal or geometrically unibranch
higher-dimensional obstacles boundary-saturated.  All P03 atoms and the
inventory count remain unchanged.

The collar obstruction also has an exact connected-carrier formulation.
Theorem `thm:p031-rational-defect-escape` proves that every positive gap of a
local rational competitor forces, at every lower positive level and on every
smaller relatively compact domain, a compact connected high-defect component
joining the central point to the surrounding boundary.  Corollary
`cor:p031-rational-defect-escape-characterization` proves the converse: one
local competitor and one positive level whose distinguished component
escapes across every admissible smaller domain are equivalent to positivity
of the complete rational globalization defect.
Thus no counterexample can have only isolated or locally trapped
high-defect components.  Trapping all such components in the normal or
geometrically unibranch higher-dimensional range would force the complete
defect ledger to vanish, but no such theorem is proved here.  All P03 atoms
and the inventory count remain unchanged.

The escape theorem also yields a genuine defect maximum principle.  Theorem
`thm:p031-rational-defect-maximum-principle` proves that the positive part of
the difference between a local rational minorant and the global rational
envelope takes its maximum on the boundary of every relatively compact test
domain.  Corollary `cor:p031-rational-defect-coherent-carrier` then shows
that all truncated carriers through the point lie in one intrinsic connected
superlevel component which crosses every smaller boundary and is not
relatively compact in the local domain.  Corollary
`cor:p031-rational-defect-end-characterization` makes existence of such a
coherent end-reaching carrier that is not relatively compact equivalent to
positivity of the complete
rational globalization defect.  Excluding these carriers in the unresolved
normal or geometrically unibranch higher-dimensional range would force the
complete defect ledger to vanish, but no such exclusion is proved here.  All
P03 atoms and the inventory count remain unchanged.

The coherent carrier now has an exact numerical boundary signature.
Theorem \`thm:p031-rational-defect-boundary-trace\` identifies the supremum
of the positive rational defect profile on every relatively compact local
domain with the maximum of its interior upper trace on the actual boundary.
Corollary \`cor:p031-rational-defect-end-height\` recovers the pointwise
excess as the supremal level of a connected carrier whose closure reaches
that boundary, while
\`cor:p031-rational-defect-open-set-trace-characterization\` makes zero
rational defect on an open set equivalent to zero boundary trace for every
relatively compact local rational competitor.  The finite-flat companion
\`cor:p031-finite-flat-boundary-trace-and-carrier-anchor\` preserves each
boundary trace at every lift and bounds the pullback components of a compact
truncated carrier by the cardinality of one central fiber.  Thus finite flat
pullback neither lowers the end height nor creates infinitely many
unanchored compact branches.  No argument forces these boundary traces to
vanish throughout the unresolved normal or geometrically unibranch
higher-dimensional range.  P03.1--P03.3 and the total count therefore remain
unchanged.

The levelwise contacts now have a common terminal core.  Theorem
`thm:p031-rational-defect-terminal-boundary-core` shows that, for every root
point of positive rational defect, the nested compact boundary-contact sets
of all strict superlevels have nonempty intersection.  Its rooted terminal
trace is upper semicontinuous, lies below the full boundary trace, and has
maximum exactly equal to the pointwise defect.  Corollary
`cor:p031-rational-defect-rooted-terminal-formula` rewrites the complete
rational globalization defect using these rooted maxima.  Under finite flat
pullback, Corollary
`cor:p031-finite-flat-persistent-terminal-anchor` further chooses, for every
lift of a terminal endpoint, one central-fiber point that remains in the
same pulled-back compact component at every strict level.  Thus a surviving
obstruction has a persistent endpoint and cannot evade the finite-flat
constraint by switching central sheets as the level rises.  This still does
not exclude such a persistent end in the unresolved normal or geometrically
unibranch higher-dimensional range, so P03.1--P03.3 and the total count
remain unchanged.

The finite-fiber restriction in the terminal-anchor mechanism is now removed
topologically.  Theorem `thm:p031-proper-open-component-surjectivity` proves
that every component over a compact connected set maps onto that set under
any continuous proper open surjection of locally compact Hausdorff spaces.
Theorem `thm:p031-proper-open-persistent-component-anchor` consequently gives
one common point in a fixed compact fiber for every decreasing family of
components through a lifted endpoint, and Corollary
`cor:p031-proper-open-persistent-terminal-anchor` applies this to the entire
rooted terminal-carrier family.  Fiber finiteness is needed only for the
finite component-count bound.  Scalar projection still lacks the required
general openness and analytic defect compatibility, so P03.1--P03.3 and the
total count remain unchanged.

The algebraically closed scalar-extension range now has a complementary
section-selected anchor.  Lemma
`lem:p031-continuous-section-pointwise-openness` proves that every continuous
section makes its projection pointwise open along the section image and makes
usc regularization commute with pullback there.  Theorem
`thm:p031-continuous-section-persistent-component-anchor` shows that the
component through a section-selected endpoint contains the section of every
connected base carrier, maps onto that carrier, and has the explicit common
anchor `sigma(x)` for every decreasing family.  Poineau's universal-point
theorem supplies the required canonical continuous section for every scalar
extension over an algebraically closed complete ground field, and Corollary
`cor:p031-canonical-scalar-persistent-terminal-anchor` applies it to all
strict levels of a rooted terminal carrier.  No properness, global openness,
compactness, or fiber-cardinality condition is needed for this canonical
component.  The result does not control arbitrary endpoint lifts and proves
neither scalar-fiber constancy nor analytic defect compatibility, so
P03.1--P03.3 and the total count remain unchanged.

The canonical section also puts the scalar usc defect into an exact
retraction normal form.  Theorem
`thm:p031-canonical-scalar-retraction-normal-form` defines the continuous
idempotent retraction `r=sigma o pi` and proves that the value of the
upstairs regularization at `r(y)` is both the downstairs regularization at
`pi(y)` and the maximum over the whole scalar fiber.  Hence the strict
defect locus is exactly `{b < b o r}`, is disjoint from the section image,
and is empty exactly when `b` is fiberwise constant.  Corollary
`cor:p031-affine-canonical-retraction-reduction` gives
`u o pi = v o r` for the affine Perron family and reduces classical psh-ness
to subharmonicity of `v o r` on every extended smooth strict curve.  The
retraction is only continuous; no psh-preservation theorem for composition
with it is proved.  Thus the analytic obstruction is sharper, but P03.1--P03.3
and the total count remain unchanged.

There is now an automatic-modulus invariant toric companion result for
P03.1--P03.3.  On the inverse image of an ordinary open convex subset of the
dense tropical vector space of a split torus, every upper-semicontinuous
invariant obstacle with a nonempty finite convex minorant family has a finite,
continuous, locally psh-approximable raw envelope over all continuous
invariant psh minorants.  Under tropicalization it is the envelope of finite
convex minorants, and supporting affine functions prove that it equals the
smaller invariant toric real-PL envelope.  The lower bound from one competitor
forces the obstacle to be finite; together with upper semicontinuity, it gives
the local bounds that make the tropical convex supremum locally Lipschitz.
The exact source and scope ledger is
`solver_dossiers_20260909/p033_invariant_toric_convex_envelope_20260909/`.
It treats only that invariant psh competitor family, not all
local-FS/semipositive-real-PL minorants; the P03 atoms therefore remain active
and the inventory count is unchanged.

There is now a further source-scoped LFS-only refinement on every ordinary
open convex set compactly contained in that split-toric chamber whose inverse image is
good, separated, strictly analytic, and boundaryless.  For every
upper-semicontinuous invariant obstacle with a nonempty finite
convex-minorant family, the local envelope of finite convex
minorants is also exactly the raw envelope over the invariant locally
Fubini--Study minorants alone.  Finite supporting planes on a compact
exhaustion are rounded from below to one character-lattice
denominator at a time.  Taking common-denominator finite maxima yields a
pointwise increasing locally Fubini--Study sequence below the obstacle that
converges locally uniformly to the convex envelope.  It excludes all
noninvariant competitors; P03.1--P03.3 and every inventory count therefore
remain unchanged.  The exact source and scope ledger is
`solver_dossiers_20260910/p033_invariant_toric_lfs_minorant_envelope_20260910/`.

The same invariant envelope is also locally in the first decreasing CLD-smooth
psh stage by
cor:p024-invariant-toric-cld-smooth-regularization.  Thus this exact
invariant-toric chamber settles the nonempty-upper-semicontinuous-obstacle
restricted P03.1 classical-psh and P03.2 CLD-v2 assertions; for continuous
obstacles it also settles the P03.3 continuity assertion.  It says nothing
about the noninvariant local-FS/semipositive-real-PL envelope, so none of
P03.1--P03.3 retires.

The continuous invariant-psh portion now extends from convex tropical
chambers to every ordinary tropical open set.  If an upper-semicontinuous
invariant obstacle has one finite continuous locally convex minorant, the
raw envelope over all finite continuous invariant current-psh minorants is
the pullback of the supremum of its finite continuous locally convex
minorants.  On each convex ball that supremum is finite convex, so it is
continuous and supplies a current-psh function; the local toric
correspondence gives the reverse envelope comparison.  The germwise P02
regularization result then places it at the first decreasing CLD-smooth
stage.  The same germwise theorem also gives decreasing locally
Fubini--Study, weakly smooth, and (on good strict pieces) semipositive-real-PL
regularizations of this envelope, but it does not make those approximants
minorants of the obstacle.  This handles nonconvex ambient tropical domains
but deliberately does not compare with a real-PL, locally-Fubini--Study,
semipositive-real-PL, or any noninvariant envelope there.  It therefore narrows the invariant
P03 range without retiring P03.1--P03.3 or changing the count.

The strict LFS-minorant comparison has a correspondingly local nonconvex
form.  At every point admitting a relatively compact ordinary convex ball
whose inverse image is good, separated, strictly analytic, and boundaryless,
the raw invariant LFS envelope for the restricted obstacle is the pullback
of the convex-minorant envelope on that ball and has an increasing locally
uniform LFS approximation from below.  A locally convex global minorant
supplies the required convex minorant after passing to a slightly larger
ball.  This is a statement about that restricted ball only: it neither
identifies the raw LFS envelope on the ambient nonconvex open set nor
introduces a noninvariant competitor.  Thus it further records the local
invariant P03 range without retiring an atom or changing the count.

On the same strict boundaryless ball, the conclusion strengthens from the
LFS subfamily to the full invariant part of the original local-
Fubini--Study/semipositive-real-PL competitor union: its raw envelope, the
semipositive-real-PL raw envelope, and the LFS raw envelope all equal the
ball's convex-minorant envelope.  It is finite, continuous, CLD-v2 psh, and
classically psh, with the preceding increasing LFS approximation.  This
uses the strict-domain comparison only after restricting to the ball; it
does not compare the corresponding global envelope on a nonconvex ambient
open set and leaves all three P03 atoms active.

On a good separated strictly analytic boundaryless such toric domain,
the same envelope is exactly the raw envelope over the full
maximal-compact-torus-invariant part of the original
local-Fubini--Study/semipositive-real-PL competitor union.  Indeed, a
locally Fubini--Study function is real PL and semipositive at every point,
so that alternative contributes no functions outside the invariant
semipositive real-PL class.  Every supporting affine function gives the
reverse comparison through the CLD-to-classical and real-PL comparisons;
GJR's one-way current theorem puts each semipositive competitor in the psh
class without a pure-dimensionality assumption.  By the preceding
first-stage result, this exact invariant
local-Fubini--Study/semipositive-real-PL raw envelope is also locally CLD-v2
and classically psh.  This does not control any noninvariant candidate in
the original envelope.

### `prob:frontier-local-ma` --- 4 atoms

Each atom must carry a stated boundary datum and satisfy model independence,
monotone continuity, locality, and functoriality.

- **P04.1** `[T4; open]` Extend the verified common-model product to
  arbitrary nonalgebraizable analytic modifications.
- **P04.2** `[T4; open]` Construct the product for arbitrary bounded
  classical psh functions outside the jointly realizable model closure.
- **P04.3** `[T5; open]` Construct a finite-energy or unbounded extension
  with a coherent polar-mass rule.
- **P04.4** `[T5; open]` Extend the construction to singular and nonnormal
  germs, compatibly with normalization and conductor descent.

The model-algebraizable and jointly realizable bounded core is verified.
Probability normalization under literal restriction and uniqueness of an
unrestricted unbounded continuation are disproved.

### `prob:frontier-polyhedral-regularity` --- 3 active atoms

- **P05.1** `[T3; open]` Characterize the pairs \((\mathbf X,\gamma)\) for
  which the Botero--Mazzon--Pille-Schneider regularity property holds.
- **P05.2** `[T3; open]` Characterize the pairs for which their
  orthogonality property holds.
- **P05.5** `[T4; open after the calibrated recursive model cases]`
  Characterize polarized Monge--Amp\`ere realizations of
  \((\mathbf X,\gamma)\), construct global semipositive lifts of the
  relative potentials \(a_i-\gamma\) in a named BFJ domain, prove the exact
  intersection-mass and component-calibration identities, and compare the
  resulting global non-Archimedean Monge--Amp\`ere measure with the
  polyhedral measure, including boundary and mixed products.

Complete affine space, the exact normalization, and the abstract cross-fan
counterexample are verified.  The positive-at-infinity Bergman-fan
obstruction \(\texttt{prop:frontier-polyhedral-bergman-positive-infinity-obstruction}\)
now strengthens the source's \(U_{3,4}\) example: for a polyhedrally convex
reference with the required growth, the constructed envelope agrees with
the source reference near its mass-four origin.  A bounded PA reference
shift identifies its envelope and regularization classes with those of a
conical reference, so the displayed positive-at-infinity pair itself has
regularity and its orthogonality integral is at most
\(-4\varepsilon\).  Thus positive growth alone cannot yield a
smooth-Bergman regularity-and-orthogonality theorem.  This does not decide
either characterization atom.  P05.3 and
P05.4 are retired by
`prop:p053-projection-recursion-repaired-candidate` and
`cor:p053-algebraic-chart-repaired-candidate`: the proof constructs the
intermediate source currents, retains contractions and saturated lattice
indices, identifies the CLD and delta-form products, and passes to
regularizable weights.  P05.5 remains open precisely at the proper
polarized realization, global lift, mass, calibration, and operator-domain
gates stated above.  The production-verified
`prop:p055-boundary-mass-completion` proves that a local pushforward equality
and equality of finite positive total masses force zero source-boundary mass
and the global extension-by-zero identity; it closes the last purely
measure-theoretic step but supplies none of the geometric inputs.  The
production-verified `prop:p055-model-calibration-transfer` now proves the
full BFJ--Chambert--Loir--formal-CLD model-measure and proper-pushforward
comparison once a proper polarized realization, global semipositive model
lifts, exact mass matching, and componentwise intersection calibration are
given.  It deliberately makes no GK assertion on the original
analytification in this field scope.  Thus P05.5 remains active precisely at
the construction and calibration inputs, not at the subsequent atomic
measure bookkeeping.

The new bounded-reference-shift proposition
`prop:frontier-polyhedral-bounded-reference-shift` identifies the
polyhedral psh, piecewise-affine, and regularizable classes for any two
references differing by a bounded piecewise-affine function; it also
identifies their envelope problems and transfers orthogonality in both
directions.  In particular,
`cor:frontier-polyhedral-boundedly-conical-regularity` puts every
piecewise-affine polyhedrally convex reference that is a bounded
piecewise-affine perturbation of a positive-at-infinity conical reference
in the P05.1 regularity range.  This is a genuine reference-class reduction,
not a characterization.  The conical source result gives regularity only,
so it yields no new unconditional P05.2 case.

The source's only announced strict-positivity extension is an upcoming
sequel, whose own bibliography labels it ``In preparation.''  It is not an
available theorem for P05.1 or P05.2 and is therefore not used to narrow
either atom; see BMPS26, pp. 4 and 45.

### `prob:frontier-pluriharmonic` --- 2 atoms

- **P06.1** `[T2; open after the quasi-smooth, all strict-curve, arbitrary
  finite curve-factor, finite constant-group quotient, finite-flat cover of
  a verified range, all-orbits split
  toric, split-toric quasi-smooth-product and arbitrary-curve-factor
  product, algebraic-split toric-form and its arbitrary-curve-factor product,
  pointwise analytic algebraic-split toric charts with arbitrary curve
  factors,
  source-Zariski-local ordinary-etale algebraic-split toric charts with
  arbitrary curve factors,
  analytic standard-etale algebraic-split toric charts with arbitrary curve
  factors,
  positive-weighted affine-cone vertex and finite relative
  positive-weighted-cone towers over any verified base range along their
  composite zero sections, together with displayed analytic standard-etale
  perturbations at central-fibre points over a quasi-smooth or otherwise
  verified central fibre and algebraic ordinary-etale germs over the zero
  section of a relative positive-weighted cone with smooth algebraic base,
  including finite algebraic towers at their composite zero sections,
  algebraic-split analytic-toric-form,
  algebraic-split-form quasi-smooth-product, transverse toric-product, and
  source-Zariski-local ordinary-etale algebraic-split-toroidal and analytic
  standard-etale algebraic-split-toroidal cases]` On a good,
  separated, strict, boundaryless analytic space, outside the local
  arbitrary-curve-factor scope of
  `thm:p061-arbitrary-curve-factors-ph-rpl`, the positive-weighted-cone vertex
  scope of `thm:p061-positive-weighted-cone-vertex-constancy`, its relative
  zero-section and finite-tower scope of
  `prop:p061-relative-positive-weighted-cone-descent` and
  `cor:p061-iterated-relative-weighted-cone-closure`, the standard-etale
  central-fibre scope of `thm:p061-standard-etale-weighted-cone-tube`, the
  algebraic ordinary-etale zero-section scope of
  `thm:p061-algebraic-etale-weighted-cone-zero-section` and
  `thm:p061-algebraic-etale-weighted-cone-towers`, and the
  all-orbits split toric
  and algebraic-split-form scope of `thm:p061-split-toric-all-orbits` and
  `cor:p061-algebraic-split-toric-forms` and
  `cor:p061-algebraic-split-analytic-toric-forms`, and outside the split-toric
  quasi-smooth and arbitrary-curve-factor product scope of
  `cor:p061-split-toric-quasismooth-products` and
  `cor:p061-toric-arbitrary-curve-factor-products`, and outside its pointwise
  analytic algebraic-split extension
  `cor:p061-analytic-toric-arbitrary-curve-factor-products`, and outside the
  source-Zariski-local ordinary-etale algebraic-split product extension
  `cor:p061-etale-toric-arbitrary-curve-factor-products`, and outside the
  analytic standard-etale algebraic-split product extension
  `cor:p061-analytic-standard-etale-arbitrary-curve-factor-products`, decide whether
  every classically pluriharmonic function is \(\mathbf R\)-PL near a
  non-quasi-smooth point of analytic dimension at least two.
- **P06.2** `[T2; open after the weakly smooth, real-PL, proper full-rank
  moment-factor, good-strict invariant split-toric (including boundary) and
  algebraic-split scalar-stable invariant-toric, including its analytic-local
  algebraic-split analytic-form and scalar-stable open-polydisc-bundle
  versions, including the latter's analytic-local version,
  algebraically closed closed-polydisc, arbitrary-field standard strict
  endpoint-polycylinder, arbitrary-radius scalar-stable endpoint-polycylinder,
  smooth-proper-curve, arbitrary-field scalar-stable locally trivial proper
  smooth curve-bundle descent, and strict-open-polydisc product or locally
  trivial
  bundle or finite tower of such bundles, locally trivial projective-space
  bundles, locally trivial smooth proper split-toric bundles, or locally
  trivial proper smooth connected curve bundles over a published curve,
  including finite mixed towers in which these four bundle
  types occur in any order and globally coordinated standard strict-open-
  annulus products over the boundaryless tops of such towers, including
  finite boundaryless towers in which globally coordinated standard strict-
  open-polyannulus product stages occur at arbitrary levels among those four
  exact bundle types, including curve-locally coordinated versions in which
  one analytic open cover of the original curve trivializes every annular
  stage after base change, and finite globally coordinated
  standard strict-open-annulus products over a boundaryless finite tower of
  locally trivial standard strict-open-polydisc bundles over a published
  curve, or analytically locally trivial finite
  standard strict-open-polyannulus or mixed open-polycylinder bundles,
  including finite towers of strict-open-polydisc bundles over these
  product or bundle bases, over a published-curve,
  endpoint-polycylinder-base or a finite tower over such a base, and lifted-
  maximal-compact-torus-invariant split-toric-base cases]` Decide
  whether an arbitrary
  continuous function with zero
  \(\mathrm d'\mathrm d''\)-current is classically pluriharmonic, or
  harmonic whenever the classical notion is available, outside the verified
  standard strict-coordinate-product, invariant split-toric, factorized, and
  curve scopes, with the arbitrary-germ, nonproduct, strict-core-only, and
  weaker-than-scalar-stable boundary-control residuals stated below.  The
  unrestricted arbitrary-radius product extension is now known to be false.

The weakly smooth zero-current statement is known.  The real-PL
zero-current implication is now verified on good separated boundaryless
strict pure-dimensional spaces by production run
`20260825T061351Z_655e7f503e5d`: it uses rational coefficients of calibrated
skeletal currents and does not extend to arbitrary continuous functions.
There is also a good-strict invariant split-toric boundary case.  On an open
inverse image under extended tropicalization in a split toric variety, every
finite continuous maximal-compact-torus-invariant function with zero CLD
Hessian is locally CLD-smooth with zero Hessian, real-PL, GJR harmonic, and
classically pluriharmonic; this includes the toric boundary strata.  The
exact statement/proof SHA-256 values are
`8d69697806c33d59531b5d3247a2f9e0c1d07e313d329c15a2432646134a544a` and
`c17e99ebb54f45003d78f55670a978092294b44a7c4536b78d7207ec52cfda85`.
The dependency-closed packet passed independent model-backed verification as
item `pi_30ec53e8836ba1d2b08fdf64`, final `correct`, with zero critical errors
and zero gaps.  It does not address noninvariant functions, nonsplit toric
forms, arbitrary toroidal charts, or arbitrary analytic germs, so P06.2
remains active and the inventory count is unchanged.
The algebraic-split scalar-stable invariant-toric range is now also live.  If
a good strict analytic form becomes a split toric open inverse image over a
complete analytic extension which is the completion of an algebraic extension,
and the pulled-back finite continuous function is maximal-compact-torus-invariant
with zero CLD Hessian there, then
`cor:p062-algebraic-split-invariant-scalar-stable-zero-current` descends local
real-PL regularity, classical pluriharmonicity, and GJR harmonicity.  Its
upstairs invariance and zero-current assumptions are explicit; no automatic
ascent of the downstairs continuous Hessian current is asserted, and no
model-backed verifier was used for this direct source-cited corollary.
The analytic-local companion
`cor:p062-local-algebraic-split-invariant-scalar-stable-zero-current` transfers
the same conclusion to every germ which becomes one such displayed split
toric domain after an extension which is the completion of an algebraic
extension, after imposing the
upstairs assumptions.  It does not manufacture a model for a general analytic
germ and uses no model-backed verifier.
The invariant split-toric range also propagates through an actual locally
trivial standard strict open-polydisc bundle when the maximal compact torus
action lifts and the continuous zero-current function is invariant upstairs.
`cor:p062-invariant-toric-open-polydisc-bundles` first uses the exact bundle
descent to obtain a zero-current base function, whose invariance follows
from equivariance and surjectivity, and then applies the split-toric boundary
theorem.  This does not treat noninvariant functions, nonsplit forms,
annular fibres, or bundles without the displayed local product charts.
The same split-toric conclusion persists through every finite such tower
when the maximal compact torus acts on each level and every bundle map is
equivariant: `cor:p062-iterated-invariant-toric-open-polydisc-bundles`
successively descends the invariant zero-current function to the toric base.
Its scalar-stable algebraic-split companion
`cor:p062-algebraic-split-invariant-toric-open-polydisc-bundles` applies when
the entire displayed bundle becomes such a toric bundle after a complete
extension that is the completion of an algebraic extension, and the lifted
action, invariance, and zero-current assumptions are all imposed upstairs.
It descends the resulting real-PL, classical-pluriharmonic, and GJR-harmonic
conclusions, but asserts neither automatic current ascent nor a toric-bundle
presentation for an arbitrary germ.
Its finite-tower version,
`cor:p062-iterated-algebraic-split-invariant-toric-open-polydisc-bundles`,
requires the entire compatible tower, lifted action, invariance, and
zero-current equation after the chosen algebraic-completion extension; it
then descends the same three conclusions to the original field.
The analytic-local companion
`cor:p062-local-algebraic-split-invariant-toric-open-polydisc-bundles`
requires the preceding bundle, extension, action, invariance, and
zero-current data only near each point of the total space.  It makes no
claim where that local structure is absent.
The finite-tower analogue,
`cor:p062-local-iterated-algebraic-split-invariant-toric-open-polydisc-bundles`,
likewise needs the entire displayed scalar-stable tower only near each point
of the total space.  In particular, every tower level must carry the
compatible lifted torus action and every bundle map must be equivariant after
the specified algebraic-completion extension.  It yields the same local
real-PL, classical-pluriharmonic, and GJR-harmonic conclusions, but neither
constructs such local data nor supplies automatic ascent of a downstairs
current equality.
The quasi-smooth scope of P06.1 is settled by
`thm:p061-quasismooth-ph-rpl`: every classically pluriharmonic function on a
good strict quasi-smooth analytic space is \(\mathbf R\)-PL and GJR
harmonic, without global quasicompactness, separatedness, or
boundarylessness. The proof combines Temkin's altered local uniformization
with rigid étale sheaf descent. The published curve comparison already
covers all strict analytic curves, including singular and nonreduced ones
(`GR25Classical`, §4.1.2 and Proposition 3.15).
The same conclusion now descends through every finite, flat, surjective map
of good strictly analytic spaces: if the source is in any verified P06.1
regularity range, `cor:p061-finite-flat-cover-descent` applies GJR26,
Proposition 5.11 with divisible coefficient group \(\mathbf R\) to descend
real-PL regularity, and GR25Classical, Theorem 4.3 supplies GJR harmonicity.
This covers a neighbourhood only when such a finite-flat cover is actually
given; it does not manufacture one for an arbitrary singular germ.
The exact finite-product extension is now also verified.  By
`thm:p061-curve-product-ph-rpl` and
`cor:p061-finite-curve-products-ph-rpl`, every classically pluriharmonic
function is \(\mathbf R\)-PL and GJR harmonic on a good product of finitely
many geometrically reduced good strict analytic curves and a good strict
quasi-smooth factor, and on every good strict space locally isomorphic to an
open analytic subspace of such a product.  The normalization-descent input is
`prop:p061-curve-product-normalization-descent`; the concrete nodal and
cuspidal strata are recorded in `ex:p061-nodal-cuspidal-products`.  The exact
statement/proof SHA-256 values are
`96b246d6f6032bce38751095935525a67456c6753e006e7b188778bc945e50bc` and
`6f6158b5253922539f81e42ab9e6d9e2c48a6b3c8b727e4157351b9591baabe5`.
Production run `20260829T191019Z_0b5e24145108`, item
`pi_6add90bcf0cfded12d6a074b`, returned final `correct`, with zero critical
errors and zero gaps.  This does not cover arbitrary singular germs,
or spaces without the stated local product decomposition.
The reducedness restrictions on the curve factors have now also been
removed.  By `thm:p061-arbitrary-curve-factors-ph-rpl`, the same conclusion
holds for arbitrary finite products of good strict analytic curves, including
nonreduced and non-geometrically-reduced ones, with a good strict factor whose
reduction is quasi-smooth, as well as their stated local open-product models.
The case with no curve factor includes nilpotent thickenings of quasi-smooth
spaces.  Its exact statement/proof SHA-256 values are
`6954b3ebc1f9efb060b4858ce732d9720d62741ba2397c39573312dd6e3ba8f3` and
`e308ba5df336e38717ac27413c6f669a7fa37535bed613a79f095811c6dba4a7`.
Production item `pi_7dceb6442b4d586c4475feca` returned final `correct`,
with zero critical errors and zero gaps.
There is also a non-toric positive-weighted-cone vertex range.  By
`thm:p061-positive-weighted-cone-vertex-constancy`, an affine cone defined by
positive-weighted homogeneous equations has no nonconstant classically
pluriharmonic germ at its vertex.  The proof contracts any point of a
cofinal weighted affinoid neighbourhood to the vertex along a closed disc
over its completed residue field; classical pluriharmonicity pulls back, and
the disc maximum--minimum principle forces equality.  Thus the conclusion
does not require the cone to be reduced, normal, irreducible, or toric.  It
includes, for example when \(\operatorname{char}K\ne3\), the normal isolated
cubic cone `x^3+y^3+z^3=0`.  It neither creates a weighted-cone presentation for an
arbitrary germ nor gives a conclusion away from the vertex.
There is also a relative positive-weighted-cone zero-section range.  For a
strict affinoid family defined over a strict affinoid base by
positive-weighted homogeneous fibre equations, including analytic
base-dependent coefficients, `prop:p061-relative-positive-weighted-cone-descent`
uses the fibrewise closed-disc contraction over every completed residue field
to show that a classically pluriharmonic function factors through the base on
a sufficiently small weighted tube around the zero section.  Consequently,
`cor:p061-iterated-relative-weighted-cone-closure` propagates the local
pluriharmonic real-PL property from any verified base range through an
arbitrary finite tower of such relative cones, along the composite zero
section.  Intermediate bases may be singular and later coefficients may
depend on earlier fibre variables; no common grading, product, flatness,
reducedness, normality, or irreducibility is required.  The displayed
two-stage example with equations `x^3+y^3+z^3=0` and
`UV-(x+y^2)W^2=0` has no common positive weighting, although each stage is
positively homogeneous in its new variables.  This says nothing about
points away from the composite zero section or a base outside the initial
verified regularity range, so P06.1 remains active and the count is
unchanged.
The weighted-cone range is now also stable under the displayed strict
analytic standard-etale presentations.  After shrinking the cone variables,
the kernel of the zero-section retraction tends to zero in the quotient
Gauss norms.  The existing contractive Newton lemma then identifies the
source tube with the same relative cone after base change to the central
standard-etale fibre.  Thus `thm:p061-standard-etale-weighted-cone-tube`
propagates the local pluriharmonic real-PL property from that fibre to the
source point; a quasi-smooth original base is sufficient because the
Jacobian criterion makes the central fibre quasi-smooth over it.  The example
`T^2-T-x=0`, with the derivative inverted, shows that the displayed source
equations need not be positively homogeneous.  This treats only central-
fibre points in an actual strict standard-etale presentation and asserts no
uniformization of an arbitrary singular germ, so P06.1 and all counts remain
unchanged.
The displayed-chart hypothesis is now removed for the corresponding
algebraic ordinary-etale zero-section germs.
`thm:p061-algebraic-etale-weighted-cone-zero-section` starts with a separated
finite-type algebraic etale morphism to a relative positive-weighted cone
over a smooth algebraic base.  Stacks Project Tag 025C supplies only an open
immersion into a standard-etale scheme; the proof then chooses a principal
open inside its image, shrinks the target to an actual strict relative-cone
affinoid, and imposes strict bounds on the standard-etale coordinate and its
inverse.  These three firewalls put the chosen source point in an ordinary
analytic neighbourhood before the preceding tube theorem is applied.  The
result neither treats points away from the zero section nor produces a
weighted-cone target for an arbitrary germ, so P06.1 and all counts remain
unchanged.
The same algebraic localization now propagates through every finite tower of
the displayed relative weighted cones.
`thm:p061-algebraic-etale-weighted-cone-towers` strengthens the induction
statement to all separated finite-type algebraic etale sources over a shorter
tower: after the top standard-etale tube is constructed, its central domain
is proved to be an ordinary neighbourhood in an algebraic etale source over
the preceding stage, so the induction hypothesis supplies the central-germ
regularity.  This avoids assuming that singular intermediate bases are
quasi-smooth.  Different stages need no common grading, but the result remains
confined to the composite zero section and does not manufacture such a tower
for an arbitrary singular germ.  P06.1 and all counts remain unchanged.
There is independently an affine toric scope:
`thm:p061-toric-fixed-point-constancy` proves that every classically
pluriharmonic germ at the torus-fixed point associated to a full-dimensional
strongly convex rational cone is locally constant.  Its exact
statement/proof SHA-256 values are
`edbe69950a0a9c81ca2fd9077a58be96ec6bdb6c27ce9cf2524da5bf653a5ab6` and
`531e326b4aeb19067fcb88af2f6eb6477a169587d71a3249103777c9131cf8f4`.
Production item `pi_dfd932c583fee3acd3fefbe3` returned final `correct`,
with zero critical errors and zero gaps.  This fixed-point theorem does not
cover positive-dimensional torus orbits or arbitrary toric domains.
Real-PL regularity also descends through arbitrary finite constant-group
quotients of separated strict affinoids.  The exact statement/proof SHA-256
values of `prop:p061-finite-group-rpl-descent-candidate` are
`e1daa4b3e3efd64fcc8f0ce05b9c1d5d6cb69b28686b939b48535fc56b0ccc07` and
`a6c24d1686c726dc72aebe55a1e83eb8d4fe1ed4025d4a8d7166da59123ce30e`.
Two source-aware hostile audits passed.  Production run
`20260829T235341Z_e1daa4b3e3ef` used `gpt-5.6-sol` at `xhigh` and returned
final `correct`, with zero critical errors and zero gaps; the direct endpoint
assigned no item identifier.  No flatness, freeness, reducedness, normality,
or invertibility of the group order is assumed.  Hence the verified P06.1
source scopes remain verified after taking separated strict affinoid finite
constant-group quotients.  The theorem does not produce such a quotient
uniformization for an arbitrary singular germ.
The finite-group argument has now been combined with an exact radicial
Frobenius descent proposition to cover every good strict domain in a split
simplicial affine toric variety, including a non-full cone and a quotient
index divisible by the ground-field characteristic.  The exact live
statement/proof SHA-256 values of
`prop:p061-frobenius-rpl-descent` and
`thm:p061-simplicial-toric-ph-rpl` are
`b2cdce85c771e2ccf6bbd4d0fd8ba274d521d35d3d371a5575c71b77db5aabce`
and
`e81b0f7d1156af135c75dcd15ec11b636e2d82131715cfbee0d765fd1c8900e0`.
An independent hostile audit passed.  A dependency-closed production
request using `gpt-5.6-sol` at `xhigh` returned final `correct`, zero
critical errors, and zero gaps; the direct endpoint assigned no run or item
identifier.  The archived request/response/header SHA-256 values are
`246d058026f2581c0e6c1b28f6231b936e697c1613b78f1fce7cbcbdd773f2b9`,
`b4a03f9def9dbb51cdb808951afe6a1a0232a2b54e8493b8a2c37c0eeb2e4467`,
and
`f327f862ee85670ad3cdff73e3212734eb9c4e2edf391f0325f1a50489a40f26`.
This simplicial theorem is retained as an independent quotient-descent
result.  The stronger all-orbits theorem now removes simpliciality and the
closed-orbit restriction.  `thm:p061-split-toric-all-orbits` and
`cor:p061-split-toric-varieties` cover every ordinary open analytic subspace
of every split toric variety, for arbitrary fans and at every orbit;
`cor:p061-algebraic-split-toric-forms` descends the conclusion for forms that
become split after the completion of an algebraic extension.  The
parameterized fixed-fibre theorem also
covers actual local products of a pointed full-dimensional affine toric
factor with a quasi-smooth factor.  The exact statement/proof SHA-256 values
are
`05bda70eb1cf7ebbcc95d1831feadd946afa168f64a7298171381b9f1e865e60` /
`21c44c47a91a28469fb91a6c00569ed56d12699bae9c956c68c33ad493825b03`.
An independent exact-byte hostile audit passed.  Dependency-closed
production Rethlas using `gpt-5.6-sol` at `xhigh` returned final `correct`,
zero critical errors, and zero gaps.  The archived
request/response/header SHA-256 values are
`def28bf9f16539fadab9b8b99dbd435d00eed8c3730c496d2b8832ee865a29c9` /
`718044118ee65e0d76b7c02b8b553552b8da974367513aa5ed4d57e8b6231f7d` /
`4146f66712746a54a0f3f2be457e6ae87cd4ab1be92013e1e8480765492d7958`.
The orbitwise proof has a further direct consequence:
`cor:p061-split-toric-quasismooth-products` covers every ordinary open
analytic subspace of a split toric variety times a good strict quasi-smooth
analytic space, as well as analytic spaces locally modeled on such an open
subspace.  At each orbit, the principal-open product chart replaces the
parameter by the product of the orbit torus and the given quasi-smooth
factor; this is again quasi-smooth, so
`prop:p061-parameterized-toric-fixed-fibre` and
`thm:p061-quasismooth-ph-rpl` apply.  This is a direct consequence of the
verified all-orbits and fixed-fibre arguments, not a claim about nonsplit
toric factors, non-quasi-smooth parameters, or spaces without an actual
local product chart.
The same conclusion descends to algebraic-split toric forms with a good
strict quasi-smooth parameter.  Over a complete splitting extension which is
the completion of an algebraic extension, the pullback lies in the preceding
split-toric product range; classical pluriharmonicity and quasi-smoothness
survive scalar extension, and `GJR26`, Corollary 5.12 descends the resulting
real-PL function.  Hence `cor:p061-algebraic-split-toric-forms` includes
ordinary open subspaces of such products and their analytic local product
models.  It does not cover forms without such an algebraic splitting
extension, non-quasi-smooth parameters, or arbitrary nonproduct germs.
The toric and curve-factor ranges also combine directly.
`cor:p061-toric-arbitrary-curve-factor-products` treats every ordinary open
analytic subspace of the product of a split toric variety, an arbitrary
finite family of good strict analytic curves, and a good strict factor with
quasi-smooth reduction.  At an arbitrary toric orbit, the exact principal
open decomposition makes the transverse pointed toric factor visible and
absorbs the orbit torus into the last factor; its reduction remains
quasi-smooth.  The parameterized fixed-fibre theorem then factors a
classically pluriharmonic function through a parameter in the scope of
`thm:p061-arbitrary-curve-factors-ph-rpl`.  The same conclusion descends for
a toric form split by the completion of an algebraic extension.  This is a
formal combination of the two verified mechanisms, not a theorem for a
reduced higher-dimensional singular factor outside the toric factor, a form
without such a splitting extension, or a nonproduct singular germ.  P06.1
and all counts remain unchanged.
The same range is pointwise analytic local in the toric factor.
`cor:p061-analytic-toric-arbitrary-curve-factor-products` assumes that each
point has an ordinary neighbourhood which becomes an ordinary open subspace
of a split toric variety after a completed algebraic extension, carries the
curve factors and the factor with quasi-smooth reduction through scalar
extension, and descends the split product conclusion.  It does not produce
the splitting chart, replace the algebraic extension by an arbitrary
complete extension, or treat a nonproduct germ.  P06.1 and all counts remain
unchanged.
The same scalar-extension proof is analytic local.  If every point has an
ordinary neighbourhood which becomes an ordinary open subspace of a split
toric variety after one displayed complete algebraic splitting extension,
`cor:p061-algebraic-split-analytic-toric-forms` gives the same conclusion,
also after product with a good strict quasi-smooth parameter.  It does not
construct such a chart for an arbitrary analytic germ.
The ordinary-etale split-toroidal range is now also verified.
`prop:p061-v3-etale-toric-product` constructs an actual affinoid product over
a sufficiently deep weighted toric tube from a separated finite-type etale
map to a pointed split toric factor times a smooth factor;
`thm:p061-v3-etale-toroidal-ph-rpl` and
`cor:p061-v3-zariski-etale-toric-charts` give real-PL and GJR harmonicity,
including the rank-zero transverse factor at the dense orbit.  The principal
statement/proof SHA-256 values are
`fbb294c435dffacf8153a076846586d2bdf2ee68a6e7268f94d2a12241629c34` /
`10d188621a07242ea278c5699a27ef25488605365c953f94ddf0d08bb4ec9729`.
Independent exact-byte re-audit passed, and dependency-closed production
Rethlas using `gpt-5.6-sol` at `xhigh` returned `correct`, zero critical
errors and zero gaps.  The request/response/header hashes are
`dab3e30657a5118304753fa1eb97a07c9bbb3cfd72cacc5d64181e3dfd4ff44f` /
`7e06480126ac47adfa84bffba5dd9de913c6e73230808f710ddc8c9b73b0e1b5` /
`8f2831a5383da9db987a8cdb4dad4d4246775fa50afb754120d9aba71ae9b4d7`.
The same source-Zariski-local ordinary-etale conclusion now covers
algebraic-split toric forms.  If the toric factor of a chart becomes split
over a complete analytic extension which is the completion of an algebraic
extension, base change puts that chart in the preceding ordinary-etale
split-toroidal range; classical pluriharmonicity pulls back by GR25,
Proposition 7.2(6),(7), and GJR26, Corollary 5.12 descends the resulting
real-PL conclusion.  This direct source-cited corollary is live as
`cor:p061-zariski-etale-algebraic-split-toric-charts`; it has not been sent to
a model-backed verifier.  It does not manufacture an ordinary-etale chart or
cover forms without such an algebraic splitting extension.
The manufactured ordinary-etale tube now also carries arbitrary finite good
strict analytic curve factors.  In
`cor:p061-etale-toric-arbitrary-curve-factor-products`, singleton-Shilov
factorization leaves those curves, the quasi-smooth fixed-fibre factor and a
final factor with quasi-smooth reduction.  The fixed fibre may be grouped
with that final factor because the reduction of their product is
quasi-smooth; the existing arbitrary-curve-factor theorem then applies, and
completed-algebraic-extension descent returns the conclusion to the ground
field.  This result requires the displayed source-Zariski-local
ordinary-etale chart and an actual external product.  It does not cover a
genuinely log-etale chart, a toric form outside the stated splitting class,
or a locally twisted nonproduct germ.  P06.1 and all counts remain unchanged.
The same tube argument has a direct analytic standard-etale extension.
`prop:p061-analytic-standard-etale-toric-product` starts from an actual
strict affinoid chart over a weighted pointed split toric domain times a
good strict quasi-smooth affinoid parameter, with a monic standard-etale
Tate presentation.  The normalized toric restriction makes every finite
coefficient error contract to zero, so the existing common-Newton-radius
lemma gives an actual product tube.  The fixed fibre is quasi-smooth and
the fibrewise semigroup Gauss norm is singleton Shilov, yielding
`thm:p061-analytic-standard-etale-toroidal-ph-rpl` and the local chart
corollary `cor:p061-analytic-standard-etale-toroidal-charts`.  This direct
extension does not assert a standard-etale presentation for an arbitrary
analytic etale map, and it does not cover a non-quasi-smooth parameter or a
non-etale local model.
At an arbitrary orbit of a split toric base,
`cor:p061-analytic-standard-etale-all-orbits` applies the exact principal
toric decomposition and absorbs its split-torus factor into the
quasi-smooth parameter.  It therefore covers an actual standard-etale
strict affinoid chart over an arbitrary split toric variety when its target
affinoid is an ordinary neighbourhood of the image point.  This remains a
chart criterion: it supplies neither that ordinary-target condition nor a
standard-etale presentation for an arbitrary analytic etale map.
When the toric base becomes split over a complete analytic extension which is
the completion of an algebraic extension,
`cor:p061-analytic-standard-etale-algebraic-split-forms` pulls this chart to
the split extension, applies the all-orbits conclusion there, and descends
the resulting real-PL function.  It retains the ordinary-target condition and
does not cover forms without such an algebraic splitting extension.
The same actual analytic standard-etale tube now carries arbitrary finite
good strict analytic curve factors.  In
`cor:p061-analytic-standard-etale-arbitrary-curve-factor-products`, the
coefficient contraction manufactures the weighted toric product before
singleton-Shilov factorization.  The retained quasi-smooth fixed fibre is
grouped with a final factor having quasi-smooth reduction, and the existing
arbitrary-curve theorem applies.  Completed-algebraic-extension descent
includes algebraic-split toric bases.  This remains an explicit chart and
external-product criterion: it does not manufacture a standard-etale chart
for an arbitrary analytic etale map or cover a locally twisted nonproduct
germ.  P06.1 and all counts remain unchanged.
P06.1 remains active only for arbitrary nonproduct singular germs, products
containing higher-dimensional reduced singular factors outside the verified
ranges, genuinely log-etale charts not covered by an ordinary-etale chart of
the displayed toroidal or weighted-cone kind or by the displayed analytic
standard-etale charts, and
nonsplit local models outside the verified algebraic-split descent range.
The coefficient cannot be strengthened: `prop:p061-integral-pl-counterexample`
gives \(\sqrt2\log|T|\) on a strict semistable annulus, which is not
\(\mathbf Q\)-PL. The exact statement and proof passed production Rethlas
run `20260829T043457Z_0b1b4d161e3b`, item
`pi_7cd35ebd843cf80a7cd696bb`, final `correct`, with zero critical errors
and zero gaps. P06.1 remains one active T2 atom, now confined to arbitrary
nonproduct non-quasi-smooth points in dimension at least two outside the
verified product and quotient ranges, products containing a reduced singular
factor of dimension at least two outside those ranges, genuinely log-etale
charts not covered by the verified ordinary-etale algebraic-split-toroidal
theorem, and nonsplit local models outside the algebraic-split range. No atom count, tier
count, or queue position changes.
The proper full-rank moment-factor case is also verified by
`prop:p062-proper-full-rank-moment`.  It applies only when \(X\) is pure of
dimension \(n\geq 1\) and \(h=\varphi\circ F\), where
\(F=(-\log|f_1|,\ldots,-\log|f_n|)\) is one pleasant full-rank moment,
\(F(X)=F(\Sigma_F^{(n)})\) is a nonempty connected open subset of
\(\mathbf R^n\), \(F\) has compact inverse images of compact subsets, and
the pushed-forward canonical calibration has constant positive
multiplicity.  In this scope, zero current forces \(\varphi\) to be affine.
When \(X\) is boundaryless,
`cor:p062-proper-full-rank-moment-automatic-calibration` makes the constant
calibration automatic and gives the converse.  The exact statement and proof
passed production Rethlas run `20260829T031126Z_75e9cb498ce4`, item
`pi_f96fe9f8904943602779f274`, final `correct`, with zero critical errors and
zero gaps.  No theorem in the packet constructs such an \(F\) for an
arbitrary continuous function, so P06.2 remains one active T2 atom outside
this factorized scope.  No atom count, tier count, or queue position changes.
The factorization-free strict-polydisc case is now verified as well.
`thm:p062-polydisc-zero-current-candidate` proves that, over an algebraically
closed complete nontrivially valued field, a continuous function with zero
CLD current on a strict open polydisc is constant; the same holds on a strict
closed polydisc when the equation holds on its analytic interior.  Its exact
statement/proof SHA-256 values are
`017f3da108ae737e4bbc1d490d6988faf76ce643b4cb52104aae53c4dcda75d6` and
`3763bf9a7e4b1f47602544ad2c3248d9b8abd7b9d34109e3c14259e422393bbd`.
An independent exact-byte hostile audit passed.  Production run
`20260830T001728Z_017f3da108ae` used `gpt-5.6-sol` at `xhigh` and returned
final `correct`, with zero critical errors and zero gaps; the direct endpoint
assigned no item identifier.  The theorem does not descend the conclusion to
an arbitrary complete ground field by itself and does not uniformize an
arbitrary analytic germ by strict polydiscs.  The following
one-dimensional finite-trace theorem removes the first restriction for
strict discs, but not in higher dimension.  Thus P06.2 remains one active
T2 atom, and the atom count, tier count, and queue position remain unchanged.

The arbitrary-field one-dimensional strict-disc case is now verified.
`prop:p062-finite-flat-continuous-trace` proves continuity of the calibrated
trace of an arbitrary continuous multiplier under a finite flat analytic
map, identifies its current with direct image, and preserves vanishing
Hessian.  For a rigid point, its minimal polynomial gives a finite flat map
of discs whose zero fibre and a selected Gauss fibre are both single fibres
of the full degree, including ramified and inseparable degrees.  Together
with the verified rational-centred radial identity and rigid-point density,
this proves `prop:p062-arbitrary-field-disc`: a continuous zero-current
function on a strict open disc is constant over every complete
nontrivially valued field; the closed-disc version holds when the equation
is imposed on the analytic interior.  The exact statement/proof SHA-256
values are
`67a8d8a21e23cb34cf9b8f6685efbf2c9eaa6ff484b3696cbc1867a8940e095c`
and
`479643ee3aa534bbfc98adcf69837356d3cd8eff22d92accd1319aabb049553e`.
An independent exact-byte hostile audit passed.  The dependency-closed
production request archived as `20260830T033245Z_5c4711a474d8`, using
`gpt-5.6-sol` at `xhigh`, returned final `correct`, zero critical
errors, zero gaps, and thirteen checked citation uses; the endpoint assigned
no run or item identifier.  This does not prove the arbitrary-field result
on strict polydiscs of dimension at least two and does not uniformize an
arbitrary analytic germ.

At an earlier verification gate, the arbitrary-field result was extended to
every standard strict open
polycylinder.  `prop:p062-strict-product-fibre-slicing-v4-research` proves exact
restriction of the zero-Hessian current to every strict disc or annulus
fibre over the completed residue field of an arbitrary base point;
`prop:p062-arbitrary-field-annulus-v4-source-correct` and
`thm:p062-arbitrary-field-polycylinder-v4-source-correct` then give

```text
h = c + sum_j lambda_j log|S_j|.
```

Thus strict open polydiscs are constant over every complete nontrivially
valued field.  The frozen v3 statement/proof SHA-256 values are
`985be85d97b583f72be5cee65988df6f31c1edb49a685121b834df179fa87fda` /
`42b592bf8ac26ed46c36928e5e90272225ae6883bd2bfe62d3ff2840f01d46e5`.
After an independent exact-byte audit, dependency-closed production Rethlas
using `gpt-5.6-sol` at `xhigh` returned final `correct`, zero critical
errors, and zero gaps.  The archived request/response/header SHA-256 values
are
`6261b61bc49669a74a6eee4a2d834c25c8741bef59b084b81eaa684629f2d604` /
`c8c951075a574c6a3badde2e2a22942718616cd21da0144cb8a983bc3cac822f` /
`dcac7f45ad5464d4599d880862ce27c9c98e18cc3f4060bbf250426080c7fb45`.
That v3 packet was strictly open: the closed and half-closed endpoint
assertions rejected from v2 were absent.  A later transitive source audit
found that its slicing proof used a local-moment result in the wrong
direction.  The source-correct v4 proof below supersedes it; no live theorem
depends on the v3 proof.

The one-dimensional closed and half-closed annulus endpoints are now settled
by a separate proof, not by restoring the rejected v2 product claim.
`prop:p062-annulus-endpoint-arbitrary-field` proves that, over every complete
nontrivially valued field, a continuous zero-current function on each of

```text
{r<|T|<=R},  {r<=|T|<R},  {r<=|T|<=R}
```

is `a log|T|+b`, when the equation is imposed on the absolute analytic
interior.  Its exact frozen statement/proof SHA-256 values are
`a54723f040926d5a309494bb77d3c734c1c9d27bfb9fd18c56fc70ea4d03c9e1` /
`461afad5804a3269cb385550af6f4abcb5543d4f3151db56f986490c74e6947e`.
An independent exact-byte release audit passed.  Dependency-closed
production Rethlas using `gpt-5.6-sol` at `xhigh` returned final `correct`,
zero critical errors, and zero gaps.  The archived request/response/header
SHA-256 values are
`34a4d9f0d4b10a1f5a4693adef7a233a8ee756813dfe1f21450dc0cfd2d67242` /
`6b5aa2445bbd8b1dbe594fc23571c979d64eb5dc839f038101ce97b93181cee4` /
`7d1ce47df4f2cceae087f95d72337b90ce2a3a2b6c51cabf015395597ff3e396`.
The proof makes no product or higher-dimensional endpoint assertion by
itself.  It is, however, an ingredient in the following product theorem.

The higher-dimensional standard strict endpoint variants are now settled.
`thm:p062-endpoint-polycylinder-v4-research` proves over every complete
nontrivially valued field that, on any finite product of standard strict
open or closed discs and standard strict open, closed, or half-closed
annuli, a continuous function whose Hessian current vanishes on the absolute
analytic interior is

```text
h = c + sum_j lambda_j log|S_j|.
```

The proof uses only the inclusion of the product of the factor interiors in
the product interior, slices there, and propagates through rigid base points,
finite residue extensions, the one-dimensional endpoint result, and density.
The principal statement/proof SHA-256 values are
`56ffaad6c42e0a14c56279e263d326120ce03f6ae132d8261deee56ff9ca7663` /
`2616ac69cd450010b8f0d108d030bd69d2ff2728cad9641ad7d9d0e1a981a0b7`.
An independent exact-byte hostile audit passed.  Dependency-closed
production Rethlas using `gpt-5.6-sol` at `xhigh` returned final `correct`,
zero critical errors, and zero gaps.  The archived
request/response/header SHA-256 values are
`7b5bdbb4a15fb8d5202d57ddb4c49f84e1844908863c95580ceec7c1f1324171` /
`c0d9aaf5a8ef3400b6b20782a0a8d9073c24c200027c4451a9aec9e5432b446d` /
`1013a47eaabe8bdeec363937720e76b988fb76dbd90f2009ca10f6a513d0cb94`.

The arbitrary-radius residual now has a sharp negative--positive resolution
on standard products.  `prop:p062-nonstrict-boundary-resonance-counterexample`
takes \(R\notin\sqrt{|K^\times|}\) and the reciprocal closed bidisc
\(\{|T|\leq R\}\times\{|S|\leq R^{-1}\}\).  Its relatively open tube
\(\{|TS-1|<1\}\) lies entirely outside the absolute analytic interior, so an
explicit nonconstant continuous cutoff supported there has zero Hessian on
the interior.  Thus the unrestricted arbitrary-radius extension is false.
By contrast, `prop:p062-nonstrict-scalar-stable-repair` proves the full
affine formula on every arbitrary-radius standard endpoint polycylinder if,
after one complete extension strictifying the radii, the pulled-back Hessian
vanishes on the full upstairs interior.  Its exact statement/proof SHA-256
values are
`27ff3ad7a6174b8b38d5890d8c891681edf416f02e2538017db22edf372c1ed8` /
`15ff9b3a28b63c1e3f37c104f27e30e77431f389ec694a1d3f3823232ef1f125`.
An independent exact-byte hostile re-audit passed.  Dependency-closed
production Rethlas using `gpt-5.6-sol` at `xhigh` returned final `correct`,
zero critical errors, and zero gaps.  The archived request/response/header
SHA-256 values are
`bb90f025d3e6fb616918a364a9f1b014968a58164ff142557ec8188a45b40759` /
`839c5b3f0506f9789f2f14d5eaff8afc0c2bd20b17ba11bf7400b3a5e0a7582a` /
`3f31d65b71c13800f8486cf689d9fb508fa35c7b44e0b94084292abffd0dad66`.
No automatic ascent of an arbitrary continuous current is asserted.

A separate exact recovery endpoint is now recorded as
`prop:ch15-pointwise-pluriharmonic-closure`: on any analytic space, a
continuous pointwise limit of a sequence of classically pluriharmonic
functions is classically pluriharmonic, with locally uniform convergence.
It is the direct content of Gubler--Rabinoff Theorem 7.6, not a new
regularization theorem.  In particular, it supplies the final step once a
future P06.2 argument produces a pointwise curve-test approximation, but
the zero-current equation itself produces no such sequence and the criterion
does not give ordinary CLD-smooth harmonic approximants.  The atom count is
unchanged.

P06.2 remains one active T2 atom only for arbitrary analytic germs,
nonproduct local domains, equations known merely on the coordinatewise
strict radial core, and the classification of boundary-control hypotheses
weaker than scalar stability.  Higher-dimensional standard strict product
endpoints, the scalar-stable arbitrary-radius products, and the algebraic-split
scalar-stable invariant-toric range, including its analytic-local
algebraic-split analytic-form version, together with scalar-stable proper
smooth curve-bundle descent over arbitrary complete nontrivially valued
fields, are removed from the residual; the
unrestricted arbitrary-radius version is disproved.  The
strict-open-disc descent proposition `prop:p062-open-disc-descent` also
shows that a continuous zero-current function on
\(B\times_KD_R^-\) is pulled back from a unique continuous zero-current
function on the good, topologically separated, pure strict base \(B\).
Iterating it over the published Wanner curve scope gives
`cor:p062-open-disc-products-over-curves`: all zero-current functions on a
finite product of that curve domain with standard strict open discs are
classically pluriharmonic, locally real-PL, and GJR harmonic.  The proof
descends the equation by a normalized compactly supported disc top form,
rather than by an invalid current pullback along the zero section.  The
finite-polyannulus product theorem
`thm:p062-open-polyannulus-products-over-curves` writes every zero-current
function on \(W\times_K\prod_{i=1}^s A^-_{r_i,R_i}\) uniquely as
\(p^*b+\sum_i(a_i\circ p)q_i^*\log|T_i|\), with \(b\) a zero-current curve
function and every \(a_i\) locally constant.  Exact fibre slicing and radial
averages give the zero-current coefficients; a mixed compact test gives the
slope coefficient zero first current, and an induction through lower
polyannulus products makes it locally constant.  Thus this strict product is
classically pluriharmonic, locally real-PL, and GJR harmonic.  The \(s=1\)
case is `thm:p062-open-annulus-products-over-curves`.  Its displayed
coefficient formula needs globally coordinated annular coordinates, but
`cor:p062-open-polyannulus-bundles-over-curves` globalizes the regularity
conclusion to every analytically locally trivial finite standard strict
open-polyannulus bundle over \(W\): it applies the product theorem in each
analytic product chart and requires no global coordinate or coefficient
compatibility.  The overlap defect is now intrinsic rather than unspecified:
`prop:p062-polyannulus-bundle-slope-local-system` writes every logarithmic
coordinate change as a locally constant unimodular integer matrix plus a
vector of zero-current base functions.  These transformations satisfy the
affine Cech cocycle law, define a rank-\(s\) local system of lattices, and
make the local slope vectors of every zero-current function a global
parallel section of the dual real local system.  The proposition does not
trivialize the lattice system or give global annular coordinates.  The
translation cocycle now defines the canonical zero-current radiance class
`rho_0(pi)` in twisted Cech degree one.  Proposition
`prop:p062-polyannulus-radiance-obstruction` proves that this class vanishes
exactly when zero-current affine gauges remove all translations after a
refinement; then every zero-current function has one global base coefficient
and a pairing of its parallel slope with the global continuous logarithmic-
radius section of the associated flat vector bundle.  These gauges are not
claimed to be logarithms of analytic units, so the criterion does not give
global analytic annular coordinates.  The sharper statement
`prop:p062-polyannulus-slope-exact-sequence` requires no total vanishing:
the slopes realized by global zero-current functions are exactly the kernel
of scalar contraction with `rho_0(pi)`.  It gives a natural exact sequence
from curve zero-current functions through total-space zero-current
functions and parallel slopes to scalar Cech degree one.  If the contraction
is injective---in particular, if there are no parallel dual sections---all
zero-current functions descend uniquely to the curve; if `rho_0(pi)=0`, a
chosen zero-current affine gauge splits the sequence.  For the
globally coordinated product, the same coefficient
formula persists through every finite tower of locally trivial standard
strict open-polydisc bundles by
`cor:p062-polyannulus-base-open-polydisc-towers`.  Separately,
`cor:p062-open-polyannulus-bundle-open-polydisc-towers` supplies classical
pluriharmonicity, local real-PL regularity, and GJR harmonicity for every
such tower over a locally trivial polyannulus bundle.  Annular fibrations
lacking these analytic product charts and arbitrary nonproduct germs remain
outside the proved scope.  The common transfer mechanism is now isolated in
`prop:p062-mixed-exact-bundle-tower-transfer`: unique zero-current descent,
classical-pluriharmonic transfer, real-harmonic transfer, and first-current
rigidity pass through any finite interleaving of the four exact bundle
types.  Hence `cor:p062-polyannulus-base-mixed-bundle-towers` preserves the
same unique coefficient formula when the globally coordinated product is
the bottom of an arbitrary such mixed tower.  The locally twisted
polyannulus and mixed polycylinder bottoms retain all three regularity
conclusions by
`cor:p062-open-polyannulus-bundle-mixed-bundle-towers` and
`cor:p062-mixed-open-polycylinder-bundle-mixed-bundle-towers`, without a
global coefficient formula.  These results still require the displayed
local annular charts and do not insert an annular stage at an arbitrary
later level of the tower.
Conversely, cor:p062-open-polyannulus-over-open-polydisc-towers reverses
the order: after a boundaryless finite tower of locally trivial standard
strict open-polydisc bundles over the published curve domain, it treats a
globally coordinated finite strict-open-polyannulus product over the tower
top.  The unique logarithmic formula has its base term and locally constant
slope coefficients on that tower top, and yields classical
pluriharmonicity, local real-PL regularity, and GJR harmonicity.  It does
not jointly trivialize the disc tower over the curve.
There is also a globally coordinated mixed strict-open-polycylinder product
range: `cor:p062-open-polycylinder-products-over-curves` first descends all
disc factors and gives the unique logarithmic coefficient formula over the
published curve, with classical pluriharmonic, real-PL, and GJR harmonic
conclusions.  More generally, if every analytic trivializing chart has both
at least one standard strict open-annulus factor and at least one standard
strict open-disc factor, then
`cor:p062-mixed-open-polycylinder-bundles-over-curves` gives the same three
regularity conclusions on the total space.  Its finite towers of locally
trivial standard strict open-polydisc bundles are covered by
`cor:p062-mixed-open-polycylinder-bundle-open-polydisc-towers`, but the
nontrivial tower conclusion has the same three local regularity outcomes.
The locally trivial mixed result asserts no global logarithmic coefficient
formula, and none of these results treat fibrations without the stated
analytic product charts.
The local product theorem globalizes by
`prop:p062-open-polydisc-bundle-descent`: on every locally trivial standard
strict open-polydisc bundle over a good separated strict pure-dimensional base,
a continuous zero-current function uniquely descends to a zero-current
function on the base.  In the published curve scope,
`cor:p062-open-polydisc-bundles-over-curves` then makes it classically
pluriharmonic, real-PL, and GJR harmonic, without a global section or product
decomposition.  This does not cover nontrivial annular fibres, disc
fibrations without the stated local product charts, arbitrary nonproduct
germs, or strict-core-only equations.  For a
positive-dimensional standard strict endpoint-polycylinder base,
`prop:p062-open-polydisc-bundle-endpoint-base` further identifies the descended
function with the affine combination of the base annular logarithms and
makes the total-space function classically pluriharmonic, real-PL, and GJR
harmonic.  The local finite-curve-product presentation propagates through
every displayed finite open-polydisc-bundle tower: over the published curve,
the curve-polyannulus and mixed curve-polycylinder bases, and the standard
strict endpoint-polycylinder base, the corresponding tower results therefore
have the same classical-pluriharmonic, real-PL, and GJR-harmonic conclusions.
They require every displayed local product chart and do not cover annular
fibres, fibrations without those charts, arbitrary nonproduct germs, or
strict-core-only equations.  The atom count, tier count, and queue position
are unchanged.
There is also a verified proper-fibre bundle consequence.  On a locally
trivial projective-space bundle over a published curve,
`prop:p062-projective-bundle-descent` exhausts every relative standard affine
chart by strict open polydiscs, applies the existing open-disc descent on
each such chart, and identifies the descended functions through the common
projective point \([1:\cdots:1]\).  The statement explicitly requires the
base to be locally holomorphically separated and paracompact, so its local
zero-current identities glue by `prop:ch14-currents-sheaf`.
`cor:p062-projective-bundles-over-curves` consequently gives classical
pluriharmonicity, real-PL regularity, and GJR harmonicity in this range.  It
is a proper-fibre globalization of the strict-disc result, not a conclusion
for arbitrary nonproduct germs or arbitrary fibrations; the atom count, tier
count, and queue position remain unchanged.
The same common-point mechanism gives a strictly larger verified
proper-fibre range.  If the fibre is the analytification of a
positive-dimensional smooth proper split toric variety,
`prop:p062-smooth-proper-split-toric-bundle-descent` exhausts each affine
space attached to a maximal cone of the complete regular fan by strict open
polydiscs.  The identity of the dense split torus lies in every such
exhaustion, so the local descended functions agree without any invariance
hypothesis.  The base must again be locally holomorphically separated and
paracompact for current gluing.  Consequently,
`cor:p062-smooth-proper-split-toric-bundles-over-curves` gives classical
pluriharmonicity, real-PL regularity, and GJR harmonicity over a published
curve.  This subsumes the projective-space fibre but does not cover singular,
nonsplit, or nonproper toric fibres, arbitrary fibrations, or arbitrary
nonproduct germs; the atom count, tier count, and queue position remain
unchanged.
There is another verified proper-fibre range.  For a locally trivial bundle
whose fibre is the analytification of a geometrically connected smooth proper
algebraic curve, `prop:p062-proper-smooth-curve-bundle-descent` uses exact
fibre slicing only over \(K\)-rational rigid base points.  The base field is
algebraically closed, so those fibres remain over \(K\); Wanner comparison
and the compact maximum principle make their restrictions constant.  Rigid
points are dense in the entire local product, which extends the resulting
function identity without scalar extension of a current, and a normalized
fibre top form descends the current equation.  Consequently,
`cor:p062-proper-smooth-curve-bundles-over-curves` gives classical
pluriharmonicity, real-PL regularity, and GJR harmonicity over a published
curve.  This does not assert the result for arbitrary proper or nonproper
curve fibres, arbitrary fibrations, or arbitrary nonproduct germs; the atom
count, tier count, and queue position remain unchanged.
Over an arbitrary complete nontrivially valued field,
`prop:p062-scalar-stable-proper-curve-bundle-descent` now gives the exact
replacement under a fibrewise scalar-stability hypothesis at every rigid
base point.  Wanner comparison after completed algebraic closure makes the
rigid fibre restrictions constant.  A closed point of the fibre curve gives
a finite faithfully flat multisection; equalizer descent and rigid-point
density replace the unavailable rational section, and a normalized top form
on the fixed fibre descends the current identities.  The proposition makes
no automatic current-ascent claim.  Its exact statement/proof SHA-256 values
are `cce5a5ff689f110e02564ee155b75027c3eec06d0e484af8e86dba0662fe9564` /
`b371852f0f87b4a1b382d6f67d792d8b34ba5299ee43e40323b01f7df8ede2d5`.
The repaired standalone packet passed local `gpt-6-astra`/`xhigh`
verification as item `pi_3cceee63c457c144abd9869c`, final `correct`, with
zero critical errors and zero gaps.  The rejected first packet is retained
because it exposed and records the false separability claim repaired in the
accepted version.  The atom count, tier count, and queue position remain
unchanged.
The four exact bundle descents may also be iterated together.
`thm:p062-mixed-bundle-towers-over-curves` allows every stage of a finite
tower over a published curve to be a locally trivial standard strict
open-polydisc bundle, a projective-space bundle, a smooth proper split-toric
bundle, or a proper smooth connected curve bundle, in arbitrary order.
Successive unique descent gives a
zero-current function on the curve; curve comparison and harmonic pullback
make the original function classically pluriharmonic, real-PL, and GJR
harmonic.  Projective-space, split-toric, and proper-curve stages retain the
exact locally holomorphically separated and paracompact base hypotheses of
their source propositions.  Annular fibres, arbitrary fibrations, and
nonproduct germs
without the displayed local trivializations remain outside this range; the
atom count, tier count, and queue position remain unchanged.
If the top of such a mixed tower is boundaryless, then
`cor:p062-open-polyannulus-over-mixed-bundle-towers` also treats its product
with finitely many globally coordinated standard strict open annuli.  The
unique zero-current base coefficient and locally constant annular slope
coefficients all descend to the original curve, and the total function is
classically pluriharmonic, real-PL, and GJR harmonic.  This does not cover
locally twisted annulus bundles at the top or annular stages inside the
tower.  Together with the preceding annular-bottom mixed-tower results, it
allows annular coordinates on either side of the four exact stage types,
and `thm:p062-interleaved-polyannulus-mixed-bundle-towers` now allows the
globally coordinated annular product stages to occur at arbitrary levels.
Its unique normal form contains every annular coordinate introduced in the
tower, while the base coefficient and all locally constant slope
coefficients live on the original curve.  That normal-form statement does
not trivialize locally twisted annular coordinate changes.  Their
single-bundle coefficient monodromy is nevertheless encoded by
`prop:p062-polyannulus-bundle-slope-local-system` as the integral lattice
local system and real affine cocycle described above.  Its zero-current
radiance class is the exact obstruction to removing the translations by
zero-current affine gauge and hence to the resulting global metric
coefficient formula; it is not an analytic-coordinate obstruction theorem.
Before total vanishing, its contraction with a parallel slope is the exact
obstruction to realizing that slope in a global zero-current function, by
`prop:p062-polyannulus-slope-exact-sequence`.  Thus the coefficient system
is now classified slope by slope, and an injective contraction forces every
zero-current function to descend to the curve.
For regularity without a global coefficient formula,
`cor:p062-curve-local-annular-mixed-bundle-towers` now permits those annular
coordinates, radii, and product trivializations to vary across one analytic
open cover of the original curve.  On each member of that cover the whole
restricted tower satisfies the globally coordinated interleaved theorem, so
classical pluriharmonicity, real-PL regularity, and GJR harmonicity glue
without any overlap compatibility of the coefficient systems.  Annular
charts existing only over arbitrary opens of intermediate tower levels
remain outside the result, since those opens need not retain the preceding
tower or its paracompactness hypotheses.  The atom count, tier count, and
queue position remain unchanged.
The former literal request for ordinary CLD-smooth harmonic approximants is
disproved by exact-live production run `20260825T055907Z_b5c8f0719b60`;
positive-curvature psh approximants are not covered by that obstruction.
The former P06.3 is now retired positively:
`thm:p063-current-psh-ordinary-regularization` proves on every smooth proper
algebraic curve over an algebraically closed complete nontrivially valued
field that current positivity, Thuillier subharmonicity, and local membership
in the first ordinary CLD-smooth decreasing-limit stage agree for continuous
functions.  The exact frozen statement and proof passed production run
`20260827T090645Z_767cbf81c723`, final `correct`, with zero critical errors
and zero gaps.  Their SHA-256 digests are respectively
`767cbf81c723279c1218df4136f8e299465240b325f41f6b0663d001fb5d8a68`
and
`d1db3c2db861d920598697fdad5d002a2b1ce947dbdbd95ad9b78b8f9f312bd8`.
The direct endpoint assigned no item identifier.  P06.1 and P06.2 retain
the residual scopes stated above.

### `prob:frontier-cld-hierarchy` --- 1 active atom

- **P07.1** `[T2; open after the tropical-toric, finite ambient-star,
  finite ambient-star × open-convex-Euclidean and × convex-polyhedral
  joint-convex-generator, Stone × finite-star × convex-polyhedral
  joint-convex-generator, Stone × exact CLD infinite-star, exact CLD
  infinite-star × open-convex-Euclidean and × convex-polyhedral, Stone ×
  exact CLD infinite-star × convex-polyhedral, and Stone × exact CLD
  infinite-star × arbitrary-open-Euclidean joint-convex-generator, Stone ×
  exact CLD infinite-star × generator-convex arbitrary-incidence
  polyhedral-complex, two
  nonambient interval, exact CLD infinite-star, Stone--Euclidean,
  Stone--polyhedral, and generator-convex arbitrary-incidence
  polyhedral-complex cases]`
  Decide whether the CLD psh hierarchy collapses after its first
  decreasing-limit stage.

Eventual cardinal stabilization is known.  Production run
`20260825T024707Z_d1b8d7eaf79e` controls the tropical toric case and the
historical narrower finite-curve statement.  The latter is superseded by the
exact finite ambient-induced real-affine-star theorem archived under
`20260827T103835Z_c8131b22d800`; the direct endpoint assigned no run or item
identifier and returned final `correct`, with zero critical errors and zero
gaps.

The finite ambient-star result now also has a genuine Euclidean product
extension.  For a finite ambient real-affine star $S$ and an open convex
Euclidean domain $\Omega$, if the ambient stage-zero generators on
$S\times\Omega$ are jointly convex in all variables, then
`thm:p071-finite-star-euclidean-collapse` identifies the first-stage, full,
and explicit extended-real comparison sheaves.  The comparison condition is
the product junction Jensen inequality only for tuples whose joining segments
remain in the open set, and every germ has a decreasing smooth approximation
on one fixed smaller product neighbourhood.  A compact-core partial Legendre
transform, finite dual sampling, finite-star smoothing, and regularized
maxima preserve the mixed Hessian positivity; direct radial chords do not.
This book-local theorem does not apply to separately convex generators,
nonambient or calibrated product stars, or branched/nonconvex chamber
gluings.  It narrows P07.1 but does not retire it.

The same finite ambient-star model now also permits one nonempty convex
polyhedron \(P\), including every face and corner and allowing \(P\) to be
unbounded or zero-dimensional.  Under the same joint ambient convexity
hypothesis, `thm:p071-finite-star-polyhedral-collapse` identifies the
first-stage, full, and explicit extended-real comparison sheaves, and gives
one decreasing smooth approximation on a fixed smaller product
neighbourhood.  The new boundary step is a junction-convex envelope on a
compact polytope core: it is needed because ordinary Legendre biconjugation
can lose an upper boundary value of finite convex data.  Partial Legendre
smoothing, finite dual sampling, finite-star smoothing, regularized maxima,
and summable tail constants then preserve the full mixed Hessian condition.
This book-local result does not extend to arbitrary compact convex factors,
separately convex generators, nonambient product stars, or nonconvex or
branched chamber gluings.  It narrows P07.1 but does not retire it.

The locally constant Stone parameter and the finite-star--polyhedral model
may now occur simultaneously.  For
\(X=Z\times S\times P\), where \(Z\) is any locally compact Hausdorff
clopen-base space with only locally constant affine functions, \(S\) is a
finite ambient real-affine star, and \(P\) is one convex polyhedron,
`thm:p071-stone-finite-star-polyhedral-collapse` identifies the first-stage,
full generated, and Stone-factorized fibrewise comparison sheaves.  Every
germ has one decreasing smooth approximation on a fixed smaller product
neighbourhood.  The proof combines the star--polytope junction-convex
envelope with finite clopen discretizations of a compact metrizable quotient;
the envelope is nonexpanding in the uniform norm, so the two mechanisms
preserve exact monotonicity after a summable tail correction.  This permits
nonmetrizability, finite branching, nonconstant polyhedral affine
directions, and faces or corners simultaneously.  It does not permit
nonconstant affine functions on the Stone factor, infinite non-CLD stars,
separately convex generators, nonambient branch structures, or nonconvex
chamber gluings.  P07.1 remains active, and the atom and tier counts do not
change.  The exact statement/proof SHA-256 values are
`4e73599647ca6d3181503d35d103750158b974a59ca9a003076b3ff633692d43` /
`512578208462782ba27699d078b90d4b12cf47edf683947ee2276cb40703d268`.
Model-backed verification run `20260913T013351Z_8e2841681a9a`, using
`gpt-6-astra` at `xhigh`, returned final `correct` after 25 ordered checks,
with zero critical errors and zero gaps.  The archived request/response
SHA-256 values are
`0d8331cede6a9aac67c13153fa14d54167f849d2192ea529369bf712e73fdee1` /
`cfdd311cbbfe052e3791bcd00b63fdc44cdb5d78bf7b95879f457c944e6608fc`.

The Stone parameter may now also be combined with the exact CLD star
\(X_B\) for an arbitrary nonempty branch set \(B\).  Theorem
thm:p071-stone-infinite-star-collapse identifies the first-stage, full
generated, and explicit Stone-factorized comparison sheaves on
\(Z\times X_B\).  At a node the family has one common countable set of
active full branches.  The proof extracts this set and a common compact
metrizable Stone quotient, proves that compact parameter maxima preserve
the exact full-endpoint trace and the finite-point Jensen balance, truncates
to finitely many active branches, and applies the exact-star slope budget
and finite harmonic smoothing.  Every germ is approximated on one fixed
product neighbourhood.  The result excludes nonconstant affine directions
on the Stone factor, non-CLD infinite stars, an additional active
polyhedral factor, and nonambient branch structures.  P07.1 therefore
remains active, with unchanged atom and tier counts.  The exact
statement/proof SHA-256 values are
9f42a4c909f1aae06db633550a71b8fddffe08db87150864d29f7a9de0673d29 /
68b480c7e063d7ebaea1c3af370020cded38dc3cfa076cbc41b5d4db446172cf.
Dependency-closed local verification with gpt-6-astra at xhigh returned
final correct, zero critical errors, and zero gaps.  The final archived
request/response SHA-256 values are
52edf497268a0bf7e4f6151535b1b3dcd2255a3a1ca511328b89ad028ef9d955 /
10ee898d364bd93999884f9b63018b62b65e62283e542cb38e0a24c842cfa321.

The exact CLD star may now also be combined with a nonempty open convex
Euclidean domain.  For every nonempty branch set \(B\) and
\(\Omega\subset\mathbf R^d\), theorem
`thm:p071-infinite-star-euclidean-collapse` identifies the first-stage,
full generated, and explicit product-comparison sheaves on
\(X_B\times\Omega\) under joint branch--Euclidean convexity.  The comparison
condition consists of exact endpoint trace, one countable activity set, and
the reciprocal-distance junction Jensen inequality with its Euclidean
barycentre constraint.  Partial Legendre transformation, finite dual
sampling, finite branch truncation, exact-star smoothing, and a summable
tail produce one decreasing smooth-psh approximation on a fixed smaller
product neighbourhood while retaining mixed Hessian terms.  The theorem
does not cover a simultaneous Stone parameter, polyhedral faces or corners,
separately convex generators, non-CLD infinite stars, or nonambient branch
structures.  P07.1 remains active, with unchanged atom and tier counts.  The
exact statement/proof SHA-256 values are
`8b9c6605c4016b4c69e489e5165d214360a8d5d3a34bf08b8f96419acde97e15` /
`452530d86fbc979d2e6f95e2c8a489a24fa87a2ba466477933455cd68cea3d94`.
Dependency-closed local verification with `gpt-6-astra` at `xhigh` returned
final `correct`, zero critical errors, and zero gaps.  The archived
request/response/header SHA-256 values are
`af8696b3af1527198e85a7559b592a310883a6911253225f8728aa3739cdbee8` /
`e94df5b40ac7d3ae4f771fb708637466a38ba1898b30a712a85328fb26d7a8d7` /
`794ea8f4c4fa06fb9f3a8a509cbbeb1020577224a26f327028dc45bfd45e5ff7`.

The exact CLD star may now also be combined with one nonempty convex
polyhedron.  For every nonempty branch set \(B\), theorem
`thm:p071-infinite-star-polyhedral-collapse` identifies the first-stage,
full generated, and exact product-comparison sheaves on \(X_B\times P\)
under joint ambient convexity in the branch and polyhedral variables.  All
faces and corners are included, and every germ has a decreasing smooth-psh
approximation on one fixed smaller product neighbourhood.  The proof uses a
compact-core exact comparison envelope, finite-moment insertion, countable
branch reduction, partial Legendre sampling, finite-star smoothing, and a
summable-tail correction.  It does not cover separately convex generators,
nonconstant affine directions on a Stone parameter, non-CLD infinite stars,
nonambient branch structures, or nonconvex or branched chamber gluings.
P07.1 therefore remains active, with unchanged atom and tier counts.  The
exact statement/proof SHA-256 values are
`9b3e2c4163f30ad26f606a06d591a064f57994b56aa7910eb012093777f3c1a1` /
`0cc78aa605311e6709cbf33b0580c946b5b50cef610ffff28eb5fb7c1aae6d20`.
Dependency-closed V2 verification with `gpt-6-astra` at `xhigh` returned
final `correct`, zero critical errors, and zero gaps.  The archived
request/response/header SHA-256 values are
`55b1ef2a48f52008cac7820cf81a0ac931e9688d504c311adf767b56dbb4475f` /
`4e43d68634260430b157e261e485a133b50ca3517ddde2d8dbffd74d9c5c1da3` /
`b2ea5d5f52042d3197d3358bf8460698df26d0d9e92842a8b9c31ed9531f93d9`.

All three factors may now occur simultaneously.  For any locally compact
Hausdorff clopen-base space $Z$ carrying only locally constant affine
functions, any nonempty exact CLD branch set $B$, and any nonempty convex
polyhedron $P$,
`thm:p071-stone-infinite-star-polyhedral-collapse` identifies the
first-stage, full generated, and Stone-factorized fibrewise comparison
sheaves on $Z\times X_B\times P$.  Sequential generation forces one
countable activity set common to the Stone family.  On that metrizable
branch reduction, the exact star--polyhedral comparison envelope is
nonexpanding, so finite clopen discretization, the uniform one-step
smoothing estimate, and a summable tail give one decreasing generator
sequence on a fixed smaller product neighbourhood.  This permits a
nonmetrizable Stone factor, arbitrary exact CLD valence, and all affine
directions, faces, and corners of one convex polyhedron simultaneously.  It
does not cover nonconstant affine directions on the Stone factor, non-CLD
or nonambient infinite stars, separately convex generators, or nonconvex or
branched chamber gluings.  P07.1 remains active, with unchanged atom and
tier counts.

The same three-factor theorem already contains the missing open-Euclidean
combination.  The whole affine space $\mathbf R^d$ is a convex polyhedron,
and the theorem identifies sheaves, so restriction to any nonempty ordinary
open $\Omega\subset\mathbf R^d$ gives
`cor:p071-stone-infinite-star-euclidean-collapse` on
$Z\times X_B\times\Omega$.  Every germ has a decreasing generator sequence
on one fixed smaller product neighbourhood, and at a node one countable set
of active full branches is common to the compact Stone family and the
Euclidean variable.  When $\Omega$ is convex, these are exactly the joint
branch--Euclidean generator and comparison germs of the independent
exact-star--Euclidean theorem.  This corrects the earlier scope ledger but
still excludes nonconstant Stone-affine directions, non-CLD or nonambient
infinite stars, separately convex generators, and nonconvex or branched
chamber gluings.  P07.1 and the active count therefore remain unchanged.

The three-factor sheaf identity also transports through every local
two-sided generator-preserving convex development.  Let $\Sigma$ be a
possibly infinite Hausdorff face-to-face polyhedral complex, not assumed
locally finite, whose complete generator germ at each point is identified in
both directions with the single-chamber generator sheaf on a relatively open
convex subset of one polyhedron.  Then
`cor:p071-stone-infinite-star-generator-convex-collapse` identifies the
first-stage, full generated, and chartwise comparison sheaves on
$Z\times X_B\times|\Sigma|$.  Every germ has a fixed-neighbourhood
decreasing generator sequence.  At a node, one countable active-branch set
works simultaneously for the compact Stone family and the developed
polyhedral variable.  The proof is germwise and uses no finite subdivision,
so arbitrary incidence, infinitely many cells through every neighbourhood,
and global chamber monodromy are allowed.  It does not produce a convex
development for branched or singular lower links and does not cover
nonconstant Stone-affine directions, non-CLD or nonambient stars, or
separately convex generators.  P07.1 and the atom and tier counts remain
unchanged.  The exact statement/proof SHA-256 values are
`fceb1f33684cd431298d020b0be3649a4ef1f96d0f06719562660ab9fcbb7615` /
`9a693cc3d087557132a23584817de1dc8018ce35c8e101948c548a5f87996513`.
Dependency-closed local verification with `gpt-6-astra` at `xhigh` returned
final `correct`, zero critical errors, and zero gaps.  The checked item is
`pi_289ea5bf00583ce43371f809`; the request/response/header SHA-256 values
are
`ac6d606c41cd9c1945dff1486e7e366108406db4c8968752cd1903a1d06e3d83` /
`2ca78da177806f66dc9d79f91891f68640d68c604a5f17c2ab26bb7a696c34df` /
`a05e697bb3131b6d2db9d32d1b2da1e27750ec4e5638fda78a7052e06f44e738`.

Two additional nonambient interval models are now controlled.  For the
finite constant-collar endpoint, the comparison sheaf is the extended-real
convex functions satisfying the boundary-minimum condition.  Its exact
statement and proof, SHA-256
`69f04be69f70be0abfdb720fa6aceaad799240421046d14333cfd542e2e56498`
and
`5e7d96e8badf030b64d063b26fb353aa4be097438ae267cdd72911907c2a5c7c`,
passed production run `20260829T002250Z_69f04be69f70`, final `correct`, with
zero critical errors and zero gaps.  For the constant-collar endpoint at
`-infinity`, the comparison condition is instead the exact finite-side trace
at the endpoint.  Its exact statement and proof, SHA-256
`779b1304255d6e803cf34d9e429acb085eb5cf827e54c6a30a15ba3058182d9a`
and
`dacaa96b68c5ddb260736d40075d229ffbe843dbe4994436c1a18428aa407f5b`,
passed production run `20260829T003722Z_779b1304255d`, again final `correct`,
with zero critical errors and zero gaps.

On 30 August 2026, the exact CLD star \(X_B\) of CLD Section 6.7.3 also
became controlled for every nonempty branch set \(B\), including infinite
\(B\).  Its first-stage,
full generated, and explicit comparison psh sheaves coincide, and every germ
admits a pointwise decreasing smooth psh approximation on one fixed
neighbourhood.  The exact statement and proof have SHA-256
`99c1a6a6a712005e73ee3b7cdae297606895b22ce79c80a6411dfd7f4863c963`
and
`ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090`.
Production item `pi_00f6c73303087d94da9eb724`, using `gpt-5.6-sol` at
`xhigh`, returned final `correct`, zero critical errors, and zero gaps; the
response SHA-256 is
`b271d51ed81898ccfe68a798b3fc69e165c0c72486ff6c59711995f5b9e581af`.

The exact product of a locally compact Hausdorff clopen-base space $Z$,
carrying only locally constant affine functions, with an arbitrary open
convex Euclidean domain is also controlled.  The first-stage and full CLD
psh sheaves coincide, every germ has a fixed-neighbourhood decreasing smooth
psh approximation, and every germ factors through a compact metrizable
zero-dimensional quotient of a compact clopen neighbourhood in $Z$.  This
includes nonmetrizable Cantor
cubes.  The frozen statement/proof SHA-256 hashes are
`dfd8c7cc9d6d26f50260707975ff62d4f292627f084400bcd37b32253c876cdc` /
`9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6`.
The source-aware production endpoint, using `gpt-5.6-sol` at `xhigh`,
returned final `correct`, zero critical errors, and zero gaps; it assigned
no run or item identifier.  The archived request/response SHA-256 hashes are
`ac70562c588dbf8f22925086bc85dc327585f026809563a71c79feb29787ca23` /
`ef9be00d4ed1462f11068a2b99a2c7fbe366af2b3bd180850b6763db541c3d6a`.
This result does not cover nonconstant affine directions in $Z$ or general
polyhedral face gluings, so it narrows but does not retire P07.1; the
uniform-ordinal atom is handled separately below.

The same conclusion is now verified when the second factor is one nonempty
convex polyhedron \(P\), possibly unbounded, lower-dimensional, or
zero-dimensional, with its induced affine tropical structure. All faces
and corners are included. Fibrewise convexification on compact polytope
cores, smooth convex majorants, finite clopen partitions, and summable tail
corrections produce the fixed-neighbourhood decreasing smooth-psh sequence.
The exact statement/proof SHA-256 hashes are
b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002 /
37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb.
After independent exact-byte and exact-source audits, dependency-closed
production Rethlas using gpt-5.6-sol at xhigh returned final correct, zero
critical errors, and zero gaps. The request/response SHA-256 hashes are
6697bc79ad50c8b7a9cf3c63dc63fd5b08a9930f9369b304595254f635573d11 /
c5871408ef86be152ecd6e169eaae05f590feef00e5487d37f185780951d5285.
The theorem does not glue nonconvex or branched chamber systems and does not
permit nonconstant affine directions on the Stone factor. P07.1 therefore
remains one active atom.

The chartwise consequence is now also verified for every finite Hausdorff
face-to-face polyhedral complex whose complete smooth-psh generator germ is
locally, and in both directions, identified with the single-chamber
generator sheaf on a relatively open convex subset of one polyhedron.  On
the product with any locally compact Hausdorff clopen-base parameter, the
first-stage, full generated, and chartwise comparison sheaves coincide, and
every germ has a fixed-neighbourhood decreasing smooth-psh approximation
crossing all chart faces.  The exact principal statement/proof SHA-256
hashes are
`2bc8574fecdc46ecafc1e41f24608c6db60cb9e48f696204ef503a83bed0625e` /
`ab3348d8d0dc31c4c661e1358f8b70894eff83890a3c6d6abc412810dea4ca30`.
The independent exact-byte hostile reaudit passed.  A dependency-closed
production Rethlas request using `gpt-5.6-sol` at `xhigh` returned final
`correct`, zero critical errors, and zero gaps.  The materialized
statement/proof and request/response/header SHA-256 hashes are
`e163679c6f1140eb3452e9f052f89f8895b7b1d300e081f6149feec099d47ac7` /
`1505aa473b3092f80d26bde3e8e947c709b138992370599645948ed510e39400` /
`dd51939097d53f3c1b195388d6312c6b2c5fc15816e88e444b3e5d8ca0dd4985` /
`8bab39fea7dd28f75309d021731f23de1386f1801c6a8ae8362452b237b0106f` /
`35f9ddd2168e155c0351c56b4bcae5b3b0d28a4922703d59413aa194280dea57`.
The arbitrary-incidence extension
`cor:p071-locally-finite-generator-convex-collapse` is a formal local
consequence of the single-chamber theorem: its proof uses only one
generator-preserving convex chart and no finite local subdivision.  It
therefore retains the fixed-neighbourhood decreasing smooth approximation at
every germ even when infinitely many cells meet every neighbourhood, but
asserts no global sequence.  The verified two-ray example shows that
face-to-face topological unbranching plus independent cellwise positivity is
insufficient: the ambient affine generator `-x-y` unfolds to the nonconvex
function `-|t|`.  Consequently the extension does not cover branched links,
singular lower links, or generator germs without a generator-preserving
convex development.  P07.1 remains one active T2 atom, and the active count
and tier counts are unchanged.

The general cross-row order obstruction is also eliminated conditionally by
`prop:p071-fixed-core-flattening`: if every row approximation is defined on
a neighbourhood of one common compact core, a finite-square diagonal and
summable tail constants yield a single decreasing smooth-psh approximation
on the fixed interior.  Its exact statement/proof SHA-256 are
`b29ccabac98982c239fcedcc34a701c9a9bb98ca95710d6ed7fbaa3f0f96e4d9` /
`7677ba46620cc4cef8a74d502cdf9fde344e045b04bbc66a4274a5c20b1838c2`.
Production run `20260829T234341Z_b29ccabac989`, using
`gpt-5.6-sol` at `xhigh`, returned final `correct`, zero critical errors and
zero gaps.

**Retired P07.2 (positive).**  For every CLD affine $G$-tropical space,
the full generated psh and continuous psh sheaves occur by the first
uncountable stage:

```text
Psh_{X,\omega_1} = Psh_X,
CPsh_{X,\omega_1} = CPsh_X.
```

The compact-core proof correctly treats the limit stage as a
sheaf-theoretic local union and uses that a countable supremum of countable
row ranks is still below $\omega_1$.  The frozen statement/proof SHA-256
hashes are
`37ca59d5bd863e6af4d46ed18d1cf1c4cfcdb45aeeac1f25631fa582750985f8` /
`9cb9222dbd307d4ff21c0043951a5c0b4a65dec645012fe5e5584b86808a6b5b`.
After an independent exact-byte re-audit, dependency-closed production
Rethlas using `gpt-5.6-sol` at `xhigh` returned final `correct`, zero
critical errors, and zero gaps.  The request/response/header SHA-256 hashes
are
`befa29ce409a5b20bf3d40acd1adf20c99a599ecab7c3d886b29327676950f11` /
`d40c473aad890ff6361e637af8219e5f8ed3c09fc6c8beacd77e94e49780fec3` /
`226053b84fefdb73d19c1ae547c54425604190f55d4d026f5a9f46ab061d064c`.
This supplies no finite or fixed countable bound and does not retire P07.1.
At this checkpoint the active count drops from 53 to 52 and the tier counts
become `(0,5,13,17,17)`.

P07.1 therefore retains branched or singular-link higher-dimensional
chamber systems without a generator-preserving convex development,
nonconstant affine structures on zero-dimensional parameters, products of
an exact infinite star with active factors outside the verified
single-polyhedron, arbitrary-open-Euclidean, and locally
generator-convex-development models, non-CLD infinite stars, and other
nonambient local models outside the two exact interval structures, \(X_B\),
and the verified locally constant-parameter models.
The residual obstruction is sharpened to the existence of a compatible
local convex development and to fixed-neighbourhood globalization beyond
it, rather than diagonal order.  It remains active.

### `prob:frontier-cld-global-metric` --- 1 active atom

- **P08.1** `[T3; open beyond the verified implications below]` Decide
  whether a continuous locally CLD-psh metric on a projective
  non-Archimedean variety is globally psh in CLD's literal sense: a
  uniform limit of globally defined smooth psh metrics.

**Correction of the comparison scope, 31 August 2026.** The source question
is CLD Remark 17.8.10, first paragraph. Fixed-line-bundle approximation by
nef rational model metrics is a distinct comparison assertion, not the
definition in the source.

The current theorem `thm:p081-corrected-curve-comparison` applies to
smooth proper geometrically connected algebraic curves over every complete
nontrivially valued field. For a continuous locally CLD-psh metric of
positive degree it gives uniform
approximation by relatively ample rational algebraic model metrics and
membership in the uniform Fubini--Study closure. For degree zero the
curvature vanishes, and approximation by nef rational formal metrics holds
if and only if the fixed line bundle has one such metric. It does not
assert that degree zero alone ensures this existence.
Its statement/proof SHA-256 values are
`5158fe6399885289ba2e9bf7a57f7da32a87fdb7b7d6e6b5bc20879e054564b6` /
`99028d9d33abcfe31e42dd6f5e1aedb6c00822c5408ef46da4ef692ed2ef3a17`.
After independent exact-byte review, strict Rethlas 0.2 production run
`20260830T234536Z_5158fe639988`, item `pi_4592d7150e75755585cdfa20`,
using `gpt-5.6-sol` / `xhigh`, returned final `correct`, zero critical
errors and zero gaps. Exact-current request, source, coverage, and adaptive
context reconstruction passed again on 31 August. The response SHA-256 is
`ec419c5259c5aebba62c8349070a89b2cb82b6d127b5a5b9ff5b7a04188700c5`.

The degree-zero hypothesis cannot be dropped:
`thm:p081-irrational-tate-period-obstruction` constructs a Tate-curve
line bundle with a smooth harmonic metric and no nef rational formal metric
on any positive tensor power. Its statement/proof SHA-256 values are
`4d997e024fa7ec642299a0d86ae1d9b9d06c6041f7f10b694369d7faa458d28c` /
`c7a2a08ad4ad82df4470004d01fa131fecdc01ab03f60eefa67bbe7eaa8f0a5a`.
Independent exact-byte review passed; the strict production retry, item
`pi_f2b822c25aa05cfebdd8bcc0`, returned final `correct`, zero critical
errors and zero gaps, with model/effort `gpt-5.6-sol` / `xhigh`.
Its exact-current audit also passed. The response SHA-256 is
`a8d296d20c4ea5496262e30b83509d9f21bdae7fc03a33b48b6de87aab9c0054`.
The smooth harmonic metric is already globally psh in CLD's literal sense.
This is not a counterexample to P08.1 or to ample envelope continuity.

**Invariant complete toric global-smoothing range, 10 September 2026.**
`prop:p081-invariant-projective-toric-global-smoothing` settles the literal
CLD global-psh conclusion for a continuous maximal-compact-torus-invariant
locally CLD-psh metric on any toric line bundle over a split toric
variety with complete fan, in every dimension.  Neither the toric dictionary
nor the global smoothing theorem requires projectivity.  BGJKK Theorem 5.3.11
first identifies the metric with a continuous semipositive toric metric.  Its
concave logarithmic weight differs from the integral support function by a
bounded amount; scaling the concavity inequality therefore shows that the
support function is automatically concave.  BGJKK Corollary 5.4.5 then gives
the global decreasing smooth regularization.  Dini's theorem on the compact
tropical toric variety upgrades the pointwise monotone sequence to a uniform
sequence, and surjective tropicalization transfers that uniform convergence
to the metrics.  This is a literal global smooth psh approximation, rather
than the separate fixed-line-bundle rational-model comparison.  It requires
torus invariance, but no extra concavity or projectivity assumption; it gives
no averaging or smoothing procedure for a noninvariant metric.  P08.1
therefore remains active outside this range, with no change to the atom or
tier counts.

**Supersession.** The old unrestricted degree-zero theorem
`thm:p081-curve-local-global`, its old analytic transfer, and the
alternative factorization proof depending on that theorem are no longer
live proof inputs. Their historical sources and receipts remain preserved;
a previous model verdict cannot validate the missing rationalization step.
Corrected analytic-transfer and factorization packets are awaiting their
own production gates. No pending result is counted as established here.

P08.1 retains the higher-dimensional and singular comparison questions and
all residual scope not covered by the exact displayed implications.
The general nontrivially valued envelope property is not proved by these
curve results. This correction retires no additional atom: the active total
remains 51, with tiers `(0,5,12,17,17)`.

**Retired P08.2 (negative).**  The extension of CLD Corollary 17.8.9 to all
proper strict analytic spaces possessing a formal model with projective
special fibre is false.  On the generic fibre of a very general formal
twistor deformation of a projective complex K3 surface, the analytic Picard
group is zero.  An admissible blow-up of a closed point of the special fibre
produces a nonconstant strictly integral parlinear metric on the trivial
line bundle, while the maximum principle forces every globally dpsh metric
on that bundle to be constant.  The frozen statement/proof SHA-256 hashes
are
`1e9b7c31a70c55f407de07d76c67d6912e61e1673ef81c66c60789afd2202d2f` /
`78fab726abcdfb3086988150359568ccd8a9b29d63c3a94e0c513f14b9fc148c`.
After an independent twelve-obligation audit, dependency-closed production
Rethlas using `gpt-5.6-sol` at `xhigh` returned final `correct`, zero
critical errors, and zero gaps.  The request/response/header SHA-256 hashes
are
`7916d3750482946cd933591a3f836d6e3b308dcbddb8a24a26c836de41d73e1b` /
`f5e780184515b39bbb7d4fd099366da98b96a74896fa1d693b43f66cce19d57e` /
`29d3ae7255f5ee74b5deca5d6cc3c297ec382d97c8d078731eecc273940c1d45`.
The counterexample does not address P08.1.  At this checkpoint the active
count drops from 52 to 51 and the tier counts become `(0,5,12,17,17)`;
the number of formal problem environments remains 14.

### Retired P09 history --- 0 active atoms

P09.2 asked whether, over an algebraically closed, complete,
nontrivially valued field, every cubical metric on every ample symmetric
rigidified line bundle on an abelian variety with non-isotrivial mixed
reduction is an ordinary delta-metric.  It is retired with a negative
answer.  The product--Gauss criterion
`thm:p09p2-product-gauss-candidate` proves more generally that a
nondegenerate quadratic weight `F(h)` on an equivariant locally integral-PL
map is ordinary delta exactly when all coordinates of `h` are CLD-smooth.
Applied to split Raynaud uniformization, an ample cubical metric is ordinary
delta exactly when the residual Raynaud extension is isotrivial.  Thus no
ample cubical metric in non-isotrivial mixed reduction is ordinary delta.
The exact statement and proof passed production run
`20260826T055627Z_b68659fba1be`, item
`pi_75c74fac9a98efc3719b9773`, with `gpt-5.6-sol` at `xhigh`, final
`correct`, zero critical errors, and zero gaps.

P09.1 is retired.  Signed generation holds in every residual dimension by
`thm:p09-signed-semipositive-span`, while
`cor:p09-good-reduction-positive-cone-counterexample` disproves the natural
nonnegative-coefficient formulation in residual dimension two.  Production
runs `20260825T130036Z_c1607c25ec38` and
`20260825T130707Z_4c4a1f2c885f` returned final `correct`, zero critical
errors, and zero gaps.  The formerly bundled unrestricted cohomological
isomorphism question is likewise inactive: the book gives a good-reduction
elliptic-curve counterexample to surjectivity.  This does not settle the
separately restricted totally degenerate case, which is not a formal problem
environment here.

The former displayed P09.2 formulation was the exact residual problem, not a
strengthening.  Under the stated field hypotheses,
`thm:p09p2-reduction` proves that all cubical metrics on a fixed abelian
variety are ordinary delta-metrics if and only if this holds for all ample
symmetric cubical metrics; it also settles every line bundle in
`Pic^0(A)`.  Exact production run
`20260825T145229Z_b37e13478cc7`, item
`pi_10f6228b6e69e780dad8b17b`, returned final `correct`, zero critical
errors, and zero gaps.  Good reduction, total degeneration, and isotrivial
residual Raynaud extensions remain the positive boundary cases.  The later
product--Gauss run above closes the exact residual question, removes its
displayed problem environment, and lowers the active count by one.

### Retired P11 history --- 0 active atoms

- **P11.1** `[retired; disproved]` Weak convergence together with convergence
  of the Boucksom--Jonsson exhaustion does not imply strong convergence on
  all of \(X^{\mathrm{lin}}\).  On \(\mathbf P^n\), every \(n\ge2\), moving
  point-blowup valuations along a linear line converge weakly to its
  line-centred valuation, all exhaustion values equal one, and the strong
  distance stays at least one.  Generalized production run
  `20260825T044839Z_326e2035bbb9`, item
  `pi_9e222887262acc5d9fbc740a`, returned final `correct`, zero critical
  errors and zero gaps; the adapted exact-live theorem and proof passed run
  `20260825T051642Z_049da6197deb`, item
  `pi_062d99c623958fae25885125`, with the same verdict.  The fixed-SNC-complex positive result remains
  valid.  The identifier `P11.1` is retired and will not be reassigned.

### `prob:frontier-singular-local` --- 6 atoms

- **P12.1** `[T4; open after the reduced excellent curve-link
  classification]` Determine the normalizing boundary datum for excellent
  singular and nonnormal germs.
- **P12.2** `[T4; open beyond the book-local ideal-psh completion on
  reduced-curve links]` Construct the corresponding independently geometric
  valuative psh class.
- **P12.3** `[T4; open beyond the complete book-local ideal-psh envelope
  on reduced-curve links]` Construct its independently geometric envelope
  theory.
- **P12.4** `[T5; open]` Construct model-independent bounded products.
- **P12.5** `[T5; open]` Construct a finite-energy theory.
- **P12.6** `[T4; open after normalized curve-branch functoriality,
  ideal-psh/envelope pullback, branch-surjective generic trace and
  conductor-scaled principal descent, finite conditional-expectation
  calculus, finite-flat canonical norm
  pushforward, and high-order conductor realization]`
  Establish finite-map functoriality, including branch and conductor descent.

All six targets remain active, but four now have sharply delimited
one-dimensional ranges.  Theorem `thm:p121-reduced-nagata-curve-link` identifies
the primary-ideal-normalized link of every reduced Nagata curve germ with
the finite set of points of its normalization above the closed point and
proves the exact change-of-ideal cocycle.  Proposition
`prop:p126-finite-reduced-curve-link` proves normalized restriction for
arbitrary finite local maps in that class: branch ramification multiplies
both the order and the extended-ideal denominator and therefore cancels.
The restriction map need not be surjective.  Proposition
`prop:p126-curve-conductor-principal-realization` realizes every sufficiently
deep integral branch-order vector by one downstairs regular primary
principal ideal.  Theorem `thm:p122-curve-principal-ideal-envelope` then
identifies those profiles with the strictly negative rational orthant, their
uniform closure with the nonpositive real orthant, and their raw finite-link
envelope with pointwise truncation by zero.  Theorem
`thm:p122-curve-ideal-psh-functoriality` defines the book-local ideal-psh
candidate by that uniform closure, computes its decreasing completion as all
extended nonpositive branch functions, identifies its normalization-free
homogeneous branch-cone form, and proves exact normalization, envelope, and
finite-map pullback formulas.  The pullback image is exactly the
fiber-constant subclass; pullback injectivity and surjectivity are
equivalent, respectively, to surjectivity and injectivity of the finite
branch map, and a surjective branch map gives a sup-norm isometry on the
continuous class.  On the completed lattices, fiberwise supremum and
infimum are the exact left and right adjoints to pullback, and their
source-side composites give the least fiber-constant majorant and greatest
fiber-constant minorant.  Example
`ex:p122-curve-psh-pullback-bottom` shows sharply why the completed class
must retain its bottom element: projection of a node onto one branch pulls
the nonbottom profile `(-infinity,0)` back to the bottom.  The superscript
`id` is a firewall: this is
not an identification with an independently constructed singular nef,
CLD-psh, or complex-analytic psh cone and supplies no product or energy
theory.  Theorem `thm:p126-curve-generic-norm-trace-descent` supplies the
reverse operation for every finite map surjective on branches.  The
branchwise generic degree is `delta_q=sum e_(q'/q) f_(q'/q)`; the
unnormalized weighted traces compose in arbitrary branch-surjective finite
towers, while division by `delta_q` gives an infimum/supremum-bounded
retraction of pullback.  This condition is sharp, since a missed base branch
makes pullback noninjective and therefore rules out any left inverse.
For finite obstacles, normalized pushforward after the ideal envelope is at
most the ideal envelope after normalized pushforward; equality holds exactly
on fibers without both strict signs.
On finite-valued functions the pullback of the normalized average is a
positive norm-one projection onto the fiber-constant descent image.  Its dual
Markov kernel lifts all signed measures with weights `ef/delta_q`, is a
total-variation isometry and a section of measure pushforward, and satisfies
the exact function--measure pairing identity.  Lift after pushforward is the
adjoint positive norm-one projection onto source measures with these
canonical conditional fiber weights; no singular Monge--Ampere interpretation
is claimed.  Relative to any full-support base probability and its canonical
lift, the function projection is the finite conditional expectation onto the
descent image: it satisfies the pullback-module identity, contracts every
`L^p` norm, is the orthogonal projection in `L^2`, and has the exact
within-fiber variance decomposition.  For `1<p<infinity`, equality in the
contraction holds exactly for fiber-constant functions.
Generic determinant orders of principal source models descend, after one
sufficiently divisible common scaling, through the downstairs conductor to
one regular primary principal element.  The normalized averages and their
dual signed-measure lifts compose if and only if the upper generic degree is
constant over intermediate branches.  Example
`ex:p126-curve-variable-degree-average` makes the distinction sharp on an
explicit reduced curve tower: direct and iterated normalized averages are
`-2` and `-7/4`, while both unnormalized traces are `-6`; the direct and
iterated lifts of unit mass are respectively `(1/3,1/3,1/3)` and
`(1/2,1/4,1/4)`.  Theorem
`thm:p126-curve-finite-flat-norm-descent` then makes this construction
canonical in the finite flat range.  For a rank-`d` local map, the
branch weights `e_(q'/q) f_(q'/q)` sum to `d`; the resulting normalized
weighted average is an order-preserving retraction of pullback, is squeezed
between the fiberwise infimum and supremum, commutes with changes of
primary-ideal cross-section, and composes in towers.  The determinant-norm
identity sends the principal source model `(g,N)` exactly to
`(Norm(g),dN)` downstairs, so the source conductor realization has a
genuine norm descent with no conductor scaling.  Flatness is essential only
for this canonical global determinant norm; the preceding generic trace
already covers arbitrary branch-surjective finite maps.  Theorem
`thm:p122-conductorial-disc-radial-psh-classification` makes that firewall
exact whenever the finite normalization is a union of closed discs, is an
isomorphism away from one point, and its conductor contains separated high
branch powers: the literal logarithmic radial extension is classically psh
exactly when it is CLD-v2 psh, and the extendable cone is
`{0} union [-infinity,0)^q`.  The conductor descends the normalized tuple
whose retained components are `t_i^{k_i}` and whose negative-infinite
components are zero; scaled logarithms and decreasing closure in the
remaining finite slopes prove the positive direction.  Upper
semicontinuity and the affinoid maximum principle exclude every mixed-zero
face, including `(-1,0)`.  Theorem
`thm:p122-multinode-radial-psh-classification` records the ordinary
multinode as the explicit coordinate-ring instance in which the descended
function is `sum_i x_i^{k_i}` over the retained branches.  The complementary
unibranch cusp example `ex:p122-cusp-radial-psh-classification` has conductor
`t^2K<t>` and every nonpositive radial profile extends, confirming that the
mixed-zero obstruction begins only when distinct branches must share one
singular value.  This classifies only
the radial disc-normalized realization, not a different boundary-trace
comparison or arbitrary singularities outside the stated conductor range.
Thus P12.1, P12.2, P12.3, and P12.6 are narrowed rather than retired, and
the atom count is unchanged.

A 10 September 2026 primary-source recheck
separates them from the global trivially-valued theory used in
\cite[\S2]{BJKS2}: over an algebraically closed characteristic-zero field,
that framework permits an integral projective variety before normality is
assumed and supplies global psh, finite-energy, and Monge--Amp\`ere objects.
Its exact Monge--Amp\`ere surjectivity is conditional on the envelope
property (recorded there in the smooth case).  It supplies neither the
normalizing datum of an excellent local germ nor the curve-local conductor
realization, local bounded products, or a local finite-map formula, so it
had changed no P12 atom or count before the curve results above.  The two BdFF local-volume
questions recorded as historical context
in the chapter are resolved and are not atoms here.

### `prob:frontier-affine-cone-ma` --- 2 atoms

- **P13.1** `[T4; open]` Develop comparison calculus for nonproportional
  Reeb fields strong enough to prove uniform differentiability of energy.
- **P13.2** `[T4; open]` Characterize exactly the image of the fixed-Reeb
  Monge--Amp\`ere operator and hence the measures admitting a solution.

For a fixed Reeb field the operator, decreasing continuity, and
bi-Lipschitz property onto its image are known.  Cross-polarization control
and the image characterization remain open; uniqueness on the image is not
counted as an additional unresolved atom.

A 10 September 2026 source recheck finds only version 1 of Wu's affine-cone
preprint.  Its ``Outlook and relation to other works'' identifies uniform
differentiability as the missing ingredient and specifically reduces it to
comparing \(\PSH(\xi)\) and \(\PSH(\xi')\) for nonproportional Reeb fields.
It supplies neither such a comparison nor a surjectivity theorem, so P13.1
and P13.2 remain unchanged.

### `prob:frontier-mp-pseff` --- 5 active atoms

- **P14.1** `[T4; open beyond established K\"ahler and projective regimes]` Intrinsically
  characterize the image of the raw ideal-valuative transform.
  `thm:p143-full-kahler-comparison` identifies that image in every K\"ahler
  class exactly with the full MP cone, without projectivity, rationality, or
  a finite-energy restriction.  Its restriction to finite energy is
  `cor:p141-finite-energy-raw-image`.  For a connected smooth
  projective variety and an ample \(\mathbf Q\)-line-bundle class,
  `thm:pseff-projective-dxz-mp-bijection` identifies the literal raw transform
  on every semivaluation with the full MP cone, without a finite-energy
  hypothesis.  For a projective real N\'eron--Severi class, the full
  DXZ--Boucksom--Jonsson identification is known, but the literal
  ideal-valuative formula is asserted only in the \(\mathbf Q\)-line-bundle
  case.  The big non-nef image characterization remains open.
- **P14.2** `[retired 19 September 2026]` The Chapter 71 theorem proves
  upper semicontinuity at arbitrary nondivisorial semivaluations by an
  explicit decreasing sequence of continuous finite-ideal approximants.  Its
  initial V14 source-closed review passed, but a later combined audit detected
  that the proof had applied psh subadditivity to quasi-psh levels without
  displaying the local bounded-perturbation reduction.  The live proof now
  supplies that reduction.  The repaired exact-current V15 review by
  `gpt-5.6-sol` at `xhigh` returned final `correct`, zero critical errors,
  and zero gaps for item `pi_4e14dc8a6a26aa190cd191b5`.  The V15 target,
  exact premise cards, first failed review, accepted retry, and hashes are
  archived in
  `solver_dossiers_20260919/p142_v15_qpsh_repair_production_20260919/`;
  the superseded V14 pass remains archived in
  `solver_dossiers_20260919/p142_v14_source_closed_production_20260919/`;
  the 58-row source manifest, 197 tests, final-path smoke, and two earlier
  `gpt-6-astra` hostile audits remain archived in
  `solver_dossiers_20260911/p142_v14_preproduction_gate_20260911/`.
- **P14.3** `[retired 19 September 2026]` Decide MP
  positivity at arbitrary semivaluations in a K\"ahler class.  The earlier
  source-bound dominated-divisorial theorem and finite-energy comparison
  passed production review as `pi_75b42272e15105bb6be0525c`.  The later
  `thm:p143-mp-section` constructs a unique DXZ preimage for every MP
  potential, without a finite-energy restriction; its final endpoint-aware
  version is archived in
  `solver_dossiers_20260913/p143_model_monotone_closure_20260913/`.
  The remaining direction is now proved by
  `thm:p143-full-kahler-comparison`: for every DXZ object, the truncations
  `Gamma vee (0-j)` have a literal zero tail, positive volume, and finite
  energy, decrease to `Gamma`, and have MP images whose nontrivial decreasing
  limit remains MP psh.  The P14.2 upper-semicontinuity theorem and the dominated
  comparison identify that limit with the literal raw transform everywhere.
  The original conditional exact statement, proof, source ranges, failed
  dependency-closure review, and repaired V4 receipt are archived in
  `solver_dossiers_20260919/p143_full_kahler_truncation_integration_20260919/`.
  The V4 `gpt-5.6-sol` / `xhigh` verdict is `correct`, with zero critical
  errors and zero gaps (`pi_88c7024842d3fd7d91b55d28`).  After the P14.2
  repair, the exact current target was rematerialized with seventeen exact
  internal premise cards, the accepted P14.2 V15 receipt, and one consistent
  extract family for each cited source.  The repaired unconditional production
  review returned `correct`, zero critical errors, and zero gaps for item
  `pi_90c4637f53444d88823e88f3`; its failed diagnostic review and accepted
  response are archived in
  `solver_dossiers_20260919/p143_unconditional_post_p142_production_20260919/`.
  Thus P14.3 has no independent K\"ahler residual and the full theorem is
  unconditional in its stated setting.  The big non-nef programme remains
  separated as P14.4--P14.6.
- **P14.4** `[T4; open]` Construct a \(P\)-sensitive positivity theory for
  big non-nef classes.  The unchanged relatively nef MP model signature is
  impossible, while the ideal-valuative transform and positive-volume DXZ
  energy remain only \(\mathcal I\)-level data.  Since
  \(\mathcal I\)-equivalence is strictly coarser than \(P\)-equivalence even
  for positive-mass K\"ahler potentials, no construction depending only on
  that transform can itself be \(P\)-sensitive or recover raw mass.  This is
  a boundary condition on a solution, not a negative answer: a theory that
  retains \(P\)-, movable-positive-part, or comparable extra data remains
  open.
- **P14.5** `[T5; open]` Construct the corresponding Monge--Amp\`ere
  measure theory.
- **P14.6** `[T5; open]` Construct the corresponding energy theory.
- **P14.8** `[T5; open; source-bound exact dichotomy verified]` A
  frozen, independently audited candidate specifies reconstruction from a
  realizable \(\mathcal I\)-class in a compact K\"ahler class to its canonical
  normalized \(\mathcal I\)-model representative.  It proves that this
  canonical representative is reconstructible, while a polar Cantor family
  shows that neither a raw representative nor raw nonpluripolar mass descends
  to the \(\mathcal I\)-quotient.  The source-bound V6 packet appends the
  exact Boucksom, BEGZ, and Kellay--Mashreghi extracts and passed final
  independent model-backed review as `pi_af3d4e7db16b025b3ed90770`, with zero
  critical errors and zero gaps.  The exact-live V7 audit then passed a
  source-and-boundary review (item `pi_c2863cf20cfa0c4bba834a16`) with zero
  critical errors and zero gaps, conditional on the exact excerpts whose
  local source hashes are pinned in
  `solver_dossiers_20260909/p148_v6_source_closed_packet_20260909/`
  `LIVE_INTEGRATION_AUDIT_V7_20260909`.  After the initial
  `gpt-6-astra`/`xhigh` review, the same frozen V7 statement and proof
  received a production `gpt-5.6-sol`/`xhigh` verdict of final `correct`,
  with zero critical errors and zero gaps (`pi_c2863cf20cfa0c4bba834a16`).
  Its exact request, response, strict receipt audit, and the immutable
  release-pin boundary are archived in that dossier.  This discharges the
  production-review gate for the frozen conditional comparison, not the
  broader atom.  A current-source V2 release, pinned to Git commit
  `01ba38fbd824f75ba4150f1913150950f9d4c19d`, now checks the same dichotomy
  against the corrected Chapter 51 source (including the arbitrary-divisor
  error `A(E)/m`).  Its source stage passed 197 tests and a zero-finding
  `gpt-6-astra`/`xhigh` audit, and its final path passed the long smoke.  Two
  earlier attempts were rejected and excluded.  The accepted
  `gpt-5.6-sol`/`xhigh` run
  `20260911T121602Z_4e4256d738ec_e04ebb78` returned `correct`, with zero
  critical errors and zero gaps; independent hostile replay closed all 87
  tool-call bindings with zero critical errors and zero material gaps.  The
  exact release and receipts are in
  `solver_dossiers_20260911/p148_current_source_release_v2_20260911`.  P14.8
  remains open: this verifies only the realizable-I-data canonical
  reconstruction/raw-data obstruction dichotomy, not arbitrary formal-data
  realization, a general all-semivaluation reconstruction formula, or a
  zero-mass strict-interior range of the DXZ filtration curve.

The divisorial realization, the finite-energy K\"ahler comparison, and the
projective real N\'eron--Severi DXZ--Boucksom--Jonsson comparison are known
in their stated domains.  P14.7 is retired by
`thm:pseff-filtration-maximality`, which proves raw maximality for every
strict-interior parameter without finite generation.  The equality of the
ordinary and multiplier-ideal envelopes remains attributed to DXZ,
Lemma 4.5.  Finski's March 2026 approximation theorem
[arXiv:2603.22194v1, Theorem 4.3](https://arxiv.org/html/2603.22194v1)
provides a separate published route after identifying its resolved envelope
with the DXZ ordinary envelope.  This is an explicitly attributed inference,
not a claim that Finski states the DXZ conjecture verbatim.

P14.8 remains active and separate.  The terminal left-limit corollary
`cor:pseff-terminal-filtration-slice` applies only to the particular DXZ
terminal slice; it does not reconstruct arbitrary zero-mass data.  The
frozen exact-dichotomy candidate in
`solver_dossiers_20260901/p148_zero_mass_reconstruction_candidate_v2_20260901`,
its source-bound V6 successor, its exact-live V7 audit, and the current-source
V2 production release are a source-scoped answer to the two defined
reconstruction readings.  The latest release is production verified, but it
is not a retirement of the broad atom and not a sourced second interval of
zero-mass slices.
The exact source comparison is preserved in
`solver_dossiers_20260831/p147_source_correction_independent_audit_20260831/SOURCE_CORRECTION_AUDIT.md`.
That source-only correction did not itself retire an atom; the complete
proof integrated in Chapter 71 is the retirement basis used here.

Pang--Sun--Wang--Zhou's version-one preprint of 14 July 2026
[arXiv:2607.12797, Theorem 1.2](https://arxiv.org/abs/2607.12797) proves
on the complex side that, for every potential in a big class, the
Darvas--Di Nezza--Lu ceiling equals the ordinary \(P\)-envelope and that
this envelope is idempotent even at zero mass.  It does not construct a
non-Archimedean realization or raw transform, realize arbitrary formal
\(\mathcal I\)-data, identify an all-semivaluation formula, recover raw
mass, or provide a second DXZ zero-mass filtration interval.  It narrows
only that complex envelope subissue; P14.8 and the count remain active and
unchanged.

### `prob:frontier-zero-volume` --- 3 atoms

- **P15.1** `[T5; open]` Construct a path-independent unnormalized energy
  after choosing the minimum necessary reference scale.
- **P15.2** `[T5; open]` Construct a path-independent zero-volume
  Monge--Amp\`ere theory.
- **P15.3** `[T4; open]` Construct a \(P\)-sensitive transcendental
  Okounkov body encoding lower-dimensional numerical data.

Probability normalization and mass recovery from only
\(\mathcal I\)-equivalence are disproved.  The positive-volume scope of
Xia's Conjecture 8.8 is verified in the separately stated domain; the three
zero-volume targets remain open.  Xia's numerical-dimension and Chebyshev
independence questions are useful milestones for `P15.3`, not additional
formal environments in this crosswalk.

The published Darvas--Reboulet--Witt Nystr\"om--Xia--Zhang theorem gives a
natural compact convex body for every pseudoeffective transcendental
cohomology class with a chosen flag, whose full-dimensional volume is
\(\operatorname{vol}(\alpha)/n!\).  At zero volume this supplies a
class-level body of zero ambient volume only.  It neither identifies its
lower-dimensional data with numerical dimension nor retains a prescribed
\(P\)-singularity type, and it supplies no zero-volume energy or
Monge--Amp\`ere theory.  Thus it narrows the context of P15.3 but leaves
P15.1--P15.3 active.

### `prob:frontier-general-ma` --- 7 atoms

Each atom asks for the finite-energy Monge--Amp\`ere operator and the
corresponding existence-and-uniqueness theorem after removing one indicated
restriction.

- **P16.1** `[T5; open]` Singular or unibranch varieties.
- **P16.2** `[T5; open]` Nonprojective but algebraizable proper settings.
- **P16.3** `[T5; open]` Positive residue characteristic.
- **P16.4** `[T4; open after the arbitrary-field invariant toric,
  skeleton-supported endpoint]` Nondiscrete valuations and arbitrary complete
  non-Archimedean fields outside
  `prop:p164-arbitrary-field-toric-skeletal-endpoint`.
- **P16.5** `[T5; open]` Big or pseudoeffective nonample positivity classes.
- **P16.6** `[T4; open after the invariant toric,
  skeleton-supported endpoint]` Arbitrary finite-energy measure support,
  beyond the skeletal measures in
  `prop:p164-arbitrary-field-toric-skeletal-endpoint`.
- **P16.7** `[T5; open]` Genuinely nonalgebraizable analytic spaces.

P16.2 has a necessary formulation boundary.  A proper algebraic
\(K\)-scheme with an ample line bundle is already projective over \(K\)
\(\cite[\mathrm{Tag}\ 0B5N]{StacksProject}\).  Hence it does not ask to
retain the BFJ ample line-bundle datum while omitting projectivity.  It asks
for a replacement positivity datum on a proper nonprojective algebraizable
space, together with the psh, finite-energy, and comparison theory needed for
an equation.  No such general replacement is currently supplied by the
listed endpoints.

The arbitrary-field toric endpoint has a proper toric variety, an ample toric
line bundle, a positive measure of the correct mass supported on the
canonical skeleton with no tropical-boundary mass, and a unique (up to
scaling) toric continuous singular psh solution; see
`prop:p164-arbitrary-field-toric-skeletal-endpoint` and
\(\cite[\mathrm{Theorem}\ 6.3.13]{BGJKK25}\).  It is not a general
arbitrary-field finite-energy operator or arbitrary-support result.  The
unrestricted axes remain open, and known nonskeletal examples rule out a
general reduction to one skeleton or to rational PL potentials.

There is a separate adjacent nonproper endpoint.  Wang's preprint
\(\cite[\mathrm{Theorem}\ A]{Wang25NACalabiYau}\) constructs, over trivially
valued \(\mathbf C\), a continuous local-CLD psh solution whose
Monge--Amp\`ere measure is the canonical Lebesgue measure on the essential
skeleton of \(X=\overline X\setminus D\), when \(\overline X\) is a smooth
projective Fano variety of dimension \(n>d\geq1\) and \(D\) is a reduced
SNC anticanonical divisor with standard-simplex dual complex.  This does not
narrow P16.2: the displayed \(X\) is affine, hence nonproper, and the source
does not construct a BFJ finite-energy theory or solve arbitrary-measure
equations.  It is included to keep the proper/nonproper boundary explicit;
it changes no atom or tier count.

Fang's version-one preprint
\(\cite[\mathrm{Proposition}\ 4.8]{Fang25Shilov}\) gives a different
finite-atomic inverse statement under the standing assumptions that the
ground field is maximally complete with
\(\lvert K^\times\rvert=\mathbf R_{>0}\).  For a finite set of graded
birational points on the affine cone of an ample line bundle, it realizes any
probability vector as the source's equidistribution measure of a
Shilov-finite, possibly singular metric.  This is not a P16.6 endpoint: the
paper identifies comparison with the genuine Monge--Amp\`ere measure as a
separate envelope-continuity step, so it constructs neither a continuous
semipositive solution nor the BFJ finite-energy operator.  The atom and tier
counts are unchanged.

### Retired P17 history --- 0 active atoms

P17.1 asked whether fibrewise mixed Monge--Amp\`ere integrals vary
continuously over a general integral Banach ring.  It is retired positively
by `thm:p171-full-assembly`, which answers Pille--Schneider Question 4.9
with its original quantifiers.  The proof derives finite presentation from
the source hypotheses, retains the top fundamental cycle and every generic
length, treats all Archimedean powers and both non-Archimedean branches, and
adds no reducedness or purity assumption.

The exact live dependency closure and principal theorem passed production
Rethlas item `pi_87b42b938a8d830222bed78f`, using `gpt-5.6-sol` at
`xhigh`, with final verdict `correct`, zero critical errors, and zero gaps.
The materialized statement and proof SHA-256 values are
`0ba26fe924a065af31198cfc74aa44e790feb128159eef24458f8ca0b151f8b4`
and
`cdce552b3750faed4dfbb6a0284405094be10b56c138363482cca0464e20f4af`.
The principal live statement and proof hashes are
`0d95354a4cd2bd15d03020dde630779f4f423b73e9661eb8e65e0511dc765e24`
and
`9cab2f0f679b095b00b2d9f760a4a5315d3a24fe7b295a9d0a9bf414d91e434a`.
The earlier finite closed-immersion reduction remains valid historical
input, but it is no longer the controlling frontier status.

### Retired P18 history --- 0 active atoms

`thm:hybrid-endpoint-continuity-counterexample` disproves both the literal
Favre--Pille-Schneider endpoint question and the zero-supremum normalized
strengthening.  The latter is controlled by production run
`20260825T035945Z_070e264c3ef1`, item
`pi_db89dd432acabcf33a3f2272`, with final verdict `correct`; the exact
adapted live bytes passed the independent run
`20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`, with the same verdict.  The former
`P18.1` is therefore not an active atom and has no replacement.

### `prob:frontier-hybrid-ytd` --- 4 atoms

These atoms retain only the residual scope after the smooth polarized
projective results described in the chapter.

- **P19.1** `[T5; open]` Prove the remaining entropy-slope statement for
  arbitrary finite-energy weak rays on a compact K\"ahler manifold.
- **P19.2** `[T4; open]` Construct model approximations preserving the
  required energy, entropy, and singularity data.
- **P19.3** `[T5; open]` Prove the hybrid compactness and measure-continuity
  statements needed along degenerating families.
- **P19.4** `[T5; open]` Establish the required automorphism-equivariant,
  transcendental, and singular extensions.

The dated smooth polarized projective claims listed in the chapter are not
open atoms.  The four corrected residual targets above are independent hybrid
targets, not prerequisites for the already cited Kähler-class implication
from uniform model stability to a cscK metric; they remain open.

Boucksom--Jonsson's 19 May 2026 version-two lecture notes are an orientation
source that sketches a cscK YTD argument, not a separate approximation or
hybrid-continuity result; they therefore do not narrow P19.1--P19.4.

Wang's source-stated Theorem B supplies a different, nonproper endpoint: in
each of its three affine/Calabi-model settings, explicitly rescaled
Archimedean and non-Archimedean potentials glue continuously on the hybrid
space, and the rescaled Archimedean Monge--Ampère measures converge weakly to
the non-Archimedean measure \(\cite[\mathrm{Theorem}\ B]{Wang25NACalabiYau}\).
It concerns a fixed quasi-projective variety under hybridization, rather than
a degenerating family of compact Kähler manifolds, so it does not narrow
P19.3 or alter the active-atom count.

### `prob:frontier-cross-fan-upstairs` --- 1 atom

- **P21.3** `[T2; open residual]` In analytic dimension at least two,
  determine whether every positive closed CLD current of bidegree
  \((p,p)\), \(0\le p\le n-1\), on a good separated strict boundaryless
  pure \(n\)-dimensional analytic space has Bedford--Taylor independence for
  continuous psh pairs of equal curvature, or construct a counterexample.
  The entire one-dimensional case inside these ambient hypotheses is settled
  by `prop:p213-componentwise-arbitrary-valuation`, over either a trivial or
  nontrivial valuation and without reducedness or normalization-smoothness
  assumptions.  Spaces carrying a genuine ordinary-topology basis of
  standard strict open polycylinders are settled by
  `cor:p213-polycylinder-basis-v2-candidate`; on one standard strict open
  polycylinder, pairs defined on the whole polycylinder are settled by
  `prop:p213-fixed-polycylinder-v2-candidate`.  The invariant
  split-toric subcase, including toric boundary strata, is settled by
  `prop:p213-invariant-split-toric-continuous-pairs-candidate`: it allows an
  arbitrary positive closed CLD current on an open inverse image under
  extended tropicalization in a split toric variety, including its toric
  boundary strata.  Its multiplier identity requires only a finite continuous
  pair with equal current Hessian and maximal-compact-torus-invariant
  difference; its stated Bedford--Taylor consequence retains psh pairs because
  that is the P21.3 predicate.
  In every dimension, `cor:ch16-cpsh-component-curvature` additionally
  settles the specified reduced analytic component integration currents on
  every ordinary open: arbitrary continuous CPsh pairs of equal canonical
  curvature have equal products against each such component current, with
  generic nonreduced multiplicities and divisorial crossings retained.  It
  uses ordinary-local full-CPsh analytic nullity and does not classify an
  arbitrary positive closed current.  Its immediate linear extension
  `cor:ch16-cpsh-component-diagonal-current` covers every locally finite
  nonnegative component-diagonal \((0,0)\)-current
  \(\sum_i c_i\delta_{W_i}\) on the same ordinary open.  Its smooth-factor
  extension `cor:ch16-cpsh-smooth-component-current` also covers every fixed
  smooth positive closed decoration
  \(\bigl(\sum_i c_i\delta_{W_i}\bigr)\wedge\gamma\) in bidegree
  \((q,q)\), \(0\leq q\leq n-1\).  This remains a component-diagonal
  current with a prescribed smooth factor: it neither treats a general
  positive closed current nor supplies a variable or singular
  positive-bidegree factor.  More generally,
  `cor:ch16-cpsh-weak-component-current` covers the weak limits, with
  \(q\) fixed, of finite nonnegative sums of such smooth-component currents.
  Its local extension
  `cor:ch16-cpsh-local-weak-component-current` permits the component families
  and approximating nets to vary over an ordinary open cover.  Both are stated
  weak-approximability conditions, not density theorems for positive closed
  currents.
  There is an exact sufficient bridge in the remaining scope: if the
  zero-Hessian difference of a continuous psh pair is locally uniformly
  approximable by smooth zero-Hessian functions, then
  `cor:ch16-local-pluriharmonic-criterion` gives the required independence for
  every positive closed current.  A further pairwise class is now closed:
  if the current is locally weak-form-induced from a closed weakly smooth
  form in the sense of `def:ch18-weak-form-induced-current`, and the
  zero-Hessian difference is weakly smooth, then
  `prop:ch18-weak-form-induced-bt` identifies its order-zero ordinary product
  with the restricted strong product and gives the equality.  This is not an
  assertion for an arbitrary strong lift, arbitrary positive closed current,
  or arbitrary continuous zero-Hessian difference.
  The same bridge is now closed under the paired local closures recorded in
  `def:ch18-weak-approximation-classes`: a weak limit of positive closed
  locally weak-form-induced currents and a locally uniform limit of weakly
  smooth zero-Hessian differences satisfy the equality by
  `prop:ch18-weak-form-closure-bt`.  This uses two applications of the
  ordinary order-zero multiplication-continuity lemma.  It is a conditional
  closure statement, not a density theorem for arbitrary currents or
  continuous zero-Hessian differences, so P21.3 remains active.
  Independently, a further pairwise class is now closed:
  when that difference locally factors through a proper full-rank moment
  satisfying every hypothesis of `prop:p062-proper-full-rank-moment`, its
  affine source formula makes it smooth with zero Hessian, and
  `cor:ch18-local-proper-full-rank-moment-bt` gives the required independence.
  A further spatial class is now closed: if the ordinary topology has a
  genuine basis of boundaryless strict finite towers of locally trivial
  standard open-polydisc bundles over standard strict endpoint polycylinders,
  `cor:p213-endpoint-tower-basis-bt` gives the required equality for every
  positive closed CLD current.  The endpoint-tower formula makes the
  difference ordinary CLD-smooth with zero Hessian, and the proof therefore
  uses the local smooth criterion rather than pulling back the current.  It
  requires that actual ordinary-open basis only to obtain the conclusion for
  every open set at once.  For one specified open set, an ordinary cover by
  such actual endpoint towers suffices by
  `cor:p213-endpoint-tower-cover-bt`.  Neither version applies to one chart
  inside an arbitrary germ, annular fibres, or fibrations lacking the stated
  local product charts.
  This endpoint class is now closed under finite mixtures of all four
  exact locally trivial descent geometries.  In
  `thm:p213-endpoint-mixed-tower-classification`, each stage may be a
  standard strict open-polydisc bundle, a projective-space bundle, a smooth
  proper split-toric bundle, or---when the field is algebraically
  closed---a proper smooth connected curve bundle.  A continuous
  zero-current function on the whole tower is the
  pullback of a unique logarithmic-affine function on the endpoint base and
  is therefore ordinary CLD-smooth with zero Hessian.  The whole-space,
  cover, and genuine-basis consequences are respectively
  `cor:p213-endpoint-mixed-tower-bt`,
  `cor:p213-endpoint-mixed-tower-cover-bt`, and
  `cor:p213-endpoint-mixed-tower-basis-bt`.  Each projective, split-toric,
  or proper-curve stage retains the exact locally holomorphically separated
  and paracompact
  base hypotheses of its descent theorem.  The result introduces no
  annular bundle fibre and gives no conclusion from a tower chart that does
  not refine the potentials' domain.
  A distinct residual-geometric spatial class is also closed.  On an open
  subset of the analytification of a smooth proper curve over an
  algebraically closed complete nontrivially valued field,
  `prop:p213-residual-picard-smooth-curve` identifies the exact obstruction
  to ordinary CLD-smoothness of a continuous zero-current function at a
  type-2 point with its class in
  \(\operatorname{Pic}^0(C_x)\otimes_{\mathbf Z}\mathbf R\); at all other
  point types the obstruction vanishes automatically.  If these Picard
  tensors vanish throughout the base, then
  `thm:p213-residual-picard-mixed-tower` propagates ordinary smooth
  zero-Hessian regularity through every finite mixed tower of locally
  trivial standard strict open-polydisc, projective-space, smooth proper
  split-toric, and proper smooth connected curve bundles.  The projective,
  split-toric, and proper-curve stages retain
  the exact locally holomorphically separated and paracompact base
  hypotheses of their descent propositions.  On a boundaryless top level,
  `cor:p213-residual-picard-mixed-tower-bt` gives whole-space independence
  against every positive closed ordinary CLD current; an ordinary cover by
  such towers gives the same result on that specified open by
  `cor:p213-residual-picard-mixed-tower-cover-bt`, and a genuine basis gives
  the every-open predicate by
  `cor:p213-residual-picard-mixed-tower-basis-bt`.  This includes bases over
  Mumford curves and over residue fields algebraic over a finite field.  It
  neither treats a single tower chart that fails to refine the potentials'
  domain nor removes the residual-Picard hypothesis.
  This residual-geometric class now permits a locally twisted
  open-polycylinder bundle at the bottom before the four exact bundle types
  are iterated.  In
  `thm:p213-residual-picard-open-polycylinder-mixed-tower`, the annular
  coefficient formula is used only chartwise: its curve coefficient is
  ordinary smooth by the residual-Picard criterion, its slopes are locally
  constant, and every `log|T_i|` is ordinary smooth with zero Hessian.
  Exact open-disc descent handles the optional disc factors, and exact mixed
  descent plus CLD-form pullback handles the later tower.  Thus neither the
  integral annular monodromy nor the zero-current radiance class must vanish.
  The whole-space, cover, and genuine-basis consequences are
  `cor:p213-residual-picard-open-polycylinder-mixed-tower-bt`,
  `cor:p213-residual-picard-open-polycylinder-mixed-tower-cover-bt`, and
  `cor:p213-residual-picard-open-polycylinder-mixed-tower-basis-bt`.
  They give independence against every positive closed ordinary CLD current
  in their stated scopes, but no global logarithmic coefficient formula and
  no result without the displayed local product charts or the
  residual-Picard hypothesis.  Hence P21.3 and the inventory count are
  unchanged.
  The annular geometry need not be confined to the bottom of the tower.
  In `thm:p213-residual-picard-curve-local-interleaved-tower`, one analytic
  open cover of the residual-Picard curve base makes the base-changed tower
  an arbitrary finite interleaving of globally coordinated standard strict
  open-polyannulus products and the four exact bundle types.  Coordinates,
  radii, and product trivializations may depend on the cover member and need
  not agree on overlaps.  The local coefficient formula, residual-Picard
  criterion, logarithmic smoothness, and functorial CLD pullback make every
  continuous zero-current function on the top ordinary CLD-smooth with zero
  smooth Hessian.  Its whole-space, specified-cover, and every-open basis
  Bedford--Taylor consequences are
  `cor:p213-residual-picard-curve-local-interleaved-tower-bt`,
  `cor:p213-residual-picard-curve-local-interleaved-tower-cover-bt`, and
  `cor:p213-residual-picard-curve-local-interleaved-tower-basis-bt`.
  This removes the bottom-only placement restriction from the preceding
  residual-Picard annular class, but retains the curve-local tower charts
  and residual-Picard hypothesis and gives no global coefficient formula.
  P21.3 and the active count therefore remain unchanged.
  The common curve-cover restriction can now be replaced by a stage-local
  one.  `prop:p062-stage-local-polyannulus-smooth-rigidity-transfer` proves
  that a locally trivial finite strict open-polyannulus bundle preserves
  ordinary CLD-smooth zero-Hessian regularity and first-current rigidity
  when every member of its chosen trivializing base cover already has those
  properties (and classical pluriharmonicity) for continuous zero-current
  functions.  Combining that transfer with the four exact bundle types gives
  `thm:p213-residual-picard-stage-local-annular-tower`: annular charts may
  occur over arbitrary intermediate bases and need not be pulled back from
  one cover of the residual-Picard curve.  Its whole-space, cover, and basis
  Bedford--Taylor consequences are
  `cor:p213-residual-picard-stage-local-annular-tower-bt`,
  `cor:p213-residual-picard-stage-local-annular-tower-cover-bt`, and
  `cor:p213-residual-picard-stage-local-annular-tower-basis-bt`.
  The stage-local hypothesis cannot be replaced by the corresponding
  whole-space conclusion in general.  Proposition
  `prop:p213-zero-current-smoothness-not-open-hereditary` gives a smooth
  proper surface `X = (P^1_K)^an x D^an` on which every global continuous
  zero-current function is constant, yet an ordinary product open carries
  a continuous zero-current function which is not ordinary CLD-smooth.  A
  good-reduction elliptic curve over
  `K = completion(overline(C((t))))` supplies an explicit instance.  The
  projection of this `X` to `(P^1_K)^an` is itself the proper smooth
  curve-bundle stage allowed by the mixed exact-tower theorem.  Hence the
  failure occurs on an exact intermediate base and proves that the v69
  stage-local premise is mathematically necessary for that route.  This is
  not a counterexample to P21.3, so the active count remains unchanged.
  The bare real-PL or GJR-harmonic outcomes occurring in P06.1/P06.2 remain
  G-local/weakly smooth and do not themselves give this ordinary CLD-smooth
  approximation: `prop:ch19-cld-smooth-harmonic-nonregularization` gives an
  integral PL weakly smooth harmonic curve example with no locally uniform
  ordinary CLD-smooth harmonic approximation.  That blocks this route, not the
  separately proved one-dimensional P21.3 classification.
  P06.2 supplies no such local factorization for an arbitrary difference, so
  this is a pairwise exclusion rather than a spatial solution of P21.3.  The
  unresolved issue is therefore the higher-dimensional gluing/approximation
  step outside these factorized pairs.
  Scalar extension alone is not an additional P21.3 narrowing: the present
  cited base-change statements control specified CLD form/measure degrees or
  top-degree Monge--Amp\`ere measures of semipositive metrics, not an arbitrary
  positive closed CLD current together with faithful descent of its mixed
  Bedford--Taylor current.  The source audit
  `solver_dossiers_20260909/p213_scalar_extension_current_audit_20260909/`
  records the exact boundary.  Consequently the scalar-stable potential
  results for P06.1/P06.2 do not themselves supply an algebraic-split-form
  P21.3 corollary for an arbitrary positive closed current.  There is a
  narrower paired extension: if the current is locally weak-form-approximable
  and the difference has the analytic-local algebraic-split invariant-toric
  tower data, including the scalar-stable upstairs zero-current equality, then
  `cor:p213-algebraic-split-scalar-stable-weak-form-bt` gives the ordinary
  Bedford--Taylor equality.  This uses scalar stability only to obtain a
  downstairs weakly smooth harmonic difference, whose constant net meets the
  weak-harmonic approximation condition; it then applies the existing
  weak-form closure bridge.  It creates neither current ascent nor current
  descent and does not treat arbitrary currents or arbitrary continuous
  zero-current differences.
  There is nevertheless a split, nonproduct P21.3 extension.  On a
  boundaryless top-level finite tower of equivariant locally trivial standard
  strict open-polydisc bundles over an actual split-toric base, every finite
  continuous equal-curvature psh pair with invariant difference has
  Bedford--Taylor independence against every positive closed CLD current:
  `cor:p213-invariant-toric-open-polydisc-tower-bt`.  Exact descent moves the
  difference to the toric base; the compactified-ray argument makes that base
  difference ordinary CLD-smooth with zero Hessian, and CLD-form pullback
  preserves this through the tower.  This requires the split base, the action
  on every tower level, and equivariance of every map.  It does not cover
  pairs with noninvariant difference, nonsplit forms, or arbitrary-current
  descent through a scalar extension, so P21.3 remains active.
  For one specified ordinary open, the spatial extension
  `cor:p213-invariant-toric-open-polydisc-tower-cover-bt` needs only an
  ordinary cover by such actual boundaryless split-toric equivariant towers,
  with the difference invariant for the action on each member.  The basis
  version `cor:p213-invariant-toric-open-polydisc-tower-basis-bt` applies on
  every ordinary open when the ambient topology has such a basis.  Neither
  version claims that arbitrary local charts glue to one action or that an
  arbitrary pair is locally invariant.
  The literal
  discontinuous-potential predicate of CLD
  Definition 8.6.2 is a stronger scope boundary and is not a separately
  counted atom.

The two preceding realization atoms are retired.  `P21.1` is negatively
settled by the compact-source obstruction in production run
`20260825T024519Z_16376e0d52eb`.  `P21.2` is positively settled by the
proper noncompact split-Gauss construction and its positive cycle current
in seven-item production run `20260825T021353Z_058a4390b0fb`.  In that
construction the two curvature currents are unequal upstairs and agree only
after pushforward, so it does not settle `P21.3`.

A third guarded production run,
`20260825T034743Z_ea6194f07e86`, item
`pi_19c9aad210847a2875a0fe4a`, excludes one smooth connected workaround.
For the natural four-punctured \(\mathbf P^1\) construction the two real-PL
curvatures are equal at the same Gauss point, but adjoining the third unit
\((z-a)/(z-c)\) forces all four visible weights of a positive closed
order-zero current to be equal.  Hence the proposed `(2,2,1,1)` weights do
not come from such a current.  The run returned final `correct`, zero
critical errors, and zero gaps.  This is a candidate-level obstruction only:
`P21.3` remains open, stays in the queue, and the inventory count is
unchanged.

The original wording also offered an unrestricted delta-current branch.
That branch was not well-defined.  The exact Gubler--Künnemann module is
`B_GK × E_GK → E_GK`, with `B_GK^(0,0)=A^(0,0)`; it does not multiply an
arbitrary real-PL or continuous function by an arbitrary delta-current.
The complete graded Leibniz identity and this scope boundary passed
production Rethlas run `20260826T072535Z_e0a34aabb30f`, item
`pi_2554dbbac2584768c3a71996`, with final `correct`, zero critical errors,
and zero gaps.  This correction neither proves nor disproves the analytic
CLD question, so it does not retire the atom.

The principal continuous-pair curve subcase, including arbitrary nilpotent
thickenings in the stated analytic class, is now retired over every complete
nontrivially valued field.  Every positive closed CLD current of bidegree
\((0,0)\) on a good separated strict pure one-dimensional boundaryless
analytic space whose reduced component normalizations are rig-smooth is a
unique locally finite nonnegative linear combination of the normalized
reduced-component currents.  Ordinary forms, compact-test topologies,
currents, positivity, closedness, and the psh sheaves are invariant under
reduction, while the integration current retains the generic
multiplicities.  The exact arbitrary-field reduced packet passed production
Rethlas run `20260828T042906Z_f2a1c1b9f2a3` with 17 statement and 19 source
checks; the independent nonreduced combined packet passed
`20260828T044008Z_dfdaa04a1cea` with 24 and 25 checks; and the exact-live
arbitrary-field nonreduced packet passed the HTTP-archived closure run
`20260828T051601Z_db92555a72e1` with 23 and 25 checks.  All three used
`gpt-5.6-sol` at `xhigh` and returned final `correct`, zero critical errors,
and zero gaps.  The exact-live nonreduced statement and proof SHA-256 values
are
`e7b9889f6c063d9952d61c0472290183aac07b58c8d0569cfebc5e9ea73f1a9c`
and
`25fe49a46b1c5cd62b0d1a5024095b47cdd49c66f594d1d86eec4f9f270c83ec`.
The earlier `20260828T045515Z_db92555a72e1` run is service-only corroborating
provenance rather than the controlling gate.  Independent byte, source, and
hostile audits also passed.  Thus neither
nonreducedness nor failure of algebraic closedness remains in the residual
domain over a complete nontrivially valued field.  This gate did not retire
P21.3.  At that stage, after the separate P00.1 retirement, the controlling
count was 54 active atoms.  The later P17.1 retirement lowers the current
count to 53.

**29 August 2026 P21.3 rigid-exception narrowing addendum.**  Let `X` be a
nonempty connected good separated strict normal boundaryless analytic curve
over a complete nontrivially valued field, and let `E` be a locally finite
set of rigid points whose complement is rig-smooth.  Then `X - E` is
nonempty and connected; every positive `d'`- and `d''`-closed CLD
`(0,0)` current on `X` is a unique nonnegative multiple of the integration
current; and continuous-pair Bedford--Taylor independence holds.  The exact
candidate statement and proof have SHA-256
`cf53c4101b6fe798d89c7e37188f2d1f03f389a5a468fdd055b6fba8bf8cf2f5`
and
`cf94877ec4b2a1010a3eb51915c7cbc20a134da0bf2563b90585deab992850ce`.
Submitted with the exact rig-smooth dependency, they passed production run
`20260829T021315Z_cc0c48725114` using `gpt-5.6-sol` at `xhigh`: 14
statement checks and 26 primary-source checks, final `correct`, zero
critical errors, and zero gaps.  This narrows but does not retire P21.3; the
atom count is unchanged.

**29 August 2026 P21.3 componentwise rigid-exception controlling
addendum.**  Let `X` be a good separated strict boundaryless pure
one-dimensional analytic space over a complete nontrivially valued field,
with arbitrary nilpotent structure.  Assume that, for every irreducible
component of `X_red`, the non-rig-smooth locus of its normalization is
contained in a locally finite set of rigid points.  Then nilreduction
identifies the ordinary CLD calculus, current topology, positivity,
closedness, and continuous-psh sheaves; the integration current retains the
generic component multiplicities; every positive closed `(0,0)` current is
a unique locally finite nonnegative combination of the normalized reduced
component currents; and continuous-pair Bedford--Taylor independence holds.
Thus reducible and nonreduced curves in this class are settled, not residual.

The complete dependency-closed production materialization has statement and
proof SHA-256
`2bf673687e935bcdae91550158344647cb1ca1cd4ae0a5040109aeb5fb2f3cbc`
and
`a27c40fbb1328b008acab07b871f50a778c34bab2b0f1d05e3a6d9d229839716`.
Production Rethlas run `20260829T061505Z_2bf673687e93`, item
`pi_ee24d64b88f0c4e60ad1acbd`, used `gpt-5.6-sol` at `xhigh` and returned
final `correct`, zero critical errors, and zero gaps.  An earlier
noncontrolling materialization omitted the already verified transitive
canonical-collar bridge and was rejected for that packaging defect; the
candidate theorem bytes were unchanged, so that rejection is not recorded
as a mathematical failure.  This is a book-level verified extension with no
novelty or priority claim.

**29 August 2026 P21.3 arbitrary-valued curve controlling addendum.**  On a
connected good separated normal boundaryless pure analytic curve over any
complete non-Archimedean field, possibly trivially valued, every positive
closed ordinary CLD `(0,0)` current is a nonnegative multiple of the
integration current and has the full CLD Bedford--Taylor property.  On an
arbitrary good separated strict boundaryless pure one-dimensional analytic
space, with reducible and nonreduced structure allowed and with no smoothness
assumption on component normalizations, every such current is a unique
locally finite nonnegative combination of normalized reduced-component
currents and has continuous-pair Bedford--Taylor independence.

The exact normal statement/proof hashes are
`339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`
and
`d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`;
production item `pi_d9543424f0492e1412e0d203` returned final `correct`,
zero critical errors, and zero gaps.  The dependency-closed componentwise
materialization has statement/proof hashes
`d1ad274eb03a9a51db54427c6cef1f8ff7121a987e70caecd6453f868598d1f6`
and
`cd7f2e4cc32ca90c6f866f8190da57ad885fd7effa0bed3248f880d09bbf209f`;
production item `pi_1ca3e6d14c7e8596372d863d` returned final `correct`,
zero critical errors, and zero gaps, with the exact materialized proof
digest.  All one-dimensional cases within the ambient hypotheses are
therefore retired from P21.3.

**30 August 2026 P21.3 strict-open-polycylinder narrowing addendum.**  Let
`X` be a good topologically separated pure boundaryless analytic space.  If
`X` has a genuine basis for its ordinary topology on whose members every
continuous zero-current function is ordinary CLD-smooth with zero smooth
Hessian, then every positive `d'`- and `d''`-closed CLD current on `X` has
continuous-pair Bedford--Taylor independence on every open set.  This
applies, over a nontrivially valued field, when the basis members are
standard strict open polycylinders.  On one standard strict open
polycylinder the same identity holds for an equal-curvature pair defined on
the whole polycylinder, but this fixed-domain statement does not claim the
every-open predicate.

The exact principal statement/proof SHA-256 values are
`955e1ab4323ddfe935b8bb54d7657915ea6f563e8d6e8f178ab589fcee5f16f1`
and
`70f34cad9f975402dd03f7f03de0b941898df112df2c018570bdbcba0b48f077`.
After prepending the exact verified P06.2 dependency, the materialized
statement/proof values are
`6c90e664468b815126ff64f1c0e2297b4d81bf0cf8d51e2a243ee778822f42ce`
and
`6eff86ba6c989143485449b189f1379e986f3d8349abc403dc23ae5d56e7fd33`.
The archived request/response values are
`add3a522de8d31ffb393d3c38c9ef63f33d125bccc5f56797cd7679cc3b7696d`
and
`8ef692e78c8ab156238597405a0b5cd8003f5bc9bee94acc62ab4eb913317779`.
Production Rethlas used `gpt-5.6-sol` at `xhigh` and returned final
`correct`, zero critical errors, and zero gaps after an independent
exact-byte hostile audit.

The superseded first candidate confused a polycylinder atlas with a basis
refining every open set.  Its exact-byte audit therefore failed closed, and
it was neither submitted nor integrated.  The repaired theorem keeps the
basis and fixed-domain assertions separate.  This narrows P21.3 but does not
retire its general higher-dimensional atom, so the inventory count is
unchanged.

P21.3 remains one T2 atom only in analytic dimension at least two.  At this
29 August milestone, before the independent P17.1 retirement recorded above, the
inventory stood at 15 formal problem environments and 54 active atoms, with
tier totals `(0,6,14,17,17)`.

**28 August 2026 P00.1 controlling retirement addendum.**  For every
connected smooth projective complex variety and every ample real numerical
class, GAGA identifies the rational PL Mesquita--Piccione and
Boucksom--Jonsson model cones, including their relative-nef conditions, and
their decreasing completions therefore agree on all semivaluations.  For an
ample rational line-bundle class, composition with Darvas--Xia--Zhang,
Theorem 3.14 gives the unrestricted DXZ--MP order isomorphism without a
finite-energy hypothesis.  This is a book-level, source-explicit synthesis
of published MP, BJ, and DXZ inputs; it is not a novelty or priority claim.
The exact frozen statement and proof have SHA-256
`e40829e3586bcabeeb866229dc068c2e518a736fc908dec32f3bf3957c59c9ab`
and
`baad23068e9dcae47619f3e2d81cfd26fa5bd51b1e4c4d4baa1a7c024824e671`.
The production archive
`rethlas_packets_20260828/p001_mp_bj_full_cone_run_20260828` records verdict
`correct`, zero critical errors, and zero gaps after two independent
exact-byte audits.  This controls the frozen candidate; the exact-live
statement and proof, SHA-256
`949819c48c8d0e991acbb92ed7c15d504dd691056f06553c58ac1d4ab564d33e`
and
`58c2954ad1e541ab41e0649c4e84e22252299265b422159df41fe5772f2e8064`,
passed the superseding archive
`rethlas_packets_20260828/p001_mp_bj_full_cone_live_run2_20260828`, verdict
`correct`, zero critical errors, and zero gaps.  P00.1 and its Chapter 71
problem environment are retired.
At this 28 August milestone, the active inventory was 15 formal
environments and 54 atoms.  After the 30 August retirements recorded above,
the P14.7, P14.3, and P14.2 retirements, the current inventory is 14 formal
environments and 46 atoms.

## Easy-to-hard Rethlas queue

The tiers estimate how bounded the first exact submission can be, not the
probability that its expected answer is affirmative.  A verified
counterexample retires an atom just as a verified proof does.

### T1 --- concrete first submissions (0 atoms)

No active atom remains in this tier after retirement of `P01.1`.

### T2 --- focused problems with one principal missing bridge (5 atoms)

`P21.3`, `P07.1`, `P06.1`, `P06.2`, `P03.1`.

### T3 --- major theorems within mature frameworks (8 atoms)

`P02.1`, `P02.2`, `P02.3`, `P05.1`, `P05.2`,
`P08.1`, `P03.2`,
`P03.3`.

### T4 --- new comparison theories or several coupled inputs (16 atoms)

`P02.4`, `P04.1`, `P04.2`, `P05.5`, `P12.1`, `P12.2`, `P12.3`,
`P12.6`, `P13.1`, `P13.2`, `P14.1`, `P14.4`, `P15.3`,
`P16.4`, `P16.6`, `P19.2`.

### T5 --- foundational theory or programme-level targets (17 atoms)

`P04.3`, `P04.4`, `P12.4`, `P12.5`, `P14.5`, `P14.6`, `P14.8`,
`P15.1`, `P15.2`, `P16.1`, `P16.2`, `P16.3`, `P16.5`, `P16.7`,
`P19.1`, `P19.3`, `P19.4`.

## Retirement rule

An atom leaves this inventory only after its exact current statement and
proof or counterexample receive a production Rethlas
`gpt-5.6-sol`/`xhigh` verdict of `correct` with no critical errors and no
gaps, survive source and boundary audits, and are integrated into the live
book.  Removing one atom from a compound environment does not retire the
remaining atoms.
