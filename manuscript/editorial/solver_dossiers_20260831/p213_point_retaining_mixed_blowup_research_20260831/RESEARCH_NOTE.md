# Point-retaining mixed-to-vertical blowups

Research date: 1 September 2026, continuing the 31 August task.
Author: /root/p213_skeletal_hostile. Root supplied the proposed two-chart algorithm; this author is responsible for the proof below. This is a new isolated research candidate, not a production theorem, fresh independent audit, or claim about the full P21.3 problem.

## 1. Exact purpose and inputs

The previously frozen simpler mixed reduction uses the strict-vertical section at every step. It produces a whole all-vertical curve tube but can lose a given analytic point. Here the section is chosen from the weights of a prescribed point. The result is a finite sequence, a whole proper curve isomorphic to the old one, and exact maps of the entire punctured closed-point tubes. No ordinary-open support or arbitrary-moment capture result is proved.

The proof of the blowup geometry is given below, not inferred from tropical weight subtraction alone. The relevant preserved predecessor is:

- (M), the simpler mixed reduction, `../p213_mixed_snc_wall_blowup_reduction_20260831/RESEARCH_NOTE.md`, SHA-256 `9463a10f2918a01a214c458052a50c5604293a6e4192f7c5aa1c91234c7e1120`.

Its actual completed-tube presentation and the basic completion-to-tube interpretation are used in Section 6. The optional properness/current corollary in Section 9 explicitly assumes:

- (L), `../p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md`, SHA-256 `3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a`, Sections 2-5.

No chartwise representation premise (R), slicing theorem, generic source-sheet assertion, or ordinary-étale-sheet interpretation is used in the geometric statement. In particular, no independent re-verification of this author's all-vertical residual-functional theorem is claimed here.

## 2. Statement

Let K be a complete discretely valued field, R its valuation ring, k its perfect residue field, and pi a uniformizer. Set \(v=-\log|\cdot|\) and \(\ell=v(\pi)>0\). Let \(\mathcal X\) be an integral proper flat regular finite-type R-scheme of relative dimension \(n\ge2\), with smooth generic fibre. Let B be a reduced strict-normal-crossings divisor containing the support of the special fibre, with its remaining components horizontal.

Choose distinct components \(D_0,\ldots,D_{n-1}\) of B, with \(D_0\) vertical, and a nonempty connected component C of their scheme-theoretic intersection. Put
\[
 N_i=\operatorname{ord}_{D_i}(\pi),\qquad N_0>0,\qquad N_i\ge0.
 \tag{2.1}
\]
Thus C is a proper smooth integral k-curve; geometric connectedness is not assumed. Let \(\xi\in \mathcal X_K^{\rm an}\) reduce to the generic point \(\eta_C\). For component equations \(x_i\) at \(\eta_C\), assume
\[
 0<\alpha_i:=v_\xi(x_i)<\infty,\qquad
 \alpha_0,\ldots,\alpha_{n-1}\ \hbox{are linearly independent over }\mathbf Q.
 \tag{2.2}
\]
Changing a component equation by a local unit does not change its weight: both the unit and its inverse have norm at most one at a point centered at \(\eta_C\). Since no further boundary component contains C,
\[
 \sum_{i=0}^{n-1}N_i\alpha_i=\ell.
 \tag{2.3}
\]
Independence in (2.2) concerns the n numbers \(\alpha_i\), NOT the list obtained by adjoining ell; (2.3) is not excluded.

There exists a FINITE sequence of blowups along connected components of intersections of one selected vertical and one selected horizontal component, with the following properties.

1. Every center is a closed regular codimension-two subscheme contained in the special fibre. All resulting models are integral proper flat and regular over R, their reduced total boundary is SNC, and every generic-fibre map is an actual isomorphism.
2. At every stage the n selected components have a whole proper connected intersection component \(C_r\simeq C\). Under the generic-fibre identification the SAME point xi reduces to \(\eta_{C_r}\).
3. The distinguished selected component in slot 0 remains vertical of multiplicity N_0. Every selected component is vertical at the end. All final normal weights are finite, positive, and Q-linearly independent.
4. Near each p in C and its unique point on every \(C_r\), the normal-coordinate changes are monomial with integral unimodular exponent matrices. The curve parameter and every other boundary parameter can be retained. Whole final curve tubes are ordinary open subdomains of the original curve tube.
5. On the punctured closed-point tubes, omitting slot 0 gives exact entire-source identities (6.6), (6.9), and (7.3). The retained target change is affine with determinant ONE. It is generally rational-affine, not necessarily integral-affine for the standard retained-coordinate lattices.
6. For each fixed closed p, the original target patch selected by the complete sequence contains a relative neighborhood of \((\alpha_1,\ldots,\alpha_{n-1},0)\) with positive last coordinate. This is a statement about the explicit target inequalities; it does not assert an ordinary neighborhood basis at xi or support inside a prescribed ordinary open W.

