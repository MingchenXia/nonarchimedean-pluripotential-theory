# Actual Reboulet–Witt Nyström revised source notes, 9 October 2026

Complete pinned v2: 19 physical pages in ten individually displayed matching views.

---

# Reboulet Witt Nystrom flats actual primary view 01

UTC: 2026-10-09T03:30:28.129778+00:00. Physical pages: 1, 2.

Read the complete selected text and displayed matching rendered image.

Physical pages 1–2 begin Reboulet–Witt Nystrom, Infinite-dimensional flats in the space of positive metrics on an ample line bundle, pinned arXiv 2311.13451v2, 29 October 2025, 19 pages. The controlling setting is a projective complex manifold and an ample line bundle, with continuous or bounded positive metrics. This is not a theorem over arbitrary non-Archimedean fields. The source constructs Lp-isometric flat cones from convex decreasing functions attached to a bounded filtration; the actual domain/support convention and proof remain to be read. The arXiv metadata says this revision fixes a referee-identified support issue; metadata alone supplies no proof credit.

The introductory quantization uses Hermitian L2 norms and Fubini–Study potentials k^{-1} log sum |s_i|^2. This squared-norm convention must be calibrated against the finite logarithmic norm ratio and against the book's probability/volume conventions. The displayed filtration measures use k^{-n} times the sum of Dirac masses, not the probability normalization by h0(kL). Their asymptotic mass is the Hilbert leading coefficient; the later distance/Monge–Ampere normalization needs to agree with it.

The initial claims about Darvas completions and Busemann convexity cite external primary results, rather than establish them in these pages. The definition of 'flat' here permits isometric subsets of real vector spaces and does not impose the 2026 source introduction's strict convexity condition. The scope distinguishes ordinary Hermitian quantization from trivially valued filtration norms. It does not identify their scalar homogeneity categories.

No primary result is yet imported into the active book, no whole-paper reading claim is made by this first two-page note, and no canonical problem status or independent model receipt is changed.

---

# Reboulet Witt Nystrom flats actual primary view 02

UTC: 2026-10-09T03:31:01.394330+00:00. Physical pages: 3, 4.

Read the complete selected text and displayed matching rendered image.

Physical pages 3–4 explicitly describe the support repair: first define the construction for convex decreasing f on all of R, then approximate functions on the limiting DH support by globally defined functions and extend using metric completeness. This is an additional procedure absent from the literal finite-degree formula in the 2026 filtration paper. Its actual proof in §2.2 and §3 remains to be checked; the introduction cannot by itself settle finite-degree evaluation or representative independence.

The modified FS expression uses squared section lengths multiplied by exp(-k f(lambda/k)). The corresponding Hermitian norm weights must therefore have logarithmic shift k f/2 if the norm denotes the square root of the L2 integral. Later conventions need checking before asserting the displayed dp equality. The limiting DH mass is still degree-volume normalized, not assumed probability normalized.

The introductory filtration-to-norm display sets the norm equal to the supremum of filtration indices. That is a weight, potentially zero or negative, and not a positive definite ultrametric norm. The usual positive norm is exp(-sup lambda); the body must fix the sign and exponential. The introductory assertion that every bounded filtration gives an infinite-dimensional cone also needs a nontrivial spectral-support qualification: a scalar filtration has a singleton support and only a one-dimensional function cone.

Uniform approximation of every bounded convex decreasing function by global convex functions requires an endpoint-continuity convention. A bounded convex function on a closed interval can jump at the left endpoint: f(0)=1 and f(x)=0 for x>0 on [0,1] is convex and decreasing but not continuous, so cannot be a uniform limit of continuous restrictions. This diagnoses the literal introductory phrasing only. The source may use a more precise function class or Lp/completeness argument in the body, which is not yet reviewed.

The main theorem is stated for a continuous positive initial metric on an ample line bundle over a compact projective complex manifold. Finski's quantization/isometry inputs are explicitly external. This partial reading supplies no imported general theorem, canonical problem resolution or independent-model receipt.

---

# Reboulet Witt Nystrom flats actual primary view 03

UTC: 2026-10-09T03:31:38.540166+00:00. Physical pages: 5, 6.

Read the complete selected text and displayed matching rendered image.

Physical pages 5–6 give finite complex spectral distances, sequence pseudodistances and the initial quantization formulas. Successive minima are logarithms of norm ratios, not logarithms of squared Gram eigenvalues; for Hermitian norms they are half the log Gram eigenvalues. The probability normalization is 1/N. The relative signed mean is consistent with this convention, and the finite Hermitian maximum identity (1.4) follows in a common orthogonal basis.

