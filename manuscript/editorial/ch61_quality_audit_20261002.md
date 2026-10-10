# Chapter 61 completion audit

Date: 2 October 2026

Base: local Chapter 60 commit `5488b52`.

Scope: `parts/part5/ch61_transcendental_cy.tex`, under the sequential quality
programme. Chapter 62 is next; the whole-book goal continues. Independent
Chapter 72 research remains paused. Frozen receipts and releases are preserved.

## Mathematical and expository review

The complete chapter and all six preceding unit audits were read. All twenty
formal assertions retain proofs or exact imported interfaces. There are 32
labelled reusable environments and 98 labels. The eight numbered sections,
eleven new subsections and source note have semantic labels. They expose the
order of compactness, finite-energy duality, envelopes, orthogonality, strong
topologies, variational existence, approximation and regularity.

The principal checks and repairs are:

- Weak compactness uses a convergent subnet in a Tychonoff product. Tail
  envelopes use the imported arbitrary-family envelope theorem, and the
  trivial valuation prevents an identically minus-infinite limit. Energy
  upper semicontinuity includes extended values; finite lower energy bounds
  are imposed before identifying finite-energy compact subsets.
- Non-pluripolar point bounds retain genuine convex coefficients summing to
  one. A decreasing convex series contradicts an infinite point size. The
  separation argument uses PL positive-pair decomposition and ordinary
  division by a common background multiplier, separately from the rational
  valuation-scaling action. The point-energy estimate uses bounded model
  truncations and mixed probability measures before passing to the limit.
  The stronger algebraic upper constant is not asserted in this setting.
- Finite dual energy gives integrability before pairings are subtracted.
  The finite-energy tangent inequality supplies the energy identity of a
  Monge--Ampere measure before the general integrability lemma is applied
  to it. Constant invariance uses mass one. The two ordered J conventions
  and the variational gap have their explicit orientations.
- Envelope approximation now uses positive rational translations, which
  preserve the rational model class. Continuity retains the exact imported
  radial-envelope core. Orthogonality keeps the restricted masses, central
  multiplicities, division by volume and the positive regularization error
  divided by the multiplicity. Continuous-obstacle orthogonality follows
  from uniform potential convergence and a fixed continuous test function.
  The first variation reverses the inequalities for a negative parameter.
- Strong quasi-metric existence is imported independently of Calabi--Yau
  surjectivity. The normalized Monge--Ampere map first embeds into its image;
  the later variational argument proves surjectivity. The two root distances
  distinguish dual energy from J. The mixed estimate, joint pairings and
  evaluation bound retain the dimension exponent, energy bounds and root
  translation term. Dimension zero is treated directly.
- Fixed-measure integral convergence first chooses a model approximation
  of the reference measure, then takes the potential-net limit. The mixed
  estimate controls the first error uniformly. The absolute-integral identity
  has the correct minus sign; finite-energy integrability excludes undefined
  differences on a null set. The weak-but-not-strong curve example now derives
  the rational model potential by valuation scaling and convexity, then
  computes both its energy and its probability measure.
- Variational existence uses bounded-energy maximizing sequences and a
  convergent subnet. Strong convergence of their measures to the target
  follows from the variational gap before surjectivity is known. The fixed
  measure argument and mixed estimate supply the integral limit; upper
  semicontinuity then identifies a maximizer. Normalized ordered distances
  identify both strong topologies. The two-ray curve solution checks masses,
  energies, the sharp dimension-one point bound and the inverse direction
  of the Calabi--Yau homeomorphism.
- The previously verified whole-complex boundary proof is byte-identical.
  Its uniform divisorial input now points to the preceding chapter's actual
  fixed-model oscillation proposition and exact author-version locator.
  Convexity alone with finite vertex values is not substituted for the
  whole-face lower bound. Retraction convergence uses compatibility,
  continuous PL density, fixed Radon monotone-net integration and interchange
  of two suprema. A sequence is selected through quasi-distance and entropy
  tails; no countable cofinal system of all models is asserted.
- Finite barycentric interpolation uses compatible rational subdivisions
  of one complex, nonnegative real masses, convex decreasing interpolants
  and the exact affine discrepancy identity. The abstract triangulations
  need not themselves be realized as a new analytic model. Zero weights
  and zero-dimensional faces are included.
- The interval example now gives the full continuous solution, its dyadic
  piecewise-linear solutions, slope jumps and supported-endpoint values.
  It computes the exact uniform error h^2/8, energies -1/6+h^2/24, dual
  energies 1/6-h^2/24 and entropy 1/2. Its quadratic restriction also shows
  why continuous regularity need not give a PL function.
