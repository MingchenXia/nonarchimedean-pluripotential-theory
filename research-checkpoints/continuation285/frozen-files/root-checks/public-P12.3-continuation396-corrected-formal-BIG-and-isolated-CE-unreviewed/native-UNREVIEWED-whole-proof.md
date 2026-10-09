# n1. Whole-input review and the geometric envelope calculus

Only the entire qualified G331 is used as an incoming theorem. All of native274/391, native271/386 and amended ROOT392 are mathematical data. In particular 391's scoped favorable review of 386 is not a correctness grant. The mathematical conclusions below are independent arguments, relative to G331 and the explicitly named ordinary foundations.

Let X be a primary normalized boundary of an excellent reduced local ring. Use G331's independently geometric continuous cone C and actual decreasing-net completion D. They are nonpositive, closed under addition, nonnegative scaling and finite maximum; C is uniformly closed, and its rational primary profiles are dense. All prime supports are retained. For finite continuous f define p(f)=sup{u in D:u<=f}. A sufficiently negative primary constant is a competitor, so p(f) is finite and bounded.

If h_i decreases in C to h<=f, the open sets {h_i<f+epsilon} cover the compact space. Directedness selects one term valid everywhere. Its negative constant shift h_i-epsilon belongs to C, is below f, and is at least h-epsilon. Thus C and D give the same raw supremum. It is lower semicontinuous and satisfies ||p(f)-p(g)||<=||f-g||, by negative shifts in both directions. If it is continuous, finite maxima of continuous competitors approximate it uniformly, so it belongs to C. Conversely C membership implies continuity. D membership also implies continuity, since D functions are upper semicontinuous. A greatest D minorant, a maximal D minorant, and p(f)^* belonging to D are equivalent to this property: maxima make any maximal element greatest, and p(f)^*<=f makes a positive regularization a competitor. Hence regularization alone does not recognize positivity.

The ideal J_k(f)={r:v(r)>=-k f(v) for every v in X} contains a primary power, is unit or primary, and is integrally closed. The latter follows by killing the support and applying the least-term test to a monic integral equation. Products satisfy J_k J_l subset J_(k+l). Rational density with negative shifts gives
\[
p(f)=\sup_k[-v(J_k(f))/k]=\sup_n[-v(J_{n!}(f))/n!].
\]
The factorial profiles increase, without invoking increasing closure of D.

Decreasing closure of D follows by insertion, not by flattening representations. On a normal branch, G331's zero dichotomy says that a nonzero D function is everywhere strictly negative, hence bounded above by a negative constant on the compact link. If u_i in D decreases to u, either all terms are zero or a tail lies below -c. Given finite continuous F>u, compact strict-test covers choose one u_i<F, then one continuous representing majorant g with u_i<=g<F and g<-c/2. Scaling g by 1-b for sufficiently small positive b keeps it below F and makes it strictly above u at finite points; bottom points cause no difficulty. Applying this insertion to the minimum of two continuous majorants proves that the majorants are downward directed. Urysohn cutoffs on the compact Hausdorff link show their infimum is u. This supplies one actual decreasing C net. For a reduced germ pull back to finitely many normal centres, apply this argument, and use G331's full-fibre D descent. Under CE (p(f) in C for every finite continuous f), applying p to the downward-directed finite continuous nonpositive majorants of min(phi,0) gives the greatest D minorant for every bounded-above extended upper semicontinuous phi. The same construction and decreasing closure prove decreasing-obstacle-net stability with specified upper semicontinuous limit.

The exact Jensen reduction is also independently valid. Put
\[
\mathcal J_x=\{\mu\ge0:\mu(X)\le1,\ h(x)\le\int h\,d\mu\text{ for all }h\in C\}.
\]
These are nonempty compact convex sets with closed graph. For t>p(f)(x), separate (f,t) from the closed convex cone which is the closure of {(g,s): some h in C satisfies h<=g, s<=h(x)} in C(X) times R. Nonexpansivity proves the point is outside this closure. The separating functional has form mu(g)-alpha s, with mu positive and alpha>=0. The pairs (-a,-a) force alpha>0: otherwise positivity gives mu(X)=0 and the functional vanishes. Normalize alpha=1. Testing (h,h(x)) gives the Jensen inequalities; h=-1 gives mass<=1. Separation gives integral f<t. Weak compactness therefore proves
\[
p(f)(x)=\min_{\mu\in\mathcal J_x}\int f\,d\mu.
\]
CE is equivalent to weak lower hemicontinuity of these particular sets. Sufficiency follows from the minimum theorem and their compact closed graph. For necessity, a failure of lower hemicontinuity gives a net x_i->x and finite continuous tests whose compact convex projected Jensen sets avoid a fixed ball about the projection of some mu in J_x. Closest-point separation gives unit separating vectors; take a convergent subnet. Uniform boundedness of all projected measures preserves half the positive gap for the limiting vector. The corresponding fixed linear combination of the tests has discontinuous p, a contradiction. Hahn--Banach, Riesz and weak compactness of the positive dual unit ball are the ordinary functional foundations used here. General lower hemicontinuity is not asserted.

G331 already proves completion of all extended-valued semivaluations, exact primary jets and actual C/D cones. Thus 391's completion argument is a reconstruction of an existing result, with envelope, upper-regularization, gauge and Jensen transport as corollaries. It is not a new algebraization theorem or an equivalence of model categories. The change of primary gauge is the homogeneous formula u_b(v/v(b))=u_a(v)/v(b); bounded positive denominators preserve uniform and actual decreasing convergence, so envelopes transform by the same formula.

Whole391's five actual FINAL notes and five different expanded notes are retained separately. Its complete proof, independent review, ledger, scope and coverage, and the entire 386 mathematical appendix were examined as data. The full standalone TeX is checked against these proof bodies and the entire literal grants, rather than treating repeated appendices as new independent source readings. The full amended 22408-byte ROOT392 was examined, including regular-subring completeness, trace/idempotent lifting, adjugates, completed tensor exactness, full Hom factorization, S reduction and its conditional product result. Its conditional BIG gate is not assumed below. The source-ledger reading and encoding boundaries are stated in whole-reading-ledger.md and reports/whole-content-audit.json; identity checks establish retention, not correctness.

