# Independent audit of the frozen Ch23 consumer repair

31 August 2026. Reviewer: `/root/p081_weighted_repair_fresh`. Author of the reviewed Ch23 candidate: parent/root. This review is independent of the Ch23 authorship; it is **not** an independent audit of this reviewer's own Ch29/Ch31 revised2 work.

## Verdict and boundary

The fixed-skeleton approximation repair is mathematically sound relative to the stated Ch21 inputs. The new real-model chord mechanism also has the correct proof direction: numerical positivity upstairs, same-field graph retraction, chording, real numerical nef reflection, and finally fixed-skeleton BFJ approximation. I found no counterexample or core obstruction to that intended theorem.

The frozen full-copy bytes should nevertheless be corrected before exact acceptance: the nonregular-model invocation of the SNC-only BFJ definition needs the explicit subdivision transfer in R1; the inherited numerical example needs rational blowup centres in R2; and its contact/harmonicity wording needs R3. These are bounded corrections, not permission to enlarge the theorem or identify rational-model and unrestricted envelopes.

No live file, frozen candidate, source packet, or production record was modified by this audit. This report and its read-only byte checker are new sibling artifacts. No production Rethlas submission was made. The independent and production gates remain in force.

## Exact reviewed bytes

Candidate directory:

`/private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p081_ch23_curve_consumer_repair_20260831/`

| File in that directory | SHA-256 |
|---|---|
| MANIFEST.json | d174891d4af1c3dc947f8bdfabfc5dbd9dcbb668f70a2b7f15989adc1607cc4a |
| fixed_skeleton_approximation.tex | 4ea4feda1865279cc5af256abaf781f630f4f2f5f0745271a028505cc95dc6a6 |
| curve_chord_bridge.tex | a616bd67ff4728fec041dba98e345e91eda95b01299c42a1c464522c15630c46 |
| numerical_example_end.tex | 335223c8e5ed110b31d44398d18d9c0ac3a91f5a5a60f526817d4aae71256525 |
| model_dependence_end.tex | 880780eebaa8b6a34bffd2b688fe343ec996079d4bf2b2efbfbec8a6e8e1ad74 |
| patched/ch23_bfj_envelopes.tex | a3e00bb50daa668f107a8847e55408e69c554a88ddc7b6f8dfdf63f785599fca |
| chapter.patch | 0808cb031343deda099dca51da06fad569b72472a129cdb375480c9b96a9c85a |

All four fragments were read in full, together with their enclosing statements, the numerical calculation, the fixed-model polyhedron proof, and the relevant standing hypotheses. The assembly script was inspected but not run: it writes frozen outputs. The independent `verify_sources.mjs` only reads and checks bytes.

## R1 — explicitly transfer the SNC hypotheses to a nonregular semistable model

Locations: `curve_chord_bridge.tex` lines 6–11, 79–105. Compare live Ch21 `def:ch21-bfj-psh` and `lem:ch21-model-skeletal-properties`, whose quantifiers are explicitly over SNC models.

The new lemma permits the nonregular local equation xy=π^a with a>1. Such a model is not itself an SNC determination in the sense used by those Ch21 inputs. Therefore “by its defining approximation on the fixed skeleton” and “the BFJ retraction inequality” need a connecting sentence. The current reference to regular subdivision at lines 89–90 only explains the interpolated Cartier divisor and does not explicitly transfer these two BFJ properties.

Suggested insertion before the BFJ approximation passage: resolve the nodal singularities over the original discretely valued field. Locally the regular resolution of xy=π^a subdivides the annular segment into a unit-length segments; the same construction is checked on the étale node charts. It does not attach new branches or change the underlying analytic skeleton or its retraction. The resulting regular semistable model is an SNC determination of θ. Apply the Ch21 approximation and retraction assertions there and view them on the unchanged Γ.

This also explicitly proves that all original vertex values of φ are finite. Do not require the model approximants to be determined on this regular subdivision: only their restrictions to its fixed skeleton are used.