- General finite-energy locality is retained as the full imported MPWN
  theorem. The source's summary of decreasing weak continuity is not
  presented as an independent moving-weight limit proof. The published
  algebraic proof uses its stronger weighted continuity proposition.
  Support domination uses almost-everywhere finiteness and equality of
  probability measures, rather than a false pointwise inclusion at common
  minus-infinite values. Fixed-complex Dini convergence then yields global
  continuity. Divisorial envelopes retain all vertices and coefficients
  multiplied by central multiplicities. Uniform fixed-complex continuity
  and general strong/entropy density keep their different support hypotheses.

Inline mathematics follows the house convention outside the preserved
verification block. Compact statements and warnings, the point-size display
and the atomic-solution definition are kept with their introductions.
The Chapter 60 audit's publication metadata was also corrected to Contemporary
Mathematics 810 (2025) for the already inspected synthetic-energy offprint;
its PDF, page locators, hash and the book bibliography were already correct.

## Direct source interfaces

Four primary PDFs and 46 source pages were read and inspected in rendered
contact sheets. The version-specific page list is:

| Source | Principal interfaces | Physical pages inspected |
| --- | --- | --- |
| Mesquita-Piccione--Witt Nystrom, arXiv 2509.09442 v1 | Radial envelopes, energy, compactness, point bounds, orthogonality, quasi-metrics, Calabi--Yau, retractions, locality and regularity | 8--30 |
| Mesquita-Piccione, arXiv 2409.06221 v2 | Uniform model bound used in the preserved boundary argument | 40--41 |
| Boucksom--Jonsson, published AFST 31 (2022) | Weighted locality, variational estimates, fixed-measure limits, point bounds, bounded-set continuity and algebraic Calabi--Yau/regularity | 123--125, 140--142, 154--155, 158--159, 164--166 |
| Boucksom--Jonsson, published Contemporary Mathematics 810 (2025) author offprint | Ordered energy, strong density before surjectivity, quasi-metric construction and class-independent topology | 19--20, 24--29 |

The PDFs were cached during the immediately preceding units of this same
continuation; the listed passages were checked directly for this chapter.
The published synthetic construction is precisely Theorems 2.22, 2.23 and
2.25, printed pp. 182--185; 2.24 is a lemma. The published algebraic locality
proof is printed pp. 768--770 and uses Proposition 7.19(iii). These are
antecedents and reusable estimates, not substitutions for the analytic-model
and restricted-volume inputs in the transcendental theorem.

PDF SHA-256 values, in table order:

1. `54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464`
2. `9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`
3. `50bd6e6782c29088edc96d013a5d49257b0395d9fb398664f1a9859639992948`
4. `4ecf20801f0871223ddfc1ea3e09927904affaab75bb5e195bfe55a2b0f09498`

## Verification and preservation

The exact-arithmetic supplement passes 6,374 checks across 23 families:
convex-series weights, weak/strong curve energy, interval probability and
entropy, exact interpolation, nested monotonicity, uniform error, slope
masses, supported endpoints, trapezoidal quadratic integrals, model/dual
energies, two-ray curves, ordered surface distances, the signed-to-absolute
integral identity and constant-obstacle first variation. Finite calculations
supplement the proof review and do not establish the general imported theorems.

The legacy house-audit executable is unavailable. Manual review and the scoped
structural substitute pass: balanced environments, no duplicate or missing
reusable labels, no proofless formal assertions, no double dollars and no
unfinished-work markers. The 100 legacy inline delimiter occurrences are
confined to the byte-preserved verified boundary block; outside it there
are zero. That block retains SHA-256
`f82585d8a420d3214a008a583a14f0487bd657372b4f8656acae3c027ac487de`.
Its frozen receipt and provenance are unchanged, and this pass claims no
new independent verifier verdict.

Post-render verification passes for 425 input files and 12,213 labels.
All six reference-checker tests pass. The inventory remains 42 atoms in
twelve environments, tiers (0,3,7,15,17). `git diff --check` passes.

Final full build: **4,130 pages, 19,279,694 bytes**. PDF SHA-256:
`d0dac3594638a156def90702dbf62620fe8edcbe457720bcd00f1d624d5947a4`.
Final chapter SHA-256:
`9c3ed4e4b4c7813c63d728c4dfa6721dc24784323cfc91a1a78d6c28bdab0b0e`.
No unresolved references or citations, missing glyphs, rerun requests or
fatal errors remain. Chapter 61 has no overfull boxes or LaTeX/package
warnings. Repairing its long inline curve-energy expression reduces the
global overfull count to eighteen; thirteen duplicate PDF destinations in
Chapter 70 remain recorded for the later pass.

All 26 physical chapter pages 3249--3274 (printed 3179--3204) and both
adjoining seams were inspected at detail size. The last layout repair
changed ten page images, all reinspected; every other final chapter/seam
image was compared byte for byte with its inspected preceding version.
No reviewed chapter layout defect remains. The review PDF is saved at
`/workspace/book-completion-drafts/Chapter_61_Review_2026-10-02.pdf`.
Verified work remains local pending explicit remote-push approval.
