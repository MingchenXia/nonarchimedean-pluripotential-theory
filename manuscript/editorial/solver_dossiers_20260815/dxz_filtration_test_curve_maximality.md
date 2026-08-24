# Maximality of filtration test curves in a big class

**Problem id:** `open_problems/dxz_filtration_test_curve_maximality`
**Solver pass:** in-session direct solve, 15 August 2026.
**Promotion status:** CANDIDATE-ONLY. No Rethlas receipt. Nothing enters theorem
typography.
**Source:** Darvas--Xia--Zhang, arXiv:2302.02541v3, the conjecture stated immediately
before Definition 4.4. Direct arXiv retrieval is blocked by the egress proxy here;
source-numbered claims are used as transmitted by the packet (**[from-packet]**) or
recalled and marked **[UNCONFIRMED]**.

**Binding caution, restated from the packet.** DXZ Definition 4.4 does *not* assert
maximality: it inserts the maximization operator precisely because the conjecture is
open. No sentence below may be read as attributing maximality to that definition.

---

## 1. Formalization

\(X\) is a connected projective manifold of dimension \(n\), \(L\) a big line bundle,
\(\theta\in c_1(L)\) smooth. \(\mathcal F\) is a filtration of the section ring
\(R(X,L)\) that is multiplicative, decreasing, left-continuous and linearly bounded
[from-packet]. For \(m\ge1\) and \(\tau\in\mathbf R\) the Bergman test curve is
\[
  \phi^{\mathcal F}_{\tau,m}
   :=\frac1{2m}\,\log\ \sup\Bigl\{|s|^2_{h^m}\ :\ s\in\mathcal F^{m\tau}H^0(X,mL),
      \ \lVert s\rVert\le1\Bigr\},
\]
and \(\phi^{\mathcal F}_\tau\) is the limiting test curve of §4.1 [from-packet],
formed as the usc regularization of \(\lim_m\), decreasing and concave in \(\tau\).

*\(\mathcal I\)-maximality* means \(\phi_\tau=P[\phi_\tau]_{\mathcal I}\) for every
\(\tau\), where \(P[\cdot]_{\mathcal I}\) is the \(\mathcal I\)-envelope: the largest
\(\mathcal I\)-model potential \(\mathcal I\)-dominated by the argument. Equivalently,
\(\phi_\tau\) is determined by its multiplier ideals \(\mathcal J(k\phi_\tau)\),
\(k\ge1\), through the standard envelope construction.

**Conjecture (C).** For \(L\) big, \(\phi^{\mathcal F}_\tau\) is
\(\mathcal I\)-maximal for every \(\tau\), i.e. the maximization in Definition 4.4 is
redundant.

Two regimes must be separated throughout, and conflating them is the main trap:
- the **positive-mass range** \(\tau<\tau_{\mathrm{crit}}\), where
  \(\mathrm m(\phi_\tau)>0\);
- the **zero-mass range** \(\tau\ge\tau_{\mathrm{crit}}\).

---

## 2. Endpoints (unconditional)

**(a) \(\tau\le\tau_{\min}\).** The filtration condition is vacuous and
\(\phi^{\mathcal F}_\tau\) is the equilibrium potential of \(L\), i.e. the envelope
\(P_\theta(0)\), which has minimal singularities. Potentials with minimal
singularities satisfy \(P[\phi]=\phi\), hence are \(\mathcal I\)-maximal. **(C) holds
at this endpoint for \(L\) merely big.**

**(b) \(\tau>\tau_{\max}\).** \(\mathcal F^{m\tau}H^0(mL)=0\) for all \(m\), so
\(\phi_\tau\equiv-\infty\) and the statement is vacuous under the book's
extended-real conventions.

So (C) is a statement about the interior of the \(\tau\)-range, and the first
non-trivial regime is the positive-mass interior.

---

## 3. The finitely generated case, and the exact obstruction

Let \(\mathcal F\) be finitely generated, so that it arises from a test configuration
or flag ideal and the Bergman curves have analytic singularities.

