# Independent exact-byte audit: real weight parameters

Date: 1 September 2026.
Reviewer: /root/p213_skeletal_hostile.
Candidate author: /root.
Frozen candidate note: p213_weight_parameter_extension_research_20260901/RESEARCH_NOTE.md, 10961 bytes, SHA256 23859df000c8754f5853fa5acd32b5606e73d4ca10989dac5ad28e91b3d11c70.

## 1. Verdict, independence and exact boundary

PASS for the entire NEW real-a>1 weighted assertion and its structured-regularization proof, relative to the explicitly named energy-calculus input. I found no substantive gap, critical error, or required correction in the frozen statement or proof, including the top endpoint and the order-one mixed term.

This is a fresh independent review of ROOT's parameter-extension argument, not a fresh independent certification of the earlier energy calculus. I authored the earlier full-CPsh weighted/polar note; its Sections 2–4 are therefore treated here as a disclosed assumed input, already accompanied by a separate fresh independent audit by another agent. I did not author the new structured mollification argument, propose its replacement proof, or edit the candidate. The calculations below are audit checks of its frozen proof, not substituted candidate text.

The accepted scope is the displayed inequality for every real a>1, 0<=k<=n, on the stated boundaryless locally differentially separated CLD tropical space, with smooth psh rho, compact K_delta, and ALL potentials and the smooth auxiliary V defined near K_delta. V is required negative only on U={rho<0}. The CPsh factors are in the full minimal continuous uniform-closure sheaf. Empty products mean canonical integration. No smooth approximation sequence for an arbitrary CPsh factor is added.

The verdict is mathematical and conditional on the exact energy inputs. This is NOT production verification, runtime-policy approval, a full dependency-closed production submission, or authorization to integrate live. The earlier production execution caveats are retained. No assertion at a=1, parameter sharpness, general psh hierarchy collapse, scalar-current classification, or P21.3 solution is verified here.

## 2. Exact byte and source checks

I read the complete frozen RESEARCH_NOTE.md (166 lines), SOURCE_AND_DEPENDENCIES.md, manifest, checksum list and checker. The note and manifest match the hashes supplied by root. The candidate's read-only checker succeeds: five manifest entries and six checksums, including the exact earlier energy note and its ledger.

INPUT_PINS.json records nine independent read-only pins, including all five candidate files, the exact energy note and ledger, its separate independent audit and the primary CLD text. The candidate was not modified by this review.

The earlier energy note is pinned at SHA256 2bdbb2c72135779323fea27c6d8c38ebd665c3eca21037017ff0442953433a5f. I reread its complete Sections 2–4 and source ledger for interface matching. Those sections, not its weighted estimate in Sections 5–6, supply:

- order zero and finite coefficient variation for the explicitly decomposed dpsh curvatures and energies;
- energy positivity for full dpsh functions through separate-variable CPsh closure;
- the full-CPsh exponential identities;
- the signed top-degree mixed energy measure, Radon–Nikodym Schwarz inequality, and the identity with a distributional derivative paired against a SMOOTH rho;
- commutation of energy with a fixed smooth closed positive form.

Primary CLD text was checked directly at local lines 10249–10329 (8.5.1–8.5.5), 10410–10482 (8.7 products and symmetry), and 10489–10560 (8.8 smooth/dpsh functions and multilinear extension). The source's degree conventions are not used to skip the explicit degree calculation below. No primary source is cited as already proving the new all-real-a/full-CPsh theorem.

## 3. Space, compact support and finiteness (candidate lines 16–35)

Since K_delta is compact and rho is continuous, rho(K_delta) is bounded and K_0 is a compact subset of K_delta. Every scalar coefficient of beta_k is continuous and bounded there: at k=0 the smallest exponent is a-1>0. Outside K_0 all coefficients vanish. The top-index weight has only the first summand, as explicitly stated.