The construction need not be canonical or minimal. There is no claimed uniform bound on its number of blowups as xi varies.

## 3. The two actual blowup charts and the global sections

At a current stage distinguish a selected vertical V of multiplicity N_0 and select a horizontal H. Let Z be the connected component of \(V\cap H\) containing the current C. By strict SNC, \(V\cap H\) is regular of codimension two. In a noetherian regular scheme the irreducible components are disjoint; consequently this connected component is closed, integral, and regular. It is proper because the model is proper and V is vertical. No third boundary component contains Z, by the expected codimension of a triple SNC intersection.

Locally along Z let x and y be equations for V and H. They are part of a regular system of parameters. The blowup of the ideal (x,y) has charts
\[
 x=yt \quad\hbox{and}\quad y=xr.
 \tag{3.1}
\]
These are actual affine Rees charts. For example, \(A[t]/(x-yt)\) has no y-torsion. Indeed, if \(yg=(x-yt)a\), reduction modulo y and regularity of x modulo y give \(a=ya_1\). Cancellation of y in A[t] gives \(g=(x-yt)a_1\). Repeating this proves absence of all y-power torsion, so the quotient injects into its localization at y, with image \(A[x/y]\). The other chart is symmetric. The general affine chart construction is [Stacks, Lemma 31.33.2](https://stacks.math.columbia.edu/tag/01OF).

For completeness these charts remain regular at EVERY point over Z, not only at the two sections. In a localization of A[t] above a prime of Z, the old regular parameters remain independent normal directions; this follows also by lifting a parameter system of the local polynomial fibre. The equation x-yt has nonzero cotangent class \(x-\bar t y\). Its quotient is regular. At t=0, the boundary parameters are y,t and the other old boundary parameters. At t invertible, the strict transform of V is absent, and y together with the other boundary parameters remains part of a regular system. This argument is valid at generic polynomial-fibre points and after arbitrary residue-field extensions; it does not require a separable residue for t. The other chart gives the same conclusion. Thus the reduced total boundary is again strict SNC, including away from the selected section. Outside Z the blowup is the identity.

The exceptional divisor E has two disjoint sections
\[
 E\cap\widetilde V\simeq Z,\qquad E\cap\widetilde H\simeq Z.
 \tag{3.2}
\]
The first is \(y=t=0\) in the first chart and the second \(x=r=0\) in the second chart. Their coordinate rings are A/(x,y). These are GLOBAL sections: replacing x,y by unit multiples changes t or r by a unit ratio and preserves the corresponding zero section. No normal line bundle is trivialized. The two component line directions in the normal bundle supply exactly these two sections.

A further boundary divisor meeting Z has a third regular parameter z there, since it does not contain Z. Its strict transform is still cut out by z in the displayed charts, and its restriction to either section is its original restriction to Z. Therefore intersecting either section with the other n-2 selected strict transforms gives exactly the old selected intersection over Z. In particular the component corresponding to C is a whole proper connected component \(C'\simeq C\), not C with finitely many points removed. The full new selected intersection contains E and hence lies above Z, so there is no additional component outside this comparison.

At any closed p of C, a further boundary component, if present, has its equation w unchanged in these charts; its multiplicity in the special fibre is unchanged as well. A boundary component discarded by choosing one section is disjoint from the new curve, since it meets the opposite section. Its strict transforms after later blowups remain disjoint from all subsequent curves: those curves map into the current curve.

The blowup is projective, integral, and an isomorphism away from Z. Because Z is contained in the special fibre, its generic-fibre map is an isomorphism. Integrality implies R-torsion-freeness and hence flatness over the DVR. Properness and generic smoothness are retained. The underlying general blowup facts are [Stacks, Lemmas 31.33.4, 31.33.9, and 31.33.13](https://stacks.math.columbia.edu/tag/01OF); the boundary and section computations above supply the additional assertions.

## 4. Choosing a section from the point

Let the current weights in slots 0 and h be
\[
 a=v_\xi(x)>0,\qquad b=v_\xi(y)>0,\qquad N_h=0.
\]
They are unequal, because the current normal weights are Q-linearly independent.

**Case A: \(b>a\).** Use \(y=xr\). Select E in slot 0, \(\widetilde H\) in slot h, and all other selected strict transforms. Their curve is the section \(E\cap\widetilde H\) restricted to C. The new coordinates and weights are
\[
 x_0'=x_0,\quad x_h'=x_h/x_0,\quad x_i'=x_i\ (i\ne0,h),
 \qquad
 \alpha_0'=a,\quad \alpha_h'=b-a.
 \tag{4.1}
\]
The distinguished multiplicity is still N_0, and slot h is still horizontal. This follows by substituting \(y=xr\) into the divisor equation: the exponent of y was zero, so the exceptional exponent is exactly N_0. The strict transform of the old V is discarded and misses the new curve.

**Case B: \(b<a\).** Use \(x=yt\). Select \(\widetilde V\) in slot 0, E in slot h, and all other selected strict transforms. The new coordinates and weights are
\[
 x_0'=x_0/x_h,\quad x_h'=x_h,\quad x_i'=x_i\ (i\ne0,h),
 \qquad
 \alpha_0'=a-b,\quad \alpha_h'=b.
 \tag{4.2}
\]
Now slot h becomes vertical of multiplicity N_0, while slot 0 keeps multiplicity N_0. This eliminates one selected horizontal. The strict transform of H is discarded and misses the new curve.

All new selected coordinates have strictly positive valuation at xi, so the lift of xi reduces to their intersection in the chosen chart. Its reduction maps to \(\eta_C\). The chosen intersection component is isomorphic to C and has exactly one point over \(\eta_C\), namely its generic point. Hence the center of xi is precisely \(\eta_{C'}\). This verifies point retention using reduction and actual charts, not merely subtraction of numbers.

Each normal weight update is an elementary integral row subtraction and has determinant one. Thus it preserves Q-linear independence; it also preserves finiteness and, with the stipulated inequality, positivity. The local equation of pi verifies
\[
 \sum_i N_i'\alpha_i'=\sum_i N_i\alpha_i=\ell.
 \tag{4.3}
\]
The global chart choice is independent of changes of local component equations, because those changes have valuation zero at xi.

## 5. Finite termination and the final monomial matrix

Process the selected horizontal slots in any fixed order. For one current slot h, let a,b be its current weights as above. While \(b>a\), Case A leaves a fixed and subtracts a from b. Since b/a is not an integer, after
\[
 k=\lfloor b/a\rfloor
\]
Case A steps the new horizontal weight is \(b-ka\), strictly between zero and a. If b<a initially, k=0. Apply Case B once. The horizontal slot is now vertical and never needs processing again.

The number of steps for this slot is exactly \(k+1<\infty\). There are finitely many selected horizontal slots. The distinguished weight can decrease when a horizontal is eliminated, but is strictly positive at every finite stage; it is held fixed during the subtraction block for the next horizontal. Thus induction proves termination. This is not an appeal to termination of an infinite subtractive Euclidean algorithm.

Write the resulting models and curves as \(\mathcal X_r,C_r\), \(0\le r\le m\), and use superscript f for the final stage. The residue fields at corresponding closed points are unchanged by \(C_r\simeq C\). The multiplicities satisfy
\[
 N_0^f=N_0,\qquad
 N_i^f=N_i\ \ (N_i>0),\qquad
 N_i^f=N_0\ \ (N_i=0,\ i>0).
 \tag{5.1}
\]
The final vector \(\alpha^f\) is positive and Q-linearly independent.

Near any chosen p the inverse chart expressions are coordinate multiplications, not root extractions. Composing them yields an integral matrix P such that
\[
 P\in {\rm SL}_n(\mathbf Z),\quad P_{ij}\ge0,\qquad
 x_i=\prod_{j=0}^{n-1}(x_j^f)^{P_{ij}},\qquad w=w^f.
 \tag{5.2}
\]
The expressions are exact when the local equations are carried through the charts as specified. Arbitrary later changes of component equations only introduce units. The matrix is independent of p: it is the finite word of the chosen coordinate operations. Each row has a positive entry, so the substitution sends normal parameters to elements of the final maximal ideal. Moreover
\[
 \alpha=P\alpha^f,\qquad N^f=P^{\mathsf T}N.
 \tag{5.3}
\]
The second equality is consistent with (5.1); in Case A the exponent being added to the distinguished column is the zero exponent N_h.

Every original selected horizontal strict transform is disjoint from \(C_f\) after its eliminating Case B step. Original or intermediate distinguished vertical components discarded in Case A are likewise disjoint. Consequently no such discarded boundary contributes an unrecorded extra boundary point of \(C_f\).

## 6. Exact entire-source domains at a closed point

Fix a closed p of C. Choose actual regular parameters \(x_0,\ldots,x_{n-1},w\) at p with the x_i defining the selected components. If an additional boundary component occurs, take w to be its equation. Its special multiplicity is denoted N_p; this is zero if it is horizontal or if there is no additional vertical component. There is at most one additional boundary component. The multiplicity N_p stays unchanged through the sequence.

As in (M), over the unramified coefficient DVR R_p with residue \(\kappa(p)\), the actual completed tube is
\[
 \pi=\epsilon(x,w)\prod_{i=0}^{n-1}x_i^{N_i}w^{N_p},
 \qquad |x_i|<1,\quad |w|<1,
 \tag{6.1}
\]
with epsilon a formal unit of norm one. This presentation includes the case of total monomial degree one. At every later stage it is obtained by the actual chart substitutions; the new formal unit still has unit constant term and norm one. The coefficient map R_p can be composed with the local completed map, and the residue field remains \(\kappa(p)\). Nothing is split by a field extension.

Puncture the p-tube at every selected horizontal zero locus and also at w=0 when N_p=0; call it P_p. Every displayed coordinate is then nonzero. The moment and target are
\[
 q_p=(v(x_1),\ldots,v(x_{n-1}),v(w))=(u,s),\quad
 Q_p=\{u_i>0,\ s>0:\sum_{i=1}^{n-1}N_i u_i+N_p s<\ell\}.
 \tag{6.2}
\]
The omitted valuation is the affine function
\[
 U_0(u,s)=\frac{\ell-\sum_{i=1}^{n-1}N_i u_i-N_p s}{N_0}>0.
 \tag{6.3}
\]
These are actual analytic moment functions on the punctured tube, not formal labels on a skeleton.

At one current step use the same notation for the current N_i, q_p, Q_p, and the current closed point. The primed point is its unique point on the selected section.

### Case A

Define
\[
 Q_p^A=\{(u,s)\in Q_p:u_h>U_0(u,s)\},\qquad
 A_p(u,s)=(u_1,\ldots,u_h-U_0(u,s),\ldots,u_{n-1},s).
 \tag{6.4}
\]
All multiplicities are unchanged. Since N_h=0, U_0 is independent of u_h and
\[
 A_p:Q_p^A\xrightarrow{\ \sim\ }Q_p'
 \tag{6.5}
\]
is an affine bijection, with inverse adding U_0 to the h-th coordinate. Under the generic-fibre isomorphism,
\[
 P_{p'}=q_p^{-1}(Q_p^A)\subset P_p,\qquad
 q_{p'}=A_p\circ q_p\quad\hbox{on this ENTIRE domain}.
 \tag{6.6}
\]
Indeed, in the new tube \(|x_0|<1\) and \(|x_h/x_0|<1\), so \(|x_h|<1\) and \(u_h>U_0\); all other parameters and w are unchanged. Conversely these inequalities on the old tube make the quotient x_h/x_0 analytic with norm less than one and make the lifted point reduce to p' in the chosen section. The punctures correspond: x_0 is nonzero, so x_h=0 if and only if x_h/x_0=0, and w has not changed. Thus both inclusions concern all analytic points in the tube, not a chosen branch of a finite map.

### Case B

The included coordinates are unchanged, but \(N_h'=N_0\). Therefore
\[
 Q_p'=Q_p^B:=\{(u,s)\in Q_p:U_0(u,s)>u_h\}.
 \tag{6.7}
\]
The quotient \(x_0'=x_0/x_h\) has valuation
\[
 U_0'(u,s)=U_0(u,s)-u_h>0.
 \tag{6.8}
\]
Using this actual quotient and its inverse \(x_0=x_hx_0'\) gives
\[
 P_{p'}=q_p^{-1}(Q_p^B)\subset P_p,\qquad
 q_{p'}=q_p|_{P_{p'}}.
 \tag{6.9}
\]
Every final selected coordinate in this pair is forced nonzero by its positive exponent; the old horizontal puncture therefore corresponds exactly. Again w is punctured on both sides if needed.

These equalities deliberately concern PUNCTURED closed-point tubes. If N_p=0, the whole new p'-tube may contain w=0, whereas q_p does not. Independently of this puncture distinction, compatibility of reduction gives
\[
 X_{C'}=\operatorname{red}_{\mathcal X'}^{-1}(C')\subset
 X_C=\operatorname{red}_{\mathcal X}^{-1}(C)
 \tag{6.10}
\]
under the actual generic-fibre isomorphism. Both are ordinary open tubes of closed subschemes in the proper models. No ordinary open cover is inferred from a formal Zariski cover.

## 7. Determinants, composition, and the retained point

In Case A, the h-th retained coordinate in (6.4) is
\[
 u_h'=u_h+\sum_{\substack{1\le i<n\\i\ne h}}\frac{N_i}{N_0}u_i
                    +\frac{N_p}{N_0}s-\frac{\ell}{N_0}.
 \tag{7.1}
\]
Every other coordinate is unchanged. Hence its linear determinant is exactly one. Case B has the identity retained-coordinate map. Notice the distinction:

- the FULL n normal weights at eta_C change by an integral unimodular matrix;
- the retained n coordinates (the n-1 normal valuations and s), after eliminating U_0 using pi, generally change by a RATIONAL shear with determinant one.

If N_0 does not divide an indicated N_i or N_p, (7.1) is not an integral-affine automorphism of the standard retained lattice. No such assertion is needed or made.

Let \(\mathcal A_p:\mathbf R^n\to\mathbf R^n\) be the composition of the affine maps for the whole sequence, taking the identity at a Case B step. Define
\[
 S_p=\mathcal A_p^{-1}(Q_p^f).
 \tag{7.2}
\]
Induction using (6.5)-(6.9) proves
\[
 S_p\subset Q_p,\qquad
 P_{p^f}=q_p^{-1}(S_p),\qquad
 q_{p^f}=\mathcal A_p\circ q_p,\qquad
 \det(\mathcal A_p)_{\rm lin}=1.
 \tag{7.3}
\]
In particular S_p is the patch obtained by imposing EVERY intermediate strict inequality. No additional inequalities or selected analytic sheets are omitted. To see why the inverse image in (7.2) automatically satisfies all intermediate conditions, work backwards: each inverse Case A maps all of its new target to Q_p^A, and each inverse Case B is the inclusion of all of its new target Q_p^B. Iterate. The inverse source maps are the monomial multiplications (5.2), defined on the entire final punctured tube.

Every affine map leaves s unchanged and extends to s=0. At xi, w is a unit of the local ring at eta_C, so \(v_\xi(w)=0\). Component equations at p and at eta_C differ by units at eta_C and give the same weights. Consequently
\[
 \mathcal A_p(\alpha_1,\ldots,\alpha_{n-1},0)
       =(\alpha_1^f,\ldots,\alpha_{n-1}^f,0).
 \tag{7.4}
\]
The final positive normal weights satisfy
\[
 \ell-\sum_{i=1}^{n-1}N_i^f\alpha_i^f=N_0\alpha_0^f>0.
\]
Thus the right side of (7.4) is an interior point of the final normal slice at s=0. Continuity of the finite affine maps and strict inequalities yields, for this fixed p, a \(\delta_p>0\) such that
\[
 |u_i-\alpha_i|<\delta_p\ (1\le i<n),\qquad 0<s<\delta_p
 \quad\Longrightarrow\quad (u,s)\in S_p.
 \tag{7.5}
\]
Shrink delta also below all relevant positive normal margins. This is only a finite-dimensional target calculation. Xi itself reduces to eta_C, not to a closed p, and is not asserted to belong to P_p. Equation (7.5) is not a theorem that those collars fit inside an arbitrary ordinary neighborhood of xi.

All C_r are whole proper curves isomorphic to C and xi lies in every \(X_{C_r}\) by its retained generic center. This proves the point-retaining geometric statement in Section 2.

## 8. Two diagnostics

### 8.1 The simplified section can lose the point

Let \(\mathcal X=\mathbf P^1_R\times_R\mathbf P^1_R\), let V be the special fibre and let H be z=0 in the first factor. Then \(C=V\cap H\simeq\mathbf P^1_k\). Take the Gauss seminorm with
\[
 v_\xi(\pi)=\ell,\qquad v_\xi(z)=\sqrt2\,\ell,
\]
and generic reduction in the second factor. Concretely on the affine coordinates z,w it is the two-variable Gauss seminorm with radii \((\exp(-\sqrt2\,\ell),1)\). Its reduction on the original model is eta_C. The two normal weights are Q-linearly independent.

Always taking the strict-V section would impose \(v(z)<\ell\) and lose xi. The point-retaining algorithm first uses \(z=\pi r\), then \(\pi=rt\). The final selected weights are
\[
 v(t)=(2-\sqrt2)\ell,\qquad v(r)=(\sqrt2-1)\ell,
\]
both positive, with both selected multiplicities one. The retained coordinate changes by \(u'=u-\ell\); its final target is \(0<u'<\ell\), or
\[
 \ell<u<2\ell
\]
in the original coordinate. This patch contains the prescribed weight. The exact inverse normal equations are \(\pi=rt,\ z=r^2t\), with nonnegative exponent matrix of determinant one. Both chosen curves are whole copies of C, as in Section 3.

### 8.2 Equality is a real obstruction to THIS section algorithm

In the same model instead take the Gauss seminorm with radii \((|\pi|,1)\) in z,w. Its normal weights are \((\ell,\ell)\), which violate (2.2). After blowing up \((\pi,z)\), both ratios \(z/\pi\) and \(\pi/z\) have norm one. The residue of \(z/\pi\) at this Gauss point is transcendental over k(w); the reduction is the generic point of the exceptional projective-line fibre over eta_C, not either of its zero/infinity sections. Neither selected curve in (3.2) retains the point as its generic center.

This shows why equality cannot be assigned arbitrarily to one of the two cases. It is not a proof that no other modification or enlarged boundary could treat dependent weights. The independence assumption is a sufficient way of avoiding every equality throughout the stated finite algorithm.

## 9. Optional conditional compact-test comparison

This section is not required for the geometry and does not assert an ordinary-W support theorem. Assume (L), Sections 2-5, for the actual local equations at the original and final stages. Then inverse images of compact subsets of Q_p and Q_p^f are compact in the corresponding punctured tubes.

For \(\varphi\in C_c^\infty(Q_p^f)\), its pullback by \(\mathcal A_p\), initially on S_p, extends smoothly by zero to Q_p with compact support. By (7.3), the two pulled-back test forms have exactly the same entire compact source support. The identity of moment pullbacks can be checked in the actual common analytic moment consisting of the old and new nonzero coordinates: the chart quotient identities hold there, and the formal unit in (6.1) has valuation identically zero. Thus differentiating the displayed affine valuation identity is legitimate in that smooth-form sheaf; no ordinary-sheet claim is involved.

For the standard paired top superform \(\Omega\), the linear determinant one gives
\[
 \mathcal A_p^*\Omega=\Omega,\qquad
 \int_{S_p}\varphi(\mathcal A_p(q))\,\mathrm dq
       =\int_{Q_p^f}\varphi(q')\,\mathrm dq'.
 \tag{9.1}
\]
More generally the top superform change has the square of the determinant, and Lebesgue change has its absolute value; both are one here. Accordingly, if T is an actual positive separately closed (0,0) current on the WHOLE X_C and b_p,b_p^f denote the constant pushforward coefficients supplied by (L) in these two coordinate systems, restriction to \(X_{C_f}\) and one integral-one test give
\[
 b_p=b_p^f.
 \tag{9.2}
\]
The canonical coefficients are \(N_0[\kappa(p):k]\) on both sides by (L), since the omitted multiplicity and residue field are unchanged. These are aggregate pushforward coefficients. No single-source interpretation is asserted here, and no R assumption has been hidden in the calculation.

If T is given only on an ordinary W containing xi, the whole-tube restriction used in this paragraph is NOT automatically available. The geometric point retention alone does not justify (9.2) in that situation.

## 10. Exact remaining boundaries

The result handles a GIVEN actual proper regular mixed SNC model, a WHOLE proper selected residual curve, and a GIVEN analytic point with the stipulated independent positive normal weights. It retains that point while converting the selected components to vertical ones. Arbitrary positive special-fibre multiplicities and perfect residue fields are allowed; no tame or reduced-fibre hypothesis was inserted.

The proof does not construct such an SNC model from an arbitrary moment chart, principalize the functions of a prescribed analytic moment, or show that every relevant current coefficient can be captured by this construction. It does not prove an ordinary-W compact-primitive lemma, compatibility between unrelated chart coefficients, or equality of currents on all tests. It is not a solution of either the whole bidegree-zero rigidity problem or the full P21.3 residual.

A fresh independent review of the frozen new proof is still required. Root contributed the algorithm outline and cannot serve as its sole fresh reviewer. The previous all-vertical proof and the simpler mixed proof are preserved unchanged.
