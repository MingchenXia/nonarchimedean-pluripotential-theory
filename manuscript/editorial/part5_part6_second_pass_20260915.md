# Second adversarial pass — Parts 5 and 6 (ch51–ch71)

Date: 2026-09-15
Chapters: ch51, ch52, ch53, ch63, ch64, ch65, ch66, ch67, ch68, ch69, ch70, ch71.

Four parallel reviews, each told the first-pass findings were off-limits. Every
item below was re-derived or re-verified against the cited statement before
being applied; §D lists what was left unapplied and why.

**ch63 and ch69 came back mathematically clean.** ch68 had one defect, ch70 one.

---

## A. Proofs leaning on statements the book elsewhere disowns

### A.1 ch53 `lem:tna-transition-mass-identity` — the `I`-envelope does not preserve mass

The lemma asserts `M_{θ+ω}(u) = vol(θ+ω, u)` — equality in
`eq:complex-mass-volume` — and justifies it with "Total mixed nonpluripolar
mass against a fixed smooth semipositive form is preserved under that
projection, which is `eq:complex-current-volume`".

Two problems. `eq:complex-current-volume` supplies only
`M_θ(φ) ≤ vol(θ,φ)`, the wrong direction, with equality reserved for analytic
singularities, which the levels are not assumed to have. And the sentence is,
verbatim, the claim that the `I`-envelope preserves mass — which ch51
explicitly disowns under the heading *"Not claimed: the `I`-envelope preserves
mass. Only the `P`-envelope does"*, with `ex:ch51-cantor` raising the mass from
`½` to `1`.

The conclusion is recoverable, and the input is available eleven lines earlier
in the same chapter: the levels are `I`-good, so
`P_{θ+ω}[u] = P_{θ+ω}[u]_I`, and then the `P`-envelope mass identity
`eq:complex-p-projection` gives the equality. Rewritten that way, with the
warning attached. The equality is genuinely needed —
`lem:tna-mass-drop-transition` subtracts it at two parameters and breaks with
only `≥`.

### A.2 ch51 `thm:complex-p-projection` Step 3 — a lemma whose only use violates its hypothesis

`lem:ch51-rooftop-contact` requires `u` and `v` to have bounded difference from
one fixed positive-mass model potential `φ`, which forces `u − v` bounded. It
is applied to `(φ + C, V_θ)` for an arbitrary positive-mass `φ`, where
`φ − V_θ` is unbounded — already in the chapter's own `ex:ch51-p1-envelope`
(`φ = ½G_0`, `V_ω = 0`), which the same step cites two lines later as the
worked illustration. So the lemma supplies nothing at any fixed `C`. Its proof
confirms the hypothesis is load-bearing, routing through `thm:appH-comparison`,
stated only for `E(X,θ,φ)`. The fixed-`C` case now goes to the import that
covers it, and the lemma is cited only where it applies.

---

## B. Errors in computed or asserted mathematics

### B.1 ch64 `thm:cma-test-curve-moments` — a mass normalization dropped

ch64 states the DH moment formula with `V = (L^n)` where ch55's
`thm:ok-dh-flag-independent` has `vol(Γ) = ∫_X⟨θ^n_{Γ_{-∞}}⟩`. The
substitution is legitimate only when the terminal level has **full** mass,
which no hypothesis gives: `def:rays-test-curve`(3) requires merely
`∫_X θ^n_{Γ_{-∞}} > 0`, and "bounded" in ch52 constrains the parameter range,
not the potential.

Counterexample. `X = P¹`, `L = O(1)`, `V = 1`; let `φ = P_θ[½log|z−p|²]`, a
model potential of mass `½`, and take `Γ_τ ≡ φ` for `τ < 0` with
`Γ_max = 0`. Every hypothesis holds. Then `DH_Γ = ½δ_0` of mass `½ ≠ V`, and
ch64's formula returns `∫_{−∞}^0(½ − 1)dτ = −∞` where ch55's returns `0`. The
two do not merely differ; ch64's diverges.

Nothing downstream breaks — every `Γ` actually used comes from a linearly
bounded filtration, where `eq:rf-linear-bounds` forces `Γ_{−∞} = V_θ` — but
the theorem as stated was false. Corrected in all three places, with the
full-mass condition named.

