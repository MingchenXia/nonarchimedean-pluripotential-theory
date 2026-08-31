# Chapter 24 real model maximum/locality: isolated author candidate

Date: 31 August 2026. This is not an independent or production verdict.

The editing base is the frozen Chapter 24 overlay in
`../p081_ch20_ch22_ch24_unit_weight_followup_20260831/patched/ch24_bfj_ma.tex`,
SHA-256 `391930d26a49779b10a96ac7e381fefade0677642669e7a20e93c7902e660eae`.
All its weighted and unit-weight follow-up changes remain byte-for-byte
untouched outside the five exact spans in `assembly_edits.json`.

## Original scope retained

The statements of `prop:model-maximum-principle`,
`cor:ch24-model-locality-open` (including its mixed conclusion), and
`prop:ch24-model-comparison` are retained byte-for-byte. Their inputs are
still real theta-psh model functions. The maximum is now explicitly
interpreted as a continuous theta-psh potential with the already-constructed
bounded Monge--Ampere measure; it is not asserted to be model. The original
DVR, residue-characteristic-zero BFJ, real fixed-form, ample-generic-class
scope is retained. No rationality or semipositivity restriction is added
to the given reference form. No new continuous-input theorem is stated.

## Full proof direction

1. For rational potentials, maximum closure from corrected
   `prop:ch20-model-max` permits a common SNC model for the two inputs,
   their maximum, and the fixed real form. At a strict vertex, simultaneous
   affinity forces the winning potential to dominate on every incident
   edge. The divisor coefficients consequently agree on the component and
   every neighboring component. Clearing the rational denominators gives
   zero numerical restriction of their difference. The original component
   formula gives equal masses. No claim that the strict set is literally
   a union of full stars is needed.
2. For real model inputs, new
   `lem:ch20-fixed-form-rational-approximation` supplies rational theta-psh
   approximants uniformly at the same real theta. The lemma's complete
   proof and the corrected rational-maximum proof were read. Their inputs
   are a cofinal positive representative, nef-plus-ample, openness of the
   ample cone, and finite-dimensional coefficient approximation; neither
   uses Chapter 24 locality.
3. The maxima of the approximants converge uniformly as well. Uniform psh
   stability and the already-proved `prop:ch24-continuous-uniform` give
   positivity and weak MA convergence, including for the non-model limit
   maximum. For each continuous test supported on a compact subset of the
   fixed strict set, the positive minimum gap preserves the strict order
   for all sufficiently accurate approximants. Thus the rational identity
   can be integrated against that test and passed to the limit. Radon
   uniqueness on the open locally compact Hausdorff strict set proves the
   original real-input identity. No moving-set mass convergence or
   bounded/plurifine locality is assumed.
4. Comparison uses the resulting real-input formula twice with the shifted
   real model input psi-epsilon. The maximum is merely continuous, so its
   positivity and total mass are taken from `thm:bounded-ma-extension`.
   Discarding the nonnegative contact mass and using continuity from below
   for one fixed measure along epsilon=1/m proves the original conclusion.

Chronology is acyclic relative to the stated inputs: Chapter 24's bounded
operator and uniform-continuous operator occur before this locality
section. Uniform continuity is proved from model integration by parts,
the uniform estimate, bounded monotone extension, and dense tests. It does
not use the maximum/comparison assertions being repaired. The new fixed-
form approximation input is upstream in the separate Chapter 20/21
candidate, whose gates remain independent of this dossier.

## Adjoining consistency corrections

- The introductory reduction is first to rational model potentials;
  intersection coefficients may be real since theta remains real, not
  necessarily integers.
- The open-locality corollary retains its direct mixed real-divisor proof.
  Instead of writing an honest `O(D_i-D_i')` for a real divisor, it sums the
  real numerical classes of the Cartier components disjoint from E. Each
  honest component bundle restricts trivially, so the real restriction is
  zero. No rational approximation is needed for this corollary.
- The contact-set remark now says the strict formula does not determine
  contact mass, rather than claiming nothing true can be said there. Its
  mass source is the bounded operator for a possibly non-model maximum.
- The farther unit-weight contact example was checked only to support the
  retained statement that a new atom of mass one occurs; its example
  computations and the parent's weighted changes were not edited. Its
  description of the multiplicity-two midpoint as having “degree” one
  should be read as the atomic mass b_E times component degree; the actual
  component degree there is one half. This terminology precision is
  outside the present proof spans and remains for separate review.
- The earlier general intersection-number construction's `O(D_i)` notation
  is outside the adjoining proofs. Its real-multilinearity reduction is
  not re-audited or rewritten here.

All exact source hashes and label owners are in `SOURCE_HASHES.json` and
`VALIDATION.json`. Their verification is mechanical and does not certify
the upstream theorem proofs.

## Artifact and integration boundaries

The three named replacement files contain full proofs. The two adjoining
prose changes are also displayed in `ancillary_consistency_edits.tex`.
The full copy is an exact assembly. `incremental_overlay.patch` assumes
the named Chapter 24 overlay; `combined_live.patch` includes that overlay
and these edits against the recorded live Chapter 24. These are alternative
routes, never successive patches. Neither includes or authorizes the
separate Chapter 20/21 prerequisite integration.

No live chapter or frozen parent was changed. No production call or
permission bypass was attempted. Draft compilation is syntax-only and
produces no PDF. Every new mathematical byte requires independent review
and the requested production Rethlas sol/xhigh review before live
integration. The production permission gate remains unresolved.
