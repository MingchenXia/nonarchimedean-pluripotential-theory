# Continuation and fresh-clone audit — 22 September 2026

## Starting point and source recovery

Work resumed from commit `179c0cdd5697d18e9f5eba985dec286daa09a840`
(`Add affine cross-collar smoothing for two stars`, 20 September 2026),
in a fresh clone of the existing private repository, initially clean and
matching `origin/main`.

The initial full build failed because Chapter 70 included
`p122_curve_ideal_psh_functoriality_20260911/CURVE_PSH.tex`, absent from
the fetched history. Eight missing labels caused thirteen unresolved
file/label pairs in the 388-file available closure. The include had first
appeared in `b944553` without the target file.

**The author has now supplied the original file.** It is restored without
changes, with its hash and provenance in the
[recovery build receipt](source_recovery_build_20260922.md).
The recovered graph contained 389 TeX files and 11,475 unique labels,
with no missing input or unresolved reference. The current full build
passes and produces 3,403 pages. Its 38 horizontal layout overflows remain
to be reviewed. The historical release artifacts are preserved; the
current build is not a declaration that the mathematical audit is complete.

The earlier scoped receipts below describe the checks made while recovery
was pending. Their former build limitation is superseded by this recovery.

## Chapter 16: explicit geometry of the affine collar

Added `ex:p071-cross-collar-corner-coupling` directly after the existing
affine cross-collar smoothing proposition. This is a worked application and
an elementary explanation of its hypotheses, not a new research theorem:

1. Subtract the common affine minorant. The resulting nonnegative convex
   function vanishes at the five vertices of
   `Q = [0,R0]^2 intersect {r+s <= R0+delta}`, hence on all of `Q`.
2. The nine independently chosen nonnegative coefficients in
   `a_ij max(0,r+s-R0-delta)` give admissible mixed terms in the remaining
   corner. A four-point rectangular difference proves nonseparability when
   `a_ij > 0`; zero coefficients cause no exceptional case.
3. The existing proof's geometric tails give the explicit upper error
   `(5/3) 4^(-n)` and the common collar shift `(17/12) 4^(-n)`.

Chapter 72 now points to the example and describes coupling compatible with
the collar. P07.1 remains open. The exact existing statement and proof files
were not edited; their SHA-256 values still equal
`2e538f70b29d2ce359902f5ff16931d750112dc4e6a81903075c08e604b1296e`
and
`396d2be290d6262c68468c0b1e0490bf919ec3e504f4c79edd7797d29593f922`.
Those receipts do not purport to verify the newly added exposition.

## Source-check repair and validation

The former reference checker silently omitted absent inputs and returned
exit status zero even after printing unresolved references. It also missed
lowercase `cref` commands. The checker now reports missing inputs, checks
both reference cases and starred variants, ignores commented TeX, and
returns a failing status for missing files, unresolved or duplicate labels,
or structural defects. Its programmatic `closure()` also refuses an
incomplete graph.

- Six regression checks pass: missing input, missing root, lowercase
  multi-reference, nested includes with comments and escaped percent signs,
  duplicate labels, and unbalanced environments.
- The real repository correctly returns status 1 for its pre-existing
  missing input and thirteen unresolved references. The available closure
  has 11,428 distinct labels, with no duplicate or per-file structural defect.
- The exact open-problem inventory passes: 46 active atoms in 14 formal
  environments; tiers `(0,5,8,16,17)`.
- The new example passes the strict Mingchen writing audit with zero errors
  and zero warnings; a second statement-to-calculation reading confirms the
  collar geometry, nonseparability, geometric sums, and degenerate coefficients.
- A temporary `includeonly` driver compiles Chapter 16 into a 341-page
  diagnostic PDF. Its thirteen external-reference warnings concern chapters
  and appendices unavailable to that scoped build. This is not a full-book
  build or a release. The new example and its internal citations resolve.
- Physical pages 164–167 of that diagnostic PDF were rendered and inspected;
  the example is on physical pages 165–166 (printed pages 832–833), with no
  clipping, overlap, or broken display at the insertion or its transitions.
- `git diff --check` passes.

Temporary build drivers, logs, and PDFs follow the existing ignore rules.

## Chapter 60: relative numerical nefness

The numerical reduction in `thm:mp-model-closedness` now has a detailed
proof using ambient Kähler test classes, fibrewise positivity, base-class
correction, and a uniform shrinking parameter. The normalization in the
polynomial identity is checked explicitly; a printed normalization slip in
the primary source is recorded rather than repeated. The analytic-cycle
core remains an import with its actually checked preprint version specified.

The [source and validation audit](ch60_relative_nef_audit_20260922.md)
records exact published Demailly–Păun locators, the distinction between the
import and the reconstructed reduction, and the second-pass checks. The
84-page scoped Chapter 60 build has no overfull box or unresolved citation;
its two external-reference occurrences are inherited from the scoped
baseline. The revised proof and the energy display were visually checked.
This does not repair the missing Chapter 70 source or constitute a full build.

The follow-up in the same audit now gives the snc model-independence
descent using dominating inverse-image cycles. It retains the normal-model
assertion as an explicit import and corrects the introduction's line-bundle
claim and fixed-background cone terminology. The new proof has passed the
second reading, scoped compilation, source check, and visual inspection.

The Fubini--Study warning now distinguishes rational algebraic line-bundle
models from unrestricted analytic models and records the BJ dominating
ample locus. Appendix I includes the proper-morphism fibre criterion used
in that explanation. The same source audit records the published BJ
locators, second-pass checks, and the unchanged Chapter 71 comparison.

Appendix I's compact dependency table has also passed its layout follow-up:
all 21 rows are preserved, tags print upright, and explicit column spacing
separates the longest statements from the chapter links. The complete table
fits on one page in the final scoped build.

The Chapter 60 maximum proof now specifies the sum ideal, its sign and
denominators, and the fixed-resolution limit proving relative nefness.
The common relative Kähler extension argument has a separate lemma used
by both this proof and the numerical criterion. The final scoped build
has 85 pages and no new unresolved source reference; the source graph has
11,429 labels. The detailed audit records the second-pass checks.

The model-measure pass proves mass one for signed model measures and
nonnegativity for all relatively nef model classes. The deformation-to-the-
normal-cone example now states the required center and rationality
hypotheses and treats point blowups on curves separately. The
[measure and energy audit](ch60_model_measure_energy_audit_20260922.md)
records the second-pass checks and the next energy-domain issue.

The energy pass now gives the weighted intersection-matrix proof of the
Zariski inequality and defines the real model domain before differentiating.
Monotonicity uses the difference of ordered endpoints only as a nonnegative
function; concavity includes dimension zero. The same measure and energy
audit records the source correction and the 87-page scoped validation.

The monotone-completion pass now supplies fixed-model decreasing
rational approximants for real nef model functions, closes the psh class
under arbitrary decreasing nets, and proves agreement of the extended
energy with real model intersections. It also restores connectedness,
handles dimension zero and preserves rationality in divisorial comparison.
The [completion audit](ch60_monotone_completion_audit_20260922.md)
records the exact dependencies and the 88-page scoped validation.

The finite-energy measure pass now defines the required differences of
finite pairings and proves positivity, mass, uniqueness and weak convergence
using the positive-functional construction. The
[measure and energy audit](ch60_model_measure_energy_audit_20260922.md)
records the 89-page scoped validation and 11,431-label source closure.

The ray pass now states joint psh and upper growth conditions, defines
the signed normalized Lelong number with the central multiplicity, and
exhausts logarithmic truncations in the regularization deduction. It also
corrects the earlier maximum proof to use squared norms. The
[ray audit](ch60_ray_normalization_audit_20260922.md) records both the
remaining imported analytic input and the 90-page scoped validation.

## Chapter 46: finite pairings and model tests

The [pairing audit](ch46_finite_pairing_audit_20260922.md) records the
corrected nef finite-energy domain, positive test decomposition,
coupled-pair extension, signed-measure variation bound, and integrable
representatives. A blowup intersection and an atomic curve calculation
explain the invalid shortcuts. The scoped build has 124 pages; its 22
external-reference occurrences disappear in the restored full build.

## Chapters 47–49: support and capacity