### B.2 ch68 `eq:ytd-j-divisor` — a divergent integral

`j(F) = ∫_0^{+∞}(V − vol(L − xF))dx` diverges for every `F`: past the
pseudoeffective threshold the integrand is `V > 0`, not `0`. The trailing
clause "with the integral effectively cut off at the pseudoeffective
threshold" is true of the *preceding* display, where the integrand is
`vol(L − xF)` and does vanish; it does not transfer. The cut-off must be
imposed, and now is.

### B.3 ch65 `thm:rf-commutativity` — a false claim inside a proof

"on those both sides take the value `−∞`, since every section entering either
expression vanishes on the support". False under the chapter's own standing
hypotheses: by `eq:rf-linear-bounds` the base ideal `a_{m,mC_-}` is trivial for
large `m`, so both sides are bounded below by `C_-` everywhere. It also
contradicts `prop:rf-fg-pl`, which says both sides are rational PL and hence
real valued, and the chapter's own `ex:rf-p1-complete`, where at the trivial
valuation supported at `p = [0:1]` both sides equal `0` — `y^m` does not vanish
at `p`. The theorem survives (divisorial determination already covers
`X^an`); the justification did not.

### B.4 ch70 — a worked example that depends on an unstated choice

"blow up the origin and then one point of the first exceptional curve". The
intersection numbers are indeed choice-independent, but `ord_{E_2}(a)` is not.
For `a = (x³, xy, y²)`: blowing up the `y = 0` direction gives (in `x = cd`,
`y = cd²`) `ord_{E_2}(x) = 1`, `ord_{E_2}(y) = 2`, hence `ord_{E_2}(a) = 3`,
`A = 2E_1 + 3E_2`, and the stated two-atom measure. Blowing up a general point
gives `ord_{E_2}(x) = ord_{E_2}(y) = 1`, `ord_{E_2}(a) = 2`, `A = 2E_1 + 2E_2`,
and `(−A)·E_2 = 0` — a **single** atom `2δ_{v_{E_1}}`, which collapses the
argument the example exists to make. The point is now named.

### B.5 ch67 `prop:functor-scaling-ledger`(3) — the ledger contradicts itself

The factor `m` is attached to "when both metrics are expressed with the same
normalization `v(s) = 1`". But item (1) of the same proposition says the two
agree in one fixed normalization, and expressing both in `v(s) = 1` multiplies
both by `m`, which a degree-one homogeneous functional preserves — so the
clause asserts `X = mX`. The factor appears only when each configuration is
read with its own base coordinate normalized to one. Corrected.

### B.6 ch52 `ex:rays-hyperplane-test-curve` — a singularity that is not there

"analytic singularities … of coefficient `τ` along `H` and `1−τ` at the point
`P_0 = [1:0:⋯:0]`". `P_0` has `a_0 = 1 > τ`, so it lies in the region
`{a_0 > τ}` where the level vanishes identically — there is no singularity
there at all. The true statement is stronger and simpler: `Γ_τ − τψ` is
bounded (it is `(1−τ)log(1−a_0) + H_2(τ)` where `1−a_0 > 1−τ > 0`, and
`−τ log a_0` where `a_0 > τ > 0`), so the only singularity is coefficient `τ`
along `H`. That is also what the mass computation `M_θ(Γ_τ) = (1−τ)^n` needs.

---

## C. Invalid arguments, wrong citations, and overclaims

### C.1 ch51 `prop:ch51-vtheta-bounded-iff` — the converse proof cannot work

The converse deduces a uniform *lower* bound from "the uniform bound on
`sup_X` and the sub-mean-value inequality". The sub-mean-value inequality
bounds a psh function *above* by its spherical means; it never yields a lower
bound, and an `L¹`-limit of normalized `θ`-psh functions is only `θ`-psh, not
bounded. The statement may also be too strong — nefness gives boundedness of
`V_{θ+εω}` for each `ε`, and `V_θ` is the *decreasing* limit, exactly what
`warn:ch51-lelong-decreasing` warns about. Weakened to what is proved (bounded
⟹ nef) plus the sufficient condition the chapter actually uses (a smooth
semipositive representative, in particular a nonnegative combination of
semiample classes, which covers both call sites).

