# Projective model functions and the original-source endpoint comparison

Date: 1 September 2026. Author: /root.
Status: new research draft; not independently accepted, not production Rethlas verified, and not a live-book theorem. All current conclusions below are conditional on the explicitly stated source-representation and local-current inputs.

## 1. Scope and the interface to be supplied

Let R be a complete discrete valuation ring, K its fraction field, k its residue field of characteristic zero, pi a uniformizer, and ell=-log|pi|>0. Let X be a smooth connected PROJECTIVE K-variety of dimension n>=2. Every model used here has generic fibre IDENTIFIED with this same X. No generic birational replacement of X and no scalar extension of an unknown current occurs.

Let W be a nonempty ordinary connected open subset of X^an. A rational moment on an ordinary open U contained in W is F=(v(f_1),...,v(f_m)), where the f_i are nonzero rational functions on X which are analytic units on U. Consider a full-dimensional source cell Delta of F, with Delta contained in U, F affine-injective on Delta, and a fixed coefficient-constant source presentation. Its interior is taken relative to its n-dimensional affine structure. The locally finite compact-cell presentation and absence of a lower-cell residual, when used for a current, are PRECISELY the assumptions of displayed R, not newly proved here.

The first geometric conclusion is that, inside any specified nonempty relatively open part of Delta's interior, one can choose an actual analytic point x and finitely many GLOBAL rational model functions whose simultaneous determination forces x to lie in a maximal monomial chamber of a model of the ORIGINAL X. Near x, n selected coordinates of F are an invertible affine function of that chamber's actual normal-coordinate moment. The equality holds on an ordinary source neighborhood, not only on the skeleton.

The second conclusion, conditional on L, O, Q, displayed R and the two separately authored model/graph packages, is equality of the normalized coefficients on ANY TWO such rational-moment source cells lying in W. Their moments, ordinary chart domains and cells need not coincide or intersect. This supplies the missing same-generic-X endpoint interface in the projective setting. It is not an assertion that the source-representation premise R has been proved.

The final conditional consequence explains how local rational replacement and compact ordinary partitions turn those pairwise comparisons into T=c delta_W. The exact assumptions and remaining verification boundary are repeated in Section 10; the word conditional is essential.

## 2. Exact local logarithms from global vertical ideals

Fix finitely many nonzero rational functions f_j on X and finitely many analytic points x_a having generic algebraic support. There are integral model functions G_j and one ordinary open neighborhood N of all x_a such that

    G_j(y)=v(f_j(y))                 (y in N)

for every j. The f_j are analytic units on N. The functions G_j are defined continuously on ALL of X^an, even at the zeros and poles of f_j outside N.

Here is a direct construction. Embed X into projective space P^r_K. Each rational f_j is a ratio P_j/Q_j of homogeneous polynomials of the same degree with nonzero restrictions to X. Indeed one can write it as a fraction in the affine coordinate ring on a standard projective chart and homogenize numerator and denominator to equal degree. Multiply both polynomials by a common power of pi so that their coefficients are integral. The common factor cancels in their ratio.

Let M_0 be the normalization of the scheme-theoretic closure of X in P^r_R. It is an integral projective flat model with generic fibre X. Normalization is finite here by excellence of R. Pull back O(deg P_j) and the two sections to M_0. Write them s_j^+ and s_j^-, so f_j=s_j^+/s_j^- on their common nonvanishing locus. They are honest integral sections of the SAME model line bundle for each j; no extension-of-line-bundles assertion is being assumed.

For one such section s of a model line bundle L and an integer M>0, define the coherent ideal

    I(s,M) = image(s:L^(-1) -> O_(M_0)) + pi^M O_(M_0).

Its generic-fibre restriction is O_X, so it is a vertical ideal. In a local model frame e with s=a e it is (a,pi^M). Changing e multiplies a by a model unit and does not change this ideal. Let ||s|| be the continuous norm of the model metric on L. At every actual analytic point whose center lies in this frame open,

    tau(s,M) := -log|I(s,M)| = min(-log||s||, M ell).       (2.1)

