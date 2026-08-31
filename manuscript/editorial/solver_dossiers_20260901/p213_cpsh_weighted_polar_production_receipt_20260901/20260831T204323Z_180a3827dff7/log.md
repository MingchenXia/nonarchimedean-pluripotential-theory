started_at_utc: 2026-08-31T20:43:23.831883+00:00
command: /Applications/ChatGPT.app/Contents/Resources/codex exec -C /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification -m gpt-5.6-sol --sandbox workspace-write --config 'approval_policy="never"' --config 'model_reasoning_effort="xhigh"' --config sandbox_workspace_write.network_access=false --config 'mcp_servers.verification_agent.command="/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python"' --config 'mcp_servers.verification_agent.cwd="/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification"' 'Run_id: 20260831T204323Z_180a3827dff7. Statement: ## 1. Scope, notation, and the proposed conclusion

Let X be a boundaryless, locally differentially separated tropical space of level n>=1 in the sense of CLD, with its canonical positive closed integration current delta_X. All sheaves, ordinary smooth forms, positivity and compact-test topologies are those of CLD. Local differential separation supplies the compact smooth partitions, positive test majorants and Radon-measure interpretation used below (CLD 6.5.2 and 7.2.4–7.2.12). The analytic spaces in Section 8 have this property by CLD 15.2.4. Write dd=d'"'"'d'"'"''"'"'. The symbol CPsh means the least subsheaf of real continuous functions containing smooth psh functions and stable under local uniform closure (CLD 8.1.7–8.1.8), NOT merely the first locally approchable stage.

The elementary calculus input consists of CLD 8.5.1, 8.5.5, 8.7.2 and 8.8.4–8.8.5: positivity of dd(uS) for continuous CPsh u and positive closed S, continuity with uniformly converging continuous coefficients and positive currents, and the dpsh extension. The required convex composition is proved directly from CPsh minimality in Section 2; the proof does not need to identify every current-positive continuous function with CPsh or collapse its hierarchy. None of these inputs is the weighted polar estimate to be proved.

Here is the fixed-neighbourhood weighted assertion. Let Y be an ordinary open in X, let rho be smooth psh on Y, and suppose for some delta>0 that

    K_delta={rho<=delta} is compact in Y,
    U={rho<0} is nonempty.

All functions u_1,...,u_k are CPsh on a neighbourhood of K_delta, and V is a SMOOTH psh function on a neighbourhood of K_delta, negative on U. In particular V has no uncontrolled boundary singularity at closure(U). Set r=max(-rho,0), theta=dd rho, eta=d'"'"'rho wedge d'"'"''"'"'rho. Fix an integer a>=4. For 0<=k<=n put

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

. Proof:
## 1. Scope, notation, and the proposed conclusion

Let X be a boundaryless, locally differentially separated tropical space of level n>=1 in the sense of CLD, with its canonical positive closed integration current delta_X. All sheaves, ordinary smooth forms, positivity and compact-test topologies are those of CLD. Local differential separation supplies the compact smooth partitions, positive test majorants and Radon-measure interpretation used below (CLD 6.5.2 and 7.2.4–7.2.12). The analytic spaces in Section 8 have this property by CLD 15.2.4. Write dd=d'"'"'d'"'"''"'"'. The symbol CPsh means the least subsheaf of real continuous functions containing smooth psh functions and stable under local uniform closure (CLD 8.1.7–8.1.8), NOT merely the first locally approchable stage.

The elementary calculus input consists of CLD 8.5.1, 8.5.5, 8.7.2 and 8.8.4–8.8.5: positivity of dd(uS) for continuous CPsh u and positive closed S, continuity with uniformly converging continuous coefficients and positive currents, and the dpsh extension. The required convex composition is proved directly from CPsh minimality in Section 2; the proof does not need to identify every current-positive continuous function with CPsh or collapse its hierarchy. None of these inputs is the weighted polar estimate to be proved.

Here is the fixed-neighbourhood weighted assertion. Let Y be an ordinary open in X, let rho be smooth psh on Y, and suppose for some delta>0 that

    K_delta={rho<=delta} is compact in Y,
    U={rho<0} is nonempty.

All functions u_1,...,u_k are CPsh on a neighbourhood of K_delta, and V is a SMOOTH psh function on a neighbourhood of K_delta, negative on U. In particular V has no uncontrolled boundary singularity at closure(U). Set r=max(-rho,0), theta=dd rho, eta=d'"'"'rho wedge d'"'"''"'"'rho. Fix an integer a>=4. For 0<=k<=n put

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

We first record the needed composition fact directly from the definition. If F:R->R is smooth, convex and nondecreasing, the CPsh functions u for which F(u) is CPsh form a subsheaf stable under uniform limits. Local uniform convergence is preserved by F because the functions have uniformly bounded images near each compact support. The class contains every smooth psh u by the ordinary smooth chain rule, so it is all of CPsh. Addition and nonnegative scalar multiplication follow by the same separate-variable closure argument starting with smooth psh functions. For squares on a positive range, use a globally smooth convex nondecreasing F equal to t^2 for t>=1/2: for instance prescribe F'"'"'(t)=2t chi(t) for t>=0, zero for t<=0, with chi a smooth nondecreasing cutoff from zero near 0 to one for t>=1/2, and choose the additive constant to match t^2 on that range. Thus no appeal to a broader Psh/CPsh equivalence is needed for either squares or exponentials below.

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
       = [d'"'"'h wedge d'"'"''"'"'l+d'"'"'l wedge d'"'"''"'"'h] wedge S/2.        (2.5)

For h=l this is the strongly positive (1,1)-form d'"'"'h wedge d'"'"''"'"'h multiplied by S.

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

    d'"'"'(hQ) wedge d'"'"''"'"'rho = Gamma_Q(h,rho)                  (4.3)

in top degree. Initially the left side is merely a distribution. For smooth h the two cross terms in (2.5) have the same top-degree pairing with symmetric Q; their difference is antisymmetric, as in the ordinary symmetry calculation used in CLD 8.5.3. Thus (4.3) holds for smooth h.

For fixed smooth rho, both sides of (4.3) are continuous under the CPsh uniform closures: the left by distributional continuity of hQ and its first derivative, the right by (2.4), using a fixed local dpsh decomposition of rho, available by CLD 8.8.1. The same minimal-subsheaf argument proves it first for CPsh h and then by linearity for dpsh h. Therefore the mixed distribution is indeed the signed Radon measure in (4.3). Multiplication by a fixed smooth weight is now legitimate on either description.

For a smooth closed form theta, the defining formulas also show

    Gamma_(theta^j wedge S)(h,l)
       =theta^j wedge Gamma_S(h,l).                      (4.4)

We shall use this only when theta is positive, so the relevant Q is positive closed.

## 5. Compact C^2 barrier forms and integration by parts

Return to the fixed data of Section 1. Put l=k+a for 1<=k<=n, and put b_k=2 when k<n and b_n=1. The functions r^b=max(-rho,0)^b with integer b>=3 are C^2 in each smooth tropical presentation. Formula (1.1) therefore defines compactly supported C^2 forms, with support contained in closure(U), a compact subset of Y. Both theta and eta are positive, so beta_k is positive.

The exact identities on U are

    d'"'"''"'"' beta_k = -b_k l r^(l-1) d'"'"''"'"'rho theta^(n-k),        (5.1)
    dd beta_k = b_k l[-r^(l-1) theta^(n-k+1)
                       +(l-1)r^(l-2) eta theta^(n-k)].    (5.2)

For k<n both summands in beta_k contribute to d'"'"''"'"' beta_k, and give the factor two. For k=n, beta_n=r^(n+a) is a SCALAR and has only its first summand: its derivatives have the factor one. These surviving scalar derivatives cannot be discarded on degree grounds. This corrects an endpoint factor in the analogous printed source calculation. Both formulas extend across rho=0 with the required finite regularity: the powers appearing in derivatives vanish there, and no boundary delta term occurs.

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
                      +2 integral V d'"'"'(zS) wedge d'"'"''"'"'beta_k.    (6.1)

One can verify the sign first by expanding dd(-V beta_k) and applying Stokes to d'"'"'(z V d'"'"''"'"'beta_k wedge S); Section 5 permits the C^2 passage. Symmetry combines the two cross terms. Formula (4.3) and (5.1) identify the last term with

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

Let now X be good, separated, strict and boundaryless, pure of dimension n over an arbitrary complete non-Archimedean field K. CLD'"'"'s standing field convention explicitly includes trivial valuation. Strictness is understood in the source'"'"'s convention; the usual strict class is a sufficient smaller class.

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

The stage-one assertion for this PARTICULAR pole can be made explicit. Let F be the convolution of max(t,0) with an even smooth probability kernel supported in [-1,1]. Then F is smooth convex, 0<=F'"'"'<=1, F=0 for t<=-1, and F=t for t>=1. Put F_p(t)=-p+F(t+p). The smooth functions F_p(log|f|), extended by the constant -p where f=0, are psh: they are constant on an ordinary neighbourhood of every zero, and elsewhere are convex functions of the analytic log-unit. Since the derivative with respect to p is -1+F'"'"'(t+p)<=0, they decrease to log|f|, also at its poles. Thus log|f| is locally approchable without taking a limit of successive approximation stages. Apply Section 7 with this V. Its polar set contains Z, proving zero total-variation mass on Z for the general-CPsh product trace.



Use AGENTS.md to verify the above proof for the statement.'

Reading additional input from stdin...
2026-08-31T20:43:24.033486Z  WARN codex_skills::interface: ignoring interface.icon_small: icon path with '..' must resolve under plugin assets/
2026-08-31T20:43:24.033517Z  WARN codex_skills::interface: ignoring interface.icon_large: icon path with '..' must resolve under plugin assets/
OpenAI Codex v0.151.0-alpha.7.2
--------
workdir: /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
model: gpt-5.6-sol
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: none
session id: 01a0598f-fdde-7be1-b3d9-6cf4e6668433
--------
user
Run_id: 20260831T204323Z_180a3827dff7. Statement: ## 1. Scope, notation, and the proposed conclusion

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

. Proof:
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



Use AGENTS.md to verify the above proof for the statement.
2026-08-31T20:43:24.946392Z  WARN codex_skills::interface: ignoring interface.icon_small: icon path with '..' must resolve under plugin assets/
2026-08-31T20:43:24.946422Z  WARN codex_skills::interface: ignoring interface.icon_large: icon path with '..' must resolve under plugin assets/
warning: Exceeded skills context budget. All skill descriptions were removed and 48 additional skills were not included in the model-visible skills list.
codex
I’ll verify the proof in order, check the cited CLD results against their exact hypotheses, and write the required verdict file. I’m using `verify-sequential-statements`, then `check-referenced-statements`, then `synthesize-verification-report`.
exec
/bin/zsh -lc 'cat .agents/skills/verify-sequential-statements/SKILL.md .agents/skills/check-referenced-statements/SKILL.md .agents/skills/synthesize-verification-report/SKILL.md' in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:
---
name: verify-sequential-statements
description: Verify a markdown proof in the order it is written. Use when the task is to check local correctness, theorem applicability, and reasoning gaps statement by statement through a paper-style proof.
---

# Verify Sequential Statements

Check each statement and subproof in order and log all local issues.

## Input Contract

Assume:

- `Proof` is markdown text.
- The proof is written in good mathematical order.
- `Statement` contains the target theorem statement and its hypotheses.

Do not split the proof with utility code. Read the markdown in order and use its own structure.

## Procedure

1. Extract the assumptions and hypotheses from `Statement` before checking the proof.
2. Iterate through the statements/subproofs in the order they appear in the markdown.
3. For each item, determine a location key:
   - use the displayed theorem/lemma/claim heading if present,
   - otherwise use a local textual locator such as `proof paragraph 2`.
4. Check local reasoning:
   - Is the inference valid?
   - Are assumptions stated and sufficient?
   - Is each theorem application valid in context?
   - Are there skipped or hand-wavy steps?
   - Do similar-looking definitions actually match exactly?
   - Do similar-looking formulas in those definitions differ in a way that matters for the argument?
   - If the proof deduces one property from another, do the exact definitions and defining formulas of those two properties really support that deduction?
   - For each small deduction step, do all assumptions needed for that step actually hold?
5. Pay special attention to assumptions that an object exists or satisfies a property. Sometimes such an object has not been constructed, or it exists but has not been proved to satisfy the claimed property.
6. Audit whether the assumptions from `Statement` are actually used in the proof.
7. If some assumptions seem unused, do not assume they are harmless. Reason carefully about whether:
   - the assumption is truly redundant, or
   - the proof is silently omitting a necessary use of it and therefore has a gap or error.
8. Classify findings:
   - `critical_error`: logical contradiction, invalid theorem use, false implication.
   - `gap`: missing derivation, vague justification, unsupported step, unjustified existence or property assumptions about objects, suspiciously unused assumptions whose role is not justified, failure to distinguish between similar-looking definitions or formulas, or a hand-wavy deduction from one property to another.
9. Persist each checked item to `statement_checks` using `memory_append`.

## Output Contract

Append records to `statement_checks` with structure like:

```json
{
  "location": "Lemma 3",
  "status": "checked",
  "critical_errors": [
    {"location": "Lemma 3", "issue": "Incorrect implication from A to B."}
  ],
  "gaps": [
    {"location": "Lemma 3", "issue": "Missing justification of boundedness."}
  ]
}
```

## MCP Tools

- `memory_append`
- `memory_query`
---
name: check-referenced-statements
description: Validate externally referenced theorems by querying arXiv theorem search first and Codex's built-in web search second. Use when a markdown proof cites statements from external papers.
---

# Check Referenced Statements

Validate every external-paper reference used in the proof.

## Input Contract

For each cited external theorem/lemma/definition:

- location where it is used,
- the full referenced statement text.

## Procedure

1. Query `search_arxiv_theorems` using the full referenced statement as `query`.
2. Inspect returned results and compare theorem text directly to the referenced statement in reasoning.
3. Expand the definitions and terminology appearing in the cited statement using the cited paper's context before deciding whether the theorem applies.
4. Check whether the same words in the current proof mean the same thing as they do in the cited paper. In mathematics, identical words can carry different definitions in different contexts.
5. Distinguish similar-looking definitions and compare their exact formulas, notation, and quantifiers. Do not collapse two definitions just because the names or formulas look close.
6. Accept as matched and applicable only when both are true:
   - the result clearly corresponds to the cited statement,
   - the contextual definitions and hypotheses align with the current problem.
7. If the proof uses the referenced statement to obtain further conclusions, verify the transition from the referenced statement to those conclusions.
8. Treat a hand-wavy specialization, instantiation, or downstream deduction as a gap even when the cited theorem itself is valid.
9. Treat a logically invalid transition from the cited theorem to the claimed conclusion as a critical error.
10. If that downstream step deduces one property from another, compare the exact definitions and defining formulas of both properties before accepting the deduction.
11. If the theorem exists but the current proof uses different definitions, hypotheses, ambient objects, or a subtly different defining formula, record a critical error for incorrect application.
12. If no match is found, use Codex's built-in web search with the same statement text.
13. If still not found, emit a critical error:
   - location: where the citation is used,
   - issue: referenced theorem appears non-existent or incorrectly cited.
14. Persist each reference check in `reference_checks`.

Do not rely on dedicated comparison utility code; perform comparison through careful reasoning.

## Output Contract

Append records to `reference_checks` like:

```json
{
  "location": "Lemma 2",
  "referenced_statement": "Exact statement text",
  "context_expansion": "In the cited paper, 'regular' means regular with respect to the valuation topology.",
  "arxiv_match_found": false,
  "web_match_found": false,
  "critical_error": {
    "location": "Lemma 2",
    "issue": "Referenced external theorem was not found in arXiv search or Codex built-in web search."
  }
}
```

## Tools

- `search_arxiv_theorems`
- `memory_append`
- Codex's built-in web search
---
name: synthesize-verification-report
description: Aggregate all detected errors and gaps into the final verification report, apply strict accept/reject logic, and produce repair hints when rejected.
---

# Synthesize Verification Report

Produce the final verification output JSON and verdict.

## Input Contract

Read all findings from:

- `statement_checks`
- `reference_checks`

Each issue must include `location` and `issue`.

## Procedure

1. Collect all critical errors and all gaps from previous checks.
2. Build a complete `verification_report` object with:
   - `summary`
   - `critical_errors`
   - `gaps`
3. Apply strict verdict rule:
   - `correct` iff `critical_errors=[]` and `gaps=[]`.
   - otherwise `wrong`.
4. If verdict is `wrong`, produce concrete non-empty `repair_hints`.
5. Validate the output via `validate_verification_output`.
6. Persist output via `write_verification_output`.

## Output Contract

Final output JSON:

```json
{
  "verification_report": {
    "summary": "string",
    "critical_errors": [],
    "gaps": []
  },
  "verdict": "correct",
  "repair_hints": ""
}
```

If there is any error or gap, verdict must be `"wrong"` and `repair_hints` must be non-empty.

## MCP Tools

- `memory_query`
- `memory_append`
- `validate_verification_output`
- `write_verification_output`

exec
/bin/zsh -lc "pwd && rg --files -g 'AGENTS.md' -g '*memory*' -g '*verification*' -g '*arxiv*' -g 'SKILL.md' -g 'README*' -g 'server.py' -g 'pyproject.toml' -g 'requirements*' -g '*cld*' -g '*CLD*' -g '"'!tmp/verification-venv/**'"' -g '"'!results/**'"' -g '"'!memory/**'"'" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:
/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
requirements.txt
AGENTS.md
api/requirements.txt
api/server.py
schemas/verification_output.schema.json
mcp/requirements.txt
mcp/server.py
tmp/arxiv_0912.5220.pdf
tmp/20260828T043230Z_6476f760173b_arxiv_theorem_search.json
tmp/arxiv_1810.04662.pdf
tmp/write_verification_20260830T084832Z_5ba8ac5123a5.py
tmp/1204.6277v2-cld-src.tar
tmp/cld.txt
tmp/P10_20260831T104106Z_fbf006f74b68/verification_payload_final.json
tmp/P10_20260831T104106Z_fbf006f74b68/verification_payload.json
tmp/1204.6277v2-cld.pdf
tmp/20260831T193139Z_249bb54aa321/verification_payload.json
tmp/write_20260828_9e611f_verification.py
tmp/20260827T102704Z_7d83478aafc9_audit_memory_records.json
tmp/1204.6277v2-cld.txt
tmp/20260831T103522Z_af92c16fb79b/verification_payload.json
tmp/query_20260830T023734Z_298d547e11c5_memory.py
tmp/arxiv_20260830T052905Z_ed52db88f947.py
tmp/report_memory_20260830T054245Z_0b014db9e73a.json
tmp/arxiv_1810.04662.txt
tmp/query_20260830T013214Z_9d4620324f74_memory.py
tmp/query_memory_20260830T093752Z_2349768060ac.py
tmp/query_20260830T023911Z_b71556260146_memory.py
tmp/20260831T143728Z_5c9ad14a90f6/verification_payload.json
tmp/finalize_verification_20260830T121753Z_b42ef4d2f2f8.py
tmp/p031_eff46514/arxiv_search_results.json
tmp/20260830T000134Z_08943b803418_verification.json
tmp/20260831T182212Z_60cc46cdfc59/arxiv-search.json
tmp/20260831T102727Z_7394e9ef20df/arxiv_search_results.json
tmp/arxiv_0912.5220.txt
tmp/20260829T225739Z_622f19a1d2bc_arxiv_theorem_search.json
tmp/20260830T000537Z_d3105e8390f5_verification.json
tmp/P14_20260831T120130Z_2491fd2568aa/verification_payload.json
tmp/query_20260830T072452Z_861421d00a4d_memory.py
tmp/query_20260830T042801Z_dcbcf1b63eb1_memory.py
tmp/20260830T000537Z_d3105e8390f5_verification_report_record.json
tmp/arxiv_20260831T103336Z_a8e40db347b2.json
tmp/20260828T054645Z_0280ba1c62e7_arxiv_theorem_search.json
tmp/20260827T102704Z_7d83478aafc9_verification_payload.json
tmp/20260831T105640Z_18a867409dfa/R11_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R05_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R19_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R08_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R14_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R13_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R02_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R07_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R21_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R16_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R04_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R18_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R09_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R15_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R22_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R10_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R01_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R06_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R20_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R17_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R12_arxiv.json
tmp/20260831T105640Z_18a867409dfa/R03_arxiv.json
tmp/pdfs/20260831T112711Z_b86bf0eae113/verification_payload.json
tmp/pdfs/popovici-iwasawa-arxiv.pdf
tmp/pdfs/20260831T025059Z_c4939835ee62/arxiv_search_results.json
tmp/pdfs/popovici-iwasawa-arxiv.txt
tmp/pdfs/20260831T172728Z_60613f09e266/chen-arxiv-application-14.png
tmp/pdfs/20260831T172728Z_60613f09e266/chen-arxiv-application-13.png
tmp/pdfs/20260831T172728Z_60613f09e266/arxiv.txt
tmp/pdfs/20260831T172728Z_60613f09e266/chen-arxiv-bib.png
tmp/pdfs/20260831T172728Z_60613f09e266/chen-arxiv-p6.png
tmp/pdfs/p041_abb28116/arxiv_search_results.json
tmp/pdfs/20260831T112714Z_e6afd5e54ed0/verification_payload.json
tmp/pdfs/20260831T153754Z_f86897a37640/R26_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R11_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R32_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R05_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R19_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R08_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R14_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R23_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R13_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R24_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R29_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R35_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R02_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R07_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R30_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R21_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R16_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R33_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R04_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R18_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R09_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R15_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R22_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R27_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R10_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R01_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R36_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R06_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R31_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R20_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R17_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R12_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R25_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R28_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R34_arxiv.json
tmp/pdfs/20260831T153754Z_f86897a37640/R03_arxiv.json

mcp: verification_agent/memory_init started
mcp: verification_agent/memory_init (failed)
MCP tool call requires approval, but approval policy is never
exec
/bin/zsh -lc "cat AGENTS.md && sed -n '1,240p' mcp/server.py && rg -n '8\\.1\\.7|8\\.5\\.1|8\\.5\\.5|8\\.7\\.2|8\\.8\\.1|8\\.8\\.4|8\\.8\\.5|15\\.2\\.1|15\\.2\\.4|16\\.9\\.1|16\\.9\\.4|8\\.4\\.3|7\\.2\\.4' tmp/1204.6277v2-cld.txt" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:
# Proof Verification Agent

## Relocated local runtime

This checkout is local under `/Users/mingchen/Projects/Yethlas`. For every
Python command used to call `mcp.server`, memory functions, or verification
helpers, use the following interpreter explicitly:

`/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python`

Do not call bare `python` or `python3`: those resolve outside the verification
environment and do not contain the required `requests` and MCP packages.

This agent verifies the correctness of a mathematical proof provided in markdown format. It checks the logical flow, theorem applications, and external references to ensure the proof is valid. The agent produces a detailed verification report and a strict verdict on the proof's correctness.

## Objective

Given:

- `Run_id: <run_id>`
- `Statement: <informal theorem statement>`
- `Proof: <proof>`

verify whether the proof is correct and output:

- `results/{run_id}/verification.json`

with JSON fields:

- `verification_report`
- `verdict` (`"correct"` or `"wrong"`)
- `repair_hints`

## Input Contract

Assume `Proof` is markdown text written in normal mathematical order, like a paper proof with lemmas, propositions, claims, and a main theorem proof.

- Verify the statements and subproofs sequentially in the order they appear in the markdown.
- Split each statement's proof into every small deduction step and check the correctness of these steps one by one.
- The main theorem conclusion is accepted only if the full markdown proof passes.


## Required Skills

Use these skills in this order:

1. `$verify-sequential-statements`
2. `$check-referenced-statements`
3. `$synthesize-verification-report`


## Memory Policy

Initialize memory first:

- `memory_init(run_id, meta={"statement": ..., "input_shape": "proof_markdown_text"})`

Then persist artifacts in channels:

- `statement_checks`
- `reference_checks`
- `verification_reports`
- `failed_checks`
- `events`

Every detected issue must be persisted before final verdict.

## Verification Workflow

### Step 1: Initialize run context

1. Read `Run_id`, `Statement`, `Proof`.
2. Treat `Proof` as markdown text and read it in the order written.
3. Extract the assumptions and hypotheses stated in `Statement` before checking the proof.
4. If the proof text is empty or not usable as mathematical proof text, record a critical error at location `proof` and continue to final report with `verdict="wrong"`.

### Step 2: Sequential proof-item verification

For each statement/subproof in the markdown, in textual order:

1. Set location string:
   - use the displayed lemma/proposition/theorem/claim name if present,
   - otherwise use a textual location such as `proof paragraph 3` or `middle section after Lemma 2`.
2. Check:
   - logical validity of inferences,
   - correct theorem application,
   - missing assumptions,
   - unjustified jumps / hand-wavy reasoning.
   - whether similar-looking definitions are actually the same definition,
   - whether similar-looking formulas in those definitions are in fact identical or differ in a way that matters,
   - whenever the proof deduces one property from another, whether the exact definitions and defining formulas of those two properties really justify the deduction,
   - for every small deduction step, whether all assumptions needed for that step actually hold.
3. Pay special attention to assumptions saying that an object exists or satisfies some property. Do not assume such an object exists or has the claimed property unless it has been constructed, cited, or proved in the current context.
4. Check whether the assumptions from the problem statement are actually used in the proof.
5. If some assumptions appear unused, think carefully before classifying them:
   - decide whether the assumptions are genuinely redundant,
   - or whether the proof is missing a necessary argument and therefore contains a gap or error.
6. Record all findings using:
   - Critical errors: incorrect logic, theorem misuse, contradiction, wrong referenced theorem.
   - Gaps: skipped derivations, vague arguments, missing intermediate justification, unjustified existence or property assumptions about objects, suspiciously unused assumptions whose role is not justified, or hand-wavy deductions from one property to another without checking the exact definitions.
7. Append structured records to `statement_checks`.

### Step 3: External reference checking

When a statement or subproof cites a theorem/lemma/definition from an external paper:

1. Query `search_arxiv_theorems` with the full referenced statement text.
2. Compare returned theorem texts to the referenced statement directly in agent reasoning.
3. Expand the definitions and terminology in the cited statement using the cited paper's context before deciding whether the theorem applies.
4. Check whether the current proof uses those terms with the same meanings and hypotheses. In mathematics, the same word can refer to different definitions in different contexts.
5. Distinguish similar-looking definitions and compare their exact formulas, notation, and quantifiers. Do not treat two definitions as interchangeable just because their names or displayed formulas look close.
6. Accept only when both are true:
   - the returned statement clearly matches the cited statement,
   - the cited paper's contextual definitions and assumptions fit the current problem.
7. If the proof uses the referenced statement to obtain further conclusions, check the transition from the referenced statement to those conclusions. Do not accept a citation as sufficient if the proof hand-waves the specialization, instantiation, or intermediate deductions.
8. If that transition is vague, missing, or unsupported, record a gap; if the transition is logically invalid, record a critical error.
9. If the theorem exists but is used with mismatched definitions, assumptions, ambient context, or a subtly different formula in the definition, add a critical error for incorrect application.
10. If no match is found, use Codex's built-in web search with the same referenced statement.
11. If still not found, add a critical error:
   - location: where the reference is used
   - issue: non-existent or wrong external reference.
12. Append details to `reference_checks`.


### Step 4: Build verification report

Aggregate every error and gap across the full markdown proof.

`verification_report` must include:

- `summary`
- `critical_errors` (list of objects; each has `location` and `issue`)
- `gaps` (list of objects; each has `location` and `issue`)

Do not drop any finding.

### Step 5: Verdict rule and repair hints

Verdict rule is strict:

- Return `"correct"` if and only if both `critical_errors` and `gaps` are empty.
- Otherwise return `"wrong"`.

Repair hints:

- If verdict is `"correct"`, set `"repair_hints": ""`.
- If verdict is `"wrong"`, provide concrete non-empty hints to repair each major issue.

### Step 6: Output write and completion

Write final JSON using:

- `write_verification_output(run_id, payload)`

Target file must be:

- `results/{run_id}/verification.json`

Stop only after this file is written successfully.

## Output JSON Contract

The final response and file content must be:

```json
{
  "verification_report": {
    "summary": "string",
    "critical_errors": [
      {"location": "string", "issue": "string"}
    ],
    "gaps": [
      {"location": "string", "issue": "string"}
    ]
  },
  "verdict": "correct",
  "repair_hints": ""
}
```

