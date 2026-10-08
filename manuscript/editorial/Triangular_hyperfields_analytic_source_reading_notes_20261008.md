# Actual primary and selected dependency reading notes

Date: 8 October 2026. One complete 88-page primary and four partial dependencies (47 pages). Total 135 distinct exact-source/page pairs and 68 individually displayed matching images. Preparation and metadata searches have zero reading credit. Earlier observations remain unchanged; later notes explicitly resolve them.


## Complete primary

### BHKL analytic physical pages 1,2

Actual primary reading, sheet 01, physical pages 1--2 of 2607.15375v2. Complete selected text and the individually displayed matching original-resolution image were read.

The title/author/date and 88-page structure agree with acquisition: Baker--Huh--Kummer--Lorscheid, analytic Part 2, revised 18 August 2026. The abstract distinguishes a homeomorphism with every positive-q weak cell from coefficientwise sandwich containments with a support-dependent lower parameter and universal upper parameter two. These are not the same assertion. For general M-convex support the coefficient normalization divides by the multi-index factorial; matroid support is squarefree. The announced q(4), q(5) and asymptotic bounds remain provisional until their statements/proofs are read. Contents locate the upper containment, rank-two/general sandwiches, sharp five-element lower bound, strong representations and six tree-distance proofs. No proof or integration credit yet.


### BHKL analytic physical pages 3,4

Actual primary reading, sheet 02, physical pages 3--4. Full selected text and original matching image read.

Theorem 1.1's general sandwich includes N on both weak-cell bounds; N is trivial on matroid bases. The unnormalized bivariate inclusion is explicitly said to fail for every positive q, so normalization is load-bearing. Theorem 1.2 assumes n>=4, a symmetric zero diagonal matrix, strictly positive off-diagonals and 0<q<=log_2(1+1/(n-2)); metric powers and rank-two contractions are only the announced route at this point. Definition 1.3 is a supremum of containment parameters, not a priori attainment assertion.

Audit item TH-A01 pending: the earlier introductory statement Gr^w_J(T_0) subset P L_J is printed without N for every M-convex J, whereas the normalized theorem and bivariate obstruction suggest the exact coefficient convention needs inspection. Do not assert an error before reading definitions and the cited foundation; do not import this unnormalized preliminary assertion unqualified. The book's raw bivariate base enumerator fixture provides a useful later convention test.


### BHKL analytic physical pages 5,6

Actual primary reading, sheet 03, physical pages 5--6. Full selected text and original matching image read.

Proposition 1.4 announces parity-sensitive upper bounds 2 log_2(n/(n-2)) and log_2((n+1)/(n-3)); Conjecture 1.5 says these are sharp for all n>=4, with n=5 already proved later. This is a source-era conjecture, not a canonical open-status addition. The appendix introductory unnormalized T_0 assertion repeats TH-A01's convention concern. Definitions 2.1--2.4 require nonnegative entries for Lorentzian matrices and inertia (1,n-1,0) for strictness; CND is negative on the sum-zero hyperplane. The author AI/Lean acknowledgement is a source statement, not an independently run Lean certificate or a model-verification receipt for this book; no formalization files occur in the acquired three-file source archive.


### BHKL analytic physical pages 7,8

Actual primary reading, sheet 04, physical pages 7--8. Complete selected text and matching original-resolution image read.

Theorem 2.5's alternating principal-determinant criterion assumes a nonnegative real symmetric matrix; dependency [17] Lemma 2.2 remains to anchor. Polynomial notation f=sum c_alpha x^alpha/alpha! is expressly normalized. Theorems 2.9--2.11 cite BH Proposition 2.19/Theorem 2.23, Theorem 2.25 and Theorem 3.10 for M-convex support, the derivative criterion and the exponential base enumerator. The support J is nonempty and lies in a fixed finite degree simplex. These exact locators need controlling-edition checks before import. TH-A01 remains pending: the local polynomial coefficient convention is now explicit, but the weak-cell coordinate convention is on following pages. Definitions concern limits of strict forms and distinguish M-convex support from arbitrary positive coefficients.


### BHKL analytic physical pages 9,10

Actual primary reading, sheet 05, physical pages 9--10. Complete selected text and matching original-resolution image read.

The tract definition here deliberately strengthens general tract conventions by additive ideal closure; the footnote prevents transferring this definition to all tracts without qualification. T_q uses 1/q-powers as polygon side lengths. Lemma 2.14's full Heron-factor argument handles nonnegative and degenerate triangles; Corollary 2.17 has the exact exponents 4/q and 2/q. T_0 is the intersection, T_infinity the union, of these null sets. Lemma 2.19's maximum-attained-twice description and the infinity extra three-nonzero condition are attributed to Part 1 Lemma 3.9 and need its exact edition checked. No representability means ordinary real/complex algebraic representability yet.


### BHKL analytic physical pages 11,12

Actual primary reading, sheet 06, physical pages 11--12. Read complete selected text and original matching image.

Definitions 2.20--2.22 fix coordinatewise inf/sup bounds on admissible weak three-term Plucker relations, including repeated indices; projectivization is positive scaling. Definition 2.23 explicitly identifies rho with the exponential generating polynomial sum rho(alpha)x^alpha/alpha!. This can explain the earlier no-N T_0 containment under that identification, so TH-A01 is a convention question rather than a demonstrated false formula.

TH-A02 pending: Section 3 again describes N as dividing ordinary polynomial coefficients by alpha!, and says the normalized upper statement follows by the same argument applied to N^{-1}f. This needs checking against the exponential identification and the actual proof: N^{-1} need not preserve Lorentzianity (the full bivariate boundary quadratic is a test). Do not conflate raw rho, exponential f_rho and a second application of N. Theorem 3.1 and general sandwich must be read in their proof's explicit coordinates before import. Lemma 3.2's n=2 proof uses strict positive single-basis coefficient; n=3 continuation remains unread.


### BHKL analytic physical pages 13,14

Actual primary reading, sheet 07, physical pages 13--14. Complete selected text and matching original-resolution image read.

Lemma 3.2's n=3 determinant 2abc gives strict inertia (1,2,0) for positive off-diagonals. Proposition 3.3's full four-element computation reduces Lorentzianity to det A<=0 and the triangle condition for sqrt(af),sqrt(be),sqrt(cd), with automatic smaller minors. Lemma 3.4 subtracts a nonnegative diagonal bounded by the original diagonal; its two-dimensional positive-subspace argument is valid and does not assert converse monotonicity. Proposition 3.5 explicitly uses exponential coefficients rho and quadratic derivatives, confirming the need to separate that identification from raw coefficients. Its proof continues; Theorem 3.1's extra normalization remains TH-A02 pending.


### BHKL analytic physical pages 15,16

Actual primary reading, sheet 08, physical pages 15--16. Complete selected text and original matching image read.

Proposition 3.5's four-case proof is fully read: distinct indices delete diagonals; one repeated index gives d(2bc-ad)>=0, hence the weaker T_2 threshold ad<=4bc; two repeated pairs give ac<=b^2, hence ac<=4b^2; triple repetition is automatic. The strictly positive U_2,4 proposition is invoked for a possibly sparse restriction, but its displayed determinant identity directly extends to nonnegative entries, so no new positivity hypothesis is necessary for that elementary inequality. Lemma 3.6 announces factorial division preserves every weak T_q representation, including endpoints; proof is next. Upper normalized containment remains pending, since preservation alone has a subset direction that does not reverse.


### BHKL analytic physical pages 17,18

