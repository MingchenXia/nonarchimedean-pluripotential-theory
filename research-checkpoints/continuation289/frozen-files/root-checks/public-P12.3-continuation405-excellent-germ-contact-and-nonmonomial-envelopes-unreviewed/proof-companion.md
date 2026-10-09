# n1. Finite contact certificates on every excellent germ

Support: G331, with its entire source, annotation, ledger and scope unchanged. No result of current401, B341 or E350 is a premise. We prove a general excellent-germ theorem, followed by an explicit monomial certificate. No general CE is assumed.

Let R be an excellent local ring whose reduction has positive dimension, a a proper primary gauge, and X=V_a(R). All ideals and semivaluations below are interpreted on the reduction, as required by G331. Let J be ANY proper primary ideal and q a positive integer. There is a FINITE nonempty set E_J of centred semivaluations on X such that the independently geometric classes of G331 satisfy
\[
 u\in D,\quad u(x)\le -v_x(J)/q\ (x\in E_J)
 \quad\Longrightarrow\quad u(v)\le-v(J)/q\ (v\in X).       \tag{G1}
\]
Thus for ANY continuous obstacle f, however nonmonomial, the conditions
\[
 f\ge H=-v(J)/q\text{ everywhere},\qquad f|_{E_J}=H|_{E_J} \tag{G2}
\]
give its greatest geometric D envelope P(f)=H in the actual geometric core. The same holds for any bounded-above upper semicontinuous f satisfying (G2). If f>=H-epsilon and f(x)<=H(x)+delta at all contacts, epsilon,delta>=0, then H-epsilon<=p(f)<=H+delta, without assuming positivity of p(f). These are sufficient conditions, not a density or necessity theorem for arbitrary obstacles.

We construct and prove the certificate first when R is an excellent NORMAL local domain. Normalize the actual primary blowup Bl_J(R). Excellence makes normalization finite, so Y is projective, normal and Noetherian. The pulled-back ideal J O_Y=O_Y(-E) is invertible and E is an ACTUAL effective Cartier divisor supported over the closed point. Normalization is only used to test inequalities; H itself already has its actual nef primary-blowup presentation on Bl_J(R). No cofinality among arbitrary models, new cone definition, or positivity on a merely numerical Weil list is invoked.

The effective divisor E has finitely many prime components E_1,...,E_s, all of height one and all lying over the closed point. The DVR orders nu_i=ord_{E_i} restrict to valuations of Frac(R) centred at m. They have 0<nu_i(a)<infinity and nu_i(J)>0: every element of m is in the height-one maximal ideal at that centre, and a,J contain primary powers. Normalize nu_i by nu_i(a) to define E_J. There is at least one component: J O_Y is nonunit at any point of the nonempty closed fibre, and a nonunit regular local Cartier equation has a height-one prime. Proper birationality gives the nonempty fibre over the positive-dimensional domain.

Let u=-v(I)/r be any rational unit-or-primary profile and assume its contact inequalities. After clearing q and r they say
\[
 \nu_i(I^q)\ge r\nu_i(J)\quad (1\le i\le s).              \tag{G3}
\]
For each generator t of I^q, (G3) gives the height-one section condition t in O_Y(-rE) at every E_i. At all other height-one points E has coefficient zero and t, being in R, is regular. The normal codimension-one section criterion on every affine open therefore proves
\[
 I^q O_Y\subset J^r O_Y.                                  \tag{G4}
\]
This is a direct proof of the needed finite Rees-valuation implication. No toric or test-ideal theorem, or Rees integral-closure criterion, is imported as an additional premise.

To evaluate (G4) at ANY v in X, including nonzero prime support p, pass first to its valued quotient field Frac(R/p). The generic point p differs from m, so Y is isomorphic there. Properness and the valuative criterion lift the map of its valuation ring to Y. The local generator of J O_Y at this valued centre has nonzero image, because J has finite value and its canonical generic trivialization is off the closed fibre. Pull (G4) to the valuation ring. The value of the invertible J ideal is exactly v(J), since the base generators generate it and one local coefficient is a unit. Hence qv(I)>=rv(J). This proves u<=H on EVERY support. No map from the original total fraction ring through p or subtraction of infinite values is attempted.

For a general excellent reduced R, its finite normalization is the semilocal union of normal local centres S_i. Every extension J S_i is proper primary for its marked centre. Form the preceding finite certificate at every S_i with gauge a S_i and restrict all these points to X_R. Their union is finite. A D_R function satisfying those downstairs tests has a positive pullback by G331, satisfying the tests on every normal centre. The normal theorem controls it on EVERY source point, and surjectivity of the boundary restriction controls it on every downstairs point. This proves (G1). The full conductor relation is respected: H is the evaluation of a DOWNSTAIRS primary ideal, so its pullback is constant on all fibres, including the infinite-conductor quotient stratum. No separate compatibility of arbitrary source extrema is asserted.

The C,D steps require no completion shortcut. For g in C with the contact bounds, approximate by a rational primary profile within epsilon and subtract a rational primary-gauge constant between epsilon and 2epsilon. This is again a rational profile after clearing denominators and multiplying by a power of a. It satisfies all exact contact bounds, hence is below H by (G3)--(G4). Let epsilon tend to zero. For u=inf_i g_i in D, finitely many strict contact tests and directedness select one term with g_i(x)<H(x)+epsilon at EVERY contact, even if u has poles there. Apply the C implication to g_i-epsilon and let epsilon tend to zero. This proves (G1) for ACTUAL decreasing nets, bottom and partial poles, without flattening, increasing closure or CE. H is an actual geometric competitor under (G2), so the envelope statement follows. The quantitative statement applies (G1) to competitors shifted by -delta and uses H-epsilon as an actual C competitor.

For nilpotent R this is exactly the reduction theory of G331, without unreduced intersection multiplicities. In dimension zero the boundary is empty and the unique empty envelope is direct. The unit barrier is zero and needs no contacts. Thus this theorem supplies a nonmonomial obstacle sector over EVERY excellent singular or nonnormal germ, including mixed characteristic and imperfect residue. It does not assert continuity for obstacles which do not satisfy (G2). Its conventional backgrounds are finite normalization, proper valuative criterion and normal codimension-one sections at their actual Noetherian excellent hypotheses. These are disclosed backgrounds, not new incoming grants.

Rerun delivery: python prepare_delivery.py; python verify_delivery.py. The entire explicit toric specialization follows in this same authoritative n1 note. Artifact paths and commands are evidence of retention, not theorem premises.

## Explicit saturated-monoid certificate and finite arithmetic implementation

Support: G331, with its entire source, annotation, ledger and scope unchanged. No result of current401, B341 or E350 is a premise. The argument below reconstructs the required monomial facts and proves the new envelope theorem directly.

Let M be a rank-d lattice, T a pointed full-dimensional rational polyhedral cone, S=T intersect M, and R the completion of k[S] at its monomial maximal ideal, over any field k. Let a be any monomial primary gauge, X=V_a(R), and C,D the independently geometric classes of qualified G331. In particular, C is the uniform closure of negative finite real primary profiles, rational profiles are uniformly dense, and D is made of actual decreasing C-nets. These are consequences of the granted geometric comparison, not new definitions of positivity. Every semivaluation support is included.

The monoid is finitely generated by the rational-cone lattice-point theorem. The affine ring is normal: in its fraction field it is the intersection of the normal Laurent polynomial ring k[M] and the valuation rings of the primitive facet weights. For a Laurent polynomial each facet minimum is the minimum of its term weights; nonnegativity of all these minima says exactly that every exponent belongs to T. The finite-type ring is excellent, and its normal local ring has normal excellent completion. Thus the stipulated R is an excellent normal local domain over arbitrary k. These exact conventional algebraic facts require neither perfection nor a finite extension of a regular local ring. Its elements have unique formal monomial expansions in the maximal-adic topology.

Fix a nonunit monomial primary ideal J and a positive integer q. Put H(v)=-v(J)/q. This is an actual geometric core function: on Bl_J(R) its negative effective Cartier exceptional divisor has an ample negative bundle and nonnegative degree on every contracted proper integral curve, as granted and proved in G331. H is finite continuous on all X. Write
\[
 P_J=\operatorname{conv}\{u_1,\ldots,u_h\}+T
\]
for its Newton polyhedron, using a finite monomial generating set. A finite rational half-space presentation consists of the cone inequalities together with finitely many inequalities
\[
 \langle x,w_j\rangle\ge b_j,\qquad b_j>0.                 \tag{1}
\]
Every w_j in (1) is in the interior of the dual cone. Indeed, a supporting normal is nonnegative on the recession cone T. If it has zero value on a nonzero monoid generator g, primaryness puts some Ng in P_J, so its supporting intercept is zero. Such zero-intercept inequalities are already consequences of x in T. Consequently all positive-intercept facet normals are strictly positive on all monoid generators. The elementary finite rational polyhedral half-space/vertex theorem applies here; no toric test-ideal theorem is used.

For an interior dual weight w, the minimum weight of terms defines a centred monomial valuation of the completed ring. Positivity on the finitely many generators bounds the number of monomials of bounded weight and proves the minimum exists. The associated graded monomials cannot cancel, so multiplication and the ultrametric inequality hold. Normalize by w(a). Denote the resulting point associated to w_j by x_j. Then
\[
 v_{x_j}(J)=b_j/w_j(a).
\]
The finite set E_J={x_j} is a contact certificate for H in the following strong sense:
\[
 u\in D,\quad u(x_j)\le H(x_j)\ (\text{every }j)
 \quad\Longrightarrow\quad u(v)\le H(v)\ (\text{every }v\in X).       \tag{2}
\]

Here is a proof on every support that avoids approximating an infinite monomial weight. First let u=-v(I)/r be a rational primary or unit profile. Let M(I) be the monomial ideal generated by all terms in a finite collection of formal generators of I. Noetherianity makes it generated by finitely many of those terms. Moreover I is contained in M(I): each finite truncation of a generator belongs to this monomial ideal, and the ideal is adically closed by separation of its finite quotient. At every interior monomial valuation v_w(I)=v_w(M(I)), because a least term in a generator cannot cancel against distinct monomials.

The contact inequalities imply, for every occurring exponent u_0,
\[
 q\langle u_0,w_j\rangle\ge r b_j,
 \qquad q u_0\in rP_J.                                    \tag{3}
\]
The second statement follows from the complete half-space presentation and u_0 in S. Write q u_0 as a rational convex combination of the r u_i plus a rational vector in T. Such a rational decomposition exists: it solves a finite rational linear system with nonnegative unknowns, and row reduction on the minimal face of a real solution gives rational feasible points. Clear its denominators by a positive integer D_0. The recession remainder then lies in S, by saturation, and
\[
 \chi^{D_0 q u_0}\in J^{rD_0}.
\]
Thus chi^{q u_0} is integral over J^r, using the equation Z^{D_0}-chi^{D_0 q u_0}=0. For any semivaluation v in X, J has finite value because it is primary. Integral dependence implies
\[
 qv(\chi^{u_0})\ge r v(J).                                 \tag{4}
\]
If the left side is infinite this is automatic. Otherwise a hypothetical strict inequality makes the leading monic term in the integral equation have uniquely smallest finite value, contradicting the ultrametric inequality. Taking the minimum over the finite monomial generators of M(I), then using I subset M(I), proves v(I)/r>=v(J)/q on EVERY support. This proves (2) for rational profiles without assuming that monomialization preserves an arbitrary obstacle.

For g in C satisfying the contact inequalities, approximate g uniformly by a rational primary profile within epsilon. Subtract a rational primary-gauge constant between epsilon and 2epsilon. This subtraction is again a single rational profile after clearing denominators and taking an ideal product. It satisfies the exact contact inequalities, hence is at most H everywhere by the preceding proof. Let epsilon tend to zero to obtain g<=H. For u=inf_i g_i in D, the finite contact set and directedness select one term with g_i(x_j)<H(x_j)+epsilon for every j, even if u has poles at some contacts. Then g_i-epsilon is in C and satisfies the contact inequalities. Hence u<=H+epsilon, and epsilon tends to zero. This proves (2) for the ACTUAL decreasing completion, including bottom and partial poles; no flattening or increasing closure is used.

Now let f be ANY finite continuous obstacle on X, with no weight-dependence assumption, such that
\[
 f\ge H\text{ on }X,\qquad f(x_j)=H(x_j)\text{ for every }j.             \tag{5}
\]
H is a geometric competitor. Every geometric D competitor below f satisfies (2), so is below H. Consequently
\[
 \sup\{u\in D:u\le f\}=H\in C.
\]
This is an actually positive continuous greatest geometric envelope among ALL competitors. The same proof works for ANY bounded-above extended upper semicontinuous f satisfying (5); its envelope is still the continuous function H. Here (5) forces f to be finite below, although its upper size may vary. The unit case J=R has H=0 and no contacts; every obstacle f>=0 has envelope zero by nonpositivity.

There is a quantitative version with no presumed continuity of the raw envelope. If f>=H-epsilon everywhere and f(x_j)<=H(x_j)+delta at the finite contacts, for epsilon,delta>=0, then
\[
 H-\epsilon\le p(f)\le H+\delta.                           \tag{6}
\]
The lower inequality uses the actual C competitor H-epsilon. The upper inequality applies (2) to each competitor shifted by -delta. Thus increasingly accurate lower barriers and contact bounds give uniform approximation of raw envelopes to H, even when CE is not established for each perturbed obstacle. Conditions (5) are sufficient; no necessity or density among all obstacles is claimed.

This advances beyond weight-dependent obstacles: arbitrary cancellation-sensitive functions satisfying the finite contacts are allowed. The general theorem above removes the toric hypothesis for the finite-contact obstacle sector. Neither theorem supplies arbitrary-obstacle CE or an envelope counterexample. Finite geometry controls the competitors; the obstacle is never averaged or monomialized. G331 remains the sole correctness grant. The proof's conventional backgrounds are finite rational polyhedral geometry, Gordan's finite-generation lemma, normal excellent completion, and finite-module adic separation, at exactly the stated hypotheses.

Artifacts: n1.md, proof-companion.md and P12.3-contact-envelopes.tex. The explicit finite certificate used in n2 is implemented by the independently written contact_certificate.py, with contact-input.json and contact-output.json. Rerun: python contact_certificate.py. Program success is only finite arithmetic evidence, not a proof of (2) or of general CE.


# n2. Explicit nonmonomial primary obstacles on normal nonisolated fourfolds, including mixed characteristic

Support: G331 and earlier own n1. We use n1's finite-contact theorem, not the current401 toric-envelope theorem or a finite-cover theorem.

For ANY field k let
\[
 R=k[[a,b,c,d,z]]/(ad-bc),\quad \mathfrak m=(a,b,c,d,z),\quad
 J=(a^2,b^3,c^3,d^2,z^4),\quad
 K=(a+b,c+d,z)+\mathfrak m^2.                               \tag{7}
\]
Both J and K are genuine primary ideals. J contains powers of every maximal generator, and K contains m^2. Write the saturated monoid cone in Z^4 with generators
\[
 g_a=(1,0,0,0),\ g_b=(1,1,0,0),\ g_c=(1,0,1,0),\
 g_d=(1,1,1,0),\ g_z=(0,0,0,1).
\]
The cone consists of x_2,x_3,x_4>=0, x_1>=x_2,x_3. Every integer point is generated by these vectors: choose the coefficient of g_d between max(0,x_2+x_3-x_1) and min(x_2,x_3), then use g_b,g_c,g_a for the remainder and g_z for x_4. The only lattice relation among the first four generators is g_a+g_d=g_b+g_c. Reducing monomials by ad=bc gives the monoid algebra presentation. Thus (7) is the normal excellent complete germ of n1. Its dimension is four. It is regular where any of a,b,c,d is invertible, by solving its equation for the opposite variable. At P=(a,b,c,d), the equation has no linear term in the four normal variables, so that localization has embedding dimension four and dimension three. Its singular locus is exactly the positive-dimensional line P, over every k, including characteristic two. This is a normal nonisolated germ.

The Newton polyhedron of J has the following COMPLETE presentation: the cone inequalities and
\[
 \langle x,w_+\rangle\ge1,\quad \langle x,w_-\rangle\ge1,\qquad
 w_\pm=(1/2,\ \pm1/6,\ \mp1/6,\ 1/4).                  \tag{8}
\]
Both normals are interior to the dual cone: their values on the five generators are respectively (1/2,2/3,1/3,1/2,1/4) and (1/2,1/3,2/3,1/2,1/4). To check completeness without assuming a program's answer, the section at x_4=0 is the cone over the unit square x_1=1, cut by (3x_1+x_2-x_3)/6>=1 and (3x_1-x_2+x_3)/6>=1. Its four vertices are (2,0,0),(3,3,0),(3,0,3),(2,2,2). This follows by considering the four square-edge equalities x_2=0, x_3=0, x_1=x_2, x_1=x_3; intersections of both cutting planes force x_2=x_3 and x_1=2, whose endpoints are (2,0,0) and (2,2,2). Each individual cutting plane's remaining endpoint is the corresponding opposite square corner at x_1=3. There are no other vertex intersections. For 0<=x_4<=4, the right sides for this three-dimensional section are 1-x_4/4. For x_4>4 the section is the whole recession cone. Consequently the full polyhedron has precisely those four vertices with fourth coordinate zero and (0,0,0,4), and recession cone T. These are exactly the five generating exponents in (7), proving (8).

Normalize by the monomial primary gauge m. The two contacts v_+,v_- in n1 have generator values
\[
 (a,b,c,d,z)=(2,8/3,4/3,2,1),\quad (2,4/3,8/3,2,1),
\]
respectively. Both have v(m)=1 and v(J)=4. At EVERY interior monomial valuation, a+b and c+d have their least term values without cancellation, so v(K)=v(m). This also follows at the two contacts directly from the displayed numbers. For an arbitrary semivaluation in V_m, containment m^2 subset K subset m gives 1<=v(K)<=2. Define for any real delta>=0
\[
 f_\delta=-v(J)+\delta\big(v(K)-v(\mathfrak m)\big).
                                                                    \tag{9}
\]
This is a finite continuous obstacle on the entire compact boundary. It is at least H=-v(J), and agrees with H at both contacts. By n1 its greatest geometric D envelope is exactly
\[
 P(f_\delta)=-v(J).
                                                                    \tag{10}
\]
For delta=1/2 this is a rational signed PRIMARY model obstacle:
\[
 f_{1/2}=\big(v(K)-v(J^2\mathfrak m)\big)/2.
\]
The primary product blowup principalizes J,K,m, so it is the evaluation of an actual signed exceptional rational Cartier divisor there. Its obstacle need not be nef. Its envelope is the actual negative effective nef Cartier profile on Bl_J(R), not positivity conferred by upper regularization. Since J subset m^2, f_{1/2}<=-3/2 throughout V_m; it is a genuinely negative example.

To prove the obstacle is genuinely nonmonomial, consider the quotient map to k[[r,h,z]] given by
\[
 a=c=r,\qquad b=d=r(h-1),\qquad z=z,
\]
followed by the monomial valuation with r,h,z weights 1,1,3. The relation ad=bc is identically satisfied. The kernel on R is (c-a,d-b): the quotient is k[[a,b,z]], and substitution a=r,b=r(h-1) is injective because replacing b by a+b sends its two coordinates to r,rh, whose distinct monomials r^{i+j}h^j have distinct exponent pairs. This is a prime support strictly below m. It is an allowed centred semivaluation, normalized already by v(m)=1, and
\[
 v(a,b,c,d,z)=(1,1,1,1,3),\quad v(K)=2,\quad v(J)=2.
\]
The equalities a+b=c+d=rh hold over every field, including characteristic two. At the monomial valuation w_0=(1,0,0,3) on R, the monomial weights of all five generators are identical, but w_0(K)=1 and w_0(J)=2. Therefore
\[
 f_{1/2}(v)=-3/2,\qquad f_{1/2}(w_0)=-2.
\]
They have the same values on EVERY monomial by additivity. Hence (9) cannot be a function only of monomial weights. This is an actual nonmonomial continuous signed primary/model obstacle, not a coordinate re-description of a weight-only obstacle.

The retained singular-supported valuation killing P and giving z value one has v(m)=v(K)=1, v(J)=4, and f_delta=-4. Its Jacobian value v((a,b,c,d)) is infinite. Formula (10) includes this point and all other supports. No nonprimary correction is divided by an index, and no support is discarded. The proof uses finite contact inequalities and genuine primary profiles. It is independent of the Frobenius/test-ideal route and works over imperfect fields and all characteristics. It proves an obstacle sector, not CE for arbitrary obstacles on this ring. It does not prove that this ring lacks a finite regular cover, and no such premise is needed.

Evidence: the own program contact_certificate.py enumerates the five choose four candidate positive facets and the seven choose four candidate vertices by exact rational row reduction. Its observed output is two positive facet normals, five vertices, and PASS on 23 explicitly enumerated positive rational monomial-weight cases. It records the normalized contacts and the exact cancellation and singular-support values above in contact-output.json. The polyhedral and semivaluation arguments above are mathematical proofs; the program checks only this finite certificate. Rerun: python contact_certificate.py. Inputs, source and full output are in contact-input.json, contact_certificate.py and contact-output.json; no supplied program is executed or imported.

## A mixed-characteristic normal nonisolated example

The general theorem in n1 also yields an explicit sector outside equicharacteristic field germs. Fix any prime p, take V=Z_p with uniformizer pi=p, and put
\[
 R_V=V[[a,b,c,d]]/(ad-bc),\quad \mathfrak n=(\pi,a,b,c,d),\quad
 K_V=(a+b,c+d,\pi)+\mathfrak n^2.                         \tag{11}
\]
This is a complete excellent normal domain of dimension four with a singular line (a,b,c,d). Here are explicit checks, so no general mixed-characteristic positivity theorem is assumed. The standard monomials after replacing ad by bc form a V-basis, also after completion degree by degree. The parametrization a=xy,b=xw,c=ty,d=tw in V[[x,y,t,w]] identifies distinct standard monomials with distinct exponent vectors. Thus the quotient is a domain. It is a hypersurface in a regular local ring, so is S2. At a prime not containing all four a,b,c,d, a partial derivative d,-c,-b or a is a unit. In the regular ambient localization the defining equation is outside the square of the maximal ideal (apply that derivation), so the quotient localization is regular. The ideal (a,b,c,d) has height three, by the catenary hypersurface dimension formula and quotient V. Every height-one localization is regular, and Serre's R1+S2 criterion proves normality. At the generic point of that line the quadric has embedding dimension four and dimension three, hence is singular. These CM/S2 facts check this SPECIFIC hypersurface; they are not imposed on the general theorem or formal audit.

The n-adic graded ring is exactly
\[
 \operatorname{gr}_{\mathfrak n}(R_V)
   =\mathbf F_p[\Pi,A,B,C,D]/(AD-BC),                       \tag{12}
\]
a domain. The regular ambient ring has polynomial associated graded ring. For any h there, ord(h(ad-bc))=ord(h)+2, because its associated graded ring is a domain. Its initial form is in(h)(AD-BC). Thus the initial ideal of the principal relation is precisely (AD-BC), with no extra initial relation. The quotient polynomial ring is a domain by the same monomial parametrization. Consequently nu=ord_n is a valuation, not merely a subadditive order, and nu(n)=1.

For EVERY centred semivaluation v with v(n)=1, membership f in n^r gives v(f)>=r, so v(f)>=nu(f). Selecting an element of least finite v-value in a primary ideal I gives v(I)>=nu(I). Every negative rational or real primary profile g therefore satisfies g(v)<=g(nu). Uniform limits and the ACTUAL infima defining D preserve this inequality. This is a one-point contact certificate at nu, proved directly; no count of normalized-blowup components is needed.

