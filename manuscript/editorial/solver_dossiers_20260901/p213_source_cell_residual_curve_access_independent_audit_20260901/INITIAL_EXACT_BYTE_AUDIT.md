# Initial exact-byte audit: source-cell access to a residual curve

Date: 2026-09-01. Reviewer: /root/p213_skeletal_hostile. Candidate author: /root.

## Verdict on the original frozen version

REQUIRED SCOPE CORRECTION. The original frozen statement does not explicitly put Delta inside W or say that Delta is a source cell for F restricted to W. Its proof uses that hypothesis. No unconditional PASS is assigned to these original bytes.

With that intended scope made explicit, the complete new assembly has no other substantive gap found in this review, conditional on its exact geometric inputs A and B and, for the current conclusion only, O/Q/L and the displayed R representation on the actual source domains. A separate addendum is required for any corrected frozen version; this report never silently changes the original statement.

The reviewer did not author A, B or this new cell-to-curve assembly. The reviewer authored earlier point-retaining and whole-tube functional packets and separately audited Q and the mixed ordinary-local synthesis. Those authored results are not freshly self-certified here. In fact P and the mixed synthesis are not premises of this assembly. A and B are explicit geometric research premises with separate independent audits; reading their full notes and ledgers here checks their interface, not a replacement production certification.

## 1. Exact original input

Candidate directory: ../p213_source_cell_residual_curve_access_20260901.

- RESEARCH_NOTE.md: 15730 bytes; SHA256 46eba8ebccb7d87c404c184a83ae51bce9f84e2d14f636fba19212d1fe73c596.
- SOURCE_LEDGER.md: 3647 bytes; SHA256 1f9a293de8415ce7b388c19a10ef155e1a1ea70e568cc17ae9c7c4ba312f7e6c.
- freeze.mjs: 4831 bytes; SHA256 4abd6d00aeacdbfd6659764889a20c22d6302f0ba423455052a2b0cbc0aac609.
- Announced MANIFEST.json: a50514a0fce52b892f171e261ba8e9c2bcd2990cc869f1e1026ce1453091c7c2.
- Announced SHA256SUMS: 3a1a25e1988e4e12839ba3fb88c32c60133a02e04c25c996bbe6008742edf2d3.

The complete 152-line original note, source ledger, freeze script and manifest were read. The complete A and B notes and ledgers were also read. The companion machine output records the independent hash checks; it is not a mathematical proof. Line references in this report refer only to the original note, not a later revision.

## 2. Required correction and its exact effect

Lines 24-26 introduce an ordinary W inside U^an and then a compact source cell Delta for F with an arbitrary nonempty relatively open V inside its interior. They do not state Delta subset W. Yet line 74 applies B with W as an ordinary neighbourhood at a chosen point of V; lines 97 and 148 put the constructed patch in W; lines 101 onward apply O to a current given only on W.

Without the missing relationship, W could be empty or disjoint from V. The hypotheses as literally written would not supply B's neighbourhood hypothesis, and the asserted W-supported application would not follow. The current coefficient wording at line 32 suggests the intended interpretation, but does not repair the preceding pure-geometric statement.

The same-scope repair is explicit: Delta is a compact full-dimensional source cell for F restricted to W, and Delta is contained in W. Then V, its smaller compact patch, the B wall point and the whole monomial simplex all lie in the prescribed ordinary current domain. No new current extension is authorized by this repair.

The author confirmed this intent and agreed to preserve the original and prepare a separately frozen corrected version. This review did not edit candidate files.

## 3. Finite exceptional set and compact source inverse

Assuming the corrected scope, lines 49-62 apply A with all required hypotheses: original complete DVR, residue characteristic zero, smooth proper integral algebraic X, finite nonzero rational moment, common algebraic unit-open U, and an ordinary W therein. A's generic modification is an actual isomorphism over U. Thus W and its current can be identified on Y without any pullback theorem across exceptional loci.

Because F is affine-injective on an n-cell, its image has dimension n. It cannot be contained in the finite union E of lower-dimensional affine subspaces. A chosen point outside F^{-1}(E) lies in a closed maximal boundary-stratum tube where F=A_p q+b_p and A_p has rank n on the entire punctured tube.

The trace of that ordinary tube on Delta is relatively open. A sufficiently small compact n-polytope Delta_0 lies in this trace and inside V. A linear left inverse of A_p expresses q as an affine function of F on this whole trace. Therefore q is affine-injective on Delta_0 and its image is a full-dimensional compact n-polytope. The inverse sigma_C is continuous because the domain Delta_0 is compact and the target of q is Hausdorff. No faithful-tropicalization converse is assumed.