The displayed 'unique geodesic' formula in Proposition 1.1 is a sum of absolute coordinates times interpolated norm weights. That is a weighted l1 norm, not a Hermitian norm. In rank two with equal standard Euclidean endpoints it gives |a|+|b|, differing from sqrt(|a|^2+|b|^2) already at t=0 and t=1. The corrected Hermitian formula is the square root of the sum of |c_i|^2 times the squared interpolated weights. This is a direct endpoint/type diagnostic, not a denial of the usual Hermitian geodesic theorem.

Section 1.2 defines sequence distances and volumes by limsup. Formula (1.5) cannot hold for arbitrary relatively bounded sequences merely by passing the finite identity to limsup. Take eta_k any Hermitian norm on H0(P1,kO(1)) and xi_k=exp((-1)^k k) eta_k. The left normalized d1 is always 1. The two normalized distances to the Hermitian maximum alternate between 1 and 0, so each limsup is 1 and the printed right side is 2. The signed volume limsups in opposite orders are both 1 as well. An actual common limit or a restricted submultiplicative convergence setting is needed before using a signed cocycle or the asymptotic maximum identity. This example is for the literal arbitrary-sequence definition and does not challenge an applicable theorem for submultiplicative sequences with established limits.

The opening L2 expression on page 6 prints |s| rather than |s|^2 inside a formula for the squared norm; literal scalar scaling would not be quadratic. Its sup-norm exponent must also be checked against the squared-metric convention and the later FS definition. The finite norm contraction/metric claims are cited to BE21 and Fin23, whose precise Archimedean hypotheses are separate primary inputs.

These actual two-page observations remain ordinary source diagnostics, with no active book change, original general theorem, canonical status change or independent-model receipt.

---

# Reboulet Witt Nystrom flats actual primary view 04

UTC: 2026-10-09T03:32:33.651074+00:00. Physical pages: 7, 8.

Read the complete selected text and displayed matching rendered image.

Physical pages 7–8 define the quotient FS metric, cite the quantization isometries and give a genuine bounded graded class. Definition 1.3 compares a submultiplicative norm sequence with sup norms coming from a bounded positive metric. Unlike the unrestricted comparator in the 2026 paper, this is a meaningful independent reference. Bernstein–Markov equivalence is normalized infinity distance zero, with uniform bounds C_epsilon exp(epsilon k); Proposition 1.7 correctly aims to preserve the regularized FS limit under this o(k) perturbation. Its proof can use the quotient-norm comparison for all genuine norms, not just the Hermitian subspace named in the last sentence.

Several literal quantization conventions are inconsistent. Formula (1.6) has exp(-2 ||v_i||) rather than ||v_i||^{-2}=exp(-2 log ||v_i||). With an orthonormal basis the displayed exponential contributes an unwanted factor exp(-2). The preceding quotient norm on kL gives the standard potential log sum |v_i|^2/||v_i||^2. The subsequent finite-to-asymptotic convergence display and the final FS operator display omit the degree division k^{-1}, although the Fekete paragraph and Proposition 1.7 use it. These must be reconciled before use.

Under the introduction's squared metric potential, shifting the potential by c multiplies Hermitian L2 norm lengths by exp(-kc/2). The printed sup-norm definition on page 6 instead multiplies them by exp(-kc). Thus the two normalized finite distances in Theorem 1.2 differ already for a constant metric shift. The MA mass convention also needs to match probability-normalized finite distances and the k^{-n} DH mass. For the squared FS potential the norm comparison gives potential change 2C/k, not an unqualified constant-one formula in every degree. This does not disprove a consistently calibrated Finski quantization theorem; the original Fin22 input must be checked separately.

The explicit Ep characterization requires full non-pluripolar MA mass in addition to the pth integrability condition. Without full mass, a logarithmic section-pole metric on P1 can have non-pluripolar MA measure zero and hence finite integral against that zero measure, while it does not lie in the Darvas finite-energy completion. That premise is not present in the literal short display. The original Darvas definition is the controlling external input.

The useful Fekete mechanism is superadditivity followed by usc regularization, not monotonicity of the full degree-averaged sequence. Its raw limit may differ from its regularization, as the already reviewed NA example illustrates. This checkpoint establishes only actual pages 7–8 and ordinary diagnostics, with no book or canonical-status change and no independent-model receipt.

---

# Reboulet Witt Nystrom flats actual primary view 05

UTC: 2026-10-09T03:33:26.214277+00:00. Physical pages: 9, 10.

