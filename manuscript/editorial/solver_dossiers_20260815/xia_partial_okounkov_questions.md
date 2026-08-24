# Partial Okounkov bodies, numerical dimension, and Chebyshev transforms

**Problem id:** `open_problems/xia_partial_okounkov_questions`
**Solver pass:** in-session direct solve, 15 August 2026.
**Promotion status:** CANDIDATE-ONLY. No Rethlas receipt exists for anything below.
Nothing may enter theorem typography.
**Source:** Mingchen Xia, *Partial Okounkov bodies and Duistermaat--Heckman measures
of non-Archimedean metrics*, arXiv:2112.04290 — Conjecture 5.29, Conjecture 8.8, and
the final paragraph of §6.4. Direct arXiv retrieval is blocked by the egress proxy
in this environment; source-numbered statements are used exactly as transmitted by
the packet and are marked **[from-packet]**, and structural facts recalled from the
paper are marked **[UNCONFIRMED]** where a verbatim check was impossible.

> **Superseded interim correction, 24 August 2026.**  The 15 August novelty
> separation in Section 3.0 treated *Mixed Volumes of Okounkov Bodies* as a
> completed literature resolution.  A later independent audit established
> that the available July 2026 document is an unpublished work in progress,
> and no exact-current independent verification of its headline theorems is
> available.  Hence Q2 is **OPEN PENDING VERIFICATION**, not
> literature-resolved.  Nothing in this dossier is promoted: the argument in
> Section 3.1 remains a candidate conditional on its stated inputs.  The
> superseded wording is left in place below to preserve the audit history.

> **24 Aug 2026 controlling addendum (later exact verification).**  The
> author subsequently supplied the TeX proof.  The new, separate repaired
> proof packet is
> `../solver_dossiers_20260824/xia_conjecture_8_8_repaired_proof_packet.md`,
> with SHA-256
> `9227826d7ba5c641c5fe32cc4daae9acbb3b57274dcc1b356ba8beadd58cad7b`.
> After human and hostile repair audits, production Rethlas
> (`gpt-5.6-sol`, `xhigh`) returned `correct`, zero critical errors, and zero
> gaps.  Q2 is therefore verified for smooth projective varieties, big line
> bundles, and positive Cao/ideal volume.  This does not promote the old
> Section 3.1 candidate proof, does not claim publication of the supplied
> manuscript, and does not cover zero volume, transcendental classes,
> singular varieties, or attainment.  This later paragraph controls over
> both the temporary open notice above and the 15 August chronology below.

**Standing constraints from the book.** Two results are already verified and are used
as inputs, not re-proved: (i) the rational-toric case of Q1, \(\dim\Delta=\mathrm{nd}\)
for invariant data in rational toric classes; (ii) the no-go: **no construction
invariant under \(\mathcal I\)-equivalence can recover nonpluripolar mass in the
zero-mass regime.** Every proposal below is checked against (ii).

---

## 1. Formalization and normalizations

\(X\) is a connected compact Kähler manifold of dimension \(n\); \(L\) a line bundle
(or \(\theta\) a smooth closed real \((1,1)\)-form); \(\phi\) a \(\theta\)-psh potential.
For a rank-\(n\) valuation \(\nu\) (equivalently an admissible flag) the *partial
Okounkov body* is \(\Delta_\nu(L,\phi)\subseteq\mathbf R^n\).

Normalizations fixed once, and used consistently:

- \(\operatorname{vol}\bigl(\Delta_\nu(L,\phi)\bigr)=\dfrac{1}{n!}\displaystyle\int_X
  \bigl(\theta+dd^c\phi\bigr)^n_{\mathrm{np}}\) — Xia's volume theorem
  **[UNCONFIRMED numbering; the normalization is the one making
  \(\operatorname{vol}\Delta(L)=(L^n)/n!\) in the classical case]**. Write
  \(\mathrm m(\phi):=\int_X(\theta+dd^c\phi)^n_{\mathrm{np}}\).
