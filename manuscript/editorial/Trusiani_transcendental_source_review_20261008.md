# Transcendental YTD: primary reading and proof boundaries

This cloud source checkpoint concerns Antonio Trusiani,
[*On the transcendental Yau-Tian-Donaldson Conjecture*, arXiv:2609.31089v1](https://arxiv.org/abs/2609.31089v1),
posted 25 September 2026 at 10:27:06 UTC. All sixteen physical PDF pages,
including proofs and references, were actually read with eight individually
displayed matching images and sequential notes. This is distinct from the
August projective companion arXiv:2605.30063v2, already reviewed on 6 October.
Neither the September main theorem nor a complete repaired special-Fujita
proof is admitted by this checkpoint.

The September PDF has 490,652 bytes and SHA-256
`e7e1d89236f5663dba29ed721bf82dea70182d9c5bedb82108c1efc8fe67d562`.
The full-primary actual-reading record has SHA-256
`a113b2d175ae8ee1f4f431e0467149b7a7aeb9e6d072d3a9ccef602c7d0970c9`.
Acquisition, view preparation, actual reading and subsequent diagnosis
remain separate immutable records. Earlier pending notes are retained;
the assessment below records the subsequent dependency checks.

## Category and claimed result

Theorem A concerns a smooth compact Kähler manifold with trivial identity
component of its linear automorphism group. Ordinary uniform K-stability
tests Kähler configurations; stability for models tests big configurations.
Translations of an abelian variety need not belong to the linear
automorphism group. Weighted, relative and singular extensions are future
directions in this source, not established by Theorem A.

Theorem B claims special Kähler Fujita approximation of an arbitrary big
real (1,1)-class α on a smooth compact Kähler n-fold. It requires smooth
modifications p_k, Kähler classes β_k and effective real fixed divisors E_k,
with p_k*α=β_k+[E_k], β_k^n tending to Vol(α), and
β_k^(n−1)·K_Yk tending to ⟨α^(n−1)⟩·K_X. The last trace is an extra
requirement: ordinary top-volume approximation does not imply it.
The direct canonical reduction also requires convergence against the fixed
pullback of K_X, leaving the varying relative discrepancy as the new term.

The source uses dd^c=i/(2π)∂bar∂, logarithmic singularity c log sum|f_j|²,
and multiplier integrability |f|²exp(−u). Its DF and J expressions are raw
total-space intersections, before division by the generic volume. Complex
Siu decomposition of currents is distinct from NA BJ22 Theorem 6.21.

## Actually checked dependencies

| Exact file | Actual pages in this checkpoint | Scope |
| --- | --- | --- |
| Trusiani 2609.31089v1, sixteen pages | 1–16 | Complete primary paper |
| MPWN 2509.09442v1, forty-two pages | 1–2, 6, 16–20, 31–34 | Twelve selected pages; definitions, normalized mass/intersection domain, fixed-measure L1 lemma, beginning of completion |
| Popovici, CR Math. 338 (2004), 59–64 | All six physical pages | Complete published paper; fixed-cover closed-form patching mechanism |
| Boucksom, ENS 37 (2004), 45–76 | 1, 18, 20–23 | Six selected pages; surface nef cone, negative-definite support, orthogonal decomposition and volume |

There are forty actual source/page pairs in twenty individually displayed
images, two complete files and two partial selections. MPWN's main proof
and Boucksom's entire analytic antecedents are not newly read in full.
Popovici part (ii), with a nonclosed C1 lower bound, refers further details
to a thesis and is outside the present application.

Tosatti arXiv:2608.30153v2 is reused from the preceding complete fourteen-page
actual reading, pinned by PDF SHA-256
`a40feb12fb2b0219a0857f4f9b81e2f6acea43c08ef7e461d00a9d4020d03fe0`
and the Dinh–Nguyen–Nguyen review manifest SHA-256
`b79717a3b4a81117ea47ae68c75915937255b8d730eceb2aa91eb9cad1f142c1`.
Corollary 1.3 identifies numerical restricted volume along a prime divisor
with the fixed positive-product trace and its non-Kähler-locus vanishing.
This reuses existing actual evidence, adds no fresh-page credit and retains
the preceding audit's external-proof qualifications. Its general Kähler
Morse result is separate from the normalized test-configuration argument.

## Normalization obstruction

Trusiani's page-13 proof treats adding cX_0 as preserving raw DF and J
for an arbitrary absolutely big class, then assumes D≥X_0. MPWN's
Definition 1.1.1 permits arbitrary vertical real D with an absolutely big
class. Its mass formulas and Theorem 9.1.1 instead require f_D≥1,
equivalently D≥X_0. Proposition 9.1.2 inherits that domain through
Proposition 4.2.1. Translation of a PL envelope preserves its intrinsic
NA M and J; it does not establish the unnormalized raw correspondence.

The book already records this obstruction in
`ex:mpwn-big-translation-failure` and distinguishes the normalized model
inequality from the literal all-big-model inequality. No duplicate example
is needed to explain the September proof's boundary.

The additional direct diagnostic takes the blowup of C_g×P¹ at (x,0),
with H the horizontal point-section class, F the fiber and E exceptional.
The reduced zero fiber is (F−E)+E. Set L=H+F−E and consider

* α_before=H+(3/2)F−2E, with P_before=L/2 and
  N_before=(F−E)+(H−E)/2;
* α_after=α_before+(3/2)F, with P_after=L+F and N_after=F−E.

The two negative curves are disjoint with square −1. For any other strict
transform of a curve, its multiplicity at the point is bounded by its
intersection with each selected horizontal section and fiber. This proves
L nef; L²=1 and F is nef. Both decompositions have effective orthogonal
negative parts and satisfy the standard surface Zariski characterization.
Their moving volumes are 1/4 and 3, and H traces are 1/2 and 2.

For the genus-two fixture K_relative=2H+E and generic V=1. The raw
values are DF_before=5/4, J_before=3/8, DF_after=2, J_after=1/2.
The changed vertical divisor is 3(F−E)+E≥X_0. A genus-two curve has
trivial automorphism identity component, so this proof-step obstruction
also occurs in the automorphism domain of Theorem A. Four exact rational
fixtures, for genera zero through three, preserve the original diagnostic
record and verify the printed raw formula. This refutes the stated shift
argument; it does not refute the cscK equivalence or prove either direction
of the all-big/normalized stability equivalence false.

## Uniform regularization and fixed ideal errors

Popovici's published Lemma 1.2 is on printed page 62, with proof on 63.
After local potentials of a smooth closed lower-bound form are subtracted,
the two-chart Bergman comparison has constants determined by fixed cover
geometry, rather than by the size of the psh weight or class coefficients.
The weighted bar∂ correction vanishes at the evaluation point because of
its logarithmic pole; cutoff and quadratic estimates bound its norm.
Collar separation then bounds the cost of patching.

This supplies the relevant weight-independent mechanism for Trusiani
Lemma 4.3. An explicit adaptation should use holomorphic transition
multiplication on the overlap and the target chart's global psh weight;
it need not assume extension of a transition function to the union of
charts. Fixed Jacobian bounds, weight/operator conversion and the usual
local multiplier-ideal finite-generation input remain explicit. Merely
quoting the abstract's constant independent of m would be insufficient.

The September fixed-error construction uses this regularization twice
and absorbs its fixed curvature cost with k_0ψ. Writing O(−k_0E) requires
an integral effective E, arranged by resolving the initial analytic ideal
and rescaling its coefficient first. Multiplication by an invertible
Cartier ideal preserves integral closedness. The volume squeeze keeps
(k/(k+k_0))^n and both positive summands. These checks do not establish
the varying discrepancy estimate.

## Remaining proof inputs and local slips

Proposition 4.1 imports the analytic normalized-blowup discrepancy bound
from Proposition 3.1 of the August companion. The earlier complete
25-page reading retained a qualification on its analytic normal-direction
argument. Citing it again does not clear that qualification.

The normal intermediate blowup Z_k need not be Q-Gorenstein. Ordinary
q_k* K_Zk/X and K_Yk/Zk therefore need an additional definition or
hypothesis. A possible alternative pairs the bounded residual current
with the pushed-forward canonical Weil cycle, but its bounded-potential
cycle projection formula and coefficient bound must actually be proved.
This is an identified route, not a certified repaired theorem.

Lemma 3.5 imports prescribed-singularity solvability and singularity-metric
mixed-mass continuity from three DDL papers. Those exact proof chains
have not been freshly read for this checkpoint. A signed smooth canonical
form must be written as a difference of positive forms before applying
a positive-current convergence statement. An unrestricted assertion that
top-volume convergence gives strong NA convergence is not supplied by
MPWN Lemma 5.0.5: that lemma requires weak NA convergence and bounded J
and tests a fixed finite-energy MA measure. Trace/pairing identification
and the admissible approximation hypotheses must precede its use.

Theorem A additionally needs C*-equivariant regularization and resolution,
zero-fiber support and preservation of the generic polarization. None is
licensed by the invalid normalization step. These are retained inputs to
the conditional passage from ordinary tests to normalized model tests.

Local slips have their own scope: the introduction's prime fixed divisor
must be an effective divisor; the scalar-curvature numerator needs ω^(n−1);
two S_k integrals need the appropriate n−1 power; the test-configuration
complement needs X×(P¹ minus zero); and equation (4.3)'s canonical base
index should be X. In MPWN the regularization Lelong error approaches
from above, not below, the maximum identity in Lemma 5.0.5 has a minus
sign, and the fixed-divisor ordering in Proposition 9.1.5 needs consistent
signs. The associated source notes give the precise corrections. These
slips are not represented as counterexamples to the limiting conclusions.

## Admission and preservation

The permissible book addition explains the canonical-trace requirement,
the conditional passage on already normalized configurations and the
version-specific normalization obstruction. The full September YTD or
special-Kähler-Fujita claim is excluded from certified book results.
Weighted/relative/singular extensions remain source-announced directions.

There is no new original general theorem, independent gpt-6.1-sol xhigh
receipt, canonical status change or new whole-book reading. The forty-two
atoms in twelve formal problems are preserved. General BJ22 critical
homogeneous Siu division/envelopes remain OPEN; LPWZ density remains
UNVERIFIED. The active 4,626-page book, all active TeX inputs, both
bibliographies and the native catalogue are protected at this source
checkpoint. Preparation and export provide no actual-reading credit.

Read-only GitHub checks on 8 October at 16:31 UTC found work at
`807e300e2421f71fbe9d7bdcd8829b70a4526ed2` and main at
`00957114db21b627e97369563032ceda9cea09c7`, unchanged. Evidence exports
and local checkpoints continue under the user's authorization. The earlier
automatic-review ownership requirement for the full upload remains pending;
this checkpoint neither retries nor bypasses that rejected action.