The review preserves the following negative conclusions. A single discriminant may vanish on a regular puncture and have infinite value on a nonzero support. The diagonal uses the full rooted kernel, not the ordinary extension of the diagonal ideal. An unrestricted imperfect-field extension does not give perfect-coefficient Frobenius descent. Multiplying a full test ideal by a Jacobian does not itself prove diagonal stability. A nonnormal double plane and increasing energy spikes are not normal continuous-obstacle counterexamples. The normal raw envelope is either zero or uniformly negative: if f is negative somewhere, divisorial density supplies nu with f(nu)<0 and G331's inequality g(nu)>=A_nu g(v) gives p(f)(v)<=f(nu)/A_nu for every v. This excludes the mixed-zero normal shortcut without proving general CE.

Artifacts: n1.md, whole-proof.md, whole-reading-ledger.md, reports/whole-content-audit.json. Rerun: python audit_inputs.py; python audit_whole.py; python build_delivery.py; python check_delivery.py. These are fresh local readers/builders, and no supplied program is imported or executed. Source is uncompiled.

# n2. Actual completed modules and uniform Noether-different lifts

Let R be a complete normal local domain of characteristic p>0 with perfect residue coefficient field k. Put S=R completed-tensor_k R, mu:S->R, and I=ker(mu). For q=p^e use root modules T=R^(1/q) and S^(1/q), equivalently the Frobenius-pushforward modules. Roots are abstract Frobenius-root rings when a reduced ring has several components; normality of S is never assumed.

A coefficient presentation R=k[[u]]/(f) gives S=k[[u,v]]/(f(u),f(v)), a Noetherian complete local ring. Exponent grouping modulo q and perfect coefficient roots make R and S F-finite. The same presentations identify S^(1/q)=T completed-tensor_k T, with the usual cofinal adic/root-adic topologies. Here and below compatibility means carrying I^(1/q), the entire kernel of root multiplication, into I.

We spell out completed tensor exactness. Finite modules over R are inverse limits of finite-dimensional k-vector spaces with their adic topology. Their continuous k dual V^o is the direct limit of the dual finite quotients, and V=(V^o)^*. Artin--Rees makes a finite submodule's induced topology equivalent to its adic topology; continuous functionals extend through finite quotients. Thus continuous duality is exact on finite-module sequences. Since tensor over k is exact and algebraic dual is exact on vector spaces,
\[
V\widehat\otimes_k W=(V^o\otimes_k W^o)^*
\]
is exact in either argument. This proves the needed kernel identifications; it does not invoke exact completion over the potentially non-Noetherian uncompleted tensor ring. Applying exactness to R->R^(1/p) in each factor shows S->S^(1/p) injective. Under the root identification this is Frobenius injectivity, so S is reduced.

Finite presentations now give the full Hom identity
\[
\operatorname{Hom}_S(M\widehat\otimes_k N,S)
=\operatorname{Hom}_R(M,R)\widehat\otimes_k\operatorname{Hom}_R(N,R)
\]
for finite R modules M,N. To check it, present M and N by finite free modules. In S^(ab) impose the M relation matrix first; completed exactness identifies that kernel with Hom_R(M,R) completed-tensor R^b. Impose the N matrix and apply exactness again. This is precisely the simultaneous kernel defining the left side. In particular finite paired generators generate every S Cartier map. The identity applies to ideals and source twists, not only free modules.

The broader regular-subring claim in amended ROOT392 is also valid. If A is any regular Noetherian subring over which R is finite, lying over and locality of R make A local. The n-adic and m-adic topologies on finite R are cofinal. Exact Noetherian completion of A subset R embeds A-hat in R, so A-hat is finite over A. Its quotient by A is finite and has zero residue quotient; Nakayama gives A=A-hat. Its residue field F embeds in k with finite extension. Since k is perfect and finite over F, comparison of [k:F] and [k^p:F^p] gives F=F^p. Cohen's regular complete presentation then gives A=F[[x]] and finite FREE A^(1/q). This proves the broad freeness statement without importing CM or R-flatness. The Jacobian sum used next is nevertheless restricted to the fixed common field k.

Fix a parameter normalization A=k[[x_1,...,x_d]] subset R, over which R is finite. Define K_A=Fitt_0 Omega_(R/A) and N_A=mu_A(Ann_(R tensor_A R) ker(mu_A)). Ordinary finite differentials suffice since R is a finite A algebra. If K_A is nonzero, its generic differential module vanishes, so L=Frac(R) is separable over K=Frac(A). No CM or A-flatness follows or is needed.

There is a direct inclusion K_A subset N_A. Write a finite polynomial A-algebra presentation R=A[z_1,...,z_n]/(g_1,...,g_r). In R tensor_A R the diagonal ideal is generated by t_i=z_i tensor1-1tensor z_i. Write g_j(z tensor1)-g_j(1tensor z)=sum a_ji t_i. The adjugate of any square n-row submatrix shows its determinant annihilates every t_i. Multiplication mu_A sends this determinant to the corresponding Jacobian minor. Thus each generator of K_A belongs to N_A. Noetherianity supplies the finite presentation and finite diagonal generation explicitly.

For every d in N_A and every q,
\[
dR^{1/q}\subset A^{1/q}[R].
\]
Indeed choose z=sum r_i tensor s_i annihilating the diagonal with mu_A(z)=d. Over L tensor_K L, separability makes z equal d times the separability idempotent. Applying the trace in the second factor proves d w=sum r_i Tr(s_i w). Purely inseparable K^(1/q)/K is linearly disjoint from L/K and L K^(1/q)=L^(1/q), so the same identity holds there. If w is integral over A^(1/q), the traces are integral and lie in its fraction field; normality of A^(1/q) puts them in A^(1/q). This gives the inclusion. The free exponent basis of A^(1/q) makes P=A^(1/q) tensor_A R a finite FREE R module. Its multiplication map into L^(1/q) is injective because its generic map is an isomorphism and it is A-torsion-free. Its image is A^(1/q)[R]. This freeness does not assert that R is free over A.

