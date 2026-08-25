# GJR semipositive integral decomposition: audited curve case

> **Superseded status (25 August 2026).**  This dossier remains the audit
> record for the positive curve theorem.  Its statements that P09.1 remains
> globally open are historical: production runs
> `20260825T130036Z_c1607c25ec38` and
> `20260825T130707Z_4c4a1f2c885f` respectively verify signed generation in
> arbitrary residual dimension and disprove nonnegative-cone generation in
> residual dimension two.  P09.1 is therefore retired.

## Purpose and disposition

This note audits the curve argument in
`manuscript/editorial/solver_dossiers_20260815/gjr_three_questions.md`,
recovers the exact Gubler--Jell--Rabinoff source statement, and replaces the
candidate branch-gluing proof by a residue-model proof.

The result below proves the natural positive-cone version of the question for
good rig-smooth strict analytic curves, over an arbitrary complete
nontrivially valued ground field.  It therefore closes the **curve subcase**.
It does not settle the higher-dimensional question.  Accordingly, inventory
atom **P09.1 remains globally active**: its one-dimensional stratum is proved
here, while dimensions at least two remain open.

This is an internal deduction from the cited GJR results, not an assertion
that the curve theorem already appears in the literature.

## Primary-source attestation

The local primary source is

`Rethlas_isolated_20260813_232740/agents/generation/data/open_problems/gjr_three_questions.refs/Gubler_Jell_Rabinoff_2111.05741.pdf`,

the locally archived arXiv v3 PDF of W. Gubler, P. Jell, and J. Rabinoff,
*Forms on Berkovich spaces based on harmonic tropicalizations*.

The exact source formulation is deliberately brief.  On printed page 46,
immediately before Proposition 7.5, the authors write:

> We do not know if the same characterization holds for semipositive
> functions.

Proposition 7.5 then says that a \(\Lambda\)-PL function \(h\) is harmonic at
\(x\) if and only if, on a strictly analytic neighbourhood \(U\) of \(x\),
one has a finite decomposition
\[
             h|_U=\sum_{i=1}^m\lambda_i h_i,
\]
where \(\lambda_i\in\Lambda\) and the \(h_i\) are \(\mathbf Z\)-harmonic on
\(U\).

The source does **not** state the coefficient signs in a proposed
semipositive analogue.  GJR Remark 7.3(5), printed page 45, says that
semipositive germs form a monoid (a cone when \(\Lambda=\mathbf R\)), whereas
harmonic germs form a group.  Thus the only formulation for which both
directions express semipositivity is the positive-cone formulation with
coefficients in \(\Lambda_{\geq0}\).  This sign condition is a necessary
formalization of the source question, not a verbatim condition imposed by
GJR.

The proof below uses the following exact source locators.

1. Definition 5.1, printed page 31: \(\Lambda\)-PL functions.
2. Proposition 5.8, printed page 33: analytic-locally, a
   \(\Lambda\)-PL function is a finite \(\Lambda\)-linear combination of
   \(\mathbf Z\)-PL functions, for \(\Lambda=\mathbf Z\) or divisible.
3. Sections 6.2 and 6.6 and Lemma 6.5, printed pages 37--38: models of a
   quasi-compact open subset of a Riemann--Zariski space form a filtered
   system, and finitely many residue line bundles can be represented on a
   common model.
4. Definition 6.7 and Definition 6.9, printed pages 38--40: nefness is tested
   by degrees on integral proper closed curves.
5. Lemma 6.18, printed pages 43--44: the residue map on PL germs is
   \(\Lambda\)-linear.
6. Proposition 7.1, printed pages 44--45: a \(\Lambda\)-PL germ is
   semipositive, respectively harmonic, exactly when its residue is nef,
   respectively numerically trivial; the proof realizes the residue by a
   nef, respectively numerically trivial, formal model after shrinking.
7. Remark 7.3(3)--(5), printed page 45: the conditions are germ-local, their
   loci are open, and the relevant algebraic structures are a monoid/cone
   versus a group/vector space.
8. Proposition 7.5, printed page 46: the harmonic integral-decomposition
   theorem and the adjacent open sentence.
9. Section 15.4 and Proposition 15.5, printed page 78; Proposition 15.7,
   printed pages 78--79; Section 15.8, printed page 79; and Proposition 15.9,
   printed page 80: the curve skeleton, boundary, value-group, and integral
   graph-realization statements relevant to auditing the rejected proof.

## Precise positive-cone formulation

For a point \(x\) of a good strictly \(K\)-analytic space \(X\), let
\(\operatorname{SP}_\Lambda(X,x)\) be the monoid of germs at \(x\) of
\(\Lambda\)-PL functions semipositive at \(x\).  By GJR Remark 7.3(4), such a
germ has a representative semipositive on an analytic neighbourhood of
\(x\).

