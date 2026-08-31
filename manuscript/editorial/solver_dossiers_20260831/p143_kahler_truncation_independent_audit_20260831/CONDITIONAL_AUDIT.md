# Exact-byte conditional mathematical audit: P14.3 Kähler truncation

Date: 31 August 2026. Reviewer: /root/p081_weighted_repair_fresh.

## Verdict and independence disclosure

CONDITIONAL PASS: no substantive mathematical gap was found in the exact statement and proof identified below, assuming A1 (raw-transform upper semicontinuity), A2 (dominated rational-divisorial density), and the explicitly stipulated existing finite-energy DXZ–MP correspondence and primary-source interfaces.

This is an audit of root's separate truncation/completion argument. I did not author that argument. I did author the separate candidate proposed to establish A2, and previously wrote its finite-energy consequence. Accordingly, this report assumes A2; it does not independently certify A2, its proof, or its production status. A1 is likewise an assumed candidate input here. My preliminary review of the present packet suggested expanding the already cited sup–mean bridge; the frozen mathematical core was not changed.

The conclusion assessed is the full DXZ–MP order isomorphism in a Kähler class on a connected compact Kähler manifold, including equality with the literal raw function at all semivaluations and equality of extended energies. It is not an arbitrary pseudoeffective MP-cone theorem.

## Exact target and byte checks

Author packet:
 /private/tmp/nappt_p071_20260827/manuscript/editorial/solver_dossiers_20260831/p143_kahler_truncation_research_20260831/

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| statement.tex | 3053 | befc29fb89ff79fe90172d03b1fe088e5f19ebf2ca28aedbd4c83cd05f008100 |
| proof.tex | 9542 | 1ef28983e1ac242f9a23080e24ced0c21531899f56ab29a96312f4ce79757652 |
| MANIFEST.json | 4822 | f5e70b72c09601f27d2210391d8f72935bc37564481be9a5818c19f8926c0b8b |

All 16 manifest entries and all eight parent inputs were independently read and checked for exact size and SHA-256: zero mismatches. The statement and proof were read in full after freeze. The source/dependency/build ledgers were inspected. Nine labels are unique and all 12 internal references resolve. These mechanical checks are recorded in CHECKS.json; the read-only checker is check_exact_packet.mjs.

No author build script was executed during this audit. The saved final log has no undefined citation/reference, LaTeX/package warning, error, or overfull box. It does have one underfull hbox, badness 10000, at the paragraph reported as lines 15–18. The author's warning filter does not count underfull boxes. This is nonblocking draft-layout output, not a mathematical defect. No PDF was produced or visually inspected.

## Mathematical review

### 1. All-point comparison is genuinely conditional on A1 and A2

The ideal order gives the correctly directed inequality F(v) ≤ F(q) when q ≤ v. A2 supplies a net of such q converging to v, not merely an arbitrary dense approximating net. Divisorial agreement and upper semicontinuity of the existing MP function then give F(v) ≤ φ(v). This remains valid when either value is −∞: every finite upper threshold for the approximating values eventually bounds F(v).

The opposite inequality uses MP Theorem 4.3.8 with the psh function on the left and the A1-usc raw transform on the right. No positivity of F is assumed in this step. In particular there is no dense-set equality shortcut and no circular use of the eventual full comparison.

### 2. The decreasing-completion lemma is valid without minimum closure

For two candidate dominants h₁,h₂ with positive margins above possibly different rows, choose a later row fⱼ and a rational δ smaller than one quarter of both margins. The function g=min(h₁,h₂) is continuous, and fⱼ+4δ<g everywhere. This remains strict where fⱼ=−∞.

The open sets {hⱼ,λ+2δ<g} form an increasing cover. Compactness gives a finite subcover, and directedness of the row net gives one index covering all points. Thus hⱼ,λ+δ is a member of the proposed dominant set and lies below both h₁,h₂. This proves downward directedness using only rational translation in the model class.

The pointwise threshold argument proves that the infimum of this directed family is exactly infⱼ fⱼ, including at −∞ points. There is no countable diagonal, no unproved sequence extraction, and no assertion that g is model psh. Excluding the identically −∞ limit is exactly the condition needed in the MP definition.

### 3. The DXZ truncation is proved finite-energy in its actual source category

The key argument concerns actual perturbation components, not only divisorial values. In a Kähler perturbation class, the constant object of value −j has level 0 for τ<−j. Order dominance and the normalization of every genuine model level force the same equality for Γ∨(−j). Its −∞ level is therefore exactly 0.