The right side takes value M ell when s vanishes. Model units have norm one on their reduction domains, so this identity holds on the entire source, not just on monomial points.

For completeness, normalize the blowup of I(s,M). The pulled-back ideal is invertible, of the form O(-E) for an effective vertical Cartier divisor E. With the BFJ convention phi_D=log|O(D)|, equation (2.1) says tau(s,M)=phi_E. In particular tau(s,M) is an integral model function. This is the direct ideal construction in BFJ Proposition 2.2; its sign is fixed here by O(-E)=I O.

At a generic-support point each nonzero section has nonzero finite norm. Choose M large enough that

    -log||s_j^+(x_a)|| < M ell,
    -log||s_j^-(x_a)|| < M ell

for all finitely many pairs and points. Continuity makes all these strict inequalities hold on one ordinary neighborhood N of the finite set. In particular no section vanishes there. On N put

    G_j = tau(s_j^+,M) - tau(s_j^-,M).

Since the two sections use the same model metric, their metric factors cancel, proving G_j=v(f_j) exactly. This construction does not claim global equality with a logarithm having poles. It also does not require a path between the x_a to stay inside N.

## 3. Choosing an independent point of an original source cell

Choose any nonempty relatively open V_Delta inside the interior of Delta. The affine-injective map F has rank n there. Thus n of its coordinate functions, indexed by J={j_1,...,j_n}, have independent linear parts. Their joint values range over a nonempty open subset of R^n.

Choose x in V_Delta for which

    ell, v(f_(j_1)(x)), ..., v(f_(j_n)(x))

are Q-linearly independent. Such choices are dense: each prohibited nonzero rational relation is a proper affine hyperplane in that open subset, and a countable union of these hyperplanes has empty interior by the Baire theorem. No assertion is made that the set of dependent points is a finite polyhedral exceptional set.

This x has generic algebraic support. To see this without importing a valuation-rank converse, let xi be its underlying algebraic point. The chosen f_(j_i) are defined and invertible at x, hence have images in kappa(xi). A nonzero polynomial relation among these images with coefficients in K would have finitely many nonzero terms. Their valuations are

    v(a_nu) + sum_i nu_i v(f_(j_i)(x)),

with v(a_nu) in ell Z. Independence makes the valuations of distinct terms distinct. The least-valued term cannot cancel, a contradiction. These n images are therefore algebraically independent over K. Since dim X=n and X is integral, trdeg_K kappa(xi)>=n forces xi to be the generic point. This justifies applying Section 2 at the chosen source point.

Apply Section 2 to the selected rational functions. It gives global model functions G_i equal to v(f_(j_i)) on an ordinary neighborhood N_x of x.

## 4. Every sufficiently high determination captures the SAME point

Let M be any regular SNC model of X determining all the G_i. Extra global model functions or finitely many other models may be included in its common domination. Such models exist in the original-DVR residue-characteristic-zero projective setting by BFJ Sections 1.1 and 2.4. The special-fibre multiplicities need not be one.

Let z be the center of x on M, and let E_1,...,E_r be the distinct vertical components through z, with multiplicities N_b>0. Choose local equations t_b. At the actual point x write alpha_b=v_x(t_b)>0. Every local-ring unit has valuation zero: it and its inverse lie in the valuation ring of the center. Therefore, if G_i is determined by sum_b d_(ib) E_b near z, with rational d_(ib), then

    ell = sum_b N_b alpha_b,
    v(f_(j_i)(x)) = G_i(x) = sum_b d_(ib) alpha_b.          (4.1)

The n+1 independent numbers on the left lie in the Q-span of the r numbers alpha_b. Thus r>=n+1. Strict normal crossings on the regular (n+1)-dimensional total space gives r<=dim O_(M,z)<=n+1. Consequently r=n+1, z is a closed maximal-stratum point p, and all the n+1 positive alpha_b are Q-linearly independent. In particular p has a finite residue field extension of k. Rename the parameters t_0,...,t_n.

