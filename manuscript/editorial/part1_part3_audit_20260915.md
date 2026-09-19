# Part 1 and Part 3 — adversarial audit and repair
## 2026-09-15 (waves 10–11)

Scope: ch02–ch08 (Part 1 foundations) and ch21–ch24, ch32 (BFJ and the
trivially valued analytification). All read in full. `refcheck.py` after every
batch — 282 files, 10 985 labels, 0 multiply defined, 0 dangling.
**Not compile-verified**: the TeX tree reachable from the mounted shell lacks
`newtxtext.sty`, so verification was `refcheck.py` (which also checks
environment and brace balance per file) plus hand re-derivation of every edit.

---

## A. Part 1 (ch02–ch08)

### A.1 `prop:centers-proper-separated` was false as stated

The proposition read "If `X` is proper, every valuation of `F` has a unique
center on `X`", with the preceding definition fixing only "`X` an integral
scheme with function field `F`" — so "proper" had no base.

**Counterexample.** `k = C`, `X = P^1_C`, proper over `C`, `F = C(z)`. Since
`C` has infinite transcendence degree over `Q` it carries nontrivial
valuations; extend one to `F` by `prop:chevalley-extension`. A center `ξ`
would force `C ⊂ O_{X,ξ} ⊂ R_v`, contradicting nontriviality on `C`. The same
failure occurs in the setting the chapter cares about: `X` proper over `K°`
and `v` a valuation of `K(X)` with `R_v ⊉ K°`.

This is exactly the gap relative to the cited `[Tag 0BX5]`, which is stated
for a *given* morphism `Spec R_v → S`. The uniqueness half — which is what
ch05 actually uses, in `lem:skeleton-monomial-invariants`(1) and
`prop:skeleton-nesting` — is correct as written and unaffected. The
proposition now carries the base and the extension hypothesis, with a warning
box giving the counterexample and noting that in this book the hypothesis
always holds, the valuations being either trivial on the ground field or
normalized so that `R_v ⊇ K°`.

### A.2 A node normal form that cannot hold in mixed characteristic

The proof of `prop:ch08-retraction-max` wrote
`Ô_{X,ξ} ≅ κ(ξ)[[x,y]]` with `π = u·xy`. But `X` is flat over `R`, so
`R ↪ Ô_{X,ξ}`; if `char K = 0` and `char K̃ = p > 0` then `p ≠ 0` in
`Ô_{X,ξ}`, while `p = 0` in `κ(ξ)[[x,y]]`. The isomorphism is impossible, and
it contradicts `def:ch08-semistable-curve-model` eight lines earlier, which
correctly says `R[[x,y]]/(xy−π)`. The section's standing hypotheses are only
"complete discretely valued, `v(π)=1`, algebraically closed residue field" —
mixed characteristic is in scope.

Rather than add a residue-characteristic-zero hypothesis to the whole
section, the proof now uses the chapter's own presentation over `R`, with the
monomial valuation written in it, and notes that ch05's `κ(ξ)[[x,y]]` form
needs a Cohen coefficient field, which exists only in equal characteristic.
That is what ch05's own standing-hypotheses paragraph already says, adding
that `v_α` can be built from the `α`-weighted filtration in any
characteristic.

### A.3 An argument that proved only the trivial case

The same proof ended: "For a vertical Cartier divisor the local equation is a
single element, both inequalities apply to it and to its inverse, and equality
`φ_D ∘ r = φ_D` follows." If `D` is effective and `ξ ∈ Supp D` then
`f ∈ O_{X,ξ}` but `f^{-1} ∉ O_{X,ξ}`, so the first part gives nothing about
`f^{-1}`; the two conditions hold together only where `D = 0`. Replaced by the
direct computation: `f = u ∏_j z_j^{a_j}` by `lem:snc-normal-form`(1),
`v_z(u) = 0`, and `v_z(z_j) = v_{r(z)}(z_j)` by the construction of `r`, so
both sides equal `Σ_j a_j α_j`. The statement's first inequality was also
asserted for *fractional* ideals but proved only for integral ones; the `π^N`
reduction is now displayed.

