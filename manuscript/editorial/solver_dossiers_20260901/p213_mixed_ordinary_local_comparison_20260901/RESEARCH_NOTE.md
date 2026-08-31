# Local residual coefficients on a mixed SNC model

Date: 1 September 2026. Research author: /root.
Status: conditional research synthesis; new independent review and production Rethlas verification are required. No live-book theorem or open-problem retirement.

## 1. Purpose and exact inputs

Three arguments address different domain issues. The point-retaining blowups replace selected horizontal components by vertical ones while keeping a specified analytic point. The outer-collar argument supplies entire inverse images and compact primitives inside an arbitrary ordinary neighbourhood of that point. The proper target-open comparison identifies the represented source coefficients without extending a current to the whole modelled tube. This note proves their compatibility on a mixed model; it does not infer any one of these conclusions from the others alone.

The exact research premises are:

- P: `../../solver_dossiers_20260831/p213_point_retaining_mixed_blowup_research_20260831/RESEARCH_NOTE.md`, SHA-256 `1d8531a8cc4df4a11f21e56ba02ad4393f192f1ad8bec55c1c9cb27126ce4f55`. Only its geometric Sections 2-8 are used. Its optional whole-tube current statement is NOT applied.
- O: `../../solver_dossiers_20260831/p213_ordinary_open_outer_collar_research_20260831/RESEARCH_NOTE.md`, SHA-256 `f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b`. We use its all-source ordinary-open containment and its local residual functional, including the compact principal-divisor primitives on the current's actual domain. O in turn assumes the geometric/properness and canonical-degree parts of L.
- Q: `../p213_proper_target_open_comparison_20260901/RESEARCH_NOTE.md`, SHA-256 `35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec`. Its target-constant statement is used on connected target opens. The additional source-cell assertion below assumes Q's full L/R hypotheses, in particular R's DISPLAYED source-multiplier formula on the actual restricted source. It does not assume R's stronger local-affine-separation wording.

L is the exact finite-projection note with SHA-256 `3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a`. These premises have scoped independent research reviews, not production acceptance. Root helped develop P/O and authored Q and L; root is not the sole independent reviewer of this synthesis.

## 2. Setting and conclusion

Let R be a complete DVR with fraction field K, uniformizer pi, perfect residue field k, and ell=v(pi)>0, where v=-log|.|. Let mathcalX be an integral proper flat regular R-model of relative dimension n>=2 with smooth generic fibre. A reduced strict-SNC boundary B contains the support of its special fibre and may also contain horizontal divisors. Set X=mathcalX_K^an.

Choose n boundary components D_0,...,D_{n-1}. Let C be a nonempty connected component of their scheme-theoretic intersection, and suppose D_0 is vertical. Write N_i for the special-fibre multiplicity of D_i; thus N_0>0, the other N_i are nonnegative, and N_i=0 for a horizontal component. The curve C is proper, smooth and integral over k but need not be geometrically connected.

Assume an actual point xi of X is centered at eta_C and has positive, Q-linearly independent values alpha_i on the selected component parameters. Then sum N_i alpha_i=ell. Neither existence of this model nor capture of an arbitrary analytic moment is asserted here.