K_V is proper primary and n^2 subset K_V subset n. Since a+b has order one, nu(K_V)=1. For any delta>=0 the finite continuous obstacle
\[
 F_\delta=-v(\mathfrak n)+\delta\big(v(K_V)-v(\mathfrak n)\big)           \tag{13}
\]
is at least -1 and equals -1 at nu. Every D competitor below it is at most -1 at nu, hence everywhere. The primary profile -v(n) is itself a geometric competitor, proving
\[
 P(F_\delta)=-v(\mathfrak n)=-1
\]
on the entire normalized boundary. For delta=1/2, (13) is (v(K_V)-v(n^3))/2, an actual rational signed primary/model obstacle on the product primary blowup. Its greatest geometric envelope is actual nef Cartier. Since v(K_V)<=2, this obstacle lies in [-1,-1/2].

It is cancellation-sensitive even with the uniformizer weight retained. Map a=c=r,b=d=r(h-1) into V[[r,h]] and use the weighted valuation with pi,r,h weights 3,1,1. For a formal series sum c_ij r^i h^j its value is min(3 ord_pi(c_ij)+i+j); its associated graded coefficient/monomial ring over F_p is a domain, proving multiplicativity. Pullback is centred, with prime support (c-a,d-b) strictly below n, and
\[
 v(\pi,a,b,c,d)=(3,1,1,1,1),\qquad v(K_V)=2.
\]
The matching monomial valuation on R_V has the same generator and uniformizer weights but K_V value one. It exists by the standard monomial expansion over V, with value 3 ord_pi(coefficient)+total monomial degree. Its associated graded ring is the domain monoid algebra over F_p with a uniformizer variable, so distinct monomials cannot cancel. Thus F_(1/2) has values -1/2 and -1 at these equal-weight semivaluations. The supported valuation killing (a,b,c,d) and giving pi value one has K_V value one and envelope -1, even though the ideal (a,b,c,d) has infinite value. Every support is retained.

This is an unconditional mixed-characteristic excellent normal nonisolated obstacle sector relative to G331. It is not arbitrary-obstacle mixed-characteristic CE. The proofs above establish its universal statements. The own finite program checks only the equicharacteristic Newton instance and is not a p-adic ring computation.


# n3. Exact gauges, compatible normalization contacts, and geometric curve clipping

Support: incoming qualified G331 and earlier own n1,n2. No B341/E350 product or energy result is used.

The contact theorem of n1 applies to every excellent germ and is homogeneous on rays. If b is another primary gauge, write d(v)=v(b) on V_a, T(v)=v/d(v), and transport obstacle, barrier and contacts by
\[
 f_b(Tv)=f_a(v)/d(v),\quad H_b(Tv)=H_a(v)/d(v),\quad x_{j,b}=T(x_{j,a}).
\]
The positive bounded continuous denominator preserves inequalities, contact equalities, uniform convergence and actual decreasing representations. G331 gives precisely this bijection of C,D competitors. Taking their suprema proves the exact envelope rule
\[
 P_b(f_b)(Tv)=P_a(f_a)(v)/d(v).
\]
Substitution supplies the exact three-primary-gauge cocycle. The contact normals remain centred under every primary section; the barrier remains -v(J)/q in the new section. Completion transport is the already granted all-support homeomorphism and exact primary contraction, not a new algebraization or equivalence of geometric model categories.

Here is a full-fibre normalization extension of the new contact sector, which does not assume general CE upstairs. Let R be any excellent reduced germ with finite normalization S, and suppose each positive-dimensional normal local centre S_i is of the saturated monoid type of n1. Take barriers H_i=-v(J_i)/q_i as in n1, or the zero barrier. Require their tuple H to be constant on EVERY restriction fibre of rho:X_S->X_R. Qualified G331 positively descends the continuous tuple to h in C_R. Let f be any finite continuous obstacle on X_R such that f>=h, and for every nonzero barrier's finite contact x_{ij} require
\[
 f(\rho(x_{ij}))=H_i(x_{ij}).
\]
For a D_R competitor u<=f, its pullback on each nonzero branch is at most H_i by n1. On a zero-barrier branch its nonpositivity gives the same inequality. Thus u<=h by surjectivity of rho, while h is itself a competitor. Its greatest D_R envelope is h. The same statement holds for a bounded-above extended upper semicontinuous obstacle satisfying these bounds and contacts. A contact condition at one source point never replaces the imposed FULL-fibre compatibility of H.

Specifically, if c is the conductor, G331 identifies a fibre as a singleton when v(c)<infinity. When v(c)=infinity, lifts kill c and equality of their restrictions through S/c -> R/c is exactly the identification rule. The finite-value locus is open, the infinite-value locus closed. Both are retained in the contact argument. No value v(c)/m is used as a uniform error. Compatibility includes all branches, nonminimal supports, mixed-zero and partial-bottom patterns. This theorem does not assert that an incompatible tuple of source envelopes descends positively or that an arbitrary fibre maximum is psh.

On EVERY excellent reduced curve, normalization has the finite collection of DVR local centres over the closed point, including multiple branches on one irreducible component. A regular conductor element has finite order on every branch, so normalized boundary fibres are singleton. On each DVR the marked point is an actual effective Cartier divisor and there are no contracted integral curves to test. All finite nonpositive coordinates are independently geometric there; G331's positive full-fibre continuous descent gives all finite nonpositive branch vectors downstairs. For an extended nonpositive vector u, max(u,-j) is an actual decreasing sequence of these C vectors with infimum u. Thus D is exactly every extended nonpositive branch vector. For any branch obstacle phi its greatest geometric D minorant is min(phi,0). This is the exact complete ideal-envelope comparison by G331's independently proved cone comparison. The branch coordinate for two primary gauges rescales by ord_i(a)/ord_i(b), with the exact cocycle above.

Nilpotents remain invisible and are removed by reduction; if the local reduction has dimension zero the centred boundary is empty and statements concern its unique empty function. Literal classical or CLD logarithmic radial extension classes are not changed: their stated multibranch mixed-zero obstruction remains. The boundary class may contain (-1,0) without such a literal radial extension. At a smooth affine CLOSED germ over an algebraically closed characteristic-zero field, G331 identifies this exact C,D class with the full published BFJ all-semivaluation class, with bottom adjoined. Wherever our contact theorem applies at that specialization, its greatest minorant is therefore the BFJ envelope in the SAME class. This does not extend BFJ's published hypotheses to arbitrary smooth excellent, imperfect or mixed-characteristic germs. Dimension-one and empty cases above are direct.

Artifacts: n3.md, proof-companion.md and P12.3-contact-envelopes.tex, retaining the full incoming G331 proof/annotation/ledger. Rerun delivery and data checks: python prepare_delivery.py. This scope leaves P12.4 products, P12.5 energy and P12.6 full operator theory separate.


# n4. Current401 audit, formal reconstruction boundary, and unchanged original residual

Support: G331 and earlier own n1,n2,n3 for the new contact theorem, geometric comparison, gauges and curves. Supplied current401, ROOT392, native verdicts, programs, ledgers and inherited B341/E350 are DATA, not grants. None is listed as support or used as an unproved mathematical premise of n1--n3.

The seven actual current401 FINAL objects were read in their entirety, all five fields. The separate expanded JSON agrees in every field except actual n2's two spacing-command backslashes around its d tensor1 arrow label; the displayed algebra is identical. Both complete objects and the full terminal framing remain separately retained. The proof companion is exactly the expanded text join. The current standalone is retained byte-for-byte, including its full qualified G331, B341 and E350 appendices and every annotation/ledger/qualification. Incoming G331's whole 93375-byte text occurs literally in that standalone. Neither an inherited B341/E350 acceptance label nor a native PASS is an additional incoming envelope premise. Data retention and duplicate identity confer no fresh proof/source reading credit.

The following is my independent reconstruction of the active formal chain and the limits of the present audit. It concerns complete normal characteristic-p rings with perfect coefficient/residue field, not arbitrary original germs.

Completed algebra: for a finite complete local k-module V, continuous duality gives V=(V^o)^*, with V^o the union of the duals of its finite-dimensional adic quotients. Artin--Rees identifies the topology of a finite submodule with its induced topology; linear functionals extend in a finite quotient. Thus continuous duality is exact. The identity V completed-tensor_k W=(V^o tensor_k W^o)^* proves exactness in both slots. Applying kernels of two finite presentation matrices then proves the FULL Hom factorization
\[
 \operatorname{Hom}_{R\widehat\otimes_k R}(M\widehat\otimes_k N,R\widehat\otimes_k R)
 =\operatorname{Hom}_R(M,R)\widehat\otimes_k\operatorname{Hom}_R(N,R).
\]
Paired generators generate every map; individual maps need not be decomposable. Perfect coefficients and exponent grouping identify the root of S=R completed-tensor_k R with R^(1/q) completed-tensor_k R^(1/q). Exactness applied twice to the root injections proves S reduced. A parameter ring k[[x_1,...,x_d]] makes R finite torsion-free; embedding it into a finite free module and applying completed exactness makes S finite torsion-free over k[[x,y]]. Its minimal primes contract to zero, so every minimal quotient has dimension 2d. Normality or Cohen--Macaulayness of S is not used.

Different/lift: for a fixed k-parameter normalization A, the adjugate of a square matrix of differences of the presentation equations annihilates all diagonal generators. Its product image is the relative Jacobian minor; hence the Kahler different is contained in the Noether different. If its generic extension is separable, a Noether-different element d is the product image of d times the separability idempotent. The identity
\[
 dw=\sum_i r_i\operatorname{Tr}(s_iw)
\]
base changes through the linearly disjoint purely inseparable K^(1/q)/K. For w in R^(1/q), trace coefficients are integral and lie in the fraction field of the normal regular A^(1/q); they therefore lie in A^(1/q). This proves d R^(1/q) subset P_q=A^(1/q)[R], and P_q is finite FREE over R because its generic multiplication is injective and A^(1/q) tensor_A R is an R-free torsion-free module. It does not make R free over A.

For T=R^(1/q), lift multiplication from the B-free module P_q completed-tensor T through B=R completed-tensor T -> T. Compose with ROOT multiplication d on the first T and 1 completed-tensor phi on the target. After multiplication into R its value is phi(dxy)=d phi(xy). This holds on all completed elements by finite-module continuity, factors through the SURJECTIVE root multiplication, and sends its ENTIRE kernel into the ordinary diagonal ideal. The lift induces output d phi. In F_*^e notation its source multiplier is d^q. Multiplication by d^q in the root module instead gives output d^q phi. The latter is the historical immutable false paragraph, not the corrected401 formula. A concrete check in k[[x]], q=3, phi selecting x^(2/3), gives phi(x^3 x^(2/3))=x^3 while x phi(x^(2/3))=x. The corrected lift is consistent and the whole root kernel is essential.

The fixed-common-field sum of relative Jacobian ideals is exactly Wang's formal Jacobian, not an unrestricted choice of normalization fields. At finite residue field one can preserve each generator's cotangent coset by adding elements of m^2 avoiding a finite incomparable list of nonmaximal primes: for each bad prime choose an element in all the other primes and outside it, then add only for primes containing the current representative. Induct over minimal primes of all previously selected subset ideals. Catenarity and the height theorem preserve the required parameter drops. Thus every d-subset is a parameter system without assuming an infinite residue field. Wang's immediate statement/proof and Liu's exact reduced-equidimensional perfect-residue criterion were read. The common-field sum supplies the compatible-map inclusion Jac(R) C_e subset D_e. Its singular-locus assertion is used only at the actual perfect-residue equidimensional formal rings.

BIG minimum: for a reduced excellent F-finite B, a Cartier algebra C that becomes full on regular B_c, and pair ideals that become unit there, every stable ideal H containing a regular element has H_c=B_c. Locally on B_c, finite free Frobenius and Krull intersection make the root of a regular element primitive for sufficiently large q, and a linear map sends it to one. Clear one splitting's denominators to get theta(F_*1)=c^a. Choose B_0 so c^(q B_0) belongs to that degree's pair coefficient ideal. For the least n with c^n in H, stability implies
\[
 n\le B_0+a+\lceil n/q\rceil\le B_0+a+1+n/q.
\]
Hence a single c^L lies in EVERY such H. Their intersection is an actual generically nonzero stable minimum, not a finitistic test ideal. For any regular seed in that minimum, every arbitrarily late tail of its twisted images is stable and becomes unit on B_c by the same primitive-vector argument. Minimality makes each tail equal the minimum. The gaps between ceil(tq) and ceil(t(q-1)), and between ceil(qt) and r ceil(qt/r), are bounded; a fixed regular element of a bounded coefficient-ideal power bridges them. Shared regular seeds give both-rounding and power invariance. Localization follows by finite Hom localization and those shared seeds. For full algebras only, completion uses finite Frobenius/Hom faithful-flat base change and a common c^L supplied by regular formal fibres. It never assumes an arbitrary nonzero completed ideal has nonzero contraction. If J C_e subset D_e, multiplying the outputs of a COMMON-seed C-tail proves J tau_C subset tau_D; claiming J tau_C itself stable would be invalid.

Diagonal/product: choose a nonzero Jacobian minor j and regular pair elements a_0,b_0. The block minor j(u)j(v) shows S is regular at its generic diagonal. The element c_S=j(u)j(v)(a_0 tensor b_0) is regular by completed exactness and survives multiplication as j^2 a_0 b_0. Thus the actual full S algebra and restricted R diagonal algebra satisfy the BIG framework. The image of the product BIG ideal is D-stable and contains the surviving c_S^L, so minimality gives tau_D subset its image. Full Hom factorization makes the product of the two factor BIG ideals stable for EVERY S map and generically nonzero. Combining these facts gives
\[
 \operatorname{Jac}(R)\tau_R(a^t b^s)
 \subset\tau_D(a^t b^s)
 \subset\mu\tau_S((aS)^t(bS)^s)
 \subset\tau_R(a^t)\tau_R(b^s).
\]
Iteration has Jacobian power ell-1 on the left. Only isolatedness replaces it by a PRIMARY correction uniformly on the whole link.

Isolated model chain: perfect exponent grouping makes ORDINARY Omega_(R/k) finite. Finite-type model rings are F-finite with finite ordinary differentials. Their closed residues are finite separable extensions of k; completion has a compatible coefficient field, and ordinary/formal differential modules and their dth Fitting ideals agree. Closed model points have local dimension d; normal excellent completions and faithful flatness transfer the formal subadditivity to all model points. CEMSv4 explicitly allows finite type over an F-finite LOCAL base with dualizing complexes and the specified F! compatibility; its divisorial reflexive canonical sheaf need not be locally free or CM. The complete immediate Setting2.1, Definition2.2 and Lemmas2.3--2.4 were checked at that scope.

Blowing up Fitt_1(omega), discarding actual chart torsion, and using Fitt_1=unit, Fitt_0=0 produces a rank-one strict-transform line bundle. Pull it to the normalization and use the SAME rational section as K_Y. A positive full-fibre Cartier divisor dominates the exceptional difference, giving effective Delta with L=K_Y+Delta Cartier. An ample negative full-fibre twist is generated; its sections lie in R by Hartogs. It yields a proper primary J with J O_Y invertible. The very ample graph closure proves Y=Bl_J(R), an actual primary model. No arbitrary-model cofinality is inferred.

For every m>=1, I_m=Gamma(Y,O(mC_0)) contains a primary power by the actual Cartier order unit; Hartogs puts it in R. It is unit or primary at EVERY index. Its finite valuations are subadditive, so the all-index Fekete limit of -v(I_m)/m exists. A rational primary competitor below the Cartier obstacle satisfies the normal height-one section inequalities, and its powers lie in I_(rm). Rational density with negative shifts then proves this raw limit equals the C/D raw envelope BEFORE positivity. Asymptotic BIG families stabilize at common multiples for finite lists by Noetherianity and power invariance. A global effective Cartier test divisor dominates all local seeds and finite rounding corrections; its sufficiently ample twist has a section. Every sufficiently late trace sum may use this divisor. The fixed relative Koszul constant c_0 makes (c_0-i)H-L ample for each needed i. Serre vanishing for a fixed finite coherent list after finite Frobenius, followed by the locally split exact Koszul complex, yields late global generation over the Noetherian affine base. No base/module flatness is assumed.

The trace source multiplication is INSIDE Frobenius: F_*t maps to F_*(s t). The remainder ell ceil(qm/ell)-qm ranges over a finite list; different late Frobenius exponents may generate different images. No single exponent is required to realize the sum. Generation and Hartogs put the resulting fractional sheaf inside O_Y; one extra negative primary twist makes its section ideal J_m proper. The inclusions I_m J^(r+c) subset J_m prove genuine primaryness for EVERY m. If s_m,t_m are the two asymptotic BIG ideals and T_0 is a fixed test ideal, the subadditivity bound first gives pointwise
\[
 v(s_m)/m\le[v(b_{m\ell})+v(T_0)]/(m\ell)
                 +(\ell-1)v(J_Y)/(m\ell).
\]
Let ell tend to infinity POINTWISE before using the uniform bound. Isolatedness gives primary J^a O_Y subset J_Y and Delta<=bF. The actual competitor g_m=-v(J_m)/m then satisfies
\[
 0\le p(f_{C_0})-g_m\le[(c+b)v(J)+v(J_Y)]/m
                         \le(c+a+b)N_J/m
\]
on EVERY support. This recognizes actual C positivity by uniform approximation, not by upper regularization alone. The all-support completion transport is already G331. These reconstruction gates agree with the corrected active formal argument at its stated isolated perfect-residue hypotheses; no extension to imperfect or mixed characteristic follows.

Active n5 audit: affine normality, monomialization of competitors, finite rational primary Newton polyhedra and rational approximation make its ALL-field weight-obstacle sector consistent. Its domination does not preserve an arbitrary nonmonomial obstacle. Own n1 uses instead finite contact constraints on competitors, with all-support integral dependence, and own n2 demonstrates an obstacle outside the weight-dependent class. Active n6 audit: extension of every R Cartier map for k[[s^2,st,t^2,z]] to the regular double cover uses the separable fraction extension, the explicit root base change on the s- and t-etale charts, and normal height-one coefficient intersection. The root translations with alpha_i>-1 and the lattice selection prove the stated strict test-ideal threshold. The capacity inequalities tend to the strict weight threshold, so arbitrarily late translations from the regular seed prove minimum stability. The parity argument excludes factorization of Uz^L into two allowed monomials for N>6L+9. This excludes a single primary correction for all ideals, not obstacle-dependent corrections or CE on the ring. Its finite regular cover explains why it is not an envelope counterexample.

Attempted general route and retained failure: replacing Jac by a fixed primary ideal contradicts that parity example. Multiplying or dividing a nonprimary Jacobian error at its supported infinity stratum yields no estimate. Allowing a correction depending on one obstacle does not fix the missing proof: one needs actual primary J_m and a correction whose normalized valuation error tends UNIFORMLY to zero, with a proved limit on supported strata. Saturating away a fixed test ideal or taking (tau_m:tau_0) has not been proved to preserve the needed subadditivity, trace generation or finite values on every support. This attempted route is diagnostic only. No general Jensen weak lower hemicontinuity and no genuine normal CE failure were obtained.

Audit limitation: the entire active seven-note chain and the essential immediate formal source units were examined; the whole ROOT392 proof was read. The inherited large B341/E350 appendices and entire 96986-byte book chapter are retained but NOT freshly independently audited here. Full primary publications' recursively cited proofs likewise are not declared freshly read. Thus this delivery does NOT claim to have completed the requested entire-current historical/source audit. It reports the active reconstruction and new complete scoped theorem, with the incomplete audit boundary explicit. The source/application/reading ledger lists exact fresh windows and repairs of display truncation. An input hash match or compiler record cannot fill that gap.

All 1269 bound records matched their expected byte hashes. The observed exact finite output of the own program is two facets, five vertices and 23 weight cases; source, input, output and environment are retained. No supervised heavy-compute facility was supplied or needed. No supplied/native program was imported/executed, no agent/additional model/native campaign was called, and no supplied/protected source, runtime, authentication, proxy, CA, editor, compiler, publication or catalogue state was changed. Source is deliberately uncompiled. Full sources/pixels/books remain LOCALONLY. Reproducible own commands: python prepare_delivery.py; python contact_certificate.py; python verify_delivery.py. Exact original task/problem/criteria are retained unchanged in original-task.json, original-problem.txt and original-completion-criteria.txt. Complete current actual/expanded/terminal objects remain separate in retained/.

Candidate=false. New progress is the full finite-contact theorem on EVERY excellent germ for arbitrary nonmonomial obstacles satisfying the barrier and contact conditions, its explicit normal nonisolated any-field and mixed-characteristic signed-primary families, and compatible normalization extension. Arbitrary normal nonisolated CE, arbitrary nonmonomial toric obstacles outside the contact sector, general imperfect-residue/mixed-characteristic/higher-dimensional excellent CE, a general Jacobian infinity-stratum repair, Jensen lower hemicontinuity, and a qualifying normal continuous-obstacle counterexample remain unresolved. The original 'when possible/appropriate regularity' and whole completion criteria are unchanged. P12.4 products, P12.5 energy and P12.6 full operators remain separate. Neither the original problem nor the complete requested audit is claimed solved.


# Entire retained active401 proof companion: historical DATA, not a premise

# n1. Whole corrected396 audit and the envelope criterion

This note uses only the entire qualified G331. The independently geometric core is its actual negative effective real Cartier presentations on actual primary blowups, tested by nonnegative degree on every contracted integral curve. Let C be its continuous uniform closure and D its actual decreasing-C-net completion, including bottom. Every prime support is retained. No envelope assertion is included in the grant. B341 and E350 are retained with their qualifications but are not needed below.

The entire 288-line corrected proof, all seven actual native276 notes with every field, their separate expanded framing, all current ledgers/coverage/verdict/residual, the 459-line ROOT392 proof, and the entire 386 mathematical appendix were examined. The standalone current TeX is 697312 bytes. An independently written serialization matches every nonempty line of the corrected proof and six ledger/scope blocks; all three full incoming grant texts occur literally. These facts identify duplicate content; they do not prove it correct or provide additional readings of historical sources. The terminal retention adds an artifact-location suffix to each actual note; this is separately retained. The actual native n2 text differs from corrected396 at the root-multiplier paragraph, and remains immutable.

The native assertion phi(d^q z)=d phi(z), for an R-linear phi:R^(1/q)->R, is false. In k[[x]] over a perfect field of characteristic3, q=3, use the free root basis 1,x^(1/3),x^(2/3) and the linear functional selecting the last basis vector. With d=x and z=x^(2/3), phi(d^q z)=x^3 whereas d phi(z)=x. The corrected formula is phi(dz)=d phi(z). Root multiplication by d is underlying Frobenius-source multiplication by d^q. The complete repair and full rooted-kernel argument are proved in n2; this note does not give the immutable paragraph a positive verdict.

For finite continuous f on the compact primary section X, define p(f)=sup{u in D:u<=f}. A sufficiently negative primary constant is a competitor. If g_i decreases in C to u<=f, the open sets {g_i<f+epsilon} cover X. Compactness and directedness select one term satisfying the inequality everywhere. Its negative constant shift g_i-epsilon is in C and below f, and is at least u-epsilon. Therefore C and D give the same raw supremum. It is finite, bounded, lower semicontinuous and nonexpansive in the uniform norm. Negative shifts in both directions prove the latter; no positive-translation invariance is used.

If p(f) is continuous, finitely many continuous competitors and their maximum approximate it uniformly from below, so p(f) belongs to C. If p(f) belongs to D, upper semicontinuity plus the preceding lower semicontinuity makes it continuous. Any maximal D minorant is greatest, since its maximum with another minorant is again a minorant. Conversely a greatest minorant equals the raw supremum. If the upper regularization p(f)^* belongs to D, continuity of f gives p(f)^*<=f, so it too is a competitor and equals p(f). Thus raw continuity, C positivity, D positivity, a greatest/maximal D minorant, and positive upper regularization are equivalent. Regularization by itself is not positivity recognition.