The SAME point x is the monomial point with these normal values, not merely a point mapping to the same tropical target. Here is the required uniqueness argument. In the regular local ring A=O_(M,p), m=(t_0,...,t_n), take 0!=a in A and let d=ord_m(a)<infinity. Choose L>d with

    L min_b(alpha_b) > d max_b(alpha_b).

The regular associated graded ring gives a finite expansion modulo m^L with coefficients chosen as zero or unit lifts from kappa(p). The error lies in m^L, hence has valuation at least L min alpha_b. Some degree-d retained coefficient is nonzero; its valuation is at most d max alpha_b. All distinct retained monomials have distinct valuations by independence. Thus the error and all other terms cannot cancel the unique least-valued retained term. This determines v_x(a) as the minimum of their monomial values, finitely. The argument applies equally to the standard monomial valuation with weights alpha and gives equality on A and then on its fraction field K(X).

BFJ Section 3.3 constructs the monomial embedding with precisely this rule, or equivalently using the completed regular local ring. An analytic point with generic support is determined by its valuation on K(X). Hence x really belongs to the interior of M's maximal monomial chamber at p.

This argument works for EVERY higher SNC determination of the G_i. In particular a later common model does not silently replace x by a different lift or a section. It is not necessary to first choose a generic birational access variety Y.

## 5. An invertible relation on an ordinary source neighborhood

Let D_p be the entire ordinary analytic tube reducing to the closed point p. Each t_b is an actual analytic unit there, since every component is vertical and pi is nonzero on the generic fibre. The local special-fibre equation and the model-function equations give, on all of D_p,

    pi = epsilon product_(b=0)^n t_b^(N_b),
    G_i = sum_(b=0)^n d_(ib) v(t_b),

where the local model unit epsilon has norm one everywhere in the tube.

The identification of D_p with an entire multiplicity hypersurface is a geometric input preceding L, not a conclusion of L's analytic projection theorem. Specifically use the completed-ring/formal-tube interface recorded in O Section 2. At this maximal point it has a direct algebraic check: the finite separable residue extension kappa(p)/k has an unramified lift R_p/R, which embeds in the henselian completed local ring. Successive maximal-ideal approximation gives a surjection R_p[[T_0,...,T_n]] onto that completion. Lift the unit in the equation for pi to a formal unit epsilon(T). The quotient by pi-epsilon(T) product T_b^(N_b) is regular of dimension n+1: its relation has nonzero linear pi term, since sum N_b>=n+1>=3. The further surjection onto the completed regular local ring of the same dimension is an isomorphism. The special-formal generic-fibre/tube identification in that interface gives the ENTIRE p-tube, with all |T_b|<1; all T_b are automatically nonzero. Only after this identification does L apply, with omitted multiplicity N_0 and coefficient-field degree [kappa(p):k]. No root of epsilon or base change of T is used.

Set q=(v(t_1),...,v(t_n)), omitting t_0. On the ordinary open H_0=D_p intersect N_x intersect U,

    F_J = B q + c,                                       (5.1)
    B_(ib)=d_(ib)-d_(i0)N_b/N_0,
    c_i=d_(i0)ell/N_0.

The n by n matrix B is invertible. If not, the rational matrix with first row (N_0,...,N_n) and subsequent rows (d_(i0),...,d_(in)) would have a rational row dependence. Evaluating at alpha would yield a nonzero rational relation among the n+1 independent values in Section 3. This is impossible.

Equation (5.1) is an equality of ordinary smooth logarithmic functions on H_0, so the two expressions give the same ordinary pulled-back top forms there. It is NOT asserted outside N_x. The complete p-tube need not be contained in U or W. These points matter in the next comparison.

## 6. Saturating a path without imposing endpoint identities along it

