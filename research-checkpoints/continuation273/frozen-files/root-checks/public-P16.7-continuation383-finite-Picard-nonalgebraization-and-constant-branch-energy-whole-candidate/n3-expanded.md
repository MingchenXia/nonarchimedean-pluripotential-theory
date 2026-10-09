# n3. Ordinary bounded products and a constant-energy branch obstruction

Use the actual base-K quotient X of n2, with K=C((s)), |s|=exp(-1/8), t=s^8 and periods (t,2),(3,t). No supplied note is a premise. This note constructs its bounded ordinary-local operator anew, verifies the checkpoint for EVERY real N>=1, and proves two new consequences: normalized constant-energy potentials fail uniform compactness, and finite bounded dual energy imposes a quantitative branch-tail condition. Neither conclusion is a counterexample to the literal P16.7 equation.

Let DD=d'd''. On a deck sheet put x_j=-log|z_j|, q=|x|^2/2 and theta=DDq. Under x->x+n the potential changes by n dot x+|n|^2/2, a smooth DD-null function, so theta is a global real analytic datum. Define C_theta to consist of continuous real u for which q+u is locally on ORDINARY opens a locally uniform limit of ordinary CLD smooth functions having positive semidefinite Hessian. This is an explicit bounded generated class, without recognition of any larger psh class.

We first justify the bounded calculus rather than importing it. In an m-dimensional moment presentation, symmetric (p,p) coefficients, with the usual sign, are symmetric matrices on Lambda^p R^m. Their dimension is d(d+1)/2, d=binomial(m,p). Middle positivity is the PSD cone. For m=4,p=2, d=6 and the coefficient space has dimension 21. Strong squares ww^t satisfy Q(w)=w12 w34-w13 w24+w14 w23=0. Their span has dimension EXACTLY 20: Q=0 characterizes decomposable bivectors, by expressing a bivector with a nonzero coefficient as a wedge of two vectors (equivalently its skew matrix has rank two). With x=(w12,w13,w14), y=(w34,-w24,w23), Q=x dot y. A quadratic form R vanishing for x dot y=0 has no pure-x or pure-y part, by setting the other variable zero. Write its remaining part x^t B y. For each x, vanishing for every y perpendicular to x makes B^t x a multiple of x; testing basis vectors and their pairwise sums makes B scalar. Hence the annihilator is precisely the one-dimensional span of Q. In particular (e12+e34)(e12+e34)^t has Q=1 and is outside that span. Strong squares supply NO ambient order unit in this presentation.

The middle cone supplies the needed order unit. If lambda is the Euclidean positive (1,1) form, lambda^p has coefficient matrix p! I. Every symmetric smooth coefficient matrix B on a compact tropical support satisfies -C lambda^p<=B<=C lambda^p. A nonnegative smooth cutoff, equal to one on that support and compactly supported in the same ordinary open, decomposes the test form into two middle-positive compactly supported forms. Local moment representations, a finite cover of its compact support, and a smooth partition of unity globalize this. The positive supports may grow but stay compact inside the specified open. CLD-v2 1.2.6-13 and 6.5.1-3 state the middle-cone and decomposition results; 15.1.1 and 15.2.3-9 supply ordinary moment charts, cutoffs and density on locally holomorphically separated spaces. X satisfies these hypotheses because it is good, separated and boundaryless. The directly applied statements and immediate proofs are recorded locally; no strong-domination assertion from 7.2.9 is used.

For a symmetric middle-positive current T and a positive test eta, the functional phi-><T,phi eta> is positive. A cutoff plateau bounds it by ||phi||_infinity times <T,chi eta> on compact sets. Smooth scalar density and Riesz give a Radon measure. If beta=eta_+-eta_-, subtract the two scalar measures. Equality on smooth scalars proves independence of the decomposition and support in supp(beta); antisymmetric tests pair to zero. Continuous multiplication is thereby defined and obeys

