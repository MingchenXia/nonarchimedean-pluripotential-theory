# Original-field model adaptation: what is available and what is still missing

Date: 31 August 2026. Author: `/root/p082_independent_reaudit`.

## Status and bounded conclusion

This is a source-backed diagnostic and conditional reduction, not a P21.3 proof or a production acceptance. The parent asked whether proper modifications on the original field can adapt the finite ordinary analytic moments used by a compact test to the frozen residual-wall argument. The author previously wrote the generic common-moment comparison and the derivative-degree diagnostic; those are disclosed related work, not independent verification of this new note.

The answer separates into two positive steps and a genuine remaining interface:

1. On the analytification of an algebraic variety, finite analytic-unit moments can be replaced, on a finite ORDINARY open cover of a compact test, by rational-function moments with exactly the same tropical maps. This is the standard strict non-Archimedean approximation mechanism used by CLD; it is proved explicitly below, without a novelty claim.
2. In RESIDUE characteristic zero, those finitely many rational functions admit a proper regular model after original-field proper modifications, with strictly normal-crossing SUPPORT for the special fibre and their horizontal divisors. Multiplicities of the special fibre are retained. This follows from the precise characteristic-zero resolution theorems below.
3. That output does not satisfy the frozen wall packet automatically: the packet assumes a REDUCED regular strictly semistable model and selects VERTICAL components. Extending its wall argument would require multiplicity control, mixed vertical-horizontal walls, a locality/compact-support interface for a current defined only on an ordinary open W, and model-cell capture of the prescribed moment. The generic common-moment result compares already overlapping noncontracted cells; it does not construct that capture or determine new rank-drop cells.

The decisive next hypothesis is therefore a **source-local model-cell capture statement with individual coefficient control**, not the availability of algebraic rational functions or an unqualified appeal to semistable reduction. A separate nonreduced finite-projection candidate has now been frozen and received a separate independent conditional PASS. It includes an additional original-DVR argument for individual source cells, beyond aggregate finite-degree control; this note records that progress without importing it as a dependency or equating it with full model-cell capture.

## 1. Exact setting and frozen inputs

Let R be a complete discrete valuation ring, with uniformizer pi, fraction field K, perfect residue field k, and ell=-log|pi|>0. For the positive algebraic reduction, let X be a smooth proper INTEGRAL ALGEBRAIC K-variety of dimension n>=2. Write X^an for its analytification. Smooth proper varieties with several connected components can be treated componentwise. An arbitrary nonalgebraizable proper analytic space is not included in this algebraic reduction.

Let W be an ordinary open subset of X^an, and let T be a positive ordinary CLD current of bidegree (0,0) on W, with d'T=d''T=0. Its domain is not silently enlarged. The special case W=X^an will be distinguished below. A compact test means a compactly supported ordinary smooth (n,n)-form on W, presented locally by finitely many analytic units and smooth real superforms.

The entire following frozen notes were read before this investigation:

- `../p213_general_snc_wall_residual_functional_research_20260831/RESEARCH_NOTE.md`, together with its obstruction and source ledgers;
- `../p213_common_moment_generic_isolation_research_20260831/RESEARCH_NOTE.md`.

Their checksum lists were revalidated. Despite the historical directory name `general_snc_wall`, its actual statement requires an integral proper REGULAR STRICTLY SEMISTABLE R-SCHEME, hence a REDUCED special fibre, with local equation x_0...x_r=pi. Its final exclusions explicitly do not include nonreduced or non-strict models. It proves the residual divisor functional on the whole tube of a connected proper residual curve; it does not realize arbitrary analytic walls. The present note does not broaden those frozen hypotheses.

The displayed source representation premise (R) remains an assumption whenever source-cell coefficients are used. Neither the algebraic approximation nor the two obstruction examples below requires (R).

## 2. Exact rational-norm replacement on a finite ordinary cover