> **Theorem (curve case of the positive integral-decomposition question).**
> Let \(K\) be a complete non-Archimedean field with nontrivial valuation,
> let \(X\) be a good rig-smooth strictly \(K\)-analytic curve, with boundary
> allowed, and let \(\Lambda=\mathbf Z\) or let \(\Lambda\subset\mathbf R\)
> be a divisible additive subgroup containing \(1\).  Then, for every
> \(x\in X\),
> \[
>   \operatorname{SP}_\Lambda(X,x)
>     =\Lambda_{\geq0}\operatorname{SP}_{\mathbf Z}(X,x),
> \]
> where the right side means finite sums.  More explicitly, if \(h\) is
> \(\Lambda\)-PL and semipositive at \(x\), then there are a single strictly
> analytic neighbourhood \(W\) of \(x\), finitely many
> \(a_j\in\Lambda_{\geq0}\), and semipositive \(\mathbf Z\)-PL functions
> \(g_j\) on \(W\) such that
> \[
>                         h|_W=\sum_j a_jg_j.
> \]
> All but at most one of the \(g_j\) may be chosen \(\mathbf Z\)-harmonic on
> \(W\).

The theorem has no algebraic-closedness assumption and no containment
assumption relating the coefficient group \(\Lambda\) to the value group
\(\Gamma=v(K^\times)\).  It has no density or discreteness assumption on
\(\Gamma\).  For \(\Lambda=\mathbf Z\), the bare equality is formally
trivial by taking \(h=1\cdot h\); the substantive assertion concerns
divisible coefficient groups larger than \(\mathbf Z\), as well as the
strengthening that all but at most one integral piece can be harmonic.

The locality is the analytic locality used in GJR Proposition 7.5: all
representatives and all positivity conditions hold on one common strictly
analytic neighbourhood.  It is not merely an equality of abstract slope
vectors or an equality on a G-cover.

## Proof

Fix \(x\in X\) and a \(\Lambda\)-PL function \(h\) semipositive at \(x\).
By GJR Proposition 5.8, after replacing \(X\) by a strictly analytic
neighbourhood \(U\) of \(x\), write
\[
                         h=\sum_{i=1}^m\lambda_i h_i,
       \qquad \lambda_i\in\Lambda,\quad h_i\in\operatorname{PL}(U).
\]
Thus the \(h_i\) are actual \(\mathbf Z\)-PL functions on a common
neighbourhood, not formal slope vectors.

By GJR Lemma 6.18,
\[
             L_h(x)=\sum_{i=1}^m\lambda_iL_{h_i}(x)
             \quad\hbox{in }\operatorname{Pic}(\operatorname{red}(X,x))_\Lambda.
\]
Represent the finitely many integral residue classes \(L_{h_i}(x)\) on one
common model \(V\) of \(\operatorname{red}(X,x)\), using the filtered-model
statement in GJR Lemma 6.5 and Section 6.6.  Write \(L_i\in\operatorname{Pic}(V)\)
for the resulting line bundles.

Because \(X\) is a curve,
\[
        \dim V\leq
        \operatorname{trdeg}_{\widetilde K}\widetilde{\mathcal H(x)}
        \leq1.
\]
There are two cases.

### Case 1: no proper curve in the residue model

If \(\dim V=0\), or if \(\dim V=1\) and \(V\) is not proper, then \(V\) has
no integral proper closed curve.  Indeed, a one-dimensional integral closed
subscheme of the integral curve \(V\) would be \(V\) itself.  The nef and
numerically trivial conditions of GJR Definitions 6.7 and 6.9 are therefore
vacuous.  Each \(L_i\) and \(-L_i\) is nef, so every \(h_i\) is harmonic at
\(x\) by Proposition 7.1.

Writing
\[
       \lambda_i=\lambda_i^+-\lambda_i^-,
       \qquad \lambda_i^+=\max(\lambda_i,0),\quad
              \lambda_i^-=\max(-\lambda_i,0),
\]
gives
\[
              h=\sum_i\lambda_i^+h_i+\sum_i\lambda_i^-(-h_i),
\]
a positive-coefficient decomposition into integral functions harmonic at
\(x\).

This case includes boundary points whose one-dimensional reduction model is
affine; compare GJR Proposition 15.5(2).

### Case 2: a proper residue curve

Otherwise \(V\) is a proper integral curve.  Put
\[
                    d_i=\deg L_i\in\mathbf Z,
                    \qquad d=(d_1,\ldots,d_m).
\]
On an integral proper curve, a line bundle is nef exactly when its degree is
nonnegative, and it is numerically trivial exactly when its degree is zero.
Since \(h\) is semipositive at \(x\), Proposition 7.1 gives the single
inequality
\[
                    D:=\deg L_h(x)=\sum_i d_i\lambda_i\geq0.
\]