Read the complete selected text and displayed matching rendered image.

Physical pages 9–10 give a properly bounded trivially valued graded-norm class and, importantly, the actual support-domain repair. The ground field for this construction is C with its trivial absolute value. Every finite-dimensional norm has an adapted orthogonal basis; this exact fact does not transfer to arbitrary norms for a nontrivial absolute value. The graded bound is explicitly exp(-delta k) times the trivial norm <= F_k <= exp(delta k) times the trivial norm. Thus it is not the vacuous unrestricted-reference definition in the 2026 paper. The filtration norm has basis weights exp(-a_i), correcting the introductory omission of the exponential.

The normalized spectral arguments in the construction are -log F(s_i)/k. Section 2.2 explicitly acknowledges that some finite arguments can lie below the limiting support [a,b]. For f with bounded right derivative, it extends f affinely below a, with slope f'_+(a), to a fixed segment containing all arguments. The source says this extension is always implicit thereafter. This supplies a real, separately stated convention that was not spelled out in the 2026 norm formula. Its explanation accidentally writes positive log F/k when referring to the negative-log spectral arguments; the sign must follow the actual measure and construction formula.

The stated claim that extension values do not affect asymptotics needs its precise topology: finite-p spectral probabilities with common bounded interval and continuous extensions can ignore values on a limiting-null part; the strong infinity metric does not generally ignore rare spectral outliers. The earlier exp(k) constant-monomial example detects this distinction. The arbitrary-derivative case is deferred to a completeness/approximation procedure later in the main theorem, not claimed by the finite-degree formula alone.

Example 2.1 correctly maps f=0 to the trivial norm and f(x)=-x to the original norm. The measure display uses k^{-n} total mass, so no probability normalization can be silently assigned. BC11/CM15 convergence and BHJ17 Corollary 5.4/Remark 5.5 are the cited original inputs for support and finite spectral bounds; their actual hypotheses remain separate dependencies. No new general theorem or independent model receipt is asserted.

---

# Reboulet Witt Nystrom flats actual primary view 06

UTC: 2026-10-09T03:34:03.363584+00:00. Physical pages: 11, 12.

Read the complete selected text and displayed matching rendered image.

Physical pages 11–12 prove Theorem 2.2's submultiplicativity and begin the finite complex rescaling construction. With the extension already supplied on a common spectral interval, the algebraic proof is sound: if alpha=-log F_m(u), beta=-log F_n(v), then every nonzero coefficient of their product in an adapted basis has weight delta_j>=alpha+beta. Decreasing f and Jensen's inequality give (m+n) f(delta_j/(m+n)) <= m f(alpha/m)+n f(beta/n). Taking the maximum proves the required product bound, and the ultrametric inequality extends it to arbitrary sections. Several intermediate left sides omit the new f subscript; they must refer to the modified norm, as their right sides show. A zero product is handled directly before taking its logarithm.

The boundedness constant must be sup |f| on the full extended finite spectral interval, or another nonnegative two-sided bound. The displayed C=sup f fails for a negative constant f, when exp(-Ck) exceeds exp(Ck). The substantive conclusion still follows from boundedness of the extension. The common adapted-basis formula is intrinsically determined by the original norm levels: for a nonzero vector it applies the increasing transform r -> exp(k f(-log r/k)) to F(v), so it is independent of the adapted basis. This is a direct explanation of the existing construction, not a new general theorem.

The last flat-dimension sentence still needs a non-singleton support premise. Its strict-convexity observation is explicitly for p>1 here, correctly distinguishing it from L1. The complex apartment has the probability-normalized l_p metric, including N^{-1/p}; it is not the unnormalized counting-norm metric. The finite rescaling multiplies norm lengths by exp(-a_i), and the NA gauge uses the same exponential values. The general non-Hermitian envelope construction on the next page must be checked against these signs.

This is a qualified ordinary proof/interface review. No active book change, independent hostile-model receipt or canonical status change is claimed.

---

# Reboulet Witt Nystrom flats actual primary view 07

UTC: 2026-10-09T03:35:14.449134+00:00. Physical pages: 13, 14.

Read the complete selected text and displayed matching rendered image.

Physical pages 13–14 define the complex sum-envelope and prove its graded product property. The infimum over decompositions of sums of eta(w_i)F(w_i) is a genuine complex norm: finite positive bounds on F compare it above and below with eta, and the sum infimum gives homogeneity and the triangle inequality. This sum-envelope differs essentially from the ultrametric maximum-envelope in the 2026 paper.

