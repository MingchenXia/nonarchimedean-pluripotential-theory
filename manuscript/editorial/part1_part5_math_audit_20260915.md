# Mathematical audit — the seven previously unaudited chapters

Date: 2026-09-15
Chapters: ch01, ch27, ch30, ch45, ch54, ch55, ch58.

These are the chapters that no earlier wave had touched. Five parallel
adversarial reviews were run; every finding below was re-derived by hand
before being applied, and the ones that could not be settled are listed
unapplied in §F rather than guessed at.

**ch54 and ch58 came back clean.** No findings in either. The min-plus
conventions of ch58 (larger ideal → smaller value; `Z(v) ⊆ Supp(v)` from
`p_s ⊆ p_c`) and the sup/inf hypothesis pairing of ch54 were checked
against two concrete valuations and found consistent throughout.

---

## A. Errors in computed mathematics

### A.1 ch27 `ex:ch27-toric-legendre` — the contact set is all of `N_R`

The text asserts that for `1 < t < 2` the contact set is `{-1, 0, 1}`.
Write `λ = t-1`, so the perturbed weight is `w = h_Q + λg` with
`h_Q = max{0, 2x}` and `g = max{0, 1-|x|}`. Reading left to right, the slopes
of `w` on `(-∞,-1), (-1,0), (0,1), (1,∞)` are

    0,   λ,   2-λ,   2,

which is nondecreasing exactly when `0 ≤ λ ≤ 1`, i.e. exactly when
`1 ≤ t ≤ 2`. So on the *entire* stated range `w` is already convex,
`u_t = conv(w) = w`, and the contact set is all of `N_R`. The three displayed
verifications are individually correct but only give `{-1,0,1} ⊆ C`; the text
converts them into an equality.

Consequence for the exposition: orthogonality on that range holds trivially,
`f - P` vanishing identically, which is the opposite of the point the sentence
is making. The measure itself is right —
`MA_R(u_t) = (t-1)δ_{-1} + (4-2t)δ_0 + (t-1)δ_1`, the three slope jumps,
of total mass 2. Rewritten to say what the computation actually shows, and to
note that the envelope is proper only outside `[1,2]`.

### A.2 ch27 `ex:ch27-naive-failure-chain` — the wrong constraint is named

With `A_0 = 1 + (v_1 - v_0)` and `A_1 = (v_2-v_1) - (v_1-v_0)`, at
`P = (-1,-2,-3,-2,-1)` both `A_0(P) = 0` and `A_1(P) = 0`. Replacing `P_0` by
`P_0 + ε`:

    A_0 = 1 + (P_1 - P_0 - ε) = -ε < 0,
    A_1 = A_1(P) + ε = +ε ≥ 0.

So raising `v_0` is blocked by `A_0 ≥ 0`, the constraint **at `e_0`**, and it
strictly *relaxes* convexity at `e_1`. The text says the reverse on both
counts, and contradicts the general mechanism of Step 4 of
`thm:ch23-model-orthogonality-curve`, which the very next sentence cites
correctly. Rewritten.

### A.3 ch30 `ex:ch30-gauss-normal-cone` — a twisting divisor counted twice

The polarization is defined as `L_c := ρ*L_{A^1} + D`. The displayed
coefficients `((L_c + D)·E_i)` therefore double-count `D`, and do not produce
the stated values: `((ρ*L + 2D)·E_0) = -1` and `((ρ*L + 2D)·E_c) = 2`, not
`0` and `1`. The quoted values are those of `(L_c·E_i)`, which is what
`eq:bj-model-ma-atomic` prescribes; the conclusion `MA^u_ω(φ) = δ_{c·ord_0}`
is right. Corrected, with a note that the twist is already inside `L_c`.

### A.4 ch55 `prop:ok-mvob-movable-upper` — degree bookkeeping off by `n`

`s_0 = ∏_j b_j` and `s_j = a_j ∏_{ℓ≠j} b_ℓ` are products of `n` sections of
the common degree, so they lie in `W_{1,nq}`, not `W_{1,q}`. The error
propagates: `s_0^{rm}` then has degree `rm·nq`, not `k`. The valuation
bookkeeping `ν(s_j) - ν(s_0) = e_j` is unaffected. Repaired by naming the
common degree `q` and setting `p_0 = nq`.

