# Independent exact-byte audit: strictly semistable wall residual functional

Date: 2026-08-31. Reviewer: /root/p081_weighted_repair_fresh.

## Verdict and limits

PASS for the full stated model-specific geometric/current theorem: on the tube of the chosen proper residual curve in the actual strictly semistable DVR model, the displayed coefficients exist, are coordinate independent, annihilate every principal divisor, and equal c[κ(p):k] for one c>=0. No substantive mathematical gap or required correction was found.

The proof of that divisor-functional theorem does not use representation premise (R). Its final interpretation as ratios of represented source-cell coefficients is conditional on (R). Transport to other moments additionally needs the stated actual common-source comparison. Neither those hypotheses for every moment nor arbitrary-wall realization/all-cell accessibility is proved. This is not a proof of full P21.3, a general SNC/nonreduced-model theorem, a production verdict, or integration authorization.

No candidate, earlier packet, previous audit, live chapter, inventory, git state, or production record was edited.

## 1. Exact object and independence

The reviewed candidate is the sibling directory p213_general_snc_wall_residual_functional_research_20260831.

- RESEARCH_NOTE.md: 24822 bytes; SHA-256 1c8011863516d8bdc900b3432b270c923126ee36d6600d915f714dc016553ae7.
- OBSTRUCTIONS_AND_SOURCE_COMPARISON.md: 12579 bytes; SHA-256 a101573735710ab80d881dd29750b7fa777265c9926f35c50929c3d866b7dc72.
- SOURCE_AND_INPUTS.md: 7290 bytes; SHA-256 05b06d9ad8b132b5e915314b0f5a47c334f5e6e621b786f7515c4594138c0867.
- VALIDATION.json: 7734 bytes; SHA-256 d7e72c6b6fbad1ed6293718fd84aaf02d85ce41eb007e2d680bf2cd93460251d.
- MANIFEST.json: SHA-256 2ee5bb8478d7f4cd04b1632af51028c90023cc18323e9db5c8f67deea25d36b8.
- SHA256SUMS: SHA-256 6d218ef106058a0b0b686612fcf923c969be81a5349d6f87dbdc8695482c38c5.

All three mathematical/source Markdown files were read completely. The author confirmed the freeze before this exact-byte verdict. The independent checker matches all six announced pins, all 15 manifest entries, all 16 checksum entries, and all 14 embedded validation records (11 inputs and three outputs). Prior audit files among those inputs were checked for preservation, not treated as proof of the new result.

The candidate author is /root/p213_skeletal_hostile. The candidate discloses root's pre-draft advice on actual Cartier generators and the chosen connected component. I did not author this argument, supply a replacement proof, or revise it. I authored the earlier torsor audit and recently audited representation/common-moment packets; that prior involvement is disclosed, not used to turn the present conditional interfaces into assumptions of universal applicability. This review rechecks the new completed-ring, deformation, support, and current arguments directly.

## 2. The actual original-field geometry

RESEARCH_NOTE Sections 2 and 3.1, lines 16-105, retain the necessary scope: complete DVR, perfect residue field, actual integral proper regular strictly semistable model, relative dimension n>=2, and one connected component C of an intersection of n distinct components.

The intersection is smooth of dimension one. A connected smooth curve is integral here: regular irreducible components cannot meet, and the finite disjoint decomposition into them would otherwise disconnect C. Properness is inherited from the model. This does not imply geometric connectedness, which is correctly not assumed.

The tube of a closed special-fibre subset is ordinary open by reduction anticontinuity. The finite-ideal strict norm description is compatible with that fact, but does not declare generic fibres of formal Zariski opens to be ordinary opens. The continuous functions U_j are globally well-defined by the component formal metrics, are nonnegative, and sum to ell because the special fibre is reduced. They are used only as continuous functions.

Let D be the whole selected intersection. The tubes of C and D\C form a disjoint ordinary-open partition of the D-tube. Thus restricting the closed set {all selected U_i>=a} of compact X to the C-tube yields a compact K_a inside X_C. This is a valid clopen restriction of a compact set already contained in the D-tube. It does not silently equate X_C with the full positive-radius locus.

Goodness and absence of analytic boundary hold for this ordinary open in the analytification of the smooth proper generic fibre. The current lives throughout on X_C, not on an invented sliced curve.

