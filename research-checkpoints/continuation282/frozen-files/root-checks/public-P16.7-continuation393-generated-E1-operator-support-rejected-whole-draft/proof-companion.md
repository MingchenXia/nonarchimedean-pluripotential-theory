# Generated finite-energy analytic operators on the concrete quotient

Unverified scoped proof draft. Original P16.7 incomplete.

# Bounded sheaf recognition and canonical generated energy

This is an unverified proof draft under the ordinary CLD foundations stated here. It distinguishes the locally smooth-approximable class C1 from the larger class C defined using the smallest continuous-psh sheaf P, closed under local uniform limits. Equality C1=C is neither assumed nor proved.

Let X be compact Hausdorff, good, pure two-dimensional and boundaryless, with ordinary CLD smooth forms, smooth cutoffs and finite partitions of unity. Let theta be a smooth positive closed (1,1)-form with local smooth psh potentials rho. Use middle positivity; for the (1,1) tests below it is the positive semidefinite matrix cone. Let C={u continuous:rho+u is locally in P}. Retain canonical integration and M=integral theta^2>0. The surface restriction avoids confusing a current's degree with its bidimension: the positive closed currents T used in Green's formula have both equal to (1,1).

The external source units are CLD, arXiv:1204.6277v2, Definitions 8.1.7-8, Lemmas 8.5.1/3/5, Section 8.7.1 and Propositions 8.7.2/4, Section 8.8.4-5, Proposition 7.2.8 and Examples 7.2.11-13, Proposition 5.11.1 and Theorem 15.7.1. Their actual statements used are: P is the minimal continuous sheaf containing smooth positive-Hessian functions and closed under uniform limits; continuous coefficients can multiply positive currents; locally uniformly convergent coefficients times weakly convergent positive currents converge; DD(fT) is positive closed for continuous psh f and positive closed T; recursive continuous-psh products are symmetric and locally uniformly continuous; smooth DD-null potential changes leave the products unchanged; positive top currents correspond to positive Radon measures; smooth closed-factor differentiation and boundaryless Stokes hold; a separated pure-dimensional analytic space with its analytic boundary has the associated calibrated tropical calculus. These statements and their immediate source arguments were read in the retained full text. General higher-degree strong-cone order-unit assertions and the continuous-multiplier closedness statement 8.6.7 are not premises. Deeper CLD integration, cutoffs and positivity foundations remain conventional published inputs.

The recursive bounded product is B(u,v)=theta wedge theta_v+DD(u theta_v), where theta_v=theta+DD[v]. Local potentials and the cited recursion make it symmetric, positive and local. Testing the differentiated terms with 1 gives B(u,v)(X)=M. Convexity and maximum stability of C follow by two successive minimal-sheaf arguments from the corresponding smooth convex combinations and soft maxima. No global smooth psh approximation is used.

Here is a proof of the Green input for ALL stages of P. For a fixed positive closed T complete compact smooth (1,0)-forms modulo the null space of the pairing integral a wedge Jb wedge T. The pairing is symmetric, nonnegative and satisfies Cauchy-Schwarz by positivity applied to a+tb. Local cutoff seminorms are Q_chi(f,g)=integral chi d'f wedge d''g wedge T. Let H_T consist of continuous functions locally uniformly approximable by smooth functions whose gradients converge strongly in these seminorms. Smooth partitions show that H_T is a vector-space sheaf: for local approximants f_i,k and partition chi_i, the gradients of sum chi_i f_i,k are sum chi_i d'f_i,k+sum f_i,k d'chi_i. Both terms converge strongly, the latter by uniform convergence and finite smooth coefficient pairings. Products and smooth cutoffs obey the same Leibniz argument. Continuous bounded coefficients act in the completion by smooth uniform approximation and the norm bound ||fa||<=||f||infinity ||a||.

The gradient is unique. If smooth f_k tend uniformly to zero and their gradients strongly to a, closedness gives integral d'f_k wedge Jb wedge T=-integral f_k d'(Jb) wedge T ->0 for every compact smooth b. The right pairing is a finite signed Radon measure. Compact smooth forms are dense by the definition of this completion; hence a=0. For local cutoff completions use b supported in the larger patch and test against chi b; restriction to a smaller compact support proves the local assertion. No independent distributional Sobolev density theorem is assumed.

If f is in H_T and L_Tf=DD(fT) is signed Radon, then for compactly supported g in H_T,

integral g L_Tf=-Q_T(f,g).

For smooth g this follows from integral f DDg wedge T and smooth approximation of f. Approximate g uniformly and strongly, after multiplying by a cutoff equal to one on its support: the measure pairing converges uniformly and the gradient pairing strongly. Applying this identity to g=chi w and using the product rule gives the exact cutoff identity

Q_chi(w,w)=(1/2) integral w^2 DDchi wedge T-integral chi w L_Tw.

To recognize all continuous-psh stages, consider the sheaf of members of H_T with nonnegative L_T. It contains smooth psh functions. For u_j in this sheaf converging uniformly near supp chi, put |u_j|<=B, eta>=0 compact smooth and equal to one near supp chi, and epsilon=||u_j-u_k|| there. Positivity and distributional differentiation give

integral chi(L_Tu_j+L_Tu_k)<=2B||chi||infinity ||DDeta wedge T||TV,

0<=Q_chi(u_j-u_k,u_j-u_k)<=epsilon^2||DDchi wedge T||TV/2+2B epsilon||chi||infinity ||DDeta wedge T||TV.