Actual decreasing closure of D needs a proof. On each normal centre G331 gives the zero dichotomy: a nonzero D function is everywhere strictly negative and hence bounded above by -c on the compact section. For u_i in D decreasing to u, either all terms are zero or a tail has this common bound. Given finite continuous F>u, compactness of the open strict tests selects u_i<F everywhere, then a continuous representing term g with u_i<=g<F and g<-c/2. A small positive b keeps (1-b)g below F and makes it strictly above u at each finite point, with bottom automatic. The family of continuous C majorants strictly above u is downward directed: apply this insertion to the continuous minimum of two majorants. Upper semicontinuity of u and a Urysohn cutoff give, at each point and finite t>u(x), a continuous F>u with F(x)<t. Insertion then shows this single decreasing net has infimum u. On a reduced germ pull back to the finitely many normal centres, apply the argument there, and use G331 full-fibre D descent. This avoids flattening nested representations and assumes no increasing closure.

If CE holds (p(f) in C for every continuous f), the finite continuous nonpositive majorants of min(phi,0), for bounded-above extended upper semicontinuous phi, are directed by minima and have that infimum. Their envelopes form a single decreasing C net. Its infimum is in D by the preceding closure proof, is below phi, and dominates every D competitor. This is the greatest D envelope. The same reasoning proves commutation with decreasing obstacle nets having a specified upper semicontinuous limit. The statements include poles and bottom.

For another primary gauge b, d(v)=v(b) and its inverse are bounded positive continuous. The section map T(v)=v/d(v) and the homogeneous rule u_b(Tv)=u_a(v)/d(v) give a bijection of competitors. Hence p_b(f_b)(Tv)=p_a(f_a)(v)/d(v), with the exact three-gauge cocycle. G331 already proves the all-support completion homeomorphism, exact primary contraction and C/D identification. The envelope transport is a corollary; it is not new algebraization or model-category equivalence.

The Jensen calculation was also checked, but remains a reduction. For positive Radon subprobabilities set J_x={mu:h(x)<=integral h dmu for all h in C}. They are nonempty compact convex sets with closed graph. Separate (f,t), t>p(f)(x), from the closure of {(g,s):some h in C has h<=g, s<=h(x)} in C(X) times R. Nonexpansivity keeps the point outside that closure. A separating functional has form mu(g)-alpha s, with mu positive and alpha>=0. Testing (-a,-a) rules out alpha=0, since then mu(X)=0. Normalize alpha=1; testing (h,h(x)) gives the Jensen inequalities, and h=-1 gives mass<=1. Let t decrease and use compactness to obtain p(f)(x)=min_{mu in J_x} integral f dmu. Conversely, failure of weak lower hemicontinuity of J_x is detected by finitely many continuous tests. Their compact convex projections avoid a fixed ball about a member of J_x; unit separating vectors have a convergent subnet and retain half the gap by uniform boundedness. A fixed linear combination of the tests then has discontinuous p. Thus CE iff this correspondence is weakly lower hemicontinuous. Hahn--Banach, Riesz and positive-dual weak compactness are named ordinary foundations. No general lower hemicontinuity is proved.

Audit verdict at this point: native276 is incorrect as written at the displayed scalar paragraph. Corrected396 repairs this defect. The remaining formal theorem is judged in n2--n4, with every mathematical gate reconstructed. Historical386 assertions were read as data; no historical acceptance or compilation is a correctness premise. The normal raw envelope of an obstacle negative somewhere is uniformly negative: divisorial density finds nu with f(nu)<0, and G331's g(nu)>=A_nu g(v) gives p(f)(v)<=f(nu)/A_nu. A mixed-zero normal counterexample cannot be inferred from the nonnormal example or increasing spikes.

Evidence: reports/input-integrity.json records 1258/1258 bound records matching; reports/serialization.json records the complete current-content identity and separate actual/expanded/terminal framing. Full actual fields remain in review-data/actual-FINAL and expanded fields in review-data/expanded. Rerun: python audit_packet.py; python audit_serialization.py. These are own data readers, not supplied programs. No compiler, agent, network or heavy computation was used.

# n2. Corrected completed free lift and full root kernel

All statements here are reconstructed; neither corrected396 nor ROOT392 is a grant. Let R be a complete normal local domain of characteristic p>0 with perfect coefficient/residue field k. Set S=R completed-tensor_k R, multiplication mu:S->R, I=ker(mu), q=p^e, and T=R^(1/q). A presentation R=k[[u]]/(f) gives S=k[[u,v]]/(f(u),f(v)), a Noetherian complete local ring. Exponent grouping and perfect coefficient roots make both rings F-finite and identify S^(1/q)=T completed-tensor_k T. The compatible kernel is I^(1/q), the whole kernel of root multiplication, not merely the extension of I to the root ring.

Here is the exactness argument needed for these completed tensors. A finite module V over R is the inverse limit of its finite-dimensional k quotients; its continuous dual V^o is their direct-limit dual. Artin--Rees makes a finite submodule's induced topology cofinal with its adic topology. A continuous functional on a submodule extends through a sufficiently deep finite quotient. Thus continuous duality is exact on the relevant finite-module sequences. Algebraic vector-space tensor and duality are exact, and
\[
 V\widehat\otimes_k W=(V^o\otimes_k W^o)^*.
\]
This proves completed exactness in either slot. It does not appeal to completion over an uncompleted non-Noetherian tensor ring. Applied twice to R->R^(1/p), it makes S->S^(1/p) injective. This is the Frobenius map under the root presentation, so S is reduced.

Present finite R modules M,N by finite free modules. In S^(ab), impose the M-relation matrix, then the N-relation matrix. Completed exactness identifies the first kernel with Hom_R(M,R) completed-tensor R^b and the second with the corresponding completed tensor of Hom modules. Therefore
\[
\operatorname{Hom}_S(M\widehat\otimes_k N,S)
=\operatorname{Hom}_R(M,R)\widehat\otimes_k\operatorname{Hom}_R(N,R).
\]
This is the full Hom factorization, including finite ideals/twists and every S Cartier map. Finite paired generators generate the right-hand module; no decomposability assertion for individual maps is needed.

If a regular Noetherian subring A makes R module finite, integral locality makes A local. Its maximal-adic and R maximal-adic topologies on R are cofinal. Exact completion embeds A-hat in R, so A-hat/A is a finite A module, with zero residue quotient. Nakayama gives A=A-hat. The residue field F has finite extension k; perfection of k and [k:F]=[k^p:F^p] force F perfect. Cohen structure then gives A=F[[x]], whose roots are finite free. This broader ROOT392 claim is valid, but the Jacobian sum below uses only the fixed common field k.

Fix A=k[[x_1,...,x_d]] inside R, finite over A. Let K_A=Fitt_0 Omega_(R/A) and N_A=mu_A(Ann ker(mu_A)) in R tensor_A R. A finite polynomial presentation R=A[z]/(g) expresses differences g(z tensor 1)-g(1 tensor z) as a matrix times the diagonal generators z_i tensor1-1tensor z_i. Each square adjugate makes its determinant annihilate all these generators. After multiplication its determinant is the corresponding relative Jacobian minor. Hence K_A subset N_A. This uses ordinary finite relative differentials and no CM or A-flatness.

For K_A nonzero the fraction field extension L/K is separable. If d in N_A, choose z=sum r_i tensor s_i annihilating the diagonal with product d. Over L tensor_K L, z is d times the separability idempotent. The trace in the second slot gives
\[
d w=\sum_i r_i\operatorname{Tr}(s_i w).
\]
The purely inseparable extension K^(1/q)/K is linearly disjoint from L/K, and L K^(1/q)=L^(1/q). The same identity holds there. Elements of R^(1/q) are integral over A^(1/q), so their trace coefficients are integral and in its fraction field. Normality of the regular A^(1/q) puts them in A^(1/q). Consequently dT subset A^(1/q)[R]. The multiplication of P=A^(1/q) tensor_A R into L^(1/q) is injective: its generic map is an isomorphism and the free R module P is torsion-free over A. Thus P is the indicated submodule of T and is finite free over R. Freeness of R over A is not asserted.

Set B=R completed-tensor_k T. The multiplication B->T is surjective and B-linear. The module P completed-tensor_k T is free over B, so its multiplication into T lifts to a B-linear map Psi into B, by lifting its finite free basis. Compose
\[
T\widehat\otimes_k T\xrightarrow{,d\otimes1,}
P\widehat\otimes_k T\xrightarrow{\Psi}
R\widehat\otimes_k T\xrightarrow{1\widehat\otimes\phi}S
\]
for any R-linear phi:T->R. This is S-linear with the Frobenius root source action. On pure tensors, applying mu gives phi(dxy)=d phi(xy). Finite-module continuity extends this equality to the completed tensor. Its reduction therefore factors through the surjective root multiplication to T. It takes the ENTIRE kernel I^(1/q) into I, and induces the OUTPUT multiple d phi. In the identification F_*^e z->z^(1/q), the first arrow uses underlying source multiplier d^q. Multiplication by d^q in T would instead induce d^q phi, the immutable error demonstrated in n1. No claim about only pure tensors or the ordinary extended diagonal kernel suffices.

Let D_e be the quotient-restriction image of all compatible S maps in C_e=Hom_R(F_*^e R,R). These finite kernel/image modules form a Cartier algebra: lift left/right scalars arbitrarily to S and compose compatible maps. The root kernel remains preserved. Summing lifts over finitely many parameter normalizations proves J_norm C_e subset D_e for every degree, where J_norm=sum_A K_A.

Wang's fixed-coefficient-field Definition4.1/4.2 and whole Lemma4.3 identify this sum with the formal Jacobian Fitt_d of continuous differentials. Finite residue fields require no generic rational-coordinate assumption: prescribe a basis modulo m^2, and at each stage avoid the finitely many nonmaximal minimal primes of subset-generated ideals. Discard contained primes. For incomparable P_i, choose a_i in m^2 intersect all other P_j but outside P_i, using products and prime avoidance. Add a_i only where the original representative lies in P_i. Its cotangent coset is unchanged and every bad prime is avoided. The height theorem/catenarity preserves the expected drop for every subset, so each d-subset is a parameter system. Formal coordinate changes preserving the cotangent basis have invertible Jacobian. Their complementary minors give the required finite sum exactly as in Wang. This explicitly repairs the finite-field reading boundary.

The singular-locus criterion used is ONLY for reduced equidimensional complete equicharacteristic rings with perfect residue. Liu4.8--4.9 and immediate proof state it; Wang4.5 and its entire postponed proof supply the pertinent source context. All six official printed pages597--602 were actually viewed and their text units read in this run. The cited analytic universal-finite results, Matsumura criterion and earlier historical foundations remain named published background, not newly recursively proved. Iyengar--Takahashi's complete definition and Section3 block corroborate but do not replace the fixed-field Wang sum. No Ext/CM theorem is applied. The criterion gives J_norm nonzero; isolatedness gives a primary power in it.

Verdict: corrected completed module/different theorem and the amended ROOT392 direct algebraic part are valid at these exact hypotheses. ROOT392's BIG-product application was conditional and is discharged separately in n3. S was proved reduced, not normal. Matching files and old correctness labels were not used as mathematical premises.

Artifacts: n2.md; reports/finite-diagnostics.json includes the exact scalar counterexample. Primary statements/pixels remain under inputs/primary-LOCALONLY, including Wang page11--16. Rerun: python finite_diagnostics.py. No supplied program or compiler is executed.

# n3. BIG minima, late tails, and the actual completed diagonal

Use the completed module and lift theorem of n2, not a grant from396. Let B be reduced excellent Noetherian F-finite. Let C be a Cartier subalgebra with finite degree modules and C_0=B. Assume c in B^o has B_c regular, all C_e become the full Hom modules there, and finitely many regular-element pair ideals a_i become units there. These explicit regular-open hypotheses will be verified for the product and diagonal; no graded finite generation is presumed. Put r_i(e)=ceil(t_i(p^e-1)). Stability means that all maps in C_e take F_*^e((product a_i^r_i(e))H) into H. The twisted maps compose because r_i(e)+p^e r_i(f)>=r_i(e+f).

Every stable H meeting B^o has H_c=B_c. At a regular maximal localization of B_c, F-finiteness and Kunz give a finite free Frobenius module. A regular h in H is outside n^[q] for large q, since n^[q] subset n^q and Krull intersection. Thus F_*h is primitive in that free module and a linear map sends it to1. Hom localization holds by finite presentation; localized stability gives the unit ideal. This holds at every maximal localization. Kunz is the named ordinary theorem at exactly regular Noetherian characteristic-p rings; its full statement in Smolkinv3 2.3 was read, not its entire original historical proof.

There is one universal power of c in EVERY such H. Choose a positive degree q. Evaluation at1 splits on B_c; clear denominators to obtain theta in C_e with theta(F_*1)=c^a. Choose B_0 so c^(q B_0) belongs to that degree's pair coefficient ideal. For the least n with c^n in H, stability and the Frobenius scalar rule give c^(B_0+ceil(n/q)+a) in H. Therefore
\[
n\le B_0+a+\lceil n/q\rceil\le B_0+a+n/q+1,
\qquad n\le\frac{q(B_0+a+1)}{q-1}.
\]
Fix an integer L at least this bound. The intersection of all stable ideals meeting B^o is stable and contains c^L in B^o, so it is the actual smallest such ideal tau. This is BIG, not finitistic. The ideal generated by all twisted maps of an arbitrary regular d, with degree zero included, is stable and generically nonzero, and therefore contains c^L. Thus the construction supplies the required universal BIG test element, rather than assuming arbitrary-Cartier-algebra existence.

If d belongs to tau intersect B^o, every late tail generated by twisted images of dB lies in tau. Composition shows the tail is stable. On B_c the pair ideals are units; for each maximal localization a sufficiently large degree sends the regular d to1 by the preceding primitive-vector argument. Hence the tail is generically nonzero and minimality makes it equal tau. This holds for EVERY cutoff E, not merely for all degrees starting at0.

Both exponent conventions ceil(t_i q) and ceil(t_i(q-1)) give the same ideal and all their late tails. Their gaps are bounded by ceil(t_i)+1 independently of e. Construct the minima for both conventions by the same argument and choose a common regular seed in their intersection. Multiplication by a fixed regular element of product a_i^(ceil(t_i)+1) is enough to bridge the bounded gaps. Since a seed in tau can be multiplied by a regular element and remains a seed, the two tail sums sandwich each other. The same argument proves power invariance tau((a^r)^(t/r))=tau(a^t): the exponents ceil(qt) and r ceil(qt/r) differ by at most r-1. No finite-tail approximation or Q-Gorenstein index enters.

Localization of these ideals follows from finite Hom localization and shared nonzero seeds. Full-algebra completion is also exact for excellent F-finite normal local A: the m-adic and Frobenius filtrations are cofinal, so F_*A completes to F_*(A-hat), and finite Hom commutes with faithful flat completion. Extending tau_A is stable, giving tau_hat subset tau_A A-hat. Choose c in A with A_c regular and pair ideals unit. Regular formal fibres make A-hat_c regular; the same cleared splitting supplies a common c^L in tau_hat. Its contraction is nonzero and stable, giving the reverse inclusion. An arbitrary nonzero formal ideal is never assumed to have nonzero contraction. This proves the completion rule for full algebras only.

If J C_e subset D_e, the correct comparison is J tau_C subset tau_D. Choose a regular seed in both minima. The C late-tail formula expresses tau_C; multiplying each output by J turns the map into a D map, whose image of the common seed lies in tau_D. This proves the comparison without claiming J tau_C is itself D-stable.

Return to n2's S. It is reduced F-finite and equidimensional of dimension2d. Indeed a parameter ring A_0=k[[x_1,...,x_d]] makes R finite torsion-free. Clear denominators of a generic basis to embed R in a finite free A_0 module. Completed exactness embeds S in a free module over k[[x,y]]. Every minimal prime of this finite torsion-free algebra contracts to0, so all minimal quotients have dimension2d. A nonzero d-codimensional Jacobian minor j of R yields the block minor j(u)j(v) in Jac(S). At the diagonal prime I its image is j^2, nonzero in R. The exact reduced-equidimensional perfect-residue singular-locus criterion of n2 makes S_I regular. No S normality or product-domain assertion is needed.

Choose regular a_0 in a and b_0 in b and set c_S=j(u)j(v)(a_0 tensor b_0). Completed exactness makes multiplication by a_0 and b_0 injective in their slots, and similarly for j; thus c_S is regular. Its diagonal image j^2 a_0 b_0 is nonzero. On S_cS the ring is regular and both pair ideals A=aS, B=bS are units. For R's diagonal algebra D, n2 gives j C_e subset D_e, so localization at j is full and regular. Thus the BIG framework applies to all three actual algebras.

Let T_S=tau_S(A^t B^s). Its image mu(T_S) is D-stable: compatible lifts carry its coefficient-twisted roots into T_S, and passage to the quotient gives the required maps. Its image is nonzero because it contains mu(c_S^L). Minimality therefore gives tau_D(a^t b^s) subset mu(T_S).

The completed product of tau_R(a^t) and tau_R(b^s), extended into S, is stable for EVERY full S Cartier map by n2's full Hom factorization and stability in each factor. It contains a regular pure tensor, again by completed exactness, so T_S lies in this product ideal. Multiplication sends it to tau_R(a^t) tau_R(b^s). Combining the common-seed comparison with these two inclusions gives
\[
\operatorname{Jac}(R)\tau_R(a^t b^s)
\subset\tau_D(a^t b^s)
\subset\mu(T_S)
\subset\tau_R(a^t)\tau_R(b^s).
\]
Iteration yields Jac^(ell-1) tau(a^(ell t)) subset tau(a^t)^ell. This is the corrected direction. A primary multiplier is obtained only under isolatedness; no finite value of a nonprimary Jacobian on every support is inferred.

Verdict: the complete formal BIG/subadditivity gate is discharged for complete normal characteristic-p perfect-residue R, with no finite-type-over-field, CM, algebraizability, Q-Gorenstein or graded Cartier-finite-generation assumption. The verification uses the explicit nonzero diagonal seed, rather than a guessed image theorem. Local source and arithmetic checks are evidence, not a correctness grant.

Artifacts: n3.md and proof-companion.md. Own finite seed/rounding proofs are universal arguments above; reports/finite-diagnostics.json concerns only the later new semigroup example. Rerun: python build_delivery.py; python check_delivery.py. Neither command runs a compiler or any supplied program.

# n4. Entire isolated formal envelope chain and scoped verdict

Use n1--n3 and the full qualified G331. Let R be complete normal local, characteristic p>0, perfect residue, isolated singularity, dimension d>=2. This note reconstructs the entire model/trace/primary approximation chain. In dimension1 R is a DVR; dimension0 has empty boundary. No algebraizability, CM, Q-Gorenstein or resolution is assumed.

First justify model transfer. Exponent grouping in R over R^p makes ordinary Omega_(R/k) finite: every element is a finite sum b_i^p u^i and every k-derivation kills the pth powers and the perfect field. This agrees with continuous formal differentials. A finite-type affine model algebra A is F-finite and has finite Omega_(A/k). Grouping over A^p and cofinal filtrations similarly gives Omega_(A/k) completed at a closed point equal to the formal differential module of its completion. Its closed residue field is a finite extension of perfect k, hence perfect. Hensel lifting of that finite separable extension gives a coefficient field compatible with k, and its differentials vanish. Closed points of a projective birational model over this local base lie above m and have local dimension d by catenarity and the residue/dimension formula. Normality, F-finiteness and excellence pass to their completions. Consequently the dth Fitting Jacobian and full BIG ideals commute with this completion. Apply n3 at every completed closed model point and descend by faithful flatness. A coherent failure elsewhere has closed support and a closed point, so the Jacobian subadditivity holds on the entire model.

CEMS1412.6453v4 Setting2.1 explicitly includes schemes essentially of finite type over an F-finite LOCAL base with dualizing complexes and the stated Frobenius-duality compatibility. The complete base R has a dualizing complex, and the projective models inherit one. The canonical sheaf used is the divisorial reflexive rank-one sheaf, not a locally free CM canonical module. Definition2.2 and Lemmas2.3--2.4 with their entire immediate proofs give the BIG trace formula, localization, monotonicity and Cartier shift at precisely this setting. Those immediate units were read in full. Their finite-duality/divisor foundations are named ordinary published background; no anti-canonical finite generation or Lemma2.10 is used. The following globalization uses their arbitrary-late formula, with BIG existence, roundings and seeds already proved in n3.

Principalize any finite primary collection, including the gauge, on its product blowup and normalize. Its pulled-back exceptional F_0 is actual Cartier with full-fibre positive coefficients and relatively ample negative bundle. On this normal model omega has rank one. Blow up Fitt_1(omega). On an affine G/a blowup chart, discard a-power torsion in the pullback. The full Stacks15.27.3--4 proof makes its first Fitting ideal unit. Its zeroth Fitting ideal vanishes after inverting a and hence vanishes in the chart domain. The full15.8.8--9 criterion makes the strict transform a rank-one line bundle. Normalize and pull back that bundle. Choose the SAME rational section for its Cartier divisor L_0 and for K_Y; they agree on the puncture. Thus K_Y-L_0 is an exceptional Weil divisor. For sufficiently large r,
\[
\Delta=rF_0-(K_Y-L_0)\ge0,\qquad K_Y+\Delta=L_0+rF_0=:L
\]
is Cartier. This allows non-CM models throughout.

The negative Fitting blowup bundle times a sufficiently high pullback power of O(-F_0) is ample; finite normalization preserves it. A high power A=O(-F), H=-F, is very ample and generated with full-fibre support. Its global sections J belong to R by normal Hartogs, are finite by proper coherence, unit off m and proper because they vanish on the nonempty fibre. Generation gives J O_Y=A. Very ample section generators give a closed immersion into the projective space of J; its integral image and Bl_J R have the same dense punctured graph. Scheme-theoretic closure proves Y=Bl_J R. This is an actual primary model in G331, rather than an assumed cofinal arbitrary model. Every prescribed factor remains invertible.

The coherent model Jacobian J_Y is unit on the puncture. Full-fibre support and a finite affine cover give integers a,b,N_J with J^a O_Y subset J_Y, Delta<=bF, and a_gauge^N_J subset J. The inequalities imply v(J_Y)<=a v(J)<=a N_J at EVERY support. This primary containment is the precise use of isolatedness.

For an integral signed exceptional Cartier obstacle C_0, set for EVERY m>=1
\[
I_m=\Gamma(Y,O(mC_0)),\quad
b_m=I_mO_Y O(-mC_0),\quad u_m=-v(I_m)/m.
\]
Hartogs gives I_m subset R. An actual Cartier order-unit bound C_0>=-M F_gauge gives a_gauge^(Mm) subset I_m. Therefore I_m is unit or primary at every index. Section products are graded and u_m=f_(C_0)-v(b_m)/m<=f_(C_0) at all valued centres, using the support quotient field and canonical punctured trivialization of the invertible sheaf. No total fraction field is mapped through a nonzero support.

For each v, v(I_m) is finite nonnegative and subadditive. Writing arbitrary indices as multiples plus bounded remainders proves the ALL-index Fekete limit u_m->sup_m u_m, without monotonicity of the sequence. A rational primary profile -v(I)/q below f_(C_0) satisfies the requisite order at every exceptional height-one point of the normal Y; at other height-one points it is automatically regular. The normal codimension-one section criterion gives I^r subset I_(rq) for all r. It follows that every rational competitor is below the Fekete limit. Rational density with negative shifts handles C; n1 handles D. Thus BEFORE positivity recognition,
\[
p(f_{C_0})=\lim_m u_m=\sup_m u_m,\qquad h=f_{C_0}-p(f_{C_0})\ge0.
\]

