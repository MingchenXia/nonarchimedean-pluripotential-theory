Use the base-K quotient of n2. This note independently constructs the bounded ordinary-local operator, verifies the checkpoint for EVERY real N>=1 and proves the new constant-energy and measure-tail consequences. These are unverified mathematical drafts under the named analytic foundations, not a counterexample to the original P16.7 equation.

Write DD=d'd'', x_j=-log|z_j|, q=|x|^2/2 and theta=DDq on a deck sheet. Its change under x->x+n is n dot x+|n|^2/2, smooth and DD-null. Define C_theta as the continuous real functions u such that q+u is locally on ORDINARY opens a locally uniform limit of ordinary CLD smooth functions with middle-positive Hessian. This explicit generated bounded class is not identified with a larger psh theory.

The coefficient-space correction is essential. In an m-dimensional moment presentation, symmetric (p,p) coefficients are symmetric matrices on Lambda^p R^m, with the exterior sign; their dimension is d(d+1)/2, d=binomial(m,p). Middle positivity is PSD. For m=4,p=2, d=6 and the coefficient dimension is 21. Strong squares ww^t satisfy Q(w)=w12 w34-w13 w24+w14 w23=0 and span EXACTLY 20 dimensions. Indeed Q=0 characterizes decomposable bivectors, by rank two of their skew matrices. Put x=(w12,w13,w14), y=(w34,-w24,w23), so Q=x dot y. A quadratic form vanishing on Q=0 has no pure-x or pure-y part, and its remaining part x^t B y vanishes whenever y is perpendicular to x. Hence B^t x is proportional to every x; testing basis vectors and their pairwise sums makes B scalar. The annihilator is exactly the one-dimensional span of Q. The witness e12+e34 has Q=1. Thus the strong cone is NOT an ambient order-unit cone.

For the middle cone, a Euclidean positive form lambda has lambda^p represented by p! I. On compact tropical support every symmetric smooth coefficient matrix B satisfies -C lambda^p<=B<=C lambda^p. A nonnegative cutoff equal to one on that support decomposes a test into two middle-positive compact tests inside the SAME ordinary open. Finite moment-chart localization globalizes this. CLD-v2 1.2.6–13 and 6.5.1–3 give these precise middle-cone/decomposition inputs; 15.1.1 and 15.2.3–9 supply ordinary moments, cutoffs and density. Their full applied statements and immediate proofs were freshly read. The good separated boundaryless X meets their local-separation hypotheses. No strong domination from 7.2.9 is used.

For a symmetric middle-positive current T and positive test eta, phi-><T,phi eta> is a positive scalar functional. A cutoff plateau bounds it by the compact supremum norm. Smooth scalar density and Riesz give a Radon measure. Decompose beta=eta_+-eta_- and subtract their coefficient measures; equality on smooth scalars proves independence and support in supp(beta). Antisymmetric tests pair to zero. Continuous multiplication is defined and satisfies

|<bT,beta>|<=sup_K|b| <T,eta_++eta_->,

where K is their compact support union. If positive T_j->T weakly and b_j->b locally uniformly, approximate b on K by a smooth g within epsilon and split b_jT_j-bT=(b_j-g)T_j+g(T_j-T)+(g-b)T. The first/last terms obey the bound with bounded positive-current masses, the middle tends to zero; then let epsilon vanish. This reconstructs CLD-v2 7.2.8 and 7.2.11–12 using the corrected middle order unit.

For closed symmetric T and smooth h, complementary-degree Leibniz gives DD(hT)=DDh wedge T. Arbitrary continuous multiplication is not claimed to preserve closedness. For u,v in C_theta, set alpha_u=theta+DD[u] and locally, f=q+u,g=q+v,

B(u,v)=DD(f DD[g]).

Smooth-positive approximants give DDg_j->DDg and f_j DDg_j->f DDg by the preceding lemma. Differentiating proves convergence of their positive symmetric smooth mixed products, independently of approximation. Smooth DD-null changes glue the products on ordinary overlaps. Differences inherit bilinearity by subtraction. The applied bounded recursive units are CLD-v2 8.5.1/3/5, 8.7.1–4 and 8.8.1, 8.8.4–8. No arbitrary-current density, upward recognition or 8.6.7 continuous-multiplier closedness is used.

