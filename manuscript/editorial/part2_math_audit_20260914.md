# Mathematical audit — Part 2 (Chapters 10–19) and conventions sweep

Date: 2026-09-14
Scope: chs 10, 15, 16, 17, 18, 19; plus convention-consistency corrections
landing in chs 20, 25, 26, 28, 29, 39.

Every item below was re-derived from first principles before the edit was
made; two candidate findings were rejected on re-derivation and are recorded
at the end so they are not raised again.

---

## A. Corrections applied

### A.1 ch10 — `ex:ch10-unbalanced` (open vs closed half-plane)

The text asserted that rays in the *same* half-plane cannot form a balanced
one-cycle with positive weights. As stated this is false: the two rays
`R_{\geq 0}(1,0)` and `R_{\geq 0}(-1,0)` with unit weights *are* balanced,
and they lie in the closed half-plane `{x_2 \geq 0}`. The hypothesis needed
is an **open** half-plane, where pairing with the defining covector `m`
gives `\langle m, \sum_k m_k u_k\rangle > 0`, contradicting balancing.
Corrected, with the closed-half-plane witness supplied. The follow-on
sentence "Two rays pointing in the same direction…" was retitled "Rays
contained in an open half-plane…".

### A.2 ch10 — affine span of a cone

"Its affine span is `x_0 + N_{\sigma,R}`" — the antecedent of "its" was the
preceding lattice, not the cone. Rewritten to name `\sigma` explicitly.

### A.3 ch10 — "both fail without balancing"

The stable-intersection statement has two clauses (support inclusion and the
multiplicity count). Only the count needs balancing; the support inclusion is
formal, since the stable weight formula puts weight only on cells contained
in `\sigma \cap \sigma'`. The claim that "both fail" was corrected and the
formal reason for the surviving clause given.

### A.4 ch10 — Stokes and orientation reversal

The text said orientation reversal flips both boundary terms, so the identity
is preserved. That is not the mechanism: the traces are built from the
outward primitive normals `n_{\sigma,\tau}`, which are geometric, and both
integrals are unsigned (`lem:ch11-orientation-drops-out`). Nothing changes
sign; the induced endpoint orientations flip but enter neither integral.
Rewritten accordingly, and tied back to the orientation-blindness of the
`(n,n)`-form integral established two paragraphs earlier.

### A.5 ch15 — sign of the vertex atom in the unbalanced case

`lem:ch15-vertex-atom` recorded the extra term as
`-u(p)\langle d\Psi(p), \mathbf N(p)\rangle \delta_p`. Integrating by parts
edge by edge, the boundary contribution at `p` is

    \sum_\sigma m_\sigma d_\sigma u(p)\,\Psi(p) - u(p)\sum_\sigma m_\sigma d_\sigma\Psi(p),

and `\sum_\sigma m_\sigma d_\sigma\Psi(p) = \langle d\Psi(p), \sum_\sigma
m_\sigma u_{\sigma/p}\rangle = -\langle d\Psi(p), \mathbf N(p)\rangle`
because `\mathbf N(p) := -\sum_\sigma m_\sigma u_{\sigma/p}` by
`def:ch11-defect`. The two minus signs cancel: the extra term is
**`+u(p)\langle d\Psi(p), \mathbf N(p)\rangle \delta_p`**. Corrected, with
the one-line derivation inserted so the sign is auditable.

### A.6 ch15 — tangent-direction count on the quartic

"There are thus three tangent directions at each of `\theta = 1,2,3,4`" is
wrong twice over: at a type-II point there are infinitely many tangent
directions (one per `\mathbf P^1(\widetilde K)`), and the number carrying a
*nonzero* outgoing slope is three at `\theta = 1,2,3` but two at `\theta = 4`.
Restated in terms of nonzero slopes, with the branching reference kept for
the genuine tangent-direction count.

### A.7 ch16 — bidegree in `prop:ch16-skeletal-first-derivative`

For `T` of bidimension `(p,p)`, the current `d'(uT)` has bidimension
`(p-1,p)` and therefore pairs with forms of bidegree `(p-1,p)`. With
`\rho` of type `(r,0)` this forces `\omega` of type `(p-r-1,p)`, not
`(p-r,p)`, and `0 \leq r \leq p-1`. (Check: the right-hand side
`d'u \wedge \rho \wedge \omega` then has type `(p,p)`, which is what
integrates over the `p`-calibrated `P^T_f`; and `r = 0` recovers the stated
special case `d'(uT) = T \wedge d'u`.) Corrected, with the bidegree
bookkeeping stated inline.

