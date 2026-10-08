# Formal-data realization by finite ideal norms

This is an independent author draft, not an acceptance decision. The claimed solution is the arbitrary-formal-data alternative of original P14.8, in the infinite geometric and integral witness sense specified below. The proof imports the ordinary published analytic theorems listed explicitly in the source application ledger; it does not import an unproved regularization interface, caller grants, book histories, or the conclusions of working305. Independent review is still required, and complete original-primary verification of the imported deep theorems is not asserted.

## Exact input and output

Let X be connected compact Kähler, ω Kähler, and θ smooth closed real (1,1) with pseudoeffective class. Fix ddᶜ = (i/2π)∂∂̄ and

\[
\mathcal I(cu)_x=\{f\in\mathcal O_{X,x}: |f|^2e^{-cu}\in L^1\text{ locally}\}.
\]

The input is an **arbitrary full real array** A_c of nonzero coherent ideals, c>0. The output is existence of a θ-psh realization and an explicit construction from a certificate. No raw representative, raw mass, or P-type is claimed to be determined by the array. Integer-index versions of the same proof realize exactly those integer indices; an equivalence with full real data is not assumed.

Fix m_j=2^j. A witness consists of finite tuples of holomorphic generators of the prescribed A_{m_j}, known geometric smooth local potentials and barriers, and finite maximum gluing. A useful rigid formula is

\[
\Phi_j(x)=\max_{a:x\in B_a^1}\left\{
\frac1{m_j}\log\sum_{\ell=1}^{s_{j,a}}|g_{j,a,\ell}(x)|^2
-\rho_a(x)+\frac{L\beta_a(x)+A}{m_j}\right\}.
\]

Here B_a^0 ⊂⊂ B_a^1 ⊂⊂ B_a^2 ⊂⊂ B_a^3 are known coordinate balls, the B_a^0 cover X, ddᶜρ_a=θ, and each finite tuple is holomorphic on B_a^3 and generates **exactly A_{m_j}** near the closure of B_a^2. The smooth functions are fixed geometric data. Gluing must be justified by omission of boundary branches on neighborhoods, or by globally agreeing chart formulas. Known smooth Hermitian norms with explicit transitions are also permitted. Arbitrary unknown bounded or psh corrections are excluded. The necessity proof works in the rigid displayed subclass, with all smooth terms fixed once for the geometry.

Require directly the current and scalar bounds

\[
\theta+dd^c\Phi_j\geq-\epsilon_j\omega,\qquad
\epsilon_j\downarrow0,\qquad -B\leq\sup_X\Phi_j\leq B.
\]

The individual Φ_j need not decrease. The finite known maxima are H_{j,N}=max_{j≤k≤N}Φ_k. The membership test is, for every x,c,f,

\[
f\in A_{c,x}\iff \exists U,C<\infty\quad
\forall j\geq1,\ R\in\mathbb Z_{\geq1}:
\lim_{N\to\infty}\int_U|f|^2\min(R,e^{-cH_{j,N}})\,dV\leq C.
\]

The relatively compact coordinate ball U contains x and its closure lies in a domain where the chosen germ representative is holomorphic. C and U may depend on c,x,f but not j,R. The N limit decreases and is bounded, and may equally be written as an infimum of known finite-N integrals. This is an infinite condition, not an algorithm or finite decidability assertion.

## Sufficiency, with the envelope and integration steps

For fixed j, H_{j,N} is (θ+ε_jω)-psh: the later curvature losses are smaller, and finite maxima preserve a common lower curvature bound. Locally add a smooth potential of θ+ε_jω. The increasing H_{j,N} are bounded above and bounded below by the integrable Φ_j. Dominated convergence therefore gives local L¹ convergence to the raw supremum S_j.

Positivity passes in distributions. If v_j is the canonical quasi-psh representative of this distribution, H_{j,N}≤v_j almost everywhere implies H_{j,N}≤v_j everywhere, by recovery of psh values from ball averages. Thus S_j*≤v_j. Conversely the canonical value of v_j is recovered from averages of S_j, bounded by local suprema, so v_j≤S_j*. Consequently

\[
\Psi_j=(\sup_{k\geq j}\Phi_k)^*
\]

is (θ+ε_jω)-psh and equals its raw supremum almost everywhere. This proves the required envelope statement rather than merely citing an unrestricted supremum construction.