Take any two rational-moment source cells Delta_0 and Delta_1 as in Section 1, with prescribed nonempty relatively open interior pieces. Apply Sections 2–3 to choose x_0 and x_1 and the finite list of global model functions for their selected coordinates. These functions may be determined simultaneously.

The connected ordinary W is path connected by Berkovich's local contractibility theorem in the stated smooth algebraic, nontrivially valued setting. Choose a path in W from x_0 to x_1 and let P be its compact connected image. The saturated-open package constructs a rational model function g such that

    P subset V={g>1/2},       closure(V) subset W.

Choose a common BFJ-SNC model M determining g and ALL of the endpoint G_i. The exact determined-divisor identity g composed with p_M=g gives full ordinary saturation of V. Sections 4–5 put each x_a in the interior of an actual maximal chamber of this M and supply its endpoint ordinary neighborhood H_(0,a). The connected set p_M(P) lies in V intersect Sk(M) and retains the actual endpoints.

There is no requirement that P, V, or every intervening chamber lie inside N_(x_0) or N_(x_1). The G_i need equal the original logarithms ONLY where the endpoint test will be supported. Along the path it is g, a different globally determined model function, that controls ordinary support.

Apply the separately authored stratum-incidence/controlled-chambers argument and its actual-model augmentation input to M, g and those two initial chambers. It produces on a common higher model a finite chain of chambers joined through WHOLE proper residual curves. At every crossing an independent normal point has g>1/2. All modifications have the same generic X; the old chambers and their full maximal-point tubes survive the star augmentations. An optional actual toroidal subdivision can also be accommodated: the endpoint remains captured by Section 4, and the affine positive portions of the old chambers have finite adjacent subchamber chains.

The cited packages prove geometry independently of R. Their current consequence uses L, O, Q and displayed R. This note assumes those packages with their actual stated hypotheses; it does not replace their proofs by connectedness of an old skeleton.

## 7. One identical compact source test anchors the original coefficient

Let T be a positive separately closed ordinary CLD current of bidegree (0,0) on W. Assume the following exact interfaces on the domains in use:

- The geometric completed-ring/formal-tube interface in O Section 2 identifies the entire model p-tube as in Section 5. On that actual hypersurface L gives finite proper projection and canonical degree, including all multiplicities and residue degrees.
- Q gives the target-open comparison for T defined on the FULL inverse image of a connected ordinary target open, including arbitrary compact ordinary source multipliers under displayed R.
- O gives the W-supported proper residual-curve comparison, with its full shallow collars and compact principal-divisor tests.
- Displayed R gives the locally finite coefficient-constant source-cell formula, including arbitrary smooth compact source multipliers and no lower-cell residual, for the rational moments, model-coordinate moments and their required ordinary restrictions.

At one endpoint use the final model's closed point p and q from Sections 4–5. If D=sum_b a_b E_b determines g there, the tube intersection D_p intersect V is EXACTLY q^(-1)(Omega), where

    Omega={u_b>0, sum_(b=1)^n N_b u_b<ell,
       (a_0/N_0)(ell-sum_(b=1)^n N_b u_b)+sum_(b=1)^n a_b u_b>1/2}.

This is nonempty, convex and open because x lies in it. It contains EVERY source point over each of its target points, not just a selected skeleton section. It lies inside W. Q therefore assigns one normalized coordinate constant kappa_p=b_p/(N_0 [kappa(p):k]) on this whole target-open domain.

Let r_Delta=b_Delta/a_Delta denote the ratio on the original cell, with a_Delta>0 its canonical source coefficient in the same coordinates. By local finiteness of its compact-cell presentation and x in Delta's interior, choose an ordinary neighborhood H of x whose intersection with the source skeleton of F meets no cell other than that interior piece of Delta. Shrink H so that H is contained in H_0 intersect V and its closure is compact in that open. Ordinary smooth cutoffs allow a nonnegative rho supported in H with rho positive near x.