The [support audit](ch47_49_support_capacity_audit_20260922.md) replaces
the unsupported general full-mass inference with the proved atomic
statement, smooth-curve case and finite-height-moment criterion.
The new model example has capacity one on every uniform height tail.
Dependent Chapter 47 sup bounds and Chapter 48 endpoint arguments now
use divisorial determination and integrability directly.
The complete build still has 3,403 pages, now with 11,476 labels and no
missing or dangling reference. The 38 horizontal overflows are unchanged.

## Chapter 46: curve energies and finite identities

The [curve and identity audit](ch46_curve_and_finite_identities_audit_20260922.md)
reconstructs the Dirichlet energy through finite convex model
interpolation and branch exhaustion. It retains distributional corner
atoms and separates the graph measure from the finite-energy operator.
The cocycle, tangent and integration-by-parts identities now follow
from the finite pairing; the Gram-matrix limit treats nef backgrounds.
The full build remains 3,403 pages with all 11,476 labels resolved.

## Chapter 60: maximal rays and limits

The [maximal-ray audit](ch60_maximal_ray_audit_20260922.md) distinguishes
fixed-time complex energy continuity from identification of the limiting
non-Archimedean data. The latter remains part of the imported general
Kähler existence theorem. The projective proof's additional energy
inequality and strict monotonicity are identified by exact locators.
A new proposition proves order preservation and translation, and a
constant-in-space example computes the failure of interchanging the
approximation and time limits for general psh rays.
The full build has 3,405 pages and 11,480 resolved labels, with the same
38 horizontal overflows.

## Chapter 60: test-curve and mixed-slope normalization

The [test-curve and mixed-slope audit](ch60_test_curve_mixed_slope_audit_20260922.md)
fixes the zero base point in the DXZ correspondence and displays the
volume-normalized energy integral. The mixed-slope calculation now
records the intersection coefficient for the average term, the
probability normalization of d1, and a bound uniform in the model
index. The complete build has 3,405 pages and 11,481 resolved labels;
the 38 horizontal overflows remain.

## Chapters 59–62: reduced entropy slopes

The [reduced entropy audit](ch60_reduced_entropy_slope_audit_20260922.md)
records the analytic snc fibre-volume calculation, its reduced
discrepancy divisor, and the entropy variational argument. The
normalizer for total discrepancy has slope one, explicitly exposing
the old normalization error. Directed model limits are justified by
compactness and Radon integration. Chapter 62 now records the
corresponding Mabuchi lower bound, while entropy equality and the
deep cscK existence input remain separate.
The full build has 3,407 pages and 11,486 resolved labels, with the
same 38 horizontal overflows and unchanged open-problem inventory.

## Whole-book layout: table font scope

The [font-scope audit](ch18_font_scope_audit_20260922.md) traces the
unexpected body-size reduction to two Chapter 18 longtables. Four
grouping lines confine their small type to those tables. All 186
entry/exit checks now report the template's 10-point body size and
12-point baseline. The full build has 3,913 pages, no unresolved
references or citations, and eight horizontal overflows.
The page increase is reflow only; no mathematical content or frozen
proof bytes changed.

## Whole-book layout: the remaining long lines

The [display-layout audit](full_book_overflow_audit_20260922.md)
records seven formula reflows and one local prose setting. Two
external sources have separate layout editions with their original
files and hashes preserved. The complete build has 3,913 pages,
11,486 resolved labels and no horizontal or vertical overflow.
The eight affected locations were rendered and inspected.

## Chapters 14 and 19: current and measure pushforward

The [pushforward audit](ch14_pushforward_sign_audit_20260922.md)
reconciles the involution statement with the book's duality convention,
checks the negative sign by embedding a point in a line, and records
the even-dimension case in Appendix J. The curve-skeleton argument
now pushes the identified Radon measure along a continuous map.
The complete build has 3,913 pages and 11,487 resolved labels,
with no horizontal or vertical overflow.

## Chapter 17: projection and metric variation

The [projection and variation audit](ch17_projection_and_variation_audit_20260922.md)
replaces arbitrary-current pullback and exceptional-set shortcuts
with canonical integration-current pushforward followed by the
continuous-potential projection formula. The model proof now keeps
ramification, residue degrees and the restriction of valuations.
A telescoping formula repairs the false closedness assertion for
the metric-variation primitive; an annulus Hessian checks it.
The final complete build has 3,915 pages and 11,489 resolved labels,
with no horizontal or vertical overflow.

## Chapter 19: curvature and the slope formula

The [curvature and slope audit](ch19_curvature_slope_audit_20260922.md)
replaces the graph-current shortcut by testing against analytic
smooth functions and using Stokes on an adapted skeleton.
The revised formulas retain annular lengths, residue-degree edge
weights, tensor powers and nonreduced-model multiplicities.
A closed-point blowup checks the weight explicitly.
The slope proof now displays its annular and residue-slope inputs,
the disc divisor calculation and scalar-extension descent, including
inseparable point multiplicities. The common strictly semistable
model is an explicit hypothesis of the finite positivity criterion.
The full build has 3,915 pages and 11,492 resolved labels,
with no horizontal or vertical overflow.

## Curve lengths, weights and compatible norms

The [length and norm audit](curve_length_norm_audit_20260922.md)
distinguishes the intersection metric from the stable lattice
metric using the published Baker--Nicaise source. Changing the
length by the gcd factor requires changing the weight by that
factor as well. A multiplicity-(2,2) blowup verifies both mass
and Lipschitz scaling. Chapters 20 and 22 and Appendix J now
use consistent definitions, and the model proof retains node
residue degrees. The full build has 3,915 pages and 11,493
resolved labels, with no horizontal or vertical overflow.

## Chapter 61: non-pluripolar points and Dirac energy

The [point-energy audit](ch61_point_energy_audit_20260922.md)
expands metric finiteness and separation, identifies the finite-energy
tangent input without a circular integrability inference, and proves
the truncation bound from model mixed probability measures.
The P1 example now controls all psh potentials and the full
variational supremum. The complete build has 3,915 pages and 11,494
resolved labels, with no horizontal or vertical overflow.

## Chapter 61: strong topology and variational limits

The [variational-limit audit](ch61_variational_limit_audit_20260922.md)
proves weak upper semicontinuity and compactness at bounded energy,
states the imported mixed estimates precisely, and reconstructs the
fixed-measure L1 limit for nets. The Calabi--Yau proof now displays
the maximizing-sequence energy bound and the order of the two
integral limits. A curve example separates weak and strong convergence
for both potentials and measures. The full build has 3,919 pages and
11,500 resolved labels, with no horizontal or vertical overflow.

## Chapter 61: model measures and sequential selection

The [model-measure audit](ch61_model_measure_audit_20260922.md)
proves weak convergence through PL tests, verifies the semicontinuous
Radon hypotheses for the directed integrals, and establishes finite
energy of retracted measures before taking their dual-energy limits.
Nested models are selected using strong quasi-distance and entropy,
including the infinite-entropy case. No countable cofinal model
system is assumed. The full build has 3,919 pages and 11,500 labels,
with no horizontal or vertical overflow.

## Chapter 61: orthogonality and envelope variation

The [orthogonality and variation audit](ch61_orthogonality_variation_audit_20260922.md)
separates raw restricted-volume mass from probability mass, writes
the contact gap with its component multiplicity, and verifies the
uniform-gap/weak-measure limit. The first-variation proof now shows
both tangent inequalities and handles positive and negative
parameters. The full build has 3,919 pages and 11,501 labels,
with no horizontal or vertical overflow.

## Chapters 61--62: domination and model normalization

The [normalization audit](ch62_model_normalization_audit_20260922.md)
repairs the domination proof at simultaneous minus-infinity points.
A blowup of P1 x P1 shows that the raw positive-product M and J
expressions change under adding a base class. The all-big-model
definition is preserved and distinguished from the normalized
model inequality with f_D >= 1.
The latter is equivalent to the finite-energy and divisorial-measure
conditions. The implication from all big models to cscK existence
remains valid. The converse to the literal raw all-big-model
condition needs an additional comparison; it is not inferred from
the disproved invariance argument.
Chapter 68 and the provenance appendix now reflect this scope.
The full build has 3,921 pages and 11,506 labels, with no horizontal
or vertical overflow. The factor-n verification block is unchanged.