Thus the gradients are strongly Cauchy. On each smaller patch choose smooth approximants with both errors at most 1/j, obtaining a smooth approximation of the uniform limit. Distributional positivity survives the limit. The sheaf is uniformly closed and therefore contains P by minimality, including every stage. Its span contains all continuous dpsh functions. On compact X finite patching and the preceding test identity consequently give

integral f DD(gT)=integral g DD(fT)=-Q_T(f,g), integral f DD(fT)<=0.

For u in C set E(u)=(1/3)integral u(theta^2+B(u,0)+B(u,u)), E(0)=0. Differentiating the actual cubic along u_t=u+t(v-u), and using Green with T=theta and theta_u_t, gives E'(u_t)=integral(v-u)MA(u_t) and E''(u_t)=-2Q_theta_u_t(v-u,v-u)<=0. Hence E is concave, monotone, satisfies E(u+c)=E(u)+Mc and the full-class tangent inequality. Also

E(u)-E(v)=(1/3)integral(u-v)[MA(u)+B(u,v)+MA(v)].

For u>=v every displayed nonnegative term is at most 3(E(u)-E(v)). Maximum, locality and common mass give bounded comparison: MA(v){u<v-epsilon}<=MA(u){u<=v-epsilon}; both sets increase to {u<v} as epsilon decreases to zero. This proof includes contact-set mass on the intermediate right side.

Define G=E1_downarrow as functions u_j in C decreasing pointwise to u with inf E(u_j)>-infinity. This is a generated class, not every intrinsic unbounded psh stage. Its canonical energy is independent of EVERY bounded continuous decreasing presentation. Indeed, if continuous v_k decrease to u and a is continuous with u<a everywhere, the increasing open sets {v_k<a} cover compact X, so one index works everywhere, including poles. Apply this to a=u_j+epsilon and, in reverse, to a=v_k+epsilon. Monotonicity and the constant rule yield equality of the two energy limits and finiteness of both. If u were identically minus infinity, the same cover with a=-A would force E(u_j)<=-MA for every A, a contradiction. The same strict-majorant proof gives order preservation and the constant rule on G.

Finite convex combinations of generated members are generated, by bounded concavity. Energies on each such finite-dimensional simplex are polynomials of degree at most three. For two variables or any fixed finite number, evaluate bounded polynomials at an unisolvent finite interpolation set inside the simplex. The energy values converge finitely by canonical independence; the coefficients therefore converge. The limiting polynomial is exactly canonical energy at every simplex point. Unisolvent sets exist because a polynomial vanishing on an open simplex is zero, so finitely many point evaluations span the dual of the finite-dimensional polynomial space.

A useful additional continuity fact needs no flattening: if u_k in G decrease to u already in G, then E(u_k) decreases to E(u). Each u_k is upper semicontinuous. For a fixed bounded continuous term v_l of a presentation of u, the sets {u_k<v_l+epsilon} are open, increase and cover X. Order gives lim E(u_k)<=E(v_l)+M epsilon. Let l increase and epsilon decrease. The reverse inequality is order preservation. This asserts no automatic generation of a limit of unbounded generated functions.

For a positive finite Radon measure define E*(mu)=sup_C(E(v)-integral v mu). Finiteness forces mass M by testing constants. Every u in G is integrable for every finite-dual mu, and integral(-u)mu<=E*(mu)-E(u) when u<=0. To prove this, subtract a single upper bound for the first presentation term, use the bounded dual inequality and monotone convergence, then cancel the shift using mass M. The same argument gives L1(mu) convergence of EVERY decreasing bounded continuous presentation. Finally bounded tangent gives E*(MA(v))=E(v)-integral v MA(v), attained at v. These reproduce the valid ROOT389 conclusions without assuming an unbounded operator.

Artifact: n1.md. The complete current proofs are in generated-E1-paper.tex and proof-companion.md. Rerun the own packet and version observations with `python inspect_packet.py verify` and `python verify_versions.py`; these checks do not prove the universal statements. No supplied program was executed.


# Global bounded potentials separating every analytic point

This new unverified proof uses the bounded all-stage calculus of n1. Retain the actual quotient X=(G_m^2)^an/<(s^8,2),(3,s^8)> over K=C((s)), |s|=exp(-1/8). The datum is theta=DD((x_1^2+x_2^2)/2), x_i=-log|z_i|. Deck changes are affine and theta descends. The raw mass is M=2, with the degree-one, saturated Z^2 torus normalization. The source-dependent exclusion of every separated finite-type algebraic-space algebraization is retained from whole390 settled n2 under its explicitly named Gruson, coherent-descent, Conrad-Temkin, Stacks and Ducros regularity foundations; that foundational proof tree is not newly certified here. The new construction needs quotient charts and the stated theta, not the radial calibration or a skeletal support theorem.

For clarity the elementary quotient properties used here can be checked directly. Tropical translations are Z^2. The inverse image of a rectangle of coordinate widths less than one injects into the quotient and provides an ordinary open chart. Around bounded tropical ranges only finitely many closed deck graphs occur, giving a Hausdorff separated quotient under analytic open gluing. The compact polyannulus x^{-1}([0,1]^2) surjects onto X. Strict nested polyannuli yield good strict neighborhoods. Torus charts give smoothness, dimension two and empty relative boundary; compactness and separatedness give properness. The connected torus covers X. These are the retained analytic quotient/gluing foundations, rather than a new algebraization assertion.

Claim: C from n1 separates ALL distinct analytic points. Its real linear span D is uniformly dense in C(X). In particular it distinguishes points away from every selected skeleton. We now prove this explicitly.

