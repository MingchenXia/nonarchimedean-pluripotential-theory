# Exact-revision review: Chapter 20/21 real-model maximum repair

Date: 2026-08-31. Reviewer: /root/p082_independent_reaudit.
Author of the reviewed packet: /root.

## Verdict and provenance

PASS for the substantive maximum/density/envelope repair at the exact
original bytes listed below, with three nonblocking wording/source notes
in Section 5. This is not a certification of both entire chapters or a
production acceptance. The explicit gate exclusions remain in force.

The reviewer independently diagnosed the original real-model maximum and
directedness defects, checked the elementary counterexample, and supplied
the fixed-form rational approximation and downward-shift repair
ingredients. Consequently this is an exact-revision mathematical and
assembly review of root's text, not a completely fresh independent review
of the reviewer's own diagnostic reasoning. A further independent review
is required. No novelty, priority, open-problem retirement, or general
envelope result is claimed.

## 1. Exact targets and assembly

Worktree: /private/tmp/nappt_p071_20260827.

Packet: manuscript/editorial/solver_dossiers_20260831/
p081_ch20_ch21_real_model_max_repair_20260831.

| Role | SHA256 |
| --- | --- |
| Original patched/ch20_model_forms.tex | 7b287229f071aceeaa8396a8ea00bd6f6d70a566f67bdd452fc72bd2281fb586 |
| Original patched/ch21_bfj_psh.tex | 957e2a2d16ff85c036aa42c1647aa055f56767fb9973a02b34d4853899d39310 |
| MANIFEST.json | c93d77d0cef6bec9b16ffe9ff3f499cae581237553f72872b87ee7f2bbc4421e |
| Weighted Ch20 parent | bc479b67a29261f001d0409656e150bc3bf9441dbdf1ff90fb4298fe3c1ad414 |
| Live Ch21 parent | 477db8e896633bcf5f89c8738e16e0afa8eaac55f36042c1d263b683daed72b3 |

The Ch20 parent is the separate
p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/
ch20_model_forms.tex, not the live unweighted chapter. I read the complete
Ch20 difference against this actual parent and the complete Ch21
difference against its live parent. The larger recorded ch20.patch is a
comparison against the live chapter and therefore also contains inherited
weighted corrections. Those inherited changes are not new claims of this
repair and are not independently recertified here.

The read-only check_exact_assembly.mjs validates all seven file entries and
both chapter entries of the author's manifest. It replays only the
fully inspected in-memory transformation prefix, with a read-only file
interface, excluding the entire directory/write/diff output phase.
All 22 recorded operations and both resulting chapter byte strings match
exactly. All three proof fragments occur exactly once in assembled Ch20.
The original comparison patches also equal fresh read-only diffs.

Ch20 preserves all 209 parent labels and adds exactly these three:

- lem:ch20-fixed-form-rational-approximation;
- cor:ch20-real-max-uniform-approximation;
- ex:ch20-real-max-irrational-breakpoint.

Ch21 preserves all 172 labels and adds none. Thus the assembled total is
384 labels, without duplicates within either chapter. Neither chapter has
a control byte or an unmatched begin/end environment in the static scan.
This is not a LaTeX compilation or PDF visual-QA claim.

## 2. Rational maximum and fixed-form approximation

### 2.1 Rational maximum

The revised prop:ch20-model-max states two different facts correctly:
real theta-psh model functions are real-convex, while rational theta-psh
model functions are rational-convex and finite-max stable. Theta remains
an arbitrary real closed model form. There is no ample-generic-class
hypothesis on this proposition.

The proof represents theta numerically in an ample line-bundle basis on
one common model. Rounding the reference coefficients upward by positive
amounts yields a rational ample perturbation of each nef class theta+D_i.
The denominator m clears both input divisors and the rational perturbed
reference; the two large line-bundle multiples are globally generated.
The sum of their vertical fractional ideals computes m times the maximum.
The twisted sum ideal is globally generated, so its blowup metric is nef.