Actual primary reading, sheet 09, physical pages 17--18. Full selected text and original matching image read.

Lemma 3.6's factorial-product comparison is read through all nontrivial repetition types: distinct indices have equal denominator products; one repeated index or two pairs shrink the unique Plucker product relative to the equal pair by factorial log-convexity. Finite-q condition is T_unique<=2^q T_equal. The i<j=k<ell case has a different named unique term but the same relabelled inequality. Zero entries and q=0/infinity endpoints must be handled by null-set definitions rather than taking undefined 1/0 powers; the source explicitly states that interpretation. The lemma's conclusion is preservation by N, not by N^{-1}. Final trivial cases and subsequent normalized proof are on the next sheet.


### BHKL analytic physical pages 19,20

Actual primary reading, sheet 10, physical pages 19--20. Complete selected text and original matching image read.

Lemma 3.6 ends correctly with equal products/denominators in triple or quadruple repetition. Proposition 3.7 does not assume N^{-1}f is Lorentzian: after differentiation and positive diagonal rescaling its diagonal coefficients acquire lambda_i=(alpha_i+2)/(alpha_i+1)<=2, while off-diagonals stay fixed. The original derivative's Lorentzian minors then give the required factor-four weak T_2 inequalities, including lambda_i lambda_k<=4. This resolves TH-A02's suspected inverse-preservation step in favour of the explicit proof, subject to its final continuation. TH-A01's no-N foundational assertion is consistent with the exponential identification in Definition 2.23; an integration must state the embedding explicitly and avoid silently treating the raw coefficient polynomial as the same generating function. No source error is asserted from the earlier convention questions.


### BHKL analytic physical pages 21,22

Actual primary reading, sheet 11, physical pages 21--22. Complete selected text and original matching image read.

Theorem 3.1 now has its complete proof through Proposition 3.7's repeated-index factor bounds; no inverse-Lorentzian preservation was used. TH-A02 is cleared mathematically. The eventual presentation must explicitly fix raw/exponential embeddings (TH-A01 convention resolved by Definition 2.23) rather than infer coefficientwise identity from homeomorphism.

Definitions 4.1--4.2 require symmetric zero diagonal and strictly positive off-diagonals. T_q imposes quartet triangle inequalities on product 1/q-powers, with q=0 interpreted by repeated maxima. Theorem 4.3 uses epsilon(n), n>=4, and monotonicity for smaller positive q. Lemma 4.4's complete positive diagonal congruence proof preserves all three quartet sides by one common factor and inertia by Sylvester. Boundary semidefinite Lorentzian conclusion is weaker than strict inertia; no strictness is asserted yet.


### BHKL analytic physical pages 23,24

Actual primary reading, sheet 12, physical pages 23--24. Complete selected text and original matching image read.

Theorem 4.5 imports [11] Theorem 3.6: m-point metrics snowflaked to d^(p/2), 0<=p<eta(m)=log_2(1+1/(m-1)), embed affinely independently in R^(m-1). The strict endpoint and p=0 off-diagonal-one convention are explicit and load-bearing; this dependency needs primary checking. Lemma 4.7's two directions are read: a kernel argument on a putative positive plane gives CND necessity/sufficiency, while the large-T Gram determinant constructs a second positive direction from any positive sum-zero vector. Euclidean-distance and strict-affine-independence consequences continue next. Schoenberg is a background import, not the actual quantitative input here.


### BHKL analytic physical pages 25,26

Actual primary reading, sheet 13, physical pages 25--26. Complete text and matching original-resolution image read.

Lemma 4.7's Euclidean CND identity is -2||sum alpha_i v_i||^2 on sum-zero vectors. Affine independence excludes the kernel, and the isotropic nonzero (1,0) vector plus nonsingularity/at-most-one-positive gives inertia (1,m,0). The rank-two proof chooses D=diag(1,A_12^{-1},...,A_1n^{-1}), normalizes the first row to ones, and obtains the (n-1)-point metric d_ij=B_ij^(1/q) from quartets involving the first vertex. The snowflake exponent p=q then gives squared distances B and strict inertia for q<epsilon(n). Correct positivity, dimension and exponent factors are retained. Boundary case continues next and is not yet credited.


### BHKL analytic physical pages 27,28

Actual primary reading, sheet 14, physical pages 27--28. Complete selected text and original matching image read.

Theorem 4.3's endpoint is handled by A^epsilon satisfying T_{epsilon epsilon(n)} with epsilon<1, then closure as epsilon tends to one; strict inertia is only concluded in the interior. Only distinguished-vertex quartets enter this basic proof. The four-cycle test has sum-zero quadratic 4*2^q-8 and shows arbitrary four-point snowflakes cannot improve beyond q=1. The later sharp q(5) argument needs the extra Ptolemy quartets. Blumenthal/[15] Theorem 2.4 is a separate stronger imported input to locate.

Theorem 5.1 assumes t>0 and uses N_t(x^alpha)=x^alpha/(alpha!)^t, a support-dependent positive lower threshold and upper parameter p(t)=2 max(1,t), including p=infinity. The t=0 endpoint is a compatibility remark, not a positive universal lower threshold. Under the explicitly exponential representation embedding, N_t additionally divides the generating polynomial's coefficients; the convention must remain explicit. Full general proof unread beyond this statement.


### BHKL analytic physical pages 29,30

Actual primary reading, sheet 15, physical pages 29--30. Full selected text and original matching image read.

Lemmas 5.3--5.4 fix the exponential coefficients a_k: Lorentzianity requires log-concavity with no internal zeros; weak repeated-index relations allow the weaker a_(k-1)a_(k+1)<=2^q a_k^2. Proposition 5.5 explicitly applies N_t to f_rho, so its polynomial has factorial power t+1. This decisively resolves the earlier embedding ambiguity for the proof. The positive threshold is t times the minimum log_2((k+1)(d-k+1)/(k(d-k))), with d>=2 and t>0; proof continues next.

TH-A03: Lemma 5.4's printed iff for an arbitrary nonnegative coefficient function omits the exact-support condition supp(rho)=Delta^d_2 from Definition 2.21. The all-zero function satisfies every displayed inequality but is not in the specified weak cell; sparse non-M-convex examples can do likewise. Its relation calculation is valid under exact full support (all a_k>0). This is a missing standalone qualification, not a disproof of the fixed-support sandwich theorem. Any integration must retain exact support/positivity explicitly; no canonical status or original result promotion follows.


### BHKL analytic physical pages 31,32

Actual primary reading, sheet 16, physical pages 31--32. Full selected text and matching original-resolution image read.

Proposition 5.5's whole proof is read: factorial ratios exactly offset the 2^q weak log-concavity loss, and one interior coefficient in (2^{-q/2},1) gives a positive full-support t=0 failure for every positive q. Division is legitimate because exact full support means positive a_k. Its q=0 equality is with the fixed full-support stratum, not all sparse Lorentzian polynomials. The stated large-degree asymptotic is 4t/((ln 2)d).

Theorem 5.6 starts contraction to rank two and parallel-class simplification. TH-A04 pending: the printed shortcut for at most three parallel classes cannot hold for arbitrary positive cross-class coefficients without the weak Plucker constraints. A two-by-two bipartite block of rank two has two positive singular-value eigenvalues. The weak relations impose extra rank-one/proportionality structure; this must precede the uniform m<=3 assertion. Its displayed ratio argument later explicitly uses two distinct outside classes, so m=2 needs the two-parallel-pairs relation instead. Check continuation and primary foundations before integration. Also state rank-zero/one conventions separately if the all-rank theorem is used, since the local derivative setup assumed d>=2.