If p,q have different tropical classes in R^2/Z^2, choose a smooth periodic real f with f(tau(p))!=f(tau(q)). Such functions exist, for example suitable sine or cosine of a coordinate character. Its Hessian is bounded on the compact real torus, so for sufficiently small epsilon>0, Id+epsilon Hess f is positive semidefinite. Therefore epsilon f composed with tau belongs to C and separates p,q.

Suppose their tropical classes agree. Choose a common lift a in R^2, 0<r<1/2, and the ordinary quotient chart V whose lifts satisfy |x_i-a_i|<r. Both points have unique lifts in this chart. Berkovich points of the algebraic torus are multiplicative seminorms on K[z_1^+-1,z_2^+-1]; distinct points differ on some Laurent polynomial P. Relabel so |P(p)|>|P(q)| and put b=log|P(p)|, which is finite. The possible value |P(q)|=0 is allowed.

Set rho_a=(1/2)sum(x_i-a_i)^2, so DD rho_a=theta on V and rho_a(p)=rho_a(q)=0. On the closed lifted polyannulus |x_i-a_i|<=r the ultrametric Laurent-polynomial estimate supplies a finite upper bound L for log|P|. Choose delta>0 with delta<r^2/4, and epsilon>0 so small that delta+epsilon(L-b)<r^2/2. With a strict margin, this inequality remains below rho_a in a collar of every tropical boundary face. Define on V

F=max(rho_a, delta+epsilon(log|P|-b)),
v=F-rho_a,

and set v=0 outside V. At zeros of P the second term is minus infinity; F=rho_a in an ordinary neighborhood of such a zero. Consequently F and v are finite continuous, and v vanishes on a collar of the chart boundary, so this is a well-defined global continuous function.

On {P!=0}, log|P| is an ordinary affine unit moment, while rho_a is a convex smooth function of the torus unit moments. Smooth convex nondecreasing soft maxima therefore locally uniformly approximate F by ordinary smooth positive-Hessian weights. Near a zero F equals rho_a. Near the boundary v is identically zero. Thus v lies even in C1, and hence in C; this is a direct class-membership proof, not an identification C1=C. At p, v(p)=delta. At q, v(q)=max(0,delta+epsilon(log|P(q)|-b))<delta, with value zero if P(q)=0. This proves point separation on the full analytic carrier.

D is a vector lattice. Every element is a positive scalar times a difference of two C members, since C is convex and contains constants. If f=A(p-q), g=A(r-s) after enlarging a common positive A, with p,q,r,s in C, then

max(f,g)=2A max((p+s)/2,(r+q)/2)-2A(q+s)/2,

which belongs to D by maximum stability of C. Minima follow by negation. Constants lie in D, and the preceding construction proves that D separates points.

Here is the uniform-density argument, without invoking an unstated algebra version of Stone-Weierstrass. Given continuous h and eta>0, for each pair x,y use point separation and constants to choose f_xy in D with f_xy(x)=h(x), f_xy(y)=h(y); when x=y the constant h(x) suffices. Fix x. The neighborhoods where f_xy>h-eta cover X; choose finitely many y and let g_x be their maximum. Then g_x>h-eta everywhere and g_x(x)=h(x). By continuity g_x<h+eta near x. Select finitely many such neighborhoods and take the minimum of their g_x. It lies in D and has uniform error less than eta. Hence D is uniformly dense in all continuous real analytic-space tests.

This construction changes no positivity datum and asserts no globally strictly positive Kahler current. In fact theta vanishes on the ordinary residue bidisc W={|z_1-1|<1,|z_2-1|<1}, since x_i=0 there. On an annular portion where w_1=z_1-1 is a unit, DD((log|w_1|)^2/2) has positive curvature in its moment direction and cannot be bounded by C theta there. Thus the suggested global Hessian domination is unavailable for this datum. The separating potentials overcome that obstruction through bounded energy coefficients, rather than by assuming domination.

Artifacts: n2.md, generated-E1-paper.tex and proof-companion.md. No numerical experiment is used to prove point separation or density. Rerun serialization and finite interpolation checks with `python build_own.py` and `python finite_checks.py`. Geometry/nonalgebraization support: whole390 settled n2, retained under its named published foundations; no incoming correctness grant is asserted.


# Approximation-independent all-direction generated MA and mixed operators

This is a new unverified scoped theorem on the actual X and theta of n2, using the independently reconstructed bounded theory and canonical generated energy of n1. Let C use the ALL-stage smallest continuous-psh sheaf, and G=E1_downarrow its finite-energy decreasing generated class. No torus invariance, radiality or measure-support restriction is imposed on G or on the following limits.

Theorem. For EVERY bounded continuous presentation u_j in C decreasing to u in G, the genuine analytic bounded measures MA(u_j) converge weakly against EVERY continuous function on X. Their limit MA(u) is independent of the presentation, positive Radon and of raw mass M=2. For every pair u,v in G, simultaneous bounded presentations have approximation-independent weak mixed limits B(u,v), positive Radon of mass M. These are extensions of actual bounded analytic products. They agree with local CLD products wherever the limiting weights are continuous. The theorem is about G, not a recognition of every intrinsic unbounded psh function.

Proof of existence and independence. For a bounded v in C put

P_j(t)=E((1-t)u_j+t v), R_j(t)=E(t u_j).

Both are actual cubic polynomials. At four distinct points in [0,1] their values converge to the finite canonical energies of the generated limits, by n1. Thus all coefficients, and their endpoint derivatives, converge. Bounded first variation gives the exact analytic identity

