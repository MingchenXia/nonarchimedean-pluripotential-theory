# Chapter 60: finite-energy test curves, order and mass defect

Date: 24 September 2026.
Baseline: `c41a25cc1941fd8f7b6c4ad76f488e733cb01657`.
Scope: Section 60.6 before the existing full-comparison warning.
All preceding Chapter 60 text, the warning and all following text retain
their baseline bytes. This unit expands consequences of cited analytic
correspondences; it does not promote a research-frontier theorem.

## Correspondence and normalization

The local setting now declares the connected compact Kähler manifold,
dimension, Kähler class and form, reference volume, closed terminal level
and fixed zero initial value. The forward supremum is stated for positive
time. Its value at zero is the finite-energy boundary value from the RWN
correspondence, not an unjustified interchange of a pointwise supremum
with a boundary limit.

The inverse is explicitly the infimum of U(0,phi)_s-s tau over positive
times. Biconjugacy recovers every level, including the closed endpoint
and values of minus infinity. Existence of the MP/DXZ identification and
I-maximality of this inverse remain cited analytic inputs. Neither is
claimed to follow from scalar convex duality alone.

The energy formula now holds at every positive time: E(U_s)/s=E(phi).
It follows from the preceding maximal-ray energy identity, together with
the cited relative RWN energy identity and division by the reference
volume. It no longer uses the later mixed-slope theorem as a dependency.
Reference-volume normalization and the squared annular coordinate
s=-log|z|^2 are kept separate. The terminal mass may be zero.

## Deductions and examples

The two Legendre transforms preserve order; the maximal-ray order theorem
therefore makes the finite-energy correspondence an order isomorphism.
Parameter translation Gamma_(tau-c) adds cs to the ray and c to the MP
datum, cutoff and energy. Adding a constant to every nontrivial level
instead changes the initial value and violates the fixed zero-obstacle
normalization when the constant is nonzero.

The second pass replaces the first draft's average-slope argument for the
cutoff by a direct proof. Comparison with the constant datum a is equivalent
to comparison with the zero-level test curve cut off at a; this is equivalent
to Gamma_max<=a. Hence Gamma_max=sup phi=phi(v_triv), by the previously
proved finite vertex test. This deduction requires neither the average-slope
lemma nor the mixed-slope theorem.

The mass-defect integral is consequently J(phi). The ordered rooftop
formula proves d1(U_s,s Gamma_max)=s J(phi), including s=0. Nondegeneracy
of the complex d1 metric shows that J vanishes exactly for constant MP
data, whose inverse curves are zero through the closed cutoff. These
arguments retain the finite-energy hypotheses and the already imported
existence/energy identity; they do not independently reconstruct those
analytic inputs. The connected dimension-zero case reduces to constant
data and satisfies the same formulas.

The existing degree-one projective-line hyperplane example has cutoff one,
mass 1-tau on [0,1], energy 1/2, J=1/2 and distance s/2 from the upper
constant ray s. Its endpoint is log r, a nontrivial psh potential with
zero non-pluripolar mass. Replacing that endpoint by the identically
minus-infinity function leaves the positive-time supremum unchanged,
but the inverse transform still recovers log r. The altered family is
not a closed test curve. This tests why the endpoint convention is
required for injectivity, rather than asserting a counterexample within
the stated domain.

The datum 1/2 has the same energy as the hyperplane datum but the rays
cross at r=0 and r=1. Ray order reflection therefore makes the two data
incomparable. This demonstrates the failure of energy equality alone to
identify arbitrary data. A constant-level curve supplies the opposite
terminal-mass behavior, with full terminal mass and zero J.

## Sources and status

