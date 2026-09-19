# Mathematical audit of Part 1 (ch01–ch08) and the appendices

Date: 2026-09-14.  Status: **closed**.  Every item was re-derived by hand before
any edit.  `lint.py` and `refs.py` run clean on all touched files; manual `\tag`
sequences untouched.  **Nothing is compile-verified.**

---

## The one structural item: two different lengths on a skeleton edge

`rem:lattice-length` (ch05) computed the **lattice length** of the edge
`σ_{i,i'}` correctly as `1/lcm(b_i,b_{i'})` — with `Aff_Z(σ_J) = {Σ a_jα_j :
a_j ∈ Z}` of `def:integral-affine`, the achievable slopes in the parameter `t`
are `(a_ib_{i'} − a_{i'}b_i)/(b_ib_{i'})`, and the numerator ranges over
`gcd(b_i,b_{i'})Z` — and then asserted "This is the metric that appears in the
Laplacian."  It is not.  The metric for which the graph Laplacian equals the
Chambert–Loir measure is `1/(b_i b_{i'})` per intersection point, which is
`gcd(b_i,b_{i'})` times smaller.  Meanwhile ch20's
`rem:ch20-multiplicities-lengths` asserted `1/(b_ib_j)` **in the integral affine
structure**, and ch22 contained both claims (line 299 the lcm one, line 1888 the
`b_Fb_{F'}(F·F') = 1/(t_{F'}−t_F)` one).

The witness, now written into ch05.  On `X = P^1_K` blow up `T=0` in the special
fibre of `P^1_R`, then the resulting node — giving `F_2` with `b = 2` at
`v(T) = 1/2` — then a closed point `Q` of `F_2` on no other component.  The
exceptional `G` has `b_G = ord_G(π) = 2` (locally `π = u²`, so `π = u_1²` in the
blowup chart) and meets `F̃_2`, also of multiplicity `2`, at one point:
`gcd = 2`.  With `D = G` one has `φ_G(x_G) = 1/2` and `φ_G = 0` elsewhere.  The
model measure has atom `b_G(G²) = 2·(−1) = −2` at `x_G`; the graph Laplacian
gives `(0 − 1/2)/ℓ`, so `ℓ = 1/4 = 1/(b_Gb_{F̃_2})`, and the lattice length
`1/2` would give `−1`.

Independent check, free of any convention about lengths: let `c̃ ∈ R^×` lift the
coordinate of `Q` on `F_2 ≅ P^1_k` and put `f = T² − c̃π`.  Then
`ord_{F_2}(f) = 2`, so `v_{F_2}(f) = 1`; and `ord_G(f) = ord_G(π) +
ord_G(T²/π − c̃) = 2 + 1 = 3`, so `v_G(f) = 3/2`.  On `X`, `div(f)` is the
degree-two closed point `{T² = c̃π}` minus `2[∞]`, and both retract to `x_G` and
`x_{E_0}` respectively, so `r_*div(f) = 2δ_{x_G} − 2δ_{x_{E_0}}` and
`eq:ch08-slope-formula` puts the atom `−2` at `x_G` — again forcing `1/4`.

Applied in three places: ch05's `rem:lattice-length` now states both lengths,
their ratio `gcd`, and the witness; ch20's remark says "analytic length", with a
pointer; ch22's line 299 is corrected the same way, noting that every example
used there has `gcd = 1`.  All existing numerical examples in the book are
unaffected: every edge in them has `gcd(b_i,b_j) = 1`, where the two lengths
agree.

---

## Part 1

### ch02 — the two invariants do not separate four types
"For points of analytic curves, these two invariants distinguish the four types"
is false for types I and IV: over `C_p`, a type-IV point has `H(x)` a proper
**immediate** extension of `K`, so value group `p^Q` and residue field `F̄_p`,
identical to a type-I point's.  `ch04`'s own `prop:berk-type-invariants` carries
the extra clause `H(x) ≠ K` precisely for this reason.  Corrected to: the
invariants separate II and III from each other and from the pair {I, IV}.

### ch03 — the SNC definition admits a non-SNC model
The displayed local condition `π = u z_0^{b_0}⋯z_r^{b_r}` for *some* regular
parameters does not force the `z_i` to cut out **distinct** components, nor the
components to be regular.  An `I_1` degeneration of an elliptic curve — special
fibre one irreducible nodal rational curve, local equation `xy = π` at the node —
satisfies it with all `b_i = 1`, hence would be "strictly semistable", yet its
special fibre is not an SNC divisor and its dual complex is a loop.  ch03 itself
excludes this case at `ex:snc-chain-models` (`n = 1`), and ch05 quotes a
definition that includes the regularity clause.  Both missing clauses added,
with the counterexample.

