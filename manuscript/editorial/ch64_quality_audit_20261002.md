# Chapter 64 completion audit

Date: 2 October 2026.

Base: local Chapter 63 commit 7260e4c.

Scope: parts/part6/ch64_compare_ma.tex, under the sequential quality
programme. The whole-book goal continues, with independent Chapter 72
research paused. Frozen releases, verifier receipts and checksum ledgers
are preserved.

## Mathematical and expository review

The entire chapter and all three earlier Chapter 64 unit audits were read.
All twelve formal assertions were checked, including their proofs or exact
imported interfaces. There are 21 labelled reusable environments and
77 labels. Eight numbered sections, three subsections and the source note
have semantic labels. The introduction identifies the model, bounded,
finite-energy, partial-body and filtration dependencies.

The principal checks and repairs are:

- The introduction distinguishes model and monotone Monge--Ampere products
  from the one-dimensional DH measures of complex test curves. No universal
  singular operator is inferred from that list of constructions.
- The nontrivially valued sections explicitly use the analytic additive
  convention with |pi| = exp(-1). Model functions, the unit fibre and
  intersection duality therefore have compatible units. Arbitrary base
  norms are treated by the later atom-location conversion and Chapter 63's
  lambda formula, without changing the atomic masses.
- The model domain is proper, reduced and pure-dimensional, with relative
  normality. Completion first gives integral metrics on the powers L_i^m_i,
  then division by every m_i gives the rational product. CLD defect factors
  reduce to b_E in precisely this domain. Flat specialization gives mass;
  relative nefness gives positivity.
- Model duality cancels b_E against the model-function value. Refinement
  retains contracted zero-degree components, residue-field degrees and the
  pushforward of div(pi). No exceptional atom is added to a pulled-back
  metric. The nonreduced example tests both occurrences of multiplicity.
- A rational model test is a difference of two ample rational semipositive
  model metrics on the same generic line bundle. Telescoping the tuple and
  symmetric vertical intersection give the explicit 2 sum c_i sup-error
  bound. The signed curvature difference keeps its minus sign; both
  resulting positive measures have mass c_i.
- Density and the fixed positive mass turn model-test limits into a positive
  functional on all continuous tests. Riesz representation uses compact
  Hausdorff analytification, without a metrizability assumption. Comparing
  two approximating tuples proves independence, and zero mixed mass gives
  the zero measure without division.
- The BFJ domain includes connectedness. A common rapidly convergent
  subsequence in all slots is made decreasing by rational fibre shifts.
  Different ample classes are handled by the finite polarization identity
  and pure bounded monotone continuity; separate-slot continuity does not
  justify a diagonal limit. CLD agreement retains the stipulated common
  formal regularization.
- The BJ model theorem explicitly chooses rational line bundles, their
  classes and a common test configuration dominating the punctured product.
  The energy pairing is defined by compactified intersection, whose
  independence is the projection formula. The atomic measure and mass then
  follow from vertical test pairing, with the fixed trivialization.
- A former homogeneous-to-b-divisor assertion conflicted with the completed
  Chapter 46 and is replaced. Finite-energy scaling is the published
  pushforward identity. For homogeneous potentials, bounded truncations
  have measures; a full weak limit, if it exists, is invariant and carried
  by scaling-fixed points. Existence and finite energy are not inferred.
  The divisorial coefficient dictionary and n-fold b-intersections remain
  separate from the (n+1)-fold compactified energy pairing.
- A new degree-d curve example computes the homogeneous profile -as,
  bounded truncation mass (d-a) at the root and a at R ord_p, and raw
  energy -a^2 R/2. The full weak limit has mass d at scaling-fixed points,
  while the potential has energy minus infinity. The Cartier total-class
  degree d-a equals the root mass in this particular curve calculation;
  it is not a general higher-dimensional intersection identity.
- First variation is stated for an affine segment of semipositive model
  weights, with the exact internal BFJ and BJ proofs cited. An arbitrary
  differentiable finite-energy path is no longer claimed to follow from
  formal multilinearity. Constant paths, tensor powers, class scaling and
  rational presentation exponents independently check the volume factors.
