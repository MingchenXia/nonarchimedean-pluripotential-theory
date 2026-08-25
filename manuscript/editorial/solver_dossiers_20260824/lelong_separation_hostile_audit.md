# Hostile audit: generalized Lelong numbers separate valuative transforms

Date: 24 August 2026.  Object audited:

- `manuscript/editorial/solver_dossiers_20260824/lelong_separation_candidate.md`;
- `manuscript/editorial/rethlas_packets_20260824/ch70_lelong_separation_candidate_statement.tex`;
- `manuscript/editorial/rethlas_packets_20260824/ch70_lelong_separation_candidate_source_aware_proof.tex`.

No live chapter was edited.

## Verdict

**Pass: no mathematical flaw was found.**  In particular, none of the seven
suspected failure points produces a counterexample.  The proof is a valid
finite-model separation argument once BFJ's exact Proposition 1.14 and the
one-Weil-input clause implicit in Propositions 4.6 and 4.9 are used.  The
intersection form

\[
              (D,C)\longmapsto D\cdot C\cdot A^{n-2}
\]

is indeed negative definite on the coefficient space of divisors supported
over the point when \(A\) is relatively ample.  Thus the conclusion is literal
pointwise equality on the full normalized valuation space, not merely equality
on the divisorial or quasimonomial locus.

This is a mathematical verdict on the supplied proof, not a novelty or
priority verdict.  BFJ explicitly left the implication open, and the later
relative-type/Zhou-weight literature recorded in the manuscript does not by
itself supply a priority comparison for this argument.

## Primary-source audit

The official PRIMS PDF of Boucksom--Favre--Jonsson, *Valuations and
plurisubharmonic singularities*, PRIMS 44 (2008), 449--494, was inspected
directly.  The inspected file has SHA-256

`c7e8757e1e63ad0989f3fa3619094abc9352429dd7572116e0f65c0cd5a2033a`.

The exact relevant statements are:

1. On printed pp. 450--451 BFJ state Theorem A and say that they expect
   condition (4), equality of generalized Lelong numbers for all tame psh
   weights, to imply the other conditions.  The implication was therefore not
   already a theorem in that paper.
2. On printed pp. 458--459, for a projective modification
   \(X_\pi\to X\) above the point, BFJ identify the coefficient space of
   exceptional divisors with \(NS(X_\pi/X)_{\mathbf R}\).  In particular an
   exceptional divisor is determined by its relative numerical class.
3. Proposition 1.14 on printed p. 466 says exactly that
   \(\operatorname{C-Div}(\mathfrak X)\simeq PA(\mathcal V)\), and that the
   integral subgroup \(PA(\mathcal V)_{\mathbf Z}\) is the subgroup generated
   by the functions \(\log|\mathfrak a|\) for primary ideals
   \(\mathfrak a\).  This is exact group generation; it is not merely the
   uniform-density statement of Proposition 1.15.
4. Proposition 2.2 on printed p. 469 identifies nef Cartier b-divisors with
   relatively nef incarnations.  Proposition 2.4 supplies trace monotonicity
   and, in particular, the coefficientwise negativity of a nonzero nef
   exceptional b-divisor.
5. Proposition 3.11 on printed pp. 474--475 gives the unique formal-psh
   function of a nef Weil divisor and continuity on each simplex.  Definition
   2.8 on printed p. 470 is the extension
   \(g(\nu)=\inf_\pi g(r_\pi(\nu))\).
6. Proposition 4.6 on printed p. 482 represents the mixed intersection by the
   Monge--Ampere measure.  Proposition 4.9 on printed p. 483 computes the
   piecewise-affine case atomically and then explicitly observes that the
   intersection of nef Weil divisors is finite when all but at most one input
   are Cartier.
7. Lemma 5.10 on printed p. 487 makes an ideal weight tame when its
   exponential is Holder.  Theorem B, stated on p. 455 and proved on
   pp. 490--492, is the generalized-Lelong/intersection formula used by the
   candidate.

For the global input, the Hodge--Riemann statement was checked against
Claire Voisin, *On the cohomology of algebraic varieties*, Section 2.2.1,
Theorem 2.12.  On \(H^{1,1}_{\mathbf R}\), and hence on the Neron--Severi
space, it gives one positive direction and a negative-definite primitive
hyperplane for the form \(L_1L_2H^{n-2}\).  The inspected author-hosted PDF
has SHA-256