For phi:T->R, let B=R completed-tensor_k T. P completed-tensor_k T is free over B. Lift its multiplication to T along the surjection B->T, obtaining Psi:P completed-tensor T->B. Since d^q T subset P, compose multiplication by d^q in the first factor, Psi, and 1 tensor phi. This is an S-linear map T completed-tensor T->S and after mu it is phi(d^q z)=d phi(z). Hence it is compatible with the full root kernel and lifts the OUTPUT multiplier d phi. In F_* notation its SOURCE multiplier is d^q, not d. All maps are adically continuous on finite modules; the free lift is made on the completed modules themselves.

Let D_e be the quotient-restriction image of all such compatible S maps in C_e=Hom_R(F_*^e R,R). Composition and left/right R multiplications lift to S by choosing any lift of a scalar; compatibility with the full rooted kernel is preserved by composition. Thus D is an actual graded Cartier algebra, with finite degree pieces given by kernels and images of finite Hom modules. Summing the preceding lifts over finitely many normalizations proves
\[
J_{\rm norm} C_e\subset D_e\quad\hbox{for every e},\qquad
J_{\rm norm}=\sum_{A=k[[x]]}K_A.
\]
Wang 1994 Definition 4.1/4.2 and full Lemma 4.3 identify THIS fixed-coefficient-field sum with the formal Jacobian Fitt_d Omega_(R/k)^cont. We do not replace it with an unexamined sum over all regular finite subrings. Iyengar--Takahashi Example 3.3 is a corroborating statement, not the sole authentication of Wang.

Wang's generator choice does not require an infinite residue field. Maintain a prescribed basis of m/m^2 and choose its representatives successively. At a stage avoid the finitely many nonmaximal minimal primes of the ideals generated by subsets of at most d-1 earlier representatives. After discarding contained primes they are incomparable. For each P_i, m^2 is not contained in P_i; products give a_i in m^2 intersect all P_j (j!=i), but outside P_i. Add a_i exactly for those P_i containing the original representative. Its coset modulo m^2 is unchanged and it avoids every P_i. Catenarity and the height theorem preserve the dimension drop for every subset. Consequently every d-subset is a parameter system. The corresponding complementary Jacobian minors give Wang's finite sum. Formal substitutions preserving the cotangent basis are automorphisms, so their Jacobian change matrices are invertible. This verifies the finite-field qualification independently.

The formal Jacobian singular-locus criterion is applied at exactly reduced equidimensional complete equicharacteristic rings with perfect residue. Liu's published Corollary 4.9 and immediate proof state this criterion, with Wang 4.4/4.5 among its dependencies. Wang's actual printed pages 597--602, including the entire postponed proof of 4.5, were freshly viewed. The universal-finite/analytic historical dependencies cited inside that proof are disclosed ordinary published foundations, not claimed recursively reread. It follows that J_norm is nonzero and, for isolated R, contains an m-primary power.

Artifacts: n2.md, inputs/primary-LOCALONLY/Wang1994-official.pdf, page-11.png through page-16.png, Iyengar-Takahashi-jac3.txt, Liu-annihilator-published.txt. Rerun the fresh retention/audit with python audit_inputs.py and python audit_whole.py. No supplied program or PDF compiler is run.

# n3. Direct BIG all-map test ideals and arbitrarily late tails

Here is the precise framework used below. Let B be a reduced excellent Noetherian F-finite ring, C a graded Cartier subalgebra with C_0=B and finite degree pieces. Assume there is c in B^o (outside all minimal primes) such that B_c is regular, C_e localized at c is the full Cartier module for every e, and the finitely many pair ideals a_i contain regular elements and become unit ideals on B_c. Shrink by multiplying c by suitable regular elements if necessary. This hypothesis is verified for the full algebra and the actual diagonal algebra in n4. No finite generation of C as a graded algebra, gauge boundedness or finite-type-over-a-field hypothesis is assumed.

For real t_i>=0 put r_i(e)=ceil(t_i(p^e-1)). An ideal H is stable if every phi in C_e carries F_*^e((product a_i^r_i(e))H) into H. The twisted maps form a graded subalgebra: under composition the coefficient exponents are r_i(e)+p^e r_i(f), which are at least r_i(e+f). Source and output multiplication preserve the family.

First, every stable H meeting B^o has H_c=B_c. At a regular local localization of B_c, Kunz's theorem makes F_*^e B finite free. For a regular h in H choose q large enough that h is not in n^[q], using n^[q] subset n^q and Krull intersection. Then F_*h is primitive in the free module, so some Cartier map sends it to one. Hom localization holds by finite presentation. Stability gives the unit ideal at every maximal localization, proving H_c=B_c. The authentic applied Kunz statement is Smolkin v3 Theorem 2.3, quoting Kunz 1969; its original historical proof is ordinary background and not claimed freshly read.

There is a fixed power of c in EVERY such H. Choose one degree e_0>0. The same primitive-one argument on B_c gives a map splitting one. Clear its localization denominator to obtain theta in C_(e_0) with theta(F_*1)=c^a, a>=0. Choose B_0 so c^(q B_0) belongs to the required pair coefficient ideal for this degree. This is possible because those ideals become units after inverting c. If n is the least integer with c^n in H, stability and the Frobenius scalar rule applied to c^(q B_0+q ceil(n/q)) give
\[
c^{B_0+\lceil n/q\rceil+a}\in H,
\qquad n\le q(B_0+a+1)/(q-1).
\]
Take an integer L at least this bound. Then c^L lies in every stable generically nonzero ideal. Their intersection is stable and contains c^L in B^o. It is therefore the actual smallest such ideal, denoted tau(B,C,product a_i^t_i). Moreover the ideal generated by all twisted maps of any d in B^o, including degree zero, is stable and meets B^o. Hence this same c^L lies in that ideal for every d: it is a genuine universal BIG test element in the sense used in the trace formulas. This is the BIG all-map ideal, with generically nonzero convention on reduced rings, not the finitistic ideal. Existence was proved, not inferred from a name for an arbitrary Cartier algebra.

If d=c^L (or any sufficiently larger power), then for EVERY E>=0
\[
\tau=\sum_{e\ge E,\ \phi\in C_e}
\phi\big(F_*^e((\prod a_i^{r_i(e)})dB)\big).
\]
The sum is stable by composition; multiplying an output coefficient is absorbed by its Frobenius power in the inner source. At every minimal prime its localization is the full field, since c,d and all pair ideals are units and the algebra is full. Prime avoidance thus makes the sum meet B^o. Minimality gives tau subset the sum, and d in tau plus stability gives the reverse. The same proof works for ANY d in tau intersect B^o, in particular nonzero regular multiples of a common seed: only those two properties of d were used. Every arbitrarily late tail works. No claim that a single degree generates the ideal is made. Noetherianity only allows any one such sum to be replaced by a finite sum, possibly of different degrees.