This is a missing hypothesis-transfer explanation, not a failure of the local Q-Cartier calculation. In the normal node ring, the branch prime (x,π) has ord(x)=a because y is a unit at its generic point, while x has order zero at the other branch. Hence div(x)=a times that branch; the analogous statement holds for y. Cartierness is étale local, so this verifies Q-Cartierness also at a nonrational node. Since the special fibre is reduced and v(π)=1, a vertical real divisor with given component coefficients has those vertex values, with edge-affine interpolation.

## R2 — the unit-weight numerical example must choose rational centres

Location: full proposed Ch23 lines 2859–2876, in the unchanged opening of `ex:ch23-curve-envelope-numbers`.

“Each at a smooth point of the special fibre” is insufficient for the asserted intersection numbers and edge weights equal to one. A smooth closed point may have residue degree r>1. Blowing it up produces an exceptional projective line over its residue field, and the new node has conductance r. The component intersection degrees over the base residue field then contain that factor.

For a concrete test, take residue field ℝ and the closed point t²+1=0 on the original projective line. Its residue field is ℂ and its degree is two. The first new edge has weight two, not one. Degrees over ℝ on the exceptional component are twice their degrees over ℂ, so the subsequent assertion that arbitrary integer residual-degree vectors are obtained by the displayed unit moves also fails without the split choice.

Required edit: choose each blowup centre to be a smooth **base-residue-field-rational** point away from the preceding nodes. Such points are available on the projective-line components in the standing residue-characteristic-zero regime. This is a specification of the freely chosen numerical example, not a restriction of the chord theorem. With that edit, the displayed five-vertex constraints and the vector (-1,-2,-3,-2,-1) check directly.

The issue predates the new tail, but it is part of the full proposed copy on which the new global-envelope argument relies.

## R3 — distinguish skeletal contact and reference-adjusted harmonicity

Location: full proposed Ch23 lines 2951–2964.

The skeletal contact set is {e₂}. Since both u and the computed P are extended through the retraction, their global contact set is p_X^{-1}({e₂}), not the single divisorial point. The curvature measure is nevertheless 2δ_{e₂}, so the orthogonality calculation is unchanged.

Likewise P itself has graph Laplacian −δ_{e₀}+2δ_{e₂}−δ_{e₄}; it is not harmonic at the noncontact endpoints e₀,e₄. What vanishes off the contact set is the **reference-adjusted curvature** θ+dd^c P. The edge-affineness statements are correct.

Suggested wording: call {e₂} the “skeletal contact set,” give the global preimage if discussing all of X^an, and replace “P is harmonic off the contact set” by “the reference-adjusted curvature vanishes off the contact set.” No numerical value or envelope theorem changes.

## Checks of the new proof mechanisms

### Fixed-skeleton approximation

The model Z chosen to approximate the continuous obstacle remains fixed. Clause (2) of the BFJ definition approximates ψ on precisely Δ_Z, while the model retraction inequality gives χ≤χ∘p_Z even if χ is determined elsewhere. Thus χ<f+2ε globally, and χ−2ε is an allowed real-model competitor. At the chosen quasimonomial point the final loss is 4ε. The use of real constants is legitimate in the chapter's real vertical-divisor convention; no rational-model conclusion is smuggled into this argument.

### Refinement and chording

Thuillier Proposition 2.2.26(iv) is stated for a pullback from the smaller skeleton, not an arbitrary function on the refined skeleton. The candidate correctly supplies the extra argument it needs: subtract the pulled-back restriction; the difference vanishes on the old graph; each attached finite piece has total Laplacian mass zero including its attaching point. Its entire pushforward is therefore zero. This proves the required identity for nonfactoring χ without presuming factorization.

The nonnegative restricted curvature gives convexity on every old open edge. If a convex piecewise affine function on [0,ℓ] is replaced by its endpoint chord of slope s, then s is at least its right derivative at 0 and at most its left derivative at ℓ. Both outgoing endpoint slopes consequently increase; all new interior curvature is zero. Summing these weighted endpoint inequalities gives nefness of the chord.

