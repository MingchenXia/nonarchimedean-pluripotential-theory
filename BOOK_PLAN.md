# Non-Archimedean Pluripotential Theory

## Detailed research and writing plan

**Provisional subtitle:** *Local Calculus, Global Energies, and Complex Degenerations*  
**Planning date:** 14 August 2026  
**Status:** approved and implemented in the complete first draft; the future
tense below is retained as the historical writing specification.  Current
release gates are tracked in `manuscript/editorial/chapter_status.md`.  
**Primary source manuscripts:**

- `Singularities_in_global_pluripotential_theory_Final.zip`;
- `The_envelope_property_for_unibranch_projective_varieties.zip`.

This document plans one logical monograph. At the projected length, it would be
most usable as two physical volumes with continuous numbering:

- **Volume I:** foundations, Chambert--Loir--Ducros, and the
  Boucksom--Favre--Jonsson theory;
- **Volume II:** the trivially valued theory, the complete envelope theorem,
  complex/transcendental theories, and comparison theorems.

The division is editorial only: notation, bibliography, cross-references, and
the mathematical narrative will be unified.

---

## Supplied P08.1 counterexample integrated on 25 September 2026

The author-supplied *A locally plurisubharmonic metric without any global
smooth plurisubharmonic metric* is integrated with its complete argument in
Chapter 17.  On a constant good-reduction elliptic curve over `C((t))`, a
non-torsion degree-zero line bundle has a continuous locally ordinary-CLD-psh
nef integral model metric but no globally ordinary smooth psh metric.  The
outgoing-slope divisor makes the obstruction explicit, and the proof also
constructs smooth psh approximants on a fixed neighborhood of the
good-reduction point.

This gives a negative answer to the literal first question in CLD Remark
17.8.10 and retires P08.1.  The inventory is now **42 active atoms in 12
formal problem environments**, tiers **(0,3,7,15,17)**.  The original PDF,
source correction and two-pass integration review are recorded separately;
no earlier verification receipt is extended to the edited book bytes.

## Supplied P05.2 one-vertex real-PA criterion integrated on 25 September 2026

The author-supplied *Orthogonality on one-dimensional balanced fans* is
integrated in Chapter 72 after an essential convention repair.  For a balanced
rational fan made of finitely many rays from one vertex, real-polyhedral
orthogonality holds exactly when the cone of nonnegative balancing relations
is one-dimensional.  The explicit higher-rank obstacle and nonsaturated
tripod are retained, and bounded reference shift extends the criterion to
every real-piecewise-affine polyhedrally convex reference positive at
infinity.

The literal integral-slope PA class in BMPS Definition 2.28 is not closed
under the envelopes asserted in Proposition 6.13; Chapter 72 gives the
explicit real-line slope-$1/2$ counterexample.  Thus this classifies the
real scalar extension, not the literal integral-slope P05.2 formulation.
The book-local contact argument now also covers every one-dimensional
balanced graph whose cone of nonnegative balancing relations is
one-dimensional at each vertex.  It allows bounded edges and cycles, hence
includes all bivalent/trivalent balanced graphs without lattice saturation.
The converse at higher-rank vertices and higher dimensions remain open.
P05.2 stays active;
the inventory remains **42 active atoms in 12 formal problem environments**,
tiers **(0,3,7,15,17)**.

## Supplied solutions integrated on 24 September 2026

Six distinct supplied papers are integrated with complete arguments in
Chapters 15, 16, 18 and 70. P06.1 is settled for arbitrary singularities in
its original good, separated, strict, boundaryless, nontrivially valued
scope. P07.1 is false for general affine G-tropical spaces and true for good
separated analytic spaces; the arbitrary-star product theorem applies at
node tuples. These two atoms are retired: **43 active atoms in 13 formal
problem environments**, tiers **(0,3,8,15,17)**.

The codimension-two envelope obstruction narrows P03.1. The continuous and
ideal-generated finite-transfer calculus, including normal nonflat targets
and conductor descent, narrows P12.6. The full-polycylinder proof adds an
independent argument in an already established P21.3 range. Those three
atoms and P06.2 remain active. Supplied manuscripts, archived Xean evidence,
two local checks and historical production receipts have distinct scopes;
no new production or independent-agent verdict is asserted. See
`manuscript/editorial/supplied_solutions_integration_audit_20260924.md`.

## Current local-boundary result: 23 September 2026

The author-supplied normalized-valuation-links manuscript is integrated in
the live Chapter 70. It settles P12.1 for excellent local germs through
primary normalized sections, their exact radial changes, and the quotient
of normalization branches along the conductor. Nonprimary sections and
nilpotent reduction are explicit. Chapter 72 and the atomic inventory now
retain five singular-local targets, P12.2--P12.6; this boundary result does
not construct their psh, envelope, product, energy or finite-map theory.
The source and the two-pass local review are recorded in
`manuscript/editorial/p121_integration_audit_20260923.md`; no new production
verifier or independent-agent receipt is asserted.

## 1. Aim and governing principles

The book will explain non-Archimedean pluripotential theory through four
constructions that are often learned separately:

1. the **local differential and current-theoretic calculus** of
   Chambert--Loir--Ducros (CLD);
2. the **model-theoretic and variational theory over a nontrivially valued
   field** initiated by Boucksom--Favre--Jonsson (BFJ);
3. the **global homogeneous theory over a trivially valued field** of
   Boucksom--Jonsson (BJ), including the now-proved envelope property;
4. the **non-Archimedean geometry attached to complex and compact Kähler
   spaces**, in the test-curve approach of Darvas--Xia--Zhang/Xia and in the
   tropical-spectrum approach of Mesquita-Piccione, including the later
   Calabi--Yau theory of Mesquita-Piccione--Witt Nyström.

The organizing problem is not merely to present four theories, but to state
and prove every comparison that is valid between them, with exact hypotheses.
The central leitmotif is

\[
  \text{models and vertical divisors}
  \longleftrightarrow
  \text{piecewise affine potentials on skeleta}
  \longleftrightarrow
  \text{semipositive metrics}
  \longleftrightarrow
  \text{positive currents and Monge--Ampère measures}.
\]

### 1.1 Mathematical standards

- Every theorem carries a visible hypothesis signature: base field,
  characteristic, valuation, singularities of the space, positivity of the
  class, and regularity/energy of the potential.
- Original BFJ assumptions are distinguished from later extensions. In
  particular, the first BFJ existence theorem is not silently presented as a
  theorem over an arbitrary complete field.
- Results are proved at the greatest generality for which a complete proof can
  be supplied and checked. Broader variants are stated only with a precise
  citation and an explanation of what changes.
- Model, continuous, bounded, and finite-energy Monge--Ampère products are
  never conflated.
- Sequences are not substituted for nets unless first countability,
  metrizability, or a Choquet reduction has been proved.
- Expressions involving `-infinity`, undefined differences, zero masses, and
  pullbacks through singular spaces receive explicit conventions.
- New proof claims arising from the research programme in Section 10 enter
  the book only after a solver pass, an independent hostile audit, examples,
  and a source/hypothesis audit.

### 1.2 Pedagogical standards

The intended reader is a graduate student with a first course in algebraic
geometry or complex geometry, but not necessarily prior knowledge of
Berkovich spaces. The main text will therefore:

- motivate each new category of objects before formal construction;
- introduce one running degeneration of a curve and one toric example in
  Part I and revisit them throughout;
- place a concrete example immediately after most foundational definitions;
- begin every part and chapter with a roadmap and a dependency paragraph;
- split long proofs into named steps and isolate the geometric idea before
  technical estimates;