The convention with r'_i(e)=ceil(t_i p^e) has the SAME smallest stable ideal. Run the preceding existence proof for these exponents also; they obey the same composition inequality. Choose a sufficiently large power d common to both ideals. For each i, 0<=r'_i-r_i<=ceil(t_i). Choose a regular z in product a_i^ceil(t_i). The q-1 tail with seed dz lies in the q tail with seed d, because z times its coefficient ideal lies in the latter one. The q-1 tail is tau for that convention, while the q tail lies in the q-convention ideal. Conversely the q-stable ideal is contained in the q-1-stable one by minimality, since any q-1-stable ideal is q-stable. Thus equality holds. The q trace-tail formula also holds with this common d. This addresses the actual convention in CEMS Definition 2.2, rather than silently interchanging two roundings.

Localization at multiplicative subsets of B^o is exact. The localized ideal is stable and meets the localized regular elements, so the localized minimum lies inside it. Conversely the contraction of that minimum is stable and meets B^o: all minimal primes survive, and one numerator of a regular localized element avoids them. The contraction therefore contains the original minimum. These two inclusions prove equality. For normal domains this applies to every ordinary localization. Finite-presentation Hom localization verifies the maps and powers used here.

The uniform comparison needed later is stronger than a stability guess. Suppose J C_e subset D_e for every e and both algebras satisfy this framework with the same regular c. Choose a universal seed d in BOTH minima. Express tau_C by its arbitrary-late tail. For j in J, j phi is a D map, and all its source coefficients and d lie in the D-stable ideal. Therefore
\[
J\tau_C\subset\tau_D.
\]
This argument does not assert that J tau_C is D-stable.

For full Cartier algebras on excellent F-finite local normal domains, completion commutes with these ideals. The finite module F_*^e A completes to F_*^e(A-hat): the filtrations defined by powers of n and Frobenius powers are cofinal. Hom then commutes with the faithfully flat completion. Extending tau_A is stable, giving tau_hat subset tau_A A-hat. Choose c in A on a regular open set where the pairs are units; excellence makes A-hat_c regular as well (regular formal fibres). The same cleared splitting theta from A works after completion and supplies a common c^L in tau_hat. Its contraction is thus nonzero and stable, giving the reverse inclusion. This proves completion compatibility without assuming that an arbitrary nonzero formal ideal has nonzero contraction.

Artifacts: n3.md and whole-proof.md. The integer bounds and rounding identities have finite diagnostics in finite_checks.py and reports/finite-checks.json. Rerun: python finite_checks.py. Those checks cover only their recorded finite domains; the universal proof is the preceding argument.

# n4. BIG completed-diagonal restriction and subadditivity

Use n2's actual S, I and diagonal algebra D. All hypotheses in n3 are now verified; none is supplied by a finite-type diagonal theorem. Let a,b be nonzero ideals of R and t,s>=0. On S put A=a in the first factor and B=b in the second factor.

First S is equidimensional of dimension 2d. Choose a parameter subring A_0=k[[x_1,...,x_d]] over which R is finite. A generic basis with cleared denominators embeds R in a finite free A_0 module. Completed tensor exactness from n2 embeds S in a finite free module over A_0 completed-tensor A_0=k[[x,y]]. Also S is finite over this ring. Every nonzero element of the latter is therefore S-regular. Since S is reduced, its minimal primes are associated, and all contract to zero. Each component is finite dominant over k[[x,y]], so has dimension 2d. This proof uses no S-normality, R-flatness over A_0, or CM.

Write R=k[[u_1,...,u_n]]/(f) and c=n-d. Choose a nonzero c by c formal Jacobian minor j of R. In S's two-block presentation the block diagonal minor j(u)j(v) is a 2c by 2c minor. The formal singular-locus criterion, at the exact equidimensional complete perfect-residue hypotheses checked in n2, makes S regular wherever this minor is invertible. At the diagonal prime P=I its image is j^2!=0. Thus S_P is regular. This proves regularity at the GENERIC diagonal directly, including any residue-field inseparability there.

Choose nonzero a_0 in a, b_0 in b and set
\[
c_S=j(u)j(v)(a_0\otimes b_0).
\]
Multiplication by a nonzero element of R in either tensor factor is injective by completed exactness. Consequently c_S is in S^o, mu(c_S)=j^2 a_0 b_0!=0, S_(c_S) is regular and both pair ideals are units there. The full algebra on S satisfies n3 and its BIG ideal T_S contains c_S^L for some L. In particular mu(T_S) is a nonzero ideal of R. A nonzerodivisor was not assumed to survive the diagonal quotient; its specific nonzero image has been exhibited.

The diagonal algebra D is full after inverting j: n2 gives J_norm C_e subset D_e and j is in J_norm. Thus the full R algebra and D satisfy n3 with a common nonzero c divisible by j a_0 b_0. They are generically nondegenerate; all source/output multiplications and compositions are actual compatible lifts. Using a common universal seed in both BIG ideals gives
\[
J_{\rm norm}\tau_R(a^t b^s)\subset\tau(R,D,a^t b^s).
\]

The image mu(T_S) is stable under the D pair maps. Indeed every D map has an actual compatible S lift. Each generator of a^ceil(t(q-1)) b^ceil(s(q-1)) lifts to the corresponding source power of A and B in their separate factors. For h in mu(T_S), lift h to T_S, apply the lift with these source coefficients, and reduce by mu. Compatibility with the full rooted kernel identifies this with the desired R map. S stability proves R stability. Since the image is nonzero, minimality, rather than a possibly zero restriction ideal, proves
\[
\tau(R,D,a^t b^s)\subset\mu(T_S).
\]