### BHKL analytic physical pages 33,34

Actual primary reading, sheet 17, physical pages 33--34. Full selected text and matching original-resolution image read.

Theorem 5.6 ends by positive linear substitution from simplified rank-two uniform polynomials and a finite minimum of epsilon(m). The earlier at-most-three-classes shortcut still needs the weak proportionality constraints (TH-A04). Remark 5.7 states q(M)>=q(h(M)), nonincreasing q(n), binary q=infinity and ternary q>=2; no blanket current-open consequence is imported.

TH-A05 pending: its proof of arbitrary-minor monotonicity q(N)>=q(M) only observes that representations and Lorentzianity descend. This does not, by itself, show every weak representation of N extends to M. An extension or density argument is required for that quantifier direction; do not import the arbitrary-minor assertion on this proof alone. Uniform minors may admit an explicit duplicate-row extension, but that is a different restricted argument. Investigate rigid projective-plane supports as a finite diagnostic rather than assert a counterexample prematurely.

Lemma 5.8 begins quadratic M-convex simplification, with multipartite support and singleton parts containing squares attributed to Part 1 Lemma 4.5. It fixes positive class weights summing to one and the simplified c-bar. Its full proof is next; isolated single-square support requires a separate boundary check because V(K) is defined via off-diagonal monomials.


### BHKL analytic physical pages 35,36

Actual primary reading, sheet 18, physical pages 35--36. Complete selected text and original matching image read.

Lemma 5.8's proof imports Part 1 Theorem 4.7's T_infinity simplification, then pulls back each T_q relation with a common positive weight factor. Lemma 5.10's surjective linear pullback preserves positive index and only adds zero directions; it asserts Lorentzian equivalence, not strict inertia equivalence. These dependency locators are load-bearing and remain to check. Lemma 5.11 begins the finite weighted-copy construction, with theta_a in (0,1) precisely on square-containing singleton parts and zero elsewhere. Exact claim is a uniform rank-two weak representation on the enlarged ground set. The pure-square support not appearing in V(K)'s off-diagonal definition remains a boundary to check in the final general argument.


### BHKL analytic physical pages 37,38

Actual primary reading, sheet 19, physical pages 37--38. Complete selected text and original matching image read.

Weighted-copy probabilities have positive entries, total one and 1-sum mu^2=theta, with finite size chosen independently of the coefficient magnitudes. The lifted off-diagonals use sqrt(mu_u mu_v)c_bar, and compression vectors use sqrt(mu_u); the resulting off-diagonal factor is exactly one and diagonal factor theta. Disjoint supports ensure independent compression vectors. For quartets mapping to four increments within the downstairs inf/sup bounds, products share one weight factor. If three or four copies map to the same index, the downstairs relation need not be admissible under those bounds, but all three products coincide and satisfy every triangular null-set relation directly. This supplies the trivial configuration qualification to the proof's blanket pullback sentence; no counterexample to the lift is found.


### BHKL analytic physical pages 39,40

Actual primary reading, sheet 20, physical pages 39--40. Complete selected text and matching original-resolution image read.

Lemma 5.11 ends by quadratic compression decreasing positive index. In Remark 5.12, equal copy weights give theta=1-1/m; calling general natural-matroid copies parallel is loose terminology when a basis can contain two copies in one fibre. An eventual book presentation should say copies/clones and reserve parallel for rank-one fibres.

Proposition 5.13 fixes each quadratic residual K_gamma and uses exact exponential expansion. Scalar (gamma!)^t and diagonal congruence (gamma_i+1)^t give theta_i=((gamma_i+1)/(gamma_i+2))^t in (0,1); copy size depends only on gamma/support/t, not rho. Uniform lifted sizes two or three have the earlier elementary Lorentzian matrices; larger sizes use epsilon(M_gamma).

TH-A06: the proof directly applies Lemma 5.8 even when K_gamma is the singleton {2e_i}, which has empty off-diagonal V(K). The stated simplification cannot represent that nonzero pure square on zero variables. This boundary is easily handled separately as a one-positive-eigenvalue rank-one Hessian; verify the continuation does not already do so. Do not regard it as a disproof of the main containment.


### BHKL analytic physical pages 41,42

Actual primary reading, sheet 21, physical pages 41--42. Full selected text and matching original-resolution image read.

Proposition 5.13 ends with a finite minimum over nonzero quadratic residuals; zero derivatives impose no condition. It does not explicitly handle the nonzero pure-square boundary, so TH-A06 remains the needed elementary separate case. N_1 permits equal copy counts gamma_i+2; general t uses continuously weighted copies. The source again calls copies parallel loosely.

Lemma 5.15 gives exact nonnegative Lorentzian Hessian bounds: distinct quartet T_2, single repeat H_ii H_kl<=2H_ik H_il, and paired repeats H_ii H_kk<=H_ik^2. Its three-minor proof includes the z=0 case. Proposition 5.16 uses p(t)=max{2,1+t,2t}, equal to 2 max{1,t}; proof continues. No arbitrary-minor monotonicity issue is used in this general weighted-copy containment route.


### BHKL analytic physical pages 43,44

Actual primary reading, sheet 22, physical pages 43--44. Full selected text and original matching image read.

The upper N_t proof fully checks the diagonal factors: distinct products need p>=2; one repeated index needs p>=1+t; paired repeats need p>=2t. Their maximum equals 2 max(1,t). Triple/quadruple repeats are automatic; the main theorem concludes with the lower finite-copy proof and its elementary pure-square qualification TH-A06.

Remark 5.17 uses BH Theorem 3.2's symbol criterion and the product of bivariate symbols, whose normalized coefficient sequence (a!)^{-t} is log-concave for finite t>=0. This proves preservation by N_t, not its inverse. The weak preservation extends Lemma 3.6 by raising denominator comparisons to t. These exact symbol/product/bivariate inputs need primary locators. Section 6's opening distinguishes support-dependent positive lower bounds from an impossible positive universal parameter.


### BHKL analytic physical pages 45,46

Actual primary reading, sheet 23, physical pages 45--46. Full selected text and original matching image read.

Proposition 6.1's explicit two-block obstruction has within-block alpha>1 and cross-block one. All quartet conditions reduce to alpha<=2^(q/2). The block-sum complement has eigenvalue -alpha with multiplicity n-2; the remaining quotient has trace alpha(n-2)>0 and determinant alpha^2(a-1)(b-1)-ab. Although written in a nonorthonormal block-constant basis, the quotient is similar to a symmetric matrix and has real eigenvalues. Two positives occur exactly for alpha>sqrt(ab/((a-1)(b-1))). Optimizing ab gives balanced block sizes. The parity-specific simplification and asymptotic are next; no computational check yet.


### BHKL analytic physical pages 47,48

Actual primary reading, sheet 24, physical pages 47--48. Full selected text and matching original-resolution image read.

The two-block proof completes the parity bounds and upper asymptotic 4/((ln 2)n)+O(n^-2), while the existing lower epsilon(n) has the same order. Corollary 6.2 therefore excludes a universal positive q; Conjecture 6.4's exact parity formula remains a source-era conjecture for n>=6. q(4)=2 follows from the exact four-element criterion and obstruction, independently of arbitrary-minor monotonicity.