## 3. Completed p-tubes and coefficient fields

Section 3.2, lines 107-117, justifies an actual analytic tube, not only a skeleton model.

Perfectness makes κ(p)/k finite separable. Finite étale lifting over the henselian DVR supplies R_p/R, of rank d_p=[κ(p):k]. A residue-compatible embedding into the completed local ring follows by the simple-root form of Hensel lifting. A local étale map with the same residue field has isomorphic completed local rings; completing the standard chart after the coefficient extension consequently gives (2.1). These algebraic facts were checked against Stacks Tags 04GK and 0AGX, with exact scope recorded in SOURCE_LEDGER.md.

The selected normal x_i are algebraic local equations in O_{𝒳,p} before completion. This point is needed later when z_i/x_i is an element of the localization at η_C. At e_p=0 the remaining curve parameter may be centered after adjoining the residue lift; it need not have belonged to the original algebraic local ring. At e_p=1 all n+1 component parameters occur, and the relation is x_0...x_{n-1}w=π.

The complete-ring isomorphism and its inverse converge on the smaller closed domains with every parameter norm <1. They give the actual p-tube isomorphism upon exhaustion. Eliminating x_0, and removing w=0 only when e_p=0, gives exactly Q_p. In particular the e_p=1 inequality includes s:
sum u_i+s<ell.
No use is made of the rectangular e_p=0 domain in that case.

A compact subset of Q_p has compact inverse image: the coordinate values are bounded away from all missing faces, and its inverse image is a closed subset of a compact closed polyannulus. This supplies compact source support for every target test and every derivative primitive in Section 4.

There is one K_p-domain regarded as K-analytic. It is not d_p ordinary-open sheets. No pullback of an arbitrary K-current to a different coefficient field is performed.

## 4. Existence and coordinate independence of b_T(p)

Section 4, lines 119-142, is a valid direct scalar-distribution argument.

For h>=0 the pulled-back interleaved top form is positive. A nonnegative compact target cutoff equal to one near a fixed compact set gives a sup-norm bound on the resulting positive distribution. Its representing measure is locally finite. Deleting one d' coordinate factor supplies a compact (n-1,n)-test; applying d'T=0 proves that every distributional coordinate derivative is zero. Local convolution gives constant distributions on target balls; overlapping balls and convex connected Q_p yield one finite b_T(p)>=0.

This uses ordinary test forms in the actual source, not restrictions of T to fibres, an assumption about its order on every chart, or (R). The compactness check also gives continuity in the usual compact-test topology. CLD7.1.11 is the abstract tropical-space pushforward formalism; in this application the moment supplies the relevant pullback, and properness is proved rather than inferred from that citation.

Equations for the same component differ by a completed unit of norm one, so all U_i coincide as actual functions. For e_p=0 a second curve parameter differs by a unit linear w-term, higher w-terms, and terms in the normal ideal. On a common collar with all U_i>ε and 0<s<δ<ε the linear term strictly dominates. The logarithmic parameters therefore coincide on an ordinary open collar, sufficient to compare integral-one tests. For e_p=1 the two additional-component equations differ by a unit everywhere.

Changing the omitted normal coordinate is an affine transformation with absolute determinant one, including the term -e_p s. Both the interleaved top form and Lebesgue normalization are preserved. This establishes the stated coordinate independence without a global normal-coordinate assumption.

## 5. Cartier generators and domination chronology

Sections 5 and 6, lines 144-220, make the correct stronger choice: z_i generates the Cartier ideal of E_i at η_C. Thus z_i/x_i is a local-ring unit with nonzero residue in k(C). Prescribing just the component valuation vector would not suffice; the supplied x_i(x_i+x_j) diagnostic verifies this.

The lift F of f is also a unit of O_{𝒳,η_C}. Both its numerator and denominator, and those of z_i/x_i, can be chosen in O_{𝒳,p} outside the prime defining C. Their reductions in the completed curve ring κ(p)[[w]] remain nonzero. The bad set is finite because each divisor-support difference avoids η_C and has zero-dimensional intersection with the proper curve. Zero-order bad points are correctly retained.