Define t_m=tau(Y,Delta,b_bullet^m) and s_m=tau(Y,b_bullet^m). Gradedness and n3 power invariance direct their defining families by common multiples. Noetherianity on a finite affine cover makes each stabilize at a common index for any finite list. The transferred subadditivity gives J_Y^(ell-1) s_(m ell) subset s_m^ell, with the correct direction.

A scheme-global effective Cartier test divisor D_0 exists. On a finite affine cover choose the BIG seeds and finite Weil rounding corrections. Dominate their divisors by an effective Weil E. A high ample negative-fibre twist of O(-E) is generated; a nonzero rational section has divisor at least E and cuts an effective Cartier divisor D_0>=E. Normal height-one regularity makes its local equations multiples of every chosen seed. By n3 any such regular multiples still give EVERY late tail. CEMS therefore yields, for a chosen stabilizing ell and every cutoff E_0,
\[
t_m=\sum_{e\ge E_0}\operatorname{Im}
\left[F_*^e\big(b_\ell^{\lceil q m/\ell\rceil}
 O(K_Y-qL-D_0)\big)\longrightarrow O_Y\right].
\]
D_0, ell and the Serre threshold may depend on m. The generation constant below does not.

The relative Koszul generation statement works over ANY Noetherian affine base. If A is ample generated and H^i(M A^(-i))=0 for 1<=i<=dim Y, choose finitely many generating sections. Their Koszul complex is locally split exact, so remains exact after tensoring M. Its higher groups successively prove the same vanishings at the next twist and surjectivity of multiplication by the generating sections. Beyond dim Y coherent cohomology vanishes. Repetition and high Serre generation show M generated. There is no flatness hypothesis on M or the base. Thus choose c_0 once so (c_0-i)H-L is ample for every required i. For each fixed finite coherent list M_j,
\[
F_*^e(M_j O(q(c_0H-L)))
\]
is generated for all sufficiently late e: projection formula makes the Koszul vanishings Serre vanishings for (c_0-i)H-L. Frobenius is finite; all sheaves are coherent.

Put a_e=ceil(qm/ell), j_e=ell a_e-qm, so 0<=j_e<ell. Products of the actual global I_ell sections generate b_ell^a_e O(ell a_e C_0). After twisting the trace target by O(mC_0+c_0H), its source is a quotient of finitely many copies of
\[
Q_{e,j}=F_*^e O(q(c_0H-L)+K_Y-D_0-jC_0).
\]
The multiplication is F_*t->F_*(s t), INSIDE Frobenius; coefficients are not extracted as ordinary R scalars. For fixed m the finite list j=0,...,ell-1 is coherent even when K_Y is not Cartier. The preceding regularity argument generates every sufficiently late source. The arbitrary-tail trace formula permits restriction to those degrees. A finite coherent image sum stabilizes on the quasicompact Noetherian scheme, possibly using DIFFERENT late exponents. Its target t_m O(mC_0+c_0H) is therefore generated. One exponent realizing the whole trace is neither asserted nor needed.

Set c=c_0+1. The sections of F_m=t_m O(mC_0) A^c form an actual ideal J_m of R, with J_m O_Y=F_m. Before the extra A twist the generated sheaf's sections are in R by Hartogs and it embeds in O_Y; afterwards it lies in J O_Y. Thus J_m is proper. Let T_0=tau(Y,Delta), unit on the puncture and containing J^r O_Y. The tail formula and the identity f phi(F_*z)=phi(F_*(f^q z)) give b_m T_0 subset t_m, by a common regular seed and the bounded exponent gap. Consequently I_m J^(r+c) subset J_m, proving primaryness for EVERY m. Its actual geometric profile satisfies
\[
g_m=-v(J_m)/m=f_{C_0}-(c v(J)+v(t_m))/m\le f_{C_0}.
\]

Now b_(m ell) T_0 subset t_(m ell) subset s_(m ell), and J_Y^(ell-1) s_(m ell) subset s_m^ell, yield
\[
\frac{v(s_m)}m\le
\frac{v(b_{m\ell})+v(T_0)}{m\ell}
 +\frac{\ell-1}{m\ell}v(J_Y).
\]
All values here are finite because the ideals contain closed-fibre primary powers. FIRST let ell tend to infinity pointwise. Fekete gives v(s_m)<=m h+v(J_Y); the finite v(T_0) term disappears. Cartier shift and Delta<=bF give O(-bF)s_m subset t_m subset s_m. Since g_m is already an actual competitor, substitution proves
\[
0\le p(f_{C_0})-g_m
\le\frac{(c+b)v(J)+v(J_Y)}m
\le\frac{(c+a+b)N_J}{m}
\]
on the ENTIRE link. The last step, after the pointwise limit, is uniformly primary and retains all nonminimal supports. Hence the raw envelope is in C. Signed rational primary lattice functions are dense by G331; each is determined by a finite collection principalized above. Clear denominators and use n1 nonexpansivity to obtain CE for every finite continuous obstacle.

The greatest D envelopes for bounded-above extended upper semicontinuous obstacles, decreasing-obstacle-net continuity and exact gauge cocycle now follow from n1. G331 completion transports the result exactly to excellent normal characteristic-p local rings whose completions have perfect residue and are regular away from the maximal ideal. Isolated excellent normal rings with perfect residue satisfy this: normal completion and regular formal fibres give regularity over every nonmaximal regular prime, and the fibre over m is the residue field. This is existing G331 completion transport, not new algebraization. At smooth closed affine algebraically closed characteristic-zero germs G331 gives the exact published BFJ class; the historical BFJ envelope comparison remains at that scope, not at arbitrary singular/imperfect germs.

Independent scoped verdict: PASS corrected396's entire new formal BIG theorem and isolated perfect-residue formal CE theorem, as unverified mathematical drafts relative to G331 and the named ordinary foundations. The immutable native paragraph is rejected; corrected396 is accepted only after the explicit n2 repair. No new gap was found in the stated isolated chain. This judgment is not mathematical certification, publication, a catalogue action or a grant derived from compilation. General P12.3 is not closed.

Artifacts: n4.md, proof-companion.md, independent-scoped-verdict.md, source-application-ledger.md. Rerun: python build_delivery.py; python check_delivery.py. Source is deliberately uncompiled; essential private primary bodies and pixels remain LOCALONLY.

# n5. New positive sector: all monomial-weight obstacles on complete normal toric germs

Use G331 and the raw-envelope/nonexpansivity/decreasing-closure results proved in n1. This is new scoped progress on the original envelope target, valid over ANY field, including imperfect fields and every characteristic. It concerns actual geometric positivity and all geometric competitors, not a new order definition or a restriction to radial functions on a finite link.

Let M be a lattice of rank d, C_0 a pointed full-dimensional rational polyhedral cone in M_R, and S=C_0 intersect M its saturated positive monoid. Let R be the completion at the monomial maximal ideal of k[S]. For precision, k[S] is the intersection, in its fraction field, of the normal Laurent polynomial ring k[M] with the valuation rings given by the finitely many primitive facet weights. On a Laurent polynomial the least facet weight is the least term weight, so these inequalities mean that every exponent belongs to C_0 intersect M. This proves the asserted intersection and hence normality. Finite generation is the elementary rational-cone lattice-point theorem. The finite-type ring is excellent, and excellent normal completion is normal; thus R is an excellent normal local domain. Its elements are formal sums of monomials chi^u, with the maximal-adic completion topology. Fix a monomial primary gauge a. G331 supplies its full all-support compact boundary X and independently geometric C,D. These conventional algebraic foundations are used at this exact saturated positive affine-monoid setup; no perfect-field base change or torus averaging is used.

The monomial weight of v is w_v(u)=v(chi^u). It is additive, may take infinity, and is strictly positive on nonzero monoid elements when finite. The finite-valued elements form a face of S. For finite weights w in the interior of the dual cone sigma=C_0^vee, taking the least weight of the terms defines a monomial valuation v_w on the completed ring. Positivity makes the least value well-defined and makes the operation compatible with the completion. Distinct monomials in its associated graded cannot cancel. Divide by w(a) to obtain its primary-section point.

Every extended monomial weight arising from v is a limit of these finite interior weights, after normalization. Indeed its finite face is cut out by a rational exposing functional lambda>=0, zero on that face and strictly positive on its complement. Extend its finite additive weight linearly from the face span to M_R. Add N lambda, and if necessary a vanishing small positive interior functional. For large N the finitely many monoid generators outside the face become positive, and the generators inside the face have their given positive values. The outside values tend to infinity. Some primary-gauge generator has finite value; hence normalized primary values converge as well. Monomial primary profiles are continuous on all X by G331. Thus inequalities between such profiles and signed monomial obstacles, checked on finite interior weights, hold on every extended monomial weight and hence on EVERY semivaluation having that weight.

For any ideal I of R, let M(I) be the monomial ideal generated by all monomials appearing with nonzero coefficient in a finite set of formal generators. Noetherianity makes this ideal finitely generated. A monomial ideal is maximal-adically closed, since its finite-module quotient is separated; therefore each series whose terms lie in it belongs to it. Hence I subset M(I). If I contains a primary power then so does M(I). At a finite interior monomial valuation, v_w(I)=v_w(M(I)): the least appearing monomial realizes the value and cannot cancel. At a general semivaluation, -v(M(I))>=-v(I). This is a domination of arbitrary ideal profiles, proved by term membership, not by an averaging operation over k-rational torus points.

Consider a rational signed monomial primary obstacle on rays,
\[
F(w)=\frac{w(A)-w(B)}r,
\]
where A,B are monomial unit-or-primary ideals and r is a positive integer. Finite lattice combinations are of this form by synchronized products and sums. On X its restriction f is finite continuous. Write phi=-F, a homogeneous rational piecewise-linear function on sigma. Common normal fans of the finite exponent sets of A and B make phi linear on finitely many rational cones. Define
\[
P=\{x\in C_0:\langle x,w\rangle\ge\phi(w)\text{ for all }w\in\sigma\}.
\]
These conditions reduce to the finitely many rays of that fan, together with the cone inequalities. Thus P is a rational polyhedron. Because |f| is bounded on the a-section, phi(w)<=T w(a) for a finite T. Therefore P contains T times the Newton polyhedron of a and is nonempty. Its recession cone is exactly C_0. The finite polyhedral vertex/recession decomposition, obtained by successively moving a nonvertex to bounding faces, gives P=conv(x_1,...,x_h)+C_0, with rational vertices. Pointedness rules out a lineality factor.

Clear denominators with q so q x_i belong to M and hence S. Add sufficiently large powers of EACH monoid generator to the ideal generated by chi^(q x_i). These added exponents can be chosen inside qP: for a fan ray w with w(u)=0 on a nonzero monoid generator u, primaryness implies w(a)=0 and hence phi(w)=0. All remaining finite inequalities are met by a sufficiently large multiple of u. Call the resulting monomial ideal J. Its radical is the maximal ideal, unless P contains0, in which case include1 and use the unit ideal. Adding these points does not change its Newton polyhedron, which is qP. Thus
\[
h(w):=\min_{x\in P}\langle x,w\rangle=w(J)/q,
\qquad -h\le F
\]
for finite weights, and the preceding extended-weight continuity proves -v(J)/q<=f on ALL supports. This is an actual primary ideal profile and hence an actual negative effective curve-nef Cartier presentation on Bl_J R by G331's independently proved geometric comparison/core inclusion.

It is the raw envelope among ALL geometric competitors. For any rational arbitrary-ideal profile -v(I)/l<=f, equality at monomial valuations shows -v(M(I))/l<=f there and hence everywhere, while this monomialized profile dominates the original. Each generating exponent u of M(I) satisfies u/l in P, so w(M(I))/l>=h(w); the same domination holds at extended weights by continuity. Consequently -v(I)/l<=-v(J)/q at every semivaluation. To handle C competitors, approximate by rational primary profiles, then make a negative rational gauge shift to keep them below f. Their errors vanish. N1 identifies the C and D raw suprema. Therefore
\[
p(f)=-v(J)/q\in C_{\rm geom}
\]
and this is the greatest D minorant. This controls arbitrary nonmonomial ideal profiles, their real uniform limits, and completed D competitors; it is not merely a toric-restricted supremum. The formula gives a finite rational polyhedral construction for every rational signed monomial model obstacle.

Let W be the compact image of X under all monomial evaluations. Primary monomial profile differences contain rational constants, form a lattice by products and ideal sums, and separate W using (chi^u)+a^N, whose value is min(w(u),N). The compact lattice approximation proof therefore makes their rational span uniformly dense in C(W). For every finite continuous obstacle f=F_0 composed with the weight map, choose such rational signed obstacles tending uniformly to it. N1 nonexpansivity makes their raw envelopes uniformly Cauchy. Their limit is p(f), belongs to C_geom, and is weight-dependent. Thus EVERY finite continuous monomial-weight obstacle has an actually positive continuous envelope, not just the rational ones.

For a bounded-above extended upper semicontinuous obstacle on W, take all finite continuous nonpositive majorants of its clipping to0, directed by minima. Their envelopes are in C_geom by the preceding theorem and form one decreasing net. N1 decreasing closure shows its infimum is in D_geom; it is below the obstacle and dominates every D competitor. This gives its greatest D envelope, with the appropriate upper semicontinuity, poles/bottom, and decreasing-obstacle-net stability for specified upper semicontinuous limits. The ray formulation and n1 give the exact gauge cocycle for ANY primary section; changing a monomial gauge is the immediate weight-coordinate formula. At these normal germs normalization is the identity and conductor fibres are singletons. No nonnormal monomial descent theorem is asserted.

This includes normal nonisolated toric germs of arbitrary dimension and monomial-weight obstacles over imperfect residue fields. For example k[[s^2,st,t^2,z]] has a nonisolated singular line in dimension3. The nonsimplicial rank3 saturated cone generated by (1,0,0),(1,1,0),(1,0,1),(1,1,1) gives k[[a,b,c,d]]/(ad-bc); adding formal monomial variables gives nonisolated examples. The theorem does NOT prove CE for arbitrary obstacles that distinguish valuations with the same monomial values, or for arbitrary excellent germs. Its smooth specialization uses the same G331 cone; in the published smooth affine closed/algebraically closed/characteristic-zero range it is the restriction of the BFJ envelope, because both are greatest minorants of that identical class. This does not extend BFJ's published hypotheses or identify literal analytic/CLD radial extensions.

Artifacts: n5.md, toric_envelope.py, inputs/toric-examples.json and reports/toric-envelopes.json. The own exact program implements the finite rational fan/vertex construction for its two explicitly supplied rank3 examples; its finite outputs are certificates of those computations, not a proof of the universal theorem. Rerun: python toric_envelope.py. No supplied code, solver, compiler, field extension, network or resource-heavy computation is used.

# n6. New normal nonisolated obstruction to a universal primary correction

Use the explicit BIG convention in n3 and the toric setup of n5 only at its stated scope. The calculation below proves its all-map test-ideal formula independently; no toric test-ideal formula or finite-map operator is imported. Let k be perfect of odd characteristic p, and
\[
R=k[[U,V,W,z]]/(UW-V^2)=k[[s^2,st,t^2,z]],
\quad B=k[[s,t,z]],\quad P=(U,V,W).
\]
R is an excellent normal three-dimensional domain, and its singular locus is the formal line P. This follows from the saturated monoid or the hypersurface and its codimension-two Jacobian locus. Write monomials as chi^m=s^a t^b z^c, with m in M={(a,b,c) in Z^3:a+b even}, all coordinates nonnegative. For N>=1 set A_N=(U,W^N,z^N), a genuine primary ideal, and
\[
w_N(a,b,c)=a/2+b/(2N)+c/N,\qquad
H_{N,t}=\langle\chi^m:w_N(m+(1,1,1))>t\rangle.
\]
We claim tau_R(A_N^t)=H_(N,t) for every real t>=0, using stability exponents ceil(t(q-1)).

First every R Cartier map extends to a B Cartier map. The fraction field extension L/K is separable quadratic; purely inseparable root extension gives L tensor_K K^(1/q)=L^(1/q). Hence an R-linear phi extends uniquely to an L-linear map on L^(1/q). Outside (s,t) the finite cover is etale: where s is invertible, B is given by S^2=U with derivative2S a unit, and similarly for t. Frobenius root base change on this chart is explicit, since s^(1/q)=s (U^(1/q))^(-(q-1)/2), with t=V/s; the t-chart is analogous. Thus the extended map carries the root module into B at every height-one localization. Since B^(1/q) is finite free and B is normal, the intersection-of-height-one-localizations criterion makes all its coefficients integral globally. The extension is an actual B-linear map B^(1/q)->B. Codimension-two etaleness and normality, not a general trace theorem, justify this step.

In the regular ring B, the root monomials with residues0,...,q-1 in each coordinate form a free basis. For any monomial chi^h in a source and any output monomial chi^n of any B Cartier map, these basis expansions give
\[
q n_i+(q-1)\ge h_i\quad(i=1,2,3).
\]
The map coefficients are power series with nonnegative exponents. Thus cancellation can only remove possible output monomials. If chi^h is in A_N^r H_(N,t), r=ceil(t(q-1)), then w_N(h)+w_N(1,1,1)>r+t. The displayed coordinate bound gives
\[
q w_N(n+(1,1,1))\ge w_N(h)+w_N(1,1,1)>r+t\ge qt.
\]
H_(N,t) is therefore stable under every extended B map and hence EVERY R map. Monomial ideals are adically closed, so this calculation handles formal series as well as polynomial monomials. It is nonzero, indeed contains sufficiently high primary powers.

To prove minimality, let K be any generically nonzero stable ideal. Invert c=UW. The ring becomes regular and A_N becomes unit. Finite Hom localization and the primitive-vector Frobenius argument of n3 give K_c=R_c. Hence d=(UW)^L belongs to K for some integer L. For a target m=(a,b,c_0) satisfying w_N(m+1)>t, choose q=p^e large and r=ceil(t(q-1)). The three capacities
\[
\left\lfloor\frac{q(a+1)-2L-1}{2}\right\rfloor,
\quad\left\lfloor\frac{q(b+1)-2L-1}{2N}\right\rfloor,
\quad\left\lfloor\frac{q(c_0+1)-1}{N}\right\rfloor
\]
are nonnegative and their sum exceeds r for all sufficiently large e: dividing by q gives w_N(m+1)>t. Choose i,j,h within these capacities with i+j+h=r. The monomial d U^i W^(Nj) z^(Nh) lies in A_N^r K; its exponent A has A_i<q(m_i+1). Put alpha=m-A/q, so alpha_i>-1 and alpha in (1/q)M.

Define the R-linear map pi_alpha on root monomials chi^u by pi_alpha(chi^u)=chi^(u+alpha) if u+alpha belongs to M, and0 otherwise. Whenever the lattice condition holds, its coordinates are integers strictly greater than-1, hence nonnegative. It therefore maps into R, not merely its fraction field. Translation by an ordinary monoid exponent preserves the selection condition and proves R-linearity. Its residue-class selection and rescaling make it adically continuous; it extends to completed series. Applied to the chosen source root it returns chi^m. Stability implies chi^m belongs to K. This works for each target and every fixed L, with arbitrarily large Frobenius exponents. Thus H_(N,t) is the smallest stable generically nonzero ideal and proves the formula. The strict threshold and the q-versus-q-1 rounding are checked directly, not inferred from an asymptotic name.

Now let Q be ANY fixed proper primary ideal of R. Choose L>=1 with z^L in Q and choose N>6L+9. Set t=2/3. Since
\[
w_N((2,0,0)+(1,1,1))=3/2+3/(2N)>4/3,
\]
U belongs to tau(A_N^(4/3)). For every0<=j<=L,
\[
w_N((0,0,j)+(1,1,1))=1/2+(j+3/2)/N<2/3.
\]
Hence no z^j, j<=L, belongs to H=tau(A_N^(2/3)). A factorization of U z^L into two monomials in R has t-exponent0 and s-exponents summing to2. Each s-exponent is even, so one factor has s=t exponent0 and is z^j with j<=L. That factor is outside H. Monomial ideal products have ordinary monomial membership, also after completion. Therefore
\[
U z^L\in Q\tau(A_N^{4/3}),\qquad
U z^L\notin\tau(A_N^{2/3})^2.
\]
There is NO single primary Q for which Q tau(a^(2t)) subset tau(a^t)^2 holds for all genuine primary ideals a, even at the fixed rational t=2/3, on this normal nonisolated germ. Taking Q=m^h in particular disproves a uniform primary replacement of the Jacobian over all primary pair models. The example is normal and uses actual primary ideals; a nonnormal conductor or unsupported radial example is not involved.

This is a proof-route obstruction, NOT an envelope counterexample. Indeed this ring has CE over perfect odd characteristic by the actual finite regular cover: the full fibre has the two sign conjugates (or their coincident specialization), as follows from the qualified G331 normal coefficient trace/full-fibre theorem. Max(g,g composed with sign) stays in C_B, is full-fibre constant, and descends positively; finite maximum commutes with actual decreasing nets, so likewise in D. Source competitors below a pulled-back obstacle yield descended majorants, and base competitors pull back. Thus p_B(rho^*f)=rho^*p_R(f). The regular complete B satisfies n4 CE; quotient topology and G331 positive descent give CE on R. This finite-cover conclusion is previously known in the historical sector and is reconstructed here to prevent an erroneous normal-counterexample inference.

The Jacobian (U,V,W) has infinite value on the supported valuation killing P and giving z value1. Its failure to be primary is real, but CE still holds. The obstruction excludes a fixed primary correction independent of the ideal/model. It does NOT exclude corrections depending on an individual obstacle or a fixed model, does not prove failure of Jensen lower hemicontinuity, and does not decide arbitrary normal nonisolated CE. Those distinctions are essential to the unchanged original target.

Evidence: reports/finite-diagnostics.json independently checks L=1,...,32 with N=6L+10 and all1120 admissible factorizations of U z^L; none is a product of two H monomials. It also constructs270 exact Frobenius witnesses for p=3,5,7, N=16,22,40, t=2/3,4/3,5/2, seed powers1,2,5 and the recorded target list whenever eligible. These are exhaustive ONLY on those explicit finite domains. The universal theorem is the preceding algebraic proof. Rerun: python finite_diagnostics.py. Sources, inputs and outputs are local; no supplied code is run.

# n7. Full conductor rules, geometric curves, evidence and unchanged original residual

Use G331 and earlier own n1--n6. The standalone source and proof companion contain the complete reconstructed chain, the entire incoming qualified grants unchanged, exact source/reading ledger, scoped verdict and original residual. Candidate=false: the last note makes no complete solution claim for the literal original P12.3.

Full conductor fibres remain binding. Let S normalize an excellent reduced germ and rho:X_S->X_R be G331's compact quotient, with conductor c. Fibres are singletons at finite conductor value; at infinite value, equality through the conductor quotient is the exact identification. Suppose every normal centre has CE, and let f be finite continuous. Clip it to [-B,0], and clamp source competitors to -B. The primary masks b_N=-(B/N)v(c+a^N) are exactly -B on the conductor-infinite locus and tend to0 at every finite-conductor point. For any source C competitor g, max(g+rho^*b_N,-B) is full-fibre constant and descends POSITIVELY by G331. Sending N to infinity proves rho^*p_R(f)=p_S(rho^*f) on the finite-conductor locus. The reverse inequality everywhere is immediate by pullback of competitors. No nonprimary conductor value divided by N is used as a uniform error.

