# Mathematical audit of Part 5 (ch51–ch62) and Part 6 (ch63–ch71)

Date: 2026-09-14.  Status: **closed** (ch72 excluded by instruction).  Every
item was re-derived by hand before any edit.  `lint.py` and `refs.py` run clean
on every touched file; manual `\tag` sequences preserved (ch52 1–30, ch56 1–24,
ch69 1–39 after a deliberate reordering described below; ch71's pre-existing gap
at 71.33–71.35 was left alone).  **Nothing is compile-verified.**

---

## The largest item: the hyperplane test curve on `P^n` (ch52, ch56)

`ex:rays-hyperplane-test-curve` asserted that the Bergman test curve of the
order-of-vanishing filtration along `H = {x_0 = 0}` has levels
`Γ_τ = τψ`, `ψ = log(|x_0|²/|x|²)`, and dual ray `Γ_t^* = max{0, t+ψ}`.  Both
are wrong, and for the same reason: definition (52.28) normalizes competing
sections by their **sup norms** (`|s|²_{h^m} ≤ 1`), which contributes an entropy
term that `τψ` omits.

Write `a_i = |x_i|²/|x|²`.  A monomial `x^J` with `J_0 ≥ mτ` has
`sup_X |x^J|²_{h^m} = ∏_i (J_i/m)^{J_i}`, so the normalized monomial contributes
`Σ_i σ_i log a_i + H(σ)` with `σ = J/m ∈ Δ_n`.  The unconstrained maximum over
`Δ_n` is `0`, at `σ = a`; hence

```
Γ_τ = 0                                                  if τ ≤ 0 or a_0 ≥ τ,
Γ_τ = τ log a_0 + (1−τ) log(1−a_0) + H_2(τ)              if a_0 ≤ τ ≤ 1,
```
with `H_2(τ) = −τlogτ − (1−τ)log(1−τ)`.  The discrepancy is already visible at
`m = 2`, `n = 1`, `τ = 1/2`: the section `s = 2x_0x_1` lies in
`F^1H^0(O(2))`, has `|s|²_{h²} = 4a_0(1−a_0) ≤ 1`, hence is admissible, and at
`a_0 = 1/4` gives `(1/2)log(3/4) = −0.1438`, while `(1/2)ψ = −0.6931`.  The
corrected formula returns exactly `−0.1438`.

The Legendre transform is the log partition function,
`Γ_t^* = log(e^t a_0 + 1 − a_0) = log(1 + (e^t−1)e^ψ)`, the supremum being
attained at `τ = e^t a_0/(e^t a_0 + 1 − a_0) ≥ a_0`.  This is the **product
geodesic ray**, which is what `ex:rays-p1-action` (same chapter) and
`ex:rf-p1-complete` (ch65) both say the answer should be.  That
`max{0, t+ψ}` is not a geodesic at all follows from the energy: for `n = 1`,
`θ` pushes forward to `da_0` on `[0,1]`, and
`E(max{0,t+ψ}) = (t−1+e^{−t})/2`, so the value at `t=2` is
`(1+e^{−2})/2 = 0.5677` while twice the value at `t=1` is `e^{−1} = 0.3679` —
not affine.  The corrected ray has `E = t/2` exactly.

Everything downstream survives, and the record says so: the two rays differ by
at most `log 2`, the mass is still `M_θ(Γ_τ) = (1−τ)^n` (on `{a_0 > τ}` the
curvature is `θ`; on `{a_0 < τ}` it is `τ[H] + (1−τ)η` with `η` pulled back
from `P^{n−1}`, so `η^n = 0`, and `[H]` is pluripolar; and `θ^n` pushes forward
to normalized Lebesgue measure on `Δ_n`), the energy is still `1/(n+1)`, and
`sup_X Γ_1^* = 1`.

**Propagation into ch56.**  `ex:va-hyperplane-analytification` said each level
"has analytic singularities along a single smooth divisor".  The corrected level
has two centres: coefficient `τ` along `H` and coefficient `1−τ` at
`P_0 = [1:0:⋯:0]`.  So
`(Γ_τ)^An(v) = −τ v(H) − (1−τ)v(m_{P_0})`, and
`Γ^An(v) = max{0, −v(m_{P_0}), 1−v(H)} = max{0, 1−v(H)}` — the same final
answer, since `v(m_{P_0}) ≥ 0`.  The Gauss-identity check likewise survives:
the corrected complexification `Ψ = log(|s_H|²/|z|² + (1−|s_H|²))` has
`σ(v)(Ψ) = min{v(H)−1, v(m_{P_0})} = min{0, v(H)−1}`, because `H` and `P_0` are
disjoint so at most one of the two valuations is nonzero.