## 4. Dense independent values identify actual analytic points

This is the essential new source-to-model bridge, lines 64-72.

B supplies a continuous original-field monomial section sigma_M on the positive weighted slice at the same closed stratum p. The q-image of Delta_0 lies in its positive domain. Points z for which ell,z_1,...,z_n are rationally independent are dense in every full-dimensional subpolytope: the complement is a countable union of proper affine hyperplanes. Density holds in the whole compact polytope because its interior is dense.

The rational transformation from (ell,z) to the full normal vector beta, with beta_0=(ell-sum N_j z_j)/N_0, is invertible. Hence beta_0,...,beta_n are rationally independent at those dense values. Both sigma_C(z) and sigma_M(z) have centre p and these same values.

A's finite regular-local expansion then forces equality as analytic points, not just equality of their tropical coordinates. For a nonzero element a in the regular local ring, take its finite expansion modulo a sufficiently high power of the maximal ideal. The retained coefficients can be chosen zero or units; independence gives a unique least nonzero monomial value, while the tail has strictly larger value. This forces a finite value for a, including when generic algebraic support had not initially been known. It gives generic support and a unique valuation on the fraction field. Thus the two analytic points coincide.

Both maps are continuous into the Hausdorff Y^an. Their agreement on the dense set therefore extends to the entire q(Delta_0). The relative interior of Delta_0 really is an open patch of the model monomial cell. This does not say that all points of a full q-inverse image are monomial points.

The local regular-ring interface was checked directly against Stacks 00NN, Lemmas 10.106.1-3 and the cited Krull-intersection argument; B's separate coefficient-field and continuous-section construction remains the exact geometric input.

## 5. Nearby wall, entire-source coordinates and rank

B now applies to a relative open neighbourhood inside that actual model-cell patch and the ordinary W. It provides the closed simplex tau entirely inside V, a whole proper residual curve Gamma associated to a facet, and an independent-normal point eta on that facet. No whole analytic inverse image is placed in W by this step.

Lines 78-97 correctly exploit more than the abstract cone picture. In the tracked local charts the old parameters are actual monomials in the final parameters, up to model units:
t_i=product y_j^{P_ij}, with P unimodular and all its final columns strictly positive in the old coordinates. For every analytic point reducing to p_*, final vertical parameters are nonzero and have positive values. Thus every old parameter also has positive finite value. The whole p_*-tube, not just tau, maps into the original p-tube.

At the old point each f_i is a parameter monomial times a local model unit. Its pullback remains so at p_*. The final boundary components through p_* are all vertical and exhaust that maximal boundary stratum. Consequently no horizontal zero/pole remains through p_*, and each f_i is an analytic unit throughout the p_*-tube. This entire tube lies in the generic unit-open on which Y to X is an isomorphism. It need not lie entirely in W.

Let M be the original divisor-order matrix and N the multiplicity row. A supplies injectivity of M on ker(N). If v belongs to ker(NP) and MPv=0, then Pv belongs to ker(N) and M(Pv)=0, hence Pv=0 and v=0. Thus MP has rank n on ker(NP). Eliminating a positive vertical parameter identifies this hyperplane with retained coordinates and gives the rank-n affine identity F=A_*q_*+b_* throughout the actual source tube.

Model units have norm one throughout that reduction tube. All coordinates are analytic units there, so the equality is an ordinary smooth valuation identity on an actual common moment. It can be differentiated. No integral-affine condition on the eliminated-coordinate matrix is asserted or needed.

The positive q_*-target parametrizes the relative interior of the whole final maximal cone slice. Near eta the residual coordinate s tends to zero and the other selected normal values have positive limits. Therefore a small shallow collar about eta has a nonempty open set of monomial points in tau's interior, hence in Delta's interior and W.

## 6. The ordinary current domain and source isolation

O applies to the final model, the whole Gamma, the given independent-normal eta, and the current only on W. All selected normal components are vertical with their actual positive multiplicities; residue characteristic zero supplies the perfect-field hypothesis. O returns full inverse-image coordinate collars inside W and a single degree-proportional functional c_T[kappa(p):k]. Its compact principal-divisor primitives are already ordinary forms on W. No current is needed on an entire Gamma-tube.