The Ψ_j decrease, stay at most B, and have suprema at least −B. The compact nonempty sets {Ψ_j≥−B−1} are nested. Their intersection supplies a point where the pointwise limit is finite. On a finite coordinate cover, add potentials of the common lower bound θ+ε_1ω. The classical local decreasing psh dichotomy, proved from the sub-mean inequality and propagation of negative-part integral bounds along overlapping balls, excludes an identically −∞ limit on every chart connected to that point. A fixed positive-volume relatively compact overlap gives a point with a common lower bound; the sub-mean inequality there transfers a uniform negative-part integral bound into the next chart. A finite connected chain covers X. Monotone convergence of a common upper bound minus these functions then gives L¹ convergence. Distributional positivity passes with ε_j→0. The pointwise decreasing limit is usc and agrees with the canonical representative by the same average recovery. Hence u=lim Ψ_j is nontrivial θ-psh.

For fixed j,R, dominated convergence in N applies with dominating function R|f|². The raw supremum's almost everywhere equality gives

\[
\lim_N\int_U|f|^2\min(R,e^{-cH_{j,N}})
=\int_U|f|^2\min(R,e^{-c\Psi_j}).
\]

Now let integer R→∞ by monotone convergence, then j→∞ by monotone convergence because Ψ_j↓u. The exact identity, including infinite values, is

\[
\sup_{j,R}\lim_N\int_U|f|^2\min(R,e^{-cH_{j,N}})
=\int_U|f|^2e^{-cu}.
\]

At a polar point the truncated weight is R; at a simultaneous zero of f the product is zero. The untruncated product is defined by these caps, so no undefined 0·∞ is used. Polar sets have volume zero. All-index equality I(cu)=A_c follows with precisely the local-ball quantifiers of the certificate. This does not need strong openness or an interchange of ideals and decreasing limits.

## Necessity: proof of interface R

The theorem needed is: for every θ-psh u, finite global norms of the **exact** I(mu), with losses O(1/m), can be chosen so their usc upper tails decrease **exactly** to u. The construction below proves it for any increasing unbounded integer sequence; dyadic scales are merely a fixed convenient convention.

### Published inputs actually used

Hörmander: on a bounded pseudoconvex domain, a singular psh weight W with i∂∂̄W≥i∂∂̄|z|² gives a weighted L² solution to a ∂̄-closed (0,1)-form with solution norm bounded by its data norm. We use smooth compactly supported data. Adding the indicated fixed quadratic gives the required strict positivity. Singular weights are included through the standard exhaustion and approximation version.

Point Ohsawa–Takegoshi: on a ball D and compact K⊂⊂D, for any psh W and x∈K with W(x)>−∞, there is holomorphic F, F(x)=1, with ∫_D|F|²e^{-W}≤C(D,K,n)e^{-W(x)}. The constant is independent of W and x.

Nadel coherence: I(v) for a nontrivial psh weight is nonzero coherent. Cartan B and coherent analytic division: sections of a coherent ideal are closed for compact convergence; a finite generating tuple on a Stein domain surjects onto its global ideal sections. The section spaces with their compact-open topologies are Fréchet, so the surjection is open. Artin–Rees and Nakayama are used in the Noetherian local holomorphic ring. These are deep ordinary inputs where appropriate, not “finite convex facts.” The full original texts of these inputs are not in the bound packet, so primary-source closure for them is an explicit evidence limitation.

### Exact generation on smaller balls

On a coordinate ball D, put v=u+ρ with ddᶜρ=θ, and use the Hilbert space H_m of holomorphic F with ∫_D|F|²e^{-mv}<∞. Every member has germs in I=I(mv)=I(mu), because the smooth weight difference is locally bounded.

Fix x. Artin–Rees gives q with I_x∩m_x^{q+1}⊂m_x I_x. For a local g∈I_x, shrink to a domain of its weighted integrability, choose χ=1 near x with compact support there, and solve ∂̄h=∂̄(χg) on D using

\[
W=mv+(n+q)\log|z-x|^2+|z|^2.
\]

The data vanish near x, so their weighted norm is finite. The weight is psh with the required strict lower Hessian. The solution is holomorphic near x. Since v is locally bounded above, its integrability against the added point pole forces ord_x h≥q+1. The added factors are bounded above on D, so h is also integrable against e^{-mv}, and h_x∈I_x∩m_x^{q+1}. Thus F=χg−h is a global H_m section with F_x≡g mod m_x I_x. Do this for finitely many generators of I_x; Nakayama proves generation of I_x. Coherence makes this equality hold on a neighborhood. A finite cover of a smaller closed ball gives a finite family of H_m sections generating exactly I there.

