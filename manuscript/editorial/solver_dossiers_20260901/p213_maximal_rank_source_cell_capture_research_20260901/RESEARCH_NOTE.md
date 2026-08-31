# Generic source-cell capture by an adapted SNC coordinate moment

Date: 1 September 2026. Author: /root/p082_independent_reaudit.
Status: frozen authored research candidate, identified by the companion manifest. The parent was notified and read the complete draft before freeze. Fresh independent review and production are separate. No live or earlier frozen file is changed.

## 1. Exact result and its boundary

Let K be a complete discretely valued field, R its valuation ring, pi a uniformizer, ell=v(pi)>0, and k its perfect residue field. Let X be a smooth proper integral K-variety of dimension n>=1. For the existence of the adapted model below, assume char(k)=0. The rank/capture argument itself only needs the displayed adapted regular model, and does not use characteristic zero after that model is supplied.

Fix nonzero rational functions f_1,...,f_r on X. Let U be their common algebraic unit-open locus: the complement of the supports of their zero and pole divisors. Write F=(v(f_1),...,v(f_r)) on U^an and for its restrictions. Let W be any ordinary open subset of U^an. Write S_F for the maximal-variation source skeleton of F restricted to W in ambient dimension n, in the sense of CLD Definition 5.2.1. Consider any compact n-dimensional source cell C on which F is affine and injective.

The bounded conclusion is:

1. There is a proper integral regular R-model mathcalY, with a proper birational generic-fibre map Y->X, and a reduced SNC boundary B containing the special-fibre support and all total zero/pole supports. The generic map is an ISOMORPHISM over U. It need not be an isomorphism over all X.
2. There is a finite union E of affine subspaces of R^r, each of dimension less than n, such that
\[
 Z_C=\partial C\ \cup\bigl(C\cap F^{-1}(E)\bigr)
                                                        \tag{1.1}
\]
is a closed PL subset of C of dimension less than n.
3. Every x in C minus Z_C, viewed on Y through the isomorphism over U, reduces to a CLOSED point p where exactly n+1 boundary components meet. Some component is vertical. After omitting one vertical equation, their valuations give an actual analytic moment q on the punctured ordinary p-tube. On that ENTIRE tube
\[
                       F=A_pq+b_p,\qquad \operatorname{rank}A_p=n,
                                                        \tag{1.2}
\]
with rational A_p and b_p a rational vector times ell. In particular, on its ordinary intersection with W,
\[
                    S_F=S_q=S_{(F,q)}.                   \tag{1.3}
\]
Each x therefore has an actual relatively open source patch, and a smaller compact n-cell patch, described by the resolved model coordinates. This is not an inference from target overlap.
4. Points of these patches with Q-independent full normal weights are dense. At those points the valuation is uniquely given by the elementary finite leading-monomial rule of Section 6.

This is SNC-COORDINATE capture, not a theorem that its coefficients have one already-known value. The optional comparison under the source representation premise R is recorded in Section 7. Neither L, the residual-wall theorem, the ordinary-W outer-collar theorem, nor the point-retaining algorithm is required for the geometric capture assertion. No arbitrary current is pulled through a birational map: on W the map is an analytic isomorphism.

The remaining distinction matters. A relatively open coordinate patch inside W is not automatically a whole proper q-inverse target box or an entire residual-curve tube. Equality of normalized coefficients between overlapping descriptions does not, by itself, make their value a single constant across all charts. These are not silently supplied by (1.1)-(1.3).

## 2. Rational replacement for compact ordinary tests

Here is the exact interface with an initially analytic moment, rather than a rational one.

At an analytic point x of an algebraic analytification, choose an affine algebraic chart. The residue field of its underlying algebraic point is dense in H(x): by the seminorm construction H(x) is the completion of the fraction field of the affine coordinate ring modulo its kernel. Thus for an analytic unit h near x there is a rational function g, defined at x, with
\[
                         |h(x)-g(x)|<|h(x)|.
\]
Write a representative g=a/b with b(x) nonzero. Continuity and ordinary shrinking give the strict inequality throughout a neighborhood on which g is an analytic unit. The ultrametric inequality then gives |h|=|g| exactly on that whole ordinary neighborhood. Apply this to each of finitely many moment coordinates.