---

## Part 5

### ch51 — five items
* `ex:ch51-disk-three-types` had the first link of the singularity chain
  reversed.  With `u_2 = u_1 + u_3` and `u_3 < 0`, one has `u_2 ⪯ u_1` and
  `u_1 ⋠ u_2`; the chain is `u_2 ⪯ u_1 ⪯ u_3 ⪯ u_4`.  The stated version is
  impossible for any `u_2`: `ν(u_2,0) = 1` already forces
  `u_2 ≤ u_1 + O(1)` by the convexity clause of `prop:ch51-lelong-three`, so
  `u_1 ⪯ u_2` would give `u_1 ∼ u_2`, contradicting the example's own point.
  The ambiguous `\log(-\log|z|^2)^{-1}` was also written out as
  `−log(−log|z|²)`.
* Skoda's bound `ν > n` was weakened to `ν ≥ n` at four places.  `ν ≥ n` gives
  `λ_φ(t) ≤ λ_φ(t_0) + n(t−t_0)`, hence `φ ≤ n log|z−x|² + O(1)` and
  `e^{−φ} ≥ c|z−x|^{−2n}`, whose integral diverges.  The chapter's own middle
  example (`φ = n log|z|²`, `ν = n`, not integrable) proves it.  "The bounds are
  sharp at both ends" / "neither bound can be improved" now read "neither
  *constant* can be moved", which is what the `γ < n` example shows.
* The floor derivation had `k ≥ ⌈λ⌉−1+1 = ⌊λ⌋`, which is false for
  `λ ∉ Z` (at `λ = 1.5` it gives `2`, not `1`).  The chain is
  `k > λ−1 ⟺ k ≥ ⌈λ−1⌉ = ⌈λ⌉−1 = ⌊λ⌋`.  The endpoint discussion also had the
  two conventions swapped: `(z^{⌈λ⌉−1})` comes from the **non-strict**
  `k ≥ λ−1`, and differs from ours only at integral `λ`.
* Twice — before `eq:complex-p-i-comparison` and at the head of
  `sec:ch51-i-envelope` — `P_θ[φ] ≤ P_θ[φ]_I` was justified by "the constraint
  is weaker, so the envelope is larger".  The two competitor families are
  **incomparable**: on `P^1` with `φ = ½G_0`, `ψ = G_0 ≤ 0` satisfies
  `ψ ⪯ φ` but `ν(ψ,0) = 1 ≠ ½`; and in `ex:ch51-cantor`, `ψ = 0` satisfies
  `0 ∼_I φ_{1/2}` but not `0 ⪯ φ_{1/2}`.  Replaced by the argument the chapter
  actually proves in Step 3 of `thm:complex-i-projection`.

### ch53 — a missing square
`φ = log|s_E|_h` with `θ + ddc φ = [E]` is impossible in the convention
`ddc = (i/2π)∂∂̄`, where Lelong–Poincaré reads `ddc log|s_D|²_h = [D] − Θ_D`:
one gets `½(θ + [E])`, and `ν_E(log|s_E|_h) = ½`.  Corrected to `log|s_E|²_h`,
matching the squared-norm convention used throughout ch52 and ch56.

### ch59 — a sign claim that the chapter's own definition contradicts
`prop:mp-pl-vcar`'s proof asserted `D` anti-effective "since `bO ⊆ O`", and that
"both sides are nonpositive on `PL^+` generators".  `def:mp-pl-functions` allows
arbitrary integer shifts `k_j`, so `φ ≡ 1` is in `PL^+` (take `N = 1`,
`a_1 = O_X`, `k_1 = m = 1`), and on the product model it gives `D = X_0`,
effective.  The chapter's own density proof forms `max{f, 0}` with positive
values, and the converse half of the same proposition already says "fractional
flag ideals".  Corrected: the sign is forced only for `k_j ≤ 0`; in general
`b = t^{−k}b_0` and `D = D_0 + kX_0`.  The coefficient formula (59.14e) is
untouched.