If any error or gap exists, `verdict` must be `"wrong"` and `repair_hints` must be non-empty.

## Hard Invariants

1. Verify the markdown proof in textual order.
2. Include every critical error and every gap in the report.
3. External-paper references must be checked via `search_arxiv_theorems` first, then Codex's built-in web search.
4. Accept iff there are zero errors and zero gaps.
5. Persist final JSON to `results/{run_id}/verification.json`.
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import requests

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - dependency managed by requirements
    Draft202012Validator = None  # type: ignore[assignment]

try:
    from fastmcp import FastMCP
except ImportError:  # pragma: no cover - dependency managed by requirements
    FastMCP = None  # type: ignore[assignment]


REPO_ROOT = Path(__file__).resolve().parents[1]
MEMORY_ROOT = REPO_ROOT / "memory"
RESULTS_ROOT = REPO_ROOT / "results"
SCHEMA_PATH = REPO_ROOT / "schemas" / "verification_output.schema.json"

THEOREM_SEARCH_URL = "https://leansearch.net/thm/search"
THEOREM_SEARCH_TASK = (
    "Given a math statement, retrieve useful references, such as theorems, "
    "lemmas, and definitions, that are useful for solving the given problem."
)

CHANNEL_FILES: Dict[str, str] = {
    "statement_checks": "statement_checks.jsonl",
    "reference_checks": "reference_checks.jsonl",
    "verification_reports": "verification_reports.jsonl",
    "failed_checks": "failed_checks.jsonl",
    "events": "events.jsonl",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sanitize_run_id(raw: str) -> str:
    cleaned = re.sub(r"\s+", "_", str(raw).strip())
    cleaned = re.sub(r"[^A-Za-z0-9._-]", "_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("._")
    return cleaned or "run"


def _run_dir(run_id: str) -> Path:
    return MEMORY_ROOT / sanitize_run_id(run_id)


def _channel_path(run_id: str, channel: str) -> Path:
    if channel not in CHANNEL_FILES:
        allowed = ", ".join(sorted(CHANNEL_FILES))
        raise ValueError(f"Unknown channel '{channel}'. Allowed channels: {allowed}")
    return _run_dir(run_id) / CHANNEL_FILES[channel]


def _append_jsonl(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def _iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    if not path.exists():
        return
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(payload, dict):
                yield payload


def search_arxiv_theorems(
    query: str,
    num_results: int = 10,
    endpoint: str = THEOREM_SEARCH_URL,
    timeout_seconds: int = 30,
) -> Dict[str, Any]:
    if not query.strip():
        raise ValueError("query must be non-empty")
    if num_results <= 0:
        raise ValueError("num_results must be > 0")

    payload = {
        "query": query,
        "task": THEOREM_SEARCH_TASK,
        "num_results": num_results,
    }

    response = requests.post(endpoint, json=payload, timeout=timeout_seconds)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, list):
        raise ValueError("The theorem endpoint must return a JSON list")

    normalized: List[Dict[str, str]] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        normalized.append(
            {
                "title": str(item.get("title", "")),
                "theorem": str(item.get("theorem", "")),
                "arxiv_id": str(item.get("arxiv_id", "")),
                "theorem_id": str(item.get("theorem_id", "")),
            }
        )

    return {
        "query": query,
        "count": len(normalized),
        "results": normalized,
        "endpoint": endpoint,
    }


def memory_init(run_id: str, meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    sanitized_run_id = sanitize_run_id(run_id)
    run_dir = _run_dir(sanitized_run_id)
    run_dir.mkdir(parents=True, exist_ok=True)

    created_files: Dict[str, str] = {}
    for channel, filename in CHANNEL_FILES.items():
        channel_path = run_dir / filename
        channel_path.touch(exist_ok=True)
        created_files[channel] = str(channel_path)

    meta_path = run_dir / "meta.json"
    existing_meta: Dict[str, Any] = {}
    if meta_path.exists() and meta_path.stat().st_size > 0:
        with meta_path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
            if isinstance(loaded, dict):
                existing_meta = loaded

    merged_meta: Dict[str, Any] = {
        "run_id": sanitized_run_id,
        "created_at_utc": existing_meta.get("created_at_utc", _utc_now()),
        "updated_at_utc": _utc_now(),
    }
    merged_meta.update(existing_meta)
    if meta:
        merged_meta.update(meta)

    with meta_path.open("w", encoding="utf-8") as handle:
        json.dump(merged_meta, handle, indent=2, ensure_ascii=False)

    return {
        "run_id": sanitized_run_id,
        "memory_dir": str(run_dir),
        "meta_path": str(meta_path),
        "channels": created_files,
    }


def memory_append(run_id: str, channel: str, record: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(record, dict):
        raise ValueError("record must be a JSON object")

    resolved_run_id = sanitize_run_id(run_id)
    memory_init(resolved_run_id)

    entry = {
        "timestamp_utc": _utc_now(),
        "channel": channel,
        "record": record,
    }
    target = _channel_path(resolved_run_id, channel)
    _append_jsonl(target, entry)

    if channel != "events":
        _append_jsonl(
            _channel_path(resolved_run_id, "events"),
            {
                "timestamp_utc": _utc_now(),
                "event_type": "memory_append",
                "channel": channel,
            },
        )

    return {
        "status": "ok",
        "run_id": resolved_run_id,
        "channel": channel,
        "path": str(target),
        "entry": entry,
    }


def memory_query(
    run_id: str,
    channel: str,
    filters: Optional[Dict[str, Any]] = None,
    contains: Optional[str] = None,
    limit: int = 100,
    reverse: bool = True,
) -> Dict[str, Any]:
    if limit <= 0:
        raise ValueError("limit must be > 0")

    resolved_run_id = sanitize_run_id(run_id)
    path = _channel_path(resolved_run_id, channel)
    items = list(_iter_jsonl(path))

    if filters:
        filtered: List[Dict[str, Any]] = []
        for item in items:
            if all(item.get(key) == value for key, value in filters.items()):
                filtered.append(item)
        items = filtered

    if contains:
        needle = contains.lower()
        items = [item for item in items if needle in json.dumps(item, ensure_ascii=False).lower()]

    if reverse:
        items = list(reversed(items))

    items = items[:limit]
    return {
        "run_id": resolved_run_id,
        "channel": channel,
        "count": len(items),
        "items": items,
    }


6202:proposition 12.4.7) et localement différentiellement séparé (corollaire 15.2.4).
7927:Lemme 7.2.4. — Supposons que l’espace tropical X soit localement différentiellement
9791:Définition 8.1.7. — On note CPshX le plus petit sous-faisceau du faisceau CX des
10132:Proposition 8.4.3. — On suppose a ⩾ 3 et on pose C(k, a) = (4e)k a−1 (k + a)(2 +
10252:Lemme 8.5.1. — Soit (Tn ) une suite de courants positifs et soit (un ) une suite de
10312:Lemme 8.5.5. — Soit T un courant de bidegré (p, p) sur X, positif et fermé. Pour
10384:d′ d′′ (uT ) = lim d′ d′′ (uTk ) (lemme 8.5.1). Il en résulte que T est un courant de Bedford–
10402:(lemme 8.5.1). Par suite, P contient le faisceau des fonctions psh. En particulier, le
10410:Compte tenu du lemme 8.5.5, on définit par récurrence un courant positif fermé
10427:Proposition 8.7.2. — Soit (Tk ) une suite de courants positifs fermés qui converge vers
10436:lemme 8.5.1. Supposons q ⩾ 1 et l’assertion démontrée pour q − 1. Pour tout k, po-
10438:courants positifs fermés, par récurrence, et l’on a Sk → S. D’après le lemme 8.5.1,
10443:le courant d′ d′′ (u1 S) l’est également. En appliquant de nouveau le lemme 8.5.1, on en
10455:les notations. Pour q = 0, il s’agit du lemme 8.5.1 qui n’exige que la continuité
10458:courants positifs fermés, par récurrence, et l’on a Sk → S. D’après le lemme 8.5.1, on
10462:nouveau le lemme 8.5.1, on en conclut que uk0 d′ d′′ (uk1 Sk ) converge vers u0 d′ d′′ (u1 S), ce
10489:Lemme 8.8.1. — Soit u une fonction lisse sur X. Tout point x de X possède un
10520:8.8.4. — Soit CPsh±   X le sous-faisceau en R-espaces vectoriels de CX engendré par le
10522:fonctions plurisousharmoniques »). D’après le lemme 8.8.1, ce sous-faisceau contient les
10527:8.8.5. — Soit T un courant positif fermé sur X de bidegré (q, q). Il existe un unique
10567:type (p, p). Le lecteur prendra garde que le courant défini au §8.8.4 n’est pas en général
11180:   Reprenons les notations de la proposition 8.4.3 en prenant m = n et a = 3. Pour tous
11191:Faisons tendre ℓ vers +∞ ; la proposition 8.7.2 et l’exemple 7.2.13 entraînent
12808:découle alors de la proposition 8.7.2.
21544:Proposition 15.2.1. — Soit X un espace k-analytique topologiquement séparé, consi-
21586:Corollaire 15.2.4. — Soit X un espace k-analytique localement holomorphiquement
21634:Corollaire 15.2.10. — Soit X un espace analytique localement holomorphiquement
22048:localement différentiellement séparé (corollaire 15.2.4). Il est décent (proposition 12.4.7)
22198:Cette dernière assertion découle de la proposition 8.7.2 ; démontrons a).
23720:Proposition 16.9.1. — Soit X un n-espace analytique sans bord sur un corps complet
23760:Démonstration. — D’après la proposition 16.9.1, l’espace tropical associé à X est justi-
23770:Démonstration. — D’après la proposition 16.9.1, l’espace tropical associé à X est justi-
23773:Corollaire 16.9.4. — Soit X un n-espace k-analytique sans bord. Soit u1 , . . . , um des
23858:En vertu du la proposition 8.7.2, le membre de gauche converge vers
23864:D’après le corollaire 16.9.4, le complémentaire de U est RnégligeableR pour la mesure µα .
24082:Remarque 17.2.4. — Soit E un fibré vectoriel muni d’une métrique paralinéaire en-
24162:positifs telle que ∥ei ∥ = ri identiquement sur V pour tout i (remarque 17.2.4).       P Les ei (x)
24249:vecteurs sont de norme constante (17.2.4). Quitte à raffiner ce recouvrement, on peut
25712:Corollaire 18.1.7. — Soit X une k-courbe analytique propre et soit L un fibré en
26341:a expliqué au paragraphe 8.8.5 comment la construction (v1 , . . . , vm ) 7→ d′ d′′ (v1 ) ∧
26479:D’après la proposition 8.7.2 le second terme du membre de gauche et le membre de droite
26490:sition 8.7.2. Comme Σ est compact et contenu dans U , la fonction log∥s∥−1 est bornée
26638:Proposition 18.4.3. — Soit X un n-espace k-analytique sans bord. Soit (L1 , . . . , Ln )
26722:Démonstration. — On sait d’après la proposition 18.4.3, que le support de cette mesure
26740:   Soit x ∈ Xstr . Avec les notations de la proposition 18.4.3, il s’agit de démontrer
26748:proposition 18.4.3, on se ramène au cas où tous les fibrés métrisés Li sont égaux à
26849:trement dit, de calculer les coefficients λx de la proposition 18.4.3) dans le cas général,
26874:Démonstration. — D’après la proposition 18.4.3, le support de cette mesure est contenu
27159:est une somme finie       λx δx (prop. 18.4.3) et les λx sont entiers par le théorème 18.4.7.
27194:Proposition 18.5.1. — Soit X un k-schéma propre de dimension n et soit L un fibré
27208:17.7.10). D’après la proposition 18.4.3 il existe un nombre réel λ tel que
27252:Théorème 18.5.5. — Soit X un k ◦ -schéma formel plat, localement topologiquement
27273:Démonstration. — Notons µ cette mesure c1 (L1 ) . . . c1 (Ln ). D’après la proposition 18.4.3
27496:Démonstration. — L’assertion a) est un simple rappel de la proposition 18.4.3.
27600:Théorème 18.7.2 (Mihatsch). — Soit X un n-espace k-analytique sans bord, soit
27748:lisses positives sur les fibrés sous-jacents. Par passage à la limite (proposition 8.7.2), il
27786:18.8.1. — Soit X un n-espace k-analytique sans bord, soit L1 , . . . , Ld des fibrés in-
27836:Théorème 18.8.4. — Soit X un espace analytique sans bord, topologiquement séparé.
27938:Corollaire 18.8.5. — Soit L1 , . . . , Ld des fibrés en droites sur X munis de métriques
27978:(ii)⇒(iii) est le théorème 18.8.4 et l’implication (iii)⇒(i) est la proposition 17.8.4.
28034:Exemple 18.8.10. — (Dans cet exemple, la notation e· désigne la réduction usuelle,
28042:   a) Expliquons comment déduire du théorème 18.8.4 et de la description du fibré ré-
28048:   D’après le théorème 18.8.4 et la remarque qui le suit, le courant c1 (L1 ) ∧ · · · ∧ c1 (Ld )
28194:  D’après le théorème 18.8.4, la classe c1 (L   e1,x ) . . . c1 (L
28229:   Posons Λi = Li |Y . Compte tenu du théorème 18.8.4, il reste à démontrer que
28256:via le théorème 18.8.4, et c’est ainsi que sa généralisation peut se formuler en l’état ac-
28452:  b) Il résulte de l’exemple 18.8.10, b), que les trois propriétés de positivité suivantes
28524:à zéro. D’après le théorème 18.8.4, le courant c1 (Q) est donc nul. Cela entraîne que le

  → Initialize memory and verify the proof sequentially.
  • Check all cited CLD statements and their applications.
  • Synthesize, validate, and write verification.json.
exec
/bin/zsh -lc "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python - <<'PY'
from mcp.server import memory_init, memory_append
run='20260831T204323Z_180a3827dff7'
print(memory_init(run, meta={'statement': 'Weighted CLN estimate (1.2) with explicit C(k,a) for full CPsh factors and smooth psh negative V near compact K_delta; polar integrability (1.3) for locally approchable canonically integrable V; nullity of lower-dimensional analytic subsets over any complete field.', 'input_shape':'proof_markdown_text'}))
memory_append(run,'events',{'event':'verification_started','skills':['verify-sequential-statements','check-referenced-statements','synthesize-verification-report'],'runtime':'AGENTS-prescribed local verification interpreter','note':'Connector memory call required unavailable approval; using the explicitly prescribed local memory helpers within writable workspace.'})
memory_append(run,'statement_checks',{'location':'Section 1: hypotheses and target extraction','status':'checked','assumptions':['Boundaryless locally differentially separated tropical space of level n with positive closed integration current','Full continuous CPsh minimal subsheaf, not first approximation stage','rho smooth psh on Y, delta>0, K_delta compact in Y, nonempty U={rho<0}','All u_j CPsh near K_delta; V smooth psh near K_delta and negative on U','Integer a>=4 and 0<=k<=n','For polar application, arbitrarily small compact smooth psh sublevels and locally approchable canonically integrable V','For analytic consequence, good separated strict boundaryless pure n-dimensional Berkovich space over arbitrary complete non-Archimedean field'], 'critical_errors':[], 'gaps':[]})
PY" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 213ms:
{'run_id': '20260831T204323Z_180a3827dff7', 'memory_dir': '/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/memory/20260831T204323Z_180a3827dff7', 'meta_path': '/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/memory/20260831T204323Z_180a3827dff7/meta.json', 'channels': {'statement_checks': '/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/memory/20260831T204323Z_180a3827dff7/statement_checks.jsonl', 'reference_checks': '/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/memory/20260831T204323Z_180a3827dff7/reference_checks.jsonl', 'verification_reports': '/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/memory/20260831T204323Z_180a3827dff7/verification_reports.jsonl', 'failed_checks': '/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/memory/20260831T204323Z_180a3827dff7/failed_checks.jsonl', 'events': '/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/memory/20260831T204323Z_180a3827dff7/events.jsonl'}}

exec
/bin/zsh -lc "sed -n '9740,9840p' tmp/1204.6277v2-cld.txt && sed -n '10245,10345p' tmp/1204.6277v2-cld.txt && sed -n '10405,10570p' tmp/1204.6277v2-cld.txt" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:
  Supposons d’abord que u soit lisse. Les fonctions f telles que f + u soit psh forment
un sous-faisceau de PshU qui contient les fonctions lisses psh et est stable par limite
décroissante ; il contient donc toutes les fonctions psh sur U . En particulier, u + v est
psh lorsque u est lisse.
  Dans le cas général, les fonctions f telles que f + v soit psh forme un sous-faisceau
de PshU qui contient les fonctions lisses psh d’après le premier cas traité et est stable
par limite décroissante ; il contient donc toutes les fonctions psh sur U ; par suite, u + v
est psh.
196                    CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

Remarque 8.1.3. — Cette définition est inspirée par le théorème de [67] en analyse
complexe qui affirme que dans ce contexte, une fonction psh sur un espace de Stein est
limite d’une suite décroissante de fonctions psh lisses.
   Dans le présent travail, nous considérerons surtout des fonctions psh continues.
   Par ailleurs, rappelons que si une suite décroissante de fonctions continues converge
simplement vers une fonction continue, elle converge même localement uniformément
(théorème de Dini), puisqu’un espace tropical est localement compact.
Lemme 8.1.4. — Pour tout ordinal α, on définit par récurrence transfinie un sous-
faisceau PshX,α du faisceau des fonctions sur X par les conditions suivantes :
   a) On définit PshX,0 comme le faisceau des fonctions lisses u telles que d′ d′′ u ⩾ 0 ;
   b) Si α est un ordinal, on définit PshX,α+1 comme le sous-faisceau des fonctions sur X
qui sont localement limites décroissantes de fonctions de PshX,α ;
   c) Si α est un ordinal limite, on définit PshX,α comme le sous-faisceau des fonctions
sur X qui appartiennent localement à un PshX,β pour β < α.
La famille ordinale (PshX,α ) est une famille croissante de sous-faisceaux de PshX qui
vaut PshX pour α assez grand.
Démonstration. — Par récurrence transfinie, il résulte de la définition de PshX , que
PshX,α ⊂ PshX pour tout ordinal α. La construction montre que cette famille de sous-
faisceau est croissante. Elle est nécessairement stationnaire, par un argument de cardinal.
Soit α un ordinal à partir duquel la famille est constante et démontrons que PshX ⊂
PshX,α . Il suffit pour cela de démontrer que PshX,α vérifie les deux conditions de la
définition de PshX . Il est évident que PshX,α contient les fonctions lisses u telles que
d′ d′′ u ⩾ 0, qui appartiennent au sous-faisceau PshX,0 . Soit maintenant U un ouvert de X
et (un ) une suite décroissante de fonctions de PshX,α (U ) qui converge simplement vers
une fonction localement intégrable u et démontrons que u ∈ PshX,α (U ). Par construction,
on a u ∈ PshX,α+1 (U ) ; par définition de α, on a donc u ∈ PshX,α (U ).

Proposition 8.1.5. — Soit f : Y → X un morphisme d’espaces G-tropicaux affinés.
Pour toute fonction psh u sur X, la fonction u ◦ f sur Y est psh. Plus précisément, pour
tout ordinal α tel que u appartient à PshX,α , la fonction u ◦ f appartient à PshY,α .
Démonstration. — Compte tenu du lemme 8.1.4, il suffit de démontrer la seconde asser-
tion. On procède par récurrence sur α. Le cas α = 0 résulte de ce que pour toute fonction
psh lisse u, la fonction u ◦ f est psh lisse. L’assertion découle alors de la construction
par récurrence des faisceaux PshX,α et PshY,α .

Remarque 8.1.6. — En géométrie complexe, on pourrait définir une hiérarchie ordi-
nale analogue des faisceaux de fonctions psh, mais leur théorie établit que cette hiérarchie
est stationnaire à partir du cran 1. Dans notre cadre, nous ne savons même pas si la
hiérarchie ordinale des espaces de fonctions psh est stationnaire. Cependant, tous les
exemples de fonctions psh que nous connaissons appartiennent au premier cran de cette
hiérarchie.
Définition 8.1.7. — On note CPshX le plus petit sous-faisceau du faisceau CX des
fonctions continues sur X tel que pour tout ouvert U de X, l’ensemble CPshX (U ) vérifie
les propriétés :
   i) Il contient les fonctions lisses u sur U telles que d′ d′′ u ⩾ 0 ;
                        § 8.1. FONCTIONS PLURISOUSHARMONIQUES                          197

  ii) Il est stable par limite uniforme.
  On note CPshX ce sous-faisceau ; ses sections sont appelées des fonctions continues
plurisousharmoniques (cpsh).
Lemme 8.1.8. — Pour tout ordinal α, on définit par récurrence transfinie un sous-
faisceau CPshX,α par les conditions suivantes :
   a) On définit CPshX,0 comme le faisceau des fonctions lisses u telles que d′ d′′ u ⩾ 0 ;
   b) Si α est un ordinal, on définit CPshX,α+1 comme le sous-faisceau des fonctions
sur X qui sont localement limites uniforme de fonctions de CPshX,α ;
   c) Si α est un ordinal limite, on définit CPshX,α comme le sous-faisceau des fonctions
sur X qui appartiennent localement à un CPshX,β pour β < α.
La famille ordinale (CPshX,α ) est une famille croissante de sous-faisceaux de CPshX qui
vaut CPshX pour α assez grand.
Démonstration. — La démonstration est analogue à celle du lemme 8.1.4 en remplaçant
partout « limite décroissante » par « limite uniforme ».

Proposition 8.1.9. — Soit (fn ) une suite de fonctions de X dans R qui converge
localement uniformément vers une fonction f . Si les fn sont psh, alors f est psh.
Démonstration. — Comme les fonctions constantes sont psh, l’assertion découle du
lemme suivant.

Lemme 8.1.10. — Soit X un ensemble et soit (fn ) une suite de fonctions de X dans R
qui converge uniformément vers une fonction f . La suite (fn + 2∥f − fn ∥∞ ) converge
uniformément vers f et admet une sous-suite qui est décroissante.
Démonstration. — Puisque ∥f − fn ∥∞ tend vers 0, il est clair que la suite (fn +
2∥f − fn ∥∞ ) converge uniformément vers f . L’assertion est évidente s’il existe une
infinité d’entiers n tels que ∥f − fn ∥∞ = 0. On peut donc supposer que ∥f − fn ∥ > 0
pour tout n. Soit n un entier. Puisque (fn ) converge uniformément vers f , il existe
m > n tel que ∥fm − f ∥∞ < ∥f − fn ∥∞ /3. Des inégalités fm ⩽ f + ∥fm − f ∥∞ et
f − ∥fn − f ∥∞ ⩽ fn , on déduit que
fm +2∥fm − f ∥∞ ⩽ f +3∥fm − f ∥∞ ⩽ fn +3∥fm − f ∥∞ +∥fn − f ∥∞ ⩽ fn +2∥fn − f ∥∞ .
Le lemme s’en déduit.

Proposition 8.1.11. — On a CPshX = CX ∩ PshX : les fonctions continues plurisous-
harmoniques sont les fonctions continues (à valeurs réelles) qui sont plurisousharmoni-
ques. Plus précisément, pour tout ordinal α, on a CPshX,α = CX ∩ PshX,α .
Démonstration. — Compte tenu des lemmes 8.1.4 et 8.1.8, il suffit de vérifier la seconde
assertion. Prouvons cette égalité par récurrence transfinie. Les cas de l’ordinal 0 et
d’un ordinal limite sont évidents. Il suffit donc de prouver que pour tout ordinal α,
une fonction continue u définie sur un ouvert U est localement limite décroissante de
fonctions de CPshX,α si et seulement si elle est localement limite uniforme de telles
fonctions.
  Soit U un ouvert de X et soit (un ) une suite décroissante de fonctions de CPshX,α (U )
qui converge simplement vers une fonction continue u sur U . Le théorème de Dini assure
que la convergence est uniforme sur toute partie compacte de U . Comme U est localement



      § 8.5. THÉORIE DE BEDFORD–TAYLOR : PRODUIT PAR UN
                   COURANT POSITIF DE BIDEGRÉ (1, 1)

  Soit X un espace tropical de niveau n, sans bord.
Lemme 8.5.1. — Soit (Tn ) une suite de courants positifs et soit (un ) une suite de
fonctions continues. On suppose que la suite (Tn ) converge vers un courant T et que la
suite (un ) converge localement uniformément vers une fonction u. On a un Tn → uT .
206                      CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

Démonstration. — On peut raisonner localement et supposer que (un ) converge uni-
formément vers u. Soit ε > 0 et soit v une fonction lisse telle que ∥u − v∥ ⩽ ε ; on
écrit
                 un Tn − uT = (un − v)Tn + v(Tn − T ) + (v − u)T.
Soit ω une forme lisse à support compact, et soit α, β des formes lisses positives à support
compact telles que ω = α − β. Comme Tn est positif, on a
      |⟨(un − v)Tn , ω⟩| ⩽ |⟨(un − v)Tn , α⟩| + |⟨(un − v)Tn , β⟩| ⩽ ∥un − v∥⟨Tn , α + β⟩.
Comme v est lisse, le second terme
                                 ⟨v(Tn − T ), ω⟩ = ⟨Tn − T, vω⟩
tend vers 0 quand n tend vers +∞. Enfin, comme T est positif,
                             |⟨(v − u)T, ω⟩| ⩽ ∥v − u∥⟨T, α + β⟩.
Cela démontre que
               lim sup|⟨un Tn − uT, ω⟩| ⩽ 2∥u − v∥⟨T, α + β⟩ ⩽ 2ε⟨T, α + β⟩.
                  n

Comme ceci vaut pour tout ε, on a
                                    lim⟨un Tn , ω⟩ = ⟨uT, ω⟩.
                                      n

Cela prouve que un Tn → uT .

8.5.2. — Soit T un courant de bidegré (p, p) sur X qui est positif et fermé. L’hypothèse
que T est fermé signifie d′ T = 0 et d′′ T = 0. Par définition d’un courant positif, le
courant T est symétrique ; ainsi, chacune de ces annulations entraîne l’autre.

Lemme 8.5.3. — Soit S un courant fermé symétrique de bidegré (p, p), soit q un entier
tel que q ⩽ p − 1 et soit α une forme lisse symétrique de type (q, q). On a
                                  d′ d′′ (α ∧ S) = (d′ d′′ α) ∧ S.

Démonstration. — Soit β une forme lisse de type (p − q − 1, p − q − 1) ; démontrons que
l’on a
                         ⟨d′ d′′ α ∧ S, β⟩ = ⟨α ∧ S, d′ d′′ β⟩.
Comme les courants d′ d′′ α ∧ S et α ∧ S sont symétriques, on peut supposer que β est
symétrique. Par définition, on a
              ⟨d′ d′′ α ∧ S, β⟩ − ⟨α ∧ S, d′ d′′ β⟩ = ⟨S, d′ d′′ α ∧ β − α ∧ d′ d′′ β⟩.
Or, on a

  d′ (α d′′ β − d′′ α ∧ β) = d′ α ∧ d′′ β + α d′ d′′ β − d′ d′′ α ∧ β + d′′ α ∧ d′ β.
De plus, on démontre comme dans la preuve du lemme 1.5.10, la forme de type (p, p)
                                    d′ α ∧ d′′ β + d′′ α ∧ d′ β
est antisymétrique. Sa valeur sur le courant symétrique S est donc nulle. Comme S est
fermé, cela entraîne l’égalité voulue.
                               § 8.6. COURANTS DE BEDFORD–TAYLOR                                            207

8.5.4. — Soit T un courant de bidegré (p, p) sur X qui est positif et fermé. Soit u une
fonction psh (continue) sur X. Comme est T est positif, on peut former le courant uT
(exemple 7.2.12) et considérer le courant d′ d′′ (uT ). Si u est lisse, le lemme 8.5.3 entraîne
que l’on a
                   d′ d′′ (uT ) = d′ d′′ (u ∧ T ) = d′ d′′ u ∧ T = T ∧ d′ d′′ (u),
car T est fermé.
  En géométrie complexe, cette remarque est la base de la construction, par Bedford–