## Chapter 62: finite-energy completion — 23 September 2026

The [completion audit](ch62_finite_energy_completion_audit_20260923.md)
separates the strongly continuous nonentropy term from entropy,
using the checked published twisted-energy theorem.
The fixed-complex argument now includes domination, compatible
subdivisions, real interpolation with central-fiber multiplicities,
normalization before the support formula, and one fixed discrepancy
test function. Infinite entropy is handled separately.
The normalized stability scope is unchanged.
The complete second-pass build has 3,921 pages and 11,507 labels,
with no unresolved references or citations and no layout overflow.
Frozen verification bytes and the active research inventory are unchanged.

## Chapter 62: class derivatives at a fixed measure — 23 September 2026

The [class-derivative audit](ch62_class_derivative_audit_20260923.md)
identifies the exact published differentiability theorem and the
class independence of the finite-energy measure space.
The potential-energy intersection calculation now differentiates
the volume denominator before invoking the fixed-measure theorem.
A P1 calculation gives derivatives +1/8 and -1/8 for fixed and
moving measures, respectively. The zero-energy ratio case is
handled through the trivial Dirac measure.
The complete final build has 3,923 pages and 11,509 labels,
with no unresolved reference or citation and no layout overflow.
The normalized stability scope and frozen verification bytes
remain unchanged.

## Chapter 62: finite constraints and volume — 23 September 2026

The [finite-volume audit](ch62_finite_volume_audit_20260923.md)
constructs the continuous obstacle using all model vertices and
central-fiber multiplicities. The variational reduction now has both
inequalities and an attainment argument, without assuming saturation.
The volume proof establishes the finite pseudoeffective cutoff and
minimal residual singularities, using the exact published DXZ energy
normalization. A two-point P1 example checks inactive constraints,
zero weights and the remaining maximizing half-lines.
The final full build has 3,925 pages and 11,511 labels, with no unresolved
reference or citation and no layout overflow. The research inventory,
normalized-model scope and frozen verification bytes are unchanged.

## Chapter 52: endpoints, energy and decreasing limits — 23 September 2026

The [endpoint and energy audit](ch52_endpoint_energy_audit_20260923.md)
proves that normalized terminal levels remain nontrivial, reconstructs
the raw Legendre transform and the inverse closed domain, and separates
reference mass from endpoint mass. The exact relative energy source and
the half-logarithmic radial conversion are explicit.
A decreasing family of constant test curves has masses 1/j and a zero-mass
limit; the missing positive-mass assumption is restored to the limit theorem.
The final full build has 3,927 pages and 11,515 labels, with no unresolved
reference or citation and no layout overflow. The research inventory,
frozen proofs and author sources are unchanged.

## Chapters 52 and 54: projected operations — 23 September 2026

The [operations audit](ch52_operations_projection_audit_20260923.md)
corrects the Legendre formulas for sums and maxima: equality holds for
the raw families, while model projection can strictly increase the ray.
Opposite coordinate actions on P1 give an explicit strict maximum and
an ordinary sum with energy second derivative 2/3, hence not a geodesic.
The dependent Chapter 54 associativity proof now retains projection.

Arbitrary suprema pass through finite joins before increasing closure.
Countable reduction selects finite index sets at rational parameters,
and closed profiles recover every real level. Transition hypotheses
and the scaling of the Kähler perturbation are explicit.
The final build has 3,929 pages and 11,522 labels, with no unresolved
reference or citation and no overflow. The research inventory and
frozen sources are unchanged.

## Chapters 51, 53 and 54: perturbation and limits — 23 September 2026

The [perturbation audit](ch53_54_perturbation_audit_20260923.md)
proves order reflection for I-model transitions and derives a uniform
positive-mass bound from the component at half the Kähler perturbation.
The decreasing-envelope theorem is applied only after verifying its
limiting-mass hypothesis. Endpoint, terminal-parameter and greatest-
lower-bound assertions are explicit. The Kähler index set has a countable
cofinal sequence; this is now distinguished from arbitrary metric nets.
Chapter 54 citations identify the checked arXiv version separately from
the published chapter.

The final full build has 3,931 pages, 389 TeX inputs and 11,526 labels,
with no unresolved references, citations or layout overflow.
Mathematical/source review, scoped strict style review and final page
inspection pass. Frozen verifier material and the research inventory
are unchanged. The next unit checks the volume-continuity arguments
and the role of the initial-level limit.

## Chapter 54: volume continuity — 23 September 2026

The [volume-continuity audit](ch54_volume_continuity_audit_20260923.md)
separates the metric index, initial-level limit and Kähler perturbation.
The proof gives a bound uniform in the metric and distinguishes integrated
mass monotonicity from a current inequality. The increasing initial-level
identity and fixed-background analytic inputs have precise sources.
A decreasing family on P1 has volume 1 at every stage and limit volume
1-a > 0; its exact mass profile displays the two noncommuting limits.

The final full build has 3,933 pages, 389 TeX inputs and 11,531 labels,
with no unresolved references, citations or layout overflow.
The second mathematical/source pass, scoped strict style review and
final page inspection pass. Frozen sources, production verifier records
and the active research inventory are unchanged.

## Chapter 54: the analytic trace construction

The [trace-construction audit](ch54_trace_construction_audit_20260923.md)
reconstructs Theorem 54.5.1 in a fixed target background
Theta = rho^* Omega + kappa. The explicit lower bound integral kappa^m
is independent of the approximant and verifies the completeness
hypothesis before taking a singularity-metric limit.
The normalized model envelopes converge even when the raw restrictions
have pointwise limit -infinity.

Two quasi-equisingular approximations are compared with a vanishing
coefficient loss and a cofinal subsequence. A uniform scaling estimate
and closed P-order give independence in both directions. Analytic
closure, background change and canonical dyadic multiplier ideals give
I-goodness and dependence on the ambient I-class. Dimension zero is
handled separately. The approximation definition and primary-source
locators are explicit; the accepted trace-paper version has its own
bibliography entry.

The final full build has 3,935 pages and no unresolved references,
citations or layout overflow. The 389-file closure has 11,536 labels.
The second mathematical/source pass, strict scoped style review,
reference and inventory checks, and final page inspection pass.
The 46 active research atoms, frozen proof files and production records
are unchanged. The next unit audits the trace calculus and the exact
hypotheses of decreasing continuity.

## Chapter 54: trace calculus and decreasing continuity

The [trace-calculus audit](ch54_trace_calculus_audit_20260923.md)
proves compatibility of quasi-equisingular approximation with sums,
maxima and positive real scaling, using rational coefficients at the
analytic stage. Decreasing continuity is reconstructed with separate
ambient and restricted diagonal errors, normalized model envelopes,
and an explicit reduction from nets to sequences. The domain of every
net input and the absence of an I-goodness assumption on the original
inputs are checked.

The increasing counterexample now consists of global Fubini--Study
divisor weights on P2. Its inputs converge to zero in d_S, while all
traces have mass 1 in a target class where the trace of zero has mass 2.
Source versions and exact hypotheses are recorded separately.

The final full build has 3,937 pages, 389 TeX inputs and 11,540 labels,
with no unresolved references, citations or layout overflow.
The second mathematical/source pass, scoped strict style review,
reference/inventory checks and final page inspection pass.
Frozen source and verifier records and the 46 active research atoms
remain unchanged. No production verification or new atom closure is claimed.

## Chapter 54: non-Archimedean trace and closed endpoints

The [non-Archimedean trace audit](ch54_na_trace_audit_20260923.md)
reconstructs Section 54.7 from the analytic trace class. The domain is
tested at one interior level in one perturbation. A uniform lower bound
of 2^(-m) times the target Kähler volume supplies positive mass before
model-envelope completeness is used, and remains valid at the closed
cutoff. The proof checks normalized concavity, initial and terminal
limits, perturbation transitions and birational pullback with a smooth
ambient manifold upstairs.

The worked hyperplane example has ambient terminal parameter 1 and
trace cutoff 0, with the cutoff level retained. Its Chapter 52 dependency
now treats nonpositive filtration parameters correctly and uses
I-goodness under real scaling instead of claiming irrational analytic
singularities. Exact primary-source locators and the second mathematical
pass are recorded in the audit.