The weights are legitimate products of continuous scalar functions with fixed smooth forms theta and eta. Pairing them with positive currents, or finite differences thereof, therefore uses the established Radon coefficient measures. It does not require a global new theory of arbitrary continuous forms, and chart changes respect these products. A finite chart cover and compact partition handle a given K_delta. No unproved order-zero statement about arbitrary distributions is invoked.

All factors are defined on one open neighborhood of K_delta. Even if not defined on all Y, all tests below lie compactly in that common neighborhood, so distributional identities are local there. Continuous u_j and V are bounded on K_delta; the relevant currents have finite coefficient variation on that compact set. Thus the integrals and the later energy terms are FINITE before any cancellation. Their finiteness is not deduced from the weighted inequality being proved.

Theta=dd rho is positive of bidegree (1,1), and eta=d'rho wedge d''rho is strongly positive of that degree. Their powers and indicated products with positive currents have the required positivity. No sign of V outside U is assumed.

Here and throughout, positive means the CLD middle-positive convention, not merely weak positivity against strongly positive tests. The explicit energy input and its separate audit use that convention. The required coefficient bounds can be obtained with middle-positive compact majorants; the stronger-cone spanning error in the source proof of 7.2.9 is not an additional input to this argument.

## 4. Structured approximation and the endpoint (lines 39–80)

For every differentiated step k>=1, l=k+a>2. Hence F(t)=(-t)_+^l is genuinely C2, with F'=-l(-t)_+^(l-1) and F''=l(l-1)(-t)_+^(l-2), both tending to zero at the origin. Convolution by a nonnegative compactly supported smooth probability kernel gives the claimed uniform convergence of F_epsilon, F_epsilon' and F_epsilon'' on every fixed compact interval. The unbounded polynomial behavior as t tends to minus infinity causes no issue, since the kernel is compactly supported and the relevant rho-image is compact.

F_epsilon is nonnegative and nonincreasing, and vanishes for t>=epsilon. Consequently beta_(k,epsilon) is smooth positive and supported in K_epsilon, a compact subset of the SAME K_delta when epsilon<delta. It is not merely supported in varying noncompact neighborhoods. No inequality is yet applied to V on the small outer collar.

For q=n-k>0, check the algebra:
d''eta=-theta wedge d''rho, and d''rho wedge eta=0. Thus differentiation of F_epsilon(rho)theta^q contributes one F_epsilon' term; differentiation of -F_epsilon'(rho)eta theta^(q-1) contributes a second copy. The F_epsilon'' d''rho wedge eta term is zero. Differentiating once more therefore uses only F_epsilon' and F_epsilon'', not F_epsilon'''.

For q=0, beta_(n,epsilon) is the scalar F_epsilon(rho). There is only ONE copy of each derivative. The value b=1 in this case, versus b=2 for q>0, is essential and correct. These endpoint derivative terms lie in permitted degree; they cannot be discarded on dimensional grounds.

It follows that beta_(k,epsilon), d''beta_(k,epsilon), and dd beta_(k,epsilon) converge in coefficient norm on finite compact chart covers to the exact expressions (3.4)–(3.5). Distributional differentiation agrees with that limit, so there is no hidden hypersurface delta term at rho=0.

The proof correctly does NOT claim beta_k itself has C2 coefficients for all a>1. For example, when k=1 and q>0 with 1<a<=2, the second scalar coefficient involves (-rho)_+^a, which need not be C2. Its exterior derivatives nevertheless have the stated uniform limits because of the exact wedge cancellation. Likewise beta_0 can fail C2 even at the book choice a=3, but beta_0 is never differentiated in this argument. These are reasons the STRUCTURED approximation is necessary, not defects of it.

## 5. Degree ledger and the smooth-test identity (lines 84–99)

At the kth step:

- S has bidegree (k-1,k-1);
- beta_k has bidegree (q,q), q=n-k;
- dd(zS) has bidegree (k,k);
- Q=theta^q wedge S has bidegree (n-1,n-1);
- d'(zS) wedge d''beta_(k,epsilon) and every displayed integral have bidegree (n,n).

