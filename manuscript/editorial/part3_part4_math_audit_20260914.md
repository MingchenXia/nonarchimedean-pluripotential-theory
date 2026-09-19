# Mathematical audit of Parts 3 and 4 (ch20–ch50)

Date: 2026-09-14.  Status: **closed**.  All items below were re-derived by hand
before any edit was made; the last section records findings that were reported
and **rejected**.

Verification available: `/tmp/lint.py` (environment balance, brace delta,
`\[`/`\]` and `\(`/`\)` balance, `\tag{NN.M}` sequence, duplicate labels) and
`/tmp/refs.py` (every `\Cref`/`\cref`/`\eqref` target resolves).  Both run clean
on every file touched; manual `\tag` sequences were preserved exactly
(ch38 1–47, ch39 1–55, ch40 1–29, ch41 1–47, ch42 1–10, ch44 1–32, ch46 1–28,
ch47 1–27, ch48 1–15, ch49 1–35, ch50 1–90).  **Nothing is compile-verified**;
the VM TeX installation lacks `newtx` and has no network.

---

## Part 3 (ch20–ch31)

### ch20 — `rem:ch20-multiplicities-lengths`, new identity `eq:ch20-curve-laplacian-general`
`eq:ch20-curve-laplacian-graph` was stated only for semistable models, and the
remark said the identification "carries the normalization".  It survives in
general: with the canonical edge length `1/(b_i b_j)` at a node of `E_i ∩ E_j`,
summing outgoing slopes at `x_{E_i}` gives
`Σ_j b_i b_j (E_i·E_j)(u_j−u_i) = b_i (D·E_i)`, so
`Δ_{Δ_X} φ_D = Σ_i b_i (D·E_i) δ_{x_{E_i}}` — the **model measure**, not
`Σ_i (D·E_i)δ`.  Checked on the blown-up conic: `b_{1/2}=2`, edge length `1/2`,
and `Δ|s−1/2|({1/2}) = 2`, matching `eq:ch21-conic-max-measure`.

