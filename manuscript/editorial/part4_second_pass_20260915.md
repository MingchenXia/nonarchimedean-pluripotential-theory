# Second adversarial pass — Part 4 (ch31–ch50)

Date: 2026-09-15
Chapters: ch31 (in part3), ch32–ch50.

Every chapter here had already had a first pass whose findings were applied,
so the easy errors were gone before this started. Four parallel reviews were
run with the first-pass findings listed as off-limits. Each item below was
re-derived by hand before being applied; the ones that could not be settled
are in §E, unapplied.

**ch33, ch36, ch37, ch46, ch47, ch49 came back clean.** So did ch42 apart from
a step mislabel. That is six chapters with no mathematical finding.

---

## A. Errors in computed mathematics

### A.1 ch31 `ex:ch31-p1-blowup` — the wrong degenerate case is named

The text says to check `eq:two-component-energy` "with `m_0=1, m_1=0`". That
equation reads `E = −m_0m_1 − ½m_1²`, which at `(1,0)` returns **0**, not the
`−½` computed two lines above. The mass here sits at the endpoint carrying no
degree, so the matching labelling is `x_0 = x_E` (`m_0 = 0`), `x_1 = x_G`
(`m_1 = 1`): then `(a,b) = (−1,0) = (−m_1,0)` and `E = −0·1 − ½·1² = −½`.
Corrected, with both degenerate cases named so the reader can tell them apart.

### A.2 ch34 `ex:ch34-two-corner` — a spurious factor of 2

"the two integral affine structures differ by a factor 2 in the lattice
length". They do not: the two edges carry multiplicities `(1,2)` and `(2,1)`,
symmetric, so each has lattice length `1/lcm(1,2) = ½`, and the two sum to the
lattice length 1 of `Δ_Y`. The book verifies this same `b = (1,2,1)`
configuration in ch05 and concludes there that the structures agree.
Corrected, noting that `b_G = 2` is exactly what keeps the structure unchanged.

### A.3 ch48 `ex:ch48-p1-capacity` — the equality regime is wrong

`Capa(A_2(t)) = min{1, 2/t}` and the sum of the two point capacities is
`2 min{1, 1/t}`. These agree only for `t ≥ 2`: at `t = 1` the left side is 1
and the right side is 2. The text placed the whole of `t ≥ 1` in the equality
regime. Corrected to three regimes, with the loss `2/t − 1` on `1 ≤ t < 2`.

### A.4 ch50 `thm:ch50-J-L1` — a limit taken in the wrong direction

For `μ_ε = (1−ε)δ_{−ℓ} + εδ_0` one computes `λ̄ = −(1−ε)ℓ`, `A = (1−ε)ℓ` and
`‖μ_ε‖₁ = 2ε(1−ε)ℓ`, so `‖μ_ε‖₁/A = 2ε`. That tends to 2 as `ε → 1⁻`, when
almost all mass sits at the top atom — not as `ε → 0`, where it tends to 0.
As written the sentence offered a family whose ratio tends to 0 as evidence
that the constant 2 is approached.

### A.5 ch31 — three counting and bookkeeping slips

The "Numbers to remember" table gives 12 outright equalities and 3 one-way
implications; the census four pages earlier says 11 and 4, and I recounted the
three tables to confirm 11/4/5/7/2 summing to 29. (Both versions sum to 29,
which is how the slip survived.) The mass ledger says "Twenty rows"; the three
tables carry 8 + 7 + 6 = **21** data rows. And `ex:ch31-chain-lebesgue` lists
interpolation nodes at spacing `1/N` while quoting the error `3/(4N²)`, which
is `(1/12)(3/N)²` — the node list should be `0, 3/N, 6/N, …, 3`. Also
`prop:graph-ma-solution` wrote `(μ−ω)(Γ) = 0` where `ω` is a closed model
form, not a measure; the mass computation is for `μ − μ_0`.

### A.6 ch30 (carried from the ch41–ch44 review) — `ex:ch42-endtoend` step number