Section 7 uses all five-vertex quartets: the four remaining vertices form a Ptolemaic metric, improving arbitrary-metric q<=1. The announced four-point exponent log_2(3) and q(5) proof remain unread. Its footnote supplies a concrete author Lean repository, https://github.com/icarm/FourPointPtolemaic.git. This is a candidate formalization source to inspect/pin; no execution or independently checked Lean credit yet.


### BHKL analytic physical pages 49,50

Actual primary reading, sheet 25, physical pages 49--50. Complete selected text and original matching image read.

Definitions 7.1--7.2 separate all-order Ptolemy inequalities from q-negative type on sum-zero coefficients. Lemma 7.3 fixes the factor 1/2 in the based Schoenberg Gram matrix. The proof's bijection a<->c with c_p=-sum a gives the exact quadratic identity c^T E c=-2a^T G a. The semidefinite Gram realization produces distances d^(q/2); the converse and strict/affine-independence equivalences continue next. All finite coordinates and base-point hypotheses are clear, and no arbitrary global metric-space embedding is claimed.


### BHKL analytic physical pages 51,52

Actual primary reading, sheet 26, physical pages 51--52. Complete selected text and original matching image read.

Lemma 7.3 completes the converse Gram realization and strict affine-independence equivalences for every base point. Remark 7.4 assumes the powered distance is itself a metric; then all required two-by-two minors are nonnegative and the three-by-three determinant is the last PSD condition. Its rotation-interval interpretation retains possible degenerate triangles. P(m) is a supremum over all m-point Ptolemaic metrics. Proposition 7.5 begins the exact relation q(n)=P(n-1) by distinguished-row normalization; full two-way argument is next. This is a uniform-support metric correspondence, not arbitrary matroid-minor extension.


### BHKL analytic physical pages 53,54

Actual primary reading, sheet 27, physical pages 53--54. Complete selected text and original matching image read.

Proposition 7.5's matrix/metric correspondence is pointwise in each q>0 in both directions, so the sets of valid universal exponents and their suprema agree; no arbitrary minor-extension assertion is needed. The source phrases the last step using q below the supremum, whose interval property can instead be avoided by stating that exact pointwise equivalence.

Lemma 7.6's line-metric integral proof has the correct negative modulus-square expression; printed 'sum_i c_i0' is an obvious missing equality symbol and must be read as sum c_i=0, not copied. The alternative log-star-shapedness locators are BH Proposition 3.25 and Part 1 Theorem 4.4. Lemma 7.8's inversion fixes p at the origin and inverts only the other nonzero points; I(0) must not be applied to p. Lemma 7.9's proof of the inverted triangle inequalities continues next. Classical fractional-power integral input remains imported until its anchor is checked.


### BHKL analytic physical pages 55,56

Actual primary reading, sheet 28, physical pages 55--56. Complete selected text and matching original-resolution image read.

Lemma 7.9 completes the Ptolemy-to-inverted-triangle calculation. Lemma 7.10's full star inequality proof is read for 1<=q<=log_2 3: m=1/q>=log_3 2, reciprocal symmetry and derivative reduction rho_m(v), then Theta's endpoint zeros and the decreasing Xi with derivative 3(v^2-1)/((2+v)^2(1+2v)^2). The sign change occurs once between Xi endpoint values 1/2 and 1/3. This proves the exact star constant, including zero a/b cases; it is not a numerical approximation. Example 7.11 begins the sharp four-point Ptolemaic fixture with distances 2 on one edge and 1 elsewhere. Its negative-type calculation is next.


### BHKL analytic physical pages 57,58

Actual primary reading, sheet 29, physical pages 57--58. Complete selected text and matching original-resolution image read.

Example 7.11 gives a Euclidean unit-side rhombus at q*=log_2 3 and the exact sum-zero witness w=(1,1,-1,-1), with quadratic 2(2^q-3), excluding every larger q. Lemma 7.12 concerns center plus three leaves (four points), not arbitrary-size tree metrics. Positive leaf lengths permit the diagonal normalization. The star bound gives eta in [0,1], determinant 1-(eta_12^2+eta_13^2+eta_23^2+eta_12 eta_13 eta_23)/4>=0 and all two-minors. Lemma 7.13's concavity is exactly the -C coefficient with fixed remaining entries. Figure 1 and Lemma 7.14 fix the attached-tail distances; proof continues, with a potentially coincident endpoint h=|r-z| handled as a limiting line configuration if needed.


### BHKL analytic physical pages 59,60

Actual primary reading, sheet 30, physical pages 59--60. Complete selected text and matching original-resolution image read.

Lemma 7.14's entire attached-ray proof is read: powered distances remain metric since q/2<1, all two-minors hold, and determinant is concave in h^q. Endpoints are a line configuration (including coincident limiting points) and a center-plus-three-leaves star. Lemma 7.15 assumes P is on AB and the particular Ptolemy bound (y+z)r<=za+yb. After b=1 scaling it fixes the interval max{|a-y|,|1-z|}<=r<=min{a+y,1+z,(za+y)/(y+z)}. Concavity in R=r^q has coefficient -s^q/4; r0=0 gives identical P/O Gram rows, determinant zero. Other endpoint cases remain next; no complete geodesic-insertion proof credit yet.


### BHKL analytic physical pages 61,62

Actual primary reading, sheet 31, physical pages 61--62. Complete selected text and matching original-resolution image read.

Lemma 7.15's full remaining endpoint proof is read. Positive lower endpoints either reduce by relabelled attached-ray lemma or force line equalities through the triangle bounds. Metric upper endpoints force line metrics by the specific Ptolemy bound. At r=r*, inversion at A yields both P--B--O and P--B--A additive distances; the remaining inverted triangle is degenerate, so it is a metric and Lemma 7.14 applies with tail P attached at B. Inversion/Gram equivalence returns q-negative type. Concavity then covers the full r interval. All divisions have positive denominators from distinct-point distances. Theorem 7.16 is stated for every four-point Ptolemaic metric and 0<q<=log_2 3; its main proof is next.


### BHKL analytic physical pages 63,64

Actual primary reading, sheet 32, physical pages 63--64. Complete selected text and original matching image read.

Theorem 7.16 uses Blumenthal for 0<q<=1, then the already proved star/insertion machinery up to log_2 3. Fixing five distances, the full Ptolemaic feasible interval for delta_12 has the exact two triangle lower bounds and absolute Ptolemy-difference lower bound, with the corresponding sum upper bounds. Determinant is concave in delta_12^q. The zero lower endpoint has equal first two normalized Gram rows. Every positive boundary either has a tight triangle (four correctly relabelled insertion cases) or a tight Ptolemy product. The final tight-Ptolemy argument is next; no complete main-proof credit yet. The original positive base distances ensure all displayed denominators exist.


### BHKL analytic physical pages 65,66

Actual primary reading, sheet 33, physical pages 65--66. Complete selected text and matching original-resolution image read.

Theorem 7.16's final tight-Ptolemy case is read: invert at point 3, obtain the geodesic 1--4--2, and the insertion inequality becomes the original triangle bound delta_12<=rho_1+rho_2. All endpoint determinants are therefore nonnegative and concavity completes PSD. Corollary 7.17 combines this exact lower bound with the n=5 two-block upper bound, proving q(5)=log_2 3. The source proof has now been fully read; the author Lean repository is still uninspected/unexecuted and receives no formal-verification credit.

Section 8 explicitly distinguishes strong representations, referring their full definition to [4]. Proposition 8.1's lower inclusion is a direct formal consequence of strong subset weak and the source-scoped positive lower parameter. Reverse strong containment is a separate higher-relation question. Strong membership must not be inferred solely from the local quadratic tests.