Write U=p_S(rho^*f), continuous by the stated normal-centre CE assumption. Finite-conductor points are dense on each normal centre, since the conductor contains a regular element and centred divisorial points are dense. The preceding equality and the upper bound imply that the upstairs upper regularization of the pulled-back raw envelope is U. A compact-fibre neighbourhood cover gives the quotient regularization identity p_R(f)^*(x)=max_{rho^-1(x)}U. This is not a positivity theorem for a fibre maximum. The raw envelope is continuous and D-positive exactly when U is constant on EVERY full fibre: if constant, its positive C descent is a competitor and equals the raw supremum; if the raw supremum is continuous, its pullback equals U on a dense set and hence everywhere. If the displayed fibre maximum is continuous, its pullback similarly forces fibre constancy. If positive upper regularization exists, n1 gives the same condition. Outside this compatibility domain no maximal D minorant exists. For arbitrary extended upper semicontinuous obstacles the unconditional formula is instead the supremum over full-fibre-constant source D competitors; the continuous fibre-maximum formula is not extended without proof. No deletion of the infinite-conductor stratum is permitted.

On EVERY excellent reduced curve the normalized link is the finite set of normalization DVR centres, retaining separate branches even on one irreducible component. The conductor has finite value on every branch, so these boundary fibres are singletons. At each DVR, the marked point is an actual effective Cartier divisor and there are no contracted curves to test. Its negative real multiples realize every finite nonpositive branch value. Semilocal gluing and G331 positive descent give all finite nonpositive vectors downstairs. For an extended vector u, max(u,-j) is an actual decreasing sequence of these C vectors with infimum u, including mixed zero and partial bottom. Consequently the greatest geometric envelope is EXACTLY min(phi,0) for every branch obstacle. It equals the known complete ideal envelope by the proved geometric cone comparison, rather than by redefining positivity. If a_q and b_q are the branch orders of two gauges, the coordinate factor is a_q/b_q. The literal disc logarithmic radial class from the dossier remains different and excludes mixed-zero patterns; no classical/CLD identification is inferred.

The new normal positive sector is n5: on every complete normal affine-monoid germ over any field, all continuous monomial-weight obstacles have geometrically positive continuous envelopes among ALL competitors. Rational signed monomial obstacles admit an actual primary profile from a finite rational polyhedron. This includes imperfect-residue and nonisolated examples, but not obstacles separating valuations with equal monomial weights. The new negative result is n6: on the normal three-dimensional A1-times-line germ in perfect odd characteristic, no fixed primary correction works for all actual primary pair ideals at t=2/3. It excludes the universal-primary-replacement route, not a correction depending on a particular model or obstacle, and not CE. This ring itself has CE by its actual finite regular cover.

The exact new finite outputs are also explicit. On k[[s^2,st,t^2,z]], with A=m and B=(U,W^2,z^2), the program finds P vertices (0,0,1),(0,2,0),(1,0,0); q=2 gives J=(U,W^2,z^2,V^2), with V^2 redundant, and the envelope of v(m)-v(B) is -v(J)/2. It enumerates14 fan rays. On the nonsimplicial determinantal cone with generators a,b,c,d and ad=bc, B=(a^2,b^2,c^3,d^3) and A=m, it finds four vertices (4/3,0,0),(4/3,4/3,0),(2,0,2),(2,2,2), giving q=3 and J=(a^4,b^4,c^6,d^6); the envelope is -v(J)/3. It enumerates24 fan rays. Exact half-space/vertex/generator certificates are retained. The diagnostics additionally check32 primary-correction failures, all1120 monomial factorizations in those cases and270 Frobenius witnesses. These are finite observations at specified inputs; the universal proofs are n5/n6.

The corrected formal theorem of n2--n4 is independently judged PASS within its complete-normal/perfect-residue/characteristic-p scope, and the entire isolated formal CE chain is PASS after the mandatory scalar repair. Native276 remains REJECTED AS WRITTEN at its root paragraph. ROOT392's conditional BIG gate was separately proved, not granted. Completion transport is already G331, not new novelty. Full immediate Wang597--602 pixels, CEMSv4 Setting2.1/Definition2.2/Lemmas2.3--2.4, Stacks strict-transform/Fitting statements and proofs, Smolkin's exact Kunz setting, IT/Liu units and BFJ3.15--3.22 immediate envelope proof were read at their precise hypotheses. Recursive Cohen/Artin--Rees/Kunz/duality/normal-formal-fibre/proper-cohomology/polyhedral and BFJ smooth historical foundations are disclosed; they are not all claimed freshly reproved. Historical386's whole argument was read, but deeper historical source bodies are not assigned fresh reading credit merely by appendix identity.

The unchanged ORIGINAL residual remains: arbitrary normal nonisolated dimension>=3 CE beyond the proved obstacle sectors; arbitrary higher-dimensional mixed-characteristic and imperfect-residue CE; general excellent germs outside the exact formal/monoid hypotheses; the characteristic-zero nonprimary-correction infinity stratum; general canonical Jensen weak lower hemicontinuity; and a genuine normal continuous signed primary/model obstacle whose raw envelope or regularization fails geometric positivity. No such normal counterexample was obtained. The nonnormal double-plane obstruction and increasing energy spikes do not settle this residual. General normalization/conductor envelopes remain within the full-fibre criterion, not an unrestricted clipping rule. Original 'when possible/appropriate regularity' is preserved. P12.4 products, P12.5 energy and full P12.6 operators remain separate.

Evidence and rerun: python audit_packet.py; python audit_serialization.py; python finite_diagnostics.py; python toric_envelope.py; python build_delivery.py; python check_delivery.py. The deliverables are P12.3-audit-and-toric-envelopes.tex, proof-companion.md, source-application-ledger.md, whole-reading-ledger.md, coverage.md, independent-scoped-verdict.md, original-residual.md and native-notes.json, plus separate actual/expanded input records and own scripts/reports. The exact original task object/problem bytes are retained separately. All full primary bodies/pixels and book chapters are LOCALONLY. No supplied program was imported/executed, and no agent, additional native/model campaign, compiler, publication, network, authentication/runtime/proxy/CA or protected-editor change occurred. No supervised heavy-compute service was supplied or needed. Compilation and retention identity are not mathematical certification; the source is deliberately uncompiled for ROOT.


# Entire incoming qualified G331, unchanged

QUALIFIED CALLER GRANT G331: accepted complete P12.2 construction/comparison, with every mandatory source/scope qualification. No P12.3 envelope theorem is supplied.

BEGIN ENTIRE P12.2-paper.tex
\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\emergencystretch=4em
\title{A geometric valuative psh cone on excellent local germs\\
Actual Cartier positivity, uniform comparison, and full conductor descent}
\author{Fresh local reconstruction of ORIGINAL P12.2}
\date{8 October 2026}
\begin{document}
\maketitle
\begin{abstract}
On the intrinsic centred semivaluation boundary of an excellent local germ,
we define a geometric core by actual negative effective real Cartier divisors
on actual primary blowups, with nonnegative degrees on all contracted integral
curves. We prove its continuous uniform closure and actual decreasing completion
equal the corresponding ideal classes. A fixed primary correction to finite
global sections, corrected Keeler generation on the full closed fibre, and
explicit real ample perturbation prove the comparison without a normality,
smoothness or characteristic restriction. We reconstruct full finite-injection
and normalization/conductor descent, including mixed-zero and bottom patterns,
and recover the full smooth BFJ class on all semivaluations at its exact published
hypotheses. A nonisolated cusp separates the entire finite-real raw cone from its
completion. This is an unverified complete-solution candidate for P12.2;
independent whole-original review remains required.
\end{abstract}
\tableofcontents
\newpage
\section*{Main theorem and proof map}
Let $(R,\mathfrak m)$ be excellent local and replace it by its reduction.
For every proper primary $\mathfrak a$, let $V_{\mathfrak a}$ be the compact
section of centred real semivaluations with $v(\mathfrak a)=1$, retaining every
prime support. Define $Q$ by finite nonnegative real sums of negative
unit-or-primary ideal values, $C$ by uniform closure, and $D$ by actual infima
of nonempty decreasing $C$-nets, with bottom allowed.

On actual primary blowups, take actual negative effective finite real Cartier
presentations having nonnegative degree on every contracted proper integral
curve. Their evaluations define $M_{\rm geom}$ independently of ideal
positivity. Then
\[
 Q\subset M_{\rm geom}\subset C,\qquad
 C_{\rm geom}=C,\qquad D_{\rm geom}=D.
\]
For every reduced finite injection, the pullback image of either completed
class is precisely its full-fibre-constant subclass. Normalization fibres are
singletons at finite conductor value and precisely conductor-quotient fibres
at infinite value. Primary changes obey the exact homogeneous cocycle.
At a smooth affine closed germ over an algebraically closed characteristic-zero
field, $C$ is exactly the finite continuous BFJ subclass and $D$ is the full
BFJ all-semivaluation extension with the identically bottom function adjoined.
Smooth DVR and empty dimension zero are direct.

The proofs are the numbered local chain below: n1 gives the boundary; n2--n6
give full algebraic descent; n7 discharges the exact published geometric inputs;
n8 constructs and compares the independent cone; n9 gives full BFJ recovery;
n10--n11 preserve raw-cone and radial distinctions; n12 records the exact
original-target decision. Each support list contains only earlier local IDs.
Source applications are ordinary published applications, with disclosed
recursive historical dependencies, and no supplied draft is an accepted premise.
Separate envelopes, products, energy and their geometric operator theory are
the P12.3--P12.6 targets. They are not claimed here.
\section{n1. Boundary, finite lifting, conductor fibres, and completion}
\textit{Earlier local supports: none.}

All rings below are commutative. For a Noetherian local ring \((R,\mathfrak m)\), a centred real semivaluation is a map to \([0,+\infty]\) satisfying \(v(0)=+\infty\), \(v(1)=0\), multiplicativity, the ultrametric inequality, and \(0<v(\mathfrak m)<+\infty\). Its support \(v^{-1}(+\infty)\) is a prime strictly below \(\mathfrak m\); no minimal-support restriction is imposed. Ideal values are minima over finite generating sets. Relations between generating sets prove independence and
\[
v(IJ)=v(I)+v(J),\qquad v(I+J)=\min\{v(I),v(J)\}.
\]
Units have value zero. A proper primary ideal always means primary for the marked maximal ideal.

Fix a proper primary ideal \(\mathfrak a\). The section \(V_{\mathfrak a}(R)=\{v:v(\mathfrak a)=1\}\) is compact Hausdorff. Indeed semivaluation axioms and \(v(\mathfrak m)=1\) are closed conditions in the compact product \([0,+\infty]^R\); addition, minimum and the order relation have the required continuity/closedness. Choose \(\mathfrak m^r\subset\mathfrak a\subset\mathfrak m^s\), with \(r\ge s\ge1\). Then \(s v(\mathfrak m)\le v(\mathfrak a)\le r v(\mathfrak m)\). Rescaling identifies the two sections. Every primary ideal value is finite positive continuous and bounded there. For another primary ideal \(\mathfrak b\),
\[
H_{\mathfrak a,\mathfrak b}(v)=v/v(\mathfrak b),\qquad
u_{\mathfrak b}(H_{\mathfrak a,\mathfrak b}v)=u_{\mathfrak a}(v)/v(\mathfrak b).
\]
The denominator and its inverse are bounded. Substitution proves the inverse and the exact three-gauge cocycle. The centred cone is the product of its section and the positive radial coordinate \(v(\mathfrak a)\); hence these sections represent its intrinsic ray quotient. Nonprimary proper ideals give only their open finite-value domain, which can be noncompact. Units and zero ideals have no level-one section.

Nilpotents have infinite value. Comparing \(f+n\) and \((f+n)-n\) proves that reduction preserves every semivaluation and ideal gauge. A zero-dimensional reduced local ring is a field and has empty centred boundary. For a positive-dimensional excellent reduced local ring, a penultimate prime of a saturated chain to the maximal ideal gives a one-dimensional excellent domain quotient. Its finite normalization has a local DVR factor, whose order pulls back and normalizes into the section. This proves nonemptiness. Ordinary background used throughout is lying over, prime avoidance, finite Artinian decompositions, and the quotient/finite-type-localization stability, Nagata finiteness and universal catenarity consequences of excellence. None is used to assert resolution in arbitrary characteristic.

Every finite integral injection \(R\hookrightarrow B\), with \(B\) reduced and nonzero, gives a continuous surjective restriction \(V_{\mathfrak aB}(B)\to V_{\mathfrak a}(R)\). Here a finite algebra has the finite union of its closed-centre sections above \(\mathfrak m\). To lift \(v\) with support \(\mathfrak p\), choose a prime \(P\) of \(B\) above \(\mathfrak p\) and form the finite field extension \(\operatorname{Frac}(B/P)/\operatorname{Frac}(R/\mathfrak p)\). Extend the valuation ring by taking the integral closure, a prime over its maximal ideal, and a dominating valuation ring. The domination assertion follows from Zorn: in a maximal dominating local subring, either adjoining \(x\) or \(x^{-1}\) leaves the maximal ideal proper. If \(1=\sum a_i x^{-i}\) with all \(a_i\) in that ideal, multiplying by a power and dividing by \(1-a_0\) makes \(x\) integral, so lying over makes the ideal proper after adjoining \(x\). Localizing contradicts maximality unless one of the two elements already belongs. Intersection with the old field is the original valuation ring: an element outside it has inverse in its maximal ideal. An algebraic equation for any new nonzero field element has two least-valued terms; thus an integer multiple of its value is in the old value group. Dividing this old real value by the integer gives a well-defined order-preserving real embedding, using common multiples. Integral elements have nonnegative value by the least-term test for a monic equation. Compose with \(B\to B/P\), assigning \(P\) infinite value. This construction first kills the support; it never extends a nonzero-support semivaluation to the original fraction field. Compactness makes restriction a quotient map.

Let \(S\) be the finite normalization of an excellent reduced \(R\), and \(\mathfrak c=(R:S)\). Clearing denominators of finitely many generators of \(S\) gives a regular conductor element. The conductor is an ideal of both rings and
\[
R=S\times_{S/\mathfrak c}(R/\mathfrak c).
\]
An element of \(S\) whose residue comes from \(R\) differs from an element of \(R\) by an element of \(\mathfrak c\), proving this identity. The normalization boundary is the finite disjoint union of local normal centres above \(\mathfrak m\). Idempotents choose a minimal component; localization at its centre changes no values of denominators. Chinese remainder elements separating the finitely many centres, and their complements, have open positive-value loci selecting these pieces. The pieces are therefore clopen. Branches mean these local centres, not merely minimal primes.

If \(v(\mathfrak c)<+\infty\), choose \(c\in\mathfrak c\) of finite value. Every lift satisfies \(w(s)=v(cs)-v(c)\), so it is unique. The subtracted number is finite. If \(v(\mathfrak c)=+\infty\), all lifts kill the conductor, and equality after restriction \(S/\mathfrak c\to R/\mathfrak c\) is exactly their identification. This infinity stratum is closed; its finite complement is open, without a closedness claim. A fibre-constant continuous function descends continuously by the compact quotient. A fibre-constant extended nonpositive upper semicontinuous function descends upper semicontinuously: its closed superlevel sets have compact, hence closed, images. These assertions alone supply no positivity descent.

Completion preserves the entire boundary for every Noetherian local ring. For \(F\in\widehat R\), choose representatives \(F_N\) modulo \(\mathfrak m^N\), and put \(d=v(\mathfrak m)>0\). Differences have value at least \(Nd\). If some \(v(F_N)<Nd\), later values stabilize; otherwise they tend to infinity. Define \(\widehat v(F)\) by this limit. It is independent of representatives and satisfies
\[
\min\{\widehat v(F),Nd\}=\min\{v(F_N),Nd\}.
\]
Applying this to sums and products proves all axioms and uniqueness, including infinite values; completed units have unit representatives. Compose with \(q(t)=t/(1+t)\), \(q(+\infty)=1\). The displayed continuous truncations have uniform error at most \((1+N/r)^{-1}\), because \(d\ge1/r\). Thus completed evaluation is continuous and completion restriction is a homeomorphism. Every completed primary \(J\) contains \(\widehat{\mathfrak m}^N\). Representatives modulo that power of its generators belong to \(J\cap R\) and, with the boundary power, generate \(J\). Hence \(J=(J\cap R)\widehat R\). The quotient isomorphism also proves contraction of an extended primary ideal recovers it. Unit-or-primary profiles and their uniform and decreasing classes therefore agree under completion. No equivalence of geometric model categories is asserted.

This is a mathematical argument with the stated ordinary background. Swanson--Huneke 6.4.1--2 were read in full and agree with the domination proof. Artifact n1.md is authoritative and is reproduced in argument.md and the paper. Rerun: python audit\_inputs.py; python build\_delivery.py. Execution does not verify the mathematics.

\section{n2. Exact algebraic applications and their qualifications}
\textit{Earlier local supports: n1.}

Use n1 for boundary conventions. The following are ordinary published theorem applications at their stated hypotheses, with their immediate units checked from the bound primary data. This is not an independent reconstruction of all historical proofs.

Swanson--Huneke is the current author PDF created July 2024, not asserted byte-identical to the 2006 printing. Its complete 6.8.1--4 statements and proofs give the following consequence. Let \(E\) be Noetherian semilocal, \(J\) contain a boundary power, and \(Q\) be a finite ideal. If every normalized centred semivaluation satisfies \(w(Q)\ge w(J)\), and \(Q\) has zero image on every zero-dimensional minimal component where \(J\) is nonunit, then
\[
Q\subset\overline J.
\]
Apply 6.8.4 on each positive-dimensional local domain component, normalizing each centred rank-one DVR by the boundary ideal. Apply 6.8.3 to all minimal components. On zero-dimensional components there are no boundary points; the extra zero-image condition is needed. In all uses below \(Q=K(\mathfrak aE)^L\), with \(L>0\), so this condition holds. Unit components of \(J\) impose no condition. For nonreduced \(E\), lift the componentwise monic equations, multiply them over the finitely many minimal primes, then raise to a power to kill the nilpotent error. The resulting equation is monic with degree-i coefficients in \(J^i\). This is the finite-minimal-prime argument of 1.1.5, also read completely. PDF inspection of printed page 140 confirmed the integral-closure bars omitted in the text extraction.

The common exponent needed later has a short direct proof. Each \(qt\), \(q\in Q\), is integral over \(E[Jt]\) with its homogeneous ideal-integrality equation. Thus \(E[(J+Q)t]\) is finite graded over \(E[Jt]\). Choose homogeneous module generators of degrees at most \(h\). Its degree \(N+h\) terms have coefficients in \(J^{N+h-d}\subset J^N\). Consequently
\[
Q^{N+h}\subset (J+Q)^{N+h}\subset J^N\quad(N\ge1).
\]
This works for nonreduced rings and assumes no finiteness of the full normalized Rees algebra. The complete 1.2.3--5 reduction chain was checked too; printed page 6 confirms the criterion uses integral closure.

For an excellent local domain \(A\) of positive dimension and a nonzero proper primary ideal, 10.2.2, including its proof ending at 10.2.3, constructs finitely many Rees DVRs centred at the closed point. The full 10.4.3 proof gives their residue transcendence degree \(\dim A-1\) when \(A\) is formally equidimensional. Excellence supplies universal catenarity, and the full B.5.1 statement/proof identifies this with local formal equidimensionality for Noetherian domains. B.3.2 and its immediate context give, for a finite-type birational domain \(B\) over excellent local domain \(A\), and \(P\cap A=\mathfrak m\),
\[
\dim B_P+\operatorname{trdeg}_{A/\mathfrak m}\kappa(P)=\dim A.
\]
The book describes B.3.2's proof as a modification of an earlier dimension argument. Its recursive historical dependencies, including Mori--Nagata and Ratliff, are disclosed rather than claimed independently read.

Stacks 0C23, full immediate HTML lemma/proof, states that normal Noetherian local rings with normal formal fibres have normal completion; excellence suffices. Its proof refers to Algebra 10.163.8, not recursively read. A normal local completed ring is a domain. Thus an excellent normal local domain is analytically irreducible and analytically unramified. This is not claimed for an arbitrary nonnormal domain.

Exact Rond--Spivakovsky arXiv 1404.4885v1, complete pages 1--2 definitions and statements 1.3, 1.4 and 1.7, yields an order bound at precisely this analytic domain. For a centred divisorial valuation \(\nu\) and the finitely many maximal-ideal Rees valuations \(\nu_j\), 1.3 gives \(\nu(f)\le c_j\nu_j(f)\). Set \(C_0=\max_j c_j\nu_j(\mathfrak m)\). Statements 1.4 and 1.7 imply
\[
\nu(f)\le C_0\min_j\frac{\nu_j(f)}{\nu_j(\mathfrak m)}
=C_0\overline{\operatorname{ord}}_{\mathfrak m}(f)
\le C_0(\operatorname{ord}_{\mathfrak m}(f)+K).
\]
For nonzero nonunits the order is at least one and finite by Krull intersection, giving \(\nu(f)\le C_0(1+K)\operatorname{ord}_{\mathfrak m}(f)\). Units have both values zero and are handled separately. The literal strict Remark 1.6 fails on units and is not used. Swanson's full Rees-valuations Section 5 was read; its 5.2 is stated for complete domains. The general-domain application here uses exact Rond--Spivakovsky 1.3. Original Rees 1989 and the historical Izumi proofs have not been independently read. Published applications with these disclosed dependencies are allowed by the task; metadata and old reading receipts are not grants.

Artifacts: n2.md, source-application-ledger.md, reports/source-images/book-140.png and book-6.png, reports/input-hashes.json. Rerun: python inspect\_primary.py; python audit\_inputs.py; python build\_delivery.py. No finite check certifies these published applications or the new consequences.

\section{n3. Exact cones, density, and normal-target traces}
\textit{Earlier local supports: n1.}

Use n1's sections. Define \(P_R\) to be the raw finite nonnegative REAL combinations of gauges \(v(I)\), where \(I\) contains a power of the primary boundary ideal, with the unit ideal allowed. Put \(Q_R=-P_R\), let \(C_R\) be its uniform closure in finite continuous functions, and let \(D_R\) consist of infima of nonempty decreasing \(C_R\)-nets. Include zero and the identically minus-infinity bottom. A finite semilocal algebra uses the product classes over its closed centres. These agree with global semilocal ideal profiles: local primary ideals contract to ideals primary at their own centre and unit at the others, and tuples glue in a common Artinian boundary quotient. Denominators synchronize by powers. Rational profiles \(-v(I)/k\) are uniformly dense in \(C_R\): approximate finitely many real coefficients rationally and turn their sum into a product-ideal profile. The class \(C_R\) is a closed convex cone, stable under maxima by ideal sums. Its decreasing completion is upper semicontinuous and stable under addition, positive scaling and finite maxima by product directed sets. We do not assume increasing-limit closure, arbitrary-infimum closure, or flattening of nested nets.

The rational difference span of bounded gauges is a lattice: after a common denominator every expression is \((v(I)-v(J))/k\), and
\[
\min\{v(I)-v(J),v(K)-v(H)\}=v(IH+KJ)-v(JH).
\]
It contains rational constants since \(v(\mathfrak a)=1\), and separates points using \(v((f)+\mathfrak a^N)=\min\{v(f),N\}\), and centre-separating ideals in the semilocal case. Its UNIFORM closure is a real vector lattice. The compact lattice approximation proof makes this closure all real continuous functions: affine combinations of a separating function match a target at two points; rational approximations preserve strict local error tests. For a fixed first point take finitely many minima to bound the target from above throughout the space, while matching near that point; then finitely many maxima over first-point neighbourhoods give a uniform approximation. Negating interchanges the needed bounds. No integer ideal formula is asserted for an arbitrary finite irrational span.

