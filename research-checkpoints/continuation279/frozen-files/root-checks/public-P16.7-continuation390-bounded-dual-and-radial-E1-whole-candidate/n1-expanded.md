# Bounded integration by parts, variation, and the tangent inequality

This is an unverified proof draft. The theorem below concerns the entire specified bounded class, with all its ordinary analytic directions. It does not concern an unconstructed all-direction unbounded class.

Let X be a compact, good, separated, smooth, boundaryless analytic surface with its canonical CLD integration, and let theta be a smooth positive closed (1,1)-form with local smooth positive potentials q. Define C_theta by requiring that u is continuous and that q+u, on a neighborhood of each point in the ordinary topology, is a locally uniform limit of ordinary smooth functions with middle-positive Hessian. Write DD=d'd'', alpha_u=theta+DD[u], B(u,v)=alpha_u wedge alpha_v, and V=integral theta^2. Then the genuine local bounded products satisfy

E(u)=(1/3) integral u(theta^2+theta wedge alpha_u+B(u,u)),
E(u+C)=E(u)+VC,
d/dt E(u+t(v-u))=integral(v-u)B(u+t(v-u),u+t(v-u)),
E(v)<=E(u)+integral(v-u)B(u,u).

Here all t in [0,1] are allowed, with the endpoint derivatives interpreted one-sided. In particular E is concave on all of C_theta. We prove the integration by parts needed for these identities without assuming global smooth positive approximation.

The analytic infrastructure is exactly the ordinary current/form calculus of CLD, arXiv:1204.6277v2 (submitted 25 July 2025): compact smooth cutoffs and finite partitions in prescribed ordinary neighborhoods; density of smooth scalars on compact supports; canonical integration on a topologically separated pure two-dimensional boundaryless analytic space; symmetry and positive wedge calculus. The applicable statements are 6.5.2, 7.2.8/11/13, 7.7.1-8, 8.5.1/3/5, 8.7.1/2/4, and 15.7.1-2. Their hypotheses are retained. Only the smooth-factor Leibniz rule is used. The erroneous general continuous-multiplier closedness assertion 8.6.7 is not used.

First reconstruct the bounded products. In a moment presentation, symmetric (p,p) coefficients are symmetric matrices on the exterior coefficient space. Middle positivity is the PSD cone; the pth power of a Euclidean positive (1,1)-form is p! times its identity matrix. Thus every smooth symmetric test on a compact support is a difference of two compact middle-positive tests, using a cutoff and a finite partition. A positive symmetric current consequently has coefficient Radon measures: a scalar test times a positive form gives a positive functional bounded by the scalar sup norm, and Riesz representation applies. Independence of decompositions follows from equality on smooth tests and density. If positive T_j converge weakly and b_j converge locally uniformly, then b_j T_j converge to b T. Indeed choose a smooth g uniformly close to b and split the difference into (b_j-g)T_j+g(T_j-T)+(g-b)T; the first and last terms are bounded by the positive test masses times the uniform errors.

Locally let p=q+u and r=q+v. Set B(u,v)=DD(p DD[r]). Simultaneous local smooth positive approximants, the preceding multiplication lemma, and smooth closed-factor Leibniz show that this is the limit of the positive smooth mixed products. It is symmetric, positive, closed, local, independent of approximants, and continuous when the potentials converge locally uniformly within the declared class. Smooth DD-null changes of q glue it. Globally B(u,v)=theta wedge alpha_v+DD(u alpha_v), and theta wedge alpha_v=theta^2+DD(v theta). Testing the differentiated currents with the constant 1 gives integral B(u,v)=V. None of these assertions requires a global positive approximant. Finite convex combinations are in C_theta by intersecting finitely many local approximation neighborhoods. The same argument and a smooth convex nondecreasing regularization prove finite-max stability.

Now fix a positive symmetric closed (1,1)-current T, held fixed throughout the next argument. Locally let f be a difference of two functions individually uniformly approximable by smooth positive weights. Choose smooth differences f_i=p_i-r_i converging uniformly on compact subsets. The signed measure L_T f=DD(fT) is the difference of the positive measures DD(pT) and DD(rT). For smooth p_i, DD(p_i T)=DD p_i wedge T by smooth closed-factor Leibniz. Positivity, distributional convergence, and coefficient multiplication give L_T f_i -> L_T f and f_i L_T f_i -> f L_T f, locally as currents; local signed variations are uniformly bounded. For example, if chi is a smooth nonnegative compact cutoff, then

integral chi DD p_i wedge T=integral p_i DD chi wedge T,

which is bounded uniformly because p_i are locally uniformly bounded and DD chi wedge T is a fixed finite signed measure. A cutoff equal to one on a smaller compact set bounds the entire positive measure there.

