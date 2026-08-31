# Residual divisor tests in an actual strictly semistable wall neighborhood

Date: 2026-08-31. Author: /root/p213_skeletal_hostile.
Status: new bounded research proof, frozen only after the companion manifest is written. Independent mathematical review and any production verification remain separate and pending.

## 1. Scope and the remaining P21.3 question

The result below concerns the tube of a proper residual curve in an ACTUAL regular strictly semistable model over a complete DVR. The formal neighborhood need not be a product, need not be an annular line-bundle torsor over a lifted curve, and need not admit a global analytic normal coordinate.

The geometric/current result constructs a finite-valued positive divisor functional by explicit compact tests in that neighborhood, in every dimension n>=2. It does not assume the source-calibration representation (R). Only its interpretation as a ratio of represented source-cell coefficients uses (R).

This is not a theorem about every wall of an arbitrary analytic tropical moment. In particular, no construction of such a model around an arbitrary analytic wall, descent through an alteration, slicing of an unknown current, or universal common-source-cell comparison is supplied. Full P21.3 remains open here.

The preceding product and annular-torsor proofs are the author's earlier work, independently audited elsewhere. They motivated this extension but are not used as black boxes: the new completed-ring, deformation, support, and current arguments are given below. Root identified the need to choose actual Cartier-ideal generators rather than merely prescribe component orders, and to distinguish a connected component of an intersection from the entire intersection. Both corrections are built into the argument.

## 2. Statement

Let K be complete discretely valued, R its valuation ring, pi a uniformizer, k a perfect residue field, v=-log|.|, and ell=v(pi)>0.

Let 𝒳 be an integral proper regular strictly semistable R-scheme of relative dimension n>=2. Thus the special fibre is reduced with strict normal crossings, and locally there are étale charts over

  Spec R[x_0,...,x_n]/(x_0...x_r-pi).

Let E_0,...,E_{n-1} be distinct special-fibre components whose intersection has a nonempty connected component C. Strict normal crossings imply that C is a smooth proper integral k-curve. Geometric connectedness over k is NOT required. Fix this component C, not the entire possibly disconnected intersection.

Write X=𝒳_K^an, red:X->𝒳_k for reduction, and

  X_C=red^{-1}(C).

This is an ordinary open, good, boundaryless analytic space, as justified below. Let T be a positive ordinary CLD current of bidegree (0,0) on X_C with d'T=d''T=0.

For a closed point p of C, set d_p=[κ(p):k]. Let e_p=1 if an additional special-fibre component meets C at p, and e_p=0 otherwise. There is at most one additional component at p. Completed étale coordinates give one actual K_p-analytic domain, viewed over K, with K_p/K unramified of degree d_p and completed local ring

\[
 R_p[[x_0,\ldots,x_{n-1},w]]/
     (x_0\cdots x_{n-1}w^{e_p}-\pi).                 \tag{2.1}
\]

Here every x_i cuts out E_i, and w reduces to a local parameter of C at p; when e_p=1 it also cuts out the additional component. Put

\[
 u=(u_1,\ldots,u_{n-1}),\quad u_i=v(x_i),\quad s=v(w),
\]
\[
 Q_p=\{u_i>0,\ s>0,\ \sum_{i=1}^{n-1}u_i+e_ps<\ell\}.
                                                               \tag{2.2}
\]

If e_p=0 the condition on s is just s>0. On the punctured p-tube let q_p=(u,s), and set

