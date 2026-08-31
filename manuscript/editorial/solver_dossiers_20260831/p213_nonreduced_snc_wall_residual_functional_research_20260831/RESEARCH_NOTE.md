# Residual divisor tests for a regular SNC model with multiplicities

Date: 31 August 2026. Author: /root/p213_skeletal_hostile.
Status: authored conditional research proof. Frozen only when the companion manifest exists; fresh independent review and production verification are separate requirements.

## 1. Scope, conditional input, and provenance

This packet extends the all-selected-vertical wall calculation to an ACTUAL proper regular model whose special fibre has strict-normal-crossing SUPPORT and arbitrary positive multiplicities. It does not replace that model by a reduced semistable model or a normal-cone product, extract a root of a formal unit, or change the field on which an unknown current is given.

The following local analytic result is an EXPLICIT CONDITIONAL PREMISE, denoted (L):

- sibling p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md;
- SHA-256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a;
- author /root.

Precisely, for a tube given by a bounded formal unit times \(x^m\prod z_j^{a_j}=\pi\), (L), Sections 2-5, supplies the actual finite flat degree-m coordinate projection, properness over the open tropical polyhedron, the constant positive closed-current pushforward coefficient, and canonical coefficient \(m[L:K]\) when the coefficient field is finite over K. Its Sections 6-7 are used ONLY in the final source-cell interpretation, together with the separate source representation premise (R). No acceptance of (L) or (R) is silently promoted by writing this packet.

The geometric completed-ring presentation, global radii, bad-point set, domination of deformation terms, compact primitive, divisor relation, and change of omitted normal coordinate are proved below. The preceding strictly semistable proof was authored by the same reviewer; the new argument is written in full rather than inferred from its reduced-fibre case.

Root supplied the multiplicity-extension outline, including the weighted support budget and non-unimodular omitted-coordinate factor. Root therefore cannot be the sole fresh independent reviewer of this packet. No previous frozen input is edited.

## 2. Exact statement

Let K be a complete discretely valued field, R its valuation ring, pi a uniformizer, and k its perfect residue field. Put \(v=-\log|\cdot|\) and \(\ell=v(\pi)>0\).

Let \(\mathcal X\) be an integral proper flat regular R-scheme of finite type, of relative dimension \(n\ge2\), whose generic fibre is smooth. Write its special fibre as

\[
                 \mathcal X_k=\sum_{\alpha}N_\alpha E_\alpha,
                 \qquad N_\alpha\in\mathbf Z_{>0},
                                                        \tag{2.1}
\]

where the reduced support has STRICT normal crossings. In particular, at every point the distinct local component equations are part of a regular system of parameters. No reducedness of the special fibre or tameness of its multiplicities is imposed.

Fix distinct VERTICAL components \(E_0,\ldots,E_{n-1}\) and a nonempty connected component C of their scheme-theoretic intersection. Then C is a smooth proper integral k-curve; it need not be geometrically connected. Put \(X=\mathcal X_K^{\rm an}\) and

\[
                   X_C=\operatorname{red}^{-1}(C).
\]