The flattening square is chosen in **Step 1** of
`thm:bj-finite-normal-descent`; Step 2 descends a homogeneous carrier, which
the example explicitly does not illustrate. The neighbouring sentences
correctly say Step 0 and Step 3.

### A.7 ch44 `sec:ch44-monotonization` — a prohibited product

The recipe `a_j := 1 − 2^{−j}` gives `a_0 = 0`, and where `ψ_0 = −∞` the
sandwich forces `F_{n_0} = −∞`, so the first term is `0·(−∞)` — exactly the
product `thm:bj-basic-closure`(3) prohibits. The worked example already starts
at `j = 1`. Index restricted.

---

## B. A false claim in a proposition

### ch35 `prop:ch35-curve-classification` — "all but finitely many zero"

The classification asserts that a homogeneous psh function on a curve has
`c_r > 0` for only finitely many closed points `r`, and that the corresponding
`B = −Σ_r c_r r̄` is a Cartier b-divisor. Only **countability** follows from
`Σ c_r ≤ deg θ`, and the finiteness claim is false.

Counterexample, verified in full. On `X = P¹` with `θ = c_1(O(1))`, pick
distinct closed points `r_1, r_2, …` and set `c_n = 2^{−n}`. Put

    ψ_N := Σ_{n≤N} 2^{−n} log|m_{r_n}| = 2^{−N} log|b_N|,
    b_N  := Π_{n≤N} m_{r_n}^{2^{N−n}},   deg b_N = 2^N − 1.

Then `deg(O(2^N) ⊗ b_N) = 2^N − (2^N − 1) = 1`, and a degree-1 line bundle on
`P¹` is globally generated, so `ψ_N ∈ H^gf_Q(O(1))`. The `ψ_N` decrease
(each increment is `2^{−(N+1)} log|m| ≤ 0`), the class is constant, the limit
has `ψ(v_triv) = 0` finite, `ψ(s·ord_{r_k}) = −2^{−k}s`, and
`Σ c_n = 1 = deg θ`. So `ψ ∈ PSH_hom,X(θ)` with infinitely many nonzero
slopes.

Such a `ψ` is not the coefficient function of any b-divisor: local finiteness
on the single model `X` is exactly the finiteness condition. So on a curve
`PSH_hom,X(θ)` is **strictly larger** than the set of b-divisor coefficient
functions. The proof's own justification was circular — "Finiteness … follows
because ψ must be the coefficient function of a divisor, or directly because
local finiteness on the single model X requires finiteness" — local finiteness
being the thing asserted. Corrected, with the counterexample recorded in place.

---

## C. Proofs whose cited authority does not supply the step

### C.1 ch43 `thm:bj-positive-universal-reflection` — the regularization

The proof routes the passage from real to rational Fubini–Study weights
through `cor:ch41-real-weights`. That corollary extends the determinant-norm
averaging `Av_q` to weights in an arbitrary additive subgroup — the *real*-weight
direction — and says nothing about approximating an `H^gf_R` function by
`H^gf_Q` ones. The sketched substitute (perturb each weight upward to a nearby
rational) is also not proved and not obviously monotone.

Worse, the citation contradicts the chapter's own dependency declaration:
"Nothing from the averaging machinery of that chapter is used." `cor:ch41-real-weights`
is a corollary of exactly that machinery.

The step is free: `thm:ch34-fs-regularization` states verbatim that for
`φ ∈ PSH_X(θ)` there are `Q`-line bundles `L_i` and a decreasing net
`φ_i ∈ H^gf_Q(L_i)` with `c_1(L_i) → θ`. Re-pointed; the dependency
declaration is now true.

### C.2 ch43 `cor:ch43-reflection-structure` — normalization applied off its class

The identity of suprema was justified by `prop:ch35-homogeneous-normalization`
"applied on each side". That proposition is stated for **homogeneous** psh
functions and concludes `ψ(v_triv) = 0`; applied to a general `θ`-psh `φ` it
would assert `φ(v_triv) = 0`, false for `φ +` constant. The correct input is
`prop:ch32-maximum-principle`(sup), psh functions being decreasing.