integral v MA(u_j)=P_j'(0)+R_j'(1).

The right-hand limit depends only on u and v. Linearity therefore supplies a presentation-independent limit for every test in D=span_R C. This is not just a restricted test result: n2 proves D uniformly dense in C(X). For phi continuous choose f in D with ||phi-f||infinity<eta. Since all the actual bounded measures have the same positive mass M,

|integral phi(MA(u_j)-MA(u_k))|<=2M eta+|integral f(MA(u_j)-MA(u_k))|.

The second term tends to zero and eta is arbitrary. Thus the integrals against every continuous phi are Cauchy and independent of the presentation. Their limit is a positive linear functional of norm M taking 1 to M. The compact-Hausdorff Riesz representation theorem states that such a functional has a unique finite regular Borel, equivalently Radon, measure; apply it to obtain MA(u). This proves convergence of the whole sequence, not an arbitrary selected subsequence or an inverse measure assignment. It requires neither metrizability of X nor global Hessian domination by theta.

For mixed products use the bounded analytic polarization identity

B(u_j,v_j)=2 MA((u_j+v_j)/2)-(MA(u_j)+MA(v_j))/2.

The average is a bounded presentation of (u+v)/2 in G. The already established weak convergence proves a unique limit. Positivity and mass M pass from the actual mixed measures. Thus B(u,v)=2 MA((u+v)/2)-(MA(u)+MA(v))/2. In particular B(u,u)=MA(u), and B(u,0) extends theta wedge theta_u. If u,v are continuous on an ordinary open set, on its compact subsets their bounded presentations converge uniformly by the compact open-cover proof of Dini. The local CLD uniform product theorem then identifies these limits with the actual local products. No locality on a singular comparison set is assumed here.

We next prove finite dual and identify self-integrals; these facts will justify unbounded first variation rather than presuming it. Let D_u=lim_j integral u_j MA(u_j)=R'(1), which is finite by coefficient convergence. Bounded tangent and continuous-test weak convergence give, for every bounded v in C,

E(v)-integral v MA(u)<=E(u)-D_u.

Consequently E*(MA(u)) is finite. The n1 integrability theorem now applies to EVERY generated potential, including u, against this new measure; all their pole sets have MA(u)-mass zero.

For fixed j and k>=j, the bounded cocycle and positivity give

0<=integral(u_j-u_k)MA(u_k)<=3(E(u_j)-E(u_k)).

Let k increase: u_j is a fixed continuous test and the self-integral tends to D_u. Therefore

0<=integral u_j MA(u)-D_u<=3(E(u_j)-E(u)).

Let j increase. L1(MA(u)) convergence from n1 proves integral u MA(u)=D_u. In particular

E*(MA(u))=E(u)-integral u MA(u).

The upper bound was just proved. For the lower bound test the bounded u_j in the definition of E* and use their canonical energy and L1(MA(u)) convergence. Equality is attained at u in the dual extended to G; u need not be a bounded test.

Unbounded moment formula. For u,w in G the canonical function F(t,s)=E(tu+sw), on t,s>=0, t+s<=1, is a polynomial of degree at most three by n1, with zero coefficients interpreted at boundary weights without multiplying zero by minus infinity. We claim

integral w MA(u)=partial_s F(1,0).

First let w be bounded. The bounded identity partial_s E(tu_j+sw) at (1,0) is integral w MA(u_j). Polynomial coefficient convergence and weak convergence prove the formula. For arbitrary generated w choose bounded w_l decreasing to w. The functions t u+s w_l decrease to the already generated t u+s w, so their canonical energies converge by the additional decreasing-energy lemma in n1. Finite interpolation makes their polynomial coefficients and derivatives converge. On the other hand E*(MA(u)) is finite, so the w_l converge in L1(MA(u)). These two limits prove the formula. This step does not use any flattening of nested presentations.

It follows that for u,v in G and u_t=(1-t)u+t v,

d/dt E(u_t)=integral(v-u)MA(u_t), 0<=t<=1.

Indeed both partial_t and partial_s of the energy polynomial correspond to the just-proved moments at the convex-combination point. A rigorous way to check the base point is to regard u_t as one fixed generated member and apply the moment formula to the two-variable polynomial E(a u_t+b w); it is the same canonical polynomial obtained by substituting a(1-t), at, b in E(r u+s v+b w). The self-integral identity supplies the derivative in the u_t direction. All integrals are finite because every generated member is integrable for MA(u_t). Poles have measure zero and differences there may be assigned any value. Concavity passes from n1, giving the full GENERATED tangent inequality. This identifies numerical differentiation with the already constructed analytic bounded-limit operator.

Decreasing continuity and moving integrability. Suppose u_j,v_j in G decrease to u,v already in G. They need not be bounded. The strict-majorant argument of n1 gives convergence of energies at every fixed convex combination of these functions. Finite polynomial interpolation then gives convergence of their coefficients. For a bounded test w, the moment formula applied to E(tu_j+s w) proves integral w MA(u_j)->integral w MA(u). Density D and mass give weak convergence on all continuous tests. Polarization gives B(u_j,v_j)->B(u,v). The moment formula for E(tu_j+s v_j) further gives

integral u_j MA(v_j)->integral u MA(v).

With one slot fixed it gives integral u MA(v_j)->integral u MA(v). Subtracting yields the stronger moving-measure convergence

integral |u_j-u|MA(v_j)->0.

Absolute values here equal u_j-u almost everywhere. Every involved measure has finite full dual, so u and u_j are finite almost everywhere. The same argument applies to any generated fixed test, and by polarization to positive mixed measures. For mixed integrability one can also use 0<=B(a,b)<=2MA((a+b)/2).