- end each chapter with a short dictionary of the newly established
  correspondences and a historical/source note;
- use no routine exercise lists in the first draft, matching the supplied
  manuscript, but include fully worked examples and proof checkpoints.

The target is self-containedness of the theory rather than self-containedness
of all of algebraic geometry. Deep general facts about schemes may be cited to
stable Stacks Project tags; deep complex pluripotential preliminaries may be
cited to the supplied book after their interfaces and normalizations have been
restated.

---

## 2. Style inherited from the supplied book

The new text will be written afresh but will retain the following structural
features of *Singularities in Global Pluripotential Theory*:

- Springer `svmono` architecture, `newtxtext/newtxmath`, theorem numbering by
  section, an alphabetic bibliography, and a detailed subject index;
- part introductions that explain dependencies and alternate reading routes;
- dense but disciplined cross-referencing;
- a definition--lemma--proposition--theorem cadence, with examples and remarks
  placed close to the point of use;
- exact normalizations and explicit treatment of limiting and infinite cases;
- source attributions in theorem headings when a result is imported;
- step-labelled long proofs;
- optional chapter mottos in the source, disabled in the default build so that
  the mathematical edition remains neutral;
- a mathematical revision log recording repaired gaps, changed hypotheses,
  and results omitted from the final text.

The orphaned Section 11.3 in the first archive was intentionally removed there
because of a proof gap. It will not be reused or cited as an established
result.

---

## 3. Conventions and the hypothesis ledger

The book begins with a four-page detachable convention sheet. Each part then
adds only its local notation.

### 3.1 Global conventions

- Absolute values are multiplicative and valuations use
  \(v=-\log|\cdot|\).
- A point of a trivially valued analytification is treated consistently as a
  real semivaluation; the trivial valuation and the proper-support points are
  retained.
- Complex differential operators use
  \(dd^c=(2\pi)^{-1}i\partial\bar\partial\), as in the supplied book.