### C.2 ch51 — nonpluripolar local finiteness assumes `θ_j ≥ 0`

`max{φ_j, −k}` is `θ_j`-psh only when `θ_j ≥ 0`, since locally the second
entry of `max{g_j + φ_j, g_j − k}` is psh only then. The standing hypothesis
is merely that `θ_j` is smooth closed real `(1,1)`, and the chapter's headline
`ex:ch51-blowup-mass` uses a non-semipositive `θ`. `sec:appH-npp` flags exactly
this trap. Repaired by truncating in dominating Kähler classes.

### C.3 ch51 — two citations to a colliding label

`itm:ch51-lc:convex` is "`ν((1−t)φ + tψ) = (1−t)ν(φ) + tν(ψ)`", about convex
*combinations of potentials*. It is cited twice for steps needing convexity of
the spherical mean plus `λ'_φ ≥ ν` (`prop:ch51-lelong-three`), and once also
additivity (`itm:ch51-lc:sum`). Both claims are true; both pointers were wrong,
and the near-collision `lc:convex` / `lelong:convex` makes it a live trap for a
reader checking the Skoda endpoint.

### C.4 ch51 — a positivity hierarchy that refutes itself

"These four conditions are strictly decreasing in strength" followed
immediately by "a nef class … need not be big; a big class need not be nef".
Nef and big are incomparable, so the four form a partial order, not a chain —
which is the whole point of the chapter's two examples.

### C.5 ch52 `def:rays-test-curve`(2) — a terminology collision with mathematical bite

"every level is model: `P_θ[Γ_τ] = Γ_τ`". ch51 reserves *model potential* for
the positive-mass case and repeats the reservation in a warning and in its
dictionary. Read with that meaning, clause (2) imposes positive mass at every
interior level, which makes `lem:rays-test-positive-levels` vacuous and
destroys the design the chapter is built on — positivity at `Γ_{−∞}` only,
interior levels deduced from concavity. Restated as the bare fixed-point
equation with the reservation spelled out.

### C.6 ch66 — an inference from a seminorm condition that excludes nothing

The passage rejecting Laurent series argues that inverting `t` forces
`|t|_x = r` and so puts the spectrum "over the circle `{|t| = r}`, leaving no
room for the complex points with `|t| < r`". But by `eq:hybrid-lambda` the
Archimedean point with parameter `t` carries `|·|_∞^{λ(t)}` with
`λ(t) = log r/log|t|`, so `|t|_x = |t|_∞^{λ(t)} = r` at **every** point of the
hybrid base, the centre included. The disc coordinate is the complex parameter,
not the seminorm value, and the stated inference excludes nothing. This is a
normalization-seam error in the chapter written to police that seam. The false
inference is removed and the seam stated explicitly; which algebra the source
uses is left to a check against `BJ17Hybrid`/`Favre20Hybrid` (see §D).

### C.7 ch66 — `λ(t)` silently redefined inside a proof

`λ(t)` is fixed globally as `log r/log|t|`; the volume-forms proof redefines it
locally as `(log|t|^{-1})^{-1}`, differing by the factor `−log r`. The proof is
internally consistent, but this is the one symbol carrying the
Archimedean/non-Archimedean conversion. Renamed `ε(t)`.

### C.8 ch66 — "arbitrary Banach ring"

`thm:p171-full-assembly` and every fragment supporting it assume an
**integral** Banach ring, and the subsection is headed "Continuity over
integral Banach bases", yet the remark advertises "an arbitrary Banach ring"
and "in its stated generality". Qualified.

### C.9 ch67 — a projective-only citation used in a Kähler chapter

`prop:va-i-equivalence` is stated in ch56 under "Throughout, `X` is a connected
projective manifold over **C**"; ch67's standing hypothesis is "connected
compact Kähler manifolds". The equivalence does transfer — its proof uses only
the valuative characterization of multiplier ideals and strong openness, both
local — but the citation as written did not cover the use. Noted in place.