The energy formula and cocycle now extend with actual finite integrals:

E(u)=(1/3)integral u[MA(0)+B(u,0)+MA(u)],
E(u)-E(v)=(1/3)integral(u-v)[MA(u)+B(u,v)+MA(v)].

To check this, use bounded presentations in the bounded identities. Each measure is a polarization of MA at averages of the slots; the moving-moment convergence just established passes every term to its asserted integral. Finiteness also follows from finite dual for each MA average and domination of mixed measures. No subtraction of infinite integrals occurs.

For u<=0, the first identity implies -integral u MA(u)<=-3E(u), because the three negative integrals are nonnegative after changing signs. Thus E*(MA(u))<=-2E(u). For u<=0 with E(u)>=-C, its ordinary clamps u^A=max(u,-A) belong to G: max(u_j,-A) is a bounded continuous presentation and has energy bounded below by E(u). Hence E*(MA(u^A))<=2C, and n1 applied to u gives

MA(u^A){u<=-A}<=3C/A.

This quantitative estimate already rules out loss of mass in the weak clamp recipe. The stronger exact restricted-truncation identification, comparison and mixed locality are proved in n4. No analogous conclusion is asserted for nongenerated intrinsic psh stages.

Artifacts: n3.md, generated-E1-paper.tex, proof-companion.md and final-notes.json. Rerun `python build_own.py` and `python finite_checks.py`. The finite program checks interpolation identities, not this universal analytic theorem. Supports: n1 and n2.


# Generated comparison, mixed locality and exact truncation identification

This new unverified argument uses the analytic weak operators, unbounded moment formula and moving L1 convergence proved in n3, and the bounded comparison of n1. It applies to the all-direction generated class G on the actual quotient of n2. Its conclusions do not extend by fiat to every intrinsic psh stage.

We first give the measure-theoretic passage needed to handle discontinuous comparison functions. Suppose positive measures mu_j of common mass M converge weakly to mu on compact X, and generated a,b have bounded continuous presentations a_j,b_j. Put f_j=a_j-b_j and f=a-b off their pole sets. Assume

integral |a_j-a|mu_j+integral |b_j-b|mu_j ->0,

and, for each fixed l,

integral(a_l-a)mu_j ->integral(a_l-a)mu,
integral(b_l-b)mu_j ->integral(b_l-b)mu.

All these integrals are finite; poles have zero measure. These hypotheses hold by n3 whenever mu_j=MA(c_j), c_j decreases to c already in G. They also hold for mixed measures by positive polarization and the moving-moment formulas. In the fixed-l equations, the limits tend to zero as l increases by L1(mu) convergence.

For bounded Lipschitz H and continuous phi, the two-stage estimate gives

integral phi H(f_j)mu_j ->integral phi H(f)mu.

Proof: replace f_j by f, with error bounded by ||phi||infinity Lip(H) integral|f_j-f|mu_j. Replace f by f_l=a_l-b_l, with limsup error bounded by the two fixed-l integrals. The function phi H(f_l) is continuous, so weak convergence applies for fixed l. Let l increase to remove the two errors on both sides. This also proves the corresponding assertion with f_j replaced by any other bounded presentation of the same a,b.

If mu{f=epsilon}=0, approximating the step 1_{f>epsilon} from above and below by bounded Lipschitz ramps, whose transition widths decrease to zero, yields

integral phi 1_{f_j>epsilon}mu_j ->integral phi 1_{f>epsilon}mu.

For nonnegative phi the ramps sandwich the integrals and their limiting gap is bounded by ||phi||infinity mu{|f-epsilon|<=delta}, tending to zero. Signed phi follows by subtraction. Only countably many levels have positive mass for a finite measure; pole sets have already been removed. No capacity or quasi-continuity premise is hidden in this lemma.

Generated comparison. Choose arbitrary bounded continuous presentations u_j,v_j of u,v in G. Bounded comparison applied to u_j,v_j-epsilon gives

MA(v_j){v_j-u_j>epsilon}<=MA(u_j){v_j-u_j>epsilon}.

Use the preceding indicator lemma separately with moving measures MA(v_j) and MA(u_j). Its hypotheses are n3's diagonal and fixed-slot moving integrals for u and v. At levels epsilon>0 with zero level mass for both MA(v) and MA(u), passage to the limit proves the same inequality for the set {v-u>epsilon}. Choose such levels decreasing to zero and use continuity from below. The result is

MA(v){u<v}<=MA(u){u<v}

for EVERY u,v in G. The sets are Borel; the undefined difference at common poles is irrelevant to both measures because every generated pole set has zero mass.

Maximum locality. Set w=max(u,v) and w_j=max(u_j,v_j). Then w belongs to G, since the w_j decrease to w and E(w_j)>=E(u_j); canonical independence applies. On the ordinary open set {u_j-v_j>epsilon}, bounded locality gives MA(w_j)=MA(u_j). Test this identity with phi 1_{u_j-v_j>epsilon} for arbitrary continuous phi. N3 proves every indicator-lemma hypothesis for the moving measures MA(w_j) and MA(u_j). At common atom-free positive levels the limit identity is

1_{u-v>epsilon}MA(w)=1_{u-v>epsilon}MA(u).

To turn equality of continuous-test integrals into equality of Borel-restricted measures, note that a finite Borel restriction of a Radon measure on compact X is again a finite regular measure; Riesz uniqueness applies. Alternatively regular approximation of Borel sets gives the same conclusion. Let epsilon decrease through atom-free levels. Therefore