**Route.** \(\mathcal I\)-maximality of a potential with analytic singularities is
equivalent to the ideal data being integrally closed at each level, in the sense that
the potential is recovered from \(\{\mathcal J(k\phi_\tau)\}_k\). For a Bergman
potential, the comparison between the section-defined potential and the multiplier
ideals is the Demailly approximation package: one needs, for a fixed ample \(A\) and
all \(m\),
\[
  \mathcal J(m\phi_\tau)\otimes\mathcal O(mL+A)\quad\text{globally generated,}
\]
which follows from Castelnuovo--Mumford regularity, plus Ohsawa--Takegoshi to go
back. In the **ample** case one may take \(A\) to be a fixed multiple of \(L\) itself,
so the twist is absorbed into the same bundle and the comparison is *internal* to the
graded ring \(R(X,L)\); the error in the potential is \(O(1/m)\) and the multiplier
ideals at each level match after passing to the limit. This is why the ample case is
known [UNCONFIRMED as to DXZ's exact route].

**First genuinely unsupported implication in the big case**, recorded verbatim:
*"since the twist costs only \(O(1/m)\) in the potential, the limiting multiplier
ideals are unchanged, so the section-defined curve is \(\mathcal I\)-maximal."*

This is the crux and it is not supported. The reason is structural:

> An \(O(1/m)\) perturbation of the *class* is harmless for the potential, which
> converges uniformly on compacta away from the base locus, but
> \(\mathcal I\)-equivalence is **not** continuous under such perturbations. Two
> potentials differing by \(o(1)\) can have different multiplier ideals at every
> level — jumping numbers move discontinuously.

When \(L\) is ample the auxiliary twist can be taken inside \(\mathbf R_{\ge0}L\), so
the perturbation is a *rescaling* of the same test curve and the discrepancy is
absorbed by concavity in \(\tau\). When \(L\) is merely big, the required twist
\(A\) is transverse to \(L\): \(L+\varepsilon A\) is not proportional to \(L\), the
comparison leaves the graded ring, and no mechanism returns it. Concretely, the
sections of \(m L\) all vanish along the augmented base locus \(\mathbf B_+(L)\),
while the multiplier ideals of \(\phi_\tau\) are computed from the twisted system;
whether the two agree along \(\mathbf B_+(L)\) is exactly the open point.

**CONDITIONAL-REDUCTION.** (C) for finitely generated \(\mathcal F\) in the
positive-mass range follows from the following statement, which is the precise
missing input:

> **(U)** For \(L\) big and \(\mathcal F\) finitely generated, the Bergman
> approximations satisfy \(\mathcal J(k\phi_\tau)=\varinjlim_m\mathcal
> J(k\phi_{\tau,m})\) for every \(k\), with the limit independent of the auxiliary
> ample twist used to globally generate.

(U) is a Fujita-approximation-type uniformity statement. It is plausible and is
exactly what an eventual proof must supply; it is *not* a formal consequence of the
\(O(1/m)\) potential estimate.

---

## 4. The blow-up test, computed — a refuted counterexample mechanism

The packet flagged birational pullback of ample data as the most likely source of a
counterexample. It is not one, and the computation is worth recording because it
kills the mechanism cleanly.

Let \(\mu:X'=\mathrm{Bl}_p\mathbf P^2\to\mathbf P^2\), \(E=\mu^{-1}(p)\), and
\(L':=\mu^*\mathcal O(d)+E\) with \(d\ge1\). Then \(L'\) is big and not nef, since
\(L'\cdot E=0+E^2=-1<0\), so \(E\subseteq\mathbf B_+(L')\) — the exact regime the
conjecture is about.

**Sections.** \(\mu_*\mathcal O_{X'}(mE)=\mathcal O_{\mathbf P^2}\), so
\[
  H^0(X',mL')=H^0\bigl(X',\mu^*\mathcal O(md)+mE\bigr)
   =\{s\in H^0(\mathbf P^2,\mathcal O(md)):\ \operatorname{mult}_p s\ge m\}.
\]
Hence *every* section of \(mL'\) vanishes to order \(\ge m\) at \(p\), so every
Bergman potential has Lelong number \(\ge1\) along \(E\) after normalization.

**Zariski decomposition.** Write \(L'=P+N\). From \(L'\cdot E=-1<0\), \(E\) lies in the
negative part; setting \(N=aE\) and imposing \(P\cdot E=0\) gives
\((\mu^*\mathcal O(d)+(1-a)E)\cdot E=-(1-a)=0\), so \(a=1\), \(N=E\),
\(P=\mu^*\mathcal O(d)\) nef.

**Conclusion of the test.** Minimal-singularity potentials in \(c_1(L')\) have Lelong
number exactly \(1\) along \(E\) — matching the section-theoretic lower bound. The
sections therefore *do* see the correct singularity along the exceptional divisor,
and the naive expectation that the pulled-back curve is strictly more singular than
its maximization fails. Taking \(\mathcal F\) the filtration induced by
\(\operatorname{ord}_E\) (or by \(\operatorname{mult}_p\)) reproduces the same
matching at every level, because the graded pieces are again cut out by multiplicity
conditions at \(p\), whose integral closures are the corresponding monomial ideals.

**Disposition of the mechanism: refuted.** Exceptional-divisor pullback of ample data
does not produce a gap. Any counterexample must therefore live where the base locus
is *not* an exceptional divisor of a single blow-up with an integrally closed
multiplicity filtration — e.g. a base locus of higher codimension, or a filtration
whose graded ideals fail to be integrally closed.

---

## 5. The zero-mass range: a reduction to an already-open book problem

For \(\tau\) in the zero-mass range, \(\mathcal I\)-maximality of \(\phi_\tau\) asks
whether a zero-mass potential agrees with its \(\mathcal I\)-envelope. This is
precisely the circle of questions already on the book's open list — the relation
\(\varphi\sim_P P_\theta[\varphi]\) in the zero-mass regime, and
\(\mathcal I\)-goodness of zero-mass \(\mathcal I\)-model potentials.

**Recorded reduction.** (C) restricted to the zero-mass range is at least as hard as
the zero-mass \(\mathcal I\)-model problems already recorded as open in the book. It
should therefore not be attacked independently, and a future packet should state (C)
for the positive-mass range only, unless it intends to solve the zero-mass envelope
problem as well. This is the single most useful scoping correction from this pass.

---

## 6. Self-adversarial audit

- *Endpoint vs interior.* §2(a) uses minimal singularities, valid for big \(L\); it
  does not silently extend into the interior of the \(\tau\)-range.
- *Order of limits.* Throughout, \(m\to\infty\) is taken before any statement about
  \(\tau\); the usc regularization is applied after, as in §4.1 [from-packet]. No
  interchange of \(\sup_m\) with the \(\mathcal I\)-envelope is performed — indeed §3
  identifies exactly that interchange as the unsupported step.
- *\(\sup_m\) versus its usc regularization.* The regularization can only decrease
  singularity; it is applied to both sides of every comparison in §4.
- *Non-finitely-generated filtrations.* Untouched. §3 is stated for f.g. only, and
  the general case is strictly harder since analytic singularities are lost.
- *Did the blow-up computation assume \(d\) large?* Only \(d\ge1\), and the Zariski
  computation is independent of \(d\).
- *Energy/Legendre shortcuts.* None used, in compliance with the packet's
  requirement that multiplier ideals be compared at every level.

---

## 7. Dispositions

| Item | Disposition |
|---|---|
| (C) at \(\tau\le\tau_{\min}\) | **CANDIDATE-PROPOSITION** (minimal singularities are \(\mathcal I\)-maximal), §2(a) |
| (C) at \(\tau>\tau_{\max}\) | vacuous under the book's conventions, §2(b) |
| (C), f.g. filtration, positive-mass interior | **CONDITIONAL-REDUCTION** to the uniformity statement (U), §3 |
| Exceptional-pullback counterexample mechanism | **refuted**, with a complete computation, §4 |
| (C), zero-mass range | **OPEN-AFTER-ATTEMPT**, reduced to the book's existing zero-mass \(\mathcal I\)-model problems, §5 |
| (C) in general | **OPEN-AFTER-ATTEMPT** |

---

## 8. Proposed ledger lines

- **Problem id:** `open_problems/dxz_filtration_test_curve_maximality`. In-session
  solver pass, 15 August 2026; **no Rethlas receipt**; candidate-only.
- **Endpoints settled:** at the trivial end of the \(\tau\)-range the filtration test
  curve is the equilibrium potential, which has minimal singularities and is
  therefore \(\mathcal I\)-maximal for \(L\) merely big; the far end is vacuous. The
  conjecture is a statement about the interior.
- **Exact obstruction identified:** the ample proof transports to the big case only
  through the claim that an \(O(1/m)\) twist leaves the limiting multiplier ideals
  unchanged. That claim is unsupported, because \(\mathcal I\)-equivalence is not
  continuous under small perturbations of the class, and for big non-ample \(L\) the
  necessary ample twist is transverse to \(L\) and leaves the graded ring \(R(X,L)\).
  Reduced to a single Fujita-approximation-type uniformity statement (U).
- **Counterexample mechanism refuted:** for \(X'=\mathrm{Bl}_p\mathbf P^2\) and
  \(L'=\mu^*\mathcal O(d)+E\), every section of \(mL'\) has \(\operatorname{mult}_p\ge m\),
  and the Zariski decomposition is \(P=\mu^*\mathcal O(d)\), \(N=E\); the
  section-theoretic and minimal-singularity Lelong numbers along \(E\) agree at
  \(1\). Exceptional-divisor pullback of ample data therefore produces no gap, and
  future searches must use a base locus of higher codimension or graded ideals that
  are not integrally closed.
- **Scoping correction (recommended for the book):** in the zero-mass \(\tau\)-range
  the conjecture subsumes the book's already-open zero-mass \(\mathcal I\)-model
  problems. The research chapter should state the maximality question for the
  positive-mass range, with the zero-mass range explicitly deferred to those
  problems, rather than presenting one undifferentiated conjecture.
- **Book disposition:** retain (C) as open; record the endpoint results, the
  obstruction (U), and the refuted pullback mechanism in the editorial ledger only.
  No priority claim; DXZ Definition 4.4 must continue to be described as inserting
  maximization because the question is open.