### BHKL analytic physical pages 67,68

Actual primary reading, sheet 34, physical pages 67--68. Complete selected text and matching original-resolution image read.

Proposition 8.2's full bivariate obstruction uses a_k=2^{k choose 2}, so local weak T_1 inequalities are equalities a_(k-1)a_(k+1)=2a_k^2. One strong degree-d relation has endpoint product a_0 a_d and d equal products a_1 a_(d-1). Polygon membership demands 2^{d-1}<=d^c, impossible for any fixed positive c as d grows. Exact full support holds here, avoiding Lemma 5.4's standalone omission. Strong-relation definition/indices are an external Part 1/[4] dependency to check; no claim that this particular polynomial is Lorentzian is made. Corollary 8.3 announces the uniform-matroid lift, but its construction/strong implication continues next.


### BHKL analytic physical pages 69,70

Actual primary reading, sheet 35, physical pages 69--70. Complete selected text and matching original-resolution image read after repeating the previously truncated display.

Corollary 8.3 lifts the exact-full-support bivariate weak/strong obstruction via the natural matroid of Delta_d^2, namely U_(d,2d), and Part 1 Proposition 4.8. That lifting equivalence is an external dependency, not verified here. Proposition 8.4 has a complete elementary weak T_q failure under identifying x_5=x_6: two disjoint cubic coefficients c_135=c_246=2^q and all other squarefree coefficients 1 give only triples (1,1,1) or (1,1,2^q) in every relation. After identification, one relation has terms 4,(1+2^q)^2,4; the root-triangle condition would require 1+2^q<=2^(1+q/2), contradicted by (2^(q/2)-1)^2>0 for q>0. This is a weak representation example, with no Lorentzian assertion. Multi-affine input avoids factorial ambiguity; the displayed output relation uses squarefree coefficients as well.


### BHKL analytic physical pages 71,72

Actual primary reading, sheet 36, physical pages 71--72. Complete selected text and matching original-resolution image read.

Proposition 8.5 gives a rank-3, six-element strong T_q example for 1<=q<=2: nonbases 126 and 346 (intersection size one), c_135=2^q, all remaining bases weight 1. The support is a sparse paving matroid. Three-term relations have multisets (1,1,1),(0,1,1),(1,1,2^q); four-term disjoint relations have five displayed multisets, each root-polygon admissible. These finite enumeration assertions should be checked exactly before use. After x_6=x_5, the relevant weak relation has terms 4,2(1+2^q),1; failure of the required root triangle still awaits the inequality proof on the next page. The text says rank-3 multi-affine strong relations reduce to 3/4 terms; exact external strong-definition correspondence remains to be checked in Part 1.


### BHKL analytic physical pages 73,74

Actual primary reading, sheet 37, physical pages 73--74. Complete selected text and matching original-resolution image read.

Proposition 8.5's remaining inequality is valid: convexity gives (1+4^(1/q))^q<=5*2^(q-1), below 2(1+2^q) for 1<=q<2; the endpoint q=2 is directly 9<10. Questions 8.6 and 8.7 are explicitly source-era questions about degree-dependent downward strong preservation and fixed-support strong upper envelopes; they are not additions to the canonical open catalogue or verified current open status. Appendix A introduces strict inertia (1,n-1) for ordinary positive-edge leaf-tree distance matrices and their off-diagonal exponentials. The reduction exponential->ordinary uses tree=ultrametric+lineality and positive diagonal congruence, then monotonicity of exp on off-diagonal ultrametric values. Pending Lemma A.8 and subsequent proofs supply this reduction's premises. Strict CND belongs to ordinary tree distance, not automatically to the unnormalized exponential matrix on the same sum-zero hyperplane.


### BHKL analytic physical pages 75,76

Actual primary reading, sheet 38, physical pages 75--76. Complete selected text and matching original-resolution image read.

Proposition A.3 reduces weak T_0 matroid polynomials to rank-2 contractions, then factors parallel classes before positive linear substitution. Uniform rank-2 tropical max-twice relations for log weights give a tree metric up to lineality; positive diagonal congruence then transfers strict inertia from the exponential distance matrix. Parallel-class factorization is needed even with two/three classes and is not implied by mere positivity of the full multipartite matrix. Rank<2 base cases and loops require the usual derivative conventions. The tree-metric/tropical identification is asserted rather than proved here; exact cited input is still pending. Remark A.4 invokes the prior general M-convex quadratic reduction, whose pure-square boundary case was omitted in the earlier presentation (TH-A06). Definitions A.5/A.6 give strict CND on sum-zero vectors and the ultrametric max-triangle property.


### BHKL analytic physical pages 77,78

Actual primary reading, sheet 39, physical pages 77--78. Complete selected text and matching original-resolution image read.

Lemmas A.7/A.8 prove the tree-to-ultrametric lineality reduction explicitly: extend each leaf to height H=max h_i and choose c_i=h_i-H<=0, giving d_ij=u_ij+c_i+c_j and E_d=diag(exp c_i) E_u diag(exp c_i). Zero extension length is harmless after retaining the original leaf. Rooted lowest-common-ancestor formula gives ultrametricity. Proof #1 invokes Timan--Vestfrid square-root ultrametric Euclidean embedding and additionally affine independence, deferred to explicit construction A.4; Schoenberg criterion then yields strict CND of the normalized matrix. The external theorem's affine-independent conclusion is not simply asserted from an arbitrary embedding. No source dependency [23] has yet been independently read.


### BHKL analytic physical pages 79,80

Actual primary reading, sheet 40, physical pages 79--80. Complete selected text and matching original-resolution image read.

Proof #2 is self-contained: root at an internal/subdivided vertex, map each vertex to sum over root path of sqrt(edge length) times its own edge coordinate. Squared Euclidean distance is tree distance. Every labelled leaf has a positive pendant-edge coordinate absent at other leaves, so the leaf images are linearly, hence affinely, independent. Strict CND on H_0 and a positive all-ones Rayleigh quotient give inertia (1,n-1). Proof #3 introduces splits, with c^T delta_sigma c=-2(sum_{i in A_sigma} c_i)^2 on sum-zero vectors. Positive pendant splits are essential to the strictness assertion; nonnegative arbitrary split combinations alone need not be strict. Proposition A.10's completion follows next.


### BHKL analytic physical pages 81,82

Actual primary reading, sheet 41, physical pages 81--82. Complete selected text and matching original-resolution image read.

Proof #3 completes strictness via every positive pendant split, and inertia via codimension-one negative restriction plus positive Rayleigh quotient. Proof #4 correctly distinguishes full-vertex Bapat--Kirkland--Neumann determinant formula from leaf principal-minor formula attributed to Richman--Shokrieh--Wang; the former alone does not justify the latter. The strict principal-minor signs use positive edge lengths and at least two selected distinct leaves. These determinant identities are externally attributed, not independently checked in this reading. Proof #5 begins resistance-distance strict CND on distinct points of a metric graph; full argument remains next. If integrating the tree statement, the self-contained edge embedding/split proof can avoid importing the determinant dependencies altogether.


### BHKL analytic physical pages 83,84

Actual primary reading, sheet 42, physical pages 83--84. Complete selected text and matching original-resolution image read.