If \(d=0\), every \(h_i\) is harmonic at \(x\), and the sign-splitting
argument from Case 1 applies.  Suppose \(d\neq0\).  Let
\[
                       \delta=\gcd(d_1,\ldots,d_m)>0,
                       \qquad \ell=d/\delta:\mathbf Z^m\longrightarrow\mathbf Z.
\]
The homomorphism \(\ell\) is primitive.  Choose \(u\in\mathbf Z^m\) with
\(\ell(u)=1\), and choose a \(\mathbf Z\)-basis
\(v_1,\ldots,v_{m-1}\) of \(\ker\ell\).  Then
\[
                         \mathbf Z^m=\mathbf Zu\oplus\ker\ell.
\]
The same unimodular coordinate change over \(\Lambda\) gives a unique
decomposition
\[
        \lambda=(\lambda_1,\ldots,\lambda_m)
              =tu+\sum_{j=1}^{m-1}c_jv_j,
        \qquad
        t=\ell(\lambda)=D/\delta\in\Lambda_{\geq0},
        \quad c_j\in\Lambda.
\]
There is no hidden division issue: the coordinates of \(\ell\) are
integers, so \(t=\ell(\lambda)\) lies in \(\Lambda\); the inverse basis
change is integral as well.

Define actual integral PL functions on \(U\) by
\[
                   q=\sum_i u_i h_i,
                   \qquad r_j=\sum_i(v_j)_i h_i.
\]
Their residue line bundles on the chosen model \(V\) are the corresponding
integral tensor combinations of the \(L_i\), and
\[
                      \deg L_q(x)=\delta>0,
                      \qquad \deg L_{r_j}(x)=0.
\]
Therefore \(q\) is semipositive at \(x\), while every \(r_j\) and
\(-r_j\) is harmonic at \(x\).  Splitting each \(c_j\) by sign yields
\[
            h=tq+
              \sum_j c_j^+r_j+
              \sum_j c_j^-(-r_j),
              \qquad c_j^\pm\in\Lambda_{\geq0}.
\]
This is the required positive integral decomposition at the level of germs,
with only \(q\) possibly nonharmonic.

Finally, there is no omitted model-realization step.  GJR Proposition 7.1
turns nef or numerically trivial residue data into a nef or numerically
trivial formal model on a neighbourhood.  By GJR Remark 7.3(4), the
semipositivity locus of \(q\) and the harmonicity loci of the finitely many
\(\pm r_j\) are open.  Intersect these finitely many loci and choose a good
strictly analytic neighbourhood \(W\subset U\) of \(x\).  All displayed
functions then have the asserted positivity on the same \(W\), and their
identity remains valid there.

The precise degree ledger is
\[
                         t\deg L_q(x)=t\delta=D.
\]
Thus the coefficient-scaled positive piece contributes exactly the full
degree of \(h\).  No bound on the unscaled positive integral piece follows.
This completes the proof.

## Audit of the rejected candidate proof

The conclusion of Proposition A in the 2026-08-15 dossier is salvageable
after deleting its claimed degree bound and broadening its ground-field
scope.  Its written proof is not complete.  The following six points must
not be carried into a source-aware packet.

### 1. The special-fibre gluing is not a formal-model realization

The construction in lines 42--46 glues
\(\mathcal O_{C_x}(v-w)\), respectively \(\mathcal O_{C_x}(w)\), on one
component of the special fibre to trivial bundles on the other components.
That does not by itself construct a line bundle on the formal scheme
\(\mathfrak Y\), much less a line bundle equipped with a chosen trivialization
on the generic fibre, which is what membership in \(M(\mathfrak Y)\) requires.
The extension and generic-triviality assertions are both missing.

The phrase “slope along the branch at \(v\) equals the local degree at
\(v\)” is also not the precise GJR model statement.  GJR Section 15.4 gives
a canonical vertical Cartier divisor from a compatible
piecewise-\((\mathbf Z,\Gamma)\)-linear skeleton function, and Proposition
15.9 realizes harmonic graph functions.  A graph-based repair would have to
invoke those results and check all vertex constraints.  The residue proof
above instead uses Proposition 7.1, which supplies exactly the missing
formal-model realization.

### 2. Equality of slopes omits the additive constant

The formula in lines 44--46 matches the outgoing slopes at the central
point, but a PL germ on a star is determined by its central value as well as
its slopes.  The proof neither normalizes \(h(x)=0\) nor decomposes the
constant germ.  Hence the displayed equality is, as written, only equality
modulo an additive constant.  Proposition 5.8 in the proof above retains
the complete functions and automatically carries their constant terms.

### 3. The asserted degree bound is false