Let V be an ordinary open subset of X^an and f_1,...,f_m analytic units on V. For every x in V there are rational functions g_1,...,g_m in K(X)^times and an ordinary open neighbourhood O_x contained in V such that each g_i is analytic and nonvanishing on O_x and

\[
                         |g_i|=|f_i|\quad\hbox{on }O_x.       \tag{2.1}
\]

Proof. Choose an affine algebraic neighbourhood Spec(A) of the scheme point xi underlying x. Its analytification is an ordinary open neighbourhood of x. The completed valued field H(x) is the completion of kappa(xi) for the seminorm induced by x. One can read this directly from the construction of affine analytification: on an affinoid ball containing x, polynomials in algebraic generators are dense in its affinoid algebra; passing to the residue seminorm and then fractions gives density of Frac(A/ker(x))=kappa(xi) in H(x). This is the affine construction in CLD Section 11.1.11, combined with the definition of H(x) in Section 11.1.1.

For each i choose c_i in kappa(xi) such that

\[
                       |f_i(x)-c_i|<|f_i(x)|.                \tag{2.2}
\]

Lift c_i to a fraction g_i=a_i/b_i with a_i,b_i in A and b_i(x) nonzero. Inequality (2.2) also makes a_i(x) nonzero. On the algebraic open D(a_i b_i), g_i is an analytic unit. The strict inequality |f_i-g_i|<|f_i| is open in the ordinary analytic topology. Intersecting these finitely many open neighbourhoods with V gives O_x. The ultrametric inequality proves (2.1) everywhere on O_x. This is exact equality of functions, not an approximation of their derivatives or an equality only on classical points.

The same argument works simultaneously for any finite tuple of moments already defined near x. Its source-precision is the one in CLD Lemma 12.2.3; the rational variant on an algebraic space is also used explicitly in the proof of CLD Proposition 18.4.5, printed pp.521-522. No global algebraization of the original analytic functions is asserted.

Here is the full compact-test consequence. Let alpha be a compactly supported ordinary form, with compact support K_0 contained in W. For each x in K_0 first choose one original ordinary moment presentation alpha=F_x^*beta_x near x, then apply the preceding argument. On O_x the rational tuple G_x has EXACTLY the same tropical map as F_x, so

\[
                         \alpha|_{O_x}=G_x^*\beta_x.          \tag{2.3}
\]

Compactness gives a finite subcover O_1,...,O_N of K_0. Choose smooth nonnegative compact cutoffs phi_i supported in O_i whose sum H is positive on a neighbourhood of K_0. This is obtained by first shrinking to finitely many compact neighbourhoods and using CLD Corollary 15.2.5, squaring the cutoffs if necessary. Choose a further smooth compact cutoff eta supported in {H>0}, equal to one near K_0. Define

\[
             \rho_i=\eta\phi_i/H\quad\hbox{on }\{H>0\},
             \qquad \rho_i=0\quad\hbox{elsewhere}.            \tag{2.4}
\]

These are ordinary smooth functions: eta has compact support inside {H>0}, so extension by zero is smooth. Each rho_i has compact support in O_i, and their sum is one near K_0. Consequently

\[
                 \alpha=\sum_{i=1}^N \rho_i G_i^*\beta_i,    \tag{2.5}
\]

where each summand is extended by zero from O_i because its SOURCE support is compact there. This uses an ordinary open cover and actual source cutoffs, not a formal Zariski cover declared to be ordinary open. The cutoffs need not themselves be rational functions; (R), when used, already permits arbitrary smooth source multipliers.

Thus finitely many rational functions suffice for the moment coordinates relevant to this one compact test. Literal analytic functions can be transcendental over K(X); that fact is not an obstruction to (2.5), because only their local absolute values enter the tropical form presentation.

## 3. The original-field model supplied in residue characteristic zero

Now impose char(k)=0, equivalently R contains Q. This is stronger than merely char(K)=0: mixed characteristic is NOT covered by the resolution theorem used here.