- The semistable curve uses a rational node, unit-length normalization and
  rational model vertex values. Its outgoing slopes and intersection matrix
  compute the same measure. The moving-atom example separates uniform-to-weak
  continuity from total variation and verifies the decreasing constant-shift
  variant.
- The DH tail theorem retains a bounded positive-mass I-model test curve.
  The initial partial body's volume is the total mass. Its transform's
  superlevels give tails; finite-measure continuity from above gives the
  terminal atom. Concavity of the nth root of interior mass gives local
  Lipschitz continuity and the density below the cutoff. No endpoint mass
  equality is inserted in the general statement.
- Signed Fubini on bounded transform support proves every integer moment,
  including odd powers and negative translated cutoffs. The first moment
  is the raw relative radial energy. Substituting ambient V for a smaller
  initial mass creates a divergent lower-half-line integrand.
- The two-cutoff P1 example computes the reference body, transform, continuous
  DH part, terminal atom, all mass normalizations and the first moment.
  It includes a = b, zero terminal mass and non-full initial mass.
- The algebraic DH comparison uses spectral tails and the filtered-series
  mass theorem, not equality of total masses. BHJ's limit is probability
  normalized; multiplying its fibration and barycenter formulas by V gives
  the raw moments. Linearization shifts change moment and ray energy by cV.
- The mixed canonical-truncation proof uses Borel strict-inequality layers,
  not ordinary open-set locality. The BJ mixed maximum rule follows by
  polarization with common auxiliary terms. The positive average expansion
  and one raw energy term give the kappa_n tail bound. Equal full masses
  give the total-variation estimate; continuous-test duality passes the
  weak limit without restricting it to an arbitrary Borel set.
- Independent cutoffs use their minimum, and a bound on negative average
  energy gives uniformity. The harmonic example computes variation 2/(m+1).
  Infinite energy permits polar limiting mass; general decreasing bounded
  approximation gives only weak convergence. A comparison of two singular
  operators requires bounded agreement and truncation continuity in both.
- The final ledger retains each theory's separate signature and imported
  scope, the unaffected BHJ19 Section 3 theorem and the published erratum,
  and the factor-two MP--DXZ radial convention. Psh-cone equality alone is
  not used to identify Monge--Ampere operators.

Inline mathematics follows the house convention. Compact model, truncation
and ledger statements and the first-variation display are kept together.

## Direct primary-source interfaces

Six primary PDFs and 35 selected pages were read and visually inspected.
The CLD and bounded BFJ pages reuse the checked Chapter 63 source versions;
the current review checks their Chapter 64 interfaces. These are direct
source checks, not a new independent verification of all deep dependencies.

| Source and version | Interfaces checked | Physical PDF pages |
| --- | --- | --- |
| CLD, 25 July 2025 | Formal intersection Theorem 18.5.5 and relative-normal discrete formula Proposition 18.5.8, including the full multiplicity proof | 528--532 |
| Boucksom--Eriksson, published Advances in Mathematics 378 (2021), 107501, freshly retrieved publisher PDF | Lemma 5.17 and its completed proof, model/difference-of-FS conventions, Theorem 8.4 and Lemma 8.6, their proofs and regularization scope | 54--55, 72--74 |
| BFJ15, published author offprint, JAMS 28 (2015), 617--667 | Theorem 3.1, bounded weighted decreasing-net continuity, constant/uniform comparison; full proofs of Lemma 6.8 and Proposition 6.9 | 16--18, 30 |
| BJ22, published AFST 31 (2022), 647--836 | Definition 3.12, Proposition 3.14 and model measures; Definition 7.6, Proposition 7.7; Theorem 7.18 and Proposition 7.19 with proofs; maximum Theorem 7.40's interface | 50--53, 106, 111--112, 123 |
| Xia, published Geometry & Topology 29 (2025), 1283--1344 | Initial-potential and I-model conventions, Definitions 7.6 and 7.8, Lemma 7.7 and its proof; bare Lebesgue pushforward and endpoint body | 46, 49--50 |
| BHJ17, published Annales de l'Institut Fourier 67 (2017), 743--841 | Theorem 3.1 and Corollary 3.4 with proofs, linearization translation, Proposition 3.12's barycenter proof and Proposition 5.9's filtration identification | 32--40, 51 |