### C.10 ch67 — a diagram arrow of the wrong type

In `eq:functor-trace-diagram` the dashed "literal restriction" arrow used `dr`,
landing in `QPSH(Ỹ)^N`, a space of *sequences*; restriction of a single
function lands in the bottom node `QPSH(Ỹ)/∼_P`. Changed to `ddr`.

### C.11 ch65 — a stale boundary item

Boundary item 2 says the outer maximal envelope is irremovable in a big class
because RWN's ample theorem does not remove it. `thm:pseff-filtration-maximality`
(ch71) does remove it, with no finite-generation hypothesis, on the strict
interior — and ch72 records that as settled. Updated.

### C.12 ch69 — a count and a citation

The chapter announces "eight outcomes" but proves a ninth,
`prop:verified-lci-current-slice`, with a full proof; it was in neither the
list nor the closed ledger in `rem:verified-read-ledger`. Added to both. And
`Cao14` is cited as "Definitions 3–4" once against "Definitions 2–3" twice
elsewhere (including this chapter's own source notes); made consistent, pending
a check against the source.

---

## D. Reported but NOT applied

- **ch52 / ch53, increasing continuity of the `I`-envelope** (UNCERTAIN). The
  `−∞` level of an `I`-model test curve is said to be `I`-model "by increasing
  continuity of the `I`-envelope", used in three places. That amounts to
  `P_θ[⋁*φ_i]_I = ⋁*P_θ[φ_i]_I`. ch51 supplies only `≤`
  (`lem:ch51-lelong-increasing` plus `prop:ch51-i-calculus`(increasing)); the
  reverse is the maximality being asserted. No counterexample was found. It
  should be stated as an import from `DXZ23`/`Xia23Operations` rather than
  deduced — but that is the author's call, since it may be provable in place.
- **ch53, three "continuity of `I`-model volumes" appeals** — all decreasing-net
  statements of the kind `warn:ch51-continuity-rules` forbids asserting without
  a theorem. One (`ex:tna-boundary-class`) can be rescued by squeezing; the
  other two need a citation.
- **ch51 `prop:ch51-mass-inequalities`(nef)** — the argument gives only
  `vol({θ}) ≤ ∫{θ}^n`; the reverse, which is what fails for big non-nef
  classes, is not supplied. The conclusion is true. Interacts with C.1, so both
  should be settled together.
- **ch66, which algebra** — the Laurent-vs-power-series question needs a check
  against `BJ17Hybrid`/`Favre20Hybrid`. The reviewer's own computation suggests
  the power-series algebra admits extra Archimedean points over the centre,
  which the next paragraph forbids, and that inverting `t` cuts the spectrum
  down to exactly the hybrid disc — i.e. the opposite of what the removed
  sentence claimed. Not asserted here.
- **ch71 `thm:p143-mp-section`** — the divisorial equality is established only
  at nonzero rational multiples of divisorial orders, while the theorem it
  invokes needs it on all of `X^divis`, which contains `v_triv`. The step is
  true and short (the levelwise infimum commutes with the endpoint for a
  decreasing net of usc functions on a compact space) but is not stated;
  `cor:p143-all-point-kahler-comparison` does treat `v = 0` explicitly, so the
  omission is an asymmetry rather than a convention. Also a compressed
  justification and an `X`-vs-`X^Berk` slip in that corollary.
- **ch68 dated-claims ledger** — narrower than ch72's on the same cutoff
  (ch72 also records `DarvasZhang25YTD` and `BJ25WeightedYTD`). Editorial.
- **ch70** — one terse step in `thm:local-generalized-lelong-separation`
  implicitly uses the relative Néron–Severi decomposition; correct, but a
  reader at `n ≥ 4` must supply it.

---

## E. Verification

`editorial/tools/refcheck.py` after every batch: 282 files in the build
closure, 10,979 labels, **0 multiply-defined, 0 dangling**; structure clean
except the known ch71 tag gap 71.33–71.35 (work in progress). Manual `\tag{}`
sequences in ch66, ch67, ch68 and ch69 were checked complete and in order
before editing, and no edit inserted a numbered display.

**Not compile-verified.** Run
`latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex` natively.