1_{u>v}MA(max(u,v))=1_{u>v}MA(u).

This is a proved singular comparison-set locality statement, not an invocation of an ordinary open-set theorem on the generally nonopen set {u>v}.

Mixed maximum locality follows by polarization. For any z in G, apply the preceding assertion to (u+z)/2 and (v+z)/2; their maximum is (max(u,v)+z)/2. On {u>v}, except the pole set of z, which is null for all measures involved, it gives the needed equality for the MA averages. Combine this with maximum locality of MA(u) and the polarization formula in n3. The result is

1_{u>v}B(max(u,v),z)=1_{u>v}B(u,z).

The pole set of z is null even for mixed measures because B(a,b)<=2MA((a+b)/2), and the latter has finite full dual and integrates every generated z.

Exact full-mass truncation identification. Normalize u<=0 and put u^A=max(u,-A), A>0. The generated decreasing-energy continuity lemma gives E(u^A) decreases to E(u), and n3 gives MA(u^A)->MA(u). Maximum locality with v=-A proves the stronger exact equality

1_{u>-A}MA(u^A)=1_{u>-A}MA(u).

The right sides increase with A and exhaust MA(u), since MA(u) gives {u=-infinity} zero mass. Thus the genuine generated nonpluripolar recipe, formed from the analytic bounded-limit products of the clamps and restricting to their strict unclamped sets, equals MA(u) and has raw mass M=2. The endpoint {u=-A} is excluded in its entirety. There is no assumed locality on that contact set. N3's quantitative bound MA(u^A){u<=-A}<=3C/A, when E(u)>=-C, provides a separate explicit no-mass-loss estimate.

For u,v<=0 the mixed recipe uses u^A,v^B. Successive mixed maximum locality gives

1_{u>-A,v>-B}B(u^A,v^B)=1_{u>-A,v>-B}B(u,v).

These restrictions increase to B(u,v); both pole sets are null by domination with the finite-dual MA of their average. The mixed recipe therefore has full raw mass M. If E(u)>=-C_u and E(v)>=-C_v, the same domination and dual estimates give the explicit discarded-mass bound

B(u^A,v^B){u<=-A or v<=-B}<=2(2C_u+C_v)/A+2(C_u+2C_v)/B.

Indeed E((u^A+v^B)/2)>=-(C_u+C_v)/2, so its MA has dual at most C_u+C_v; integrate -u and -v using n1 and dominate the mixed measure by twice that MA. The formula includes all contact atoms.

There is a precise boundary to the word nonpluripolar here. Every constructed measure gives the pole set of EVERY global generated finite-energy potential zero mass, and its own clamp recipe is exactly the stated measure. We have not proved that it vanishes on the pole set of every arbitrary LOCAL intrinsic psh function, nor recognized every bounded discontinuous intrinsic psh function as generated. The clamp operator on such a generated bounded discontinuous function is the newly constructed analytic bounded-limit extension; it is not silently identified with a previously defined CLD continuous product. Where clamp weights are continuous, n3 identifies it with that actual product.

Artifacts: n4.md, generated-E1-paper.tex and proof-companion.md. All-direction weak continuity, comparison, first variation and the exact generated truncation assertions above are proofs under n1-n3; finite executions are only observations. Rerun `python build_own.py` and `python finite_checks.py`. Supports: n1, n2 and n3.


# Version/source audit, evidence and original P16.7 residual

This is an unverified scoped deliverable, candidate=false. N1-n4 give a new all-direction GENERATED finite-energy analytic operator draft on the supplied actual quotient, with approximation independence for every bounded continuous decreasing presentation, mixed limits, raw mass two, generated truncation identification, decreasing continuity with a generated limit, comparison and analytic first variation. They do not solve the original equation axis. The requested independent entire recursive supporting-proof/book review is also not certified complete.

Own bounded standard-library byte checks found no mismatch in 228 mathematical bindings, 839 private primary/evidence bindings and 17 whole-book bindings. These are identity observations, never mathematical correctness grants. All supplied/native programs were treated as inert data; none was executed or imported. Only own helpers were written, entirely read before execution, and run. No agent, additional campaign/model call, publication, compiler, editor, authentication, proxy or CA action occurred. No heavy computation was needed; no supervised compute facility was supplied or launched.

The current settled FINAL is the 38218-byte JSON at mathematical index191. Index190, named actual-final-notes.json, is its DIFFERENT 52591-byte expanded serialization. Own parsing confirms four actual text lengths 6453,9584,9978,8234 and four expanded lengths 9518,12865,14512,11135; all four pairs differ. The expanded bodies occur in the 64776-character companion at offsets142,9661,22527,37040, and its 16600-character ledger at48176. The current ROOT224 identity correction is consistent with these observations, but is used for bookkeeping only. Incoming native evidence223/216 audits older whole387 and does not certify the current four notes. Own ordered encoding verification maps all companion lines, including Markdown headings to section commands, into the current 70203-byte TeX; only its complete unique preamble and final end-document remain outside that encoding. The preamble was read. Exact equality neither duplicates fresh reading nor establishes correctness.