### ch04 — the disc-combinatorics lemma needs a dense value group
`lem:berk-disc-combinatorics`(3) and the sentence "two discs give the same
seminorm precisely when they are the same disc" are stated before the standing
hypothesis "algebraically closed and nontrivially valued" is imposed, and they
are false over `Q_p`: `D(0,p^{-1/2}) = D(0,p^{-1}) = pZ_p` as sets, while
`|T|` at the two Gauss points is `p^{-1/2} ≠ p^{-1}`.  The hypothesis
`|K^×|` dense in `R_{>0}` was added to the lemma (parts (1) and (2) hold over
any `K`), and the claim "nontriviality is never used" in the classification was
qualified accordingly.

### ch05 — three further items
* The refinement proof asserted that `x` and `x'` have the same `X`-center.
  False: when `ξ` is a closed point of `E_i` on no other component,
  `c_X(x')` is the **generic** point of `E_i`.  Replaced by the argument that
  works: `c_X(x')` is a generization of `ξ`, so `J(c_X(x')) ⊆ J(ξ)`, and the two
  normalizations `Σ b_jv(z_j) = 1` with positive terms force equality.
* Tate degeneration: `yz = πF` with `z' = zF` gives `yz' = πF²`, not `πF`.  The
  coordinate change is `z' = z/F`.
* `φ_{-F}(B) = −(−1)·1/3` is the value of `h = −φ_{-F}`, not of `φ_{-F}`;
  `φ_{-F}(B) = b_F^{-1}ord_F(−F) = −1/3`, as the same example's
  `log|a|(v_α) = −h(α)` twelve lines later confirms.
* "Residue characteristic zero is used exactly once" was weakened: the
  coefficient-field presentation of `Ô_{X,ξ_J}` in `sec:skeleton-monomial` needs
  equal characteristic, and the graded substitute is now named as the
  characteristic-free construction.

### ch06 — a sign in the weight/section dictionary
`‖f‖ = |f|e^{-φ}` with `φ = −log|f|` gives `‖f‖ = |f|²`, not `1`.  On `P^1_K`
with `f = π`: the claimed metric has `φ ≡ 1` and `‖π‖ = e^{-2}`.  The weight
making `‖f‖ ≡ 1` is `φ = log|f| = −v(f)`; `φ = v(f)` is the one making
`‖f^{-1}‖ ≡ 1`, as `prop:metric-difference-model` already says.

### ch07 — two items
* The argument that `(+∞)+(−∞)` cannot be defined is invalid as written:
  "the same argument with the roles exchanged forces the opposite sign" is false
  — the exchanged computation gives `s = −1 + s`, satisfied by both signs.
  Associativity genuinely does not exclude a value: inf-addition
  `(+∞)⊕(−∞) = −∞` is commutative, monotone and associative, as is its mirror.
  The real obstruction is limits: `n + (−n + c) → c` for every `c`, which is the
  chapter's own `lem:extended-real-safe`(5).  Replaced.
* "Directedness fails … for the family of compact subsets of a noncompact space
  ordered by reverse inclusion" is false: `K_1 ∩ K_2` is a compact lower bound
  for inclusion, hence an upper bound for reverse inclusion (and `∅` is a
  maximum).  What such a family lacks is a cofinal exhaustion.  Corrected.

### ch08 — four items
* `v(j) = 0` for `j = 0` contradicts `v(0) = +∞` (appJ's own convention and unit
  test 9).  Corrected to `+∞`; the conclusion (integral `j`, potential good
  reduction) is unaffected.
* The "epigraph-like polyhedron" `{(m,s) : ⟨m,u⟩ ≤ −F(u) + s ∀u}` is **empty**
  for full-dimensional `P`: positive homogeneity of `ȟ_P` forces
  `⟨m,u⟩ ≤ −ȟ_P(u)` for all `u`, hence
  `sup_{m'∈P}⟨m',u⟩ ≤ inf_{m'∈P}⟨m',u⟩`.  Numerically, `n=1`, `P=[0,1]`,
  `F = max{0,−u}`, `m = −1/2`, `u = −N`: the sum is `3N/2 → ∞`.  Corrected to
  the epigraph of the Legendre transform `F^*`, whose domain is `−P`.
* Thuillier's Green functions are `log p` **times** Rumely's, not `(log p)^{-1}`
  times: `ℓ_T = (log p)ℓ_R` and the Green function scales linearly in edge
  lengths; `ddc = (log p)^{-1}ddc_R` then gives `g_T = (log p)g_R`.  Check:
  `e = 1`, `p = 3`, one edge, midpoint charge — `g_R = 1/4`,
  `g_T = (log 3)/4`.
