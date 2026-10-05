# n3. Conditional countable-field Runge, Hartogs, and singular-stratum chain

This is a full mathematical proof draft of a CONDITIONAL countable-field chain, using n1 and n2. The field k is countable, algebraically closed, trivially valued, and of characteristic zero. Y is integral affine of finite type. The original u is usc, generically finite, locally bounded above, has an upper bound by an actual original-ring AFS exhaustion, and is weak on ONE proper birational contact witness. All uses of the accepted smooth affine gate retain GEO as defined in n1, including the required smooth ample-boundary compactification and projective birational domination of that same restricted witness by a smooth projective source. No arbitrary completed-residue-field affine theorem or singular EP is imported.

## Split pieces on one controlled neighborhood, including gamma=1

Suppose pi:Y->S is finite surjective onto a principal affine open of A^n. Suppose Z is closed, pi|Z is a CLOSED IMMERSION onto its image, and Z and Z'=pi^(-1)(pi(Z))\Z are disjoint closed subsets. Assume the ORIGINAL u is locally genuinely AFS regularizable off Z. We prove its strict sublevels are Runge.

Use n2's countable nonnegative rho and its positive support replacements. If a strict sublevel of u_c=u+c rho, c>0 rational, is not Runge, there is compact L such that its compact polynomial hull K contains a point where u_c>=0 although sup_L u_c<0. After an additive normalization let sup_K u_c=0 and sup_L u_c=-delta<0; if the latter is minus infinity choose any finite delta with sup_L u_c<=-delta. The finite attained maximum x belongs to Z by n2's off-bad-set inequality.

Put C=hull_S{pi(x)}. Because pi|Z is a closed immersion, the quotient-ring hull property gives C subset pi(Z)^an. The ENTIRE compact preimage of C consists of disjoint compact pieces C_1 in Z and C_2 in Z'. Choose disjoint open neighborhoods A_1,A_2 of these pieces, with A_1 avoiding Z' and A_2 avoiding Z. Properness of the finite analytic map gives an open neighborhood A of C whose entire preimage is in A_1 union A_2: take the complement of the closed image of Y^an\(A_1 union A_2).

By n2's strict polynomial neighborhoods choose a nonnegative actual base AFS g with C in an inner strict neighborhood U where g=0, and {g<=1} compactly contained in A. Let W={g<1}; its preimage splits into the clopen OPEN pieces W_i=pi^(-1)(W) intersect A_i. These interiors are not compact; their controlled closures in pi^(-1){g<=1} are compact. On the preimage of W put h=1 on W_1 and 0 on W_2. The global continuous contact weight H=max(3g circ pi-1,h) there, and 3g circ pi-1 elsewhere, has a whole reference-winning outer collar, and equals h over U.

The task-granted continuous canonical norm trace makes the trace of this indicator over U continuous and integer valued:

gamma_1(s)=sum_{y in pi^(-1)(s) intersect W_1}m_y.

It is only LOCALLY constant. Shrink ONE base neighborhood N of pi(x) inside U where gamma_1 is the positive integer gamma; retain this N for EVERY subsequent hull, boundary and fiber test. All weights m_y are the raw positive canonical integers of n1, never fiber lengths. A closed immersion guarantees analytic fiber injectivity, so the W_1 fiber above pi(x) is exactly {x}, even after a completed residue-field extension.

For gamma>1 shrink N further so all its W_1 fiber values of u_c are <delta/[2(gamma-1)]. This follows from usc at the unique central point x and properness: cover that point by the requisite strict sublevel, cover the other central piece by W_2, and exclude the closed image of the complement. For gamma=1 do not divide by gamma-1. Positivity and integrality imply every W_1 fiber over N is one point of weight one.

Choose a relatively compact open V around x with compact closure in pi^(-1)(N) intersect W_1, disjoint from L. Let K_V=boundary(V) intersect K. Replace rho by rho' with equality at x and rho'<=rho-delta' on boundary(V). Put u'_c=u+c rho'. Then u'_c(x)=0, u'_c<=u_c, and sup_{K_V}u'_c<=-c delta'. The factor c is essential.

