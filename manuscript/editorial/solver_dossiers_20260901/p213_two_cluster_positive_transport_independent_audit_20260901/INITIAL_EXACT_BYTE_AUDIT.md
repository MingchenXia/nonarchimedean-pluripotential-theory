# Independent full-proof audit: two-cluster transport, original frozen version

Date: 1 September 2026. Reviewer: /root/p213_skeletal_hostile.
Status of the ORIGINAL frozen note: CORRECTION REQUIRED at Section 8. The other parts of the full conditional argument have been checked without finding another substantive gap. This is not a production/Rethlas verdict, and is not a conclusion about full P21.3.

## 1. Independence, exact target, and verdict

The candidate was authored by /root/p082_independent_reaudit; root requested the finite example and raised its all-torus-radii domain requirement. The reviewer did not author this proof, its explicit model chain, or its positive-transport assertion. The reviewer has authored other residual-functional and point-retaining packets and has reviewed related inputs. Those historical contributions are disclosed, not treated as fresh independent certification of any premise here. In particular L, O, Q and the displayed R identity remain explicit inputs.

Reviewed in full: RESEARCH_NOTE.md, SOURCE_LEDGER.md, VALIDATION.md, and the read-only check_packet.mjs. The accompanying manifests and exact input identities are independently checked by the separate audit script, not accepted merely from the author's validation.

Original principal note:

- Path: ../p213_two_cluster_positive_transport_research_20260901/RESEARCH_NOTE.md
- Bytes: 32047.
- SHA256: 292087eb0b34072f15f7bb2426e8adf27fe03858aa85f30107538adf0962e4bf.
- Original manifest SHA256: 0bda4e908fa42e8b683ef96fbe61ae34298482829d77fae645adab157dab717b.
- Original checksum-file SHA256: 162116e70eb80c6f4f844e5e7a826f39b15e29116e0546215db8c81aa3c95e4d.

The required correction is precise: Section 8, original line 362, follows its assertion that d''t=0 on the ordinary shallow collar at the order-zero bad point ζ=1 with “Away from the bad tubes the same identity holds.” If “same identity” means d''t=0, it asserts too much. At the residual generic-centre/Gauss point, t=v(ζ)=0 does not make t constant on an ordinary neighbourhood. Every such neighbourhood has points in the shallow 0/∞ branches where t varies. The proof must use t=0 and therefore χ'(t)=0 near each such point, not vanishing of the differential germ.

This is a necessary proof-wording correction, not a counterexample to the stated transport theorem. Its repair does not require changing the model construction or the compact primitive: χ is already constant near zero, and t is continuous on the ordinary unit locus. The correctly stated order-zero TRANSITION-collar assertion is valid. Section 5's shorter “Off the bad tubes t=0” is a pointwise statement and is not itself false; an explicit distinction there is useful for the same reason.

No original frozen file was altered. A preserved revision must be read and checked separately before an exact-byte conditional PASS is assigned. A separate revision addendum, if present, does not retroactively change this original verdict.

## 2. Scope actually established, conditionally

The base is exactly K=C((π)), R=C[[π]], n>=2, d=n−1, ell=v(π)>0. The current T is positive and separately d'- and d''-closed of bidegree (0,0), defined ONLY on

    W = (A1_K \ {0,π,1,1+π}) ×_K Gm_K^d, analytified.

This is the analytic fibre product; no Cartesian-product description of all analytic points is assumed.

For c=0,1 the four entire source domains are D_c^-:0<v(z−c)<ell and D_c^+:v(z−c)>ell. The coordinate moments are q_c^-=(u,v(z−c)) and q_c^+=(u,v((z−c)/π)), with all u in R^d. Conditional on L/O/Q and the displayed R on the specified actual domains, the proof identifies one finite nonnegative coefficient for these four coordinate families. The permitted source-multiplier tests are arbitrary compact ordinary smooth multipliers times coordinate target top forms. It also applies to H tests on all four families and F tests on the two plus families by actual full-source affine identities.

It does NOT cover pole branches near π and 1+π, the outward H branch |z|>1, arbitrary additional moments, all ordinary top forms, or the whole current on W. The minus families are genuinely rank-collapsed for F. Neither continuity of an unknown coefficient across a lower-dimensional face nor general common-constant propagation is used. No open problem is retired.

All closed points used in the three principal divisors are k-rational. All omitted special-fibre multiplicities and all local finite degrees in this particular construction are one. Accordingly there is no hidden residue-degree factor: the canonical coefficient in the actual q coordinates is 1.

## 3. Exact input interfaces and no circular enlargement

L is the finite-projection note with SHA256 3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a. Its positive slice allows ALL retained exponents a_j=0, with m=1 and epsilon=1; this degenerate weighted inequality is crucial for Section 3. It gives actual full-tube properness and canonical degree. It does not license selecting only a Gauss section.