At the adjacent point p_*, Q is used on the actual collar D_* with the explicit L geometry and the displayed R representation there. This supplies (5.2) for coordinate-moment top forms multiplied by arbitrary compact ordinary source cutoffs. The canonical factor is M_0[kappa(p_*):k], so the scalar in (5.2) is c_T/M_0.

There really is a common top-cell patch for the final comparison. The actual full-rank relation F=A_*q_*+b_* implies equality of the maximal-variation source sets for F, q_* and their concatenation on D_*. This follows by comparing local tropical dimensions on each ordinary neighbourhood, with ambient dimension n retained. It does not compare intrinsic dimension on an arbitrary compact subdomain with ambient dimension.

Take a compact monomial patch inside tau's interior and the collar. Its q_*-image contains an n-dimensional open set. The two assumed locally finite source cell structures have only finitely many relevant lower-dimensional faces near such a compact patch. Their images cannot cover that open set. Choose a point outside them. Since the source sets coincide and the cell families are locally finite closed cells, there is an ordinary neighbourhood isolating their common top-cell piece inside Delta. One need not assume a stronger affine-separation axiom or ordinary analytic sheets.

This is different from comparing two coincident target images: the common source set and the full-source affine relation have already been proved. Nor is a globally injective moment on all source points being asserted.

## 7. Same positive compact form and the coefficient ratio

Choose n components of F whose matrix in A_* is invertible. On the isolated source neighbourhood, a smooth target top form in those components pulls back to a nondegenerate paired top form. Choose a nonnegative compact ordinary source cutoff that is positive on a smaller relative open part of the common top cell, and a nonnegative target coefficient positive there. Its canonical integral is strictly positive because the coordinate image has nonempty n-dimensional interior and the canonical cell coefficient is positive.

The cutoff can be compactly supported inside the isolating neighbourhood, then extended by zero inside D_* and W. This is ordinary extension of a compact smooth function, not extension of the unknown current. No unproved ordinary-open basis of torus polycylinders is used.

The analytic relation F=A_*q_*+b_* makes the F-expression and the q_*-expression the same ordinary top form on the entire support. In the R formula isolated to the F cell, its current pairing is r_Delta times its canonical pairing. Q evaluates the same form as c_T/M_0 times that same positive canonical pairing. The common nonzero denominator proves r_Delta=c_T/M_0.

A determinant calculation is compatible with this argument: paired top forms acquire the square of the determinant; scalar integration acquires the inverse absolute determinant. Arbitrary-current and canonical coefficients acquire the same net absolute factor, so their ratio is unchanged. There is no source-aggregation inference and no comparison of unrelated moments only on a skeleton.

The resulting equation lambda(T,p)=M_0 r_Delta[kappa(p):k] holds for every closed p of this particular Gamma by O's already-established degree functional. It does not compare the ratios of two arbitrary original cells.

## 8. Numerical diagnostic

In the example, the column rays (1,1,1), (m,m+1,m), (m,m,m+1) have multiplicities 1,m,m. Their determinant is one. With residual coordinate s=v(y_0), retained q=v(y_2), and y_1 omitted, the equation gives
v(y_1)=(ell-s-mq)/m.
The old x and y values are ell+v(y_1) and ell+q. Thus the displayed retained matrix is (-1,-1/m;1,0), with positive determinant 1/m.

If the q-coordinate canonical coefficient is m at a rational residual point, its push to the old F coordinates is m times 1/m, namely one. This uses the paired-form determinant square together with scalar change of variables; it is not merely a coordinate relabelling of a degree. The arbitrary-current coefficient transforms by the same factor. Consequently lambda=m r_Delta d_p is the correct formula. Replacing the special multiplicities by one would fail.

## 9. Remaining boundaries and method

The corrected result is conditional access from each prescribed finite rational-moment cell to a residual functional, in the original-DVR residue-characteristic-zero algebraic setting. The model and the wall may depend on the cell and its relative neighbourhood. Rational replacement for analytic moments is a finite local presentation step, not a proof that coefficients of all summands agree. No propagation through arbitrary lower-dimensional attachments, arbitrary nonalgebraizable spaces, other value groups, or full P21.3 is established.

The only required correction found in the original statement is Section 2 of this report. The rest of the full assembly passed its stated conditional interface review. No candidate, live file or frozen predecessor was edited; no git or production call was made. No candidate freeze script was executed. No PDF was opened or rendered and no TeX compilation was performed for this audit. Primary CLD text and official HTML sources were inspected; their exact use is recorded separately.

