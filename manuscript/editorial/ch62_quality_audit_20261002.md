# Chapter 62 completion audit

Date: 2 October 2026

Base: local Chapter 61 commit 6bebdb8.

Scope: parts/part5/ch62_k_stability_kahler.tex, under the sequential
chapter-quality programme. Part V is complete; Chapter 63 is next.
The whole-book goal continues. Independent Chapter 72 research remains
paused. Frozen releases, receipts and checksum ledgers are preserved.

## Mathematical and expository review

The entire chapter and all seven preceding Chapter 62 unit audits were read.
All fourteen formal assertions have proofs or precise imported interfaces.
There are 28 labelled reusable environments and 99 labels. The eight
numbered sections, twelve new subsections and source note have semantic
labels. They distinguish raw intersection invariants, normalized envelopes,
completion, fixed-measure class derivatives, finite-support duality,
mass variation, threshold variation, volume integrals and radial slopes.

The principal checks and additions are:

- The introduction states the probability normalization of potential
  energies and Monge--Ampere measures, separately from the raw model
  intersection convention. Model identities retain central multiplicities,
  division by volume and f_D >= 1. Restricted positive-product and
  approximation interfaces remain full MPWN imports; this pass does not
  replace them by a proof summary.
- Pullback invariance and base translation are derived from the normalized
  envelope identities only when both representatives satisfy f_D >= 1.
  The non-nef surface calculation retains its Zariski decomposition and
  explicitly disproves raw base invariance. No binomial rule for arbitrary
  positive products or converse to the all-big-model implication is added.
- Translating a PL obstacle until f_D >= 1 supplies a big representative:
  D minus the central fibre is effective and A plus the fibre is big.
  The comparison thus identifies the normalized model inequality with the
  PL-envelope test. The raw all-big-model condition remains stronger unless
  a further comparison is proved.
- On fixed divisorial support, normalized point bounds give finite dual
  energy before using Calabi--Yau existence. Both orders of the dual
  supremum give the Lipschitz mass bound. Weak convergence plus convergence
  of dual energy gives strong convergence, and the fixed-complex estimate
  gives uniform solution convergence. Zero masses and a zero point bound
  are included.
- Completion preserves the same real coercivity constant through all five
  test domains. The strongly continuous twisted functional is imported
  from the published synthetic-energy construction; model polynomial
  identities extend through finite-energy mixed continuity. No derivative
  is interchanged with a limit. Rational simplex rounding preserves
  nonnegativity and total mass, including boundary faces.
- Entropy/strong density supplies the full-to-finite-support passage.
  Infinite entropy gives the inequality automatically. The ratio argument
  excludes zero J, retains positive denominators in the approximation,
  allows minus-infinite infima and gives plus infinity for an empty test
  set. Rational masses do not imply rational obstacle coefficients.
- The cscK conclusion remains the precise MPWN imported existence
  implication with ordinary J coercivity and reduced entropy. It is not
  strengthened to an automorphism-relative or unrestricted YTD statement.
- Class variation fixes the measure throughout. Class-independent energy
  spaces and their topology use the published BJ Theorem 3.1; the derivative
  uses its Theorem 4.8. Differentiating the model quotient supplies both the
  twisted term and the derivative of the normalizing volume. The dual
  identity has the ordered J(phi,0) convention; comparison with J(0,phi)
  changes constants by dimension rather than identifying optimal constants.
- A complete continuous-measure example now continues Chapter 61's interval
  solution in class V times O(1). It computes dual energies V/6 and
  V(1/6-h^2/24), entropy 1/2, beta values 1/6 and 1/6+h^2/12,
  and rational-test ratios (4+2h^2)/(V(4-h^2)) tending to 1/V.
  The uniform error is Vh^2/8. All supports are divisorial and masses
  rational, while coefficients may be real. This family is not asserted
  to determine the optimal stability constant.
- The measure-valuative criterion uses Calabi--Yau and the PL-envelope
  solution theorem. Zero dual energy is exactly the trivial Dirac measure;
  its beta invariant is zero, so the ratio excludes it legitimately.
  Finite combinations remain the test domain, without a dreaminess
  assumption or a claimed reduction to single divisor orders.
- Constraint obstacles include every model vertex, the correct central
  multiplicities and bounds at unprescribed vertices. Real-weight Legendre
  duality is proved in both directions and includes attainment. The exact
  gap characterizes maximizing thresholds; zero weights allow independent
  slack, while positive weights force contact.
- The mass derivative uses the oriented variational remainder and the
  uniform fixed-complex estimate. Its constant is independent of minimum
  mass. Division occurs only for a positive remainder; inward directions
  at zero coordinates are feasible and tangent to the simplex. An arbitrary
  slack threshold cannot replace the normalized solution in that derivative.
- Threshold variation constructs affine PL obstacles on one fixed full
  vertex set. Restricted masses and orthogonality remove unprescribed
  vertices. Fixed continuous nodal functions prove contact-mass continuity,
  and envelope first variation proves C1 regularity. Contact does not imply
  positive mass, strict concavity or C2 regularity.
- The volume integral has a finite terminal parameter detected by pairing
  with a Kähler (n-1)-power. The pseudoeffective range is closed and its
  interior is big. Siu decomposition, descent and minimal singularities
  give the residual volume. The I-maximal test-curve/ray identification
  remains the exact MPWN input; the published DXZ energy formula uses the
  positive reference mass. The single zero-volume endpoint does not affect
  the integral.
- The two-point curve calculation checks the three volume branches,
  optimizing half-lines, exact mass remainder, inward derivative and
  continuous but non-C2 threshold gradient.
