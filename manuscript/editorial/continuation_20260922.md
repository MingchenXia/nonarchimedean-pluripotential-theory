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

## Next work

1. Audit Chapter 53--54 perturbation arguments: order reflection
   and the uniform positive-mass bound from a smaller Kähler
   perturbation before forming a decreasing inverse-system limit.
   Match the operations-paper citations to the checked version;
   the author reports an earlier version in the published volume.
   The projected-operations correction now has a separate
   23 September receipt. Keep the normalized model
   condition separate from the literal raw all-big-model condition;
   examine any proposed comparison before restoring a converse.
   General Kähler maximal-ray existence, sequential regularization
   and the full mixed-slope reduction remain explicit source inputs.
2. For P07.1, separately examine continuous convex collar data and the
   production of compatible collars from stratified comparison.
   No extension beyond the current hypotheses is asserted.
3. Repeat the complete build after coherent revisions; preserve dated
   checksum ledgers for their stated snapshots. Commit and push
   checked units with outstanding limits recorded; no force pushes
   or changes to visibility.