The proof first imposes W_ε={all selected U_i>ε}. Modulo the normal ideal a numerator has form w^r times a unit. Lifting this expression leaves a sum of x_i A_i with bounded coefficients, of norm at most exp(-ε); its leading term has norm exp(-rs). Choosing rδ<ε therefore proves exact dominance throughout the ordinary collar. Applying this to the finitely many numerators and denominators proves
r_i=U_i+n_{i,p}s and t=m_p s
there as identities of actual functions.

Only after that conclusion does the proof choose the compact r-support and derive stronger U-bounds. Thus it does not bootstrap the hypotheses of its own leading-term argument from an unproved rational-coordinate bound. It handles nonlinear deformation terms; it does not assert that they vanish formally.

The n_{i,p} record a rational trivialization of a normal line bundle. No degree-zero relation is imposed on their divisor.

## 6. Ordinary cutoff gluing and entire-source compactness

Section 7, lines 222-269, supplies the crucial source support, including at points reducing to η_C.

Inside W_ε, the closure of the support of 1-η_p lies in {all selected U_i>=ε, s>=a_p}. In the actual p-coordinates this is compact inside the p-tube: for e_p=0 it is a closed normal polyannulus times the closed w-disc; for e_p=1 the relation also gives lower coordinate norms. The strict bound s>=a_p keeps it away from the outer w-boundary. Therefore extension by zero across the complement of that p-tube is ordinary smooth on W_ε. The finite sum over disjoint bad tubes gives the claimed global η.

The closure used for this gluing need not be compact inside W_ε itself; it suffices that it stays in the p-tube at any prospective boundary point within W_ε. The subsequent radial support estimate supplies compactness inside W_ε for the actual primitive. The frozen proof makes both checks, in this order.

The exact outer-collar identities exclude zeros and poles there. Away from bad tubes the functions are formal units; all remaining zeros/poles in W_ε lie where η is zero on a neighborhood. Hence zero-extension across their divisors is smooth.

The inequalities (7.1) and supp(φ)⊂Δ_{4ε} imply U_i>3ε for every selected i, including
U_0=ell-sum r_i+(sum n_{i,p}-e_p)s>3ε.
Thus the closure of the support of ηφ(r) lies in compact K_{3ε}, strictly inside W_ε. The e_p term is essential and is present. Global U_i are never differentiated.

## 7. Exact form cancellation, including zero-order bad points

In Section 8, lines 271-315, ηβ is a legitimate compact ordinary (n-1,n)-test on X_C.

On a transition collar with m_p!=0, |t|>=|m_p|a_p>h makes χ(t) vanish. If m_p=0, t is identically zero on the entire ordinary collar, making d''t=0. These prove d'η wedge β=0 as a source form before pairing with T. They include points with zero F-order but nonzero normal twisting.

Since r_i and t are logarithms of analytic units on the complement of the removed divisor, their d'd'' derivatives vanish. The derivative of φ repeats one d'r_i. Moving d't past Ω_r introduces no sign because Ω_r has even total degree. This gives (8.3).

Outside the contributing bad collars, χ'(t) vanishes on an ordinary neighborhood: at a point with t=0 this follows from continuity of t and the interval on which χ' is zero, not from a false assertion that the reduction fibre of η_C is open. On every contributing collar, χ' vanishes near s=0 and is supported below h/|m_p|<a_p, where η=1. Together with the normal bounds this gives a finite decomposition into compact top forms inside actual p-tubes. No current-support or measure-zero substitute is needed for any error term.

## 8. Determinants, simplex slices, and both signs

Section 9, lines 317-361, has the correct all-dimensional calculation. The shear (u,s)->(u+n_p s,s) has determinant one. Substituting t=m_p s gives two factors of m_p, hence m_p^2; terms repeating d's or d''s vanish. The result is (9.2), with no additional normal-bundle or lattice factor.

For each s on the derivative support, translation of supp(φ) lies entirely inside the actual Q_p slice and W_ε by (7.1). This verifies the integral-one assertion (9.3), including when e_p=1. There is no lost simplex-boundary portion.

For m_p of either sign, direct integration gives
m_p^2 ∫_0^{δ_p} χ'(m_p s) ds
= m_p(χ(m_p δ_p)-χ(0))=-m_p.
Consequently closedness of the original current yields (2.4). The proof neither slices T nor treats a canonical-calibration identity as an identity for unknown weights.

