# Weighted polar estimates for the full continuous CPsh sheaf

Date: 1 September 2026. Author: /root/p213_skeletal_hostile.
Status: authored research candidate, not frozen until its manifest is issued; no independent or production verdict. This is a NEW deduction from the specified CLD calculus, not a claim that CLD 16.9.4 already states the conclusion below.

## 1. Scope, notation, and the proposed conclusion

Let X be a boundaryless, locally differentially separated tropical space of level n>=1 in the sense of CLD, with its canonical positive closed integration current delta_X. All sheaves, ordinary smooth forms, positivity and compact-test topologies are those of CLD. Local differential separation supplies the compact smooth partitions, positive test majorants and Radon-measure interpretation used below (CLD 6.5.2 and 7.2.4–7.2.12). The analytic spaces in Section 8 have this property by CLD 15.2.4. Write dd=d'd''. The symbol CPsh means the least subsheaf of real continuous functions containing smooth psh functions and stable under local uniform closure (CLD 8.1.7–8.1.8), NOT merely the first locally approchable stage.

The elementary calculus input consists of CLD 8.5.1, 8.5.5, 8.7.2 and 8.8.4–8.8.5: positivity of dd(uS) for continuous CPsh u and positive closed S, continuity with uniformly converging continuous coefficients and positive currents, and the dpsh extension. The required convex composition is proved directly from CPsh minimality in Section 2; the proof does not need to identify every current-positive continuous function with CPsh or collapse its hierarchy. None of these inputs is the weighted polar estimate to be proved.

Here is the fixed-neighbourhood weighted assertion. Let Y be an ordinary open in X, let rho be smooth psh on Y, and suppose for some delta>0 that

    K_delta={rho<=delta} is compact in Y,
    U={rho<0} is nonempty.

All functions u_1,...,u_k are CPsh on a neighbourhood of K_delta, and V is a SMOOTH psh function on a neighbourhood of K_delta, negative on U. In particular V has no uncontrolled boundary singularity at closure(U). Set r=max(-rho,0), theta=dd rho, eta=d'rho wedge d''rho. Fix an integer a>=4. For 0<=k<=n put

    beta_k = r^(k+a) theta^(n-k)
             +(k+a) r^(k+a-1) eta theta^(n-k-1),          (1.1)

omitting the second summand when k=n. These are compactly supported C^2 forms; the product notation with currents means the coefficient-measure pairing explained below. Put

    J_k = integral (-V) beta_k wedge dd u_1 wedge ... wedge dd u_k.

The claim is

    J_k <= C(k,a) product_{j=1}^k ||u_j||_U
                       integral (-V) beta_0,             (1.2)
    C(0,a)=1,
    C(k,a)=product_{j=1}^k
                  [4e (j+a)(j+a+1)/(j+a-1)].