For the last inclusion let U=tau_R(a^t), V=tau_R(b^s). The completed tensor U completed-tensor V injects into S and is the ideal generated by its finitely many paired ideal generators. It contains a regular element u tensor v for nonzero u in U, v in V. N2's FULL Hom factorization expresses every Cartier map of S as a finite S-linear sum of paired R maps. Such a paired map carries F_*(A^r B^w (U completed-tensor V)) into the same ideal, by the two BIG stability conditions. The verification on pure tensors extends to completions: finite module maps are continuous and this finite generated ideal is adically closed. Consequently this is a stable generically nonzero S ideal, and n3's minimality gives T_S subset U completed-tensor V. Its diagonal image is precisely UV, by its finite paired generators. We obtain the entire chain
\[
J_{\rm norm}\tau_R(a^t b^s)
\subset\tau(R,D,a^t b^s)
\subset\mu\tau_S(A^t B^s)
\subset\tau_R(a^t)\tau_R(b^s).
\]
The same statement uses either q-1 or q rounding by n3. It is a BIG completed-diagonal theorem for every complete normal local characteristic-p ring with perfect residue coefficient field, without finite-type, CM, Q-Gorenstein or algebraizability assumptions. Generic separability is required only for the parameter normalizations with nonzero relative different and follows from that condition; it is not imposed on every finite normalization.

Iteration gives J_norm^(ell-1) tau_R(a^(ell t)) subset tau_R(a^t)^ell for every integer ell>=1. This is the correctly directed Jacobian correction. It does not claim uncorrected singular subadditivity.

Artifacts: n4.md, whole-proof.md, P12.3-formal-BIG-and-envelope.tex. Rerun: python build_delivery.py; python check_delivery.py. These perform consistency checks and create an uncompiled source; execution is not mathematical certification.

# n5. Passing the formal theorem to actual models and generating trace images

Let R be as in n4 and Y a normal integral projective birational model, equal to Spec(R) outside m. It is finite type over the F-finite excellent local base, but is not assumed finite type over k. The coherent module Omega_(Y/k) is nevertheless finite. In characteristic p over perfect k, every formal series in k[[u]] is uniquely a finite sum sum_(alpha<p) g_alpha^p u^alpha. Derivations kill the coefficients g_alpha^p, so ordinary differentials are generated by du_i, with the formal derivative relations. Thus ordinary and continuous differentials of R coincide. Finite-type presentations of Y over R now give a finite presentation for Omega_(Y/k).

For any F-finite reduced local k algebra A, completing this differential module commutes with completion. To see this without a continuity assumption on arbitrary derivations, k subset A^p, so Omega_(A/k)=Omega_(A/A^p). The ring A is finite over A^p. Completing the finite extension identifies the completed A^p with (A-hat)^p: this is the same Frobenius-module completion and cofinal filtration calculation in n3. Finite-algebra differential base change therefore gives Omega_(A/k) tensor A-hat=Omega_(A-hat/k).

Every closed point y of Y lies over m: a closed point's immersion into Y is proper, so its image is a closed singleton of Spec(R). Its residue is finite over k and hence perfect. The catenary dimension formula for a birational finite-type model gives dim(O_(Y,y))=d. Its completion is normal by excellence. A coefficient field compatible with k exists: the finite separable residue extension lifts in the complete local ring by the simple-root Hensel argument. Its differentials over k vanish. Hence
\[
\operatorname{Fitt}_d(\Omega_{Y/k})\,\widehat{O_{Y,y}}
=\operatorname{Jac}_{\rm formal}(\widehat{O_{Y,y}}).
\]
Apply n4 to this completion and use n3's full BIG completion equality. Faithfully flat descent proves, at y, the full test-ideal subadditivity corrected by J_Y=Fitt_d Omega_(Y/k). Coherent ideal inclusions on this finite-dimensional Noetherian Y can be checked at closed points: any nonzero coherent quotient has a closed point in its support. Thus
\[
J_Y\tau_Y(a^t b^s)\subset\tau_Y(a^t)\tau_Y(b^s)
\]
holds on the ACTUAL model. On its puncture J_Y is unit. Indeed it agrees there with the corresponding localized differential module of R; the formal Jacobian criterion for R gives Fitt_d=unit on its regular puncture. Its lower Fitting ideal vanishes by the domain's generic rank d, so this module is locally free of rank d. This also verifies the punctured Jacobian assertion without claiming that every regular ring over k is of finite type or smooth over k.

We use CEMS arXiv 1412.6453v4 at its actual Setting 2.1, Definition 2.2 and full Lemmas 2.3/2.4. The setting is Noetherian F-finite normal schemes with dualizing complexes and F^! omega-complex isomorphic to the omega-complex. It explicitly includes schemes essentially finite type over an F-finite local ring. Here R is a quotient of a regular complete power-series ring, giving a dualizing complex by finite duality; Y inherits one by projective duality. Thus these hypotheses hold. Its canonical sheaf on a normal integral model is the reflexive rank-one canonical module, irrespective of CM. We choose its rational section once. No anticanonical finite generation, CEMS 2.10 or finite-type-over-field global generation theorem is used.

For an effective integral exceptional Delta with L=K_Y+Delta Cartier, the applied trace statement is: for every nonzero coherent ideal b, real t>=0, sufficiently large effective Cartier test divisor D_0, and EVERY lower exponent cutoff E,
\[
\tau(Y,\Delta,b^t)=\sum_{e\ge E}
\operatorname{Im}\left[F_*^e(b^{\lceil p^e t\rceil}
 O(K_Y-p^e L-D_0))\xrightarrow{\operatorname{Tr}_e}O_Y\right].
\]
Its minimum is the BIG all-map ideal. The q versus q-1 and arbitrary-late-tail parts are also proved directly in n3 for full algebras and for divisor-restricted algebras, which are full after inverting Delta and a regular-locus element. The divisorial trace identification is the immediate CEMS application, via finite duality and normal height-one extension. Source twists are reflexive coherent sheaves; no canonical index bound is presumed. CEMS 2.4 supplies localization, monotonicity in Delta and Cartier shift; the shift follows directly by moving a local Cartier equation through the trace with its qth power. Power invariance tau(b^t)=tau((b^r)^(t/r)) follows from ceil(qt)<=r ceil(qt/r)<=ceil(qt)+r-1 and multiplying a common test seed by a regular element of b^r. Consequently graded asymptotic ideals stabilize through common multiples on a finite affine cover, by Noetherianity.