Taylor [6], de produits de courants. Nous allons utiliser la même méthode dans ce
contexte. Pour poursuivre la construction, il faut garantir que le courant d′ d′′ (uT ) est
encore positif. C’est le cas si T est positif et u est psh lisse et, plus généralement, si u
est psh en vertu du lemme suivant.
Lemme 8.5.5. — Soit T un courant de bidegré (p, p) sur X, positif et fermé. Pour
toute fonction continue psh u, le courant d′ d′′ (uT ) est positif et fermé.
Démonstration. — Pour tout ouvert U de X, soit P(U ) l’ensemble des fonctions conti-
nues u sur U telles que d′ d′′ (uT |U ) soit un courant positif. Le préfaisceau P ainsi défini
est un sous-faisceau de CX . Si u est psh lisse, on d′ d′′ (uT ) = d′ d′′ (u) ∧ T , donc u appar-
tient à P. Si (un ) est une suite de fonctions de P(U ) qui converge uniformément vers
une fonction u, la suite de courants (un T |U ) converge vers uT |U , donc d′ d′′ (uT |U ) est
limite de la suite de courants (d′ d′′ (un T |U )). Ces courants étant positifs par hypothèse, le
courant d′ d′′ (uT |U ) est positif et u appartient à P(U ). Cela entraîne que le faisceau P
contient le faisceau CPshX , ce qu’il fallait démontrer.

Proposition 8.5.6. — Soit j : Y → X un morphisme topologiquement propre d’espaces
tropicaux de niveaux m et n respectivement. Soit u une fonction psh continue sur X et
soit S un courant positif fermé sur Y . Le courant j∗ S sur X est positif fermé et l’on a
l’égalité
                            d′ d′′ (u) ∧ j∗ S = j∗ (d′ d′′ (j ∗ u) ∧ S).
Démonstration. — L’ensemble des fonctions psh u qui vérifient cette relation forment
un sous-faisceau en R+ -modules du faisceau des fonctions continues sur X. Il est stable
par limite uniforme. Compte tenu de la définition du faisceau CPshX , il suffit donc de
vérifier qu’il contient les fonctions lisses u telles que d′ d′′ u ⩾ 0. Dans ce cas, pour toute
forme lisse ω à support compact sur un ouvert U de X, on a
         ⟨d′ d′′ (uj∗ S), ω⟩ = ⟨uj∗ S, d′ d′′ ω⟩ = ⟨j∗ S, u d′ d′′ ω⟩
                            = ⟨S, j ∗ u d′ d′′ j ∗ ω⟩ = ⟨j ∗ uS, d′ d′′ j ∗ ω⟩ = ⟨d′ d′′ (j ∗ uS), j ∗ ω⟩
                            = ⟨j∗ d′ d′′ (j ∗ uS), ω⟩,
ainsi qu’il fallait démontrer.



                    § 8.6. COURANTS DE BEDFORD–TAYLOR

8.6.1. — Soit u et v des fonctions psh telles que h = u − v est lisse. Alors on a
d′ d′′ (uT ) = d′ d′′ (hT ) + d′ d′′ (vT ) = d′ d′′ (h) ∧ T + d′ d′′ (vT ), car h est lisse. En particulier,
si d′ d′′ h = 0, on en déduit que d′ d′′ (uT ) = d′ d′′ (vT ). Nous ne savons pas si cette égalité
208                       CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR


            § 8.7. THÉORIE DE BEDFORD–TAYLOR : ITÉRATION

8.7.1. — Soit u1 , . . . , uq des fonctions psh sur X et soit T un courant positif fermé.
Compte tenu du lemme 8.5.5, on définit par récurrence un courant positif fermé
                                  d′ d′′ (u1 d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T )))).
Par construction, ce courant est même d′ d′′ -exact si q ⩾ 1.
   Lorsque T est un courant de Bedford–Taylor, on démontre par récurrence à l’aide de
la proposition 8.6.8 qu’il en est de même du courant
                                  d′ d′′ (u1 d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T )))).
et que ce courant ne dépend que de la suite de courants (d′ d′′ (u1 ), . . . , d′ d′′ (uq ), T ),
justifiant ainsi la notation.
  Lorsque les uj sont lisses, ce courant est égal à
                                  d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ) ∧ T.
  Dans la suite de ce texte, nous nous autoriserons l’abus de notation consistant à écrire
ce courant
                          d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ) ∧ T
même si T n’est pas de Bedford–Taylor.
  En prenant T = δX , on a d′ d′′ (u) ∧ δX = d′ d′′ (u), pour toute fonction psh u. Plus
généralement, on a
        d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ) ∧ δX = d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) · · · ∧ d′ d′′ (uq ).
Proposition 8.7.2. — Soit (Tk ) une suite de courants positifs fermés qui converge vers
un courant positif fermé T . Soit (uk0 ), (uk1 ), . . . , (ukq ) des suites de fonctions continues
sur X qui convergent localement uniformément vers des fonctions u0 , u1 , . . . , uq sur X.
On suppose que pour tout j ∈ {1, . . . , q} et tout k, la fonction ukj est psh. Alors, la suite
de courants
                            uk0 d′ d′′ (uk1 ) ∧ · · · ∧ d′ d′′ (uqq ) ∧ Tk
converge vers le courant
                                      u0 d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (uq ) ∧ T.
Démonstration. — On raisonne par récurrence sur q. Pour q = 0, l’assertion résulte du
lemme 8.5.1. Supposons q ⩾ 1 et l’assertion démontrée pour q − 1. Pour tout k, po-
sons Sk = d′ d′′ (uk2 d′ d′′ (. . . d′ d′′ (ukq Tk ))) et S = d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T ))) ; ce sont des
courants positifs fermés, par récurrence, et l’on a Sk → S. D’après le lemme 8.5.1,
on a uk1 Sk → u1 S. Par continuité de l’opérateur d′ d′′ sur les courants, on a donc
210                              CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

d′ d′′ (uk1 Sk ) → d′ d′′ (u1 S). Comme pour tout k, le courant d′ d′′ (uk1 Sk ) est positif fermé,
le courant d′ d′′ (u1 S) l’est également. En appliquant de nouveau le lemme 8.5.1, on en
conclut que uk0 d′ d′′ (uk1 Sk ) converge vers u0 d′ d′′ (u1 S), ce qu’il fallait démontrer.
   Nous aurons besoin de la variante suivante.
Proposition 8.7.3. — Soit (Tk ) une suite de courants positifs fermés qui converge
vers un courant positif fermé T . Soit f : X → Rn une carte harmonique. Soit (v0k ),
(v1k ), . . . , (vqk ) des suites de fonctions convexes continues sur Rn qui convergent loca-
lement uniformément vers des fonctions v0 , v1 , . . . , vq ; pour tout i et tout k, posons
uki = f ∗ vik et ui = f ∗ vi . Alors, la suite de courants
                                        uk0 d′ d′′ (uk1 ) ∧ · · · ∧ d′ d′′ (uqq ) ∧ Tk
converge vers le courant
                                        u0 d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (uq ) ∧ T.
Démonstration. — La démonstration est analogue à la précédente ; on en reprend
les notations. Pour q = 0, il s’agit du lemme 8.5.1 qui n’exige que la continuité
des fonctions en jeu. Supposons q ⩾ 1 et l’assertion démontrée par q − 1. Posons
Sk = d′ d′′ (uk2 d′ d′′ (. . . d′ d′′ (ukq Tk ))) et S = d′ d′′ (u2 d′ d′′ (. . . d′ d′′ (uq T ))) ; ce sont des
courants positifs fermés, par récurrence, et l’on a Sk → S. D’après le lemme 8.5.1, on
a uk1 Sk → u1 S d’où, par continuité de l’opérateur d′ d′′ sur les courants, la convergence
d′ d′′ (uk1 Sk ) → d′ d′′ (u1 S). Pour tout k, le courant d′ d′′ (uk1 Sk ) est positif fermé en vertu
du corollaire 8.11.3, si bien que le courant d′ d′′ (u1 S) est positif fermé. En appliquant de
nouveau le lemme 8.5.1, on en conclut que uk0 d′ d′′ (uk1 Sk ) converge vers u0 d′ d′′ (u1 S), ce
qu’il fallait démontrer.

Proposition 8.7.4. — Soit T un courant positif fermé. Soit u1 , . . . , um des fonctions
psh et soit σ une permutation de {1, . . . , m} ; on a
d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) ∧ · · · ∧ d′ d′′ (um ) ∧ T = d′ d′′ (uσ(1) ) ∧ d′ d′′ (uσ(2) ) ∧ · · · ∧ d′ d′′ (uσ(m) ) ∧ T.
Démonstration. — Soit v une fonction psh sur X. Soit P le sous-faisceau de CPshX
formé des fonctions psh u telles que d′ d′′ (u d′ d′′ (vT )) = d′ d′′ (v d′ d′′ (uT )). Si u est lisse,
on a
      d′ d′′ (u d′ d′′ (vT )) = d′ d′′ (u) ∧ d′ d′′ (vT ) = d′ d′′ (vT ∧ d′ d′′ (u)) = d′ d′′ (v d′ d′′ (uT )),
de sorte que ce faisceau P contient les fonctions lisses. Il est stable par limites uniformes.
Par suite, il contient le faisceau des fonctions psh.
  Cela entraîne l’assertion voulue lorsque m = 2.
  Le cas où σ est la transposition échangeant deux entiers successifs en découle immé-
diatement. Le cas général s’en déduit car σ est composée de telles transpositions.

Proposition 8.7.5. — Soit j : Y → X un morphisme topologiquement propres d’es-
paces tropicaux de niveaux m et n respectivement. Soit u1 , . . . , up des fonctions psh sur X
et soit S un courant positif fermé sur Y . Le courant j∗ S sur X est positif fermé et l’on
a l’égalité
d′ d′′ (u1 ) ∧ d′ d′′ (u2 ) ∧ . . . d′ d′′ (up ) ∧ j∗ S = j∗ (d′ d′′ (j ∗ u1 ) ∧ d′ d′′ (j ∗ u2 ) · · · ∧ d′ d′′ (j ∗ up ) ∧ S).
Démonstration. — La démonstration se déduit de la proposition 8.5.6 par une récurrence
immédiate sur p.
                   § 8.8. EXTENSION AUX DIFFÉRENCES DE FONCTIONS PSH                           211

     § 8.8. EXTENSION AUX DIFFÉRENCES DE FONCTIONS PSH

Lemme 8.8.1. — Soit u une fonction lisse sur X. Tout point x de X possède un
voisinage sur lequel u s’écrit comme la différence de deux fonctions lisses psh.
   Plus précisément, soit U un ouvert contenu dans un domaine compact W sur lequel u
est tropicalisée par une carte tropicale f , il existe des fonctions lisses psh u1 , u2 sur U ,
f -tropicales, telles que u|U = u1 − u2 .

Démonstration. — Soit f : W → T un moment tropicalisant u, soit P le polyèdre com-
pact f (W ) et soit v une fonction lisse au voisinage de P telle que u|W = v ◦ ftrop .
   D’après la proposition 1.10.2, il existe des fonctions lisses v1 et v2 au voisinage de P
telles que v = v1 −v2 et telles que les formes d′ d′′ v1 et d′ d′′ v2 sont positives. Les fonctions
u1 = v1 ◦ ftrop |U et v2 = u2 ◦ ftrop |U sur U sont lisses, psh, et l’on a u = u1 − u2 .

Proposition 8.8.2. — a) Soit u une fonction G-lisse sur X. Soit W un domaine
analytique compact W sur lequel u est tropicalisée par un moment f , il existe des fonc-
tions convexes v1 , v2 sur l’enveloppe convexe de f (W ) telles que u|U = f ∗ v1 − f ∗ v2 .
   b) Soit u une fonction paralinéaire sur X et soit W un domaine analytique compact
de X sur lequel u est tropicalisée par un moment f . Il existe des fonctions paralinéaires
convexes v1 , v2 sur l’enveloppe convexe de f (W ) telles que u|U = f ∗ v1 − f ∗ v2 .

Démonstration. — D’après la proposition 6.3.4, il existe un voisinage domanial com-
pact V de x, une carte tropicale f : V → E sur V et une fonction G-lisse v sur f (V )
telle que u|V = f ∗ v. Lorsque u est paralinéaire, v l’est. D’après les propositions 1.10.10
et 1.10.11, il existe alors des fonctions convexes v1 et v2 sur l’enveloppe convexe de f (V )
telles que v = v1 − v2 sur f (V ), que l’on peut choisir paralinéaires sur u l’est. D’après la
proposition 8.2.5, les fonctions u1 = f ∗ v1 et u2 = f ∗ v2 sur V sont tropicalement convexes
et sont paralinéaires si u l’est ; elles vérifient u = u1 − u2 .

Corollaire 8.8.3. — Soit u une fonction G-lisse sur X. Tout point de X en lequel X
est décent possède un voisinage sur lequel u s’écrit comme la différence de deux fonctions
tropicalement convexes, que l’on peut choisir paralinéaires si u l’est.

8.8.4. — Soit CPsh±   X le sous-faisceau en R-espaces vectoriels de CX engendré par le
faisceau CPshX des fonctions psh. Ses sections seront appelées dpsh (« différence de
fonctions plurisousharmoniques »). D’après le lemme 8.8.1, ce sous-faisceau contient les
fonctions lisses. De même, les fonctions localement différence de deux fonctions tropi-
calement convexes seront appelées tropicalement d-convexes ; de telles fonctions sont
dpsh. Lorsque X est décent, toute fonction G-lisse est tropicalement d-convexe (propo-
sition 8.8.2).
8.8.5. — Soit T un courant positif fermé sur X de bidegré (q, q). Il existe un unique
morphisme (p + 1)-linéaire sur CX0 × (CPsh± p
                                          X) ,

                         (u0 , u1 , . . . , up ) 7→ u0 d′ d′′ u1 ∧ · · · ∧ d′ d′′ up ,
à valeurs dans le faisceau des courants de bidegré (p + q, p + q) sur X qui coïncide
avec cette application lorsque u0 , u1 , . . . , up sont psh et u0 est positive. Par construc-
tion, l’image de ce faisceau est constituée de différences de deux courants positifs. Il est
212                         CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

symétrique en (u1 , . . . , up ). Si T est de Bedford–Taylor, il ne dépend que de u0 et des
courants d′ d′′ u1 , . . . , d′ d′′ up . Si, de plus, u0 est dpsh, on a
             d′ d′′ (u0 d′ d′′ u1 ∧ · · · ∧ d′ d′′ up ) = d′ d′′ u0 ∧ d′ d′′ u1 ∧ · · · ∧ d′ d′′ up .
  Soit f 1 , . . . , f p des fonctions lisses telles que d′ d′′ (f i ) = 0. On a
      u0 d′ d′′ (u1 + f 1 ) ∧ · · · ∧ d′ d′′ (up + f p ) ∧ T = u0 d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (up ) ∧ T,
même si T n’est pas de Bedford–Taylor. Autrement dit, ce morphisme passe au quotient
en un morphisme de source CX0 × (CPsh±                 p
                                            X / HarmX ) où HarmX est le faisceau sur X des
fonctions lisses h telles que d′ d′′ h = 0.
Remarque 8.8.6. — Supposons que u1 , . . . , up sont tropicalement d-convexes et soit α
une forme lisse de type (n − p, n − p) sur X. Alors u0 7→ ⟨u0 d′ d′′ u1 ∧ · · · ∧ d′ d′′ up , α⟩
est une mesure de Radon sur X, car les uj sont dpsh.
   Démontrons que son support est localement contenu dans une partie squelettique. (Il
est donc contenu dans une partie squelettique de X si ce support est compact ou si X
est paracompact.)
   Plus précisément, soit U un ouvert de X, soit f : U → E une carte tropicale, soit P une
partie paralinéaire de E contenant f (U ) et soit a1 , . . . , ap des fonctions d-convexes sur P
telles que uj = f ∗ aj pour j ∈ {1, . . . , p}, soit enfin ω une forme de type (n − p, n − p)
sur P telle que α = f ∗ ω. Démontrons que la trace sur U du support de cette mesure de
                            (n)
Radon est contenu dans Σf .
   Lorsque les aj sont lisses et convexes, la restriction à U de cette mesure est égale à la
mesure associée à la forme lisse positive f ∗ (d′ d′′ a1 ∧ · · · ∧ d′ d′′ ap ∧ ω) et son support est
                (n)
contenu dans Σf . Cette propriété est locale sur X, et est préservée par limite uniforme,
d’après la continuité du produit de courants à la Bedford–Taylor. Il en résulte qu’elle
vaut dès que les ap sont convexes. Par multilinéarité, le résultat vaut également lorsque
les aj sont d-convexes.
Remarque 8.8.7. — Lorsque les fonctions uj comme ci-dessus sont par ailleurs G-
C 2 , l’expression u0 d′ d′′ u1 ∧ · · · ∧ d′ d′′ up peut être interprétée comme une G-forme de
type (p, p). Le lecteur prendra garde que le courant défini au §8.8.4 n’est pas en général
celui associé à cette G-forme. Ce dernier courant ne jouera d’ailleurs pas de rôle dans la
théorie, ce qui rend inoffensif cet abus de notation.
Définition 8.8.8. — Soit X un espace tropical de niveau n, sans bord. Si u est une

codex
The closure arguments in Sections 2–3 appear to work for the full CPsh sheaf: they use controlled differences of positive currents and separate closure in each variable. I’m now checking the integration-by-parts signs, the endpoint \(k=n\), and the analytic barrier construction.
exec
/bin/zsh -lc "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python - <<'PY'
from mcp.server import memory_append
r='20260831T204323Z_180a3827dff7'
records=[
('Section 2: convex composition and vector-cone operations', ['The subclass with F(u) in CPsh is a subsheaf and is closed under local uniform limits because F is uniformly continuous on local bounded ranges.','Smooth chain rule gives d\\'d\\'\\'F(u)=F\\'(u)d\\'d\\'\\'u+F\\'\\'(u)d\\'u wedge d\\'\\'u, positive for convex nondecreasing F.','The prescribed derivative 2t chi(t) has nonnegative derivative, is smooth across zero because chi vanishes nearby, and equals 2t beyond 1/2. An additive constant matches the square.','Addition uses closure separately in each variable; positive rescaling and adding constants preserve CPsh.']),
('Section 2: equations (2.1)–(2.3)', ['Local common shifts give positive CPsh f,g, their squares and their sum square. Algebra gives h"'^2=2f''^2+2g''^2-(f+g)''^2 and polarization gives hl.'"','Each curvature of a square or product is a finite difference of positive closed currents; no arbitrary differentiation of order-zero currents is assumed to preserve order zero.','Continuous coefficients multiply differences of positive currents, so Gamma is well defined and independent of decompositions. Direct expansion proves symmetry and bilinearity.']),
('Section 2: equation (2.4) and smooth equation (2.5)', ['On a neighborhood of each compact support, all four uniformly converging CPsh sequences and their limits have a common bounded positive shift.','Square and product curvature terms decompose into finitely many weakly convergent positive currents. CLD positive-current continuity applies separately to all coefficient products.','A fixed positive compact majorant bounds the masses of each positive sequence; finite sums give uniform local variation control, including additional uniformly converging continuous multipliers.','For smooth inputs, the separate closedness of S removes derivatives of S and ordinary Leibniz gives the displayed symmetric gradient product.']),
('Section 3: positivity for every dpsh function', ['Fix smooth psh v; positivity of Gamma_S(u-v) defines a local subsheaf, contains smooth psh u, and is closed under uniform limits by (2.4).','Fix arbitrary CPsh u and repeat closure in v, using the preceding case for smooth v. Positivity is local and every dpsh is locally such a difference.','The separate-variable argument needs no common smooth approximation sequence and does not identify CPsh with arbitrary current-positive continuous functions.']),
('Section 3: exponential identities (3.1)–(3.3)', ['The smooth chain rules are correct.','For uniformly converging CPsh u_j, exp(Bu_j) converges locally uniformly and remains CPsh. Curvatures and energies, including their exponential coefficients, converge by Section 2 and positive-current continuity.','The subclass satisfying both identities is a subsheaf closed under uniform limits and contains smooth psh inputs. CPsh minimality gives the identities for all CPsh u.','Combining the two identities produces the coefficient z"'^(-1) without nonsmooth derivatives.'"']),
('Section 4: positivity polynomial and measure Schwarz (4.1)–(4.2)', ['Bilinearity and positivity for h+t*l yield the polynomial inequality.','A dominating Radon measure exists locally as the sum of diagonal measures and the mixed total variation. A countable union over rational t leaves one null set.','Continuity of each scalar quadratic gives A,C>=0 and B"'^2<=AC almost everywhere. Bounded continuous nonnegative weights may be multiplied and integrated.'"']),
('Section 4: mixed derivative identity and smooth form compatibility (4.3)–(4.4)', ['For smooth h,rho, symmetry of Q equates the two top-degree cross terms; their difference pairs to zero.','Fixed smooth rho is locally dpsh, so (2.4) handles the right side, while distributional convergence handles the left. Closure proves (4.3) for CPsh h and linearity extends to dpsh.','Closed smooth theta"'^j commutes with d'"\\'d\\'\\' and with continuous multiplication in the definition of Gamma; positivity holds when theta is positive.'])]
for loc,steps in records:
 memory_append(r,'statement_checks',{'location':loc,'status':'checked','deduction_checks':steps,'critical_errors':[],'gaps':[],'references_pending':True})
print('Persisted 7 sequential checks (Sections 2–4).')
PY" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 230ms:
Persisted 7 sequential checks (Sections 2–4).

exec
/bin/zsh -lc "sed -n '10105,10248p' tmp/1204.6277v2-cld.txt && sed -n '7880,8145p' tmp/1204.6277v2-cld.txt && sed -n '11090,11190p' tmp/1204.6277v2-cld.txt" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:
classe C ⌊a⌋ ; on a d′ ρa− = −aρ−
                                a−1 ′
                                   d ρ et d′′ ρa− = −aρa−1     ′′
                                                          − d ρ.
   Soit a un nombre réel tel que a > 1. Pour tout k ∈ {0, . . . , n}, on définit une forme
de type (n − k, n − k) sur U par
                         ′ ′′
               βk = ρk+a
                     − (d d ρ)
                              n−k
                                  + (k + a)ρk+a−1
                                            −     d′ ρ ∧ d′′ ρ ∧ (d′ d′′ ρ)n−k−1 .
(Lorsque k = n, on omet le second terme.) La forme βk est à coefficients de classe C ⌊a⌋−1 ,
et son support contenu dans W , donc est compact, car k + a − 1 > 0. Comme ρ est lisse
et psh, la (1, 1)-forme lisse d′ d′′ ρ est positive ; de plus, d′ ρ ∧ d′′ ρ est une (1, 1)-forme
positive ; par suite, la forme βk est positive.
   On a
                          d′′ βk = −2(k + a)ρk+a−1
                                              −       d′′ ρ ∧ (d′ d′′ ρ)n−k
et
d′ d′′ βk = 2(k + a) −ρk+a−1 (d′ d′′ ρ)n−k+1 + (k + a − 1)ρk+a−2 d′ ρ ∧ d′′ ρ ∧ (d′ d′′ ρ)n−k .
                                                                                             
                       −                                   −

Par suite, on a l’inégalité de formes
                             −2(k + a)βk−1 ⩽ d′ d′′ βk ⩽ 2(k + a)βk−1 .

Proposition 8.4.3. — On suppose a ⩾ 3 et on pose C(k, a) = (4e)k a−1 (k + a)(2 +
a) . . . (k + 1 + a). Soit V une fonction psh négative lisse sur U . Pour tout entier k et
toute suite (u1 , . . . , uk ) de fonctions lisses psh sur X, on a
             Z                                                                Z
                              ′ ′′           ′ ′′
                βk ∧ |V | d d u1 ∧ · · · ∧ d d uk ⩽ C(k, a)∥u1 ∥U . . . ∥uk ∥U |V |β0 .
             U                                                                             U
204                               CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

Démonstration. — On démontre l’inégalité par récurrence sur k. Elle est évidente
lorsque k = 0, car C(0, a) = 1. Supposons maintenant k ⩾ 1. Notons Jk l’intégrale à
majorer et posons ψk = d′ d′′ u1 ∧ · · · ∧ d′ d′′ uk . Comme βk est ponctuellement nulle hors
de U , on a
      Z                            Z                                Z
                        ′ ′′                               ′ ′′
Jk = (−V βk )∧ψk−1 ∧d d uk =            (−V βk )∧ψk−1 ∧d d uk =       (−V βk )∧d′ d′′ (uk ψk−1 ).
         U                                      X                                 X

Comme X est sans bord, la formule de Green (proposition 5.11.1) entraîne alors
                               Z
                          Jk =    d′ d′′ (−V βk ) ∧ uk ψk−1 .
                                                X

Alors,
                    Z
         Jk = −             d′ (d′′ V ∧ βk + V d′′ βk ) ∧ uk ψk−1
                    ZX
             =−             (d′ d′′ V ∧ βk − d′′ V ∧ d′ βk + d′ V ∧ d′′ βk + V d′ d′′ βk ) ∧ uk ψk−1
                    ZX
             =−             (d′ d′′ V ∧ βk + 2 d′ V ∧ d′′ βk + V d′ d′′ βk ) ∧ uk ψk−1
                    X

en utilisant la symétrie de V , βk et ψk−1 (lemme 1.3.8). Puisque
d′ (V d′′ βk ∧ uk ψk−1 ) = d′ V ∧ d′′ βk ∧ uk ψk−1 + V uk d′ d′′ βk ∧ ψk−1 − V d′′ βk ∧ d′ uk ∧ ψk−1 ,
la formule de Stokes (proposition 5.11.1) et le fait que X soit sans bord entraînent que
      Z                         Z                            Z
         ′      ′′
        d V ∧ d βk ∧ uk ψk−1 =         ′′       ′
                                    V d βk ∧ d uk ∧ ψk−1 −       V uk d′ d′′ βk ∧ ψk−1 .
         X                                    X                               X

si bien que
                    Z
             Jk =           uk (V d′ d′′ βk − d′ d′′ V ∧ βk ) ∧ ψk−1 + 2V d′ uk ∧ d′′ βk ∧ ψk−1 .
                        X

En utilisant de nouveau que βk est ponctuellement nulle hors de U , on a
               Z
          Jk =    uk (V d′ d′′ βk − d′ d′′ V ∧ βk ) ∧ ψk−1 + 2V d′ uk ∧ d′′ βk ∧ ψk−1 .
                        U

  On a
               2V d′ uk ∧ d′′ βk = −4(k + a)V ρk+a−1
                                               −     d′ uk ∧ d′′ ρ ∧ (d′ d′′ ρ)n−k .
Pour deux fonctions u, v de classe C 1 , et pour h strictement positive, la positivité de la
forme (d′ u − h d′ v) ∧ (d′′ u − h d′′ v) entraîne la majoration
                        d′ u ∧ d′′ v − d′ v ∧ d′′ u ⩽ h−1 d′ u ∧ d′′ u + h d′ v ∧ d′′ v.
Lorsque uk est strictement positive, on en déduit la majoration

  2V d′ uk ∧ d′′ βk ∧ ψk−1
                              ⩽ 4(k + a)2 (−V )uk ρk+a−2
                                                   −     d′ ρ ∧ d′′ ρ ∧ (d′ d′′ ρ)n−k
                                                                     −1 ′      ′′      ′ ′′
                                                          + ρk+a
                                                             − (−V )uk d uk ∧ d uk ∧ (d d ρ)
                                                                                             n−k
                                                                                                 .
§ 8.5. THÉORIE DE BEDFORD–TAYLOR : PRODUIT PAR UN COURANT POSITIF DE BIDEGRÉ (1,
                                                                              2051)

Utilisant que V est psh sur U , donc d′ d′′ V ⩾ 0, il vient alors
        Z
           uk (−V ) − d′ d′′ βk + 4(k + a)2 ρk−2+a d′ ρ ∧ d′′ ρ ∧ (d′ d′′ ρ)n−k ∧ ψk−1
                                                                               
 Jk ⩽                                        −
         U
                                         Z
                                                         ′ ′′   n−k −1 ′
                                      + (−V )ρk+a  − (d d ρ)        uk d uk ∧ d′′ uk ∧ ψk−1 .
                                                   U
                                      ′ ′′
Compte tenu du calcul de d d βk , la forme entre parenthèse dans la première intégrale
est égale à
                   k+a−1 ′ ′′
          2(k + a)ρ−    (d d ρ)n−k+1 + (k + a + 1)ρk+a−2
                                                   −     d′ ρ ∧ d′′ ρ ∧ (d′ d′′ ρ)n−k ,
donc est majorée par cβk−1 , où c = 2(k + a)(k + a + 1)/(k + a − 1). Ainsi,
                                   Z
              Jk ⩽ c∥uk ∥U Jk−1 + (−V )βk ∧ ψk−1 ∧ u−1      ′      ′′
                                                        k d uk ∧ d uk ,
                                               U
inégalité valable sous l’hypothèse que uk est strictement positive.
   Soit B un nombre réel ; posons aussi M = ∥uk ∥U . nous allons appliquer l’inégalité
précédente en remplaçant uk par vk = exp(Buk ). On a d′ vk = d′ (exp(Buk )) = Bvk d′ uk ,
d′′ vk = Bvk d′′ uk et
d′ d′′ vk = d′ (B exp(Buk ) d′′ uk ) = B 2 vk d′ uk ∧d′′ uk +Bvk d′ d′′ uk = vk−1 d′ vk ∧d′′ vk +Bvk d′ d′′ uk .
Comme d′ d′′ uk est positive et uk ⩾ −M , on a donc
                               d′ d′′ vk ⩾ Be−BM d′ d′′ uk + vk−1 d′ vk ∧ d′′ vk .
Par suite,
                       Z
          −BM
     Be         Jk =   βk ∧ (−V )ψk−1 ∧ (Be−BM d′ d′′ uk )
                    ZU                           Z
                  ⩽                      ′ ′′
                       βk ∧ (−V )ψk−1 ∧ d d vk −     βk ∧ (−V )ψk−1 ∧ vk−1 d′ vk ∧ d′′ vk
                           U                                  U
                  ⩽ c∥vk ∥U Jk−1
                  ⩽ ceBM Jk−1 ,
si bien que Jk ⩽ cB −1 e2BM Jk−1 . En choisissant B = 1/2M , on en déduit
                                                       (k + a)(k + a + 1)
                       Jk ⩽ 2ec∥uk ∥U Jk−1 = 4e                           ∥uk ∥U Jk−1 .
                                                           k+a−1
La proposition s’en déduit.



      § 8.5. THÉORIE DE BEDFORD–TAYLOR : PRODUIT PAR UN
de T et de φ∗ α est compacte. On a supp(φ∗ T ) ⊂ φ(supp(T )).
  En particulier, si le support de T est compact, celui du courant φ∗ T est également
compact, et l’égalité ⟨T, φ∗ α⟩ = ⟨φ∗ T, α⟩ vaut pour toute forme lisse α sur X.
7.1.12. Prolongement par zéro. — Soit X un espace tropical de niveau n. Soit U
un ouvert de X, notons j : U ,→ X l’immersion canonique, et soit T un courant sur U
de bidimension (p, q). On dit que T se prolonge par zéro à X si, pour toute forme lisse α
sur X, de bidegré (p, q) et à support compact, le support du courant T ∧ α|U sur U est
compact. Dans ce cas, la formule
                                    ⟨j! T, α⟩ = ⟨T, α|U ⟩
définit un courant j! T sur X qu’on appelle le prolongement par zéro de T .
  Cette application de prolongement est linéaire, commute à l’opérateur J et aux opé-
rateurs différentiels d′ , d′′ , d′ d′′ , etc.
Lemme 7.1.13. — Supposons de plus que dtrop (x) < max(p, q) pour tout x ∈ X             U.
160                  CHAPITRE 7. COURANTS SUR UN ESPACE TROPICAL

   Tout courant de bidimension (p, q) se prolonge par zéro à X.
   L’application de restriction de D p,q (X) dans D p,q (U ) est un isomorphisme, l’applica-
tion réciproque est donnée par T 7→ j! T .
  Dans le cas des espaces de Berkovich, l’exemple typique sera le cas où q = p et où U
est le complémentaire d’un fermé de Zariski de dimension < p.
Démonstration. — Soit T un courant sur U . Pour toute (p, q)-forme lisse α à support
compact sur X, le support de α est contenu dans U (lemme 3.3.6), donc le support
de T ∧ α|U est contenu dans U . Par suite, le courant T se prolonge par zéro à X. Plus
précisément, l’application α 7→ α|U est un isomorphisme d’espace vectoriels topologiques
de Acn−p,n−q (X) sur Acn−p,n−q (U ) (lemme 6.4.5), de sorte que le courant j! T est le seul
courant de bidimension (p, q) sur X qui prolonge T .



                            § 7.2. COURANTS POSITIFS

  Soit X un espace tropical de niveau n.
Définition 7.2.1. — Soit p un entier. Un courant S de bidimension (p, p) est dit
faiblement positif, respectivement positif, respectivement fortement positif, s’il est sy-
métrique et si pour toute forme α ∈ Acp,p (X) qui est fortement positive, respectivement
positive, respectivement faiblement positive, on a ⟨S, α⟩ ⩾ 0.
7.2.2. — Les trois notions de positivité pour les formes de type (0, 0) et (n, n) coïn-
cident ; il en est donc de même pour les courants. Comme les différentes notions de
positivité coïncident pour les formes symétriques de type (1, 1) et (n − 1, n − 1), il en
est de même pour les courants symétriques.
Remarque 7.2.3. — Soit T un courant tel que T et −T sont positifs ; démontrons
que T = 0. Soit ω une forme lisse à support compact sur X ; prouvons que ⟨T, ω⟩ = 0.
Si ω est antisymétrique, cela découle de la symétrie de T ; supposons donc que ω est
symétrique. Il existe aussi des formes positives α1 et α2 , lisses à support compact telles
que ω = α1 − α2 (proposition 6.5.2). Par linéarité, on peut donc supposer que ω est
positive. Mais alors, ⟨T, ω⟩ est à la fois positif (T est positif) et négatif (−T est positif),
donc nul.
Lemme 7.2.4. — Supposons que l’espace tropical X soit localement différentiellement
séparé. Les courants de bidimension (p, p) positifs ( resp. faiblement positifs, resp. for-
tement positifs) forment un sous-faisceau du faisceau Dp,p (X) des courants de bidimen-
sion (p, p).
Démonstration. — Soit S un courant de bidimension (p, p) sur X.
   Supposons que S soit positif. Soit U un ouvert de X. Pour toute forme ω sur U , de
type (p, p), positive et à support compact, le prolongement par 0 de ω est une forme
positive à support compact sur X. Il en résulte que S|U est positif.
   Soit maintenant (Ui ) un recouvrement ouvert de X tel que S|Ui soit positif pour tout i ;
démontrons que S est positif. Soit ω une forme de type (p, p) sur X, positive et à support
compact. Reprenons la preuve que les faisceaux forment un courant (proposition 7.1.7).
Il existe une famille finie (φi ) de fonctions lisses, positives et à support compact sur X
                                  § 7.2. COURANTS POSITIFS                                 161
                                                                              P
telle que pour tout i, le support de φi soit contenu dans P Ui , et telle que   φi soit égale
à 1 au voisinage du support de ω. On a de plus ⟨S, ω⟩ = ⟨S, φi ω⟩ ⩾ 0. Pour tout i, on
a a ⟨S, φi ω⟩ ⩾ 0, car φi ω est une forme positive dont le support est compact et contenu
dans Ui . Cela démontre que S est positif.
   Appliqué à chaque ouvert de X, cet argument démontre que les courants positifs de bi-
dimension (p, p) forment un sous-faisceau du faisceau des courants de bidimension (p, p).
Les cas des courants faiblement positifs et fortement positifs se démontrent de même.

Lemme 7.2.5. — Supposons que X soit localement différentiellement séparé. Soit T un
courant sur X. On suppose que pour tout ouvert U de X, toute forme tropicale ω sur U
qui est positive ( resp. faiblement positive, resp. fortement positive) et toute fonction lisse
positive ρ dont le support est compact et contenu dans U , on a ⟨T, ρω⟩ ⩾ 0. Alors T est
positif ( resp. fortement positif, resp. faiblement positif ).
Démonstration. — On traite le cas des formes positives, les deux autres sont analogues.
Soit ω une forme lisse positive à support compact sur X ; démontrons que ⟨T, ω⟩ ⩾ 0.
Pour tout x ∈ X, soit Ux un voisinage ouvert de X sur lequel ω est tropicale. Soit
                                                                       que, pour tout x ∈ X,
(λx )x∈X une famille à support fini de fonctions lisses positives telleP
le support de λx soit compact et contenu dans Ux , et telle que   P      λx soit égale à 1 au
voisinage du support de ω (corollaire 6.2.8). On a alors ω = x∈X λx ω. Par hypothèse,
⟨T, λx ω⟩ ⩾ 0 pour tout x. Donc ⟨T, ω⟩ ⩾ 0.

7.2.6. — L’image directe d’un courant positif (resp. faiblement positif, fortement po-
sitif) par un morphisme topologiquement propre d’espaces tropicaux est de même type.
Cela résulte du fait que la même propriété vaut pour l’image inverse des formes (§3.5.2).
Lemme 7.2.7. — Soit α une forme lisse symétrique sur X et soit T un courant symé-
trique sur X.
   a) Supposons que la forme α soit fortement positive. Alors, si T est positif ( resp.
faiblement positif, resp. fortement positif ), il en est de même de T ∧ α.
   b) Supposons que la forme α soit positive. Si T est positif, le courant T ∧ α est positif.
   c) Supposons que la forme α soit faiblement positive. Si T est fortement positif, le