The final full build has 3,939 pages, 389 TeX inputs and 11,548 labels,
with no unresolved references, citations or layout overflow. Scoped
strict style, reference/inventory and final visual checks pass.
Frozen source and verifier records, the supplied curve file and the
46 active research atoms remain unchanged. No independent-agent or
production verification and no new atom closure are claimed.

## Chapter 57: finite-section realization and trace comparison

The [trace-comparison audit](ch57_trace_comparison_audit_20260923.md)
replaces the finite-section concavification sketch by an explicit sliced
simplex formula. Rational levels have analytic singularities; real levels
use I-goodness. The existing P1 example now displays its raw maximum.
The big-class hypotheses in the imported realization theorem are checked
using half of the chosen ample perturbation.

The nontriviality criterion is proved with a common-background GF
approximation and its uniform mass bound. This establishes the cutoff
identity at the proper-support trivial valuation before the trace theorem
is used. Restriction of finite-section levels is performed on the face of
surviving sections and only inside the trace domain. Convergence of the
cutoffs and a compact interval for maximizing parameters justify the
Legendre supremum limit. A P2 example distinguishes a nontrivial line
restriction from an undefined trace at a point on that line.

The final complete build has 3,941 pages, 389 TeX inputs and 11,556 labels,
with no unresolved references, citations or layout overflow. The second
mathematical/source pass, strict scoped style audit, reference/inventory
checks and final visual inspection pass. Frozen proofs, author sources,
production verifier records and all 46 active research atoms are preserved.
No independent-agent or production verification and no atom closure are
claimed. The next unit checks Chapter 56's Gauss complexification and
multiplier-ideal approximation, including proper-support behavior.

## Chapter 56: Gauss normalization and multiplier-ideal approximation

The [Gauss and multiplier-ideal audit](ch56_gauss_multiplier_audit_20260923.md)
checks the rational Gauss normalization and the common upper bound
needed for complexification. The hyperplane example is shifted to
terminal parameter zero before its central-fiber calculation. Its
ideal is that of H times {0}, and its exact multiplier ideals give
explicit dyadic approximants, including proper-support values.

The product-ideal equality over the punctured disk is proved with
an annulus rooftop sandwich. The uniform generation argument now
extracts global generators of every coefficient ideal, retaining
the possibly nonunit terminal ideal. The decreasing GF formula has
explicit section weights, a noncollapse check, and uniqueness by
two-sided divisorial domination among psh extensions. The same
argument identifies different perturbations at all points.

The final full build has 3,941 pages, 389 TeX inputs and 11,562 labels,
with no unresolved references, citations or layout overflow. The
second local mathematical/source pass, strict scoped style audit,
reference/inventory checks and final visual inspection pass.
The 46 active atoms, frozen proofs, author sources, production
verifier records and dated release artifacts are preserved.
No independent-agent or production verification and no atom closure
are claimed. The next unit checks Chapter 57's order reflection,
valuation scaling and closed parameter profiles for Legendre inversion.

## Chapter 57: order reflection and rational valuation rays

The [order-reflection audit](ch57_order_reflection_audit_20260923.md)
reconstructs the comparison proof using positive rational valuation
scaling. The new interior inversion lemma proves finiteness and
continuity of the scalar dual, including its limit at zero. Interior
I-model order is then extended to the endpoint by decreasing potential
limits, including zero terminal mass. BJ domination supplies the
passage from divisorial inequalities to all analytic points.

Two explicit O(2) metrics on P1 agree at the trivial valuation and
every unscaled prime order, but differ at half of one prime order.
The dependent operations proof now treats real parameter rescaling
separately and identifies arbitrary suprema as least upper bounds.

The final full build has 3,941 pages, 389 TeX inputs and 11,566 labels,
with no unresolved references, citations or layout overflow. The
second local mathematical/source pass, strict scoped style audit,
reference/inventory checks and final page inspection pass.
Previously checked GF and trace blocks retain their exact bytes.
The 46 active atoms, frozen proofs, author sources, production
verifier records and dated release artifacts are preserved.
No independent-agent or production verification and no atom closure
are claimed. The next unit checks decreasing-net comparison, uniform
positive mass and the Legendre limit in Chapter 57.

## Chapter 57: decreasing nets and the Legendre limit

The [decreasing-net audit](ch57_decreasing_net_audit_20260923.md)
reconstructs Chapter 57's limit comparison from the uniform positive-mass
bound in Chapter 54. A countable subfamily with the same pointwise
infimum permits the sequential Lelong theorem to control the whole net;
no cofinal sequence is assumed. A compact-parameter subnet argument
then proves the Legendre limit, including maximizers approaching a
zero-mass endpoint. BJ closure and divisorial determination give the
identity on every analytic point.

The new P1 calculation identifies the metrics as max(-a v(I_p),-j).
Their values at p tend to minus infinity while the trivial valuation
stays at zero. Their volumes are 1 and the limiting volume is 1-a,
making the distinction from decreasing volume continuity explicit.
The constant-collapse example now uses the full divisorial formula.

The second local mathematical/source pass, strict section-wide style
audit, reference/inventory checks and final page inspection pass.
The final full build has 3,943 pages, 389 TeX inputs and 11,569 labels,
with no unresolved references, citations or layout overflow.
All Chapter 57 bytes outside the decreasing-limits section are preserved.
The 46 active atoms, author sources, frozen proofs, production verifier
records and dated release artifacts are unchanged. No independent-agent
or production verification and no atom closure are claimed.
The next unit checks Chapter 58's support and center construction,
prime coherent ideals, support descent and local point criteria.

## Chapter 58: support, center and local recovery

The [support and center audit](ch58_support_center_audit_20260923.md)
specifies the global coherent-ideal meaning of prime, proves its
radical/irreducible interpretation, and explains the compactness
needed for finite sums. A nodal cubic distinguishes this condition
from primality of the analytic stalk at a node.

The support-stratum proof now checks canonical ideal lifts and both
inverse maps. Point-center reconstruction uses exact ideal sandwiches
and the finite truncation formula v(a_k(f))=min(w(f),k v(m_p)),
including infinite maximal-ideal value and the zero stalk.
The revised section cites the checked final author version v2 through
a separate bibliography entry; the published entry is preserved.

The second local mathematical/source pass, strict section-wide style
audit, reference/inventory checks and final page inspection pass.
The full build has 3,943 pages, 389 TeX inputs and 11,572 labels,
with no unresolved references, citations or layout overflow.
All other Chapter 58 text and pre-existing bibliography entries retain
their exact bytes. The 46 active atoms, author sources, frozen proofs,
production verifier records and dated release artifacts are unchanged.
No independent-agent or production verification and no atom closure
are claimed. The next unit checks proper bimeromorphic transport,
the lifted character's positivity, twist independence and resolution.

## Chapter 58: bimeromorphic transport and conductor descent

The [bimeromorphic transport audit](ch58_bimeromorphic_audit_20260923.md)
reconstructs the full-support bijection for proper bimeromorphic maps
without dropping nonnormal spaces. A conductor calculation handles
finite maps; normalized blowups and integral closure justify positivity
and equality of values for equal pullbacks on a normal base. The
relative-ampleness formula now checks every choice, sum and product,
the zero ideal, the unit, and uniqueness. The common-resolution
argument proves general surjectivity before using it for the second
arrow, and finite normalization recovers the original scope.

A nodal cubic gives an explicit ideal that does not descend despite
relative generation, then shows how the conductor repairs it. Its
two point characters also disprove bijectivity on all support strata.
Geometric source inputs and the limits of primary-source access are
identified in the audit; no new research theorem is promoted.

The second local mathematical/source pass, strict full-block style
audit, reference/inventory checks and final page inspection pass.
The final full build has 3,945 pages, 389 TeX inputs and 11,575 labels,
with no unresolved references, citations or layout overflow. The
chapter's text outside the unit and the bibliography retain their
exact bytes. The 46 active atoms, supplied CURVE_PSH.tex, author sources,
frozen proofs, verifier receipts and dated releases are unchanged.
No independent-agent or production verification and no atom closure
are claimed. The next unit checks proper algebraic recovery, GAGA,
centering and the comparison topology in Chapter 58.