A global Cartier D_0 is legitimate. On a finite affine cover take local BIG test elements and the fixed rounding corrections, and dominate their divisors by an effective Weil divisor E_0. For a full-fibre negative ample bundle A, a high twist O(-E_0) A^r is generated. A nonzero section is a rational function whose divisor is at least E_0+rF when A=O(-F); in particular its principal effective Cartier divisor D_0 dominates E_0. Normal height-one regularity makes its local equation a regular multiple of every local seed. Larger seeds remain BIG test seeds by n3's tail argument. This glues the displayed formula with ONE global D_0. The divisor and the late threshold may depend on b,t; the ampleness integer used next will not.

Here is the relative generation theorem over the complete affine base. If A is ample and generated on finite-dimensional projective Y and M is coherent with H^i(M A^-i)=0 for all 1<=i<=dim(Y), then M is generated. The finitely many generating sections of A give a locally split exact Koszul complex (one local coordinate is a unit). Tensoring by M preserves exactness. Its higher syzygy sequences, with vanishings in degrees i,i+1,..., propagate H^i(M A^(t-i))=0 from t to t+1; groups beyond dim(Y) vanish. The same syzygies show multiplication of sections H^0(M A^t) onto H^0(M A^(t+1)) for t>=0. A high twist is generated by Serre; repeated multiplication implies M itself is generated. This proof assumes no base flatness, finite type over a field or CM.

In particular choose c_0 once such that (c_0-i)H-L is ample for every required i, where H=-F. For any FIXED finite coherent list M_j, the sheaves
\[
Q_{e,j}=F_*^e(M_j\otimes O(p^e(c_0H-L)))
\]
are generated for all sufficiently late e, uniformly over that finite list. Projection formula turns their regularity vanishings into Serre vanishings for the ample bundles (c_0-i)H-L. Finite Frobenius makes Q coherent. Every trace tail may be cut off this late. Finite stabilization of its image sum can involve DIFFERENT e, which suffices for target generation.

Artifacts: n5.md; inputs/primary-LOCALONLY/CEMS-anticanonical-1412.6453v4.txt; whole-source-application-ledger.md. Complete CEMS Setting 2.1, Definition 2.2, Lemma 2.3 and Lemma 2.4 with its proof ending were read. The source's recursively cited duality and historical divisor/test-ideal foundations are ordinary published dependencies, not falsely claimed fully reread. Rerun: python audit_whole.py; python build_delivery.py.

# n6. Complete isolated formal continuous-envelope theorem

Assume R is a complete excellent normal local domain of characteristic p>0 with perfect residue k, regular away from m. For d>=2 we prove CE on the FULL primary link for G331's independently geometric C/D, with an all-support uniform estimate. Neither algebraizability, finite type over k, CM, a canonical index bound nor resolution is assumed. For d=1 the normal ring is a DVR and its link is a singleton; d=0 has empty boundary.

Principalize any finite primary collection, including the gauge a, by blowing up its product and normalizing. Factors are invertible because an invertible product of ideals in a local domain gives an inverse fractional ideal, and a unit product in a local expression of one gives a generator. The resulting full-fibre Cartier F_0 has negative ample bundle. Use the coherent reflexive DIVISORIAL canonical sheaf omega obtained from the dualizing complex at codimension one and extended reflexively; it is rank one, including the non-CM case. No dualizing complex is replaced by a locally free canonical module. Blow up Fitt_1(omega). On an a-chart of this blowup, the strict transform is the pulled-back module modulo a-power torsion. Stacks 15.27.3 gives Fitt_1=unit; its generic rank one and the chart's injection into its localization give Fitt_0=0. The finite locally free Fitting criterion gives an invertible module. This is also precisely 15.27.4, whose immediate proof and inputs were read. Normalize once more and pull back this invertible module.

On this final normal model choose the SAME rational canonical section for its canonical divisor K_Y and the invertible divisor L_0 just obtained. Their difference is exceptional because both agree on the unchanged regular puncture. Choose r so Delta=rF_0-(K_Y-L_0)>=0. Then Delta is integral effective exceptional and L=K_Y+Delta=L_0+rF_0 is Cartier. The negative Fitting exceptional bundle, times a sufficiently high pullback power of O(-F_0), is ample over Spec(R); finite normalization preserves ampleness. A high power is very ample and generated. Write it A=O(-F), with F effective and supported on the ENTIRE closed fibre.

This model is an ACTUAL primary blowup. Put J=Gamma(Y,A). Every section is regular on the puncture and hence in R by normal Hartogs (d>=2). Proper coherent finiteness makes J finite; A generation gives J O_Y=A; it is unit off m and proper because every section vanishes on the nonempty closed fibre. Hence J is primary. Choose very ample generating sections and add the other ideal generators. They embed Y in the projective space associated to J. Off m this image is the graph defined by J. The blowup of J and this integral closed image are both the scheme-theoretic closure of the same dense punctured graph, so Y=Bl_J R. This verifies G331's actual primary-model scope, rather than claiming cofinality of arbitrary birational models. All specified factors remain invertible.

By n5 the coherent J_Y=Fitt_d Omega_(Y/k) is unit on the puncture and obeys actual BIG subadditivity. Fix a,b,N_J with
\[
J^a O_Y\subset J_Y,\qquad \Delta\le bF,
\qquad \mathfrak a^{N_J}\subset J.
\]
These constants exist by finite coherent support on the closed fibre and its full Cartier order unit. In particular v(J_Y)<=a v(J)<=aN_J on EVERY semivaluation support. This is a primary correction, not a discriminant finite only on selected valuations.

Let C_0 be any integral exceptional Cartier obstacle on Y. Its evaluation f=f_(C_0) is finite continuous on the full link by G331's actual lattice evaluation and Cartier order-unit argument. For ALL m>=1 put
\[
I_m=\Gamma(Y,O(mC_0)),\qquad
\mathfrak b_m=I_m O_Y O(-mC_0),\qquad u_m=-v(I_m)/m.
\]
Hartogs puts I_m in R. A fixed actual bound C_0>=-M F_a implies a^(Mm) subset I_m. Thus every I_m is unit or primary, at every index. Products give gradedness. At every valued centre (first passing to the support quotient field) evaluation gives u_m=f-v(b_m)/m<=f. Values are finite, because the ideals contain a closed-fibre primary power. The sequence v(I_m) is subadditive; the all-index Fekete argument, writing an index as qr+s with bounded finitely many remainders, gives lim_m u_m=sup_m u_m.