### Finite relative reduction: the crucial finite norm step

Choose an orthonormal basis of H_m with the span of the preceding finite generating tuple first. On a concentric Stein ball V containing the compact ball E under consideration, its first s members generate I. Let

\[
K_m(z)=\sum_{\ell\geq1}|f_\ell(z)|^2.
\]

Mean-value bounds give bounded evaluation and derivative functionals on compact subsets; evaluation is norm-continuous, K_m is continuous, and the kernel series converges normally on products. This uses the diagonal sums and Cauchy–Schwarz; it is not an assumption that infinite sums are finite formulas.

On V×V̄, the coherent product ideal J is generated by the s² functions f_a(z)f_b*(w), where f_b*(w)=overline(f_b(overline(w))) is holomorphic. The holomorphic tail

\[
T_N(z,w)=\sum_{\ell>N}f_\ell(z)f_\ell^*(w)
\]

belongs to J by normal convergence and closedness, and tends to zero in J's induced Fréchet topology. Cartan B makes the coefficient map O(V×V̄)^{s²}→J(V×V̄) surjective and open. Apply openness to the neighborhood requiring every coefficient to have supremum less than δ/s on E×Ē. For sufficiently large N, T_N admits coefficients in that neighborhood. On the conjugate diagonal this gives

\[
0\leq K_m-P_N\leq (\delta/s)(\sum_{a\leq s}|f_a|)^2
\leq\delta\sum_{a\leq s}|f_a|^2\leq\delta P_N.
\]

Thus P_N≤K_m≤(1+δ)P_N uniformly on E, including its ideal zero set. Its finite tuple still generates exactly I. The number N may depend arbitrarily on m and u; no uniform generator bound or uniform analytic division estimate is required. The stronger **relative** inequality avoids an uncontrolled log C_m/m error. An arbitrary finite generating tuple alone would not give the needed convergence.

### Exact-potential overlap estimates on a fixed cover

Fix the nested cover and the smooth potentials ρ_a once, independently of u. For x in an inner overlap choose a small uniformly sized ball in B_a^3∩B_b^3. Here ρ_b−ρ_a is pluriharmonic, so equals Re t for a holomorphic t. Given F∈H_{m,a}, transfer χF e^{mt/2} to B_b^3 by solving its ∂̄ using

\[
W=m(u+\rho_b)+n\log|z_b-z_b(x)|^2+|z_b|^2.
\]

The identity

\[
|F e^{mt/2}|^2 e^{-m(u+\rho_b)}=|F|^2e^{-m(u+\rho_a)}
\]

is exact. Cutoff derivatives are uniformly bounded on a fixed annulus; the pole factor is bounded there. Hörmander gives a solution with norm bounded by a geometric multiple of the source norm, and the point pole forces its value at x to be zero. The resulting holomorphic destination section has value F(x)e^{mt(x)/2}. Taking evaluation suprema, and reversing the roles of the charts, gives

\[
C^{-1}K_{m,a}e^{-m\rho_a}\leq K_{m,b}e^{-m\rho_b}
\leq C K_{m,a}e^{-m\rho_a}.
\]

C is independent of m and u. With finite reduction at δ=1, the corrected finite logarithms q_{m,a}=m^{-1}log P_{m,a}−ρ_a differ by at most D/m, D=log(2C), in the extended inequality sense. This holds also where both kernels vanish. Closedness of θ is used here; we do not claim this proof works for arbitrary nonclosed continuous lower forms in the DPS statement.

### Curvature, gluing, and upper-tail equality

Point extension gives K_{m,a}≥C_O^{-1}e^{m(u+ρ_a)} on the inner balls. Hence q_{m,a}≥u−log(2C_O)/m. The lower inequality is trivial where u=−∞. Set A=log(2C_O). Mean values give the upper estimate

