# Atomic crosswalk for the active problem environments

**Inventory date:** 30 August 2026
**Literature cutoff:** 24 August 2026
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
continuity theorem,
the exact count is

```text
14 formal problem environments = 53 active atomic research questions.
Tier counts: (T1,T2,T3,T4,T5) = (0,5,14,17,17).
```

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

### `prob:frontier-unibranch-local-envelope` --- 3 atoms

- **P03.1** `[T2; open]` Classify the higher-dimensional and remaining
  singular hypotheses, and determine necessity, under which usc
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
relative boundary.  P03.1 remains active only beyond this curve range and
for sharp necessity; P03.2 and P03.3 are unchanged.  The total remains 53
active atoms in 14 formal problem environments.

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

### `prob:frontier-polyhedral-regularity` --- 5 atoms

- **P05.1** `[T3; open]` Characterize the pairs \((\mathbf X,\gamma)\) for
  which the Botero--Mazzon--Pille-Schneider regularity property holds.
- **P05.2** `[T3; open]` Characterize the pairs for which their
  orthogonality property holds.
- **P05.3** `[T3; open]` Under realizability, compare the polyhedral
  Monge--Amp\`ere operator with the CLD operator.
- **P05.4** `[T3; open]` Under realizability, compare it with the delta-form
  operator.
- **P05.5** `[T4; open]` Under realizability, compare it with the
  non-Archimedean Monge--Amp\`ere operator.

Complete affine space, the exact normalization, and the abstract cross-fan
counterexample are verified.  The recursive analytic comparison is only
conditional; the general targets remain open.

### `prob:frontier-pluriharmonic` --- 2 atoms

- **P06.1** `[T2; open after the quasi-smooth, all strict-curve, arbitrary
  finite curve-factor, finite constant-group quotient, split simplicial
  toric-domain, and affine-toric fixed-point cases]` On a good,
  separated, strict, boundaryless analytic space, outside the local
  arbitrary-curve-factor scope of
  `thm:p061-arbitrary-curve-factors-ph-rpl`, the split simplicial toric
  scope of `thm:p061-simplicial-toric-ph-rpl`, and the exact toric
  fixed-point scope of `thm:p061-toric-fixed-point-constancy`, decide whether every
  classically pluriharmonic function is \(\mathbf R\)-PL near a
  non-quasi-smooth point of analytic dimension at least two.
- **P06.2** `[T2; open after the weakly smooth, real-PL, proper full-rank
  moment-factor, algebraically closed strict-polydisc, arbitrary-field
  one-dimensional strict-disc, and smooth-proper-curve cases]` Decide
  whether an arbitrary
  continuous function with zero
  \(\mathrm d'\mathrm d''\)-current is classically pluriharmonic, or
  harmonic whenever the classical notion is available, outside the verified
  strict-polydisc, factorized, and curve scopes, with the arbitrary-field
  higher-dimensional and arbitrary-germ residual boundaries stated below.

The weakly smooth zero-current statement is known.  The real-PL
zero-current implication is now verified on good separated boundaryless
strict pure-dimensional spaces by production run
`20260825T061351Z_655e7f503e5d`: it uses rational coefficients of calibrated
skeletal currents and does not extend to arbitrary continuous functions.
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
The atom remains active only outside the split simplicial toric-domain
scope and the other verified scopes listed above; in particular, the
non-simplicial, nonsplit, and general toroidal residuals are unchanged.
The coefficient cannot be strengthened: `prop:p061-integral-pl-counterexample`
gives \(\sqrt2\log|T|\) on a strict semistable annulus, which is not
\(\mathbf Q\)-PL. The exact statement and proof passed production Rethlas
run `20260829T043457Z_0b1b4d161e3b`, item
`pi_7cd35ebd843cf80a7cd696bb`, final `correct`, with zero critical errors
and zero gaps. P06.1 remains one active T2 atom, now confined to arbitrary
nonproduct non-quasi-smooth points in dimension at least two outside the
verified quotient range, products containing a reduced singular factor of
dimension at least two outside that range, non-simplicial positive-orbit
toric domains, nonsplit toric forms, and general toroidal or log-etale
charts. No atom count, tier count, or queue position
changes.
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
arbitrary analytic germ.  Hence P06.2 remains one active T2 atom and the
total remains 53.
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

### `prob:frontier-cld-hierarchy` --- 2 atoms

- **P07.1** `[T2; open]` Decide whether the CLD psh hierarchy collapses after
  its first decreasing-limit stage.
- **P07.2** `[T3; open]` If not, determine whether a finite or otherwise
  uniformly controlled early ordinal works on a natural class of affine
  tropical spaces.

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

P07.1 therefore retains arbitrary higher-dimensional settings and other
nonambient local models outside the two exact interval structures and
\(X_B\), with the residual obstruction sharpened to fixed-neighbourhood
globalization rather than diagonal order.  P07.2 retains the absence of a
uniform early-ordinal bound.  Both atoms remain active.  The controlling
P17.1 retirement addendum below gives the current total of 53 atoms in 14
formal problem environments, with tier counts `(0,5,14,17,17)`.

### `prob:frontier-cld-global-metric` --- 2 atoms

- **P08.1** `[T3; open beyond the verified smooth algebraically closed
  curve scope]` Decide whether a continuous locally CLD-psh metric on a
  projective non-Archimedean variety is globally psh in the Fubini--Study
  or nef-model sense outside the curve scope stated below.
- **P08.2** `[T3; open beyond the verified algebraic and strict analytic
  smooth-curve scope]`
  Prove or disprove the corresponding global approximation statement on a
  proper strict analytic space admitting a formal model with projective
  special fibre.

The smooth proper algebraic curve case over an algebraically closed complete
nontrivially valued field is now verified by
`thm:p081-curve-local-global`. A continuous locally CLD-psh metric has
nonnegative degree and is a uniform limit of semipositive Q-formal metrics,
equivalently semipositive algebraic model metrics. In positive degree the
approximants may be chosen relatively ample and the metric lies in the
uniform Fubini--Study closure; in degree zero its curvature vanishes and
the approximants may be chosen numerically trivial. The exact
statement/proof SHA-256 values are
`1f2c51f101fd8447fbb6b65a3c0686515efaf982674efaadcaf2271079173e93`
and
`9847a08c98a640ee7def082a73cc1b3ff116980f2882920808557822056f0f2f`.
An independent hostile audit passed. A dependency-closed production
request using `gpt-5.6-sol` at `xhigh` returned final `correct`, zero
critical errors, and zero gaps; the archived request/response/header
SHA-256 values are
`307ba899872bfd33720dd863bd58269820d5c0687b848760afef960cb549c7cd`,
`7af690cea941960fc8c8bfba39acfacd6cbf0bbe8bf52273431b93945d1af0af`,
and
`c2d6c04bd79ddd90ddd7e91a6c6bbf64282d5f7cd193bb1e682ff9c89d8d69a3`.
The same conclusions now hold for every smooth proper connected strict
analytic curve over the same field, without assuming beforehand that it has
a formal model with projective special fibre.  The exact transfer statement
and proof, SHA-256
`64e507146c65614e37d831a25d230f1bb05cdf4decc25f298f4adbea22f4c9da`
and
`8b0c95bc1b4822cd29560b8f8045f53ab09281131c59c1bfb4dbf9770cf546de`,
use strict Berkovich--rigid comparison, projective curve algebraization, and
proper GAGA for the line bundle.  An independent hostile audit passed.  The
dependency-closed production request using `gpt-5.6-sol` at `xhigh`
returned final `correct`, zero critical errors, and zero gaps; its
request/response/header SHA-256 values are
`492ed02879f4f2b3346e8389996f259a5a665f85bb521f4f425ace93d6879f60`,
`fb038501912bea4c1d6d816d5188e08b3249b016a00d7331d4fcfc56da78ba00`,
and
`176e7a69175ba6de0ce09be2633852742af43e415cbf283ad51991fbddf084e0`.

P08.1 retains higher dimension, singular curves, and arbitrary complete
ground fields. P08.2 retains higher-dimensional proper strict analytic
spaces, singular analytic curves, and the general-field and trivially
valued ranges.  No smooth strict-curve residual remains under the verified
field hypotheses, but neither atom is retired; the count and tier
distribution are unchanged.

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

### `prob:frontier-mp-pseff` --- 8 atoms

- **P14.1** `[T4; open]` Intrinsically characterize the image of the raw
  ideal-valuative transform.
- **P14.2** `[T3; open]` Decide upper semicontinuity at arbitrary
  nondivisorial semivaluations.
- **P14.3** `[T4; open]` Decide MP positivity at those semivaluations.
- **P14.4** `[T4; open]` Construct a \(P\)-sensitive positivity theory for
  big non-nef classes.
- **P14.5** `[T5; open]` Construct the corresponding Monge--Amp\`ere
  measure theory.
- **P14.6** `[T5; open]` Construct the corresponding energy theory.
- **P14.7** `[T3; open]` Prove maximality of DXZ filtration test curves in
  the positive-mass range.
- **P14.8** `[T5; open]` Recover an \(\mathcal I\)-model potential from
  zero-mass filtration data.

The divisorial realization, the finite-energy K\"ahler comparison, and the
projective real N\'eron--Severi DXZ--Boucksom--Jonsson comparison are known
in their stated domains.  The eight residual targets above remain open.

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

### `prob:frontier-general-ma` --- 7 atoms

Each atom asks for the finite-energy Monge--Amp\`ere operator and the
corresponding existence-and-uniqueness theorem after removing one indicated
restriction.

- **P16.1** `[T5; open]` Singular or unibranch varieties.
- **P16.2** `[T5; open]` Nonprojective but algebraizable proper settings.
- **P16.3** `[T5; open]` Positive residue characteristic.
- **P16.4** `[T4; open]` Nondiscrete valuations and arbitrary complete
  non-Archimedean fields.
- **P16.5** `[T5; open]` Big or pseudoeffective nonample positivity classes.
- **P16.6** `[T4; open]` Arbitrary finite-energy measure support.
- **P16.7** `[T5; open]` Genuinely nonalgebraizable analytic spaces.

Strictly delimited endpoints are known.  The unrestricted axes remain open,
and known nonskeletal examples rule out a general reduction to one
skeleton or to rational PL potentials.

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
open atoms.  The four corrected residual targets above remain open.

### `prob:frontier-cross-fan-upstairs` --- 1 atom

- **P21.3** `[T2; open residual]` In analytic dimension at least two,
  determine whether every positive closed CLD current of bidegree
  \((p,p)\), \(0\le p\le n-1\), on a good separated strict boundaryless
  pure \(n\)-dimensional analytic space has Bedford--Taylor independence for
  continuous psh pairs of equal curvature, or construct a counterexample.
  The entire one-dimensional case inside these ambient hypotheses is settled
  by `prop:p213-componentwise-arbitrary-valuation`, over either a trivial or
  nontrivial valuation and without reducedness or normalization-smoothness
  assumptions.  The literal discontinuous-potential predicate of CLD
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
environments and 54 atoms.  After the 30 August P17.1 retirement recorded
above, the current inventory is 14 formal environments and 53 atoms.

## Easy-to-hard Rethlas queue

The tiers estimate how bounded the first exact submission can be, not the
probability that its expected answer is affirmative.  A verified
counterexample retires an atom just as a verified proof does.

### T1 --- concrete first submissions (0 atoms)

No active atom remains in this tier after retirement of `P01.1`.

### T2 --- focused problems with one principal missing bridge (5 atoms)

`P21.3`, `P07.1`, `P06.1`, `P06.2`, `P03.1`.

### T3 --- major theorems within mature frameworks (14 atoms)

`P02.1`, `P02.2`, `P02.3`, `P05.1`, `P05.2`, `P05.3`, `P05.4`,
`P07.2`, `P08.1`, `P08.2`, `P14.2`, `P14.7`, `P03.2`,
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