This supremum is the RAW envelope, before continuity recognition. If -v(I)/q<=f is a rational primary competitor, testing at the exceptional height-one primes of the NORMAL Y gives ord_E(I)+q(C_0)_E>=0. Other height-one points lie off the exceptional divisor and sections of I are regular. The normal height-one section criterion therefore gives I^r subset I_(rq) for every r. Consequently the rational competitor is below sup_m u_m. Rational density with negative shifts treats C competitors, and n1 treats D competitors. Therefore p(f)=lim_m u_m on all supports. Set h=f-p(f)>=0 without claiming that p(f) is already psh.

Define the coherent stabilized asymptotic ideals
\[
t_m=\tau(Y,\Delta,\mathfrak b_\bullet^m),\qquad
s_m=\tau(Y,\mathfrak b_\bullet^m).
\]
Gradedness, power invariance and common multiples in n5 give their actual stabilization. The full model subadditivity proves
\[
J_Y^{\ell-1}s_{m\ell}\subset s_m^\ell.
\]
To justify the common index, choose a common multiple attaining both asymptotic ideals and apply the iterated ordinary ideal inclusion at that index. No asymptotic formalism is accepted on a label alone.

Choose c_0 ONCE so that (c_0-i)H-L is ample for 1<=i<=dim(Y), H=-F. For fixed m choose ell attaining t_m and a global Cartier test divisor D_0 as in n5. For EVERY exponent cutoff E the trace expression for t_m uses q=p^e and a_e=ceil(qm/ell). Set j_e=ell a_e-qm, so 0<=j_e<ell. Products of the actual global generators of I_ell generate b_ell^a_e O(ell a_e C_0). After twisting the trace target by O(mC_0+c_0H), its source is a quotient of finitely many copies of
\[
Q_{e,j}=F_*^e O(q(c_0H-L)+K_Y-D_0-j C_0),\qquad 0\le j<\ell.
\]
The maps multiply these section products INSIDE Frobenius. They are linear for its scalar action; coefficients are not extracted as ordinary scalars. The finitely many reflexive sheaves O(K_Y-D_0-j C_0) are coherent without any Q-Gorenstein or CM hypothesis. N5 generates every sufficiently late Q_(e,j). The arbitrary-late trace formula then generates t_m O(mC_0+c_0H). Coherent finite image stabilization permits different late exponents. Only the finite list, test divisor and threshold depend on m,ell; c_0 does not.

Put c=c_0+1 and F_m=t_m O(mC_0) A^c. It is generated. Its sections are in R by punctured Hartogs. Before the extra A twist, generation by R sections makes the fractional sheaf a subsheaf of O_Y; afterwards F_m subset J O_Y. Let J_m=Gamma(Y,F_m). Then J_m O_Y=F_m and J_m is proper.

The ideal T_0=tau(Y,Delta) is unit on the regular puncture and contains J^r O_Y for some fixed r. One has b_m T_0 subset t_m: compute T_0 with a seed common to the Delta and (Delta,b_m) ideals; for f in b_m move it through each Cartier map as f phi(F_*z)=phi(F_*(f^q z)), using b_m^q inside the q-rounded trace. This proves b_m T_0 subset tau(Y,Delta,b_m^1), which is contained in t_m by its index m. Thus
\[
I_m J^{r+c}\subset J_m.
\]
Every J_m is therefore genuinely m-primary for ALL m, not merely eventually. Its primary profile belongs to the independently geometric cone by G331:
\[
g_m=-v(J_m)/m=f-(c v(J)+v(t_m))/m\le f.
\]

Also b_(m ell) T_0 subset t_(m ell) subset s_(m ell). Evaluate the correctly directed asymptotic subadditivity to obtain
\[
\frac{v(s_m)}m\le
\frac{v(\mathfrak b_{m\ell})+v(T_0)}{m\ell}
+\frac{\ell-1}{m\ell}v(J_Y).
\]
All these values are finite at every support, since each ideal contains a closed-fibre primary power. FIRST let ell tend to infinity pointwise. Fekete along this subsequence gives v(s_m)<=m h+v(J_Y); the finite T_0 term disappears. Monotonicity in the boundary and Cartier shift, with Delta<=bF, give O(-bF)s_m subset t_m subset s_m. Substitution in the expression for g_m, using its already established competitor status, proves
\[
0\le p(f)-g_m\le
\frac{(c+b)v(J)+v(J_Y)}m
\le\frac{(c+a+b)N_J}{m}
\quad\hbox{on the ENTIRE link.}
\]
The final bound is uniform on all supports, including infinite function values of nonprimary elements. Hence p(f) is a uniform limit of actual primary geometric profiles and belongs to C.

Signed rational primary lattice functions are uniformly dense among continuous obstacles by G331. The formula min(v(I)-v(J),v(K)-v(H))=v(IH+KJ)-v(JH) and the primary truncations (f)+a^N give its separating lattice; every such obstacle is determined by a finite primary collection, principalized on the model above. Clear denominators, use the estimate, then use n1's nonexpansivity to pass to arbitrary finite continuous obstacles. This proves CE in the entire stated isolated formal class. N1 now gives actual greatest D envelopes for bounded-above extended upper semicontinuous obstacles, their appropriate upper semicontinuity, decreasing-obstacle-net stability, and the exact primary-gauge cocycle.

Completion transport from G331 extends this theorem exactly to excellent normal local characteristic-p rings whose completions have perfect residue and are regular away from their maximal ideal. In particular these completion hypotheses hold for isolated excellent normal local rings with perfect residue: excellence gives normal completion and regular formal fibres; a prime over a nonmaximal regular prime is regular, and the fibre over m is just the residue field. No universal algebraization statement is made.

Artifacts: n6.md, whole-proof.md, P12.3-formal-BIG-and-envelope.tex, coverage.md. Rerun: python build_delivery.py; python finite_checks.py; python check_delivery.py. The source remains uncompiled. This is a complete nontrivial scoped mathematical draft, not a complete solution of the unchanged original P12.3.

# n7. Original residual, curve comparison and independent scoped decision

