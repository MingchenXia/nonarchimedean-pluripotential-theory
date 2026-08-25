# Dossier: residual YTD questions after the 2025–2026 preprints

Solver stage, run 15 August 2026. Literature cutoff 15 August 2026. Scope fixed by
`/home/claude/work/refs/post2025_ytd_residuals.md` (binding). Book environment:
`ch72_major_open_problems.tex`, §"Hybrid entropy slopes and the remaining compact-Kähler YTD frontier"
(Problem `prob:frontier-hybrid-ytd`) and the PS23 Question 4.9 Banach-family
problem.  The Favre--Pille-Schneider endpoint problem and its former
zero-supremum normalized replacement were both retired on 25 August after
the production-verified counterexample.

## 0. Sources, quarantine, firewall

**Fetch log (one attempt each, 15 Aug 2026).** arXiv:2509.15173 (Darvas–Zhang) abs page fetched:
title "A YTD correspondence for constant scalar curvature metrics", authors Darvas, Zhang, v1
18 Sep 2025 / v2 3 Nov 2025 — consistent with the packet; no content beyond the abstract obtained.
arXiv:2509.15016 (Boucksom–Jonsson) partially readable (weighted cscK/extremal on polarized
projective manifolds confirmed; no theorem text). arXiv:2605.30063 (Trusiani) unreadable. All three
are used **exactly at packet scope** as dated preprint claims:

- **BJ25** = arXiv:2509.15016v1 (18 Sep 2025): polarized projective weighted-cscK/b-\(K\)-polystability statements. *(dated claim)*
- **DZ25** = arXiv:2509.15173v2 (3 Nov 2025): \(K^\beta\) and log-discrepancy-model correspondences, incl. Thms 1.6/10.4. *(dated claim)*
- **Tru26** = arXiv:2605.30063v1 (28 May 2026): special Fujita approximation, equivariant entropy regularization, smooth polarized projective YTD (Thm A), Corollary B signature equivalences. *(dated claim)*
- **MPWN25** = Mesquita-Piccione–Witt Nyström, arXiv:2509.09442v1 (11 Sep 2025): full text locally available; packet grants Theorems A and B. *(dated claim, text-verified quotations below)*
- **MP24** = Mesquita-Piccione, arXiv:2409.06221v2, to appear Adv. Math.: Theorem A (uniform K-stability over \(\mathcal E^1\) \(\Rightarrow\) unique cscK, compact Kähler), Theorem B (\(X^{\mathrm{div}}\) dense in \(X^\beth\)). *(accepted; treated as published)*

No nonprojective, singular, equivariant, or klt statement is inferred from any of BJ25/DZ25/Tru26.

**Erratum firewall.** BHJ 2022 erratum binding: BHJ19 Theorem 5.6, Theorem 5.4, Theorem C,
Corollaries D–E are **never used**. All slope/intersection formulas used below are routed through
MPWN25 Thm 9.1.1 (proved in-text via positive intersection classes, transcendental), Li,
Ann. Sci. ÉNS 55 (2022) 1529–1574, Sjöström Dyrefelt, J. Geom. Anal. 28 (2018) 2927–2960, and
Dervan–Ross, Math. Res. Lett. 24 (2017) 689–739. Firewall audit in §6.

**Notation** (MPWN25 §§2.4, 10). \(X\) compact Kähler manifold, \(n=\dim X\), \(\alpha\) Kähler,
\(V=\alpha^n\). \(\mathcal M^{\mathrm{div}}\) = divisorial measures \(\mu=\sum_i \xi_i\delta_{v_i}\),
\(v_i\in X^{\mathrm{div}}\). Energy of a measure
\(\mathrm E^\vee_A(\mu)=\sup\{\mathrm E_A(\varphi)-\int\varphi\,d\mu:\varphi\in\mathcal E^1_A\}\);
entropy \(\mathrm{Ent}(\mu)=\int (A_{X\times\mathbb P^1}-1)\,d\mu\), so
\(\mathrm{Ent}(\mu_\xi)=\sum_i\xi_i A_X(F_i)\); beta invariant
\(\beta_A(\mu)=\mathrm{Ent}(\mu)+\nabla_{K_X}\mathrm E^\vee_A(\mu)\),
\(\nabla_{K_X}\mathrm E^\vee_A(\mu)=\tfrac{d}{dt}\big|_{t=0}\mathrm E^\vee_{A+tK_X}(\mu)\)
(differentiability: Boucksom–Jonsson, arXiv:2307.01697 [BJ23a], preprint). "Uniform
b-\(K\)-stability" below always means \(\inf_{\mu\in\mathcal M^{\mathrm{div}}}\beta_A(\mu)/\mathrm E^\vee_A(\mu)>0\),
which by MPWN25 Thm 10.0.4 (granted, dated) is equivalent to
\(\mathrm M_A\ge\delta \mathrm J_A\) on \(\mathcal E^1_A\).

---

## 1. Status table