The paragraph claiming exact equality of this sum-envelope with the weighted Hermitian norm in an adapted basis is false literally. On C^2, take eta(a,b)=sqrt(|a|^2+|b|^2), and the trivially valued F with basis weights (1,sqrt(2)): F(a,b)=1 if b=0 and a!=0, otherwise sqrt(2) for b!=0. The weighted Hermitian norm is H(a,b)=sqrt(|a|^2+2|b|^2). At w=(1,1), H(w)=sqrt(3). The sum-envelope A(w) is exactly 2. The one-piece decomposition gives A(w)<=eta(w)F(w)=2. For every vector, the linear functional ell(a,b)=a+b is dominated by the product gauge: on b=0 this is |a|; otherwise Cauchy–Schwarz gives |a+b|<=sqrt(2)eta(a,b). For every decomposition its absolute value is therefore bounded by the summed gauges, giving A(w)>=|ell(w)|=2. The same value holds at (1,-1), so the envelope is not Hermitian (its parallelogram squares give 8 versus 6). This is a counterexample to the printed finite equality, not the asymptotic main theorem.

A correctly typed approximation suffices for the later argument. For an eta-orthogonal, F-adapted basis, the weighted Hermitian norm H is bounded by the product gauge and hence H<=A. Coordinate decomposition and Cauchy–Schwarz give A<=sqrt(N)H. Comparing a second complex base norm with eta adds its d_infinity error through envelope monotonicity/scalar covariance. Thus a logarithmic-rank estimate such as Lemma 3.1, rather than exact equality, is the proper interface. Polynomial rank growth makes log(N_k)/k tend to zero.

The product proof in Theorem 3.2 is a valid mechanism after restoring the missing sums: take decompositions u=sum u_q and v=sum v_r, use the products u_q v_r, sum their costs, and factor that double sum into two sums before taking infima. The rendered proof omits these sum signs and an f subscript in several places; they cannot be read as a single arbitrary cost. Submultiplicativity of both genuine and trivially valued input norms supplies the needed product bound. Bernstein–Markov transfer then uses Lemma 3.1 and the o(k) rank error.

Formula (3.2) shifts Hermitian norm lengths by exp(kf). Under the squared FS convention it produces exp(-2kf) section weights, whereas the introductory modified FS formula uses exp(-kf). Remark 3.4's literal identification thus needs a factor-two calibration. The proof remains an attributed, qualified construction with separate Fin22 quantization inputs. No active book or canonical status change or independent-model receipt is claimed.

---

# Reboulet Witt Nystrom flats actual primary view 08

UTC: 2026-10-09T03:36:36.636694+00:00. Physical pages: 15, 16.

Read the complete selected text and displayed matching rendered image.

Physical pages 15–16 prove Theorem 3.5 and begin the research discussion. The common-basis spectral calculation has three separate literal issues. The distance raised to p must be divided by k^p, not by k; its slopes are k(g-f). The empirical probability average 1/N_k is not equal to the k^{-n} DH integral defined earlier: the conversion factor is k^n/N_k. Finally the finite integral must range over the full finite spectral interval with the prescribed extensions, not S alone when finite eigenvalues lie outside S. Weak convergence then gives the finite-p integral limit for continuous bounded extensions; it does not repair these finite identities automatically.

The approximation argument here is explicit: replace f on [a,a+epsilon] by the chord from f(a) to f(a+epsilon), obtaining convex decreasing functions with finite right derivative and decreasing them toward f. For continuous f at a this is a uniform approximation, and for a bounded endpoint-jump function it can give Lp approximation but not the claimed uniform approximation. Lp identifies functions differing on a null endpoint. For the standard P1 divisorial filtration the DH law is Lebesgue measure on [0,1]; f(0)=1, f(x)=0 for x>0 and g=0 are distinct pointwise bounded convex decreasing functions with Lp distance zero. The final injectivity claim therefore requires an a.e. quotient or a suitable continuous/semicontinuous representative convention. This diagnoses the literal function-set formulation, not a corrected Lp-space isometry.

Darvas completeness gives a finite-p completion limit, but increasing bounded approximants by itself does not imply a bounded limit. A uniform bound is needed. The canonical affine extensions of the chord approximants can have increasingly negative left slope and therefore increasingly large values below a; their order there differs from their order on S. A possible repair must first prove extension-independence using the calibrated finite-p FS isometry, then establish order on S via compatible extensions and compare to constant functions. The source only says order reversal and increasing approximation imply boundedness, without displaying that uniform support-based bound. The preceding imported quantization theorem, with corrected factors and exact scope, is essential to such a repair.