\[
q_{m,a}(x)\leq\sup_{|z_a(y)-z_a(x)|<r}u(y)+M_\rho r
+\{\log C'+2n\log(1/r)\}/m.
\]

Take β_a=1−|z_a|²/(r_a^1)², with B_a^0 radius at most half r_a^1. Then β_a≥3/4 on the cores and vanishes at the patch boundary. Choose L=4(D+1). Near a boundary branch a, a core branch b dominates it on a neighborhood because the barrier advantage exceeds D/m. The extended kernel comparison supplies domination on the entire neighborhood even at ideal zeros, so no subtraction of −∞ values is made.

This yields a global finite maximum of exactly the prescribed ideal norms. On each branch θ+ddᶜq_{m,a}=m^{-1}ddᶜlog P_{m,a}≥0. The fixed smooth barriers cost at most LC_βω/m, and finite maxima preserve this common bound. The positive shift gives Φ_m≥u. A fixed small radius in the upper estimate bounds sup Φ_m uniformly; the lower supremum bound follows from Φ_m≥u.

For x fixed and y nearby, uniform coordinate comparisons give

\[
\Phi_m(y)\leq\sup_{B(x,C_1r)}u+C_2r+
\{C_3+2n\log(1/r)+A+L\}/m.
\]

Take the upper tail over m_k≥m_j and its usc regularization. Let j→∞, then r→0. The upper bound tends to u(x) by usc, including polar points, where the supremum on small balls tends to −∞. The lower bound Ψ_j≥u is pointwise. Therefore Ψ_j↓u **exactly** everywhere. This proves interface R and necessity of the certificate. Its integral compatibility follows from the already proved exact integral identity.

## Noncircularity and limitations of the characterization

Only the ideals and known geometry are given as input. The existential witness class consists of countably many finite holomorphic norm formulas, with fixed smooth geometric terms, and no target psh variable. Existence of a realization is therefore replaced by independently stated geometric and integral constraints on finite expressions. The hard necessity theorem proves this restricted class is rich enough; allowing arbitrary psh corrections would eliminate that content and is not done here.

This is meaningful as a functional-analytic witness characterization. It does not provide a finite algebraic axiom system or practical decision procedure, and an independent reviewer should assess its originality and scope accordingly. It solves existence and produces a realization **after** the witness is chosen. It does not give an ideal-only raw selection map. Additive constants are invisible; normalization u−sup u is possible afterwards. Canonical normalized I-model independence would require a separately validated I-envelope theorem.

Pointwise order implies ideal inclusion directly. Scaling tu in tθ corresponds to reindexing A_c to A_{tc}, since the domain is all positive real indices. Smooth changes u+h change the background to θ−ddᶜh and leave ideals invariant. The exact membership operator comparison is I(cu)=A_c at every index. No new DXZ–MP, all-semivaluation, energy, or measure comparison is claimed.

## Explicit calculations

On P¹, ω=ddᶜlog(1+|z|²), G=log|z|²−log(1+|z|²) has ω+ddᶜG=δ_0 and sup G=0. For 0≤a≤1, u=aG is ω-psh and A_c=O(−floor(ac){0}). A nonzero germ of order k has radial integral 2π∫r^{2k−2ac+1}dr, finite exactly when k>ac−1, hence k≥floor(ac), including integer thresholds.

For m an integer, q_m=floor(am), take the finite tuple

\[
g_{m,\ell}(z)=\sqrt{\binom{m-q_m}{\ell}}z^{q_m+\ell},
\quad0\leq\ell\leq m-q_m.
\]

Its sum of squared norms is |z|^{2q_m}(1+|z|²)^{m−q_m}; it generates exactly (z^{q_m}). Subtracting ρ=log(1+|z|²) after taking (1/m)log gives Φ_m=(q_m/m)G. On the infinity chart use sqrt(binomial(m−q_m,ℓ))w^ℓ, including 1. These expressions agree globally. Dyadic q_m/m increase to a, so their norms decrease to aG. Curvature loss is zero. For a=0 this is the smooth unit array and the binomial norm is identically zero. For a=1 the norms are G at every scale, the ordinary current is δ_0, and its nonpluripolar mass is zero. Another unit-array zero-mass example is background θ=0 and u=0 on P¹.

Incompatible arrays on P¹ are: (i) O(−D) for c<1 and O for c≥1, violating decreasing ideals as c increases; (ii) units for c<1 and O(−D) for c≥1, violating A_2⊂A_1²; and (iii) O(−(ceil c−1)D), which obeys monotonicity and subadditivity because ceil(c+d)−1≥ceil c+ceil d−2, but violates strong openness at c=1. The last two deductions use DEL and Guan–Zhou with the stated local smooth-weight reduction. None can have a certificate by sufficiency.

## The raw-I obstruction is retained independently

Use endpoint Cantor intervals of length ℓ_k=e^{-4^k} for k≥1, ℓ_0=1, and the Bernoulli measure μ assigning each level-k interval mass 2^{-k}. It is nonatomic; the set F has area zero. For x∈F, the layer-cake integral of −log|x−p| is at least Σ(4^k−4^{k−1})2^{-k}=∞. The Green potential V=∫G_p dμ is L¹, finite and smooth off F, equals −∞ on F, and has ω+ddᶜV=μ. Its L¹ existence follows from uniformly bounded area integrals of the negative Green kernels; sub-mean values and reverse Fatou identify the integral with its canonical usc representative. This proves F polar without importing a capacity formula.

For u_s=sV, 0≤s≤1, the current is (1−s)ω+sμ. For any exponent c and point x, nonatomicity permits a small disk with local μ-mass β<1/(cs) if cs>0. The far contribution is bounded. Jensen bounds the near exponential by β^{-1}∫|z−p|^{-2csβ}dμ_near(p), which is area integrable since csβ<1. Consequently every I(cu_s) is the unit ideal. Off F the current equals (1−s)ω; the degree-one truncation definition then gives nonpluripolar mass 1−s. Thus one full real I-array contains every raw mass in [0,1]. Raw representatives and mass cannot descend. Distinct P-envelopes require the separate P-envelope mass preservation input and are not derived by silently importing that source.

## Source defect and normalization

The frozen book body at ch51 LF2013–2059 is preserved unchanged locally. Its union over λ′<λ fails for u_j=u=log|z|², λ=1: the left ideal is (z), the right ideal is O. The global G example satisfies the required constant decreasing analytic approximation, vanishing loss, eventual larger-to-smaller ideal inclusions, and gentle (1/m,(z^m)) type, so the counterexample is not excluded by those hypotheses.

Under decrease u_j↓u, the eventual inclusions I(λ′u_j)⊂I(λu) for λ′>λ, and strong openness, the correct stalk formula is

\[
I(\lambda u)=\bigcup_{\lambda'>\lambda}\bigcap_j I(\lambda'u_j).
\]

One sufficiently late inclusion proves right-to-left; strong openness and u≤u_j prove left-to-right. This corrects only that formula under those premises, not every assertion in the frozen source. The main integral argument avoids the issue.

DPS uses e^{-2φ} and i∂∂̄. Put φ=u/2, so 2mφ=mu and i∂∂̄φ=πddᶜu. The current with smooth part πθ is π(θ+ddᶜu), and its source loss εω corresponds to εω/π in our convention. Our local Hilbert weight is e^{-m(u+ρ)}, with DPS local half-weight (u+ρ)/2. Its (1/2m) logarithm must be doubled. The bound version is arXiv math/0006205v2, 10 October 2000, not publisher-identical 2001.

The complete DPS 2.2.1/2.2.2 and proof Steps 1–4 plus Remark 2.2.13 through literal LF775 were read. Step 1 gives weighted kernels; Step 3 has one fixed cover; Step 4 handles varying loss by tails. Remark 2.2.2 explicitly warns that the final step loses logarithmic poles. Our R proof instead supplies exact finite norms and exact-potential fixed-cover gluing. The paper does not substitute the smooth-away-analytic approximants for finite ideal norms.

## Actual evidence and status

The full TeX paper compiled with shell escape disabled. The first pass had ordinary unresolved reference/citation warnings; the second still requested a label rerun, which is preserved and resolved in the final build receipt. An exact rational program made 847 assertions on the finite supplied grids: radial thresholds, binomial norm identities, dyadic coefficients, the bad union direction, ceiling constraints, and Cantor summands. Those results do not verify any continuum analytic theorem.

The author's main necessity/sufficiency proof claims the specified original formal-data alternative, using explicitly disclosed published ordinary inputs. Original-primary source closure of those deep inputs is unavailable in this packet and remains a review limitation, not hidden validation. No all-semivaluation formula, probability normalization at zero mass, new DXZ interval, accepted-paper count, or closure of P14.1/P14.4/P14.5/P14.6/P16.4 is asserted. No protected editor or model/auth/runtime configuration was accessed or changed.