Let W be any ordinary open neighbourhood of xi, and let T be a positive separately \(\mathrm d'\)- and \(\mathrm d''\)-closed current of bidegree (0,0) given ONLY on W.

At each closed p of C, choose actual local selected equations x_i and a residual parameter w. If an additional boundary component meets C at p, w is its equation; otherwise choose a curve parameter. Let N_p>=0 be its vertical multiplicity, with N_p=0 if there is no additional vertical component. Put d_p=[kappa(p):k]. The entire completed p-tube has the equation inherited in P,
\[
 \pi=\epsilon_p\prod_{i=0}^{n-1}x_i^{N_i}w^{N_p},
 \qquad |x_i|,|w|<1,
 \tag{2.1}
\]
over the unramified coefficient DVR with residue field kappa(p), viewed over K. Puncture the selected horizontal zero loci and w=0 when necessary, and denote this ordinary domain by P_p. Its actual moment and target are
\[
 q_p=(v(x_1),\ldots,v(x_{n-1}),v(w))=(u,s),
 \quad Q_p=\{u_i>0,\ s>0:\ \sum_{i=1}^{n-1}N_i u_i+N_p s<\ell\}.
 \tag{2.2}
\]
The omitted value is U_0=(ell-sum N_i u_i-N_p s)/N_0. All inverse images in this note are full inverse images in P_p, not selections of source sheets.

For every p there exist a connected open box B_p about alpha'=(alpha_1,...,alpha_{n-1}) and delta_p>0 such that
\[
 \Omega_p=B_p\times(0,\delta_p)\subset Q_p,
 \qquad D_p=q_p^{-1}(\Omega_p)\subset W.
 \tag{2.3}
\]
With omega_p the paired coordinate top form in (u,s), there is a finite lambda_0(T,p)>=0 satisfying
\[
 \langle T,q_p^*(h\omega_p)\rangle
       =\lambda_0(T,p)\int_{\Omega_p}h\,\mathrm d u\,\mathrm d s,
 \qquad h\in C_c^\infty(\Omega_p).
 \tag{2.4}
\]
The value is independent of allowable shrinking, parameter choices, and the point-retaining sequence used to construct (2.3). It depends only on the germ of T at xi and the indicated model/omitted component. There is c_0(T)>=0 such that
\[
 \lambda_0(T,p)=c_0(T)d_p,\qquad
 \sum_p\operatorname{ord}_p(f)\lambda_0(T,p)=0
               \quad(f\in k(C)^\times).
 \tag{2.5}
\]
Each displayed principal-divisor relation is obtained from a compact ordinary primitive inside W. The primitives for any prescribed finite list can be chosen simultaneously. For canonical integration, lambda_0=N_0d_p and c_0=N_0.

Under Q's additional L/R premises on each actual D_p, its coordinate-moment source cells have normalized coefficient c_0(T)/N_0; more precisely,
\[
 \langle T,\rho q_p^*\beta\rangle
   =\frac{c_0(T)}{N_0}
      \langle\delta_{D_p},\rho q_p^*\beta\rangle
 \tag{2.6}
\]
for arbitrary compact ordinary smooth source multipliers rho and smooth target top forms beta. This is a statement for the indicated coordinate-moment tests, not equality on all ordinary top forms from unrelated moments.

## 3. Apply the geometric modification without transporting a current

By P, there is a finite sequence of blowups along whole regular vertical strata, with final model mathcalX^f and selected proper curve C^f isomorphic to C. All final selected components are vertical. The generic-fibre map is an isomorphism, so both generic analytic spaces are literally identified with X. Xi still reduces to eta_C^f; its final selected weights alpha_i^f are positive and Q-linearly independent. The final omitted multiplicity is still N_0. No current is pulled through a nontrivial analytic modification: the original T is still defined on the SAME W in X.

For p^f over p the residue field, residual parameter and extra vertical multiplicity N_p are unchanged. P provides a real affine automorphism A_p of the retained coordinate space, with determinant one and last coordinate s unchanged, such that
\[
 S_p=A_p^{-1}(Q_p^f)\subset Q_p,\qquad
 P_{p^f}^f=q_p^{-1}(S_p),\qquad
 q_{p^f}^f=A_p\circ q_p
                 \quad\hbox{on this entire ordinary source}.
 \tag{3.1}
\]
Here the inclusion includes every intermediate chart inequality; this is P's backward-composition conclusion, not an inference from a final tropical image alone. Moreover
\[
 A_p(\alpha',0)=(\alpha^{f\prime},0).
 \tag{3.2}
\]
Although A_p need not be integral-affine, it is an identity of valuation functions coming from actual analytic coordinate identities on the common source. It may therefore be differentiated there. No equality of forms is inferred solely from a skeletal equality.

Apply O to the final all-vertical model, the SAME xi and W, and T on W. This gives connected final collar boxes
\[
 \Omega_p^f=B_p^f\times(0,\delta_p^f)\subset Q_p^f,
 \qquad (q_{p^f}^f)^{-1}(\Omega_p^f)\subset W,
 \tag{3.3}
\]
with final coefficients lambda^f(T,p^f)=c^f(T)d_p and compact W-supported principal-divisor primitives. It does not require T on the whole final C^f-tube. This is precisely why the whole-tube current paragraph of P is not invoked.

## 4. Pull the collars back, including every source point

Since A_p is affine and fixes the last coordinate, it has the form
\[
 A_p(u,s)=(L_pu+a_ps+b_p,s)
 \tag{4.1}
\]
with L_p invertible. Equation (3.2) gives L_p alpha'+b_p=alpha^{f\prime}. A small closed box around alpha' has its L_p-image strictly inside B_p^f. After shrinking its interior B_p and choosing delta_p>0 small, continuity gives
\[
 A_p(B_p\times(0,\delta_p))\subset\Omega_p^f.
 \tag{4.2}
\]
The same choices can enforce membership in Q_p. Alternatively (3.1) implies it because the image lies in Q_p^f. Hence (2.3) is established, and more precisely
\[
 q_p^{-1}(\Omega_p)
   =(q_{p^f}^f)^{-1}(A_p\Omega_p)
   \subset(q_{p^f}^f)^{-1}(\Omega_p^f)\subset W.
 \tag{4.3}
\]
All equalities hold on entire actual source domains by (3.1); no extra source point with the same moment values is omitted. The set A_p Omega_p is connected and ordinary open but need not be a product box. Q applies to this shape as well.

The geometric map q_p is proper by L, which permits zero horizontal exponents. Its restriction over Omega_p remains proper. Thus compact target forms and primitives have compact source pullbacks in W. Q's elementary target-distribution argument now gives (2.4) on the current's actual domain.

## 5. Compare the coefficients with one identical compact test

Take h in C_c^infinity(Omega_p), nonnegative and of integral one. Let h^f=h composed with A_p^{-1}; it has compact support in A_p Omega_p, and extends smoothly by zero to Omega_p^f. Its integral is one because det A_p=1. For paired top superforms,
\[
 A_p^*(h^f\omega_p^f)=h\omega_p;
 \tag{5.1}
\]
the differential factor is (det A_p)^2=1. This identity holds for actual ordinary forms after pullback to the common analytic source in (4.3). Compactness follows from properness, not from a source sheet count.

Pair the SAME resulting compact form with T, once using the original coordinates and once using the final ones. Equations (2.4), (3.3) and (5.1) give
\[
 \lambda_0(T,p)=\lambda^f(T,p^f)=c^f(T)d_p.
 \tag{5.2}
\]
Set c_0(T)=c^f(T). The canonical coefficient is unchanged because both N_0 and d_p are unchanged.

Two admissible original boxes about alpha' and two positive shallow intervals have a smaller common product box. A compact normalized test there compares their constants. This also proves independence from the particular point-retaining sequence: each sequence produces the same constant for T in the original q_p coordinates on a common full inverse image. We do not compare currents on unrelated final whole tubes.

Changing a component equation multiplies it by a model unit, so its norm is unchanged on the relevant reduction tube. If N_p=0, two residual parameters satisfy w'=wV+sum x_i B_i with bounded formal coefficients and V a unit. On a common sufficiently shallow collar where all selected normal values have a fixed positive lower bound, strict domination gives |w'|=|w|. Conversely a sufficiently shallow w' value forces the same w value: if |w| were at most the normal error bound, so would be |w'|. This proves equality of the entire two source collar domains after shrinking, not just equality where both were already prescribed. When N_p>0, model-unit invariance suffices. Coefficients are therefore parameter independent. The full normal values are bounded below on these collars by the positive alpha_i and continuity of the weighted equation, even for horizontal selected components.

For two representatives of the same T-germ, perform the construction in an ordinary neighbourhood of xi on which they agree. The same comparison proves germ independence. Constants need not be uniform for arbitrary unrelated xi or arbitrary unrelated models.

## 6. Principal-divisor primitives stay on W

The isomorphism C^f to C identifies their function fields, closed points, residue degrees and divisor orders. For f in k(C)^times, O supplies a compact ordinary (n-1,n)-form gamma_f inside W such that
\[
 \langle T,\mathrm d'\gamma_f\rangle
    =-\sum_{p^f}\operatorname{ord}_{p^f}(f)
                                      \lambda^f(T,p^f).
 \tag{6.1}
\]
Its actual source support and the zero-order bad branches are controlled by O, Sections 7-8. They are not replaced here by a claim that an entire final curve tube lies inside W. Under the generic-fibre identification, gamma_f is already a test form on the original X and W. There is no pushforward or zero extension of the unknown current.

Closedness and (5.2) give the second identity in (2.5). O permits a common finite set of bad points and normal/shallow budgets for a prescribed finite list of f's, so the same simultaneous compact-support assertion holds here. No infinite uniform family is asserted.

For completeness the degree implication is purely algebraic. The positive divisor functional Lambda(sum a_p p)=sum a_p lambda_0(T,p) annihilates principal divisors. If deg_k D=0, choose an effective H with deg_k H+chi_k(O_C)>0. Riemann--Roch in its degree/Euler-characteristic form gives a nonzero section of H+jD for every integer j. Therefore 0<=Lambda(H)+j Lambda(D) for all j, forcing Lambda(D)=0. Apply this to d_q p-d_p q to obtain the first identity of (2.5). This argument uses degrees over k and does not require a rational point or geometric connectedness.

## 7. Source coefficients and changing the omitted vertical component

Apply Q on D_p with m=N_0, coefficient degree d_p, target Omega_p and T restricted from W. Its hypotheses include the L single-Gauss-source geometry and R's precise source representation ON D_p. The aggregate lambda_0 has just been identified; Q consequently gives (2.6). Applying the same argument to final coordinate collars yields the same ratio c_0/N_0. This is not an assertion that every unknown source cell has been captured by one of those moments.

One can remove the apparent dependence of this ratio on the choice of omitted vertical component. Let D_j be another selected vertical component, so N_j>0. Reorder retained coordinates consistently after replacing x_j by x_0. The affine coordinate map B_{0j} between the two target descriptions is obtained from
\[
 v(x_0)=\frac{\ell-\sum_{i=1}^{n-1}N_i v(x_i)-N_p v(w)}{N_0}.
 \tag{7.1}
\]
It is a bijection between the two full positive weighted targets and has absolute determinant N_j/N_0. All coordinates involved are nonzero on the common punctured tube, and the equation comes from (2.1) with |epsilon_p|=1; this is again an actual smooth-function identity. It sends (alpha',0) to the limiting point for the other omission and fixes s.

Choose a sufficiently small common full-source patch in W, with one target open the affine image of the other. The same compact top-form computation as in Section 5 now has differential factor |det B_{0j}|^2 and Lebesgue factor |det B_{0j}|^{-1}. It gives
\[
 \lambda_j(T,p)=\frac{N_j}{N_0}\lambda_0(T,p),\qquad
 \frac{\lambda_j(T,p)}{N_j d_p}
     =\frac{\lambda_0(T,p)}{N_0 d_p}.
 \tag{7.2}
\]
To identify these with coefficients defined by product collars, take smaller product collars inside the corresponding affine target opens near their limiting points. The same compact-test comparison applies. Thus c_j=(N_j/N_0)c_0 and the normalized ratio is independent of which selected VERTICAL component is omitted. Omitting a horizontal component is not allowed by this finite-projection argument because its exponent is zero.

## 8. Example and limits

Take the product P^1_R times P^1_R, with selected D_0 the special fibre and D_1 the horizontal divisor z=0 on the first factor. Let xi reduce generically along their intersection and have weights (ell,sqrt(2)ell). The point-retaining sequence has two steps. Near the retained final curve the exact coordinates satisfy
\[
 \pi=rt,\qquad z=r^2t,
 \quad v(r)=v(z)-\ell,\quad v(t)=2\ell-v(z).
 \tag{8.1}
\]
The final selected components are both vertical. The original target patch ell<v(z)<2ell contains the specified point's limiting normal value, while the simpler strict-vertical-only blowup would require v(z)<ell and miss it. For arbitrary W about xi, the present proof uses sufficiently small full inverse-image collars inside this patch and W; it does not claim the entire displayed strip lies in W. Since the retained map is translation by ell and N_0=1, the original and final aggregate coefficients are equal, and their value is c_0 d_p.

The result handles mixed selected boundaries, arbitrary positive vertical multiplicities, and a current defined only on W over the original complete DVR. It still requires the specified proper SNC model and independent normal point. It proves neither arbitrary-cell capture nor all-moment or higher-bidegree rigidity. The known dependent-weight counterexample to all-source collar containment remains an obstruction to dropping independence by the same argument. No general nontrivially valued envelope theorem or full P21.3 conclusion follows.

Independent review of this assembly must check the actual domain equalities (4.3), the two compact top-form transformations, and the use of O's W-supported primitives. Separate passes for P, O and Q do not themselves constitute such a review. All new mathematical conclusions remain pending production Rethlas verification.