Let \(A\) be excellent normal local domain and \(A\subset B\) a finite domain extension, with fraction fields \(K\subset L\), \(n=[L:K]\). For a \(B\)-ideal \(J\), choose finite \(A\)-module generators \(b_i\) and define \(\mathcal N(J)\) as the coefficient ideal of
\[
N_{L(T)/K(T)}\Big(\sum_i T_i b_i\Big)
=\prod_{\sigma:L\hookrightarrow M}\Big(\sum_i T_i\sigma(b_i)\Big)^q,
\qquad q\,|\Sigma|=n.
\]
Here \(M/K\) is a finite field containing all embedding images. The generic inseparable length \(q\) follows by decomposing \(L\otimes_K\overline K\) into its Artinian factors: determinant of multiplication on a length-q factor is its residue scalar to the power q. The coefficients are integral over \(A\) and belong to \(K\), hence belong to \(A\). Linear substitution in both directions when changing generators proves independence of this coefficient ideal. If \(J\supset\mathfrak a^N B\), add base generators \(x\) of \(\mathfrak a^N\) redundantly: the pure variable coefficient is \(x^n\). The coefficient ideal therefore contains a boundary power and is unit-or-primary.

Let \(E\) be the finite integral closure of \(A\) in \(M\). Lift any base semivaluation to \(E\) by n1, including nonzero support, and compose with the embeddings to obtain \(w_\sigma\) on \(B\). Minimum coefficient values of polynomials multiply. To prove this, quotient by the support, enter the valued quotient fraction field, divide each nonzero polynomial by a coefficient of smallest finite value, and reduce to nonzero residue polynomials. Their product is nonzero. A polynomial vanishing modulo support has infinite coefficient minimum and causes no difficulty. Applying this to the displayed norm polynomial gives on EVERY support
\[
v(\mathcal N(J))=q\sum_{\sigma\in\Sigma}w_\sigma(J).
\]
Boundary-power ideals make these sums finite. Define \(\mu_v=q\sum_\sigma\delta_{w_\sigma}\), of mass \(n\). Its integrals on all ideal gauges are fixed by the coefficient identity; the density just proved and equal mass make it independent of the lift on every continuous function, hence as a finite measure. Its support is the full restriction fibre. Indeed for any fibre point on \(B\), extend it to \(E\) by n1 with the identity embedding of \(B\). That point occurs with positive weight. Choice independence forces it into the support of every such measure. Thus the whole fibre is finite of cardinality at most \(n\). This proof uses generic inseparable lengths and quotient-support Gauss values; it does not assume a defectless ramification/residue-degree formula.

The trace \(TH(v)=\int H\,d\mu_v\) is positive, of norm \(n\), and continuous-valued. Continuity holds first on gauges by the coefficient identity, then on all continuous functions by uniform density and the mass bound. It preserves \(C\), mapping a rational negative profile to \(-v(\mathcal N(J))/k\). A finite positive sum commutes with decreasing nonpositive extended limits: if one summand goes to bottom so does the sum; otherwise directedness approximates all finite limits simultaneously. Consequently a fibre-constant \(D_B\)-function descends via \(T/n\) to an actual decreasing \(C_A\)-net, as does a fibre-constant \(C_B\)-function.

For any reduced finite injection into normal local \(A\), choose the minimal source components dominating \(A\), at least one of which exists over the generic point, and normalize them. Sum their traces divided by the sum of their generic degrees. At every base semivaluation all traced values equal the descended value by constancy on the FULL original fibre. Vertical components receive no fabricated generic degree, but remain constrained by that full constancy. This proves exact \(C,D\) descent for normal targets. Pullback of ideals and limits supplies the converse. Every lift has the same base primary-gauge denominator, so these assertions obey n1's gauge cocycle.

Artifacts: n3.md and the paper. Rerun: python build\_delivery.py. This coefficient trace is proved here rather than imported from a supplied label. It is not a construction of envelopes, products, energy, or a degree trace on arbitrary nonnormal targets.

\section{n4. Bounded descent for every reduced excellent finite injection}
\textit{Earlier local supports: n1, n2, n3.}

Using n1--n3, we prove
\[
f^*C_R=\{u\in C_B:u\text{ is constant on every restriction fibre}\}
\]
for every excellent reduced local \(R\) and nonzero reduced finite injection \(R\hookrightarrow B\). Pullback is an isometry. The theorem concerns the continuous UNIFORM cone, not the raw cone or a decreasing completion.

Induct on target dimension. Dimension zero has empty sections. Normal targets are n3. In dimension d, first prove normalization descent, using the arbitrary finite-injection theorem below dimension d; then prove arbitrary injections by normalization base change. Let \(S\) normalize \(R\), \(\mathfrak c\) be its conductor, \(C_0=R/\mathfrak c\), and \(E=S/\mathfrak c\). A regular conductor element gives \(\dim C_0<d\). The injection \(C_0\hookrightarrow E\) stays injective after reduction because nilpotence is detected in an injected subring. Restriction of primary gauges and uniform limits to the quotient section preserves the class. Thus for fibre-constant \(u\in C_S\), its continuous descent \(h\) from n1 has quotient restriction \(h_0\in C_{C_0}\) by induction. If the quotient section is empty, the conductor value is finite at every point and quotient estimates below are unnecessary.

Fix \(\varepsilon>0\). Choose rational profiles \(j=-w(J)/k\) and \(\kappa=-v(K)/k\) approximating \(u\) and \(h_0\) with error less than \(\varepsilon\). All ideals contain boundary powers. We can make \(J\) proper at every positive-dimensional centre: add an arbitrarily small negative boundary constant before rational approximation, or multiply a rational profile ideal by the boundary ideal with an arbitrarily large common denominator. Start with smaller errors to accommodate this correction. Synchronize denominators by ideal powers and enlarge k until \(1/k<\varepsilon\). On the entire quotient boundary,
\[
|w(K_E)-w(J_E)|<2k\varepsilon.
\]
Choose integer \(L\) with \(2k\varepsilon<L\le2k\varepsilon+1\). The ideal \(Q=K_E(\mathfrak aE)^L\) has \(w(Q)\ge w(J_E)\) everywhere. Its POSITIVE boundary factor kills its image on zero-dimensional minimal components. The exact n2 criterion therefore gives \(Q\subset\overline{J_E}\), on all minimal components and even a nonreduced quotient. The finite graded argument gives one \(h'\ge0\) with \(Q^{N+h'}\subset J_E^N\) for every N.

Put \(I_N=J^N\cap R\). It contains a boundary power and is proper, hence primary. The conductor fibre product in n1 gives the exact residue identity
\[
(I_N+\mathfrak c)/\mathfrak c=J_E^N\cap C_0.
\]
For the nontrivial inclusion, lift a residue in the right side to an element of \(J^N\). Since its residue comes from \(C_0\), that very element lies in \(R\), and hence in \(I_N\). Thus the image contains \(K^{N+h'}(\mathfrak aC_0)^{L(N+h')}\). At a conductor-infinite point its quotient semivaluation yields
\[
\frac{v(I_N)}{kN}\le(1+h'/N)\left(\frac{v(K)}k+\frac Lk\right).
\]
All terms here are finite. At a conductor-finite point the unique lift \(w\) and \(\mathfrak cJ^N\subset I_N\) yield instead
\[
\frac{w(J)}k\le\frac{v(I_N)}{kN}\le\frac{w(J)}k+\frac{v(\mathfrak c)}{kN}.
\]
The latter estimate is used ONLY at finite conductor value. On every point the lower bound from \(I_N\subset J^N\) gives \(v(I_N)/(kN)\ge-h-\varepsilon\). The limit upper bound is at most \(-h+4\varepsilon\): at infinity use \(-\kappa\le-h+\varepsilon\) and \(L/k<3\varepsilon\), and at finite conductor use \(-j\le-h+\varepsilon\).

The continuous functions \(b_n=v(I_{2^n})/(k2^n)\) decrease, since \(I_N^2\subset I_{2N}\). Their increasing strict-test open sets \(\{b_n+h<5\varepsilon\}\) cover the compact section. One n covers it entirely. Together with the common lower bound this proves \(\|-b_n-h\|_\infty<5\varepsilon\), and then \(h\in C_R\). These negative dyadic profiles INCREASE internally. They are not used as a decreasing regularization, and no increasing-limit closure is invoked.

For arbitrary \(R\hookrightarrow B\), form \(B'=(B\otimes_R S)_{\rm red}\). Base change of an integral surjective spectrum map is surjective, so its kernel in reduced \(S\) lies in every prime and is zero. Hence \(S\hookrightarrow B'\) is a finite injection. Pullback of \(u\) is fibre constant over each normal local centre of \(S\); equal restrictions there imply equal underlying restrictions to \(R\). N3 descends it to \(C_S\), exactly the pullback of \(h\). Normalization descent just proved gives \(h\in C_R\), closing induction. Ideal extension gives pullback inclusion and surjectivity in n1 gives the isometry.

Define \(N_R\) as the continuous functions whose normalization pullbacks belong to the RAW local negative real ideal cones and are fibre compatible. We have only
\[
Q_R\subset N_R\subset C_R,\qquad
\overline{Q_R}^{\|\cdot\|_\infty}=\overline{N_R}^{\|\cdot\|_\infty}=C_R.
\]
No raw equality is inferred. All conductor-infinite quotient supports remain. Artifacts: n4.md and the paper. Rerun: python build\_delivery.py. The incompatible-ideal contraction shortcut is deliberately absent; n11 diagnoses it.

\section{n5. Unbounded strictly negative descent by insertion}
\textit{Earlier local supports: n1, n2, n3, n4.}

Use n1--n4. A fibre-constant \(u\in D_B\) descends into \(D_R\) whenever its descent \(h\) is everywhere strictly negative, including partial minus-infinity and discontinuous unbounded functions. The descent is upper semicontinuous by n1, so on a nonempty compact section \(h\le-c\) for some finite \(c>0\). All-bottom is directly the limit of \(-N v(\mathfrak a)\); zero is separate. Normal targets follow from n3. Induct on dimension exactly as in n4: prove normalization from lower-dimensional finite-injection descent and then arbitrary injections by reduced normalization base change.

In the normalization step use \(S,\mathfrak c,C_0,E\) from n4. A decreasing representation of \(u\) restricts to the quotient, whose fibre-constant limit descends by induction to \(h_0\in D_{C_0}\). We prove an insertion lemma: for every finite continuous test \(F>h\) there is \(q\in C_R\) with \(h<q<F\). Choose a FINITE positive lower bound \(e\) for the lower semicontinuous gap \(F-h\), for example any number below half the minimum of 1 and its infimum. When that infimum is infinite, e remains finite; no infinity subtraction is performed.

From a decreasing continuous representation of \(u\), choose one term \(g\) satisfying \(u\le g<-c/2\) and \(g<F\circ\rho-e/2\). Each point eventually satisfies these strict continuous tests; their open sets and directedness give one common index by compactness. No uniform convergence to \(u\) is used. Choose \(0<b<1/2\) with \(b\|g\|<e/8\). The scaled term \((1-b)g\) is still below \(F-e/4\), and exceeds finite \(u\) by at least \(bc/2\). Uniform rational approximation with error less than \(\min(e/8,bc/4)\), further tightened to retain strict negativity, gives \(j=-w(J)/k\) and a fixed \(s>0\) such that
\[
u+s\le j<F\circ\rho-e/8.
\]
The first inequality is automatic at bottom. \(J\) is proper at all centres and contains a boundary power. Put \(M=\|j\|\).

We need a rational quotient profile \(\kappa=-v(K)/k\) with \(h_0\le\kappa\) and \(\kappa\circ\rho_E<j|_E+\delta\), for arbitrarily small \(\delta>0\). Here is the needed construction. Choose \(0<b_1<1/2\) with \(b_1M<s/4\), and a decreasing \(C_{C_0}\)-net \(g_i\) to \(h_0\). Since \(u_E\le j_E-s\), we have \((1-b_1)u_E<j_E-s/4\). Compactness on E selects one i with its scaled pullback below \(j_E-s/8\); simultaneously compactness on \(C_0\) selects \(g_i<-c/2\). Scaling therefore lifts it above \(h_0\) by a positive uniform gap at finite points. Rational approximation with error less than \(\min(b_1c/4,s/16)\) gives \(\kappa\) with the stated two bounds, even with a negative gap to \(j_E\). Synchronize denominators with J and enlarge k so \(1/k<\delta\). If the quotient boundary is empty omit this construction.

Choose integer \(L\) with \(k\delta<L\le k\delta+1\). On E the ideal \(Q=K_E(\mathfrak aE)^L\) dominates \(J_E\) in value. N2, including the zero-dimensional boundary factor, gives \(Q\subset\overline{J_E}\) and a common \(h'\) with \(Q^{N+h'}\subset J_E^N\). Contract \(I_N=J^N\cap R\). The exact residue identity of n4 gives at infinity-conductor points
\[
\liminf_N[-v(I_N)/(kN)]\ge\kappa-2\delta\ge h-2\delta.
\]
At finite-conductor points its finite-value estimate gives limit j, at least \(h+s\). The dyadic \(f_n=-v(I_{2^n})/(k2^n)\) increase, are finite continuous, and satisfy \(f_n\le j\) on every lift. Their strict open sets \(\{f_n>h-3\delta\}\) cover the compact section, including bottom points: these sets are open because h is upper semicontinuous. Select one n valid everywhere.

Choose \(\delta\) so small that \(\eta=3\delta/c<1/2\) and \(\eta M<e/16\), and put \(q=(1-\eta)f_n\in C_R\). At finite \(h\le-c\),
\[
q>(1-\eta)(h-3\delta)\ge h+\eta c-3\delta(1-\eta)=h+3\delta\eta>h.
\]
At bottom q is finite. Also \(q\le(1-\eta)j\le j+\eta M<F\). This proves insertion using real positive scaling, not adding a positive constant to the class.

Let \(\mathcal Q\) be all continuous \(C_R\)-functions strictly above h. Zero belongs. For two members apply insertion to their continuous minimum; the test need not itself be psh. This gives a member below both, so \(\mathcal Q\) is downward directed. At any v and finite \(t>h(v)\), upper semicontinuity and compact Hausdorff normality give a finite continuous F strictly above h with \(F(v)<t\): choose \(h(v)<\ell<t\), a neighbourhood where \(h<\ell\), and a Urysohn cutoff supported there, interpolating from \(\ell\) to a global strict upper bound outside. Insertion supplies \(q(v)<t\). Thus \(\inf\mathcal Q=h\), and reverse pointwise order is an ACTUAL decreasing \(C_R\)-net to h. This closes normalization and the finite-injection induction. Neither an increasing completion step nor a flattening theorem is needed.

Artifacts: n5.md and the paper. Rerun: python build\_delivery.py. This proof reconstructs strict-negative descent without accepting any supplied provenance label. Mixed-zero descent is next.

\section{n6. Divisorial density, normal zero dichotomy, and full completed descent}
\textit{Earlier local supports: n1, n2, n3, n4, n5.}

Use n1--n5. We prove the full statement
\[
f^*D_R=\{u\in D_B:u\text{ is constant on every restriction fibre}\}
\]
for every nonzero reduced finite injection over an excellent reduced local ring. It includes allzero, allbottom, mixedzero, partialbottom, conductor-infinite, and nonminimal supports.

First prove divisorial density on an excellent local domain \(A\). A basic neighbourhood of v in its primary section imposes finitely many strict coordinate tests. Choose a generator \(a_0\) of \(\mathfrak a\) with \(v(a_0)=1\) and put all \(a_j/a_0\) in a finite-type birational subalgebra \(B_0\subset\operatorname{Frac}(A)\). For each finite positive tested coordinate f choose rational bounds \(p/q<v(f)<r/s\) within its required interval, and put \(f^q/a_0^p\) and \(a_0^r/f^s\) in \(B_0\). For an infinity coordinate use only a lower bound and its first ratio. Units and zero have fixed values. Every denominator has finite value, so even a nonzero-support v extends nonnegatively to this algebra. Its positive-value prime P contains \(a_0\) and every strict-test ratio and contracts to \(\mathfrak m\). Thus \((B_0)_P\) is excellent domain of positive dimension. A Rees DVR of its maximal ideal, furnished by n2, is positive on P and nonnegative on \(B_0\). Its valuation \(\nu\) has \(\nu(\mathfrak a)=\nu(a_0)>0\); dividing by this number satisfies all the original tests.

This DVR is divisorial over A itself. N2's birational dimension formula gives \(\dim(B_0)_P+\operatorname{trdeg}_{A/\mathfrak m}\kappa(P)=\dim A\). The Rees DVR has residue transcendence degree \(\dim(B_0)_P-1\) over \(\kappa(P)\). Transcendence degrees add to \(\dim A-1\). Its value group is discrete rank one and centre on A is the closed point. Thus it has precisely the divisorial definition in Rond--Spivakovsky. This establishes density on the actual all-support pointwise section without any singular SNC or characteristic-zero resolution argument.

Now assume A is normal. N2 gives, for each centred divisorial \(\nu\), a finite constant with \(\nu(f)\le C_\nu\operatorname{ord}_{\mathfrak m}(f)\) for nonzero nonunits; units are separately zero. Normalize \(\nu\) by \(\mathfrak a\). If \(\mathfrak m^r\subset\mathfrak a\), then every \(v_0\) in the section has \(v_0(\mathfrak m)\ge1/r\). Choosing a nonzero generator attaining a proper primary ideal's finite \(v_0\)-value yields \(\nu(I)\le C_\nu r v_0(I)\). For unit ideals it holds too. Therefore every finite real negative ideal combination, and its uniform limit \(g\in C_A\), satisfies
\[
g(\nu)\ge C_\nu r\,g(v_0).
\]
If \(g(v_0)=0\), nonpositivity forces g to vanish at all divisorial points; density and continuity force \(g=0\). If \(u=\inf_i g_i\in D_A\) has value zero anywhere, every nonpositive \(g_i\) is zero there and hence everywhere. Thus on a normal local branch every completed function is either identically zero or everywhere strictly negative, with bottom allowed. Compact upper semicontinuity bounds each negative branch above by a finite negative constant.

Let \(u\in D_S\) be normalization-fibre constant. Call its finitely many normal centres active if their functions are everywhere negative, including bottom centres. Active and inactive points cannot share a fibre. The tuple \(\sigma=-1\) on active centres, zero elsewhere, belongs to \(C_S\) by primary-gauge/unit gluing from n3 and is fibre constant. The independently proved bounded theorem n4 descends it WITH POSITIVITY to \(\sigma\in C_R\). Its active set \(T=\{\sigma=-1\}\) is clopen. The descent h of u equals zero off T and is at most \(-c\) on T for some finite \(c>0\). If T is empty the result is zero. If every active value is bottom, the decreasing sequence \(N\sigma\) already proves the result.

For the remaining cases, every \(u-\delta\), \(\delta>0\), is an everywhere negative fibre-constant \(D_S\)-function by n3's addition rule, so n5 gives \(h-\delta\in D_R\). We do NOT take their increasing limit. Instead take any finite continuous test \(F>h\) on compact T and a finite positive lower gap e. Choose \(0<\eta<1/2\) with \(\eta(\|F\|+e)<e/4\), and set \(\delta=\eta c/[2(1-\eta)]\). At finite h on T,
\[
(1-\eta)(h-\delta)=h+\eta(-h-c/2)>h.
\]
Since \(h\le F-e\), the same choice gives \((1-\eta)(h-\delta)<F-e/2\), also at bottom. A decreasing \(C_R\)-net \(g_i\) to \(h-\delta\) has one index satisfying \((1-\eta)g_i<F-e/4\) throughout T, by compact strict-test covers. Choose \(N>0\) with \(-N<\min_T F\). Then
\[
q=\max\{(1-\eta)g_i,N\sigma\}\in C_R
\]
is strictly between h and F on T and EXACTLY zero off T. Both terms are below F on T; the first dominates the strictly larger scaled target at finite h, and q is finite at bottom. Off T its second term is zero and its first nonpositive.

The set of these continuous majorants, exactly zero off T and strictly above h on T, contains zero and is downward directed by insertion with the continuous minimum of two tests. The Urysohn construction in n5, applied on T, makes its pointwise infimum exactly h. Reverse pointwise order therefore gives an actual decreasing \(C_R\)-net. This proves full normalization descent, including mixed finite/bottom and mixed-zero functions, without an increasing closure or unproved flattening.

For arbitrary \(R\hookrightarrow B\), pull back to \((B\otimes_R S)_{\rm red}\), injective over S by n4. N3's traces at each normal local centre descend the pulled-back fibre-constant function to \(D_S\); it is precisely h pulled back from R. Full normalization descent then gives \(h\in D_R\). Conversely ideal extension preserves uniform and decreasing limits. Every primary change follows n1. Empty zero-dimensional sections have just their unique empty function. Artifacts: n6.md and the paper. Rerun: python build\_delivery.py. These are mathematical draft proofs, not consequences of registration.

\section{n7. Discharge of the primary-source geometry and real perturbation}
\textit{Earlier local supports: n1.}

Use n1 for rings and the boundary. We prove the three geometric inputs, using the exact published primary units recorded below. No supplied continuation label is a premise.

Let Y be the actual blowup of a proper primary ideal I on a POSITIVE-DIMENSIONAL reduced Noetherian local R. Dimension zero is the empty-boundary case of n1, treated separately. No minimal component of this positive-dimensional local reduced ring is zero-dimensional: that would make its maximal ideal a minimal prime and force dimension zero. The Rees algebra is a subalgebra of R[t], so is reduced. Its component primes are obtained from the minimal primes of R: projecting the Rees algebra to each component domain gives prime kernels with intersection zero; component-separating elements of R show these kernels are the minimal primes. Since I has nonzero image on each positive-dimensional component, every component of its blowup dominates a component of R. The standard f-chart is the degree-zero subring R[I/f] of R\_f. Multiplication by f is injective there and I becomes (f). Consequently I O\_Y is invertible with a regular local generator, defining an ACTUAL effective Cartier divisor E; O\_Y(-E) is the relatively ample tautological bundle. The morphism is projective and is an isomorphism away from the closed point. Relative and absolute ampleness agree over this affine base, by complete Stacks 29.38.4--5 (01VG).

G1: T=H\textasciicircum{}0(Y,O\_Y) is a finite R-module by complete Stacks 30.16.1 and 30.16.3 (0B5S). Restriction to all generic components embeds T in the total quotient ring of R, since Y is reduced and those components are dense. The inclusion R into T is injective. Global sections localize on the base: choose a finite affine cover of the separated Y; its pairwise intersections are affine, and H\textasciicircum{}0 is the kernel of the difference map between finite products of the affine section modules. Localization is exact and commutes with those finite products. Since Y is the identity off the closed point, (T/R)\_p=0 for p different from m. The finite module T/R is therefore killed by m\textasciicircum{}h for some h>=0. Fix ONCE on this model
\[
\mathfrak c_0=\mathfrak m^{h+1},\qquad \mathfrak c_0 T\subset\mathfrak m\subset R.
\]
The containment is as elements of R: m\textasciicircum{}h T lies in R and then one more factor m puts it in m. This primary correction is not the full normalization conductor.

G2: Complete Stacks 28.27.13(7) (01PR) gives eventual generation of F tensor A\textasciicircum{}k for any coherent F and ample A on the Noetherian scheme Y. Thus for each invertible L, A\textasciicircum{}\{k-1\} tensor L is generated for large k. Complete 28.27.5 says ample tensor generated invertible is ample, so A\textasciicircum{}k tensor L is ample. Complete 28.27.2 gives the ample power-root assertion. These are applicable to Y without normality or smoothness. Their proofs were read, including the affine-section criterion and the high-power generation equivalences; deeper referenced scheme-theoretic results are published background, not claimed independently reconstructed.