Choose a nonnegative smooth target density h compactly supported in a small neighborhood of q(x) in Omega and positive near q(x). Put beta=h(u) eta_q, where eta_q is the interleaved coordinate (n,n)-form. The ordinary compact source form

    theta = rho q^* beta

is supported where (5.1) holds. If alpha_J on R^n is defined by

    alpha_J(y)=h(B^(-1)(y-c))/(det B)^2 eta_J,

then q^*beta=F_J^*alpha_J on H. Pull alpha_J back by the selected-coordinate projection R^m->R^n to view theta as the SAME F-based form. The target form need not be compactly supported in all m coordinates: the actual source multiplier has compact support, which is the R hypothesis.

Its canonical integral is strictly positive. The standard monomial section of q is continuous, takes q(x) to x, and lies in H for a small target neighborhood. There rho and h are positive. The canonical calibration is N_0[kappa(p):k]>0. Integrating over this nonempty target open proves the asserted strict positivity. This does not assert that all source points in H are monomial points.

Apply Q to theta to obtain <T,theta>=kappa_p<delta_W,theta>. Apply displayed R to its F-based expression. Only Delta contributes by the choice of H, and the canonical integration formula uses the identical cell coordinates and target density, so <T,theta>=r_Delta<delta_W,theta>. Dividing by the positive common canonical integral gives

    r_Delta = kappa_p.                                   (7.1)

No equality of two unrelated source skeleta is required for this argument. It uses one actual common compact form, isolation only in the original F presentation, and the positive canonical integral on the known q-monomial section. The invertible affine determinant is applied to both current and canonical pairings. Nor is the current extended from H to an entire tube: Q applies to its actual already available restriction on D_p intersect V contained in W.

## 8. Conditional equality of all rational-moment cell ratios in W

For Delta_0 and Delta_1, the controlled chamber chain in Section 6 and the degree-accurate current overlap in the stratum-incidence package identify their two coordinate constants kappa_(p_0) and kappa_(p_1). Every crossing uses O on the same current in W, and every complete chamber piece uses Q on a connected full-source target-open domain. The same omitted-normal multiplicity and the actual closed-point residue degree are retained in each comparison.

Equation (7.1) at the two endpoints now gives

    r_(Delta_0) = r_(Delta_1).                            (8.1)

The moments may be different and their chart domains disjoint. The only connecting set chosen is the path P in W; support outside W is never used. The argument applies inside any prescribed relatively open interior portion of each cell. For a different fixed presentation or a refinement, an original coefficient is compared by its own local compact test, so (8.1) also compares presentations rather than just one decomposition chosen globally in advance.

This is a conditional comparison theorem in the smooth projective original-DVR residue-characteristic-zero setting. In contrast to the former generic-birational access route, its models throughout are models of X itself. It still does not prove R, L, O or Q.

## 9. Conditional passage to all ordinary compact top-form tests

This step is included to expose the coverage obligation instead of stopping at a finite list of convenient moments.

On an algebraic analytification every analytic unit h near a point x can be replaced, after ordinary shrinking, by a nonzero rational function f with |h-f|<|h|. Indeed, in an affine algebraic chart A the field Frac(A/ker(x)) is dense in H(x). Approximate h(x) by an element of that field, lift it to a fraction a/b of A with b(x)!=0, and use continuity to retain the strict inequality near x. Then f=a/b is a rational function on X and is a unit there; the ultrametric inequality gives |h|=|f| on that WHOLE ordinary neighborhood. Do this simultaneously for finitely many coordinates of an analytic moment. This is the strict-approximation mechanism of CLD 12.2.3 with rational algebraic representatives; it is not an equality of analytic functions. Their tropicalizations, and hence their ordinary pulled-back forms, coincide on the chosen neighborhood.