The component masses are consequently explicit ordinary Kähler volumes. Their decreasing perturbation limit is V>0. Positive-volume recovery is invoked only after establishing that positivity. Its levelwise recovery formula preserves the zero lower-end levels, so the unperturbed curve is constant at zero below −j.

For the recovered curve the integrand in the normalized DXZ energy lies in [−V,0], and its support in the parameter direction is contained in [−j,cⱼ]. Hence the displayed estimate −j≤I(Γⱼ)≤cⱼ is correct. The degenerate case cⱼ=−j is harmless. No uniform lower energy bound as j grows is required or claimed. In particular, an arbitrary zero-volume inverse-system object has not been silently identified with an unperturbed curve.

### 4. Endpoint normalization: source bridge made explicit

There is a compressed source bridge in the frozen text, but it is not a substantive gap requiring a new mathematical version. The statement of MP Lemma 5.3.1 is an integral-slope assertion. Its proof relates that integral slope to the supremum slope using the uniform normalized sup–mean bound.

Here is the complete bridge in the packet's conventions. A nontrivial normalized I-model level γτ has supremum zero. Indeed, if its supremum were M<0, then γτ−M would be a larger admissible competitor with the same multiplier ideals, contradicting its envelope fixed-point property. Thus
\[
 \sup_X U_t
 =\sup_{\tau<c}\bigl(\sup_X\gamma_\tau+t\tau\bigr)=tc.
\]
The literal inverse Legendre supremum is legitimate; DXZ Lemma 2.4 supplies its upper semicontinuity.

Put \(\overline U_t=V^{-1}\int_XU_t\omega^n\). The bound used in the proof of MP Lemma 5.3.1 is
\[
 0\leq \sup_XU_t-\overline U_t\leq T_\omega .
\]
Equivalently, apply the uniform L¹ bound for ω-psh functions with supremum zero to \(U_t-tc\). Dividing by t yields
\[
 c-T_\omega/t\leq \overline U_t/t\leq c.
\]
The integral-slope identity therefore gives φ(o)=c. The fixed ordinary/squared-norm convention conversion rescales both potential and logarithmic time together, leaving this quotient unchanged. This is the same normalization interface stipulated in the existing finite-energy correspondence, not a newly changed convention.

Thus the frozen citation encompasses the needed argument. Including the displayed sup–mean estimate in a future pedagogical integration would improve readability, but no substantive mathematical correction to the frozen conditional proof is requested.

### 5. Both full-cone directions close without a uniform energy estimate

Forward direction: every DXZ truncation has an MP finite-energy image. Their divisorial truncation values decrease, and MP comparison gives the global decreasing order. The zero-valuation values tend to the finite endpoint cΓ, preventing the limit from being identically −∞. The proved completion lemma makes the limit MP psh; the conditional all-point comparison identifies it with FΓ.

Reverse direction: max(φ,−j) is bounded MP psh. Upper semicontinuity on the compact spectrum supplies its finite upper bound, and energy monotonicity between constants makes it finite-energy. Its finite-energy DXZ inverse images decrease by divisorial order reflection. Their endpoints have the finite lower bound φ(o), since the zero valuation belongs to the MP divisorial locus. The decreasing DXZ infimum theorem thus applies with its actual endpoint hypothesis. The source's divisorial and endpoint limit formulas supply agreement with φ on D. The conditional all-point comparison then gives equality everywhere.

The second invocation of the forward result in this direction is not circular: that result was already established for every DXZ object. No decreasing closure of an unspecified larger cone is used.

### 6. Order and extended energy

Divisorial order reflection supplies injectivity and order reflection. MP comparison supplies order preservation after positivity of each image is established. The argument includes the zero valuation and therefore does not lose endpoint information.

Agreement of finite-energy values alone would not prove equality of extended-energy domains. The packet additionally checks this: if FΓ has finite MP energy, take its finite-energy DXZ inverse image. Divisorial injectivity forces that object to equal Γ. Thus the finite-energy domains correspond in both directions, and assigning −∞ to their complements gives the claimed extended equality. This argument is sound and does not rely on unproved continuity of energy for the new truncation construction.

## Remaining conditions and exclusions

No substantive gap remains in this conditional implication relative to the stated external inputs. This verdict does not discharge A1 or A2, independently audit the entire existing finite-energy theory, confer a production verdict, or authorize integration.

All new mathematics and both topological candidate dependencies remain subject to the user's independent and production Rethlas sol/xhigh gates. The production permission gate is unchanged; no production call, live edit, inventory change, or permission workaround was made.

The report does not retire the complete pseudoeffective P14.3 problem, solve a general envelope problem, construct zero-volume energy, or extend the unchanged relatively nef MP cone to big non-nef classes.

