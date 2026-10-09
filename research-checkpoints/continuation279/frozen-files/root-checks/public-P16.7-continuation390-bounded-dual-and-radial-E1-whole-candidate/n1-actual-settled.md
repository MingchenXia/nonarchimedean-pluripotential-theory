This is an unverified proof draft.

Let X be a compact, good, separated, smooth, boundaryless analytic surface with canonical CLD integration. Let theta be a smooth positive closed (1,1)-form with local smooth positive potentials q. Define C_theta to consist of continuous u such that, on an ordinary neighborhood of each point, q+u is a locally uniform limit of ordinary smooth functions with middle-positive Hessian. Write DD=d'd'', alpha_u=theta+DD[u], and V=integral theta^2.

The published infrastructure used is CLD arXiv:1204.6277v2, 25 July 2025: ordinary smooth cutoffs and finite partitions, positive-current coefficient representation and continuous multiplication, canonical integration, and smooth closed-factor calculus. Applied units are 6.5.2, 7.2.8/11/13, 7.7.1-8, 8.5.1/3/5, 8.7.1/2/4 and 15.7.1-2. Their goodness, separation, pure-dimension and boundary hypotheses are retained. No general continuous-multiplier closedness assertion is used.

First construct the bounded products. In a moment presentation, symmetric coefficient forms correspond to symmetric matrices on an exterior coefficient space. The middle-positive cone is PSD, and the appropriate power of a Euclidean positive form is a positive multiple of the identity. A cutoff therefore bounds any compact symmetric test above and below by middle-positive tests. Positivity gives coefficient Radon measures through Riesz representation. If positive T_i converge weakly and b_i converge locally uniformly, then b_i T_i converge to bT: approximate b uniformly on the test support by a smooth scalar g and split the difference into (b_i-g)T_i+g(T_i-T)+(g-b)T. Positive test masses bound the error terms.

Locally put p=q+u, r=q+v and B(u,v)=DD(p DD[r]). Simultaneous smooth positive approximants and the preceding multiplication estimate show that this is the weak limit of positive smooth mixed products. It is positive, symmetric, local, independent of approximants and continuous for locally uniform convergence in the declared class. Smooth DD-null changes of q glue it. Globally
B(u,v)=theta wedge alpha_v+DD(u alpha_v),
theta wedge alpha_v=theta^2+DD(v theta).
Testing with 1 gives integral B(u,v)=V. Finite convex combinations and finite maxima belong to C_theta, using common local neighborhoods and smooth convex nondecreasing regularizations. This requires no global positive approximant.

Here is the needed integration by parts. Fix a positive symmetric closed (1,1)-current T; do not approximate T. Locally let f be a difference of two uniformly smooth-positive-approximable weights and choose smooth differences f_i=p_i-r_i converging uniformly on compact subsets. The signed Radon measure L_T f=DD(fT) is the difference of DD(pT) and DD(rT), both positive. For a nonnegative compact smooth cutoff chi,
integral chi DD p_i wedge T=integral p_i DD chi wedge T.
Local uniform bounds on p_i give a uniform mass bound. The same holds for r_i and hence for the signed variations of L_T f_i. Distributional convergence and coefficient multiplication yield L_T f_i -> L_T f and f_i L_T f_i -> f L_T f.

For smooth a define Q_T(a)=d'a wedge d''a wedge T. This is positive and its polarization is symmetric. Smooth closed-factor Leibniz gives
Q_T(a)=(1/2)DD(a^2T)-a L_T a.
For a=f_i-f_j, with uniform error eta on a neighborhood of the cutoff support, the preceding variation bounds give
0<=integral chi Q_T(f_i-f_j)<=C_chi(eta+eta^2).
The same identity bounds integral chi Q_T(f_i) uniformly. PSD coefficient positivity gives Cauchy-Schwarz when d''a wedge T is tested against any compact smooth (1,0)-form beta. This follows by integrating the nonnegative quadratic obtained from lambda beta+d'a; bounded smooth scalar multiples of beta are allowed.

Thus d''f_i wedge T are Cauchy as currents. For another such difference g, the currents f_i d''g_i wedge T are Cauchy: split their difference into (f_i-f_j)d''g_i wedge T and f_j d''(g_i-g_j) wedge T. The first tends to zero by uniform convergence and bounded gradient mass, and the second by the Dirichlet estimate. Interleaving sequences proves independence, including independence of different local difference presentations. The limiting currents glue on overlaps.

For smooth f_i,g_i symmetry cancels cross terms:
d'(f_i d''g_i wedge T-g_i d''f_i wedge T)=f_i L_T g_i-g_i L_T f_i.
Pass to the established local limits and glue. On compact X, testing with 1 proves
integral f DD(gT)=integral g DD(fT).
The positive local limits Q_T(f_i) equal
Q_T(f)=(1/2)DD(f^2T)-f DD(fT),
so integral f DD(fT)=-integral Q_T(f)<=0. Here f^2T is only a coefficient product; it is not asserted closed, and f^2 is not asserted psh. This avoids CLD 8.6.7's continuous-multiplier closedness issue.

Every u in C_theta is locally (q+u)-q. The identities therefore apply to global u,v and to T=theta or alpha_w. Directly from the reconstructed products,
DD((u-v)alpha_w)=B(u,w)-B(v,w).

Define
E(u)=(1/3)integral u(theta^2+theta wedge alpha_u+B(u,u)).
Constants satisfy E(u+C)=E(u)+VC. For f=v-u, u_t=u+tf and alpha_t=alpha_{u_t}, multilinearity makes E(u_t) a polynomial of degree at most three. Differentiation and the proved integration by parts give
E'(u_t)=(1/3)integral f[theta^2+theta alpha_t+alpha_t^2+(alpha_t-theta)(theta+2alpha_t)]
=integral f alpha_t^2.
Differentiating again gives
E''(u_t)=2integral f DD(f alpha_t)=-2integral Q_{alpha_t}(f)<=0.
Integrating the decreasing derivative proves, for EVERY u,v in C_theta,
E(v)<=E(u)+integral(v-u)MA(u).

Comparison also holds for the entire bounded class. For epsilon>0 set w=max(u,v-epsilon). Locality on the two strict open regions and positivity imply
V>=integral_{u>v-epsilon}MA(u)+integral_{u<v-epsilon}MA(v).
Consequently integral_{u<v-epsilon}MA(v)<=integral_{u<=v-epsilon}MA(u). Both sets increase to {u<v} as epsilon decreases to zero. Continuity from below proves integral_{u<v}MA(v)<=integral_{u<v}MA(u). Equality-set mass is correctly included on the intermediate right side.

This proves the bounded variation, concavity, tangent and comparison gates under the named analytic infrastructure. It does not prove unbounded decreasing continuity or intrinsic all-direction E1 recognition.

Complete artifacts: n1.md, P16.7-bounded-dual-paper.tex, proof-companion.md and source-application-ledger.md. Rerun own integrity and finite algebra diagnostics with python identity_audit.py and python diagnostics.py; neither execution establishes this universal analytic proof.