Take an arbitrary ordinary compactly supported (n,n)-test form theta on W. Its ordinary local descriptions by analytic moments admit a finite cover of its support. Make the rational replacements just described on a finite refinement. If the formulation of R requires paracompact chart domains, choose them to be sets {chi>0}, where chi is a nonnegative compact ordinary smooth cutoff supported in the original moment neighborhood and positive near the chosen point. Each such open is the countable union of compact sets {chi>=1/l}, hence is sigma-compact and locally compact Hausdorff, therefore paracompact. Finitely many cover the test support. This does not require W itself to be paracompact.

Choose ordinary smooth compact cutoffs phi_i supported in these smaller neighborhoods with sum H positive near supp(theta), and another compact cutoff eta in {H>0} equal to one near supp(theta). The functions rho_i=eta phi_i/H, extended by zero, form a finite smooth partition equal to one near supp(theta). Thus theta is a finite sum of actual compact-source forms rho_i F_i^*alpha_i with rational moments on their ordinary domains. The cutoffs are supplied by CLD Corollary 15.2.5 (or its compact-set partition version 15.2.9); a separated good algebraic analytification is locally holomorphically separated, as required. No G-open domain is treated as an ordinary neighborhood without this justification.

Assume displayed R is available on these domains and every coordinate domain required in Sections 6–8. Local finiteness makes each summand's R formula finite on its source support. All of its full-dimensional coefficients have the same normalized ratio c by (8.1), comparing them also across the finitely many moments. The lower-dimensional residual is zero BY R. The identical canonical calibration formula then gives <T,theta>=c<delta_W,theta>.

If at least one such cell exists, c is fixed by that reference cell and is finite and nonnegative. A reference cell can also be produced by the geometric packages: apply saturation to any single point of nonempty W, choose a positive vertex in its skeletal superlevel, and augment that vertex by ample cuts. A new maximal chamber has a nonempty relative-open part with g>1/2 near that vertex. Its coordinate moment on the corresponding full-source target-open domain lies in W and has positive canonical coefficient by L. A convenient top cell supplies the reference. Thus this auxiliary existence is not a presumption that the original unaugmented skeleton was pure of dimension n.

Under ALL the foregoing current and geometric premises, therefore,

    T = c delta_W,     c>=0.

Uniqueness follows by testing a nonnegative compact form with positive canonical integral on the reference cell. This conditional conclusion does not promote an unverified source representation to a theorem: R is exactly what excludes both varying source-cell measures and a lower-dimensional residual in this last step.

## 10. Example, scope exclusions, and verification status

On X=P^n_K with homogeneous coordinates Z_0,...,Z_n, take f_j=Z_j/Z_0. On the ordinary region where the standard model frame Z_0 has norm one and 0<v(f_j)<M ell, the ideals (Z_j,pi^M) in the corresponding model-line-bundle sense give tau_j=v(f_j), while tau_0=0. Thus G_j=tau_j-tau_0 agrees exactly with the coordinate logarithm there, although globally it is a bounded continuous model function. A point with ell and these n coordinate values Q-independent must lie in a maximal chamber on every SNC determination of these functions. The original smooth model of projective space has no such maximal chamber for n>0; the necessary vertical modifications, not a change of generic variety, create it.

The geometric local-logarithm construction and the independent-point capture use existing BFJ model theory plus the displayed elementary proofs. They are not a priority claim. The propagation and whole-current assertions additionally use the two new geometric packages and the exact research premises L/O/Q/R. These are distinct logical dependencies, not interchangeable audit labels.

Not established here: R itself or the discarded stronger local-affine-separation argument; arbitrary nonalgebraizable analytic spaces; nonprojective X without a separately justified projective passage; other value groups; residue-positive-characteristic model existence; higher-bidegree rigidity; general plurisubharmonic regularization; or the envelope property. No claimed resolution of those questions follows from the conditional identity above.

This draft requires independent exact-byte review and production Rethlas verification before any new mathematical statement can be promoted into the book or an open item retired. No source inventory or live chapter is changed. Corrections after freeze must be made in a sibling version or addendum, preserving the reviewed history.