G3 first for integral bundles: restrict to the full projective closed fibre X over the residue field, which may be nonreduced. Corrected Keeler, math/0108068v5 Corollary 5.19, gives generation of A\textasciicircum{}m tensor N uniformly over ALL integral curve-nef N for m sufficiently large (a fixed A has a very ample power). Apply it with N\textasciicircum{}k and m=k-1. Thus G=A\textasciicircum{}\{k-1\} tensor N\textasciicircum{}k is generated, and
\[
(A\otimes N)^k=A\otimes G
\]
is ample by 28.27.5. Taking a power root shows A tensor N ample on X. Complete Stacks 30.21.4 (0D2N) extends fibre ampleness to relative ampleness on a neighbourhood of the closed point. Every open neighbourhood of the closed point in Spec of a local ring is the whole base. The argument therefore proves integral curve-nef plus ample on Y. It applies directly to the nonreduced fibre; reduction is unnecessary. If used, complete 30.17.5 (01XO) separately supplies nilpotent invariance of ampleness.

The Keeler correction is essential. The complete immediate 1.5 proof, its 4.9--4.10 regularity/generation inputs, and the complete 5.19 derivation were read together with the ENTIRE appended 2018 erratum. False original 3.3 (geometric integrality without the needed change of ground field) is not used. E1.3 replaces it with a finite faithfully flat altered base after localization and smooth geometrically integral fibres over the new base. E2.4 transfers vanishing through that finite base; E2.5 repairs the induction proving 1.5. The erratum retains 1.5 and hence 5.19 on arbitrary projective schemes over arbitrary commutative Noetherian rings. No normal, reduced, characteristic, or smooth hypothesis is introduced. Its historical de Jong alteration, EGA, Illusie, Kleiman and regularity dependencies are disclosed published background. We do not claim every historical edition has been independently read.

Here is the real-Cartier extension, proved explicitly. Write additive bundle notation in \(\operatorname{Pic}(Y)\otimes_{\mathbb Z}\mathbb R\). Call a real class real-ample when it is a finite positive real sum of integral ample classes. Rational curve-nef F plus integral ample A is real-ample: for rational t>=0, clearing a common denominator makes A+tF genuinely rational ample by the integral theorem just proved. For arbitrary real t, bracket t by two nonnegative rational parameters and take their convex combination. Hence A+tF is real-ample. If S=sum s\_j A\_j is real-ample, with s\_j>0 and s=sum s\_j, then
\[
S+F=\sum_j s_j(A_j+F/s)
\]
is real-ample for rational nef F.

Fix an integral ample H and integral classes L\_i spanning a real curve-nef D. G2 gives positive integers N\_i such that N\_i H+L\_i and N\_i H-L\_i are ample. On every contracted integral curve, their positive degrees imply |deg L\_i|<=N\_i deg H. For rational delta>0 choose rational D\_r in this finite span with error coefficients e\_i in D-D\_r satisfying sum N\_i|e\_i|<delta/4. Then F=D\_r+delta H/4 is rational curve-nef. The residual is explicitly real-ample:
\[
D+\delta H-F=(3\delta/4-\sum_i N_i|e_i|)H+
\sum_i |e_i|(N_iH+\operatorname{sign}(e_i)L_i).
\]
The H coefficient is positive; omit zero error terms. Therefore D+delta H=F+S is real-ample. For arbitrary real delta>0 first use a rational delta\_0 between zero and delta and add (delta-delta\_0)H. This establishes curve-nef real plus any positive ample perturbation.

We also need finite-span openness, not a finite-rank assertion about the whole Picard group. For an integral ample A and finitely many L\_i choose N\_i A +/- L\_i ample. If sum N\_i|e\_i|<1, the identity
\[
A+\sum_i e_iL_i=(1-\sum_i N_i|e_i|)A+
\sum_i|e_i|(N_iA+\operatorname{sign}(e_i)L_i)
\]
is an ample-generator expression. For a general real-ample S reserve one positive summand sA, apply this expression to perturbations of that summand, and retain the other summands. This proves openness on every finite-dimensional coefficient span, even when relations exist among its classes.

Finally a rational Cartier class that is real-ample is genuinely Q-ample. Let G be the subgroup of Pic(Y) generated by its finitely many integral constituents and the integral ample classes in a positive real expression. G is a finitely generated abelian group, with finite torsion; \(G\otimes_{\mathbb Z}\mathbb R\) embeds in \(\operatorname{Pic}(Y)\otimes_{\mathbb Z}\mathbb R\) because the REAL NUMBERS are flat over Z. This tensor coefficient field is not the local base ring R. In G modulo torsion, equality with the rational class is a finite rational linear system for the positive expression coefficients. A positive real solution is approximated by a positive rational solution in that rational affine solution space (row reduction over Q proves rational points dense). Clear denominators and then kill the finite torsion. A positive integer multiple of the rational class is a tensor product of positive powers of integral ample bundles, hence ample. This proves genuine Q-ampleness without asserting finite rank of Pic(Y) or a Neron--Severi group.

Artifacts: n7.md and source-application-ledger.md. Rerun: python build\_delivery.py. These source applications discharge G1--G3 rather than assume unnamed positivity theorems. Their published recursive dependencies remain explicit; execution cannot certify them.

\section{n8. Independent geometric construction and unconditional comparison}
\textit{Earlier local supports: n1, n3, n4, n5, n6, n7.}

Use n1, n3 and n7 for the construction and comparison, and n4--n6 for its descent rules. Assume the local reduction has positive dimension; dimension zero has the unique empty-boundary cone directly. Here is the geometric definition BEFORE its comparison to ideals. Admissible models are actual blowups Y\_I of proper primary ideals of the reduced excellent local germ. On such a model consider an exceptional real Cartier divisor
\[
D=-\sum_{j=1}^r d_j A_j,\qquad d_j\ge0,
\]
where every A\_j is an ACTUAL effective integral Cartier divisor supported on the closed fibre. Real Cartier divisors here lie in the integral Cartier divisor group tensored over Z with the REAL NUMBERS; their bundle classes lie in the corresponding real Picard group. Require deg\_C D>=0 for EVERY proper integral curve contracted to the closed point. This is line-bundle degree positivity, and actual Cartier effectivity; it is not effectivity of a list of nonnormal Weil coefficients. Neither ideal generation nor membership in a completed function cone defines the positivity test.

The model system is directed. Y\_\{IJ\} maps to both Y\_I and Y\_J. To justify this over a reduced ring, on Y\_\{IJ\} the product of the pulled-back ideals is invertible, locally (f) with f regular. Set J'=f\textasciicircum{}\{-1\}J in the total quotient sheaf. I J'=O, which expresses 1 as a finite sum of products. In a local ring one product ij' is a unit. For any x in I, xj' belongs to O, and x=(xj')/(ij') times i. Thus I is principal there, with a regular generator because ij' is a unit in the total quotient ring. J is its invertible inverse times (f). The universal property of the blowup gives the two maps. Pullback preserves actual effectivity. For a contracted integral curve its image is a point or an integral curve; in the latter case degree of a pulled-back bundle is its image degree times a positive field degree, and in the former case it is zero. Thus curve-nefness is preserved. Identifying data after a common pullback is legitimate.

E\_I is a Cartier order unit on Y\_I, not merely a numerical order unit. An integral exceptional Cartier F is trivial as a divisor off the closed fibre. The coherent modules (O(F)+O)/O and (O(-F)+O)/O, viewed in the total quotient sheaf, are supported on that fibre. On a finite affine cover a common power of I O kills them. Since I O=O(-E), this gives inclusions O(F-NE) subset O and O(-F-NE) subset O. An invertible subsheaf of O with a regular local generator defines an actual effective Cartier divisor. Therefore
\[
-NE\le F\le NE
\]
in actual Cartier order, for some integer N. For finite real sums this yields real order bounds too.

Define evaluation on ALL boundary points as follows. For v with support p, first pass to the valued field Frac(R/p). A generator f of I of least finite value gives the centre on the f-chart, because every a/f has nonnegative value. The centre is independent of this choice by the blowup universal property, or by the overlap units when two generators have the same least value. Pull O(F) back to the spectrum of this field's valuation ring. The support's generic point lies outside the exceptional fibre, so O(F) there has its canonical trivialization as O. This identifies the pulled-back invertible module with a rank-one lattice inside the quotient fraction field. If g is a generator of that lattice, set f\_F(v)=-v(g). Its image is nonzero by the generic trivialization. This is a pullback of an invertible bundle with generic trivialization; it does NOT assume a homomorphism from the total quotient ring of R to Frac(R/p). Different generators differ by units of the valuation ring and so have value zero. Extend linearly to real divisors. Evaluation is homogeneous on rays, additive, invariant under common pullback, and f\_E=v(I). The order-unit bounds make it finite and bounded on a primary section. This construction uses quotient fraction fields; it never loses a nonminimal support by trying to use a fraction field of R itself.

We now prove continuity and comparison, rather than stipulate them. For a negative rational relatively ample exceptional L, take arbitrarily large sufficiently divisible k for which O(kL) is generated. Its sections F\_k=H\textasciicircum{}0(Y,O(kL)) lie in the finite algebra T of n7 because O(kL) subset O. They are finite R-modules by 0B5S. With the FIXED primary ideal c\_0 of n7 set J\_k=c\_0 F\_k. It is an ideal of R: multiplication by R preserves sections, and c\_0 T subset m AS ELEMENTS OF R. It is proper. Away from m it is the unit ideal, because c\_0 is unit there and O(kL)=O there; localization of H\textasciicircum{}0 and generation give this assertion. Therefore J\_k is proper primary. At every valued centre, global generation says the images of the sections generate the local invertible module, and at least one coefficient is a unit. Thus
\[
-v(J_k)/k=f_L(v)-v(\mathfrak c_0)/k
\]
on ALL semivaluations. All terms are finite. Since c\_0 is primary, its value is uniformly bounded. Hence f\_L is a uniform limit of negative rational primary profiles, with an explicit error bound ||v(c\_0)||/k.

For an arbitrary integral exceptional F, G2 and the order-unit assertion let us choose N so L=F-NE is both actual negative and ample. Apply the preceding section construction for any generated divisible k. Its equality gives
\[
f_F=-v(J_k)/k+v(\mathfrak c_0)/k+Nv(I).
\]
Each ideal in this equality is primary. This proves continuity of every exceptional Cartier evaluation, without assuming continuity of nonnormal model coefficients. Real evaluations are finite sums, hence continuous. A negative actual effective divisor has nonpositive evaluation.

Let M\_geom be all evaluations of the independent negative curve-nef divisors defined above, including zero; set C\_geom to their uniform closure, and D\_geom to actual infima of nonempty decreasing C\_geom-nets, including bottom. We prove M\_geom subset C\_R. Write D=-sum d\_j A\_j. By n7, D-delta E is real-ample for every delta>0, since -E is ample. In the finite span of the A\_j and E, round ALL nonnegative coefficients UP to nearby rational numbers. Finite-span openness retains ampleness; the rounded divisor D' is actual negative and rational. It is genuinely Q-ample by the finite-subgroup argument in n7. Continuity and boundedness of the finitely many evaluations give ||f\_D'-f\_D|| arbitrarily small as delta and rounding errors tend to zero. Apply the fixed-c\_0 section construction to D' and send divisible k to infinity. This proves f\_D in C\_R. The generated section profiles can be chosen below f\_D, but only uniform approximation is needed. No full-conductor value is divided by k.

Conversely every raw finite REAL negative ideal combination is geometric: pull the finitely many primary-ideal exceptional divisors to their common product blowup. Each -E\_i is a pullback of an ample bundle and is curve-nef; each E\_i is actually effective. The combination meets the definition and evaluates to the given profile. Unit terms evaluate to zero. Thus
\[
Q_R\subset M_{\rm geom}\subset C_R,\qquad
C_{\rm geom}=C_R,\qquad D_{\rm geom}=D_R.
\]
This is the additional geometric comparison theorem required by ORIGINAL P12.2. It is not a renaming of ideal positivity. Raw equality with Q\_R is not claimed.

The geometric meaning is relative Cartier degree positivity on the explicitly stated primary-model system, followed by uniform and decreasing completion. We make no cofinality assertion for arbitrary proper birational models, no singular SNC or positive-characteristic resolution assertion, and no replacement of actual effectivity by nonnormal Weil coefficients. Finite pullback can also be checked on cores: a base primary ideal extends to a boundary ideal on the finite semilocal source; its blowup maps to the base blowup, actual effectivity pulls back, and degrees have the point/positive-degree rule. The comparison and n1, n4--n6 prove the full gauge and conductor rules without needing a separate raw descent claim.

Artifacts: n8.md and P12.2-paper.tex/PDF. Rerun: python build\_delivery.py. The independent curve test is the new geometric content; the uniform comparison is a proof. No envelope, product, energy, CLD, or classical radial-extension identification is asserted.

\section{n9. Full smooth BFJ specialization on all semivaluations}
\textit{Earlier local supports: n1, n3, n8.}

Use n1, n3 and n8. The published BFJ application in this note is ONLY at the closed point of a smooth affine variety over an algebraically closed field of characteristic zero. Dimension at least two is treated by BFJ; dimensions one and zero are treated directly below. No characteristic-free singular resolution is inferred.

The complete used units of Boucksom--Favre--Jonsson, Valuations and plurisubharmonic singularities, were checked from the bound publication: the setting; semivaluations and primary profiles; simple modifications, simplices, and retractions in Sections 1.2--1.7; Definitions 2.1 and 2.5, Proposition 2.2, and 2.7--2.8; 3.6--3.14; and the complete proofs of 3.9--3.10 through 3.18 and 3.22--3.25. The historical smooth resolution, usual multiplier ideal subadditivity, and smooth Izumi inputs remain disclosed published background. BFJ's nef Weil cone is its weak closed cone generated by formal-ideal divisors; its formal psh functions are finite and strongly continuous on quasi-monomials and have that nef coefficient divisor. They extend to ALL semivaluations by
\[
H_W(v)=\inf_\pi H_W(r_\pi v).
\]
Proposition 2.7 says H\_W<=H\_W composed with r\_pi; the composed functions decrease under refinement. The projective-limit statement 1.13 applies to the all-support compact semivaluation space, not just fraction-field valuations.

Proposition 3.11 proves substantive continuity on each CLOSED simplex. Its proof uses multiplier profiles h\_k=(1/k)log|L\textasciicircum{}2(kW)| and the estimate |h\_k-H\_W|<=A/k on divisorial points. Thinness A is bounded on each closed simplex. The continuous multiplier profiles are consequently uniformly Cauchy there, and their limit supplies the continuous extension, including its faces. One must not substitute the false assertion that a finite convex function is automatically continuous at the boundary of a closed simplex.

Correct 3.13 as follows. For a nonzero formal psh g, define, for integers j>=1,
\[
B_j=L^2(2^j g)+\widehat{\mathfrak m}^{\,4^j},\qquad
g_j=2^{-j}\log|B_j|=\max\{2^{-j}\log|L^2(2^jg)|,-2^j\}.
\]
The exponents were checked visually in the actual PDF on printed page 475. Subadditivity 3.10 gives the decreasing first term, and 3.9 gives convergence to g at every quasi-monomial. The truncation also decreases. The ideals contain a boundary power but early terms can be the unit ideal. Nonzero g has g(ord\_m)<0 by 3.14, and 3.9 at ord\_m makes the multiplier profile strictly negative there for all large j. Thus B\_j is EVENTUALLY proper primary; discard a finite prefix. For g=0 use the UNIT ideal, not a sequence of proper primary ideals decreasing to zero. The identically bottom function is not a finite formal psh function on quasi-monomials; add it separately by -N=-v(m\textasciicircum{}N).

