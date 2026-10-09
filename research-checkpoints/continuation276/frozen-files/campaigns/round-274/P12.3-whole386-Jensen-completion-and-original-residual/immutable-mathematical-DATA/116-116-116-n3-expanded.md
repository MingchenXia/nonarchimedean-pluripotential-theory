# n3. Characteristic-zero approximation, isolated CE and the exact open locus

Use qualified G331 and n1. Here R is a normal algebraic germ at a CLOSED point over an algebraically closed characteristic-zero field, dimension >=2. The source is the THREE-author Boucksom–de Fernex–Favre, Duke 161 (2012), not the four-author singular multiplier paper. Sections 1–3 apply to general normal varieties; isolation begins in Section 4. We checked the complete immediate Lemma 1.12, the full three-step 2.12 and 2.13, 2.15–2.17, 2.24–2.25, asymptotic 3.12–3.17 and integral 4.11. Their Hironaka, numerical and singular-multiplier/Takagi foundations remain disclosed published dependencies.

A core divisor is source-nef because its contracted-curve degrees are nonnegative. If g in C is a uniform limit of cores, its divisorial coefficients converge. On each model only finitely many exceptional divisors occur, and all base traces are zero because the marked point has codimension >=2. Source 1.12(a) with this FIXED zero trace converts coefficient convergence to numerical convergence; closedness gives a source-nef b-divisor H_g. Only this core/C -> source-nef direction is used. No source-nef -> D recognition is assumed, and no merely USC inequality is extended from a dense set.

For f=(v(A)-v(B))/N choose a normal common primary model Y determining A,B,a. The integral-denominator Cartier obstacle C=(Z(B)-Z(A))/N evaluates to f, with Z(I)=-ord(I). Let E_i be its exceptional primes, b_i=ord_Ei(a)>0 and nu_i=ord_Ei/b_i. Actual Cartier order bounds give MZ(a)<=C. Source 2.11–2.13 and 2.15–2.17 give the largest source-nef trace envelope W=Env_pi(C_Y), with MZ(a)<=W<=C and W<=0 by negativity at base trace zero. It is supported over the point. If W=0, divisorial continuity/density imply f>=0 on all supports, so p(f)=0.