Importantly, rational model membership of the maximum is established
before taking a limit: fix any denominator m0 clearing D1,D2 and blow up
O(m0 D1)+O(m0 D2), normalizing if needed. This model determines the same
maximum independently of the perturbations. Nefness of each perturbed
form reflects to that fixed model. Closedness is now applied in one
finite-dimensional numerical space, not to an unknown limit function.
This matches the actual rational convention in BFJ Proposition 5.8.

No step requires theta itself to be rational, semipositive, or ample on
the generic fibre. Projectivity supplies the auxiliary ample basis. The
proof does not infer a real-model maximum from rational maxima.

### 2.2 Fixed real theta, ample generic class

The new density lemma has exactly the additional hypothesis it needs:
the generic numerical class of theta is ample. Its proof chooses a final
common model determining theta and D and admitting a fresh correcting
vertical real Cartier divisor P with theta+[P] relatively ample.
The cofinal positive-representative input is sufficient; one must not
instead pull back a previously ample representative and presume it is
still ample. The referenced Ch20 proposition and the directly checked
BFJ Proposition 5.2/Corollary 1.5 supply the required cofinal statement.

The interpolation D_delta=(1-delta)D+delta P has ample curvature because
theta+[D] is nef and theta+[P] is ample. Small delta controls the global
uniform error by linearity and compactness. D and P belong to the span
of finitely many integral vertical Cartier divisors on that same model.
Rational coefficient approximation inside the open ample cone retains
positivity at the exact same theta. The displayed weighted sum of the
sup norms of their model functions bounds the second approximation error.
Both epsilon/2 budgets are correct. This gives a sequence, if desired,
by taking epsilon=1/n; it assumes no metrizability of X analytification.

Only divisor coefficients are rounded. No positivity descent for arbitrary
real reference forms, no envelope theorem, and no global regularization
are used. The finite-real-maximum uniform-approximation corollary follows
from this lemma, rational maximum stability, and the max Lipschitz bound.
It makes no model-membership claim for the limit.

## 3. Counterexample, truncation, and envelope scope

The blowup of P1 over C[[pi]] at a rational special-fibre point is a
regular projective flat SNC model with two multiplicity-one components
C,E, intersection one, and self-intersections minus one. For
L=rho*O(2)(-E), its degrees are (1,1); L+E has degrees (2,0).
Thus both 0 and g-a, where g=phi_E and a is irrational in (0,1), are
real theta-nef models. The special-fibre divisor supplies the real
constant, with zero curvature. On the unit edge g(s)=s.

Rational model functions have finitely many rational edge cuts, as
asserted by prop:skeleton-model-pa. This interface was additionally
checked by the monomial/ideal proof recorded in the earlier diagnostic
audit: at the node pi=zu, valuations of local series are finite minima of
integer-affine functions of s; a finite set of minimal monomial exponents
suffices. BFJ Proposition 2.2 reduces arbitrary higher-model functions to
differences of such ideal logarithms. Rational cuts therefore apply to
all higher models. A finite real linear combination does not introduce
new cut coordinates. The kink of max(0,s-a) proves nonmembership in D_R.
Only the first assertion of BFJ Corollary 3.13 is needed, not its stronger
printed converse. Bare piecewise affineness alone would not suffice.

The same continuous bounded h is a valid obstacle: any admissible real
model upper bound of 0 and g-a below h would equal h. This correctly
disproves directedness of the full real family, including in an ample
generic class. It does not disprove psh maximum stability.

The truncation corollary now keeps the distinctions: real constants are
real models under semipositive theta; rational function/rational constant
truncation stays rational and nef; with ample generic class, real
truncations are uniformly rational-model approximable, not necessarily
models. Its proof imports precisely these hypotheses.

The model envelope remains defined over D_R. Its theorem still assumes
only semipositive theta and bounded real obstacles for the ordinary
bounds, order, translation, Lipschitz, idempotence, real concavity and
reference-change items. Their unchanged proofs use set inclusion, linear
curvature, or real translation, not real maximum closure.