| # | Residual (source) | Status |
|---|---|---|
| R1 | Direct algebraic proof: b-\(K\)-polystability \(\Leftrightarrow\) uniform b-\(K\)-polystability (BJ25 Q&FR) | **OPEN** (conditional route (A)–(C) in §4; Fano-proportional subcase PUBLISHED/RESOLVED) |
| R2 | Test uniform b-\(K\)-polystability on divisorial measures with support cardinality bounded in \(\dim X\) (BJ25 Q&FR) | **OPEN** after attempt; **CONDITIONAL-REDUCTION proved here** (support \(\le 1\) under hypothesis \((\ast)\); \((\ast)\) proved for \(K_X\equiv c\alpha\), \(c\le 0\); \((\ast)\) fails for \(c>0\)) |
| R3 | Algebraic proofs of equivariance implications now obtained via cscK metrics (BJ25 Q&FR) | **OPEN** |
| R4 | Extend the theory to polarized klt pairs and nonprojective Kähler (BJ25 Q&FR) | **OPEN** (smooth-Kähler, non-equivariant, uniform-models\(\Rightarrow\)cscK direction RESOLVED as dated claims MPWN25/MP24; klt and equivariant parts fully open) |
| R5 | Regularize log-discrepancy-model rays by test configurations strongly enough to recover strong uniform YTD (DZ25 Rem. 1.7) | **OPEN** (a conditional discharge via Tru26 entropy regularization is *plausible* but unverifiable at packet scope) |
| R6 | Extend log-discrepancy-model correspondence equivariantly to transcendental classes with nontrivial automorphisms (DZ25) | **OPEN** |
| B1 | Book: explicit normalization-preserving comparison maps between the analytic/NA signatures | **OPEN** (programme; partial bridges dated; dependency map §5.1) |
| B2 | Book: equivariant theory on singular compact Kähler spaces | **OPEN** (dependency map §5.2; published/preprint partials named) |
| B3 | Book: hybrid compactness and family Monge–Ampère continuity through degenerations | **OPEN** (dependency map §5.3) |

Trusiani's post-Corollary-B note (a direct algebraic bridge between the equivalent projective
signatures is still unavailable) is itself a dated statement of openness; it is consistent with,
and subsumed by, R1/R3/B1 above.

## 2. Justifications (one paragraph each)

**R1 — OPEN.** The packet grants (dated) that BJ25 prove their polarized projective
b-\(K\)-polystability YTD statements; through the cscK metric both b-\(K\)-polystability and its
uniform version are then equivalent to existence, hence to each other — but *through analysis*.
No algebraic proof exists at cutoff. The exact projective analogue that IS proved algebraically is
the Fano-proportional case: for log Fano pairs, K-polystability \(\Leftrightarrow\) reduced uniform
K-polystability, Liu–Xu–Zhuang, Ann. of Math. (2) 196 (2022) 507–566 (finite generation for
minimizing quasi-monomial valuations), building on Li–Xu, Ann. of Math. (2) 180 (2014) 197–232 and
Fujita, J. Reine Angew. Math. 751 (2019) / Li, Duke Math. J. 166 (2017). For general polarizations
no analogue of any of the three pillars (minimizer existence, structure of minimizers, finite
generation) is published. Sharpest conditional statement: §4.

**R2 — OPEN after attempt; partial reduction proved.** §3 proves: *if* \((\ast)\)
\(\mu\mapsto\nabla_{K_X}\mathrm E^\vee_A(\mu)\) is concave on \(\mathcal M^{\mathrm{div}}\), then
uniform b-\(K\)-stability can be tested on Dirac masses \(\delta_v\), \(v\in X^{\mathrm{div}}\)
— support cardinality \(1\), far below any \(b(\dim X)\). \((\ast)\) is proved when
\(K_X\equiv c\alpha\) with \(c\le0\) (recovering the Fujita–Li-type single-valuation testing in
the Fano-proportional and \(c_1=0\) cases), and *disproved* when \(K_X\equiv c\alpha\), \(c>0\)
(where stability is anyway automatic with \(\delta=c\)). In the genuinely non-proportional zone
\((\ast)\) is neither proved nor refuted: it *holds* in two exactly computed surface faces (one by
closed form, one numerically to \(10^{-5}\)-validated code). The Carathéodory route without
\((\ast)\) fails structurally: the only linear space through which the face-restricted functional
factors is \(N^1\) of the common log resolution, whose dimension grows with the support itself (§3.6).

**R3 — OPEN.** The equivariance implications (e.g. stability for a maximal torus implies stability,
and polystability descent statements) are, at cutoff, obtained by passing through the cscK metric
(granted, dated: BJ25, and in the Kähler \(K^\beta\) form DZ25). No algebraic proof is claimed by
any packet source. Tru26 claims *equivariant entropy regularization* (dated); even granted, the
packet forbids inferring that its proof mechanism is algebraic or that it yields the specific
equivariance implications; nothing else in scope touches them. The transcendental sources are
explicitly non-equivariant: MP24 p. 5 states Chi Li's automorphism version is "not treated in the
present paper"; MPWN25 has no group action anywhere.