Canonical integration in CLD-v2 14.3.1–5 and 14.5.2–3 retains actual generic Artinian lengths and calibration degrees. The full immediate proofs were read; their deeper Berkovich/calibration foundations remain cited. CLD-v2 15.7.1–2 gives canonical tropical level equal to pure analytic dimension, with the analytic boundary, on a topologically separated space. Thus the positive top current is an actual analytic Radon measure. Our identity and translated identity moments have saturated Z^2 lattice and actual degree one. The exterior factor is 2!, so theta^2=2 i_*dx for probability Haar dx. RAW mass is two.

Globally B(u,v)=theta wedge alpha_v+DD(u alpha_v), and theta wedge alpha_v=theta^2+DD(v theta). Pairing differentiated terms with 1 on compact boundaryless X makes them zero; hence each B has mass two. Define MA_theta(u)=B(u,u). The multiplication argument proves continuity under uniform convergence WITHIN C_theta. Dini handles decreasing limits only when still continuous and in that class. Smooth convex nondecreasing regularization proves convexity and finite-max stability. For w=max(u,v-epsilon), ordinary locality and equal mass give

MA_theta(v){u<v-epsilon}<=2-MA_theta(u){u>v-epsilon}=MA_theta(u){u<=v-epsilon}.

Let epsilon decrease to zero; both sets increase to {u<v}. This proves bounded comparison, not full-E1 comparison or uniqueness.

Let G(y)=y^2/2-y/2+1/12 on [0,1], extended periodically. Its mean is zero and G''=dy-delta_0. Put u0=-G(x1)-G(x2). Positive periodic convolution gives smooth-positive approximants, so

A=alpha_u0, A^2=2 delta_i(0),
theta wedge A=i_*(dy tensor delta_0+delta_0 tensor dy).

The range of u0 is [-1/6,1/12], and u0=-1/6 on the ENTIRE fibre F=tau^-1(0). On its ordinary sheet V={|x_j|<1/4}, for every real N>=1 put r=exp(-N), ell_j=log max(r,|z_j-1|), b_j=log max(1,|z_j|), d_j=ell_j-b_j and D_N=max(d1,d2). Real convex thresholds and Gauss seminorms permit arbitrary positive r; no strict-affinoid assertion for radius r is needed. Each d_j<=0 and is zero if |z_j|!=1. Thus D_N vanishes off F and extends continuously by zero outside V. Its negative locus W={|z1-1|<1,|z2-1|<1} is ORDINARY open, contained in F.

For U_N=u0+D_N, direct calculation gives on V

q+U_N=max(ell1+b2,b1+ell2)-(1/2)log|z1z2|-1/6.

Near a zero of z_j-1 the truncated ell_j is constant; omit that inactive coordinate. Elsewhere the involved analytic functions are invertible and their logarithms give ordinary moment charts. Sums/maxima are convex functions of these logarithms, while the last logarithm is pluriharmonic. Softmax or convolution gives actual ordinary smooth-positive approximants. No logarithmic chart crosses a zero. Consequently U_N belongs to the EXACT C_theta.

In W put w_j=z_j-1. Its weight is log max(r,|w1|,|w2|)-1/6. The bidisc Gauss point xi_N with both w-radii r is in W. There |z_j-1|=r<1, whereas the original Gauss point i(0) has value one; xi_N is off the original section. Near xi_N the w_j are invertible and form a translated identity moment with degree one and saturated lattice. In y_j=log|w_j|+N, regularize max(0,y1,y2) by epsilon log(1+exp(y1/epsilon)+exp(y2/epsilon)). Its gradient is a diffeomorphism onto the triangle p_j>0,p1+p2<1. Change of variables gives integral det(Hess)=1/2; rescaling gives concentration at zero. Multiplication by 2! gives mass one. CLD-v2 5.8.1–6 places the smooth measures on the actual translated Gauss section; continuity of that section, checked by seminorm evaluation as in 12.1.2–5, gives convergence against analytic continuous tests. Operator continuity identifies the atom. Away from the vertex the weight is locally affine or depends on one coordinate after affine subtraction; near a zero omit its inactive log. Its square therefore vanishes there. Hence MA_theta(U_N)|W=delta_xi_N, with total mass two. The other mass one outside W is NOT identified.

