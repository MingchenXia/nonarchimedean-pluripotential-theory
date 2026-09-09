# Atomic crosswalk for the active problem environments

**Inventory date:** 10 September 2026
**Literature cutoff:** 10 September 2026; targeted P14.7/P14.8 source update on 31 August and P05/P13/P15/P16 source updates on 10 September 2026
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
theorem,
the exact count is

```text
14 formal problem environments = 48 active atomic research questions.
Tier counts: (T1,T2,T3,T4,T5) = (0,5,9,17,17).
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

There is now a source-scoped P02.1 companion on an ordinary Euclidean ball
compactly contained in a split-toric convex chamber.  If the ball inverse
image is good, separated, strict, boundaryless, and pure-dimensional, every
finite continuous maximal-compact-torus-invariant current-psh function there
is a locally uniform decreasing limit of invariant semipositive real-PL
functions.  Finite tangent-plane maxima approximate gently shifted radial
convex smoothings from above, and their positive interstage gaps enforce
monotonicity.  This begins with the invariant current-psh class and supplies
only the real-PL conclusion by itself; the distinct companion arguments below
add the locally Fubini--Study and weakly smooth conclusions.  It does not
alter any P02 atom or count.

There is now a source-scoped P02.2 companion on the same type of split-toric
interior ball.  It approximates the finitely many supporting planes of
successive convex smoothings directly, from above, by affine functions with
one common character denominator.  Their finite maxima pull back to locally
Fubini--Study functions on the same fixed ball, and the prescribed positive
gaps retain monotonicity.  This starts with the invariant current-psh class,
not an arbitrary classically psh function, and does not alter any P02 atom or
count.

There is now a source-scoped P02.4 companion on the inverse image of an
ordinary open convex tropical chamber in a split torus.  Every finite
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
neither the finite-continuous invariant starting class nor the interior-ball
scope, supplies no local-Fubini--Study conclusion, and does not alter any
P02 atom or count.

### `prob:frontier-unibranch-local-envelope` --- 3 atoms

- **P03.1** `[T2; open]` Classify the irreducible, normal, or analytically
  unibranch higher-dimensional hypotheses, and determine sharp necessity,
  under which usc
  regularization of every upper-semicontinuous local
  FS/semipositive-PL obstacle envelope is classically psh.  The
  perfected-unibranch reduced strict curve range is settled positively by
  `thm:p031-perfected-unibranch-curve-envelope`.
- **P03.2** `[T3; open]` Determine the additional hypotheses under which the
  regularized envelope is CLD-v2 psh for every such obstacle.
- **P03.3** `[T3; open]` For continuous finite obstacles, determine the
  additional hypotheses under which the regularized envelope is continuous.

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
remain active only beyond the reducible product obstruction and, for P03.1,
beyond the perfected-unibranch curve range; P03.3 is unchanged.  At the
earlier verification checkpoint the total was 53 active atoms in 14 formal
problem environments;
the later P07.2 and P08.2 retirements gave a total of 51 at that checkpoint.
The subsequent P05.3 and P05.4 retirements gave 49, and the P14.7
retirement gives the current total of 48.

For a fixed nonempty competitor family, the separate source-scoped
proposition `prop:p031-modulus-controlled-envelope-candidate` settles the
classical-psh and continuity conclusions whenever the functions are
finite-valued, their pointwise supremum is finite, and they have a common
local modulus. It passed independent verification as
`pi_2640874e3c1d992c29bd2646` with final `correct`, zero critical errors, and
zero gaps. This is not an automatic property of the full local-FS/PL
minorant family and makes no CLD-v2 assertion, so it narrows none of the
three P03 atoms beyond that stated family-level regime.

There is now an automatic-modulus invariant toric companion result for
P03.3.  On the
inverse image of an ordinary open convex subset of the dense tropical vector
space of a split torus, a finite continuous invariant obstacle has a finite,
continuous, locally psh-approximable raw envelope over all continuous
invariant psh minorants.  Under tropicalization it is the envelope of finite
convex minorants, and supporting affine functions prove that it equals the
smaller invariant toric real-PL envelope.  The lower bound from one
competitor and the upper obstacle bound make the tropical convex supremum
locally Lipschitz.  The exact source and scope ledger is
`solver_dossiers_20260909/p033_invariant_toric_convex_envelope_20260909/`.
It treats only that invariant psh competitor family, not all
local-FS/semipositive-real-PL minorants; P03.3 therefore remains active and
the inventory count is unchanged.

There is now a further source-scoped LFS-only refinement on every Euclidean
ball compactly contained in that split-toric chamber whose inverse image is
good, separated, strictly analytic, and boundaryless.  For a finite continuous
invariant obstacle, the local envelope of finite convex minorants is also
exactly the raw envelope over the invariant locally Fubini--Study minorants
alone.  Finite supporting planes on an exhausting family of closed subballs
are rounded from below to one character-lattice denominator at a time, so
their maxima remain below the obstacle and converge locally uniformly from
below to the convex envelope.  It excludes all noninvariant competitors and
all arbitrary upper-semicontinuous obstacles; P03.1--P03.3 and every inventory
count therefore remain unchanged.  The exact source and scope ledger is
`solver_dossiers_20260910/p033_invariant_toric_lfs_minorant_envelope_20260910/`.

The same finite continuous invariant envelope is also locally in the first
decreasing CLD-smooth psh stage by
cor:p024-invariant-toric-cld-smooth-regularization.  Thus this exact
invariant-toric chamber settles the finite-continuous-obstacle restricted
P03.1 classical-psh and P03.2 CLD-v2 assertions as well as the continuity
assertion.  It says nothing about arbitrary upper-semicontinuous obstacles
or the noninvariant local-FS/semipositive-real-PL envelope, so none of
P03.1--P03.3 retires.

On a good separated strict boundaryless pure-dimensional such toric domain,
the same envelope is exactly the raw envelope over the full
maximal-compact-torus-invariant part of the original
local-Fubini--Study/semipositive-real-PL competitor union.  Indeed, a
locally Fubini--Study function is real PL and semipositive at every point,
so that alternative contributes no functions outside the invariant
semipositive real-PL class; supporting affine functions give the reverse
comparison.  By the preceding first-stage result, this exact invariant
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

The source's only announced strict-positivity extension is an upcoming
sequel, whose own bibliography labels it ``In preparation.''  It is not an
available theorem for P05.1 or P05.2 and is therefore not used to narrow
either atom; see BMPS26, pp. 4 and 45.

### `prob:frontier-pluriharmonic` --- 2 atoms

- **P06.1** `[T2; open after the quasi-smooth, all strict-curve, arbitrary
  finite curve-factor, finite constant-group quotient, all-orbits split
  toric, split-toric quasi-smooth-product, algebraic-split toric-form,
  algebraic-split analytic-toric-form,
  algebraic-split-form quasi-smooth-product, transverse toric-product, and
  source-Zariski-local ordinary-etale algebraic-split-toroidal and analytic
  standard-etale algebraic-split-toroidal cases]` On a good,
  separated, strict, boundaryless analytic space, outside the local
  arbitrary-curve-factor scope of
  `thm:p061-arbitrary-curve-factors-ph-rpl` and the all-orbits split toric
  and algebraic-split-form scope of `thm:p061-split-toric-all-orbits` and
  `cor:p061-algebraic-split-toric-forms` and
  `cor:p061-algebraic-split-analytic-toric-forms`, and outside the split-toric quasi-smooth-product
  scope of `cor:p061-split-toric-quasismooth-products`, decide whether every
  classically pluriharmonic function is \(\mathbf R\)-PL near a
  non-quasi-smooth point of analytic dimension at least two.
- **P06.2** `[T2; open after the weakly smooth, real-PL, proper full-rank
  moment-factor, good-strict invariant split-toric (including boundary) and
  algebraic-split scalar-stable invariant-toric, including its analytic-local
  algebraic-split analytic-form version,
  algebraically closed closed-polydisc, arbitrary-field standard strict
  endpoint-polycylinder, arbitrary-radius scalar-stable endpoint-polycylinder,
  smooth-proper-curve, and strict-open-polydisc product or locally trivial
  bundle over published-curve and endpoint-polycylinder-base cases]` Decide
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
The quasi-smooth scope of P06.1 is settled by
`thm:p061-quasismooth-ph-rpl`: every classically pluriharmonic function on a
good strict quasi-smooth analytic space is \(\mathbf R\)-PL and GJR
harmonic, without global quasicompactness, separatedness, or
boundarylessness. The proof combines Temkin's altered local uniformization
with rigid étale sheaf descent. The published curve comparison already
covers all strict analytic curves, including singular and nonreduced ones
(`GR25Classical`, §4.1.2 and Proposition 3.15).
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
P06.1 remains active only for arbitrary nonproduct singular germs, products
containing higher-dimensional reduced singular factors outside the verified
ranges, genuinely log-etale charts not covered by an ordinary-etale chart of
the displayed kind or by the displayed analytic standard-etale chart, and
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

P06.2 remains one active T2 atom only for arbitrary analytic germs,
nonproduct local domains, equations known merely on the coordinatewise
strict radial core, and the classification of boundary-control hypotheses
weaker than scalar stability.  Higher-dimensional standard strict product
endpoints, the scalar-stable arbitrary-radius products, and the algebraic-split
scalar-stable invariant-toric range, including its analytic-local
algebraic-split analytic-form version, is removed from the residual; the
unrestricted arbitrary-radius version is disproved.  The
strict-open-disc descent proposition `prop:p062-open-disc-descent` also
shows that a continuous zero-current function on
\(B\times_KD_R^-\) is pulled back from a unique continuous zero-current
function on the good, topologically separated, pure strict base \(B\).
Iterating it over the published Wanner curve scope gives
`cor:p062-open-disc-products-over-curves`: all zero-current functions on a
finite product of that curve domain with standard strict open discs are
classically pluriharmonic.  The proof descends the equation by a normalized
compactly supported disc top form, rather than by an invalid current
pullback along the zero section.  The local product theorem globalizes by
`prop:p062-open-polydisc-bundle-descent`: on every locally trivial standard
strict open-polydisc bundle over a good separated strict pure-dimensional base,
a continuous zero-current function uniquely descends to a zero-current
function on the base.  In the published curve scope,
`cor:p062-open-polydisc-bundles-over-curves` then makes it classically
pluriharmonic, without a global section or product decomposition.  This does
not cover annular fibres, disc fibrations without the stated local product
charts, arbitrary nonproduct germs, or strict-core-only equations.  For a
positive-dimensional standard strict endpoint-polycylinder base,
`prop:p062-open-polydisc-bundle-endpoint-base` further identifies the descended
function with the affine combination of the base annular logarithms.  The
atom count, tier count, and queue position are unchanged.
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

- **P07.1** `[T2; open after the tropical-toric, finite ambient-star, two
  nonambient interval, exact CLD infinite-star, Stone--Euclidean,
  Stone--polyhedral, and generator-convex locally finite polyhedral-complex
  cases]`
  Decide whether the CLD psh hierarchy collapses after its first
  decreasing-limit stage.

Eventual cardinal stabilization is known.  Production run
`20260825T024707Z_d1b8d7eaf79e` controls the tropical toric case and the
historical narrower finite-curve statement.  The latter is superseded by the
exact finite ambient-induced real-affine-star theorem archived under
`20260827T103835Z_c8131b22d800`; the direct endpoint assigned no run or item
identifier and returned final `correct`, with zero critical errors and zero
gaps.

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
The locally finite extension
`cor:p071-locally-finite-generator-convex-collapse` is a formal local
consequence of the finite-complex theorem: its proof uses only one
generator-preserving convex chart with a finite local subdivision, so no
global finiteness is needed.  It retains the fixed-neighbourhood decreasing
smooth approximation at every germ, but asserts no global sequence.  The
verified two-ray example shows that face-to-face topological
unbranching plus independent cellwise positivity is insufficient: the
ambient affine generator `-x-y` unfolds to the nonconvex function `-|t|`.
Consequently the new theorem does not cover branched links, singular lower
links, or generator germs without a generator-preserving convex
development.  P07.1 remains one active T2 atom, and the active count and
tier counts are unchanged.

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
nonconstant affine parameter directions, and other nonambient local models
outside the two exact interval structures, \(X_B\), and the verified
locally constant-parameter models. The residual obstruction is sharpened
to the existence of a compatible local convex development and to
fixed-neighbourhood globalization beyond it, rather than diagonal order.
It remains active.

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

**Invariant projective toric global-smoothing range, 10 September 2026.**
`prop:p081-invariant-projective-toric-global-smoothing` settles the literal
CLD global-psh conclusion for a continuous maximal-compact-torus-invariant
locally CLD-psh metric on a concave toric line bundle over a projective split
toric variety with complete fan, in every dimension.  The proof applies the
finite continuous/local-psh-approximable equivalence of BGJKK Theorem 5.3.11
and its global decreasing smooth regularization in Corollary 5.4.5.  Dini's
theorem on the compact tropical toric variety upgrades the pointwise monotone
sequence to a uniform sequence, and surjective tropicalization transfers
that uniform convergence to the metrics.  This is a literal global smooth
psh approximation, rather than the separate fixed-line-bundle rational-model
comparison.  It requires torus invariance and a concave toric support
function; it gives no averaging or smoothing procedure for a noninvariant
metric.  P08.1 therefore remains active outside this range, with no change
to the atom or tier counts.

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

- **P12.1** `[T4; open]` Determine the normalizing boundary datum for
  excellent singular and nonnormal germs.
- **P12.2** `[T4; open]` Construct the corresponding valuative psh class.
- **P12.3** `[T4; open]` Construct its envelope theory.
- **P12.4** `[T5; open]` Construct model-independent bounded products.
- **P12.5** `[T5; open]` Construct a finite-energy theory.
- **P12.6** `[T4; open]` Establish finite-map functoriality, including
  branch and conductor descent.

All six targets are open.  The two BdFF local-volume questions recorded as
historical context in the chapter are resolved and are not atoms here.

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

### `prob:frontier-mp-pseff` --- 7 active atoms

- **P14.1** `[T4; open beyond established K\"ahler and projective regimes]` Intrinsically
  characterize the image of the raw ideal-valuative transform.  In the
  finite-energy K\"ahler domain, `cor:p141-finite-energy-raw-image` identifies
  that image exactly with the finite-energy MP cone.  For a connected smooth
  projective variety and an ample \(\mathbf Q\)-line-bundle class,
  `thm:pseff-projective-dxz-mp-bijection` identifies the literal raw transform
  on every semivaluation with the full MP cone, without a finite-energy
  hypothesis.  For a projective real N\'eron--Severi class, the full
  DXZ--Boucksom--Jonsson identification is known, but the literal
  ideal-valuative formula is asserted only in the \(\mathbf Q\)-line-bundle
  case.  The genuinely transcendental or nonprojective compact K\"ahler,
  and the big non-nef, image characterizations remain open.
- **P14.2** `[T3; open; source-closed production verification pending]` The
  audited Chapter 71 candidate proves upper semicontinuity at arbitrary
  nondivisorial semivaluations and has passed a zero-finding independent
  model-backed review of its frozen proof and five cited source extracts.
  The V7 local exact-live binding additionally replays the repaired V6
  source-stage candidate's manifest, release gates, and 179 tests, and pins
  its target statement, proof, and example to exact current Chapter 71
  excerpts.  The preceding independent V5 source-stage hostile audit instead
  returned `wrong`, with five critical errors and six gaps in the release and
  smoke-control evidence; V6 is only a local repair replay.  It is not the
  outstanding independent hostile audit, final-path smoke, or production
  verification.
  This atom remains active until source-closed production verification passes.
- **P14.3** `[T4; open; source-bound conditional theorem verified]` Decide
  MP positivity at those semivaluations.  The Chapter 71
  domination-preserving rational-divisorial theorem and its finite-energy
  K\"ahler corollary recover the all-point comparison from P14.2 upper
  semicontinuity and divisorial agreement.  Its frozen V3 source-bound
  packet embeds hashed MP24 and DXZ23 excerpts.  After its initial review,
  the same frozen V3 files passed an isolated `gpt-5.6-sol` / `xhigh`
  production review: final `correct`, zero critical errors, and zero gaps
  (`pi_75b42272e15105bb6be0525c`).  Its archived HTTP receipt and strict
  protocol audit are in `p143_v3_source_bound_packet_20260909/`
  `PRODUCTION_RECEIPT_SOL_20260909.md`.  It verifies only the conditional
  bridge: P14.2 upper semicontinuity and the finite-energy divisorial
  normalization are explicit premises.  The general MP-positivity problem
  remains open.  The historical local V4 exact-live audit records
  then-current Chapter 71 source ranges, the frozen V3 packet, and this
  live-open boundary; it is a local integrity check, rather than a
  replayable release pin or production verifier receipt.
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
  broader atom: P14.8 remains open, and this is not a zero-mass
  strict-interior range of the DXZ filtration curve.

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
its source-bound V6 successor, and its exact-live V7 audit are a source-scoped
answer to the two defined reconstruction readings, but they are not yet a
production-verified retirement and not a sourced second interval of zero-mass
slices.
The exact source comparison is preserved in
`solver_dossiers_20260831/p147_source_correction_independent_audit_20260831/SOURCE_CORRECTION_AUDIT.md`.
That source-only correction did not itself retire an atom; the complete
proof integrated in Chapter 71 is the retirement basis used here.

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
  boundary strata, but requires finite maximal-compact-torus invariant
  continuous psh potentials.
  There is an exact sufficient bridge in the remaining scope: if the
  zero-Hessian difference of a continuous psh pair is locally uniformly
  approximable by smooth zero-Hessian functions, then
  `cor:ch16-local-pluriharmonic-criterion` gives the required independence for
  every positive closed current.  A further pairwise class is now closed:
  when that difference locally factors through a proper full-rank moment
  satisfying every hypothesis of `prop:p062-proper-full-rank-moment`, its
  affine source formula makes it smooth with zero Hessian, and
  `cor:ch18-local-proper-full-rank-moment-bt` gives the required independence.
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
  P21.3 corollary.
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
environments and 54 atoms.  After the 30 August retirements recorded above
and the P14.7 retirement, the current inventory is 14 formal environments
and 48 atoms.

## Easy-to-hard Rethlas queue

The tiers estimate how bounded the first exact submission can be, not the
probability that its expected answer is affirmative.  A verified
counterexample retires an atom just as a verified proof does.

### T1 --- concrete first submissions (0 atoms)

No active atom remains in this tier after retirement of `P01.1`.

### T2 --- focused problems with one principal missing bridge (5 atoms)

`P21.3`, `P07.1`, `P06.1`, `P06.2`, `P03.1`.

### T3 --- major theorems within mature frameworks (9 atoms)

`P02.1`, `P02.2`, `P02.3`, `P05.1`, `P05.2`,
`P08.1`, `P14.2`, `P03.2`,
`P03.3`.

### T4 --- new comparison theories or several coupled inputs (17 atoms)

`P02.4`, `P04.1`, `P04.2`, `P05.5`, `P12.1`, `P12.2`, `P12.3`,
`P12.6`, `P13.1`, `P13.2`, `P14.1`, `P14.3`, `P14.4`, `P15.3`,
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