- Mixed volumes \(\mathrm{MV}\) are normalized so that
  \(\mathrm{MV}(K,\dots,K)=\operatorname{vol}(K)\), whence
  \(\operatorname{vol}\bigl(\sum_i t_iK_i\bigr)=\sum_{|\beta|=n}\binom{n}{\beta}
  t^\beta\,\mathrm{MV}(K_1^{\beta_1},\dots,K_n^{\beta_n})\) for \(t_i\ge0\).
- **Homogeneity.** \(\Delta_\nu(tL,t\phi)=t\,\Delta_\nu(L,\phi)\) for \(t\in\mathbf
  Q_{>0}\), extended by continuity **[UNCONFIRMED]**.
- **Superadditivity.**
  \(\Delta_\nu(L_1,\phi_1)+\Delta_\nu(L_2,\phi_2)\subseteq
  \Delta_\nu(L_1+L_2,\phi_1+\phi_2)\), from multiplicativity of the valuation
  semigroup together with the fact that a product of sections satisfies the
  singularity bound defining the partial body **[UNCONFIRMED; this is the natural
  analogue of the classical statement \(\Delta(L_1)+\Delta(L_2)\subseteq\Delta(L_1+L_2)\)
  and is the single external input for §3]**.

The three questions, kept separate as the packet demands:

**Q1.** \(\dim\Delta(L,\phi)=\mathrm{nd}(L,\phi)\), Cao's analytic numerical
dimension, including zero mass (Conjecture 5.29 [from-packet]). The independence of
the limit body from the auxiliary \((H,\omega)\) is *not* the question.

**Q2.** Conjecture 8.8 [from-packet]:
\(\frac1{n!}\int_X dd^c\phi_1\wedge\cdots\wedge dd^c\phi_n
=\sup_\nu \mathrm{MV}\bigl(\Delta_\nu(L_1,\phi_1),\dots,\Delta_\nu(L_n,\phi_n)\bigr)\)
for big \((L_i,\phi_i)\) of positive volume.

**Q3.** Independence of the Chebyshev transform \(c_{[\varphi]}[v]\) from the
auxiliary \(\eta\preceq\varphi\) with Kähler-current curvature, in the definition via
\(\varphi_\varepsilon=(1-\varepsilon)\varphi+\varepsilon\eta\) (§6.4 [from-packet]).
This is *not* the \((H,\omega)\) independence of the limit body.

---

## 2. Q1 — dimension versus numerical dimension

### 2.1 What is unconditional

**(a) The zero end.** \(\dim\Delta_\nu(L,\phi)=0\) iff \(\Delta_\nu\) is a point.
Since \(\Delta_\nu\) is convex and contains the valuation image of the (nonempty)
space of sections with the prescribed singularity bound, \(\dim\Delta_\nu=0\) forces
the graded pieces to have bounded dimension, i.e. vanishing volume growth in every
direction. On the other side \(\mathrm{nd}(L,\phi)=0\) means the positive products
\(\langle(\theta+dd^c\phi)^k\rangle\) vanish against Kähler forms for all \(k\ge1\).
The implication \(\mathrm{nd}=0\Rightarrow\dim\Delta=0\) is the accessible one and
follows from the definition of \(\mathrm{nd}\) via positive products together with the
volume theorem applied to perturbations \(L+\varepsilon H\). The converse requires
the reverse comparison in §2.2 and is **not** established here.

**(b) The top end.** \(\dim\Delta_\nu=n\) iff \(\operatorname{vol}\Delta_\nu>0\) iff
\(\mathrm m(\phi)>0\), by the volume theorem; and \(\mathrm{nd}=n\) iff
\(\mathrm m(\phi)>0\) by definition of the analytic numerical dimension in the
positive-mass regime. Hence **Q1 holds unconditionally at both ends
\(\{0\}\) — modulo the converse in (a) — and \(\{n\}\)**; the whole content is the
intermediate range \(0<\mathrm{nd}<n\), which is exactly the zero-mass regime.