### A.5 ch55 `rem:ok-mvob-normalizations` — the mixed-volume coefficient

The remark normalizes by `V(K,…,K) = λ_n(K)` and then calls `V` "the
coefficient of `t_1⋯t_n`". These are inconsistent: by (D.16) that coefficient
is `n!·V(K_1,…,K_n)`. Setting every `K_i = K` makes the contradiction visible
— the `t_1⋯t_n` coefficient of `(Σt_i)^n λ_n(K)` is `n!λ_n(K)`, not `λ_n(K)`.
No downstream formula is affected, since the section carries the `n!`
explicitly throughout; only this sentence, whose sole job is to pin the
normalization, was wrong. Corrected, with the `K_i = K` check included.

### A.6 ch55 `thm:ok-dh-flag-independent` — a truncation that is not concave

Grafting `Γ_{-∞}` onto the levels at `-ε^{-1}` leaves a downward jump there
and so violates the concavity required by `def:rays-test-curve`(1): if `γ` is
concave decreasing with `γ(-∞) = L > γ(-C)`, concavity at the midpoint of
`-C∓h` forces `γ(-C) ≥ L` in the limit. Replaced by the standard truncation
`Γ^ε_τ := Γ_{max{τ, -ε^{-1}}}`, which is concave, bounded, decreases
levelwise to `Γ`, and has the volume convergence the limiting argument needs.

---

## B. Proofs whose cited authority does not supply the step

### B.1 ch30 `prop:finite-pullback-psh` — an import that says something else

Ampleness of a finite pullback is cited to
`sec:ch20-imported`(`itm:ch20-import:ega`). That item is *openness of
relative ampleness in the fibres* (EGA III 4.7.1) and says nothing about
pullback along a finite or affine morphism. The assertion is true (EGA II
5.1.12), but the book was quoting an import it does not have — and this
proposition is what puts `(Y, f*θ)` inside (BFJ). Re-pointed to EGA II
5.1.12, with a note that the ch20 item is not the relevant one.

### B.2 ch30 `sec:ch30-descent-limits` — an unnecessary and invalid "repair"

The text claims averaging preserves monotonicity "only after passing to the
net of finite minima, which is again a net of model functions by
`prop:ch20-model-max`". Two independent problems. First, no repair is needed:
each `g ∈ G` acts by a homeomorphism, so a finite convex combination of
decreasing nets over one index set is decreasing, with limit the same
combination of the limits, which is `u∘π` by `G`-invariance. Second, the
proposed substitute breaks the argument — a finite *minimum* of `θ`-psh model
functions is a model function but need not be `θ`-psh (on `P^1`, the minimum
of two tent functions has a concave corner), and `prop:ch20-model-max` is
stated for finite **maxima**. Both halves corrected.

### B.3 ch27 `prop:ch27-orthogonality-equivalences` — a false hypothesis signature

The scope sentence puts `(4)⇔(5)` among the implications using no continuity
of `P_ω(f)`. But (5) is the Fenchel equality against the model-test conjugate,
and `(4)⇔(5)` runs through `prop:ch27-conjugate-identification`(2), which is
proved by uniform approximation by `ω`-psh *model* functions — i.e. it spends
`thm:bfj-envelope-regularity`. The chapter records exactly this elsewhere as
item (EC5) of `sec:ch27-local-uses`, and `rem:ch27-legendre-picture` calls it
"unavoidable in that form". No proof is damaged; the signature claim was.
In a chapter whose stated purpose is auditing which hypothesis is spent
where, this matters more than its mathematical weight.

### B.4 ch45 `warn:ch45-continuity-ample` — two defects in one sentence

`cor:ch45-extremal` proves only `V_θ ≡ 0 ⟺ θ ∈ Nef(X)`; unboundedness below
comes from `lem:ch34-psh-nonempty`. And "in particular it is not continuous
or finite valued" does not follow: an usc function on a compact space can be
real valued and unbounded below — `x ↦ -1/x` on `(0,1]`, extended by `0` at
`0`, is usc (`limsup_{x→0} = -∞ ≤ 0`), finite everywhere, unbounded below.
"Not continuous" is correct, a continuous function on a compact space being
bounded. Both corrected.

