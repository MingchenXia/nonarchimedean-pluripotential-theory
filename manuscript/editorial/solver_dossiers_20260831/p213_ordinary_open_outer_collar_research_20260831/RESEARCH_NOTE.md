# Ordinary-open outer collars at independent normal radii

Authored starting 31 August 2026; completed and frozen 1 September 2026 (Asia/Shanghai). Author: /root/p082_independent_reaudit.
Status: frozen authored research candidate, identified by the companion manifest; independent review and production verification are separate.

## 1. Exact setting, assertions, and provenance

Let R be a complete DVR, K its fraction field, pi a uniformizer, k its perfect residue field, and ell=v(pi)>0, with v=-log|.|. Let mathcalX be an integral proper flat regular R-scheme of relative dimension n>=2 with smooth generic fibre and special fibre
\[
                     \sum_\gamma N_\gamma E_\gamma
\]
having strict-normal-crossing SUPPORT. Its multiplicities need not be one or prime to the residue characteristic. Write X=mathcalX_K^an.

Choose n distinct VERTICAL components E_0,...,E_{n-1}, and a nonempty connected component C of their scheme-theoretic intersection. It is a smooth proper integral k-curve, not necessarily geometrically connected. Let X_C=red^{-1}(C). Put
\[
 A=\mathcal O_{\mathcal X,\eta_C},\qquad
 I=\mathfrak m_A=(z_0,\ldots,z_{n-1}),
\]
where z_i is a rational function generating the Cartier ideal of E_i at eta_C. These form a regular parameter system of A.

Assume there is an analytic point xi centered at eta_C such that
\[
 \alpha_i=v_\xi(z_i)>0\quad(0\le i<n),\qquad
 \alpha_0,\ldots,\alpha_{n-1}\ \hbox{are Q-linearly independent}.
                                                        \tag{1.1}
\]
Existence of such a point is not proved here. Since units of A have value zero, the equation for pi gives sum N_i alpha_i=ell. Thus (1.1) is equivalent to independence of ell,alpha_1,...,alpha_{n-1}. Section 3 proves that the point has generic algebraic support; that is not silently assumed in the topology argument.

Let W be ANY ordinary open neighbourhood of xi in X.

The first assertion is purely geometric. Let U_i be the finite continuous vertical model radii, locally v(x_i) for a component equation. There exist a closed box P in the positive normal orthant, with alpha in its interior, a finite set S of closed points of C, and numbers delta_p>0 with actual curve parameters w_p at p, such that EVERY analytic point of
\[
 \mathcal O(P,S,\delta)=
 \{y\in X_C:(U_0(y),\ldots,U_{n-1}(y))\in P,\ 
       y\in red^{-1}(p),\ p\in S\Rightarrow
                         0<v(w_p(y))<\delta_p\}
                                                        \tag{1.2}
\]
belongs to W. The implication in (1.2) excludes w_p=0. There is no residual restriction over closed points outside S or over eta_C. P is closed; (1.2) is not declared to be a formal-open or ordinary-open chart. It is an all-source containment statement, not just a statement on a skeleton. S can be enlarged by any chosen finite set, with new shallow cutoffs, preserving the conclusion.

For the current consequence, assume explicitly the exact local finite-projection premise (L):
sibling p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md,
SHA256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a,
Sections 2-5. Its geometric properness and canonical degree apply to the full coordinate tube independently of the domain of a current.