Thus Gamma_Q(z,rho) is a signed Radon MEASURE, not merely a lower-degree current being treated as a scalar measure. S and Q are positive and separately closed; z>0 is CPsh and rho is smooth psh (in particular dpsh).

I checked the sign and factor 2 of (4.1) directly. Write beta=beta_(k,epsilon). Symmetry and the compact smooth product rule give the integrated expression

    I = -integral z [V dd beta + dd V wedge beta
                             +2 d'V wedge d''beta] wedge S.

Closedness and Stokes, applied distributionally to zS with the smooth compact coefficient V d''beta, give

    integral V d'(zS) wedge d''beta
      = -integral z [d'V wedge d''beta+V dd beta] wedge S.

Substitution is exactly (4.1): the dd-beta term becomes positive inside z[V dd beta-ddV beta], and the remaining term is +2 integral V d'(zS) wedge d''beta. These calculations require neither a pointwise ordinary derivative of z nor a smooth approximation to z. All differentiated test coefficients are smooth for fixed epsilon.

The three order-zero terms converge by uniform convergence of their coefficient forms on the one compact set. Multiplication by the fixed bounded continuous z and smooth V is permitted. This part does not depend on any weighted estimate.

## 6. The order-one mixed passage (lines 101–113)

This is the decisive issue, and the frozen proof resolves it.

Because theta is separately closed,

    d'(zS) wedge theta^q = d'(zQ).

Inserting (3.2), and ONLY THEN using the assumed top-degree mixed-energy identity from the predecessor Section 4, gives for each epsilon

    integral V d'(zS) wedge d''beta_(k,epsilon)
       = b integral V F_epsilon'(rho) Gamma_Q(z,rho).

The current on the left is initially of order one. The argument does not extend its action by C0 continuity. Instead, the right side is the same ONE FIXED signed Radon measure for all epsilon. Its total variation is finite on K_delta. More explicitly, the error in passing to the limit is bounded by

    b ||V||_(K_delta)
      ||F_epsilon'-F'||_(rho(K_delta))
      |Gamma_Q(z,rho)|(K_delta),

which tends to zero. There is no varying signed weak measure multiplied by a varying continuous coefficient, and no lost derivative of F_epsilon'.

The limit F'=-l r^(l-1) changes V F' into l(-V)r^(l-1), giving the POSITIVE displayed sign +2bl in (4.3). The other limiting coefficients involve r^l, r^(l-1), or r^(l-2), all zero at rho=0 since l>2. Thus even if an underlying current charges that level, it contributes nothing to these limiting integrals. Integration over Y can be replaced by integration over U after the limit.

The proof applies inequalities only after that limit, on U. No sign condition on V in 0<rho<epsilon is smuggled into the calculation. The stronger requirement that V be smooth near K_delta supplies legal compact smooth test coefficients for every epsilon.

## 7. Weighted Schwarz and both coefficient cases (lines 117–142)

The assumed measure-level Schwarz inequality applies to the fixed three measures Gamma_Q(z), Gamma_Q(z,rho), Gamma_Q(rho). On U the Young weights can be taken as

    A=(-V)r^l/z,
    C=b^2 l^2(-V)z r^(l-2).

Both are nonnegative and have continuous zero extension at r=0. Since z is strictly positive on a neighborhood of the compact K_delta, its reciprocal is bounded there. Their geometric mean is b l(-V)r^(l-1), giving exactly (5.1). All products are finite signed/positive Radon measure products. Schwarz does not require differentiation of those weights.

The term -z ddV wedge beta_k wedge S is nonpositive on U. Using Gamma_Q(rho)=eta wedge Q, the remaining comparison is (5.2). The eta coefficient is

    b^2 l^2 - b l(l-1) = b l[(b-1)l+1].

For b=2 this is 2l(l+1); the theta coefficient is 2l. With c_l=2l(l+1)/(l-1), the eta coefficient agrees with c_l(l-1), and 2l<=c_l.

For b=1 both coefficients are l. They satisfy l<=c_l and l<=c_l(l-1), since l>2. Hence the SAME deliberately nonsharp c_l works at the scalar endpoint. No false factor-two identity is reintroduced.

The beta_(k-1) weight is used only as a continuous positive coefficient form, including at k=1. Taking the supremum norm of positive z on U yields exactly (5.3).

## 8. Exponential identity, finite cancellation and recursion (lines 144–158)

For M=||u_k||_U=0, the given continuous function is identically zero on U, so its curvature product vanishes there by locality. The weights vanish at the boundary; this case has J_k=0 independently of any division by M.

For M>0 set z=exp(Bu_k), B>0. The assumed full-CPsh exponential identity is

    dd(zS)=B z dd(u_k S)+z^(-1)Gamma_S(z).

The first term, after multiplication by the positive (-V)beta_k on U, is bounded below by B exp(-BM)J_k(u_k). The first summand of beta_k paired with the second term is EXACTLY

    E=integral_U (-V)r^l z^(-1)Gamma_Q(z),

using the predecessor's closed-form energy identity. The second beta summand gives an additional nonnegative measure and is discarded. This proves (5.4) with exactly the same E as in (5.3).

E is finite by compact support, bounded coefficients and finite energy mass. Therefore subtracting it is legitimate; no infinity-minus-infinity step occurs. Also ||z||_U<=exp(BM). The resulting estimate is

    J_k(u_k)<=c_l B^(-1) exp(2BM) J_(k-1).

Choosing B=1/(2M) gives 2 exp(1)M c_l
=4 exp(1)M l(l+1)/(l-1), the claimed factor. Iteration yields precisely the stated product C(k,a), with J_0=integral_U(-V)beta_0. All lower bounds on u and signs of V are explicitly used only on U.

No integer-power property is used anywhere. The lower parameter restriction needed by the proof is l>2 for differentiated k>=1 and a-1>0 for beta_0; both follow from a>1.

## 9. Consequences, source attribution and retained limits

The full proof therefore covers the book value a=3, WITHOUT asserting all beta_k are C2. It also covers every real a>1 under the displayed compact-neighborhood hypotheses. This is stronger than a cosmetic endpoint correction.

Candidate Section 6 is accurate: a=4 remains available for the earlier polar application, so the new extension is not a hidden dependency of its already frozen proof. If another admissible a is chosen, beta_0 is a bounded continuous positive top coefficient form. On fixed compact charts it has a smooth positive top-form majorant, so canonical local integrability of an auxiliary pole implies integrability with the beta_0 weight. No beta_0 derivative is required.

The candidate does not drop smoothness of the V used in the weighted inequality near K_delta; for polar applications the chosen smooth truncations still supply it. Nor does it remove the actual approachability/canonical integrability requirement of the AUXILIARY polar function. It changes only the real weight parameter in the weighted estimate.

CLD Sections 8.4 and 8.12 are comparison sources and sources of the older strategy, not citations for this full-CPsh real-parameter extension. The candidate's source ledger says so. The existing full-CPsh energy result is necessary and must accompany this note in a dependency-closed submission. The new note alone is not such a submission.

No edits to candidate, predecessor or book, no Git actions, no service changes, no production call and no PDF compilation were performed in this audit. The primary source was read as the pinned extracted text. I cannot independently attest this review agent's runtime model/effort from the exposed metadata; no production sol/xhigh status is claimed.

## 10. Final bounded conclusion

Required mathematical corrections: none.
Critical errors: none found.
Unresolved gaps within the displayed real-a>1 theorem, GIVEN the explicit energy input: none found.

The existing execution-policy caveat and the need for dependency-closed exact production verification remain operational gates. This independent mathematical PASS does not remove them.