courant T ∧ α est faiblement positif.
Démonstration. — Ces assertions découlent des propriétés de positivité d’un produit de
deux formes (prop. 3.5.5).

Proposition 7.2.8. — Soit X un espace tropical de niveau n, localement différentiel-
lement séparé.
  a) Toute mesure de Radon positive µ sur X induit, par restriction à Ac (X), un courant
positif [µ] d’ordre 0.
  b) L’application µ 7→ [µ] ainsi définie est une bijection continue de l’espace des me-
sures de Radon positives sur X sur l’espace des courants positifs de bidimension (0, 0)
sur X.
Démonstration. — a) Soit µ une mesure de Radon positive sur X ; démontrons que
la forme linéaire [µ] est un courant ; ce sera alors un courant positif. Soit K une partie
compacte de X et soit D un jeu de cartes couvrant sur X. Il suffit de démontrer que
la restriction de [µ] à l’espace AD,K
                                  0,0
                                      (X) est continue pour sa topologie C 0 . Soit ∥µ∥K
162                  CHAPITRE 7. COURANTS SUR UN ESPACE TROPICAL

la norme de µ sur K : pour toute fonction continue à support compact sur K, on a
|µ(f )| ⩽ ∥µ∥K ∥f ∥K . Cette inégalité vaut a fortiori pour toute fonction de AD,K (X) et
entraîne la continuité voulue.
   b) Cette implication est injective car l’espace des fonctions lisses à support compact
est dense dans l’espace des fonctions continues à support compact (corollaire 6.2.6).
   Il reste à prouver qu’elle est surjective. Soit S un courant positif de bidimension (0, 0)
sur X. Soit K une partie compacte de X. Soit λ une fonction lisse et positive, à support
compact sur X, qui vaut 1 au voisinage de K. Pour toute fonction lisse f sur X dont
le support est contenu dans K, on a −∥f ∥K λ ⩽ f ⩽ ∥f ∥K λ. Comme S est positif, il en
résulte l’inégalité
                                     |S(f )| ⩽ ∥f ∥K S(λ).
Par suite, S est continu lorsque l’espace des fonctions lisses à support compact est muni
de la topologie de la convergence compacte. Par densité, S s’étend en une forme linéaire
positive sur Cc (X), c’est-à-dire en une mesure de Radon positive.
  La démonstration précédente n’a utilisé que la positivité de la forme linéaire S et
pas sa continuité. La proposition suivante montre comment ce fait se généralise en tout
degré.
Proposition 7.2.9. — Soit X un espace tropical de niveau n, localement différentiel-
lement séparé, soit p un entier et soit S une application linéaire de Acp,p (X) dans R
telle que S(Jω) = S(ω) pour tout ω ∈ Acp,p (X). Si S(ω) ⩾ 0 pour toute forme fortement
positive ω, alors S est un courant faiblement positif, d’ordre 0.
Démonstration. — Il s’agit de prouver la continuité de S lorsque Acp,p (X) est muni de la
topologie C 0 . D’après le lemme 7.1.3, il suffit de démontrer l’énoncé suivant : soit f une
carte tropicale définie sur une partie ouverte U de X, soit ρ une fonction lisse, positive
et à support compact sur U , la forme linéaire ω 7→ S(ρω) sur Afp,p (U ) est continue pour
la topologie C 0 .
   Soit W un domaine compact de U qui contient le support de ρ. Notons E l’espace
affine codomaine de f et munissons-le d’une norme euclidienne ; notons η = d′ d′′ ∥x∥2
la (1, 1)-forme fortement positive sur E. Soit P l’espace paralinéaire compact f (W ) ;
considérons une norme C 0 sur l’espace A p,p (P ). On déduit de la proposition 1.2.13 qu’il
existe un nombre réel c > 0 tel que la forme α + c∥α∥η p est fortement positive, pour
tout α ∈ A p,p (P ).
   Pour toute ω ∈ Afp,p (U ) ; il existe une unique forme α ∈ A p,p (P ) telle que ω|W = f ∗ α,
et l’application ω 7→ ∥ω∥P,0 est une semi-norme C 0 sur Af (U ). On la note ∥·∥W,0 .
   Soit ω ∈ Afp,p (U ) ; il existe une unique forme α ∈ A p,p (P ) telle que ω|W = f ∗ α, si
bien que ω + c∥α∥f ∗ η p est fortement positive. Il en est de même de ρ(ω + c∥α∥P,0 f ∗ η p ).
Par l’hypothèse sur S, on a donc
                              S(ρω) + c∥ω∥W,0 S(ρf ∗ η p ) ⩾ 0.
En appliquant ce raisonnement à −ω, on en déduit l’inégalité
                                |S(ρω)| ⩽ cS(ρf ∗ η p )∥ω∥W,0 .
Cela démontre la continuité requise.
  Ainsi, S est un courant. La condition S(Jω) = S(ω) implique alors que c’est un courant
symétrique, et la condition de positivité S(ω) ⩾ 0 pour ω positive entraîne que c’est un
courant faiblement positif.
                                 § 7.2. COURANTS POSITIFS                                 163

Corollaire 7.2.10.  — Soit u une fonction localement intégrable sur X. La forme li-
néaire ω 7→ X uω sur Acn,n (X) définit un courant d’ordre 0 et de bidimension (n, n)
            R
sur X, fortement positif si u est positif.
   On note [u] ce courant.
Démonstration. — Les fonctions u+ = sup(u, 0) et u− = sup(−u, 0) sont localement
intégrables. Les formes linéaires qu’elles définissent sont fortement positives, donc sont
des courants d’ordre 0. Comme on a u = u+ −u− , la forme linéaire donnée est la différence
de ces deux courants, donc est un courant.

7.2.11. — Soit X un espace tropical de niveau n, localement différentiellement séparé.
Soit p un entier naturel et soit T un courant positif (resp. faiblement positif, resp.
fortement positif) de bidimension (p, p).
   Soit ω une forme positive (resp. fortement positive, resp. faiblement positive) de bide-
gré (p, p). Le courant T ∧ω est positif, de bidimension (0, 0) ; d’après la proposition 7.2.8,
il est donc associé à une unique mesure µTω sur X. Cette mesure applique une fonction
lisse à suppport compact u sur ⟨uT, ω⟩. Lorsque ω est à support compact, cette mesure
est à support compact. Lorsque ω est positive, cette mesure est positive.
Exemple 7.2.12. — Soit X un espace tropical de niveau n, localement différentiel-
lement séparé. Soit p un entier naturel et soit T un courant positif (resp. faiblement
positif, resp. fortement positif) de bidimension (p, p). Soit u une fonction borélienne et
localement bornée sur X. L’application ω 7→ µTω (u) est une forme linéaire sur Acp,p (X)
que nous noterons uT .
   Lorsque u est positive, cette forme linéaire uT est positive, donc est un courant positif
(resp. faiblement positif, resp. fortement positif) sur X.
   Lorsque u est une fonction borélienne et localement bornée arbitraire, on l’écrit u =
u − u− , où u+ = sup(u, 0) et u− = sup(−u, 0), comme différence de deux fonctions
  +

positives boréliennes localement bornées sur X. Comme uT = u+ T − u− T , c’est un
courant sur X, d’ordre 0.
   Cette notation est compatible avec celle déjà introduite lorsque u est une fonction
lisse puisque l’on a alors ⟨uT, ω⟩ = ⟨T, uω⟩ = µTω (u).
Exemple 7.2.13. — Soit (µn ) une suite de mesures de Radon positives et soit µ une
mesure de Radon positive sur X. Si [µn ] → [µ] au sens des courants, alors µn → µ au
sens des mesures. Cela résulte de la densité des fonctions lisses à support compact dans
les fonctions continues à support compact (corollaire 6.2.6).
Exemple 7.2.14. — Il n’est pas vrai que tout courant d’ordre 0 se prolonge en une
mesure. Considérons l’étoile XB associée à un ensemble infini B (cf. §6.7.3, dont nous
reprenons les notations). Soit (cb )b∈B une famille de nombres réels. Pour toute fonction
lisse f sur X, posons
                                      X                      
                            ⟨T, f ⟩ =     cb fb (0) − fb (−∞) .
                                        b∈B

Cela définit un courant sur X, de bidimension (0, 0), mais il ne provient d’une mesure
que lorsque la famille (cb ) est sommable. Cette mesure est alors égale à
                                   X         X
                                     cb δη −   cb δp(b,−∞) .
                                  b∈B         b∈B
164                  CHAPITRE 7. COURANTS SUR UN ESPACE TROPICAL

                      § 7.3. COURANTS D’INTÉGRATION

7.3.1. — Soit X un espace tropical de niveau    R n. Pour toute (n, n)-forme lisse α à sup-
port compact sur X, posons alors ⟨δX , α⟩ = X α, où l’intégrale d’une (n, n)-forme lisse
à support compact sur X a été définie en (5.8.5). On définit ainsi une forme linéaire sur
l’espace Acn,n (X). Elle est positive ; d’après la proposition 7.2.9, c’est donc un courant
sur X, qu’on appelle le courant d’intégration sur X et on le note δX . Il est de bidimen-
sion (n, n) et d’ordre 0. Une forme antisymétrique de type (n, n) sur X étant nulle, donc
son intégrale aussi, le courant δX est symétrique.
7.3.2. — On définit de manière analogue
                                   R∂       le courant d’intégration « sur le bord » de X,
      ∂                       ∂
noté δX , par la formule ⟨α, δX ⟩ = X α, pour toute (n − 1, n)-forme à support compact α
sur X.
  Cette   forme linéaire est continue pour la topologie C 0 . Compte tenu de la définition
de X α, cela découle en effet de la continuité pour la topologie C 0 de l’intégrale de bord
   R
d’une forme sur un polytope calibré dans un espace affine.
  Il est de bidimension (n − 1, n) et d’ordre 0 ; son support est contenu dans le bord
de X.
7.3.3. — Soit Y un espace tropical de niveau m et soit φ : Y → X un morphisme
topologiquement propre d’espaces tropicaux. Un cas particulier important est celui d’une
partie squelettique de X munie de son n-calibrage canonique, plus généralement d’une
partie squelettique de dimension ⩽ d quelconque munie d’un d-calibrage.
  Les constructions précédentes fournissent des courants φ∗ δY et φ∗ δY∂ sur X de bidi-
mensions (m, m) et (m − 1, m) respectivement.
  Le courant φ∗ δY est fortement positif.
7.3.4. — Soit ω une G-forme de type (p, q) à coefficients tropicalement boréliens loca-
lement bornés sur X. ROn définit un courant [ω] de bidimension (p, q) et d’ordre 0 sur X
par la formule α 7→ X ω ∧ α définie par l’intégrale des G-formes. Lorsque ω est une
forme lisse, on a [ω] = δX ∧ ω.
   Si ω est positive (resp. faiblement positive, resp. fortement positive), il en va de même
du courant [ω]. Cela découle de la définition d’un courant positif, des propriétés de
stabilité de la positivité par produit (prop. 3.5.5), et de ce que l’intégrale d’une (n, n)-
forme positive est positive.                             R∂
   On définit aussi le courant [ω]∂ par la formule α 7→ X ω∧α défini à l’aide de l’intégrale
de bord des G-formes. Il est d’ordre 0 et de bidimension (n − p − 1, n − q). Lorsque ω
est une forme lisse, on a [ω]∂ = δX ∂
                                      ∧ ω.
   Il découle de la définition de la topologie des espaces de courants que les applications
ω 7→ [ω] et ω 7→ [ω]∂ sont continues.
7.3.5. — Nous allons maintenant généraliser cette construction aux « G-formes » qui
sont combinaisons linéaires de G-formes usuelles à coefficients dans un anneau de fonc-
tions non nécessairement tropicales.
   Soit V un domaine de X et soit U un voisinage ouvert de V dans X dans lequel V
est fermé. Soit u ∈ L1loc (V ), ω ∈ AXp,q
                                       G
                                          (V ) et α ∈ Acn−p,n−q (U ) ; la G-forme ω ∧ α|V est à
support compact
            R     dans V , de sorte que u est intégrable pour la mesure associée. L’appli-
cation α 7→ V u(ω ∧ α)Rad est un courant d’ordre 0 sur U . La section correspondante de
                              § 7.3. COURANTS D’INTÉGRATION                              165

π ∗ Dp,q (V ) ne dépend pas du choix de U . On définit ainsi un morphisme de G-faisceaux
                                L1loc,X ⊗ AXp,q
                                             G
                                                → π ∗ (Dp,q )X .
                                                 Σ                           Σ                        Σ
puisque v est paralinéaire.
   Fixons une (p − 1)-cellule D ∈ C et soit x ∈ D̊. Considérons un morphisme de tores
p : T → Gp−1
           m  tel que la composée (p ◦ f )trop induise une immersion par morceaux d’un
voisinage de x dans D vers Rp−1 .
   Dans la suite, on va se contenter de considérer des formes ω du type f ∗ p∗ γ, où γ
est une (p − 1, p − 1)-forme lisse sur Rp−1 , et des fonctions lisses ρ dont le support ne
rencontre aucune p-cellule de Σ autres que celles qui contiennent D.
   Choisissons un (p − 1)-vecteur µD , une orientation εD . Pour toute p-cellule de C
contenant D, on en déduit une orientation de C (par la règle de la normale sortante)
222                        CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

et un vecteur eC dans C tel que le calibrage canonique de C soit égal à [eC ∧ µD , εC ].
Fixons aussi une fonction affine φC sur C qui est nulle sur D et telle que φC (eC ) = 1.
    Soit aC = ∂eC (v|C ) la dérivée de v|C dans la direction de eC ; alors vC = v − aC φC
est invariant par eC et donc provient de D par la projection de C sur D parallèlement
à eC . Sur C, on a donc d′′ v = d′′ vC + aC d′′ φC . Compte tenu de la construction de ω =
f ∗ p∗ γ, lorsqu’on calcule le produit extérieur d′′ v ∧ ω, qu’on le contracte par le calibrage
canonique µC et qu’on le restreint à D, il reste
                                           aC θ⟨f ∗ p∗ γ|D , µD ⟩.
On a donc                            Z X
                                               aC ρ⟨f ∗ p∗ γ, µD ⟩ = 0.
                                       D C⊃D

Comme θ et β sont arbitraires, on en déduit C⊃D aC f∗ p∗ µD = 0 ; en simplifiant par le
                                                P
(p − 1)-vecteur non nul p∗ f∗ µD , on a ainsi prouvé l’égalité
                                     X
                                          ∂eC (v|C ) = 0.
                                            C⊃D

   Avec les notations précédentes, µC = µD ∧ eC et u∗ (µC ) = u∗ (µD ) ∧ u∗ (eC ). Le premier
facteur u∗ (µD ) est indépendant de C, le second est le vecteur dont les coordonnées sont
les aC φC (eC ) = ∂eC (v|C ), lorsque v parcourt les coordonnées de u. On a donc
                            X                          X
                                 u∗ (µC ) = u∗ (µD ) ∧   u∗ (eC ) = 0
                             D⊃C                             C⊃D
                                              P                                      P
puisque les composantes du vecteur               C u∗ (eC ) sont données par            C ∂eC (v|C ) = 0.


Corollaire 8.11.2. — Soit T un courant squelettique sur X, localement différence de
courants de Bedford–Taylor, et soit u1 , . . . , ud des fonctions G-lisses, localement harmo-
niquement tropicalisables. Alors le produit
                                    T ∧ d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (ud )
pris au sens de la théorie de Bedford–Taylor coïncide avec le produit du courant squelet-
tique T par la G-forme d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (ud ).
Démonstration. — Pour résoudre le conflit de notations, désignons dans cette preuve
par ∩ le produit à la Bedford–Taylor et par ∧ le produit naïf entre G-formes, ou celui
d’un courant paralinéaire par une G-forme. Il s’agit de prouver
               T ∩ d′ d′′ (u1 ) ∩ · · · ∩ d′ d′′ (ud ) = T ∧ d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (ud ).
Par récurrence, on peut supposer que
            T ∩ d′ d′′ (u1 ) ∩ · · · ∩ d′ d′′ (ud−1 ) = T ∧ d′ d′′ (u1 ) ∧ · · · ∧ d′ d′′ (ud−1 ).
Ce courant S est localement différence de courants de Bedford–Taylor ; il s’agit alors de
démontrer que S ∩ d′ d′′ (u1 ) = S ∧ d′ d′′ (u1 ). On est ainsi ramené au cas d = 1 et S = T .
Alors, on a
         T ∩ d′ d′′ (u1 ) = d′ d′′ (u1 T ) = d′ d′′ (u1 T )) = d′ (T ∧ d′′ u1 ) = T ∧ d′ d′′ u1
d’après la proposition 8.11.1 appliquée avec d′′ puis avec d′ . Cela conclut la démonstra-
tion.
                      § 8.12. NÉGLIGEABILITÉ DES ENSEMBLES POLAIRES                          223

Corollaire 8.11.3. — Soit X un espace tropical de niveau n, sans bord. Soit T un
courant positif fermé sur X et soit u une fonction continue, localement de la forme f ∗ v,
où f est une carte harmonique et v est une fonction convexe. Alors u est dpsh et le
courant T ∧ d′ d′′ u sur X est positif.
Démonstration. — Le résultat est local sur X ; on peut donc supposer qu’il existe une
telle carte harmonique sur X. Par approximation, on peut également supposer que v est
lisse. Alors, u est G-lisse, de sorte que u est dpsh. De plus, la G-forme d′ d′′ u est égale
à f ∗ (d′ d′′ v), donc est positive. Le corollaire précédent identifie le courant T ∧ d′ d′′ u au
produit de T par la G-forme positive d′ d′′ u. par définition de ce dernier courant, il est
positif.



          § 8.12. NÉGLIGEABILITÉ DES ENSEMBLES POLAIRES

Théorème 8.12.1. — Soit X un espace tropical de niveau n, sans bord. On suppose
que tout point x de X possède une base de voisinages ouverts U sur lesquels il existe une
fonction psh lisse ρ : U → R telle que l’ouvert de U défini par {ρ < 0} soit un voisinage
relativement compact de x dans U .
   Soit u1 , . . . , un des fonctions psh continues sur X qui sont localement approchables,
soit V une fonction psh localement approchable sur X. Si V est localement intégrable
sur X, est elle est localement intégrable pour la mesure d′ d′′ u1 ∧ . . . d′ d′′ un sur X.
Démonstration. — L’assertion est locale sur X. Soit x un point de X. Comme les fonc-
tions ui et la fonction V sont localement approchables, on peut donc supposer que les ui
sont limite uniforme de suites (ui,ℓ )ℓ et que V est limite décroissante d’une suite (Vp )p de
fonctions psh lisses sur X. Compte tenu de l’hypothèse sur X, on peut en outre supposer
qu’il existe une fonction psh lisse ρ sur X telle que l’ouvert U défini par ρ < 0 soit un
voisinage relativement compact de x.
   Reprenons les notations de la proposition 8.4.3 en prenant m = n et a = 3. Pour tous
entiers ℓ et p, on a donc l’inégalité
     Z                                                                          Z
                      ′ ′′              ′ ′′
        βn ∧ (−Vp ) d d u1,ℓ ∧ · · · ∧ d d un,ℓ ⩽ C(n, 3)∥u1,ℓ ∥U . . . ∥un,ℓ ∥U (−Vp )β0 .
      U                                                                           U