The rational minorant subfamily is nonempty under semipositivity because
it contains a sufficiently small rational constant, and it is directed
by rational maxima. Equality of its supremum with the real-model
envelope is asserted only under ample generic class. Given a real
minorant psi, choose rational q within epsilon and rational
epsilon<c<2epsilon. Then psi-3epsilon<q-c<=psi<=obstacle, exactly as
displayed. Taking pointwise suprema and epsilon tending to zero proves
equality, and the rational family ordered by pointwise comparison gives
the increasing net. No continuity of the obstacle is assumed or needed.

The convex-chord sign is now correct: a maximum of affine functions lies
below the affine interpolant of its vertex values. The vertexwise curve
lattice and fixed-model vertex-constrained envelope are retained as
different operations; the repair does not equate them with pointwise
maximum of affine interpolants or a global envelope theorem.

## 4. Chapter 21 interfaces

The inherited standing hypotheses require smooth connected projective X
over a complete discretely valued field with residue characteristic zero
and real closed reference forms of ample generic class. No algebraic
closedness of the valued field is introduced.

In the skeletal-properties proof, rational approximants satisfy convexity
and the retraction inequality by the relative ideal argument. The new
real-case paragraph invokes fixed-form density, retaining theta, and
passes the inequalities by global uniform convergence. This is valid on
each theta-determining SNC skeleton. Equality when the model is already
determined is still the separate model-function factorization statement.

In the PSH maximum proof the definition first supplies real theta1-nef
approximants on a fixed skeleton. Replacing each by a rational theta1-nef
model with global error less than 1/k leaves the skeletal limits
unchanged. Rational maxima then approximate the desired maximum. Upper
semicontinuity, nontriviality and the retraction inequality are checked
separately. This proves the maximum clause without rationalizing theta1
or changing the PSH class. The sequence index is legitimate because the
required approximation is a uniform norm closure on a fixed skeleton.

Real linear combinations remain allowed in the separate convexity proof.
The revised orientation and composition remark describe these coefficient
distinctions accurately. The core conclusion agrees with BFJ Proposition
7.4 through Definitions 2.1, 5.5 and 7.1.

## 5. Original-revision precision notes

These do not invalidate the core repaired conclusions, but belong in the
revision ledger rather than being hidden by a blanket PASS.

1. In the modified example around original patched Ch20 lines 2345--2351,
   inherited wording says the obstruction always occurs and that a maximum
   of two affine functions is not affine. This requires genuine crossing:
   identical functions or a dominating affine function give an affine
   maximum. The corrected chord inequality itself is valid.
2. The inherited Ch21 relative-ideal approximation citation is BFJ Lemma
   5.3, whereas the exact inspected arXiv version has this as Lemma 5.7.
   The stated interface and argument are the latter's.
3. The inherited proof of lem:ch20-special-fibre-test ends by denying that
   it asserts openness inside the numerical subspace, although the lemma's
   statement calls the ample cone open and the new proof correctly uses
   this standard openness. The denial is stale, not a failure of the
   mathematical openness input; BFJ Proposition 5.8 explicitly uses it.

Root has announced a separately frozen revised1 addressing these notes;
that revision is not silently substituted into this original-byte report.
It receives its own addendum and hash check.

## 6. Limits and preservation

The full GATE.md was read. This review does not repair or certify the
distinct Ch21 curve/cofinal-semistable retraction issue, all Ch24
model-locality consumers, Ch26 bounded-energy preparation, or the final
Ch30 descent argument. It does not recertify inherited weighted-curve
work or every unrelated assertion of either full chapter.

No reviewed packet, parent, source, or live manuscript file was edited.
Only this sibling review directory was written, with apply_patch.
No assembly writing phase, production call, acceptance claim, or live
integration occurred. No standalone or book PDF was compiled here.
