# A common minimum datum for the specified zero-volume energy and operator families

Root-authored new mathematical draft, 4 October 2026. This is a local bridge between the exact R31 and R32 constructions, not an original-scope acceptance or an independent review. Both originals remain open. No external submission has been made. The earlier blocked original-scope audit, its argument and its pending approval are unchanged.

## Exact inputs and hypotheses

Let X be a connected smooth compact Kähler n-fold, alpha a pseudoeffective class with vol(alpha)=0, theta a smooth real representative, and psi an actual theta-psh function not identically minus infinity. Put P=theta+dd^c psi. Retain the actual two-sided bounded singularity type C_psi, rather than ideal equivalence alone. Let d<n be the largest integer with a nonzero actual nonpluripolar product <P^d>, and m=n-d. The empty product is 1.

Use the exact common relative full-mass domain H_psi and common joint linear finite-energy domain F^1_psi established in R31/R32. For one, hence every, Kähler form Omega, they are

H_psi = {u theta-psh: u<=psi+C and int <T_u^d> Omega^m = int <P^d> Omega^m},

F^1_psi = {u in H_psi: sum_(a=0)^d binom(d,a) int |u-psi| <T_u^a P^(d-a)> Omega^m < infinity}.

For d=0 use the empty product and ordinary smooth-volume integrability. The direct formulas, common-domain proofs, mixed full-mass identities, bounded and unbounded cocycle proofs, bare-current decreasing convergence, coefficientwise extension and exact minimum-reference equivalences are in the complete frozen author arguments:

* R31: /workspace/research/campaigns/round-31/P15.1-minimum-reference-finite-energy/artifacts/codex-7YBaVo/P15.1-argument.md.
* R32: /workspace/research/campaigns/round-32/P15.2-minimum-reference-full-mass-operator/artifacts/codex-UNkbGs/P15.2-argument.md.

Those are generated mathematical sources, not published literature. Their scoped PASS reviews are separate evidence, not mathematical premises. The root has read and reconstructed their complete proofs and source applications. This bridge assumes precisely the stated constructions and uses their proved identities; it does not substitute a review verdict for them. The binding accompanying this note records the exact source hashes.

Set V=H^(1,1)(X,R), B=Sym^m V. R31 constructs the finite-dimensional energy quotient Q_E=B/K_E, with quotient q_E, where

K_E = intersection_(u in C_psi) ker(ell_u^psi).

The same kernel is obtained on F^1_psi, and for every Kähler omega,

ell_u^psi([omega]^odot m) = E_(psi,[omega])(u)
 = (1/(d+1)) sum_(a=0)^d int (u-psi) <T_u^a P^(d-a)> omega^m.

R32 instead uses the actual form space

W=span_R{omega^m: omega a smooth Kähler form on X},

L_u(eta)=<T_u^d> wedge eta,
N_M=intersection_(u in C_psi) ker L_u,
Q_M=W/N_M, with quotient q_M.

The same N_M is the intersection on H_psi and on F^1_psi. Its factorwise description is indispensable: eta belongs to N_M if and only if every mixed degree-d nonpluripolar product from H_psi wedges with eta to the zero signed measure. This is R32 equation (Q2), proved by positive-cone polynomial coefficient extraction and then mixed decreasing-current convergence. For d=0 N_M={0}.

## The bridge theorem

There is a canonical surjective linear map pi:Q_M -> Q_E with

pi(q_M(omega^m))=q_E([omega]^odot m)

for every smooth Kähler omega. Consequently the whole measure-family datum suffices for the anchored energy family as well. It is the coarsest sufficient datum for this specified pair of families on the admissible Kähler powers. Raw mass is preserved. The map pi is continuous for R32's quotient C^0 norm and Q_E's finite-dimensional topology. It need not be injective; in the P^1 x P^1 example its kernel is infinite-dimensional.

This theorem does not say that every possible zero-volume theory must use these same families, that Q_M is a geometric carrier, that d is numerical dimension, or that all perturbation paths converge. Those conclusions are outside the statement.

### Step 1: the actual-form energy map is well-defined

For eta in W and u in F^1_psi define