Comme βn est nulle hors de U , on peut récrire cette inégalité
   Z                                                                         Z
                   ′ ′′              ′ ′′
     βn ∧ (−Vp ) d d u1,ℓ ∧ · · · ∧ d d un,ℓ ⩽ C(n, 3)∥u1,ℓ ∥U . . . ∥un,ℓ ∥U (−Vp )β0 .
      X                                                                           U

apply patch
patch: completed
/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

exec
/bin/zsh -lc "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python - <<'PY'
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from mcp.server import search_arxiv_theorems, memory_append
run='20260831T204323Z_180a3827dff7'
base=Path('tmp')/run
refs=json.loads((base/'references.json').read_text())
def query(ref):
 try:
  result=search_arxiv_theorems(query=ref[2],num_results=3,timeout_seconds=12)
 except Exception as exc:
  result={'error':str(exc),'query':ref[2],'results':[]}
 (base/(ref[0]+'_arxiv.json')).write_text(json.dumps(result,indent=2))
 return (ref[0],result)
with ThreadPoolExecutor(max_workers=6) as pool:
 for rid,result in pool.map(query,refs):
  memory_append(run,'events',{'event':'arxiv_search_attempt','reference_id':rid,'query':result['query'],'result':result})
  print(rid, json.dumps(result)[:1000],flush=True)
PY" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 281ms:
R01 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.1.7\u20138.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage.", "results": []}
R02 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T.", "results": []}
R03 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed.", "results": []}
R04 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product.", "results": []}
R05 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.8.4\u20138.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford\u2013Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents.", "results": []}
R06 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 6.5.2 and 7.2.4\u20137.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces.", "results": []}
R07 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S.", "results": []}
R08 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation.", "results": []}
R09 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3.", "results": []}
R10 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated.", "results": []}
R11 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel.", "results": []}
R12 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford\u2013Taylor measures with continuous psh factors do not charge poles of integrable psh functions.", "results": []}
R13 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n.", "results": []}
R14 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|.", "results": []}
R15 {"error": "HTTPSConnectionPool(host='leansearch.net', port=443): Max retries exceeded with url: /thm/search (Caused by NameResolutionError(\"HTTPSConnection(host='leansearch.net', port=443): Failed to resolve 'leansearch.net' ([Errno 8] nodename nor servname provided, or not known)\"))", "query": "Chambert-Loir Ducros Formes diff\u00e9rentielles r\u00e9elles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii.", "results": []}

exec
/bin/zsh -lc "sed -n '21515,21612p' tmp/1204.6277v2-cld.txt && sed -n '23690,23805p' tmp/1204.6277v2-cld.txt && rg -n '6\\.5\\.2|1\\.2\\.13|triviale|strict.*sens|localement approchable|approchables' tmp/1204.6277v2-cld.txt | head -n 60" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:
tropicales.

Proposition 15.1.3. — Soit G une classe de coefficients. Soit X un espace analytique
topologiquement séparé et soit u une fonction numérique sur X.
  a) Pour que u soit G-localement de classe G , il faut et il suffit que u|Xred le soit.
  b) Si X est presque bon, pour que u soit localement de classe G , il faut et il suffit que
u|Xred le soit.

  Une variante de cet énoncé vaut pour les formes et les G-formes.
Démonstration. — Si u est localement (resp. G-localement) de classe G , il en est de
même de sa restriction à Xred . Démontrons la réciproque.
   a) Supposons que u|Xred soit G-localement de classe G . Soit V un domaine affinoïde
de Xred sur lequel il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn
telle que u|V = φ ◦ ftrop . On déduit du théorème de Gerritzen–Grauert (voir par exemple
[128], théorème 3.1) que V est recouvert par une réunion de domaines affinoïdes de la
forme Wred , où W est un domaine affinoïde de X. Sur Wred , chacune des fi se relève
en une fonction gi sur W ; ces fonctions sont inversibles et ont même norme que fi ;
elles définissent un moment g : W → Gnm tel que uW = φ ◦ gtrop . Cela prouve que u est
G-localement de classe G .
   b) Soit x un point de X et soit V un voisinage analytique de x dans Xred sur lequel
il existe un moment f : V → Gnm et une fonction φ de classe G sur Rn telle que u|V =
φ ◦ ftrop . Comme X est presque bon en x, chaque fi (x) ∈ H (x) est approchée par une
fonction gi ∈ OX,x . En particulier fi et gi ont même norme au voisinage de g. Ainsi, les
gi définissent un moment g défini au voisinage de X sur lequel on a u = φ ◦ gtrop ; cela
prouve que u est de classe G au voisinage de x.
                              § 15.2. SÉPARATION HOLOMORPHE                                423

                      § 15.2. SÉPARATION HOLOMORPHE

Proposition 15.2.1. — Soit X un espace k-analytique topologiquement séparé, consi-
déré comme espace G-tropical affiné. Soit ω une G-forme de type (p, q) sur X.
  a) Le support de ω est contenu dans l’ensemble des points x ∈ X tels que dk (x) ⩾
max(p, q).
  b) Soit V un domaine analytique de X et soit Y un fermé de Zariski de V . Si
dim(Y ) < max(p, q), le support de ω ne rencontre pas Y .

Démonstration. — Démontrons l’assertion a). Soit x ∈ X un point tel que dk (x) <
max(p, q). Comme dtrop (x) ⩽ dk (x), on a donc dtrop (x) < max(p, q) ; l’assertion résulte
donc de la proposition 3.3.6.
  L’assertion b) en résulte car tout point y de Y vérifie dk (y) ⩽ dim(Y ).

15.2.2. Séparation holomorphe. — On dira qu’un espace analytique X est holo-
morphiquement séparé si pour tout couple (x, y) de points de X avec x ̸= y il existe une
fonction analytique f sur X telle que |f (x)| ̸= |f (y)|. Un tel espace est topologiquement
séparé.
  Si X est un espace holomorphiquement séparé, il en va trivialement de même de tout
domaine analytique de X.
  Tout espace affinoïde est par définition holomorphiquement séparé ; en conséquence,
tout domaine analytique d’un espace affinoïde est holomorphiquement séparé.
  Un espace analytique sera dit localement holomorphiquement séparé s’il est topologi-
quement séparé et si chacun de ses points possède un voisinage analytique holomorphi-
quement séparé.
  Un espace analytique topologiquement séparé qui est bon, ou plus généralement dont
tout point possède un voisinage isomorphe à un domaine analytique d’un espace affi-
noïde, est localement holomorphiquement séparé. C’est en particulier le cas d’un espace
analytique topologiquement séparé sans bord.

Lemme 15.2.3. — Soit X un espace k-analytique holomorphiquement séparé. L’an-
neau des fonctions lisses sur X sépare les points.

Démonstration. — Soit x, y des points distincts de X. Par définition de la séparation
holomorphe, il existe une fonction analytique f sur X telle que |f (x)| ̸= |f (y)|.
  Supposons ces deux valeurs non nulles ; soit φ une fonction C ∞ à support compact
sur R valant 0 au voisinage de log|f (x)| et 1 au voisinage de log|f (y)|. La fonction
φ ◦ log|f |, définie sur l’ouvert d’inversibilité de f , est lisse ; prolongeons-la par 0 sur X
tout entier. Comme φ est à support compact, la fonction obtenue est nulle au voisinage
de l’ensemble des zéros de f ; elle est donc lisse et prend des valeurs différentes en x et y.
  Si f (x) = 0, on a alors f (y) ̸= 0 et on raisonne de même à partir d’une fonction φ à
support compact valant 1 au voisinage de log|f (y)|.
  Le cas où f (y) = 0 est analogue par symétrie.

Corollaire 15.2.4. — Soit X un espace k-analytique localement holomorphiquement
séparé. L’espace G-tropical affiné X est localement différentiellement séparé. En parti-
culier, le faisceau des fonctions lisses sur X sépare localement les points.
424 CHAPITRE 15. FORMES DIFFÉRENTIELLES RÉELLES EN GÉOMÉTRIE ULTRAMÉTRIQUE

Corollaire 15.2.5. — Soit X un espace analytique localement holomorphiquement sé-
paré. Soit K une partie compacte de X et soit U un voisinage ouvert de K. Il existe
une fonction lisse sur X qui vaut 1 au voisinage de K et dont le support est compact et
contenu dans U .
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du corollaire 6.2.4.

Théorème 15.2.6 (Stone–Weierstraß). — Soit X un espace analytique localement
holomorphiquement séparé et soit U un ouvert de X. Soit f une fonction continue à
valeurs réelles sur X dont le support est compact et contenu dans U . Soit a et b des
nombres réels tels que a ⩽ f ⩽ b. Pour tout ε > 0, il existe une fonction lisse g sur X
dont le support est compact, contenu dans U , telle que |f (x) − g(x)| < ε pour tout x ∈ X
et telle que a ⩽ g ⩽ b.
Démonstration. — Comme X est localement différentiellement séparé, c’est une consé-
quence du théorème 6.2.5.

Corollaire 15.2.7. — Soit X un espace analytique localement holomorphiquement sé-
paré.
  a) L’ensemble des fonctions lisses à support compact sur X est dense dans l’es-
pace Cc (X) des fonctions continues à support compact sur X, muni de la topologie limite
inductive des espaces de fonctions à support dans un compact donné.
  b) L’ensemble des fonctions lisses à support compact sur X est dense dans l’es-
montrons qu’elle est tropicalement H p -négligeable. On peut raisonner G-localement et
supposer que X est affinoïde. Soit W un domaine analytique compact de XL et soit f
un moment sur W . En utilisant le lemme 16.8.7 et en utilisant un recouvrement fini
de σ −1 (W ), on se ramène au cas où il existe un moment g au voisinage de A tel que
ftrop ◦ σ = gtrop + e log(r), où e ∈ Zm . Par hypothèse, gtrop (A) est H p -négligeable ; il en
est donc de même de ftrop (σ(A)).
   Pour tout j, posons uj,r = π ∗ uj et notons Tr le courant d′ d′′ u1,r ∧· · ·∧d′ d′′ up,r sur Xr ;
il est positif fermé. Posons aussi αr = π ∗ α.
   D’après la remarque 16.8.2, on a l’égalité de courants π∗ (Tr ) = T et et l’égalité de
mesures π∗ (Tr ∧ αr ) = T ∧ α. Toujours d’après cette remarque, le support de Tr ∧ αr
est contenu dans l’image σ(X) de la section de Shilov. D’après le théorème 16.8.5, cette
mesure sur Xr ne charge pas σ(A). Elle ne charge donc pas π −1 (A). Par suite, T ∧ α ne
charge pas A, ce qu’il fallait démontrer.

Lemme 16.8.7. — Soit X = M (A ) un espace k-affinoïde, soit W un domaine ana-
lytique compact de XL et soit f ∈ AL× une fonction analytique sur W , inversible. Il
existe une suite finie (K1 , . . . , Mm ) de parties compactes de σ −1 (W ) et pour tout j, une
fonction analytique gj sur X et un entier ej , telle que |f | ◦ σ = |gj |rej sur Kj .
Démonstration. — En utilisant le théorème de Gerritzen–Grauert, on se ramène au cas
où W est un domaine rationnel de XL . Il existe donc deux fonctions analytiques φ et ψ
sur XL telles que ψ ne s’annule pas sur W et telles que |f | = |φ|/|ψ| sur W . On est
ainsi ramené au cas où f est la restriction d’une fonction
                                                         Panalytique φ sur XL puis, par
approximation, au cas où φ ∈ A [T, T −1 ]. Écrivons φ = j fj T j , où fj ∈ A pour tout j.
Pour tout x ∈ X, on a |φ| ◦ σ(x) = max (|fj |(x)rj ). On peut ainsi prendre pour partie
compacte Kj l’ensemble des points x ∈ σ −1 (W ) tels que |φ| ◦ σ(x) = |fj (x)|rj .
466               CHAPITRE 16. COURANTS SUR LES ESPACES ANALYTIQUES

          § 16.9. NÉGLIGEABILITÉ DES ENSEMBLES POLAIRES

Proposition 16.9.1. — Soit X un n-espace analytique sans bord sur un corps complet
non archimédien k. On suppose que X est bon. Tout point de X possède une base de
voisinages ouverts U sur lesquels il existe une fonction psh lisse ρ : U → R telle que
ρ < 0 sur U et {ρ ⩽ 0} est compact.
Démonstration. — Comme tout ouvert de X est bon, il suffit de démontrer que tout
point x de X possède un voisinage ouvert comme dans l’énoncé. Comme X est bon,
il existe un domaine affinoïde V de X qui est un voisinage de x. Soit W un voisinage
affinoïde de x contenu dans Int(V /X) qui est un domaine rationnel : il existe des fonctions
holomorphes f1 , . . . , fn , g sur V sans zéro commun et des nombres réels strictement
positifs λ1 , . . . , λn strictement tel que W soit défini par les conditions |fi | ⩽ λi |g| ([8],
§2.2). Soit U l’ouvert d’inversibilité de V . Pour tout nombre réel µ ⩾ 1, Wµ = {|fi | ⩽
λi µ|g|} est un voisinage rationnel de x dans V qui est contenu dans U , car les fi et g
sont sans zéro commun.
   Pour tout i, posons ui = log(|fi /g|/λi ) ; c’est une fonction psh sur U , qui vaut −∞
sur {fi = 0} ∩ U est est paralinéaire en dehors. La fonction u = max(u1 , . . . , un ) sur U
est paralinéaire et psh, et pour tout t ⩾ 0, l’ensemble {u ⩽ t} est un voisinage de x
dans U . Nous allons en construire une approximation psh lisse.
   Soit θ une fonction lisse sur R, positive, de support contenu dans [−1; 1] et d’inté-
grale 1. Pour tout ε > 0 et tout s ∈ Rm , posons
                                   Z                                  m
                                                                      Y
           Mε (s1 , . . . , sm ) =    max(s1 + t1 , . . . , sm + tm )   θ(ti /ε) dt1 · dtm .
                                  Rm                                     i=1
                                                                  m
D’après le lemme 5.18 de [45], la fonction Mε sur R                   est lisse, convexe, croissante en
chaque variable, vérifie
                 max(s1 , . . . , sm ) ⩽ Mε (s1 , . . . , sm ) ⩽ max(s1 , . . . , sm ) + ε.
En outre, si s′ est la famille déduite de s en enlevant les coordonnées xi telles que
si ⩽ max(s1 , . . . , sm ) − 2ε, on a Mε (s) = Mε (s′ ). Par suite, la fonction uε sur U définie
par uε = Mε (u1 , . . . , un ) est lisse et psh, et vérifie u ⩽ uε ⩽ u + ε.
   Prenons ε = 1 et posons ũ = u1 − u1 (x) − 1. La fonction ũ sur U est psh et lisse ; on
a ũ(x) = −1 < 0. L’ensemble de U défini par ũ ⩽ 0 est contenu dans l’ensemble fermé
{u ⩽ u1 (x) + 1} de U . Or, ce dernier ensemble est aussi le domaine rationnel de V défini
par |fi | ⩽ eu1 (x)+1 λi |g|, car les fi et g sont sans zéro commun ; il est donc compact.

Théorème 16.9.2. — Soit X un n-espace k-analytique sans bord. Soit u1 , . . . , um des
fonctions psh continues sur X qui sont localement approchables, soit V une fonction
psh localement approchable sur X, soit α une forme lisse sur X. Si V est localement
intégrable sur X, est elle est localement intégrable pour la mesure d′ d′′ u1 ∧. . . d′ d′′ um ∧α
sur X.
Démonstration. — D’après la proposition 16.9.1, l’espace tropical associé à X est justi-
ciable du corollaire 8.12.2.

Corollaire 16.9.3. — Soit X un n-espace k-analytique sans bord. Soit u1 , . . . , um des
fonctions psh continues sur X qui sont localement approchables, soit α une forme lisse
                       § 16.9. NÉGLIGEABILITÉ DES ENSEMBLES POLAIRES                                 467

de type (n − m, n − m) sur X et soit V une fonction psh localement approchable sur X.
Si V est localement intégrable sur X, la mesure d′ d′′ u1 ∧ . . . d′ d′′ um ∧ α sur X ne charge
pas le lieu polaire de V .
Démonstration. — D’après la proposition 16.9.1, l’espace tropical associé à X est justi-
ciable du corollaire 8.12.3.

Corollaire 16.9.4. — Soit X un n-espace k-analytique sans bord. Soit u1 , . . . , um des
fonctions psh continues sur X qui sont localement approchables, soit α une forme lisse
de type (n − m, n − m) sur X. La mesure d′ d′′ u1 ∧ · · · ∧ d′ d′′ um ∧ α sur X ne charge
aucun fermé de Zariski de dimension < n.
Démonstration. — Soit Y un fermé de Zariski de X tel que dim(Y ) < dim(X). L’asser-
tion est locale au voisinage de tout point y de Y . Soit W un voisinage affinoïde de y. La
trace Y ∩ W ne contient aucune composante irréductible de W de dimension n. D’après
le lemme d’évitement des idéaux premiers, il existe une fonction analytique f sur W
telle que Y ⊂ V (f ) et telle que f ne s’annule identiquement sur aucune composante
irréductible de W de dimension n. Quitte à remplacer X par l’intérieur de W , on peut
supposer qu’il existe une fonction analytique f sur X qui ne s’annule identiquement sur
aucune composante irréductible de dimension n et X et telle que Y ⊂ V (f ).
   La fonction log|f | est alors continue sur toute partie squelettique de X, donc est
localement intégrable sur X. Par ailleurs, c’est la limite décroissante des fonctions
log max(|f |, t), pour t → 0. Comme ces fonctions sont psh et continues sur X, il en
résulte que log|f | est psh approchable. Comme son lieu polaire contient Y , le corollaire
en découle.

Corollaire 16.9.5. — Reprenons les hypothèses du corollaire précédent. Soit Y un n-
espace k-analytique et soit f : Y → X un morphisme topologiquement compact qui est
fini au-dessus d’un ouvert de Zariski dense. Pour toute fonction δ de X dans R qui
prolonge la fonction dcf , on a l’égalité de courants de bidegré (m, m)
              f∗ (d′ d′′ (f ∗ u1 ) ∧ · · · ∧ d′ d′′ (f ∗ um )) = δ · d′ d′′ u1 ∧ · · · ∧ d′ d′′ um
sur X.
Démonstration. — Dans la formule précédente, le membre de gauche est l’image directe
d’un courant positif sur Y , donc est un courant positif sur X. Quant à lui, le membre
de doite est le produit d’un courant positif d′ d′′ u1 ∧ · · · ∧ d′ d′′ um par la fonction δ ; nous
allons prouver qu’il s’agit d’un courant en démontrant que pour toute forme lisse α à
support compact, de type (n − m, n − m), la fonction δ est localement intégrable contre
la mesure signée µα = d′ d′′ u1 ∧ · · · ∧ d′ d′′ um ∧ [α], et que l’on a
                                                     Z
          ′ ′′  ∗              ′ ′′ ∗         ∗
       ⟨d d (f u1 ) ∧ · · · ∧ d d (f um ), f α⟩ =       δ · d′ d′′ u1 ∧ · · · ∧ d′ d′′ um ∧ [α].
152:  § 11.8. Espaces stricts et réduction de Temkin ; le cas trivialement valué . . . . . . . . 322
601:   La théorie est aussi valable en valuation triviale. C’est d’ailleurs un point crucial pour
604:de la valeur absolue triviale.
636:n’est pas isotriviale.
1042:Proposition 1.2.13 ([84], corollaire 1.17). — Soit ω une (1, 1)-forme symétrique
2133:même strictement convexe au sens des fonctions linéaires par morceaux, c’est-à-dire que
2426:Par suite, sa cohomologie est triviale sur tout ouvert, si bien que l’application canonique
2658:position 1.2.13, la forme λp appartient à l’intérieur du cône des formes de type (p, p)
4556:des formes linéaires non triviales, on verra plus loin des conditions raisonnables qui
4834:En effet, les conditions de recollement dans le faisceau quotient sont triviales, puisque
7353:Proposition 6.5.2. — Soit ω une forme de type (p, p) et symétrique sur X, à coef-
7540:        / I, on peut réaliser cet espace comme la couronne |T | ∈ I sur un corps triviale-
7553:un corps trivialement valué.
7589:trivialement valué ; l’ensemble B s’identifie à P1 (k) et le point η à la valeur absolue
7590:triviale sur le corps des fonctions k(P1k ).
7924:que ω = α1 − α2 (proposition 6.5.2). Par linéarité, on peut donc supposer que ω est
8020:considérons une norme C 0 sur l’espace A p,p (P ). On déduit de la proposition 1.2.13 qu’il
8374:sition 6.5.2) ; posons α = ω1 + ω2 . Puisque ±ω ⩽ α, on observe l’inégalité de mesures
8518:de la proposition 1.2.13 qu’il existe un nombre réel c > 0 tel que la forme α + c∥α∥η p
10075:(proposition 6.5.2). Posons ω0 = α0 + β0 ; c’est une forme lisse positive, de bidegré (p −
11171:   Soit u1 , . . . , un des fonctions psh continues sur X qui sont localement approchables,
11172:soit V une fonction psh localement approchable sur X. Si V est localement intégrable
11175:tions ui et la fonction V sont localement approchables, on peut donc supposer que les ui
11206:u1 , . . . , um des fonctions psh continues sur X qui sont localement approchables, soit α
11218:u1 , . . . , um des fonctions psh continues sur X qui sont localement approchables, soit α
11915:et qui tropicalise ρ, et adjoignons-lui la carte tropicale triviale de domaine le complé-
12946:trivialement gradués, c’est-à-dire tels que A[1] = A.
13250:   Lorsque A est trivialement gradué, son spectre au sens ci-dessus coïncide avec son
13251:spectre au sens usuel (son faisceau structural est donc également trivialement gradué).
13898:   Lorsque v est la valuation triviale, on écrira simplement PL/K au lieu de PL/(K,v) . C’est
13909:valuations : la valuation triviale v, la valuation v − qui prend une valeur strictement
13944:L1 et K 1 sont trivialement gradués), et l’on a OPL/K = OP1 L/K ⊗K 1 K.
14026:rème 1.3 de [50], qui établissait essentiellement (1) lorsque v est la valuation triviale. Il
14118:peut supposer que K et L sont trivialement gradués, ce que nous faisons désormais.
14129:trivialement valuée et algébriquement close (F, w) de (K, v) le sous-ensemble de X (F )
14839:absolue peut être triviale. On note k ◦ son anneau de valuation. Nous désignerons par ek
15360:n’est pas le cas en général : par exemple si k est non trivialement valué et si f ∈ k[[t]] est
15589:contre si k est trivialement valué et si 0 < r < s < 1, le morphisme continu naturel de k{T /s} vers
16118:(D, y). Lorsque la valeur absolue de k n’est pas triviale, y possède une base de voisinages
16121:11.7.7. — Supposons que la valeur absolue de k n’est pas triviale. On déduit alors
16132:   Notons que l’hypothèse que la valeur absolue de k n’est pas triviale est indispensable
16147:11.8.1. Modification de la terminologie dans le cas trivialement valué. —
16158:|k × | ̸= {1}, mais en diffère si k est trivialement valué ; sous cette hypothèse les espaces
16159:stricts au sens traditionnel le sont dans le nôtre, mais la réciproque est fausse en général :
16160:par exemple l’ouvert 0 < |T | < 1 de A1k est strict dans notre sens, mais pas dans
16165:et seulement si l’espace M (A) est strict au sens défini ci-dessus.
16168:que X soit strict dans notre sens. Pour montrer que X est strict au sens classique il suffit
16185:   Nous n’emploierons désormais l’adjectif « strict » que dans notre sens, sauf mention
16192:la réciproque (qui est déjà connue dans le cas où la valeur absolue de k n’est pas triviale).
16211:Remarque 11.8.4. — Si (X,   ^  x) est strict et si la valeur absolue de k n’est pas triviale,
16214:faux en général lorsque k est trivialement valué : l’ouvert strict de A1k défini par les
16320:fini. Précisons que nous autorisons toujours le corps k à être trivialement valué ; dans
16333:fini. C’est en effet évident si k est trivialement valué car alors A = Ak = A      fk . Supposons
16334:maintenant que k n’est pas trivialement valué. Choisissons un morphisme continu et
17226:   (i) il existe une valuation graduée |·| sur F , triviale sur e k, telle que |f]     i (y)| = hi pour
17228:   (ii) il existe une valuation graduée |·| sur F (ti )δ+1⩽i⩽n , triviale sur e    k(ti )δ+1⩽i⩽n , telle
17263:laires à K ; on peut dès lors supposer que k est algébriquement clos, non trivialement
17309:clos, non trivialement valué, et comme ftrop        (ξ) est strictement analytique, il existe un
17332:Proposition 12.3.5. — On suppose que la valuation de k n’est pas triviale. Soit X un
17363:Lemme 12.3.6. — Supposons que la valeur absolue du corps k n’est pas triviale. Soit X

diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

web search: 
web search: 
web search: 
web search: 
web search: CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents. ...
web search: CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage. ...
web search: CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3. ...
web search: CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n. ...
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

exec
/bin/zsh -lc "sed -n '760,1098p' tmp/1204.6277v2-cld.txt && sed -n '7310,7387p' tmp/1204.6277v2-cld.txt && sed -n '11200,11230p' tmp/1204.6277v2-cld.txt && sed -n '16142,16186p' tmp/1204.6277v2-cld.txt && sed -n '14828,14850p' tmp/1204.6277v2-cld.txt" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:
                                                          ′   ′
                                 ω ′ ∧ ω = (−1)(p+q)(p +q ) ω ∧ ω ′ .
                                                                                               →
                                                                                               −
   Pour distinguer les formes linéaires apparaissant dans le premier facteur Λp V ∗ de
                                              →
                                              −
celles apparaissant dans le second Λq V ∗ , on convient de noter systématiquement les
premières avec le préfixe d′ et les secondes avec le préfixe d′′ . Ainsi, si x ∈ V ∗ , on note
d′ x l’élément x ⊗ 1 dans A1,0 (V ) et d′′ x l’élément 1 ⊗ x de A0,1 (V ).
   Soit (x1 , . . . , xn ) une base de V ∗ . Pour tout couple (I, J) de suites strictement crois-
santes de {1, . . . , n}, où I = (i1 , . . . , ip ) et J = (j1 , . . . , jq ), notons d′ xI ∧ d′′ xJ la
superforme de type (p, q) définie par

                  d′ xI ∧ d′′ xJ = d′ xi1 ∧ · · · ∧ d′ xip ∧ d′′ xj1 ∧ · · · ∧ d′′ xjq .

Ces superformes d′ xI ∧ d′′ xJ fournissent une base de Ap,q (V ).
   Toute application linéaire f donne lieu à un morphisme d’algèbres évident
f : A∗,∗ (V ) → A∗,∗ (W ).
 ∗
22 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

1.1.2. — Il existe un unique automorphisme d’algèbres, J : A∗,∗ (V ) → A∗,∗ (V ), tel que
J(d′ xi ) = d′′ x et J(d′′ x) = − d′ x pour tout x ∈ V .
   On a donc J2 d′ x = − d′ x et J2 d′′ x = − d′′ x pour tout x ∈ V . Par suite, J2 agit
comme (−1)p+q sur Ap,q (V ) ; en particulier J2 est l’identité sur Ap,p (V ). On prendra
garde que notre définition diffère de celle de Lagerberg qui posait J d′′ x = d′ x ; elle fait
disparaître des termes de signe ;
   On dira qu’une forme ω de type (p, q) est symétrique si l’on a p = q et si Jω = ω. Les
formes symétriques définissent une sous-algèbre commutative de A∗,∗ (V ).



                        § 1.2. SUPERFORMES POSITIVES

1.2.1. — Comme l’a montré Lagerberg, les superformes fournissent un analogue réel
de l’algèbre des formes différentielles réelles sur un espace complexe. Cette analogie se
prolonge jusqu’à des notions de positivité qui jouent un rôle crucial dans la théorie.
Nous commençons ainsi par décrire un certain nombre de cônes des espaces Ap,p (V ). Les
résultats qui suivent sont pour l’essentiel des adaptations d’énoncés classiques dans le
cas complexe ; certains sont énoncés (parfois sans preuve) dans [92].
Définition 1.2.2. — Soit V un espace vectoriel réel de dimension n, Soit ω ∈ An,n (V ).
On dit que ω est positive s’il existe une base (x1 , . . . , xn ) de V ∗ et un nombre réel a ⩾ 0
tel que ω = a d′ x1 ∧ d′′ x1 ∧ · · · ∧ d′ xn ∧ d′′ xn .
  C’est alors possible pour toute base de V ∗ ; en effet, si f est un isomorphisme linéaire
