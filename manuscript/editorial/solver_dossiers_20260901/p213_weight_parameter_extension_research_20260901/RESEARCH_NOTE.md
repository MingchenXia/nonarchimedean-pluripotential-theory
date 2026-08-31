# Real weight parameters and structured coefficient regularization

Date: 1 September 2026.
Status: new research draft, not independently verified, not production verified, not integrated.

## 1. Target and dependency boundary

The full-CPsh weighted/polar note dated 1 September uses integer a>=4 to make every displayed weight a C^2 coefficient form. Its exact Sections 1-8 received a positive mathematical Rethlas report, but the recorded execution-compliance exception prevents a clean production gate. This note does not change that status.

The proposed improvement keeps every space, support, potential and auxiliary-function hypothesis of that note and replaces integer a>=4 in the weighted inequality by real a>1. It uses the full-CPsh one-factor theorem, symmetry, order-zero products, the energy pairing, its positivity/Schwarz inequality and exponential identity from that note's Sections 2-4. Those inputs must be included in any dependency-closed verification; none is claimed newly verified here.

This improvement concerns the weight parameter and its boundary regularization. It is not a full P21.3 theorem, an unrestricted polar-potential regularization theorem, or a novelty claim. The primary comparison is CLD, arXiv:1204.6277v2, Sections 8.4 and 8.12. The source's printed compact-barrier wording and endpoint derivative are not assumed.

## 2. Precise weighted assertion

Let Y be a boundaryless locally differentially separated CLD tropical space of pure dimension n>=1. Let rho be smooth psh on Y, and suppose K_delta={rho<=delta} is compact for some delta>0. Assume U={rho<0} is nonempty. All factors below are defined on a neighborhood of K_delta.

Put r=max(-rho,0), theta=d'd''rho and eta=d'rho wedge d''rho. For a real a>1, set, for 0<=k<=n,

    beta_k = r^(k+a) theta^(n-k)
          +(k+a) r^(k+a-1) eta theta^(n-k-1),             (2.1)

omitting the second summand when k=n. These are continuous, positive coefficient forms with support in the compact set K_0. They need not have C^2 coefficients. Their products with positive or finite differences of positive order-zero currents are defined by local coefficient measures, independently of a chart representation by the usual smooth-uniform extension.

Let V be smooth psh on a neighborhood of K_delta and negative on U. For u_1,...,u_k in the full minimal locally uniform-closure sheaf CPsh, define

    J_k = integral_U (-V) beta_k wedge dd u_1 ... dd u_k,
    C(k,a) = product_(j=1)^k [4 exp(1)(j+a)(j+a+1)/(j+a-1)].

The claim is

    J_k <= C(k,a) product_(j=1)^k ||u_j||_U
                          integral_U (-V) beta_0.         (2.2)

The empty product is one. All integrals are finite because K_delta is compact, V and the u_j are continuous near it, and the currents have locally finite coefficient measures. The claim remains local when the original hypotheses and factors are restricted to a neighborhood containing this same K_delta.

## 3. The actual regularization

Fix 1<=k<=n, write l=k+a, q=n-k, and b=2 if q>0, b=1 if q=0. Then l>2. The single function

    F(t)=max(-t,0)^l

is C^2 on the real line: its first two derivatives are

    F'(t)=-l max(-t,0)^(l-1),
    F''(t)=l(l-1) max(-t,0)^(l-2),

and both vanish continuously at t=0. No assertion that t_+^integer is C^integer is made.

Choose a nonnegative smooth convolution kernel of integral one, supported in [-1,1], and let F_epsilon be its epsilon-regularization. Then F_epsilon is smooth, nonnegative, and nonincreasing. It vanishes for t>=epsilon. On each compact real interval, F_epsilon and its first two derivatives converge uniformly to F, F', F''.

Define the smooth forms

    beta_(k,epsilon)
       = F_epsilon(rho) theta^q
         -F_epsilon'(rho) eta theta^(q-1)                 (3.1)

when q>0, and beta_(n,epsilon)=F_epsilon(rho) when q=0. For 0<epsilon<delta these forms all have support in the ONE compact K_delta. Both scalar coefficients in (3.1) are nonnegative, so these forms are positive, though positivity of the regularization is not needed for the integration-by-parts identity.

Because theta is separately closed, d''eta=-theta wedge d''rho, and d''rho wedge eta=0, direct differentiation gives

    d'' beta_(k,epsilon)
       = b F_epsilon'(rho) d''rho theta^q,                (3.2)
    dd beta_(k,epsilon)
       = b [F_epsilon'(rho) theta^(q+1)
                      +F_epsilon''(rho) eta theta^q].     (3.3)

For q=0 these are just the derivatives of F_epsilon(rho), with b=1. For q>0, the two copies of F_epsilon' arise respectively from differentiating the first summand of (3.1) and from differentiating eta in the second. The derivative of that second summand's scalar coefficient wedges to zero against eta.

Thus beta_(k,epsilon), d''beta_(k,epsilon), and dd beta_(k,epsilon) converge in continuous coefficient norms on a finite fixed tropical-chart cover of K_delta. In particular the last two limits are

    d'' beta_k = -b l r^(l-1) d''rho theta^q,              (3.4)
    dd beta_k = b l[-r^(l-1)theta^(q+1)
                         +(l-1)r^(l-2)eta theta^q].       (3.5)

The meaning of the differential in (3.5) is also distributional, by convergence on smooth tests. It is represented by the displayed continuous coefficient form. There is no measure supported on {rho=0}: F' and F'' have the stated continuous vanishing, and the approximating expressions converge uniformly.