|<bT,beta>| <= sup_K|b| <T,eta_++eta_->,

where K is the compact union of their supports. If positive T_j->T weakly and b_j->b locally uniformly, approximate b on K by a smooth g within epsilon. Split b_j T_j-bT into (b_j-g)T_j+g(T_j-T)+(g-b)T. The first and last terms are bounded by the displayed inequality, with a bounded sequence <T_j,eta_++eta_->; the middle term tends to zero. Let epsilon tend to zero. This proves multiplication continuity on the fixed bounded class. These are the exact scalar and coefficient-measure arguments of CLD-v2 7.2.8 and 7.2.11-12, here reconstructed with the middle order unit.

For closed symmetric T and smooth h, the complementary-degree Leibniz rule gives DD(hT)=DDh wedge T. Arbitrary continuous multipliers need not preserve closedness. For u,v in C_theta define alpha_u=theta+DD[u] and, locally with f=q+u,g=q+v,

B(u,v)=DD(f DD[g]).

Smooth-positive approximants give DDg_j->DDg; multiplication continuity gives f_j DDg_j->f DDg. Differentiating identifies B as the limit of the positive smooth mixed products, independently of the approximants. It is symmetric and positive, and the smooth DD-null change rule glues it on ordinary overlaps. Differences of such potentials inherit bilinearity by subtraction. No arbitrary-current density or upward recognition is asserted. The applied bounded recursive units are CLD-v2 8.5.1, 8.5.3, 8.5.5, 8.7.1-4 and 8.8.1, 8.8.4-8. The overbroad continuous-multiplier closedness in 8.6.7 is unnecessary.

Canonical integration of CLD-v2 14.3.1-5 and 14.5.2-3 retains all generic Artinian lengths and calibration degrees. CLD-v2 15.7.1-2 gives the canonical tropical level equal to pure analytic dimension on a topologically separated analytic space, with its analytic boundary. Thus this positive top current on the boundaryless surface is an actual analytic Radon measure. These deep analytic integration foundations are cited; their full dependency trees are not newly proved. The identity torus moment and translated identity moments used below have saturated lattice Z^2 and actual degree one. The exterior-product factor is 2!, so theta^2=2 i_*dx, with dx probability Haar measure on R^2/Z^2, and the RAW reference mass is two. It cannot be replaced silently by probability mass.

Globally B(u,v)=theta wedge alpha_v+DD(u alpha_v), and theta wedge alpha_v=theta^2+DD(v theta). Pairing the differentiated terms with 1 on compact boundaryless X makes them zero. Hence every B(u,v) has mass two. Define MA_theta(u)=B(u,u). The multiplication argument proves uniform continuity within C_theta. Dini only gives decreasing continuity when the limit is still continuous and in this class. Convex nondecreasing regularizations of max preserve Hessian positivity by the smooth chain rule, so C_theta is convex and closed under finite maxima. With w=max(u,v-epsilon), ordinary locality on its two strict regions and equal mass give

MA_theta(v){u<v-epsilon} <= 2-MA_theta(u){u>v-epsilon}=MA_theta(u){u<=v-epsilon}.

As epsilon decreases to zero both sets on the sides increase to {u<v}. This proves bounded comparison, without full-E1 comparison or uniqueness.

Let G(y)=y^2/2-y/2+1/12 on [0,1], periodically extended. Its mean is zero, G''=dy-delta_0, and u0=-G(x1)-G(x2) has range [-1/6,1/12]. Nonnegative periodic convolutions give smooth-positive approximants to q+u0. Their diagonal squares and the continuity just proved give

A=alpha_u0, MA_theta(u0)=A^2=2 delta_i(0),
theta wedge A=i_*(dy tensor delta_0+delta_0 tensor dy).