## Chapter 58: proper algebraic recovery and topology

The [proper algebraic recovery audit](ch58_algebraic_recovery_audit_20260923.md)
reconstructs GAGA as an ideal-semiring identification, recovers a local
valuation using colon ideals and extension of finite ideal generators,
and proves the comparison topology by finite closed affine bounded sets.
The original proper scope, including nonprojective and nonnormal
varieties, is preserved. A P1 Gauss family distinguishes continuous
ideal coordinates from the discontinuous center map; the complex-line
sine ideal exhibits the separate nonproper GAGA obstruction.

The exact SGA 1 reprint was checked against its publisher record and
the cited pages. Its new bibliography entry preserves the 1971 entry.
The second local mathematical/source pass, strict block style audit,
reference/inventory checks, final full build and page inspection pass.
The build has 3,947 pages, 389 TeX inputs and 11,576 labels, with no
unresolved references, citations or layout overflow. The bibliography
audit's exact-version preprint warning was reviewed and its source-access
limit recorded. All earlier bibliography entries and the Chapter 58
text outside the recovery unit retain their exact bytes.

The 46 active atoms, author sources, supplied CURVE_PSH.tex, frozen
packets, verifier receipts and dated releases remain unchanged.
No independent-agent or production verification and no atom closure
are claimed. The next unit checks Chapter 59's normalized blowups,
integral-closure values and the divisorial converse.

## Chapter 59: integral-closure values and divisorial tests

The [integral-closure comparison audit](ch59_integral_closure_audit_20260923.md)
replaces unsupported local-germ evaluation by a uniform identity of
global coherent ideals and proves value invariance for all semivaluations,
including infinite values. The analytic normalized-blowup formula now
states its hypotheses and exact published source. The divisorial
converse is proved by a finite test, with zero ideals, unit ideals,
local branches and nonexceptional divisors treated explicitly.
A projective-plane calculation and a curve example show why neither
divisors on X alone nor exceptional divisors alone suffice.

The second local mathematical/source pass, strict full-block style
audit, reference/inventory checks and final page inspection pass.
The full build has 3,949 pages, 389 TeX inputs and 11,577 labels,
with no unresolved references, citations or layout overflow. The
new published Lejeune-Jalabert--Teissier entry preserves all earlier
bibliography bytes. The exact-version MPTropicalV2 warning and
publisher-access limitation are recorded in the audit.

Chapter 58 and all Chapter 59 text outside this unit retain their exact
bytes. The 46 active atoms, supplied CURVE_PSH.tex, author sources,
frozen proofs, verifier receipts and dated releases remain unchanged.
No independent-agent or production verification and no atom closure
are claimed. The next unit checks monomial valuations, adapted
coordinates, globalization along strata, zero weights and rational
divisorial realization in Chapter 59.

## Chapter 59: monomial valuations and cone faces

The [monomial-valuation audit](ch59_monomial_globalization_audit_20260923.md)
reconstructs coordinate independence by intrinsic divisor-ideal filtrations,
point independence by coefficient germs, and continuity by finite minimal
supports. It defines the cone faces and supplies the missing separation
of different components of a divisor intersection. Rational weights are
realized by a terminating sequence of ordinary blowups with the scalar
normalization retained. Zero weights and the dimension-one blowup are
treated explicitly. A P1 x P1 example distinguishes two cones with the
same boundary coordinates and computes a rational prime-order multiple.

The exact author-version source and the published Jonsson--Mustata
statements were checked. The second local mathematical/source pass,
strict full-block style audit, reference/inventory checks and final page
inspection pass. The final full build has 3,951 pages, 389 TeX inputs
and 11,579 labels, with no unresolved references, citations or overflow.
The exact-version preprint warning and publisher-access limit are recorded.

The earlier integral-closure unit, all other Chapter 59 text, Chapter 58,
the bibliography, 46 active research atoms, supplied CURVE_PSH.tex,
author sources, frozen proofs, verifier receipts and dated releases remain
unchanged. No independent-agent or production verification and no atom
closure are claimed. The next unit checks normalized invariant vertical
divisors, projection pullback, local algebra and global model realization.

## Chapter 59: invariant vertical divisors and model realization

The [invariant vertical-divisor audit](ch59_vertical_divisor_audit_20260923.md)
corrects the projection-pullback map and the BHJ theorem locator, proves
the relative local-ring restriction lemma, and supplies finite termination
of center blowups. It retains local branches and rational normalization.
A separate extraction on X x P1 now verifies every model condition,
including triviality off the central fiber. The examples compute the
factor 2/3 and exhibit why a product modification is insufficient.

The published BHJ and Jonsson--Mustata statements and the exact MP author
version were checked. The second mathematical/source pass, strict block
style audit, reference/inventory checks and final rendered-page inspection
pass. The complete build has 3,953 pages, 389 TeX inputs and 11,581 labels,
with no unresolved references, citations or horizontal or vertical overflow.
The exact-version preprint warning and its access limit remain documented.

All Chapter 59 text outside the unit, Chapter 58 and the bibliography
retain their baseline bytes. The 46 research atoms, author sources,
supplied CURVE_PSH.tex, frozen proofs, verifier receipts and dated releases
are unchanged. No independent-agent or production verification, new research
theorem or atom closure is claimed. The next unit checks the PL/vertical-
Cartier correspondence, its denominators and fractional flag-ideal evaluation.

## Chapter 59: fractional flags and vertical Cartier divisors

The [PL and vertical-Cartier audit](ch59_pl_vcar_audit_20260923.md)
restores rational denominators and evaluates fractional flags through
the Gauss formula on X x P1. It proves finite integral-closure invariance
and injectivity before using divisorial density, constructs a vertical
relatively ample divisor, and supplies uniform relative generation.
A P1 blowup computes the signs, rational factors, constant shift and
proper-support value. The density consequence uses its checked exact
source version and rational constants.

The second local mathematical/source pass, strict changed-block style
audit, reference/inventory checks and final rendered-page review pass.
The complete build has 3,955 pages, 389 TeX inputs and 11,583 labels,
with no unresolved references, citations or horizontal or vertical overflow.
The whole-chapter style audit still reports legacy delimiter, label and
heading issues; its baseline comparison and source-access limits are
recorded separately. No clean whole-chapter style audit is claimed.

The earlier Chapter 59 units, the text from its dual-simplex definition
onward, Chapter 58 and the bibliography retain their exact baseline bytes.
The 46 research atoms, author sources, supplied CURVE_PSH.tex, frozen
proofs, verifier receipts and dated releases are unchanged. No independent-
agent or production verification, new research theorem or atom closure
is claimed. The next unit checks dual-complex strata, retraction continuity,
model evaluation, transition maps and inverse-limit separation.

## Chapter 59: retractions and the inverse limit

The [dual-complex retraction audit](ch59_retraction_audit_20260923.md)
retains every intersection component, constructs model-ideal values at
proper-support characters, and proves continuity through a finite set of
stratum ideals. It checks the monomial section and transition maps, then
proves inverse-limit surjectivity by the finite intersection property.
A two-blowup surface example has distinct edges with the same vertices.
The affine/Cartier factors, product model and convergence of the retraction
net are explicit, including the composition used in Chapter 61.

The second local mathematical/source pass and final rendered-page review
are complete. The full build has 3,957 pages, 389 TeX inputs and 11,580
labels, with no unresolved references, citations or horizontal or vertical
overflow. The strict changed-block style audit passes; the audit records
the remaining legacy whole-chapter reports and exact-version source limit.
The earlier Chapter 59 units, its projective comparison and later sections,
Chapters 58 and 61, and the bibliography retain their baseline bytes.
The 46 research atoms, author sources, supplied CURVE_PSH.tex, frozen
proofs, verifier receipts and dated releases are unchanged. No independent-
agent or production-verifier pass, research theorem or atom closure is
claimed. Next: log discrepancy, retraction inequalities and normalization.

## Chapter 59: log discrepancy

The [log-discrepancy audit](ch59_discrepancy_audit_20260923.md)
reconstructs the analytic Jacobian bound, monomial independence, model
monotonicity and supremum extension. It corrects the exceptional-boundary
hypothesis and the domain of the Gauss comparison, with surface and curve
examples. The reduced model identity used by the entropy chapters is explicit.