The [published DXZ article](https://ems.press/content/serial-article-files/50355?nt=1),
Comment. Math. Helv. 100 (2025), 269–322, DOI 10.4171/CMH/586, was
rechecked through the publisher's indexed PDF text: Theorem 2.6(iii)
on p. 282; Section 3.4, formulas (34) and (35), and Theorem 3.17 on
p. 299. The annular coordinates in formulas (6) and (10) on pp. 280–281
agree with the existing Chapter 52 normalization audit. The bibliography
already contains the correct published record under DXZ23 and is unchanged.
Local download attempts failed at TLS connection establishment; web PDF
screenshots returned cache misses. No new local DXZ PDF checksum or
visual source-page inspection is claimed for this turn.

The [exact MP author version](https://arxiv.org/html/2409.06221v2),
18 September 2025, was checked at Section 5.2, printed p. 48, and its
dependency on Theorem 5.1.7. The existing local PDF retains SHA-256
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`.
The [published MP record](https://doi.org/10.1016/j.aim.2025.110543)
was confirmed: Advances in Mathematics 481 (2025), 110543, already
recorded under MP24. Direct publisher full-text access returned an access
error; the displayed section/page locators therefore remain attached to
MPTropicalV2. The reviewed house-audit warning is not a claim that the
paper is unpublished, or that preprint pagination equals publication
pagination. No bibliography or frozen citation record is changed.

Internal dependencies are the Chapter 52 closed-endpoint and biconjugacy
arguments, its cited RWN energy theorem and established hyperplane example,
and the preceding Chapter 60 finite vertex test, maximal-ray order,
translation and energy identity. The full-cone scope warning is unchanged.

## Two passes and validation

The first full build produced 3,983 pages, 18,958,645 bytes. Physical
pages 3373–3376 were rendered and inspected. One 17.31pt horizontal
overflow came from the proof heading and first citation. The second
complete statement/proof/source/notation pass checked zero initial value,
closed endpoints, extended-real inequalities, both directions of order,
translation signs, reference-volume normalization, positive time versus
the boundary, constant data, dimension zero and both endpoint examples.
It replaced the cutoff proof by the direct order argument and shortened
the proof heading. The second build eliminated the overflow. A final
copyedit declares the dimension locally and removes a repeated phrase;
the resulting full build is the artifact checked below.

Final full build: **3,983 pages, 18,959,115 bytes**. Physical pages
3373–3376 were rendered and inspected in full, covering the revised block
and its following boundary. This is a scoped visual review.

- Input/reference check: 390 TeX files, 11,648 unique labels; no missing
  input, duplicate label, dangling reference or structural defect.
- Final log: no unresolved citation/reference, multiply defined label,
  rerun request or horizontal/vertical overflow. Existing class and
  underfull warnings remain.
- Scoped strict house audit: zero errors and one reviewed exact-version
  warning about MPTropicalV2; exit status 1, not a warning-free strict pass.
- Inventory: PASS, 45 active atoms across 14 formal environments, tiers
  (0,5,8,15,17).
- Surrounding Chapter 60 source is byte-identical to the baseline.
- `git diff --check`: PASS.

Final Chapter 60 SHA-256:
`0a9840fa9c28d0aedaa52f8cea59e82ad8b26d98238a46b926f8d5797225bc54`.
Final live PDF SHA-256:
`4d4f798d96e8440ba3a654dcc63267bdbdbbc856467c8fee76d249dd3e16f04f`.

The preserved P12.1 fragment has SHA-256
`8d9f9bd9edb057b95773479279bbdabb3240319e4cb56f6f15cb2bd923fb4380`.
The supplied normalized-links PDF and archived copy both retain SHA-256
`71f5e0d50bdcbf493cb96a869e2db03a78bd591b3eba2f797da5a23f6253daaa`.
The supplied CURVE_PSH.tex retains SHA-256
`9142aac73c5af7e4e715b3313def5ed56fae4e63e1ac8a53d0419df7d2194be9`.

The 45 active atoms, P12.1 integration/provenance, P12.2–P12.6 residuals,
supplied originals, bibliography, frozen packets, verifier receipts and
dated releases are preserved. No independent-agent or production-verifier
pass is claimed. The live PDF remains an ignored build product.
Next work is the mixed-slope argument and its uniform estimates; general
Kähler existence, sequential regularization and the full analytic slope
reduction retain their existing cited-input boundaries.