**R4 — OPEN with resolved sub-piece.** Nonprojective Kähler, smooth, non-equivariant, one
direction: RESOLVED as dated claims — MPWN25 Thm A (uniform K-stability for models
\(\Rightarrow\) unique cscK in \(\alpha\); granted by packet) with MP24 Thm A as its published
engine; the converse direction cscK \(\Rightarrow\) (uniform) K-stability in the Kähler setting is
published in the non-uniform form (Sjöström Dyrefelt 2018; Dervan–Ross 2017; MP24 intro states the
coercivity \(\Rightarrow\) uniform K-stability direction from these). The *b-K/weighted formalism*
itself in the Kähler setting, the polystable/equivariant statements, and the entire polarized klt
pair extension are untouched: for klt Kähler varieties even the analytic side is only partial
(MP24 Rem. 0.0.1: coercivity \(\Rightarrow\) singular cscK for \(\mathbb Q\)-Gorenstein smoothable
[Pan–Tô–Trusiani, arXiv:2312.13653] or nef relative anticanonical resolution
[Boucksom–Jonsson–Trusiani, arXiv:2412.06096 + Pan–Tô, arXiv:2412.07968] — all preprints), "in
this generality the conjecture is completely open" (MP24, verbatim).

**R5 — OPEN.** DZ25 (dated) prove the log-discrepancy-model correspondence; their Remark 1.7 asks
for regularization of the attached rays by test configurations strong enough to recover the strong
uniform YTD formulation. Tru26 (dated) claims entropy regularization for smooth polarized
projective; *if* the DZ ray class embeds into the class of finite-energy potentials to which
Tru26's claimed regularization applies with entropy convergence, R5 would discharge in the smooth
polarized projective automorphism-relative case — but the bridging lemma requires DZ's exact ray
definitions (unfetchable) and would rest on an unverifiable dated claim; the packet's "do not
infer" rule blocks recording this as CONDITIONAL. Transcendental and singular versions are open
outright.

**R6 — OPEN.** DZ25's Kähler statement is the *unique*-cscK/\(K^\beta\) correspondence; the
equivariant transcendental extension with nontrivial automorphisms has no partial coverage in
scope: MP24/MPWN25 are non-equivariant (see R3), there is no transcendental theory of reduced
norms \(\mathrm J_T\), no transcendental Cartan/Matsushima-type NA reductivity input, and no
equivariant version of the transcendental Calabi–Yau theorem (MPWN25 §6) exists. Missing inputs
named in §5.2 overlap.

**B1, B2, B3 — OPEN.** Programmes, not single statements; graded via dependency maps §5.1–5.3
with named missing theorems. None is CONDITIONAL as a whole because in each case at least one
required input has no precise published or dated formulation.

---

## 3. Proof attempt A (residual R2): support bounds via the divisorial-measure simplex

### 3.1 Formalization

