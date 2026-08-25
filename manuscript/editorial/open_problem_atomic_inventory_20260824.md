# Atomic crosswalk for the active problem environments

**Inventory date:** 24 August 2026
**Literature cutoff:** 24 August 2026
**Source scope:** the formal `problem` environments in Chapters 71 and 72

This file is an editorial crosswalk for solving, verifying, and retiring the
problems that are formally displayed in the book.  It is not an exercise
list, and it is not a claim that the displayed problems form a complete list
of the open problems in non-Archimedean pluripotential theory or in the
surrounding literature.

## Counting method

The current source contains exactly twenty-one formal problem environments:
one in Chapter 71 and twenty in Chapter 72.  A compound environment is
split below into independently auditable theorem or construction targets.
Equivalent reformulations are counted only once.  The compatibility axioms
that make a construction meaningful---for example model independence,
monotone continuity, locality, and functoriality for a local
Monge--Amp\`ere product---are acceptance conditions for that construction,
not artificial extra atoms.  Known boundary cases and counterexamples are
reported in the status notes but are not counted as active atoms.

After deletion of the unrestricted Gubler--Jell--Rabinoff cohomological
isomorphism question, which is negatively answered in the book, and the
generalized-Lelong separation question, which is proved in
`thm:local-generalized-lelong-separation`, the exact count is

```text
21 formal problem environments = 63 active atomic research questions.
```

The identifiers `P00.1` through `P21.2` below are an editorial addressing
scheme.  The prefix records the formal environment, not a theorem number in
the book.

## Atomic inventory

### `prob:pseff-projective-rational-full-link` --- 1 atom

- **P00.1** `[T2; open]` Decide whether, for an ample rational class, the
  full Mesquita--Piccione psh cone agrees on all semivaluations with the full
  Boucksom--Jonsson psh cone, without a finite-energy hypothesis.  The
  finite-energy comparison is known; the unrestricted comparison is open.

### `prob:frontier-current-pullback` --- 1 atom

- **P01.1** `[T1; open]` Decide whether positivity of
  \(\mathrm d'\mathrm d''[h]\) for a real PL function forces residue-nef,
  equivalently model-semipositive, behaviour.  The converse and an exact
  conditional curve reduction are known; a coarse tropical restriction
  principle is disproved, while the analytic converse remains open.

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

### `prob:frontier-local-envelope` --- 3 atoms

- **P03.1** `[T2; open]` Determine when the usc regularization of the local
  FS/semipositive-PL envelope is classically psh.
- **P03.2** `[T3; open]` Determine when it is CLD-v2 psh.
- **P03.3** `[T3; open]` Determine when it is continuous.

If the raw envelope is already usc, the classical-psh conclusion is
verified.  The unrestricted regularized-envelope targets remain open.

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
- **P06.2** `[T2; open]` Decide whether a continuous function with zero
  \(\mathrm d'\mathrm d''\)-current is classically pluriharmonic, or
  harmonic whenever the classical notion is available.
- **P06.3** `[T2; open]` Prove or disprove decreasing regularization on every
  smooth Berkovich curve by CLD-smooth harmonic approximants.

The weakly smooth zero-current statement is known; these three upgrades are
open.

### `prob:frontier-cld-hierarchy` --- 2 atoms

- **P07.1** `[T2; open]` Decide whether the CLD psh hierarchy collapses after
  its first decreasing-limit stage.
- **P07.2** `[T3; open]` If not, determine whether a finite or otherwise
  uniformly controlled early ordinal works on a natural class of affine
  tropical spaces.

Eventual cardinal stabilization is known.  Early analytic collapse and a
uniform early bound remain open.

### `prob:frontier-cld-global-metric` --- 2 atoms

- **P08.1** `[T3; open]` Decide whether a continuous locally CLD-psh metric
  on a projective non-Archimedean variety is globally psh in the
  Fubini--Study or nef-model sense.
- **P08.2** `[T3; open]` Prove or disprove the corresponding global
  approximation statement on a proper strict analytic space admitting a
  formal model with projective special fibre.

Agreement is known on the common model loci.  Both unrestricted global
statements are open.

### `prob:frontier-gjr-remaining` --- 2 atoms

- **P09.1** `[T2; open]` Determine whether the local finite integral
  decomposition of harmonic PL functions has a semipositive analogue in
  arbitrary residual dimension.  The natural positive-cone formulation is
  now proved when the residual dimension is at most one, including all good
  strict analytic curves.
- **P09.2** `[T3; open]` Determine whether the canonical metric on an
  abelian variety is an ordinary delta-metric rather than merely weakly
  smooth.

Both unrestricted questions are open.  The formerly bundled unrestricted
cohomological isomorphism question is not active: the book gives a
good-reduction elliptic-curve counterexample to surjectivity.  This negative
answer does not settle the separately restricted totally degenerate case,
which is not a formal problem environment here.

### `prob:frontier-bj-radon-riesz` --- 1 atom

- **P11.1** `[T2; open]` Decide whether weak convergence together with
  convergence of the Boucksom--Jonsson exhaustion implies strong
  \(d_{\infty,\omega}\)-convergence on all of \(X^{\mathrm{lin}}\).
  The fixed-snc-complex characteristic-zero case is verified; the global
  statement remains open.

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

### `prob:frontier-favre-hybrid-extension` --- 1 atom

- **P18.1** `[T2; open]` Decide whether continuous Archimedean and
  non-Archimedean endpoint metrics force continuity of the glued hybrid
  metric.  The psh property and special semistable canonical cases are
  known; general continuity is open.

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

### `prob:frontier-real-toric` --- 1 atom

- **P20.1** `[T1; open]` Prove or disprove
  \(\nu(T)=\dim\Delta(T)\) for a torus-invariant positive current in a big
  irrational real class, with numerical dimension defined by real positive
  products.  The integral and rational cases are verified; the irrational
  real case is open.

### `prob:frontier-cross-fan` --- 2 atoms

- **P21.1** `[T1; open]` Realize the verified weighted cross-fan as a
  harmonic tropicalization of a good strict analytic space, or prove a
  realization obstruction.
- **P21.2** `[T2; open]` Realize the displayed weights by a positive closed
  analytic or delta-current, or prove a multiplicity obstruction.

The abstract calibrated fan counterexample is verified.  Both analytic
realization targets remain open.

## Easy-to-hard Rethlas queue

The tiers estimate how bounded the first exact submission can be, not the
probability that its expected answer is affirmative.  A verified
counterexample retires an atom just as a verified proof does.

### T1 --- concrete first submissions (3 atoms)

Recommended internal order:

1. `P20.1`
2. `P21.1`
3. `P01.1`

### T2 --- focused problems with one principal missing bridge (11 atoms)

`P21.2`, `P11.1`, `P07.1`, `P00.1`, `P17.1`, `P18.1`, `P03.1`,
`P06.1`, `P06.2`, `P06.3`, `P09.1`.

### T3 --- major theorems within mature frameworks (15 atoms)

`P02.1`, `P02.2`, `P02.3`, `P03.2`, `P03.3`, `P05.1`, `P05.2`,
`P05.3`, `P05.4`, `P07.2`, `P08.1`, `P08.2`, `P09.2`, `P14.2`,
`P14.7`.

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
