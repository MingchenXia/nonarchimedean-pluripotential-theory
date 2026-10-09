Use X of n2 and the bounded operator of n3. Let C=R/Z with probability Lebesgue dy and H={h continuous: rho_h=dy+h''>=0 distributionally}. Testing against one gives mass one. The periodic G(y)=y^2/2-y/2+1/12 has mean zero and G''=dy-delta_0. For any circle probability nu, h_nu=-G*nu satisfies rho_h_nu=nu. Conversely h-h_rho_h has zero second derivative and is periodic, hence constant. Since G ranges in [-1/24,1/12] and is 1/2-Lipschitz, mean-zero potentials range in [-1/12,1/24], have Lipschitz constant 1/2 and oscillation at most 1/8. Sup-zero normalization gives a bounded equicontinuous closed family, uniformly compact by Arzela–Ascoli. Positivity passes by distributional testing. This is circle compactness only.

Define S_theta={h1(tau1)+h2(tau2):h_j in H}. Positive periodic convolution gives actual ordinary smooth-positive approximants, hence S_theta is contained in C_theta. Diagonal smooth Hessians and n3's continuity give the ANALYTIC equalities

B(h1+h2,k1+k2)=i_*(rho_h1 tensor rho_k2+rho_k1 tensor rho_h2),
MA_theta(h1+h2)=2 i_*(rho_h1 tensor rho_h2).

Product probabilities converge weakly first on product tests and then by Stone–Weierstrass on all continuous tests; continuity of the actual section gives analytic convergence. Every measure 2i_*(nu1 tensor nu2) has solution h_nu1+h_nu2. Marginals recover each nu_j, so uniqueness modulo constants holds WITHIN S_theta. X itself need not be a product of curves.

Every h is Lipschitz. Set e(h)=integral h dy-(1/2)integral|h'|^2dy. Periodic convolution gives uniform convergence of h, L2 convergence of derivatives and weak curvature convergence. Consequently

integral h d rho_h=integral h dy-integral|h'|^2dy,
e(k)-e(h)=integral(k-h)d rho_h-(1/2)integral|k'-h'|^2dy.

Thus e is concave, strictly concave modulo constants, with derivative on each admissible circle segment given by curvature integration. E_sep(h1+h2)=2(e(h1)+e(h2)) is independent of shifting constants between factors and satisfies E_sep(u+c)=E_sep(u)+2c. The three bounded analytic energy measures yield respectively 2 sum integral h_jdy, sum(integral h_jdy+integral h_jd rho_hj), and 2 sum integral h_jd rho_hj. Their average equals E_sep. No all-direction variation is assumed.

For ANY positive analytic Radon mu of RAW mass two, define E*_sep(mu)=sup_(u in S_theta)(E_sep(u)-integral u dmu). Normalize each factor by sup h_j=0. Then -1/4<=u<=0 and E_sep(u)<=0; u=0 gives 0<=E*_sep(mu)<=1/2. Let nu_j=(tau_j)_*mu/2. The objective is 2 sum(e(h_j)-integral h_jdnu_j), whose energy-difference identity gives maximizing curvature rho_hj=nu_j, uniquely modulo constants. The maximizing MA is the skeletal product of these marginals, regardless of mu's original support or correlations. Thus restricted finiteness is not the original criterion. For y=(1,1), its value at u0 is -1/6-2(-1/6)=1/6, although MA(u0)=2delta_i(0), not 2delta_y. The full bounded dual infinity is separately proved in n3.

All circle obstacle claims are also reconstructed. For continuous a let P(a)=sup{h in H:h<=a}. Constants below min a ensure nonemptiness. Common Lipschitz bounds, the obstacle upper bound and a constant lower bound make the supremum finite and continuous. On R, y^2/2+P(a)(y) is a supremum of convex functions, hence convex. Therefore P(a) belongs to H and is the largest admissible minorant. Monotonicity and constant translation give ||P(a)-P(b)||_infinity<=||a-b||_infinity.

Put p=P(a), F(y)=y^2/2+p(y). If curvature charged a noncontact arc, choose a short interval [c,d] compactly inside it with positive interior curvature and positive minimum clearance a-p. Replace F there by its endpoint chord. It raises F somewhere, while its slope lies between exterior one-sided slopes, preserving convexity. These slopes are bounded on the fixed compact arc, so the increase is bounded by a constant times d-c and can stay below the obstacle. Repeat on integer translates using F(y+n)=F(y)+ny+n^2/2; affine corrections preserve chords and periodicity of F-y^2/2. This contradicts maximality. Positive curvature on an arc can be localized in arbitrarily short such intervals. Thus rho_p is supported on {p=a} and integral(a-p)d rho_p=0.

For continuous v put p_b=P(a+bv). The energy-difference identity, its reverse and both contact statements give

b integral v d rho_pb<=e(p_b)-e(p)<=b integral v d rho_p.

Nonexpansiveness gives p_b->p uniformly. Distributional testing and fixed mass give rho_pb->rho_p weakly. Dividing by b, reversing inequalities for b<0, proves the derivative at zero of e(P(a+bv)) equals integral v d rho_p. Orthogonality and first variation therefore hold in EVERY circle direction, not for arbitrary analytic obstacles or a full intrinsic cone.

The full E1 attempt has concrete constraints: C_theta contains the branch pencils on the nonalgebraizable base-field example; its bounded products and mass are fixed. Defining a larger class merely by decreasing limits does not construct an operator outside the established continuous class. Uniform energy-bounded compactness fails, while skeleton L1 fails separation. Any proposed full finite-dual criterion must imply n3's branch-tail tests after verified containment and energy agreement. Appropriate weaker compactness, all-direction envelopes and orthogonality, unbounded full-mass products and continuity, full first variation, existence for EVERY admissible arbitrary-support mass-two measure and full uniqueness modulo constants remain unproved. No inverse measure construction is substituted for MA.

Artifacts: notes/n4.md, P16.7-standalone-paper.tex and proof-companion.md. Rerun own finite diagnostics with `python scripts/diagnostics.py`; the analytic circle claims rely on the universal arguments above.