For smooth a define Q_T(a)=d'a wedge d''a wedge T. It is a positive measure; its bilinear polarization is symmetric because T annihilates antisymmetric (1,1)-tests. Smooth Leibniz gives

Q_T(a)=(1/2)DD(a^2T)-a L_T a,
integral chi Q_T(a)=(1/2)integral a^2 DD chi wedge T-integral chi a L_T a.

Apply this with a=f_i-f_j. If eta is its sup norm on a fixed compact neighborhood containing the support of chi, the positive decompositions of L_T f_i and L_T f_j just bounded give

0<=integral chi Q_T(f_i-f_j)<=C_chi(eta+eta^2).

The constant is independent of i,j. The same identity gives a uniform bound on integral chi Q_T(f_i). For any smooth compact (1,0)-test beta, coefficient PSD positivity gives Cauchy-Schwarz between beta and d''a, with chi=1 on the test support. This can be seen by applying T to (lambda beta+d'a) wedge J(lambda beta+d'a), integrating, and requiring the resulting quadratic to be nonnegative for every real lambda. The bound is the square root of the corresponding two positive quadratic masses. It is valid also for beta multiplied by any smooth bounded scalar.

Consequently d''f_i wedge T are Cauchy when tested against beta, and, for another such difference g, f_i d''g_i wedge T are Cauchy: split their difference into (f_i-f_j)d''g_i wedge T and f_j d''(g_i-g_j) wedge T. The first is bounded by the uniform error in f times the bounded local gradient mass of g; the second tends to zero by the displayed estimate and the boundedness of f_j. Interleaving any two approximation sequences proves independence. The resulting currents f d''g wedge T glue on overlaps, since the same estimates apply on every smaller compact subset of an overlap. This argument uses no positive approximation of T and no global approximation of f or g.

For smooth f_i,g_i, symmetry cancels the cross terms and yields

d'(f_i d''g_i wedge T-g_i d''f_i wedge T)
    =f_i L_T g_i-g_i L_T f_i.

Pass to the limit using the established convergence on each side. The local currents glue, so this is a global identity for global f,g of the stated local difference class. On compact X, test with 1 to obtain the required symmetry

integral f DD(gT)=integral g DD(fT).

Also the local limits of Q_T(f_i) equal Q_T(f)=(1/2)DD(f^2T)-f DD(fT), a positive top measure. In particular

integral f DD(fT)=-integral Q_T(f)<=0.

Notice that f^2T is merely a well-defined coefficient product. It is never asserted to be closed, nor is f^2 asserted to be psh. This is why the proof does not invoke 8.6.7.

Every u in C_theta is locally the difference (q+u)-q; hence these identities apply to global u,v and to T=theta or alpha_w for any w in C_theta. They also apply by subtraction to their signed differences. The identification DD((u-v)alpha_w)=B(u,w)-B(v,w) follows directly from the reconstructed recursive products.

Put f=v-u, u_t=u+tf and alpha_t=alpha_{u_t}. Difference multilinearity makes E(u_t) a polynomial of degree at most three. Differentiate its three terms and integrate by parts with T=theta and alpha_t:

E'(u_t)=(1/3) integral f[theta^2+theta alpha_t+alpha_t^2+(alpha_t-theta)(theta+2alpha_t)]
        =integral f alpha_t^2.

There are no limiting derivative assertions in this polynomial calculation. Differentiating again gives

E''(u_t)=2 integral f DD(f alpha_t)=-2 integral Q_{alpha_t}(f)<=0.

Thus the derivative decreases along the segment. Integrating it from 0 to 1 proves the tangent inequality for every u,v in the entire C_theta. Constants cancel in its dual objective when a measure has raw mass V. This closes the bounded first-variation/concavity gate under the stated analytic current infrastructure, without solving an unbounded all-direction gate.

There is also comparison for the ENTIRE bounded class. For epsilon>0 set w=max(u,v-epsilon), which belongs to C_theta by the local convex regularization already proved. Locality on its two strict open regions and positivity imply

V=integral MA(w)>=integral_{u>v-epsilon} MA(u)+integral_{u<v-epsilon} MA(v).

Subtracting the first term from V yields integral_{u<v-epsilon} MA(v)<=integral_{u<=v-epsilon} MA(u). As epsilon decreases to zero, both sets increase to {u<v}. Continuity from below for finite measures proves integral_{u<v} MA(v)<=integral_{u<v} MA(u). Possible mass on each intermediate equality set causes no difficulty, because it was included on the right and its increasing union is exactly the final strict set. No global approximation or unbounded comparison theorem is used.

Artifacts: n1.md, P16.7-bounded-dual-paper.tex, proof-companion.md and source-application-ledger.md. Rerun the own integrity and finite algebra diagnostics with `python identity_audit.py` and `python diagnostics.py`. Neither program establishes the universal analytic argument above. Support: none.