Two local mathematical/source passes, the full build and final page review
pass: 3,961 pages, 389 inputs, 11,585 labels, no unresolved references,
citations or layout overflow. The scoped style audit passes; legacy chapter
reports and the exact-version source limitation are recorded in the audit.
Only Section 59.5 changed in the mathematical text. The 46 research atoms,
author sources, frozen proofs, verifier records and dated releases remain
unchanged in this unit; no new production or independent-agent pass is claimed.
The author-supplied P12.1 manuscript is being integrated as the next unit.

## P12.1: excellent normalized links

The author supplied *Normalized valuation links and boundary ideals on
excellent local germs* and requested its integration as the solution of
P12.1. The complete adapted proof is in Chapter 70, Section 70.1.1,
before the existing curve classification. It constructs compact primary
sections and their radial changes, proves lifting and the conductor
quotient, and treats blowup gauges, nonprimary sections and reduction.
The original four-page PDF is archived unchanged, with its hash and exact
source checks in the [integration audit](p121_integration_audit_20260923.md).

P12.1 is retired under the author's supplied-source instruction. The
five targets P12.2--P12.6 retain their stated open scopes. Chapter 72,
Appendix L, the inventory and tier queue, the count checker, BOOK_PLAN,
research ledger and README now agree on 45 active atoms in 14 environments,
tiers (0,5,8,15,17). This is supplied-manuscript provenance, not a new
production Rethlas or independent-agent verification; historical receipts
remain unchanged.

Two local proof/source passes, strict fragment audit, full build and
scoped final page review pass. The book has 3,965 pages, 390 TeX inputs
and 11,597 labels, with no unresolved references/citations or layout
overflow. The audit records all checked pages and preserved source bytes.
The preceding Chapter 59 discrepancy unit is separately committed and
pushed as fd272ed. Existing proof packets, author files, bibliography,
verifier records and dated releases are unchanged.

## Chapter 59 projective comparison and examples: 23 September 2026

The [projective comparison and nonalgebraic examples audit](ch59_projective_examples_audit_20260923.md)
matches algebraic and analytic ideal coordinates, boundary multiplicities,
retractions and PL divisor coefficients, with exact BJ22 locators.
The torus example proves generic existence with NS = 0 and computes the
point-blowup dual interval. The K3 example computes both blowup charts,
all weight faces, two global separating ideals and discrepancy 2s+3t.
The source note identifies the exact MP author version; the K3 sources
are added with verified publication metadata.

Two local mathematical/source passes, final rendering and the complete
build pass: 3,965 pages, 390 inputs, 11,599 labels, no unresolved references,
citations or layout overflow. The scoped strict style audit passes; the
remaining legacy chapter style reports are recorded separately. The earlier
Chapter 59 text and discrepancy section, P12.1 proof and supplied-source
provenance, all 45 active research atoms, frozen packets, verifier records
and dated releases are preserved. No new research theorem, atom closure,
independent-agent pass or production-verifier receipt is claimed.

## Chapters 59–60: notation and model definitions, 23 September 2026

The [notation and model-definition audit](ch59_notation_ch60_model_definitions_audit_20260923.md)
completes Chapter 59's remaining inline notation, definition-heading and
source-version pass. Its 17 proofs retain their mathematical content.
Chapter 60 defines the potential on all characters through the model
retraction, specifies relative positivity on reduced fibres, and separates
the rational and real classes. The point-blowup example computes the
nef interval [0,1], the relatively Kähler interval (0,1), and a horizontal
curve of negative degree. The zero-dimensional case and the some-model
quantifier for H(alpha) are explicit.

Two local mathematical/source passes and the final build/render check are
complete: 3,967 pages, 390 TeX inputs, 11,601 labels, no unresolved references,
citations or layout overflow. Chapter 59 and the changed Chapter 60 block
have zero house-audit errors; the audit records their reviewed label and
source-version warnings. All 19 existing Chapter 60 proofs and its text
from the model-category warning onward are preserved, apart from the exact
source locator in the first proof. The completed P12.1 integration and
author provenance, all 45 active atoms, supplied sources, frozen packets,
verifier receipts and dated releases are unchanged. No new independent-agent
or production-verifier pass is claimed.

## Chapter 60: rational scaling and finite pullback, 23 September 2026

The [scaling and finite-pullback audit](ch60_scaling_pullback_audit_20260923.md)
supplies a PL representative before rational descent, computes the flag
base-change formula, and proves nef reflection after resolution using
dominating inverse-image cycles. It reconstructs finite pullback on graph
models and proves that the pulled-back background is Kähler; the finite
map need not be surjective. The P1 examples distinguish 2·phi from 2 phi,
exclude irrational breakpoints from PL_R, and compute the change under
z -> z^d.

Two local mathematical/source passes, the final full build and the scoped
page review are complete. The book has 3,969 pages, 390 TeX inputs and
11,607 labels, with no unresolved references, citations or layout overflow.
The changed-block style audit has zero errors and one reviewed exact-version
source warning. The earlier model definitions, entire maximum proof and
all text from model closedness onward are preserved. The audit records
primary locators, source hashes and the final PDF hash. All 45 research
atoms, P12.1 integration/provenance, supplied sources, frozen packets,
verifier records and dated releases are unchanged. This unit claims no
new independent-agent or production-verifier pass.

## Chapter 60: model measure and pairing normalization, 23 September 2026

The [model measure and pairing audit](ch60_model_measure_pairing_audit_20260923.md)
proves the constant-fibre, zero-potential and rational-scaling pairing
identities, and derives the correctly oriented pushforward of model
Monge–Ampère measures. It supplies the relative Kähler argument in the
normal-cone example, the exact Zariski equality graph and a nonconstant
zero-seminorm example. Energy translation, rational homogeneity and
nonnegativity of J are proved from the model pairing, including dimension zero.

Two local proof/source passes, the final full build and scoped page review
are complete: 3,973 pages, 390 inputs and 11,614 labels, with no unresolved
reference/citation or layout overflow. The scoped house audit has zero
errors and one reviewed exact-author-version warning. Earlier Chapter 60
model constructions and all text from monotone completion onward retain
their baseline bytes. All 45 research atoms, the completed P12.1 integration
and supplied-source provenance, author originals, frozen packets, verifier
records and dated releases are preserved. No independent-agent or
production-verifier pass is claimed.

## Chapter 60: finite vertices and divisorial comparison, 23 September 2026

The [divisorial comparison audit](ch60_divisorial_comparison_audit_20260923.md)
proves analytic negativity for the model blowups, the finite vertex test
for PL obstacles, and a fixed-model oscillation bound by an explicit
weighted-graph recursion. The proof handles arbitrary real Kähler weights,
single-vertex models and dimension zero. It derives divisorial finiteness
from the original decreasing net and constructs continuous majorants for
upper semicontinuous comparison. The obstacle supremum is continuous in
the divisorial topology; a P1 example attains the graph bound and has a pole
at the supported endpoint.

Two local proof/source passes, the final full build and scoped page review
are complete: 3,975 pages, 390 inputs and 11,623 labels, with no unresolved
reference/citation or layout overflow. The scoped house audit has zero
errors and one reviewed exact-author-version warning. Earlier Chapter 60
text and all text from the extended pairing onward retain their baseline
bytes. All 45 research atoms, completed P12.1 integration and supplied-source
provenance, author originals, frozen packets, verifier receipts and dated
releases are unchanged. No independent-agent or production-verifier pass
is claimed.

## Chapter 60: extended pairings and finite-energy measures, 23 September 2026

The [extended pairing audit](ch60_extended_pairing_audit_20260923.md)
proves upper semicontinuity from continuous obstacle suprema and derives
decreasing-net continuity and exact real translation. An explicit common-
background estimate, proved by concavity and intersection expansion,
establishes mixed finiteness before twisted and test-function differences.
The measure construction now depends on these proved steps. A curve example
has convergent model measures but energy tending to minus infinity.