It is important that we regularize F and use its DERIVATIVE in the second summand. We do not require convergence of every second partial derivative of every coefficient of beta_k. Such a claim would be false for some 1<a<=2. The exterior-derivative identities (3.2)-(3.3) only use F, F' and F'', so no third derivative is needed.

The case k=0 needs no differentiated regularization anywhere in the argument. Formula (2.1) defines beta_0 continuously since a-1>0. Positivity, compact support and coefficient-measure pairing suffice for J_0 and for every coefficient comparison below.

## 4. Passing the integration-by-parts identity

Let

    S=dd u_1 ... dd u_(k-1),  Q=theta^q wedge S.

Then S is positive separately closed, and Q has top-minus-one bidegree. Fix a positive CPsh function z near K_delta. All products below use the established energy calculus; in particular Gamma_Q(z,rho) is a signed Radon measure. Its total variation is finite on K_delta.

With beta_(k,epsilon) smooth, the product rule, symmetry and Stokes give

    integral (-V) beta_(k,epsilon) wedge dd(zS)
      = integral z[V dd beta_(k,epsilon)
                         -dd V wedge beta_(k,epsilon)] wedge S
        +2 integral V d'(zS) wedge d''beta_(k,epsilon).    (4.1)

Only test coefficients have been regularized. There is no smooth approximation sequence for an arbitrary CPsh z or u_j.

The first integral in (4.1) converges because dd(zS) is positive and order zero. The two terms in the first integral on its right converge because S is order zero and the coefficients in (3.1),(3.3) converge uniformly on fixed compact charts. Multiplication by the bounded continuous z and smooth V is harmless.

For the remaining term, the top-degree mixed-energy identity with the smooth function rho gives exactly

    integral V d'(zS) wedge d''beta_(k,epsilon)
      = b integral V F_epsilon'(rho) Gamma_Q(z,rho).      (4.2)

This identity follows from (3.2) and
d'(zQ) wedge d''rho = Gamma_Q(z,rho). It is not an assertion that the order-one current d'(zS) acts continuously on arbitrary C^0 forms. The right side of (4.2) converges because the one FIXED signed measure has finite variation and F_epsilon' converges uniformly. Therefore (4.1) passes to

    J_k(z)
      = integral z[V dd beta_k-dd V wedge beta_k] wedge S
        +2 b l integral_U (-V) r^(l-1) Gamma_Q(z,rho).     (4.3)

All integrals in this passage may first be taken on Y; their limiting integrands have support in K_0. The weights appearing on {rho=0} vanish since l>2, so the limiting expressions equal the displayed U-integrals. V is not required to be negative on the epsilon-collar outside U, as no inequality was applied there.

## 5. Coefficient comparison and cancellation

The energy Schwarz inequality, with continuous weights extended by zero at r=0, yields the signed-measure inequality

    2 b l (-V) r^(l-1) Gamma_Q(z,rho)
       <= (-V) r^l z^(-1) Gamma_Q(z)
          +b^2 l^2 (-V) z r^(l-2) Gamma_Q(rho).           (5.1)

Here z has a positive minimum on K_delta, Gamma_Q(rho)=eta wedge Q, and r^(l-2) is continuous and vanishes at zero. The inequality is applied only on U, where -V>0.

The -z dd V wedge beta_k wedge S term in (4.3) is nonpositive. Adding the eta coefficient in (5.1) to -dd beta_k gives

    b l r^(l-1) theta^(q+1)
     +b l[(b-1)l+1] r^(l-2) eta theta^q.                (5.2)

On the other hand,

    beta_(k-1)=r^(l-1)theta^(q+1)
                         +(l-1)r^(l-2)eta theta^q.

For b=2, both coefficients in (5.2) are bounded by

    c_l beta_(k-1),  c_l=2l(l+1)/(l-1).

For b=1, the coefficients are l and l; they satisfy the same bound because l>2. Thus

    J_k(z) <= c_l ||z||_U J_(k-1)
                +integral_U (-V)r^l z^(-1)Gamma_Q(z).   (5.3)

For arbitrary u=u_k, put M=||u||_U. If M=0, u=0 on U and locality gives J_k=0. If M>0, use z=exp(Bu), B>0. The established full-sheaf exponential energy identity, multiplied by beta_k, gives

    J_k(z) >= B exp(-BM) J_k(u)
                +integral_U (-V)r^l z^(-1)Gamma_Q(z).   (5.4)

The energy contribution from the second summand of beta_k is nonnegative, so discarding it is legitimate. The comparison uses u>=-M only on U. Subtracting the identical finite energy term from (5.3) and (5.4) gives

    J_k(u) <= c_l B^(-1) exp(2BM) J_(k-1).

Taking B=1/(2M) proves the recursion

    J_k <= [4 exp(1)(k+a)(k+a+1)/(k+a-1)]
                      ||u_k||_U J_(k-1),

and iteration proves (2.2). The algebra requires no integer parameter and the structured regularization used precisely l>2, which follows from a>1 for every k>=1.

## 6. Consequences and limits

If verified, this argument preserves the existing book's choice a=3 and its numerical constant while allowing all real a>1. It repairs the k=n factor and the boundary coefficient justification without weakening that existing parameter range.

The full-CPsh polar argument may still choose the conservative a=4; hence this extension is not necessary for that conclusion. Alternatively beta_0 remains a bounded continuous positive coefficient form, dominated on fixed compact charts by a smooth positive top form, so the same canonical local-integrability hypothesis on the auxiliary V suffices for its weighted integral. No derivatives of beta_0 or of the nonsmooth auxiliary V are taken.

No assertion is made at a=1, no sharpness claim is made, and no new function-class equality or regularization theorem is asserted. This draft must receive an independent audit and correctly authorized dependency-closed production verification before any live integration.