### 2.2 Attempted proof of \(\dim\Delta\le\mathrm{nd}\)

The natural route perturbs: for \(H\) ample and \(\varepsilon>0\), set
\(\phi_\varepsilon\) an appropriate potential on \(L+\varepsilon H\), and compare
\(\operatorname{vol}\Delta_\nu(L+\varepsilon H,\phi_\varepsilon)=
\mathrm m(\phi_\varepsilon)/n!\) with the asymptotics of \(\mathrm m(\phi_\varepsilon)\)
as \(\varepsilon\downarrow0\). If \(\dim\Delta_\nu(L,\phi)=d\), then
\(\Delta_\nu(L,\phi)\) has nonempty relative interior in a \(d\)-plane, and
\(\Delta_\nu(L+\varepsilon H,\phi_\varepsilon)\supseteq
\Delta_\nu(L,\phi)+\varepsilon\Delta_\nu(H,\cdot)\) by superadditivity, whose volume
is \(\gtrsim\varepsilon^{\,n-d}\). Hence
\[
  \mathrm m(\phi_\varepsilon)\ \gtrsim\ \varepsilon^{\,n-d},
\]
so the order of vanishing of \(\mathrm m(\phi_\varepsilon)\) is at most \(n-d\).

**First genuinely unsupported implication**, recorded verbatim: *"the order of
vanishing of \(\mathrm m(\phi_\varepsilon)\) as \(\varepsilon\downarrow0\) equals
\(n-\mathrm{nd}(L,\phi)\)."* This is the analytic characterization of Cao's numerical
dimension by the vanishing order of perturbed masses. It is exactly the statement
one needs, it is *not* Cao's definition, and I could not verify it in the available
sources. **Everything in Q1 beyond §2.1 is conditional on it.**

**CONDITIONAL-REDUCTION (Q1).** Granting the displayed characterization,
\(\dim\Delta_\nu(L,\phi)\le\mathrm{nd}(L,\phi)\) follows by the superadditivity bound
above, for every \(\nu\). The reverse inequality requires producing a flag adapted to
a subvariety computing \(\mathrm{nd}\), and is not obtained here.

### 2.3 Surfaces

For \(n=2\), \(\mathrm{nd}\in\{0,1,2\}\); the cases \(0\) and \(2\) are §2.1. The single
open case is \(\mathrm{nd}=1\), \(\mathrm m(\phi)=0\), i.e. \(\Delta_\nu\) should be a
segment. Superadditivity gives \(\dim\ge1\) as soon as some perturbed body grows
linearly; the difficulty is excluding \(\dim\Delta_\nu=0\) with \(\mathrm{nd}=1\),
which again needs §2.2's characterization. **A complete unconditional \(n=2\)
statement was not obtained**, contrary to the optimistic expectation in the packet.
Recording this honestly is the outcome: the surface case is not easier than the
general case, because Zariski decomposition controls the *class* while
\(\mathrm{nd}(L,\phi)\) depends on \(\phi\) beyond its class.

**Consistency with the book's no-go.** \(\dim\Delta\) is an \(\mathcal I\)-invariant of
the data **[UNCONFIRMED]**; \(\mathrm{nd}\) is likewise expected to be. Q1 therefore
does *not* violate the verified no-go, which concerns recovery of nonpluripolar
*mass*, a strictly finer quantity, in the zero-mass regime. No conflict.

**Disposition Q1: OPEN-AFTER-ATTEMPT**, with the unconditional endpoints of §2.1 and
the sharply identified missing input of §2.2.

---

## 3. Q2 — the mixed-volume conjecture

This is where the pass produced its strongest result. The engine is a
polynomial-degeneration argument that upgrades an aggregate inequality to individual
coefficients.