* "The four zero coefficients are the reason the point `t=1` contributed nothing
  in `ex:ch08-newton-cubic`" is a false explanation: those coefficients are
  atoms of a different measure, and if they were the reason they would equally
  kill the atoms the chapter computes at `t = 2,3,4`.  The reason is that `F` is
  affine across `t = 1` (`f` has no root of valuation one).

---

## Appendices

### appH — three items
* The test-curve definition omitted **upper semicontinuity in `τ`**, which
  `def:appD-test-curve` requires and `eq:rays-test-endpoint` (ch52) stipulates.
  Without it the displayed inverse transform is false: on `P^1` with
  `θ = ω_FS`, `ψ_τ = 0` for `τ < 0`, `ψ_0 = P_θ[½u]` with
  `u = log(|z|²/(1+|z|²))`, `ψ_τ = −∞` for `τ > 0` satisfies every other listed
  condition, has `u_t ≡ 0`, and the inverse transform returns `0` at `τ = 0`.
  Hypothesis restored, with the witness.
* `P_θ[u] ≤ P_θ[u]_I` was argued by containment of competitor families.  The
  ordinary family requires only `w ⪯ u`; the ideal family requires equality of
  all multiplier ideals, so the containment goes the wrong way — for `u = 0` on
  `P^1`, `w = log(|z|²/(1+|z|²)) ≤ 0` satisfies `w ⪯ 0` but has
  `I(w) = m_0 ≠ O_X`.  Replaced by the argument through idempotence:
  `P_θ[u] ∼_I u`, so `P_θ[u]` is itself a competitor.
* The nonpluripolar product was defined by truncating the **global**
  `θ_j`-psh potentials, for which `ddc u_j` is not positive and
  `max{u_j,−k}` is not psh.  Corrected to local psh potentials, as
  `ch51` states it.

### appA — a missing injectivity hypothesis
"In characteristic zero, a finite universal homeomorphism … is subintegral"
needs injectivity (e.g. reduced source): `Q[x]/(x²) → Q` is a finite universal
homeomorphism with trivial residue extension and nonzero kernel, and
`def:appA-subintegral` is a condition on an extension.  Added.

### appF — a non-sequitur in the monotone-continuity derivation
`A(α_{i,b}) ⊆ A(α_i)` gives only `lim_b I ≥ I`; the reverse needs
`⋃_b A(α_{i,b})` cofinal in `A(α_i)`, which fails because a nef Cartier
`θ ≥ α_i` need not dominate `α_{i,b}`.  The derivation was replaced by the
correct one-sided statement plus the honest import from [DF20, Thm 3.2],
where monotone continuity is already listed.

### Appendices found clean
appB, appC, appD, appE, appG, appI: audited in full, no mathematical defect
found.  Of note: appD's `thm:appD-concave-duality` correctly requires upper
semicontinuity (it is appH that dropped it); appC honours its own
`rem:appC-asymptotic-valuative-safeguard`, ch40 using only the ordinary-ideal
criterion plus the one-sided estimate; appE nowhere claims a directed set has a
cofinal sequence; appI is a Stacks-Project tag ledger and contains no stacky
statements at all (terminology only: it says "strict transform" where appB says
"pure transform").

### appJ and appK found clean
All twelve translation-table rows and all nine unit tests were recomputed and
check out, including `ddc = (i/2π)∂∂̄ ⟹ ddc log|z|² = δ_0`,
`c_p = (−1)^{p(p−1)/2}`, the total-mass identity
`Σ_E b_E(L_1⋯L_n·E) = (L_1⋯L_n·X_s)`, and the radial-parameter row added on
2026-09-01.  appK's entries agree with the body definitions checked.

---

## Reported and rejected

* **ch01.** Audited in full; no defect found, and the report said so.  Every
  worked example — the equilibrium lemma with `ddc = (4π)^{-1}Δ`, the blowup
  model function, the node blowup with `b_E = 2` entering twice, the toric
  two-break example, the product test configuration with `DF = 0` — recomputes
  exactly.
* **ch05 base-change heuristic for the edge length.**  An argument that the
  analytic length of the `gcd = 2` edge is `1/lcm = 1/2`, on the ground that the
  two Galois-conjugate branches upstairs each map bijectively onto it, was
  checked and **rejected**: the slope-formula computation with
  `f = T² − c̃π` gives `1/4` unambiguously, the degree-two closed point
  contributing mass `2` to `r_*div(f)`.