Own exact finite observations: at cubic interpolation nodes(0,1/3,2/3,1), derivative-at-zero weights are(-11/2,9,-9/2,1) and derivative-at-one weights(-1,9/2,-9,11/2); all four monomials of degrees0-3 satisfy these identities. The total-degree-three bivariate polynomial basis has dimension10, and its ten-point simplex grid has exact rational rank10. All729 pairs of symmetric2x2 matrices with three entries each in{0,1,2} satisfy the determinant polarization identity used algebraically in n3. These matrices need not be positive and this finite check proves no analytic positivity. A separation parameter instance r=1/4,delta=1/128,epsilon=1/1024 gives boundary upper term9/1024<1/32 and smaller-point value1/256<delta. Python3.12.14, Clang22.1.3, Linux6.18.44 x86_64 and glibc2.41 were observed. The configured native-model request was not independently introspectable. These are finite execution/environment observations, not proof acceptance.

The actual and expanded four mathematical texts and companion ledger were physically read, with follow-up reads repairing combined-output truncation. ROOT388's whole 21426-character mathematical proof and ROOT389's whole12184-character proof were read, together with their scope records. N1 reconstructs their relevant proof chain independently and preserves C1 versus all-stage C. Whole385's entire14879-character radial proof was additionally read. Current whole390's reconstructed geometric/radial arguments were examined: the declared local smooth-approximation boundary, Picard circle/disc restriction and annulus filling, pole-ideal argument, all-real cutoff formula, degree-one calibration, actual outside atom, Stieltjes clamps and contact endpoints, full versus restricted dual, and radial-only uniqueness are retained accurately. The complete older whole383 and whole387 companions and every essential deeper source proof were NOT all physically reread. No whole-book chapter is certified freshly read in full. Accordingly the requested ENTIRE independent audit remains incomplete, even though the bounded chain needed by the new operator has its own proof in n1.

A concrete NEW source-reading diagnostic concerns ROOT388's retained unit descriptors. The cited whole CLD source has SHA256 64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085, matching its report. However the actual retained units do not contain the full statements described in ROOT184: the file named LF9724-9864 contains Theorem7.8.5 and harmonic discussion, not the continuous-psh definition through8.1.11; LF9885-9980 includes7.8.8 and8.1.1-5, not8.2.1-4; LF10249-10490 includes8.4.1/3 and8.5.1, not all8.5-8.7; LF10494-10574 contains8.5.5/6 and8.6.2/3, not8.8.1-7; LF6990-7024 contains5.9.3, not5.11.1. This is a source-unit/content mismatch, not a refutation of the bounded theorem. Direct LF reads from the retained whole source repair the needed application: lines9724-10110 contain8.1.7-11 and8.2.1-5;10249-10485 contain8.5.1/3/5,8.7.1/2/4 with immediate arguments;10480-10609 contain8.8.4-5 and adjacent units;6990-7024 contain5.11.1;7978-8088 contain7.2.8/11-13;22100-22148 contain15.7.1-2. No dependence on the general strong-Plucker order-unit claim or on arbitrary continuous-multiplier closedness is introduced. The general higher-degree proof in7.2.9 is not a premise of n1.

Ducros's actual author tropicbis full text was read directly for1.1/1.2 at LF1206-1475,1.3 through1578, and the complete applied local3.4 chain through2260. All six provided original-detail page images27,28,29,39,40,41 were viewed. The printed1.3 premise says fi in K; its proof and3.4 application require fi in L. The printed page41 inequality has phi on the right; page40 defines Q with psi on both sides and already derives the corrected inequality. These are real printed typos, not OCR errors. The authentic local upper dimension proof uses the definable translated cone P of dimension<=d, its inverse image as a neighborhood via Temkin reduction, and stabilization of the tropical germ; strict torus charts meet Gamma={1}. The full official2013 erratum was read: it repairs the distinct page36 finite Gauss-fibre separation argument using [14]Lemma3.4.12 and [15]Lemma6.2.2. It is not the missing premise in local3.4's upper-bound chain. Its PDF text prints received6/revised9/accepted9September2013. Web metadata and author/official layouts are not conflated. Deeper Temkin, ACVF, valuation-extension and erratum-reference proofs remain explicitly conventional external foundations, not newly recursively audited. This local-dimension result is needed by the retained radial outside-atom audit, not by the new dense-test operator proof.

The next missing gate was pursued after constructing the operator. Finite full dual now equals the dual over all of G: every finite-dual measure integrates every generated potential, and bounded presentations pass the objective to its limit. Conversely every MA(u), u in G, has finite full dual exactly E(u)-integral u MA(u). Thus mass two plus finite full bounded dual is a correct NECESSARY admissibility condition for a generated solution, with no support restriction. Sufficiency for EVERY such measure is not proved.

An attempted general compactness argument uses integral(-u)mu<=E*(mu)+C on normalized generated energy sublevels E(u)>=-C. This gives only bounded L1 norms for each fixed finite-dual measure. It does not establish uniform integrability, separation of potentials by these integrals, or closure of G under limits in a proposed compact topology. The elementary sequence n times the indicator of[0,1/n] illustrates why bounded L1 norm alone is insufficient; this is only a measure-theoretic diagnostic, not an analytic counterexample. N2's point separation is separation by potential VALUES, and cannot be substituted for a potential-compactness theorem. No diagonal flattening or nested-net closure is inferred. The all-stage intrinsic regularization and compactness problem remains a concrete gap.

Without that compactness replacement, the variational maximization of E(u)-integral u mu has no proved maximizing potential in G for arbitrary finite-dual mu. Nor have analytic obstacle envelopes and orthogonality been constructed for every continuous obstacle. Generated tangent and comparison do not by themselves prove that identical MA measures force potentials to differ by a constant: a strictness/domination or Dirichlet-separation theorem is still required. We do not convert these missing inputs into hypotheses and call the original target solved.