## 9. Degree factorization without geometric connectedness

The Section 10 argument is valid over k, not only over the constant field of a geometrically connected curve. With degree measured over k,
χ(O_C(H+jD))=deg_k(H)+χ(O_C)
for deg_k D=0. Choosing H effective of sufficiently large degree makes this positive for every integer j, so H+jD has a nonzero section and is linearly equivalent to an effective divisor. Positivity of λ_T then forces λ_T(D)=0 by allowing both signs of j.

Applying this to d_q p-d_p q gives b_T(p)/d_p independent of p. No degree-one closed point or divisor is assumed. The source scope was checked directly in Stacks Section33.44, including its constant-field caveat; see SOURCE_LEDGER.md.

Finiteness here means finite values on finite-support divisors. It is not finite total mass over the infinite set of all closed points.

## 10. Canonical coefficient and conditional interpretation

For the primitive K_p-polyannulus the standard-coordinate canonical calibration is one. CLD14.4.3 multiplies it by the full finite degree when that same analytic space is viewed over K. Since R_p/R is unramified, [K_p:K]=d_p; the determinant-one shears add no factor. Hence b_{δ_{X_C}}(p)=d_p exactly.

At e_p=1 the displayed source Gauss n-cell is the interior of the adjacent canonical n-simplex. At e_p=0 the extra curve parameter exposes further n-dimensional Gauss cells absent from the unmarked model skeleton. The argument properly uses both kinds for arbitrary residual principal divisors.

Assuming (R) identifies the tested constants with represented coefficients on these displayed cells. It does not identify all cells of an arbitrary moment with them. The requirement for genuine common analytic moments and isolatable identical source patches is explicitly retained. This audit does not replace that boundary by an earlier independent pass for another packet.

## 11. Obstructions and source comparisons

The companion's three concrete diagnostics check out.

1. The Legendre discriminant is a unit on the specified B, and smooth pullback gives the claimed strictly semistable relative surface. Properness over B gives compact closed radial strips. The logarithmic derivative j'/j at λ=3 is 15/7-2/3-1=10/21, so the family is not a fixed elliptic product over the displayed annular base. The note expressly does not assert this particular model is proper over R or rule out unrelated presentations.
2. x_i(x_i+x_j) keeps the generic selected component orders while its quotient by x_i has zero residual value at η_C. This demonstrates the real distinction between the generator and component-order conditions.
3. The actual punctured-P1 moment has four primitive directions (±1,0),(0,±1); balancing permits (A,A,B,B). This is only a nonuniqueness diagnostic for one moment's constraints, not a constructed positive closed current.

The GRW comparison retains the algebraically closed source scope, proper residual curve, corrected alpha terms, possible negative alpha values, and nonintegral higher-dimensional slopes. Its principal-divisor intersection proof computes canonical degrees, not arbitrary T-weighted sums. The frozen candidate does not import that stronger conclusion.

The CLD14.6.2 and 14.7.2 comparisons also correctly retain their full stated hypotheses and canonical conclusions. In particular, neither is a theorem restricting T to a residue curve, identifying the analytic neighborhood with a product, or transporting unknown coefficients through fibres.

## 12. Presentation and verification notes

No mandatory mathematical correction is requested. Two harmless points should remain explicit during eventual typesetting:

- Ω_q in q_p^*(hΩ_q) denotes the coordinate volume form on Q_p before pullback; the same symbols then denote pulled-back coordinate differentials. This is conventional but worth saying once.
- Despite the directory name, the theorem assumes a reduced strictly semistable DVR model. It must not be relabelled as a theorem for arbitrary nonreduced SNC models, non-discrete fields, or arbitrary analytic walls.

The PDF skill was used only to inspect primary source pages. All twelve rendered full pages were viewed; their equations and hypotheses were legible. Two successful rendering calls emitted font-cache warnings; no permission or cache workaround was used. The source PDFs were unchanged, and no PDF artifact or TeX compile was made. Exact rendering evidence and temporary-image hashes are in SOURCE_VISUAL_QA.json.

The independent byte checks are reproducible with verify.mjs. The attached machine checks establish identity and preservation, not mathematical validity; the mathematical reasoning above is the basis of the scoped verdict. Production verification and any live integration gate remain unresolved and unchanged.

