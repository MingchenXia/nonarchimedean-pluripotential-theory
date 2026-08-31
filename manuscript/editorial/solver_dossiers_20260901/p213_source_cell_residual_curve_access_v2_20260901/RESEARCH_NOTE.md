# Access from a source cell to a residual curve

Date: 1 September 2026. Research author: /root.
Version 2: the source cell is explicitly required to belong to W. The frozen first version remains unchanged; see the source ledger.
Status: new conditional research assembly, not a production-accepted theorem. No inventory change or all-current rigidity claim.

## 1. Inputs and the point of the argument

The finite-rank capture statement and the nearby-wall construction have different hypotheses. Capture supplies a relatively open patch of a coordinate SOURCE skeleton. The wall construction starts with a relatively open patch of the MODEL monomial cell. Equality of dimensions alone would not identify these patches. Section 3 supplies that identification by two continuous maps which agree on dense independent radii. We then compare one actual compact test on a closed-point collar to the original source-cell coefficient.

The precise geometric research inputs are:

- A: `../p213_maximal_rank_source_cell_capture_research_20260901/RESEARCH_NOTE.md`, SHA-256 `4cc25ff627af56aca05c8733e3e5bff65aea21015abe35e49726f9966bb1b384`.
- B: `../p213_toroidal_nearby_wall_research_20260901/RESEARCH_NOTE.md`, SHA-256 `5ad7cc7f5899ba3a251ba6d3417ec4456f0fa5cdc21db05ea8f262dcc17ab38e`.

The optional current conclusion uses:

- O, the ordinary-open outer-collar note, SHA-256 `f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b`, including its geometric L premise and W-supported principal-divisor tests;
- Q, the proper target-open comparison, SHA-256 `35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec`, with the displayed R source representation on the domains where it is applied.

O and Q are not inputs to the purely geometric access statement. Conversely A and B by themselves compute no current coefficient. The separate mixed-local synthesis is not needed: the wall constructed here is already all-vertical.

## 2. Statement in the original-field algebraic setting

Let K be complete discretely valued with residue characteristic zero, valuation ring R, uniformizer pi and ell=v(pi)>0. Let X be a smooth proper integral K-variety of dimension n>=2. Let f_1,...,f_r be nonzero rational functions, U their common algebraic unit-open locus, and W an ordinary open subset of U^an. Put F=(v(f_1),...,v(f_r)).

Let Delta be a compact full-dimensional source cell for the restriction F|W, explicitly with Delta contained in W, on which F is affine-injective. Let V be any nonempty relatively open subset of its interior. Under A and B there is a proper regular SNC model of a smooth proper variety Y, with a generic proper birational map to X which is an isomorphism over U, and a whole smooth proper residual curve Gamma on a further vertical blowup of that model, such that:

1. Gamma is a connected component of an intersection of n VERTICAL components. Its normal multiplicities may be greater than one.
2. An independent-normal monomial point eta centered at eta_Gamma belongs to V, using the actual isomorphism over U to identify the analytic points. There is an entire adjacent closed n-simplex tau contained in V, one of whose facets contains eta in its relative interior.
3. At the closed maximal-stratum point p_* corresponding to tau, the original moment F is an affine function of rank n of the final retained coordinate moment q_* on the ENTIRE punctured p_*-tube. This identity is on the actual source, not only on tau.