The entire fibre F=tau^-1(0) has u0=-1/6. Choose its ordinary sheet V={|x_j|<1/4}. For EVERY real N>=1 put r=exp(-N), ell_j=log max(r,|z_j-1|), b_j=log max(1,|z_j|), d_j=ell_j-b_j and D_N=max(d1,d2). Real constants in convex functions and Gauss seminorms permit these radii even when r is outside |K*|; no new strict-affinoid assertion for radius r is needed. Each d_j<=0 and is zero if |z_j|!=1. Thus D_N is zero off F and extends continuously by zero outside V. Its negative locus

W={|z1-1|<1, |z2-1|<1}

is ORDINARY open, contained in F. On V one directly computes

q+U_N=max(ell1+b2,b1+ell2)-(1/2)log|z1 z2|-1/6, U_N=u0+D_N.

Every ell_j is constant near a zero of z_j-1; omit that inactive coordinate on that neighborhood. Elsewhere the analytic functions involved are invertible and their logarithms define ordinary moment charts. Sums and maxima in the display are convex functions of those logarithms, and the last logarithm is smooth pluriharmonic. Softmax or convolution supplies actual ordinary smooth-positive approximants. No logarithmic chart crosses a zero. This proves U_N in the EXACT C_theta, not an unspecified current-defined or generated larger class.

In W write w_j=z_j-1. The local weight is log max(r,|w1|,|w2|)-1/6. The bidisc Gauss seminorm xi_N with both w-radii r is an actual analytic point of W, where |z_j-1|=r<1. At the original Gauss point i(0) these values are one, so xi_N is off that section. Near xi_N, w1,w2 are invertible and the translated identity moment has lattice Z^2 and degree one. With y_j=log|w_j|+N, regularize max(0,y1,y2) by epsilon log(1+exp(y1/epsilon)+exp(y2/epsilon)). Its gradient is a diffeomorphism onto the interior of the triangle {p_j>0,p1+p2<1}; hence integral det(Hess)=1/2 by change of variables. Rescaling y=epsilon Y gives concentration at zero. The calibrated exterior square multiplies by 2!, giving mass one. Its smooth measures live on the translated Gauss section by CLD-v2 5.8.1-6; its continuity, established by direct evaluation of Gauss seminorms (12.1.2-5), gives convergence against continuous ANALYTIC tests. Operator continuity identifies the analytic atom. At every other point of the invertible-w chart the weight is locally affine or, after subtracting an affine function, depends on a single coordinate, so its square is zero. Near w_j=0 omit the inactive log, again giving rank at most one. Therefore MA_theta(U_N)|W=delta_xi_N. Its total mass is two. The remaining mass one outside W is deliberately NOT identified.

On W, q and u0 are constant, so theta|W=A|W=0. The scalar D_N is zero on its complement, including its boundary. The coefficient-measure calculus gives D_N theta=D_N A=0 globally by ordinary locality, not a nonsmooth integration-by-parts assertion. Therefore theta wedge alpha_U_N=theta wedge A. Outside F, U_N=u0 on ordinary neighborhoods, so MA_theta(U_N) is supported on F. Also D_N vanishes everywhere on the original Gauss section. The complete three-term energy is

E_theta(u)=(1/3) integral u(theta^2+theta wedge alpha_u+MA_theta(u)),
integral U_N theta^2=0,
integral U_N(theta wedge alpha_U_N)=-1/6,
integral U_N MA_theta(U_N)=-1/3-N,
E_theta(U_N)=-1/6-N/3.

At the rigid point y=(1,1), U_N(y)=-1/6-N and E_theta(U_N)-2U_N(y)=1/6+5N/3. Thus E*_C_theta(2 delta_y)=infinity. For comparison, circle potentials with dy+h''>=0 are h=-G*nu+c; their energy is e(h)=integral h dy-(1/2) integral |h'|^2 dy. Convolution proves integral h d(dy+h'')=integral h dy-integral |h'|^2 and e(k)-e(h)=integral(k-h)d(dy+h'')-(1/2) integral|k'-h'|^2. For separable sums their bounded mixed energy is 2(e(h1)+e(h2)). The rigid mass-two objective only sees the two delta_0 marginals, is maximized at u0, and equals -1/6-2(-1/6)=1/6. This restricted dual does not supply full admissibility. Any extension inherits the infinite rigid dual ONLY after verifying containment of C_theta and identity of bounded energy.