Proposition A.13 uses the metric-graph energy identity r-energy=-2 positive energy on mass-zero signed measures, with distinct point masses yielding strictness. External Baker--Rumely energy and canonical-measure references are not yet independently checked. TH-A07: the wording 'canonical probability measure' needs care: the usual canonical measure on a branched metric tree has negative vertex masses, so it is a signed mass-one measure rather than necessarily positive; the linear energy identity may survive this wording error, but do not import it as a probability claim. Proof #6 introduces strictly Lorentzian positive stratum and logarithmic limit sets. Lemma A.14 is valid under CLOSED log set plus star-shapedness; strict-inertia strata are generally open, so the later application must be checked separately. No strictness follows merely from a closed non-strict cone.


### BHKL analytic physical pages 85,86

Actual primary reading, sheet 43, physical pages 85--86. Complete selected text and matching original-resolution image read.

TH-A08: Appendix proof #6 explicitly applies closedness to the STRICT inertia stratum and asserts squared complex Pluecker absolute values land there. Both require correction: a strict-inertia stratum is not generally closed, and real Vandermonde rank-2 configurations give squared-distance matrices of rank <=3, hence singular for n>=4. Part 1 must be checked for whether its positive-support notation was mistaken for strict Hessian signature. The logarithmic-limit argument can yield a non-strict Lorentzian containment from a closed non-strict stratum but cannot on its own establish nondegeneracy. Do not import proof #6 as written. The already read elementary edge embedding and ultrametric congruence prove the main tree statement independently. References [4]/[5] identify Representation theory of polymatroids, arXiv:2507.14718, and Topological aspects, arXiv:2508.02907; editions still to be pinned before selected dependency reading.


### BHKL analytic physical pages 87,88

Actual primary reading, sheet 44, physical pages 87--88. Complete selected text and matching original-resolution image read.

References and author affiliations read completely. The quantitative embedding input [11] is Faver--Kochalski--Murugan--Verheggen--Wesson--Weston, Roundness properties of ultrametric spaces, Glasgow Math. J. 56(3):519--535 (2014). [15] is Maehara, Euclidean embeddings of finite metric spaces, Discrete Math. 313:2848--2856 (2013). [10] is the 2020 Annals Lorentzian paper already stored in the checked source collection. No reading of these cited works is credited by this bibliography inspection. Full primary edition 2607.15375v2 has now actually been read: 88 physical pages, 44 matching composite images, with sequential notes 01--44. Source archives/Lean repository remain separate from this completed PDF reading scope.


## Selected dependencies

### TOPO physical pages 1,2

Actual dependency reading, sheet 01, TOPO physical pages 1--2. Complete selected text and matching original-resolution image read.

Controlling Part 1 edition is arXiv:2508.02907v3, 10 October 2025, 82 pages. Introductory projective fixed-support homeomorphisms are topology claims and do not identify the coefficient maps or prove analytic threshold containments. Squarefree log-concavity equivalence and general complete log-concavity are background assertions here, not independently proved in these two selected pages. Only the stated selected scope receives reading credit.


### TOPO physical pages 32,33

Actual dependency reading, sheet 02, TOPO physical pages 32--33. Complete selected text and matching original-resolution image read.

Part 1 uses the exponential coefficient convention f=sum c_alpha x^alpha/alpha!, confirmed independently of Part 2. Theorem 4.4 concerns Lorentzian polynomials with fixed exact support and normalized coefficient powers 0<=p<=1; it does not assert closedness of a strict-inertia stratum. It anchors BH Proposition 3.25 and Theorem 3.14 (not freshly read yet). Lemma 4.5 defines V including squares (j=i is allowed), unlike any off-diagonal-only convention; the pure-square edge case needs to be compared to Part 2's own V definition before treating TH-A06 as a substantive omission. The multipartite graph statement includes the single-vertex case, although the prose rank-2-matroid shortcut then needs the trivial separate interpretation. Source typo 'i in J' in D definition should read variable indices. Part 1's all-degenerate-relation assertion is attributed, not promoted as new book work.


### TOPO physical pages 34,35

Actual dependency reading, sheet 03, TOPO physical pages 34--35. Complete selected text and matching original-resolution image read.

Theorem 4.7 supplies the missing parallel-class factorization: every nonzero two-class coefficient block has rank one because all its 2x2 minors vanish under degenerate T_infinity relations; normalized class weights agree across different outside classes by another two-term relation. This explicitly covers the two-class case that Part 2's later shortcut should use first (TH-A04). Nonnegative substitution and representative restriction/scaling give Lorentzian equivalence. Unused variables require care: the printed uniqueness of all lambda_1,...,lambda_n cannot constrain indices outside V; restrict the assertion to active variables or state those weights are immaterial. Pure-square singleton simplification is immediate separately. Corollary 4.10 only identifies a sufficient interior condition relative to the representation variety; it does not claim every fixed-positive-support Lorentzian Hessian is nonsingular.


### TOPO physical pages 36,37

Actual dependency reading, sheet 04, TOPO physical pages 36--37. Complete selected text and matching original-resolution image read.

Lemma 4.11 proves singular positive off-diagonal Lorentzian quadratic matrices lie on the relative boundary, by a perturbation positive on a two-dimensional subspace. Its displayed final coefficient drops an inessential factor two; the sign conclusion is unaffected. The coefficient logarithm is explicitly normalized. Lemma 4.12 correctly removes a bounded nonnegative diagonal without introducing additional positive eigenvalues. Theorem 4.13's log(f) requires a_ii>0 whenever 2e_i is in the fixed exact support; the printed interval [0,1] includes values where that logarithm is undefined. For any use retain 0<a_ii<1 on present squares, and absent squares zero. This additional wording boundary does not affect the positive theta construction in Part 2.


### TOPO physical pages 38,39

Actual dependency reading, sheet 05, TOPO physical pages 38--39. Complete selected text and matching original-resolution image read.

Part 1 treats closedness of the non-strict Lorentzian locus relative to positive exact-support coefficients/log coordinates, not strict Hessian signature. The normalization is explicitly N_t(x^alpha)=x^alpha/(alpha!)^t applied to an already exponential f_J, so exponent t+1 is confirmed. Lemma 4.15 gives the precise derivative rescaling and diagonal theta_i=((a_i+1)/(a_i+2))^t, matching Part 2. Lemma 4.14 cites the generalized BH symbol criterion without proof details, whose source anchor is selected later. Theorem 4.16's strong star-shaped topology is not being imported solely from these selected proof pages because its Section 2 topological inputs were not read. Rank-one all-ones matrix's nonzero eigenvalue is squared norm, not norm as prose says; only positivity versus 1 is used and is unaffected.


### TOPO physical pages 40,41

Actual dependency reading, sheet 06, TOPO physical pages 40--41. Complete selected text and matching original-resolution image read.

Corollaries 4.21/4.23 are homeomorphisms, not equalities of coefficient loci. Most decisively, Part 1 Theorem 5.1 maps squared complex absolute values into the NON-STRICT Lorentzian/stable locus and explicitly puts real U_2,4 (and complex U_2,5) images on its boundary. This confirms Part 2 Appendix proof #6's claim of a STRICT target is a source mismatch (TH-A08), rather than a theorem of the cited Part 1. Only the statement has been read here, not its later proof, and the book will not claim a fresh complete proof audit of Theorem 5.1. Selected Topological dependency scope is now pages 1,2,32--41: 12 pages, 6 images.


### POLY physical pages 1,2

Actual dependency reading, sheet 07, POLY physical pages 1--2. Complete selected text and matching original-resolution image read.