For the isolated case and W!=0, CLEAR denominators first: C0=NC is integral Cartier and W0=NW. Source 4.11 forms graded coherent section ideals and asymptotic multiplier ideals b_k, obtaining Z(b_k)>=kW0+Z(d(K))+Z(Jac), and Z(b_k)/k->W0 coefficientwise. At an isolated singularity the two correction ideals are unit or primary, not necessarily strictly primary. Their combined divisor is >=c Z(m). Source 4.7–4.9 gives W0<=epsilon Z(m)<0. Thus Z(b_k)>=(k+c')W0; replacing c' by a larger positive integer is correct because W0 is negative. Set B_k=Z(b_k)/(N(k+c')). Then B_k>=W, B_k->W coefficientwise. Nonzero W forces b_k proper eventually; discard a finite unit prefix. Sections lie in R by normal codimension-two Hartogs, and contain a primary power, so the retained b_k are actual primary. The zero case uses the unit ideal.

Define eta_k=max_i ((B_k(E_i)-C(E_i))^+/b_i), which tends to zero. B_k+eta_k Z(a) is source-nef with trace <=C_Y, hence <=W by 2.13. Therefore B_k-eta_k<=W<=B_k on normalized divisors. The continuous primary profiles of B_k are uniformly Cauchy on these divisors, hence on the WHOLE section by G331 density; their uniform limit U belongs to C and U<=f. For an arbitrary D competitor h<=f and epsilon>0, select ONE term g of its actual C-net with g(nu_i)<=f(nu_i)+epsilon at every finite determining vertex. H_g+epsilon Z(a) has constrained trace, so g-epsilon<=W on divisors. Continuity and density give g-epsilon<=U everywhere; h<=g yields h<=U+epsilon. Consequently U=p(f). Density of signed obstacles and nonexpansivity establish CE for all finite continuous obstacles on isolated normal closed algebraic germs in this exact characteristic-zero setting.

We reconstruct the general nonisolated result without applying isolated 4.11. Let Q=d(K)Jac be the coherent nonzero ideal, O={v(Q)<infinity} OPEN, and K_L={v(Q)<=L} compact. Canonical Cartier shifts do not change d(K). The omitted closed stratum consists of supports containing Q.

Use the same C0,W0. Put a_m=pi_*O_Y(mC0). Proper coherence makes each a_m finite; codimension-one regularity away from the marked point and normal Hartogs put its sections in R. Actual Cartier order gives a^(M1 m) subset a_m for a fixed integer M1, so each is unit or primary and nonzero. The family is graded. We claim no finite generation of its graded algebra. By the definition and largest-trace characterization, Z(a_bullet)=W0.

General source 3.17, with b_k=J(a_bullet^k), gives

Z(b_k)>=kW0+Z(Jac)+Z(d_bullet(K)), and Z(b_k)/k->W0.

Multiplication of the divisor sheaves gives d(K)^m subset d(mK); hence Z(d_bullet(K))>=Z(d(K)). Thus Z(b_k)>=kW0+Z(Q). These multiplier ideals may be NONPRIMARY. Choose integers A0>M0 with W0>=M0 Z(a), and set b'_k=b_k+a^(A0 k), U_k=Z(b'_k)/(Nk). They are actual unit-or-primary ideals. Ideal addition takes the maximum of the two negative divisors. Its second term is strictly below the coefficient limit W0 at each centred divisor, so U_k->W coefficientwise, while still U_k>=W+Z(Q)/(Nk).

The finite trace errors eta_k=max_i ((U_k(E_i)-C(E_i))^+/b_i) tend to zero. Source largest-trace negativity gives U_k+eta_k Z(a)<=W. Continuous ideal profiles u_k therefore satisfy on normalized divisors

W-v(Q)/(Nk)<=u_k<=W+eta_k.

The functions g_k=u_k-eta_k lie in C and below f on ALL of X: this last continuous inequality extends by full divisorial density. They are genuine global competitors. Subtracting the two estimates for k,l gives

u_k-u_l<=eta_k+v(Q)/(Nl), and u_l-u_k<=eta_l+v(Q)/(Nk).

FIRST extend these continuous inequalities on the OPEN finite-Q locus O by density there. Only afterwards restrict to closed K_L; divisorial density within K_L is not presumed. They give a uniform Cauchy sequence on each K_L and on every neighbourhood {v(Q)<L}. Its limit U is continuous on O, agrees with W on divisors, and

0<=U-g_k<=eta_k+v(Q)/(Nk) on O.

Hence U<=p(f) there. Conversely for EVERY D competitor choose ONE continuous term at the finitely many vertices as above. Source comparison gives g-epsilon<=W=U on divisors. Continuity on O extends it to all its support points, and h<=g gives h<=U+epsilon. Thus p(f)=U on O. Signed-profile approximation and global nonexpansivity extend this to every finite continuous f. Because O is open, p*=p there as well. If Q is unit or primary this is global CE. Otherwise no continuity or positivity on {v(Q)=infinity} has been proved.

The correction criterion is exact. For every nonzero ideal I on an excellent normal positive-dimensional local domain, v(I) is uniformly bounded on ALL points, equivalently on ALL centred divisors, iff I is unit or primary. The forward primary direction follows from a^N subset I. For a proper nonprimary I choose I subset p<m. The positive-dimensional excellent quotient R/p has a normalized boundary point, whose pullback kills I. Each nonempty open set {v(I)>L} then contains a centred divisor by G331 density, proving unboundedness even on divisors. A finite chosen list of divisors always gives a finite maximum and cannot replace this global bound.

The normal threefold k[x,y,z,t]/(xy-z^2) at its origin illustrates the correction failure in EVERY characteristic. It is a hypersurface domain, S2 and regular in codimension one, hence normal. Its Jacobian ideal (x,y,2z) has radical (x,y,z), with quotient k[t]. The t-order support valuation has the other coordinates infinite. The canonical defect is unit because the hypersurface is Gorenstein. Thus Q is nonprimary and has unbounded values. A failed correction estimate alone is NOT a normal CE counterexample; an independent actual-cover CE proof in characteristic zero is given later in n5. No capacity, source-USC spike or truncation of Q supplies the missing global UPPER approximation.

Artifacts: n3.md, whole-proof.md and the LOCALONLY full-literal source ledger. Rerun: python extract_literal.py; python build_delivery.py; python final_audit.py. Source application and the new arguments, not execution success, support the conclusions.
