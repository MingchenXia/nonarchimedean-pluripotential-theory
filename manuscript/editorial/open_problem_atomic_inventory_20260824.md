# Atomic crosswalk for the active problem environments

**Inventory date:** 25 August 2026
**Literature cutoff:** 24 August 2026
**Source scope:** the formal `problem` environments in Chapters 71 and 72

This file is an editorial crosswalk for solving, verifying, and retiring the
problems that are formally displayed in the book.  It is not an exercise
list, and it is not a claim that the displayed problems form a complete list
of the open problems in non-Archimedean pluripotential theory or in the
surrounding literature.

## Counting method

The current source contains exactly seventeen formal problem environments:
one in Chapter 71 and sixteen in Chapter 72.  A compound environment is
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
and positive-cone counterexample,
the exact count is

```text
17 formal problem environments = 57 active atomic research questions.
```

The identifiers `P00.1` through `P21.3` below are an editorial addressing
scheme.  The prefix records the formal environment, not a theorem number in
the book.

## Atomic inventory

### `prob:pseff-projective-rational-full-link` --- 1 atom

- **P00.1** `[T2; open]` Decide whether, for an ample rational class, the
  full Mesquita--Piccione psh cone agrees on all semivaluations with the full
  Boucksom--Jonsson psh cone, without a finite-energy hypothesis.  The
  finite-energy comparison is known; the unrestricted comparison is open.

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

- **P03.1** `[T2; open]` Classify the hypotheses, beginning with normal or
  analytically unibranch good strict domains, under which usc regularization
  of every upper-semicontinuous local FS/semipositive-PL obstacle envelope is
  classically psh.
- **P03.2** `[T3; open]` Determine the additional hypotheses under which the
  regularized envelope is CLD-v2 psh for every such obstacle.
- **P03.3** `[T3; open]` For continuous finite obstacles, determine the
  additional hypotheses under which the regularized envelope is continuous.

The continuous obstacle on the reduced strict nodal affinoid curve in
`prop:ch15-nodal-local-envelope` disproves all three unconditional universal
assertions, but it does not answer these classification questions.
Its exact statement and proof passed production run
`20260825T094005Z_10ac70696f69`, item
`pi_31f95353b7e94f3cb98b09b6`, final `correct`, with zero critical errors
and zero gaps.  If the raw envelope is already usc, the classical-psh
conclusion remains valid.  No positive classification on normal or
analytically unibranch domains is inferred.

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

### `prob:frontier-pluriharmonic` --- 3 atoms

- **P06.1** `[T2; open]` Decide whether every classically pluriharmonic
  function is PL without the extra regularity assumptions in the cited
  result.
- **P06.2** `[T2; open after the real-PL case]` Decide whether an arbitrary
  continuous function with zero
  \(\mathrm d'\mathrm d''\)-current is classically pluriharmonic, or
  harmonic whenever the classical notion is available.
- **P06.3** `[T2; open after the literal harmonic variant]` Decide whether
  every continuous current-psh function on every smooth proper Berkovich
  curve in the stated Wanner scope is locally a decreasing limit of ordinary
  CLD-smooth psh functions, without the supplementary hypotheses of Wanner
  Corollary 5.4.

The weakly smooth zero-current statement is known.  The real-PL
zero-current implication is now verified on good separated boundaryless
strict pure-dimensional spaces by production run
`20260825T061351Z_655e7f503e5d`: it uses rational coefficients of calibrated
skeletal currents and does not extend to arbitrary continuous functions.
The former literal request for ordinary CLD-smooth harmonic approximants is
disproved by exact-live production run `20260825T055907Z_b5c8f0719b60`;
positive-curvature psh approximants are not covered.  Wanner's
published comparison settles the continuous problem on open subsets of
smooth proper algebraic curves over algebraically closed complete
nontrivially valued fields.  The three atoms retain the residual scopes
stated above.

### `prob:frontier-cld-hierarchy` --- 2 atoms

- **P07.1** `[T2; open]` Decide whether the CLD psh hierarchy collapses after
  its first decreasing-limit stage.
- **P07.2** `[T3; open]` If not, determine whether a finite or otherwise
  uniformly controlled early ordinal works on a natural class of affine
  tropical spaces.

Eventual cardinal stabilization is known.  Production run
`20260825T024707Z_d1b8d7eaf79e` proves stage-one collapse on tropical toric
partial compactifications and on finite-valence boundaryless
one-dimensional affine tropical spaces with ambient-induced smooth
structure.  The two atoms retain only higher-dimensional arbitrary balanced
spaces, tropical boundary points, infinite-valence stars, and the absence of
a uniform general bound.

### `prob:frontier-cld-global-metric` --- 2 atoms

- **P08.1** `[T3; open]` Decide whether a continuous locally CLD-psh metric
  on a projective non-Archimedean variety is globally psh in the
  Fubini--Study or nef-model sense.
- **P08.2** `[T3; open]` Prove or disprove the corresponding global
  approximation statement on a proper strict analytic space admitting a
  formal model with projective special fibre.

Agreement is known on the common model loci.  Both unrestricted global
statements are open.

### `prob:frontier-gjr-remaining` --- 1 atom

- **P09.2** `[T3; open]` Determine whether the canonical metric on an
  abelian variety is an ordinary delta-metric rather than merely weakly
  smooth.

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

### `prob:frontier-banach-family-ma` --- 1 atom

- **P17.1** `[T2; open]` Prove or disprove continuity of the fibrewise mixed
  Monge--Amp\`ere integral over a general integral Banach ring.  The hybrid
  base case is known; the general Banach-base statement is open.

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

- **P21.3** `[T2; open]` Construct a good strict analytic space, a positive
  closed order-zero analytic or delta-current \(T\), and continuous psh
  functions \(U,V\) with equal analytic curvature currents but
  \(\mathrm d'\mathrm d''((U-V)T)\ne0\), or prove that the available
  analytic and delta-currents force Bedford--Taylor compatibility.

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

## Easy-to-hard Rethlas queue

The tiers estimate how bounded the first exact submission can be, not the
probability that its expected answer is affirmative.  A verified
counterexample retires an atom just as a verified proof does.

### T1 --- concrete first submissions (0 atoms)

No active atom remains in this tier after retirement of `P01.1`.

### T2 --- focused problems with one principal missing bridge (8 atoms)

`P21.3`, `P07.1`, `P00.1`, `P17.1`, `P06.1`, `P06.2`, `P06.3`,
`P03.1`.

### T3 --- major theorems within mature frameworks (15 atoms)

`P02.1`, `P02.2`, `P02.3`, `P05.1`, `P05.2`, `P05.3`, `P05.4`,
`P07.2`, `P08.1`, `P08.2`, `P09.2`, `P14.2`, `P14.7`, `P03.2`,
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