If T is a positive \(\mathrm{d}'\)- and \(\mathrm{d}''\)-closed ordinary current of bidegree (0,0) given only on W, then, with omitted E_0 fixed, shallow full inverse-image collar patches define finite numbers lambda_T(p)>=0 for every closed p of C. These are independent of shrinking and local parameter choices, depend only on the germ of T at xi, and satisfy
\[
 \sum_p ord_p(f)\lambda_T(p)=0\quad(f\in k(C)^\times),
 \qquad \lambda_T(p)=c_T[\kappa(p):k]\quad(c_T\ge0).
                                                        \tag{1.3}
\]
For the canonical integration current restricted to W, lambda_T(p)=N_0[\kappa(p):k]. Every one of the finitely supported principal-divisor tests in (1.3), or any chosen finite list, is represented by a compact ordinary test form supported INSIDE W. No extension of T from W is performed.

This is not whole-current rigidity, an all-moment source representation, or model capture for arbitrary analytic charts. No individual source-cell conclusion from (R) is asserted in this packet. The geometry requires the independent normal point (1.1); Section 10 gives an explicit failure of the all-source containment without that condition.

Root supplied the finite-expansion outline and requested the affine-domain and full-source checks. The author supplied the complete argument below and the dependent-weight diagnostic. Root's review will therefore not constitute a fresh independent review. The author's earlier rational-norm replacement and model-adaptation notes are context, not a black box for the new containment claim.

## 2. Geometric facts used on the actual model

We use the completed-ring and vertical-radius geometry from Sections 3-4 of the frozen nonreduced-wall packet (V):
p213_nonreduced_snc_wall_residual_functional_research_20260831/RESEARCH_NOTE.md,
SHA256 d9e57c21c276edb40bc7619562b7f0a782cdc7a7eb05a04dd0b0cf0770dc9ea9.
The global whole-tube current conclusion of V is NOT applied to T on W.

Here is the needed geometry and its algebraic justification. At a closed p, local component equations x_0,...,x_{n-1}, together with a curve parameter w, are a regular parameter system. At most one additional vertical component occurs; let N_p be its multiplicity, or zero if none occurs. Choose w as its equation when present. Perfectness of k gives the finite unramified DVR R_p/R with residue field kappa(p). Hensel lifting embeds R_p in the completed regular local ring. The formal power-series presentation is
\[
 \widehat{\mathcal O}_{\mathcal X,p}
  =R_p[[x_0,\ldots,x_{n-1},w]]/
       (\pi-\epsilon_p\prod_i x_i^{N_i}w^{N_p}).
                                                        \tag{2.1}
\]
Indeed the map from the power-series ring is surjective by successive maximal-ideal approximation. The displayed relation has nonzero linear pi term because sum N_i>=n>=2, so its quotient is regular of dimension n+1; the further surjection to the completed local ring of that dimension is an isomorphism. The formal unit epsilon_p has unit constant coefficient and |epsilon_p|=1 on the open unit polydisc. No root is extracted.

Berkovich's special-formal generic-fibre construction and Proposition 1.3 of Vanishing cycles for formal schemes II identify (2.1) with the ENTIRE ordinary p-tube, with all parameters of norm <1. The construction includes w=0 when N_p=0. Removing w=0 gives the coordinate moment
\[
 q_p=(v(x_1),\ldots,v(x_{n-1}),v(w))=(u,s),
\]
with target
\[
 Q_p=\{u_i>0,\ s>0,\ \sum_{i=1}^{n-1}N_i u_i+N_p s<\ell\},
\quad
 U_0=\frac{\ell-\sum_{i=1}^{n-1}N_i u_i-N_p s}{N_0}.
                                                        \tag{2.2}
\]
The source, described over K_p=Frac(R_p), is viewed as a K-analytic space. This does not change the field of T.

The U_gamma are the continuous functions -log||1|| for the formal metrics on O(E_gamma). Unit changes of model frame have norm one, so they are locally v(component equation), finite and nonnegative. They satisfy sum N_gamma U_gamma=ell. The tube X_C is a clopen component of the tube of the full selected intersection. Therefore
\[
 K_a=\{y\in X_C:U_i(y)\ge a\ (0\le i<n)\}
                                                        \tag{2.3}
\]
is compact for every a>0: it is the appropriate clopen piece of a closed subset of proper X. Only continuity, not smoothness, of the U_i is used.

## 3. Finite leading monomials and generic support

The center condition gives v_xi(a)>=0 for a in A and v_xi(a)=0 for a in A^\times. This follows because both a unit and its inverse belong to the local valuation ring.

Fix nonzero a in A. Let d=ord_I(a)<infinity; finiteness follows from Krull intersection. Choose M>d with
\[
                         M\min_i\alpha_i>d\max_i\alpha_i.
                                                        \tag{3.1}
\]
Finite successive approximation modulo I^M gives an EXACT identity in A,
\[
 a=\sum_{|\nu|<M}c_\nu z^\nu+
                      \sum_{|\nu|=M}b_\nu z^\nu,
                                                        \tag{3.2}
\]
where each c_\nu is zero or a chosen unit lift of a nonzero residue coefficient, and b_\nu belongs to A. All degrees below d can be taken zero, and at least one degree-d coefficient is nonzero. This is finite algebra, not an assumed convergent expansion with a coefficient field.

The retained nonzero terms have distinct values nu dot alpha by (1.1), since all c_\nu have value zero. There is a unique least term, at index nu(a), of value at most d max alpha. Every tail term has value at least M min alpha. The strict ultrametric inequality consequently gives
\[
                  v_\xi(a)=\nu(a)\cdot\alpha<\infty.
                                                        \tag{3.3}
\]
In particular A maps injectively into H(xi). Its fraction field is K(mathcalX), so the underlying algebraic point on the generic fibre is generic. This conclusion justifies the later use of finite positive rational-function values.

For any FINITE collection of nonzero rational functions g, choose g=a_g/b_g with nonzero a_g,b_g in A and apply (3.2) separately. There is a closed box P_0 about alpha in the positive orthant and a number e>0 such that, for every one of these numerator/denominator expansions, all retained competitors have weight at least e more than the chosen leading term and
\[
              M\min_i U_i-\nu(a)\cdot U>e
                      \quad(U\in P_0).
                                                        \tag{3.4}
\]
There are only finitely many expansions and terms; (3.4) and the competitor inequalities follow by continuity from their strict inequalities at alpha. Fix rho>0 with every U_i>2rho on P_0.

## 4. Uniform estimates off finitely many points and on exceptional collars

Choose a finite set S of closed points of C containing all additional-component intersections and all failures along C of the following finite data:

- z_i is a local equation of E_i times a unit;
- every nonzero c_\nu in (3.2) is a model unit;
- every b_\nu in (3.2) is model-regular.

Such S is finite. The respective divisor supports or pole supports miss eta_C; their intersections with the proper integral curve are finite. For a tail coefficient b_\nu that is not a unit, only absence of poles is needed.

At EVERY point reducing to C minus S, including eta_C, these properties give
\[
          v(z_i)=U_i,\quad v(c_\nu)=0,\quad v(b_\nu)\ge0.
                                                        \tag{4.1}
\]
Thus (3.4) implies exact leading-term dominance on all such source points with U in P_0.

Fix p in S. All estimates that follow are first made on U_i>rho for every selected i. In (2.1), reduction modulo (x_0,...,x_{n-1}) is kappa(p)[[w]]. For any q in A^\times, write q=a/b with a,b in O_mathcalX,p having nonzero reductions modulo that ideal. Each numerator has an expansion
\[
                    a=w^r V(w)+\sum_i x_i A_i
                                                        \tag{4.2}
\]
with V a unit and all formal coefficients bounded by one. The remainder norm is at most exp(-rho). If r delta<rho, the first term strictly dominates on 0<s=v(w)<delta. The same applies to the denominator. Hence, for any fixed finite list of such units,
\[
                            v(q)=ord_p(\bar q)\,s
                                                        \tag{4.3}
\]
on the entire sufficiently shallow source collar, not just its skeleton.

For b in A that is not necessarily a unit, represent b=a/b' with a in O_mathcalX,p and b' having nonzero reduction. The numerator has norm <=1; applying (4.2) to b' yields
\[
                              v(b)\ge-B_p s
                                                        \tag{4.4}
\]
for some nonnegative integer B_p. The value infinity, if the numerator vanishes, is harmless. It would be incorrect to assign every such tail coefficient a residual unit order.

Apply (4.3) to z_i/x_i and to all c_\nu, and (4.4) to all b_\nu. There are integers n_{i,p} and gamma_{\nu,p} such that a retained monomial has value
\[
               \nu\cdot U+
                   \bigl(\nu\cdot n_p+\gamma_{\nu,p}\bigr)s.
                                                        \tag{4.5}
\]
Every tail has value at least M min U-C_p s, for some finite C_p. Choose delta_p so small that all these finitely many s-errors are smaller than the gaps in (3.4). Then the same chosen monomial remains strictly least on EVERY point with U in P_0, reduction p, and 0<s<delta_p. All denominators needed for the rational identities are nonzero there, so the identities define genuine analytic units on these collars. This also justifies their evaluation at analytic points with otherwise nontrivial algebraic support.

We have proved the useful simultaneous formula: for each of the chosen rational functions g there is an integral linear function L_g(U), with
\[
 v_\xi(g)=L_g(\alpha),\qquad
 v_y(g)=
 \begin{cases}
 L_g(U(y)),& red(y)\notin S,\\
 L_g(U(y))+\gamma_{g,p}s,& red(y)=p\in S,\ 0<s<\delta_p,
 \end{cases}
                                                        \tag{4.6}
\]
on all indicated source points. Coefficients at different p need not be uniformly bounded over an infinite set; only this FINITE S is involved.

## 5. The actual affine-open domain and proof of (1.2)

Choose any affine algebraic open U in mathcalX_K containing the generic point. By Section 3, xi belongs to U^an. The affine analytification topology is the subspace product topology of evaluations on O(U), as recalled in CLD Section 11.1.11. Consequently there are finitely many nonzero g_l in O(U) and finite open intervals J_l around v_xi(g_l) such that
\[
 \{y\in U^{an}:v(g_l(y))\in J_l\text{ for every }l\}
                           \ \subset W\cap U^{an}.
                                                        \tag{5.1}
\]
Zero functions impose no condition. The remaining issue is membership in U^an; rational inequalities stated only on U are not enough by themselves.

Let Z=mathcalX_K minus U, and let Zbar be its reduced scheme-theoretic closure in mathcalX. It is a proper closed subset of the integral model. Cover C by finitely many affine model opens V_j meeting C. Each contains eta_C. In each nonzero ideal I_Zbar(V_j), choose one nonzero element h_j. If the intersection with Zbar is empty, choose h_j=1. Each h_j is a nonzero rational function in A and vanishes on Zbar intersect V_j.

Apply Sections 3-4 simultaneously to all g_l and all h_j. Shrink the closed normal box P inside P_0, still with alpha in its interior, and shrink the finitely many delta_p, so that (4.6) puts every g_l value strictly inside J_l. The same argument ensures each h_j is defined and nonzero on every resulting outer-collar point.

For such a point y, choose j with red(y) in C intersect V_j. The point lies in the generic analytic domain of V_j, where h_j is the actual regular function chosen above. If y lay in Z^an, then h_j(y)=0, contradicting its computed nonzero value. Hence y belongs to U^an. Now (5.1) proves y belongs to W.

This proves (1.2), including the actual algebraic-open domain. No projectivity, Cartier boundary for Z, or global rational approximation of every analytic function was assumed. The witness argument uses the coherent ideal of Zbar, not a fictitious global defining equation. The only role of the finite model-affine cover is to choose these algebraic witnesses; it is never promoted to an ordinary open cover of X.

If a finite set S' is added to S, simply remove a deep portion of each newly named tube. This makes (1.2) smaller, so the containment remains true. Local parameters at original exceptional points are retained; parameters at new points can be arbitrary as in Section 2.

## 6. Local coefficients without a current on the whole Q_p-preimage

Fix a closed p and local coordinates as in Section 2. Enlarge S to contain p. By continuity of (2.2), there is a connected open box B_p about alpha'=(alpha_1,...,alpha_{n-1}) and a number delta>0 such that
\[
        B_p\times(0,\delta)\subset Q_p,\qquad
 D_p=q_p^{-1}(B_p\times(0,\delta))\subset W.
                                                        \tag{6.1}
\]
Indeed the full normal vector in (2.2) tends uniformly to alpha as (u,s) tends to (alpha',0), and alpha is interior to P. The outer-collar lemma controls the ENTIRE inverse image, so this is not merely a statement about Gauss points.

The geometric map q_p is proper by (L). Its restriction to the full inverse image of the open target box in (6.1) remains proper. Thus any compact target form pulls back to a compact ordinary form in D_p, hence in W. Restrict the given T to D_p and define its target pushforward by these compact pairings. Positivity gives a positive scalar distribution in top degree, and \(\mathrm{d}'T=0\) makes all its first partial derivatives vanish. On the connected target box it is a finite constant times Lebesgue measure. Denote the constant by lambda_T(p).

This repeats the elementary current argument of (L) on a restricted target open. It does NOT apply (L)'s statement for a globally defined current on the entire original Q_p. Only the geometric properness of that map is used globally; the current is never extended.

Two allowed normal boxes about alpha' have a nonempty connected smaller common box, and two shallow intervals have a common interval (0,delta'). Proper pullbacks of one nonzero compact test there compare the constants. Hence shrinking does not change lambda_T(p).

Changing a selected component equation preserves U_i. If N_p>0, changing w preserves its norm as well. If N_p=0, two curve parameters obey
\[
                          w'=wV+\sum_i x_i B_i.
\]
With the selected normal radii bounded below, sufficiently shallow collars give |w'|=|w|. Conversely, a shallow w' value forces that same w value by strict domination. A smaller common target box therefore has identical actual source support and identical form pullbacks in both coordinates. The constants agree. Any two initial algebraic/generic parameter choices can be compared this way.

Finally, if W is replaced by a smaller neighbourhood of xi on which the same current germ is given, (1.2) and (6.1) apply again and produce a smaller common collar. Thus these coefficients depend on the germ, not on an arbitrary chosen extension of T.

For the canonical current, the finite degree N_0 over K_p and the restriction-of-scalars factor d_p from (L) give lambda_T(p)=N_0d_p on every such restricted target box.

## 7. Compact principal-divisor tests entirely inside W

Fix f in k(C)^\times. Choose F in A^\times with residue f and retain the generic Cartier generators z_i, i>=1. Define m_p=ord_p(f) and n_{i,p}=ord_p(overline{z_i/x_i}). Enlarge the finite S from the outer-collar lemma to include all extra-component points and all divisor/pole failures for F and z_i/E_i along C. This includes zero-order bad points. Outside their tubes,
\[
                            v(F)=0,\qquad v(z_i)=U_i.
                                                        \tag{7.1}
\]
These are pointwise model-unit identities, not an ordinary-neighbourhood constancy assertion.

Choose rho>0 much smaller than every alpha_i. Work first on W_rho={U_i>rho for every selected i}, which is an ordinary open subset of X_C independent of the current. The finite local estimates of Section 4 give, on shallow p-collars,
\[
 r_i=v(z_i)=U_i+n_{i,p}s,\qquad t=v(F)=m_p s,
\]
\[
 N_0U_0=\ell-\sum_{i=1}^{n-1}N_i r_i+
                  \left(\sum_{i=1}^{n-1}N_i n_{i,p}-N_p\right)s.
                                                        \tag{7.2}
\]
These identities are proved BEFORE using them to infer stronger normal bounds.

Choose a nonnegative smooth phi(r), integral one, with compact support in a sufficiently small box about alpha'. At s=0 its full normal vector belongs to the interior of P and has all U_i>4rho. For the finitely many p in S, choose cutoffs
\[
                         0<a_p<b_p<\delta_p
\]
so small that for r in supp(phi) and 0<=s<=b_p the vector in (7.2) belongs to a fixed closed box P_1 in the interior of P and has all U_i>3rho. This is a finite compact-continuity choice. Explicit bounds may be imposed as well:
\[
 |n_{i,p}|b_p<\rho,\qquad
 |\sum_iN_i n_{i,p}-N_p|b_p<N_0\rho.
                                                        \tag{7.3}
\]
Reduce them further so that each translated target support (u=r-n_ps,s) lies in a box used to define lambda_T(p). Such boxes are neighbourhoods of (alpha',0) in the shallow sense of (6.1), so this is possible.

On W_rho let eta equal one off the bad tubes, and equal eta_p(s) in the p-tube, where eta_p is smooth, equals one for s<=a_p, and zero for s>=b_p. Set eta_p=0 at w=0 when N_p=0.

Here is the full source gluing check. The support of 1-eta_p, relative to W_rho, is contained in the actual zero locus (2.1) inside the closed polydisc
\[
                 |x_i|\le \mathrm{e}^{-\rho},\qquad |w|\le \mathrm{e}^{-a_p}.
                                                        \tag{7.4}
\]
The formal equation converges there and the zero locus is compact, entirely inside the p-tube. If N_p=0, w=0 is INCLUDED; no punctured-properness result is being used at that locus. Hence 1-eta_p extends smoothly by zero across the complement of the p-tube within W_rho. The finite disjoint gluing defines ordinary smooth eta.

Let V be the locus in W_rho where all z_i and F are analytic units. On the excluded zero/pole sets eta is identically zero on a neighbourhood, since shallow collars have exact nonzero leading terms and eta already vanishes in the deep part. Forms with factor eta phi(r) thus extend by zero across those loci. Their support is contained in compact K_{3rho}.

More importantly, their support is a compact SUBSET OF W, not merely of X_C. The closure of the nonzero locus has U in P_1 by continuity. If a limit point reduces to p in S, its ordinary open p-tube contains the tail of any approaching net. There \(|w|\ge\mathrm{e}^{-b_p}\) on the nonzero locus, so the limit has 0<s<=b_p<delta_p; in particular it is not w=0. If its reduction is outside S, (1.2) imposes no residual condition. Every limit point therefore belongs to the outer-collar set contained in W. This proves compact source support inside W and avoids inferring it from a tropical image alone.

## 8. The primitive and residual divisor relation

If every m_p is zero, the asserted relation is immediate. Otherwise choose
\[
 0<h<\min_{p\in S,\ m_p\ne0}|m_p|a_p,\qquad
 \chi\in C_c^\infty((-h,h)),\quad \chi=1\text{ near }0 .
\]
On V define
\[
 \Omega_r=\bigwedge_{i=1}^{n-1}\mathrm{d}'r_i\wedge \mathrm{d}''r_i,\qquad
                 \beta=\phi(r)\chi(t)\Omega_r\wedge \mathrm{d}''t.
                                                        \tag{8.1}
\]
Section 7 proves that eta beta extends to a compact ordinary (n-1,n)-form supported inside W. The form may be constructed geometrically on X_C and then restricted to W; this does not extend T.

On each transition collar, \(\mathrm{d}'\eta\wedge\beta\) vanishes. If m_p is nonzero, |t|>=|m_p|a_p>h makes chi(t)=0. If m_p=0, t is identically zero on the whole ordinary collar and \(\mathrm{d}''t=0\). All zero-order bad points, including those introduced solely to control W, are therefore harmless but are not omitted.

On V the logarithms are pluriharmonic, and differentiating gives
\[
 \mathrm{d}'\beta=\phi(r)\chi'(t)\Omega_r\wedge \mathrm{d}'t\wedge \mathrm{d}''t.
                                                        \tag{8.2}
\]
No global U_i is differentiated. Off the contributing bad tubes, chi'(t) is zero on an ordinary neighbourhood because t=0 there and chi' vanishes near zero. On a contributing tube, its support has s bounded away from zero and s<h/|m_p|<a_p. All selected normal radii have the previously proved margin. Consequently the derivative is a finite sum of compact source tests in the collar boxes where lambda_T(p) was defined.

The actual shear (u,s)->(u+n_ps,s) has determinant one. The two differential blocks from t=m_ps give m_p^2, so closedness of the current GIVEN ONLY ON W yields
\[
 \begin{aligned}
 0&=\langle T,\mathrm{d}'(\eta\beta)\rangle\\
  &=\sum_{p:m_p\ne0}\lambda_T(p)
           \int_0^\infty m_p^2\chi'(m_ps)
                           \left(\int\phi(u+n_ps)\,\mathrm{d}u\right)\mathrm{d}s\\
  &=-\sum_p m_p\lambda_T(p).
 \end{aligned}                                             \tag{8.3}
\]
There is no translated-support loss at a target face: (7.2)-(7.3) place the full translated support inside the local box and Q_p. Its phi integral is one. For either sign of m_p, the last one-variable integral equals -m_p because chi(0)=1 and chi vanishes before the outer end of the chosen collar.

All pairings are with compact forms inside W. No current slice, scalar extension, or zero-extension/differentiation identity for currents has entered.

For a finite list of residual functions, take the union of their bad sets and finite coefficient lists before making these choices. A common sufficiently small normal support and shallowness budget then works; the cutoffs chi may be chosen separately. Each test is finite and compact in W.

## 9. Degree factorization and the exact remaining boundary

The coefficients are individually finite and nonnegative, so
\[
                    \lambda(\sum a_pp)=\sum a_p\lambda_T(p)
\]
is a well-defined positive homomorphism on divisors, whose supports are finite. By (8.3) it annihilates principal divisors.

If deg_k D=0, choose an effective H with deg_k H+chi_k(O_C)>0. The degree/Euler-characteristic formula gives h^0(H+jD)>0 for every integer j. Hence H+jD is linearly equivalent to an effective divisor and
\[
                          0\le\lambda(H)+j\lambda(D)
                                   \quad(j\in\mathbf Z).
\]
Thus lambda(D)=0. Applying this to d_q p-d_p q proves (1.3). This uses degrees and Euler characteristics over k, not geometric connectedness or a k-rational point.

The result is a local residual FUNCTIONAL at the independent normal point, not T=c delta on all source tests. In particular:

- No such point or adapted model is constructed for an arbitrary analytic moment.
- No statement for a point with dependent normal weights is obtained.
- All selected components remain vertical, with positive multiplicities.
- The source representation R and all-moment accessibility are not proved or used.
- The original closed-current argument uses only collar-domain restrictions; it does not extend T to the whole proper residual tube.
- No production acceptance or full P21.3 conclusion is claimed.

## 10. Why independence cannot simply be dropped

There is an elementary all-source topological obstruction at dependent weights. Take K=C((pi)). Blow up P^1_R at one closed special-fibre point, obtaining the regular strictly semistable curve model with a node xy=pi. Take its product with P^1_R. The selected two vertical components meet in the proper curve C=P^1_k; their tube is an annulus factor times the good-reduction analytic curve.

At the monomial point above eta_C with alpha_x=alpha_y=ell/2, the Gauss rule gives
\[
                        |y^2-\pi|=|\pi|.
\]
Hence
\[
                    W=\{|y^2-\pi|>|\pi|/2\}\cap X_C
                                                        \tag{10.1}
\]
is an ordinary neighbourhood of that point.

Every normal box about (ell/2,ell/2), and every shallow residual interval in a chosen p-tube, has actual source points with y=sqrt(pi), x=sqrt(pi), after viewing points over the finite extension as ordinary Berkovich points over K. A Gauss point of any prescribed shallow w-radius supplies the residual factor. These points have the required normal and residual radii but lie outside W. They are not Gauss points for the normal moment, which is precisely why checking only a skeleton would miss them.

Thus no whole inverse-image normal-box collar lies in W at these weights. Nor can a finite exceptional set repair the cofinite outer-collar statement: choose p outside that set. This is a counterexample to dropping (1.1) from (1.2), not a counterexample to closed-current rigidity. The example introduces no pullback of an unknown current.

## 11. Verification status

The proof is now complete as an authored research argument. Sections 3-5 contain the new ordinary-topology/finite-expansion bridge; Sections 6-9 give its domain-sensitive current consequence conditional on L. V is used for its actual-model geometry and as a proof reference, not by applying its whole-tube current theorem outside its hypotheses. The source ledger identifies these interfaces exactly.

The parent read the complete draft and was notified that the domain checks and proof were complete before this freeze. Any independent review must read the entire new bridge and the compact-support argument, not infer acceptance from the separate audits of L or V. A separate bounded check of the Section 10 example is not a review of the positive proof and is not a premise of it. No live or earlier frozen file is edited.