### A.8 ch16 — illegitimate use of `prop:ch16-hierarchy-status` for a uniform limit

`cor:ch16-max-psh` took a uniform limit of stage-`\alpha` functions and
placed it at stage `\sup(1,\alpha)` by citing the hierarchy-status
proposition. That proposition is only the identity
`CPsh_{X,\alpha} = C^0_X \cap Psh_{X,\alpha}`; it says nothing about uniform
limits, and the asserted conclusion would collapse precisely the hierarchy
that `prob:frontier-cld-hierarchy` leaves open. Replaced by the diagonal
argument: approximate each `u_i` by a decreasing net at stage `\beta` and
`g` by a decreasing uniform net of smooth convex coordinatewise-nondecreasing
functions, then invoke stability under decreasing limits.

### A.9 ch17 — direction of `\rho` in the Levine sketch

The text had `\rho : L_a \to L_b` with `\log\|\rho\|^{-1} = g^*h`. With
`h = \log(\max_i|x_i| / \max_{i<p}|x_i|)` one computes
`g^*h = \log\|x_j\|_b - \log\|x_j\|_a`, so a morphism `L_a \to L_b` would
have `\log\|\rho\| = +g^*h`, not `-g^*h`. The correct direction is
`\rho : L_b \to L_a`; equivalently `L_a = L_b \otimes \cO(E)`, which is the
standard identity `g^*\cO(1) = (f')^*\cO(1) + E` on the blowup of a linear
centre. Corrected, with the reason the reverse direction has no nonzero
section.

### A.10 ch17 — inverted inequality in the formal-metric criterion

`|a_i g^{-1}| \leq r/c` was written where `|a_i g| \leq r/c` is meant.

### A.11 ch17 — sign in `prop:ch17-mass-independent`

The proof defined `u_i` by `\log\|s\| = u_i + \log\|s\|'` and then quoted
`prop:cld-c1-metric-change` as giving
`c_1(\overline L_i) = d'd'' u_i + c_1(\overline L_i')`. With that definition
`\|\cdot\| = e^{u_i}\|\cdot\|'`, so the proposition gives
`c_1(\overline L_i) = c_1(\overline L_i') - d'd'' u_i`. Repaired by flipping
the defining equation to `\log\|s\|' = u_i + \log\|s\|`, which restores the
quoted identity verbatim and leaves the rest of the proof untouched.

Separately, the multilinear expansion listed the alternatives for `T_i` as
"`c_1(\overline L_i)` or `d'd'' u_i`"; expanding
`\bigwedge(c_1(\overline L_i') + d'd'' u_i)` the non-correction factor is the
**primed** class. Corrected.

### A.12 ch18 — Euclidean asymmetry in `ex:ch18-positivity-four-cases`

Three of the computations silently treated the three rays of
`eq:ch18-gauge-rays` symmetrically. They are not symmetric for the Euclidean
norm: `|v_3|^2 = 2` while `|v_1|^2 = |v_2|^2 = 1`. The three affected
displays now read

    d'd''[\varphi] = -2\,ds_1 - 2\,ds_2 - 4\,ds_3,
    d'd''[\varphi] = 3\delta_0 - \epsilon(2\,ds_1 + 2\,ds_2 + 4\,ds_3),
    3 - (4 + 2\sqrt2)\epsilon R,

the last being the correct total mass on a ball of radius `R`.

### A.13 ch18 — basis of very affine opens