On W_1 put v=u'_c, on W_2 put v=0. On the controlled compact closure these have a finite common upper bound M. Choose a rational C_0>M+1+delta and define

tilde v=max(C_0 g circ pi-delta,v) on pi^(-1)(W),
tilde v=C_0 g circ pi-delta outside.

For g sufficiently close to 1 the reference wins on the ENTIRE collar. Pullbacks, products, support replacements and maxima all use the SAME original witness. Its pullback remains locally a decreasing contact limit. The global upper bound is an actual original reference, and the floor makes tilde v finite. Over U it is max(u'_c,-delta) on W_1 and zero on W_2. Apply n1, retaining its GEO applications, to obtain w=N_pi(tilde v) as a genuine original-base AFS limit. Pullback w circ pi is a genuine original-source AFS limit. To retain every source generator, use its monic norm bound to dominate a source exhaustion by a positive multiple of a base exhaustion and append decreasing low floor/generator branches as in n2; the limit is unchanged at every point.

Rossi gives x in hull_Y(K_V), hence w(pi(x))<=sup_{K_V}w circ pi. Its left side is zero. For z in K_V intersect Z, analytic injectivity and avoidance of Z' make the W_1 fiber exactly {z}, of weight gamma, giving

w(pi(z))<=-gamma min(delta,c delta').

For y in K_V\Z, the off-bad-set inequality gives u_c(y)<=sup_L u_c<=-delta, so tilde v(y)=-delta. Every other W_1 fiber point is in the SAME pi^(-1)(N); when gamma>1 its value is at most delta/[2(gamma-1)]. Thus, writing its positive weight m_y>=1,

w(pi(y)) <= -m_y delta+(gamma-m_y)delta/[2(gamma-1)] <= -delta/2.

When gamma=1 there is no other W_1 point and w(pi(y))=-delta. The W_2 values are zero. These are uniform negative bounds on ALL of K_V, a contradiction. Consequently each {u+c rho<0} is Runge. As rational c decreases to zero these opens increase to {u<0}, since rho is finite and nonnegative; compactness gives Runge for their union. The argument applies at every translated level. It preserves minus infinity, all raw weights, the whole collar, and one controlled base neighborhood.

## Genuine Runge exhaustion before coefficient radii

For a countable ring R, the seminorm topology of Y^an is a subspace topology of the countable product of the norm coordinates |f|, f in R. It is second countable and metrizable. Generator-bounded polydisc domains are compact and exhaust Y^an through their strict interiors. Hence every open Runge D admits a countable exhaustion by compact subsets L_r with controlled interiors.

Inductively take the polynomial hull of L_r union the previous controlled closure. It is compact and stays in D by the Runge property. Apply n2's thick polynomial-neighborhood construction to obtain STRICT finite polynomial opens Q_r, with compact controlled closures P_r contained in D, satisfying P_{r-1} subset Q_r and L_r subset Q_r. Then Q_r increase and exhaust D. Their defining polynomials retain bounds for EVERY original generator. We use Q_r={log|P_{rj}|<b_{rj}}, with rational b_{rj}; we do not identify the interior of an arbitrary closed weak-inequality domain with its strict-inequality locus.

Apply this to a genuinely established Runge D in (Y times A^1)^an containing the zero section, writing each P_{rj}=sum_i a_{rji} w^i in ORIGINAL R[w]. The opens where zero lies in Q_r are

Omega_r={log|a_{rj0}|<b_{rj} for all j};

they increase and cover Y^an. For y in Omega_r the fiber is the analytic affine line over F=H(y). Define its open-disc containment radius d_r(y). The EXACT formula is

-log d_r(y)=max_{j,i>=1}(log|a_{rji}(y)|-b_{rj})/i.       (D)

Zero coefficients contribute minus infinity; an empty maximum is minus infinity and means radius infinity. The constant-coefficient conditions defining Omega_r are indispensable.

To prove (D), on a closed radius-s disc the polynomial Gauss norm is max_i |a_i|s^i at EVERY positive real s, whether or not s is in the value group. The ultrametric inequality bounds every point by that norm. Hence the open radius-r disc is contained in all strict constraints exactly when each positive-degree coefficient has |a_i|r^i<=exp(b_j), given the strict constant constraints. Equality at the endpoint causes no problem, since the endpoint is excluded. Conversely a larger open radius contains a Gauss point violating a constraint. This proves (D) over any completed residue field using only polynomial norms, not a regularization theorem there.

By the nesting, d_r increase. For every s<d_D(y), the compact closed fiber disc of radius s lies in D, so a finite subcover of the increasing Q_r puts it in one Q_r. Thus d_r(y) increase to d_D(y), including infinity, and A_r=-log d_r decrease to -log d_D on every eventually defined Omega_r. The exhaustion includes a w-bound, so individual A_r can be taken to have a constant floor. Their rational positive coefficient maxima are continuous contact weights on Omega_r.

If u_D=-log d_D is generically finite and bounded above by an original AFS reference g+B, we now prove controlled ORIGINAL-ring regularization. Choose R_i increasing and C_i decreasing as in n2's G, and indices r_i increasing so the compact {g<=R_i} lies in Omega_{r_i} and A_{r_i}<g+B+1 there. The latter assertion follows from nested compact closed superlevel emptiness; no Dini assertion for u_D is used. Glue max(A_{r_i},cg+C_i) inside {g<=R_i} to cg+C_i outside. The outer reference wins on a whole collar. These continuous contact weights decrease on the old compact domain, the new annulus and the exterior separately, exactly as in G. The granted bridge and decreasing genuine closure give membership in ONE actual bundle cB_ref, then same-class FS regularization gives original-ring affine FS weights decreasing to u_D. Every original coefficient and every original generator is retained by localization and dominated padding. Infinite radius values give minus infinity correctly. This proves the needed Hartogs conclusion after Runge, without presupposing the affine weak/global theorem.

## Hartogs on the same product witness

For any original u as above put H=log|w|+u circ p on Y times A^1, defining its value to be minus infinity when w=0 or u=-infinity. There are no plus-infinity values. Its one witness is P times A^1. Restrict each original contact approximant and approximate log|w| by its decreasing rational floors on the same neighborhoods before taking sums and limits. Supports away from its zeros are unit logarithms, and the zero floors provide continuous contact weights. Thus H is weak on that SAME product witness. It has upper growth by a product exhaustion retaining every Y-generator and w.

On a good affine chart where ORIGINAL u is an AFS limit, H is an actual AFS limit: form products for positive sums, use decreasing floors for log|w|, and append decreasing low generator branches retaining every product-chart generator. If the split-piece hypotheses hold on Y, they hold on Y times A^1 with Z times A^1 and pi times identity, including closed immersion and closed disjoint complementary piece. Applying the already proved split argument to H proves

D={log|w|+u circ p<0}

is genuinely Runge in the PRODUCT. This is not inferred merely from sublevels on Y. It contains the zero section, and its fiber radius is exp(-u(y)), with infinity when u(y)=-infinity. Therefore the preceding coefficient argument gives actual AFS regularization of u. The same reasoning with EMPTY bad set will supply the final local-to-global step.

## Descending Z and localization

Suppose only pi|Z is a closed immersion; drop the initial disjoint-piece hypothesis. Define reduced closed sets Z_1=Z and

Z_{r+1}=Z_r intersect closure_Y(pi^(-1)(pi(Z_r))\Z_r).

They strictly drop dimension until empty. To check ALL components, a closed immersion identifies pi(Z_r) with Z_r; images of its irreducible components are distinct and incomparable. Each component T of Z_r is a component of pi^(-1)(pi(Z_r)): a containing component maps onto a containing component of pi(Z_r), and finiteness preserves its dimension, forcing equality. The closure of the complementary union therefore omits the generic point of every component T. Its intersection with Z_r has strictly smaller maximum dimension. Outside pi^(-1)(pi(Z_{r+1})), the complementary piece pi^(-1)(pi(Z_r))\Z_r is closed, since the only new closure points on Z_r are in Z_{r+1}. This also proves the required localization equality, rather than just a set-theoretic dimension estimate.

Inductively let Pi_r assert ORIGINAL local AFS regularizability at every closed point of Y\Z_r. Pi_1 is the assumed off-Z cover. A closed y in pi^(-1)(pi(Z_{r+1}))\Z_{r+1} is off ORIGINAL Z: otherwise closed-immersion injectivity places it in Z_{r+1}. Use the original off-Z cover. For any other y in Y\Z_{r+1}, choose a principal affine base S' inside S\pi(Z_{r+1}) around pi(y), and set U=pi^(-1)(S') EXACTLY. The induced finite map is onto S'. On U the bad set U intersect Z_r and its complementary inverse-image piece are disjoint closed; the off-bad-set local hypothesis is Pi_r. Apply the split proof on U times A^1 using the same product witness. Its Hartogs domain is Runge, so the preceding coefficient argument gives actual AFS regularization on U. This proves Pi_{r+1}.

At the empty last Z_r we have an algebraic affine local cover. Closed-point neighborhoods cover every scheme point: finite-type schemes over a field are Jacobson, so a nonempty closed complement would contain a closed point ([Stacks 33.14.1](https://stacks.math.columbia.edu/tag/0478)). Their analytifications therefore cover every analytic point. A local cover is not yet the desired global affine conclusion. Apply n2's off-bad-set proof with Z empty to get every {u+c rho<0} Runge, hence {u<0} Runge. Apply that SAME empty-bad-set reasoning to H on the product; now its Hartogs domain is Runge, and the coefficient argument gives ORIGINAL global AFS regularization of u. This supplies the final LOCAL-TO-GLOBAL implication that was missing from the printed induction.

## Finite projection along a smooth stratum, with the correct U

Let Y be integral affine of dimension n and Z proper smooth closed, with dim Z<=n-1. For a closed k-point z in Z, embed the projective closure X into P^D with D>=n+1. Let B=X\Y and T=closure_X Z union B, reduced. T has dimension <=n-1 and is smooth at z, since z is outside B.

Choose a projection center p outside X, outside the closed secant cone from z to T\{z}, and outside the projective tangent space of T at z. The secant cone has dimension <=dim T+1<=n<D. The tangent space and X also have dimension <D, so a k-point outside their union exists. Projection from p is finite on X by [Stacks 43.23.1](https://stacks.math.columbia.edu/tag/0B1P). Its T-fiber over the image of z is only z, and its differential on T there is injective. This is the secant/tangent argument of [43.23.2](https://stacks.math.columbia.edu/tag/0B1Q); the following local algebra proves the needed statement also for the reduced union T with possibly several components away from z.

Let C be the local ring of the scheme-theoretic image at q, and D_T the finite local ring above it. There is just the one point above q, with residue field k. Injective differential gives a surjection on cotangent spaces, so m_{D_T}=m_C D_T+m_{D_T}^2. Nakayama gives m_{D_T}=m_C D_T. Thus D_T/m_C D_T=k is generated by 1; Nakayama for the finite C-module D_T gives D_T=C. The image inclusion and projection are consequently inverse over a Zariski neighborhood of q, after shrinking to kill the finite kernel and cokernel. Here T is smooth at z, and the secant exclusion gives the single fiber; it is not enough to know an arbitrary set-theoretic injectivity statement.

Repeat the projection while the ambient dimension exceeds n. At each step the image T is still smooth at the tested point through the just proved local isomorphism, and has dimension <=n-1; the integral projective image of X has dimension n. The final image of X in P^n is all P^n. The tested point is outside the image of B, since B is part of T and the T-fiber was the single z. Choose a principal affine open S around its image, avoiding the image of B and lying in the isomorphism neighborhood of T. Set

U=r^(-1)(S), pi=r|U:U->S.

This is the correct U, not the printed r^(-1)(W) with a different target S. U is affine, is contained in the ORIGINAL Y, pi is finite onto S, and pi|Z_U is an isomorphism onto a closed image. Its analytic restriction is injective because a closed immersion stays a closed immersion after every complete field extension. Restricting u and its original witness preserves the hypotheses; monic integrality bounds give the required reference growth on S. This geometric finite-projection step is proved here. It does not discharge GEO's separate compactification/resolution antecedents.

## Singular-stratum induction and the conditional affine conclusion

Let Y_0=Y and Y_{r+1} be the reduced singular locus of Y_r. In characteristic zero the regular locus is smooth and dense in EVERY reduced irreducible component ([Stacks 33.25.8](https://stacks.math.columbia.edu/tag/0B8X)), so maximum dimension strictly drops until Y_r is empty. Reducible and unequal-dimensional strata are allowed. Let Sigma_r assert local genuine AFS regularizability at all closed points of Y\Y_r. Sigma_1 follows on smooth affine opens from the accepted smooth gate, retaining all its GEO hypotheses and restrictions of the SAME original witness.

At a new point y in Y_r\Y_{r+1}, choose an affine neighborhood V inside Y\Y_{r+1}. Its Z=V intersect Y_r is a smooth proper closed stratum. The finite projection just proved supplies U around y and pi:U->S with pi|Z_U a closed immersion. The induction gives ORIGINAL local AFS regularizability on U\Z_U. The descending-Z/product-Hartogs theorem supplies actual AFS regularizability on U. This proves Sigma_{r+1}. At the final empty stratum, invoke the EMPTY-Z local-to-global conclusion above, not merely the existence of a local cover.

Consequently, under GEO for its specified smooth applications, every original upper-growth weak input on integral affine Y over countable k is an ORIGINAL-ring decreasing AFS limit, and every strict sublevel is Runge. Every whole-base trace used in this chain is n1's trace on the one original witness. No singular envelope theorem, Wu affine main theorem, arbitrary-field affine regularization, or printed denominator-order claim is a premise.

## A limited countable global membership consequence

Let X be integral projective over countable k, L ample rational, and phi generically finite, globally upper bounded and weak relative to the canonical reference of L. Require the same contact/GEO hypotheses on each of its specified affine witnesses; a common domination, if used, remains a conditional geometric antecedent. Choose a very ample tensor qL with homogeneous sections z_i. Its principal charts Y_i have actual reference weights rho_i=q^(-1)max_j log|z_j/z_i|>=0. Then u_i=phi+rho_i has upper growth and the conditional affine theorem applies.

Use G on the ORIGINAL projective compactification X, with its actual section z_i and matching reference rho_i. For each rational c>1 this proves genuine membership in cL of the function phi-(c-1)rho_i on Y_i, minus infinity outside. At every analytic point one of the homogeneous coordinates attains the maximum; there rho_i=0. Therefore the maximum over all chart functions equals ORIGINAL phi on all of X^an, including minus infinity. Finite maxima and varying-class decreasing closure as c decreases to one prove phi in PSH(L).

This is conditional countable weak/global membership for the stated actual ample canonical reference. It does NOT show that every genuine resolved-nef potential is constant on the analytic fibers of a resolution, and so it supplies no singular EP by itself. Onto birational descent cannot be inferred from EP on the resolution: BJ5.13 needs approaching EP on the TARGET.

Evidence and reproduction: n1-trace.md and n2-affine-tools.md contain the required trace and elementary tools. Diagnostic Wu v1 LF1731--1814,1886--1964,2200--2696 and its envelope proof LF2697--2755 are pinned; their printed conclusions are not granted premises. The primary projection units are retained in web-primary-03.json and external-premises.json. Run python3 rerun.py for the complete paper, both TeX passes, hashes and finite documentary checks. All conclusions remain unverified drafts; the unchanged original P16.1 is not solved.
