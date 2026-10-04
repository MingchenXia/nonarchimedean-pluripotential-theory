# Unchanged original mathematical family

Original P15.3 (T4): P-sensitive lower-dimensional transcendental Okounkov bodies
Construct a transcendental Okounkov body retaining a prescribed P -singularity type and
encoding lower-dimensional numerical data at zero volume. A class-level compact body of
zero ambient volume is already known; it does not identify numerical dimension or retain the
requested P -type.


Complete unchanged mathematical family:

9     Zero-volume energy, measures and convex bodies
Active items: P15.1, P15.2, P15.3. Status: Open in the residual scope.

9.1   Atomic targets
P15.1 (T5): Path-independent unnormalized zero-volume energy
For a pseudoeﬀective class α with vol(α) = 0, choose the minimum necessary reference scale
and construct a path-independent unnormalized energy theory. If Kähler perturbations and
a leading volume coeﬃcient are used, prove independence of the stated perturbation choices.
Division by zero volume is not an admissible normalization.

P15.2 (T5): Path-independent zero-volume Monge–Ampère theory
Construct a path-independent zero-volume Monge–Ampère theory with its carrier, dimension,
mass and reference choices explicitly stated. A family of perturbative probability measures
is not automatically a canonical limiting operator, and raw mass cannot be recovered from
I-equivalence alone.

P15.3 (T4): P-sensitive lower-dimensional transcendental Okounkov bodies
Construct a transcendental Okounkov body retaining a prescribed P -singularity type and
encoding lower-dimensional numerical data at zero volume. A class-level compact body of
zero ambient volume is already known; it does not identify numerical dimension or retain the
requested P -type.

9.2   What constitutes a solution
Name the reference scale, dimensional carrier and retained singularity data, then prove inde-
pendence of all claimed perturbation choices. Do not normalize zero mass to a probability. A
class-level body with zero ambient volume does not supply a P -sensitive numerical-dimension
theorem or an energy/operator construction.

9.3   Full statement and detailed state of the art
Problem 9.1. After choosing the minimum necessary reference scale, is there a path-
independent unnormalized energy and Monge–Ampère theory for a pseudoeﬀective zero-
volume class? Is there a P -sensitive transcendental Okounkov body encoding its lower-
dimensional numerical data?

    The unchanged probability signature is disproved: total mass zero cannot be normalized to
mass one. Kähler perturbations give a family of probabilities, not automatically a canonical
limit. Moreover Book Theorem 69.6.1 proves that a body depending only on I-equivalence
cannot recover actual nonpluripolar mass.
    The attempted positive construction rescales by the ﬁrst nonzero coeﬃcient in vol(α + εω),
then tests independence of the perturbation path and comparison with numerical dimension.
Nef zero-volume classes and toric examples provide the ﬁrst nontrivial cases. Any surviving
convex body must use P -type or richer data. No general path-independent construction is
presently veriﬁed.
    A distinct published class-level endpoint must be kept separate. Darvas–Reboulet–Witt
Nyström–Xia–Zhang attach a natural compact convex set to a pseudoeﬀective transcendental
cohomology class and a chosen ﬂag, and prove that its full n-dimensional volume equals


                                             71

vol(α)/n! [DRWN+ 26, pp. 135–136]. Hence a zero-volume class has such a canonical class-
level body of zero n-volume. This does not identify its lower-dimensional volume or dimension
with the numerical dimension, attach a body to a prescribed P -singularity type, or construct
an unnormalized energy or Monge–Ampère operator. It therefore narrows the starting point
for P15.3 but does not close any of the three zero-volume atoms.
    Two source questions give sharper benchmarks. Xia conjectures that the dimension of the
partial Okounkov body equals the numerical dimension even at zero mass [Xia25b, Conjec-
ture 5.29], and the same source asks whether the Chebyshev transform is independent of its
auxiliary positive form [Xia25b, p. 34]. These remain genuine published questions. The P -
sensitive body requested above is a stronger construction formulated in this book and should
not be attributed to that source.
    The third conjecture of that source is the non-toric mixed-volume formula [Xia25b, Conjec-
ture 8.8]. On 24 August 2026, the author supplied the TeX proof underlying the unpublished
manuscript [Xia26a]. After repairs of its positive-Cao-volume reduction, convex sandwich,
pointwise potential sandwich, rational analytic-resolution step, degenerate ﬁnite-level case,
multigraded saturation step, and eﬀective-shift body inclusion, the exact repaired proof re-
ceived a production gpt-5.6-sol/xhigh verdict of correct, with no critical error and no gap.
Thus Book Theorem 55.5.1 proves Conjecture 8.8 for singular psh metrics on big line bundles
over a smooth projective complex variety when every Cao (equivalently, ideal-model) volume
is positive; Book Theorem 55.5.2 gives the movable-product specialization for big line bundles
with minimal singularities. This is an author-supplied, repaired, and independently veriﬁed
proof in an unpublished work in progress, not a claim that the result has appeared in the pub-
lished literature. It asserts a supremum over surjective rank-n valuations, not attainment by
one valuation. Zero volume, transcendental classes, singular varieties, and attainment remain
outside the theorem; in particular, the genuinely diﬀerent problem Problem 9.1 remains open.
This source-status item is not an additional problem environment in the literal count at the
beginning of the chapter.




                                             72



# Exact claimed restricted result and remaining original obligations

{
  "id": "P15.3",
  "status": "partial",
  "exact_result": "A genuine partial current-valuation body for rational smooth divisorial singularities with smooth semipositive residual is a translated pseudoeffective class body and is independent of the stated positive perturbations. Its ordinary P-envelope remains in the prescribed bounded type. A nonprojective transcendental surface-times-curve example, after a specified blowup, has class volume zero, body dimension 2, retained logarithmic coefficient a recovered by min x_2, and unnormalized degree-two mass kappa^2-a^2 equal to twice its area. Actual and Cao cohomological products agree in this analytic domain. A separate dense-fiber P-envelope example proves that the direct analytic-domination recipe has no competitors even locally near any flag center at any positive Kähler perturbation; it does not prove impossibility of the original demand. Unchanged original P15.3 is not solved.",
  "proof_file": "P15.3-argument.md",
  "concrete_gaps": [
    "No genuine construction for arbitrary prescribed nonanalytic P-envelope types without passing to I-equivalence.",
    "No P-preserving approximation or general existence, compactness, and limiting theorem for such types.",
    "No general lower-dimensional numerical-dimension theorem or general identification of Cao and actual P-sensitive products.",
    "No general flag hypotheses realizing numerical dimension; the proved dimension equality uses the specified product flag.",
    "No general independence theorem for modifications or flags when the original manifold lacks a complete smooth flag.",
    "No general reference/carrier/perturbation theorem outside the fixed divisorial smooth-residual domain."
  ]
}

# Complete author proof

# P15.3: a proved divisorial partial construction, with the original obligations left open

This is an unverified mathematical draft. It proves a restricted construction, including a nonprojective transcendental example with class volume zero. It does **not** solve unchanged original P15.3. In particular, it gives no construction for arbitrary prescribed nonanalytic P-envelope data and no general numerical-dimension theorem. Compilation, source hashes, and successful execution are documentary checks, not mathematical verification.

## 1. Sources and distinctions

Only the four supplied public primary caches have been used. Their exact versions are DRWNXZ, arXiv:2309.07584v3 (5 January 2026); Xia, arXiv:2112.04290v2 (13 April 2024); Cao, arXiv:1210.5692v1 (21 October 2012); CHPW, arXiv:1508.03922v5 (arXiv header 5 February 2018, internal manuscript date 24 September 2018). Here and below source line numbers mean one-based indexing of `text.split('\n')`, preserving form feeds and the trailing empty line. Literal statements and relevant proof bodies, their inclusive locations, and application checks are in `source-extracts/source-provenance.json`. Complete byte-identical supplied text extracts are also preserved there.

DRWNXZ Definition 3.2 and the pseudoeffective definition (lines 561–691) use successive generic Lelong numbers of analytic currents along a **globally smooth connected complete flag**. For a pseudoeffective class they take the intersection of the bodies of Kähler perturbations. Theorem 7.6 and Corollary 7.7 (lines 1389–1415) prove ambient volume equals class volume divided by n!. The last proof proves zero ambient volume by comparison with perturbations. It proves no lower-dimensional numerical equality and contains no prescribed-potential input. Their Definition 5.1 and Example 5.3 (lines 852–894) do impose bounded singularity order on analytic Kähler currents. That analytic partial construction, rather than just their class body, is used below.

Xia's sections/multiplier ideals, equation (1.2), and Proposition 5.8 (lines 73–99 and 1181–1185) make his partial body invariant under I-equivalence. His definitions distinguish bounded type, ordinary P-envelope, the mass-sensitive envelope C, and the I-envelope (lines 371–429). In particular, at zero actual mass Proposition 2.10 does not identify C with P. Theorem 2.19 (lines 490–494) computes the section volume as the actual mass of the **I-envelope**, divided by n!, not as an unconditional equality with the mass of the input potential. Positive class volume, positive ideal-model volume, and positive actual potential mass are distinct hypotheses. An input in a big class can have zero actual mass; an I-invariant body does not, merely from its definition, recover its ordinary P-envelope or actual mass.

Xia section 5.6 (lines 1623–1637) defines a limit using rational positive perturbations by an ample divisor and explicitly retains I-invariance. Conjecture 5.29 states `dim Delta(theta,phi) = nd(theta,phi)`; its next sentence refers to Cao Definition 4, and the following sentence expresses an expectation about a proof. It is not a proved theorem. Xia's source domain is projective and line-bundle based. It is not invoked for the transcendental example below.

Cao Definition 2, Proposition 2.2 with its proof, and Definition 3 (lines 162–279) define a cohomological product through the absolutely continuous parts of quasi-equisingular analytic approximants. Definition 4 (lines 284–289) defines the numerical dimension of a line bundle with metric from that product. This is not the definition of the actual nonpluripolar product of the given current. We will denote by d_Cao(T) the maximum nonzero degree of Cao's **current** product of Definition 3, which is stated for general positive currents; we do not pretend a genuinely transcendental class is a line bundle. Equality with actual products will be proved for the specific analytic type below.

CHPW Theorem B/Corollary 3.22 (lines 173–185 and 1071–1085) requires a smooth projective variety, a pseudoeffective real divisor, and a flag **containing a positive volume subvariety** of dimension equal to the numerical Iitaka dimension. The lower-dimensional volume is augmented restricted volume along that subvariety. The relevant proof bodies are Theorem 3.20 and Proposition 3.21 (lines 919–1070). Remark 3.24 (lines 1090–1096) expressly allows strict dimension inequality for other flags. None of this theorem is applied to our nonprojective example. Its dimension is established by an explicit product-body identity.

These are precise source limitations, not an impossibility proof for original P15.3.

## 2. A restricted analytic construction

Use dd^c = i partial-barpartial/(2 pi), so dd^c log|z|^2 is the unit divisor current. Fix a compact Kähler n-fold M with a globally smooth connected complete flag Y. Let F be a smooth prime divisor, a a positive rational number, and D=aF. Fix a Hermitian metric on O(F), with curvature e, and put

    phi = a log |s_F|_h^2,  theta = beta + a e,
    T = theta + dd^c phi = beta + [D],  alpha = [theta],

where beta is a smooth closed semipositive (1,1)-form. Assume vol(alpha)=0. The chosen flag (or its specified flag on a modification) is part of the data. No independence of flags or arbitrary modifications is asserted.

For a Kähler form Omega on M, define

    B_Y(alpha,phi) = intersection over epsilon>0 of
        Delta_Y(alpha+epsilon[Omega]; T+epsilon Omega).

At each positive epsilon the right side is the genuine partial current-valuation body of DRWNXZ Definition 5.1: the reference current is Kähler, has rational gentle analytic divisorial singularities, and admissible currents must be more singular than phi up to a bounded constant. Thus this is a geometric Okounkov construction, not a numerical shape decorated with a potential.

**Proposition.** This construction is nonempty, compact, and convex, and

    B_Y(alpha,phi) = nu_Y([D]) + Delta_Y([beta]).                 (2.1)

It is independent of Omega. It retains the ordinary P-envelope type of phi within this divisorial bounded-type domain. Its dimension is dim Delta_Y([beta]); no general identification of this dimension with a numerical dimension is claimed.

**Proof of (2.1).** At positive epsilon, R_epsilon=[D]+beta+epsilon Omega satisfies every hypothesis of DRWNXZ Example 5.3. For completeness, its inclusions are as follows. A residual Kähler current S with gentle analytic singularities in [beta]+epsilon[Omega] yields S+[D], which is admissible for R_epsilon, and its valuation is nu(S)+nu([D]). Conversely, an admissible analytic Kähler current G has generic divisorial multiplicity at least a on F. Divisor subtraction (DRWNXZ Lemma 2.5, including its analytic quotient proof) gives a positive analytic residual G-[D] in [beta]+epsilon[Omega]. It is Kähler: apply the same subtraction to G-delta Omega for a sufficiently small delta>0. Its valuation belongs to the residual class body by Definition 3.2/Lemma 3.1. Valuation additivity gives the converse inclusion after closure. Therefore

    Delta_Y(alpha+epsilon[Omega]; R_epsilon)
        = nu_Y([D]) + Delta_Y([beta]+epsilon[Omega]).             (2.2)

No nonanalytic regularization that supposedly preserves P-type is used in this step. Taking intersections and the actual pseudoeffective definition gives (2.1). Compactness and convexity follow from the published class-body construction. Nonemptiness also follows directly: the smooth residual beta+epsilon Omega gives nu([D]) in every body.

**Perturbation independence, with its exact scope.** Adding a smooth positive form to an analytic current does not change any valuation coordinate. Consequently, if xi and xi+[rho] are big and rho is smooth positive, Delta_Y(xi) is contained in Delta_Y(xi+[rho]). For two Kähler forms Omega and Omega', choose constants 0<c<C such that c Omega < Omega' < C Omega pointwise. The residual bodies for these perturbations sandwich one another after rescaling epsilon; hence their intersections are equal. This proves independence without comparing zero ambient volumes. More generally, if rho_j are smooth Kähler forms tending to zero in the norm of a fixed Omega, then

    Delta_Y([beta]) subset Delta_Y([beta]+[rho_j])
        subset Delta_Y([beta]+delta_j[Omega]),  delta_j -> 0.

The right-hand compact bodies are nested when delta decreases. They converge in Hausdorff distance to their intersection: otherwise a sequence of points at fixed distance from the intersection has a convergent subsequence in a fixed compact body, whose limit belongs to every member. The sandwich therefore proves convergence to (2.1) along these paths. We claim neither arbitrary nonpositive perturbations nor convergence when the positive perturbations do not tend to zero. Rational cofinal epsilon sequences give the same intersection.

**Retained P-data.** Write

    P_theta[phi] = (sup {v in PSH(M,theta): v<=0, v<=phi+C_v})^*.

We prove P_theta[phi]=phi+O(1), rather than presuming the I-envelope equals this envelope. Take a competitor v. Its divisorial Lelong number on F is at least a; subtraction gives a beta-psh potential w=v-phi, initially off F and then extended as the potential of the positive residual current. This extension is upper semicontinuous and agrees off F. On a compact set away from F, v<=0 bounds w above uniformly by -phi, independently of C_v. In a coordinate polydisc along F, use F={z_1=0}, phi=a log|z_1|^2+b with b smooth, and a local smooth potential r for beta. On |z_1|=r_0 and z' in a smaller polydisc, w+r is uniformly bounded above by -phi+r. Its restriction to each transverse disc is subharmonic or identically minus infinity. The maximum principle gives the same bound inside the disc. A finite covering of F, together with the compact complement, gives w<=K independent of v. Thus every competitor satisfies v<=phi+K, and this inequality persists after upper semicontinuous regularization, using the local logarithmic bound near F. The competitor phi-sup_M phi gives the reverse bounded inequality. This proves the assertion.

If two inputs differ by a bounded function, their P-envelope competitor sets coincide. In particular P_theta[P_theta[phi]]=P_theta[phi] here. Altering the Hermitian metric on O(F) changes phi by a smooth bounded function and does not change the body or the P-data. This is retention of the analytic P-envelope type through the actual singularity constraint; it does not assert that one body reconstructs arbitrary singularity types.

**Products in this restricted domain.** On M minus F, the current T is the smooth beta. Actual nonpluripolar products are local there and put no mass on F, so <T^k>_NP=beta^k. The constant analytic approximation phi_j=phi satisfies all of Cao Definition 2: L1 convergence and positivity are immediate, singularity order is unchanged, and the required multiplier-ideal inclusion for (1+delta)m follows after normalizing phi<=0. The absolutely continuous part of T is beta. Cao Definition 3 therefore gives [beta^k]. Its equality with [<T^k>_NP] has now been proved for this domain, without making a general identification.

The cohomological data also persist for a positive current of the same bounded singularity type. After subtracting [D], its residual potential b is globally bounded relative to beta. The bounded Bedford--Taylor products have cohomology [beta^k]: the telescoping identity

    (beta+dd^c b)^k - beta^k
      = dd^c( b sum_{j=0}^{k-1} (beta+dd^c b)^j wedge beta^{k-1-j})

is valid for bounded potentials by the defining local Bedford--Taylor operation and its multiplication by closed products. Off F these are the nonpluripolar products, and bounded products charge no pluripolar set. Thus their extension across F is the actual nonpluripolar product. This proves cohomological invariance for the retained type. It is not equality of the different representative measures.

## 3. A genuinely transcendental zero-class-volume example with a proved dimension theorem

Here is an explicit admissible domain where (2.1) has proved numerical content. Let S be a compact Kähler surface with a Kähler class kappa outside the real span of divisor classes; fix a Kähler form in it. Such input may, for example, be a two-dimensional complex torus with no nonzero integral (1,1)-classes. Existence of such tori follows by choosing a linear complex structure on R^4 outside the countably many proper real-analytic loci on which a fixed nonzero integral alternating two-form is of type (1,1); each locus is proper since a complex structure can be varied to fail that invariance condition. Baire's theorem supplies the choice. A constant Hermitian form makes the quotient R^4/Z^4 Kähler. Only existence, not any computation on a selected torus, is being asserted.

Fix p in S. Put pi: S_hat=Bl_p S -> S, with exceptional E. Choose coordinates near p and a smooth cutoff chi supported in that chart, equal to 1 near p. Let

    f=chi log(|z_1|^2+|z_2|^2), u_a=a f.

For every sufficiently small a>0, kappa_form+dd^c u_a is positive. Indeed dd^c log|z|^2 is semipositive away from p in the region chi=1, and the negative part of dd^c f on the compact cutoff annulus is bounded by a fixed multiple of the Kähler form. Choose a positive rational a below the resulting bound. Its pullback has the decomposition

    pi^*(kappa_form+dd^c u_a)=beta_a+a[E],
    [beta_a]=kappa_a=pi^*kappa-a[E],                            (3.1)

with beta_a a **smooth Kähler form**. To see smoothness and strict positivity near E, in the chart z_1=w, z_2=wt the potential is a log|w|^2+a log(1+|t|^2). Subtraction of a[E] leaves pi^*kappa_form+a dd^c log(1+|t|^2); on E the first form is positive in the normal direction and the second in the tangent direction. They are semipositive in a neighborhood with their kernels complementary. The other chart is identical. On the cutoff annulus small a gives strict positivity, and outside it beta_a is the pullback of kappa_form where pi is an isomorphism. This proves (3.1), not just a nef or unproved Seshadri assumption.

Let C be any connected compact Riemann surface, c_0 a point, and q a point of E. Start on X_0=S x C with class alpha_0=p_S^*kappa and potential phi_0=p_S^*u_a. Use the specified modification

    Pi=pi x id_C: X=S_hat x C -> X_0.

Its center {p} x C is smooth. On X put alpha=Pi^*alpha_0, theta=p_S_hat^*pi^*kappa_form, phi_a=Pi^*phi_0, beta=p_S_hat^*beta_a, and D=a(E x C). Then theta+dd^c phi_a=beta+[D]. The globally smooth connected complete flag is

    X superset Y_1=S_hat x {c_0}
      superset Y_2=E x {c_0} superset Y_3={(q,c_0)}.             (3.2)

It is a current-valuation flag. We do not require the meromorphic function field of a nonprojective manifold to admit a surjective rank-three valuation.

The example is genuinely transcendental: if alpha_0 belonged to the real span of divisor classes, restricting to S x {c} would put kappa in that span. The same argument after pullback uses restriction followed by pi_*; divisor classes push to divisor classes or zero. Thus alpha is also outside that span. X_0 is nonprojective for the indicated torus example. The modification supplies the required flag even when a suitable flag was unavailable on the original manifold.

We need a psh pullback statement at zero class volume, whereas the setup of DRWNXZ section 2 initially fixes a big class. Here is its proof with no bigness hypothesis. If v is Pi^*theta_0-psh on X, then away from the exceptional image, w=v composed with Pi^{-1} is theta_0-psh and is bounded above, because v is quasi-psh on a compact space. Locally add a smooth potential of theta_0. A psh function bounded above extends over an analytic set by its upper semicontinuous extension (the removable-singularity argument used in the proof of DRWNXZ Lemma 2.1). Its pullback and v are psh potentials agreeing outside an analytic set, hence almost everywhere; canonical psh representatives agreeing almost everywhere agree everywhere by the submean regularization. This proves surjectivity. Injectivity and pointwise order preservation follow from surjectivity of Pi. This reproduces the cited proof and verifies the extension to the present nonbig class rather than assuming a big-class theorem applies.

A surjective pullback preserves both inequalities defining a bounded type and v<=0. Ordinary envelopes are least psh upper bounds of their competitor families, so the proved order isomorphism also commutes with P-envelopes for the pulled-back theta and zero obstacle. The retained P-type is consequently the pullback of the prescribed original point-logarithmic P-type. No independence of unrelated modifications or flags is asserted.

**Theorem (restricted product case).** For these data,

    B_Y(alpha,phi_a)
      = {(0,a+x,y): (x,y) in Delta_(E,q)(kappa_a)}.              (3.3)

Its affine carrier is {x_1=0}, with the standard (x_2,x_3) coordinate area. Its intrinsic dimension is exactly 2, and

    2! Area(B_Y)=integral_(S_hat) beta_a^2
                 = integral_S kappa_form^2 - a^2 > 0.         (3.4)

The ambient three-dimensional volume, class volume, and actual top nonpluripolar mass are all zero. The degree-two actual nonpluripolar cohomological data and Cao current product are [beta^2], nonzero; their largest nonzero degree is 2. In this example the nef class alpha itself also has numerical dimension 2. Equation (3.4) is an unnormalized lower-dimensional mass, not a probability.

**Class volume zero.** alpha has the smooth semipositive representative theta. It is not big: a Kähler current K in alpha would satisfy K>=delta Omega for some Kähler Omega, whereas

    integral_X K wedge theta^2 = integral_X theta^3 = 0,
    integral_X Omega wedge theta^2 > 0.

This is a contradiction. The published definition assigns volume zero to a nonbig pseudoeffective class. The same proof works on X_0. No implication from a particular potential's zero mass to class volume zero is used.

**The product-body identity supplying the dimension proof.** Choose a Kähler form eta on S_hat and a positive form sigma on C of degree 1. Let Omega_0=p_S_hat^*eta+p_C^*sigma. We prove, for every epsilon>0,

    Delta_Y([beta]+epsilon[Omega_0])
       = [0,epsilon] x Delta_(E,q)(kappa_a+epsilon[eta]).       (3.5)

For the upper inclusion, take a positive analytic current G in this class, with first valuation t along Y_1. Subtracting t[Y_1] leaves a positive analytic current. Restrict it to a generic curve {z} x C avoiding the locus on which the analytic potential is identically minus infinity. Its degree is epsilon-t, since Y_1 intersects that curve once; hence 0<=t<=epsilon. The restriction to Y_1 after the first subtraction is positive, analytic near the flag point, and lies in kappa_a+epsilon[eta]. (The normal bundle of a product fiber is trivial; the curve pullback contributes no surface class.) Its remaining two coordinates lie in the surface body by DRWNXZ Definition 3.2/Lemma 3.1. The upper inclusion follows after closure.

For the lower inclusion take a surface Kähler current R with gentle analytic singularities in kappa_a+epsilon[eta]. For any rational 0<=t<epsilon, the product current

    p_S_hat^* R + p_C^*((epsilon-t)sigma+t[c_0])

is Kähler with rational gentle analytic singularities and has valuation (t,nu_(E,q)(R)). Its positivity is strict in both product directions. Rational t are dense in [0,epsilon], including the endpoint in closure, and surface valuations of these R are dense in the surface body. This gives the full lower inclusion and proves (3.5).

Now kappa_a is Kähler. Proposition 3.3(3) of DRWNXZ, applied to this **big surface class**, gives

    intersection_(epsilon>0) Delta_(E,q)(kappa_a+epsilon[eta])
      = Delta_(E,q)(kappa_a).

Intersecting (3.5) therefore gives Delta_Y([beta])={0} x Delta_(E,q)(kappa_a). The fixed divisor has valuation (0,a,0): it does not contain Y_1, restricts to aE on Y_1, and has zero residual after subtracting that divisor. Equation (2.1) proves (3.3). The ordinary surface class body has nonempty interior because kappa_a is Kähler. Hence the dimension is 2; it is not inferred from Xia's conjecture or from zero ambient volume.

**Numerical mass and singularity sensitivity.** Apply DRWNXZ Theorem 7.6 to kappa_a on the surface. Its volume is its Kähler self-intersection: for bounded truncations all top masses equal this intersection by Stokes, arbitrary nonpluripolar masses are at most that value, and a smooth representative attains it. Since pi^*kappa.E=0 and E^2=-1, expansion gives (3.4). These intersection facts follow respectively from restricting a pulled-back class to the contracted E, and from the normal bundle O_E(-1). The actual nonpluripolar products of the chosen current are beta^k by Section 2, so the top degree 3 vanishes and degree 2 is nonzero. The constant analytic approximation computes exactly the same Cao cohomological products. For the nef class alpha the smooth representative theta likewise has largest nonzero intersection degree 2.

The surface geometric carrier is Y_1 and its residual two-dimensional mass is integral beta_a^2. Equivalently, with the explicitly named transverse scale integral_C sigma=1,

    integral_X beta^2 wedge Omega_0 = integral_(S_hat) beta_a^2.

Changing eta or the degree-one sigma does not change this number. An arbitrary reference form of fiber degree m would instead give m times this number; there is no claim that that changed reference scale is irrelevant. No zero quantity is divided out.

The body contains (0,a,0), because the surface body contains (0,0) from a smooth Kähler representative; all its second coordinates are at least a. Thus min_B x_2=a. For fixed p, this recovers the rational logarithmic coefficient of the prescribed P-type. Distinct a give distinct bodies in the **same original class** alpha_0; their lower mass is kappa^2-a^2. This demonstrates actual type sensitivity within the stated family, rather than appending a label to a class body. It does not show recovery of arbitrary supports or nonanalytic P-types from one flag.

All Kähler perturbation choices on the specified modified manifold, and the positive paths explicitly covered in Section 2, have the same limit. The proof uses the positive-epsilon valuation realization and compact sandwiches, not numerical volume equality at zero.

## 4. An exact obstruction to the direct analytic-domination recipe

The limitation to analytic divisorial input is substantive. There are prescribed P-envelope data at class volume zero for which **no** nontrivial competitor more singular than that envelope is analytic even near a single flag point, for any positive Kähler perturbation. This rules out the direct extension of the positive-epsilon competitor construction of Section 2 to all P-types; it does not rule out a different geometric construction.

Take M=P^1 x C for a compact connected curve C, theta=p_1^*omega_FS, with integral_(P^1) omega_FS=1. Its class is pseudoeffective and nonbig: a Kähler current in [theta], paired with theta, contradicts theta^2=0 and integral Omega wedge theta>0. Hence its class volume is zero. Choose distinct dense points p_j in P^1 and a_j=2^{-j-2}, j>=1, so A=sum a_j=1/4. Let g_j be the logarithm of the squared chordal distance to p_j. It satisfies g_j<=0, dd^c g_j=[p_j]-omega_FS, has unit logarithmic pole at p_j, and its L1 norm with respect to omega_FS is independent of p_j by unitary invariance. Define

    u=sum_(j>=1) a_j p_1^*g_j.

The partial sums are decreasing theta-psh functions with uniformly summable L1 norms. Thus their limit is theta-psh and not identically minus infinity; in particular it is a legitimate input. Its current is

    theta+dd^c u = (1-A)theta + sum_(j>=1) a_j[F_j],
    F_j={p_j} x C.

The equality follows in distributions from L1 convergence; positivity is explicit. Its top nonpluripolar mass also vanishes: every bounded truncation max(u,-k) is pulled back from P^1, so its local top wedge on the surface is zero. This potential's zero mass is established separately from class volume zero.

Let psi=P_theta[u], with the zero obstacle as in Section 2. The competitor u is bounded above by zero, so the envelope is nontrivial. For each j, u<=a_j p_1^*g_j. Consequently every competitor for P_theta[u] is a competitor for P_theta[a_j p_1^*g_j]. The latter is the single smooth-divisor situation of the envelope proof in Section 2, with residual (1-a_j)theta. Thus, for a constant K_j independent of the competitors,

    psi <= P_theta[a_j p_1^*g_j]
         <= a_j p_1^*g_j+K_j.

Upper semicontinuous regularization preserves this logarithmic upper bound by the same transverse maximum argument. In particular psi=-infinity along every F_j. Their union is dense in M.

Now let v be any nontrivial quasi-psh potential satisfying v<=psi+C. It is minus infinity on every F_j. If v had analytic singularities on any nonempty open neighborhood U, its minus-infinity locus in a smaller coordinate neighborhood would be the zero set of finitely many holomorphic functions, a proper closed analytic subset (or empty). It would contain the dense set U intersect union F_j; hence all of that coordinate neighborhood. All generators would vanish identically, making v identically minus infinity there, contrary to a nontrivial quasi-psh potential's local integrability. This proves the impossibility.

The argument does not use the background class of v. It applies in particular to v in PSH(M,theta+epsilon Omega), for every Kähler Omega and epsilon>0. Even restricting to currents analytic only near a chosen flag center cannot make that competitor set nonempty. This defeats the direct recipe "value analytic currents more singular than the fixed P-envelope, then take perturbative intersections" for this explicit prescribed datum. It does not defeat the unchanged original demand if another genuine valuation/geometric realization can incorporate such data; none is supplied here. It is not an inference of impossibility from an unsuccessful search.

## 5. What remains of unchanged original P15.3

The original quantification includes arbitrary compact Kähler manifolds, pseudoeffective classes with zero class volume, and prescribed P-singularity data. The preceding proof handles a rational analytic divisorial type with smooth semipositive residual; its numerical equality is proved only in the product example. The following obligations remain unresolved:

1. Construct a genuine current-valuation or geometric Okounkov body for arbitrary prescribed nonanalytic P-envelope type, without replacing that type by I-equivalence. The analytic divisor-subtraction argument does not approximate such types while retaining them. Section 4 proves that simply keeping the same analytic-domination competitor rule can yield an empty set at every positive perturbation.
2. Establish nonemptiness, compactness, limiting behavior, and any P-preserving analytic approximation required by that construction. These do not follow from I-equisingular approximation.
3. Define and prove a general lower-dimensional numerical theorem for the retained type, with the relevant actual product or other numerical invariant precisely specified. Neither Cao's product nor Xia's conjectured dimension equality has been identified with such a theorem here.
4. Prove the exact flag hypotheses realizing that numerical dimension. An arbitrary flag cannot be assumed to do so. The product proof establishes only (3.2).
5. Specify a modification when a smooth complete flag is absent, and prove every claimed relation or independence under those choices. We retain one specified modification and flag; no general independence theorem has been proved.
6. Name any further reference scales or carriers in the general construction and prove every claimed perturbation independence. The positivity sandwiches here require a fixed divisor and smooth residual; they do not justify a general P-sensitive limit.

There is no proof here that the original demand is impossible. The source gaps, restricted scope, and obstruction to one specified recipe are not such a proof. P15.1 and P15.2 are outside this assignment and no energy or Monge--Ampère operator is constructed.

## 6. Reproducible evidence

The frozen files are `input.json`, its byte-identical copy `input-original.json`, the exact decoded UTF-8 assignment in `assignment-original.txt`, and the frozen supplied task object in `task-original.json`. The latter two standalone files did not initially exist; their derivation and initial hashes are recorded in `input-preservation.json`. They are not rewritten by subsequent scripts.

Run `python3 prepare_sources.py` to regenerate the literal source records from the four allowed caches. Run `python3 build_paper.py` to perform the two actual TeX builds and preserve separate stdout, stderr, and TeX logs. Run `python3 verify_artifacts.py` for documentary consistency. Tool versions and OS/kernel are in `environment.json`; the run commands and exit codes are recorded in the build and verification output files. The standalone full proof is `P15.3-paper.tex`, with compiled `P15.3-paper.pdf` when the builds succeed. `status.json` has exactly the required five fields and reports partial completion.

The new mathematical claims are the divisorial limit proposition, its bounded/P-type argument, the restricted product theorem, and the exact empty-competitor obstruction of Section 4. No exhaustive numerical experiment, independent proof review, or computation-based mathematical verification is claimed.


# All four actual native canonical notes

[
  {
    "id": "n1",
    "summary": "Primary-source audit: the published class body proves ambient volume only; Xia’s body retains I-equivalence and leaves zero-volume dimension conjectural; Cao and CHPW require distinctions and hypotheses absent from a general P-sensitive theorem.",
    "detailedSummary": "The four supplied source hashes were checked. DRWNXZ requires a smooth complete flag and proves ambient volume equals class volume/n!. Xia section 5.6 explicitly states Conjecture 5.29 rather than proving its numerical-dimension equality. His multiplier-ideal construction is I-invariant, and its volume formula concerns the I-envelope. Cao’s product uses absolutely continuous parts of quasi-equisingular approximants. CHPW’s numerical theorem requires a flag containing a positive volume subvariety on a smooth projective variety. None supplies unchanged original P15.3.",
    "text": "The inspected versions are DRWNXZ arXiv:2309.07584v3, Xia arXiv:2112.04290v2, Cao arXiv:1210.5692v1, and CHPW arXiv:1508.03922v5. Their supplied PDF and extract hashes matched. The extract line counts, computed using split('\\n'), are respectively 2034, 2700, 1931, and 1425.\n\nDRWNXZ Definition 3.2 and the pseudoeffective definition, lines 561–691, construct bodies from successive Lelong valuations along a globally smooth connected complete flag. Theorem 7.6 and Corollary 7.7, lines 1389–1415, prove vol_Rn(Delta)=vol(alpha)/n!. The nonbig proof compares with perturbations and concludes zero ambient volume. It does not prove a lower-dimensional numerical theorem or retain prescribed potential data. Definition 5.1 and Example 5.3, lines 852–894, do impose bounded singularity order for analytic Kähler reference currents.\n\nXia’s section spaces use I(k phi), so I-equivalent inputs give identical bodies. Proposition 5.8 and section 5.6 retain this invariance. Section 5.6, lines 1623–1637, defines the perturbative intersection and literally states Conjecture 5.29: dim Delta(theta,phi)=nd(theta,phi). Its following sentences refer to Cao’s definition and express an expectation about a proof. This is not a proved equality. Xia’s definitions, lines 371–429, distinguish bounded type, ordinary P-envelope, C-envelope, and I-envelope. At zero actual mass Proposition 2.10 does not identify C with P. Theorem 2.19 computes section volume from the mass of P[phi]_I, not unconditionally from the actual mass of phi. Class volume, ideal-model volume, and actual potential mass must therefore be kept separate.\n\nCao Definitions 2–4, lines 162–289, use quasi-equisingular analytic approximation and absolutely continuous parts to define a cohomological product. Definition 3 concerns general positive currents; Definition 4 is stated for line bundles with metrics. Identifying this product with an actual nonpluripolar product requires an additional argument.\n\nCHPW Theorem B/Corollary 3.22 requires a smooth projective variety, a pseudoeffective real divisor, and a flag containing a positive volume subvariety. Its lower-dimensional mass is augmented restricted volume along that subvariety. Remark 3.24 explicitly allows strict dimension inequality for other flags. These results cannot simply be applied to arbitrary transcendental classes or arbitrary flags.\n\nLiteral statements and relevant proof bodies, exact versions and LF locations, hashes, and application checks are preserved in source-extracts/source-provenance.json. Complete byte-identical extracts are also preserved. Rerun: python3 prepare_sources.py. These are source findings, not a proof that original P15.3 is impossible.\n\nArtifacts: /workspace/research/campaigns/round-50/P15.3-public-source-zero-volume-P-sensitive-bodies/artifacts/codex-YlB9gG",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Restricted genuine P-sensitive construction: rational divisorial data with smooth residual give a perturbation-independent translated body. A nonprojective transcendental product example has dimension 2, recovers coefficient a, and has unnormalized mass kappa²−a².",
    "detailedSummary": "For T=beta+[D], with beta smooth semipositive and D=aF a rational smooth divisor, the positive-perturbation partial current-valuation bodies equal nu(D)+Delta([beta]+epsilon[Omega]). Their intersection is independent of the stated positive perturbations. A transverse maximum argument proves P_theta[phi]=phi+O(1). In a specified blowup of a transcendental Kähler surface times a curve, an explicit product-body identity proves dimension 2 and twice the area equals kappa²−a². Actual and Cao cohomological products agree in this analytic domain. Arbitrary nonanalytic P-types and general numerical equality remain outside the result.",
    "text": "Use dd^c=i partial-barpartial/(2 pi). Fix a compact Kähler manifold with a globally smooth complete flag, a smooth prime divisor F, rational a>0, and D=aF. Suppose T=theta+dd^c phi=beta+[D], where phi is the logarithmic divisor potential and beta is smooth closed semipositive. Assume class volume zero. Define B as the intersection of the genuine DRWNXZ partial bodies for T+epsilon Omega, with admissible analytic currents more singular than phi up to a bounded constant.\n\nAt every epsilon>0, the reference is Kähler with gentle analytic singularities. Adding [D] to a residual analytic Kähler current gives an admissible current and translates its valuation by nu(D). Conversely, admissibility forces multiplicity at least a on F. Divisor subtraction leaves a positive analytic residual; subtracting from G−delta Omega proves that residual is Kähler. The published analytic-current realization places its valuation in the residual class body. Hence Delta(alpha+epsilon[Omega];T+epsilon Omega)=nu(D)+Delta([beta]+epsilon[Omega]), and B=nu(D)+Delta([beta]). It is nonempty, compact, and convex.\n\nAdding a smooth positive form preserves valuations. Pointwise comparisons c Omega<Omega'<C Omega sandwich the residual bodies after rescaling epsilon, proving independence of the Kähler perturbation form. Smooth positive perturbations tending to zero are similarly sandwiched by the fixed-form nested bodies. Compactness proves Hausdorff convergence to their intersection. No nonpositive-path independence is claimed.\n\nThe retained P-data are proved directly. For a normalized competitor v<=phi+C, subtract [D] and write its residual potential w=v−phi. Away from F, v<=0 bounds w uniformly. In coordinates F={z_1=0}, add a local smooth potential of beta. On fixed transverse circles this psh function has a uniform upper bound independent of C. The subharmonic maximum principle extends it across the transverse discs. A finite cover gives v<=phi+K uniformly. This logarithmic bound survives envelope regularization; phi−sup phi supplies the reverse bound. Thus P_theta[phi]=phi+O(1). Boundedly equivalent inputs have identical envelope competitor families and identical body constraints.\n\nFor numerical content, take a compact Kähler surface S with Kähler class kappa outside the real span of divisor classes. Such input exists on a generic complex two-torus with no nonzero integral (1,1)-classes. Blow up p, obtaining pi:S_hat→S and exceptional E. A cutoff logarithmic potential u_a=a chi log(|z_1|²+|z_2|²), for sufficiently small rational a>0, has positive curvature. On the blowup its current is beta_a+a[E], where beta_a is smooth Kähler in kappa_a=pi*kappa−a[E]. In blowup coordinates z_1=w,z_2=wt, subtracting the divisor leaves pi*kappa_form+a dd^c log(1+|t|²), positive normally and tangentially; the cutoff annulus is controlled by choosing a small.\n\nOn X=S_hat×C use the flag X⊃S_hat×{c_0}⊃E×{c_0}⊃{(q,c_0)}. The original class on S×C is pulled back from kappa, and the prescribed original potential is the pullback of u_a. The specified modification supplies a complete smooth flag. The psh pullback bijection in this nonbig class is proved by descending off the exceptional image, extending bounded-above psh potentials across it, and using uniqueness of canonical psh representatives. This order isomorphism also preserves ordinary envelope competitor families. No independence of unrelated modifications or flags is asserted.\n\nLet beta be the pullback of beta_a. For Omega_0=p_S_hat*eta+p_C*sigma with integral_C sigma=1, the exact product identity is Delta_Y([beta]+epsilon[Omega_0])=[0,epsilon]×Delta_(E,q)(kappa_a+epsilon[eta]). For the upper inclusion, subtract the first valuation t and restrict to a generic curve fiber; positivity gives epsilon−t>=0. The remaining flag restriction has surface class kappa_a+epsilon[eta]. For the lower inclusion, pull back a surface analytic Kähler current R and add the curve current (epsilon−t)sigma+t[c_0], for rational 0<=t<epsilon. Its valuation is (t,nu(R)); density and closure give the identity.\n\nIntersecting and using continuity from above for the big surface class gives B={(0,a+x,y):(x,y)∈Delta_(E,q)(kappa_a)}. The surface body has nonempty interior, so B has intrinsic dimension 2 and affine carrier {x_1=0}. Its standard coordinate area satisfies 2! Area(B)=integral beta_a²=kappa²−a²>0. This follows from the published surface volume identity, pi*kappa.E=0, and E²=−1. Its minimum second coordinate is a, since the surface body contains the origin. Thus distinct a give distinct bodies in the same original class, genuinely retaining the prescribed analytic P-type.\n\nClass volume is zero independently: a hypothetical Kähler current in the pulled-back class, paired with its smooth semipositive representative squared, contradicts the zero cube. Actual nonpluripolar products of beta+[D] are beta^k by locality off D and absence of pluripolar mass. The constant analytic approximation computes Cao’s current products as [beta^k]. The largest nonzero degree is 2. For boundedly equivalent representatives the bounded Bedford–Taylor telescoping identity proves the same cohomological products. This proves equality in this domain, not generally. The unnormalized mass is the surface integral; a transverse reference form of degree m would multiply its threefold pairing by m. No zero mass is normalized.\n\nThe complete proof is in P15.3-argument.md and standalone P15.3-paper.tex. This is an unverified restricted theorem, not complete coverage of original P15.3.\n\nArtifacts: /workspace/research/campaigns/round-50/P15.3-public-source-zero-volume-P-sensitive-bodies/artifacts/codex-YlB9gG",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Exact obstruction: a zero-volume P-envelope with poles on dense fibers admits no more-singular nontrivial potential analytic near any flag center, even after positive Kähler perturbation. This defeats the direct analytic-domination recipe, not original P15.3 itself.",
    "detailedSummary": "On P¹×C, a summable sequence of positive rational logarithmic poles at dense base points defines a legitimate zero-mass potential in a zero-volume class. Its ordinary P-envelope retains every fiber pole by the uniform single-divisor envelope bound from n2. Any more-singular potential must have a dense minus-infinity locus, incompatible with analytic singularities on any open neighborhood. The impossibility is for that competitor rule and does not exclude another geometric realization.",
    "text": "Take M=P¹×C and theta=p_1*omega_FS, with integral omega_FS=1. Its class is pseudoeffective and nonbig: pairing a hypothetical Kähler current with theta contradicts theta²=0 and integral Omega wedge theta>0. Thus class volume is zero.\n\nChoose distinct dense points p_j on P¹ and a_j=2^(−j−2), j>=1, whose sum is A=1/4. Let g_j<=0 be the logarithm of squared chordal distance to p_j. Then dd^c g_j=[p_j]−omega_FS, and its L1 norm is independent of p_j by unitary invariance. The decreasing series u=sum a_j p_1*g_j has summable L1 norms, so it defines a nontrivial theta-psh potential. Distributionally, theta+dd^c u=(1−A)theta+sum a_j[F_j], where F_j={p_j}×C. Its actual top nonpluripolar mass is separately zero because every bounded truncation is pulled back from the curve.\n\nPut psi=P_theta[u] with zero obstacle. Since u<=a_j p_1*g_j, envelope competitor inclusion and the single-divisor bound proved in n2 give psi<=P_theta[a_j p_1*g_j]<=a_j p_1*g_j+K_j. Thus psi is minus infinity on every F_j. The competitor u ensures the envelope is nontrivial.\n\nSuppose a nontrivial quasi-psh v satisfies v<=psi+C and has analytic singularities on any open neighborhood. It is minus infinity on the dense union of the fibers. Locally an analytic potential has minus-infinity locus equal to a closed holomorphic zero set, or the empty set. Containing a dense set forces that zero set to be the whole neighborhood, making every generator identically zero and v identically minus infinity there. This contradicts local integrability of a nontrivial quasi-psh potential.\n\nThe argument is independent of the background form. Therefore no such analytic competitor exists in PSH(M,theta+epsilon Omega), for any Kähler Omega and epsilon>0, even if analyticity is required only near a flag center. Consequently the direct recipe of valuing analytic currents more singular than a fixed P-envelope and intersecting perturbative bodies cannot handle arbitrary prescribed P-data. Another genuine valuation or geometric construction remains possible in principle; no impossibility theorem for unchanged original P15.3 is claimed.\n\nThe complete obstruction proof appears in Section 4 of P15.3-argument.md and in P15.3-paper.tex.\n\nArtifacts: /workspace/research/campaigns/round-50/P15.3-public-source-zero-volume-P-sensitive-bodies/artifacts/codex-YlB9gG",
    "support": [
      "n2"
    ]
  },
  {
    "id": "n4",
    "summary": "Deliverables and documentary checks completed; unchanged original P15.3 remains unresolved. Two final TeX builds succeeded, frozen inputs and source hashes passed, and status is partial with candidate=false.",
    "detailedSummary": "The workspace contains the full argument, standalone TeX/PDF, literal source provenance, rerun programs, preserved build diagnostics, and exactly the required five-field status.json. General nonanalytic P-data, P-preserving approximation, numerical dimension and flag theorems, and general modification/reference independence remain unproved. Compilation and hash checks establish documentary consistency only.",
    "text": "Deliverables are P15.3-argument.md, P15.3-paper.tex, P15.3-paper.pdf, source-extracts/source-provenance.json, and status.json. The status object has exactly id,status,exact_result,proof_file,concrete_gaps and reports partial.\n\ninput.json and input-original.json are byte-identical, with SHA256 e00f660fe5d12953e51ce76d8311a36603284f802d6573c811adb62b1d93900b. assignment-original.txt preserves the exact decoded assignment bytes, and task-original.json freezes the supplied task object. Those standalone files did not initially exist; their initial hashes and derivation are recorded in input-preservation.json and subsequent scripts do not rewrite them.\n\nBoth final pdflatex builds returned 0. Separate actual stdout, stderr, and TeX logs are preserved as build-1.stdout/build-1.stderr/build-1.log and build-2.stdout/build-2.stderr/build-2.log. The first final pass had a bookmark rerun warning; the second had no diagnostic warnings. verification.stdout records successful input-preservation, four source-hash and LF-location checks, status-schema checks, and build-record checks. environment.json records tool versions and OS/kernel. No other models, subagents, external messages, installation, or heavy computation were used.\n\nRerun from the workspace: python3 prepare_sources.py; python3 build_paper.py; python3 verify_artifacts.py. RUNBOOK.txt gives commands with preserved diagnostic streams; artifact-manifest.json records artifact hashes.\n\nThe remaining unchanged original obligations are a genuine construction for arbitrary nonanalytic P-envelope types, P-preserving approximation and existence/limiting results, a general lower-dimensional numerical theorem, exact flag hypotheses realizing numerical dimension, general modification relations when flags are absent, and all claimed general reference/carrier/perturbation independence. The restricted theorem and the obstruction to one recipe do not discharge these obligations. No energy or Monge–Ampère operator is claimed. These are unverified mathematical drafts; execution and compilation do not establish mathematical correctness. Candidate=false.\n\nArtifacts: /workspace/research/campaigns/round-50/P15.3-public-source-zero-volume-P-sensitive-bodies/artifacts/codex-YlB9gG",
    "support": [
      "n1",
      "n2",
      "n3"
    ]
  }
]

# Source provenance, literal primary units and application checks

{
  "scope": "Only the four supplied public primary caches were read. No generated proof, private material, or other mathematical source was read.",
  "epistemic_status": "Source quotations and application audit; new arguments are unverified mathematical drafts.",
  "page_convention": "Textflow pages count literal form-feed separators, independently of printed pagination. Exact locations are the inclusive LF line ranges.",
  "sources": [
    {
      "id": "DRWNXZ",
      "title": "Transcendental Okounkov bodies",
      "exact_arxiv_version": "2309.07584v3",
      "printed_date": "5 Jan 2026",
      "public_source": "https://arxiv.org/pdf/2309.07584v3",
      "pdf_location": "/workspace/research/shared-sources/P15.3-arxiv-2309.07584v3-20261004.pdf",
      "pdf_sha256": "48b82ded9de9d2fee8d2c525129b1f176bbfc87dfa67f7ac4bfe9b23eba94e83",
      "supplied_extract_location": "/workspace/research/shared-sources/P15.3-arxiv-2309.07584v3-20261004.txt",
      "extract_sha256": "203fcf50f30ff047be9557db66d9f83473e996ea3cc943f652db0b6bd9da802e",
      "byte_identical_local_extract": "source-extracts/2309.07584v3-full.txt",
      "source_line_count": 2034,
      "line_number_convention": "UTF-8 text.split('\\n'); one-based indexing; trailing empty line counted; form feeds remain inside lines",
      "passages": [
        {
          "id": "flag-domain-and-modifications",
          "first_line": 101,
          "last_line": 146,
          "first_textflow_page": 2,
          "last_textflow_page": 3,
          "literal": "\f    Let (X, ω) be a connected compact Kähler manifold of dimension n. Let ξ := {θ} ∈\n  1,1\nH (X, R) be a big (or pseudoeffective) cohomology class, with θ being a smooth closed\n(1, 1)-form. Assume that X has a complete flag of submanifolds\n\n                         Y• := (X = Y0 ⊃ Y1 ⊃ · · · ⊃ Yn−1 ⊃ Yn ),\n\nLet A(X, ξ) be the set of positive\n                               P currents    θ + ddc u in ξ with analytic singularities. This\n                                      2\nmeans that locally u = c log( j |fj | ) + h, for c ∈ Q+ , fj holomorphic, and h bounded.\n    To any T0 ∈ A(X, ξ) one associates a valuation vector ν(T0 ) = (ν1 , . . . , νn ) ∈ Rn in\nthe following manner. Let ν1 equal ν(T0 , Y1 ), the generic Lelong number of T0 along Y1 .\nOne can show that T1 := (T0 − ν1 [Y1 ])|Y1 has analytic singularities on Y1 . Then one sets\nν2 := ν(T1 , Y2 ) and continues the above process until all components of ν(T0 ) are defined.\nThe Okounkov body of ξ, denoted ∆Y• (ξ) (or just ∆(ξ), once the flag is fixed), is then\ndefined as:\n                                  ∆(ξ) := ν(A(X, ξ)) ⊂ Rn .\nAs in the line bundle case, the convexity of the Okounkov body follows from the fact\nthat ν(S + T ) = ν(S) + ν(T ). When ξ is a pseudoeffective class, one puts ∆(ξ) =\n∩ε>0 ∆(ξ + ε{ω}). For more details, the reader is invited to consult § 3.\n   Deng’s body coincides with Okounkov’s when ξ is the first Chern class of a big line\nbundle [25]. Thus, this body is a natural generalization of the Okounkov body to the\ntranscendental setting, and we will work with Deng’s definition in our paper.\n   It remained to show that the transcendental Okounkov body satisfies (1.2). Deng\nproved that this is true when the dimension of X is at most two, but the general case\nwas open until now. Our main result proves the volume identity in full generality:\n\nTheorem 1.1. Let ξ be a big cohomology class on X and Y• be a flag on X. Then the\nassociated Okounkov body ∆(ξ) of ξ satisfies the volume equality\n                                                  1\n                                 volRn (∆(ξ)) =      vol(ξ).                            (1.3)\n                                                  n!\n   Passing to the limit, the volume identity can be extended to pseudoeffective classes\nas well:\n\nCorollary 1.2. The identity (1.3) holds even if ξ is pseudoeffective.\n\n    Theorem 1.1 and Corollary 1.2 confirm [25, Conjecture 1.4] and also give an affirmative\nanswer to the question of Lazarsfeld–Mustaţă [35, p. 831].\n    We note that, a priori X might not contain any proper complex submanifolds of\npositive dimension, let alone flags. For example, this happens if X is a non-algebraic\nsimple compact torus. However, one can always blow up X at a point p. Then one\ncan construct a flag Y• on Blp X with Y1 ∼   = CPn−1 being the exceptional divisor and\nY2 ⊃ · · · ⊃ Yn being a flag of linear subspaces in Y1 . Therefore, up to modifying X and\npulling back ξ, our main result is always applicable.",
          "local_file": "source-extracts/2309.07584v3--flag-domain-and-modifications.txt",
          "sha256": "0102b4b9c7aed4f44deb53f4b9bf5d7d3211247a3bf755cff9317be425c74d1a",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "singularity-order-and-pullback-proof",
          "first_line": 226,
          "last_line": 263,
          "first_textflow_page": 5,
          "last_textflow_page": 6,
          "literal": "2    Preliminaries\nLet (X, ω) be an n-dimensional connected compact Kähler manifold. Let ξ := {θ} ∈\nH 1,1 (X, R) be a big cohomology class. We write Z+ (X) for the set of closed positive\n(1, 1)-currents on X and Z+ (X, ξ) for the set of T ∈ Z+ (X) representing ξ. A function\nφ : X → [−∞, ∞) is called quasi-plurisubharmonic (qpsh) if locally φ = ϕ + ψ, where ϕ\nis smooth and ψ is plurisubharmonic. Put\n\n           PSH(X, θ) := {φ : X → [−∞, ∞) :\n                         φ is a qpsh function on X such that θ + ddc φ ≥ 0},\n               √\nwhere ddc :=        ¯\n                −1∂ ∂/2π. Given a qpsh function φ, the Lelong number of φ at x ∈ X is\n\n                ν(φ, x) := sup{c ≥ 0 : φ(z) ≤ c log |z − x|2 + O(1) near x}.\n\nGiven an irreducible analytic subset E ⊂ X, the generic Lelong number of φ along E is\n\n                                  ν(φ, E) := inf ν(φ, x).\n                                              x∈E\n\nIf T = θ + ddc φ for φ ∈ PSH(X, θ), then set ν(T, x) := ν(φ, x) and ν(T, E) := ν(φ, E).\n    If ϕ, ψ are qpsh, we say that ϕ is more singular than ψ and write ϕ ⪯ ψ if ϕ ≤ ψ + C\nfor some constant C. If ϕ ⪯ ψ and ψ ⪯ ϕ, we then write ϕ ∼ ψ and say that ϕ and ψ\nhave the same singularity type. This defines an equivalence relation.\n    Given T, S ∈ Z+ (X), with T = θ1 + ddc ϕ and S = θ2 + ddc ψ, θ1 , θ2 being smooth,\nthen we say that T is more singular than S if ϕ is more singular than ψ, and write T ⪯ S.\nIf ϕ ∼ ψ we also say that T and S have the same singularity type and write T ∼ S.\n\n                                             5\n\fLemma 2.1. Let π : Z → X be a proper bimeromorphic morphism with Z being a Kähler\nmanifold. Then π ∗ and π∗ induce a bijection between Z+ (X, ξ) and Z+ (Z, π ∗ ξ).\nProof. One can show that the pullback map π ∗ is an isomorphism between PSH(X, θ)\nand PSH(Z, π ∗ θ), where θ is a smooth closed (1, 1)-form representing ξ.\n    It is clear that the pullback map is injective. To show surjectivity, let v ∈ PSH(Z, π ∗ θ).\nLet U ⊂ X be the Zariski open set such that π : π −1 (U ) → U is biholomorphic. Then\nw := v ◦ π −1 ∈ PSH(U, θ), moreover w is bounded from above. Since X \\ U is an analytic\nset, it follows that w extends to an element of PSH(X, θ) [22]. Since π ∗ w = v away from\nan analytic set, it follows that π ∗ w = v [22].",
          "local_file": "source-extracts/2309.07584v3--singularity-order-and-pullback-proof.txt",
          "sha256": "24c7835f46b7454a193e5395002e12365e8f2cea3e9d389c1e45b509c0f1c3a5",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "divisor-subtraction-and-proof",
          "first_line": 309,
          "last_line": 333,
          "first_textflow_page": 7,
          "last_textflow_page": 7,
          "literal": "Lemma 2.4. If u, v are qpsh functions with analytic singularities, then max(u, v) also\nhas analytic singularities.\n\n   The following useful result due to Siu [44] will be also frequently used.\n\nLemma 2.5. Assume T ∈ ξ is a positive current and D is a prime divisor on X. If\nν(T, D) ≥ a for some a ∈ Q≥0 , then T − a[D] is a positive current in ξ − a{[D]}.\nMoreover, if T has analytic singularities near a point, then so does T − a[D].\n\nProof. The first assertion follows from Siu’s decomposition [44].\n   Let q ∈ X. In a neighborhood of q we have that\n                                           X\n                                 u = c log    |fj |2 + O(1).\n                                            j\n\n\n   After rescaling we can assume that a, c ∈ Z. Let T = θ + ddc u for some qpsh function\nu and smooth closed (1, 1)-form θ.\n   By the Lelong–Poincaré formula there exists a neighborhood U of q and w ∈ O(U )\nsuch that ddc log |w|2 = a[D]. By properties of Lelong numbers there exists C > 0 such\nthat\n                                   u ≤ log |w|2 + C.\nThis implies that |fj |2c ≤ C̃|w|2 for all j, for some C̃ > 0. Due to the Riemann extension\ntheorem, there exists gj ∈ O(UP   ) such that fjc = wgj . As a result, the local singularities\nof T − a[D] is modelled by log j |gj |2 .",
          "local_file": "source-extracts/2309.07584v3--divisor-subtraction-and-proof.txt",
          "sha256": "61b6b232d7204155cf7dabcb0195ad2d463e9687dab058e09cf3a92f6c9a47c2",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "gentle-singularities",
          "first_line": 338,
          "last_line": 361,
          "first_textflow_page": 7,
          "last_textflow_page": 8,
          "literal": "Definition 2.6. Let I ⊆ OX be an analytic coherent ideal sheaf and c ∈ Q>0 . A qpsh\nfunction φ on X is said to have gentle analytic singularities of type (I, c) if\n\n  1. eφ/c : X → R≥0 is a smooth function;\n\n  2. locally φ can be written as\n                                                    X\n                                      φ = c log         |fi |2 + h,                     (2.1)\n                                                    i\n\n      where {fi } is a finite set of local generators of I and h is a bounded remainder;\n\n  3. there is a proper bimeromorphic morphism π : X̃ → X from a Kähler manifold X̃\n     and an effective Z-divisor D on X̃ such that one can write π ∗ φ locally as\n\n                                       π ∗ φ = c log |g|2 + h,\n\n      where g is a local equation of the divisor D and h is smooth.\n\n                                                7\n\f    A positive current T = θ+ddc φ ∈ Z+ (X, ξ) is said to have gentle analytic singularities\nof type (I, c) if so does φ. We set\n\n             Ω(X, ξ) := {Kähler current in ξ with gentle analytic singularities} .",
          "local_file": "source-extracts/2309.07584v3--gentle-singularities.txt",
          "sha256": "1ff0f35e76b85030575caa466ffb360af8af9d61adf3126b5217e36790a9b90e",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "regularization",
          "first_line": 398,
          "last_line": 411,
          "first_textflow_page": 8,
          "last_textflow_page": 8,
          "literal": "Theorem 2.8. Let T = θ+ddc φ ∈ Z+ (X, ξ) be a Kähler current. Then one can construct\na sequence Tk = θ + ddc φk , which are Kähler currents with gentle analytic singularities of\ntype (I(kφ), k1 ) and φ ≤ φk for all k ≫ 0. Here I(kφ) denotes the multiplier ideal sheaf\nof kφ that is generated by holomorphic functions f ∈ OX such that |f |2 e−kφ ∈ L1loc .\n\n    As a direct consequence, we have the following result.\n\nLemma 2.9. For any two Kähler currents T1 , T2 ∈ Z+ (X, ξ), one can find T3 ∈ Ω(X, ξ)\nthat is less singular than both T1 and T2 .\n\nProof. Write Ti = θ + ddc φi for i = 1, 2. Put φ0 := max{φ1 , φ2 }. Then T := ω + ddc φ0\nis a Kähler current that is less singular than both T1 and T2 . Note that T may not have\ngentle analytic singularities, but then we can apply Theorem 2.8 to find another Kähler\ncurrent T ′ ∈ Ω(X, ξ) that is less singular than T .",
          "local_file": "source-extracts/2309.07584v3--regularization.txt",
          "sha256": "dae5f5b1549ce4de18b13e4e324db831454ec1989e916019e992002b16ed253b",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "class-body-definitions-and-proofs",
          "first_line": 561,
          "last_line": 715,
          "first_textflow_page": 11,
          "last_textflow_page": 14,
          "literal": "3     Transcendental Okounkov bodies\nThe big case. Let ξ a big (1, 1)-class on X. The goal of this paragraph is to attach\nnatural convex bodies (compact convex sets with non-empty interior) ∆(ξ) ⊂ Rn to ξ,\nwhich will be called the Okounkov bodies of ξ. One starts with a flag\n\n                     Y• = (X = Y0 ⊃ Y1 ⊃ · · · ⊃ Yn−1 ⊃ Yn = {q}),\n\nwhere Yi is a smooth connected complex submanifold of X with codimension i. We call\nsuch a flag a smooth flag on X centered at q.\n    However, it is possible that X might not contain any proper submanifolds of positive\ndimension, let alone flags. As we have pointed out in the introduction, an easy remedy\nfor this issue is to replace X by a smooth model X ′ and then one can construct a flag\nY• on X ′ . So after possibly modifying X and pulling back ξ, in what follows we always\nassume that X contains a flag Y• , which is centered at the point q ∈ Yn .\n\n                                               11\n\f  Next, using Y• we shall associate an Okounkov body ∆(ξ) = ∆Y• (ξ) ⊂ Rn with ξ.\nThe construction is essentially the same as in [25], apart from some minor modifications.\n  Following [35, 25], we define a valuative map ν : A(X, ξ, q) → Qn≥0 by\n                         T 7→ ν(T ) = νY• (T ) = (ν1 (T ), . . . , νn (T ))\nas follows. First, set\n                                       ν1 (T ) := ν(T, Y1 ).\nSince the generic Lelong number of T1 := (T − ν1 (T )[Y1 ]) along Y1 is zero and this\ncurrent has analytic singularities near q, its potential is not identically −∞ on Y1 , hence\nT1 := (T − ν1 (T )[Y1 ])|Y1 is a positive current on Y1 , with analytic singularities near q.\n    Next put\n                                        ν2 (T ) := ν(T1 , Y2 ),\nand continue in this manner to define all the remaining values νi (T ) ∈ Q≥0 .\n   Note that Ω(X, ξ) ⊆ A(X, ξ, q). So the map ν is also defined on Ω(X, ξ). Consider\nthe image sets\n                            ν(Ω(X, ξ)) and ν(A(X, ξ, q)).\nThese two are bounded sets in Qn≥0 , since all the Lelong numbers appearing in the above\nconstruction are bounded by cohomological constants (see e.g. [25, Lemma 4.3]). More-\nover, they are convex sets in Qn≥0 , since ν(tT1 + (1 − t)T2 ) = tν(T1 ) + (1 − t)ν(T2 ) for\nT1 , T2 in Ω(X, ξ) (or in A(X, ξ, q)) and t ∈ [0, 1] ∩ Q.\n     The following lemma plays a key role in this paper.\nLemma 3.1. For any T ∈ A(X, ξ, q), one can find a sequence Tk ∈ Ω(X, ξ) such that\nν(Tk ) → ν(T ) in Qn≥0 .\nProof. First, we might as well assume that T is a Kähler current. Indeed, one can take\nS ∈ Ω(X, ξ) and let Tε := (1 − ε)T + εS for ε ∈ (0, 1) ∩ Q. So Tε is a Kähler current in\nA(X, ξ, q) and ν(Tε ) = (1 − ε)ν(T ) + εν(S) can be made  Parbitrarily close to ν(T ).\n                                        c                   r     2\n      Next assume that T = θ + dd φ with φ = c log i=1 |gi | + O(1) near q, where\ng1 , . . . , gr ∈ OX,q and c ∈ Q≥0 . Let J ⊆ OX,q be the ideal generated by g1 , . . . , gr . Up\nto rescaling the class ξ we will assume that c = 1 for simplicity. Let Tk P= θ + ddc φk be\nthe sequence given by Theorem 2.8. Near q, one can write φk = k1 log l |gkl |2 + O(1)\nfor some local generators {gkl }l of I(kφ)q . Let m := min{n − 1, r − 1}. Then by the\nBriançon–Skoda theorem (see [23, Theorem 11.17]), the equality of ideals\n                                I((k + m)φ)q = J k · I(mφ)q\nholds at qPfor any large k ∈ N. Let {hj } be a set of generators of I(mφ)q and put\nψ := log j |hj |2 , which is a qpsh function defined near q. Then the above equality\nimplies that\n                                     k          1\n                           φk+m =        φ+         ψ + O(1)\n                                   k+m       k+m\nholds near q. So sending k → ∞ we find that ν(Tk ) → ν(T ), as desired.\n   Consequently, we are led to the following definition (cf. [25, Definition 4.12]).\nDefinition 3.2. The Okounkov body ∆(ξ) = ∆Y• (ξ) of ξ is defined to be\n                     ∆(ξ) := ν(Ω(X, ξ)) = ν(A(X, ξ)) = ν(A(X, ξ, q)).\nHere the closure is taken with respect to the Euclidean topology of Rn .\n\n                                                12\n\f    As in [25, Proposition 4.13], we have the following properties for ∆(ξ):\nProposition 3.3. The following properties hold:\n   1. For λ ∈ R>0 , one has ∆(λξ) = λ∆(ξ);\n   2. ∆(ξ1 ) + ∆(ξ2 ) ⊆ ∆(ξ1 + ξ2 ) for two big classes ξ1 and ξ2 ;\n              T\n   3. ∆(ξ) = ε>0 ∆(ξ + ε{ω}) for any Kähler form ω on X.\nProof. Point (1) is clear when λ ∈ Q>0 . If λ ∈ R>0 , it suffices to observe that, for any\nT ∈ Ω(λξ), one can find a sequence Ti ∈ Ω(X, ξ) so that λν(Ti ) → ν(T ). Point (2) is\nalso clear. So it remains to argue (3).                                            √\n    First, it is easy to see that ∆(ξ) ⊆ ∆(ξ + ε{ω}). On the other hand, (1 + ε)ξ −\n(ξ\n√ +n ε{ω}) is a big class for small ε > 0. So from (1) and (2) we have that (1 +\n   ε) volRn (∆(ξ)) ≥ volRn (∆(ξ + ε{ω})). Thus, we get that\n                              volRn (∆(ξ)) = lim volRn (∆(ξ + ε{ω})).\n                                                ε→0\n               T\nSo ∆(ξ) = ε>0 ∆(ξ + ε{ω}) follows (here we used that ∆(ξ) is a convex body, by\nProposition 3.4 below).\nProposition 3.4. When ξ is big, ∆(ξ) is a convex body in Rn , so volRn (∆(ξ)) > 0.\n    This result is also from [25]. Below we give a slightly different proof.\nProof. We need to show that ∆(ξ) has non-empty interior. Since ξ can be written as the\nsum of a Kähler class and a big class, it suffices to show that ∆(ξ) has non-empty interior\nwhen ξ is Kähler.\n    So assume that ξ is Kähler. Fix a Kähler form ω ∈ ξ. We will argue that ∆(ξ)\ncontains a small simplex near the origin. Clearly, ∆(ξ) contains the origin. Applying\n[27, Lemma 2.1(i)] to Yi , we can find qpsh functions ψi on X for 1 ≤ i ≤ n so that\nψi has analytic singularities precisely along Yi . Choosing ε > 0 small enough so that\nTi := ω + εddc ψi are all elements in Ω(X, ξ). Then one has ν(Ti ) = εei ∈ Rn≥0 , so that\n∆(ξ) contains a simplex.\n    The following result could be of independent interest.\nProposition 3.5. The map ξ 7→ ∆(ξ) from the big cone of X to Rn is continuous with\nrespect to the Hausdorff topology in Rn .\nProof. Choose smooth (1, 1)-forms η1 , . . . , ηr on X so that the {ηi } form a basis of\nH 1,1 (X, R). For any two big classes ξ, ξ ′ ∈ H 1,1 (X, R) write ξ = (a1 , . . . , ar ) and\nξ ′ = (a′1 , . . . , a′r ) using this basis and let ∥ξ − ξ ′ ∥ := maxi |ai − a′i |. We wish to argue that\nthe Hausdorff distance between ∆(ξ) and ∆(ξ ′ ) tends to zero as ∥ξ − ξ ′ ∥ → 0.\n      Fix a Kähler current T ∈ ξ and assume that T ≥ ω for some Kähler form                P ω′ on X.\n                                                                                     ′ :=\nPick C > 1 so that −Cω ≤ ηi ≤ Cω holds for all 1 ≤ i ≤ r. Then T                          T + i (ai − ai )ηi\n                                  ′                   ′           −1\nis a Kähler current in ξ as long as ∥ξ − ξ ∥ < (Cr) . Moreover, we see that (1 + ∥ξ −\nξ ′ ∥1/2 )ξ − ξ ′ is big as well when ∥ξ − ξ ′ ∥ < (Cr)−2 , since (1 + ∥ξ − ξ ′ ∥1/2 )T − T ′ is a\nKähler current in that class. This implies that ∆(ξ ′ ) ⊆ (1 + ∥ξ − ξ ′ ∥1/2 )∆(ξ) as long\nas ∥ξ − ξ ′ ∥ < (Cr)−2 . On the other hand, observe that (1 + ∥ξ − ξ ′ ∥1/2 )T ′ − T is a\nKähler current when ∥ξ − ξ ′ ∥ < (2Cr)−2 , so that ∆(ξ) ⊆ (1 + ∥ξ − ξ ′ ∥1/2 )∆(ξ ′ ) when\n∥ξ − ξ ′ ∥ < (2Cr)−2 .\n      The above discussion easily implies that the Hausdorff distance between ∆(ξ) and\n∆(ξ ′ ) tends to zero as ∥ξ − ξ ′ ∥ → 0.\n\n                                                      13\n\fThe pseudoeffective case. In case ξ is only pseudoeffective and not big, there are\ndifferent ways to associate a compact convex set with ξ [18]. In [25, Definition 4.23] Deng\nsuggests the definition below that we will follow in this work. For a Kähler form ω, let\n                                         \\\n                                 ∆(ξ) :=    ∆(ξ + ε{ω}).                               (3.1)\n                                          ε>0\n\nDue to Proposition 3.3, the above definition does not depend on the choice of ω. Another\nnatural choice is\n                                    ˜\n                                    ∆(ξ) := ν(A(X, ξ)).\nSince A(X, ξ) ⊂ A(X, ξ + ε{ω}) we obtain that ∆(ξ) ˜                             ˜\n                                                          ⊂ ∆(ξ). Notice that ∆(ξ)    might\nbe empty.\n    In case ξ is pseudoeffective and non-big, we will establish later that volRn ∆(ξ) = 0 =\n                                      ˜\nvol(ξ), so this will imply that volRn ∆(ξ) = 0 = vol(ξ).\n    In particular, Theorem 1.1 will remain valid, regardless what definition one chooses\nfor the convex compact sets associated to pseudoeffective (non-big) classes.\n\nThe conjectured volume identity. Let us return to a big class ξ. When ξ is in the\nNéron–Severi space it was shown in [25] that vol(ξ) = n! volRn (∆(ξ)). For a transcenden-\ntal big class ξ, following [25, Conjecture 1.4], we expect the same:\n\nProperty An . Assume that dim X = n and ξ is big. Then vol(ξ) = n! volRn (∆(ξ)).\n\n    Note that the ensemble of Property An ’s for all n ≥ 1 is equivalent to Theorem 1.1.\n    It is easy to establish this when n = 1. We recall its proof for the reader’s convenience.\n\nLemma 3.6. Property A1 holds.\n\nProof. When Rdim X = 1, H 1,1 (X, R) ∼ = H 2 (X, R) ∼= R. A class ξ ∈ H 1,1 (X, R) is Kähler\nif and only if X ξ > 0. Moreover, in this setting every big class ξ = {θ} is a Kähler class,\nand a flag is simplyRa choice of point Y1 = X ⊃ Y0 = {q}.\n    For any t ∈ (0, X θ), {θ} − t{q} the class is Kähler, which then contains a smooth\n                                                                                     R\nKähler form ωt . Then ωt +t[q] ∈ Ω(X, {θ}) and it Rhas Lelong number t at q. So [0, X θ] ⊆\n∆({θ}).R On the other hand, one has ν(T, q) ≤ X θ for any T ∈ Ω(X, {θ}),      R otherwise\n{θ} − X θ{q} is a Kähler class, which is absurd. So we have ∆({θ}) = [0, X θ].\n   The following sections aim to prove Property An for higher dimensions. It is notable\nthat, by using the divisorial Zariski decomposition for surfaces, it was shown in [25,\nTheorem 1.8] that Property A2 holds as well.\n",
          "local_file": "source-extracts/2309.07584v3--class-body-definitions-and-proofs.txt",
          "sha256": "844744b8b796c05384d83061106f4b339ec67546985e09db8fd138d212da8b7e",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "lifting-flags-and-proof-bodies",
          "first_line": 716,
          "last_line": 850,
          "first_textflow_page": 14,
          "last_textflow_page": 17,
          "literal": "\n4     Lifting the flags\nIn this section, we fix a smooth flag Y• = (Y0 ⊃ · · · ⊃ Yn ) on X.\n    If π : Y → X is a proper bimeromorphic morphism of complex manifolds and Z is\nan analytic set in X not contained in the exceptional locus E, then we define the strict\ntransform of Z in Y as the closure of π −1 Z \\ π −1 E in Y . This is an analytic set in Y by\n[22, Corollary 5.4]. When π is a modification, this coincides with the notion defined in\n[10, Section 3, strict transforms] by [10, Remark 3.15].\n\n\n\n                                                14\n\fDefinition 4.1. Let π : Z → X be a proper bimeromorphic morphism with Z being a\ncompact Kähler manifold. We say that a smooth flag W• = (W0 ⊃ · · · ⊃ Wn ) is a lifting\nof Y• to Z if the restriction of π to Wi → Yi is defined and bimeromorphic.\n\nLemma 4.2. Let π : Z → X be a proper bimeromorphic morphism with Z being a Kähler\nmanifold. Assume that there is a lifting W• = (W0 ⊃ · · · ⊃ Wn ) of Y• to Z. Then there\nis a matrix g ∈ SLn (Z) of the form I + N with N being strictly upper triangular (namely,\nall entries on and below the diagonal are 0) such that for any T ∈ A(X), we have\n\n                                       νW• (π ∗ T ) = νY• (T )g.\n\n    Here the valuations of currents are considered as row vectors. For simplicity, we will\nalso say (W• , g) is a lifting of Y• to Z.\n    Observe that matrices of the form I +N are exactly the automorphisms of the ordered\nAbelian group Zn with respect to the lexicographic order. So this result can be seen as\na generalization of [15, Theorem 2.9].\nProof. We take induction on n = dim X. The case n = 1 is trivial. In general, assume\nthat the result is proved when dim X = n − 1.\n   For simplicity, we write ν = νY• and ν ′ = νW• . Let µ (resp. µ′ ) be the valuation of\ncurrents defined by Y1 ⊃ · · · ⊃ Yn (resp. W1 ⊃ · · · ⊃ Wn ). Then we need to show that\n                         \u0002 ′ ∗\n                          ν (π T )1 µ′ ((π ∗ T − ν ′ (π ∗ T )1 [W1 ])|W1 )\n                                                                           \u0003\n\n\nequals                          \u0002                               \u0003\n                                 ν(T )1 µ((T − ν(T )1 [Y1 ]))|Y1 g.\nClearly\n                                      ν ′ (π ∗ T )1 = ν(T )1 =: c.\nBy the inductive hypothesis, we can find h ∈ SLn−1 (Z) of the form I plus a strictly upper\ntriangular matrix such that\n\n                           µ′ (Π∗ (T − c[Y1 ])|Y1 ) = µ((T − c[Y1 ])|Y1 )h,                       (4.1)\n\nwhere Π : W1 → Y1 is the restriction of π. Observe that\n\n                Π∗ (T − c[Y1 ])|Y1 = (π ∗ (T − c[Y1 ]))|W1\n                                   = (π ∗ T − c[W1 ])|W1 + c(π ∗ [Y1 ] − [W1 ])|W1 .\n\nSo\n          µ′ (Π∗ (T − c[Y1 ])|Y1 ) = µ′ ((π ∗ T − c[W1 ])|W1 ) + cµ′ ((π ∗ [Y1 ] − [W1 ])|W1 ).\nCombining the above with (4.1), we see that the following choice of g satisfies the re-\nquirements of the lemma:\n\n                                1 −µ′ ((π ∗ [Y1 ] − [W1 ])|W1 )\n                              \u0014                                 \u0015\n                         g :=                                     .\n                                0                h\n\n\n\nTheorem 4.3. Assume that π : Z → X is a modification of X, then there is a modifica-\ntion π ′ : Z ′ → Z such that the flag Y• admits a lifting W• to Z ′ .\n\n                                                   15\n\f    By Hironaka’s Chow lemma [29, Corollary 2], we can relax the assumption to that π\nis a proper bimeromorphic morphism from a reduced complex space Z.\n    When X is projective, this result is already known, see [15, Theorem 2.9] for example.\n    The proof below relies on the embedded resolutions studied in [10] and [46]. Let Z be\nan analytic subset of a compact complex manifold M1 , that in turn is a submanifold of\na compact complex submanifold M2 . Due to [46, Theorem 2.0.2(4)] there exist canonical\ndesingularizations σ1 : M1′ → M1 and σ2 : M2′ → M2 of Z inside M1 and M2 respec-\ntively, so that a canonical embedding M1′ ,→ M2′ exists and makes the following diagram\ncommute:\n                                      M1′         M2′\n                                         σ1         σ2                               (4.2)\n\n                                         M1          M2 .\nMoreover, M1′ ,→ M2′ maps the (desingularized) strict transforms of Z onto each other.\nProof. We begin by setting W0 = Z. We will construct Wi inductively for each i. Assume\nthat for 0 ≤ i < n a smooth partial flag W0 ⊃ · · · ⊃ Wi has been constructed on a\nmodification πi : Zi → Z so that π ◦ πi restricts to bimeromorphic morphisms Wj → Yj\nfor each j = 0, . . . , i.\n    By Zariski’s main theorem, Wi → Yi is an isomorphism outside a codimension 2 subset\nof Yi . We let Wi+1 be the strict transform of Yi+1 in Wi . The problem is that Wi+1 is not\nnecessarily smooth.\n    We will further modify Zi and lift W1 , . . . , Wi+1 in order to make the flag smooth.\nTake the embedded resolution of (Wj , Wi+1 ), say Wj′ → Wj for each j = 0, . . . , i.\n    Due to (4.2), we have canonical embeddings Wi′ ,→ Wi−1     ′\n                                                                  ,→ · · · ,→ W0′ making the\nfollowing diagram commutative:\n\n                           Wi′             ′\n                                         Wi−1         ···        W0′\n                                                       ..\n                                                        .\n                            Wi           Wi−1         ···        W0\n      ′\nLet Wi+1 be the strict transform of Wi+1 in Wi′ . It suffices to define πi+1 as the morphism\nW0′ → Zi → Z and replace W0 ⊃ · · · ⊃ Wi+1 by W0′ ⊃ · · · ⊃ Wi+1   ′\n                                                                      .\n   As a consequence, we have the following useful approximation result.\nProposition 4.4. Let π : Z → X be a modification of X and ξ be a big class on X.\nAssume that Y• admits a lifting (W• , g) to Z. For any T ∈ Ω(Z, π ∗ ξ) we can find Kähler\ncurrents Tk ∈ A(X, ξ) such that\n  1. limk→∞ νY• (Tk ) = νW• (T )g −1 ;\n\n  2. Tk ⪯ π∗ T .\n   In particular, it follows that\n\n                                 ∆W• (Z, π ∗ ξ) = ∆Y• (X, ξ)g.\n\nThis is the transcendental generalization of the birational invariance of the classical Ok-\nounkov bodies.\n\n                                                16\n\fProof. By Theorem 4.3 there exists a modification π ′ : Z ′ → Z such that\n    (i) π ′∗ T = β + [D], where β is a smooth semipositive (1, 1)-form on Z ′ and D is an\n        effective Q-divisor;\n (ii) Y• admits a lifting (V• , h) to Z ′ .\n   Observe that (V• , g −1 h) is a lifting of Y• to Z ′ .\n   Note that π ′ is a composition of blowups with smooth centers. By the proof of [27,\nTheorem 3.5], one can find an effective exceptional divisor E on Z ′ and a smooth (1, 1)-\nform η in {E} such that π ′∗ T − εη is a Kähler current for any small ε > 0. This implies\nthat β − εη is a smooth Kähler form. Let us put for k ≫ 1\n                            βk := β − k −1 η and Dk := D + k −1 E.\nThen βk +[Dk ] ∈ (π◦π ′ )∗ ξ and by Lemma 2.11 one has Tk := (π◦π ′ )∗ (βk +[Dk ]) ∈ A(X, ξ).\n  We compute\n             νY• (Tk ) = νV• (βk + k −1 [E] + [D])h\n                       = νV• (π ′∗ T )h + k −1 νV• ([E])h = νW• (T )g + k −1 νV• ([E])h.\nLetting k → ∞ we conclude the first point. The second point is clear from the construc-\ntion of Tk .\n",
          "local_file": "source-extracts/2309.07584v3--lifting-flags-and-proof-bodies.txt",
          "sha256": "ed3d7bc16702cee22985fdb8805e0ecae2eba278f15a6f4587741490af3e2151",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "partial-bodies-and-proof-bodies",
          "first_line": 852,
          "last_line": 966,
          "first_textflow_page": 17,
          "last_textflow_page": 19,
          "literal": "5      Partial Okounkov bodies\nFor this section let ξ be a big class on X. Fix a smooth flag Y• = (Y0 ⊃ · · · ⊃ Yn ). We\nwill show that Property An holds with the help of partial Okounkov bodies, introduced\nand studied recently in [52] in case of big line bundles.\nDefinition 5.1. For R ∈ Ω(X, ξ), we set\n                            Ω(X, ξ; R) := {T ∈ Ω(X, ξ) : T ⪯ R} .\nThe partial Okounkov body of R is defined as the following closed convex subset of Rn≥0 :\n                           ∆(ξ; R) = ∆Y• (ξ; R) := νY• (Ω(X, ξ; R)).\n     We will fix R ∈ Ω(X, ξ) throughout this section.\nProposition 5.2. The partial Okounkov body ∆(ξ; R) is a convex body in Rn≥0 .\nProof. Since R is a Kähler current, we may fix a small ε > 0 such that R − εω is still a\nKähler current. This implies that ∆(ξ; R) contains the set ν(R) + ε∆({ω}). As we have\nseen in the proof of Proposition 3.4, the body ∆({ω}) contains a simplex, hence so does\n∆(ξ; R).\nExample 5.3. When R = [D] + β, where D is a Q-divisor on X and β ∈ Z+ (X) is a\ncurrent with bounded potentials, we have\n                            ∆Y• (ξ; R) = ∆Y• (ξ − {D}) + νY• ([D]).\nIndeed, suppose that T ∈ Ω(X, ξ − {D}), then T + [D] ∈ Ω(X, ξ; R), so\n                            ∆Y• (ξ; R) ⊃ ∆Y• (ξ − {D}) + νY• ([D]).\nOn the other hand, if T ∈ Ω(X, ξ; R), then T − [D] ∈ A(X, ξ − {D}), due to Lemma 2.5.\nIt follows from Lemma 3.1 that ν(T ) ∈ ∆Y• (ξ − {D}) + νY• ([D]).\n\n                                                 17\n\f   Let us put\n                           A(X, ξ; R) := {T ∈ A(X, ξ) : T ⪯ R}\nIt is helpful to know the following equivalent formulation of ∆(ξ; R).\nLemma 5.4. One has\n                                  ∆(ξ; R) = ν(A(X, ξ; R)).\nProof. The proof uses similar strategy as in Lemma 3.1. It suffices to argue that ν(G) ∈\n∆(ξ; R) for any G ∈ A(X, ξ; R). We might as well assume that G is a Kähler current,\notherwise one can replace G by (1 − ε)G + εR.\n     Write R = θ + ddc u and G = θ + ddc φ, with φ ≤ u. Since they are both Kähler\ncurrents, we can assume that R ≥ ω and G ≥ ω. For any sufficiently small rational\nnumber ε > 0, put uε := (1 + ε)u and φε := φ + εu. Then one has Rε := θ + ddc uε ≥ 21 ω\nand Gε := θ + ddc φε ≥ 21 ω. Let Gε,k := θ + ddc φε,k be the regularization sequence\nof Gε given in Theorem 2.8, which are Kähler currents with analytic singularities of\ntype (I(kφε ), k1 ). Since I(kφε ) ⊆ I(kuε ) and uε has analytic singularities, we can apply\n                                                                                 k\nBriançon–Skoda theorem as in the proof of Lemma 3.1 to see that φε,k+m ≤ k+m       uε +O(1)\nholds on X, where m ∈ N is independent of k (but it may depend on ε). Then for all\nsufficiently large k, one has φε,k ≤ u+O(1), i.e., Gε,k ∈ Ω(ξ, R). Moreover, by the proof of\nLemma 3.1, νY• (Gε ) = limk→∞ νY• (Gε,k ), since Gε has analytic singularities; meanwhile,\nit is clear that νY• (G) = limε→0 νY• (Gε ). So the desired assertion follows.\nProposition 5.5. One can find an increasing sequence Ri ∈ Ω(X, ξ) such that\n  1. E+ (Ri ) = EnK (ξ);\n     R\n  2. X Rin ↗ vol(ξ);\n              S\n  3. ∆(ξ) = i ∆(ξ; Ri ), so that volRn (∆(ξ; Ri )) ↗ volRn (∆(ξ)).\nProof. Since ν(Ω(X, ξ)) ⊆ Qn≥0 is a countable set, we can write ν(Ω(X, ξ)) = {a1 , a2 , . . . }.\nRPick nTi ∈ Ω(X, ξ) such that ν(Ti ) = ai and also pick a sequence Gi ∈ Ω(X, ξ) such that\n  X\n     Gi → vol(ξ). Choose R0 ∈ Ω(X, ξ) such that E+ (R0 ) = EnK (ξ). Then applying\n Lemma 2.9 repeatedly, we choose Ri ∈ Ω(X, ξ) so that it is less singular than Ti , Gi and\n Ri−1 . So Ri is an increasing sequence, which clearly satisfies (1) and (3). That (2) holds\n follows from the monotonicity of Monge–Ampère masses, see [5, Theorem 1.16] or [50,\n Theorem 1.2].\nLemma 5.6. Let R ∈ Ω(X, ξ). Take a modification π : Z → X such that the flag Y•\nadmits a lifting (W• , g) to Z and π ∗ R = β + [D], where β is a smooth semipositive form\non Z and D is an effective Q-divisor. Then\n\n                            ∆Y• (ξ; R)g = ∆W• ({β}) + νW• ([D]).                          (5.1)\n\nProof. For any T ∈ Ω(X, ξ; R), by Lemma 2.5 π ∗ T −[D] is a positive current with analytic\nsingularities in {β}. So one has\n\n            νW• (π ∗ T ) = νW• (π ∗ T − [D]) + νW• ([D]) ∈ ∆W• ({β}) + νW• ([D]).\n\nTherefore, νY• (T ) ∈ ∆W• ({β}) + νW• ([D]) g −1 , implying that\n                                               \u0001\n\n                          ∆Y• (ξ; R) ⊆ ∆W• ({β}) + νW• ([D]) g −1 .\n                                                                \u0001\n\n\n                                              18\n\f    On the other hand, for any Kähler current S ∈ Ω(Z, {β}), note that S + [D] belongs\nto Ω(Z, π ∗ ξ) and is more singular than π ∗ R.\n    By Proposition 4.4, there exist Kähler currents Tk ∈ A(X, ξ) s.t. limk→∞ νY• (Tk ) =\nνV• (S + [D])g −1 and Tk ⪯ R.\n    It follows from Lemma 5.4 that νW• (S + [D]) ∈ ∆Y• (ξ; R)g, finishing the proof of\n(5.1):\n                          ∆W• ({β}) + νW• ([D]) g −1 ⊆ ∆Y• (ξ; R).\n                                                \u0001\n\n\n\n     We hope to show that partial Okounkov bodies have the following property:\nProperty Bn . Assume that dim X = n and ξ is big. For any R ∈ Ω(X, ξ) one has\n                           Z\n                              Rn = n! volRn (∆(ξ; R)).\n                                  X\n\nLemma 5.7. Property An and Property Bn are equivalent.\nProof. That Property Bn implies Property An is immediate thanks to Proposition 5.5.\nLet us prove the other direction.\n   Fix R ∈ Ω(X, ξ). By Theorem 4.3, there is a modification π : Z → X such that\n    (i) π ∗ R = β + [D], where β is a smooth semipositive form on Z and D is an effective\n        Q-divisor;\n (ii) The flag Y• admits a lifting (W• , g) to Z.\n                                                 \u0001\nBy Lemma 5.6, ∆Y• (ξ; R)g = ∆W• ({β}) + νW• ([D]) . Since det g = 1, we obtain that:\n\n              volRn (∆Y• (ξ; R)) = volRn (∆Y• (ξ; R)) · det g = volRn (∆W• ({β}))\n                                                                   Z\n                                                                 1\n                                                              =        βn\n                                                                n! Z\n                                                                   Z\n                                                                 1\n                                                              =        Rn .\n                                                                n! X\n\n\n     We shall see in §7 that Property Bn holds for all n ≥ 1, and so does An .",
          "local_file": "source-extracts/2309.07584v3--partial-bodies-and-proof-bodies.txt",
          "sha256": "20b36b80561e98eb376d229ab812a8cb129360c59f058f4d936e3670d6be5439",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "volume-theorem-and-entire-section-7-proof",
          "first_line": 1137,
          "last_line": 1415,
          "first_textflow_page": 22,
          "last_textflow_page": 27,
          "literal": "7      The volume identity\nUnless specified otherwise, in this section ξ is a big class on X and dim X = n. We also\nfix a smooth flag Y• = (X = Y0 ⊃ · · · ⊃ Yn ) on X. Define\n\n              νmin (ξ, Y1 ) :=     inf       ν(T, Y1 ),        νmax (ξ, Y1 ) :=      sup       ν(T, Y1 ).\n                                 T ∈Ω(X,ξ)                                         T ∈Ω(X,ξ)\n\n\nLemma 7.1. One has νmin (ξ, Y1 ) < νmax (ξ, Y1 ). Moreover,\n\n                             ν1 (Ω(X, ξ)) = [νmin (ξ, Y1 ), νmax (ξ, Y1 )],\n\nwhere ν1 is the first component of the valuative map ν.\n\nProof. Pick any T ∈ Ω(X, ξ), then T − νmin (ξ, Y1 )[Y1 ] is a Kähler current, which implies\nthat ξ − νmin (ξ, Y1 ){Y1 } is a big class. So for small ε > 0, ξ − (νmin (ξ, Y1 ) + ε){Y1 } is\na big class as well. So there exists S ∈ Ω(X, ξ) with ν(S, Y1 ) ≥ νmin (ξ, Y1 ) + ε, giving\nνmin (ξ, Y1 ) < νmax (ξ, Y1 ). The second assertion follows from the convexity of Ω(X, ξ).\n\n\n                                                          22\n\fProposition 7.2. Assume that n ≥ 2. One has\n                                      Z νmax (ξ,Y1 )\n                         vol(ξ) = n                    volX|Y1 (ξ − t{Y1 }) dt.\n                                       νmin (ξ,Y1 )\n\nProof. We first observe that for any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )), one has\n\n                                   Y1 ∩ K(ξ − t{Y1 }) ̸= ∅.\n\nIn fact, by Lemma 7.1, for t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) lying in a dense subset, there\nexists T ∈ Ω(X, ξ) with ν(T, Y1 ) = t. So T − t[Y1 ] is a Kähler current in ξ − t{Y1 } with\nY1 ⊈ E+ (T − t[Y1 ]).\n    Clearly, vol(ξ) = vol(ξ − νmin (ξ, Y1 ){Y1 }). By the continuity of vol(·) [12, Proposition\n4.7], one thus has\n                        vol(ξ) = lim vol(ξ − (νmin (ξ, Y1 ) + ε){Y1 }).\n                                   ε↘0\n\nWe can apply Theorem 2.14 to the big class ξ − (νmin (ξ, Y1 ) + ε){Y1 } to get\n                                         Z νmax (ξ,Y1 )\n                       vol(ξ) = lim n                       volX|Y1 (ξ − t{Y1 }) dt\n                                ε↘0       νmin (ξ,Y1 )+ε\n                                   Z νmax (ξ,Y1 )\n                              =n                    volX|Y1 (ξ − t{Y1 }) dt\n                                    νmin (ξ,Y1 )\n\nas desired.\n   Now for any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )), we look at the following restricted volume\n                                                               Z\n                     volX|Y1 (ξ − t{Y1 }) =           sup         T |n−1\n                                                                     Y1\n                                                      T ∈Ω(X,ξ−t{Y1 })   Y1\n\n\nand the t-slice of the Okounkov body\n\n                            ∆t (ξ) := {x ∈ Rn−1 : (t, x) ∈ ∆(ξ)}.\n\nWe shall prove that they are related in the following way (cf. [35, Corollary 4.25(i)]).\n\nProperty Cn . If n ≥ 2, then for any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )), one has\n\n                        volX|Y1 (ξ − t{Y1 }) = (n − 1)! volRn−1 (∆t (ξ)).\n\nLemma 7.3. Assume that n ≥ 2. Property Cn implies Property An .\n\nProof. By Lemma 7.1, we can express volRn (∆(ξ)) as\n                                           Z νmax (ξ,Y1 )\n                        volRn (∆(ξ)) =                       volRn−1 (∆t (ξ)) dt.\n                                             νmin (ξ,Y1 )\n\nSo we conclude from Proposition 7.2.\n\n\n\n\n                                                      23\n\f    Our goal is now to show that for n ≥ 2, Property Bn−1 implies Property Cn . Since we\nalready know by Lemma 5.7 that Property An and Property Bn are equivalent, this will\ntogether with Lemma 7.3 complete the induction argument and thus prove Property An\nfor all n.\n    Note that both maps t 7→ volX|Y1 (ξ − t{Y1 }) and t 7→ volRn−1 (∆t (ξ)) are continuous:\nthe former continuity is due to [37, Corollary 4.11] and the latter follows from the Brunn–\nMinkowski inequality. Therefore, to establish Property Cn it is enough to show that\n\n                          volX|Y1 (ξ − t{Y1 }) = (n − 1)! volRn−1 (∆t (ξ))\n\nfor all rational t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )).\n    For t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q, we introduce t-slices of Ω(X, ξ) and A(X, ξ) and\nshow how they are connected to the t-slice of the Okounkov body:\n\n                           Ωt (X, ξ) := {T ∈ Ω(X, ξ) : ν(T, Y1 ) = t},\n\n                           At (X, ξ) := {T ∈ A(X, ξ) : ν(T, Y1 ) = t}.\n\nLemma 7.4. For any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q, one has\n\n                           {t} × ∆t (ξ) = ν(Ωt (X, ξ)) = ν(At (X, ξ)).\n\nProof. It is clear that\n\n                           ν(Ωt (X, ξ)) ⊆ ν(At (X, ξ)) ⊆ {t} × ∆t (ξ).\n\nTo finish we will argue that {t} × ∆t (ξ) ⊆ ν(Ωt (X, ξ)). Let a ∈ {t} × ∆t (ξ). Then there\nexists a sequence Ti ∈ Ω(X, ξ) such that ν(Ti ) → a. So in particular, ti := ν(Ti , Y1 ) → t.\nPick S, G ∈ Ω(X, ξ) such that s := ν1 (S, Y1 ) < t and g := ν(G, Y1 ) > t. Define\n                                 (\n                                                  −t\n                                   t\n                                    t−s\n                                      −s\n                                         Ti + ttii−s S, if ti ≥ t,\n                            Si := g−t\n                                    i\n                                               t−ti\n                                   g−ti i\n                                         T + g−ti G, if ti < t.\n\nThen Si ∈ Ωt (X, ξ) for i ≫ 0 and limi ν(Si ) = limi ν(Ti ) = a, hence a ∈ ν(Ωt (X, ξ)).\n   We are now ready to prove that Property Bn−1 implies Property Cn :\n\nLemma 7.5. Assume that n ≥ 2, then Property Bn−1 implies Property Cn .\n\nProof. Pick any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q. Put ξt := ξ − t{Y1 } for simplicity. It\nsuffices to show the following: there is an increasing sequence Ri ∈ Ω(X, ξt ) such that\n\n (1) E+ (Ri ) = EnK (ξt ) for all i;\n\n (2) Ri |Y1 has positive mass and Y1 Ri |n−1\n                                  R\n                                          Y1 ↗ volX|Y1 (ξt );\n\n (3) One has Y1 Ri |n−1\n               R\n                      Y1  = (n − 1)! volRn−1 (∆t,i ), where ∆t,i is the (n − 1)-dimensional\n     partial Okounkov body ∆(ξt |Y1 ; Ri |Y1 ) of ξt |Y1 with respect to Ri |Y1 , which is defined\n     using the truncated flag Y1 ⊃ Y2 ⊃ · · · ⊃ Yn ;\n\n (4) ∆t,i is an increasing sequence of (n − 1)-dimensional convex bodies contained in\n     ∆t (ξ) such that volRn−1 (∆t,i ) ↗ volRn−1 (∆t (ξ)).\n\n                                                24\n\f    The above conditions would imply volX|Y1 (ξ − t{Y1 }) to equal (n − 1)! volRn−1 (∆t (ξ))\nfor any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q, hence proving Property Cn .\n    To construct the sequence Ri , first note that the set νY• (Ωt (X, ξ)) ⊂ Qn≥0 is countable.\nSo one can write ν(Ωt (X, ξ)) = {a1 , a2 , . . . , ai , . . . } with ai ∈ Qn≥0 . Let a′i ∈ Qn−1≥0 be such\n                 ′\nthat ai = (t, ai ). Pick Ti ∈ Ωt (ξ) so that νY• (Ti ) = ai . Fix RR0 ∈ Ω(X, ξt ) so that\nE+ (R0 ) = EnK (ξt ). Also pick a sequence Gi ∈ Ω(X, ξt ) so that Y1 Gn−1               i    → volX|Y1 (ξt ).\nApplying Lemma 2.9 inductively, we can find Ri ∈ Ω(X, ξt ) that is less singular than\nTi − t[Y1 ], Gi and Ri−1 . So Ri ∈ ξt is an increasing sequence of Kähler currents with\nanalytic singularities precisely on EnK (ξt ), showing (1). That (2) holds is due to [50,\nTheorem 1.2] and (3) holds thanks to Property Bn−1 . It remains to argue (4).\n    Let νY′ • : A(Y1 , ξt |Y1 ) → Qn−1  ≥0 denote the valuative map constructed using the flag\nY1 ⊃ Y2 ⊃ · · · ⊃ Yn on Y1 . Then one has that a′i ∈ νY′ • (A(Y1 , ξt |Y1 ; Ri |Y1 )), since (Ti −\nt[Y1 ])|Y1 ∈ A(Y1 , ξt |Y1 ; Ri |Y1 ) and a′i = νY′ • ((Ti − t[Y1 ])|Y1 ). Thus, a′i ∈ ∆t,i by Lemma 5.4,\n                                     S\nwhich implies that ∆t (ξ) ⊆ i ∆t,i by Lemma 7.4.\n    Next, we show that ∆t,i ⊆ ∆t (ξ) holds for all i. By Theorem 4.3, there are modifica-\ntions πi : Xi → X such that\n  (i) πi∗ Ri = βi +[Di ], where βi is a smooth semipositive form on Xi and Di is an effective\n      Q-divisor on Xi ;\n                                                  (i)\n (ii) The flag Y• admits a lifting (Y• , gi−1 ) to Xi .\n                        (i)\n    Note that Y1 is the strict transform of Y1 , and it is not contained in Di (as ν(Ri , Y1 ) =\n0). By the Lelong–Poincaré formula, the restricted current [Di ]|Y (i) only has divisorial\n                                                                                          1\ncomponents in its Siu decomposition. Let ν ′ (i) be the Qn−1\n                                                         ≥0 -valued map determined by\n                                                             Y•\n            (i)                     (i)   (i)\nthe flag Y1 ⊃ · · · ⊃ Yn on Y1 . By Lemma 4.2, there is hi ∈ SLn−1 (Z) such that\n                               νY′ (i) (πi∗ T )hi = νY′ • (T ) for all T ∈ Ω(Y1 , ξt |Y1 ).\n                                     •\n\n\nFrom the proof of Lemma 4.2, we see that hi is obtained from gi with the first row and\nthe first column removed.\n   Now, for any T ∈ Ω(Y1 , ξt |Y1 ; Ri |Y1 ), Lemma 2.5 implies that Si := πi∗ T − [Di ]|Y (i) is a\n                                                                                                         1\n                              (i)\npositive current on Y1 in the semipositive class {βi |Y (i) } and Si has analytic singularities.\n                                                       1\n   Fix a smooth Kähler form ωi on Xi . Then for any ε > 0, Si,ε := Si +εωi |Y (i) is a Kähler\n                                                                                                  1\n                  (i)\ncurrent on Y1            in the Kähler class (βi + εωi )|Y (i) with analytic singularities. Note that\n                                                                  1\n                                                                                                             (i)\n(merely from Definition 2.6) it is unclear if Si,ε has gentle analytic singularities on Y1 or\nnot, but thanks to Theorem 2.8 one can approximate Si,ε by a sequence, say {Si,ε,k }k∈N ,\n                                         (i)\nwith gentle analytic singularities on Y1 .\n   Applying Theorem 6.4, we get S̃i,ε,k ∈ {βi + εωi }, currents on Xi , extending Si,ε,k for\neach k. Moreover, S̃i,ε,k has analytic singularities on Xi . Then (the proof of) Lemma 3.1\nimplies that\n             (0, νY′ (i) (Si )) = (0, νY′ (i) (Si,ε )) = (0, lim νY′ (i) (Si,ε,k ))\n                        •                  •                    k→∞       •\n\n                                                        = lim νY (i) (S̃i,ε,k ) ∈ ∆Y (i) ({βi + εωi })\n                                                          k→∞         •               •\n\n\nfor any ε > 0. By Proposition 3.3(3) we can let ε → 0 to find that\n                 0, νY′ (i) (πi∗ T ) ∈ ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]),\n                                    \u0001\n                               •                  •                                   •\n\n\n\n                                                           25\n\fwhere we used (0, ν ′ (i) ([Di ]|Y (i) )) = νY (i) ([Di ]). Since (0, νY′ • (T )) = (0, ν ′ (i) (πi∗ T )hi ) =\n                            Y•       1        •                                          Y•\n(0, ν ′ (i) (πi∗ T ))gi , we have that\n     Y•\n\n                    (0, νY′ • (T )) ∈ ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]) gi .\n                                                                                  \u0001\n                                         •                                     •\n\n\nThus, we see that\n\n                    {0} × ∆t,i ⊆ ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]) gi .\n                                                                             \u0001\n                                         •                                     •\n\n                                                                             (i)\n   On the other hand, for any G ∈ Ω(Xi , {βi }) with ν(G, Y1 ) = 0, G+[Di ] is an element\nin Ω(πi∗ ξt ). One can then apply Proposition 4.4 to find a sequence Gk ∈ A(X, ξt ) such\nthat\n\n                     νY (i) (G + [Di ]) = lim νY (i) (πi∗ Gk )\n                       •                     k→∞   •\n\n                                        = lim νY• (Gk )gi−1 ∈ {0} × ∆t (ξ) gi−1 ,\n                                                                          \u0001\n                                             k→∞\n\nwhere the last inclusion follows from Lemma 7.4 (since Gk + t[Y1 ] ∈ At (X, ξ), as t ∈ Q).\nThus,\n                 ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]) gi ⊆ {0} × ∆t (ξ).\n                                                             \u0001\n                        •                                   •\n\nTherefore, ∆t,i ⊆ ∆t (ξ) follows, as claimed.\n                                                            S\n   From the above discussions we conclude that ∆t (ξ) = i ∆t,i . Moreover, since Ri is\nan increasing sequence, we see that ∆t,i is an increasing sequence of (n − 1)-dimensional\nconvex bodies contained in ∆t (ξ). So we deduce that volRn−1 (∆t,i ) ↗ volRn−1 (∆t (ξ)),\nconcluding the proof of (4).\n   We summarize our findings in the next result that proves both Theorem 1.1 and\nCorollary 1.2:\nTheorem 7.6. Let ξ be a big cohomology class on X. Let Y• be a flag on X. Then one\ncan associate to it a natural compact convex set ∆Y• (ξ) with ξ so that\n                                                                1\n                                      volRn (∆Y• (ξ)) =            vol(ξ).\n                                                                n!\nProof. Let n = dim X. Let us first assume that ξ is big. We will show that Property An\nand Property Bn hold for any dimension n ≥ 1 and Property Cn holds for any n ≥ 2.\nWe have proved the following implications:\n   1. An ⇐⇒ Bn for n ≥ 1 by Lemma 5.7;\n   2. Bn−1 =⇒ Cn for n ≥ 2 by Lemma 7.5;\n   3. Cn =⇒ An for n ≥ 2 by Lemma 7.3.\nBy Lemma 3.6 Property A1 holds, so we conclude the big case by induction.\n    As a simple corollary, we obtain the result for pseudoeffective classes as well:\nCorollary 7.7. Let ξ be a pseudoeffective cohomology class on X. Let Y• be a flag on\nX. Then one can associate to it a natural compact convex set ∆Y• (ξ) with ξ so that\n                                                                1\n                                      volRn (∆Y• (ξ)) =            vol(ξ).\n                                                                n!\n                                                       26\n\fProof. Due to the previous theorem, we can assume that ξ is pseudoeffective but not big.\nIn this case vol(ξ) = 0. By the definition of ∆Y• (ξ) (recall (3.1)) we obtain that\n\n                           volRn (∆Y• (ξ)) ≤ volRn (∆Y• (ξ + ε{ω})) → 0,\n\nthanks to the continuity of the volume functional on the pseudoeffective cone [12].",
          "local_file": "source-extracts/2309.07584v3--volume-theorem-and-entire-section-7-proof.txt",
          "sha256": "66070cf0ccb51a97ec6777db24d846681ac4cdf816e2a055ed9e10cef740bf85",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        }
      ],
      "application_checks": [
        "Applied only on compact Kähler manifolds with a specified globally smooth connected complete flag.",
        "Definition 5.1 requires a Kähler current with gentle analytic singularities. R_epsilon=[D]+beta+epsilon*Omega has these properties for rational smooth D and smooth semipositive beta.",
        "Example 5.3 is used only with residual beta+epsilon*Omega Kähler. The two inclusions are also proved in the argument.",
        "Lemma 3.1 is applied only to positive currents with analytic singularities in a big residual class.",
        "Theorem 7.6 is applied to the Kähler surface class kappa_a, never to infer dimension from zero three-dimensional volume.",
        "Section 2 initially fixes a big class. For Lemma 2.1 the argument reproduces its removable-singularity proof explicitly, thereby checking the same psh pullback bijection in a nonbig pullback class; it is not applied to an arbitrary class on a modification. No independence of arbitrary modified flags is claimed.",
        "The class-level Corollary 7.7 and its proof do not assert a lower-dimensional numerical theorem or retention of a prescribed potential."
      ]
    },
    {
      "id": "Xia",
      "title": "Partial Okounkov bodies and Duistermaat--Heckman measures of non-Archimedean metrics",
      "exact_arxiv_version": "2112.04290v2",
      "printed_date": "13 Apr 2024",
      "public_source": "https://arxiv.org/pdf/2112.04290v2",
      "pdf_location": "/workspace/research/shared-sources/P15.3-arxiv-2112.04290v2-20261004.pdf",
      "pdf_sha256": "0847fc4313e630946e8ff122ab2de587185eb9067d6c3efe2a65dfcfc8e72f2f",
      "supplied_extract_location": "/workspace/research/shared-sources/P15.3-arxiv-2112.04290v2-20261004.txt",
      "extract_sha256": "d59c0231ec64871b6a21657bcc3a952af8b2e9c975eee07db1d99f0ef4cf7273",
      "byte_identical_local_extract": "source-extracts/2112.04290v2-full.txt",
      "source_line_count": 2700,
      "line_number_convention": "UTF-8 text.split('\\n'); one-based indexing; trailing empty line counted; form feeds remain inside lines",
      "passages": [
        {
          "id": "projective-domain-and-introduction-theorems",
          "first_line": 33,
          "last_line": 119,
          "first_textflow_page": 1,
          "last_textflow_page": 3,
          "literal": "                                           1.1. Background. Let X be an irreducible smooth projective variety of dimension n and L be\n                                           a big holomorphic line bundle on X. Given any admissible ﬂag X = Y0 ⊇ Y1 ⊇ · · · ⊇ Yn on\n                                           X (see Deﬁnition 2.7 for the precise deﬁnition), one can attach a natural convex body ∆(L) of\n                                           dimension n to L, generalizing the classical Newton polytope construction in toric geometry. This\n                                           construction was ﬁrst considered by Okounkov [Oko96; Oko03] and then extended by Lazarsfeld–\n                                           Mustat, ă [LM09] and Kaveh–Khovanskii [KK12]. The convex body ∆(L) is known as the Okounkov\n                                           body or Newton–Okounkov body associated with L (with respect to the given ﬂag). We brieﬂy recall\n                                           its deﬁnition: given any non-zero s ∈ H0 (X, Lk ), let ν1 (s) be the vanishing order of s along Y1 .\n                                           Then s can be regarded as a section of H0 (X, Lk ⊗ OX (−ν1 (s)Y1 )). It follows that s1 := s|Y1 is a\n                                           non-zero section of L|kY1 ⊗ OX (−ν1 (s)Y1 )|Y1 . We can then repeat the same procedure with s1 , Y2\n                                           in place of s, Y1 . Repeating this construction, we end up with ν(s) = (ν1 (s), . . . , νn (s)) ∈ Nn . In\n                                           fact, ν extends naturally to a rank n valuation on C(X). Consider the semigroup\n                                                                               n                                                o\n                                                                     Γ(L) := (ν(s), k) ∈ Zn+1 : k ∈ N, s ∈ H0 (X, Lk )× .\n\n                                             Keywords—Okounkov bodies, pseudo-effective line bundles, convex bodies, pluri-subharmonic functions\n                                             MSC : 14M25, 32U05\n                                             Mingchen Xia, Institut de Mathématiques de Jussieu-Paris Rive Gauche\n                                             Email address, mingchen@imj-prg.fr\n                                             Homepage, http://mingchenxia.github.io/home/.\n                                                                                                   1\n\f2                                          MINGCHEN XIA\n\nThen ∆(L) is the intersection of the closed convex cone in Rn+1 generated by Γ(L) with the\nhyperplane {(x, 1) : x ∈ Rn }. A key property of ∆(L) is that the Lebesgue volume of ∆(L) is\nproportional to the volume of the line bundle L:\n                                                    1\n(1.1)                                   vol ∆(L) = hLn i.\n                                                    n!\nHere h•i denotes the movable intersection product in the sense of [BDPP13; BFJ09].\n   In [LM09], Lazarsfeld–Mustat, ă showed moreover that ∆(L) depends only on the numerical class\nof L. Conversely, it is shown by Jow [Jow10] that the information of all Okounkov bodies with\nrespect to various ﬂags actually determines the numerical class of L. In other words, Okounkov\nbodies can be regarded as universal numerical invariants of big line bundles.\n   This paper concerns a similar problem. Assume that L is equipped with a singular plurisubhar-\nmonic (psh) metric φ. We will construct universal invariants of the singularity type of φ. We call\nthese universal invariants the partial Okounkov bodies of (L, φ).\n1.2. Main results. Let us explain more details about the construction of partial Okounkov bodies.\nRecall that any admissible ﬂag on X induces a rank n valuation on C(X) with values in Zn . We\nwill work more generally with such valuations, not necessarily coming from admissible ﬂags on X.\nWe deﬁne a set\n                             n                                                   o\n(1.2)             Γ(L, φ) := (ν(s), k) ∈ Zn+1 : k ∈ N, s ∈ H0 (X, Lk ⊗ I(kφ))×\nsimilar to Γ(L). Here I(•) denotes the multiplier ideal sheaf in the sense of Nadel. However, a key\ndiﬀerence here is that Γ(L, φ) is not a semigroup in general. Thus, the constructions in both [LM09]\nand [KK12] break down. We will show that in this case, there is still a canonical construction of\nOkounkov bodies.\n   Before stating our main theorem, let us recall the deﬁnition of volume. The volume of (L, φ) is\ndeﬁned as\n                                                 1\n                               vol(L, φ) := lim n h0 (X, Lk ⊗ I(kφ)).\n                                            k→∞ k\nThe existence of this limit is proved in [DX21].\nTheorem A. Let (L, φ) be as above. Assume that vol(L, φ) > 0. Then there is a convex body\n∆(L, φ) ⊆ ∆(L) associated with (L, φ) satisfying\n(1.3)                                 vol ∆(L, φ) = vol(L, φ).\n                                              R\n   Moreover, ∆(L, φ) is continuous in φ if X (ddc φ)n > 0. Here the set of φ is endowed with\nthe dS -pseudometric in the sense of [DDNL21b] and the set of convex bodies is endowed with the\nHausdorff metric.\n   Define                      n                                       o\n                         Γk := k−1 ν(s) ∈ Rn : s ∈ H0 (X, Lk ⊗ I(kφ))×\nand let ∆k denote the convex hull of Γk . Then\n(1.4)                                      ∆k → ∆(L, φ)\nwith respect to the Hausdorff metric if vol(L, φ) > 0.\n   Observe that the last assertion actually uniquely determines ∆(L, φ), so ∆(L, φ) can be regarded\nas canonically attached to the given data (X, L, φ, ν).\n   The convex body ∆(L, φ) is called the partial Okounkov body of (L, φ) with respect to the given\nvaluation. Here the word partial refers to the fact that the partial Okounkov bodies are contained\nin ∆(L). One should not confuse them with the notion of Okounkov bodies with respect to partial\nﬂags.\n   We will also extend the deﬁnition to the case vol(L, φ) = 0 in Section 5.6, at the expense of\nlosing continuity in φ.\n\f                                        PARTIAL OKOUNKOV BODIES                                   3\n\n  Observe that (1.3) bears strong resemblance with (1.1). In fact, when φ has minimal singularities,\n∆(L, φ) = ∆(L) and (1.3) just reduces to (1.1).\n  The second main result says that partial Okounkov bodies uniquely determine the I-singularity\ntype of φ.\nTheorem B. Let L be a big line bundle on X. Let φ, φ′ be two singular psh metrics on L with\npositive volumes. Then the following are equivalent:\n    (1) φ ∼I φ′ .\n    (2) ∆(L, φ) = ∆(L, φ′ ) for all rank n valuations on C(X) taking values in Zn .\n   Recall that φ ∼I φ′ means I(kφ) = I(kφ′ ) for all real k > 0. This relation is studied in detail\nin [DX22; DX21]. It captures a lot of important information about the singularity of a psh metric.\nTheorem B should be regarded as a metric analogue of Jow’s theorem.\n   As a byproduct of our proof of Theorem B, we reprove a formula computing the generic Lelong",
          "local_file": "source-extracts/2112.04290v2--projective-domain-and-introduction-theorems.txt",
          "sha256": "472b877be180f1cec774ad7d68423ea91c614aed49aeca721523285ca63d91d7",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "P-C-and-I-definitions-and-proof",
          "first_line": 371,
          "last_line": 429,
          "first_textflow_page": 8,
          "last_textflow_page": 9,
          "literal": "2.3. Model potentials and I-model potentials. Let X be a connected compact Kähler mani-\nfold of dimension n and θ be a smooth closed real (1, 1)-form representing a (1, 1)-cohomology class\n[θ]. Deﬁne Vθ := sup{ϕ ∈ PSH(X, θ) : ϕ ≤ 0}. For any two ϕ, ψ ∈ PSH(X, θ), we say ϕ is more\nsingular than ψ and write [ϕ] \u0016 [ψ] if there is a constant C such that ϕ ≤ ψ + C. When ϕ \u0016 ψ\nand ψ \u0016 ϕ, we say that they have the same singularity type. We write θϕ = θ + ddc ϕ.\nDefinition 2.9. Let ϕ ∈ PSH(X, θ). Deﬁne\n                         \u001a                                        Z                       Z                      \u001b\n(2.2)       θ\n           C [ϕ] := sup* ψ ∈ PSH(X, θ) : [ϕ] \u0016 [ψ], ψ ≤ 0,                θϕk ∧ θVn−k\n                                                                                   θ\n                                                                                      =       θψk ∧ θVn−k\n                                                                                                       θ\n                                                                                                          , ∀k       .\n                                                                      X                   X\nIf C θ [ϕ] = ϕ, we say ϕ is a model potential. We omit θ from the notation if there is no risk of\nconfusion.\n  Here and in the sequel the Monge–Ampère type operators are taken in the non-pluripolar sense\n[BEGZ10].\nProposition 2.10 ([DDNL21b, R Proposition   2.6]). For any ϕ ∈ PSH(X, θ), C θ [ϕ] is a model\npotential in PSH(X, θ). When X θϕn > 0 we have\n                                             C θ [ϕ] = P θ [ϕ],\nwhere\n(2.3)                      P θ [ϕ] := sup* {ψ ∈ PSH(X, θ) : [ψ] \u0016 [ϕ], ψ ≤ 0} .\nIn general, we only have\n(2.4)                              C θ [ϕ] = lim P θ [(1 − ǫ)ϕ + ǫVθ ].\n                                            ǫ→0+\n\n    We omit θ from the notation P θ [ϕ] if there is no risk of confusion.\nDefinition 2.11. A birational model of X is a projective birational morphism π : Y → X from a\nsmooth projective variety Y to X.\n   Recall that I(ϕ) denotes the multiplier ideal sheaf of a qpsh function ϕ on X in the sense of\nNadel, namely the coherent subsheaf of OX consisting of functions f such that |f |2 exp(−ϕ) is\nlocally integrable.\nDefinition 2.12. Let ϕ, ψ be two quasi-psh functions, we say ϕ \u0016I ψ if the following equivalent\nconditions are satisﬁed:\n   (1) I(kϕ) ⊆ I(kψ) for all real k > 0.\n   (2) I(kϕ) ⊆ I(kψ) for all integer k > 0.\n   (3) For any birational model π : Y → X and any y ∈ Y , we have ν(π ∗ ϕ, y) ≥ ν(π ∗ ψ, y).\nThe equivalence between (1) and (3) is just [DX22, Corollary 2.16]. The equivalence between (2)\nand (3) follows from [DX22, Proposition 2.14].\n  We say ϕ ∼I ψ if ϕ \u0016I ψ and ψ \u0016I ϕ.\n  Given any ϕ ∈ PSH(X, θ), we deﬁne\n                           P θ [ϕ]I := sup {ψ ∈ PSH(X, θ) : ψ \u0016I ϕ, ψ ≤ 0} .\nWe omit θ when there is no risk of confusion. We say ϕ is I-model if ϕ = P [ϕ]I .\n   It is shown in [DX22, Proposition 2.18] that P [ϕ]I ∈ PSH(X, θ) and ϕ ∼I P [ϕ]I . Moreover,\nP [ϕ]I is always I-model. We can also talk about the ∼I relation of two psh metric on L in the\nobvious manner.\n   Typical model potentials are not I-model, however, the converse is true:\nProposition 2.13. If ψ ∈ PSH(X, θ) is an I-model potential then it is model.\n\f                                    PARTIAL OKOUNKOV BODIES                                         9\n\nProof. We need to show that ψ ∼I C[ψ]. Let π : Z → X be a birational modiﬁcation. Let z ∈ Z.\nAs ψ ≤ C[ψ] + C for some constant C, it suﬃces to show that\n                                        ν(C[ψ], z) ≥ ν(ψ, z).\nHere ν(ψ, z) denotes the Lelong number of π ∗ ψ at z. By (2.4) and the upper semi-continuity of\nLelong numbers (see [GZ17, Page 73, Exercise 2.7]), we ﬁnd\n          ν(C[ψ], z) ≥ lim ν(P [(1 − ǫ)ψ + ǫVθ ], z) = lim ν((1 − ǫ)ψ + ǫVθ , z) = ν(ψ, z).\n                       ǫ→0+                                   ǫ→0+\nWe conclude our assertion.                                                                         \u0003",
          "local_file": "source-extracts/2112.04290v2--P-C-and-I-definitions-and-proof.txt",
          "sha256": "c31672f6c01afc06da5429d404711db3ae87f7f9da628e154b2a95e5283a0223",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "ideal-volume-and-I-envelope-formula",
          "first_line": 458,
          "last_line": 494,
          "first_textflow_page": 9,
          "last_textflow_page": 10,
          "literal": "2.5. Quasi-equisingular approximations. We recall the concept of quasi-equisingular approxi-\nmations in the sense of [Cao14; DPS01].\n   Let X be a connected compact Kähler manifold of dimension n and θ (resp. θi , i = 1, . . . , n)\nbe a smooth real (1, 1)-form representing a pseudo-eﬀective (1, 1)-cohomology class [θ] (resp. [θi ]).\nTake a Kähler form ω on X.\nDefinition 2.16. Let ϕ ∈ PSH(X, θ). A quasi-equisingular approximation is a sequence ϕj ∈\nPSH(X, θ + ǫj ω) with ǫj → 0 such that\n   (1) ϕj → ϕ in L1 .\n   (2) ϕj has analytic singularities.\n   (3) ϕj+1 ≤ ϕj .\n   (4) For any δ > 0, k > 0, there is j0 > 0 such that for j ≥ j0 ,\n                                 I(k(1 + δ)ϕj ) ⊆ I(kϕ) ⊆ I(kϕj ).\n  The existence of a quasi-equisingular approximation follows from the arguments in [Cao14;\nDem15; DPS01].\n\f10                                                      MINGCHEN XIA\n\n2.6. Volumes of Hermitian pseudo-effective line bundles. Let X be a smooth irreducible\nprojective variety of dimension n.\nDefinition 2.17. A Hermitian pseudo-effective(psef) line bundle on X is a pair (L, φ), where L is\na pseudo-eﬀective line bundle on X and φ is a psh metric on L.\n  When L is big, we say (L, φ) is a Hermitian big line bundle.\n  Let (L, φ) be a Hermitian psef line bundle on X. In this section, we recall the main results in\n[DX22; DX21] concerning the volume of (L, φ).\nDefinition 2.18. The volume of (L, φ) is deﬁned as\n                                                             1 0\u0010      k\n                                                                                \u0011\n                                   vol(L, φ) := lim             h X, L   ⊗ I(kφ)  .\n                                                        k→∞ k n\n\n  The existence of the limit follows from [DX21, Theorem 1.1].\n  We take a smooth Hermitian metric h on L. Set θ = c1 (L, h). Then we can identify φ with a\nθ-psh function ϕ, namely φ = h exp(−ϕ).\nTheorem 2.19 ([DX21, Theorem 1.1]). Under the above assumptions,\n                                                                      Z\n                                                              1\n                                                  vol(L, φ) =              θPn [ϕ]I .\n                                                              n!       X",
          "local_file": "source-extracts/2112.04290v2--ideal-volume-and-I-envelope-formula.txt",
          "sha256": "41ba4ee042f3c601f5b6eaea447cff642367df7c15edfc423958cbc3f3ec9e1c",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "partial-body-construction-and-proof",
          "first_line": 988,
          "last_line": 1185,
          "first_textflow_page": 18,
          "last_textflow_page": 21,
          "literal": "                                                   ϕ and max{ψ j , ψ} −→\n                                                                       S\n                                                                         ψ by [DDNL21b, Proposi-\ntion 3.5], each term tends to 0 by Theorem 4.2.                                              \u0003\n     Finally, we prove the continuity of P [•]I .\nTheorem 4.6. The map PSH(X, θ)>0 → PSH(X, θ)>0 given by ϕ 7→ P [ϕ]I is continuous with\nrespect to the dS -pseudometric.\n                                                                                                                   R   n\n     Here PSH(X, θ)>0 denotes the subset of PSH(X, θ) consisting of ϕ with                                          X θϕ > 0.\n                                                      d\nProof. Let ϕi , ϕ ∈ PSH(X, θ)>0 , ϕi −→\n                                      S\n                                        ϕ. We want to show that\n                                                                        S  d\n(4.4)                                                         P [ϕi ]I −→ P [ϕ]I .\nWe may assume that the ϕi ’s and ϕ are all model potentials by [DDNL21b, Theorem 3.3]. By\n[DDNL21b, Theorem 5.6], we may assume that ϕi is either increasing or decreasing. These cases\nfollow from [DX22, Lemma 2.21] and [DDNL21b, Proposition 4.8, Lemma 4.1].                  \u0003\n\n                                                  5. Partial Okounkov bodies\n  Let X be an irreducible smooth complex projective variety of dimension n and L be a big line\nbundle on X. Take a singular psh metric φ on L. We assume that vol(L, φ) > 0. Let h be a smooth\nHermitian metric on L. Let θ = c1 (L, h). Then we can identify φ with a function ϕ ∈ PSH(X, θ).\nWe will use interchangeably the notations (θ, ϕ) and (L, φ).\n  For each k ≥ 0,\n                                                                                                     ∞\n                                                                                                     M\n                                   Wk (θ, ϕ) := H0 (X, Lk ⊗ I(kϕ)),                 W (θ, ϕ) :=            Wk (θ, ϕ).\n                                                                                                     k=0\nWe omit (θ, ϕ) from our notations when there is no risk of confusion. Observe that Wk (θ, ϕ) 6= 0\nwhen k is large enough, as follows from Theorem 2.19.\n  Fix a rank n valuation ν : C(X)× → Zn . We will write\n                                                          n                                   o\n                                         Γν,k (θ, ϕ) = k−1 ν(s) : s ∈ Wk (θ, ϕ)× ,                       k≥1\n                                                          \b\n                                           Γν (θ, ϕ) = (ν(s), k) : k ∈ N, s ∈ Wk (θ, ϕ)× .\n  In [LM09], Lazarsfeld–Mustat, ă only considered the case where ν is induced by an admissible\nﬂag, but thanks to Remark 2.8, their results can be easily extended to the current setup. We will\nuse these results without further comments.\n5.1. Construction of partial Okounkov bodies. Our goal in this section is to show that\nΓν (θ, ϕ) ∈ S ′ (∆ν (L))>0 , namely it is an almost semigroup. Then we shall deﬁne\n(5.1)                                                  ∆ν (θ, ϕ) := ∆ (Γν (θ, ϕ))\nusing the theory of Okounkov bodies of almost semigroups developed in Section 3.3. Moreover, we\nhave\n                                                    Z\n                                                  1\n(5.2)                             vol ∆ν (θ, ϕ) =     θn      .\n                                                  n! X P [ϕ]I\n\f                                          PARTIAL OKOUNKOV BODIES                                                     19\n\n5.1.1. The case of analytic singularities. Assume that ϕ has analytic singularities and θϕ is a Kähler\ncurrent.\n   For any rational ǫ ≥ 0, we deﬁne\n                                          n                                                                   o\n(5.3)              Wkǫ = Wkǫ (θ, ϕ) := s ∈ H0 (X, Lk ) : |s|2hk e−k(1−ǫ)ϕ is bounded .\n              L∞\nThen W ǫ :=          ǫ\n                k=0 Wk has the property that\n                                      n                                             o\n(5.4)                   Γν (W ǫ ) := (ν(s), k) : k ∈ N, s ∈ Wkǫ,× ∈ S ′ (∆ν (L)).\nTo see this, we may assume that ϕ has analytic singularities along a Q-divisor E, then (5.4) follows\nfrom the fact that L − (1 − ǫ)E is big proved in [Xia23b, Lemma 2.4], c.f. [LM09, Lemma 2.2].\n   For any ǫ ∈ Q>0 , we have that\n(5.5)                                                  Wk0 ⊆ Wk ⊆ Wkǫ\nfor k large enough depending on ǫ. The ﬁrst inclusion is of course trivial. The second inclusion is\nwidely known among experts. A detailed proof can be found in [DX21, Remark 2.9].\n   Let π : Y → X be a resolution such that π ∗ ϕ has analytic singularities along a normal crossing\nQ-divisor E. Then we have a natural identiﬁcation for suﬃciently divisible k,\n                             Wǫ ∼= H0 (Y, π ∗ Lk ⊗ OY (−(1 − ǫ)kE)).\n                                  k\n\nOn the other hand,\n                           Wk0 ∼\n                               = H0 (Y, π ∗ Lk ⊗ OY (−kE)) ⊆ H0 (Y, π ∗ Lk ).\nWe compute the volumes,\n                                                   Z                                              Z\n                                              1                                              1\n(5.6)                   vol Γν (W ǫ ) =                     n\n                                                           θ(1−ǫ)ϕ ,       vol Γν (W 0 ) =            θϕn .\n                                              n!   X                                         n!   X\n\nIt follows that Γν (W ǫ ) → Γν (W 0 ) and Γν (θ, ϕ) is equivalent to Γν (W 0 ). In particular, Γν (θ, ϕ) ∈\nS ′ (∆ν (L))>0 , (5.1) makes sense and (5.2) holds.\nRemark 5.1. It follows from the proof that if W 0 (θ, ϕ) is deﬁned as in (5.3) and (5.4):\n                                          n                                                           o\n                        Wk0 (θ, ϕ) := s ∈ H0 (X, Lk ) : |s|2hk e−kϕ is bounded ,\nthen\n(5.7)                                 ∆(Γν (W 0 (θ, ϕ))) = ∆ν (θ, ϕ).\nIf we assume furthermore that π ∗ ϕ has analytic singularity along some normal crossing Q-divisor\nE on Y , then ∆ν (θ, ϕ) is just the translation of ∆ν (π ∗ L − E) by ν(E).\n5.1.2. The case of Kähler currents. Now assume that θϕ is Kähler current. Let ϕj ∈ PSH(X, θ) be\n                                                                       d\na quasi-equisingular approximation of ϕ. Then ϕj −→\n                                                  S\n                                                    P [ϕ]I by [DX21, Proposition 3.3].\n  In this case, we claim that\n(5.8)                                          Γν (θ, ϕj ) → Γν (θ, ϕ).\nIn fact, by Theorem 2.19, we have\n                                                       \u0010                                                          \u0011\n        d(Γν (θ, ϕj ), Γν (θ, ϕ)) = lim k−n h0 (X, Lk ⊗ I(kϕj )) − h0 (X, Lk ⊗ I(kϕ))\n                                  k→∞\n                                = lim k−n h0 (X, Lk ⊗ I(kϕj )) − lim k−n h0 (X, Lk ⊗ I(kϕ))\n                                  k→∞                                                   k→∞\n                                      Z                        Z\n                              1            1\n                            =       θ nj −     θn      .\n                              n! X ϕ       n! X P [ϕ]I\nLetting j → ∞, we conclude (5.8) by Theorem 4.2.\n\f20                                              MINGCHEN XIA\n\n\n     Thus, Γν (θ, ϕ) ∈ S ′ (∆ν (L))>0 and (5.1) makes sense. By Theorem 3.14, we ﬁnd that\n                                                            ∞\n                                                            \\\n                                           ∆ν (θ, ϕ) =           ∆ν (θ, ϕj ).\n                                                         j=0\n\nIn particular, (5.2) holds.\n                                                                                                   R\n5.1.3. General case. Now we consider general ϕ with the assumption that X θPn [ϕ]I > 0. We may\nreplace ϕ with P [ϕ]I and then assume that the non-pluripolar mass of ϕ is positive. Take a potential\nψ ∈ PSH(X, θ) such that ψ ≤ ϕ and θψ is a Kähler current. The existence of ψ is proved in [DX21,\nProposition 3.6]. For each ǫ ∈ Q ∩ (0, 1], let ϕǫ = (1 − ǫ)ϕ + ǫψ. Then we have W (θ, ϕǫ ) ⊆ W (θ, ϕ).\nBy (5.2),\n                                                        Z\n                                                      1\n                                   vol ∆ν (θ, ϕǫ ) =         θn    .\n                                                     n! X P [ϕǫ ]I\nWe claim that\n                                        Γν (θ, ϕǫ ) → Γν (θ, ϕ).\nIn fact, this follows from the simple computation:\n                                               \u0010                                                       \u0011\n          d (Γν (θ, ϕǫ ), Γν (θ, ϕ)) = lim k−n h0 (X, Lk ⊗ I(kϕ)) − h0 (X, Lk ⊗ I(kϕǫ ))\n                                  k→∞\n                                = lim k−n h0 (X, Lk ⊗ I(kϕ)) − lim k−n h0 (X, Lk ⊗ I(kϕǫ ))\n                                  k→∞                                           k→∞\n                                       Z            Z\n                                  1            1\n                                =        θϕn −               θPn [ϕǫ ]I .\n                                  n!   X       n!       X\nBy [DX21, Proposition 2.7], as ǫ decreases to 0, P [ϕǫ ]I increases to P [ϕ]I = ϕ a.e., which implies the\ndS -convergence by [DDNL21b, Lemma 4.1]. Therefore, the right-hand side of the above equation\nconverges to 0 by Theorem 4.2. Our claim is proved. It follows that Γν (θ, ϕ) ∈ S ′ (∆ν (L))>0 and\n(5.1) makes sense. By Theorem 3.14,\n                                                            [\n                                           ∆ν (θ, ϕ) =           ∆ν (θ, ϕǫ ).\n                                                         ǫ>0\n\nIt remains to verify (5.2):\n                                                         Z                      Z\n                                           1                      1\n                           vol ∆ν (θ, ϕ) =     lim   θPn [ϕǫ ]I =                     θPn [ϕ]I .\n                                           n! ǫ→0+ X              n!             X\n                                                    R\nDefinition 5.2. Assume that ϕ ∈ PSH(X, θ), X θPn [ϕ]I > 0. We call ∆ν (θ, ϕ) the partial Okounkov\nbody of (L, φ) or of (θ, ϕ) with respect to ν. When ν is induced by an admissible ﬂag (Y• ) on X\n(see Deﬁnition 2.7), we also say that ∆ν (θ, ϕ) the partial Okounkov body of (L, φ) or of (θ, ϕ) with\nrespect to (Y• ). In this case, we also write ∆Y• instead of ∆ν .\n  We use interchangeably the notations ∆ν (θ, ϕ) and ∆ν (L, φ). When there is no risk of confusion,\nwe write ∆ instead of ∆ν or ∆Y• .\nRemark 5.3. We have assumed X to be smooth only for simplicity. All of our constructions work\nequally well when X is normal or merely unibranch, based on the pluripotential theory in these\nsettings developed in [Xia23a].\nRemark 5.4. In the transcendental setting, a theory of Okounkov bodies is recently established in\n[DRWN+23] based on the work of [Den17]. The proof of the volume identity of transcendental\nOkounkov bodies relies on the technique of partial Okounkov bodies developed in this paper. The\ntranscendental analogue of the partial Okounkov bodies is constructed in a forthcoming joint paper\nwith T.Darvas.\n\f                                        PARTIAL OKOUNKOV BODIES                                         21\n\n5.2. Basic properties of partial Okounkov bodies. We ﬁrst show that ∆(θ, ϕ) does not depend\non the explicit choices of L, h and ϕ, it just depends on ddc φ.\nLemma 5.5. Let L′ be another big line bundle on X. Let h′ be a smooth Hermitian metric on L′\nwith c1 (L, h) = c1 (L′ , h′ ). Then ∆(θ, ϕ) defined with respect to (L, h) is the same as the one defined\nwith respect to (L′ , h′ ).\nProof. From our construction, we may assume that θϕ is a Kähler current and ϕ has analytic\nsingularities. After taking a birational resolution, it suﬃces to deal with the case where ϕ has\nanalytic singularities along normal crossing Q-divisors E. By rescaling, we may also assume that\nE is a divisor. By Remark 5.1, we further reduce to the case without the singular potential φ.\n   In this case, the assertion is proved in [LM09, Proposition 4.1].                           \u0003\nLemma 5.6. Let h′ be another smooth Hermitian metric on L. Set θ ′ = c1 (L, h′ ). Write ddc f =\nθ − θ ′ . Let ϕ′ = ϕ + f ∈ PSH(X, θ ′ ). Then\n(5.9)                                        ∆(θ, ϕ) = ∆(θ ′ , ϕ′ ).\nProof. This is obvious as W (θ, ϕ) = W (θ ′ , ϕ′ ).                                                     \u0003\nCorollary 5.7. The partial Okounkov body ∆(L, φ) depends only on ddc φ, not on the explicit\nchoices of L, φ, h.\n                                                                                          R     n > 0, we\n  Thanks to this result, given a closed positive (1, 1)-current T ∈ c1 (L) on X with       XT\ncan deﬁne ∆(T ) as ∆(θ, ϕ) if T = θ + ddc ϕ for some ϕ ∈ PSH(X, θ).\nProof. This is a direct consequence of Lemma 5.5 and Lemma 5.6.                                         \u0003\n                                                                                               R   n\n  Let PSH(X, θ)>0 denote the subset of PSH(X, θ) consisting of potentials ϕ such that           X θϕ > 0.\n\nProposition 5.8. Let ϕ, ψ ∈ PSH(X, θ)>0 . Assume that ϕ \u0016I ψ, then\n(5.10)                                        ∆(θ, ϕ) ⊆ ∆(θ, ψ).\nIn particular, as by definition, ∆(θ, Vθ ) = ∆(L), we have\n                                                 ∆(θ, ϕ) ⊆ ∆(L).\nProof. This follows from Corollary 3.15.                                                                \u0003",
          "local_file": "source-extracts/2112.04290v2--partial-body-construction-and-proof.txt",
          "sha256": "8fbf581b8474d3547924037ee93268e09cecacda4051d4aa307e543bd1014b99",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "valuative-singularity-recovery-and-proof",
          "first_line": 1514,
          "last_line": 1562,
          "first_textflow_page": 28,
          "last_textflow_page": 29,
          "literal": "Theorem 5.23. Let E be a prime divisor on X. Let (Y• ) be an admissible flag with E = Y1 . Then\n(5.17)                                       ν(ϕ, E) =       min x1 .\n                                                           x∈∆(θ,ϕ)\n\n  Here x1 denotes the ﬁrst component of x. The generic Lelong number ν(ϕ, E) means the mini-\nmum of ν(ϕ, x) for various x ∈ E.\nProof. We ﬁrst reduce to the case where θϕ is a Kähler current. Let ψ ≤ ϕ, θψ is a Kähler current.\nThen by (5.17) applied to ϕǫ := (1 − ǫ)ϕ + ǫψ, we have\n                                             ν(ϕǫ , E) =     min        x1 .\n                                                           x∈∆(θ,ϕǫ )\n\nLet ǫ → 0+ using Theorem 5.9, we conclude (5.17).\n   Similarly, taking a quasi-equisingular approximation of ϕ and applying Lemma 5.22, we easily\nreduce to the case where ϕ also has analytic singularities. Replacing X by a birational model, we\nmay assume that ϕ has analytic singularities along a simple normal crossing Q-divisor F . Perturbing\nL by an ample Q-line bundle by Proposition 5.16, we may assume that θϕ is a Kähler current.\nFinally, by rescaling, we may assume that F is a divisor and L is a line bundle and L − F is ample\nby [Xia23b, Lemma 2.4]. In fact, since θϕ is a Kähler current, the same holds for θϕ − ǫω, where\nω is a Hodge form lying in c1 (A) for some ample line bundle A on X and ǫ > 0 is a small enough\nrational number. By [Xia23b, Lemma 2.4], we deduce that L − F − ǫA is nef and big and hence\nL − F is ample.\n   By Theorem 5.17, we know that\n                                        min x1 = lim             min           x1 .\n                                       x∈∆(θ,ϕ)        k→∞ x∈∆k (θ,ϕ)\n\nBy deﬁnition,\n                                 min        x1 = k−1 ordE H0 (X, Lk ⊗ I(kϕ)).\n                               x∈∆k (θ,ϕ)\nIt remains to show that\n(5.18)                   lim k−1 ordE H0 (X, Lk ⊗ I(kϕ)) = lim k−1 ordE I(kϕ).\n                         k→∞                                          k→∞\n\nThe ≥ direction is trivial, we prove the converse. Observe that\n                 H0 (X, Lk ⊗ I(kϕ)) = H0 (X, Lk ⊗ OX (−kF )),                     I(kϕ) = O(−kF ).\nAs L − F is ample, for large enough k, we have\n                               ordE H0 (X, Lk ⊗ OX (−kF )) = ordE (kF ).\nThus, (5.18) is clear.                                                                               \u0003\nCorollary 5.24. Let ϕ, ψ ∈ PSH(X, θ)>0 . If\n                                        ∆(π ∗ θ, π ∗ ϕ) ⊆ ∆(π ∗ θ, π ∗ ψ)\nfor all birational models π : Y → X and all admissible flags on Y , then ϕ \u0016I ψ.\n\f                                    PARTIAL OKOUNKOV BODIES                                         29\n\nProof. In view of Theorem 5.23, the assumption implies the following: for any prime divisor E\nover X, we have ν(ϕ, E) ≥ ν(ψ, E). This implies ϕ \u0016I ψ: take a birational model π : Y → X\nand y ∈ Y , we need to show that ν(π ∗ ϕ, y) ≥ ν(π ∗ ψ, y). Let E be the exceptional divisor of the\nblow-up of Y at {y}. As explained in [Bou02a, Corollaire 1.1.8], we have ν(π ∗ ϕ, y) = ν(ϕ, E) and\nν(π ∗ ψ, y) = ν(ψ, E). Our assertion follows.                                                    \u0003\n   In particular, Theorem B is proved. This corollary is similar to [Jow10]. It suggests that ∆(θ, ϕ)\nis a universal invariant of the singularities of ϕ.",
          "local_file": "source-extracts/2112.04290v2--valuative-singularity-recovery-and-proof.txt",
          "sha256": "fb4e6919a03c290f96ac8a7c66460dd26c6970dd3c30597abcd16e6494382b09",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "section-5.6-and-conjecture-5.29",
          "first_line": 1623,
          "last_line": 1637,
          "first_textflow_page": 30,
          "last_textflow_page": 30,
          "literal": "5.6. Limit partial Okounkov bodies. Let ϕ ∈ PSH(X, θ), not necessarily of positive volume.\nTake an ample eﬀective divisor H on X and a Kähler form ω ∈ c1 (H). Then we just set\n                                                        \\\n                                    ∆(θ, ϕ) :=              ∆(θ + ǫω, ϕ).\n                                                    ǫ∈Q>0\n\nClearly, this deﬁnition does not depend on the choice of H and ω. As in [CHPW18b], we can-\nnot expect ∆(θ, ϕ) to be continuous along decreasing sequences of ϕ. Note that Theorem 5.23,\nCorollary 5.24 and Proposition 5.8 extend to this setup without changes.\n  We propose the following conjecture:\nConjecture 5.29. Under the above assumptions,\n                                        dim ∆(θ, ϕ) = nd(θ, ϕ).\n  For the deﬁnition of the analytic numerical dimension nd(θ, ϕ), we refer to [Cao14, Deﬁnition 4].\n  We expect that this conjecture follows from the arguments in [CHPW18b] together with the\nnumerical criterion of [Cao14].",
          "local_file": "source-extracts/2112.04290v2--section-5.6-and-conjecture-5.29.txt",
          "sha256": "111ec323bf00dce58efafb4048d156ace3c4eac9336b198483085296379476f2",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        }
      ],
      "application_checks": [
        "This source constructs section/multiplier-ideal bodies on projective varieties with line-bundle data. It is audited, not applied to the nonprojective product theorem.",
        "The invariant factors through all multiplier ideals I(k*phi); Proposition 5.8 and section 5.6 preserve this I-invariance.",
        "Theorem 2.19 uses the mass of P[phi]_I, not a general equality with the mass of phi.",
        "At zero actual mass, Proposition 2.10 does not identify C[phi] with P[phi]. They are kept separate.",
        "Section 5.6 defines the limiting body; Conjecture 5.29 states, rather than proves, its dimension equality.",
        "No extension of the conjecture to every flag or to transcendental classes is assumed."
      ]
    },
    {
      "id": "Cao",
      "title": "Numerical dimension and a Kawamata--Viehweg--Nadel-type vanishing theorem on compact Kahler manifolds",
      "exact_arxiv_version": "1210.5692v1",
      "printed_date": "21 Oct 2012",
      "public_source": "https://arxiv.org/pdf/1210.5692v1",
      "pdf_location": "/workspace/research/shared-sources/P15.3-arxiv-1210.5692v1-20261004.pdf",
      "pdf_sha256": "17717664b0ae2b154e76e2ecb68c9f63f09dc74be6f25bac7f04b7ee0103b0d6",
      "supplied_extract_location": "/workspace/research/shared-sources/P15.3-arxiv-1210.5692v1-20261004.txt",
      "extract_sha256": "1bae7bf39d69c41451507e29d908977cb4599bf0b10216eb8b8295c7ba769fce",
      "byte_identical_local_extract": "source-extracts/1210.5692v1-full.txt",
      "source_line_count": 1931,
      "line_number_convention": "UTF-8 text.split('\\n'); one-based indexing; trailing empty line counted; form feeds remain inside lines",
      "passages": [
        {
          "id": "normalization-and-metric-convention",
          "first_line": 100,
          "last_line": 128,
          "first_textflow_page": 3,
          "last_textflow_page": 3,
          "literal": "                                     ψ ≤ϕ+C\nfor some constant C. We denote it ϕ 4 ψ.\n   We now recall the analytic definition of multiplier ideal sheaves. Let I(ϕ)\nbe the multiplier ideal sheaves associated to the quasi-psh function ϕ, i.e.\n                                      Z\n                   I(ϕ)x = {f ∈ OX |      |f |2 e−2ϕ < +∞}\n                                            Ux\nwhere Ux is some open neighborhood of x in X (cf. [Dem] for a more\ndetailed introduction to the concept of multiplier ideal sheaf). When ϕ\ndoes not possess analytic singularities, we need to introduce the “upper\nsemicontinuous regularization” of the multiplier ideal sheaf, namely the ideal\nsheaf\n                        I+ (ϕ) = lim I((1 + ǫ)ϕ).\n                                       ǫ→0+\nBy the Notherian property of coherent ideal sheaves, there exists an ǫ > 0\nsuch that\n                I+ (ϕ) = I((1 + ǫ′ )ϕ)     for any 0 < ǫ′ < ǫ.\nWhen ϕ has analytic singularities, it is easy to see that I+ (ϕ) = I(ϕ).\nConjecturally we have the equality for all psh functions. 2\nImportant Convention: When we talk about a line bundle L on X, we\nalways first implicitly fix a smooth metric h0 on L. Given a singular metric\nϕ on L or sometimes ϕ for simplicity, we just means that the new metric on\nL is given by h0 e−ϕ . Recall that the curvature of the metric ϕ for L is\n                          i           i\n                            Θϕ (L) =    Θh (L) + ddc ϕ.\n                        2π           2π 0\n                                                                 i\nThe pair (L, ϕ) is said to be a pseudo-effective line bundle if 2π Θϕ (L) ≥ 0\nas a current.",
          "local_file": "source-extracts/1210.5692v1--normalization-and-metric-convention.txt",
          "sha256": "2ba5ce00c68a41b03ed0d77f107cad134292976ced9efc1b0bdd315bf2976368",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "definitions-2-3-4-and-independence-proof",
          "first_line": 162,
          "last_line": 289,
          "first_textflow_page": 4,
          "last_textflow_page": 6,
          "literal": "  Let X be a compact Kähler manifold and let T be a closed positive (1, 1)-\ncurrent. It is well known that T can be written as\n                                      T = θ + ddc ϕ,\nwhere θ is a smooth (1, 1)-closed form representing [T ] ∈ H 1,1 (X, R) and ϕ is\na quasi-psh function. Demailly’s famous regularization theorem states that\nϕ can be approximated by a sequence of quasi-psh functions with analytic\nsingularities. We say that it is an analytic approximation of ϕ. Among all\nthese analytic approximations, we want to deal with those which keep the\ninformation concerning the singularities of T . More precisely, we introduce\nthe following definition.\nDefinition 2. Let θ + ddc ϕ be a positive current, where θ is a smooth form\nand ϕ is a quasi-psh function on a compact Kähler manifold (X, ω). We\nsay that {ϕk }∞k=1 is a quasi-equisingular approximation of ϕ for the current\nθ + ddc ϕ if it satisfies the following conditions:\n  (i) {ϕk }∞                          1\n            k=1 converge to ϕ in L topology and\n                                  θ + ddc ϕk ≥ −τk · ω\nfor some constants τk → 0 as k → +∞.\n   (ii) all ϕk have analytic singularities and ϕk 4 ϕk+1 for any k.\n   (iii) For any δ > 0 and m ∈ N, there exists k0 (δ, m) ∈ N such that\n            I(m(1 + δ)ϕk ) ⊂ I(mϕ)               for every k ≥ k0 (δ, m)\nRemark. By condition (i), such type of approximation depends not only on\nϕ but also on the current θ + ddc ϕ.\n\f            A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                      5\n\n   The existence of such quasi-equisingular approximations was proved in\nTheorem 2.2.1 of [DPS 01] by a Bergman kernel method. The choice of such\napproximations corresponds in some sense to the most singular approxima-\ntions asymptotically. The following proposition makes this assertion more\nprecise.\nProposition 2.2. Let θ + ddc ϕ1 , θ + ddc ϕ2 be two positive currents on a\ncompact Kähler manifold X as usual. We assume that the quasi-psh function\nϕ2 is more singular than ϕ1 . Let {ϕi,1 }∞i=1 be an analytic approximation to\nϕ1 and let {ϕi,2 }∞\n                  i=1 be a  quasi-equisingular approximation to ϕ2 . For any\nclosed smooth (n − 1, n − 1)-semi-positive form u, we have\n                    Z                         Z\n                          c\n(2.1)          lim     (dd ϕi,1 )ac ∧ u ≥ lim    (ddc ϕi,2 )ac ∧ u\n               i→∞ X                       i→∞ X\n\nwhere (ddc ϕi,1 )ac denotes the absolutely continuous part of the current ddc ϕi,1 .\nProof. It is enough to show that\n                 Z                         Z\n                       c\n(2.2)               (dd ϕs,1 )ac ∧ u ≥ lim   (ddc ϕi,2 )ac ∧ u\n                   X                    i→∞ X\n\nfor any s ∈ N fixed. Since {ϕi,2 }∞\n                                  i=1 is a quasi-equisingular approximation\nto ϕ2 , for any δ > 0 and m ∈ N, there exists a k0 (δ, m) ∈ N such that\n(2.3)       I(m(1 + δ)ϕk,2 ) ⊂ I(mϕ2 )        for every k ≥ k0 (δ, m).\nSince ϕ1 4 ϕ2 and ϕs,1 4 ϕ1 , (2.3) implies that\n(2.4)                     I(m(1 + δ)ϕk,2 ) ⊂ I(mϕs,1 )\nfor any s ∈ N fixed and k ≥ k0 (δ, m).\n                                                 b → X be a log resolution\n   Using (2.4), we begin to prove (2.2). Let π : X\nof ϕs,1 . We can thus assume that\n                            ddc ϕs,1 ◦ π = [F ] + C ∞ ,\nwhere F is a R-normal crossing divisor. Using Lemma 2.1, (2.4) implies that\n(2.5)       I(m(1 + δ)ϕk,2 ◦ π) ⊗ O(−J) ⊂ I(mϕs,1 ◦ π) = O(−⌊mF ⌋)\nfor k ≥ k0 (δ, m), where J is the Jacobian of the blow up π. Since F is a\nnormal crossing divisor, (2.5) implies that m(1 + δ)ddc ϕk,2 ◦ π + [J] − ⌊mF ⌋\nis a positive current. Then\n      Z                                        Z\n         (ddc m(1 + δ) · ϕk,2 ◦ π)ac ∧ u ≤ C +   (ddc m · ϕs,1 ◦ π)ac ∧ u\n        b\n        X                                          b\n                                                   X\n\nfor k ≥ k0 (δ, m), where the constant C is independent of m and k. Therefore,\nif m → +∞, we get\n          Z                                         Z\n                                        1\n(2.6)          (ddc ϕk,2 ◦ π)ac ∧ u ≤ O( ) + C1 δ +     (ddc ϕs,1 ◦ π)ac ∧ u\n            Xb                          m             b\n                                                      X\n\f6                                    JUNYAN CAO\n\nfor k ≥ k0 (δ, m) and a constant C1 independent of m and k. Then\n            Z                                     Z\n                                      1\n                (ddc ϕk,2 )ac ∧ u ≤ O( ) + C1 δ +    (ddc ϕs,1 )ac ∧ u\n              X                       m            X\n\nfor k ≥ k0 (δ, m). Letting m → +∞ and δ → 0, we get\n                      Z                     Z\n                            c\n                  lim    (dd ϕk,2 )ac ∧ u ≤   (ddc ϕs,1 )ac ∧ u.\n                 k→∞ X                              X\n\nThus (2.2) is proved.\n                                                                               \u0003\nRemark. Assume that {ϕi,1 }, {ϕi,2 } are two quasi-equisingular approxima-\ntions to the same ϕ. Proposition 2.2 implies in particular that\n                   Z                         Z\n               lim   (ddc ϕi,1 )ac ∧ u = lim   (ddc ϕi,2 )ac ∧ u.\n               i→∞ X                           i→∞ X\n\n  Thanks to Proposition 2.2 and the above remark, we can define a related\ncohomological product of closed positive (1, 1)-currents.\nDefinition 3. Let T1 , · · · , Tk be closed positive (1, 1)-currents on a compact\nKähler manifold. We write them by the potential forms Ti = θi + ddc ϕi as\nusual. Let {ϕi,j }∞\n                  j=1 be a quasi-equisingular approximation to ϕi . Then we\ncan define a product\n                                  hT1 , T2 , · · · , Tk i\n                  k,k\nas an element in H≥0  (X) such that for all u ∈ H n−k,n−k (X),\n                                hT1 , T2 , · · · , Tk i ∧ u\n                    Z\n            = lim       (θ1 + ddc ϕ1,j )ac ∧ · · · ∧ (θk + ddc ϕk,j )ac ∧ u\n              j→∞ X\nwhere ∧ is the usual wedge product in cohomology.\nRemark. Thanks to Proposition 2.2 and its remark, the product defined\nhere does not depend on the choice of quasi-equisingular approximation.\nMoreover the product here is smaller than the product defined by any other\nanalytic approximations.\n\n                           3. Numerical dimension\n   Using the product defined in the last section, we can give our definition\nof the numerical dimension.\nDefinition 4. Let (L, ϕ) be a pseudo-effective line bundle on a compact\n                                i\nKähler manifold X such that 2π   Θϕ (L) ≥ 0. We define the numerical di-\nmension nd(L, ϕ) as the largest v ∈ N, such that h(iΘϕ )v i 6= 0, where the\ncohomological product h(iΘϕ )v i is the v-fold product of iΘϕ (L) defined in\nDefinition 3.",
          "local_file": "source-extracts/1210.5692v1--definitions-2-3-4-and-independence-proof.txt",
          "sha256": "0135cddbf0ed5fc31288aefd971415b578bf89ec4ca9fdea143d7259212460c2",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "class-dimension-versus-pair-dimension",
          "first_line": 1165,
          "last_line": 1179,
          "first_textflow_page": 22,
          "last_textflow_page": 22,
          "literal": "ifold. S.Boucksom defined in [Bou] a concept of numerical dimension nd(L)\nof pseudo-effective line bundles without metrics. Let ϕmin be a positive\nmetric of L with minimal singularity. Proposition 4.4 implies in particular\nthat\n                           nd(L) ≥ nd(L, ϕmin ).\nThe example 1.7 in [DPS 94] tells us that we cannot hope the equality\n                              nd(L) = nd(L, ϕmin ).\nIn that example, the line bundle L is nef and nd(L) = 1. But there exists a\nunique positive singular metric h on L with the curvature form\n                                i\n                                  Θh (L) = [C],\n                               2π\nwhere C is a curve on X. Therefore ϕmin = h. Moreover, since h has\nanalytic singularities, we have nd(L, ϕmin ) = 0 by definition. Thus\n                              nd(L) > nd(L, ϕmin ).",
          "local_file": "source-extracts/1210.5692v1--class-dimension-versus-pair-dimension.txt",
          "sha256": "3be26d1f645a5a8662544fe9f1d7bb46eb8c3e2cb44e45ae0367dadfba9e8a5b",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        }
      ],
      "application_checks": [
        "Definition 3 is a cohomological product of general positive currents, computed using absolutely continuous parts of quasi-equisingular analytic approximants.",
        "Definition 4 is worded for a pseudoeffective line bundle and metric; the transcendental example explicitly names its current-product analogue d_Cao instead of claiming a line-bundle application.",
        "For the analytic divisorial current in the theorem, the constant approximation meets every condition of Definition 2, so Definition 3 gives [beta^k].",
        "Equality with actual nonpluripolar products is proved only for this analytic divisorial type using locality and the bounded remainder. No general identification is made.",
        "The cited approximation-independence statement is retained with its actual proof, not replaced with nonpluripolar continuity."
      ]
    },
    {
      "id": "CHPW",
      "title": "Okounkov bodies associated to pseudoeffective divisors",
      "exact_arxiv_version": "1508.03922v5",
      "printed_date": "5 Feb 2018 (arXiv header); September 24, 2018 (internal manuscript Date)",
      "public_source": "https://arxiv.org/pdf/1508.03922v5",
      "pdf_location": "/workspace/research/shared-sources/P15.3-arxiv-1508.03922v5-20261004.pdf",
      "pdf_sha256": "8217255c74b4402b6e6a3167db1a6fd8f539056029d82b13556b82828b191a0c",
      "supplied_extract_location": "/workspace/research/shared-sources/P15.3-arxiv-1508.03922v5-20261004.txt",
      "extract_sha256": "5ff42d0b3c3c0f0aca4af9fccafdfc96f9e60a30e46cb64fcf9a59b45fcf2c14",
      "byte_identical_local_extract": "source-extracts/1508.03922v5-full.txt",
      "source_line_count": 1425,
      "line_number_convention": "UTF-8 text.split('\\n'); one-based indexing; trailing empty line counted; form feeds remain inside lines",
      "passages": [
        {
          "id": "limiting-body-definition",
          "first_line": 80,
          "last_line": 105,
          "first_textflow_page": 2,
          "last_textflow_page": 2,
          "literal": "  Now we define the valuative Okounkov body and the limiting Okounkov body of a divisor.\nDefinition 1.1. Let D be an R-divisor on a smooth projective variety X of dimension n, and\nY• be an admissible flag on X.\n (1) Suppose that D is effective up to R-linear equivalence, that is, |D|R 6= ∅. The valuative\n  Okounkov body ∆val\n                   Y• (D) of D with respect to Y• is defined as\n\n                    ∆val                                                         n\n                     Y• (D) := the closure of the convex hull of νY• (|D|R ) in R≥0 .\n                                         ∗\n If |D|R = ∅, then we put ∆val\n                             Y• (D) := ∅.\n(2) Suppose that D is pseudoeffective. The limiting Okounkov body ∆lim\n                                                                    Y• (D) of D with respect\n to Y• is defined as\n                                                   \\\n                   ∆lim\n                     Y• (D) := lim ∆Y• (D + εA) =     ∆Y• (D + εA) in Rn≥0\n                                      ε→0+\n                                                                   ε>0\n\n    where A is a fixed ample divisor on X. If D is not pseudoeffective, then we put ∆lim\n                                                                                      Y• (D) := ∅.\n    Note that the definition of the limiting Okounkov body ∆lim\n                                                              Y• (D)  is independent of the choice\n    of the ample divisor A.",
          "local_file": "source-extracts/1508.03922v5--limiting-body-definition.txt",
          "sha256": "84983e2ee04eba25f2ad2da943bb3600d313d7524caa66b574a916e12b4f3bce",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "theorem-B-and-flag-hypotheses",
          "first_line": 124,
          "last_line": 185,
          "first_textflow_page": 3,
          "last_textflow_page": 3,
          "literal": "V 6⊆ B− (D), the augmented restricted volume of D along V is defined as\n                               vol+\n                                  X|V (D) := lim volX|V (D + εA)\n                                             ε→0+\n\nwhere A is some fixed ample divisor on X. It is independent of the choice of the ample divisor\nA. For more details, we refer to Subsection 2.3. The Iitaka dimension of D is defined as\n                                 \u001a                                       \u001b\n                                                   h0 (X, OX (⌊mD⌋))\n                  κ(D) := max k ∈ Z≥0 lim sup                         >0\n                                             m→∞           mk\nif h0 (X, OX (⌊mD⌋)) 6= 0 for some m > 0, and κ(D) := −∞ otherwise. Similarly, the numerical\nIitaka dimension of D is defined as\n                                \u001a                                         \u001b\n                                                h0 (X, OX (⌊mD⌋ + A))\n                κν (D) := max k ∈ Z≥0 lim sup                         >0\n                                           m→∞            mk\nfor some fixed ample Cartier divisor A if h0 (X, OX (⌊mD⌋ + A)) 6= 0 for some m > 0, and\nκν (D) := −∞ otherwise. It is also independent of the choice of the ample divisor A. For more\ndetails, see Subsections 2.4 and 2.5.\n   To extract asymptotic invariants of a divisor D with κ(D) ≥ 0 from the valuative Okounkov\nbody ∆valY• (D), we consider an admissible flag Y• that contains a special subvariety Yn−κ(D) =\nU ⊆ X such that the natural restriction map H 0 (X, OX (⌊mD⌋)) → H 0 (U, OU (⌊mD|U ⌋)) is\ninjective for every integer m ≥ 0. We call such U a Nakayama subvariety of D (see Subsection\n2.4). Note that any general subvariety of dimension κ(D) is a Nakayama subvariety of D\n(Proposition 2.13). If D is big, then X itself is the unique Nakayama subvariety of D.\nTheorem A (=Theorem 3.12). Let D be an R-divisor on a smooth projective variety X of\ndimension n such that κ(D) ≥ 0. Fix an admissible flag Y• containing a Nakayama subvariety\nU of D such that Yn = {x} is a general point. Then ∆val         n−κ(D) ×Rκ(D) . Furthermore,\n                                                    Y• (D) ⊆ {0}          ≥0\nwe have\n                                                                 1\n              dim ∆val                              val\n                    Y• (D) = κ(D) and volRκ(D) (∆Y• (D)) =          volX|U (D)\n                                                              κ(D)!\nwhere ∆val\n       Y• (D) is regarded as a convex subset of R\n                                                  κ(D) .\n\n\n   For convenience, we define dim(point) := 0 and volR0 (point) := 1 throughout the paper.\nTheorem A does not hold if D is only effective up to R-linear equivalence (see Remark 3.14).\n   To investigate the asymptotic properties of a pseudoeffective divisor D using the limiting\nOkounkov body ∆lim Y• (D), we consider an admissible flag Y• that contains a special subvariety\nYn−κν (D) = V ⊆ X such that vol+ X|V (D) > 0. We call such V a positive volume subvariety of D\n(see Subsection 2.5). Note that that the intersection of (n − κν (D)) general ample divisors is a\npositive volume subvariety of D (Proposition 2.22). Thus we may take a general admissible flag\nY• constructed by successively intersecting general ample divisors. If D is big, then X itself is\nthe unique positive volume subvariety of D.\nTheorem B (=Corollary 3.22). Let D be a pseudoeffective R-divisor on a smooth projective\nvariety X of dimension n. Fix an admissible flag Y• containing a positive volume subvariety V\nof D. Then ∆lim           n−κν (D) × Rκν (D) . Furthermore, we have\n              Y• (D) ⊆ {0}            ≥0\n                                                                        1\n             dim ∆lim\n                  Y• (D) = κν (D) and       volRκν (D) (∆lim\n                                                         Y• (D)) =           vol+\n                                                                                X|V (D)\n                                                                     κν (D)!\nwhere ∆lim\n       Y• (D) is regarded as a convex subset of R\n                                                  κν (D) .",
          "local_file": "source-extracts/1508.03922v5--theorem-B-and-flag-hypotheses.txt",
          "sha256": "96a6dc12942d127275c0b7460ef06666517b51ededc0eef2cc45fbdd5855c823",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "positive-volume-subvarieties-and-proof",
          "first_line": 532,
          "last_line": 574,
          "first_textflow_page": 10,
          "last_textflow_page": 10,
          "literal": "  Now we define the positive volume subvariety associated to a pseudoeffective divisor.\nDefinition 2.19. Let D be a pseudoeffective divisor on a variety X. A subvariety V ⊆ X\nof dimension κν (D) such that vol+  X|V (D) > 0 and V 6⊆ B− (D) is called a positive volume\nsubvariety of D. (In other words, a positive volume subvariety V ⊆ X is the subvariety at which\nthe maximum in Theorem 2.18 is attained.)\nRemark 2.20. In [CPW, Lemma 4.3], we show that vol+       X|V (D) > 0 implies V 6⊆ B− (D). Thus\nthe condition V 6⊆ B− (D) in the definition of the positive volume subvariety is redundant.\nExample 2.21. Let S be a relatively minimal rational elliptic surface with a reducible singular\nfiber, and E a (−2)-curve in a singular fiber. Then E 6⊆ B− (−KS ) but vol+ S|E (−KS ) = 0. In\nthis example, we see that V 6⊆ B− (D) and dim V = κν (D) does not imply vol+ X|V (D) > 0.\n\n   By definition, if D is a big divisor on X, then V = X is the unique positive volume subvariety\nof D. Theorem 2.18 guarantees the existence of a positive volume subvariety in general. Fur-\nthermore, we can also find a smooth positive volume subvariety by the following. It also shows\nthat a positive volume subvariety is not unique in general.\nProposition 2.22. Let D be a pseudoeffective divisor on a variety X of dimension n. If\nκν (D) < n, then the subvariety V := A1 ∩ · · · ∩ An−κν (D) satisfies vol+     X|V (D) > 0, where\nA1 , · · · , An−κν (D) are general members of sufficiently ample linear systems. In particular, V is\na positive volume subvariety of D.\nProof. By Theorem 2.18, there exists a positive volume subvariety W of D. In particular, we\nhave vol+X|W (D) > 0. We can take a sequence {Hi }i∈Z≥0 of ample divisors on X such that each\nD + Hi is a Q-divisor and Hi → 0 as i → ∞. For a large and sufficiently divisible integer\n                                     1 , · · · , E κν (D) ∈ |k(D + H )|. Since A , · · · , A\nk, choose κν (D) general divisors Ek,i            k,i               i           1           n−κν (D) are\nsufficiently ample divisors, we have\n              1               κ (D)                           1                      κ (D)\n       #(V ∩ Ek,i ∩ · · · ∩ Ek,iν     \\ SB(D + Hi )) ≥ #(W ∩ Ek,i ∩ · · · ∩ Ek,iν            \\ SB(D + Hi )).\nThus by applying [ELMNP2, Theorem B], we obtain\n                                                           κ (D)\n                                                  1 ∩···∩E ν\n                                            #(V ∩Ek,i     k,i      \\SB(D+Hi ))\n             volX|V (D + Hi ) = lim                     k κν (D)\n                                      k→∞\n                                                           κ (D)\n                                                  1 ∩···∩E ν\n                                            #(W ∩Ek,i     k,i      \\SB(D+Hi ))\n                                    ≥ lim               k κν (D)\n                                                                                 = volX|W (D + Hi ).\n                                      k→∞\n\nThis implies that vol+            +\n                     X|V (D) ≥ volX|W (D) > 0. Since A1 , · · · , An−κν (D) are sufficiently ample,\nwe also have V 6⊆ B− (D).                                                                        \u0003",
          "local_file": "source-extracts/1508.03922v5--positive-volume-subvarieties-and-proof.txt",
          "sha256": "4d16e4d7559357d2e060d8502bd38eeb9d939158abe8d1064c3a5545f094df7b",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "theorems-3.20-3.22-and-proofs-and-flag-warning",
          "first_line": 919,
          "last_line": 1106,
          "first_textflow_page": 16,
          "last_textflow_page": 19,
          "literal": "a positive volume subvariety V of D. To investigate such ∆Y• (D) in detail, we introduce the\nfollowing alternative construction, which also gives the same convex body as ∆lim  Y• (D) after all\n(see Proposition 3.21). This construction is often more convenient to study the asymptotic\ninvariants of pseudoeffective divisors. To begin with, we first consider a pseudoeffective Cartier\nZ-divisor D on a variety X of dimension n. Let V ⊆ X be a v-dimensional irreducible subvariety\nof D. We will mainly concern the case that V is a positive volume subvariety of D. Fix an\nadmissible flag V• on V :\n                               V• : V = V0 ⊇ V1 ⊇ · · · ⊇ Vv = {x}.\n\f                OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                         17\n\nLet A be an ample Cartier Z-divisor on X. For each integer k ≥ 1, consider the restricted\ngraded linear series W•k := W• (kD + A|V ) of kD + A along V given by Wm (kD + A|V ) =\nh0 (X|V, m(kD + A)) for m ≥ 0. We define the restricted limiting Okounkov body of a Cartier\ndivisor D along V with respect to V• as\n                                              1\n                              ∆lim\n                               V• (D) := lim    ∆V• (W•k ) ⊆ Rv≥0 .\n                                          k→∞ k\n\nOne can easily check that ∆lim\n                            V• (D) = limε→0+ ∆V• (D + εA). We can extend this definition for\nany pseudoeffective R-divisor D.\nDefinition 3.19. Let D be a pseudoeffective divisor on a variety X, and V ⊆ X be a v-\ndimensional irreducible subvariety. The restricted limiting Okounkov body ∆lim\n                                                                           V• (D) of D along\nV with respect to V• as\n                            ∆lim\n                              V• (D) := lim ∆V• (D + εA) ⊆ R≥0\n                                                                v\n                                         ε→0+\n\nfor some ample divisor A on X. If D is not pseudoeffective, then we define ∆lim\n                                                                            V• (D) := ∅.\n\n  This definition depends on the choice of V and the admissible flag V• on it, but it is indepen-\ndent of the choice of A. By definition, ∆lim                                  v\n                                         V• (D) is a closed convex subset of R . By the inclusion\nRv = {0}n−v × Rv ֒→ Rn , we often treat ∆lim                        n\n                                             V• (D) as a subset of R .\n  The following is the main property of the restricted limiting Okounkov body ∆lim V• (D).\n\nTheorem 3.20. Let D be a pseudoeffective divisor on a variety X, and V be a v-dimensional\nirreducible subvariety of X. Fix an admissible flag V• on V . Suppose that V 6⊆ B− (D) and\nvol+\n   X|V (D) > 0. Then we have\n\n                                                                 1\n                   dim ∆lim\n                        V• (D) = v and      volRv (∆lim\n                                                    V• (D)) =       vol+\n                                                                       X|V (D).\n                                                                 v!\nProof. We first consider the case where D is a Z-divisor. Let A be an ample Z-divisor on\nX. Since V 6⊆ B− (D) by definition, it follows that V 6⊆ B+ (kD + A) for any k ≥ 1. Let\nW•k := W• (kD + A|V ) be the restricted graded series of kD + A along V for k ≥ 1. Then W•k\nsatisfies Condition (C) by [LM, Lemma 2.16]. It follows from Theorem 3.4 that for each k ≥ 1,\nwe have\n                                                                1\n             dim ∆V• (W•k ) = dim V = v and volRv (∆V• (W•k )) = volX|V (kD + A).\n                                                                v!\nThe first equality implies dim ∆lim\n                                V• (D) = v, and the second equality yields the following compu-\ntation:                                           \u0012                 \u0013\n                         volRv (∆lim\n                                 V• (D)) = volRv       lim 1 ∆V• (W•k )\n                                                      k→∞ k\n                                           = lim k1v volRv (∆V• (W•k ))\n                                             k→∞                        \u0001\n                                           = lim v!1 volX|V D + k1 A\n                                             k→∞\n                                           = v!1 vol+\n                                                    X|V (D).\nThus we have shown the assertion for Z-divisors. When D is a Q-divisor, there is a sufficiently\ndivisible integer m > 0 such that mD is a Z-divisor. It is easy to check that ∆lim      V• (D) =\n 1 lim\n  ∆\nm V•   (mD).   Thus the  assertions for Q-divisors follow from the  Z-divisor case.\n  Now, we assume that D is an R-divisor. Then there exists a sequence of ample divisors Ai on\nX such that D + Ai are Q-divisor and limi→∞ Ai = 0. Note that V 6⊆ B+ (D + Ai ). Thus V 6⊆\nB− (D + Ai ) and vol+                                              lim              lim\n                    X|V (D + Ai ) = volX|V (D + Ai ) > 0. Since ∆V• (D) = limi→∞ ∆V• (D + Ai ),\nthe assertion for R-divisors follow from the Q-divisor case.                                   \u0003\n\f18           SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON\n\nProposition 3.21. Let D be a pseudoeffective divisor on a variety X of dimension n, and fix\nan admissible flag Y• containing a positive volume subvariety V = Yn−κν (D) of D. Consider the\n(n − κν (D))-th partial flag V• := Yn−κν (D)• . Then\n                                        ∆lim       lim\n                                         Y• (D) = ∆V• (D).\n\nIn particular, ∆lim\n                Y• (D) depends on the (n − κν (D))-th partial flag V• .\n\nProof. We will denote κν := κν (D). If κν = n, then there is nothing to prove. Therefore, we\nassume that 0 ≤ κν < n. Fix an ample divisor A on X. By definition, the positive volume\nsubvariety Yn−κν = V is not contained in B− (D). Since Yi ⊇ Yn−κν for 0 ≤ i ≤ n − κν , we\nhave Yi 6⊆ B+ (D + εA) for any ε > 0. Thus Theorem 3.6 implies that if 0 ≤ i ≤ n − κν , then\n∆Y• (D + εA) ∩ ({0}i × Rn−i ) = ∆Yi• (D + εA). By taking the limit ε → 0, for 0 ≤ i ≤ n − κν ,\nwe obtain\n(*)                  ∆lim          i\n                      Y• (D) ∩ ({0} × R\n                                        n−i\n                                            ) = lim ∆Yi• (D + εA) =: ∆lim\n                                                                      Yi• (D).\n                                                ε→0+\n\nSince Yn−κν = V , it is enough to check ∆lim\n                                         Y• (D) ⊆ {0}\n                                                     n−κν × Rκν to prove ∆lim (D) = ∆lim (D).\n                                                                          Y•         V•\nSuppose that this does not hold, that is,\n                                  ∆lim\n                                   Y• (D) 6⊆ {0}\n                                                n−κν\n                                                     × Rκν ⊆ Rn .\nWe will derive a contradiction to [Le1, Theorem 1.1 (2)], which says that κν is the maximum\nof integers k ≥ 0 such that there exists a constant C > 0 with volX (D + εA) ≥ Cεn−k for all\nε > 0. By Theorem 3.20, l := dim ∆lim                   lim\n                                    Y• (D) > κν = dim ∆V• (D) and we have\n\n                             ∆lim       i1  i2\n                              Y• (D) ⊆ R × R × · · · × R\n                                                         in−κν\n                                                               × Rκν\n                     Pn−κν\nwhere ij = 0 or 1,     j=1   ij = l − κν and R0 := {0}. For simplicity, we may just assume\n                                 ∆lim\n                                  Y• (D) ⊆ R\n                                             l−κν\n                                                  × {0}n−l × Rκν .\nNow consider a sufficiently positive ample divisor A′ so that ∆Y• (εA′ ) contains\n                                (                            n\n                                                                      )\n                                                             X\n                         △ε := (x1 , · · · , xn ) xi ≥ 0 and   xi ≤ ε\n                                                             i=1\n\nfor all ε > 0. We may assume that A is sufficiently ample so that A′′ := A − A′ is also ample.\nBy the convexity of ∆Y• (D) (cf. [LM, Proof of Corollary 4.12]), we have\n      ∆lim            lim             ′               ′′          ′\n       Y• (D) + △ε ⊆ ∆Y• (D) + ∆Y• (εA ) ⊆ ∆Y• (D + εA ) + ∆Y• (εA ) ⊆ ∆Y• (D + εA).\n\nSince dim ∆lim\n           Y• (D) = l, it follows that\n                                                           1\n              C · volRl ∆lim\n                         Y• (D) · ε\n                                   n−l\n                                       ≤ volRn ∆Y• (D + εA) =· volX (D + εA).\n                                                          n!\nfor some constant C > 0 depending only on n and l. We get a contradiction to [Le1, Theorem\n1.1 (2)] since l > κν .                                                                  \u0003\nCorollary 3.22. Let D be a pseudoeffective divisor on a smooth projective variety X. Fix a\npositive volume subvariety V ⊆ X of D and consider an admissible flag Y• on X containing V .\nThen ∆lim            n−κν (D) × Rκν (D) . Furthermore, we have\n         Y• (D) ⊆ {0}            ≥0\n                                                                         1\n             dim ∆lim\n                  Y• (D) = κν (D) and        volRκν (D) (∆lim\n                                                          Y• (D)) =           vol+\n                                                                                 X|V (D)\n                                                                      κν (D)!\nwhere ∆lim\n       Y• (D) is regarded as a convex subset of R\n                                                  κν (D) .\n\nProof. Immediate by Theorem 3.20 and Proposition 3.21.                                       \u0003\n\f                OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                          19\n\nRemark 3.23. We do not need to assume the generality of Yn = {x} as we did for the valuative\nOkounkov body in Theorem 3.12.\nRemark 3.24. Boucksom also studies the limiting Okounkov body (the numerical Okounkov\nbody in his terminology) of a pseudoeffective divisor with respect to any admissible flag in [B,\n4.1.3]. He defines the limiting Okounkov body as a fiber of the global Okounkov body (see [LM,\nTheorem B]) over a given pseudoeffective divisor class. He proves that dim ∆lim   Y• (D) ≤ κν (D)\nfor any admissible flag Y• ([B, Lemma 4.8]) and the inequality can be strict ([B, Example 4.14]).\nFurthermore, he also shows that there exists an admissible flag Y• such that dim ∆lim    Y• (D) =\nκν (D) when D is nef ([B, Proposition 4.9]). Our result Corollary 3.22 generalizes his result.\n  Using Corollary 3.22, we can give a new characterization of numerical Iitaka dimension.\nCorollary 3.25. Let D be a pseudoeffective divisor on a smooth projective variety X. Then we\nhave\n              κν (D) = max{dim ∆lim\n                                  Y• (D) | Y• is an admissible flag on X }.\n\nProof. By [B, Lemma 4.8], we know that dim ∆lim    Y• (D) ≤ κν (D) for any admissible flag Y•\non X. If Y• contains a positive volume subvariety, then it follows from Corollary 3.22 that\ndim ∆lim\n      Y• (D) = κν (D). Thus the assertion follows.                                         \u0003",
          "local_file": "source-extracts/1508.03922v5--theorems-3.20-3.22-and-proofs-and-flag-warning.txt",
          "sha256": "1af071c06c62f4e5a4e337980d1e48bbe45e6c4716ca00ec72176271119d8449",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        },
        {
          "id": "bad-flag-example-4.1",
          "first_line": 1258,
          "last_line": 1274,
          "first_textflow_page": 21,
          "last_textflow_page": 21,
          "literal": "                                          4. Examples\n   In this section, we exhibit various examples and counterexamples related to our results. We\nstart with an example that shows that for some badly chosen admissible flags, Theorems 3.12\nand 3.20 do not hold.\nExample 4.1. Let π : S → P2 be a blow-up of P2 at two distinct points with exceptional\ndivisors E1 and E2 , and L ∈ |π ∗ OP2 (1)| be an effective divisor containing E1 but not containing\nE2 . Consider a non-big effective divisor D := (L − E1 ) + E2 , and fix an admissible flag\n                                        Y• : S ⊇ E2 ⊇ {x}\nwhere x is a general point on E2 . Here we note that E2 is neither a Nakayama subvariety nor a\npositive volume subvariety of D. We have\n                 ∆val       lim                     2\n                  Y• (D) = ∆Y• (D) = {(x1 , x2 ) ∈ R | 1 ≤ x1 ≤ 2 and x2 = 0}\nwhose Euclidean volume in the x1 -axis is 1. However, note that B− (D) = B+ (D + εA) = E2\nfor an ample divisor A and a small ε > 0. Thus we see that volX|E2 (D) = vol+\n                                                                            X|E2 (D) = 0. We\nalso remark that ∆val       lim\n                  Y• (D) = ∆Y• (D) is not in the x2 -axis as expected.",
          "local_file": "source-extracts/1508.03922v5--bad-flag-example-4.1.txt",
          "sha256": "7fa4d7ccd6997abf8a22f824030ab5adb488a470e7fed9112d45b235818e1966",
          "content_kind": "Literal statement(s) and relevant proof body/bodies; conjecture records have no supplied proof."
        }
      ],
      "application_checks": [
        "Theorem B/Corollary 3.22 is for a pseudoeffective real divisor on a smooth projective variety, with a flag containing a positive volume subvariety.",
        "The lower-dimensional mass is augmented restricted volume along that subvariety, not an unrestricted flag-independent number.",
        "Remark 3.24 explicitly allows strict dimension inequality for other flags.",
        "None of these algebraic theorems is applied to the nonprojective transcendental example. Its product formula is proved directly."
      ]
    }
  ]
}


# Complete actual public primary text: 2309.07584v3

                                                           Transcendental Okounkov bodies
                                                 T. Darvas, R. Reboulet, D. Witt Nyström, M. Xia, K. Zhang

                                                                    To the memory of Jean-Pierre Demailly



                                                                                   Abstract
arXiv:2309.07584v3 [math.DG] 5 Jan 2026




                                                  We show that the volume of transcendental big (1, 1)-classes on compact Kähler
                                               manifolds can be realized by convex bodies, thus answering questions of Lazarsfeld–
                                               Mustaţă and Deng. In our approach we use an approximation process by partial
                                               Okounkov bodies together with properties of the restricted volume, and we study
                                               the extension of Kähler currents, as well as the bimeromorphic behavior of currents
                                               with analytic singularities. We also establish a connection between transcendental
                                               Okounkov bodies and toric degenerations.


                                          Contents
                                          1 Introduction                                                                              1
                                          2 Preliminaries                                                                              5
                                          3 Transcendental Okounkov bodies                                                            11
                                          4 Lifting the flags                                                                         14
                                          5 Partial Okounkov bodies                                                                   17
                                          6 Extension of Kähler currents                                                             19
                                          7 The volume identity                                                                       22
                                          8 Moment bodies                                                                             27


                                          1    Introduction
                                          In toric geometry, there is a striking correspondence between Delzant polytopes ∆ and
                                          polarized toric manifolds (X∆ , L∆ ). Much of the geometry of the toric manifold is encoded
                                          in its Delzant polytope: for instance, the volume of L∆ , defined as

                                                                                         h0 (X∆ , kL∆ )
                                                                        vol(L∆ ) := lim                 ,
                                                                                     k→∞     k n /n!

                                          is seen to equal n! times the Euclidean volume of ∆.
                                              Toric manifolds are very special, due to their large group of symmetries. Thus, it was
                                          quite remarkable that Okounkov in the 90s [41] showed how one can naturally associate
                                          a convex body ∆(L) to any polarized manifold (X, L). These bodies are now known as
                                          Okounkov bodies (or Newton–Okounkov bodies).


                                                                                        1
    To construct the Okounkov body, one fixes a complete flag of submanifolds Y• = (X =
Y0 ⊃ Y1 ⊃ · · · ⊃ Yn−1 ⊃ Yn ). To any s ∈ H 0 (X, kL) \ {0} we associate a valuation vector
ν(s) := (ν1 , . . . , νn ) ∈ Rn in the following way. First, we let ν1 be the order of vanishing
of s along Y1 . Next, if sY1 is a defining section for Y1 , we get that (s/sνY11 )|Y1 is a non-zero
section of Lk ⊗ O(−ν1 Y1 ) restricted to Y1 . We set ν2 to be the order of vanishing along
Y2 of this section. Continuing this process yields the full valuation vector ν(s). The
Okounkov body of L, denoted ∆Y• (L), is then defined as the closure of the set of rescaled
valuation vectors

                     ∆Y• (L) := {ν(s)/k : s ∈ H 0 (X, kL) \ {0}, k ∈ N}.

Convexity of the Okounkov body follows from the fact that ν(s ⊗ t) = ν(s) + ν(t). A
more difficult fact, however, is that the Okounkov body satisfies the volume identity:
                                                      1
                                  volRn (∆Y• (L)) =      vol(L).                             (1.1)
                                                      n!
    Later Lazarsfeld–Mustaţă [35] and Kaveh–Khovanskii [34] showed that Okounkov’s
construction works for more general big line bundles as well, together with the analogous
volume identity (1.1). One should note that the volume of big line bundles is a much
more subtle notion compared to the ample case; using convex bodies to study this object
was indeed a breakthrough. For example, Lazarsfeld–Mustaţă used Okounkov bodies to
show that the volume function is C 1 on the cone of big R-divisors [35, Corollary C].
Since then, numerous applications of Okounkov bodies have been found in algebraic and
complex geometry (see e.g. [3, 9, 36, 8, 32], to only name a few works).
    The Okounkov body is a numerical invariant of the line bundle, i.e., it only depends on
the first Chern class c1 (L) of L, which is a real cohomology class of bidegree (1, 1). Real
cohomology classes that do not correspond to line bundles are called transcendental.
The weaker positivity notions of being big or pseudoeffective have been extended to
transcendental classes by Demailly, and Boucksom showed in [12] how to define the volume
vol(ξ) of a transcendental class ξ.
    In light of the above, given a flag Y• , a very natural question raised by Lazarsfeld–
Mustaţă [35, p. 831] asks whether one can define the Okounkov body ∆Y• (ξ) associated
with a transcendental class ξ, in such a way that it satisfies the volume identity
                                                      1
                                  volRn (∆Y• (ξ)) =      vol(ξ).                             (1.2)
                                                      n!
    There are some notable open problems related to the volume of big transcendental
classes, such as obtaining transcendental holomorphic Morse inequalities, or the continu-
ous differentiability of the volume on the big cone [4]. Identity (1.2) could turn out to be
useful with tackling these problems, the same way as it was in the line bundle case [35,
Corollary C].
    As we explain now, in [25] Deng proposed a construction of Okounkov bodies ∆(ξ)
for a transcendental class ξ. In the transcendental case global sections make no sense,
but these classes admit a lot of currents. The vanishing order of a global section s of a
line bundle can be expressed using Lelong numbers of the current of integration [s = 0].
Deng’s construction rests on the idea that computing Lelong numbers of appropriate
currents should be the transcendental analogue of computing vanishing order of sections
in the algebraic case.

                                                2
    Let (X, ω) be a connected compact Kähler manifold of dimension n. Let ξ := {θ} ∈
  1,1
H (X, R) be a big (or pseudoeffective) cohomology class, with θ being a smooth closed
(1, 1)-form. Assume that X has a complete flag of submanifolds

                         Y• := (X = Y0 ⊃ Y1 ⊃ · · · ⊃ Yn−1 ⊃ Yn ),

Let A(X, ξ) be the set of positive
                               P currents    θ + ddc u in ξ with analytic singularities. This
                                      2
means that locally u = c log( j |fj | ) + h, for c ∈ Q+ , fj holomorphic, and h bounded.
    To any T0 ∈ A(X, ξ) one associates a valuation vector ν(T0 ) = (ν1 , . . . , νn ) ∈ Rn in
the following manner. Let ν1 equal ν(T0 , Y1 ), the generic Lelong number of T0 along Y1 .
One can show that T1 := (T0 − ν1 [Y1 ])|Y1 has analytic singularities on Y1 . Then one sets
ν2 := ν(T1 , Y2 ) and continues the above process until all components of ν(T0 ) are defined.
The Okounkov body of ξ, denoted ∆Y• (ξ) (or just ∆(ξ), once the flag is fixed), is then
defined as:
                                  ∆(ξ) := ν(A(X, ξ)) ⊂ Rn .
As in the line bundle case, the convexity of the Okounkov body follows from the fact
that ν(S + T ) = ν(S) + ν(T ). When ξ is a pseudoeffective class, one puts ∆(ξ) =
∩ε>0 ∆(ξ + ε{ω}). For more details, the reader is invited to consult § 3.
   Deng’s body coincides with Okounkov’s when ξ is the first Chern class of a big line
bundle [25]. Thus, this body is a natural generalization of the Okounkov body to the
transcendental setting, and we will work with Deng’s definition in our paper.
   It remained to show that the transcendental Okounkov body satisfies (1.2). Deng
proved that this is true when the dimension of X is at most two, but the general case
was open until now. Our main result proves the volume identity in full generality:

Theorem 1.1. Let ξ be a big cohomology class on X and Y• be a flag on X. Then the
associated Okounkov body ∆(ξ) of ξ satisfies the volume equality
                                                  1
                                 volRn (∆(ξ)) =      vol(ξ).                            (1.3)
                                                  n!
   Passing to the limit, the volume identity can be extended to pseudoeffective classes
as well:

Corollary 1.2. The identity (1.3) holds even if ξ is pseudoeffective.

    Theorem 1.1 and Corollary 1.2 confirm [25, Conjecture 1.4] and also give an affirmative
answer to the question of Lazarsfeld–Mustaţă [35, p. 831].
    We note that, a priori X might not contain any proper complex submanifolds of
positive dimension, let alone flags. For example, this happens if X is a non-algebraic
simple compact torus. However, one can always blow up X at a point p. Then one
can construct a flag Y• on Blp X with Y1 ∼   = CPn−1 being the exceptional divisor and
Y2 ⊃ · · · ⊃ Yn being a flag of linear subspaces in Y1 . Therefore, up to modifying X and
pulling back ξ, our main result is always applicable.
    The proof of Theorem 1.1 proceeds by induction on dim X, with the recent work
of the third named author [51] helping with the induction step. In our proof, it will
be necessary to approximate the volume of ∆(ξ) using the volume of partial Okounkov
bodies, as studied in [52]. The advantage of our partial Okounkov bodies is that they
have good bimeromorphic properties, allowing to reduce their study to the case when ξ
is Kähler. We will also study currents with analytic singularities whose pushforward also

                                             3
have this property. This contrasts Deng’s approach in the surface case [25], where he can
apply the Zariski decomposition, without modifying the surface (cf. [13]).
   In our approach, an extension result slightly generalizing [19, Theorem 1.1] will be
necessary to relate the slice volume of the Okounkov body to the restricted volume of
the big class (see Property Cn ). Let us state this extension result, which could be of
independent interest, in light of [26, Conjecture 37] and [17].
Theorem 1.3. Let V ⊆ X be a connected positive dimensional compact complex sub-
manifold of (X, ω), and T = ω|V + ddc φ be a Kähler current on V . Assume that eφ is a
Hölder continuous function on V . Then one can find a Kähler current T̃ = ω + ddc φ̃ on
X such that φ̃|V = φ, i.e., T̃ extends T . Moreover, φ̃ is continuous on X \ V and eφ̃ is
Hölder continuous on X. In addition, if φ has analytic singularities, then so does φ̃.
    For the definition of analytic singularities we refer to Definition 2.2. Our definition
is more general compared to [19]; see Remark 2.7 for a comparison of various notions of
analytic singularities appearing in the literature.
    Potentials with exponential Hölder continuity often appear in the literature (see [6,
42]), so this result may find other applications in Kähler geometry. Similar to [19], we
prove our extension result using Richberg’s gluing technique. We will adapt the exposition
from [22, Section I.5.E], which allows for some simplifications.
    Note that one can not expect Theorem 1.3 to hold for big classes, due to the obvious
obstruction coming from the non-Kähler locus. In fact one can hope to extend a Kähler
current in a big class only if it has appropriate prescribed singularities along the non-
Kähler locus. This technical point will arise in our proof of Theorem 1.1, and will be
circumvented with the help of partial Okounkov bodies.
    In Section 8, we describe an alternative way of defining a convex body associated
with a big class ξ. Instead of using the valuation vectors ν(T ) of closed positive currents
T ∈ ξ, we consider certain iterated toric degenerations of X, where in n steps (X, T )
is degenerated to (Pn , Tn ). Here, T is a closed positive (1, 1)-current in ξ, while Tn is a
closed positive and toric (1, 1)-current on Pn . As described in Section 8, any such toric
degeneration (Pn , Tn ) comes with a naturally associated moment body ∆(Tn ). This allows
us to define the moment body ∆µ (ξ) of ξ as the closure of the union of the moment bodies
of all such metrized toric degenerations of (X, ξ). We note that an algebraic version of
this construction is considered in the recent thesis of Murata [38]. We show that this
alternative body agrees with the Okounkov body of ξ:
Theorem 1.4. For ξ big the moment body ∆µ (ξ) coincides with the Okounkov body ∆(ξ).
    As a direct consequence of Theorem 1.4 we get that ∆(Tn ) ⊆ ∆(ξ) for all toric degen-
erations (Pn , Tn ) of (X, ξ), and that for any ϵ > 0 we can find a toric degeneration (Pn , Tn )
of (X, ξ) such that the Hausdorff distance between ∆(Tn ) and ∆(ξ) is less than ϵ. This
provides a strong link between transcendental Okounkov bodies and toric degenerations,
which we think will be useful in further investigations.
    The above result is inspired by the works of Harada–Kaveh [31] and Kaveh [33], who,
building on earlier work of Anderson [2], prove related results in the algebraic setting.
This theorem is also related to work on canonical growth conditions [48].

Further directions Finally, we mention several appealing directions that one could
explore further. One may try to define the Chebyshev transform of [47] in the transcen-
dental setting to study weak geodesic rays in connection with transcendental notions of

                                               4
K-stability attached to cscK metrics [28, 43]. One could try to use Okounkov bodies to
make progress on the conjectured transcendental Morse inequality [4], or to show differ-
entiability of the volume in the big cone, akin to [35, Corollary C]. Moreover, one can
study the mixed volume of Okounkov bodies and investigate its relation with the movable
intersection product of big classes introduced in [11].
    Regarding the extension of Kähler currents, it is intriguing to understand how far the
Richberg type gluing techniques can be pushed.
    The results of this paper seem to naturally extend to manifolds of the Fujiki class C.
Going beyond, we ask if one can attach Okounkov bodies to transcendental pseudoeffec-
tive cohomology classes ξ on general compact complex manifolds.
    Acknowledgements.We thank Sébastien Boucksom for suggesting Lemma 2.11, sim-
plifying our original argument, and for helpful discussions regarding analytic singularities.
We also thank Zhiwei Wang for discussions on the extension of Kähler currents. We also
thank the anonymous referees for suggestions on how to improve the presentation.
    The first named author is partially supported by an Alfred P. Sloan Fellowship and
National Science Foundation grant DMS–2405274. The second named author is sup-
ported by the Knut och Alice Wallenbergs Stiftelse. The third named author is partially
supported by a grant from the Swedish Research Council and a grant from the Göran
Gustafsson Foundation for Research in Natural Sciences and Medicine. The fourth named
author is supported by Knut och Alice Wallenbergs Stiftelse grant KAW 2024.0273. The
fifth named author is supported by NSFC grants 12101052, 12271040, and 12271038.


2    Preliminaries
Let (X, ω) be an n-dimensional connected compact Kähler manifold. Let ξ := {θ} ∈
H 1,1 (X, R) be a big cohomology class. We write Z+ (X) for the set of closed positive
(1, 1)-currents on X and Z+ (X, ξ) for the set of T ∈ Z+ (X) representing ξ. A function
φ : X → [−∞, ∞) is called quasi-plurisubharmonic (qpsh) if locally φ = ϕ + ψ, where ϕ
is smooth and ψ is plurisubharmonic. Put

           PSH(X, θ) := {φ : X → [−∞, ∞) :
                         φ is a qpsh function on X such that θ + ddc φ ≥ 0},
               √
where ddc :=        ¯
                −1∂ ∂/2π. Given a qpsh function φ, the Lelong number of φ at x ∈ X is

                ν(φ, x) := sup{c ≥ 0 : φ(z) ≤ c log |z − x|2 + O(1) near x}.

Given an irreducible analytic subset E ⊂ X, the generic Lelong number of φ along E is

                                  ν(φ, E) := inf ν(φ, x).
                                              x∈E

If T = θ + ddc φ for φ ∈ PSH(X, θ), then set ν(T, x) := ν(φ, x) and ν(T, E) := ν(φ, E).
    If ϕ, ψ are qpsh, we say that ϕ is more singular than ψ and write ϕ ⪯ ψ if ϕ ≤ ψ + C
for some constant C. If ϕ ⪯ ψ and ψ ⪯ ϕ, we then write ϕ ∼ ψ and say that ϕ and ψ
have the same singularity type. This defines an equivalence relation.
    Given T, S ∈ Z+ (X), with T = θ1 + ddc ϕ and S = θ2 + ddc ψ, θ1 , θ2 being smooth,
then we say that T is more singular than S if ϕ is more singular than ψ, and write T ⪯ S.
If ϕ ∼ ψ we also say that T and S have the same singularity type and write T ∼ S.

                                             5
Lemma 2.1. Let π : Z → X be a proper bimeromorphic morphism with Z being a Kähler
manifold. Then π ∗ and π∗ induce a bijection between Z+ (X, ξ) and Z+ (Z, π ∗ ξ).
Proof. One can show that the pullback map π ∗ is an isomorphism between PSH(X, θ)
and PSH(Z, π ∗ θ), where θ is a smooth closed (1, 1)-form representing ξ.
    It is clear that the pullback map is injective. To show surjectivity, let v ∈ PSH(Z, π ∗ θ).
Let U ⊂ X be the Zariski open set such that π : π −1 (U ) → U is biholomorphic. Then
w := v ◦ π −1 ∈ PSH(U, θ), moreover w is bounded from above. Since X \ U is an analytic
set, it follows that w extends to an element of PSH(X, θ) [22]. Since π ∗ w = v away from
an analytic set, it follows that π ∗ w = v [22].
   For a positive current R ∈ Z+ (X, ξ), let E+ (R) denote the locus where R has positive
Lelong number. The non-Kähler locus EnK (ξ) and Kähler locus K(ξ) are defined by
                                \
             EnK (ξ) :=                      E+ (R), K(ξ) := X \ EnK (ξ).
                          Kähler current R∈Z+ (X,ξ)

The class ξ is Kähler if and only if EnK (ξ) = ∅.
Definition 2.2. Let q ∈ X be a point. A qpsh function φ on X is said to have (local)
analytic singularities near q if there exists an open set U containing q such that
                                              X
                                   φ = c log     |fi |2 + h,
                                                   i

where fi ∈ OX (U ) is a finite set of holomorphic functions, c ∈ Q≥0 , and h is bounded.
   If I is a coherent ideal sheaf on X and c ∈ Q>0 , we say that a qpsh function φ on X
has analytic singularities (of type (I, c)) if for any q ∈ X, we can locally write φ as
                                              X
                                   φ = c log      |fi |2 + h,
                                                   i

where f1 , . . . , fN is a finite collection of local generators of I, and h is bounded.
   Similarly, we say a positive current T =: θ+ddc φ ∈ Z+ (X, ξ) has analytic singularities
near q (resp. has analytic singularities (of type (I, c))) if so does φ. We set
            A(X, ξ, q) := {T ∈ Z+ (X, ξ) : T has analytic singularities near q} ,
             A(X, ξ) := {T ∈ Z+ (X, ξ) : T has analytic singularities} ,
               A(X) := {T ∈ Z+ (X) : T has analytic singularities} .
Remark 2.3. If φ has local analytic singularities near every point of X, then there is a
coherent ideal sheaf I and c ∈ Q>0 such that φ has analytic singularities of type (I, c).
   To see this, take a finite covering {Uj }j of X such that φ can be written as
                                        cj log |Fj |2 + O(1),
where Fj = (f1j , . . . , fnj j ) is a finite tuple of holomorphic functions on Uj . In the above
representation we can always divide cj by an arbitrary N ∈ Z>0 , by adjusting the Fj .
Since X is compact, we can guarantee that cj does not depend on j. We denote this
common value by c.
    Now locally on Uj , the ideal sheaf I can be constructed as the integral closure of the
ideal generated by f1j , . . . , fnj j . As a consequence of Briançon–Skoda theorem (see [23,
Corollary 11.18]), this gives a well-defined coherent ideal sheaf on X. But note that T
does not uniquely determine the pair (I, c).

                                                   6
    Due to the above remark, when talking about currents T with analytic singularities,
we will often not specify the type (I, c).
    We continue with a well known observation, that follows from the short argument of
[23, Proposition 4.1.8]:

Lemma 2.4. If u, v are qpsh functions with analytic singularities, then max(u, v) also
has analytic singularities.

   The following useful result due to Siu [44] will be also frequently used.

Lemma 2.5. Assume T ∈ ξ is a positive current and D is a prime divisor on X. If
ν(T, D) ≥ a for some a ∈ Q≥0 , then T − a[D] is a positive current in ξ − a{[D]}.
Moreover, if T has analytic singularities near a point, then so does T − a[D].

Proof. The first assertion follows from Siu’s decomposition [44].
   Let q ∈ X. In a neighborhood of q we have that
                                           X
                                 u = c log    |fj |2 + O(1).
                                            j


   After rescaling we can assume that a, c ∈ Z. Let T = θ + ddc u for some qpsh function
u and smooth closed (1, 1)-form θ.
   By the Lelong–Poincaré formula there exists a neighborhood U of q and w ∈ O(U )
such that ddc log |w|2 = a[D]. By properties of Lelong numbers there exists C > 0 such
that
                                   u ≤ log |w|2 + C.
This implies that |fj |2c ≤ C̃|w|2 for all j, for some C̃ > 0. Due to the Riemann extension
theorem, there exists gj ∈ O(UP   ) such that fjc = wgj . As a result, the local singularities
of T − a[D] is modelled by log j |gj |2 .
   We also need to refine the notion of analytic singularities, in a way that goes back to
Demailly [24]. The definition below is a bit lengthy but turns out to be the most suitable
one for this paper.

Definition 2.6. Let I ⊆ OX be an analytic coherent ideal sheaf and c ∈ Q>0 . A qpsh
function φ on X is said to have gentle analytic singularities of type (I, c) if

  1. eφ/c : X → R≥0 is a smooth function;

  2. locally φ can be written as
                                                    X
                                      φ = c log         |fi |2 + h,                     (2.1)
                                                    i

      where {fi } is a finite set of local generators of I and h is a bounded remainder;

  3. there is a proper bimeromorphic morphism π : X̃ → X from a Kähler manifold X̃
     and an effective Z-divisor D on X̃ such that one can write π ∗ φ locally as

                                       π ∗ φ = c log |g|2 + h,

      where g is a local equation of the divisor D and h is smooth.

                                                7
    A positive current T = θ+ddc φ ∈ Z+ (X, ξ) is said to have gentle analytic singularities
of type (I, c) if so does φ. We set

             Ω(X, ξ) := {Kähler current in ξ with gentle analytic singularities} .

Remark 2.7. Let φ be a qpsh function with analytic singularities of type (I, c) such
that the remainder h is smooth in (2.1). Then φ is easily seen to have gentle ana-
lytic singularities. The reverse direction is not true however, as the smoothness of the
remainder depends on the choice of generators for I (we are grateful to S. Boucksom
for helpful discussions regarding this point). For instance one can look at the potentials
                                                              2 +|z |2
log(|z1 |2 + |z2 |2 ) = log(|z1 |2 + |2z2 |2 ) + log |z|z11||2 +|2z2
                                                                    2|
                                                                             2
                                                                       2 in C ; the first has 0 as its smooth
                                               2    2
remainder while the remainder log |z|z11||2 +|2z
                                            +|z2 |
                                                 2|
                                                    2 of the second potential is not smooth. This

motivates the use of gentle analytic singularities throughout the paper.

    In the whole paper, we are using the word modification in a ’restrictive’ sense: We
shall say that π : Y → X is a modification if it is bimeromorphic, and it is a composition
of a sequence of blowing-ups with smooth centers. Observe that by the construction in
[46, Theorem 2.0.2], the embedded resolutions where the ambient space is compact are
always modifications in this sense. Note that if X is a Kähler manifold, then so is Y .
    It follows from Definition 2.6 that one can always resolve the singularities of Kähler
currents with gentle analytic singularities. More precisely, by [46, Theorem 3.6.1], for
any R ∈ Ω(X, ξ), one can find a modification π : Y → X so that

                                             π ∗ R = β + [D],

where β is a smooth semipositive (1, 1)-form on X̃ and D is an effective Q-divisor on Y .
    A classical regularization result due to Demailly [24] shows that there are plenty of
Kähler currents in ξ with gentle analytic singularities. We refer the reader to [27, Theorem
3.2] for a proof of the following version of Demailly’s regularization theorem, and also
[23, Corollary 13.13] for a detailed exposition.

Theorem 2.8. Let T = θ+ddc φ ∈ Z+ (X, ξ) be a Kähler current. Then one can construct
a sequence Tk = θ + ddc φk , which are Kähler currents with gentle analytic singularities of
type (I(kφ), k1 ) and φ ≤ φk for all k ≫ 0. Here I(kφ) denotes the multiplier ideal sheaf
of kφ that is generated by holomorphic functions f ∈ OX such that |f |2 e−kφ ∈ L1loc .

    As a direct consequence, we have the following result.

Lemma 2.9. For any two Kähler currents T1 , T2 ∈ Z+ (X, ξ), one can find T3 ∈ Ω(X, ξ)
that is less singular than both T1 and T2 .

Proof. Write Ti = θ + ddc φi for i = 1, 2. Put φ0 := max{φ1 , φ2 }. Then T := ω + ddc φ0
is a Kähler current that is less singular than both T1 and T2 . Note that T may not have
gentle analytic singularities, but then we can apply Theorem 2.8 to find another Kähler
current T ′ ∈ Ω(X, ξ) that is less singular than T .
   This lemma together with the Noetherian property of analytic sets imply that one
can find R ∈ Ω(X, ξ) such that E+ (R) = EnK (ξ). So in particular, EnK (ξ) is a closed
analytic subset of X (see [13, Theorem 3.17]).



                                                        8
Remark 2.10. By definition, if T ∈ A(X) has type (I, c) and g : Y → X is a proper
bimeromorphic morphism and Y is a Kähler manifold, then g ∗ T has type (OY · g −1 I, c).
    In fact, if we locally write T as ddc φ for some φ satisfying φ = c log(|f1 |2 + · · · +
|fN |2 ) + O(1), then g ∗ T can locally be written as c log(|g ∗ f1 |2 + · · · + |g ∗ fN |2 ) + O(1). The
ideal generated by g ∗ f1 , . . . , g ∗ fN is just OY · g −1 I.

   By the above remark, the pullback of currents with analytic singularities is well-
behaved. The same can not be said about pushforwards. However, the following result
suggested by Boucksom shows that in certain particular situations good behaviour can
be expected:

Lemma 2.11. Assume that π : Z → X is a proper bimeromorphic morphism and Z is a
Kähler manifold. Let ξ be a big class on X and D an effective Q-divisor on Z. Assume
that π ∗ ξ − {D} contains a smooth Kähler form β. Let T := β + [D]. Then π∗ T belongs
to A(X, ξ).

Proof. By rescaling, we may assume that D is an integral divisor.
    After a further rescaling of D, we claim that −D is π-globally generated in the follow-
ing sense: For all z ∈ Z there exists an open neighborhood U ⊂ X of π(z) such that the
sections O(−D)(π −1 (U )) generate O(−D)z . Let us assume the claim for the moment. It
implies that:
                              OZ · π −1 π∗ OZ (−D) = OZ (−D).                         (2.2)
    By definition, T has analytic singularities of type OZ (−D). We want to show that
π∗ T ∈ α has analytic singularities of type π∗ OZ (−D).
    By [12, Proposition 2.2], there is a closed positive current S on X with analytic singu-
larities of type π∗ OZ (−D). Then π ∗ S has analytic singularities of type OZ ·π −1 π∗ OZ (−D)
by Remark 2.10.
    From (2.2) we obtain that π ∗ S ∼ T = π ∗ π∗ T (the latter equality follows from
Lemma 2.1). It follows that S ∼ π∗ T . So π∗ T has analytic singularities of type
π∗ OZ (−D).
    Finally, we address the claim. This is a simple consequence of [39, Proposition 1.4]
when π is projective. Here we give a different proof by adapting the L2 techniques of [23,
Theorem 6.27].
    Let ω be a Kähler metric of X, satisfying θ < ω, where θ is a smooth closed (1, 1)-form
in the class of ξ.
    Let U ⊂ X be a coordinate ball neighborhood of π(z). We can assume existence of
v ∈ C ∞ (U ) such that ω = ddc v.
    Let h be a hermitian metric of O(−D) on Z such that iΘ(h) = β − π ∗ θ. We consider
h̃ = he−v◦π , a hermitian metric on O(−D)|π−1 (U ) . We get that h̃ is a positive metric,
since iΘ(he−v◦π ) = β + π ∗ (ω − θ) ≥ β > 0.
    Let fz ≥ 0 be a smooth function on X such that fz (x) = |x−z|2n+1 in a neighborhood
of z, and fz is bounded away from zero, away from z. Since Z is compact, we can construct
fz in such a manner that there exists ε > 0 and C > 1, both independent of z, such that:

                                                                           1
                  fz |B(z,ε) = |x − z|2n+1 , ∥fz ∥C 2 (Z) ≤ C,      sup       ≤ C,                 (2.3)
                                                                  X\B(z,ε) fz


where B(z, ε) is a geodesic ball centered at z, with radius ε > 0.



                                                   9
   Let m be an arbitrary hermitian metric on KZ−1 . Let ĥk := h̃k ⊗ me− log fz be a
hermitian metric on O(−kD) ⊗ KZ−1 |π−1 (U ) . We have that

            iΘ(h̃k ) = iΘ(hk ) + iΘ(m) + ddc log fz ≥ kβ + iΘ(m) + ddc log fz .
Since log fz is psh in B(z, ε), for k big enough (only dependent on the constant C of
(2.3)) iΘ(ĥk ) is a strongly positive metric.
    As a result of the compactness of Z, taking a sufficiently divisible k, we can replace
D (resp. θ, ω, β) with kD (resp. kθ, kω, kβ) and assume that ĥ is a strongly positive
(singular) metric of O(−D) ⊗ KZ−1 on π −1 (U ).
    Let q ∈ O(−D)z = (O(−D) ⊗ KZ−1 ⊗ KZ )z . Let ϕ : Z → R≥0 be a smooth
function supported in a neighbourhood of z, identically equal to 1 near z, so that
ϕq ∈ C ∞ (π −1 (U ), O(−D)). Then ∂(ϕq)  ¯     is a smooth 1-form on π −1 (U ), with values
in O(−D) ⊗ KZ−1 ⊗ KZ ⊗ I(e− log fz ).
    Since U is a coordinate ball, we get that π −1 (U ) is weakly pseudoconvex, so [23,
Corollary 5.3] is applicable to yield existence of a smooth section g of O(−D) ⊗ KZ−1 ⊗
                                                    ¯
KZ ⊗ I(e− log fz ), defined on π −1 (U ) with ∂g = ∂(ϕq) on π −1 (U ).
    Due to our choice of fz , g must vanish at z. Hence, w := ϕq−g ∈ H 0 (π −1 (U ), O(−D)),
moreover (q − w)z ∈ mZ,z · O(−D)z .
    Since O(−D)z is a finite OZ,z -module, we apply Nakayama’s lemma [1, Proposi-
tion 2.8] to conclude that O(−D)(π −1 (U )) generates O(−D)z , proving the claim.
   Finally, we recall the notion of non-pluripolar volumes.
Definition 2.12 ([12]). The volume vol(ξ) of pseudoeffective class ξ is zero if ξ is not
big. If ξ is big then                          Z
                                  vol(ξ) :=     sup            T n.
                                              T ∈Ω(X,ξ)    X

   Here and in the sequel, products of the form T n are interpreted as non-pluripolar
complex Monge–Ampère measures, as introduced in [5]. It is shown in [12] that the
volume function vol(·) thus defined is continuous in H 1,1 (X, R).
Definition 2.13 ([30, 37, 51, 20]). Assume Z ⊂ X is a closed complex submanifold of
dimension d. If Z ∩ K(ξ) ̸= ∅, then the restricted volume volX|Z (ξ) of ξ along Z is
                                                   Z
                             volX|Z (ξ) := sup        T |dZ .
                                               T ∈Ω(X,ξ)   Z

If Z ∩ K(ξ + ε{ω}) ̸= ∅ for any ε > 0, then set
                            volX|Z (ξ) := lim volX|Z (ξ + ε{ω}).
                                         ε→0

Otherwise, set volX|Z (ξ) := 0.
    Note that the restricted volume volX|Z (ξ) could be strictly smaller than the volume
of the restricted class ξ|Z . In general, the restricted volume is notR easy to compute. But
when ξ is semipositive, one simply has volX|Z (ξ) = vol(ξ|Z ) = Z ξ d . Also recall that,
in the open cone of big classes whose non-Kähler locus does not contain Z, the function
volX|Z (·) is continuous [37, Corollary 4.11].
    The following result was proved by the third named author [51] and extended very
recently by Vu [45] (see also [25, Theorem 1.5] for the surface case and [7, 35, 49] for the
case of projective manifolds). It will play a crucial role in proving Theorem 1.1.

                                               10
Theorem 2.14. Assume that Z is a connected smooth hypersurface in X such that
Z ∩ K(ξ) ̸= ∅. Put νmax (ξ, Z) := sup{ν(T, Z) : T ∈ Ω(X, ξ)}. Then one has

                         d
                                vol(ξ − t{Z}) = −n volX|Z (ξ)
                         dt t=0

and                                  Z νmax (ξ,Z)
                        vol(ξ) = n                  volX|Z (ξ − t{Z}) dt.
                                      0

Remark 2.15. According to the recent result of [45], the assumption on Z can be relaxed:
it suffices to assume that Z is an irreducible hypersurface in X. In particular, the case
where Z is contained in the non-Kähler locus of ξ is also allowed.

Proof. The first point is due to [51, Theorem C]. The second point is also contained in
[51]. We recall its proof for the reader’s convenience.
    We claim that Z ∩ K(ξ − t{Z}) ̸= ∅ for any t ∈ [0, νmax (ξ, Z)). Indeed, for any small
ε > 0, one can find T ∈ Ω(X, ξ) such that ν(T, Z) = νmax (ξ, Z) − ε. And also, due to
Z ∩K(ξ) ̸= ∅, there exists S ∈ Ω(X, ξ) with ν(S, Z) = 0. Considering linear interpolation
between S and T shows that for any t ∈ (0, νmax (ξ, Z)) one can find a Kähler current
G ∈ Z+ (X, ξ) so that ν(G, Z) = t. Then Siu’s decomposition implies that G − t[Z] is a
Kähler current with zero Lelong number along Z, showing that Z ∩ K(ξ − t{Z}) ̸= ∅.
    On the other hand we have vol(ξ − t{Z}) ↘ 0 as t ↗ νmax (ξ, Z). If this were
not the case, then ξ − νmax (ξ, Z){Z} would have to be a big class. For small ε > 0,
ξ − (νmax + ε)(ξ, Z){Z} must also be big, and contains a Kähler current Q with gentle
analytic singularities. Choosing ε so that νmax + ε ∈ Q, then Q + (νmax + ε)[Z] is an
element in Ω(X, ξ) with Lelong number larger than νmax (ξ, Z) along Z, a contradiction.
    Now for any c ∈ (0, νmax (ξ, Z)), we deduce from the above that
                                                Z c
                    vol(ξ) − vol(ξ − c{Z}) = n      volX|Z (ξ − t{Z}) dt,
                                                      0

where the integrand is continuous by [37, Corollary 4.11]. Sending c ↗ νmax (ξ, Z) we
conclude the second point.


3     Transcendental Okounkov bodies
The big case. Let ξ a big (1, 1)-class on X. The goal of this paragraph is to attach
natural convex bodies (compact convex sets with non-empty interior) ∆(ξ) ⊂ Rn to ξ,
which will be called the Okounkov bodies of ξ. One starts with a flag

                     Y• = (X = Y0 ⊃ Y1 ⊃ · · · ⊃ Yn−1 ⊃ Yn = {q}),

where Yi is a smooth connected complex submanifold of X with codimension i. We call
such a flag a smooth flag on X centered at q.
    However, it is possible that X might not contain any proper submanifolds of positive
dimension, let alone flags. As we have pointed out in the introduction, an easy remedy
for this issue is to replace X by a smooth model X ′ and then one can construct a flag
Y• on X ′ . So after possibly modifying X and pulling back ξ, in what follows we always
assume that X contains a flag Y• , which is centered at the point q ∈ Yn .

                                               11
  Next, using Y• we shall associate an Okounkov body ∆(ξ) = ∆Y• (ξ) ⊂ Rn with ξ.
The construction is essentially the same as in [25], apart from some minor modifications.
  Following [35, 25], we define a valuative map ν : A(X, ξ, q) → Qn≥0 by
                         T 7→ ν(T ) = νY• (T ) = (ν1 (T ), . . . , νn (T ))
as follows. First, set
                                       ν1 (T ) := ν(T, Y1 ).
Since the generic Lelong number of T1 := (T − ν1 (T )[Y1 ]) along Y1 is zero and this
current has analytic singularities near q, its potential is not identically −∞ on Y1 , hence
T1 := (T − ν1 (T )[Y1 ])|Y1 is a positive current on Y1 , with analytic singularities near q.
    Next put
                                        ν2 (T ) := ν(T1 , Y2 ),
and continue in this manner to define all the remaining values νi (T ) ∈ Q≥0 .
   Note that Ω(X, ξ) ⊆ A(X, ξ, q). So the map ν is also defined on Ω(X, ξ). Consider
the image sets
                            ν(Ω(X, ξ)) and ν(A(X, ξ, q)).
These two are bounded sets in Qn≥0 , since all the Lelong numbers appearing in the above
construction are bounded by cohomological constants (see e.g. [25, Lemma 4.3]). More-
over, they are convex sets in Qn≥0 , since ν(tT1 + (1 − t)T2 ) = tν(T1 ) + (1 − t)ν(T2 ) for
T1 , T2 in Ω(X, ξ) (or in A(X, ξ, q)) and t ∈ [0, 1] ∩ Q.
     The following lemma plays a key role in this paper.
Lemma 3.1. For any T ∈ A(X, ξ, q), one can find a sequence Tk ∈ Ω(X, ξ) such that
ν(Tk ) → ν(T ) in Qn≥0 .
Proof. First, we might as well assume that T is a Kähler current. Indeed, one can take
S ∈ Ω(X, ξ) and let Tε := (1 − ε)T + εS for ε ∈ (0, 1) ∩ Q. So Tε is a Kähler current in
A(X, ξ, q) and ν(Tε ) = (1 − ε)ν(T ) + εν(S) can be made  Parbitrarily close to ν(T ).
                                        c                   r     2
      Next assume that T = θ + dd φ with φ = c log i=1 |gi | + O(1) near q, where
g1 , . . . , gr ∈ OX,q and c ∈ Q≥0 . Let J ⊆ OX,q be the ideal generated by g1 , . . . , gr . Up
to rescaling the class ξ we will assume that c = 1 for simplicity. Let Tk P= θ + ddc φk be
the sequence given by Theorem 2.8. Near q, one can write φk = k1 log l |gkl |2 + O(1)
for some local generators {gkl }l of I(kφ)q . Let m := min{n − 1, r − 1}. Then by the
Briançon–Skoda theorem (see [23, Theorem 11.17]), the equality of ideals
                                I((k + m)φ)q = J k · I(mφ)q
holds at qPfor any large k ∈ N. Let {hj } be a set of generators of I(mφ)q and put
ψ := log j |hj |2 , which is a qpsh function defined near q. Then the above equality
implies that
                                     k          1
                           φk+m =        φ+         ψ + O(1)
                                   k+m       k+m
holds near q. So sending k → ∞ we find that ν(Tk ) → ν(T ), as desired.
   Consequently, we are led to the following definition (cf. [25, Definition 4.12]).
Definition 3.2. The Okounkov body ∆(ξ) = ∆Y• (ξ) of ξ is defined to be
                     ∆(ξ) := ν(Ω(X, ξ)) = ν(A(X, ξ)) = ν(A(X, ξ, q)).
Here the closure is taken with respect to the Euclidean topology of Rn .

                                                12
    As in [25, Proposition 4.13], we have the following properties for ∆(ξ):
Proposition 3.3. The following properties hold:
   1. For λ ∈ R>0 , one has ∆(λξ) = λ∆(ξ);
   2. ∆(ξ1 ) + ∆(ξ2 ) ⊆ ∆(ξ1 + ξ2 ) for two big classes ξ1 and ξ2 ;
              T
   3. ∆(ξ) = ε>0 ∆(ξ + ε{ω}) for any Kähler form ω on X.
Proof. Point (1) is clear when λ ∈ Q>0 . If λ ∈ R>0 , it suffices to observe that, for any
T ∈ Ω(λξ), one can find a sequence Ti ∈ Ω(X, ξ) so that λν(Ti ) → ν(T ). Point (2) is
also clear. So it remains to argue (3).                                            √
    First, it is easy to see that ∆(ξ) ⊆ ∆(ξ + ε{ω}). On the other hand, (1 + ε)ξ −
(ξ
√ +n ε{ω}) is a big class for small ε > 0. So from (1) and (2) we have that (1 +
   ε) volRn (∆(ξ)) ≥ volRn (∆(ξ + ε{ω})). Thus, we get that
                              volRn (∆(ξ)) = lim volRn (∆(ξ + ε{ω})).
                                                ε→0
               T
So ∆(ξ) = ε>0 ∆(ξ + ε{ω}) follows (here we used that ∆(ξ) is a convex body, by
Proposition 3.4 below).
Proposition 3.4. When ξ is big, ∆(ξ) is a convex body in Rn , so volRn (∆(ξ)) > 0.
    This result is also from [25]. Below we give a slightly different proof.
Proof. We need to show that ∆(ξ) has non-empty interior. Since ξ can be written as the
sum of a Kähler class and a big class, it suffices to show that ∆(ξ) has non-empty interior
when ξ is Kähler.
    So assume that ξ is Kähler. Fix a Kähler form ω ∈ ξ. We will argue that ∆(ξ)
contains a small simplex near the origin. Clearly, ∆(ξ) contains the origin. Applying
[27, Lemma 2.1(i)] to Yi , we can find qpsh functions ψi on X for 1 ≤ i ≤ n so that
ψi has analytic singularities precisely along Yi . Choosing ε > 0 small enough so that
Ti := ω + εddc ψi are all elements in Ω(X, ξ). Then one has ν(Ti ) = εei ∈ Rn≥0 , so that
∆(ξ) contains a simplex.
    The following result could be of independent interest.
Proposition 3.5. The map ξ 7→ ∆(ξ) from the big cone of X to Rn is continuous with
respect to the Hausdorff topology in Rn .
Proof. Choose smooth (1, 1)-forms η1 , . . . , ηr on X so that the {ηi } form a basis of
H 1,1 (X, R). For any two big classes ξ, ξ ′ ∈ H 1,1 (X, R) write ξ = (a1 , . . . , ar ) and
ξ ′ = (a′1 , . . . , a′r ) using this basis and let ∥ξ − ξ ′ ∥ := maxi |ai − a′i |. We wish to argue that
the Hausdorff distance between ∆(ξ) and ∆(ξ ′ ) tends to zero as ∥ξ − ξ ′ ∥ → 0.
      Fix a Kähler current T ∈ ξ and assume that T ≥ ω for some Kähler form                P ω′ on X.
                                                                                     ′ :=
Pick C > 1 so that −Cω ≤ ηi ≤ Cω holds for all 1 ≤ i ≤ r. Then T                          T + i (ai − ai )ηi
                                  ′                   ′           −1
is a Kähler current in ξ as long as ∥ξ − ξ ∥ < (Cr) . Moreover, we see that (1 + ∥ξ −
ξ ′ ∥1/2 )ξ − ξ ′ is big as well when ∥ξ − ξ ′ ∥ < (Cr)−2 , since (1 + ∥ξ − ξ ′ ∥1/2 )T − T ′ is a
Kähler current in that class. This implies that ∆(ξ ′ ) ⊆ (1 + ∥ξ − ξ ′ ∥1/2 )∆(ξ) as long
as ∥ξ − ξ ′ ∥ < (Cr)−2 . On the other hand, observe that (1 + ∥ξ − ξ ′ ∥1/2 )T ′ − T is a
Kähler current when ∥ξ − ξ ′ ∥ < (2Cr)−2 , so that ∆(ξ) ⊆ (1 + ∥ξ − ξ ′ ∥1/2 )∆(ξ ′ ) when
∥ξ − ξ ′ ∥ < (2Cr)−2 .
      The above discussion easily implies that the Hausdorff distance between ∆(ξ) and
∆(ξ ′ ) tends to zero as ∥ξ − ξ ′ ∥ → 0.

                                                      13
The pseudoeffective case. In case ξ is only pseudoeffective and not big, there are
different ways to associate a compact convex set with ξ [18]. In [25, Definition 4.23] Deng
suggests the definition below that we will follow in this work. For a Kähler form ω, let
                                         \
                                 ∆(ξ) :=    ∆(ξ + ε{ω}).                               (3.1)
                                          ε>0

Due to Proposition 3.3, the above definition does not depend on the choice of ω. Another
natural choice is
                                    ˜
                                    ∆(ξ) := ν(A(X, ξ)).
Since A(X, ξ) ⊂ A(X, ξ + ε{ω}) we obtain that ∆(ξ) ˜                             ˜
                                                          ⊂ ∆(ξ). Notice that ∆(ξ)    might
be empty.
    In case ξ is pseudoeffective and non-big, we will establish later that volRn ∆(ξ) = 0 =
                                      ˜
vol(ξ), so this will imply that volRn ∆(ξ) = 0 = vol(ξ).
    In particular, Theorem 1.1 will remain valid, regardless what definition one chooses
for the convex compact sets associated to pseudoeffective (non-big) classes.

The conjectured volume identity. Let us return to a big class ξ. When ξ is in the
Néron–Severi space it was shown in [25] that vol(ξ) = n! volRn (∆(ξ)). For a transcenden-
tal big class ξ, following [25, Conjecture 1.4], we expect the same:

Property An . Assume that dim X = n and ξ is big. Then vol(ξ) = n! volRn (∆(ξ)).

    Note that the ensemble of Property An ’s for all n ≥ 1 is equivalent to Theorem 1.1.
    It is easy to establish this when n = 1. We recall its proof for the reader’s convenience.

Lemma 3.6. Property A1 holds.

Proof. When Rdim X = 1, H 1,1 (X, R) ∼ = H 2 (X, R) ∼= R. A class ξ ∈ H 1,1 (X, R) is Kähler
if and only if X ξ > 0. Moreover, in this setting every big class ξ = {θ} is a Kähler class,
and a flag is simplyRa choice of point Y1 = X ⊃ Y0 = {q}.
    For any t ∈ (0, X θ), {θ} − t{q} the class is Kähler, which then contains a smooth
                                                                                     R
Kähler form ωt . Then ωt +t[q] ∈ Ω(X, {θ}) and it Rhas Lelong number t at q. So [0, X θ] ⊆
∆({θ}).R On the other hand, one has ν(T, q) ≤ X θ for any T ∈ Ω(X, {θ}),      R otherwise
{θ} − X θ{q} is a Kähler class, which is absurd. So we have ∆({θ}) = [0, X θ].
   The following sections aim to prove Property An for higher dimensions. It is notable
that, by using the divisorial Zariski decomposition for surfaces, it was shown in [25,
Theorem 1.8] that Property A2 holds as well.


4     Lifting the flags
In this section, we fix a smooth flag Y• = (Y0 ⊃ · · · ⊃ Yn ) on X.
    If π : Y → X is a proper bimeromorphic morphism of complex manifolds and Z is
an analytic set in X not contained in the exceptional locus E, then we define the strict
transform of Z in Y as the closure of π −1 Z \ π −1 E in Y . This is an analytic set in Y by
[22, Corollary 5.4]. When π is a modification, this coincides with the notion defined in
[10, Section 3, strict transforms] by [10, Remark 3.15].



                                                14
Definition 4.1. Let π : Z → X be a proper bimeromorphic morphism with Z being a
compact Kähler manifold. We say that a smooth flag W• = (W0 ⊃ · · · ⊃ Wn ) is a lifting
of Y• to Z if the restriction of π to Wi → Yi is defined and bimeromorphic.

Lemma 4.2. Let π : Z → X be a proper bimeromorphic morphism with Z being a Kähler
manifold. Assume that there is a lifting W• = (W0 ⊃ · · · ⊃ Wn ) of Y• to Z. Then there
is a matrix g ∈ SLn (Z) of the form I + N with N being strictly upper triangular (namely,
all entries on and below the diagonal are 0) such that for any T ∈ A(X), we have

                                       νW• (π ∗ T ) = νY• (T )g.

    Here the valuations of currents are considered as row vectors. For simplicity, we will
also say (W• , g) is a lifting of Y• to Z.
    Observe that matrices of the form I +N are exactly the automorphisms of the ordered
Abelian group Zn with respect to the lexicographic order. So this result can be seen as
a generalization of [15, Theorem 2.9].
Proof. We take induction on n = dim X. The case n = 1 is trivial. In general, assume
that the result is proved when dim X = n − 1.
   For simplicity, we write ν = νY• and ν ′ = νW• . Let µ (resp. µ′ ) be the valuation of
currents defined by Y1 ⊃ · · · ⊃ Yn (resp. W1 ⊃ · · · ⊃ Wn ). Then we need to show that
                          ′ ∗
                          ν (π T )1 µ′ ((π ∗ T − ν ′ (π ∗ T )1 [W1 ])|W1 )
                                                                           


equals                                                         
                                 ν(T )1 µ((T − ν(T )1 [Y1 ]))|Y1 g.
Clearly
                                      ν ′ (π ∗ T )1 = ν(T )1 =: c.
By the inductive hypothesis, we can find h ∈ SLn−1 (Z) of the form I plus a strictly upper
triangular matrix such that

                           µ′ (Π∗ (T − c[Y1 ])|Y1 ) = µ((T − c[Y1 ])|Y1 )h,                       (4.1)

where Π : W1 → Y1 is the restriction of π. Observe that

                Π∗ (T − c[Y1 ])|Y1 = (π ∗ (T − c[Y1 ]))|W1
                                   = (π ∗ T − c[W1 ])|W1 + c(π ∗ [Y1 ] − [W1 ])|W1 .

So
          µ′ (Π∗ (T − c[Y1 ])|Y1 ) = µ′ ((π ∗ T − c[W1 ])|W1 ) + cµ′ ((π ∗ [Y1 ] − [W1 ])|W1 ).
Combining the above with (4.1), we see that the following choice of g satisfies the re-
quirements of the lemma:

                                1 −µ′ ((π ∗ [Y1 ] − [W1 ])|W1 )
                                                               
                         g :=                                     .
                                0                h



Theorem 4.3. Assume that π : Z → X is a modification of X, then there is a modifica-
tion π ′ : Z ′ → Z such that the flag Y• admits a lifting W• to Z ′ .

                                                   15
    By Hironaka’s Chow lemma [29, Corollary 2], we can relax the assumption to that π
is a proper bimeromorphic morphism from a reduced complex space Z.
    When X is projective, this result is already known, see [15, Theorem 2.9] for example.
    The proof below relies on the embedded resolutions studied in [10] and [46]. Let Z be
an analytic subset of a compact complex manifold M1 , that in turn is a submanifold of
a compact complex submanifold M2 . Due to [46, Theorem 2.0.2(4)] there exist canonical
desingularizations σ1 : M1′ → M1 and σ2 : M2′ → M2 of Z inside M1 and M2 respec-
tively, so that a canonical embedding M1′ ,→ M2′ exists and makes the following diagram
commute:
                                      M1′         M2′
                                         σ1         σ2                               (4.2)

                                         M1          M2 .
Moreover, M1′ ,→ M2′ maps the (desingularized) strict transforms of Z onto each other.
Proof. We begin by setting W0 = Z. We will construct Wi inductively for each i. Assume
that for 0 ≤ i < n a smooth partial flag W0 ⊃ · · · ⊃ Wi has been constructed on a
modification πi : Zi → Z so that π ◦ πi restricts to bimeromorphic morphisms Wj → Yj
for each j = 0, . . . , i.
    By Zariski’s main theorem, Wi → Yi is an isomorphism outside a codimension 2 subset
of Yi . We let Wi+1 be the strict transform of Yi+1 in Wi . The problem is that Wi+1 is not
necessarily smooth.
    We will further modify Zi and lift W1 , . . . , Wi+1 in order to make the flag smooth.
Take the embedded resolution of (Wj , Wi+1 ), say Wj′ → Wj for each j = 0, . . . , i.
    Due to (4.2), we have canonical embeddings Wi′ ,→ Wi−1     ′
                                                                  ,→ · · · ,→ W0′ making the
following diagram commutative:

                           Wi′             ′
                                         Wi−1         ···        W0′
                                                       ..
                                                        .
                            Wi           Wi−1         ···        W0
      ′
Let Wi+1 be the strict transform of Wi+1 in Wi′ . It suffices to define πi+1 as the morphism
W0′ → Zi → Z and replace W0 ⊃ · · · ⊃ Wi+1 by W0′ ⊃ · · · ⊃ Wi+1   ′
                                                                      .
   As a consequence, we have the following useful approximation result.
Proposition 4.4. Let π : Z → X be a modification of X and ξ be a big class on X.
Assume that Y• admits a lifting (W• , g) to Z. For any T ∈ Ω(Z, π ∗ ξ) we can find Kähler
currents Tk ∈ A(X, ξ) such that
  1. limk→∞ νY• (Tk ) = νW• (T )g −1 ;

  2. Tk ⪯ π∗ T .
   In particular, it follows that

                                 ∆W• (Z, π ∗ ξ) = ∆Y• (X, ξ)g.

This is the transcendental generalization of the birational invariance of the classical Ok-
ounkov bodies.

                                                16
Proof. By Theorem 4.3 there exists a modification π ′ : Z ′ → Z such that
    (i) π ′∗ T = β + [D], where β is a smooth semipositive (1, 1)-form on Z ′ and D is an
        effective Q-divisor;
 (ii) Y• admits a lifting (V• , h) to Z ′ .
   Observe that (V• , g −1 h) is a lifting of Y• to Z ′ .
   Note that π ′ is a composition of blowups with smooth centers. By the proof of [27,
Theorem 3.5], one can find an effective exceptional divisor E on Z ′ and a smooth (1, 1)-
form η in {E} such that π ′∗ T − εη is a Kähler current for any small ε > 0. This implies
that β − εη is a smooth Kähler form. Let us put for k ≫ 1
                            βk := β − k −1 η and Dk := D + k −1 E.
Then βk +[Dk ] ∈ (π◦π ′ )∗ ξ and by Lemma 2.11 one has Tk := (π◦π ′ )∗ (βk +[Dk ]) ∈ A(X, ξ).
  We compute
             νY• (Tk ) = νV• (βk + k −1 [E] + [D])h
                       = νV• (π ′∗ T )h + k −1 νV• ([E])h = νW• (T )g + k −1 νV• ([E])h.
Letting k → ∞ we conclude the first point. The second point is clear from the construc-
tion of Tk .


5      Partial Okounkov bodies
For this section let ξ be a big class on X. Fix a smooth flag Y• = (Y0 ⊃ · · · ⊃ Yn ). We
will show that Property An holds with the help of partial Okounkov bodies, introduced
and studied recently in [52] in case of big line bundles.
Definition 5.1. For R ∈ Ω(X, ξ), we set
                            Ω(X, ξ; R) := {T ∈ Ω(X, ξ) : T ⪯ R} .
The partial Okounkov body of R is defined as the following closed convex subset of Rn≥0 :
                           ∆(ξ; R) = ∆Y• (ξ; R) := νY• (Ω(X, ξ; R)).
     We will fix R ∈ Ω(X, ξ) throughout this section.
Proposition 5.2. The partial Okounkov body ∆(ξ; R) is a convex body in Rn≥0 .
Proof. Since R is a Kähler current, we may fix a small ε > 0 such that R − εω is still a
Kähler current. This implies that ∆(ξ; R) contains the set ν(R) + ε∆({ω}). As we have
seen in the proof of Proposition 3.4, the body ∆({ω}) contains a simplex, hence so does
∆(ξ; R).
Example 5.3. When R = [D] + β, where D is a Q-divisor on X and β ∈ Z+ (X) is a
current with bounded potentials, we have
                            ∆Y• (ξ; R) = ∆Y• (ξ − {D}) + νY• ([D]).
Indeed, suppose that T ∈ Ω(X, ξ − {D}), then T + [D] ∈ Ω(X, ξ; R), so
                            ∆Y• (ξ; R) ⊃ ∆Y• (ξ − {D}) + νY• ([D]).
On the other hand, if T ∈ Ω(X, ξ; R), then T − [D] ∈ A(X, ξ − {D}), due to Lemma 2.5.
It follows from Lemma 3.1 that ν(T ) ∈ ∆Y• (ξ − {D}) + νY• ([D]).

                                                 17
   Let us put
                           A(X, ξ; R) := {T ∈ A(X, ξ) : T ⪯ R}
It is helpful to know the following equivalent formulation of ∆(ξ; R).
Lemma 5.4. One has
                                  ∆(ξ; R) = ν(A(X, ξ; R)).
Proof. The proof uses similar strategy as in Lemma 3.1. It suffices to argue that ν(G) ∈
∆(ξ; R) for any G ∈ A(X, ξ; R). We might as well assume that G is a Kähler current,
otherwise one can replace G by (1 − ε)G + εR.
     Write R = θ + ddc u and G = θ + ddc φ, with φ ≤ u. Since they are both Kähler
currents, we can assume that R ≥ ω and G ≥ ω. For any sufficiently small rational
number ε > 0, put uε := (1 + ε)u and φε := φ + εu. Then one has Rε := θ + ddc uε ≥ 21 ω
and Gε := θ + ddc φε ≥ 21 ω. Let Gε,k := θ + ddc φε,k be the regularization sequence
of Gε given in Theorem 2.8, which are Kähler currents with analytic singularities of
type (I(kφε ), k1 ). Since I(kφε ) ⊆ I(kuε ) and uε has analytic singularities, we can apply
                                                                                 k
Briançon–Skoda theorem as in the proof of Lemma 3.1 to see that φε,k+m ≤ k+m       uε +O(1)
holds on X, where m ∈ N is independent of k (but it may depend on ε). Then for all
sufficiently large k, one has φε,k ≤ u+O(1), i.e., Gε,k ∈ Ω(ξ, R). Moreover, by the proof of
Lemma 3.1, νY• (Gε ) = limk→∞ νY• (Gε,k ), since Gε has analytic singularities; meanwhile,
it is clear that νY• (G) = limε→0 νY• (Gε ). So the desired assertion follows.
Proposition 5.5. One can find an increasing sequence Ri ∈ Ω(X, ξ) such that
  1. E+ (Ri ) = EnK (ξ);
     R
  2. X Rin ↗ vol(ξ);
              S
  3. ∆(ξ) = i ∆(ξ; Ri ), so that volRn (∆(ξ; Ri )) ↗ volRn (∆(ξ)).
Proof. Since ν(Ω(X, ξ)) ⊆ Qn≥0 is a countable set, we can write ν(Ω(X, ξ)) = {a1 , a2 , . . . }.
RPick nTi ∈ Ω(X, ξ) such that ν(Ti ) = ai and also pick a sequence Gi ∈ Ω(X, ξ) such that
  X
     Gi → vol(ξ). Choose R0 ∈ Ω(X, ξ) such that E+ (R0 ) = EnK (ξ). Then applying
 Lemma 2.9 repeatedly, we choose Ri ∈ Ω(X, ξ) so that it is less singular than Ti , Gi and
 Ri−1 . So Ri is an increasing sequence, which clearly satisfies (1) and (3). That (2) holds
 follows from the monotonicity of Monge–Ampère masses, see [5, Theorem 1.16] or [50,
 Theorem 1.2].
Lemma 5.6. Let R ∈ Ω(X, ξ). Take a modification π : Z → X such that the flag Y•
admits a lifting (W• , g) to Z and π ∗ R = β + [D], where β is a smooth semipositive form
on Z and D is an effective Q-divisor. Then

                            ∆Y• (ξ; R)g = ∆W• ({β}) + νW• ([D]).                          (5.1)

Proof. For any T ∈ Ω(X, ξ; R), by Lemma 2.5 π ∗ T −[D] is a positive current with analytic
singularities in {β}. So one has

            νW• (π ∗ T ) = νW• (π ∗ T − [D]) + νW• ([D]) ∈ ∆W• ({β}) + νW• ([D]).

Therefore, νY• (T ) ∈ ∆W• ({β}) + νW• ([D]) g −1 , implying that
                                               

                          ∆Y• (ξ; R) ⊆ ∆W• ({β}) + νW• ([D]) g −1 .
                                                                


                                              18
    On the other hand, for any Kähler current S ∈ Ω(Z, {β}), note that S + [D] belongs
to Ω(Z, π ∗ ξ) and is more singular than π ∗ R.
    By Proposition 4.4, there exist Kähler currents Tk ∈ A(X, ξ) s.t. limk→∞ νY• (Tk ) =
νV• (S + [D])g −1 and Tk ⪯ R.
    It follows from Lemma 5.4 that νW• (S + [D]) ∈ ∆Y• (ξ; R)g, finishing the proof of
(5.1):
                          ∆W• ({β}) + νW• ([D]) g −1 ⊆ ∆Y• (ξ; R).
                                                



     We hope to show that partial Okounkov bodies have the following property:
Property Bn . Assume that dim X = n and ξ is big. For any R ∈ Ω(X, ξ) one has
                           Z
                              Rn = n! volRn (∆(ξ; R)).
                                  X

Lemma 5.7. Property An and Property Bn are equivalent.
Proof. That Property Bn implies Property An is immediate thanks to Proposition 5.5.
Let us prove the other direction.
   Fix R ∈ Ω(X, ξ). By Theorem 4.3, there is a modification π : Z → X such that
    (i) π ∗ R = β + [D], where β is a smooth semipositive form on Z and D is an effective
        Q-divisor;
 (ii) The flag Y• admits a lifting (W• , g) to Z.
                                                 
By Lemma 5.6, ∆Y• (ξ; R)g = ∆W• ({β}) + νW• ([D]) . Since det g = 1, we obtain that:

              volRn (∆Y• (ξ; R)) = volRn (∆Y• (ξ; R)) · det g = volRn (∆W• ({β}))
                                                                   Z
                                                                 1
                                                              =        βn
                                                                n! Z
                                                                   Z
                                                                 1
                                                              =        Rn .
                                                                n! X


     We shall see in §7 that Property Bn holds for all n ≥ 1, and so does An .


6      Extension of Kähler currents
In order to prove Property An , the natural idea is to argue by induction on n. Then we
need to investigate the Kähler currents on submanifolds and see if they can be extended to
Kähler currents on the ambient space. This motivates us to prove the following extension
theorem, generalizing [19, Theorem 1.1].
Theorem 6.1. (=Theorem 1.3) Let V ⊆ X be a connected positive dimensional compact
complex submanifold of (X, ω). Let T = ω|V + ddc φ be a Kähler current on V . Assume
that eφ is a Hölder continuous function on V . Then one can find a Kähler current
T̃ = ω + ddc φ̃ on X such that φ̃|V = φ, i.e., T̃ extends T . Moreover, φ̃ is continuous
on X \ V and eφ̃ is Hölder continuous on X. In addition, if φ has analytic singularities,
then so does φ̃.

                                              19
Proof. Thanks to [27, Lemma 2.1], we can find a qpsh potential F on X, such that
F |V ≡ −∞, F is smooth on X \ V and ω + ddc F is a Kähler current with analytic
singularities precisely along V . Moreover, eF : X → R≥0 is a Hölder continuous function.
    Choose ε > 0 small enough so that

                          ω|V + ddc φ ≥ 3εω|V and ω + ddc F ≥ 3εω.

   We also choose finitely many open coordinate balls {Wj }1≤j≤r covering V , such that on
each Wj there are local coordinates (z1 , . . . , zn ) so that V ∩ Wj = {z1 = · · · = zn−k = 0},
where k = dim V . Write z = (z1 , . . . , zn−k ) and z ′ = (zn−k+1 , . . . , zn ).
   Assume that eφ is α-Hölder continuous for some α > 0. Due to [27, Lemma 2.1(i)] we
can rescale F to arrange the existence of c ∈ (0, α) ∩ Q such that on Wj we have
                                               n−k
                                          c    X
                                   F (z) = log     |zi |2 + O(1).                           (6.1)
                                          2    i=1

   We define a function φj on Wj by
                                             ′           ′
                    φj (z, z ′ ) := log(eφ(z ) + eF (z,z ) ) + A · dist((z, z ′ ), V )2 ,   (6.2)

where dist is the Riemannian distance. After shrinking Wj ’s slightly, still preserving
V ⊂ ∪j Wj , we can fix A > 1 sufficiently large so that φ(z ′ ) + A · dist((z, z ′ ), V )2 and
F (z, z ′ ) + A · dist((z, z ′ ), V )2 are (1 − 2ε)ω-psh (see [40, §2]). Then

                                           ω + ddc φj ≥ 2εω

holds on Wj for all j, due to [22, Theorem I.4.16].
    From (6.2) one sees that φj is continuous on Wj \ V and φj |V = φ. If in addition
φ has analytic singularities, then due to Lemma 2.4, the potential φj has local analytic
singularities on Wj (in the sense of Definition 2.2), as φj has the same singularity type
as max(φ(z ′ ), F (z, z ′ )).
    Next we need to fix slightly smaller open coordinate balls Wj′ ⋐ Uj ⋐ Tj ⋐ Wj such
that ∪j Wj′ still covers V .
    Let fj ∈ C ∞ (Wj ), fj ≥ 0, compactly supported such that supp fj ⊂ Wj′ c and fj > 1
in a neighborhood of Tj \ Uj .
    Let η > 0 small, so that ddc ηfj ≤ εω. We introduce

                              φ̃j := φj − ηfj ∈ PSH(Wj , (1 − ε)ω).

   Let W := ∪j Tj and for x ∈ W we introduce the function

                                          ψ(x) := max φ̃l (x).                              (6.3)
                                                     x∈Tl


We will show that ψ ∈ PSH(G, (1 − ε)ω) for some neighborhood G ⊂ W of V , moreover
ψ|V = φ and ψ is continuous on G \ V .
    For any x ∈ Wj′ let Ix ⊂ {1, . . . , r} be the collection of indices l such that x ∈ Tl \ Ul .
    Fixing x ∈ Wj′ , there exists an open coordinate ball Bx ⊂ Wj′ , centered at x such that
for all y ∈ Bx we have Iy ⊂ Ix .
    After shrinking Bx further, we can assume that φl − η ≥ φ̃l on Bx , for any l ∈ Ix .
Indeed, this follows from the fact that fl > 1 in a neighborhood of Tl \ Ul , containing x.

                                                    20
   In case x ∈ V ∩ Wj′ , due to Lemma 6.2, we can shrink Bx ⊂ Wj′ further so that

                    φ̃j (z) = φj (z) > φl (z) − η > φ̃l (z), z ∈ Bx , l ∈ Ix .             (6.4)

    We denote by Jx ⊂ {1, . . . , r} \ Ix the collection of indices l such that Tl ∩ Bx is
non-empty. We claim that Bx ⊂ Tl for any l ∈ Jx . If this were not the case then there
would exist y ∈ Bx such that y ∈ ∂Tl ⊂ Tl \ Ul . Hence, l ∈ Iy ⊂ Ix , a contradiction. As
a result, Jx is also the subset of indices l in {1, . . . , r} \ Ix such that Bx ⊂ Tl . This will
be used crucially in (6.5) below.
    Let Bx1 , . . . , Bxp be a covering of V with xi ∈ Wj′i ∩ V . We take
                                                [
                                           G :=    Bxj .
                                                  j

   Clearly, ψ ≥ φ̃j = φj on Wj′ . As φl − ηfl ≤ φ on V ∩ Tj for all l, we get ψ = φ on V .
   Revisiting (6.3), due to (6.4), on each Bxi we have
                                                                           
           ψ|Bxi := max φ̃ji |Bxi , max φ̃k |Bxi = max φji |Bxi , max φ̃k |Bxi .     (6.5)
                                     k∈Jxi                               k∈Jxi

Since the right-hand side above is clearly a (1 − ε)ω-psh function on Bxi , we get that
ψ ∈ PSH(G, (1 − ε)ω). Moreover, ψ|V = φ and ψ is continuous on G \ V .
    After slightly shrinking G, we can assume that ψ is defined and continuous in a
neighborhood of ∂G. Let k > 0 and introduce φ̃ := max(ψ, F + k) on G and φ̃ := F + k
on X \ G. For k big enough φ̃ ∈ PSH(X, (1 − ε)ω).
    If in addition φ has analytic singularities, then thanks to Lemma 2.4 so does φ̃,
since due to (6.5) the potential φ̃ is locally the maximum of finitely many potentials
with analytic singularities. Note also that the maximum operation preserves exponential
Hölder continuity, so all the potentials involved in the proof are exponentially Hölder
continuous. Therefore, the potential φ̃ satisfies all the required properties.
   As promised in the above argument, we deliver the following key lemma:
Lemma 6.2. With the notation of the above proof, the following property holds: for any
1 ≤ i, j ≤ r, any point p ∈ Wi ∩ Wj ∩ V and η > 0, there is an open neighborhood of p
on which φj ≥ φi − η holds.
Proof. Let pi : Wi → V and pj : Wj → V be the coordinate projections onto V in each
respective chart. To show that φj ≥ φi − η in a neighborhood of p, it is enough to show
that in a neighborhood of p we have

                        eφ(pj (x)) + eF (x) ≥ e−η eφ(pi (x)) + eF (x) .
                                                                     

This in turn is equivalent to

                            1 − e−η eF (x) ≥ e−η eφ(pi (x)) − eφ(pj (x)) .
                                   
                                                                                           (6.6)

Since e−η < 1, we claim that in fact the following slightly stronger inequality holds, in a
neighborhood of p:
                         1 − e−η eF (x) ≥ e−η eφ(pi (x)) − eφ(pj (x)) .
                                                                    

   Due to (6.1) there exists D > 0 such that

                             1 − e−η eF (x) ≥ D · dist(x, V )c
                                    


                                                21
for all x ∈ Wi ∩ Wj \ V . As a result, it is enough to argue that in a neighborhood of p
we have:
                        D · dist(x, V )c ≥ e−η eφ(pj (x)) − eφ(pi (x)) .
                                                                      
                                                                                   (6.7)
This follows from the α-Hölder continuity of the expression on the right-hand side and
its vanishing on V (recall that 0 < c < α). So the proof is complete.

Remark 6.3. The key inequality (6.6) does not holdP∞when     eφ is not continuous. Here is
                                                          1
a counterexample: let V = C, X = C . Let φ = n=1 n2 log |z − 1/n|2 , a psh function
                                       2

on C (discontinuous at z = 0). Let pi (z, w) = z and pj (z, w) = z + w. Then one asks if
                                           ∞                              ∞
                                                               2/n2                                 2
                                           Y                              Y
                             c        −η
                 (1 − η)|w| ≥ e                  |z − 1/n|            −         |z + w − 1/n|2/n
                                           n=1                            n=1

holds in a neighborhood of (0, 0). The answer is negative, unfortunately. One sees this
by taking the sequence of points (z = 0, w = 1/n). Therefore, if one wants to remove the
continuity assumption on eφ in our extension theorem, a different approach is needed.

    Finally, we state a direct consequence of Theorem 6.1 that is enough for our later use.

Theorem 6.4. Let V ⊊ X be a connected positive dimensional compact complex subman-
ifold of (X, ω). Let T = ω|V + ddc φ be a Kähler current with gentle analytic singularities
on V . Then one can find a Kähler current T̃ = ω + ddc φ̃ on X such that

    1. φ̃|V = φ, i.e., T̃ extends T ;

    2. φ̃ has analytic singularities on X;

    3. φ̃ is continuous on X \ V , so φ̃ and φ have the same singular locus.

Proof. Using Definition 2.6(1), we see that eφ ∈ C α (V ) for some α > 0. So the result
follows directly from Theorem 6.1.


7      The volume identity
Unless specified otherwise, in this section ξ is a big class on X and dim X = n. We also
fix a smooth flag Y• = (X = Y0 ⊃ · · · ⊃ Yn ) on X. Define

              νmin (ξ, Y1 ) :=     inf       ν(T, Y1 ),        νmax (ξ, Y1 ) :=      sup       ν(T, Y1 ).
                                 T ∈Ω(X,ξ)                                         T ∈Ω(X,ξ)


Lemma 7.1. One has νmin (ξ, Y1 ) < νmax (ξ, Y1 ). Moreover,

                             ν1 (Ω(X, ξ)) = [νmin (ξ, Y1 ), νmax (ξ, Y1 )],

where ν1 is the first component of the valuative map ν.

Proof. Pick any T ∈ Ω(X, ξ), then T − νmin (ξ, Y1 )[Y1 ] is a Kähler current, which implies
that ξ − νmin (ξ, Y1 ){Y1 } is a big class. So for small ε > 0, ξ − (νmin (ξ, Y1 ) + ε){Y1 } is
a big class as well. So there exists S ∈ Ω(X, ξ) with ν(S, Y1 ) ≥ νmin (ξ, Y1 ) + ε, giving
νmin (ξ, Y1 ) < νmax (ξ, Y1 ). The second assertion follows from the convexity of Ω(X, ξ).


                                                          22
Proposition 7.2. Assume that n ≥ 2. One has
                                      Z νmax (ξ,Y1 )
                         vol(ξ) = n                    volX|Y1 (ξ − t{Y1 }) dt.
                                       νmin (ξ,Y1 )

Proof. We first observe that for any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )), one has

                                   Y1 ∩ K(ξ − t{Y1 }) ̸= ∅.

In fact, by Lemma 7.1, for t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) lying in a dense subset, there
exists T ∈ Ω(X, ξ) with ν(T, Y1 ) = t. So T − t[Y1 ] is a Kähler current in ξ − t{Y1 } with
Y1 ⊈ E+ (T − t[Y1 ]).
    Clearly, vol(ξ) = vol(ξ − νmin (ξ, Y1 ){Y1 }). By the continuity of vol(·) [12, Proposition
4.7], one thus has
                        vol(ξ) = lim vol(ξ − (νmin (ξ, Y1 ) + ε){Y1 }).
                                   ε↘0

We can apply Theorem 2.14 to the big class ξ − (νmin (ξ, Y1 ) + ε){Y1 } to get
                                         Z νmax (ξ,Y1 )
                       vol(ξ) = lim n                       volX|Y1 (ξ − t{Y1 }) dt
                                ε↘0       νmin (ξ,Y1 )+ε
                                   Z νmax (ξ,Y1 )
                              =n                    volX|Y1 (ξ − t{Y1 }) dt
                                    νmin (ξ,Y1 )

as desired.
   Now for any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )), we look at the following restricted volume
                                                               Z
                     volX|Y1 (ξ − t{Y1 }) =           sup         T |n−1
                                                                     Y1
                                                      T ∈Ω(X,ξ−t{Y1 })   Y1


and the t-slice of the Okounkov body

                            ∆t (ξ) := {x ∈ Rn−1 : (t, x) ∈ ∆(ξ)}.

We shall prove that they are related in the following way (cf. [35, Corollary 4.25(i)]).

Property Cn . If n ≥ 2, then for any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )), one has

                        volX|Y1 (ξ − t{Y1 }) = (n − 1)! volRn−1 (∆t (ξ)).

Lemma 7.3. Assume that n ≥ 2. Property Cn implies Property An .

Proof. By Lemma 7.1, we can express volRn (∆(ξ)) as
                                           Z νmax (ξ,Y1 )
                        volRn (∆(ξ)) =                       volRn−1 (∆t (ξ)) dt.
                                             νmin (ξ,Y1 )

So we conclude from Proposition 7.2.




                                                      23
    Our goal is now to show that for n ≥ 2, Property Bn−1 implies Property Cn . Since we
already know by Lemma 5.7 that Property An and Property Bn are equivalent, this will
together with Lemma 7.3 complete the induction argument and thus prove Property An
for all n.
    Note that both maps t 7→ volX|Y1 (ξ − t{Y1 }) and t 7→ volRn−1 (∆t (ξ)) are continuous:
the former continuity is due to [37, Corollary 4.11] and the latter follows from the Brunn–
Minkowski inequality. Therefore, to establish Property Cn it is enough to show that

                          volX|Y1 (ξ − t{Y1 }) = (n − 1)! volRn−1 (∆t (ξ))

for all rational t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )).
    For t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q, we introduce t-slices of Ω(X, ξ) and A(X, ξ) and
show how they are connected to the t-slice of the Okounkov body:

                           Ωt (X, ξ) := {T ∈ Ω(X, ξ) : ν(T, Y1 ) = t},

                           At (X, ξ) := {T ∈ A(X, ξ) : ν(T, Y1 ) = t}.

Lemma 7.4. For any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q, one has

                           {t} × ∆t (ξ) = ν(Ωt (X, ξ)) = ν(At (X, ξ)).

Proof. It is clear that

                           ν(Ωt (X, ξ)) ⊆ ν(At (X, ξ)) ⊆ {t} × ∆t (ξ).

To finish we will argue that {t} × ∆t (ξ) ⊆ ν(Ωt (X, ξ)). Let a ∈ {t} × ∆t (ξ). Then there
exists a sequence Ti ∈ Ω(X, ξ) such that ν(Ti ) → a. So in particular, ti := ν(Ti , Y1 ) → t.
Pick S, G ∈ Ω(X, ξ) such that s := ν1 (S, Y1 ) < t and g := ν(G, Y1 ) > t. Define
                                 (
                                                  −t
                                   t
                                    t−s
                                      −s
                                         Ti + ttii−s S, if ti ≥ t,
                            Si := g−t
                                    i
                                               t−ti
                                   g−ti i
                                         T + g−ti G, if ti < t.

Then Si ∈ Ωt (X, ξ) for i ≫ 0 and limi ν(Si ) = limi ν(Ti ) = a, hence a ∈ ν(Ωt (X, ξ)).
   We are now ready to prove that Property Bn−1 implies Property Cn :

Lemma 7.5. Assume that n ≥ 2, then Property Bn−1 implies Property Cn .

Proof. Pick any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q. Put ξt := ξ − t{Y1 } for simplicity. It
suffices to show the following: there is an increasing sequence Ri ∈ Ω(X, ξt ) such that

 (1) E+ (Ri ) = EnK (ξt ) for all i;

 (2) Ri |Y1 has positive mass and Y1 Ri |n−1
                                  R
                                          Y1 ↗ volX|Y1 (ξt );

 (3) One has Y1 Ri |n−1
               R
                      Y1  = (n − 1)! volRn−1 (∆t,i ), where ∆t,i is the (n − 1)-dimensional
     partial Okounkov body ∆(ξt |Y1 ; Ri |Y1 ) of ξt |Y1 with respect to Ri |Y1 , which is defined
     using the truncated flag Y1 ⊃ Y2 ⊃ · · · ⊃ Yn ;

 (4) ∆t,i is an increasing sequence of (n − 1)-dimensional convex bodies contained in
     ∆t (ξ) such that volRn−1 (∆t,i ) ↗ volRn−1 (∆t (ξ)).

                                                24
    The above conditions would imply volX|Y1 (ξ − t{Y1 }) to equal (n − 1)! volRn−1 (∆t (ξ))
for any t ∈ (νmin (ξ, Y1 ), νmax (ξ, Y1 )) ∩ Q, hence proving Property Cn .
    To construct the sequence Ri , first note that the set νY• (Ωt (X, ξ)) ⊂ Qn≥0 is countable.
So one can write ν(Ωt (X, ξ)) = {a1 , a2 , . . . , ai , . . . } with ai ∈ Qn≥0 . Let a′i ∈ Qn−1≥0 be such
                 ′
that ai = (t, ai ). Pick Ti ∈ Ωt (ξ) so that νY• (Ti ) = ai . Fix RR0 ∈ Ω(X, ξt ) so that
E+ (R0 ) = EnK (ξt ). Also pick a sequence Gi ∈ Ω(X, ξt ) so that Y1 Gn−1               i    → volX|Y1 (ξt ).
Applying Lemma 2.9 inductively, we can find Ri ∈ Ω(X, ξt ) that is less singular than
Ti − t[Y1 ], Gi and Ri−1 . So Ri ∈ ξt is an increasing sequence of Kähler currents with
analytic singularities precisely on EnK (ξt ), showing (1). That (2) holds is due to [50,
Theorem 1.2] and (3) holds thanks to Property Bn−1 . It remains to argue (4).
    Let νY′ • : A(Y1 , ξt |Y1 ) → Qn−1  ≥0 denote the valuative map constructed using the flag
Y1 ⊃ Y2 ⊃ · · · ⊃ Yn on Y1 . Then one has that a′i ∈ νY′ • (A(Y1 , ξt |Y1 ; Ri |Y1 )), since (Ti −
t[Y1 ])|Y1 ∈ A(Y1 , ξt |Y1 ; Ri |Y1 ) and a′i = νY′ • ((Ti − t[Y1 ])|Y1 ). Thus, a′i ∈ ∆t,i by Lemma 5.4,
                                     S
which implies that ∆t (ξ) ⊆ i ∆t,i by Lemma 7.4.
    Next, we show that ∆t,i ⊆ ∆t (ξ) holds for all i. By Theorem 4.3, there are modifica-
tions πi : Xi → X such that
  (i) πi∗ Ri = βi +[Di ], where βi is a smooth semipositive form on Xi and Di is an effective
      Q-divisor on Xi ;
                                                  (i)
 (ii) The flag Y• admits a lifting (Y• , gi−1 ) to Xi .
                        (i)
    Note that Y1 is the strict transform of Y1 , and it is not contained in Di (as ν(Ri , Y1 ) =
0). By the Lelong–Poincaré formula, the restricted current [Di ]|Y (i) only has divisorial
                                                                                          1
components in its Siu decomposition. Let ν ′ (i) be the Qn−1
                                                         ≥0 -valued map determined by
                                                             Y•
            (i)                     (i)   (i)
the flag Y1 ⊃ · · · ⊃ Yn on Y1 . By Lemma 4.2, there is hi ∈ SLn−1 (Z) such that
                               νY′ (i) (πi∗ T )hi = νY′ • (T ) for all T ∈ Ω(Y1 , ξt |Y1 ).
                                     •


From the proof of Lemma 4.2, we see that hi is obtained from gi with the first row and
the first column removed.
   Now, for any T ∈ Ω(Y1 , ξt |Y1 ; Ri |Y1 ), Lemma 2.5 implies that Si := πi∗ T − [Di ]|Y (i) is a
                                                                                                         1
                              (i)
positive current on Y1 in the semipositive class {βi |Y (i) } and Si has analytic singularities.
                                                       1
   Fix a smooth Kähler form ωi on Xi . Then for any ε > 0, Si,ε := Si +εωi |Y (i) is a Kähler
                                                                                                  1
                  (i)
current on Y1            in the Kähler class (βi + εωi )|Y (i) with analytic singularities. Note that
                                                                  1
                                                                                                             (i)
(merely from Definition 2.6) it is unclear if Si,ε has gentle analytic singularities on Y1 or
not, but thanks to Theorem 2.8 one can approximate Si,ε by a sequence, say {Si,ε,k }k∈N ,
                                         (i)
with gentle analytic singularities on Y1 .
   Applying Theorem 6.4, we get S̃i,ε,k ∈ {βi + εωi }, currents on Xi , extending Si,ε,k for
each k. Moreover, S̃i,ε,k has analytic singularities on Xi . Then (the proof of) Lemma 3.1
implies that
             (0, νY′ (i) (Si )) = (0, νY′ (i) (Si,ε )) = (0, lim νY′ (i) (Si,ε,k ))
                        •                  •                    k→∞       •

                                                        = lim νY (i) (S̃i,ε,k ) ∈ ∆Y (i) ({βi + εωi })
                                                          k→∞         •               •


for any ε > 0. By Proposition 3.3(3) we can let ε → 0 to find that
                 0, νY′ (i) (πi∗ T ) ∈ ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]),
                                    
                               •                  •                                   •



                                                           25
where we used (0, ν ′ (i) ([Di ]|Y (i) )) = νY (i) ([Di ]). Since (0, νY′ • (T )) = (0, ν ′ (i) (πi∗ T )hi ) =
                            Y•       1        •                                          Y•
(0, ν ′ (i) (πi∗ T ))gi , we have that
     Y•

                    (0, νY′ • (T )) ∈ ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]) gi .
                                                                                  
                                         •                                     •


Thus, we see that

                    {0} × ∆t,i ⊆ ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]) gi .
                                                                             
                                         •                                     •

                                                                             (i)
   On the other hand, for any G ∈ Ω(Xi , {βi }) with ν(G, Y1 ) = 0, G+[Di ] is an element
in Ω(πi∗ ξt ). One can then apply Proposition 4.4 to find a sequence Gk ∈ A(X, ξt ) such
that

                     νY (i) (G + [Di ]) = lim νY (i) (πi∗ Gk )
                       •                     k→∞   •

                                        = lim νY• (Gk )gi−1 ∈ {0} × ∆t (ξ) gi−1 ,
                                                                          
                                             k→∞

where the last inclusion follows from Lemma 7.4 (since Gk + t[Y1 ] ∈ At (X, ξ), as t ∈ Q).
Thus,
                 ∆Y (i) ({βi }) ∩ {0} × Rn−1 + νY (i) ([Di ]) gi ⊆ {0} × ∆t (ξ).
                                                             
                        •                                   •

Therefore, ∆t,i ⊆ ∆t (ξ) follows, as claimed.
                                                            S
   From the above discussions we conclude that ∆t (ξ) = i ∆t,i . Moreover, since Ri is
an increasing sequence, we see that ∆t,i is an increasing sequence of (n − 1)-dimensional
convex bodies contained in ∆t (ξ). So we deduce that volRn−1 (∆t,i ) ↗ volRn−1 (∆t (ξ)),
concluding the proof of (4).
   We summarize our findings in the next result that proves both Theorem 1.1 and
Corollary 1.2:
Theorem 7.6. Let ξ be a big cohomology class on X. Let Y• be a flag on X. Then one
can associate to it a natural compact convex set ∆Y• (ξ) with ξ so that
                                                                1
                                      volRn (∆Y• (ξ)) =            vol(ξ).
                                                                n!
Proof. Let n = dim X. Let us first assume that ξ is big. We will show that Property An
and Property Bn hold for any dimension n ≥ 1 and Property Cn holds for any n ≥ 2.
We have proved the following implications:
   1. An ⇐⇒ Bn for n ≥ 1 by Lemma 5.7;
   2. Bn−1 =⇒ Cn for n ≥ 2 by Lemma 7.5;
   3. Cn =⇒ An for n ≥ 2 by Lemma 7.3.
By Lemma 3.6 Property A1 holds, so we conclude the big case by induction.
    As a simple corollary, we obtain the result for pseudoeffective classes as well:
Corollary 7.7. Let ξ be a pseudoeffective cohomology class on X. Let Y• be a flag on
X. Then one can associate to it a natural compact convex set ∆Y• (ξ) with ξ so that
                                                                1
                                      volRn (∆Y• (ξ)) =            vol(ξ).
                                                                n!
                                                       26
Proof. Due to the previous theorem, we can assume that ξ is pseudoeffective but not big.
In this case vol(ξ) = 0. By the definition of ∆Y• (ξ) (recall (3.1)) we obtain that

                           volRn (∆Y• (ξ)) ≤ volRn (∆Y• (ξ + ε{ω})) → 0,

thanks to the continuity of the volume functional on the pseudoeffective cone [12].


8     Moment bodies
The purpose of this section is to give an alternative approach to defining a convex body
associated with a big cohomology class ξ on a connected compact Kähler manifold X.
Instead of using valuation vectors ν(T ) of currents T ∈ Ω(X, ξ), we consider certain
iterated toric degenerations, where say (X, T ) degenerates to (Pn , Tn ), Tn being some
closed positive toric (1, 1)-current. Since Tn is toric it has an associated moment body
∆(Tn ) ⊆ Rn (as explained below). We then define the moment body ∆µ (ξ) as the closure
of the union of the moment bodies ∆(Tn ) of all toric degenerations. In the end we will
show that this moment body actually coincides with the Okounkov body ∆(ξ), thus
establishing a link between transcendental Okounkov bodies and toric degenerations.

Moment bodies of toric currents on Pn . Let T be a closed positive (1, 1)-current
on Pn which is toric (i.e. (S 1 )n -invariant) with respect to the standard toric action on
Pn . On Cn ⊂ Pn we can then write T = ddc ϕ where ϕ is a toric psh function on Cn , and
uϕ (x1 , . . . , xn ) := ϕ(ex1 /2 , . . . , exn /2 ) is a convex function on Rn .

Definition 8.1. The moment body ∆(T ) of T is the image of ∇uϕ , the subgradient map
of uϕ :
                              ∆(T ) := ∇uϕ (Rn ).

    If T is Kähler on (C∗ )n then in particular ((C∗ )n , T ) is a toric symplectic manifold, and
µ(e(x1 +iy1 )/2 , . . . , e(xn +iyn )/2 ) := ∇uϕ (x1 , . . . , xn ) is the so-called moment map, explaining
our terminology (see e.g. [14]).         R
    If {T } = c1 (O(k)) and Pn T n > 0, then the moment body ∆(T ) coincides with the
partial Okounkov body of the singular metric corresponding to T in the sense of [52], as
proved in [52, Theorem 8.3].
    Let us now record three well-known facts, whose proofs we give for the convenience
of the reader.

Lemma 8.2. The moment body ∆(T ) is convex.

Proof. Let u := uϕ . Note that u is convex and finite, and hence continuous. Let v be
a smooth convex function on Rn such that ∇(v)(Rn ) = B1 , where B1 denotes the unit
ball. Let ϵ > 0 and uϵ := u + ϵv. Let y1 , y2 ∈ ∇u(Rn ). We then get that the functions
u(x) − x · y1 and u(x) − x · y2 are both bounded from below, and thus uϵ (x) − x · y1 and
uϵ (x) − x · y1 are both proper and continuous. Given t ∈ [0, 1] it follows that

           t(uϵ (x) − x · y1 ) + (1 − t)(uϵ (x) − x · y2 ) = uϵ (x) − x · (ty1 + (1 − t)y2 )

also is proper and continuous, and hence achieves a minumum at some point x0 . One
then sees that ty1 + (1 − t)y2 is a subgradient of uϵ at x0 , thus ty1 + (1 − t)y2 ∈ ∇uϵ (Rn )


                                                    27
for all ϵ > 0. Now we note that ∇uϵ (Rn ) ⊆ ∇u(Rn ) + Bϵ . It follows that ty1 + (1 − t)y2 ∈
∇u(Rn ) + Bϵ for all ϵ > 0, and hence ty1 + (1 − t)y2 ∈ ∇u(Rn ).
    If y1 , y2 ∈ ∇u(Rn ) then y1 and y2 can be approximated by y1′ , y2′ ∈ ∇u(Rn ), hence
ty1 + (1 − t)y2′ ∈ ∇u(Rn ), and going to the limit yields that ty1 + (1 − t)y2 ∈ ∇u(Rn ).
  ′

This shows that ∆(T ) = ∇u(Rn ) is convex.

Lemma 8.3. Suppose that T1 and T2 are two toric closed positive (1, 1)-currents on Pn .
Assume that T1 is more singular than T2 , then ∆(T1 ) ⊆ ∆(T2 ).

Proof. Let u1 := uϕ1 and u2 := uϕ2 and let v be as in the proof of Lemma 8.2. For ϵ > 0
let u1,ϵ := u1 + ϵv and u2,ϵ := u2 + ϵv. Let y ∈ ∇u1 (Rn ). It follows then that the function
u1 (x) − x · y is bounded from below, and since u1 ≤ u2 + C we get that u2,ϵ (x) − x · y
is proper and continuous for all ϵ > 0. Hence, u2,ϵ (x) − x · y achieves its minimum at
some point xϵ , and there y will be a subgradient of u2,ϵ . Thus, y ∈ ∇u2 (Rn ) + Bϵ for
all ϵ, and hence y ∈ ∇u2 (Rn ). We have thus shown that ∇u1 (Rn ) ⊆ ∇u2 (Rn ), i.e.,
∆(T1 ) ⊆ ∆(T2 ).

Proposition 8.4. Under the assumptions as above,
                                              Z
                                            1
                            volRn (∆(T )) =       T n.
                                            n! Pn
Proof. We have that
            Z       Z                            Z
                  n                  c   n
                T =                (dd ϕ) = n!        MA(uϕ ) = n! volRn (∇u(Rn ))
                Pn        (C∗ )n                 Rn

                                                              = n! volRn (∆(T )),

where MA denotes the real Monge–Ampère operator in the sense of Alexandrov. In
the second equality we used the standard relationship between the complex and the real
Monge–Ampère operator [16, Lemma 2.2] (note that the normalization of the real Monge–
Ampère operator in [16] differs from the usual convention by n!) while the third equality
used the definition of the real Monge–Ampère operator, namely that
                                Z
                                    MA(u) := volRn (∇u(A))
                                     A

for any Borel subset A ⊆ Rn .

Deformation to the normal bundle. Recall that if Y is a connected submanifold
of a complex manifold X, the blow-up of X × P1 along Y × {0} defines the total space
X of what is called the (standard) deformation of X to the normal bundle NY |X of
Y . There is an obvious morphism X → P1 . The zero fiber has two components: Z
which is isomorphic to the blow-up of Y in X, and the exceptional divisor E, which is
isomorphic to the projective completion of NY |X . The natural C∗ -action on X × P1 (i.e.
τ (z, w) := (z, τ w)) lifts to X , and it restricts to the inverse C∗ -action on the normal
bundle (i.e. τ acts on a fiber by multiplication by τ −1 ).




                                                 28
Toric degenerations. Now assume that Y• is a smooth flag in X. Let X 1 denote the
deformation of X to the normal bundle NY1 |X of Y1 , and let X 1 denote the exceptional
divisor, so that X 1 is ismorphic to P(NY1 |X ⊕ C). Let also Z 1 denote the other component
of the zero fiber.
     If we use the natural identification between Y1 and the zero section of NY1 |X we can
identify Y2 with a submanifold in X 1 . Thus, we let X 2 denote the deformation of X 1 to
the normal bundle NY2 |X 1 of Y2 . Also let X 2 denote the exceptional divisor, so that X 2
is isomorphic to P(NY2 |X 1 ⊕ C). We also let Z 2 denote the other component of the zero
fiber. As Y2 is fixed by the C∗ -action on X 1 , the action extends to X 2 . This gives X 2 a
combined (C∗ )2 -action, which also restricts to X 2 .
     Continuing this way we get a sequence of deformation spaces X i for i = 1, . . . , n, with
generic fiber X i−1 (with X 0 := X) and exceptional divisor X i (the other component of
the zero fiber is denoted by Z i ), such that X i has a (C∗ )i -action restricting to X i .
     Choose local holomorphic coordinates zi on X centered at Yn = x ∈ X such that
locally Yi = {z1 = · · · = zi = 0}. This induces local holomorphic coordinates zi on
NY1 |X centered at Yn = x ∈ NY1 |X such that the C∗ -action on the normal bundle acts
by τ (z1 , . . . , zn ) = (τ z1 , z2 , . . . , zn ). When taking the normal bundle of Y2 we again
get an induced set of local holomorphic coordinates zi centered at Yn = x ∈ NY2 |X 1 .
The C∗ -action inherited from NY1 |X will still act by τ (z1 , . . . , zn ) = (τ z1 , z2 , . . . , zn ),
while the new C∗ -action coming from the normal bundle structure will be τ (z1 , . . . , zn ) =
(τ z1 , τ z2 , z3 , . . . , zn ). Continuing this way we see that we get local coordinates zi on each
X i centered at Yn = x ∈ X i adapted to the induced (C∗ )i -action.
     In the last step we consider the normal bundle of Yn = x ∈ X n−1 , but since x
is just a point, NYn |X n−1 is the tangent space Tx (X n−1 ) of x in X n−1 . One can see
that the induced local coordinates zi on Tx (X n−1 ) respect the vector space structure,
giving us an identification of Tx (X n−1 ) with Cn which adapts to the torus action. As
X n = P(NYn |X n−1 ⊕ C) we see that X n ≃ Pn , and we will identify X n with Pn by means
of the identification of Tx (X n−1 ) with Cn . The induced (C∗ )n -action on X n , described
above, acts on Cn ⊆ X n by (τ1 , . . . , τn )(z1 , . . . , zn ) = (τ1 τ2 . . . τn z1 , τ2 τ3 . . . τn z2 , . . . , τn zn ).
Here we note that this is different from the standard action (τ1 , . . . , τn )(z1 , . . . , zn ) =
(τ1 z1 , τ2 z2 , . . . , τn zn ). But we note that a current is toric (i.e. (S 1 )n -invariant) with
respect to the induced action if and only if it is toric with respect to the standard action.
     Via the above method X is degenerated (in n steps) to Pn , without taking account of
the class ξ. To remedy this, we want to equip the deformation spaces X i with compatible
currents, that somehow ‘metrize’ the n-step degeneration (in a possibly singular sense).
     Note that there is a natural morphism X i → P1 for each i = 1, . . . , n. For any c ∈ P1 ,
we denote the fiber of X i over c as Xci . For i = 1, . . . , n − 1, let πX i : X i+1 → X i denote
the natural morphism. We write πX 0 = πX : X 1 → X for the natural projection map.
Note that the inclusion X ,→ X × P1 as the fiber over 1 induces an isomorphism X ∼                                = X11 .
                                                                  1                                           i−1
We will fix this isomorphism and identify X with X1 . Similarly, we identify X                                      with
   i
X1 in the natural way for any i = 2, . . . , n.

Definition 8.5. A choice of closed positive (1, 1)-currents Ti on X i for each i = 1, . . . , n
is called a toric degeneration of (X, ξ) (with respect to the flag Y• ) if:

   1. Ti is (S 1 )i -invariant for all i = 1, . . . , n;

   2. for all i = 1, . . . , n, Ti has smooth local potentials on the complement of some
      analytic set Ai ⊂ X i which does not contain (but can intersect) X1i or X i ;

                                                           29
   3. T1 |X11 ∈ Z+ (X, ξ) and Ti |X1i = Ti−1 |X i−1 for i = 2, . . . , n.

   Note that by the second assumption we are allowed to restrict Ti to X1i and X i .
   If we denote by T0 := T1 |X11 and Ti := Ti |X i for i = 1, . . . , n, we see that the toric
degeneration T• encodes a degeneration of (X, T0 ) to (Pn , Tn ), and that Tn is a toric
current. By abuse of language, we will thus also call (Pn , Tn ) a toric degeneration of
(X, ξ). It should be understood that when we refer to a toric degeneration (Pn , Tn ), the
currents T1 , . . . , Tn are implicitly chosen. We also say the T• ’s are the family of currents
associated with the toric degeneration (Pn , Tn ).

The moment body of (X, ξ). We now note that if (Pn , Tn ) is a toric degeneration of
(X, ξ), then Tn will have an associated moment body ∆(Tn ).
Definition 8.6. We define the moment body ∆µ (ξ) = ∆µY• (ξ) of ξ (with respect to the
flag Y• ) as the closure of the union of the moment bodies ∆(Tn ) of all toric degenerations
(Pn , Tn ) of (X, ξ) (with respect to the flag Y• ).
    From the definition it is not obvious that the moment body is convex, since the union
of convex sets need not be convex. However, the convexity will follow from the next
proposition.
Proposition 8.7. If (Pn , Tn ) and (Pn , Tn′ ) are two toric degenerations of (X, ξ) one can
find a third toric degeneration (Pn , Tn′′ ) of (X, ξ) such that

                                     ∆(Tn′′ ) ⊇ ∆(Tn ) ∪ ∆(Tn′ ).

    The proof of Proposition 8.7 will rely on the following lemma.
Lemma 8.8. Let T• be a toric degeneration of (X, ξ). For any i = 1, . . . , n and b, c ∈ R≥0 ,
the currents T̃• defined by
                             
                             
                                                    Tj , if j ̸= i, i + 1;
                      T̃j :=               i
                                  Ti + b[X∞ ] + c[Z i ], if j = i;
                                        ∗      i
                               Ti+1 + c[πX i ([Z ]|X i )], if j = i + 1 ≤ n
                             

also give a toric degeneration of (X, ξ). Furthermore, we have that

                                           ∆(T̃n ) = ∆(Tn ).

Proof. We first verify that T̃• is a toric degeneration. It suffices to verify the three
                                                                                      i
conditions in Definition 8.5. Condition 1 follows from the facts that Ti , [X∞          ] and [Z i ] are
all (S 1 )i -invariant and that πX i is C∗ -equivariant. Condition 2 and Condition 3 are clear
by definition.
     To see that the moment body remains unchanged, note that if i < n − 1, then
T̃n = Tn , in which case the equality is obvious. If i = n − 1, note that Z n−1 does not
intersect the zero section of X n−1 which we identify with Yn−1 . From this it follows
         −1       n−1                                                  ∗
that πX    n−1 (X     ∩ Z n−1 ) does not intersect X n = Pn . Since πX        i
                                                                         i ([Z ]X i ) has support on
  −1         n−1
πX  n−1 (X       ∩ Z n−1 ) we thus get that also in this case T̃n = Tn . Now assume that i = n.
Here we see that T̃n = Tn + c[Zn ]|Pn , but since Pn ∩ Z n is the divisor at infinity and the
moment body only depends on T̃n |Cn , we get that also in this case the moment body is
unchanged.

                                                   30
Proof of Proposition 8.7. Let T• and T•′ be the families of currents associated with the
toric degenerations (Pn , Tn ) and (Pn , Tn′ ). First we want to show that we can find toric
degenerations T̃• and T̃•′ such that ∆(T̃n ) = ∆(Tn ) and ∆(T̃n′ ) = ∆(Tn′ ) and such that
{T̃i } = {T̃i′ } for all i = 1, . . . , n.
     Let βi := {Ti } and βi′ := {Ti′ }. Recall that H 1,1 (X i , R) is generated by the pullback
of H 1,1 (X i−1 × P1 , R) together with the class {[X i ]}. Since β1 |X11 = β1′ |X11 = ξ we thus
have that
                 ∗
           β1 = πX             1            1
                   0 ξ + b1 {[X∞ ]} − c1 {[X ]},           β1′ = πX
                                                                  ∗        ′    1       ′    1
                                                                    0 ξ + b1 {[X∞ ]} − c1 {[X ]}



for some real numbers b1 , c1 , b′1 , c′1 . Now note that

                {[Z 1 ]} = {[X01 ] − [X 1 ]} = {[X01 ]} − {[X 1 ]} = {[X∞
                                                                        1
                                                                          ]} − {[X 1 ]},

so we can write
                                    ∗                  1
                              β1 = πX ξ + (b1 − c1 ){[X∞ ]} + c1 {[Z 1 ]},
                              β1′ = πX
                                     ∗
                                       ξ + (b′1 − c′1 ){[X∞
                                                          1
                                                            ]} + c′1 {[Z 1 ]}.
From this it is clear that one can find positive numbers d1 , d′1 , e1 , e′1 such that
                                   1
                        {T1 + d1 [X∞ ] + e1 [Z 1 ]} = {Ω′1 + d′1 [X∞
                                                                   1
                                                                     ] + e′1 [Z 1 ]}.
                                          1                                 ∗
Let T̃• be defined by T̃1 := Ω1 + d1 [X∞    ] + e1 [Z 1 ], T̃2 := T2 + e1 πX          1
                                                                               1 ([Z ]|X 1 ) and T̃j := Tj for

j > 2. Similarly, let T̃1′ := T1′ + d′1 [X∞1
                                             ] + e′1 [Z 1 ], T̃2′ := T2′ + e′1 πX∗      1               ′
                                                                                   1 ([Z ]|X 1 ) and T̃j := Tj
                                                                                                              ′

for j > 2.
    It follows from Lemma 8.8 that T̃• and T̃•′ are new toric degenerations such that

                                             ∆(T̃n ) = ∆(Tn ).

We have also made sure that {T̃1 } = {T̃1′ }. If {T̃i } ̸= {T̃i′ } for some i > 1 we can use
the same trick of modifying T̃• and T̃•′ without changing the moment bodies, eventually
achieving that {T̃i } = {T̃i′ } for all i.
   Thus, without loss of generality we can assume that {Ti } = {Ti′ } for all i = 1, . . . , n.
For all such i, pick a smooth closed real (S 1 )i -invariant (1, 1)-form θi ∈ {Ti } and write
Ti = θi + ddc ϕi and Ti′ = θ1 + ddc ϕ′i for some ϕi , ϕ′i ∈ PSH(X i , θ1 ). Let also maxreg (x, y)
be a regularized maximum function with the properties that it is smooth and convex,

                              max(x, y) ≤ max(x, y) ≤ max(x, y) + 1,
                                               reg

and such that
                                max(x, y) = max(x, y) if |x − y| ≥ 1.
                                 reg

     Let T1′′ := θ1 + ddc maxreg (ϕ1 , ϕ′1 ). It is clear that T1′′ is (S 1 )-invariant, has smooth
local potentials on the complement of some analytic set which does not contain X11 or
X 1 , and that {T1′′ |X 1 } = ξ.
                        1
                    ∗                2             2            ∗    ′′         2         2
     If {T2 } = {πX   1 T1 } + d2 {[X∞ ]} + e2 {[Z ]}, write πX 1 T1 + d2 [X∞ ] + e2 [Z ] = θ2 +

ddc ψ2 for some ψ2 ∈ PSH(X 2 , θ2 ). Since the current T1′′ is less singular than T1 and
T1′ it follows that ψ2 |X12 is less singular than ϕ2 |X12 and ϕ′2 |X12 . After possibly adding
a constant we can thus assume that ψ2 ≥ maxreg (ϕ2 , ϕ′2 ) + 1 on X12 . Now let T2′′ :=
θ2 + ddc maxreg (ψ2 , maxreg (ϕ2 , ϕ′2 )).

                                                      31
    It is clear that T2′′ is (S 1 )2 -invariant, has smooth local potentials on the complement
of some analytic set which does not contain X12 or X 2 . Also, since

                                    max(ψ2 , max(ϕ2 , ϕ′2 )) = ψ2
                                        reg         reg


on X12 , we have that T2′′ |X 2 = T1′′ |X 1 .
                             1
    Continuing this way we can construct currents Ti′′ for all i = 1, . . . , n, and as above
one can easily check that T•′′ will have the properties of a toric degeneration of (X, ξ).
We also see that the current Tn′′ will be less singular than Tn and Tn′ , and so the desired
inclusion
                                     ∆(Tn′′ ) ⊇ ∆(Tn ) ∪ ∆(Tn′ )
follows from Lemma 8.3.
Corollary 8.9. The moment body ∆µ (ξ) is convex.
Proof. From Lemma 8.2 and Proposition 8.7 it follows that ∆µ (ξ) is the closure of a
convex set, and hence it is convex.
    We now prove a volume inequality for the moment body.
Proposition 8.10. Under the above assumptions, we have that
                                                                1
                                        volRn (∆µ (ξ)) ≤           vol(ξ).
                                                                n!
Proof. It follows from Proposition 8.7 that the volume of ∆µ (ξ) is equal to the supremum
of the volume of the moment bodies of the toric degenerations of (X, ξ).
    Let T• be a toric degeneration. We first claim that for all i = 1, . . . , n:
                                    Z          Z
                                          n
                                        Ti ≤      Ti n .                              (8.1)
                                              Xi               X1i

                                                                  ∗                     i            i
From the proof of Proposition 8.7 we see that {Ti } = πX            i−i {Ti−1 } + bi {[X∞ ]} − ci {[X ]}

for some real numbers bi , ci . We let
                              (
                                                 i
                                      Ti − bi [X∞   ] + ci [X i ], if ci ≥ 0;
                     T̃i :=                       i
                                Ti − (bi − ci )[X∞  ] − ci [Z i ], if ci < 0.

                                          ∗                                            i     i
It follows that in both cases {T̃i } = πX   i−i {Ti−1 } and that T̃i is positive on X \ X∞ . Let
                                                                                    ∗           c
θ be a smooth closed real (1, 1)-form in {Ti−1 }. We can then write T̃i = πX          i−1 θ + dd ϕi
                 ∗                           i−1
where ϕi is a πX   i−1 θ-psh function on X       × C. Since Ti is S 1 -invariant with respect to
the action on the base, so is T̃i , and therefore ϕi is S 1 -invariant. For a fixed x ∈ X i−1
we get that ϕi (x, τ ) is subharmonic in τ , and since it also only depends on |τ | it follows
that it is increasing in |τ |. Since T̃i = Ti on X i−1 × C∗ and using monotonicity [50] we
get that                        Z         Z
                                      n
                                    Ti =         (θ + ddc ϕi (·, τ ))n
                                  Xτi              X i−1

is increasing in |τ | for |τ | > 0.
    Pick a tubular neighbourhood Ui of Yi in X i−1 together with an associated diffeo-
morphism f between NYi |X i−1 and Ui . Let F : NYi |X i−1 × C → X i be defined by

                                                          32
F (ζ, τ ) := (f (τ ζ), τ ) for τ ̸= 0 while F (ζ, 0) := ζ ∈ X i . Then F is a diffeomorphism
between NYi |X i−1 × C and its image. Pick a volume form dV on NYi |X i−1 . Since Ti has
smooth potentials on the complement of an analytic set not containing X i we can write
for τ ̸= 0:
                                       Fτ∗ ((Ti|Xτi )n ) = gτ dV,
for τ = 0:
                                              Tin = g0 dV,
and gτ will converge pointwise to g0 almost everywhere. It thus follows from Fatou’s
Lemma that
        Z         Z                    Z                   Z         Z
               n                                                n
             Ti =         g0 dV ≤ lim          gτ dV ≤ lim    Ti ≤      Ti n ,
             Xi         NY |X i−1          τ →0   NY |X i−1          τ →0   Xτi        X1i
                          i                         i


thus proving our claim (8.1).                              R
   Now we note that since T1 |X11 ∈ Z+ (X, ξ) we have that X 1 T1n ≤ vol(ξ) by definition.
                                                             1
By Proposition 8.4 we also have that
                                                  Z
                                                1
                               volRn (∆(Tn )) =       T n,
                                                n! Pn n
and combined with the inequalities (8.1) the proposition follows.
  Given a big class ξ and a flag Y• , we can construct the Okounkov body ∆Y• (ξ) and the
moment body ∆µY• (ξ). We will now show that they in fact coincide, proving Theorem 1.4.
Theorem 8.11. Under the above assumptions, we have that

                                          ∆µY• (ξ) = ∆Y• (ξ).                                       (8.2)

Proof. Pick T0 ∈ Ω(X, ξ) and write νY• (T0 ) = (ν1 , . . . , νn ). Pick also a smooth real closed
(1, 1)-form θ in the class ξ − ν1 [Y1 ]. We can thus write T0 = θ + ν1 [Y1 ] + ddc ϕ, where
ϕ ∈ PSH(X, θ) restricts to a θ|Y1 -psh function on Y1 . Let D1 denote the strict transform
of Y1 × P1 in X 1 , and let T1 := πX     ∗
                                           θ + ν1 [D1 ] + ddc πX∗
                                                                   ϕ. We see that T1 is a closed positive
S 1 -invariant current on X 1 which restricts to T0 on X11 , and which has a continuous
potential away from an analytic set not containing X11 or X 1 .
     Note that T1 = ν1 [Y1 ] + πY∗1 θ|Y1 + ddc πY∗1 (ϕ|Y1 ), where πY1 denotes the projection from
X 1 = P(NY1 |X ⊕ C) to the zero section identified with Y1 . We now see that we can write
T1 = θ1 + ν1 [Y1 ] + ν2 [W2 ] + ddc ϕ1 , where W2 := πY−1        1
                                                                   (Y2 ), θ1 and ϕ1 are S 1 -invariant and
ϕ1 restricts to a θ1 |Y2 -psh function on Y2 .
     Let D1 and D2 denote the strict transforms of Y1 × P1 and W2 × P1 in X 2 respectively.
               ∗                                     c ∗
Let T2 := πX     1 θ1 |Y2 + ν1 [D1 ] + ν2 [D2 ] + dd πX 1 (ϕ1 |Y2 ). We see that T2 is a closed positive

(S 1 )2 -invariant current on X 1 which restricts to T1 on X12 , and which has a continuous
potential away from an analytic set not containing X12 or X 2 .
     Note that T2 = ν1 [Y1 ] + ν2 [W2 ] + πY∗2 θ1 |Y2 + ddc πY∗2 (ϕ1 |Y2 ), where πY2 denotes the
projection from X 2 to Y2 . We now see that we can write T2 = θ2 + ν1 [Y1 ] + ν2 [W2 ] +
ν3 [W3 ] + ddc ϕ2 , where W3 := πY−1     2
                                           (Y3 ), θ2 and ϕ2 are (S 1 )2 -invariant and ϕ2 restricts to a
θ2 |Y3 -psh function on Y3 .
     Continuing this way we get a toric degeneration T• of (X, ξ) such that Tn = ν1 [Y1 ] +
ν2 [W2 ] + · · · + νn [Wn ]. The divisors Y1 , W2 , . . . , Wn are toric divisors and in the standard
toric coordinates zi we have that Y1 = {z1 = 0}, W2 = {z1 = z2 = 0}, and so on. Thus,

                                                   33
on Cn , Tn has the toric potential ψ = ν1 log |z1 |2 + · · · + νn log |zn |2 , and uψ (x1 , . . . , xn ) =
ν1 x1 + · · · + νn xn . We thus see that ∆(Tn ) = {(ν1 , . . . , νn )} = {ν(T0 )}, hence ∆Y• (ξ) ⊆
∆µY• (ξ). In particular,
                                                         1
                 volRn (∆Y• (ξ)) ≤ volRn (∆µY• (ξ)) ≤       vol(ξ) = volRn (∆Y• (ξ)),
                                                         n!
where the second inequality follows from Proposition 8.10 and the equality follows from
Theorem 7.6. It follows that all inequalities are actual equalities. Since ∆Y• (ξ) has
positive volume, we conclude (8.2).
Corollary 8.12. For any toric degeneration (Pn , Tn ) of (X, ξ) we have that

                                            ∆(Tn ) ⊆ ∆(ξ).

Furthermore, for any ϵ > 0 we can find a toric degeneration (Pn , Tn ) of (X, ξ) such that
the Hausdorff distance between ∆(Tn ) and ∆(ξ) is less than ϵ.
Proof. Since by definition ∆(Tn ) ⊆ ∆µ (ξ), the first claim follows from Theorem 8.11.
   That the moment body ∆µ (ξ) can be approximated arbitrarily well (with respect to
the Hausdorff distance) by moment bodies ∆(Tn ) of toric degenerations (Pn , Tn ) follows
from Proposition 8.7, so combined with Theorem 8.11 we get the second claim.
    Corollary 8.12 provides a strong link between transcendental Okounkov bodies and
toric degenerations, which could be useful in further investigations, for example studying
the transcendental Chebyshev transform.


References
[1] M. F. Atiyah and I. G. Macdonald, Introduction to commutative algebra, Addison-
    Wesley Publishing Co., 1969.

[2] D. Anderson, Okounkov bodies and toric degenerations, Math. Ann. 356.3 (2013), pp.
    1183–1202.

[3] S. Boucksom and H. Chen, Okounkov bodies of filtered linear series, Compos. Math.
    147.4 (2011), pp. 1205–1229.

[4] S. Boucksom, J.-P. Demailly, M. Păun, and T. Peternell, The pseudo-effective cone of
    a compact Kähler manifold and varieties of negative Kodaira dimension, J. Algebraic
    Geom. 22.2 (2013), pp. 201–248.

[5] S. Boucksom, P. Eyssidieux, V. Guedj, and A. Zeriahi, Monge-Ampère equations in
    big cohomology classes, Acta Math. 205.2 (2010), pp. 199–262.

[6] S. Boucksom, C. Favre, and M. Jonsson, Valuations and plurisubharmonic singulari-
    ties, Publ. Res. Inst. Math. Sci. 44.2 (2008), pp. 449–494.

[7] S. Boucksom, C. Favre, and M. Jonsson, Differentiability of volumes of divisors and
    a problem of Teissier, J. Algebraic Geom. 18.2 (2009), pp. 279–308.

[8] H. Blum and M. Jonsson, Thresholds, valuations, and K-stability, Adv. Math. 365
    (2020), pp. 107062, 57.

                                                   34
[9] S. Boucksom, A. Küronya, C. Maclean, and T. Szemberg, Vanishing sequences and
    Okounkov bodies, Math. Ann. 361.3-4 (2015), pp. 811–834.

[10] E. Bierstone and P. D. Milman, Canonical desingularization in characteristic zero
    by blowing up the maximum strata of a local invariant, Invent. Math. 128.2 (1997),
    pp. 207–302.

[11] S. Boucksom, Cônes positifs des variétés complexes compactes, Université Joseph-
    Fourier-Grenoble I, 2002.

[12] S. Boucksom, On the volume of a line bundle, Internat. J. Math. 13.10 (2002), pp.
    1043–1063.

[13] S. Boucksom, Divisorial Zariski decompositions on compact complex manifolds, Ann.
    Sci. École Norm. Sup. (4) 37.1 (2004), pp. 45–76.

[14] A. Cannas da Silva, An invitation to symplectic toric manifolds, Bol. Soc. Port. Mat.
    77 (2019), pp. 119–132.

[15] C. Ciliberto, M. Farnik, A. Küronya, V. Lozovanu, J. Roé, and C. Shramov, New-
    ton–Okounkov bodies sprouting on the valuative tree, Rendiconti del Circolo Matem-
    atico di Palermo Series 2 66.2 (2017), pp. 161–194.

[16] D. Coman, V. Guedj, S. Sahin, and A. Zeriahi, Toric pluripotential theory, Ann.
    Polon. Math. 123.1 (2019), pp. 215–242.

[17] D. Coman, V. Guedj, and A. Zeriahi, Extension of plurisubharmonic functions with
    growth control, J. Reine Angew. Math. 676 (2013), pp. 33–49.

[18] S. R. Choi, Y. Hyun, J. Park, and J. Won, Okounkov bodies associated to pseudoef-
    fective divisors, J. Lond. Math. Soc. (2) 97.2 (2018), pp. 170–195.

[19] T. C. Collins and V. Tosatti, An extension theorem for Kähler currents with analytic
    singularities, Ann. Fac. Sci. Toulouse Math. (6) 23.4 (2014).

[20] T. C. Collins and V. Tosatti, Restricted volumes on Kähler manifolds, Ann. Fac. Sci.
    Toulouse Math. (6) 31.3 (2022), pp. 907–947.

[21] J.-P. Demailly, Analytic methods in algebraic geometry, Vol. 1, Surveys of Modern
    Mathematics, International Press, Higher Education Press, Beijing, 2012.

[22] J.-P. Demailly, Complex Analytic and Differential Geometry, Available on personal
    website, 2012.

[23] J.-P. Demailly, On the cohomology of pseudoeffective line bundles, Complex geometry
    and dynamics, Vol. 10, Abel Symp., Springer, Cham, 2015, pp. 51–99.

[24] J.-P. Demailly, Regularization of closed positive currents and intersection theory, J.
    Algebraic Geom. 1.3 (1992), 361–409.

[25] Y. Deng, Transcendental Morse inequality and generalized Okounkov bodies, Algebr.
    Geom. 4.2 (2017), 177–202.



                                            35
[26] S. Dinew, V. Guedj, and A. Zeriahi, Open problems in pluripotential theory, Complex
    Var. Elliptic Equ. 61.7 (2016), 902–930.

[27] J.-P. Demailly and M. Păun, Numerical characterization of the Kähler cone of a
    compact Kähler manifold, Ann. of Math. (2) 159.3 (2004), 1247–1274.

[28] R. Dervan and J. Ross, K-stability for Kähler manifolds, Math. Res. Lett. 24.3
    (2017), 689–739.

[29] H. Hironaka, Flattening theorem in complex-analytic geometry, Amer. J. Math. 97
    (1975), 503–547.

[30] T. Hisamoto, Restricted Bergman kernel asymptotics, Trans. Amer. Math. Soc. 364.7
    (2012), 3585–3607.
[31] M. Harada and K. Kaveh, Integrable systems, toric degenerations and Okounkov
    bodies, Invent. Math. 202.3 (2015), 927–985.

[32] C. Jiang and Z. Li, Algebraic reverse Khovanskii-Teissier inequality via Okounkov
    bodies, Math. Z. 305.2 (2023), Paper No. 26, 14.

[33] K. Kaveh, Toric degenerations and symplectic geometry of smooth projective vari-
    eties, J. Lond. Math. Soc. 99.2 (2019), 377–402.

[34] K. Kaveh and A. G. Khovanskii, Newton-Okounkov bodies, semigroups of integral
    points, graded algebras and intersection theory, Ann. of Math. (2) 176.2 (2012),
    925–978.

[35] R. Lazarsfeld and M. Mustaţă, Convex bodies associated to linear series, Ann. Sci.
    Éc. Norm. Supér. (4) 42.5 (2009), 783–835.

[36] C. Li and C. Xu, Stability of valuations: higher rational rank, Peking Math. J. 1.1
    (2018), 1–79.

[37] S. Matsumura, Restricted volumes and divisorial Zariski decompositions, Amer. J.
    Math. 135.3 (2013), 637–662.
[38] T. Murata, Toric degenerations of projective varieties with an application to equivari-
    ant Hilbert functions, Thesis (Ph.D.)–University of Pittsburgh, ProQuest LLC, Ann
    Arbor, MI, 2020.

[39] N. Nakayama, The lower semicontinuity of the plurigenera of complex varieties, Al-
    gebraic geometry, Sendai, 1985, Vol. 10, Adv. Stud. Pure Math., North-Holland,
    Amsterdam, 1987, 551–590.

[40] J. Ning, Z. Wang, and X. Zhou, On the extension of Kähler currents on compact
    Kähler manifolds: holomorphic retraction case, Ann. Fac. Sci. Toulouse Math. (6)
    (2024), 183–195.

[41] A. Okounkov, Brunn-Minkowski inequality for multiplicities, Invent. Math. 125.3
    (1996), 405–411.

[42] J. Ross and D. Witt Nyström, Envelopes of positive metrics with prescribed singu-
    larities, Ann. Fac. Sci. Toulouse Math. (6) 26.3 (2017), 687–728.

                                            36
[43] Z. Sjöström Dyrefelt, K-semistability of cscK manifolds with transcendental coho-
    mology class, J. Geom. Anal. 28.4 (2018), 2927–2960.

[44] Y. T. Siu, Analyticity of sets associated to Lelong numbers and the extension of
    closed positive currents, Invent. Math. 27 (1974), 53–156.

[45] D.-V. Vu, Derivative of volumes of big cohomology classes, 2023, arXiv:2307.15909
    [math.AG].

[46] J. Wlodarczyk, Resolution of singularities of analytic spaces, Proceedings of
    Göokova Geometry-Topology Conference 2008, Göokova Geometry/Topology Con-
    ference (GGT), 2009, 31–63.

[47] D. Witt Nyström, Transforming metrics on a line bundle to the Okounkov body, Ann.
    Sci. Éc. Norm. Supér. (4) 47.6 (2014), 1111–1161.

[48] D. Witt Nyström, Canonical growth conditions associated to ample line bundles,
    Duke Math. J. 167.3 (2018), 449–495.

[49] D. Witt Nyström, Duality between the pseudoeffective and the movable cone on a
    projective manifold, J. Amer. Math. Soc. 32.3 (2019), 675–689. With an appendix by
    Sébastien Boucksom.

[50] D. Witt Nyström, Monotonicity of non-pluripolar Monge-Ampère masses, Indiana
    Univ. Math. J. 68.2 (2019), 579–591.

[51] D. Witt Nyström, Deformations of Kähler manifolds to normal bundles and
    restricted volumes of big classes, J. Differential Geom. (to appear) (2021).
    arXiv:2103.03660 [math.AG].

[52] M. Xia, Partial Okounkov bodies and Duistermaat–Heckman measures of non-
    Archimedean metrics, Geom. Topol. (to appear) (2021). arXiv:2112.04290 [math.AG].


Tamás Darvas, University of Maryland
tdarvas@umd.edu
Rémi Reboulet, David Witt Nyström, Chalmers University of Technology
and University of Gothenburg
reboulet@chalmers.se, wittnyst@chalmers.se
Mingchen Xia, Chalmers Tekniska Högskola and Institute of Geometry
and Physics, USTC
xiamingchen2008@gmail.com
Kewei Zhang, Beijing Normal University
kwzhang@bnu.edu.cn




                                          37


# Complete actual public primary text: 2112.04290v2

                                                  PARTIAL OKOUNKOV BODIES AND DUISTERMAAT–HECKMAN
                                                         MEASURES OF NON-ARCHIMEDEAN METRICS

                                                                                           MINGCHEN XIA
arXiv:2112.04290v2 [math.AG] 13 Apr 2024




                                                   Abstract. Let X be a smooth complex projective variety. We construct partial Okounkov bodies
                                                   associated with Hermitian big line bundles (L, φ) on X. We show that partial Okounkov bodies are
                                                   universal invariants of the singularities of φ. As an application, we construct Duistermaat–Heckman
                                                   measures associated with finite energy metrics on the Berkovich analytification of an ample line
                                                   bundle.




                                                                                             Contents
                                             1. Introduction                                                                                              1
                                             2. Preliminaries                                                                                             6
                                             3. The Okounkov bodies of almost semigroups                                                                 11
                                             4. The metric on the space of singularity types                                                             15
                                             5. Partial Okounkov bodies                                                                                  18
                                             6. Chebyshev transform                                                                                      30
                                             7. A generalization of Boucksom–Chen theorem                                                                34
                                             8. Toric setting                                                                                            42
                                             References                                                                                                  47



                                                                                         1. Introduction
                                           1.1. Background. Let X be an irreducible smooth projective variety of dimension n and L be
                                           a big holomorphic line bundle on X. Given any admissible ﬂag X = Y0 ⊇ Y1 ⊇ · · · ⊇ Yn on
                                           X (see Deﬁnition 2.7 for the precise deﬁnition), one can attach a natural convex body ∆(L) of
                                           dimension n to L, generalizing the classical Newton polytope construction in toric geometry. This
                                           construction was ﬁrst considered by Okounkov [Oko96; Oko03] and then extended by Lazarsfeld–
                                           Mustat, ă [LM09] and Kaveh–Khovanskii [KK12]. The convex body ∆(L) is known as the Okounkov
                                           body or Newton–Okounkov body associated with L (with respect to the given ﬂag). We brieﬂy recall
                                           its deﬁnition: given any non-zero s ∈ H0 (X, Lk ), let ν1 (s) be the vanishing order of s along Y1 .
                                           Then s can be regarded as a section of H0 (X, Lk ⊗ OX (−ν1 (s)Y1 )). It follows that s1 := s|Y1 is a
                                           non-zero section of L|kY1 ⊗ OX (−ν1 (s)Y1 )|Y1 . We can then repeat the same procedure with s1 , Y2
                                           in place of s, Y1 . Repeating this construction, we end up with ν(s) = (ν1 (s), . . . , νn (s)) ∈ Nn . In
                                           fact, ν extends naturally to a rank n valuation on C(X). Consider the semigroup
                                                                               n                                                o
                                                                     Γ(L) := (ν(s), k) ∈ Zn+1 : k ∈ N, s ∈ H0 (X, Lk )× .

                                             Keywords—Okounkov bodies, pseudo-effective line bundles, convex bodies, pluri-subharmonic functions
                                             MSC : 14M25, 32U05
                                             Mingchen Xia, Institut de Mathématiques de Jussieu-Paris Rive Gauche
                                             Email address, mingchen@imj-prg.fr
                                             Homepage, http://mingchenxia.github.io/home/.
                                                                                                   1
2                                          MINGCHEN XIA

Then ∆(L) is the intersection of the closed convex cone in Rn+1 generated by Γ(L) with the
hyperplane {(x, 1) : x ∈ Rn }. A key property of ∆(L) is that the Lebesgue volume of ∆(L) is
proportional to the volume of the line bundle L:
                                                    1
(1.1)                                   vol ∆(L) = hLn i.
                                                    n!
Here h•i denotes the movable intersection product in the sense of [BDPP13; BFJ09].
   In [LM09], Lazarsfeld–Mustat, ă showed moreover that ∆(L) depends only on the numerical class
of L. Conversely, it is shown by Jow [Jow10] that the information of all Okounkov bodies with
respect to various ﬂags actually determines the numerical class of L. In other words, Okounkov
bodies can be regarded as universal numerical invariants of big line bundles.
   This paper concerns a similar problem. Assume that L is equipped with a singular plurisubhar-
monic (psh) metric φ. We will construct universal invariants of the singularity type of φ. We call
these universal invariants the partial Okounkov bodies of (L, φ).
1.2. Main results. Let us explain more details about the construction of partial Okounkov bodies.
Recall that any admissible ﬂag on X induces a rank n valuation on C(X) with values in Zn . We
will work more generally with such valuations, not necessarily coming from admissible ﬂags on X.
We deﬁne a set
                             n                                                   o
(1.2)             Γ(L, φ) := (ν(s), k) ∈ Zn+1 : k ∈ N, s ∈ H0 (X, Lk ⊗ I(kφ))×
similar to Γ(L). Here I(•) denotes the multiplier ideal sheaf in the sense of Nadel. However, a key
diﬀerence here is that Γ(L, φ) is not a semigroup in general. Thus, the constructions in both [LM09]
and [KK12] break down. We will show that in this case, there is still a canonical construction of
Okounkov bodies.
   Before stating our main theorem, let us recall the deﬁnition of volume. The volume of (L, φ) is
deﬁned as
                                                 1
                               vol(L, φ) := lim n h0 (X, Lk ⊗ I(kφ)).
                                            k→∞ k
The existence of this limit is proved in [DX21].
Theorem A. Let (L, φ) be as above. Assume that vol(L, φ) > 0. Then there is a convex body
∆(L, φ) ⊆ ∆(L) associated with (L, φ) satisfying
(1.3)                                 vol ∆(L, φ) = vol(L, φ).
                                              R
   Moreover, ∆(L, φ) is continuous in φ if X (ddc φ)n > 0. Here the set of φ is endowed with
the dS -pseudometric in the sense of [DDNL21b] and the set of convex bodies is endowed with the
Hausdorff metric.
   Define                      n                                       o
                         Γk := k−1 ν(s) ∈ Rn : s ∈ H0 (X, Lk ⊗ I(kφ))×
and let ∆k denote the convex hull of Γk . Then
(1.4)                                      ∆k → ∆(L, φ)
with respect to the Hausdorff metric if vol(L, φ) > 0.
   Observe that the last assertion actually uniquely determines ∆(L, φ), so ∆(L, φ) can be regarded
as canonically attached to the given data (X, L, φ, ν).
   The convex body ∆(L, φ) is called the partial Okounkov body of (L, φ) with respect to the given
valuation. Here the word partial refers to the fact that the partial Okounkov bodies are contained
in ∆(L). One should not confuse them with the notion of Okounkov bodies with respect to partial
ﬂags.
   We will also extend the deﬁnition to the case vol(L, φ) = 0 in Section 5.6, at the expense of
losing continuity in φ.
                                        PARTIAL OKOUNKOV BODIES                                   3

  Observe that (1.3) bears strong resemblance with (1.1). In fact, when φ has minimal singularities,
∆(L, φ) = ∆(L) and (1.3) just reduces to (1.1).
  The second main result says that partial Okounkov bodies uniquely determine the I-singularity
type of φ.
Theorem B. Let L be a big line bundle on X. Let φ, φ′ be two singular psh metrics on L with
positive volumes. Then the following are equivalent:
    (1) φ ∼I φ′ .
    (2) ∆(L, φ) = ∆(L, φ′ ) for all rank n valuations on C(X) taking values in Zn .
   Recall that φ ∼I φ′ means I(kφ) = I(kφ′ ) for all real k > 0. This relation is studied in detail
in [DX22; DX21]. It captures a lot of important information about the singularity of a psh metric.
Theorem B should be regarded as a metric analogue of Jow’s theorem.
   As a byproduct of our proof of Theorem B, we reprove a formula computing the generic Lelong
numbers of currents of minimal singularities in c1 (L), slightly generalizing [Bou02b, Theorem 5.4]:
Theorem 1.1 (=Corollary 5.25). Let L be a big line bundle on X. Consider a current Tmin of
minimal singularity in c1 (L). Then for any prime divisor E over X, we have
                                                 1
(1.5)                           ν(Tmin , E) = lim ordE H0 (X, Lk ).
                                             k→∞ k
Here ν(Tmin , E) denotes the generic Lelong number of Tmin along E.
   As a consequence, we ﬁnd a new formula computing the multiplier ideal sheaf I(Tmin ) in Corol-
lary 5.26.
   The third main result is an analogue of [WN14]. Given any continuous metric ψ on L, one can
naturally construct a convex function c[ψ] on Int ∆(L), known as the Chebyshev transform of ψ.
The main property of c[ψ] is that given another continuous metric ψ ′ on L, we have
                                  Z
                                                           
(1.6)                                        c[ψ] − c[ψ ′ ] dλ = vol(ψ, ψ ′ ),
                                      ∆(L)

where vol(ψ, ψ ′ ) is the relative volume as studied in [BB10;
                                                           BBWN11] and dλ is the Lebesgue
measure on Rn . In our setup, we also associate a convex function: c[φ] [ψ] : Int ∆(L, φ) → R.
Moreover,
Theorem C. Assume that the valuation ν is induced by an admissible flag on X. Let ψ, ψ ′ be two
continuous metrics on L, then
                        Z                             
(1.7)                             c[φ] [ψ] − c[φ] [ψ ′ ] dλ = −E[φ]
                                                                θ          θ
                                                                    (ψ) + E[φ] (ψ ′ ),
                         ∆(L,φ)
       θ is the partial equilibrium energy functional defined in (6.1).
where E[φ]
   Theorem A, Theorem B and Theorem C together give convex-geometric interpretations of the
main results of [DX22; DX21]. These results also provide us with a convex-geometric approach to
the study of psh singularities.
   As an application of our theory, we prove a generalization of Boucksom–Chen theorem (Theo-
rem 7.9). Recall the theorem Boucksom–Chen [BC11] says that given a multiplicative ﬁltration F
on the section ring R(X, L), one can naturally associate a probability measure on R, known as the
Duistermaat–Heckman measure. Moreover, the Duistermaat–Heckman measure is the weak limit
of a sequence of discrete measures µk associated with the ﬁltration F on H0 (X, Lk ). We show
that this construction can be generalized to all I-model test curves, not necessarily coming from
ﬁltrations. Here we only prove the generalized Boucksom–Chen theorem for ﬁltrations on the full
graded linear series, which suﬃces for our purpose. It is, however, easy to see that the techniques
apply to more general situations.
4                                               MINGCHEN XIA

  More generally, we introduce the notion of an Okounkov test curve (Deﬁnition 7.2) and generalize
Duistermaat–Heckman measures to this setting.
  When L is ample, this construction allows us to associate a Radon measure DH(η) on R with
each element η in the non-Archimedean space E 1 (Lan ) in the sense of [BJ22], see Deﬁnition 7.13.
The space E 1 (Lan ) can be seen as the completion of the space of test conﬁgurations.
Theorem 1.2. The Duistermaat–Heckman measure construction of test configurations as in
[WN12] admits a unique continuous extension DH : E 1 (Lan ) → M(R). Here M(R) is the space of
Radon measures on R.
   The Duistermaat–Heckman measure of a non-Archimedean metric is also constructed by Inoue
[Ino22] using a diﬀerent method. See Remark 7.17 for more details.
   In Theorem 7.16, we will furthermore prove that DH(η) contains a lot of interesting information
of η.
   In the last section, we interpret the partial Okounkov bodies in the toric setting. We prove the
following results:
Theorem 1.3. Let X be a smooth toric variety of dimension n and (L, φ) be a toric invariant
Hermitian big line bundle on X with positive volume. Fix a toric invariant admissible flag on X.
Recall that upon choosing a toric invariant rational section of L, φ can be identified with a convex
function φR on Rn . Then the partial Okounkov body ∆(L, φ) is naturally identified with the closure
of the image of ∇φR .
Theorem D. Let (Li , φi ) (i = 1, . . . , n) be toric invariant Hermitian big line bundles on X of pos-
itive volumes. If the toric invariant flag (Y• ) satisfies the additional condition: Yn is not contained
in the polar locus of any φi , then
                     Z
                          ddc φ1 ∧ · · · ∧ ddc φn = n! vol(∆(L1 , φ1 ), . . . , ∆(Ln , φn )).
                      X

   It is of interest to generalize Theorem D to the non-toric setting as well. As shown by Example 8.5,
the non-toric generalization has to involve all valuations instead of just one.
   Lastly, let us mention that our generalization of Boucksom–Chen theorem has important conse-
quences in Archimedean pluripotential theory as well. When applied to generalized deformation to
the normal cone in the sense of [Xia23b], it gives a number of interesting equidistribution results
of the jumping numbers of multiplier ideal sheaves. As a detailed investigation would lead us too
far away, we do not include these results in this paper.

1.3. Strategy of the proofs. We will sketch the proof of these theorems.
   The proof of Theorem A. In general, the graded linear space
                                                   ∞
                                                   M
                                    W (L, φ) :=          H0 (X, Lk ⊗ I(kφ))
                                                   k=0

is not an algebra and similarly Γ(L, φ) as deﬁned in (1.2) is not a semigroup. Thus, one can not
directly apply the theory of graded linear series or the theory of semigroups as in [LM09] and
[KK12].
   A key observation here is that although Γ(L, φ) is not a semigroup, it is not too far away from
being one.
   To make this precise, we introduce a pseudometric d on the space Ŝ of subsets of Zn+1 lying in
a suitable strictly convex cone:
                                                                                   
                             d(S, S ′ ) := lim k−n |Sk | + |Sk′ | − 2|Sk ∩ Sk′ | .
                                          k→∞
                                       PARTIAL OKOUNKOV BODIES                                       5

Let ∼ be the equivalence relation deﬁned by d. The classical Okounkov body construction associates
with each semigroup a convex body. As we will prove later, this map factorizes through the ∼-
equivalence classes, and it extends continuously to an almost semigroup, namely an object in Ŝ
which can be approximated by certain nice semigroups with respect to d.
  In order to deﬁne the Okounkov body of (L, φ), we will actually show that Γ(L, φ) is an almost
semigroup and we could simply deﬁne
                                            ∆(L, φ) := ∆(Γ(L, φ)).
The proof follows the same pattern as the proof in [DX21]. We proceed by approximations. We ﬁrst
consider the case where φ has analytic singularities. In this case, after taking a suitable resolution,
we can easily see that W (L, φ) can be approximated by graded linear series both from above and
from below. In the case of a singular φ with ddc φ being a Kähler current, we make use of analytic
approximations as in [DPS01; Cao14]. More precisely, take a quasi-equisingular approximation φj
of φ. Based on the convergence theorems proved in [DX21], we can show that Γ(L, φj ) converges to
Γ(L, φ) with respect to the pseudometric d, which enables us to conclude in this case. Finally, in
the general case, a trick discovered in [DDNL21b] and [DX21] enables us to reduce to the previous
case.
   Along the lines of the proof, we actually ﬁnd that Γ(L, φ) satisﬁes a stronger property (1.4). This
property is essential to the proof of Theorem B, we call it the Hausdorff convergence property.
   The proof of Theorem B. Recall that in the classical setting, we can read information about the
asymptotic base loci of L from the Okounkov body ∆(L) directly, see [CHPW18a]. In our setup,
the analogue says that the Okounkov body ∆(L, φ) gives information about the generic Lelong
numbers of φ. We will prove a qualitative version of Theorem B:
Theorem 1.4. Let E be a prime divisor over X. Let π : Z → X be a birational model of X such
that E is a divisor on Z. Take an admissible flag (Y• ) on Z with Y1 = E, then
                                        ν(φ, E) =         min           x1 .
                                                     x∈∆(π ∗ L,π ∗ φ)

   Here ν(φ, E) is the generic Lelong number of φ along E, deﬁned as the minimum of the Lelong
numbers ν(π ∗ φ, x) for all x ∈ E. The proof of Theorem 1.4 again follows the same pattern as in
the proof of Theorem A. With some eﬀorts, we can reduce the problem to the case where φ has
analytic singularities along some normal crossing Q-divisor on X and ddc φ is a Kähler current. In
this case, the desired result follows from a result proved in [Xia23b].
   The proofs of Theorem C and Theorem D. The proofs roughly follow the same pattern as
above. Namely, we ﬁrst handle the case of analytic singularities and then conclude the general case
by suitable approximations. We will not repeat the details here.
   As explained above, our approach to general psh singularities requires a number of approxima-
tions, this motivates the study of the metric geometry of the space of psh singularity types. We
prove the continuity of mixed masses under dS -approximations:
Theorem 1.5 (= Theorem 4.2). Let θi (i = 1, . . . , n) be smooth closed real (1, 1)-forms representing
big classes on a connected compact Kähler manifold X of dimension n. Let ϕki , ϕi ∈ PSH(X, θi )
                                             dS,θ
(i = 1, . . . , n, k ∈ N). Assume that ϕki −−−→
                                              i
                                                ϕi for all i as k → ∞. Then
                                Z                              Z
(1.8)                     lim       θ1,ϕk ∧ · · · ∧ θn,ϕkn =       θ1,ϕ1 ∧ · · · ∧ θn,ϕn .
                         k→∞ X          1
                                                               X

Here the Monge–Ampère operators are taken in the non-pluripolar sense.
  This theorem and its various consequences are indispensable in all of our proofs. They are of
independent interests as well.
6                                                   MINGCHEN XIA

1.4. Structure of the paper. In Section 2, we collect a few preliminaries.
   In Section 3, we study the Okounkov bodies of almost semigroups.
   In Section 4, we further develop the theory of dS -pseudometrics on the space of singularity types
initiated in [DDNL21b].
   In Section 5, we deﬁne partial Okounkov bodies associated with Hermitian pseudo-eﬀective line
bundles and prove a number of properties.
   In Section 6, we deﬁne and study Chebyshev transforms of continuous metrics.
   In Section 7, we generalize the theory of Boucksom–Chen and study the non-Archimedean
Duistermaat–Heckman measures.
   In Section 8, we give an explicit description of partial Okounkov bodies construction in terms of
the moment polytope in the toric situation.
1.5. Conventions. In this paper, Monge–Ampère operators θϕn refer to the non-pluripolar product
in the sense of [BEGZ10]. The group Zn is always endowed with the lexicographic order. A line
bundle always refers to a holomorphic line bundle. We do not distinguish a line bundle and the
associated invertible sheaf. When talking about a birational modiﬁcation (resolution) π : Y → X,
we always assume that Y is smooth and π is projective. We follow the convention that ddc = 2π
                                                                                            i
                                                                                              ∂∂.
1.6. Acknowledgements. I beneﬁted a lot from discussions with David Witt Nyström, Chen
Jiang, Sébastien Boucksom,Yi Yao, Jian Xiao, Tamás Darvas, Kewei Zhang, Longke Tang and
Rémi Reboulet. I would like to thank especially Yi Yao for explaining his computations in the toric
setting to me, Chen Jiang for providing Example 8.5 and Yaxiong Liu for pointing out a number
of typos in the arXiv version.
   I also want to express my gratitude to the referees for numerous valuable comments helping to
improve this paper in many aspects.
   The author is supported by Knut och Alice Wallenbergs Stiftelse grant KAW 2021.0231.

                                               2. Preliminaries
2.1. Hausdorff metric of convex bodies. In this section, we recall the theory of Hausdorﬀ
metrics on the set of convex bodies following [Sch14, Section 1.8]. Fix n ∈ N. Recall that a convex
body in Rn is a non-empty compact convex subset of Rn , which may have empty interior. Let Kn
denote the set of convex bodies in Rn . We will ﬁx the Lebesgue measure dλ on Rn , normalized so
that the unit cube has volume 1.
   Recall the deﬁnition of the Hausdorﬀ metric between K1 , K2 ∈ Kn :
                                          (                                              )
                   dn (K1 , K2 ) := max       sup    inf |x1 − x2 |, sup    inf |x1 − x2 | .
                                          x1 ∈K1 x2 ∈K2             x2 ∈K2 x1 ∈K1

We extend dn to an extended metric on Kn ∪ {∅} by setting
                                                    dn (K, ∅) = ∞
for all K ∈ Kn .
Theorem 2.1. The metric space (Kn , dn ) is complete.
Theorem 2.2 (Blaschke selection theorem). Every bounded sequence in Kn has a convergent sub-
sequence.
Theorem 2.3. The Lebesgue volume vol : Kn → R≥0 is continuous.
                                                              d
Theorem 2.4. Let Ki , K ∈ Kn (i ∈ N). Then Ki −→       n
                                                         K if and only if the following conditions
hold
    (1) Each point x ∈ K is the limit of a sequence xi ∈ Ki .
                                       PARTIAL OKOUNKOV BODIES                                               7

    (2) The limit of any convergent sequence (xij )j∈N with xij ∈ Kij lies in K, where ij is a
        subsequence of 1, 2, . . ..
  The proofs of all these results can be found in [Sch14, Section 1.8].
Lemma 2.5. Let K0 , K1 ∈ Kn . Assume that K0 ⊆ K1 and
                                           vol K0 = vol K1 > 0.
Then K0 = K1 .
Proof. In fact, if K1 6= K0 , then K1 \ K0 is a non-empty open subset of K1 . As vol K1 > 0,
(K1 \ K0 ) ∩ Int K1 6= ∅. Thus, vol K1 > vol K0 , which is a contradiction.
                                                                                          
  Let K ∈ Kn be a convex body with positive volume. For δ > 0 small enough, let K δ := {x ∈ K :
d(x, ∂K) ≥ δ}. Then Kδ ∈ Kn for δ small enough.
Lemma 2.6. Let K ∈ Kn be a convex body with positive volume and K ′ ∈ Kn . Assume that for
                                                                      1/2 −1
some large enough k ∈ Z>0 , K ′ contains K ∩ (k−1 Z)n , then K ′ ⊇ K n k .
                     1/2 −1
Proof. Let x ∈ K n k , by assumption, the closed ball B with center x and radius n1/2 k−1 is
contained in K. Observe that x can be written as a convex combination of points in B ∩ (k−1 Z)n ,
which are contained in K ′ by assumption. It follows that x ∈ K ′ .                           
  Given a sequence of convex bodies Ki (i ∈ N), we set
                                                       ∞ \
                                                       [
                                            lim Ki =             Kj .
                                           i→∞         i=0 j≥i

  Suppose K is the limit of a subsequence of Ki , we have
(2.1)                                           lim Ki ⊆ K.
                                               i→∞
This is a simple consequence of Theorem 2.4.
2.2. Admissible flags and valuations. Let X be an irreducible normal projective variety of
dimension n.
Definition 2.7. An admissible flag (Y• ) on X is a ﬂag of subvarieties
                                         X = Y0 ⊇ Y1 ⊇ · · · ⊇ Yn
such that Yi is irreducible of codimension i and smooth at the point Yn .
   Given any admissible ﬂag (Y• ), we can deﬁne a rank n valuation ν(Y• ) : C(X)× → Zn as in
[LM09]. Here we consider Zn as a totally ordered Abelian group with the lexicographic order. We
recall the deﬁnition: let s ∈ C(X)× . Let ν1 (s) = ordY1 s. After localization around Yn , we can take
a local deﬁning equation t1 of Y1 , set s1 = (s(t1 )−ν1 (s) )|Y1 . Then s1 ∈ C(Y1 ). We can repeat this
construction with Y2 in place of Y1 to get ν2 (s) and s2 . Repeating this construction n times, we
get ν(Y• ) (s) = ν(s) = (ν1 (s), ν2 (s), . . . , νn (s)) ∈ Zn . It is easy to verify that ν is indeed a rank n
valuation.
Remark 2.8. Conversely, by a theorem of Abhyankar, any valuation of C(X) with Noetherian
valuation ring of rank n is equivalent to a valuation taking value in Zn , see [FK18, Chapter 0,
Theorem 6.5.2]. As shown in [CFKL+17, Theorem 2.9], any such valuation is equivalent to (but
not necessarily equal to) a valuation induced by an admissible ﬂag on a birational modiﬁcation of
X. Here two valuations ν, ν ′ with value in Zn are equivalent if one can ﬁnd a matrix G of the form
I + N , where N is strictly upper triangular with integral entries, such that ν ′ = Gν.
8                                            MINGCHEN XIA

2.3. Model potentials and I-model potentials. Let X be a connected compact Kähler mani-
fold of dimension n and θ be a smooth closed real (1, 1)-form representing a (1, 1)-cohomology class
[θ]. Deﬁne Vθ := sup{ϕ ∈ PSH(X, θ) : ϕ ≤ 0}. For any two ϕ, ψ ∈ PSH(X, θ), we say ϕ is more
singular than ψ and write [ϕ]  [ψ] if there is a constant C such that ϕ ≤ ψ + C. When ϕ  ψ
and ψ  ϕ, we say that they have the same singularity type. We write θϕ = θ + ddc ϕ.
Definition 2.9. Let ϕ ∈ PSH(X, θ). Deﬁne
                                                                 Z                       Z                      
(2.2)       θ
           C [ϕ] := sup* ψ ∈ PSH(X, θ) : [ϕ]  [ψ], ψ ≤ 0,                θϕk ∧ θVn−k
                                                                                   θ
                                                                                      =       θψk ∧ θVn−k
                                                                                                       θ
                                                                                                          , ∀k       .
                                                                      X                   X
If C θ [ϕ] = ϕ, we say ϕ is a model potential. We omit θ from the notation if there is no risk of
confusion.
  Here and in the sequel the Monge–Ampère type operators are taken in the non-pluripolar sense
[BEGZ10].
Proposition 2.10 ([DDNL21b, R Proposition   2.6]). For any ϕ ∈ PSH(X, θ), C θ [ϕ] is a model
potential in PSH(X, θ). When X θϕn > 0 we have
                                             C θ [ϕ] = P θ [ϕ],
where
(2.3)                      P θ [ϕ] := sup* {ψ ∈ PSH(X, θ) : [ψ]  [ϕ], ψ ≤ 0} .
In general, we only have
(2.4)                              C θ [ϕ] = lim P θ [(1 − ǫ)ϕ + ǫVθ ].
                                            ǫ→0+

    We omit θ from the notation P θ [ϕ] if there is no risk of confusion.
Definition 2.11. A birational model of X is a projective birational morphism π : Y → X from a
smooth projective variety Y to X.
   Recall that I(ϕ) denotes the multiplier ideal sheaf of a qpsh function ϕ on X in the sense of
Nadel, namely the coherent subsheaf of OX consisting of functions f such that |f |2 exp(−ϕ) is
locally integrable.
Definition 2.12. Let ϕ, ψ be two quasi-psh functions, we say ϕ I ψ if the following equivalent
conditions are satisﬁed:
   (1) I(kϕ) ⊆ I(kψ) for all real k > 0.
   (2) I(kϕ) ⊆ I(kψ) for all integer k > 0.
   (3) For any birational model π : Y → X and any y ∈ Y , we have ν(π ∗ ϕ, y) ≥ ν(π ∗ ψ, y).
The equivalence between (1) and (3) is just [DX22, Corollary 2.16]. The equivalence between (2)
and (3) follows from [DX22, Proposition 2.14].
  We say ϕ ∼I ψ if ϕ I ψ and ψ I ϕ.
  Given any ϕ ∈ PSH(X, θ), we deﬁne
                           P θ [ϕ]I := sup {ψ ∈ PSH(X, θ) : ψ I ϕ, ψ ≤ 0} .
We omit θ when there is no risk of confusion. We say ϕ is I-model if ϕ = P [ϕ]I .
   It is shown in [DX22, Proposition 2.18] that P [ϕ]I ∈ PSH(X, θ) and ϕ ∼I P [ϕ]I . Moreover,
P [ϕ]I is always I-model. We can also talk about the ∼I relation of two psh metric on L in the
obvious manner.
   Typical model potentials are not I-model, however, the converse is true:
Proposition 2.13. If ψ ∈ PSH(X, θ) is an I-model potential then it is model.
                                    PARTIAL OKOUNKOV BODIES                                         9

Proof. We need to show that ψ ∼I C[ψ]. Let π : Z → X be a birational modiﬁcation. Let z ∈ Z.
As ψ ≤ C[ψ] + C for some constant C, it suﬃces to show that
                                        ν(C[ψ], z) ≥ ν(ψ, z).
Here ν(ψ, z) denotes the Lelong number of π ∗ ψ at z. By (2.4) and the upper semi-continuity of
Lelong numbers (see [GZ17, Page 73, Exercise 2.7]), we ﬁnd
          ν(C[ψ], z) ≥ lim ν(P [(1 − ǫ)ψ + ǫVθ ], z) = lim ν((1 − ǫ)ψ + ǫVθ , z) = ν(ψ, z).
                       ǫ→0+                                   ǫ→0+
We conclude our assertion.                                                                         
2.4. Potentials with analytic singularities.
Definition 2.14. A quasi-plurisubharmonic function (quasi-psh) ϕ on X is said to have analytic
singularities if for each x ∈ X, there is a neighborhood Ux ⊆ X of x with respect to the Euclidean
topology, such that on Ux ,
                                                               
                                                     Nx
                                                     X
(2.5)                                ϕ = c log            |fj |2  + ψ,
                                                     j=1

where c ∈ Q≥0 , the fj ’s are analytic functions on Ux , Nx ∈ Z>0 is an integer depending on x,
ψ ∈ L∞ (Ux ).
                                                                                    P
Definition 2.15. Let D be an eﬀective normal crossing R-divisor on X. Let D = i ai Di with Di
being prime divisors and ai ∈ R>0 . We say that a quasi-psh function ϕ has analytic singularities
along D if locally (in the Euclidean topology),
                                            X
                                       ϕ=        ai log |si |2 + ψ,
                                             i
where si is a local holomorphic function deﬁning Di , ψ is a bounded function.
   In the sequel, when we talk about a normal crossing divisor, we always assume that it is eﬀective.
   Note that a potential with analytic singularities along a normal crossing Q-divisor has analytic
singularities in the sense of Deﬁnition 2.14.
   For any quasi-psh function ϕ on X with analytic singularities, there is always a birational model
π : Y → X such that π ∗ ϕ has analytic singularities along a normal crossing Q-divisor on Y . See
[MM07, Lemma 2.3.19] for example. We remind the readers that in [MM07], the deﬁnition of
analytic singularities diﬀers slightly from ours: they require the remainder ψ to be smooth instead
of just bounded. However, the proof of [MM07, Lemma 2.3.19] works verbatim with our deﬁnition.
2.5. Quasi-equisingular approximations. We recall the concept of quasi-equisingular approxi-
mations in the sense of [Cao14; DPS01].
   Let X be a connected compact Kähler manifold of dimension n and θ (resp. θi , i = 1, . . . , n)
be a smooth real (1, 1)-form representing a pseudo-eﬀective (1, 1)-cohomology class [θ] (resp. [θi ]).
Take a Kähler form ω on X.
Definition 2.16. Let ϕ ∈ PSH(X, θ). A quasi-equisingular approximation is a sequence ϕj ∈
PSH(X, θ + ǫj ω) with ǫj → 0 such that
   (1) ϕj → ϕ in L1 .
   (2) ϕj has analytic singularities.
   (3) ϕj+1 ≤ ϕj .
   (4) For any δ > 0, k > 0, there is j0 > 0 such that for j ≥ j0 ,
                                 I(k(1 + δ)ϕj ) ⊆ I(kϕ) ⊆ I(kϕj ).
  The existence of a quasi-equisingular approximation follows from the arguments in [Cao14;
Dem15; DPS01].
10                                                      MINGCHEN XIA

2.6. Volumes of Hermitian pseudo-effective line bundles. Let X be a smooth irreducible
projective variety of dimension n.
Definition 2.17. A Hermitian pseudo-effective(psef) line bundle on X is a pair (L, φ), where L is
a pseudo-eﬀective line bundle on X and φ is a psh metric on L.
  When L is big, we say (L, φ) is a Hermitian big line bundle.
  Let (L, φ) be a Hermitian psef line bundle on X. In this section, we recall the main results in
[DX22; DX21] concerning the volume of (L, φ).
Definition 2.18. The volume of (L, φ) is deﬁned as
                                                             1 0      k
                                                                                
                                   vol(L, φ) := lim             h X, L   ⊗ I(kφ)  .
                                                        k→∞ k n

  The existence of the limit follows from [DX21, Theorem 1.1].
  We take a smooth Hermitian metric h on L. Set θ = c1 (L, h). Then we can identify φ with a
θ-psh function ϕ, namely φ = h exp(−ϕ).
Theorem 2.19 ([DX21, Theorem 1.1]). Under the above assumptions,
                                                                      Z
                                                              1
                                                  vol(L, φ) =              θPn [ϕ]I .
                                                              n!       X

   We argue that vol deserves the name volume by proving that it satisﬁes the Brunn–Minkowski
inequality.
Corollary 2.20. Let (L, φ), (L, φ′ ) be two Hermitian psef line bundles on X. Then
(2.6)                      vol(L + L′ , φ + φ′ )1/n ≥ vol(L, φ)1/n + vol(L′ , φ′ )1/n .
Proof. Fix a smooth Hermitian metric h′ on L′ with θ ′ = c1 (L′ , h′ ). We identify φ′ with ϕ′ ∈
PSH(X, θ ′ ). By Theorem 2.19, (2.6) is equivalent to
          Z                                           n 1/n       Z                    1/n       Z                       1/n
                       ′       c   θ+θ ′            ′
                 θ + θ + dd P              [ϕ + ϕ ]I              ≥            θPn θ [ϕ]I          +         θ ′nP θ′ [ϕ′ ]            .
                                                                                                                            I
             X                                                             X                            X
Observe that
                                              ′                                       ′
                                      P θ+θ [ϕ + ϕ′ ]I ≥ P θ [ϕ]I + P θ [ϕ′ ]I .
Thus, by the monotonicity theorem of [WN19], it suﬃces to show that
        Z                                                  n 1/n       Z                    1/n       Z                        1/n
                   ′       c   θ              c    θ′    ′
               θ + θ + dd P [ϕ]I + dd P [ϕ ]I                          ≥            θPn θ [ϕ]I          +          θ ′nP θ′ [ϕ′ ]            .
                                                                                                                                  I
         X                                                                      X                              X

This follows from [DDNL21a, Theorem 6.1].                                                                                                        

2.7. Non-Archimedean pluripotential theory. In this section, we brieﬂy recall the notion of
Berkovich analytiﬁcation of a smooth complex projective variety and the pluripotential theory in
the sense of Boucksom–Jonsson [BJ22] on it.
   For simplicity, we assume that X is a connected smooth projective variety of dimension n and
L is an ample line bundle on X.
   The set of real valuations on C(X) trivial on C is denoted by X val . This set can be deﬁned in
the same way for non-smooth varieties as well.
   The center of a valuation v is the scheme-theoretic point c = c(v) of X such that v ≥ 0 on OX,c
and v > 0 on the maximal ideal mX,c of OX,c . The center exists and is unique.
   Let X an denote the Berkovich analytiﬁcation X an of X with respect to the trivial valuation
on C. As a set, X an is the set of semi-valuations on X, in other words, real-valued valuations
                                            PARTIAL OKOUNKOV BODIES                                                11

v on irreducible reduced subvarieties Y in X that is trivial on C. We call Y the support of the
semi-valuation v. In other words,               a
                                         X an =   Y val .
                                                              Y
The Berkovich space X an admits a natural topology, called the Berkovich topology and a sheaf of
analytic functions. The natural morphism of ringed spaces X an → X allows us to pull-back L to
an invertible sheaf Lan on X an . See [Ber90] for more details.
   In [BJ22], Boucksom–Jonsson developed a pluripotential theory with respect to (X an , Lan ), simi-
lar to its complex counterpart. In particular, there is a natural notion of plurisubharmonic metrics
on Lan . In [BJ22, Section 7.1], Boucksom–Jonsson deﬁned the notion of energy pairings (ϕ0 , . . . , ϕn )
between (n+1) plurisubharmonic metrics ϕ0 , . . . , ϕn on Lan . One can then deﬁne the space E 1 (Lan )
of ﬁnite energy metrics as the space of plurisubharmonic functions ϕ on Lan such that
                                              1
                                   E(ϕ) :=        (ϕ, . . . , ϕ) > −∞.
                                           n+1
Note that our deﬁnition of E diﬀers from the deﬁnition of [BJ22] by a multiple V1 . We will explain
the relation between the non-Archimedean pluripotential theory and the complex pluripotential
theory in Section 7.4.

                          3. The Okounkov bodies of almost semigroups
  Fix an integer n ≥ 0. Fix a closed convex cone C ⊆ Rn × R≥0 such that C ∩ {xn+1 = 0} = {0}.
Here xn+1 is the last coordinate of Rn+1 .

3.1. Generality on semigroups. Write Ŝ(C) for the set of subsets of C ∩ Zn+1 and S(C) for the
set of sub-semigroups S ⊆ C ∩ Zn+1 . For each k ∈ N and S ∈ Ŝ(C), we write
                                           Sk := {x ∈ Zn : (x, k) ∈ S} .
Note that Sk is a ﬁnite set by our assumption on C.
  We introduce a pseudometric on Ŝ(C) as follows:
                               d(S, S ′ ) := lim k−n (|Sk | + |Sk′ | − 2|(S ∩ S ′ )k |).
                                             k→∞
Here | • | denotes the cardinality of a ﬁnite set.
Lemma 3.1. The above defined d is a pseudometric on Ŝ(C).
Proof. Only the triangle inequality needs to be argued. Take S, S ′ , S ′′ ∈ Ŝ(C). We claim that for
any k ∈ N,
            |Sk | + |Sk′ | − 2|Sk ∩ Sk′ | + |Sk′′ | + |Sk′ | − 2|Sk′′ ∩ Sk′ | ≥ |Sk | + |Sk′′ | − 2|Sk ∩ Sk′′ |.
From this the triangle inequality follows. To argue the claim, we rearrange it to the following form:
                                   |Sk′ | − |Sk ∩ Sk′ | ≥ |Sk′ ∩ Sk′′ | − |Sk ∩ Sk′′ |,
which is obvious.                                                                                                  
  Given S, S ′ ∈ Ŝ(C), we say S is equivalent to S ′ and write S ∼ S ′ if d(S, S ′ ) = 0. This is an
equivalence relation by Lemma 3.1.
Lemma 3.2. Given S, S ′ , S ′′ ∈ Ŝ(C), we have
                                          d(S ∩ S ′′ , S ′ ∩ S ′′ ) ≤ d(S, S ′ ).
In particular, if S i , S ′i ∈ Ŝ(C) (i ∈ N) and S i → S, S ′i → S ′ , then
                                                  S i ∩ S ′i → S ∩ S ′ .
12                                                      MINGCHEN XIA

Proof. Observe that for any k ∈ N,
                                   |Sk ∩ Sk′′ | − |Sk ∩ Sk′ ∩ Sk′′ | ≤ |Sk | − |Sk ∩ Sk′ |.
The same holds if we interchange S with S ′ . It follows that
                     |Sk ∩ Sk′′ | + |Sk′ ∩ Sk′′ | − 2|Sk ∩ Sk′ ∩ Sk′′ | ≤ |Sk | + |Sk′ | − 2|Sk ∩ Sk′ |.
The ﬁrst assertion follows.
  Next we compute
           d(S i ∩ S ′i , S ∩ S ′ ) ≤ d(S i ∩ S ′i , S i ∩ S ′ ) + d(S i ∩ S ′ , S ∩ S ′ ) ≤ d(S ′i , S ′ ) + d(S i , S)
and the second assertion follows.                                                                                          
     The volume of S ∈ S(C) is deﬁned as
                                      vol S := lim (ka)−n |Ska | = lim k−n |Sk |,
                                                 k→∞                        k→∞

where a is a suﬃciently divisible positive integer. The existence of the limit and its independence
from a both follow from the more precise result [KK12, Theorem 2].
Lemma 3.3. Let S, S ′ ∈ S(C), then
                                                | vol S − vol S ′ | ≤ d(S, S ′ ).
Proof. By deﬁnition, we have
                                       d(S, S ′ ) ≥ vol S + vol S ′ − 2 vol(S ∩ S ′ ).
It follows that vol S − vol S ′ ≤ d(S, S ′ ) and vol S ′ − vol S ≤ d(S, S ′ ).                                             

  We deﬁne S(C) as the closure of S(C) in Ŝ(C) with respect to the topology deﬁned by the
pseudometric d. By Lemma 3.3, vol : S(C) → R admits a unique 1-Lipschitz extension to
(3.1)                                                  vol : S(C) → R.
Lemma 3.4. Suppose that S, S ′ ∈ S(C) and S ⊆ S ′ . Then
                                                        vol S ≤ vol S ′ .
Proof. Take sequences S j , S ′j in S(C) such that S j → S, S ′j → S ′ . By Lemma 3.2, after replacing
S j by S j ∩ S ′j , we may assume that S j ⊆ S ′j for each j. Then our assertion follows easily.     

3.2. Okounkov bodies of semigroups. Given S ∈ Ŝ(C), we will write C(S) ⊆ C for the closed
convex cone generated by S ∪ {0}. Moreover, for each k ∈ Z>0 , we deﬁne
                                                        n                           o
                                    ∆k (S) := Conv k−1 x ∈ Rn : x ∈ Sk ⊆ Rn .
Here Conv denotes the convex hull.
Definition 3.5. Let S ′ (C) be the subset of S(C) consisting of semigroups S such that S generates
Zn+1 (as an Abelian group).
  Note that for any S ∈ S ′ (C), the cone C(S) has full dimension (i.e. the topological interior is
non-empty). Given a full-dimensional subcone C ′ ⊆ C, it is clear that C ′ ∩ Zn+1 ∈ S ′ (C).
  This class behaves well under intersections:
Lemma 3.6. Let S, S ′ ∈ S ′ (C). Assume that vol(S ∩ S ′ ) > 0, then S ∩ S ′ ∈ S ′ (C).
     The lemma obviously fails if vol(S ∩ S ′ ) = 0.
                                     PARTIAL OKOUNKOV BODIES                                        13

Proof. We ﬁrst observe that the cone C(S) ∩ C(S ′ ) has full dimension since otherwise vol(S ∩ S ′ ) =
0. Take a full-dimensional subcone C ′ in C(S) ∩ C(S ′ ) such that C ′ intersects the boundary of
C(S) ∩ C(S ′ ) only at 0. It follows from [KK12, Theorem 1] that there is an integer N > 0
such that for any x ∈ Zn+1 ∩ C ′ with Euclidean norm no less than N lies in S ∩ S ′ . Therefore,
S ∩ S ′ ∈ S ′ (C).                                                                                   
  We recall the following deﬁnition from [KK12].
Definition 3.7. Given S ∈ S ′ (C), its Okounkov body is deﬁned as follows
                                 ∆(S) := {x ∈ Rn : (x, 1) ∈ C(S)} .
Theorem 3.8. For each S ∈ S ′ (C), we have
(3.2)                           vol S = lim k−n |Sk | = vol ∆(S) > 0.
                                         k→∞
Moreover, as k → ∞,
                                                    d
                                                    n
(3.3)                                       ∆k (S) −→ ∆(S).
  This is essentially proved in [WN14, Lemma 4.8], which itself follows from a theorem of Kho-
vanskii [Kho92]. We remind the readers that (3.2) fails for a general W ∈ S(C), see [KK12,
Theorem 2].
Proof. The equalities (3.2) follow from the general theorem [KK12, Theorem 2].
   It remains to prove (3.3). By the argument of [WN14, Lemma 4.8], for any compact set K ⊆
Int ∆(S), there is k0 > 0 such that for any k ≥ k0 , α ∈ K ∩ (k−1 Z)n implies that α ∈ ∆k (S).
   In particular, taking K = ∆(S)δ for any δ > 0 and applying Lemma 2.6, we ﬁnd
                                   dn (∆(S), ∆k (S)) ≤ n1/2 k−1 + δ
when k is large enough. This implies (3.3).                                                         
Corollary 3.9. Let S, S ′ ∈ S ′ (C). Assume that vol(S ∩ S ′ ) > 0, then we have
                             d(S, S ′ ) = vol(S) + vol(S ′ ) − 2 vol(S ∩ S ′ ).
Proof. This is a direct consequence of Lemma 3.6 and (3.2).                                         
Lemma 3.10. Given S ∈ S ′ (C), we have S ∼ Reg(S).
  Recall that the regularization Reg(S) of S is deﬁned as C(S) ∩ Zn+1 .
Proof. Since S and Reg(S) have the same Okounkov body, we have vol S = vol Reg(S) by Theo-
rem 3.8. By Corollary 3.9 again,
                               d(Reg(S), S) = vol Reg(S) − vol S = 0.
                                                                                                    
Lemma 3.11. Let S, S ′ ∈ S ′ (C). Assume that d(S, S ′ ) = 0, then ∆(S) = ∆(S ′ ).
Proof. Observe that vol(S ∩ S ′ ) > 0, as otherwise
                                     d(S, S ′ ) ≥ vol S + vol S ′ > 0,
which is a contradiction.
   It follows from Lemma 3.6 that S ∩ S ′ ∈ S ′ (C). It suﬃces to show that ∆(S) = ∆(S ∩ S ′ ). In
fact, suppose that this holds, since vol ∆(S ′ ) = vol S ′ = vol S = vol ∆(S), the inclusion ∆(S ′ ) ⊇
∆(S ∩ S ′ ) = ∆(S) is an equality.
   By Lemma 3.2, we can therefore replace S ′ by S ∩ S ′ and assume that S ⊇ S ′ . Then clearly
∆(S) ⊇ ∆(S ′ ). By (3.2),
                                       vol ∆(S) = vol ∆(S ′ ).
Thus, ∆(S) = ∆(S ′ ) by Lemma 2.5.                                                                   
14                                                    MINGCHEN XIA

Lemma 3.12. Suppose that S i ∈ S ′ (C) is a decreasing sequence such that
                                                      lim vol S i > 0.
                                                     i→∞

Then there is S ∈ S ′ (C) such that S i → S.
                                                        T     i
  In general, one cannot simply take S =                    iS .   For example, consider the sequence S i = S 1 ∩
{xn+1 ≥ i}.
Proof. By Lemma 3.10, we may replace S i by its regularization and assume that S i = C(S i ) ∩ Zn+1 .
We deﬁne                                           !   ∞
                                                       \
                                               S=           C(S i ) ∩ Zn+1 .
                                            i=1
        T∞
Since i=1    C(S ) is a full-dimensional cone by assumption, we have S ∈ S ′ (C).
                i                                                                                          By Corollary 3.9
and Theorem 3.8, we can compute the distance
                               d(S, S i ) = vol S i − vol S = vol ∆(S i ) − vol ∆(S),
which tends to 0 by construction.                                                                                        
3.3. Okounkov bodies of almost semigroups.
Definition 3.13. We deﬁne S ′ (C)>0 as elements in the closure of S ′ (C) in Ŝ(C) with positive
volume. An element in S ′ (C)>0 is called an almost semigroup in C.
     Recall that the volume here is deﬁned in (3.1).
     Our goal is to prove the following theorem:
Theorem 3.14. The Okounkov body map ∆ : S ′ (C) → Kn as defined in Definition 3.7 admits a
unique continuous extension
(3.4)                                              ∆ : S ′ (C)>0 → Kn .
Moreover, for any S ∈ S ′ (C)>0 , we have
(3.5)                                               vol S = vol ∆(S).
Proof. The uniqueness of the extension is clear as long as it exists. Moreover, (3.5) follows eas-
ily from Theorem 3.8 and Theorem 2.3 by continuity. It remains to argue the existence of the
continuous extension. We ﬁrst construct an extension and prove its continuity.
   Step 1. We construct the desired map (3.4). Let S ∈ S ′ (C)>0 . We wish to construct a convex
body ∆(S) ∈ Kn .
   Let S i ∈ S ′ (C) be a sequence that converges to S such that
                                                    d(S i , S i+1 ) ≤ 2−i .
For each i, j ≥ 0, we introduce
                                              S i,j = S i ∩ S i+1 · · · ∩ S i+j .
Then by Lemma 3.2,
                                      d(S i,j , S i,j+1 ) ≤ 2−i−j .
Take i0 > 0 large enough so that for i ≥ i0 , vol S i > 2−1 vol S and 22−i < vol S and hence
               vol S i − vol S i,j ≤ d(S i,0 , S i,1 ) + d(S i,1 , S i,2 ) + · · · + d(S i,j−1 , S i,j ) ≤ 21−i .
It follows that vol S i,j > 2−1 vol S − 21−i > 0 whenever i ≥ i0 . In particular, by Lemma 3.6,
S i,j ∈ S ′ (C) for i ≥ i0 .
    By Lemma 3.12, for i ≥ i0 , there exists T i ∈ S ′ (C) such that S i,j → T i as j → ∞. Moreover,
                d(T i , S) = lim d(S i,j , S) ≤ lim d(S i,j , S i ) + d(S i , S) ≤ 21−i + d(S i , S).
                              j→∞                    j→∞
                                      PARTIAL OKOUNKOV BODIES                                           15

Therefore, T i → S. We then deﬁne
                                                    ∞
                                                    [
                                          ∆(S) :=          ∆(T i ).
                                                    i=i0

In other words, we have deﬁned
                                          ∆(S) := lim ∆(S i ).
                                                    i→∞
This is an honest limit: if ∆ is the limit of a subsequence of ∆(S i ), then ∆(S) ⊆ ∆ by (2.1).
Comparing the volumes, we ﬁnd that equality holds. So by Theorem 2.2,
(3.6)                                     ∆(S) = lim ∆(S i ).
                                                    i→∞

   Next we claim that ∆(S) as deﬁned above does not depend on the choice of the sequence S i . In
fact, suppose that S ′i ∈ S ′ (C) is another sequence satisfying the same conditions as S i . The same
holds for Ri := S i+1 ∩ S ′i+1 . It follows that
                                        lim ∆(Ri ) ⊆ lim ∆(S i ).
                                       i→∞              i→∞

Comparing the volumes, we ﬁnd that equality holds. The same is true with S ′i in place of S i . So
we conclude that ∆(S) as in (3.6) does not depend on the choices we made.
   Step 2. It remains to prove the continuity of ∆ deﬁned in Step 1. Suppose that S i ∈ S ′ (C)>0
is a sequence with limit S ∈ S ′ (C)>0 . We want to show that
                                                    d
(3.7)                                        ∆(S i ) −→
                                                      n
                                                        ∆(S).
   We ﬁrst reduce to the case where S i ∈ S ′ (C). By (3.6), for each i, we can choose T i ∈ S ′ (C)
                                                                                          dn
such that d(S i , T i ) < 2−i and dn (∆(S i ), ∆(T i )) < 2−i . If we have shown ∆(T i ) −→  ∆(S), then
(3.7) follows immediately.
   Next we reduce to the case where d(S i , S i+1 ) ≤ 2−i . In fact, thanks to Theorem 2.2, in order to
prove (3.7), it suﬃces to show that each subsequence of ∆(S i ) admits a subsequence that converges
to ∆(S). Hence, we easily reduce to the required case.
   After these reductions, (3.7) is nothing but (3.6).                                               
Corollary 3.15. Suppose that S, S ′ ∈ S ′ (C)>0 with S ⊆ S ′ , then
(3.8)                                        ∆(S) ⊆ ∆(S ′ ).
Proof. Let S j , S ′j ∈ S ′ (C) be elements such that S j → S, S ′j → S ′ . Then it follows from Lemma 3.2
that S j ∩ S ′j → S. Since vol is continuous, for large j, S j ∩ S ′j has positive volume and hence lies
in S ′ (C) by Lemma 3.6. We may therefore replace S j by S j ∩ S ′j and assume that S j ⊆ S ′j . Hence
(3.8) follows from the continuity of ∆ proved in Theorem 3.14.                                          
Remark 3.16. As the readers can easily verify, the construction of ∆ is independent of the choice
of C in the following sense: Suppose that C ′ is another cone satisfying the same assumptions as C
and C ′ ⊇ C, then the Okounkov body map ∆ : S ′ (C ′ )>0 → Kn is an extension of the corresponding
map (3.4). We will constantly use this fact without further explanations.

                      4. The metric on the space of singularity types
  Let X be a connected compact Kähler manifold of dimension n and θ (resp. θi , i = 1, . . . , n)
be a smooth real (1, 1)-form representing a big (1, 1)-cohomology class [θ] (resp. [θi ]). Let ω be a
Kähler form on X.
  In this section, we develop further the metric geometry on the space of singularity types of
quasi-psh functions, initiated in [DDNL21b] and studied further in [DX22].
16                                                           MINGCHEN XIA

   As explained in [DDNL21b, Section 3], one can introduce a pseudometric dS on the set of
singularity types of functions in PSH(X, θ). In particular, dS lifts to a pseudometric on PSH(X, θ)
as well. We do not recall the precise deﬁnition, as the following double inequality from [DDNL21b,
Proposition 3.5] will be enough for us. For any ϕ, ψ ∈ PSH(X, θ) we have
                       n  Z
                       X                                                    Z                            Z               
(4.1)    dS (ϕ, ψ) ≤                2         i
                                             θmax{ϕ,ψ} ∧ θVn−i
                                                            θ
                                                               −                    θϕi ∧ θVn−i
                                                                                             θ
                                                                                                −               θψi ∧ θVn−i
                                                                                                                         θ
                                                                                                                            ≤ C0 dS (ϕ, ψ),
                       i=0              X                                       X                         X

where C0 > 1 is a constant depending only on n. In addition, dS (ϕ, ψ) = 0 if and only if
                                                              C[ϕ] = C[ψ].
When there is a risk of confusion, we write dS,θ instead of dS .
Lemma 4.1. Let ϕi ∈ PSH(X, θi ) (i = 1, . . . , n). Then
                                Z                                       Z
                                        θ1,ϕ1 ∧ · · · ∧ θn,ϕn =                 θ1,C[ϕ1 ] ∧ · · · ∧ θn,C[ϕn] .
                                 X                                        X

Proof. From the deﬁnition (2.2), we have [u]  [C[u]], the ≤ direction is obvious. For the reverse
direction, recall that C[ϕi ] = limǫ→0+ P [(1 − ǫ)ϕi + ǫVθi ]. Thus, for ǫ ∈ (0, 1),
                       Z                                                                    Z
                                                                                        n
                               θ1,C[ϕ1 ] ∧ · · · ∧ θn,C[ϕn] ≥ (1 − ǫ)                             θ1,ϕ1 ∧ · · · ∧ θn,ϕn .
                           X                                                                 X
Letting ǫ → 0+, we conclude.                                                                                                                  
                                                                                                                             dS,θ
Theorem 4.2. Let ϕki , ϕi ∈ PSH(X, θi ) (i = 1, . . . , n, k ∈ N). Assume that ϕki −−−→
                                                                                      i
                                                                                        ϕi as k → ∞.
Then
                                         Z                                          Z
(4.2)                           lim            θ1,ϕk ∧ · · · ∧ θn,ϕkn =                  θ1,ϕ1 ∧ · · · ∧ θn,ϕn .
                               k→∞ X               1
                                                                                     X

Proof. By Lemma 4.1 and [DDNL21b, Theorem 3.3], we may assume that ϕki and ϕk are model
potentials.
  Step 1. We assume that there is a constant δ > 0, such that for all i and k,
                                                              Z
                                                                       n
                                                                      θi,ϕ k > δ.
                                                               X            i
                                                                                                                   R
In order to show (4.2), it suﬃces to prove that any subsequence of X θ1,ϕk ∧ · · · ∧ θn,ϕkn has a
                                     R                                           1
converging subsequence with limit X θ1,ϕ1 ∧ · · · ∧ θn,ϕn . Thus, by [DDNL21b, Theorem 5.6], we
may assume that for each ﬁxed i, ϕki is either increasing or decreasing. We may assume that for
i ≤ i0 , the sequence is decreasing and for i > i0 , the sequence is increasing.
   Recall that in (4.2) the ≥ inequality always holds [DDNL18b, Theorem 2.3], it suﬃces to prove
                                         Z                                          Z
(4.3)                           lim            θ1,ϕk ∧ · · · ∧ θn,ϕkn ≤                  θ1,ϕ1 ∧ · · · ∧ θn,ϕn .
                               k→∞ X               1
                                                                                     X
By Witt Nyström’s monotonicity theorem [WN19; DDNL18b], in order to prove (4.3), we may
assume that for j > i0 , the sequences ϕkj are constant. Thus, we are reduced to the case where for
all i, ϕki are decreasing.
   In this case, for each i we may take an increasing sequence bki > 1, tending to ∞, such that
                                                       Z                                    Z
                                             (bki )n        n
                                                           θi,ϕ i
                                                                  > (bki )n − 1                        n
                                                                                                      θi,ϕ k.
                                                       X                                          X       i

Let ψik be the maximal θi -psh function, such that
                                                                                        
                                               (bki )−1 ψik + 1 − (bki )−1 ϕki ≤ ϕi ,
whose existence is guaranteed by [DDNL21b, Lemma 4.3].
                                                           PARTIAL OKOUNKOV BODIES                                                                            17

    Then by Witt Nyström’s monotonicity theorem [WN19; DDNL18b] again,
                               n 
                               Y                        Z                                          Z
                                         1 − (bki )−1          θ1,ϕk ∧ · · · ∧ θn,ϕkn ≤                  θ1,ϕ1 ∧ · · · ∧ θn,ϕn .
                                                                       1
                               i=1                         X                                         X

Let k → ∞, we conclude (4.3).
  Step 2. Now we deal with the general case.
                                                 dS
  We claim that if t ∈ (0, 1], (1 − t)ϕki + tVθi −→ (1 − t)ϕi + tVθi as k → ∞ for each i. From this
and Step 1, we ﬁnd that for ti ∈ (0, 1],
               Z                                                                            Z
    lim            θ1,(1−t1 )ϕk +t1 Vθ ∧ · · · ∧ θn,(1−tn )ϕkn +tn Vθn =                         θ1,(1−t1 )ϕ1 +t1 Vθ ∧ · · · ∧ θn,(1−tn )ϕn +tn Vθn .
    k→∞ X                      1             1                                               X                              1

Thus, (4.2) follows, after letting ti ց 0.
   It remains to prove the claim. For simplicity, let us suppress the i indices momentarily. We need
to argue that
         Z                                                                  Z                                           Z
                  j                                n−j                               j               n−j                         j
    2            θmax{(1−t)ϕ k +tV ,(1−t)ϕ+tV } ∧ θVθ  −                            θ(1−t)ϕ k +tV ∧ θVθ  −                      θ(1−t)ϕ+tVθ
                                                                                                                                            ∧ θVn−j
                                                                                                                                                 θ
                                                                                                                                                    → 0.
                                  θ          θ                                                   θ
             X                                                                  X                                        X
Note that the above expression is a linear combination of terms of the following type:
                                         Z                                      Z                         Z
                                                  r              n−r
                                     2           θmax{ϕ k ,ϕ} ∧ θV
                                                                  θ
                                                                     −                  θϕr k ∧ θVn−r
                                                                                                   θ
                                                                                                      −           θϕr k ∧ θVn−r
                                                                                                                             θ
                                                                                                                                .
                                          X                                         X                      X
                                                                                                                                    d
Thanks to (4.1), all these expressions tend to 0 as k → ∞ since ϕk −→
                                                                    S
                                                                      ϕ, which proves our
claim.                                                                                 
Corollary 4.3. Let ϕk , ϕ ∈ PSH(X, θ) (k ∈ N). Let ω be a Kähler form on X. Assume that
        dS,θ                         dS,θ+ω
ϕk −−→ ϕ. Then ϕk −−−−→ ϕ.
Proof. It suﬃces to show that for each j = 0, . . . , n, we have
    Z                                                          Z                                                    Z
2           (θ + ω)jmax{ϕk ,ϕ} ∧ (θ + ω)Vn−j
                                          θ+ω
                                              −                        (θ + ω)jϕk ∧ (θ + ω)Vn−j
                                                                                             θ+ω
                                                                                                 −                          (θ + ω)jϕ ∧ (θ + ω)Vn−j
                                                                                                                                                 θ+ω
                                                                                                                                                     →0
        X                                                       X                                                    X
as k → ∞. Note that this quantity is a linear combination of terms of the following form:
    Z                                                              Z                                                        Z
2            r
            θmax{ϕ k ,ϕ} ∧ ω
                             j−r
                                 ∧ (θ + ω)Vn−j
                                            θ+ω
                                                −                          θϕr k ∧ ω j−r ∧ (θ + ω)Vn−j
                                                                                                    θ+ω
                                                                                                        −                           θϕr ∧ ω j−r ∧ (θ + ω)Vn−j
                                                                                                                                                           θ+ω
                                                                                                                                                               ,
        X                                                          X                                                            X
                                                                                                                                        d
where r = 0, . . . , j. By Theorem 4.2, it suﬃces to show that max{ϕ, ϕk } −→
                                                                            S
                                                                              ϕ. But this follows
from [DDNL21b, Proposition 3.5].                                                               
Corollary 4.4. Let ϕ ∈ PSH(X, θ) be an I-model potential of positive mass. Let ω be a Kähler
form on X. Then P θ+ω [ϕ] is I-model.
Proof. By [DX21, Theorem 3.8], we may take a sequence ϕj with analytic singularities such that
        dS,θ                       dS,θ+ω
ϕj −−→ ϕ. Then ϕj −−−−→ ϕ by Corollary 4.3. Thus, P θ+ω [ϕ] is I-model.                                                                                       
                                                                                                                                                       dS,θ
Corollary 4.5. Let ϕj , ϕ ∈ PSH(X, θ1 ), ψ j , ψ ∈ PSH(X, θ2 ) (j ∈ N). Assume that ϕj −−−→
                                                                                          1
                                                                                            ϕ,
        dS,θ
ψ j −−−→
       2
         ψ. Then
                                                                                dS,θ +θ
                                                             ϕj + ψ j −−−1−−→
                                                                            2
                                                                              ϕ + ψ.
Proof. Let θ = θ1 + θ2 . It suﬃces to show that for each r = 0, . . . , n,
                           Z                                                Z                                 Z
                                                      n−r
                       2        r
                               θmax{ϕ j +ψ j ,ϕ+ψ} ∧ θV
                                                       θ
                                                          −                         θϕr j +ψj ∧ θVn−r
                                                                                                   θ
                                                                                                      −             r
                                                                                                                   θϕ+ψ ∧ θVn−r
                                                                                                                             θ
                                                                                                                                → 0.
                           X                                                 X                                X
Observe that
                                         max{ϕj + ψ j , ϕ + ψ} ≤ max{ϕj , ϕ} + max{ψ j , ψ}.
18                                                              MINGCHEN XIA

Thus, it suﬃces to show that
                        Z                                              Z                             Z
                                                            n−r
                    2            r
                                θmax{ϕ j ,ϕ}+max{ψ j ,ψ} ∧ θV
                                                             θ
                                                                −              θϕr j +ψj ∧ θVn−r
                                                                                              θ
                                                                                                 −          r
                                                                                                           θϕ+ψ ∧ θVn−r
                                                                                                                     θ
                                                                                                                        → 0.
                            X                                           X                             X
The left-hand side is a linear combination of
            Z                                                       Z                                         Z
                     a                 r−a
        2           θ1,max{ϕ j ,ϕ} ∧ θ
                                       2,max{ψj ,ψ}
                                                    ∧ θVn−r
                                                         θ
                                                            −                   a
                                                                               θ1,ϕ j ∧ θ
                                                                                          r−a
                                                                                          2,ψj
                                                                                               ∧ θVn−r
                                                                                                    θ
                                                                                                       −           a
                                                                                                                  θ1,ϕ    r−a
                                                                                                                       ∧ θ2,ψ ∧ θVn−r
                                                                                                                                   θ
                X                                                       X                                     X
                                                                   d                                      d
with a = 0, . . . , r. Observe that max{ϕj , ϕ} −→
                                                 S
                                                   ϕ and max{ψ j , ψ} −→
                                                                       S
                                                                         ψ by [DDNL21b, Proposi-
tion 3.5], each term tends to 0 by Theorem 4.2.                                              
     Finally, we prove the continuity of P [•]I .
Theorem 4.6. The map PSH(X, θ)>0 → PSH(X, θ)>0 given by ϕ 7→ P [ϕ]I is continuous with
respect to the dS -pseudometric.
                                                                                                                   R   n
     Here PSH(X, θ)>0 denotes the subset of PSH(X, θ) consisting of ϕ with                                          X θϕ > 0.
                                                      d
Proof. Let ϕi , ϕ ∈ PSH(X, θ)>0 , ϕi −→
                                      S
                                        ϕ. We want to show that
                                                                        S  d
(4.4)                                                         P [ϕi ]I −→ P [ϕ]I .
We may assume that the ϕi ’s and ϕ are all model potentials by [DDNL21b, Theorem 3.3]. By
[DDNL21b, Theorem 5.6], we may assume that ϕi is either increasing or decreasing. These cases
follow from [DX22, Lemma 2.21] and [DDNL21b, Proposition 4.8, Lemma 4.1].                  

                                                  5. Partial Okounkov bodies
  Let X be an irreducible smooth complex projective variety of dimension n and L be a big line
bundle on X. Take a singular psh metric φ on L. We assume that vol(L, φ) > 0. Let h be a smooth
Hermitian metric on L. Let θ = c1 (L, h). Then we can identify φ with a function ϕ ∈ PSH(X, θ).
We will use interchangeably the notations (θ, ϕ) and (L, φ).
  For each k ≥ 0,
                                                                                                     ∞
                                                                                                     M
                                   Wk (θ, ϕ) := H0 (X, Lk ⊗ I(kϕ)),                 W (θ, ϕ) :=            Wk (θ, ϕ).
                                                                                                     k=0
We omit (θ, ϕ) from our notations when there is no risk of confusion. Observe that Wk (θ, ϕ) 6= 0
when k is large enough, as follows from Theorem 2.19.
  Fix a rank n valuation ν : C(X)× → Zn . We will write
                                                          n                                   o
                                         Γν,k (θ, ϕ) = k−1 ν(s) : s ∈ Wk (θ, ϕ)× ,                       k≥1
                                                          
                                           Γν (θ, ϕ) = (ν(s), k) : k ∈ N, s ∈ Wk (θ, ϕ)× .
  In [LM09], Lazarsfeld–Mustat, ă only considered the case where ν is induced by an admissible
ﬂag, but thanks to Remark 2.8, their results can be easily extended to the current setup. We will
use these results without further comments.
5.1. Construction of partial Okounkov bodies. Our goal in this section is to show that
Γν (θ, ϕ) ∈ S ′ (∆ν (L))>0 , namely it is an almost semigroup. Then we shall deﬁne
(5.1)                                                  ∆ν (θ, ϕ) := ∆ (Γν (θ, ϕ))
using the theory of Okounkov bodies of almost semigroups developed in Section 3.3. Moreover, we
have
                                                    Z
                                                  1
(5.2)                             vol ∆ν (θ, ϕ) =     θn      .
                                                  n! X P [ϕ]I
                                          PARTIAL OKOUNKOV BODIES                                                     19

5.1.1. The case of analytic singularities. Assume that ϕ has analytic singularities and θϕ is a Kähler
current.
   For any rational ǫ ≥ 0, we deﬁne
                                          n                                                                   o
(5.3)              Wkǫ = Wkǫ (θ, ϕ) := s ∈ H0 (X, Lk ) : |s|2hk e−k(1−ǫ)ϕ is bounded .
              L∞
Then W ǫ :=          ǫ
                k=0 Wk has the property that
                                      n                                             o
(5.4)                   Γν (W ǫ ) := (ν(s), k) : k ∈ N, s ∈ Wkǫ,× ∈ S ′ (∆ν (L)).
To see this, we may assume that ϕ has analytic singularities along a Q-divisor E, then (5.4) follows
from the fact that L − (1 − ǫ)E is big proved in [Xia23b, Lemma 2.4], c.f. [LM09, Lemma 2.2].
   For any ǫ ∈ Q>0 , we have that
(5.5)                                                  Wk0 ⊆ Wk ⊆ Wkǫ
for k large enough depending on ǫ. The ﬁrst inclusion is of course trivial. The second inclusion is
widely known among experts. A detailed proof can be found in [DX21, Remark 2.9].
   Let π : Y → X be a resolution such that π ∗ ϕ has analytic singularities along a normal crossing
Q-divisor E. Then we have a natural identiﬁcation for suﬃciently divisible k,
                             Wǫ ∼= H0 (Y, π ∗ Lk ⊗ OY (−(1 − ǫ)kE)).
                                  k

On the other hand,
                           Wk0 ∼
                               = H0 (Y, π ∗ Lk ⊗ OY (−kE)) ⊆ H0 (Y, π ∗ Lk ).
We compute the volumes,
                                                   Z                                              Z
                                              1                                              1
(5.6)                   vol Γν (W ǫ ) =                     n
                                                           θ(1−ǫ)ϕ ,       vol Γν (W 0 ) =            θϕn .
                                              n!   X                                         n!   X

It follows that Γν (W ǫ ) → Γν (W 0 ) and Γν (θ, ϕ) is equivalent to Γν (W 0 ). In particular, Γν (θ, ϕ) ∈
S ′ (∆ν (L))>0 , (5.1) makes sense and (5.2) holds.
Remark 5.1. It follows from the proof that if W 0 (θ, ϕ) is deﬁned as in (5.3) and (5.4):
                                          n                                                           o
                        Wk0 (θ, ϕ) := s ∈ H0 (X, Lk ) : |s|2hk e−kϕ is bounded ,
then
(5.7)                                 ∆(Γν (W 0 (θ, ϕ))) = ∆ν (θ, ϕ).
If we assume furthermore that π ∗ ϕ has analytic singularity along some normal crossing Q-divisor
E on Y , then ∆ν (θ, ϕ) is just the translation of ∆ν (π ∗ L − E) by ν(E).
5.1.2. The case of Kähler currents. Now assume that θϕ is Kähler current. Let ϕj ∈ PSH(X, θ) be
                                                                       d
a quasi-equisingular approximation of ϕ. Then ϕj −→
                                                  S
                                                    P [ϕ]I by [DX21, Proposition 3.3].
  In this case, we claim that
(5.8)                                          Γν (θ, ϕj ) → Γν (θ, ϕ).
In fact, by Theorem 2.19, we have
                                                                                                                 
        d(Γν (θ, ϕj ), Γν (θ, ϕ)) = lim k−n h0 (X, Lk ⊗ I(kϕj )) − h0 (X, Lk ⊗ I(kϕ))
                                  k→∞
                                = lim k−n h0 (X, Lk ⊗ I(kϕj )) − lim k−n h0 (X, Lk ⊗ I(kϕ))
                                  k→∞                                                   k→∞
                                      Z                        Z
                              1            1
                            =       θ nj −     θn      .
                              n! X ϕ       n! X P [ϕ]I
Letting j → ∞, we conclude (5.8) by Theorem 4.2.
20                                              MINGCHEN XIA


     Thus, Γν (θ, ϕ) ∈ S ′ (∆ν (L))>0 and (5.1) makes sense. By Theorem 3.14, we ﬁnd that
                                                            ∞
                                                            \
                                           ∆ν (θ, ϕ) =           ∆ν (θ, ϕj ).
                                                         j=0

In particular, (5.2) holds.
                                                                                                   R
5.1.3. General case. Now we consider general ϕ with the assumption that X θPn [ϕ]I > 0. We may
replace ϕ with P [ϕ]I and then assume that the non-pluripolar mass of ϕ is positive. Take a potential
ψ ∈ PSH(X, θ) such that ψ ≤ ϕ and θψ is a Kähler current. The existence of ψ is proved in [DX21,
Proposition 3.6]. For each ǫ ∈ Q ∩ (0, 1], let ϕǫ = (1 − ǫ)ϕ + ǫψ. Then we have W (θ, ϕǫ ) ⊆ W (θ, ϕ).
By (5.2),
                                                        Z
                                                      1
                                   vol ∆ν (θ, ϕǫ ) =         θn    .
                                                     n! X P [ϕǫ ]I
We claim that
                                        Γν (θ, ϕǫ ) → Γν (θ, ϕ).
In fact, this follows from the simple computation:
                                                                                                      
          d (Γν (θ, ϕǫ ), Γν (θ, ϕ)) = lim k−n h0 (X, Lk ⊗ I(kϕ)) − h0 (X, Lk ⊗ I(kϕǫ ))
                                  k→∞
                                = lim k−n h0 (X, Lk ⊗ I(kϕ)) − lim k−n h0 (X, Lk ⊗ I(kϕǫ ))
                                  k→∞                                           k→∞
                                       Z            Z
                                  1            1
                                =        θϕn −               θPn [ϕǫ ]I .
                                  n!   X       n!       X
By [DX21, Proposition 2.7], as ǫ decreases to 0, P [ϕǫ ]I increases to P [ϕ]I = ϕ a.e., which implies the
dS -convergence by [DDNL21b, Lemma 4.1]. Therefore, the right-hand side of the above equation
converges to 0 by Theorem 4.2. Our claim is proved. It follows that Γν (θ, ϕ) ∈ S ′ (∆ν (L))>0 and
(5.1) makes sense. By Theorem 3.14,
                                                            [
                                           ∆ν (θ, ϕ) =           ∆ν (θ, ϕǫ ).
                                                         ǫ>0

It remains to verify (5.2):
                                                         Z                      Z
                                           1                      1
                           vol ∆ν (θ, ϕ) =     lim   θPn [ϕǫ ]I =                     θPn [ϕ]I .
                                           n! ǫ→0+ X              n!             X
                                                    R
Definition 5.2. Assume that ϕ ∈ PSH(X, θ), X θPn [ϕ]I > 0. We call ∆ν (θ, ϕ) the partial Okounkov
body of (L, φ) or of (θ, ϕ) with respect to ν. When ν is induced by an admissible ﬂag (Y• ) on X
(see Deﬁnition 2.7), we also say that ∆ν (θ, ϕ) the partial Okounkov body of (L, φ) or of (θ, ϕ) with
respect to (Y• ). In this case, we also write ∆Y• instead of ∆ν .
  We use interchangeably the notations ∆ν (θ, ϕ) and ∆ν (L, φ). When there is no risk of confusion,
we write ∆ instead of ∆ν or ∆Y• .
Remark 5.3. We have assumed X to be smooth only for simplicity. All of our constructions work
equally well when X is normal or merely unibranch, based on the pluripotential theory in these
settings developed in [Xia23a].
Remark 5.4. In the transcendental setting, a theory of Okounkov bodies is recently established in
[DRWN+23] based on the work of [Den17]. The proof of the volume identity of transcendental
Okounkov bodies relies on the technique of partial Okounkov bodies developed in this paper. The
transcendental analogue of the partial Okounkov bodies is constructed in a forthcoming joint paper
with T.Darvas.
                                        PARTIAL OKOUNKOV BODIES                                         21

5.2. Basic properties of partial Okounkov bodies. We ﬁrst show that ∆(θ, ϕ) does not depend
on the explicit choices of L, h and ϕ, it just depends on ddc φ.
Lemma 5.5. Let L′ be another big line bundle on X. Let h′ be a smooth Hermitian metric on L′
with c1 (L, h) = c1 (L′ , h′ ). Then ∆(θ, ϕ) defined with respect to (L, h) is the same as the one defined
with respect to (L′ , h′ ).
Proof. From our construction, we may assume that θϕ is a Kähler current and ϕ has analytic
singularities. After taking a birational resolution, it suﬃces to deal with the case where ϕ has
analytic singularities along normal crossing Q-divisors E. By rescaling, we may also assume that
E is a divisor. By Remark 5.1, we further reduce to the case without the singular potential φ.
   In this case, the assertion is proved in [LM09, Proposition 4.1].                           
Lemma 5.6. Let h′ be another smooth Hermitian metric on L. Set θ ′ = c1 (L, h′ ). Write ddc f =
θ − θ ′ . Let ϕ′ = ϕ + f ∈ PSH(X, θ ′ ). Then
(5.9)                                        ∆(θ, ϕ) = ∆(θ ′ , ϕ′ ).
Proof. This is obvious as W (θ, ϕ) = W (θ ′ , ϕ′ ).                                                     
Corollary 5.7. The partial Okounkov body ∆(L, φ) depends only on ddc φ, not on the explicit
choices of L, φ, h.
                                                                                          R     n > 0, we
  Thanks to this result, given a closed positive (1, 1)-current T ∈ c1 (L) on X with       XT
can deﬁne ∆(T ) as ∆(θ, ϕ) if T = θ + ddc ϕ for some ϕ ∈ PSH(X, θ).
Proof. This is a direct consequence of Lemma 5.5 and Lemma 5.6.                                         
                                                                                               R   n
  Let PSH(X, θ)>0 denote the subset of PSH(X, θ) consisting of potentials ϕ such that           X θϕ > 0.

Proposition 5.8. Let ϕ, ψ ∈ PSH(X, θ)>0 . Assume that ϕ I ψ, then
(5.10)                                        ∆(θ, ϕ) ⊆ ∆(θ, ψ).
In particular, as by definition, ∆(θ, Vθ ) = ∆(L), we have
                                                 ∆(θ, ϕ) ⊆ ∆(L).
Proof. This follows from Corollary 3.15.                                                                
Theorem 5.9. The Okounkov body map
                                ∆(θ, •) : (PSH(X, θ)>0 , dS ) → (Kn , dn )
is continuous.
Remark 5.10. On the other hand, it is of interest to understand the dependence of ∆(θ, •) on ν
as well. For some preliminary results and anticipations in the usual Okounkov body setting, see
[AI22]. In particular, see [AI22, Conjecture 10.1] for a concrete continuity conjecture.
Proof. Let ϕj → ϕ be a dS -convergent sequence in PSH(X, θ)>0 . We want to show that
                                                        n  d
(5.11)                                       ∆(θ, ϕj ) −→ ∆(θ, ϕ).
By Proposition 5.8 and [DDNL21b, Theorem 3.3], we may assume that all ϕj ’s and ϕ are model
potentials. By Theorem 2.2 and [DDNL21b, Theorem 5.6], we may assume that ϕj is either
decreasing or increasing. By Theorem 4.6, we may further assume that the ϕj ’s are I-model. In
both cases, we claim that Γν (θ, ϕj ) → Γν (θ, ϕ). In fact, we can compute their distance as follows
            d (Γν (θ, ϕj ), Γν (θ, ϕ)) = lim k−n h0 (X, Lk ⊗ I(kϕj )) − h0 (X, Lk ⊗ I(kϕ))
                                        k→∞
                                             Z             Z
                                        1
                                    =             θϕnj −           θϕn ,
                                        n!    X                X
22                                                  MINGCHEN XIA

where we applied Theorem 2.19 at the last step. Then Theorem 4.2 implies our claim. Hence, (5.11)
follows from Theorem 3.14.                                                                     
  Although W (θ, ϕ) and Γν (θ, ϕ) are not birationally invariant, we could still show that the Ok-
ounkov body is.
Proposition 5.11. Let π : Y → X be a birational resolution. Let (L, φ) be a Hermitian big line
bundle on X with positive volume, then
                                          ∆(π ∗ L, π ∗ φ) = ∆(L, φ).
     Here we are using the same valuation ν on the function ﬁeld C(Y ) = C(X) of Y .
Proof. By Deﬁnition 2.12(3), Pθ [•]I commutes with birational pullbacks, we may assume that ϕ is I-
model. By [DX21, Theorem 3.8], we can ﬁnd a sequence ϕj ∈ PSH(X, θ) with analytic singularities
                 d                                            d
such that ϕj −→
              S
                 ϕ. It follows from (4.1) that π ∗ ϕj −→S
                                                          π ∗ ϕ. By Theorem 5.9, we may then reduce
to the case where ϕ has analytic singularities. In this case, up to replacing Y by a further sequences
of blowups, we may assume that π ∗ ϕ has analytic singularities along a normal crossing Q-divisor
D. It suﬃces to apply Remark 5.1.                                                                   
     Next we prove the Brunn–Minkowski inequality.
Proposition 5.12. Let (L, φ), (L′ , φ′ ) be Hermitian big line bundles on X of positive volumes.
Then
              (vol ∆(L + L′ , φ + φ′ ))1/n ≥ (vol ∆(L, φ))1/n + (vol ∆(L′ , φ′ ))1/n .
Proof. This follows from Corollary 2.20.                                                            
Proposition 5.13. Let (L′ , φ′ ) be another Hermitian big line bundle on X with positive volume.
Then
                                 ∆(L, φ) + ∆(L′ , φ′ ) ⊆ ∆(L ⊗ L′ , φ ⊗ φ′ ).
Proof. Take a smooth metric h′ on L′ , let θ ′ = c1 (L′ , h′ ). We identify φ′ with ϕ′ ∈ PSH(X, θ ′ ).
Then we need to show
(5.12)                           ∆(θ, ϕ) + ∆(θ ′ , ϕ′ ) ⊆ ∆(θ + θ ′ , ϕ + ϕ′ ).
By [DX21, Theorem 3.8], we can ﬁnd ϕj ∈ PSH(X, θ), ϕ′j ∈ PSH(X, θ ′ ) such that
   (1) ϕj and ϕ′j both have analytic singularities and have positive masses.
             d         d
      (2) ϕj −→
              S
                ϕ, ϕ′j −→
                        S
                          ϕ′ .
                                                         d
Then ϕj + ϕ′j ∈ PSH(X, θ + θ ′ ) and ϕj + ϕ′j −→
                                               S
                                                 ϕ + ϕ′ by Corollary 4.5. Thus, by Theorem 5.9,
we may assume that ϕ and ψ both have analytic singularities. Taking a birational resolution, we
may further assume that they have analytic singularities along some normal crossing divisors. By
Remark 5.1, we reduce to the case without singularities, in which case the result is well-known, see
[LM09, The proof of Corollary 4.12] for example.                                                  
Theorem 5.14. Let ϕ, ψ ∈ PSH(X, θ)>0 . Then for any t ∈ (0, 1),
(5.13)                     ∆(θ, tϕ + (1 − t)ψ) ⊇ t∆(θ, ϕ) + (1 − t)∆(θ, ψ).
Proof. We may assume that t is rational as a consequence of Theorem 5.9. Similarly, by [DX21,
Theorem 3.8], we could reduce to the case where both ϕ and ψ have analytic singularities. Taking
a resolution, we may assume that ϕ (resp. ψ) has analytic singularities along a normal crossing
Q-divisor E (resp. E ′ ). In this case, let N > 0 be an integer such that N t is an integer. Then for
any s ∈ Wk0 (θ, ϕ), r ∈ Wk0 (θ, ψ), we have
                                              N
                                    st r 1−t        ∈ WN0 k (θ, tϕ + (1 − t)ψ).
By Theorem 3.8, (5.13) follows.                                                                     
                                       PARTIAL OKOUNKOV BODIES                                   23

Proposition 5.15. For any integer a > 0,
                                         ∆(aθ, aϕ) = a∆(θ, ϕ).
Proof. By Theorem 5.9, it suﬃces to treat the case where ϕ has analytic singularities. Taking
a birational resolution, we may assume that ϕ has analytic singularities along a normal crossing
Q-divisor E. By Remark 5.1, we reduce to the case without the singularity ϕ, which is already
proved in [LM09].                                                                             
                                                                             R
  In particular, if T is a closed positive (1, 1)-current on X with X T n > 0 and such that the
cohomology class of T lies in the Néron–Severi group with rational coeﬃcients, then we can deﬁne
∆(T ) as a−1 ∆(aT ) for a suﬃciently divisible positive integer a.
  We also need the following perturbation. Let A be an ample line bundle on X. Fix a smooth
Hermitian metric hA on A such that ω := c1 (A, hA ) is a Kähler form on X. Then for any δ ∈ Q>0 ,
we can deﬁne
                    ∆(θ + δω, ϕ) := ∆(θ + δω + ddc ϕ) = C −1 ∆(Cθ + Cδω, Cϕ),
where C ∈ N>0 is any integer so that Cδ ∈ N.
Proposition 5.16. Under the above assumptions, as δ ∈ Q>0 decreases to 0, ∆(θ + δω, ϕ) is
decreasing under inclusion with Hausdorff limit ∆(θ, ϕ).
Proof. Let 0 ≤ δ < δ′ be two rational numbers. Take C ∈ N>0 divisible enough, so that Cδ and
Cδ′ are both integers. Then by Proposition 5.13,
                              ∆(Cθ + Cδω, Cϕ) ⊆ ∆(Cθ + Cδ′ ω, Cϕ).
It follows that
                                    ∆(θ + δω, ϕ) ⊆ ∆(θ + δ′ ω, ϕ).
On the other hand,
                                         Z                           Z
                                   1                           1
                  vol ∆(θ + δω, ϕ) =    (θ + δω)nP θ+δω [ϕ]I =      (θ + δω)nP θ [ϕ]I ,
                                   n! X                        n! X
where we applied Corollary 4.4. As δ → 0+, the right-hand side converges to
                                                    Z
                                                 1
                                  vol ∆(θ, ϕ) =          θn θ  .
                                                n! X P [ϕ]I
It follows that                              \
                                 ∆(θ, ϕ) =        ∆(θ + δω, ϕ).
                                               δ∈Q>0
                                                                                                 
5.3. The Hausdorff convergence property of partial Okounkov bodies. For each k ∈ Z>0 ,
we introduce                    n                                   o
               ∆k (θ, ϕ) := Conv k−1 ν(f ) : f ∈ H0 (X, Lk ⊗ I(kϕ))× ⊆ Rn .
Here Conv denotes the convex hull. The convex hull is a polytope if it is non-empty by [LM09,
Lemma 1.4]. For large enough ∆k (θ, ϕ) is non-empty thanks to Theorem 2.19.
   For later use, we introduce a twisted version as well. If T is a holomorphic line bundle on X, we
introduce                           n                                        o
                ∆k,T (θ, ϕ) := Conv k−1 ν(f ) : f ∈ H0 (X, T ⊗ Lk ⊗ I(kϕ))× ⊆ Rn .
We also write                            n                                       o
                      ∆k,T (L) := Conv k−1 ν(f ) : f ∈ H0 (X, T ⊗ Lk )× ⊆ Rn
and                                       n                              o
                         ∆k (L) := Conv k−1 ν(f ) : f ∈ H0 (X, Lk )× ⊆ Rn .
24                                             MINGCHEN XIA

  We write I∞ (ϕ) = I∞ (φ) for the ideal sheaf on X locally consisting of holomorphic functions f
such that |f |φ is locally bounded.
  The main result is the following:
Theorem 5.17 (Hausdorﬀ convergence property). Let T be a holomorphic line bundle on X. As
                               d
k → ∞, we have ∆k,T (θ, ϕ) −→
                            n
                              ∆(θ, ϕ).
  Although we are only interested in the untwisted case, the proof given below requires twisted
case.
  We ﬁrst extend Theorem 3.8 to the twisted case.
Proposition 5.18. For any holomorphic line bundle T on X, as k → ∞
                                                     d n
                                             ∆k,T (L) −→ ∆(L).
Proof. As L is big, we can take k0 ∈ Z>0 so that
   (1) T −1 ⊗ Lk0 admits a non-zero global holomorphic section s0 ;
   (2) T ⊗ Lk0 admits a non-zero global holomorphic section s1 .
Then for k ∈ Z>k0 , we have injective linear maps
                                        ×s                    ×s
                         H0 (X, Lk−k0 ) −−→
                                          1
                                            H0 (X, T ⊗ Lk ) −−→
                                                              0
                                                                H0 (X, Lk+k0 ).
It follows that
                  (k − k0 )∆k−k0 (L) + ν(s1 ) ⊆ k∆k,T (L) ⊆ (k + k0 )∆k+k0 (L) − ν(s0 ).
By Theorem 3.8, we conclude.                                                                          
Lemma 5.19. Let T be a holomorphic line bundle on X. Assume that ϕ has analytic singularities
and θϕ is a Kähler current, then as k → ∞,
                                                     dn
                                         ∆k,T (θ, ϕ) −→ ∆(θ, ϕ).
Proof. Up to replacing X by a birational model and twisting T accordingly, we may assume that
ϕ has analytic singularities along a normal crossing Q-divisor D, c.f. Proposition 5.11. Take
ǫ ∈ (0, 1) ∩ Q. In this case, as in (5.5), for large enough k ∈ Z>0 we have
      H0 (X, T ⊗ Lk ⊗ I∞ (kϕ)) ⊆ H0 (X, T ⊗ Lk ⊗ I(kϕ)) ⊆ H0 (X, T ⊗ Lk ⊗ I∞ (k(1 − ǫ)ϕ)).
Take an integer N ∈ Z>0 so that N D is a divisor and N ǫ is an integer.
    Let ∆′ be the limit of a subsequence of (∆k,T (θ, ϕ))k , say the sequence deﬁned by the indices
k1 , k2 , . . .. We want to show that ∆′ = ∆(θ, ϕ).
   There exists t ∈ {0, 1, . . . , N −1} such that ki ≡ t modulo N for inﬁnitely many i, up to replacing
ki by a subsequence, we may assume that ki ≡ t modulo N for all i. Write ki = N gi + t. Then
           H0 (X, T ⊗ L−N +t ⊗ LN (gi +1) ⊗ I∞ (N (gi + 1)ϕ)) ⊆ H0 (X, T ⊗ Lki ⊗ I(ki ϕ))
                                               ⊆ H0 (X, T ⊗ Lt ⊗ LN gi ⊗ I∞ (gi N (1 − ǫ)ϕ)).
So
            (gi + 1)∆gi +1,T ⊗L−N+t (N L − N D) + N (gi + 1)ν(D) ⊆ (N gi + t)∆k,T (θ, ϕ)
                                      ⊆ gi ∆gi ,T ⊗Lt (N L − N (1 − ǫ)D) + N gi (1 − ǫ)ν(D).
Letting i → ∞, by Proposition 5.18,
                      ∆(L − D) + ν(D) ⊆ ∆′ ⊆ ∆(L − (1 − ǫ)D) + (1 − ǫ)ν(D).
Letting ǫ → 0+, we ﬁnd that
                                        ∆(L − D) + ν(D) = ∆′ .
                                       PARTIAL OKOUNKOV BODIES                                                          25

It follows from Theorem 2.2 that
                                         nd
                            ∆k,T (θ, ϕ) −→ ∆(L − D) + ν(D) = ∆(θ, ϕ)
as k → ∞.                                                                                                               
Lemma 5.20. Assume that θϕ is a Kähler current, then as Q ∋ β → 0+, we have
                                       ∆((1 − β)θ, ϕ) → ∆(θ, ϕ).
Proof. By Proposition 5.13, we have
                                 ∆((1 − β)θ, ϕ) + β∆(L) ⊆ ∆(θ, ϕ).
In particular, if ∆′ is a limit of a subsequence of (∆((1 − β)θ, ϕ))β , then
                                                  ∆′ ⊆ ∆(θ, ϕ).
But
                                              Z                                            Z
         ′                                                         c   (1−β)θ       n
   vol ∆ = lim ∆((1 − β)θ, ϕ) = lim                ((1 − β)θ + dd P             [ϕ]I ) =       (θ + ddc P θ [ϕ]I )n ,
             β→0+                   β→0+ X                                                 X

where the last step follows easily from [Xia22, Theorem 0.6]. It follows that ∆′ = ∆(θ, ϕ). We
conclude by Theorem 2.2.                                                                     

Proof of Theorem 5.17. Fix a Kähler form ω ≥ θ on X.
   Step 1. We ﬁrst handle the case where θϕ is a Kähler current, say θϕ ≥ β0 ω for some β0 ∈ (0, 1).
  Take a decreasing quasi-equisingular approximation ϕj of ϕ. Up to replacing β0 by β0 /2, we may
assume that θϕj ≥ β0 ω for all j ≥ 1.
   Let ∆′ be a limit of a subsequence of (∆k,T (θ, ϕ))k . Let us say the indices of the subsequence
are k1 < k2 < · · · . By Theorem 2.2, it suﬃces to show that ∆′ = ∆(θ, ϕ).
  As [ϕ]  [ϕj ] for each j ≥ 1, we have ∆′ ⊆ ∆(θ, ϕj ) by Lemma 5.19. Letting j → ∞, we ﬁnd
                                                  ∆′ ⊆ ∆(θ, ϕ).
In particular, it suﬃces to prove that
                                          vol ∆′ ≥ vol ∆(θ, ϕ).
Take β ∈ (0, β0 ) ∩ Q. Write β = p/q with p, q ∈ Z>0 . Observe that for any j ≥ 1,
                                                  θϕj ≥ βω ≥ βθ.
Namely, ϕj ∈ PSH(X, (1 − β)θ). Similarly, ϕ ∈ PSH(X, (1 − β)θ). By Lemma 5.20, it suﬃces to
argue that
(5.14)                                 vol ∆′ ≥ vol ∆((1 − β)θ, ϕ).
For this purpose, we are free to replace ki ’s by a subsequence, so we may assume that ki ≡ a
modulo q for all i ≥ 1, where a ∈ {0, 1, . . . , q − 1}. We write ki = gi q + a. Observe that for each
i ≥ 1,
             H0 (X, T ⊗ Lki ⊗ I(ki ϕ)) ⊇ H0 (X, T ⊗ L−q+a ⊗ Lgi q+q ⊗ I((gi q + q)ϕ)).
Up to replacing T by T ⊗ L−q+a , we may therefore assume that a = 0.
   By [DX21, Lemma 4.2], we can ﬁnd k′ ∈ Z>0 such that for all k ≥ k′ , there is vβ,k ∈ PSH(X, θ)
satisfying
    (1) P [ϕ]I ≥ (1 − β)ϕk + βvβ,k ;
    (2) vβ,k has positive mass.
26                                               MINGCHEN XIA

     Fix k ≥ k′ . It suﬃces to show that
(5.15)                                    ∆((1 − β)θ, ϕk ) + v ′ ⊆ ∆′
for some v ′ ∈ Rn . In fact, if this is true, we have
                                        vol ∆′ ≥ vol ∆((1 − β)θ, ϕk ).
Letting k → ∞ and applying Theorem 5.9, we conclude (5.14).
   It remains to prove (5.15). We will ﬁx k ≥ k′ . Let π : Y → X be a log resolution of the
singularities of ϕk . By the proof of [DX21, Proposition 4.3], there is j0 = j0 (β, k) ∈ Z>0 such that
for any j ≥ j0 , we can ﬁnd a non-zero section sj ∈ H0 (Y, π ∗ Lpj ⊗ I(jpπ ∗ vβ,k )) such that we get an
injective linear map
                                                                   ×sj
             H0 (Y, π ∗ T ⊗ KY /X ⊗ π ∗ L(q−p)j ⊗ I(jqπ ∗ ϕk )) −−→ H0 (X, T ⊗ Ljq ⊗ I(jqϕ)).
In particular, when j = ki for some i large enough, we then ﬁnd
                   ∆ki ,π∗ T ⊗KY /X ((1 − β)qπ ∗ θ, qπ ∗ ϕk ) + (ki )−1 ν(ski ) ⊆ q∆ki ,T (θ, ϕ).
We observe that (ki )−1 ν(ski ) is bounded as both convex bodies appearing in this equation are
bounded when i varies. Then by Lemma 5.19, there is a vector v ′ ∈ Rn such that
                                       ∆((1 − β)π ∗ θ, π ∗ ϕk ) + v ′ ⊆ ∆′ .
By Proposition 5.11, we ﬁnd (5.15).
   Step 2. Next we handle the general case.
   Let ∆′ be the limit of a subsequence of (∆k,T (θ, ϕ))k , say the subsequence with indices k1 <
k2 < · · · . By Theorem 2.2, it suﬃces to prove that ∆′ = ∆(θ, ϕ).
   Take ψ ∈ PSH(X, θ) such that
    (1) θψ is a Kähler current;
    (2) ψ ≤ ϕ.
The existence of ψ is proved in [DX21, Proposition 3.6].
   Then for any ǫ ∈ Q ∩ (0, 1),
                                    ∆k,T (θ, ϕ) ⊇ ∆k,T (θ, (1 − ǫ)ϕ + ǫψ)
for all k. It follows from Step 1 that
                                          ∆′ ⊇ ∆(θ, (1 − ǫ)ϕ + ǫψ).
     Letting ǫ → 0 and applying Theorem 5.9, we have ∆′ ⊇ ∆(θ, ϕ). It remains to establish that
(5.16)                                       vol ∆′ ≤ vol ∆(θ, ϕ).
For this purpose, we are free to replace k1 < k2 < · · · by a subsequence. Fix q > 0, we may then
assume that ki ≡ a modulo q for all i ≥ 1 for some a ∈ {0, 1, . . . , q − 1}. We write ki = gi q + a.
Observe that
                   H0 (X, T ⊗ Lki ⊗ I(ki ϕ)) ⊆ H0 (X, T ⊗ La ⊗ Lgi q ⊗ I(gi qϕ)).
Up to replacing T by T ⊗ La , we may assume that a = 0.
   Take a very ample line bundle H on X and ﬁx a Kähler form ω ∈ c1 (H), take a non-zero section
s ∈ H0 (X, H).
   We have an injective linear map
                                                    ×sj
                     H0 (X, T ⊗ Ljq ⊗ I(jqϕ)) −−→ H0 (X, T ⊗ H j ⊗ Ljq ⊗ I(jqϕ))
for each j ≥ 1. In particular, for each i ≥ 1,
                             ki ∆ki ,T (qθ, qϕ) + ki ν(s) ⊆ ki ∆ki ,T (ω + qθ, qϕ).
                                     PARTIAL OKOUNKOV BODIES                                           27

Letting i → ∞, by Step 1, we have
                                     q∆′ + ν(s) ⊆ ∆(ω + qθ, qϕ).
So                                                   Z
                                                                                  −1 ω+θ
                  vol ∆′ ≤ vol ∆(q −1 ω + θ, ϕ) =         (q −1 ω + θ + ddc P q            [ϕ]I )n .
                                                      X
By Corollary 4.4,                          Z
                                vol ∆′ ≤       (q −1 ω + θ + ddc P θ [ϕ]I )n .
                                           X
Letting q → ∞, we conclude (5.16).                                                                     
Theorem 5.21. The Okounkov body ∆(L, φ) is independent of the choice of a very general flag in
a family of admissible flags.
Proof. By Theorem 5.17, it suﬃces to show that ∆k (W (θ, ϕ)) is independent of the choice of a very
general ﬂag. For this purpose, we may assume that k = 1.
  Let T be an irreducible component of the moduli space of admissible ﬂags. Let
                                       X × T = Y 0 ⊇ · · · ⊇ Yn
be the universal ﬂag. The Hermitian line bundle (L, φ) pulls back to (L, Φ) on X × T . We denote
quantities at the ﬁber at t ∈ T by a sub-index t.
  We claim that for each σ ∈ Nn , there is a proper Zariski closed set Σ ⊆ T , so that
                                      dim H0 (Xt , Lt ⊗ I(φt ))≥σ
are constants for t ∈ T \ Σ, where H0 (Xt , Lt ⊗ I(φt ))≥σ denotes the space of sections in H0 (Xt , Lt ⊗
I(φt )) with valuations no less than σ.
   Let L≥σ be the coherent subsheaf of L introduced in [LM09, Remark 1.6]. After possibly shrink-
ing T , we may guarantee that L≥σ ⊗ I(Φ) is ﬂat over T . By further shrinking T , we may guarantee
that                                                                
                                 t 7→ dim H0 Xt , (L≥σ ⊗ I(Φ))|Xt
is constant. Observe that
                                   (L≥σ ⊗ I(Φ))|Xt ∼  ≥σ
                                                   = Lt ⊗ I(φ).
Thus, our claim follows.
  From this claim, it follows that the images of Γk (W (L, φ)) are independent of the choice of a
very general ﬂag (Y• ) as [LM09, Proof of Theorem 5.1]. Thus, ∆(W (L, φ)) is independent of the
choice of a very general ﬂag.                                                                  
5.4. Recover Lelong numbers from partial Okounkov bodies.
Lemma 5.22. Suppose that ϕ ∈ PSH(X, θ) such that θϕ is a Kähler current. Let ϕj be a quasi-
equisingular approximation of ϕ. Then ν(ϕj , E) → ν(ϕ, E) for any prime divisor E over X.
  This result is essentially [Xia23b, Lemma 2.2], proved under slightly diﬀerent assumptions. We
reproduce the argument for the convenience of the readers.
Proof. Fix k ∈ Z>0 , δ ∈ Q>0 , take j0 > 0, so that when j > j0 , I((1 + δ)kϕj ) ⊆ I(kϕ). When
j > j0 , we get
                           1                  1
                              ordE (I(kϕ)) ≤ ordE (I((1 + δ)kϕj )).
                           k                  k
By Fekete’s lemma,
                                                 1
                                ν(ϕj , E) = sup    ordE (I(kϕj )).
                                           k∈Z>0 k
So
                                1
                                  ordE (I(kϕ)) ≤ (1 + δ)ν(ϕj , E).
                                k
28                                                MINGCHEN XIA

Take sup with respect to k ∈ Z>0 , we get
                                         ν(ϕ, E) ≤ (1 + δ)ν(ϕj , E).
Letting j → ∞ and then δ → 0+, we get
                                            ν(ϕ, E) ≤ lim ν(ϕj , E).
                                                       j→∞

The reverse inequality is trivial.                                                                   
Theorem 5.23. Let E be a prime divisor on X. Let (Y• ) be an admissible flag with E = Y1 . Then
(5.17)                                       ν(ϕ, E) =       min x1 .
                                                           x∈∆(θ,ϕ)

  Here x1 denotes the ﬁrst component of x. The generic Lelong number ν(ϕ, E) means the mini-
mum of ν(ϕ, x) for various x ∈ E.
Proof. We ﬁrst reduce to the case where θϕ is a Kähler current. Let ψ ≤ ϕ, θψ is a Kähler current.
Then by (5.17) applied to ϕǫ := (1 − ǫ)ϕ + ǫψ, we have
                                             ν(ϕǫ , E) =     min        x1 .
                                                           x∈∆(θ,ϕǫ )

Let ǫ → 0+ using Theorem 5.9, we conclude (5.17).
   Similarly, taking a quasi-equisingular approximation of ϕ and applying Lemma 5.22, we easily
reduce to the case where ϕ also has analytic singularities. Replacing X by a birational model, we
may assume that ϕ has analytic singularities along a simple normal crossing Q-divisor F . Perturbing
L by an ample Q-line bundle by Proposition 5.16, we may assume that θϕ is a Kähler current.
Finally, by rescaling, we may assume that F is a divisor and L is a line bundle and L − F is ample
by [Xia23b, Lemma 2.4]. In fact, since θϕ is a Kähler current, the same holds for θϕ − ǫω, where
ω is a Hodge form lying in c1 (A) for some ample line bundle A on X and ǫ > 0 is a small enough
rational number. By [Xia23b, Lemma 2.4], we deduce that L − F − ǫA is nef and big and hence
L − F is ample.
   By Theorem 5.17, we know that
                                        min x1 = lim             min           x1 .
                                       x∈∆(θ,ϕ)        k→∞ x∈∆k (θ,ϕ)

By deﬁnition,
                                 min        x1 = k−1 ordE H0 (X, Lk ⊗ I(kϕ)).
                               x∈∆k (θ,ϕ)
It remains to show that
(5.18)                   lim k−1 ordE H0 (X, Lk ⊗ I(kϕ)) = lim k−1 ordE I(kϕ).
                         k→∞                                          k→∞

The ≥ direction is trivial, we prove the converse. Observe that
                 H0 (X, Lk ⊗ I(kϕ)) = H0 (X, Lk ⊗ OX (−kF )),                     I(kϕ) = O(−kF ).
As L − F is ample, for large enough k, we have
                               ordE H0 (X, Lk ⊗ OX (−kF )) = ordE (kF ).
Thus, (5.18) is clear.                                                                               
Corollary 5.24. Let ϕ, ψ ∈ PSH(X, θ)>0 . If
                                        ∆(π ∗ θ, π ∗ ϕ) ⊆ ∆(π ∗ θ, π ∗ ψ)
for all birational models π : Y → X and all admissible flags on Y , then ϕ I ψ.
                                    PARTIAL OKOUNKOV BODIES                                         29

Proof. In view of Theorem 5.23, the assumption implies the following: for any prime divisor E
over X, we have ν(ϕ, E) ≥ ν(ψ, E). This implies ϕ I ψ: take a birational model π : Y → X
and y ∈ Y , we need to show that ν(π ∗ ϕ, y) ≥ ν(π ∗ ψ, y). Let E be the exceptional divisor of the
blow-up of Y at {y}. As explained in [Bou02a, Corollaire 1.1.8], we have ν(π ∗ ϕ, y) = ν(ϕ, E) and
ν(π ∗ ψ, y) = ν(ψ, E). Our assertion follows.                                                    
   In particular, Theorem B is proved. This corollary is similar to [Jow10]. It suggests that ∆(θ, ϕ)
is a universal invariant of the singularities of ϕ.
   Corollary 5.24 has a reminiscence of [BFJ08]: in order to understand plurisubharmonic singular-
ities, we need to consider all birational models of our variety at the same time.
   Theorem 5.23 can be regarded as a generalization of the following (slightly generalized form of
the) classical result proved by Boucksom, see [Bou02b, Theorem 5.4].
Corollary 5.25. Let E be a prime divisor over X. Then
                                               1
(5.19)                         ν(Vθ , E) = lim ordE H0 (X, Lk ).
                                          k→∞ k

Proof. This follows from Theorem 5.23 and the fact that ∆(θ, Vθ ) = ∆(L).                           
  We write
                                                          1
                                ordE kLk := lim               ordE H0 (X, Lk ).
                                                   k→∞ k
Corollary 5.26. We have
     I(Vθ ) = {f ∈ OX : ∃ǫ > 0 s.t. ordE (f ) ≥ (1 + ǫ) ordE kLk − AX (E) ∀prime E over X} ,
where AX (E) is the log discrepancy of E over X.
Proof. This follows from [Bou17, Corollary 10.17] and Corollary 5.25.                               
5.5. Okounkov bodies induced by filtrations. Assume that L is ample.
Definition 5.27. A multiplicative filtration on R(X, L) is a decreasing, left continuous, multiplica-
tive R-ﬁltration F • on the ring R(X, L) which is linearly bounded in the sense that there is C > 0,
so that
                        F −kλ H0 (X, Lk ) = H0 (X, Lk ), F kλ H0 (X, Lk ) = 0,
when λ > C.
   A multiplicative ﬁltration F is called a multiplicative Z-filtration if F λ = F ⌊λ⌋ for any λ ∈ R.
   A multiplicative Z-ﬁltration F is called finitely generated if the bigraded algebra
                                           M
                                                        F λ H0 (X, Lk )
                                      λ∈Z,k∈Z≥0

is ﬁnitely generated over C.
  Let F • be a multiplicative ﬁltration on R(X, L). Then we can associate a test curve ψ• as in
[RWN14; Xia23b].
                                                                                           
(5.20)         ψτ := sup* k−1 sup*       log |s|2hk : s ∈ F kτ H0 (X, Lk ), sup |s|hk ≤ 1       .
                      k∈Z>0                                                       X

Here sup∗ denotes the upper-semicontinuous regularized supremum. By [DX22, Theorem 3.11], ψτ
is I-model or −∞ for each τ ∈ R.
Theorem 5.28. Let F • be a finitely generated multiplicative Z-filtration on R(X, L). Let ψ• be
the test curve associated with F . For any τ < τ + ,
                                    ∞
                                                                  !
                                    M
                                              kτ    0         k
                                ∆         F        H (X, L ) = ∆(θ, ψτ ).
                                    k=0
30                                             MINGCHEN XIA

Proof. Observe that F kτ H0 (X, Lk ) ⊆ H0 (X, Lk ⊗ I(kψτ )) for any k ∈ N. Thus, by Corollary 3.15,
                                    ∞
                                                                !
                                    M
                                              kτ    0       k
                                ∆         F        H (X, L ) ⊆ ∆(θ, ψτ ).
                                    k=0

On the other hand, the two sides have the same volume by [Xia23b, Lemma 4.5]. Thus, equality
holds.                                                                                    

5.6. Limit partial Okounkov bodies. Let ϕ ∈ PSH(X, θ), not necessarily of positive volume.
Take an ample eﬀective divisor H on X and a Kähler form ω ∈ c1 (H). Then we just set
                                                        \
                                    ∆(θ, ϕ) :=              ∆(θ + ǫω, ϕ).
                                                    ǫ∈Q>0

Clearly, this deﬁnition does not depend on the choice of H and ω. As in [CHPW18b], we can-
not expect ∆(θ, ϕ) to be continuous along decreasing sequences of ϕ. Note that Theorem 5.23,
Corollary 5.24 and Proposition 5.8 extend to this setup without changes.
  We propose the following conjecture:
Conjecture 5.29. Under the above assumptions,
                                        dim ∆(θ, ϕ) = nd(θ, ϕ).
  For the deﬁnition of the analytic numerical dimension nd(θ, ϕ), we refer to [Cao14, Deﬁnition 4].
  We expect that this conjecture follows from the arguments in [CHPW18b] together with the
numerical criterion of [Cao14].

                                    6. Chebyshev transform
  Let X be an irreducible smooth complex projective variety of dimension n and L be a big line
bundle on X. Let h be a ﬁxed smooth Hermitian metric on L and θ = c1 (L, h). Consider
                                                                               R      a singular
positive Hermitian metric φ on L corresponding to ϕ ∈ PSH(X, θ). Assume that X θPn [ϕ]I > 0.
   Let v ∈ C 0 (X) corresponding to a continuous metric he−v/2 on L. We do not distinguish v and
he−v/2 . Fix a valuation ν = (ν1 , . . . , νn ) : C(X)× → Zn of rank n. Assume that ν is deﬁned by an
admissible ﬂag (Y• ) on X.
   The whole section is devoted to the proof of Theorem C. Our results are direct extensions of the
results of Witt Nyström [WN14]. The latter is motivated by [Zah75].

6.1. Equilibrium energy. Let E ∞ (X, θ; P [ϕ]I ) denote the set of ψ ∈ PSH(X, θ) such that ψ and
P [ϕ]I have the same singularity types.
         θ : E ∞ (X, θ; P [ϕ] ) → R be the relative Monge–Ampère energy:
   Let E[ϕ]                  I

                                              n      Z
                          θ              1 X
                         E[ϕ] (ψ) :=               (ψ − P [ϕ]I ) θψi ∧ θPn−i
                                                                          [ϕ]I .
                                       n + 1 i=0 X
                              θ : C 0 (X) → R:
Deﬁne the equilibrium energy E[ϕ]
                                        θ           θ
(6.1)                                  E[ϕ] (v) := E[ϕ] (P [ϕ]I (v)).
Here
                        P [ϕ]I (v) = sup* {η ∈ PSH(X, θ) : η ≤ v, η I ϕ} .
Note that this deﬁnition is diﬀerent from the energy deﬁned in [DX21], so we choose a diﬀerent
notation.
                                      PARTIAL OKOUNKOV BODIES                                       31

                                          θ at v ∈ C 0 (X) is given by θ n
Theorem 6.1. The Gateaux differential of E[ϕ]                           P [ϕ]I (v) . In other words,
             0
for any f ∈ C (X),
                                                 Z
                            d       θ
(6.2)                              E (v + tf ) =    f θPn [ϕ]I (v) .
                            dt t=0 [ϕ]            X

Proof. This is not exactly [DX21, Proposition 5.10] because we are using P [•]I projections instead
of P [•] projections, but the proofs are identical.                                               
  The metric he−v/2 induces an L∞ -type norm k • kL∞ (kv) on H0 (X, Lk ⊗ I(kϕ)):
                                      kskL∞ (kv) := sup |s|hk e−kv/2 .
                                                           X

In particular, det k • kL∞ (kv) is a Hermitian metric on det H0 (X, Lk ⊗ I(kϕ)).
Theorem 6.2. Let v, v ′ ∈ C 0 (X),
                     n!                                         
                                                                     θ          θ
(6.3)           lim n+1 log det k • kL∞ (kv) / det k • kL∞ (kv′ ) = E[ϕ] (v) − E[ϕ] (v ′ ).
               k→∞ k

Remark 6.3. When ϕ = Vθ , the left-hand side of (6.3) is known as the relative volume between the
                            ′
two metrics he−v/2 and he−v /2 . They are studied in detail in [BBWN11].
   This theorem partially generalizes [BB10, Theorem A]. We remind the readers that our conven-
tions of multiplier ideal sheaves are diﬀerent from those in [BB10] and [BBWN11], which explains
the diﬀerence between our coeﬃcients and theirs.
   For the deﬁnition of Bernstein–Markov property, see [BB10, Deﬁnition 2.3].
Proof. We may assume that v ′ = 0. Let ν be a smooth volume form on X. Then recall that ν
satisﬁes the Bernstein–Markov property with respect to tv for all t ∈ [0, 1] [BB10, Theorem 2.4].
We may replace the L∞ -norm on the left-hand side with the L2 (ν)-norm by [DX21, Lemma 6.5].
We recall the deﬁnition of the partial Bergman kernel:
                                                   Z                                           
             k
            Btv,ϕ,ν (x) := sup |s|2hk e−kv (x) :         |s|2hk e−tv ≤ 1, s ∈ H0 (X, Lk ⊗ I(kϕ))
                                                     X
and
                                            k            n! k
                                           βtv,ϕ,ν :=      B       dν,
                                                         kn tv,ϕ,ν
where k ∈ Z>0 .
  By [DX21, Theorem 1.2],
                                             k
                                            βtv,ϕ,ν ⇀ θPnX [ϕ]I (tv)
as k → ∞ for all t ∈ [0, 1]. By the dominated convergence theorem,
                                   Z 1Z                        Z 1Z
                                              k
                            lim            v βtv,ϕ,ν dt =                 v θPnX [ϕ]I (tv) dt
                           k→∞ 0       X                        0     X
and (6.3) follows.                                                                                  
Proposition 6.4. Let ϕ ∈ PSH(X, θ) such that θϕ is a Kähler current. Let (ϕj )j∈N be a quasi-
equisingular approximation of ϕ. Then
(6.4)                                       lim E θ j (v) = E[ϕ]
                                                             θ
                                                                 (v).
                                           j→∞ [ϕ ]

Proof. By Theorem 6.1, for j ∈ N,
                                                    Z 1Z
                                     θ
                                    E[ϕ j ] (v) =            v θPn [ϕj ]I (tv) dt,
                                                    0    X
                                                    Z 1Z
                                      θ
                                     E[ϕ] (v) =              v θPn [ϕ]I (tv) dt.
                                                    0    X
32                                                MINGCHEN XIA

It follows from [DX21, Proposition 3.3] and [DDNL18b, Theorem 1.2] that as j → ∞,
                                            θPn [ϕj ]I (tv) ⇀ θPn [ϕ]I (tv) .
By the dominated convergence theorem, (6.4) follows.                                                    
Proposition 6.5. Let ϕ, ψ ∈ PSH(X, θ). Assume that ψ ≤ ϕ. Set ϕǫ = (1 − ǫ)ϕ + ǫψ for any
ǫ ∈ [0, 1]. Then
(6.5)                                        lim E θ (v) = E[ϕ]
                                                            θ
                                                                (v).
                                            ǫ→0+ [ϕǫ ]

Proof. The proof is similar to that of Proposition 6.4. We just replace [DX21, Proposition 3.3] by
[DX21, Proposition 2.7].                                                                        
     We ﬁnally recall a technical lemma.
Lemma 6.6 ([WN14, Corollary 3.4]). Let C ⊆ Rn+1 be an open convex cone. Let F be a subadditive
function on C ∩ Zn+1 defined outside a compact set. Then for any sequence αk ∈ C ∩ Zn+1 tending
to infinity such that αk /|αk | converges to some point p ∈ C. Then the limit
                                                              F (αk )
                                            c[F ](p) := lim
                                                           k→∞ |αk |

exists and depends only on p and F . Moreover, c[F ] is a convex function on C ∩ {xn+1 = 1}.
  Here |αk | denotes the absolute value of the last component of αk .
  Recall that a real-valued function F deﬁned on a semigroup Γ is said to be sub-additive if for
any x, y ∈ Γ, F (x + y) ≤ F (x) + F (y).
6.2. The case of analytic singularities. Assume that ϕ has analytic singularities.
   Let π : Y → X be a resolution such that π ∗ ϕ has analytic singularity along a normal crossing
Q-divisor E. We deﬁne as before
                             Wk0 = H0 (Y, π ∗ Lk ⊗ OY (−kE)) ⊆ H0 (X, Lk ).
Fix a ∈ Γk (W 0 ). Let p be the center of ν on X. Let z = (z1 , . . . , zn ) be a regular sequence in OX,p
such that (Yi )x is the zero locus of z1 , . . . , zi . Fix a local trivialization of L near p. Deﬁne
                         n                                                            o
                  Aak := s ∈ Wk0 : ν(s) ≥ ka, s = z ka + higher order terms near p .
Deﬁne
                                   F [v](ka, k) = inf log |s|L∞ (kv) .
                                                         s∈Aa,k
Recall the following two lemmas proved in [WN14, Lemma 5.3, Lemma 5.4].
Lemma 6.7. F [v] is subadditive on Γ(W 0 ).
Lemma 6.8. There is C > 0, so that for any (ka, k) ∈ Γ(W 0 ),
                                        F [v](ka, k) ≥ C|(ka, k)|.
Proof. It suﬃces to apply [WN14, Lemma 5.4].                                                            
     Let c[ϕ] [v] : Int ∆(θ, ϕ) → R be the convex function c[F [v]] deﬁned by Lemma 6.6.
Theorem 6.9. We have
                              Z                                   
                                                                         θ
                                              c[ϕ] [v] − c[ϕ] [0] dλ = −E[ϕ] (v).
                               ∆(W (θ,ϕ))

Proof. The proof follows verbatim from that of [WN14, Theorem 6.2], taking into account Theo-
rem 6.2.                                                                                   
                                            PARTIAL OKOUNKOV BODIES                                    33

  Observe that
(6.6)                                 sup         c[ϕ] [v] − c[ϕ] [0] ≤ kvkC 0 (X) /2.
                              Int ∆(W (θ,ϕ))

  The following result is obvious:
Lemma 6.10. Let ϕ, ϕ′ ∈ PSH(X, θ) be potentials with analytic singularities. If [ϕ]  [ϕ′ ], then
                                                    c[ϕ] [v] ≥ c[ϕ′ ] [v]
when restricted to Int ∆(θ, ϕ).
6.3. The case of Kähler currents. Assume that θϕ is a Kähler current. Let ϕj be a quasi-
equisingular approximation of ϕ. Then c[ϕj ] [v] restricted to Int ∆(W (θ, ϕ)) is an increasing sequence.
Thus, we can deﬁne c[ϕ] [v] : Int ∆(θ, ϕ) → R ∪ {∞} by
                                                c[ϕ] [v] := lim c[ϕj ] [v].
                                                            j→∞

Lemma 6.11. Let s ∈ Wk (θ, ϕ), locally written as z ka plus higher order terms near p. Then
                                        c[ϕ] [v](a) ≤ k−1 log kskL∞ (kv) .

Proof. This follows from the corresponding result for the ϕj ’s.                                       

   By convexity, c[ϕ] [v] takes ﬁnite values.
   It follows that (6.6) still holds in this case. By the dominated convergence theorem, Proposi-
tion 6.4 and the previous case we ﬁnd
                               Z                                 
                                                                           θ
                                                c[ϕ] [v] − c[ϕ] [0] dλ = −E[ϕ] (v).
                                   ∆(θ,ϕ)

  It follows from Lemma 6.10 that our deﬁnition of c[ϕ] (v) is independent of the choice of ϕj .
Lemma 6.12. Let ϕ, ϕ′ ∈ PSH(X, θ) be potentials such that θϕ and θϕ′ are both Kähler currents.
If [ϕ] I [ϕ′ ], then
                                     c[ϕ] [v] ≥ c[ϕ′ ] [v]
when restricted to Int ∆(θ, ϕ).
Proof. This follows from Lemma 6.10.                                                                   
                                                                  R
6.4. General case. Let ϕ ∈ PSH(X, θ) such that X θPn [ϕ]I > 0. We may replace ϕ with P [ϕ]I
and therefore assume that the non-pluripolar mass of ϕ is positive.
   Let η ∈ PSH(X, θ) be a potential so that θη is a Kähler current and η  ϕ. The existence
of such η is guaranteed by [DX21, Proposition 3.6]. Deﬁne ϕǫ := (1 − ǫ)ϕ + ǫη. Then we deﬁne
c[ϕ] [v] : Int ∆(θ, ϕ) → R ∪ {−∞} as
                                                c[ϕ] [v] := lim c[ϕǫ ] [v].
                                                            ǫ→0+

This is a decreasing limit by Lemma 6.12. On the other hand, c[ϕ] [v] ≥ c[Vθ ] [v], the latter is ﬁnite by
[WN14]. Thus, c[ϕ] [v] is real-valued. (6.6) extends to this situation. By the dominated convergence
theorem and Proposition 6.5 again,
                                  Z
                                                                          θ
                                             (c[ϕ] [v] − c[ϕ] [0]) dλ = −E[ϕ] (v).
                                   ∆(θ,ϕ)

We do not know if c[ϕ] [v] is independent of the choice of η.
34                                              MINGCHEN XIA

                      7. A generalization of Boucksom–Chen theorem
   In this section, let X be an irreducible smooth projective variety of dimension n. Let L be a big
line bundle on X. Take a smooth Hermitian metric h on L with θ = c1 (L, h).
   Fix a rank n valuation ν : C(X)× → Zn .
7.1. The theory of test curves. Let V = hLn i.
Definition 7.1. A test curve (of finite energy) with respect to (X, θ) is a map ψ = ψ• : R →
PSH(X, θ) ∪ {−∞}, such that
   (1) ψ• is concave in •.
   (2) ψτ is a model potential or −∞ for any τ .
   (3) ψ is usc as a function in the R-variable.
   (4) limτ →−∞ ψτ = Vθ in L1 .
   (5) ψτ = −∞ for τ large enough.
   (6)
                                                Z τ + Z                  
(7.1)                       E(ψ• ) := τ + V +                  θψnτ − V       dτ > −∞.
                                                 −∞      X

Here τ + := inf{τ ∈ R : ψτ = −∞}. The set of test curves of ﬁnite energy with respect to (X, θ)
is denoted by T C 1 (X, θ). We say ψ is normalized if τ + = 0. The test curve is called bounded if
ψτ = Vθ for τ small enough. Let τ − := sup{τ ∈ R : ψτ = Vθ } in this case. The set of bounded test
curves is denoted by T C ∞ (X, θ).
   We say a test curve is I-model if ψτ is I-model for each τ < τ + . The set of I-model test curves
is denoted by T C 1I (X, θ).
7.2. Okounkov test curves. Let ∆ ∈ Kn . Assume that V = n! vol ∆ > 0.
Definition 7.2. An Okounkov test curve relative to ∆ is an assignment (∆τ )τ ≤τ + (τ + ∈ R) such
that
   (1) ∆τ is a decreasing assignment of convex bodies in Rn for τ ≤ τ + ;
   (2) ∆τ converges to ∆ as τ → −∞ with respect to the Hausdorﬀ metric (c.f. Section 2.1);
   (3) ∆τ is concave in the τ variable;
   (4) The energy is ﬁnite:
                                                Z τ+                         
                                                         n!
                         E(∆• ) := τ + V + V                vol ∆τ − 1            dτ > −∞ ;
                                                 −∞      V
     (5) Continuity holds at τ + :
                                                         \
                                            ∆τ + =              ∆τ .
                                                      τ <τ +

Proposition 7.3. Any Okounkov test curve (∆τ )τ ≤τ + relative to ∆ is continuous for τ < τ + .
Proof. We ﬁrst claim that vol ∆τ ′ > 0 for all τ ′ < τ + . By Condition (2) and Theorem 2.3, we know
that vol ∆τ ′′ > 0 when τ ′′ is small enough. Fix one such τ ′′ . Any τ ′ < τ + can be written as a
convex combination of τ + and τ ′′ , thus ∆τ ′ has positive volume by Condition (3).
   Next we claim that vol ∆τ is continuous for τ < τ + . In fact, by Condition (3) and the Minkowski
inequality, we know that log vol ∆τ is concave for τ < τ + . The continuity follows.
   Next we show that                                \
                                           ∆τ =         ∆τ ′ .
                                                      τ ′ <τ
The ⊇ direction is obvious. By the continuity of the volume, both sides have the same volume and
the volume is positive, hence, equality holds by Lemma 2.5.
                                     PARTIAL OKOUNKOV BODIES                                      35

  Similarly, we have
                                                        [
                                            ∆τ =             ∆τ ′ .
                                                    τ ′ >τ
The continuity of ∆τ at τ < τ + is proved.                                                        
Definition 7.4. A test function on ∆ is a function F : ∆ → [−∞, ∞) such that
   (1) F is concave;
   (2) F is ﬁnite on Int ∆;
   (3) F is usc;
   (4) the energy is ﬁnite:
                                                    Z
(7.2)                                 E(F ) := n!           F dλ > −∞.
                                                    ∆

  Let τ + = sup∆ F , then
                                              Z τ+                      
                                                        n!
(7.3)                     E(F ) = τ + V + V                vol{F ≥ τ } − 1   dτ.
                                               −∞       V
  Let ∆• be an Okounkov test curve relative to ∆. We deﬁne the Legendre transform of ∆• as
                                                                   n               o
                       G[∆• ] : ∆ → [−∞, ∞),        a 7→ sup τ < τ + : a ∈ ∆τ .
Conversely, a test function F on ∆, set τ + = sup∆ F . We deﬁne the inverse Legendre transform of
F as
                            ∆[F ] : (−∞, τ + ] → Kn , ∆[F ]τ = {F ≥ τ }.
Theorem 7.5. The Legendre transform and inverse Legendre transform are inverse to each other,
defining a bijection between the set of Okounkov test curves relative to ∆ and test functions on ∆.
Moreover, if ∆• is an Okounkov test curve relative to ∆, then
(7.4)                                    E(∆• ) = E (G[∆• ]) .
Proof. Let ∆• be an Okounkov test curve relative to ∆. We prove that G[∆• ] is a test function on
∆.
   Firstly G[∆• ] is concave by Condition (1) and Condition (3) in Deﬁnition 7.2. More precisely,
take a, b ∈ ∆. We want to prove that for any t ∈ (0, 1),
(7.5)                   G[∆• ](ta + (1 − t)b) ≥ tG[∆• ](a) + (1 − t)G[∆• ](b).
There is nothing to prove if G[∆• ](a) or G[∆• ](b) is −∞. So we assume that both are ﬁnite. Take
ǫ > 0, then a ∈ ∆G[∆• ](a)−ǫ and b ∈ ∆G[∆• ](b)−ǫ . Thus,
           ta + (1 − t)b ∈ t∆G[∆• ](a)−ǫ + (1 − t)∆G[∆• ](b)−ǫ ⊆ ∆tG[∆• ](a)+(1−t)G[∆• ](b)−ǫ .
We deduce that
                      G[∆• ](ta + (1 − t)b) ≥ tG[∆• ](a) + (1 − t)G[∆• ](b) − ǫ.
Since ǫ > 0 is arbitrary, (7.5) follows.
   Next G[∆• ] is ﬁnite on Int ∆ by Condition (2). In fact, as ∆τ is increasing and converges to ∆
as τ → −∞, we have
                                                        [
                                              ∆=            ∆τ .
                                                        τ
                                                                              S
Hence, by [Sch14, Theorem 1.1.15] and the assumption that vol ∆ > 0, τ ∆τ contains Int ∆.
  Thirdly, we show that G[∆• ] is usc. Let ai ∈ ∆ with ai → a ∈ ∆. Deﬁne τi = G[∆• ](ai ). Let
τ = limi τi . We need to show that
(7.6)                                        G[∆• ](a) ≥ τ.
36                                              MINGCHEN XIA

There is nothing to prove if τ = −∞. We assume that it is not this case. Up to subtracting a
subsequence we may assume that τi → τ . In particular, we can assume that τi 6= −∞ for all i. Fix
                                                   dn
ǫ > 0, then ai ∈ ∆τi −ǫ . Observe that ∆τi −ǫ −→       ∆τ −ǫ . By Theorem 2.4 it follows that a ∈ ∆τ −ǫ .
Thus,(7.6) follows since ǫ > 0 is arbitrary.
    Finally, (7.4) follows from (7.3), and it follows that E(G[∆• ]) > −∞.
    Conversely, if F : ∆ → [−∞, ∞) is a test function on ∆. Let ∆[F ] be the inverse Legendre
transform of F . Then one can similarly show that ∆[F ] is an Okounkov test curve.
    Firstly, for each τ < τ + := sup∆ F , ∆[F ](τ ) is a convex body as F is concave and usc. Moreover,
∆[F ]τ is clearly decreasing in τ . Hence, ∆[F ]τ + is also a convex body.
    Secondly, for each a ∈ ∆, we can write a = limi ai with ai ∈ Int ∆. By assumption, F is ﬁnite at
ai . Thus,
                                                               [
                                      a ∈ {F > −∞} =               ∆[F ]τ .
                                                               τ

                          nd
By Theorem 2.4, ∆[F ]τ −→    ∆ as τ → −∞.
  Thirdly, ∆[F ] is concave. To see, take τ, τ ′ ≤ τ + , we need to prove that for any t ∈ (0, 1),

(7.7)                          ∆[F ]tτ +(1−t)τ ′ ⊇ t∆[F ]τ + (1 − t)∆[F ]τ ′ .

Let a ∈ ∆[F ]τ and b ∈ ∆[F ]τ ′ . We have F (a) ≥ τ and F (b) ≥ τ ′ . As F is concave, we have
F (ta + (1 − t)b) ≥ tτ + (1 − t)τ ′ . Thus,

                                     ta + (1 − t)b ∈ ∆[F ]tτ +(1−t)τ ′

and (7.7) follows.
  Fourthly, (7.2) follows immediately from (7.3).
  Finally, we show that ∆[F ]• is continuous at τ + . This amounts to
                                                       \
                                       {F ≥ τ + } =            {F ≥ τ },
                                                      τ <τ +

which is obvious.
  To see that these two operations are inverse to each other, observe that by deﬁnition for any
Okounkov test curve ∆• , any a ∈ ∆ and any τ ≤ τ + , G[∆• ](a) ≥ τ if and only if a ∈ ∆τ −ǫ for any
ǫ > 0. By Proposition 7.3, this happens if and only if a ∈ ∆τ , that is,

                                           {G[∆• ] ≥ τ } = ∆τ .

     Conversely, for any test function F : ∆ → [−∞, ∞), any τ ≤ τ + , by deﬁnition,

                                           {F ≥ τ } = ∆[F ]τ .

                                                                                                      

Definition 7.6. Let ∆• be an Okounkov test curve relative to ∆. We deﬁne the Duistermaat–
Heckman measure DH(∆• ) as
                                        DH(∆• ) := G[∆• ]∗ (dλ).
It is a Radon measure on R.

     Observe that
                                          Z
(7.8)                                           DH(∆• ) = vol ∆.
                                            R
                                     PARTIAL OKOUNKOV BODIES                                        37

7.3. Boucksom–Chen theorem. Let ψ• ∈ T C 1I (X, θ). Let τ + = inf{τ ∈ R : ψτ = −∞}.
Lemma 7.7. The curve                          
                                              
                                                        ∆(θ, ψτ ),        τ < τ +,
                                                    \
                                ∆[ψ• ]τ :=                   ∆[ψ• ]τ ′ ,   τ = τ+
                                              
                                              
                                                  τ ′ <τ +
is an Okounkov test curve relative to ∆(L). Moreover,
(7.9)                                    E(ψ• ) = E(∆[ψ• ]• ).
Proof. We verify the conditions in Deﬁnition 7.2. Condition (1) follows from Proposition 5.8. Con-
dition (2) follows from the fact
                                       lim vol ∆τ = vol ∆.
                                        τ →−∞
Condition (3) follows from Theorem 5.14 and Proposition 5.8. Condition (4) is a translation of
(7.1). Condition (5) is obvious.
   Finally, (7.9) follows from (7.1) and (1.3).                                             
Definition 7.8. Let ψ• ∈ T C 1I (X, θ). Deﬁne the Duistermaat–Heckman measure of ψ• as
                                       DH(ψ• ) := DH(∆[ψ• ]• ).
  We write
                                          G[ψ• ] = G[∆[ψ• ]].
Then
                                     DH(ψ• ) = G[ψ• ]∗ (dλ).
  Now consider the (not necessarily multiplicative) ﬁltration:
                                              (
                                                  H0 (X, Lk ⊗ I(kψτ )),                 τ < τ +,
                         Fτk H0 (X, Lk ) :=
                                                                               0,       τ ≥ τ +.
Let ej (H0 (X, Lk ), F k ) be the jumping numbers of F k listed in the decreasing order. In order
words,                                       n                               o
                     ej H0 (X, Lk ), F k := sup τ ∈ R : dim Fτk H0 (X, Lk ) ≥ j .
Let
                                              h0 (X,Lk )
                                        1          X
                                  µk := n                     δej (H0 (X,Lk ),F k ) .
                                       k           j=1

Theorem 7.9. Let ψ• ∈ T C 1I (X, θ). Then as k → ∞, µk converges weakly to DH(ψ• ).
   As explained in [RWN14; DX22; Xia23b], T C 1I (X, θ) is the completion of the space of ﬁltrations,
so this theorem indeed generalizes [BC11, Theorem A], in the case of full graded linear series.
Proof. It suﬃces to show the convergence holds as distributions. By our deﬁnition, µk is the
distributional derivative of the function
                                       ( −n 0
                                        k h (X, Lk ⊗ I(kψτ )), τ < τ + ,
                            hk (τ ) :=
                                                            0, τ ≥ τ + .
On the other hand, DH(ψ• ) is the distributional derivative of h(τ ) := vol{G[∆[ψ• ]• ] ≥ τ } = vol ∆τ
by Fubini–Tonelli theorem.
   By Theorem 2.19, hk (τ ) → h(τ ) for all τ 6= τ + . By the dominated convergence theorem hk → h
in L1loc (R). Hence, µk ⇀ DH(ψ• ).                                                                   
Corollary 7.10. For any ψ• ∈ T C 1I (X, θ). The Duistermaat–Heckman measure DH(ψ• ) is inde-
pendent of the choice of the valuation ν.
38                                           MINGCHEN XIA

7.4. Applications to non-Archimedean geometry. Assume that L is ample and θ is a Kähler
form. We write ω = θ instead.

Finite energy geodesic rays. Let E 1 (X, ω) denote the space of ω-psh functions with ﬁnite energy:
                                                   Z                 Z           Z                 
                  E 1 (X, ω) := ϕ ∈ PSH(X, ω) :             ωϕn =           ωn,           |ϕ| ωϕn < ∞ .
                                                        X               X             X

See [Dar19] for a detailed introduction.      Recall that E 1 (X, ω) admits a natural metric d1 :         for
ϕ, ψ ∈ E 1 (X, ω), given by
                              d1 (ϕ, ψ) := E(ϕ) + E(ψ) − 2E(ϕ ∧ ψ).
Here
                           ϕ ∧ ψ := sup {η ∈ PSH(X, ω) : η ≤ ϕ, η ≤ ψ} .
In [DDNL18c, Theorem 2.10], Darvas–Di Nezza–Lu proved that ϕ ∧ ψ ∈ E 1 (X, ω). They proved
in [DDNL18a, Section 3] that d1 is indeed a metric. The Monge–Ampère energy functional E :
E 1 (X, ω) → R is deﬁned as
                                                   n    Z
                                              1 X
                                   E(ϕ) =               ϕ ωϕi ∧ ω n−i .
                                            n + 1 i=0 X
  In this case, let R1 (X, ω) denote the set of geodesic rays in E 1 (X, ω) emanating from 0. For a
detailed study of R1 (X, ω), we refer to [DL20]. Here we only recall the deﬁnition of the metric on
R1 (X, ω). Given ℓ, ℓ′ ∈ R1 (X, ω), we deﬁne
                                                            1
                                      d1 (ℓ, ℓ′ ) := lim        d1 (ℓt , ℓ′t ).
                                                   t→∞ t

By [CC18, Corollary 5.5], t 7→ d1 (ℓt , ℓ′t ) is convex, guaranteeing the existence of the limit. It is
shown in [DL20] that (R1 (X, ω), d1 ) is a complete metric space.
  The following notion is introduced in [Xia23a]:
Definition 7.11. A rooftop metric space is a triple (E, d, ∧): (E, d) is a metric space and ∧ :
E × E → E is an associative, commutative binary operator on E satisfying
                                        d(a ∧ c, b ∧ c) ≤ d(a, b)
for any a, b, c ∈ E.
    For ℓ, ℓ′ ∈ R1 (X, ω), deﬁne ℓ ∧ ℓ′ as the greatest geodesic in R1 (X, ω) that lies below both ℓ and
ℓ′ . It is shown in [Xia23a, Theorem 7.6] that ∧ is well-deﬁned and (R1 (X, ω), d1 , ∧) is a complete
rooftop metric space.
    The energy functional E : R1 (X, ω) → R is deﬁned as
                                             E(ℓ) := E(ℓ1 ).
Recall that we have the following two maps: given any ℓ ∈ R1 (X, ω), its inverse Legendre transform
is deﬁned as
                                        ℓ̂τ := inf (ℓt − tτ ).
                                                  t≥0

Conversely, given any ψ• ∈ T C 1 (X, ω), we deﬁne its Legendre transform by

                                          ψ̌t := sup(ψτ + tτ ).
                                                 τ ∈R

They are inverse to each other, as proved in [DX22, Theorem 3.7].
                                     PARTIAL OKOUNKOV BODIES                                        39

Non-Archimedean pluripotential theory. Let X an be the Berkovich analytiﬁcation of X with respect
to the trivial valuation on X and Lan be the analytiﬁcation of L. See Section 2.7 for a brief
introduction. In the same section, we also recalled the deﬁnition of the space E 1 (Lan ) of non-
Archimedean psh metrics on Lan with ﬁnite energy and the energy functional E : E 1 (Lan ) → R.
   Next we brieﬂy explain the relation between the non-Archimedean pluripotential theory and the
complex pluripotential theory. Firstly, given a geodesic ray ℓ ∈ R1 (X, ω), one can associate a non-
Archimedean potential ℓan ∈ E 1 (Lan ) as in [BBJ21, Deﬁnition 4.2, Theorem 6.2]. The construction
of ℓan requires the notion of Gauss extension of valuations, as explained in [BBJ21, Section 3.1].
The map
                                         R1 (X, ω) → E 1 (Lan )
is surjective but not injective. It admits a canonical section
                                       ι : E 1 (Lan ) ֒→ R1 (X, ω)
sending φ ∈ E 1 (Lan ) to the maximal element ℓ ∈ E 1 (Lan ) with ℓan = φ. See [BBJ21, Theorem 6.6].
   The geodesics lying in the image of ι are known as maximal geodesic rays or approximable geodesic
rays. Moreover,
(7.10)                                     E(ι(α)) = E(α)
for any α ∈ E 1 (Lan ), see [BBJ21, Corollary 6.7].
  Maximal geodesic rays are closely related to test curves:
Theorem 7.12. The Legendre transform is a bijection from T C 1I (X, ω) (resp. T C 1 (X, ω)) to
ι(E 1 (Lan )) (resp. R1 (X, ω)), the converse is given by the inverse Legendre transform. Moreover,
for any ψ• ∈ T C 1 (X, ω),
(7.11)                                      E(ψ• ) = E(ψ̌).
  This is one of the main theorems of [DX22, Theorem 3.7, Theorem 3.17]. It is based on the
previous works [RWN14; DDNL18a].
Duistermaat–Heckman measures. The space E 1 (Lan ) is closely related to the theory of test conﬁgu-
rations. For the latter, we refer to [BHJ17, Section 2] for a brief introduction. Recall that two test
conﬁgurations (X , L) and (X ′ , L′ ) of (X, L) are said to be equivalent if they can be dominated by a
common test conﬁguration, see [BHJ17, Deﬁnition 6.1]. There is a natural injection from the set of
equivalence classes of test conﬁgurations to E 1 (Lan ). Moreover, this injection has dense image and
E 1 (Lan ) is the d1 -completion of the space of test conﬁgurations (modulo the equivalence relation).
These results are explained in detail in [DX22, Section 3.2].
    Given a test conﬁguration (X , L), Witt Nyström [WN12] constructed a naturally deﬁned Radon
measure DH(X , L) on R, called the Duistermaat–Heckman measure. See [BHJ17, Section 3.2] for
more details. It is not hard to see from the deﬁnition that DH(X , L) depends only on the equivalence
class of (X , L).
    In the sequel, we will deﬁne the Duistermaat–Heckman measure of an element in E 1 (Lan ). As
the space E 1 (Lan ) is the completion of the space of test conﬁgurations (modulo the equivalence
relation), our deﬁnition can be seen as an extension of Witt Nyström’s results [WN12].
Definition 7.13. For any α ∈ E 1 (Lan ), deﬁne the Duistermaat–Heckman measure of α as
                                                             
                                                     d .
                                        DH(α) := DH ι(α)

  We get a map DH : E 1 (Lan ) → M(R). Here M(R) denotes the space of Radon measures on R.
  For the proof of the next theorem, we need to recall several basic constructions of test curves.
  The space T C 1 (X, ω) is a rooftop metric space. Its rooftop structures (d1 , ∧) are induced from
the corresponding structures on R1 (X, ω).
40                                               MINGCHEN XIA

Corollary 7.14. Let ψ• , ϕ• , η• ∈ T C 1 (X, ω).
  (1) The rooftop operator on T C 1 (X, ω) is given by
(7.12)                                        (ψ ∧ ϕ)τ = ψτ ∧ ϕτ .
         It is the maximal element in T C 1 (X, ω) that lies below both ψ• and ϕ• . In particular,
(7.13)                               d1 ((ψ ∧ η)• , (ϕ ∧ η)• ) ≤ d1 (ψ• , ϕ• ).
                            1
     (2) The metric on T C (X, ω) is given by
(7.14)                          d1 (ψ• , ϕ• ) := E(ψ• ) + E(ϕ• ) − 2E((ψ ∧ ϕ)• ).
Proof. (1) Note that (7.13) is part of our deﬁnition of a rooftop structure.
   Observe that the bijection T C 1 (X, ω) → R1 (X, ω) is order-preserving. In order to prove our
claim, it suﬃces to show that (ϕ ∧ ψ)• deﬁned by (7.12) is indeed in T C 1 (X, ω), which is obvious.
   (2) This follows simply from (1) and (7.11).                                                   
   If ϕ• , ψ• ∈ T C 1I (X, ω), then (ψ ∧ ϕ)• ∈ T C 1I (X, ω) as well. This follows from the simple observa-
tion that the rooftop of two I-model potentials is still I-model. Now the d1 metric on T C 1 (X, ω)
restricts to a metric d1 on T C 1I (X, ω). The rooftop structure also restricts to a rooftop structure
on T C 1I (X, ω).
   We need the following constructions on test curves.
    (1) Increasing limit. Let ψ•α ∈ T C 1 (X, ω) be an increasing net. Assume that τψ+α is bounded
          from above. Deﬁne
                                             ψ̃τ := C[sup* ψτα ].
                                                               α
         Let τ + = inf{τ : ψ̃τ = −∞}. We deﬁne
                                               
                                                            ψ̃τ ,     τ 6= τ + ;
                                        ψτ =
                                                lim ψ̃σ ,             τ 6= τ + .
                                                   σ→τ + −

         It is easy to verify that ψ• ∈ T C 1 (X, ω).
     (2) Decreasing limit. Let ψ•α ∈ T C 1 (X, ω) be an increasing net and η• ∈ T C 1 (X, ω). Assume
         that ψ•α ≥ η• for all α. Deﬁne
                                               (inf ψ)τ := inf ψτα .
                                                                   α

         Then if (inf ψ )• is not identically −∞, then (inf ψ)• ∈ T C 1 (X, ω).
     (3) Max. Let ϕ• , ψ• ∈ T C 1 (X, ω). There is the smallest test curve (ϕ ∨ ψ)• ∈ T C 1 (X, ω) such
         that (ϕ ∨ ψ)• ≥ ϕ• , (ϕ ∨ ψ)• ≥ ψ• . In fact, we could simply deﬁne
                                          n                                            o
                       (ϕ ∨ ψ)τ := inf ητ : η• ∈ T C 1 (X, ω), η• ≥ ϕ• , η• ≥ ψ• .
         In terms of the Legendre transform, (ϕ ∨ ψ)ˇ is the minimal geodesic ray lying above both
         ϕ̌ and ψ̌. We observe that
(7.15)             d1 (ϕ• , ψ• ) ≤ d1 (ϕ• , (ϕ ∨ ψ)• ) + d1 (ψ• , (ϕ ∨ ψ)• ) ≤ C0 d1 (ϕ• , ψ• )
         for some C0 (n) > 0. See [DDNL21b, Proposition 2.15] for the proof of the latter inequality.
         Moreover, if η• ∈ T C 1 (X, ω) and if ϕ• ≤ ψ• , then
(7.16)                               d1 ((ϕ ∨ η)• , (ψ ∨ η)• ) ≤ d1 (ϕ• , ψ• ).
         This follows from the corresponding inequality of geodesic rays, which in turn follows from
         [Xia23a, Proposition 4.12] (Proposition 6.8 in the arXiv version).
           We also observe that the operator ∨ is associative and commutative, hence, we could also
         deﬁne ψ•1 ∨ · · · ∨ ψ•k in the obvious way.
                                             PARTIAL OKOUNKOV BODIES                                          41


Lemma 7.15. Let ψ•j , ψ• ∈ T C 1 (X, ω). Assume that one of the following conditions holds
      (1) ψ•j is increasing and ψ• is the increasing limit of ψ•j .
      (2) ψ•j is decreasing and ψ• = (inf ψ)• .
            d
Then ψ•j −→
          1
            ψ• .
Proof. We assume that condition (2) holds, the other case is similar. First observe that τψ+j → τψ+ .
It suﬃces to observe that
                                                          Z             Z ∞ Z          Z         
                      d1 (ψ•j , ψ• ) = (τψ+j − τψ+ )              n
                                                                  ω +             ω nj −   ωψnτ       dτ.
                                                              X         −∞       X ψτ    X
The assertion is a simple consequence of dominated convergence theorem.                                       
Theorem 7.16. The map DH : E 1 (Lan ) → M(R) is continuous.
  For any α ∈ E 1 (Lan ),
                                                Z
(7.17)                                                  x dDH(α)(x) = E(α)
                                                  R
and
                                                    Z
                                                                        1 n
(7.18)                                                    DH(α) =          (L ).
                                                      R                 n!
Proof. We ﬁrst prove the continuity of DH.
   By the dominated convergence theorem, it suﬃces to show that G[ψ• ](x) depends continuously
on ψ• for almost all x ∈ Int ∆(L). To be more precise, let ψ•j ∈ T C 1I (X, ω) be a sequence converging
to ψ• . We want to show that
                                       G[ψ•j ](x) → G[ψ• ](x)
for almost all x ∈ Int ∆(L). We will reduce to the case where ψ•j is either increasing or decreasing.
In these cases, it suﬃces to show that G[ψ•j ] → G[ψ• ] in L1 . By (7.4) and (7.9), this amounts to
showing that E(ψ•j ) → E(ψ• ). The latter follows from Lemma 7.15.
   In order to make the reduction, we will prove that after passing to a subsequence, there exists
an increasing sequence ϕj• ∈ T C 1I (X, ω) and a decreasing sequence η•j ∈ T C 1I (X, ω) such that
                          d             d
ϕj• ≤ ψ•j ≤ η•j and ϕj• −→
                         1
                           ψ• , η•j −→
                                     1
                                       ψ• . In fact, we can relax the requirement to ϕj• , η•j ∈ T C 1 (X, ω),
not necessarily I-model. Then it suﬃces to replace both test curves by their pointwise I-projections,
which satisfy the same conditions by [DX22, Theorem 3.18].
   Up to subtracting a subsequence, we may assume that for all j,
                                                        d1 (ψ•j , ψ• ) ≤ 2−j .
  For k ≥ j ≥ 0, we set
                                        η•j,k := ψ•j ∨ · · · ∨ ψ•k ∈ T C 1 (X, ω).
Let η•j ∈ T C 1 (X, ω) be the increasing limit of η•j,k as k → ∞. We then have
                 d1 (η•j,k , ψ• ) ≤d1 (ψ• , (ψ ∨ ψ j )• ) + d1 ((ψ ∨ ψ j )• , (ψ ∨ ψ j ∨ ψ j+1 )• ) + · · ·
                                  + d1 ((ψ ∨ ψ j ∨ · · · ∨ ψ k−1 )• , (ψ ∨ ψ j ∨ · · · ∨ ψ k )• )
                                ≤d1 (ψ• , (ψ ∨ ψ j )• ) + · · · + d1 (ψ• , (ψ ∨ ψ k )• )
                                      k
                                      X
                                ≤C0         d1 (ψ• , ψ•i )
                                      i=j

                                ≤C0 21−j .
Here the second inequality follows from (7.16), the third inequality follows from (7.15). Then by
                                                                             d
Lemma 7.15, we ﬁnd that d1 (η•j , ψ• ) ≤ C21−j . Thus, η•j −→
                                                            1
                                                              ψ• .
42                                                              MINGCHEN XIA

     Similarly, for k ≥ j ≥ 0, let
                                                   ϕj,k   j            k      1
                                                    • := ψ• ∧ · · · ∧ ψ• ∈ T C (X, ω).

The same argument as above shows that for k ≥ j ≥ 0, d1 (ϕj,k
                                                          • , ψ• ) ≤ 2
                                                                      1−j . Let

                                                                ψτj := inf ϕj,k
                                                                            τ .
                                                                        k≥j

By monotone convergence theorem, we ﬁnd that ψ j ∈ T C 1 (X, ω). Thus, by Lemma 7.15,
d1 (ϕj• , ψ• ) ≤ 21−j .
   Next we prove (7.17). Let α ∈ E 1 (Lan ). Let ψ• be the test curve corresponding to α. We need
to compute                      Z                  Z
                                                         x DH(α)(x) =                   G[ψ• ] dλ.
                                                     R                         ∆(L)
By (7.3), (7.4) and (7.9), the right-hand side is just E(ψ• ), which is equal to E(α) by (7.10) and
(7.11).
   Finally, (7.18) follows from (7.8).                                                            
Remark 7.17. On the subspace HNA , the Duistermaat–Heckman measure is the same as the one
deﬁned in [BHJ17, Section 3.2]. This follows from Theorem 5.28 and [BC11, Theorem A]. On
the other hand, in [Ino22, Deﬁnition 3.56], Inoue deﬁned the Duistermaat–Heckman measure for a
general non-Archimedean metric on Lan . As explained in [Ino22, Remark 1.4], his deﬁnition agrees
with ours for metrics in E 1 (Lan ).

                                                            8. Toric setting
     This section is devoted to a toric interpretation of the partial Okounkov body construction.
8.1. Technical lemmata.
Lemma 8.1. Let α, β1 , . . . , βm ∈ Zn . Let ∆ be the convex polytope generated by β1 , . . . , βm . Then
the following are equivalent:
    (1)
                                                                      m
                                                                                       !−1
                                                                      X
(8.1)                                                       |z α |2         |z βi |2
                                                                      i=1
          is a bounded function on C∗n .
      (2) α ∈ ∆.
                                                    P                                        P
Proof. (2) implies (1): Write α =                      i ti βi , where ti ∈ [0, 1], i ti = 1. Then
                    m
                                     !−1                         m
                                                                          ! −1                   m
                                                                                                                             !−1
                    X                          Y                 X                YX             X
          |z α |2         |z βi |2         =          βi 2ti
                                                    |z |             βi 2
                                                                      |z |             ≤  βj 2ti
                                                                                                     |z |         |z βi |2         ≤ 1.
                    i=1                        i               i=1                         i     j          i=1

  (1) implies (2): Assume that α 6∈ ∆. Let H be a hyperplane that separates α and ∆. Say H is
deﬁned by a1 x1 + · · · + an xn = C. Set
                                                           z(t) := (ta1 , . . . , tan ).
Then clearly (8.1) evaluated at z(t) is not bounded.                                                                                      
Lemma 8.2. Let β1 , . . . , βm ∈ Nn and β ∈ Rn . Then the following are equivalent
         P
  (1) log m i=1 e
                 x·βi − (x, β) is bounded from below.

  (2) β is in the convex hull of the βi ’s.
Proof. The proof follows the same pattern as Lemma 8.1.                                                                                   
                                     PARTIAL OKOUNKOV BODIES                                          43

8.2. Toric Okounkov bodies. Let X be an n-dimensional smooth projective toric variety, corre-
sponding to a smooth complete fan Σ in NR ∼        = Rn . Let N be the lattice in NR , whose dual is the
character lattice M . Let T := N ⊗Z C be the corresponding torus. Deﬁne MR = NR∨ . Given any
                                           ∗

T -invariant divisor D on X, let PD ⊆ MR be the polyhedron associated with D.
   Let D1 , . . . , Ds be the class of prime T -invariant divisors on X, each corresponding to a ray ρi
in Σ. Let vi be the primitive generator of ρi . Any T -invariant admissible ﬂag Y• has the following
form after renumbering the Di ’s:
                                             Yi = D1 ∩ · · · ∩ Di .
Now the vi ’s induce an isomorphism Φ : M → Zn , u 7→ ((u, vi ))i . Let ΦR : MR → Rn be the
extension of φ to MR and σ be the cone generated by the vi ’s. Let Uσ be the corresponding orbit
of T . Given any T -invariant line bundle, there is a unique T -invariant divisor D with D|Uσ = 0
such that OX (D) = L.
   It is shown in [LM09, Proposition 6.1] that
(8.2)                                 Γk (L) = ΦR ((kPD ) ∩ M )
for suﬃciently divisible k. We will omit ΦR from out notations from now on.
   Let Tc be the compact torus in T . Next consider a Tc -invariant metric φ on L. An unpublished
result of Yi Yao says that in the toric setting, two invariant potentials φ′ , φ′′ are I-equivalent if
and only if ∇φ′R (Rn ) = ∇φ′′R (Rn ). In other words, in the toric setting, for the invariant potentials,
the P [•]-envelope is the same as the P [•]I -envelope. In particular,
                                                       Z
                                                     1
                                        vol(L, φ) =       (ddc φ)n
                                                    n! X
always holds, without having to take the P [•]I -envelope. For the proof of a more general result,
we refer to [BBGHdJ21, Theorem 3.13, Proposition 3.11].
   Let U0 be the maximal orbit of T . The basis (vi ) allows us to identify U0 = C∗n . We denote
the coordinates on C∗n by (z1 , . . . , zn ), zi = xi + iyi . Fix a T -invariant section s0 of L on U0
corresponding to D. Then we can identify φ with a Tc -invariant function on U0 . Given the
identiﬁcation U0 = C∗n , φ can be identiﬁed with a convex function φR : Rn → R such that
∇φR ⊆ PD . We let PD,φ be the closure of the image of ∇φ. By [BB13, Lemma 2.5], PD,φ
corresponds to the closure of
                     QD,φ := {y ∈ MR : φ(x) − (x, y) is bounded from below} .
  We will be more explicit at this point. Assume that
                                                 a
                                                 X
                                       φ = log         |si |2 + O(1),
                                                 i=1

where si ∈ H0 (X, L).     Let βi be the lattice points in PD corresponding to si . In this case, QD,φ is
just the convex polytope generated by the βi ’s by Lemma 8.2.
   Consider α ∈ M ∩PD . It corresponds to a Laurent polynomial z α on C∗n . Observe that α ∈ QD,φ
if and only if |z α |2 e−φ is bounded from above. This is just a reformulation of Lemma 8.1.
   Thus, we ﬁnd
(8.3)                               Γk (W 0 (L, φ)) = (kQD,φ ) ∩ M
when k is suﬃciently divisible. Hence, ∆(L, φ) ⊇ PD,φ . Comparing the volumes, we ﬁnd that
equality holds.
  Next we deal with Tc -invariant φ such that ddc φ is a Kähler current. Let φj be an equivari-
ant quasi-equisingular approximation of φ constructed as in [Dem12, Corollary 13.23]. Then by
deﬁnition,                                     \
                                    ∆(L, φ) = ∆(L, φj ).
                                                       j
44                                                        MINGCHEN XIA

On the other hand,
                                                                          \
                                                        PD,φ ⊆                PD,φj .
                                                                          j
Hence, PD,φ ⊆ ∆(L, φ). On the other hand, the volume of both sides agree, so they are indeed
equal thanks to the assumption that φ has analytic singularities.
   In general, if φ is Tc -invariant and has positive volume. Let ψ ≤ φ be a potential with ddc ψ
being a Kähler current. We may guarantee that ψ is Tc -invariant. Then by deﬁnition, if we set
φǫ = (1 − ǫ)φ + ǫψ, then
                                                                          [
                                                  ∆(L, φ) =                     ∆(L, φǫ ).
                                                                      ǫ∈(0,1)
While
                                                                      \
                                                      PD,φ ⊇              PD,P [φǫ ]I .
                                                                      ǫ
Thus, ∆(L, φ) ⊇ PD,φ . Comparing the volumes, we ﬁnd that these convex bodies are equal.
Theorem 8.3. Let φ be a Tc -invariant psh metric on L with positive volume. Then
                                                         ∆(L, φ) = PD,φ
under the identification ΦR as above.
8.3. Mixed volumes of line bundles. Let X, T be as in Section 8.2.
Lemma 8.4. Let L1 , . . . , Ln be big and nef T -invariant line bundles on X. Assume that the flag
is T -invariant. Then
                              1
(8.4)                            (L1 , . . . , Ln ) = vol(∆(L1 ), . . . , ∆(Ln )).
                              n!
  Here vol denotes the mixed volume functional. We refer to [Sch14, Section 5.1] for the precise
deﬁnition.
  As pointed out by Rémi Reboulet, this result is already proved in [BGPS14, Proposition 3.4.3].
Proof. Step 1. We ﬁrst assume that all Li ’s are ample.
  In this case, we know that for any ti ∈ N (i = 1, . . . , n),
                                                       n
                                                                      !       n
                                                       X                      X
                                                 ∆           t i Li       =         ti ∆(Li )
                                                       i=1                    i=1

by [Kav11, Theorem 3.1]. Hence,
                          n
                                         !                                !
                          X                           X               n α
                  vol ∆         t i Li       =                          t vol (∆(L1 )α1 , . . . , ∆(Ln )αn ) .
                          i=1                    α∈Nn ,|α|=n
                                                                      α

On the other hand, by (1.3),
                                  n
                                                  !                                   !
                                  X                     1     X        n α α1
                       vol ∆             t i Li       =                  t (L1 , . . . , Lαnn ) .
                                  i=1
                                                        n! α∈Nn ,|α|=n α

Comparing the coeﬃcients, we ﬁnd (8.4).
   Step 2. General case.
   The results of Step 1 generalize immediately to ample Q-divisors. Hence, the nef case follows
from a simple perturbation argument.                                                          
     The following example is due to Chen Jiang.
                                      PARTIAL OKOUNKOV BODIES                                         45

Example 8.5. If the flag is not toric invariant, Lemma 8.4 fails. For example, consider X =
P1 × P1 , L1 = O(1, 2) and L2 = O(2, 1). Take a flag X = Y0 ⊇ Y1 ⊇ Y2 with Y1 being the diagonal.
In this case, (8.4) fails.
   In this case, (L1 , L2 ) = 5. By a simple computation using [LM09, Theorem 6.4], we find ∆(L1 ) =
∆(L2 ) is the trapezoid shown in Fig. 1. In particular,
                                                                      5
                                     vol(∆(L1 ), ∆(L2 )) = 2 <           .
                                                                      2!


                                                     y
                                                 3
                                                 2
                                                 1

                                                     0 1              x
                                     −3 −2 −1                2   3
                                            −1
                                                −2
                                                −3




                                      Figure 1. Okounkov body


   For simplicity, we call (L, φ) a T -invariant Hermitian big line bundle on X if (T, φ) is a Hermitian
big line bundle on X, L is T -invariant and φ is Tc -invariant.
Corollary 8.6. Let (Li , φi ) (i = 1, . . . , n) be T -invariant Hermitian big line bundles on X with
positive volumes. If the T -invariant flag satisfies that Yn is not contained in any of the polar loci
of the φi ’s, then
                       Z
                     1
(8.5)                     ddc φ1 ∧ · · · ∧ ddc φn = vol(∆(L1 , φ1 ), . . . , ∆(Ln , φn )).
                    n! X
Proof. According to Proposition 5.16, by perturbing Li , we may assume that each ddc φi is a Kähler
current.
   Observe that both sides of (8.5) are continuous under dS -approximations of φi : the left-hand
side follows from Theorem 4.2 and the right-hand side follows from Theorem 5.9.
   Hence, by [DX21, Lemma 3.7], we may assume that each φi has analytic singularities. Taking
a birational resolution, we may assume that φi has analytic singularities along normal crossing
Q-divisor Ei . By Remark 5.1, we reduce to the situation of Lemma 8.4.                           
  We have ﬁnished the proof of Theorem D.
Corollary 8.7. Let L1 , . . . , Ln be big T -invariant line bundles on X. Assume that the flag (Y• ) is
T -invariant and Yn is not contained in the non-Kähler locus of any c1 (Li ). Then
                              1
(8.6)                            hL1 , . . . , Ln i = vol(∆(L1 ), . . . , ∆(Ln )).
                              n!
  Here h•i denotes the movable intersection in the sense of [BDPP13; BFJ09].
Proof. It suﬃces to apply Corollary 8.6 to the case where φi has minimal singularities.               
46                                          MINGCHEN XIA

  Finally, we propose the following conjecture concerning the mixed volume of partial Okounkov
bodies in the non-toric setting:
Conjecture 8.8. Let (Li , φi ) (i = 1, . . . , n) be Hermitian big line bundles on X (not necessarily a
toric variety) with positive volumes. Then
                     Z
                  1
(8.7)                   ddc φ1 ∧ · · · ∧ ddc φn = sup vol(∆ν (L1 , φ1 ), . . . , ∆ν (Ln , φn )),
                  n! X                              ν
where ν runs over all rank n valuations C(X) → Zn .×

   To the best of the author’s knowledge, this conjecture is open even when the φi ’s have minimal
singularities.
                                         REFERENCES                                         47

                                        References
[AI22]     Omid Amini and Hernan Iriarte. Geometry of higher rank valuations. 2022. arXiv:
           2208.06237 [math.AG].
[BB10]     Robert Berman and Sébastien Boucksom. Growth of balls of holomorphic sections
           and energy at equilibrium. Invent. Math. 181.2 (2010), pp. 337–394. issn: 0020-9910.
           url: https://doi.org/10.1007/s00222-010-0248-9.
[BB13]     Robert J. Berman and Bo Berndtsson. Real Monge-Ampère equations and Kähler-
           Ricci solitons on toric log Fano varieties. Ann. Fac. Sci. Toulouse Math. (6) 22.4
           (2013), pp. 649–711. issn: 0240-2963,2258-7519. url: https://doi.org/10.5802/a
           fst.1386.
[BBGHdJ21] A. Botero, J. I. Burgos Gil, D. Holmes, and R. de Jong. Chern–Weil and Hilbert–
           Samuel formulae for singular hermitian line bundles. 2021. arXiv: 2112 . 09007
           [math.AG].
[BBJ21]    Robert J. Berman, Sébastien Boucksom, and Mattias Jonsson. A variational ap-
           proach to the Yau-Tian-Donaldson conjecture. J. Amer. Math. Soc. 34.3 (2021),
           pp. 605–652. issn: 0894-0347. url: https://doi.org/10.1090/jams/964.
[BBWN11]   Robert Berman, Sébastien Boucksom, and David Witt Nyström. Fekete points and
           convergence towards equilibrium measures on complex manifolds. Acta Math. 207.1
           (2011), pp. 1–27. issn: 0001-5962. url: https://doi.org/10.1007/s11511-011-0
           067-x.
[BC11]     Sébastien Boucksom and Huayi Chen. Okounkov bodies of ﬁltered linear series. Com-
           pos. Math. 147.4 (2011), pp. 1205–1229. issn: 0010-437X. url: https://doi.org/1
           0.1112/S0010437X11005355.
[BDPP13]   Sébastien Boucksom, Jean-Pierre Demailly, Mihai Păun, and Thomas Peternell. The
           pseudo-eﬀective cone of a compact Kähler manifold and varieties of negative Kodaira
           dimension. J. Algebraic Geom. 22.2 (2013), pp. 201–248. issn: 1056-3911. url: htt
           ps://doi.org/10.1090/S1056-3911-2012-00574-8.
[BEGZ10]   Sébastien Boucksom, Philippe Eyssidieux, Vincent Guedj, and Ahmed Zeriahi.
           Monge-Ampère equations in big cohomology classes. Acta Math. 205.2 (2010),
           pp. 199–262. issn: 0001-5962. url: https://doi.org/10.1007/s11511-010-0054
           -7.
[Ber90]    Vladimir G. Berkovich. Spectral theory and analytic geometry over non-Archimedean
           ﬁelds. Vol. 33. Mathematical Surveys and Monographs. American Mathematical So-
           ciety, Providence, RI, 1990, pp. x+169. isbn: 0-8218-1534-2. url: https://doi.or
           g/10.1090/surv/033.
[BFJ08]    S. Boucksom, C. Favre, and M. Jonsson. Valuations and plurisubharmonic singular-
           ities. Publications of the Research Institute for Mathematical Sciences 44.2 (2008),
           pp. 449–494.
[BFJ09]    Sébastien Boucksom, Charles Favre, and Mattias Jonsson. Diﬀerentiability of vol-
           umes of divisors and a problem of Teissier. J. Algebraic Geom. 18.2 (2009), pp. 279–
           308. issn: 1056-3911. url: https://doi.org/10.1090/S1056-3911-08-00490-6.
[BGPS14]   José Ignacio Burgos Gil, Patrice Philippon, and Martín Sombra. Arithmetic ge-
           ometry of toric varieties. Metrics, measures and heights. Astérisque 360 (2014),
           pp. vi+222. issn: 0303-1179,2492-5926.
[BHJ17]    Sébastien Boucksom, Tomoyuki Hisamoto, and Mattias Jonsson. Uniform K-stability,
           Duistermaat-Heckman measures and singularities of pairs. Ann. Inst. Fourier
           (Grenoble) 67.2 (2017), pp. 743–841. issn: 0373-0956. url: http : / / aif . cedra
           m.org/item?id=AIF_2017__67_2_743_0.
48                                      REFERENCES

[BJ22]    Sébastien Boucksom and Mattias Jonsson. Global pluripotential theory over a triv-
          ially valued ﬁeld. Ann. Fac. Sci. Toulouse Math. (6) 31.3 (2022), pp. 647–836. issn:
          0240-2963,2258-7519. url: https://doi.org/10.5802/afst.170.
[Bou02a]  S. Boucksom. Cônes positifs des variétés complexes compactes. Université Joseph-
          Fourier-Grenoble I, 2002.
[Bou02b]  S. Boucksom. Higher dimensional Zariski decompositions. 2002. arXiv: 0204336
          [math.AG].
[Bou17]   S. Boucksom. Singularities of plurisubharmonic functions and multiplier ideals. htt
          p://sebastien.boucksom.perso.math.cnrs.fr/notes/L2.pdf. 2017.
[Cao14]   Junyan Cao. Numerical dimension and a Kawamata-Viehweg-Nadel-type vanishing
          theorem on compact Kähler manifolds. Compos. Math. 150.11 (2014), pp. 1869–1902.
          issn: 0010-437X. url: https://doi.org/10.1112/S0010437X14007398.
[CC18]    X. Chen and J. Cheng. On the constant scalar curvature Kähler metrics, general
          automorphism group. 2018. arXiv: 1801.05907 [math.DG].
[CFKL+17] Ciro Ciliberto, Michal Farnik, Alex Küronya, Victor Lozovanu, Joaquim Roé, and
          Constantin Shramov. Newton-Okounkov bodies sprouting on the valuative tree.
          Rend. Circ. Mat. Palermo (2) 66.2 (2017), pp. 161–194. issn: 0009-725X,1973-4409.
          url: https://doi.org/10.1007/s12215-016-0285-3.
[CHPW18a] Sung Rak Choi, Yoonsuk Hyun, Jinhyung Park, and Joonyeong Won. Asymptotic
          base loci via Okounkov bodies. Adv. Math. 323 (2018), pp. 784–810. issn: 0001-
          8708,1090-2082. url: https://doi.org/10.1016/j.aim.2017.11.007.
[CHPW18b] Sung Rak Choi, Yoonsuk Hyun, Jinhyung Park, and Joonyeong Won. Okounkov
          bodies associated to pseudoeﬀective divisors. J. Lond. Math. Soc. (2) 97.2 (2018),
          pp. 170–195. issn: 0024-6107,1469-7750. url: https://doi.org/10.1112/jlms.12
          107.
[Dar19]   Tamás Darvas. Geometric pluripotential theory on Kähler manifolds. Advances in
          complex geometry. Vol. 735. Contemp. Math. Amer. Math. Soc., [Providence], RI,
          2019, pp. 1–104. isbn: 978-1-4704-4333-7. url: https://doi.org/10.1090/conm/7
          35/14822.
[DDNL18a] Tamás Darvas, Eleonora Di Nezza, and Chinh H. Lu. L1 metric geometry of big
          cohomology classes. Ann. Inst. Fourier (Grenoble) 68.7 (2018), pp. 3053–3086. issn:
          0373-0956. url: http://aif.cedram.org/item?id=AIF_2018__68_7_3053_0.
[DDNL18b] Tamás Darvas, Eleonora Di Nezza, and Chinh H. Lu. Monotonicity of nonpluripolar
          products and complex Monge-Ampère equations with prescribed singularity. Anal.
          PDE 11.8 (2018), pp. 2049–2087. issn: 2157-5045. url: https://doi.org/10.214
          0/apde.2018.11.2049.
[DDNL18c] Tamás Darvas, Eleonora Di Nezza, and Chinh H. Lu. On the singularity type of full
          mass currents in big cohomology classes. Compos. Math. 154.2 (2018), pp. 380–409.
          issn: 0010-437X. url: https://doi.org/10.1112/S0010437X1700759X.
[DDNL21a] Tamás Darvas, Eleonora Di Nezza, and Chinh H. Lu. Log-concavity of volume and
          complex Monge-Ampère equations with prescribed singularity. Math. Ann. 379.1-2
          (2021), pp. 95–132. issn: 0025-5831. url: https://doi.org/10.1007/s00208-019
          -01936-y.
[DDNL21b] Tamás Darvas, Eleonora Di Nezza, and Hoang-Chinh Lu. The metric geometry of
          singularity types. J. Reine Angew. Math. 771 (2021), pp. 137–170. issn: 0075-4102.
          url: https://doi.org/10.1515/crelle-2020-0019.
[Dem12]   Jean-Pierre Demailly. Analytic methods in algebraic geometry. Vol. 1. Surveys of
          Modern Mathematics. International Press, Somerville, MA; Higher Education Press,
          Beijing, 2012, pp. viii+231. isbn: 978-1-57146-234-3.
                                         REFERENCES                                          49

[Dem15]   Jean-Pierre Demailly. On the cohomology of pseudoeﬀective line bundles. Complex
          geometry and dynamics. Vol. 10. Abel Symp. Springer, Cham, 2015, pp. 51–99.
[Den17]   Ya Deng. Transcendental Morse inequality and generalized Okounkov bodies. Algebr.
          Geom. 4.2 (2017), pp. 177–202. issn: 2313-1691,2214-2584. url: https://doi.org
          /10.14231/AG-2017-009.
[DL20]    Tamás Darvas and Chinh H. Lu. Geodesic stability, the space of rays and uniform
          convexity in Mabuchi geometry. Geom. Topol. 24.4 (2020), pp. 1907–1967. issn:
          1465-3060. url: https://doi.org/10.2140/gt.2020.24.1907.
[DPS01]   Jean-Pierre Demailly, Thomas Peternell, and Michael Schneider. Pseudo-eﬀective
          line bundles on compact Kähler manifolds. Internat. J. Math. 12.6 (2001), pp. 689–
          741. issn: 0129-167X. url: https://doi.org/10.1142/S0129167X01000861.
[DRWN+23] Tamás Darvas, Rémi Reboulet, David Witt Nyström, Mingchen Xia, and Kewei
          Zhang. Transcendental Okounkov bodies. 2023. arXiv: 2309.07584 [math.DG].
[DX21]    T. Darvas and M. Xia. The volume of pseudoeﬀective line bundles and partial equi-
          librium. Geometry & Topology (2021). arXiv: 2112.03827 [math.DG].
[DX22]    Tamás Darvas and Mingchen Xia. The closures of test conﬁgurations and algebraic
          singularity types. Adv. Math. 397 (2022), Paper No. 108198, 56. issn: 0001-8708.
          url: https://doi.org/10.1016/j.aim.2022.108198.
[FK18]    Kazuhiro Fujiwara and Fumiharu Kato. Foundations of rigid geometry. I. EMS
          Monographs in Mathematics. European Mathematical Society (EMS), Zürich, 2018,
          pp. xxxiv+829. isbn: 978-3-03719-135-4.
[GZ17]    V. Guedj and A. Zeriahi. Degenerate Complex Monge–Ampère Equations. 2017.
[Ino22]   Eiji Inoue. Entropies in µ-framework of canonical metrics and K-stability, II – Non-
          archimedean aspect: non-archimedean µ-entropy and µK-semistability. 2022. arXiv:
          2202.12168 [math.AG].
[Jow10]   Shin-Yao Jow. Okounkov bodies and restricted volumes along very general curves.
          Adv. Math. 223.4 (2010), pp. 1356–1371. issn: 0001-8708. url: https://doi.org/1
          0.1016/j.aim.2009.09.015.
[Kav11]   Kiumars Kaveh. Note on cohomology rings of spherical varieties and volume poly-
          nomial. J. Lie Theory 21.2 (2011), pp. 263–283. issn: 0949-5932.
[Kho92]   A. G. Khovanskiı̆. The Newton polytope, the Hilbert polynomial and sums of ﬁnite
          sets. Funktsional. Anal. i Prilozhen. 26.4 (1992), pp. 57–63, 96. issn: 0374-1990,2305-
          2899. url: https://doi.org/10.1007/BF01075048.
[KK12]    Kiumars Kaveh and A. G. Khovanskii. Newton-Okounkov bodies, semigroups of
          integral points, graded algebras and intersection theory. Ann. of Math. (2) 176.2
          (2012), pp. 925–978. issn: 0003-486X. url: https://doi.org/10.4007/annals.20
          12.176.2.5.
[LM09]    Robert Lazarsfeld and Mircea Mustaţă. Convex bodies associated to linear series.
          Ann. Sci. Éc. Norm. Supér. (4) 42.5 (2009), pp. 783–835. issn: 0012-9593. url:
          https://doi.org/10.24033/asens.2109.
[MM07]    Xiaonan Ma and George Marinescu. Holomorphic Morse inequalities and Bergman
          kernels. Vol. 254. Progress in Mathematics. Birkhäuser Verlag, Basel, 2007, pp. xiv+422.
          isbn: 978-3-7643-8096-0.
[Oko03]   Andrei Okounkov. Why would multiplicities be log-concave? The orbit method in
          geometry and physics (Marseille, 2000). Vol. 213. Progr. Math. Birkhäuser Boston,
          Boston, MA, 2003, pp. 329–347. isbn: 0-8176-4232-3.
[Oko96]   Andrei Okounkov. Brunn-Minkowski inequality for multiplicities. Invent. Math.
          125.3 (1996), pp. 405–411. issn: 0020-9910,1432-1297. url: https://doi.org/10
          .1007/s002220050081.
50                                    REFERENCES

[RWN14]    Julius Ross and David Witt Nyström. Analytic test conﬁgurations and geodesic rays.
           J. Symplectic Geom. 12.1 (2014), pp. 125–169. issn: 1527-5256. url: https://doi
           .org/10.4310/JSG.2014.v12.n1.a5.
[Sch14]    R. Schneider. Convex bodies: the Brunn–Minkowski theory. 151. Cambridge univer-
           sity press, 2014.
[WN12]     David Witt Nyström. Test conﬁgurations and Okounkov bodies. Compos. Math.
           148.6 (2012), pp. 1736–1756. issn: 0010-437X. url: https://doi.org/10.1112/S0
           010437X12000358.
[WN14]     David Witt Nyström. Transforming metrics on a line bundle to the Okounkov body.
           Ann. Sci. Éc. Norm. Supér. (4) 47.6 (2014), pp. 1111–1161. issn: 0012-9593. url:
           https://doi.org/10.24033/asens.2235.
[WN19]     David Witt Nyström. Monotonicity of non-pluripolar Monge-Ampère masses. Indi-
           ana Univ. Math. J. 68.2 (2019), pp. 579–591. issn: 0022-2518. url: https://doi.o
           rg/10.1512/iumj.2019.68.7630.
[Xia22]    Mingchen Xia. Non-pluripolar products on vector bundles and Chern–Weil formulae
           on mixed Shimura varieties. 2022. arXiv: 2210.15342 [math.AG].
[Xia23a]   Mingchen Xia. Mabuchi geometry of big cohomology classes. J. Reine Angew. Math.
           798 (2023), pp. 261–292. issn: 0075-4102,1435-5345. url: https://doi.org/10.15
           15/crelle-2023-0019.
[Xia23b]   Mingchen Xia. Pluripotential-theoretic stability thresholds. Int. Math. Res. Not.
           IMRN 14 (2023), pp. 12324–12382. issn: 1073-7928,1687-0247. url: https://do
           i.org/10.1093/imrn/rnac186.
[Zah75]    V. P. Zaharjuta. Transﬁnite diameter, Čebyšev constants and capacity for a com-
           pactum in C n . Mat. Sb. (N.S.) 96(138) (1975), pp. 374–389, 503. issn: 0368-8666.


# Complete actual public primary text: 1210.5692v1

                                                    NUMERICAL DIMENSION AND A
                                               KAWAMATA-VIEHWEG-NADEL TYPE VANISHING
                                               THEOREM ON COMPACT KÄHLER MANIFOLDS
arXiv:1210.5692v1 [math.AG] 21 Oct 2012




                                                                             JUNYAN CAO


                                                 Abstract. Let X be a compact Kähler manifold and let L be a pseudo-
                                                 effective line bundle on X with singular metric ϕ. We first define a no-
                                                 tion of numerical dimension of the pseudo-effective pair (L, ϕ) and then
                                                 discuss the properties of it. We prove also a very general Kawamata-
                                                 Viehweg-Nadel type vanishing theorem on an arbitrary compact Kähler
                                                 manifold.




                                                                          1. Introduction
                                             Let X be a compact Kähler manifold and let (L, ϕ) be a pseudo-effective
                                          line bundle on X (c.f Section 3 for the definition of a pseudo-effective pair
                                          (L, ϕ)). H.Tsuji [Tsu] has defined a notion of numerical dimension by an
                                          algebraic method:
                                          Definition 1. Let X be a projective variety and (L, ϕ) a pseudo-effective
                                          line bundle. One defines
                                                     νnum (L, ϕ) = sup{dim V | V subvariety of X such that

                                                           ϕ is well defined on V and (V, L, ϕ) is big.}

                                          Here (V, L, ϕ) to be big means that there is a desingularization π : Ve → V
                                          such that
                                                                   h0 (Ve , mπ ∗ (L) ⊗ I(mϕ ◦ π))
                                                              lim                                 >0
                                                             m→∞                   mn
                                          where n is the dimension of V . 1
                                             Since Tsuji’s definition depends on the existence of subvarieties, it is more
                                          convenient to find an analytic definition if the base manifold is not projec-
                                          tive. Following a suggestion of J-P. Demailly, we first define a notion of
                                          numerical dimension nd(L, ϕ) (cf. Definition 4) for a pseudo-effective line
                                          bundle (L, ϕ) on a manifold X which is just assumed to be compact Kähler.
                                          The definition involves a certain cohomological intersection product of pos-
                                          itive currents, introduced in Section 2. We then discuss the properties of
                                          nd(L, ϕ) in Section 3 and 4. The main properties are as follows.

                                            1[Tsu] proved that the bigness does not depend on the choice of desingularization.
                                                                                    1
2                               JUNYAN CAO

Proposition 1.1. Let (L, ϕ) be a pseudo-effective line bundle on a projective
variety X of dimension n and nd(L, ϕ) = n. Then
                          h0 (X, mL ⊗ I(mϕ))
                       lim                   > 0.
                      m→∞         mn
Proposition 1.2. Let (L, ϕ) be a pseudo-effective line bundle on a projective
variety X. Then
                         νnum (L, ϕ) = nd(L, ϕ).
  Our main interest in this article is to prove a very general Kawamata-
Viehweg-Nadel type vanishing theorem on an arbitrary compact Kähler
manifold. Our statement is as follows.
Theorem 1.3. Let (L, ϕ) be a pseudo-effective line bundle on a compact
Kähler manifold X of dimension n. Then
      H p (X, KX ⊗ L ⊗ I+ (ϕ)) = 0       for any p ≥ n − nd(L, ϕ) + 1,
where I+ (ϕ) is the upper semicontinuous variant of the multiplier ideal sheaf
associated to ϕ (cf. [FJ]).
   The organization of the article is as follows. In Section 2, we first re-
call some elementary results about the analytic multiplier ideal sheaves and
define our cohomological product of positive currents by quasi-equisingular
approximation. In Section 3, using the product defined in Section 2, we give
our definition of the numerical dimension nd(L, ϕ) of pseudo-effective line
bundles with singular metrics. The main goal of this section is to give an
asymptotic estimate when nd(L, ϕ) = dim X. In section 4, we prove that
our numerical dimension coincides with the definition in [Tsu] when X is
projective. We also give a numerical criterion of the numerical dimension
and discuss a relationship between the numerical dimension without mul-
tiplier ideal sheaves and the numerical dimension defined here. In Section
5, we first give a quick proof of a Kawamata-Viehweg-Nadel type vanishing
theorem on projective varieties. We finally generalize the vanishing theorem
on arbitrary compact Kähler manifolds by the methods developed in [DP]
and [Mou].
Acknowledgements: I would like to thank Professor J-P. Demailly for
numerous ideas and suggestions for this article, and also for his patience
and disponibility.

         2. Cohomological product of positive currents
   We first recall some basic definitions and results about quasi-psh func-
tions. Let X be a complex manifold. We say that ϕ is a psh function (resp.
a quasi-psh function) on X, if
                  i∂∂ϕ ≥ 0,        (resp. i∂∂ϕ ≥ −c · ωX )
           A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                            3

where c is a positive constant and ωX is a smooth hermitian metric on X.
We say that a quasi-psh function ϕ has analytic singularities, if ϕ is locally
of the form                           X
                        ϕ(z) = c · ln(  |gi |2 ) + O(1)
with c > 0 and {gi } are holomorphic functions. Let ϕ, ψ be two quasi-psh
functions. We say that ϕ is less singular than ψ if
                                     ψ ≤ϕ+C
for some constant C. We denote it ϕ 4 ψ.
   We now recall the analytic definition of multiplier ideal sheaves. Let I(ϕ)
be the multiplier ideal sheaves associated to the quasi-psh function ϕ, i.e.
                                      Z
                   I(ϕ)x = {f ∈ OX |      |f |2 e−2ϕ < +∞}
                                            Ux
where Ux is some open neighborhood of x in X (cf. [Dem] for a more
detailed introduction to the concept of multiplier ideal sheaf). When ϕ
does not possess analytic singularities, we need to introduce the “upper
semicontinuous regularization” of the multiplier ideal sheaf, namely the ideal
sheaf
                        I+ (ϕ) = lim I((1 + ǫ)ϕ).
                                       ǫ→0+
By the Notherian property of coherent ideal sheaves, there exists an ǫ > 0
such that
                I+ (ϕ) = I((1 + ǫ′ )ϕ)     for any 0 < ǫ′ < ǫ.
When ϕ has analytic singularities, it is easy to see that I+ (ϕ) = I(ϕ).
Conjecturally we have the equality for all psh functions. 2
Important Convention: When we talk about a line bundle L on X, we
always first implicitly fix a smooth metric h0 on L. Given a singular metric
ϕ on L or sometimes ϕ for simplicity, we just means that the new metric on
L is given by h0 e−ϕ . Recall that the curvature of the metric ϕ for L is
                          i           i
                            Θϕ (L) =    Θh (L) + ddc ϕ.
                        2π           2π 0
                                                                 i
The pair (L, ϕ) is said to be a pseudo-effective line bundle if 2π Θϕ (L) ≥ 0
as a current.
           e → X be a modification of a smooth variety X, and let ϕ, ψ
   Let π : X
be two quasi-psh fuctions on X such that I(ϕ) ⊂ I(ψ). In general, this
inclusion does not imply I(ϕ ◦ π) ⊂ I(ψ ◦ π). We thus need the following
lemma.
Lemma 2.1. Let E = π ∗ KX − KXe . If I(ϕ) ⊂ I(ψ), then
                          I(ϕ ◦ π) ⊗ O(−E) ⊂ I(ψ ◦ π),
  2This equality is well known in dimension 1 and is proved to be true in dimension 2 by
Favre-Jonsson [FJ]. See [DP] for more details about I+ (ϕ).
4                                         JUNYAN CAO

where the sheaf O(−E) is the germs of holomorphic functions f such that
div(f ) ≥ E.
Proof. It is known that I(ϕ ◦ π) ⊂ π ∗ I(ϕ) (cf. Proposition 14.3 of [Dem]).
Then for any f ∈ I(ϕ ◦ π)x , we have
                         Z
                                π∗ (f )e−2ϕ < +∞,
                                 π(Ux )

where Ux is some open neighborhood of x and π(Ux ) is its image under π
which is not necessary open. Combining with the condition I(ϕ) ⊂ I(ψ),
we get
                        Z
(1.1)                        | π∗ f |2 e−2ψ < +∞.
                             π(Ux )

(1.1) implies that
                        Z
(1.2)                            | f |2 | J |2 e−2ψ◦π < +∞,
                            Ux

where J is Jacobian of π. Since O(−E) = J · OX , (1.2) implies the lemma.
                                                                       
  Let X be a compact Kähler manifold and let T be a closed positive (1, 1)-
current. It is well known that T can be written as
                                      T = θ + ddc ϕ,
where θ is a smooth (1, 1)-closed form representing [T ] ∈ H 1,1 (X, R) and ϕ is
a quasi-psh function. Demailly’s famous regularization theorem states that
ϕ can be approximated by a sequence of quasi-psh functions with analytic
singularities. We say that it is an analytic approximation of ϕ. Among all
these analytic approximations, we want to deal with those which keep the
information concerning the singularities of T . More precisely, we introduce
the following definition.
Definition 2. Let θ + ddc ϕ be a positive current, where θ is a smooth form
and ϕ is a quasi-psh function on a compact Kähler manifold (X, ω). We
say that {ϕk }∞k=1 is a quasi-equisingular approximation of ϕ for the current
θ + ddc ϕ if it satisfies the following conditions:
  (i) {ϕk }∞                          1
            k=1 converge to ϕ in L topology and
                                  θ + ddc ϕk ≥ −τk · ω
for some constants τk → 0 as k → +∞.
   (ii) all ϕk have analytic singularities and ϕk 4 ϕk+1 for any k.
   (iii) For any δ > 0 and m ∈ N, there exists k0 (δ, m) ∈ N such that
            I(m(1 + δ)ϕk ) ⊂ I(mϕ)               for every k ≥ k0 (δ, m)
Remark. By condition (i), such type of approximation depends not only on
ϕ but also on the current θ + ddc ϕ.
            A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                      5

   The existence of such quasi-equisingular approximations was proved in
Theorem 2.2.1 of [DPS 01] by a Bergman kernel method. The choice of such
approximations corresponds in some sense to the most singular approxima-
tions asymptotically. The following proposition makes this assertion more
precise.
Proposition 2.2. Let θ + ddc ϕ1 , θ + ddc ϕ2 be two positive currents on a
compact Kähler manifold X as usual. We assume that the quasi-psh function
ϕ2 is more singular than ϕ1 . Let {ϕi,1 }∞i=1 be an analytic approximation to
ϕ1 and let {ϕi,2 }∞
                  i=1 be a  quasi-equisingular approximation to ϕ2 . For any
closed smooth (n − 1, n − 1)-semi-positive form u, we have
                    Z                         Z
                          c
(2.1)          lim     (dd ϕi,1 )ac ∧ u ≥ lim    (ddc ϕi,2 )ac ∧ u
               i→∞ X                       i→∞ X

where (ddc ϕi,1 )ac denotes the absolutely continuous part of the current ddc ϕi,1 .
Proof. It is enough to show that
                 Z                         Z
                       c
(2.2)               (dd ϕs,1 )ac ∧ u ≥ lim   (ddc ϕi,2 )ac ∧ u
                   X                    i→∞ X

for any s ∈ N fixed. Since {ϕi,2 }∞
                                  i=1 is a quasi-equisingular approximation
to ϕ2 , for any δ > 0 and m ∈ N, there exists a k0 (δ, m) ∈ N such that
(2.3)       I(m(1 + δ)ϕk,2 ) ⊂ I(mϕ2 )        for every k ≥ k0 (δ, m).
Since ϕ1 4 ϕ2 and ϕs,1 4 ϕ1 , (2.3) implies that
(2.4)                     I(m(1 + δ)ϕk,2 ) ⊂ I(mϕs,1 )
for any s ∈ N fixed and k ≥ k0 (δ, m).
                                                 b → X be a log resolution
   Using (2.4), we begin to prove (2.2). Let π : X
of ϕs,1 . We can thus assume that
                            ddc ϕs,1 ◦ π = [F ] + C ∞ ,
where F is a R-normal crossing divisor. Using Lemma 2.1, (2.4) implies that
(2.5)       I(m(1 + δ)ϕk,2 ◦ π) ⊗ O(−J) ⊂ I(mϕs,1 ◦ π) = O(−⌊mF ⌋)
for k ≥ k0 (δ, m), where J is the Jacobian of the blow up π. Since F is a
normal crossing divisor, (2.5) implies that m(1 + δ)ddc ϕk,2 ◦ π + [J] − ⌊mF ⌋
is a positive current. Then
      Z                                        Z
         (ddc m(1 + δ) · ϕk,2 ◦ π)ac ∧ u ≤ C +   (ddc m · ϕs,1 ◦ π)ac ∧ u
        b
        X                                          b
                                                   X

for k ≥ k0 (δ, m), where the constant C is independent of m and k. Therefore,
if m → +∞, we get
          Z                                         Z
                                        1
(2.6)          (ddc ϕk,2 ◦ π)ac ∧ u ≤ O( ) + C1 δ +     (ddc ϕs,1 ◦ π)ac ∧ u
            Xb                          m             b
                                                      X
6                                    JUNYAN CAO

for k ≥ k0 (δ, m) and a constant C1 independent of m and k. Then
            Z                                     Z
                                      1
                (ddc ϕk,2 )ac ∧ u ≤ O( ) + C1 δ +    (ddc ϕs,1 )ac ∧ u
              X                       m            X

for k ≥ k0 (δ, m). Letting m → +∞ and δ → 0, we get
                      Z                     Z
                            c
                  lim    (dd ϕk,2 )ac ∧ u ≤   (ddc ϕs,1 )ac ∧ u.
                 k→∞ X                              X

Thus (2.2) is proved.
                                                                               
Remark. Assume that {ϕi,1 }, {ϕi,2 } are two quasi-equisingular approxima-
tions to the same ϕ. Proposition 2.2 implies in particular that
                   Z                         Z
               lim   (ddc ϕi,1 )ac ∧ u = lim   (ddc ϕi,2 )ac ∧ u.
               i→∞ X                           i→∞ X

  Thanks to Proposition 2.2 and the above remark, we can define a related
cohomological product of closed positive (1, 1)-currents.
Definition 3. Let T1 , · · · , Tk be closed positive (1, 1)-currents on a compact
Kähler manifold. We write them by the potential forms Ti = θi + ddc ϕi as
usual. Let {ϕi,j }∞
                  j=1 be a quasi-equisingular approximation to ϕi . Then we
can define a product
                                  hT1 , T2 , · · · , Tk i
                  k,k
as an element in H≥0  (X) such that for all u ∈ H n−k,n−k (X),
                                hT1 , T2 , · · · , Tk i ∧ u
                    Z
            = lim       (θ1 + ddc ϕ1,j )ac ∧ · · · ∧ (θk + ddc ϕk,j )ac ∧ u
              j→∞ X
where ∧ is the usual wedge product in cohomology.
Remark. Thanks to Proposition 2.2 and its remark, the product defined
here does not depend on the choice of quasi-equisingular approximation.
Moreover the product here is smaller than the product defined by any other
analytic approximations.

                           3. Numerical dimension
   Using the product defined in the last section, we can give our definition
of the numerical dimension.
Definition 4. Let (L, ϕ) be a pseudo-effective line bundle on a compact
                                i
Kähler manifold X such that 2π   Θϕ (L) ≥ 0. We define the numerical di-
mension nd(L, ϕ) as the largest v ∈ N, such that h(iΘϕ )v i 6= 0, where the
cohomological product h(iΘϕ )v i is the v-fold product of iΘϕ (L) defined in
Definition 3.
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                             7

   Let (L, ϕ) be a pseudo-effective line bundle on X of dimension n and
nd(L, ϕ) = n. If moreover ϕ is a quasi-psh function with analytic singulari-
ties, it is not difficult to see that
                             h0 (X, mL ⊗ I(mϕ))
                                     mn
admits a strictly positive limit by using the Riemann-Roch formula. When
ϕ is just a quasi-psh function, H.Tsuji conjectured in [Tsu] that
                              h0 (X, mL ⊗ I(mϕ))
                                       mn
admits also a strictly positive limit. The main goal of this section is to prove
that if nd(L, ϕ) = n, then
                                h0 (X, mL ⊗ I(mϕ))
                               lim                 > 0.
                            m→∞         mn


   For the more precise estimates, we first need to explain the construction
of quasi-equisingular approximations by a Bergman Kernel method. Before
doing this, we first prove a useful estimate which is essentially proved in
[DP] in a more general situation. For the sake of completeness, we give the
proof here with a more precise estimate.
Lemma 3.1. Let A be a sufficiently large very ample line bundle on a pro-
jective manifold X and let (L, ϕ) be a pseudo-effective line bundle. Let ϕm
be the metric on L constructed by the Bergman Kernel of H 0 (X, A + mL ⊗
O(mϕ)) with respect to the metric mϕ. Then
                    sm
                I(      ϕm ) ⊂ I(sϕ)      for any m, s ∈ N.
                   m−s
Proof. First of all, we have the following estimate on X:
     Z                              Z
                         −2s·ϕ(x)
                        e         =                 e2(m−s)·ϕ(x)−2m·ϕ(x)
              sm                                    sm
      s·ϕ(x)≤ m−s ·ϕm (x)                   s·ϕ(x)≤ m−s ·ϕm (x)
                 Z
             ≤       e2m·ϕm e−2m·ϕ = h0 (X, A + mL ⊗ I(mϕ)) < +∞.
                 X
                                            sm
Using the above finiteness, for any f ∈ I( m−s ϕm )x , we have
      Z                  Z                         Z
                                                                  2sm
               2 −2sϕ
           |f | e     ≤                  2 −2sϕ
                                     |f | e     +       | f |2 e− m−s ϕm
                                    sm
        Ux                       ϕ≤ m−s ϕm                        Ux
                           Z                       Z
                                                                       sm
        ≤ sup | f | ·  2                −2sϕ
                                        e      +            | f |2 e−2 m−s ϕm < +∞.
                               sm
                            ϕ≤ m−s ϕm                  Ux

Then f ∈ I(sϕ). The lemma is proved.                                                  
8                                JUNYAN CAO

   We are going to construct a quasi-equisingular approximation to ϕ. Such
type of approximations were implicitly constructed in[DPS 01] for the local
case. Philosophically, we can generalize the local properties to the global
case after tensoring by KX . The Ohsawa-Takegoshi extension theorem and
the Skoda theorem are two typical examples. In fact, at least in the pro-
jective case, when S is a smooth zero divisor of a section of an ample line
bundle then X \ S is Stein. So we can reduce the proof to the Stein case.
The reason for tensoring with KX is that the L2 integral is globally well
defined after tensoring by KX .

Proposition 3.2. Let X be a projective variety of dimension n and let ω
be a Kähler metric in H 1,1 (X, Q). Let (L, ϕ) (i.e. the metric on L is h0 e−ϕ
for some smooth metric h0 and quasi-psh function ϕ) be a pseudo-effective
line bundle on X such that nd(L, ϕ) = n.
   Let (G, hG ) be an ample line bundle on X with smooth metric hG , such
that the curvature iΘhG (G) is positive and sufficiently large (e.g. G very
ample and G − KX ample). Let {τp,q,i }i be an orthonormal basis of
                        H 0 (X, 2p G + 2q L ⊗ I(2q ϕ))
                                       p    q     q
with respect to the singular metric h2G · h20 · e−2 ϕ . We define
                                1 X
                        ϕp,q = q ln      |τp,q,i |2h2p ·h2q .
                               2                    G    0
                                      i
Then there exist two increasing integral sequences pm → +∞ and qm → +∞
with
      lim(qm − pm ) = +∞ and qm − qm−1 ≥ pm − pm−1 for all m ∈ N,
such that {ϕpm ,qm }+∞
                    m=1 is a quasi-equisingular approximation to ϕ for the
         i
current 2π Θh0 (L) + ddc ϕ. We denote ϕpm ,qm by ϕm for simplicity.
  Moreover, {ϕm } satisfies the following two properties:
(i)                  H 0 (X, 2pm G + 2qm L ⊗ I(2qm ϕm ))
                     = H 0 (X, 2pm G + 2qm L ⊗ I(2qm ϕ))
for every m ∈ N+ .
(ii) There exists a constant C > 0 independent of G, s0 , such that for all
ǫ > 0, we have          Z
                             i
                           ( Θϕm (L) + ǫω)nac > C
                          X 2π
for m ≥ m0 (ǫ).
Proof. By Theorem 13.21, 13.23 of [Dem], there exists two squences pm →
+∞ and qm → +∞ with
       lim qm /pm = +∞ and qm − qm−1 ≥ pm − pm−1 for all m ∈ N,
                                                                   i
such that {ϕm } is an analytic approximation to ϕ for the current 2π Θh0 (L)+
  c
dd ϕ, i.e. it satisfies property (i) in Definition 2. Lemma 3.1 implies that
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                                                      9

{ϕm } satisfies property (iii) in Definition 2. To prove that {ϕm } is a quasi-
equisingular approximation, it is enough to prove property (ii) in Definition
2.
   We first prove that
(2.1)            ϕp−1,q−1 4 ϕp,q                     and        ϕp,q−1 4 ϕp−1,q−1 .
Let ∆ be the diagonal of X × X and π1 , π2 the two direction projections
from X × X to X. We define a new bundle on X × X:
                 F = 2p−1 π1∗ G + 2p−1 π2∗ G + 2q−1 π1∗ L + 2q−1 π2∗ L
with the singular metric
                                    2q−1 π1∗ (ϕ) + 2q−1 π2∗ (ϕ).
Since 2p−1 G − KX is enough ample, we can apply the Ohsawa-Takegoshi
extension theorem from ∆ to X×X for the line bundle F . Thus the following
map is surjective:
(2.2)                  (H 0 (X, (2p−1 G + 2q−1 L) ⊗ I(2q−1 ϕ)))2
                       → H 0 (X, 2p G + 2q L ⊗ I(2q ϕ)).
Let {fp−1,q−1,i }N
                 i=1 be an orthonormal basis of
                         H 0 (X, 2p−1 G + 2q−1 L ⊗ I(2q−1 ϕ))
                                                       p−1           q−1               q−1 ϕ
with respect to the singular metric h2G                        · h02        · e−2              . For any
                                     0           p         q                q
                           g ∈ H (X, 2 G + 2 L ⊗ I(2 ϕ)),
applying the effective version of Ohsawa-Takegoshi extension theorem to the
morphism (2.2), we obtain the existence of constants {ci,j } such that
                        X
                g(z) = (     ci,j fp−1,q−1,i(z)fp−1,q−1,j (w))|z=w
                              i,j

with                                    X
                                               |ci,j |2 ≤ C1 kgk2
                                         i,j
where C1 depends only on X and kgk is the L2 -norm with respect to the
                      p   q  q
singular metric h2G · h20 e−2 ϕ . By the Cauchy inequality, we have
                          X           X
       |g(z)|2h2p ·h2q ≤ ( |ci,j |2 )(  |fp−1,q−1,i(z)fp−1,q−1,j (z)|2h2p ·h2q )
             G     0                                                                                G      0
                            i,j                 i,j
                                  X
                       ≤ C1 kgk2 (  |fp−1,q−1,i (z)|2 2p−1                         q−1    )2 .
                                                                       hG       ·h02
                                         i
Thus for g with norm kgk = 1, we have
      1                      ln C1    1     X
       q
         ln|g(z)|2h2p ·h2q ≤    q
                                   + q−1 ln(  |fp−1,q−1,i(z)|2 2p−1 2q−1 )
     2             G    0      2    2                        hG    ·h0
                                                                 i
                                         ln C1
                                    =          + ϕp−1,q−1 (z).
                                           2q
10                                 JUNYAN CAO

By the extremal property of Bergman kernel, we obtain finally
                                 ϕp−1,q−1 4 ϕp,q .
The second inequality in (2.1) is obvious by observing that G is very am-
ple. Thanks to the construction of pm , qm , (2.1) implies that ϕm−1 4 ϕm .
Therefore ϕm is a quasi-equisingular approximation to ϕ for the current
 i             c
2π Θh0 (L) + dd ϕ.
   We check the two properties listed in the proposition. Property (i) comes
directly from the construction of ϕm . Since nd(L, ϕ) = n and ϕm is an
quasi-equisingular approximation, the definition of the numerical dimension
implies property (ii).
                                                                          

   The rest of this section is devoted to prove Proposition 1.1. The strategy
is as follows. Thanks to property (ii) of the approximating sequence {ϕm },
we can construct a new metric on L with strictly positive curvatures and
the new metric is much singular than ϕ in an asymptotic way. Proposition
1.1 follows by the standard estimate for this new metric. Before giving the
construction of this new metric, we first prove two preparatory propositions.
Proposition 3.3. Let ϕm be the quasi-psh function constructed in Propo-
sition 3.2. Then there exists another quasi-psh function ϕ
                                                         em such that
                                  i          δ
            sup ϕ
                em (x) = 0,         Θϕe (L) ≥ · ω and ϕm 4 ϕ
                                                           em ,
            x∈X                  2π m        2
where δ is a strictly positive number independent of m.
Proof. Let π : Xm → X be a log resolution of ϕm . We can hence assume
that
                        i
                          Θϕ ◦π (π ∗ (L)) = [E] + C ∞ ,
                       2π m
where [E] is a normal crossing divisor. Keeping the notations in Proposition
3.2, we can suppose A to be a Q-ample line bundle such that c1 (A) = ω,
and ǫ to be a positive rational number in property (ii) of Proposition 3.2,
i.e.                    Z
                             i
                           ( Θϕm (L) + ǫω)nac > C.
                          X 2π
Thanks to Proposition 3.2,
                             i
                        (      Θϕ ◦π (π ∗ (L)) + ǫπ ∗ ω)ac
                            2π m
is a Q-nef class for m large enough. We can thus choose a Q-nef line bundle
Fm on Xm such that
                                  i
                  c1 (Fm ) = (      Θϕ ◦π (π ∗ (L)) + ǫπ ∗ ω)ac .
                                 2π m
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                    11

   Thanks to property (ii) of Proposition 3.2 and the cohomological fact that
Fmn−1 · π ∗ A are uniformly bounded for all m, we can thus choose a constant

δ > 0 independent of ǫ and m, such that
                              n      n−1
(3.1)                        Fm > nδFm   · π ∗ A.
Using the holomorphic Morse inequality (cf. [Dem] or [Tra]) for the Q-bundle
Fm − δ · π ∗ (A) on Xm , we have
                                        kn n
(3.2)   h0 (Xm , kFm − kδ · π ∗ A) ≥ C    (F − nδFm    n−1
                                                           · π ∗ A) + O(kn−1 ).
                                        n! m
Combining (3.1) and (3.2), we get that Fm − δπ ∗ ω is pseudo-effective. In
particular, if we take ǫ ≤ δ2 , the pseudo-effectiveness of Fm − δπ ∗ ω implies
the existence of a quasi-psh function ψm on Xm such that
                      i                              δ
(3.3)                   Θϕm ◦π (π ∗ (L)) + ddc ψm ≥ π ∗ ω.
                     2π                              2
Choosing a constant C1 such that
                        sup (ϕm ◦ π + ψm + C1 )(x) = 0,
                      x∈Xm

(3.3) implies that ϕm ◦ π(x) + ψm (x) + C1 induces a quasi-psh function on X
satisfying all the requirements in the proposition. We denote it by ϕem . 
Remark. The essential point here is the holomorphic Morse inequality. There-
      i
fore 2π Θϕm ◦π is required to be rational. By using other techniques, Demailly
and Paun proved in [DP 04] the same results for the case of a real class.
  Thanks to Proposition 3.3, we are going to construct a singular metric
on L which is a kind of limit of ϕ
                                 em . We first recall the notion of upper
semicontinuous regularization. Let Ω ⊂ Rn and let (uα )α∈I be a family of
upper semicontinuous fuctions Ω → [−∞, +∞[. Assume that (uα ) is locally
uniformly bounded from above. Since the upper envelope
                                   u = sup uα
                                         α∈I
need not be upper semicontinuous, we consider its upper semicontinuous
regularization:
                         u∗ (z) = lim sup u.
                                      ǫ→0 B(z,ǫ)

We denote this upper semicontinuous regularization sg
                                                    up(uα ). It is easy to
                                                          α
proof that if {uα }α∈I are psh fonctions with locally uniformly bounded from
above, then sg up(uα ) is also a psh function (cf. [Dem] for details).
              α
  We need the following lemma.
Lemma 3.4. Let ϕ be a quasi-psh fonction with normal crossing singulari-
ties and let {ψi } be quasi-psh functions such that
                  sup ψi (z) ≤ 0      and       ddc ψi ≥ −Cω
                  z∈X
12                                   JUNYAN CAO

for some uniform constant C independent of i. If ϕ 4 ψi for all i, then
                                     ϕ 4 sg
                                          up(ψi ).
                                              i

Proof. Since ϕ has normal crossing singularities and ϕ is less singular than
ϕi , ψi − ϕ are quasi-psh functions and
(4.1)                         ddc (ψi − ϕ) ≥ −C1 ω
for some uniform constant C1 independent of i.
   On the other hand, since sup ψi (z) ≤ 0 and ddc ϕi ≥ −Cω for a uniform
                                 z∈X
C, by the standard potential theory, there exists a constant M such that
                        Z
                            ψi ≤ M       for all i.
                             X
Therefore
                                 Z
(4.2)                                    (ψi − ϕ) ≤ M ′
                                     X
for a uniform constant M ′ .
   (4.1) and (4.2) imply the existence of a uniform constant C2 such that
                   sup (ψi (z) − ϕ(z)) ≤ C2                 for all i.
                   z∈X
Then ϕ 4 sg
          up(ψi ). The lemma is proved.                                     
               i
  The following metric will be useful in our context. Using the same ter-
mology as above, we have
Proposition 3.5. Let ϕ(z)
                     e    = lim sg
                                 up((ϕ
                                     em+s (z))). Then the new metric
                                     m→∞ s≥0
ϕ
e satisfies:
                    i        δ
(5.0)                 Θ (L) ≥ ω                   and       ϕm 4 ϕ
                                                                 e
                   2π ϕe     2
for any m ≥ 1.
Proof. By Proposition 3.3, we have
                         i           δ
                           Θϕem (L) ≥ ω     for m ≥ 1.
                        2π           2
       i
Then 2π  Θϕe(L) ≥ δ2 ω. To check ϕm 4 ϕ,
                                       e it is enough to show that
(5.1)                            ϕm 4 sg
                                       up(ϕ
                                          em+s )
                                            s≥0

by observing ϕ
             e ≤ sg
                  up(ϕ
                     em+s ). Combining Proposition 3.3 and Proposition
                   s≥0
3.2, we have
(5.2)              ϕm 4 ϕm+s 4 ϕ
                               em+s                     for any m, s.
Let π be a log resolution of ϕm . Then
(5.3)                    ϕm ◦ π 4 ϕm+s ◦ π 4 ϕ
                                             em+s ◦ π.
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                     13

Thanks to Lemma 3.4, (5.3) implies that
                          ϕm ◦ π 4 sg
                                    up(ϕ
                                       em+s ◦ π).
                                      s≥0

By passing to π∗ , (5.1) is proved.                                           
  Using the new metric ϕ,
                       e we can give an asymptotic estimate.
Proposition 3.6. Let (L, ϕ) be a pseudo-effective line bundle on a projective
variety X of dimension n with nd(L, ϕ) = n. Then
                           h0 (X, mL ⊗ I(mϕ))
                        lim                   > 0.
                       m→∞         mn
Proof. Lemma 3.1 implies that for any m ∈ N,
                                                    m · 2qk
(6.1)        h0 (X, mL ⊗ I(mϕ)) ≥ h0 (X, mL ⊗ I( q          ϕk )).
                                                   2 k −m
Let ϕe be the metric constructed in Proposition 3.5. Then Proposition 3.5
implies that
                           m · 2qk                          m · 2qk
(6.2)       h0 (X, mL ⊗ I( q       ϕk )) ≥ h0 (X, mL ⊗ I( q         ϕ)).
                                                                    e
                          2 k −m                          2 k −m
for any k, m. Combining (6.1) and (6.2), we get
                                                    m · 2qk
(6.3)        h0 (X, mL ⊗ I(mϕ)) ≥ h0 (X, mL ⊗ I( q          ϕ)).
                                                            e
                                                   2 k −m
Since (6.3) is true for all m and k, if we take k such that 2qk ≫ m, by
          i
applying 2π Θϕe(L) > 0 proved in Proposition 3.5, (6.3) implies that
                           h0 (X, mL ⊗ I(mϕ))
                        lim                   > 0.
                       m→∞         mn
                                                                              

                        4. A numerical criterion
   Until now, we have two kind of numerical dimension of pseudo-effective
line bundles: νnum (L, ϕ) in Defintion 1 and more analytically nd(L, ϕ) in
Definition 4. We prove in this section that νnum (L, ϕ) = nd(L, ϕ) when X is
projective. Before giving the proof, we first list some properties of multiplier
ideal sheaves which will be useful in our context. The essential tool here is
the Ohsawa-Takegoshi extension theorem.
Lemma 4.1. Let (L, ϕ) be a pseudo-effective line bundle on a projective
variety X of dimension n and let {ϕk } be a quasi-equisingular approximation
to ϕ. Let s1 be a positive number such that
(∗)             I((1 + ǫ′ )ϕ) = I+ (ϕ)      for any 0 < ǫ′ ≤ s1
Assume that A is a very ample line bundle and S is the zero divisor of a
general global section of H 0 (X, A). We have the following properties:
14                                        JUNYAN CAO

     (i) The restrictions
(1.1)                    I(m(1 + δ)ϕk ) → I(S, m(1 + δ)ϕk |S )

(1.2)                      I(m(1 + δ)ϕ) → I(S, m(1 + δ)ϕ |S )
are well defined for all m ∈ N, δ ≥ 0, where ϕ |S denotes the restriction of
ϕ on S and I(S, ϕ |S ) is the multiplier ideal sheaf associated to ϕ |S on S.
3
  Moreover we have
            I(S, (1 + ǫ′ )ϕ |S ) = I(S, (1 + s1 )ϕ |S )            for any 0 < ǫ′ ≤ s1 .
     (ii) {ϕk |S } is also a quasi-equisingular approximation to ϕ |S .
     (iii) If the restrictions are well defined, we have an exact sequence:
                  0 → I+ (ϕ) ⊗ O(−S) → adjǫS (ϕ) → I+ (S, ϕ |S ) → 0
for any 0 < ǫ ≤ s1 , where
                                           Z
                                                     | f |2
                 adjǫS (ϕ)x = {f ∈ Ox ,                       ǫ
                                                       2(1− 2 )
                                                                  e−2(1+ǫ)ϕ < +∞}
                                               Ux | s |

and I+ (S, ϕ |S ) is multiplier ideal sheaf I+ (ϕ|S ) on S.
  (iv) adjǫS (ϕ) = I+ (ϕ) for any 0 < ǫ ≤ s1 .
Proof. (i) By the Notherian property, except for countably many s ∈ R+ ,
we have
                            I(sϕ) = I((s + δ)ϕ)
for δ > 0 small enough. Therefore there exists a countable set I ⊂ R+ such
that for any t ∈ R+ , we can find an α ∈ I such that
(1.3)                                  I(αϕ) = I(tϕ).
Since I is a countable set, we can take S to be very general in such a way
that the restrictions
                            I(αϕ) → I(S, αϕ |S )
are well defined for all α ∈ I. Then (1.3) implies that (1.1) and (1.2) are
well defined for all m, δ ≥ 0.
  For the second part of (i), if the restrictions
                                      I(ϕ) → I(S, ϕ |S )
                       I((1 + δ)ϕ) → I(S, (1 + δ)ϕ |S )
are well defined, then the Ohsawa-Takegoshi extension theorem and (∗) im-
ply immediately that
                         I(S, (1 + ǫ′ )ϕ |S ) = I(S, (1 + s1 )ϕ |S ).
     (ii) Since {ϕk } is a quasi-equisingular approximation to ϕ, we have
                  I(m(1 + δ)ϕk ) ⊂ I(mϕ)                 for any k ≥ k0 (δ, m).
     3ϕ |
        S is also psh if it is well defined.
           A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                         15

Using (1.1), (1.2) and the Ohsawa-Takegoshi extension theorem, we have
         I(S, m(1 + δ)ϕk |S ) ⊂ I(S, mϕ |S )              for any k ≥ k0 (δ, m).
Therefore ϕk |S is a quasi-equisingular approximation to ϕ |S .
   (iii) First of all, the Ohsawa-Takegoshi extension theorem implies the
surjectivity of the sequence. We need only to prove the exactness of the
middle term, i.e., for any f ∈ Ox satisfying the conditions
                                 Z
              f                         | f |2
(1.4)           ∈ Ox      and             2(1− 2ǫ )
                                                    e−2(1+ǫ)ϕ < +∞,
              s                   Ux | s |

we should prove the existence of some ǫ′ > 0 such that
                        Z
                           | f |2 −2(1+ǫ′ )ϕ
(1.5)                             e          < +∞,
                           | s |2
where s is a local function defining S. In fact, if fs ∈ Ox , then
                    Z
                           | f |2
(1.6)                         4−δ
                                  < +∞      for any δ > 0.
                      Ux | s |
If we take ǫ′ = 4ǫ in the left side of (1.5), then
                                 Z
                                        | f |2 −2(1+ ǫ )ϕ
(1.7)                                        2
                                               e      4
                                   Ux | s |
                    Z                                     Z
                            | f |2                  1+ ǫ
                                         −2(1+ǫ)ϕ 1+ǫ4         | f |2 1+ǫ
                                                                        3ǫ
                                                                        4
                ≤(            2(1− 2ǫ )
                                        e         )      (          α
                                                                      )
                      Ux | s |                              Ux | s |
by Hölder’s inequality, where
                          ǫ 1 + 4ǫ               4    10ǫ + ǫ2
          α = (2 − 2(1 − )         ) · (1 + ǫ) ·    =          < 4.
                         2 1+ǫ                   3ǫ      3ǫ
Thanks to (1.4) and (1.6), the second line of (1.7) is finite. Thus (1.5) is
proved.
   (iv) By the definition of I+ (ϕ), we have an obvious inclusion
                                    adjǫS (ϕ) ⊂ I+ (ϕ).
In order to prove the equality, it is enough to show that for any f ∈ I((1 +
ǫ)ϕ)x , we have
                     Z
                             | f |2
(1.8)                          2(1− 2ǫ )
                                         e−2(1+ǫ)ϕ dV < +∞,
                       Ux | s |

where s is a general global section of H 0 (X, A) independent of the choice of
f and x.
   (1.8) comes from the Fubini theorem. In fact, let {s0 , · · · , sN } be a basis
of H 0 (X, A). Then
                         N
                         X
                               |si (x)|2 6= 0    for any x ∈ X.
                         i=0
16                                                    JUNYAN CAO

Taking {τ0 , · · · , τN } ∈ CN +1 , we have
                   Z                 Z
                                              | f |2
(1.9)                 N
                      P           dτ                         e−2(1+ǫ)ϕ dV
                              2
                         |τi | =1     Ux   P
                                           N             ǫ
                     i=0                 |   τi si |2(1− 2 )
                                                       i=0
      Z                                                       Z
                          | f |2              −2(1+ǫ)ϕ                                                  1
  =                                           e          dV       N
                                                                  P                                                           dτ
        Ux        P
                  N                       ǫ                             |τi |2 =1       P
                                                                                        N
                                                                                                 si                     ǫ
              |         |si (x)|2 |(1− 2 )                        i=0               (       τi P
                                                                                               N
                                                                                                                  )2(1− 2 )
                  i=0                                                                i=0              |si (x)|2
                                                                                                i=0
          Z                                                        Z
                               | f |2             −2(1+ǫ)ϕ                                      1
      =                                           e           dV        N
                                                                        P                    2(1− 2ǫ )
                                                                                                            dτ < +∞
             Ux         P
                        N                   ǫ                                 |τi |2 =1 |τ0 |
                   |         |si (x)|2 |(1− 2 )                         i=0
                       i=0
For any f ∈ I((1 + ǫ)ϕ)x fixed, applying the Fubini theorem to (1.9), we
obtain
                     Z
                             | f |2
(1.10)                         2(1− 2ǫ )
                                         e−2(1+ǫ)ϕ < +∞
                       Ux | s |

for a general element s ∈ H 0 (X, A). Observing that I((1 + ǫ)ϕ) is finitely
generated on X, we can thus choose a general section s such that (1.10) is
true for any f ∈ I((1 + ǫ)ϕ). The equality adjǫS (ϕ) = I+ (ϕ) is proved. 
   The next proposition confirms that our definition of numerical dimension
coincides with Tsuji’s definition.
Proposition 4.2. If (L, ϕ) is a pseudo-effective on a projective variety X
of dimension n, then
                         νnum (L, ϕ) = nd(L, ϕ).
Proof. We first prove νnum (L, ϕ) ≥ nd(L, ϕ) by induction on dimension.
If nd(L, ϕ) = n, the inequality comes from Proposition 3.6. Assume now
nd(L, ϕ) < n. Let A be a general hypersurface given by a very ample line
bundle and let {ϕk } be a quasi-equisingular approximation to ϕ. Lemma
4.1 implies that ϕk |A is also a quasi-equisingular approximation to ϕ |A .
Since A is a general section and nd(L, ϕ) < n, we have
                          Z
                               i
                      lim    (( Θϕk )ac )s ∧ ω n−s−1 > 0
                     k→∞ A 2π

where s = nd(L, ϕ). Thus Definition 2 implies that
(2.1)                                   nd(A, L, ϕ |A ) ≥ s = nd(L, ϕ).
Notice moreover that the definition of νnum implies
(2.2)                                   νnum (L, ϕ) ≥ νnum (A, L, ϕ |A ).
Combining (2.1) and (2.2), the equality νnum (L, ϕ) ≥ nd(L, ϕ) is concluded
by induction on dimension.
           A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                       17

  We now prove νnum (L, ϕ) ≤ nd(L, ϕ). Assume that νnum (L, ϕ) = k. By
definition, there exists a subvariety V of dimension k such that
                               h0 (V, mL ⊗ I(mϕ))
                             lim                  > 0.
                           m→∞         mk
        e → X be the desingularization of the ideal sheaf of V in X, and
Let π : X
    e
let V be the strict transform of V .
   By the Ohsawa-Takegoshi extension theorem, there exists a very ample
line bundle A on X e such that the following restrictions are surjective
           e A + mπ ∗ (L) ⊗ I(mϕ ◦ π)) → H 0 (Ve , A + mπ ∗ (L) ⊗ I(mϕ ◦ π))
(2.3) H 0 (X,
for all m > 0. Fix a smooth metric h0 on L and let {ei,m } be an orthonormal
              e A + mπ ∗ (L) ⊗ I(mϕ ◦ π)) with respect to hA · hm e−mϕ◦π . It
basis of H 0 (X,                                                 0
is well known that we can take a smooth function ψ 4 independent of m on
Xe such that
                  1            X
                    i∂∂(ψ + ln    |ei,m |2hA ,hm ) ≥ −Cπ ∗ ωX .
                  m                            0
                                i
        1        P       2
Then m (ψ + ln |ei,m |hA ,hm ) induces a quasi-psh fucntion on X and we
                                   0
                     i
denote it by ϕm . We claim that
                      Z
                          i             1
(2.4)             lim    ( Θϕm (L) + ω)kac ∧ ω n−k > 0.
                 m→∞ X 2π               m
   We postpone the proof of (2.4) in Lemma 4.3 and conclude first the proof
of Proposition 4.2. By Lemma 3.1, {ϕm ◦ π} is a quasi-equisingular approx-
imation to ϕ ◦ π. Thanks to the formula
                             π∗ (KX/X
                                  e   ⊗ π ∗ I(ϕ)) = I(ϕ),
{ϕm } is a quasi-equisingular approximation to ϕ. Therefore (2.3) implies
nd(L, ϕ) ≥ k. Since νnum (L, ϕ) = k by assumption, we conclude that
nd(L, ϕ) ≥ νnum (L, ϕ). The proposition is proved.                     
Remark. From the proof, it is easy to conclude that if S1 , S2 , ..., Sk are
divisors of general global sections of a very ample line bundle, then
(∗)           nd(S1 ∩ S2 ∩ · · · ∩ Sk , L, ϕ) = max(nd(L, ϕ), n − k).
In fact, if nd(L, ϕ) ≤ n − k, by the same argument as above, ϕm |S1 ∩S2 ...∩Sk
is also a quasi-equisingular approximation to ϕ |S1 ∩S2 ∩···∩Sk . Then (∗) is
proved by simple calculation.
   We now prove Lemma 4.3 promised in the above proposition.
Lemma 4.3. We have
                 Z
                    i         1
(3.1)        lim   ( Θϕm (L) + ω)kac ∧ ω n−k > 0.
            m→∞ X 2π          m
   4we can take a smooth metric on the exceptional divisor O(−E), and the canonical
section gives this function. See [Bou] for details.
18                                 JUNYAN CAO


Proof. Let {e′i,m } be an orthonormal basis of H 0 (Ve , A+mπ ∗ (L)⊗I(mϕ◦π))
                           −mϕ◦π and let ϕ′ = 1 (ψ + ln
                                                           P ′ 2
with respect to hA · hm 0 e               m    m            |ei,m |hA ,hm ) which
                                                                        0
                                                            i
is a psh function on Ve . We prove (3.1) in two steps.
     Step 1: We first prove that
Z                                      Z                                  Z
    i         1                                i            1                     i          1
     (Θϕm (L)+ ω)kac ∧ω n−k ≥ C1            (    Θϕm ◦π (L)+ ω)kac = C1        (    Θϕ′m (L)+ ω)kac
 X 2π         m                            Ve 2π            m                 Ve 2π          m
for some constant C1 > 0. Noting that we abuse a little bit the notation
here. We denote L also for the pull back of L on X.   e
   In fact, there exists a C1 such that [V ] ⩽ C1 ω   n−k in the sense of coho-
                      i            1
mology class, and ( 2π Θϕm (L) + m ω)ac is the push forward of a nef class.
Therefore
    Z                                      Z
          i             1 k      n−k                   i            1
        ( Θϕm (L) + ω)ac ∧ ω         ≥ C1            ( Θϕm (L) + ω)kac .
      X 2π              m                    V \Vsing 2π            m

Since Ve is the strict transformation of V , we have
            Z                          Z
                 i             1 k           i       1
              ( Θϕm (L) + ω)ac = ( Θϕm ◦π (L) + ω)kac .
             V 2π              m         Ve 2π       m
We obtain thus the first inequality.
   We now prove the second equality. Since ψ is a smooth function on X,   e
              c          c                 c
we have (dd ψ)ac = dd ψ. Therefore (dd ψ)ac has no contribution for the
integral on Ve by a cohomological reason. We can thus suppose for simplicity
that
                 i            i          1       X
                   Θϕm (L) =    Θh0 (L) + ddc ln    |ei,m |2hA ,hm
                2π           2π          m                       0
                                                      i
and
               i             i          1       X
                 Θϕ′m (L) =    Θh0 (L) + ddc ln   |e′i,m |2hA ,hm .
              2π            2π          m                       0
                                                      i
Thanks to the surjectivity of (2.3) in Proposition 4.2 and the extremal prop-
erty of Bergman kernels,
                                P
                                   |ei,m |2hA ,hm
                                                0
                                 i
                                P ′ 2
                                   |ei,m |hA ,hm
                                                0
                                   i

is thus a smooth function and does not vanish on Ve . Therefore ( 2π
                                                                   i
                                                                     Θϕm ◦π )ac (L) |Ve
       i
and ( 2π Θϕ′m )ac (L) |Ve are in the same cohomology class. The equality is
proved.
  Step 2: We prove in this step the existence of a uniform constant C > 0
such that       Z
                      i
                    ( Θϕ′m (L))kac ≥ C      for m ≫ 1.
                  e
                  V  2π
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                   19

  For any m fixed, since ϕ′m is less singular than ϕ, we have
(3.2)       h0 (Ve , A + sL ⊗ I(sϕ)) ≤ h0 (Ve , A + sL ⊗ I(sϕ′m )).
Notice that by the bigness of (V, L, ϕ) we have
                         h0 (Ve , A + sL ⊗ I(sϕ))
                      lim                         ≥ C0
                    s→∞              sk
for some constant C0 > 0. Then (3.2) implies
(3.3)      h0 (Ve , A + sL ⊗ I(sϕ′m )) ≥ h0 (Ve , A + sL ⊗ I(sϕ)) ≥ C0 sk
for a sequence s → ∞.
   On the other hand, since ϕ′m has analytic singularities, we have
                                              Z
                                                   i
(3.4)      h0 (Ve , A + sL ⊗ I(sϕ′m )) = C1 sk ( Θϕ′m )kac + O(sk−1 )
                                               Ve 2π
for m ≫ 1. Combining (3.3) and (3.4), we get
                Z
                      i              C0
                    ( Θϕ′m (L))kac ≥    >0    for m ≫ 1.
                  e
                  V  2π              C1
Step 2 is proved.
   Combining Steps 1 and 2, the lemma is proved.                            
  We now give a numerical criterion to calculate the numerical dimension.
Proposition 4.4. Let (L, ϕ) be a pseudo-effective line bundle on a projectvie
variety X, and let A be a very ample line bundle. Then nd(L, ϕ) = d if and
only if
                                0
                      ln( lim h (X,mǫA+mL⊗I(mϕ))
                                        mn       )
                         m→∞
                 lim                               = n − d.
                 ǫ→0               ln ǫ
Proof. First of all, the inclusion
        H 0 (X, mǫA + mL ⊗ I(mϕ)) ⊃ H 0 (X, mǫA + mL ⊗ I+ (mϕ))
                    ⊃ H 0 (X, mǫA + mL ⊗ I((m + 1)ϕ)),
implies that h0 (X, mǫA + mL ⊗ I+ (mϕ)) has the same asymptotic comport-
ment as h0 (X, mǫA + mL ⊗ I(mϕ)). Since we have constructed the exact
sequence for I+ in Lemma 4.1, we prefer to calculate h0 (X, mǫA + mL ⊗
I+ (mϕ)) in the following argument.
  If nd(L, ϕ) = n, the proposition comes directly from Proposition 4.2.
Assume now that nd(L, ϕ) = d < n. Let {Yi }ni=1 be n general sections of
H 0 (X, A). By the remark of Proposition 4.2, there exists a uniform constant
C > 0 such that for all m, ǫ,
(4.1)     h0 (Y1 ∩ · · · ∩ Yn−d , mǫA + mL ⊗ I+ (mϕ)) = C(ǫ, m)md .
and C(ǫ, m) ≥ C. We prove by induction on s that
                1
(4.2)           n−s
                    h0 (Y1 ∩ · · · ∩ Ys , mǫA + mL ⊗ I+ (mϕ))
              m
20                                       JUNYAN CAO

                                   1                           1
                = C(ǫ, m)ǫn−s−d            + O(ǫn−s−d+1 ) + O( )
                              (n − d − s)!                     m
for 0 ≤ s ≤ n − d, where the constant C(ǫ, m) is the same constant in (4.1),
in particular it does not depend on the codimension s.
   If s = n − d, (4.2) comes from the definition of C(ǫ, m). We suppose that
(4.2) is true for s0 ≤ s ≤ n − d. We now prove that (4.2) is also true for
s = s0 − 1.
   Let Y be the intersection of zero divisors of s0 − 1 general elements of
H 0 (X, A), and let
                        
           0,q           mǫ 0
(4.3)     e1 (ǫ, m) =       h (Y ∩ Y1 ∩ · · · ∩ Yq , mǫA ⊗ mL ⊗ I+ (mϕ)).
                         q
We claim the formula:
                           1
(4.4)                            h0 (Y, mǫA + mL ⊗ I+ (mϕ))
                        mn−s0 +1
                             1      X                       1
                      = − n−s0+1 ( (−1)q e0,q1 (ǫ, m)) + O(   ).
                         m                                  m
                                        q≥1
   We postpone the proof of (4.4) in Lemma 4.5 and conclude first the proof
of the formula (4.2). First of all, if q > n − d − s0 + 1, we have by definition
                         1
(4.5)           lim            e0,q (ǫ) = O(ǫq ) ≤ O(ǫn−d−s0 +2 ).
               m→∞ mn−s0 +1 1
Thus (4.4) and the induction hypothesis of (4.2) implies that
                       1
                             h0 (Y, mǫA + mL ⊗ I+ (mϕ))
                    m 0 +1
                      n−s

           n−d−s
             X0 +1                ǫn−d−s0 +1 C(ǫ, m)                          1
     = −(              (−1)q                           ) + O(ǫn−d−s0 +2 ) + O( )
                               q!(n − q − s0 + 1 − d)!                        m
                q=1
        n−d−s
          X0 +1              n−d−s0 +1 C(ǫ, m)
                                                      
                        qǫ               n − s0 + 1 − d                     1
= −(              (−1)                                   )+O(ǫn−d−s0 +2 )+O( )
          q=1
                       (n − s0 + 1 − d)!        q                           m
                               n−d−s
                                 X0 +1                             
   ǫn−d−s0+1 C(ǫ, m)                          q       n − s0 + 1 − d                     1
=−                   (                   (−1)                         )+O(ǫn−d−s0 +2 )+O( )
   (n − s0 + 1 − d)!              q=1
                                                             q                           m
                                     1                              1
         = C(ǫ, m)ǫn−d−s0 +1                   + O(ǫn−d−s0 +2 ) + O( ).
                            (n − d − s0 + 1)!                       m
Therefore (4.2) is proved for s = s0 − 1.
  In particular, since (4.1) implies that
                   1 0
        lim lim      h (Y1 ∩ · · · ∩ Yn−d , mǫA + mL ⊗ I+ (mϕ)) > 0,
        ǫ→0 m→∞ md
by taking s = 0 in (4.2), we obtain
                          1
            lim lim            h0 (X, mǫA + mL ⊗ I+ (mϕ)) > 0.
            ǫ→0 m→∞ m ǫn−d
                        n
         A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                    21

The proposition is proved.                                                  
  We now prove the formula (4.4) promised in the above proposition.
Lemma 4.5. We have
         1                                       1
              h0
                 (Y, mǫA + mL ⊗ I + (mϕ))  =          e0,0 (ǫ, m)
       n−s
     m 0   +1                                 m 0 +1 1
                                                n−s

                      1    X                        1
            = − n−s0+1 ( (−1)q e0,q  1 (ǫ, m)) + O(   ).
                  m                                 m
                              q≥1

Proof. Thanks to (iii), (iv) of Lemma 4.1 and the section 4 of [K], OY (mL⊗
I+ (mϕ)) is resolved by
(∗) OY (mǫA + mL ⊗ I+ (mϕ)) → ⊕1≤i≤mǫ OY ∩Yi (mǫA + mL ⊗ I+ (mϕ))
             → ⊕1≤i1 <i2 ≤mǫ OY ∩Yi1 ∩Yi2 (mǫA + mL ⊗ I+ (mϕ))
                                    → ···
Then
(5.1)                H k (Y, mL ⊗ I+ (mϕ)) = Hk (ǫ, m)
where Hk (ǫ, m) represents the hypercohomology of (∗).
   We now calculate the asymptotic behaviour of on the both sides of (5.1).
The Nadel vanishing theorem implies that
                     1
(5.2)        lim          hk (Y, mL ⊗ I+ (mϕ)) = 0          for any k ≥ 1.
            m→∞ mn−s0 +1
Moreover, since we assume that nd(L, h) = d < dim Y , we have
                           1
(5.3)              lim    n−s 0 +1
                                   h0 (Y, mL ⊗ I+ (mϕ)) = 0.
                  m→∞ m
By calculating the asymptotic cohomology on both sides of (5.1), the equa-
tions (5.2) and (5.3) imply in particular that
                              1      X
(5.4)                lim                 (−1)k hk (ǫ, m) = 0,
                    m→∞ mn−s0 +1
                                    k

where hk (ǫ, m) denotes the dimension of Hk (ǫ, m).
  For the right side of (5.1), we have
                   
             1      mǫ p
    lim                  h (Y ∩ Y1 ∩ · · · ∩ Yq , mǫA ⊗ mL ⊗ I+ (mϕ)) = 0
   m→∞ mn−s0 +1      q
for every p ≥ 1 by Nadel vanishing theorem. If p = 0, then
        
         mǫ 0
             h (Y ∩ Y1 ∩ · · · ∩ Yq , mǫA ⊗ mL ⊗ I+ (mϕ)) = e0,q
                                                             1 (ǫ, m)
         q
by definition. Thus (5.4) implies that
                  1      X
           lim          (   (−1)q e0,q
                                   1 (ǫ, m)) = 0      for any ǫ > 0.
         m→∞ mn−s0 +1
                        q≥0
22                                JUNYAN CAO

Then
            1                                                  1
                    h0 (Y, mǫA + mL ⊗ I+ (mϕ)) =                   e0,0 (ǫ, m)
         mn−s0 +1                                            m 0 +1 1
                                                              n−s

                          1        X                       1
                 =−      n−s   +1
                                  (  (−1)q e0,q
                                            1 (ǫ, m)) + O(   ).
                       m     0                             m
                                 q≥1
                                                                                 
Remark. Let L be a pseudo-effective line bundle on a compact Kähler man-
ifold. S.Boucksom defined in [Bou] a concept of numerical dimension nd(L)
of pseudo-effective line bundles without metrics. Let ϕmin be a positive
metric of L with minimal singularity. Proposition 4.4 implies in particular
that
                           nd(L) ≥ nd(L, ϕmin ).
The example 1.7 in [DPS 94] tells us that we cannot hope the equality
                              nd(L) = nd(L, ϕmin ).
In that example, the line bundle L is nef and nd(L) = 1. But there exists a
unique positive singular metric h on L with the curvature form
                                i
                                  Θh (L) = [C],
                               2π
where C is a curve on X. Therefore ϕmin = h. Moreover, since h has
analytic singularities, we have nd(L, ϕmin ) = 0 by definition. Thus
                              nd(L) > nd(L, ϕmin ).
Remark. The example 3.6 in [Tsu] tells us that we cannot hope the following
equality:
                         ln h0 (X, A + mL ⊗ I(mϕ))
              sup lim                              = nd(L, ϕ),
               A m→∞                 ln m
where A runs over all the amples bundles on X. In fact, H.Tsuji defined a
closed positive (1, 1)-current T on P1 :
                                     +∞ 3Xi−1
                                     X     1
                               T =                    Pi,j
                                                 4i
                                     i=1 j=1

where {Pi,j } are distinct points on P1 . There exists thus a singular metric ϕ
                     i
on L = O(1) with 2π    Θϕ (L) = T . It is easy to construct a quasi-equisingular
approximation {ϕk } to ϕ such that
                                       k 3i−1
                                    XX 1
                        i
                          Θϕk (L) =       Pi,j + C ∞ .
                       2π              4i
                                       i=1 j=1

Then nd(L, ϕ) = 0.
  On the other hand, thanks to the construction of ϕ, we have
    h0 (P1 , O(s + m) ⊗ I(mϕ))       h0 (P1 , O(s + 4k − 1) ⊗ I((4k − 1)ϕ))
 lim                           = lim
m→∞               m             k→∞                   4k − 1
            A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                       23

for every s ≥ 1. By construction,
                               I((4k − 1)ϕ)x = Ox
                                                                k
      / {Pi,j }i≤k−1 , and I((4k − 1)ϕ) has multiplicity ⌊ 4 4−1
for x ∈                                                       i ⌋ = 4
                                                                     k−i − 1 on

3i−1 points {Pi,1 , ..., Pi,3i−1 }. Therefore
                                                          k−1
                                                          X
       0    1         k               k               k
    h (P , O(s + 4 − 1) ⊗ I((4 − 1)ϕ)) = s + 4 −                3i−1 (4k−i − 1)
                                                          i=1
                                 9          1
                                = 3k−1 + s − .
                                 2          2
Then
                         ln h0 (P1 , A + O(m) ⊗ I(mϕ))   ln 3
                  sup lim                              =      .
                   A m→∞                ln m             ln 4
Therefore
                                  ln h0 (P1 , A + O(m) ⊗ I(mϕ))
                nd(L, ϕ) 6= sup lim                             .
                            A m→∞                ln m
           5. A Kawamata-Viehweg-Nadel Vanishing Theorem
  In this section, we will prove that given a pseudo-effective line bundle
(L, ϕ) on a compact Kähler manifold X of dimension n, then
           H p (X, KX ⊗ L ⊗ I+ (ϕ)) = 0      for p ≥ n − nd(L, ϕ) + 1.
The main advantage of this version of the Kawamata-Viehweg-Nadel van-
ishing theorem is that we do not need any strict positivity of the line bundle.
In our case, we just suppose that X is a compact Kähler manifold and ϕ is
                                  i
a quasi-psh function such that 2π   Θϕ (L) ≥ 0. But as a compensation, we
need the multiplier ideal sheaf I+ (ϕ) instead of I(ϕ).
   When X is projective, the proof of our vanishing theorem is much easier.
We first give a quick proof of this vanishing theorem in the projective case
by the tools developed in the previous sections. First of all, we prove the
vanishing theorem in the case nd(L, ϕ) = dim X.
Proposition 5.1. Let (L, ϕ) a pseudo-effective line bundle on a smooth
projective variety of dimension n with nd(L, ϕ) = n. Then
                  H i (X, KX + L ⊗ I+ (ϕ)) = 0      for any i > 0.
Proof. Fix a smooth metric h0 on L. (L, ϕ) is pseudo-effective means that
                       i             i
                         Θϕ (L) =      Θh (L) + ddc ϕ ≥ 0.
                      2π            2π 0
       i
Since 2π Θϕ (L) is not strictly positive, we need to add a portion of the metric
ϕ
e constructed in Proposition 3.5 to make the new curvature become strictly
positive. We will see that this operation preserves I+ (ϕ).
  First of all, by the definition of I+ , there is a δ > 0 such that
                              I+ (ϕ) = I((1 + δ)ϕ).
24                                      JUNYAN CAO

Let ϕe be the psh function constructed in Propositon 3.5. For any ǫ > 0, we
define a new metric
                              h0 e−(1+σ(ǫ)−ǫ)ϕ−ǫϕe
on L where 0 < σ(ǫ) ≪ ǫ. Since ddc ϕ ≥ −cω for some constant c, 5 the
condition σ(ǫ) ≪ ǫ implies that
 i                                       i          i
   Θ(1+σ(ǫ)−ǫ)ϕ+ǫϕe (L) = (1 + σ(ǫ) − ǫ) Θϕ (L) + ǫ Θϕe(L) + σ(ǫ)ddc ϕ > 0.
2π                                      2π         2π
Applying the standard Nadel vanishing theorem on
                             (X, L, I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ))
                                                         e
we get
(1.1)         H i (X, KX + L ⊗ I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ))
                                                    e =0                    for i > 0.
On the other hand, it it not hard to prove that
(1.2)              I+ (ϕ) = I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ)
                                                 e               for ǫ ≪ 1.
We postpone the proof of (1.2) in Lemma 5.2 and conclude first the proof
of Proposition 5.1. Taking ǫ small enough, (1.1) and (1.2) imply the propo-
sition.                                                                  
Lemma 5.2. If ǫ is small enough, then
                           I+ (ϕ) = I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ).
                                                         e
Proof. By Proposition 3.5, we have ϕm 4 ϕ.
                                        e Therefore
                  (1 + σ(ǫ) − ǫ)ϕm + ǫϕm 4 (1 + σ(ǫ) − ǫ)ϕ + ǫϕ,
                                                              e
which implies that
(2.1)                I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ)
                                          e ⊂ I((1 + σ(ǫ))ϕm ).
Notice moreover that Lemma 3.1 implies that
(2.2)                           I((1 + σ(ǫ))ϕm ) ⊂ I+ (ϕ)
for m large enough with respect to σ(ǫ). Combining (2.1) and (2.2), we
obtain
                      I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ) e ⊂ I+ (ϕ).
   For the other side inclusion, we take f ∈ I+ (ϕ)x , i.e., f satisfies
                         Z
(2.3)                         | f |2 e−2(1+δ)ϕ < +∞.
                                 Ux
We need to prove that
                              f ∈ I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ)
                                                       e x.
Since ϕ
      e is a quasi-psh function, by taking ǫ small enough, we have
                             Z
                                      ǫ
(2.4)                             e−2 δ ϕe < +∞.
                                      Ux

     5In our context, ϕ is a function on X, then    i          i
                                                      Θ (L) = 2π Θh0 (L)+ddc ϕ ≥ 0. Therefore
                                                   2π ϕ
     c
dd ϕ ≥ −cω.
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                      25

Therefore (2.3) and (2.4) imply that
                        Z
                            | f |2 e−2(1+σ(ǫ)−ǫ)ϕ−2ǫϕe
                            Ux
                       Z                       Z
                                                        ǫ
                   ≤        | f |2 e−2(1+δ)ϕ         e−2 δ ϕe < +∞
                       Ux                      Ux
by Hölder’s inequality. Then f ∈ I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ),
                                                       e and we obtain
              I+ (ϕ) ⊂ I((1 + σ(ǫ) − ǫ)ϕ + ǫϕ)
                                            e               for ǫ ≪ 1.
The lemma is proved.
                                                                               
  Using Proposition 5.1, we now prove a Kawamata-Viehweg-Nadel type
vanishing theorem by induction on dimension.
Proposition 5.3. Let (L, ϕ) be a pseudo-effective line bundle on a projective
variety X of dimension n. Then
        H p (X, KX + L ⊗ I+ (ϕ)) = 0               for p ≥ n − nd(L, ϕ) + 1.
Proof. If nd(L, ϕ) = n, the proposition has already been proved in Proposi-
tion 5.1.
   Assume now that nd(L, ϕ) < n. Let A be a sufficient ample line bundle
large enough with respect to L, and let S be the zero divisor of a general
section of H 0 (X, A). Let ǫ > 0 be small enough such that the condition of
(iv) of Lemma 4.1 is satisfied (by Lemma 4.1, such kind of ǫ is independent
of A ! ) . Then we have an exact sequence:
(3.1)        0 → I+ (ϕ) ⊗ O(−S) → adjǫS (ϕ) → I+ (S, ϕS ) → 0.
By (iv) of Lemma 4.1, we have
                                 adjǫS (ϕ) = I+ (ϕ).
Then (3.1) induces the following exact sequence:
H q (S, KS +L⊗I+ (ϕ|S )) → H q+1 (X, KX +L⊗I+ (ϕ)) → H q+1 (X, KX +A+L⊗I+(ϕ)),
for every q. Taking A to be sufficient ample, we have
                    H q+1 (X, KX + A + L ⊗ I+ (ϕ)) = 0
by Nadel vanishing theorem. Thus the above exact sequence implies that
          H q (S, KS + L ⊗ I+ (ϕ|S )) → H q+1 (X, KX + L ⊗ I+ (ϕ))
is surjective. The proposition is proved by induction on dimension.
                                                                               
Remark. We can also prove that
             H i (X, KX + A + L ⊗ adjǫS (ϕ)) = 0             for i > 0,
which gives another proof of this theorem.
26                                 JUNYAN CAO

  The main goal of this section is to prove our vanishing theorem in the
Kähler case. For this, we combine the methods developed in [Mou] and
[DP]. First of all, we prove that I+ is essentially with analytic singularities.
More precisely,
Lemma 5.4. Let (L, ϕ) be a pseudo-effective line bundle on a compact
kähler manifold X. Then there exists a quasi-equisingular approximation
{ϕk } of ϕ such that
                           2
(4.1)                I((1 + )ϕk ) = I+ (ϕ)         for k ≫ 1.
                           k
Proof. By [DPS 01], there exists a quasi-equisingular approximation {ϕk }
of ϕ. The comparison of integrals techniques discussed in [DPS 01] implies
that we can choose a subsequence {ϕf (k) } such that
                                 2
(4.1)                      I((1 + )ϕf (k) ) ⊂ I+ (ϕ).
                                 k
In fact, if X is projective, we take s = 1 + ǫ and a subsequence {f (k)}∞   k=1
for f (k) ≫ k in Lemma 3.1. Using Lemma 3.1, we get the inclusion (4.1).
If X is just a compact Kähler manifold, we can get the same inclusion for
some Stein neighborhood. Using the glueing techniques, we obtain also the
inclusion (4.1). (see [DPS 01] for details)
   On the other hand, since ϕk is less singular than ϕ, the definition of I+ (ϕ)
implies that
                           2
                   I((1 + )ϕf (k) ) ⊃ I+ (ϕ)      for k ≫ 1.
                           k
The lemma is thus proved.
                                                                              

   The following lemma will be important in the proof of our Kawamata-
Viehweg-Nadel vanishing theorem. The advantage of the lemma is that to
prove the convergence in higher degree cohomology with multiplier ideal
sheaves, we just need to check the convergence for some smooth metric.
   We first fix some notations. Let (L, ϕ) be a pseudo-effective line bundle
on a compact Kähler manifold X and let U = {Uα }α∈I be a Stein covering
of X. We denote Uα0 α1 ···αq = Uα0 ∩ · · · ∩ Uαq and C q (U , KX ⊗ L ⊗ I+ (ϕ))
the Čech q-cochain associated to KX ⊗ L ⊗ I+ (ϕ). For an element c ∈
C q (U , KX ⊗ L ⊗ I+ (ϕ)), we denote its component on Uα0 α1 ···αq by cα0 α1 ···αq .
Let
                     δp : C p−1 (U , I+ (ϕ)) → C p (U , I+ (ϕ))
be the Čech operator, and Z p (U , I+ (ϕ)) = Ker δp+1 .
Lemma 5.5. Let L be a line bundle on a compact Kähler manifold X and
ϕ a singular metric on L. Let {Uα }α∈I be a Stein covering of X. Let u be
an element in Ȟ p (X, KX + L ⊗ I+ (ϕ)). If there exists a sequence {vk }∞
                                                                         k=1 ⊂
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                     27

C p (U , KX ⊗ L ⊗ I+ (ϕ)) in the same cohomology class as u satisfying the key
L2 convergent condition:
                               Z
(5.1)                     lim         |vk,α0 ...αp |2 → 0,
                         k→∞ Uα ...α
                               0    p

where the L2 norm |v|2 in (5.1) is taken for some fixed smooth metric on L,
then u = 0 in Ȟ p (X, KX + L ⊗ I+ (ϕ)).
Proof. On the p-cochain space C p (U , I+ (ϕ)), we first define a familly of
natural semi-norms: for f ∈ C p (U , I+ (ϕ)), we define a family of semi-norms:
                  Z
                 { |f |2 ω n | any open set V ⋐ Uα0 ...αp }.
                   V
               p
We claim that C (U , I  + (ϕ)) is a Fréchet space with respect to the family of
semi-norms as above.
   Proof of the claim: We need to prove that if fi ∈ I+ (ϕ) and fi → f0
in the family of the above semi-norms, then f0 ∈ I+ (ϕ). First of all, by
the definition of the semi-norms, f0 is holomorphic. By Lemma 5.4 we can
choose a quasi-psh function ψ with analytic singularities such that
                                 I(ψ) = I+ (ϕ).
Let π : Xk → X be a log resolution of ψ. Then the current E = ⌊ddc (ψ ◦ π)⌋
has normal crossing singularities. Since fi ∈ I+ (ϕ) = I(ψ), we have
(5.2)                        (fi ◦ π) · J ∈ O(−E),
where J is the Jacobian of π. Since fi ◦ π ⇀ f0 ◦ π in the sense of weak
convergence and E has normal crossing singularities, (5.2) implies that
                             (f0 ◦ π) · J ∈ O(−E).
Therefore f0 ∈ I+ (ϕ). The claim is proved.
   As a consequence, the Čech operator δp is continuous and its kernel
Z p−1 (U , I+ (ϕ)) is also a Fréchet space. Therefore we have a refined contin-
uous morphism between the following two Fréchet spaces:
                    δp : C p−1 (U , I+ (ϕ)) → Z p (U , I+ (ϕ)).
Since the cokernel of δp is Ȟ p (X, (KX + L) ⊗ I+ (ϕ)) which is of finite di-
mension, by the standard Fredholm theory, the image of δp is closed. Thus
the quotient morphism
                                            Z p (U , I+ (ϕ))
(5.3)                  Z p (U , I+ (ϕ)) →
                                                 Im(δp )
                                 p
is continuous. By observing Z (U ,I+ (ϕ))
                              Im(δp )     = Ȟ p (X, KX + L ⊗ I+ (ϕ)), (5.3)
implies that
(5.4)            Z p (U , I+ (ϕ)) → Ȟ p (X, KX + L ⊗ I+ (ϕ))
is continuous.
28                                JUNYAN CAO

   Thanks to the claim, the condition (5.1) implies that {vk }∞  k=1 tends to 0
in the Fréchet space Z p (U , I+ (ϕ)). Therefore their images in Ȟ p (X, KX ⊗
L ⊗ I+ (ϕ)) tend to 0 by the continuity of (5.4). Since by construction their
images are in the same class [u], we conclude u = 0 in Ȟ p (X, KX ⊗L⊗I+ (ϕ)).
                                                                              
Remark. The essential point here is that for the quasi-psh function ϕ without
analytic singularities, we should consider I+ (ϕ) instead of I(ϕ). We do not
know whether this lemma is also true for I(ϕ).
   We prove Theorem 1.3 in the rest of this section. Since ϕ has not neces-
sarily analytic singularities, this makes troubles when we use L2 estimates.
Therefore we replace ϕ by a quasi-equisingular approximation. Thanks to
Lemma 5.4, we can keep I+ (ϕ) by the metrics (1 + k2 )ϕk with analytic sin-
gularities. We should also use a Monge-Ampère equation to construct other
metrics ϕbk of which we can control the eigenvalues. Therefore we can use L2
estimates for every ϕ
                    bk . By some delicate analysis, we can prove the theorem.
This idea comes from [DP] and [Mou]. We will construct the key metrics
ϕ
bk in Lemma 5.6 and prove some important properties of ϕ     bk in Lemma 5.7
and 5.8. We prove finally the vanishing theorem in Proposition 5.9.
Lemma 5.6. Let (L, ϕ) be a pseudo-effective line bundle on a compact
kähler manifold (X, ω) and let p ≥ n − nd(L, ϕ) + 1. Then there exists a
sequence of new metrics {ϕ  bk }∞
                                k=1 with analytic singularities on L satisfying
the following properties:
   (i) I(ϕ
         bk ) = I+ (ϕ) for all k.
                                                                 i
   (ii) Let λ1,k ≤ λ2,k ≤ · · · ≤ λn,k be the eigenvalues of 2π    Θϕbk (L) with
respect to the base metric ω. Then there exist two sequences τk → 0, ǫk → 0
such that
                          1                               C
              ǫk ≫ τ k +        and      λ1,k (x) ≥ −ǫk − − τk
                          k                               k
for all x ∈ X and k, where C is a constant independent of k.
   (iii) We can choose β > 0 and 0 < α < 1 independent of k such that for
every k, there exists an open subset Uk of X satisfying
            vol(Uk ) ≤ ǫβk     and      λp + 2ǫk ≥ ǫαk on X \ Uk .
Proof. Recall that we first fix a smooth metric h0 on L. Then given a new
metric ϕ as a form of function, we just means that the hermitian metric
form on L is h0 e−ϕ .
   By definition, there exists a s1 > 0 such that
(∗)                          I+ (ϕ) = I((1 + s1 )ϕ).
Let ϕk be the quasi-equisingular approximation of ϕ in Lemma 5.4. Then
there is a positive sequence τk → 0 such that
             i                                   2
(6.1)          Θϕk (L) ≥ −τk ω    and      I((1 + )ϕk ) = I+ (ϕ)
            2π                                   k
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                    29

for every k. We can also choose a positive sequence ǫk → 0 such that
ǫk ≫ τk + k1 .
   We begin to construct new metrics by solving a Monge-Ampère equation.
Let π : Xk → X be a log resolution of ϕk . Then ddc (ϕk ◦ π) is of the form
[Ek ] + C ∞ where [Ek ] is a normal crossing Q-divisor. Let Zk = π∗ (Ek ). By
[Bou], there exists a smooth metric hk on [Ek ], such that for all δ > 0 small
enough,
                                        i
                            π ∗ (ω) + δ Θhk (−Ek )
                                       2π
is a Kähler form on Xk . Therefore, fixing a positive sequence δk → 0, we
can solve a Monge-Ampère equation on Xk :
             i ∗                               i
(6.2)      ((   π Θϕk (L))ac + ǫk π ∗ ω + δk Θhk (−Ek ) + ddc ψk,ǫ,δk )n
            2π                                2π
                                                i
                  = C(k, δ, ǫ) · ǫkn−d (ω + δk Θhk (−Ek ))n
                                               2π
with the condition
                 sup (ϕk ◦ π + ψk,ǫ,δk + δk ln |Ek |hk )(z) = 0
                 z∈Xk

where d = nd(L, ϕ). Thanks to the definition of the numerical dimension,
there exists a uniform constant C > 0 such that C(k, δ, ǫ) ≥ C. By observing
moreover that
                                               i
                     i∂∂ ln |Ek |hk = [Ek ] +    Θh (−Ek ),
                                              2π k
the equation (6.2) implies
                    i
(6.3)                 Θ                          (π ∗ L) ≥ −ǫk ω.
                   2π ϕk +ψk,ǫ,δk +δk ln |Ek |hk
   We define now a new metric on (Xk , π ∗ L) by (i.e. h0 e−ϕbk as a metric
form ! )
                       2
(6.4)     ϕ
          bk = (1 +       − s)ϕk ◦ π + s(ϕk ◦ π + ψk,ǫ,δ + δ ln |Ek |hk )
                       k
where s is a constant sufficient small with respect to s1 . s will be made
precise in Lemma 5.7. Then
(6.5)
 i                        i               i                               2
   Θϕbk (π ∗ L) = (1−s) Θϕk (π ∗ L)+s Θϕk +ψk,ǫ,δ +δk ln |Ek |h (π ∗ L)+ ddc ϕk .
2π                       2π              2π          k            k       k
(6.3) gives the estimate for the second term of the right hand side of (6.5).
For the last term of the right hand side of (6.5), since ϕk is a function on X
satisfying
                     i             i
                       Θϕk (L) =      Θh (L) + ddc ϕk ≥ −cω,
                    2π            2π 0
we have
                                  ddc ϕk ≥ −Cω
30                                       JUNYAN CAO

for some uniform constant C. Then
                      i                              C
(6.6)                   Θϕbk (π ∗ L) ≥ −ǫk ω − τk ω − ω.
                     2π                              k
Thus ϕbk induces a quasi-psh function on X by extending it from X \ Zk to
the whole X. It is the metric that we want to construct. We denote it also
ϕ
bk for simplicity. We will prove properties (i) to (iii) in Lemma 5.7 and
Lemma 5.8.                                                              
Lemma 5.7. If we take s in (6.4) small enough with respect to s1 in (∗) of
Lemma 5.6, then
              Z                        Z
                                                                1
                |f |2 e−2ϕbk ≤ C|f |L∞   (|f |2 e−2(1+s1 )ϕ ) 1+s1
                    U                           U
for all U in X and k ≫ 1, where C|f |L∞ is a constant depending only on
|f |L∞ (in particular, it is independent of the open subset U and k). As a
consequence, we have
                              I(ϕ
                                bk ) = I+ (ϕ)       for any k.
Proof. Thanks to (6.3) in Lemma 5.6, we can extend ϕk +ψk,ǫ,δk +δ ln |Ek |hk
to the whole X, satisfying the same inequality. Then the condition
                        sup (ϕk + ψk,ǫ,δ + δk ln |Ek |hk )(x) = 0
                        x∈X

and (6.3) in Lemma 5.6 imply the existence of a > 0 such that
                      Z
                         e−2a(ϕk +ψk,ǫ,δ +δk ln |Ek |hk )
                                X
is uniformly bounded for all k.
   By Hölder’s inequality and the construction (6.4) in Lemma 5.6, we have
                               Z
(7.1)                             |f |2 e−2ϕbk ≤
                                         U
      Z                        Z         2s(1+s1 )                                s1
                           1
           2 −2(1+s1 )ϕk 1+s1          −           (ϕk +ψk,ǫ,δk +δk ln |Ek |hk ) 1+s
     ( |f | e           )     ( |f |2 e     s1
                                                                                ) 1
       U                             U
for k ≫ 1, where U is any open subset of X. If we take s > 0 satisfying
s(1+s1 )                                                    R
   s1    ≤ a, then the uniform boundness of X e−2a(ϕk +ψk,ǫ,δk +δk ln |Ek |hk )
implies that
             Z           2s(1+s1 )
                       −           (ϕk +ψk,ǫ,δk +δk ln |Ek |hk )
(7.2)           |f |2 e     s1                                   ≤ C · |f |L∞
                U
for any U ⊂ X and k ≫ 1. Combining (7.1) and (7.2), we have
             Z                        Z
                                                              1
                    2 −2ϕ
(7.3)           |f | e  bk
                           ≤ C|f |L∞ ( |f |2 e−2(1+s1 )ϕk ) 1+s1
                    U                           U
                                     Z                      1
                          ≤ C|f |L∞ ( |f |2 e−2(1+s1 )ϕ ) 1+s1 .
                                         U
for some constant C|f |L∞ independent of the open subset U and k ≫ 1.
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                     31

   We now prove the equality I(ϕ   bk ) = I+ (ϕ). The inclusion I(ϕ
                                                                  bk ) ⊃ I+ (ϕ)
comes directly from (7.3). By the construction, ϕ    bk is more singular than
(1 + k2 )ϕk . Then equality (6.1) in Lemma 5.6 implies that I(ϕ  bk ) ⊂ I+ (ϕ).
The lemma is thus proved.
                                                                             

  The following lemma was essentially proved in [Mou].
                            bk }∞
Lemma 5.8. The new metrics {ϕ   k=1 satisfy properties (ii) and (iii) in
Lemma 5.6.
Proof. Let λ1 (z) ≤ λ2 (z) ≤ · · · ≤ λn (z) be the eigenvalues of the new metric
(X, L, ϕ
       bk ) with respect to the base metric ω for simplicity, ( i.e. λi here is
equal to λi,k in Lemma 5.6, since the proof is for fixed k, the simplification
here will not lead misunderstanding.) By (6.6) in Lemma 5.6, we have
                                                  C
                                λi (z) ≥ −ǫk −      − τk .
                                                  k
    bi = λi + 2ǫk . Since s is a fixed positive constant, the Monge-Ampère
Let λ
equation (6.2) implies that
                                 n
                                 Y
(8.1)                                  bi (z) ≥ C(s)ǫn−d
                                       λ             k
                                 i=1

where C(s) > 0 does not depend on k. Since p > n − d, we can take α such
that 0 < α < 1 and n − d < αp.
  Let
                                     bp (z) < ǫα }.
                       Uk = {z ∈ X | λ         k
                             bi (z) = λi (z) + 2ǫk ≥ 0 for any z and i. Thus
Since ǫk ≫ τk + k1 , we have λ
the cohomological condition
                       Z
                          b1 + λ
                         (λ      b2 + · · · + λ
                                              bn )ω n ≤ M
                          X

implies that
                      Z
(8.2)                           b1 + λ
                               (λ    b2 + · · · + λ
                                                  bn )ω n ≤ M.
                          Uk

Observe that (8.1) and the definition of Uk imply that
                    Y                          n−d
                               bi (z) ≥ C(s) ǫkαp
                               λ                        for z ∈ Uk .
                                              ǫk
                  p+1≤i≤n

Then
                   X                        n−d
                           bi (z) ≥ C( ǫkαp ) n−p
                                                    1
(8.3)                      λ                               for z ∈ Uk
                                        ǫk
                 p+1≤i≤n
32                                    JUNYAN CAO

by the inequality of arithmetic and geometric means. Applying (8.3) to
(8.2), we have
                          Z
                                ǫn−d 1
(8.4)                          ( kαp ) n−p ω n ≤ M ′ .
                            U k ǫk

Since n − d < αp, (8.4) implies the existence of β > 0 such that
                                     vol(Uk ) ≤ ǫβk .
The lemma is proved.                                                                    
     We now prove the final conclusion.
Proposition 5.9. Let (L, ϕ) be a pseudo-effective line bundle on a compact
kähler manifold (X, ω). Then
          H p (X, KX ⊗ L ⊗ I+ (ϕ)) = 0            for p ≥ n − nd(L, ϕ) + 1.
Remark. One of the reason to use I+ (ϕ) instead of I(ϕ) is that it does not
seem to be easy to prove that
                    H p (X, KX ⊗ L ⊗ I(ϕ)) = 0             for p ≥ 1
even when X is projective and nd(L, ϕ) = dim X.
Proof. We prove it in two steps.
  Steps 1: L2 Estimates
  Let {ϕbk }∞
            k=1 be the metrics constructed in Lemma 5.6, and let [u] be
any element in H p (X, KX ⊗ L ⊗ I+ (ϕ)). Let f be a smooth (n, p)-form
representing [u]. Then
                         Z
                            |f |2 e−2(1+s1 )ϕ < +∞,
                               X
for the constant s1 in (∗) of Lemma 5.6. Lemma 5.7 implies that
                  Z                  Z
                                                            1
                          2 −2ϕ
(9.1)                 |f | e  bk
                                 ≤ C( |f |2 e−2(1+s1 )ϕ ) 1+s1
                      U                     U
for any open subset U of X and k ≫ 1, where C is a constant independent
of U and k (but certainly depends on |f |L∞ ). We now use the L2 method
in [DP] to get a key estimate: we can write
(9.2)                                f = ∂uk + vk
with the following estimate
(9.3)
 Z                        Z                  Z
                      1                                      1
     |uk |2 e−2ϕbk +         |vk |2 e−2ϕbk ≤                                |f |2 e−2ϕbk ,
   X                 2pǫ k X                     b      b              b
                                               X λ1,k + λ2,k + · · · + λp,k

    bi,k = λi,k + 2ǫk . This comes from the Bochner inequality:
for λ
                            Z
          2       ∗    2           b1,k + λ
                                          b2,k + · · · + λ
                                                         bp,k − Cǫk )|u|2 dV
     k∂ukϕbk + k∂ ukϕbk ≥         (λ                                    ϕ
                                                                        bk
                                X−Zk
          A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                                   33

where Zk is the singular locus of ϕk in X. (see [DP] or the appendix for
details)
   Using (9.3), we claim that
                               Z
(9.4)                      lim    |vk |2 e−2ϕbk → 0.
                                 k→∞ X

Proof of the claim: Properties (ii), (iii) in Lemma 5.6 and (9.3) imply that
                    Z                          Z
                                          1
                        |uk |2 e−2ϕbk +           |vk |2 e−2ϕbk
                      X                 2pǫ k X
                    Z                     Z
                        C1 2 −2ϕbk               1
                  ≤       α |f | e      +              |f |2 e−2ϕbk .
                      X ǫk                  U k C2 ǫ k
Then
          Z                              Z                        Z
(9.5)              2 −2ϕ
               |vk | e bk
                            ≤ C3 ǫ1−α
                                  k
                                                  2 −2ϕ
                                               |f | e bk
                                                           + C4            |f |2 e−2ϕbk .
           X                              X                           Uk

Since vol(Uk ) → 0 by property (iii) of Lemma 5.6, (9.1) implies that the
second term of the right hand side of (9.5) tends to 0. Reminding that
0 < α < 1 and ǫk → 0 as k → ∞, (9.1) implies thus that the first term of
the right hand side of (9.5) also tends to 0. The claim is proved.
   Step 2: Final step
   We use Lemma 5.5 to obtain the final conclusion. Let U = {Uα }α∈I be
a Stein covering of X. Thanks to (9.4), we get a p-cycle representative of
each vk by solving ∂-equations, i.e., vk can be writen as
                   vk = {vk,α0 ...αp } ∈ C p (U , KX ⊗ L ⊗ I(ϕ
                                                             bk ))
satisfying the L2 conditions:
                 Z                               Z
                                       2 −2ϕ
(9.6)                    |vk,α0 ...αp | e  bk
                                              ≤C   |vk |2 e−2ϕbk
                    Uα0 ...αp                              X

where C does not depend on k. (9.6) and property (i) in Lemma 5.6 imply
that {vk }∞               p
          k=1 are all in C (U , KX ⊗ L ⊗ I+ (ϕ)).
   Since ϕ
         bk ≤ 0, (9.4) and (9.6) imply that
                               Z
(9.7)                     lim        |vk,i0 ...ip |2 = 0.
                                k→∞ Ui ...i
                                      0    p

By (9.2), {vk }∞
               k=1 are in the same cohomology of u. Using Lemma 5.5, (9.7)
implies that [u] = 0. Since we choose [u] as any element in H p (X, KX ⊗ L ⊗
I+ (ϕ)), the proposition is proved.
                                                                           

                                      6. Appendix
   For the convenience of reader, we give the proof of estimate (9.3) in Propo-
sition 5.9, but the proof is just extracted from [DP].
34                                          JUNYAN CAO

Proposition 6.1. Let (X, ω) be a compact Kähler manifold and let (L, h0 e−ϕ )
be a line bundle on X where h0 is a smooth metric on L and the quasi-psh
function ϕ has analytic singularities and smooth outside a subvariety Z.
Assume that
                             i
                               Θϕ (L) ≥ −ǫω
                            2π
on X \ Z, and f is a smooth L-valued (n, p)-form satisfying
                          Z
                             |f |2 e−2ϕ dV < ∞.
                                        X
                                               i
Let λ1 ≤ λ2 ≤ .... ≤ λn be the eigenvalues of 2π Θϕ (L) and λ   bi = λi + 2ǫ ≥ ǫ.
Then there exist u and v such that f = ∂u+v and with the following estimate
 Z                      Z                 Z
        2 −2ϕ        1         2 −2ϕ                   1
     |u| e    dV +          |v| e    dV ≤                            |f |2 e−2ϕ dV.
  X                 2pǫ   X                X b
                                             λ 1 + b
                                                   λ 2 + · · · + b
                                                                 λ p

Proof. Let ω1 be a complete Kähler metric on X \ Z and ωδ = ω + δω1 for
some δ > 0. We now do the standard L2 estimate on (X \ Z, ωδ , L, ϕ).
   If s is a L-valued (n, p) form in Cc∞ (X \ Z), then the Bochner inequality
implies that:
                            Z
              2     ∗ 2           b1 + λ
                                       b2 + · · · + λ
                                                    bp − 2pǫ)|s|2 e−2ϕ ω n
(1)      k∂skδ + k∂ skδ ≥        (λ                                     δ
                                      X\Z
                    R
where ksk2δ = X |s|2 e−2ϕ ωδn . Notice that there is an abuse of notion here.
We calculate the norm |u|2 by the metric (or the volum form) in the equa-
tions. For example, if the volum form is ωδn , then we calculate the norm of
u by the metrics ωδ and h0 .              R
   Since f is a (n, p)-form, the condition X |f |2 e−2ϕ ω n < +∞ implies that
                            f ∈ L2 (X \ Z, L, ϕ, ωδ )          for δ > 0.
                                                                                 ∗
We write every form s in the domain of the L2 extension of ∂ as s = s1 + s2
with
                                                           ∗
              s1 ∈ Ker ∂     and    s2 ∈ (Ker ∂)⊥ ⊂ Ker ∂ .
Since f ∈ Ker ∂, by (1) we obtain
                                      |hf, si|2ϕ,δ = |hf, s1 i|2ϕ,δ
     Z                                               Z
                        1                 2 −2ϕ              b1 + λ b2 + · · · + λ
                                                                                 bp )|s1 |2 e−2ϕ dVδ
≤                                     |f | e     dVδ       (λ
         b1 + λ
     X\Z λ    b2 + · · · + λ
                           bp                          X\Z
             Z
                                 1                                ∗
         ≤                                      |f |2 e−2ϕ dVδ (k∂ s1 k2δ + 2pǫk∂s1 k2δ )
                     b1 + λ
                 X\Z λ    b2 + · · · + λ
                                       bp
             Z
                                  1                                ∗
         ≤                         |f |2 e−2ϕ dVδ (k∂ sk2δ + 2pǫk∂sk2δ ).
              b    b            b
          X\Z λ1 + λ2 + · · · + λp
By the Hahn-Banach theorem, we can find vδ , uδ such that
                                            ∗
                        hf, siδ = huδ , ∂ siδ + hvδ , siδ         for any s,
             A KAWAMATA-VIEHWEG-NADEL TYPE VANISHING THEOREM                            35

and with the following estimate
                                 Z
              2    1       2                 1
         kuδ kδ +     kvδ kδ ≤ C                          |f |2 e−2ϕ ωδn .
                  2pǫ                b    b            b
                                   X λ1 + λ2 + · · · + λp

Thereofre
(2)                                  f = ∂uδ + vδ .
Since the norm k · kδ for (n, p)-forms is increasing when δ → 0, we find limits
(3)                      u = lim uδ        and       v = lim vδ
                              δ→0                         δ→0
satisfying
                                Z
                    1                          1
(4)           kuk2δ +     2
                       kvkδ ≤ C                            |f |2 e−2ϕ ωδn
                   2pǫ              b       b
                                 X λ1 + λ2 + · · · + λp  b
                        Z
                                    1
                   ≤C                            |f |2 e−2ϕ ω n
                            b    b            b
                          X λ1 + λ2 + · · · + λp
for any δ > 0. Formulas (2) and (3) imply that f = ∂u + v. Let δ → 0 in
(4), we obtain the estimate in the proposition.
                                                                          

                                     References
[Bou] S.Boucksom, Cones positifs des variétés complexes compactes, Thesis,Grenoble 2002
[Dem] J-P. Demailly, Analytic methods in algebraic geometry, vol. 1 in the Surveys of
     Modern Mathematics series, 2012, International Press of Boston
[DPS 94] J-P. Demailly, Th. Peternell, M. Schneider, Compact complex manifolds with
     numerically effective tangent bundles, J.Algebraic Geometry, 3 (1994), 295-345
[DPS 01] J-P. Demailly, Th. Peternell, M. Schneider, Pseudo-effective line bundles on
     compact Kähler manifolds, International Journal of Math 6 (2001) 689-741
[DP 04] J-P. Demailly, M.Paun, Numerical characterization of the Kähler cone of a com-
     pact Kähler manifold, Annals of Math. 159 (2004) 1247-1274
[DP] J-P. Demailly, Th. Peternell, A Kawamata-Viehweg vanishing theorem on compact
     Kähler manifolds, J. Differential Geometry 63 (2003) 231-277
[FJ] C.Favre, Mattias Jonsson, Valuations and multiplier ideals, J.Amer.Math.Soc. 18
     (2005), 655-684
[K] A. Küronya, Asymptotic cohomological functions on projective varieties, Amer. J.
     Math. 128 (2006), no. 6, 1475–1519
[Mou] C.Mourougane, Versions kählériennes du théorème d’annulation de Bogomolov-
     Sommese, C. R. Acad. Sci. Paris Sér. I Math. 321 (1995), no. 11, 1459–1462
[Tra] S.Trapani, Numerical criteria for the positivity of the difference of ample divisors,
     Math.Zeitschrift, 219 (1995), 387-401
[Tsu] H.Tsuji, Extension of log pluricanonical forms from subvarieties, arXiv: 0709.2710
   E-mail address: junyan.cao@ujf-grenoble.fr

  Université de Grenoble I, Institut Fourier, 38402 Saint-Martin d’Hères,
France


# Complete actual public primary text: 1508.03922v5

                                           OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS

                                                    SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON


                                                  Abstract. An Okounkov body is a convex subset in Euclidean space associated to a big divisor
                                                  on a smooth projective variety with respect to an admissible flag. In this paper, we introduce
arXiv:1508.03922v5 [math.AG] 5 Feb 2018




                                                  two convex bodies associated to pseudoeffective divisors, called the valuative Okounkov bodies
                                                  and the limiting Okounkov bodies, and show that these convex bodies reflect the asymptotic
                                                  properties of pseudoeffective divisors as in the case with big divisors. Our results extend the
                                                  works of Lazarsfeld-Mustaţă and Kaveh-Khovanskii. For this purpose, we define and study
                                                  special subvarieties, called the Nakayama subvarieties and the positive volume subvarieties,
                                                  associated to pseudoeffective divisors.




                                                                                      1. Introduction
                                             For a divisor D on a smooth projective variety X of dimension n, one can associate a convex
                                          body ∆Y• (D), called the Okounkov body of D, in the Euclidean space Rn with respect to
                                          an admissible flag Y• . After the pioneering works by Lazarsfeld-Mustaţă ([LM]) and Kaveh-
                                          Khovanskii ([KK]), motivated by earlier works by Okounkov ([O1], [O2]), the Okounkov bodies
                                          ∆Y• (D) have received a considerable amount of attention in a variety of flavors. It is believed
                                          that this convex body carries rich information of the asymptotic invariants of D. For example,
                                          it was proven in [LM, Theorem A] that if D is big, then the Euclidean volume of ∆Y• (D) in Rn
                                          is equal to the volume volX (D) of a divisor D up to the constant n!, that is, we have
                                                                                                 1
                                                                             volRn (∆Y• (D)) =     volX (D).
                                                                                                n!
                                          However, little is known about the Okounkov bodies for non-big pseudoeffective divisors. One
                                          of the annoying phenomena is that for a pseudoeffective divisor D that is not big, the associated
                                          convex body ∆Y• (D) is not full dimensional in Rn so that its Euclidean volume in Rn is zero.
                                          Nevertheless, it is still tempting to study the asymptotic properties of pseudoeffective divisors
                                          using the associated Okounkov bodies.
                                             In this paper, we introduce and study two different convex bodies, the valuative Okounkov
                                          body ∆val                                           lim
                                                  Y• (D) and the limiting Okounkov body ∆Y• (D), associated to a pseudoeffective divisor
                                          D with respect to an admissible flag Y• (see Definition 1.1). Using these convex bodies, we
                                          extend some of the previous works of [LM] and [KK] on big divisors to the pseudoeffective
                                          divisors. We will readily see that ∆val             lim
                                                                                Y• (D) and ∆Y• (D) with respect to a suitable choice of an
                                          admissible flag Y• encode the asymptotic invariants of the divisor D as in the case of big divisors.
                                             Turning to the details, we recall the construction of the Okounkov body that is equivalent
                                          to the ones given by Lazarsfeld-Mustaţă ([LM]) and Kaveh-Khovanskii ([KK]). Let D be an
                                          R-divisor on a projective variety X of dimension n. We fix an admissible flag Y• on X, which
                                          is, by definition, a sequence of subvarieties
                                                                       Y• : X = Y0 ⊇ Y1 ⊇ · · · ⊇ Yn−1 ⊇ Yn = {x}
                                             Date: September 24, 2018.
                                             2010 Mathematics Subject Classification. 14C20, 52A20.
                                             Key words and phrases. Okounkov body, pseudoeffective divisor, Kodaira dimension, restricted volume,
                                          Nakayama subvariety, positive volume subvariety.
                                             S. Choi and J. Park were partially supported by the NRF grant (NRF-2016R1C1B2011446). J. Won was
                                          partially supported by IBS-R003-D1, Institute for Basic Science in Korea.
                                                                                                1
2              SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

such that each Yi is an (n − i)-dimensional irreducible subvariety of X that is nonsingular at
a point x. After possibly replacing X by an open subset, we may suppose that each Yi+1 is a
Cartier divisor on Yi . Let |D|R := {D ′ | D ∼R D ′ ≥ 0} and suppose that it is nonempty. We
define a valuation-like function
                                        νY• : |D|R → Rn≥0
as follows. For D ′ ∈ |DR |, let
            ν1 = ν1 (D ′ ) := ordY1 (D ′ ) and         ν2 = ν2 (D ′ ) := ordY2 ((D ′ − ν1 (D ′ )Y1 )|Y1 ).
Assuming we have defined ν1 , ν2 , · · · , νi−1 , we inductively define νi as
             νi = νi (D ′ ) := ordYi ((· · · ((D ′ − ν1 Y1 )|Y1 − ν2 Y2 )|Y2 − · · · − νi−1 Yi−1 )|Yi−1 ).
By collecting the values νi = νi (D ′ ), we obtain
                                         νY• (D ′ ) = (ν1 , · · · , νn ) ∈ Rn≥0 .
Following [LM] and [KK], we define the Okounkov body ∆Y• (D) of a divisor D with respect to
an admissible flag Y• as the closed set
                    ∆Y• (D) := the closure of the convex hull of νY• (|D|R ) in Rn≥0 .
In [LM], Lazarsfeld-Mustaţă mainly consider the Okounkov body ∆Y• (D) of a big divisor D.
However, the valuation-like function νY• works for any divisors D with nonempty |D|R , and the
construction of the Okounkov body can be carried out for such divisors without any changes.
See Subsection 3.1 for more details.
  Now we define the valuative Okounkov body and the limiting Okounkov body of a divisor.
Definition 1.1. Let D be an R-divisor on a smooth projective variety X of dimension n, and
Y• be an admissible flag on X.
 (1) Suppose that D is effective up to R-linear equivalence, that is, |D|R 6= ∅. The valuative
  Okounkov body ∆val
                   Y• (D) of D with respect to Y• is defined as

                    ∆val                                                         n
                     Y• (D) := the closure of the convex hull of νY• (|D|R ) in R≥0 .
                                         ∗
 If |D|R = ∅, then we put ∆val
                             Y• (D) := ∅.
(2) Suppose that D is pseudoeffective. The limiting Okounkov body ∆lim
                                                                    Y• (D) of D with respect
 to Y• is defined as
                                                   \
                   ∆lim
                     Y• (D) := lim ∆Y• (D + εA) =     ∆Y• (D + εA) in Rn≥0
                                      ε→0+
                                                                   ε>0

    where A is a fixed ample divisor on X. If D is not pseudoeffective, then we put ∆lim
                                                                                      Y• (D) := ∅.
    Note that the definition of the limiting Okounkov body ∆lim
                                                              Y• (D)  is independent of the choice
    of the ample divisor A.

  We briefly recall definitions of some of basic asymptotic invariants of divisors. Let D be an
R-divisor on a smooth projective variety X. The restricted volume of D along a v-dimensional
subvariety V of X is defined as
                                                            h0 (X|V, ⌊mD⌋)
                                    volX|V (D) := lim sup
                                                        m→∞      mv /v!

    ∗ By definition, we have in fact ∆             val
                                         Y• (D) = ∆Y• (D) for any divisor D.
                                                                          However, in this paper, we use the
notation ∆Y• (D) only when D is a big divisor in order to stress the properties of ∆val          lim
                                                                                    Y• (D) and ∆Y• (D) for a
non-big divisor D.
                OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                          3

where h0 (X|V, ⌊mD⌋) is the dimension of the image of the restriction map H 0 (X, OX (⌊mD⌋)) →
H 0 (V, OV (⌊mD⌋)). Note that volX|X (D) =: volX (D) is the usual volume of the divisor D. When
V 6⊆ B− (D), the augmented restricted volume of D along V is defined as
                               vol+
                                  X|V (D) := lim volX|V (D + εA)
                                             ε→0+

where A is some fixed ample divisor on X. It is independent of the choice of the ample divisor
A. For more details, we refer to Subsection 2.3. The Iitaka dimension of D is defined as
                                                                        
                                                   h0 (X, OX (⌊mD⌋))
                  κ(D) := max k ∈ Z≥0 lim sup                         >0
                                             m→∞           mk
if h0 (X, OX (⌊mD⌋)) 6= 0 for some m > 0, and κ(D) := −∞ otherwise. Similarly, the numerical
Iitaka dimension of D is defined as
                                                                         
                                                h0 (X, OX (⌊mD⌋ + A))
                κν (D) := max k ∈ Z≥0 lim sup                         >0
                                           m→∞            mk
for some fixed ample Cartier divisor A if h0 (X, OX (⌊mD⌋ + A)) 6= 0 for some m > 0, and
κν (D) := −∞ otherwise. It is also independent of the choice of the ample divisor A. For more
details, see Subsections 2.4 and 2.5.
   To extract asymptotic invariants of a divisor D with κ(D) ≥ 0 from the valuative Okounkov
body ∆valY• (D), we consider an admissible flag Y• that contains a special subvariety Yn−κ(D) =
U ⊆ X such that the natural restriction map H 0 (X, OX (⌊mD⌋)) → H 0 (U, OU (⌊mD|U ⌋)) is
injective for every integer m ≥ 0. We call such U a Nakayama subvariety of D (see Subsection
2.4). Note that any general subvariety of dimension κ(D) is a Nakayama subvariety of D
(Proposition 2.13). If D is big, then X itself is the unique Nakayama subvariety of D.
Theorem A (=Theorem 3.12). Let D be an R-divisor on a smooth projective variety X of
dimension n such that κ(D) ≥ 0. Fix an admissible flag Y• containing a Nakayama subvariety
U of D such that Yn = {x} is a general point. Then ∆val         n−κ(D) ×Rκ(D) . Furthermore,
                                                    Y• (D) ⊆ {0}          ≥0
we have
                                                                 1
              dim ∆val                              val
                    Y• (D) = κ(D) and volRκ(D) (∆Y• (D)) =          volX|U (D)
                                                              κ(D)!
where ∆val
       Y• (D) is regarded as a convex subset of R
                                                  κ(D) .


   For convenience, we define dim(point) := 0 and volR0 (point) := 1 throughout the paper.
Theorem A does not hold if D is only effective up to R-linear equivalence (see Remark 3.14).
   To investigate the asymptotic properties of a pseudoeffective divisor D using the limiting
Okounkov body ∆lim Y• (D), we consider an admissible flag Y• that contains a special subvariety
Yn−κν (D) = V ⊆ X such that vol+ X|V (D) > 0. We call such V a positive volume subvariety of D
(see Subsection 2.5). Note that that the intersection of (n − κν (D)) general ample divisors is a
positive volume subvariety of D (Proposition 2.22). Thus we may take a general admissible flag
Y• constructed by successively intersecting general ample divisors. If D is big, then X itself is
the unique positive volume subvariety of D.
Theorem B (=Corollary 3.22). Let D be a pseudoeffective R-divisor on a smooth projective
variety X of dimension n. Fix an admissible flag Y• containing a positive volume subvariety V
of D. Then ∆lim           n−κν (D) × Rκν (D) . Furthermore, we have
              Y• (D) ⊆ {0}            ≥0
                                                                        1
             dim ∆lim
                  Y• (D) = κν (D) and       volRκν (D) (∆lim
                                                         Y• (D)) =           vol+
                                                                                X|V (D)
                                                                     κν (D)!
where ∆lim
       Y• (D) is regarded as a convex subset of R
                                                  κν (D) .
4            SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

   In general, we have ∆val         lim
                        Y• (D) ⊆ ∆Y• (D) (see Remark 3.31), and the inclusion can be strict
(see Example 4.2). Note that if D is big, then we have
                                  ∆val       lim
                                   Y• (D) = ∆Y• (D) = ∆Y• (D).
We also remark that Di Biagio-Pacienza [DP] also studied valuative Okounkov bodies of effective
divisors and the subvarieties on which the restricted divisors behave like big divisors.
   Recall that the Okounkov body of a big divisor is a numerical invariant. More precisely, by
[LM, Proposition 4.1] and [J, Theorem A], for big divisors D, D ′ on X, we have ∆Y• (D) =
∆Y• (D ′ ) for any admissible flag Y• if and only if D ≡ D ′ . As Theorem C states below, this
result can be extended to the limiting Okounkov bodies ∆lim  Y• (D) for pseudoeffective divisors D.
                                                         val
We note however that the valuative Okounkov body ∆Y• (D) is not a numerical invariant (see
Remark 3.13), but an invariant of R-linear equivalence (see Proposition 3.15).
Theorem C (=Theorem 3.27). Let D, D ′ be pseudoeffective R-divisors on a smooth projective
variety X. Then
             D ≡ D ′ if and only if ∆lim       lim  ′
                                     Y• (D) = ∆Y• (D ) for every admissible flag Y• .

    Since the limiting Okounkov body is a numerical invariant, we can consider a function
                                ∆lim            n          lim
                                 Y• : Eff(X) → R≥0 , ξ 7→ ∆Y• (ξ)
for a fixed admissible flag Y• on a smooth projective variety X of dimension n. By [LM, Theorem
B] and the definition of the limiting Okounkov body, the shapes of limiting Okounkov bodies
continuously change. In contrast, Example 4.2 also shows discontinuity of valuative Okounkov
bodies at some non-big divisor class.
   We finally remark that Boucksom also defined and studied the limiting Okounkov body (the
numerical Okounkov body in his terminology) in [B]. See Remark 3.24 for more details on his
results. In this paper, we do not use any results in [B].
   This paper is organized as follows. We start in Section 2 by collecting relevant basic facts on as-
ymptotic invariants such as asymptotic base locus, asymptotic valuation, (augmented) restricted
volume, (numerical) Iitaka dimension, etc., and prove some useful properties of Nakayama subva-
rieties and positive volume subvarieties. Section 3 is the main part of this paper. We first recall
the construction of the Okounkov body ∆Y• (D) of a big divisor D in Subsection 3.1. We then
introduce and study the valuative Okounkov body ∆val     Y• (D) and the limiting Okounkov body
  lim
∆Y• (D) of a pseudoeffective divisor D in Subsections 3.2 and 3.3, respectively. Especially, we
prove Theorems A, B, and C. Finally, in Section 4, we exhibit various examples of the valuative
Okounkov body ∆val                                              lim
                    Y• (D) and the limiting Okounkov body ∆Y• (D).

Aknowledgement. We are grateful to Mihai Fulger for helpful suggestions and useful com-
ments. We would like to thank the referee for careful reading of our manuscript and for making
a number of valuable suggestions.

                                        2. Preliminaries
   In this section, we collect basic facts and introduce some notions that will be used in later
sections. First, we fix some notations. Throughout the paper, we work over the field C of
complex numbers. For simplicity, a variety in this paper is assumed to be smooth, projective,
reduced and irreducible, but a subvariety can be singular. By a divisor on a variety X, we always
mean an R-divisor unless otherwise stated. Since we assume that X is smooth, every divisor is
R-Cartier. A divisor D is called pseudoeffective if its numerical class [D] ∈ N1 (X)R := N1 (X)⊗R
lies in the pseudoeffective cone Eff(X), the closure of the cone N1 (X)R spanned by the classes
of effective divisors. A divisor is called big if its numerical class lies in the big cone Big(X), the
interior of Eff(X).
                 OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                           5

2.1. Asymptotic base locus.
   Let D be a divisor on a smooth projective variety X. If D is a Q-divisor, then we define the
stable base locus of D as                     \
                                    SB(D) :=      Bs(mD)
                                                    m
where the intersection is taken over all positive integers m such that mD are Z-divisors, and
Bs(mD) denotes the base locus of the linear system |mD|. Now we assume that D is an R-divisor.
The augmented base locus B+ (D) is defined as
                                               \
                                   B+ (D) :=      SB(D − A)
                                                A

where the intersection is taken over all ample divisors A such that D − A are Q-divisors. The
restricted base locus B− (D) of D is defined as
                                              [
                                   B− (D) :=     SB(D + A).
                                                A

where the union is taken over all ample divisors A such that D + A are Q-divisors. We have
B− (D) ⊆ SB(D) ⊆ B+ (D) for a Q-divisor D. One can check that a divisor D is ample (or nef)
if and only if B+ (D) = ∅ (respectively, B− (D) = ∅). Furthermore, D is not pseudoeffective
(or not big) if and only if B− (D) = X (respectively, B+ (D) = X). The asymptotic base loci
B+ (D) and B− (D) depend only on the numerical class of D while SB(D) does not (see [La,
Example 10.3.3]). For more properties, we refer to [ELMNP1].

2.2. Asymptotic valuation.
   Let D be a pseudoeffective divisor on a smooth projective variety X, and V ⊆ X be an
irreducible subvariety of X. When D is big, we define the asymptotic valuation of V at D as
                          ordV (||D||) := inf{ordV (D ′ ) | D ≡ D ′ ≥ 0}.
When D is non-big pseudoeffective, we define
                              ordV (||D||) := lim ordV (||D + εA||)
                                             ε→0+

for some ample divisor A. This definition is independent of the choice of A, and the value
ordV (||D||) depends only on the numerical class [D] ∈ N1 (X)R (see [N, Chapter III]).
Remark 2.1. By [Le2, Proposition 6.4], if D is an abundant pseudoeffective divisor, then the
limit process in computing ordX (||D||) is unnecessary. Otherwise, it is necessary in general. For
example, let π : S → P2 be the blow-up of P2 at nine general points. Then |− KS | consists of one
irreducible curve C, and | − mKS | = {mC} for any integer m > 0. Thus ordC (D ′ ) = 1 for every
effective divisor D with D ≡ −KS . On the other hand, since −KS is nef, ordC (|| − KS ||) = 0
by Theorem 2.2.
  The restricted base locus B− (D) can be characterized in terms of ordV (||D||) as follows.
Theorem 2.2 ([ELMNP1, Proposition 2.8],[N, Lemma V.1.9]). Let D be a pseudoeffective
divisor on a variety X, and V ⊆ X an irreducible subvariety. Then V ⊆ B− (D) if and only if
ordV (||D||) > 0.
   The asymptotic valuation is a birational invariant: for a birational morphism f : Y → X
with the exceptional divisor E such that f (E) = V , we have ordV (||D||) = ordE (||f ∗ (D)||) (see
[BBP, Lemma 1.4]). For more details on asymptotic valuations, see [ELMNP1] and [N, Chapter
III].
6            SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

2.3. Augmented restricted volume.
   In this subsection, we introduce the notion of the augmented restricted volume. For this
purpose, we first recall the restricted volume function. Let D be a divisor on a smooth projective
variety X of dimension n, and V be a v-dimensional irreducible subvariety of X. For the
natural restriction map ϕ : H 0 (X, OX (⌊D⌋)) → H 0 (V, OV (⌊D⌋)), we denote the image Im(ϕ)
by H 0 (X|V, ⌊D⌋) and its dimension by h0 (X|V, ⌊D⌋). We define the restricted volume of D
along V as
                                                  h0 (X|V, OX (⌊mD⌋))
                            volX|V (D) := lim sup                      .
                                            m→∞           mv /v!
Remark 2.3. In [ELMNP2], the restricted volume volX|V (D) is initially defined for a Q-divisor
D. If V 6⊆ B+ (D), then volX|V (D) depends only on the numerical class of a Q-divisor D
([ELMNP2, Corollary 2.14]). Furthermore, the restricted volume function uniquely extends to
a continuous function
                                    volX|V : BigV (X) → R≥0
where BigV (X) is the set of all R-divisor classes ξ such that V is not properly contained in any
irreducible component of B+ (ξ), and volX|V (ξ) = 0 if and only if V is an irreducible component
of B+ (ξ) ([ELMNP2, Theorem 5.2]).
   On the other hand, one can easily show that our restricted volume volX|V for Q-divisors is
homogeneous of degree v so that our definition of volX|V (D) coincides with that in [ELMNP2]
for a Q-divisor D. By perturbing by ample divisors and using the continuity property, one
can also check that for any R-divisor D such that [D] ∈ BigV (X), our definition of volX|V (D)
coincides with the value volX|V ([D]) of the continuous function volX|V : BigV (X) → R≥0 in
[ELMNP2, Theorem 5.2]. See also [Le1, Remark 2.13].
   By Remark 2.3 and [ELMNP2, Corollary 2.14], volX|V (D) depends only on the numerical
class of an R-divisor D, and by [ELMNP2, Theorem 5.2], we obtain a continuous function

                                    volX|V : BigV (X) → R≥0 ,
and volX|V (ξ) = 0 if and only if V is an irreducible component of B+ (ξ). Furthermore, by
[ELMNP2, Corollary 2.15], ‘lim sup’ can be replaced by ‘lim’ in the definition of the restricted
volume volX|V (D) of a divisor D when V 6⊆ B+ (D).
  By letting V = X, we recover the classical volume function volX (D) = volX|X (D). Note that
BigX (X) = Big(X). Thus we obtain a continuous function volX : Big(X) → R>0 . Furthermore,
the volume function continuously extends to the entire Néron-Severi space
                                     volX : N1 (X)R → R≥0 ,
and volX (ξ) = 0 if and only if ξ 6∈ Big(X) (see [La, Corollary 2.2.45]). For more details on the
functions volX and volX|V , see [ELMNP2], [La], [Le1], etc.
   If D is a non-big pseudoeffective divisor, then B+ (D) = X. Thus the functions volX|V and
volX do not capture the subtle asymptotic properties of pseudoeffective divisors that are not
big on V or X. In such situations, the following function seems useful.
Definition 2.4. Let D be a pseudoeffective divisor on a smooth projective variety X, and
V ⊆ X be an irreducible subvariety such that V 6⊆ B− (D). The augmented restricted volume of
D along V is defined as
                              vol+
                                 X|V (D) := lim volX|V (D + εA)
                                             ε→0+

where A is an ample divisor on X.
                 OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                          7

   Note that if V 6⊆ B− (D), then V 6⊆ B+ (D + εA) for any ample divisor A and for any ε > 0.
Thus using the above basic properties of volX|V , we can deduce that in Definition 2.4, the limit
exists and vol+
              X|V (D) is independent of the choice of A.
   We also observe that vol+X|V (D) depends only on the numerical class of D. This can be seen
as follows. Let D ≡ D and V 6⊆ B− (D) = B− (D ′ ). Then volX|V (D + εA) = volX|V (D ′ + εA)
                        ′

so that by taking the limit ε → 0, we obtain vol+             +     ′
                                                 X|V (D) = volX|V (D ). By the continuity of the
function volX|V , we also see that
                           vol+                               V
                              X|V (D) = volX|V (D) for D ∈ Big (X).

For a divisor D such that [D] ∈ Eff(X) \ Big(X) and V 6⊆ B− (D), by definition, vol+  X|V (D) is
the limit of the values of the continuous function volX|V . Thus we obtain a continuous function
                                                 V
                                      vol+
                                         X|V : Eff (X) → R
          V                                                                            V
where Eff (X) := BigV (X) ∪ {ξ ∈ Eff(X) \ Big(X) | V 6⊆ B− (ξ)}. For D ∈ Eff (X), the
following inequalities hold by definition:
                             volX|V (D) ≤ vol+
                                             X|V (D) ≤ volV (D|V ).
Both inequalities can be strict in general.
Example 2.5. Let S be a relatively minimal rational elliptic surface, and H be an ample Z-
divisor on S. Take a general element V ∈ |kH| for a sufficiently large integer k > 0. Then
                         0
volS|V (−KS ) = lim sup h (S,OSm
                               (−mKS ))
                                        is apparently independent of k and H. However, one can
                 m→∞
check that vol+                                   +
              S|V (−KS ) = (−KS ) · (kH). Thus volS|V (−KS ) can be arbitrarily large depending
on k. Thus we have volS|V (−KS ) < vol+
                                      S|V (−KS ).
2.4. Nakayama subvariety.
   In this subsection, we introduce and study Nakayama subvarieties of divisors, which are closely
related to the Iitaka dimension. Let X be a smooth projective variety.
Definition 2.6. For a divisor D on a variety X, the Iitaka dimension of D is defined as
                                                                       
                                                  h0 (X, OX (⌊mD⌋))
                 κ(D) := max k ∈ Z≥0 lim sup                        >0
                                           m→∞            mk
if h0 (X, OX (⌊mD⌋)) 6= 0 for some m > 0, and κ(D) := −∞ otherwise.
Remark 2.7. If D is a divisor such that κ(D) ≥ 0, then there exists an integer m0 ≥ 1 such
that h0 (X, OX (⌊mm0 D⌋)) ∼ mκ(D) for m ≫ 0 ([N, Theorem II.3.7]). For this m0 , we have
κ(D) = κ(m0 D). Thus in many situations below, we may assume that m0 = 1.
Remark 2.8. Note that the Iitaka dimension κ(D) is not a numerical invariant in general ([Le1,
Example 6.1]). Moreover, it is not an R-linear invariant in general, that is, κ(D) 6= κ(D ′ ) even
if D ∼R D ′ . For instance, let P, Q be distinct points on P1 . For an irrational number a ∈ R,
we consider an R-divisor D := a(P − Q). We have D ∼R 0, so D is effective up to R-linear
equivalence. But κ(a(P − Q)) = −∞ since ⌊ma(P − Q)⌋ = ⌊ma⌋P − (⌊ma⌋ + 1)Q < 0 for any
integer m > 0. However, if both D, D ′ are effective and D ∼R D ′ , then κ(D) = κ(D ′ ) holds true
(see [G, Remark 2.1]).
Remark 2.9. We have the following implications:
                            D is effective ⇒ κ(D) ≥ 0 ⇒ |D|R 6= 0.
If the latter condition holds, then we say that D is effective up to R-linear equivalence. By what
we have seen above, it is easy to check that the converses are not true in general.
8             SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

    The following is well known, but we include the whole proof for reader’s convenience.
                                                                                    P
Lemma 2.10. Let P be a principal R-divisor. Then we may write P = ki=1 ai div(fi ) where
a1 , · · · , ak are real numbers linearly independent over Q and f1 , · · · , fk ∈ C(X) are rational
functions.
                                                                                     P
Proof. Let k be the minimum of integers m such that we may write P = m                 i=1 ai div(fi ) where
ai are real numbers and fi ∈ C(X) are rational functions. We now fix an expression P =
Pk
   i=1 ai div(fi ). Suppose that a1 , · · · , ak are not linearly independent over Q. Possibly by
reordering the indices, we have
                                             p1           pk−1
                                      ak = a1 + · · · +        ak−1
                                             q1           qk−1
where pi , qi are relatively prime integers with qi 6= 0. Then we obtain
                              k−1
                              X                           X  k−1
                                                 pi                ai               
                          P =     ai div(fi ) + div(fk ) =            div fiqi fkpi
                                                 qi                qi
                             i=1                                i=1
which is a contradiction to the minimality of k.                                                          
    The following lemma is useful when we deal with effective R-divisors.
Lemma 2.11. Let D be an effective  P       divisor on aPvariety X, and D ′ ∈ |D|R be any element.
Suppose that we can write D = i ai Ei and D ′ = j a′j Ej′ where Ei , Ej′ are prime divisors and
ai , a′j > 0. Then for any sufficiently small ε > 0, there exist a sufficiently large and divisible
                                                                                 P        P
integer m > 0 and an effective divisor G ∈ |⌊mD⌋| such that we can write m  G
                                                                              = i bi Ei + j b′j Ej′
where bi < ε and |a′j − b′j | < ε for all i, j.
Proof. SincePD ∼R D ′ , there exist rational functions fk ∈ C(X) and real numbers ck such that
D = D ′ + k ck div(fk ). By Lemma 2.10, we may assume that ck are linearly independent
over Q. Then Supp div(fk ) ⊆ Supp(D) ∪ Supp(D ′ ) for eachPk. There are arbitrarily small real
numbers c′k such that          ′
                  P c′k − ck are rational     numbers, D ′ + k c′k div(fk ) is an effective divisor,
                ′                       ′
and | multEj′ (D + k ck div(fk )) − aj | are arbitrarily small for all j. We now have
                                      !                                                  !
                     X                    X                               X
         D = D′ +         c′k div(fk ) +     (ck − c′k )div(fk ) ∼Q D ′ +    c′k div(fk ) .
                         k                   k                                  k
                                                                               P
For a sufficiently large and divisible integer m > 0, let G := ⌊m (D ′ +               ′
                                                                                    k ck div(fk ))⌋. Then we
have                                          P            P
                                         G   ⌊ j ma′j Ej′ + k mc′k div(fk )⌋
                     ⌊mD⌋ ∼ G and          =                                 .
                                         m                 m
Since m > 0 is sufficiently large, Supp(div(fk )) ⊆ Supp(D) ∪ Supp(D ′ ) and c′k are arbitrarily
small for all k, we obtain the assertion.                                                     
    Now we define the Nakayama subvariety associated to an effective divisor.
Definition 2.12. Let D be a divisor on a variety X with κ(D) ≥ 0. An irreducible subvariety
U ⊆ X is called a Nakayama subvariety of D if κ(D) = dim U and the natural map
                             H 0 (X, OX (⌊mD⌋)) → H 0 (U, OU (⌊mD|U ⌋))
is injective (or equivalently, H 0 (X, IU ⊗ OX (⌊mD⌋)) = 0 where IU is an ideal sheaf of U in X)
for every integer m ≥ 0.
   By definition, U = X is the (unique) Nakayama subvariety of D if and only if D is big. The
following lemma guarantees the existence of smooth Nakayama subvarieties. It also shows that
a Nakayama subvariety is not unique in general.
                OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                          9

Proposition 2.13 (cf. [N, Lemma V.2.11]). Let D be a divisor on a variety X with κ(D) ≥ 0.
Any general subvariety U ⊆ X of dimension κ(D) is a Nakayama subvariety of D. In particular,
U = A1 ∩ · · · ∩ An−κ(D) is a Nakayama subvariety of D where A1 , · · · , An−κ(D) are general
members of sufficiently ample linear systems.
Proof. Consider a dominant rational map ϕm : X 99K Zm induced by a complete linear series
|⌊mD⌋| for any integer m > 0 such that |⌊mD⌋| =   6 ∅. We have dim Zm ≤ κ(D) = dim U . Let
f : Y → X be the blow-up at U with the exceptional divisor E. Since U ⊆ X is general,
f ∗ (⌊mD⌋) − kE is not effective for any k > 0. Thus H 0 (X, IU ⊗ OX (⌊mD⌋)) = 0, and hence, U
is a Nakayama subvariety of D. The latter statement also follows from this argument.         
  Nakayama subvarieties have the following properties.
Lemma 2.14. If D, D ′ are divisors on a variety X such that κ(D), κ(D ′ ) ≥ 0 and D ∼R D ′ ,
then they have the same Nakayama subvarieties.
Proof. The given conditions imply that κ(D) = κ(D ′ ). Suppose that U is a Nakayama subvariety
of D, but it is not a Nakayama subvariety of D ′ . Then for some integer m > 0, there exist an
effective Z-divisor E such that E ∼ ⌊mD ′ ⌋ and an irreducible component E0 of E that contains
U . This means that there exists an element D ′′ ∈ |D ′ |R = |D|R such that E0 is a component of
D ′′ . By Lemma 2.11, we can find an integer m′ > 0 such that some element of ⌊m′ D⌋ contains
E0 as an irreducible component. Then such an element should also contain U . Thus we have a
contradiction to our assumption that U is a Nakayama subvariety of D.                         
  Let V be a smooth subvariety of a variety X. A birational morphism f : Y → X is said to
be V -birational if V is not contained in the image of the f -exceptional locus. We denote by Ve
the proper transform of V on Y . Then the pair (Y, Ve ) is called a V -birational model of X (see
[Le1, Definition 2.10]).
Proposition 2.15. Let U ⊆ X be a Nakayama subvariety of a divisor D on a variety X with
                                                         e is also a Nakayama subvariety of
κ(D) ≥ 0. If f : Y → X is a U -birational morphism, then U
 ∗
f D.
                    e is not a Nakayama subvariety of f ∗ D. Then there exists an integer
Proof. Suppose that U
m > 0 and an effective Z-divisor E on Y such that E ∼ ⌊mf ∗ D⌋ and U   e ⊆ Supp(E). Then
             ∗
f∗ E ∼ f∗ ⌊mf D⌋ = ⌊mD⌋ and U ⊆ Supp(f∗ E). By definition, this is a contradiction.      
Theorem 2.16. Let D be a divisor on a variety X with κ(D) ≥ 0, and U ⊆ X be its Nakayama
subvariety. Then D|U is big.
Proof. By the definition of Nakayama subvariety, we have
                           h0 (U, OU (⌊mD|U ⌋)) ≥ h0 (X, OX (⌊mD⌋))
for every integer m ≥ 0. Since h0 (X, OX (⌊mD⌋)) ∼ mκ(D) for m ≫ 0, the assertion follows.     
2.5. Positive volume subvariety.
   In this subsection, we introduce and study positive volume subvarieties of divisors, which are
closely related to the numerical Iitaka dimension and the restricted volume. First, we review
the numerical Iitaka dimension.
Definition 2.17. Let D be a divisor on a variety X. We define the numerical Iitaka dimension
of D as the nonnegative integer
                                                                         
                                                 h0 (X, OX (⌊mD⌋ + A))
               κν (D) := max k ∈ Z≥0 lim sup                           >0
                                          m→∞              mk
for some fixed ample Cartier divisor A if h0 (X, OX (⌊mD⌋ + A)) 6= ∅ for infinitely many m > 0
and we let κν (D) := −∞ otherwise.
10              SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

  The numerical Iitaka dimension κν (D) depends only on the numerical class [D] ∈ N1 (X)R .
Note that D is pseudoeffective if and only if κν (D) ≥ 0. One can easily check that κ(D) ≤ κν (D)
holds and the inequality is strict in general (see [Le1, Example 6.1]). However, if κν (D) = dim X,
then κ(D) = dim X. See [N], [Le1], and [E] for detailed properties of κ and κν .
  The following theorem relates the numerical Iitaka dimension κν (D) and vol+      X|V (D).

Theorem 2.18 ([Le1, Theorem 1.1]). Let D be a pseudoeffective divisor on a variety X. Then
we have
               κν (D) = max{dim W | vol+X|W (D) > 0 and W 6⊆ B− (D)}.

  The numerical Iitaka dimension κν (D) actually coincides with many other invariants defined
with D. For details, see [Le1] and [E].
  Now we define the positive volume subvariety associated to a pseudoeffective divisor.
Definition 2.19. Let D be a pseudoeffective divisor on a variety X. A subvariety V ⊆ X
of dimension κν (D) such that vol+  X|V (D) > 0 and V 6⊆ B− (D) is called a positive volume
subvariety of D. (In other words, a positive volume subvariety V ⊆ X is the subvariety at which
the maximum in Theorem 2.18 is attained.)
Remark 2.20. In [CPW, Lemma 4.3], we show that vol+       X|V (D) > 0 implies V 6⊆ B− (D). Thus
the condition V 6⊆ B− (D) in the definition of the positive volume subvariety is redundant.
Example 2.21. Let S be a relatively minimal rational elliptic surface with a reducible singular
fiber, and E a (−2)-curve in a singular fiber. Then E 6⊆ B− (−KS ) but vol+ S|E (−KS ) = 0. In
this example, we see that V 6⊆ B− (D) and dim V = κν (D) does not imply vol+ X|V (D) > 0.

   By definition, if D is a big divisor on X, then V = X is the unique positive volume subvariety
of D. Theorem 2.18 guarantees the existence of a positive volume subvariety in general. Fur-
thermore, we can also find a smooth positive volume subvariety by the following. It also shows
that a positive volume subvariety is not unique in general.
Proposition 2.22. Let D be a pseudoeffective divisor on a variety X of dimension n. If
κν (D) < n, then the subvariety V := A1 ∩ · · · ∩ An−κν (D) satisfies vol+     X|V (D) > 0, where
A1 , · · · , An−κν (D) are general members of sufficiently ample linear systems. In particular, V is
a positive volume subvariety of D.
Proof. By Theorem 2.18, there exists a positive volume subvariety W of D. In particular, we
have vol+X|W (D) > 0. We can take a sequence {Hi }i∈Z≥0 of ample divisors on X such that each
D + Hi is a Q-divisor and Hi → 0 as i → ∞. For a large and sufficiently divisible integer
                                     1 , · · · , E κν (D) ∈ |k(D + H )|. Since A , · · · , A
k, choose κν (D) general divisors Ek,i            k,i               i           1           n−κν (D) are
sufficiently ample divisors, we have
              1               κ (D)                           1                      κ (D)
       #(V ∩ Ek,i ∩ · · · ∩ Ek,iν     \ SB(D + Hi )) ≥ #(W ∩ Ek,i ∩ · · · ∩ Ek,iν            \ SB(D + Hi )).
Thus by applying [ELMNP2, Theorem B], we obtain
                                                           κ (D)
                                                  1 ∩···∩E ν
                                            #(V ∩Ek,i     k,i      \SB(D+Hi ))
             volX|V (D + Hi ) = lim                     k κν (D)
                                      k→∞
                                                           κ (D)
                                                  1 ∩···∩E ν
                                            #(W ∩Ek,i     k,i      \SB(D+Hi ))
                                    ≥ lim               k κν (D)
                                                                                 = volX|W (D + Hi ).
                                      k→∞

This implies that vol+            +
                     X|V (D) ≥ volX|W (D) > 0. Since A1 , · · · , An−κν (D) are sufficiently ample,
we also have V 6⊆ B− (D).                                                                        
     We prove some notable properties of positive volume subvariety.
                 OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                             11

Lemma 2.23. If D and D ′ are pseudoeffective divisors on a variety X such that D ≡ D ′ , then
they have the same positive volume subvarieties.
Proof. Note first that B− (D) = B− (D ′ ). The statement then follows from the fact that
vol+                                                                          ′
   X|V (D) depends only on the numerical class [D] for any V 6⊆ B− (D) = B− (D ).     

Proposition 2.24. Let V ⊆ X be a positive volume subvariety of a pseudoeffective divisor D
on a variety X. If f : Y → X is a V -birational morphism, then Ve is also a positive volume
subvariety of f ∗ D.

Proof. The birational transform Ve ⊆ Y of V has dimension dim Ve = dim V = κν (D) = κν (f ∗ D).
If Ve ⊆ B− (f ∗ (D)), then V = f (Ve ) ⊆ f (B− (f ∗ (D)) = B− (D). Thus Ve 6⊆ B− (f ∗ (D)). It is
enough to show that vol+ e (f ∗ D) > 0. Since V 6⊆ B− (D) by definition, for any ample divisor
                          Y |V
A on X, we have V 6⊆ B+ (D + A). We can also check that Ve 6⊆ B+ (f ∗ D + f ∗ A) using [BBP,
Proposition 2.3]. Note that there is an effective divisor E on Y such that f ∗ A − E is ample.
Thus we have
                         vol+ e (f ∗ D) = lim volY |Ve (f ∗ D + ε(f ∗ A − E)).
                            Y |V             ε→0+

                       (f ∗ D + ε(f ∗ A − E)) − vol
The difference | volY |Ve                        Y |Ve
                                                       (f ∗ D + εf ∗ A)| can be arbitrarily small when
ε > 0 is sufficiently small. On the other hand, by [ELMNP2, Lemma 2.4], we have
                vol+                                              ∗      ∗
                   X|V (D) = lim volX|V (D + εA) = lim volY |Ve (f D + εf A).
                                 ε→0+                    ε→0+

Since vol+                               +    ∗
         X|V (D) > 0, it follows that vol e (f D) > 0.                                              
                                             Y |V

  It is known that D|V is pseudoeffective for any subvariety V ⊆ X such that V 6⊆ B− (D).
Thus κ(D|V ) ≥ 0. Furthermore, we have the following.
Theorem 2.25. Let V be a positive volume subvariety of a pseudoeffective divisor D on a variety
X. Then volV (D|V ) > 0. In particular, D|V is big on V and κν (D) = κν (D|V ) = dim V .
Proof. By taking a suitable V -birational model and considering Proposition 2.24, we may assume
that V is smooth. We can take a sequence of ample divisors Ai such that D + Ai are Q-divisors
and Ai → 0 as i → ∞. Since V ⊆ X is a positive volume subvariety of D, there exists a constant
C0 such that for any large integer k > 0, we have
                                        h0 (X|V, m(D + Ak ))
                                   lim sup                   > C0
                                    m→∞        mκν (D)
where m is taken over all positive integers such that m(D + Ak ) is a Z-divisor. Note that
h0 (X|V, m(D + Ak )) ≤ h0 (V, m(D|V + Ak |V )). Thus for any large integer k > 0, we also have
                                       h0 (V, m(D|V + Ak |V ))
                                 lim sup                       > C0 .
                                   m→∞         mκν (D)
By the continuity of the volume function volV , we obtain volV (D|V ) > 0. Thus D|V is big on
V.                                                                                          


                     3. Okounkov body of a pseudoeffective divisor
  In this section, we introduce and study the valuative Okounkov body ∆val
                                                                       Y• (D) and the limiting
                    lim
Okounkov body ∆Y• (D) associated to a divisor D on a variety X.
12           SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

3.1. Okounkov body ∆Y• (D).
   Let X be a (possibly singular) projective variety of dimension n, and D be an R-divisor on X
such that the R-linear system |D|R is nonempty. In Introduction, we have defined the function
νY• : |D|R → Rn for a given admissible flag Y• on X. We also recall that the Okounkov body
∆Y• (D) of a divisor D with respect to an admissible flag Y• is defined as
            ∆Y• (D) := the closure of the convex hull of the image νY• (|D|R ) in Rn≥0 .
We remark that such construction of ∆Y• (D) is equivalent to the one given in [LM] where
∆Y• (D) is defined as the natural extension of the Okounkov body defined for Z-divisors using
the homogeneity and the continuity of the Okounkov bodies. See [LM] for details.
   In this Subsection, we also recall from [LM] the construction of the Okounkov body of a
graded linear series W• associated to D.
   Let D be a Cartier Z-divisor on X such that H 0 (X, OX (D)) 6= 0, and fix an admissible flag
Y• on X. For a non-zero section s ∈ H 0 (X, OX (D)) \ {0}, we can find an effective divisor
D ′ = div(s) ∼ D. Thus we can also define the following function
                      νY• : H 0 (X, OX (D)) \ {0} → Zn≥0 , νY• (s) := νY• (D ′ ).
Recall that a graded linear series W• (D) = {Wm := Wm (D)}m≥0 associated to D consists of
subspaces Wm ⊆ H 0 (X, OX (mD)) with W0 = C satisfying Wm · Wl ⊆ Wm+l for all m, l ≥ 0.
The volume of W• is defined as
                                                      dim Wm
                                    volX (W• ) := lim
                                                   m→∞ mn /n!

Note that the above limit exists by [LM, Theorem 2.13 and Remark 2.14]. We define the graded
semigroup of W• as
              Γ(W• ) := {(ν(s), m) | Wm 6= {0} and s ∈ Wm \ {0} } ⊆ Zn≥0 × Z≥0 .
Definition 3.1. Let W• be a graded linear series associated to a Cartier Z-divisor D on a variety
X of dimension n. We can associate the convex body ∆Y• (W• ) called the Okounkov body of a
graded linear series W• with respect to an admissible flag Y• on X as follows:
                    ∆Y• (W• ) := Σ(Γ(W• )) ∩ (Rn≥0 × {1}) ⊆ Rn≥0 × {1} = Rn≥0
where Σ(Γ(W• )) denotes the closure of the convex cone in Rn≥0 × R≥0 spanned by Γ(W• ).
  Note also that ∆Y• (W• ) is a convex subset in Rn , that is, ∆Y• (W• ) ⊆ Rn≥0 . If W• is a complete
graded linear series (that is, Wm = H 0 (X, O(mD)) for each m) of a Cartier Z-divisor D, then
we write W• = W• (D) and we have
                                      ∆Y• (D) = ∆Y• (W• (D)).
   By construction, the Okounkov body ∆Y• (D) of a divisor D or the Okounkov body ∆Y• (W• )
of a graded linear series W• depends on the choice of the admissible flag Y• .
Remark 3.2. Let Y• be an admissible flag on a variety X of dimension n. For each integer k
such that 0 ≤ k ≤ n, we can define the k-th partial flag Yk• of Y• as
                                Yk• : Yk ⊇ Yk+1 ⊇ · · · ⊇ Yn = {x}.
Then Yk• is an admissible flag on a projective variety Yk of dimension n − k. If D is an effective
divisor on X such that ordYk (D) = 0, then we obtain an effective divisor D|Yk on Yk . As above,
we can define
                                                                     n−k
                           νYk• (D) := (νk+1 (D), · · · , νn (D)) ∈ R≥0  .
                 OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                           13

                                                           n−k
If ordYk (D) > 0, then we set νYk• (D) = (0, · · · , 0) ∈ R≥0  . The k-th partial Okounkov body of a
divisor D on X with respect to the k-th partial flag Yk• is defined as
                                                                               n−k
                ∆Yk• (D) := the closure of the convex hull of νYk• (|D|R ) in R≥0  .
These partial flags and partial Okounkov bodies will be useful in the next subsections.
  Under the following conditions, the Okounkov body ∆Y• (W• ) behaves well.
Definition 3.3 ([LM, Definitions 2.5 and 2.9]).
(1) We say that a graded linear series W• satisfies Condition (B) if Wm 6= 0 for all m ≫ 0, and
 for all sufficiently large m, the rational map ϕm : X 99K P(Wm ) defined by |Wm | is birational
 onto its image.
(2) We say that a graded linear series W• satisfies Condition (C) if
    i. for every m ≫ 0, there exists an effective divisor Fm such that the divisor Am := mD−Fm
       is ample, and
   ii. for all sufficiently large p, we have
                         H 0 (X, OX (pAm )) ⊆ Wpm ⊆ H 0 (X, OX (pmD)).
  If W• is complete, that is, Wm = H 0 (X, OX (mD)) for all m ≥ 0 and D is big, then it
automatically satisfies Condition (C).
Theorem 3.4 ([LM, Theorem 2.13]). Suppose that a graded linear series W• satisfies Condition
(B) or Condition (C). Then for any admissible flag Y• (with a general choice of the point
Yn = {x} when W• only satisfies Condition (B)), we have
                                                                         1
             dim ∆Y• (W• ) = dim X(= n) and        volRn (∆Y• (W• )) =      · volX (W• ).
                                                                         n!
  Note that [LM, Theorem 2.13] also requires Condition (A) ([LM, Definition 2.4]), but it is
automatically satisfied in our situation since we always assume that our variety X is projective.
The smoothness assumption on X is not necessary for this theorem.
Remark 3.5. It is well known by [LM, Proposition 4.1] that for a fixed admissible flag Y• on
X, if D is a big divisor on X, then ∆Y• (D) depends only on the numerical class of D. If D is
not big, then it is no longer true. See Remark 3.13.
  We will use the following result, which generalizes [LM, Theorem 4.26]. Many of our subse-
quent results will rely on this nontrivial theorem. The detailed proof is given in [CPW].
Theorem 3.6 ([CPW, Theorem 1.1]). Let D be a big divisor on a smooth projective variety X
of dimension n. Suppose that Y• is an admissible flag on X such that Yk 6⊆ B+ (D). Then we
have
                           ∆Y• (D) ∩ ({0}k × R≥0
                                               n−k
                                                   ) = ∆Yk• (D).
Remark 3.7. If Yk ⊆ B+ (D), then the conclusion of Theorem 3.6 does not hold in general. For
example, following [ELMNP2, Example 5.10], we consider the blow-up π : X → P3 of P3 at a
line with exceptional divisor E. Let D ∈ |π ∗ OP3 (1)| be an effective divisor, and C be a smooth
curve of type (2, 1) in E ≃ P1 × P1 . Note that D is nef and big and C ⊆ B+ (D) = E. Fix an
admissible flag
                          Y• : X = Y0 ⊇ E = Y1 ⊇ C = Y2 ⊇ Y3 = {x}
on X where x is any point on C. We may regard both ∆Y• (D) ∩ ({0}2 × R1≥0 ) and ∆Y2• (D) as
convex subsets in R1≥0 . We then have
     ∆Y• (D) ∩ ({0}2 × R1≥0 ) = {x ∈ R1≥0 | 0 ≤ x ≤ 2} ) {x ∈ R1≥0 | 0 ≤ x ≤ 1} = ∆Y2• (D).
14            SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

3.2. Valuative Okounkov body ∆val   Y• (D).
   Throughout the subsection, X is a smooth projective variety of dimension n.
Definition 3.8. Let D be a divisor on a variety X of dimension n such that |D|R 6= ∅. The
valuative Okounkov body ∆val
                         Y• (D) associated to D with respect to an admissible flag Y• on X is
defined as
                                ∆val                    n
                                  Y• (D) := ∆Y• (D) ⊆ R≥0 .
For a divisor D with |D|R = ∅, we define ∆val
                                          Y• (D) := ∅.

Remark 3.9. Note that the constructions for the valuative Okounkov body ∆val Y• (D) and for the
usual Okounkov body ∆Y• (D) are the same. However, for a non-big divisor D, we will use the
notation ∆val                                                                           val
          Y• (D) in order to emphasize special properties of valuative Okounkov body ∆Y• (D).

  Clearly, the valuative Okounkov body ∆val Y• (D) of a divisor D depends on the choice of the
admissible flag Y• . However, we will see below that if κ(D) ≥ 0 and Y• contains a Nakayama
subvariety U = Yn−κ(D) of D, then the valuative Okounkov body ∆val  Y• (D) depends only on the
choice of a Nakayama subvariety of D and the (n − κ(D))-th partial flag Yn−κ(D)• on U .
  Let D be a divisor on X with κ(D) ≥ 0, and fix an admissible flag Y• on X containing a
Nakayama subvariety U = Yn−κ(D) of D. As in Remark 3.2, we can also consider νYn−κ(D)• (D ′ ) ∈
 κ(D)
R≥0     for any D ′ ∈ |D|R .
Proposition 3.10. Under the notations as above, for any D ′ ∈ |D|R , we have
                               νY• (D ′ ) = (0, . . . , 0, νYn−κ(D)• (D ′ )).
                                             | {z }
                                              n−κ(D)

In particular, ∆val         n−κ(D) × Rκ(D) , and so we can regard ∆val (D) as a subset of Rκ(D) .
                Y• (D) ⊆ {0}          ≥0                           Y•                      ≥0

Proof. By Lemma 2.14, U = Yn−κ(D) is also a Nakayama subvariety of D ′ . By the definition of
Nakayama subvariety, we have
                                  H 0 (X, IU ⊗ OX (⌊mD ′ ⌋)) = 0
for all m ≥ 0. This implies that U 6⊆ Supp(D ′ ). Since Yk ⊇ U for 1 ≤ k ≤ n − κ(D), it follows
that Yk 6⊆ Supp(D ′ ). Thus we obtain νk (D ′ ) = 0 for 1 ≤ k ≤ n − κ(D), and the assertions
immediately follow.                                                                          
   Now let D be a Z-divisor on X such that κ(D) ≥ 0, and fix a Nakayama subvariety U ⊆ X of
D. By Theorem 2.16, D|U is a big divisor on U . Consider the restricted complete graded linear
series W• (D|U ) of a Z-divisor D along U which is given by
                                   Wm (D|U ) := H 0 (X|U, mD)
for each m ≥ 0. Recall that H 0 (X|U, mD) is the image of the natural restriction map ϕU :
H 0 (X, OX (mD)) → H 0 (U, OU (mD|U )). Note that W• (D|U ) is a graded linear subseries of
W• (D|U ) on U .
Remark 3.11. Let Y• be an admissible flag containing a Nakayama subvariety U of a Z-divisor
D on X such that κ(D) ≥ 0. Then the valuative Okounkov body ∆val       Y• (D) can be constructed
alternatively as follows. Consider the (n − κ(D))-th partial flag Yn−κ(D)• on U . Since W• (D|U )
is a graded linear subseries associated to D|U on U , we can define the Okounkov body
                                                                    κ(D)
                                  ∆Yn−κ(D)• (W• (D|U )) ⊆ R≥0
as in Definition 3.1. By regarding ∆val
                                    Y• (D) as a subset of R
                                                            κ(D) (Proposition 3.10), we have


                                ∆val
                                 Y• (D) = ∆Yn−κ(D)• (W• (D|U )).
                  OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                                   15

Thus ∆Yn−κ(D)• (W• (D|U )) gives an alternative construction of ∆val
                                                                 Y• (D).

  The following is the main property of ∆val
                                         Y• (D).

Theorem 3.12. Let D be a divisor such that κ(D) ≥ 0 on a smooth projective variety X, and
fix an admissible flag Y• containing a Nakayama subvariety U of D such that Yn = {x} is a
general point. Then ∆val
                       Y• (D) ⊆ {0}
                                   n−κ(D) × Rκ(D) . Furthermore, we have


                                                                           1
                dim ∆val
                     Y• (D) = κ(D) and           volRκ(D) (∆val
                                                            Y• (D)) =          volX|U (D)
                                                                         κ(D)!
where ∆val
       Y• (D) is regarded as a convex subset of R
                                                  κ(D) .


Proof. The first part of the assertions is shown in Proposition 3.10. We now prove the second
part. We first consider the case where D is a Z-divisor. We can easily check that ∆val Y• (mD) =
 1 val
m ∆Y• (D) for any integer m > 0. Thus we may assume that the constant m0 in Remark 2.7
is equal to 1. In particular, h0 (X, OX (mD)) > 0 for any integer m > 0. By Remark 3.11, we
have ∆val
        Y• (D) = ∆Yn−κ(D)• (W• (D|U )). By the properties of a Nakayama subvariety, there exits
an integer m0 such that h0 (X, OX (mm0 D)) = dim Wmm0 ∼ mκ(D) for all m ≫ 0 (cf. Remark
2.7) and dim U = κ(D). Furthermore, Yn = {x} is assumed to be general. By [LM, Remark
2.8], the assertions follow from Theorem 3.4.
   Now, we assume that D is a Q-divisor. There exists a sufficiently divisible integer m > 0 such
                                                           1 val
that mD is a Z-divisor. We can also see that ∆val Y• (D) = m ∆Y• (mD). Thus the assertions for
Q-divisors follow from the Z-divisor case.
   Finally, we treat the case where D is an R-divisor. Consider a sequence of Q-divisors Dm :=
⌊mD⌋
  m    converging to D as m → ∞. Then Em := D − Dm = mD−⌊mD⌋          m      forms a sequence of
effective R-divisors converging to 0 as m → ∞. We have
        ∆val         val         val
         Y• (Dm ) + ∆Y• (Em ) ⊆ ∆Y• (D)          and     lim ∆val
                                                              Y• (Em ) = {the origin of R
                                                                                          κ(D)
                                                                                               }
                                                        m→∞

                          κ(D)
as convex subsets in R≥0 . Take any D ′ ∈ |D|R . For any sufficiently small number ε > 0, by
                                      ′ ∈ |D | := {D ′ | D           ′
applying Lemma 2.11, we can find Dm         m Q       m    m ∼Q Dm ≥ 0} for a sufficiently
large and divisible integer m > 0 such that
                                          |νi − νi′ | < ε for all i
where νY• (D ′ ) = (ν1 , · · · , νn ) and νY• (Dm′ ) = (ν ′ , · · · , ν ′ ). Observe that if m | m′ , then D ≤
                                                            1          n                                    m
Dm′ . Since m > 0 is sufficiently large, Dm′ − Dm = Em − Em′ is arbitrarily small. Thus for a
sufficiently large and divisible integer m′ > 0 with m | m′ , we can also find Dm              ′ ∈ |D ′ | such
                                                                                                 ′      m Q
that
                                            |νi − νi′′ | < ε for all i
            ′ ) = (ν ′′ , · · · , ν ′′ ). Therefore, by considering sufficiently divisible integers m > 0,
where νY• (Dm ′     1              n
we may assume that
                                        lim ∆val         val
                                             Y• (Dm ) = ∆Y• (D).
                                       m→∞

On the other hand, by definition of the Iitaka dimension, we have κ(Dm ) = κ(D) for a sufficiently
large m > 0. By definition of the restricted volume, we have
                                    volX|U (D) = lim volX|U (Dm ).
                                                    m→∞

Note that U is a Nakayama subvariety of Dm for a sufficiently large m > 0. Thus the assertions
for R-divisors follow from the Q-divisor case.                                              
16            SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

Remark 3.13. It is natural to ask whether ∆valY• (D) is a numerical invariant of D or not. If D
                                             val
is a big divisor on X, then by Remark 3.5, ∆Y• (D) = ∆Y• (D) depends only on the numerical
class of D. However, in general, we may have κ(D) < κ(D ′ ) even if D ≡ D ′ (see [Le1, Example
6.1]). Thus by choosing an admissible flag Y• containing Nakayama subvarieties of D and D ′ ,
we obtain ∆val          val  ′
             Y• (D) 6= ∆Y• (D ).
Remark 3.14. If D is only effective up to R-linear equivalence, then Theorem 3.12 does not
hold in general. As in Remark 2.8, take two distinct points P, Q on P1 and an irrational number
a. Set D := a(P − Q). Then D ∼R 0 and ∆val                   1
                                            Y• (D) = {0 ∈ R }. However, we have κ(D) = −∞.
     On the other hand, we have the following.
Proposition 3.15. If two divisors D, D ′ satisfy D ∼R D ′ , then ∆val       val  ′
                                                                  Y• (D) = ∆Y• (D ) with respect
to any admissible flag Y• .
Proof. It is trivial by definition.                                                              
Remark 3.16. The converse of Proposition 3.15 is false even if D is big. Indeed, for two big
divisors D, D ′ such that D ≡ D ′ but D 6∼R D ′ , we have ∆Y• (D) = ∆Y• (D ′ ) for any admissible
flag Y• (see [LM, Proposition 4.1]). Moreover, we can also construct such non-big effective
divisors. For example, consider a minimal ruled surface f : S → C over a smooth projective
curve of genus g ≥ 1. Let F1 := f ∗ P and F2 := f ∗ Q where P and Q are two distinct points on
C. Note that F1 6∼R F2 . However, we claim that ∆val            val
                                                    Y• (F1 ) = ∆Y• (F2 ) for any admissible flag Y•
on S. To see this, observe that a curve Y1 is either a fiber of f or dominating C via f . In the
first case, we have
                    ∆val         val                       2
                     Y• (F1 ) = ∆Y• (F2 ) = {(x1 , x2 ) ∈ R | 0 ≤ x1 ≤ 1, x2 = 0}.
In the second case, note that Y1 is a Nakayama subvariety of both F1 and F2 . Furthermore, we
have
                          volS|Y1 (F1 ) = Y1 · F1 = Y1 · F2 = volS|Y1 (F2 ),
and hence, the claim follows.
3.3. Limiting Okounkov body ∆lim   Y• (D).
   Throughout the subsection, X is a smooth projective variety of dimension n.
Definition 3.17. Let D be a pseudoeffective divisor D on a variety X of dimension n. The
limiting Okounkov body ∆lim
                         Y• (D) of D with respect to an admissible flag Y• is defined as
                                                   \
                  ∆lim
                    Y• (D) := lim ∆Y• (D + εA) =      ∆Y• (D + εA) ⊆ Rn≥0
                                 ε→0+
                                                        ε>0

where A is an ample divisor. If D is not a pseudoeffective divisor, then we define ∆lim
                                                                                    Y• (D) := ∅.
Remark 3.18. It is easy to see that the definition of the limiting Okounkov body does not
depend on the choice of an ample divisor A. If D is big, then ∆lim
                                                               Y• (D) coincides with ∆Y• (D)
for any admissible flag Y• on X.
   We are mainly interested in the limiting Okounkov bodies ∆lim  Y• (D) when Y• contains contains
                                                                lim
a positive volume subvariety V of D. To investigate such ∆Y• (D) in detail, we introduce the
following alternative construction, which also gives the same convex body as ∆lim  Y• (D) after all
(see Proposition 3.21). This construction is often more convenient to study the asymptotic
invariants of pseudoeffective divisors. To begin with, we first consider a pseudoeffective Cartier
Z-divisor D on a variety X of dimension n. Let V ⊆ X be a v-dimensional irreducible subvariety
of D. We will mainly concern the case that V is a positive volume subvariety of D. Fix an
admissible flag V• on V :
                               V• : V = V0 ⊇ V1 ⊇ · · · ⊇ Vv = {x}.
                OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                         17

Let A be an ample Cartier Z-divisor on X. For each integer k ≥ 1, consider the restricted
graded linear series W•k := W• (kD + A|V ) of kD + A along V given by Wm (kD + A|V ) =
h0 (X|V, m(kD + A)) for m ≥ 0. We define the restricted limiting Okounkov body of a Cartier
divisor D along V with respect to V• as
                                              1
                              ∆lim
                               V• (D) := lim    ∆V• (W•k ) ⊆ Rv≥0 .
                                          k→∞ k

One can easily check that ∆lim
                            V• (D) = limε→0+ ∆V• (D + εA). We can extend this definition for
any pseudoeffective R-divisor D.
Definition 3.19. Let D be a pseudoeffective divisor on a variety X, and V ⊆ X be a v-
dimensional irreducible subvariety. The restricted limiting Okounkov body ∆lim
                                                                           V• (D) of D along
V with respect to V• as
                            ∆lim
                              V• (D) := lim ∆V• (D + εA) ⊆ R≥0
                                                                v
                                         ε→0+

for some ample divisor A on X. If D is not pseudoeffective, then we define ∆lim
                                                                            V• (D) := ∅.

  This definition depends on the choice of V and the admissible flag V• on it, but it is indepen-
dent of the choice of A. By definition, ∆lim                                  v
                                         V• (D) is a closed convex subset of R . By the inclusion
Rv = {0}n−v × Rv ֒→ Rn , we often treat ∆lim                        n
                                             V• (D) as a subset of R .
  The following is the main property of the restricted limiting Okounkov body ∆lim V• (D).

Theorem 3.20. Let D be a pseudoeffective divisor on a variety X, and V be a v-dimensional
irreducible subvariety of X. Fix an admissible flag V• on V . Suppose that V 6⊆ B− (D) and
vol+
   X|V (D) > 0. Then we have

                                                                 1
                   dim ∆lim
                        V• (D) = v and      volRv (∆lim
                                                    V• (D)) =       vol+
                                                                       X|V (D).
                                                                 v!
Proof. We first consider the case where D is a Z-divisor. Let A be an ample Z-divisor on
X. Since V 6⊆ B− (D) by definition, it follows that V 6⊆ B+ (kD + A) for any k ≥ 1. Let
W•k := W• (kD + A|V ) be the restricted graded series of kD + A along V for k ≥ 1. Then W•k
satisfies Condition (C) by [LM, Lemma 2.16]. It follows from Theorem 3.4 that for each k ≥ 1,
we have
                                                                1
             dim ∆V• (W•k ) = dim V = v and volRv (∆V• (W•k )) = volX|V (kD + A).
                                                                v!
The first equality implies dim ∆lim
                                V• (D) = v, and the second equality yields the following compu-
tation:                                                            
                         volRv (∆lim
                                 V• (D)) = volRv       lim 1 ∆V• (W•k )
                                                      k→∞ k
                                           = lim k1v volRv (∆V• (W•k ))
                                             k→∞                        
                                           = lim v!1 volX|V D + k1 A
                                             k→∞
                                           = v!1 vol+
                                                    X|V (D).
Thus we have shown the assertion for Z-divisors. When D is a Q-divisor, there is a sufficiently
divisible integer m > 0 such that mD is a Z-divisor. It is easy to check that ∆lim      V• (D) =
 1 lim
  ∆
m V•   (mD).   Thus the  assertions for Q-divisors follow from the  Z-divisor case.
  Now, we assume that D is an R-divisor. Then there exists a sequence of ample divisors Ai on
X such that D + Ai are Q-divisor and limi→∞ Ai = 0. Note that V 6⊆ B+ (D + Ai ). Thus V 6⊆
B− (D + Ai ) and vol+                                              lim              lim
                    X|V (D + Ai ) = volX|V (D + Ai ) > 0. Since ∆V• (D) = limi→∞ ∆V• (D + Ai ),
the assertion for R-divisors follow from the Q-divisor case.                                   
18           SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

Proposition 3.21. Let D be a pseudoeffective divisor on a variety X of dimension n, and fix
an admissible flag Y• containing a positive volume subvariety V = Yn−κν (D) of D. Consider the
(n − κν (D))-th partial flag V• := Yn−κν (D)• . Then
                                        ∆lim       lim
                                         Y• (D) = ∆V• (D).

In particular, ∆lim
                Y• (D) depends on the (n − κν (D))-th partial flag V• .

Proof. We will denote κν := κν (D). If κν = n, then there is nothing to prove. Therefore, we
assume that 0 ≤ κν < n. Fix an ample divisor A on X. By definition, the positive volume
subvariety Yn−κν = V is not contained in B− (D). Since Yi ⊇ Yn−κν for 0 ≤ i ≤ n − κν , we
have Yi 6⊆ B+ (D + εA) for any ε > 0. Thus Theorem 3.6 implies that if 0 ≤ i ≤ n − κν , then
∆Y• (D + εA) ∩ ({0}i × Rn−i ) = ∆Yi• (D + εA). By taking the limit ε → 0, for 0 ≤ i ≤ n − κν ,
we obtain
(*)                  ∆lim          i
                      Y• (D) ∩ ({0} × R
                                        n−i
                                            ) = lim ∆Yi• (D + εA) =: ∆lim
                                                                      Yi• (D).
                                                ε→0+

Since Yn−κν = V , it is enough to check ∆lim
                                         Y• (D) ⊆ {0}
                                                     n−κν × Rκν to prove ∆lim (D) = ∆lim (D).
                                                                          Y•         V•
Suppose that this does not hold, that is,
                                  ∆lim
                                   Y• (D) 6⊆ {0}
                                                n−κν
                                                     × Rκν ⊆ Rn .
We will derive a contradiction to [Le1, Theorem 1.1 (2)], which says that κν is the maximum
of integers k ≥ 0 such that there exists a constant C > 0 with volX (D + εA) ≥ Cεn−k for all
ε > 0. By Theorem 3.20, l := dim ∆lim                   lim
                                    Y• (D) > κν = dim ∆V• (D) and we have

                             ∆lim       i1  i2
                              Y• (D) ⊆ R × R × · · · × R
                                                         in−κν
                                                               × Rκν
                     Pn−κν
where ij = 0 or 1,     j=1   ij = l − κν and R0 := {0}. For simplicity, we may just assume
                                 ∆lim
                                  Y• (D) ⊆ R
                                             l−κν
                                                  × {0}n−l × Rκν .
Now consider a sufficiently positive ample divisor A′ so that ∆Y• (εA′ ) contains
                                (                            n
                                                                      )
                                                             X
                         △ε := (x1 , · · · , xn ) xi ≥ 0 and   xi ≤ ε
                                                             i=1

for all ε > 0. We may assume that A is sufficiently ample so that A′′ := A − A′ is also ample.
By the convexity of ∆Y• (D) (cf. [LM, Proof of Corollary 4.12]), we have
      ∆lim            lim             ′               ′′          ′
       Y• (D) + △ε ⊆ ∆Y• (D) + ∆Y• (εA ) ⊆ ∆Y• (D + εA ) + ∆Y• (εA ) ⊆ ∆Y• (D + εA).

Since dim ∆lim
           Y• (D) = l, it follows that
                                                           1
              C · volRl ∆lim
                         Y• (D) · ε
                                   n−l
                                       ≤ volRn ∆Y• (D + εA) =· volX (D + εA).
                                                          n!
for some constant C > 0 depending only on n and l. We get a contradiction to [Le1, Theorem
1.1 (2)] since l > κν .                                                                  
Corollary 3.22. Let D be a pseudoeffective divisor on a smooth projective variety X. Fix a
positive volume subvariety V ⊆ X of D and consider an admissible flag Y• on X containing V .
Then ∆lim            n−κν (D) × Rκν (D) . Furthermore, we have
         Y• (D) ⊆ {0}            ≥0
                                                                         1
             dim ∆lim
                  Y• (D) = κν (D) and        volRκν (D) (∆lim
                                                          Y• (D)) =           vol+
                                                                                 X|V (D)
                                                                      κν (D)!
where ∆lim
       Y• (D) is regarded as a convex subset of R
                                                  κν (D) .

Proof. Immediate by Theorem 3.20 and Proposition 3.21.                                       
                OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                          19

Remark 3.23. We do not need to assume the generality of Yn = {x} as we did for the valuative
Okounkov body in Theorem 3.12.
Remark 3.24. Boucksom also studies the limiting Okounkov body (the numerical Okounkov
body in his terminology) of a pseudoeffective divisor with respect to any admissible flag in [B,
4.1.3]. He defines the limiting Okounkov body as a fiber of the global Okounkov body (see [LM,
Theorem B]) over a given pseudoeffective divisor class. He proves that dim ∆lim   Y• (D) ≤ κν (D)
for any admissible flag Y• ([B, Lemma 4.8]) and the inequality can be strict ([B, Example 4.14]).
Furthermore, he also shows that there exists an admissible flag Y• such that dim ∆lim    Y• (D) =
κν (D) when D is nef ([B, Proposition 4.9]). Our result Corollary 3.22 generalizes his result.
  Using Corollary 3.22, we can give a new characterization of numerical Iitaka dimension.
Corollary 3.25. Let D be a pseudoeffective divisor on a smooth projective variety X. Then we
have
              κν (D) = max{dim ∆lim
                                  Y• (D) | Y• is an admissible flag on X }.

Proof. By [B, Lemma 4.8], we know that dim ∆lim    Y• (D) ≤ κν (D) for any admissible flag Y•
on X. If Y• contains a positive volume subvariety, then it follows from Corollary 3.22 that
dim ∆lim
      Y• (D) = κν (D). Thus the assertion follows.                                         
  If D is a big divisor, then by [LM, Proposition 4.1] and [J, Theorem A] it is known that
∆Y• (D) = ∆Y• (D ′ ) for all admissible flags Y• on X if and only if D ≡ D ′ . Remark 3.13 implies
that the statement is false in general in the pseudoeffective case for ∆valY• (D). We prove next
       lim
that ∆Y• (D) is an appropriate generalization of ∆Y• (D) which makes the statement true.
  For a pseudoeffective divisor D, we define the following set of divisors
                                                                                   
                lim                 there exists an admissible flag Y• with Y1 = E
           div(∆ (D)) := E                                                            .
                                    such that∆lim
                                                Y• (D)x1 =0 = ∅

Lemma 3.26. The divisors in div(∆lim (D)) are precisely the divisorial components of B− (D)
and the set div(∆lim (D)) is finite.
Proof. Let Y• be an admissible flag on X such that Y1 = E. By the definition of the Okounkov
body, it is easy to see that for any ample divisor A and ε > 0,
                   ordE (||D + εA||) = inf {x1 |(x1 , · · · , xn ) ∈ ∆Y• (D + εA) } .
If we let ε → 0, then we have
                                          n                                 o
                        ordE (||D||) = inf x1 (x1 , · · · , xn ) ∈ ∆lim
                                                                    Y•  (D)   .
By Theorem 2.2, ordE (||D||) > 0 if and only if E ⊆ B− (D). Thus we obtain the desired
statement. The set div(∆lim (D)) is finite by [N, Corollary 1.11].                  
  We now prove a generalization of Jow’s theorem for the limiting Okounkov bodies.
Theorem 3.27. Let D and D ′ be pseudoeffective divisors on X. Then the following are equiv-
alent:
    (1) D ≡ D ′
    (2) ∆lim       lim  ′
         Y• (D) = ∆Y• (D ) with respect to any admissible flags Y• on X.

Proof. The equivalence (1) ⇔ (2) is known for big divisors by [LM, Proposition 4.1] and [J,
Theorem A]. Thus we assume that D, D ′ are not big. The implication (1)⇒(2) follows from the
big case: since ∆Y• (D + εA) = ∆Y• (D ′ + εA) for any ample divisor A and any ε > 0, we have
                 ∆lim                                   ′         lim  ′
                  Y• (D) = lim ∆Y• (D + εA) = lim ∆Y• (D + εA) = ∆Y• (D ).
                             ε→0                    ε→0
20               SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

To prove (1)⇐(2), we use the argument used to prove the big case by Jow in [J]. Let E1 , · · · , El
be the divisorial components of B− (D) and A an ample divisor on X. For any sufficiently
general admissible flag Y• on X such that Yn−1 6⊆ B− (D), we have Yn−1 6⊆ B+ (D + A) for any
ample divisor A. We see that
                  volR1 (∆ lim
                         Y• (D)x1 =···=xn−1 =0)
             = volR1         lim ∆Y• (D + εA)
                             ε→0+                      x1 =···=xn−1 =0
                                                                   
             = volR1         lim ∆Y• (D + εA)x1 =···=xn−1 =0
                             ε→0+
             =     lim volR1 (∆Y• (D + εA)x1 =···=xn−1 =0 )
                  ε→0+
             =     lim volX|Yn−1 (D + εA)              (by Theorem 3.6 or [J, Theorem 3.4 (b)])
                  ε→0+
                                  P
                                  l        P
             = Yn−1 · D −                          ordEi (||D||)       (by Lemma 3.28).
                                  i=1 p∈Yn−1 ∩Ei

As can be seen in the proof of Lemma 3.26, we can read off ordEi (||D||) from the limiting
Okounkov bodies ∆lim                                              ′              ′
                     Y•′ (D) with respect to admissible flags Y• such that Y1 = Ei . Therefore,
if ∆lim         lim   ′                                                                    ′
     Y• (D) = ∆Y• (D ) for any admissible flags Y• on X, then Yn−1 · D = Yn−1 · D . Let ρ :=
dim N1 (X)R . As in [J, Proof of Theorem A], we can choose general admissible flag Y•1 , · · · , Y•ρ
consisting of subvarieties that are transversal complete intersections of very ample divisors such
        1 ,··· ,Y ρ
that Yn−1         n−1 form a basis of N1 (X)R . Since we can read off the intersection numbers
Yn−1 · D = Yn−1 · D ′ from the limiting Okounkov bodies ∆lim
   i          i
                                                             Y•i
                                                                 (D) = ∆lim
                                                                          Y•i
                                                                              (D ′ ) for 1 ≤ i ≤ ρ, we
can conclude that D ≡ D ′ .                                                                          
     It remains to prove the following lemma that is used in the proof above.
Lemma 3.28 (cf. [J, Corollary 3.3]). Let Y• be a sufficiently general admissible flag on X.
For a pseudoeffective divisor D on X, let E1 , E2 , · · · , El be the divisorial components of B− (D).
Then we have
                                                                     Xl     X
           +
        volX|Yn−1 (D) = lim volX|Yn−1 (D + εA) = Yn−1 · D −                        ordEi (||D||).
                              ε→0+
                                                                               i=1 p∈Yn−1 ∩Ei

Proof. Suppose first that D is big. Since Yn−1 is very general, we have D ∈ BigYn−1 (X). Thus
vol+
   X|Yn−1 (D) = volX|Yn−1 (D) and the statement is nothing but [J, Corollary 3.3].
   Now let D be a pseudoeffective divisor. Applying the statement for the case of big divisors
to volX|Yn−1 (D + εA), we obtain
            vol+
               X|Yn−1 (D) =         lim volX|Yn−1 (D + εA)
                                    ε→0+                                                               !
                                                                     P
                                                                     l       P
                              =     lim    Yn−1 · (D + εA) −                          ordEi (||D + εA||)
                                    ε→0+                             i=1 p∈Yn−1 ∩Ei
                                                   P
                                                   l      P
                              = Yn−1 · D −                          ordEi (||D||).
                                                   i=1 p∈Yn−1 ∩Ei

                                                                                                           
Remark 3.29. Fulger pointed out to us that in the equation of Lemma 3.28 we actually have
                                      l
                                      X        X
                                                       ordEi (||D||) = Yn−1 · N
                                      i=1 p∈Yn−1 ∩Ei

where N is the negative part of the divisorial Zariski decomposition of D.
                 OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                          21

Remark 3.30. In Theorem 3.27, it is tempting to expect that D ≡ D ′ if and only if ∆limY• (D) =
  lim   ′
∆Y• (D ) for any admissible flags Y• containing positive volume subvarieties of both D and
D ′ . However, it is not true and we also need to consider the admissible flags not containing
the positive volume loci of the divisor. For example, consider a pseudoeffective divisor D 6≡ 0
on a variety X with κν (D) = 0. Let D ′ := 2D so that D 6≡ D ′ . Every point x ∈ X with
x 6∈ B− (D) = B− (D ′ ) is a positive volume subvariety of both D and D ′ . However, we see that
for any admissible flag Y• containing x, we have
                         ∆lim       lim  ′
                          Y• (D) = ∆Y• (D ) = {the origin of R
                                                               dim X
                                                                     }.
In fact, if we consider the admissible flags Y• containing positive volume subvarieties of both D
and D ′ in Theorem 3.27, then using Remark 3.29 we only obtain P ≡ P ′ where D = P + N and
D ′ = P ′ + N ′ are the divisorial Zariski decompositions.
Remark 3.31. Let D be a pseudoeffective divisor on X, and V ⊆ X be a smooth positive
volume subvariety of D. Fix an admissible flag Y• containing V . The (n − κν (D))-th par-
tial flag Y(n−κν (D))• induces an admissible flag V• on V . Recall that ∆lim          lim
                                                                         Y• (D) = ∆V• (D) =
limε→0+ ∆V• (D + εA) where A is an ample divisor on X. By Theorem 2.25, D|V is a big divisor
on V , and A|V is an ample divisor on V . By definition, ∆V• (D + εA) ⊆ ∆V• ((D + εA)|V ). Thus
we obtain
              ∆lim
               Y• (D) = lim ∆V• (D + εA) ⊆ lim ∆V• ((D + εA)|V ) = ∆V• (D).
                          ε→0+                  ε→0+

By Theorem 3.4, we have
                                                                      1
             dim ∆V• (D|V ) = κν (D) and volRκν (D) ∆V• (D|V ) =           volV (D|V ).
                                                                   κν (D)!
Let Y• be an admissible flag on X that is general enough so that it contains both a Nakayama
subvariety U and a positive volume subvariety V of a pseudoeffective divisor D. Then we have
the following inclusions:
(#)                              ∆val       lim
                                  Y• (D) ⊆ ∆Y• (D) ⊆ ∆V• (D|V ).

This confirms the inequalities volX|V (D) ≤ vol+ X|V (D) ≤ volV (D|V ) which we saw in Subsection
2.4. If D is big, then all the inclusions are equalities. However, we will see in the next section
that if D is not big, then they are strict in general.

                                          4. Examples
   In this section, we exhibit various examples and counterexamples related to our results. We
start with an example that shows that for some badly chosen admissible flags, Theorems 3.12
and 3.20 do not hold.
Example 4.1. Let π : S → P2 be a blow-up of P2 at two distinct points with exceptional
divisors E1 and E2 , and L ∈ |π ∗ OP2 (1)| be an effective divisor containing E1 but not containing
E2 . Consider a non-big effective divisor D := (L − E1 ) + E2 , and fix an admissible flag
                                        Y• : S ⊇ E2 ⊇ {x}
where x is a general point on E2 . Here we note that E2 is neither a Nakayama subvariety nor a
positive volume subvariety of D. We have
                 ∆val       lim                     2
                  Y• (D) = ∆Y• (D) = {(x1 , x2 ) ∈ R | 1 ≤ x1 ≤ 2 and x2 = 0}
whose Euclidean volume in the x1 -axis is 1. However, note that B− (D) = B+ (D + εA) = E2
for an ample divisor A and a small ε > 0. Thus we see that volX|E2 (D) = vol+
                                                                            X|E2 (D) = 0. We
also remark that ∆val       lim
                  Y• (D) = ∆Y• (D) is not in the x2 -axis as expected.
22             SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

     Examples 4.2 and 4.3 show that the inequalities in (#) of Remark 3.31 can be strict.
Example 4.2. In this example, we see that ∆val              lim
                                                 Y• (D) ( ∆Y• (D) even if κ(D) = κν (D). Let
S be a relatively minimal rational elliptic surface, and H a sufficiently positive ample divisor.
Take a general element V ∈ |H|. Fix an admissible flag
                                            Y• : S ⊇ V ⊇ {x}.
Note that κ(−KS ) = κν (−KS ) = 1, and V is both a Nakayama subvariety and a positive volume
subvariety of −KS . Thus we have volR1 (∆val                                    lim
                                         Y• (−KS )) = volS|V (−KS ) and volR1 (∆Y• (−KS )) =
vol+                                                                       +
   S|V (−KS ). However, we saw in Example 2.5 that volS|V (−KS ) < volS|V (−KS ). Thus
∆val          lim
 Y• (−KS ) ( ∆Y• (−KS ).
Example 4.3. Let S := P(E) where E is a rank two vector bundle on an elliptic curve C such
that it is a nontrivial extension of OC by OC , and H be the tautological divisor of P(E). Then
we can easily check that H is nef and κ(H) = 0 but κν (H) = 1. Let F be a general fiber of the
natural ruling π : S → C. Note that any general point in S is a Nakayama subvariety of H and
F is a positive volume subvariety of H. Thus take an admissible flag
                                            Y• : S ⊇ F ⊇ {x}
where x is a general point on a general fiber F . Then we can easily compute the following.
   (1) ∆val
         Y• (H) = {(0, 0)} and volS|{x} (H) = 1 by convention.
                                                              +
   (2) ∆lim
         Y• (H) = {(x1 , x2 ) | x1 = 0 and 0 ≤ x2 ≤ 1} and volS|F (H) = 1.
      (3) ∆Y• (H|F ) = ∆lim
                        Y• (H).
For ∆lim
       Y• (H), we see the convergence of limε→0+ ∆Y• (H + εA) for any ample divisor A in the
following picture.
                                      x2
                                                     ∆(H + εA)
                                   1+ε

                                       1

                                  ∆lim
                                   Y• (H)



                                                                 x1

  In fact, we use the following theorem to compute the limiting Okounkov body ∆lim
                                                                               Y• (D) of a
pseudoeffective divisor D on a surface (cf. [LM, Theorem 6.4])
Theorem 4.4. Let S be a smooth projective surface, and D be a pseudoeffective divisor on S.
Fix an admissible flag Y• : S ⊇ C ⊇ {x}. Let a := multC N where D = P + N is the Zariski
decomposition, and µ := sup{s ≥ 0 | D−sC is pseudoeffective}. Consider a divisor Dt := D−tC
for a ≤ t ≤ µ. Denote by Dt = Pt + Nt the Zariski decomposition. Let α(t) := ordx (Nt |C ) and
β(t) := α(t) + C.Pt . Then the limiting Okounkov body of D is given by
                 ∆lim                     2
                  Y• (D) = {(x1 , x2 ) ∈ R | a ≤ x1 ≤ µ and α(x1 ) ≤ x2 ≤ β(x2 )}.
Proof. Let D ε := D + εA for some ample divisor A and a positive number ε ≥ 0, and Dtε :=
D ε − tC. Denote by Dtε = Ptε + Ntε the Zariski decomposition. By Lemma 4.6 below, we see
that the Zariski decomposition Dt = Pt + Nt is given by
                          Pt = Pt0 = lim Ptε and Nt = Nt0 = lim Ntε .
                                      ε→0+                        ε→0+
                   OKOUNKOV BODIES ASSOCIATED TO PSEUDOEFFECTIVE DIVISORS                                     23

Since ∆lim
       Y• (D) = limε→0+ ∆Y• (D + εA), the assertion now follows from [LM, Theorem 6.4].                       
Remark 4.5. In Theorem 4.4, we do not need to assume that an admissible flag Y• contains a
positive volume subvariety.
  In the proof of Theorem 4.4, we use the following continuity property of the Zariski decom-
position on a surface.
Lemma 4.6. Let S be a smooth projective surface, D be a pseudoeffective divisor and A an
ample divisor on S. Consider the divisor D ε := D + εA for ε ≥ 0, and denote by D ε = P ε + N ε
the Zariski decomposition. Then P 0 = limε→0+ P ε and N 0 = limε→0+ N ε .
                                                                           P
Proof. It is sufficient to show that N 0 = limε→0+ N ε . We write N 0 = i a0i Di where Di are
prime divisors
             P  and a0i > 0. Since Supp(N ε ) = B− (D ε ) ⊆ B− (D 0 ) = Supp(N 0 ), we can also
write N ε = i aεi Di with aεi ≥ 0 for any ε ≥ 0. Note that aεi = ordDi (||D ε ||) for any ε ≥ 0 (see
[N, Remark III.1.17 (1)]). By definition, we have
                   lim ordDi (||D ε ||) = lim ordDi (||D + εA||) = ordDi (||D||) = a0i .
                  ε→0+                     ε→0+

Thus it follows that N 0 = limε→0+ N ε .                                                                      
  Examples 4.7 and 4.8 provide examples in higher dimensions. It is in general very difficult to
compute the Okounkov body in higher dimensions.
Example 4.7. Let D be a nef divisor on a smooth projective variety X, and fix an admissible
flag Y• containing a positive volume subvariety V = Yn−κν (D) of D. Then we have
                                                                                  1
           ∆lim
            Y• (D) = ∆Yn−κν (D) (D|V )       and     volRκν (D) (∆lim
                                                                  Y• (D)) =            (D|V )κν (D) .
                                                                               κν (D)!
Example 4.8. Let X be a smooth projective toric variety, and D be a T -invariant divisor on
X. Fix an admissible flag Y• consisting of T -invariant subvarieties. In toric geometry, one can
associate a rational polytope PD to D (see [F]). In [LM, Proposition 6.1], it is shown that
PD is nothing but the Okounkov body ∆Y• (D) up to translation when D is big. When D is
pseudoeffective, one can find an admissible flag Y• consisting of T -invariant subvarieties such
that
                                  PD = ∆val           lim
                                           Y• (D) = ∆Y• (D)
up to translation.

                                                References
[B]      S. Boucksom, Corps D’Okounkov (d’après Okounkov, Lazarsfeld- Mustaţă et Kaveh-Khovanskii),
         Séminaire Bourbaki, 65ème année, 2012-2013, no. 1059.
[BBP]    S. Boucksom, A. Broustet, and G. Pacienza, Uniruledness of stable base loci of adjoint linear systems
         via Mori Theory, Math. Z. 275 (2013), 499-507.
[CPW]    S. Choi, J. Park, and J. Won, Okounkov bodies associated to pseudoeffective divisors II, Taiwanese J.
         Math. 21 (2017), 602-620 (special issue for the proceedings of the conference “Algebraic Geometry in
         East Asia 2016”).
[DP]     L. Di Biagio, G. Pacienza, Restricted volumes of effective divisors, Bull. Soc. Math. France 144 (2016),
         299-337.
[E]      T. Eckl, Numerical analogues of the Kodaira dimension and the abundance conjecture, Manuscripta
         Math. 150 (2016), 337-356.
[ELMNP1] L. Ein, R. Lazarsfeld, M. Mustaţă, M. Nakamaye, and M. Popa, Asymptotic invariants of base loci,
         Ann. Inst. Fourier, 56 (2006), 1701-1734.
[ELMNP2] L. Ein, R. Lazarsfeld, M. Mustaţă, M. Nakamaye, and M. Popa, Restricted volumes and base loci of
         linear series, Amer. J. Math. 131 (2009), 607-651.
[F]      W. Fulton, Introduction to toric varieties, Ann. Math. Studies. 131, Princeton Univ. Press, Princeton,
         NJ (1993).
24              SUNG RAK CHOI, YOONSUK HYUN, JINHYUNG PARK, AND JOONYEONG WON

[G]          Y. Gongyo, On the minimal model theory for dlt pairs of numerical log Kodaira dimension zero, Math.
             Res. Lett. 18 (2011), 991-1000.
[J]          S.-Y. Jow, Okounkov bodies and restricted volumes along very general curves, Adv. Math. 223 (2010),
             1356-1371.
[KK]         K. Kaveh and A. G. Khovanskii, Newton convex bodies, semigroups of integral points, graded algebras
             and intersection theory, Ann. Math. (2) 176 (2012), 925-978.
[La]         R. Lazarsfeld,Positivity in algebraic geometry I & II, Ergeb. Math. Grenzgeb., 48 & 49 (2004),
             Springer-Verlag, Berlin.
[LM]         R. Lazarsfeld and M. Mustaţă, Convex bodies associated to linear series, Ann. Sci. Ec. Norm. Super.
             (4) 42 (2009), 783-835.
[Le1]        B. Lehmann, Comparing numerical dimensions, Algebra Number Theory. 7 (2013), 1065-1100.
[Le2]        B. Lehmann, On Eckl’s pesudo-effective reduction map, Trans. Amer. Math. Soc. 366 (2014), 1525-
             1549.
[N]          N. Nakayama, Zariski-decomposition and abundance, MSJ Memoirs 14. Mathematical Society of
             Japan, Tokyo, 2004.
[O1]         A. Okounkov, Brunn-Minkowski inequality for multiplicities, Invent. Math. 125 (1996) 405-411.
[O2]         A. Okounkov, Why would multiplicities be log-concave? in The Orbit Method in Geometry and Physics,
             Progr. Math. 213 (2003), Birkhuser Boston, Boston, MA, 329-347.

      Department of Mathematics, Yonsei University, Seoul, Korea
      E-mail address: sungrakc@yonsei.ac.kr

      Samsung Advanced Institute of Technology, Suwon, Korea
      E-mail address: yoonsuk.hyun@samsung.com

      School of Mathematics, Korea Institute for Advanced Study, Seoul, Korea
      E-mail address: parkjh13@kias.re.kr

      Center for Geometry and Physics, Institute for Basic Science, Pohang, Korea
      E-mail address: leonwon@ibs.re.kr