Two local mathematical/source passes, final full compilation and scoped
page review are complete: 3,979 pages, 390 inputs and 11,630 labels, with
no unresolved references/citations or layout overflow. The scoped house
audit has zero errors and one reviewed author-version warning. All earlier
Chapter 60 text and the radial-limit section onward retain their baseline
bytes. The 45 research atoms, P12.1 integration/provenance, supplied originals,
bibliography, frozen packets, verifier records and dated releases are
unchanged. No independent-agent or production-verifier pass is claimed.

## Chapter 60: radial limits and flag regularization, 23 September 2026

The [radial regularization audit](ch60_ray_regularization_audit_20260923.md)
proves the finite invariant flag expansion and reconstructs the passage
from Demailly's local Bergman regularization to relatively nef model
classes. A smooth disc correction removes the product curvature loss.
The proof quantifies divisorial approximation by the product discrepancy
and keeps the dyadic, background and cutoff limits separate. A constant
ray computes the exact multiplier ideals and tests the necessity of
cutoff exhaustion. The original Demailly source is now directly checked;
the analytic regularization theorem remains explicitly cited.

Two local proof/source passes, the final full build and scoped page review
are complete: 3,979 pages, 390 inputs and 11,637 labels, with no unresolved
reference/citation or layout overflow. The scoped house audit has zero
errors and one reviewed exact-author-version warning. All earlier Chapter 60
text and all text from maximal rays onward retain their baseline bytes.
The 45 research atoms, P12.1 integration/provenance, supplied originals,
bibliography, frozen packets, verifier records and dated releases remain
unchanged. No independent-agent or production-verifier pass is claimed.

## Chapter 60: quantitative stability of maximal rays, 24 September 2026

The [maximal-ray stability audit](ch60_maximal_stability_audit_20260924.md)
proves that the ray order reflects both initial values and non-Archimedean
data. Affine translation gives the sharp B+C s perturbation bound.
The explicitly cited energy identity yields an exact ordered d1 formula,
a finite-energy maximality criterion, and decreasing convergence uniformly
on bounded time intervals. The pointwise limit is identified by its energy.
Constant rays show why uniformity on the whole half-line fails; the earlier
non-geodesic counterexample remains. General Kähler existence and its
data identification retain their explicit source boundary.

Two local proof/source passes, final full compilation and scoped page
review are complete: 3,981 pages, 390 inputs and 11,643 labels, with no
unresolved references/citations or layout overflow. The scoped house
audit has zero errors and one reviewed exact-version warning. The entire
earlier Chapter 60 text and all text from the test-curve comparison onward
retain their baseline bytes. The 45 active atoms, completed P12.1
integration/provenance, supplied originals, bibliography, frozen packets,
verifier receipts and dated releases are preserved. No independent-agent
or production-verifier pass is claimed.

## Chapter 60: test-curve order and mass defect, 24 September 2026

The [test-curve comparison audit](ch60_test_curve_comparison_audit_20260924.md)
gives the inverse transform at all parameters with the closed endpoint,
proves the finite-energy order correspondence and parameter translation,
and identifies the cutoff by comparison with constant data. The mass
defect equals J and the distance from the upper constant ray is exactly
s J; its vanishing characterizes constant data. The projective-line
example checks a zero-mass terminal level and equal-energy incomparable
data. The probability energy identity now uses the preceding maximal-ray
identity rather than the later mixed-slope theorem. The analytic
correspondence and I-maximality of the inverse remain cited inputs.

Two complete local proof/source passes, final full compilation and scoped
page review are complete: 3,983 pages, 390 inputs and 11,648 labels, with
no unresolved references/citations or layout overflow. The scoped house
audit has zero errors and one reviewed exact-version warning. Earlier
Chapter 60 text, the full-cone scope warning and all following text retain
their baseline bytes. The 45 active atoms, P12.1 integration/provenance,
supplied originals, bibliography, frozen packets, verifier records and
dated releases remain unchanged. No independent-agent or production-verifier
pass is claimed.

## Chapter 60: simultaneous mixed-energy slopes, 24 September 2026

The [mixed-slope audit](ch60_mixed_slope_audit_20260924.md) defines the
two-point J quantity, proves its separate-translation invariance and its
bound by n times the ordered energy gap, and restores the signed
cohomological coefficient in every translated pairing slot. The proof
now regularizes all finite-energy slots simultaneously, with a uniform
error bound that tends to zero after taking slopes. The average slope
comes from the preceding cutoff identity. A Kähler-background decomposition
justifies signed-form continuity, and constant rays test the centering
terms and failure of separate-translation invariance for d1. The
dimension-zero case and full theorem's imported boundaries are explicit.

Two complete local proof/source passes, the final full build and scoped
page review are complete: 3,985 pages, 390 inputs and 11,652 labels, with
no unresolved references/citations or layout overflow. The scoped house
audit has zero errors and one reviewed exact-version warning. Earlier
Chapter 60 text and the reduced entropy definition onward retain their
baseline bytes. The 45 active atoms, P12.1 integration/provenance, supplied
originals, bibliography, frozen packets, verifier records and dated
releases remain unchanged. No independent-agent or production-verifier
pass is claimed.

## Chapter 60: logarithmic volume and reduced entropy slopes, 24 September 2026

The [entropy-slope audit](ch60_entropy_slope_audit_20260924.md)
reconstructs the two-sided logarithmic volume estimate with exponent
equal to the dual-complex dimension. It computes the local weighted
simplex and central multiplicities; a nodal curve model shows that the
logarithmic error can be unbounded. Reference-volume change is proved
for all probability measures, including infinite entropy. The reduced
entropy/Mabuchi slope proof now gives the fixed-model error explicitly,
justifies the directed discrepancy supremum, and proves divergence to
infinity in the infinite-entropy case. Dimension zero and the existing
total-normalization obstruction are explicit. The full mixed-slope input
and cscK existence theorem retain their cited boundaries.

Two complete local mathematical/source passes, final full compilation
and scoped page review are complete: 3,987 pages, 390 inputs and 11,654
labels, with no unresolved references/citations or layout overflow. The
scoped house audit has zero errors and two reviewed bibliography warnings.
Source outside the revised block and its BHJ source-note update retains
its baseline bytes. The 45 active atoms, P12.1 integration/provenance,
supplied originals, bibliography, frozen packets, verifier records and
dated releases are preserved. No independent-agent or production-verifier
pass is claimed.

## Chapter 60: finite-energy stability and its model interface, 24 September 2026

The [stability-interface audit](ch60_stability_interface_audit_20260924.md)
proves invariance of the Mabuchi functional under constants, with the
scalar and twisted-energy translations cancelling. The optimal coercivity
constant is reduced to normalized nonconstant data of finite entropy;
constant, infinite-entropy and zero-dimensional cases are explicit.
A projective-line blowup gives M=a-a^2 and J=a^2/2, showing both failure
of a common positive bound and failure of the converse from cscK existence.
The maximal-ray consequence records its exact d1 growth and permits the
eventual time to depend on the ray. The closing interface distinguishes
PL envelopes, normalized models and raw big classes. The cscK theorem
remains imported, now checked on the exact source PDF together with the
model-completion passages.

Two complete local proof/source passes, final full compilation and scoped
page review are complete: 3,989 pages, 390 inputs and 11,657 labels, with
no unresolved references/citations or layout overflow. The scoped house
audit has zero errors and two reviewed bibliography warnings. All earlier
Chapter 60 text, P12.1 integration/provenance, supplied originals,
bibliography, frozen packets, verifier records and dated releases retain
their previous bytes. All 45 research atoms are unchanged. No independent-
agent or production-verifier pass is claimed.

## Chapter 61: ordered quasi-distances and strong pairings, 24 September 2026

The [strong-pairing audit](ch61_strong_pairing_audit_20260924.md)
fixes the order of the two root distances and proves the exact comparison
between potential and measure quasi-distances. On normalized potentials,
MA is a strong topological embedding into its image; its surjectivity is
left to the existing variational proof. Quasi-symmetry compares J with
the dual energy of MA. A quantitative two-pair estimate proves joint
strong continuity of finite-energy integration, with one energy bound
on a tail of each convergent net. Point evaluations are uniform on sets
with bounded T. The P2 point-blowup example has the two ordered distances
a^3/3 and 2a^3/3. The imported quasi-metric theorems and mixed-gap estimate
were checked on the exact source PDF at pp. 20--22.