### ch21 — semistable models are not cofinal
`prop:ch21-curve-criterion` quantified over semistable models `C' ≥ C` and its
proof asserted "semistable models are cofinal because SNC models are and an SNC
model of a curve is semistable after a further blowup".  **False**: a blowup can
only raise multiplicities.  `ex:ch21-conic-numbers` itself produces a
multiplicity-2 component `E_{1/2}` by blowing up the node; blowing up a closed
point of `E_{1/2}` gives `E'` with `b_{E'}=2`, whose divisorial point lies on no
semistable skeleton (a vertex of a semistable skeleton is divisorial with
`b=1`, and a branch point of a skeleton is a vertex).  Removing the obstruction
needs a ramified base extension, which is not available.
Applied: the quantifier is now over **SNC** models, with `Γ'` carrying its
canonical metric; the relative-degree identification acquires the harmless
factor `b_E>0`; new `rem:ch21-semistable-not-cofinal` records the failure.
`prop:ch21-curve-retraction` was likewise restated for SNC models — its Step 1
already carried the `b_E` weight, and Steps 2–3 are pure metric-graph arguments,
so nothing else changed.  The false companion claim at ch21:2453 ("every type-2
or type-3 point lies on the skeleton of some semistable model") was corrected.

### ch23 — `ex:ch23-globally-generated`, sign of the exceptional divisor
`L_1 := π^*O(1) − E_1` was to exhibit a **vertical base locus**; it exhibits
none.  Direct computation: the sections of `mL_1` are the sections of `mO(1)`
vanishing to order `m` at `ξ`, namely `Z^i W^{m−i} π^{m−i}`, and their weight
relative to the standard metric is `max{ψ,−1} = ψ_1`, which is exactly the model
metric of `L_1`; so `mL_1` is globally generated and `a_m = O`.
With `L_1 := π^*O(1) + E_1` everything the example claims is true:
`π_*O(mE_1) = O`, so `H^0(X_1,mL_1) = H^0(P^1_R,mO(1))` and every section
vanishes to order `m` along `E_1` inside `mL_1`; hence `a_m = I_{E_1}^m`,
`φ_m = −φ_{E_1} = max{ψ,−1} = ψ_1` for every `m`, with `φ_m(e_1) = −1` as the
text says; `deg(L_1|_{E_1}) = −1 < 0`, so `0` is not `θ`-psh, and the largest
`θ`-psh `u ≤ 0` is `−φ_{E_1} = ψ_1` (a psh function for the standard form is
convex, hence nonincreasing, along the infinite branch through `e_1`).
Applied, with the degree computation and the envelope argument written out.

### ch24 — three items
1. `cor:ch24-model-uniqueness-curve`: "Multiplying by `f(x_E)` and summing"
   cannot symmetrize `b_F(E·F)`.  The equation at `E` must be multiplied by
   `b_E f(x_E)`; then `Σ_{E≠F} w_{EF} f_E(f_F−f_E) = −Σ_{E<F} w_{EF}(f_E−f_F)^2`
   with the symmetric `w_{EF} = b_E b_F (E·F)`.  Applied.
2. ch24:1236 and ch24:3218 asserted that `ex:ch22-countable-blind-spot`
   produces a `θ`-psh function that **no countable family of model functions
   approximates from above**.  That example produces a function not separated by
   countably many *dual complexes*; ch22's own warning after it says so, and
   `cor:psh-sequential-regularization` (ch25) proves that every `θ`-psh function
   *is* the pointwise decreasing limit of a **sequence** of psh model functions.
   The real reason ch24 uses nets is **circularity**: that corollary is proved in
   ch25 out of capacity theory, which rests on the operator built in ch24.  Both
   passages rewritten accordingly.

### ch26 — two items
1. `thm:ch26-e1-comparison` proof: as `ε↓0` the sets `{φ ≤ ψ−ε}` **increase**;
   the text said they decrease to `⋂_{ε>0}{φ≤ψ−ε}` while correctly identifying
   the limit as `{φ<ψ} ∪ {φ=ψ=−∞}`, which is the **union**.  Corrected, with
   continuity from below on both sides.
2. `ex:ch26-two-vertex-energy`: the admissible region is
   `−m_0 ≤ b−a ≤ m_1`, not `|a−b| ≤ min{m_0,m_1}` — the two agree only when
   `m_0=m_1`.  `ex:two-vertex-ma` (ch24) and `eq:ch31-two-component-window`
   (ch31) already have it right.  Corrected.

### ch28 — two items
1. The domain paragraph justified finiteness of `∫φ dμ` for `μ ∈ M^1_V` by
   "`eq:measure-fenchel-energy` once `prop:ch28-test-class` is available".
   `eq:measure-fenchel-energy` is stated for **model** functions, and clause (4)
   of `prop:ch28-test-class` restricts to the `φ` for which the integral is
   already finite.  The book does have a correct argument, in
   `rem:ch28-two-energies` (truncations `max{φ,−j}` against clause (3)); the
   paragraph now cites it.
2. `eq:maximizing-uniform-differentiability` was stated as an upper bound on
   `Ẽ_ω(φ_j+tf)`.  The next display is a second upper bound on the same
   quantity, and the two cannot be combined.  The estimate is two-sided;
   restated with absolute values, with a note that only the lower bound is used.

### ch29 — `thm:bfj-supported-regularity`, Step 0
"each `φ_j` is a continuous function with `−‖φ_{j_0}‖_∞ ≤ φ_j ≤ 0`" is false:
the net **decreases**, so `φ_{j_0}` bounds it above, not below, and `φ ∈ E^1`
need not be bounded below.  Replaced by `φ ≤ φ_j ≤ 0`, with a note that no
lower bound is available or used.

### ch31 — `lem:ch31-curve-ma-affine`
The lemma said `MA_ω(u) = μ_0 + Δ_Γ u` for every model function `u` determined
on a model **dominating** `X`, with `Γ = Sk(X)`.  False: a blowup at a smooth
point of `X_s` attaches a new edge to `Γ` rather than subdividing one, and a `u`
supported on that edge has `Δ_Γ u = 0`.  `ex:ch31-p1-blowup` in the same chapter
is exactly that configuration and computes the right answer, `δ_{x_E}`, on the
**larger** skeleton.  Applied: the Laplacian is now taken on `Γ_u = Sk(X_u)`,
with the observation (proved in the proof) that `μ_0` is unchanged on a
dominating model, since contracted components carry degree `0` and all
multiplicities are `1`.  All fourteen downstream uses have `Γ_u = Γ` and are
unaffected.

---

## Part 4 (ch32–ch50)

### ch32
* `ex:ch32-normal-cone-valuation`: `f ↦ max{m : f ∈ b^{(m)}}` is **not a
  valuation** — for `b=(x^2,y^3)` it returns `0` at `x` and `1` at `x^2`.  It
  computes `⌊v_P(f)⌋`, and only when `b` has a single Rees valuation; the
  correct object is `v_P = b_P^{-1} ord_P`, `b_P = ord_P(ϖ)`, with
  `v_P(x)=1/2`, `v_P(y)=1/3` in that example.  "The exceptional divisor of the
  normalized blowup" also presumes uniqueness (`b = m_p ∩ m_q` has two).
* `rem:ch32-specialization`: "the support stays put" is false.  `v ≥ w` forces
  `s(v) ⊆ s(w)` (test on `I_{s(w)}`), and `v_{p,triv} ≥ ord_p` with
  `s(ord_p)=P^1 ⊋ {p}`.  Corrected, and tied to `eq:trivial-endpoints`.
* Polar locus of `φ_a`: "contained in the proper-support locus whenever `a≠0`"
  fails for the reducible `X` the chapter's own conventions allow — take
  `X = V(x_0x_1)` and `a = I_{X_1}`.  Hypothesis strengthened to "nonzero at
  every generic point of `X`".
* `thm:ch32-a1-classification`: the substitution `r = e^{-t}` is inconsistent on
  the `r>1` branch, where `v_{∞,t} = −t·deg` forces `r = e^{t}`.  Both branches
  now stated explicitly.

### ch33
`thm:ch33-flag-tc-equivalence`(1): the chain `σ(v)(a) = σ(v)(aO) = σ(v)(O(−D))`
has a sign error — `aO = O(D)`.  Unit test `a = (ϖ)`: `D = −X_0`,
`σ(v)(O(D)) = 1`, `φ_a = −1 = φ_{−X_0}`, whereas `O(−D)` would give `+1`.
Corrected, with the unit test written into the proof.

### ch34
* `prop:ch34-pl-operations`, max clause: the perturbing class
  `(c_1(L))_X + D + ε(L − (c_1(L))_X)` has horizontal class `c_1(L)`, not
  `(1+ε)c_1(L)`, and need not be relatively nef.  On `Y = Bl_{(p,0)}(P^1×A^1)`
  with `deg θ = 1+δ`, `D = −E`, `L = (c_1(L))_Y − ½E`, it has degree
  `δ − ε/2 < 0` on `P̃` for `ε > 2δ`.  Replaced by
  `((c_1(L))_X + D) + εL`, relatively ample as nef + ample, horizontal class
  `(1+ε)c_1(L)`, function `φ + εφ_L` — everything downstream unchanged.
* `ex:ch34-psh-check`: with `d=1`, `c=−1` only the **left** inequality of
  `−d ≤ c ≤ 0` is an equality.

### ch36
`prop:ch36-no-sequences` needs `k` **uncountable**: over `k = Q̄` the closed
points of a curve are countable, `X^div` is countable (divisorial points are
`t·ord_E` with `t ∈ Q_{>0}`), and the proposition is false.  The chapter's own
`warn:sequence-insufficient-envelope` already carries the qualifier.

### ch37
"bounded above by a constant cannot be weakened to a pointwise bound, as
`ex:ch37-pointwise-not-uniform` shows" is doubly wrong.  (a) That family is
bounded above at **no** point: `ψ_j ≥ j` off the ray.  (b) For families inside
`PSH_X(θ)` the pointwise and uniform conditions **coincide**, because
`sup_{X^An} φ = φ(v_triv)` — true for FS functions by
`prop:ch34-generic-finiteness`(3) and inherited by decreasing limits.  New
`rem:ch37-pointwise-equals-uniform` records the equivalence with its one-line
proof; the example is retained as a witness that boundedness cannot be dropped.

### ch38 — four items
* PSH2 is `thm:bj-basic-closure`**(5)** (varying classes), not (4); (4) is its
  fixed-class case, as ch34's proof says verbatim.
* `warn:ch38-drift-not-absorbed` asserted "There is no clause allowing the class
  to move to a limit".  Clause (5) is exactly that clause.  Rewritten: what (5)
  does not supply is generic finiteness of the drifting limit, which is the
  whole difficulty.
* The summary described the approximating coefficient b-divisors as
  "increasing"; `cor:ch38-gf-regularization-bdivisor`(3) says the net `(C_a)`
  **decreases** (the effective `−C_a` increase).
* `prop:ch38-evaluation-domains`(3): the upper-semicontinuous extension is
  **not** unique — on `P^1` with `B = −p̄`, lowering the value at `v_{p,triv}`
  to `−5` keeps upper semicontinuity (every neighbourhood
  `{v(m_p)>t}` carries values `≤ −t`).  The **continuous** extension is unique,
  and `v ↦ v(b)` is continuous into `[0,+∞]` by
  `thm:ch32-ideals-generate`(continuous).  Statement and proof corrected.
* `ex:ch38-...` (curve): "the hypothesis cannot be weakened to
  pseudoeffectivity, since on a curve pseudoeffective and nef coincide" — the
  stated reason is precisely why the example cannot separate the two.  Retracted.

### ch39
`ex:ch39-grid-correction-needed`: the grid maximum is **constant** in `n`.  The
family `q_λ = max{0,1+λ}log|m_p|` is affine in `λ` on the window `[−1,0]`, and
every `Γ_n` contains both endpoints, so
`G_n ≡ max{−s,−1} = u` for all `n` and the grid error is zero.  The example was
claiming a strict increase.  Rewritten: it now shows that the correction costs
nothing, and that a strict increase needs strict concavity in `λ`.

### ch40 — four items
* `warn:ch40-firewall`(4) said `P_L(φ_D)` is "the raw supremum"; (40.1) defines
  it with the usc star, as `warn:ch40-two-envelopes` says.  Corrected.
* `ex:ch40-smooth-parameter`: only the **left** inequality of
  `Q ≤ u_m ≤ 0` is an equality (`u_m = Q = log|(x)|`); the right one is strict
  wherever `x` is not a unit.
* The standing enlargement demanded `c_1(A)` **ample**, contradicting
  `ex:ch40-p2-engines` and `ex:ch40-drift-real`(a), where `A = O_X` on `P^n`
  with `d = n+1`.  `lem:ch40-drift-nef-monotone` needs only **nef**; weakened.
* "for `L` big but not semiample, `H^0(X,mL)=0` for infinitely many `m`" is
  false: Kodaira's lemma gives `h^0(mL) > 0` for all `m ≫ 0`.  Replaced by the
  accurate statement that only finitely many indices are excluded.

### ch41 / ch42 — descent bookkeeping
* ch42: "the separable degree counts the sheets visible as distinct points of a
  fibre, while the inseparable degree is absorbed into the weights `e(w/z)`" is
  false in both halves.  `ex:ch42-endtoend`, in characteristic `≠ 2`, has
  `d_s = 2`, `d_i = 1`, one point over `v_P`, and weight `e = 2` (tame).
  Replaced by a pointer to `rem:ch41-weight-anatomy`: each weight collects Artin
  length, ramification of any kind, and residue degree; only
  `Σ_{w|z} e(w/z) = d` survives.
* ch42 `rem:ch42-normal-middle` had source and target interchanged twice.
  `B^G = A` is normality of the **target** (`X = S/G`, ch41 Step 1);
  `lem:bj-canonical-carrier` is applied on the **source** (`Y`, ch39 line 3030).
  `ex:ch41-node-not-open` — normal source, non-normal target, non-open
  analytification — is the reminder.
* ch41: `Cl(X) ≅ Z/2` for `X = P(1,1,2)` is wrong; `Cl(X) = Z·O_X(1)` and
  `Pic(X) = Z·H` (ch42:1992).  `ex:ch41-nonflat-cone` computes `Cl(R) ≅ Z/2` for
  the affine cone, i.e. the local class group at the vertex.
* ch41 `lem:ch41-projection-formula`: the proof says `q_*[W] = d[Z]` "is where
  constancy of the rank is used" and then, in the same sentence, that it "would
  still be `d[Z]`".  The identity holds for any proper surjective generically
  finite `q`; it is used for the **non-flat** `h` in `lem:ch42-class-ledger`.
  Constancy of the rank is needed for the divisor identity, not for this.
* ch41 `rem:ch41-weight-anatomy`: `ex:ch41-frobenius-average` has `e = p`,
  `f = 1` at divisorial points (the value group is divided by `p`, the residue
  field does not grow), so the weight is purely inseparable **ramification**, not
  a residue extension.
* ch41 firewall: two suprema over arbitrary families occur (Step 0's pullback of
  the given family, and the canonical carrier), not one; and the firewall needed
  the same `thm:bj-smooth-envelope` exception that ch42's firewall carries, since
  `ex:ch41-descent-cone` uses it.

### ch43 / ch44
* ch43: "the pullbacks of rational classes from `C` are exactly the multiples of
  `3`, whereas `d_i ∉ 3Q`" — `3Q = Q`.  Moreover `ν^*: Pic(C) → Pic(P^1)` is
  **surjective** for the cuspidal cubic, as the chapter states 300 lines earlier.
  Rewritten: the net is *presented* without pullbacks, existence does hold here,
  and the genuine obstruction is nonsurjectivity for general nonnormal `X`.
* ch43: `ε_i := i^{-1/2}` is irrational, violating the rationality hypothesis of
  `lem:bj-normalization-class-promotion` and making `r_i(3ε_i + 1/i) ∈ Z`
  impossible.  Replaced by `ε_i := 1/⌈√i⌉`, for which `1/i = o(ε_i)`.
* ch43: the singular locus `{P} × P^1` of `C × P^1` meets **both** `V_1` and
  `V_2`, so two of the four charts are non-isomorphisms, not one.  (`q = p`,
  `e_min = 1` unchanged.)
* ch43: "That would be fatal" overstates.  With a stage-dependent exponent the
  descended functions are still correct pointwise and the class is still `L_i`
  (the denominator being `q_i m_i`), so the net survives; what is lost is a
  single presentation discipline, and `q_i → ∞`.  Softened at both places.
* ch44: the monotonized classes were evaluated one index late.  The factor is
  `(3n_j+8)/(3n_j+6)`: `(3/4)(44/42) = 11/14` at `n_2 = 12` and
  `(7/8)(92/90) = 161/180` at `n_3 = 28`, not `5/6` and `11/12`.  The recursion
  was also reindexed so that it produces `n_1,n_2,n_3 = 4,12,28`.
* ch44: `s_1 = b^2(a+b)` vanishes doubly on `R_{[1:0]} = {b=0}`, not on
  `R_{[0:1]} = {a=0}` — consistent with the `v_ℓ(s_1) = 0` computed three lines
  earlier.
* ch44: `G_{n+1} = (1+t)^n(1−nt)` does not arise in the `f_1 = t` presentation
  (there `g_1 = t^3`, `g_2 = u(2+t)^3`, and the `u`-degree-zero part of
  `a_{n+1}` is `z_1^{n+1}t^{3(n+1)}`).  The reference now points at the
  phenomenon in `ex:ch44-splitting-fails` rather than at the literal polynomial.

### ch46 — five items
* `ex:ch46-trivial-metric`: `(Σc_i)(θ_0⋯θ_n)` is an `(n+1)`-fold product on an
  `n`-fold, hence `0` by `eq:bj-trivial-energy-zero`, while the left side is not.
  Should be `(Σc_i)(θ^n)`.  Check on `P^1`: `(ω,c)^2 = 2c`.
* `thm:bj-e1-basic`, elementary case: the inequality runs the other way.  With
  `ω = O(1)`, `ω' = O(2)`, `φ ≡ −1` on `P^1`: `(ω,φ)^2 = −2`,
  `(ω',φ)^2 = −4`.  Each cross term is `∫φ` against a positive mixed measure,
  hence `≤ 0` for `φ ≤ 0`; the spurious "times `−1`" is removed.  Corrected,
  with a note that the bound therefore does **not** give `E^1(ω) ⊆ E^1(ω')`.
* `ex:ch46-e1-curve`: the Monge–Ampère measure was missing the endpoint atom
  `(−h'(+∞))δ_{v_{p,triv}}`.  Without it the stated mass identity assumes
  `h'(∞) = 0`, and for `h = −t` the displayed measure is `0` while the true one
  is `δ_{v_{p,triv}}`; the energy chain `½∫hh'' = −½∫|h'|^2` then reads
  `0 = −∞`.  Restored, with `E = ½(∫hh'' − h'(∞)h(∞)) = −½∫|h'|^2` valid in
  `[−∞,0]`.  This is exactly the error `ex:ch46-homogeneous-mass-escapes` warns
  against.
* `rem:ch46-vector-space`: "finite on `X^val` only if it is a generically finite
  Fubini–Study function" is false — `h(t) = −log(1+t)` in `ex:ch46-e1-curve` is
  finite on `X^val` and not piecewise affine.  The cited item characterizes
  finiteness *for functions already given by an FS presentation*.
* `rem:ch46-mass-location`: a **bounded** truncation has empty polar set, so it
  cannot have "the same polar set".  Replaced by the genuine finite-energy
  witness `h(t) = −log(1+t)`, with `E_ω = −½` and a pole at `v_{p,triv}`.

### ch47 — three items
* `imp:ch47-imported`: the quasi-triangle inequality is used inside a proof —
  the energy bound along an `I`-Cauchy net in
  `thm:bj-cy-envelope-equivalence` — contrary to "never inside a proof".
* `ex:ch47-explicit-potential`: the truncated potentials **decrease** to
  `φ_α`, not increase.  Deleting tail mass `α/(1+R)` and renormalizing
  multiplies `μ^u([0,t])` by `(1−ε)^{-1} > 1`, so `h_R' ≥ h_α'` with
  `h_R(0)=0`, hence `φ_R ≥ φ_α`; and `ε` decreases in `R`.  With `d=α=1`,
  `h_R'(t) = (t/R−1)/(1+t)` and `E(φ_R) = −½(3−4log2) ≈ −0.114` at `R=1`,
  `≈ −0.463` at `R=100`, decreasing to `−½`.  `cor:ch47-monotone-I` then
  applies with `(φ,ψ) = (φ_α,φ_R)`.
* `prop:ch47-skeletal-admissible`: the last assertion quoted a **global**
  Lipschitz constant for `Δ_X ↪ (X^lin, d_∞)` that `rem:ch49-dual-complex-
  lipschitz` explicitly declines to supply (`itm:ch49-dc:lipschitz` has constant
  `C_X/c` on the part of each face at distance `≥ c` from the coordinate
  hyperplanes, degenerating as `c ↓ 0`).  Restated for the truncated complexes
  `Δ_X^{(c)}`, with new `warn:ch47-skeletal-boundary` recording what the full
  statement would need.

### ch48 — two items
* `rem:ch48-criterion-sharp`: on `P^1`, `n = 1`, so the integrand of the
  criterion is `t·Capa`; decay `t^{-2}` gives the divergent `∫t^{-1}dt`.  The
  example actually cited decays like `s^{-4}`.  Corrected, with the general rate
  `t^{-(n+1)}`.
* `thm:bj-strong-measures`, compactness half: the bound on `E^∨(μ_i)` was
  justified by `prop:ch47-test-class`, which reintroduces `E^∨(μ_i)` and the
  uncontrolled `J(φ_i)` on the right, and gives finiteness for each `i` rather
  than uniformity in `i`.  The step is now stated as importing that uniform
  bound from [BJ22, Thm 10.14], with the display made explicit.

### ch49
`rem:ch49-minkowski-check`: the two extremal cases are interchanged.  A cone's
cross-sectional measure at relative height `s` above the apex is `∝ s^{n−1}`, so
the centroid sits at `n/(n+1)` **above the apex**; apex at `h` gives the
right-hand case, apex at `H` the left.  The remark's own simplex examples confirm
it: `u = (1,…,1)` has apex `0` at `h = 0` and `⟨u,b_P⟩ = n/(n+1)`.

### ch50 — four items
* `cor:ch50-vanishing`: the chain `‖χ‖_1 ≤ ‖χ‖_p ≤ ‖χ‖_∞ ≤ 2J` is false at the
  last step — the norms are **centred**, and `(50.34)` is only the `p = 1`
  statement.  On `ex:ch50-p1-dnc` with `c = 1/5`, `L = O(2)`: `λ̄ = −0.01`,
  `λ_min = −0.2`, `J = 0.01`, `‖χ‖_∞ = 0.19 > 0.02`.  The corollary survives:
  a centred `L^1` norm vanishes iff the measure is the Dirac at its mean.
* `ex:ch50-nonhomogeneous` is **not a norm**: superadditivity fails at
  `s = s' = x`, `m = m' = 1`, where `χ_2(x^2) = 1 < 2`.  Replaced by
  `χ_m(x^ay^{m−a}) = ⌊a/2⌋`, extended by minima: superadditive by
  `⌊(a+a')/2⌋ ≥ ⌊a/2⌋+⌊a'/2⌋`, with `χ^hom_m = a/2`, gap exactly `½` at odd
  `a`, and `d_1(χ,χ^hom) = 0`.
* `thm:ch50-J-L1`, Step 1: `eq:ch50-concave-upper` is derived for `s ≥ A` and
  then integrated over `[0,s_0] ⊇ [0,A]`, where concavity with `v(0) ≥ 0` forces
  the **opposite** inequality (witness `v(s) = (1+s)/2`, `n=1`: `A = 1/4`,
  `γ = 5/8`, `s_0 = 2/5`, and `v(0.1) = 0.55 > 0.25 = γs/A`).  Replaced by a
  correct convex-duality argument: with `ψ = v^{-1}`, `A = n∫_{v_0}^1 w^{n−1}ψ`,
  `m = 1−v_0^n`, `q = n(1−v_0^{n+1})/(n+1)`, and `p` a subgradient at `γ`, the
  two convexity inequalities give `Av_0^n ≥ p(q−γm)` and `A ≤ p(γ−v_0)`, whence
  `γ ≥ q + v_0^{n+1} = n/(n+1) + v_0^{n+1}/(n+1)` (or `γ ≥ q/m ≥ n/(n+1)` in the
  other case).  Sharp in both regimes: `v(s)=s` gives `γ = n/(n+1)`, and
  `v(s)=(1+s)/2` gives `γ = 5/8 = q + v_0^2` exactly.
* `Imported deep step`: the direction was inverted.  `D ≥ δJ ⟹ M ≥ δJ` is
  immediate from the already-proved `D ≤ M`; the deep, imported direction is
  `M ≥ δJ ⟹ D ≥ δJ`.  The dated scope table was corrected to match.

---

## Reported and rejected

* **ch50 `+X_0` in the anticanonical identification** (claimed spurious).
  Rejected.  The chapter defines `K^log = K + B_X + X_{0,red}` relative to
  `A^1` (ch50:3175), so `−K^log_{X/A^1} + X_0 = −K_{X/A^1} − X_0 + X_0
  = μ^*pr_1^*O(2) − E = L_1`.  The display is correct as written; the report
  assumed `K^log = K`.
* **ch33 `C_+ = 1` / `C_+ = 1/4` not satisfying the linear-boundedness
  definition** and **ch33 `cor:ch33-dh-structure`(2) over-read at `n=2`**.
  Left alone: the first is an attained-versus-strict boundary reading of the
  definition, the second a wording matter, and neither is a false statement.
* **ch46 `E^1(ω) ⊆ E^1(ω')` itself.**  The statement of `thm:bj-e1-basic` is not
  in question; only its "elementary case" motivation was, and that has been
  repaired without touching the theorem.

## Left for editorial decision

* **ch47 `prop:ch47-skeletal-admissible` downstream.**  `cor:bj-cy-unibranch`
  and `ex:ch47-explicit-potential` quote it for "a measure carried by a dual
  complex".  `warn:ch47-skeletal-boundary` now flags the gap, but the author
  should decide whether to prove the boundary-Lipschitz statement (true in every
  case computed in ch49, including the toric one) or to carry the truncation
  through those statements.
* **ch48 `thm:bj-strong-measures`.**  The uniform pairing bound is now declared
  imported; if a self-contained argument is wanted, it will need an input beyond
  `prop:ch47-test-class`.
* **ch43 `cor:ch43-frobenius-all-affines`.**  Now described as buying
  presentation discipline rather than as load-bearing.  If the author disagrees,
  the corrected passages name exactly what would have to be re-argued.