de V , f ∗ (ω) = det(f )2 ω.
Définition 1.2.3. — Soit V un espace vectoriel réel de dimension n, soit p un entier
naturel et soit ω ∈ Ap,p (V ) une forme symétrique de type (p, p) sur V .
  a) On dit que ω est faiblement positive si pour toute famille (α1 , . . . , αn−p ) de formes
de type (1, 0), la (n, n)-forme
                           ω ∧ α1 ∧ J(α1 ) ∧ · · · ∧ αn−p ∧ J(αn−p )
est positive.
  b) On dit que ω est positive si pour toute forme α de type (n − p, 0), la (n, n)-forme
                               (−1)(n−p)(n−p−1)/2 ω ∧ α ∧ J(α)
est positive.
  c) On dit que ω est fortement positive s’il existe un entier m, des nombres réels
positifs a1 , . . . , am et des formes αj,s de type (1, 0) (pour 1 ⩽ j ⩽ p et 1 ⩽ s ⩽ m) tels
que
                                 Xm
                            ω=      as α1,s ∧ J(α1,s ) ∧ · · · ∧ αp,s ∧ J(αp,s ).
                            s=1

  Pour l’explication du signe dans la condition b), noter que si α = α1 ∧ · · · ∧ αm est le
produit de m formes de type (1, 0), alors
                 α1 ∧ J(α1 ) ∧ · · · ∧ αm ∧ J(αm ) = (−1)m(m−1)/2 α ∧ J(α).
                                   § 1.2. SUPERFORMES POSITIVES                                       23

   Ces cônes, dont la définition est due à Lagerberg [92], sont des analogues de cônes
classiquement introduits en géométrie complexe (chapitre III de [45], §3.2 de [91]). Bien
qu’inspirée par celle utilisée en géométrie analytique complexe, la terminologie adoptée
en diffère légèrement : les formes faiblement positives sont analogues à celles qui sont
simplement appelées positives en géométrie analytique complexe.
1.2.4. — Une (0, 0)-forme a ∈ A0,0 (V ) = R fortement positive est un nombre réel
positif ou nul.
     Si (x1 , . . . , xn ) est une base de V , une (n, n)-forme ω s’écrit de manière unique a d′ (x1 )∧
  ′′
d (x1 ) ∧ . . . ; les trois conditions de positivité sont équivalentes à l’inégalité a ⩾ 0.
     Nous avons restreint les définitions de positivité aux formes symétriques. Rappelons
que si dim(V ) = n, toute (n, n)-forme antisymétrique est nulle, de sorte qu’une (p, p)-
forme antisymétrique est orthogonale à toute (n − p, n − p)-forme symétrique.
     Ces trois conditions définissent des cônes convexes fermés de l’espace Ap,p          sym (V ) des
formes symétriques de type (p, p). Par définition, une forme symétrique α de type (p, p)
est faiblement positive si et seulement si α ∧ β est positive pour toute forme β fortement
positive de type (n − p, n − p). La bidualité des cônes convexes fermés en dimension finie
(theorem 14.1 de [118]) entraîne que α est fortement positive si et seulement si α ∧ β
est positive pour toute forme faiblement positive β.
     Nous verrons plus bas (corollaire 1.2.9) que la condition de positivité est auto-duale :
une forme α de type (p, p) est positive si et seulement si α ∧ β est positive pour toute
forme positive β de type (n − p, n − p).
     Une forme fortement positive est positive, une forme positive est faiblement positive.
Proposition 1.2.5 ([92], proposition 2.2). — Une forme symétrique ω de type (p, p)
sur V est faiblement positive si et seulement si pour tout espace vectoriel W de dimen-
sion p et toute application linéaire f : W → V , la forme f ∗ ω est positive.
Démonstration. — Soit ω une forme de type (p, p) telle que la forme f ∗ ω soit positive
pour tout espace vectoriel W de dimension p et toute application linéaire f : W → V ;
démontrons que ω est faiblement positive. Soit α1 , . . . , αn−p des formes de type (1, 0)
sur V ; posons
                      µ = ω ∧ α1 ∧ J(α1 ) ∧ · · · ∧ αn−p ∧ J(αn−p ).
On doit prouver que µ est positive. Si les formes αj sont linéairement dépendantes,
                             α1 ∧ J(α1 ) ∧ · · · ∧ αn−p ∧ J(αn−p ) = 0,
donc µ = 0. On peut donc supposer qu’elles sont linéairement indépendantes. Soit
αn−p+1 , . . . , αn des formes de type (1, 0) de sorte que la famille (α1 , . . . , αn ) soit une
base de V ∗ ; soit (v1 ,P     . . . , vn ) la base duale. Soit f : Rp → V l’application linéaire donnée
par f (x1 , . . . , xp ) = pi=1 xi vn−p+i et soit g : Rn−p → V l’application linéaire donnée par
g(y1 , . . . , yn−p ) = n−p                                                      ∗               ∗
                         P
                             j=1 yj vj . Pour tout j ∈ {1, . . . , n − p}, on a f (αj ) = 0 et g (αj ) =
d′ yj . Soit (f, g) : Rn → V l’application linéaire définie par (x1 , . . . , xp , y1 , . . . , yn−p ) 7→
f (x1 , . . . , xp ) + g(y1 , . . . , yn−p ) ; c’est un isomorphisme. De plus,
                 (f, g)∗ µ = (f, g)∗ (ω ∧ α1 ∧ J(α1 ) ∧ · · · ∧ αn−p ∧ J(αn−p )
                          = (f, g)∗ (ω) ∧ d′ y1 ∧ d′′ y1 ∧ · · · ∧ d′ yn−p ∧ d′′ yn−p .
En outre, (f, g)∗ (ω) = f ∗ (ω) + g ∗ (ω) et
                       g ∗ (ω) ∧ d′ y1 ∧ d′′ y1 ∧ · · · ∧ d′ yn−p ∧ d′′ yn−p = 0.
24 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

Ainsi,
                    (f, g)∗ µ = f ∗ (ω) ∧ d′ y1 ∧ d′′ y1 ∧ · · · ∧ d′ yn−p ∧ d′′ yn−p .
La positivité de la (p, p)-forme f ∗ (ω) entraîne donc celle de (f, g)∗ (µ). Comme (f, g) est
un isomorphisme linéaire, µ est positive.
   Inversement, soit W un espace vectoriel de dimension p et soit f : W → V une ap-
plication linéaire. Si f est n’est pas injective, la (p, p)-forme f ∗ ω est nulle. Supposons
donc que f est injective. Soit (v1 , . . . , vn ) une base de V tel que (v1 , . . . , vp ) soit une
base de f (W ) ; soit (α1 , . . . , αn ) la base duale. Définissons µ et g comme précédem-
ment. Par hypothèse, (f, g)∗ µ est positive ; le calcul ci-dessus entraîne alors que f ∗ (ω)
est positive.

1.2.6. — Expliquons comment la notion de positivité d’une (p, p)-forme symétrique ω
peut s’interpréter en termes de positivité d’une forme bilinéaire qω sur Λp V canonique-
ment associée à ω.
   Pour tout k ∈ N, posons σk = (−1)k(k−1)/2 . Fixons un élément non nul λ de Λn V ∗ .
Par définition les (n, n)-formes positives sont les multiples positifs de σn λ ∧ J(λ).
   On associe à ω une application bilinéaire sur Λn−p (V ∗ ) à valeurs dans An,n (V ) par la
formule (α, β) 7→ ω ∧ α ∧ Jβ.
   Rappelons aussi que le choix de λ fournit un isomorphisme v 7→ φv entre Λp V et
  n−p ∗
Λ V . Pour v ∈ Λp V , φv est la (n − p)-forme sur V donnée par φv (w) = ⟨λ, v ∧ w⟩
pour tout w ∈ Λn−p V . Il en résulte une application bilinéaire bω sur Λp (V ) à valeurs
dans An,n (V ) : pour v, w ∈ Λp V , on a
                                       bω (v, w) = ω ∧ φv ∧ Jφw .
  Par ailleurs, puisqu’elle appartient à Λp V ∗ ⊗ Λp V ∗ , ω « est » une forme bilinéaire qω
sur Λp V , symétrique puisque l’on a supposé que ω est symétrique. Explicitement, si
ω = α ⊗ β, pour α, β ∈ Λp V ∗ , on a
                                        qω (v, w) = ⟨α, v⟩⟨β, w⟩.
  Pour tous v, w ∈ Λp V , on a
(1.2.6.1)                       bω (v, w) = (−1)p(n−p) qω (v, w)λ ∧ Jλ.
Pour démontrer cette formule, on peut se donner une base (e1 , . . . , en ) de V et la base
duale (x1 , . . . , xn ) de V ∗ . On note eI = ei1 ∧ · · · ∧ eip si I = {i1 , . . . , ip } et i1 < · · · < ip ;
on définit d′ xI de manière analogue. On peut aussi supposer que λ = d′ x1 ∧ · · · ∧ d′ xn
et ω = d′ xI ⊗ d′′ xJ , où I, J sont des parties à p éléments de {1, . . . , n}. Si I est une
partie à p éléments de {1, . . . , n}, notons εI la signature de la permutation de {1, . . . , n}
qui est croissante et d’image I sur {1, . . . , p} et est croissante sur {p + 1, . . . , n}. Si K
et L sont des parties à n − p éléments de {1, . . . , n}, on a
                                      (
                                        (−1)p(n−p) εI εJ λ ∧ Jλ si K = ∁I et L = ∁J,
           ω ∧ d′ xK ∧ J d′ xL =
                                        0                            sinon.
En outre, φeK = εK d′ x∁K , si bien que
                                (
                                 (−1)p(n−p) λ ∧ Jλ si I = K et J = L,
                bω (eK , eL ) =
                                 0                 sinon.
                                § 1.2. SUPERFORMES POSITIVES                                  25

Enfin,                                                      (
                                                             1 si I = K et J = L,
               qω (eK , eL ) = ⟨d′ xI , eK ⟩⟨d′ xJ , eL ⟩ =
                                                             0 sinon,
d’où la formule annoncée.
   En outre, les formules précédentes entraînent que les signes de ces diverses formes sont
reliées par les équivalences suivantes :
La forme ω est positive au sens de la définition 1.2.3 ;
⇔ L’application bilinéaire (α, β) 7→ ω ∧ α ∧ Jβ est de signe σn−p ;
⇔ L’application bilinéaire bω est de signe σn−p ;
⇔ La forme bilinéaire qω est de signe σn−p (−1)p(n−p) σn = σp .
   Enfin, si f : W → V est une application linéaire, on a qf ∗ ω = qω ◦ (f, f ).
   Nous dirons qu’une (p, p)-forme symétrique est définie positive si la forme bilinéaire
symétrique σp qω est définie positive.
Lemme 1.2.7. — Soit ω ∈ Ap,p (V ) une forme symétrique de type (p, p), soit
(x1 , . . . , xn ) une base de V et soit
                                                X
                               ω = (−1)p(p−1)/2   ωI,J d′ xI ∧ d′′ xJ
                                               I,J

la décomposition de ω dans la base correspondante de Ap,p (V ). Alors, les quatre propriétés
suivantes sont équivalentes :
   a) La forme ω est positive ( resp. définie positive) ;
   b) La matrice symétrique (ωI,J ) (indexée par les parties à p éléments de {1, . . . , n})
est positive ( resp. définie positive) ;
   c) Il existe une base (αI ) de Λp V ∗ et une famille (cI ) de nombres réels positifs ou nuls
( resp. strictement positifs), indexées par les parties à p éléments de {1, . . . , n}, telles
que                                             X
                              ω = (−1)p(p−1)/2     cI αI ∧ J(αI ).
                                                     I

Démonstration. — L’équivalence des assertions (1) et (2) résulte de la discussion qui
précède le lemme et de ce qu’avec les notations introduites, la matrice (ωIJ ) est celle de
la forme bilinéaire (−1)p(p−1)/2 qω dans la base duale de la base (d′ xI )I de Λp V ∗ . Celle des
propriétés (2) et propriétés (3) découle de la diagonalisation des formes quadratiques.

Corollaire 1.2.8. — L’ensemble des formes positives dans Ap,p (V ) est le cône convexe
fermé engendré par les formes du type (−1)p(p−1)/2 α ∧ Jα, où α parcourt l’ensemble des
formes de type (p, 0).
Démonstration. — Le lemme précédent montre que les formes positives sont contenues
dans ce cône. Inversement, si α ∈ Ap,0 (V ) est une forme de type (p, 0) et β est une
(n − p, 0)-forme, la formule
     (−1)p(p−1)/2 α ∧ Jα ∧ (−1)(n−p)(n−p−1)/2 β ∧ Jβ = (−1)n(n−1)/2 (α ∧ β) ∧ J(α ∧ β)
montre que (−1)p(p−1)/2 α ∧ Jα est une forme positive, d’où l’autre inclusion.

Corollaire 1.2.9. — La condition de positivité est auto-duale : une forme α, symé-
trique de type (p, p), est positive si et seulement si α ∧ β est positive pour toute forme
positive β de type (n − p, n − p).
26 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

Démonstration. — Cela résulte immédiatement du corollaire précédent.

Corollaire 1.2.10. — Les trois notions de positivité coïncident pour les formes de
bidegrés (0, 0), (1, 1), (n − 1, n − 1) et (n, n).
   Elles ne coïncident pas en général, pas plus que leurs analogues en géométrie complexe.
Démonstration. — Le cas des formes de type (0, 0) et (n, n) a déjà été expliqué. Par
définition même, les formes faiblement positives de type (n − 1, n − 1) sont positives.
Le lemme précédent, ou un argument de dualité, prouve que les formes positives de
type (1, 1) sont fortement positives.
   Soit ω une forme deP  type (1, 1) qui est faiblement positive. Dans une base (x1 , . . . , xn )
                           n           ′        ′′
de V , écrivons ω =        i,j=1 ωi,j d xi ∧ d xj . D’après la proposition 1.2.5 appliquée à
l’application linéaire f : R → V donnée par t 7→ tv, on a
                                       X n
                                           ωi,j xi (v)xj (v) ⩾ 0
                                    i,j=1

pour tout vecteur v de V , de composantes vi = xi (v). La matrice (ωi,j ) est donc positive ;
d’après le lemme 1.2.7, la forme ω est positive, et aussi fortement positive.
  Par dualité, les formes de type (n − 1, n − 1) faiblement positives sont aussi fortement
positives.

Lemme 1.2.11. — Soit ω une forme symétrique de type (p, p) sur V . Soit W un espace
vectoriel réel et f : W → V une application linéaire.
  a) Si ω est positive ( resp. faiblement positive, resp. fortement positive), il en est de
même de la forme f ∗ ω sur W .
  b) Si f est surjective et si f ∗ ω est positive ( resp. faiblement positive, resp. fortement
positive), il en est de même de ω.
Démonstration. — Commençons par l’assertion 1). Le cas des formes fortement positives
est évident, celui des formes faiblement positives résulte de la proposition 1.2.5, tandis
que celui des formes positives découle de l’interprétation de la positivité en termes de
formes bilinéaires (§1.2.6).
   Venons-en à l’assertion 2) ; on suppose donc f surjective. Le cas des formes faiblement
positives résulte de la proposition 1.2.5 et du fait que toute application affine g : U → V
se relève à W .
   En ce qui concerne les formes positives et fortement positives, on choisit un isomor-
phisme W ≃ V ⊕ V ′ modulo lequel f est la première projection. Si f ∗ ω est positive, la
forme bilinéaire η qu’elle induit sur Λp W est positive (§1.2.6) ; comme η est le prolon-
gement par 0 de la forme bilinéaire η ′ induite par ω sur le sommande Λp V de Λp W , la
forme η’ est positive, et ω est positive en vertu là encore de §1.2.6.
   Si f ∗ ω est fortement positive, elle s’écrit sous la forme
                   X
                      ai αi,1 ∧ J(αi,1 ) ∧ αi,2 ∧ J(αj,2 ) ∧ . . . ∧ αi,ni ∧ J(αi,ri ),
où les αi,j sont de type (1, 0) et les ai strictement positifs. Comme f ∗ ω est égale au pro-
longement par 0 de la forme ω vue comme vivant dans le sommande Ap,p (V ) de Ap,p (W ),
il vient
              X
         ω=       ai αi,1,V ∧ J(αi,1,V ) ∧ αi,2,V ∧ J(αj,2,V ) ∧ . . . ∧ αi,ni ,V ∧ J(αi,ri ,V ),
                                  § 1.2. SUPERFORMES POSITIVES                                      27

où le V en indice indique la projection sur le sommande A1,0 (V ). Ainsi, ω est fortement
positive.

Proposition 1.2.12 (cf. [92], Lemma 2.1). — Soit ω1 , . . . , ωs des formes sur V et
posons ω = ω1 ∧ · · · ∧ ωs .
  a) Si les ωj sont toutes fortement positives, alors ω est fortement positive.
  b) Si les ωj sont toutes positives, alors ω est positive.
  c) Si les ωj sont toutes faiblement positives et si au plus une d’entre elle n’est pas
fortement positive, alors ω est faiblement positive.

Démonstration. — Par récurrence, l’assertion b) découle de la caractérisation du cône
des formes positives et de la formule
        (−1)p(p−1)/2 α ∧ Jα ∧ (−1)q(q−1)/2 β ∧ Jβ = (−1)r(r−1)/2 (α ∧ β) ∧ J(α ∧ β),
où α, β sont des formes de type (p, 0) et (q, 0) respectivement, et r = p + q.
   Pour démontrer les assertions a) et c), il suffit par récurrence de prouver que si une
forme β est fortement positive, alors α ∧ β est de même nature que α. On peut supposer
que β est de la forme β1 ∧ Jβ1 ∧ · · · ∧ βm ∧ Jβm , où les βj sont des formes de type (1, 0).
La preuve est alors directe.

Proposition 1.2.13 ([84], corollaire 1.17). — Soit ω une (1, 1)-forme symétrique
définie positive sur V . Soit p un entier ⩾ 1. Dans l’espace des (p, p)-formes symétriques,
la forme ω p appartient à l’intérieur relatif du cône des (p, p)-formes fortement positives,
à l’intérieur du cône des (p, p)-formes symétriques positives, et à l’intérieur du cône
des (p, p)-formes faiblement positives.

   En particulier, les formes positives, et a fortiori les formes faiblement positives, en-
gendrent l’espace des formes symétriques. En revanche, Lagerberg donne dans [92] (re-
mark 4.1) un exemple de (2, 2)-forme faiblement positive sur R4 , non nulle, qui est
orthogonale à toute forme fortement positive ; ainsi les formes fortement positives en-
gendrent un sous-espace strict des (2, 2)-formes symétriques sur R4 .
Démonstration. — D’après la proposition 1.2.12, ω p est fortement positif.
   Nous allons démontrer que si α ∈ An−p,n−p (V ) est une forme faiblement positive
et symétrique telle que ω p ∧ α = 0, alors β ∧ α = 0 pour toute forme β fortement
positive. Cela entraîne la première partie de la proposition, par dualité. Cela entraîne
aussi la troisième partie. Soit en effet une forme α, fortement positive, orthogonale à ω p ;
démontrons qu’elle est nulle. Comme elle est également faiblement positive, elle est alors
orthogonale à toute forme fortement positive. Puisque α est fortement positive, elle est
somme de formes du type cα1 ∧ Jα1 ∧ · · · ∧ αn−p ∧ Jαn−p , où (α1 , . . . , αn−p ) est une
famille d’éléments de V ∗ , qu’on peut supposer libre, et c ∈ R+ . Par positivité, chacun
de ces termes est également orthogonal à toute fortement positive. Mais cela entraîne
qu’ils sont nuls : complétons en effet la famille (α1 , . . . , αn−p ) en une base (α1 , . . . , αn ) ;
en prenant β = αn−p+1 ∧ Jαn−p+1 ∧ . . . , on trouve cα1 ∧ Jα1 ∧ · · · ∧ αn ∧ Jαn ⩾ 0, d’où
c = 0.
   Démontrons maintenant l’énoncé admis. Soit α une forme symétrique faiblement po-
sitive de type (n − p, n − p) telle que ω p ∧ α = 0, soit β1 , . . . , βp dans V ∗ et soit
β = β1 ∧ Jβ1 ∧ · · · ∧ βp ∧ Jβp ; prouvons que β ∧ α = 0.
28 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

   C’est évident si β1 , . . . , βp ne sont pas linéairement indépendantes, puisqu’alors β = 0.
Supposons donc que β1 , . . . , βp soient linéairement P     indépendantes et prolongeons cette
famille en une base (β1 , . . . , βn ) de V ∗ ; posons η = nj=1 βj ∧ Jβj .
   Comme ω est symétrique définie positive, il existe un nombre réel strictement positif c
tel que ω ⩾ cη au sens où la différence ω − cη est une (1, 1)-forme symétrique fortement
positive. D’après la proposition 1.2.12, appliquée à la forme faiblement positive α et
aux formes fortement positives ω, ω − cη et η, la différence ω p ∧ α − cp η p ∧ α est une
(n, n)-forme faiblement positive, de même que la forme η p ∧ α. Comme ω p ∧ α = 0 par
hypothèse, on en déduit que η p ∧ α = 0.
   Pour toute partie I = {i1 , . . . , ip } de {1, . . . , n}, où i1 < · · · < ip , notons βI =
βi1 ∧ · · · ∧ βip ; notons aussi λ = β1 ∧ · · · ∧ βn . Si p ∈ N, posons enfin σp = (−1)p(p−1)/2 .
Alors, η p = p!σp |I|=p βI ∧ JβI . La famille (βJ ∧ JβK ) indexée par les couples (J, K)
                     P

de parties à n − p éléments de {1, . . . , n} est une base de An−p,n−p (V ). Écrivons donc α
dans cette base :                               X
                                  α = σn−p             αJ,K βJ ∧ JβK .
                                        |J|=|K|=n−p

Pour toute partie I à p éléments de {1, . . . , n}, on a donc
                                   X
       σn−p βI ∧ JβI ∧ α = σp σn−p   αJ,K βI ∧ JβI ∧ βJ ∧ JβK = σn α∁I,∁I λ ∧ Jλ,
                                       J,K
d’où
                                     X
                   η p ∧ α = p!σn             αJ,J λ ∧ Jλ.
                                    |J|=n−p

ainsi définie est linéaire et continue pour les topologies C m .
  b) Cette application est injective.
  c) Supposons que Γ ⪯j ∆ et que toute partie fermée F de X appartenant à Ψ qui
contenue dans U appartient à Φ. Supposons que plus que dtrop (x) < max(p, q) pour tout
x ∈ X U . Alors cette application j! est un homéomorphisme, d’inverse donné par j ∗ .

Démonstration. — Cela résulte de la proposition 3.7.12, appliqué aux familles ΓU et ΓX ,
ce qui est licite car pour tout jeu de cartes tropicales couvrant U et toute partie F de U
qui est fermée dans X, le jeu de carte obtenu en adjoignant la carte tropicale constante
de domaine X U est couvrant sur X.

Proposition 6.4.6. — Soit X un espace G-tropical affiné, soit Φ une famille de sup-
ports sur X, et soit m ∈ N ∪ {+∞}.
   a) Pour toute forme ω ∈ AΦp,q (X), la forme Jω appartient à AΦq,p (X). L’application J
ainsi définie est linéaire et continue.
   b) Supposons m ⩾ 1. Pour toute G-forme ω ∈ AΦp,q (X), on a d′ ω ∈ AΦp+1,q (X) et
d′′ ω ∈ AΦp,q+1 (X). Les applications d′ et d′′ ainsi définies sont continues lorsqu’on munit
AΦp,q (X) de la topologie C m et les espaces AΦp+1,q (X) et AΦp,q+1 (X) de la topologie C m−1 .

Démonstration. — L’assertion découle de la proposition 3.7.13, appliquée à la famille
filtrante ΓX des jeux de cartes tropicales couvrants sur X.




                             § 6.5. FORMES POSITIVES

  Soit X un espace G-tropical affiné. Soit G une classe de coefficients.

Lemme 6.5.1. — Soit ω une forme de type (p, p) et symétrique sur X qui est positive
en tant que G-forme ( resp. faiblement positive, resp. fortement positive). Pour tout
point x ∈ X, il existe une carte tropicale f définie sur un voisinage U de x à valeurs dans
un espace affine E, et une forme positive α ( resp. faiblement positive, resp. fortement
positive) sur un sous-espace paralinéaire de E contenant f (U ), telle que ω|U = f ∗ α.

Démonstration. — Soit x un point de X. Soit V un voisinage domanial compact de x
sur lequel ω est tropicale ; soit f : V → E une carte tropicale qui tropicalise ω et soit α
une forme sur un sous-espace paralinéaire de E contenant f (V ) tels que ω|V = f ∗ α.
D’après le lemme 3.5.3, la restriction à f (V ) de α est positive (resp. faiblement positive,
resp. fortement positive). Il suffit donc de prendre pour carte tropicale la restriction à V̊
de f et pour forme α sa restriction à f (V ).
148                            CHAPITRE 6. ESPACES TROPICAUX

Proposition 6.5.2. — Soit ω une forme de type (p, p) et symétrique sur X, à coef-
ficients dans G dont le support est contenu dans un ouvert paracompact et localement
différentiellement séparé de X.
   a) Il existe des formes positives ω1 et ω2 sur X, à coefficients dans G , telles que
ω = ω1 − ω2 .
   b) Si, de plus, le support de ω est compact, les formes ω1 et ω2 peuvent être choisies
à support compact.
   L’hypothèse sur le support de ω est notamment réalisée lorsque X est localement
différentiellement séparé et paracompact. Dans le cas des espaces analytiques, elle sera
également réalisée si le support de ω est compact et si l’espace X est presque bon.
Démonstration. — Soit U un voisinage ouvert paracompact et localement différentielle-
ment séparé du support de ω. Dans le second cas, on s’arrange en outre pour que U soit
relativement compact dans X, ce qui est possible car X possède une base d’ouverts qui
sont dénombrables à l’infini.
   Soit (fi , Pi ) une famille de cartes tropicales, de sorte que fi soit un moment sur un
ouvert Vi de X et Pi un polytope compact contenant fi,trop (Vi ), et, pour tout i, soit αi
une forme sur Pi telle que ω|Vi = fi∗ αi . Il existe alors une famille localement finie (λi ) de
fonctionsP lisses sur X, subordonnée au recouvrement (U ∩Vi )i∈I telles que 0 ⩽ λi ⩽ 1 pour
tout i et λi est identiquement égale à 1 au voisinage du support de ω (corollaire 6.2.8).
Pour tout i, choisissons des formes positives  P αi,1 ∗et αi,2 sur Pi telles
                                                                       P que       αi = αi,1 − αi,2
(proposition 1.10.2). Posons alors ω1 =           λi fi αi,1 et ω2 =      λi fi∗ αi,2 ; ce sont des
formes lisses et positives telles que ω = ω1 − ω2 .

Remarque 6.5.3. — Nous appliquerons cette proposition aux formes lisses. Elle s’ap-
plique aussi aux G-formes lisses sur un espace tropical affiné décent, car de telles G-
formes sont des formes à coefficients G-lisses (proposition 6.3.4).
Proposition 6.5.4. — Soit X un espace G-tropical de niveau n, riche. Soit ω une
G-forme à coefficients tropicalement continus sur X.
   a) Pour que ω soit nulle, resp. positive, resp. faiblement positive, resp. fortement po-
sitive, il faut et il suffit que pour toute partie squelettique compacte P de X, la restric-
tion ω|P de ω à P soit nulle, resp. positive, resp. faiblement positive, resp. fortement
positive.
   b) Les points squelettiques x du support de ω sont denses dans supp(ω).
Démonstration. — a) Si ω est nulle (resp. . .), il en est de même de ses restrictions ω|P
          X                                                                   U
La fonction βn est continue et strictement positive sur U . Par suite, (−V ) est localement
intégrable sur U pour la mesure d′ d′′ u1 ∧ · · · ∧ d′ d′′ un .
224                     CHAPITRE 8. THÉORIE DE BEDFORD–TAYLOR