Let T be a positive ordinary CLD current of bidegree (0,0) on the WHOLE ordinary open set \(X_C\), with \(d'T=d''T=0\).

For a closed point p of C, put \(d_p=[\kappa(p):k]\). At most one further vertical component meets C at p. Let \(N_p\) be its multiplicity if it exists, and set \(N_p=0\) otherwise. There are actual parameters in \(\mathcal O_{\mathcal X,p}\), denoted \(x_0,\ldots,x_{n-1},w\), such that each x_i defines E_i and w reduces to a uniformizer of C at p. When \(N_p>0\), w also defines the additional component. The completion has the presentation

\[
 \widehat{\mathcal O}_{\mathcal X,p}\simeq
 R_p[[x_0,\ldots,x_{n-1},w]]/
 \left(\pi-\epsilon_p(x,w)
                   \prod_{i=0}^{n-1}x_i^{N_i}w^{N_p}\right),
                                                        \tag{2.2}
\]

where \(R_p/R\) is finite unramified of degree d_p and epsilon_p is a genuine formal unit. Its constant coefficient has norm one. This presentation is proved in Section 3, not assumed to come from a semistable étale chart.

Remove w=0 from the p-tube when \(N_p=0\); when \(N_p>0\) it is already absent. On this punctured tube define the actual coordinate moment

\[
 g_p=(x_1,\ldots,x_{n-1},w),\qquad q_p=\operatorname{trop}(g_p)=(u,s),
\]
\[
 u_i=v(x_i),\quad s=v(w),\qquad
 Q_p=\left\{u_i>0,\ s>0,\
                 \sum_{i=1}^{n-1}N_i u_i+N_p s<\ell\right\}.
                                                        \tag{2.3}
\]

Here the source, including its coefficient field \(K_p=\operatorname{Frac}(R_p)\), is considered as a K-analytic space. This is not a scalar extension of T.

Assume (L) for these actual completed tubes. There is a finite coefficient \(b_0(p)\ge0\) such that

\[
 \left\langle T,q_p^*(h\Omega_0)\right\rangle
       =b_0(p)\int_{Q_p}h(u,s)\,du\,ds,
 \quad h\in C_c^\infty(Q_p),\qquad
 \Omega_0=
 \left(\bigwedge_{i=1}^{n-1}d'u_i\wedge d''u_i\right)
                       \wedge d's\wedge d''s .
                                                        \tag{2.4}
\]

Omega_0 is a TARGET coordinate form before its indicated pullback. The test pullback has compact analytic support and is extended by zero as a test form to \(X_C\).

With the omitted component E_0 fixed, \(b_0(p)\) is independent of the chosen regular local parameters. The coefficients annihilate every residual principal divisor:

\[
 \sum_{p\in C^{(1)}}\operatorname{ord}_p(f)b_0(p)=0
       \quad (f\in k(C)^\times).
                                                        \tag{2.5}
\]

Consequently one \(c_0\ge0\) satisfies

\[
                         b_0(p)=c_0d_p
                         \quad\hbox{for every closed }p.
                                                        \tag{2.6}
\]

For the canonical integration current, \(b_0(p)=N_0d_p\). If E_j is omitted instead, the corresponding coefficient obeys

\[
 b_j(p)=\frac{N_j}{N_0}b_0(p),\qquad
 c_j=\frac{N_j}{N_0}c_0,\qquad
                \frac{c_j}{N_j}=\frac{c_0}{N_0}.
                                                        \tag{2.7}
\]

Only under (L), Sections 6-7, and (R), the represented coefficient/canonical-calibration ratio on each displayed full-dimensional coordinate-moment source cell is \(c_0/N_0\). This is not an assertion that every ordinary test or every moment is detected by those cells.

“Finite coefficient” means finite at each p and defines a homomorphism on divisors, which have finite support. No finiteness of the sum over all closed points is claimed.

## 3. The completed local equation from regularity

### 3.1 Parameters, multiplicities, and the coefficient ring

The strict-normal-crossing support assumption supplies distinct component parameters. At a closed point of C, the local ring \(A_p=\mathcal O_{\mathcal X,p}\) is regular of dimension n+1. The equations \(x_0,\ldots,x_{n-1}\) extend to a regular system of parameters by one w. If an additional component is present, use its equation as w; there cannot be two additional components. If none is present, choose w mapping to a uniformizer of the regular one-dimensional local ring of C.

The quotient by \((x_0,\ldots,x_{n-1})\) is regular of dimension one and is a k-algebra. The relevant intersection is therefore regular. Since k is perfect, its finite-type regular curves are smooth. Regular connected components are integral and disjoint; properness follows from properness of the original model.

Every component E_alpha is Cartier because the model is regular. Equality of Cartier divisors in (2.1) implies, in \(A_p\),

\[
              \pi=e_p\prod_{i=0}^{n-1}x_i^{N_i}w^{N_p}
                        \quad\hbox{with }e_p\in A_p^\times.
                                                        \tag{3.1}
\]

There is no unspecified horizontal factor in this equality: it is equality of the full divisor of pi in the regular local ring.

As k is perfect, \(\kappa(p)/k\) is finite separable. The henselian finite-étale lifting equivalence gives the unramified DVR \(R_p/R\) with this residue extension. The identity on the residue field lifts to an R-map \(R_p\to\widehat A_p\): one can lift a separable residue generator and use Hensel's simple-root property in the complete local ring. The map is injective since pi remains nonzero in the regular completed domain. Its residue map is the specified identification with \(\kappa(p)\).

### 3.2 Surjection and the linear pi term

Let
\[
                     B=R_p[[X_0,\ldots,X_{n-1},W]].
\]
Sending the variables to the actual regular parameters gives a continuous surjection \(B\to\widehat A_p\). For completeness, surjectivity follows by successive approximation in the maximal ideal: the parameter monomials generate each graded piece, coefficients in the residue field lift to \(R_p\), and completeness makes the successive sums converge. This does not require a coefficient FIELD inside a mixed-characteristic ring.

Lift \(e_p\in\widehat A_p^\times\) to a unit \(\epsilon_p\in B^\times\). Its constant coefficient is a unit of \(R_p\). The kernel contains
\[
                 F=\pi-\epsilon_p\prod X_i^{N_i}W^{N_p}.
\]
Since \(\sum_iN_i\ge n\ge2\), the monomial term lies in the square of the maximal ideal of B. Thus the image of F modulo that square is the nonzero class of pi. In particular F is part of a regular system of parameters of B.

The ring B is regular local of dimension n+2. Therefore \(B/(F)\) is regular local of dimension n+1. The induced surjection to \(\widehat A_p\), also regular local of dimension n+1, is an isomorphism: a nonzero kernel in the regular domain \(B/(F)\) would lower dimension. This proves (2.2).

All coefficients of epsilon_p lie in \(R_p\) and are bounded by one, with unit constant coefficient. On the open unit polydisc its nonconstant part has norm less than one, so \(|\epsilon_p|=1\). No root of epsilon_p, pi, or a coordinate has been extracted, even when a multiplicity is divisible by the residue characteristic.

### 3.3 Actual tubes and applicability of (L)

The tube of p is the generic fibre of the completion at p. This is the special-formal-scheme generic-fibre construction and Proposition 1.3 of Berkovich, Vanishing cycles for formal schemes II, Section 1, pp.370-372; its standing field is complete discretely valued, with no semistability assumption. The presentation just proved identifies the tube with the actual analytic equation (2.2), with all displayed parameters of norm less than one. Every formal series converges uniformly on smaller closed polydiscs, and the completed-ring isomorphism induces compatible analytic maps on the resulting exhaustion. Regular functions with denominators nonzero at p remain invertible there. This is an analytic identification of the whole tube, not merely its Gauss points.

It is one \(K_p\)-analytic domain viewed over K, not \(d_p\) ordinary-open sheets. The selected x_i never vanish on the generic fibre by (3.1). After the indicated removal of w=0, (L) applies with
\[
 m=N_0,\quad (a_1,\ldots,a_n)=(N_1,\ldots,N_{n-1},N_p).
\]
It gives finite flat degree N_0 for g_p, surjectivity onto the domain with tropical image Q_p, and topological properness of q_p. The restricted current is the current originally given over K on this ordinary open tube. No current base change occurs.

## 4. Global radii and compact normal strips

Let \(U_\alpha\) be the continuous model function associated with the vertical Cartier divisor E_alpha, normalized locally by \(U_\alpha=v(a_\alpha)\) for a formal component equation. Equations differ by a formal unit of norm one. Equivalently, use the formal metric on \(\mathcal O(E_\alpha)\) and its nowhere-vanishing generic section 1; then \(U_\alpha=-\log\|1\|\). These are finite, nonnegative continuous functions, not assumed to be ordinary smooth functions.

Equality (2.1) gives
\[
                      \sum_\alpha N_\alpha U_\alpha=\ell.
                                                        \tag{4.1}
\]
The tube of the whole intersection \(D=E_0\cap\cdots\cap E_{n-1}\) is \(\{U_i>0\ \text{for all selected }i\}\). The tubes of C and of the finite union D minus C are ordinary open and partition this tube; thus \(X_C\) is clopen in it.

For any \(a>0\),
\[
 K_a=\{\xi\in X_C:U_i(\xi)\ge a\ (0\le i<n)\}
                                                        \tag{4.2}
\]
is compact inside \(X_C\). Indeed the same inequalities define a closed subset of the compact space X, entirely inside the tube of D; restricting to its clopen C-piece preserves compactness. This argument uses the whole proper model and the WHOLE tube \(X_C\).

At a point p with parameters as above, \(|\epsilon_p|=1\) gives the exact weighted relation
\[
              N_0U_0+\sum_{i=1}^{n-1}N_i u_i+N_p s=\ell
                                                        \tag{4.3}
\]
on the punctured tube. At a point reducing to C away from extra-component intersections, all other component radii are zero.

## 5. Local coefficients and parameter independence

By (L), every compact target test in (2.4), including a primitive with one d' factor omitted, has compact actual inverse-image support. Thus the positive scalar distribution obtained from T has every distributional first partial derivative zero. Convolution on relatively compact balls and connectedness of the convex Q_p give the finite nonnegative constant \(b_0(p)\). This also explains the current part of the conditional local input without identifying an unknown coefficient with canonical multiplicity.

Replacing a selected component equation x_i by another equation multiplies it by a local unit. Its norm is one on the tube, so each U_i is unchanged. The same holds for w when \(N_p>0\).

When \(N_p=0\), a second choice of curve parameter has, after completion,
\[
                 w'=wV(w)+\sum_{i=0}^{n-1}x_iB_i,
                                                        \tag{5.1}
\]
where V has unit constant coefficient and all coefficients are bounded. This follows by reducing modulo the ideal of C; its reduction is another uniformizer of \(\kappa(p)[[w]]\).

Choose \(\rho>0\) small enough that \(2\rho\sum_{i=0}^{n-1}N_i<\ell\); the normal slice with all selected \(U_i>\rho\) is then nonempty. On that slice and \(0<s<\delta<\rho\), the w-term strictly dominates, so \(v(w')=s\) on the whole ordinary source collar. Conversely, if \(v(w')<\delta\) and all \(U_i>\rho\), (5.1) forces \(|w|=|w'|\): a value \(|w|\le\exp(-\delta)\) would make both terms too small. Hence a sufficiently small compact target test inside this nonempty common collar has identical pullback and identical support in both coordinate systems. The finite coefficients agree.

The choice of OMITTED component is different and is not covered by a determinant-one assertion. It is addressed explicitly in Section 11.

## 6. Rational lifts and the finite residual bad set

Let \(A=\mathcal O_{\mathcal X,\eta_C}\). Its residue field is k(C). For each \(i=1,\ldots,n-1\), choose a rational function z_i GENERATING the Cartier ideal of E_i at \(\eta_C\). Then \(z_i/x_i\in A^\times\) for every local equation x_i near a closed point of C. Merely specifying its orders at the selected vertical components is insufficient.

Given \(f\in k(C)^\times\), choose an ACTUAL unit \(F\in A^\times\) reducing to f. Put
\[
 m_p=\operatorname{ord}_p(f),\qquad
 n_{i,p}=\operatorname{ord}_p(\overline{z_i/x_i}).
                                                        \tag{6.1}
\]
Changing x_i by a local unit does not change this latter order. The integers n_{i,p} arise from a rational trivialization of a line bundle and are not assumed to sum to a degree-zero divisor.

Let B_f be the union of the intersections with C of the supports of \({\rm div}(F)\), of \({\rm div}(z_i)-E_i\), and of all additional vertical components. These supports do not contain \(\eta_C\); their intersections with the proper integral curve are finite. The set B_f retains bad points with \(m_p=0\).

At points outside the tubes of B_f, the relevant ratios and F are formal units. Therefore, pointwise there,
\[
                         v(z_i)=U_i,\qquad v(F)=0.
                                                        \tag{6.2}
\]
This is not a claim that the complement of the bad tubes is an ordinary-open formal chart or that every such point has an ordinary neighbourhood of constancy.

## 7. Exact dominance before the radial inference

Fix \(\rho>0\), and work FIRST on
\[
 W_\rho=\{\xi\in X_C:U_i(\xi)>\rho\ (0\le i<n)\}.
                                                        \tag{7.1}
\]
For \(p\in B_f\), put \(I=(x_0,\ldots,x_{n-1})\) in the completed local ring. Equation (2.2) gives \(\widehat A_p/I=\kappa(p)[[w]]\), regardless of the multiplicities.

Every relevant element of \(A^\times\) is represented at p by a quotient a/b with \(a,b\in A_p\) not in the prime ideal of C. Each completed numerator or denominator thus has nonzero reduction modulo I. For a numerator write
\[
                    a=w^rV(w)+\sum_{i=0}^{n-1}x_iA_i,
                                                        \tag{7.2}
\]
where \(r\ge0\), V has unit constant coefficient, and the formal coefficients are bounded. This is obtained by lifting the nonzero reduction and subtracting it; the remainder belongs to I.

On \(W_\rho\), the remainder has norm at most \(\exp(-\rho)\). The first term has norm \(\exp(-rs)\). If \(r\delta_p<\rho\), it strictly dominates for \(0<s<\delta_p\). Apply this to the finitely many numerators and denominators at all bad points. For suitable \(\delta_p>0\) it proves the EXACT identities
\[
 r_i:=v(z_i)=U_i+n_{i,p}s,\qquad
 t:=v(F)=m_ps
       \quad\text{on }W_\rho\cap\operatorname{red}^{-1}(p)
                       \cap\{0<s<\delta_p\}.
                                                        \tag{7.3}
\]
All relevant functions are analytic units on these collars. No deformation term is discarded as an approximation.

Combining with (4.3) gives
\[
 N_0U_0=\ell-\sum_{i=1}^{n-1}N_i r_i+
                \left(\sum_{i=1}^{n-1}N_i n_{i,p}-N_p\right)s.
                                                        \tag{7.4}
\]
Both the extra multiplicity N_p and the weights N_i are essential in this equality.

## 8. Smooth source cutoffs, including w=0, and compact support

Choose \(\rho>0\) sufficiently small that
\[
 \Delta_{4\rho}=
 \{r_i>4\rho,\quad
             \ell-\sum_{i=1}^{n-1}N_i r_i>4N_0\rho\}
                                                        \tag{8.1}
\]
is nonempty; it suffices that \(4\rho\sum_{i=0}^{n-1}N_i<\ell\).
Choose a nonnegative \(\phi\in C_c^\infty(\Delta_{4\rho})\) with integral one with respect to \(dr_1\cdots dr_{n-1}\).

For each bad p choose \(0<a_p<b_p<\delta_p\) such that
\[
 |n_{i,p}|b_p<\rho,\qquad
 \left|\sum_{i=1}^{n-1}N_i n_{i,p}-N_p\right|b_p<N_0\rho.
                                                        \tag{8.2}
\]
A zero coefficient imposes no condition. Choose a smooth cutoff eta_p(s) between zero and one, equal to one for \(s\le a_p\), and zero for \(s\ge b_p\). When \(N_p=0\), extend eta_p by zero at w=0.

On \(W_\rho\), define eta to be eta_p in the bad p-tube and one elsewhere. This gluing is ordinary smooth, for the following actual source-support reason.

The support of \(1-\eta_p\), relative to \(W_\rho\), lies in
\[
 \{U_i\ge\rho\ (0\le i<n),\quad |w|\le\exp(-a_p)\}.
                                                        \tag{8.3}
\]
In the presentation (2.2), this set is the zero locus of the actual analytic equation in the closed polydisc
\[
 |x_i|\le\exp(-\rho)\ (0\le i<n),\qquad
                         |w|\le\exp(-a_p).
\]
All radii are strictly less than one, so the formal equation converges there and this zero locus is compact. Its points lie inside the p-tube; the equation forces each x_i to be nonzero. When \(N_p>0\) it also forces w to be nonzero. When \(N_p=0\), w=0 is allowed and is deliberately INCLUDED in this compact-polydisc argument. Thus this step does not apply the punctured finite-projection premise outside its domain.

The support closure of \(1-\eta_p\) cannot reach the boundary of the p-tube within \(W_\rho\). It therefore extends smoothly by zero across that complement. The bad p-tubes are disjoint and finite in number, so \(\eta=1-\sum_p(1-\eta_p)\) is smooth. No formal Zariski cover has been declared an ordinary open cover.

Let V be the ordinary open locus in \(W_\rho\) where all z_i and F are analytic units. Equations (6.2) and (7.3) show that every zero or pole excluded from V lies where eta is zero on a neighbourhood. In particular, inside a bad tube none occurs on \(0<s<\delta_p\); the remaining region has \(s\ge\delta_p>b_p\), or w=0. The selected vertical x_i have no zeros on the generic fibre.

If eta is nonzero and \(r\in\operatorname{supp}\phi\), either (6.2) or the collar identities give
\[
 U_i=r_i-n_{i,p}s>3\rho\quad(i\ge1),
\]
\[
 N_0U_0=\ell-\sum_{i=1}^{n-1}N_i r_i+
                  \left(\sum_{i=1}^{n-1}N_i n_{i,p}-N_p\right)s
                                            >3N_0\rho.
                                                        \tag{8.4}
\]
Outside the bad tubes the s-terms are absent. These implications use (7.3) only on \(W_\rho\), where it was proved first; they are not circular.

Consequently a form with scalar factor \(\eta\phi(r)\), once extended across the removed divisor as zero, has support in the compact \(K_{3\rho}\). This compact lies strictly inside \(W_\rho\). All global U_i have been used only as continuous support bounds, never differentiated.

## 9. The compact principal-divisor primitive

If all m_p vanish, (2.5) is immediate. Otherwise choose
\[
             0<h<\min_{p\in B_f,\ m_p\ne0}|m_p|a_p
\]
and \(\chi\in C_c^\infty((-h,h))\) equal to one near zero. On V put
\[
 \Omega_r=\bigwedge_{i=1}^{n-1}d'r_i\wedge d''r_i,\qquad
 \beta=\phi(r)\chi(t)\Omega_r\wedge d''t.
                                                        \tag{9.1}
\]
The form \(\eta\beta\) extends by zero to a compact ordinary smooth form of bidegree (n-1,n) on \(X_C\). Near the removed divisor eta is identically zero. At the boundary of \(W_\rho\), compact support in \(K_{3\rho}\) supplies an actual neighbourhood where the extension is zero. This is extension of a compact TEST FORM, not an extension-commutation assertion about currents.

On each transition collar of eta_p, if \(m_p\ne0\), then \(|t|\ge |m_p|a_p>h\), so \(\chi(t)=0\). If \(m_p=0\), then t is identically zero on the whole ordinary collar by (7.3), and \(d''t=0\) there. Therefore
\[
                             d'\eta\wedge\beta=0.
                                                        \tag{9.2}
\]
This retains every bad zero-order branch, regardless of n_{i,p} or N_p.

On V the functions r_i,t are actual logarithms of analytic units, so \(d'd''r_i=d'd''t=0\). Differentiating only there gives
\[
 d'\beta=\phi(r)\chi'(t)\Omega_r\wedge d't\wedge d''t.
                                                        \tag{9.3}
\]
The derivatives of phi repeat a d'r_i and vanish; the degree of Omega_r is even. Thus there is no additional exterior sign.

The source support of \(d'(\eta\beta)\) is a finite union of compact pieces in the bad punctured p-tubes with \(m_p\ne0\). Indeed t=0 pointwise off those tubes, and continuity makes \(\chi'(t)\) zero on an ordinary neighbourhood of every such point. On a bad tube, its nonzero part satisfies
\[
               0<s<h/|m_p|<a_p,
\]
so eta=1 there; since chi' vanishes near zero, s is also bounded away from zero. The normal-radius bounds (8.4) and properness from (L) make each piece compact inside its actual punctured tube. No current has been sliced along C or along a tangential fibre.

## 10. The determinant-one shear and divisor identity

Put \(n_p=(n_{1,p},\ldots,n_{n-1,p})\). On the p-collar, the ACTUAL coordinate functions satisfy
\[
                 (u,s)\longmapsto(r,s)=(u+n_ps,s),
                 \qquad t=m_ps.
                                                        \tag{10.1}
\]
For the fixed omitted component E_0, this shear has determinant one. The weighted relation only changes its domain, not this Jacobian. Equation (9.3) becomes
\[
         m_p^2\,\phi(u+n_ps)\chi'(m_ps)\,\Omega_0.
                                                        \tag{10.2}
\]
The two differential blocks produce \(m_p^2\); all mixed terms repeating d's or d''s vanish.

Whenever \(\chi'(m_ps)\ne0\), (8.2) and the support of phi place every translated u in the actual slice
\[
                    \sum_{i=1}^{n-1}N_i u_i+N_ps<\ell
\]
and give all selected \(U_i>3\rho\). Hence no translated support is lost at a face of Q_p and
\[
                        \int\phi(u+n_ps)\,du=1.
                                                        \tag{10.3}
\]

Use closedness on the original n-dimensional source and (2.4):
\[
 \begin{aligned}
 0&=\langle T,d'(\eta\beta)\rangle\\
  &=\sum_{p\in B_f,\ m_p\ne0}b_0(p)
       \int_0^{\delta_p}m_p^2\chi'(m_ps)
                    \left(\int\phi(u+n_ps)\,du\right)\,ds\\
  &=-\sum_p m_pb_0(p).
 \end{aligned}                                             \tag{10.4}
\]
For either sign of the nonzero integer m_p,
\[
 \int_0^{\delta_p}m_p^2\chi'(m_ps)\,ds
     =m_p\bigl(\chi(m_p\delta_p)-\chi(0)\bigr)=-m_p .
\]
The current derivative is used only through its vanishing; no disputed zero-extension/differentiation commutation is invoked. This proves (2.5).

The positive finite-valued homomorphism
\(\lambda(\sum a_pp)=\sum a_pb_0(p)\) now annihilates principal divisors. For a divisor D of degree zero, choose an effective H with \(\deg_k H+\chi_k(\mathcal O_C)>0\). Riemann--Roch gives a nonzero section of \(\mathcal O_C(H+jD)\) for every integer j, so an effective divisor is linearly equivalent to H+jD. Thus
\[
                         0\le\lambda(H)+j\lambda(D)
                         \quad\hbox{for all }j\in\mathbf Z.
\]
It follows that \(\lambda(D)=0\). Apply this to \(d_qp-d_pq\) to obtain (2.6). Degrees and Euler characteristics are taken over k; geometric connectedness is unnecessary.

By the canonical part of (L), the actual degree N_0 projection over K_p has canonical target coefficient N_0, and viewing the same source over K multiplies by \(d_p\). Therefore \(b_0(p)=N_0d_p\) for the canonical current. The unknown coefficient is not equated to that degree; its normalized ratio is \(c_0/N_0\).

## 11. Changing the omitted component is NOT unimodular

Fix a p and compare the two actual coordinate moments obtained by omitting E_0 and E_j, \(1\le j<n\), keeping w. List their remaining normal coordinates in increasing index order and append s. Equation (4.3), valid as an equality of ordinary logarithmic functions on the entire punctured tube, gives the affine relation \(q_j=A_jq_0+a_j\), with
\[
                             |\det A_j|=\frac{N_j}{N_0}.
                                                        \tag{11.1}
\]
The unit epsilon_p has norm one and makes no additional logarithmic term. This is a rational-affine change of the chosen target coordinates, not a claim that both are primitive lattice bases.

For a compact test in Q_j the equality of actual source functions gives equality of their ordinary form pullbacks. In top bidegree the pullback factor is \((\det A_j)^2\), whereas the change of Lebesgue variables has factor \(|\det A_j|\). Applying (2.4) therefore gives
\[
                            b_j(p)=|\det A_j|b_0(p)
                                  =\frac{N_j}{N_0}b_0(p).
\]
The domains are carried onto one another by the same affine relation, so the compact test comparison has no source-support loss. This proves (2.7) and agrees with canonical coefficient \(N_jd_p\).

For example, if \(N_0=2\) and \(N_j=3\), the target volume-coordinate Jacobian is \(3/2\), the top-form factor is \(9/4\), and the resulting coefficient factor is \(3/2\), not one. All of these are coordinate/degree checks, not an extra assumption that the corresponding global proper model has been constructed.

## 12. Conditional source interpretation and remaining interfaces

Only now assume (R) for the local moments g_p and (L), Sections 6-7. The original field is a DVR field and \(K_p/K\) is unramified, so (L)'s generic-Gauss single-source-point assertion has exactly its stated hypotheses. Its comparison then identifies each represented coordinate-moment top-cell coefficient with the aggregate \(b_0(p)\), and its canonical coordinate coefficient with \(N_0d_p\). Their ratio is \(c_0/N_0\), independent of p and of the omitted component.

This application does not pull T to a residue field, a tangential fibre, an alteration, or a ramified scalar extension. Finite degree alone is not used to identify individual source coefficients; the extra source-point and representation inputs are explicit.

The following remain outside the result:

- T is assumed on the WHOLE \(X_C\). No assertion says an arbitrary ordinary open set W containing one wall point contains the compact normal strips, all bad tubes, or the primitive constructed here.
- No proof realizes every wall or every full-rank cell of an arbitrary analytic moment in such an original-field proper model.
- No proof supplies a genuine common-moment/source-isolation bridge for every comparison with a different analytic moment.
- All selected E_i are VERTICAL with positive N_i. For an SNC pair with selected horizontal components, some N_i would be zero and the corresponding model radii could take infinite values on the generic fibre. The finite-radius compactness and eta-alone divisor argument above would require a separate checked extension with appropriate upper radial cutoffs. Zero exponents allowed by the LOCAL premise do not settle that GLOBAL support issue.
- No global scalar rigidity, all-current representation theorem, or full P21.3 conclusion is claimed.

The new gain is precisely the conditional residual divisor-functional identity on the whole proper modelled curve tube with arbitrary positive vertical multiplicities, including genuine deformation units. Fresh independent review must cover this entire global argument; the local premise's separate audit is not an audit of this extension.