---

## C. Claims stronger than what was proved

### C.1 ch45 `rem:ch45-increasing-asymmetry` — raw envelope vs its regularization

The remark says `sup F_θ(h)` "need not be `≤ h`". By
`def:ch45-admissible-obstacle`(3), `F_θ(h) = {ψ ∈ PSH_X(θ) : ψ ≤ h}`, so the
raw supremum is `≤ h` **always**, whatever the regularity of `h`. The object
that can escape is the *regularized* supremum `(sup F_θ(h))^*` — which is
precisely the mechanism `lem:ch45-raw-equals-regularized` isolates, and
precisely what the remark is arguing for. The star had been dropped.

### C.2 ch45 `rem:ch45-fixed-class-cost` — a construction that does not break down

The remark claims that for a pseudoeffective non-nef class "the obstacle `g`
may have an empty competitor family, so the construction breaks down at the
first step". But in `thm:ch45-continuous-regularization` the obstacles are the
members of `G = {g ∈ C⁰ : g ≥ u}` for the given `u`, so `u ∈ F_θ(g)` for
every `g ∈ G` — the proof says so itself — and the family is never empty.
`G` is nonempty and downward directed with `inf G = u` by
`lem:ch35-usc-inf-continuous`, which needs only that `u` be usc and bounded
above. So `u_g = P_θ(g) ↓ u` still holds in the fixed class. What genuinely
fails off the ample locus is *continuity* of the approximants, and
necessarily: a continuous member of `PSH_X(θ)` would be bounded and would
force `θ ∈ Nef(X)`. Rewritten to say that.

### C.3 ch45 `thm:ch45-continuous-regularization` — generic finiteness

The concluding sentence describes `PSH_X(ω)` as the set of pointwise limits
of decreasing nets of continuous `ω`-psh functions. The constants `-m` are
continuous and `ω`-psh (ample ⟹ nef) and decrease to `≡ -∞`, which
`def:bj-psh`(2) excludes. The proof already carries the right form
("generically finite limit"); the statement did not.

### C.4 ch45 `ex:ch45-no-attainment` — "any subfamily"

A singleton subfamily has a greatest element. The claim holds for every
subfamily *with the same supremum*, whose parameters must accumulate at `0`.

### C.5 ch30 `sec:ch30-dict-backward` — an invariant that distinguishes nothing

"The invariant that distinguishes them is the degree of the induced extension
of function fields." In `ex:ch30-conic-base-change` that degree is
`[K':K] = 2` and the mass is *unchanged*; in `ex:ch30-power-map` it is `3` and
the mass triples. The degree exceeds one in both, so it separates neither.
The chapter's own `rem:ch30-two-inputs` says what does: whether the ground
field, and with it the residue field over which special-fibre degrees are
taken, has changed. Corrected to agree with it.

### C.6 ch30 `itm:ch30-import:regularization` — "the only place"

`lem:ch30-base-change-model`(mult) also invokes separability of `K'/K` and
`k'/k`, so regularization is not the only entry point for residue
characteristic zero. Qualified — and noted that the second use is avoidable,
since `ef = [K':K]` needs no separability for a complete discretely valued
field (`R'` is finite free over `R`) and `O_{X,η_E}` is excellent.

### C.7 ch30 `thm:ch30-gauss-image` — an implication stated backwards

"Assume `k` infinite --- in particular algebraically closed" asserts that
infinite implies algebraically closed. The intended direction is the reverse.

### C.8 ch01 — four previews stronger than the theorems they preview

This is the characteristic failure mode of an overview chapter, and all four
instances hand a *complex* or *ideal-case* generality to a non-Archimedean or
restricted theorem.