The stated reason ("a principal open of an affine variety in `\mathbf A^N`
embeds in `\mathbf G_m^{N+1}`") does not produce a *basis*, and inverting a
single function genuinely fails: `\mathbf G_m \times \mathbf A^1` has
`\cO^\times/K^\times \cong \mathbf Z` generated by `x_1`, so its canonical
map to a torus collapses every fibre `\{c\} \times \mathbf A^1` and it admits
no closed immersion into a split torus at all. Replaced by the correct
construction: invert all of `x_i - c_i` for a `c` avoiding the coordinates of
the given point (possible since `K` is infinite).

### A.14 ch19, ch20 — analytic vs lattice edge length

This is the convention error the cross-chapter sweep turned up, including one
instance I introduced myself in an earlier wave.

The two lengths on an edge of a dual complex with multiplicities `b_i, b_j`
are

    analytic (Laplacian) length  = 1/(b_i b_j),
    integral-affine lattice length = 1/lcm(b_i, b_j),

so that **lattice = gcd × analytic**: the lattice length is the *larger* of
the two, and they agree exactly when `gcd(b_i,b_j) = 1`. `rem:ch20-...` had
been left asserting the reverse ("exceeds the lattice length … by the factor
gcd"). Corrected in ch20, and the distinction spelled out in ch19 where the
chapter's examples all have `b = 1` and the two therefore coincide.

Verified twice independently on an explicit `\mathbf P^1` model with
`gcd = 2` (slope formula against `f = T^2 - \tilde c \pi`).

### A.15 chs 25, 26, 28, 29, 39 — cofinality and PSH2

- Four occurrences of "semistable model/skeleton" in contexts requiring a
  *cofinal* system were changed to SNC. Semistable models are **not** cofinal
  over a fixed complete discretely valued field; SNC models are (char 0).
  Affected: `ch25` (quasimonomial points as a union of skeleta), `ch26`
  (skeleton of "some" model), `ch28` (cofinal system of skeleta), `ch29`
  (choice of a model whose skeleton contains a given one).
- `ch39`'s gloss of PSH2 quoted the fixed-class axiom. PSH2 is the
  **varying-class** decreasing-limit axiom
  (`lem:ch39-closure-any-class`(5) / `thm:bj-basic-closure`(5)); the
  fixed-class statement (4) is its specialization `\theta_j = \theta`. The
  gloss now states the varying-class form and names the specialization.

---

## B. Candidate findings re-derived and REJECTED

**B.1 ch50, "spurious `+X_0`".** Rejected. `ch50` defines
`K^{\log} = K + B_X + X_{0,\mathrm{red}}`, so
`-K^{\log} + X_0 = \mu^* pr_1^* \cO(2) - E = L_1` is correct as written.

**B.2 A base-change heuristic giving analytic edge length `1/\mathrm{lcm}`.**
Rejected. On the explicit model with `b_i = b_j = 2`, the slope formula
applied to `f = T^2 - \tilde c\pi` forces `1/4 = 1/(b_i b_j)`, not
`1/2 = 1/\mathrm{lcm}`.

---

## C. Verification performed

- All touched files: environment balance, brace delta, math-delimiter
  counts, `\tag{}` sequence integrity, duplicate labels — clean.
- Reference sweep against the full label set of `parts/`, `appendices/`,
  `frontmatter/`, `style/` **and `editorial/`** — zero dangling targets
  (see §E).
- **Not compile-verified.** The audit VM's TeX installation lacks `newtx`
  and has no network. Run
  `latexmk -pdf -interaction=nonstopmode -halt-on-error book.tex`
  natively before committing.

---

## D. Second ch18 pass (six further items)

### D.1 `cor:ch18-delta-total-mass` — the "alternatively" argument

The alternative proof offered inside the delta-calculus was wrong in its
premise and overstated in its conclusion. It opened "the mass is
`∫ d'd''[φ₁] ∧ ⋯`", which holds only when the `L_i` are trivial: in general
`c_1^δ(L̄_i)` carries a cycle part besides `d'd''[φ_i]`. And it claimed to
deliver the intersection number, whereas the telescoping-plus-Stokes argument
delivers only that the mass is the *same* for all metrics; the *value*
requires evaluating one metric, which is `thm:ch17-degree`. Rewritten:
two metrics on `L_i` differ by `d'd''[u_i]` for a global R-PL `u_i`, the
multilinear expansion leaves a sum of terms each with at least one such
factor, each is `d'd''` of a compactly supported delta-form (the remaining
factors being closed), and `prop:ch18-delta-integration`(stokes) kills it on
the boundaryless `X^an`. This is the same argument as
`prop:ch17-mass-independent` (corrected in A.11 above), and the record now
says so.

### D.2 `thm:harmonic-balancing` — a misapplied citation

The proof formed the graph tropicalization `(g,h)` of an ordinary moment map
`g` against the harmonic `h`, then asserted the graph "is balanced away from
the analytic boundary by `thm:analytic-tropical-balancing`". That theorem is
about *ordinary* moment maps, and `(g,h)` is not one — the coordinates `h_j`
are precisely the ones that are not of the form `-log|f_j|`, which is the
content of `ex:ch18-harmonic-not-smooth`. The citation also makes the proof
look circular, since the next paragraph then handles the `h_j` separately.
Repaired: the cited theorem supplies the vanishing of the **`g`-component**
of the Stokes defect only; the `h`-component is what harmonicity kills, as
the following paragraph does.

### D.3 `ex:ch18-harmonic-disc` — the example does not satisfy its own hypotheses

`W = {|T| ≤ 1}`, `h = -log|T|` was called "an ordinary and hence harmonic
tropicalization". It is neither. `T` is not invertible on the closed unit
disc, so `h` is not an ordinary tropicalization in the sense of
`ex:ch18-harmonic-ordinary`; and `h(0) = +∞`, so `h` is not a map `W → R^r`
at all, which is what `thm:harmonic-balancing` requires. Its stated image
`[0,+∞]` is correspondingly not a polyhedron.

Replaced by the closed annulus `W = {|π| ≤ |T| ≤ 1}`, where `T` *is* a unit.
The image is the segment `[0,1]` (with `v_K(π)=1`) of canonical weight `1`;
the balancing sum is `+1` at `{0}` and `-1` at `{1}`; both endpoints are
`h(∂W)`, the image of the Shilov boundary — the Gauss points of radii `1`
and `|π|` — so both are excluded by the theorem, and every interior point
balances. The example now also records why the disc fails, since it is the
first thing one reaches for. The dictionary row and
`rem:ch18-balancing-boundary`'s "closed disc" were updated to match; the
label `ex:ch18-harmonic-disc` was kept so no cross-reference breaks.

### D.4 `ex:ch18-harmonic-abelian` — fundamental domain vs quotient torus

The local coordinates `-log|z_i|` are defined modulo `trop(Λ)`, so they patch
into a map to the real torus `N_R/trop(Λ)` — not onto a fundamental domain,
which is a choice of representatives admitting no continuous lift of the
patched map. This also contradicted `thm:abelian-harmonic-tropicalization`
itself (ch19), which states that `trop_A` is the harmonic tropicalization.
The follow-on claim that balancing is automatic "the image being an open
subset of `R^g`" was the same error: the correct reason is that the quotient
torus is **compact without boundary**, so no face is excluded. Corrected,
with a note that the target is not literally an `R^r` and the theorem is
therefore applied locally, on neighbourhoods where a lift exists.

### D.5 `ex:ch18-compare-toric` — Legendre transform vs recession function

The text said `ψ`'s *Legendre transform* is the support function of `P_L`.
It is the **recession function** that is the support function; the Legendre
transform `ψ^∨(m) = inf_x(⟨m,x⟩ − ψ(x))` is a concave function on `M_R`
whose finiteness locus is `P_L`, and it records the whole metric rather than
just its asymptotics. Corrected, and tied to ch19's own observation
(following `eq:toric-metric-potential`) that it is the prescribed *boundary
growth* of `φ` that sees `L`.

### D.6 `thm:gr-pl-curve-test` — the curve test needs scalar extensions

The statement quantified over Zariski-closed analytic curves `C ⊂ U` over
`K`, but the proof's converse direction produces its test curve only "after
shrinking a strict neighborhood and if necessary making an analytic scalar
extension". The criterion as stated is therefore not what the argument
establishes. Added the quantifier over complete analytic extensions `K'/K`
with `C ⊂ U_{K'}`, noted why it is needed, and tied it to the
base-change-stable shape of the "classically psh" definition that follows
(which was unlabelled and has been given `def:ch18-classically-psh`).

---

## E. Correction to an earlier finding of my own

Previous waves in this project reported roughly 149 dangling `\Cref` targets
of the `p0xx`/`p21p3` families and recommended leaving them. That was **my
error, not the manuscript's**: my reference checker globbed only `parts/`,
`appendices/`, `frontmatter/` and `style/` when collecting `\label`s, and
those targets are defined in `editorial/` sources that the chapters
`\input` directly (e.g. `ch17` inputs
`editorial/rethlas_packets_20260830/...`, `ch19` inputs
`editorial/solver_dossiers_20260911/...`).

Re-checked properly, by resolving the actual input graph from `book.tex`
rather than globbing — following `\input`, `\include` and the book's own
`\draftinclude` macro transitively. The result for the **whole manuscript**:

    files in build closure:      282
    labels in closure:        10,979
    multiply-defined labels:       0
    dangling references:           0

So the manuscript's cross-referencing is clean end to end, and the earlier
records' "~149 pre-existing dangling refs" notes should be disregarded. The
resolver is saved as `editorial/tools/refcheck.py`; note that globbing
`editorial/**` is *too permissive* in the other direction, since not every
packet there is inputted — only the input graph gives the right answer.