- CLD's \(d'\), \(d''\), and \(d'd''\) normalization is kept in its natural
  form; a comparison box records all factors and signs whenever Chern forms or
  Poincaré--Lelong formulae cross between formalisms.
- The Monge--Ampère measure attached to an \(L\)-psh metric has total mass
  \((L^n)\) unless explicitly normalized to a probability measure.
- `psh metric`, `potential`, and `metric function relative to a reference
  metric` are not used interchangeably until the relevant identification has
  been fixed.
- Spaces are Hausdorff when that is part of the analytic definition. Complex
  spaces are reduced, paracompact, and Hausdorff unless otherwise stated.
- A modification, model, domination, refinement, and test configuration are
  separately defined; none is used as a generic synonym for another.

### 3.2 Hypothesis matrix used throughout

| Axis | Main regimes kept distinct |
|---|---|
| Base field | complete nontrivially valued; complete discretely valued; trivially valued; algebraically closed or not |
| Characteristic | residue characteristic zero; positive residue characteristic; equal/mixed characteristic; arbitrary characteristic in the envelope theorem |
| Space | smooth; regular; normal; integral unibranch; reduced/reducible; compact Kähler complex space |
| Positivity | ample line bundle; nef/big line bundle; real numerical class; Kähler/big/pseudoeffective transcendental class |
| Potential | model/PL; smooth CLD; continuous psh; bounded psh; arbitrary psh; finite energy |
| Measure | atomic/model-supported; finite-energy; nonpluripolar; prescribed support; full mass |

Every major theorem will have a small margin code referring to this matrix.
The code is expository metadata, not part of the theorem statement.

### 3.3 Three reading routes

- **Local differential route:** Chapters 1--8, Part II, Chapters 29, 45, 61,
  and 64.
- **Global variational route:** Chapters 1--8, Parts III--IV, and Chapters
  60--66.
- **Complex/Kähler route:** Chapters 1--6, Part V, and Chapters 60--66; the
  reader may consult the supplied complex book for deeper background at the
  marked interfaces.

---

## 4. Detailed table of contents

The page estimates include proofs and examples but not appendices. They are
planning ranges, not quotas.

# Part I. Valuations, models, and analytic spaces (Chapters 1--8; 170--210 pp.)

## Chapter 1. Four entrances to the subject

**Purpose.** Give the reader a complete bird's-eye view before technical
foundations.

1. Complex potentials and their non-Archimedean analogues.
2. Degenerations, valuations, and Berkovich points.
3. Local differential forms versus global model functions.
4. The trivially valued cone and homogeneous potentials.
5. A nodal degeneration, a toric variety, and a test configuration as the
   three running examples.
6. Statement, without proof, of the master comparison diagram proved in
   Part VI.

## Chapter 2. Absolute values, valuations, and graded reduction

1. Ordered groups, seminorms, semivaluations, centers, and supports.
2. Rank, rational rank, residue transcendence degree, and Abhyankar's
   inequality.
3. Completed residue fields and extensions of valuations.
4. Graded residue rings and tropical spectra.
5. Divisorial, monomial, quasimonomial, and linear-growth valuations.
6. Examples on curves, affine space, and monomial ideals.

## Chapter 3. Schemes over valuation rings and models

1. Valuation rings, admissible formal schemes, and projective models.
2. Generic and special fibres; vertical Cartier and Weil divisors.
3. Domination, normalized blowups, flattening, and inverse systems of models.
4. SNC and dlt models; alterations where resolution is unavailable.
5. Intersection theory on models and projection formulae.
6. Precisely delimited use of Stacks Project results.

## Chapter 4. Berkovich spectra and analytification

1. The spectrum of a Banach ring and its topology.
2. Affinoid domains, gluing, and analytification of a scheme.
3. Reduction maps, generic points, and specialization.
4. Points on the analytic affine and projective line.
5. Properness, compactness, base change, and functoriality.
6. Trivial valuations as a genuine case, not a limiting slogan.

## Chapter 5. Dual complexes, skeleta, and retractions

1. Monomial valuations associated to a model.
2. Dual complexes and integral affine structures.
3. Skeleton embeddings and retraction maps.
4. Refinement, subdivisions, and cofinal systems.
5. Piecewise affine functions and vertical divisors.
6. Essential and canonical skeleta: what is used later and what is not.

## Chapter 6. Line bundles and metrics

1. Continuous metrics and metric functions.
2. Formal/model metrics and model functions.
3. Fubini--Study and piecewise linear metrics.
4. Semipositivity through nef models.
5. Pullback, tensor product, maximum, and change of reference metric.
6. Chambert--Loir measures at model level.

## Chapter 7. Topological, convex, and measure-theoretic tools

1. Nets, subnets, compactness, and upper semicontinuous regularization.
2. Choquet lemmas and monotone convergence.
3. Radon measures, weak convergence, energy duality, and Legendre transforms.
4. Capacities, quasicontinuity, and polar sets.
5. Concave functions and Duistermaat--Heckman distributions.
6. A ledger for extended-real arithmetic.

## Chapter 8. Model calculations in dimension one and in the toric case

1. Metric graphs and Laplacians on Berkovich curves.
2. The projective line over a nontrivially valued field.
3. The trivially valued affine cone of valuations.
4. Toric skeleta, support functions, and real Monge--Ampère measures.
5. Semistable reduction of the running curve.
6. Translation table between the examples and later abstract definitions.

# Part II. Chambert--Loir--Ducros forms and currents (Chapters 9--19; 260--320 pp.)

The revised 2025 Chambert--Loir--Ducros manuscript is a primary mathematical
source for this part, **not its expository template**. The theory will be
reconstructed in the style of the supplied complex book. In particular:

- the reader first calculates superforms, slopes, currents, and masses in
  Euclidean, curve, and toric examples;
- abstract tropical spaces are introduced only after the invariant they are
  designed to carry has appeared concretely;
- calibrations are developed next to integration, where their purpose is
  visible, rather than as an isolated layer of formalism;
- the minimal categorical machinery needed for coordinate independence stays
  in the main text, while maximal generality and technical variants move to
  Appendix G;
- repeated constructions are factored into reusable lemmas and every sign or
  orientation convention is tested on the running examples;
- the original CLD core is visibly distinguished from later delta-form and
  harmonic-tropicalization extensions;
- the 2025--2026 Gubler--Rabinoff curve-test framework is used to motivate
  maximum principles and pluriharmonicity more cleanly, while its
  “classically psh” functions remain distinguished from CLD's
  approximation-defined psh class until a comparison theorem applies.

Thus Part II contains the CLD theory and proves its principal results, but it
does not follow the source's order, pacing, notation, or presentation. Its
organizing direction is concrete-to-invariant and local-to-global.

## Chapter 9. Lagerberg superforms

1. Bigraded forms on real vector spaces and affine spaces.
2. The operators \(d'\), \(d''\), involution, and wedge signs.
3. Symmetric, positive, strongly positive, and weakly positive forms.
4. Pullback, contraction, and coordinate invariance.
5. Convex functions as local psh potentials.

## Chapter 10. Polyhedral and tropical spaces

1. Polyhedra, polyhedral complexes, lattices, and weights.
2. Tropical cycles and balancing.
3. Superforms on polyhedral subsets.
4. Tropical spaces and changes of charts.
5. Calibrations, orientations, and multiplicities.
6. Products, Gysin maps, and tropical intersection, introduced through
   explicit stable-intersection calculations before the general construction.

## Chapter 11. Integration and Stokes formulae

1. Integration of top-degree superforms.
2. Boundary orientations and balancing cancellation.
3. Stokes and Green formulae.
4. Pushforward and projection formulae.
5. Tropical intersection products as current products.

## Chapter 12. Tropicalization of analytic spaces

1. Moment maps and tropical charts.
2. Local skeleta and canonical calibrations.
3. Independence under refinement of tropical charts.
4. Dimension and multiplicity formulae.
5. Graded reduction, analytic cycles, and degrees as the source of tropical
   multiplicities.
6. Compact supports, weak analytic structures, and partitions of unity.

## Chapter 13. Real differential forms on Berkovich spaces

1. The sheaves \(A^{p,q}\).
2. Differential operators, pullbacks, and locality.
3. Integration on pure-dimensional analytic spaces.
4. Stokes on analytic domains.
5. Comparison with forms on a skeleton.

## Chapter 14. Currents and positivity

1. Currents as continuous functionals and their topology.
2. Positive currents and closed currents.
3. Pushforward, pullback where defined, and proper maps.
4. Currents of integration over analytic cycles.
5. Fibre integration, projection formulae, and support theorems.
6. Compactness and regularization issues particular to the non-Archimedean
   setting.
7. Berndtsson's metric-dependent supercurrent of a real submanifold,
   minimality, and the distinction from calibrated tropical currents.
8. Convex Bedford--Taylor products, weakly-null directions, strongly
   homogeneous currents, and an explicit convention dictionary.

## Chapter 15. Poincaré--Lelong and local potential theory

1. The current of a meromorphic function.
2. Poincaré--Lelong with the book's normalization.
3. Bochner--Martinelli and Levine formulae.
4. CLD-plurisubharmonic functions.
5. Polar loci, maximum principles, and pullbacks.

## Chapter 16. Bedford--Taylor products

1. Locally bounded psh functions and recursive wedge products.
2. Monotone convergence and locality.
3. Mixed products and comparison principles.
4. Chern--Levine--Nirenberg inequalities.
5. Local and relative Monge--Ampère measures.
6. Skeletal-current products, harmonic tropicalizations, and polar
   negligibility.
7. The precise boundary between CLD Bedford--Taylor products and global
   finite-energy products.
8. Harmonic ambiguity: a sufficient smooth-pluriharmonic approximation
   criterion, cell-interior affine regularity, and the cross-fan boundary
   obstruction showing that cellwise harmonicity alone is insufficient.

## Chapter 17. Metrized vector bundles and Chern currents

1. Smooth, PL, integral PL, formal, and residual metrics on vector bundles.
2. Reduction of metrized bundles and dimension of definition.
3. First Chern forms of metrized line bundles.
4. Psh metrics and Chern currents.
5. Products of curvature currents and relative Monge--Ampère operators.
6. Formal metrics and special-fibre intersection numbers.
7. Recovery of Chambert--Loir measures.
8. Bochner--Martinelli and Levine formulae.
9. Projection, functoriality, and detection of positivity on subvarieties.

## Chapter 18. Delta-forms and harmonic tropicalizations

1. Why smooth forms alone do not contain all model-theoretic curvature.
2. Delta-forms and delta-currents.
3. Positivity and Poincaré--Lelong in the enlarged calculus.
4. Harmonic tropicalizations and functorial forms.
5. Comparison with model functions and piecewise affine potentials.

## Chapter 19. Curves, tori, and abelian varieties

1. Laplacians and slope formulae on curves.
2. Toric metrics and tropical Monge--Ampère.
3. Raynaud uniformization of abelian varieties.
4. Canonical metrics and their currents.
5. A first CLD--BFJ comparison theorem on model and continuous psh loci.
6. A limitations table: assertions not known or not meaningful for arbitrary
   singular psh functions.

# Part III. The BFJ global theory over nontrivially valued fields (Chapters 20--31; 280--350 pp.)

The first goal is a detailed account of the original BFJ theory. Later
generalisations are presented in separate sections so the reader can see
exactly where discreteness, residue characteristic zero, algebraicity, or
support assumptions enter.

## Chapter 20. Model forms and semipositivity

1. Closed \((1,1)\)-forms as direct limits over models.
2. Model functions, vertical divisors, and the \(dd^c\)-operator.
3. Nefness, semipositivity, and numerical classes.
4. Model envelopes and maximum constructions.
5. Intersection pairings and Hodge-type inequalities.

## Chapter 21. Non-Archimedean psh functions

1. Equivalent definitions on SNC skeleta.
2. Upper semicontinuity and restrictions to dual complexes.
3. Stability under constants, maxima, convex combinations, and pullbacks.
4. Singularities and polar sets.
5. Comparison with continuous semipositive metrics.

## Chapter 22. Compactness and decreasing regularization

1. Equicontinuity on dual complexes.
2. Compactness modulo constants.
3. Multiplier ideals on models.
4. Toroidal techniques and nef approximation.
5. Decreasing approximation by model psh functions.
6. The exact role of residue characteristic zero.

## Chapter 23. Envelopes

1. Obstacle envelopes and psh envelopes.
2. Supremum stability and usc regularization.
3. Continuity of envelopes under the available hypotheses.
4. Orthogonality at model level.
5. Later extensions via test ideals and alterations.

## Chapter 24. The non-Archimedean Monge--Ampère operator

1. Mixed Chambert--Loir measures for model metrics.
2. Intersection-theoretic formulae.
3. Monotone extension to bounded psh functions.
4. Locality and maximum principles.
5. Comparison with the CLD current product.

## Chapter 25. Capacity and quasicontinuity

1. Monge--Ampère capacity.
2. Quasicontinuity of bounded and finite-energy potentials.
3. Negligible and pluripolar sets.
4. Convergence in capacity.
5. Domination and comparison principles.

## Chapter 26. Energy and finite-energy potentials

1. The Monge--Ampère energy \(E\).
2. Mixed-energy identities and cocycle formulae.
3. The class \(\mathcal E^1\).
4. Strong convergence and compactness of normalized sublevels.
5. Extension of mixed Monge--Ampère products.

## Chapter 27. Differentiability and orthogonality

1. Directional derivatives of energy.
2. Differentiability along model and continuous directions.
3. Orthogonality of envelopes.
4. The variational Euler--Lagrange equation.
5. Where envelope continuity is needed.

## Chapter 28. Finite-energy measures and variational solutions

1. Legendre dual energy of measures.
2. Coercivity and maximizers.
3. Existence and uniqueness in finite energy.
4. The Calabi--Yau/Monge--Ampère correspondence.
5. Stability with respect to the measure.

## Chapter 29. Continuity of solutions

1. Capacity estimates and non-Archimedean Kołodziej arguments.
2. Measures supported on a dual complex.
3. Continuous solutions and uniqueness.
4. The function-field/completion and support assumptions in the original BFJ
   theorem.
5. Later continuity theorems and their exact extra hypotheses.

## Chapter 30. Functoriality and change of field

1. Pullback under finite and birational morphisms.
2. Base extension of analytic spaces and metrics.
3. Pushforward of measures and projection formulae.
4. Descent questions.
5. The Gauss extension as a bridge to a trivially valued base.

## Chapter 31. Complete examples and synthesis

1. Curves and metric graphs.
2. Toric varieties and Alexandrov measures.
3. Model measures supported at divisorial points.
4. Canonical metrics in simple degenerations.
5. A theorem-by-theorem BFJ--CLD compatibility table.

# Part IV. The trivially valued BJ theory and the envelope theorem (Chapters 32--50; 400--500 pp.)

## Chapter 32. The trivially valued analytification

1. Semivaluations trivial on the ground field.
2. Centers, supports, and the compact Berkovich topology.
3. The scaling action and normalized links.
4. Divisorial and quasimonomial points.
5. Gauss extensions and complexifications.

## Chapter 33. Test configurations, norms, and filtrations

1. Test configurations and their compactifications.
2. Rees algebras and flag ideals.
3. Graded norms and multiplicative filtrations.
4. Finite generation and base ideals.
5. Duistermaat--Heckman measures.
6. The dictionary with geodesic rays, deferred in proof to Part VI.

## Chapter 34. Fubini--Study, PL, and psh functions

1. Fubini--Study functions and metrics.
2. Piecewise linear functions on dual complexes.
3. Generically finite Fubini--Study presentations.
4. Definition and basic closure properties of \(\operatorname{PSH}(\theta)\).
5. Compactness modulo constants and regularization.
6. Proper-support points and the value \(-\infty\).

## Chapter 35. Homogeneity, Legendre duality, and b-divisors

1. Homogeneous psh functions and the scaling action.
2. Cartier and Weil b-divisors.
3. Nef b-divisors and homogeneous potentials.
4. Legendre transforms, test curves, and carrier functions.
5. Determination by divisorial points.
6. Translation between the homogeneous and inhomogeneous categories.

## Chapter 36. Envelopes before the general theorem

1. Obstacle and psh envelopes.
2. Equivalent forms of the envelope property.
3. Known smooth/ample/low-dimensional cases.
4. The 2022 addendum and the remaining historical gap.
5. Why increasing nets, arbitrary bounded suprema, and sequential limits must
   be distinguished.

## Chapter 37. The envelope theorem: statement and sharpness

The principal theorem is stated here in its final form:

> Let \(X\) be an integral projective unibranch variety over an algebraically
> closed trivially valued field, let \(\theta\in N^1(X)_\mathbf R\), and let
> \((\varphi_i)\) be a nonempty bounded-above family in
> \(\operatorname{PSH}_X(\theta)\). Then
> \((\sup_i\varphi_i)^*\) is \(\theta\)-psh.

1. Equivalence with the historical BJ envelope conjecture.
2. Arbitrary dimension, characteristic, and real numerical class.
3. Behaviour on semivaluations of proper support.
4. Why unibranchness is essentially sharp.
5. The node/cusp comparison.
6. Proof map for Chapters 38--44.

## Chapter 38. Cartier b-divisors and homogeneous realization

1. Evaluation of a Cartier b-divisor on valuations.
2. Model and homogeneous FS functions.
3. Realization and approximation lemmas.
4. Passage between numerical classes on birational models.
5. Extended-real safeguards.

## Chapter 39. Birational and carrier reflection

1. Homogeneous birational reflection.
2. Legendre carrier reflection.
3. Equality on divisorial points and psh determination.
4. Descent of the envelope property through birational maps.
5. The exact functorial diagram.

## Chapter 40. Smooth varieties in arbitrary characteristic

1. The characteristic-zero argument.
2. Graded base ideals of obstacles.
3. Asymptotic test ideals in positive characteristic.
4. Subadditivity and uniform \(O(m^{-1})\) class errors.
5. The valuation inequality and psh convergence.
6. Comparison of multiplier-ideal and test-ideal proofs.

## Chapter 41. Determinant norms and finite descent

1. Analytic openness under finite maps.
2. Raynaud--Gruson flattening.
3. Determinant norms for finite algebras.
4. Weighted averaging without separability or reducedness assumptions.
5. Descent for finite normal morphisms.
6. Universal polynomial laws and base change.

## Chapter 42. Alterations and the normal case

1. Alterations in arbitrary characteristic.
2. Stein factorization.
3. Separating birational and finite steps.
4. Descent from a smooth alteration.
5. The envelope property for normal projective varieties.

## Chapter 43. Universal homeomorphisms in positive characteristic

1. Radicial finite maps and topological invariance.
2. Uniform Frobenius powers.
3. Pullback and reflection of Fubini--Study functions.
4. Psh reflection under universal homeomorphisms.
5. Descent through normalization.

## Chapter 44. Subintegral normalization in characteristic zero

1. Subintegral and seminormal extensions.
2. The Roberts--Singh additive-power sandwich.
3. Uniform control of homogeneous functions.
4. Psh reflection in characteristic zero.
5. Completion of the unibranch normalization step.

## Chapter 45. Consequences of the envelope theorem

1. Completion of the proof of Chapter 37.
2. Increasing nets and regularized suprema.
3. Obstacle envelopes for arbitrary real classes.
4. Monotone approximation consequences.
5. Geometric characterization by unibranchness in the ample case.
6. Replacement of the obsolete conjecture in the supplied book by this
   theorem and a historical note.

## Chapter 46. Monge--Ampère energy and mixed measures

1. Energy of PL metrics via intersection theory.
2. Extension to arbitrary psh metrics.
3. Mixed Monge--Ampère measures.
4. Locality, monotonicity, and integration by parts.
5. Compatibility with homogeneous potentials.

## Chapter 47. Finite-energy functions and measures

1. \(\mathcal E^1\) and its metric geometry.
2. Finite-energy measures and dual energy.
3. Differentiability of energy.
4. Orthogonality and the variational equation.
5. The non-Archimedean Calabi--Yau theorem.

## Chapter 48. Strong topologies, capacities, and pluripolar sets

1. Strong topology on \(\mathcal E^1\).
2. Strong topology on finite-energy measures.
3. Continuity and homeomorphism properties of Monge--Ampère.
4. Capacity, negligible sets, and pluripolar sets.
5. Compactness and convergence criteria.

## Chapter 49. Valuations of linear growth and toric models

1. Linear growth and finite-energy loci.
2. Topologies on valuation spaces.
3. Divisorial density and dual complexes.
4. Toric psh functions and convex bodies.
5. Explicit Monge--Ampère and energy formulae.

## Chapter 50. Stability functionals and filtrations

1. Norms, filtrations, and finite-energy metrics.
2. Non-Archimedean energy functionals.
3. Log discrepancy and entropy.
4. Ding and Mabuchi functionals.
5. Uniform K-stability and valuative criteria.
6. Scope warning: statements depending on results later than the foundational
   BJ paper are dated and sourced individually.

# Part V. Complex and transcendental non-Archimedean theory (Chapters 51--62; 300--380 pp.)

This part contains the mathematical content of the supplied book's entire
chapter on non-Archimedean pluripotential theory, not merely its subsection
called “The transcendental setting.” That subsection depends on the earlier
test-curve, envelope, trace, and Okounkov-body theories. The material will be
rewritten as a self-contained route rather than copied out of context.

## Chapter 51. Complex pluripotential prerequisites

1. Quasi-psh functions and positive currents.
2. Singularities, Lelong numbers, and multiplier ideals.
3. Nonpluripolar products and masses.
4. \(P\)- and \(\mathcal I\)-envelopes.
5. \(P\)- and \(\mathcal I\)-equivalence.
6. Exact interfaces with the supplied complex book.

## Chapter 52. Geodesic rays and test curves

1. Weak geodesics and subgeodesic rays.
2. Test curves and Legendre transforms.
3. The Ross--Witt Nyström correspondence.
4. Relative and \(\mathcal I\)-model test curves.
5. Operations and monotone limits.
6. Flag configurations and projective test configurations.

## Chapter 53. Transcendental non-Archimedean metrics

1. Inverse systems over Kähler perturbations.
2. Definition of \(\operatorname{PSH}^{\mathrm{NA}}(X,\theta)\).
3. Components, maximal metric, and volume.
4. Positive-volume and zero-volume regimes.
5. Homogeneous metrics attached to complex psh functions.
6. Bimeromorphic invariance.

## Chapter 54. Operations, limits, and traces

1. Order, addition, translation, and maximum.
2. Regularized suprema and Choquet reduction.
3. Decreasing infima and rescaling.
4. Volume under operations.
5. Trace/restriction of transcendental metrics.
6. Domain and singularity hypotheses for trace.
7. Descent of the existing trace to \(\mathcal I\)-classes on its natural
   domain, the resulting factorization from input \(P\)-classes to output
   \(\mathcal I\)-classes, and the still-open \(P\)-valued refinement.

## Chapter 55. Okounkov test curves and Duistermaat--Heckman measures

1. Partial and transcendental Okounkov bodies.
2. Okounkov test curves.
3. Definition of the Duistermaat--Heckman measure.
4. Flag independence.
5. Moment formulae and weak continuity.
6. Birational invariance.
7. Zero mass: the toric numerical-dimension theorem and the
   \(\mathcal I\)-invariant refined-body obstruction.

## Chapter 56. Valuative analytification of complex singularities

1. The valuative formula using multiplier ideals.
2. Gauss extension/complexification.
3. Analytification of test curves by Legendre duality.
4. Piecewise linear test curves.
5. GAGA and global generation for algebraic metrics.
6. Extended-real and zero-mass cases.

## Chapter 57. Comparison with Boucksom--Jonsson

1. Realization of Fubini--Study functions.
2. Order reflection and injectivity.
3. Compatibility with decreasing limits.
4. The projective order-preserving bijection.
5. Compatibility with sum, translation, maximum, scaling, and envelopes.
6. Compatibility of trace with analytic restriction.

## Chapter 58. Tropical spectra of complex spaces

1. Idempotent semirings and tropical algebras.
2. Berkovich spectra viewed as tropical spectra.
3. Semivaluations on a nonalgebraic complex space.
4. Topology, centers, and functoriality.
5. Recovery of the usual trivially valued analytification in the projective
   algebraic case.

## Chapter 59. Dual complexes and log discrepancy over \(\mathbf C\)

1. Ideals and modifications of complex spaces.
2. Divisorial and monomial semivaluations.
3. Dual complexes and retractions.
4. Log discrepancy.
5. Compactness and approximation.
6. Worked Kähler examples with no algebraic model.

## Chapter 60. Mesquita-Piccione psh functions and complex-to-NA transforms

1. Model functions and non-Archimedean psh functions on complex spaces.
2. Semipositive non-Archimedean metrics in a Kähler class.
3. Complex singularities as non-Archimedean functions.
4. Energies and stability functionals.
5. The cscK application in its exact original scope.
6. Comparison with the constructions of Chapter 53.

## Chapter 61. Transcendental envelopes and Calabi--Yau theory

1. Continuity of envelopes in the Kähler setting.
2. Orthogonality.
3. Strong topologies on potentials and measures.
4. Measures supported on dual complexes.
5. Transcendental non-Archimedean Calabi--Yau.
6. Regularity and approximation of solutions.

## Chapter 62. K-stability for compact Kähler manifolds

1. Big test configurations and models.
2. Uniform K-stability for models.
3. Valuative criteria and the beta invariant.
4. Existence and uniqueness of cscK metrics.
5. Relation to flag configurations and radial functionals.
6. A dated map of the 2025--2026 theorem boundary.

# Part VI. Comparison theorems, degenerations, and applications (Chapters 63--69; 180--230 pp.)

## Chapter 63. The master dictionary

This chapter states and proves the main comparison diagram on each locus where
all terms are defined:

| Geometric datum | Model/global realization | Differential realization | Trivially valued realization | Complex realization |
|---|---|---|---|---|
| vertical Cartier divisor | model function | PL potential/current | homogeneous FS function | test-configuration ray |
| nef model line bundle | semipositive model metric | positive Chern form/current | psh FS metric | semipositive ray/test curve |
| intersection product | Chambert--Loir measure | CLD wedge product | BJ Monge--Ampère | slope/nonpluripolar mass data |
| inverse system of models | BFJ psh function | skeletal restrictions | BJ psh function | DXZ/MP non-Archimedean metric |

The chapter separates genuine equivalence theorems from one-way functors and
from analogies.

## Chapter 64. Comparing Monge--Ampère operators

1. Formal/model metrics: intersection number equals CLD current product.
2. Continuous semipositive metrics: approximation and weak convergence.
3. BFJ versus Chambert--Loir measures.
4. BJ homogeneous measures and projective intersections.
5. Complex/test-curve moments and Duistermaat--Heckman measures.
6. Finite-energy comparison: proven loci and unresolved scope.

## Chapter 65. Rays, filtrations, and Legendre transforms

1. Test configurations and weak geodesic rays.
2. Multiplicative filtrations and non-Archimedean metrics.
3. Test curves and Legendre duality.
4. Radial energy slopes.
5. Quantization and Fubini--Study approximation.
6. Commutativity of the construction diagram.
7. Erratum audit for asymptotic-slope results: the unaffected statements are
   separated from BHJ 2019 Theorem 5.6 and its dependent consequences, whose
   published proof was identified as incorrect in the 2022 erratum.

## Chapter 66. Hybrid spaces and convergence

1. Hybrid analytification over discs and Banach rings.
2. Complex fibres and the non-Archimedean central fibre.
3. Hybrid convergence of metrics.
4. Convergence of Monge--Ampère measures.
5. Skeletal limits and canonical measures.
6. Limits of energy and entropy functionals.

## Chapter 67. Functoriality, restriction, and trace

1. Birational pullback in all four approaches.
2. Finite maps and norm constructions.
3. Base change and descent.
4. Restriction of metrics and currents.
5. Complex trace versus analytic restriction.
6. Singular/unibranch comparison and the boundary of present methods.

## Chapter 68. Stability and the Yau--Tian--Donaldson bridge

1. Algebraic, analytic, and non-Archimedean functionals.
2. Slope formulae.
3. Divisorial and valuative criteria.
4. Properness/coercivity principles.
5. Projective and Kähler cscK conclusions.
6. Exactly which implications are theorem, conditional theorem, or heuristic.

## Chapter 69. Verified extensions and structural obstructions

This is not a list of unsolved exercises. It records only outcomes that survive
the research protocol:

1. complete proofs of any new theorems produced while writing;
2. counterexamples showing that proposed extensions are false;
3. sharp conditional reductions when a question is equivalent to a clearly
   isolated missing theorem;
4. compatibility results not previously assembled in one source;
5. a final hypothesis atlas and normalization concordance.

If an attempted problem remains unresolved, no theorem will be fabricated.
Its detailed attempt and obstruction remain in the companion research ledger,
not disguised as a solved result in the textbook.

---

## 5. Appendices (projected 180--240 pp.)

### Appendix A. Commutative algebra over valuation and graded rings

Integral dependence, Rees algebras, normalization, subintegrality,
seminormality, finite universal homeomorphisms, determinant norms, and the
Roberts--Singh input.

### Appendix B. Birational geometry and alterations

Normalized blowups, exceptional divisors, flattening, Stein factorization,
resolution in characteristic zero, and alterations in arbitrary
characteristic.

### Appendix C. Multiplier ideals and test ideals

Valuative descriptions, subadditivity, asymptotic ideals, global generation,
Skoda division, and the precise parallel used in the envelope proof.

### Appendix D. Convex analysis and Legendre duality

Convex bodies, support functions, Legendre--Fenchel duality, concave test
curves, real Monge--Ampère, moment measures, strongly homogeneous
supercurrents, mixed volumes, and the Alexandrov--Fenchel form.

### Appendix E. Nets and compact upper-envelope calculus

Willard subnets, Moore--Smith convergence, usc regularization, Choquet
selection, and safe extended-real identities.

### Appendix F. Intersection theory and b-divisors

Numerical classes, mixed intersections, Cartier/Weil b-divisors, nefness, and
projection formulae.

### Appendix G. Tropical and idempotent algebra

Tropical semirings, spectra, graded reduction, polyhedral conventions, and
calibration signs.

### Appendix H. Complex pluripotential reference sheet

Nonpluripolar products, singularity types, energy classes, envelopes, and weak
geodesics, with detailed pointers to the supplied complex book.

### Appendix I. Stacks Project dependency table

For every cited tag: the exact statement used, local hypotheses, and the first
place of application. The envelope proof will at least audit the tags for
flattening, normalization, universal homeomorphisms, finite morphisms, and
Stein factorization.

### Appendix J. Normalization concordance

All signs and constants for valuations, metric weights, \(dd^c\), \(d'd''\),
Chern forms, intersection products, energies, entropy, and probability
normalizations.

### Appendix K. Notation and symbol atlas

A global symbol table, a list of spaces of potentials and measures, and a map
from BFJ/BJ/CLD/MP notation to the book's notation.

### Appendix L. Source and theorem provenance

The first proof source, later generalizations, dependencies, and audit status
of every major theorem.

---

## 6. Connection programme

Connections will not be postponed to one comparative epilogue. Each one is
introduced at the first point where both sides exist, then consolidated in
Part VI.

### 6.1 Model metrics and CLD currents

**Claim to establish.** For a formal/model metric, the CLD Chern current and
its top wedge recover the corresponding vertical intersection data and
Chambert--Loir measure. The proof proceeds first on a fixed skeleton, then
through tropical-chart refinements, and finally by functoriality.

### 6.2 CLD psh versus BFJ psh

The book will give an exact comparison on model and continuous semipositive
metrics. For singular metrics it will state only the strongest published
comparison supported by a complete proof. “Both are psh” is not treated as an
automatic equivalence: the local regularity and global approximation
definitions are genuinely different pieces of structure.

### 6.3 Nontrivial versus trivial valuation

Gauss extension, scaling, and degeneration constructions will relate
trivially valued homogeneous functions to metrics over a discretely valued
extension. The comparison will track centers, supports, line-bundle classes,
and total Monge--Ampère mass.

### 6.4 Test configurations, filtrations, and rays

The Rees construction gives

\[
  \text{test configuration}
  \longrightarrow
  \text{finitely generated filtration}
  \longrightarrow
  \text{FS/PL non-Archimedean metric},
\]

while the complex Legendre construction gives a weak geodesic ray/test curve.
The book proves compatibility of energies and Duistermaat--Heckman measures,
including the normalization at time one and asymptotic slopes.

### 6.5 DXZ/Xia versus BJ

For projective classes, the inverse-limit/test-curve construction is compared
to BJ analytification by the valuative multiplier-ideal formula. Order,
monotone limits, operations, volume, and trace are each checked separately;
the comparison is not left as a single abstract bijection.

### 6.6 Mesquita-Piccione versus DXZ/Xia

The objects live on differently constructed spaces. The comparison will be
built in three stages:

1. identify divisorial and monomial semivaluations and their dual complexes;
2. compare model functions and their limits;
3. compare energy/Monge--Ampère structures on the common finite-energy locus
   where the literature proves such an identification.

Any extension beyond the published finite-energy/Kähler scope will be placed
under the research audit before use.

### 6.7 Hybrid complex/non-Archimedean geometry

Hybrid spaces provide the topological carrier on which complex metrics and
measures can converge to non-Archimedean ones. The book separates:

- convergence of spaces;
- convergence of potentials;
- convergence of Monge--Ampère measures;
- convergence or lower semicontinuity of energy and stability functionals.

### 6.8 Trace and restriction

The complex trace of a singularity class, analytic restriction of a metric,
and pullback to valuation spaces will be placed in one commutative diagram.
The diagram will display exactly where smoothness, unibranchness, avoidance of
the singular locus, or positive mass is required.

---

## 7. Source map

The bibliography will be rebuilt from primary sources and the supplied
`ComplexGeometry.bib`, deduplicated by DOI/arXiv identifier. The following are
anchor sources, not an exhaustive bibliography. Full publication data,
scope notes, version warnings, and book placement appear in the companion
`LITERATURE_MAP.md`.

### 7.1 Analytic and model foundations

- Berkovich, *Spectral Theory and Analytic Geometry over Non-Archimedean
  Fields* and *Étale Cohomology for Non-Archimedean Analytic Spaces*.
- Chambert-Loir, the construction of measures from semipositive metrized line
  bundles.
- Gubler and Thuillier on models, tropicalization, skeleta, and forms.
- Gubler--Rabinoff--Werner on skeleta and tropicalization.

### 7.2 CLD calculus

- Chambert-Loir--Ducros, *Formes différentielles réelles et courants sur les
  espaces de Berkovich*, revised version of 25 July 2025, used as a theorem
  source rather than a writing model.
- Gubler--Künnemann on positivity and delta-forms.
- Gubler--Jell--Rabinoff on forms from harmonic tropicalizations.
- Vilsmeier on comparison of real and non-Archimedean Monge--Ampère measures.

### 7.3 Nontrivially valued global theory

- Boucksom--Favre--Jonsson, *Singular Semipositive Metrics in
  Non-Archimedean Geometry*.
- Boucksom--Favre--Jonsson, *Solution to a Non-Archimedean Monge--Ampère
  Equation*.
- Gubler--Jell--Künnemann--Martin on continuity of envelopes and test ideals.
- Boucksom--Gubler--Martin on non-Archimedean volumes.
- Reboulet on finite-energy geodesics and degenerations.

### 7.4 Trivially valued theory

- Boucksom--Jonsson, *Global Pluripotential Theory over a Trivially Valued
  Field*.
- Boucksom--Jonsson, the 2022 addendum.
- The supplied manuscript *The Envelope Property for Unibranch Projective
  Varieties*, used as the proof source for Chapters 37--45.
- Boucksom--Hisamoto--Jonsson on uniform K-stability and
  Duistermaat--Heckman measures.
- Boucksom--Jonsson and later work on norms, filtrations, and K-stability.

### 7.5 Complex/transcendental theory

- The supplied book, especially its entire Chapter 13, plus its prerequisite
  chapters on envelopes, comparison of singularities, test curves, trace,
  Okounkov bodies, and b-divisors.
- Darvas--Xia--Zhang, *A Transcendental Approach to Non-Archimedean Metrics of
  Pseudoeffective Classes*.
- Xia's work on operations, partial Okounkov bodies, and
  Duistermaat--Heckman measures.
- Mesquita-Piccione, *A Non-Archimedean Theory of Complex Spaces and the cscK
  Problem*.
- Mesquita-Piccione--Witt Nyström, *A Transcendental Non-Archimedean
  Calabi--Yau Theorem with Applications to the cscK Problem*.
- Witt Nyström on Calabi--Yau theorems for degenerations of compact Kähler
  manifolds.

### 7.6 Bridges and 2026 context

- Boucksom--Jonsson, *From Complex to Non-Archimedean Geometry: An Approach to
  the YTD Conjecture* (2026 lecture notes).
- Boucksom's hybrid-space lecture notes.
- Primary papers on hybrid convergence of measures and energy slopes.
- Boucksom--Hisamoto--Jonsson's 2022 erratum to the 2019 energy-asymptotics
  paper; any theorem depending on the invalidated proof of Theorem 5.6 is
  flagged rather than repeated as established.

---

## 8. Treatment of the envelope theorem

The first supplied book labels the envelope property as a conjecture. That
paragraph is obsolete and will be replaced by Chapters 37--45.

The proof is not compressed into a black box. Its architecture is pedagogical:

1. translate psh functions to Cartier b-divisors and homogeneous functions;
2. prove birational and Legendre-carrier reflection;
3. settle the smooth case in all characteristics, using multiplier ideals in
   characteristic zero and asymptotic test ideals in positive characteristic;
4. prove finite descent using flattening and determinant norms, without
   assuming separability or reduced fibres;
5. use alterations and Stein factorization for normal varieties;
6. descend along the unibranch normalization, treating positive
   characteristic by Frobenius and characteristic zero by the
   Roberts--Singh additive-power argument;
7. return from homogeneous functions to arbitrary \(\theta\)-psh functions.

The proof audit will pay special attention to:

- the two distinct gradings that occur in Rees/base-ideal arguments;
- the \(O(m^{-1})\) drift in numerical class;
- passage from equality on divisorial points to equality everywhere;
- universal properties of determinant norms;
- values at proper-support semivaluations;
- nets rather than sequences;
- every use of subtraction involving an infinite value.

The sharpness discussion will use the known implication that the envelope
property for an ample class forces unibranchness. Thus “remove the unibranch
hypothesis” is not placed in the research queue as though it were a plausible
general theorem.

---

## 9. Self-containedness and citation policy

### 9.1 Proved in full in the main text

- basic Berkovich spectra and analytification used later;
- construction and elementary functoriality of model metrics/functions;
- dual complexes and skeletal restrictions;
- Lagerberg/CLD calculus through Bedford--Taylor products;
- BFJ compactness, approximation, energy, and variational arguments at the
  stated foundational hypotheses;
- the BJ psh/energy/measure formalism needed for finite energy;
- the full envelope theorem from the second supplied manuscript;
- the projective comparison between transcendental and BJ metrics;
- all master-dictionary compatibility statements.

### 9.2 Cited but explained at the interface

- general resolution of singularities, alterations, flattening, and some
  scheme-theoretic descent;
- deep multiplier-ideal and test-ideal theorems;
- foundational nonpluripolar product results already treated fully in the
  supplied complex book;
- major cscK existence theorems whose proof would require a second monograph
  in Riemannian/PDE geometry.

For each such input, the text states the exact version used and verifies that
its hypotheses are met. “By standard results” will not replace a check when
singularities or characteristic matter.

### 9.3 Citations to the supplied book

The new book may cite the supplied complex book for long complex-analytic
foundations, but Chapter 51 will restate every definition and theorem required
to read Parts V--VI. A reader will not be forced to guess which convention for
\(dd^c\), multiplier ideals, masses, or singularity comparison is in force.

---

## 10. Research programme for related open questions

The instruction to try to solve the related open questions will be treated as
a genuine parallel research project, not as decorative “future work.” The
bounded initial corpus is:

1. every formal conjecture/problem in the supplied complex book;
2. every explicitly unresolved technical point in chapters used by the new
   monograph;
3. every explicit conjecture or question in the core BFJ, BJ, CLD,
   DXZ/Xia, Mesquita-Piccione, and Mesquita-Piccione--Witt Nyström sources
   that bears directly on a planned theorem;
4. new compatibility gaps exposed by the master dictionary.

This scope is intentionally auditable. “All related open questions” cannot
coherently mean every question in valuation theory, K-stability, tropical
geometry, and complex Monge--Ampère equations.

### 10.1 Current seed list from the supplied complex book

The literature and first requested `gpt-5.6-sol`/`xhigh` pass have already
changed several labels. The complete statements and audit state are recorded
in `RESEARCH_QUESTION_LEDGER.md`. The source-book list is:

1. extension of a prescribed Kähler-current singularity type from a
   submanifold (the trace Dirichlet problem);
2. construction of trace when the ambient space is merely unibranch;
3. a zero-mass transcendental Okounkov body of dimension equal to numerical
   dimension;
4. refinement of trace from \(\mathcal I\)-classes to \(P\)-classes--open;
   Xia's Proposition 2.12 supplies only an \(\mathcal I\)-valued trace, and
   the map from input \(P\)-classes to output \(\mathcal I\)-classes merely
   factors through the input \(\mathcal I\)-class;
5. a refined partial Okounkov body whose Euclidean volume equals the
   nonpluripolar mass--now accompanied by a validated no-go theorem for every
   construction invariant under \(\mathcal I\)-equivalence;
6. extension of the theory to non-Kähler spaces;
7. higher-bidegree analogues for closed positive currents;
8. \(\varphi\sim_P P_\theta[\varphi]\) in the zero-mass regime;
9. \(\mathcal I\)-goodness of zero-mass \(\mathcal I\)-model potentials;
10. removal of the \(P_\theta\)-projection in the big-line-bundle
    filtration-to-test-curve construction;
11. removal of the closure in a valuative characterization of
    transcendental partial Okounkov bodies;
12. unibranch extensions of the equisingularity criterion and general trace.

The zero-mass Okounkov question now has a complete argument in the rational
toric category via Cao's numerical criterion, and the trace Dirichlet question
has a split product/retraction special case. Both, together with the CLD
harmonic-reduction lemmas, passed an independent Rethlas audit. They still
require final source citation and line-by-line manuscript proofs before
publication.

The current-literature expansion of this seed list will also test directly
relevant complex inputs, including ample-locus regularity in a non-nef big
class and local finiteness of nonpluripolar products outside the Fujiki
setting. Historical questions already settled or refuted--such as general
monotonicity/log-concavity statements now proved, or smoothness of arbitrary
complex geodesics now known to fail--will be labelled as such and not sent to
the proof queue.

The former envelope conjecture is **not** on this list: it is solved by the
second supplied manuscript and belongs in the main theorem sequence. Because
that manuscript is presently the proof source rather than a public
bibliographic reference, the proof still receives the same independent audit
as any theorem newly introduced into the book.

### 10.2 Solver protocol

Each problem receives a dedicated high-reasoning research dossier using the
requested `gpt-5.6-sol` at `xhigh` effort. The dossier has seven stages:

1. **Status audit:** search current primary literature and eliminate problems
   already solved, refuted, or reformulated.
2. **Formalization:** write exact hypotheses, conclusion, equivalent forms,
   and low-dimensional/model cases.
3. **Attack map:** list at least two plausible mechanisms and their necessary
   lemmas.
4. **Proof attempt:** carry one mechanism through line by line; record the
   first genuinely unsupported implication rather than smoothing it over.
5. **Adversarial audit:** a separate solver tries to break the proof through
   zero-mass examples, singular spaces, positive characteristic, nondivisorial
   valuations, and failure of sequential compactness.
6. **External audit:** compare every invoked theorem against its primary
   source and exact hypotheses.
7. **Disposition:** one of
   `literature-resolved`, `proved-and-audited`, `counterexample`,
   `conditional-reduction`, or `unresolved-after-attempt`.

No result receives `proved-and-audited` from a single model pass. Promising
new arguments will also be written as standalone propositions before being
used downstream.

### 10.3 How research outcomes enter the book

- `literature-resolved`: incorporated with a dated source note;
- `proved-and-audited`: incorporated as a theorem with complete proof and an
  explicit provenance note;
- `counterexample`: incorporated where it clarifies the sharp boundary of a
  construction;
- `conditional-reduction`: used only if the antecedent is visibly stated;
- `unresolved-after-attempt`: excluded from the theorem narrative and retained
  honestly in the companion research ledger.

The standard is “try every scoped question seriously,” not “declare every
question solved.”

---

## 11. Writing and verification workflow

### Phase 0. Architecture and source freeze

1. Obtain approval of this plan and the scope of the research corpus.
2. Freeze dated versions of all anchor papers, especially the 2025 CLD
   revision and 2025--2026 complex/Kähler papers.
3. Deduplicate the bibliography and assign stable citation keys.
4. Create the notation, hypothesis, and theorem-provenance ledgers.

**Deliverables:** approved plan, bibliography database, source manifest,
notation concordance.

### Phase 1. Foundations and running examples

Draft Part I and Appendices D--G first. This fixes conventions before any
high-level theorem is stated.

**Verification:** compile each chapter; check every definition against at
least two later uses; test all running examples by hand.

### Phase 2. CLD calculus

Reconstruct Part II from the mathematical content of the 2025 revision and
the delta-form/harmonic extensions. Do not inherit the source's chapter order
or expository architecture. Build each abstraction out of the running curve
and toric calculations, then prove the first formal/model comparison
theorems.

**Verification:** sign and orientation audit, Poincaré--Lelong normalization
audit, and independent checks on curves and toric charts.

### Phase 3. BFJ theory

Draft Part III while maintaining two parallel labels: “original BFJ scope”
and “later extension.”

**Verification:** approximation monotonicity, total masses, capacity arguments,
and every location where residue characteristic zero enters.

### Phase 4. BJ theory and the envelope proof

Draft Chapters 32--50. Chapters 37--45 receive a separate proof ledger based
on the second supplied manuscript.

**Verification:** characteristic-by-characteristic audit; finite-descent and
universal-homeomorphism audit; tests on nodes and cusps; net/usc audit.

### Phase 5. Complex/transcendental theory

Rewrite and expand the supplied Chapter 13 with its prerequisites, then add
the Mesquita-Piccione and Mesquita-Piccione--Witt Nyström theories.

**Verification:** projective comparison diagrams; compatibility of operations;
zero-mass and trace edge cases; separation of algebraic and general Kähler
hypotheses.

### Phase 6. Bridges and applications

Draft Part VI only after both sides of every comparison have stable notation.

**Verification:** each arrow in the master diagram is tagged as equivalence,
injection, surjection, functor, or analogy; no dashed/heuristic arrow is used
inside a proof.

### Phase R. Open-question research, in parallel

Run the protocol of Section 10 throughout Phases 1--6. A result may alter a
later chapter only after audit. Research is therefore parallel but cannot
silently destabilize already verified foundations.

### Phase 7. Global editorial pass

1. dependency and forward-reference audit;
2. notation and normalization audit;
3. theorem-hypothesis audit;
4. bibliography/provenance audit;
5. index and glossary pass;
6. graduate-reader pass for motivation and local readability;
7. mathematical revision log and final build.

---

## 12. File architecture for the manuscript

The planned source tree mirrors the supplied book while separating generated
and human-written material:

```text
nonarchimedean_pluripotential_theory/
  book.tex
  book-volume-I.tex
  book-volume-II.tex
  latexmkrc
  bibliography/
    nonarchimedean.bib
    source_manifest.md
  frontmatter/
    preface.tex
    conventions.tex
    reading_guide.tex
  parts/
    part-I-foundations/
    part-II-cld/
    part-III-bfj/
    part-IV-bj-envelope/
    part-V-complex/
    part-VI-bridges/
  appendices/
  figures/
  research/
    question_ledger.md
    proof_audits/
  editorial/
    notation_ledger.md
    hypothesis_ledger.md
    theorem_provenance.md
    mathematical_revision_log.tex
```

The actual LaTeX manuscript will be created only after approval of the plan.
Research dossiers remain outside the publishable source unless their results
pass audit.

---

## 13. Estimated scale and milestones

| Milestone | Content | Estimated polished length |
|---|---|---:|
| M1 | Part I + foundational appendices | 220--280 pp. |
| M2 | Part II (CLD) | 260--320 pp. |
| M3 | Part III (BFJ) | 280--350 pp. |
| M4 | Part IV (BJ + envelope) | 400--500 pp. |
| M5 | Part V (complex/transcendental) | 300--380 pp. |
| M6 | Part VI + remaining appendices | 250--330 pp. |
| **Total** | one logical monograph | **1,710--2,160 pp.** |

The upper estimate reflects full proofs of CLD foundations and the new
envelope theorem. If a single-volume ceiling becomes important, the cleanest
compression is to move basic Berkovich geometry and tropical calculus to a
separate preliminary volume; compressing the proof chapters would damage the
graduate-level objective.

---

## 14. Decisions requested before full drafting

The plan makes the following default editorial choices, which can be changed
before Phase 0 closes:

1. one logical monograph, issued as two physical volumes if needed;
2. English exposition, with original French titles retained in the
   bibliography;
3. no routine exercises, but many fully worked examples;
4. the complete envelope proof in the main text rather than an appendix;
5. the full 2025 CLD theory, including calibrations, currents,
   Bedford--Taylor products, formal metrics, and abelian varieties;
6. a separate, auditable research ledger for attempted new results;
7. no claim of a new theorem until independent mathematical audit succeeds.

Once these choices are approved, the first writing milestone should be the
frontmatter, convention sheet, and Chapters 1--2, followed immediately by the
running curve and toric examples needed to test all later normalizations.