### ch54, ch55, ch57, ch58, ch60, ch61, ch62 — audited, nothing found
Recomputed in full, including: ch55's `P^1` DH example and the `n!`
normalization chain `λ_n(Δ) = vol/n!` → `DH(Γ)(R) = vol(Γ)`; ch60's
deformation-to-the-normal-cone numbers on `P^2` (`E_α = −c³/3`, `J_α = c³/3`,
`A^tot(v_{E_1}) = n+1`, `Ent = 2c²`) and the Mabuchi normalization against
ch50's (50.49)–(50.59); ch61's `P^1` Calabi–Yau example and the sharpness of
`1/(n+1)` in (61.10); ch62's factor-`n` correction `s = −nC/V`, verified by the
product-model unit test, and (62.24) verified in two independent cases whose
Legendre transform reproduces ch61's `E^∨`.

---

## Part 6

### ch66 — Laurent series where power series are meant
"Let `A_r` be the Banach algebra of **Laurent** series in `t` converging for the
hybrid norm of radius `r`.  Its spectrum is homeomorphic to a closed disc."
With Laurent series `t` is a unit, `‖t‖ ≤ r` and `‖t^{-1}‖ ≤ r^{-1}` force
`|t|_x = r` exactly for every bounded multiplicative seminorm, so the spectrum
lies over the **circle** and the complex points with `|t| < r` that (66.7)
requires are missing.  Corrected to power series, with the reason.

### ch68 — a hypothesis the proof does not use
`thm:ytd-smooth-functional-slopes` was stated "under the subklt logarithmic
extension hypotheses of [BHJ19, Thm 4.2]".  Its proof applies
`thm:rf-bhj-unaffected-slopes` (ch65), which supplies the slope identities
**unconditionally** in the absolute case from [BHJ19, Thm 3.6] and quarantines
the subklt condition to the logarithmic setting in a separate sentence.  The
chapter is a smooth polarized projective manifold throughout, with no boundary
divisor, so the hypothesis is also vacuous.  Removed, and `prop:ytd-status`
item 2 corrected.

### ch69 — a hypothesis that is a consequence
`thm:verified-cld-criterion` listed `d'd''u = d'd''v` as a hypothesis alongside
the pluriharmonic approximation (69.3).  The proof uses only the latter, and the
latter implies the former (`d'd''h_j = 0` with `h_j → h` locally uniformly gives
`d'd''h = 0`).  Restated as a consequence, with the two tags exchanged so the
sequence stays in order.  The companion `prop:verified-cross-fan` said its
example fails "despite the preceding equality"; the equality it verifies is for
the **unit-weighted** fan, whereas `T` carries weights `(2,2,1,1)`, for which
`d'd''[u] = 8δ_0 ≠ 6δ_0 = d'd''[v]`.  Reworded to say what actually fails.

### ch71 — a gap at the trivial semivaluation
`cor:p143-all-point-kahler-comparison` invokes
`thm:p143-dominated-divisorial-density`, whose comparison clause requires
agreement on `X^div`, and the chapter's convention (following [MP24, Def. 2.3.1])
puts the trivial semivaluation `0` in `X^div`.  The cited identity (71.40) is
stated only for `p ∈ Q_{>0}`.  The missing case is true and one line —
`T_Γ(0) = Γ_max` by `prop:pseff-one-curve-transform`(1), and
`φ(0) = sup φ = Γ_max` by the maximum principle — and is now supplied.

### ch63, ch64, ch65, ch67, ch70 — audited, nothing found
Recomputed in full, including: ch63's `b_E`/`b_E^{-1}` cancellation and the
`P^1` DH example; ch64's nonreduced-curve example (mass `4δ_{x_0}+δ_{x_1}`,
generic degree `5`) and the BHJ moment identity checked on `P^1` via the
Grothendieck relation; ch65's factor-two firewall
(`φ_{2s}/(2s) = ψ_s/s`) and the limit `(1/m)log Σ_j e^{tj}|z|^{2j} →
max{0, t+log|z|²}` — note that this **is** `max{0,t+ψ}`, because there the
monomials are unnormalized, which is exactly the distinction the ch52 repair
turns on; ch67's non-Archimedean coefficient check
`Σ_{F↦E} b_F((f^*L)|_F^n) = d·b_E(L|_E^n)`; and, in ch70, the polarization plus
relative-Hodge-index argument of `thm:local-generalized-lelong-separation` and
the Gauss-shell comparison `thm:local-cld-model-comparison`, including the
`2^n` audit.

---

## Reported and rejected

* **ch66's coefficient `b_σ^{-1}λ_σ` vs `b_σλ_σ`** in
  `thm:hybrid-volume-forms`: raised as uncertain, not reported as a finding, and
  left alone here for the same reason — settling it needs the exact residue
  normalization `Res_{Y_σ}(ψ)`, which is worth an editorial pass of its own.
