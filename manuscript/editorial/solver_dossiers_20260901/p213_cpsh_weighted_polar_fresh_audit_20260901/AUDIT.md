# Independent exact-final audit: full CPsh weighted polar estimate

Date: 1 September 2026. Independent reviewer: /root/p213_general_propagation_fresh_audit. Auditee author: /root/p213_skeletal_hostile. Parent /root proposed the route and supplied prefreeze mathematical corrections; neither the parent nor the author is substituted for this independent reviewer.

This is a new exclusive audit sibling. The entire final note and source ledger were read and checked at the frozen identities below. All input artifacts, earlier audit reports, and live manuscript files remained unchanged. No git, production service, Rethlas submission, or textbook promotion was performed. This report does not attest a runtime model/effort identity or production acceptance merely from a requested configuration label.

## 1. Verdict

**Mathematical PASS for the stated full-CPsh weighted estimate, its locally approachable polar-helper consequence, and its analytic closed-subset consequence, at the exact frozen identities in Section 2.** No substantive mathematical gap was found in the new proof. The optional classification-free component-curvature consequence in Section 9 also follows. This is an independent mathematical verdict, not a formal proof certificate, novelty claim, production receipt, or solution of full P21.3.

This verdict concerns a genuinely new deduction, not an assertion that CLD 16.9.4 already states the full-CPsh result. The preceding approachable/component-curvature audit did not prove this estimate and is not used as its mathematical justification. The new proof is checked below through its actual energy, positivity, compact-test, weighted-cancellation and polar-limit arguments.

Three scope distinctions are essential:

| Accepted clause | Hypotheses retained |
|---|---|
| Fixed weighted inequality (1.2) | Boundaryless locally differentially separated CLD tropical n-space, n>=1; one smooth psh barrier with a positive closed sublevel K_delta compact in its ordinary domain; integer a>=4; every continuous factor in the full CPsh sheaf near K_delta; V smooth psh near that same compact and negative on U={rho<0}. |
| Polar integrability (1.3) and polar-set total-variation nullity | The local barrier condition; u_1,...,u_m in full CPsh, 0<=m<=n; the auxiliary possibly singular V is locally approachable by a direct decreasing smooth sequence and canonically locally integrable. The approachability hypothesis on V is not removed. |
| Analytic closed-subset nullity | Good, separated, strict in the stated CLD convention, boundaryless, pure n-dimensional Berkovich space, n>=1, over any complete non-Archimedean K including trivial valuation. The usual strict class is a sufficient smaller class. No normality, reducedness, perfectness or residue-characteristic-zero condition is introduced. |

The continuous factors need not possess a single smooth approximation sequence. Their use of the full uniform-closure sheaf is justified by the new argument, without proving that its hierarchy collapses. No discontinuous factor u_j, arbitrary-current polar theorem without potentials, scalar-current classification over arbitrary K, or general positive-bidegree Bedford–Taylor assertion is established by this packet.

## 2. Exact final inputs and method

The reviewed target is `../p213_cpsh_weighted_polar_research_20260901/`. All 299 lines of RESEARCH_NOTE.md and the complete SOURCE_LEDGER.md were read. The author validation was also read, but not counted as an independent verdict. A provisional reading was subsequently checked against these final frozen bytes; this verdict is bound to the final packet, not to an unfrozen draft.

| Artifact | Bytes | SHA256 |
|---|---:|---|
| RESEARCH_NOTE.md | 28152 | `2bdbb2c72135779323fea27c6d8c38ebd665c3eca21037017ff0442953433a5f` |
| SOURCE_LEDGER.md | 9954 | `6e33263a3415ac67fd4fc2d47baaac715e80a418c4ae5d8617edb3b3feb6b5c8` |
| MANIFEST.json | 3132 | `421b53dc7ed848a23ea64157907d6946d9eaca3719c12586bf60af849e7b4167` |
| SHA256SUMS | 1268 | `7b0aea1c780a4ef7016bd0440a212fdaf1e18d6d9be0a1fc369317d4be582e1a` |