`26b374e2710a9223100aee4a414c4377b4b38cd7de7d42cf95d129f41823748e`.

## Audit of the suspected failure points

### 1. Scope of BFJ Proposition 1.14

The candidate uses the proposition within its exact scope.  If
\(\mathcal C_{\mathbf Z}\) denotes the integral exceptional Cartier b-divisor
group, then

\[
 \mathcal C_{\mathbf Z}
 =\left\langle Z(\mathfrak a):\mathfrak a
          \text{ is }\mathfrak m\text{-primary}\right\rangle_{\mathbf Z}.
\]

Tensoring with \(\mathbf R\) is legitimate because every real Cartier
b-divisor is determined on a finite model and its exceptional-prime
coefficient vector is finite dimensional.  No completion or density argument
is being smuggled in.

The passage from a complex analytic germ to the ideals used here causes no
gap.  Polynomial primary ideals already give the BFJ generators and define
analytic psh weights.  Conversely, any finite analytic primary ideal is
finitely determined modulo a high power of \(\mathfrak m\), if one wants a
polynomial representative.

### 2. One Weil input and arbitrary Cartier slots

Let \(W\) be a nef Weil b-divisor and let \(C_1,\ldots,C_{n-1}\) be Cartier
b-divisors determined on \(X_\pi\).  The formula

\[
 I_W(C_1,\ldots,C_{n-1})
   =W_\pi(C_1)_\pi\cdots(C_{n-1})_\pi
\]