This is the strict-approximation mechanism of CLD Lemma 12.2.3, with algebraic residue-field representatives. It is not a global algebraization of the analytic functions. No algebraically closed field is needed for this direct argument.

For a compactly supported ordinary test form, finitely many such ordinary neighborhoods cover its support. Smooth compact source cutoffs provide a finite partition of unity near that support. Explicitly, choose nonnegative compact cutoffs phi_i inside those neighborhoods whose sum H is positive near the support, and a compact eta in {H>0} equal to one near it; use rho_i=eta phi_i/H and extend by zero. The test is the finite sum of rho_i times pullbacks by rational moments. Each summand has actual compact source support in its ordinary neighborhood.

Consequently the rational-moment assertion applies to each source cell relevant to these finitely many presentations. The source cutoffs need not be rational; any later use of R must permit them. The original analytic and rational tropical maps agree on the whole chosen ordinary neighborhood, so their ordinary pullback forms and maximal-variation source sets there agree.

## 3. An adapted model which preserves the algebraic unit-open locus

Only this section requires char(k)=0.

A proper integral R-model exists without assuming X projective. Indeed K=R[1/pi], so X->Spec(R) is separated and finite type. Nagata compactification gives a proper R-scheme containing X as an open subscheme. Take the closure of the integral open X with its reduced induced scheme structure. Its generic fibre is exactly X: the immersion of proper X in the separated generic fibre is also closed. The integral model is flat because it is R-torsion-free.

It is excellent, being finite type over the complete noetherian local ring R. Apply characteristic-zero desingularization with empty boundary, preserving the regular locus; the smooth generic fibre stays unchanged. On the resulting regular model put the finite divisorial boundary formed by the special-fibre components and the closures of every prime divisor occurring in div(f_i).

Apply Temkin, arXiv:0912.2570v2, Theorem 1.1.3, to this boundary. Its centers lie over the ORIGINAL boundary's non-SNC locus, and its output has SNC complete boundary and strictly monomial total transform. In particular it is an isomorphism over the original boundary complement. The algebraic open U lies in that complement on the generic fibre. Thus the final generic map is an isomorphism over U, even when its horizontal centers cause a nontrivial birational modification elsewhere.

This preservation clause is stronger than merely knowing the final map is birational. It permits identifying W and its test supports with ordinary opens on Y. No extension of an unknown current across an exceptional set is used.

Write the finite irreducible components of the final reduced boundary as B_gamma. A regular local ring is factorial (Stacks 0AG0), so each prime divisor is locally Cartier and rational functions with the indicated divisor differ from the corresponding parameter monomials by local units. There are fixed integers m_{i,gamma} and nonnegative integers N_gamma with
\[
 \operatorname{div}(f_i)=\sum_\gamma m_{i,\gamma}B_\gamma,
 \qquad
 \operatorname{div}(\pi)=\sum_\gamma N_\gamma B_\gamma.
                                                        \tag{3.1}
\]
The N_gamma are positive precisely on the vertical components. They need not be one or tame. Every horizontal component of this final boundary maps into X minus U, since the construction is an isomorphism over U and its initial horizontal boundary lies there. Conversely the full inverse image of X minus U is supported on the total horizontal boundary, by the strictly monomial total-transform assertion. Thus its support is exactly the horizontal boundary on the generic fibre. The preimage of U avoids that boundary; no boundary coordinate evaluated below is zero at an analytic point over U.

No strictly semistable or reduced-fibre conclusion is made. Temkin's separate semistability theorem allowing a finite DVR extension is not used.

## 4. Finite rank-deficient target planes

Identify U with its inverse image on Y. Properness of the model gives a center y=red(x) for every analytic x over U. Let
\[
 I(y)=\{\gamma:y\in B_\gamma\},\qquad s=|I(y)|.
\]
At least one member is vertical, since y lies in the special fibre. Actual strict SNC gives
\[
                      1\le s\le\dim\mathcal O_{\mathcal Y,y}\le n+1.
                                                        \tag{4.1}
\]
Choose local component equations t_gamma at y. They are part of a regular parameter system. Their values beta_gamma=v_x(t_gamma) are finite and positive. A local-ring unit has value zero because it and its inverse belong to the valuation ring of the center.