The primary text is Chambert-Loir–Ducros, [*Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2](https://arxiv.org/abs/1204.6277v2), revision dated 25 July 2025. Its local full extraction `/private/tmp/CLD25.txt` has 2150944 bytes and SHA256 `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e`. The PDF is pinned as provenance; this task does not claim a new visual PDF audit.

Primary interfaces were read in the actual source: positive-form cones in 1.2.6 and 1.2.12–13; the topology in 3.1.4 and A.1.4; ordinary cutoffs and test decomposition in 6.2.6–8 and 6.5.2; the tropical-space definition 6.6.2; positive currents and coefficients in 7.2.1–12; CPsh minimality and stages in 8.1; 8.5.1–5; iterated products 8.7.1–4; smooth and general dpsh in 8.8.1 and 8.8.4–5; the printed weighted and polar arguments in 8.4 and 8.12; and the analytic topology, form-support and polar interfaces in 11.8.1, 15.2, 15.7, and 16.9.1–4. These checks include the source's two relevant defects, discussed below, rather than accepting its broadest wording indiscriminately.

The pinned earlier SOURCE_AUDIT.md, SHA256 `4b5818d69ee5fa319d15d42dfdef61b839bc32f78ad689f3714266d524ec7e97`, was read completely. It provides source-scope context and the optional elementary common-curvature implication. It was written by the author before the present proof and is not an independent validation of that later proof. Its recursive manifest contains older classification provenance; byte-checking that provenance does not turn classification into a proof prerequisite here.

The author checker was run read-only, and a separate reviewer checker was written. Exact checks cover ten direct pins, five external source pins, fourteen recursive manifests with 217 entries, eleven target checksum rows, and a standalone 23-node acyclic mathematical dependency graph. The reviewer checker also performs 4752 bounded exact-integer checks of the endpoint bracket coefficients. Those numerical checks supplement the symbolic calculation in Section 8 below; they do not establish its validity for all parameters and are not a proof certificate.

## 3. Positive versus strongly or weakly positive: the required source restriction

The note's unqualified word “positive” must retain CLD's middle-positive meaning. Under 7.2.1, a positive current is nonnegative on middle-positive test forms. The latter correspond to positive semidefinite symmetric bilinear forms on the appropriate exterior power in 1.2.6. This is not the weaker condition of testing only strongly positive forms.

There is an upstream discrepancy that must not be imported. CLD 1.2.13 states that an Euclidean (1,1)-form's p-th power is in the full interior of the middle-positive cone, but only in the *relative* interior of the strongly positive cone. It explicitly explains that strongly positive forms need not span all symmetric forms, with the (2,2) case on R^4 as an example. The proof of 7.2.9 nevertheless claims that adding a multiple of this p-th power makes every symmetric form strongly positive. That inference is unavailable in general. This audit therefore does not accept from that proof a blanket assertion that an arbitrary merely weakly positive functional has all the needed order-zero properties.

The restricted positive-current claim actually needed by this note is sound independently of that overstatement. On a fixed finite-dimensional tropical chart, let eta be the Euclidean positive definite (1,1)-form. For a symmetric coefficient form alpha in a bounded coefficient class, the PSD-matrix interpretation gives

    -C ||alpha|| eta^p <= alpha <= C ||alpha|| eta^p

in the *middle-positive* cone. Pullback preserves that cone. A nonnegative compact cutoff then gives, for a positive current S, a bound of the form

    |<S, chi f^*alpha>| <= C ||alpha|| <S, chi f^*(eta^p)>.

This supplies the C^0 coefficient estimate, compact positive majorants, order-zero extension in fixed presentations, and finite signed-coefficient variation. Weak convergence of positive S_j makes their pairing with the one fixed majorant uniformly bounded. Thus the continuity proof in 8.5.1 is valid in precisely this positive range; it already decomposes test forms into *positive*, not strongly positive, pieces.

All currents on which the new proof uses these bounds are positive in that stronger, middle sense, or finite signed sums of such currents: the initial S, each dd(fS) with f in CPsh, and eventually Gamma_S(h). Positivity of Gamma is itself proved in that same middle sense by closedness of the positive cone. Top-degree positive currents are Radon measures by the elementary scalar argument of 7.2.8. Wedge by the smooth positive forms used here preserves positivity by 7.2.7(b); the particular theta/eta barrier expressions are in fact sums of strongly positive products. None of these operations requires the false strong-cone spanning assertion.

The assumption of local differential separation suffices for the compact-support arguments, without requiring global paracompactness. A CLD G-tropical space already has a locally compact Hausdorff topology with a basis of opens countable at infinity (3.1.4). A.1.4 gives an eligible relatively compact paracompact open neighborhood of each compact support, and 6.2.8 supplies finite compact cutoffs near that support. This verifies the actual support hypothesis of 6.5.2 in the abstract setting as well as in the analytic one.

Thus the source defect in 7.2.9 is a necessary restriction on what is imported, but not a gap in the frozen note's positive-current proof. No book manuscript assertion is used to replace this independent cone check.

## 4. CPsh composition, dpsh products and controlled continuity

Lines 49–59 correctly derive the algebra needed for energy before invoking any weighted estimate. Smooth convex nondecreasing F preserves smooth psh by the usual smooth chain rule. For the general CPsh sheaf, the functions u for which F(u) belongs to CPsh form a subsheaf containing the smooth psh functions. Uniform convergence locally is preserved by F after restricting to a neighborhood where the functions have bounded range. The local restriction is legitimate even if the functions are unbounded on a larger open. Minimality therefore gives the composition property for all CPsh u. Separate-variable closure likewise proves addition; nonnegative scaling is immediate by closure.

The positive-range square extension at line 49 is valid. Its derivative 2t chi(t) on t>=0 is nonnegative and has nonnegative derivative, extends smoothly through zero when chi vanishes there, and agrees with 2t eventually. An additive constant then makes the function equal to t^2 on the required positive range. Consequently common positive shifts of finitely many locally bounded CPsh functions may be squared within CPsh. This avoids the invalid use of t^2 as a globally increasing function on all real numbers.

For h=u−v, the exact identity h^2=2f^2+2g^2−(f+g)^2 with f=u+M and g=v+M proves that h^2 is locally dpsh. Polarization proves the same for products hl. Therefore dd(hS), dd(h^2S), and dd(hlS) are finite differences of positive curvature currents. Their order zero is not inferred by differentiating an arbitrary order-zero current. It follows from the displayed CPsh decompositions and the positive curvature theorem 8.5.5.

The energy definition (2.3) is accordingly meaningful: continuous functions multiply positive currents and their finite differences, and all its terms have locally finite coefficient variation. Independence from a chosen decomposition follows because the terms have the stated distributional meaning. Bilinearity follows from expansion of the product and the linear operations; it is not an assumption about the positivity of a mixed term.

The continuity assertion (2.4) is deliberately restricted to decompositions whose four CPsh sequences converge locally uniformly to the stated CPsh limits. Near a fixed compact support, all sequences and limits admit a *common* positive shift. The shifted square curvatures are positive currents converging weakly, because their potentials converge uniformly and differentiation is continuous. Polarization handles the mixed products. A term such as h_j dd(l_j S) is split into h_j dd(a_jS)−h_j dd(b_jS), so 8.5.1 applies to positive convergent currents, not to an uncontrolled signed sequence. An extra varying continuous multiplier is absorbed into those same locally uniformly convergent coefficients. Compact positive majorants give a uniform variation bound for the finite collection.

This is sufficient for every subsequent closure argument. It does not assert continuity for arbitrary signed weakly convergent currents or convergence in total variation. Nor does it presuppose that the arbitrary CPsh function under study possesses a direct sequence of smooth approximants.

## 5. Positivity and the exponential chain identities

The separate-variable closure at lines 93–95 is logically valid. Fix smooth psh v. As u varies, the condition Gamma_S(u−v)>=0 is local, contains all smooth psh u by the smooth Leibniz formula, and is closed under uniform limits by the controlled continuity just proved. It therefore holds for all CPsh u. Now hold one such arbitrary u fixed and apply the same argument in v; the first step supplies the smooth v starting class. Local dpsh decompositions then cover every h. No simultaneous two-variable smoothing or transfinite-stage collapse is used.

After this step Gamma_S(h) is a positive order-zero current, although it need not be closed. The proof uses only positivity, not closedness, of the energy current. The positive closed S in the definition remains fixed during these closure arguments.

The exponential identities (3.1)–(3.2) also form a genuine closed subsheaf condition. For smooth u they follow from the ordinary differential chain rule. If CPsh u_j satisfy them and converge locally uniformly, composition makes exp(Bu_j) converge locally uniformly in CPsh. Controlled energy continuity gives convergence of Gamma_S(u_j) and Gamma_S(exp(Bu_j)); their positivity and 8.5.1 justify all additional exponential multipliers. The other curvature terms converge for the same reason. Hence both identities hold for every CPsh u by minimality.

Combining them yields the coefficient-one formula

    dd(exp(Bu)S) = B exp(Bu) dd(uS)
                  + exp(-Bu) Gamma_S(exp(Bu)).

There is no derivative of a nonsmooth u asserted to be an ordinary form here. The inverse exponential is a locally bounded continuous multiplier, not a new dpsh curvature input. Most importantly, the justification of these identities uses only positive-current continuity and the preceding algebra. It does not use the weighted estimate that they will later prove. This rules out the main possible circularity.

## 6. Top-degree mixed energy and the first-derivative identification

For positive closed Q of bidegree (n−1,n−1), both diagonal energies are positive Radon measures; the mixed energy is a signed Radon measure by polarization. For each rational t, positivity of Gamma_Q(h+t l) gives the quadratic measure inequality (4.1). On a relatively compact open, the sum of the total variations of the three measures is a common finite Radon dominating measure. Passing to densities and excluding a countable union of exceptional sets makes all rational inequalities simultaneous. Continuity of the scalar quadratic in t then gives A>=0, C>=0 and B^2<=AC almost everywhere. The resulting weighted Young inequality is therefore a measure inequality, with no derivative of the weights required.

The identification (4.3) needs its stated top-degree and symmetry hypotheses, which are present. For smooth h and rho, the two cross terms d'h wedge d''rho and d'rho wedge d''h have the same pairing against symmetric Q; their difference is antisymmetric. This holds also after multiplying by a scalar test. Closedness of Q identifies the first with d'(hQ) wedge d''rho, giving precisely Gamma_Q(h,rho), with no missing factor two.

For nonsmooth h, the left side is initially a distribution. It depends continuously on h under local uniform convergence, since Q has order zero and differentiation is continuous. The right side has the controlled continuity from Section 4 above, using the fixed local smooth-dpsh decomposition of rho given by 8.8.1. Minimal-sheaf closure extends the identity to CPsh h, then linearity to dpsh h. It follows that this particular mixed first-derivative distribution is an actual signed Radon measure. This does not assert an order-zero first derivative for every unrelated nonsmooth function/current expression.

The compatibility Gamma_(theta^j S)=theta^j Gamma_S follows directly from the definition when theta is smooth and closed; the differentials commute with its wedge. In the application theta is positive, so the resulting Q is positive closed. These are exactly the hypotheses needed when energy is moved between S and Q in the weighted calculation.

## 7. One compact C^2 test construction, not an uncontrolled boundary passage

The strengthened fixed-neighborhood conditions at lines 12–17 and 141–157 are enough for every integration by parts used later. Since K_delta={rho<=delta} is compact in Y and delta>0, closure(U) is compactly contained in Y. All potentials, including the smooth polar surrogate V, are defined near that one compact. Continuity makes the CPsh potentials bounded there.

For integer a>=4, the smallest exponent in the original beta_0 is a−1>=3. The scalar function max(−t,0)^b is genuinely C^2 across zero for each such integer b. Thus all beta_k have C^2 coefficients and compact support in closure(U); this statement also covers the scalar beta_n. The formula does not use the source's incorrect finite-regularity shorthand at an integer endpoint.

One-variable convolution gives smooth approximants whose first two derivatives converge on the bounded rho-range in question. The approximants may extend a distance epsilon to the positive side, but for small epsilon their entire supports are inside the same K_delta. Because all remaining differential factors are smooth, a finite fixed chart cover of that compact gives convergence of the forms and their first two derivatives in the required coefficient seminorms.

For an order-zero current the original pairings converge by the C^0 coefficient bounds from Section 3. For dd(uS), transferring the two derivatives to the test coefficients gives a second consistent limit, because uS has order zero. Closedness identities and Stokes likewise pass by these derivative seminorm bounds. For the mixed first derivative, the C^1 test limit agrees with the energy-measure identity just established; its remaining continuous scalar weights can then be evaluated as measure multipliers. Thus no uncontrolled pairing of an arbitrary distribution with a merely continuous form is inserted.

Positivity of the temporary smooth coefficient approximants is not needed: they justify identities only. Positivity and inequalities are applied to the limiting beta_k and to the established positive current/measure objects. All relevant beta coefficients and differentiated weighted powers vanish at rho=0, so the construction generates no extra boundary delta term.

The hypothesis that V is smooth near K_delta, not merely on U, is material. It makes (−V)beta_k a compact C^2 test with controlled derivatives for this limiting operation. In the polar application each fixed smooth V_p has exactly that property. No uniform control of derivatives across p is claimed or required.

## 8. Correct endpoint algebra, IBP sign and coefficient-one cancellation

Write l=k+a and b_k=2 for k<n, b_n=1. For k<n, both terms of beta_k contribute to d''beta_k. For k=n only r^l remains, and the derivative has coefficient l, not 2l. Direct differentiation verifies (5.1)–(5.2):

    d''beta_k = -b_k l r^(l-1) d''rho theta^(n-k),
    dd beta_k = b_k l[-r^(l-1)theta^(n-k+1)
                     +(l-1)r^(l-2)eta theta^(n-k)].

The derivatives of the scalar beta_n do not vanish by degree. The note has explicitly corrected the printed source's endpoint factor and uses that correction in every subsequent cross and Young coefficient. No false endpoint equality is imported from CLD 8.4.2.

For S with k−1 curvature factors and Q=theta^(n-k)S, the IBP identity (6.1) has the correct sign:

    J(z) = integral z(V dd beta_k - dd V wedge beta_k) wedge S
           +2 integral V d'(zS) wedge d''beta_k.

It follows by expanding dd(−V beta_k) and transferring one cross derivative using Stokes and symmetry. As a sign check in one variable, its right side reduces after ordinary integration by parts to integral z(−V beta)''; this equals integral (−V)beta z''. The distributional derivation uses exactly the C^2 compact testing established in Section 7, not a smoothness assumption on z.

Using (4.3) and the corrected d''beta_k gives cross term 2b_k l(−V)r^(l−1)Gamma_Q(z,rho). The measure-level Young inequality with the two weights displayed in the note yields the coefficient-one term (−V)r^l z^(-1)Gamma_Q(z), plus b_k^2 l^2(−V)z r^(l−2)Gamma_Q(rho). This remains valid at r=0 because the powers vanish; z is bounded below by a positive constant near K_delta. All terms are finite measures on the common compact, so no improper-boundary convention is being used.

The contribution −z ddV wedge beta_k wedge S is nonpositive: z>0, ddV is positive, and the barrier factors and S are positive. Dropping it is therefore in the claimed upper-bound direction. The remaining bracket has coefficients

    b_k l                 on r^(l-1)theta^(n-k+1),
    b_k l((b_k-1)l+1)     on r^(l-2)eta theta^(n-k).

For k<n these are 2l and 2l(l+1). For k=n they are l and l. Since beta_(k−1) has coefficients 1 and l−1 in these same two slots, c_k=2l(l+1)/(l−1) bounds both cases. In the two-summand case the second coefficient is exact and the first is bounded; in the scalar endpoint both are bounded. These are nonnegative-coefficient combinations of positive forms, so the coefficient comparison is a valid form/current inequality. The reviewer's finite integer tests are consistent with, but do not replace, this symbolic check.

It follows that

    J(z) <= c_k ||z||_U J_(k-1)
            + integral (-V)r^l z^(-1)Gamma_Q(z).

Now take z=exp(Bu_k). The exponential identity gives the lower bound (6.6) only on U, where u_k>=−M with M=||u_k||_U. That is sufficient because beta_k has zero coefficients everywhere outside U, including its boundary. Its first summand gives *the very same* coefficient-one energy integral as in the preceding upper bound; the second summand, when present, is nonnegative and can be discarded from the lower bound. Consequently the subtraction in (6.7) is legitimate and the energy integrals cancel exactly.

With ||exp(Bu_k)||_U<=exp(BM), the result is J_k<=c_k B^(-1)exp(2BM)J_(k−1). Taking B=1/(2M), for M>0, gives the stated factor 4e l(l+1)/(l−1) M. The norm is finite by the common compact neighborhood. If M=0, u_k vanishes on U, so dd(u_kS) is zero there by locality; possible current mass elsewhere is multiplied by zero barrier coefficients. Hence J_k=0, and no division by zero is used.

The induction starts with J_0 itself, and multiplying the step constants gives (1.2), including the telescoped alternative expression. The temporary compact-majorant bounds used to justify coefficient limits may depend on the fixed current S and the fixed potentials; they serve only to establish the identities and continuity passages. They do not enter the numerical weighted constant. The actual estimate is derived from the exact identities, positivity, and the displayed scalar coefficient comparison, so its final dependence is precisely the fixed barrier data and potential sup norms stated in the note, not an ordinal stage or an approximation-dependent mass bound. The case n=1 consists entirely of the correctly treated scalar endpoint. The proof has not assumed smooth approximation of the arbitrary continuous factors at any stage of the calculation.

## 9. Polar passage: which function is approachable, and the order of limits

Section 7 correctly keeps the polar helper and the continuous factors separate. At a fixed point, choose one ordinary neighborhood on which the auxiliary V is a decreasing limit of smooth psh V_p. Choose the compact-sublevel barrier inside that neighborhood and inside the domains of the finitely many CPsh factors. The first smooth V_1 is bounded on a neighborhood of K_delta; subtracting one sufficiently large constant makes every V_p negative there. Adding that constant back does not affect local integrability against a locally finite measure.

For each *fixed p*, the new weighted estimate applies to the arbitrary CPsh u_j and this smooth V_p. Any C^2 smoothing limits used in its proof have already been justified with p fixed. The resulting bound involves no derivatives of V_p. Since −V_p increases to −V, its right side is bounded by the single integral of −V against beta_0, multiplied by constants depending on the fixed barrier and sup norms only.

That right side is finite. The compact C^2 coefficient form beta_0 is bounded in fixed smooth presentations and is dominated by finitely many positive compact smooth top forms via the middle-positive majorant argument. Canonical local integrability of V therefore supplies the needed finite bound. This is not a weak-convergence argument for null sets, and does not require uniform smooth-approximation neighborhoods for u_j.

Monotone convergence now applies to the fixed positive n-fold current measure and the nonnegative weights r^(n+a)(−V_p). It gives integrability of r^(n+a)|V|. On a smaller compact set contained in U and near the chosen point, r^(n+a) has a positive lower bound. Thus V is locally integrable for the unweighted product measure there, and its polar set has zero measure. The auxiliary V remains directly locally approachable throughout; only the continuous factors are generalized to the full CPsh sheaf.

The order of operations is exact: first controlled CPsh closure and compact coefficient identities, then the weighted estimate at fixed p, then a canonical-L1 bound uniform in p, then the monotone polar limit. There is no unsupported diagonal approximation or inference that weak limits preserve analytic-null sets.

## 10. All ordinary trace forms and signed total variation

For m<n, an ordinary smooth trace form is locally f^*omega in a fixed tropical presentation. Remove its antisymmetric part, which pairs to zero with the symmetric product current. On a compact tropical image, the symmetric coefficients are bounded. The positive definite Euclidean Hessian gives a middle-positive form majorant

    -C(dd v)^(n-m) <= alpha <= C(dd v)^(n-m),
    v=f^*||t||^2.

This uses the full interior of the middle-positive cone, not of the strongly positive cone. Pullback preserves the comparison even when the chart has rank drop. No full-rank assumption at all analytic points is needed. The smooth v is psh and is defined and bounded on the compact neighborhood on which the barrier is subsequently chosen.

Apply the established n-factor integrability to u_1,...,u_m and n−m copies of v. If mu is the signed trace with alpha and nu the resulting positive trace with (ddv)^(n−m), the two form inequalities give −Cnu<=mu<=Cnu as measures. Therefore |mu|<=Cnu. This is a genuine total-variation bound, not merely a signed integral cancellation. It proves (1.3) locally for every symmetric alpha, and then for all alpha by symmetry and a finite compact partition.

The proof covers the endpoints correctly. At m=0 the additional smooth factors give the needed domination of the canonical trace. At m=n, alpha is a locally bounded smooth scalar and the top-degree result applies directly after multiplication by its absolute value. No nonexistent negative wedge power or extra auxiliary factor is used at m=n.

## 11. Actual analytic barriers over the original complete field

The construction in lines 257–285 repairs the problematic literal wording of CLD 16.9.1. It constructs rho on an ambient ordinary open Y with a *smaller* negative sublevel, and a positive closed sublevel K_delta compact inside Y. It does not assert that rho is negative everywhere on its domain while the whole domain is compact.

Goodness allows an affinoid neighborhood A inside the prescribed ordinary neighborhood, and a rational affinoid neighborhood W of x inside Int(A). Because the ambient space is boundaryless, this analytic interior is the relevant ordinary interior at these points. Use the actual rational inequalities with functions f_i,g having no common zero and arbitrary positive real radii lambda_i.

The step from W to W_mu inside Int(A) is justified by nested compactness. If every W_mu, mu>1 arbitrarily close to 1, met the closed complement of Int(A), the corresponding nested compact sets in A would have a point in their intersection, hence in W but outside Int(A), a contradiction. The no-common-zero condition ensures g has no zero on any W_mu. Thus the logarithmic ratios are legitimately defined on Y=Int(A) intersect {g!=0}, with their allowed negative infinities only at numerator zeros.

The constant branch a_0=−1 is important. It keeps the regularized maximum finite even if every numerator vanishes. Convolution of the maximum with an even product probability kernel is convex, coordinatewise nondecreasing, lies between the maximum and maximum+epsilon, and ignores a coordinate separated below the maximum by more than 2epsilon. Near a numerator zero that coordinate is ignored; elsewhere the surviving coordinates are analytic log-units. Consequently the expression extends to a genuine ordinary smooth psh function across all numerator zero loci, rather than only defining a function on a torus.

With t=log(mu), epsilon<t/8 and rho=M_epsilon(a_0,...,a_s)−t/2, the point x has rho(x)<0. The positive closed sublevel rho<=t/4 implies every a_i<=3t/4 and is contained in W_(exp(3t/4)), itself inside the compact W_mu and Y. Restricted to that compact rational domain, rho is continuous, so the sublevel is closed there and compact. This verifies the exact K_delta hypothesis used for C^2 testing and the fixed-neighborhood weighted inequality.

No uniformizer, scalar extension, nontrivial value group or strict-affinoid neighborhood basis over a trivial field is used. Arbitrary real rational-domain radii are permissible. The final note states CLD's strictness convention explicitly, with usual strictness sufficient as a smaller class; it does not silently confuse the two over trivial valuation. In fact the local construction uses only the stated good analytic neighborhoods and boundaryless interior properties.

For an abstract tropical barrier with only a relatively compact negative sublevel, the upward shift in line 285 is also sufficient: choose a positive shift smaller than −rho(x), then a smaller positive delta, so the new closed sublevel lies in the old negative sublevel. Its closedness and the old relative compactness provide the needed compact K_delta. This does not enlarge the class of abstract spaces beyond the local barrier hypothesis.

## 12. The analytic pole and lower-dimensional closed subsets

For an analytic closed Z with local dimension <n, prime avoidance on a sufficiently small affinoid neighborhood chooses f vanishing on Z but on no top-dimensional component. Pure dimension ensures its zero set has dimension <n. The construction requires neither normality nor geometric reducedness; avoiding all top-dimensional minimal primes is the relevant condition, and lower-dimensional embedded structure does not change this dimension assertion.

CLD 15.2.1(b) is used in its actual ordinary form-support meaning. Every compact ordinary smooth top form has support disjoint from this zero set. Thus |f| is bounded above and away from zero on that compact support, and log|f| is bounded there. This gives canonical local integrability, including the original canonical generic multiplicities on a nonreduced space. It is not an assertion that all lower-degree tests avoid Z.

The proof supplies a direct smooth sequence for this particular logarithm. The regularized positive part F has 0<=F'<=1, is zero below −1, and equals its argument above 1. Therefore F_p(t)=−p+F(t+p) decreases in p. Composed with log|f|, it is a smooth convex log-unit function off the zero set, and extends as the constant −p on an ordinary neighborhood of each zero. It is smooth psh on one common neighborhood for each p, and decreases to log|f| also at the poles. This directly verifies the helper's stage-one hypothesis without passing from one approximation stage to another.

Applying Section 9 to this helper and Section 10 to arbitrary trace forms proves zero *total-variation* mass on Z for every product of full continuous CPsh factors. Only the helper has been explicitly smoothed. The conclusion is therefore the claimed new all-CPsh-factor analytic-nullity result, not merely the old statement with locally approachable u_j.

## 13. Optional component-curvature consequence and independence

The optional Section 9 does not supply scalar classification, and its elementary implication is valid. For the actual locally finite reduced components X_i with positive generic lengths m_i, write delta_X=sum_i m_i delta_i. For a continuous CPsh potential u, each dd(u delta_i) is a positive closed current by 8.5.5 on X itself. No current pullback through a normalization is needed.

For u,v with equal canonical curvature S, there are two decompositions S=sum_i m_i A_i(u)=sum_i m_i A_i(v) into positive currents. At a compact positive test alpha they give positive-measure domination 0<=A_i(u) wedge alpha<=S wedge alpha/m_i, and similarly for v. The just established analytic-nullity theorem with m=1 makes S's coefficients null on the component crossings, whose dimension is <n. Hence every component coefficient is null there.

Independently, R_i=A_i(u)−A_i(v) is supported on its crossing locus: off X_i it is zero by support, and on the ordinary complement of all other components the equality gives m_iR_i=0. Combining support with signed total-variation nullity gives R_i=0. Compact positive-form decomposition then accounts for every ordinary test. The positive generic weights are retained; no algebraic cancellation of unrelated currents at the crossing is presumed.

This optional consequence remains classification-free and does not require discreteness or residue characteristic zero. To pass from it to a statement about *every* positive closed scalar current would require a separate valid classification on the actual ordinary domain, with that theorem's field and dimension hypotheses. This report neither inserts that classification into the weighted proof nor independently certifies a new combined all-field scalar theorem.

## 14. Findings, source cautions and correction status

No blocking or substantive correction is required to the frozen proof in its exact stated scope. In particular, the core conclusion is not being restricted back to stage one for the continuous factors.

The following explicit qualifications should accompany future use; they do not require changing the frozen bytes:

1. **Note lines 8, 61–80, 151–153, 249–253; source ledger row 7.2.1–12.** Interpret all unqualified positive-current bounds in the middle-positive sense. The proof needs only that range, which the independent PSD-majorant check above validates. Do not import the overbroad merely weak-positive order-zero assertion from the flawed strong-cone step in CLD 7.2.9. An explicit parenthetical source warning would be useful in a future exposition, but the note never states that broader assertion.
2. **Note lines 141–149 and 190–199.** The k=n correction is substantive and is already present. A future transcription must preserve b_n=1 and the corresponding Young coefficient and bracket coefficients. Keeping the printed source's factor two at the endpoint would be erroneous, even though a loose upper bound can absorb the corrected smaller coefficients.
3. **Note lines 17, 151–157 and 231–243.** Smoothness of each V_p on a neighborhood of the one compact K_delta, and the fixed-p order of coefficient limits, are essential hypotheses. Replacing them by smoothness only on U with uncontrolled boundary growth would invalidate the supplied IBP justification.
4. **Note lines 36 and 231–247.** The new full-CPsh scope applies to u_j, not to arbitrary singular helpers V. Direct local approachability and canonical local integrability of V are retained. The analytic logarithm is explicitly checked to satisfy them.
5. **Note lines 257–283.** Strictness is stated in the CLD convention; the usual strict class is sufficient. Arbitrary real radii in the rational domains do not assert that every ordinary open over a trivial field has a usual-strict affinoid basis.

These are exact-scope safeguards, not substitute missing lemmas. The proof already has the necessary hypotheses and the corrected endpoint computation. All frozen predecessors and this auditee remain unchanged.

## 15. Final dependency and verification statement

The standalone graph has 23 clause nodes. Its main path is: primary middle-positive current calculus and CPsh minimality; explicit dpsh products and controlled continuity; separate-variable energy positivity; exponential identities and top-degree Schwarz; one-compact C^2 integration by parts and corrected endpoint algebra; weighted energy cancellation; fixed-helper then monotone polar passage; ordinary trace domination; and actual original-field analytic barriers and logarithms. There is no classification, displayed representation, L/O/Q model-current package, prior approachable audit verdict, or assumed hierarchy-collapse node.

The source and byte checker validates ten direct pins, five external pins, fourteen recursive manifests with 217 entries, eleven source checksum rows, the final audit checksum list, and the graph's absence of the forbidden classification/R/collapse prerequisites. Recursive context manifests are checked only for provenance. The bounded endpoint arithmetic checks test coefficients using exact integers and have no authority over the analytic parts of the proof. The actual mathematical reasons for the verdict are Sections 3–13 of this report.

The new proof legitimately removes the locally approachable restriction on the *continuous potential factors* in the weighted/polar analytic-nullity argument. It does not prove a regularization theorem collapsing CPsh, does not remove the helper V's hypotheses, does not classify arbitrary positive currents, and does not establish full P21.3. Mathematical PASS here is separate from any production review the parent may conduct through its own actual protocol.
