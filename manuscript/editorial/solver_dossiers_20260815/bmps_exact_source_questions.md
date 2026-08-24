# Exact open directions in Botero--Mazzon--Pille-Schneider

**Problem id:** `open_problems/bmps_exact_source_questions`
**Solver pass:** in-session direct solve, 15 August 2026.
**Promotion status:** CANDIDATE-ONLY. No Rethlas receipt. Nothing enters theorem
typography.
**Source:** Botero--Mazzon--Pille-Schneider, arXiv:2603.08664v1 (submitted 9 March
2026, internally dated 10 March 2026). The preprint postdates the model's training
data and direct arXiv retrieval is blocked by the egress proxy here. **Every
source-numbered statement below is used exactly as transmitted by the packet and is
marked [from-packet]; none was independently verified.**

**Book inputs used, not re-proved** (already verified with receipts):
regularity and orthogonality of the polyhedral obstacle envelope on complete affine
\(N_{\mathbf R}\) in every dimension, with the exact normalization
\(\mathrm{MA}_{\mathrm{poly}}(P)=d!\,c\,\mathrm{MA}_{\mathbf R}(P)\); the strict
cross-fan counterexample \(\gamma=|x|+|y|\) on the four-ray fan in \(\mathbf R^2\),
whose orthogonality integral is \(-2\varepsilon\); and the conditional recursive
calibrated analytic comparison.

**Source map [from-packet]:** Theorem 6.4 characterizes regularity; Proposition 6.13
and Remark 6.6 give positive regularity loci; Proposition 6.21 and Theorem 6.22 give
the one-dimensional polyhedrally smooth theorem; Examples 6.23--6.24 and Remarks
6.26--6.27 give counterexamples and warnings; Proposition 7.2 has a specific toric
Calabi--Yau complete-intersection scope.

---

## 1. Conventions

\((X,\gamma)\) is a balanced polyhedral space of dimension \(d\) with a reference
function \(\gamma\); \(f\) is an obstacle; \(P=P_\gamma(f)\) is the envelope, the
largest \(\gamma\)-convex minorant of \(f\). *Regularity* is the property in Theorem
6.4 [from-packet]; *orthogonality* is
\[
  \int_X (P-f)\,\mathrm{MA}_{\mathrm{poly}}(P)=0 ,
\]
which, since \(P\le f\) and the measure is positive, is equivalent to
\(\mathrm{MA}_{\mathrm{poly}}(P)\) being carried by the contact set \(\{P=f\}\).
Normalizations are those of the book's verified affine core.

Every sufficient condition proposed below is checked against the cross-fan
counterexample, which must remain excluded.

---

## 2. Question 3 (matroids) — a complete structural answer in rank two

This is the strongest outcome of the pass, and it is elementary.

**Observation.** The Bergman fan of a matroid \(M\) of rank \(r\) is a balanced
polyhedral fan of dimension \(r-1\).

**Consequence (CANDIDATE-PROPOSITION).** For every **rank-two** matroid — in
particular every uniform matroid \(U_{2,n}\), \(n\ge3\) — the Bergman fan is
**one-dimensional**, and orthogonality follows from the source's own one-dimensional
theorem (Proposition 6.21 and Theorem 6.22 [from-packet]) whenever \(\gamma\)
satisfies the growth and strict-positivity hypotheses stated there. No new argument
is required.

Explicitly, for \(U_{2,n}\) the Bergman fan is the \(n\)-ray fan in
\(\mathbf R^n/\mathbf R(1,\dots,1)\cong\mathbf R^{n-1}\) spanned by the images
\(\bar e_1,\dots,\bar e_n\), which satisfy the single relation
\(\sum_i\bar e_i=0\); this is the balancing condition with all weights \(1\). For
\(n=3\) this is exactly the standard tropical line in \(\mathbf R^2\), the tripod.

**Reading of the U\(_{3,4}\) obstruction.** \(U_{3,4}\) has rank \(3\), so its Bergman
fan is **two-dimensional** — the first case not covered by the one-dimensional
theorem. The book's recorded finding, that for \(U_{3,4}\) the reference \(\gamma\)
vanishes on a line and is therefore neither strictly convex nor positive at
infinity, is thus a statement about the *reference*, not about the fan. Combining:

> The matroid question of Remark 6.27 [from-packet] is entirely a question about
> **rank \(\ge3\)**. In rank two it is closed by the source's own one-dimensional
> theorem, and the known failure at \(U_{3,4}\) is a failure of the growth hypotheses
> on \(\gamma\), not of the Bergman fan.

**Graphic matroid of \(K_4\).** Rank \(=|V|-1=3\), so the Bergman fan is
two-dimensional in \(\mathbf R^6/\mathbf R\cong\mathbf R^5\). It is therefore *not*
covered by the one-dimensional theorem and is a genuine test case, at the same rank
as \(U_{3,4}\) but with a different reference geometry. **OPEN-AFTER-ATTEMPT**; it is
the natural first rank-three target and is recommended for a future packet.

---

## 3. Question 1(a) (products) — split obstacles close

**Setup.** Let \((X_1,\gamma_1)\), \((X_2,\gamma_2)\) be balanced polyhedral spaces of
dimensions \(d_1,d_2\), each satisfying regularity and orthogonality (for instance,
each one-dimensional and polyhedrally smooth, by Theorem 6.22 [from-packet]). Give
\(X:=X_1\times X_2\) the product balanced structure and the reference
\(\gamma:=\gamma_1\oplus\gamma_2\), \((\gamma_1\oplus\gamma_2)(x,y)=\gamma_1(x)+\gamma_2(y)\).
Let the obstacle be **split**: \(f=f_1\oplus f_2\).

**CANDIDATE-PROPOSITION (split-obstacle orthogonality on a product).** With
\(d=d_1+d_2\), assume the two structural identities

- **(S1) the envelope splits:** \(P_\gamma(f_1\oplus f_2)=P_{\gamma_1}(f_1)\oplus P_{\gamma_2}(f_2)\);
- **(S2) the Monge--Ampère factorizes:**
  \(\mathrm{MA}_{\mathrm{poly}}(u_1\oplus u_2)
   =\binom{d}{d_1}\,\mathrm{MA}_{\mathrm{poly}}(u_1)\otimes\mathrm{MA}_{\mathrm{poly}}(u_2)\),
  the binomial arising from the book's factorial normalization
  \(\mathrm{MA}_{\mathrm{poly}}=d!\,c\,\mathrm{MA}_{\mathbf R}\) together with
  \(\det\) of a block-diagonal Hessian;

and assume both factor measures have finite mass. Then \((X,\gamma)\) satisfies
orthogonality for \(f\).

*Proof.* Write \(P_i:=P_{\gamma_i}(f_i)\), \(\mu_i:=\mathrm{MA}_{\mathrm{poly}}(P_i)\).
By (S1), \(P-f=(P_1-f_1)\oplus(P_2-f_2)\), i.e.
\((P-f)(x,y)=(P_1-f_1)(x)+(P_2-f_2)(y)\). By (S2),
\(\mathrm{MA}_{\mathrm{poly}}(P)=\binom{d}{d_1}\mu_1\otimes\mu_2\). Hence
\[
  \int_X(P-f)\,\mathrm{MA}_{\mathrm{poly}}(P)
  =\binom{d}{d_1}\Bigl[\ \lvert\mu_2\rvert\!\int_{X_1}\!(P_1-f_1)\,d\mu_1
   \ +\ \lvert\mu_1\rvert\!\int_{X_2}\!(P_2-f_2)\,d\mu_2\Bigr]=0,
\]
each bracketed integral vanishing by orthogonality on the factor. \(\square\)

**Why (S1) is reasonable, and where it must be checked.** The envelope is a supremum
of \(\gamma\)-affine minorants. On a product with a split reference, the relevant
affine functions are sums \(a_1(x)+a_2(y)+c\); for a separable obstacle the constant
splits, and the classical identity \(\operatorname{conv}(f_1\oplus f_2)=
\operatorname{conv}(f_1)\oplus\operatorname{conv}(f_2)\) applies verbatim. On complete
affine space this is standard. On a product of *fans* it requires that the
\(\gamma\)-affine functions on the product be exactly the sums — this is the one
place where the product of balanced spaces could misbehave, and it is flagged as the
step needing verification against BMPS's definition of the envelope operator.