### C.3 ch34 `lem:ch34-log-s-properties`(4) — comparable semivaluations

"Two comparable semivaluations have the same center by `eq:trivial-endpoints`."
False: on `P¹`, `v_{X,triv} ≤ ord_p` have centres `η` and `p`. The right input
is `thm:ch32-order-centers`: `v ≤ w` puts `c(w)` in the closure of `{c(v)}`, so
`c(v)` is a generization of `c(w)` and every trivializing neighbourhood of
`c(w)` contains `c(v)`. The conclusion was correct; the reason was not.

### C.4 ch32 `cor:ch32-determination-divisorial`(usc) — hypothesis on the wrong function

The repair offered is "`ψ` being the usc regularization of its restriction to a
dense set". The counterexample supplied three lines later satisfies it: there
`ψ ≡ 0`, and since `X^divis` is dense, `ψ` *is* its own usc regularization from
that set, yet `φ(v_0) = 1 > 0`. The hypothesis belongs on the smaller function:
if `φ = (φ|_D)^*` for a dense `D` and `ψ` is usc then
`φ(v) = limsup_{D∋w→v} φ(w) ≤ limsup ψ ≤ ψ(v)`. That is also the form used
downstream.

---

## D. Missing hypotheses, and claims stronger than what was proved

### D.1 ch38 `lem:ch38-activation` — nefness of the total class

Items (vi) and (vii) assert that `P = π*θ + B_Y` is nef and that `−D'` is
`π`-nef. Neither follows from the stated hypotheses: take `X = P²`, `π = id`,
`B = 0`, `θ = −c_1(O(1))`; every hypothesis holds and `P` is not nef. Step 5
of the proof says "because `P` is nef", and ch39's `lem:ch39-fixed-pole` treats
it as a hypothesis, noting it must check that items (i)–(v) hold "without the
nefness of the total class — a hypothesis which is not available to us". Only
the statement omitted it. Added to items (vi)–(vii) alone, so ch39 may still
quote (i)–(v) unconditionally.

### D.2 ch32 `prop:ch32-nodal-curve` — anticontinuity used backwards

`{v : c(v) ∉ Sing X} = c^{-1}(X∖Sing X)` is called **open**; the centre map is
anticontinuous, so the preimage of an open set is **closed** (indeed compact).
The same sentence then calls it the complement of the rays `c^{-1}(p)`, which
the chapter has just shown to be open — so it contradicted itself. Conspicuous
because anticontinuity of `c` is one of the chapter's main points.

### D.3 ch39 — a stale description of `thm:bj-basic-closure`

ch39 says that theorem "is stated for nef classes" and that its clauses need
the "nefness hypothesis standing in that theorem" discharged. It opens: "Let
`θ, θ' ∈ N¹(X)` be **arbitrary** numerical classes. No positivity hypothesis
is needed." There is nothing to discharge. As written it told the reader that
a theorem they are about to use is weaker than it is. What ch39 genuinely adds
is clause (5), monotonicity of `PSH_X(θ)` in `θ`; the prose now says so.

### D.4 ch39 `cor:ch39-nef-reflection` — a curve with no strict transform

"`θ·C = β*θ·C̃` for every integral curve `C ⊂ X` with strict transform `C̃`".
For `β` proper birational with `X` normal, `β(Exc β)` has codimension ≥ 2, but
as soon as `dim X ≥ 3` it can contain integral curves — `Bl_ℓ P³` with `C = ℓ`
— and such a curve has no strict transform. The needed direction is already
proved for arbitrary dominating curves inside
`lem:ch38-nef-total-intrinsic`(indep). Re-pointed there.

### D.5 ch38 — two overclaims

`rem:ch38-hypothesis-map` says nefness "is used exactly once, in Step 2" and
that `ex:ch38-usc-not-psh` "shows that it cannot be weakened". Step 1 uses it
too, and that example ends with an explicit disclaimer that it "says nothing …
about weakening the hypothesis to pseudoeffectivity of `P`". It shows the
hypothesis cannot be *dropped*. Separately, `ex:ch38-usc-not-psh` states
`Psef(X) ⊋ Nef(X)` as a fact in dimension ≥ 2; it is false whenever the Picard
number is one — on `P²` both cones are `R_{≥0}H`.