The divisor identities (3.1) therefore give EXACT numerical identities at EVERY such source point:
\[
              F(x)=M_I\beta,\qquad N_I\beta=\ell,\qquad \beta>0,
                                                        \tag{4.2}
\]
where M_I=(m_{i,gamma}) and N_I=(N_gamma). No ordinary-neighborhood constancy of an arbitrary model unit is being inferred here; this is its value at its actual center.

For each subset I which can occur, define the affine subspace
\[
             H_I=M_I\{\beta\in\mathbf R^I:N_I\beta=\ell\}.
                                                        \tag{4.3}
\]
There are finitely many such I because the boundary has finitely many components. We may harmlessly include all subsets with nonempty intersection and a vertical member. Put
\[
                    E=\bigcup_{\dim H_I<n}H_I.
                                                        \tag{4.4}
\]
Each member in this finite union is closed and has dimension less than n.

If F(x) is outside E, (4.2) forces dim(H_I)=n. But
\[
               \dim H_I\le s-1\le n.
\]
Thus s=n+1, all inequalities in (4.1) are equalities, and y is a closed maximal boundary stratum point p. Its residue field is a finite extension of k. Moreover M_I is injective on the direction space ker(N_I), since that space has dimension n and its image has dimension n.

This direct rank count supplies the missing link between monomial divisor data and source cells; it does not cite a converse to faithful tropicalization.

On a compact F-injective n-cell C, the inverse image of each affine subspace of dimension less than n is a compact PL subset of dimension less than n. Adding the cell boundary gives exactly Z_C in (1.1). No n-dimensional affine F-image can lie in a finite union of those lower-dimensional subspaces. Hence C minus Z_C is relatively open and dense.

The exceptional set is finite-PL on each fixed cell. It is not the set of all Q-dependent values, which is generally countable and dense; independence is used only for the additional monomial characterization in Section 6.

## 5. Actual source patch and the full-rank coordinate relation

Fix x in C minus Z_C and its closed maximal stratum p. Reorder its n+1 boundary equations as t_0,...,t_n with N_0>0. Let D_p be the ordinary p-tube, punctured at every horizontal parameter's zero locus. Every vertical parameter is already nonzero because pi is nonzero. Set
\[
             q=(v(t_1),\ldots,v(t_n)),\qquad
             v(t_0)=\frac{\ell-\sum_{j=1}^nN_jq_j}{N_0}.
                                                        \tag{5.1}
\]
These are actual analytic unit coordinates on the punctured tube. The standard completion-to-tube description makes it the formal-unit multiplicity domain if desired, but finite projection or a choice of an analytic sheet is not needed here.

At p, f_i equals a local model unit times the indicated powers of t_j. That model unit and its inverse are bounded by one at EVERY point reducing to p. Hence (5.1) gives, on the ENTIRE D_p,
\[
 F_i=\frac{m_{i,0}}{N_0}\ell+
       \sum_{j=1}^n
       \left(m_{i,j}-\frac{m_{i,0}N_j}{N_0}\right)q_j.
                                                        \tag{5.2}
\]
This is (1.2). Its linear matrix A_p has rank n by the injectivity on ker(N_I) established in Section 4. The punctured tube is in the algebraic unit-open preimage; one may in any case restrict to its ordinary intersection with W for the source statement.

For an injective affine map A_p, a tropical map q and A_pq+b_p have the same local tropical dimension on every ordinary subdomain. Thus (1.3) follows from the definition of the maximal-variation source set; the concatenation is another injective affine image of q. This is also the precise invariance stated in CLD Lemma 12.9.2(a).

The p-tube is ordinary open, so x has an ordinary neighborhood O inside W intersect D_p. Its trace on C is relatively open and n-dimensional. Since A_p has a linear left inverse, q on that trace is affine in F and injective. Choose a sufficiently small compact n-polytope inside that trace. It is a genuine common source cell patch for the original rational moment and the adapted coordinate moment, not merely two polyhedra having the same target image.

If fixed coefficient-constant presentations are later imposed, refine or remove their lower-dimensional source boundaries on this patch as in the generic common-moment argument. No G-open cover has been promoted to an ordinary open cover.

## 6. Dense independent normal points and the monomial rule

On the n-dimensional affine image of such a patch choose n of the F coordinates whose linear parts are independent. Their values range over an open subset of R^n. The points at which those n values together with ell are Q-linearly independent are dense: the excluded set is a countable union of proper affine hyperplanes.