The new scoped theorem is complete as a relative mathematical draft: actual completed-diagonal BIG restriction/subadditivity (n2--n4), its coherent actual-model transfer and trace generation (n5), and the full isolated formal CE theorem with all-support O(1/m) primary approximants (n6). The only incoming correctness support is the entire qualified G331. B341 and E350 are retained in full with their qualifications but no bounded product or energy theorem from them is needed for this chain. Native/ROOT drafts and favorable verdicts were not used as premises. There is no claim of formal verification or publication.

For every excellent reduced curve the full link is the finite discrete set of normalization DVR centres. The independent negative Cartier point divisor on each DVR gives every nonpositive real branch slope; full-fibre positive G331 descent gives these functions downstairs. Actual truncations give extended nonpositive vectors. Consequently, for every branch obstacle,
\[
P_{\rm geom}(\phi)=P_{\rm ideal}(\phi)=\min(\phi,0).
\]
This is a geometric comparison, not a new cone defined by clipping. Branches are normalization centres, not just irreducible components. Primary gauges rescale by ord_q(a)/ord_q(b); all conductor fibres retain G331's exact finite-value singleton and infinite-value quotient rule. This valuative result does not identify literal classical/CLD disc radial extensions: the dossier's mixed-zero exclusion in its stated disc-normalized range remains unchanged.

On higher-dimensional nonnormal germs, full positive descent requires constancy on EVERY normalization fibre, including conductor-infinite ones. Even where the normal branches have CE, this compatibility is an actual condition on their envelopes. The double-plane obstruction can be verified directly: take R=k[[x,y,z]]/(xy), maximal-ideal gauge, and f=-1-1/v(y), with 1/infinity=0. On the normal x,z plane it is -1. On the y,z plane the ordinary maximal-ideal valuation has f=-2, and every C or D function satisfies g(v)<=g(ord_m), since v(I)>=ord_m(I) for every primary ideal and this inequality survives both completions. Thus competitors on that plane are at most -2. On the first plane the primary profiles of (x^n,xz^(n-1),z^(2n)), divided by -n, are at most -1 and equal -2 at the point killing x. Paired with the constant -2 on the second plane they are fibre-compatible and descend positively by G331. Their supremum is -1 off the identified point on the first plane and -2 on the second plane and the identified point. The valuations (v(x),v(z))=(L,1) tend to that point, proving raw discontinuity. The upper regularization is -1 there and -2 at the second plane's ordinary valuation, violating the displayed C/D inequality. It is not a positive envelope. This reconstructs the examined diagnostic, remains NONNORMAL, and does not contradict n6 or negate the unchanged 'when possible/appropriate regularity' target. The primary-model and all-support definitions have not been weakened to radial functions or to valuations with zero support.

Independent whole391 decision: its completion and envelope-transport argument is valid but reconstructs G331's already supplied completion, rather than adding an algebraization theorem. Its Jensen duality is valid as an exact reduction, without general lower hemicontinuity. Its discriminant lift is valid with generic separability, perfect coefficients and an actual common residue coefficient field for the completed product. Its isolated formal gate was genuinely unresolved there. Its scoped review of 386 is an unreviewed review, not an incoming grant. The complete 386 proof was examined; its finite-type isolated, surface, exact characteristic-zero/smooth, finite-cover, conductor and curve sectors remain precisely delimited and are not silently enlarged by our result. Historical source-reading receipts are not fresh source authentications. ROOT392 decision: the amended full root/different/completed-module lemmas are valid with the exact topology and finite-module qualifications independently supplied in n2; its BIG product assertion was conditional. That condition is now discharged by the common seed, genuine generic diagonal and actual restriction proof, rather than accepted from ROOT392.

The unchanged ORIGINAL P12.3 is still incomplete. This paper does not prove general normal CE in nonisolated dimension at least three, general mixed-characteristic higher-dimensional CE, imperfect-residue formal CE, or every excellent/nonalgebraic/nonclosed singular scope. General Jensen lower hemicontinuity remains unproved outside the established sectors. No actual NORMAL continuous signed primary/model obstacle violating the literal raw continuity/positivity criterion was found. Failure of one discriminant estimate, restricted radial constructions, arbitrary alterations, and increasing capacity/energy spikes do not constitute such counterexamples. P12.4 products, P12.5 energy and P12.6 full operator compatibility remain separate targets.

Deliverables are the complete standalone uncompiled TeX P12.3-formal-BIG-and-envelope.tex, whole-proof.md, n1.md through n7.md, whole-reading-ledger.md, whole-source-application-ledger.md, coverage.md, independent-scoped-verdict.md, original-residual.md, native-notes.json and separately different expanded-notes.json, plus fresh scripts, exact finite inputs/outputs, environment and integrity reports. The actual final fields are bound to their own JSON, never replaced by expanded text. Full private primary bodies, pixels and book context stay LOCALONLY; the paper states applied results and reading boundaries, rather than publishing private sources.

Observed execution evidence: all 1546 supplied manifest records match (312 mathematics, 1231 private-primary, three context). Independent encoding matches every full examined proof body and literal grant in the 686035-byte incoming TeX, leaving 2140 characters of separately read framing. The new seven actual and seven different expanded notes pass full-body/support consistency, with source uncompiled. Exact arithmetic passes 1056 composition cases and 2112 rounding/power cases for p=2,3,5, e,f=1..4, t=i/7 (i=0..21), power multiplier r=1..8; 890 seed-bound cases satisfying n<=a+ceil(n/q), for q=2,3,4,5,8,9,25, a=0..12, n=0..100; and 3582 source/output cases for q=2,3,4,5,8,9, d=0..5, basis=0..q-1, input power=0..3q-1. The q=3 diagnostic phi(x^2)=1 gives phi(x*x^2)=0 while x*phi(x^2)=x, exposing the wrong source multiplier. These are observations/exhaustive finite results ONLY on those domains; universal correctness rests on the proofs, not execution.

Rerun in this directory: python audit_inputs.py; python audit_whole.py; python finite_checks.py; python build_delivery.py; python check_delivery.py. No supplied/native program is executed or imported, no compiler is run, and no agents, additional model/native campaigns, network/auth/runtime/proxy/CA/editor/catalogue/publication actions occur. No supervised heavy-compute facility was supplied; none was needed. Finite diagnostics, hash matches and artifact generation establish only their recorded execution facts, not the universal mathematical claims. Original candidate=false.