The literal P16.7 residual is therefore: identify the correct full intrinsic analytic E1 space; establish its approximation/closure and all local pluripolar recognition beyond G; prove separated normalized energy-sublevel compactness; construct analytic envelopes and prove orthogonality; prove existence for EVERY positive Radon mass-two finite-energy measure with arbitrary support, or an appropriately stronger sufficient energy condition stated and justified; and prove full uniqueness modulo constants. The present datum remains explicit and consistent with the supplied nonalgebraization foundations. Existing radial solutions agree with the new operator because their bounded generating presentations are genuine and approximation independence now holds for EVERY such presentation. The distinct 2delta_xi_N has only the supplied restricted lower bound1/6+5N/3; no universal atom cap or full eligibility assertion is made. Infinite cubic-tail measures remain excluded by dual energy, not counterexamples.

Artifacts in this working directory: n1.md through n5.md; proof-companion.md; generated-E1-paper.tex; source-application-ledger.md; final-notes.json; scoped-verdict.json; binding-check.json; version-check.json; finite-checks.json; environment.json; build-checks.json; inspect_packet.py; verify_versions.py; finite_checks.py; build_own.py. Rerun only these OWN helpers: `python inspect_packet.py verify`, `python verify_versions.py`, `python finite_checks.py`, `python build_own.py`. All primary bodies, literal units, images and whole-book contexts remain LOCALONLY at their bound locations; they are not included as public source reproductions. ROOT retains compilation, acceptance and publication responsibility. The final note claims scoped progress and an incomplete original atom, so candidate=false.


# Local reading and application ledger

This ledger records actual fresh reading separately from own byte observations. All supplied data, including programs and historical reading reports, were inert. No complete recursive primary-source or whole-book audit is claimed. The original assignment's entire older383/387/source/book review remains unfinished; source boundaries in n5 are binding on the mathematical claims here.

Current proof material physically read: four actual text files201/203/205/207; four distinct expanded bodies202/204/206/208, including repaired204[9400,end),206[0,6500) and[6500,end); current companion215[0,17000) and[48000,end), with its remaining mathematical content identified exactly as the four separately read expanded bodies; the complete current ledger226 is the suffix already read inside215. ROOT183 whole proof, repaired final[19000,end), and185 whole proof were read. ROOT184/186 scope bodies,187 Ducros version record,224 current identity correction and200 qualification were read. ROOT139 whole385 was read. The current TeX188 unique preamble was read both directly and in the current identity report; own encoding checks identify all other mathematical lines. Duplicate body identity is not separate physical reading credit.

The older whole383 and whole387 companions, their complete scope bodies, and all deeper geometric foundation proof trees were not wholly freshly reread. Their historical ledgers are data, not transferable correctness. The supplied whole390 geometry is retained with its named published-foundation scope as explicitly declared support for n2. The new all-direction proof does not rely on radial calibrations, skeleton-factorization, an atom cap, a Banach inverse measure, or unverified source8.6.7.

Ordinary CLD v2: full local retained source at /workspace/research/primary-data-LOCALONLY/P16.7-native264-whole-primary-and-retrieval-evidence-20261008/sources/CLD-v2-whole.txt, SHA25664846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085. The five retained ROOT388 source-unit files were entirely read and their mismatched descriptors checked against actual headings. Fresh direct LF reading covered9724-10110,10249-10485,10480-10850,6990-7024,7978-8088 and22100-22148. Applied exact units are described in n1, with all-stage P, smooth factors, Radon top measures, local uniform recursive products and analytic boundary retained. The accidental larger10480-10850 range includes additional unused units; those are not extra premises. Middle positivity is retained and the higher-degree strong-span order-unit argument is not used. Deeper canonical integration/cutoff/positivity trees remain conventional foundations.

Ducros2012: full tropicbis text retained in /workspace/research/primary-data-LOCALONLY/P16.7-Ducros2012-local-tropical-dimension-20261009/. Direct LF1206-1475 gives complete1.1/1.2. Complete1.3 was read through its actual proof and original-detail images27-29; the missing1.3.2 formula from text is visible on page28. Complete3.4 was read using the retained initial extract, direct LF2165-2245 and2240-2395 (the latter includes unused subsequent context), and original-detail images39-41. The extracted unit boundaries are not substituted for complete proof reading. All six images were physically viewed. The full official2013 erratum text was read, including its entire replacement proof and printed dates. Author erratum body was retained and identity checked, but not separately wholly freshly read; no false duplicate-reading credit is claimed. Actual typo/version distinctions and deeper Temkin/ACVF scope are in n5.

All17 bound book chapters were byte verified, not wholly freshly read. The provided catalogue statement supplies the original residual for comparison and is mathematical context, not an independently proved source theorem. No book theorem is an unproved premise of n1-n4.

The only additional conventional theorem used by n3 is the compact-Hausdorff Riesz representation theorem: every positive linear functional L on C(X,R) is integration against a unique finite regular Borel measure; its mass is L(1). Compactness/Hausdorffness and positivity/boundedness of L are proved or retained explicitly. The vector-lattice uniform-density argument and finite-dimensional polynomial interpolation facts are proved inside n2 and n1, respectively, rather than cited without their content.

All helper sources are own and were entirely read before execution. Byte/hash/encoding checks are observations. Finite rational interpolation and polarization checks are exhaustive only over the finite polynomial bases named by finite_checks.py, not mathematical acceptance of the analytic assertions. No heavy compute facility was supplied or required. No supplied program or active other mathematics was executed/read, and no agent or extra campaign was created. Environment and output are retained locally. ROOT handles any compiler, acceptance or publication.