Fix a face of \(\mathcal M^{\mathrm{div}}\): prime divisors \(F_1,\dots,F_\ell\) over \(X\),
valuations \(v_i=\mathrm{ord}_{F_i}\), simplex
\(\Delta_\ell=\{\xi\in\mathbb R^\ell_{\ge0}:\sum\xi_i=1\}\ni\xi\mapsto\mu_\xi=\sum\xi_i\delta_{v_i}\).
Note \(\mathcal M^{\mathrm{div}}\) is convex and every \(\mu\) lies on the face spanned by its
atoms. Question (BJ25 Q&FR, packet item 2): is there \(b(n)\) with
\(\inf_{\mathcal M^{\mathrm{div}}}\beta_A/\mathrm E^\vee_A
=\inf_{\#\mathrm{supp}\,\mu\le b(n)}\beta_A/\mathrm E^\vee_A\)?

### 3.2 Curvature ledger of the three functionals on a face

1. **Entropy is affine.** \(\mathrm{Ent}(\mu)=\int(A_{X\times\mathbb P^1}-1)d\mu\) is the integral
   of a fixed function: linear in \(\mu\); on the face,
   \(\mathrm{Ent}(\mu_\xi)=\sum\xi_iA_X(F_i)\) (MPWN25 §10.1, using
   \(A_{X\times\mathbb P^1}(\mathrm{ord}_F)=A_X(F)+1\)). *Exact.*
2. **Energy is convex.** \(\mathrm E^\vee_A(\mu)=\sup_\varphi\{\mathrm E_A(\varphi)-\int\varphi
   d\mu\}\) is a supremum of affine functionals of \(\mu\): convex on \(\mathcal M^1\). *Exact.*
   On the face it is the explicit Legendre transform (MPWN25 Cor 10.1.3):
   \(\mathrm E^\vee_A(\mu_\xi)=g_A(\xi):=\sup_{t\in\mathbb R^\ell}\{f_A(t)-\xi\cdot t\}\), with
   \(f_A(t)=\lambda_0+V^{-1}\int_{\lambda_0}^{\infty}\big\langle\big(\alpha-\sum_i(\lambda-t_i)^+F_i\big)^n\big\rangle d\lambda\)
   (MPWN25 Thm 10.1.2).
3. **\(f_A\) is concave in \(t\)** (proved here, elementary): \(t\mapsto\varphi_t=\sup\{\varphi\in
   \mathrm{PSH}_A:\varphi(v_i)\le t_i\}\) satisfies \(\varphi_{(1-s)t^0+st^1}\ge(1-s)\varphi_{t^0}
   +s\varphi_{t^1}\) (the right side is a competitor), and \(\mathrm E_A\) is monotone and concave
   along affine segments (BJ22, Ann. Fac. Sci. Toulouse 31 (2022) 647–836, published — not a
   BHJ-firewalled source); hence \(f_A(t)=\mathrm E_A(\varphi_t)\) is concave. Consistent with 2:
   \(g_A\) convex.
4. **The pivot term has no a priori curvature.**
   \(\nabla_{K_X}\mathrm E^\vee_A(\mu)=\lim_{t\to0}t^{-1}(\mathrm E^\vee_{A+tK_X}-\mathrm E^\vee_A)(\mu)\)
   is a limit of *differences of convex* functions of \(\mu\): DC, sign of curvature undetermined.
   On a face, by the envelope identity, \(h(\xi):=\nabla_{K_X}g_A(\xi)=\partial_c|_0
   f_{A+cK_X}(t^*(\xi))\) at the dual optimizer \(t^*(\xi)\): a composition with no general
   convexity law.

### 3.3 The vertex-reduction theorem (rigorous, conditional)

**Hypothesis \((\ast)\):** \(\mu\mapsto\nabla_{K_X}\mathrm E^\vee_A(\mu)\) is concave on each
face of \(\mathcal M^{\mathrm{div}}\).

**Proposition 3.3.1.** Assume \((\ast)\). If \(\beta_A(\delta_v)\ge\delta\,\mathrm E^\vee_A(\delta_v)\)
for every \(v\in X^{\mathrm{div}}\), then \(\beta_A(\mu)\ge\delta\,\mathrm E^\vee_A(\mu)\) for every
\(\mu\in\mathcal M^{\mathrm{div}}\). Hence, under \((\ast)\), uniform b-\(K\)-stability is tested on
divisorial measures of support cardinality \(1\).

*Proof.* \(\mu=\sum\xi_i\delta_{v_i}\). Then
\(\beta_A(\mu)=\mathrm{Ent}(\mu)+\nabla_{K_X}\mathrm E^\vee_A(\mu)
\ge\sum_i\xi_i\big[\mathrm{Ent}(\delta_{v_i})+\nabla_{K_X}\mathrm E^\vee_A(\delta_{v_i})\big]
=\sum_i\xi_i\beta_A(\delta_{v_i})\ge\delta\sum_i\xi_i\mathrm E^\vee_A(\delta_{v_i})
\ge\delta\,\mathrm E^\vee_A(\mu)\),
using linearity of \(\mathrm{Ent}\), \((\ast)\), the vertex hypothesis, and convexity of
\(\mathrm E^\vee_A\). \(\square\)

Combining with MPWN25 Thm 10.0.4 (granted, dated): under \((\ast)\), uniform b-\(K\)-stability
\(\Leftrightarrow\) \(\inf_{v\in X^{\mathrm{div}}}\beta_A(\delta_v)/\mathrm E^\vee_A(\delta_v)>0\),
where \(\mathrm E^\vee_A(\delta_{\mathrm{ord}_F})=V^{-1}\int_0^{\tau_{\mathrm{psef}}}
\langle(\alpha-\lambda F)^n\rangle d\lambda\) is the transcendental \(S\)-invariant (MPWN25
(10.1.2) specialization, \(\ell=1\)).

### 3.4 Where \((\ast)\) is proved and where it fails

**Scaling identity.** \(\mathrm E_{s\alpha}(s\varphi)=s\,\mathrm E_\alpha(\varphi)\) and
\(\mathcal E^1_{s\alpha}=s\mathcal E^1_\alpha\) give \(\mathrm E^\vee_{s\alpha}(\mu)=
s\,\mathrm E^\vee_\alpha(\mu)\); hence if \(K_X\equiv c\alpha\) in \(H^{1,1}(X,\mathbb R)\),
\(\nabla_{K_X}\mathrm E^\vee_A(\mu)=c\,\mathrm E^\vee_A(\mu)\). Consequences:

- \(c<0\) (Fano, \(\alpha\propto-K_X\)): \(\nabla_{K_X}\mathrm E^\vee=-|c|\mathrm E^\vee\) is
  concave; \((\ast)\) holds; Prop 3.3.1 recovers single-valuation testing,
  \(\beta_A(\delta_v)=A(v)-|c|S(v)\)-type — the transcendental shadow of the Fujita/Li valuative
  criterion (published in the projective Fano case: Fujita, Crelle 751 (2019); Li, Duke 166 (2017)).
- \(c=0\) (\(c_1=0\)): \(\beta=\mathrm{Ent}\) is linear; \((\ast)\) trivial; support-1 testing holds
  (and stability is anyway automatic via Yau's theorem on the analytic side).
- \(c>0\) (canonically proportional): \(\nabla_{K_X}\mathrm E^\vee=c\,\mathrm E^\vee\) is
  **strictly convex** on faces wherever \(g_A''>0\) (generic), so \((\ast)\) **fails**; but then
  \(\beta_A\ge \mathrm{Ent}+c\mathrm E^\vee\ge c\,\mathrm E^\vee\) since \(A\ge0\) on
  \(X^{\mathrm{div}}\): uniform stability holds with \(\delta=c\) — the failure zone of the
  *method* is covered by trivially true *statement*. By continuity of
  \(\zeta\mapsto\mathrm E^\vee_\zeta\) (BJ23a Thm 5.5-type Lipschitz estimates, preprint — as
  imported by MPWN25 Cor 10.0.3), a neighbourhood of the ray \(\mathbb R_{>0}\alpha\) behaves
  likewise. The genuinely open zone is \(K_X\) far from \(\mathbb R\alpha\).

**Exact computations in the non-proportional zone.** Two 2-point faces, computed twice
(closed form by hand; independent numerics validated to \(5\) decimals against the closed form):

1. \(X=\mathbb P^1\times\mathbb P^1\), \(\alpha=H_1+2H_2\), face \(=\) one fiber of each ruling,
   \(K_X=-2H_1-2H_2\not\propto\alpha\). Closed form (derived from Thm 10.1.2 by direct
   integration; three chamber regions):
   \(h(\xi)=-2\xi^{3/2}+2\xi-1\) on \([0,\tfrac14]\); \(-\tfrac{15}{16}+\xi-\xi^2\) on
   \([\tfrac14,\tfrac34]\); \(-2(1-\xi)^{3/2}+2(1-\xi)-1\) on \([\tfrac34,1]\). \(C^1\), and
   **concave** throughout.
2. \(X=\mathrm{Bl}_p\mathbb P^2\), \(\alpha=2H-E\), face \(=\{\mathrm{ord}_E,
   \mathrm{ord}_{\tilde L}\}\) (\(\tilde L\) = strict transform of a line through \(p\)),
   \(K_X=-3H+E\); the class path crosses a Zariski chamber wall. Numerically (validated code):
   \(h\) **concave** (max second difference \(<0\) on a 49-point grid), \(\beta_A(\mu_\xi)=1+h(\xi)\)
   **negative near both vertices** and the face infimum of \(\beta/\mathrm E^\vee\) attained at a
   vertex. Consistency check: \(\mathrm{Bl}_p\mathbb P^2\) has non-reductive automorphism group,
   hence no cscK metric in any class (Matsushima–Lichnerowicz), and indeed the *vertex* test
   already destabilizes.

### 3.5 FIRST unsupported implication (recorded)

The attempted general proof runs: (i) \(\beta=\)affine\(+\nabla_{K_X}\mathrm E^\vee\); (ii)
**"\(\nabla_{K_X}\mathrm E^\vee\) is concave on \(\mathcal M^{\mathrm{div}}\) whenever \((X,\alpha)\)
is b-\(K\)-semistable"**; (iii) vertex reduction. Step (ii) is the first unsupported implication:
it is proved only for \(K_X\equiv c\alpha, c\le0\), verified in two non-proportional faces, and
*false* for \(c>0\). No counterexample within the semistable zone is known to me; no proof either.
Weakenings tried and failed: quasiconcavity of \(\beta-\delta\mathrm E^\vee\) (would still give
vertex minima) has no better certificate — the DC structure of \(\nabla_{K_X}\mathrm E^\vee\)
blocks both.

### 3.6 The Carathéodory space: identified, and why it is not \(\dim X\)-bounded

If a Carathéodory-type argument is to bound support, the pair
\((\beta_A(\mu),\mathrm E^\vee_A(\mu))\) must factor affinely through a finite-dimensional linear
image of \(\mu\). On a face with common log resolution \(Y\to X\) carrying all
\(F_i\): (a) \(\mathrm{Ent}\) factors through the coefficients of \(K_{Y/X}\) — data on
\(N^1(Y)\)-level; (b) \(f_A(t)\) is an integral of \(\mathrm{vol}\) along the PL path
\(\lambda\mapsto\alpha-\sum_i(\lambda-t_i)^+[F_i]\) in \(N^1(Y)_{\mathbb R}\) — it sees only
numerical classes, *but the parametrization retains all \(\ell\) kink times \(t_i\)* even when the
\([F_i]\) are linearly dependent (checked on numerically proportional fibers: the path, hence
\(f\), does not factor through \(\sum\xi_i[F_i]\)); (c) \(\mathrm E^\vee=g_A\) is a Legendre
transform in \(\mathbb R^\ell\), not affine in \(\xi\). So the only linear ambient space the face
functional factors through is (the volume function on) \(N^1(Y)_{\mathbb R}\), of dimension
\(\rho(Y)\ge\rho(X)+\#\{\text{exceptionals}\}\) — it *grows with the support*, and \(\rho(X)\)
itself is topological, not bounded by \(\dim X\). **Conclusion:** no affine/convex simplex
mechanism can yield \(b(\dim X)\); any support bound must come from deeper geometry — e.g.
boundedness/finite generation for minimizing data, i.e. exactly the missing engine of R1 (§4).
Disposition: **OPEN-AFTER-ATTEMPT**, with the conditional reduction of §3.3 as a candidate
theorem and \((\ast)\) as the isolated frontier hypothesis.

---

## 4. Proof attempt B (residual R1): stability \(\Rightarrow\) uniform, algebraically

### 4.1 The projective template

Fano, \(\alpha\propto -K_X\): the published chain is (1) existence of a minimizing valuation for
\(\delta\le\) threshold (Blum–Jonsson; Blum–Liu–Xu — published, exact issue data not re-verified
here, flagged); (2) quasi-monomial structure and **higher-rank finite generation** of the
minimizer, giving a genuine (twisted) special degeneration computing the threshold: Liu–Xu–Zhuang,
Ann. of Math. (2) 196 (2022) 507–566; (3) the polystable dichotomy: a vanishing-invariant
degeneration of a K-polystable Fano is a product — Li–Xu, Ann. of Math. (2) 180 (2014) 197–232 +
LXZ. Output: K-polystable \(\Leftrightarrow\) reduced uniformly K-polystable. For general
polarized \((X,L)\) (cscK/Mabuchi \(\beta\)) **none** of (1)–(3) is published; there is no
Rees-algebra finite generation statement adapted to \(\beta_A=\mathrm{Ent}+\nabla_{K_X}\mathrm
E^\vee\), and the minimizing object is a *measure* (equivalently, by MPWN25 §8.3/BFJ15, a
potential \(\varphi_{\mu}\) or by Ross–Witt Nyström duality a test curve/filtration), not a
valuation.

### 4.2 Sharpest correct conditional statement

**Conditional Theorem.** Let \((X,L)\) be a smooth polarized projective (statements verbatim
transportable to the Kähler case through MPWN25, dated). Assume:

- **(A) Minimizer existence.** The threshold \(\delta_b=\inf_{\mathcal M^{\mathrm{div}}}
  \beta/\mathrm E^\vee\) is computed by some \(\mu^*\in\mathcal M^1\) with
  \(\mathrm{Ent}(\mu^*)<\infty\), \(\mathrm E^\vee(\mu^*)=1\): requires (A1) strong-topology
  compactness of \(\{\mathrm E^\vee=1,\ \mathrm{Ent}\le C\}\subset\mathcal M^1\) and (A2)
  strong lower semicontinuity of \(\mu\mapsto\nabla_{K_X}\mathrm E^\vee(\mu)\) on it.
  (\(\mathrm{Ent}\) is lsc and \(\mathrm E^\vee\) continuous in the strong topology — importable
  from BJ22 (published) at the level of \(\mathcal E^1\)/\(\mathcal M^1\) duality; (A2) has no
  source.)
- **(B) Finite generation for b-minimizers.** The maximal test curve/filtration attached to
  \(\varphi_{\mu^*}\) (MPWN25 §10.1.1 mechanism; DXZ, arXiv:2302.02541) is generated by a finitely
  generated filtration of the section ring, so that \(\delta_b\) is computed by a (twisted) test
  configuration. **UNCONFIRMED — no analogue of LXZ exists for the Mabuchi-type \(\beta\); this is
  the named boundedness conjecture.**
- **(C) Product dichotomy.** Any test configuration computing \(\beta=0\) with
  \(\mathrm E^\vee>0\) for a b-K-polystable \((X,L)\) is a product induced by
  \(\mathrm{Aut}^0(X,L)\). **UNCONFIRMED — the cscK analogue of Li–Xu/LXZ special degeneration
  theory.**

Then b-\(K\)-polystability implies reduced uniform b-\(K\)-polystability; with the trivial converse
(uniform \(\Rightarrow\) polystable, an inequality check on product configurations, no firewall
exposure), the two notions coincide.

### 4.3 FIRST unsupported implication (recorded)

Already **(A1)/(A2)**: the compactness-plus-semicontinuity package for the *pivot term*
\(\nabla_{K_X}\mathrm E^\vee\) in the strong topology of \(\mathcal M^1\). Everything in §4.2
downstream of (A)–(C) is a faithful transcription of the LXZ mechanism and is *not* claimed
proved. Note the structural echo of §3: the reason (B) has no analogue is the same reason the
Carathéodory space of §3.6 is unbounded — the minimizing object carries an a priori unbounded
amount of divisorial data. A proof of (B) with rank bound \(r(n)\) would *simultaneously* answer
R2 with \(b(n)=r(n)\)-type support control. Disposition: **OPEN**, conditional route recorded;
Fano-proportional signature PUBLISHED/RESOLVED (LXZ 2022).

---

## 5. Dependency maps for the book-formulated residuals

### 5.1 B1 — normalization-preserving comparison maps

Target: explicit maps between signatures preserving normalizations (sup-normalization vs
\(\mathrm E\)-normalization; \(V\)-factors; translation conventions), *not* routed through a cscK
metric. Existing bridges (each dated unless noted): uniform b-\(K\) \(\Leftrightarrow\) uniform
K-stability for models, Kähler: MPWN25 Thm 9.2.1 + Cor 9.1.6; \(\Leftrightarrow\) divisorial
valuative threshold: MPWN25 Thm 10.0.4; uniform-models \(\Rightarrow\) coercivity engine: MP24
Thm A (published-accepted); algebraic-case divisorial stability and openness: BJ23b, J. Reine
Angew. Math. 805 (2023) 1–53 (published); \(K^\beta\)/log-discrepancy signatures: DZ25 (dated);
projective signature identifications: Tru26 Cor B (dated). **Missing named inputs:** (i) a
normalization audit table (finite bookkeeping task, book-executable now); (ii) a
measure-to-filtration comparison map matching DZ25's \(K^\beta\)-ray signature with the
divisorial-measure signature — no construction in any source; (iii) replacement of every
metric-mediated equivalence by an NA map — this *is* R1+R3, so B1 strictly contains two open
source residuals. Status: OPEN (programme); the audit sub-item (i) is CONDITIONAL-REDUCTION on
nothing — it can be executed against the dated texts once fetchable.

### 5.2 B2 — singular compact Kähler equivariance

Required end theorem: for \(X\) a normal compact Kähler klt space with
\(T\subset\mathrm{Aut}^0(X)\), reduced coercivity \(\Leftrightarrow\) equivariant model/b-K
stability \(\Leftrightarrow\) singular cscK. Published/preprint partials: analytification
\(X^\beth\) exists for normal compact complex spaces (MP24 §2, published-accepted); coercivity
\(\Rightarrow\) singular cscK under smoothability (PTT23, arXiv:2312.13653) or nef relative
anticanonical resolution (BJT24, arXiv:2412.06096 + PT24, arXiv:2412.07968) — all preprints;
Kähler CY theorem and envelopes: smooth only (MPWN25 §§4–6). **Missing named inputs:** (M1)
continuity of envelopes + orthogonality on normal Kähler spaces (singular analogue of MPWN25
Thm 4.x/Cor); (M2) singular transcendental CY theorem; (M3) equivariant \(X^\beth\) with torus
action and reduced energies \(\mathrm J_T\), absent even for manifolds (MP24 p. 5 exclusion);
(M4) singular Chen–Cheng (coercivity \(\Leftrightarrow\) existence, klt Kähler) beyond the two
special regimes; (M5) NA Matsushima/reductivity, transcendental. Status: OPEN.

### 5.3 B3 — hybrid compactness / family MA continuity

Required end theorems: (H1) the literal continuity question for polarized
degenerations (Favre Q1 / PS23 Q3.18) is now disproved by the verified
smooth-product counterexample.  The stronger fibre-dependent construction
also disproves its zero-supremum normalized replacement; production run
`20260825T035945Z_070e264c3ef1`, item
`pi_db89dd432acabcf33a3f2272`, returned final `correct`; the adapted exact
live theorem and proof passed `20260825T043840Z_d77f7f93aeb0`, item
`pi_b7f015a6ad5570f431769a71`, with the same verdict.  The canonically
polarized semistable case remains PS23 Theorem 5.1 and is not contradicted.
(H2) family
MA continuity over a Banach base (PS23 Q4.9; book problem above it): reduced by PS23 Lem 4.10 to
FS metrics/model functions; hybrid-base case done (PS23 Thm 4.11). (H3) a *family* version of the
finite-energy compactness in MPWN25 Thm B/MP24 (fixed-\(X\) statements only at cutoff), i.e.
hybrid strong compactness of \(\{\mathrm{Ent}\le C\}\) uniformly in the degeneration parameter —
no source; this is the compactness half of the book's `prob:frontier-hybrid-ytd`. (H4)
semicontinuity of the stability threshold \(\delta_b\) in families: published Fano analogue
(Blum–Liu–Xu openness; BJ23b openness in the polarization direction, Crelle 805, published;
transcendental openness in \(\alpha\): MPWN25 Cor 10.0.3, dated, resting on BJ23a preprint);
degenerating-family version missing. Status: OPEN; every item has a named missing estimate.

---

## 6. Self-adversarial audit

- **Preprint leak check.** Prop 3.3.1 and §3.2 items 1–3 use only: definitions, BJ22 (published),
  and elementary convexity — *no* dated claim enters the proofs. Dated claims enter only: (a) the
  *equivalence* of the divisorial threshold with uniform b-K-stability (MPWN25 Thm 10.0.4, granted)
  — without it, §3 is unconditionally a statement about the threshold
  \(\inf\beta/\mathrm E^\vee\) itself; (b) the identification \(h=\nabla_{K_X}g_A\) via
  MPWN25 Cor 10.1.4 with differentiability from BJ23a (preprint) — flagged. The surface
  computations use only classical Zariski-decomposition volume formulas.
- **Erratum firewall.** No statement above cites BHJ19 Thm 5.4/5.6/Thm C/Cor D–E. Slope
  formulas: MPWN25 Thm 9.1.1 (in-text proof via \(\langle\cdot\rangle\)-classes) and Li 2022.
  Non-Archimedean entropy/Mabuchi conventions: MPWN25 §2.4. Checked line-by-line.
- **Separations maintained.** Equivariant vs non-equivariant: R3/R6/B2 record that *all*
  transcendental sources are non-equivariant (MP24 explicit exclusion). Projective vs Kähler:
  Tru26/BJ25 claims kept projective; DZ25's Kähler claim kept at unique-cscK scope; MPWN25/MP24
  Kähler smooth. Smooth vs klt: klt appears only in R4/B2 with the three named preprints; no
  smooth result was silently extended.
- **Honesty of attempt outcomes.** §3: the two computed faces are evidence *for* \((\ast)\) in the
  Fano-side zone, not a proof; the \(c>0\) failure of \((\ast)\) is a failure of the *method*,
  not a counterexample to the tested statement — no DISPROVED label is claimed. §4: (A)–(C) are
  labelled unproved; no priority claim on the conditional theorem, whose skeleton is the known
  LXZ mechanism.
- **Computation integrity.** The \(\mathbb P^1\times\mathbb P^1\) closed form was derived twice
  (hand integration; independent numerical Legendre optimization agreeing to \(5\) decimals at 7
  test points including region boundaries); the \(\mathrm{Bl}_p\mathbb P^2\) run reused the
  validated code path; the destabilization found there is cross-checked against
  Matsushima–Lichnerowicz.

## 7. Dispositions

R1 OPEN (conditional route (A)–(C); Fano-proportional case published). R2 OPEN-AFTER-ATTEMPT
(Prop 3.3.1 conditional reduction to support 1 under \((\ast)\); \((\ast)\) proved for
\(K_X\equiv c\alpha, c\le0\), refuted for \(c>0\), open otherwise; Carathéodory route excluded by
§3.6). R3 OPEN. R4 OPEN with resolved dated sub-piece. R5 OPEN (plausible Tru26 discharge blocked
by scope). R6 OPEN. B1/B2/B3 OPEN with dependency maps. No item is VERIFIED (nothing here was
independently reproved end-to-end); no item is DISPROVED.

---

## Proposed ledger lines

*(Candidates only; none is a verified book input until a fresh-session verifier receipt exists.)*

- Candidate (R2, positive part): "Uniform b-\(K\)-stability is tested on Dirac divisorial masses
  whenever \(\mu\mapsto\nabla_{K_X}\mathrm E^\vee_A(\mu)\) is concave on
  \(\mathcal M^{\mathrm{div}}\); this concavity holds if \(K_X\equiv c\alpha\) with \(c\le0\)."
  (Prop 3.3.1 + scaling identity; verifier to re-derive both.)
- Candidate (R2, obstruction): "For \(K_X\equiv c\alpha\), \(c>0\),
  \(\nabla_{K_X}\mathrm E^\vee_A=c\,\mathrm E^\vee_A\) is strictly convex on generic faces: the
  simplex-concavity mechanism for support bounds fails, while uniform stability holds trivially
  with \(\delta=c\)."
- Candidate (R2, structural): "The face-restricted functional
  \((\mathrm{Ent},\mathrm E^\vee,\nabla_{K_X}\mathrm E^\vee)\) factors through no linear space of
  dimension bounded in \(\dim X\); the minimal factorization space is \(N^1\) of the common log
  resolution, which grows with the support." (§3.6 argument; verifier to check the
  numerically-proportional-fibers non-factorization example.)
- Candidate (worked example): closed-form face profile on \(\mathbb P^1\times\mathbb P^1\),
  \(\alpha=H_1+2H_2\): \(h\) piecewise \(-2\xi^{3/2}+2\xi-1\ /\ -\tfrac{15}{16}+\xi-\xi^2\ /\
  -2(1-\xi)^{3/2}+2(1-\xi)-1\), concave and \(C^1\) — a testable exhibit for the b-K chapter.
- Candidate (R1): "b-\(K\)-polystability \(\Leftrightarrow\) reduced uniform b-\(K\)-polystability
  holds conditional on (A) minimizer existence with strong semicontinuity of the pivot term,
  (B) finite generation for b-minimizing filtrations, (C) the cscK product dichotomy; (B) with a
  rank bound would simultaneously give the R2 support bound."
- Candidate (B1): a finite normalization-audit table across MPWN25/MP24/BJ23b conventions is
  executable now and should be queued as a separate Rethlas input.
- Candidate (status line for ch71): replace "Boucksom–Jonsson also isolate bounded support size…
  remain open" by a pointer to the conditional reduction and its \((\ast)\)-frontier, keeping the
  OPEN label.