A_u(eta)=(1/(d+1)) sum_(a=0)^d int (u-psi) <T_u^a P^(d-a)> wedge eta.

This is a finite real number. In a finite chart cover, coefficient measures of a positive (d,d) current are controlled by its Kähler trace measure. Multiplication by a smooth complementary form therefore gives

|A_u(eta)| <= C_u ||eta||_(C^0),

where C_u is finite: each weighted trace integral in its bound is one of the finitely many F^1 integrals above. This also proves absolute integrability of the signed weighted measures. Differences on the common polar sets are assigned arbitrarily, because all relevant trace measures give those sets zero mass. Thus A_u is a linear map on the actual form eta, independent of any presentation of eta as a sum of powers.

If eta=sum_i a_i omega_i^m, define tentatively

c(eta)=sum_i a_i q_E([omega_i]^odot m).

Suppose a second presentation is used. The difference is a zero smooth form, so its A_u value is zero for every u in C_psi. By the exact R31 energy formula this means that the corresponding difference of tensors is annihilated by every bounded-type ell_u. It lies in K_E. The two proposed values in Q_E are therefore equal. This proves c:W -> Q_E is well-defined and linear. It also proves

A_u(eta)=bar-ell_u^psi(c(eta))

for every u in F^1_psi, using R31's extension of the energy kernel to the entire domain.

The powers [omega]^odot m span B: a homogeneous polynomial annihilating those powers vanishes on the open Kähler cone and hence is identically zero. This is the complete polynomial spanning proof in R31. Therefore c is surjective onto Q_E.

### Step 2: the operator kernel is contained in the energy kernel

Let eta belong to N_M. For d>=1, R32 (Q2), with a copies of T_u and d-a copies of P, gives

<T_u^a P^(d-a)> wedge eta=0

as a signed measure for every 0<=a<=d and every u in F^1_psi. Multiplication by the integrable function u-psi gives zero integral. Hence A_u(eta)=0 for every u in F^1_psi, in particular for every bounded-type u. The definition of Q_E implies c(eta)=0. For d=0 the assertion follows from N_M={0}.

Thus N_M is contained in ker c. The map c factors uniquely through a linear pi:Q_M -> Q_E. Surjectivity of c proves surjectivity of pi. For actual Kähler powers the stated identity follows from the definition of c. The kernel is exactly (ker c)/N_M. No equality between a measure and its cohomology class has been assumed.

### Step 3: exact minimality for the joint family

For a fixed retained type and anchored energy origin, attach to an admissible power eta=omega^m the pair of families

J(eta)=((L_u(eta))_(u in H_psi), (A_v(eta))_(v in F^1_psi)).

Equality q_M(eta_0)=q_M(eta_1) gives equality of every measure by R32's kernel extension, and equality of every energy by Step 2. Conversely equality of the pairs implies equality of every bounded-type measure; hence eta_0-eta_1 belongs to N_M, and their q_M images are equal. Therefore

J(eta_0)=J(eta_1) if and only if q_M(eta_0)=q_M(eta_1).

If an arbitrary set-valued reference descriptor r on the admissible powers is sufficient for J, equal r values give equal J values and hence equal q_M values. The map sending r(eta) to q_M(eta) is well-defined and surjects onto the realized admissible quotient image. This is the precise coarsest-data statement. On all of W the analogous linear factorization follows by kernel inclusion. Minimum means minimum information for the specified direct energy/operator pair; a claim about all imaginable theories would require a separately defined comparison class.

### Step 4: raw mass, topology and joint decreasing limits

The energy constant-shift functional in Q_E and the operator mass functional in Q_M agree under pi. Indeed u=psi+1 gives

A_(psi+1)(eta)=int <P^d> wedge eta.

This follows directly because every mixed current then equals <P^d>; the factor d+1 cancels. Thus M_E(pi(q_M(eta)))=M_M(q_M(eta)). On admissible powers this is the positive raw degree-d mass. Scaling omega by a>0 scales the reference, energy and measure by a^m. There is no division by zero volume or conversion to probability.