Q is the proper target-open comparison note with SHA256 35d4ae59a167025ef595aa50a45101619ed1aef586be39abebca1486c62857ec. The proof uses T restricted to the FULL inverse image of a connected ordinary target open. Compact target primitives then pull back compactly in the current's actual domain. Its extra conclusion under displayed R identifies individual coordinate source coefficients, not merely their pushforward sum.

O is the ordinary-open outer-collar note with SHA256 f629a77106d023763c7b99626c1ec1f8f449164f3749de475bf18bb0661e1d5b. Here it is an explicit premise, including its compact-support construction, at each of three independently chosen normal Gauss points. The candidate checks actual proper regular models, all selected components vertical, entire proper residual curves, positive independent normal weights, and W as an ordinary neighbourhood. It does NOT apply an older whole-tube current theorem to T on W. O's pointwise/ordinary-open distinction is itself explicit in its Sections 7–8 and is precisely the distinction required in Section 1 above.

R means ONLY eq:p213-source-cell-formula in statement SHA256 5c06cd6f091e5964a16c07b3efddd2104fed938447605f4f9b19ff8dfea01f1a. Its source multipliers, local finiteness, convenient constant coefficients and absence of a lower-cell residual term are assumed for the coordinate moments used in the construction, F, H and restrictions. The associated proof hash is provenance, not an input theorem established in this audit. No stronger local-affine-separation assertion is certified.

The old two-cluster diagnostic is motivation, not a theorem proving a positive transport edge. Its independent diagnostic PASS cannot be promoted to a PASS of this new proof.

## 4. Section 3: all torus radii, actual positive slices, and compact nesting

The all-u step is valid, rather than an informal appeal to exhaustion. With residual variable ζ and t=v(ζ) in I=(0,ell) or (0,infinity), set T_i=π^N t_i, U_i=u_i+N ell. The domain D_N has u_i>−N ell and t in I. It is the actual L domain with x=π, all T_i and ζ nonzero of norm <1, restricted over Omega=R_{>0}^d×I. The equation is x=π: m=1, epsilon=1 and every a_j=0. In particular the special-fibre equation imposes no unintended upper bound on the sum of U_i. Omega is connected and is contained in the exact positive slice allowed by L.

The four removed z-points do not remove any further source point from these polyannuli. For minus annuli |π|<|z−c|<1; for plus annuli 0<|z−c|<|π|. Strong triangle inequalities keep the pole at c+π and the other cluster outside. The torus coordinates never vanish.

Q therefore supplies b_N and its coordinate source interpretation. D_N is contained in D_{N+1}, and q_{N+1}=q_N+(ell,...,ell,0). Translate one compactly supported target function of integral one. Its two pullbacks have the SAME full source support: any point meeting the translated support has q_N in the old positive target support and thus already lies in D_N. Properness makes that support compact. A smooth ordinary cutoff equal to one near it can be supported in D_N. Evaluating the identical actual compact form in both domains proves b_N=b_{N+1}; it is not a comparison of unrelated target integrals.

Every compact source support in the full domain has all u_i bounded below, so it is contained in some D_N. The arbitrary compact-source multiplier identity from Q then proves the full-domain identity. The same argument also proves properness of the full q over any compact target subset: choose N for that subset, and its full inverse image is the same compact L inverse image.

Thus b_c^± is independent of all torus radii and all permitted residual radii in its domain. This is the step that allows a later single small collar to identify the entire family.

The F/H table is valid on the ENTIRE domains by strict dominance. H has rank n on all four coordinate families, and F has rank n only on the plus ones. Pulling a target form back through these actual affine maps is legitimate on ordinary source domains; it is not merely an equality along a skeleton. Both current and canonical coefficients transform together, so the normalized ratios agree. No conclusion is drawn for F top cells inside its rank-(n−1) minus domains.

## 5. Section 4: the central proper model and generic-centre point

The model Y starts from (P1_R)^d and uses the actual closed connected component of each regular codimension-two vertical/horizontal intersection. The relevant t_i-pivot chart successively gives

    π = x0 t2 ... tn.

The other affine Rees chart is also part of the blowup. For two regular SNC parameters a,b, the chart A[b/a] has the expected regular coordinate replacement; the two charts preserve SNC support. The new exceptional multiplicity is the sum 1+0=1. These are blowups supported in the special fibre, hence actual generic-fibre isomorphisms, not finite covers or an asserted ordinary étale-sheet decomposition.

At the tracked rational point of Y the n selected vertical parameters are x0,t2,...,tn. Their intersection is a regular zero-dimensional stratum; its connected component is the entire rational point. Taking P1_R×_R Y=P1_Y gives a proper regular model of X with the whole residual curve C_cen=P1_k over that point. Regularity follows from smoothness over the REGULAR scheme Y, not from an unsupported claim that Y is smooth over R.