### 3.0 NOVELTY SEPARATION — Q2 IS RESOLVED IN THE LITERATURE

**Correction entered 15 August 2026, after the pass, on the author's pointer.**
Mingchen Xia, *Mixed Volumes of Okounkov Bodies*
(`https://mingchenxia.github.io/Papers/MVOB.pdf`), proves Conjecture 8.8 **in
full**, as an equality and in both the algebraic and the singular-metric forms:

- **MVOB Theorem 1.1.** For big line bundles \(L_1,\dots,L_n\) on a smooth
  projective \(X\) of dimension \(n\),
  \(\langle L_1,\dots,L_n\rangle=n!\,\sup_\nu
  \operatorname{vol}(\Delta_\nu(L_1),\dots,\Delta_\nu(L_n))\), with \(\nu\)
  ranging over surjective valuations \(\mathbf C(X)^\times\to\mathbf Z^n_{\mathrm{lex}}\)
  trivial on \(\mathbf C^\times\).
- **MVOB Theorem 1.2.** For big \(L_i\) with psh metrics \(h_i\) of positive
  volume,
  \(\operatorname{vol}(dd^ch_1,\dots,dd^ch_n)=n!\,\sup_\nu
  \operatorname{vol}(\Delta_\nu(L_1,h_1),\dots,\Delta_\nu(L_n,h_n))\).

MVOB also states the superadditivity
\(\Delta_\nu(L,h)+\Delta_\nu(L',h')\subseteq\Delta_\nu(L\otimes L',h\otimes h')\)
together with \(\mathcal I\)-monotonicity, which was the single load-bearing
input flagged **[UNCONFIRMED]** in §1 and §3.1. That input is therefore
confirmed, and the argument of §3.1 is sound — **but its conclusion is a
special case of MVOB Theorem 1.2 and is not new.**

**Revised disposition for Q2: LITERATURE-RESOLVED.** The §3.1 material is
retained below only as an independently found partial proof, demoted from
CANDIDATE-PROPOSITION. It carries no priority claim, must not be submitted for a
receipt, and must not appear in the book as a result of this book. Where the
book needs the mixed-volume formula it should cite MVOB directly, for the full
equality rather than one inequality.

This is precisely the novelty-separation step of the verification protocol
working as intended: the pass produced a correct argument for a known theorem.
The failure was one of literature search, not of proof — MVOB was not in the
local reference pack and arXiv was unreachable during the pass.

### 3.1 Independently found partial proof (DEMOTED — see §3.0)

**Statement.** Assume superadditivity and homogeneity as normalized in §1 and Xia's
volume theorem. Let \((L_1,\phi_1),(L_2,\phi_2)\) be big of positive volume. Then
for **every** rank-\(n\) valuation \(\nu\),
\[
  \frac1{n!}\int_X (dd^c\phi_1)^{n-1}\wedge dd^c\phi_2
  \ \ \ge\ \ \mathrm{MV}\bigl(\Delta_\nu(L_1,\phi_1)^{n-1},\Delta_\nu(L_2,\phi_2)\bigr),
\]
and consequently the \(\ge\) half of Conjecture 8.8 holds for these mixed terms:
the left side dominates \(\sup_\nu\mathrm{MV}\).

*Proof.* Fix \(\nu\) and write \(K_i:=\Delta_\nu(L_i,\phi_i)\). For \(t_1,t_2\ge0\)
rational, homogeneity and superadditivity give
\[
  t_1K_1+t_2K_2\ \subseteq\ \Delta_\nu\bigl(t_1L_1+t_2L_2,\ t_1\phi_1+t_2\phi_2\bigr),
\]
so taking Euclidean volumes and applying the volume theorem to the right-hand side,
\[
  \operatorname{vol}(t_1K_1+t_2K_2)\ \le\
  \frac1{n!}\int_X\bigl(t_1\,dd^c\phi_1+t_2\,dd^c\phi_2\bigr)^n .
\]
Expand both sides by the Minkowski and multinomial expansions and set
\[
  P(t_1,t_2):=\sum_{k=0}^n\binom nk t_1^{\,n-k}t_2^{\,k}\Bigl[
     \tfrac1{n!}\!\int_X (dd^c\phi_1)^{n-k}\!\wedge (dd^c\phi_2)^{k}
     -\mathrm{MV}(K_1^{n-k},K_2^{k})\Bigr]
   =:\sum_{k=0}^n\binom nk t_1^{\,n-k}t_2^{\,k}c_k .
\]
Then \(P(t_1,t_2)\ge0\) for all \(t_1,t_2\ge0\) (rational, hence all, by continuity).