1. **Bedford–Taylor for locally bounded psh, claimed twice** (in the Part II
   summary and in item (C) of the master-diagram legend). `ch16` opens by
   saying the CLD nonlinear domain is the class of *continuous* psh functions,
   "In particular, we do not silently replace ``continuous'' by ``locally
   bounded.''", has a delimitation row reading "locally bounded → **not**
   used", and carries a warning ending "the classical convergence theorem of
   [BT82] ... is **not** being transported." The introduction promised exactly
   what that chapter was written to forbid, once of them in the arrow legend a
   reader will treat as the book's contract. This is the most damaging of the
   four.
2. **Monge–Ampère mass preserved along arrow (B).** The arrow as described
   includes the decreasing-singular-limit step, but
   `thm:cl-continuous-extension` covers only uniform limits of semipositive
   model metrics, and `ch24` says the opposite for the singular step: "mass
   may be lost to the polar set". Restated: preserved on the uniform half and
   for bounded potentials, preserved on `E^1` with the nonpluripolar
   convention, only nonincreasing in general.
3. **"Compact Kähler space".** Both `ch53` and `ch60` say "compact Kähler
   **manifold**" in their first line, and `rem:tna-smooth-scope` says the
   singular extension is cited, not proved. The book uses "Kähler space" as a
   precise term for the singular case elsewhere, so this reads as a claim.
4. **The toric example cites a model-metric theorem** in a case the example
   itself concedes need not be a model metric. `thm:toric-ma-comparison`
   assumes a semipositive toric `Q`-model metric over a complete discretely
   valued field. The statement is still true in the remaining case, but by
   `cor:toric-ma-continuous`.

### C.9 ch27 `sec:ch27-dependency` (D8) — "proved outright"

Neither cited statement is unconditional: `prop:ch27-curve-orthogonality`
carries a model-level hypothesis available only for strictly semistable
models (and `rem:ch27-curve-base-change` says in as many words that no
unconditional curve theorem is stated), and `thm:ch27-toric-orthogonality`
proves orthogonality for the *invariant* envelope only, which
`rem:ch27-toric-scope` says is not the orthogonality property of
`def:orthogonality-property`. Qualified.

---

## D. Verified and found correct

Recorded so the negatives are on file. Every number in every worked example
of all seven chapters was recomputed. In particular:

- **ch01**: the equilibrium-measure computation including the
  `dc = (i/4π)(∂̄-∂)` normalization and the inner-normal sign; the Gauss-point
  and node/cusp valuations; the blowup model function with `(E·E) = -1` and
  total mass `0`; the Lagerberg corner sign; the toric three-piece `F` with
  `MA_R(F) = ½δ_{-1/2} + ½δ_{1/2}`; the product test configuration with
  `DF = 0` and barycentre `= energy slope = ½`.
- **ch27**: the Beta weight `1/(n+1)`, the mutual-integrability chain, the
  Hahn–Banach superdifferential package with `D^+ = min` and `D^- = max`, the
  two-sided squeeze, the five-vertex chain in full (all three energy pieces
  and both matching points), and both toric Legendre examples including
  `V = n!·vol_M(Q)`.
- **ch30**: the whole `(e,f)` ramification calculus and the cancellation
  `(1/e)(1/f)(ef) = 1` that removes `[K':K]` from `thm:base-change-ma`; all
  five examples (power map, surface blowup with nef cone `-1 ≤ c ≤ 0`, conic
  base change with the `A_1` singularity, and both Gauss examples). No sign
  error and no variance error anywhere in the chapter.
- **ch45**: the nodal cubic, the cuspidal cubic and its explicit envelope, and
  the transcendental-constant example with `τ = log 2` and the
  second-derivative jump — all line by line; the four-step assembly and the
  perturbation reduction.
- **ch55**: the `n!` bookkeeping in all three of its roles, the layer-cake
  identity, the Okounkov/DH orientation (the pushforward is *not* reflected,
  cross-checked against ch65), the Kodaira trick, the John-ellipsoid
  uniformity lemma, and both toric examples.
- **ch54, ch58**: as above — clean.

---

## E. Cross-reference health

The whole manuscript was re-checked with a resolver that follows the actual
input graph from `book.tex` (`\input`, `\include`, and the book's own
`\draftinclude`), saved at `editorial/tools/refcheck.py`:

    files in build closure:      282
    labels in closure:        10,979
    multiply-defined labels:       0
    dangling references:           0