Corollaire 8.12.2. — Soit X un espace tropical comme dans le théorème 16.9.2. Soit
u1 , . . . , um des fonctions psh continues sur X qui sont localement approchables, soit α
une forme lisse de type (n − m, n − m) sur X, et soit V une fonction psh localement
approchable sur X. Si V est localement intégrable sur X, est elle est localement intégrable
pour la mesure d′ d′′ u1 ∧ . . . d′ d′′ um ∧ α sur X.
Démonstration. — L’assertion est locale sur X. On peut donc supposer que la forme α
est tropicale, du type f ∗ ω, où f : X → RN est une carte affine. Soit x ∈ X. Pour vérifier
la propriété d’intégrabilité au voisinage de x, on peut remplacer α par ρα, où ρ est
une fonction lisse à support compact, non nulle en x. Soit v = f ∗ ∥t∥2 ; il existe alors
un nombre réel c tel que −c(d′ d′′ v)n−m ⩽ α ⩽ c(d′ d′′ v)n−m . Le théorème précédent,
appliqué aux fonctions u1 , . . . , um , v, . . . , v, entraîne le résultat voulu.

Corollaire 8.12.3. — Soit X un espace tropical comme dans le théorème 8.12.1. Soit
u1 , . . . , um des fonctions psh continues sur X qui sont localement approchables, soit α
une forme lisse de type (n − m, n − m) sur X. et soit V une fonction psh localement
approchable sur X. Si V est localement intégrable sur X, la mesure d′ d′′ u1 ∧. . . d′ d′′ um ∧α
sur X ne charge pas le lieu polaire de V .
CHAPITRE 9


INTERSECTION TROPICALE




                 § 9.1. PRODUIT D’ESPACES TROPICAUX
322                   CHAPITRE 11. RAPPELS DE GÉOMÉTRIE ANALYTIQUE

  § 11.8. ESPACES STRICTS ET RÉDUCTION DE TEMKIN ; LE CAS
                       TRIVIALEMENT VALUÉ

11.8.1. Modification de la terminologie dans le cas trivialement valué. —
Nous aurons besoin dans la suite de manipuler des espaces analytiques (séparés) sur
un corps trivalement valué dont tous les germes sont à réduction stricte. Pour éviter
l’introduction d’un vocabulaire spécifique à cette situation, nous allons nous écarter de la
terminologie standard. Nous appellerons désormais espace strictement k-analytique tout
espace k-analytique X possédant un G-recouvrement (Xi ) par des domaines analytiques
séparés tels que (X ^               ^
                       i , x) et (Xi ∩ Xj , x) soient stricts pour tout (i, j) et tout x ∈ Xi ∩ Xj ;
si X est séparé (ce qui sera essentiellement toujours le cas ici) cela revient à demander
que (X,^   x) soit strict pour tout x ∈ X.
   Notre notion d’espace strictement k-analytique coïncide avec la notion usuelle lorsque
|k × | ̸= {1}, mais en diffère si k est trivialement valué ; sous cette hypothèse les espaces
stricts au sens traditionnel le sont dans le nôtre, mais la réciproque est fausse en général :
par exemple l’ouvert 0 < |T | < 1 de A1k est strict dans notre sens, mais pas dans
l’acception classique.
   Les deux notions sont toutefois équivalentes dans le cas affinoïde, comme en atteste
le lemme ci-dessous, pour lequel il n’est pas nécessaire de supposer |k × | ̸= {1}.
Lemme 11.8.2. — Soit A une algèbre k-affinoïde. Elle est strictement k-affinoïde si
et seulement si l’espace M (A) est strict au sens défini ci-dessus.
Démonstration. — Posons X = M (A). Si A est strictement k-affinoïde alors X est stric-
tement k-analytique au sens classique, et a fortiori au nôtre. Réciproquement, supposons
que X soit strict dans notre sens. Pour montrer que X est strict au sens classique il suffit
de s’assurer que pour tout f ∈ A la semi-norme spectrale ∥f ∥∞ appartient à {0} ∪|k × |Q .
Soit f ∈ A un élément tel que ∥f ∥∞ ̸= 0 ; nous allons montrer que ∥f ∥∞ ∈ |k × |Q . Choi-
sissons x ∈ X tel que |f (x)| = ∥f ∥∞ . L’image de l’élément fe de Ae dans H^  (x) est alors
                                                 ^
égale à f (x), et l’ouvert quasi-compact strict (X, x) de P
         g                                                          est alors contenu dans
                                                                  H
                                                                  ^ (x)/k
                                                                        e

PH       {fg
           (x)}. D’après 10.5.5, ceci entraîne que |fg                  e× |Q , c’est-à-dire
                                                     (x)| appartient à |k
 ^ (x)/e
       k
que |f (x)| ∈ |k × |Q .
   Nous n’emploierons désormais l’adjectif « strict » que dans notre sens, sauf mention
expresse du contraire. Nous dirons qu’un germe est strict s’il admet un représentant


RAPPELS DE GÉOMÉTRIE ANALYTIQUE




 § 11.1. GÉOMÉTRIE ANALYTIQUE : CONVENTIONS, NOTATIONS,
                       PREMIERS RAPPELS

   On fixe pour toute la suite de l’article un corps ultramétrique complet k ; sa valeur
absolue peut être triviale. On note k ◦ son anneau de valuation. Nous désignerons par ek
                                                         1
le corps gradué résiduel de k (10.8.1). Sa composante k de degré 1 est le corps résiduel
                                                        e
standard de k, c’est-à-dire le corps résiduel de l’anneau local k ◦ .
   Dans ce texte, la notion d’espace k-analytique sera à prendre au sens de Berkovich,
et plus précisément de [9]. Rappelons qu’un polyrayon est une famille (le plus souvent
finie) de nombres réels strictement positifs ; la longueur d’un polyrayon est le cardinal
de son ensemble d’indices. Faisons quelques rappels pour la commodité du lecteur.
11.1.1. — La construction fondamentale sur laquelle repose la géométrie de Berkovich
est la suivante. Soit A un anneau de Banach, c’est-à-dire un anneau A muni d’une norme
sous-multiplicative ∥ · ∥ (on inclut dans la définition le fait que ∥1∥ ⩽ 1, ce qui entraîne

web search: 
web search: 'Définition 8.1.7'
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

codex
The endpoint calculation checks out: \(b_n=1\) still gives the stated upper bound, and the exponential substitution cancels the same energy term on both sides. The arXiv theorem-search endpoint was unavailable; I found the CLD manuscript through web search and am checking the references directly there.
exec
/bin/zsh -lc "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python - <<'PY'
from mcp.server import memory_append
r='20260831T204323Z_180a3827dff7'
records=[
('Section 5: support, positivity and barrier derivatives (5.1)–(5.2)', ['closure(U) is a closed subset of compact K_delta and hence compact in Y. All needed factors are defined on a neighborhood of this support.','The smallest scalar power in beta_0 is a-1>=3. Since max(-t,0)"'^b is C''^(b-1), every beta_k is at least C''^2.'"','theta and eta are positive (1,1)-forms and their nonnegative weighted products are positive.','Writing p=n-k, d\\'\\'eta=-d\\'\\'rho wedge theta. The first term of beta_k contributes -l*r"'^(l-1)*d'"\\'\\'rho*theta"'^p and, for p>0, the second contributes the same. At p=0 only the first exists.'"','Applying d\\' gives b_k*l*(-r"'^(l-1)*theta''^(p+1)+(l-1)*r''^(l-2)*eta*theta''^p). The coefficients vanish at rho=0; there are no boundary delta terms.'"']),
('Section 5: compact C"'^2 test-form approximation'"', ['Convolution of the one-variable coefficient max(-t,0)"'^b by compact kernels converges in C''^2 on the bounded range of rho relevant to K_delta.'"','For small epsilon all approximants vanish for rho>epsilon, so their supports lie in the fixed compact K_delta. Compositions use a finite collection of fixed tropical presentations.','Order-zero coefficient pairings converge by uniform coefficient control. Transferring two derivatives from dd(uS) to compact C"'^2 tests defines the same limit because S is order zero and u is bounded on the compact neighborhood.'"','The smoothness of V on a neighborhood of K_delta makes (-V)beta_k a valid compact C"'^2 coefficient and avoids uncontrolled boundary derivatives. Positivity is used only after taking the coefficient limit.'"']),
('Section 6: degrees and integration by parts (6.1)–(6.2)', ['The iterated current S has degree (k-1,k-1), and Q=theta"'^(n-k)*S has degree (n-1,n-1); k=1 means S=delta_X.'"','Expand dd(-V beta_k)=-ddV*beta_k-2*d\\'V*d\\'\\'beta_k-V*ddbeta_k under symmetric pairing.','Stokes gives integral z*d\\'V*d\\'\\'beta_k*S=-integral V*d\\'z*d\\'\\'beta_k*S-integral zV*ddbeta_k*S, yielding precisely (6.1). For nonsmooth z this uses distributional d\\'(zS) and the C"'^2 argument.'"','Substituting (5.1) and (4.3) produces +2*b_k*l*(-V)*r"'^(l-1)*Gamma_Q(z,rho), with the displayed positive sign.'"']),
('Section 6: weighted Schwarz and coefficient comparison (6.3)–(6.5)', ['Young applied to the Radon–Nikodym densities with a=r"'^(l/2)/sqrt(z) and b=b_k*l*sqrt(z)*r''^((l-2)/2) gives exactly (6.3).'"','Every weight is bounded and continuous on the common compact support; z is bounded below, V is smooth, and r=0 annihilates every term outside U.','The term -z*ddV*beta_k*S is nonpositive because ddV, beta_k and S have the requisite positivity.','The remaining coefficients are b_k*l and b_k*l*((b_k-1)*l+1). For k<n these are 2l and 2l(l+1); for k=n they are l and l.','Both cases are bounded by c_k*beta_(k-1), with c_k=2l(l+1)/(l-1). Bounding z by its U supremum proves (6.5).']),
('Section 6: exponential substitution and recursion (6.6)–(6.9)', ['Continuity of u near compact K_delta makes exp(Bu) bounded above and below there. On U, exp(Bu)>=exp(-BM), where M=sup_U |u|.','Identity (3.3) and positivity imply (6.6). Multiplication by beta_k gives at least its first-summand energy contribution; the omitted energy contribution when k<n is nonnegative.','The first-summand energy equals the integral in (6.5) by (4.4). Subtraction therefore cancels it exactly and gives c_k*B"'^(-1)*exp(2BM).'"','Taking B=1/(2M) gives 4e*l*(l+1)/(l-1)*M. If M=0, locality makes dd(uS) vanish on U, while beta_k annihilates its complement.','The recursion starts at J_0. The product of the factors (j+a)/(j+a-1) telescopes to (k+a)/a, yielding the alternative constant.']),
('Section 7: fixed smooth polar truncations and monotone limit', ['Local approchability of this V supplies one decreasing sequence of smooth psh functions on a common neighborhood of x. Choose a compact smooth barrier inside that neighborhood and inside the domains of all CPsh factors.','Subtracting a constant exceeding the maximum of V_1 near K_delta makes every V_p and V negative there. This does not change local integrability because the positive product measure is locally finite.','For each fixed p, the completed weighted estimate applies; no derivative bound uniform in p is required.','The positive C"'^2 top form beta_0 is dominated by finitely many compact smooth positive top forms, using bounded coefficients and local charts. The stipulated canonical integrability of V makes the fixed right-hand side finite.'"','The functions -V_p increase to -V after the shift, so monotone convergence applies to the positive product measure multiplied by r"'^(n+a).'"','On compact subsets of U, r"'^(n+a) has a positive minimum. Hence the unweighted local integral is finite and the polar set is null.'"']),
('Section 7: arbitrary smooth traces (7.2), including endpoints', ['A symmetric current pairs to zero with the antisymmetric part of alpha, including after multiplying by scalar test functions.','On a local ambient affine presentation the symmetric coefficient matrix of alpha is bounded on the compact support. The coefficient matrix of (dd||t||"'^2)''^(n-m) is positive definite in the ambient space.'"','A sufficiently large scalar C gives positive-form inequalities plus/minus alpha<=C*(ddv)"'^(n-m), which remain valid under pullback even where the presentation has deficient rank.'"','Pairing with the positive mixed current gives -mu<=nu<=mu and therefore |nu|<=mu. Applying the n-factor case with repeated v proves integrability for |nu|.','For m=0 this uses only the repeated smooth v factors; for m=n alpha is a bounded local scalar. A finite partition of unity covers compact supports.']),
('Section 8: rational analytic barrier construction', ['Goodness supplies arbitrarily small affinoid neighborhoods, and rational domains with positive real radii give refinements W inside Int(A).','As mu decreases to 1, the compact sets W_mu decrease to W. If each met A outside Int(A), compactness would force W to meet that complement, a contradiction.','No common zero of f_i,g implies W_mu misses {g=0}. Thus W_mu is contained in the ordinary open Y=Int(A) intersect {g"'!=0}.'"','Even product-kernel convolution of max is smooth, convex and coordinatewise increasing. Jensen gives the lower bound max and kernel support gives the upper bound max+epsilon. A coordinate lower than the maximum by more than 2epsilon never maximizes after convolution and is ignored.','The constant a_0=-1 guarantees a finite maximum even when every f_i vanishes. Near each zero its log coordinate is ignored, making rho ordinary smooth. The other coordinates are log norms of analytic units; convex composition gives smooth psh.','At x, max(a_0,...,a_s)<=0, so rho(x)<=epsilon-t/2<0. If rho<=t/4 then every a_i<=3t/4, hence the sublevel lies in W_exp(3t/4), a compact subset of Y. It is closed there and therefore compact.','For the abstract relatively compact negative-sublevel assumption, shift by c>0 with rho(x)+c<0 and choose 0<delta<c. Then the new closed sublevel lies in the old negative sublevel and is compact.']),
('Section 8: analytic prime avoidance and explicit log-pole approximation', ['Locally the ideal of Z is not contained in any prime of an n-dimensional irreducible component. Finite prime avoidance gives f in that ideal but outside all those primes. Its zero set has dimension<n.','CLD 15.2.1(b) puts every compact smooth (n,n)-form support in the complement of {f=0}. The continuous real function log|f| is bounded on each such compact support, giving canonical local integrability.','For F=max(t,0) convolved with an even compact smooth kernel, convexity and 0<=F\\'<=1 hold, with F=0 for t<=-1 and F=t for t>=1.','Each F_p(log|f|) is constant -p on an ordinary neighborhood of {f=0}, and is a smooth convex function of a log-unit elsewhere. It is therefore smooth psh throughout.','The derivative with respect to p is -1+F\\'(t+p)<=0. For finite t the expression eventually equals t; at zeros it is -p. The sequence decreases to log|f| on a fixed neighborhood.','Section 7 applies to this stage-one locally approchable pole and every full-CPsh mixed trace; its polar set contains Z. No unknown current is pulled back or classified.']),
('Final assumption and dependency audit', ['Boundarylessness is used in Stokes and closedness of delta_X. Local differential separation is used for local positive-current sheaves, compact majorants and Radon measures.','Compact K_delta, neighborhood domains, a>=4 and smooth V supply the fixed compact C"'^2 integration-by-parts framework.'"','Full CPsh minimality supplies all closure arguments; local smooth approximation is assumed only for the polar function V, and explicitly constructed for log|f|.','Canonical integrability is used precisely in the final beta_0 bound; local sublevels turn the weighted integral into local integrability.','Goodness and separation support the analytic affinoid barrier construction; pure dimension gives the lower-dimensional zero set. Strictness is an allowed stronger analytic hypothesis and is not needed separately in the elementary barrier construction.','The weighted estimate is proved independently of CLD 8.4.3. The stronger full-CPsh polar conclusion is not inferred from the source theorem, which assumes local approchability of the u_i.'])]
for loc,steps in records:
 memory_append(r,'statement_checks',{'location':loc,'status':'checked','deduction_checks':steps,'critical_errors':[],'gaps':[],'references_pending':True})
print('Persisted 10 further sequential checks (Sections 5–8 and dependency audit).')
PY" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 379ms:
Persisted 10 further sequential checks (Sections 5–8 and dependency audit).

  ✓ Initialize memory and verify the proof sequentially.
  → Check all cited CLD statements and their applications.
  • Synthesize, validate, and write verification.json.
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

exec
/bin/zsh -lc "sed -n '240,370p' mcp/server.py && sed -n '1040,1072p' tmp/1204.6277v2-cld.txt && sed -n '9950,10030p' tmp/1204.6277v2-cld.txt && rg -n 'approchable|premier cran' tmp/1204.6277v2-cld.txt | head -n 30" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 0ms:

def _load_schema() -> Dict[str, Any]:
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"Schema not found: {SCHEMA_PATH}")
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        schema = json.load(handle)
    if not isinstance(schema, dict):
        raise ValueError("schema must be a JSON object")
    return schema


def validate_verification_output(payload: Dict[str, Any]) -> Dict[str, Any]:
    errors: List[str] = []

    try:
        schema = _load_schema()
    except Exception as exc:
        return {"valid": False, "errors": [f"schema load failed: {exc}"]}

    if Draft202012Validator is None:
        errors.append("jsonschema dependency is missing; cannot validate schema")
    else:
        validator = Draft202012Validator(schema)
        for error in validator.iter_errors(payload):
            path = ".".join(str(part) for part in error.path)
            if path:
                errors.append(f"schema error at '{path}': {error.message}")
            else:
                errors.append(f"schema error: {error.message}")

    report = payload.get("verification_report")
    verdict = payload.get("verdict")
    repair_hints = payload.get("repair_hints")

    critical_errors = []
    gaps = []
    if isinstance(report, dict):
        if isinstance(report.get("critical_errors"), list):
            critical_errors = report["critical_errors"]
        if isinstance(report.get("gaps"), list):
            gaps = report["gaps"]

    has_any_finding = len(critical_errors) + len(gaps) > 0

    if verdict == "correct":
        if has_any_finding:
            errors.append("verdict='correct' is invalid when critical_errors or gaps are non-empty")
        if repair_hints != "":
            errors.append("repair_hints must be empty when verdict='correct'")
    elif verdict == "wrong":
        if not has_any_finding:
            errors.append("verdict='wrong' requires at least one critical error or gap")
        if not isinstance(repair_hints, str) or not repair_hints.strip():
            errors.append("repair_hints must be non-empty when verdict='wrong'")
    else:
        errors.append("verdict must be 'correct' or 'wrong'")

    return {"valid": len(errors) == 0, "errors": errors}


def write_verification_output(run_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    validation = validate_verification_output(payload)
    if not validation["valid"]:
        raise ValueError("verification output validation failed: " + "; ".join(validation["errors"]))

    resolved_run_id = sanitize_run_id(run_id)
    output_dir = RESULTS_ROOT / resolved_run_id
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "verification.json"

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)

    memory_init(resolved_run_id)
    memory_append(
        resolved_run_id,
        "verification_reports",
        {
            "event_type": "final_report_written",
            "output_path": str(output_path),
            "verdict": payload.get("verdict"),
        },
    )

    return {
        "status": "ok",
        "run_id": resolved_run_id,
        "output_path": str(output_path),
    }


def build_mcp_app() -> Optional[Any]:
    if FastMCP is None:
        return None

    app = FastMCP("verification_agent")

    @app.tool(name="search_arxiv_theorems")
    def _tool_search_arxiv_theorems(query: str, num_results: int = 10) -> Dict[str, Any]:
        return search_arxiv_theorems(query=query, num_results=num_results)

    @app.tool(name="memory_init")
    def _tool_memory_init(run_id: str, meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return memory_init(run_id=run_id, meta=meta)

    @app.tool(name="memory_append")
    def _tool_memory_append(run_id: str, channel: str, record: Dict[str, Any]) -> Dict[str, Any]:
        return memory_append(run_id=run_id, channel=channel, record=record)

    @app.tool(name="memory_query")
    def _tool_memory_query(
        run_id: str,
        channel: str,
        filters: Optional[Dict[str, Any]] = None,
        contains: Optional[str] = None,
        limit: int = 100,
        reverse: bool = True,
    ) -> Dict[str, Any]:
        return memory_query(
            run_id=run_id,
            channel=channel,
            filters=filters,
            contains=contains,
            limit=limit,
            reverse=reverse,
        )

    @app.tool(name="validate_verification_output")
    def _tool_validate_verification_output(payload: Dict[str, Any]) -> Dict[str, Any]:
        return validate_verification_output(payload=payload)

La preuve est alors directe.

Proposition 1.2.13 ([84], corollaire 1.17). — Soit ω une (1, 1)-forme symétrique
définie positive sur V . Soit p un entier ⩾ 1. Dans l’espace des (p, p)-formes symétriques,
la forme ω p appartient à l’intérieur relatif du cône des (p, p)-formes fortement positives,
à l’intérieur du cône des (p, p)-formes symétriques positives, et à l’intérieur du cône
des (p, p)-formes faiblement positives.

   En particulier, les formes positives, et a fortiori les formes faiblement positives, en-
gendrent l’espace des formes symétriques. En revanche, Lagerberg donne dans [92] (re-
mark 4.1) un exemple de (2, 2)-forme faiblement positive sur R4 , non nulle, qui est
orthogonale à toute forme fortement positive ; ainsi les formes fortement positives en-
gendrent un sous-espace strict des (2, 2)-formes symétriques sur R4 .
Démonstration. — D’après la proposition 1.2.12, ω p est fortement positif.
   Nous allons démontrer que si α ∈ An−p,n−p (V ) est une forme faiblement positive
et symétrique telle que ω p ∧ α = 0, alors β ∧ α = 0 pour toute forme β fortement
positive. Cela entraîne la première partie de la proposition, par dualité. Cela entraîne
aussi la troisième partie. Soit en effet une forme α, fortement positive, orthogonale à ω p ;
démontrons qu’elle est nulle. Comme elle est également faiblement positive, elle est alors
orthogonale à toute forme fortement positive. Puisque α est fortement positive, elle est
somme de formes du type cα1 ∧ Jα1 ∧ · · · ∧ αn−p ∧ Jαn−p , où (α1 , . . . , αn−p ) est une
famille d’éléments de V ∗ , qu’on peut supposer libre, et c ∈ R+ . Par positivité, chacun
de ces termes est également orthogonal à toute fortement positive. Mais cela entraîne
qu’ils sont nuls : complétons en effet la famille (α1 , . . . , αn−p ) en une base (α1 , . . . , αn ) ;
en prenant β = αn−p+1 ∧ Jαn−p+1 ∧ . . . , on trouve cα1 ∧ Jα1 ∧ · · · ∧ αn ∧ Jαn ⩾ 0, d’où
c = 0.
   Démontrons maintenant l’énoncé admis. Soit α une forme symétrique faiblement po-
sitive de type (n − p, n − p) telle que ω p ∧ α = 0, soit β1 , . . . , βp dans V ∗ et soit
β = β1 ∧ Jβ1 ∧ · · · ∧ βp ∧ Jβp ; prouvons que β ∧ α = 0.
28 CHAPITRE 1. SUPERFORMES SUR UN ESPACE VECTORIEL RÉEL (D’APRÈS LAGERBERG)

   C’est évident si β1 , . . . , βp ne sont pas linéairement indépendantes, puisqu’alors β = 0.
Supposons donc que β1 , . . . , βp soient linéairement P     indépendantes et prolongeons cette
g(u1 , . . . , un )|U appartient à PshX,β+1 , c’est-à-dire à PshX,α .

Corollaire 8.2.3. — Soit α un ordinal et soit u1 , . . . , un des fonctions psh sur X,
appartenant à PshX,α . La fonction x 7→ max(u1 (x), . . . , un (x)) appartient à PshX,sup(α,1) ,
et est en particulier psh.
Démonstration. — D’après le lemme 1.7.6, la fonction t 7→ max(t1 , . . . , tn ) sur Rn est
limite uniforme de la famille de fonctions t 7→ log(eat1 + · · · + eatm )/a, lorsque a → +∞.
Ces fonctions sont lisses, convexes et croissantes en chaque variable. L’assertion découle
alors du corollaire précédent.

Corollaire 8.2.4. — Soit Ω un ouvert convexe de Rn et soit g : Ω → R une fonc-
tion convexe, croissante par rapport à chaque variable. Pour toute suite (u1 , . . . , un ) de
fonctions continues psh sur X, la fonction g(u1 , . . . , un ) est continue et psh. Plus précisé-
ment, si α est un ordinal tel que u1 , . . . , un appartiennent à CPshX,α , on a g(u1 , . . . , un ) ∈
CPshX,sup(1,α) .
Démonstration. — Comme g est convexe sur l’ouvert Ω, elle est continue ; puisque les ui
sont continues, la fonction g(u1 , . . . , un ) est continue. D’après la proposition 8.1.11, il
suffit de démontrer qu’elle appartient à PshX,sup(1,α) . D’après cette même proposition,
les fonctions uk appartiennent à PshX,α .
   Soit x ∈ X et soit Ω′ un voisinage ouvert convexe relativement compact de
(u1 (x), . . . , un (x)) dans Ω. Comme les ui sont continues, la partie U de X formée des
x ∈ X tels que (u1 (x), . . . , un (x)) ∈ Ω′ est ouverte. Par convolution, g|Ω′ est limite
uniforme d’une suite (gk ) de fonctions lisses qui sont convexes et croissantes en chaque
variable. D’après le corollaire précédent, g(u1 , . . . , un )|U appartient à PshX,sup(1,α) . Cela
conclut la démonstration.

Proposition 8.2.5. — Soit X un espace G-tropical affiné. Soit f : X → E une carte
tropicale, soit P un sous-espace paralinéaire de E contenant f (X) et soit v une fonction
convexe continue sur P (définition 1.10.5). Alors la fonction f ∗ v sur X est continue et
psh.
Démonstration. — Le sous-faisceau de CP formé des fonctions v telles que f ∗ v soit
psh contient les fonctions lisses telles que d′ d′′ v ⩾ 0 et est stable par limite uniforme. Il
contient donc le faisceau des fonctions convexes sur P . Cela démontre la proposition.

Définition 8.2.6. — Soit X un espace G-tropical affiné. On dit qu’une fonction u
sur X est tropicalement convexe si pour tout point x de X, il existe un voisinage U
de x, une carte tropicale f : U → E sur U , une partie paralinéaire P de Ttrop qui contient
f (U ) et une fonction convexe convexe v sur P tel que u|U = f ∗ v.
  Une fonction tropicalement convexe est psh.
                         § 8.3. FONCTIONS PSH ET COURANTS POSITIFS                             201

             § 8.3. FONCTIONS PSH ET COURANTS POSITIFS

 Soit X un espace tropical de niveau n. On suppose que X est sans bord ; en particulier,
X est localement différentiellement séparé, très riche et décent.

Proposition 8.3.1. — Soit u une fonction sur X à valeurs dans R∪{−∞}, localement
intégrable.
  a) Si u est plurisousharmonique, le courant d′ d′′ [u] est positif.
  b) Si u est lisse, elle est plurisousharmonique si et seulement si le courant d′ d′′ [u] est
positif.

Démonstration. — Pour tout U , notons P(U ) l’ensemble des fonctions localement inté-
grables u sur U telles que le courant d′ d′′ [u] sur U soit positif. Il est immédiat que
P est un sous-faisceau du faisceau des fonctions localement intégrables (à valeurs
dans R ∪ {−∞}) qui contient les fonctions lisses psh. Vérifions qu’il est également
stable par limite décroissante. Soit (un ) une suite décroissante de fonctions localement
intégrables sur un ouvert U de X qui converge simplement vers une fonction u locale-
ment intégrable sur U . Soit ω une (n, n)-forme lisse et à support compact       R sur U . Si ω est
positive,
      R    le théorème de  convergence      monotone  entraîne que  la  suite  (   un ω) converge
vers uω. Comme ω est différence de deux formes positives à support compact, cette
convergence est encore vérifiée. Cela démontre que la suite de courants ([un ]) converge
vers le courant [u]. Si de plus d′ d′′ [un ] ⩾ 0 pour tout n, alors d′ d′′ [u] ⩾ 0 par passage à
la limite. Par conséquent, P contient CPshX . Cela démontre l’assertion a).
   Supposons maintenant que u est lisse. Si u est plurisousharmonique, alors d′ d′′ [u] est
positif d’après a). Supposons inversement que le courant d′ d′′ [u] soit positif. Comme
c’est le courant associé à la forme lisse d′ d′′ u, cette forme est positive, d’après le corol-
laire 7.3.10. La fonction u appartient donc à CPshX (U ) par définition de ce cône.