Now let T be a positive separately \(\mathrm d'\)- and \(\mathrm d''\)-closed current of bidegree (0,0) on W. Assume R's displayed representation for F, the required coordinate moments and their actual common-domain restrictions, and the L/O/Q premises. In this additional conclusion require Delta to lie in a coefficient-constant top cell of the chosen R presentation. Let b_Delta and a_Delta>0 be the coefficient of T and the canonical integration coefficient on Delta in the same cell coordinates, and write
\[
                         r_\Delta=b_\Delta/a_\Delta.
 \tag{2.1}
\]
For the residual curve Gamma, omit one selected vertical component of multiplicity M_0>0. The local residual coefficients provided by O, at eta and on full inverse-image collars INSIDE W, satisfy
\[
 \lambda(T,p)=M_0 r_\Delta[\kappa(p):k]
                       \quad(p\in\Gamma\text{ closed}).
 \tag{2.2}
\]
Consequently Q identifies the normalized coefficients on every one of those specified coordinate collars with r_Delta, including collars in residual directions which need not belong to the original F cell. Their compact principal-divisor tests are the ones in O and remain supported in W.

The statement does not say that r_Delta equals the ratio of every other unrelated cell. Establishing one common value through arbitrary source incidences remains a separate task. Nor does it assert that tau's entire analytic inverse image lies in W.

## 3. From a coordinate source patch to an actual model cell

Apply A to the finite rational moment. It gives a proper regular adapted model mathcalY, a generic map isomorphic over U, and a finite union E of target affine subspaces of dimension less than n. We identify W with its ordinary inverse image in Y^an using this isomorphism, not an unproved pullback operation on arbitrary currents.

The set V cannot lie in F^{-1}(E), since F is affine-injective on the n-cell. Choose x in V outside E. After ordinary shrinking at x, A gives a closed maximal boundary stratum p, its n+1 boundary parameters t_0,...,t_n, with N_0>0, and the actual coordinate moment q=(v(t_1),...,v(t_n)). On the punctured ordinary p-tube,
\[
 F=A_pq+b_p,\qquad \operatorname{rank}A_p=n,
 \quad v(t_0)=\frac{\ell-\sum_{j=1}^nN_jq_j}{N_0}.
 \tag{3.1}
\]
On the trace of Delta in that ordinary tube, q is affine and injective: take a left inverse of A_p in (3.1). Choose a compact n-polytope Delta_0 in this trace whose relative interior contains x and lies in V. Its q-image is a compact n-polytope, and
\[
      \sigma_C:q(\Delta_0)\longrightarrow\Delta_0
 \tag{3.2}
\]
is continuous. Indeed q is continuous and injective on the compact Delta_0, and the ambient analytic space is Hausdorff.

B, Section 2, constructs the continuous original-field monomial section sigma_M on the entire positive weighted parameter slice of the same closed stratum p. In retained coordinates it is a continuous map defined on the positive target of q. At a point z of q(Delta_0) for which ell,z_1,...,z_n are Q-linearly independent, the full n+1 normal values given by (3.1) are Q-linearly independent. Both sigma_C(z) and sigma_M(z) are centered at p and have exactly these values. A's finite regular-local leading-term argument uniquely determines the valuation on the entire fraction field. It proves that both points have generic algebraic support and are equal.

Such z are dense in the full-dimensional polytope q(Delta_0), including up to its boundary. The two maps are continuous and the target Y^an is Hausdorff, so
\[
                     \sigma_C=\sigma_M
                           \quad\hbox{on }q(\Delta_0).
 \tag{3.3}
\]
Thus the relative interior of Delta_0 is genuinely a relative open subset of this MODEL monomial cell. It is not merely a subset of S_q of the same dimension. This density argument does not assert that all source points of a full q-inverse image are monomial points.

Apply B with a small relative neighbourhood inside that interior and with the ordinary neighbourhood W. Its vertical stratum blowups give the entire all-vertical closed simplex tau inside V, and a facet with a whole proper residual curve Gamma and an independent-normal point eta on it. These blowups leave Y's generic analytic space unchanged. Together with the isomorphism over U, every point of tau and the current's existing W are still on their original analytic source.

## 4. The full-rank moment identity at the adjacent closed point

Let p_* be the tracked closed maximal-stratum point for tau. Its n+1 boundary components are all vertical. Locally let y_0,...,y_n be their parameters. B's explicit toroidal chart construction gives
\[
 t_i=\prod_{j=0}^n y_j^{P_{ij}},\qquad
 P\in\operatorname{GL}_{n+1}(\mathbf Z),\quad
 P_{ij}\ge0,
 \tag{4.1}
\]
with every column strictly positive in the original parameter coordinates for the final contracted simplex. Local changes of generators only add units of norm one. The old selected parameters therefore all have positive finite values at EVERY point of the p_*-tube. This tube maps into the original p-tube; it is not a statement confined to monomial points.

Each original f_i is a monomial in the t_j times a local model unit near p. Pull back this expression to p_* and use (4.1). It is a monomial in all y_j times a model unit on the ENTIRE p_*-tube. In particular these rational functions are analytic units there. Their zero/pole divisors have no component through p_* other than the vertical ones, whose equations cannot vanish on the generic fibre.

Let N denote the row of old special multiplicities and M the matrix of old divisor orders of F. By A, the restriction of M to ker(N) is injective of rank n. The new rows are NP and MP. Since P is invertible, MP is injective on ker(NP). Eliminating one positive vertical coordinate using the equation for pi therefore gives an affine map of rank n,
\[
                      F=A_*q_*+b_*,
                           \operatorname{rank}A_*=n,
 \tag{4.2}
\]
on the whole p_*-tube. Here choose the eliminated coordinate among the n components defining Gamma, and use the remaining component as its residual parameter w. The resulting q_* has n-1 retained normal coordinates and s=v(w). The formal unit has norm one throughout this domain. Thus (4.2) is an identity of ordinary smooth valuation functions on a common analytic moment.

Because tau is the entire positive slice of this final maximal cone, its relative interior is parametrized by the entire positive q_*-target Q_*. Near eta on the chosen facet, s tends to zero and the other selected normal values tend to positive numbers. In particular every sufficiently small shallow collar target about eta meets tau's interior in a nonempty target open; its monomial source points are in Delta's interior and W.

## 5. Identify the residual constant with the original cell coefficient

Apply O to the final all-vertical curve Gamma at eta and to the same T given only on W. It gives, for every closed p of Gamma, full inverse-image collars D_p inside W and constants
\[
                   \lambda(T,p)=c_T[\kappa(p):k],
 \tag{5.1}
\]
as well as its compact W-supported principal-divisor primitives. At p_*, take such a collar D_* with coordinate moment q_* as above. Under the additional R/L premises, Q gives
\[
 \langle T,\rho q_*^*\beta\rangle
   =\frac{c_T}{M_0}
      \langle\delta_{D_*},\rho q_*^*\beta\rangle
 \tag{5.2}
\]
for arbitrary compact ordinary smooth source multipliers rho on D_* and smooth target top forms beta.

To compare this with Delta, choose a small compact monomial patch in tau's interior with q_*-image inside that collar target. This patch lies in Delta's interior. By (4.2), the maximal-variation source sets for F, q_* and their concatenation coincide on the entire D_*; both projections have full rank. Refine the two locally finite cell structures on this patch and choose a point off their lower-dimensional faces. Such a point exists because their locally finite lower-dimensional sets cannot cover its n-dimensional open image. Around it, an ordinary source neighbourhood isolates a common top-cell piece lying in Delta. This uses the actual common source sets and local finiteness, not equality of two unrelated target images or a stronger affine-separation assertion.

Choose n coordinates of F whose matrix in (4.2) is invertible. Choose a nonnegative compact source cutoff rho in that isolating ordinary neighbourhood and a smooth target top form whose pullback there has strictly positive canonical integral. Such a choice is possible on the common affine-injective top piece. If necessary shrink its target support within the piece. Extend the compact source cutoff by zero inside D_* and W.

The SAME resulting ordinary top form is expressed in the F coordinates or the q_* coordinates using (4.2). Both the current coefficient and the canonical coefficient acquire the same affine Jacobian factor. The R formula in the isolated F piece therefore evaluates its T-pairing as r_Delta times its canonical pairing. Equation (5.2) evaluates the identical form as c_T/M_0 times that same strictly positive canonical pairing. Hence
\[
                            r_\Delta=c_T/M_0.
 \tag{5.3}
\]
Substituting in (5.1) proves (2.2) for every closed p, including residual directions invisible to the original F moment. Q gives the stated coordinate-collar interpretation there. There is no comparison of aggregates without source isolation in this last step.

The coefficient r_Delta is unchanged on a smaller common source cell because it is the normalized coefficient in the fixed R presentation. Thus the argument works inside any nonempty relatively open V in Delta's interior. It does not prove equality between ratios assigned to different original source cells merely because those cells occur on a connected analytic space.

## 6. A coordinate example with a nonunit Jacobian

In B's example on P^2_R, the initial maximal-stratum parameters are pi,x,y and the moment is F=(v(x),v(y)). After the indicated extraction and repeated blowups, the primitive rays are (1,1,1), (m,m+1,m), (m,m,m+1), with vertical multiplicities 1,m,m. The corresponding monomial triangle shrinks toward (v(x),v(y))=(ell,ell), so it fits inside any fixed relative neighbourhood there for sufficiently large m.

Take the facet opposite the multiplicity-one ray. Its selected normals y_1,y_2 both have multiplicity m, and w=y_0 is the residual parameter at the adjacent closed point. Put q=v(y_2), s=v(w), omitting y_1. The actual coordinate equations give
\[
 v(y_1)=\frac{\ell-s-mq}{m},\qquad
 v(x)=\ell+v(y_1),\qquad v(y)=\ell+q.
 \tag{6.1}
\]
The retained affine matrix from (q,s) to F is
\[
 \begin{pmatrix}-1&-1/m\\1&0\end{pmatrix},
                    \qquad |\det|=1/m.
 \tag{6.2}
\]
The coordinate-collar canonical coefficient is m over a rational residual point, whereas the original (x,y)-Gauss coefficient is one. The Jacobian factor 1/m converts one to the other, just as it converts the corresponding arbitrary-current coefficients. Equation (2.2) reads lambda(T,p)=m r_Delta[kappa(p):k]. Setting every special multiplicity to one would therefore break this comparison, even though the normalized ratios remain equal.

## 7. Exact remaining gap

This assembly removes an existential accessibility premise in the residue-characteristic-zero algebraic setting: a prescribed full-dimensional rational-moment cell can be compared to a local residual functional on a proper curve, within any chosen relative cell neighbourhood and with all current pairings supported in W.

For general analytic moments, A's exact local rational replacement and finite compact source partition permit applying this result to the resulting finite presentations. They do not ensure that the constants for all summands coincide. The still-required continuation argument must compare these ratios through actual common source incidences, including directions contracted by a previous moment, and must handle the lower-dimensional attachments rather than simply deleting them. No such general propagation theorem is asserted here.

The result also leaves arbitrary nonalgebraizable analytic spaces, other value groups, residue positive characteristic without the model-existence interface, higher-bidegree currents, and full P21.3 outside its conclusions. New independent and production Rethlas verification are required for this assembly and its research inputs before any live theorem promotion.