Controlling Representation theory edition is arXiv:2507.14718v2, 17 September 2025, 90 pages. The title is 'for polymatroids', correcting Part 2's reference wording 'of'. Contents show representation definitions on pages 33 onward; the prepared selection omitted pages 33--34, which must be added in a separate supplemental preparation before importing the strong definition. The canonical tract/foundation and embedding assertions in the abstract remain attributed summaries, not independently audited full-paper claims.


### POLY physical pages 17,18

Actual dependency reading, sheet 08, POLY physical pages 17--18. Complete selected text and matching original-resolution image read.

Finite nonempty M-convex sets have coordinate infimum/supremum delta^-/delta^+; translation and reflection preserve exchange when the result stays nonnegative. The refined dual delta_J-J is involutive and differs from ordinary matroid complement when loops/coloops are present. Proposition 2.6 correctly restricts its agreement to no isolated elements (loops/coloops); its proof has a second delta^- typo that should be delta^+. These normalization details corroborate that repeated-index representation bounds must use the fixed support's coordinate extrema rather than an arbitrary ambient simplex.


### POLY physical pages 19,20

Actual dependency reading, sheet 09, POLY physical pages 19--20. Complete selected text and matching original-resolution image read.

Definitions 2.9/2.10 fix reduced support and effective independence via mu<=alpha-delta^-. Embedded contractions/deletions inject into J; no surjectivity or extension of arbitrary minor representations follows from these injections. The sentence comparing effective independence to mu-delta^- independence seems inconsistent with its preceding definition, and the displayed exchange proof has variable/sign typos. Do not import these prose formulas uncorrected; they are not load-bearing for the proposed rank-2/normalization section. Figure 1 was inspected. Any asserted representation descent remains distinct from threshold monotonicity quantified over all minor representations.


### POLY physical pages 35,36

Actual dependency reading, sheet 10, POLY physical pages 35--36. Complete selected text and matching original-resolution image read.

Definition 4.3 is here in full, so the earlier sheet 07 concern about needing 33--34 specifically for the strong definition is RESOLVED without a supplemental scope. A representation uses effective rank r-|delta^-| and reduced support, exact nonzero support (SR1/WR1), permutation sign, and coordinate-width bounds. In T_q, -1=1 removes signs. For squarefree rank 3 on six nonisolated elements the bound excludes repeated union indices, so all nontrivial strong relations are exactly common-element five-point 3-term relations and six-point 4-term relations; the diagnostic's 30 three-term plus 15 four-term checks therefore cover the full definition. A weak local relation identity without exact M-convex support is not a representation, corroborating TH-A03. Translation recovers the vector formulation used by Part 2.


### POLY physical pages 37,38

Actual dependency reading, sheet 11, POLY physical pages 37--38. Complete selected text and matching original-resolution image read.

Lemma 4.6/Proposition 4.7 explain why repeated support exponents force -1=1 for proper polymatroids, with a near-idempotent relation and width>=3 forcing the three-unit relation. Definition of the up operator copies labels into the natural matroid but vanishes on repeated lifted elements. Proposition 4.8 states the equivalence of both weak and strong conditions under this operator for a function already satisfying exact-support and permutation axioms; its complete proof remains next. This matches precisely the dependency used to lift Part 2's positive bivariate obstruction to U_(d,2d), without assuming arbitrary downward substitution preservation.


### POLY physical pages 39,40

Actual dependency reading, sheet 12, POLY physical pages 39--40. Complete selected text and matching original-resolution image read.

Proposition 4.8 full proof checks both directions: every distinct-lift relation projects to a permitted width-bounded relation, and every width-bounded tuple admits a distinct lift by the available copy counts. This clears the up-operator weak/strong dependency used in Part 2 Corollary 8.3 for the explicit two d-element blocks. The vector formulation uses exact support and delta^-<=alpha plus total union<=delta^+; all signs disappear over T_q. Perfect=>excellent imports an external matroid theorem, not needed for the proposed book integration. Lemma 4.10's arbitrary-tract proof continues on unselected page 41 and is not claimed fully read; its near-idempotent case is already established by the complete preceding discussion. Selected POLY scope 1,2,17--20,35--40 now completed, 12 pages/6 images.


### FAVER physical pages 1,5

Actual dependency reading, sheet 13, FAVER physical pages 1 and 5. Complete selected text and matching original-resolution image read.

Published controlling edition: Glasgow Mathematical Journal 56 (2014), 519--535, DOI 10.1017/S0017089513000438; accepted 28 May 2013, online 13 August 2013. Author list and journal title/page metadata verified. Negative type and generalized roundness use sum-zero/balanced-mass conditions; strictness is distinct. Theorem 2.11 is a recalled equivalence rather than a new proof in these pages; its external references are not cleared by reading the statement. The intended quantitative embedding anchor is later Theorem 3.6, not the abstract's general ultrametric claim.


### FAVER physical pages 6,7

Actual dependency reading, sheet 14, FAVER physical pages 6--7. Complete selected text and matching original-resolution image read.

Lemma 3.2 proves the exact Gram identity 2 eta^T A_p eta=-eta_*^T D_p eta_* under eta_0=-sum eta_j. Theorem 3.3 and Corollary 3.4 relate strict negative type to affine independence and minimal Euclidean dimension; the latter restricts 0<=p<=2 so d^(p/2) is a metric, with p=0 interpreted as the off-diagonal equilateral metric. The Gram criterion can also be proved directly by finite-dimensional positive-semidefinite factorization, so its use does not require accepting a recalled citation on faith. The quantitative threshold is not yet read.


### FAVER physical pages 8,9

Actual dependency reading, sheet 15, FAVER physical pages 8--9. Complete selected text and matching original-resolution image read.

Published Theorem 3.6 locator cleared: n+1 points, n>1, threshold wp=log_2(1+1/n), 0<=p<wp STRICT endpoint, Euclidean dimension n and no smaller. Applied to m=n+1 remaining points this gives eta(m)=log_2(1+1/(m-1)), hence Part 2 lower threshold log_2(1+1/(N-2)) after deleting one distinguished point from N. Endpoint containment in Part 2 comes by a limit and only non-strict Lorentzian signature; never attribute an endpoint affinely independent embedding to Faver et al. The published proof is a reduction to earlier Deza--Maehara/Weston bounds and Li--Weston strictness; those earlier papers were not freshly read. Selected FAVER scope 1,5--9 is completed (6 pages/3 images), not the entire 17-page paper.


### BH physical pages 14,15

Actual dependency reading, sheet 16, BH physical pages 14--15 (printed 834--835). Complete selected text and matching original-resolution image read.

Published Theorem 2.10: any nonnegative rectangular linear substitution preserves the Lorentzian class, including zero output. Its proof reduces to splitting, dilation (zero included), and identifying variables, with M-convex support checked before closure. Corollary 2.11 gives nonnegative directional derivatives. This supplies the exact substitution input used in parallel simplification and contrasts with Part 2's weak/strong representation failures under downward aggregation. Lemma 2.12's proof begins and continues outside this sheet, so no completed audit of that smoothing lemma is claimed here.


### BH physical pages 16,30

Actual dependency reading, sheet 17, BH physical pages 16 and 30 (printed 836 and 850). Complete selected text and matching original-resolution image read.