This is the same constant as (4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for k>=1. The restriction a>=4, and the requirement that V be smooth near closure(U), are deliberate safe strengthening of the hypotheses printed in CLD 8.4.3.

Assume further that every point has arbitrarily small neighbourhoods with such a smooth psh relatively compact sublevel. Let 0<=m<=n. If u_1,...,u_m belong to the FULL CPsh sheaf, V is locally approchable psh and locally integrable for canonical smooth top-form measures, and alpha is any ordinary smooth (n-m,n-m)-form, then

    |V| is locally integrable for the total variation of
    dd u_1 wedge ... wedge dd u_m wedge alpha.             (1.3)

Consequently this measure gives zero mass to the polar set {V=-infinity}.

For a good separated strict boundaryless pure n-dimensional Berkovich space over ANY complete field K, including a trivially valued one, Section 8 constructs the required local sublevels and applies the analytic log-pole argument. Thus the proposed analytic consequence is: for all continuous CPsh factors u_j the measure in (1.3) gives zero mass to every closed analytic subset of dimension <n.

The entire new argument is written below. No single local smooth approximation sequence for an arbitrary CPsh function is assumed. No unknown current is pulled back by a field extension or normalization. Scalar-current classification and P21.3 are not input theorems of this packet.

## 2. Squares, products, and finite-variation continuity

We first record the needed composition fact directly from the definition. If F:R->R is smooth, convex and nondecreasing, the CPsh functions u for which F(u) is CPsh form a subsheaf stable under uniform limits. Local uniform convergence is preserved by F because the functions have uniformly bounded images near each compact support. The class contains every smooth psh u by the ordinary smooth chain rule, so it is all of CPsh. Addition and nonnegative scalar multiplication follow by the same separate-variable closure argument starting with smooth psh functions. For squares on a positive range, use a globally smooth convex nondecreasing F equal to t^2 for t>=1/2: for instance prescribe F'(t)=2t chi(t) for t>=0, zero for t<=0, with chi a smooth nondecreasing cutoff from zero near 0 to one for t>=1/2, and choose the additive constant to match t^2 on that range. Thus no appeal to a broader Psh/CPsh equivalence is needed for either squares or exponentials below.

Let S be any fixed positive separately closed current of bidegree (q,q), with q<n. A dpsh function means locally a difference u-v of CPsh functions. On a relatively compact ordinary neighbourhood, shift u and v by the SAME constant M so that f=u+M and g=v+M are greater than one. The composition fact just proved gives f^2, g^2 and (f+g)^2 in CPsh. Since h=u-v=f-g,

    h^2=2 f^2+2 g^2-(f+g)^2.                              (2.1)

Thus h^2 is dpsh. For two dpsh functions h,l, their sum is dpsh, and

    h l = ((h+l)^2-h^2-l^2)/2                            (2.2)

shows that their product is dpsh as well.

In particular dd(hS), dd(h^2 S) and dd(hlS) are differences of positive currents. They have order zero and locally finite coefficient variation. This does NOT assert that derivatives of arbitrary order-zero currents have order zero; it uses the explicit CPsh decompositions and positivity of each dd(fS).

Define the symmetric bilinear energy current

    Gamma_S(h,l)
       = [dd(hlS)-h dd(lS)-l dd(hS)]/2,
    Gamma_S(h)=Gamma_S(h,h)
       = dd(h^2 S)/2-h dd(hS).                            (2.3)

All multiplications here are continuous multiplication of differences of positive order-zero currents. The formula is independent of the chosen CPsh decompositions, because each term is also the indicated distributional expression. Algebra in (2.3) proves bilinearity and symmetry.

We will repeatedly use the following EXACT continuity statement. Suppose h_j=u_j-v_j and l_j=a_j-b_j, where all four displayed sequences are CPsh and converge locally uniformly to their corresponding CPsh limits. Then

    Gamma_S(h_j,l_j) -> Gamma_S(h,l)                     (2.4)

as currents. The same holds with any additional locally uniformly converging continuous multiplier.

To verify this, work near one compact test support and choose a common positive shift for all four bounded sequences and their limits. Formula (2.1) expresses each square curvature as a finite linear combination of curvatures of positive CPsh squares, converging by CLD 8.5.1 and continuity of dd. Formula (2.2) handles mixed products. Terms such as h_j dd(l_j S) split into continuous coefficients multiplying the positive converging currents dd(a_j S), dd(b_j S). CLD 8.5.1 applies to each summand, and likewise after an additional continuous multiplier. The finitely many positive currents have uniformly bounded masses on compact supports: pair against a fixed positive compact test majorant, and use their weak convergence. Hence the signed differences have a locally uniform finite-variation bound.

This proof uses only the established positive-current continuity lemma and elementary local shifts. It does not invoke weighted CLN, polar nullity, or convergence in total variation. In particular we never multiply an uncontrolled signed weakly convergent sequence by varying continuous coefficients.

For smooth h,l, the ordinary Leibniz identity and closedness of S give

    Gamma_S(h,l)
       = [d'h wedge d''l+d'l wedge d''h] wedge S/2.        (2.5)

For h=l this is the strongly positive (1,1)-form d'h wedge d''h multiplied by S.

## 3. Positivity and nonlinear identities without stage-one approximation

First we prove Gamma_S(h)>=0 for EVERY dpsh h.

Fix a smooth psh v on an ordinary open. For each subopen consider the CPsh functions u for which Gamma_S(u-v) is positive. This is a subsheaf, contains every smooth psh u by (2.5), and is stable under uniform limits by (2.4). By the defining minimal-subsheaf property of CPsh, it contains all CPsh u.

Now fix any CPsh u and repeat the argument in the variable v. The preceding paragraph provides all smooth psh v. Formula (2.4) again gives closure under uniform limits. Hence the assertion holds for all CPsh v, and therefore locally for every dpsh difference h=u-v. Positivity is local, so these local assertions glue. This is a SEPARATE-variable closure argument, not a claim that the pair has a common smooth approximation sequence.

This also shows that Gamma_S(h) is itself a positive order-zero current, not just a signed distribution.

For a CPsh function u and a constant B>0, put w=exp(Bu). Convex increasing composition gives w in CPsh. The following identities hold:

    dd(wS)=B w dd(uS)+B^2 w Gamma_S(u),                   (3.1)
    Gamma_S(w)=B^2 w^2 Gamma_S(u).                        (3.2)

Proof: for smooth psh u these are the elementary differential chain rules and (2.5). For general u, take the subsheaf of CPsh functions satisfying both identities. Formula (2.4), positivity of all Gamma terms just proved, and CLD 8.5.1 show that both identities are stable under local uniform limits. Smooth psh functions belong to it, so minimality of CPsh proves (3.1)–(3.2). Every term is continuous in this argument for the explicit positive-current reasons in Section 2.

Combining the two formulas gives

    dd(wS)=B w dd(uS)+w^(-1) Gamma_S(w).                  (3.3)

There is no first derivative of a nonsmooth function being treated as an ordinary smooth form in this statement.

## 4. Mixed energy in top degree and Schwarz

Let Q be positive closed of bidegree (n-1,n-1). Its energies Gamma_Q(h) are positive Radon measures. For dpsh h,l, Gamma_Q(h,l) is a signed Radon measure by Section 2. Bilinearity and positivity give, for every rational t,

    Gamma_Q(h)+2t Gamma_Q(h,l)+t^2 Gamma_Q(l)>=0.          (4.1)

To obtain a simultaneous pointwise inequality, use on each relatively compact open a positive Radon measure dominating the total variations of all three terms. Their Radon–Nikodym densities A,B,C satisfy A+2tB+t^2C>=0 outside a null set for every rational t; a countable union suffices. Continuity in t gives the inequality for all real t, so

    A>=0, C>=0, B^2<=AC.                                 (4.2)

In particular the variation of the mixed measure is bounded by the sum of the two diagonal measures, up to a fixed constant. For positive continuous weights the usual weighted Schwarz/Young inequalities follow pointwise from (4.2) and may be integrated. No differentiability of those weights is needed.

We also need to relate the distributional mixed derivative with a SMOOTH function rho to this measure:

    d'(hQ) wedge d''rho = Gamma_Q(h,rho)                  (4.3)

in top degree. Initially the left side is merely a distribution. For smooth h the two cross terms in (2.5) have the same top-degree pairing with symmetric Q; their difference is antisymmetric, as in the ordinary symmetry calculation used in CLD 8.5.3. Thus (4.3) holds for smooth h.

For fixed smooth rho, both sides of (4.3) are continuous under the CPsh uniform closures: the left by distributional continuity of hQ and its first derivative, the right by (2.4), using a fixed local dpsh decomposition of rho, available by CLD 8.8.1. The same minimal-subsheaf argument proves it first for CPsh h and then by linearity for dpsh h. Therefore the mixed distribution is indeed the signed Radon measure in (4.3). Multiplication by a fixed smooth weight is now legitimate on either description.

For a smooth closed form theta, the defining formulas also show

    Gamma_(theta^j wedge S)(h,l)
       =theta^j wedge Gamma_S(h,l).                      (4.4)

We shall use this only when theta is positive, so the relevant Q is positive closed.

## 5. Compact C^2 barrier forms and integration by parts

Return to the fixed data of Section 1. Put l=k+a for 1<=k<=n, and put b_k=2 when k<n and b_n=1. The functions r^b=max(-rho,0)^b with integer b>=3 are C^2 in each smooth tropical presentation. Formula (1.1) therefore defines compactly supported C^2 forms, with support contained in closure(U), a compact subset of Y. Both theta and eta are positive, so beta_k is positive.

The exact identities on U are

    d'' beta_k = -b_k l r^(l-1) d''rho theta^(n-k),        (5.1)
    dd beta_k = b_k l[-r^(l-1) theta^(n-k+1)
                       +(l-1)r^(l-2) eta theta^(n-k)].    (5.2)

For k<n both summands in beta_k contribute to d'' beta_k, and give the factor two. For k=n, beta_n=r^(n+a) is a SCALAR and has only its first summand: its derivatives have the factor one. These surviving scalar derivatives cannot be discarded on degree grounds. This corrects an endpoint factor in the analogous printed source calculation. Both formulas extend across rho=0 with the required finite regularity: the powers appearing in derivatives vanish there, and no boundary delta term occurs.

Here is why using these C^2 forms is legitimate. Convolve the one-variable coefficient functions max(-t,0)^b with smooth compact probability kernels. On a bounded t-interval they converge in C^2 for every exponent b used in beta_k and beta_0. Their supports in t lie in t<=epsilon. Composing with rho produces smooth forms supported in the ONE compact K_delta for all sufficiently small epsilon. Their coefficients and first two derivatives converge in every member of a finite fixed smooth-chart cover of K_delta.

For an order-zero current, pairings with continuous coefficient forms converge under uniform coefficient convergence on these fixed charts. Positive compact test majorants provide the needed finite bounds. Distributional dd(uS), before using its positivity, may also be paired by transferring its two derivatives to these C^2 test coefficients; the resulting integrals converge since u is bounded near K_delta and S has order zero. Thus the limiting pairings and integration-by-parts identities are independent of the coefficient smoothing.

The smooth approximants need not retain positivity or satisfy (5.1) exactly: they are used only to justify identities, which then pass to the C^2 limit. Positivity and inequalities are applied to the limiting beta_k and to the positive energy measures already constructed.

The hypothesis that V is smooth on a NEIGHBOURHOOD of K_delta is essential for this argument. It makes (-V)beta_k a compact C^2 test coefficient. Smoothness only on U with unrestricted behaviour at its boundary would not suffice. The local polar truncations in Section 7 do satisfy this stronger hypothesis.

## 6. Weighted estimate by energy and the exponential substitution

Fix 1<=k<=n and write

    S=dd u_1 wedge ... wedge dd u_(k-1),
    Q=theta^(n-k) wedge S.

The first is a positive closed current of bidegree (k-1,k-1), and Q is positive closed of bidegree (n-1,n-1). The case k=1 means S=delta_X.

For the moment let z be a POSITIVE CPsh function, bounded above and below by positive constants on a neighbourhood of K_delta. Put

    J(z)=integral (-V) beta_k wedge dd(zS).

The distributional product rule with smooth V and beta_k, closedness of S, and the compact C^2 justification above give

    J(z)= integral z(V dd beta_k-dd V wedge beta_k) wedge S
                      +2 integral V d'(zS) wedge d''beta_k.    (6.1)

One can verify the sign first by expanding dd(-V beta_k) and applying Stokes to d'(z V d''beta_k wedge S); Section 5 permits the C^2 passage. Symmetry combines the two cross terms. Formula (4.3) and (5.1) identify the last term with

    2b_k l integral (-V) r^(l-1) Gamma_Q(z,rho).           (6.2)

The Radon–Nikodym inequality (4.2), with weights
r^(l/2)/sqrt(z) and b_k l sqrt(z) r^((l-2)/2), gives

    2b_k l(-V)r^(l-1) Gamma_Q(z,rho)
       <=(-V) r^l z^(-1) Gamma_Q(z)
                   +b_k^2 l^2(-V) z r^(l-2) Gamma_Q(rho). (6.3)

Here Gamma_Q(rho)=eta theta^(n-k) wedge S. Every term is a finite measure on the common compact support: z has a positive lower bound, V is smooth there, and the remaining weights are bounded continuous functions. At r=0 all displayed weights vanish. Thus (6.3) can be integrated without an improper-boundary convention.

Since z>0 and dd V is positive, the term -z dd V wedge beta_k wedge S in (6.1) is nonpositive. Formula (5.2) gives the coefficientwise positive-form inequality

    -dd beta_k+b_k^2 l^2 r^(l-2) eta theta^(n-k)
       <= c_k beta_(k-1),
    c_k=2l(l+1)/(l-1).                                   (6.4)

Indeed the left side equals
b_k l r^(l-1)theta^(n-k+1)
+b_k l((b_k-1)l+1)r^(l-2)eta theta^(n-k).
If k<n, its coefficients are 2l and 2l(l+1); the second agrees with c_k(l-1), and c_k>=2l. If k=n, its coefficients are l and l; both are bounded by the respective coefficients c_k and c_k(l-1), since l>=a+1>=5. Thus the SAME convenient upper bound c_k works in both cases. No false factor-two identity is used at the endpoint.

Combining (6.1)–(6.4) yields

    J(z) <= c_k ||z||_U J_(k-1)
                + integral (-V) r^l z^(-1) Gamma_Q(z).    (6.5)

No derivative-square expression for nonsmooth z has been used outside its already defined energy measure.

Now let u=u_k, let M=||u||_U, and first suppose M>0. Set z=exp(Bu), B>0. By (3.3) and positivity, the following current inequality holds ON U, where u>=-M:

    dd(zS) >= B exp(-BM) dd(uS)+z^(-1)Gamma_S(z).         (6.6)

The first summand of beta_k is r^l theta^(n-k); its second, when present, is positive. All beta_k coefficients vanish outside U, including on rho=0, so the inequality on U suffices for the full integral. Multiplying (6.6) by (-V)beta_k and using (4.4) gives

    B exp(-BM) J_k
        <= J(z)-integral (-V)r^l z^(-1)Gamma_Q(z).        (6.7)

The same energy integral appears in (6.5) and cancels. Since ||z||_U<=exp(BM),

    J_k <= c_k B^(-1) exp(2BM) J_(k-1).                  (6.8)

Choose B=1/(2M). Then

    J_k <= 4e l(l+1)/(l-1) M J_(k-1).                   (6.9)

If M=0, u is zero on U and dd(uS) is zero there by locality; beta_k vanishes outside U, so J_k=0 and (6.9) still holds. Iterating proves (1.2).

This proof is valid for the full CPsh sheaf. Smooth approximation of u_k on one fixed neighbourhood is not an intermediate assumption. Positivity and nonlinear energy identities came from the defining subsheaf closure and the independently established positive-current continuity lemma.

## 7. Polar limits: fixed weights first, then monotone convergence

Assume local smooth psh compact-sublevel neighbourhoods exist. Fix a point x and a locally approchable psh function V, locally integrable in the canonical sense. Shrink to an ordinary neighbourhood Y on which V is the decreasing limit of smooth psh functions V_p. Choose a barrier rho there so that K_delta is compact in Y and rho(x)<0. All continuous CPsh functions u_j are defined on Y and bounded near K_delta.

A single constant can be subtracted from the sequence V_p and V so that V_p<0 near K_delta for every p: the first smooth V_1 is bounded there and V_p<=V_1. Adding back that constant does not affect local integrability. This step is made BEFORE any estimate, and all smooth V_p are defined on the same neighbourhood of K_delta.

For fixed p apply (1.2) with k=n:

    integral r^(n+a)(-V_p) dd u_1 wedge ... wedge dd u_n
       <= C(n,a) product ||u_j||_U integral (-V_p) beta_0
       <= C(n,a) product ||u_j||_U integral (-V) beta_0.    (7.1)

The last quantity is finite and independent of p. Indeed beta_0 has compact continuous coefficients in fixed smooth charts and is dominated in absolute value by a finite sum of positive smooth compact top forms; local integrability of V gives this finite integral.

All C^2 coefficient approximations and energy-closure identities used to obtain the first inequality were performed with p FIXED. No estimate uniform in derivatives of V_p is needed: after that passage the final right side of (7.1) involves only the integral of -V against the ONE beta_0. Now let p tend to infinity. Monotone convergence for the positive Monge–Ampère measure gives (7.1) with V itself.

Since r^(n+a) is strictly positive on U, it has a positive lower bound on every compact subset of U. Thus V is locally integrable for dd u_1 wedge ... wedge dd u_n near x. In particular this measure gives zero mass to {V=-infinity}.

This is the required order of limiting operations. One first establishes the weighted estimate for each smooth polar truncation using the nonsmooth CPsh energy calculus, including its compact coefficient limit. Only afterwards is the monotone polar limit taken with the uniform bound (7.1). There is no simultaneous diagonal smoothing of all CPsh factors and no naive weak-limit preservation of null sets.

To treat m<n and an arbitrary smooth (n-m,n-m)-form alpha, first replace it by its symmetric part: the antisymmetric part pairs to zero with the symmetric product current. Work locally in an ordinary tropical presentation alpha=f^*omega, and localize near one compact test support. Put v=f^*||t||^2. This is a smooth psh function, and bounded coefficients on the compact tropical image give

    -C(dd v)^(n-m) <= alpha <= C(dd v)^(n-m).             (7.2)

The form inequality is first checked on the ambient affine chart and then pulled back; no full-rank assumption at every analytic point is needed. Apply the just proved n-factor result to u_1,...,u_m,v,...,v. Its positive measure dominates in total variation the signed trace with alpha, by (7.2). This includes m=0. For m=n, alpha is a smooth scalar, locally bounded, so the already proved n-factor integrability directly gives integrability for the total variation after multiplication by alpha. This proves (1.3). A finite partition on a compact support gives the general local statement.

## 8. Actual analytic barriers and analytic polar sets

Let now X be good, separated, strict and boundaryless, pure of dimension n over an arbitrary complete non-Archimedean field K. CLD's standing field convention explicitly includes trivial valuation. Strictness is understood in the source's convention; the usual strict class is a sufficient smaller class.

We give the barrier construction because the printed wording of CLD 16.9.1 cannot be copied literally as saying both rho<0 everywhere on its domain and {rho<=0} compact. The needed object is a smooth function on an ambient ordinary neighbourhood with a SMALLER relatively compact negative sublevel.

Given x and a prescribed ordinary neighbourhood, choose an affinoid neighbourhood A inside it and a rational affinoid neighbourhood W of x contained in Int(A). Write W as

    |f_i| <= lambda_i |g|  (1<=i<=s),

where f_i,g are analytic on A with no common zero and lambda_i>0. For mu>1 put W_mu={|f_i|<=mu lambda_i|g|}. Compactness of A and W_mu decreasing to W as mu decreases to 1 show that W_mu is contained in Int(A) for some mu>1. Indeed otherwise the nested compact sets W_mu intersected with the closed complement of Int(A) would have a point in W outside Int(A).

Every W_mu misses {g=0}, by the no-common-zero condition. On the ordinary open Y=Int(A) intersect {g!=0} define

    a_i=log(|f_i/g|/lambda_i),   a_0=-1.

The a_i may equal -infinity at zeros of f_i. Let t=log(mu)>0 and choose 0<epsilon<t/8. Take a smooth convex coordinatewise increasing regularized maximum M_epsilon with

    max(s_i)<=M_epsilon(s)<=max(s_i)+epsilon,

which ignores coordinates lying more than 2epsilon below the maximum. Such a function is obtained by convolving the maximum with an even product probability kernel supported in [-epsilon,epsilon] in each coordinate.

Set

    rho=M_epsilon(a_0,a_1,...,a_s)-t/2.

The constant branch a_0 is essential when all f_i vanish. Near any zero f_i=0 that coordinate is ignored, so the expression extends smoothly. Locally the remaining coordinates are logarithms of analytic units and the regularized maximum is convex; hence rho is smooth psh. At x all a_i<=0 and a_0<0, so rho(x)<=epsilon-t/2<0.

For delta=t/4 the closed sublevel {rho<=delta} lies in W_(exp(3t/4)), hence in W_mu and in Y. It is a closed subset of that compact rational domain, and is therefore compact. This is exactly the hypothesis of Section 1. The construction stays on the original K-space and uses arbitrary real rational-domain radii; it does not require a nontrivial value group.

If an abstract tropical space is only given the relatively compact negative-sublevel hypothesis of CLD 8.12.1, shift rho slightly upward while retaining rho(x)<0. A sufficiently small positive closed sublevel of the shifted function is then a closed subset of the old relatively compact negative sublevel. This supplies the K_delta form used above.

Finally let Z be a closed analytic subset of local dimension <n. Locally prime avoidance produces an analytic function f vanishing on Z but not identically on any n-dimensional component. Its zero set has dimension <n. Every compact ordinary smooth top form has support disjoint from that set by CLD 15.2.1(b); log|f| is bounded on this compact support, and hence canonically locally integrable, as in the proof of 16.9.4.

The stage-one assertion for this PARTICULAR pole can be made explicit. Let F be the convolution of max(t,0) with an even smooth probability kernel supported in [-1,1]. Then F is smooth convex, 0<=F'<=1, F=0 for t<=-1, and F=t for t>=1. Put F_p(t)=-p+F(t+p). The smooth functions F_p(log|f|), extended by the constant -p where f=0, are psh: they are constant on an ordinary neighbourhood of every zero, and elsewhere are convex functions of the analytic log-unit. Since the derivative with respect to p is -1+F'(t+p)<=0, they decrease to log|f|, also at its poles. Thus log|f| is locally approchable without taking a limit of successive approximation stages. Apply Section 7 with this V. Its polar set contains Z, proving zero total-variation mass on Z for the general-CPsh product trace.

## 9. Relation to component curvature and exact exclusions

The preceding polar conclusion, IF independently accepted, supplies the common-curvature nullity hypothesis in the separately frozen source audit p213_polar_nullity_source_audit_20260901/SOURCE_AUDIT.md, SHA256 4b5818d69ee5fa319d15d42dfdef61b839bc32f78ad689f3714266d524ec7e97. Its elementary positive-weighted-sum argument then excludes componentwise curvature cancellation for two general continuous CPsh potentials with equal ambient curvature, over the original field and including generic nonreduced multiplicities.

This implication does not by itself classify all positive closed (0,0)-currents, and does not prove full P21.3 for arbitrary bidegree. Any use of a scalar-current classification must retain that separate theorem's field, dimension and ordinary-domain hypotheses.

No regularization theorem collapsing CPsh to its first stage is proved. The new bound instead bypasses that requirement. No polar conclusion for discontinuous u_j, for arbitrary positive currents with unknown potentials, or for spaces lacking the stated local barrier condition is claimed.

Root suggested checking the dpsh energy route, supplied boundary cautions for V and the barrier wording, and independently discussed the algebra. The present author wrote this complete proof. Therefore root's review is not the sole fresh independent review; a new exact-final auditor is required before mathematical acceptance. The source audit is a source/scope document, not an independent verdict on this subsequent authored proof.