For the finite rational functions in (2.5), there exists a proper regular integral R-model mathcalY whose generic fibre Y has a proper birational morphism p:Y -> X, and such that the reduced SUPPORT of the special fibre together with all total transforms of the zero and pole divisors of those functions is a strict normal-crossing divisor. The special fibre itself need not be reduced. No extension of K occurs.

Here is the construction, including nonprojective proper X. The morphism X -> Spec(R) is separated and finite type, since K=R[1/pi]. Nagata compactification (Stacks Tag 0F41) embeds X as an open subset of a proper R-scheme. Take the scheme-theoretic closure of the integral X. It is an integral proper R-model mathcalX_0; its generic fibre is X, because X is already proper over K and hence its open immersion in the separated generic fibre is also closed. Flatness follows from torsion-freeness over the DVR. This avoids assuming X projective.

The model is excellent, since R is complete noetherian local and the model is finite type (Stacks Section 29.20, especially Lemma 29.20.7). Apply Temkin's characteristic-zero desingularization of a B-scheme, Theorem 1.1.6 of arXiv:0912.2570v2, initially with empty boundary. Its centres avoid the regular locus, so it leaves the smooth generic fibre X unchanged and yields a proper regular model mathcalX_1.

On mathcalX_1 take the finite boundary consisting of the reduced special-fibre components and the closures of the prime zero and pole divisors of the selected rational functions. On a regular scheme these prime divisors are locally Cartier. Temkin Theorem 1.1.3 supplies a further proper sequence of regular-centre blowups making the boundary support strict normal crossing, with strictly monomial total transform. Its generic fibre is a proper birational modification Y of X, possibly nontrivial where the horizontal boundary was bad. It is smooth over the characteristic-zero field K, since it is regular. All operations are over R.

In a regular local ring of the resulting model, choose the local equations t_a of the boundary components through the point. The relevant rational functions and pi have the form

\[
          g_i=u_i\prod_a t_a^{m_{ia}},\qquad
          \pi=u_0\prod_{a\ \mathrm{vertical}}t_a^{e_a},       \tag{3.1}
\]

with units u_i, integers m_ia, and positive INTEGERS e_a. This follows from their Cartier divisors and local factorization, not from a claim that the units have constant valuation on every ordinary neighbourhood. On the appropriate formal tube the model units have norm one. Passing from formal charts to a prescribed ordinary source test still requires the source-local checks below.

This establishes monomial DIVISOR DATA, not a statement that a prescribed analytic source skeleton equals a model skeleton. Temkin's Theorem 1.1.11 gives another route through weak principalization; neither route eliminates the e_a. Likewise its formal strict-semistability Theorem 1.1.18 explicitly permits a finite extension R'/R and normalization after base change. That theorem is not an original-field answer to the present question.

## 4. Two concrete failures of automatic reduced adaptation

### 4.1 Nonreduced multiplicity persists under further domination

Start with P^1_R and blow up the closed point z=0 on its special fibre. This is a proper regular strictly semistable model of P^1_K; at its node there are parameters x,y with xy=pi. Blow up that node. In the chart y=xv the equation becomes

\[
                              \pi=x^2v.                      \tag{4.1}
\]

At the generic point of the exceptional divisor E, v is a unit and x is a uniformizer. Therefore ord_E(pi)=2. The new model remains regular and its special-fibre SUPPORT is SNC, but its special fibre is not reduced.

Let Z -> mathcalX_2 be any proper birational morphism with Z reduced, for example any proposed further regular model dominating this blowup. A proper birational morphism is an isomorphism over every codimension-one normal point of its target (Stacks Tag 0BBQ; its scheme reference is Lemma 33.17.3). Hence it is an isomorphism near the generic point of E. The corresponding prime divisor on Z still has order two on pi. Thus Z cannot have reduced special fibre.