On W both q and u0 are constant, so theta|W=A|W=0. D_N is zero on the complement, including the boundary. Coefficient measures and ordinary locality give D_N theta=D_N A=0 globally, without nonsmooth integration by parts. Therefore theta wedge alpha_U_N=theta wedge A. Off F, U_N=u0 on ordinary neighborhoods, so MA_theta(U_N) is supported on F. D_N also vanishes on the original Gauss section. For

E_theta(u)=(1/3) integral u(theta^2+theta wedge alpha_u+MA_theta(u)),

the COMPLETE three integrals for U_N are 0, -1/6 and -1/3-N. Thus E_theta(U_N)=-1/6-N/3. At the rigid y=(1,1), U_N(y)=-1/6-N, giving E_theta(U_N)-2U_N(y)=1/6+5N/3. The mass-two rigid atom therefore has infinite C_theta dual energy. Its restricted separable dual is 1/6, as independently computed in n4. An extension inherits the infinity ONLY after verified containment of C_theta and identity of bounded energy.

The NEW energy-bounded test is V_(a,N)=u0+aD_N=(1-a)u0+aU_N, 0<=a<=1. Bilinearity for differences gives A wedge DD D_N=DD(D_N A)=0. Expansion yields

MA_theta(V_(a,N))=(1-a^2)MA_theta(u0)+a^2 MA_theta(U_N),
theta wedge alpha_V=theta wedge A.

Both right-hand measures are actual bounded measures supported on F. D_N vanishes at i(0) and integrates to -N against MA(U_N). The energy integrals are therefore 0, -1/6 and -1/3-a^3N. Hence

E_theta(V_(a,N))=-1/6-a^3N/3,
V_(a,N)(y)=-1/6-aN,
sup V_(a,N)=1/12.

The supremum follows from D_N<=0 and a maximum of u0 outside F. Along this entire admissible pencil, dE/da=-a^2N=integral D_N MA(V_(a,N)); this is pencil variation, not all-direction variation.

Choose a=N^(-1/3). Then E=-1/2, while V(y)=-1/6-N^(2/3). Subtracting the supremum gives sup v_N=0, E(v_N)=-2/3 and v_N(y)=-1/4-N^(2/3). A uniformly relatively compact family of continuous functions on compact X is uniformly bounded. Thus this normalized energy-bounded family is NOT uniformly relatively compact. Unlike the unscaled family, its energies are bounded. This disproves only uniform compactness in C_theta; weaker useful compactness, unbounded E1 membership and unbounded continuity remain open. All these potentials have the same skeleton restriction, so theta-reference skeleton L1 is not a separated topology even on this energy-bounded family.

There is also a NEW necessary measure condition. For positive Radon mu of RAW mass two assume M=E*_C_theta(mu)<infinity. Put J0=E_theta(u0)-integral u0 dmu and C=M-J0>=0. Let L_N=integral(-D_N)dmu. Testing V gives

aL_N-a^3N/3<=C for every a in [0,1].

For N>3C/2, L_N>N would contradict the a=1 inequality. Hence L_N<=N. If L_N>0, maximize at a=sqrt(L_N/N), obtaining (2/3)L_N^(3/2)/sqrt(N)<=C. Thus

L_N<=(3C/2)^(2/3)N^(1/3),
mu(B_N)<=(3C/2)^(2/3)N^(-2/3), for N>=1 and N>3C/2,
B_N={|z1-1|<=exp(-N),|z2-1|<=exp(-N)}.

The second inequality follows from -D_N=N on B_N. If C=0, the tests force L_N=0. The bidiscs decrease to y, so mu({y})=0. This is necessary, not sufficient, and supplies no existence theorem. It tests actual branch support missed by skeletal marginals.

Artifacts: notes/n3.md, P16.7-standalone-paper.tex, proof-companion.md, source-application-ledger.md and evidence/diagnostics.json. Rerun `python scripts/diagnostics.py`; its finite exact algebra does not prove the universal analytic statements above.