For a maximal-stratum patch, the map
\[
        \beta\longmapsto
        (N_I\beta,\ F_{i_1}(\beta),\ldots,F_{i_n}(\beta))
\]
is an invertible rational matrix. Therefore at the chosen dense points the n+1 positive normal values beta_0,...,beta_n are Q-linearly independent.

Here is a direct valuation characterization at such a point, avoiding an unsupported skeleton-existence theorem. In A=O_mathcalY,p, let m=(t_0,...,t_n). For nonzero a in A, d=ord_m(a) is finite by Krull intersection. Choose M>d with
\[
                        M\min\beta>d\max\beta.
\]
The regular associated graded ring gives a finite exact expansion
\[
 a=\sum_{|\nu|<M}c_\nu t^\nu+\sum_{|\nu|=M}b_\nu t^\nu,
\]
with each retained c_nu zero or a unit lift of a residue coefficient and b_nu in A. There is a nonzero degree-d retained term. All retained nonzero values are distinct by independence, and the tail lies strictly above the least one. Hence
\[
                   v_x(a)=\min_{c_\nu\ne0}\nu\cdot\beta.
                                                        \tag{6.1}
\]
It is finite. This formula uniquely determines the valuation on A and its fraction field, from the prescribed beta. It also proves generic algebraic support. Thus the dense points really are model-monomial valuations in this explicit finite-leading-term sense.

This characterization does not claim that every dependent point of the coordinate source skeleton is an ordinary covering sheet, or that all analytifications admit this adapted model without the specified resolution hypothesis.

## 7. What the capture result gives under R, and what remains

Assume the source-cell representation R explicitly for a positive separately closed ordinary (0,0)-current on W, including arbitrary smooth compact source multipliers and no residual lower-cell term. This is a separate premise, not proved here.

On the actual ordinary patch from Section 5, concatenate the rational moment and the model coordinate moment. Both projections have rank n; indeed (5.2) holds on the entire ordinary domain. The already established generic common-moment comparison, or its direct determinant calculation, identifies their normalized source coefficients on a smaller common top patch. The same absolute determinant relates arbitrary-current and canonical coefficients, so their ratio agrees.

The source cutoff in this comparison is compact INSIDE W intersect D_p. CLD's ordinary smooth cutoffs provide it. No claim that the entire D_p lies in W is needed for this representation comparison.

This removes a specific artificial capture premise: after rational replacement and residue-characteristic-zero boundary resolution, one does not need to assume separately that a full-dimensional rational-moment cell has any adapted full-rank source-coordinate patch. Sections 4-5 supply such patches outside a finite lower-dimensional exception.

The following further tasks remain distinct:

- Knowing the coefficient on a source patch is not the same as computing its value. A whole-domain L coefficient cannot automatically be applied to a current defined only on W intersect D_p.
- Closedness comparisons along residual curves require their own compact-source support or target-open localization. The rank argument does not extend a current or supply a whole residual-curve tube inside W.
- Constants assigned to different coordinate patches need not be declared equal merely because X or W is connected. An actual incidence/continuation argument and source coverage are still needed for one common c.
- This does not capture arbitrary analytic charts over a field or analytic space outside the algebraic, original-DVR, residue-characteristic-zero existence scope.
- No rank-drop cell is discarded merely by calling it lower-dimensional. The bad sets here are the explicitly constructed target subspaces of dimension less than n for one FIXED adapted rational moment. Adjoining unrelated units changes the moment and may require a new adapted model.

Consequently neither T=c delta_X nor full P21.3 follows from this note alone.

## 8. Provenance and verification status

Root requested an independent investigation of the capture interface but did not supply the finite affine-subspace rank argument. The present author also authored the earlier rational-norm/model-adaptation diagnostic and generic common-moment note; these related contributions are disclosed, not described as independent acceptance of this new argument.

The finite affine-rank/source argument is proved here. The model-existence and source-definition ingredients are primary-source results, not priority claims. A future independent reviewer should check preservation of U, all-source identities (4.2) and (5.2), and the finite lower-cell dimension argument separately from any later coefficient-synthesis theorem.

The packet is research-only. No frozen packet, live chapter, inventory, git state, or production endpoint was changed.