Here is the new energy-bounded obstruction. For 0<=a<=1 let V_(a,N)=u0+aD_N=(1-a)u0+aU_N, which belongs to C_theta. Bilinearity for differences gives A wedge DD D_N=DD(D_N A)=0. Expanding alpha_V^2 therefore yields

MA_theta(V_(a,N))=(1-a^2)MA_theta(u0)+a^2 MA_theta(U_N),
theta wedge alpha_V=theta wedge A.

Both terms on the right are actual bounded measures. Their support is F, where u0=-1/6; D_N vanishes at i(0), and its integral against MA_theta(U_N) is -N. Hence the three energy integrals are 0, -1/6, and -1/3-a^3 N. Consequently

E_theta(V_(a,N))=-1/6-a^3 N/3,
V_(a,N)(y)=-1/6-aN,
sup V_(a,N)=1/12.

The last equality follows because D_N<=0 and a maximum of u0 lies outside F. Along this entire admissible pencil dE/da=-a^2 N=integral D_N MA_theta(V_(a,N)); this is a verified pencil first variation, not all-direction variation.

Choose a=N^(-1/3). Then E_theta(V_(a,N))=-1/2 for all real N>=1, while V_(a,N)(y)=-1/6-N^(2/3). Subtracting the supremum gives sup v_N=0, E_theta(v_N)=-2/3 and v_N(y)=-1/4-N^(2/3). A uniformly relatively compact set of continuous functions on compact X is uniformly bounded, so this normalized, energy-bounded family is NOT uniformly relatively compact. This improves the unscaled U_N test, whose energies tend to minus infinity. It disproves only uniform compactness in this explicit bounded class. It does not disprove compactness in a useful weaker topology, construct an unbounded E1 element, or prove any unbounded continuity theorem. All these v_N have the same Gauss-skeleton restriction; theta-reference L1 alone therefore cannot separate this family, even under the energy bound.

There is also a new necessary measure condition. For a positive Radon mu of RAW mass two, set M=E*_C_theta(mu) and assume M finite. Put J0=E_theta(u0)-integral u0 dmu and C=M-J0>=0. For L_N=integral(-D_N)dmu, testing V_(a,N) gives

a L_N-a^3 N/3<=C for EVERY a in [0,1].

If N>3C/2 and L_N>N, choosing a=1 contradicts this inequality. Thus L_N<=N. If L_N>0 its maximizing a is sqrt(L_N/N), and the optimized inequality is (2/3)L_N^(3/2)/sqrt(N)<=C. Therefore

L_N <= (3C/2)^(2/3) N^(1/3),
mu(B_N) <= (3C/2)^(2/3) N^(-2/3), N>=1 and N>3C/2,
B_N={|z1-1|<=exp(-N), |z2-1|<=exp(-N)}.

Indeed -D_N=N on this closed branch bidisc. For C=0 the inequalities force L_N=0. The bidiscs decrease to y, so continuity from above also gives mu({y})=0. This is a necessary condition, not a sufficient finite-energy characterization or an existence theorem. It is an all-analytic-support test at this specified branch; the skeletal marginal condition alone misses it.

Artifacts: notes/n3.md, P16.7-standalone-paper.tex, proof-companion.md, source-application-ledger.md and evidence/diagnostics.json. Rerun own finite rational/Plucker checks with `python scripts/diagnostics.py`; those checks are exhaustive only in their finite declared domains and do not establish universal analytic correctness. Support: n2 (the quotient geometry only).