The maximum theorem is used as a precise published input; its complete
proof on subsequent pages is not newly audited here. The relative initial
Okounkov-body construction is the previously proved internal theorem,
rather than an enlargement of Xia's full-initial-volume Lemma 7.7.
The RWN, MP--DXZ and BHJ19/erratum interfaces retain the separately checked
chapter dependencies; no new independent research conclusion is claimed.

Selected-source SHA-256 values (the cached files are not staged):

- CLD: `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`.
- BE: `f9b8d54cfb2733486f35d450f5f763acf81a51816368ccd2c24c0663845d84f9`.
- BFJ: `a1314cba684f9a126faf9c79155fed3d0d4070dd028cc9f573b4c76a7646a2d3`.
- BJ: `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`.
- Xia: `b8568896bbf7cdad2dedfc97a8048d3caa75bc800d67f04bfcbadd3705a2a5f9`.
- BHJ: `edfd3b1506b49cf42ae85014d731bd9d86af5ed248134397cd562fba70c6f60e`.

## Exact example supplement

The supplement passes 10,835 exact rational checks in 25 families. It
covers finite polarization in dimensions one through six; semistable mass,
positivity, intersection pairing and the explicit continuity bound; tensor
presentation exponents and nonreduced multiplicity; homogeneous mass,
raw and probability energy and scaling; signed DH layer cake, first moments
and translated moments through order six; harmonic-series mass, variation,
cocycle energy and cutoff tails; and moving-atom weak/variation behavior.
These computations supplement the proofs and test the worked examples;
they are not tests of the general imported theorems.

## Build, render and final gates

Three changed-source full builds pass. The final PDF has 4,140 pages and
19,307,224 bytes. Source SHA-256:
`16b882eeec3371c660eee5fb22fc51c6c3b4caf13033c9fb06307a2f5a6c3159`.
PDF SHA-256:
`a7398c0af89f1ad4e238b8c31a313f03d7d1047b3e4c46eba300697202ef25d0`.
There are no unresolved references/citations, missing glyphs, rerun requests
or fatal errors. Chapter 64 has no overfull boxes or LaTeX/package warnings.
Eighteen inherited overfull boxes elsewhere and thirteen duplicate PDF
destinations in Chapter 70 remain recorded for the whole-book pass.

All twenty physical chapter pages 3327--3346 (printed 3257--3276) and the
adjoining physical pages 3326 and 3347 were visually checked at detail size.
All fourteen images changed in the second build were reinspected. The last
layout repair was then checked on every one of its seven changed pages,
3340--3346. The other fifteen final chapter/seam images match the already
inspected preceding images byte for byte at the same render resolution.
The final page contains the source note; it is no longer a blank page.
No reviewed layout defect remains.

The post-render scoped check finds twelve formal assertions, 21 reusable
labelled environments and 77 labels, without duplicate labels, unlabelled
objects, missing proofs, environment imbalance, unfinished markers or legacy
inline delimiters. The project reference checker passes for 425 inputs and
12,275 unique labels, with no missing input or dangling reference; all six
checker tests pass. The inventory remains 42 active atoms in twelve Chapter
72 environments, tiers (0,3,7,15,17). git diff --check passes. The unavailable
legacy house-audit executable is replaced by the recorded manual and scoped
review, rather than reported as having run.

Frozen releases, receipts and checksum ledgers are unchanged. This is a
direct editorial/source audit and claims no new independent verifier verdict.
Chapter 65 is next; the whole-book completion goal continues. Verified
commits remain local pending explicit remote-push approval.