The pure coefficient vanishes: \(c_0=\frac1{n!}\mathrm m(\phi_1)-\operatorname{vol}(K_1)=0\)
by the volume theorem. Therefore, for \(s\ge0\),
\[
  0\ \le\ P(1,s)\ =\ c_0+n\,s\,c_1+O(s^2)\ =\ n\,s\,c_1+O(s^2),
\]
and dividing by \(s>0\) and letting \(s\downarrow0\) gives \(c_1\ge0\), which is the
assertion. \(\square\)

**Audit of this proof.** (i) The vanishing of \(c_0\) is essential and is exactly
Xia's volume theorem — without it the degeneration yields nothing. (ii) Only the
*first-order* coefficient is forced: for \(k\ge2\), \(c_1>0\) swamps the expansion and
\(c_k\) is unconstrained. So the argument does **not** give the general mixed term,
and I do not claim it. (iii) The inequality goes in the direction *mass-side
\(\ge\) body-side*, i.e. the bodies under-estimate; this is the direction consistent
with superadditivity, and it is the direction in which the supremum over \(\nu\) is
the natural completion. (iv) Everything rests on the superadditivity input flagged
**[UNCONFIRMED]** in §1; if that inclusion is false or holds only up to closure, the
proposition fails and must be withdrawn.

**Toric sanity check.** In the toric case with the coordinate valuation,
\(\Delta_\nu\) is the moment polytope \(P_i\) and
\(\frac1{n!}\int dd^c\phi_1\wedge\cdots\wedge dd^c\phi_n=\mathrm{MV}(P_1,\dots,P_n)\)
with the §1 normalization, so \(c_k=0\) for all \(k\) and the inequality is an
equality, with the supremum attained. Consistent, and it confirms the normalization
is not off by a factorial.

### 3.2 The reverse direction

The reverse inequality \(\frac1{n!}\int\le\sup_\nu\mathrm{MV}\) would require, for
each \(\varepsilon\), a valuation \(\nu\) whose bodies nearly saturate superadditivity
— i.e. asymptotic multiplicativity of the section semigroup along \(\nu\). In the
pure case this is exactly what the volume theorem encodes; in the genuinely mixed
case no mechanism was found. **OPEN-AFTER-ATTEMPT.**

**Disposition Q2:** \(\ge\) half for two-bundle mixed terms
**CANDIDATE-PROPOSITION** (§3.1); general mixed terms and the reverse inequality
**OPEN-AFTER-ATTEMPT**.

---

## 4. Q3 — independence of the Chebyshev transform from \(\eta\)

The packet proposed a max-interpolation squeeze. It **half** works, and the reason it
fails is itself the main finding.

### 4.1 The admissible set is upward directed (complete proof)

Call \(\eta\) *admissible* for \(\varphi\) if \(\eta\preceq\varphi\) (i.e.
\(\eta\le\varphi+C\)) and \(\theta+dd^c\eta\ge\delta\omega\) for some \(\delta>0\).