Lemma 2.12 proof completes on page 16, but Theorem 2.13 continues beyond selected page, so no full closure-proof reading is credited. Published Theorem 3.2 exact signature: homogeneous linear operator T on coordinate-degree-bounded polynomials R_kappa, degree shift ell, symbol sum binom(kappa,alpha) T(w^alpha) u^(kappa-alpha), Lorentzian symbol implies T preserves the Lorentzian class. This is the normalization-preservation input; product bivariate factorial-log-concave symbols are applicable with finite degree bounds. Polarization discussion distinguishes coefficient-normalized polarization from raw copying of polymatroid representation weights.


### BH physical pages 31,32

Actual dependency reading, sheet 18, BH physical pages 31--32 (printed 851--852). Complete selected text and matching original-resolution image read.

Theorem 3.2 proof read through completion: polarization reduces to multi-affine symbols, multiply symbol by f in separate variables, apply the two-variable contraction operator for every pair, then set auxiliary variables zero to obtain T(f). It uses product preservation, polarization, and Lemma 3.3, whose displayed proof was also read. The symbol condition is sufficient, not necessary: the paper supplies a preservation operator with a non-M-convex symbol. Theorem 3.4 proof begins outside the proposed import scope and continues later; no full proof credit from this sheet alone.


### BH physical pages 33,34

Actual dependency reading, sheet 19, BH physical pages 33--34 (printed 853--854). Complete selected text and matching original-resolution image read.

Published Corollary 3.7 and full proof explicitly define normalization on raw monomials and factor the binomial symbol into bivariate factors whose normalized coefficients 1/k! are log-concave. Replacing by (1/k!)^t for t>=0 is the direct formal extension stated in Part 1 Lemma 4.14/Part 2 Remark 5.17, not an original theorem claim. The converse of N preservation fails, as source notes. Corollary 3.5 gives multi-affine-part preservation; its stable-polynomial input is externally cited. Corollary 3.8 proof starts here and continues next; it is not an independent new claim in the book.


### BH physical pages 35,36

Actual dependency reading, sheet 20, BH physical pages 35--36 (printed 855--856). Complete selected text and matching original-resolution image read.

Published Theorem 3.10 statement cleared: nonempty M-convex support J iff its exponential generating function sum x^alpha/alpha! is Lorentzian; squarefree case is matroid basis support. The proof begins with the quadratic 0/1 matrix classification and continues on unselected page 37, so only statement/partial proof reading is credited. This supplies an attributed standard background input, including the constant-weight polynomial used in the still-UNVERIFIED PG(2,3) source-objection candidate. It does not alone settle all weak representations. Corollary 3.8 completes before the matroid section and uses the operator symbol criterion. The Markov-chain discussion is background, not proposed new book scope.


### BH physical pages 45,46

Actual dependency reading, sheet 21, BH physical pages 45--46 (printed 865--866). Complete selected text and matching original-resolution image read.

Published Proposition 3.25 is exactly normalized coefficient powering R_p, 0<=p<=1, preserving Lorentzian polynomials. The proof reduces via quadratic characterization/nonnegative substitutions to Lemma 3.24. Its lemma statement is on unselected preceding page 44 and needs supplemental reading if used for a detailed proof explanation. This supplies the lower-q preservation route after a sharp q* rank-2 result, avoiding an unchecked Blumenthal citation for 0<q<1. The valuation polarization/projection paragraph is an attributed background operation and is not a claim that ordinary coefficient aggregation preserves hyperfield relations. Initial BH selected scope 14--16,30--36,45--46 now completed, 12 pages/6 images; no complete 71-page reread claimed.


### BH physical pages 26,27

Actual supplemental dependency reading, sheet 01, BH physical pages 26--27 (printed 846--847). Complete selected text and matching original-resolution image read.

The bivariate characterization has no internal zeros and ultra log-concavity in ordinary coefficient convention, equivalent to log-concavity after binomial/exponential normalization. Product preservation Corollary 2.32 and its full displayed proof are read. Theorem 2.30's complete/strong log-concavity equivalence is stated, with proof continuing later and not credited as fully read. Theorem 2.25's actual statement is on the preceding physical page 25, not 26; an additional single-page selection is required for that exact anchor. The current pages do not falsely clear the earlier missing locator.


### BH physical pages 37,44

Actual supplemental dependency reading, sheet 02, BH physical pages 37 and 44 (printed 857 and 864). Complete selected text and matching original-resolution image read.

Theorem 3.10 proof now completed for the intended M-convex=>generating-polynomial Lorentzian direction: normalized quadratic derivatives have 0/1 Hessian coefficients, classified as an all-ones form minus disjoint class squares; derivative criterion completes the argument, with degree 0/1 immediate. Other equivalence directions use earlier external/internal inputs, not a fully audited independent reconstruction. Lemma 3.24 is explicitly for matrices with ALL entries strictly positive, and gives one positive eigenvalue under entry powers 0<=p<=1; its proof was read on dependency sheet 21. Zero diagonal rank-2 use should invoke Proposition 3.25, whose reduction/limits handle boundary zeros, not apply Lemma 3.24 directly to a zero-diagonal matrix. The tree statement on this page only asserts non-strict inertia and does not settle Appendix six's strict gap.


### BH physical pages 25

Actual final-locator dependency reading, sheet 01, BH physical page 25 (printed 845). Complete selected text and matching original-resolution image read.

Published Theorem 2.25 and the immediately following quadratic-derivative characterization are now directly read and locator-cleared: the Lorentzian class is the closure of the strictly Lorentzian class, is closed in fixed homogeneous degree, and is characterized by nonnegative coefficients, M-convex support, and all degree-two partial derivatives having at most one positive eigenvalue. Example 2.26 gives ultra log-concavity/no internal zeros, matching the next page's bivariate statement. This is the non-strict closure used in analytic threshold endpoint limits; it does not imply the strict-signature subset is closed. Supplemental BH scope now adds pages 25,26,27,37,44 to the initial 12 distinct BH pages.


## Focused rereading of four already counted primary pages

No additional distinct pages or whole-book reread credit.


Actual focused primary rereading, sheet 18, physical pages 35--36. Complete selected text and matching original-resolution image read again after the Part 1 dependency check. This is a reread of already credited primary pages, not additional distinct primary pages.

Part 2's simplification proof correctly references Part 1 Theorem 4.7. Lemma 5.10 uses the off-diagonal-index set V(K) and only promises equality of positive indices; kernel directions add zeros. To settle the pure-square support scope one must inspect the actual V(K) definition on the preceding page 34; this sheet alone does not settle TH-A06. Weighted-copy lemma's singleton support is allowed provided the simplification index exists; the unqualified small-size uniform reduction can be handled separately.


Actual focused primary rereading, sheet 17, physical pages 33--34. Complete selected text and matching original-resolution image read again after dependency checks. This repeats already credited pages and adds no distinct primary pages.

TH-A06 CONFIRMED as a boundary omission: Part 2 explicitly defines V(K) using j!=i, whereas Part 1 includes squares. If K={2e_i}, then V(K) is empty and the asserted simplification support on Delta_0^2 cannot represent it. This case is a single positive rank-one quadratic and is handled directly, so the main sandwich statement is not thereby disproved. For any nonsingleton nonempty quadratic M-convex K with a square, exchange forces an off-diagonal term and the active variable is in V(K). TH-A05 is also exactly located at Remark 5.7: the quantified arbitrary-minor threshold assertion is justified only by descending representations, without extension of arbitrary minor representations. The finite PG(2,3) rank diagnostic is retained as an UNVERIFIED original candidate; do not use it as a promoted book theorem. A proof via rank-2 contractions can support the intended lower bound without importing arbitrary-minor monotonicity.