- The toric example is now fully computed for P2 in class aH.
  The residual triangle has area (a-lambda)^2/2; multiplying by 2! gives
  its volume. The divisor measure has dual energy a/3 > 0 and beta zero
  after the fixed-measure canonical direction a to a-3t. The single test
  excludes positive ordinary normalized-model coercivity.
- Radial J has an exact slope identity with the volume factor. Mabuchi has
  only the stated lower slope bound. No new entropy-slope equality is
  inferred. The two recent 2026 preprints remain dated orientation claims,
  separately from the dependency-checked proof core.

Inline mathematics follows the house convention outside the preserved
coefficient correction. Compact model, completion, maximizer and volume
statements are kept together in the rendered text.

## Direct source interfaces

Six primary PDFs and forty selected pages were read and visually inspected.
The six recent announcement pages were checked for the reported claims,
hypotheses and version metadata; this is not a full dependency-proof audit
of either recent preprint.

| Source | Interfaces | Physical pages inspected |
| --- | --- | --- |
| MPWN, arXiv 2509.09442 v1 | Definitions, entropy/cscK scope, orthogonality, constraints, model identities, completion, beta and volume | 1--3, 13, 17--18, 27, 30--40 |
| BJ, published Contemporary Mathematics 810 (2025) author offprint | Class-independent spaces, twisted continuity and fixed-measure differentiability with proofs | 29--30, 33--35, 37--39 |
| Published DXZ, Geometry and Topology 29 (2025) | Test-curve energy, finite-energy RWN correspondence and proof | 11, 14--15 |
| Published BJ divisorial-stability author offprint, DOI 10.1515/crelle-2023-0062 | Projective scope, finite divisorial combinations, dual energy and beta orientation | 1--5 |
| BJ, arXiv 2602.10800 v2 | Reported projective YTD overview and hypotheses | 1--3 |
| Trusiani, arXiv 2605.30063 v2 | Reported relative projective theorem, approximation and entropy statements | 1--3 |

The first three cached PDFs were reopened directly. The BJ stability offprint
and both recent versioned PDFs were freshly fetched. The BJ source's printed
pp. 187--188 and 191--197 contain the precise synthetic interfaces. The
published DXZ formula is printed p. 279, with Theorem 2.6(iii) and its proof
on pp. 282--283. The recent arXiv headers are dated 19 May and 17 August
2026. Their hypotheses are not folded into the earlier analytic-model
proofs or extended to arbitrary nonprojective Kähler classes.

PDF SHA-256 values, in table order:

1. 54c7f7e75bc9869f979fff2c2e0e56079660a408cc18d2df95d327dff01b7464
2. 4ecf20801f0871223ddfc1ea3e09927904affaab75bb5e195bfe55a2b0f09498
3. 467778ff37b893681482e43b4d8f1d717e947a34fe61026b2e6bc418e4a1f70e
4. 35c76c4c132885f57446c2c83b3eda6cf1fc591719cf9c2880b172cdfeae8f19
5. cd3a7c63ad35e48ef1d9e8bffe281d6d4a8c70d57a126c04d9139b28c1604cdb
6. aa00afeb58947e0f839d5f1af752c83c429b407d387166b624cb3f6315589712

## Verification and preservation

The exact-arithmetic supplement passes 11,194 checks across 41 families:
the surface positive products and translation boundary, the factor n,
constraint integrals/contact/duality, convexity and contraction, oriented
remainders, zero-weight slack, inward derivatives, fixed versus moving
measures, continuous rational tests, interpolation errors, toric volume and
beta, and rational simplex rounding. These finite calculations supplement
the proof review and do not establish the general imported theorems.

The legacy house-audit executable is unavailable. Manual and scoped review
pass: balanced environments, no duplicate or missing reusable labels, no
proofless formal assertions, no double dollars and no unfinished markers.
All 24 legacy inline delimiter occurrences are confined to the byte-preserved
2,112-byte coefficient correction. Its SHA-256 remains
204ca71038019e4ca4b24aba3b89e54965ef8586fe433a511619e4a54933ee25.
The prior verification receipt is not extended to the edited chapter.

Post-render references pass for 425 input files and 12,241 labels.
All six reference-checker tests and the inventory check pass. The inventory
remains 42 atoms in twelve environments, tiers (0,3,7,15,17).
The scoped review and git diff --check pass.

Final full build: 4,134 pages, 19,291,465 bytes.
PDF SHA-256:
21ab050f731bf67c05cfe8fda67f53ac1b40d614223f26f68273e5387b4d5b89.
Chapter SHA-256:
82b7486fd410b47a2c47ecf99377920003c0110f3e2cac6ae5fd3e06ccaea358.
There are no unresolved references/citations, missing glyphs, rerun requests
or fatal errors. Chapter 62 has no overfull boxes or LaTeX/package warnings.
Eighteen overfull boxes elsewhere and thirteen duplicate PDF destinations in
Chapter 70 remain recorded for the later pass.

All 26 physical chapter pages 3275--3300 (printed 3205--3230), and both
adjoining seams, were inspected at detail size. The last repair changed
26 chapter/seam images, all reinspected; the two other final images match
their inspected preceding versions byte for byte. Physical 3300 is
intentionally blank. No reviewed chapter layout defect remains.
The review PDF is saved at
/workspace/book-completion-drafts/Chapter_62_Final_Review_2026-10-02.pdf.
This direct editorial/source audit claims no new independent verifier
verdict. Verified work remains local pending explicit remote-push approval.