**Claim.** If \(\eta_1,\eta_2\) are admissible then so is
\(\eta':=\max(\eta_1,\eta_2)\).

*Proof.* Write \(\delta:=\min(\delta_1,\delta_2)\). Each \(\eta_i\) is
\((\theta-\delta\omega)\)-psh, since \(\theta-\delta\omega+dd^c\eta_i\ge
(\delta_i-\delta)\omega\ge0\). The maximum of two \((\theta-\delta\omega)\)-psh
functions is \((\theta-\delta\omega)\)-psh, so
\(\theta+dd^c\eta'\ge\delta\omega\). And \(\eta'\le\varphi+\max(C_1,C_2)\). \(\square\)

### 4.2 The unconditional half

Assume the transform is order-reversing in the potential and translation-equivariant
**[UNCONFIRMED, but immediate from a \(\limsup\)-of-normalized-sup-norms definition]**.
Since \(\eta'\ge\eta_i\), we get
\((1-\varepsilon)\varphi+\varepsilon\eta'\ge(1-\varepsilon)\varphi+\varepsilon\eta_i\)
pointwise, hence \(c_{\eta'}\le c_{\eta_i}\) in the limit, for \(i=1,2\):
**the maximum gives a common lower bound.**

### 4.3 Why the squeeze does not close — and the structural obstruction

To conclude \(c_{\eta_1}=c_{\eta_2}\) one needs the reverse: that the
\(\eta_1\)-family is dominated by an \(\eta'\)-family at a comparable parameter. Trying
\((1-\varepsilon)\varphi+\varepsilon\eta_1\ \ge\ (1-t)\varphi+t\eta'\) reduces, using
only \(\eta'\le\varphi+C\), to
\[
  \varepsilon\bigl(\eta_1-\varphi\bigr)\ \ge\ tC ,
\]
which fails wherever \(\eta_1\) is much more singular than \(\varphi\).

**And that locus is unavoidable.** Admissibility does *not* bound the singularity of
\(\eta\) from below: if \(\eta_0\) is admissible and \(s\) is a holomorphic section,
then \(\eta_1:=\eta_0+\log|s|\) satisfies
\(\theta+dd^c\eta_1=\theta+dd^c\eta_0+[\operatorname{div}s]\ge\delta\omega\), so
\(\eta_1\) is still admissible, and \(\eta_1\preceq\varphi\) still holds. Hence:

> **The admissible set is upward directed (§4.1) but is unbounded below in
> singularity, and in particular is not downward directed.**

This kills the squeeze uniformly, not accidentally.

**First genuinely unsupported implication**, verbatim: *"by monotonicity and the
max-interpolation, the \(\eta_1\)- and \(\eta_2\)-families are trapped between each
other up to \(O(\varepsilon)\)."* False, by the display above.

**CONDITIONAL-REDUCTION (Q3).** Independence holds if and only if the transform is
asymptotically insensitive to the singular part of the auxiliary datum, i.e.
\[
  \lim_{\varepsilon\downarrow0}\Bigl(
   c\bigl[(1-\varepsilon)\varphi+\varepsilon\eta\bigr]
   -c\bigl[(1-\varepsilon)\varphi+\varepsilon\max(\eta,\eta_0)\bigr]\Bigr)=0
\]
for admissible \(\eta,\eta_0\). This is a genuine analytic statement — plausibly
provable from a capacity or Skoda-type estimate showing that a set where \(\eta\) is
very singular contributes \(o(1)\) to the normalized section asymptotics — and it is
the exact missing input. It is *not* formal.

**Disposition Q3:** upward-directedness and the common lower bound
**CANDIDATE-PROPOSITION** (§4.1--4.2); full independence **OPEN-AFTER-ATTEMPT** with
the reduction of §4.3.

---

## 5. Self-adversarial audit

- *Did any argument use \(\mathcal I\)-invariance to recover mass at zero mass?* No.
  §3 is entirely in the positive-volume regime, as Conjecture 8.8 requires; §2 is
  about dimension, not mass. The book's no-go is respected.
- *Flag versus rank-\(n\) valuation.* §3.1 is proved for a fixed \(\nu\) and only then
  passes to the supremum, so no interchange of \(\sup_\nu\) with a limit occurs.
- *\(\sup\) versus \(\max\).* Nowhere is attainment of the supremum used.
- *Rational versus real scaling.* §3.1 argues with rational \(t_i\) and passes to real
  \(t\) by continuity of both sides in \(t\); the left side is a polynomial and the
  right side is continuous in the Hausdorff metric on the bodies.
- *The degeneration step.* \(P(1,s)\ge0\) for \(s\ge0\) plus \(c_0=0\) gives \(c_1\ge0\);
  this needs \(P\) to be a genuine polynomial with the stated coefficients, i.e. it
  needs the volume theorem for the *sum*, which is where positivity of volume is used.
- *Where the whole of §3 could collapse:* the superadditivity inclusion. Flagged
  three times; it is the single load-bearing unconfirmed input.

---

## 6. Proposed ledger lines

- **Problem id:** `open_problems/xia_partial_okounkov_questions`. In-session solver
  pass, 15 August 2026; **no Rethlas receipt**; candidate-only; the account cap
  remains in force so no promotion is possible.
- **Q1 (Conjecture 5.29):** OPEN-AFTER-ATTEMPT. Unconditional at both endpoints
  (\(\mathrm{nd}=n\) is the positive-mass case by the volume theorem; \(\mathrm{nd}=0\)
  in one direction). The missing input is precise and should be recorded as such:
  the characterization of Cao's numerical dimension as the vanishing order of
  \(\mathrm m(\phi_\varepsilon)\) under ample perturbation. Contrary to expectation,
  surfaces are **not** easier — Zariski decomposition controls the class while
  \(\mathrm{nd}(L,\phi)\) depends on \(\phi\) beyond it.
- **Q2 (Conjecture 8.8): LITERATURE-RESOLVED — no new result.** Xia's *Mixed
  Volumes of Okounkov Bodies* proves the conjecture in full, as an equality, both
  algebraically (Theorem 1.1) and for singular metrics of positive volume
  (Theorem 1.2), and confirms the superadditivity input. The pass independently
  found a correct proof of the \(\ge\) half for two-bundle mixed terms — via
  superadditivity, homogeneity, and a first-order polynomial degeneration
  anchored on Xia's volume theorem — but that conclusion is subsumed by MVOB
  Theorem 1.2. It is **demoted from candidate grade, carries no priority claim,
  and must not be submitted for a receipt.** The book should cite MVOB for the
  full equality. Recorded as a literature-search failure, not a proof failure:
  MVOB was absent from the local reference pack and arXiv was unreachable during
  the pass.
- **Q3 (Chebyshev \(\eta\)-independence):** OPEN-AFTER-ATTEMPT, with two clean
  by-products: the admissible set is upward directed under \(\max\) (complete proof
  via \((\theta-\delta\omega)\)-psh), giving a common lower bound for the transform;
  and the squeeze **cannot** close, because admissibility is preserved by adding
  \(\log|s|\), so the admissible set is unbounded below in singularity and not
  downward directed. Reduced to a single analytic statement: asymptotic insensitivity
  of the transform to the singular part of the auxiliary datum as
  \(\varepsilon\downarrow0\).
- **Book disposition:** all three questions stay open in the research chapter. The
  Q2 half-inequality and the Q3 directedness facts may be mentioned as recorded
  candidate progress in the editorial ledger only; neither may appear in theorem
  typography, and no priority claim is made. If the superadditivity input is later
  confirmed against the source, the Q2 statement is the one worth submitting for a
  production receipt first, since its proof is short and self-contained.

**24 Aug 2026 controlling addendum to the preceding historical disposition.**
Q2 no longer stays open in its original positive-volume projective domain:
the separate repaired packet identified at the head of this dossier has an
exact production receipt.  Q1, Q3, all zero-volume questions, and the
transcendental, singular-variety, and attainment extensions remain open.
