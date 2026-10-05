# Independent all-point fiber mathematical review


# UNCHANGED new deduction, NOT granted: fixed-reference fiber proof92

# Fixed actual ample perturbations for all-point fiber descent

New, unreviewed mathematical reconstruction for original P16.1. It does not close an original problem. The actual round86 PASS grants the unchanged root89/90 deductions only in their precise conditional partial scope. Author84, review85 and the new review87 retain immutable independent inputs; this draft is not feedback to them.

## 1. Statement and fixed-bundle reduction

Let \(k\) be algebraically closed, trivially valued, and of characteristic zero. Let \(\pi:Y\to X\) be a projective morphism of integral projective varieties with geometrically connected fibers, let \(L\) be an actual ample rational line bundle on \(X\), and set \(M=\pi^*L\), \(\theta=c_1(M)\). The proposed conclusion is that every \(\varphi\in\operatorname{PSH}(Y,\theta)\) is constant on every fiber of \(\pi^{\mathrm{an}}\), on ALL analytic points and allowing value \(-\infty\). No countability is needed for this proposed fiber statement. A resolution over a geometrically unibranch target is the application.

Choose ONE actual very ample line bundle \(A\) on \(Y\). By BJ4.15(ii), there is a decreasing net of finite continuous rational PL functions \(\varphi_i\in\mathcal H(L_i)\), with actual ample rational \(L_i\), \(c_1(L_i)\to\theta\), and pointwise limit \(\varphi\). For each positive rational \(\delta\), sufficiently large \(i\) satisfies
\[
 \theta+\delta c_1(A)-c_1(L_i)\in\operatorname{Amp}(Y).
\]
Use only these VALID pairs \((i,\delta)\), ordered by increasing \(i\) and decreasing \(\delta\). They form a directed set: choose a smaller rational \(\delta\) than two given parameters, then an index above their indices and the ample-cone tail for this parameter. The scalar functions \(\varphi_i\) still decrease to \(\varphi\). Adding the genuine zero potential in the ample difference class shows
\[
 \varphi_i\in\operatorname{PSH}\bigl(Y,c_1(M+\delta A)\bigr).
\]
This is class addition preserving the ACTUAL scalar function. It does not equate two unrelated line-bundle metrics.

For a fixed pair, BJ3.10 and the literal same-bundle inclusion BJ3.9 give uniform approximation of \(\varphi_i\) by \(\mathcal H_{\mathrm{dom}}(M+\delta A)\subset\mathcal H(M+\delta A)\). The safe rational interpolation in the actual round86 report applies. Thus the metric with scalar potential \(\varphi_i\) has genuine uniform fixed-bundle FS approximation on the actual ample rational bundle \(M+\delta A\), without any EP assumption. Pull each finite section formula before taking its uniform limit. No decreasing fixed-nef-bundle approximation, abstract higher-dimensional current pullback, or unknown affine theorem over an extended field is being asserted.

## 2. A norm-preserving field with rational weights in its value group

Fix \(s\in X^{\mathrm{an}}\) and a complete valued extension \(F\) of \(\mathcal H(s)\). To use proper smooth algebraic curves through rational lifts, extend \(F\) by an independent Gauss variable \(\tau\) with \(|\tau|=e^{-1}\), complete, take an algebraic closure with an extended absolute value, and complete again. Denote the resulting complete algebraically closed nontrivially valued field by \(K\).

Adjoin \(\tau\) EVEN IF \(F\) already has a nontrivial absolute value. This preserves every original norm while ensuring \(\mathbb Q\subset\log|K^\times|\). Consequently all rational weights in the FS approximations are realized by norms of scalars after base change. No renormalization of \(\mathcal H(s)\) or of the tested analytic point occurs. The original trivially valued \(k\) remains embedded isometrically.

Let \(f:C\to Y_K\) be any nonconstant algebraic morphism from a smooth connected proper \(K\)-curve whose composite with \(\pi_K\) is the \(K\)-point \(s_K\). For a constant morphism the desired assertion is immediate. The analytic scalar pullbacks \(v_{i,\delta}=\varphi_i\circ f^{\mathrm{an}}\) are finite continuous, decrease, and have limit \(v=\varphi\circ f^{\mathrm{an}}\).

## 3. One graph model and one positive finite background measure

Take the product models \(\mathcal Y=Y\times_kK^\circ\), \(\mathcal X=X\times_kK^\circ\), with the pulled actual models \(\mathcal M=\pi^*L\) and \(\mathcal A=A\). BE5.13 gives ONE projective graph model \(\mathcal C\) of \(C\) with an extension of \(f\) to \(\mathcal Y\). Its flat finite-type model is finitely presented by BE4.5; \(K^\circ\) is not assumed Noetherian. It is enough to use the graph construction, without its optional flattening clause.

Properness extends \(s_K:\operatorname{Spec}K\to\mathcal X\) to a section over \(K^\circ\). The composite \(\mathcal C\to\mathcal X\) agrees generically with that section composed with \(\mathcal C\to\operatorname{Spec}K^\circ\). The two maps agree everywhere: the equalizer is closed by separatedness and contains the schematically dense generic fiber of the flat model. Hence \(f^*\mathcal M\) on \(\mathcal C\) is literally pulled from a line on \(\operatorname{Spec}K^\circ\). That line is free. Its reference metric on \(C\) is constant in a fixed frame and has zero curvature.

The model \(f^*\mathcal A\) is nef on every irreducible special-fiber curve. Indeed it is pulled from the original ample \(A\) along that component's morphism into a residue-field base change of \(Y\); its degree is nonnegative, including zero for constant images. BE4.20 permits a reduced-special-fiber dominating model over this algebraically closed nontrivially valued \(K\), and pullback retains the metric and nefness. BE8.11 then supplies ONE positive finitely supported curve curvature measure
\[
 \sigma_A=\sum_{\zeta\in\Sigma}a_\zeta\delta_\zeta,\qquad
 a_\zeta\ge0,\qquad \sigma_A(C)=\deg_C(f^*A).
\]
The support consists of the finitely many type-II Shilov points of the model. Reduced-model formula (8.3) is applied with its exact hypotheses; any use on an unreduced model must retain its fundamental cycle and multiplicities. No coefficient is discarded. The background for the actual reference \(f^*(M+\delta A)\) is exactly \(\delta\sigma_A\).

For each valid pair, pull the actual fixed-bundle FS formulas to \(C\). Basepoint freeness persists. BE7.14 and BE8.4 give the positive finite curvature \(\mu_{i,\delta}\) of the resulting continuous metric on \(f^*(M+\delta A)\), with mass \(\delta\deg_C(f^*A)\). Linearity for differences of the actual continuous metrics gives
\[
 dd^c v_{i,\delta}=\mu_{i,\delta}-\delta\sigma_A.
 \tag{1}
\]
Here the canonical \(M\)-reference is flat and the \(A\)-reference is FIXED. Wanner3.27–3.28 identify model-function CLD measures with Thuillier's curve Laplacian on semistable refinements, and the continuous uniform approximation determines the same current difference. The model-to-semistable-refinement and model-to-piecewise-linear dictionaries used in those published theorems remain primary curve background with their exact hypotheses. Independent verification of this dictionary and (1), rather than a degree-only claim, is a required part of the proposed proof.

## 4. Vanishing Green corrections and comparison of the original limit

Let \(V\subset C^{\mathrm{an}}\) be a connected strict affinoid domain with ordinary interior, with its finite boundary avoiding \(\Sigma\). Such domains can be chosen locally around any point of the smooth curve over nontrivial algebraically closed \(K\), moving their boundary to avoid finitely many specified type-II points. For each \(\zeta\in\Sigma\cap(V\setminus\partial V)\), Thuillier3.3.7(ii) gives a nonnegative continuous lisse Green function \(g_\zeta^V\), zero on \(\partial V\), whose interior Laplacian is \(-\delta_\zeta\). Set
\[
 p_\delta=-\delta\sum_{\zeta\in\Sigma\cap V}a_\zeta g_\zeta^V.
\]
The finite sum gives \(\|p_\delta\|_V\le B_V\delta\), \(p_\delta|_{\partial V}=0\), and, by (1),
\[
 dd^c(v_{i,\delta}+p_\delta)=\mu_{i,\delta}\ge0
 \quad\text{on }V\setminus\partial V.
\]
The corrected function is continuous. Wanner4.7 identifies continuous CLD-psh functions with Thuillier-subharmonic functions on that interior. Positivity of the lisse correction current uses the same signed model/slope dictionary. A compact boundary comparison follows from the curve maximum principle, as in Thuillier3.1.11–3.1.12.

The corrected functions need NOT be decreasing. Compare the ORIGINAL decreasing net directly. Suppose \(H\in H(V)\) and \(v\le H\) on \(\partial V\). For \(\varepsilon>0\), the compact closed sets
\[
 \{x\in\partial V:v_{i,\delta}(x)\ge H(x)+\varepsilon\}
\]
decrease with empty intersection. Directedness and compactness imply that eventually all are empty. On that tail the corrected function is at most \(H+\varepsilon\) on the boundary, hence throughout \(V\). Thus
\[
 v_{i,\delta}\le H+\varepsilon+B_V\delta\quad\text{on }V.
\]
Taking the net limit, for which \(\delta\to0\), and then \(\varepsilon\downarrow0\), gives \(v\le H\) throughout \(V\). This proof is valid at \(-\infty\) and never uses a nonexistent monotone corrected net.

The limit \(v\) is usc as the infimum of continuous functions. Its local harmonic comparison shows it is subharmonic or identically \(-\infty\) on a connected component, with the usual curve convention. To avoid any component-identically-infinite issue in the final application, apply the entire argument instead to the bounded floors
\[
 \varphi^{(m)}=\max\{\varphi,-m\}\in\operatorname{PSH}(Y,\theta).
\]
Zero is genuinely \(\theta\)-psh since \(M\) is semiample and nef, and maxima are allowed by BJ4.3. Each floor is bounded above by the global bound for \(\varphi\) and below by \(-m\). Its pullback to the proper connected \(C^{\mathrm{an}}\) is bounded usc subharmonic, attains a maximum, and is constant by Thuillier3.1.11. Letting \(m\to\infty\) proves that \(\varphi\circ f\) is constant, including the possible constant \(-\infty\).

## 5. Every analytic point, rather than only dense rational lifts

The analytic fiber over \(s\) is the analytification of the proper projective algebraic fiber \(Y_s\) over \(\mathcal H(s)\). Fix ONE closed point \(z\) of \(Y_s\). Its residue field is finite over \(\mathcal H(s)\), with the uniquely extended complete-field absolute value. For ANY analytic \(y\in Y_s^{\mathrm{an}}\), begin the preceding construction with \(F=\mathcal H(y)\). A compatible embedding of \(\kappa(z)\) into the resulting algebraically closed \(K\) is norm preserving. Both the evaluation giving \(y\) and this embedding giving \(z\) therefore define actual \(K\)-rational points on the geometric fiber, and their scalar pullback values are the ORIGINAL \(\varphi(y)\) and \(\varphi(z)\).

The geometric fiber is connected; reduction retains its topology. Its finite irreducible-component adjacency graph is connected. Choose closed \(K\)-points in the relevant component intersections. Within an integral projective component of positive dimension, any two closed points can be joined by a finite chain of morphisms from smooth connected proper curves. One construction resolves the component, lifts the two points by proper surjectivity, blows up the two distinct smooth lifts, takes sufficiently positive very ample complete intersections through their exceptional loci by Bertini, and maps the resulting smooth proper curves back. In dimension one use the normalization; zero-dimensional components contribute only their point. The precise Stacks/Bertini construction recorded in root81 must be checked as a scheme-theoretic curve-MORPHISM chain; an embedded smooth curve through a singular point is not required.

Constancy of every floor on those curves implies \(\varphi^{(m)}(y)=\varphi^{(m)}(z)\) for all \(m\), and hence \(\varphi(y)=\varphi(z)\). This compares each analytic point to the SAME closed point, even though its auxiliary field \(K\) depends on \(y\). No density argument for usc functions is used.

Consequently \(\varphi=\pi^*\psi\) as actual scalar functions for a unique \(\psi\) on \(X^{\mathrm{an}}\). Proper analytic surjectivity and compactness give usc descent: for every finite \(a\), \(\{\psi\ge a\}=\pi(\{\varphi\ge a\})\) is closed. The function is globally bounded above. In the birational case, the generic trivial valuation lifts to the generic trivial valuation, so \(\psi\) is finite there.

## 6. Proposed join to countable singular EP, retaining unproved inputs

For a resolution \(\pi:Y\to X\) of a geometrically unibranch projective characteristic-zero target, Stacks0GIQ and 0AY8 give geometrically connected fibers under their exact normalization/Stein hypotheses, as recorded in root81. The original possibly nonnormal \(X\) is retained. No normalization inverse theorem requiring target EP is used at this stage.

Suppose \(k\) is countable. The accepted actual-reference conversion in root90/round86 supplies a local decreasing rational affine-FS net for \(\pi^*\psi+h_{\pi^*L}\). The root91 countable extraction supplies a sequence on the same local neighborhood, with genuine unit-log contacts. The original witness is ONE fixed resolution \(\pi\), and the frame is the pullback of the original \(L\)-frame. Thus the proposed scalar descent has the precise weak local contact input needed by the conditional author83 global first-membership chain.

IF the unchanged author83 conditional global C1 chain is independently accepted and the root91 geometrical construction supplies its GEO antecedents, it follows that the ORIGINAL \(\psi\) belongs to \(\operatorname{PSH}(X,L)\). This is first membership before any target EP assertion. Pullback already preserves genuine target PSH; scalar fiber constancy and first membership make pullback onto. Birational identification of divisorial valuations then makes the onto map a homeomorphism in the divisorial pointwise topologies. The generic trivial point, hence the sup normalization, is also preserved.

Smooth nef source compactness (BJ5.20–5.21) now transports to normalized target PSH. BJ5.11 supplies countable target EP for EVERY actual ample rational \(L\). This would discharge E in the independently accepted round86 cardinality implication. That implication would then give arbitrary-cardinality target EP, followed by the accepted root89 actual raw equation, uniqueness, and after-EP normalization transport. The logic is ordered to avoid assuming target EP to prove the first onto pullback.

These implications are proposed joins, not already accepted conclusions. This draft still needs independent verification of the fixed-model curve Laplacian identity, Green/current comparison, all-point curve chains and resolution fibers, and their exact compatibility with the countable first-membership chain. Pending native author/review results must be read in their actual canonical scope before any join or original closure.

## 7. Exact primary reading and publication limits

The new literal units read use UTF8 byte decoding and one-based inclusive LF coordinates: BE1805.01016v3 LF1514–1590,1970–1995,2765–2808; Thuillier tel-00010990v1 LF3366–3445,4800–4902; Wanner1801.04713v3 LF735–821. The current-source SHA256 and exact literal-unit hashes will be recorded separately before freezing. Existing frozen root88 units include the full pertinent Green/max-principle bodies, BE graph/model-reduction material, Wanner4.6 and the complete pertinent 4.7 proof, and BJ smooth-nef EP. Only the listed pertinent source bodies are claimed read, not whole source files or every recursive model/semistable/Bertini proof.

Primary URLs: https://arxiv.org/pdf/1805.01016v3 ; https://theses.hal.science/tel-00010990v1/document ; https://arxiv.org/pdf/1801.04713v3 ; https://arxiv.org/pdf/1801.08229v4 . The proof uses published primary curve and resolution background with stated hypotheses; documentary provenance alone supplies no mathematical acceptance.


# UNCHANGED new deduction, NOT granted: current/boundary clarification93

# Curve current identity for the fixed-reference fiber draft

This is a new unreviewed mathematical addendum to the unchanged, checkpoint91-frozen root92 draft. It is not a grant, feedback to active native runs, or an original solution. It makes the proposed curve calculation more explicit and removes an unnecessary affinoid-boundary restriction.

## 1. Finite stages on the same actual bundle

Retain the field \(K\), the smooth connected proper curve \(C\), the morphism \(f\), the graph model, and the fixed actual references from root92. In particular \(K\) is complete algebraically closed nontrivially valued, its value group contains \(\mathbb Q\), the \(M\)-reference is flat in one fixed frame, and the \(A\)-reference has the fixed positive finite measure \(\sigma_A\). Fix one valid pair \((i,\delta)\) and write \(B=f^*(M+\delta A)\).

The uniform same-actual-bundle FS approximation from the accepted round86 local-reference argument, used here globally for the finite continuous PL \(\varphi_i\), gives rational FS metrics \(h_j\) on \(B\). They converge uniformly to the metric whose scalar difference from the fixed \(B\)-reference is \(v_{i,\delta}\). Every rational FS weight is in \(\log|K^\times|\). Thus \(h_j\) is a PURE FS metric on the actual \(B\), induced by a semiample rational model by BE5.14. The fixed reference is induced by the actual model \(f^*(\mathcal M+\delta\mathcal A)\). After clearing tensor powers and taking a common dominating graph model, their DIFFERENCE \(w_j\) is a rational model metric on the trivial bundle, with its actual generic-fiber identification. The reference has curvature \(\delta\sigma_A\), so the model difference has the signed curvature
\[
 \operatorname{curv}(w_j)=\mu_j-\delta\sigma_A.
\]
Here \(\mu_j\) is the positive curvature of \(h_j\), including the fundamental cycle, of mass \(\deg B=\delta\deg(f^*A)\). This is an additive actual-model identity, rather than comparison of equal degrees alone.

Algebraic model metrics are formal by completion. GK1406.7637v3, 8.8–8.11, supplies the precise formal/piecewise-linear dictionary, tensor/dual/pullback operations, and G-cover criterion over an algebraically closed complete NONTRIVIAL field. Its 8.13 statement is also read, but the nontrivial formal-to-algebraic converse is not needed for this direction. On a smooth proper curve the semistable formal model dictionary in Wanner3.26–3.28 puts a rational trivial model metric into a skeleton description and identifies its CLD measure with its Thuillier Laplacian. This uses the published curve semistable-model background with its stated field hypotheses; it does not assume higher-dimensional semistable reduction over an arbitrary valuation ring. The curve model refinement needed to preserve a specified formal metric remains part of the exact primary dictionary to be verified independently.

Consequently, for every finite stage,
\[
 d'd''[w_j]=[\mu_j-\delta\sigma_A].
 \tag{2}
\]
For a compactly supported smooth test \(q\), uniform convergence \(w_j\to v_{i,\delta}\) gives convergence of the left side: \(d'd''q\) is a fixed compactly supported signed Radon measure on the curve, and the integral difference is bounded by \(\|w_j-v_{i,\delta}\|_\infty\) times its total variation. BE8.4 gives weak convergence \(\mu_j\to\mu_{i,\delta}\) on this SAME actual generic-fiber bundle. Passing to the limit in (2) gives the precise current form of root92's identity:
\[
 d'd''[v_{i,\delta}]=[\mu_{i,\delta}-\delta\sigma_A].
 \tag{3}
\]
Both limits are uniform/weak limits of genuine fixed-bundle metrics. No pullback of an unspecified higher-dimensional current or preexisting singular EP is used.

## 2. Exact lisse correction current, including point types

Wanner4.2 proves that the CLD current and Thuillier Laplacian of a lisse function agree locally at every type-II point. Its proof constructs local signed model functions with integral slopes on rational-length edges, expresses the lisse function as a real linear combination plus a constant, and applies 3.27–3.28. The rational lengths can be chosen here because the auxiliary Gauss variable ensured \(\mathbb Q\subset\log|K^\times|\); the original absolute values remain unchanged.

For the Green functions used here, the Thuillier Laplacian on the affinoid interior is supported at the specified type-II center. At a type-I or IV point, a lisse function is locally constant, as in Wanner4.3. At a type-III point away from the discrete Laplacian support, its skeletal restriction is locally affine on the corresponding annulus. In an annulus coordinate it is \(a\log|T|+b\), and both currents vanish by Poincare–Lelong for the invertible analytic \(T\). Thus the type-II equality and these other point-type calculations give
\[
 d'd''[g_\zeta^V]=[-\delta_\zeta]
 \quad\text{on the interior of }V.
\]
This supplies the signed equality for the Green correction itself; positivity of a current of \(-g_\zeta^V\) alone would not identify its exact measure.

By linearity and (3), the finite lisse correction in root92 therefore satisfies
\[
 d'd''[v_{i,\delta}+p_\delta]=[\mu_{i,\delta}]\ge0
\]
on the interior. The function is continuous. Wanner4.7 then supplies genuine Thuillier subharmonicity there. The compact boundary maximum principle and the original-net comparison in root92 apply verbatim. In particular monotonicity of the corrected functions is never required.

## 3. No need to move the affinoid boundary

The demand in root92 that \(\partial V\) avoid the finite set \(\Sigma\) is UNNECESSARY. Use ANY connected strict affinoid \(V\) with interior. Define \(p_\delta\) using only \(\zeta\in\Sigma\cap\operatorname{Int}(V)\). Atoms of \(\sigma_A\) on \(\partial V\) are absent from its restriction to the interior current in (3), so they require no correction there. Every interior Green function still vanishes on all of \(\partial V\), and the same finite uniform estimate holds. Hence (3), positivity on the interior, compact boundary comparison, and the limit \(v\le H\) hold for every such \(V\).

For the bounded floors of root92 this verifies exactly Wanner2.4's harmonic-comparison definition on every connected strict affinoid. For a disconnected strict affinoid apply the same comparison on its finitely many connected components. The curve is strict and good over this \(K\); local strict affinoid neighborhoods exist. Thus no separate boundary-avoidance or point-density assertion is needed to infer subharmonicity of a bounded floor.

The subsequent maximum principle on the proper connected curve, comparison of each analytic fiber point to one fixed closed point by curve morphism chains, and the countable first-membership join retain root92's exact dependencies. This addendum does not independently verify or grant those later steps.

## 4. Primary bodies read and exact scope

New bodies read by UTF8 byte decode with one-based inclusive LF coordinates: Wanner1801.04713v3 LF232–312 and 822–990, including the exact harmonic/lisse/Green definitions and complete pertinent 4.2–4.5 proof bodies; GK1406.7637v3 LF353–385 and 3380–3595, including the standing field/variety hypotheses, 8.4 full G-cover proof, and 8.11–8.13 statements and pertinent proofs. The fixed GK PDF is https://arxiv.org/pdf/1406.7637v3, verified as the latest listed v3 (13 September 2016) at its live abstract page, not assigned an imaginary edition. PDF SHA256 62c7e4dfebab75d725f529c6ef78c300856c63fd050a9399e8a86879e569315d; layout text SHA256 4336903644edf53838f829cf22a3326257f909adfae1f906738f9f8534d1826b.

Live Stacks0AY8 rendered24–39 and 0GIQ rendered22–24 were read in full: the former requires the NORMAL base in all six hypotheses and gives geometric connectedness; the latter supplies a universal-homeomorphism normalization of an irreducible geometrically unibranch target. Thus in root92's resolution application, factor the smooth source through the actual normalization, apply 0AY8 to that normal base, then use the universal homeomorphism to identify every geometric target fiber topologically. This retains nonnormal \(X\) and every analytic fiber; it does not apply 0AY8 directly to a nonnormal base. Properness over the normal base follows from the graph/properness argument, with the same generic function field and all source generic points dominating it.

The new live observations are saved in continuation93-live-curve-model-and-fiber-primary-observation.json. No whole GK/Wanner source file or every recursive Raynaud/formal-GAGA/semistable proof is claimed read. The fresh mathematical uses and the complete fiber/first-membership join remain unreviewed.


# UNCHANGED older unreviewed geometric curve-chain lead81, NOT a grant

# Geometric details for fiber descent and conditional normalization onto

New root reconstruction, not independently reviewed or accepted. It supplements the frozen continuation80 proposal without editing it or either active campaign. The original P16.1 and P13.2 are still open. Retain projective reduced irreducible geometrically unibranch varieties over algebraically closed trivially valued characteristic-zero fields and an ample rational line bundle. Actual metric/curve compatibility F1 and the singular countable Runge/genuine-membership gate C1 remain to establish.

## 1. The resolution has geometrically connected fibers

Let nu: Xn -> X be the normalization and p: Z -> Xn a projective resolution. Finite-type schemes over a field have finite normalization. Geometric unibranchness makes nu a universal homeomorphism; this is [Stacks, Tag 0GIQ](https://stacks.math.columbia.edu/tag/0GIQ), with its local normalization-ring proof read. For normal X the same conclusion follows from the local normal-domain definition; see [Tag 0BQ3](https://stacks.math.columbia.edu/tag/0BQ3).

Apply [Tag 0AY8](https://stacks.math.columbia.edu/tag/0AY8) to p. The target Xn is normal and integral, Z is integral and reduced, p is proper, its generic point dominates the target, and the birational generic fiber is Spec k(Xn), whose global functions are exactly k(Xn). All six hypotheses are therefore satisfied. Stein factorization gives geometrically connected fibers of p. The finite intermediate algebra is a reduced integral algebra with the same function field as Xn; normality forces it to equal O_Xn.

For any field-valued point x of X, the normalization fiber is a finite universal-homeomorphism scheme over k(x). Its reduction is a single point with a purely inseparable residue extension. In characteristic zero that extension is the identity. After any further field extension the same conclusion holds. The reduced fiber of pi=nu p consequently has the same underlying space as the corresponding p fiber. Nilpotent thickenings do not change analytic points. Thus pi has geometrically connected fibers also over arbitrary completed residue fields H(x). This concerns fiber topology; it does not discard multiplicities in the MA fundamental cycle.

## 2. Joining two values uses ordinary Bertini on a blowup

Let K be algebraically closed of characteristic zero and Y smooth projective irreducible over K, of dimension d. To compare values at two K-points a,b, equality is immediate if a=b or d=0; for d=1 use Y itself. Assume d>=2 and a!=b.

Blow up the two distinct smooth points. The resulting Y' is smooth projective irreducible. Its exceptional divisors Ea and Eb are projective (d-1)-spaces. Choose a very ample H on Y'. Successively choose d-1 general members of H, keeping every intermediate intersection smooth and connected and meeting each exceptional divisor properly. Ordinary smooth Bertini applies because the complete linear system generates H and embeds Y'; its exact hypotheses and the dimension-count proof are [Tag 0FD6](https://stacks.math.columbia.edu/tag/0FD6). At each stage of dimension at least two, connectedness follows from depth at least two, properness and ampleness in [Tag 0FD9](https://stacks.math.columbia.edu/tag/0FD9). Smooth connected schemes over K are irreducible here. The combined argument is also recorded in [Tag 0G4G](https://stacks.math.columbia.edu/tag/0G4G).

The additional proper-intersection requirements exclude only finitely many proper closed subsets of each hyperplane parameter space, so they can be imposed with the smoothness requirements. The final C is a smooth projective connected curve. Because H restricts amply to each Ei,

    length(C intersection Ei) = (H^(d-1) . Ei) > 0.

It therefore has a K-point above a and another above b. The composed algebraic morphism C -> Y joins the original points. No linear system with assigned base points was used.

For a connected reduced projective scheme, resolve its finitely many irreducible components, choose preimages of the two points and of closed points in adjacent component intersections, and apply this construction on each resolution. Its component-intersection graph is connected, so finitely many curve comparisons connect the two values. The curves need only map to the original scheme. Consequently F1 must mean pullback of supplied actual metric approximants along algebraic morphisms from smooth curves, including the resolution and blowup maps; it must not be read as just restriction along smooth closed embeddings. Pullback of actual generating sections preserves generation and supplies that functorial route once F1's metric/class identification has been proved.

## 3. Finite normalization data really can be descended

Let k0 be the algebraic closure in k of a field generated by finitely many coefficients of X, L and a finite PL test. It is countable. Enlarge this finite coefficient set by affine presentations of the finite normalization, multiplication tables, monic integral equations for its generators, overlap maps, and the birational inverse on one nonempty affine open. These are finitely many data. The resulting map B0 over A0 is finite and birational, with its base change the original normalization. The original variety and its generic fiber are retained.

Reducedness descends because A0 -> A0 tensor k is injective. Normality of B0 descends by [Tag 033G](https://stacks.math.columbia.edu/tag/033G). Locally an element a/b integral over a downstairs domain lies in its upstairs normal extension. Faithful flatness contracts bS to bR, so a/b was downstairs already. Since B0 is finite birational and normal, it is precisely the integral closure of A0: an element integral over A0 is also integral over B0 in their common fraction field.

The descended finite map is a universal homeomorphism by fpqc descent, whose exact statement and proof were read at [Tag 0CEX](https://stacks.math.columbia.edu/tag/0CEX). Thus each local integral closure has one maximal ideal and purely inseparable residue extension. This is geometric unibranchness by [Tag 0BPZ](https://stacks.math.columbia.edu/tag/0BPZ). It proves that the countable descended variety satisfies the geometric hypothesis required by C1. The proof does not assume that arbitrary PSH functions descend.

Finite Hdom nef dominance has an especially direct downward check over the algebraically closed fields being used. Clear denominators in the rational difference D=L-M. Every integral proper curve C over the smaller algebraically closed field is geometrically integral; its base extension stays integral. Cohomology under field extension gives the same Euler characteristic and hence the same degree of D. If D is nef upstairs, its degree on every such downstairs curve is nonnegative. Thus D is nef downstairs. Finite generation of the section presentation descends by faithful flatness. This verifies downward finite Hdom data, while actual inclusion in the genuine class still uses the nef-reference/model compatibility in C2. No ascent of arbitrary model regularity or absolute normalization is inferred.

## 4. A finite birational normalization is an actual blowup

This provides a concrete route into BJ's birational PSH theorem after EP, not a substitute for EP. Let B=nu_*O_Xn. It is a finite O_X-algebra inside the common rational function field. The conductor J=Ann(B/O_X) is a nonzero coherent ideal. For a sufficiently high ample twist A choose a generically nonzero section a of J tensor A. Locally trivialize A and let a_i be the resulting nonzero element of J. The ideals

    I_i = a_i B_i subset O_X(U_i)

glue to a coherent ideal I: on overlaps the a_i differ by an invertible regular transition factor. Each I_i is finite and generically trivial. The multiplication of B_i gives I_i^m=a_i^m B_i for every m>=1.

On U_i=Spec A_i the Rees algebra is A_i in degree zero and a_i^m B_i in positive degree m. Its Proj is covered by the single chart D_+(a_i t). Indeed, for b in B_i a monic integral equation over A_i, multiplied by the appropriate powers of a_i t, makes (a_i b t) integral over the graded subalgebra generated by a_i t. A homogeneous prime containing a_i t must therefore contain every positive-degree generator, and cannot be a Proj point. The degree-zero part of the localized Rees algebra is

    A_i[I_i/a_i] = B_i.

Hence Bl_I X is exactly Xn, compatibly on overlaps. This makes the ideal needed for the error-term argument explicit, without changing the variety or passing to a different hull.

## 5. Conditional onto PSH after the envelope gate

Suppose EP has been proved in every rational ample class of X by C1 and the finite-data extension. Put theta=c1(L) and theta_m=(1+1/m)theta. Then theta_m-theta is ample, the theta_m have EP, and theta_m decreases to theta.

BJ 1801.08229v4 LF2557--2594 proves the birational error theorem: for the blowup ideal I there is an ample class omega and h=log|I| in PSH(omega) such that any psi in PSH(pi*theta) satisfies

    psi + epsilon pi*h = pi* v_epsilon,

with v_epsilon in PSH(theta+epsilon omega). Choose epsilon_m decreasing to zero, small enough that theta_m-theta-epsilon_m omega is nef. Since h<=0, the v_m increase on divisorial valuations and therefore everywhere by the minimum usc extension theorem. Their sup normalization is bounded: h has zero value at the trivial valuation. For each m0, EP in theta_m0 supplies the increasing-net limit as a genuine theta_m0-psh function. Its divisorial values are independent of m0. Varying-class closure then puts that same minimum usc function v in PSH(theta), and divisorial uniqueness yields pi*v=psi. This is the actual onto conclusion of BJ Lemma 5.13, LF2859--2873.

The source's final line LF2594 prints PSH(theta) after proving membership in PSH(L_m+H). In that error theorem the class there must be theta+omega, as the theorem statement and every preceding line require. The ample error is retained in the preceding argument and is sent to zero only in the later EP-based step. Dropping it at LF2594 would incorrectly assert unconditional onto invariance.

Applied to nu, the analytic map is a homeomorphism: each completed-residue-field fiber is finite, local and radicial, with one analytic point, and properness gives a closed continuous surjection of compact Hausdorff spaces. Thus onto PSH also gives onto CPSH, using actual continuity and the inverse homeomorphism.

To extend this to E1 and the equation one still must verify the proper projection formula for the actual continuous mixed operator, nu_*[Xn]=[X], degree-one raw mass equality and decreasing unbounded energy/MA compatibility. With those identities, the continuous-majorant definitions on the two spaces correspond exactly, giving energy equality and E1 onto; finite-energy target measures correspond by the homeomorphism. These analytic operator identities and the actual variational existence argument are deliberately retained as requirements, not declared solved by this geometric addendum.

## 6. Read evidence and remaining limit

The linked Stacks statement/proof bodies were actually read through the native web tool on 5 October 2026. These are live scholarly pages; their stable tags are cited, but no full primary-file hash or LF snapshot is asserted. The explanations above are new paraphrased derivations with their application hypotheses, not copied page bodies. Local BJ evidence is the frozen extract with SHA256 659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0, read at inclusive LF2550--2616 and previously LF2859--2881.

This addendum supplies checked primary geometric inputs and an explicit conditional normalization route. It does not establish F1 metric conversion, C1 singular Runge/genuine membership, or the remaining equation theorem. No original closure or accepted new dependency is asserted.


# Unchanged original P16.1 and full family

{
  "problem": "Original P16.1:\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nComplete unchanged mathematical family:\n\n10     The general non-Archimedean Monge–Ampère equation\nActive items: P16.1, P16.2, P16.3, P16.4, P16.5, P16.6, P16.7. Status: Open in the\nresidual scope.\n\n10.1    Atomic targets\nP16.1 (T5): Finite-energy equations on singular or unibranch varieties\nExtend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-\nuniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in\ncompactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization\nand ﬁeld hypotheses.\n\nP16.2 (T5): Proper nonprojective algebraizable equation theories\nConstruct an appropriate replacement positivity datum and the associated psh, ﬁnite-energy,\ncomparison and equation theory on proper nonprojective algebraizable spaces. A proper\nalgebraic scheme with an ample line bundle is already projective, so retaining that datum\nwhile dropping projectivity is not a new case.\n\nP16.3 (T5): Finite-energy equations in positive residue characteristic\nConstruct the required ﬁnite-energy operator and prove existence and uniqueness when the\noriginal residue-characteristic restriction is removed. Replace the resolution, model-regularity\nand envelope inputs wherever they are used rather than merely changing the standing ﬁeld\nhypothesis.\n\nP16.4 (T4): Finite-energy equations over arbitrary complete valued ﬁelds\nExtend the operator and existence theorem to nondiscrete valuations and arbitrary complete\nnon-Archimedean ﬁelds outside the established invariant-toric, skeleton-supported endpoint.\nA deﬁnition of the ﬁnite-energy space alone does not establish the operator or the equation.\n\nP16.5 (T5): Finite-energy equations for nonample positivity classes\nExtend the equation theory to big or pseudoeﬀective nonample classes, specifying the psh cone,\nreference singularity type, energy and total mass. At zero volume, the existing probability\nnormalization must be replaced rather than retained unchanged.\n\nP16.6 (T4): Arbitrary-support ﬁnite-energy measures\nProve the operator and existence-and-uniqueness theorem for arbitrary ﬁnite-energy measure\nsupport beyond the known toric skeletal regime. Measures must satisfy the correct mass and\nenergy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine\nMonge–Ampère measure by another inverse measure construction.\n\nP16.7 (T5): Finite-energy equations on nonalgebraizable analytic spaces\nConstruct the ﬁnite-energy operator and its existence-and-uniqueness theory on genuinely\nnonalgebraizable analytic spaces, with an explicit positivity datum and the necessary com-\npactness, envelope and comparison replacements.\n\n\n\n\n                                              73\n\n10.2    What constitutes a solution\nFor each axis, state the retained hypotheses and construct the ﬁnite-energy operator together\nwith the corresponding existence-and-uniqueness theorem. Specify the measure mass and\nﬁnite-energy condition, uniqueness modulo constants and the replacement inputs for com-\npactness, envelopes, energy diﬀerentiation and comparison. An endpoint solving a special\ntoric measure class does not remove a general axis.\n\n10.3    Full statement and detailed state of the art\nProblem 10.1. Extend the ﬁnite-energy existence and uniqueness theory for the NA Monge–\nAmpère equation beyond the currently proved combinations of smoothness, projectivity,\nresidue characteristic, valuation, positivity class, support, and algebraizability hypotheses.\n\n    This is not one yes-or-no assertion. Positive characteristic, singular or unibranch varieties,\nnondiscrete valuations, big classes, arbitrary support, and nonalgebraizable analytic spaces\nrequire diﬀerent inputs. The known variational proofs use compactness, envelope regularity,\ndiﬀerentiability of energy, and a comparison principle; deleting a geometric hypothesis is valid\nonly after replacing every place where it enters. The relevant positive results and their distinct\ndomains are surveyed in Book Chapter 28, Book Chapter 29.\n    The projectivity axis has one logical constraint. A proper algebraic K-scheme endowed\nwith an ample line bundle is already projective over K [Stacksb, Tag 0B5N]. Thus P16.2\ncannot mean that one retains the BFJ line-bundle polarization L while simply deleting the\nword “projective.” A nonprojective proper algebraizable extension must ﬁrst replace that\npositivity datum—and then construct the corresponding psh, ﬁnite-energy, and comparison\ntheory—rather than merely rerun the original argument. No canonical replacement with the\nrequired equation theory is asserted here.\n    One exact source-stated axis is especially clean. Pille–Schneider observes that the ﬁnite-\nenergy space can be deﬁned over an arbitrary non-Archimedean ﬁeld, but that the extension of\nthe Monge–Ampère operator is not known there in general; the discretely valued characteristic-\nzero and trivially valued cases are the established endpoints [PS23, Remark 4.4]. This should\nbe solved before bundling all remaining axes into a single theorem.\n\nProposition 10.1 (Arbitrary-ﬁeld invariant toric skeletal endpoint). Let K be a complete\nnontrivially valued non-Archimedean ﬁeld, XΣ a proper toric K-variety, and L an ample toric\nline bundle. If µ is a positive Radon measure on XΣan , is supported on the canonical skeleton\nNΣ , gives zero mass to NΣ \\NR , and has total mass degL (XΣ ), then there is a toric continuous\nsingular psh metric on L whose Monge–Ampère measure is µ. It is unique up to multiplication\nof the metric by a positive constant.\n\n    Thus nondiscreteness and the arbitrary complete ground ﬁeld cause no obstruction in\nthis invariant toric, skeleton-supported range. Here “continuous singular” has the source’s\nextended-valued meaning: local weights are continuous into R ∪ {−∞}, as in [BGGJK25,\n§5.3.1]. It does not imply ﬁnite real-valued weights or ﬁnite energy. This is not an arbitrary-\nﬁeld ﬁnite-energy theorem in the BFJ sense: the result permits a singular potential, requires\ntorus invariance and skeletal support, and does not construct the general extended Monge–\nAmpère operator. In particular, P16.4 and P16.6 retain the respectively nonskeletal and\nnoninvariant ﬁnite-energy residual scopes.\n    There is also a distinct, nonproper algebraic endpoint. Let n > d ≥ 1, let X be a smooth\nprojective Fano complex variety of dimension n, and let D be a reduced simple-normal-crossing\nanticanonical divisor whose dual complex is the standard (d−1)-simplex. For the aﬃne Calabi–\nYau complement X = X \\ D, Wang’s Theorem A constructs a continuous non-Archimedean\npsh function on X an , over the trivially valued ﬁeld C, whose local Monge–Ampère measure\n\n                                               74\n\nis the canonical Lebesgue measure on the essential skeleton [Wan25]. The source is a version-\none preprint and uses a local CLD/tropical–convex construction. In particular, it neither\nconstructs the BFJ ﬁnite-energy operator nor treats arbitrary measures or arbitrary aﬃne\nvarieties. Since X is aﬃne and hence not proper, this endpoint does not answer P16.2; it\nonly records a special nonprojective algebraic solution after the properness requirement is\nalso dropped.\n    There is a separate ﬁnite-atomic inverse statement which must not be called a ﬁnite-energy\nMonge–Ampère theorem. Under its standing assumptions that K is maximally complete and\n|K × | = R>0 , Fang ﬁxes an irreducible projective K-variety with an ample line bundle and a\nﬁnite set of graded birational points on its aﬃne cone. For every probability vector on that\nﬁnite set, the source constructs a Shilov-ﬁnite, possibly singular metric having the prescribed\nequidistribution measure [Fan25, Proposition 4.8]. The source itself says that comparing this\nBanach-algebra measure with the genuine Monge–Ampère measure requires the separate con-\ntinuity property of an envelope metric. Thus it supplies neither a continuous semipositive\nsolution nor the BFJ ﬁnite-energy operator for the prescribed atomic measure, and does not\nnarrow P16.6.\n    There is also a resolved negative regularity chronology. The ﬁrst skeletal-factorization\nquestion of Gubler–Jell–Künnemann–Martin already fails on their toric surface [GJKM19,\nAppendix A]. Boucksom–Jonsson then construct a ﬁnite atomic Monge–Ampère measure sup-\nported on a dual complex whose solution is invariant under no retraction attached to any\nSNC model; they also construct a divisorial Green function that is not Q-PL [BJ24b, Theo-\nrems A and B]. Hence support on a dual complex does not imply factorization through some\nreﬁned skeleton. This is a theorem-level obstruction to a proof strategy, not an open regularity\nexpectation.\n    The Rethlas programme treats each axis separately and ﬁrst searches the post-2020 liter-\nature for an existing theorem. Alterations and universal homeomorphisms can address some\nalgebraic descent questions, but they do not by themselves supply multiplier ideals or dif-\nferentiability in positive characteristic. The unrestricted formulation is open; several strictly\ndelimited axes are already known.\n\n\n\n\n                                               75\n\n",
  "completionCriteria": "Establish the genuine finite-energy operator, exact measure mass and energy condition, existence, uniqueness modulo constants, and every compactness/envelope/differentiation/comparison replacement for the singular/geometrically unibranch projective domain with explicitly retained field and polarization hypotheses. Verify the new envelope source and the actual general-variety global theory. No change to the original mathematical target is permitted."
}


# TASK-GRANTED actual precise partial PASS

{
  "verdict": "PASS",
  "report": "PASS for the precise retained conditional partial scope. The operator construction, target-EP-to-equation implication, local reference conversion, conditional cardinality reduction, and after-EP normalization transport are correct. This does not establish singular EP or close P16.1. E remains the explicit antecedent of the cardinality implication; all-point fiber constancy and countable global C1 remain separate missing gates. Neither pending author result nor documentary observations were used as mathematical background.\n\nThe retained domain is an algebraically closed trivially valued field of characteristic zero, a reduced irreducible projective variety, and an actual ample rational line bundle L. The relevant BJ constructions allow singular varieties. The multilinear extension in BJ7.14 supplies the test-containing pairing used in BJ7.18; positivity, PL density, and the constant test produce the genuine Radon operator. Its model coefficients retain every b_E, and its raw mass is V=(L^n). Thus MA_raw=V MA_BJ, E_raw=V E_BJ, and E_raw-dual(μ)=V E_BJ-dual(μ/V). BJ9.20 applies because X is irreducible: finite dual energy is equivalent to integrability of every actual E1 potential. No support restriction is introduced. These are statements about the published operator, not an assigned inverse measure. [BJ](https://arxiv.org/pdf/1801.08229v4)\n\nUnder target EP, BJ5.11 gives compactness of the normalized target PSH space in the divisorial topology. The maximizing sequence has bounded J by BJ9.15–9.16. Its convergent subnet has an actual normalized PSH limit, and lower semicontinuity of J puts that limit in E1. BJ9.19 gives target-measure L1 convergence; energy upper semicontinuity then proves attainment of the variational supremum. Applying the PL variation estimate with both f and −f identifies the maximizing potential’s probability MA with μ/V, hence its raw MA with μ. This establishes an actual solution, rather than only convergence of measures. Irreducibility gives uniqueness modulo constants through BJ10.4. Genuine finite-energy locality and comparison are available before EP.\n\nThe supplied sign corrections are mathematically harmless and correct. The absolute-value identity is |a−b|=2(max(a,b)−b)−(a−b). The weighted integral is the test-containing pairing minus the zero-test pairing, at both finite stages and the limit. For continuous directions, the error is |t|ε on each side before division by t; the derivative follows by taking the PL derivative first and then sending ε to zero. For locality’s limiting step, the appropriate weighted convergence result is BJ7.21(ii); the source’s reference to BJ7.19(iii) there is a harmless cross-reference slip.\n\nContinuous base change has the required fixed reference. BJ3.9 literally places Hdom(L) inside H(L) for the same actual ample rational bundle, and BJ4.16 supplies uniform approximation without EP. Consequently BE7.14 applies to the corresponding fixed-bundle metrics. The smooth regularized FS formulas pull back with their real weights unchanged. BE8.3(iv) preserves the fundamental cycle and the raw measure at each smooth stage; BE8.4 and continuity of pushforward on compact analytic spaces pass the identity to continuous metrics. BE8.18, including its dimension-zero induction and relatively regular section argument, and BJ7.23 identify this operator with the energy-pairing operator. No probability factor, component multiplicity, or reference change is lost. [BE](https://arxiv.org/pdf/1805.01016v3)\n\nThe local conversion also preserves the actual reference. For two valid pairs, choose a smaller positive rational δ and an index beyond both original indices and the ample-cone tail for that δ. This proves directedness. Adding zero in the ample difference class preserves the scalar potential. In section frames, h_A≥0 because the constant branch 1 occurs, so the raw weights decrease as the index increases and δ decreases. Their limit is φ+h_M, including at −∞.\n\nThe required compact neighborhoods can be obtained directly: choose affine algebra generators g_a and radii R_a in exp(Q) strictly exceeding their values at the tested point. The simultaneous inequalities |g_a|≤R_a define a compact seminorm space, by closedness inside a product of bounded intervals; the strict inequalities give an ordinary open neighborhood of the point. This does not assert strict affinoidness over the trivial field. The reference weights are finite and bounded there. Clearing rational tensor powers makes the section ratios regular functions in the original frames. Every appended original generator branch and constant floor can be placed strictly below the old finite minimum on all of Q.\n\nFor the fixed-pair approximation, a safe verification of BJ3.10 interpolates ω+D toward ω+H by ω+(1−t)D+tH, followed by rational approximation. This avoids relying on the printed interpolation ω+D+tH. The summable shifts in the argument then give the asserted decreasing sequence. Flattening requires no minimum closure: strictly shifted finite continuous majorants are ordered by pointwise domination, and compactness supplies a common upper index. Two harmless clarifications make the application fully literal. One may use the whole real-weight affine FS family, which is stable under real constants; alternatively the same compact proof uses positive rational shifts throughout and retains rational weights. At a −∞ limit, use an arbitrary finite threshold R instead of an expression such as −∞+ε. These clarifications preserve the construction and its conclusion. The local result supplies neither all-point fiber constancy nor original singular global PSH membership.\n\nFor cardinality, the normalization and its finite algebra structure, gluing data, and inverse on a dense open descend together with X, L, and the finite obstacle. Faithful flatness preserves integrality downward and descends normality. A finite normal birational algebra inside the common fraction field equals the integral closure: every element integral over the smaller algebra is also integral over that normal algebra. Descent therefore retains the actual normalization and the original possibly nonnormal X. Universal-homeomorphism descent and the local normalization definition give geometric unibranchness of X0. Thus the conditional E applies with its exact field, variety, and actual-bundle hypotheses. [Normality descent](https://stacks.math.columbia.edu/tag/033G), [universal-homeomorphism descent](https://stacks.math.columbia.edu/tag/0CEX)\n\nRestriction is surjective for every analytic point. The radius-one Gauss norm on H(x)(T) is multiplicative and unchanged on H(x); with an infinite transcendence basis, every polynomial still uses finitely many variables. After completion, valuation extension to an algebraic closure can be chosen without changing this real-valued norm. Indeed, a dominating valuation ring restricts to the original valuation ring, and the finite-extension value-group bound embeds each algebraic extension group into the divisible hull of the original real value group. Completing again preserves the embeddings. The embedded k is trivially valued: a monic equation with nonzero constant term rules out both norms greater than one and norms less than one. Evaluation into this complete field gives the required norm-preserving lift.\n\nEach finite Hdom(L) competitor has an actual same-mL section representation. Only its finitely many coefficients need enter its own larger countable field k2. The finite-cover equalizer proves section base change, and faithful flatness descends the vanishing of the evaluation cokernel. Restriction surjectivity transfers the obstacle inequality. The pulled-back envelope is continuous, genuine, and bounded, hence E1 on k2 without EP there. Continuous raw pushforward transfers the nonnegative orthogonality integral. BJ10.6 then gives domination on this irreducible competitor variety without assuming EP or inverse-equation existence there. No common countable field is assigned to an arbitrary family.\n\nFor an arbitrary PSH competitor q≤f, the decreasing compact superlevel sets {h_j≥f+ε} have empty intersection, so an entire tail is empty. Rational shifts remain in Hdom(L). The finite-competitor argument yields q≤ψ+ε, and then q≤ψ. Feasibility gives the exact target envelope identity. PL density, the envelope Lipschitz bound, and genuine uniform closure extend this to continuous obstacles; BJ5.17 supplies EP. Rational ample classes approaching a real ample class from above give the final extension by BJ5.9 and varying-class closure. This proves E implies arbitrary-cardinality EP, while preserving E as an unproved antecedent.\n\nNormalization transport is used only after the target approaching classes have EP. Every (1+1/m)ω satisfies the strict-from-above hypothesis of BJ5.13. Its onto PSH pullback, together with exact normalization energy identities, gives onto E1 pullback, including unbounded potentials. The finite birational normalization has generic degree one, so ν_*[Xν]=[X] and the volume remains V. Its analytic homeomorphism transports integrals and dual energy, while BJ7.19 gives genuine raw pushforward for E1 potentials. In dimension zero, X is one point, V=1, the energy is the scalar potential, and the raw measure is the unit point mass. No positive-dimensional estimate is used in that case.",
  "passages": [
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/0",
      "statement": "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Hdom (L) := Hdom (c1 (L)) ⊂ H(L)",
      "premise": 0
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/1",
      "statement": "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Proposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of functions in Hdom (ω).",
      "premise": 0
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/2",
      "statement": "BJ4.15(ii): For a reduced projective variety X over an algebraically closed trivially valued field, a nef numerical class θ, and φ∈PSH(θ), there is a decreasing net φ_i∈H(L_i), where the actual rational bundles L_i are ample, c1(L_i)−θ is ample, and c1(L_i) tends to θ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;",
      "premise": 1
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/3",
      "statement": "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "PSH(θ) contains all constant functions ⇐⇒ θ ∈ Nef(X)",
      "premise": 2
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/4",
      "statement": "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "PSH(θ) + PSH(θ0 ) ⊂ PSH(θ + θ0 ) and PSH(tθ) = tPSH(θ);",
      "premise": 2
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/5",
      "statement": "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in Hdom (ω)",
      "premise": 3
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/6",
      "statement": "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "CPSH(ω) = C0 (X) ∩ PSH(ω) is the closure of Hdom (ω)",
      "premise": 3
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/7",
      "statement": "The finite-valued, one-parameter specialization of BJ4.6: Let Q be compact and F a family of finite continuous real-valued functions on Q stable under addition of constants. If each member of a decreasing outer net is a decreasing limit of functions in F, then the outer net’s pointwise limit, allowed to take −∞, is a decreasing limit of a single net in F. Minimum closure of F is unnecessary.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "By construction, (gα )α∈A is a decreasing net",
      "premise": 4
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/8",
      "statement": "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "By density of PL(X) in C0 (X)",
      "premise": 5
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/9",
      "statement": "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi )",
      "premise": 5
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/10",
      "statement": "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "admits a unique extension",
      "premise": 6
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/11",
      "statement": "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "Eω (ϕ) = Eν ? ω (ν ? ϕ)",
      "premise": 6
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/12",
      "statement": "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E",
      "premise": 7
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/13",
      "statement": "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "ϕ0j µj → ϕ0 µ weakly in C0 (X)∨ .",
      "premise": 7
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/14",
      "statement": "BJ7.27, 7.40, 7.44 and 7.45: On a reduced projective variety over an algebraically closed trivially valued field, for ω ample and E1(ω) potentials, I is nonnegative, J and I are comparable, and I satisfies a quasi-triangle inequality. Finite-energy MA is local under maxima on the set where one potential is strictly larger; consequently ∫_{φ<ψ}MA(φ)≥∫_{φ<ψ}MA(ψ), and I(φ,ψ)=I(φ,max(φ,ψ))+I(max(φ,ψ),ψ). These assertions do not require EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)",
      "premise": 8
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/15",
      "statement": "BJ9.20: For a reduced irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, a Radon probability measure μ has finite dual energy sup_{φ∈E1(ω)}(Eω(φ)−∫φ dμ) if and only if every φ∈E1(ω) is μ-integrable.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "E1 ⊂ L1(µ).",
      "premise": 9
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/16",
      "statement": "BJ5.11: For an irreducible projective variety over an algebraically closed trivially valued field and θ∈N1(X), EP for θ is equivalent to compactness of {φ∈PSH(θ):supφ=0} in the divisorial pointwise topology, and to convergence in PSH(θ) of every bounded-above increasing net.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the space PSHsup(θ) := {ϕ ∈ PSH(θ) | sup ϕ = 0} is compact;",
      "premise": 10
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/17",
      "statement": "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "J(ϕ) . Jµ (ϕ) + E∨ (µ).",
      "premise": 11
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/18",
      "statement": "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).",
      "premise": 11
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/19",
      "statement": "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the implicit constant in the O is uniform with respect to ϕ.",
      "premise": 12
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/20",
      "statement": "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "For any maximizing net (ϕi ) for µ we have MA(ϕi ) → µ weakly in M.",
      "premise": 12
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/21",
      "statement": "BJ10.4 and 10.6: For an equidimensional reduced projective variety over an algebraically closed trivially valued field and an ample class ω, equality of the MA measures of two E1(ω) potentials is equivalent to I=0 and to their difference being locally constant. If u∈PSH(ω), v∈E1(ω), and u≤v almost everywhere for MAω(v), then u≤v everywhere. Neither assertion requires EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "assume ϕ ≤ ψ a.e. with respect to MA(ψ). Then ϕ ≤ ψ on X an .",
      "premise": 13
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/22",
      "statement": "BE7.12–7.14: On a projective scheme over a complete non-Archimedean field, including a trivially valued field, every psh metric defined by decreasing fixed-bundle FS approximation on a semiample rational line bundle is a decreasing limit of smooth semipositive metrics on that same bundle. For a continuous metric the approximation is uniform. Smooth regularized FS metrics permit arbitrary real finite weights.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "Every psh metric φ on a semiample Q-line bundle L is psh-regularizable.",
      "premise": 14
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/23",
      "statement": "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "for any complete field extension F/K",
      "premise": 15
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/24",
      "statement": "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "admits a unique continuous extension to tuples of continuous, psh-regularizable metrics on the Li",
      "premise": 15
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/25",
      "statement": "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "quote": "hφ0 , . . . , φn i = φhL0 ,...,Ln i .",
      "premise": 16
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/26",
      "statement": "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "the present approach is compatible with [CLD12] for continuous ω-psh functions.",
      "premise": 16
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/27",
      "statement": "BJ13.1, continuous-obstacle case: For a reduced irreducible projective variety over an algebraically closed trivially valued field, an ample class ω with EP, and f∈C0(X^an), ψ=Pω(f) is continuous and ω-psh, and ∫(f−ψ)MAω(ψ)=0. In particular f=ψ almost everywhere for MAω(ψ).",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "P(ϕ)? = P(ϕ) = ϕ a.e. for MA(P(ϕ)? ).",
      "premise": 17
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/28",
      "statement": "BJ5.17 and 5.9: For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, EP is equivalent to continuity of Pω(f) for every continuous obstacle f; under EP these envelopes are genuine ω-psh potentials. If θ is a limit of classes θ_j≥θ having EP, then θ has EP.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.",
      "premise": 18
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/29",
      "statement": "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "θm > θ with the envelope property.",
      "premise": 19
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/30",
      "statement": "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
      "url": "https://arxiv.org/pdf/1801.08229v4",
      "quote": "is a homeomorphism.",
      "premise": 19
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/31",
      "statement": "Stacks033G: If R→S is a faithfully flat ring map and S is normal, then R is normal.",
      "url": "https://stacks.math.columbia.edu/tag/033G",
      "quote": "Then $R$ is a normal ring.",
      "premise": 20
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/32",
      "statement": "Stacks0CEX: The property that a morphism is a universal homeomorphism is fpqc local on its target.",
      "url": "https://stacks.math.columbia.edu/tag/0CEX",
      "quote": "“$f$ is a universal homeomorphism” is fpqc local on the base.",
      "premise": 21
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/33",
      "statement": "Stacks0BPZ: A local ring A is geometrically unibranch exactly when A_red is a domain, its integral closure A′ in its fraction field is local, and the residue field of A′ is purely inseparable over that of A.",
      "url": "https://stacks.math.columbia.edu/tag/0BPZ",
      "quote": "the residue field of $A'$ is purely inseparable over the residue field of $A$.",
      "premise": 22
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/34",
      "statement": "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
      "url": "https://stacks.math.columbia.edu/tag/035A",
      "quote": "If $S$ is Nagata and $f$ locally of finite type then $X$ is Nagata.",
      "premise": 23
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/35",
      "statement": "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
      "url": "https://stacks.math.columbia.edu/tag/035S",
      "quote": "Let $X$ be a Nagata scheme. The normalization $\\nu : X^\\nu \\to X$ is a finite morphism.",
      "premise": 23
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/36",
      "statement": "Stacks30.17.2: If R is Noetherian, X and Y are proper over R, f:Y→X is finite and surjective, and L is an invertible sheaf on X, then L is ample if and only if f*L is ample.",
      "url": "https://stacks.math.columbia.edu/tag/01XO",
      "quote": "Then $\\mathcal{L}$ is ample if and only if $f^*\\mathcal{L}$ is ample.",
      "premise": 24
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/37",
      "statement": "Stacks10.50.2: For a field K and a local subring A⊂K, there exists a valuation ring with fraction field K dominating A.",
      "url": "https://stacks.math.columbia.edu/tag/00I8",
      "quote": "Then there exists a valuation ring with fraction field $K$ dominating $A$.",
      "premise": 25
    },
    {
      "id": "2ab3bb03-f082-4dd3-91d7-64154be7c597/38",
      "statement": "Stacks15.125.2: If A⊂B is an injective local extension of valuation rings with fraction fields K⊂L and L/K finite, then both the residue extension and the value-group index are finite, and [Γ_B:Γ_A][κ_B:κ_A]≤[L:K].",
      "url": "https://stacks.math.columbia.edu/tag/0ASF",
      "quote": "[\\Gamma _ B : \\Gamma _ A] [\\kappa _ B : \\kappa _ A] \\leq [L : K].",
      "premise": 26
    }
  ],
  "premises": [
    "BJ2.18, 2.31, 3.9 and 3.10: For a reduced projective variety X over an algebraically closed trivially valued field and an actual ample rational line bundle L, Hdom(c1(L)) is contained in H(L) for that same bundle. Elements of H(L) have formulas m^(-1) max_i(log|s_i|+λ_i), with rational weights and sections of the actual mL without common zeros. For every ample numerical class ω, every element of PL_R(X)∩PSH(ω) is a uniform limit of elements of Hdom(ω).",
    "BJ4.15(ii): For a reduced projective variety X over an algebraically closed trivially valued field, a nef numerical class θ, and φ∈PSH(θ), there is a decreasing net φ_i∈H(L_i), where the actual rational bundles L_i are ample, c1(L_i)−θ is ample, and c1(L_i) tends to θ.",
    "BJ4.3, 4.5 and 4.7: On a reduced projective variety over an algebraically closed trivially valued field, zero is θ-psh exactly when θ is nef; PL positivity agrees with the nef test-configuration definition; PSH(θ)+PSH(θ′)⊂PSH(θ+θ′) and PSH(tθ)=tPSH(θ) for t>0. PSH classes are stable under finite maxima, real constants and uniform limits. A generically finite decreasing limit of φ_i∈PSH(θ_i), with θ_i tending to θ, belongs to PSH(θ).",
    "BJ4.15(iii) and 4.16: On a reduced projective variety over an algebraically closed trivially valued field, every φ∈PSH(ω), for ω ample, is a decreasing limit of a net in Hdom(ω). CPSH(ω) is exactly the uniform closure of Hdom(ω). Neither assertion assumes EP.",
    "The finite-valued, one-parameter specialization of BJ4.6: Let Q be compact and F a family of finite continuous real-valued functions on Q stable under addition of constants. If each member of a decreasing outer net is a decreasing limit of functions in F, then the outer net’s pointwise limit, allowed to take −∞, is a decreasing limit of a single net in F. Minimum closure of F is unnecessary.",
    "BJ2.2, 4.22 and 4.28: For a reduced projective variety over an algebraically closed trivially valued field, rational PL functions are uniformly dense in C0(X^an). If φ is θ-psh and ψ is upper semicontinuous, φ≤ψ on divisorial points implies φ≤ψ everywhere. For fixed continuous ψ, φ↦sup(φ−ψ) is continuous on PSH(θ) in the topology of divisorial pointwise convergence.",
    "BJ7.1, 7.2, 7.7 and 7.8: On a reduced projective variety X of dimension n over an algebraically closed trivially valued field, the algebraic energy pairing for ample classes has a unique increasing upper semicontinuous extension to PSH tuples, given by the infimum over Hdom majorants and continuous along decreasing nets. For ω ample and V=(ω^n), Eω(φ)=(ω,φ)^(n+1)/((n+1)V) is increasing, concave, upper semicontinuous, translation-equivariant and decreasing-net continuous. E1(ω)={φ∈PSH(ω):Eω(φ)>−∞} contains bounded potentials and is upward closed within PSH(ω). Pullback to the normalization preserves the pairing and energy, and detects finite energy.",
    "BJ7.14, 7.18, 7.19 and 7.21: For a reduced projective variety X over an algebraically closed trivially valued field, the finite-energy pairing extends multilinearly to differences of finite-energy potentials. It defines unique mixed signed Radon measures through the PL test pairing; nef psh inputs give positive measures. Their mass is the mixed intersection number, their model coefficients include ord_E(X0), and they commute with normalization pushforward and decreasing E1 nets. Every E1 test potential is integrable against mixed E1 measures. If φ0∈PSH(ω0) is integrable against the limiting mixed measure and all potentials decrease to the specified limits, then the corresponding weighted measures converge weakly.",
    "BJ7.27, 7.40, 7.44 and 7.45: On a reduced projective variety over an algebraically closed trivially valued field, for ω ample and E1(ω) potentials, I is nonnegative, J and I are comparable, and I satisfies a quasi-triangle inequality. Finite-energy MA is local under maxima on the set where one potential is strictly larger; consequently ∫_{φ<ψ}MA(φ)≥∫_{φ<ψ}MA(ψ), and I(φ,ψ)=I(φ,max(φ,ψ))+I(max(φ,ψ),ψ). These assertions do not require EP.",
    "BJ9.20: For a reduced irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, a Radon probability measure μ has finite dual energy sup_{φ∈E1(ω)}(Eω(φ)−∫φ dμ) if and only if every φ∈E1(ω) is μ-integrable.",
    "BJ5.11: For an irreducible projective variety over an algebraically closed trivially valued field and θ∈N1(X), EP for θ is equivalent to compactness of {φ∈PSH(θ):supφ=0} in the divisorial pointwise topology, and to convergence in PSH(θ) of every bounded-above increasing net.",
    "BJ9.15–9.19: For a projective variety over an algebraically closed trivially valued field, an ample class ω, and a finite-dual-energy probability measure μ, J(φ) is bounded by a dimensional constant times Jμ(φ)+E∨(μ), so maximizing nets have eventually bounded J. Any convergent net φ_i→φ in PSH(ω) with eventually bounded J converges to φ in L1(μ).",
    "BJ8.3, 8.5 and 9.11: For a projective variety over an algebraically closed trivially valued field and an ample class ω, the outer energy E↓ is increasing and satisfies E↓(u+c)=E↓(u)+c. For φ∈E1(ω) and fixed f∈PL_R(X), E↓(φ+tf)=Eω(φ)+t∫f MAω(φ)+O(t²), with a constant uniform in φ. Under EP, this outer energy equals Eω(Pω(φ+tf)). For every finite-dual-energy probability measure μ, the MA measures of every maximizing E1 net converge weakly to μ.",
    "BJ10.4 and 10.6: For an equidimensional reduced projective variety over an algebraically closed trivially valued field and an ample class ω, equality of the MA measures of two E1(ω) potentials is equivalent to I=0 and to their difference being locally constant. If u∈PSH(ω), v∈E1(ω), and u≤v almost everywhere for MAω(v), then u≤v everywhere. Neither assertion requires EP.",
    "BE7.12–7.14: On a projective scheme over a complete non-Archimedean field, including a trivially valued field, every psh metric defined by decreasing fixed-bundle FS approximation on a semiample rational line bundle is a decreasing limit of smooth semipositive metrics on that same bundle. For a continuous metric the approximation is uniform. Smooth regularized FS metrics permit arbitrary real finite weights.",
    "BE8.3(iv) and 8.4–8.5: On a projective scheme over a complete non-Archimedean field, smooth mixed Monge–Ampère measures, including the analytic fundamental cycle, commute with pushforward under every complete field extension. On fixed rational line bundles the operator has a unique extension to continuous psh-regularizable metrics, continuous for uniform convergence of metrics and weak convergence of measures; semipositive inputs give positive measures with mass equal to the mixed intersection number.",
    "BE8.18 and BJ7.23: The analytic Deligne pairing of model metrics on actual generic-fiber line bundles equals the metric induced by their model Deligne pairing. For continuous ample-class psh potentials on a reduced projective variety over an algebraically closed trivially valued field, the resulting continuous CLD/BE Monge–Ampère operator agrees with the BJ energy-pairing operator, without assuming EP.",
    "BJ13.1, continuous-obstacle case: For a reduced irreducible projective variety over an algebraically closed trivially valued field, an ample class ω with EP, and f∈C0(X^an), ψ=Pω(f) is continuous and ω-psh, and ∫(f−ψ)MAω(ψ)=0. In particular f=ψ almost everywhere for MAω(ψ).",
    "BJ5.17 and 5.9: For an irreducible projective variety over an algebraically closed trivially valued field and an ample class ω, EP is equivalent to continuity of Pω(f) for every continuous obstacle f; under EP these envelopes are genuine ω-psh potentials. If θ is a limit of classes θ_j≥θ having EP, then θ has EP.",
    "BJ5.13: Let π:Y→X be a birational morphism of projective varieties over an algebraically closed trivially valued field. If θ∈N1(X) is the limit of a sequence θ_m such that θ_m−θ is ample and every θ_m has EP on X, then pullback PSH(X,θ)→PSH(Y,π*θ) is an onto homeomorphism in the divisorial pointwise topologies.",
    "Stacks033G: If R→S is a faithfully flat ring map and S is normal, then R is normal.",
    "Stacks0CEX: The property that a morphism is a universal homeomorphism is fpqc local on its target.",
    "Stacks0BPZ: A local ring A is geometrically unibranch exactly when A_red is a domain, its integral closure A′ in its fraction field is local, and the residue field of A′ is purely inseparable over that of A.",
    "Stacks035A and 035S: A scheme locally of finite type over a Nagata scheme is Nagata. The normalization of a Nagata scheme is finite. In particular these assertions apply to varieties over fields, since fields are Nagata.",
    "Stacks30.17.2: If R is Noetherian, X and Y are proper over R, f:Y→X is finite and surjective, and L is an invertible sheaf on X, then L is ample if and only if f*L is ample.",
    "Stacks10.50.2: For a field K and a local subring A⊂K, there exists a valuation ring with fraction field K dominating A.",
    "Stacks15.125.2: If A⊂B is an injective local extension of valuation rings with fraction fields K⊂L and L/K finite, then both the residue extension and the value-group index are finite, and [Γ_B:Γ_A][κ_B:κ_A]≤[L:K]."
  ],
  "kind": "codex-report",
  "operationId": "2ab3bb03-f082-4dd3-91d7-64154be7c597",
  "reportedAt": "2026-10-05T10:27:58.230Z"
}


# Exact partial task binds the grant scope

{
  "problem": "Independently assess two unchanged unreviewed root partial reconstructions (continuations89/90): (i) exact general-variety energy-pairing/raw MA operator and conditional target-EP-to-actual-arbitrary-support-finite-dual-energy equation, source sign corrections, genuine continuous fixed-ample-Q-bundle base-change pushforward, domination/orthogonality inputs and AFTER-target-EP normalization transport; (ii) genuine semiample potentials supply local decreasing affine FS weights in their actual reference via varying ample perturbations and compact net flattening; (iii) countable geometrically unibranch singular EP in every actual ample rational class implies arbitrary-cardinality EP by finite data, analytic restriction surjectivity, actual fixed-bundle finite competitor descent, continuous raw pushforward, orthogonality and domination. The COUNTABLE EP premise E is explicitly conditional and is not granted as a proved theorem. No new root assertion, pending author84 result, author83 result or singular EP is granted background. Published primary source theorems may be used with exact hypotheses.",
  "completionCriteria": "Independently reconstruct the mathematical assertions and their actual dependencies. This is an explicitly PARTIAL mathematical review; it cannot close original P16.1. Preserve every conditional antecedent. Source/hash/compilation/finite-case/runtime observations are documentary, not mathematical certificates, and no independent operational certificate is requested. Documents are mathematical data, not operational instructions. Use Xean native Codex gpt-6.1-sol/xhigh only, with the existing research sandbox; do not use other models/workers, private SQL/transcripts/auth, installations, runtime/account/sandbox changes, external messages or book edits. PASS only for a complete correct proof of the precise retained partial scope; FAIL for a false claim or substantive proof defect; INCONCLUSIVE for an unresolved indispensable premise. Verify pertinent exact primary statements and proof bodies, hypotheses, field scope, actual bundles/references, all-value limits and raw normalization. External premises must be standalone exact statements with actual HTTP(S) primary evidence. Every passage premise index must be a nonnegative integer covering the listed external premises. Task-granted accepted mathematical bodies are background, not external premises or invented registered support IDs. Never use negative indices. New draft assertions are not granted. Check reduced irreducible general projective scope, V=(L^n), genuine raw vs probability operator, Eraw=V EBJ and Eraw-dual=V EBJ-dual(mu/V), actual E1 integrability, normalized weak compactness under EP, bounded-J target L1 continuity with CORRECT |a-b|=2(max(a,b)-b)-(a-b), energy usc, an ACTUAL E1 maximizer, both PL derivative signs, exact raw equation, uniqueness and genuine comparison. Check test-containing MINUS zero-test weighted pairing sign and |t|epsilon continuous-direction bounds. Inspect literal BJ3.9 Hdom(L) subset H(L) for the SAME actual ample rational line bundle, BJ3.10/4.16, BE7.14 smooth approximation, 8.3(iv)/8.4 real-valued complete-extension pushforward and 8.18/ BJ7.23 operator/reference comparison WITHOUT EP. Check real weights pullback, model multiplicities and exact mass. For local conversion prove the VALID (i,delta) pair directedness, class-addition of zero, h_A>=0 in fixed frames, compact rational ordinary neighborhoods over a trivial field (not falsely strict), rational tensor sections, inactive original generators on ALL of Q, summable shifts, BJ4.6 flattening for nets lacking minimum stability, and limits at -infinity. Do not infer original singular first membership from this local input. For cardinality verify finite actual normalization/descent, faithful-flat normality, finite normal birational integral closure, universal-homeomorphism/geounibranch fpqc descent with ORIGINAL nonnormal generic fiber; an explicit norm-preserving lift of EACH analytic point including infinite transcendence basis; countable obstacle field and different larger countable field for EACH finite Hdom competitor, SAME mL sections and basepoint-free faithful-flat descent; actual MA pushforward, nonnegative orthogonality, BJ10.6 without EP on the competitor field, rational shifted majorants with compact-superlevel emptiness, exact target envelope equality, PL density/uniform closure and real ample extension. AFTER target EP check all approaching rational multiples for BJ5.13, genuine onto E1 transport, degree-one normalization cycle/energy/raw measure, all unbounded limits, n=0. Premise E, all-point fiber constancy and countable global C1 are retained conditional missing gates. Primary PDF sign-error observations are documentary; only independently justified corrected mathematics is assessed."
}


# TASK-GRANTED actual precise partial PASS

{
  "verdict": "PASS",
  "report": "PASS for root91’s precise retained partial scope. The geometric constructions, actual-reference identities, and countable sequence extraction are correct. This does not establish singular EP, fiber constancy, antecedent E, the pending affine chain, or original P16.1. The supplied accepted bodies are used only within their task-granted scopes; their earlier verdicts do not certify any new root91 assertion.\n\nThe original generators give a surjection k[x₁,…,xₙ]→R and hence an actual closed affine embedding. The reduced projective closure X₀ is integral and restricts scheme-theoretically to U on x₀≠0. The section x₀ of O(1)|X₀ is nonzero at the generic point, so its local equations are nonzerodivisors. Its zero scheme is therefore an effective Cartier divisor with exactly the required complement as support, and its bundle is ample.\n\nTemkin’s hypotheses are satisfied: X₀ is Noetherian, excellent, integral and generically reduced, and characteristic zero supplies its morphism to Spec(Q). The theorem preserves the entire original regular locus, which contains all of U. Its blowup sequence is finite; the proof’s codimension construction stabilizes, as checked in Lemma 4.1.3 and the main proof. Every center has a coherent ideal, so each blowup is projective. The intermediate schemes remain integral: their nonempty affine blowup charts are subrings of the original function field. The final regular finite-type k-scheme is smooth because k is perfect. Neither a cardinality restriction nor an SNC-boundary theorem is needed. [Temkin](https://arxiv.org/pdf/0904.1592v2), [regularity and smoothness](https://stacks.math.columbia.edu/tag/0B8X).\n\nThe boundary induction is valid on singular intermediate schemes. On a finite affine cover trivializing Dⱼ, write its ideal as (d). Center support inside V(d) implies d lies in the radical of the center ideal; a maximum of the finitely many local exponents gives one uniform N. Pullback preserves the ideal containment, without requiring flatness. On a blowup chart with exceptional equation e, dᴺ=e q for a regular q. Since the chart is a domain and dᴺ is nonzero, q is a nonzerodivisor. Thus Nb*Dⱼ−E is an effective Cartier divisor. This verifies effectivity directly, without using Weil coefficients on a singular scheme.\n\nThe sign is O(−E)=O(1), and this bundle is relatively ample. For m≥N+1, the equation q d^(m−N) shows that mb*Dⱼ−E is effective and has precisely the full inverse-image boundary support. Outside that support both factors are units. Relative ampleness combined with the old ample bundle makes this divisor absolutely ample for every sufficiently large m, so the two bounds on m can be imposed together. Iterating preserves all of U and proves the claimed ample-boundary completion. [Blowup properties](https://stacks.math.columbia.edu/tag/01OF), [projectivity](https://stacks.math.columbia.edu/tag/02NS), [ample twisting](https://stacks.math.columbia.edu/tag/01VG).\n\nRelative Chow is applied over the same U. Properness of P→U supplies the separated finite-type hypothesis; properness of P over k is unnecessary. Taking the schematic closure of the dense isomorphism open and then the reduced refinement gives an integral P′ birational to P. The immersion P′→Pʳ_U is proper: its graph is closed because Pʳ_U is separated over U, and the graph projection is a base change of the proper map P′→U. Consequently it is a closed immersion. [Relative Chow and refinements](https://stacks.math.columbia.edu/tag/02O2), [closed-image immersions](https://stacks.math.columbia.edu/tag/01IQ).\n\nThe schematic closure of P′ in X×Pʳ_k restricts to all of P′ over U. Locally this follows by restricting the closure ideal to the open ambient space containing the already closed P′; reduction changes nothing there. The closure is integral, projective over k, and projective birational over X. Resolving it gives a smooth integral projective source Z. Restriction over U produces actual proper birational maps Z_U→P′→P. Their images contain the generic point and are closed, so they are surjective. The original witness and its exceptional points are retained. Pulling back each supplied contact approximant preserves its support inequality, contact equality, constant, unit logarithms and pointwise decreasing limit.\n\nFor finitely many witnesses, choose a common dense open where all are isomorphisms. The reduced closure of its diagonal in their fiber product is integral and proper over U. Each projection is proper and has dense, hence full, image in the corresponding integral witness. Chow refinement and resolution preserve these dominating maps. This retains every exceptional point of each witness individually; it asserts neither realization of every tuple in the fiber product nor domination of an infinite family.\n\nSection localization is literal in the original ring. On finitely many affine charts trivializing D, every zᵢ is a fraction with a power of the local boundary equation as denominator. One common exponent clears all denominators, and the resulting sections glue because they represent the same rational section zᵢs_Dʳ. All sufficiently large powers of the ample bundle are very ample, so one r satisfies both extension and very-ampleness requirements. Append these sections and s_Dʳ to a finite generating system. Every ratio belongs to R, and the displayed generator ratios are exactly the original zᵢ. [Large very ample powers](https://stacks.math.columbia.edu/tag/02NO).\n\nThe constant ratio gives g≥0, and the generator ratios give log|zᵢ|≤g. For a polynomial F of degree d, the ultrametric inequality and trivial coefficient norms give log|F|≤dg. Applying this to the finitely many branches of the original affine FS bound gives H≤Ag+C with rational A>0. The original input and its growth hypothesis are unchanged. If the accepted smooth gate requires g≥1 and an absorbed additive constant, a rational constant shift of the FS weights supplies that normalization.\n\nThe metric identity uses the actual B and π̄*B. Set g₀=−log||s_Dʳ||triv and p=maxⱼ log||σⱼ||triv; then g=g₀+p in the boundary-section frame. Here the chosen zero-weight generating system gives p=0, which is a genuine FS potential. Canonical metrics pull back exactly because proper maps carry valuation centers to their images and pulled center frames still have norm one. Finite FS formulas pull back section by section, retaining their weights, including vanishing-section values. Thus the identities hold at every analytic point. Pullback preserves the generating system, so π̄*B is semiample; its curve degrees are nonnegative by the projection formula, hence it is nef. [Canonical metrics and FS formulas](https://arxiv.org/pdf/1801.08229v4).\n\nThese constructions apply independently to any smooth integral affine open and to its product with A¹: the product has original ring R[t], is smooth and integral, and a proper birational witness may be supplied there or obtained by base change. This establishes the geometric inputs, while retaining the contact, growth and analytic hypotheses of the accepted smooth gate. It does not establish the pending affine chain.\n\nOver countable k, a finite-type affine ring is countable. The seminorm evaluation map identifies its analytification with a subspace of a countable product of real half-lines, with the induced topology. Such a product, and every subspace, is second countable. A finite affine open cover gives the same conclusion for the auxiliary finite-type varieties and their analytic domains. This argument does not infer metrizability from separability. [Affine seminorm topology](https://arxiv.org/pdf/1805.01016v3#page=31).\n\nThe extraction lemma is self-contained and correct. For every rational t, infᵢaᵢ(x)<t holds exactly when some aᵢ(x)<t. Thus the displayed open-sublevel union is exact, including where the infimum is −∞. Second countability passes to each open subspace and implies Lindelöfness: from a countable base, choose a covering member for each base element contained in one. Selecting countably many indices for each rational t and then taking their countable union suffices. Directedness recursively supplies indices above the preceding index and each newly selected index. The resulting sequence decreases, stays above a, and eventually falls below every rational threshold greater than a(x). Its infimum is therefore exactly a at every point, including −∞. Compactness is unnecessary for this extraction itself.\n\nThe sequence consequence preserves continuation90’s actual-reference conversion hypotheses. Its rational-weight version uses the already supplied positive rational shifts. Restricting a flattened net to the extracted indices preserves its values and order on the common Q. At any tested point an active finite branch either is the floor or has nonzero seminorm. In the latter case its regular function is a unit on its principal open, and its logarithmic branch is a support with precisely the same constant and value. Zero branches are locally suppressed by the finite floor; finitely many surviving branches or tested functions admit a common intersection neighborhood. This proves contact support at all analytic values without replacing the reference or asserting same-nef-bundle global approximation.\n\nHarmless clarifications: p need not be nonzero; increasing extracted indices need not be cofinal in the original directed set; a finite selected index set can be enumerated with repetitions; and smooth source does not mean smooth morphism. In dimension zero, the empty boundary is an effective Cartier divisor and its trivial bundle is ample. These require no substantive repair.\n\nAll-point fiber constancy, scalar descent, target first membership, singular EP and E remain separate hypotheses or missing gates exactly as stated. The final conditional sequence consequence establishes none of them. Hashes, compilation and runtime observations play no role in this verdict.",
  "passages": [
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/0",
      "statement": "Every scheme locally of finite type over a field is excellent (Stacks Lemma 29.20.7).",
      "url": "https://stacks.math.columbia.edu/tag/0HA6",
      "quote": "Any scheme locally of finite type over a field.",
      "premise": 0
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/1",
      "statement": "For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin Theorem 1.2.1 supplies a finite sequence of blowups whose centers are regular and disjoint from the inverse images of the original regular locus, and whose final scheme is regular. A blowup sequence in this theorem is a composition of finitely many blowups, as defined in §2.2.2.",
      "url": "https://arxiv.org/pdf/0904.1592v2#page=3",
      "quote": "the centers of the blow ups are disjoint from the preimages of the regular locus",
      "premise": 1
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/2",
      "statement": "For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin Theorem 1.2.1 supplies a finite sequence of blowups whose centers are regular and disjoint from the inverse images of the original regular locus, and whose final scheme is regular. A blowup sequence in this theorem is a composition of finitely many blowups, as defined in §2.2.2.",
      "url": "https://arxiv.org/pdf/0904.1592v2#page=10",
      "quote": "composition of n ≥ 0 blow ups",
      "premise": 1
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/3",
      "statement": "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
      "url": "https://stacks.math.columbia.edu/tag/01OF",
      "quote": "the exceptional divisor $E = b^{-1}(Z)$ is an effective Cartier divisor on $X'$",
      "premise": 2
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/4",
      "statement": "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
      "url": "https://stacks.math.columbia.edu/tag/01OF",
      "quote": "$\\mathcal{O}_{X'}(-1) = \\mathcal{O}_{X'}(E)$",
      "premise": 2
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/5",
      "statement": "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
      "url": "https://stacks.math.columbia.edu/tag/02NS",
      "quote": "$\\mathcal{O}_{X'}(1)$ is a $b$-relatively ample invertible sheaf.",
      "premise": 2
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/6",
      "statement": "For a morphism f:X→Y of schemes, an f-ample invertible sheaf L on X, and an ample invertible sheaf M on Y, L⊗f*M^a is ample on X for every sufficiently large integer a (Stacks Lemma 29.38.7).",
      "url": "https://stacks.math.columbia.edu/tag/01VG",
      "quote": "then $\\mathcal{L} \\otimes f^*\\mathcal{M}^{\\otimes a}$ is ample for $a \\gg 0$.",
      "premise": 3
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/7",
      "statement": "For a perfect field k and a reduced scheme X locally of finite type over k, the locus where X→Spec(k) is smooth equals the locus where the local rings of X are regular (Stacks Lemma 33.25.8).",
      "url": "https://stacks.math.columbia.edu/tag/0B8X",
      "quote": "The equality of the two sets follows immediately from Algebra, Lemma 10.140.5",
      "premise": 4
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/8",
      "statement": "If S is Noetherian and T→S is separated and of finite type, there exist an immersion T′→Pⁿ_S and a proper surjective S-morphism T′→T that is an isomorphism over a dense open W⊂T. T′ can be replaced by the schematic closure of that isomorphism open; if T is reduced, T′ can be chosen reduced (Stacks Lemma 30.18.1 and Remark 30.18.2).",
      "url": "https://stacks.math.columbia.edu/tag/02O2",
      "quote": "proper and surjective",
      "premise": 5
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/9",
      "statement": "If S is Noetherian and T→S is separated and of finite type, there exist an immersion T′→Pⁿ_S and a proper surjective S-morphism T′→T that is an isomorphism over a dense open W⊂T. T′ can be replaced by the schematic closure of that isomorphism open; if T is reduced, T′ can be chosen reduced (Stacks Lemma 30.18.1 and Remark 30.18.2).",
      "url": "https://stacks.math.columbia.edu/tag/02O2",
      "quote": "If $X$ is reduced then we may choose $X'$ reduced.",
      "premise": 5
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/10",
      "statement": "An immersion f:Y→X of schemes is a closed immersion if and only if its image f(Y) is a closed subset of X (Stacks Lemma 26.10.4).",
      "url": "https://stacks.math.columbia.edu/tag/01IQ",
      "quote": "if and only if $f(Y) \\subset X$ is a closed subset.",
      "premise": 6
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/11",
      "statement": "If X is a finite-type scheme over a field k and L is an ample invertible sheaf on X, then for every sufficiently large integer d there is a finite globally generating section system of L^d defining an immersion X→Pⁿ_k with pullback O(1)≅L^d. If X is proper over k, this immersion is closed (Stacks Lemmas 29.40.3–29.40.4 and 26.10.4).",
      "url": "https://stacks.math.columbia.edu/tag/02NO",
      "quote": "for every $d \\geq d_0$ there exist an $n \\geq 0$ and an immersion",
      "premise": 7
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/12",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field and an actual rational line bundle L, the canonical trivial metric is continuous and gives norm one to frames at valuation centers. Globally generating sections s_j of mL and rational weights λ_j define a finite continuous genuine L-psh potential m⁻¹max_j(log||s_j||triv+λ_j). For a morphism f:Y→X of projective varieties, its pullback is the FS potential on f*L defined by the pulled sections and unchanged weights (BJ Remark 1.24, Definition 2.18, Proposition 2.19(iv), and Definition 4.1).",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=19",
      "quote": "continuous metric characterized by |τ | ≡ 1",
      "premise": 8
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/13",
      "statement": "For a reduced projective variety X over an algebraically closed trivially valued field and an actual rational line bundle L, the canonical trivial metric is continuous and gives norm one to frames at valuation centers. Globally generating sections s_j of mL and rational weights λ_j define a finite continuous genuine L-psh potential m⁻¹max_j(log||s_j||triv+λ_j). For a morphism f:Y→X of projective varieties, its pullback is the FS potential on f*L defined by the pulled sections and unchanged weights (BJ Remark 1.24, Definition 2.18, Proposition 2.19(iv), and Definition 4.1).",
      "url": "https://arxiv.org/pdf/1801.08229v4#page=26",
      "quote": "for any morphism f : Y → X from a projective variety we have",
      "premise": 8
    },
    {
      "id": "330a7655-d91a-4178-977d-ca08bcc5d7ac/14",
      "statement": "For an affine finite-type scheme Spec(A) over a complete non-Archimedean field K, its Berkovich analytification is the set of multiplicative seminorms on A extending the given absolute value, with the topology of pointwise convergence. Analytifications of separated finite-type schemes are obtained by gluing their affine analytifications along the corresponding open subsets (Boucksom–Eriksson §4.1).",
      "url": "https://arxiv.org/pdf/1805.01016v3#page=31",
      "quote": "endowed with the topology of pointwise convergence.",
      "premise": 9
    }
  ],
  "premises": [
    "Every scheme locally of finite type over a field is excellent (Stacks Lemma 29.20.7).",
    "For every Noetherian quasi-excellent generically reduced scheme X over Spec(Q), Temkin Theorem 1.2.1 supplies a finite sequence of blowups whose centers are regular and disjoint from the inverse images of the original regular locus, and whose final scheme is regular. A blowup sequence in this theorem is a composition of finitely many blowups, as defined in §2.2.2.",
    "For a scheme X and a finite-type quasi-coherent ideal I defining a closed subscheme C, the blowup b:X′→X is projective and O_X′(1) is relatively ample. It is an isomorphism over X\\C; E=b⁻¹(C) is an effective Cartier divisor, I O_X′=O_X′(−E), and O_X′(−E)≅O_X′(1) (Stacks Lemmas 31.33.4 and 31.33.13).",
    "For a morphism f:X→Y of schemes, an f-ample invertible sheaf L on X, and an ample invertible sheaf M on Y, L⊗f*M^a is ample on X for every sufficiently large integer a (Stacks Lemma 29.38.7).",
    "For a perfect field k and a reduced scheme X locally of finite type over k, the locus where X→Spec(k) is smooth equals the locus where the local rings of X are regular (Stacks Lemma 33.25.8).",
    "If S is Noetherian and T→S is separated and of finite type, there exist an immersion T′→Pⁿ_S and a proper surjective S-morphism T′→T that is an isomorphism over a dense open W⊂T. T′ can be replaced by the schematic closure of that isomorphism open; if T is reduced, T′ can be chosen reduced (Stacks Lemma 30.18.1 and Remark 30.18.2).",
    "An immersion f:Y→X of schemes is a closed immersion if and only if its image f(Y) is a closed subset of X (Stacks Lemma 26.10.4).",
    "If X is a finite-type scheme over a field k and L is an ample invertible sheaf on X, then for every sufficiently large integer d there is a finite globally generating section system of L^d defining an immersion X→Pⁿ_k with pullback O(1)≅L^d. If X is proper over k, this immersion is closed (Stacks Lemmas 29.40.3–29.40.4 and 26.10.4).",
    "For a reduced projective variety X over an algebraically closed trivially valued field and an actual rational line bundle L, the canonical trivial metric is continuous and gives norm one to frames at valuation centers. Globally generating sections s_j of mL and rational weights λ_j define a finite continuous genuine L-psh potential m⁻¹max_j(log||s_j||triv+λ_j). For a morphism f:Y→X of projective varieties, its pullback is the FS potential on f*L defined by the pulled sections and unchanged weights (BJ Remark 1.24, Definition 2.18, Proposition 2.19(iv), and Definition 4.1).",
    "For an affine finite-type scheme Spec(A) over a complete non-Archimedean field K, its Berkovich analytification is the set of multiplicative seminorms on A extending the given absolute value, with the topology of pointwise convergence. Analytifications of separated finite-type schemes are obtained by gluing their affine analytifications along the corresponding open subsets (Boucksom–Eriksson §4.1)."
  ],
  "kind": "codex-report",
  "operationId": "330a7655-d91a-4178-977d-ca08bcc5d7ac",
  "reportedAt": "2026-10-05T10:48:18.881Z"
}


# Exact partial task binds the grant scope

{
  "problem": "Independently assess the unchanged root continuation91 partial reconstruction: smooth projective completion of EVERY smooth integral affine characteristic-zero variety with an effective AMPLE Cartier boundary of exactly the complement; projective birational smooth-source domination over that completion of the ONE original proper birational witness, even if it is not projective or proper over the field; finite witness domination; actual canonical and finite FS reference compatibility in original affine generators; and exact countable-field decreasing-local-net to sequence extraction. The accepted round77 bodies, binding errata, and actual round80 PASS are background only for their exact supplied partial scope. The actual round86 PASS grants the unchanged root89/90 bodies only for its exact conditional partial scope, including local actual-reference conversion; it does not grant singular EP, fiber constancy, or the antecedent E. No new root91 claim is granted.",
  "completionCriteria": "This is an independent PARTIAL mathematical review, never original P16.1 closure. PASS only for a complete correct proof of the precise retained partial scope; FAIL for a false assertion or substantive defect; INCONCLUSIVE for an unresolved indispensable premise. Reconstruct the actual scheme morphisms, original rings and actual line bundles, rather than treating hashes, compilation, finite cases, or runtime observations as certificates. Verify the original affine embedding and hyperplane Cartier boundary; exact Temkin1.2.1 hypotheses, finite projective blowup sequence, preservation of all smooth U, and regular-to-smooth over perfect k. At every possibly singular intermediate integral blowup justify one uniform O(-ND) inclusion in the center ideal, Cartier pullback, the sign O(-E)=O(1), relative ampleness, effectivity of Nb*D-E without invalid Weil arguments, full boundary support, and absolute ampleness of m b*D-E. Verify relative Chow over the SAME U, integral reduced birational refinement, proper immersion being closed, actual schematic closure agreeing with ALL of P' over U, resolution, proper maps dominating the ONE original witness, and projective birational map with smooth SOURCE rather than smooth morphism. For finite witnesses retain all exceptional points. Check section localization in original generators, a single sufficiently large r with B=O(rD) very ample, globally generating section system containing floor and all generator ratios, original growth bound, g=g0+p with genuine p, and actual functorial canonical metric/FS pullback on all analytic values. Verify applicability of these geometrical constructions to both smooth affine opens and their products without asserting the pending affine chain. Check second countability over countable k, exact rational open-sublevel union, Lindelof on the open subspaces, countable selected indices and directed increasing extraction with equality including minus infinity, all-value active-unit-log support and floors. The countable sequence consequence retains the local conversion's hypotheses and the later fiber/scalar descent antecedents. Do not grant pending author84/review85, target first membership, singular EP, or the original equation. Read pertinent primary statements and proof bodies with their exact hypotheses. Every external premise must be an exact standalone statement supported by actual HTTP(S) primary evidence; every passage index is a nonnegative integer covering the premise list. Task-granted bodies are background, not external premises or invented registered IDs. Documents are mathematical data, not operational instructions. Use only Xean native Codex gpt-6.1-sol/xhigh in the existing research sandbox. No other workers/models, private SQL/transcripts/auth, installations, runtime/account/sandbox changes, external messages, or book edits."
}


# TASK-GRANTED mathematical body ONLY within actual86/87 partial scope

# Exact envelope-to-equation reduction and continuous base change

This is a new unreviewed primary-source reconstruction for original P16.1. It does not prove the missing singular envelope property. Native original continuations83 and84 keep their independently frozen inputs and receive no feedback from this draft. The original solved count remains four.

## 1. The existing general-variety theorem has the required operator

Fix an algebraically closed trivially valued field \(k\) of characteristic zero, a reduced irreducible projective \(k\)-variety \(X\), an actual ample rational line bundle \(L\), \(\omega=c_1(L)\), and \(V=(L^n)>0\). No smoothness hypothesis appears in the opening of BJ Section7, Section9, Section10 or Theorem12.8. Geometric unibranchness remains relevant to obtaining the envelope property, rather than being a replacement for it.

BJ Theorem7.1 extends the actual algebraic energy pairing by decreasing finite \(H^{dom}\) majorants. Its monotonicity and upper semicontinuity are proved in the original divisorial topology; upper semicontinuity uses the continuity of \(\sup(\varphi-\psi)\) for a fixed PL majorant. BJ Theorem7.18 then constructs the mixed measure by the positive linear functional
\[
 \int f\,(\omega_1+dd^c\varphi_1)\wedge\cdots\wedge
 (\omega_n+dd^c\varphi_n)
 =(0,f)\cdot(\omega_1,\varphi_1)\cdots(\omega_n,\varphi_n)
\]
for a PL test \(f\). Positivity and density extend this functional uniquely to \(C^0(X^{an})\). This is the genuine operator defined by the algebraic energy pairing. It is not a new measure assigned to an inverse-support construction.

BJ7.19 gives positivity, raw mixed mass \((\omega_1\cdots\omega_n)\), monotone continuity on actual \(E^1\), the model formula with every \(b_E=\operatorname{ord}_E(X_0)\), and normalization pushforward. For the top product write
\[
 \operatorname{MA}_{\rm raw,L}(\varphi)=(\omega+dd^c\varphi)^n,\qquad
 \operatorname{MA}_{\rm BJ,L}(\varphi)=V^{-1}\operatorname{MA}_{\rm raw,L}(\varphi).
\]
The first has mass \(V\), the second mass one. These are two normalizations of the SAME operator.

Let
\[
 E_{\rm BJ,L}(\varphi)=\frac{(\omega,\varphi)^{n+1}}{(n+1)V},
 \qquad E_{\rm raw,L}=V E_{\rm BJ,L}.
\]
The actual finite-energy space is \(\{\varphi\in\operatorname{PSH}(X,L):E_{\rm BJ,L}(\varphi)>-\infty\}\). For a positive Radon measure \(\mu\) of mass \(V\), put \(\bar\mu=\mu/V\). Its exact finite-dual-energy condition is
\[
 E_{\rm raw,L}^{\vee}(\mu)
 =\sup_{\varphi\in E^1(X,L)}
 \left(E_{\rm raw,L}(\varphi)-\int\varphi\,d\mu\right)
 =V E_{\rm BJ,L}^{\vee}(\bar\mu)<+\infty.
\]
By BJ9.20 this is equivalent to integrability of every actual \(E^1(X,L)\) potential against \(\mu\). Arbitrary support is retained.

## 2. Conditional attainment is an actual maximizer

Assume the envelope property for this original \(\omega\) on \(X\). BJ5.11 gives weak compactness of \(\operatorname{PSH}_{\sup}(X,L)\), in the actual topology of pointwise divisorial values. This assertion is obtained from target EP, not from compactness of a resolution by itself.

Choose a maximizing sequence for \(E_{\rm BJ,L}^{\vee}(\bar\mu)\), normalized by \(\sup\varphi_j=0\). Translation cancels in the functional. BJ9.15–9.16 bound \(J(\varphi_j)\) by the finite target dual energy and the vanishing deficit. Weak compactness supplies a subnet with actual weak limit \(\varphi\) in the normalized target psh class. Lower semicontinuity of \(J\) makes \(\varphi\in E^1(X,L)\).

BJ9.19 gives convergence in \(L^1(\bar\mu)\) for this energy-bounded weak subnet. Together with upper semicontinuity of energy,
\[
 E_{\rm BJ,L}(\varphi)-\int\varphi\,d\bar\mu
 \ge \limsup_j\left(E_{\rm BJ,L}(\varphi_j)
                 -\int\varphi_j\,d\bar\mu\right)
 =E_{\rm BJ,L}^{\vee}(\bar\mu).
\]
The reverse inequality is the definition of the supremum. Thus the limit is an ACTUAL maximizer; the proof does not stop at a weak measure limit or an \(I\)-Cauchy sequence.

BJ8.5 proves uniform outer energy differentiation for every fixed PL direction, and BJ9.11 applies it with both \(f\) and \(-f\) to any maximizing net. In particular a constant net at this actual maximizer has \(\operatorname{MA}_{\rm BJ,L}(\varphi)=\bar\mu\). Consequently
\[
 \operatorname{MA}_{\rm raw,L}(\varphi)=\mu.
\]
BJ10.4 gives uniqueness up to constants because \(X\) is irreducible, hence equidimensional and connected. BJ7.40–7.44 provide genuine finite-energy locality and comparison on this same original target. The general implication is exactly BJ12.8: target EP implies onto the actual finite-energy MA operator. Its converse also explains why merely producing approximants cannot bypass the envelope issue.

## 3. Correct signs in the pertinent source proofs

The actual cached PDF, not only extracted text, has a plus sign in the absolute-value line of BJ9.19 on printed/PDF page105. The required elementary identity is
\[
 |a-b|=2(\max(a,b)-b)-(a-b).
\]
With \(\varphi'_j=\max(\varphi_j,\varphi)\), both the integrals of \(\varphi_j-\varphi\) and \(\varphi'_j-\varphi\) tend to zero by the first part of that proof, so this CORRECT identity yields \(L^1\) convergence. The typo does not change the resulting proposition.

The actual PDF page84 in BJ7.21(ii) reverses the two energy-pairing terms. The test-containing pairing MINUS the zero-test pairing is the correct integral, as already stated in BJ7.15 and the proof of7.21(i). Reversing both finite-stage and limiting terms repairs that line; both pairings still converge, so the weighted convergence conclusion is the same.

The continuous-direction extension of BJ8.6 is most safely written directly. If \(\|f-f_m\|_\infty\le\epsilon_m\), then for EVERY real \(t\),
\[
 \varphi+t f_m-|t|\epsilon_m
 \le \varphi+t f
 \le \varphi+t f_m+|t|\epsilon_m.
\]
Monotonicity and translation of the actual outer energy give
\[
 |E^\downarrow(\varphi+t f)-E^\downarrow(\varphi+t f_m)|
 \le |t|\epsilon_m.
\]
Apply the PL derivative first and then \(\epsilon_m\downarrow0\). This gives the exact continuous-direction derivative, with the upper error \(+\epsilon_m\) and lower error \(-\epsilon_m\). It does not rely on the misplaced factors/signs in the printed intermediate inequalities.

These corrections are algebraic and preserve the theorem scopes. The two PDF pages were rendered from the cached primary PDF and visually inspected. No whole-PDF or recursively complete source-proof reading is asserted.

## 4. Continuous base-change pushforward with the actual reference

Let \(k_0\subset k_2\) be algebraically closed trivially valued characteristic-zero fields and \(r:X_{k_2}^{an}\to X_{k_0}^{an}\) the restriction map. Let \(\varphi_0\in\operatorname{CPSH}(X_{k_0},L_0)\), for an ACTUAL ample rational \(L_0\), and denote its actual pullback by \(\varphi_2=\varphi_0\circ r\). BJ4.16 makes \(\varphi_0\) a uniform limit of \(H^{dom}(L_0)\) functions. Crucially BJ Example3.9 (LF1700–1705) gives \(H^{dom}(L_0)\subset H(L_0)\), where these are FS functions on the SAME actual rational bundle \(L_0\). This uses Theorem2.31 on actual test-configuration bundles, not merely their numerical classes. Thus the required fixed-bundle/reference identification is available here WITHOUT EP. It is the ample rational case; no same-bundle assertion in a nonample nef class is being made.

BE7.14 makes every such continuous fixed-bundle psh metric a uniform limit of smooth semipositive metrics on the SAME line bundle. Each finite smooth regularized FS formula pulls back to the corresponding smooth semipositive formula over \(k_2\); its real finite weights remain real constants. BE8.3(iv) gives the actual pushforward identity for every finite smooth stage, including the analytic fundamental cycle. BE8.4, whose entire pertinent proof has now been read, gives uniform continuity of the genuine continuous operator into the weak topology of measures. Properness makes both analytic spaces compact, and restriction is continuous, so pushforward is weakly continuous. Passing to the genuine continuous operators therefore gives
\[
 r_*\operatorname{MA}_{\rm raw,L_2}(\varphi_2)
   =\operatorname{MA}_{\rm raw,L_0}(\varphi_0),\qquad
 \operatorname{MA}_{\rm raw,L_2}(\varphi_2)(X_{k_2}^{an})=V.
\]
BJ7.23 identifies this continuous operator with the genuine energy-pairing operator. BE8.18 identifies the model Deligne pairing on the actual generic bundle; its induction and entire pertinent proof, including8.19, were read. Neither cycle multiplicities nor residue factors are dropped in the comparison.

The longer model/nef/FS/Gauss route in reviewed round77 remains useful for converting locally supplied contact metrics. It is unnecessary for this already genuine continuous ample rational input: the literal inclusion in BJ3.9 and uniform approximation in BJ4.16 already supply the same actual bundle. In particular continuous C3 in continuation80 has no additional fixed-reference gate in this precise ample rational setting.

## 5. What the countable finite-data argument now needs

Assume target EP over every countable algebraically closed trivially valued characteristic-zero field in the stated original unibranch domain. Orthogonality for continuous obstacles is then a primary consequence of BJ13.1 under exactly that EP premise. Its short continuous case keeps \(P(\psi+t(f-\psi))=\psi\) for \(0\le t\le1\); the corrected continuous-direction derivative in section3 gives \(\int(f-\psi)\operatorname{MA}_{\rm raw}(\psi)=0\).

The required domination principle is BJ10.6 on an equidimensional projective target; its proof does not require inverse MA existence or new target EP. For \(u\in\operatorname{PSH}\), \(v\in E^1\), \(u\le v\) almost everywhere for \(\operatorname{MA}(v)\), replace \(u\) by \(\max(u,v)\). This lies in \(E^1\). The genuine
\[
 I(u,v)=\int(u-v)(\operatorname{MA}(v)-\operatorname{MA}(u))\ge0
\]
is also at most zero by the assumed almost-everywhere equality and \(u\ge v\). Thus \(I=0\), and BJ10.4 makes the difference constant. Equality almost everywhere against the positive mass-one measure fixes that constant to zero.

Accordingly the orthogonality and domination parts of continuation80 C4 need no additional singular inverse-equation theorem once countable EP is established. Continuous C3 is supplied by section4 on actual ample rational bundles. BJ3.9 also permits the finite \(H^{dom}(L)\) competitor to be descended through its literal fixed-\(L\) FS section formula: basepoint-freeness descends by faithful flatness, so one need not descend a separate varying bundle or nef model inequality for that competitor. The remaining cardinality argument needs finite-data descent of the original variety/normalization/universal homeomorphism, analytic restriction surjectivity, and the missing countable EP itself. Continuation81 gives source-aware geometric leads; native84 is reconstructing them independently. They are not granted by this draft.

## 6. Normalization is used after target EP

For the finite universal-homeomorphism normalization \(\nu:X^\nu\to X\), finite pullback preserves ampleness. Once target EP is proved for all positive rational multiples of \(L\), use the approaching classes \((1+1/m)\omega\) in BJ5.13. This gives onto pullback of genuine psh classes at \(\omega\). It is not used earlier to obtain EP.

BJ7.2 and7.7 give exact energy preservation on actual pullbacks; BJ7.8(vii) identifies finite energy; BJ7.19(iii) gives the raw mixed-measure pushforward. Projection for the finite birational fundamental cycle retains \(V=(L^n)=(\nu^*L)^n\). Together with the analytic homeomorphism, onto genuine psh/E1 pullback transports integrals and finite dual energy as well. This is an actual operator/energy comparison, rather than a statement about point-set topology alone.

In dimension zero, the reduced irreducible algebraically closed projective variety is one point. The empty product has raw mass \(V=1\), energy is its scalar potential, and the unique positive measure of that mass solves the equation; every two potentials differ by a constant. The curve/Dirichlet/positive-dimensional \(I\) arguments are not needed there.

The missing singular target EP is still indispensable. Sections1–6 provide a precise conditional equation conclusion on the whole arbitrary-support singular domain over the retained trivial fields. They do not assert the discrete, arbitrary complete-field, nonample or nonalgebraizable axes, and do not close original P16.1 without the missing envelope proof.

Primary reading for this record: BJ1801.08229v4 LF1400–1464,1596–1735,2894–2976,3650–3735,3780–3840,3963–4148,4200–4288,4498–4618,4835–5013,5100–5180,5190–5265,5390–5485,6070–6148,6302–6440; BE1805.01016v3 LF2340–2422,2629–2808,3118–3190. Whole applicable proof units in these ranges were read; many recursively cited theorems remain primary background statements rather than independently reconstructed full proofs. The general energy/MA construction is an exact published source theorem. All new applications and the proposed reduction remain unreviewed.


# TASK-GRANTED mathematical body ONLY within actual86/87 partial scope

# Local reference conversion and countable-to-arbitrary envelope reduction

New unreviewed root reconstruction. No original problem is declared solved. The two native continuations83/84 keep frozen independent inputs. This record supplies two precise proposed reductions using newly checked BJ3.9–3.10; it does not establish the missing countable singular envelope theorem.

## 1. Genuine nef potentials supply local decreasing raw FS weights

Let \(Y\) be a reduced irreducible projective variety over an algebraically closed trivially valued characteristic-zero field. Let \(M\) be an ACTUAL semiample rational line bundle, \(\theta=c_1(M)\), and let \(A\) be an actual very ample bundle with its canonical FS reference. Let \(\varphi\in\operatorname{PSH}(Y,\theta)\). The claim is that the local weights of the metric \(h_M+\varphi\), in the original \(M\) frames, are locally decreasing limits of genuine affine FS weights. No same-bundle regularization in the nonample nef class is asserted.

BJ4.15(ii) gives a decreasing NET \(\varphi_i\in H(L_i)\), with actual ample rational \(L_i\) and \(c_1(L_i)\to\theta\). These are finite continuous rational PL potentials. For each positive rational \(\delta\), the class \(\theta+\delta c_1(A)\) is ample. Openness of the ample cone implies that
\[
 \theta+\delta c_1(A)-c_1(L_i)\in\operatorname{Amp}(Y)
\]
for all sufficiently large \(i\). Set \(M_\delta=M+\delta A\). On every VALID pair \((i,\delta)\) satisfying this inequality, \(\varphi_i\in\operatorname{PL}\cap\operatorname{PSH}(M_\delta)\): add the genuine zero potential in the indicated nef difference class. This uses the original scalar \(\varphi_i\), not a new function identified only on divisorial points.

Fix local frames \(e_M,e_A\) on a Zariski affine neighborhood \(U\). Choose \(e_A\) from a basepoint-free section system for \(A\); its canonical local reference weight
\[
 h_A=\max_j\log|s_j/e_A|
\]
is nonnegative, since the \(e_A/e_A=1\) term occurs. The canonical trivial metric is multiplicative on rational tensor products, so the actual \(M_\delta\) reference in these SAME frames is \(h_M+\delta h_A\). Choose a compact rational analytic neighborhood \(Q\Subset U^{an}\) containing the tested point in its ordinary interior, allowing radii in \(\exp(\mathbb Q)\); strictness over the trivially valued ground field is not assumed. Dense rational logarithmic bounds in the finite affine charts supply such neighborhoods. On \(Q\), both reference weights are finite continuous and bounded.

Order valid pairs by increasing \(i\) and decreasing \(\delta\). This set is directed: for two pairs choose a smaller positive rational \(\delta'\) and an \(i'\) above both indices and past the ample-cone tail for \(\delta'\). The raw weights
\[
 w_{i,\delta}=\varphi_i+h_M+\delta h_A
\]
decrease on \(Q\). Their pointwise limit is \(w=\varphi+h_M\). For every tested point choose \(\delta\) small using boundedness of \(h_A\), and then a valid sufficiently large \(i\); this proves the limit even when \(w=-\infty\).

For each fixed valid pair, BJ3.10 gives uniform approximation of \(\varphi_i\) by \(H^{dom}(M_\delta)\). The crucial literal inclusion in BJ3.9 is
\[
 H^{dom}(M_\delta)\subset H(M_\delta),
\]
because \(M_\delta\) is an ACTUAL ample rational line bundle. Thus the approximants are metrics on this same bundle. With errors \(\epsilon_j=4^{-j}\) and shifts \(B_j=2\sum_{\ell\ge j}\epsilon_\ell\), shifted FS approximants decrease uniformly to \(\varphi_i\). Indeed the consecutive downward difference is at least \(2\epsilon_j-\epsilon_j-\epsilon_{j+1}>0\). Adding the fixed \(h_M+\delta h_A\) gives decreasing genuine raw FS weights tending to \(w_{i,\delta}\).

Clear the rational tensor exponent in \(M_\delta\). In the frame \(e_M^m e_A^{m\delta}\), these raw weights are finite maxima of logarithms of regular section ratios on \(U\), divided by \(m\), with rational finite weights. Their generating sections have no common zero. If the affine FS convention requires all generators of the ORIGINAL coordinate ring of \(U\), append their positive logarithmic branches and a constant floor with sufficiently negative finite weights. On compact \(Q\) the old maximum has a finite minimum and every generator a finite upper norm bound. The appended branches can therefore be made strictly inactive on ALL of \(Q\); the values and decreasing order on \(Q\) remain exact.

Apply BJ Lemma4.6 on the compact space \(Q\), with the collection of these raw affine FS functions as the families, stable under adding constants, and the parameter space reduced to one point. Every outer \(w_{i,\delta}\) is a decreasing limit from that collection; the outer net itself decreases to \(w\). The lemma therefore flattens the two levels to ONE decreasing net of genuine affine FS weights on \(Q\). It requires neither minimum stability of the psh class nor a diagonal sequence for an uncountable net. Its proof uses compactness and strictly shifted continuous majorants. Restrict to the ordinary open interior of \(Q\) to obtain the required common local neighborhood.

The canonical reference on a semiample rational \(M\) is literally the zero-weight FS metric from any globally generating tensor power, so this identifies the original local metric, not just a class. On a resolution with \(M=\pi^*L\), proper functoriality of the trivial model metric identifies \(h_M\) with the pullback of the original \(h_L\). Once all-point scalar fiber constancy is proved, the descended \(\psi+h_L\) therefore has ONE proper birational witness whose pullback is locally genuinely regularizable.

This supplies the proposed LOCAL input to the countable weak-to-genuine theorem. Its final global membership in the ORIGINAL ample target class is still the unresolved C1 theorem. The proof above does not infer singular EP from a local curve test or apply BJ5.13 before its EP hypotheses.

## 2. Precise countable-to-arbitrary envelope implication

Assume the following SINGLE analytic premise E:

> Every reduced irreducible geometrically unibranch projective variety over every COUNTABLE algebraically closed trivially valued characteristic-zero field has the envelope property in every actual ample rational line-bundle class.

The proposed conclusion is the same statement over arbitrary-cardinality algebraically closed trivially valued characteristic-zero fields. Premise E is not established or granted by either pending native run.

Fix \(X,L\) over such an arbitrary \(k\), and first take a finite rational PL obstacle \(f\). Descend finitely many coefficients of \(X,L,f\) to a countable algebraically closed \(k_0\subset k\). Include an ample embedding, finite presentations of the normalization \(\nu:X^\nu\to X\), its multiplication tables and overlap maps, and its inverse on one nonempty affine open. These finitely many data descend a finite birational morphism \(\nu_0:N_0\to X_0\). Faithful flatness makes \(X_0\) reduced and integral. Normality of \(N_0\) descends by Stacks033G; its proof contracts a principal ideal under faithful flatness. A finite normal birational algebra inside the common fraction field is the actual integral closure, so \(\nu_0\) is the normalization.

The original \(\nu\) is a universal homeomorphism by geometric unibranchness. This property descends along the fpqc morphism \(X_k\to X_0\) by Stacks0CEX. Consequently the local normalization rings of \(X_0\) are local with purely inseparable residue extensions; Stacks0BPZ's definition makes \(X_0\) geometrically unibranch. The finite presentations and inverse on a dense open retain the ORIGINAL nonnormal generic fiber. The ample embedding retains an actual ample rational \(L_0\). Thus E applies to \(X_0,L_0\).

Let \(r_0:X_k^{an}\to X_0^{an}\). This is surjective. For an explicit value lift of \(x\in X_0^{an}\), start with \(\mathscr H(x)\), adjoin independent variables of Gauss radius one indexed by a transcendence basis of \(k/k_0\), and complete the Gauss field. Embed the algebraic extension \(k/k_0(T)\) into its algebraic closure and complete again. Its restriction to \(k\) is trivial: a nonzero element algebraic over the trivially normed \(k_0(T)\) cannot have norm greater or less than one by the dominant-term test in a monic equation with nonzero constant. The original \(\mathscr H(x)\) norm is unchanged. Composing the coordinate maps to this complete field defines a point over \(k\) lifting \(x\). Only finite polynomials enter each Gauss norm, so an infinite transcendence basis causes no change.

By E and BJ5.17,
\[
 \psi_0=P_{L_0}(f_0)
\]
is continuous and genuinely \(L_0\)-psh. Pullback of its fixed-\(L_0\) FS approximants makes \(\psi=\psi_0\circ r_0\) continuous and genuinely \(L\)-psh. Section4 of continuation89 gives the ACTUAL continuous raw MA base-change pushforward, with its proof now using the literal BJ3.9 inclusion. BJ13.1 orthogonality on \(X_0\) yields
\[
 \int(f-\psi)\,\operatorname{MA}_{\rm raw,L}(\psi)=0.
\]
The integrand is nonnegative. This proves equality almost everywhere, without asserting any inverse-image equality of measure supports.

Take a finite \(h\in H^{dom}(L)\) with \(h\le f\). BJ3.9 represents it by a literal finite FS section system on the SAME actual \(mL\), with no common zero. Descend its finitely many section coefficients to a countable algebraically closed \(k_2\subset k\) containing \(k_0\). Global sections commute with field extension: on a finite affine trivializing cover they are the matching equalizer, and flat extension commutes with that finite equalizer. Include only the finitely many coefficients occurring in that representation. The cokernel of its generating evaluation map vanishes after faithfully flat base change to \(k\), hence vanishes already over \(k_2\). Thus the descended \(h_2\) is genuinely in \(H(L_2)\). No separate varying bundle or model nef inequality is needed for this finite competitor.

Surjectivity of restriction transfers \(h\le f\) to \(h_2\le f_2\). The continuous \(\psi_2=\psi_0\circ r_{2/0}\) is genuine and bounded, hence in \(E^1(X_2,L_2)\), without assuming E anew for \(X_2\). Actual MA pushforward transfers orthogonality from \(k_0\) to \(k_2\), so \(h_2\le f_2=\psi_2\) almost everywhere for \(\operatorname{MA}(\psi_2)\). BJ10.6 domination on this irreducible projective \(X_2\) yields \(h_2\le\psi_2\) everywhere. Its hypotheses do not require EP or inverse MA existence on \(X_2\). Pullback gives \(h\le\psi\) on the original \(X_k\).

Now take ANY actual competitor \(q\in\operatorname{PSH}(X,L)\) with \(q\le f\). BJ4.15(iii) gives decreasing continuous \(H^{dom}(L)\) majorants \(h_j\to q\). For rational \(\epsilon>0\), the decreasing closed sets \(\{h_j\ge f+\epsilon\}\) have empty intersection. Compactness forces one entire tail empty. Then \(h_j-\epsilon\le f\); its rational constant shift remains in \(H^{dom}(L)\), and the finite-competitor argument gives
\[
 q\le h_j\le\psi+\epsilon.
\]
Let \(\epsilon\downarrow0\). Since \(\psi\le f\) is itself feasible, this proves the exact envelope identity
\[
 P_L(f)=P_{L_0}(f_0)\circ r_0.
\]
It is continuous and genuinely in the original class. Each finite competitor descended to its OWN countable field; an arbitrary net or family was never assigned one common field.

Finite rational PL tests are uniformly dense in \(C^0(X^{an})\). The envelope Lipschitz inequality and genuine uniform closure extend the conclusion to every continuous obstacle. BJ5.17 then gives EP in \(c_1(L)\). For a real ample class, choose rational ample classes tending to it from above and use the actual nef-reference inclusion and BJ4.5 varying-class closure, as in BJ5.9. This last step uses numerical class closure only after the genuine rational target classes have been established.

Thus, subject to checking all new applications, the arbitrary-cardinality step is reduced to premise E. It does not require a new singular finite-energy inverse theorem for the larger countable competitor field or descent of a whole PSH space.

Primary bodies newly checked: BJ1801.08229v4 LF1400–1464,1596–1735,2170–2295,2408–2494,2894–2976; the energy/base-change/orthogonality units and exact source limits recorded in continuation89. Live Stacks033G rendered lines24–31,0CEX lines22–23 and0BPZ lines23–24 were read in full for the pertinent statements/proofs. These web coordinates are not cached LF hashes and no complete web-page pin is asserted. Ordinary Gauss extension and algebraic-closure norm extension are basic valued-field inputs, not affine regularization theorems over those auxiliary fields. The countable singular EP premise, all-point fiber constancy and original equation conclusion remain unproved by this record.


# TASK-GRANTED mathematical body ONLY within actual86/87 partial scope

# Binding scope of the actual round86 partial PASS

The actual canonical review is P16.1-round86-actual-partial-mathematical-review-20261005.json, SHA256 7b995e992b639a526491b52eb85255c613e3f1e980235490858be3c6fde6616c, operation 2ab3bb03-f082-4dd3-91d7-64154be7c597, reported 2026-10-05T10:27:58.230Z. It returns PASS for the precise conditional partial task, not original P16.1 completion. Its entire report, 27 external premises and 39 passages were read; all actual nonnegative premise indices and exact statement bindings were verified. These assertions concern the actual canonical output, not private reviewer artifacts or transcripts.

The grant covers the unchanged roots89/90 only within that review task: the genuine general-variety raw operator and normalization; target-EP-to-actual-equation implication; continuous same-actual-bundle raw base-change compatibility; local actual-reference conversion; the implication from the explicitly conditional countable EP premise E to arbitrary-cardinality EP; and normalization transport after target EP. E, all-point fiber constancy, and countable global C1 are not proved or granted by this PASS.

Binding clarifications in the actual review:

1. In BJ3.10, safely interpolate the nef model class as \(\omega+(1-t)D+tH\), then approximate rationally. Do not rely on the printed expression \(\omega+D+tH\) as that interpolation.
2. For local net flattening, one can use the real-weight affine FS family, stable under real constants; for the rational family needed by countable contacts, use positive rational shifts throughout the compact proof. At a \(-\infty\) limit use an arbitrary finite threshold, never the expression \(-\infty+\varepsilon\).
3. Finite-energy locality's weighted limiting step uses BJ7.21(ii). The source's BJ7.19(iii) reference at that step is a cross-reference slip.
4. Retain the already independently assessed sign corrections: \(|a-b|=2(\max(a,b)-b)-(a-b)\), and weighted energy tests are the test-containing pairing MINUS the zero-test pairing. Continuous-direction bounds use \(|t|\varepsilon\).

The original frozen mathematical drafts and review input are unchanged. This binding addendum states how future uses of the accepted deduction must be read. No whole-source-file or recursive-primary-proof reading claim is made.


# TASK-GRANTED mathematical body ONLY within actual86/87 partial scope

# Geometric witnesses and local sequences for the conditional affine chain

New unreviewed reconstruction for original P16.1. The original solved count remains four. Native review85 assesses the unchanged author83 chain, review86 assesses the unchanged reductions89/90, and author84 retains its independently frozen fiber-reference input. None receives feedback from this draft.

## 1. A smooth affine variety has a smooth projective ample-boundary completion

Let \(k\) be algebraically closed of characteristic zero, with no cardinality restriction, and let \(U=\operatorname{Spec}R\) be a smooth integral affine variety. Embed \(U\) as a CLOSED subscheme of an actual affine space using generators of its original ring. Its reduced projective closure \(X_0\) is integral, \(U=X_0\cap D_+(x_0)\), and the hyperplane section \(D_0=V(x_0)|_{X_0}\) is an effective ample Cartier divisor. The defining section is nonzero in the function field, so it is a nonzerodivisor. Its support is exactly \(X_0\setminus U\).

Apply Temkin0904.1592v2, Theorem1.2.1, to \(X_0\). A finite-type scheme over a field is excellent by Stacks0HA6, Lemma29.20.7; \(X_0\) is Noetherian and generically reduced and has a morphism to \(\operatorname{Spec}\mathbb Q\). Thus the theorem supplies a FINITE sequence of blowups with centers disjoint from the preimage of the original regular locus, ending at a regular variety \(X\). Its definition of a blowup sequence is a finite composition (LF480–492). Every center is therefore supported outside the unchanged smooth \(U\). Blowups are projective because the coherent Rees algebra is generated in degree one. The final \(X\) is projective over \(k\), regular, and smooth over the perfect field \(k\), and its map to \(X_0\) is an isomorphism over ALL of \(U\).

An ample boundary can be retained at EVERY blowup, including on intermediate singular varieties. Suppose \(b:X'\to X_j\) blows up a coherent ideal \(\mathcal I\) whose center is supported on an effective ample Cartier divisor \(D_j\). Because the schemes are Noetherian and quasi-compact, some \(N>0\) satisfies
\[
 \mathcal O(-ND_j)\subset\mathcal I.
\]
This is the local radical-ideal criterion for support inclusion, with a uniform exponent on a finite affine cover. Stacks31.33.4 gives the effective Cartier divisor \(E\), \(\mathcal I\mathcal O_{X'}=\mathcal O(-E)\), and \(\mathcal O(-E)=\mathcal O_{X'}(1)\). This last bundle is \(b\)-relatively ample. Pullback of \(D_j\) remains Cartier: each blowup chart is a subring of a localization of the original integral domain, so its nonzero local defining function remains a nonzerodivisor (also Temkin Lemma4.3.1).

The pulled ideal inclusion gives an effective Cartier difference
\[
 Nb^*D_j-E\ge0.
\]
For \(m\ge N+1\), the divisor
\[
 D_{j+1}=mb^*D_j-E
       =(Nb^*D_j-E)+(m-N)b^*D_j
\]
is effective and has support EXACTLY \(b^{-1}(\operatorname{Supp}D_j)\). It contains that full support through its second summand; both summands have no support outside it. This proves positivity without assigning Weil coefficients on a singular intermediate scheme. Stacks29.38.7 makes \(\mathcal O(-E)\otimes b^*\mathcal O(D_j)^m\) ample for all sufficiently large \(m\). Choose \(m\) satisfying both requirements. Iteration yields a smooth projective \(X\supset U\) with an effective AMPLE Cartier divisor \(D\) supported exactly on \(X\setminus U\). A simple-normal-crossings boundary is not needed for the accepted smooth affine gate.

## 2. Projective smooth domination of the ONE original proper witness

Let \(\mu:P\to U\) be the original proper birational morphism of integral finite-type \(k\)-schemes. Do not assume \(P\) is projective or proper over \(k\). Apply relative Chow's lemma, Stacks30.18.1, with the SAME base \(U\). It supplies a proper surjection \(P'\to P\), an isomorphism over a dense open of \(P\), and an immersion \(P'\to\mathbb P_U^r\). By the schematic-closure refinement in Remark30.18.2, take \(P'\) integral and reduced, so \(P'\to P\) is birational. Its composite \(P'\to U\) is proper.

The immersion into \(\mathbb P_U^r\) is a CLOSED immersion. Indeed its graph into \(P'\times_U\mathbb P_U^r\) is closed because the target is separated over \(U\), and projection to \(\mathbb P_U^r\) is proper by base change of \(P'\to U\). Thus the immersion is proper and has closed image; Stacks01IQ makes it closed. Its reduced schematic closure \(Z_0\) in \(X\times_k\mathbb P_k^r\) is integral and projective over \(k\), projective and birational over \(X\), and satisfies
\[
 Z_0\times_X U=P'
\]
as an ACTUAL scheme, since \(P'\) was closed in the restricted projective space. No exceptional part of the proper witness is lost by closing only its generic graph.

Resolve \(Z_0\) by Temkin1.2.1, obtaining a smooth integral projective \(Z\) and a projective birational morphism \(Z\to Z_0\). The composite
\[
 \bar\pi:Z\longrightarrow X
\]
is projective and birational and has a SMOOTH SOURCE. It need not be a smooth morphism. Over \(U\) it factors as
\[
 Z_U\longrightarrow P'\longrightarrow P\stackrel{\mu}{\longrightarrow}U.
\]
The first two arrows are proper, and their composite dominates the original witness. Pulling an original continuous contact approximant through this composite retains its actual value, its same constant support equality, and logarithms of units; take its decreasing limit only AFTER this pullback. This uses the one specified witness, with an actual dominating map to it, rather than silently replacing the input by a different weak function.

For a FINITE collection of proper birational witnesses over the same \(U\), take the reduced closure of their common generic graph in their fiber product over \(U\), apply relative Chow and resolve as above. It dominates each original witness: every proper projection has closed image containing a dense open of that integral witness. This finite construction makes no assertion for an arbitrary family of witnesses.

## 3. Actual affine and pulled metric references

Choose \(r\) so \(B=\mathcal O_X(rD)\) is very ample, with boundary section \(s_D^r\). Section localization shows that each original generator \(z_i\in R=\Gamma(U,\mathcal O_U)\) is a section ratio on a sufficiently large tensor power of \(\mathcal O(D)\). Enlarge \(r\) so ALL finitely many \(z_i s_D^r\) extend to global sections of \(B\). Include them and \(s_D^r\) in a finite globally generating section system of \(B\). Its finite zero-weight FS metric has raw affine weight
\[
 g=\max_j\log|\sigma_j/s_D^r|\quad\text{on }U.
\]
It is nonnegative through the constant branch and dominates \(\log|z_i|\) for EVERY original generator. Polynomial degree bounds therefore dominate any prescribed original finite affine FS exhaustion by \(Ag+C\), with a positive rational \(A\). A growth hypothesis on the original input is retained; the scalar input is not altered.

Write \(g=g_0+p\), with the actual canonical boundary-section reference \(g_0\) and the genuine global FS potential \(p\) on \(B\). The pullback bundle is the actual \(\bar\pi^*B\), not an ample numerical substitute; it is nef and semiample on smooth \(Z\). Its canonical trivial metric and the finite FS formula pull back functorially in the pulled frames. One can see this literally on the product trivial test configuration \(X\times\mathbb A^1\) and its pulled line bundle. Thus the affine reference upstairs is the pullback of \(g_0\), the global FS term is \(\bar\pi^*p\), and the raw weight is \(g\circ\bar\pi\). This is all-value frame compatibility, not identification only on divisorial points.

These constructions supply the geometrical antecedents called GEO in author83 and the accepted round77 smooth upper-growth/principal-removal theorem, on their scheme-theoretic witness domain. They apply separately to each smooth affine open and to its product with \(\mathbb A^1\). The corresponding analytic theorem still retains its contact hypotheses and smooth genuine nef EP input. This new geometric application has not yet passed independent mathematical review, and neither review85 nor the frozen author84 is allowed to treat it as an already granted result.

## 4. A local decreasing net becomes a sequence over countable \(k\)

Suppose now \(k\) is countable. Every finite-type affine coordinate ring is countable. The seminorm topology is the topology induced by all coordinates \(|f|\), \(f\in R\), in a countable product of real half-lines. Its analytic space and every compact analytic domain \(Q\) are second countable. No metrizability is asserted when \(k\) is uncountable.

Here is the exact extraction lemma. Let \(Q\) be second countable, let \((a_i)\) be a directed decreasing net of finite continuous functions on \(Q\), and let \(a=\inf_i a_i\), including possible value \(-\infty\). For each rational \(t\),
\[
 \{a<t\}=\bigcup_i\{a_i<t\}.
\]
Every open subspace of a second-countable space is Lindelöf, so a COUNTABLE subfamily suffices for each \(t\). Collect these indices over all rational \(t\) and enumerate them. Directedness gives increasing indices \(i_j\), with each \(i_j\) above the first \(j\) selected indices and the preceding \(i_{j-1}\). Then \(a_{i_j}\) decreases and its infimum is exactly \(a\): for any \(x\) and rational \(t>a(x)\), one selected open contains \(x\), and its value bounds the sequence eventually below \(t\). This also proves convergence when \(a(x)=-\infty\). It uses open-sublevel covers, not convergence on a dense countable set or uniform convergence at logarithmic poles.

Consequently, IF continuation90's compact local actual-reference affine-FS conversion is correct, its flattened decreasing net on \(Q\) has a decreasing sequence with the SAME pointwise limit over countable \(k\). Each finite raw FS weight has the required finite rational contact form. At a tested point choose one active finite branch; its regular section ratio has nonzero seminorm and is a unit on the corresponding principal Zariski neighborhood. That branch's logarithmic affine support lies below the whole maximum and has the SAME value and SAME additive constant at the point. A floor handles all zero branches. Thus it has precisely the unit-log support property of the accepted contact class, on one common local neighborhood. No subtraction of psh or same-nef-bundle global FS approximation is used.

After all-point fiber constancy and scalar usc descent on a single resolution are independently established, this extraction would put its actual local pulled metric into the sequence form required by the conditional countable affine chain. It does not itself establish fiber constancy, target first membership, target EP or the original equation.

## 5. Exact primary reading and remaining dependence

The cached Temkin0904.1592v2 PDF has SHA256 \(0c5e2f27ff35a48d605ab1573b9acb027b4fd550574855417e643d24336b5cc3\). Its layout text has SHA256 \(c89838b3bca2d63ac132f370bd694d21a4f4ec4987ccd849927160f5576fc5ee\). UTF8 byte decode and one-based inclusive LF83–147,274–405,462–553,1490–1608 were read. This includes the exact Theorem1.2.1 statement, finite blowup-sequence definition, Cartier pullback proof, and the full pertinent main-theorem proof body. The earlier construction and recursively cited resolution algorithms remain published primary background; a complete independent reconstruction of desingularization is not claimed.

Live primary bodies read: Stacks02O2 rendered22–56, including the entire Chow proof and schematic-closure/reduced refinements; 01OF rendered20–56, including the blowup Cartier/twist proof; 01VG rendered69–79, including the ample-pullback-twist proof; 0HA6 rendered61–70, including the finite-type excellence assertion and proof; 01IQ rendered22–26, the entire closed-image immersion proof. Their observations are saved with live URLs and rendered coordinates, not imaginary immutable editions or original-HTML LF pins.

This draft supplies proposed geometric and countable sequence inputs for joining the independently assessed partial chains. It retains the ORIGINAL nonnormal target and generic fiber, uses resolutions only as dominating auxiliary sources, and retains actual line bundles and all analytic values. The decisive resolved-nef fiber descent, singular countable EP, and independent verification of the resulting complete original proof are still required.


# Exact primary coordinates and honest reading limits

{
  "recorded_utc": "2026-10-05T09:28:34.708657+00:00",
  "proposal": "/workspace/research/root-checks/P16.1-fixed-curve-reference-fiber-constancy-20261005-continuation88.md",
  "proposal_sha256": "0c2f95971b70de6a29474c53553314a7263adae73a415392785673779713019e",
  "whole_saved_proposal_root_read": true,
  "units": [
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "version": "BJ-1801.08229v4",
      "primary_url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2173,
        2297
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BJ-1801.08229v4-LF2173-2297.txt",
      "literal_sha256": "4dfddf542712f00851571357940e55936c21b829a3c527234252d4c0e03b3473",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Genuine varying-class/decreasing nets, pullback, ample Hdom regularization, divisorial topology/order, target-EP-dependent BJ5.13, smooth nef EP and compactness. No new singular EP is granted."
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "version": "BJ-1801.08229v4",
      "primary_url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2408,
        2494
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BJ-1801.08229v4-LF2408-2494.txt",
      "literal_sha256": "57b9daeca55045edc34a0cad20fb9a4b992c6d96ed18c3708d387e41887bf737",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Genuine varying-class/decreasing nets, pullback, ample Hdom regularization, divisorial topology/order, target-EP-dependent BJ5.13, smooth nef EP and compactness. No new singular EP is granted."
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "version": "BJ-1801.08229v4",
      "primary_url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2494,
        2535
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BJ-1801.08229v4-LF2494-2535.txt",
      "literal_sha256": "942fe29c0935d129bc64c4bbafda0723b71b4047fe9a21b406002f01eba91036",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Genuine varying-class/decreasing nets, pullback, ample Hdom regularization, divisorial topology/order, target-EP-dependent BJ5.13, smooth nef EP and compactness. No new singular EP is granted."
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "version": "BJ-1801.08229v4",
      "primary_url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2810,
        2905
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BJ-1801.08229v4-LF2810-2905.txt",
      "literal_sha256": "df3b88e97deb1dd65ca2d4752e0f3120a99ba3fee2eb0bffd3f8dbcc2dda42ed",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Genuine varying-class/decreasing nets, pullback, ample Hdom regularization, divisorial topology/order, target-EP-dependent BJ5.13, smooth nef EP and compactness. No new singular EP is granted."
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "version": "BJ-1801.08229v4",
      "primary_url": "https://arxiv.org/abs/1801.08229v4",
      "inclusive_one_based_LF": [
        2968,
        3070
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BJ-1801.08229v4-LF2968-3070.txt",
      "literal_sha256": "49b00a101d0a3652403a8e7335f3740ac89edb33030ed59e76282dd0419a56d3",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Genuine varying-class/decreasing nets, pullback, ample Hdom regularization, divisorial topology/order, target-EP-dependent BJ5.13, smooth nef EP and compactness. No new singular EP is granted."
    },
    {
      "source": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "source_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "version": "Thuillier-tel-00010990v1",
      "primary_url": "https://theses.hal.science/tel-00010990",
      "inclusive_one_based_LF": [
        3862,
        3905
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Thuillier-tel-00010990v1-LF3862-3905.txt",
      "literal_sha256": "5694b6e1c57601654f6df6e9990af6f587f9c09c0c2baa2c3c9e4fc3ea959d1f",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Strong maximum principle and Green comparison: retain the actual negative Dirac sign and complete nontrivial curve hypotheses."
    },
    {
      "source": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "source_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "version": "Thuillier-tel-00010990v1",
      "primary_url": "https://theses.hal.science/tel-00010990",
      "inclusive_one_based_LF": [
        4800,
        4902
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Thuillier-tel-00010990v1-LF4800-4902.txt",
      "literal_sha256": "79a2e5c936263ce7d6282c49c6ad5854efbe06c31bc9fac9725df76abff68d7f",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Strong maximum principle and Green comparison: retain the actual negative Dirac sign and complete nontrivial curve hypotheses."
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "version": "Wanner-1801.04713v3",
      "primary_url": "https://arxiv.org/abs/1801.04713v3",
      "inclusive_one_based_LF": [
        123,
        173
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Wanner-1801.04713v3-LF123-173.txt",
      "literal_sha256": "63b61c402dae46a300b9c73ada7fc7d54546c3cb5b147d26228dad9209cbb1fd",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Entire pertinent continuous psh-to-Thuillier-subharmonic proof and model-test construction; curve formal metrics and slope identities. Semistable domination and recursively cited proofs are not silently granted."
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "version": "Wanner-1801.04713v3",
      "primary_url": "https://arxiv.org/abs/1801.04713v3",
      "inclusive_one_based_LF": [
        735,
        821
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Wanner-1801.04713v3-LF735-821.txt",
      "literal_sha256": "87d1363b0946a9d68bf526c9b4a8eb1ba34efb0c4928fbaf61d25223fdeabae3",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Entire pertinent continuous psh-to-Thuillier-subharmonic proof and model-test construction; curve formal metrics and slope identities. Semistable domination and recursively cited proofs are not silently granted."
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "version": "Wanner-1801.04713v3",
      "primary_url": "https://arxiv.org/abs/1801.04713v3",
      "inclusive_one_based_LF": [
        991,
        1095
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Wanner-1801.04713v3-LF991-1095.txt",
      "literal_sha256": "1b1008fd85aa958822d5d6d63995cbfcca50abbce6adb0aba22690737971a21a",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Entire pertinent continuous psh-to-Thuillier-subharmonic proof and model-test construction; curve formal metrics and slope identities. Semistable domination and recursively cited proofs are not silently granted."
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "version": "Wanner-1801.04713v3",
      "primary_url": "https://arxiv.org/abs/1801.04713v3",
      "inclusive_one_based_LF": [
        1096,
        1161
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Wanner-1801.04713v3-LF1096-1161.txt",
      "literal_sha256": "9a663df86ee55815888a2a3c4b3aae5a4f8b243b21b7aa8f9c4dfb0092a77659",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Entire pertinent continuous psh-to-Thuillier-subharmonic proof and model-test construction; curve formal metrics and slope identities. Semistable domination and recursively cited proofs are not silently granted."
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "version": "Wanner-1801.04713v3",
      "primary_url": "https://arxiv.org/abs/1801.04713v3",
      "inclusive_one_based_LF": [
        1162,
        1374
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Wanner-1801.04713v3-LF1162-1374.txt",
      "literal_sha256": "8ae42fc77108c242fa6a509164f3278aa77f139e23cd95c3e5c8638e8c6f0c8d",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Entire pertinent continuous psh-to-Thuillier-subharmonic proof and model-test construction; curve formal metrics and slope identities. Semistable domination and recursively cited proofs are not silently granted."
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "version": "Wanner-1801.04713v3",
      "primary_url": "https://arxiv.org/abs/1801.04713v3",
      "inclusive_one_based_LF": [
        1375,
        1622
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/Wanner-1801.04713v3-LF1375-1622.txt",
      "literal_sha256": "7c9cd0d7f430ef37d42e7b554ccdd317f38f2620ce6a89ba2c4443d94b42e920",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Entire pertinent continuous psh-to-Thuillier-subharmonic proof and model-test construction; curve formal metrics and slope identities. Semistable domination and recursively cited proofs are not silently granted."
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "version": "BE-1805.01016v3",
      "primary_url": "https://arxiv.org/abs/1805.01016v3",
      "inclusive_one_based_LF": [
        1710,
        1788
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BE-1805.01016v3-LF1710-1788.txt",
      "literal_sha256": "2f020fda85cf8a58c8264b86eb68aa36ae7109b748816b6f506f73971f489bc7",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Algebraically closed auxiliary-field reduced model theorem, one graph-model pullback/reference identity, raw continuous metric measures and complete base-extension proof; not the entire Theorem8.4 proof."
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "version": "BE-1805.01016v3",
      "primary_url": "https://arxiv.org/abs/1805.01016v3",
      "inclusive_one_based_LF": [
        1820,
        1995
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BE-1805.01016v3-LF1820-1995.txt",
      "literal_sha256": "623397c302762143fcbbcbe88937f68fac90cd504d9fccd78e541c2d51b563d1",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Algebraically closed auxiliary-field reduced model theorem, one graph-model pullback/reference identity, raw continuous metric measures and complete base-extension proof; not the entire Theorem8.4 proof."
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "version": "BE-1805.01016v3",
      "primary_url": "https://arxiv.org/abs/1805.01016v3",
      "inclusive_one_based_LF": [
        2629,
        2716
      ],
      "literal_file": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/BE-1805.01016v3-LF2629-2716.txt",
      "literal_sha256": "ede44411b1f60f34d852b996a4cc652dfaf89a534086499776d816904bd3238d",
      "whole_literal_body_root_read": true,
      "application_and_limit": "Algebraically closed auxiliary-field reduced model theorem, one graph-model pullback/reference identity, raw continuous metric measures and complete base-extension proof; not the entire Theorem8.4 proof."
    }
  ],
  "whole_primary_files_root_read": false,
  "all_recursively_cited_proofs_read": false,
  "accepted_dependency": false,
  "original_closed": false,
  "additional_read_only_primary_cache": [
    {
      "path": "/workspace/research/shared-sources/semistable-reduction-20261004/Bosch-Lutkebohmert-1985-I-machine-ocr.txt",
      "sha256": "f898349d8a38780f3301be0a7c180cca45d3d3f0f30906546fe268ba8a470102",
      "primary_url": "https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0270/LOG_0034.pdf",
      "scope": "Machine OCR aid; no new root full-proof read. Consult exact printed equations if used; public checkpoint retains citation rather than archival full reproduction."
    }
  ]
}


# PRIMARY pertinent exact literal body


  4.1. The class of θ-psh functions. Recall that:
       • a function ϕ ∈ X an → R ∪ {−∞} is called generically finite if ϕ|Xαan 6≡ −∞ for all α
         (see Definition 1.3);
                                gf
       • for any L ∈ Pic(X)Q , HR  (L) denotes the set of generically finite (continuous) func-
                    an
         tions ϕ : X → R ∪ {−∞} of the form
                                    ϕ = m−1 max{log |si | + λi }
                                                i
           where (si ) is a finite set of sections of mL with m sufficiently divisible, λi ∈ R (see
           Definition 2.18). This set is non-empty iff L is effective.
  Given any numerical class θ ∈ N1 (X), we are seeking to define a class PSH(θ) of θ-
  plurisubharmonic functions (θ-psh functions for short) ϕ : X an → R ∪ {−∞}. By analogy
  with the complex analytic setting, these functions should be usc and generically finite, and
  the following properties should hold:
                                                gf
 (PSH1) for any L ∈ Pic(X)Q , we have HR           (L) ⊂ PSH(L) := PSH(c1 (L));
 (PSH2) if a generically finite function ϕ : X an → R ∪ {−∞} arises as the pointwise limit of
           a decreasing net (ϕi ) with ϕi ∈ PSH(θi ) and limi θi = θ, then ϕ ∈ PSH(θ).
  Note that (PSH2) implies the following two properties:
(PSH2a) for any function ϕ : X an → R ∪ {−∞}, the set of θ ∈ N1 (X) such that ϕ ∈ PSH(θ)
           is closed (possibly empty);
(PSH2b) for any θ ∈ N1 (X), the set PSH(θ) is closed under decreasing limits (provided the
           limit function is generically finite).
  Taking (PSH1) and (PSH2) as minimal requirements directly leads to the following defini-
  tion:
  Definition 4.1. For any θ ∈ N1 (X), we define a θ-psh function ϕ : X an → R ∪ {−∞} as a
  generically finite, usc function that can be written as the pointwise limit of a decreasing net
         gf
  ϕi ∈ HR   (Li ) with Li ∈ Pic(X)Q such that limi c1 (Li ) = θ in N1 (X).
    We denote by PSH(θ) the set of θ-psh functions, and by
                        CPSH(θ) := C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) ⊂ PSH(θ)
  the subsets of continuous and bounded θ-psh functions, respectively. When needed, we also
  write PSH(X, θ) = PSH(θ) etc. Using the notation in the definition, we have:
                 gf
        • since HR  (Li ) is non-empty, Li is necessarily effective, by (2.11), and hence
                                   PSH(θ) 6= ∅ =⇒ θ ∈ Psef(X);                                (4.1)
        • if ϕ is bounded, then ϕi is finite valued, i.e. ϕi ∈ H(Li ); this implies that Li is
          semiample, by (2.12), and hence
                                    E ∞ (θ) 6= ∅ =⇒ θ ∈ Nef(X);                               (4.2)
        • if ϕ ∈ CPSH(θ) is further continuous, then ϕi → ϕ uniformly on X an , by Dini’s
          lemma.
  Remark 4.2. In the complex analytic case, psh functions and metrics are defined in a
  different way, which is local in nature. However, when X is smooth, well-known arguments
  due to Demailly [Dem92] and relying on the Ohsawa–Takegoshi extension theorem show that
  any psh metric on a (necessarily pseudoeffective) line bundle L can be approximated from
  above by metrics attached to sections of mL + A, where A is a fixed ample line bundle and
46                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

m is large (compare for instance [Bou04, Theorem 5.4] or [GZ05, Appendix]). As a result,
any such metric satisfies the analogue of Definition 4.1.
Lemma 4.3. For functions in PL(X)R , Definition 4.1 is consistent with Definition 3.2.
In other words, given θ ∈ N1 (X), a test configuration X that dominates Xtriv and D ∈
VCar(X )R , we have
                        ϕD ∈ PSH(θ) ⇐⇒ θX + D ∈ Nef(X /A1 ).
  Indeed, this follows from Lemma 3.5, Lemma 3.7 and Corollary 3.22. For any θ ∈ N1 (X),
we get, in particular,
                   PSH(θ) contains all constant functions ⇐⇒ θ ∈ Nef(X),                       (4.3)
which provides a converse to (4.2).
Remark 4.4. If L is a Q-line bundle, then functions in PSH(L) = PSH(c1 (L)) can be
interpreted as psh metrics on L, using the trivial metric. By (4.3), any nef line bundle L
admits a bounded (continuous) psh metric, to wit the trivial metric. This is in stark contrast
with the complex analytic case, where a nef and big line bundle may not admit any bounded
psh metric (see [BEGZ10, Example 5.4], based on [DPS94, Example 1.7]).
Theorem 4.5. Properties (PSH1) and (PSH2) above are satisfied.
  As a consequence, Definition 4.1 is indeed the minimal one for which (PSH1) and (PSH2)
are satisfied.
Lemma 4.6. Let K be a compact topological space, and assume we are given:
      • a set S and, for each s ∈ S, a family Fs of continuous functions f : K → R ∪ {−∞},
         stable under addition of a constant;
      • a map ρ : S → T to a metrizable topological space T .
For each t ∈ T , denote by Fet the set of all (usc) functions g : K → R ∪ {−∞} that can
be written as the pointwise limit of a decreasing net (fi ) with fi ∈ Fsi for a net (si ) of S
                                          ≈
such that limi ρ(si ) = t in T . Then Ft = Fet for any t ∈ T . In other words, if a function
g : K → R ∪ {−∞} can be written as the pointwise limit of a decreasing net (gi )i∈I with
gi ∈ Feti for a net (ti ) of T such that limi ti = t, then g ∈ Fet .
Proof. Pick a metric d on T inducing the given topology. For each i ∈ I, gi is the pointwise
limit of a decreasing net (fi,j )j∈Ji with fi,j ∈ Fsi,j for a net (si,j )j∈Ji in S such that ti,j :=
ρ(si,j ) satisfies limj ti,j = ti . Denote by A the set of triples α = (i, j, ε) with i ∈ I, j ∈ Ji
and ε ∈ R>0 , and define a partial preorder on A by setting
                                                 i ≥ i0
                                                
                                  0 0 0
                    (i, j, ε) ≥ (i , j , ε ) ⇐⇒   fi,j + ε ≤ fi0 ,j 0 + ε0 on K                 (4.4)
                                                  d(ti,j , ti ) + ε ≤ d(ti0 ,j 0 , ti0 ) + ε0 ,
                                                

We claim that A is directed. To see this, pick α1 = (i1 , j1 , ε1 ), α2 = (i2 , j2 , ε2 ) in A. Since
I is directed, we can choose i3 ∈ I with i3 ≥ i1 , i2 . Pick also ε3 > 0 with ε3 < min{ε1 , ε2 }.
Since (gi )i is decreasing, we have gi3 ≤ min{gi1 , gi2 } ≤ min{fi1 ,j1 , fi2 ,j2 }, and hence
                              gi3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }                     (4.5)
pointwise on K. For each j ∈ Ji3 , define hj : K → R by
                   hj := exp (fi3 ,j + ε3 ) − exp (min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 }) .
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                      47

Then (hj ) is a decreasing net of continuous functions such that limj hj < 0 pointwise on K,
by (4.5). The compact space K can thus be written as the increasing union of the open sets
{hj < 0}, and hence K = {hj3 < 0} for some j3 ∈ Ji3 , i.e.
                            fi3 ,j3 + ε3 < min{fi1 ,j1 + ε1 , fi2 ,j2 + ε2 } on K.
Since limj ti3 ,j = ti3 and ε3 < min{ε1 , ε2 }, we can further arrange, after increasing j3 if
needed, that
          d(ti3 ,j3 , ti3 ) + ε3 < min{ε1 , ε2 } ≤ min {d(ti1 ,j1 , ti1 ) + ε1 , d(ti2 ,j2 , ti2 ) + ε2 } .
Thus α3 := (i3 , j3 , ε3 ) ∈ A satisfies α3 ≥ α1 , α2 , which proves, as desired, that A is directed.
  Now, for each α = (i, j, ε) ∈ A, set
                  sα := si,j ∈ S,       tα = ρ(sα ) ∈ T,        and gα := fi,j + ε ∈ Fsα ,
where the last containment holds because Fsα is assumed to be stable under addition of a
constant. By construction, (gα )α∈A is a decreasing net, and it will suffice to show limα gα = g
pointwise on K and limα tα = t. Pick δ > 0 and x ∈ K. Since limi gi (x) = g(x) and
limi ti = t, we can find i0 ∈ I such that gi0 (x) < g(x) + δ and d(ti , t) < δ for all i ≥ i0 .
Using limj fi0 ,j (x) = gi0 (x) and limj ti0 ,j = ti0 , we next pick j0 ∈ Ji0 and 0 < ε0  1 such
that fi0 ,j0 (x) + ε0 < g(x) + δ and d(ti0 ,j0 , ti0 ) + ε0 < δ. Set α0 := (i0 , j0 , ε0 ) ∈ A. For each
α = (i, j, ε) ∈ A such that α ≥ α0 , we then have, by (4.4),
                           gα (x) = fi,j (x) + ε ≤ fi0 ,j0 (x) + ε0 < g(x) + δ,

                    d(tα , ti ) = d(ti,j , ti ) ≤ d(ti,j , ti ) + ε ≤ d(ti0 ,j0 , ti0 ) + ε0 < δ,
as well as i ≥ i0 , which implies d(ti , t) < δ and hence d(tα , t) < 2δ. This shows, as desired,
limα gα (x) = g(x) and limα tα = t, which concludes the proof.                                 

Proof of Theorem 4.5. That (PSH1) holds is clear from Definition 4.1. As for (PSH2), it
                                                                             gf
corresponds to the special case of Lemma 4.6 in which K := X an , FL := HR      (L) for L ∈ S :=
Pic(X)Q , and ρ : S → T := N1 (X) maps L ∈ Pic(X)Q to c1 (L). Indeed, for any θ ∈ N1 (X),
PSH(θ) is precisely the set of functions in Feθ that are generically finite.                   

# PRIMARY pertinent exact literal body

the complex analytic case, this holds in fact on any connected variety, see Corollary 4.24
below.
Remark 4.14. Any ϕ ∈ PL(X)R is η-psh with respect to some closed (1, 1)-form η, in the
sense of Remark 3.4. However, ϕ is in general not θ-psh for any θ ∈ N1 (X), since such
functions must be decreasing in the partial ordering on X an (see Proposition 4.12 ). As a
result, several potential definitions of quasi-psh functions coexist in our context.
4.3. The regularization theorem. Many properties of θ-psh functions are obtained by
regularization, that is, approximation by nicer θ-psh functions. In our present approach,
regularization of θ-psh functions is built into their definition. One can, however, improve
the properties of the approximants as follows:
Theorem 4.15. Pick θ ∈ N1 (X) and ϕ ∈ PSH(θ). Then:
                                                                   gf
     (i) ϕ can be written as the limit of a decreasing net ϕi ∈ HQ    (Li ) with Li ∈ Pic(X)Q
         such that c1 (Li ) − θ is ample and limi c1 (Li ) = θ;
    (ii) if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;
   (iii) if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in
         Hdom (ω) (see Definition 3.8).
50                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

   We shall later prove that these results actually hold with (countable) sequences instead
of nets, see Corollary 12.18.
   As already indicated by (iii), the class of θ-psh functions has particularly good properties
when θ ∈ Amp(X) is ample. In this case, we typically write ω instead of θ.
Corollary 4.16. For any ω ∈ Amp(X), the space CPSH(ω) = C0 (X) ∩ PSH(ω) is the
closure of Hdom (ω) ⊂ C0 (X) in the topology of uniform convergence.
Proof. By Theorem 4.7, CPSH(ω) is closed in the topology of uniform convergence. By
Theorem 4.15 and Dini’s lemma, any ϕ ∈ CPSH(ω) is the uniform limit of a net in Hdom (ω),
and the result follows.                                                                
Corollary 4.17. For any θ ∈ N1 (X) and any ϕ ∈ PSH(θ) we have ϕ > −∞ on X lin .
Proof. Pick an ample line ` bundle L such that c1 (L) − θ is nef. Then ϕ ∈ PSH(L). Using
Theorem 4.7 and X lin = α Xαlin , we may assume X is irreducible. Now pick v ∈ X lin . Then
TL (v) < ∞, and we claim that ϕ(v) ≥ ϕ(vtriv ) − TL (v). Indeed, TL (v) is the supremum of
m−1 v(s) over m ∈ Z>0 and s ∈ H0 (X, mL) \ {0}. Equivalently, ψ := m−1 log |s| satisfies
ψ(v) ≥ ψ(vtriv ) − TL (v). Adding constants and taking finite maxima shows that this also
holds for all ψ ∈ H(L), and then for all ϕ ∈ PSH(L), by Theorem 4.15.                     
     As another consequence, we get:
Corollary 4.18. Assume that X is irreducible, and let L be an ample Q-line bundle. Then
PSH(L) is the smallest class of functions ϕ : X an → R ∪ {−∞}, not identically −∞, that
contains all functions of the form m−1 log |s| with m ∈ Z>0 and s ∈ H0 (X, mL) \ {0}, and
is stable under addition of a real constant, finite maxima, and decreasing limits.
                                                                                gf
Proof of Theorem 4.15. By definition, ϕ is the limit of a decreasing net ϕi ∈ HR   (Li ) with
c1 (Li ) → θ. Using (2.8) it is straightforward to see that each ϕi can further be written
                                         gf
as a decreasing limit of functions in HQ    (Li ). By Lemma 4.6, we may thus assume that
        gf
ϕi ∈ HQ    (Li ). We can also arrange that c1 (Li ) − θ ∈ Amp(X). Indeed, given any ample
line bundle A, we can find εi ∈ Q>0 such that limi εi = 0 and Li − θ + εi A is ample. By
                                    gf          gf
Proposition 2.19, we have ϕi ∈ HQ      (Li ) ⊂ HQ  (Li + εi A), and replacing Li with Li + εi A
yields the claim. This proves (i).
   Assume next that θ is nef. In the notation of (i), it follows that each Li is ample. Further,
each ϕi is the decreasing limit of max{ϕi , −m} ∈ H(Li ), and Lemma 4.6 yields (ii).
   Finally assume that ω := θ is ample. Replacing ϕ with ϕ − sup ϕ, we may assume
ϕ ≤ 0. By Proposition 3.10, any function in PL ∩ PSH(ω) is a decreasing limit of functions
in Hdom (ω). Relying again on Lemma 4.6, it will thus be enough to show that ϕ is the
decreasing limit of functions in PL ∩ PSH(ω). Use the notation of (ii), and pick t ∈ Q>1 .
For all i large enough we then have tω − c1 (Li ) ∈ Amp(X) for i large enough, and hence
H(Li ) ⊂ PL ∩ PSH(tω). It follows that t−1 ϕ is the decreasing limit of a net in PL ∩ PSH(ω).
Since ϕ ≤ 0, we have t−1 ϕ & ϕ as t & 1, and another application of Lemma 4.6 shows that
ϕ is also the decreasing limit of functions in PL ∩ PSH(ω). This proves (iii).                
Remark 4.19. Assume that char k = 0 and that X is smooth and connected. Consider
the field of Laurent series K = k((t)), and denote by XKan the Berkovich analytification of
                                                               an → X an . The base change
the base change XK ; this comes with a natural projection π : XK
ωK of any ω ∈ Amp(X) defines a closed (1, 1)-form on XK   an with ample de Rham class, in

the sense of [BFJ16]. Using Theorem 4.15 (iii) and Theorem A.4 in the Appendix, one can
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                       51

show that a function ϕ : X an → R ∪ {−∞} is ω-psh in the present sense iff π ? ϕ is ωK -psh
on XKan in the sense of [BFJ16].


                                        θ ∈ N1 (X) for the moment. By Corollary 4.17 ,
4.4. The topology of PSH(θ). Let us fix `
any ϕ ∈ PSH(θ) is finite-valued on X = α Xαdiv .
                                    div


Definition 4.20. We endow PSH(θ) with the topology of pointwise convergence on X div .
  As we shall later see in Theorem   11.4, this topology coincides with the topology of point-
                       lin        lin
                            `
wise convergence on X = α Xα . In view of (4.6), we have:
Example 4.21. The map ϕ 7→ sup ϕ = maxα ϕ(vtriv,α ) is continuous on PSH(θ).
Theorem 4.22. For any ϕ ∈ PSH(θ) and any usc function ψ : X an → R ∪ {−∞}, we have

# PRIMARY pertinent exact literal body

Theorem 4.22. For any ϕ ∈ PSH(θ) and any usc function ψ : X an → R ∪ {−∞}, we have
                             ϕ ≤ ψ on X div ⇐⇒ ϕ ≤ ψ on X an .
In particular, ϕ is the smallest usc extension of ϕ|X div to X an .
Corollary 4.23. Every θ-psh function is uniquely determined by its restriction to X div , and
the topology of PSH(θ) is Hausdorff.
   Because of this, we will occasionally say that a function ϕ : X div → R is θ-psh if it admits
a (necessarily unique) extension to a θ-psh function on X an .
Corollary 4.24. If X is connected, then any 0-psh function is constant, i.e. PSH(0) = R.
Proof. By GAGA, X an is connected, and after replacing X with an irreducible component,
we may assume that X is irreducible. By Corollary 4.23, it is then enough to show that any
ϕ ∈ PSH(0) with sup ϕ = ϕ(vtriv ) = 0 satisfies ϕ(v) = 0 for any v ∈ X div . Consider the
decreasing sequence (mϕ)m∈N and its pointwise limit ψ := limm (mϕ). Since ψ(vtriv ) = 0,
we have ψ ∈ PSH(0) (see Theorem 4.5). By Corollary 4.17, we thus have ψ(v) > −∞, i.e.
ϕ(v) = 0.                                                                                
Corollary 4.25. Pick a decreasing net (ϕi ) in PSH(θ), and assume that it converges to
ϕ ∈ PSH(θ). Then ϕ = limi ϕi pointwise on X an .
Proof. The pointwise limit ψ of (ϕi ) on X an coincides with ϕ on X div . In particular,
ψ(vtriv,α ) is finite for any α, and hence ψ ∈ PSH(θ), by Theorem 4.5. By Corollary 4.23, we
infer ϕ = ψ, which means that ϕi converges to ϕ pointwise on X an                          
Lemma 4.26. For each ψ ∈ PL(X), there exists a finite set Σ ⊂ X div such that
                                  sup(ϕ − ψ) = max(ϕ − ψ)                                  (4.7)
                                   X an            Σ

for all ϕ ∈ PL+ (X), and the same result then holds for all ϕ ∈ PSH(θ), θ ∈ N1 (X).
Moreover, if ψ = r(ϕa − ρ), where r ∈ Q>0 , a is a flag ideal, and ρ ∈ PL+ (X), then we can
pick Σ = Σa , the set of Rees valuations of a.
Proof. We can always write ψ = r(ϕa − ρ) as above, and by homogeneity we may assume
r = 1. The case ϕ ∈ PL+ (X) now follows from Lemma 2.13, since ϕ + ρ ∈ PL+ (X).
  Now assume ϕ ∈ PSH(θ) for some θ ∈ N1 (X). After replacing θ with ω ∈ Amp(X)
such that ω − θ is nef, we may assume θ = ω is ample. By Theorem 4.15, we can find a
decreasing net (ϕi ) in Hdom (ω) ⊂ PL+ (X) such that ϕi & ϕ. For each v ∈ X an , we then
have ϕi (v) − ψ(v) ≤ maxΣa (ϕi − ψ) for all i, and hence ϕ(v) − ψ(v) ≤ maxΣa (ϕ − ψ). 
52                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof of Theorem 4.22. If ψ ∈ PL(X), the result follows from Lemma 4.26. Assume next
ψ ∈ C0 (X). By Theorem 2.2, ψ is a uniform limit of functions in PL(X), and the result
thus holds for ψ as well. In the general case, we can find a decreasing net (ψi ) in C0 (X)
with ψi → ψ. Then ϕ ≤ ψ ≤ ψi on X div implies ϕ ≤ ψi on X an , and hence ϕ ≤ ψ on X an
as well.                                                                                  
Remark 4.27. Assume char k = 0. By Corollary A.3, any v ∈ X an is the limit of a net
(vi ) in X div such that vi ≤ v for all i. As any ϕ ∈ PSH(θ) is decreasing and usc, it follows
that ϕ(vi ) → ϕ(v), which provides a slightly more precise version of Corollary 4.23 in that

# PRIMARY pertinent exact literal body

satisfy the envelope property. Then θ has the envelope property as well.
58                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. Pick a bounded-above family (ϕi ) in PSH(θ). Since θ ≤ θj , we have PSH(θ) ⊂
PSH(θj ). Thus sup?i ϕi is θj -psh for all j, and hence θ-psh, by Theorem 4.5.    
Corollary 5.10. If the continuity property holds for all ω ∈ Amp(X), then it holds for all
θ ∈ Nef(X).
  We next prove that the envelope property is equivalent to the analogue of a basic com-
pactness property in the complex analytic case.
Theorem 5.11. For any θ ∈ N1 (X), the following properties are equivalent:
    (i) the envelope property holds for θ;
   (ii) the space PSHsup (θ) := {ϕ ∈ PSH(θ) | sup ϕ = 0} is compact;
  (iii) every bounded-above, increasing net (ϕj ) in PSH(θ) converges in PSH(θ).
Proof. Assume (i), and pick a net (ϕi ) in PSHsup (θ). By Proposition 4.38, (ϕi (v)) is a
bounded net in R for each v ∈ X div . By Tychonoff’s theorem, after passing to a subnet,
we may thus assume that (ϕi ) converges pointwise on X div to a function ϕ : X div → R,
and it suffices to show that ϕ extends to a function in PSH(θ) (necessarily unique, by
Corollary 4.23). By (i), ψi := sup?j≥i ϕj is θ-psh for each i. The net (ψi ) is further decreasing,
and its pointwise limit ψ := limi ψi is thus either θ-psh, or identically −∞, by Theorem 4.5.
Now Theorem 5.6 implies that ψi = supj≥i ϕj on X div . Thus ψ = ϕ on X div . In particular,
ψ 6≡ −∞, hence ψ ∈ PSH(θ). This proves (i)⇒(ii).
   Next, assume (ii), and consider a bounded-above, increasing net (ϕj ) in PSH(θ). Then a
subnet ϕji −sup ϕji converges to some ϕ ∈ PSH(θ). Since (sup ϕj ) is increasing and bounded-
above, it converges to some c ∈ R. Thus ϕji → ϕ + c on X div , and hence ϕj → ϕ + c on
X div since (ϕj ) is increasing. This proves (ii)⇒(iii).
   Finally, assume (iii). Let (ϕi )i∈I be a bounded-above family of θ-psh functions, and
consider the increasing net ψJ := maxi∈J ϕi parametrized by finite subsets J ⊂ I. Then ψJ
admits a limit ψ in PSH(θ), and we claim that ψ = sup?i ϕi . On X div we have
                              ψ = lim max ϕi = supi ϕi = sup?i ϕi ,
                                    J   i∈J
by Theorem 5.6. Since ψ is θ-psh and sup?i ϕi is usc, Theorem 4.22 yields ψ ≤ sup?i ϕi on
X an . Similarly, Theorem 4.22 yields ϕi ≤ ψ, and hence sup?i ϕi ≤ ψ, since ψ is usc. This
proves the claim, and hence (iii)⇒(i).                                                  
   Recall that the variety X is said to be unibranch if the following equivalent conditions
hold (see [EGA, IV.7.6.3] and [Kol16, Corollary 32]):
      • the normalization morphism ν : X ν → X is a homeomorphism;
      • the formal completion of X at each of its points is irreducible.
In particular, any normal variety is unibranch. When k = C, X is unibranch iff the associated
complex analytic space is locally irreducible in the analytic topology. This is also true for
the Berkovich analytification as considered in this paper: the variety X is unibranch iff
the k-analytic space X an is locally irreducible in the analytic topology (see [Duc09, Lemme
5.19]).
Theorem 5.12. If the envelope property holds for some ω ∈ Amp(X), then X is necessarily
unibranch.
  The analogue of this result is known in the complex analytic setting, too. We have not
been able to locate a precise reference, but the proof below of Theorem 5.12 can easily be
adapted to that setting.
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     59

Lemma 5.13. Let π : Y → X be a birational morphism. Pick θ ∈ N1 (X), and assume that
θ can be written as the limit of a sequence of classes θm > θ with the envelope property.
                  ∼
Then π ? : PSH(θ) → PSH(π ? θ) is a homeomorphism.
  Recall that θm > θ means that θm − θ is ample.

Proof. After passing to a subsequence, we may assume that θm > θm+1 for all m, and hence
                                                           ∼
PSH(θm+1 ) ⊂ PSH(θm ). Since π induces a bijection Y div → X div , π ? : PSH(θ) → PSH(π ? θ)
is a topological embedding, and it suffices to show that it is onto. Pick ψ ∈ PSH(π ? θ), and
write π as the blowup of an ideal b ⊂ OX . By Theorem 4.32, there exists a sequence εm & 0
such that ψ + εm π ? log |b| = π ? ϕm with ϕm ∈ PSH(θm ). By Theorem 4.22, ϕm is uniquely
determined, and (ϕm )m≥m0 is an increasing sequence in PSH(θm0 ) for any given m0 . By
Theorem 5.11, ϕm converges pointwise on X div to ϕ ∈ PSH(θ), which satisfies ψ = π ? ϕ on
Y div . The result follows.                                                                 

Proof of Theorem 5.12. Since the normalization morphism ν : X ν → X is finite, ν ? ω is
ample, and hence Hdom (ν ? ω) spans PL(X ν ), see (3.2). By Lemma 2.3, PL(X ν ) separates
the points of (X ν )an , and it is thus already the case of Hdom (ν ? ω). On the other hand,
Lemma 5.13 implies that all functions in Hdom (ν ? ω) ⊂ PSH(ν ? ω) descend to X an (take ωm =
(1 + m−1 )ω). As a consequence, ν an : (X ν )an → X an is injective. By the non-Archimedean
GAGA principle, this implies that ν : X ν → X is injective as well (see [Berk90, §3.4]); this
is enough to conclude that ν is a homeomorphism, and hence that X is unibranch.             

   As mentioned above, in the complex analytic case the envelope property conversely holds
as soon as X is unibranch. It is thus natural to conjecture:
Conjecture 5.14. If X is unibranch, then the envelope property holds for all θ ∈ N1 (X).
  We will establish this conjecture in the important special case where θ is ample, X is
smooth, and char k = 0 (see Theorem 5.20).
Remark 5.15. The envelope property makes sense also when X is reducible. It is easy to
see that θ ∈ N1 (X) has the envelope property iff θ|Y ∈ N1 (Y ) has the envelope property
for every connected component Y of X. Moreover, if X is connected, then the proof of
Theorem 5.12 shows that if the envelope property holds for some ample class in N1 (X), then
the normalization morphism ν : X ν → X is a homeomorphism, which implies that X is
irreducible (and unibranch).
5.3. Envelopes. For ample classes, the envelope property admits a useful reformulation.
We continue to assume that X is irreducible unless stated otherwise. Fix a class ω ∈
Amp(X).
Definition 5.16. The ω-psh envelope of a function ϕ : X an → R ∪ {±∞} is the function
Pω (ϕ) : X an → R ∪ {±∞} defined as the pointwise supremum
                           Pω (ϕ) := sup {ψ ∈ PSH(ω) | ψ ≤ ϕ} .
  Thus Pω (ϕ) ≡ −∞ iff there is no ψ ∈ PSH(ω) with ψ ≤ ϕ. Despite the name, Pω (ϕ) is
not always ω-psh (and indeed not even usc in general). However, it is clear that
     • ϕ 7→ Pω (ϕ) is increasing;
     • Pω (ϕ + c) = Pω (ϕ) + c for all c ∈ R.
60                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON


# PRIMARY pertinent exact literal body

usc, and hence Qω (ϕ) ∈ C0 (X). Assume, conversely, that Qω (ϕ) ∈ C0 (X). Since CPSH(ω)
is stable under finite maxima, Qω (ϕ) is the pointwise limit of an increasing net (ψi ) in
CPSH(ω). By Dini’s lemma, ψi → Qω (ϕ) uniformly on X an , and hence Qω (ϕ) ∈ PSH(ω),
by Theorem 4.7. This proves (ii).
   Consider finally a net (ϕj ) as in (iii). We trivially have limj Pω (ϕj ) = supj Pω (ϕj ) ≤
Pω (ϕ). Pick ε > 0 and ψ ∈ CPSH(ω) such that ψ ≤ ϕ. As above, for all j large enough
we have ψ ≤ ϕj + ε, and hence ψ ≤ Pω (ϕj ) + ε. Thus Pω (ϕ) ≤ supj Pω (ϕj ), and we are
done.                                                                                         

5.4. The envelope property on smooth varieties. The results earlier in this section
would not be particularly useful unless we have examples of classes where the envelope
property holds. Arguing along the lines of [BFJ16, Theorem 8.5], we will prove:
Theorem 5.20. Assume that X is smooth and connected, and that either char k = 0 or
dim X ≤ 2. Then any θ ∈ Nef(X) has the envelope property.
  We do not know whether a class θ ∈ N1 (X) that is not nef has the envelope property.
Corollary 5.21. Under the assumptions of Theorem 5.20, the set
                           PSHsup (θ) = {ϕ ∈ PSH(θ) | sup ϕ = 0}
is compact.
  In [BFJ16], the above compactness property was established in the discretely valued
case, by relying on much more involved arguments based on dual complexes and toroidal
modifications.
62                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Lemma 5.22. Let L be an ample line bundle on X, and (X , L) a test configuration for
(X, L), with L an honest line bundle. Denote by am ⊂ OX the base ideal of mL, which is a
vertical ideal of X for all m  1. Then
                       PL (ϕL ) − ϕL = sup m−1 ϕam = lim m−1 ϕam
                                       m≥1             m→∞

pointwise on X an . Furthermore, PL (ϕL ) is continuous iff m−1 ϕam converges uniformly on
X an .
  As with flag ideals, see §2.1, the function ϕam ∈ PL(X) is defined by ϕam (v) = −σ(v)(am ),
where σ = σX denotes Gauss extension (see Remark 1.9).
Proof. Set ϕm := ϕL + m−1 ϕam . Note first that (am )m is a graded sequence of ideals, i.e.
am · am0 ⊂ am+m0 for all m, m0 ∈ N. The sequence m 7→ ϕam is thus superadditive, and
Fekete’s lemma yields supm≥1 m−1 ϕam = limm→∞ m−1 ϕam .
  Next write L = LX + D with a vertical Cartier divisor D on X , so that ϕL = ϕD . For
each m, denote by µm : Xm → X the integral closure of the blowup along am , and by Dm the
(antieffective) divisor on Xm such that OXm · am = OXm (Dm ); thus ϕm = ϕD + m−1 ϕDm .
By construction, OX (mL) ⊗ am is globally generated. This implies that
                         µ? (mL) + Dm = mLXm + µ? (mD) + Dm
is nef, and hence ϕm ∈ PL ∩ PSH(L). Furthermore, ϕDm ≤ 0, so ϕm ≤ ϕL , and hence
ϕm ≤ PL (ϕL ), which proves
                               sup ϕm = lim ϕm ≤ PL (ϕL ).
                               m≥1       m→∞

Conversely, Lemma 5.19 implies
                      PL (ϕL ) = QL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } .
Pick ψ ∈ H(L) with ψ ≤ ϕL . After replacing X with a higher test configuration, we may
and do assume, for the sake of notational simplicity, that ψ is determined by a vertical
Q-Cartier divisor E on X . For m large and divisible enough, Theorem 2.31 shows that
mLX + mE = mL + m(E − D) is globally generated, and hence OX (m(E − D)) ⊂ am . This
yields
                             m(ψ − ϕL ) = ϕm(E−D) ≤ ϕam ,
and hence ψ ≤ ϕm , which yields, as desired, the converse inequality
                      PL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } ≤ sup ϕm .
                                                               m
The final assertion is a simple consequence of Dini’s lemma, using the superadditivity of
m 7→ mϕm .                                                                             
Proof of Theorem 5.20. By Lemma 5.9, we may assume that θ = c1 (L) with L ∈ Pic(X)Q
ample. Pick ϕ ∈ C0 (X). By Lemma 5.17, we need to show that PL (ϕ) is continuous. Since
PL(X) is dense in C0 (X) with respect to uniform convergence (see Theorem 2.2), we may
assume ϕ ∈ PL(X), by (5.1). By Theorem 2.31, we have ϕ = ϕL for a test configuration
(X , L) for (X, L). After replacing L with a multiple, we may further assume that L and L
are honest line bundle.
   Using the notation of Lemma 5.22, we need to show that ϕm := ϕL + m−1 ϕam converges
uniformly to PL (ϕL ). Since we assume that char k = 0 or dim X ≤ 2 (and hence dim X ≤ 3),
we can rely on resolution of singularities and assume that X is smooth and X0 has simple
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                         63

normal crossings support. We may also assume that there exists an effective vertical Q-
divisor E on X such that A := L − E is ample.
   Assume first that char k = 0, and let bm be the multiplier ideal of the graded sequence am
                                                                                            • .
                                                            l
The inclusion am ⊂ bm is elementary, and we have bml ⊂ bm for all m, l by the subadditivity
of multiplier ideals. This implies that
                      m−1 ϕbm ≥ (ml)−1 ϕbml ≥ (ml)−1 ϕaml ≥ m−1 ϕam
for all sufficiently divisible m and l. Letting l → ∞ shows that
                                ϕL + m−1 ϕbm ≥ PL (ϕL ) ≥ ϕm                                (5.2)
for all sufficiently divisible m. By the uniform global generation of multiplier ideals there
exists m0 ∈ N such that

               OX (mL + m0 A) ⊗ bm = OX ((m + m0 )L) ⊗ OX (−m0 E) ⊗ bm
  is globally generated for all sufficiently divisible m. This implies that
                                      ϕbm ≤ ϕam+m0 + C
for a constant C independent of m. Combining this with (5.2) yields

                                            m0            m0        C
                       ϕm ≤ PL (ϕL ) ≤ (1 +    )ϕm+m0 −       ϕL + ,
                                            m              m        m
for all sufficiently divisible m. This shows that PL (ϕL ) is a uniform limit of continuous
functions, and hence continuous.
   When char k > 0, the very same argument applies with test ideals in place of multiplier
ideals, see [GJKM17] for details.                                                        
Remark 5.23. In view of Remark 5.15, Theorem 5.20 is valid also when X is smooth but
possibly disconnected. A suitable version of Corollary 5.21 is also true.

                       6. Homogeneous functions and b-divisors
   In this section, we assume for simplicity that X is irreducible. We study homogeneous
θ-psh functions and their relation to nef b-divisors. Inspired by the work of Ross and Witt
Nyström, we express an arbitrary θ-psh function in terms of homogeneous ones, and use this
to establish a version of Siu’s decomposition theorem in our setting.

# PRIMARY pertinent exact literal body

Proposition 3.1.11.  Étant donné un ouvert Ω de X , une fon tion sous-harmonique u
sur Ω admettant un maximum lo al en un point x de Ω est lo alement onstante au voisinage
de x.

Démonstration. Soit u une fon tion sous-harmonique admettant un maximum au point x
de Ω et soit U un voisinage ouvert onnexe de x dans Ω tel que u|U ≤ u(x) ; puisque u|U n'est
pas identiquement égale à −∞, u(x) > −∞.
   Soit Y un voisinage stri tement k-anoïde onnexe Y de x dans U . La restri tion de u à
Γ(Y ) est onstante, égale à u(x) : s'il existait, en eet, un point y ∈ Γ(Y ) tel que u(y) < u(x),
le lemme 2.3.9 fournirait une fon tion h ∈ H(Y ) telle que
    h(y) = u(y) ;
    h|Γ(Y )−{y} = u(x) ;
64



puisque Y est onnexe et h non onstante, le prin ipe du maximum pour les fon tions harmo-
niques impliquerait alors h|Y −Γ(Y ) < u(x) et don , par sous-harmoni ité, l'inégalité absurde
u(x) ≤ h(x) < u(x).
   La on lusion est maintenant immédiate : l'ensemble des points de Shilov des voisinages
stri tement k-anoïdes onnexes de x dans U étant une partie dense de U , la fon tion semi-
 ontinue supérieurement u|U est onstante, égale à u(x).                                     2

Corollaire 3.1.12.  Soient Ω ⊂ X un ouvert et u : Ω → R ∪ {−∞} une fon tion semi-
 ontinue supérieurement qui n'est identiquement égale à −∞ sur au une omposante onnexe
de Ω. Les propriétés suivantes sont équivalentes :
   (i ) u est sous-harmonique ;
   (ii ) pour tout ouvert Ω′ ⊂ Ω et pour toute fon tion harmonique h sur Ω′ , la fon tion u|Ω′ −h
satisfait au prin ipe du maximum (proposition 3.1.11) sur Ω′ .
Démonstration. L'impli ation (i) ⇒ (ii) est l'appli ation dire te de la proposition pré é-
dente puisque toute fon tion harmonique est sous-harmonique.
   L'impli ation ré iproque est immédiate : étant donnés un domaine stri tement k-anoïde
V ⊂ Ω et une fon tion h ∈ H(V ) telle que u|∂V ≤ h|∂V , l'appli ation du prin ipe du maximum
à la fon tion u − h sur v − ∂V implique que elle- i atteint son maximum en un point de ∂V ;
elle est don négative. La fon tion u est bien sous-harmonique sur Ω.                            2
   La reformulation pré édente de la dénition 3.1.5 met en éviden e le ara tère lo al de la
sous-harmoni ité.

Corollaire 3.1.13.  Le préfais eau SH sur |X| est un fais eau.

Démonstration. La semi- ontinuité supérieure et le fait de ne pas être identiquement −∞
sur une omposante onnexe sont des propriétés de nature lo ale. La propriété (ii) du orollaire
pré édent est également de nature lo ale.                                                  2


# PRIMARY pertinent exact literal body

3.3.2. Fon tions de Green élémentaires
   L'étude de l'opérateur ddc ommen e par la onstru tion de fon tions lisses parti ulières.
Proposition 3.3.7.  Soit X une ourbe stri tement k -analytique lisse.
   (i ) Si X est propre et onnexe, il existe, pour tous points x, y ∈ I(Y ), une unique fon tion
lisse gx,y ∈ A0 (X) telle que
                                     
                                        ddc gx,y = δy − δx
                                        gx,y (x) = 0.
La fon tion
                                I(X)2 → R, (x, y) 7→ gx,y (y)
                                                                                                 81



est symétrique.

   (ii ) Quels que soient le domaine k-anoïde onnexe V ⊂ X et le point x ∈ I(V ) − ∂V , il
existe une unique fon tion lisse gxV ∈ A0 (X)V qui s'annule identiquement sur ∂V et telle que
le support de la mesure νxV = ddc gxV + δx soit ontenu dans ∂V .
   La fon tion gxV est stri tement positive sur V − ∂V .
Démonstration.
(i) Supposons la ourbe X propre et onnexe. Quels que soient les points x, y ∈ I(X), l'ouvert
Ω = X − {x, y} est relativement ompa t et il existe, pour tout λ ∈ R, une unique fon tion
hλ ∈ C0 (X, R) harmonique sur Ω et telle que hλ (x) = 0, hλ (y) = λ (propositions 3.1.19 et
3.1.20). C'est une fon tion lisse et la mesure ddc hλ s'é rit c(λ)(δy − δx ) ( orollaire 3.2.11, (i)
et proposition 3.2.12).
   Les seules fon tions harmoniques sur X étant les fon tions onstantes, hλ n'est pas harmo-
nique si λ 6= 0 ; l'appli ation linéaire
                                                     Z
                                   c : R → R, c(λ) =       ddc hλ
                                                        {x}

est don un isomorphisme. Il existe ainsi un unique λ ∈ R tel que c(λ) = 1.
   La symétrie de la fon tion I(X)2 → R, (x, y) 7→ gx,y (y) se déduit immédiatement de la
proposition 3.2.12 :
                                       Z             Z
                 gx,y (y) − gy,x (x) =     gx,y δy −     gy,x δx
                                         X             X
                                          Z                    Z
                                     = −     gx,y (δx − δy ) +     gy,x (δy − δx )
                                          ZX                 Z X
                                     = −     gx,y ddc gy,x +     gy,x ddc gx,y
                                             X                  X
                                     = 0.
(ii) Soient V un domaine k-anoïde onnexe de X et x ∈ I(V ) − ∂(V ). L'espa e ve toriel
C0 (V, R) ∩ Γ(V − (∂V ∪ {x}), HX ) est isomorphe à Hom(∂V ∪ {x}, R) via l'appli ation de
restri tion ( orollaire 3.1.21) et le sous-espa e F onstitué
                                                       R     des fon tions identiquement nulles
sur ∂V est une droite. La forme linéaire F → R, ϕ 7→ {x} ddc ϕ est un isomorphisme ( ar non
nulle)R et il existe don une unique fon tion gxV ∈ A0 (X)V telle que
    {x} ddc gxV = −1 ;
    gxV s'annule identiquement sur ∂V .
   La mesure νxV = ddc gxV + δx est à support dans ∂V .
   La fon tion gxV n'est pas identiquement nulle sur V − ∂V ( ar non harmonique) ; puisqu'elle
s'annule en tout point de ∂V , elle admet don un extremum lo al stri t dans V − ∂V . L'inéga-
lité (ddc gxV )|V −∂V = −δx ≤ 0 implique qu'il ne peut s'agir que d'un maximum par appli ation
du orollaire 3.2.11, (ii) : gxV est don positive sur V . La stri te positivité sur V − ∂V dé oule
immédiatement de la onnexité de V et de l'harmoni ité de gxV sur V − (∂V ∪ {x}).               2

Remarque 3.3.8.  Nous étendrons ultérieurement le point (i) de la proposition pré édente
(théorème 3.3.13) tandis que la se tion 3.6 sera onsa rée à la généralisation du point (ii).

Corollaire 3.3.9.  Soit V ⊂ X un domaine k -anoïde onnexe ; reprenant les nota-
tions introduites dans la proposition 3.3.7 :
82



   (i ) gxV (y) = gyV (x) pour tous points x, y ∈ I(V ) − ∂V ;
   (ii ) pour toute fon tion b sur ∂V , la fon tion ontinue sur V et harmonique V − ∂V qui
 oïn ide ave b sur ∂V prend, au point x, la valeur
                                              Z
                                                   b dνxV .
                                                          ∂V

   (iii ) Pour tout x ∈ I(V ) − ∂V , νxV est une mesure de probabilité dont le support est la
frontière de la omposante onnexe de x dans V − ∂V .
Démonstration. Le point (i) dé oule dire tement de la proposition 3.2.12 et de la nullité de
gxV , gyV sur ∂V :
                                       Z                            Z
                         gxV (y) = −           gxV   ddc gyV = −            gyV ddc gxV = gyV (x).
                                           X                            X

   Soit b ∈ Hom(∂V, R) et soit h la fon tion dans H(V ) qui oïn ide ave b sur ∂V ( orollaire
3.1.21) ; le support de la mesure ddc h est ontenu dans ∂V et, appliquant de nouveau la
proposition 3.2.12,
                Z             Z              Z                 Z
                    V    c            c V           V
            0=     gx dd h =     h dd gx =      h dνx − h(x) =      b dνxV − h(x).
                     X             V                           X                           ∂V

  Le point (iii) se déduit immédiatement du pré édent : quelle que soit en eet la fon tion
positive b sur ∂V , la fon tion h ∈ H(V ) qui oïn ide ave b sur ∂V est positive et don
                                     Z
                                         b dνxV = h(x) ≥ 0.
                                                 ∂V

L'égalité h(x) = 0 est vériée si et seulement si h est identiquement nulle sur la omposante
 onnexe de x dans V − ∂V (prin ipe du maximum), d'où l'assertion sur le support de la
mesure νxV . Enn, le as de la fon tion onstante b = 1 montre que νxV est de masse totale 1.
2

     Nous sommes maintenant en mesure d'a hever la démonstration de la proposition 3.1.3.

# PRIMARY pertinent exact literal body

   In Section 4, we show the coincidence of the notions of subharmonic and psh for
continuous functions on the analytification of algebraic curves. We start by showing in
Proposition 4.3 that a lisse subharmonic function is psh. Since the psh functions form a
sheaf (see Proposition 3.19), it remains to show the assertion for an open neighborhood
of every point. The complicated case is a point of type II. The strategy is to find an open
neighborhood such that the lisse function f can be written as an R-linear combination
of model functions. One can deduce that the Monge-Ampère measure of the restriction
of f coincides with the measure ddc f defined by Thuillier since it does for every model
function, and the claim follows.
   Due to the analogue of Thuillier’s monotone regularization theorem (see Proposition
2.8), we get the following theorem.
Theorem 1. Let W be an open subset of X an and f : W → [−∞, ∞) be a subharmonic
function, then f is psh.
   We continue in Section 4 by proving the other implication for continuous functions,
i.e. the following theorem.
Theorem 2. Let W be an open subset of X an and f : W → R be a continuous function.
If f is psh, then f is subharmonic.
   To obtain this result, we first show in Lemma 4.6 that for every non-subharmonic
function f ,Rthere has to beRa specific non-negative model function g with compact support
such that f MA(g) = f ddc g < 0. The proof of the theorem is by contradiction,
and we assume that such a function g exists. RWe approximate g by non-negative
                                                                       R            smooth
functions gk with compact support such that f dMA(g) = limk→∞ f ∧d′ d′′ gk . Since f
is psh, the left hand side of the equation is non-negative, and so f has to be subharmonic.
The idea of the construction of these functions gk is based on [CD12, Proposition 6.3.2]
and we explain the modification in several steps.
   In Section 5, we give some applications of this coincidence of the two notions of
subharmonicity for continuous functions. Since we know that subharmonicity in the
sense of Thuillier is stable under pullback (see Proposition 2.6), we can deduce the
following corollary from the theorems above.
Corollary 3. Let X, X ′ be smooth proper algebraic curves over K and ϕ : W ′ → W
be a morphism of K-analytic spaces for open subsets W ⊂ X an and W ′ ⊂ (X ′ )an . If a
continuous function f : W → R is psh on W , then ϕ∗ f is psh on ϕ−1 (W ).
  Furthermore, if X satisfies some certain properties, e.g. X is the projective line
or a Mumford curve, we obtain a monotone regularization theorem in the setting of
Chambert-Loir and Ducros using the one in Thuillier’s setting (see Proposition 2.8). Note
that we need all harmonic functions on X an to be smooth in the sense of Chambert-Loir
and Ducros to prove the statement.
Corollary 4. Let X be a smooth proper curve over K. If the residue field K  e is algebraic
over a finite field or X is the projective line or a Mumford curve, then every continuous
psh function f : W → R on an open subset W of X an is locally psh-approximable. More
precisely, the sequences of smooth psh functions can be chosen monotonically decreasing.
4                                        V. WANNER


Terminology. In this paper, let K be an algebraically closed field endowed with a com-
plete, non-archimedean, non-trivial absolute value | |. We write val(K × ) := − log |K × |
and R := {x ∈ K | |x| ≤ 1} with maximal ideal m ⊂ R and residue field K   e := R/m. By
suitably normalizing the absolute value | |, we may assume that Z, and so Q, is contained
in val(K × ). A variety over K is an irreducible separated reduced scheme of finite type
over K and a curve is a 1-dimensional variety over K.

# PRIMARY pertinent exact literal body

on U an .
   A continuous metric k k on Lan is psh-approximable if there is a sequence of smooth
psh metrics k kk on Lan such that supx∈X an | log(ksx (x)k/ksx (x)kk )| converges to zero
for any local section sx of L that does not vanish in x. Clearly, this is independent of
the choice of sx .
Definition 3.26. Let X be a proper variety over K and let L be a line bundle on X.
A semistable formal model of (X, L) is a pair (X , L) consisting of a semistable formal
model X of X an and a line bundle L on X such that L |X an ≃ Lan . Note that we always
may assume that X is strictly semistable by the semistable reduction Theorem [BL93,
Ch. 7] since K is algebraically closed.
   Let (X , L) be a semistable formal model of (X, L⊗m ) for m ∈ N>0 . Then one can
define a continuous metric on Lan in the following way: If U is a formal trivialization
of L and s is a section of Lan on U η such that s⊗m corresponds to λ ∈ OX an (U η ) with
respect to this trivialization, then
                                                   1
                             − log ks(x)kL := −       log |λ(x)|
                                                   m
for all x ∈ U η . This definition is independent of all choices and shows immediately that
the defined metric is continuous. Metrics of this form are called Q-formal metrics, and
they are called formal metrics if m = 1.
   Let OX be the trivial line bundle on X. A function f : X an → R of the form f =
− log k1kL for a formal metric k kL associated to a semistable formal model of (X, O X )
is called model function.
   We have the following statements for model functions due to Chambert-Loir and
Ducros and Katz, Rabinoff and Zureick-Brown. The first theorem is a direct consequence
of a result of Chambert-Loir and Ducros in [CD12, §6.3].
Theorem 3.27. Let X be a projective variety over K and f = − log k1kL be a model
function on X an for a semistable formal model (X , L) of (X, O X ).
     i) The function f is locally approximable on X an , and so the Monge-Ampère mea-
        sure MA(f ) exists.
    ii) We have the following identity of measures
                                         X
                                MA(f ) =    degL (Y )δζY ,
                                           Y

       where Y runs over all irreducible components of the special fiber X s and ζY is the
       unique point in X an mapped to the generic point of Y under the reduction map
       (see [Ber90, Proposition 2.4.4]).
Proof. By [CD12, Corollaire 6.3.5], we know that there are line bundles L1 , L2 on X
with formal models L1 , L2 such that OX = L1 ⊗ L−1              −1
                                                 2 , L = L1 ⊗ L2 , the corresponding
metrics k kL1 and k kL2 are psh-approximable and
                         − log k · kL = − log k · kL1 + log k · kL2
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 15


on X an . Let k ki,k be a sequence of smooth psh metrics converging uniformly to k · kLi
on X an . For every point x in X an , let U be an open subset of X with x ∈ U an and s an
invertible section of L1 = L2 on U . Then − log kskLi,k is a smooth psh function on U an
for i = 1, 2 and for every k ∈ N
        − log k1kL = − log kskL1 + log kskL2 = lim − log ksk1,k + lim log ksk2,k .
                                                    k→∞                  k→∞

Hence, the function f = log k1kL is locally approximable.
  The second assertion is shown in [CD12, §6.9].                                                

  The slope formula for line bundles by Katz, Rabinoff, and Zureick-Brown in [KRZB15]
implies directly the following theorem.
Theorem 3.28. Let X be a smooth proper algebraic curve over K and f = − log k1kL
be a model function on X an for a semistable formal model (X , L) of (X, O X ). The
restriction F of f to S(X ) is a piecewise affine function and f = F ◦ τX on X an .
Furthermore, we have
                               MA(f ) = ddc F = ddc f.
Proof. This follows directly from [KRZB15, Theorem 2.6] using Theorem 3.27.                     

        4. Comparison of the two notions of subharmonic functions
  In this section, we consider a smooth proper algebraic curve X over K. We show
that every subharmonic function on X an is psh and that every continuous psh function
on X an is subharmonic. In particular, the notion of subharmonic and the notion of psh
agree for continuous functions.

4.1. Thuillier’s subharmonic functions are also subharmonic in the sense of
Chambert-Loir and Ducros. In this subsection, we show that every subharmonic
function on an open subset of X an is psh. First, we prove that every lisse subharmonic
function is psh and that every subharmonic function is locally integrable. Then we use
these results and the fact that a subharmonic function is the limit of subharmonic lisse
functions from Proposition 2.8 to prove the general claim.
Remark 4.1. Every signed Radon measure µ on an open subset W of X an defines the
following current
                                                 Z
                        [µ] : Cc∞ (W ) → R, g 7→   g dµ
                                                          W
(see [Gub16, Example 6.3]). Consider a smooth function f ∈ C ∞ (W ), then we have seen
in Proposition 3.13 that the smooth form d′ d′′ f corresponds to a signed Radon measure
which we also denote by d′ d′′ f . Using the theorem of Stokes [Gub16, Theorem 5.17], we
get d′ d′′ [f ] = [d′ d′′ f ]. Recall that a function is called psh if and only if this current is
positive.

# PRIMARY pertinent exact literal body

Lemma 4.6. Let W be an open subset of X an and f : W → R be a continuous function.
If f is not subharmonic, then there is a strictly semistable formal model (X , L) of (X, O X )
such that the model function g := − log k1kL satisfies the following properties:
      i) supp(g) is a connected strictly affinoid domain Y ⊂ W ;
     ii) g is strictly positive on Y \∂Y ;
    iii)                                Z
                                               f ddc g < 0.
                                           W
Proof. By Corollary 2.13, thereR is a connected strictly affinoid domain Y and a type II
or III point x in Y \∂Y with W f ddc gxY < 0. Since gxY is lisse, we can find a strictly
semistable formal model Y of Y and a piecewise affine function GYx on the corresponding
skeleton S(Y) such that gxY = GYx ◦τY on Y . Note that S(Y) is a closed connected subset
of X an with the structure of a finite metric graph. By blowing up Y, we may assume
that there is no edge in S(Y) whose endpoints are all contained in the boundary ∂Y . We
will explain in steps, why there is a strictly semistable formal model (X , L) such that
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 19


the corresponding
               R model  function g = − log k1kL on X an satisfies g > 0 on Y \∂Y , g = 0
                     c
elsewhere, and W f dd g < 0.

  0. Step: Strategy of the proof.

   We construct a val(K × )-rational function (see definition below) G on S(Y) with the
required properties
                                                    Z
(4.3)               G|S(Y)\∂Y > 0, G|∂Y = 0 and           f ddc G < 0.
                                                           S(Y)

Then the function g := G ◦ τY is piecewise Q-linear in the sense of [GK15] on Y . Setting
g ≡ 0 on X an \Y , we get a well-defined continuous non-negative function g on X an and
we have a G-covering of X an on which g is piecewise Q-linear. Thus, there is a semistable
                                         1
formal model (X , L) such that g = − m     log k1kL on X an by [GK14, Proposition 8.11&
8.13]. Note that we always may assume X to be strictly semistable by the semistable
reduction Theorem [BL93, Ch. 7] since K is algebraically closed. Then the formal model
(X , L⊗m ) of (X, O X ) gives the claim.
   Before we start with the construction, note that a val(K × )-rational function is a
piecewise affine function on S(Y) (we refine the vertex set such that G is affine on every
edge) such that the following properties are satisfied
   (a) ddc G is only supported on points of type II.
   (b) G has values in val(K × ) at every vertex of S(Y).
   (c) G has rational slopes.


    1. Step: Replace GYx by a piecewise affine function G′ such that (4.3) is still
             satisfied and (a) additionally holds.

   If x is of type II, the support of ddc GYx consists only of type II points. If x is of type III,
we use that the points of type II are dense in X an . Let e = [y1 , y2 ] be the edge of S(Y)
having x in its interior. Let xn be a sequence of type II points in e converging to x with
respect to the skeletal metric. Consider the piecewise affine functions Gn on S(Y) that
are given by the affine function on [y1 , xn ] (resp. on [xn , y2 ]) connecting the points GYx (y1 )
and GYx (xn ) (resp. GYx (xn ) and GYx (y2 )) and Gn ≡ GYx on S(Y)\e. It is easy to see that
the slopes converge to the ones of GYx , i.e. ddc Gn → ddc GYx for n → ∞. Furthermore, f
is continuous, so we can find n Rbig enough such that |f (xn )ddc Gn (xn ) − f (x)ddc GYx (x)|
is so small that we still have S(Y) f ddc Gn < 0 (cf. [Thu05, Proposition 3.3.4]). Set
G′ := Gn for such an n.

    2. Step: Replace G′ by a piecewise affine function G′′ such that (4.3) and (a)
             are still satisfied and (b) additionally holds.
   Due to normalizing the absolute value | |, we assume that Q is contained, and so dense,
in val(K × ). Let z be a vertex of S(Y). If G′ (z) is not in Q and (an )n is a sequence of
rational points converging to G′ (z), then the slopes of the piecewise affine functions G′n
on S(Y) resulting by replacing G′ (z) by an converge to the slopes of G′ . Thus, we can
choose an n ∈ N such that G′′ := G′n still satisfies (4.3) and takes only values in Q at
every vertex of S(Y). We choose these values such that G′′ is still strictly positive on
S(Y)\∂Y .
20                                             V. WANNER

      3. Step: Replace G′′ by a piecewise affine function G such that (4.3), (a) and (b)
               are still satisfied and (c) additionally holds.

    Now, consider an edge e = [y1 , y2 ] of S(Y). Denote by d(y1 , y2 ) the distance between
these two points with respect to the skeletal metric. If d(y1 , y2 ) ∈ Q, we are done. If
not, we can find points y1′ and y2′ of type II in e with distance d(y1′ , y2′ ) ∈ Q arbitrary
close to d(y1 , y2 ). These points are chosen so that we can decompose the edge e into
[y1 , y1′ ] ∪ [y1′ , y2′ ] ∪ [y2′ , y2 ]. Let G be the piecewise affine function on e defined by the
data G ≡ G′′ (y1 ) on [y1 , y1′ ], G ≡ G′′ (y2 ) on [y2′ , y2 ] and G|[y1′ ,y2′ ] is affine (see Figure 1).
Since G(yi′ ) = G′′ (yi ) ∈ Q, the constructed function G on e has rational slopes. Choose
yi′ with d(y1′ , y2′ ) close enough to d(y1 , y2 ) such that (4.3) is still satisfied. Note that this
is possible since f is continuous (cf. [Thu05, Proposition 3.3.4]).
    We do this for all edges except the ones containing the boundary points ∂Y , where
we just move the other vertex. Then the function G on S(Y) has slopes in Q and is
consequently the required function.


                                                    G′′ (y1 )
                                                        |
              G′′ (y1 )
                  |
                                                                                         G′′ (y2 )
                                                                                             |
                          ỹ0                 ỹ1               y1′                y2′
                 •         •                   •       •        •                  •        •
                 y0                                    y1                                   y2
                                  ∈Q                                   ∈Q

                                    ẽ                                   e

                                                FIGURE 1

                                                                                                        

# PRIMARY pertinent exact literal body

Theorem 4.7. Let W be an open subset of X an and f : W → R be a continuous function.
If f is psh, then f is subharmonic.
Proof. The proof is by contradiction.R We assume that there is a strictly semistable formal
model (X , L) of (X, O X ) such that W f ddc g < 0 for g := − log k1kL as in Lemma 4.6.

     0. Step: Strategy of the proof.

  We know that g = G ◦ τX on X an for the piecewise affine function G = g|S(X ) on
S(X ), the Monge-Ampère measure exists and ddc g = ddc G = MA(g) by Theorem 3.28.
  Assume that we have the following situation: We can write g = g + − g− on an open
subset V of W that contains the connected strictly affinoid domain Y = supp(g) such
that
     (a) g ± is the uniform limit of smooth psh functions gk± on V , i.e. g is globally ap-
         proximable on V ,
     (b) gk := gk+ − gk− ≥ 0 on V , and
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 21


    (c) gk has compact support on V .
Moreover, we want to have a connected open subset V ′ of V with Y ⊂ V ′ , V ′ ⊂ V and
gk ∈ Cc∞ (V ′ ), and a continuous map η on V such that η ≡ 1 on V ′ and η has compact
support in V .
   In this situation, we have ηf ∈ Cc0 (V ), f = ηf on V ′ and by the definition of the
Monge-Ampère measure and Theorem 3.28
                            ddc g = MA(g) = MA(g + ) − MA(g− )
is a measure with finite support contained in Y ⊂ V ′ ⊂ V . Due to our assumption, this
implies
          Z                 Z                 Z                 Z
                                                           +
       0>     f dMA(g) =       ηf dMA(g) =      ηf dMA(g ) −       ηf dMA(g − ).
             W                   V                        V   V
Applying Lemma 3.24 to the right hand side and using gk ∈ Cc (V ′ ), we get
                                                           ∞
                   Z                            Z                           Z
             0>         f dMA(g) = lim              ηf ∧ d′ d′′ gk+ − lim       ηf ∧ d′ d′′ gk−
                    W                   k→∞ V                        k→∞    V
                                                Z
                                                           ′ ′′
                                     = lim          ηf ∧ d d gk
                                        k→∞ V
                                                Z
                                     = lim       f ∧ d′ d′′ gk
                                      k→∞ V ′
                                     = lim d′ d′′ [f |V ′ ](gk ).
                                      k→∞

We know that d′ d′′ [f ] is positive on W , and so it is on V ′ . Thus,
                                        lim d′ d′′ [f |V ′ ](gk ) ≥ 0,
                                       k→∞
and so we have a contradiction. Hence, f has to be subharmonic.
  We explain in several steps how to construct V , V ′ , η and the functions gk+ , gk− such
that one has the described situation.

  1. Step:       Show that the function g is globally approximable on W .
  The curve X is projective, so we may assume X to be projective as well and can
therefore find very ample line bundles L1 , L2 such that L = L1 ⊗ L−1
                                                                   2 . Thus, we can
write
                       g = log k1kL = − log ks1 kL1 + log ks2 kL2
on W for global sections s1 , s2 that coincide on the generic fiber. Since we may work on
every open subset of W containing the compact subset Y by Proposition 3.19, we may
assume that s1 and s2 do not vanish on W . Due to the very ampleness, we can find
closed embeddings ϕi : X → PnRi such that Li ≃ ϕ∗i OPni (1) and si = ϕ∗i xji for i = 1, 2.
                                                            R
Here, let x0 , . . . , xni be the coordinates of PnRi and ji ∈ {0, . . . , ni }. Without loss of
generality, we assume xj1 = xn1 and xj2 = xn2 . These closed embeddings induce closed

# PRIMARY pertinent exact literal body

embeddings ϕi : X → PnKi into the toric varieties PnKi . Then
  g = − log ks1 kL1 + log ks2 kL2
    = ((ϕan ∗
         1 ) (− log |xn1 | +      max          log |xj |) − (ϕan ∗
                                                              2 ) (− log |xn2 | +      max          log |xj |))
                               j∈{0,...,n1 }                                        j∈{0,...,n2 }

on W . We approximate the functions φi := − log |xni | + maxj∈{0,...,ni } log |xj | for i = 1, 2
                                    ni ,an
by smooth convex functions on {η ∈ PK      | |xni |η 6= 0} as in [CD12, Proposition 6.3.2].
22                                                   V. WANNER


   For every k ∈ N>0 and n ∈ N, there is a smooth, convex function Mn, 1 on Rn+1 that
                                                                       k
is non-decreasing in every variable and has the following properties
       i) max(t0 , . . . , tn ) ≤ Mn, 1 (t0 , . . . , tn ) ≤ max(t0 , . . . , tn ) + k1 ;
                                         k
       ii) If tl + k2 ≤ maxj6=l tj , then Mn, 1 (t0 , . . . , tn ) = Mn−1, 1 (t0 , . . . , tbl , . . . , tn );
                                              k                            k
      iii) For all t ∈ R, we have Mn, 1 (t0 + t, . . . , tn + t) = Mn, 1 (t0 , . . . , tn ) + t.
                                                k                                   k

     Define for k ∈ N>0 and i ∈ {1, 2} the following function
                            φi,k := − log |xni | + Mni , 1 (log |x0 |, . . . , log |xni |)
                                                              k

    ni ,an                            ni ,an
on PK      For every point ζ in {η ∈ PK
           .                                 | |xni |η 6= 0} there is an open neighborhood
of ζ such that φi,k is smooth and psh on this neighborhood. Both are local properties
and si does not vanish on W , so (ϕan ∗
                                   i ) φi,k is a smooth psh function on W (see Remark
3.21) converging uniformly to − log ksi kLi on W . We use in the following the notations
g+ := − log ks1 kL1 and g− := − log ks2 kL2 . Furthermore, we set gk+ := (ϕan  ∗
                                                                            1 ) φ1,k and
gk− := (ϕan ∗
         2 ) φ2,k . Note that we have by construction

                                              g ± ≤ gk± ≤ gk± + 1/k.

     These functions do not necessarily satisfy (b) and (c), so we need to modify gk± .

      2. Step: Construct a suitable V and study the behavior of gk± outside of Y :


   At the end of Step 2, one can find an illustration of the construction in Figure 2. The
boundary of the strictly affinoid domain Y is a finite set of points of type II. By blowing
up our model X , we may assume that the points ∂Y are vertices in S(X ). Note that
we always may assume that an admissible blowing up is strictly semistable again by the
semistable reduction Theorem [BL85, Ch. 7]. Consider a point y ∈ ∂Y . Since y is of type
II, [BPR13, Corollary 4.27 & Theorem 4.11] tells us that there are a strictly semistable
formal model X y of X and a star-shaped open neighborhood Ωy of y in S(X y ) such that
τX−1y (Ωy ) is an open neighborhood of y in W . Here, a star-shaped open neighborhood
Ωy of y in S(X y ) is a simply-connected open neighborhood of y in S(X y ) such that the
intersection of Ωy with any edge e in S(X y ) emanating from y is a half-open interval
Iy,e = [y, xe ) with endpoints y and xe of type II. By blowing up X and modifying Ωy , we
may assume that we can find this star-shaped open neighborhood Ωy in S(X ). We explain
how to do this. The model X has to be blown up such that every vertex of S(X y ) is a
vertex in the new skeleton S(X ). Then we can modify Ωy in the following way. Consider
an edge e of the new skeleton S(X ). Then the interior of e is either contained in an
edge ẽ of S(X y ) or lies in a connected component of X an \S(X y ) isomorphic to an open
ball. In the first case, we shrink Iy,ẽ so that Iy,e is a half-open interval in e. Note that
τX−1 (Iy,e ) = τX−1y (Iy,e ), and so it is still contained in W . In the second case, we just add
a new half-open interval Iy,e to Ωy . Then τX−1 (Iy,e ) ⊂ τX−1y (y) ⊂ W . We do this blowing
ups and modifications for all boundary points. Moreover, we always choose Ωy such that
Ωy ⊂ W . Before we can construct V , we have to blow up X one more time. We find
this admissible formal blowing up X ′ of X such that Y = Y η for a formal open subset Y
of X ′ , which is possible by [BL93, Lemma 4.4]. Then we have Y = τX−1′ (S(X ′ ) ∩ Y ). As
described above, we modify Ωy such that it is a star-shaped open neighborhood of y in
S(X ′ ). Altogether, we have a strictly semistable formal model X ′ of X such that every
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 23


boundary point y of Y has an open neighborhood τX−1′ (Ωy ) in W for an open star-shaped
neighborhood Ωy of y in S(X ′ ) and Y = τX−1′ (S(X ′ ) ∩ Y ).
   For every point z ∈ (S(X ′ ) ∩ Y )\∂Y , we choose some star-shaped open neighborhood
Ωz of z in S(X ′ ) with Ωz ⊂ Y \∂Y . Then τX−1′ (Ωz ) is automatically contained in W due
to Y = τX−1′ (S(X ′ ) ∩ Y ) and Y ⊂ W .
   We have constructed for every point in S(X ′ )∩Y an open neighborhood of it in S(X ′ ),
Ωy for y ∈ ∂Y and Ωz for z ∈    / ∂Y , and so these open subsets clearly cover our compact
subset S(X ′ ) ∩ Y . Thus, there is a finite subset Y0 of S(X ′ ) ∩ Y such that
                                                        [
                             Y = τX−1′ (S(X ′ ) ∩ Y ) ⊂   τX−1′ (Ωz ).
                                                               z∈Y0

By construction, the set of boundary points ∂Y is contained in Y0 . Furthermore, we
choose Y0 minimal, i.e. removing one open subset τX−1′ (Ωz ) from the covering would no
longer cover Y . Set
                                       [
                                 V :=      τX−1′ (Ωz ),
                                                 z∈Y0
then V is an open subset of W containing Y = supp(g).
   Let y be a point in ∂Y , e an edge emanating from y in S(X ′ ) not contained in Y and
Iy,e the corresponding half-open interval in the star-shaped open neighborhood Ωy . Note
that g|e = 0. We may shrink the half-open interval Iy,e in e, and so Ωy and V , such that
        g + = (ϕan ∗
                1 ) (− log |xn1 | +       max          log |xj |) = (ϕan ∗
                                                                      1 ) (− log |xn1 | + log |xl1 |)
                                       j∈{0,...,n1 }

        g − = (ϕan ∗
                2 ) (− log |xn2 | +       max          log |xj | = (ϕan ∗
                                                                     2 ) (− log |xn2 | + log |xl2 |))
                                       j∈{0,...,n2 }

on Iy,e for some li ∈ {0, . . . , ni }. Define the map Ni,max : Iy,e → N as follows
            Ni,max (η) := |{j ∈ {0, . . . , ni }|(ϕan ∗                an ∗
                                                   i ) (log |xj |) = (ϕi ) (log |xli |)}|.

Shrink Iy,e again such that (ϕan   ∗
                                i ) (log |xj |) is affine on Iy,e for every j ∈ {0, . . . , ni }. Con-
sequently, the function Ni,max is constant on Iy,e \{y} as (ϕan       ∗                         an ∗
                                                                  i ) (log |xli |) = max(ϕi ) (log |xj |)
on Iy,e . Hence, we write Ni,max for this constant value.
   Define
                                                       2
          Ωi,k :={η ∈ Iy,e | (ϕan  ∗
                               i ) (log |xj |)(η) +      < (ϕan   ∗
                                                              i ) (log |xli |)(η)
                                                       k
                   if (ϕan  ∗                      an ∗
                        i ) (log |xj |)|Iy,e 6= (ϕi ) (log |xli |)|Iy,e , j ∈ {0, . . . , ni }}

Let N ′ ∈ N such that Ωk := (Ω1,k ∩ Ω2,k )\{y} is a non-empty connected open subset
of Iy,e for every k ≥ N ′ . We have Ωk ⊂ Ωk+1 , and we work in the following with
Ωy,e := ΩN ′ . Then we get for every k ≥ N ′ using properties i)-iii) that
(4.4)    gk+ = (ϕan ∗                            an ∗                       an ∗
                 1 ) (− log |xn1 |) + Mn1 , 1 ((ϕ1 ) (log |x0 |), . . . , (ϕ1 ) (log |xn1 |))
                                                 k

            = (ϕan ∗                                  an ∗                        an ∗
                1 ) (− log |xn1 |) + MN1,max −1, 1 ((ϕ1 ) (log |xl1 |), . . . , (ϕ1 ) (log |xl1 |))
                                                           k

            = (ϕan ∗                   an ∗
                1 ) (− log |xn1 |) + (ϕ1 ) (log |xl1 |) + MN1,max −1, 1 (0, . . . , 0)
                                                                                k
                 +
            = g + MN1,max −1, 1 (0, . . . , 0)
                                   k

on Ωy,e . Set Ck+ := MN1,max −1, 1 (0, . . . , 0) ∈ [0, k1 ]. Analogously,
                                 k

(4.5)                           gk− = g− + MN2,max −1, 1 (0, . . . , 0)
                                                                k
24                                                   V. WANNER


on Ωy,e . Set Ck− := MN2,max −1, 1 (0, . . . , 0) ∈ [0, k1 ]. Due to g = g+ − g − = 0 on Ωy,e , we
                                 k
have
                      gk+ − gk− = MN1,max −1, 1 (0, . . . , 0) − MN2,max −1, 1 (0, . . . , 0)
                                                 k                             k

on Ωy,e .



                                                                                gk+
                                                                                gk−
                                                                                       g+ = g−




            •                      •[
                                   y                                                  xe
                S(X ′ ) ∩ Y                                Ωy,e

     W                                                     Iy,e


                                                      FIGURE 2


 3. Step: Modify the constructed functions gk± on the open subset V ⊂ W
          such that (b) and (c) are satisfied.

   We start with (b). To ensure that the difference gk+ − gk− = (ϕan  ∗         an ∗
                                                                   1 ) φ1,k − (ϕ2 ) φ2,k is
non-negative on V , we work with gk+ := (ϕan ∗       1                   an ∗
                                          1 ) φ1,k + k on V instead of (ϕ1 ) φ1,k , which is
                                                                         +
still a smooth psh function on V converging uniformly to the function g = − log ks1 kL1 ,
and
                       1                               1
          (ϕan ∗
            1 ) φ1,k +   − (ϕan  ∗         an ∗
                              2 ) φ2,k ≥ (ϕ1 ) φ1,k +    − g+ + g − − (ϕan  ∗
                                                                         2 ) φ2,k
                       k                               k
                                             1 1
                                       ≥0+ − =0
                                             k k
on V . Note that we have used g = g + − g− ≥ 0 on V and property i) of Mni ,k .
   Next, we deal with (c), i.e. we modify gk+ and gk− such that gk := gk+ − gk− has compact
support on V . As in Step 2, let y be a boundary point of Y , Ωy a star-shaped open
neighborhood of y and Iy,e = [y, xe ) be a half-open interval of Ωy contained in an edge e
of S(X ′ ) emanating from y and pointing outwards of Y . Recall that we have constructed
in the second step the open subset Ωy,e of Iy,e . Here, we start with the construction
of an affine function on the closed annulus A := τX−1′ ([y, xe ]) whose graph intersects the
graphs of all our functions gk± on Ωy,e for k big enough. The annulus A is isomorphic to
a closed annulus A′ := S(a, b) = trop−1 ([val(b), val(a)]) in G1,an                     ×
                                                                  m for some a, b ∈ K with
                                                 ∼     ′
|a| < |b| and trop := − log |T |. Let Φy,e : A − → A be an isomorphism. For simplicity, we
may assume that val(b) = 0. Then we can identify Iy,e = [y, xe ) with the real half-open
                                                                              ′ ∈Ω
interval [0, val(a)) via tropy,e := − log |T | ◦ Φy,e . Choose points ζy,e , ζy,e  y,e ⊂ e, and
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 25


# PRIMARY pertinent exact literal body


m ∈ N, c ∈ R such that the function

                              ψy,e : Iy,e → R; ζ 7→ m · tropy,e (ζ) + c

satisfies

            ψy,e (ζy,e ) = ((ϕan ∗                   an ∗                          +
                              1 ) (− log |xn1 |) + (ϕ1 ) (− log |xl1 |))(ζy,e ) = g (ζy,e ),

           ′ ) = g + (ζ ′ ). Recall that N ′ was fixed in Step 2 to define Ω . Since g ±
and ψy,e (ζy,e    N ′ y,e                                                   y,e       k
converges uniformly to g+ = g − on Ωy,e , there is an N ′′ ≥ N ′ such that

                             sup (gk± − g ± ) = sup |gk± − g± | ≤ CN
                                                                   +
                                                                     ′
                            x∈Ωy,e                   x∈Ωy,e

                                        +       ± = C + + 1/N ′ , and hence
for every k ≥ N ′′ . By (4.4), we have gN ′ − g      N′

                               gk± − gN
                                      +      ±
                                        ′ = gk − g
                                                   ±         +
                                                     + g± − gN ′ < 0


on Ωy,e for every k ≥ N ′′ . Thus, for every k ≥ N ′′ there is a point ζk+ in Ωy,e such that
ψy,e (ζk+ ) = gk+ (ζk+ ). Due to g + = g− ≤ gk− ≤ gk+ by (4.5) and construction, there is also
for every k ≥ N ′′ a point ζk− in Ωy,e such that ψy,e (ζk− ) = gk− (ζk− ). Recall that g− = g+
and gk+ and gk− with k ≥ N ′ are affine on Ωy,e .
   We choose ε such that

                           Ωy,e,< := {ζ ∈ Ωy,e | ψy,e (ζ) + 2ε < g+ (ζ)}
                           Ωy,e,> := {ζ ∈ Ωy,e | ψy,e (ζ) > g+ (ζ) + 2ε}

are non-empty open subsets of Ωy,e , and we set Γy,e := Ωy,e \(Ωy,e,< ∪ Ωy,e,> ).
   In the following, we smoothen the piecewise affine functions max(gk± , ψy,e ) in a proper
way. One can construct a smooth symmetric convex 1-Lipschitz continuous function
θε : R → (0, ∞) such that θε (a) = |a| if |a| ≥ ε. We set
                                                    a + b + θε (a − b)
(4.6)                                mε (a, b) :=                      .
                                                            2
  Then the smooth function mε : R2 → R satisfies the following properties:
      i) mε is convex;
     ii) max(a, b) ≤ mε (a, b) ≤ max(a, b) + 2ε ;
    iii) mε (a, b) = max(a, b) whenever |a − b| ≥ ε;
    iv) mε is increasing in every variable.
We define the functions

                                          gek+ := mε (gk+ , ψy,e ),
                                           gek− := mε (gk− , ψy,e )

on Ωy,e . Then e gk+ (resp. gek− ) coincides with gk+ (resp. with gk− ) on Ωy,e,< for every
k ≥ N since g = g− ≤ gk− ≤ gk+ on Iy,e by (4.5) and by construction. The functions
       ′′       +

gk+ converge uniformly to g − = g+ , so we can choose Ny,e ≥ N ′′ such that for all k ≥ Ny,e ,
we have g + + ε ≥ gk+ ≥ gk− on Ωy,e . Then gek+ and gek− coincide with ψy,e on Ωy,e,> for all
                 gk+ − gek− = 0 on Ωy,e,> for every k ≥ Ny,e . We do this for every y ∈ ∂Y
k ≥ Ny,e . Thus, e
and for every edge e in S(X ′ ) emanating from y and pointing outwards of Y .
26                                              V. WANNER


                                                                                 ψy,e




                                                                           +
                                                                          gN  ′

                                                                          gk+
                                                                          gk− g+ = g−
                        g+ + ε
               max(gk± , ψy,e )


                                                     ζy,e
          •                       •[            [     •      ]
                                                      Γy,e
                                  y                                          xe
              S(X ′ ) ∩ Y              Ωy,e,<                    Ωy,e,>
                                                     Ωy,e
      W                                               Iy,e

                                             FIGURE 3
                                                   S
   Recall that we work on the open subset V = z∈Y0 τX−1′ (Ωz ) of W containing Y , where
Ωz is a star-shaped open neighborhood of z in S(X ′ ) and Iz,e = Ωz ∩ e for every edge
e in S(X ′ ) emanating from z. We have ∂Y ⊂ Y0 and the sets Ωy \Y with y ∈ ∂Y are
disjoint of all other star-shaped open neighborhoods Ωz . We write Sy for the set of edges
e in S(X ′ ) emanating from y and pointing outwards of Y . Then for every y ∈ ∂Y and
e ∈ Sy , we have constructed the open subset ΩS     y,e of Iy,e = [y, xe ) ⊂ Ωy .
   Let VY be the connected component of V \( y∈∂Y ;e∈Sy Γy,e ) containing Y and Ve be
the connected component of V \Γy,e containing xe . Note that by the construction of V
all connected components Ve are pairwise disjoint. We can extend gek± to a continuous
function on V by
                                
                                      ±                       −1
                                mε (gk , ψy,e ◦ τX ′ ) on τX ′ (Ωy,e ),
                         gek± := gk±                      on VY ,
                                
                                
                                 ψy,e ◦ τX ′              on Ve .

  Then the functions gek+ − gek− are non-negative and continuous on V with compact
support for every k ≥ maxy,e Ny,e . Recall that by property iv), mε is increasing in every
variable. From now on we only consider k ∈ N with k ≥ maxy∈∂Y,e∈Sy Ny,e .

                                                gk+ (resp. gek− ) converge uniformly to a function
      4. Step: Show that the modified functions e
               e+         −                g − ge− on V .
               g (resp. ge ) such that g = e+


     Define the following functions on V
                                
                                       ±
                                mε (g , ψy,e ◦ τX ′ )       on τX−1′ (Ωy,e ),
                         ge± := g±                           on VY ,
                                
                                
                                  ψy,e ◦ τX ′                on Ve .
   COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 27


  By construction, these functions are well-defined and continuous. Since g = g + − g−
on V with g = g + − g− = 0 on V \Y , we clearly have g = ge+ − e    g− on V .
                           +         −
  Next, we show that e   gk (resp. gek ) converge uniformly to ge (resp. to ge− ) on V . We
                                                                 +

                                                                                           gk− )
                                                                                gk+ (resp. e
know that gk+ (resp. gk− ) converge uniformly to g + (resp. to g− ) on V , thus e
                           +             −                  ±                      ±
converge uniformly to g (resp. to g ) on VY . Since gek = ψy,e ◦ τX ′ = e        g on Ve , it
                                          −1                        −1
remains to consider the open subset τX ′ (Ωy,e ). For every x ∈ τX ′ (Ωy,e ), we have
 gk± (x) − ge± (x)| = mε (gk± (x), ψy,e (τX ′ (x)) − mε (g± (x), ψy,e (τX ′ (x)))
|e
                       gk± (x) − g ± (x) + θε (gk± (x) − ψy,e (τX ′ (x))) − θε (g± (x) − ψy,e (τX ′ (x)))
                   =
                                                               2
                       gk± (x) − g ± (x)   g± (x) − g ± (x)
                   ≤                     + k
                               2                  2
                   ≤ |gk± (x) − g ± (x)|
where we used that θε is 1-Lipschitz continuous to get the inequality. Due to the uniform
convergence of gk± to g± on V , which contains τX−1′ (Ωy,e ), we get
                               lim      sup            gk± (x) − e
                                                      |e         g ± (x)| = 0.
                              k→∞ x∈τ −1 (Ω
                                       X′     y,e )


  5. Step: Show that the modified functions gek+ and e
                                                     gk− are smooth and psh on V .


  Note that both properties are local. We already know that gk± ∈ C ∞ (VY ), so it
remains to find for every point x in τX−1′ (Ωy,e ) ∪ Ve an open neighborhood Vx in V such
that gek± is smooth and psh on Vx .
  We start with a point x ∈ Ve . Choose an open neighborhood Vx of x in the open
subset Ve ⊂ V , then gek± is given by ψy,e ◦ τX ′ on Vx . For every ζ ∈ Vx ⊂ A, we have
            gek± (ζ) = (ψy,e ◦ τX ′ )(ζ) = (ψy,e ◦ τA )(ζ) = Φ∗y,e (−m · log |T | + c)(ζ)
on Vx . We first show
                   −m · log |T | + c ∈ ker(d′ d′′ : C ∞ (G1,an   1,1 1,an
                                                          m ) → A (Gm )).

Consider the tropical chart (V, ϕU ) = (G1,an                  1,an
                                               m , id) of Gm . Then tropU = log |T |, and
                                                    1,an
so −m · log |T | can be written as the triple (Gm , id, λ), where λ : R → R is the affine
                                                                               1,an
function t 7→ mt + c. Thus, −m · log |T | + c is a smooth function on Gm            (cf. Definition
                                                                                    1,an
3.11). The (1, 1) form d d (−m · log |T | + c) is given by the triple (Gm , id, d′ d′′ λ).
                              ′ ′′

Since λ is affine, the form d′ d′′ λ is zero, and so is d′ d′′ (−m · log |T | + c). Consequently,
−m · log |T | + c ∈ ker(d′ d′′ : C ∞ (G1,an         1,1    1,an
                                         m ) → A (Gm )). This implies that e              gk± |Vx =
Φ∗y,e (−m · log |T | + c) is a smooth psh function on Vx (see Remark 3.21).
   Now, consider x ∈ τX−1′ (Ωy,e ). We have just seen that ψy,e ◦ τX ′ is a smooth psh
function on τX−1′ ((y, xe )). Using Proposition 3.20, there is a chart (Vx , ϕUx ) with x ∈
Vx ⊂ τX−1′ ((y, xe )) such that ψy,e ◦ τX ′ = φ ◦ tropUx on Vx for a smooth function φ on
Rr that is convex restricted to every polyhedron contained in tropUx (Vx ). On the other
hand, we know that the function gk± is smooth and psh on τX−1′ ((y, xe )) as well. Hence,
there is also a chart (Vx′ , ϕUx′ ) with x ∈ Vx′ ⊂ τX−1′ ((y, xe )) such that gk± = φ′ ◦ tropUx′
                                            ′
on Vx′ for a smooth function φ′ on Rr that is convex restricted to every polyhedron
contained in tropUx′ (Vx′ ). Working on the intersection (Vx ∩ Vx′ , ϕUx × ϕUx′ ), which is a
28                                         V. WANNER


subchart of both [Gub16, Proposition 4.16], we get
                           ψy,e ◦ τX ′ = (φ ◦ Trop(π)) ◦ tropUx ∩Ux′
                                  gk± = (φ′ ◦ Trop(π ′ )) ◦ tropUx ∩Ux′
for the corresponding transition functions π, π ′ satisfying ϕUx = π ◦ (ϕUx × ϕUx′ ) and
ϕUx′ = π ′ ◦ (ϕUx × ϕUx′ ). Since Trop(π) and Trop(π ′ ) are integral affine functions on
     ′                                                                                     ′
Rr+r , the composition φ◦Trop(π) (resp. φ′ ◦Trop(π ′ )) is still a smooth function on Rr+r
with a convex restriction to every polyhedron. Thus, mε (φ ◦ Trop(π), φ′ ◦ Trop(π ′ )) is a
                           ′
smooth function on Rr+r , and the properties i) and iv) of mε imply that the restriction
to every polyhedron is convex since the restriction of φ ◦ Trop(π) and φ′ ◦ Trop(π ′ ) are.
We have
          gk± = mε (gk± , ψy,e ◦ τX ′ ) = mε (φ ◦ Trop(π), φ′ ◦ Trop(π ′ )) ◦ tropUx ∩Ux′
          e
on Vx ∩ Vx′ for every x ∈ τX−1′ (Ωy,e ), so gek± is a smooth psh function on τX−1′ (Ωy,e ) by
Proposition 3.20, which proves Step 5.
  Altogether, egk± are smooth psh function on V . We set
                                         gk := gek+ − gek− ,
                                         e
then the functions e
                   gk satisfy by construction all the required properties in Step 0.

     6. Step: Construction of V ′ and η.

   By the construction of V and e  gk , it is no problem to construct the required set V ′ ,
                       ′
i.e. an open subset V of V containing Y such that V ′ ⊂ V and e        gk ∈ Cc∞ (V ′ ). Fur-
thermore, let V ′′ be an open neighborhood of V ′ in V with V ′′ ⊂ V . The topological
space X an is a compact Hausdorff space. Urysohn’s Lemma states the existence of a
continuous function η : X an → [0, 1] with η ≡ 1 on V ′ and η ≡ 0 on X an \V ′′ . Thus, η
has compact support in V , i.e. it is the required function in Step 0.

  Thus, we have constructed everything as it was described in Step 0 proving the theo-
rem.                                                                                
Corollary 4.8. Let f : W → R be a continuous function. Then f is subharmonic if and
only if f is psh.
Proof. Follows directly from Theorem 4.5 and Theorem 4.7.                                   

         5. Stability under pullback and a regularization theorem
   Due to this equivalence in Corollary 4.8, we know that a continuous psh function
has all the nice properties that are shown for subharmonic functions in [Thu05]. More
precisely, we now know that the property psh for continuous functions is stable under
pullback with respect to morphisms of curves. Furthermore, we show that there is a
monotone regularization theorem in the setting of Chambert-Loir and Ducros under
certain conditions, e.g. if X is P1K or a Mumford curve.
Corollary 5.1. Let X, X ′ be smooth proper algebraic curves over K and ϕ : W ′ → W
be a morphism of K-analytic spaces for open subsets W ⊂ X an and W ′ ⊂ (X ′ )an . If a
continuous function f : W → R is psh on W , then ϕ∗ f is psh on ϕ−1 (W ).

# PRIMARY pertinent exact literal body

36                       SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

Theorem 4.19. As above, let X = Spec A be an affine model of X = Spec A. We then
have k · ksup ≤ k · kAb on A,b and hence k · kX i ≤ k · kA on A. Consider further the following
properties:
     (i) Xs is reduced;
                               b
    (ii) k · ksup = k · kAb on A;
   (iii) k · kX i = k · kA on A;
   (iv) Ab is integrally closed in A;
                                    b
    (v) A is integrally closed in A.
Then (i) ⇐⇒ (ii) ⇐⇒ (iii) =⇒ (iv) ⇐⇒ (v). If K is densely valued, we also have (v) =⇒ (i),
and (i)—(v) are then equivalent.
Proof. Pick a nonzero g ∈ A. b By Lemma 4.18, kgk b is in the value group |K × |, and we may
                                                        A
thus assume that kgkAb = 1 after multiplying g by a nonzero scalar. We then have g ∈ A,           b
hence |g(x)| ≤ 1 for all x ∈ X i , which proves that kgksup ≤ 1, and hence k · ksup ≤ k · kAb.
   Suppose now that Xs is reduced, and assume by contradiction that g as above satisfies
kgksup < 1. By [BGR, 6.2.3/2], g is topologically nilpotent, i.e. gn → 0. For n ≫ 1, we thus
                                  b since A ⊗ K
have kgn kAb < 1, i.e. gn ∈ K ◦◦ A;              e ≃ Ab ⊗ K e is reduced, this implies g ∈ K ◦◦ A,b
which contradicts kgkAb = 1. We have thus proved (i)=⇒(ii), which trivially implies (iii) by
composing with A → A.   b If (iii) holds, then k · kA is power-multiplicative, i.e. kf n kA = kf kn
                                                                                                  A
for each f ∈ A and n ∈ N. In particular, f n ∈ K ◦◦ A ⇐⇒ kf n kA < 1 ⇐⇒ f ∈ K ◦◦ A, which
means that A ⊗ K   e ≃ A/K ◦◦ A is reduced.
   Since Ab (resp. A) is the unit ball of k · kAb (resp. k · kA ), Theorem 4.15 shows that (ii)
and (iii) respectively imply (iv) and (v), while Corollary 4.16 shows that (iv) and (v) are
equivalent.
   Assume finally that K is densely valued and that (v) holds. To prove (i), we need to
show that each f ∈ A such that f n ∈ aA for some n ≥ 1 and a ∈ K ◦◦ actually satisfies
f ∈ K ◦◦ A. Since K is densely valued, we can find a′ ∈ K ◦◦ with |a|1/n ≤ |a′ | < 1, and
hence a/a′n ∈ K ◦ . As a result, g := a′−1 f ∈ A satisfies g n ∈ A, and hence g ∈ A, since A is
integrally closed in A. We have thus shown as desired that f = a′ g ∈ K ◦◦ A (we are grateful
to Walter Gubler for his help with this argument).                                                
   We conclude this section with the following rather special case of the scheme-theoretic
version of the Bosch–Lütkebohmert–Raynaud reduced fiber theorem [BLR95, Theorem 2.1’].
We provide some details for the convenience of the reader (see also [Ana73, Théorème 1’,
p.73]).
Theorem 4.20. Assume that K is non-Archimedean and nontrivially valued, and either
discretely valued or algebraically closed. Let X be a reduced K-scheme of finite type, and
pick a model X of X. The integral closure X ′ of X in X is then finite over X , and hence a
model of X as well. In the algebraically closed case, Xs′ is further reduced.
   Note conversely that the existence of a model with reduced special fiber implies that X
is reduced, by [EGA, IV,12.1.1].
Proof of Theorem 4.20. If K is discretely valued, then X is excellent, which implies that its
integral closure in X is finite. Assume that K is algebraically closed. It is then densely
valued, and the final point will thus follow from Theorem 4.19.
                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                           37

   The finiteness of X ′ over X being local, we assume that X = Spec(A) is affine and use
the above notation. We will reduce the result to the Grauert–Remmert finiteness theorem,
basically arguing as in [BL86, Proposition 1.5] and [Tem10, Theorem 3.5.5, Step 3].
   Since A is reduced, A  b is reduced as well by Lemma 4.13, and [BGR, 6.4.1/5] thus shows
that Ab is finite over A,
         ′                b i.e. Ab′ = P Ag b i for a finite set gi ∈ A,
                                                                      b in which we include 1
                                          i
for convenience. As in the proof of Lemma 4.17, we can find for each i some fi ∈ A with
gi − fbi ∈ A,b and hence Ab′ = P Abfbi . By Corollary 4.16, an element f ∈ A belongs to the
                                    i                           P
integral P closure A′ of A in A if and only fb belongs to Ab′ = i Abfbi , which
                                                                            P is also equivalent
to f ∈ i Afi by Lemma 4.17. We conclude as desired that A′ = i Afi is finite over
A.                                                                                            
Remark 4.21. Theorem 4.20 fails in general over an arbitrary densely valued non-Archimedean
field K. Let indeed X = Spec A be an affine reduced K-scheme, X = Spec A an affine model,
and denote by A′ the integral closure of A in A. If K is densely valued and A′ is finite over
A, then X ′ := Spec A′ is a model of X, and hence Xs′ is reduced, by Theorem 4.19. As a
result, the sup-seminorm k · kX i = k · kX ′i = k · kA′ takes values in |K|, a condition that is
not satisfied in general when the group |K × | is not divisible.

                     5. Fubini–Study metrics and model metrics
  This section introduces Fubini–Study metrics, and compares them with model metrics.
The main result is Theorem 6.4, which compares the supnorms and lattice norms induced
by a model metric, and relies on the reduced fiber theorem.
  In what follows, X denotes a projective K-scheme, where K is a complete valued field.


# PRIMARY pertinent exact literal body

5.2. Fubini–Study metrics. The usual Fubini–Study metric on the tautological ample
line bundle O(1) over the projective space (also known as the Weil metric in the non-
Archimedean context) generalizes in a natural way as follows (see Corollary 7.18 below for
a more conceptual characterization).
Definition 5.2. A metric φ on a line bundle L over X is called a Fubini–Study metric if
there exists m ≥ 1, a finite set of sections (si ) of mL without common zeroes, and constants
λi ∈ R such that
              1    P
   (A) φ = 2m   log i |si |2 e2λi (Archimedean case);
             1
  (NA) φ = m    maxi {log |si | + λi } (non-Archimedean case).
We say that φ is pure if λi = 0.
   By definition, L admits a (pure) Fubini–Study metric iff L is semiample, i.e. mL is globally
generated for some m ≥ 1.
   The notation |si | = elog |si | is understood as in Example 5.1, and thus means that for any
local trivializing section τ of L, the corresponding functions fi := si /τ m ∈ OX satisfy
                               1        X                      1
                − log |τ |φ =       log    |fi |2 e−2λi (resp.   max{log |fi | + λi }).
                              2m                               m i
                                    i

In the Archimedean case, one can replace si with eλi si , and all Fubini–Study metrics are
thus pure in that case.
   Given a subgroup Γ ⊂ R, we say that a metric φ as above is a Γ-Fubini–Study metric if
λi ∈ Γ for all i. We denote by
                                   FSΓ (L) ⊂ C0 (L)
the set of Γ-Fubini–Study metrics on L, and by FS(L) = FSR (L) the set of all Fubini–Study
metrics. The set of pure Fubini–Study metrics is thus FS{0} (L).
Remark 5.3. While Fubini–Study metrics are smooth in the Archimedean case, they are
instead piecewise linear when K is non-Archimedean (see §5.4 below). But it is anyway easy
to explicitly approximate a Fubini–Study metric by smooth metrics, cf. Theorem 7.14.
     The next result summarized the main properties of Fubini–Study metrics.
Proposition 5.4. If L, L′ are line bundles on X and Γ ⊂ R is a subgroup, then:
    (i) FSΓ (L) + FSΓ (L′ ) ⊂ FSΓ (L + L′ );
   (ii) FSΓ (L) = FSΓ′ (L) with Γ′ := Q(Γ + ΓK ) the Q-linear subspace of R spanned by Γ
        and ΓK ;
  (iii) FSΓ (mL) = m FSΓ (L) for all m ∈ Z>0 ;
  (iv) f ⋆ FSΓ (L) ⊂ FSΓ (f ⋆ L) for any projective morphism f : X ′ → X;
                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                               39

   (v) if Γ 6= {0}, or K is nontrivially valued, then FSΓ (L) is dense in FS(L) with respect
       to uniform convergence.
When K is non-Archimedean, we further have:
  (vi) FSΓ (L) is stable under max.
Proof. Pick m, m′ ≥ 1 and finitely many sections without common si ∈ H0 (mL), s′j ∈
                            1     P                  1        P ′ 2
H0 (m′ L′ ) such that φ = 2m   log i |si |2 , φ′ = 2m  ′ log   j |sj | in the Archimedean case, and
     1                         ′   1               ′        ′
φ = m maxi {log |si | + λi }, φ = m maxj {log |sj | + λj } in the non-Archimedean case. In the
former case,
                                                           !m′               m
                                                X                X
                       mm′ (φ + φ′ ) = log          |si |2           |s′j |2  ,
                                                  i              j
                                            P
which expands out as mm′ (φ + φ′ ) = log α |σα |2 for a finite set of sections σa ∈ H0 (mm′ L)
without common zeroes, proving that φ + φ′ is Fubini–Study. In the non-Archimedean case,
                                             ′
                mm′ (φ + φ′ ) = max{log |sm      ′                 ′m      ′
                                          i | + m λi } + max{log |sj | + mλj }
                                  i                          j
                                              ′
                              = max{log |sm  ′m     ′       ′
                                          i sj | + m λi + mλj },
                                  i,j
which proves (i). The proof of (ii) and (iii) is similar, and (iv), (vi) follow directly from
the definitions. To prove (v), note that the assumption implies that Γ′ = Q(Γ + ΓK ) is a
nontrivial Q-linear subspace of R. It is thus dense in R, and it is then straightforward to
check that FSΓ (L) = FSΓ′ (L) is dense in FS(L) = FSR (L), simply by approximating the
coefficients λi in Definition 5.2.                                                          
  By Proposition 5.4 (ii), we can make sense of Γ-Fubini–Study metrics on any Q-line
bundle L over X. As noted above, such metrics exist iff L is semiample. As we now show,
Fubini–Study metrics always descend to an ample Q-line bundle.
Lemma 5.5. If L is a semiample Q-line bundle on X, then there exists a surjective mor-
phism f : X → Y to a projective K-scheme with f⋆ OX = OY and an ample Q-line bundle
A on Y such that f ⋆ A = L. Further, f and (Y, A) are unique up to isomorphism.
  We call A the Stein factorization of L.
Proof. After passing to a multiple, we may assume that L is a globally generated line bundle.
We then have a morphism h : X → P H0 (L) such that L = h⋆ O(1). By Stein factorization,
we have h = g ◦ f with f : X → Y such that f⋆ OX = OY and g : Y → P H0 (L) finite. Thus
A := g⋆ O(1) is ample, and L = f ⋆ A. By the projection formula, we have H0 (Y, mA) ≃
H0 (X, mL) for all m. This shows that (Y, A) is recovered from the graded ring R(X, L) =
L       0
  m∈N H (X, mL) by the Proj construction, and hence is unique up to isomorphism.          
Lemma 5.6. Let L be a semiample Q-line bundle on X. Denote by Xred ⊂ X the reduction
of X, and by Lred the restriction of L. For all m sufficiently divisible, the restriction map
H0 (X, mL) → H0 (Xred , mLred ) is surjective.
Proof. Use the notation of Lemma 5.5. Since every germ on OYred locally lifts to OY , we
have f⋆ OXred = OYred , hence H0 (Xred , mLred ) ≃ H0 (Yred , mAred ), by the projection formula.
We are thus reduced to the case where L is ample, which follows from Serre vanishing. 
40                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

Corollary 5.7. Let L be a semiample Q-line bundle on X. Denote by A the Stein factor-
ization of L as in Lemma 5.5, and by Lred the restriction of L to Xred . Then
                                FSΓ (A) ≃ FSΓ (L) ≃ FSΓ (Lred ).
5.3. Model metrics. In this section, K is non-Archimedean (possibly trivially valued). A
model of a line bundle L on the projective K-scheme X is a line bundle L on a projective
model X of X, together with an isomorphism L|XK ≃ L compatible with the given isomor-
phism XK ≃ X. When L = OX , each model of L is of the form OX (D) where D is a vertical
Cartier divisor on a projective model X , i.e. Supp D ⊂ Xs .
Lemma 5.8. Let L be a line bundle on X, and X a projective model of X. Then we can
find a projective model X ′ dominating X and a model L of L determined on X ′ .
Proof. Pick very ample line bundles A1 , A2 on X such that L = A1 − A2 . Sections of Ai
yields an embedding X ֒→ PN   K such that Ai = O(1)|X . The scheme theoretic closure of X
                               i

     Ni
in PK ◦ is thus a projective model Xi of X, and Ai := O(1)|Xi is a model of Ai determined
on Xi . It remains to choose a projective model X ′ dominating X , X1 and X2 , and to define
L as the difference of the pullbacks to X ′ of A1 and A2 .                                

   A model L of L defines a continuous metric φL on L, as follows. Cover X with finitely
many open subschemes Ui with a trivializing section τi of L. Since X is in particular proper
over K ◦ , X an = X i is covered by the compact sets Uii . We may thus define a continuous
metric φL on Lan by requiring that |τi |φL = 1 on Uii . This is indeed well-defined, since any
other trivializing section of L on Ui is of the form ui τi with ui ∈ O× (Ui ) a unit, and hence
|ui | ≡ 1 on Uii .
Example 5.9. If K is trivially valued, the model metric defined by the unique model (X, L)
is called the trivial metric of L.
Lemma 5.10. Let L be a model of L, with corresponding metric φL .
      (i) For each m ∈ Z we have φmL = mφL .
     (ii) If a model X ′ dominates X , then the pull-back L′ of L to X ′ satisfies φL′ = φL .
Proof. If τ is trivializing section of L on an open set U , then τ m is a trivializing section
of mL, and the pull-back of τ is a local trivialization of L′ on the inverse image U ′ , which
satisfies U ′i = U i since U ′ is proper over U (cf. Lemma 4.6).                             

  If L is now a Q-line bundle on X, a Q-model of L is defined as a Q-line bundle L on a
projective model X of X such that mL is a model of mL for some m ≥ 1. By Lemma 5.10 (i),
the metric φL := m−1 φmL on L is independent of the choice of m.
Definition 5.11. A model metric on a Q-line bundle L is a metric of the form φ = φL ,
where L is a Q-model of L. A model function is a model metric φ on OX , identified with
the continuous function − log |1|φ on X an .
  A model function f is thus determined by a vertical Q-Cartier divisor D on some projective
model X of X. Every line bundle L on X admits a model metric φ, and any other model
metric on L is then of the form φ + f with f a model function.
                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                            41

Theorem 5.12. Assume that K is either discretely (or trivially) valued, or algebraically
closed. Let L, L′ be two models of a the same line bundle L, determined on models X , X ′ of
X. Then the model metrics φL , φL′ on L coincide iff the pullbacks of L, L′ to some model
X ′′ dominating both X and X ’ are equal.
Proof. If the pullbacks of L, L′ to some high enough model agree, then φL = φL′ , by
Lemma 5.10. Assume conversely that φL = φL′ . By Theorem 4.20, X and X ′ are dom-
inated by a model X ′′ which is integrally closed in X. After pulling back L and L′ to X ′′ ,
we may thus assume that L and L′ are determined on X integrally closed in X, and we
then claim that L = L′ . To see thus, let U = Spec(A) be an affine open subscheme of X
with trivializing sections τ ∈ H0 (U , L), τ ′ ∈ H0 (U , L′ ). Since L, L′ are both models of the
same line bundle L, the restrictions of τ, τ ′ to the generic fiber U = Spec(AK ) of U satisfy
τ ′ |U = uτ |U with u ∈ AK a unit. As φL and φL′ coincide, the definition of model metrics
yields |u| ≡ 1 on U i . By Theorem 4.19, A coincides with the unit ball of k · ksup on AK . As
kuksup = ku−1 ksup = 1, it follows that u and u−1 belong to A, i.e. u is a unit in A, and we
conclude that L = L′ .                                                                         
  The next result describes the behavior of model metrics under pullback.
Proposition 5.13. Let L be a Q-line bundle on X, and φL be the model metric determined
by a Q-model L of L on a model X of X. For any projective morphism f : Y → X, the
induced metric f ⋆ φ on f ⋆ L is also a model metric. More precisely, the family of projective
models Y of Y such that f extends to a K ◦ -morphism f : Y → X is cofinal in all projective
models, and we have f ⋆ φL = φf ⋆ L for any such model Y.
   If f : Y → X is flat, then Y can further be assumed to be flat over X .
Proof. Pick a projective model Y ′ of Y , and denote by Y the schematic (or flat) closure in
Y ′ ×K ◦ X of the graph of f . Then Y dominates Y ′ , and the projection Y → X extends f .
To see the last point, we may assume that L is a line bundle. Let (Ui ) be a finite open cover
of Y with trivializing sections τi ∈ H0 (Ui , L). Then (f −1 (Ui )) is an open cover of Y with
trivializing sections f ⋆ τi for f ⋆ L, and the result easily follows.
For the last point, by the Raynaud–Gruson flattening theorem [RG71], we can blow up X
and take the proper transform of Y to obtain a flat morphism f : Y ′ → X ′ of models. By
Lemma 5.10 this does not change the metrics induced by the models.                          
  We are now in a position to compare model metrics and Fubini–Study metrics (see [CMor18,
Proposition 3.8] for a related result).
Theorem 5.14. For a continuous metric φ on a Q-line bundle L over X, the following are
equivalent:
     (i) φ is a pure Fubini–Study metric;
    (ii) φ is a model metric determined by a semiample Q-model L of L, i.e. mL is a globally
         generated line bundle when m ∈ N is sufficiently divisible.
Proof. The key observation is that the Weil metric log maxi |zi | on PrK with homogeneous
coordinates [z0 : · · · : zr ] coincides with the model metric φO(1) determined by the canonical

# PRIMARY pertinent exact literal body

                ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα             (8.1)
                                       α
                          an
on the topological space X , the mixed Monge–Ampère measure     of the φi , with δX =
P
  α m  δ
      α Xα denoting the analytic fundamental class of X (see [CLD12,  §3.7] for the non-
Archimedean case).
Remark 8.1. When K = R, we define ddc φ1 ∧ . . . ∧ ddc φn ∧ δX as the image of the
corresponding measure on X(C) = XCan by the projection map XCan → X an .
Example 8.2. Assume that n = 0, i.e. X = Spec A with A a finite K-algebra. The pre-
vious construction produces a positive measure δX on Q    the finite set X an , which is described
as follows. We have a product decomposition A = i Ai into local finite K-algebras Ai
corresponding to the connected components of X. The (reduced) irreducible components of
X are given by Xi = Spec Ki , where the residue field Ki of Ai is a finite extension of K,
and the uniquePextension of the absolute value of K to Ki defines a point xi ∈ X an . The
current δX = i mi δXi is a measure on X an , and the requirement that δXi has total mass
deg π⋆ [Xi ] = [Ki : K] yields δXi = [Ki : K]δxi . As mi [Ki : K] = dimK Ai , we conclude that
                                           X
                                     δX =     (dimK Ai )δxi .
                                                 i

Proposition 8.3. For each tuple φ1 , . . . , φn of smooth metrics on Q-line bundles L1 , . . . , Ln ,
the mixed Monge–Ampère measure ddc φ1 ∧ . . . ∧ ddc φn ∧ δX satisfies the following properties:
    (i) it is a symmetric, multilinear function of the φi , and a positive Radon measure if
        the φi are semipositive, i.e. ddc φi ≥ 0;
56                         SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON
           R
      (ii) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX = (L1 · . . . · Ln );
     (iii) if L0 = L1 = OX (and hence φ0 , φ1 are smooth functions on X an ), then
      Z                                              Z
          φ0 dd φ1 ∧ dd φ2 ∧ . . . ∧ dd φn ∧ δX = φ1 ddc φ0 ∧ ddc φ2 ∧ . . . ∧ ddc φn ∧ δX .
               c        c              c
                                                                                               (8.2)

     (iv) for any complete field extension F/K, we have
                 p⋆ (ddc φ1,F ∧ . . . ∧ ddc φn,F ∧ δXF ) = ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
         where φi,F is the pullback of φi to Li,F and p : XFan → X an is the canonical projection.
Proof. (i) is straightforward. (ii) is classical in the Archimedean case, and proved in [CLD12,
Proposition 6.4.3] in the non-Archimedean case. (iii) is a consequence of the Stokes formula
(see [CLD12, Théorème 3.12.2] in the non-Archimedean case). In the Archimedean case, (iv)
is nontrivial only when K = R, F = C, in which case it holds by definition (see Remark 8.1).
In the non-Archimedean case, it is implicit in [CLD12], and can be checked as follows. Pick
a smooth, compactly supported function f on X an , and consider the smooth, compactly
supported (n, n)-form α := f ddc φ1 ∧ . . . ∧ ddc φn . According to [Gub16, Proposition 5.13],
there exists a Zariski open subset U ⊂ X with a closed embedding U ֒→ Grm,K and a
compactly supported smooth (n, n)-superform on Rr such that α is obtained by pulling-
back η by the tropicalization map Trop : U an → Rr , and
                             Z                                  Z
                                      c              c
                                f dd φ1 ∧ · · · ∧ dd φn ∧ δX =     α
                                                                          X
is defined as the integral of η on the tropical cycle Trop(U ). Unravelling the definitions, it
is clear that the pull-back αF of α to XFan is simply the pull-back of η by the tropicalization
map TropF : UFan → Rr . The construction of the tropical cycle of an algebraic variety being
invariant under ground field extension,
                                  R       Rwe have TropF (UF ) = Trop(U ) as tropical cycles,
and we conclude as desired that X α = XF αF .                                                 
   Recall from §7.3 that a continuous metric on a Q-line bundle L is psh-regularizable iff it is
a uniform limit of smooth semipositive metrics on L. If L is semiample, then any continuous
psh metric (in the sense of Definition 7.2, i.e. a uniform limit of Fubini–Study metrics) is
psh-regularizable, by Theorem 7.14.
Theorem 8.4. Let L1 , . . . , Ln be Q-line bundles on X. The measure-valued operator
                             (φ1 , . . . , φn ) 7→ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
defined so far on smooth metrics, admits a unique continuous extension to tuples of contin-
uous, psh-regularizable metrics on the Li , with respect to uniform convergence for tuples of
metrics, and the weak topology on Radon measures.
     As a direct consequence of Proposition 8.3, we get:
Proposition 8.5. For each tuple of continuous, psh-regularizable metrics (φi ),
                                            X
             ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα
                                                     α

is a positive Radon measure on X an , of total mass (L1 · . . . · Ln ). It is further symmetric
and multiadditive as a function of the φi .
                    NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                          57

   Theorem 8.4 follows from the classical Bedford–Taylor theory [BT76] in the Archimedean
case, and from its analogue in the non-Archimedean case [CLD12, Corollaire 5.6.5]. In the
present global setting, one can however provide a simple direct argument, based on the
following global version of the classical Chern–Levine–Nirenberg inequality that will be put
to use again a bit later.
Lemma 8.6. Let L0 , . . . , Ln be line bundles on X, and suppose given a pair of smooth,
semipositive metrics φi , φ′i on each Li . Then
       Z                                            Z
          (φ0 − φ′0 ) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX − (φ0 − φ′0 ) ddc φ′1 ∧ . . . ∧ ddc φ′n ∧ δX

                                                  n

# Exact primary coordinates and honest reading limits

{
  "recorded_utc": "2026-10-05T10:47:19.860280+00:00",
  "proposal": "/workspace/research/root-checks/P16.1-fixed-actual-ample-perturbation-fiber-descent-20261005-continuation92.md",
  "proposal_sha256": "447cf79483e6119171585b3630fd53890a9899fad848a9de11495db70b981877",
  "whole_current_proposal_root_read": true,
  "accepted_dependency": false,
  "units": [
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "inclusive_one_based_LF": [
        1514,
        1590
      ],
      "literal_file": "/workspace/research/root-checks/continuation92-fixed-reference-primary-read-units/BE-1805.01016v3-LF1514-1590.txt",
      "literal_sha256": "4ed55753e5105d05367576d3f1da93349e7f5cac5364f9a65c661fd310a62db9",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "inclusive_one_based_LF": [
        1970,
        1995
      ],
      "literal_file": "/workspace/research/root-checks/continuation92-fixed-reference-primary-read-units/BE-1805.01016v3-LF1970-1995.txt",
      "literal_sha256": "d2c3d7be21c8729b3501eb05741ea68a3f8554929bfa3e3eab8a436a02c67b18",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "url": "https://arxiv.org/pdf/1805.01016v3",
      "inclusive_one_based_LF": [
        2765,
        2808
      ],
      "literal_file": "/workspace/research/root-checks/continuation92-fixed-reference-primary-read-units/BE-1805.01016v3-LF2765-2808.txt",
      "literal_sha256": "392aee1a775eb026c998048169835908c4ad5bd67c560aae323d5658153488a8",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "source_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "url": "https://theses.hal.science/tel-00010990v1/document",
      "inclusive_one_based_LF": [
        3366,
        3445
      ],
      "literal_file": "/workspace/research/root-checks/continuation92-fixed-reference-primary-read-units/Thuillier-tel-00010990v1-LF3366-3445.txt",
      "literal_sha256": "67c935778502226dbd808859b73b8fa2c83897e62ae2673ec72c7eeac1e1a29e",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "source_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "url": "https://theses.hal.science/tel-00010990v1/document",
      "inclusive_one_based_LF": [
        4800,
        4902
      ],
      "literal_file": "/workspace/research/root-checks/continuation92-fixed-reference-primary-read-units/Thuillier-tel-00010990v1-LF4800-4902.txt",
      "literal_sha256": "79a2e5c936263ce7d6282c49c6ad5854efbe06c31bc9fac9725df76abff68d7f",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "url": "https://arxiv.org/pdf/1801.04713v3",
      "inclusive_one_based_LF": [
        735,
        821
      ],
      "literal_file": "/workspace/research/root-checks/continuation92-fixed-reference-primary-read-units/Wanner-1801.04713v3-LF735-821.txt",
      "literal_sha256": "87d1363b0946a9d68bf526c9b4a8eb1ba34efb0c4928fbaf61d25223fdeabae3",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    }
  ],
  "prior_pertinent_primary_units": "/workspace/research/root-checks/continuation88-fiber-reference-primary-read-units/source-read-record.json",
  "limit": "Only exact pertinent bodies read, not whole source files or every recursive semistable/model/curve-chain proof. New fixed-reference fiber descent and its proposed join remain unreviewed."
}


# PRIMARY pertinent exact literal body

    (ii) if u1 , . . . , ur are smooth functions on an open V ⊂ X an and χ is a smooth function
         defined near the range of the map V → Rr with components (ui ), then χ(u1 , . . . , ur )
         is smooth on V .
More explicitly, a function u on an open subset of X an is smooth iff it is locally of the form
                                  u = χ (log |f1 |, . . . , log |fr |)                     (4.1)
where the fi are invertible analytic functions and χ is a smooth function on an appropriate
subset of Rr . Note that this description of smooth functions also holds in the Archimedean
case (using Re zi = log |ezi |).
4.3. Models and reduction. In what follows, K is non-Archimedean (possibly trivially
valued). Recall that the valuation ring K ◦ is Noetherian if and only if K is discretely or
trivially valued. Let X be a K-scheme of finite type.
Definition 4.4. A model of X is a (separated) flat, finite type K ◦ -scheme X together with
an identification of K-schemes XK := X ⊗K ◦ K ≃ X.
                                           e
   The special fiber of a model X is the K-scheme     of finite type Xs := X ⊗K ◦ K.e We say
that a model X is proper (resp. projective) if it is proper (resp. projective) as a K ◦ -scheme.
This implies of course that X is proper (resp. projective) as a K-scheme.
   Models of X form a category, in which a morphism of models µ : X ′ → X is a morphism
of K ◦ -schemes compatible with the given identifications XK  ′ ≃ X ≃ X . If two models X ′ ,
                                                                         K
                             ′
X admit a morphism µ : X → X , then µ is unique, by separatedness, and we then say that
X ′ dominates X . We say that X ′ properly dominates X if µ is proper.
   In the trivially valued case, models of X are in 1–1 correspondence with automorphisms
of X, and X = X is thus the only model up to isomorphism.
Lemma 4.5. Any model X of X is automatically finitely presented over K ◦ .
  This follows from a general result of Raynaud–Gruson [RG71, Théorème 3.4.6], and goes
back to Nagata [Nag66, Theorem 3]. For the sake of completeness, we reproduce here
a simple argument due to Antoine Ducros [Duc], which is basically equivalent to that of
Nagata.
Proof. We claim that it is enough to prove the result when X is projective over K ◦ . Indeed,
arguing locally, we may first assume that X is affine, and we get the claim by choosing a
closed embedding in an affine space and passing to the schematic closure in the corresponding
projective space. Pick a closed embedding X ֒→ PN    K ◦ , and denote by I the corresponding
                                 ◦
homogeneous ideal of R := K [t0 , . . . , tN ]. Since both (R/I) ⊗ K and (R/I) ⊗ K      e are
Noetherian, we may choose a finitely generated homogeneous ideal I ⊂ I such that R/I ′ →
                                                                      ′
                  NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                   33


R/I becomes an isomorphism after tensoring with either K or K.            e This means that the
                                         ′     N                  ′
finitely presented closed subscheme X ⊂ PK ◦ defined by I has the same special fiber and
generic fiber as X . If we can show that X ′ is flat over K ◦ , it will coincide with the schematic
closure of its generic fiber, which will prove that X = X ′ is finitely presented. But X ′ is flat
over K ◦ if and only if the finite type K ◦ -module Vm := (R/I ′ )m is free for all m ∈ N large
enough, which is indeed the case since dimK Vm ⊗ K = dimKe Vm ⊗ K,          e by choice of I ′ . 

    A model X of X determines a compact subset X i 4 of X an and an anticontinuous5
reduction map
                                      redX : X i → Xs ,
as follows. If X is affine, i.e. X = Spec(A) with A a flat (i.e. torsion-free) finite type
K ◦ -algebra, then
                        X i = {x ∈ X an | |f (x)| ≤ 1 for all f ∈ A} ,
and the reduction redX (x) of x ∈ X i is the point of Xs induced by the prime ideal {f ∈ A |
|f (x)| < 1}. In the general case, X is covered by finitely many affine open subschemes Ui ,
whose generic fibers Ui give an affine open cover of X, and
                                      [        [
                                Xi =     Uii ⊂     Uian = X an .
                                               i      i

In the language of Example 4.3, X i consists of those semivaluations on X that admit a
center on X , and redX maps a semivaluation to its center, which is necessarily on Xs . By
the valuative criterion of properness, we thus have:
Lemma 4.6. If a model X ′ properly dominates X , then (X ′ )i = X i . If X is proper over
K ◦ (and hence X is proper over K), then X i = X an .
Example 4.7. In the trivially valued case, X is the only model up to isomorphism, and X i
coincides with the construction of [Thu07]. In particular, X i ⊂ X an , with equality iff X is
proper.
   The compact set X i associated to a model X can also be understood as (the underlying
topological space of) the generic fiber in the sense of [Ber94, §1] of the formal completion
Xb of X . As above, it is enough to consider the case where X = Spec(A) and X = Spec(A)
are affine. For any two nonzero a, a′ ∈ K ◦◦ , there exists n ≫ 1 with an ∈ K ◦ a′ , and the
formal completion Ab of A with respect to a is thus independent of the choice of a ∈ K ◦◦
(set Ab = A = A in the trivially valued case). The K ◦ -algebra Ab is flat and topologically
of finite type, and Xb = Spf(A)    b is thus an admissible formal K ◦ -scheme, whose generic

# PRIMARY pertinent exact literal body

kuksup = ku−1 ksup = 1, it follows that u and u−1 belong to A, i.e. u is a unit in A, and we
conclude that L = L′ .                                                                         
  The next result describes the behavior of model metrics under pullback.
Proposition 5.13. Let L be a Q-line bundle on X, and φL be the model metric determined
by a Q-model L of L on a model X of X. For any projective morphism f : Y → X, the
induced metric f ⋆ φ on f ⋆ L is also a model metric. More precisely, the family of projective
models Y of Y such that f extends to a K ◦ -morphism f : Y → X is cofinal in all projective
models, and we have f ⋆ φL = φf ⋆ L for any such model Y.
   If f : Y → X is flat, then Y can further be assumed to be flat over X .
Proof. Pick a projective model Y ′ of Y , and denote by Y the schematic (or flat) closure in
Y ′ ×K ◦ X of the graph of f . Then Y dominates Y ′ , and the projection Y → X extends f .
To see the last point, we may assume that L is a line bundle. Let (Ui ) be a finite open cover
of Y with trivializing sections τi ∈ H0 (Ui , L). Then (f −1 (Ui )) is an open cover of Y with
trivializing sections f ⋆ τi for f ⋆ L, and the result easily follows.
For the last point, by the Raynaud–Gruson flattening theorem [RG71], we can blow up X
and take the proper transform of Y to obtain a flat morphism f : Y ′ → X ′ of models. By
Lemma 5.10 this does not change the metrics induced by the models.                          
  We are now in a position to compare model metrics and Fubini–Study metrics (see [CMor18,
Proposition 3.8] for a related result).
Theorem 5.14. For a continuous metric φ on a Q-line bundle L over X, the following are
equivalent:
     (i) φ is a pure Fubini–Study metric;
    (ii) φ is a model metric determined by a semiample Q-model L of L, i.e. mL is a globally
         generated line bundle when m ∈ N is sufficiently divisible.
Proof. The key observation is that the Weil metric log maxi |zi | on PrK with homogeneous
coordinates [z0 : · · · : zr ] coincides with the model metric φO(1) determined by the canonical

# PRIMARY pertinent exact literal body

tuples of continuous, psh-regularizable metrics, extends to a symmetric, multilinear operator
on continuous dpsh metrics, with values in signed Radon measure. Note that Proposition 8.3
still holds for such metrics.
Example 8.11. If K is non-Archimedean and φ1 , . . . φn are R-PL metrics, then ddc φ1 ∧. . .∧
ddc φn ∧ δX has finite support. By ground field invariance, we may indeed assume that K is
algebraically closed, and that its value group is large enough to ensure that the φi become pure
after base change. By Proposition 5.16, φ1 , . . . , φn are then induced by Q-models L1 , . . . , Ln
of L1 , . . . , Ln determined on a projective model X of X. By linearity with respect to the
fundamental class [X], we may further assume that X is (geometrically) irreducible, which
allows us to assume that Xs is reduced, by Theorem 4.20. Each irreducible component Y of
Xs then determines a unique Shilov point xY ∈ Γ(X ), and
                                                       X
                        ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =  (L1 |Y · . . . · Ln |Y )δxY ,         (8.3)
                                                    Y
by [CLD12, Proposition 6.9.2] (compare [Gub07, Proposition 3.11]).
8.2. A Poincaré–Lelong formula. We start with the following integrability result.
Theorem 8.12. Let φ1 , . . . , φn be continuous, psh-regularizable metrics on line bundles
L1 , . . . , Ln , and let s ∈ H0 (X, L) be a regular section of a line bundle L, equiped with any
continuous metric φ. Then log |s|φ is integrable with respect to ddc φ1 ∧ . . . ∧ ddc φn ∧ δX , and
                                  Z
                                     log |s|φ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

depends continuously on the φi with respect to uniform convergence.
Lemma 8.13. We can find two ample line bundles A, A′ , a decreasing sequence (ψj ) of
smooth, semipositive metrics on A, and a smooth, semipositive metric ψ ′ on A′ such that
L = A − A′ and ψj − ψ ′ → log |s| pointwise.
Proof. Pick a very ample line bundle A′ such that A := L + A′ is also very ample. Let (sα )
and (s′β ) be bases of H0 (A) and H0 (A′ ), respectively, and set
                                                                                   
                           X                    X                           X
             ψj := 21 log    |s · s′β |2 + e−j   |sα |2  , ψ ′ := 21 log   |s′β |2  .
                            β                  α                             β
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                        59

These metrics are smooth and semipositive (both in the Archimedean and non-Archimedean
cases), and
                                                                
                                                   X
                           log |s| + ψ ′ = 21 log   |s · s′β |2 
                                                          β

is the decreasing limit of ψj .                                                                            

Proof of Theorem 8.12. Given any other metric φ′ on L, log |s|φ − log |s|φ′ = φ′ − φ is a con-

# PRIMARY pertinent exact literal body

2.3.2. Le théorème de rédu tion semi-stable.
   C'est i i qu'intervient le théorème de rédu tion semi-stable.
Théorème 2.3.8.  Soit X un espa e stri tement k -anoïde purement de dimension 1
et rig-lisse ; il existe une extension nie séparable k′ de k telle que le domaine k′ -anoïde
X ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
Démonstration. Il existe une extension nie séparable k1 de k et une ourbe algébrique C
propre et lisse sur k1 telles que X ⊗k k1 soit isomorphe à un domaine anoïde de C ([31℄,
theorem 1). Appliquant le théorème de rédu tion semi-stable sous la forme rigide-analytique
établie par S. Bos h et W. Lütkebohmert dans [9℄, il existe une extension nie séparable k′
de k1 telle que C ⊗k1 k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe C dont la
bre spé iale est simplement semi-stable ; 'est automatiquement une S - ourbe semi-stable
54



(remarque 2.2.9, 3). En hoisissant onvenablement k′ , on peut en outre supposer que tout
point x du bord de X ⊗k k′ satisfait à la ondition |κ(x)× | = |k′ × |.
    Envisageons X ′ = X ⊗k k′ omme un domaine stri tement k′ -anoïde de Cη et soit q :
C ′ → C un é latement admissible tel que C ′ soit une Spf(k′ ◦ )- ourbe simplement semi-stable,
ave ∂X ′ ⊂ S0 (C ′ ) (lemme 2.2.22). L'image de X ′ par l'appli ation de rédu tion Cη′ → Cs
est un ouvert U et X ′ est isomorphe à la bre générique de la Spf(k′ ◦ )- ourbe simplement
semi-stable X = C|U′ .                                                                       2
  Soient X un espa e stri tement k-anoïde purement de dimension 1 rig-lisse et k′ , k′′ deux
extensions nies galoisiennes de k telles que X ⊗k k′ et X ⊗k k′′ soient isomorphes aux bres
génériques de ourbes stri tement semi-stables ; étant donnée une extension nie galoisienne
K de k oiant k′ et k′′ , la proposition 2.3.7 implique l'identité des espa es H(X ⊗k k′ ) et
                   ′                                          ′′
H(X ⊗k K)Gal(K/k ) (resp. H(X ⊗k k′′ ) et H(X ⊗k K)Gal(K/k ) ), d'où dé oule l'égalité
                               ′                                              ′′
              H(X ⊗k k′ )Gal(k /k) = H(X ⊗k K)Gal(K/k) = H(X ⊗k k′′ )Gal(k /k) .
Le théorème pré édent permet ainsi de dénir, pour tout espa e stri tement k-anoïde X
purement de dimension 1 et rig-lisse, un sous-espa e ve toriel H(X) de C0 (|X|, R) : H(X) =
                ′
H(X ⊗k k′ )Gal(k /k) ⊂ C0 (|X|, R), k′ étant une extension nie galoisienne de k telle que X ⊗k k′
soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-stable.
   Désignant par C la atégorie dont les objets sont les espa es stri tement k-anoïdes, pure-
ment de dimension 1 et rig-lisses, et les morphismes les immersions anoïdes, il dé oule de la
proposition 2.3.3 que l'on vient ainsi de dénir un fon teur H sur Cop à valeurs dans VectR .
  Nous aurons besoin des deux résultats suivants.
Lemme 2.3.9.  Pour tout espa e stri tement k -anoïde Y rig-lisse et purement de di-
mension 1, l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
induit un isomorphisme du sous-espa e H(Y ) sur Hom(Γ(Y ), R).
Démonstration. Soit k′ une extension galoisienne nie de k telle que l'espa e stri tement
k′ -anoïde Y ⊗k k′ soit isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement semi-
                                                                                            ′
stable Y . La proje tion anonique p : Y ⊗k k′ → Y induit une bije tion de Γ(Y ⊗k k′ )Gal(k /k)
sur Γ(Y ) et l'appli ation de restri tion
                                   C0 (|Y |, R) → Hom(Γ(Y ), R)
 oïn ide ave l'appli ation induite par la restri tion
                            C0 (|Y ⊗k k′ |, R) → Hom(Γ(Y ⊗k k′ ), R)
                                                                                           ′
entre les sous-espa es des invariants sous Gal(k′ /k) ; puisque H(Y ) = H(Y ⊗k k′ )Gal(k /k) , la
 on lusion dé oule de la proposition 2.3.2.                                                    2
Lemme 2.3.10.  Soient Y un espa e stri tement k -anoïde onnexe, de dimension 1 et
rig-lisse, et (hn ) une suite roissante de fon tions appartenant à H(Y ). L'alternative suivante
est vraie :
    soit la suite (hn ) onverge, uniformément sur Y , vers une fon tion h ∈ H(Y ),
    soit la suite (hn ) onverge, lo alement uniformément sur Y − Γ(Y ), vers ∞.
Démonstration. Soient k′ une extension nie galoisienne de k telle que Y ′ = Y ⊗k k′ soit
isomorphe à la bre générique d'une Spf(k′ ◦ )- ourbe simplement nodale Y′ et p : Y ′ → Y la
proje tion anonique. Si l'assertion est démontrée pour la suite (p∗ hn ) dans H(Y ′ ), elle l'est
                                                                      ′
également pour la suite (hn ) : en eet, puisque H(Y ) = H(Y ′ )Gal(k /k) , il sut de s'assurer
                                                                                               55



que la fon tion limite h ∈ H(Y ′ ) du premier as de l'alternative est invariante sous Gal(k′ /k) ;
utilisant l'isomorphisme Gal(k′ /k)-équivariant de restri tion
                                   H(Y ′ ) → Hom(Γ(Y ′ ), R),
                                                    ′
 ela dé oule de l'identité entre Γ(Y ) et Γ(Y ′ )Gal(k /k) .
   Vu la dénition de l'espa e H(Y ′ ) = H(Y ′ ) (dénition 2.3.1), le résultat pour une suite
 roissante dans H(Y ′ ) s'obtient par appli ation de la proposition 1.2.12.                 2
2.3.3. Le fais eau HX .
  Soit X une ourbe stri tement k-analytique lisse. Le fon teur H : Cop → VectR donne
naturellement naissan e à un préfais eau HX sur le site rigide XR de X (2.1.1) : étant donné
un objet V de XR , les domaines stri tement k-anoïdes de X ontenus dans V forment un
système indu tif ltrant I(V ) (les morphismes sont les in lusions) et l'on pose

# PRIMARY pertinent exact literal body

3.3.2. Fon tions de Green élémentaires
   L'étude de l'opérateur ddc ommen e par la onstru tion de fon tions lisses parti ulières.
Proposition 3.3.7.  Soit X une ourbe stri tement k -analytique lisse.
   (i ) Si X est propre et onnexe, il existe, pour tous points x, y ∈ I(Y ), une unique fon tion
lisse gx,y ∈ A0 (X) telle que
                                     
                                        ddc gx,y = δy − δx
                                        gx,y (x) = 0.
La fon tion
                                I(X)2 → R, (x, y) 7→ gx,y (y)
                                                                                                 81



est symétrique.

   (ii ) Quels que soient le domaine k-anoïde onnexe V ⊂ X et le point x ∈ I(V ) − ∂V , il
existe une unique fon tion lisse gxV ∈ A0 (X)V qui s'annule identiquement sur ∂V et telle que
le support de la mesure νxV = ddc gxV + δx soit ontenu dans ∂V .
   La fon tion gxV est stri tement positive sur V − ∂V .
Démonstration.
(i) Supposons la ourbe X propre et onnexe. Quels que soient les points x, y ∈ I(X), l'ouvert
Ω = X − {x, y} est relativement ompa t et il existe, pour tout λ ∈ R, une unique fon tion
hλ ∈ C0 (X, R) harmonique sur Ω et telle que hλ (x) = 0, hλ (y) = λ (propositions 3.1.19 et
3.1.20). C'est une fon tion lisse et la mesure ddc hλ s'é rit c(λ)(δy − δx ) ( orollaire 3.2.11, (i)
et proposition 3.2.12).
   Les seules fon tions harmoniques sur X étant les fon tions onstantes, hλ n'est pas harmo-
nique si λ 6= 0 ; l'appli ation linéaire
                                                     Z
                                   c : R → R, c(λ) =       ddc hλ
                                                        {x}

est don un isomorphisme. Il existe ainsi un unique λ ∈ R tel que c(λ) = 1.
   La symétrie de la fon tion I(X)2 → R, (x, y) 7→ gx,y (y) se déduit immédiatement de la
proposition 3.2.12 :
                                       Z             Z
                 gx,y (y) − gy,x (x) =     gx,y δy −     gy,x δx
                                         X             X
                                          Z                    Z
                                     = −     gx,y (δx − δy ) +     gy,x (δy − δx )
                                          ZX                 Z X
                                     = −     gx,y ddc gy,x +     gy,x ddc gx,y
                                             X                  X
                                     = 0.
(ii) Soient V un domaine k-anoïde onnexe de X et x ∈ I(V ) − ∂(V ). L'espa e ve toriel
C0 (V, R) ∩ Γ(V − (∂V ∪ {x}), HX ) est isomorphe à Hom(∂V ∪ {x}, R) via l'appli ation de
restri tion ( orollaire 3.1.21) et le sous-espa e F onstitué
                                                       R     des fon tions identiquement nulles
sur ∂V est une droite. La forme linéaire F → R, ϕ 7→ {x} ddc ϕ est un isomorphisme ( ar non
nulle)R et il existe don une unique fon tion gxV ∈ A0 (X)V telle que
    {x} ddc gxV = −1 ;
    gxV s'annule identiquement sur ∂V .
   La mesure νxV = ddc gxV + δx est à support dans ∂V .
   La fon tion gxV n'est pas identiquement nulle sur V − ∂V ( ar non harmonique) ; puisqu'elle
s'annule en tout point de ∂V , elle admet don un extremum lo al stri t dans V − ∂V . L'inéga-
lité (ddc gxV )|V −∂V = −δx ≤ 0 implique qu'il ne peut s'agir que d'un maximum par appli ation
du orollaire 3.2.11, (ii) : gxV est don positive sur V . La stri te positivité sur V − ∂V dé oule
immédiatement de la onnexité de V et de l'harmoni ité de gxV sur V − (∂V ∪ {x}).               2

Remarque 3.3.8.  Nous étendrons ultérieurement le point (i) de la proposition pré édente
(théorème 3.3.13) tandis que la se tion 3.6 sera onsa rée à la généralisation du point (ii).

Corollaire 3.3.9.  Soit V ⊂ X un domaine k -anoïde onnexe ; reprenant les nota-
tions introduites dans la proposition 3.3.7 :
82



   (i ) gxV (y) = gyV (x) pour tous points x, y ∈ I(V ) − ∂V ;
   (ii ) pour toute fon tion b sur ∂V , la fon tion ontinue sur V et harmonique V − ∂V qui
 oïn ide ave b sur ∂V prend, au point x, la valeur
                                              Z
                                                   b dνxV .
                                                          ∂V

   (iii ) Pour tout x ∈ I(V ) − ∂V , νxV est une mesure de probabilité dont le support est la
frontière de la omposante onnexe de x dans V − ∂V .
Démonstration. Le point (i) dé oule dire tement de la proposition 3.2.12 et de la nullité de
gxV , gyV sur ∂V :
                                       Z                            Z
                         gxV (y) = −           gxV   ddc gyV = −            gyV ddc gxV = gyV (x).
                                           X                            X

   Soit b ∈ Hom(∂V, R) et soit h la fon tion dans H(V ) qui oïn ide ave b sur ∂V ( orollaire
3.1.21) ; le support de la mesure ddc h est ontenu dans ∂V et, appliquant de nouveau la
proposition 3.2.12,
                Z             Z              Z                 Z
                    V    c            c V           V
            0=     gx dd h =     h dd gx =      h dνx − h(x) =      b dνxV − h(x).
                     X             V                           X                           ∂V

  Le point (iii) se déduit immédiatement du pré édent : quelle que soit en eet la fon tion
positive b sur ∂V , la fon tion h ∈ H(V ) qui oïn ide ave b sur ∂V est positive et don
                                     Z
                                         b dνxV = h(x) ≥ 0.
                                                 ∂V

L'égalité h(x) = 0 est vériée si et seulement si h est identiquement nulle sur la omposante
 onnexe de x dans V − ∂V (prin ipe du maximum), d'où l'assertion sur le support de la
mesure νxV . Enn, le as de la fon tion onstante b = 1 montre que νxV est de masse totale 1.
2

     Nous sommes maintenant en mesure d'a hever la démonstration de la proposition 3.1.3.

# PRIMARY pertinent exact literal body

on U an .
   A continuous metric k k on Lan is psh-approximable if there is a sequence of smooth
psh metrics k kk on Lan such that supx∈X an | log(ksx (x)k/ksx (x)kk )| converges to zero
for any local section sx of L that does not vanish in x. Clearly, this is independent of
the choice of sx .
Definition 3.26. Let X be a proper variety over K and let L be a line bundle on X.
A semistable formal model of (X, L) is a pair (X , L) consisting of a semistable formal
model X of X an and a line bundle L on X such that L |X an ≃ Lan . Note that we always
may assume that X is strictly semistable by the semistable reduction Theorem [BL93,
Ch. 7] since K is algebraically closed.
   Let (X , L) be a semistable formal model of (X, L⊗m ) for m ∈ N>0 . Then one can
define a continuous metric on Lan in the following way: If U is a formal trivialization
of L and s is a section of Lan on U η such that s⊗m corresponds to λ ∈ OX an (U η ) with
respect to this trivialization, then
                                                   1
                             − log ks(x)kL := −       log |λ(x)|
                                                   m
for all x ∈ U η . This definition is independent of all choices and shows immediately that
the defined metric is continuous. Metrics of this form are called Q-formal metrics, and
they are called formal metrics if m = 1.
   Let OX be the trivial line bundle on X. A function f : X an → R of the form f =
− log k1kL for a formal metric k kL associated to a semistable formal model of (X, O X )
is called model function.
   We have the following statements for model functions due to Chambert-Loir and
Ducros and Katz, Rabinoff and Zureick-Brown. The first theorem is a direct consequence
of a result of Chambert-Loir and Ducros in [CD12, §6.3].
Theorem 3.27. Let X be a projective variety over K and f = − log k1kL be a model
function on X an for a semistable formal model (X , L) of (X, O X ).
     i) The function f is locally approximable on X an , and so the Monge-Ampère mea-
        sure MA(f ) exists.
    ii) We have the following identity of measures
                                         X
                                MA(f ) =    degL (Y )δζY ,
                                           Y

       where Y runs over all irreducible components of the special fiber X s and ζY is the
       unique point in X an mapped to the generic point of Y under the reduction map
       (see [Ber90, Proposition 2.4.4]).
Proof. By [CD12, Corollaire 6.3.5], we know that there are line bundles L1 , L2 on X
with formal models L1 , L2 such that OX = L1 ⊗ L−1              −1
                                                 2 , L = L1 ⊗ L2 , the corresponding
metrics k kL1 and k kL2 are psh-approximable and
                         − log k · kL = − log k · kL1 + log k · kL2
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 15


on X an . Let k ki,k be a sequence of smooth psh metrics converging uniformly to k · kLi
on X an . For every point x in X an , let U be an open subset of X with x ∈ U an and s an
invertible section of L1 = L2 on U . Then − log kskLi,k is a smooth psh function on U an
for i = 1, 2 and for every k ∈ N
        − log k1kL = − log kskL1 + log kskL2 = lim − log ksk1,k + lim log ksk2,k .
                                                    k→∞                  k→∞

Hence, the function f = log k1kL is locally approximable.
  The second assertion is shown in [CD12, §6.9].                                                

  The slope formula for line bundles by Katz, Rabinoff, and Zureick-Brown in [KRZB15]
implies directly the following theorem.
Theorem 3.28. Let X be a smooth proper algebraic curve over K and f = − log k1kL
be a model function on X an for a semistable formal model (X , L) of (X, O X ). The
restriction F of f to S(X ) is a piecewise affine function and f = F ◦ τX on X an .
Furthermore, we have
                               MA(f ) = ddc F = ddc f.
Proof. This follows directly from [KRZB15, Theorem 2.6] using Theorem 3.27.                     

        4. Comparison of the two notions of subharmonic functions
  In this section, we consider a smooth proper algebraic curve X over K. We show
that every subharmonic function on X an is psh and that every continuous psh function
on X an is subharmonic. In particular, the notion of subharmonic and the notion of psh
agree for continuous functions.

4.1. Thuillier’s subharmonic functions are also subharmonic in the sense of
Chambert-Loir and Ducros. In this subsection, we show that every subharmonic
function on an open subset of X an is psh. First, we prove that every lisse subharmonic
function is psh and that every subharmonic function is locally integrable. Then we use
these results and the fact that a subharmonic function is the limit of subharmonic lisse
functions from Proposition 2.8 to prove the general claim.
Remark 4.1. Every signed Radon measure µ on an open subset W of X an defines the
following current
                                                 Z
                        [µ] : Cc∞ (W ) → R, g 7→   g dµ
                                                          W
(see [Gub16, Example 6.3]). Consider a smooth function f ∈ C ∞ (W ), then we have seen
in Proposition 3.13 that the smooth form d′ d′′ f corresponds to a signed Radon measure
which we also denote by d′ d′′ f . Using the theorem of Stokes [Gub16, Theorem 5.17], we
get d′ d′′ [f ] = [d′ d′′ f ]. Recall that a function is called psh if and only if this current is
positive.

# Exact primary coordinates and honest reading limits

{
  "recorded_utc": "2026-10-05T10:57:37.647712+00:00",
  "proposal": "/workspace/research/root-checks/P16.1-curve-current-identity-and-boundary-clarifications-20261005-continuation93.md",
  "proposal_sha256": "c8e83ff56c71a8c3d7ecd1e67733f51e57a741883ba84d841e0003f5bc5bcdf6",
  "whole_current_proposal_root_read": true,
  "accepted_dependency": false,
  "units": [
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "url": "https://arxiv.org/pdf/1801.04713v3",
      "inclusive_one_based_LF": [
        232,
        312
      ],
      "literal_file": "/workspace/research/root-checks/continuation93-curve-current-primary-read-units/Wanner-1801.04713v3-LF232-312.txt",
      "literal_sha256": "892c17bcb6500825d2e1fbb79a74f96defbd7fc3c3b852e369c38af4a7d15ad4",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Wanner-1801.04713v3-20261004.txt",
      "source_sha256": "e83a0516614296bc5720c6af22845255031671293dfab9acd05b12284984798f",
      "url": "https://arxiv.org/pdf/1801.04713v3",
      "inclusive_one_based_LF": [
        822,
        990
      ],
      "literal_file": "/workspace/research/root-checks/continuation93-curve-current-primary-read-units/Wanner-1801.04713v3-LF822-990.txt",
      "literal_sha256": "b3ed876f1e87337ea00617890c4a99148615a4affaf61334d6ecf89b4c3815d8",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Gubler-Kunnemann-1406.7637v3-20261005.txt",
      "source_sha256": "4336903644edf53838f829cf22a3326257f909adfae1f906738f9f8534d1826b",
      "url": "https://arxiv.org/pdf/1406.7637v3",
      "inclusive_one_based_LF": [
        353,
        385
      ],
      "literal_file": "/workspace/research/root-checks/continuation93-curve-current-primary-read-units/GK-1406.7637v3-LF353-385.txt",
      "literal_sha256": "9504bb024cb31185fdc70ee0c44841e6ea619c4038e975ba0cd6567ee6413a32",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    },
    {
      "source": "/workspace/research/shared-sources/Gubler-Kunnemann-1406.7637v3-20261005.txt",
      "source_sha256": "4336903644edf53838f829cf22a3326257f909adfae1f906738f9f8534d1826b",
      "url": "https://arxiv.org/pdf/1406.7637v3",
      "inclusive_one_based_LF": [
        3380,
        3595
      ],
      "literal_file": "/workspace/research/root-checks/continuation93-curve-current-primary-read-units/GK-1406.7637v3-LF3380-3595.txt",
      "literal_sha256": "d8f21d84c9c9e830eb138680f59a21420e2ad5587f3c902e1c896930e095756e",
      "whole_pertinent_unit_root_read": true,
      "whole_source_file_root_read": false,
      "all_recursive_proofs_root_read": false
    }
  ],
  "GK_pdf": "/workspace/research/shared-sources/Gubler-Kunnemann-1406.7637v3-20261005.pdf",
  "GK_pdf_sha256": "62c7e4dfebab75d725f529c6ef78c300856c63fd050a9399e8a86879e569315d",
  "live_primary_observation": "/workspace/research/root-checks/continuation93-live-curve-model-and-fiber-primary-observation.json",
  "live_pertinent_bodies_root_read": [
    {
      "url": "https://stacks.math.columbia.edu/tag/0AY8",
      "rendered_lines": [
        24,
        39
      ]
    },
    {
      "url": "https://stacks.math.columbia.edu/tag/0GIQ",
      "rendered_lines": [
        22,
        24
      ]
    }
  ],
  "limit": "Exact pertinent primary statements and proof bodies only, not whole sources or all recursive curve/model/semistable proofs. Fresh applications unreviewed."
}


# PRIMARY pertinent exact literal body

Definition 2.3.        i) For a strictly semistable proper formal R-curve Y, we define
                              H(Y) := τY∗ (H(S(Y), ∂ Y η )),
        where ∂ Y η is the Berkovich boundary (see [Thu05, §2.1.2]) of the generic fiber
        Yη.
    ii) Let Y be a strictly affinoid domain in X an . Then there exists a strictly semistable
        R-curve Y and an isomorphism ϕ : Y → Y η (see [BL85] and [Thu05, Théorème
        2.3.8]), and we define the harmonic functions on Y as
                                   H(Y ) := ϕ∗ (H(Y)).
       Note that the definition is independent of ϕ and Y [Thu05, Proposition 2.3.3].
Definition 2.4. Let W be an open subset of X an . Then f : W → [−∞, ∞) is called
subharmonic if f is upper semi-continuous, f 6≡ −∞ on every connected component of
W and for every strictly K-affinoid domain Y in W and every harmonic function h on
Y , we have
                             (f |∂Y ≤ h|∂Y ) ⇒ (f |Y ≤ h).
  We recall some important properties of subharmonic functions from [Thu05, §3].
Proposition 2.5. The subharmonic functions form a sheaf on X an .
Proof. See [Thu05, Corollaire 3.1.13].                                                     
                                                                    ′ an
Proposition 2.6. Let X, X ′ be smooth algebraic curves, ϕ : (X ) → X an be a mor-
phism of K-analytic spaces and W be an open subset of X an . If f : W → R is a subhar-
monic function on W , then ϕ∗ f is a subharmonic function on ϕ−1 (W ).
Proof. See [Thu05, Proposition 3.1.14].                                                    
  In the following, we define the class of lisse functions using the characterization in
[Thu05, Proposition 3.2.4]. Note that we can replace compact strictly analytic domains
by strictly affinoid domains looking at the proof of [Thu05, Proposition 3.2.4] and using
[Thu05, Proposition 3.2.2].
Definition 2.7. Let W be an open subset of X an . A function f : W → R is called lisse
if for every strictly affinoid domain Y ⊂ W , there exists a strictly semistable formal
R-curve Y such that Y = Y η and f |Y = F ◦ τY for a piecewise affine function F on S(Y).
Proposition 2.8. Let W be an open subset of X an and f a subharmonic function on
W . For every relatively compact open subset W ′ of W , there is a decreasing net hfj i of
lisse subharmonic functions converging pointwise to f on W ′ .
Proof. See [Thu05, Théorème 3.4.2].                                                        
Definition 2.9. Let W be an open subset of X an and f : W → R be a lisse function on
W , then we denote by ddc f the unique real measure on W that
6                                         V. WANNER


     i) has discrete support contained in the set of type II and III points of X an , and
    ii) coincides with ddc F on Y whenever f = F ◦ τY on a strictly affinoid domain
        Y = Y η in W .
This measure exists and is unique by [Thu05, Théorème 3.2.10].
   With the help of this operator ddc , one can define harmonic functions on open subsets
in the Berkovich topology (see [Thu05, Corollaire 3.2.11]).
Definition 2.10. A function f : W → R on an open subset W of X an is called harmonic
if f is lisse and ddc f = 0. Harmonic functions form a sheaf on X an , which we denote by
HX .
  This measure leads also to a further way to decide whether a lisse function is subhar-
monic or not.
Proposition 2.11. A lisse function f : W → R is subharmonic if and only if ddc f ≥ 0.
Proof. See [Thu05, Proposition 3.4.4].                                                   
Proposition 2.12. Let Y    be a connected strictly affinoid domain in X an and x ∈ Y \∂Y
be a point of type II or III. Then there exists a unique lisse function gxY on X an such
that
      i) gxY is strictly positive on Y \∂Y and equal to zero on ∂Y ∪ X an \Y ;
     ii) ddc gxY is supported on ∂Y ∪ {x} with ddc gxY = −δx in a neighborhood of x;
    iii) for every harmonic function h on Y we have
                                             Z
(2.1)                                 h(x) =    h ddc gxY .
                                             ∂Y
Proof. See [Thu05, Proposition 3.3.7 & Corollaire 3.3.9].                                
Corollary 2.13. Let W be an open subset of X an . A continuous function f : W → R
is subharmonic if and only if for every connected strictly affinoid domain Y ⊂ W and
every point x ∈ Y \∂Y of type II or III, we have
                                   Z
                                        f ddc gxY ≥ 0.
                                      W
Proof. Consider a strictly affinoid domain Y in W and a harmonic function f on Y with
f ≤ h on ∂Y . As explained in [Thu05, Remarque 3.1.10], we may assume f = h on ∂Y ,
and without loss of generality Y is connected. For every x ∈ Y \∂Y of type II or III,
Equation (2.1) implies that
        Z              Z                       Z
                c Y              c Y
           f dd gx =        f dd gx − f (x) =       h ddc gxY − f (x) = h(x) − f (x).
         W               ∂Y                      ∂Y
                  R
Hence, we have W f ddc gxY ≥ 0 for every type II or III point in Y if and only if
h(x) ≥ f (x) for every type II or III point in Y . Since f and h are continuous and the
type II and III points are dense, the last is equivalent to h − f ≥ 0 on Y .          

3. Preliminaries on subharmonic functions in the sense of Chambert-Loir

# PRIMARY pertinent exact literal body

   Analogously, for every lisse function f : W → R we get a current [ddc f ] for the corre-
sponding measure ddc f from Definition 2.9 which is positive if and only if f is subhar-
monic (cf. Proposition 2.11).
Proposition 4.2. Let W be an open subset of X an and f : W → R a lisse function.
For every type II point x ∈ W , there is an open neighborhood V of x in W on which the
currents d′ d′′ [f ] and [ddc f ] agree.
16                                          V. WANNER


Proof. Consider a point x ∈ W and let Y be a strictly affinoid domain containing x
in its interior. Since f is lisse, there is a strictly semistable formal model Y of Y with
corresponding skeleton S(Y) and f = F ◦ τY on S(Y) for a piecewise affine function F
on S(Y).
   If x ∈
        / S(Y), then f is constant on an open neighborhood V of x, and so
                               d′ d′′ [f ] = [d′ d′′ f ] = [0] = [ddc f ]
on V .
   If x ∈ S(Y), we may assume that x is a vertex in S(Y). Let e1 = [x, y1 ], . . . , er = [x, yr ]
be the edges in S(Y) emanating from x, v1 , . . . , vr the corresponding tangent directions
and λi := dvi F (x). By blowing up Y, we may assume that F |ei is affine, d(x, yi ) ∈ Q and
that we divide the edge ei by an additional vertex yi′ with d(x, yi ) = 2d(x, yi′ ). Denote
this blowing up by Y ′ , and the tangent direction corresponding
                                                              S     to [yi′ , yi ] by vi′ . Define
the piecewise affine functions Fi on the closed subset Γ := i=1,...,r [x, yi ] of S(Y ′ ) by the
following data
            Fi (x) = 0, dvi (Fi )(x) = sgn(λi )δij and dvi′ (Fi )(yi′ ) = −dvi (Fi )(x).

Set fi = Fi ◦τY ′ on Y ′ := τY−1
                               ′ (Γ), which is a strictly affinoid domain in W . By definition,

fi = 0 on ∂Y for every i ∈ {1, . . . , r}. Note that ∂Y ′ = ∂Γ (cf. [JW18, Lemma 5.4]).
              ′

Hence, we can extend fi to X an by setting fi = 0 on X an \Y ′ . Then we have a G-
covering of X an on which fi is piecewise S linear, and      so fi is a model function on X an
[GK14, Proposition 8.11]. Set Γ := i=1,...,r [x, yi ] and V := τY−1
                                      ′                  ′                    ′ ◦
                                                                         ′ ((Γ ) ), which is an

open neighborhood of x in W . By the definition of fi on V , we have on V ⊂ Y
                                     Xr                            r
                                                                   X
(4.1)       f = F ◦ τY = F ◦ τY ′ = (   |λi |Fi ) ◦ τY ′ + F (x) =   |λi | · fi + F (x)
                                          i=1                                   i=1

and
                                            r
                                            X                r
                                                             X
                           c          c
(4.2)                   dd f = dd F =             λi δx =          |λi |(ddc (fi )).
                                            i=1              i=1

Since the functions fi are model functions, we know that they are locally approximable
on V and MA(fi ) = ddc (fi ) by Theorem 3.27 and Theorem 3.28. Let 0 ≤ g ∈ Cc∞ (V ).
Then for every i ∈ {1, . . . , r} we have by Lemma 3.23 and MA(fi ) = ddc (fi ) that
                                  Z               Z
                 ′ ′′
                d d [fi ](g) =       g dMA(fi ) =   g ddc (fi ) = [ddc fi ](g).
                                  V                      V

Linearity and the Equations (4.1) and (4.2) imply consequently d′ d′′ [f ](g) = [ddc f ](g).
                                                                                          
Proposition 4.3. Let W be an open subset of X an and f : W → R be a lisse function.
If f is subharmonic, then f is psh.
Proof. Note that the property to be psh, i.e. d′ d′′ [f ] ≥ 0, is a local property by Proposi-
tion 3.19.
   If x is of type I or IV, the lisse function f is constant on an open neighborhood V of
x in W by the definition of lisse. Hence, d′ d′′ [f ] = [d′ d′′ f ] = 0 on V .
   If x is of type II, we have seen in Proposition 4.2 that there is an open neighborhood
V of x in W such that d′ d′′ [f ] = [ddc f ] on V . Since f is subharmonic, the measure ddc f
on W is non-negative by Proposition 2.11, and so we have d′ d′′ [f ] = [ddc f ] ≥ 0 on V .
  COMPARISON OF TWO NOTIONS OF SUBHARMONICITY ON NON-ARCHIMEDEAN CURVES 17


   If x is of type III, we choose a strictly affinoid domain Y that contains x in its interior.
Since f is lisse, there is a strictly semistable model Y of Y with corresponding skeleton
S(Y) and a piecewise affine function F on S(Y) such that f = F ◦ τY on Y .
   If x is not contained in S(Y), then there is as in the first case an open neighborhood
V of x in W on which f is constant, and so d′ d′′ [f ] = [d′ d′′ f ] = 0 on V .
   If x ∈ S(Y), then there is an edge e in S(Y) such that x lies in the interior of e. The
closed annulus A := τY−1 (e) is isomorphic to a closed annulus A′ = trop−1 ([val(b), val(a)])
in G1,an
      m    for some a, b ∈ K × with |a| < |b| and trop := − log |T |. Thus, we can identify
                                                                                        ∼
e with the real interval [val(b), val(a)] via trop ◦Φ for a fixed isomorphism Φ : A −   → A′ .
Since e is isometric to [val(b), val(a)], we can define a function
                     ψ : [val(b), val(a)] → R; z 7→ F ((trop ◦Φ)−1 (z)).
                                                           1,an
Then ψ extends to a piecewise affine function on trop(Gm        ) = R, and its restriction to
the connected components of R\{trop(Φ(x))} is affine with outgoing slopes at trop(Φ(x))
equal to the ones of F at x on e. We have required that f is subharmonic, so the sum of
the outgoing slopes at x is greater than or equal to zero by Proposition 2.11. Hence, ψ is
convex on R, and so we can find smooth convex functions ψi on R converging uniformly
                                                                                        1,an
to ψ. Then ψi ◦ trop are smooth psh functions on trop−1 (val(b), val(a)) ⊂ Gm                by
Proposition 3.20. By Remark 3.21, the pullbacks fi := Φ∗ (ψi ◦ trop) are smooth psh
function on V ′ := τY−1 (e◦ ) converging uniformly to f on V ′ . Note that by [BPR13,
Lemma 2.13 & 3.8], the map trop = − log |T | factors through τA and τA = τY on A.
Hence, the function f is itself psh on V ′ by Lemma 3.23, i.e. d′ d′′ [f ] ≥ 0 on V ′ .       
Proposition 4.4. Let W be an open subset of X an and f : W → [−∞, ∞) be a subhar-
monic function, then f is locally integrable.
                                   R
Proof. We have to show that W f ∧ ω is finite for every ω ∈ Ac1,1 (W ). By [Gub16,
Proposition 5.13], we may assume that the (1, 1)-form ω is of the form ω = trop∗U ωtrop for
a tropical chart (V, ϕU ) of W and a form ωtrop ∈ A1,1c (tropU (V )). The closed embedding
ϕU is given by γ1 , . . . , γr ∈ O(U )× , and we denote by H the set of zeros and poles of
γ1 , . . . , γr on X. We choose a strictly semistable model X of X such that the type I
points of H lie in distinct connected components of X an \S0 (X ) (see [BPR13, Theorem
4.11 & 5.2]), where S0 (X ) denotes the vertices of the skeleton S(X ) corresponding to X .
By [BPR13, Lemma 2.13 & 3.8], we have the following commutative diagram
                                                  tropU
                                             V            // Ω
                                                        ③③==
                                        τX            ③③
                                                   ③③③trop
                                                ③         U

                                        S(X )

where τX : X an → S(X ) is the retraction map corresponding to X and Ω := tropU (V ).
The retraction map τX is defined in such a way (see [BPR13, Lemma 3.4 & Definition
3.7]) that every connected component of X an \S(X ) is retracted to a single point in
S(X ). Due to this fact and the commutativity of the diagram, the form ω = trop∗U ωtrop
is supported on S(X ). Since the restriction of the subharmonic function f to S(X ) is
continuous by [Thu05, Proposition 3.4.6], we get
                              Z           Z
                                  f ∧ω =     (f ◦ τX ) ∧ ω
                                  W                 W
is finite. Hence, f is locally integrable.                                                   
18                                         V. WANNER


Theorem 4.5. Let W be an open subset of X an and f : W → [−∞, ∞) be a subharmonic
function, then f is psh.
Proof. We already know by Proposition 4.4 that f is locally integrable, so it remains
to show that d′ d′′ [f ] is non-negative, which is also a local property by Proposition 3.19.
Since X an is a locally compact Hausdorff space, we can find for every x ∈ W a relatively
compact neighborhood W ′ of x in W . By Proposition 2.8, there is a decreasing net
hfj i of lisse subharmonic functions converging pointwise to f on W ′ . Consider a non-
negative function g ∈ Cc∞ (W ′ ). Then there are smooth forms ω + , ω − ∈ A1,1 (X an ) such
that d′ d′′ g = ω + − ω − and the corresponding signed Radon measures from Proposition
3.13 are non-negative [CD12, Lemme 5.3.3]. By [CD12, Corollaire 3.3.4], we can find a
smooth non-negative function η ∈ Cc∞ (W ′ ) such that η ≡ 1 on supp(g), and hence
                               d′ d′′ g = ηd′ d′′ g = ηω + − ηω −
on W ′ . The smooth (1, 1)-forms ηω ± are contained in Ac1,1 (W ′ ) and the corresponding
RadonRmeasures are still non-negative and have compact support by Proposition 3.13.
Thus, W ′ f ∧ ηω ± is finite (see Proposition 4.4), and we have
                             Z                   Z
                                  f ∧ ηω ± = lim     fj ∧ ηω ±
                               W′                  j   W′
by [BFJ15, Lemma 2.23]. Together, we get
                      Z                  Z             Z
          ′ ′′                    ′ ′′              +
        d d [f ](g) =      f ∧ ηd d g =      f ∧ ηω −      f ∧ ηω −
                        W′                W′            W′
                           Z               Z                   Z
                                       +              −
                    = lim(     fj ∧ ηω −       fj ∧ ηω ) = lim     fj ∧ d′ d′′ g.
                         j   W′                   W′               j   W′
                                     R             ′ ′′
By Proposition 4.3, we know that         W ′ fj ∧ d d g ≥ 0 for every fj in the net, and hence
d′ d′′ [f ](g) ≥ 0.                                                                         

4.2. Continuous subharmonic functions in the sense of Chambert-Loir and
Ducros are subharmonic in the sense of Thuillier. In this subsection, we prove
that every continuous psh function is subharmonic in the sense of Thuillier. The key
tool of the proof is the coincidence of the Monge-Ampère measure and the measure ddc g
for model functions (see Theorem 3.28).

# PRIMARY pertinent exact literal body

                        Notations and Terminology
   Throughout this paper K denotes an algebraically closed field endowed with
a complete non-trivial non-archimedean absolute value | |, valuation ring K ◦ ,
and corresponding valuation v = − log | |. Let Γ := v(K × ) be the value group.
   In A ⊂ B, A is strictly smaller than B. The complement of A in B is denoted
by B \ A. The zero is included in N and in R+ .
   The group of multiplicative units in a ring A with 1 is denoted by A× .
An (algebraic) variety over a field is an irreducible separated reduced scheme of
finite type. The terminology from convex geometry is explained in the appendix.

       1. Tropical intersection theory with smooth weights
   In tropical geometry, a tropical cycle is given by a polyhedral complex whose
maximal faces are weighted by integers satisfying a balancing condition along
the faces of codimension 1. In this section, we generalize the notion of a tropical
cycle allowing smooth real functions on the maximal faces as weights. This is
similar to the tropical fans with polynomial weights introduced by Esterov and
François [Est12, Fra13]. We generalize basic facts from stable tropical intersec-
tion theory and introduce the corner locus of a piecewise smooth function.
   Throughout this section N and N 0 denote free Z-modules of finite rank r
and r0 . We write NR = N ⊗Z R and NR0 = N 0 ⊗Z R. Every integral R-affine
polyhedron σ of dimension n in the R-vector space NR = N ⊗Z R determines an
affine subspace Aσ with underlying vector space Lσ and a lattice Nσ = Lσ ∩ N
in Lσ (see Appendix A.2). A smooth function f : σ → R on a polyhedron σ in
NR is the restriction of a smooth function on some open neighbourhood of σ in
Aσ . For further notation borrowed from convex geometry, we refer to Appendix
A.
Definition 1.1. (i) A polyhedral complex C of pure dimension n is called
weighted (with smooth weights) if each polyhedron σ ∈ Cn is endowed with a
smooth weight function mσ : σ → R. If all mσ are constant functions, then
we call them constant weights. The support |(C , m)| of a weighted polyhedral
complex (C , m) of pure dimension n is the closed set
                                      [
                          |(C , m)| =    supp (mσ ).

# PRIMARY pertinent exact literal body

     d0 d00 [− log ks|W ∩U an k] = d0 d00 [− log ksU |W ∩U an k] + d0 d00 [− log |f |W ∩U an |].
Using the definition of c1 (L|W ∩U an , k.k) for the first summand and using Theo-
rem 7.2 for the second summand, we get the claim.                               

       8. Piecewise smooth and formal metrics on line bundles
  In this section, X is an algebraic variety over K. In the following, we consider
an open subset W of X an .
  We first introduce piecewise smooth functions and piecewise linear functions
on W . This leads to corresponding notions for metrics on line bundles. We
prove that a piecewise linear metric is the same as a formal metric. We show
that canonical metrics in various situations are piecewise smooth.
   In Definition 1.6, we have defined piecewise smooth functions on an open
subset of an integral R-affine polyhedral set. Using tropicalizations and viewing
tropical varieties as polyhedral sets, we will define piecewise smooth functions
on W as follows:
Definition 8.1. A function f : W → R is called piecewise smooth if for every
x ∈ W there is a tropical chart (V, ϕU ) such that V is an open neighbourhood
of x in W and such that there is a piecewise smooth function φ on tropU (V )
with f = φ ◦ tropU on V .
   In a similar way, we will define a piecewise linear function on W . We recall
from Definition 1.6 that we have defined piecewise linear functions on integral
R-affine polyhedral complexes. As we are working with a variety over a valued
field, we will take the value group Γ into account and we will require in the def-
inition of piecewise linear functions additionally that the underlying polyhedral
complex and the restriction of the functions are both integral Γ-affine. Note
however that in Definition 8.1, the underlying polyhedral complex for φ is only
assumed to be integral R-affine.
Definition 8.2. A function f : W → R is called piecewise linear if for every
x ∈ W there is a tropical chart (V, ϕU ) such that V is an open neighbourhood
of x in W and a real function φ on tropU (V ) with f = φ ◦ tropU on V . We
require that there is an integral Γ-affine polyhedral complex Σ in NU,R with
tropU (V ) ⊆ |Σ| such that φ is the restriction of a function on |Σ| with integral
Γ-affine restrictions to all faces of Σ.
8.3. The space of piecewise smooth functions on W is an R-subalgebra of the
R-algebra of continuous functions on W . It contains all smooth functions on
W . The space of piecewise linear functions on W is closed under forming max
     A TROPICAL APPROACH TO NON-ARCHIMEDEAN ARAKELOV GEOMETRY                     65

and min. Moreover, it is a subgroup of the space of piecewise smooth functions
on W with respect to addition. If ϕ : X 0 → X is a morphism and W 0 is an
open subset of (ϕan )−1 (W ), then for every piecewise smooth (resp. piecewise
linear) function f on W , the restriction of f ◦ ϕ to W 0 is a piecewise smooth
(resp. piecewise linear) function on W 0 .
   In the following result, we need the G-topology on W . It is a Grothendieck
topology build up from analytic subdomains of W and it is closely related to
the Grothendieck topology of the underlying rigid analytic space ([Ber93, §1.3,
§1.6]).
Proposition 8.4. Let f : W → R be a continuous function. Then f is piecewise
smooth (resp. piecewise linear) if and only if there is a G-covering (Wi )i∈I
by analytic (resp. strict analytic) subdomains Wi of W and analytic moment
maps ϕi : Wi → (Ti )an to tori Ti := Spec(K[Mi ]) such that f = φi ◦ ϕi,trop
on Wi for a smooth (resp. integral Γ-affine) function φi : Ni,R → R, where
Ni := Hom(Mi , Z) as usual.
Proof. First, we assume that f is piecewise smooth (resp. piecewise linear).
For any x ∈ W , there is a tropical chart (V, ϕU ) in W containing x such that
f = φ ◦ tropU on V for a piecewise smooth (resp. integral Γ-affine function) φ
on the open subset Ω := tropU (V ) of Trop(U ). There are finitely many integral
R-affine
S         (resp. Γ-affine) polytopes ∆i in NU,R containing tropU (x) such that
   ∆
  i i  is a neighbourhood of tropU (x) in Ω and such that φ|∆i = φi |∆i for a
smooth (resp. integral Γ-affine) function φi : NU,R → R. Note that the affinoid
(resp. strictly affinoid) subdomains Wi (x) := trop−1  U (∆i ) of W contain x and
cover a neighbourhood of x. Letting x vary over W , we get a G-covering of W
with the desired properties.
   To prove the converse, we assume that f is given on a G-covering (Wi )i∈I of
W by smooth (resp. integral Γ-affine) functions φi : Ni,R → R with respect to
analytic moment maps ϕi : Wi → (Ti )an . Piecewise smoothness (resp. piecewise
linearity) is a local condition and so we have to check that f is piecewise smooth
in a neighbourhood of x ∈ X an . There is a finite I0 ⊆ I such that the sets
(Wi )i∈I0 cover a sufficiently small strict affinoid neighbourhood W 0 of x in W .
By shrinking W , we may assume that x ∈ Wi for every i ∈ I0 . In the following,
we restrict our attention to elements i ∈ I0 . The definition of an analytic (resp.
of a strict analytic) domain shows that we may assume that all Wi0 := Wi ∩ W 0
are affinoid (resp. strict affinoid) subdomains of W . Any analytic function on
a neighbourhood of x in Wi0 can be approximated uniformly on a sufficiently
small neighbourhood of x by rational functions on X. By shrinking W again,
this shows that we may assume that ϕi |Wi0 is induced by the restriction of an
algebraic moment map ϕ0i : Ui → Ti for a dense open subset Ui of X with
Wi0 ⊆ (Ui )an (see [Gub16, Prop. 7.2] for a similar argument). Similarly, we
may assume that there are affinoid coordinates (xij )j∈Ji on Wi0 which extend
to rational functions on X. Clearly, we may assume that |xij (x)| = 1 for
i ∈ IT0 and j ∈ Ji . There is a tropical chart (V, ϕU ) with x ∈ V ⊆ W 0 ,
U ⊆ i∈I0 Ui and such that all the functions xij are in O(U )× . We may assume
that tropU (x) = 0 and hence there is an open neighbourhood Ω    e of 0 in NU,R with
66                  WALTER GUBLER AND KLAUS KÜNNEMANN


V = trop−1    e                                         0
           U (Ω). By [Gub16, 4.12, Proposition 4.16], ϕi |U is the composition
of an affine homomorphism ψi : TU → Ti with ϕU . By shrinking V and using
the Bieri–Groves theorem [Gub13, Thm. 3.3], we may assume that there are
finitely many rational cones (∆j )j∈J in NU,R such that
                                             [
(8.4.1)                                  e∩
                            tropU (V ) = Ω      ∆j .
                                               j∈J

For every i ∈ I0 and every j ∈ Ji , there is a linear form uij ∈ MU with
− log |xij | = uij ◦ tropU on U an . The definition of affinoid coordinates yields
(8.4.2)                      Wi0 ∩ U an = trop−1
                                              U (σi )
for σi := {ω ∈ NU,R | uij (ω) ≥ rij ∀j ∈ Ji } and suitable rij ∈ R. Note that σi
is an integral R-affine polyhedron. In the piecewise linear case, we may choose
always rij = 0 and hence σi is a rational cone. Using that the sets Wi0 ∩U an cover
V and equations (8.4.1), (8.4.2), we get the decomposition (σi ∩ ∆j ∩ Ω) e i∈I ,j∈J
                                                                               0
                              e
of tropU (V ). On σi ∩ ∆j ∩ Ω, we choose the smooth (resp. integral Γ-affine)
function φ0ij := φi ◦ ψi . Using (8.4.2), we see that these functions paste to a
continuous piecewise smooth (resp. continuous piecewise linear) function φ0 on
tropU (V ) with φ0 ◦ tropU = f on V . This proves easily that f is piecewise
smooth (resp. piecewise linear) on W .                                            
Definition 8.5. Let L be a line bundle on X and let W be an open subset of
X an . A metric k k on L|W is called piecewise smooth (resp. piecewise linear)
if for every x ∈ W , there is a tropical chart (V, ϕU ) with x ∈ V ⊆ W and a
nowhere vanishing section s ∈ Γ(U, L) such that − log ks|V k is piecewise smooth
(resp. piecewise linear) on V .
8.6. Since − log |f | is smooth for an invertible regular function f and even
the pull-back of a linear function with respect to a suitable tropicalization, the
last definition does neither depend on the choice of the trivialization s nor on
the choice of the tropical chart (V, ϕU ). Moreover, we may also use analytic
trivializations in the definition. By Proposition 8.4, the definition of a piecewise
linear metric agrees with the definition of PL-metrics in [CLD12, §6.2].
   Note that every piecewise linear metric is piecewise smooth. It follows from
8.3 that every piecewise smooth metric is continuous, that the tensor product
of piecewise linear (resp. piecewise smooth) metrics is again a piecewise linear
(resp. piecewise smooth) metric and that the dual metric of a a piecewise linear
(resp. piecewise smooth) metric is piecewise linear (resp. piecewise smooth).
Moreover, the pull-back of a piecewise linear (resp. piecewise smooth) metric
on L|W with respect to a morphism ϕ : X 0 → X is a piecewise linear (resp.
piecewise smooth) metric on ϕ∗ (L)|W 0 for any open subset W 0 of ϕ−1 (W ).
8.7. Recall that K ◦ is the valuation ring of the given non-archimedean absolute
value | | on K. Raynaud introduced an admissible formal scheme over K ◦ as
a formal scheme X over the valuation ring K ◦ which is locally isomorphic to
Spf(A) for a flat K ◦ -algebra A of topologically finite type over K ◦ (see [BL93,
§1] for details). For simplicity, we require additionally that X has a locally
finite atlas of admissible affine formal schemes over K ◦ . Then X has a generic
     A TROPICAL APPROACH TO NON-ARCHIMEDEAN ARAKELOV GEOMETRY                      67

fibre Xη (resp. a special fibre Xs ) which is a paracompact strictly analytic
Berkovich space over K (resp. an algebraic scheme over the residue field K̃)
locally isomorphic to M (A ) (resp. Spec(A ⊗K ◦ K̃)) for the strict affinoid
algebra A := A ⊗K ◦ K (see [Ber93, §1.6] for the equivalence to rigid analytic
spaces over K with an affinoid covering of finite type).
   A formal K ◦ -model of X is an admissible formal scheme X over K ◦ with
an isomorphism Xη ∼  = X an . For a line bundle L on X, we define a formal
K ◦ -model of L as a line bundle L on a formal K ◦ -model X of X with an
isomorphism Lη ∼ = Lan over Xη ∼= X an . For simplicity, we usually identify Lη
       an
with L .
8.8. Let L be a line bundle on X. A formal metric on L is a metric k kL
associated to a formal K ◦ -model L of L in the following way: If L admits
a formal trivialization over U and if s ∈ Γ(U , L ) corresponds under this
trivialization to the function γ ∈ OX (U ), then ks(x)k = |γ(x)| for all x ∈ Uη .
This definition is independent of the choice of the trivialization and shows
immediately that formal metrics are continuous. The tensor product and the
pull-back of formal metrics are again formal metrics.
Proposition 8.9. Every line bundle L on X has a formal K ◦ -model and hence
a formal metric.
Proof. This follows as in [Gub98, Prop. 7.6] based on the theorem of Raynaud
that every paracompact analytic space has a formal K ◦ -model (see [Bos14,
Theorem 8.4.3]). The argument for paracompact strictly K-analytic spaces
was first given in [CLD12, Proposition 6.2.13].                            
Proposition 8.10. Let k k be a formal metric on the line bundle L on X. Then
there is an admissible formal K ◦ -model X of X with reduced special fibre Xs
and a K ◦ -model L of L on X such that k k = k kL . Moreover, the invertible
sheaf associated to L is always canonically isomorphic to the sheaf on X given
by {s ∈ Γ(L, Uη ) | ||s(s)|| ≤ 1 ∀x ∈ Uη } on a formal open subset U of X .
Proof. This follows as in [Gub98, Lemma 7.4 and Proposition 7.5].                  
Proposition 8.11. Let k k be a metric on the line bundle L on X. Then the
following properties are equivalent:
    (a) k k is a formal metric;
    (b) k k is a piecewise linear metric;
    (c) there is a G-covering (Wi )i∈I of X an by strict analytic subdomains Wi of
        X an and trivializations si ∈ Γ(Wi , Lan ) with ksi (x)k = 1 for all x ∈ Wi
        and all i ∈ I.
Proof. If we use again Raynaud’s theorem to generalize to paracompact X an ,
the equivalence of (a) and (c) is proved as in [Gub98, Lemma 7.4 and Propo-
sition 7.5]. The implication (a) ⇒ (c) can also be found in [CLD12, Exemple
6.2.10]. It remains to see the equivalence of (b) and (c). Suppose that (b) holds.
Then there is a locally finite covering of X by trivializations Ui of L such that
− log ksi k is piecewise linear on (Ui )an for every i ∈ I. By Proposition 8.4, there
is a G-covering Wij of (Ui )an and analytic moment maps ϕij : Wij → (Tij )an
68                  WALTER GUBLER AND KLAUS KÜNNEMANN

such that − log ksi k = φij ◦ ϕij,trop on Wij for an integral Γ-affine function φij
on Nij,R . The definition of integral Γ-affine functions shows that there is an
invertible analytic function γij on Wij such that ksi k = |γij | on Wij . Using the
                −1
trivialization γij si on Wij , we get (b) ⇒ (c). The converse is an immediate
application of Proposition 8.4.                                                  
8.12. If X is proper over K, than an algebraic K ◦ -model of X is an integral
scheme X which is of finite type, flat and proper over K ◦ and with a fixed
isomorphism between the generic fibre Xη and X. We use the isomorphism
to identify Xη and X. An algebraic K ◦ -model of L is a line bundle L on an
algebraic K ◦ -model X of X together with a fixed isomorphism between Lη and
L. We define an algebraic metric on L as in 8.8 by using an algebraic K ◦ -model
L of L.
Proposition 8.13. On a line bundle on a proper variety over K, a metric is
algebraic if and only if it is formal.
Proof. Passing to the formal completion along the special fibre, it is clear that
every algebraic metric is a formal metric. Using [Gub03, Proposition 10.5], the
converse is true if X is projective. The same argument shows that the converse
is also true for proper X if the formal GAGA theorem in [Gro61, Theorem 5.1.4]
holds over K ◦ and if X has an algebraic K ◦ -model. In [Gro61, Theorem 5.1.4],
the base has to be noetherian and hence it applies only for discrete valuation
rings. The required generalization is now given in [FK13, Theorem I.10.1.2].
The existence of an algebraic K ◦ -model follows from Nagata’s compactification
theorem. This was proved by Nagata in the noetherian case and proved by
Conrad in general (based on notes of Deligne, see Temkin’s paper [Tem11] for
another proof and references).                                                 
Corollary 8.14. Let L be a line bundle on a proper variety over K. Then L
has an algebraic metric.
Proof. This follows from Proposition 8.9 and Proposition 8.13.                    
     We will show now that many important metrics are piecewise smooth.

# PRIMARY live Stacks resolution-fiber proofs and fixed GK edition observation

{
  "content": [
    {
      "type": "text",
      "text": "[1406.7637] A tropical approach to non-archimedean Arakelov theory (https://arxiv.org/abs/1406.7637)\n【turn514928view0】 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({\"ref_id\":\"https://arxiv.org/abs/1406.7637\",\"lineno\":null}); Total lines: 165\nL0: 【0†Search】 【1†Submit】 【2†Donate†info.arxiv.org】 【3†Log in】\nL1: \nL2: Search arXiv [Input: Search papers by title, author, abstract, or ID...] [Input] [Input]\nL3: \nL4: Press Enter to search · 【4†Advanced search】\nL5: \nL6: # Mathematics > Algebraic Geometry\nL7: \nL8: [Submitted on 30 Jun 2014 (【5†v1】), last revised 13 Sep 2016 (this version, v3)]\nL9: # Title:A tropical approach to non-archimedean Arakelov theory\nL10: \nL11: Authors:【6†Walter Gubler】, 【7†Klaus Kuennemann】\nL12: \nL13: View a PDF of the paper titled A tropical approach to non-archimedean Arakelov theory, by Walter Gubler and Klaus Kuennemann\nL14: \nL15: 【8†View PDF】 【9†HTML (experimental)】\nL16: > Abstract:Chambert-Loir and Ducros have recently introduced a theory of real valued differential forms and currents on Berkovich spaces. In analogy to the theory of forms with logarithmic singularities, we enlarge the space of differential forms by so called delta-forms on the non-archimedean analytification of an algebraic variety. This extension is based on an intersection theory for tropical cycles with smooth weights.\nL17: We prove a generalization of the Poincaré-Lelong formula which allows us to represent the first Chern current of a formally metrized line bundle by a delta-form. We introduce the associated Monge-Ampère measure $\\mu$ as a wedge-power of this first Chern delta-form and we show that $\\mu$ is equal to the corresponding Chambert-Loir measure. The star-product of Green currents is a crucial ingredient in the construction of the arithmetic intersection product.\nL18: Using the formalism of delta-forms, we obtain a non-archimedean analogue at least in the case of divisors. We use it to compute non-archimedean local heights of proper varieties.\nL19: Comments:  | 91 pages, revised and updated version, new example 4.22\nL20: Subjects:  | Algebraic Geometry (math.AG)\nL21: MSC (Mathematical Subject Classification) classes:  | Primary 14G40, Secondary 14G22, 14T05, 32P05\nL22: Cite as:  | 【10†arXiv:1406.7637】 [math.AG]\nL23:    | (or 【11†arXiv:1406.7637v3】 [math.AG] for this version)\nL24:    | 【12†https://doi.org/10.48550/arXiv.1406.7637†doi.org】 arXiv-issued DOI via DataCite\nL25: Journal reference:  | Alg. Number Th. 11 (2017) 77-180\nL26: Related DOI (Digital Object Identifier):  | 【13†https://doi.org/10.2140/ant.2017.11.77†doi.org】 DOI(s) linking to related resources\nL27: ## Submission history\nL28: \nL29: From: Klaus Kuennemann [【14†view email】]\nL30: 【5†[v1]】 Mon, 30 Jun 2014 09:03:47 UTC (81 KB)\nL31: 【15†[v2]】 Wed, 30 Sep 2015 09:00:44 UTC (84 KB)\nL32: [v3] Tue, 13 Sep 2016 14:06:12 UTC (169 KB)\nL33: \nL34: Full-text links:\nL35: \nL36: ## Access Paper:\nL37: \nL38: View a PDF of the paper titled A tropical approach to non-archimedean Arakelov theory, by Walter Gubler and Klaus Kuennemann\nL39: \nL40:   * 【8†View PDF】\nL41:   * 【9†HTML (experimental)】\nL42:   * 【16†TeX Source】\nL43: \nL44: 【17†view license】\nL45: ### Current browse context:\nL46: \nL47: math.AG\nL48: \nL49: 【18†< prev】   |   【19†next >】\nL50: \nL51: 【20†new】 | 【21†recent】 | 【22†2014-06】\nL52: \nL53: Change to browse by:\nL54: \nL55: 【23†math】\nL56: \nL57: ### References & Citations\nL58: \nL59:   * 【24†NASA ADS†ui.adsabs.harvard.edu】\nL60:   * 【25†Google Scholar†scholar.google.com】\nL61:   * 【26†Semantic Scholar†api.semanticscholar.org】\nL62: \nL63: [Button: export BibTeX citation] Loading...\nL64: \nL65: ## BibTeX formatted citation\nL66: \nL67: [Button: ×]\nL68: \nL69: loading...\nL70: \nL71: Data provided by:\nL72: \nL73: ### Bookmark\nL74: \nL75: [Input] Bibliographic Tools\nL76: # Bibliographic and Citation Tools\nL77: \nL78: [Input] Bibliographic Explorer Toggle\nL79: \nL80: Bibliographic Explorer (【27†What is the Explorer?†info.arxiv.org】)\nL81: \nL82: [Input] Connected Papers Toggle\nL83: \nL84: Connected Papers (【28†What is Connected Papers?†www.connectedpapers.com】)\nL85: \nL86: [Input] Litmaps Toggle\nL87: \nL88: Litmaps (【29†What is Litmaps?†www.litmaps.co】)\nL89: \nL90: [Input] scite.ai Toggle\nL91: \nL92: scite Smart Citations (【30†What are Smart Citations?†www.scite.ai】)\nL93: \nL94: [Input] Code, Data, Media\nL95: # Code, Data and Media Associated with this Article\nL96: \nL97: [Input] alphaXiv Toggle\nL98: \nL99: alphaXiv (【31†What is alphaXiv?†alphaxiv.org】)\nL100: \nL101: [Input] Links to Code Toggle\nL102: \nL103: CatalyzeX Code Finder for Papers (【32†What is CatalyzeX?†www.catalyzex.com】)\nL104: \nL105: [Input] DagsHub Toggle\nL106: \nL107: DagsHub (【33†What is DagsHub?†dagshub.com】)\nL108: \nL109: [Input] GotitPub Toggle\nL110: \nL111: Gotit.pub (【34†What is GotitPub?†gotit.pub】)\nL112: \nL113: [Input] Huggingface Toggle\nL114: \nL115: Hugging Face (【35†What is Huggingface?†huggingface.co】)\nL116: \nL117: [Input] ScienceCast Toggle\nL118: ScienceCast (【36†What is ScienceCast?†sciencecast.org】)\nL119: \nL120: [Input] Demos\nL121: # Demos\nL122: \nL123: [Input] Replicate Toggle\nL124: \nL125: Replicate (【37†What is Replicate?†replicate.com】)\nL126: \nL127: [Input] Spaces Toggle\nL128: \nL129: Hugging Face Spaces (【38†What is Spaces?†huggingface.co】)\nL130: \nL131: [Input] Spaces Toggle\nL132: \nL133: TXYZ.AI (【39†What is TXYZ.AI?†txyz.ai】)\nL134: \nL135: [Input] Related Papers\nL136: # Recommenders and Search Tools\nL137: \nL138: [Input] Link to Influence Flower\nL139: \nL140: Influence Flower (【40†What are Influence Flowers?†influencemap.cmlab.dev】)\nL141: \nL142: [Input] Core recommender toggle\nL143: \nL144: CORE Recommender (【41†What is CORE?†core.ac.uk】)\nL145: \nL146:   * Author\nL147:   * Venue\nL148:   * Institution\nL149:   * Topic\nL150: \nL151: [Input] About arXivLabs\nL152: # arXivLabs: experimental projects with community collaborators\nL153: \nL154: arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.\nL155: \nL156: Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.\nL157: Have an idea for a project that will add value for arXiv's community? 【42†Learn more about arXivLabs†info.arxiv.org】.\nL158: \nL159: 【43†Which authors of this paper are endorsers?】 | Disable MathJax (【44†What is MathJax?†info.arxiv.org】)\nL160: \nL161: We gratefully acknowledge support from our major funders, 【45†member institutions†info.arxiv.org】, , and all contributors.\nL162: 【46†About†info.arxiv.org】 · 【47†Help†info.arxiv.org】 · 【48†Contact†info.arxiv.org】 · 【49†Subscribe†info.arxiv.org】 · 【50†Copyright†info.arxiv.org】 · 【51†Privacy†info.arxiv.org】 · 【52†Accessibility†info.arxiv.org】 · 【53†Operational Status (opens in new tab)†status.arxiv.org】\nL163: \nL164: Major funding support from\n\n--------------------------------------------------------------------------------\nLemma 37.53.6 (0AY8)—The Stacks project (https://stacks.math.columbia.edu/tag/0AY8)\n【turn514928view1】 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/0AY8\",\"lineno\":null}); Total lines: 79\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†37】: More on Morphisms\nL10:   * Section 【7†37.53】: Stein factorization\nL11:   * Lemma 【8†37.53.6】 (【9†cite】)\nL12: \nL13: [Input]\nL14: \nL15:   * 【10†previous theorem】\nL16:   * 【11†next lemma】\nL17: \nL18: * * *\nL19: \nL20:   * 【12†history】\nL21:   * 【13†statistics】\nL22:   * 【14†3 tags refer to this tag】\nL23: \nL24: 【8†Lemma 37.53.6.】 Let $f : X \\to S$ be a morphism of schemes. Assume\nL25:   1. $f$ is proper,\nL26: \nL27:   2. $S$ is integral with generic point $\\xi $,\nL28: \nL29:   3. $S$ is normal,\nL30: \nL31:   4. $X$ is reduced,\nL32: \nL33:   5. every generic point of an irreducible component of $X$ maps to $\\xi $,\nL34: \nL35:   6. we have $H^0(X_\\xi , \\mathcal{O}) = \\kappa (\\xi )$.\nL36: \nL37: Then $f_*\\mathcal{O}_ X = \\mathcal{O}_ S$ and $f$ has geometrically connected fibres.\nL38: Proof. Apply Theorem 【10†37.53.5】 to get a factorization $X \\to S' \\to S$. It is enough to show that $S' = S$. This will follow from Morphisms, Lemma 【15†29.55.8】. Namely, $S'$ is reduced because $X$ is reduced (Morphisms, Lemma 【16†29.54.8】). The morphism $S' \\to S$ is integral by the theorem cited above. Every generic point of $S'$ lies over $\\xi $ by Morphisms, Lemma 【17†29.54.9】 and assumption (5).\nL39: On the other hand, since $S'$ is the relative spectrum of $f_*\\mathcal{O}_ X$ we see that the scheme theoretic fibre $S'_\\xi $ is the spectrum of $H^0(X_\\xi , \\mathcal{O})$ which is equal to $\\kappa (\\xi )$ by assumption. Hence $S'$ is an integral scheme with function field equal to the function field of $S$. This finishes the proof. $\\square$\nL40: * * *\nL41: ## Comments (0)\nL42: \nL43: There are also:\nL44: \nL45:   * 5 comment(s) on Section 【18†37.53】: Stein factorization\nL46: \nL47: * * *\nL48: ## Post a comment\nL49: \nL50: Your email address will not be published. Required fields are marked.\nL51: \nL52: In your comment you can use 【19†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL53: \nL54: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL55: \nL56: All contributions are licensed under the 【20†GNU Free Documentation License†github.com】.\nL57: Name^{*}: [Input]\nL58: E-mail^{*}: [Input]\nL59: Site: [Input]\nL60: Comment:\nL61: \nL62: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 0AY8. Beware of the difference between the letter 'O' and the digit '0'.\nL63: \nL64: Tag: [Input] [Button: Post comment] [Input]\nL65: \nL66: The tag you filled in for the captcha is wrong. You need to write 0AY8, in case you are confused.\nL67:   * 【10†previous theorem】\nL68:   * 【11†next lemma】\nL69: \nL70: * * *\nL71: \nL72: 【21†View Lemma 37.53.6 as pdf】\nL73: \nL74: * * *\nL75: \nL76:   * 【12†history】\nL77:   * 【13†statistics】\nL78:   * 【14†3 tags refer to this tag】\n\n--------------------------------------------------------------------------------\nLemma 29.55.12 (0GIQ)—The Stacks project (https://stacks.math.columbia.edu/tag/0GIQ)\n【turn514928view2】 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({\"ref_id\":\"https://stacks.math.columbia.edu/tag/0GIQ\",\"lineno\":null}); Total lines: 63\nL0: # 【0†The Stacks project】\nL1: \nL2:   * 【1†bibliography】\nL3:   * 【2†blog†www.math.columbia.edu】\nL4: \nL5: 【3†Image】 [Input: keywords or a tag]\nL6: \nL7:   * 【4†Table of contents】\nL8:   * Part 【5†2】: Schemes\nL9:   * Chapter 【6†29】: Morphisms of Schemes\nL10:   * Section 【7†29.55】: Normalization\nL11:   * Lemma 【8†29.55.12】 (【9†cite】)\nL12: \nL13: [Input]\nL14: \nL15:   * 【10†previous lemma】\nL16: \nL17: * * *\nL18: \nL19:   * 【11†history】\nL20:   * 【12†statistics】\nL21:   * 【13†1 tag refers to this tag】\nL22: 【8†Lemma 29.55.12.】 Let $X$ be an irreducible, geometrically unibranch scheme. The normalization morphism $\\nu : X^\\nu \\to X$ is a universal homeomorphism.\nL23: Proof. We have to show that $\\nu $ is integral, universally injective, and surjective, see Lemma 【14†29.46.5】. By Lemma 【15†29.55.5】 the morphism $\\nu $ is integral. Let $x \\in X$ and set $A = \\mathcal{O}_{X, x}$. Since $X$ is irreducible we see that $A$ has a single minimal prime $\\mathfrak p$ and $A_{red} = A/\\mathfrak p$. By Lemma 【16†29.55.4】 the stalk $A' = (\\nu _*\\mathcal{O}_{X^\\nu })_ x$ is the integral closure of $A$ in the fraction field of $A_{red}$.\nL24: By More on Algebra, Definition 【17†15.108.1】 we see that $A'$ has a single prime $\\mathfrak m'$ lying over $\\mathfrak m_ x \\subset A$ and $\\kappa (\\mathfrak m')/\\kappa (x)$ is purely inseparable. Hence $\\nu $ is bijective (hence surjective) and universally injective by Lemma 【18†29.10.2】. $\\square$\nL25: * * *\nL26: ## Comments (0)\nL27: \nL28: There are also:\nL29: \nL30:   * 2 comment(s) on Section 【19†29.55】: Normalization\nL31: \nL32: * * *\nL33: ## Post a comment\nL34: \nL35: Your email address will not be published. Required fields are marked.\nL36: \nL37: In your comment you can use 【20†Markdown】 and LaTeX style mathematics (enclose it like `$\\pi$`). A preview option is available if you wish to see how it works out (just click on the eye in the toolbar).\nL38: \nL39: Unfortunately JavaScript is disabled in your browser, so the comment preview function will not work.\nL40: \nL41: All contributions are licensed under the 【21†GNU Free Documentation License†github.com】.\nL42: Name^{*}: [Input]\nL43: E-mail^{*}: [Input]\nL44: Site: [Input]\nL45: Comment:\nL46: \nL47: In order to prevent bots from posting comments, we would like you to prove that you are human. You can do this by filling in the name of the current tag in the following input field. As a reminder, this is tag 0GIQ. Beware of the difference between the letter 'O' and the digit '0'.\nL48: \nL49: Tag: [Input] [Button: Post comment] [Input]\nL50: \nL51: The tag you filled in for the captcha is wrong. You need to write 0GIQ, in case you are confused.\nL52:   * 【10†previous lemma】\nL53: \nL54: * * *\nL55: \nL56: 【22†View Lemma 29.55.12 as pdf】\nL57: \nL58: * * *\nL59: \nL60:   * 【11†history】\nL61:   * 【12†statistics】\nL62:   * 【13†1 tag refers to this tag】\n"
    }
  ],
  "isError": false
}


# PRIMARY fixed-ample-bundle approximation and continuous operator bodies

a test configuration X 00 dominating X and X 0 via µ : X 00 → X , µ0 : X 00 → X 0 , such that
L00 := µ? L = µ0? L0 . Since X and X 0 are integrally closed, Lemma 1.12 yields µ? OX 00 = OX ,
µ0? OX 00 = OX 0 , and the projection formula shows that
                           H0 (X , mL) = H0 X 00 , mL00 = H0 (X 0 , mL0 ).
                                                          

The proof is complete.                                                                             
2.7. Fubini–Study functions and test configurations. Let L be a Q-line bundle on X.
For any test configuration (X , L) for (X, L), we can choose a test configuration X 0 with two
morphisms µ : X 0 → X , ρ : X 0 → Xtriv . Then
                                D := µ? L − ρ? Ltriv ∈ VCar(X )Q ,
and mapping L to D yields a 1–1 correspondence between the set of equivalence classes
of test configurations for (X, L) and the Q-vector space limX VCar(X )Q , which in turn is
                                                         −→
isomorphic to PL(X), by Theorem 2.7. We write ϕL for the element of PL(X) associated to
30                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

L. The restriction of ϕL to X div coincides with the function associated to the equivalence
class of (X , L) in [BHJ17, §6].
Theorem 2.31. For any Q-line bundle L on X, the map L 7→ ϕL sets up a 1–1 correspon-
dence between:
    (i) the set of equivalence classes of test configurations for L and PL(X);
   (ii) the set of equivalence classes of semiample test configurations for L and H(L).
   Note that the sets in (ii) are nonempty only if L is semiample. Combined with Proposi-
tion 2.30, we infer:
Corollary 2.32. If L is an ample Q-line bundle, then L 7→ ϕL defines a 1–1 correspondence
between the set of ample, integrally closed test configurations for L and H(L).
     The set H(L) thus corresponds to HNA (L) in the notation of [BHJ17, Definition 6.2].
Proof of Theorem 2.31. By construction, the map L 7→ ϕL is the composition of D 7→ ϕD
with the canonical bijection between equivalence classes of test configurations for L and
limX VCar(X )Q . Thus (i) is a direct consequence of Theorem 2.7.
−→
   To prove (ii), let (X , L) be a semiample test configuration for (X, L). After replacing L
with a multiple and pulling-back to a higher test configuration, we may assume without loss
that L is a globally generated line bundle, and that X dominates the trivial test configuration
via µ : X → Xtriv . Set D := L − µ? Ltriv ∈ VCar(X ), so that ϕL = ϕD . Since L is globally
generated, OX (D) is µ-globally generated, and the flag ideal a := µ? OX (D) thus satisfies
a·OX = OX (D), and hence ϕa = ϕD = ϕL . Denote by a0 ⊂ a the flag ideal locally generated
by
                                H0 (Xtriv , Ltriv ⊗ a) ≃ H0 (X , L).
Since L is globally generated, we have a0 · OX = OX (D) = a · OX ; hence ϕa0 = ϕL . By
construction, L ⊗ a0 is globally generated, and Proposition 2.25 thus yields, as desired,
ϕL ∈ H(L).
   Conversely pick ϕ ∈ H(L). After replacing L with a multiple, Proposition 2.25 yields
ϕ = ϕa for a flag ideal a on Xtriv such that Ltriv ⊗ a is globally generated. Denoting by
µ : X → Xtriv the blowup along a, we have a · OX = OX (D) for a vertical Cartier divisor D
such that L := µ? Ltriv + D is globally generated, and ϕL = ϕD = ϕa = ϕ.                      
     The next result will be needed in §3.1.
Lemma 2.33. If L is an ample Q-line bundle on X and X any test configuration for X
that dominates Xtriv , then L admits an ample test configuration L determined on X .
Proof. By Lemma 1.8, we can find D ∈ VCar(X )Q that is relatively ample over Xtriv .
Denoting by LX the pullback of L to X , it follows that L := LX + εD is ample for ε ∈ Q>0
small enough, and we are done.                                                         
2.8. Geometric interpretation of the scaling action. As noted in §2.1, the spaces
PL(X) and PL+ (X) admit a natural scaling action by Q>0 . We now give a geometric
interpretation of the scaling action of Z>0 in terms of base change.
   Using flag ideals, this is easy: any function ϕ ∈ PL+ (X) can be written ϕ = m−1 ϕa for
some m ∈ Z>0 and some flag ideal a on Xtriv = X × A1 . It then follows from the discussion
after (2.5) that if d ∈ Z>0 , then d · ϕ = m−1 ϕa(d) , where a(d) is the pullback of a under the
map Xtriv → Xtriv given by $ 7→ $d .
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                           31

  Following [BHJ17, §6.3], we can give a smilar interpretation of the scaling action when
the functions are associated to test configurations.
  Let L be a Q-line bundle on X. For any test configuration (X , L) for (X, L) and d ∈ Z>0 ,

# PRIMARY fixed-ample-bundle approximation and continuous operator bodies

curve C ⊂ X0 , which we accomplish by way of a standard degeneration argument: denote
34                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

by Ct the image of C under t ∈ Gm , and note that α · C = α · Ct , by Gm -invariance of α.
By properness of the components of the Chow scheme of X0 , C0 := limt→0 Ct exists as an
effective 1-cycle. It is Gm -invariant, and hence a positive linear combination of Gm -invariant
irreducible curves. Thus
                                 α · C = lim α · Ct = α · C0 ≥ 0,
                                         t→0
and we are done.                                                                              
   If a test configuration X dominates Xtriv = X × A1 , then each class θ ∈ N1 (X) pulls back
to a class θX ∈ N1 (X /A1 ) via the composition
                                   X → Xtriv = X × A1 → X.
In line with [Zha95, Gub98, CL06, BFJ16], we introduce:
Definition 3.2. We say that a function ϕ ∈ PLR is θ-plurisubharmonic ( θ-psh for short)
if it is determined by a divisor D ∈ VCar(X )R on a test configuration X dominating Xtriv
such that θX + D ∈ Nef(X /A1 ).
   We sometimes also say that the pair (θ, ϕ) ∈ N1 (X) × PLR is psh. Here θX + D denotes,
slightly abusively, the sum of θX and of the image of D in N1 (X /A1 ).
   This definition is independent of the choice of X . Indeed, for any morphism of test
configurations µ : X 0 → X , we have
                                   θX 0 + µ? D = µ? (θX + D) ,
which is thus nef iff θX +D is nef. Restricting to X1 ≃ X further shows that a θ-psh function
in PLR can only exist when θ ∈ Nef(X).
   We will use the notation
                              PLR ∩ PSH(θ)     and    PL ∩ PSH(θ)
for the sets of θ-psh functions in PLR and PL, respectively. At this point, the notation is
purely formal, but it will be justified in §4, by defining the set PSH(θ).
   When θ = c1 (L) ∈ N1 (X) is the numerical class of L ∈ Pic(X)Q on X, we simply speak
of L-psh functions. By Theorem 2.31, we have:
Example 3.3. For any Q-line bundle L on X, L 7→ ϕL sets up a 1–1 correspondence
between the set of semipositive non-Archimedean metrics in the sense of [BHJ17, Defini-
tion 6.4], i.e. equivalence classes of nef test configurations L for L, and PL ∩ PSH(L). By
Theorem 2.31 (ii), we thus have H(L) ⊂ PL ∩ PSH(L), the inclusion being strict in general.
Remark 3.4. Following [BFJ16, BFJ15] we could define a closed (1, 1)-form on X an to be
an element η ∈ limX N1 (X /A1 ), and declare a function ϕ ∈ PLR to be η-psh if it is of the
                −→
form ϕ = ϕD , with D ∈ VCar(X )R such that η + D is nef. In this paper we only consider
the case when η ∈ N1 (Xtriv /A1 ) is determined by the pullback of a class θ ∈ N1 (X).
     As a direct consequence of the fact that Nef(X /A1 ) ⊂ N1 (X /A1 ) is closed, we have:
Lemma 3.5. Let θi → θ be a convergent sequence in N1 (X). Pick ϕ, ψ ∈ PLR , and assume
that ϕ + ci ψ is θi -psh for a sequence ci → 0. Then ϕ is θ-psh.
Proposition 3.6. Pick θ, θ0 ∈ N1 (X), and assume that ϕ, ϕ0 ∈ PLR are θ-psh and θ0 -psh,
respectively. Then:
    (i) ϕ + ϕ0 is (θ + θ0 )-psh, and tϕ is tθ-psh for all t ∈ R>0 ;
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        35

    (ii) for each c ∈ R and t ∈ Q>0 , ϕ + c and t · ϕ are θ-psh;
   (iii) if θ = θ0 and ϕ, ϕ0 ∈ PL, then max{ϕ, ϕ0 } ∈ PL is θ-psh;
   (iv) ϕ is decreasing with respect to the partial order on X an , and hence satisfies (1.4)
         (see Lemma 1.4);
    (v) for any morphism f : Y → X from a projective variety, f ? ϕ is f ? θ-psh;
   (vi) if we further assume that f : Y → X is surjective, then
                   ϕ θ-psh ⇐⇒ ϕ|Xαan θ|Xα -psh for all α ⇐⇒ f ? ϕ f ? θ-psh.
  In particular, (i) shows that PLR ∩ PSH(θ) is a convex subset of PLR .
Lemma 3.7. For any θ ∈ N1 (X) and ϕ ∈ PLR ∩ PSH(θ), there exists a sequence ϕm ∈
H(Lm ) with Lm ∈ Pic(X)Q such that ϕm → ϕ uniformly on X an and c1 (Lm ) → θ.
Proof. Pick a test configuration X dominating Xtriv and D ∈ VCar(X )R such that ϕ = ϕD .
By openness of the (relatively) ample cone of N1 (X /A1 ), we can find a sequence of Q-
line bundles Lm on X and Dm ∈ VCar(X )Q such that c1 (Lm ) → θ in N1 (X), Dm → D
in VCar(X )R , and c1 (Lm )X + Dm ∈ N1 (X /A1 ) is ample for all i. In particular, Lm :=
(Lm )X +Dm is a semiample test configuration for L, and hence ϕm := ϕLm = ϕDm ∈ H(Lm ).
Furthermore, Dm → D implies ϕm → ϕ uniformly.                                          
Proof of Proposition 3.6. Pick a test configuration X dominating Xtriv and D, D0 ∈ VCar(X )R
that determine ϕ, ϕ0 . By assumption, θX + D and θX   0 + D 0 are nef. Thus

       (θ + θ0 )X + D + D0 = (θX + D) + θX   0
                                               + D0
                                                    
                                                        and (tθ)X + tD = t (θX + D)
are nef as well, proving (i).
   For each c ∈ R we have ϕ + c = ϕD+cX0 . Since X0 = π ? (0) vanishes in N1 (X /A1 ),
θX + D + cX0 is nef, and ϕ + c is thus θ-psh. To prove the remaining part of (ii), it suffices to
prove that if d ∈ Z>0 , then ϕ is θ-psh iff d · ϕ is θ-psh. In view of Lemma 2.34, this follows
from the fact that θX + D ∈ N1 (X /A1 ) is nef iff its pullback under the base change of X
with respect to $ 7→ $d is nef.
   Assume now θ = θ0 and D, D0 ∈ VCar(X )Q . By openness of Amp(X), we can find an
Q-line bundle L on X such that c1 (L) − θ is ample and arbitrarily small. Then ϕ, ϕ0 are
L-psh, and it will be enough to show that max{ϕ, ϕ0 } is L-psh as well, by Lemma 3.5. After
perhaps passing to a higher test configuration, we may assume that X supports an ample
test configuration L for L (Lemma 2.33). For each ε ∈ Q>0 , the Q-line bundle LX + D + εL
is ample, and hence semiample. Thus ϕ + εϕL is Fubini–Study for (1 + ε)L, and similarly
for ϕ0 + εϕL . By Proposition 2.19, it follows that
                        max{ϕ + εϕL , ϕ0 + εϕL } = max{ϕ, ϕ0 } + εϕL
is Fubini–Study for (1 + ε)L, and hence (1 + ε)L-psh. Using Lemma 3.5 we conclude, as
desired, that max{ϕ, ϕ0 } is L-psh. This proves (iii).
    By Proposition 2.19, any Fubini–Study function is decreasing, and (iv) thus follows from
Lemma 3.7.
    To prove (v), note that the Gm -equivariant rational map Y × Gm 99K X induced by f
admits a Gm -equivariant resolution of indeterminacies, which is thus a test configuration Y
for Y dominating Ytriv . Also denoting by f : Y → X the corresponding morphism, we have
f ? ϕ = ϕf ? D , and the result thus follows from the fact that θY + f ? D = f ? (θX + D) is nef,
as the pullback of a nef class. If f : Y → X is surjective, then f : Y → X is surjective as
well, and (vi) follows.                                                                        
36                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

   Given a test configuration π : X → A1 , we denote by Amp(X /A1 ) ⊂ Nef(X /A1 ) the set
of π-ample classes α ∈ N1 (X /A1 ), that is, classes whose restriction to X0 is ample.
Definition 3.8. For any ω ∈ Amp(X), we denote by Hdom (ω) ⊂ PL ∩ PSH(ω) the set of ω-
psh PL functions of the form ϕD with D ∈ VCar(X )Q for a test configuration X dominating
Xtriv and ωX + D ∈ Amp(X /A1 ).
   After pulling back by the (finite) integral closure morphism Xe → X , one may always
arrange that X is integrally closed in this definition.
Example 3.9. If ω = c1 (L) for an ample Q-line bundle, then H(L) is in 1–1 correspon-
dence with the set of ample, integrally closed test configurations (X , L) for (X, L) (see Corol-
lary 2.32), and
                              Hdom (L) := Hdom (c1 (L)) ⊂ H(L)
corresponds to the subset such that X dominates Xtriv .
     As in Corollary 2.26, we have
                                     Q+ Hdom (ω) = PL+ (X)                                 (3.2)
for any ω ∈ Amp(X), so that Hdom (ω) spans the Q-vector space PL(X).
Proposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of
functions in Hdom (ω).
Lemma 3.11. For any ω ∈ Amp(X), the set of test configurations X dominating Xtriv such
that there exists H ∈ VCar(X )Q with ωX + H ∈ Amp(X /A1 ) is cofinal in the set of all test
configurations.
Proof. By Lemma 1.8, any test configuration for X is dominated by a test configuration X
with a morphism µ : X → Xtriv such that VCar(X )Q contains a µ-ample divisor A. Since
ωXtriv ∈ N1 (Xtriv /A1 ) is ample, ωX + εA = µ? ωXtriv + εA ∈ N1 (X /A1 ) is ample for ε ∈ Q>0
small enough, and setting H := εA yields the result.                                        
Proof of Proposition 3.10. Pick any ϕ ∈ PLR ∩ PSH(ω), and write ϕ = ϕD for some D ∈
VCar(X )R , where X is an integrally closed test configuration. Thus ωX + D ∈ N1 (X /A1 ) is
nef. By Lemma 3.11 we may assume that there exists P    H ∈ VCar(X )PR such that ωX + H is
ample. Pick a basis (Ci ) for VCar(X )Q and write D = i ci Ci , H = i c0i Ci with ci , c0i ∈ R.
                                  1                                                          1
For m  1, the class ωX + D + m     H ∈ N1 (X /A1 ) is ample, and we can pick εm,i ∈ (0, m     )
                    P          0
                              ci
such that if Dm := i (ci + m + εm,i )Ci , then Dm ∈ VCar(X )Q and ωX + Dm is ample. It
                                                     1
follows that ϕDm ∈ Hdom (ω), and that ϕDm − ϕ = m
                                                             P
                                                       ϕH + i εm,i ϕCi tends to 0 uniformly
on X an .                                                                                     
3.2. The energy pairing. Recall that every test configuration π : X → A1 admits a canon-
ical compactification π : X̄ → P1 . If X dominates Xtriv , then any θ ∈ N1 (X) pulls back to a
class θX̄ ∈ N1 (X̄ ), whose image in N1 (X /A1 ) coincides with θX considered above.
   Pick an (n + 1)-tuple of pairs (θi , ϕi ) ∈ N1 (X) × PLR , i = 0, . . . , n, and choose a test
configuration X dominating Xtriv and divisors Di ∈ VCar(X )R that determined the ϕi .
Following [BHJ17, Definition 6.11], we introduce:

# PRIMARY fixed-ample-bundle approximation and continuous operator bodies

psh iff L is nef.
Proof of Theorem 7.8. By Theorem 5.14, pure Fubini–Study metrics on L coincide with
model metrics associated to Q-models L of L that are semiample, and hence nef. Since K
is nontrivially valued, Corollary 7.6 implies that every continuous psh metric is a uniform
limit of pure Fubini–Study metrics, and hence is nef.
   To prove the converse, let L be a nef Q-model of L, determined on a model X of X.
Using again Theorem 5.14, it will be enough to show that φL is a uniform limit of model
metrics associated to semiample Q-models. Since L is ample, it admits an ample Q-model
A on some projective model X ′ dominating X (cf. [GM19, Lemma 4.12]). The pull-back
L′ of L to X ′ is nef. For each ε ∈ (0, 1) ∩ Q, Lε := (1 − ε)L′ + εH is thus ample on Xs ,
and hence on X , by [EGA, IV.9.6.4]. In particular, Lε is a semiample model of L. Since
φL = φL′ (Lemma 5.10), φLε − φL = ε(φH − φL ) converges to 0 uniformly as ε > 0, and we
are done.                                                                                 
Remark 7.10. We expect Theorem 7.8 and Corollary 7.9 to hold when L is merely semi-
ample. For this, it would be enough to show that any nef model metric on L descends to the
Stein factorization A as in Lemma 5.5; this would for instance follow from a relative version
of the local Hodge index theorem proved in [YZ16, Theorem 2.1].
7.3. Psh-regularizable metrics. The curvature form of a smooth metric φ on a line bun-
dle L is a closed (1, 1)-form, which we denote by ddc φ (see [CLD12, §6.4.1] for the non-
Archimedean case). For each trivializing section τ of L over an open U ⊂ X, the function
log |τ |φ is smooth, and ddc φ = −ddc log |τ |φ on U an . Again, this makes sense for Q-line
bundles as well.
Definition 7.11. A smooth metric φ on a Q-line bundle L is semipositive if its curvature
form ddc φ is semipositive (see [CLD12, §5.4] for the non-Archimedean case).
Example 7.12. Let L be a line bundle, s1 , . . . sr ∈ H0 (L) be sections without common zeroes,
λ1 , . . . , λr ∈ R, and maxε : Rr → R a regularized max function. Then
                          φ := maxε {log |s1 | + λ1 , . . . , log |sr | + λr }
50                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

is a smooth semipositive metric on L, see [CLD12, 6.3.2].
Definition 7.13. A (possibly singular) metric φ on a line bundle L is psh-regularizable if
φ can be written as the limit of a decreasing net φi of smooth semipositive metrics.
     If φ is continuous then φi → φ uniformly, by Dini’s lemma.
Theorem 7.14. Every psh metric φ on a semiample Q-line bundle L is psh-regularizable.
Proof. By Lemma 7.4, it is enough to prove the result when φ is a Fubini–Study metric.
After replacing L with a multiple, there exists a basis (s1 , . . . , sN ) of H0 (L) without common
zeroes and constants λi ∈ R such that φ = max {log |s1 | + λ1 . . . , log |sN | + λN }, and φ is
thus the uniform limit as ε → 0 of the smooth semipositive metrics
                           φε = maxε {log |s1 | + λ1 . . . , log |sN | + λN }
as in Example 7.12.                                                                             
7.4. The Fubini–Study operator. The following discussion is closely related to the point
of view developed by Chen and Moriwaki in [CMor18, §3.2].
Definition 7.15. Let L be a globally generated line bundle. We say that a subspace V ⊂
H0 (L) is basepoint free if sections in V generate L at all points. To each norm k · k on V ,
we then associate the metric FS(k · k) on L defined at each x ∈ X an as the quotient norm
                                                              |s(x)|
                                FS(k · k)(x) := log sup              .
                                                      s∈V \{0} ksk

     Recall that log |s| denotes the singular metric attached to s ∈ H0 (L), cf. Example 5.1.
Theorem 7.16. For any norm k · k on a basepoint free subspace V ⊂ H0 (L), the metric
FS(k · k) is continuous and psh.
Lemma 7.17. Let s1 , . . . , sr be finitely many sections of L without common zeroes, and
λ1 , . . . , λr ∈ R. Let V ⊂ H0 (L) be the basepoint free subspace generated by the si . Let k · kλ
be the norm on K r which is diagonal in the canonical basis (ei ) and such that kei kλ = e−λi ,
and denote by k·k the induced quotient norm on V with respect to the surjective map K r → V
that sends (ei ) to (si ). Then:
                              P
       (i) FS(k · k) = 21 log i |si |2 e2λi when K is Archimedean;
     (ii) FS(k · k) = maxi (log |si | + λi ) when K is non-Archimedean.
                                                                                P
Proof. For each s ∈ V , we have ksk = inf {kakλ | a ∈ K r , s = i ai si }. Using this, one
immediately checks that                                           P
                                                                 | i ai si |
                                     FS(k · k) = log sup
                                                     a∈K r \{0}    kakλ
                    an
pointwise on X . In the Archimedean case, the Cauchy–Schwarz inequality yields
                                        P
                                       | i ai si |2 X |si |2        X
                              sup                  =              =      |si |2 e2λi .
                            a∈K r \{0}   kak2λ         i
                                                          ke i k2
                                                                λ     i
In the non-Archimedean case, Lemma 1.16 yields
                               P
                              | i ai si |        |si |
                       sup                = max        = max |si |eλi .
                        r
                     a∈K \{0}   kakλ         i  ke k
                                                  i λ     i
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                51


# PRIMARY fixed-ample-bundle approximation and continuous operator bodies

                ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα             (8.1)
                                       α
                          an
on the topological space X , the mixed Monge–Ampère measure     of the φi , with δX =
P
  α m  δ
      α Xα denoting the analytic fundamental class of X (see [CLD12,  §3.7] for the non-
Archimedean case).
Remark 8.1. When K = R, we define ddc φ1 ∧ . . . ∧ ddc φn ∧ δX as the image of the
corresponding measure on X(C) = XCan by the projection map XCan → X an .
Example 8.2. Assume that n = 0, i.e. X = Spec A with A a finite K-algebra. The pre-
vious construction produces a positive measure δX on Q    the finite set X an , which is described
as follows. We have a product decomposition A = i Ai into local finite K-algebras Ai
corresponding to the connected components of X. The (reduced) irreducible components of
X are given by Xi = Spec Ki , where the residue field Ki of Ai is a finite extension of K,
and the uniquePextension of the absolute value of K to Ki defines a point xi ∈ X an . The
current δX = i mi δXi is a measure on X an , and the requirement that δXi has total mass
deg π⋆ [Xi ] = [Ki : K] yields δXi = [Ki : K]δxi . As mi [Ki : K] = dimK Ai , we conclude that
                                           X
                                     δX =     (dimK Ai )δxi .
                                                 i

Proposition 8.3. For each tuple φ1 , . . . , φn of smooth metrics on Q-line bundles L1 , . . . , Ln ,
the mixed Monge–Ampère measure ddc φ1 ∧ . . . ∧ ddc φn ∧ δX satisfies the following properties:
    (i) it is a symmetric, multilinear function of the φi , and a positive Radon measure if
        the φi are semipositive, i.e. ddc φi ≥ 0;
56                         SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON
           R
      (ii) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX = (L1 · . . . · Ln );
     (iii) if L0 = L1 = OX (and hence φ0 , φ1 are smooth functions on X an ), then
      Z                                              Z
          φ0 dd φ1 ∧ dd φ2 ∧ . . . ∧ dd φn ∧ δX = φ1 ddc φ0 ∧ ddc φ2 ∧ . . . ∧ ddc φn ∧ δX .
               c        c              c
                                                                                               (8.2)

     (iv) for any complete field extension F/K, we have
                 p⋆ (ddc φ1,F ∧ . . . ∧ ddc φn,F ∧ δXF ) = ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
         where φi,F is the pullback of φi to Li,F and p : XFan → X an is the canonical projection.
Proof. (i) is straightforward. (ii) is classical in the Archimedean case, and proved in [CLD12,
Proposition 6.4.3] in the non-Archimedean case. (iii) is a consequence of the Stokes formula
(see [CLD12, Théorème 3.12.2] in the non-Archimedean case). In the Archimedean case, (iv)
is nontrivial only when K = R, F = C, in which case it holds by definition (see Remark 8.1).
In the non-Archimedean case, it is implicit in [CLD12], and can be checked as follows. Pick
a smooth, compactly supported function f on X an , and consider the smooth, compactly
supported (n, n)-form α := f ddc φ1 ∧ . . . ∧ ddc φn . According to [Gub16, Proposition 5.13],
there exists a Zariski open subset U ⊂ X with a closed embedding U ֒→ Grm,K and a
compactly supported smooth (n, n)-superform on Rr such that α is obtained by pulling-
back η by the tropicalization map Trop : U an → Rr , and
                             Z                                  Z
                                      c              c
                                f dd φ1 ∧ · · · ∧ dd φn ∧ δX =     α
                                                                          X
is defined as the integral of η on the tropical cycle Trop(U ). Unravelling the definitions, it
is clear that the pull-back αF of α to XFan is simply the pull-back of η by the tropicalization
map TropF : UFan → Rr . The construction of the tropical cycle of an algebraic variety being
invariant under ground field extension,
                                  R       Rwe have TropF (UF ) = Trop(U ) as tropical cycles,
and we conclude as desired that X α = XF αF .                                                 
   Recall from §7.3 that a continuous metric on a Q-line bundle L is psh-regularizable iff it is
a uniform limit of smooth semipositive metrics on L. If L is semiample, then any continuous
psh metric (in the sense of Definition 7.2, i.e. a uniform limit of Fubini–Study metrics) is
psh-regularizable, by Theorem 7.14.
Theorem 8.4. Let L1 , . . . , Ln be Q-line bundles on X. The measure-valued operator
                             (φ1 , . . . , φn ) 7→ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
defined so far on smooth metrics, admits a unique continuous extension to tuples of contin-
uous, psh-regularizable metrics on the Li , with respect to uniform convergence for tuples of
metrics, and the weak topology on Radon measures.
     As a direct consequence of Proposition 8.3, we get:
Proposition 8.5. For each tuple of continuous, psh-regularizable metrics (φi ),
                                            X
             ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα
                                                     α

is a positive Radon measure on X an , of total mass (L1 · . . . · Ln ). It is further symmetric
and multiadditive as a function of the φi .
                    NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                          57

   Theorem 8.4 follows from the classical Bedford–Taylor theory [BT76] in the Archimedean
case, and from its analogue in the non-Archimedean case [CLD12, Corollaire 5.6.5]. In the
present global setting, one can however provide a simple direct argument, based on the
following global version of the classical Chern–Levine–Nirenberg inequality that will be put
to use again a bit later.
Lemma 8.6. Let L0 , . . . , Ln be line bundles on X, and suppose given a pair of smooth,
semipositive metrics φi , φ′i on each Li . Then
       Z                                            Z
          (φ0 − φ′0 ) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX − (φ0 − φ′0 ) ddc φ′1 ∧ . . . ∧ ddc φ′n ∧ δX

                                                  n
                                                  X
                                           ≤C           sup |φi − φ′i |
                                                  i=1

with C := 2 max1≤i≤n (L0 · L1 · . . . · Lbi · . . . · Ln ).
Proof. For brevity of notation, set T := ddc φ2 ∧ . . . ∧ ddc φn ∧ δX . By (8.2),
       Z                         Z                          Z
         (φ0 − φ′0 ) ddc φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T = (φ0 − φ′0 ) ddc (φ1 − φ′1 ) ∧ T
          Z                                       Z                              Z
      =       (φ1 − φ′1 ) ddc (φ0 − φ′0 ) ∧ T =       (φ1 − φ′1 ) ddc φ0 ∧ T +       (φ1 − φ′1 ) ddc φ′0 ∧ T.

Since ddc φ0 ∧ T and ddc φ′0 ∧ T are both positive measures of mass (L0 · L2 · . . . · Ln ), we infer
     Z                          Z
       (φ0 − φ0 ) dd φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T ≤ 2(L0 · L2 · . . . · Ln ) sup |φ1 − φ′1 |.
                ′   c


We conclude by symmetry and multilinearity.                                                                     
Proof of Theorem 8.4. Assume first that K is non-Archimedean, and pick f ∈ PLR (X an ).
By Lemma 5.17, we can find a pair of Fubini–Study metrics on an ample line bundle L0 such
that f = φ0 − φ′0 . By Theorem 7.14, φ0 and φ′0 are uniform limits of smooth, semipositive
metrics on L0 . Lemma 8.6 thus shows that
                                             Z
                        (φ1 , . . . , φn ) 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

is Lipschitz continuous with respect to the supnorm on tuples of smooth, semipositive met-
rics (with Lipschitz constant depending on f ), and hence extends continuously to tuples of
continuous, psh-regularizable metrics. For eachR tuple of continuous, psh-regularizable met-
rics (φi ), the linear form on PLR (X an ) f 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is positive, hence
continuous, and it thus extends to a positive linear form on C0 (X), by density of PLR (X an ).
   In the Archimedean case, the argument is similar, arguing with a smooth function f
instead. It is in fact even simpler, since f can directly be written as a difference of smooth
psh metrics on some ample line bundle.                                                         
   In order to exploit the multilinearity of the previous construction, it is convenient to
introduce the following terminology.
Definition 8.7. We say that a continuous metric φ on a line bundle L is dpsh if it can be
written as a difference of continuous, psh-regularizable metrics.
58                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

     A dpsh metric is thus the same as an approachable metric in the sense of [CLD12, §6.3].
Lemma 8.8. Every line bundle L admits a smooth, dpsh metric.
Proof. By Theorem 7.14, any ample line bundle admits a smooth, semipositive metric, and
the result follows since L can be written as a difference of ample line bundles.      
Example 8.9. If K is Archimedean, every smooth metric is dpsh.
   While this is probably true in the non-Archimedean case as well, it is less obvious, since
strictly positive (1, 1)-forms do not exist globally in this context.
Example 8.10. If K is non-Archimedean, every R-PL metric is dpsh, by Lemma 5.17.
   The operator (φ1 , . . . , φn ) 7→ ddc φ1 ∧. . .∧ddc φn ∧δX , being symmetric and multiadditive on
tuples of continuous, psh-regularizable metrics, extends to a symmetric, multilinear operator
on continuous dpsh metrics, with values in signed Radon measure. Note that Proposition 8.3
still holds for such metrics.
Example 8.11. If K is non-Archimedean and φ1 , . . . φn are R-PL metrics, then ddc φ1 ∧. . .∧
ddc φn ∧ δX has finite support. By ground field invariance, we may indeed assume that K is
algebraically closed, and that its value group is large enough to ensure that the φi become pure
after base change. By Proposition 5.16, φ1 , . . . , φn are then induced by Q-models L1 , . . . , Ln
of L1 , . . . , Ln determined on a projective model X of X. By linearity with respect to the
fundamental class [X], we may further assume that X is (geometrically) irreducible, which
allows us to assume that Xs is reduced, by Theorem 4.20. Each irreducible component Y of
Xs then determines a unique Shilov point xY ∈ Γ(X ), and
                                                       X
                        ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =  (L1 |Y · . . . · Ln |Y )δxY ,         (8.3)
                                                    Y
by [CLD12, Proposition 6.9.2] (compare [Gub07, Proposition 3.11]).
8.2. A Poincaré–Lelong formula. We start with the following integrability result.
Theorem 8.12. Let φ1 , . . . , φn be continuous, psh-regularizable metrics on line bundles
L1 , . . . , Ln , and let s ∈ H0 (X, L) be a regular section of a line bundle L, equiped with any
continuous metric φ. Then log |s|φ is integrable with respect to ddc φ1 ∧ . . . ∧ ddc φn ∧ δX , and
                                  Z
                                     log |s|φ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

depends continuously on the φi with respect to uniform convergence.
Lemma 8.13. We can find two ample line bundles A, A′ , a decreasing sequence (ψj ) of
smooth, semipositive metrics on A, and a smooth, semipositive metric ψ ′ on A′ such that
L = A − A′ and ψj − ψ ′ → log |s| pointwise.
Proof. Pick a very ample line bundle A′ such that A := L + A′ is also very ample. Let (sα )
and (s′β ) be bases of H0 (A) and H0 (A′ ), respectively, and set
                                                                                   
                           X                    X                           X
             ψj := 21 log    |s · s′β |2 + e−j   |sα |2  , ψ ′ := 21 log   |s′β |2  .
                            β                  α                             β
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                        59

These metrics are smooth and semipositive (both in the Archimedean and non-Archimedean
cases), and
                                                                
                                                   X
                           log |s| + ψ ′ = 21 log   |s · s′β |2 
                                                          β

is the decreasing limit of ψj .                                                                            

Proof of Theorem 8.12. Given any other metric φ′ on L, log |s|φ − log |s|φ′ = φ′ − φ is a con-