The source-domain check is reversible: if all u_i>0 and sum u_i<ell, each successive quotient π/(product of a subset of the t_i) has positive valuation. Hence every such original torus point enters the tracked chart and reduces to the specified point, not merely the visibly monomial points.

Choose ell,u_2*,...,u_n* Q-linearly independent with positive u_i* and sum u_i*<ell. Then alpha_0=ell−sum u_i* and alpha_i=u_i* form a positive Q-independent normal vector, by the invertible integral change of variables. The z unit Gauss norm together with the relative torus Gauss norm defines an actual analytic point centered at eta_Ccen. A nonzero residual rational function in z has value zero there; the normal parameters have the prescribed positive weights. This point lies in W. Thus O's centre, independence and neighbourhood hypotheses are met without claiming that ordinary-open tubes come from a formal Zariski cover.

## 6. Section 5: central transport and the first compact primitive

On C_cen=P1_k, the residual function z/(z−1) has divisor [0]−[1], with both degrees one. The retained normal rational functions t_i have no additional residual orders here.

At 0 use w=z; at 1 use w=z−1. In both collars q=(u,s), and the omitted normal radius is ell−sum u_i. A small common compact normal box inside the simplex and a shallow interval s in (0,delta), delta<ell, supply full source domains inside D_0^- and D_1^-.

There is no extraneous source on the old-polyannulus side of the comparison: the normal inequalities force the same tracked torus-model point, and |z−c|<1 forces the correct residual point c. Consequently the full pullbacks of a compact target top form agree, not just their restrictions to an embedded collar section. Their support is compact in W by the actual L/Q properness. An ordinary source multiplier can be chosen equal to one on the same support. This identifies the O coefficients with b_0^- and b_1^-.

The bad point infinity is kept. On its ordinary shallow collar z/(z−1) is an analytic unit of norm one, so its logarithm has zero differential there. The deep missing point at infinity is removed by eta, not assumed to lie in W. Elsewhere outside the finite bad tubes the logarithm is zero as a value, and χ'(t)=0 near each such point.