Proposition A claims that the one possibly nonharmonic integral piece can
have residue degree at most the degree of the residue of \(h\).  In the
candidate construction the unscaled spike \(p_w\) has degree \(1\).  If the
total degree \(S\) of \(h\) belongs to \((0,1)\), then
\(1\nleq S\).  The correct invariant statement is the scaled identity
\[
                    \text{coefficient}\times
                    \text{integral degree}=\deg L_h(x),
\]
namely \(t\delta=D\) in the proof above.

### 4. The discrete-value-group type-3 correction is wrong

Line 52 says that kinks of model functions may occur at type-3 points when
the value group is discrete.  GJR Sections 15.3--15.4 require admissible
subdivision vertices to lie in \(\Sigma(\sqrt\Gamma)\); these vertices are
type 2, not type 3.  Thus an integral model-PL germ at a type-3 point is
affine and harmonic.  GJR Section 15.8 introduces the auxiliary graph-vertex
group
\[
       \Gamma_{\mathrm{vert}}=
       \begin{cases}
          \Gamma,&\Gamma\text{ dense},\\
          \sqrt\Gamma,&\Gamma\text{ discrete},
       \end{cases}
\]
which must not be confused with the coefficient group \(\Lambda\).  The
residue proof above avoids any graph-vertex assumption.

### 5. The proposed weighted generators fail integrally

For a non-algebraically-closed field, line 52 proposes the generators
\(d_we_v-d_ve_w\) and \(e_v\) for the weighted half-space
\(\sum_vd_v\lambda_v\geq0\).  They work over a divisible positive
coefficient group after rational division, but need not generate the
integral semigroup.

For example, with weights \((2,3)\), the integral vector \((-1,1)\) has
weighted degree \(1\).  It does not belong to the nonnegative
\(\mathbf Z\)-monoid generated by \((3,-2)\), \((-3,2)\), \(e_1\), and
\(e_2\).  Indeed, writing its harmonic part with parameter \(k\) forces the
two remaining coordinate coefficients to be \(-1+3k\) and \(1-2k\), which
cannot both be nonnegative for an integer \(k\).  The bare
\(\Lambda=\mathbf Z\) statement is trivial, while the proof above uses a
Bezout vector \(u\) adapted to the finite degree vector arising from the
given decomposition and works uniformly.

### 6. The type-by-type locality discussion is under-sourced and incomplete

Lines 34--40 invoke a finite star and assert that type-1 and type-4 PL germs
are constant, without supplying the needed local-model theorem.  More
importantly, the type-2 discussion assumes a proper residue curve and hence
addresses an interior point.  At a boundary type-2 point the reduction is
affine and the nef condition is vacuous, as GJR Proposition 15.5(2)
explicitly records.  The branch description also identifies a germ only
after its additive constant is fixed.

None of this type classification is needed.  The dichotomy “the common
residue model contains no proper curve / it is a proper integral curve” is
intrinsic, includes boundary points, incorporates residue-degree weights
over non-algebraically-closed fields, and gives the complete proof above.

## Value-group and locality ledger

- **Coefficient cone:** finite positive sums with
  \(a_j\in\Lambda_{\geq0}\).  Unrestricted signs are not a semipositive
  analogue because the semipositive monoid is not symmetric.
- **Coefficient group:** \(\Lambda=\mathbf Z\), or a divisible additive
  subgroup of \(\mathbf R\) containing \(1\), exactly the standing scope in
  the introductory form of GJR Propositions 1.5--1.6.
- **Valuation:** nontrivial, as in the GJR strict analytic setup used here.
- **Value group:** no assumption that \(\Gamma=v(K^\times)\) is dense or
  discrete and no assumption \(\Gamma\subset\Lambda\).  The only
  \(\Gamma\)-constraints arise in the rejected skeleton realization route.
- **Ground field:** completeness is required; algebraic closedness is not.
- **Curve:** good, rig-smooth, and strictly analytic; analytic boundary is
  allowed.
- **Locality:** equality and positivity hold on one common strictly analytic
  neighbourhood, after a finite intersection of the open positivity loci.

## Inventory consequence

This packet proves a genuine, nonvacuous one-dimensional theorem.  It may be
cited to mark the **curve case of P09.1 as resolved**.  It must not be used to
close P09.1 itself.

In dimension at least two, a common model of
\(\operatorname{red}(X,x)\) can contain many proper curves, and nefness is
then an intersection of potentially infinitely many rational half-spaces.
The resulting nef cone need not be rational polyhedral.  The one-degree
Bezout argument above therefore stops precisely at dimension one and gives
no positive integral generation theorem in higher dimension.

**Historical inventory status at the date of this packet:** P09.1 remained
`[T2; open]` globally, with its curve subcase closed.  The superseding
25 August record above is controlling.
