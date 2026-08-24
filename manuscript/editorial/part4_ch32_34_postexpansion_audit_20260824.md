# Chapters 32--34 post-expansion mathematical audit (24 August 2026)

## Scope and source firewall

This audit covers `parts/part4/ch32_trivial_analytification.tex`,
`parts/part4/ch33_test_configurations.tex`, and
`parts/part4/ch34_fs_pl_psh.tex`.  No other manuscript source was edited.

The principal source used for the trivially valued theory was
Boucksom--Jonsson, *Global pluripotential theory over a trivially valued
field* (the manuscript key `BJ22`, especially Sections 1--4).  The audit
checked the statements used here against Definition 4.1, Lemmas 4.3, 4.6,
and 4.9, Theorems 4.5, 4.7, 4.15, and 4.22, and Corollaries 4.17, 4.23,
and 4.25.  In particular, Theorem 5.20 of that source is an envelope
theorem, not a regularization theorem.

Mingchen Xia's arXiv:1710.09731 is excluded completely.  The three audited
chapters contain neither the identifier nor a Xia citation, and no retained
proof in these chapters was routed through that paper.  The local copy of
the principal `BJ22` source likewise has no Xia or arXiv:1710.09731 hit.

The repaired block labelled `thm:bj-basic-closure` has no exact-current
Rethlas receipt.  It is therefore fenced in Chapter 34 as an exact
primary-source import.  Nothing in that block is advertised as newly
machine-verified mathematics, and no uncited extension of the imported
clauses is permitted.

## Substantive corrections

### Chapter 32: trivially valued analytification

- Corrected the trivial-locus discussion for reducible varieties and
  removed the false assertion that the set of rational points is
  uncountable in every ground-field regime.  The closed-point locus used in
  the curve description is now only called infinite and discrete where
  that is what is proved.
- Replaced the former global compact-link assertion by the actual fixed-point
  obstruction: a positive finite homogeneous gauge cannot be defined on a
  scaling-stable domain meeting the trivial locus.  Fixed-model discrepancy
  links are retained only under the klt hypothesis and no compactness claim
  is made for their union over all models.
- Scoped the log-discrepancy gauge correctly.  Finiteness, continuity, and
  affine behavior on a fixed quasimonomial complex remain available, while
  positivity is asserted only in the klt case.
- Corrected the divisorial criterion for a quasimonomial point: on a
  one-dimensional rational ray the coordinates are a common positive real
  multiple of positive integers, and divisoriality is equivalent to that
  multiple being rational.
- Corrected the Gauss comparison.  There is no map sending a trivially valued
  semivaluation to a semivaluation compatible with the nontrivial valuation
  on `k((varpi))` by simple restriction; the canonical object is the Gauss
  section.  The analogous assignment from complex points is not continuous
  into the discrete trivial locus except where it is locally constant.
- Removed unsupported countable-branching language.  The countable-field
  metrizability proof and the uncountable-field failure of first
  countability now use coherent-ideal coordinates and the countable-union
  avoidance lemma directly.
- Source-aligned the use of divisorial values at proper-support points:
  determination and comparison are the unconditional `BJ22` Theorem 4.22
  and Corollary 4.23, not consequences of an envelope property.
- Restricted inverse-limit language to the dual complexes of SNC test
  configurations and removed an unsupported global all-model compactness
  statement.
- Preserved the existing labels, including `thm:ch32-no-compact-link`, while
  changing the content under that label to the correct theorem.

### Chapter 33: test configurations and filtrations

- Aligned the standing scheme hypotheses with the reduced projective
  variety convention of `BJ22`; integral hypotheses are now stated only
  where function fields, divisorial valuations, or intersection formulae
  require them.
- Corrected the flag-ideal sign convention.  With
  `a O_Xcal = O_Xcal(D)`, the divisor is anti-effective for an ordinary
  ideal (up to a uniformizer shift), while `O(D)` and hence `D` are
  relatively ample on the blowup.
- Reproved faithfulness of flag-ideal functions without the former invalid
  orbit-closure assertion.  The proof treats divisorial valuations with
  uniformizer value zero separately and otherwise rescales to the Gauss
  slice before applying the valuative criterion for integral closure.
- Corrected the universal-property arrow: a model on which the ideal is
  invertible maps to the blowup.  An integrally closed projective model is
  recovered as the integral closure of that blowup in the common generic
  fibre.
- Corrected the filtration boundedness equivalence: finiteness of the
  maximal jumping number gives the upper linear bound, while full linear
  boundedness also includes the lower exhaustiveness bound.
- Made the test-configuration filtration invariant under equivalence by
  passing first to the integral closure in the generic fibre.  The
  finite-generation proof now uses finitely many homogeneous generators in
  their actual degrees and bounds their weight/degree ratios.
- Fenced the filtration-to-test-configuration correspondence at its real
  algebraic boundary.  Relative Proj returns the irrelevant saturation,
  and integral closure may enlarge it again; exact recovery holds only for
  an already saturated and integrally closed Rees algebra.  The bijection is
  correspondingly stated modulo common saturated integral closure and
  Veronese change.