### A.4 Two out-of-scope citations of `prop:ch08-branching`

`sec:ch08-p1-models` said the possible blowup centres "are indexed by
`P^1(K̃)`" by `prop:ch08-branching`. That proposition is proved in
`sec:ch08-p1-tree` under "`K` algebraically closed", and the section preamble
states that its two extra hypotheses "are used in disjoint places and are
never used together, since they are incompatible". The claim is also false as
stated: the section offers `K = Q_p` as the model to keep in mind, and
`P^1_{F_p}` has infinitely many closed points while `P^1(F_p)` has `p+1`.
Restated: the centres are the closed points of `P^1_{K̃}`, indexed by
`P^1(K̃)` exactly when `K̃` is algebraically closed. (The clause "each blowup
extends the skeleton by one edge of length one" is correct for any `K̃`, since
`b_E = 1`.)

### A.5 ch05: the subdivision proof used max where the blowup gives min

In `thm:skeleton-subdivision` the support function `h` was called strictly
convex and taken to be the *maximum* of the affine functions `ℓ_m`, while
three paragraphs later the blowup chart is described as "the domain on which
the affine function attached to `m_0` realizes `h`". But `v_α(m/m_0) ≥ 0` for
every generator `m` says `ℓ_{m_0}(α) ≤ ℓ_m(α)`, i.e. `ℓ_{m_0}` realizes the
**minimum**. The max-subdivision and the min-subdivision differ in general, so
the two sentences were inconsistent. The book's own convention settles the
direction: `lem:vertical-ideal-convex`(2) makes `log|a|` a maximum of affine
functions, hence `v_•(a)` a minimum. `h` is now the strictly concave support
function with `v_•(I_h) = h`, the sign explained, and the "strictly convex"
phrase in `thm:skeleton-pl-realization` Step 1 made to match. The theorem
itself was never in doubt — the two presentations differ by `ℓ ↦ −ℓ`.

### A.6 Smaller Part 1 items

- `rem:lattice-length` cited `eq:ch08-curve-cl-measure` for an atom carrying
  the factor `b_G = 2`; that equation has no `b_Y` factor and is stated for a
  *semistable* model, where every `b_Y = 1`. The witness model is chosen
  precisely so that `b_G = 2`. The factor comes from the general mixed model
  measure of `sec:metrics-cl-measure`; now cited there. The same remark cited
  `eq:ch08-slope-formula`, also stated for a semistable model; now cited with
  that scope noted. Both numbers were independently recomputed and are right.
- The Farey/Stern–Brocot claim cited `ex:snc-chain-models` "as computed
  there". That example computes `xy = π^n`, whose inserted vertices are all
  integral of multiplicity one; it never produces a vertex of multiplicity
  `> 1` or a non-integer point. The claim is true and is now proved in place,
  with `ex:snc-chain-models` cited as a contrast.
- ch06's chapter plan said the Gubler–Martin comparison is "recalled and
  proved" in `sec:metrics-formal-pl`; that section's proof environment opens
  "The three assertions are imported from Gubler–Martin with their published
  scope". Corrected.