Proposition 8.3.2. — Soit X l’espace tropical de niveau n associé à Rn . Soit U un
ouvert convexe de Rn , soit u une fonction sur U à valeurs dans R ∪ {−∞} qui n’est pas
identiquement −∞. Les assertions suivantes sont équivalentes :
  (i) La fonction u appartient à PshX ;
  (ii) La fonction u est à valeurs finies et est convexe ;
  (iii) La fonction u est localement intégrable et vérifie d′ d′′ [u] ⩾ 0 ;
  (iv) La fonction u appartient à CPshX,1 .
En particulier, les faisceaux sur X des fonctions psh, des fonctions continues psh et des
fonctions localement convexes coïncident.

Démonstration. — Soit U un ouvert de X et soit u une fonction lisse sur U telle que
9789:exemples de fonctions psh que nous connaissons appartiennent au premier cran de cette
9880:approchable si c’est une section du faisceau PshX,1 .
11171:   Soit u1 , . . . , un des fonctions psh continues sur X qui sont localement approchables,
11172:soit V une fonction psh localement approchable sur X. Si V est localement intégrable
11175:tions ui et la fonction V sont localement approchables, on peut donc supposer que les ui
11206:u1 , . . . , um des fonctions psh continues sur X qui sont localement approchables, soit α
11208:approchable sur X. Si V est localement intégrable sur X, est elle est localement intégrable
11218:u1 , . . . , um des fonctions psh continues sur X qui sont localement approchables, soit α
11220:approchable sur X. Si V est localement intégrable sur X, la mesure d′ d′′ u1 ∧. . . d′ d′′ um ∧α
11719:fonction lisse à support compact c sur X × Y est approchable par des fonctions de
23756:fonctions psh continues sur X qui sont localement approchables, soit V une fonction
23757:psh localement approchable sur X, soit α une forme lisse sur X. Si V est localement
23764:fonctions psh continues sur X qui sont localement approchables, soit α une forme lisse
23767:de type (n − m, n − m) sur X et soit V une fonction psh localement approchable sur X.
23774:fonctions psh continues sur X qui sont localement approchables, soit α une forme lisse
23788:résulte que log|f | est psh approchable. Comme son lieu polaire contient Y , le corollaire
25613:de sa métrique formelle canonique ; c’est une métrique globalement psh-approchable et
25614:tropicalement psh-approchable d’après le corollaire 17.8.7. L’isomorphisme L ≃ L1 ⊗L−1     2

web search: 
web search: 
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

exec
/bin/zsh -lc "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python - <<'PY'
import json
from pathlib import Path
from mcp.server import memory_append
r='20260831T204323Z_180a3827dff7'
base=Path('tmp')/r
refs=json.loads((base/'references.json').read_text())
checks={
'R01':('CLD 8.1.7–8.1.8, printed pp. 196–197','matched_and_applicable','CPsh is exactly the least subsheaf of real continuous functions containing smooth form-positive psh functions and closed under uniform limits. Local sheaf closure permits compact-local arguments. The transfinite construction is explicit.','The proof uses that minimality separately in variables and never assumes stabilization at stage one or the current-positive characterization of all continuous functions.'),
'R02':('CLD 8.5.1, printed pp. 205–206','matched_and_applicable','Positive currents are symmetric and can be multiplied by continuous coefficients using their Radon trace measures. The lemma requires positivity of T_j and locally uniform coefficient convergence; it does not assume closedness.','Section 2 decomposes every signed expression into finitely many positive converging currents before applying the lemma. The claimed extra continuous multiplier follows from the same decomposition, so no unsupported signed weak-convergence assertion is used.'),
'R03':('CLD 8.5.5, printed p. 207','matched_and_applicable','T is positive and separately closed; u is continuous psh in the full CPsh sense. The source proof itself uses the minimal-subsheaf argument.','All currents called S are positive and closed. Positive squares and exponential compositions are proved CPsh before their curvatures are invoked.'),
'R04':('CLD 8.7.2, printed pp. 209–210','matched_and_applicable','The multiplier u_0 is only continuous; the curvature factors u_i are continuous psh, and the background currents are positive and closed. Convergence is local uniform in coefficients and weak in currents.','All occurrences respect these hypotheses. Symmetry of the factors is also available from 8.7.4 and the cited 8.8.5; reordering dd(u_k S) is legitimate.'),
'R05':('CLD 8.8.4–8.8.5, printed pp. 211–212','matched_and_applicable','Dpsh is the vector-space subsheaf generated by CPsh, equivalently local differences of CPsh functions. Products in the cited multilinear extension are differences of positive currents. The extra Bedford–Taylor-current hypothesis is needed only for dependence on the individual curvature currents, not for forming the products.','The proof keeps the functions and distributional expressions, rather than relying on dependence only on their scalar curvature currents. Its square/product decomposition supplies precisely the finite positive decompositions required.'),
'R06':('CLD 6.5.2 and 7.2.4–7.2.12, printed pp. 148, 160–163','matched_and_applicable','Local differential separation gives local positivity and smooth compact cutoffs; 6.5.2 decomposes compact symmetric tests into differences of compact positive tests. Positive top-degree currents are Radon measures and positive currents have order zero. Compact supports lie in suitable paracompact neighborhoods.','All coefficient estimates are on fixed finite presentations and compact supports. Only positive currents or explicit differences thereof are treated as measures; no arbitrary order-zero-current classification is assumed. Domination uses the ordinary positive cone, not an invalid assertion that strongly positive forms span all symmetric forms.'),
'R07':('CLD 8.5.3 and its proof, printed p. 206','matched_and_applicable','The source cancellation pairs an antisymmetric combination of smooth cross derivatives with a symmetric current; closed means both d-prime and d-double-prime vanish.','For smooth h,rho the two cross products have equal top-degree pairing with Q by this symmetry. Extending in h via (2.4) and distributional continuity is justified separately in the submitted proof.'),
'R08':('CLD 8.8.1, printed p. 211','matched_and_applicable','Every ordinary smooth function is locally a difference of two ordinary smooth psh functions, and the source permits the same fixed tropical presentation on a compact domain.','A fixed decomposition of smooth rho suffices in (4.3); it is not a smooth approximation of the arbitrary dpsh variable.'),
'R09':('CLD 8.4.3 and preceding computation, printed pp. 203–205','matched_as_comparison_not_input','The printed proposition gives the same constant for smooth factors and a>=3. Its preceding derivative calculation writes a factor two uniformly although beta_n has only the scalar term.','The submitted proof explicitly strengthens the compact-neighborhood regularity hypotheses, uses a>=4, and recomputes the derivatives with b_n=1. Direct checking confirms that its coefficient bound and stated constant survive. It does not use the printed weighted estimate as an input.'),
'R10':('CLD 15.2.2–15.2.4, printed p. 423','matched_and_applicable','The corollary assumes local holomorphic separation. The preceding discussion includes topologically separated good spaces, because affinoid domains separate points by analytic norms.','The analytic spaces here are good and separated, so the locally differentially separated hypothesis used by the tropical argument is satisfied.'),
'R11':('CLD 16.9.1, printed p. 466','matched_as_comparison_not_input','The source printed wording indeed simultaneously says rho<0 on U and {rho<=0} compact. Its proof begins with affinoid and rational-domain neighborhoods with arbitrary positive real radii.','The submitted proof does not adopt the defective literal wording. It constructs rho on an ambient open Y, protects common numerator zeros with a constant branch, and proves compactness for a smaller positive closed sublevel by shrinking the relaxed rational domain.'),
'R12':('CLD 8.12.1, printed p. 223','matched_hypothesis_only','The geometric hypothesis is a basis of open neighborhoods with smooth psh rho such that {rho<0} is a relatively compact neighborhood of x. The full source theorem additionally assumes the continuous u_i are locally approchable.','The proof uses only that geometric hypothesis and converts it to K_delta compact by a small upward shift. It independently proves the stronger conclusion for full CPsh factors, rather than dropping the source local-approchability requirement in an application.'),
'R13':('CLD 15.2.1(a)–(b), printed p. 423','matched_and_applicable','Part (a) bounds form support by d_k(x)>=max(p,q); part (b) excludes analytic subsets of dimension below max(p,q), including inside analytic domains. This is a statement about form supports, not an assumption of nullity for an unknown current.','For compact smooth top forms p=q=n, their supports avoid the lower-dimensional zero set of f. Boundedness of log|f| on these compact supports proves precisely the canonical local integrability needed before Section 7 is applied.'),
'R14':('CLD 16.9.4 and its proof, printed p. 467','matched_as_comparison_not_input','The source nullity theorem assumes locally approchable continuous psh factors. Its proof chooses f by prime avoidance and notes canonical integrability of log|f|.','The submitted argument cites this only as context for the log-pole step. It provides an explicit decreasing sequence of smooth psh truncations for this particular pole, then uses its own full-CPsh Section 7, avoiding use of the stronger conclusion as a premise.'),
'R15':('CLD 11.1 introductory convention, 11.8.1 and 16.9.1 proof, printed pp. 291, 322, 466','matched_and_applicable','The standing complete ultrametric field may be trivially valued. CLD strictness differs from ordinary strictness in that case, and the ordinary strict class is contained in the CLD class. The rational refinement in 16.9.1 uses positive real radii.','The barrier uses only original-space analytic functions and real logarithmic constants. It never requires a nontrivial value group or a pullback of an unknown current. The statement makes the strictness convention explicit.')}
for rid,loc,query in refs:
 source,status,context,application=checks[rid]
 memory_append(r,'reference_checks',{'reference_id':rid,'location':loc,'referenced_statement':query,'status':status,'context_expansion':context,'application_check':application,'arxiv_match_found':False,'arxiv_search_status':'endpoint unavailable: DNS resolution failure; full-statement query attempted and recorded','web_match_found':True,'web_search_status':'Same full-statement web queries performed; exact source checked by web open and local text of identical v2 manuscript','source_url':'https://arxiv.org/pdf/1204.6277v2','source_location':source,'local_source':'tmp/1204.6277v2-cld.txt','critical_errors':[],'gaps':[]})
memory_append(r,'failed_checks',{'type':'reference_search_transport_failure','mathematical_issue':False,'reference_ids':[x[0] for x in refs],'issue':'search_arxiv_theorems endpoint leansearch.net could not resolve in the local runtime.','resolution':'Required built-in web fallback used; all cited statements located and checked in CLD arXiv:1204.6277v2. No reference remains unverified.'})
memory_append(r,'events',{'event':'sequential_and_reference_checks_completed','statement_items':18,'reference_items':15,'critical_errors':0,'gaps':0,'note':'Previously recorded references_pending flags are historical; all dependencies are now resolved by the reference_checks channel.'})
print('Persisted all 15 reference checks; no unresolved mathematical findings.')
PY" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 369ms:
Persisted all 15 reference checks; no unresolved mathematical findings.

  ✓ Initialize memory and verify the proof sequentially.
  ✓ Check all cited CLD statements and their applications.
  → Synthesize, validate, and write verification.json.
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

2026-08-31T20:55:35.433534Z  WARN codex_core::responses_retry: stream disconnected - retrying sampling request (1/5 in 217ms)... turn_id=01a0598f-fec4-7c91-a3c2-7bd79f0b7b49 retries=1 max_retries=5 sampling_error=stream disconnected before completion: idle timeout waiting for websocket
exec
/bin/zsh -lc "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python - <<'PY'
from mcp.server import memory_query
r='20260831T204323Z_180a3827dff7'
for ch in ['statement_checks','reference_checks','failed_checks']:
 data=memory_query(r,ch,limit=100,reverse=False)
 print(ch, data['count'])
 for entry in data['items']:
  record=entry['record']
  print({'location':record.get('location',record.get('type')),'status':record.get('status'),'critical_errors':record.get('critical_errors',[]),'gaps':record.get('gaps',[]),'resolution':record.get('resolution')})
PY" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 325ms:
statement_checks 18
{'location': 'Section 1: hypotheses and target extraction', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 2: convex composition and vector-cone operations', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 2: equations (2.1)–(2.3)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 2: equation (2.4) and smooth equation (2.5)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 3: positivity for every dpsh function', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 3: exponential identities (3.1)–(3.3)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 4: positivity polynomial and measure Schwarz (4.1)–(4.2)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 4: mixed derivative identity and smooth form compatibility (4.3)–(4.4)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 5: support, positivity and barrier derivatives (5.1)–(5.2)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 5: compact C^2 test-form approximation', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 6: degrees and integration by parts (6.1)–(6.2)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 6: weighted Schwarz and coefficient comparison (6.3)–(6.5)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 6: exponential substitution and recursion (6.6)–(6.9)', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 7: fixed smooth polar truncations and monotone limit', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 7: arbitrary smooth traces (7.2), including endpoints', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 8: rational analytic barrier construction', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 8: analytic prime avoidance and explicit log-pole approximation', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Final assumption and dependency audit', 'status': 'checked', 'critical_errors': [], 'gaps': [], 'resolution': None}
reference_checks 15
{'location': 'Section 1; Section 2–4', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 1; Section 2–3', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 1; Section 2–3', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 1; Section 6–7', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 1; Section 2', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 1; Section 2; Section 5; Section 7', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 4, equation (4.3)', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 4, equation (4.3)', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 1; Section 5–6', 'status': 'matched_as_comparison_not_input', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 1; Section 8', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 8, comparison with printed barrier', 'status': 'matched_as_comparison_not_input', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 8, abstract barrier shift', 'status': 'matched_hypothesis_only', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 8, analytic zero-set support', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 8, analytic log-pole comparison', 'status': 'matched_as_comparison_not_input', 'critical_errors': [], 'gaps': [], 'resolution': None}
{'location': 'Section 8, field convention and rational neighborhoods', 'status': 'matched_and_applicable', 'critical_errors': [], 'gaps': [], 'resolution': None}
failed_checks 1
{'location': 'reference_search_transport_failure', 'status': None, 'critical_errors': [], 'gaps': [], 'resolution': 'Required built-in web fallback used; all cited statements located and checked in CLD arXiv:1204.6277v2. No reference remains unverified.'}

diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]

codex
I found no critical errors or gaps in Sections 1–8. The analytic construction handles common numerator zeros and trivial valuation, and the explicit smooth truncations justify the log-pole application. I’m writing and validating the required JSON report now.
apply patch
patch: completed
/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json
new file mode 100644
index 0000000000000000000000000000000000000000..d21074a929456f89d01c6ddcac3b836ff81e8bc4
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json
@@ -0,0 +1,9 @@
+{
+  "verification_report": {
+    "summary": "Sequential verification of Sections 1–8 found no critical errors or gaps. The square/product decompositions give controlled differences of positive currents, making the energy continuity argument valid. Separate-variable subsheaf closure establishes energy positivity and the exponential identities for the full CPsh sheaf without assuming a common smooth approximation sequence. The mixed-energy Schwarz inequality, integration-by-parts signs, compact C^2 coefficient passage, and endpoint factor b_n=1 are correct. The coefficient comparison and exponential cancellation yield exactly the stated constant C(k,a), including the zero-norm case. Applying the estimate with each smooth polar truncation fixed, then using monotone convergence, proves local integrability; positive-form domination extends it to total variations of arbitrary smooth traces. The rational-domain construction supplies the required compact positive sublevels over trivially valued fields as well, while the constant branch handles simultaneous numerator zeros. Prime avoidance, canonical integrability of log|f|, and its explicit decreasing smooth psh truncations establish the analytic-subset consequence. The theorem-search endpoint was unavailable; the cited definitions and hypotheses were checked directly through the web fallback in the [CLD manuscript](https://arxiv.org/pdf/1204.6277v2). The proof does not import the source's local-approchability restriction on all factors or rely on its defective endpoint calculation and barrier wording.",
+    "critical_errors": [],
+    "gaps": []
+  },
+  "verdict": "correct",
+  "repair_hints": ""
+}

exec
/bin/zsh -lc "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/tmp/verification-venv/bin/python - <<'PY'
import json
from pathlib import Path
from mcp.server import memory_query, memory_append, validate_verification_output, write_verification_output
run='20260831T204323Z_180a3827dff7'
payload=json.loads((Path('tmp')/run/'verification_payload.json').read_text())
errors=[]
gaps=[]
for channel in ['statement_checks','reference_checks']:
 for item in memory_query(run,channel,limit=1000,reverse=False)['items']:
  rec=item['record']
  errors.extend(rec.get('critical_errors',[]))
  gaps.extend(rec.get('gaps',[]))
  if rec.get('critical_error'):
   errors.append(rec['critical_error'])
assert payload['verification_report']['critical_errors']==errors
assert payload['verification_report']['gaps']==gaps
validation=validate_verification_output(payload)
assert validation['valid'],validation
memory_append(run,'verification_reports',{'event_type':'synthesized_verified_report','payload':payload,'validation':validation,'statement_checks_count':18,'reference_checks_count':15})
result=write_verification_output(run,payload)
written=json.loads(Path(result['output_path']).read_text())
assert written==payload
print(json.dumps({'validation':validation,'write_result':result,'readback_matches':True},indent=2))
PY" in /Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification
 succeeded in 417ms:
{
  "validation": {
    "valid": true,
    "errors": []
  },
  "write_result": {
    "status": "ok",
    "run_id": "20260831T204323Z_180a3827dff7",
    "output_path": "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/agents/verification/results/20260831T204323Z_180a3827dff7/verification.json"
  },
  "readback_matches": true
}

  ✓ Initialize memory and verify the proof sequentially.
  ✓ Check all cited CLD statements and their applications.
  ✓ Synthesize, validate, and write verification.json.
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json
new file mode 100644
index 0000000000000000000000000000000000000000..d21074a929456f89d01c6ddcac3b836ff81e8bc4
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json
@@ -0,0 +1,9 @@
+{
+  "verification_report": {
+    "summary": "Sequential verification of Sections 1–8 found no critical errors or gaps. The square/product decompositions give controlled differences of positive currents, making the energy continuity argument valid. Separate-variable subsheaf closure establishes energy positivity and the exponential identities for the full CPsh sheaf without assuming a common smooth approximation sequence. The mixed-energy Schwarz inequality, integration-by-parts signs, compact C^2 coefficient passage, and endpoint factor b_n=1 are correct. The coefficient comparison and exponential cancellation yield exactly the stated constant C(k,a), including the zero-norm case. Applying the estimate with each smooth polar truncation fixed, then using monotone convergence, proves local integrability; positive-form domination extends it to total variations of arbitrary smooth traces. The rational-domain construction supplies the required compact positive sublevels over trivially valued fields as well, while the constant branch handles simultaneous numerator zeros. Prime avoidance, canonical integrability of log|f|, and its explicit decreasing smooth psh truncations establish the analytic-subset consequence. The theorem-search endpoint was unavailable; the cited definitions and hypotheses were checked directly through the web fallback in the [CLD manuscript](https://arxiv.org/pdf/1204.6277v2). The proof does not import the source's local-approchability restriction on all factors or rely on its defective endpoint calculation and barrier wording.",
+    "critical_errors": [],
+    "gaps": []
+  },
+  "verdict": "correct",
+  "repair_hints": ""
+}

codex
{
  "verification_report": {
    "summary": "Sequential verification of Sections 1–8 found no critical errors or gaps. The square/product decompositions give controlled differences of positive currents, making the energy continuity argument valid. Separate-variable subsheaf closure establishes energy positivity and the exponential identities for the full CPsh sheaf without assuming a common smooth approximation sequence. The mixed-energy Schwarz inequality, integration-by-parts signs, compact C^2 coefficient passage, and endpoint factor b_n=1 are correct. The coefficient comparison and exponential cancellation yield exactly the stated constant C(k,a), including the zero-norm case. Applying the estimate with each smooth polar truncation fixed, then using monotone convergence, proves local integrability; positive-form domination extends it to total variations of arbitrary smooth traces. The rational-domain construction supplies the required compact positive sublevels over trivially valued fields as well, while the constant branch handles simultaneous numerator zeros. Prime avoidance, canonical integrability of log|f|, and its explicit decreasing smooth psh truncations establish the analytic-subset consequence. The theorem-search endpoint was unavailable; the cited definitions and hypotheses were checked directly through the web fallback in the [CLD manuscript](https://arxiv.org/pdf/1204.6277v2). The proof does not import the source's local-approchability restriction on all factors or rely on its defective endpoint calculation and barrier wording.",
    "critical_errors": [],
    "gaps": []
  },
  "verdict": "correct",
  "repair_hints": ""
}
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
new file mode 100644
index 0000000000000000000000000000000000000000..887996bbd18914b02a76e7c092efbcb7397ac6b3
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/references.json
@@ -0,0 +1,77 @@
+[
+  [
+    "R01",
+    "Section 1; Section 2–4",
+    "CLD 8.1.7–8.1.8: CPsh_X is the least subsheaf of real continuous functions containing every smooth function u with d'd''u >= 0 and stable under uniform limits; it is obtained by transfinite local uniform closure and need not equal the first approximation stage."
+  ],
+  [
+    "R02",
+    "Section 1; Section 2–3",
+    "CLD 8.5.1: If positive currents T_j converge weakly to T and continuous functions u_j converge locally uniformly to u, then u_j T_j converges weakly to u T."
+  ],
+  [
+    "R03",
+    "Section 1; Section 2–3",
+    "CLD 8.5.5: On a boundaryless tropical space, if T is a positive closed current and u is a continuous plurisubharmonic function in CPsh, then d'd''(uT) is positive and closed."
+  ],
+  [
+    "R04",
+    "Section 1; Section 6–7",
+    "CLD 8.7.2: For positive closed currents T_j converging weakly to T and locally uniformly convergent continuous u_0j,u_1j,...,u_qj with u_ij continuous psh for i>=1, the currents u_0j d'd''u_1j wedge ... wedge d'd''u_qj wedge T_j converge to the corresponding product."
+  ],
+  [
+    "R05",
+    "Section 1; Section 2",
+    "CLD 8.8.4–8.8.5: The sheaf of differences of continuous plurisubharmonic functions contains smooth functions; Bedford–Taylor products extend uniquely multilinearly to dpsh factors and a continuous coefficient, producing differences of positive currents."
+  ],
+  [
+    "R06",
+    "Section 1; Section 2; Section 5; Section 7",
+    "CLD 6.5.2 and 7.2.4–7.2.12: Local differential separation yields smooth partitions of unity, compact positive test majorants, continuous multiplication of positive currents, and Radon measures for top-degree traces."
+  ],
+  [
+    "R07",
+    "Section 4, equation (4.3)",
+    "CLD 8.5.3: For a symmetric separately closed current S and a smooth symmetric form alpha, d'd''(alpha wedge S)=d'd''alpha wedge S; the cross terms in the proof form an antisymmetric form and pair to zero with S."
+  ],
+  [
+    "R08",
+    "Section 4, equation (4.3)",
+    "CLD 8.8.1: Every smooth real function on a tropical space is locally the difference of two smooth plurisubharmonic functions; in a fixed compact tropical presentation the two functions may use the same presentation."
+  ],
+  [
+    "R09",
+    "Section 1; Section 5–6",
+    "CLD 8.4.3: For beta_k=(-rho)^(k+a)(d'd''rho)^(n-k)+(k+a)(-rho)^(k+a-1)d'rho wedge d''rho wedge(d'd''rho)^(n-k-1), omitting the second term for k=n, the weighted inequality has C(k,a)=(4e)^k a^(-1)(k+a)(a+2)...(a+k+1) for a>=3."
+  ],
+  [
+    "R10",
+    "Section 1; Section 8",
+    "CLD 15.2.4: A locally holomorphically separated k-analytic space, in particular a good k-analytic space, is locally differentially separated."
+  ],
+  [
+    "R11",
+    "Section 8, comparison with printed barrier",
+    "CLD 16.9.1: Every point of a boundaryless analytic n-space over a complete ultrametric field has a basis of open neighborhoods carrying a smooth strictly negative plurisubharmonic function rho with relatively compact nonpositive sublevel."
+  ],
+  [
+    "R12",
+    "Section 8, abstract barrier shift",
+    "CLD 8.12.1: For a boundaryless tropical space where every point has arbitrarily small neighborhoods with a smooth psh function rho and relatively compact negative sublevel {rho<0}, weighted Bedford–Taylor measures with continuous psh factors do not charge poles of integrable psh functions."
+  ],
+  [
+    "R13",
+    "Section 8, analytic zero-set support",
+    "CLD 15.2.1(b): On a topologically separated k-analytic space, if a smooth form of type (p,q) has x in its support, then max(p,q)<=d_k(x); hence smooth (n,n)-forms vanish near analytic subsets of dimension less than n."
+  ],
+  [
+    "R14",
+    "Section 8, analytic log-pole comparison",
+    "CLD 16.9.4: On a boundaryless analytic n-space, the Radon measure d'd''u_1 wedge ... wedge d'd''u_m wedge alpha for locally approchable continuous psh u_i and smooth alpha of complementary degree gives zero mass to every analytic subset of dimension less than n; its proof uses prime avoidance and local integrability of log|f|."
+  ],
+  [
+    "R15",
+    "Section 8, field convention and rational neighborhoods",
+    "Chambert-Loir Ducros Formes différentielles réelles et courants sur les espaces de Berkovich: the base field k is complete non-Archimedean and may be trivially valued; affinoid neighborhoods admit rational domain refinements with real positive radii."
+  ]
+]
diff --git a/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json b/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json
new file mode 100644
index 0000000000000000000000000000000000000000..d21074a929456f89d01c6ddcac3b836ff81e8bc4
--- /dev/null
+++ b/agents/verification/tmp/20260831T204323Z_180a3827dff7/verification_payload.json
@@ -0,0 +1,9 @@
+{
+  "verification_report": {
+    "summary": "Sequential verification of Sections 1–8 found no critical errors or gaps. The square/product decompositions give controlled differences of positive currents, making the energy continuity argument valid. Separate-variable subsheaf closure establishes energy positivity and the exponential identities for the full CPsh sheaf without assuming a common smooth approximation sequence. The mixed-energy Schwarz inequality, integration-by-parts signs, compact C^2 coefficient passage, and endpoint factor b_n=1 are correct. The coefficient comparison and exponential cancellation yield exactly the stated constant C(k,a), including the zero-norm case. Applying the estimate with each smooth polar truncation fixed, then using monotone convergence, proves local integrability; positive-form domination extends it to total variations of arbitrary smooth traces. The rational-domain construction supplies the required compact positive sublevels over trivially valued fields as well, while the constant branch handles simultaneous numerator zeros. Prime avoidance, canonical integrability of log|f|, and its explicit decreasing smooth psh truncations establish the analytic-subset consequence. The theorem-search endpoint was unavailable; the cited definitions and hypotheses were checked directly through the web fallback in the [CLD manuscript](https://arxiv.org/pdf/1204.6277v2). The proof does not import the source's local-approchability restriction on all factors or rely on its defective endpoint calculation and barrier wording.",
+    "critical_errors": [],
+    "gaps": []
+  },
+  "verdict": "correct",
+  "repair_hints": ""
+}

tokens used
119 365
{
  "verification_report": {
    "summary": "Sequential verification of Sections 1–8 found no critical errors or gaps. The square/product decompositions give controlled differences of positive currents, making the energy continuity argument valid. Separate-variable subsheaf closure establishes energy positivity and the exponential identities for the full CPsh sheaf without assuming a common smooth approximation sequence. The mixed-energy Schwarz inequality, integration-by-parts signs, compact C^2 coefficient passage, and endpoint factor b_n=1 are correct. The coefficient comparison and exponential cancellation yield exactly the stated constant C(k,a), including the zero-norm case. Applying the estimate with each smooth polar truncation fixed, then using monotone convergence, proves local integrability; positive-form domination extends it to total variations of arbitrary smooth traces. The rational-domain construction supplies the required compact positive sublevels over trivially valued fields as well, while the constant branch handles simultaneous numerator zeros. Prime avoidance, canonical integrability of log|f|, and its explicit decreasing smooth psh truncations establish the analytic-subset consequence. The theorem-search endpoint was unavailable; the cited definitions and hypotheses were checked directly through the web fallback in the [CLD manuscript](https://arxiv.org/pdf/1204.6277v2). The proof does not import the source's local-approchability restriction on all factors or rely on its defective endpoint calculation and barrier wording.",
    "critical_errors": [],
    "gaps": []
  },
  "verdict": "correct",
  "repair_hints": ""
}