This disproves the tempting assertion that an arbitrary model blowup can subsequently be dominated by a reduced strictly semistable model over the SAME DVR. Taking the product of this construction with a smooth proper R-scheme gives the same obstruction in every relevant relative dimension. The generic fibre is unchanged by these vertical blowups; the example does not itself prove that every particular moment requires this blowup. Its conclusion is exactly the failure of the asserted closure-under-domination operation.

### 4.2 A ramified horizontal divisor cannot become a strict semistable boundary

Take R=C[[pi]], K=C((pi)), X=P^1_K and the closed point D cut out by z^2-pi. Its residue field is L=K(sqrt(pi)), a ramified quadratic extension. If a proper regular strictly semistable pair over R adapted to D existed, the closure H of D would be a proper smooth relative-dimension-zero R-scheme, hence finite etale. Its generic field would then be unramified over K, a contradiction.

The same obstruction works in dimension n>=2 with X=(P^1_K)^n and D the product of this point with the remaining factors. Allow even a proper birational modification of X and let H be the strict transform of D in an alleged adapted strict semistable pair. The function field K(H) still contains s=sqrt(pi). Each local ring at a vertical prime of the regular H is a DVR, and

\[
                         \operatorname{ord}(\pi)
                           =2\operatorname{ord}(s).           \tag{4.2}
\]

But the strict semistable pair equations restrict to H with reduced special fibre, so that order must be one. There is a vertical prime because H is proper and dominates Spec(R). This contradicts (4.2).

Here 'strict semistable pair' includes the horizontal-divisor coordinate condition, not merely that the ambient variety has some unmarked semistable model. The local condition is the one in GRW Definition 3.1, specialized to a DVR: horizontal components are coordinate hyperplanes transverse to the vertical crossing. The example shows that arbitrary rational moment divisors cannot automatically be made such a reduced pair by original-field birational modifications. It does not obstruct the nonreduced SNC support supplied in Section 3, nor an unrelated route not requiring this strict pair.

## 5. What the local-uniformization and skeleton sources do not provide

Temkin, arXiv:1503.05729v2, Theorem 3.3.1 obtains a strictly semistable formal covering AFTER a finite extension of valued fields and by a rig-etale covering. Theorem 3.4.1 gives a surjective quasi-etale map to X tensor_K L for a compact quasi-smooth strict analytic X, again after a finite field extension. Those are not proper birational modifications of the original X. Neither their existence nor a canonical calibration degree formula defines a pullback of the arbitrary current T. This note does not perform such a pullback or a field extension.

Its Theorem 3.1.3 algebraizes an affine rig-smooth admissible formal scheme. That is not a simultaneous algebraization theorem for a prescribed global proper formal model, all local analytic functions, and all boundary data. Section 2 avoids needing such a theorem in the algebraic case. The possibility of another algebraization theorem with additional hypotheses is not excluded.

GRW's standing field is algebraically closed. Its Definition 3.1 and Section 3.2 explain strictly semistable pairs and base change from DVR models. Proposition 9.4 and Theorem 9.5 choose rational functions giving a faithful tropicalization of an ALREADY GIVEN strictly semistable skeleton. They do not say that an arbitrary prescribed analytic moment's source skeleton can be captured by such a model over the original field. Their slope formula uses canonical divisor/intersection degrees; it is not a substitute for the unknown-current divisor functional.

The generic common-moment note establishes a different and useful fact: if an actual concatenated moment H=(F,G) has a source top cell on which BOTH projections have rank n, the shared source isolation follows generically and normalized coefficients agree under (R). Adjoining units does not make every H-cell noncontracted under the old projection. A rank-drop H-top cell is a full-dimensional new source family outside the old F-skeleton, not a removable lower-cell exception. No target overlap or faithful tropicalization statement eliminates this distinction.

## 6. Locality, source support, and an exact conditional reduction

### 6.1 The domain of the current is a separate condition