**Scope discipline.** The proposition is stated **only** for split obstacles. For a
general obstacle on a product the envelope does **not** split — the mixed envelope is
not the sum of envelopes — and nothing above applies. The packet anticipated exactly
this restriction, and it is respected.

**Cross-fan check.** The counterexample \(\gamma=|x|+|y|\) on the four-ray fan is
*not* a product of two one-dimensional balanced spaces satisfying the hypotheses: the
four-ray fan in \(\mathbf R^2\) is one-dimensional, not a product of two
one-dimensional spaces, and its \(\gamma\) fails strict convexity. The proposition
therefore does not contradict it. This check is the reason the hypotheses are stated
as they are.

---

## 4. Question 1(b) (local smoothness) — where the affine proof fails to localize

Proposed condition: \((X,\gamma)\) is *locally polyhedrally smooth* if every
codimension-one face has a neighbourhood isomorphic, as a balanced space, to
\(\mathbf R^{d-1}\times C\) with \(C\) a one-dimensional polyhedrally smooth fan.

**Attempted transfer of the verified affine argument.** The affine proof on
\(N_{\mathbf R}\) runs: the envelope is the lower boundary of the closed convex hull
of the epigraph of a finite polyhedral obstacle; at every atom of the Alexandrov
measure of \(P\), an **interior subgradient exposes a unique minimizer**; maximality
of the convex minorant then forces contact with the obstacle; the global identity
\(\mathrm{MA}_{\mathrm{poly}}(P)=d!\,c\,\mathrm{MA}_{\mathbf R}(P)\) converts this into
orthogonality.

**First genuinely unsupported implication**, recorded verbatim: *"since the space is
locally a product with a smooth one-dimensional factor, the exposing subgradient may
be chosen in a neighbourhood of the face."*

The step fails because the exposing-subgradient argument is **global in the convex
hull**: a subgradient of the convex envelope at a point is determined by the entire
epigraph, and a supporting hyperplane constructed in a neighbourhood need not support
globally. On complete affine space the two coincide because every local supporting
affine function extends; on a fan with several unbounded directions it does not, and
this is precisely what the cross-fan counterexample exploits — there the local data
at each ray are unobjectionable and the failure is global, visible only in the
aggregate orthogonality integral \(-2\varepsilon\).

**Consequence, and a genuine constraint on the whole question.** Any correct
higher-dimensional smoothness hypothesis must be **global** in the recession/growth
behaviour of \(\gamma\), not merely local along faces. Purely local conditions cannot
suffice, because the cross-fan example is locally as smooth as one likes away from
the origin. This is a real narrowing of the search space for question 1 and should be
recorded as such.

**Disposition:** **OPEN-AFTER-ATTEMPT**, with the local-to-global obstruction
identified and purely local hypotheses excluded.

---

## 5. Question 2 (Calabi--Yau degenerations)

Known-in scope: the toric Calabi--Yau complete intersections of Proposition 7.2
[from-packet]. Beyond that, the honest formulation is a reduction rather than an
answer.

**Reduction.** For a polarized Calabi--Yau degeneration, the essential skeleton
carries an integral affine structure with singularities in codimension two. The
regularity/orthogonality package is a statement about the envelope of the obstacle
determined by the polarization against \(\gamma\). Since the failure mode isolated in
§4 is global and concentrated where the affine structure degenerates, the sharp
question is:

> For which polarized Calabi--Yau degenerations does the essential skeleton admit an
> integral affine structure whose singular locus is **disjoint from the contact set**
> \(\{P=f\}\) of the polarization obstacle?

For quartic K3 and quintic threefold degenerations the affine structures are known
(they are the standard sphere/\(S^3\) structures with singular loci a graph),
but locating the contact set relative to that graph was not carried out and is not
attempted here. **OPEN-AFTER-ATTEMPT.** No answer is fabricated.

---

## 6. Self-adversarial audit

- *Cross-fan respected?* Yes, §3 explicitly checks it and §4 uses it as the engine of
  the obstruction. No proposed sufficient condition admits it.