The approximants decrease to g on ALL semivaluations. Given finite t>g(v), choose a retraction with g(r\_pi v)<t by the definition of the all-retraction infimum, even when g(v) is bottom. Then choose j with g\_j(r\_pi v)<t. The formal-psh inequalities give
\[
g(v)\le g_j(v)\le g_j(r_\pi v)<t.
\]
This proves full convergence; it is not merely divisorial or quasi-monomial convergence. N1 contracts each completed primary B\_j exactly to R, preserving the profile. The completed unit also contracts to the unit. Thus every BFJ function, with bottom adjoined, belongs to D\_R, and every finite continuous BFJ function belongs to C\_R by the compact decreasing-continuous uniform-convergence argument (Dini's open-cover proof).

Conversely any finite real primary profile is BFJ formal psh, since its coefficient divisor is nef and its evaluation is continuous on simplices; principalization and the published retractions give its canonical all-semivaluation extension. Let g be a uniform limit of such profiles. Its divisorial coefficients give a finite weak limit W in BFJ's closed nef cone. Proposition 3.11 gives H\_W. Uniform convergence on quasi-monomials shows g=H\_W there: they agree on dense divisorial points of each simplex and both are continuous there. Moreover the same uniform error estimate survives taking the infimum over ALL retractions. Thus g(v)=inf\_pi H\_W(r\_pi v) at every semivaluation. This proves C\_R is EXACTLY the finite continuous BFJ subclass.

Now let g=inf\_i g\_i be a decreasing C\_R-net. BFJ 3.14 gives g\_i(v)<=g\_i(ord\_m) at every v (first on quasi-monomials, then by retractions). If g(ord\_m) is bottom, g is bottom everywhere. Otherwise 3.14 also gives C(v)g\_i(ord\_m)<=g\_i(v) at every quasi-monomial v, so g is finite there. Its divisorial coefficients give a finite weak-nef W. On a simplex the decreasing limit g is finite convex. For any point x take its MINIMAL face; x lies in that face's relative interior, where finite convex functions are continuous. H\_W is continuous on the whole face by the actual 3.11 theorem. Their equality on the dense rational divisorial points of that relative interior proves equality at x. Vertices are already divisorial. This handles every face without asserting closed-simplex continuity from convexity alone.

Finally, extended infima commute over the Cartesian product of the net and ALL models:
\[
g(v)=\inf_i\inf_\pi g_i(r_\pi v)
=\inf_\pi\inf_i g_i(r_\pi v)
=\inf_\pi H_W(r_\pi v).
\]
No arbitrary decreasing-net flattening principle is used. Hence D\_R minus the identically bottom function is exactly the full BFJ formal psh class with its canonical extension to all semivaluations. D\_R is that class with bottom adjoined, and n8 gives the same statements for D\_geom and C\_geom.

For a smooth DVR every nonempty normalized boundary is a singleton. Primary ideals are powers of the parameter, so C is all finite nonpositive constants and D all extended nonpositive constants. The closed point itself is an effective Cartier divisor, and degree conditions on contracted curves are empty, giving the same independent geometric core. In dimension zero the centred boundary is empty and all statements mean its unique empty function. General primary gauges in the BFJ range follow n1's exact homogeneous cocycle, with bounded positive denominators preserving uniform and decreasing convergence. Completion homeomorphism and primary contraction apply without claiming equivalent model categories.

Artifacts: n9.md, reports/source-images/bfj-475.png, source-application-ledger.md. Rerun: python inspect\_primary.py; python build\_delivery.py. This specialization has precisely the published smooth affine algebraically closed characteristic-zero domain; it does not transfer singular SNC theory to arbitrary excellent germs.

\section{n10. Nonisolated cusp: separation from the entire finite-real raw cone}
\textit{Earlier local supports: n1, n3, n4, n8.}

Use n1, n3, n4 and n8. Work in characteristic zero, with
\[
R=k[t^2,t^3,z]_{(t^2,t^3,z)},\quad S=k[t,z]_{(t,z)},\quad
\mathfrak a=(t^2,t^3,z),\quad \mathfrak c=t^2S.
\]
Indeed S is finite via t, is normal, and has the same fraction field. R consists of polynomials with no term of t-degree one, localized at the stated maximal ideal; multiplying by t shows its conductor is exactly t\textasciicircum{}2S. The quotient R/c is k[z] localized, and S/c is its square-zero t-thickening. Their all-semivaluation boundaries are the same singleton when nonempty. N1 therefore makes restriction V\_\{aS\}(S) to V\_a(R) a continuous bijection and hence a homeomorphism, including the support (t) upstairs. This is a two-dimensional nonisolated cusp, not just a finite curve link.

Write s=w(t), u=w(z), b=z+t and B=w(b); min(2s,u)=1. Allow s,u,B to be infinite whenever the normalization permits. The bounded continuous positive profile
\[
A(w)=w((b,t^2))=\min\{B,2s\}
\]
descends topologically. For k>=1 define actual downstairs ideals
\[
K_k=(b^k(z-kt),\ t^2b^k,\ t^{2k+2})\subset R.
\]
The first generator has zero t-linear coefficient: the two contributions k z\textasciicircum{}k and -k z\textasciicircum{}k cancel. The other two have t-degree at least two. Localizations do not change membership. The ideals are proper primary: the last generator puts t\textasciicircum{}2 and t\textasciicircum{}3 in the radical, and the first then puts z in it.

For EVERY normalized semivaluation, every generator has value at least kA. For the first this is kB+w(z-kt)>=kA, and the other two are immediate. The upper bound is a complete case analysis. If A=2s<=B, cancellation forces s=u=1 (different values would give B=min(s,u)<2s), and the last generator has value kA+2. If A=B<2s and s<=u, normalization gives s<=1, and the second generator has value kA+2s<=kA+2. If s>u, including s infinite, then u=1 and B=w(z-kt)=1; the first generator has value kA+1. The case u infinite belongs to the second case. Thus on ALL supports, including cancellation and infinite coordinates,
\[
0\le v(K_k)/k-A\le2/k.
\]
Hence -A lies in C\_R, and is a normalization-raw profile in N\_R. This analytic bound is a proof; a finite sample check is only a diagnostic.

We separate A from the ENTIRE finite REAL positive raw cone P\_R, not merely rational single-ideal profiles. Let w\_infty kill t and give z value one. Let w\_star be the monomial valuation in coordinates (t,b) with weights (1,2); then z=b-t has value one, so both valuations are in the same primary section. They give A(w\_infty)=1 and A(w\_star)=2.

For ANY proper primary downstairs ideal I, put d=w\_infty(I), a positive integer. Choose f in I attaining d; its local denominator is a unit at both valuations. Expand in k[[t,z]]: no coefficient of t-degree one occurs. Its degree-d homogeneous part has nonzero z\textasciicircum{}d coefficient and zero t z\textasciicircum{}\{d-1\} coefficient. In characteristic zero it cannot be a scalar multiple of b\textasciicircum{}d=(z+t)\textasciicircum{}d. After substituting z=b-t, it therefore contains a nonzero term t\textasciicircum{}\{d-j\}b\textasciicircum{}j with j<d. That monomial has w\_star-value d+j<=2d-1. Terms of other total degrees cannot cancel it, since the linear substitution preserves total degree. If other terms have still smaller value they only strengthen the bound. Consequently
\[
w_\star(I)<2w_\infty(I).
\]
Every nonzero finite real positive combination of proper primary gauges retains this strict inequality; unit terms are zero. But A has equality. Thus A is outside P\_R, and -A is outside Q\_R. We have proved N\_R is not Q\_R and C\_R is not Q\_R in this example. Their uniform closures still agree by n4. This does not assert raw geometric and ideal equality.

Finally, v(c)<infinity is an OPEN complement of the CLOSED infinity stratum, not generally closed. Monomial valuations w\_N(t)=N, w\_N(z)=1 converge pointwise to w\_infty. Their conductor values are 2N, while w\_infty(c)=infinity. The quantities v(c)/N are therefore not uniform errors on the whole section. Neither descent nor comparison uses such an error globally; n4 uses quotient estimates at infinity, and n8 uses a fixed PRIMARY correction.

Artifacts: n10.md, exact\_checks.py, reports/exact-checks.json. Rerun: python exact\_checks.py; python build\_delivery.py. The script reports its exact finite input domain and does not replace the universal proof or the raw-cone separation argument.

\section{n11. Rejected shortcuts and the radial scope constraint}
\textit{Earlier local supports: n1, n2, n3, n4, n8, n10.}

Use n1--n4, n8 and n10. These are diagnostics, not extra hypotheses.

An incompatible-contraction shortcut is false even over a smooth normal surface. Inject A=k[x,y]\_(x,y) diagonally into A times A and take J=((x,y\textasciicircum{}2),(x\textasciicircum{}2,y)). Then I\_N=J\textasciicircum{}N intersect A=(x,y\textasciicircum{}2)\textasciicircum{}N intersect (x\textasciicircum{}2,y)\textasciicircum{}N. The m-order of both fibre ideals is one. A monomial x\textasciicircum{}a y\textasciicircum{}b belongs to I\_N exactly when 2a+b>=2N and a+2b>=2N. Summing gives a+b>=ceil(4N/3); balanced nonnegative exponents with that sum achieve both inequalities. Therefore
\[
\operatorname{ord}_{\mathfrak m}(I_N)=\lceil4N/3\rceil,
\]
whose normalized limit is 4/3, not one. The two ideal profiles were not fibre constant. No general contraction-as-fibre-minimum formula is used in n4--n6.

The literal positive-gauge inequality in BdFFU Proposition 2.4(b) has the wrong sign. At a smooth surface take parameters x and b=x+y, and the monomial valuation v(x)=1, v(b)=2. On the first-blowup dual complex its retraction is ord\_m. For I=(x+y,x\textasciicircum{}3), v(I)=2 whereas r(v)(I)=1. Hence the printed inequality r(v)(I)>=v(I) fails. The negative function -v(I) has the expected opposite inequality. Complete Definition 2.1--2.2 and Proposition 2.4 with proof were read from the bound BdFFU paper, solely for this diagnostic. Its own normal complex-variety hypotheses do not repair the sign. It supplies no premise of the construction.

The geometric boundary cone is not asserted to be the cone of literal CLD or classical logarithmic radial extensions. On a nodal curve R=k[x,y]\_(x,y)/(xy), its finite normalization has two DVR centres. The tuple (-1,0) is in C\_S and is fibre compatible: the conductor has finite positive value on both boundary points, so its restriction has no identified pair. N4 therefore puts (-1,0) in C\_R, and n8 puts it in C\_geom. For a classical analytic node with two normalized discs, a literal zero logarithmic slope on one disc forces the nodal value to be at least zero by upper semicontinuity. The other literal negative slope tends to minus infinity at its origin. If its nodal value is at least zero, the subharmonic maximum principle on that disc (the outer-circle value is zero and interior values are negative) forbids the resulting interior maximum. Thus this mixed-zero profile cannot be a literal classical psh radial extension. The original dossier's corresponding CLD closed-disc obstruction is kept as a scope constraint, not silently overridden or used as a theorem premise. We make no CLD comparison theorem for other singular germs. A boundary trace of a different kind is a separate question.

Artifacts: n11.md, exact\_checks.py, reports/exact-checks.json. Rerun: python exact\_checks.py; python build\_delivery.py. The monomial computation is proved for all N; finite enumeration only checks a specified range. The sign example is exact. This note rejects invalid approaches while retaining the independent geometric construction and its precise scope.

\section{n12. Complete ORIGINAL P12.2 candidate and deliverable evidence}
\textit{Earlier local supports: n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11.}

Use every earlier local note n1--n11. We claim a complete solution of the exact ORIGINAL P12.2 target, under the assignment's permitted published-background rule, as an unverified mathematical draft requiring subsequent independent whole-original review.

For every excellent singular or nonnormal local germ, reduce nilpotents and take its intrinsic centred ray boundary. Actual primary blowups carry an independent geometric core: negative ACTUAL effective finite real Cartier presentations having nonnegative degree on every contracted proper integral curve. Evaluation uses the support quotient fraction field and its valued centre. The admissible model system, common pullbacks, order units and nonminimal supports are explicit. N7 proves the exact primary-source G1--G3 applications, including the corrected Keeler v5 route on arbitrary nonreduced projective fibres and every real perturbation/rationalization transition. N8 proves C\_geom=C\_ideal and D\_geom=D\_ideal; degree positivity was defined before that comparison, so this is not merely an ideal completion renamed.

N1 proves the intrinsic primary-gauge cocycle, completion and exact normalization conductor fibres. N2--n6 prove full continuous-uniform and actual decreasing-net descent for EVERY reduced excellent finite injection, including unbounded, allzero, allbottom, partialbottom, mixedzero, conductor-infinite and nonminimal supports. Norm traces have generic inseparable lengths, quotient-support Gauss values and proved full fibre support. Conductor induction covers all minimal/zero-dimensional components and uses a positive boundary factor, a common graded exponent, the exact residue fibre product and compact open covers. Internal increasing profiles never serve as an assumed completion operation; actual completed descent is obtained by insertion and downward-directed continuous majorants.

N9 proves the FULL smooth BFJ specialization on ALL semivaluations in its actual smooth affine algebraically closed characteristic-zero domain. It uses substantive closed-simplex continuity, minimal-face interiors and commuting all-retraction infima, corrects zero/unit and eventual proper-primary approximants, and treats bottom, DVR and empty dimension zero separately. N10 separates the entire finite REAL raw cone from its normalization-raw and continuous completions by a nonisolated cusp, with the universal error <=2/k. N11 rejects the incompatible-contraction shortcut and wrong BdFFU sign and preserves the mixedzero radial obstruction. P12.3--P12.6 envelopes/products/energy/operator theory remain separate targets, not silently supplied.

No exact P12.2 mathematical gap is retained. The limits are explicit: only the stated primary-model system, no arbitrary-model cofinality, no nonnormal Weil substitute, no singular positive-characteristic SNC transfer, no literal CLD/classical radial identity, and no intersection-multiplicity theory for nilpotents. Published recursive historical dependencies are disclosed rather than claimed fully independently reread. There are zero accepted incoming notes and no provenance labels in support lists. The complete original-task.json, entire family dossier, all thirteen whole mathematical DATA files, and all complete immediate used primary units were read, with proof-body display truncations repaired. Hashes and old flags grant no mathematical status.

Fresh deliverables are P12.2-paper.tex and P12.2-paper.pdf, argument.md, source-application-ledger.md, exact-scope.md, whole-proof-coverage.md, original-scope-decision.md, native-notes.json, n1.md through n12.md, and the fresh scripts/inputs/reports. Native-notes contains the complete proof-bearing local chain, not just an index. Reports retain input and own SHA-256 hashes, environment details, local source-image inspection, exact finite checks, every PDF build attempt/warning, execution history, and final integrity/support audit. No immutable input was edited and no supplied builder/checker/binder was executed or imported.

The observed finite diagnostic result is PASS on 1600 cusp value cases (k=1..32, sixteen pairs of rational weights, coherent equal-weight cancellation cases and two infinite-coordinate endpoints), 32 exact t-linear cancellations, and all contraction minima for N=1..36 in the box 0<=a,b<=2N. The largest sampled value J-kA is exactly 2. These observations do not establish the universal mathematical claims; their proofs are n10--n11. PDF compilation and support/hash auditing likewise establish artifact consistency, not mathematical correctness.

Rerun from this directory: python audit\_inputs.py; python inspect\_primary.py; python exact\_checks.py; python build\_delivery.py; python final\_audit.py. The build uses pdflatex with -no-shell-escape. The source inspection only rasterizes three explicitly bound local pages. No network, provider, subagent or heavy compute was used; no supervised heavy-compute facility was provided or needed. Account/auth/runtime/HOME/CODEX\_HOME/proxy/CA state was not mutated. All fresh writes are in this workspace. The requested model designation is a caller execution request, not an independently measured theorem or provider attestation.

Candidate=true here means that the last note claims the entire ORIGINAL P12.2 construction, comparison, smooth specialization and gauge/conductor rules. It does not mean paper acceptance, catalogue closure or independent verification. Subsequent independent whole-original review is required.

\section*{Reproducibility and review status}
The accompanying source-application-ledger, exact-scope, whole-proof-coverage,
and original-scope-decision files state the exact domains, complete immediate
source units checked, recursive dependencies, limits and proof coverage.
The full native-notes JSON repeats every proof body and its earlier local supports.
Input and own hashes, finite diagnostic inputs/output, environment and every
build attempt are retained in reports. No supplied executable or network was used.
Execution establishes reproducibility only. The candidate flag is a draft
solution claim and does not accept the paper or close a catalogue.
\end{document}

END ENTIRE P12.2-paper.tex

BEGIN ENTIRE mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json
{
  "recorded_utc": "2026-10-08T12:26:53.361733+00:00",
  "atom": "P12.2",
  "continuation": 331,
  "source_unchanged": true,
  "original_statement_unchanged": true,
  "independent_geometry": "Actual primary blowups; actual negative effective finite REAL Cartier presentations; nonnegative degree on EVERY contracted proper integral curve, defined before ideal completion. Uniform comparison and actual decreasing-net comparison then proved.",
  "exact_general_scope": "Every excellent reduced singular/nonnormal local ring in positive dimension, arbitrary characteristic and residue field; nilpotents invisible, zero-dimensional local reduction boundary empty; ALL semivaluation supports retained.",
  "model_system_scope": "Directed actual primary blowups with pullback and arbitrary-support evaluations. Cofinality among ALL proper birational models and a full arbitrary-model b-divisor classification are unproved and unclaimed.",
  "smooth_specialization_scope": "Published BFJ smooth affine CLOSED germs over an algebraically closed characteristic-zero field, dimension>=2, plus direct DVR/empty cases. ALL-retraction extension, closed-face continuity, eventual proper-primary approximation, zero/unit and bottom exceptions retained. No singular/positive-characteristic SNC transfer.",
  "normalization_and_finite_scope": "Full conductor quotient; finite OPEN singleton stratum and CLOSED infinite-value quotient stratum; positive C and actual decreasing-net D descent, including mixed zero/partial bottom. Full finite-source fibres retained; generic trace only on actual generic-dominating domain components; no vertical generic degree invented.",
  "raw_cones": "Only Q subset normalization-compatible raw family subset C and equal uniform closures; no raw equality. Fixed PRIMARY c0 gives uniform section-ideal error; nonprimary conductor errors not uniform.",
  "source_precision": [
    "Use Keeler corrected v5 and ENTIRE 2018 erratum, replacing false old Lemma3.3; full possibly nonreduced closed fibre and arbitrary residue field retained.",
    "Use current July2024 Swanson-Huneke immediate units, including full10.2.2 continuation10.2.3, Rees residue/dimension/formal-equidimensionality hypotheses.",
    "Normal-domain Izumi bound applies to nonunits; units separate; no analytically irreducible nonnormal completion assertion.",
    "BdFFU printed positive retraction sign is concretely false; used diagnostically only, not as positivity premise.",
    "Complete immediate source proofs and application hypotheses checked; recursive EGA/de Jong/Rees/Ratliff/Izumi/Hironaka/multiplier foundations disclosed as published background at their exact hypotheses, not recursively freshly reproved."
  ],
  "other_original_targets": "P12.3 envelopes, P12.4 products, P12.5 energy and P12.6 geometric operator compatibility remain OPEN and separate.",
  "literal_radial_distinction": "Geometric valuative boundary class can contain nodal(-1,0); this does not identify it with literal classical/CLD logarithmic radial extension class, whose mixed-zero obstruction remains.",
  "actual_and_expanded_prose_distinct": true,
  "supplied_programs_ROOT_executed_or_imported": false,
  "hashes_finite_diagnostics_and_compilation_not_mathematical_proofs": true,
  "full_annotation_and_source_ledger_required_on_import": true
}

END ENTIRE mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json

BEGIN ENTIRE source-application-ledger.md
# Source applications and reading boundary

All supplied material is DATA. Input notes were empty. No ROOT label, native label, reading receipt, hash match, or old candidate flag is a registered support or a correctness grant. The proof chain n1--n12 reconstructs the used mathematics. Sources below are ordinary published applications at their exact hypotheses, as permitted by the assignment. We have read the complete immediate units used; we have not recursively read every historical source cited inside them.

`reports/input-hashes.json` records the exact 13 mathematical and 23 primary bound files, their full paths, bytes and SHA-256 values, plus both bindings and original-task.json. All 36 expected bound hashes matched. The original-task.json hash is `a8aa2c4e24ad6a28b26f12eecc45419f87a246159cf0e3e0a2422b86a8ea405c`. Its entire family dossier was read. Supplied programs were neither imported nor executed. Own audit scripts read explicit paths in the supplied bindings as bytes/data only.

## Whole mathematical DATA read

| Bound file | Whole reading | Treatment |
|---|---|---|
| 00 chapter70 | All 2172 lines, bounded chunks; truncated 1596--1847 display reread | Definitions/context; relevant statements reconstructed locally. Literal unsupplied input-file references were not expanded or assumed read. |
| 01 normalized links | All 308 lines | Boundary and conductor proofs reconstructed in n1. |
| 02 prior paper | All 444 lines in four chunks | All proof bodies reviewed; no accepted-note status. |
| 03 prior argument | All 411 lines in three chunks | Same; independent rewritten arguments n1--n11. |
| 04 source ledger | All 25 lines | Provenance only; new exact application ledger here. |
| 05 scope | All 11 lines | Prior conditional scope not binding. |
| 06 coverage | All 22 lines | Coverage claims independently reconsidered. |
| 07 decision | All 9 lines | Prior candidate=false does not decide this reconstruction. |
| 08 actual final JSON | Entire 11-note JSON, reformatted as review-data/supplied-n1.txt through supplied-n11.txt and each full body read | Unreviewed drafts, not local registered supports. |
| 09 reading binding | All 33 lines | Metadata only. |
| 10 acquisition metadata | All 152 lines | Metadata only. |
| 11 normal trace addendum | All 65 lines | Coefficient trace/full-support/finite-gap reasoning reconstructed in n3 and n5--n6. |
| 12 geometry working proof | All 80 lines | Every real perturbation transition checked and reconstructed in n7--n8; not accepted wholesale. |

## Immediate published primary applications

Line numbers refer to the exact bound text extraction, except the single HTML-only lemma. PDFs and their text counterparts are both hashed; this is not a claim to have visually read every PDF page.

| Source and complete units read | Exact application | Restrictions and recursive dependencies |
|---|---|---|
| Stacks 0B5S, 30.16.1 all five assertions/proof and 30.16.3, whole text 1--67 | Finite sections on proper schemes with an ample bundle over Noetherian base; finite T and F_k on primary blowups in n7--n8 | Usual Noetherian projective coherent cohomology is published background. H0 localization is separately proved by the finite affine-cover kernel. |
| Stacks 01PR, 28.27.2 and 28.27.5 (1--47), 28.27.13 all nine equivalences/proof (70--116) | Ample power roots, ample times generated bundle, and high-power generation; n7 G2, continuity shift, genuine Q-ample comparison | Affine-section ampleness criterion and preceding referenced scheme results disclosed. Not a singular resolution theorem. |
| Stacks 01VG, whole text 1--104, especially 29.38.4--5 | Relative ampleness equals absolute ampleness over affine local base; n7 | Relative ampleness definition and base locality used at exact projective scheme. |
| Stacks 0D2N, whole text 1--42, full 30.21.4 proof | Ample restriction to the possibly nonreduced closed fibre implies relative ample near the closed point, hence on entire local base | Immediate proof uses lifting from 30.21.3/formal functions, finiteness from 30.21.2 and finite pullback ampleness 29.38.7. Those recursive source bodies are not all separately read. |
| Stacks 01XO, full 30.17.5 statement/proof, 55--72 | Optional nilpotent invariance of fibre ampleness | Main Keeler route uses full nonreduced fibre directly, so no reduction is needed. |
| Keeler math/0108068v5: setting and 1.5 at 50--135; definitions 2.8--2.9, 2.13--2.14 at 210--286; complete 4.9--4.10 at 824--888; complete original 1.5 proof and 5.19 derivation at 1220--1288; ENTIRE appended 2018 erratum, 1780--2041 | 5.19: fixed ample powers uniformly generate twists by ALL curve-nef integral bundles on any projective scheme over any commutative Noetherian ring; yields integral ample plus nef on full fibre, n7 | Original 3.3 is false and expressly NOT applied. E1.3 changes to finite faithfully flat base with smooth geometrically integral fibres after localization. E2.4 and E2.5 repair 1.5; 5.19 remains valid. Historical de Jong, EGA, Illusie, Kleiman and regularity results are disclosed, not independently recursively reread. No char/smooth/normal/reduced hypothesis is added. |
| Swanson--Huneke CURRENT July 2024 author PDF: full 1.1.5 (580--624); 1.2.3--5 (650--722); 6.4.1--2 (5920--5979); 6.8.1--4 (6540--6630) | Support-quotient lifting agrees with n1's Zorn proof; all-minimal-component integral dependence criterion in n2, used for Q=K a^L in n4--n5; common exponent also proved by finite graded module argument | Zero-dimensional nonunit components must have Q-image zero; positive boundary factor L>0 ensures this. Book text-extraction bars repaired by visual page inspection. No assertion of byte identity with 2006 print. |
| Same book: complete 10.2.2 proof ending in 10.2.3 (9230--9390); 10.4.3 proof (9698--9756); B.3.2 and immediate context (19258--19310); B.5.1/proof (19435--19468) | Rees DVRs of positive-dimensional excellent local domains, residue trdeg under formal equidimensionality, exact birational dimension formula, universal catenarity to formal equidimensionality; n2 and density in n6 | B.3.2 describes a modification of its earlier dimension argument. Mori--Nagata, Ratliff, Rees historical dependencies disclosed. Zero-dimensional components handled separately. |
| Stacks 0C23 normal completion, full immediate HTML lemma 15.53.6 and proof | Normal excellent local domain has normal/domain completion and hence is analytically irreducible/unramified; n2 | Uses normal formal fibres and Algebra 10.163.8; latter not independently read here. No assertion for arbitrary nonnormal domain. |
| Rond--Spivakovsky 1404.4885v1 pages 1--2, text 1--115: Definitions 1.1--1.2 and Theorems 1.3, 1.4, 1.7 | Izumi--Rees comparability on an analytically irreducible local DOMAIN; asymptotic m-order and order error yield nonunit divisorial bound, n2 and zero dichotomy n6 | Units handled separately; literal strict Remark 1.6 not used. Original Rees 1989 and historical Izumi not independently read. |
| Swanson Rees-valuations survey, ENTIRE Section 5, text 833--921 | Check 5.2 really has complete-domain hypotheses | General analytic-domain application uses exact Rond--Spivakovsky 1.3 instead. |
| BFJ published Valuations and psh Singularities: complete setting and relevant Sections 1.2--1.7, 2.1--2.2, 3.1--3.6, text 1--1398 in bounded chunks; proofs through 3.25 | Full smooth BFJ recovery, n9, including substantive closed-simplex 3.11, corrected proper-primary 3.13 and all-retraction infima | ONLY smooth affine closed germ over algebraically closed characteristic zero, dimension>=2; DVR and empty dimension zero direct. Historical Hironaka, multiplier subadditivity, usual smooth Izumi disclosed. No arbitrary-characteristic singular SNC transfer. PDF page 475 inspected to settle 2^j and 4^j exponents. |
| BdFFU published singular multiplier ideals: complete Definitions 2.1--2.2 and Proposition 2.4 proof, text 175--303 | DIAGNOSTIC ONLY: positive-gauge 2.4(b) sign fails in explicit smooth example, n11 | No premise imported. Normal complex-variety hypotheses and literal sign issue preserved. |

The five bound geometry HTML counterparts are hashed data counterparts, not separately claimed line-by-line HTML proofs. The geometry packet has five Stacks HTML/text pairs plus Keeler PDF/text; the algebra packet has three PDF/text pairs plus one HTML lemma; the smooth packet has two PDF/text pairs, totalling 23 primary files. Immediate proofs were read from their text form, with three selected PDF pages inspected for extraction ambiguities.

## New proof boundary

Norm-coefficient fibre support, quotient Gauss identities, real uniform lattice closure, common graded exponent, bounded conductor approximation, insertion and mixed-zero descent, actual model degree positivity, the fixed-primary section correction, real perturbation and finite-Picard-subgroup rationalization are proved in the local note chain. They are not accepted on the strength of familiar names or supplied reading metadata. Small exact checks test only stated finite domains. Build success, support validation and matching hashes are reproducibility evidence, not mathematical acceptance.

Rerun locally: `python audit_inputs.py`; `python inspect_primary.py`; `python exact_checks.py`; `python build_delivery.py`; `python final_audit.py`. No network or supplied executable is needed.

END ENTIRE source-application-ledger.md

BEGIN ENTIRE exact-scope.md
# Exact scope

The construction is for every excellent local germ, after reduction, with a nonempty intrinsic centred ray boundary when the local reduction has positive dimension. Sections use arbitrary proper primary ideals. Nonminimal prime supports and infinite function values are retained. Zero-dimensional local reduction gives the empty boundary. For nonreduced germs this is a semivaluation theory of the reduction; nilpotent intersection multiplicities are not supplied.

The independent geometric core uses actual primary blowups of the reduced germ, actual negative effective finite real Cartier presentations, and degree >=0 on every contracted proper integral curve. Common product-ideal blowups identify presentations. There is no assertion that this system is cofinal in all proper birational models, no nonnormal Weil-coefficient substitute for Cartier effectivity, and no arbitrary-characteristic resolution assertion. The uniform and actual decreasing completions are justified by the proved comparison C_geom=C_ideal and D_geom=D_ideal; core positivity is geometric before that comparison.

P is the finite REAL positive ideal cone; Q=-P; C is its finite continuous uniform closure; D consists of actual decreasing C-nets with bottom allowed. N is the normalization-RAW compatible cone. Q subset N subset C, and both uniform closures equal C. The nonisolated cusp separates N and C from Q. No raw equality is asserted.

Primary-gauge changes are the exact homogeneous cocycle u_b(v/v(b))=u_a(v)/v(b), with bounded positive denominator. Completion is an all-semivaluation homeomorphism with exact primary contraction. Normalization branches are local normal centres above the marked point, not merely minimal components. Finite conductor value gives a singleton fibre; infinite value gives exactly the conductor quotient identification. The infinity stratum is closed and its finite complement open. Both C and D descend exactly iff constant on all fibres, including mixedzero and partialbottom. The same class-level pullback/descent result holds for every reduced finite injection over an excellent reduced local target. This supplies the cone rules asked in P12.2, not all geometric operators of P12.6.

Full BFJ specialization is proved on ALL semivaluations at a smooth affine closed germ over an algebraically closed field of characteristic zero. C is exactly its finite continuous subclass; D is its full canonically retracted formal psh class with identically bottom adjoined. Smooth DVR and empty dimension zero are direct. Source domains are not enlarged to positive-characteristic singular SNC settings.

The cone is not identified with literal classical or CLD logarithmic radial extensions. The mixedzero nodal profile (-1,0) belongs to this boundary cone and remains excluded by the stated radial compatibility obstruction. Global projective trivially valued energy constructions are not claimed to solve this local target.

P12.3 obstacle envelopes, P12.4 bounded mixed Monge--Ampere products, P12.5 energy and P12.6 geometric envelope/product/operator functoriality are separate. They are not constructed here and their omission is not a P12.2 gap. This manuscript is a complete-solution candidate for ORIGINAL P12.2 only, requiring subsequent independent whole-original review.

END ENTIRE exact-scope.md