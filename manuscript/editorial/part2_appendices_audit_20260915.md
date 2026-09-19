# Part 2 foundations and appendices — adversarial audit and repair
## 2026-09-15 (wave 8–9)

Scope: ch09–ch14 (the Lagerberg/CLD foundations) and appendices A–K.
All edits applied to live chapters. `refcheck.py` run after every batch:
282 files in the build closure, 10 985 labels, 0 multiply defined, 0 dangling.
**Not compile-verified** — the mounted shell's TeX tree lacks `newtxtext.sty`,
so verification was by `refcheck.py` (which also checks environment balance and
brace balance per file) plus hand re-derivation of every edit.

---

## A. The two convention contradictions

### A.1 The double-primed contraction (ch09 vs ch11) — resolved in favour of ch11

`def:ch09-contraction` defined the *graded* contraction,
`ι''_v(a d'x_I ∧ d''x_J) = (−1)^p a d'x_I ∧ (ι_v d''x_J)`, and proved from it
that `ι'_v ι''_w = −ι''_w ι'_v`, `J ι'_v J = ι''_v`, and a clean four-identity
Cartan proposition. `def:ch11-contractions` defined the *block* contraction,
with **no** traversal sign, proved `ι'_v ι''_w = +ι''_w ι'_v`, and declared in
so many words: *"Ours is fixed for the whole book and recorded in
§`sec:appJ-currents`."*

Three facts settled the direction:

1. **The book had already declared ch11's convention**, and ch11's whole
   §`sec:ch11-boundary` narrative — the constant `c_n c_{n−1} = (−1)^{n−1}`,
   `thm:ch11-defect-stokes`, `lem:ch11-trace-normal-form`, the sign table — is
   written in it. ch09 presented its sign as forced ("not an extra convention
   but the antiderivation sign"), never flagging a choice.
2. **`sec:appJ-currents` recorded neither.** ch11's forward promise pointed at
   a section that did not contain the statement.
3. **ch13 mixed the two**, and that was a real error, not a stylistic one.
   `eq:ch13-boundary-integral` carries the prefactor `(−1)^{n−1}` *and* cites
   `def:ch09-contraction` for the meaning of `ι''`. On `A^{n−1,n}` the two
   conventions differ by `(−1)^p = (−1)^{n−1}`, so read with ch09's convention
   the formula is off by `(−1)^{n−1}` — wrong in every even dimension.

**Applied.** ch09 now defines `ι'_v`, `ι''_v` as the block contractions and
retains the graded operator under its own name `\widetilde\iota''_v :=
(−1)^p ι''_v`, which carries all of ch09's structural content:

- `lem:ch09-contraction-basic`(1): `ι'_v` and `\widetilde\iota''_v` are the
  interior products of `∧•(V*⊕V*)` by `(v,0)` and `(0,v)`; both are
  antiderivations for the total degree. `ι''_v` is an antiderivation within its
  own block only (its Leibniz rule is `lem:ch11-contraction-basic`).
- (2): `ι'_vι'_w = −ι'_wι'_v`, `ι''_vι''_w = −ι''_wι''_v`, and the mixed pairs
  **commute**, `ι'_vι''_w = ι''_wι'_v`, equivalently
  `ι'_v\widetilde\iota''_w = −\widetilde\iota''_wι'_v`.
  (Derivation: `ι''_v` preserves the primed degree, so the two conversion
  factors `(−1)^p` cancel in the like-pair relation; `ι'_v` lowers it, so they
  are `(−1)^p` and `(−1)^{p−1}` in the mixed relation and absorb the sign.)
- (3): on `A^{p,q}`, `Jι'_vJ = (−1)^pι''_v = \widetilde\iota''_v` and
  `Jι''_vJ = (−1)^qι'_v`.
- `prop:ch09-cartan` is stated for `ι'_v`, `\widetilde\iota''_v` with all four
  identities clean, plus the block forms
  `ι''_vd'' + d''ι''_v = (−1)^p∂_v` and `ι''_vd' − d'ι''_v = 0`.
- `ex:ch09-contraction-examples`: `ι''_v(d'd''u) = +d'(∂_v u)` now (no sign);
  the `τ_2` computation is unchanged because `p = 2` there; the closing
  comparison no longer invites double-counting the `(−1)^{n−1}`.
- Sign-checklist item 4 rewritten; the section preamble no longer says the
  second-block operator "carries a sign".
- New `rem:ch09-contraction-convention` records the choice and points at ch11
  and appJ.

Also applied: ch11's promise now names `def:ch09-contraction` and the new
remark; ch13's `eq:ch13-boundary-integral` gloss now names the block
convention explicitly; ch14's two uses of `Jι'_EJ = ι''_E` carry the sign;
ch10's `n = 1` trace notes that the prefactor is `+1` there; and
`sec:appJ-currents` now carries the convention, the graded variant, and the
test that detects the double count.

### A.2 ch14's J-symmetry — was inverted in odd bidegree

Ground truth (ch09, `cor:ch09-symmetric-exchange` and its proof):
`J τ_n = (−1)^n τ_n`, and a symmetric `(p,p)`-form satisfies
`J α = (−1)^p α`, **not** `J α = α`.

ch14 wrote symmetry as `S ∘ J = S` and asserted that `J` acts trivially on
`τ_n` and on top-degree forms. For odd `p` that **inverts** the condition: it
says the functional kills the *symmetric* forms, hence every positive one, and
`prop:ch14-automatic-continuity` — on which `δ_Y`, the Dirac masses, fibre
integration and weak compactness all rest — becomes vacuous.

**Applied.** ch14 now defines `J` on currents and says what symmetry means:

- `eq:ch14-J-current`: `⟨JT,α⟩ = (−1)^n ⟨T,Jα⟩` for `T ∈ D^{p,q}`,
  `α ∈ A^{n−q,n−p}_c`, so that `JT ∈ D^{q,p}`.
- `lem:ch14-J-currents`: `∫_X Jη = (−1)^n ∫_X η` on `A^{n,n}_c`;
  `J[ω] = [Jω]`; and for `T` of bidegree `(p,p)`, bidimension `(q,q)`,
  `JT = (−1)^p T ⟺ ⟨T,Jα⟩ = (−1)^q ⟨T,α⟩`.
- `def:ch14-symmetric-current`, with the mnemonic that the current pairs with
  `Jα` exactly as a symmetric test form of bidegree `(q,q)` transforms, and an
  explicit note on why `+1` would be vacuous in odd bidimension.
- Seven downstream sites corrected: the `ddprime[ω] = [ddprime ω]` clause, the
  symmetry of `[ω]`, the hypothesis and proof of
  `prop:ch14-automatic-continuity`, `prop:ch14-positive-and-negative`(1), the
  Riemannian integration current `[M]_s` (with the derivation
  `a(Jα) = (−1)^m a(α)`), `δ_Y`, and the weak-compactness limit.
- A "Symmetry" row added to ch14's convention-comparison table.

Consequences of the new definition, found and fixed in the same wave:
`J T_h = −T_h` and `J d'd''h = −d'd''h` in bidegree `(1,1)` (both were written
with `+`), and the pushforward commutation, which is
`g_*J = (−1)^{n_Y−n_X} J g_*`, not `g_*J = Jg_*`. The corollary that
pushforward preserves symmetry survives, because the bidegree also shifts by
`n_X − n_Y`; `g_*d'' = d''g_*` survives because the sign enters squared.

A book-wide sweep for `J α = α`, `J τ_n = τ_n`, `J fixes`, `acting trivially`,
`S ∘ J = S` now returns only the four deliberate CLD-comparison occurrences.

---

## B. Appendix defects

**appJ** (the registry ~70 chapters defer to):

- The preamble said *"the notation `ddc` belongs to complex geometry"*. It is
  also the **model** operator on numerical classes, defined at
  `sec:ch20-ddc` and used 444 times in part 3 and 120 times in part 4;
  `sec:ch20-normalization-audit` and appK's own collision rule say so. Rewritten
  to type `ddc` by setting.
- appJ and appK typed the glyphs `φ` = non-Archimedean and `ϕ`(varphi) =
  complex squared-norm. Part 3 does the opposite: 5194 `\varphi` against 69
  `\phi`, with `‖·‖_φ = e^{−φ}‖·‖_0` and `φ_D = −log|f_D|` all written
  `\varphi`. A reader applying the table to part 3 halves every weight —
  exactly the factor-two error §`sec:appJ-rays` exists to prevent. Both tables
  and both appK entries now say the letters are not typed and that the norm
  symbol decides.
- `f ∈ \Supp(x)` was a type error: appK reserves `supp(v)` for the prime ideal
  and `\Supp(v)` for the analytic subspace. Corrected.
- The factor-two paragraph attributed both failure modes to
  `sec:rf-factor-two-firewall`, which names only the group-action one, and used
  `\log_r` without defining it. The asymptotic failure is ch66's
  `eq:hybrid-squared-norm-asymptotic`; now cited there.
- **Added** the two skeleton edge-length normalizations (`J.2a`): analytic
  `1/(b_i b_j)` versus integral-affine lattice `1/lcm(b_i,b_j)`, with
  lattice = `gcd` × analytic. This is a documented two-convention hazard in
  ch05/ch20/ch22/ch34 that the registry did not carry.
- **Added** the current-differential sign `J.20a` and the `J`/symmetry
  convention, which ch14 claimed were recorded here and were not.

**appK**: `\Cap_ω` is not a macro this book defines — it is the AMS `⋒` glyph,
so the entry typeset silently as `⋒_ω(E)`. The book has one capacity macro,
`\Capa`, distinguished by subscript, and the entry had the two subscripts
swapped: `\Capa_θ` is the BFJ mass-`V` capacity (`Capa_θ(X^an) = V`,
`def:bfj-capacity`) and `\Capa_ω` the BJ probability capacity
(`Capa_ω(X^an) = 1`, ch48). Entry rewritten. Five stray `X^{\Div}` in
ch56/ch57/ch58/ch65 changed to the registered `X^{\divis}`.

**appD**: the contraction in `eq:appD-strong-homogeneity` was spelled
`\iota_E'`/`\iota_E''` — the only such spelling in the manuscript, and the
reverse of the book's `\iota'_v`. Corrected, and `E` is now named as the Euler
field of `def:ch14-radial-contraction` rather than silently reusing the Borel
letter of the same appendix.

**appH** (the complex reference the non-Archimedean theory is calibrated
against) — two statements false as written:

- The test-curve definition imposed positive mass **at interior levels**. ch52's
  `def:rays-test-curve` imposes it only at `Γ_{−∞}` (52.6) and warns that
  reading it into the level condition "would make
  `lem:rays-test-positive-levels` vacuous" — that lemma *deduces* interior
  positivity from concavity plus the endpoint. Corrected to match.
- The `P`-projection theorem was stated entirely under `M_θ(u) > 0`. ch51's
  `thm:complex-p-projection` proves mass preservation for **every** `φ` (its
  Step 2 says verbatim that positivity is not used), idempotence for every
  **big** class including zero mass via `\cite[Thm 1.2]{PSWZ26}`, and needs
  positive mass only for the maximality characterization (51.25). appH's own
  printed proof already said as much, so the statement contradicted the proof
  beneath it. Theorem, following paragraph and the zero-mass list all corrected.

---

## C. ch11–ch14 beyond the two conventions

Applied, each re-derived before editing:

- **ch11 `thm:polyhedral-stokes` Step 4** said `J` "exchanges `ι'` and `ι''`".
  It conjugates `ι'_v` into the **graded** `\widetilde\iota''_v`. Taken
  literally the transported formula is off by `(−1)^{n+1}` — wrong in every
  even `n`, which is exactly what `ex:ch11-square-wrong-sign` exists to guard.
  (A residue of the A.1 repair.)
- **ch11 `thm:balanced-stokes`** applied `thm:polyhedral-stokes` — stated for a
  bounded rational `n`-polytope — cellwise to a complex whose facets are
  unbounded in every nontrivial case. Now cites
  `cor:ch11-stokes-unbounded`, which the chapter proves for this purpose and
  which `thm:ch11-defect-stokes` already cites correctly.
- **ch11 `cor:ch11-green-symmetry`** required `α` "closed". The first
  integration by parts needs `d'α = 0`, the second `d''α = 0`; under the weaker
  reading the second half of the proof fails. Both now required.
- **ch11 `prop:ch11-pushforward-projection-informal`** displayed
  `∫_C α = ∫_{C'} F_*α`, but pushforward of a *superform* is nowhere defined
  and the proof proves the pullback statement. Restated as
  `∫_C F^*α = ∫_{F_*C} α`, matching `prop:ch11-pushforward-integral`.
- **ch11 rectangle example**: the horizontal faces vanish because of the
  surviving **primed** factor `d'y`, not a double-primed one —
  `ι''_{∂_y}η = f d'y ∧ d''x`, and `d''x` does not vanish on the horizontal
  tangent line.
- **ch11 `ex:ch11-euclidean-normal-trap`**: the slices `σ ∩ (tv + N_{τ,R})` are
  `{x₁+x₂ = t}`, of lattice length `t`, not `1−t`; the Euclidean display
  beside it is parametrized inward from the hypotenuse. Reparametrized so the
  two agree, which is what "the same computation" claims.
- **ch11 `ex:ch11-two-lines-current`**: `A + t(0,1) = {y = t}` meets the
  vertical ray at `(0,t)`, not `(t,t)` — `(t,t)` is not on `|L|` for `t > 0`.
  The multiplicity computation was already right.
- **ch11 `ex:ch11-graph-tripod-check`**: ch08's *residual degrees* are
  `1+a₀+a₁, −a₀, −a₁`; ch11's atoms are those of `Δ_Γφ_D`, namely
  `a₀+a₁, −a₀, −a₁`. The central atom differs by the mass of
  `δ_{x_{\tilde C}}`. (ch11's earlier sentence, naming the ch08 *graph*
  computation, was already correct.)
- **ch11 source notes** cited an identity "`q = ck` in Step 3" that occurs
  nowhere in the book. The identity is Step 2's
  `d_τ ⟨n_{σ,τ}, ν_τ⟩ = 1`.
- **ch11 `lem:ch11-graph-trace`**: `d''u ∈ A^{0,1} = A^{n−1,n}` for `n = 1`, so
  the relevant slot of `cor:ch11-trace-flux` is `F_η`, not `G_θ`.
- **ch12 `ex:trop-fibre-counting`**: the criterion for `T^p = a` to have `p`
  distinct roots over an algebraically closed field is
  `char K ≠ p`, not `p ≠ char K̃`. The example's own field is `K = Q_p`, where
  `char K̃ = p` but `μ_p ⊂ C_p` — so as written the sentence asserted the
  opposite of the truth for exactly the field it is about, and misclassified
  every mixed-characteristic field.
- **ch12 `ex:trop-multiplicity-two`**: the residue extension is
  `F_{p²}/F_p` in one case and `F_{p²}(θ̄)/F_p(θ̄)` in the other; the text gave
  only the first, two sentences after distinguishing the cases. Degree 2 either
  way, so the conclusion stood.
- **ch12 `rem:trop-dimension-two-halves`**: a relative clause had lost its
  antecedent.
- **ch13**: the "compact support is necessary" counterexample was vacuous —
  `η = d''x` on `R` has `d'η = 0` and `R` as one unbounded cell has no
  codimension-one cell, so it exhibited `0 = 0`. Replaced by a cutoff
  `η = φ(x) d''x` with `∫ d'η = 1`.
- **ch13 `thm:ch13-stokes`** and `def:ch13-boundary-integral` assumed only
  topological separation, but both sides are *defined* through a smooth
  partition of unity, which `thm:cld-smooth-partition` supplies only for
  locally holomorphically separated paracompact `X`. The warning attributed
  partitions of unity to topological separation. Hypotheses added, warning
  corrected; `sec:ch13-properness` already said this.
- **ch13 `prop:ch13-skeletal-faithful`**: the global clause named only
  `(n,n)` and `(n−1,n)`, though the statement and proof cover every `(p,q)`
  with `max(p,q) = n` — and `ex:ch13-tate-forms` invokes it globally in
  bidegree `(1,0)` with `n = 1`. Widened.
- **ch13 faithfulness warning** promised a counterexample after a colon and
  delivered an instance of determination. Rewritten.
- **ch14**: the "parity remark after `lem:ch14-module-leibniz`" does not exist
  (a section heading follows immediately); the claim itself is true and is now
  stated inline. `rem:ch14-form-injectivity` said the CLD injectivity is quoted
  only in `sec:ch14-compactness`; it is also used in
  `prop:ch14-positive-and-negative`(2) and `cor:ch14-weakly-null-currents`.
  "No other statement of this chapter is used without proof" was contradicted
  by six further CLD citations. `prop:ch14-boundary-current` cited
  `thm:cld-global-stokes` (the tropical statement, which never displays
  `∫d'η = ∫^∂η`) instead of `thm:ch13-stokes`. `d_{trop}` was used twice and
  defined nowhere — it must be the supremum over moment maps, else one small
  chart makes every point removable. `ex:ch14-star-unbounded-order`(3) used a
  chart datum whose compact set `{|t+1| ≤ 1}` contains `η`, outside the chart
  domain.
- **ch13 `ex:ch13-affine-line`**: `c = f(η_{a,ϱ})` lies in `H(η_{a,ϱ})`, not
  `K`; corrected to the value at the centre. **`ex:ch13-type-two`**: `χ`
  supported in the Euclidean `ε`-ball cuts the `(−1,−1)` branch at lattice
  parameter `ε/√2`, not `ε`; the cube `{max|x_i| < ε}` gives the stated `ε` on
  all three branches.

---

## D. Reported and NOT applied

- **appJ J.36's `\uscsup`** — flagged as a possible mismatch with ch52 (52.10),
  which is unregularized. Not a defect: ch65 (65.16) and ch71 (71.20) do use
  `\uscsup`, and ch65's proof records that the regularization is harmless
  because the ch52 supremum is already psh.
- **`def:ch14-radial-contraction`** takes the naked transpose with no sign;
  whether that is the normalization compatible with `ι'_E[ω] = [ι'_E ω]` was not
  settled. It does not matter for `prop:ch14-strongly-homogeneous`, whose
  conclusion is a vanishing, but it would matter if
  `def:ch14-strongly-homogeneous` were used quantitatively in
  `sec:appD-supercurrents`. **Left open.**
- **`prop:ch13-finite-integral`** asserts
  `p_*((p^*ω)_Rad) = dc(p) ω_Rad` under "finite above the complement of a
  Zariski-closed subset of dimension `< n`"; whether that suffices for
  `p^*ω` to have compact support and for `p_*` of the measure to be Radon was
  not settled (a non-proper open immersion satisfies the hypothesis).
  Settling it needs CLD Prop. 15.4.3, which the text cites for the general
  case. **Left open.**
- **ch12 `thm:analytic-tropical-balancing` proof** quotes the slope formula as
  "the sum of the outgoing slopes ... equals the degree of the divisor";
  `eq:ch08-slope-formula` is an identity of *measures* with a minus sign,
  `Δ_Γ F = −r_* div(f)`. The conclusion is correct either way because `χ^m` is
  invertible on the fibre, so the atom at the vertex vanishes. Wording only;
  not applied this wave.
- External locators not checkable offline: BEGZ 1.16, Bou17 10.18, DDNL18mono
  1.1, GZ15 1.1, DF20 2.1/3.1/3.2, de Jong 4.1, PAG2 9.4.1/§9.6, DEL00 2.3,
  ST12 6.9(iii)/6.6, HY03 6.8, Stacks 29.49.2, 31.33.9, and the CLD25 numbers.
  In each case the mathematical content attributed to the source checked out
  independently.

---

## E. Verified clean

appG, appA, appC, appE, appF, appI came back with no mathematical defect after
full reads: the tropical semiring order conventions and `F_max(x) = −F_min(−x)`;
the Rees/integral-closure arithmetic and the `φ_a = −v(a)` sign; multiplier
ideals including geometric Skoda at `c ≥ n` and Briançon–Skoda at `t ≥ r`; the
net and usc-regularization calculus; b-divisor limits and the nef determination
argument; and twenty Stacks tags with the 081T/0815 firewall intact.

appD's convexity content is clean throughout: Fenchel–Moreau, the three
translation rules, the Legendre `inf_{t≥0}` vs `inf_{t>0}` agreement, the
Alexandrov–Fenchel expansion, Brunn–Minkowski, the real Monge–Ampère measure
and its Portmanteau statements, and the mixed-volume identity `(1/N!)T_{K_1} ∧
… ∧ T_{K_N} = V δ_0`.

ch11 and ch12: `lem:ch11-interlaced-grouped`, both Leibniz rules,
all four identities of `lem:ch11-trace-normal-form` (including that the
prefactors `(−1)^{n−1}` and `−1` are each exactly cancelled),
`thm:polyhedral-stokes` Steps 1–3, `lem:ch11-mixed-cancellation`, and every
worked example in both chapters recomputed by hand.

ch13 and ch14: every displayed sign recomputed at `n = 1, 2, 4`; the current
differential signs, `lem:ch14-module-leibniz`, `prop:ch14-boundary-current`,
the whole positivity-cone reversal, the Berndtsson metric-dependence exponents,
`thm:ch14-positive-compactness`, and `rem:ch14-fibre-hypotheses`. Neither
chapter uses manual `\tag{}`, so there is nothing to sequence.

The only structural anomaly left manuscript-wide is the ch71 `\tag{}` gap
71.33–71.35, which is the author's work in progress and is left alone.