\[
 \Omega_q=\left(\bigwedge_{i=1}^{n-1}
                 \mathrm d'u_i\wedge\mathrm d''u_i\right)
                 \wedge\mathrm d's\wedge\mathrm d''s .
\]

Then there is a finite number b_T(p)>=0 such that

\[
 \langle T,q_p^*(h\Omega_q)\rangle
    =b_T(p)\int_{Q_p}h(u,s)\,\mathrm du\,\mathrm ds,
 \qquad h\in C_c^\infty(Q_p).                         \tag{2.3}
\]

The pullback has compact analytic support and is extended by zero. The number is independent of the completed étale coordinates and of restricting to sufficiently outer collars with the normal radii bounded away from zero.

These coefficients satisfy

\[
 \sum_{p\in C^{(1)}}\operatorname{ord}_p(f)b_T(p)=0
       \quad\text{for every }f\in k(C)^\times.         \tag{2.4}
\]

Consequently there is one c>=0 such that

\[
                    b_T(p)=c\,d_p
                    \quad\text{for every closed }p.  \tag{2.5}
\]

For the canonical current b_{\delta_{X_C}}(p)=d_p. Under the separate representation premise (R), the ratio on each displayed source Gauss n-cell is therefore c. In particular, this controls the canonical n-cells adjacent to the wall C, which arise at points with e_p=1. An arbitrary analytic moment's coefficient can be compared only when an appropriate actual common-moment/source-isolation interface is additionally available; that interface is not automatic in this statement.

“Finite-valued” in (2.4) means a homomorphism on the divisor group, whose elements have finite support. It does not mean that the sum of all b_T(p) is finite.

## 3. Geometry, coefficient fields, and compact strips

### 3.1 Ordinary openness, selected component, and continuous radii

A tube of a closed special-fibre subset is ordinary open. In a formal affine chart this follows from strict inequalities |g_j|<1 for a finite set of generators of its defining ideal. Thus X_C is ordinary open in the analytification of the smooth proper generic fibre. Goodness and absence of analytic boundary pass to this ordinary open.

For each special-fibre component E_j, its effective vertical Cartier divisor defines a continuous nonnegative model function U_j on X. Locally U_j=v(a_j) for a formal local equation a_j of E_j; different equations differ by a formal unit of norm one. This uses the continuous formal metric, not an assertion that U_j is an ordinary smooth function. Since the special fibre is reduced,

\[
                    \sum_j U_j=\ell.                 \tag{3.1}
\]

The tube of D=E_0∩...∩E_{n-1} is {U_i>0 for 0<=i<n}. The smooth proper intersection D is a finite disjoint union of its connected components. The tubes of C and of D\C are ordinary open and partition that tube. They are therefore clopen relative to it.

For a>0, define

\[
 K_a=\{\xi\in X_C: U_i(\xi)\ge a\ (0\le i<n)\}.        \tag{3.2}
\]

The same inequalities define a closed subset of compact X, contained in the tube of D. Restricting this compact set to the clopen component tube X_C gives a compact K_a. In particular K_a is compact INSIDE X_C. This avoids falsely identifying X_C with the full positive-radius locus when D is disconnected.

### 3.2 Actual completed p-tubes

Because k is perfect, κ(p)/k is finite separable. Henselian finite-étale lifting gives the finite unramified DVR R_p/R with that residue field and degree d_p. Its residue-compatible map into the completed local ring at p is obtained by lifting a separable residue generator; uniqueness follows from Hensel's simple-root argument.

After this coefficient extension, the strictly semistable étale chart induces the presentation (2.1). Choose the normal equations x_i as the actual pullbacks of coordinates in an algebraic étale chart; they belong to O_{𝒳,p} before completion. One can check the presentation by completing the standard chart at the relevant residue point: an étale local map with identical residue fields induces isomorphisms of its infinitesimal neighborhoods, hence of completed local rings. At e_p=0 only the remaining smooth curve parameter needs to be centered by subtracting its residue lift in R_p. At e_p=1 all n+1 components already supply the parameters. The relation has coefficient pi, as in the chosen strictly semistable chart.

The generic tube is the domain with every displayed parameter of norm less than one. Formal power series converge there, uniformly on every smaller closed polydisc. Conversely the inverses furnished by the completed-ring isomorphism converge on those smaller domains. These domains exhaust the tube, giving an actual analytic isomorphism, not merely a bijection on the skeleton or a list of classical points.

After removing w=0 in the e_p=0 case, the relation eliminates x_0, and the resulting domain is exactly the polyannulus described by (2.2), over K_p. When e_p=1, w is automatically nonzero. It is one K_p-domain viewed as K-analytic, not d_p ordinary-open sheets. No current is pulled back along a field extension.

Every compact subset of Q_p has compact inverse image, being contained in a closed polyannulus in these actual coordinates. This is the precise properness needed for the test forms and all their primitives.

## 4. The coefficients and coordinate independence

Pairing T with q_p^*(hΩ_q) defines a positive scalar distribution on Q_p. A nonnegative compact cutoff equal to one near a prescribed target compact set bounds that distribution by the sup norm there. It is therefore a locally finite positive Radon measure.

Delete one d' coordinate factor from Ω_q, with the appropriate exterior-algebra sign, and use an arbitrary compactly supported coefficient h. Its pullback is a compact (n-1,n)-test by the properness just proved. Closedness gives zero for each coordinate derivative of the scalar distribution. On a relatively compact target ball, convolution is constant; testing against an integral-one function fixes a finite limiting constant. Overlapping balls, and connectedness of the convex Q_p, give (2.3) with one finite b_T(p)>=0. This argument does not use (R).

Changing the formal equation x_i for the same Cartier component multiplies it by a completed local unit. Such a unit has unit constant term and bounded higher coefficients, so its norm is one on the entire tube. Thus its logarithmic radius U_i is unchanged as an actual function.

If e_p=0, a different curve parameter has the form

\[
 w'=a_1w+w^2 A+\sum_{i=0}^{n-1}x_i B_i,\qquad
       a_1\in R_p^\times,                              \tag{4.1}
\]

with bounded formal coefficients, after incorporating higher w terms in A; the coefficient of w may itself be a formal unit, with the same conclusion. On U_i>epsilon and 0<s<delta<epsilon the w-term strictly dominates, so |w'|=|w|. If e_p=1 both parameters cut the extra Cartier component and differ by a formal unit, giving the same equality directly.

The nonempty common outer collar lies in both actual coordinate domains, so its ordinary top forms coincide. Equality of the scalar coefficients follows by an integral-one test there. The choice of omitted normal coordinate x_0 is harmless: replacing it by any other omitted x_j uses

\[
 U_0=\ell-\sum_{i=1}^{n-1}u_i-e_ps,
\]

an integral affine coordinate change of absolute determinant one on (u,s). The corresponding (n,n)-volume and Lebesgue normalization are unchanged. This establishes the asserted independence.

## 5. Generic-point generators, not mere component orders

Let A=O_{𝒳,η_C}, whose residue field is k(C). For i=1,...,n-1 choose

\[
       z_i\in K(\mathcal X)^\times
\]

to GENERATE the principal Cartier ideal O(-E_i) at η_C. In particular, if x_i is any local equation for E_i near p, then z_i/x_i belongs to A^\times. Merely prescribing ord_{E_j}(z_i)=δ_{ij} would not imply this unit condition.

Indeed multiplying a valid generator x_i by x_i+x_j (i!=j) preserves these component orders but introduces a horizontal factor through C. Its reduction after division by x_i is zero at η_C, and the following leading-curve-term argument would fail. The stronger generator choice is essential.

Given f∈k(C)^\times, lift it to an ACTUAL unit F∈A^\times. Thus both F and each z_i/x_i have nonzero reductions in k(C). The reduction of F is f. At a closed point p write

\[
 m_p=\operatorname{ord}_p(f),\qquad
 n_{i,p}=\operatorname{ord}_p\left(\overline{z_i/x_i}\right).
                                                               \tag{5.1}
\]

The latter integer is unaffected by replacing x_i by another local equation, because the resulting factor restricts to a unit at p. It is an order in a rational trivialization of a line bundle; the divisor with coefficients n_{i,p} need not have degree zero.

Let B be the union of:

- the intersections with C of the support of div(F);
- the intersections with C of the support of div(z_i)-E_i, for every chosen i;
- all points where an additional vertical component meets C.

This is finite. Each displayed residual support is closed and does not contain η_C by the unit/generator choices, so its intersection with the proper curve is zero-dimensional. Points with m_p=0, even with all n_{i,p}=0, remain in B if they occur in this list.

Outside the tubes of B, the ratios z_i/x_i and F are formal units in suitable formal local neighborhoods. Thus there, pointwise,

\[
                    v(z_i)=U_i,\qquad v(F)=0.         \tag{5.2}
\]

This is not an assertion of ordinary-open constancy at every point reducing to η_C.

## 6. Uniform domination of genuine deformation terms

Fix epsilon>0 and work FIRST on the ordinary open set

\[
 W_\epsilon=\{\xi\in X_C: U_i(\xi)>\epsilon\
                             \text{for all }0\le i<n\}.         \tag{6.1}
\]

This step precedes any attempt to infer normal-radius bounds from rational-coordinate bounds.

For p∈B, let I=(x_0,...,x_{n-1}) in its completed local ring. The quotient by I is κ(p)[[w]]. Any element of A^\times, viewed at p, can be written a/b with a,b∈O_{𝒳,p} and a,b not in the prime ideal of C. Its completed numerator and denominator consequently have nonzero reductions in κ(p)[[w]].

For such a numerator a, write

\[
             a=w^r V(w)+\sum_{i=0}^{n-1}x_i A_i,       \tag{6.2}
\]

where r>=0, V(w) has unit constant term, and all formal coefficients are bounded. This follows by lifting its nonzero reduction and subtracting it; the remainder lies in I. On W_epsilon the norm of the remainder is at most exp(-epsilon). The first term has norm exp(-rs). Hence if r delta<epsilon, it strictly dominates throughout 0<s<delta. The case r=0 requires no extra restriction. The same argument applies to every denominator.

There are finitely many functions and bad points. Shrinking each delta_p therefore gives the EXACT identities on the entire ordinary source collar in W_epsilon,

\[
 r_i:=v(z_i)=U_i+n_{i,p}s,\qquad
 t:=v(F)=m_ps,\qquad 0<s<\delta_p.                     \tag{6.3}
\]

No deformation is neglected approximately; its terms are strictly smaller in the non-archimedean norm. The identities also show that all relevant numerators and denominators are nonzero on these collars.

For e_p=1 the formal relation gives

\[
               U_0+\sum_{i=1}^{n-1}U_i+s=\ell;         \tag{6.4}
\]

for e_p=0 it gives the same relation without s. This extra s is part of the ensuing support estimate. Ignoring it would use the wrong normal simplex at an adjacent top cell.

The argument does not identify the whole neighborhood with its normal cone. It uses only actual completed p-tubes and the uniform lower bound on every selected normal radius.

## 7. Ordinary source cutoffs and the radial support estimate

Choose epsilon>0 small enough that

\[
 \Delta_{4\epsilon}
 =\{r_i>4\epsilon,\ \ell-\sum r_i>4\epsilon\}
\]

is nonempty. Choose a nonnegative smooth compactly supported phi on this simplex, with integral one over R^{n-1}. For each p∈B choose

\[
 0<a_p<b_p<\delta_p
\]

so small that

\[
 |n_{i,p}|b_p<\epsilon\quad(1\le i<n),\qquad
 \left|\sum_{i=1}^{n-1}n_{i,p}-e_p\right|b_p<\epsilon.
                                                               \tag{7.1}
\]

An inequality with zero coefficient imposes no restriction.

On the p-tube intersected with W_epsilon, choose eta_p(s) between zero and one, equal to one for s<=a_p and zero for s>=b_p. In the e_p=0 case its value at w=0 is zero. Define eta to equal eta_p on each such bad tube and one elsewhere in W_epsilon.

This is an ordinary smooth function. Here is the support check missing from a formal-open-cover argument. The function 1-eta_p is smooth on the p-tube, including the w=0 center where it is constant. Inside W_epsilon its support lies in

  {U_i>=epsilon for all selected i, |w|<=exp(-a_p)}.

In the actual completed coordinates this is a compact subset of the p-tube: for e_p=0 it is a closed normal polyannulus times a closed disc; for e_p=1 relation (6.4) bounds every coordinate both away from zero and away from radius one. Thus its support closure stays inside the p-tube even at a prospective ordinary boundary point within W_epsilon. Its extension by zero across that tube's complement is smooth. The finitely many p-tubes are disjoint, giving eta=1-sum_p(1-eta_p). No formal Zariski cover is declared an ordinary open cover.

The exact collar identities place every zero and pole of z_i or F in W_epsilon inside a region where eta vanishes on a neighborhood. On the ordinary open complement V of those zeros and poles, all r_i and t are actual smooth logarithms of analytic units, with d'd''r_i=d'd''t=0.

Whenever eta is nonzero and r belongs to supp(phi), equations (5.2) or (6.3) give, for i>=1,

\[
 U_i=r_i-n_{i,p}s>3\epsilon,
\]
\[
 U_0=\ell-\sum r_i+
           \left(\sum n_{i,p}-e_p\right)s>3\epsilon.   \tag{7.2}
\]

Outside bad tubes the same inequalities hold with s-terms absent. These estimates used (6.3) only on W_epsilon, where it had already been established. There is no circular inference of its hypotheses.

Consequently any form with scalar factor eta*phi(r) has support contained in the compact K_{3epsilon}, once extended across the removed divisor as zero. It stays strictly away from the boundary of W_epsilon. The global model functions U_i are used only for this continuity/compactness estimate; they will never be differentiated.

## 8. The compact principal-divisor primitive

If every m_p=0 there is nothing to prove. Otherwise choose

\[
 0<h<\min_{p\in B,\ m_p\ne0}|m_p|a_p
\]

and chi∈C_c^\infty((-h,h)) equal to one near zero. On V⊂W_epsilon put

\[
 \Omega_r=\bigwedge_{i=1}^{n-1}
                         \mathrm d'r_i\wedge\mathrm d''r_i,
 \qquad
 \beta=\phi(r)\chi(t)\Omega_r\wedge\mathrm d''t.         \tag{8.1}
\]

The form eta*beta extends by zero to a compactly supported ordinary smooth (n-1,n)-form on X_C. Extension across the removed divisor is valid because eta is zero near it. Extension across W_epsilon is valid by (7.2) and compactness of K_{3epsilon}. This is a statement about the actual source, not compactness of a target image alone.

On the transition collar of eta_p, if m_p!=0 then |t|>=|m_p|a_p>h, so chi(t)=0. If m_p=0, then (6.3) gives t=0 on the entire ordinary transition collar, hence d''t=0. Thus

\[
                 \mathrm d'\eta\wedge\beta=0          \tag{8.2}
\]

as a source form. This includes every bad point with zero residual F-order.

Since r_i,t are logarithms of analytic units on V, differentiation gives

\[
 \mathrm d'\beta=
       \phi(r)\chi'(t)\Omega_r\wedge\mathrm d't
                                      \wedge\mathrm d''t.
                                                               \tag{8.3}
\]

The derivative of phi repeats a d'r_i and vanishes. The total degree of Ω_r is even, so moving d't past it introduces no sign. No derivative or wedge involving a global model-metric current occurs.

Where eta is nonzero, the support of (8.3) is contained in the finitely many bad p-collars with m_p!=0. Outside those tubes t=0 pointwise; continuity of t and vanishing of chi' on an actual interval around zero imply ordinary-neighborhood vanishing of the form. The statement remains valid at points reducing to η_C, without claiming that their reduction fibres are ordinary open.

In a contributing p-collar,

  0<s<h/|m_p|<a_p,

so eta=1. Since chi' vanishes near zero, this support also stays away from s=0. Together with (7.2), each resulting top form has compact support inside its own actual p-tube.

## 9. Shear, signs, and the divisor relation

On the p-collar the coordinate change is

\[
 (u,s)\longmapsto(r,s)
       =(u+(n_{1,p},...,n_{n-1,p})s,\ s).              \tag{9.1}
\]

Its matrix is integral triangular with determinant one. Since t=m_ps, the top form (8.3) becomes

\[
 m_p^2\phi(u+n_ps)\chi'(m_ps)\Omega_q.                 \tag{9.2}
\]

All mixed terms repeating d's or d''s vanish. The two differential blocks give m_p^2; no further normal-bundle, lattice, or orientation factor remains.

For every s at which the integrand is nonzero, (7.1) and the support of phi imply that its translated u-support lies inside Q_p and inside W_epsilon. Therefore

\[
               \int\phi(u+n_ps)\,\mathrm du=1.        \tag{9.3}
\]

This is also where the e_p*s correction in (6.4) is used. The integration may be taken over the actual slice of Q_p, since the missing part has zero integrand.

Closedness, the finite source-support decomposition in Section 8, and (2.3) now give

\[
 \begin{aligned}
 0&=\langle T,\mathrm d'(\eta\beta)\rangle\\
  &=\sum_{p\in B,\ m_p\ne0} b_T(p)
      \int_0^{\delta_p}m_p^2\chi'(m_ps)
             \left(\int\phi(u+n_ps)\,\mathrm du\right)\mathrm ds\\
  &=-\sum_p m_pb_T(p).
 \end{aligned}                                                    \tag{9.4}
\]

For either sign of m_p,

\[
 \int_0^{\delta_p}m_p^2\chi'(m_ps)\,\mathrm ds
   =m_p\bigl(\chi(m_p\delta_p)-\chi(0)\bigr)=-m_p.
\]

This proves (2.4) from closedness on the original n-dimensional source. It did not restrict T to a tangential fibre or manufacture an (n-1)-fold slicing operation.

## 10. Positivity, residue degree, and precise wall interpretation

The coefficients define a positive finite-valued homomorphism λ_T on Div(C), annihilating principal divisors. To recall why it factors through degree over k, let D have degree zero and choose an effective divisor H with deg_k(H)+χ_k(O_C)>0. Riemann--Roch gives a nonzero section of O_C(H+jD) for every integer j. Thus an effective divisor is linearly equivalent to H+jD and

  0<=λ_T(H)+jλ_T(D)

for all positive and negative j. Hence λ_T(D)=0. Applying this to d_q p-d_p q yields (2.5). This proof retains degrees and Euler characteristics over k and does not require geometric connectedness.

The primitive-coordinate calibration of the actual K_p-polyannulus is one. Viewing the same space over K multiplies it by the full finite degree [K_p:K]=d_p, by CLD14.4.3. The extension is unramified, and the transformations (9.1) have determinant one, so no additional ramification or lattice factor is present. The conclusion is b_{\delta_{X_C}}(p)=d_p.

For e_p=1 the source Gauss n-cell of (2.1) is the interior of the canonical n-simplex adjacent to the (n-1)-wall belonging to C. Thus its standard-coordinate T/calibration ratio is c. For e_p=0 the added curve parameter exposes a further Gauss n-cell not present as an n-cell in the unmarked model skeleton; these additional directions are essential in testing arbitrary divisors on C.

If (R) is assumed on the actual local moments, it identifies their represented coefficients with the numbers tested above. To transfer this ratio to an arbitrary moment F, a genuine common analytic moment and an isolatable identical full-dimensional source patch, or another proved source-form comparison, are still needed. This packet supplies none of those hypotheses for every arbitrary F-cell. It proves neither T=c*delta_{X_C} on all ordinary tests nor global rigidity on X.

## 11. What the theorem avoids, and what remains open

The proof handles arbitrary deformations of the formal neighborhood allowed by the stated strictly semistable model. It does not linearize that neighborhood: the remainder terms in (6.2) are present, and their valuation is controlled only after all normal radii have a fixed positive lower bound.

The following assertions have NOT been proved here:

- every wall of an actual analytic tropical moment is realized by such a proper semistable residual curve on the original field;
- an arbitrary positive closed current can be pulled back through a semistable alteration or restricted to a tangential analytic fibre;
- norm-one residual lifts at one non-rigid point automatically define uniform compact tests on a neighboring source star;
- all represented full-dimensional source cells are accessible from the displayed Gauss cells;
- a full refinement-compatibility theorem or the global P21.3 conclusion.

The accompanying OBSTRUCTIONS_AND_SOURCE_COMPARISON.md gives an explicit nonisotrivial deformation, an actual-moment branching diagnostic, and the exact limits of the GRW/CLD source routes. Those diagnostics do not contradict (2.5).

This is an authored bounded research result requiring independent review of the entire argument, especially Sections 3, 6, 7, and 8. It is not an audit of itself and not a production acceptance.