- *Weights and multiplicities.* §2 uses weights \(1\) on the Bergman fan of a uniform
  matroid, where the balancing relation is \(\sum\bar e_i=0\); for general rank-two
  matroids the weights are the matroid's and the balancing is the standard one — the
  dimension count \(r-1\) is weight-independent, so the reduction to the
  one-dimensional theorem is unaffected.
- *Non-unimodular cones.* Not used; §2 is a dimension statement.
- *Noncompact directions.* These are exactly the source of the §4 obstruction and are
  not suppressed.
- *Normalization drift.* §3 carries the binomial \(\binom{d}{d_1}\) explicitly rather
  than absorbing it; if BMPS normalize \(\mathrm{MA}_{\mathrm{poly}}\) differently the
  constant changes but the vanishing conclusion does not, since the bracket is zero.
- *Did §2 overclaim?* It concludes only for rank two and only subject to the
  \(\gamma\)-hypotheses of the source's one-dimensional theorem; it does not assert
  that those hypotheses hold for any particular \(\gamma\) on a given Bergman fan.

---

## 7. Dispositions

| Item | Disposition |
|---|---|
| Rank-two matroids (incl. all \(U_{2,n}\)) | **CANDIDATE-PROPOSITION** — dimension \(r-1=1\), reduces to the source's one-dimensional theorem, §2 |
| Reading of the \(U_{3,4}\) failure | **CANDIDATE-PROPOSITION** — a failure of \(\gamma\)'s growth hypotheses at rank three, not of the fan, §2 |
| Graphic matroid \(K_4\) | **OPEN-AFTER-ATTEMPT**; first genuine rank-three target |
| Products, split obstacle | **CANDIDATE-PROPOSITION** modulo (S1), (S2), §3 |
| Products, general obstacle | **OPEN**; the envelope does not split |
| Local polyhedral smoothness in higher dimension | **OPEN-AFTER-ATTEMPT**; purely local hypotheses provably insufficient, §4 |
| Calabi--Yau degenerations | **OPEN-AFTER-ATTEMPT**, with a sharp reduction, §5 |

---

## 8. Proposed ledger lines

- **Problem id:** `open_problems/bmps_exact_source_questions`. In-session solver
  pass, 15 August 2026; **no Rethlas receipt**; candidate-only. The source is a
  post-training preprint that could not be fetched; all source numbering is
  from-packet and unverified.
- **Matroid question resolved in rank two:** the Bergman fan of a rank-\(r\) matroid
  has dimension \(r-1\), so every rank-two matroid — in particular every
  \(U_{2,n}\) — has a one-dimensional Bergman fan and falls under the source's own
  one-dimensional regularity/orthogonality theorem. Remark 6.27's question is
  therefore a question about rank \(\ge3\) only.
- **Reinterpretation of \(U_{3,4}\):** it has rank three, hence a two-dimensional
  Bergman fan; the book's recorded failure there is a failure of the growth and
  strict-positivity hypotheses on \(\gamma\), not an obstruction carried by the fan.
  The graphic matroid of \(K_4\) is the recommended next rank-three test.
- **Products:** candidate proof that a product of two spaces with
  regularity/orthogonality satisfies orthogonality for **split** obstacles, by
  splitting of the envelope and factorization of the Monge--Ampère measure with the
  binomial normalization \(\binom{d}{d_1}\); the general product obstacle is out of
  scope because the mixed envelope is not the sum of envelopes. Load-bearing
  unverified inputs: (S1) and (S2).
- **Structural constraint on question 1:** purely local smoothness hypotheses cannot
  suffice in higher dimension. The verified affine proof turns on an interior
  subgradient exposing a unique minimizer, which is global in the convex hull; the
  cross-fan counterexample is locally smooth away from the origin and fails only in
  the aggregate. Any correct hypothesis must constrain global recession/growth
  behaviour of \(\gamma\).
- **Calabi--Yau question:** open, reduced to whether the singular locus of the
  essential skeleton's integral affine structure can be made disjoint from the
  contact set of the polarization obstacle.
- **Book disposition:** all three source questions remain open in the research
  chapter, in their corrected scopes. The rank-two reduction and the split-product
  result may be recorded in the editorial ledger as candidate progress only. No
  priority claim; the book-formulated intrinsic singular-fan contact theorem and the
  recursive calibrated comparison remain separate and unproved.