- A truncated sentence in `rem:ch08-toric-model` ("The normal fan of that
  epigraph is, and hence a toric scheme…") completed, and a stray `\cdot` in
  ch05 removed.

---

## B. Part 3 and ch32

### B.1 `cor:ch32-determination-divisorial`(3) was false, and its own clause (2) is the counterexample

The clause read: "If `φ` is usc and `ψ` is lower semicontinuous, and `φ ≤ ψ`
on `X^div`, then `φ ≤ ψ` on `X^an`."

The proof needs `{φ > c}` open — that is *lower* semicontinuity of `φ` — and
`{ψ < c}` open — that is *upper* semicontinuity of `ψ`. Both justifications in
the proof named the opposite semicontinuity. And the statement is not merely
unproved: clause (2) of the same corollary supplies the counterexample. Take
`ψ ≡ 0`, continuous hence lsc, and `φ = 1_{v_0}` for `v_0 ∉ X^div`, which is
usc since `{v_0}` is closed; then `φ ≤ ψ` on `X^div` but `φ(v_0) = 1 > 0`. So
(2) and (3) asserted contradictory things about the same pair. The corrected
pairing is also the one in `thm:bj-basic-closure`'s determination clause,
which quantifies over upper semicontinuous test functions.

### B.2 `prop:ch24-forced-ibp`: the intermediate identity omitted two terms

The proof displayed
`∫φ_p ddc h ∧ T = 𝔈(φ_p,h,Φ) − 𝔈(φ_p,0,Φ)`.
Since `ddc h ∧ T = MA_θ(h,Φ) − MA_θ(0,Φ)` and `eq:ch24-energy-slot-bounded`
applies to each term, the correct value is
`[𝔈(φ_p,h,Φ) − 𝔈(0,h,Φ)] − [𝔈(φ_p,0,Φ) − 𝔈(0,0,Φ)]`;
the printed line drops `−𝔈(0,h,Φ) + 𝔈(0,0,Φ)`, that is, drops
`−∫h θ∧T`. The reductio is immediate: by symmetry of `𝔈` the printed
right-hand side equals the left-hand side of the *first* display, which
combined with `∫h θ∧T = 𝔈(h,0,Φ) − 𝔈(0,0,Φ)` would force `∫h θ∧T = 0` —
false already at `h = 1`, where it is `V > 0`. The proposition's statement and
its final telescoping display are correct; only the intermediate line, which
is the one a reader would quote, was wrong.

### B.3 Two arithmetic slips in ch23

- `cor:ch23-envelope-rate` stated the bound `C/m` "for `m > m_0`" with
  `C = 2m_0(B + ‖φ_E‖)`. From `eq:ch23-envelope-rate` one needs
  `m_0/(m−m_0) ≤ 2m_0/m`, i.e. `m ≥ 2m_0`; at `m = m_0+1` the inequality goes
  the wrong way. Range corrected.
- In `lem:ch23-concave-lipschitz`, rearranging
  `h(τ') ≥ (r/(d+r))h(τ) + (d/(d+r))h(τ'')` gives
  `h(τ) − h(τ') ≤ (d/r)(h(τ') − h(τ''))` — with `h(τ')`, not `h(τ)`, in the
  bracket. The final bound `2Md/r` is unaffected, so the lemma is true as
  stated.

### B.4 Wrong reference targets

- `thm:ch22-proper-normalization` Step 1 justified `ρ = ρ ∘ p_X` by
  `lem:ch21-model-skeletal-properties`, which is stated only for θ-psh model
  functions, while the theorem's `ρ` is *every* model function with no
  positivity hypothesis. The correct target is `lem:model-function-affine`,
  which ch21 itself cites for exactly this purpose elsewhere.
- ch32's `ex:ch32-gauss-ray-numbers` cited `prop:ch24-model-support` for "no
  Monge–Ampère mass of a bounded potential"; that proposition is about model
  measures only. Retargeted to `prop:bounded-ma-no-polar-mass` together with
  the pluripolarity of the rigid point.
- In `thm:ch32-trivial-locus` the parenthetical "its maximal ideal, which is
  zero" holds only when `Y` is an irreducible component of `X`; for `Y ⊊ X`
  the local ring has dimension `codim Y > 0`. What the argument needs, and
  what `cor:ch32-orbit-degenerate` states correctly, is that the maximal ideal
  *is* the support prime.

### B.5 ch21 and ch22: an example and three bookkeeping defects

- `ex:ch22-gauge-computed`: `B(σ)` is the hexagon with vertices
  `(1,0),(0,1),(−1,1),(−1,0),(0,−1),(1,−1)`, whose edges lie on `x+y=1`,
  `y=1`, `x=−1`, `x+y=−1`, `y=−1`, `x=1` at distances
  `1/√2, 1, 1, 1/√2, 1, 1`. **Two** edges lie at `1/√2`, as the central
  symmetry asserted two paragraphs earlier forces; the text said "every other
  edge lies at distance 1". `Λ(σ) = √2` is unaffected.
- `rem:ch21-semistable-not-cofinal` argued that `x_{E'}` lies on no semistable
  skeleton from "a vertex only if multiplicity 1, a branch point only if a
  vertex" — which leaves the relative interior of an edge untouched, and which
  the remark's own data refute: `x_{E_{1/2}}` is divisorial of multiplicity 2
  and *is* the midpoint of the semistable skeleton `Γ_0`. The obstruction is
  the centre, not the multiplicity; argument replaced, scoped to the running
  conic over `k((t))`.
- `prop:ch21-constants` quantified no `ε` and dropped the upper bound its own
  proof gives; `sec:ch21-chain` said only two lines of the dependency chain
  are imported when three are; the worked-example count said five where there
  are seven.

### B.6 BFJ16 numbering — resolved against the literature

ch21 cited the decreasing-regularization theorem as `[BFJ16, Thm 8.5]` and
ch22 as `[BFJ16, Thm 8.7]`; the book contradicted itself. Settled rather than
guessed: in Boucksom–Favre–Jonsson, *Singular semipositive metrics in
non-Archimedean geometry*, J. Algebraic Geom. 25 (2016), §8 "Envelopes and
regularization", **Theorem 8.7** is the monotone-regularization statement and
Theorem 8.5 is the uniform convergence of model functions to the psh envelope
— a different result. ch22 was right; ch21 corrected to 8.7. This also makes
ch21's citation of Corollary 8.8 for the continuous comparison read correctly,
as the corollary immediately following.

---

## C. The two held items — both applied after reading the surrounding text

### C.1 ch23: "we may assume the approximant is determined on the model"

Used twice, in `prop:ch23-model-vs-psh-envelope` Step 2 and
`thm:ch23-base-ideal-approximation` Step 3a. The enlargement is circular — the
model is chosen to carry a function produced by approximating on that model's
own skeleton — and it cannot be arranged in general: a θ-psh model function
determined on `Z` is *affine* on each face of `Δ_Z`
(`lem:model-function-affine`), while the function being approximated is only
convex there, so `|χ − ψ| < ε` with `χ` determined would force `ψ|_{Δ_Z}` to
be within `ε` of affine on every face.

Determinedness is never needed. Both proofs use the displayed equality only
through "`≤`", and clause (1) of `def:ch21-bfj-psh` — `φ ≤ φ ∘ p_X` for every
θ-psh `φ` and every determining SNC model — supplies exactly that, with no
hypothesis at all. **Applied** at both sites: the enlargement deleted, the
equality weakened to the inequality, and Step 3b of
`thm:ch23-base-ideal-approximation` now also dominates a model on which `φ_D`
is determined, which it needs in order to write `φ_D` as a vertical divisor.
Both conclusions, `eq:ch23-two-envelopes-quasimonomial` and
`eq:ch23-model-competitor-at-point`, are unchanged.

### C.2 ch21: `prop:ch21-curve-criterion`

The forward half identified the Laplacian of the *restriction* to `Γ'` with
the vector of relative degrees, via `eq:ch20-curve-laplacian-general`. That
identity holds only for model functions determined on the model whose skeleton
is that complex, whereas `P_{C'}(θ)` ranges — as the chapter emphasises — over
model functions determined on *arbitrary* higher models. The chapter supplies
its own counterexample: in `ex:ch21-conic-refinement`, `φ|_{Γ_0} ≡ 0` so
`μ_0 + Δ_{Γ_0}(φ|_{Γ_0}) = δ_{v_0} + δ_{v_1}`, while the relative degrees of
`ρ_1^*L − E` on `C̃_0`, `C̃_1` are `0` and `1`.

The proposition is true; the missing step is the flux inequality. **Applied.**
For `ψ` determined on `C'' ≥ C'` with skeleton `Γ'' ⊇ Γ'`, relative nefness is
`μ_0 + Δ_{Γ''}ψ ≥ 0` on `Γ''`; splitting, for `q ∈ Γ'`,
`(Δ_{Γ''}ψ)({q}) = (Δ_{Γ'}(ψ|_{Γ'}))({q}) + Σ_T Σ_{e⊂T, e∋q} ∂_e ψ(q)`
over the components `T` of `Γ''∖Γ'` attached at `q`, each inner sum is `≤ 0`
by `eq:ch21-curve-flux`, and `μ_0` gains no mass on a higher skeleton by
`eq:ch21-curve-no-new-mass`. Hence
`(Δ_{Γ'}(ψ|_{Γ'}))({q}) ≥ (Δ_{Γ''}ψ)({q}) ≥ −μ_0({q})`.

No circularity: `eq:ch21-curve-flux` sits in Step 2 of
`prop:ch21-curve-retraction`, later in the chapter, and its proof uses only
`eq:ch20-nef-pullback-test` and `eq:graph-laplacian`. The converse half of the
criterion was always sound — there the model function *is* determined on the
model realizing `Γ'`, so the identity does apply.

---

## D. Reported and NOT applied

- **`def:ch14-radial-contraction`** takes the naked transpose with no sign;
  whether that is the normalization compatible with `ι'_E[ω] = [ι'_E ω]` was
  not settled. Irrelevant to its only use, `prop:ch14-strongly-homogeneous`,
  whose conclusion is a vanishing — but it would matter if
  `def:ch14-strongly-homogeneous` were used quantitatively in
  `sec:appD-supercurrents`. **Open.**
- **`prop:ch13-finite-integral`** asserts
  `p_*((p^*ω)_Rad) = dc(p)·ω_Rad` under "finite above the complement of a
  Zariski-closed subset of dimension `< n`"; whether that suffices for `p^*ω`
  to have compact support and for `p_*` of the measure to be Radon was not
  settled — a non-proper open immersion satisfies the hypothesis. Needs CLD
  Prop. 15.4.3, which the text cites for the general case. **Open.**
- **ch12 `thm:analytic-tropical-balancing` proof** quotes the slope formula as
  "the sum of the outgoing slopes … equals the degree of the divisor";
  `eq:ch08-slope-formula` is an identity of *measures* with a minus sign,
  `Δ_Γ F = −r_* div(f)`. The conclusion is correct either way, since `χ^m` is
  invertible on the fibre and the atom at the vertex vanishes. Wording only.
- **Rejected (false positive).**
  `thm:p063-current-psh-ordinary-regularization` was reported as a dangling
  label absent from the live manuscript. It is live: defined in an `editorial/`
  packet that `parts/part2/ch19_cld_examples.tex` pulls in with `\input`, and
  `refcheck.py` — which resolves the real input graph from `book.tex`
  following `\input`, `\include` and `\draftinclude` — reports 0 dangling
  references manuscript-wide. This is the same mistake an earlier pass made by
  globbing only `parts/`, `appendices/`, `frontmatter/` and `style/`; recorded
  again so it is not raised a third time.
- **External locators** not checkable offline: `[BFJ16, App. B, Thm B.8 and
  Rem. B.9]`, `[GJKM19, Thm 8.2 / Cor 8.3 / Thm 6.3]`, `[GM19]`, `[CL06]`,
  `[BGPS14]`, `[Vil20]`, and ~15 `[Thu05]` locators. In each case the
  mathematical content attributed to the source checked out independently.
  (`[BFJ16, Thm 8.7]` *was* resolved — see B.6.)

---

## E. Verified clean

ch02–ch04 came back with no sign, constant or numerical error at all. Every
worked computation in ch06, ch07, ch08, ch21, ch22, ch23, ch24 and ch32 was
recomputed by hand, including all of ch08's intersection matrices, residual
degrees, nef cones and mass ledgers. ch22's 86 manual tags are complete,
strictly increasing and unduplicated; ch06, ch07, ch08, ch21, ch23, ch24 and
ch32 use no manual tags at all.

Notable independent confirmations: ch08's Tate-curve example, where the
`j`-invariant formula was checked twice over (degree `12 = [X(3):X(1)]`, and
pole order `3` matching `I_3`); ch22's Frobenius-power example, where all
three sample `ν(p^e)` values were recomputed from Lucas's theorem; and ch24's
toric-surface mixed example, where the Minkowski sum, its shoelace area `3/2`,
the `n! = 2` transfer and the polarization identity all agree.