- Corrected the Fubini--Study normalization after a Veronese change: the
  resulting analytic function is still normalized for `L`, not mislabeled
  as a function for `rL`.
- Corrected the Duistermaat--Heckman tail monotonicity and replaced a false
  log-concavity claim by the actual Brunn--Minkowski concavity of tail
  volumes.
- Repaired the non-finitely-generated harmonic example and its psh status,
  using the explicit `BJ22` curve slope criterion instead of an invalid
  increasing-limit argument.
- Corrected the toric finite-type criterion: real finite type means affine
  on a finite rational polyhedral subdivision; rational finite generation
  additionally requires rational affine data.  No denominator clearing is
  applied to arbitrary real weights.
- Narrowed the `BC11` import: containment in an ample series by itself is
  not presented as the full hypothesis of the concave-transform theorem.

### Chapter 34: Fubini--Study, PL, and psh functions

- Separated the four function classes correctly.  PL functions are bounded
  continuous model functions; generically finite Fubini--Study functions
  may have proper-support poles; psh functions are decreasing net limits,
  not uniform limits of PL functions.
- Corrected the scalar hierarchy: for arbitrary `L`, positive rational
  multiples of `H(L)` lie in `PL+`; equality with `PL+` holds when `L` is
  ample.  The flag-ideal weight indexing now uses the correct sufficiently
  negative tail.
- Removed the invalid purported counterexample to max-stability of
  `PL_R`.  The retained failure statement is transparently imported from
  `BJ22`, Remark 2.4, and explained by an irrational wall that cannot be
  represented on a rational model subdivision.
- Corrected the dual-complex scope.  Real PL functions restrict to real
  piecewise affine functions on a fixed SNC dual complex; rationality is
  asserted only with rational model data.  The model-directedness argument
  uses graph closure/flattening and does not assume equivariant resolution.
- Corrected psh nonemptiness and positivity scope.  Nonemptiness implies
  pseudoeffectivity; a bounded member implies nefness; constants exist
  exactly for nef classes.  The proof now explicitly notes that a defining
  approximant above a bounded limit is itself finite-valued.
- Corrected normalization: `PSH^sup(theta)` is nonempty exactly when
  `PSH(theta)` is nonempty.  Nefness is needed for bounded members and
  constants, not for the mere existence of a normalized singular psh
  function.
- Replaced the former PL-consistency argument by the exact transparent
  import `BJ22`, Lemma 4.3, whose proof depends on Lemmas 3.5 and 3.7 and
  Corollary 3.22, not on an envelope theorem.
- Fenced `thm:bj-basic-closure` with its precise source package.  The
  theorem now distinguishes fixed and varying classes, requires a
  generically finite decreasing limit, uses strictly positive scalars only,
  states the pullback alternative componentwise, and imports divisorial
  finiteness/comparison without an envelope hypothesis.
- Replaced the false regularization package under the preserved label
  `thm:ch34-fs-regularization` by exactly `BJ22`, Theorem 4.15: rational GF
  approximants in nearby classes in general, finite Fubini--Study
  approximants when the class is nef, and dominant-model approximants in an
  ample class.  The necessary class drift is explicit.
- Corrected the decreasing-to-a-pole example on `P^1`: the finite
  approximants use the base-point-free system `(s,t_0,t_1)` with weights
  `(0,-j,-j)`, so the maximum is genuinely Fubini--Study and decreases to
  `log|s|` at the proper-support endpoint.

## Verification

- Preserved all pre-existing target labels.  Added the missing item label
  `itm:bj-closure:determination` to the exact clause cited from Chapters 32
  and 34.
- Static resolution against every manuscript TeX file found zero missing
  references from the audited chapters, zero duplicate labels inside the
  slice, and zero audited labels duplicated elsewhere in the manuscript.
- Found no exercise environment, no optional name on a theorem,
  proposition, lemma, corollary, definition, example, or remark, and no
  occurrence of Xia or arXiv:1710.09731 in the audited chapters.
- Compiled Chapters 32--34 with the book preamble and an `includeonly`
  wrapper.  `latexmk` completed successfully and produced a 209-page slice.
  The final log contains no LaTeX error, missing citation/reference,
  multiply-defined label, or overfull box.

## Residual provenance and Rethlas gates

- `thm:bj-basic-closure` remains an exact `BJ22` import without an
  exact-current Rethlas receipt.  This is the principal unresolved
  verification gate.  The same status applies to the three regularization
  scopes in `thm:ch34-fs-regularization`; they are source-verified imports,
  not new Rethlas results.
- Foundational test-configuration/filtration and Duistermaat--Heckman
  statements still transparently import `BHJ17`; concave-transform
  statements import `BC11`; valuation and inverse-limit statements import
  `JM12`, `BJ22`, and the cited birational inputs.  These are ordinary
  external provenance boundaries and were not promoted to local proofs.
- The source package used in these three chapters has no identified
  dependency on arXiv:1710.09731.  Any future strengthening of the closure,
  regularization, envelope, saturation, or compactness clauses must be
  checked anew against both the excluded-source firewall and the
  exact-current Rethlas protocol.

No additional unfenced mathematical claim was left unresolved in Chapters
32--34 by this audit.