The only per-file structural anomaly manuscript-wide is the `\tag{}` gap
71.33–71.35 in ch71, which is uncommitted work in progress.

---

## F. Hypotheses restored to match their proofs

Each of these was confirmed against the cited statement before being applied.

### F.1 ch45 — the unibranch hypothesis, omitted in three places

`thm:bj-final-obstacle-psh` is stated "If `X` is unibranch". Its consumers
`thm:bj-final-decreasing-obstacles`, `prop:bj-final-obstacle-calculus`(3) and
`cor:bj-final-finite-maxima` did not carry the hypothesis, while the net
version `thm:ch45-decreasing-obstacle-nets`, two theorems later in the same
subsection, opens "Let `X` be integral projective unibranch". The omission is
conspicuous precisely because `sec:ch45-hypotheses` deliberately does *not*
make unibranchness standing — the chapter applies other statements to
non-unibranch `X` (`cor:ch45-failure-nonunibranch`, `ex:ch45-node-computed`).
Restored in all three.

### F.2 ch45 — non-metrizability needs an uncountable ground field

`sec:ch45-nets-formality` cites `prop:ch36-no-sequences` for
non-metrizability of `X^an`. That proposition reads "over an *uncountable*
algebraically closed trivially valued field", and the hypothesis is doing
work: over a countable algebraically closed field the analytification of
`P^1` is a compact star with countably many rays and has a countable base.
The chapter knew this — eleven lines later it says "may take `X` a curve over
an uncountable algebraically closed field". Qualified.

### F.3 ch55 — positivity of interior levels is a lemma, not the definition

`lem:ok-i-model-mass-volume` attributes positivity of the mass of interior
levels to `def:rays-test-curve`. That definition's clause (3) imposes
`∫_X θ^n_{Γ_{-∞}} > 0` at the **endpoint** only; clauses (1)–(2) are just
"decreasing and concave" and "every level is model". The interior statement
is `lem:rays-test-positive-levels`, *deduced* from the endpoint condition
and concavity. The step is fine; the pointer was wrong. Re-pointed.

---

## G. Reported but NOT applied

- **`prop:ch45-noncircular` numbering.** The non-circularity audit numbers its
  seven imported statements differently from `sec:ch45-inputs`: the proof's
  (4)(5)(6) split `thm:bj-normal-envelope` / `cor:bj-normalization-source-ep`
  / `lem:bj-unibranch-normalization-universal` + `cor:bj-universal-reflection`,
  while the inputs section pairs them differently. One consequence is that
  `cor:bj-universal-usc`, input (5) there and genuinely consumed in Step 3 of
  the assembly, is never audited. Renumbering needs both lists open and a
  decision about which numbering is canonical — left for the author.
- **`prop:ok-dh-weak-continuity` follow-on.** The BHJ17 §3.2 DH measure is a
  probability measure while `DH(Γ)` has mass `vol(Γ)`, so "agrees" wants a
  normalization qualifier. Not applied because `[Xia21, Rem. 7.17]`, which the
  sentence also cites, may already carry it — worth one look at that remark.
- Smaller prose items from the reports, none affecting a proof: the
  `X^{divis}` real-vs-rational multiples discrepancy (ch45 `sec:ch45-hypotheses`
  says real, ch37:204 and ch40:2582 say rational); the convexity justification
  in `sec:ch45-curve-conventions`(ii), where "slopes nondecreasing hence
  nonincreasing" does not follow and the right reason is one sentence earlier;
  "meeting" vs "containing" at ch45:1280; `cor:ch27-linearization` proving only
  `q'(0+)` where the statement claims differentiability (true, but one line
  short); the `(2C+1)/δ` constant in `thm:ch27-legendre-orthogonality`(2);
  `prop:nef-pullback` being applied throughout ch30 outside its stated
  vertical-modification hypothesis — harmless, since its one-line proof covers
  the uses, but the clean repair is to broaden the statement upstream in ch03;
  and ch01's reader's guide stopping at ch69, so that ch70, ch71 and ch72 are
  never mentioned in the introduction at all.