For clarity, the actual primitive is
    beta=phi(u) chi(t) (wedge_i d'u_i wedge d''u_i) wedge d''t,
where t=v(z/(z−1)). O supplies the finite bad-tube cutoff eta and the full support budgets. The resulting eta beta is a compact ordinary (n−1,n)-form supported in W. If an order is nonzero, chi vanishes on the eta transition; for an order-zero bad tube d''t vanishes on that ordinary transition collar. Derivatives of phi wedge to zero, and the logarithms of analytic units are pluriharmonic.

At the two contributing points t=m s with m=1 and −1. Each differential block contributes m, whereas the one-dimensional change of integration variable has its signed endpoint. Explicitly, for either sign,
    integral_0^infinity m^2 chi'(m s) ds = −m.
The even total degree of the paired normal form introduces no additional sign. Closedness yields 0=−lambda(0)+lambda(1), hence b_0^-=b_1^-.

No derivative of a zero-extended CURRENT, no slicing, and no boundaryless-tube extension of T is used. It is the test form whose compact support is constructed inside W.

## 7. Section 6: n global blowups and an entire P1 at every step

For each c separately, add the global horizontal divisor z=c and use pivots t2,...,tn,x0, with x0 LAST. At a step blow up the connected component of V_pivot intersect H_w through the tracked point, and use the vertical-pivot chart w_old=x_pivot w_new. The selected vertical component is replaced by the exceptional component of multiplicity one; the strict transform of the old vertical is an extra component at w_new=infinity. The strict horizontal meets the new curve at w_new=0.

The entire-curve argument does not follow merely from the displayed affine chart. The centre is a regular codimension-two closed stratum. Its exceptional divisor is the projectivized conormal bundle, a P1-bundle over the entire centre. None of the other n−1 selected divisors contains the centre: at the tracked point their parameters are independent of its two defining parameters. Thus their strict transforms equal their total pullbacks. They cut the centre at the tracked point, so on the exceptional divisor their intersection is the FULL P1 fibre over that k-rational point.

The selected n-fold intersection remains regular of dimension one. A closed entire P1 inside it is an irreducible component, and distinct irreducible components of a regular scheme do not meet. Therefore the chosen curve is an entire connected component, not an open affine line or an unproved completion of one.

At the next step the centre uses the zero point on that curve, disjoint from the preceding extra component at infinity. The entire next exceptional fibre maps to that zero point, so all earlier extra components remain disjoint from it. At the final curve only the former last pivot contributes an extra component, at infinity. Other unselected boundary components not passing through the tracked point cannot appear in its exceptional fibre. These checks explain both the full global curve and the complete extra-component list.

The n substitutions give z−c=π ζ and π=x0 product t_i. The chosen normal values are unchanged; intermediate horizontal quotients have positive valuations until the last residue variable ζ has value zero and transcendental reduction. The actual relative Gauss point consequently remains centered at the generic point of the full final P1 and lies in W. All generic maps are isomorphisms of the original X. A global product or annular-coordinate trivialization of an arbitrary formal neighbourhood is not being inferred.

## 8. Sections 7–8: omitted parameter, full inverse images, signs

At ζ=0 the retained coordinates are (u,t=vζ); the omitted selected parameter is x0, of valuation ell−sum u_i. Then s_c=ell+t, so the collar is in D_c^+.

At the last infinity chart put
    y0=(z−c)/(product t_i),  w=x0/y0=1/ζ.
The equations are
    π=y0 w product t_i,  z−c=y0 product t_i.
The SELECTED omitted parameter is now y0, not the old x0. The old component is the extra divisor w=0. Hence
    v(y0)=ell−sum u_i−s,  s=v(w)>0,  s_c=ell−s.
The correct positive target condition is sum u_i+s<ell. Omitting this s term would invalidate the support comparison. It is included in the frozen proof.

Choose a compact box B inside the normal simplex and delta<min_B(ell−sum u_i), also delta<ell and below O's shallow bounds. This supplies positive selected normal margins on the full support, with no arbitrary source restriction.

In particular the equality of the old polyannulus test with the final infinity-chart test is two-sided. Suppose an ORIGINAL source point meets its old target support, so u is in B and s_c=ell−s with sum u_i+s<ell. At each first n−1 blowup its horizontal quotient has valuation
    s_c − (sum of the pivots already divided out)>0,
since each partial sum is at most sum u_i<s_c. It therefore enters every required chart. At the last step v(y0)=s_c−sum u_i>0, and v(x0/y0)=s>0, so it enters the infinity chart. Thus there are no other source points carrying the old test outside the specified final tube. The finite-end comparison is similar, with s_c=ell+t>ell>sum u_i. This explicit reverse check is why comparison of the whole compact forms is valid.

The coordinate change (u,s_c) to (u,ell−s_c) has determinant −1, absolute determinant 1. Both differential blocks change sign, so the top superform sign is +1. In the finite chart the change is only translation of the residual valuation. All local degrees and residue degrees are one. These computations give lambda_c(0)=b_c^+ and lambda_c(infinity)=b_c^- by evaluation of the same actual compact form, with the same optional cutoff equal to one on its full support.

The order-zero point ζ=1 must not be dropped: it corresponds to the removed point z=c+π. A shallow punctured collar 0<v(ζ−1)<delta is an actual ordinary open subset of W; there |ζ|=1 and d''vζ=0. Eta vanishes before reaching ζ=1. The other cluster has distance one and does not intrude. The finite/end and infinity support inequalities keep all other removed points out.

The principal residual function ζ has divisor [0]−[infinity]. O's primitive uses the retained t_i without residual correction, so the normal form is the same in both charts. The m=+1 and −1 calculation is exactly the one in Section 6 above, and yields lambda_c(0)=lambda_c(infinity). The sole original wording correction identified in Section 1 is required when describing what happens outside the bad tubes; the correct χ' vanishing is sufficient for the proof.

## 9. Consequence and remaining boundary

Combining the three actual compact principal-divisor tests with the four already global coordinate constants gives

    b_0^+ = b_0^- = b_1^- = b_1^+ = kappa.

Finiteness follows by evaluating one nonnegative compact target function of integral one, and positivity gives kappa>=0. Only one independent normal germ on each of the three curves is needed, because Section 3 has already made each coordinate-family coefficient independent of u and depth. The proof does not smuggle in an unproved constancy of O's coefficient over arbitrary germs.

This is a genuine conditional positive transport result across the diagnosed old-moment rank drop. It is not a proof that every current coefficient in every moment on W is equal. It remains conditional on the exact L/O/Q interfaces and displayed R, restricted to the original field and four stated domains. Neither the diagnostic PASS nor this corrected conditional argument supplies full P21.3, a production verification record, or permission for live theorem integration.

## 10. Audit mechanics

The read-only verifier records exact original/revision input bytes, all manifest entries and checksum lines, the direct premise pins, historical L/O/Q/diagnostic manifests, and the exact revision inverse comparison where available. These are integrity checks, not a mathematical proof. The author's 44 arithmetic samples, even when reproducible, are only sanity checks and cannot establish arbitrary-dimensional geometry or rational independence.

No PDF was rendered or TeX compiled in this audit. Primary algebraic source pages were inspected directly; CLD text and exact predecessor interfaces were read for the stated purposes. No live manuscript, candidate, frozen predecessor or git state was changed. Only this new independent audit directory was authored.