This remains valid for a real model function: the equality between the numerical component degree and the curvature coefficient is extended real-linearly, then nefness tests the individual degrees. No rational approximation preserving an irrational boundary class is presumed.

### Scalar extension and disconnected geometric fibre

The candidate only moves model data, not an arbitrary singular BFJ function, to the completed algebraic closure. The computation is componentwise if the curve splits. Chording commutes with the edgewise affine scalar maps, while nefness is tested and reflected on each vertical component by degree/projection formulas. There is no need for a global harmonic-uniqueness or connected-graph argument here, so geometric connectedness is not being silently added.

### Passage to the full BFJ class and the two consumers

After the R1 transfer, uniform approximation on the fixed Γ implies convergence of the finite original vertex vectors. The affine numerical inequalities are closed, so the real chord Aφ is nef. The BFJ retraction inequality and edge convexity give φ≤Aφ globally. An edge-affine model obstacle bounds the chord whenever it bounds φ.

Consequently the new numerical tail compares every BFJ competitor to the computed finite-dimensional maximum, not merely every rational model competitor. The fixed-model stabilization remark has a nonempty set by the already established ample-class competitor existence; its finite-coordinate supremum proof only uses closed affine inequalities, coordinatewise maximum stability, and the obstacle's finite upper bounds. It does not need the background form itself to be nef.

The statements remain confined to the standing BFJ field regime and real model functions. Neither consumer identifies that envelope with the arbitrary-field rational-model envelope of Ch29.

## Read source interfaces and frozen prerequisite bytes

- Live Ch21 `ch21_bfj_psh.tex`: SHA-256 `477db8e896633bcf5f89c8738e16e0afa8eaac55f36042c1d263b683daed72b3`. Read the standing hypotheses, the two-clause BFJ definition, its fixed-skeleton quantifier explanation, model skeletal-properties lemma/proof, and the model-consistency interface. These remain accepted chapter inputs; this bounded audit does not re-certify the entire multiplier-ideal package.
- Live Ch20 `ch20_model_forms.tex`: SHA-256 `531024045204686aaf0fc12ff0e825bf67367551cd310a26c956740b4d164baa`. Read the model-function sign, real vertical-divisor convention, and degree/projection pullback identity.
- Thuillier text `/private/tmp/thuillier2005.txt`: SHA-256 `9612f1cd9b4478e4bfafd9a5a7490dd670854043b0df65ce67cd84c73be204cf`. Read Proposition 2.2.21 and its scalar weighted-affine proof, and Proposition 2.2.26 with proof (printed pp. 42–43 and 47–48). In particular the narrower pullback hypothesis of item (iv) was checked.
- Published GJKM text `.../p081_degree_zero_tate_obstruction_audit_20260831/sources/GJKM_published_2019.txt`: SHA-256 `942bef601044149054cb615612f8709358e22bd59d56bfe10be124dac94a689e`. Read §§3.5–3.8, including the original-field weighted model criterion, its completed-algebraic-closure reduction, and its explicit BL85 §7 domination citation (published pp. 2344–2346). BL85 §7 is used through that precise imported interface; its entire original proof was not independently re-audited here. No use of GJKM Theorem 3.1 or Proposition 3.10 is made.
- Ch29 revised2 fragment: SHA-256 `3760582c91ed79994f0d6817adfecd08a80eb720ff12c27b39b11966893b1d0c`. The numerical nef-reflection paragraph was read as the cross-reference target. Its degree argument does not use geometric connectedness. This is not an independent endorsement of the rest of that reviewer-authored fragment.

## Mechanical results, not mathematical certification

The read-only checker confirmed all ten original candidate manifest entries, with zero size/hash mismatches. It reconstructed the four-fragment assembly in memory and obtained the exact full-copy bytes. All 178 original Ch23 labels are retained, with one new label and no duplicates. The live Ch23 bytes still match the recorded base, and `git apply --check` passed without applying the patch.

This audit performed no compile and produced no PDF. The candidate needs a new frozen revision and exact-byte review after R1–R3, followed by the unchanged production and full-manuscript integration gates. No general-envelope or open-problem retirement claim follows.