Two complete local proof/source passes, full compilation and scoped page
review are complete: 3,991 pages, 390 inputs and 11,664 labels, with no
unresolved reference/citation or layout overflow. The scoped house audit
has zero errors and one reviewed preprint warning. Earlier Chapter 61
arguments, the following integral-convergence and variational proofs,
Chapter 60, P12.1 integration/provenance, author originals, bibliography,
frozen packets, verifier receipts and dated releases retain their prior
bytes. All 45 research atoms are unchanged. No independent-agent or
production-verifier pass is asserted.

## Chapter 61: finite divisorial approximation, 24 September 2026

The [atomic-approximation audit](ch61_atomic_approximation_audit_20260924.md)
constructs finite divisorial measures on a fixed dual complex by integrating
the nodal functions of rational subdivisions. Convexity gives increasing
dual energy and strong convergence; affinity of discrepancy preserves
entropy exactly. A dyadic interval example checks the endpoint half-weights
and entropy 1/2. The strong evaluation estimate and support domination
give a uniform bound for normalized solutions, with a constant depending
only on the fixed complex and class. Thus fixed-complex solutions admit
uniform PL-envelope approximation. A separate diagonal choice gives
strong PL-envelope approximation with entropy convergence for every
finite-energy potential, including an infinite entropy limit.

Two complete local proof/source passes and full builds are complete.
The final PDF has 3,995 pages; 390 inputs and 11,673 labels pass the
reference/structure check. There are no unresolved references/citations
or layout overflows; physical pages 3406--3411 were visually inspected.
The scoped house audit has zero errors and one reviewed preprint warning.
Apart from one updated introductory sentence, all prior Chapter 61 bytes
are preserved. Chapter 60, P12.1 integration/provenance, author originals,
bibliography, frozen packets, verifier receipts and dated releases are
unchanged. All 45 research atoms remain active as before. This is a local
two-pass consequence audit, with no independent-agent or production-
verifier verdict claimed.

## Chapter 62: rational divisorial tests, 24 September 2026

The [rational-testing audit](ch62_rational_tests_audit_20260924.md)
proves a uniform dual-energy bound for varying masses on a fixed finite
divisorial support. It gives strong and uniform continuity of normalized
solutions, including zero weights. Rational mass vectors suffice to test
the same finite-energy coercivity inequality with exactly the same
constant. The completion proof now uses Chapter 61's simultaneous strong
and entropy approximation directly. The optimal M/J infimum is unchanged
when restricted to rational masses, with positive denominators and
infinite/empty infima handled explicitly. This does not identify the
different beta/E-dual threshold or remove the raw big-class restriction.

Two complete local proof/source passes and full builds are complete.
The final PDF has 3,995 pages; 390 inputs and 11,677 unique labels pass
the reference/structure check, with no unresolved references/citations
or layout overflows. Physical pages 3418--3421 and 3429--3430 were
visually inspected. The scoped house audit has zero errors and one
reviewed preprint warning. Following two automatic permission-review
timeouts, the final build was performed in a temporary baseline export;
the delivered source and PDF are the checked bytes. The factor-n block,
all other Chapter 62 mathematics, Chapters 60--61, P12.1 integration,
author originals, bibliography, frozen packets, verifier receipts and
dated releases are preserved. All 45 research atoms are unchanged.
No independent-agent audit or production-verifier pass is asserted.

## Chapter 62: boundary variation of divisorial masses, 24 September 2026

The [mass-variation audit](ch62_mass_variation_audit_20260924.md)
extends the finite-dimensional Legendre formula to real probability
weights and identifies all maximizing parameters, including the independent
slack at zero weights. The exact remainder is the ordered measure
quasi-distance. A fixed-complex estimate gives a uniform remainder of
order 1+r and Hölder continuity of normalized solutions with exponent
r=1/(2^n-1). It yields the inward mass derivative on every boundary face.
The projective-line example verifies the estimates and shows why arbitrary
inactive slack in an optimizer cannot compute that derivative. The class
derivative in the beta formula continues to hold the measure fixed.

Two complete local proof/source passes, full builds and scoped visual
review are complete. The final PDF has 3,997 pages; 390 inputs and 11,683
unique labels pass the reference/structure check. There are no unresolved
references/citations or layout overflows. Physical pages 3424--3430 were
visually inspected in both passes. The scoped house audit has zero errors
and one reviewed preprint warning. The final sources and ignored PDF are
the checked bytes from a temporary baseline export. The complete volume
theorem/proof, Chapter 62 outside the section, all other chapters, P12.1
integration/provenance, author originals, bibliography, frozen packets,
verifier receipts and dated releases are preserved. All 45 research atoms
are unchanged. No independent-agent or production-verifier pass is claimed.

## Chapter 62: threshold derivatives and contact masses, 24 September 2026

The [threshold-variation audit](ch62_threshold_variation_audit_20260924.md)
proves that finite-constraint envelopes contract in the uniform norm and
that their energy is concave and C1 in all real thresholds. A strict
auxiliary-vertex obstacle removes unprescribed masses by orthogonality.
The gradient is exactly the continuous vector of prescribed-point masses,
with complementary contact identities. The inverse Legendre minimum has
a unique mass vector, and the gradient maps onto the closed simplex.
The curve example distinguishes contact from positive mass and shows why
C2 regularity and strict concavity on the normalized slice can fail.

Two complete local proof/source passes, full builds and scoped visual
review are complete. The final PDF has 3,999 pages; 390 inputs and 11,687
unique labels pass the reference/structure check. There are no unresolved
references/citations or layout overflows. Physical pages 3427--3433 were
visually inspected in both passes. The scoped house audit has zero errors
and one reviewed preprint warning. Both builds used a temporary baseline
export; the delivered sources and ignored PDF are the checked bytes.
Removing only the two additions recovers the entire baseline Chapter 62.
All other chapters, P12.1 provenance, author originals, bibliography,
frozen packets, verifier receipts and dated releases are preserved.
All 45 research atoms are unchanged. No independent-agent or production-
verifier pass is claimed.

## Chapter 63: volume normalization and contact masses, 24 September 2026

The [normalization audit](ch63_normalization_audit_20260924.md) records the
fixed-class conversion between probability and mass-V energies, dual
energies and Monge--Ampere measures. Both finite-constraint Legendre
formulas are transported to the closed mass-V simplex. The threshold
gradient gives raw contact masses, and the inward mass derivative pairs
with the same normalized solution. A degree-d projective-line example
checks the volume factor, both boundary half-lines and the degree-two
mass/probability distinction. The model/ray comparison keeps f_D >= 1,
the corrected scalar coefficient and the Mabuchi slope inequality;
a constant ray separately detects the discrepancy shift.

Two complete local proof/source passes and full build rounds are complete.
The final PDF has 4,001 pages; 390 inputs and 11,695 unique labels pass
the reference/structure check. No unresolved references/citations or layout
overflows remain. The final new section, its transition and the edited
comparison-ledger entry were visually inspected. The scoped house audit
has zero errors and one reviewed exact-preprint warning. All 45 research
atoms, Chapters 60--62, P12.1 provenance, supplied originals, bibliography,
frozen packets, verifier receipts and dated releases retain their baseline
bytes. No independent-agent or production-verifier pass is claimed.
The previously pending commit 569bace was successfully pushed this round.

## Next work

1. Audit Chapter 64's common-model and finite-energy Monge--Ampere
   comparisons against the now explicit Chapter 63 volume normalization.
   Check the exact common domains, multiplicities and limiting arguments;
   a psh-cone order isomorphism alone does not identify measure operators.
   Preserve Chapters 60--63, the rational-mass and finite-constraint units,
   P12.1 provenance and exact verifier-backed passages.
2. For P07.1, separately examine continuous convex collar data and the
   production of compatible collars from stratified comparison.
   No extension beyond the current hypotheses is asserted.
3. Repeat the complete build after coherent revisions; preserve dated
   checksum ledgers for their stated snapshots. Commit and push
   checked units with outstanding limits recorded; no force pushes
   or changes to visibility.

4. In the later bibliography pass, inspect the pre-existing duplicate
   Nadel and Odaka entries on current printed page 3895. Any key
   consolidation must preserve frozen citation sources and records.