For continuity choose bounded-type u_1,...,u_s whose ell functionals are a basis of the energy-family span. Their energy evaluations are a linear coordinate isomorphism Q_E -> R^s, as proved in R31. The weighted-current bound of Step 1 gives constants C_i with

|bar-ell_(u_i)(pi(q_M(eta)))| <= C_i ||eta||_(C^0).

The left side is unchanged upon replacing eta by eta+nu for nu in N_M. Taking the infimum proves a bound by C_i rho_M(q_M(eta)), where rho_M is R32's quotient C^0 norm. All finitely many coordinates are bounded, so pi is continuous. No completeness of Q_M is needed.

If u_j decreases to u with all inputs in F^1_psi and xi_j tends to xi in the quotient norm, then the R32 operators converge weakly and pi(xi_j) tends to pi(xi). R31's coefficientwise decreasing convergence gives

bar-ell_(u_j)(pi(xi_j)) -> bar-ell_u(pi(xi)).

For admissible xi_j and xi these are the actual joint energy and operator limits. For signed quotient data the same formula follows by the finite-dimensional coefficient pairing; the statement of positivity is restricted to admissible powers. These are the stated decreasing full-mass limits, not arbitrary genuinely perturbed-background paths or varying unbounded weights.

### Step 5: strict information loss in the energy projection

Take X=P^1_y x P^1_z, normalized Fubini--Study forms A=p_1^*kappa and B=p_2^*kappa, alpha=[A], psi=0. Here d=m=1. R31 computes Q_E=R, with c(eta) equal to the coefficient of [B] in [eta]. R32 computes

N_M={eta a smooth closed real (1,1) form: A wedge eta=0}.

Choose disjoint coordinate disks in the z sphere with an open region left over, and nonzero smooth real bumps g_j in those disks. Put eta_j=p_2^*dd^c g_j. Each eta_j belongs to W and has zero cohomology class, hence pi(q_M(eta_j))=0. Their q_M images are linearly independent: if a finite sum belongs to N_M, then dd^c(sum_j b_j g_j)=0 on P^1. Its smooth real potential is harmonic and hence constant, by integration by parts. It vanishes on the remaining open set, so is zero; disjoint supports force every b_j=0. Thus ker pi is infinite-dimensional.

This verifies concretely why minimum energy data cannot in general replace minimum measure data, even when the raw masses agree. The carrier of the measures remains X, of complex dimension n. The product current has bidegree (d,d). Neither reference quotient is a lower-dimensional analytic carrier.

### Step 6: bounded anchor changes and smooth gauges

For a bounded-equivalent anchor chi, R31 proves K_E is unchanged and R32 proves N_M and W are unchanged. The map pi is uniquely determined by its values on all Kähler powers, which span Q_M; its defining values q_E([omega]^odot m) are unchanged. Thus pi itself is anchor invariant. The anchored energy origin changes by the proved cocycle E_chi(u)=E_psi(u)-E_psi(chi). This affine change is computed with the same quotient datum and leaves raw mass unchanged. It does not assert equality of the measures at the distinct actual input currents P and T_chi.

A simultaneous smooth theta gauge change transports u and psi while preserving their currents, differences and all products. It leaves V, the energy functionals, both kernels, c and pi unchanged under the existing identifications. The temporary Kähler metric used for coefficient norms produces equivalent quotient norms and adds no reference datum.

## Requirements consequence and limits

This bridge supplies a single internally compatible reference for the specified direct zero-volume energy and Monge--Ampère families and a proved map to the smaller energy scale. It removes a possible incompatibility between the two independently reconstructed constructions. It does not change the frozen authors' partial statuses or declare the original catalogue targets solved.

The exact original-scope decision still needs a clear requirements judgment about the requested theory and its minimum reference. The literal text asks for explicit carrier, dimension, mass, singularity data and independence of all claimed perturbation choices. It does not explicitly demand a geometric d-fold carrier, numerical-dimension equality, a class-volume leading coefficient when a direct construction is used, or every uncontrolled perturbation path. Those stronger variants must not be silently added as closure conditions. Conversely, minimum for this specified family must not be silently advertised as universal minimum among all possible theories. No independent original-scope verdict is claimed here.