The discussion relates a divisorial filtration to the first-coordinate Okounkov Chebyshev transform, and cites Ross–Witt Nystrom Theorems 8.1 and 8.3 for a partial moment map. Its formula adding f to a multivariate Chebyshev function means f composed with first-coordinate projection. The MA versus Lebesgue mass convention must also be retained there. These external source locators have not been primary-audited in this checkpoint. The apartment/building question continues on the next page; no new canonical atom is added at this point.

No original general theorem or independent model receipt is claimed, and the active book and canonical statuses stay unchanged.

---

# Reboulet Witt Nystrom flats actual primary view 09

UTC: 2026-10-09T03:37:36.279427+00:00. Physical pages: 17, 18.

Read the complete selected text and displayed matching rendered image.

Physical pages 17–18 finish the discussion and give most references. The source asks whether any two continuous positive metrics on an ample line bundle lie in the image of one common filtration flat-cone embedding. This remains a source-stated research question, not a theorem and not a newly settled canonical atom. The discussion also proposes extensions to big classes, prescribed singularities and compact Kahler classes, while explicitly acknowledging missing quantization/DH inputs. It asks how a whole convex-function cone appears in a metrized toric degeneration. These are related directions for the book's research ledger, with no blanket claimed extension.

The toric sentence needs a multiplicative monomial-basis premise, not just multiplicativity of the original scalar filtration norm. Theorem 2.2 still used decreasing f to compare every product coefficient's weight delta_j with alpha+beta. Multiplicativity only makes the smallest delta_j equal alpha+beta; other coefficients can have higher weight. A direct diagnostic: on C[X0,X1] with original F equal to exp(-ord_{X1}), use the adapted degree-one basis (X0+X1,X1) and the usual monomial adapted basis in degree two. The original F is multiplicative. With the increasing convex f(x)=x, the modified degree-one norm of X0+X1 is 1, whereas its square has modified degree-two norm exp(2), because the X1^2 coefficient is nonzero. Submultiplicativity fails for this arbitrary adapted-basis choice. With actual toric monomial bases, monomial products have a single additive weight, and Jensen's inequality gives the appropriate convex-function construction. This distinguishes the intended toric setting from an unsupported basis-free inference.

The references pin Fin22 here to arXiv 2210.03039, Submultiplicative norms and filtrations on section rings, and Fin23 to arXiv 2305.15300. They are different from the Fin22 key in the 2026 paper, which denotes arXiv 2209.03853. Exact theorem locators must follow the source-specific key and version. The already known 2025 PLMS publication of 2210.03039 is not automatically the controlling edition for these cited Lemma 2.8/Corollary 3.6 locators. Darvas 2015, BHJ17 and Ross–Witt Nystrom 2017 are bibliographically identified but not newly recursively audited by reading the reference list.

This actual two-page review adds source-qualified research directions and a direct basis-scope diagnostic, with no active book change, canonical inventory change or independent-model receipt.

---

# Reboulet Witt Nystrom flats actual primary view 10

UTC: 2026-10-09T03:38:13.092321+00:00. Physical pages: 19.

Read the complete selected text and displayed matching rendered image.

Physical page 19 completes the actual bibliography with Tian 1990 and Zelditch 1998. The classical quantization references are read here as bibliographic entries, not recursively checked proofs.

This final note completes all 19 physical pages of arXiv 2311.13451v2, 29 October 2025, in ten sequential, individually displayed matching views with complete text and chronological notes/receipts. The IMRN 2025 published PDF was not acquired: the publisher web fetch returned HTTP 429. The pinned arXiv version is described as the version for publication; byte identity to the published PDF is not claimed.

The actual support repair extends finite-right-derivative convex functions over the finite spectral interval, then uses completion for general functions. The algebraic decreasing-convex product proof and a correctly summed complex envelope-product proof provide useful attributed interfaces. The exact complex envelope/Hermitian equality, literal Hermitian interpolation formula, arbitrary-sequence limsup maximum identity, squared-norm/DH normalization and endpoint/function-class conventions need the calibrated repairs documented above. The main intended flat theorem remains dependent on the exact Fin22 quantization inputs and the completion/order/boundedness justification; it is not promoted as independently complete by this audit.

The common-flat, big/prescribed/Kahler and toric-degeneration questions are recorded as source-stated directions, with no new canonical atom or solved status. The active 4,661-page book, native catalogue, 42-atom/twelve-problem inventory, BJ22 critical Siu/envelope boundary and LPWZ unverified status stay unchanged. This is a whole-primary-paper reading only, not another whole-book pass or an independent hostile-model receipt.