is independent of \(\pi\): on a higher model \(\mu:X_{\pi'}\to X_\pi\),
one has \(\mu_*W_{\pi'}=W_\pi\), while all \(C_i\) pull back, so the ordinary
projection formula applies.  This defines a symmetric multilinear form in
the Cartier slots even when they are signed.

When the \(C_i\) are nef, BFJ Proposition 4.6 identifies this number with
the integral against the mixed Monge--Ampere measure; Proposition 4.9 gives
the atomic trace calculation and explicitly licenses the one-Weil-input
domain.  The candidate never forms an intersection containing two signed
non-Cartier Weil inputs.  This suspected flaw is absent.

### 3. Polarization

Equality of generalized Lelong numbers for the analytic primary-ideal weight

\[
 \varphi_{\mathfrak a}=\log\max_j|f_j|
\]

gives

\[
 \Lambda(Z(\mathfrak a),\ldots,Z(\mathfrak a))=0.
\]

For primary \(\mathfrak a_i\) and positive integers \(k_i\), the product
\(\prod_i\mathfrak a_i^{k_i}\) remains primary, and its divisor is
\(\sum_i k_iZ(\mathfrak a_i)\).  Consequently the diagonal polynomial

\[
 P(t)=\Lambda\left(\sum_i t_iZ(\mathfrak a_i),\ldots,
                    \sum_i t_iZ(\mathfrak a_i)\right)
\]

vanishes on all of \(\mathbf Z_{>0}^s\), hence is identically zero.  Because
\(\Lambda\) is symmetric, each coefficient is the appropriate nonzero
multinomial factor times the corresponding mixed value.  Proposition 1.14
then extends the mixed vanishing to all real Cartier inputs.

There is no analytic polarization hidden here.  Only actual diagonal tame
weights are inserted into Theorem B; polarization occurs afterward in a
finite multilinear intersection space.

### 4. Existence and sign of an exceptional relatively ample divisor

Every BFJ model is projective over \(X\).  Choose a relatively ample Cartier
divisor \(H_0\) on \(X_\pi\).  Since the smooth base is locally factorial,
\(\pi_*H_0\) is Cartier after shrinking around the point.  Then

\[
                     A=H_0-\pi^*(\pi_*H_0)
\]

is an exceptional Cartier divisor, and it is still relatively ample because
the subtracted pullback is relatively numerically trivial.  Thus one can take
\(A\) integral; the weaker real-divisor construction in the packet is also
valid.

The sign agrees with BFJ: \(Z(\mathfrak a)\leq0\), and on the blowup of a
smooth point \(A=-E\) is relatively ample and nef as a Cartier b-divisor.

### 5. Negative definiteness in every dimension

The claim is correct.  Compactify without modifying a neighborhood of the
exceptional fibre to a projective birational morphism
\(\bar\pi:\bar Y\to\bar X\) of smooth projective \(n\)-folds.  Choose a
\(\bar\pi\)-ample divisor \(\bar A\) whose relative class on the original
neighborhood has exceptional representative \(A\).  For an ample \(B\) on
\(\bar X\), after scaling \(B\),

\[
                       H=\bar A+\bar\pi^*B
\]

is ample.  If \(D,C\) are supported over the point, then

\[
                 DC H^{n-2}=DC A^{n-2}.
\]

Indeed \(\bar A-A\) is relatively numerically trivial on the fibre, and every
term containing \(\bar\pi^*B\) vanishes because this line bundle restricts
trivially to every subvariety of the fibre.  This also proves

\[
                  D\cdot\bar\pi^*B\cdot H^{n-2}=0.
\]

The class \(\bar\pi^*B\) is nef and big, so
\((\bar\pi^*B)^2H^{n-2}>0\).  Hodge--Riemann gives signature
\((1,\rho(\bar Y)-1)\) for \(q_H(L,M)=LMH^{n-2}\); hence its restriction to
the orthogonal complement of \(\bar\pi^*B\), and therefore to the numerical
span of the exceptional divisors, is negative definite.  Finally, a nonzero
exceptional coefficient vector cannot be globally numerically zero, since
global numerical triviality would imply relative numerical triviality and
BFJ Section 1.2 identifies
\(\operatorname{Div}(\pi)\) injectively with \(NS(X_\pi/X)_{\mathbf R}\).
It follows that

\[
                      Q_A(D,C)=DCA^{n-2}
\]

is negative definite on the actual coefficient space
\(\bigoplus_E\mathbf R E\), not merely on a quotient.

The blowup check is dimension-independent:

\[
 E^2(-E)^{n-2}=(-1)^{n-2}E^n=-1,
 \qquad E^n=(-1)^{n-1}.
\]

### 6. Compactification and cross terms

No cross term survives.  The important reason is stronger than mere
exceptionality: every divisor under consideration is supported in the single
proper fibre \(\pi^{-1}(0)\).  The compactification can be chosen to be an
isomorphism near that fibre, so the local components and their intersection
numbers are unchanged.  On any intermediate cycle supported in the fibre,
the restriction of a divisor pulled back from \(\bar X\) is numerically
trivial.  The expansion of \(DCH^{n-2}\) therefore reduces term by term to
\(DCA^{n-2}\).

For a publication version, it would help to add the one sentence
"\(\bar\pi^*B\) is nef and big, hence
\((\bar\pi^*B)^2H^{n-2}>0\)" before invoking the orthogonal-complement
argument.  This is an exposition improvement, not a repair of a gap.

### 7. From finite traces to every valuation

For a fixed simple model, mixed vanishing with
\((C,A,\ldots,A)\) gives

\[
 0=(Z(u)_\pi-Z(v)_\pi)CA^{n-2}
\]

for every exceptional \(C\).  Negative definiteness implies
\(Z(u)_\pi=Z(v)_\pi\).  Simple modifications are cofinal, so equality on all
such models is equality of the Weil b-divisors and, in particular, equality
at every divisorial valuation.

On any fixed quasimonomial simplex, rational-weight points are divisorial
after a toroidal blowup and are dense.  BFJ Proposition 3.11 makes both formal
psh functions continuous on the simplex, so they agree throughout the
quasimonomial locus.  For arbitrary normalized \(\nu\), Definition 2.8 gives

\[
 \widehat u(\nu)=\inf_\pi\widehat u(r_\pi\nu),\qquad
 \widehat v(\nu)=\inf_\pi\widehat v(r_\pi\nu).
\]

Every retracted point is quasimonomial, so the two infima are termwise equal.
This proves pointwise equality even when the common value is \(-\infty\).

## Skill/non-trigger check

The `lelong-clean-moving-singular-limit` hypotheses are unnecessary here.
There is no weakly convergent current, moving logarithmic kernel, residual
Lelong density, or exchange of singular limits.  The proof is entirely an
exact finite-model intersection argument.  Thus that mechanism correctly
stops at its non-trigger boundary and supplies no unmentioned analytic
continuity claim.

## Recommended disposition

The candidate may be promoted mathematically after an independent novelty
search appropriate to a result resolving a question explicitly left open in
BFJ.  Preserve the full polarization argument and the one-Weil-input
restriction.  In the compactification paragraph, add the explicit
nef-and-big positivity sentence noted above and retain the explanation that
all cross terms vanish because the exceptional support maps to one point.