For a proper birational p:Y -> X, the fixed-bidimension CLD support theorem transports a positive closed (0,0)-current on W to p^{-1}(W): restrict across the isomorphism locus, then extend in bidimension (n,n) across the lower-dimensional analytic exceptional set. Closedness follows in the two FIRST-derivative degrees (n-1,n) and (n,n-1). No unqualified d'd''/zero-extension commutation is used.

This does not extend T from W to X^an, nor its transport from p^{-1}(W) to all Y^an. The frozen wall theorem takes a current on the WHOLE ordinary tube red^{-1}(C) of its proper residual curve. A proper model dominating X does not imply that this tube is contained in p^{-1}(W). Formal Zariski charts and their generic analytic domains are not automatically an ordinary open cover with this containment property.

If T is global on X^an, this particular domain obstruction disappears: its transported current is global on Y^an, so it can be restricted to any wall tube. If T is only local on W, a sufficient replacement would be a proved outer-collar neighbourhood lemma that puts every compact primitive used for the residual principal-divisor tests inside p^{-1}(W), including the finitely many bad-point collars and the normal-radius strip. Such a lemma may be approachable near a suitably generic normal-radius point, but it is NOT proved here or supplied just by a formal G-local chart. The relevant support is analytic source support, not only a compact polyhedral image.

### 6.2 Source-local model-cell capture: the missing input

For one of the rational-moment summands rho F^*beta in (2.5), suppose (R) is available and use a locally finite coefficient-constant source cell presentation. Only finitely many top cells meet supp(rho). An exact sufficient model-adaptation input is the following:

- For each such F-top cell, a relatively open full-dimensional patch away from its presentation boundaries can be transported through an actual proper-modification isomorphism to a model collar where the individual normalized T coefficient is known.
- The transported T is defined on the source regions needed for that collar's wall identities, either because it is global or because the preceding source-support condition has been established.
- On that patch there is an actual common analytic moment H=(F,G), with rank-n projections to both F and the controlling collar moment G. No equality of tropical target images is substituted for this source patch.
- The known collar coefficients have one specified ratio c throughout the cells used for this comparison. The wall/incidence connectivity needed to establish a common c is part of the input, not asserted from connectedness of X alone.

Under these explicit assumptions, the generic common-moment comparison gives b_{F,C}=c a_{F,C} on each original coefficient-constant cell C. The constants do not change when a cell is restricted to a nonempty open patch. Formula (R), with its no-lower-cell residual clause, then gives <T,rho F^*beta>=c<delta,rho F^*beta>. Summing (2.5) gives the desired equality on THIS compact test. This is a conditional reduction, not a proof of those model-capture assumptions for all tests.

Section 3 supplies monomial boundary equations, but neither its resolution theorem nor the already proved noncontracted-cell comparison is the displayed capture input. In particular horizontal directions in an extended skeleton, finite-cover source sheets, and new rank-drop cells cannot be discarded as lower-dimensional sets. Even a smooth good-reduction model has an unmarked skeleton of dimension zero, whereas rational coordinate moments on a torus open of (P^1_K)^n expose n-dimensional source cells. Additional model/boundary geometry is essential.

There is a further exact wall-scope distinction. The frozen wall theorem selects n VERTICAL components whose intersection is the residual curve. An adapted SNC PAIR also has horizontal boundary components. Top-dimensional extended-skeleton cells may have codimension-one faces involving both types. Thus vertical-only wall identities do not supply all incidences of an adapted pair. A mixed-component extension would have to allow multiplicity N_i=0 for horizontal components, and check upper radial cutoffs near their analytic zero sets. Neither that extension nor its compact-source support is proved here. This issue is distinct from positive vertical multiplicities, aggregate versus individual coefficients, and ordinary-W locality.

## 7. The separate nonreduced finite-projection candidate: useful but not assumed

The parent proposed retaining the multiplicities from Section 3. At a closed residual point p of a wall curve the prospective completed local equation is