### D.6 ch40 `lem:ch40-rational-approximation` — `h⁰` of a numerical class

`O_X(mN c_1(L))` is not defined: `c_1(L)` is a numerical class, and
`A' + NE_i` is only *numerically* equivalent to `NL`. The conclusion is right,
but only because bigness is a numerical invariant; as written the proof moved
between classes and bundles as if `h⁰` were numerical, which it is not.
Rewritten to prove `A' + NE_i` big and then transfer by numerical invariance.

### D.7 ch50 `rem:ch50-p1-dnc-checks` — the anticanonical constant

The remark says the `c = 1` member satisfies the anticanonical condition "with
`c = 1`", then three lines later computes `A_X(v_E) + φ_1(v_E) = 0` and
`A_X(v_Ẽ) + φ_1(v_Ẽ) = 0`, "both equal to the constant `c = 0`", and
`L^NA(φ_1) = 0`. `lem:ch50-anticanonical-constant` pins `c` by exactly that
identity, so `c = 0` and the earlier label is wrong. The divisor identity
itself survives — `X_0` is principal, so it contributes nothing to the line
bundle — but `c` is not read off the bundle, and the corrected text says so.

*(An earlier wave rejected a related "spurious `+X_0`" finding on the grounds
that `K^log = K + B_X + X_{0,red}` makes the `+X_0` cancel. That reasoning
concerned the divisor bookkeeping, which is fine. The constant was the error,
and the remark's own next sentence settles it.)*

### D.8 ch35 `lem:ch35-homogeneity-reformulations` — a vacuous clause

"`ψ ≡ 0` as soon as `ψ` is bounded on one scaling orbit through a point where
it is nonzero" — the hypothesis is self-contradictory, so the clause says
nothing; and the natural repair is false, since `ψ = log|x|` on `P¹` is
homogeneous and vanishes on the orbit through every `q ≠ [0:1]` without being
identically zero. Restated in the local form the proof actually establishes.

---

## E. Verified and found correct

### The new ch50 Step 1 proof

The proof of `eq:ch50-mass-above-mean` (`γ ≥ n/(n+1)`) written from scratch in
the first pass was re-checked adversarially link by link — the inverse-function
setup, the layer-cake identity `∫(a−λ)dμ = n∫_{v_0}^1 w^{n−1}ψ(w)dw`, the
subgradient step, both cases of the final inequality, and both stated equality
cases (`v(s) = s`, and `v(s) = (1+s)/2` with `n = 1`, where `γ = 5/8 = q + v_0²`).
**It is correct.** One completeness gap was found and closed: `ψ(γ) = A` needs
`v` strictly increasing on `[0,A]`, which follows after observing that
`v(A_1) = v(A)` with `A_1 < A` forces `v` constant on `[A_1, ℓ]` by concavity
and monotonicity, hence `γ = 1` and the bound is trivial.

### Chapters with no findings

ch33, ch36, ch37, ch46, ch47, ch49 — clean. The reviews recomputed, among much
else: ch46's `P¹` deformation to the normal cone three independent ways and the
`P²` toric computation three ways; ch47's Green's-function proof of uniform
concavity with `c_n = n/((n+1)(n+2))` and every worked energy; ch49's conic
intersection numbers and the `P²` table with both endpoints of `[1/3, 2/3]`
attained; ch33's sign conventions re-derived from the divisor bookkeeping on
the deformation to the normal cone and cross-checked against the Hirzebruch
surface; ch36's three-way cycle and the uniform squeeze; ch37's hypothesis
ledger. ch42 was clean apart from the step mislabel above.

---

## F. Reported but NOT applied

- **ch50 `ex:ch50-semistable-not-uniform`** cites `thm:ch50-entropy-lsc` plus
  weak approximation to pass from atomic `μ` to general `μ`. Entropy is only
  *lower* semicontinuous, which is the unusable direction, and
  `ex:ch50-entropy-jumps` in the same chapter refutes upper semicontinuity. A
  direct argument avoiding approximation was proposed — exchange the supremum
  with the integral in `eq:bj-dual-energy`, then use
  `E^∨_ω(δ_v) = ½T_ω(v) = ½A_X(v)` on `P¹` — and all its labels resolve, but I
  did not independently verify that last identity, so it is left for the author.
- **ch38 `lem:ch38-nef-total-intrinsic`(trace)** has the same
  no-strict-transform gap as D.4, but here the repair is not formal: for
  `Γ ⊆ π(Exc π)` every curve over `Γ` lies in `Exc π` and may meet
  `Supp(−C_Y)`. The reviewer could produce neither a counterexample nor a proof.
  The item is consumed nowhere — its only other occurrence is commentary — so
  the gap is not load-bearing. Options: restrict to `Γ ⊄ π(Exc π)`, add
  `dim X ≤ 2`, or delete the item.
- **ch31 `ex:ch31-p1-green`** — `φ_{x_E}` is a pullback under the retraction and
  so constant on retraction fibres, which "distance along the branch towards ξ"
  is not; the Gauss point of `D(1+c, r)` with `|c| = |π|^{1/2}`, `r < |π|^{10}`
  gives 0 by the stated formula and `½` by the retraction. The proposed repair
  (read `t(y)` as the retraction parameter) is almost certainly what was meant,
  but it rewrites a displayed three-case formula, so it is left for the author.
- **ch33** `ex:p1-product-dh` and `ex:ch33-harmonic-not-fg` give `C_+ = 1` and
  `C_+ = 1/4`, but `def:linearly-bounded-filtration` demands `F^{mC_+}R_m = 0`
  and both fail at exactly the endpoint (`F^{m}R_m = ⟨x^m⟩ ≠ 0`;
  `Ψ(a, m−a) = a(m−a)/m` attains `m/4`). Either state `C_+ > 1` (resp. `> 1/4`)
  or use the `λ_max(m) ≤ m` form. Also `ex:ch33-toric-p2` says the decreasing
  density is what `cor:ch33-dh-structure`(2) "requires"; that corollary gives
  concavity of `vol{G ≥ τ}^{1/n}` and forces nothing about the density for
  `n = 2`.
- **ch41 `ex:ch41-flatten-cone`** describes `Fix(ι)` as the exceptional curve
  alone; on `P²` the involution also fixes the line `{w = 0}` pointwise, so
  `Fix(ι) = F ⊔ L̃` on `W`. The smoothness criterion still applies and every
  number is unaffected, but `q` is also ramified along `L̃`.
- **ch43** `sec:ch43-uniformity` calls `cor:ch43-frobenius-all-affines` the item
  that "must" supplement the uniform-Frobenius lemma, while
  `rem:ch43-fixed-cover-not-enough` says the alternative "would not be fatal" —
  and that remark contradicts itself internally. The remark is right: a growing
  `q_i` is harmless since no fixed Veronese multiple is needed. Rhetorical only.
- Smaller prose items in the reviews: `ex:ch35-blowup-bdivisor`'s closing
  clause describes `H` rather than `H−E`; `lem:ch41-value-transitivity` would
  read better with a half-sentence pinning the exponent ambiguity;
  `prop:ch48-at-compact`'s "the integrand is ≥ 0 on `K`" is not established
  though the conclusion follows from the contact form; and ch42's
  `sec:ch42-de-jong` says algebraic closedness is used in "the only place" one
  paragraph after using perfectness.

---

## G. Verification

`editorial/tools/refcheck.py` over the real input graph after every batch:
282 files in the build closure, 10,979 labels, **0 multiply-defined, 0
dangling**; environment balance, brace delta, math delimiters and `\tag{}`
sequences clean everywhere except the known ch71 gap 71.33–71.35, which is
work in progress.

**Not compile-verified**: the audit VM's TeX lacks `newtx` and has no network.
Run `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex` natively.