\[
 R_p[[x_0,\ldots,x_{n-1},w]]/
   \bigl(\pi-u(x,w)\prod_{i=0}^{n-1}x_i^{a_i}w^{a_p}\bigr),  \tag{7.1}
\]

with a_i>0, a_p>=0, a formal unit u, and the unramified coefficient DVR R_p. The prospective projection forgets x_0 and uses q=(v(x_1),...,v(x_{n-1}),v(w)) over the region

\[
 u_i>0,\quad s>0,\quad
       \sum_{i=1}^{n-1}a_i u_i+a_p s<\ell.                   \tag{7.2}
\]

The first exact geometric lemma needed is an ACTUAL proper finite-flat analytic map of degree a_0 on the relevant compact radial boxes, compatible as the boxes vary. A division argument must handle the dependence of the unit u on x_0 and must check the domain, all roots, surjectivity and proper support; one cannot simply solve x_0 as a single analytic function.

During this investigation the parent authored and froze that local candidate in `../p213_nonreduced_tube_finite_projection_research_20260831/RESEARCH_NOTE.md`, SHA256 `3001c94985c0d3e60f184ffd9f0e9591775ea026a98cd20ee538005edac11b7a`. Its analytic proof uses a Banach contraction division argument. Before this note's freeze, a separate independent audit reported PASS in its exact scope, with the individual-cell interpretation conditional on (R). That audit is `../p213_nonreduced_tube_finite_projection_independent_audit_20260831/INDEPENDENT_EXACT_BYTE_AUDIT.md`, SHA256 `9251b5571386ca23c5e5d6bb5d307559340460a200e8c63a7cffe200d9b54159`. This diagnostic checked its verdict and pins for status only; it does not provide another independent audit of that proof and does not rely on its conclusion for Sections 2-6. No production acceptance is inferred.

The candidate distinguishes two layers. Finite flatness and closedness yield an AGGREGATE coefficient b with canonical coefficient a_0[ kappa(p):k ]. In the additional original-DVR situation, with pi a uniformizer and the coefficient extension unramified, it further claims that independent target Gauss radii make v(x_0) have order a_0 modulo the target value group. The fundamental inequality then exhausts the entire fibre dimension a_0, forcing a single fibre field and no nilpotents. Under (R), the candidate uses this to obtain the individual source-cell ratio b/(a_0[ kappa(p):k ]). This is an additional source argument, not a consequence of finite flatness alone and not a claim of ordinary analytic sheets. It is recorded as a separately frozen candidate, not silently added to the earlier wall theorem.

Even if that local candidate is verified in full, a GLOBAL residual principal-divisor identity with its compact primitives is another step. Its prospective nonreduced extension is being developed separately. Neither local finite projection nor a vertical-wall extension supplies mixed-component walls, Section 6.1's local-W support, or Section 6.2's model-cell capture and incidence connectivity. Those are not absorbed by saying 'SNC' or 'finite degree'.

## 8. Practical next step and preservation

The local finite-flat/proper radial-box lemma and its additional original-DVR individual-cell argument now have a separately audited candidate; this ledger does not duplicate that proof. The exact remaining adaptation hypothesis is Section 6.2's source-local capture condition, including all relevant vertical-horizontal incidences. A later local-rigidity argument would additionally need the outer-collar support lemma of Section 6.1; global T avoids only that domain issue.

No existing semistable-reduction source checked here supplies the whole bridge without a field extension or additional source analysis. The literal reduced-domination and reduced-horizontal-pair shortcuts are refuted by Section 4. The rational-norm replacement and characteristic-zero monomial model construction are the positive concrete progress of this bounded task.

All earlier packets are unchanged. This dossier contains new Markdown research support and a source ledger only; it creates no TeX/PDF theorem artifact, changes no live manuscript, and makes no git or production call. No whole-current P21.3 rigidity, all-chart accessibility or arbitrary-current alteration pullback is claimed.
