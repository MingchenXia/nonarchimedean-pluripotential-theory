# Exact retained theorem and remaining original obligations

{
  "id": "P16.3",
  "status": "partial",
  "exact_result": "Primary-source deduction of a genuine E1 Monge-Ampere operator and arbitrary-support finite-dual-energy existence/uniqueness on smooth geometrically integral projective surfaces of geometric origin from a curve over a perfect equal-characteristic-p field, over its nontrivially discretely valued function-field completion, with any ample line bundle and raw mass (L^2). Both geometric resolution inputs are proved in the required total dimension three by GJKM1712.00980v3 Theorem 6.3. The same argument has a conditional higher-dimensional geometric-origin range retaining both explicit resolution premises. This does not solve the entire original positive-residue-characteristic atom.",
  "proof_file": "P16.3-argument.md",
  "concrete_gaps": [
    "Mixed characteristic: no replacement is proved for cofinal regular/SNC models or their substitutes, envelopes/regularization, and the resulting compatible unbounded operator, differentiation, and comparison for characteristic-zero fields with positive residue characteristic.",
    "Unrestricted higher dimension in equal characteristic: both GJKM Definitions 6.1 and 6.2 are still required in total dimension d+n when not covered by the proved resolution range; the argument does not establish these premises.",
    "General complete discretely valued equal-characteristic-p fields and smooth projective varieties outside GJKM Definition 8.1 geometric origin: no realization or replacement compactness and envelope/regularization theorem is proved."
  ]
}

# Entire author proof

# P16.3: a proved equal-characteristic surface range and the remaining residue-characteristic axis

This is a partial mathematical result, not a solution of the full original P16.3. The main theorem below concerns nontrivially discretely valued equal-characteristic fields and general smooth projective surfaces of geometric origin. Its target measures have arbitrary support subject to the exact finite-dual-energy condition. The proof constructs the genuine nonpluripolar finite-energy operator and proves variational attainment; it does not infer surjectivity from completion of a space of measures. In higher dimensions the same argument retains precisely stated resolution premises. Mixed characteristic and the unrestricted geometric-origin and dimension obligations remain unresolved here.

All mathematical assertions below are draft deductions from the eleven supplied public primary-source caches. No priority claim is made for the combination proved here. Successful hash checks and TeX builds do not verify these deductions.

## 1. Exact sources and what they state

Use the following abbreviations, always for the exact saved versions.

[S] Boucksom--Favre--Jonsson, *Singular semipositive metrics in non-Archimedean geometry*, arXiv:1201.0187v2. Its standing residue characteristic is zero. Its compactness theorem is Theorem 7.10, and its monotone regularization theorem is Theorem 8.7. The characteristic-zero multiplier-ideal argument in section 8 and Appendix B will not be reused in characteristic p.

[B] Boucksom--Favre--Jonsson, *Solution to a non-Archimedean Monge-Ampere equation*, arXiv:1201.0188v1. This is the actual v1, not a later theorem statement: Theorem A assumes residue characteristic zero, algebraizability, and measure support in an SNC dual complex. Its sequence regularization result is Proposition 4.5. Its operator/energy results are Theorem 3.1, Theorem 5.1, Proposition 6.2, Definition 6.4, Lemmas 6.7--6.10, Propositions 6.11--6.12, and Theorem 7.2/Corollary 7.3. Proposition 8.2 treats uniqueness for finite-energy potentials, not merely continuous ones.

[G] Gubler--Jell--Kunnemann--Martin, with an appendix by Burgos Gil and Sombra, *Continuity of Plurisubharmonic Envelopes in Non-Archimedean Geometry and Test Ideals*, arXiv:1712.00980v3, dated 22 November 2018 on the PDF identifier. Starting in section 7, K is complete discretely valued and has characteristic p>0. It is not a mixed-characteristic theorem. Definition 8.1 requires a normal d-dimensional variety B over k, a codimension-one point b, an identification of the completion of the DVR R=O_{B,b} with K's valuation ring, and a projective variety over k(B) whose base change is X. Perfectness is required of k; it is not in general a statement that the residue field of K is perfect.

Theorem 8.2 of [G] proves continuity and uniform model approximation of envelopes for every closed (1,1)-form with ample de Rham class on such a smooth n-dimensional X, assuming resolution over the perfect field k in dimension d+n. It does not require that the chosen ample class itself descend to the initially chosen k(B)-variety. Its proof handles that issue at the level of model envelopes; no unbounded base-change theorem is inferred here.

Section 9 of [G] adds embedded resolution in dimension d+n. Its assumptions are exactly (A1) geometric origin over a perfect field k of characteristic p>0, (A2) resolution, and (A3) embedded resolution. It proves cofinality of projective SNC models, transfers [S] sections 1--7 and [B] sections 3--6, proves monotone regularization in Corollary 9.1, and proves orthogonality in Theorem 9.2. Its stated equation theorem, Theorem 9.3, still requires support on a projective SNC skeleton. We do not attribute the arbitrary-support theorem below to Theorem 9.3.

Definitions 6.1 and 6.2 in [G] mean the following. Resolution is a projective morphism from a regular variety to each quasi-projective variety of the specified dimension, isomorphic over its regular locus. Embedded resolution is a projective morphism between regular quasi-projective varieties, isomorphic outside the prescribed proper closed subset, with its inverse image supported on a normal crossing divisor. Theorem 6.3 states both in dimension three over any perfect field, citing Cossart--Piltant. Accordingly, Corollary 8.3 and section 9 explicitly make the n=2, d=1 case unconditional. We use this published theorem with this exact dimension check; the separately cited Cossart--Piltant papers were not among the supplied caches.

[M] Boucksom--Jonsson, *Measures of finite energy in pluripotential theory: a synthetic approach*, arXiv:2307.01697v1. It treats model/test potentials and finite-energy measures in a synthetic intersection framework. We use Theorem 1.33, Proposition 2.2, Theorem 2.23, and Lemma 2.25. Its measure completion theorem is not used to manufacture an unbounded solution.

[T] Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, arXiv:1801.08229v4. Theorem 12.9 includes smooth varieties of dimension at most two in positive characteristic, but its field has trivial valuation. It is not applied to K here. Its Proposition 9.19 and Theorem 12.8 provide a useful comparison with the variational argument, whose nontrivial-valued application is proved explicitly below.

The remaining caches give no indispensable equation input to this proof. ArXiv:1805.01016v3 is Boucksom--Eriksson's *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*. Pille--Schneider arXiv:2209.04879v2, Remark 4.4, distinguishes defining E1 over arbitrary fields from extending its operator; its literal wording says characteristic zero at the discrete endpoint. Gubler--Rabinoff arXiv:2506.13548v2 explicitly puts regularization and Monge-Ampere constructions outside its subject. Thuillier's thesis is a curve theory. The supplied Berkovich 1993 PDF is the etale-cohomology paper, not the 1990 book. Chambert-Loir--Ducros arXiv:1204.6277v2 is the July 2025 version concerning forms and currents; no global BFJ E1 surjectivity theorem is inferred from it.

## 2. Main concrete theorem and the conditional higher-dimensional range

**Theorem.** Let k be a perfect field of characteristic p>0, let B be a normal integral curve over k, let b be a closed point, let F=k(B), and let K be the completion of F at b with a nontrivial discrete absolute value. Let Y be a smooth geometrically integral projective surface over F and let X=Y times_F K. Let L be any ample line bundle on X. Choose a semipositive model reference metric on L and put theta equal to its curvature. Write V=(L^2)>0.

There is an approximation-independent genuine mixed Monge-Ampere operator on E1(X,theta), whose diagonal has raw total mass V. For every positive Radon measure mu on X analytified with mu(X)=V and finite dual energy as defined in section 5, there is phi in E1 with raw MA_theta(phi)=mu. It is unique modulo additive real constants. There is no assumption that mu is supported on a skeleton or is invariant under a torus. Continuity of the solution is not claimed.

The same proof applies to a smooth geometrically integral projective n-fold of geometric origin from a d-dimensional normal variety over a perfect characteristic-p field, provided BOTH resolution in Definition 6.1 and embedded resolution in Definition 6.2 of [G] hold in dimension d+n. This is a conditional range when these premises are not established; it does not count as resolving them. The concrete surface theorem above has d+n=3 and uses the proved case in [G], Theorem 6.3.

Here and below the analytic space is always the actual X over the nontrivially valued K. No theorem over a trivial valuation is substituted for it. The surface field has residue field finite over k, hence of characteristic p, and also has characteristic p. A field with characteristic zero and residue characteristic p is excluded by these hypotheses.

## 3. Replacement of each geometric input

Fix one of the ranges in section 2. We check the published inputs before the analytic argument.

**Reference and positivity.** A sufficiently high power of the ample L embeds X into projective space. The closure over the valuation ring, with O(1), is a projective model of that power. Resolving or taking a dominating SNC model is a modification with unchanged generic fiber. Pulling O(1) back preserves nefness by the projection formula on special-fiber curves. Its pullback need not be ample on that model, and no such assertion is needed. Taking the metric's root gives a semipositive model reference metric on the original L. Thus the positivity datum and the raw mass V remain the original ample polarization and its generic-fiber intersection degree.

**Regular and SNC models.** Proposition 5.2 of [G] first dominates any valuation-ring model by the completion of an R-model; its vertical blowups descend because their ideals contain a power of the uniformizer. One spreads the R-model to the d-dimensional B. Resolution in dimension d+n produces a regular projective model while keeping the smooth generic fiber. Embedded resolution applied to the bad fibers makes their support normal crossing. Section 9 of [G] checks that completion preserves regularity and strict normal crossing support. This is an application to models, not an alteration of X, and does not assume descent of unbounded potentials, energies, or measures through another variety.

**Compactness.** With these projective SNC models cofinal, [G] transfers [S] sections 1--7. Define PSH(X,theta) by the usc, retraction-majorization, and model-approximation conditions on each SNC dual complex, as in [S], Definition 7.1. Such functions are determined by their divisorial values; they are finite and continuous on each dual complex. Equip PSH with uniform convergence on each dual complex, called the weak potential topology. The set with sup phi=0 is compact; sup and integration against every fixed model Monge-Ampere measure are continuous. Indeed, a model measure has finite divisorial support, and those evaluations are continuous. These are [S], Corollary 7.7 and Theorem 7.10, with the transfer explicitly supplied in [G], section 9.

**Test-ideal replacement for envelope regularity.** On the smooth characteristic-p spread-out variety, [G] uses asymptotic test ideals instead of multiplier ideals. The body Theorem 4.6 assumes E-lambda D is nef, a point checked visually on PDF page 15; we do not use the differently ordered displayed condition in introductory Theorem 1.3. In Theorem 7.3 the base ideals a_m and asymptotic test ideals b_m satisfy a_m contained in b_m, b_ml contained in b_m^l, and A^m0 tensor L^m tensor b_m is globally generated uniformly in m. The last property follows by taking E=mD and lambda=m in Theorem 4.6, so E-lambda D=0, on a variety of total dimension d+n. Its global-generation threshold is that total dimension plus one, not merely n+1 for the generic fiber.

After arranging an ample extension A=L-E with E vertical and effective, these properties give

$$
\phi_m\leq P_\theta(0)\leq\frac{m}{m-m_0}\phi_m+
\frac{m_0}{m-m_0}\phi_E\qquad(m\gg1),
\quad \phi_m=m^{-1}\log|a_m|.
$$

This is the base-ideal estimate in [S], Theorem 8.5, using exactly the replacement properties proved in [G], Theorem 7.3. Both the bounded correction and a fixed lower bound for the phi_m give uniform convergence. Regular ample extensions are obtained in [G], Lemma 7.5, using semi-factorial models and resolution, rather than assuming that a resolution pulls ample bundles back to ample bundles. Descent of model functions, the envelope translation identity, the ddc lemma, and the envelope-only finite-normal-extension argument in [G], section 8 then yield Theorem 8.2 for the original X and any ample theta. These steps are part of the published envelope theorem; no new finite-energy base change is used here.

**Regularization, orthogonality, and differentiation.** Corollary 9.1 of [G] gives decreasing model approximation of every psh potential. Section 9 explicitly carries over the bounded operator and [B] sections 4--6. It also allows decreasing sequences, corresponding to Proposition 4.5 in the actual supplied [B] v1. Theorem 9.2 of [G] gives

$$
\int (f-P_\theta f)\,\mathrm{MA}_\theta(P_\theta f)=0\qquad(f\in C^0(X)).
$$

With continuous envelopes and this orthogonality, the proof of [B], Theorem 7.2 applies. Its proof uses monotone regularization, integration by parts, and concavity; the characteristic-zero orthogonality proof in [B], Appendix A is replaced entirely by [G], Theorem 9.2. Corollary 7.3 extends the envelope derivative to E1 by decreasing approximation. All applications take place on X itself.

## 4. The genuine E1 operator, mass, and comparison

We now keep n in the notation. For a bounded psh potential u let the raw mixed operator be the positive Radon measure constructed by [B], Theorem 3.1, of mass V. On model potentials it is the usual intersection-theoretic Chambert-Loir measure. Symmetry, integration by parts, and continuity along decreasing bounded model approximations characterize it uniquely. Thus the bounded definition is independent of the chosen approximation. [G], section 9 explicitly transfers this theorem.

For bounded u define raw energy and its normalized version by

$$
\mathcal E(u)=\frac1{n+1}\sum_{j=0}^n
\int u\,(\theta+dd^cu)^j\wedge\theta^{n-j},\qquad
e(u)=V^{-1}\mathcal E(u).
$$

For general psh u extend e as the infimum of e(v) over psh model v dominating u. Proposition 6.2 of [B] makes e concave, increasing, weakly upper semicontinuous, and continuous along decreasing nets, with e(u+c)=e(u)+c. Define

$$
\mathcal E^1(X,\theta)=\{u\in\mathrm{PSH}(X,\theta):e(u)>-\infty\}.
$$

For u in E1 set u_t=max(u,-t), after any constant shift needed to have u<=0, and define

$$
\mathrm{MA}_\theta(u)=\lim_{t\to\infty}
\mathbf1_{\{u>-t\}}\mathrm{MA}_\theta(u_t),\qquad
m(u)=V^{-1}\mathrm{MA}_\theta(u).
$$

Bounded locality makes the restricted measures increasing and compatible as t changes: on {u>-t}, the operators of u_s and u_t agree for s>t. Their increasing limit is a Radon measure. Changing the additive normalization only changes truncation thresholds and leaves that limit unchanged. This is [B], Definition 6.4, now justified by the transferred bounded operator and locality.

Here is the full-mass estimate, rather than an assumption of mass preservation. The energy difference formula for bounded potentials gives

$$
t\,m(u_t)\{u\leq-t\}
\leq2(n+1)\bigl(e(u_{t/2})-e(u_t)\bigr)\longrightarrow0.
$$

Indeed, u_{t/2}-u_t equals t/2 on {u<=-t}, and its integral against m(u_t), divided by n+1, is one of the nonnegative terms in that difference formula. Decreasing energy continuity makes the right side tend to zero. Thus MA_theta(u) has exactly raw mass V, places no mass on pluripolar sets, and is the weak limit of MA_theta(u_t). This reconstructs [B], Lemma 6.7 with the mass convention explicit.

The corresponding tail bound, for any continuous model test f, is

$$
\left|\int f\,m(u_t)-\int f\,m(u)\right|
\leq \frac{2(n+1)|e(u)|}{t}\,\|f\|_\infty\quad(u\leq0).
$$

Together with bounded decreasing continuity it proves [B], Proposition 6.9: every decreasing E1 approximation to u has operators converging to m(u). Hence no choice of a decreasing model sequence defines a different operator. These tail and monotone-continuity statements are mathematical estimates, not finite computational observations.

For mixed E1 potentials, simultaneously approximate each by decreasing bounded or model potentials. The diagonal operator of every convex combination converges by the preceding result. Polarization determines all mixed coefficients from finitely many such diagonal values. The resulting mixed coefficients are limits of positive measures of mass V, and are independent of all approximations. This constructs the genuine mixed operator; positivity and mass are inherited from the bounded mixed construction. Mixed measures integrate E1 potentials: Lemma 6.10 of [B], applied to a convex average and the positive terms in its Monge-Ampere expansion, bounds these integrals by finite energies.

For u,v in E1 the locality and comparison formulas are

$$
\mathbf1_{\{u>v\}}m(\max(u,v))=\mathbf1_{\{u>v\}}m(u),\qquad
\int_{\{u<v\}}m(v)\leq\int_{\{u<v\}}m(u).
$$

To see that these are the correct unbounded statements, apply bounded locality to the truncations on {u_t>v_t}. On that set u>-t, so the nonpluripolar measures agree with their truncations. Let t increase. The discarded terms lie in poles of u or v, which carry no mass, and full mass turns locality of max into comparison. This is the proof of [B], Proposition 6.11 and contains no characteristic-zero ideal input.

Energy differentiation retains the actual operator:

$$
\left.\frac{d}{dt}\right|_{0+} e((1-t)u+tv)=\int(v-u)m(u).
$$

This follows by the bounded polynomial energy formula, decreasing approximations, mixed integrability, and the tail estimate; it is [B], Proposition 6.12. The envelope derivative needed later is the stronger two-sided identity

$$
\left.\frac{d}{dt}\right|_0 e(P_\theta(u+tf))=\int f\,m(u)
\qquad(u\in\mathcal E^1,\ f\in C^0(X)).
$$

In particular P_theta(u+tf) lies in E1, since it lies between u-|t| norm(f) and u+|t| norm(f). For decreasing model u_j to u the envelopes P_theta(u_j+tf) decrease to P_theta(u+tf): their limit is psh, is below u+tf, and dominates that envelope. Decreasing energy/operator continuity and dominated convergence in the integrated continuous-envelope derivative yield the identity in [B], Corollary 7.3. Its prerequisites are exactly the inputs checked in section 3; no skeleton support of a target measure is used in this passage.

## 5. Exact finite-dual-energy measure condition

Let D be the real linear span of model functions and D_theta its psh subset. Rational model psh functions suffice in every supremum below. For clarity, the real span allows direct use of [M]. On a common model one can perturb a psh real model class toward a relatively ample representative of the same generic ample class, then approximate its vertical coefficients rationally while remaining ample; letting the perturbation decrease gives uniform approximation. The existence of such a representative is [S], Proposition 5.2, transferred by [G]. This also checks the real/rational model convention without changing L.

For a positive Radon measure mu with raw mass V put nu=mu/V, and impose

$$
\mathcal E^*_\theta(\mu):=
\sup_{v\in D_\theta}\left(\mathcal E(v)-\int v\,d\mu\right)<+\infty.
$$

Equivalently, in the normalized notation used for the proof,

$$
A=e^*(\nu):=\sup_{v\in D_\theta}\left(e(v)-\int v\,d\nu\right)<+\infty,
\qquad\mathcal E^*_\theta(\mu)=VA.
$$

Only the entire measure of mass V is divided by V. No restriction of mu to a subset is renormalized. Constants cancel because the mass condition is exact, and v=0 shows A>=0.

This is also the same supremum over all E1 potentials. To prove the indispensable integrability passage, take v_j decreasing model to u in E1. Since v_j are uniformly bounded above and

$$
\int v_j\,d\nu\geq e(v_j)-A\geq e(u)-A,
$$

monotone convergence proves u in L1(nu). Decreasing continuity of e and of the integrals gives

$$
e(u)-\int u\,d\nu=\lim_j\left(e(v_j)-\int v_j\,d\nu\right)\leq A.
$$

Thus model and E1 definitions of the dual energy coincide. We use this exact condition, not an unproved assertion that arbitrary Radon measures are allowed.

Conversely, m(u) has finite dual energy for every u in E1. Mixed integrability and the tangent inequality from concavity give

$$
e(v)\leq e(u)+\int(v-u)m(u),\qquad
e^*(m(u))=e(u)-\int u\,m(u)<\infty.
$$

The supremum equality follows by taking v=u in the already proved E1 form of the supremum. Hence the image and target have the stated finite-energy meaning.

## 6. Checking the synthetic source application

The data for [M] are the actual compact X analytified, D above, Z the direct limit of model numerical (1,1)-classes, dd^c on vertical divisors, and the usual model intersection measure. Symmetry and seminegativity of the pairing integral(f dd^c g wedge T) for nef T follow from [B], Propositions 2.20--2.21, in the setting transferred by [G]. The former is the intersection projection/integration-by-parts identity; the latter is the vertical Hodge inequality and its Cauchy--Schwarz consequence. One can also check the latter directly with the graph identity in section 9: replace A^{n-1} there by any mixed product of n-1 nef classes on a common regular SNC model. Its off-diagonal weights are nonnegative, since they are intersections of nef classes on effective special-fiber cycles. That identity makes every vertical square nonpositive; polarization gives the stated symmetric seminegative pairing and Cauchy--Schwarz. This argument works in every residue characteristic. D contains real constants and is dense in C0, and dd^c vanishes on constants. Nef forms span Z, since on a sufficiently high common model an ample representative of the same ample generic class dominates any finite collection of classes. The order is nice in [M]'s terminology: on each finite-dimensional space of forms a common model determines the classes, and nefness is the closed collection of nonnegative-degree inequalities on its proper special-fiber curves; pullback preserves and detects nefness, as in [M], section 1.2.2. Thus the positive cone is closed in the finest vector-space topology. [M], section 1.3.2 and [S], Proposition 5.2 identify the positive-class cone at this datum with the preimage of the ample cone. Thus theta is a semipositive form with positive class and volume V, which also checks that the symmetric n-linear measure pairing is nonzero.

One must check [M]'s orthogonality definition, which is stronger in wording than the integral at a continuous envelope. Its Definition 2.15 concerns the increasing directed net of tests v<f. Tests admit maxima in its Definition 2.11: rational psh model functions are closed under max, and uniform rational approximation with a small constant margin gives the assertion for real tests. Their supremum is P_theta(f). By continuity of that envelope and Dini's theorem for nets, this increasing net converges uniformly to P_theta(f). Uniform model-operator continuity then gives

$$
\lim_{v\in D_\theta,\ v<f}\int(f-v)m(v)
=\int(f-P_\theta f)m(P_\theta f)=0.
$$

The final equality is [G], Theorem 9.2. Thus [M], Definition 2.15 really is verified on this space, and Theorem 2.23 and Lemma 2.25 can be applied. No assumption about completion of the unbounded potential space has been inserted.

Set m_0=m(0) and, for tests, define

$$
J(u,v)=e(u)-e(v)+\int(v-u)m(u),\qquad
J(u)=J(0,u)=\int u\,m_0-e(u),
$$

and define the maximizing defect for the fixed target nu by

$$
a_\nu(v)=A-e(v)+\int v\,d\nu\geq0.
$$

Proposition 2.2 of [M] gives quasi-symmetry of J and the defect bound

$$
J(u,v)\leq C_n\bigl(a_\nu(u)+a_\nu(v)\bigr),\qquad
J(v)\leq C_n\bigl(A+a_\nu(v)\bigr)
$$

for tests (the second uses u=0). This can be checked directly: uniform concavity in [M], Theorem 1.33, applied to the midpoint, gives a lower bound for the sum of the two defects; the linear measure term cancels. We shall only need this test-level bound.

Theorem 2.23 and Lemma 2.25 of [M] then supply a maximizing sequence r_j of tests and, whenever J(v), J(r_j), and A are bounded by a fixed R, the estimate

$$
\left|\int v\,(\nu-m(r_j))\right|
\leq C_{n,R}\,a_\nu(r_j)^{1/2}.
$$

This is equation (2.27) with the other potential equal to zero. The theorem's model density is used to obtain this uniform integration estimate. We do not assume that its limiting measure is realized by an E1 potential.

## 7. New passage: integration is continuous on energy-bounded potential sets

By compactness from section 3, integration against m_0 is bounded on normalized PSH. Hence there exists T finite such that

$$
-T\leq\int u\,m_0\leq0\quad\text{whenever }\sup u=0.
$$

For C>0 the set

$$
K_C=\{u\in\mathrm{PSH}(X,\theta):\sup u=0,\ e(u)\geq-C\}
$$

is weakly compact, since sup is continuous and e is usc. Every member is in E1 and has 0<=J(u)<=C.

Choose maximizing tests r_j for nu; their J are bounded by the preceding defect estimate. Extend the last estimate of section 6 from tests to any u in K_C as follows. Choose a decreasing model sequence u_l to u. Both e(u_l) and integral(u_l m_0) tend to their finite limits, so J(u_l) tends to J(u) and is eventually bounded by C+1. Section 5 already proves u in L1(nu); model measures m(r_j) integrate u because of their divisorial support (or mixed integrability). Monotone convergence of both integrals therefore lets l tend to infinity in the test estimate. For a fixed common R this gives

$$
\sup_{u\in K_C}\left|\int u\,d\nu-\int u\,m(r_j)\right|
\leq C_{n,R}a_\nu(r_j)^{1/2}\longrightarrow0.
$$

Each functional u maps to integral(u m(r_j)) is weakly continuous, since m(r_j) is a fixed finite divisorial measure. Their uniform convergence on K_C proves that u maps to integral(u dnu) is weakly continuous on K_C. This is the needed actual potential-space argument. It is not a consequence of completeness of measures alone, and uses the full measure nu throughout.

## 8. New passage: actual variational attainment for arbitrary support

Normalize a model maximizing sequence v_i by sup v_i=0; arbitrary real constant shifts are allowed and leave its defect unchanged. The defect estimate bounds J(v_i). Since

$$
-e(v_i)=J(v_i)-\int v_i\,m_0\leq J(v_i)+T,
$$

all sufficiently late v_i lie in one K_C. Compactness yields a weakly converging subnet with limit u in K_C. No sequential compactness of an uncountable collection of models is assumed.

The integral continuity just proved and upper semicontinuity of energy give

$$
e(u)-\int u\,d\nu\geq
\limsup_i\left(e(v_i)-\int v_i\,d\nu\right)=A.
$$

Section 5 gives the reverse inequality. Thus u is an actual E1 maximizer. It lives on X, with no support restriction on nu.

For f continuous and t real put u_t=P_theta(u+tf). Then u_t is in E1 and u_t<=u+tf. Define

$$
h(t)=e(u_t)-\int(u+tf)\,d\nu.
$$

Positivity of nu and maximality imply h(t)<=e(u_t)-integral(u_t dnu)<=A=h(0). The envelope derivative in section 4 gives

$$
0=h'(0)=\int f\,m(u)-\int f\,d\nu.
$$

Equality for all continuous f proves m(u)=nu and hence raw MA_theta(u)=mu. This proves existence and realizes the target as the genuine operator, rather than assigning an inverse measure by definition.

## 9. Uniqueness and the characteristic-independent strict kernel step

Let u,v in E1 have the same operator. Mixed integrability makes the following expression meaningful:

$$
S=\int(u-v)\,(m(v)-m(u))=0.
$$

The proof of [B], Proposition 8.2, using its mixed polarization, integration by parts, and repeated Cauchy--Schwarz, gives, for any semipositive model reference eta in the same ample class,

$$
0\leq-\int (u-v)dd^c(u-v)\wedge\eta^{n-1}
\leq C_{u,v,\eta}S^{2^{1-n}}=0.
$$

In applying it after a reference change eta=theta+dd^c g, one uses u-g and v-g. For model or bounded approximants the raw measures coincide by the curvature identity eta+dd^c(u-g)=theta+dd^c u. Decreasing operator continuity proves the same identity for E1. The cocycle identity for model energies makes u-g and v-g finite energy: e_eta(u-g)=e_theta(u)-e_theta(g). This cocycle is the bounded mixed energy difference formula followed by decreasing approximation with the fixed bounded model g. Thus reference change is checked, not an assumption about descent through a different variety. The estimate's induction uses the nonnegative mixed norms of u-v, replacing one eta factor at a time by eta_u-dd^c(u-g). The Cauchy--Schwarz cross term bounds the next norm by a constant times the square root of the previous one; the initial mixed norms sum to S. Iterating n-1 times yields the displayed exponent. All cross energies are finite by mixed integrability. No multiplier or test ideal enters this calculus.

For the main surface theorem the vanishing needed above has an especially short independent verification. Write f=u-v, u'=u-g, and eta_u=eta+dd^c u', eta_v=eta+dd^c(v-g). Set N_T(f)=-integral(f dd^c f wedge T). Then

$$
N_{\eta_u}(f)+N_{\eta_v}(f)=VS=0.
$$

Both terms are nonnegative. Cauchy--Schwarz with f and u' for each of T=eta_u, eta_v therefore makes integral(f dd^c u' wedge T) vanish. Subtracting these two identities, using dd^c f=eta_u-eta_v, gives integral(f dd^c f wedge dd^c u')=0. Since eta=eta_u-dd^c u', it follows that N_eta(f)=0. Mixed E1 integrability makes every term finite, so no limiting product has been silently interchanged. This proves the requisite zero norm in dimension two without depending on a higher-dimensional estimate.

For completeness, we prove the final strict kernel assertion instead of leaving it as a characteristic-zero Hodge premise. Fix a sufficiently high regular SNC model determining eta and a relatively ample rational representative A of the same generic class; such an eta is obtainable after a model reference change by [S], Proposition 5.2. Write its special fiber as sum b_i E_i, and let w_ij=(E_i.E_j.A^{n-1}) for i not equal j. The effective intersection cycle and relative ampleness imply w_ij>=0, strictly positive when E_i meets E_j. Since the total fiber is principal, any vertical real divisor D=sum a_i E_i satisfies

$$
D^2 A^{n-1}=-\sum_{i<j}b_i b_j w_{ij}
\left(\frac{a_i}{b_i}-\frac{a_j}{b_j}\right)^2.
$$

This follows by expanding D squared and using (sum b_i E_i).E_j.A^{n-1}=0 to eliminate diagonal terms. The special-fiber intersection graph is connected: the model is normal and proper with geometrically integral generic fiber, so its global functions are the valuation ring (properness makes them integral, and the valuation ring is integrally closed); Stein factorization then gives connected fibers. Therefore equality D^2 A^{n-1}=0 forces a_i/b_i to be constant across all components, in every residue characteristic.

Let lambda=-log(abs(pi))>0 for a uniformizer. Set a_i=b_i(u-v)(x_i)/lambda at the divisorial point x_i of E_i, and let g_D be the model function of D. It equals u-v at all these vertices. Cauchy--Schwarz and the vanishing norm established above give integral((u-v) dd^c g_D wedge eta^{n-1})=0. This measure has support at the vertices, and integration by parts for model intersections identifies that integral with lambda D^2 A^{n-1}. Hence u-v has one constant value on those vertices.

To align these constants across refinements, keep a fixed divisorial point as an anchor and work with SNC models dominating a model containing it. Every other divisorial point occurs on such a dominating model by cofinality. The preceding argument shows that u-v has the anchor's value at every divisorial point. Since psh functions are determined by divisorial values, u=v+c on all of X. Their metrics differ by the positive factor exp(-c). If sup u=sup v=0 then c=0. This avoids the unjustified inference that separately changing the reference preserves equality of the two normalized suprema.

## 10. Coverage and concrete remaining obligations

The surface theorem covers arbitrary-support finite-dual-energy measures on general smooth geometrically integral projective surfaces over completions of function fields of curves over perfect characteristic-p fields. It retains projectivity, smoothness, an ample line bundle, algebraizability, nontrivial discrete valuation, and geometric origin. It has an unconditional resolution check in dimension three; it does not require toric geometry or a projective-line reduction. The operator, full mass, comparison, differentiation, and uniqueness are genuine finite-energy statements. The new deductions beyond [G], Theorem 9.3 are the uniform integration/attainment argument removing skeleton support within that source's geometry, and the explicit characteristic-independent vertical kernel verification. We do not claim these deductions are new to the published literature.

The complete original P16.3 still requires the following, under its retained smooth projective ample discretely valued setting.

First, mixed-characteristic fields, including characteristic-zero fields with positive residue characteristic, are not handled. One needs cofinal sufficiently regular models or proved substitutes, envelope regularity or an alternative, and compatible unbounded operator, differentiation, and comparison. Test ideals on the equal-characteristic spread-out smooth variety supply none of these mixed-characteristic replacements by themselves.

Second, arbitrary higher dimension in equal characteristic is not handled unconditionally. The conditional range above still assumes both specified forms of resolution in dimension d+n. Alterations, or one good model of X, do not prove that every model is dominated by the required regular/SNC models, nor do they prove descent of the E1 theory.

Third, general smooth projective varieties over complete discretely valued characteristic-p fields need not be covered by the geometric-origin hypothesis in [G], Definition 8.1. No claim is made that every such X, or its model-envelope theory, can be realized by an allowed d-dimensional algebraic family. Removing this hypothesis requires replacement envelope/regularization and compactness inputs on the original X.

These are remaining obligations of the original atom; they are not reassigned to a narrower reformulation. The eleven-source audit does not assert an exhaustive survey of all literature available in October 2026. The proper status is partial and candidate=false.

## 11. Evidence, source provenance, and rerun instructions

The preserved inputs are `input.json`, byte-identical `input-original.json`, decoded `assignment-original.txt`, and `task-original.json`. SHA256 of the input bytes is `551c1e4204b90a78f88201721de1c4b41a09bfd8f3c03cb997e9eb72d457c120`.

The rerunnable source audit is `python3 audit_sources.py`. It verifies all eleven supplied PDFs, text extracts, and supplied abstract files against their given hashes. Its actual result was eleven sources verified, thirty-three literal extract files saved, and input-original byte identity true. `source-extracts/source-provenance.json` retains source versions, filenames, actual hashes, literal published passages, page/line locations, exact application checks, and limitations. The original sources remain read-only. PDF pages 15 and 22 of [G] were rendered and visually checked; the images are retained there. Source-provenance records the body/introductory test-ideal condition discrepancy and the BFJ version numbering difference rather than silently correcting the extracts.

`P16.3-paper.tex` is a standalone TeX rendition containing this full argument. Run `python3 build_paper.py` to regenerate it and execute two actual pdflatex passes. Both stdout/stderr diagnostic streams and the distinct TeX logs are saved under `build/`; `build/build-results.json` records commands and return codes. `environment.json` records the actual Python/platform/TeX-tool details. No software was installed, no external messages or model workers were used, and no heavy computation was launched.

The mathematical evidence is the published extracts and the deductions above. The finite checks establish provenance and reproducibility, not mathematical correctness. `status.json` records exactly the required five fields and keeps all concrete original gaps open.


# All actual native canonical notes

[
  {
    "id": "n1",
    "summary": "GJKM 1712.00980v3 supplies equal-characteristic-p envelope and model replacements under geometric-origin and resolution hypotheses; surfaces over curve-function-field completions are unconditional. Its stated equation theorem retains SNC-skeleton support and does not cover mixed characteristic.",
    "detailedSummary": "The exact PDF requires a complete nontrivially discretely valued characteristic-p field and geometric origin over a perfect characteristic-p field. Envelope continuity requires resolution in total dimension d+n; the transferred SNC-based pluripotential theory additionally requires embedded resolution. GJKM Theorem 6.3 states both resolution inputs in dimension three, making n=2,d=1 unconditional. Section 9 explicitly transfers BFJ bounded operators, locality, comparison, and energy theory, including the finite-energy construction in section 6. Theorem 9.3 itself still assumes skeleton-supported measures. The supplied BFJ equation PDF is v1 with algebraizability and support restrictions; the Boucksom–Jonsson positive-characteristic surface endpoint is trivially valued.",
    "text": "This is a primary-source scope audit, not a complete solution of P16.3.\n\nGubler–Jell–Künnemann–Martin, with appendix authors Burgos Gil and Sombra, arXiv:1712.00980v3, is the exact supplied PDF. Its SHA256 is 6c506c3ee23c6e36900a59f3f3fba1f26c4b22708756324f89af8668ed5771b6. Starting in section 7, K is complete discretely valued and char(K)=p>0. Thus the higher-dimensional test-ideal results concern equal characteristic, not char(K)=0 with residue characteristic p.\n\nDefinition 8.1 requires a normal d-dimensional variety B over k, a codimension-one point b, K° identified with the completion of R=O_{B,b}, and a projective k(B)-variety whose base change is X. The field k must be perfect. This does not generally imply perfectness of K's residue field when d>1.\n\nTheorem 8.2 assumes X smooth projective of dimension n and resolution over k in dimension d+n. It proves continuous envelopes, uniformly approximable by psh model functions, for every closed (1,1)-form with ample de Rham class. The chosen ample class need not descend to the initially chosen k(B)-variety; the published proof handles this at the model-envelope level.\n\nSection 9 additionally assumes embedded resolution in dimension d+n. Definitions 6.1 and 6.2 specify projective regular resolutions, preserving the regular locus, and projective embedded resolutions between regular varieties, preserving the complement of the prescribed subset. Proposition 5.2 and section 9 use these to obtain cofinal projective SNC models, preserving the original smooth generic fiber. Theorem 6.3 states both resolution results in dimension three over perfect fields, citing Cossart–Piltant. Consequently n=2,d=1 is unconditional in this source. The separately cited Cossart–Piltant papers were not independently inspected.\n\nSection 9 explicitly transfers BFJ singular-metric sections 1–7 and equation-paper sections 3–6. These provide compactness, the bounded operator, locality, energy, the nonpluripolar E1 operator, full mass, and comparison. Corollary 9.1 supplies decreasing model regularization, and Theorem 9.2 supplies orthogonality. Theorem 9.3, however, states existence and uniqueness only for positive Radon measures supported on a projective SNC skeleton, with raw mass equal to the polarization degree.\n\nThe test-ideal replacement uses subadditivity and uniform generation. PDF page 15 was visually checked: body Theorem 4.6 requires E−λD nef. The differently ordered displayed condition in introductory Theorem 1.3 is not used. In Theorem 7.3 the application E=mD, λ=m makes this difference zero. The smooth spread-out variety has dimension d+n, which controls the global-generation threshold.\n\nVersion checks matter. The supplied 1201.0188 PDF is actual v1, with residue characteristic zero, algebraizability, and SNC-dual-complex support in Theorem A. Its sequence regularization is Proposition 4.5, whereas GJKM cites later numbering. The supplied 1201.0187 is v2, whose compactness theorem is Theorem 7.10. ArXiv:1805.01016v3 is Boucksom–Eriksson's Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. ArXiv:1801.08229v4 is a trivial-valuation theory; its positive-characteristic surface Theorem 12.9 cannot simply be applied to K=k((t)). ArXiv:2307.01697v1 studies finite-energy measures and model/test potentials; completion of measures alone does not establish E1 surjectivity.\n\nLiteral statements and proof passages, exact versions, hashes, and application checks are retained in source-extracts/source-provenance.json. Rerun: python3 audit_sources.py. All eleven supplied source hashes were verified, and 33 literal extracts were retained. This audit is confined to the supplied sources and is not an exhaustive contemporary literature survey.\n\nArtifacts: /workspace/research/campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs/artifacts/codex-tSmFOo",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Draft proof of genuine E1 existence and uniqueness for arbitrary-support finite-dual-energy measures on general smooth projective surfaces of geometric origin in nontrivially valued equal characteristic p. This narrower theorem remains partial for original P16.3.",
    "detailedSummary": "Let K be the completion at a closed point of a normal curve's function field over a perfect characteristic-p field, and let X be the base change of a smooth geometrically integral projective surface. For any ample L, the genuine nonpluripolar E1 operator has raw mass V=(L²). Every positive Radon measure μ of mass V satisfying sup_v(E(v)−∫v dμ)<∞ has an E1 solution, unique modulo constants, without support or invariance restrictions. The new passage extends synthetic uniform integration estimates to energy-bounded E1 sets, proving actual variational attainment using GJKM compactness and differentiation. Uniqueness includes an explicit characteristic-independent vertical intersection kernel argument. This is a deduction from published inputs, not a claim of publication priority. Higher-dimensional geometric-origin cases retain both explicit resolution premises; mixed characteristic and unrestricted geometry remain outside the theorem.",
    "text": "The following is an unverified mathematical proof draft, with a concrete unconditional surface range. It does not claim the entire original P16.3.\n\nTHEOREM. Let k be perfect of characteristic p>0, B a normal integral curve over k, b a closed point, F=k(B), and K the completion of F at b with a nontrivial discrete absolute value. Let Y/F be a smooth geometrically integral projective surface and X=Y×F K. For any ample line bundle L on X, choose a semipositive model reference metric with curvature θ and put V=(L²)>0. There is an approximation-independent genuine mixed Monge–Ampère operator on E1(X,θ), of raw mass V. Every positive Radon measure μ on Xᵃⁿ with μ(Xᵃⁿ)=V and finite dual energy specified below admits an E1 solution, unique modulo additive constants. No skeleton support, torus invariance, or continuity of the solution is assumed.\n\nPublished geometric inputs are exactly those audited in n1. Here d+n=1+2=3, so GJKM Theorem 6.3 supplies both resolution inputs without an unproved premise. Its section 9 gives cofinal SNC models and transfers BFJ compactness and bounded/finite-energy calculus. Theorem 8.2 applies to any ample θ on this X, even when L does not descend to the original F-variety. Theorem 9.2 replaces the characteristic-zero orthogonality argument. No unbounded base-change or alteration descent is introduced.\n\nA reference metric exists: embed X using a sufficiently high power of L, take its projective closure over K°, and pull O(1) to a dominating SNC model. Pullback preserves nefness by the curve projection formula, although it need not preserve ampleness. Taking the metric's root retains the original L and generic degree V.\n\n1. Genuine operator and energy. The transferred BFJ Theorem 3.1 defines the bounded mixed operator by model intersections and decreasing approximation, with raw mass V and approximation independence. For bounded u set\nE(u)=(1/(n+1))Σ[j=0,…,n]∫u(θ+ddᶜu)^j∧θ^(n−j), and e(u)=E(u)/V.\nExtend e to psh u by the infimum over dominating psh model potentials. Transferred BFJ Proposition 6.2 gives concavity, monotonicity, weak upper semicontinuity, decreasing continuity, and e(u+c)=e(u)+c. Define E1={u psh:e(u)>−∞}.\n\nFor u≤0 set u_t=max(u,−t). Define the raw operator by\nMAθ(u)=lim[t→∞] 1_{u>−t} MAθ(u_t), and m(u)=MAθ(u)/V.\nBounded locality makes these restricted measures increasing and compatible. Their limit is Radon. A constant shift only changes truncation thresholds, so it does not change the operator.\n\nFull mass is proved, rather than assumed. The bounded energy difference formula gives\nt·m(u_t){u≤−t}≤2(n+1)(e(u_{t/2})−e(u_t))→0.\nIndeed u_{t/2}−u_t=t/2 on that set, and its integral against m(u_t), divided by n+1, is a nonnegative term of the energy difference. Decreasing continuity proves the limit. Thus MAθ(u) has exactly mass V and no pluripolar mass. The BFJ tail estimate\n|∫f m(u_t)−∫f m(u)|≤2(n+1)|e(u)|·||f||∞/t\nand bounded monotone continuity prove convergence along every decreasing E1 approximation. This establishes independence of model approximation as well as truncation.\n\nMixed E1 measures are obtained by simultaneous decreasing approximation and polarization: diagonal measures of all convex combinations converge, and finitely many diagonal values determine the mixed coefficients. The coefficients are limits of positive bounded mixed measures of mass V, hence positive, of mass V, and independent of choices. BFJ Lemma 6.10 and the positive expansion of the operator of a convex average give mixed E1 integrability.\n\nLocality and comparison extend to E1:\n1_{u>v}m(max(u,v))=1_{u>v}m(u), and ∫_{u<v}m(v)≤∫_{u<v}m(u).\nApply bounded locality on {u_t>v_t}, where the relevant nonpluripolar measures agree with their truncations, and let t increase. Discarded pole sets have zero mass. Full mass then turns locality of max into comparison. This is the characteristic-independent proof of transferred BFJ Proposition 6.11.\n\nTransferred BFJ Proposition 6.12 gives de((1−t)u+tv)/dt at 0+=∫(v−u)m(u). With GJKM orthogonality, BFJ Theorem 7.2 and Corollary 7.3 also give the stronger two-sided envelope derivative\nde(Pθ(u+tf))/dt at 0=∫f m(u)\nfor u∈E1 and continuous f. The hypotheses are checked: Pθ(u+tf) lies between u−|t|||f||∞ and u+|t|||f||∞, hence in E1; decreasing model u_j give decreasing envelopes converging to Pθ(u+tf). Decreasing energy/operator continuity and dominated convergence in the integrated continuous-envelope derivative extend the identity to u. Characteristic-zero multiplier ideals and BFJ's original orthogonality appendix are not used.\n\n2. Exact measure condition. Put ν=μ/V, dividing the entire measure, never a restriction. Let Dθ denote psh tests in the real span of model functions. Require\nE*θ(μ)=sup[v∈Dθ](E(v)−∫v dμ)<∞.\nEquivalently A=e*(ν)=sup[v∈Dθ](e(v)−∫v dν)<∞, with E*θ(μ)=VA. Constants cancel because the raw mass is V. Rational model tests give the same supremum: on a common sufficiently high model, perturb a real nef class toward an ample representative of the same generic class, approximate vertical coefficients rationally inside the ample cone, and let the perturbation tend to zero. GJKM transfers the BFJ positivity input furnishing that representative.\n\nFor u∈E1 take decreasing model v_j→u. The bound ∫v_j dν≥e(v_j)−A≥e(u)−A, together with a uniform upper bound, proves u∈L1(ν) by monotone convergence. Moreover e(u)−∫u dν≤A. Thus this is also the supremum over all E1 potentials. Conversely mixed integrability and concavity give e(v)≤e(u)+∫(v−u)m(u), so e*(m(u))=e(u)−∫u m(u)<∞. The image and target therefore have the actual finite-energy meaning.\n\n3. Synthetic application. Apply Boucksom–Jonsson arXiv:2307.01697v1 on the actual compact Berkovich space, with D the real span of model functions, Z the model numerical forms, and the usual intersection measures. D is dense, contains constants, and ddᶜ kills constants. Integration by parts is the model intersection identity. Seminegativity follows on a common regular SNC model from the vertical intersection formula in step 6 below, using arbitrary mixed nef classes in place of the ample product; its off-diagonal weights are nonnegative. Nef classes span Z, and on every finite-dimensional space their cone is closed by the nonnegative curve-degree inequalities. This checks the source's nice-order requirement. BFJ positivity, transferred by GJKM, verifies that θ has positive ample class; the n-linear pairing is nonzero since its volume is V.\n\nThe source's Definition 2.15 orthogonality also needs checking. Tests below f admit maxima through rational model maxima and uniform approximation with a strict constant margin. Their increasing directed net has supremum Pθ(f), continuous by GJKM. Dini convergence is uniform, so uniform operator continuity and GJKM Theorem 9.2 give\nlim[v<f]∫(f−v)m(v)=∫(f−Pθf)m(Pθf)=0.\nThus the synthetic theorem is applicable, without assuming completeness of unbounded potentials.\n\nWrite m₀=m(0), J(u,v)=e(u)−e(v)+∫(v−u)m(u), J(u)=∫u m₀−e(u), and aν(v)=A−e(v)+∫v dν. For tests, synthetic Theorem 1.33 and Proposition 2.2 give quasi-symmetry and\nJ(u,v)≤C_n(aν(u)+aν(v)), and J(v)≤C_n(A+aν(v)).\nThe first bound follows directly from uniform concavity at the midpoint: the linear target terms cancel. The second uses u=0.\n\nTheorem 2.23 and Lemma 2.25 give maximizing tests r_j with aν(r_j)→0 and bounded J(r_j), and equation (2.27), with the other potential zero, yields\n|∫v(ν−m(r_j))|≤C_{n,R} aν(r_j)^(1/2)\nwhenever J(v), J(r_j), and A have a common fixed bound. Only this model-level uniform integration estimate is used. Completion of measures is not used to infer surjectivity.\n\n4. New integration passage. Normalized PSH is compact in the topology of uniform convergence on each SNC dual complex. Integration against m₀ is continuous, since this measure has finite divisorial support. Hence −T≤∫u m₀≤0 for sup u=0 and a fixed finite T.\n\nThe sets K_C={u psh:sup u=0,e(u)≥−C} are compact by upper semicontinuity of e, and satisfy 0≤J(u)≤C. For u∈K_C choose decreasing model u_l→u. Both energy and its m₀ integral converge, so J(u_l) is eventually bounded by C+1. The integrability already proved permits monotone passage in the ν integral; m(r_j) also integrates u, since it has finite divisorial support. Passing l→∞ in the test estimate therefore gives\nsup[u∈K_C]|∫u dν−∫u m(r_j)|≤C_{n,R}aν(r_j)^(1/2)→0.\nEach functional ∫u m(r_j) is weakly continuous. Their uniform limit proves continuity of ∫u dν on K_C. This is the indispensable potential-space argument replacing skeleton support.\n\n5. Actual existence. Normalize maximizing tests v_i by sup v_i=0. Their J are bounded by the defect estimate, and −e(v_i)=J(v_i)−∫v_i m₀≤J(v_i)+T. They therefore lie eventually in one compact K_C. Take a weakly convergent subnet to u∈K_C, without assuming sequential compactness. Integral continuity and upper semicontinuity of energy yield e(u)−∫u dν≥limsup(e(v_i)−∫v_i dν)=A. The dual-energy bound gives equality.\n\nFor continuous f put u_t=Pθ(u+tf) and h(t)=e(u_t)−∫(u+tf)dν. Positivity and maximality imply h(t)≤e(u_t)−∫u_t dν≤A=h(0). The two-sided envelope derivative gives 0=h′(0)=∫f m(u)−∫f dν. Equality against all continuous tests proves m(u)=ν, hence raw MAθ(u)=μ. The actual E1 potential is constructed by variational attainment, not by defining an inverse measure.\n\n6. Uniqueness, including the strict kernel. Suppose m(u)=m(v), and set f=u−v. All following terms are finite by mixed E1 integrability. Model reference changes η=θ+ddᶜg are legitimate: bounded/model operators coincide after replacing u by u−g, and decreasing continuity proves this in E1. The energy cocycle eη(u−g)=eθ(u)−eθ(g) proves finite energy after reference change.\n\nFor a surface set η_u=η+ddᶜ(u−g), η_v=η+ddᶜ(v−g), and N_T(f)=−∫f ddᶜf∧T. Integration by parts gives N_{η_u}(f)+N_{η_v}(f)=V∫f(m(v)−m(u))=0. Each term is nonnegative. Cauchy–Schwarz with f and u−g therefore gives ∫f ddᶜ(u−g)∧η_u=∫f ddᶜ(u−g)∧η_v=0. Subtracting, and using ddᶜf=η_u−η_v, proves ∫f ddᶜf∧ddᶜ(u−g)=0. Thus N_η(f)=0.\n\nChoose a sufficiently high regular SNC model with a relatively ample rational representative A of the original generic ample class, obtained using the transferred BFJ positivity input. Write the special fiber as Σb_iE_i. For i≠j put w_ij=(E_i·E_j·A^(n−1)); these are nonnegative and strictly positive when the components meet. The principal-fiber relation eliminates diagonal terms and gives, for D=Σa_iE_i,\nD²·A^(n−1)=−Σ[i<j]b_i b_j w_ij(a_i/b_i−a_j/b_j)².\nThe intersection graph is connected: normal proper models with geometrically integral generic fiber have global functions K°, by integrality and integrally closedness; Stein factorization gives connected fibers. Hence equality forces a_i/b_i constant across components, in every residue characteristic.\n\nLet λ=−log|π| and a_i=b_i f(x_i)/λ at component divisorial points. The model function g_D equals f at these vertices. Cauchy–Schwarz and N_η(f)=0 give ∫f ddᶜg_D∧η^(n−1)=0, which the model intersection formula identifies with λD²·A^(n−1). Thus f has one value on all those vertices. Keep a fixed divisorial anchor while refining models; cofinality places every other divisorial point together with the anchor on a dominating model. The constants consequently agree. Psh determination by divisorial values gives u=v+c everywhere. Normalizing both suprema to zero gives c=0.\n\nThe same existence argument works for geometric-origin n-folds under BOTH resolution premises in dimension d+n. The higher-dimensional zero-norm estimate is the characteristic-independent repeated Cauchy–Schwarz proof of BFJ Proposition 8.2, with the same transferred mixed calculus; the strict kernel above applies unchanged. That range remains conditional when the resolution premises are unproved.\n\nThe complete argument and exact application checks are in P16.3-argument.md and the standalone P16.3-paper.tex. These are deductions from the sources, not a claim of literature priority or execution-verified mathematics. Mixed characteristic, unrestricted higher dimension, and removal of geometric origin remain original obligations.\n\nArtifacts: /workspace/research/campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs/artifacts/codex-tSmFOo",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Deliverables preserved and compiled twice successfully. Original P16.3 remains partial: mixed characteristic, unproved higher-dimensional resolution inputs, and unrestricted geometric origin are explicit gaps; candidate=false.",
    "detailedSummary": "The workspace contains byte-preserved inputs, the full Markdown proof, standalone TeX and an 11-page PDF, literal source extracts with provenance, environment and execution records, and both actual TeX diagnostic streams and logs. Artifact checks confirm eleven sources, 33 literal extracts, successful final compilation return codes [0,0], no overfull boxes, and exactly the required status fields. These finite checks establish reproducibility only. The final status is partial and does not promote the concrete equal-characteristic surface theorem to a solution of the unchanged original atom.",
    "text": "The implementation deliverables are complete, while the mathematical status of the original atom remains partial.\n\nFiles: input.json and byte-identical input-original.json; decoded assignment-original.txt and task-original.json; P16.3-argument.md containing the full argument and concrete gaps; standalone P16.3-paper.tex; build/P16.3-paper.pdf; source-extracts/source-provenance.json containing versions, hashes, literal published proof passages, locations, and application checks; environment.json; execution-record.json; artifact-checks.json; and artifact-manifest.json.\n\nRerun commands are python3 audit_sources.py, python3 build_paper.py, and python3 check_artifacts.py. The build script executes two actual pdflatex passes and saves their stdout, stderr, and separate TeX logs as build/pass1.stdout.txt, build/pass1.stderr.txt, build/pass1.tex.log and the corresponding pass2 files. Earlier builds remain under build/previous.\n\nObserved checks: input preservation and decoded-input equality passed; all eleven supplied sources matched their hashes; 33 literal extracts matched their source passages; final TeX return codes were [0,0]; the PDF has 11 pages; no overfull boxes remained. Final TeX SHA256: 08d29e4fb4af93aff797c3e825b66e28db1e6212372f1a6af3e5af361463a316. Final PDF SHA256: 5726e6388c0c096a5ff9f5e5fca89644c40d8811989d5e53a652a305cf743997. These observations do not verify mathematical correctness.\n\nstatus.json has exactly id,status,exact_result,proof_file,concrete_gaps, with status=partial. The remaining original obligations are: mixed-characteristic replacements for model regularity, envelopes, regularization, and compatible E1 calculus; unconditional higher-dimensional equal-characteristic theory where both specified resolution premises remain unproved; and compactness/envelope replacements or a proved realization passage outside GJKM geometric origin. No alteration, base-change, or completion assertion discharges these gaps.\n\nThe surface theorem in n2 is a general-geometry, arbitrary-support finite-energy result within its precise domain. Its narrower dimension and equal-characteristic geometric-origin hypotheses prevent a complete original P16.3 claim. Candidate remains false. No other model or worker, software installation, external message, or heavy computation was used.\n\nArtifacts: /workspace/research/campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs/artifacts/codex-tSmFOo",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Published primary-source provenance and exact application checks

{
  "scope": "Only input.json, eleven explicitly listed public caches, and fresh workspace artifacts were read.",
  "input_sha256": "551c1e4204b90a78f88201721de1c4b41a09bfd8f3c03cb997e9eb72d457c120",
  "source_audit_kind": "Selected relevant statements and proof passages, not an exhaustive literature survey.",
  "version_cautions": [
    "1201.0188 is byte-verified v1; its theorem retains algebraizability and dual-complex support.",
    "1805.01016 is byte-verified Boucksom-Eriksson v3, not a differently named pluripotential paper.",
    "1801.08229v4 has trivial valuation; no nontrivial-valued conclusion is quoted from its theorem.",
    "GJKM Theorem 4.6(iii), visually checked on PDF page 15, says E-lambda D nef; the introduction Theorem 1.3 has a different displayed order. The body theorem is used.",
    "GJKM section 9 assumptions A1-A3 visually checked on PDF page 22; n+d=3 here.",
    "GJKM cites later BFJ numbering: sequence regularization maps to Proposition 4.5 in supplied BFJ v1.",
    "GJKM Theorem 6.3 is used as a published theorem with the exact dimension/perfect-field application; CP08/CP09 themselves were not supplied or independently checked."
  ],
  "visual_pdf_checks": [
    "source-extracts/GJKM-page15.png",
    "source-extracts/GJKM-page22.png"
  ],
  "sources": [
    {
      "id": "1201.0187",
      "public_source": "https://arxiv.org/pdf/1201.0187v2",
      "saved_version": "1201.0187v2",
      "application_check": "Applied through the exact positive-characteristic transfer in GJKM section 9: sections 1-7 supply psh compactness, sup continuity, and determination by divisorial values once projective SNC models are cofinal. Its multiplier-ideal section 8 and characteristic-zero Appendix B are replaced by GJKM sections 4,7,8. This cached v2 has compactness Theorem 7.10.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.pdf",
          "bytes": 768011,
          "sha256": "8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.txt",
          "bytes": 175336,
          "sha256": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
          "matches_supplied_hash": true
        },
        {
          "kind": "abstract_html",
          "path": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.html",
          "bytes": 39974,
          "sha256": "983485b15a5da892c0b29ecb5ebb7280414028bd1333614a0ae8bf5ec888dbde",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/1201.0187-standing-and-main.txt",
          "source_line_first": 84,
          "source_line_last": 219,
          "pdf_page_first": 2,
          "pdf_page_last": 5,
          "sha256": "07b92e58ae29512b4ee1ddd45e7fada0a1d43aec5d813b025a285f987f6bed10",
          "literal_text": "singular semipositive metrics with the set PSH(X, θ) of θ-psh functions. The latter are upper\nsemicontinuous (usc) functions ϕ : X → [−∞, +∞) such that θ + ddc ϕ is a positive closed\n(1, 1)-current. Modulo scaling, PSH(X, θ), endowed with the L1 -topology, is homeomorphic\nto the space of closed positive (1, 1)-currents lying in the cohomology class c1 (L) (with its\nweak topology), and hence is compact.\n   Let us now turn to the non-Archimedean case. Fix a complete, discrete valuation field K\nwith valuation ring R and residue field k, and set S := Spec R. We assume that k (and hence\nK) has characteristic zero, which means, concretely, that R is (non-uniquely) isomorphic to\nk[[t]]. Let X be a smooth projective K-analytic space in the sense of Berkovich, so that X\nis the analytification of a smooth projective K-variety by the GAGA principle. Recall that\nthe underlying topological space of X is compact Hausdorff. A model X of X is a normal\nflat projective S-scheme together with an isomorphism of the analytification of its generic\nfiber XK with X. Each line bundle L on X is (again, by GAGA) the analytification of a line\n    1In fact, [CLD12] was posted after the first version of the present paper.\n\f             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                        3\n\n\nbundle on XK (that we also denote by L), and a model metric is a metric k · kL on L that\nis naturally induced by the choice of a Q-line bundle L ∈ Pic(X )Q such that L|XK = L in\nPic(XK )Q . A model function ϕ on X is a function such that e−ϕ is a model metric on the\ntrivial line bundle. The set D(X) of model functions is then dense in C 0 (X), a well-known\nconsequence of the Stone-Weierstrass theorem.\n   Following S.-W.Zhang [Zha95, 3.1] (see also [KT, 6.2.1], [Gub98, 7.13], [CL06, 2.2]), we\nshall say that a model metric k · kL on L is semipositive if L ∈ Pic(X )Q is nef on the special\nfiber X0 of X , i.e. L · C ≥ 0 for all projective curves C in X0 . A continuous metric on L is\nthen semipositive in the sense of Zhang if it can be written as a uniform limit over X of a\nsequence of semipositive model metrics. The reader may consult [CL11] for a nice survey\non these notions.\n   In order to define a general notion of singular semipositive metrics, we use the finer\ndescription of X as an inverse limit of dual complexes (called skeletons in Berkovich’s termi-\nnology). Since the residue field k of R has characteristic zero, it follows from [Tem06] that\neach model of X is dominated by a SNC model X , by which we understand a regular model\nwhose special fiber X0 has simple normal crossing support (plus a harmless irreducibility\ncondition that we impose for convenience). To each SNC model X corresponds its dual\ncomplex ∆X , a compact simplicial complex which encodes the incidence properties of the\nirreducible components of X0 . The dual complex ∆X embeds canonically in X and for the\npurposes of this introduction we shall view ∆X as a compact subset of X. There is further-\nmore a retraction pX : X → ∆X . These maps are compatible with respect to domination of\nmodels, and we thus get a map\n                                         X → lim ∆X\n                                               ←−\n                                               X\nwhich is known to be a homeomorphism (see, for instance, [KS06, p.77, Theorem 10]).\n   Following the philosophy of [BGS95], we define the space of closed (1, 1)-forms on X as\nthe direct limit over all models X of X of the spaces N 1 (X /S) of codimension one numerical\nequivalence classes. Any model metric gives rise to a curvature form lying in this space.\nThe main reason for working with numerical equivalence (instead of rational equivalence\nas in [BGS95]) is that we can then adapt a result of [Kün96] to show that a line bundle\nL ∈ Pic(X) has vanishing first Chern class c1 (L) ∈ N 1 (X) iff it admits a model metric with\nzero curvature (cf. Corollary 4.4).\n   Fix a reference model metric k · k on L with curvature form θ. Any other metric can be\nwritten k · ke−ϕ for some function ϕ on X. When k · ke−ϕ is a semipositive model metric,\nwe say that the model function ϕ is θ-psh.\nDefinition. Let L be an ample line bundle on a smooth projective K-analytic variety X.\nFix a model metric k · k on L with curvature form θ. A θ-plurisubharmonic function on X\nis then a function ϕ : X → [−∞, +∞) such that:\n      • ϕ is upper semicontinuous (usc).\n      • ϕ ≤ ϕ ◦ pX for each SNC model X .\n      • ϕ is a uniform limit, on each dual complex ∆X , of θ-psh model functions.\nA singular semipositive metric is a metric k · ke−ϕ with ϕ a θ-psh function.\n  The consistency of the definition for model functions will be guaranteed by Theorem 5.11\nbelow. Let ϕ be a θ-psh function. Since ϕ is usc and each ϕ ◦ pX is continuous, it follows\n\f4              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n\nimmediately that S ϕ = inf X ϕ ◦ pX , so that ϕ is uniquely determined by its restriction to\nthe dense subset X ∆X of X. We may therefore endow the set PSH(X, θ) of all θ-psh\nfunctions (or, equivalently, of all singular semipositive metrics on L) with the topology\nof uniform convergence on dual complexes. We view this topology as an analogue of the\nL1 -topology in the complex case. Our first main theorem shows that this space is indeed\ncompact modulo additive constants, something that was also announced in the unpublished\nmanuscript by Kontsevich and Tschinkel [KT].\nTheorem A. Let L be an ample line bundle on a smooth projective K-analytic variety X\nendowed with a model metric with curvature form θ. Then PSH(X, θ)/R is compact.\n  In other words, the set of singular semipositive metrics on L modulo scaling is compact.\nFor curves, this result is a consequence of the work of Thuillier [Thu05], and follows from\nbasic properties of subharmonic functions on metrized graphs.\n  Our second main result is the following analogue of Demailly’s global regularization the-\norem.\nTheorem B. Let L be an ample line bundle on a smooth projective K-analytic variety X\nendowed with a model metric with curvature form θ. Then every θ-psh function ϕ is the\npointwise limit on X of a decreasing net of θ-psh model functions.\n   When dim X = 1, Theorem B is a special case of [Thu05, Théorème 3.4.19]. Thanks\nto Dini’s lemma, Theorem B implies a non-Archimedean version of the Demailly-Richberg\ntheorem, stating that every continuous θ-psh function is a uniform limit over X of θ-psh\nmodel functions. In other words, for continuous metrics our definition of semipositivity\nagrees with Zhang’s.\n   Let us briefly explain how Theorem A above is proved. The first important fact is that\nany dual complex ∆X comes equipped with a natural affine structure [KS06] such that any\nθ-psh function is convex on the faces of ∆X . On this complex we put any euclidean metric\ncompatible with the affine structure. The statement that we actually prove, and which\nimplies Theorem A, is\nTheorem C. For each dual complex ∆X there exists a constant C > 0, such that ϕ|∆X is\nLipschitz continuous with Lipschitz constant at most C for any θ-psh model function ϕ.\n   This result is proved in two steps. Assuming, as we may, that sup∆X ϕ = 0, we first bound\nϕ from below on the vertices of ∆X . This is done by exploiting the non-negativity of certain\nintersection numbers, a direct consequence of the model metric k · ke−ϕ being determined\nby a nef line bundle on some model.\n   The next step is to prove the uniform Lipschitz bound. Here again, the general idea\nis to exploit the non-negativity of certain intersection numbers, but the argument is more\nsubtle than in the first step. This time, the intersection numbers are computed on (possibly\nsingular) blowups of X corresponding to carefully chosen combinatorial decompositions of\n∆X , in the spirit of the toroidal constructions of [KKMS]. In [BFJ12b] we adapt these\ntechniques to prove a uniform version of Izumi’s theorem [Izu85].\n  The proof of Theorem B is of a different nature. Using Theorem A, we first show that the\nusc upper envelope of any family of θ-psh functions remains θ-psh, a basic property of θ-psh\nfunctions in the complex case. As a consequence, given any continuous function u ∈ C 0 (X)\n\f               SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                              5\n\n\nthe set of all θ-psh functions ψ such that ψ ≤ u on X admits a largest element, called the\nθ-psh envelope of u and denoted by Pθ (u). On the other hand, by density of D(X) in C 0 (X),\nwe may write any given function ϕ ∈ PSH(X, θ) as the pointwise limit of a decreasing family\nof (a priori not θ-psh) model functions uj , using only the upper semicontinuity of ϕ. It is not\ndifficult to see that Pθ (uj ) decreases to ϕ, and we are thus reduced to showing that the θ-psh\nenvelope of any model function is the uniform limit of a sequence of θ-psh model functions.\nThis is proved using multiplier ideals, in the spirit of [DEL00, ELS03, BFJ08]. The required\nproperties of multiplier ideals are shown to hold on regular models in Appendix B, the key\npoint being to show that the expected version of the Kodaira vanishing theorem holds in\nthis context.2\n   Let us comment on our assumptions on the field K. It is expected that pluripotential\ntheory can be developed on Berkovich spaces over arbitrary non-Archimedean fields, and\nas we mentioned before the first steps in that direction have been taken in [CLD12] (see\nalso [Gub13] for a nice account on these developments), where the notions of positive forms\nand currents are introduced, partially building upon ideas by Lagerberg [Lag12].\n   Our approach is geometric, and we restrict our attention to the discretely valued case\nin order to avoid the use of formal models over non-noetherian rings. We refer to [Gub98,\nGub03] for related works on semipositive metrics in the general setting of a complete non-\nArchimedean field. More importantly, Appendix B relies on the discreteness assumption.\n   Furthermore, we use the assumption that K has residue characteristic zero in two ways,\nthrough the existence of SNC models and through the cohomology vanishing properties of\nmultiplier ideals. In positive residue characteristic, the existence of SNC models is not known\nand it is much harder to construct retractions of X onto suitable complexes (embedded or\nnot). We refer to Berkovich [Ber99], Hrushovski-Loeser [HL10], and Thuillier [Thu11] for\nimportant contributions to the understanding of this problem.\n   The paper is organized as follows. The first two sections present the necessary back-\n"
        },
        {
          "filename": "source-extracts/1201.0187-positivity.txt",
          "source_line_first": 291,
          "source_line_last": 368,
          "pdf_page_first": 7,
          "pdf_page_last": 8,
          "sha256": "96b8cd8423ab8204e9e8a943038eab8ffa6e580375f40b4ebe971f691de852ea",
          "literal_text": "Lemma 1.2. Assume that L ∈ Pic(X ) is nef on X0 , i.e. L · C ≥ 0 for all k-proper curves\nC in X0 . Then L is also nef on XK , i.e. L · C ≥ 0 for all K-proper curves C in XK as well.\n  We will then simply say that L is nef. A curve is by definition reduced and irreducible.\nProof. Let C be K-proper curve in XK and let C be its closure in X equipped with its\nreduced structure. By [Har, Proposition III.9.7], C is flat over S. The degrees of L|C on the\ngeneric fiber and on the special fiber therefore coincide, which reads L · C = L · C0 . Now C0\nis an effective linear combination of vertical curves, and the result follows.              \u0003\n  We recall the following standard notions.\nDefinition 1.3. Let X be a normal projective S-variety.\n   (i) The space N 1 (X /S) of codimension 1 numerical classes is defined as the quotient\n       of Pic(X )R by the subspace spanned by numerically trivial line bundles, i.e. those\n       L ∈ Pic(X ) such that L · C = 0 for all projective curves contained in a fiber of\n       X → S.\n  (ii) The nef cone Nef(X /S) ⊂ N 1 (X /S) is defined as the set of numerical classes α ∈\n       N 1 (X /S) such that α · C ≥ 0 for all projective curves contained in a fiber of X → S.\n   Note that the R-vector space N 1 (X /S) is finite dimensional. Indeed Lemma 1.2 shows\nthat the restriction map N 1 (X /S) → N 1 (X0 /k) is injective, and the latter space is finite\ndimensional since X0 is projective over k. Observe also that Nef(X /S) is a closed convex\ncone of N 1 (X /S). Lemma 1.2 implies that Nef(X /S) = Nef(X0 /k) ∩ N 1 (X /S) under the\ninjection N 1 (X /S) → N 1 (X0 /k).\n   We have the following standard fact:\nLemma 1.4. Let π : X 0 → X be a vertical blowup.\n   (i) There exists a π-ample divisor A ∈ Div0 (X 0 ).\n  (ii) If L ∈ Pic(X ) is ample then there exists m ∈ N such that π ∗ (mL|XK ) extends to an\n       ample line bundle L0 on X 0 .\nProof. By definition, there exists a vertical ideal sheaf a on X such that π is obtained as the\nblowup of X along a. The universal property of blowups yields a π-ample Cartier divisor A\non X 0 such that a · OX 0 = OX 0 (A), and A is also vertical since a is, which proves (i). If L is\nample on X then mπ ∗ L + A is ample on X 0 for m \u001d 1, and (ii) follows.                         \u0003\n   Recall that an R-line bundle on X (resp. XK ) is ample if it can be written as a positive\nlinear combination of ample line bundles.\nCorollary 1.5. If L ∈ Pic(XK )R is ample, then L extends to an ample R-line bundle\nL0 ∈ Pic(X 0 )R for all sufficiently high vertical blowups X 0 → X .\n                    P\nProof. Write L = i ci Li where ci ∈ R>0 and Li ∈ Pic(XK ) is ample for all i. We may\nassume that Li is very ample for each i, so that the linear system |Li | embeds X into a\nsuitable projective space PrKi over K. Let Xi be the normalization of the closure of XK in\nPrSi and Li the restriction of O(1) to Xi . Let X 0 be any normal S-variety dominating X as well\n\f8               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n\nas all the Xi , and write πi : X 0 → Xi for the associated vertical blowups. By Lemma 1.4 (ii)\nwe can find mi ∈ N and ample line bundles L0i on X 0 such that L0i |XK0 = πi∗ (mi Li |Xi,K ). We\ncan then pick L0 := i m\n                      P ci 0\n                            i\n                              Li .                                                             \u0003\n  We shall use the following version of the Negativity Lemma, cf. [KM98, Lemma 3.39]. The\nproof we give is a variant of the argument used in [BdFF10, Proposition 2.12].\nLemma 1.6. Assume that X is vertically Q-factorial and let π : X 0 → X be a vertical\nblowup. If D ∈ Div0 (X 0 )R is π-nef then π ∗ π∗ D − D is effective.\n   The condition that X is vertically Q-factorial guarantees that the pull-back of π∗ D by π\nis well defined.\nProof. As a first step, we reduce the assertion to the case where D ∈ Div0 (X 0 )Q is π-ample.\nIndeed, the set of vertical π-ample R-divisors, which is an open convex cone in Div0 (X 0 )R ,\nis non-empty by (i) of Lemma 1.4. We may thus choose a basis A1 , . . . , Ar of DivP        0\n                                                                                        0 (X )R\n                                                           r\nmade up of π-ample Cartier divisors. Let ε = (εi ) ∈ R+ be such that Dε := D + i εi Ai\nis a Q-divisor. The fact that D is π-nef means that D · C ≥ 0 for each curve C contained\nin a fiber of π. Since each Ai is π-ample, it follows from Kleiman’s criterion [Kle66] that\nDε is π-ample on the projective k-scheme X00 , hence Dε is also π-ample on X 0 by [EGA,\nIII.4.7.1]. Upon replacing D with Dε for ε arbitrarily small we may thus assume as desired\nthat D ∈ Div0 (X 0 )Q is π-ample.\n   Now choose m \u001d 1 such that OX 0 (mD) is π-globally generated, which means that the\nvertical fractional ideal sheaf a := π∗ OX 0 (mD) satisfies a · OX 0 = OX 0 (mD). It is obvious\nthat a ⊂ OX (mπ∗ D), hence OX 0 (mD) ⊂ OX 0 (mπ ∗ π∗ D), and the result follows.              \u0003\n\n               2. Projective Berkovich spaces and model functions\n2.1. Analytifications. Let Y be a proper K-scheme. As a topological space, its K-\nanalytification Y an in the sense of Berkovich is compact and can be described as follows\n(cf. [Ber90, Theorem 3.4.1]). Choose a finite cover of Y by Zariski open subsets of the form\nU = Spec A where A is a finitely generated K-algebra. The Berkovich space U an is defined\nas the set of all multiplicative seminorms | · |x : A → R+ extending the given absolute value\nof K, endowed with the topology of pointwise convergence. It is common usage to write\n|f (x)| := |f |x for f ∈ A and x ∈ U an . The space Y an is then obtained by gluing together\nthe open sets U an .\n    There is a canonical continuous map s : Y an → Y , locally defined on U an by setting\n"
        },
        {
          "filename": "source-extracts/1201.0187-psh-compactness.txt",
          "source_line_first": 1615,
          "source_line_last": 1770,
          "pdf_page_first": 32,
          "pdf_page_last": 36,
          "sha256": "809d6ec8c790440fbd5b9d496dce0046bfe614af0adb02f1a4e8d7cd8f9dfbdc",
          "literal_text": "  Throughout this section we let X be as before a smooth connected projective K-analytic\nvariety and fix a closed (1, 1)-form θ ∈ Z 1,1 (X) whose de Rham class {θ} ∈ N 1 (X) is ample.\nAs before we write “psh” as a shorthand for “plurisubharmonic”. Similarly, “usc” and “lsc”\nwill mean “upper semicontinuous” and “lower semicontinuous”, respectively.\nDefinition 7.1. Let θ be as above. A θ-psh function ϕ : X → [−∞, +∞[ is a usc function\nsuch that for each SNC model X of X on which θ is determined we have\n    (i) ϕ ≤ ϕ ◦ pX on X;\n\f             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                      33\n\n\n  (ii) the restriction of ϕ to embX (∆X ) is a uniform limit of restrictions of θ-psh model\n       functions.\nWe write PSH(X, θ) for the set of θ-psh functions on X.\n   We say that ϕ : X → [−∞, +∞[ is quasi-psh if ϕ is θ-psh for some θ as above. Thanks\nto Theorem 5.11, the previous definition is consistent with Definition 5.5 when ϕ is a model\nfunction. In particular, constant functions are θ-psh iff θ is semipositive.\nRemark 7.2. A function on a compact (complex) Kähler manifold X is quasi-psh if it is\nlocally the sum of a psh function and a smooth function. Given a closed (1, 1)-form θ, a θ-\npsh function ϕ is a quasi-psh function such that θ + ddc ϕ ≥ 0 in the sense of currents. When\nthe de Rham class {θ} ∈ H 1,1 (X) is a Kähler class, we have a global characterization: θ-psh\nfunctions are decreasing limits of sequences of smooth θ-psh functions, see [Dem92, Theorem\n1.1]. In our current non-Archimedean setting, a general local theory of psh functions is still\nto be developed (although the first steps are taken in [CLD12]). For this reason, we work\nglobally and assume that {θ} is ample.\n  Recall the definitions from §4 of singular and model metrics on line bundles.\nDefinition 7.3. Let L be an ample line bundle on X. A singular metric on L is semipositive\nif it is of the form k · ke−ϕ , where k · k is a model metric and ϕ is c1 (L, k · k)-psh.\n   One checks that this definition does not depend on the choice of reference metric k · k.\nBelow we shall state various properties of θ-psh functions. We leave it to the reader to\nformulate analogous assertions about semipositive singular metrics on ample line bundles.\n\n7.1. Basic properties. Fix a closed (1, 1)-form θ ∈ Z 1,1 (X) as above. From Proposition 5.8\nand 5.9 we obtain:\nProposition 7.4. The set PSH(X, θ) is convex. If ϕ, ψ are θ-psh and c ∈ R, then ϕ + c\nand max{ϕ, ψ} are θ-psh.\nProposition 7.5. If ϕ ∈ PSH(X, θ) and X is an SNC model on which θ is determined,\nthen:\n    (i) ϕ ◦ embX is continuous (and finite) on ∆X and convex on each face;\n   (ii) ϕ ◦ pX is continuous on X and ϕ ≤ ϕ ◦ pX .\n  The next result shows how to reconstruct a θ-psh function from its values on quasimono-\nmial points.\nProposition 7.6. Let ϕ ∈ PSH(X, θ). Then, as X runs through the directed set of SNC\nmodels on which θ is determined, (ϕ ◦ pX )X forms a decreasing net of continuous functions\non X, converging pointwise to ϕ.\nProof. Let X 0 ≥ X be two SNC models on which θ is determined. Then pX ◦ pX 0 = pX .\nBy Proposition 7.5 (ii) this implies ϕ ≤ ϕ ◦ pX 0 ≤ ϕ ◦ pX ◦ pX 0 = ϕ ◦ pX , with equality on\nembX (∆X ). Set ϕ̃ := limX ϕ ◦ pX . Then ϕ̃ ≥ ϕ. On the other hand, by Corollary 3.9, pX\nconverges to the identity on X, so by upper semicontinuity of ϕ we have ϕ ≥ ϕ̃.             \u0003\nCorollary 7.7. If ϕ, ψ ∈ PSH(X, θ) and ϕ = ψ on X div , then ϕ = ψ.\n\f34              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n\nProof. Let X be an SNC model on which θ is determined. By Corollary 3.17, X div is dense in\nemb(∆X ) and by Proposition 7.5, ϕ and ψ are continuous on emb(∆X ), so our assumptions\nimply that ϕ = ψ on emb(∆X ). Thus ϕ ◦ pX = ψ ◦ pX . Letting X run though all sufficiently\nlarge models, we conclude using Proposition 7.6.                                         \u0003\n7.2. Equicontinuity. The Lipschitz estimates in Theorem 6.1 carry over to general θ-psh\nfunctions. As a consequence we have\nCorollary 7.8. For any SNC model on which θ is determined, the family\n                                 {ϕ ◦ embX | ϕ ∈ PSH(X, θ)}\nis an equicontinuous family of functions on ∆X .\nCorollary 7.9. If (ϕi )i is a decreasing net in PSH(X, θ) and ϕ = limi ϕi , then either\nϕ ≡ −∞ or ϕ ∈ PSH(X, θ).\nProof. Assume ϕ 6≡ −∞, and the upper semicontinuity of ϕi implies that of ϕ. Let X be\nany SNC model on which θ is determined. The inequality ϕi ≤ ϕi ◦ pX implies ϕ ≤ ϕ ◦ pX ,\nand hence\n                               sup(ϕ ◦ embX ) = sup ϕ\n                                    ∆X                      X\nis finite. By Proposition 7.5, the supremum of each ϕi is attained on the finite set of divisorial\nvaluations associated to vertices of DX . Hence\n                           sup(ϕi ◦ embX ) ≥ sup(ϕ ◦ embX ) > −∞\n                           ∆X                  ∆X\nfor all i. It then follows from Corollary 7.8 that ϕi ◦ embX converges uniformly to ϕ ◦ embX\nand that ϕ ◦ embX is continuous.                                                           \u0003\n7.3. Compactness. We endow the set PSH(X, θ) of all θ-psh functions with the topology\nof uniform convergence on dual complexes. A basis of open neighborhoods of a fixed θ-psh\nfunction ϕ0 is then given by {ϕ | sup∆X |ϕ − ϕ0 | ≤ ε} where X ranges over SNC models on\nwhich θ is determined and where ε > 0. Thanks to Proposition 7.6, the natural map\n                                              Y\n                                 PSH(X, θ) →       C 0 (∆X )\n                                                    X\nis a homeomorphism onto its image. Note also that D(X) ∩ PSH(X, θ) is dense in PSH(X, θ)\nby definition. The following result is a more precise version of Theorem A.\nTheorem 7.10. If ψ ∈ D(X) is any model function, then the map PSH(X, θ) → R defined\nby ϕ 7→ supX (ϕ − ψ) is continuous and proper. Hence PSH(X, θ)/R is compact. Further-\nmore, the topology on PSH(X, θ) is equivalent to the topology of pointwise convergence on\neither X qm or X div .\nProof. Let X be an SNC model on which θ and ψ are determined. Then ψ = ψ ◦ pX , so\nProposition 7.5 implies that (ϕ − ψ) ◦ pX is continuous and that (ϕ − ψ) ◦ pX ≥ (ϕ − ψ) for\nany ϕ ∈ PSH(X, θ). Hence the supremum of ϕ − ψ is attained on embX (∆X ), which implies\nthe continuity of ϕ 7→ supX (ϕ − ψ).\n  To prove properness, we need to show that\n                         FC := {ϕ ∈ PSH(X, θ) | | sup(ϕ − ψ)| ≤ C}\n                                                        X\n\f             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                       35\n\n\nis compact for any C > 0. Recall that PSH(X, θ) embeds in X C 0 (∆X ). By Tychonoff’s\n                                                              Q\ntheorem, the compactness of FC is therefore equivalent to the compactness in C 0 (∆X ) of\nthe closure of the image of FC in C 0 (∆X ), for each SNC model X on which θ and ψ are\ndetermined. But this is a direct consequence of Corollary 7.8 and Ascoli’s theorem.\n   Picking ψ = 0, we see that ϕ 7→ supX ϕ is proper, which implies the compactness of\nPSH(X, θ).\n   For the last statement, it is clear that convergence in PSH(X, θ) implies pointwise con-\nvergence on X qm which in turn implies pointwise convergence on X div . Now let (ϕα )α∈A\nbe a net of θ-psh functions converging pointwise to ϕ ∈ PSH(X, θ) on X div . Fix any SNC\nmodel X on which θ is determined. We must show that ϕα converges uniformly to ϕ on\nembX (∆X ). But X div ∩ embX (∆X ) is dense in embX (∆X ) by Corollary 3.17, so this follows\nfrom the equicontinuity statement in Corollary 7.8.                                       \u0003\n7.4. Upper envelopes. Finally we shall prove the following result, whose complex analogue\nserves as a basic ingredient of pluripotential theory. While we will not go deeper into\npluripotential theory here, we will use the result below in §8. The proof will in fact not use\nthe compactness result in §7.3.\nTheorem 7.11. Let (ϕα )α∈A be an arbitrary family of θ-psh functions on X, and assume\n                                                                            for each x ∈ X,\nthat (ϕα ) is uniformly bounded from above. If we set ϕ(x) := supα∈A ϕα (x) S\n                             ∗                                        qm\nthen the usc regularization ϕ of ϕ is θ-psh and coincides with ϕ on X = X embX (∆X ).\nFurther, we have ϕ∗ = limX ϕ ◦ pX = inf X ϕ ◦ pX .\n  Recall that the usc regularization of a function u on a topological space X is the smallest\nusc function u∗ ≥ u, given by u∗ (x) = lim supy→x u(y).\nProof of Theorem 7.11. Upon considering the new family ϕI = maxα∈I ϕα with I ranging\nover all finite subsets of A, we may assume that A is a directed set and (ϕα ) is an increasing\nnet. We must show that conditions (i)–(ii) of Definition 7.1 hold for ϕ∗ .\n   For each SNC model X on which θ is determined, ϕα ◦ embX is convex and continuous\non ∆X for each α. The increasing limit ϕ ◦ embX = limα ϕα ◦ embX is therefore convex\nand lsc on ∆X . On the other hand, any convex function on a convex polytope is usc,\nsee [GKR68]. Thus ϕ ◦ embX is continuous, and, by Dini, ϕα ◦ embX converges uniformly\non ∆X to ϕ ◦ embX . Equivalently, ϕ ◦ pX is continuous and ϕα ◦ pX converges uniformly to\nϕ ◦ pX on X.\n   Since X 7→ ϕα ◦ pX is decreasing, the same is true for X 7→ ϕ ◦ pX . We claim that\nlimX ϕ ◦ pX = ϕ∗ . To see this, note that ψ := limX ϕ ◦ pX is a decreasing limit of continuous\nfunctions and hence usc. On the one hand, ϕ ◦ pX ≥ ϕ for all X implies ψ ≥ ϕ, so that\nψ ≥ ϕ∗ by the definition of the usc regularization. On the other hand, Corollary 3.9 and\nthe upper semicontinuity of ϕ∗ implies\n                             ϕ∗ ≥ lim ϕ∗ ◦ pX ≥ lim ϕ ◦ pX = ψ,\n                                  X              X\n         ∗\nso that ϕ = limX ϕ ◦ pX = inf X ϕ ◦ pX , hence the claim.\n   If Y ≤ X are SNC models on which θ is determined, then pX ◦ pY = pY by Proposi-\ntion 3.6 (iv). By what precedes, this implies ϕ∗ ◦ pY = limX ϕ ◦ pX ◦ pY = ϕ ◦ pY . In\nparticular, ϕ∗ = ϕ on embY (∆Y ). Since Y was arbitrary, we get ϕ∗ = ϕ on X qm .\n   It remains to prove that ϕ∗ is θ-psh in the sense of Definition 7.1. First, ϕα ≤ ϕα ◦ pX\nfor all α implies ϕ ≤ ϕ ◦ pX , which gives ϕ∗ ≤ (ϕ ◦ pX )∗ = ϕ ◦ pX = ϕ∗ ◦ pX , where the first\n\f36                SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n\nequality follows from the continuity of ϕ ◦ pX . Thus (i) holds. Second, the restriction of\neach ϕα to embX (∆X ) is, by assumption, a uniform limit of θ-psh model functions. Since ϕα\nconverges uniformly to ϕ = ϕ∗ on embX (∆X ), we see that the restriction of ϕ∗ to embX (∆X )\nis also a uniform limit of θ-psh model functions. Thus (ii) also holds and ϕ∗ is θ-psh.   \u0003\n\n                             8. Envelopes and regularization\n  We continue to assume that θ ∈ Z 1,1 (X) is a closed (1, 1)-form whose de Rham class\n{θ} ∈ N 1 (X) is ample. This positivity property will be crucial in the arguments to follow.\n"
        },
        {
          "filename": "source-extracts/1201.0187-base-ideal-proof.txt",
          "source_line_first": 1842,
          "source_line_last": 1900,
          "pdf_page_first": 37,
          "pdf_page_last": 38,
          "sha256": "744cc1752c6771ab1e1fc4424b788385879a7378ed5b9bf36c3b36a4b8d43889",
          "literal_text": "Theorem 8.5. Let L be an ample line bundle on X and L ∈ Pic(X ) an extension of L to\nan SNC model X . Let θ ∈ Z 1,1 (X) be the curvature form of the corresponding model metric\n                                                                                1\non L. For m \u001d 1 let am ⊂ OX be the (vertical) base-ideal of mL and set ϕm := m    log |am |.\nThen ϕm is a θ-psh model function and ϕm → Pθ (0) uniformly on X as m → ∞.\nProof of Theorem 8.5. For m \u001d 1, mL|XK is globally generated, which shows that the ideal\nsheaf am is vertical. Since OX (mL) ⊗ am is globally generated by the definition of am , it\nfollows that ϕm ∈ D(X) is θ-psh by Lemma 5.6. Note that am · al ⊂ am+l for all m, l.\nThis yields the super-additivity property mϕm + lϕl ≤ (m + l)ϕm+l . As a consequence, the\npointwise limit limm ϕm exists and coincides with supm ϕm .\n   Step 1. Let us first prove that Pθ (0) = supm ϕm on X qm . The argument is similar to\nStep 2 of Theorem 5.11. Since ϕm is θ-psh and ϕm ≤ 0 for all m, we have supm ϕm ≤ Pθ (0)\non X. To see that equality holds on X qm , pick ε > 0 and x ∈ embX 0 (∆X 0 ) for some SNC\n\f38               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n\nmodel X 0 dominating X . By Lemma 8.4 there exists a θ-psh model function ϕ such that\nϕ ≤ 0 and ϕ(x) ≥ Pθ (0)(x) − ε. Replacing X 0 by a higher model, we may assume that\nϕ = ϕD is determined by some divisor D ∈ Div0 (X 0 )Q . Invoking Proposition 5.2 we may\nalso assume that there exists D0 ∈ Div0 (X 0 )Q with −ε ≤ ϕD0 ≤ 0 on X and π ∗ L + D + D0\nample. Since D + D0 ≤ 0 we then have\n                           OX 0 (mπ ∗ L + m(D + D0 )) ⊂ OX 0 (mπ ∗ L).\nNow the left-hand side is globally generated for some m, and we conclude that\n                                  OX 0 (m(D + D0 )) ⊂ OX 0 · am ;\nhence\n                                                     1\n        Pθ (0)(x) ≤ ϕD (x) + ε ≤ ϕD+D0 (x) + 2ε ≤      log |am |(x) + 2ε ≤ sup ϕl (x) + 2ε.\n                                                     m                      l\n\n   Step 2. Introduce, for each m ∈ N, the asymptotic multiplier ideal bm := J (am  • ) ⊂ OX\nassociated to the graded sequence a• . We refer to Appendix B for the definition and the\nproof of the fundamental properties of multiplier ideals in our present setting. We shall use\nthe following results. First, we have the elementary inclusion am ⊂ bm for all m. Second,\nthe subadditivity property (cf. Theorem B.7) implies bml ⊂ blm for any l, m. We infer that\naml ⊂ bml ⊂ blm for any m, l and hence\n                         1                 1\n                         m log |bm | ≥ sup ml log |aml | = sup ϕml = Pθ (0)                   (8.1)\n                                        l                   l\n\non X qm for all m, where the last equality follows from Step 1.\n  Since both Pθ (0) and ϕm remain unchanged when X is replaced with a higher model, we\nmay assume that there exists an effective divisor E ∈ Div0 (X )Q such that A := L − E is\nample on X . By the uniform global generation property of multiplier ideals (Theorem B.8\nand Remark B.9) we may then choose m0 ∈ N such that m0 A is ample enough to guarantee\nthat OX (mL + m0 A) ⊗ bm is globally generated for all m. Since OX (mL + m0 A) injects in\nOX ((m + m0 )L) by multiplying with the canonical section of OX (m0 E), it follows that\n                                 log |bm | ≤ log |am+m0 | + m0 ϕE .\nReplacing m with m − m0 and using (8.1) we infer (m − m0 )Pθ (0) ≤ mϕm + m0 ϕE , so that\n                                             m          m0\n                              ϕm ≤ Pθ (0) ≤ m−m 0\n                                                  ϕm + m−m 0\n                                                             ϕE\n\non X qm for m \u001d 1. As ϕm , Pθ (0) and ϕE are all θ-psh, Proposition 7.6 shows that this\ninequality extends to all of X. Now ϕE is bounded and ϕm is uniformly bounded, as follows\nfrom ϕ1 ≤ ϕm ≤ 0, so ϕm converges uniformly on X to Pθ (0), as was to be shown.        \u0003\n\n     Let us end this subsection with a result that will be used in [BFJ12a].\nCorollary 8.6. If ϕ ∈ PSH(X, θ) and v ∈ C 0 (X) are such that ϕ ≤ v then for every ε > 0\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "1201.0188",
      "public_source": "https://arxiv.org/pdf/1201.0188v1",
      "saved_version": "1201.0188v1",
      "application_check": "Actual v1: Theorem A assumes residue characteristic zero, algebraizability, and SNC-dual-complex support. Applied bounded operator Theorem 3.1; locality Theorem 5.1; energy Proposition 6.2; nonpluripolar construction Definition 6.4; full mass Lemma 6.7; independence Proposition 6.9; comparison Proposition 6.11; differentiation Proposition 6.12 and Theorem 7.2/Corollary 7.3. GJKM explicitly transfers sections 3-6 and supplies orthogonality for section 7. Uniqueness Proposition 8.2 proof is checked as characteristic-free finite-energy calculus; its last vertical Hodge kernel step is independently proved in the argument. Saved v1 sequence regularization is Proposition 4.5, not the later-version Proposition 4.7 cited by GJKM.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf",
          "bytes": 531005,
          "sha256": "4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.txt",
          "bytes": 161436,
          "sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
          "matches_supplied_hash": true
        },
        {
          "kind": "abstract_html",
          "path": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.html",
          "bytes": 40180,
          "sha256": "e4683a68defd5887b5952cddcccc9f625a2d0391819a97f32a15d4d51f5409ae",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/1201.0188-standing-and-Theorem-A.txt",
          "source_line_first": 58,
          "source_line_last": 108,
          "pdf_page_first": 2,
          "pdf_page_last": 3,
          "sha256": "48abb3f6004fd8a2f20ac0e09a02f2f365c2570464524c102281244fe22bd9c6",
          "literal_text": "on the work of Aubin, Calabi and Yau, which culminated in the celebrated article [Yau78],\nwhere it was shown that the solution metric is smooth when µ is a smooth positive volume\nform on X.\n   We next turn to the non-Archimedean analogue, referring to §2 for more details. Let\nK be a complete discrete valuation ﬁeld whose residue ﬁeld k has characteristic zero, so\nthat K ≃ k((t)). Let X be a smooth projective variety over K, and write n = dim X.\nThanks to the non-Archimedean GAGA principle, it is reasonable to also denote by X\nthe corresponding K-analytic space in the sense of Berkovich, whose underlying topological\nspace is compact Hausdorﬀ. A model of X is a normal scheme X that is ﬂat and projective\nover S := Spec k[[t]], and whose generic ﬁber can be identiﬁed with X.\n   Consider a ample line bundle L on X. A model metric on L is a metric deﬁned by a\nextension L ∈ Pic(X )Q of L to some model X . Such a metric is called semipositive if L is\nnef, i.e. has non-negative degree on all proper curves of the special ﬁber of X . S.-W. Zhang\nintroduced in [Zha95] the more ﬂexible notion of semipositive continuous metric as the\nuniform limit of semipositive model metrics.1 In this context, A. Chambert-Loir [CL06]\ndeﬁned the Monge-Ampère measure c1 (L, k · k)n of a semipositive continuous metric k · k on\nL. It is a positive Radon measure on X, of mass deg L.\n   V. Berkovich constructed in [Ber99] the skeleton associated to a polystable model of X.\nSince we are assuming K to have residue characteristic zero, it is easier to rely on resolution\nof singularities and instead consider SNC models, i.e. models whose special ﬁber has simple\nnormal crossing support (but is not necessarily reduced, as opposed to a semistable model).\nTo each SNC model X is associated a dual complex ∆X that encodes the combinatorics of\nthe intersections of the components of the special ﬁber, and which embeds in the Berkovich\nspace X just as skeletons do. Any ﬁnite set  S of divisorial points is contained in the dual\ncomplex of some SNC model; in particular X ∆X is dense in X.\n   We can now state our main result. We say that X is algebraizable if there exists a (one-\nvariable) function ﬁeld F admitting K as a completion and a smooth projective F -scheme\nY such that X = YK .\nTheorem A. Let K be a complete discrete valuation field of residue characteristic zero. Let\nX be a smooth projective K-variety that is algebraizable. Let L ∈ Pic(X) be an ample line\n    1We refer to Table 1 in §2.6 below for a comparison of our terminology with existing terminology.\n\f               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                          3\n\nbundle and µ be a positive Radon measure on X of mass c1 (L)n . If we further assume that\nµ is supported on the dual complex of some SNC model of X, then there exists a continuous,\nsemipositive metric k · k on L such that\n                                   c1 (L, k · k)dim X = µ .                              (1.1)\nThis metric is furthermore unique up to a multiplicative constant.\n  Even though the result is most likely true without this assumption, the algebraizability\ncondition plays an essential role in our proof, as we shall explain below. Note that the line\nbundle L is not assumed to be deﬁned over a function ﬁeld.\n   The uniqueness part in Theorem A follows from a result of X. Yuan and S.-W. Zhang\n[YZ10] asserting more generally that a continuous semipositive metric k · k is uniquely de-\ntermined up to a constant by its Monge-Ampère measure. Their proof is inspired by the\none given by Blocki [Blo03] in the complex setting.\n   Our approach does not give any information on the regularity of the metric besides con-\ntinuity. It would be interesting to further investigate this issue, for instance when µ is\nsupported on ﬁnitely many divisorial points. We refer to §9 for a discussion of this problem\nin the case of toric varieties, based on the recent work [BPS11].\n   Versions of Theorem A are already known in a few cases. For curves (and in fact over any\ncomplete non-Archimedean, non-trivially valued ﬁeld), it can easily be deduced from results\n"
        },
        {
          "filename": "source-extracts/1201.0188-psh-background.txt",
          "source_line_first": 473,
          "source_line_last": 553,
          "pdf_page_first": 11,
          "pdf_page_last": 12,
          "sha256": "c3b6375f01579eb576779c4e2c4a3223d3414892fc658a4000f3838ab6384291",
          "literal_text": "2.4. θ-psh functions. Fix a form θ ∈ Z 1,1 (X) with ample de Rham class {θ} ∈ N 1 (X).\n\nDefinition 2.5. A θ-psh function ϕ : X → [−∞, +∞[ is an usc function such that for each\nSNC model X of X on which θ is determined we have\n    (i) ϕ ≤ ϕ ◦ pX on X;\n   (ii) the restriction of ϕ to the dual complex ∆X is a uniform limit of restrictions of model\n        functions ψ such that θ + ddc ψ is a semipositive form.\nWe write PSH(X, θ) for the set of θ-psh functions on X.\n\n  It is a nontrivial fact that if ϕ is a θ-psh model function then the form θ + ddc ϕ is in fact\nsemipositive, see [BFJ11, Theorem 5.11]. In particular, the zero function is θ-psh iﬀ θ is\nsemipositive. In this case, max{ϕ, −t} is θ-psh when ϕ is θ-psh and t ∈ R.\n\nProposition 2.6. [BFJ11, Proposition 5.10]. The space of model functions D(X) is spanned\nby θ-psh model functions.\n\nProposition 2.7. [BFJ11, Proposition 7.4]. The set PSH(X, θ) is convex. If ϕ, ψ are θ-psh\nand c ∈ R, then the functions max{ϕ, ψ} and ϕ + c are also θ-psh.\n\nProposition 2.8. [BFJ11, Proposition 7.5]. Any ϕ ∈ PSH(X, θ) is continuous on the dual\ncomplex of any SNC model X , and convex on each of its faces.\n\n  In fact, the continuity statement above can be made uniform in ϕ:\nTheorem 2.9. [BFJ11, Corollary 7.7] For any SNC model X , the restrictions of all θ-psh\nfunctions to the dual complex ∆X form an equicontinuous family.\n\n   We endow PSH(X, θ) with the topology of uniform convergence on dual complexes. Notice\nthat the divisorial points are dense on each dual complex ∆X , see [BFJ11, Corollary 3.13]\nor [JM10, Remark 3.9]. As a consequence of equicontinuity we thus have\n\nTheorem 2.10. [BFJ11, Theorem 7.8]. For each model function ψ the map ϕ 7→ supX (ϕ −\nψ) is continuous and proper on PSH(X, θ). In particular, the space PSH(X, θ)/R is compact.\nFurther, the topology on PSH(X, θ) is equivalent to the topology of pointwise convergence on\nX div .\n\n  Finally we have the following regularization result. Its proof relies on multiplier ideals.\n\nTheorem 2.11. [BFJ11, Theorem 8.7]. For any θ-psh function ϕ, there exists a decreasing\nnet (ϕj )j of θ-psh model functions that converges pointwise on X to ϕ.\n\n   The complex analogue of this result is due to Demailly [Dem92] (see also [GZ05, Appendix]\nfor the case of a line bundle). By Dini’s lemma, we get as a consequence:\n\nCorollary 2.12. [BFJ11, Corollary 8.8] The set D(X) ∩ PSH(X, θ) is dense in C 0 (X) ∩\nPSH(X, θ) with respect to uniform convergence on X.\n\n  Proposition 4.5 below reﬁnes Theorem 2.11 and asserts that any θ-psh function is actually\nthe decreasing limit of a sequence of θ-psh model functions (but the proof heavily uses\nTheorem 2.11).\n\f12               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n2.5. Envelopes. Let θ be a form as in §2.4.\nProposition 2.13. [BFJ11, Theorem 7.9]. If (ϕα )α∈A is a family of θ-psh functions that\nis uniformly bounded above, then the usc upper envelope (supα ϕα )∗ is also θ-psh.\n  Recall that the usc regularization u∗ of a function u : X → [−∞, +∞[ is the smallest usc\nfunction such that u∗ ≥ u.\nDefinition 2.14. Let f : X → [−∞, +∞[ be any function. We define its θ-psh envelope\nPθ (f ) as follows. If there does not exist any ϕ ∈ PSH(X, θ) such that ϕ ≤ f on X then\nwe set Pθ (f ) ≡ −∞. Otherwise, we define Pθ (f ) as the usc upper envelope of the set of all\nθ-psh functions ϕ such that ϕ ≤ f on X, i.e. we set\n                        Pθ (f ) := (sup {ϕ | ϕ ∈ PSH(X, ω), ϕ ≤ f })∗ .\n   Thanks to Proposition 2.13 Pθ (f ) is either −∞ or belongs to PSH(X, θ). If f is usc, then\nclearly Pθ (f ) ≤ f on X, and Pθ (f ) is then the largest θ-psh function with this property.\nProposition 2.15. [BFJ11, Proposition 8.1]\n    (i) Pθ is non-decreasing: f ≤ g ⇒ Pθ (f ) ≤ Pθ (g).\n   (ii) Pθ (f ) is concave in both arguments:\n                      Ptθ+(1−t)θ′ (tf + (1 − t)g) ≥ tPθ (f ) + (1 − t)Pθ′ (g)\n           for 0 ≤ t ≤ 1.\n     (iii) For each c ∈ R we have Pθ (f + c) = Pθ (f ) + c.\n     (iv) Pθ is 1-Lipschitz continuous, i.e. supX |Pθ (f ) − Pθ (g)| ≤ supX |f − g|.\n      (v) Given a bounded function f and a convergent sequence θm → θ in N 1 (X /S) we have\n           Pθm (f ) → Pθ (f ) uniformly on X.\n2.6. Metrized line bundles and curvature forms. We refer to [CL10] for a general\naccount of metrized line bundles in a non-Archimedean context. Suﬃce it to say that a\nmetric k · k on a line bundle L on X is a way to produce a local continuous function ksk on\n(the Berkovich space) X from any local section s of L.\n   Let X be a model and L a line bundle on X such that L|X = L. To this data one can\nassociate a unique metric k · kL on L with the following property: if s is a nonvanishing\nlocal section of L on an open set U ⊂ X , then kskL ≡ 1 on U := U ∩ X. This makes sense\nsince such a section s is uniquely deﬁned up to multiplication by an element of Γ(U , OX ∗ )\n\n"
        },
        {
          "filename": "source-extracts/1201.0188-intersection-calculus.txt",
          "source_line_first": 602,
          "source_line_last": 692,
          "pdf_page_first": 13,
          "pdf_page_last": 15,
          "sha256": "860e1b137e2d780d76427c5513cdd81c8d4e17b8e848ab1770accfbabdf59246",
          "literal_text": "Proposition-Definition 2.18. To any n-tuple (θ1 , . . . , θn ) of closed (1, 1)-forms we can\nassociated a signed atomic measure θ1 ∧ · · · ∧ θn supported on X div such that\n                    Z                      X\n                       f θ1 ∧ · · · ∧ θn =   bi f (xi ) (θ1,X |Ei · . . . · θn,X |Ei )  (2.2)\n                       X                        i∈I\nfor any common determination X of the forms           P       θi , and for any model function f . Here\nwe have written the special fiber as X0 =                i∈I bi Ei and xi = xEi is the divisorial point\nassociated to Ei .\n   Further, (θ1 , . . . , θn ) 7→ θ1 ∧ · · · ∧ θn is multilinear and symmetric.\n\f14              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n                                                                           R\nProof. Choose a commonR determination of the forms θi , and deﬁne X f (θ1 ∧ · · · ∧ θn )\nusing (2.2). The fact that X f (θ1 ∧· · ·∧θn ) does not depend on the choice of a determination\nX is a consequence of the projection formula\n                          π∗ D · θ1,X · . . . · θn,X = D · π ∗ θ1,X · . . . · π ∗ θn,X\nif π : X ′ → X , and D is any vertical divisor in X ′ .                             P\n   Then by construction θ1 ∧· · ·∧θn can be identiﬁed with the atomic measure i wi δxi with\nwi = (θ1,X |Ei · . . . · θn,X |Ei ). This measure is supported on the divisorial points associated\nto the irreducible components of X0 . The last statement is clear.                               \u0003\nProposition 2.19. If the forms θ1 , . . . , θn are semipositive, then θ1 ∧ · · · ∧ θn is a positive\nmeasure, of mass           Z\n                                           θ1 ∧ · · · ∧ θn = {θ1 } · . . . · {θn }.                               (2.3)\n                                      X\n\nProof. Pick a model X such that each θi is determined by a nef class θi,X ∈ N 1 (X /S).\nThe restriction of θi,X to each component Eω of X0 is then also nef, and it follows that the\nintersection number (θ1,X |E · ... · θn,X |E ) is non-negative, hence the ﬁrst assertion. Since the\nconstant function 1 corresponds to the vertical divisor X0 we have by deﬁnition\n                               Z\n                                     θ1 ∧ ... ∧ θn = X0 · θ1 · . . . · θn .\n                                       X\nBy [Ful98, Example 20.3.3] this is the same as the intersection number against the generic\nﬁber of X , and this is equal to {θ1 } · . . . · {θn } by deﬁnition.                    \u0003\n   As a special case, ﬁx θ ∈ Z 1,1 (X). To any θ-psh model functions ϕ1 , . . . , ϕn we then\nassociate a mixed Monge-Ampère measure\n                                      (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn ).\nThis is an atomic positive measure on X of mass {θ}n .\n  Analogously to the complex case we have the following integration by parts formula:\nProposition 2.20. If f, g ∈ D(X) are model functions and θ1 , . . . , θn−1 are closed (1, 1)-\nforms then we have\n                 Z                             Z\n                   f dd g ∧ θ1 ∧ · · · ∧ θn−1 = g ddc f ∧ θ1 ∧ · · · ∧ θn−1 .\n                       c\n\n\nProof. Pick a common determination X of f, g and the θi ’s, and divisors D, D ′ , Di such that\nf = ϕD , g = ϕD′ and θi is the class in N 1 (X /S) induced by Di . Then by deﬁnition we have\n  Z                                X\n     f ddc g ∧ θ1 ∧ · · · ∧ θn−1 =   ordE (D)(D ′ |E · D1 |E · ... · Dn−1 |E )\n                                           E\n                       X\n                  =           ordE (D) ordE ′ (D ′ ) (D1 |E )|E ′ ∩E · ... · (Dn−1 |E )|E ′ ∩E\n                      E,E ′\n                      X\n                  =           ordE (D) ordE ′ (D ′ ) (D1 |E ′ )|E∩E ′ · ... · (Dn−1 |E ′ )|E∩E ′\n                      E,E ′\n                                                                                      Z\n                                                                                =         g ddc f ∧ θ1 ∧ · · · ∧ θn−1\n\f                SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                            15\n\nwhere the third equality follows from [Ful98, Theorem 2.4].                                     \u0003\n\n  The next result follows from the Hodge index theorem, compare [YZ10, Theorem 2.1.1].\nProposition 2.21. Suppose θ1 , . . . , θn−1 are semipositive closed (1, 1)-forms. Then the\nsymmetric bilinear form\n                                     Z\n                        (f, g) 7→        f ddc g ∧ θ1 ∧ · · · ∧ θn−1\n                                        X\n\non D(X) is negative semidefinite. In particular, for any two model functions f , g, the\nfollowing Cauchy-Schwarz inequality holds:\n    Z\n       f ddc g ∧ θ1 ∧ · · · ∧ θn−1 ≤\n    X\n              \u0012 Z                            \u00131/2 \u0012 Z                            \u00131/2\n                      c                                   c\n               −  f dd f ∧ θ1 ∧ · · · ∧ θn−1       −  g dd g ∧ θ1 ∧ · · · ∧ θn−1      . (2.4)\n                   X                                     X\n\nProof of Proposition 2.21. Fix a model function f . We need to prove\n                                 Z\n                            I :=   f ddc f ∧ θ1 ∧ · · · ∧ θn−1 ≤ 0\n                                    X\n\nChoose a common determination X of ϕ and all the θi . By continuity, we may assume\nϕ = ϕD for some D ∈ Div0 (X )Q , and each form θi is determined by a Q-line bundle Li on\nX . Then I = D 2 · L1 · . . . · Ln−1 and the result follows from [YZ10, Theorem 2.1.1 (a)]. \u0003\nRemark 2.22. In the complex case we have by Stokes’ theorem\n             Z                               Z\n                f ddc g ∧ θ1 ∧ ... ∧ θn−1 = − df ∧ dc g ∧ θ1 ∧ ... ∧ θn−1 ,\n\n"
        },
        {
          "filename": "source-extracts/1201.0188-bounded-operator-proof.txt",
          "source_line_first": 737,
          "source_line_last": 874,
          "pdf_page_first": 16,
          "pdf_page_last": 19,
          "sha256": "f0af0385a51ebff3dfea084996fce40c6ba449728fe02346175e61e339e691de",
          "literal_text": "In the next three sections we shall develop some of the Bedford-Taylor theory in our non-\nArchimedean setting.\n  Our ﬁrst main objective is to extend the Monge-Ampère operator deﬁned in §2.7 from\nθ-psh model functions to bounded θ-psh functions.\nTheorem 3.1. There exists a unique operator\n                                (ϕ1 , . . . , ϕn ) 7→ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn )\ntaking an n-tuple of bounded θ-psh functions to a positive Radon measure on X of mass\n{θ}n and such that\n     • the definition is compatible with the definition for θ-psh model functions given in §2.7;\n     • for any decreasing nets of bounded θ-psh functions ψ j → ψ, and ϕji → ϕi for i =\n        1, . . . , n we have\n       Z                                                Z\n          ψ j (θ + ddc ϕj1 ) ∧ · · · ∧ (θ + ddc ϕjn ) −→ ψ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn ).\n\nRemark 3.2. One can also prove continuity along increasing nets but we will not need this.\n   Note that the uniqueness part of Theorem 3.1 follows from the fact that any θ-psh function\nis the decreasing limit of a net of θ-psh model functions, see Theorem 2.11. For the same\nreason, the mapping\n                                (ϕ1 , . . . , ϕn ) 7→ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn )\nis symmetric in its arguments, and additive in the following sense:\n     (θ + tddc ϕ1 + (1 − t)ddc ϕ′1 ) ∧ (θ + ddc ϕ2 ) ∧ · · · ∧ (θ + ddc ϕn ) =\n                         t (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn ) + (1 − t) (θ + ddc ϕ′1 ) ∧ · · · ∧ (θ + ddc ϕn )\n\f                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                      17\n\nfor 0 ≤ t ≤ 1. This additivity property in particular implies\n               (θ + ddc (tϕ + (1 − t)ψ))n ≥ tn (θ + ddc ϕ)n + (1 − t)n (θ + ddc ψ)n                     (3.1)\nin the sense of measures, for all bounded θ-psh functions ϕ, ψ, and any 0 ≤ t ≤ 1.\n   Given bounded θ-psh functions, one can now deﬁne signed measures\n                    ddc ϕ1 ∧ · · · ∧ ddc ϕp ∧ (θ + ddc ϕp+1 ) ∧ · · · ∧ (θ + ddc ϕn )\nby writing ddc ϕi = (θ + ddc ϕi ) − θ and expanding the product formally using multilinearity.\nThese products are also continuous along decreasing nets, and we thus obtain\nCorollary 3.3. If ϕ1 , . . . , ϕn−1 are bounded θ-psh functions on X, then the bilinear form\n                              Z\n               (ϕ, ψ) 7→ (−ϕ) ddc ψ ∧ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn−1 )\n\nis well-defined and positive semidefinite on the vector space spanned by the set of bounded\nθ-psh functions.\n   In particular, the Cauchy-Schwarz inequality (2.4) holds for all bounded θ-psh functions\nϕ2 , . . . , ϕn and for all functions ψ, ϕ that are diﬀerences of bounded θ-psh functions.\n3.1. Proof of Theorem 3.1. We adapt to our setting the Bedford-Taylor approach as\nexplained, for instance, in [Dem, Theorem 3.7, p.188].\n   Fix 0 ≤ p ≤ n and θ-psh model functions ϕ′p+1 , . . . , ϕ′n . Consider the following statement.\nAssertion A(p). To any p-tuple ϕ1 , . . . , ϕp of bounded θ-psh functions is associated a positive\nRadon measure M(ϕ1 , . . . , ϕp ) of mass {θ}n such that:\n     • if ϕ1 , . . . , ϕp are model functions then\n M(ϕ1 , . . . , ϕp ) = (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕp ) ∧ (θ + ddc ϕ′p+1 ) ∧ · · · ∧ (θ + ddc ϕ′n ) (3.2)\n      • the mapping                                        Z\n                                (ψ, ϕ1 , . . . , ϕp ) 7→       ψ M(ϕ1 , . . . , ϕp )\n        is continuous along decreasing nets of bounded θ-psh functions.\n  We shall prove A(p) by induction on p. Observe that for p = n, this proves Theorem 3.1.\n  The assertion A(0) is clear, since M(ϕ′1 , . . . , ϕ′n ) is a ﬁnite sum of Dirac masses at divisorial\npoints of X. Assume that A(p − 1) holds for any (n − p + 1)-tuple of θ-psh model functions\nand let ϕ′p+1 , . . . , ϕ′n be θ-psh model functions.\n  Given bounded θ-psh functions ϕ1 , . . . , ϕp , we deﬁne M(ϕ1 , . . . , ϕp ) by forcing the inte-\ngration by parts formula\n  Z\n      ψ M(ϕ1 , . . . , ϕp−1 , ϕp ) :=\n    Z\n       ϕp (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕp−1 ) ∧ (θ + ddc ψ) ∧ (θ + ϕ′p+1 ) ∧ · · · ∧ (θ + ddc ϕ′n )\n       Z\n    + (ψ − ϕp )(θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕp−1 ) ∧ θ ∧ (θ + ϕ′p+1 ) ∧ · · · ∧ (θ + ddc ϕ′n ) (†)\n\nfor every model function ψ.\n\f18                  SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n   Observe that the right-hand side is continuous along decreasing nets as a function of\n(ϕ1 , . . . , ϕp ) by the induction hypothesis. Since equality holds in (†) when all the ϕi are\nmodel functions and since M(ϕ1 , . . . , ϕp ) is a positive measure of mass {θ}n , it follows by\nregularization (Theorem 2.11) that the right-hand side is also linear in ψ, and non-negative\nwhen ψ ≥ 0.\n   Now the space of model functions is spanned by θ-psh model functions by Proposition 2.6;\nhence M(ϕ1 , . . . , ϕp ) is well-deﬁned as a positive measure of mass {θ}n and is continuous\nalong decreasing nets as a function of (ϕ1 , . . . , ϕp ). It remains to show that\n                                                         Z\n                                 (ψ, ϕ1 , . . . , ϕp ) 7→ ψ M(ϕ1 , . . . , ϕp )\n\nis continuous along decreasing nets of bounded θ-psh functions. Let thus (ϕji )j , i = 1, . . . , p\nand ψ j be decreasing nets of θ-psh functions converging, respectively, to bounded θ-psh\nfunctions ϕi and ψ. Set\n                                            µj := M(ϕj1 , . . . , ϕjp ).\nWe already know that µj converges weakly to µ := M(ϕ1 , . . . , ϕp ). Since ψ j is usc for each\nj, Corollary 2.25 yields\n                                      Z         Z\n                               lim sup ψ j µj ≤ ψµ.\n                                                j\n\nFor the reverse estimate, we rely on the following approximate monotonicity property:\nLemma 3.4. Let ψ and χi ≥ ϕi , i = 1, . . . , p be bounded θ-psh functions. Then we have\n        Z                         Z\n           ψ M(χ1 , . . . , χp ) ≥ ψ M(ϕ1 , . . . , ϕp )\n                                          p Z\n                                          X\n                                      +             (ϕi − χi ) M(ϕ1 , . . . , ϕi−1 , 0, χi+1 , . . . , χp ).\n                                          i=1\n\n     The lemma implies that, for each j:\n          Z       Z          Z       X p Z\n             j j        j\n            ψ µ ≥ ψµ ≥ ψµ +                (ϕi − ϕji ) M(ϕ1 , . . . , ϕi−1 , 0, ϕji+1 , . . . , ϕjp ).\n                                                i=1\n\nBy the inductive hypothesis,R the sumRin the right-hand side tends to 0 as j → ∞, so we\ninfer as desired that lim inf j ψ j µj ≥ ψµ.\n\nProof of Lemma 3.4. Note ﬁrst that ψ may be assumed to be a model function by\nLemma 3.5. Let ν be a positive Radon measure on X and let ϕ be a bounded θ-psh function.\nThen we have                      Z           Z\n                                                    ϕν = inf         ψν\n                                                            ψ≥ϕ\n\nwhere ψ ranges over all θ-psh model functions such that ψ ≥ ϕ.\n   Since we already know that (ϕ1 , . . . , ϕp ) 7→ M(ϕ1 , . . . , ϕp ) is continuous along decreas-\ning nets, we may by regularization assume that all ϕi and χi are also model functions.\n\f                  SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                                 19\n\nIntegration by parts (†) then yields\n   Z                             Z\n     ψ M(χ1 , χ2 , . . . , χp ) − ψ M(ϕ1 , χ2 , . . . , χp ) =\n                                   Z                                  Z\n                                 = (χ1 − ϕ1 ) M(ψ, χ2 , . . . , χp ) − (χ1 − ϕ1 ) M(0, χ2 , . . . , χp )\n\nhence\n         Z                             Z                                      Z\n             ψ M(χ1 , . . . , χp ) ≥           ψ M(ϕ1 , χ2 , . . . , χp ) +       (ϕ1 − χ1 ) M(0, χ2 , . . . , χp ).\n\nWe similarly have\n               Z                                              Z\n                      ψ M(ϕ1 , χ2 , χ3 , . . . , χp ) ≥            ψ M(ϕ1 , ϕ2 , χ3 , . . . , χp )\n                                                              Z\n                                                          +       (ϕ2 − χ2 ) M(ϕ1 , 0, χ3 , . . . , χp ).\n\nIterating this argument and summing up then yields the desired result.                                                 \u0003\n\nProof of Lemma 3.5. Let ε > 0. Since ϕ is usc,R LemmaR 2.24 shows that there exists a\ncontinuous function v on X such that v ≥ ϕ and vν ≤ ϕν + ε. The result now follows\nsince [BFJ11, Corollary 8.6] yields an θ-psh model function ψ such that ϕ ≤ ψ ≤ v + ε. \u0003\nDefinition 3.6. A pluripolar set is a subset of {ψ = −∞} for some ψ ∈ PSH(X, θ).\nProposition 3.7. Let ϕ1 , ..., ϕn be bounded θ-psh functions. Then any ψ ∈ PSH(X, θ) is\n"
        },
        {
          "filename": "source-extracts/1201.0188-regularization-locality.txt",
          "source_line_first": 934,
          "source_line_last": 1102,
          "pdf_page_first": 20,
          "pdf_page_last": 24,
          "sha256": "07404bcd0b4ff83a591d9eb53a6b227cc422bac7979e755172dcbfcd695d33aa",
          "literal_text": "Definition 4.1. For any Borel set E ⊆ X, set\n                             \u001aZ                                    \u001b\n              Capω (E) = sup      MA(ϕ) | ϕ ∈ PSH(X, ω), −1 ≤ ϕ ≤ 0 .\n                                    E\n                                                   n\n   By PropositionS 2.19 wePhave 0 ≤ Capω (E) ≤ {ω} . Note that if E1 , E2 , . . . are Borel\nsets, then Capω ( Ej ) ≤ j Capω (Ej ).\n   The Monge-Ampère operator and the capacity of course depend on the choice of ω, but\nwe drop this dependence for notational simplicity.\n\f                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                       21\n\nLemma 4.2. If x ∈ X is a divisorial point, then Capω {x} > 0. As a consequence, every\nnonempty open subset of X has strictly positive capacity.\nProof. The second statement follows from the ﬁrst since divisorial points are dense in X,\nsee §2.1. To prove the ﬁrst statement, pick an SNC model X of X such that x = xE is\nassociated to an irreducible component Eω of the special ﬁber. By [BFJ11, Proposition 5.2]\nthere exists u ∈ D(X) determined on X such that −1 ≤ u ≤ 0 and ω + ddc u is determined\nby an ample class in N 1 (X /S). Then Capω {x} ≥ MA(u){x} = bE ((ω + ddc u)|E )n > 0,\nsee §2.7.                                                                               \u0003\n\n  The next two propositions are the main results of this section.\nProposition 4.3. If ϕ is a bounded ω-psh function then for each ε > 0 there exists an\nopen subset G ⊆ X with Capω (G) < ε and a decreasing sequence (ϕm )∞   m=1 of ω-psh model\nfunctions that converges uniformly to ϕ on G . In particular, ϕ is continuous on Gc .\n                                            c\n\n\nDefinition 4.4. A function h : X → R is said to be quasicontinuous iff it is continuous\noutside sets of arbitrarily small capacity.\n  The previous result can be thus rephrased by saying that bounded ω-psh functions are\nquasicontinuous.\n  Using the same technique we shall replace nets by sequences in the regularization result for\nω-psh functions (Theorem 2.11). While not crucial, this result is psychologically satisfying\nand does simplify the proof of Corollary 7.3 below.\nProposition 4.5. Any ω-psh function ϕ is the limit of a decreasing sequence (ϕm )∞\n                                                                                 m=1 of\nω-psh model functions.\n  The rest of this section is devoted to the proof of these two propositions. First we state\nand prove two estimates on special Monge-Ampère integrals.\nLemma 4.6. The Monge-Ampère measure of any bounded ω-psh is linearly bounded by the\ncapacity. More precisely, if u is an ω-psh function such that −M ≤ u ≤ 0, where M ≥ 1,\nthen\n                                    MA(u) ≤ M n Capω\non Borel sets.\nProof. Given a Borel set E ⊂ X we have\n Z            Z               Z                 Z\n                                                         u\n     MA(u) = (ω + ddc u)n ≤ (M ω + ddc u)n = M n (ω + ddc )n ≤ M n Capω (E).\n   E           E                E                E       M\nHere the ﬁrst inequality follows by writing M ω + ddc u = (M − 1)ω + ω + ddcu and expanding\nthe Monge-Ampère measure by multilinearity.                                             \u0003\nLemma 4.7. Suppose ϕ, ψ and ϕ1 , . . . , ϕn are bounded ω-psh functions such that −M ≤\nϕ ≤ ψ ≤ 0 and −M ≤ ui ≤ 0, where M ≥ 1. Then\n                Z                                  \u0012Z                \u00131\n                                                                   ϕ 2n\n             0 ≤ (ψ − ϕ) MA(ϕ1 , . . . , ϕn ) ≤ 4M    (ψ − ϕ) MA( )       .\n                                                                   2\n\f22             SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\nProof. After regularizing we may assume that all functions involved are model functions.\nWrite, symbolically, T = (ω + ddc ϕ2 ) ∧ · · · ∧ (ω + ddc ϕn ). Then\n           Z                               Z                    Z\n             (ψ − ϕ) MA(ϕ1 , . . . , ϕn ) = (ψ − ϕ)ω ∧ T + (ψ − ϕ) ddc ϕ1 ∧ T.\n         R\nSince 0 ≤ (ψ − ϕ)ω ∧ T ≤ M , the ﬁrst term in the right-hand side satisﬁes\n                     Z                      \u0012Z               \u00131\n                                          1                    2\n                       (ψ − ϕ)ω ∧ T ≤ M 2       (ψ − ϕ)ω ∧ T     .\n\nBy the Cauchy-Schwarz inequality (Corollary 3.3), the second term is bounded by\n                 \u0012Z                        \u0013 1 \u0012Z                    \u00131\n                                             2                        2\n                               c                             c\n                    (ψ − ϕ) dd (ϕ − ψ) ∧ T          (−ϕ1 ) dd ϕ1 ∧ T\n                                      R\nBy the assumption that −M ≤ u1 ≤ 0 and ω n = 1 we have\n               Z                  Z          Z\n           0 ≤ (−ϕ1 ) dd ϕ1 ∧ T = ϕ1 ω ∧ T − ϕ1 (ω + ddc ϕ1 ) ∧ T ≤ M.\n                        c\n\n\nSimilarly,\n       Z                      Z                        Z\n  0 ≤ (ψ − ϕ) dd (ϕ − ψ) ∧ T = (ψ − ϕ)(ω + dd ϕ) ∧ T − (ψ − ϕ)(ω + ddc ψ) ∧ T\n                c                            c\n\n                              Z\n                             ≤ (ψ − ϕ)(ω + ddc ϕ) ∧ T.\n\nPutting this together, and using the concavity of the square root, we get\n  Z\n    (ψ − ϕ) MA(ϕ1 , . . . , ϕn ) ≤\n                       \u0012Z                  \u00131       \u0012Z                               \u00131 !\n                   1                        2                                          2\n               M   2        (ψ − ϕ)ω ∧ T        +        (ψ − ϕ)(ω + ddc ϕ) ∧ T\n\n                                                                        \u0012Z                              \u00131\n                                                                                            cϕ\n                                                                    1                                    2\n                                                             ≤ 2M   2        (ψ − ϕ)(ω + dd       )∧T        .\n                                                                                              2\n                                                         1\nThe lemma follows (with the constant 4M/(2M ) 2n < 4M ) by repeating this argument n − 1\ntimes, successively replacing ϕ2 , . . . , ϕn by ϕ/2.                                 \u0003\nProof of Proposition 4.3. Let (ϕj )j be a decreasing net of ω-psh model functions converging\nto ϕ. We may assume that −M ≤ ϕj ≤ 0 for all j, where M ≥ 1. For any ω-psh function\nψ with −1 ≤ ψ ≤ 0 it follows from Lemma 4.7 that\n                       Z                          \u0012Z                 \u00131\n                                                                   ϕ 2n\n                   0 ≤ (ϕj − ϕ) MA(ψ) ≤ 4M            (ϕj − ϕ) MA( )\n                                                                   2\nand the right hand side tends to zero as j → ∞ by Theorem 3.1. It therefore follows from\nthe deﬁnition of the capacity and from Chebyshev’s inequality that for each integer m ≥ 1\n                                                          1\nthere exists jmSsuch that the open set Gm := {ϕjm − ϕ > m   } has capacity 2−m ε. We can\nthen set G := m Gm and ϕm := ϕjm .                                                     \u0003\n\f                  SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                            23\n\nProof of Proposition 4.5. As above let (ϕj )j be a decreasing net of ω-psh model functions\nconverging to ϕ. After adding a constant we may assume that ϕj ≤ 0 for all j. For\neach integer m ≥ 1, the net (max{ϕj , −m})j decreases to the bounded ω-psh function\nmax{ϕ, −m}. We can therefore choose jm such that\n          Z                                       \u0012              \u0013\n                                                    max{ϕ, −m}              n+1\n      0 ≤ (max{ϕjm , −m} − max{ϕ, −m}) MA                          ≤ (2m)−2 .        (4.1)\n                                                          2\nWe may further assume jm+1 ≥ jm for all m. Set ϕm := ϕjm . We claim that the decreasing\nsequence (ϕm )∞\n              m=1 converges to ϕ. By Theorem 2.10 it suﬃces to test this at any divisorial\npoint x ∈ X. We have 0 ≥ ϕ(x) > −∞ and ϕm (x) ≥ ϕ(x) ≥ −m for m ≥ −ϕ(x) ≥ 0.\nBy (4.1), Lemma 4.7 and the deﬁnition of capacity we get\n                                                             1\n                            0 ≤ (ϕm (x) − ϕ(x)) Capω {x} ≤\n                                                             m\nfor m ≥ |ϕ(x)|. Now Capω {x} > 0 by Lemma 4.2, thus ϕm (x) converges to ϕ(x), which\nconcludes the proof.                                                                    \u0003\n\n                       5. Locality and the comparison principle\n   Let ω be a form as in §4 with {ω}n = 1. In this section we prove the following analogue\nof [BT87, Proposition 4.2].\nTheorem 5.1. If ϕ and ψ are bounded ω-psh functions, then\n                          1{ϕ>ψ} MA(max{ϕ, ψ}) = 1{ϕ>ψ} MA(ϕ).                              (5.1)\n  A ﬁrst consequence is the fact that our operator MA is local in nature, something that is\nnot an immediate consequence of our deﬁnition in §3.\nCorollary 5.2. Suppose ϕ, ψ are bounded ω-psh functions that agree on an open set G ⊆ X.\nThen MA(ϕ) = MA(ψ) on G.\nProof. Given ε > 0 we apply Theorem 5.1 to ϕ + ε and ψ. This gives MA(max{ϕ + ε, ψ}) =\nMA(ϕ) on G ⊆ {ϕ+ε > ψ}. Letting ε → 0 and using Theorem 3.1 we get MA(max{ϕ, ψ}) =\nMA(ϕ) on G. Exchanging the roles of ϕ and ψ shows that MA(ϕ) = MA(ψ) on G.           \u0003\n  Another key consequence of Theorem 5.1 is the comparison principle:\nCorollary 5.3. If ϕ and ψ are bounded ω-psh functions, then\n                              Z              Z\n                                  MA(ψ) ≤        MA(ϕ).\n                              {ϕ<ψ}             {ϕ<ψ}\n\nProof. As in [GZ07, Theorem 1.5] the result easily follows from the locality property by\nintegration. More precisely, for any ε > 0 we have\n      Z                             Z                          Z\n  1 = MA(max{ϕ, ψ − ε}) ≥                MA(max{ϕ, ψ − ε}) +        MA(max{ϕ, ψ − ε})\n                                {ϕ<ψ−ε}                            {ϕ>ψ−ε}\n              Z                      Z                   Z                       Z\n      (5.1)\n       =             MA(ψ − ε) +             MA(ϕ) =             MA(ψ) + 1 −             MA(ϕ),\n           {ϕ<ψ−ε}                 {ϕ>ψ−ε}             {ϕ<ψ−ε}                 {ϕ≤ψ−ε}\n\nso we obtain the desired estimate by letting ε → 0.                                               \u0003\n\f24               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n     The rest of this section is devoted to the proof of Theorem 5.1. We shall use\n"
        },
        {
          "filename": "source-extracts/1201.0188-energy-E1-proof.txt",
          "source_line_first": 1190,
          "source_line_last": 1400,
          "pdf_page_first": 25,
          "pdf_page_last": 30,
          "sha256": "4e912df83b6e05a5fb5938842f4fdd55289ec74e467ea654a64c303e376b7087",
          "literal_text": "\n6.1. Energy of model functions. For any model function ϕ we set\n                                    n Z\n                               1 X\n                     Eω (ϕ) =           ϕ(ω + ddc ϕ)j ∧ ω n−j                           (6.1)\n                              n+1\n                                        j=0\n\f26               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\nand call Eω (ϕ) the energy of ϕ. It follows formally from an integration by parts argument,\nsee Proposition 2.20 and [Tia00, Lemma 6.2] that if ϕ, ψ are any two model functions, then\n                                       n Z\n                                 1 X\n            Eω (ψ) − Eω (ϕ) =               (ψ − ϕ)(ω + ddc ϕ)j ∧ (ω + ddc ψ)n−j .    (6.2)\n                               n+1\n                                      j=0\n\nWriting ϕt = (1 − t)ϕ + tψ, and expanding Eω (ϕt ) − Eω (ϕ) in t leads to the following\nformulas for ﬁrst and second derivatives of Eω :\n                                                 Z\n             ′                d\n           Eω (ϕ) · (ψ − ϕ) =         Eω (ϕt ) = (ψ − ϕ) MA(ϕ);                    (6.3)\n                              dt t=0+\n                                                   Z\n             ′′               d2\n           Eω (ϕ) · (ψ − ϕ) = 2        Eω (ϕt ) = n (ψ − ϕ)ddc (ψ − ϕ) MA(ϕ).      (6.4)\n                              dt t=0+\nProposition 6.1. The restriction of Eω to the convex set PSH(X, ω) ∩ D(X) is concave,\nnondecreasing, and satisfies Eω (ϕ + c) = Eω (ϕ) + c for any constant c ∈ R.\nProof. Concavity follows from (6.4) and Proposition 2.21. Monotonicity is a consequence\nof (6.3), and the last equation follows from (6.2) since (ω + ddc ϕ)j ∧ ω n−j is a probability\nmeasure for each j thanks to Proposition 2.19 and the normalization {ω}n = 1.               \u0003\n6.2. Energy of ω-psh functions. For a general ω-psh function ϕ we set\n             Eω (ϕ) := inf {Eω (ψ) | ψ ∈ PSH(X, ω) ∩ D(X), ψ ≥ ϕ} ∈ [−∞, +∞[.\nProposition 6.2. The extension Eω : PSH(X, ω) → [−∞, +∞[ is non-decreasing, concave,\nand satisfies Eω (ϕ + c) = Eω (ϕ) + c for any c ∈ R. It is also upper semicontinuous, and\ncontinuous along decreasing nets\nProof. That Eω is nondecreasing, concave and satisﬁes Eω (ϕ + c) = Eω (ϕ) + c follows\nformally from Proposition 6.1 (using that PSH(X, ω) ∩ D(X) is convex and invariant under\naddition of a constant).\n   Upper semicontinuity is also a direct consequence of these algebraic properties of Eω and\nof Theorem 2.10. Indeed, pick ϕ0 ∈ PSH(X, ω) and t ∈ R such that Eω (ϕ0 ) < t. We need\nto show that Eω (ϕ) < t for ϕ in a neighborhood U of ϕ0 in PSH(X, ω). By deﬁnition, there\nexists ψ0 ∈ PSH(X, ω) ∩ D(X) such that ψ0 ≥ ϕ0 and Eω (ψ0 ) < t − ε for some ε > 0. By\nTheorem 2.10, U := {ϕ ∈ PSH(X, ω) | supX (ϕ − ψ0 ) < ε} is an open neighborhood of ϕ0\nin PSH(X, ω). By (6.2) we have Eω (ϕ) ≤ Eω (ψ0 ) + ε < t for all ϕ ∈ U , which proves upper\nsemicontinuity.\n   Finally, being usc and nondecreasing, Eω is automatically continuous along decreasing\nnets.                                                                                      \u0003\nProposition 6.3. Formulas (6.1)-(6.4) are valid for bounded ω-psh functions.\n     This follows from the continuity of Eω along decreasing nets and from Theorem 3.1.\n6.3. Non-pluripolar Monge-Ampère measures. Let us introduce the class of ω-psh\nfunctions with ﬁnite energy\n                        E 1 (X, ω) := {ϕ ∈ PSH(X, ω) | Eω (ϕ) > −∞} .\nThis is a convex set which contains all bounded ω-psh functions.\n\f                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                       27\n\n    In this section and its sequel, we explain how to extend the Monge-Ampère operator to\nE 1 (X, ω) and prove that its basic properties continue to hold in this more general setting.\n    Consider an arbitrary ω-psh function ϕ. In the sequel we shall use the notation\n                                    ϕhti := max{ϕ, −t}.\nNote that for s > t ≥ 1, {ϕ > −t} = {ϕhsi > −t} and max{ϕhsi , −t} = ϕhti ; hence\nTheorem 5.1 implies\n   1{ϕ>−t} MA(ϕhsi ) = 1{ϕhsi >−t} MA(ϕhsi ) = 1{ϕhsi >−t} MA(ϕhti ) = 1{ϕ>−t} MA(ϕhti ).\n  This equation allows us to introduce\nDefinition 6.4. [BT87, GZ07] The non-pluripolar Monge-Ampère measure MA(ϕ) of any\nω-psh function ϕ is the increasing limit of the measures 1{ϕ>−t} MA(ϕhti ) as t → ∞.\n  Here the limit exists in a very strong sense: we have\n                           lim 1{ϕ>−t} MA(ϕhti )(E) = MA(ϕ)(E)                          (6.5)\n                          t→∞\nfor any Borel set E.\nRemark 6.5. The terminology ”non-pluripolar” comes from the fact that MA(ϕ) does not\nput mass on pluripolar sets. This in turn follows from Proposition 3.7 applied to the bounded\nω-psh function ϕhti and from (6.5).\n  The measure MA(ϕ) is always deﬁned and supported on the set {ϕ > −∞}, but its total\nmass may be strictly less than one.\nDefinition 6.6. A ω-psh function ϕ has full Monge-Ampère mass when MA(ϕ) is a prob-\nability measure.\n  This is the case iﬀ MA(ϕhti ){ϕ ≤ −t} → 0 as t → ∞, and implies that MA(ϕhti ) converges\nweakly to MA(ϕ).\nLemma 6.7. If ϕ ∈ E 1 (X, ω), then MA(ϕhti ){ϕ ≤ −t} = o(t−1 ) as t → ∞; hence ϕ has\nfull Monge-Ampère mass.\nProof. We may assume ϕ ≤ 0. Set µt := MA(ϕhti ). Since (6.2) applies to bounded ω-psh\nfunctions by Proposition 6.3, we get\n                                  Z                          Z t/2 n                  o\n                               1                          1\n  Eω (ϕht/2i ) − Eω (ϕhti ) ≥       (ϕht/2i − ϕhti )µt =          µt ϕht/2i − ϕhti ≥ s ds\n                              n+1                        n+1 0\n                                  Z t/2 n                    o\n                               1                                        t\n                            ≥          µt ϕht/2i − ϕhti ≥ t/2 ds =           µt {ϕ ≤ −t} ,\n                              n+1 0                                 2(n + 1)\nwhere µt = MA(ϕhti ). Since limt→∞ Eω (ϕht/2i ) = limt→∞ Eω (ϕhti ) = Eω (ϕ) by the continu-\nity of Eω along decreasing sequences, the proof is complete.                              \u0003\nLemma 6.8. If 0 ≥ ϕ ∈ E 1 (X, ω) and f ∈ D(X), then\n                Z                Z\n                           hti                 2(n + 1)\n                  f MA(ϕ ) − f MA(ϕ) ≤                  |Eω (ϕ)| sup |f |\n                                                   t              X\nfor any t > 0.\n\f28              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\nProof. We may assume supX |f | = 1. Pick s ≥ t. The probability measures µt := MA(ϕhti )\nand µs agree on {ϕ > −t}. Hence\n   Z        Z                                \u0012Z               Z            \u0013\n                                          1          hti             hsi\n      f µt − f µs ≤ (µt + µs ){ϕ ≤ −t} ≤          −ϕ µt + −ϕ µs\n                                          t\n                                       n+1                                  2(n + 1)\n                                     ≤      (|Eω (ϕhti )| + |Eω (ϕhsi )|) ≤          |Eω (ϕ)|.\n                                        t                                       t\nThe result follows by letting s → ∞.                                                           \u0003\nProposition 6.9. If ϕ ∈ E 1 (X, ω) and (ϕj )j is a decreasing net of ω-psh functions converg-\ning to ϕ, then ϕj ∈ E 1 (X, ω) for all j and MA(ϕj ) → MA(ϕ) as j → ∞ in the weak sense\nof measures.\n                                                        R              R\nProof. Given f ∈ D(X), we have by deﬁnition that f MA(ϕhti ) → f MA(ϕ) as t → ∞\n     R         hti    R\nand f MA(ϕj ) → f MA(ϕj ) as t → ∞ for every j. Moreover, Lemma 6.8 shows that\n                                                                R        hti    R\nthe latter convergence is uniform in j. Since for each t we have f MA(ϕj ) → f MA(ϕhti )\nas j → ∞ by Theorem 3.1, the result follows.                                               \u0003\nLemma 6.10. If ϕ, ψ ∈ E 1 (X, ω) and ϕ, ψ ≤ 0, then we have the estimate\n                              \u0012       \u0013            Z\n                                ϕ+ψ        2−(n+1)\n                    −∞ < E               ≤           (−ψ) MA(ϕ).\n                                  2         n+1\nProof. Pick s, t > 0. Since (6.1) holds for bounded ω-psh functions, we see using (3.1) that\n                      \u0012        \u0013                     !           Z\n                        ϕ+ψ             ϕhti + ψ hsi     2−(n+1)\n            −∞ < E               ≤E                    ≤           ψ hsi MA(ϕhti ).\n                           2                 2            n+1\nSince ψ hsi decreases to ψ at any point of X, the right hand side converges to\n              Z                         Z                             Z\n     2−(n+1)             hti    2−(n+1)                 hti   2−(n+1)\n                 ψ MA(ϕ ) ≤                     ψ MA(ϕ ) =                     ψ MA(ϕ)\n      n+1                        n + 1 {ϕ>−t}                  n + 1 {ϕ>−t}\nby monotone convergence. We obtain the desired estimate by letting t → ∞.                     \u0003\n6.4. Locality and the comparison principle.\nProposition 6.11. For any ϕ, ψ ∈ E 1 (X, ω), we have\n                          1{ϕ>ψ} MA(max{ϕ, ψ}) = 1{ϕ>ψ} MA(ϕ),                             (6.6)\nand the comparison principle holds:\n                             Z                    Z\n                                        MA(ψ) ≤               MA(ϕ).                       (6.7)\n                                {ϕ<ψ}                 {ϕ<ψ}\n\nProof. To prove (6.6), ﬁrst assume ψ = −t, where t ≥ 1. Pick s ≥ t so that ϕhti =\nmax{ϕs , −t}, {ϕ > −t} = {ϕs > −t}, and\n 1{ϕ>−t} MA(ϕhti ) = 1{ϕs >−t} MA(ϕhti ) = 1{ϕs >−t} MA(ϕs ) = 1{ϕ>−t} · 1{ϕ>−s} MA(ϕs ),\nwhere the second equality follows from Theorem 5.1. As s → ∞, 1{ϕ>−s} MA(ϕs )(E) →\nMA(ϕ)(E) for any Borel set E, so the right hand side of the equation above converges to\n1{ϕ>−t} MA(ϕ).\n\f                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                29\n\n  Now consider ϕ, ψ ∈ E 1 (X, ω) and set u = max{ϕ, ψ} ∈ E 1 (X, ω). Then\n     • 1{ϕhti >ψhti } MA(u) = 1{ϕhti >ψhti } MA(uhti ) since {ϕhti > ψ hti } ⊆ {u > −t};\n     • 1{ϕhti >ψhti } MA(uhti ) = 1{ϕhti >ψhti } MA(ϕhti ) by (5.1) applied to ϕhti and ψ, noticing\n       the inclusion {ϕhti > ψ hti } ⊆ {ϕhti > ψ};\n     • 1{ϕhti >ψhti } MA(ϕhti ) = 1{ϕhti >ψhti } MA(ϕ) by the previous step and the inclusion\n       {ϕhti > ψ hti } ⊆ {ϕhti > −t}.\nTo summarize, we get\n                             1{ϕhti >ψhti } MA(u) = 1{ϕhti >ψhti } MA(ϕ).                         (6.8)\nNow\n                 1{ϕhti >ψhti } MA(u) = 1{ϕ>−t≥ψ} MA(u) + 1{ϕ>ψ>−t} MA(u)\nAs t → ∞ the ﬁrst term tends to 0 since MA(u) puts no mass on the pluripolar set {ψ = −∞}\n(see Remark 6.5), and the second term converges to 1{ϕ>ψ>−∞} MA(u) = 1{ϕ>ψ} MA(u).\n   Thus the left-hand side of (6.8) tends to 1{ϕ>ψ} MA(u) as t → ∞. Similarly, the right-\nhand side tends to 1{ϕ>ψ} MA(ϕ). Finally the comparison principle follows exactly as in the\nproof of Corollary 5.3. The proof is complete.                                           \u0003\n6.5. Differentiability.\nProposition 6.12. For any ϕ, ψ ∈ E 1 (X, ω), the function t 7→ Eω ((1 − t)ϕ + tψ) is differ-\nentiable on [0, 1], and we have\n                                                             Z\n                ′                d\n             Eω (ϕ) · (ψ − ϕ) :=         Eω ((1 − t)ϕ + tψ) = (ψ − ϕ) MA(ϕ)           (6.9)\n                                 dt t=0+\nfor any ϕ, ψ ∈ E 1 (X, ω).\nProof. Set h(t) := hϕ,ψ (t) := Eω ((1 − t)ϕ + tψ) for 0 ≤ t ≤ 1. Note that h is a polynomial\nof degree at most n when ϕ and ψ are model functions. By continuity of the energy along\ndecreasing nets, the same is true in general. In particular, h is diﬀerentiable on [0, 1].\n   Pick any decreasing sequence (ψj )∞j=1 of ω-psh model functions converging to ψ. Note that\n                                                                     d\nhϕhsi ,ψj → hϕ,ψ as polynomials when s → ∞ and j → ∞, hence dt              h\n                                                                       t=0+ ϕhsi ,ψj\n                                                                                     → h′ (0+).\nSince (6.9) holds true for bounded functions by Proposition 6.3, it suﬃces to show\n                              Z                         Z\n                                        hsi       hsi\n                    lim lim (ψj − ϕ ) MA(ϕ ) = (ψ − ϕ) MA(ϕ).\n                     j→∞ s→∞\n\nFirst, we have\n             Z                           Z                                 Z\n                  hsi         hsi                               hsi\n                 ϕ      MA(ϕ        )=                (−s) MA(ϕ       )+            ϕ MA(ϕhsi )\n                                             {ϕ≤−s}                        {ϕ>−s}\n                                         Z                                 Z\n                                    =                 (−s) MA(ϕhsi ) +              ϕ MA(ϕ)\n                                             {ϕ≤−s}                        {ϕ>−s}\n\nby (6.6). By LemmaR 6.7 the ﬁrst term of the right hand side tends to 0, and the second\nterm converges to ϕ MA(ϕ) since MA(ϕ) puts no mass on {ϕ = −∞}.\n                                     R                R\n   Second, for ﬁxed j we have lims→∞ R ψj MA(ϕhsi ) R= ψj MA(ϕ) since ψj is continuous.\n   Finally, Lemma 2.23 yields limj→∞ ψj MA(ϕ) = ψ MA(ϕ), completing the proof. \u0003\n\f30              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n                           7. Envelopes and differentiability\n   Let ω be a form as in §4 with {ω}n = 1. As explained in the introduction, the diﬀerentia-\nbility of the energy is not a priori suﬃcient to make the variational approach work, i.e. to\ninfer that a maximizer of the relevant functional over E 1 (X, ω) is necessarily a critical point.\n"
        },
        {
          "filename": "source-extracts/1201.0188-envelope-derivative-proof.txt",
          "source_line_first": 1400,
          "source_line_last": 1545,
          "pdf_page_first": 30,
          "pdf_page_last": 33,
          "sha256": "8859ff10ab4a051d5ffe0234abf9570d9e1c0e8e2f6926ac2af1f5fc2650c670",
          "literal_text": "infer that a maximizer of the relevant functional over E 1 (X, ω) is necessarily a critical point.\nIn order to circumvent this diﬃculty, we show as in [BB10] the diﬀerentiability of Eω ◦ Pω ,\nwhere Pω is the ω-psh envelope operator of §2.5. This idea was originally introduced by\nAlexandrov [Ale38] in the context of real Monge-Ampère equations.\nDefinition 7.1. We say that ω has the orthogonality property if\n                            Z\n                              (f − Pω (f )) MA(Pω (f )) = 0\n\nholds for every f ∈ C 0 (X).\n   Since Pω (f ) ≤ f , this property means that MA(Pω (f )) is concentrated on the contact\nlocus {Pω (f ) = f }. We refer to Appendix A for more information on the orthogonality\nproperty.\n   We can state the main result of this section.\nTheorem 7.2. Assume that ω has the orthogonality property. Then the composition Eω ◦\nPω : C 0 (X) → R is Gâteaux differentiable, with directional derivatives given by\n                                                   Z\n                          d\n                                Eω ◦ Pω (f + tg) = g MA(Pω (f )).\n                         dt t=0\n  Before giving a proof of this crucial result, we state and prove a corollary of it that we\nshall need when solving the Monge-Ampère equation.\n  If ϕ ∈ PSH(X, ω) and f ∈ C 0 (X), observe that Pω (ϕ + f ) is ω-psh (i.e. is not identically\n−∞) since ϕ+f dominates the ω-psh function ϕ+inf X f . Furthermore we have Pω (ϕ+f ) ≤\nϕ + f since the latter is usc.\nCorollary 7.3. Assume that ω has the orthogonality property. Let ϕ ∈ E 1 (X, ω) and f ∈\nC 0 (X). Then Pω (ϕ + tf ) ∈ E 1 (X, ω) for all t ∈ R and\n                                                       Z\n                            d\n                                   Eω ◦ Pω (ϕ + tf ) = f MA(ϕ).\n                            dt t=0\nProof. Note that ϕ + tf ≥ ϕ − |t| supX |f | implies Pω (ϕ + tf ) ≥ ϕ − |t| supX |f |, hence\nPω (ϕ + tf ) ∈ E 1 (X, ω) for all t. We are going to show that\n                                                Z t \u0012Z                    \u0013\n                  Eω ◦ Pω (ϕ + tf ) = Eω (ϕ) +          f MA(Pω (ϕ + sf )) ds.         (7.1)\n                                                0\nFor all t ∈ R. If ϕ is continuous, then the result follows immediately from Theorem 7.2.\n   In general, let (ϕm )∞\n                        m=1 be a decreasing sequence of ω-psh model functions converging to\nϕ, see Proposition 4.5.\n   For each t ∈ R the sequence (Pω (ϕm +tf ))∞m=1 is a decreasing sequence of ω-psh functions,\nand we claim that limm Pω (ϕm + tf ) = Pω (ϕ + tf ). Indeed let ϕ̃t = limm Pω (ϕm + tf ). Since\nϕm + tf ≥ ϕ + tf , we have Pω (ϕm + tf ) ≥ Pω (ϕ + tf ), hence ϕ̃t ≥ Pω (ϕ + tf ). Conversely,\nϕ̃t ≤ Pω (ϕm + tf ) ≤ ϕm + tf for all m, hence ϕ̃t ≤ ϕ + tf and it follows ϕ̃t = Pω (ϕ + tf )\nas required.\n\f                SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                   31\n\n  We apply (7.1) to ϕm :\n                                                Z t \u0012Z                      \u0013\n              Eω (Pω (ϕm + tf )) = Eω (ϕm ) +            f MA(Pω (ϕm + sf )) ds.               (7.2)\n                                                 0\nAs m → ∞, Eω (Pω (ϕm +tf    R )) and Eω (ϕm ) decrease to Eω ◦Pω (ϕ+tf\n                                                                  R    ) and Eω (ϕ), respectively\nand by Proposition 6.9, f MA(Pω (ϕm + sf )) converges to f MA(Pω (ϕ + sf )) for each\ns.R Finally (7.1) follows from (7.2) using dominated convergence in view of the upper bound\n| f MA(Pω (ϕm + sf ))| ≤ supX |f | for all m and all s.                                        \u0003\nProof of Theorem 7.2. We follow the exposition in [BB10, §4.3] very closely. Arguing as in\nCorollary 7.3 we may assume that f, g ∈ D(X). Set µ := MA(Pω (f )). We need to prove\nthat                                                  Z\n                            d\n                                    Eω ◦ Pω (f + tg) = g µ.                          (7.3)\n                            dt t=0+\nAs a ﬁrst step, we linearize the problem and prove that\n                                                        Z\n                      d                         d\n                             Eω ◦ Pω (f + tg) =           Pω (f + tg) µ.                       (7.4)\n                     dt t=0+                    dt t=0+\nDenote the left and right hand sides of (7.4) by a and b, respectively. Note that the one-sided\nderivatives exist since both Eω and Pω are concave.\n  Since Eω is concave on the space of bounded ω-psh functions, the function\n                    [0, 1] ∋ s 7→ h(s) := Eω (sPω (f + tg) + (1 − s)Pω (f ))\nis also concave, hence\n\n  Eω (sPω (f + tg) + (1 − s)Pω (f )) ≤\n                                                                   \u0012Z                              \u0013\n                                     d\n                      Eω ◦ Pω (f ) +        h = Eω ◦ Pω (f ) + s        (Pω (f + tg) − Pω (f ))µ\n                                     dt t=0\nby Proposition 6.3. Taking s = 1 and letting t → 0 yields a ≤ b.\n  To prove the reverse inequality, ﬁx ε > 0. Then there exists δ > 0 such that\n                           Z                   Z\n                      D :=     Pω (f + δg)µ −    Pω (f )µ ≥ δ(b − ε).\n                               X                     X\nSince µ is the diﬀerential of Eω , there exists γ > 0 such that\n    E ((1 − t)Pω (f ) + tPω (f + δg)) ≥ Eω (Pω (f )) + t(D − δε) ≥ Eω (Pω (f )) + tδ(b − 2ε)\nfor 0 ≤ t ≤ γ. The concavity of P yields Pω (f + tδg) ≥ (1 − t)Pω (f ) + tPω (f + δg). Since\nEω is non-decreasing we get\n        Eω ◦ Pω (f + tδg) ≥ E ((1 − t)Pω (f ) + tPω (f + δg)) ≥ E(Pω (f )) + tδ(b − 2ε)\nfor 0 ≤ t ≤ γ. Letting t → 0 and ε → 0 we conclude a ≥ b. This shows that (7.4) holds.\n   In view of (7.4) it remains to show that\n                          Z                                Z\n                             (Pω (f + tg) − Pω (f )) µ = t   gµ + o(t)              (7.5)\n                           X                                X\nas t → 0+.\n\f32              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\n  Since Pω (f ) ≤ f , the orthogonality property implies Pω (f ) = f for µ-a.e. point. We thus\nhave Pω (f + tg) ≤ f + tg = Pω (f ) + tg µ-a.e. We claim that µ(Ωt ) = O(t) with\n                              Ωt := {Pω (f + tg) < Pω (f ) + tg}.\nObserve that |Pω (f + tg) − Pω (f )| ≤ t sup |g| so that the claim implies\n  Z\n     (Pω (f + tg) − Pω (f ) − tg)µ\n   X\n                   Z                               Z\n                =      (Pω (f + tg) − Pω (f ))µ +         (Pω (f + tg) − Pω (f ))µ\n                    Ωt                               X\\Ωt\n                             Z                                   Z\n                          =       (Pω (f + tg) − Pω (f ) − tg) +    tg µ\n                               Ωt                                 X\n                             Z                                                    Z\n                         ≤ t g µ + µ(Ωt ) sup |Pω (f + tg) − Pω (f ) − tg| = t g µ + O(t2 )\n                              X              X                                   X\n\nwhich proves (7.5).\n  The estimate of µ(Ωt ) is based on the comparison principle. Since g is a model function,\nthere exists C ≫ 1, ψ ∈ D(X) such that ψ and ψ + g are Cω-psh by Proposition 2.6. Note\nthat Ωt = {Pω (f + tg) + tψ < Pω (f ) + t(ψ + g)}, and both functions Pω (f + tg) + tψ and\nPω (f ) + t(ψ + g) are (1 + Ct)ω-psh. The comparison principle then yields\n   Z                                            Z\n                        c                    n\n        ((1 + Ct)ω + dd (Pω (f ) + t(ψ + g))) ≤    ((1 + Ct)ω + ddc (Pω (f + tg) + tψ))n\n      Ωt                                              Ωt\n\nBy expanding as polynomials in t, we get\n              ((1 + Ct)ω + ddc (Pω (f ) + t(ψ + g)))n = (ω + ddc Pω (f ))n + O(t)\nand\n           ((1 + Ct)ω + ddc (Pω (f + tg) + tψ))n = (ω + ddc Pω (f + tg))n + O(t).\nFrom these three estimates we conclude\n                          Z                Z\n                 µ(Ωt ) =    MA(Pω (f )) ≤            MA(Pω (f + tg)) + O(t).\n                             Ωt                  Ωt\n\nBut Ωt ⊆ {Pω (f + tg) < f + tg}, so the orthogonality property implies that the last integral\nvanishes. This concludes the proof.                                                        \u0003\nRemark 7.4. Observe that the differentiability property of Theorem 7.2 conversely implies\nthe orthogonality\n      R             property. Indeed, pick f ∈ C 0R(X) and set g := Pω (f ) − f . We claim\nthat g MA(Pω (f )) = 0. It is enough to prove g MA(Pω (f )) ≥ 0 since g ≤ 0. Now the\ndifferentiability property yields\n                                                      Z\n                   Eω (Pω (f + εg)) = Eω (Pω (f )) + ε g MA(Pω (f )) + o(ε).\n\nBut we have\n               f + εg = (1 − ε)f + εPω (f ) ≥ (1 − ε)Pω (f ) + εPω (f ) = Pω (f ),\nhence Eω (Pω (f + εg)) ≥ Eω (Pω (f )) by monotonicity of Eω , and the result follows.\n\f               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                         33\n\n"
        },
        {
          "filename": "source-extracts/1201.0188-uniqueness-existence-proof.txt",
          "source_line_first": 1546,
          "source_line_last": 1717,
          "pdf_page_first": 33,
          "pdf_page_last": 36,
          "sha256": "35acd2635de017dc0f134eee364a72b3c232607fadc5ecd59b222316e96a0268",
          "literal_text": "                             8. The Monge-Ampère equation\n  In this section we prove\nTheorem 8.1. Assume that ω is a form as in §4 with {ω}n = 1 that satisfies the orthog-\nonality property (see Definition 7.1). Let µ be a probability measure on X supported on\nthe dual complex of some SNC model of X. Then there exists a unique, continuous ω-psh\nfunction ϕ ∈ PSH(X, ω) such that MA(ϕ) = µ, and sup ϕ = 0.\n   Let us explain how to deduce Theorems A and A’ from the introduction. Let ω be any\nclosed semipositive form with {ω} ample, and µ be a positive Radon measure of mass {ω}n .\nSet ω̃ := ω/({ω}n )1/n , and µ̃ = µ/{ω}n . Assume that X is algebraizable. It follows from\nAppendix A that ω and ω̃ satisfy the orthogonality property. Applying Theorem 8.1 to ω̃\nand µ̃ yields a unique ϕ̃ ∈ PSH(X, ω̃) such that sup ϕ̃ = 0 and (ω̃ + ddc ϕ̃)n = µ̃. Theorem\nA’ follows since (ω + ddc ϕ)n = µ with ϕ = ({ω}n )1/n ϕ̃.\n   Now consider an ample line bundle L → X endowed with a semipositive model metric\nk · k. The curvature form ω = c1 (L, k · k) is semipositive and {ω}n = c1 (L)n in view\nof Proposition 2.19 and (2.1). Given any positive Radon measure µ of mass c1 (L)n and\nsupported on the dual complex of some SNC model of X, Theorem A’ thus implies the\nexistence of a unique continuous ω-psh function ϕ such that MA(ϕ) = µ, and sup ϕ = 0.\nThis statement implies Theorem A since c1 (L, k · ke−ϕ )n = MA(ϕ) by deﬁnition.\n  For the rest of this section is a form as in §4 normalized by {ω}n = 1\n\n8.1. Uniqueness. The uniqueness statement in Theorem 8.1 does not require the orthog-\nonality property. Following [Blo03] as in [GZ07, YZ10], one actually proves:\nProposition 8.2. Let ω be any semipositive closed (1, 1) form. Suppose MA(ϕ) = MA(ψ)\nfor any two functions ϕ, ψ ∈ E 1 (X, ω). Then ϕ − ψ is constant.\nProof. For simplicity we write ωϕ = ω + ddc ϕ.\n   First we brieﬂy indicate how to extend to ω-psh of ﬁnite energy the calculus that we\ndeveloped in §3. Let ϕ, ψ ∈ E 1 (X, ω). Since Eω is convex, (1 − t)ϕ + tψ ∈ E 1 (X, ω) for any\nt ∈ [0, 1]. For any 0 ≤ i ≤ n, deﬁne ωϕi ∧ ωψn−i to be the unique probability measure such\nthat\n  X \u0012n \u0013\n  n−1\n            (1 − t)k tn−k ωϕk ∧ ωψn−k = MA((1 − t)ϕ + tψ) − (1 − t)n MA(ϕ) − tn MA(ψ) (8.1)\n        k\n k=0\n\nfor any t = j/n with 1 ≤ j ≤ n − 1. By Proposition 6.9, we get ωϕi j ∧ ωψn−i\n                                                                          j\n                                                                             → ωϕi ∧ ωψn−i for\nany decreasing sequence of ω-psh functions ϕj → ϕ and ψj → ψ. In particular, ωϕi ∧ ωψn−i is\na probability measure. Replacing MA(·) = (ω + ddc ·)n by (ω + ddc ·)i+j ∧ ω n−(i+j) in (8.1),\nwe can further deﬁne probability measures of the same mass ωϕi ∧ ωψj ∧ ω n−(i+j) as soon as\ni, j ≥ 0 and i + j ≤ n.\n    Observe that by deﬁnition and Lemma 6.10, these measures integrate ω-psh functions of\nﬁnite energy. By continuity, it also follows that the Cauchy-Schwarz inequality holds\n                   Z                \u0012Z              \u00131/2 \u0012Z           \u00131/2\n                          c                  c                 c\n                     −hdd g ∧ T ≤         hdd h ∧ T         gdd g ∧ T\n\f34              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\nfor any h, g lying in the vector space generated by E 1 (X, ω) and for any T a positive linear\ncombination of measures of the type ωϕi ∧ ωψj ∧ ω n−(i+j) with i + j ≤ n and ϕ, ψ ∈ E 1 (X, ω).\n     Now pick ϕ, ψ ∈ E 1 (X, ω). We claim that\n            Z                                  \u0012Z                       \u001321−n\n                          c           n−1\n              (ϕ − ψ)dd (ϕ − ψ) ∧ ω       ≤C      (ψ − ϕ)(MA(ϕ) − MA(ψ))                   (8.2)\n\nfor some constant C depending on ϕ and ψ.\n   Grant this claim, and suppose MA(ϕ) = MA(ψ). We conclude the proof as in [YZ10].\nWe may assume sup ϕ = sup ψ. By Cauchy-Schwarz inequality, for any model function h we\nget\n           Z                               Z                            1/2\n              (ϕ − ψ)ddc h ∧ ω n−1 ≤ D 1/2   (ϕ − ψ)ddc (ϕ − ψ) ∧ ω n−1     =0,\n                R\nwith 0 ≤ D := −hddc h ∧ ω n−1 < +∞. Let L be any R-line bundle in a model X whose\nnumericalPclass is equal to ω. The above equality\n                                            P     applied to the model function determined\nin X by E bE (ϕ − ψ)(ordE )E with X0 =        bE E yields\n                                                    !2\n                             X\n                                 bE (ϕ − ψ)(ordE )E    · Ln−1 = 0\n                               E\n                        P\nwhich in turn implies E bE (ϕ − ψ)(ordE )E to be proportional to X0 by [YZ10, Theorem\n2.1.1(b)]. Since we normalized ϕ, ψ by sup ϕ = sup ψ, we conclude that ϕ = ψ on the\nvertices of ∆X .\n   Now consider any (suﬃciently) high model π : X ′ → X . By [BFJ11, Proposition 5.2]\nthere exists a model function h such that ω ′ = ω + ddc h is induced by a ample divisor in X ′ .\nThen the functions ϕ − h and ψ − h are both ω ′ -psh, normalized by sup(ϕ − h) = sup(ψ − h),\nand satisfy (ω ′ + ddc (ϕ − h))n = (ω ′ + ddc (ψ − h))n . By what precedes we get ϕ = ψ on the\nvertices of X ′ . This implies ϕ = ψ on X div , hence on X qm by Proposition 2.8, hence on X\nsince ϕ = supX ϕ ◦ pX for any ω-psh function by [BFJ11, Proposition 7.6].\n   We now prove the claim. For this we reproduce the argument of [Blo03]. By C we will\ndenote possibly diﬀerent constants depending on ω, ϕ, ψ. Set ρ = ϕ−ψ. For k = 0, 1, ..., n−1\nwe will prove inductively that\n                                 Z\n                                                                   −k\n                            0 ≤ −ρddc ρ ∧ ωϕi ∧ ωψj ∧ ω k ≤ Ca2\n\nwhere                   Z                                  Z\n                   a=       (ψ − ϕ)(MA(ϕ) − MA(ψ)) =           −ρddc ρ ∧ T ≥ 0\n          Pn−1 l\nwith T = l=0     ωϕ ∧ ωψn−1−l , and i, j are such that i + j + k = n − 1. For k = n − 1 we will\nthen obtain the desired estimate.\n  If k = 0, then           Z                        Z\n                               ρddc ρ ∧ ωϕi ∧ ωψj ≤    ρddc ρ ∧ T = a\n\nAssume that (3.1) holds for 0, 1, ..., k − 1. We have\n                             ωϕi ∧ ωψj ∧ ω k = ωϕi+k ∧ ωψj − ddc ϕ ∧ α\n\f                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                        35\n\nwhere\n                                                                 k−1\n                                                                 X\n                                             α = ωϕi ∧ ωψj ∧           ωϕl ∧ ω k−1−l\n                                                                 l=0\nTherefore\n                 Z                                         Z\n            0≤       −ρdd ρ ∧ ωϕi ∧ ωψj ∧ ω k ≤\n                                c\n                                                           −ρddc ρ ∧ (T − ddc ϕ ∧ α)\n                                                           Z             Z\n                                                        = − ρdd ρ ∧ T − ρddc ϕ ∧ α ∧ ddc ρ\n                                                               c\n\n\nThis means that\n                            Z                                               Z\n                     0≤             −ρdd ρ ∧ ωϕi ∧ ωψj ∧ ω k ≤ a −\n                                         c\n                                                                                  ρddc ϕ ∧ α ∧ ddc ρ.\n\nWe have\n                Z                                   Z                                Z\n                        c                     c              c\n            −        ρdd ϕ ∧ α ∧ dd ρ ≤                 ρdd ϕ ∧ α ∧ ωϕ +                 ρddc ϕ ∧ α ∧ ωψ .\n\nIf η is equal to ϕ or ψ, the Cauchy-Schwarz inequality gives\n            Z                    \u0012Z                 \u00131/2 \u0012Z                 \u00131/2\n                  c                     c                       c\n               ρdd ϕ ∧ α ∧ ωη ≤      ρdd ρ ∧ α ∧ ωη          ϕdd ϕ ∧ α ∧ ωη\n                                     R                  −(k−1)\nBy the Rinductive assumption, we have −ρddc ρ∧α∧ωη ≤ Ca2       , and since ϕ ∈ E 1 (X, ω)\nwe get −ϕddc ϕ ∧ α ∧ ωη < +∞. The proof is complete.                                   \u0003\n\n8.2. Existence. As in [BBGZ09], the strategy is to ﬁrst use a variational argument going\nback to Alexandrov [Ale38] in order to produce a solution ϕ ∈ E 1 (X, ω).\n   Consider the functional Fµ : PSH(X, ω) → [−∞, +∞[ deﬁned by\n                                                   Z\n                                 Fµ (ϕ) := Eω (ϕ) − ϕµ.                             (8.3)\n\n   We ﬁrst claim that FRµ is usc on PSH(X, ω). By Proposition 6.2, Eω is usc so that it is\nsuﬃcient to prove ϕ 7→ ϕµ is continuous on PSH(X, ω). Pick a net ϕk → ϕ in PSH(X, ω),\ni.e. ϕk (x) → ϕ(x) for any x ∈ X div . Since divisorial points are dense in ∆X by [JM10],\nand the family {ϕk |R∆X } is equicontinuous\n                               R             by Theorem 2.9, it follows that ϕk |∆X → ϕ|∆X\nuniformly. Whence ϕk µ → ϕµ since ∆X contains the support of µ by assumption.\n   Now write PSH0 (X, ω) := {ϕ ∈ PSH(X, ω) | sup ϕ = 0}, and observe that Fµ (ϕ + c) =\nFµ (ϕ) for any constant c by Proposition 6.2, so that supPSH(X,ω) Fµ = supPSH0 (X,ω) Fµ . Since\nFµ is usc, and PSH0 (X, ω) is compact by Theorem 2.10, it actually attains its maximum.\nWe can thus ﬁnd ϕ ∈ PSH0 (X, ω) such that\n                                                  Fµ (ϕ) =        sup      Fµ .\n                                                             PSH(X,ω)\n\nClearly Eω (ϕ) > −∞, so ϕ ∈ E 1 (X, ω). Let us show that MA(ϕ) = µ. Pick any model\nfunction f ≤ 0 on X. For t ∈ R, consider the function\n                                                   Z\n                         h(t) = Eω ◦ Pω (ϕ + tf ) − (ϕ + tf )µ.\n\f36               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\n\nIn view of Corollary 7.3, h(t) is diﬀerentiable at t = 0 with derivative\n                                        Z               Z\n                                  ′\n                                 h (0) = f MA(ϕ) − f µ.\n\nBut since Pω (ϕ + tf ) ≤ ϕ + tf ≤ 0, it follows that h(t) ≤ Fµ ◦ Pω (ϕ + tf\n                                                                         R ) ≤ FµR(ϕ) = h(0)\nfor all t. Thus h has a local maximum at t = 0, so h′ (0) = 0, that is f µ = f MA(ϕ).\nThis implies MA(ϕ) = µ, as f was an arbitrary model function.\n\n8.3. Continuity. Finally we show that ϕ is continuous. For this we use capacity estimates\nin the spirit of Kolodziej [Kol98, Kol03]; see also [EGZ09]. The following result (and its\nproof) is a translation of [EGZ09, Lemma 2.3].\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "1805.01016",
      "public_source": "https://arxiv.org/pdf/1805.01016v3",
      "saved_version": "1805.01016v3",
      "application_check": "Scope audit only: actual v3 is Boucksom-Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. Not a general finite-energy surjectivity theorem; no theorem from it is needed in the positive-residue proof.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.pdf",
          "bytes": 1034400,
          "sha256": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
          "bytes": 344553,
          "sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
          "matches_supplied_hash": true
        },
        {
          "kind": "abstract_html",
          "path": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.html",
          "bytes": 41303,
          "sha256": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/1805.01016-title-and-scope.txt",
          "source_line_first": 1,
          "source_line_last": 99,
          "pdf_page_first": 1,
          "pdf_page_last": 2,
          "sha256": "a38562aa122a73e7acffbab38169e477f1d8ea864237305d6330cfa5c8310b54",
          "literal_text": "                                              SPACES OF NORMS, DETERMINANT OF COHOMOLOGY AND\n                                                 FEKETE POINTS IN NON-ARCHIMEDEAN GEOMETRY\n\n                                                                  SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\narXiv:1805.01016v3 [math.AG] 8 Jan 2021\n\n\n\n\n                                                 Abstract. Let L be an ample line bundle on a (geometrically reduced) projective variety\n                                                 X over any complete valued field. Our main result describes the leading asymptotics of\n                                                 the determinant of cohomology of large powers of L, with respect to the supnorm of a\n                                                 continuous metric on the Berkovich analytification of L. As a consequence, we establish\n                                                 in this setting the existence of transfinite diameters and equidistribution of Fekete points,\n                                                 following a strategy going back to Berman, Witt Nyström and the first author for complex\n                                                 manifolds. In the non-Archimedean case, our approach relies on a version of the Knudsen–\n                                                 Mumford expansion for the determinant of cohomology on models over the (possibly non-\n                                                 Noetherian) valuation ring, as a replacement for the asymptotic expansion of Bergman\n                                                 kernels in the complex case, and on the reduced fiber theorem, as a replacement for the\n                                                 Bernstein–Markov inequalities. Along the way, a systematic study of spaces of norms and\n                                                 the associated Fubini–Study type metrics is undertaken.\n\n\n\n\n                                                                                        Contents\n                                            Introduction                                                                                         2\n\n                                          Part 1. Spaces of norms and determinants                                                                8\n                                            1. Spaces of norms                                                                                    8\n                                            2. Determinants and relative spectra                                                                 19\n                                            3. Alternative metric structures on spaces of norms                                                  27\n\n                                          Part 2. Models and metrics                                                                             31\n                                            4. Analytification and models                                                                        31\n                                            5. Fubini–Study metrics and model metrics                                                            37\n                                            6. The supnorm of a metric                                                                           43\n                                            7. Plurisubharmonic metrics and envelopes                                                            47\n\n                                          Part 3. Asymptotics of relative volumes                                                                55\n                                            8. Monge–Ampère measures and Deligne pairings                                                       55\n                                            9. Asymptotics of relative volumes                                                                   68\n                                            10. Transfinite diameter and Fekete points                                                           77\n                                            Appendix A. Determinant of cohomology and Deligne pairings                                           84\n                                            References                                                                                           96\n\n\n                                            Date: January 11, 2021.\n                                                                                              1\n\f2                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\n\n                                        Introduction\n   Fekete points and transfinite diameter are classical notions in logarithmic potential theory\nin the plane. For each m ∈ N, the m-diameter δm (K) of a compact subset K ⊂ C is defined\nas the supremum of the geometric mean distance between m + 1 points in K, maximizers\nbeing called Fekete configurations. The m-diameter of K admits a limit δ∞ (K) as m →\n∞, called the transfinite diameter of K, which turns out to coincide with the logarithmic\ncapacity of K. Further, Fekete configurations become asymptotically unique in the limit, in\nthe sense that they equidistribute to a certain canonical probability measure on K, called\nits equilibrium measure.\n   In several complex variables, a similar picture was only rather recently obtained. The\nfirst steps were taken by Leja in the 1950’s, introducing a notion of m-diameter δm (K) for\na compact subset K ⊂ Cn , defined in terms of the supremum of certain Vandermonde-\ntype determinants. The existence of the transfinite diameter δ∞ (K) = limm→∞ δm (K) was\nestablished by Zaharjuta [Zah75], and the next key step came with Rumely’s observation\nin [Rum07] that the general results in arithmetic intersection theory developed in [CLR03]\nyield in particular an exact formula for δ∞ (K) in terms of pluripotential theory, generalizing\nthe classical Robin formula for the logarithmic capacity in the plane, and involving plurisub-\nharmonic envelopes and mixed Monge–Ampère operators in the sense of Bedford–Taylor.\nThis triggered joint work of the first author with Berman and Witt Nyström [BB10, BBW11],\nwhich built on Bergman kernel asymptotics to establish a general version of Rumely’s for-\nmula in the setting of complex projective manifolds, and combined it with a variational\nargument to prove the equidistribution of Fekete configurations in this context.\n   The main purpose of the present paper is to study versions of these results in non-\nArchimedean (Berkovich) geometry. While many results hold over an arbitrary non-Archimedean\ncomplete valued field K, the full picture relies on more refined non-Archimedean pluripo-\ntential theory as developed in [BFJ16, BFJ15, BG+16, BJ18a], and hence requires K to be\ntrivially or discretely valued and of residue characteristic 0.\n\nAsymptotics of relative volumes. The Bouche–Catlin–Tian–Zelditch asymptotic expan-\nsion of Bergman kernels [Bou90, Cat99, Tia90, Zel98] is a fundamental result in complex\ngeometry, which describes the asymptotic behavior of the L2 -norms associated to large ten-\nsor powers of a positive Hermitian line bundle. As noticed in [BB10], it can be reformulated\nas an asymptotic expansion for the logarithmic volume ratio of such L2 -norms, as follows.\n   First, define the relative volume of any two norms k · k, k · k′ on an N -dimensional complex\nvector space V as                                          \u0012            \u0013\n                                                 ′           det k · k′\n                                 vol(k · k, k · k ) := log                ,                 (0.1)\n                                                              det k · k\n                                                                                           V\nwhere det k · k, det k · k′ denote the induced norms on the determinant line det V = N V .\nIn terms of the unit balls B, B ′ ⊂ V of the two norms,\n                                                     \u0012         \u0013\n                                         ′     1       vol B\n                         vol(k · k, k · k ) = log                + O(N log N ),\n                                               2       vol B ′\nwhere the error term O(N log N ) vanishes when the two norms are Hermitian.\n  Let next X be an n-dimensional complex projective manifold. Every smooth, positively\ncurved metric φ on an (ample) line bundle L over X induces, for each m ∈ N, an L2 -norm\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "1801.08229",
      "public_source": "https://arxiv.org/pdf/1801.08229v4",
      "saved_version": "1801.08229v4",
      "application_check": "Scope audit and proof comparison only: actual v4 concerns a trivially valued field. Theorem 12.9, including its dimension-at-most-two endpoint, is not applied to k((t)). The analogous variational proof motivates the new explicit finite-energy integration argument but is not transplanted as a theorem.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
          "bytes": 1627763,
          "sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
          "bytes": 506945,
          "sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "matches_supplied_hash": true
        },
        {
          "kind": "abstract_html",
          "path": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.html",
          "bytes": 39270,
          "sha256": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/1801.08229-title-and-standing.txt",
          "source_line_first": 1,
          "source_line_last": 110,
          "pdf_page_first": 1,
          "pdf_page_last": 3,
          "sha256": "46803a9cea066372ea756ebf20826a60ef29d83d92d13e67b3498d676598f622",
          "literal_text": "                                           GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED\n                                                                   FIELD\n\n                                                                   SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\narXiv:1801.08229v4 [math.AG] 22 Mar 2022\n\n\n\n\n                                                  Dedicated to Ahmed Zeriahi for all his contributions to complex analysis and geometry\n\n\n                                                Abstract. We develop global pluripotential theory in the setting of Berkovich geometry\n                                                over a trivially valued field. Specifically, we define and study functions and measures of\n                                                finite energy and the non-Archimedean Monge–Ampère operator on any (possibly reducible)\n                                                projective variety. We also investigate the topology of the space of valuations of linear\n                                                growth, and the behavior of psh functions thereon.\n                                                   Nous développons une théorie du pluripotentiel global dans le contexte de la géométrie de\n                                                Berkovich sur un corps trivialement valué. Plus précisément, nous définissons et étudions\n                                                des fonctions et mesures d’énergie finie et un opérateur de Monge–Ampère non-archimédien\n                                                sur toute variéte projective (éventuellement réductible). Nous explorons également la topolo-\n                                                gie de l’espace des valuations à croissance linéaire, et le comportement des fonctions psh\n                                                sur celui-ci.\n\n\n\n\n                                                                                         Contents\n                                           Introduction                                                                                               2\n                                           1. Berkovich analytification and test configurations                                                      10\n                                           2. Piecewise linear and Fubini–Study functions                                                            20\n                                           3. Plurisubharmonic functions and energy pairing: the PL case                                             33\n                                           4. Plurisubharmonic functions                                                                             44\n                                           5. Envelopes and negligible sets                                                                          56\n                                           6. Homogeneous functions and b-divisors                                                                   63\n                                           7. Functions of finite energy and mixed Monge–Ampère measures                                            74\n                                           8. Differentiability of the extended energy functional                                                    94\n                                           9. Measures of finite energy                                                                              99\n                                           10. The strong topology on M1                                                                            108\n                                           11. Valuations of linear growth                                                                          114\n                                           12. The strong topology on E 1 and the Calabi–Yau theorem                                                120\n                                           13. Capacities, pluripolar sets, and negligible sets                                                     126\n                                           Appendix A. Dual complexes and PL functions                                                              135\n                                           Appendix B. The toric case                                                                               137\n                                           References                                                                                               139\n\n\n\n                                           Date: March 24, 2022.\n                                                                                               1\n\f2                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n                                        Introduction\n   The main purpose of the present paper is to lay the foundations of pluripotential theory\nin the setting of Berkovich geometry over a trivially valued field, paralleling as much as\npossible the known theory in the complex analytic case.\n   Pluripotential theory is a crucial tool in complex analysis and geometry, and A. Zeriahi has\nbeen a central protagonist in the story of its development. For an excellent introduction, see\nthe book by V. Guedj and A. Zeriahi [GZ17]. This theory lies at the heart of the variational\napproach to complex Monge–Ampère equations [BBGZ13], which proved particularly fruitful\nin relation to Kähler–Einstein metrics, and ultimately led to a new proof of the Yau–Tian–\nDonaldson (YTD) conjecture for Fano manifolds [BBJ21], later generalized to (log terminal)\nFano varieties [LTW19, Li19].\n   There are several reasons for developing a corresponding theory over a trivially valued\nfield, that is, any field equipped with the trivial (non-Archimedean) valuation. First, the\nBerkovich approach to non-Archimedean geometry is the one closest to the complex ana-\nlytic intuition, and it is natural to see to what extent the complex analytic theory admits\na counterpart in the setting of Berkovich spaces. Second, Berkovich spaces over a triv-\nially or discretely valued field can often be used to study degenerations in complex geome-\ntry [FJ05a, FJ05b, FJ07, FJ11, BoJ17, BHJ19, Shi19], and such degenerations are central\nto the variational approach to the YTD conjecture [BBJ21, Li20], through the notion of\ngeodesic rays.\n   The thrust of the YTD conjecture is to relate the existence of a solution to a non-linear\nPDE to an algebro-geometric condition known as K-stability, which has recently also come\nto play a key role in the study of moduli spaces, especially for Fano varieties. [ABHX20,\nBHLX21, BLX19, LXZ21, XZ20]. The relation of K-stability with spaces of valuations and\nnon-Archimedean geometry over trivially valued fields, originally pointed out in [BHJ17], is\none major motivation to endeavor the present study, and will be further exploited in the\ncompanion papers [BoJ21, BoJ22].\n   K-stability of a polarized projective variety (X, L) over an algebraically closed field k is a\ncondition phrased in terms of Gm -equivariant degenerations (X , L) → A1 of (X, L) known\nas test configurations [Don02]. Our basic proposal, which goes back to [BHJ17], consists in\ninterpreting (X , L) in terms of a piecewise linear function ϕL on the Berkovich analytification\nX an with respect to the trivial absolute value on the ground field k. To readers familiar with\nnon-Archimedean geometry, this will sound very natural indeed: the base change of a test\nconfiguration (X , L) by Spec k[[$]] → A1 = Spec k[$] provides a model for the base change\n(XK , LK ) to the non-Archimedean field K = k(($)), and hence a model/PL metric on the\nBerkovich analytification Lan           an\n                               K → XK . This metric can further be canonically identified\nwith a PL function on XK , thanks to the reference metric on Lan\n                            an\n                                                                      K induced by the trivial\nmodel, and ϕL is simply the restriction of this function to X an ,→ XK an , the embedding being\n\nrealized by Gauss extension.\n   While this point of view was basically the one adopted in a previous version of this\narticle [BoJ18a], we have tried here to take a more elementary and self-contained approach,\navoiding for the most part any explicit reference to general Berkovich geometry—which\naccounts in part for the length of the present article.\n\f               GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                  3\n\nFunctions and measures of finite energy. Let k be an arbitrary algebraically closed\nfield, and X an irreducible1 projective variety over k, with function field k(X). In order to\ndescribe more precisely our main results, recall first that the Berkovich analytification X an\nof X with respect to the trivial valuation on k is a compactification of the space X val of\nvaluations v : k(X)× → R, trivial on k, endowed with the topology of pointwise convergence.\nPoints of X an can be understood as semivaluations v on X, i.e. valuations v ∈ Y val for some\nsubvariety Y ⊂ X. The set X div ⊂ X val of divisorial valuations, which are attached to\nprime divisors over X, is dense in X an .\n   For every v ∈ X an and every section s ∈ H0 (X, mL), m ∈ N, we can make sense of\n"
        },
        {
          "filename": "source-extracts/1801.08229-trivial-valued-variational-proof.txt",
          "source_line_first": 5220,
          "source_line_last": 5265,
          "pdf_page_first": 104,
          "pdf_page_last": 105,
          "sha256": "0c7e483223d5fbeeb0cefe71025f639219581b1b38693badeb2f1f65e4255249",
          "literal_text": "infer\n           ˆ\n                                                          1                        1\n             ϕ(MA(ψi ) − MA(ψ)) . (C + o(1)) I(ψi , ψ) 2 . C max{Jµ (ψi ), Jµ (ψ)} 2 ,\n\nwhere the right-hand inequality\n                            ´   follows from\n                                          ´ Lemma 9.15. By Theorem 9.11, we have\nMA(ϕi ) → µ weakly; hence ϕ MA(ψi ) → ϕ µ, while Jµ (ψi ) → 0, so we are done.         \u0003\n                                                                    ´\nCorollary 9.18. Pick µ ∈ M1 . If (ϕi ) is maximizing for µ then limi ϕi (MA(ϕi ) − µ) = 0\nand limi E∨ (MA(ϕi )) = E∨ (µ).\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            105\n\nProof. By Corollary 9.16, J(ϕi ) is bounded for i large enough. By Lemma 9.17, it follows\nthat                         ˆ         ˆ\n                                                                1\n                        ci := ϕi µ − ϕi MA(ϕi ) = O(Jµ (ϕi ) 2 )\ntends to 0, and hence\n                                       ˆ                           ˆ\n             ∨\n            E (MA(ϕi )) = E(ϕi ) −         ϕi MA(ϕi ) = E(ϕi ) −       ϕi µ + ci → E∨ (µ),\n\ncompleting the proof.                                                                               \u0003\n  As another useful consequence, we get:\nProposition 9.19. Let ϕi → ϕ be a convergent net in PSH(ω), and assume that J(ϕi ) is\neventually bounded. For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).\n                                    ´\nProof. We first claim that ψ 7→ ψ µ is continuous on {J ≤ C} ⊂ PSH(ω) for ´any C > 0.\nTo see this, pick a maximizing net (ρj )j for µ in PL ∩ PSH(ω). For each          ´ j, ϕ 7→ ϕ MA(ρ ´ j)\nis continuous on PSH(ω), by Proposition 7.19 (ii). By Lemma 9.17, ψ MA(ρj ) → ψ µ\nuniformly for ψ ∈ {J ≤ C} ⊂ PSH(ω), and the claim follows since continuity is preserved\nunder uniform convergence.\n   The functional J is lsc, so J(ϕ) ≤ lim inf J(ϕi ) < ∞. Set ϕ0i := max{ϕi , ϕ}, so that\n|ϕi − ϕ| = 2(ϕ0i − ϕ) + (ϕi − ϕ). Then ϕ0i → ϕ pointwise on X div , i.e. ϕ0i → ϕ in PSH(ω).\nBy (7.34) we further have I(ϕ0i , ϕ) ≤ I(ϕi , ϕ), and J(ϕ0i ) ≈ I(ϕ0i , 0) is thus eventually\n                                                                                        ´      bounded,\n                                                                                                  ´\nby\n´ 0 the quasi-triangle\n          ´            inequality\n                            ´      for I. The  first part of  the proof    thus  yields   ϕi µ → ϕ µ,\n  ϕi µ → ϕ µ, and hence |ϕi − ϕ|µ → 0, which concludes the proof.                                    \u0003\n9.4. Dependence on the ample class. In this section, X is assumed to be irreducible.\nAs in [BBGZ13, Proposition 3.4] we then have the following useful characterization of mea-\nsures of finite energy.\n"
        },
        {
          "filename": "source-extracts/1801.08229-trivial-valued-surjectivity-proof.txt",
          "source_line_first": 6080,
          "source_line_last": 6160,
          "pdf_page_first": 121,
          "pdf_page_last": 123,
          "sha256": "399175201f28a445a407c82d967455420bdcee723a94f5215edfbd1131fc4ccd",
          "literal_text": "12.2. Strong continuity and surjectivity of the Monge–Ampère operator. We de-\nfine the strong topology on E 1 /R ≃ Esup\n                                        1 as the one induced by the strong topology on E 1 .\n\nIt is defined by the quasi-metric (ϕ, ϕ0 ) 7→ I(ϕ, ϕ0 ), by Theorem 12.4.\n   As a direct consequence of Lemma 10.7, we have:\nProposition 12.7. The Monge–Ampère operator MA : E 1 → M1 induces a bi-Lipschitz\nembedding\n                            (E 1 /R, I) ,→ (M1 , I∨ ).\n   Recall from Theorem 5.11 that the envelope property for ω ∈ Amp(X) (which holds if X\nis smooth and k has characteristic zero, cf. Theorem 5.20) is equivalent to the compactness\nof PSH(ω)/R. In a similar vein we have:\nTheorem 12.8. For any ω ∈ Amp(X), the following are equivalent:\n    (i) the envelope property holds for ω;\n   (ii) the Monge–Ampère operator MAω : E 1 (ω) → M1 is onto;\n  (iii) the Monge–Ampère operator induces a bi-Lipschitz isomorphism\n                                  (E 1 (ω)/R, Iω ) ≃ (M1 , I∨\n                                                            ω );\n\f122                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n      (iv) (E 1 (ω)/R, Iω ) is complete;\n       (v) (E 1 (ω), Iω ) is complete.\n  In particular, E 1 (ω) can only be complete if X is unibranch, cf. Theorem 5.12.\nProof. Assume (i). By Corollary 9.12, (ii) holds iff the supremum defining\n                                            \u0012          ˆ     \u0013\n                              ∨\n                             E (µ) = sup E(ϕ) − ϕ µ\n                                             ϕ∈E 1\n\nis achieved for any µ ∈ M1 . Thus choose a maximizing sequence (ϕi ) for µ in Esup     1 . By\n\nCorollary 5.21, PSHsup is weakly compact, and we may thus assume, after passing to a\nsubnet, that (ϕi ) converges weakly to ϕ ∈ PSHsup . Since Jµ (ϕi ) → 0, (9.11) shows that J(ϕi )\nis eventually bounded, and hence that ´ϕ ∈ E 1 (ω),\n                                                 ´ since J is weakly lsc. By Proposition 9.19,\nthe weak convergence ϕi → ϕ implies ϕi µ → ϕ µ, and hence\n                             ˆ              \u0012          ˆ       \u0013\n                     E(ϕ) − ϕ µ ≥ lim sup E(ϕi ) − ϕi µ = E∨ (µ),\n                                             i\nsince E is weakly usc. This proves (i)⇒(ii). Proposition 12.7 gives (ii)⇔(iii), and (iii)⇒(iv)\nfollows from the completeness of (M1 , I∨    ω ) (Theorem 10.14).\n   Assume (iv), and pick a Cauchy sequence (ϕi ) in (E 1 (ω), Iω ). Then (ϕi −sup ϕi ) is Cauchy\n     1 (ω) ≃ E 1 (ω)/R, and hence strongly convergent in E 1 (ω). Now (sup ϕ ) is Cauchy as\nin Esup                                                                            i\nwell, and hence convergent in R, so we conclude that (ϕi ) is strongly convergent, proving\n(iv)⇒(v).\n   Finally we prove (v)⇒(i). Assume that E 1 (ω) is complete. By Theorem 5.11, (i) is\nequivalent to the fact that any bounded, increasing net (ϕi ) in PSH(ω) converges weakly in\nPSH(ω). Since the increasing net (sup ϕi ) converges in R, it will be enough to show that\n(ϕi ) is Cauchy in E 1 (ω)/R, i.e. that\n                                                                 ˆ\n              Iω (ϕi , ϕj ) ≈ Jω,ϕi (ϕj ) = Eω (ϕi ) − Eω (ϕj ) + (ϕj − ϕi ) MAω (ϕi )\n\ntends to 0 as i, j → ∞, where by symmetry of Iω we may assume i ≤ j. The increasing net\n(Eω (ϕi )) converges in R. Given ε > 0, choose i0 such that 0 ≤ Eω (ϕj ) − Eω (ϕi ) ≤ ε for\nj ≥ i ≥ i0 . As ϕi ≤ ϕj , (7.22) yields\n                   ˆ\n              0 ≤ (ϕj − ϕi ) MAω (ϕi ) ≤ (n + 1) (Eω (ϕj ) − Eω (ϕi )) ≤ (n + 1)ε.\n\nThus                                               ˆ\n                           Eω (ϕi ) − Eω (ϕj ) +       (ϕj − ϕi ) MAω (ϕi ) ≤ nε,\nwhich proves, as desired, that (ϕi ) is Cauchy in E 1 (ω)/R.                                  \u0003\n   As a direct consequence of Theorem 12.8 and Theorem 5.20, we have the following result,\ncf. Theorem A.\nTheorem 12.9. Suppose that X is smooth, that char k = 0 or dim X ≤ 2, and fix ω ∈\nAmp(X). Then the Monge–Ampère equation MA(ϕ) = µ admits a solution ϕ ∈ E 1 (ω),\nunique up to translation, for every µ ∈ M1 .\nExample 12.10. Assume the envelope property for ω ∈ Amp(X). For each v ∈ X lin , there\nexists a unique ϕv ∈ E 1 (ω) such that MA(ϕv ) = δv and ϕv (v) = 0, which we call the Green’s\nfunction of v. See Proposition 12.14 for more on these functions.\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            123\n\nExample 12.11. Let X be an irreducible curve with a nodal singularity at p ∈ X(k), and\ndenote by p1 , p2 ∈ X ν (k) the preimages of p (see Figure 1). Then v := ordp1 ∈ X ν, div ≃\nX div , and δv ∈ M1 (X) is not in the image of MA : E 1 → M1 . Using Example 7.20 and\nν? MA(ν ? ϕ) = MA(ϕ) (see (7.18)), one sees indeed that a function ϕ ∈ PSH(ω) such that\nMA(ϕ) = δv must satisfy ν ? ϕ(vtriv ) = ν ? ϕ(vp2 ,triv ) = ϕ(vp,triv ) = ν ? ϕ(vp1 ,triv ), and hence\nmust be constant on the ray through v, a contradiction.\n12.3. Continuity of solutions to Monge–Ampère equations.\nTheorem 12.12. Let ϕ ∈ E 1 , and suppose that µ := MA(ϕ) is supported in a bounded\nsubset of (X lin , d∞ ), i.e. supp µ ⊂ {T ≤ C} for some C > 0. Then ϕ ∈ CPSH(ω).\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "2307.01697",
      "public_source": "https://arxiv.org/pdf/2307.01697v1",
      "saved_version": "2307.01697v1",
      "application_check": "Applied on the actual Berkovich compact space with real spans of model functions/forms: model intersection symmetry and seminegativity are supplied by BFJ intersection calculus transferred by GJKM; positivity datum has ample class; test functions are dense and admit maxima. The smooth geometrically integral X has V>0. GJKM orthogonality verifies Definition 2.15. Theorem 1.33, Proposition 2.2, Theorem 2.23, Lemma 2.25 are used only on model/test potentials and finite-energy Radon probability measures. New extension of the uniform integration estimate to E1 and actual variational attainment are proved in the argument. Theorem A(iii), completion of measures, is not used to infer surjectivity.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.pdf",
          "bytes": 788875,
          "sha256": "979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.txt",
          "bytes": 167662,
          "sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
          "matches_supplied_hash": true
        },
        {
          "kind": "abstract_html",
          "path": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.html",
          "bytes": 39123,
          "sha256": "95e379bf14e7779de66bca6e020525202fc32bdb575bd1196934cf6ee43eb11a",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/2307.01697-synthetic-standing-and-Theorem-A.txt",
          "source_line_first": 59,
          "source_line_last": 163,
          "pdf_page_first": 2,
          "pdf_page_last": 4,
          "sha256": "824f950e592fe0dbae67511cb82d0631d9126a0a04259e7a49f595c4a243444f",
          "literal_text": "The emphasis in this paper is on measures of finite energy, as opposed to potentials of finite\nenergy, that we do not seek to investigate here (see for instance [BFJ15, BoJ22a, Reb21,\nDXZ23] in the non-Archimedean context).\n\nThe general setup. Throughout this paper, we work with a compact topological space X\nequipped with the following data:\n       • a dense linear subspace D ⊂ C0 (X) of test functions, containing all constants;\n       • a vector space Z of closed (1, 1)-forms on X, endowed with a nice1 partial order,\n         and a linear map ddc : D → Z vanishing on constants;\n       • an integer n ≥ 1 (seen as the ‘dimension’ of X), and a nonzero n-linear symmetric\n         map taking a tuple (θ1 , . . . , θn ) in Z to a signed Radon measure θ1 ∧ · · · ∧ θn on X,\n         assumed to be positive for all θi ≥ 0, and such that each bilinear form\n                                                   ˆ\n                      D × D → R (φ, ψ) 7→ φ ddc ψ ∧ θ1 ∧ · · · ∧ θn−1                          (0.1)\n\n         with θi ∈ Z is symmetric, and seminegative for θi ≥ 0.\nWe then introduce the Bott–Chern cohomology space\n                                          HBC (X) := Z/ddc D,\nand define the positive cone Pos(X) ⊂ HBC (X) as the interior2 of the image of the convex\ncone\n                                 Z+ := {θ ∈ Z | θ ≥ 0}.\nThis setup is primarily inspired by the case of a compact Kähler manifold X, where D is\nthe space of smooth functions, and Z the space of closed (1, 1)-forms. It also covers the\ncase of a projective Berkovich space X over a complete non-Archimedean field k, where D\nis generated by piecewise linear (or model ) functions, and elements of Z are represented by\nnumerical classes on models over the valuation ring (or test configurations, in the trivially\nvalued case) [BFJ16a, GM16, BoJ22a]. At least under reasonable assumptions on X and k,\nwe then have HBC (X) = N1 (X), and Pos(X) coincides with the ample cone, see §1.3.2.\n\nMeasures\n    ´     of finite energy. Fix a form ω ∈ Z+ such that [ω] ∈ Pos(X), with volume\nVω = ω n > 0. The space of ω-plurisubharmonic test functions is defined as\n                                Dω := {φ ∈ D | ωφ := ω + ddc φ ≥ 0},\nand the Monge–Ampère operator takes φ ∈ Dω to the probability measure\n                                          MAω (φ) := Vω−1 ωφn .\n\n    1See §1.1 for the terminology.\n    2Here we use the finest vector space topology of H\n                                                         BC (X), see §1.1.\n\f                                  MEASURES OF FINITE ENERGY                                          3\n\nIt admits a primitive, the Monge–Ampère energy Eω : Dω → R, explicitly given by\n                                         n      ˆ\n                                     1 X −1\n                           Eω (φ) =        Vω     φ ωφj ∧ ω n−j .\n                                    n+1\n                                              j=0\n\nDenote by M the space of (Radon) probability measures on X, and define the energy of a\nmeasure µ ∈ M as the Legendre transform3\n                                             ˆ\n                      Jω (µ) := sup {Eω (φ) − φ µ} ∈ [0, +∞].\n                                     φ∈Dω\n\nThen Jω : M → [0, +∞] is convex, and lsc in the weak topology; the space of measures of\nfinite energy is defined as\n                                  M1ω := {µ ∈ M | Jω (µ) < ∞},\nequipped with the strong topology, i.e. the coarsest refinement of the weak topology in which\nJω becomes continuous.\n   As a consequence of the seminegativity of (0.1), the functional Eω is concave. This is\nequivalent to the non-negativity of the Dirichlet functional\n                                                     ˆ\n                       Jω (φ, ψ) := Eω (φ) − Eω (ψ) + (ψ − φ) MAω (φ),\n\nwhich is more explicitly given by the familiar expression\n                                           ˆ\n                                         1\n                             Jω (φ, ψ) =     (φ − ψ)ddc (ψ − φ)\n                                         2\nwhen n = 1, and a positive linear combination of integrals of the form\n                     ˆ\n                       (φ − ψ)ddc (ψ − φ) ∧ ωφj ∧ ωψn−j−1 (0 ≤ j < n)\n\nin general, see (1.31). Our first main result shows that the Dirichlet functional induces, via\nthe Monge–Ampère operator, a complete quasi-metric4 space structure on M1ω .\nTheorem A. Assume that ω has the orthogonality property. Then:\n   (i) the image of the Monge–Ampère operator MAω : Dω → M is a dense subspace of\n       M1ω ;\n  (ii) there exists a unique (continuous) quasi-metric δω on M1ω that defines the strong\n       topology of M1ω and such that\n                                δω (MAω (φ), MAω (ψ)) = Jω (φ, ψ)\n        for all φ, ψ ∈ Dω ;\n  (iii) the quasi-metric space (M1ω , δω ) is complete.\n  The energy can be expressed in terms of the quasi-metric as\n                    Jω (µ) = δω (µ, µω )    where   µω := Vω−1 ω n = MAω (0).\nWe refer to Definition 2.15 for the precise definition of the orthogonality property. Suf-\nfice it to say here that it only depends on [ω] ∈ Pos(X), and holds when X is a com-\npact Kähler manifold, or any projective Berkovich space X over a non-Archimedean field\n(as a consequence of [BE21, BGM22]). In the former case, Theorem A can be deduced\n  3This corresponds to E∨ (µ) in the notation of [BBGZ13, BoJ22a], and to ∥µ∥ in that of [BoJ22b].\n                          ω                                                  ω\n  4See §1.1 for the notion of quasi-metric used in this paper.\n\f4                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nfrom [BBGZ13, BBEGZ19]; in the latter, it was established in the trivially valued case\nin [BoJ22a], and is thus extended here to the case of an arbitrary non-Archimedean ground\nfield.\n   The strategy of proof of Theorem A follows the same lines as the trivially case treated\nin [BoJ22a]. The first key ingredient is a uniform differentiability property for the Legendre\ntransform of the convex functional µ 7→ Jω (µ), which is shown to be equivalent to the\northogonality property. This is used to prove that if (φi ) is a maximizing sequence for a\ngiven µ ∈ M1ω (i.e. a sequence in Dω computing the supremum that defines Jω (µ)), then\nMAω (φi ) converges to µ.\n   The rest of the proof relies on an extensive use of Hölder estimates for mixed Monge–\nAmpère integrals, obtained from repeated applications of the Cauchy–Schwarz inequality\n"
        },
        {
          "filename": "source-extracts/2307.01697-NA-positive-cone.txt",
          "source_line_first": 250,
          "source_line_last": 539,
          "pdf_page_first": 6,
          "pdf_page_last": 12,
          "sha256": "824dad5a009ba9716122bacfbc3fc46530bbde9164df38db050aec6736d44e70",
          "literal_text": "   In this section, we introduce the general setup considered in this paper, which is designed\nto cover in a synthetic manner the case of a compact Kähler space and that of a projective\nBerkovich space over a non-Archimedean field.\n\n1.1. Notation and terminology.\n     • For x, y ∈ R, x ≲ y or x = O(y) mean in this paper x ≤ Cn y for a constant Cn > 0\n       only depending on a given integer n fixed in the setup, and x ≈ y if x ≲ y and y ≲ x.\n     • Recall that any real vector space V admits a finest vector space topology, generated\n       by its finite dimensional subspaces, i.e. a subset A ⊂ V is open (or closed) iff, for each\n       finite dimensional subspace W ⊂ V , A ∩ W is open (resp. closed) in the canonical\n       vector space topology of W . This topology is not locally convex as soon as the\n       dimension of V is uncountable.\n     • Consider a partially ordered R-vector space (V, ≥). We shall say for brevity that the\n       partial order is nice if V+ := {x ∈ V | x ≥ 0} spans V , and is closed in the finest\n       vector space topology of V .\n     • In this paper, a quasi-metric on a set Z is a function δ : Z × Z → R≥0 that\n          – is quasi-symmetric, i.e. there exists C > 0 such that\n                              C −1 δ(x, y) ≤ δ(y, x) ≤ Cδ(x, y);\n          – satisfies the quasi-triangle inequality, i.e. there exists C > 0 such that\n                                δ(x, y) ≤ C(δ(x, z) + δ(z, y))\n            (or, equivalently, δ(x, y) ≤ C ′ max{δ(x, z), δ(z, y)} for some other constant C ′ >\n            0);\n          – separates points, i.e. δ(x, y) = 0 ⇔ x = y.\n       Note that δ ε is then also a quasi-metric for any ε > 0. A quasi-metric space (Z, δ)\n       comes with a Hausdorff topology, and even a uniform structure. In particular,\n       Cauchy sequences and completeness make sense for (Z, δ). Such uniform structures\n       have a countable basis of entourages, and are thus metrizable, by general theory. In\n       fact, there exists a metric d on X and A > 0 and constants ε > 0 only depending on\n       C such that the quasi-metric δ ε satisfies A−1 δ ε ≤ d ≤ Aδ ε (see [Fri37, AIN98, PS09],\n       thanks to Prakhar Gupta for hinting at those references).\n\n1.2. Test functions and closed (1, 1)-forms. Throughout this paper, we work with a\ncompact Hausdorff topological space X. We denote by C0 (X)∨ the space of signed Radon\nmeasures on X, and by\n                                     M ⊂ C0 (X)∨\nthe subset of probability measures, which is convex and compact in the weak topology.\nRecall from the introduction that we assume X equipped with the following data:\n     • a dense linear subspace D ⊂ C0 (X) of test functions, containing all constants;\n     • a vector space Z of closed (1, 1)-forms on X, endowed with a nice partial order, and\n       a linear map ddc : D → Z vanishing on constants;\n     • an integer n ≥ 1 (viewed as the ‘dimension’ of X), and a nonzero n-linear symmetric\n       map taking a tuple (θ1 , . . . , θn ) in Z to a signed Radon measure θ1 ∧ · · · ∧ θn on X,\n\f                                  MEASURES OF FINITE ENERGY                                          7\n\n        assumed to be positive for all θi ≥ 0, and such that each bilinear form\n                                             ˆ\n                    D × D → R (φ, ψ) 7→ φ ddc ψ ∧ θ1 ∧ · · · ∧ θn−1\n\n       with θi ∈ Z is symmetric, and seminegative when θi ≥ 0.\nSince Z+ generates Z, symmetry in the last item amounts to the integration-by-parts formula\n                 ˆ                              ˆ\n                    φ dd ψ ∧ θ1 ∧ · · · ∧ θn−1 = ψ ddc φ ∧ θ1 ∧ · · · ∧ θn−1\n                        c\n                                                                                       (1.1)\n\nfor all φ, ψ ∈ D and θi ∈ Z, while seminegativity requires\n                              ˆ\n                                 φ ddc φ ∧ θ1 ∧ · · · ∧ θn−1 ≤ 0                                (1.2)\n\nwhen θi ≥ 0 for all i.\nDefinition 1.1. For any θ ∈ Z and φ ∈ D, we set θφ := θ + ddc φ. We say that φ is\nθ-plurisubharmonic (θ-psh for short) if θφ ≥ 0, and denote by\n                                     Dθ := {φ ∈ D | θφ ≥ 0}\nthe space of θ-psh test functions.\n  For all θ, θ′ ∈ Z and t ∈ R>0 we have\n                                 Dθ + Dθ′ ⊂ Dθ+θ′ ,     Dtθ = tDθ .\nIn particular, Dθ is a convex subset of D, and\n                                       θ ≤ θ′ =⇒ Dθ ⊂ Dθ′ .                                     (1.3)\nSince ddc vanishes on constants, we have:\nExample 1.2. Constant functions on X are θ-psh iff θ ≥ 0.\n  The main two instances of the above setup considered in this paper are as follows.\n1.2.1. The Kähler case. The above formalism is primarily inspired by the case of a compact\nKähler complex analytic space X. Here n = dim X, D = C ∞ (X) is the space of smooth\nfunctions on X, and Z is the space of closed (1, 1)-forms on X that are locally ddc -exact,\n                                     1,1                              ∞ → Ω1,1 (see for in-\ni.e. global sections of the image ZX     of the sheaf morphism ddc : CX        X\nstance [Dem85] for the definition of smooth forms in this context). When X is nonsingular,\ni.e. a compact Kähler manifold, Z coincides with the space of closed (1, 1)-forms on X, but\nthe inclusion might be strict in the singular case.\n   For all φ, ψ ∈ D and θi ∈ Z, the Stokes formula implies\n                     ˆ                 ˆ                 ˆ\n                        φ ddc ψ ∧ Θ = ψ ddc φ ∧ Θ = − dφ ∧ dc ψ ∧ Θ\n\nwith Θ := θ1 ∧ · · · ∧ θn−1 , which yields (1.1) and (1.2), since the (1, 1)-form dφ ∧ dc φ is\nsemipositive.\nRemark 1.3. More generally, fix a Kähler form ωX on X and assume n ≤ dim X. Recall\n                                                                                      dim X−i\nthat a (1, 1)-form α on X is n-semipositive (with respect to ωX ) if αi ∧ ωX                  ≥ 0 for\ni = 0, . . . , n (see [Blo05, LN15]). For any n-tuple of n-semipositive (1, 1)-forms α1 , . . . , αn ,\n                            dim X−n\nwe have α1 ∧· · ·∧αn ∧ωX              ≥ 0. One thus obtains a setup satisfying the above conditions\nby defining Z+ as the convex cone of closed (1, 1)-forms that are n-semipositive, and by\n                                                                              dim X−n\nassociating to a tuple (θ1 , . . . , θn ) in Z the measure θ1 ∧ · · · ∧ θn ∧ ωX       .\n\f8                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n1.2.2. The non-Archimedean case. Assume now that X is a projective Berkovich space over\na non-Archimedean field k, i.e. the Berkovich analytification of a projective k-scheme, of\ndimension n = dim X. We then take D to be the R-vector space generated by PL functions,\nsee [BE21, §5.4].\n   When k is nontrivially valued, D can be described in terms of vertical divisors on (pro-\njective, flat) models X of X over the spectrum S of the valuation ring. More precisely, we\nhave\n                                     D ≃ lim VCar(X )R ,\n                                         −→\n                                           X\n\nwhere VCar(X )R denotes the R-vector space generated by Cartier divisors on X that are\nvertical, i.e. supported on the special fiber. The same description applies in the trivially\nvalued case as well, if a model is now understood as a test configuration X → S := A1\n(see [BHJ17, §6.1], [BoJ22a, §2.2]).\n   In the nontrivially valued case, the space Z is defined by setting\n\n                                     Z := lim N1 (X /S),                                  (1.4)\n                                          −→\n                                            X\n\nwhere N1 (X /S) denotes the (finite dimensional) vector space of relative numerical classes\n(see [BFJ16a, §4.2], [GM16, §4], the definition being inspired by [BGS95]). A form θ ∈\nZ is thus represented by a numerical class θX ∈ N1 (X /S) for some model X , called a\ndetermination of θ, two such classes being identified if they coincide after pulling back\nto some higher model, and we write θ ≥ 0 if θX is (relatively) nef for some (hence any)\ndetermination X of θ.\n   The measure θ1 ∧ · · · ∧ θn associated to a tuple of forms θi ∈ Z is a finite linear combi-\nnation of Dirac masses at divisorial points, whose coefficients can be described in terms of\nintersection numbers computed on models.\n   The linear map ddc : D → Z takes a vertical divisor D ∈ VCar(X )R to its numerical class\nin N1 (X /S), and the seminegativity condition (1.2) follows the local Hodge index theorem\nof Yuan–Zhang [YZ17, Theorem 2.1].\n   Again, the same discussion applies to the trivially valued case as well, using test configu-\nrations instead of models. In that case, pulling back numerical classes on X to the product\ntest configuration further yields an injection\n\n                                        N1 (X) ,→ Z.                                      (1.5)\n\nNote that only forms lying in N1 (X) were considered in [BoJ22a].\n\nRemark 1.4. In the non-Archimedean case, one could also work with smooth functions and\n(1, 1)-forms in the sense of [CD12] (see also [GK15, GK17, GJR21]), but this will not be\nconsidered in the present paper.\n\nRemark 1.5. More generally, test configurations for an arbitrary compact Kähler manifold\n(as in [SD18, DeR17]) can also be approached using the above formalism. This is the topic\nof forthcoming work of Pietro Piccione.\n\nRemark 1.6. Another setting where the above formalism applies is that of tropical toric\npluripotential theory as in [BGJK21].\n\f                                  MEASURES OF FINITE ENERGY                                        9\n\n1.3. Bott–Chern cohomology and positive classes.\nDefinition 1.7. We define the Bott–Chern cohomology space as\n                                      HBC (X) := Z/ddc D,\nand denote by θ 7→ [θ] the quotient map Z → HBC (X). The positive cone\n                                       Pos(X) ⊂ HBC (X)\nis defined as the interior of the image of Z+ .\n   Here the interior is taken with respect to the finest vector space topology (see §1.1).\nConcretely, a class α ∈ HBC (X) belongs to Pos(X) if, for any β ∈ HBC (X), α + tβ lies in\nthe image of Z+ for all t ∈ R small enough.\n   Since it is assumed that Z+ spans Z, its image in HBC (X) is a convex cone that generates\nHBC (X). As a consequence, the positive cone Pos(X) is non-empty as soon as HBC (X) is\nfinite dimensional.\nRemark 1.8. The image Z+ in HBC (X) is not closed in general. This happens already in\nthe complex projective case, see [DPS94, Example 1.7].\n   Since ddc vanishes on R ⊂ D, (1.1) yields\n                 ˆ                               ˆ\n                    dd φ ∧ θ1 ∧ · · · ∧ θn−1 = φ ddc 1 ∧ θ1 ∧ · · · ∧ θn−1 = 0\n                      c\n\n                                                            ´\nfor all φ ∈ D and θi ∈ Z. As a result, (θ1 , . . . , θn ) 7→ θ1 ∧ · · · ∧ θn descends to a symmetric\nn-linear pairing\n                        HBC (X)n → R (α1 , . . . , αn ) 7→ α1 · . . . · αn ,\nwhich we call the intersection pairing.\nLemma 1.9. For all classes α1 , . . . , αn ∈ Pos(X) we have α1 · . . . · αn > 0.\n Proof. By assumption, the measure θ1 ∧ · · · ∧ θn is nonzero for some tuple θ1 , . . . , θn ∈ Z.\n´Since Z+ generates Z, we can further assume θi ∈ Z+ for all i. Then [θ1 ] · . . . · [θn ] =\n   θ1 ∧ · · · ∧ θn > 0. Now we can find 0 < ε ≪ 1 such that αi − ε[θi ] ∈ Pos(X) for all i, and\nhence α1 · . . . · αn ≥ εn [θ1 ] · . . . · [θn ] > 0.                                          □\nDefinition 1.10. For each ω ∈ Z+ and θ ∈ Z we set\n                           ∥θ∥ω := inf{C ≥ 0 | ±θ ≤ Cω} ∈ [0, +∞],\nand we say that θ is ω-bounded if ∥θ∥ω < ∞.\n  The set\n                                Zω := {θ ∈ Z | ∥θ∥ω < ∞}\nof ω-bounded forms is a linear subspace of Z, on which ∥ · ∥ω defines a norm.\nRemark 1.11. In general, Zω is a strict subspace of Z. More precisely, Zω = Z iff ω\nlies in the interior of Z+ in the finest vector space topology of Z, which is empty in the\nnon-Archimedean case (see §1.3.2 below).\n  We can now characterize positive classes as follows:\nProposition 1.12. A class α ∈ HBC (X) lies in Pos(X) iff, for each finite dimensional\nsubspace V ⊂ Z, α admits a representative ω ∈ Z+ such that V ⊂ Zω .\n\f10                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. Assume α ∈ Pos(X), and pick a basis (θi )1≤i≤r of a finite dimensional vector space\nV ⊂ Z. Since Z+ spans Z, for each i we can write θi = θi+ − θi− with θi± ≥ 0. Since\nα ∈ Pos(X) we have α − ε[θi± ] ∈ Pos(X) for all 0 < ε ≪ 1, and we can thus find ε > 0 and\nωi± ∈ α such that ωi± − εθi± ≥ 0 for all i. Now set\n                                             r\n                                             X\n                                        1\n                                   ω := 2r         (ωi+ + ωi− ) ∈ Z+ .\n                                             i=1\n                                             ε ±        ε\nThen [ω] = α, and for each i we have ω ≥ 2r   θi ≥ ± 2r   θi , and hence θi ∈ Zω , i.e. V ⊂ Zω .\nThis proves the ‘only if’ part, and the converse is clear.                                   □\nCorollary 1.13. Pick θ ∈ Z such that [θ] ∈ Pos(X). Then any f ∈ D can be written as\nf = f + − f − with f ± ∈ Dtθ = tDθ for some t > 0. In particular, Dθ spans D.\nProof. By Proposition 1.12, we can find ψ ∈ Dθ and C > 0 such that −ddc f ≤ t(θ + ddc ψ).\nThus f + := φ + tψ lies in Dtθ , and the result follows with f − := tψ ∈ DCθ .         □\n     Following [Tho63], we define the Thompson distance between ω, ω ′ ∈ Z+ as\n                      dT (ω, ω ′ ) := inf{δ ≥ 0 | e−δ ω ≤ ω ′ ≤ eδ ω} ∈ [0, +∞].              (1.6)\nWe say that ω and ω ′ are commensurable if d                ′                                 ′\n                                                     T (ω, ω ) < ∞. Note that this holds iff ω ∈ Zω\nand ω ∈ Zω′ . Commensurability is an equivalence relation on Z+ . The linear subspace Zω\nonly depends on the commensurability class of ω ∈ Z+ , and so does the equivalence class of\nthe norm ∥ · ∥ω .\n  The next result is readily checked, and left to the reader.\nLemma 1.14. The commensurability class of any ω ∈ Z+ forms an open convex cone in the\nnormed vector space (Zω , ∥·∥ω ), whose topology is defined by the restriction of the Thompson\nmetric.\n     We conclude this section with the following useful fact, that will be put to use in §3.\nProposition 1.15. Each finite subset of Pos(X) can be represented by commensurable forms\nin Z+ .\nProof. We first claim that any two α, α′ ∈ Pos(X) admit commensurable representatives.\nIndeed, setting α ∼ α′ when α and α′ admit commensurable representatives defines an\nequivalence relation on Pos(X), and it is thus enough that each equivalence class intersects\nthe line segment [α, α′ ] in an open set. Pick β ∈ [α, α′ ], and choose representatives θ, θ′ ∈\nZ+ of α, α′ . By Proposition 1.12, we can find a representative ω ∈ Z+ of β such that\nθ, θ′ ∈ Zω . By Lemma 1.14, the commensurability class of ω intersects [θ, ω] and [ω, θ′ ]\nalong neighborhood of ω, and it follows, as desired, that the equivalence class of β intersects\n[α, α′ ] along a neighborhood of β.\n   Now pick α1 , . . . , αr ∈ Pos(X). By the first part of the proof, for each i = 2, . . . , r\nwe can find two P   commensurable forms ω1,i , ωi ∈ Z+ such that [ω1,i ] = α1 and [ωi ] = αi .\nThen ω1 := r−1 ri=2 ω1,i ∈ Z+ represents α1 , and is commensurable to ωi for all i since\n                1\n\ncommensurability classes are convex cones.                                                    □\n1.3.1. The Kähler case. As in §1.2.1, assume that X is a compact Kähler space. When X is\nnonsingular, HBC (X) coincides with the (1, 1)-part of the Hodge decomposition of H2 (X, R).\nIn general, denote by PHX the sheaf of germs of pluriharmonic functions, i.e. the kernel\nof the sheaf morphism ddc : CX ∞ → Ω1,1 . The existence of partitions of unity implies that\n                                       X\n\f                                     MEASURES OF FINITE ENERGY                                                  11\n\nthe sheaf CX∞ is soft, and the cohomology long exact sequence associated to the short exact\n\nsequence of sheaves\n                                              ∞      1,1\n                                0 → PHX → CX    → ZX     →0\nthus yields\n                                  HBC (X) ≃ H1 (X, PHX ).\nWe do not know whether this is always finite dimensional, but this holds at least when X is\nnormal, as a consequence of the fact that PHX then coincides with the sheaf ℜOX of real\nparts of holomorphic functions, see [BG13, §4.6.1].\n   The positive cone Pos(X) is compatible with the usual definition, i.e. α ∈ HBC (X) lies\nin Pos(X) iff α can be represented by a Kähler form. Indeed, given any Kähler form ω,\na class α ∈ Pos(X) can be represented by a form θ ∈ Z such that θ − εω ∈ Z+ for some\n0 < ε <≪ 1, so that θ is a Kähler form. In particular, Kähler forms constitute a single\ncommensurability class that maps onto Pos(X).\n1.3.2. The non-Archimedean case. Assume, as §1.2.2, that X is a projective Berkovich space\nover a non-Archimedean field. By definition, any θ ∈ Z is represented by a numerical class\non some model X of X, whose restriction to the generic fiber defines a numerical class\n{θ} ∈ N1 (X) on (the projective variety underlying) X. This induces a surjective map\n                                            HBC (X) ↠ N1 (X),                                                (1.7)\nwhich is an isomorphism when X is smooth and k is discretely valued of residue character-\nistic 0 [BFJ16a, Theorem 4.3], or when X is normal and k is algebraically closed [Jell16,\nTheorem 4.2.7]). It is also an isomorphism when k is trivially valued, with inverse provided\nby pulling back classes in N1 (X) to the trivial test configuration Xtriv = X × A1 .\n    We claim that Pos(X) coincides with the preimage of the ample cone of X under (1.7),\nand that Z+ has empty interior in the finest vector space topology of Z (so that Kähler\nforms do not admit an analogue in the non-Archimedean case).\n    To see this, we say as in [BFJ16a, §5.1] that a form ω ∈ Z+ is X -positive for a given\nmodel/test configuration X if it is represented by a (relatively) ample class in N1 (X /S).\nNote that all X -positive forms are commensurable. As observed in [BFJ16a, Proposition 5.2]\n(see also [GM16, Proposition 4.14], [BoJ22a, Lemma 3.11]), any α ∈ HBC (X) whose image in\nN1 (X) under (1.7) is ample can be represented by an X -positive form ω for any sufficiently\nhigh model X . Now Zω contains all forms determined on X , but does not contain any\nX ′ -positive form for a model X ′ strictly dominating X . The claim easily follows.\n1.4. The energy pairing. Mimicking the properties of induced metrics on Deligne pairings\n(see for instance [BE21, Theorem 8.16]), and generalizing [SD18, §2.2] (for a compact Kähler\nmanifold) and [BoJ22a, §3.2] (for a projective Berkovich space over a trivially valued field),\nwe introduce:\nProposition-Definition 1.16. The energy pairing\n              (Z × D)n+1 → R          ((θ0 , φ0 ), . . . , (θn , φn )) 7→ (θ0 , φ0 ) · . . . · (θn , φn ),\nis defined as the unique (n + 1)-linear symmetric map such that\n                                                       ˆ\n           (0, φ0 ) · (θ1 , φ1 ) · . . . · (θn , φn ) = φ0 (θ1 + ddc φ1 ) ∧ · · · ∧ (θn + ddc φn )           (1.8)\n\nand\n                                         (θ0 , 0) · . . . · (θn , 0) = 0.                                    (1.9)\n\f12                                  SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n"
        },
        {
          "filename": "source-extracts/2307.01697-Holder-and-defect-proof.txt",
          "source_line_first": 791,
          "source_line_last": 914,
          "pdf_page_first": 17,
          "pdf_page_last": 19,
          "sha256": "d2487660d08f60346e5e58c323160d0765200a39a018ddc6ba83e04283494fc3",
          "literal_text": "                                                  (φ − ψ) ddc (ψ − φ) ∧ ωφj ∧ ωψn−1−j .\n                                  X\n               Jω (φ, ψ) = Vω−1                                                           (1.31)\n                                        n+1\n                                  j=0\nWe simply write                                        ˆ\n                              Jω (φ) := Jω (0, φ) =        φ µω − Eω (φ).                 (1.32)\n\nExample 1.31. When n = 1, we have\n                                                      ˆ\n                        Jω (φ, ψ) = Jω (ψ, φ) = 12         (φ − ψ)ddc (ψ − φ),\n\nwhich recovers the usual expression for the Dirichlet functional on a Riemann surface.\n  For each R > 0 we set\n                                  Dω,R := {φ ∈ Dω | Jω (φ) ≤ R}.                          (1.33)\nLemma 1.32. For each R > 0, Dω,R is a convex subset of D that generates it.\nProof. By convexity of Jω = Jω (0, ·), Dω,R is convex. Since Dω spans D (see Corollary 1.13),\nto see that Dω,R spans it suffices to show that any φ ∈ Dω satisfies Jω (tφ) ≤ R for 0 < t ≪ 1,\nwhich holds since Jω (tφ) is a polynomial function of t with Jω (0) = 0.                     □\n   We may now collect the fundamental properties of the Dirichlet functional in the next\nresult.\nTheorem 1.33. For all φ, φ′ , ψ, ψ ′ , τ ∈ Dω and t ∈ [0, 1], the following holds:\n    • quasi-symmetry:\n                                    Jω (φ, ψ) ≈ Jω (ψ, φ);                                (1.34)\n    • quasi-triangle inequality:\n                                  Jω (φ, ψ) ≲ Jω (φ, τ ) + Jω (τ, ψ);                     (1.35)\n      • quadratic estimate:\n                                Jω (φ, (1 − t)φ + tψ) ≲ t2 Jω (φ, ψ);                     (1.36)\n      • uniform concavity:\n              Eω ((1 − t)φ + tψ) − [(1 − t) Eω (φ) + t Eω (ψ)] ≳ t(1 − t)Jω (φ, ψ).\nFor all φ, φ′ , ψ, ψ ′ ∈ Dω,R , we further have the following Hölder estimates:\n               ˆ\n                 (φ − φ′ ) MAω (ψ) − MAω (ψ ′ ) ≲ Jω (φ, φ′ )α Jω (ψ, ψ ′ )1/2 R1/2−α ;\n                                                  \u0001\n                                                                                          (1.37)\n\nand\n                   Jω (φ, ψ) − Jω (φ′ , ψ ′ ) ≲ max{Jω (φ, φ′ ), Jω (ψ, ψ ′ )}α R1−α ,    (1.38)\nwhere α := 2−n .\nProof. In view of (1.13), this is a direct consequence of Theorem A.3 applied to\n     • the vector space V := Z × D with projection π : V → Z onto the first factor;\n\f18                             SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n        • the convex cone P := {(θ, φ) ∈ V | φ ∈ Dθ };\n                                                                             n+1\n        • the homogeneous polynomial F : V → R defined by F (θ, φ) := − (θ,φ)\n                                                                        (n+1)Vω .\n                                                                                                        □\n\n     As a simple consequence of (1.29), we finally note:\nLemma 1.34. For each τ ∈ Dω and φ, ψ ∈ Dωτ we have φ + τ, ψ + τ ∈ Dω and\n                                     Jωτ (φ, ψ) = Jω (φ + τ, ψ + τ ).                              (1.39)\nRemark 1.35. The above formalism recovers that of [BBGZ13, BBEGZ19, BFJ15, BoJ22a]\nin the Kähler and non-Archimedean settings. However, in contrast to those works, we do\nnot explicitly introduce here the functional Iω (φ, ψ), which corresponds to the right-hand side\nof (1.30).\n\n                                   2. Measures of finite energy\n   In what follows, we pick ω ∈ Z+ with [ω] ∈ Pos(X). We define the space M1ω of measures\nof finite energy with respect to ω, and show, assuming a certain orthogonality property, that\nit is complete with respect to a quasi-metric δω induced by the Dirichlet functional.\n\n2.1. The energy of a measure.\nDefinition 2.1. We define the energy of µ ∈ M relative to ψ ∈ Dω as\n                                                 ˆ\n              Jω (µ, ψ) := sup {Eω (φ) − Eω (ψ) + (ψ − φ)µ} ∈ [0, +∞].                              (2.1)\n                                  φ∈Dω\n\n     The choice of notation is justified by (2.5) below. When ψ = 0, we simply write\n                                                              ˆ\n                          Jω (µ) := Jω (µ, 0) = sup {Eω (φ) − φ µ},                                 (2.2)\n                                                    φ∈Dω\n\nand call it the energy5 of µ (with respect to ω). Note that\n                                          ˆ\n                            Jω (µ) = sup { φ(µω − µ) − Jω (φ)},                                     (2.3)\n                                          φ∈Dω\n\nby (1.32).\nProposition 2.2. For each ψ ∈ Dω , the functional Jω (·, ψ) : M → [0, +∞] is convex and\nweakly lsc, and satisfies, for all µ ∈ M and φ ∈ Dω ,\n                                                  ˆ\n                              Jω (µ, ψ) = Jω (µ) + ψ µ − Eω (ψ);                   (2.4)\n\n                                      Jω (MAω (φ), ψ) = Jω (φ, ψ);                                  (2.5)\n                                         Jω (MAω (φ)) ≈ Jω (φ);                                     (2.6)\n                                    Jω (φ, ψ) ≲ Jω (µ, φ) + Jω (µ, ψ).                              (2.7)\n\n     5This corresponds to E∨ (µ) in the notation of [BBGZ13, BoJ22a], and to ∥µ∥\n                           ω                                                   ω in that of [BoJ22b].\n\f                                  MEASURES OF FINITE ENERGY                                  19\n\nProof. Convexity and lower semicontinuity are clear from (2.1), which also directly yields (2.4).\nBy (1.28), any φ ∈ Dω further computes the supremum defining Jω (MAω (φ), ψ), which is\nthus equal to                         ˆ\n                    Eω (φ) − Eω (ψ) + (ψ − φ) MAω (φ) = Jω (φ, ψ).\nThis proves (2.5), which implies\n                 Jω (MAω (φ)) = Jω (MAω (φ), 0) = Jω (φ, 0) ≈ Jω (0, φ) = Jω (φ),\nsee (1.34). Finally, pick µ ∈ M, and set τ = 21 (φ + ψ) ∈ Dω . By (2.1), we have\n                                  ˆ                                          ˆ\n    Jω (µ, φ) ≥ Eω (τ ) − Eω (φ) + (φ − τ ) µ, Jω (µ, ψ) ≥ Eω (τ ) − Eω (ψ) + (ψ − τ ) µ,\n\nand hence\n                       Jω (µ, φ) + Jω (µ, ψ) ≥ 2 Eω (τ ) − (Eω (φ) + Eω (ψ)).\nOn the other hand,\n                         2 Eω (τ ) − (Eω (φ) + Eω (ψ)) ≳ Jω (φ, ψ)\nby uniform concavity of Eω (see Theorem 1.33), and (2.7) follows.                            □\n  Generalizing Lemma 1.34, we note:\nLemma 2.3. For all τ ∈ Dω , ψ ∈ Dωτ and µ ∈ M we have\n                                    Jωτ (µ, ψ) = Jω (µ, ψ + τ ).                          (2.8)\nIn particular,                                       ˆ\n                                Jωτ (µ) = Jω (µ) +       τ µ − Eω (τ ).                   (2.9)\n\nProof. By Lemma 1.29, we have φ ∈ Dωτ ⇔ φ + τ ∈ Dω , and\n                      ˆ                                      ˆ\n   Eωτ (φ) − Eωτ (ψ) + (φ − ψ)µ = Eω (φ + τ ) − Eω (ψ + τ ) + ((φ + τ ) − (ψ + τ ))µ.\n\nTaking the sup over φ yields (2.8), and (2.9) follows, by (2.4).                             □\nRemark 2.4. If we drop the assumption that ω ≥ 0, but still require [ω] ∈ Pos(X), then\nEω (φ) and Jω (µ) can still defined by (1.24) and (2.2), respectively. Then Lemma 1.29,\nand hence (2.9), remain valid for any τ ∈ D. This will only get used in the context of\nTheorem 4.8 below.\n2.2. Measures of finite energy.\nDefinition 2.5. The space of measures of finite energy (with respect to ω) is defined as\n"
        },
        {
          "filename": "source-extracts/2307.01697-maxima-orthogonality.txt",
          "source_line_first": 989,
          "source_line_last": 1125,
          "pdf_page_first": 21,
          "pdf_page_last": 23,
          "sha256": "4a3bed03c92670749f6f0dadbae58c1f5edbf86a40e58a0e0588268b5444df2a",
          "literal_text": "Since E                                                                    e ω (µ) < ∞ implies\n      e ω is increasing and equivariant, it is straightforward to see that E\n            ´\nµ ≥ 0 and µ = 1, i.e. µ ∈ M (compare [BoJ22a, Proposition 9.8]). By Legendre duality,\n                                 e ∨ (µ) = Jω (µ) for µ ∈ M. Since E\nthe result is thus equivalent to E                                  e ω restricts to Eω on Dω ,\n                                   ω\n                    ∨                                      0\n                  e (µ) ≥ Jω (µ). Conversely, pick f ∈ C (X) and φ ∈ Dω with φ ≤ f . Then\nwe trivially have E ω\n                                            ˆ                  ˆ\n                          Jω (µ) ≥ Eω (φ) − φ µ ≥ Eω (φ) − f µ,\n\nwhere the first and second inequality respectively follow from (2.2) and φ ≤ f . Taking the\n                                                             ´\nsupremum over φ and then over f yields Jω (µ) ≥ E                              e ∨ (µ).\n                                                   e ω (f ) − f µ and Jω (µ) ≥ E         □\n                                                                                 ω\n\n2.4. Orthogonality and differentiability.\nDefinition 2.11. We say that Dω admits maxima if, for all φ, ψ ∈ Dω and f ∈ D such\nthat max{φ, ψ} < f pointwise on X, there exists τ ∈ Dω with max{φ, ψ} ≤ τ < f .\n  This equivalently means that, for any f ∈ D, the poset\n                                 Dω,<f := {φ ∈ Dω | φ < f }\nis inductive. We can then consider limits of nets indexed by Dω,<f . For instance, note that\n                                   E\n                                   e ω (f ) =     lim     Eω (φ).                       (2.14)\n                                                φ∈Dω,<f\n\nExample 2.12. If X is a compact Kähler space, then Dω admits maxima: take τ :=\nmax(φ,\ng      ψ) for an appropriate regularized max function max.\n                                                      g\nExample 2.13. If X is a projective Berkovich space, then Dω also admits maxima, since\nQ-PL functions in Dω are dense in Dω , and stable under max.\nRemark 2.14. While we will not pursue this direction here, one can introduce as in [BFJ16a,\nBE21, BoJ22a] the space PSH(ω) of ω-psh functions φ : X → R∪{−∞}, defined as usc       ´ func-\ntions that can be obtained as pointwise limits of decreasing nets in Dω , and such that φ µω >\n−∞. Then Dω admits maxima iff PSH(ω) (or, equivalently, the subspace CPSH(ω) :=\nPSH(ω) ∩ C0 (X) of continuous ω-phs functions) is stable under max.\nDefinition 2.15. We say that ω has the orthogonality property if Dω admits maxima and\n                                   ˆ\n                              lim     (f − φ) MAω (φ) = 0                       (2.15)\n                               φ∈Dω,<f\n\nfor all f ∈ D.\n\n´ Explicitly, this means for that for any ε > 0 there exists φ0 ∈ Dω such that φ0 < f and\n (f − φ) MAω (φ) ≤ ε for all φ ∈ Dω with φ0 ≤ φ < f .\n\f22                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nRemark 2.16. The orthogonality property for ω only depends on [ω] ∈ Pos(X). Indeed, for\nany τ ∈ Dω and f ∈ D we have\n                                 φ ∈ Dωτ ,<f ⇐⇒ φ + τ ∈ Dω,<f +τ                   (2.16)\nThis implies that Dω has finite maxima iff Dωτ does, and similarly for the orthogonality\nproperty, using\n                                ˆ                    ˆ\nMAωτ (φ) = MAω (φ + τ ) and       (f − φ) MAωτ (φ) = ((f + τ ) − (φ + τ )) MAω (φ + τ ).\n\nExample 2.17. Assume X is a compact Kähler space. Conjecturally, the orthogonality\nproperty always holds. This is known when X is nonsingular, or X is projective and [ω] ∈\nAmp(X), see Appendix B for a more detailed discussion.\nRemark 2.18. More generally, the orthogonality property also holds in the setting of Re-\nmark 1.3 (assuming X is a compact Kähler manifold). This follows indeed from [LN15,\nTheorem 3.2].\n     Recall from Corollary 1.13 that any test function f ∈ D can be written as\n                                     f = f + − f −,      f ± ∈ DCω                 (2.17)\nfor some C = C(f ) > 0. In line with [BFJ15, §7], we show:\nProposition 2.19. Assume Dω admits maxima. The following properties are then equiva-\nlent:\n     (i) ω has the orthogonality property;\n    (ii) for any f ∈ D written as (2.17) for a given C > 0, we have\n                                             ˆ\n                       Eω (φ + f ) − Eω (φ) − f MAω (φ) ≲ C sup |f |\n                       e                                                      (2.18)\n\n           for all φ ∈ Dω ;\n     (iii) in the setting of (ii), we have\n                                                    ˆ\n                       e ω (φ + tf ) − Eω (φ) − t\n                       E                                f MAω (φ) ≲ Ct2 sup |f |   (2.19)\n\n          for all φ ∈ Dω and t ∈ R.\nProof. Assume (i). Write f ∈ D as in (2.17), and pick φ ∈ Dω . For any ψ ∈ Dω,<φ+εf ,\n(1.28) yields\n        ˆ                                     ˆ                  ˆ\n           (ψ − φ) MAω (ψ) ≤ Eω (ψ) − Eω (φ) ≤ (ψ − φ) MAω (φ) ≤ f MAω (φ).\n                       ´\nBy (1.19), we also have f (MAω (φ) − MAω (ψ)) ≤ 2nC sup |φ − ψ|, and we infer\n                     ˆ             ˆ\n   Eω (ψ) − Eω (φ) − f MAω (φ) ≤ ((φ + f ) − ψ) MAω (ψ) + 2nC sup |φ − ψ|.         (2.20)\n\nNow limψ∈Dω,<φ+f Eω (ψ) = E\n                          e ω (φ + f ) (see (2.14)), while orthogonality yields\n                                   ˆ\n                           lim        ((φ + f ) − ψ) MAω (ψ) = 0.\n                             ψ∈Dω,<φ+f\n\f                                   MEASURES OF FINITE ENERGY                                      23\n\nFurther, any ψ ∈ Dω,<φ+f large enough is greater than φ − sup |f | ∈ Dω,<φ+f , and hence\nsatisfies sup |φ − ψ| ≤ sup |f |. As a result, (2.20) implies\n                                               ˆ\n                      Eω (φ + f ) − Eω (φ) − f MAω (φ) ≤ 2nC sup |f |,\n                      e\n\nwhich shows (i)⇒ (ii). Next, (ii)⇒(iii), since f = f + − f − with f ∈ DCω implies tf =\nsgn(t)(|t|f + − |t|f − ) with |t|f ± ∈ DC|t|ω .\n  Finally, assume (iii), and pick f ∈ D. We need to show that\n                                               ˆ\n                                L := lim sup (f − φ) MAω (φ) ≥ 0\n                                    φ∈Dω,<f\n\nvanishes. Write f as in (2.17) for some C > 0. Pick also φ ∈ Dω,<f , and set g := f − φ ∈ D.\nFor any t ∈ [0, 1] we have φ + tg = (1 − t)φ + tf ≤ f , and hence E     e ω (φ + tg) ≤ E\n                                                                                       e ω (f ). On\n                                   +      −               +      −\nthe other hand, since f − φ = f − (f + φ) with f , < f + φ ∈ D(C+1)ω , (iii) yields a\nconstant A > 0 only depending on φ such that\n     ˆ\n0 ≤ t (f − φ) MAω (φ) ≤ E   e ω (φ + tg) − Eω (φ) + t2 A sup |g| ≤ E\n                                                                   e ω (f ) − Eω (φ) + t2 A sup |g|.\n\nSince any φ ∈ Dω,<f large enough is greater then f + − sup f − , it satisfies\n                               0 ≤ g = f − φ ≤ sup f − − f − ≤ B\nwith B only depending on f . We infer 0 ≤ tL ≤ t2 AB. Dividing by t > 0 and letting t → 0+\nyields, as desired, L = 0. This proves (iii)⇒(i).                                        □\nExample 2.20. Assume X is a projective Berkovich space over a non-Archimedean field.\nThen [BE21, Theorem A] combined with the uniform differentiability estimate of [BGM22,\nLemma 3.2] shows that (2.18) is satisfied (compare [BoJ22a, Lemma 8.7]). By Proposi-\ntion 2.19, it follows that the orthogonality property always holds in this setting.\n2.5. Maximizing sequences.\n                                                                                  1\nDefinition 2.21. We say that a sequence (ψ     ´ i ) in Dω is maximizing for µ ∈ Mω if it\ncomputes the energy of µ (2.2), i.e. Eω (ψi ) − ψi µ → Jω (µ).\n  Equivalently, (ψi ) is maximizing for µ iff Jω (µ, ψi ) → 0, see (2.4).\nExample 2.22. For any φ ∈ Dω the constant sequence ψi = φ is maximizing for µ =\nMAω (φ) (see (2.5)).\n"
        },
        {
          "filename": "source-extracts/2307.01697-density-and-uniform-integral-proof.txt",
          "source_line_first": 1120,
          "source_line_last": 1206,
          "pdf_page_first": 23,
          "pdf_page_last": 25,
          "sha256": "eea74aa468c0107b4073aba46fb851314c53d4efd713b46b2ef012d6afe3409e",
          "literal_text": "                                                                                  1\nDefinition 2.21. We say that a sequence (ψ     ´ i ) in Dω is maximizing for µ ∈ Mω if it\ncomputes the energy of µ (2.2), i.e. Eω (ψi ) − ψi µ → Jω (µ).\n  Equivalently, (ψi ) is maximizing for µ iff Jω (µ, ψi ) → 0, see (2.4).\nExample 2.22. For any φ ∈ Dω the constant sequence ψi = φ is maximizing for µ =\nMAω (φ) (see (2.5)).\n  As a key consequence of Proposition 2.19, we show:\nTheorem 2.23. Assume ω has the orthogonality property. Pick µ ∈ M1ω and a maximizing\nsequence ψi ∈ Dω . Then the measures µi := MAω (ψi ) converge strongly to µ in M1ω , i.e.\nµi → µ weakly and Jω (µi ) → Jω (µ). In particular, the image of the Monge–Ampère operator\n                                        MAω : Dω → M1ω\nis dense in the strong topology.\nProof. Pick f ∈ D, and choose C > 0 such that f = f + − f − with f ± ∈ DCω . Since we\nassume orthogonality, Proposition 2.19 yields A > 0 such that\n                                                  ˆ\n                      Eω (ψi + tf ) − Eω (ψi ) − t f µi ≤ At2 sup |f |\n                      e\n\f24                            SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nfor all i and t > 0. By Proposition 2.10 and (2.4), we have, on the other hand,\n                                     ˆ                                        ˆ\n             Eω (ψi + tf ) ≤ Jω (µ) + (ψi + tf )µ = Jω (µ, ψi ) + Eω (ψi ) + t f µ.\n             e\n\nCombining these estimates, we get\n                           ˆ        ˆ\n                          t f µi ≤ t f µ + Jω (µ, ψi ) + At2 .\n\nSince Jω (µ, ψi ) → 0, we infer\n                                                ˆ              ˆ\n                                    t lim sup       f µi ≤ t       f µ + At2 .\n                                         i\n                                                      ´         ´\nDividing´ by t and´ letting t →  0+ yields lim  sup i   f µ i ≤   f µ. Replacing f with −f , we\n                                                0\nget limi f µi = f µ. By density of D in´ C (X), this shows µi → µ weakly.       ´\n   For each i we have Jω (µi ) = Eω (ψi ) − ψi µi (see (2.5)), ´ and Eω (ψi ) − ψi µ → Jω (µ),\nsince (ψi ) is maximizing for µ. It only remains to prove ψi (µi − µ) → 0. Since Jω (ψi ) is\nbounded (see (2.7), (1.37) yields C > 0 such that\n                                ˆ\n                                   ψi (µi − µj ) ≲ CJω (ψi , ψj )α\n\nfor all i, j, and hence\n                          ˆ\n                               ψi (µi − µj ) ≲ C max{Jω (µ, ψi ), Jω (µ, ψj )}α ,\n\nby (2.7). Since µj → µ weakly and Jω (µ, ψj ) → 0 as j → ∞, we infer\n                              ˆ\n                                ψi (µi − µ) ≲ CJω (µ, ψi )α ,\n\nand we conclude, as desired, that the left-hand side tends to 0 as i → ∞.                                   □\n2.6. The Dirichlet quasi-metric. From now on, we assume that the orthogonality\nproperty holds for ω. Recall from Examples 2.17 and 2.20, that this is the case if X is a\ncompact Kähler manifold, and for any projective Berkovich space.\nTheorem 2.24. There exists a unique continuous functional\n                                         δω : M1ω × M1ω → R≥0 ,\nsuch that\n                             δω (MAω (φ), MAω (ψ)) = Jω (φ, ψ)                                          (2.21)\nfor all φ, ψ ∈ Dω . Furthermore:\n    (i) for all µ ∈ M1ω and ψ ∈ Dω we have\n                          δω (µ, MAω (ψ)) = Jω (µ, ψ),             δω (µ, µω ) = Jω (µ);                (2.22)\n     (ii) δω is a quasi-metric: for all µ, ν, ρ ∈ M1ω we have\n       δω (µ, ν) = 0 ⇔ µ = ν,      δω (µ, ν) ≈ δω (ν, µ),          δω (µ, ν) ≲ δω (µ, ρ) + δω (ρ, ν);   (2.23)\n     (iii) the quasi-metric δω satisfies the Hölder continuity property\n                      δω (µ, ν) − δω (µ′ , ν ′ ) ≲ max{δω (µ, µ′ ), δω (ν, ν ′ )}α R1−α                 (2.24)\n         for all R > 0 and µ, µ′ , ν, ν ′ ∈ M1ω,R , with α := 2−n ;\n\f                                 MEASURES OF FINITE ENERGY                                   25\n\n   (iv) for all R > 0 and φ, ψ ∈ Dω,R , µ, ν ∈ M1ω,R , we have the Hölder estimate\n                      ˆ\n                        (φ − ψ)(µ − ν) ≲ Jω (φ, ψ)α δω (µ, ν)1/2 R1/2−α .               (2.25)\n\n  We call δω the Dirichlet quasi-metric of M1ω .\nLemma 2.25. For all µ ∈ M1ω,R and φ, ψ, τ ∈ Dω,R , we have\n\n               |Jω (µ, φ) − Jω (MAω (τ ), ψ)| ≲ max{Jω (µ, τ ), Jω (φ, ψ)}α R1−α ;      (2.26)\n                   ˆ\n                     (φ − ψ)(µ − MAω (τ )) ≲ Jω (φ, ψ)α Jω (µ, τ )1/2 R1/2−α .          (2.27)\n\nProof. When µ lies in the image of MAω : Dω → M1ω this is equivalent to (1.38) and (1.37), in\nview of (2.5) and (2.6). By Theorem 2.23 the image of MAω is dense in M1ω , and the general\ncase thus follows by continuity in the strong topology of all functions of µ involved.     □\n\nProof of Theorem 2.24. Uniqueness is clear, since (2.21) determines δω on the image of\nMAω : Dω → M1ω , which is dense in the strong topology, by Theorem 2.23. To show exis-\ntence, pick µ, ν ∈ M1ω , and choose a maximizing sequences (ψi ) for ν. We can then find\nR > 0 such that µ ∈ M1ω,R and ψi ∈ Dω,R for all i, and (2.26) and (2.7) yield\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "2209.04879",
      "public_source": "https://arxiv.org/pdf/2209.04879v2",
      "saved_version": "2209.04879v2",
      "application_check": "Scope audit only: Remark 4.4 distinguishes definition of E1 over arbitrary fields from construction of its MA operator; the exact phrase characteristic zero is preserved rather than strengthened to residue characteristic zero.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.pdf",
          "bytes": 633342,
          "sha256": "55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.txt",
          "bytes": 185043,
          "sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
          "matches_supplied_hash": true
        },
        {
          "kind": "abstract_html",
          "path": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.html",
          "bytes": 40370,
          "sha256": "1b719dcc2de6a7437184f28dbaf37384bf39673fc8b66a35a4dc716f0cba5341",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/2209.04879-Remark-4.4.txt",
          "source_line_first": 1975,
          "source_line_last": 2001,
          "pdf_page_first": 35,
          "pdf_page_last": 35,
          "sha256": "c6356120d2fe735f2be0673b646e503f75004aa35b3a2375194767222ab54edd",
          "literal_text": "                    Z                           Z\n                        φ0 MA(φ1 , ..., φn ) =      φ1 MA(φ0 , φ2 , ..., φn ).\n                      X                           X\n  The Monge-Ampère measure can then be extended by density to more general metrics:\nTheorem 4.3. [BE21, thm. 8.4]\nLet K be a complete valued field, X/K an n-dimensional projective scheme and L1 ,...,Ln\nline bundles on X. Then the Monge-Ampère operator:\n                             (φ1 , ..., φn ) 7→ ddc φ1 ∧ ... ∧ ddc φn\nadmits a unique extension to continuous psh metrics on the Li . The extension is further-\nmore continuous with respect to the topology of uniform convergence and the weak topology\nof Radon measures.\nRemark 4.4. While the class E 1 (X, L) of finite-energy psh metrics on L is defined over any\nnon-archimedean field K, it is unclear in general how to extend the Monge-Ampère operator\non the latter. Note however that in the case where K is discretely-valued of characteristic\nzero, this extension was constructed in [BFJ16], and the trivially-valued case was handled\nin [BJ22].\nRemark 4.5. The Chambert-Loir - Ducros [CLD12] approach to pluripotential theory on\nBerkovich spaces makes sense of the curvature current ddc φ of a continuous psh metric,\nand its wedge products, in a spirit close to the work of Bedford-Taylor in the complex case.\nNotably, [CLD12, thm. 6.9.3] states that the wedge product ddc φ1 ∧ ... ∧ ddc φn coincides\nwith the mixed Monge-Ampère measure as described in example 4.1 when φ1 ,..., φn are psh\nmodel metrics, whence the notation.\n4.2. The Monge-Ampère equation. Let X be a smooth n-dimensional complex man-\nifold, and L an ample line bundle on X. Then Yau’s celebrated solution to the Calabi\nconjecture asserts the following:\nTheorem 4.6. [Yau78] Let µ be a smooth volume form on X, normalized to have total\nmass 1. Then there exists a unique (up to an additive constant) smooth, positive definite\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "2506.13548",
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "saved_version": "https://arxiv.org/pdf/2506.13548v2",
      "application_check": "Scope audit only: Gubler-Rabinoff v2 explicitly says additional hypotheses may be needed for regularization and MA and that this is not the subject of the paper. No BFJ E1 equation result is inferred from its maximum principles.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
          "bytes": 473505,
          "sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
          "bytes": 153456,
          "sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/2506.13548-title-and-scope.txt",
          "source_line_first": 1,
          "source_line_last": 105,
          "pdf_page_first": 1,
          "pdf_page_last": 3,
          "sha256": "86ce89e6662882385c8941c75faf8cbcf0fd6b80ce4d3413f588b7d4510a944f",
          "literal_text": "                                            CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES\n\n                                                                          WALTER GUBLER AND JOSEPH RABINOFF\n\n\n                                                   ABSTRACT. First we extend the theory of subharmonic functions on smooth strictly k-\n                                                   analytic curves from Thuillier’s thesis to the case of possibly singular analytic curves over\n                                                   a non-archimedean field k. Classically psh functions are then defined as in complex geom-\narXiv:2506.13548v2 [math.AG] 17 Sep 2025\n\n\n\n\n                                                   etry by using pullbacks to analytic curves (and requiring compatibility with base change).\n                                                   We give various properties of classically psh functions including a local and a global max-\n                                                   imum principle. As a consequence, we show that the space of pluriharmonic functions on\n                                                   a quasi-compact Berkovich space is finite dimensional. As a technical tool, we use that a\n                                                   connected Berkovich space is connected by analytic curves.\n\n\n\n\n                                                                                      1. INTRODUCTION\n                                              Plurisubharmonic functions are the complex analytic counterparts of subharmonic func-\n                                           tions in real analysis. To recall the definition, we begin with the notion of subharmonicity\n                                           on the complex line. Let Ω ⊂ C be an open set and let u: Ω → [−∞, ∞) be an upper\n                                           semicontinuous function. Then u is subharmonic if for every closed ball B(a, r) with cen-\n                                           ter a and radius r contained in Ω and every continuous function h: B(a, r) → R which\n                                           is harmonic on the open ball B(a, r) such that u ≤ h on the boundary ∂ B(a, r), we have\n                                           u ≤ h on B(a, r). Note that the notion of (sub)harmonicity is insensitive to biholomorphic\n                                           maps, hence makes sense on any one-dimensional complex manifold.\n                                              Now let X be any complex manifold (without boundary, for simplicity) and let u: X →\n                                           [−∞, ∞) be an upper semicontinuous function. Then u is plurisubharmonic or psh if,\n                                           for every holomorphic map f : B(0, 1) → X from the open unit ball B(0, 1) ⊂ C, the\n                                           pullback u ◦ f is subharmonic on B(0, 1). We say that u is pluriharmonic if u and −u are\n                                           plurisubharmonic.\n                                              Plurisubharmonicity was introduced by Lelong [Lel42] and Oka [Oka42] indepen-\n                                           dently to study holomorphic convexity. It turned out to be a crucial positivity notion\n                                           on complex manifolds. Plurisubharmonic functions satisfy the following properties:\n                                               (1) The space of psh functions forms a convex cone: that is, if u1 , u2 are psh and\n                                                   λ1 , λ2 ≥ 0, then λ1 u1 + λ2 u2 is psh.\n                                               (2) If u1 , u2 are psh functions then max{u1 , u2 } is psh.\n                                               (3) If {uk }k≥1 is a decreasing sequence of psh functions, then u = lim uk is psh.\n                                               (4) A psh function u satisfies the local maximum principle: if u attains a local maxi-\n                                                   mum at x 0 ∈ X , then u is constant on the connected component of x 0 in X .\n\n                                              2020 Mathematics Subject Classification. Primary 14G40; Secondary 31C05, 32P05, 32U05.\n                                              Key words and phrases. Berkovich spaces, plurisubharmonic and pluriharmonic functions.\n                                              W. Gubler was supported by the collaborative research center SFB 1085 Higher Invariants - Interactions\n                                           between Arithmetic Geometry and Global Analysis funded by the Deutsche Forschungsgemeinschaft.\n                                                                                                1\n\f2                                 W. GUBLER AND J. RABINOFF\n\n   Now we consider the non-Archimedean situation. Let k be a field that is complete\nwith respect to a non-Archimedean absolute value | |. We refer to Section 2 for the\nnotions used from non-Archimedean geometry. The theory of subharmonic functions\non a smooth, strictly analytic k-curve X has been completely worked out by Thuillier in\nhis thesis [Thu05]. Thuillier begins by defining harmonic functions as certain piecewise\nlinear functions satisfying a balancing condition; see [Thu05, §2.3] or 3.2. He then\ndefines a subharmonic function to be an upper semicontinuous function u: X → R ∪\n{−∞} such that, for every strictly affinoid domain U ⊂ X and every harmonic function\nh on U such that u ≤ h on ∂ U, we have u ≤ h on U. Thuillier shows that subharmonic\nfunctions on smooth non-Archimedean curves satisfy the properties one would expect,\nin analogy to the complex case.\n   In higher dimensions, it is not completely clear yet what is the best definition for\nplurisubharmonic functions. There is the global approach by Zhang [Zha95], who de-\nfines a semipositive metric on a line bundle L over a projective k-variety X to be the\nuniform limit of metrics induced by nef models. This approach is used in Arakelov ge-\nometry for various arithmetic applications. For an ample class θ on X , Boucksom and\nJonsson [BJ22] give a far reaching global pluripotential theory on a projective variety\nover a trivially valued field. Some parts work for any non-Archimedean field, at least in\nresidue characteristic zero. These psh functions might be singular, and the definition uses\ndecreasing limits of semipositive model functions as in Zhang’s approach. Chambert–Loir\nand Ducros [CD25] have posted a second version of their work in which they give a new\ndefinition of psh functions which is functorial and is based on a transfinite regularization\nprocess.\n   In all of the above approaches, a maximum principle for plurisubharmonic functions\nis missing. In this paper, we propose another class of psh functions called classically\nplurisubharmonic functions in close analogy to the complex case. The definition is local,\nthe functions are upper semicontinuous, and we will show that properties (1)–(4) are\nsatisfied. It will be clear that classically psh functions form a maximal class of reasonable\nplurisubharmonic functions that is compatible with Thuillier’s definition for curves. In\nparticular, the psh functions from the above are classically psh (see 1.2 below).\n   To get regularization by smooth psh functions in the sense of Chambert-Loir and Ducros\nor to define a Monge–Ampère measure for psh functions, additional hypotheses as in\n[CD25] might be needed, but that is not the subject of this paper.\n\n1.1. Subharmonic functions on arbitrary k-analytic curves. In Section 3, we define\nsubharmonic functions on any k-analytic curve X to be the elements of the following\nsubsheaf of the sheaf of upper semicontinuous functions on X with range [−∞, ∞).\nIt is the smallest subsheaf that is functorial with respect to pullback, stable under base\nchange, and agrees with Thuillier’s subharmonic functions on smooth k-analytic curves.\nWe will show in Proposition 3.5 that subharmonic functions satisfy the properties (1)–(3)\nas in the complex case, and the local maximum principle on the interior Int(X ) = X \\ ∂ X .\n\n1.2. Plurisubharmonic functions on k-analytic spaces. We define classically plurisub-\nharmonic functions on k-analytic spaces as the elements of the smallest subsheaf of the\nsheaf of upper semicontinuous functions with range [−∞, ∞) that is functorial with\n\f             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              3\n\nrespect to pullback, stable under base change, and agrees with the above defined sheaf\nof subharmonic functions on k-analytic curves. In Section 4, we will show that classically\npsh functions satisfy properties (1)–(3).\n   We use the terminology classically psh to distinguish from the psh functions introduced\nby Chambert-Loir and Ducros in [CD25]. Note that psh functions are classically psh.\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "Thuillier",
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "saved_version": "https://theses.hal.science/tel-00010990v1/document",
      "application_check": "Scope audit only; curve singular equation/regularization is not substituted for the higher-dimensional surface proof, and no OCR-corrupted French statement is used as an indispensable input.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
          "bytes": 1507314,
          "sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
          "bytes": 679353,
          "sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/Thuillier-curve-equation-and-regularization.txt",
          "source_line_first": 5518,
          "source_line_last": 5535,
          "pdf_page_first": 108,
          "pdf_page_last": 108,
          "sha256": "b587e85381f04134d4c7e63e60fc0bc11954efdabdff9358691086dfd80a844e",
          "literal_text": "Corollaire 3.4.13. \u0016 Soit X une ourbe stri tement k -analytique lisse, onnexe et iso-\nmorphe à une omposante onnexe de l'intérieur d'un espa e k-a\u001enoïde ou à l'analyti\u001cée\nd'une ourbe k-algébrique a\u001ene . L'appli ation\n                                D0 (X) → D1 (X),     T 7→ ddc T\ninduit une bije tion de SH(X)/Γ(X, HX ) sur l'ensemble des mesures de Radon positives sur\nl'espa e topologique lo alement ompa t |X|.\n\n   Considérons maintenant une ourbe stri tement k-analytique propre et lisse X et spé iali-\nsons e qui pré ède dans le as d'un ouvert onnexe Ω de X tel que ∂Ω soit une partie non\nvide de I(X).\nLemme 3.4.14. \u0016 Il existe, pour tout point x ∈ Ω, une unique fon tion gx ∈ SH(Ω) telle\nque                    \u001a\n                          ddc gx = δx\n                          limy∈Ω, y→ζ gx (y) = 0 pour tout ζ ∈ ∂Ω\nDémonstration. L'uni ité dé oule du prin ipe du maximum.\n   Supposons tout d'abord que le point x appartienne à I(Ω) ; quelle que soit la omposante\n onnexe c de Ω−{x}, l'existen e d'une barrière en tout point de ∂c (proposition 3.1.20) garan-\ntit l'existen e, pour tout nombre réel λ, d'une unique fon tion ontinue gλ sur c, harmonique\n"
        },
        {
          "filename": "source-extracts/Thuillier-regularization.txt",
          "source_line_first": 5697,
          "source_line_last": 5743,
          "pdf_page_first": 111,
          "pdf_page_last": 112,
          "sha256": "5b3064190e41ada3721b0cc41cd0d310756c466fdaca1a4964eefe15606fc4b6",
          "literal_text": "toujours grâ e à la formule de Poin aré-Lelong, sa ourbure est [κ(x) : k]µ.                       2\n  Le théorème 3.4.2 se généralise sans di\u001e ulté au as de fais eaux inversibles munis de\nmétriques sous-harmoniques.\nThéorème 3.4.19. \u0016 Soit L un fais eau inversible sur une                    ourbe stri tement k-\nanalytique propre et lisse. Pour toute métrique sous-harmonique ||.|| sur L, la restri tion de ||.||\nà Ω est l'enveloppe supérieure d'une famille roissante (||.||λ ) de métriques sous-harmoniques\nlisses sur L|Ω et le ourant c1 (L, ||.||)|Ω est la limite des ourants c1 (L, ||.||λ ).\nDémonstration. La preuve du théorème 3.4.2 s'adapte sans di\u001e ulté à la situation présente.\nQuel que soit le sous-ensemble \u001cni S de I(X) tel que L soit trivial sur l'adhéren e de ha une\ndes omposantes onnexes de Y − S , il existe une unique métrique sous-harmonique lisse\n||.||S sur L telle que, pour tout U ∈ π0 (X − S) et toute trivialisation ε de L au voisinage\nde U , − log ||ε||S soit l'élément de Γ(U, HX ) ∩ C0 (U , R) qui oïn ide ave − log ||ε|| sur ∂U :\n  ette formule dé\u001cnit en e\u001bet ||.||S sans ambiguité en vertu de l'harmoni ité des fon tions de\ntransitions − log |f | et la sous-harmoni ité s'obtient omme elles des fon tions uS au théorème\n3.4.2.\n\f98\n\n\n\n   De la sous-harmoni ité de ||.|| dé oule que les métriques ||.||S forment une famille rois-\nsante lorsque S par ourt l'ensemble \u001cltrant des parties \u001cnies de I(Y ) satisfaisant aux ondi-\ntions pré édentes. Son enveloppe supérieure est la métrique ||.|| (même argument que dans la\ndémonstration du théorème 3.4.2).                                                          2\n\n  Étant donnés une ourbe stri tement k-analytique onnexe, propre et lisse X et un point\nx ∈ I(X), il existe, pour toute mesure de Radon positive µ sur X , un unique ourant T ∈\nD0 (X) tel que\n                                 \u001a              R   \u0001\n                                   ddc T = µ − X µ δx\n                                   T (x) = 0\n(théorème 3.3.13) et, vu le théorème 3.4.12, la ondition ddc T|X−{x} ≥ 0 implique que le\n ourant T|X−{x} se prolonge naturellement en une fon tion sous-harmonique sur X − {x}.\n   Nous noterons gx,µ l'unique fon tion X → R ∪ {−∞} qui est sous-harmonique sur X − {x}\net satisfait aux onditions       \u001a                 R  \u0001\n                                    ddc gx,µ = µ − X µ δx\n                                    gx,µ (x) = 0.\n     La formule\n                                  gy,µ = gx,µ + (gy,x − gx,µ (y))\nest immédiate pour tous points x, y ∈ I(X) ; puisque gx,y est une fon tion ontinue (et même\nlisse), elle implique en parti ulier la semi- ontinuité supérieure de gx,µ sur l'espa e X tout\nentier.\nRemarque 3.4.20. \u0016 La fon tion gx,µ est négative.\n   Appliqué à la mesure δD asso iée à un diviseur e\u001be tif, e qui pré ède dé\u001cnit sur le fais-\n eau inversible OX (D) une métrique lisse et sous-harmonique ||.|| de ourbure deg(D)δx :\n− log ||1D || = −gx,δD .\n   En parti ulier : tout fais eau inversible de degré 0 sur X peut être muni d'une métrique\nharmonique.\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "Berkovich",
      "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "saved_version": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "application_check": "Scope audit only: 1993 Etale cohomology paper, not the 1990 book cited internally by GJKM. No unseen base-change theorem is imported from it.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
          "bytes": 19118239,
          "sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
          "bytes": 418614,
          "sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/Berkovich-title.txt",
          "source_line_first": 1,
          "source_line_last": 35,
          "pdf_page_first": 1,
          "pdf_page_last": 2,
          "sha256": "092a7b81f4b893996e25ba02e843f7544892f955595dc75aca6ba5cc1928a606",
          "literal_text": "P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.\n\n\n\n\n V LADIMIR G. B ERKOVICH\n Étale cohomology for non-Archimedean analytic spaces\n Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161\n <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>\n\n\n\n\n      © Publications mathématiques de l’I.H.É.S., 1993, tous droits réservés.\n      L’accès aux archives de la revue « Publications mathématiques de l’I.H.É.S. » (http://\n      www.ihes.fr/IHES/Publications/Publications.html) implique l’accord avec les conditions géné-\n      rales d’utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou im-\n      pression systématique est constitutive d’une infraction pénale. Toute copie ou impression de\n      ce fichier doit contenir la présente mention de copyright.\n\n\n\n\n                               Article numérisé dans le cadre du programme\n                             Numérisation de documents anciens mathématiques\n                                           http://www.numdam.org/\n\f                                ETALE COHOMOLOGY\n                       FOR NON-ARCHIMEDEAN ANALYTIC SPACES\n                                                      by VLADIMIR G. BERKOVIGH (1)\n\n\n                                                                                CONTENTS\n\n\nINTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   7\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "1204.6277",
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "saved_version": "https://arxiv.org/pdf/1204.6277v2",
      "application_check": "Scope audit only: actual v2 is dated July 2025, real forms and currents on Berkovich spaces. No local wedge-product or transfinite psh construction is used to assert global BFJ E1 surjectivity.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
          "bytes": 4659053,
          "sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
          "bytes": 2153101,
          "sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/1204.6277-title-and-version.txt",
          "source_line_first": 1,
          "source_line_last": 26,
          "pdf_page_first": 1,
          "pdf_page_last": 2,
          "sha256": "1df0c35e974c8e483d2606e0f8758fb0177b9cc964d9b858cf9a1a4a23b9c6fb",
          "literal_text": "                                          FORMES DIFFÉRENTIELLES\n                                          RÉELLES ET COURANTS SUR LES\narXiv:1204.6277v2 [math.AG] 25 Jul 2025\n\n\n\n\n                                          ESPACES DE BERKOVICH\n\n\n\n\n                                                         Antoine Chambert-Loir\n                                                                Antoine Ducros\n\fAntoine Chambert-Loir\nUniversité Paris Cité, Institut de Mathématiques de Jussieu-Paris Rive Gauche,\nF-75013, Paris, France.\nE-mail : antoine.chambert-loir@math.univ-paris-diderot.fr\nAntoine Ducros\nSorbonne Université, Université de Paris, CNRS, Institut de Mathématiques de\nJussieu-Paris Rive Gauche, IMJ-PRG, F-75005, Paris, France.\nE-mail : antoine.ducros@imj-prg.fr\n\n\n\n\n"
        }
      ],
      "pdfinfo_returncode": 0
    },
    {
      "id": "1712.00980",
      "public_source": "https://arxiv.org/pdf/1712.00980v3",
      "saved_version": "1712.00980v3",
      "application_check": "Applied: Definition 8.1 with d=1, n=2 and perfect characteristic-p k; Theorem 6.3 discharges both Definitions 6.1 and 6.2 in dimension 3. Proposition 5.2 and section 9 give cofinal projective SNC models. Theorem 8.2/Corollary 8.3 and Corollary 9.1 give continuous envelopes and monotone regularization for every ample curvature class on this X. Section 9 explicitly transfers BFJ sections 3-6. Theorem 9.2 gives orthogonality. Theorem 9.3 itself retains skeleton support; it is not cited for arbitrary-support surjectivity. Only published model/envelope descent is used; no new unbounded base-change statement is inferred.",
      "files": [
        {
          "kind": "pdf",
          "path": "/workspace/research/shared-sources/P16-completion-envelopes-arxiv-1712.00980-20261004.pdf",
          "bytes": 776710,
          "sha256": "6c506c3ee23c6e36900a59f3f3fba1f26c4b22708756324f89af8668ed5771b6",
          "matches_supplied_hash": true
        },
        {
          "kind": "literal_extract",
          "path": "/workspace/research/shared-sources/P16-completion-envelopes-arxiv-1712.00980-20261004.txt",
          "bytes": 118056,
          "sha256": "2cfdf8ae09038a52e9e84b2cf58ac301002e37f5c9c24896cbe1717d694f5b51",
          "matches_supplied_hash": true
        },
        {
          "kind": "abstract_html",
          "path": "/workspace/research/shared-sources/P16-completion-envelopes-arxiv-1712.00980-20261004.html",
          "bytes": 42287,
          "sha256": "e695b96d103f9f82f4c005e17f405b56a1708caa29121c538349e04392692740",
          "matches_supplied_hash": true
        }
      ],
      "literal_extracts": [
        {
          "filename": "source-extracts/1712.00980-title-and-introduction.txt",
          "source_line_first": 1,
          "source_line_last": 250,
          "pdf_page_first": 1,
          "pdf_page_last": 5,
          "sha256": "b6ae27b9b0bcbb5f23f8f982e162f06fc0bb08550cc5deee484476f8e46c4501",
          "literal_text": "                                                 CONTINUITY OF PLURISUBHARMONIC ENVELOPES IN\n                                                  NON-ARCHIMEDEAN GEOMETRY AND TEST IDEALS\n                                               (WITH AN APPENDIX BY JOSÉ IGNACIO BURGOS GIL AND\n                                                                MARTÍN SOMBRA)\n\n                                                WALTER GUBLER, PHILIPP JELL, KLAUS KÜNNEMANN, AND FLORENT MARTIN\narXiv:1712.00980v3 [math.AG] 22 Nov 2018\n\n\n\n\n                                                   Abstract. Let L be an ample line bundle on a smooth projective variety X over a\n                                                   non-archimedean field K. For a continuous metric on Lan , we show in the following\n                                                   two cases that the semipositive envelope is a continuous semipositive metric on Lan\n                                                   and that the non-archimedean Monge-Ampère equation has a solution. First, we prove\n                                                   it for curves using results of Thuillier. Second, we show it under the assumption that\n                                                   X is a surface defined geometrically over the function field of a curve over a perfect\n                                                   field k of positive characteristic. The second case holds in higher dimensions if we\n                                                   assume resolution of singularities over k. The proof follows a strategy from Boucksom,\n                                                   Favre and Jonsson, replacing multiplier ideals by test ideals. Finally, the appendix by\n                                                   Burgos and Sombra provides an example of a semipositive metric whose retraction is\n                                                   not semipositive. The example is based on the construction of a toric variety which\n                                                   has two SNC-models which induce the same skeleton but different retraction maps.\n\n                                                   MSC: Primary 32P05; Secondary 13A35, 14G22, 32U05\n\n\n\n\n                                                                                       Contents\n                                             1. Introduction                                                                                    2\n                                             2. Model metrics, semipositive metrics, and envelopes                                              5\n                                             3. Continuity of plurisubharmonic envelopes on curves                                              9\n                                             4. Asymptotic test ideals                                                                         14\n                                             5. Descent for model functions                                                                    15\n                                             6. Resolution of singularities                                                                    16\n                                             7. Uniform convergence to the envelope of the zero function                                       17\n                                             8. Continuity of the envelope                                                                     20\n                                             9. The Monge–Ampère equation                                                                      22\n                                             Appendix A. The skeleton and the retraction in the toric case\n                                                           by José Ignacio Burgos Gil and Martín Sombra                                        24\n                                             References                                                                                        30\n\n\n\n                                              Date: November 26, 2018.\n                                              W. Gubler, K. Künnemann and F. Martin were supported by the collaborative research center SFB\n                                           1085 funded by the Deutsche Forschungsgemeinschaft. P. Jell was for part of this work also supported by\n                                           the SFB 1085 and for the other part by the DFG Research Fellowship JE 856/1-1. J. I. Burgos was par-\n                                           tially supported by MINECO research projects MTM2016-79400-P and by ICMAT Severo Ochoa project\n                                           SEV-2015-0554. M. Sombra was partially supported by the MINECO research project MTM2015-65361-\n                                           P and through the \"María de Maeztu\" program for units of excellence MDM-2014-0445.\n                                                                                             1\n\f2                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\n                                    1. Introduction\n   Let L be an ample line bundle on an n-dimensional complex projective variety X and\nlet µ be a smooth volume form on the associated complex manifold X an of total mass\ndegL (X). The Calabi conjecture claims that there is a smooth semipositive metric k k\non Lan , unique up to positive multiples, solving the Monge–Ampère equation\n(1.1)                                c1 (L, k k)∧n = µ.\nThis was conjectured by Calabi who proved uniqueness [Cal54, Cal57] and the existence\npart was solved by Yau [Yau78]. In fact, they proved a more general version in the\nsetting of compact Kähler manifolds, but this will not be relevant for our paper.\n   The motivation of this paper is the study of the non-archimedean version of this\nconjecture. We consider a non-archimedean field K with valuation ring K ◦ . Let L be\nan ample line bundle on an n-dimensional smooth projective variety X over K. The line\nbundle L induces a line bundle Lan on the analytification X an of X as a Berkovich non-\narchimedean analytic space. In non-archimedean geometry, model metrics on Lan play\na similar role as smooth metrics on line bundles on complex manifolds. We call a model\nmetric on Lan semipositive if it is induced by an nef model. Zhang [Zha95] introduced\ncontinuous semipositive metrics on Lan as uniform limits of semipositive model metrics.\nFor such metrics, Chambert-Loir [CL06] defined a Monge–Ampère measure c1 (L, k k)∧n\non X an which is a positive Radon measure of total mass degL (X). These measures\nplay an important role in arithmetic equidistribution results (see [Yua08]). We refer to\nSection 2 for details about these notions.\n   In the non-archimedean Calabi–Yau problem, one looks for continuous semipositive\nmetrics on Lan solving the Monge–Ampère equation (1.1). Yuan and Zhang [YZ17]\nproved that such a metric is unique up to constants. The existence of a singular semi-\npositive solution was proven in the case of curves by Thuillier [Thu05, Cor. 3.4.13].\nLiu [Liu11] proved existence of a continuous semipositive solution for totally degenerate\nabelian varieties A if µ is a smooth volume form on the canonical skeleton of A.\n   Next, we describe the fundamental existence result of Boucksom, Favre and Jonsson\n[BFJ16a, BFJ15]. We assume that K is a complete discretely valued field with valuation\nring K ◦ . We recall that an SNC-model is a regular model of X such that the special\nfiber has simple normal crossing support. Boucksom, Favre and Jonsson prove in [BFJ15,\nThm. A] that the non-archimedean Calabi–Yau problem has a continuous semipositive\nsolution k k if the following assumptions are satisfied:\n    (a) The characteristic of the residue field K̃ is zero.\n    (b) The positive Radon measure µ is supported on the skeleton of a projective SNC-\n        model of X and satisfies µ(X an ) = degL (X).\n    (c) The smooth projective variety X is of geometric origin from a 1-dimensional\n        family over K̃.\nThe last condition will play an important role in this paper. More generally, we say\nthat X is of geometric origin from a d-dimensional family over the field k if there is a\ncodimension 1 point b in a normal variety B over k such that K ◦ is the completion of\nOB,b and such that X is defined over the function field k(B). In [BGJKM16, Thm. D],\nwe have shown that (c) is not necessary for the existence of a continuous semipositive\nsolution of the non-archimedean Calabi–Yau problem if we assume (a) and (b).\n   We will later look for a similar result in equicharacteristic p > 0. To do so, we have to\nunderstand the basic ingredients in the proof of the existence result of Boucksom, Favre\nand Jonsson. In [BFJ16a], the authors develop a global pluripotential theory on X an\n\f                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                3\n\n\nfor singular semipositive metrics using the piecewise linear structure on the skeletons\nof SNC-models. It is here where Assumption (a) enters the first time as resolution of\nsingularities is used to have sufficiently many SNC-models of X at hand. For a continuous\nmetric k k, we define the semipositive envelope P (k k) by\n(1.2) P (k k) := inf{k k0 | k k ≤ k k0 and k k0 is a semipositive model metric on Lan }.\nIt is absolutely crucial for pluripotential theory to prove that P (k k) is continuous as this\nis equivalent to the monotone regularization theorem (see [BFJ16a, Lemma 8.9]). The\nmonotone regularization theorem is the basis in [BFJ15] to introduce the Monge–Ampère\nmeasure, capacity and energy for singular semipositive metrics. The proof of continuity\nof P (k k) in [BFJ16a, §8] uses multiplier ideals on regular projective models. In the proof\nof the required properties of multiplier ideals (see [BFJ16a, Appendix B]), the authors\nuse vanishing results which hold only in characteristic zero, and hence Assumption (a)\nplays an important role here as well.\n   A second important result is the orthogonality property for P (k k) given in [BFJ15,\nThm. 7.2]. Multiplier ideals occur again in their proof and it is here where the geometric\nassumption (c) is used. However, it is shown in [BGJKM16, Thm. 6.3.3] that continuity of\nP (k k) is enough to prove the orthogonality property without assuming (a) or (c). Then\nthe variational method of Boucksom, Favre and Jonsson can be applied to prove existence\nof a continuous semipositive solution for the non-archimedean Calabi–Yau problem.\n   This makes it very clear that continuity of the semipositive envelope P (k k) plays a\ncrucial role in the non-archimedean Calabi–Yau problem. It is the main object of study\nin this paper. In Section 2, we will study the basic properties of a slight generalization of\nP (k k) which is called the θ-psh envelope for a closed (1, 1)-form θ on X. For the sake of\nsimplicity, we will restrict our attention in the introduction to the semipositive envelope\nP (k k), while all the results hold more generally for the θ-psh envelope assuming that\nthe de Rham class of θ is ample.\n   In Section 3, we will look at continuity of the semipositive envelope in the case of a\nsmooth projective curve X over an arbitrary complete non-archimedean field K. Poten-\ntial theory on the curve X an was developed in Thuillier’s thesis [Thu05]. We will use\nThuillier’s results and the slope formula of Katz, Rabinoff, and Zureick-Brown [KRZB16,\nThm. 2.6] to prove:\nTheorem 1.1. Let L be an ample line bundle on a smooth projective curve X over any\nnon-archimedean field K. Then P (k k) is a continuous semipositive metric on Lan for\nany continuous metric k k on Lan .\n   A slightly more general version will be proved in Theorem 3.1. The following is\nimportant in the proof: Let L be any line bundle on the smooth projective curve X. We\nassume that X has a strictly semistable model X such that Lan has a model metric k k0\nassociated to a line bundle on X . For any metric k k on Lan , we consider the function\nϕ := − log(k k/k k0 ). Let pX : X an → ∆ be the canonical retraction to the skeleton ∆\nassociated to X . Then\n(1.3)                               k k∆ := e−ϕ◦pX k k0\nis a metric on Lan which does not depend on the choice of k k0 . The following result is\ncrucial in the proof of Theorem 1.1:\nProposition 1.2. Using the hypotheses above, we consider a model metric k k of Lan .\nThen we have the following properties:\n    (i) The metric k k∆ is a model metric.\n\f4                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\n     (ii) There is an equality of measures c1 (L, k k∆ ) = (pX )∗ (c1 (L, k k)).\n    (iii) If k k is semipositive, then k k∆ is semipositive and k k∆ ≤ k k.\n   This will be proven in Propositions 3.5 and 3.8. It would make pluripotential theory\nand the solution of the non-archimedean Calabi–Yau problem much easier if Proposition\n1.2 would also hold in higher dimensions as we could work more combinatorically on\nskeletons. It is still true that k k∆ is a model metric which satisfies k k∆ ≤ k k. Burgos\nand Sombra show in a two dimensional toric counterexample in the Appendix that k k∆\ndoes not have to be semipositive.\n   We show now that Proposition 1.2 is also crucial for the existence of the solution of the\nnon-archimedean Calabi–Yau problem in the case of curves arguing as in [BFJ16b, §9].\nBy Thuillier [Thu05, Cor. 3.4.13], there is a semipositive metric k k solving (1.1), but it\nmight be singular. Here, semipositive means that the metric is an increasing pointwise\nlimit of semipositive model metrics of the ample line bundle L. If we assume that the\npositive Radon measure µ has support in the skeleton ∆ of a strictly semistable model X\nof X, then it follows easily from Proposition 1.2 that k k∆ is a continuous semipositive\nmetric solving (1.1). Burgos and Sombra show in their counterexample in the Appendix\nthat this does not hold in higher dimensions either.\n   To look for solutions of the higher dimensional non-archimedean Monge–Ampère equa-\ntion in positive characteristic, we will replace the use of multiplier ideals by the use of test\nideals. Test ideals were introduced by Hara and Yoshida [HY03] using a generalization\nof tight closure theory. In Section 4, we will gather the necessary facts about test ideals\nmainly following [Mus13] and so we work on a smooth variety X over a perfect field k\nof characteristic p > 0. Similarly as in the case of multiplier ideals, one can define an\nasymptotic test ideal τ (λkDk) of exponent λ ∈ R≥0 for a divisor D on X. Crucial for us\nis that τ (λkDk) satisfies a subadditivity property and the following uniform generation\nproperty:\nTheorem 1.3. Let X be a projective scheme over a finitely generated k-algebra R such\nthat X is a smooth n-dimensional variety over k. We assume that H is an ample and\nbasepoint-free divisor, D is a divisor with h0 (X, O(mD)) 6= 0 for some m ∈ N>0 and E\nis a divisor such that the Q-divisor D − λE is nef for some λ ∈ Q≥0 . Then the sheaf\nOX (KX/k + E + dH) ⊗OX τ (λ · kDk) is globally generated for all d ≥ n + 1.\n   This was proven by Mustaţă if X is projective over k. As we will later work over\ndiscrete valuation rings, we need the more general version with X only projective over\nR. This will be possible in Theorem 4.6 as we can replace the use of Fujita’s vanishing\ntheorem in Mustaţă’s proof by Keeler’s generalization.\n   Now we come to the non-archimedean Calabi–Yau problem in equicharacteristic p >\n0. For the remaining part of the introduction, we now fix an n-dimensional smooth\nprojective variety X over a complete discretely valued field K of characteristic p. To\napply the results on test ideals, we have to require that X is of geometric origin from a\nd-dimensional family over a perfect field k. We also fix an ample line bundle L on X.\nTheorem 1.4. Under the hypotheses above, we assume that resolution of singularities\nholds over k in dimension d + n. Then the semipositive envelope P (k k) of a continuous\nmetric k k on Lan is a continuous semipositive metric on Lan .\n  For the precise definition about resolution of singularities, we refer to Definition 6.1.\nAs resolution of singularities is known in dimension 3 over a perfect field by a result of\nCossart and Piltant [CP09, Thm. p. 1839], Theorem 1.4 is unconditional if X is a smooth\nprojective surface of geometric origin from a 1-dimensional family over k.\n\f                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                              5\n\n\n   In Section 7, we will prove Theorem 1.4 in the case when k k is a model metric\nassociated to a model which is also defined geometrically over k. We will follow the\nproof of Boucksom, Favre, and Jonsson, replacing multiplier ideals by test ideals. As\nwe use a rather weak notion of resolution of singularities, a rather subtle point in the\nargument is necessary in the proof of Lemma 7.5 which involves a result of Pépin about\nsemi-factorial models. Theorem 1.4 will be proved in full generality in Section 8 using\nthe ddc -lemma and basic properties of the semipositive envelope. In fact, we will prove\nin Theorem 8.2 a slightly more general result.\n   If we use additionally that embedded resolution of singularities (see Definition 6.2)\nholds over k in dimension d + n, then the family of projective SNC-models will be cofinal\nin the category of all models of X. We will see in Section 9 that this and Theorem\n1.4 allow us to set up the pluripotential theory from [BFJ16a] on X an . By [BFJ15,\nThm. 7.2] again, the continuity of P (k k) yields that the orthogonality property holds for\nany continuous metric on Lan . We will use this in Section 9 to show that the variational\nmethod of Boucksom, Favre and Jonsson proves the following result (see Theorem 9.3).\nTheorem 1.5. Let X be an n-dimensional smooth projective variety of geometric origin\nfrom a d-dimensional family over a perfect field k of characteristic p > 0. We assume\nthat resolution of singularities and embedded resolution of singularities hold over k in\ndimension d + n. Let L be an ample line bundle on X and let µ be a positive Radon mea-\nsure supported on the skeleton of a projective SNC-model of X with µ(X an ) = degL (X).\nThen the non-archimedean Monge–Ampère equation (1.1) has a continuous semipositive\nmetric k k on Lan as a solution.\n  Cossart and Piltant [CP08, CP09] have shown resolution of singularities and embed-\nded resolution of singularities in dimension 3 over a perfect field, hence Theorem 1.5\nholds unconditionally for a smooth projective surface X of geometric origin from a 1-\ndimensional family over the perfect field k.\nAcknowledgement. We thank Mattias Jonsson for his valuable comments on a first\nversion, Matthias Nickel for helpful discussions, and the referee for his useful remarks.\n\n                            Notations and conventions\n  Let X be a scheme. An ideal in OX is a quasi-coherent ideal sheaf in OX . A divisor\non X is always a Cartier divisor on X. Given m ∈ N we write X (m) for the set of all\np ∈ X where the local ring OX,p has Krull dimension m. Let k be a field. A variety X\nover k is an integral k-scheme X which is separated and of finite type. A curve (resp.\nsurface) is a variety of dimension one (resp. two).\n  Throughout this paper (K, | |) denotes a complete non-archimedean valued field with\nvaluation ring K ◦ and residue field K̃. Starting in Section 7 we will assume furthermore\nthat the valuation is discrete and that K has positive characteristic p > 0. In this case\n                                   ∼\nthere exists an isomorphism K ◦ −→ K̃[[T ]] [Mat89, Thm. 29.7]. Let X be a K-variety.\nWe denote the analytification of X in the sense of Berkovich [Ber90, Thm. 3.4.1] by X an .\n\n            2. Model metrics, semipositive metrics, and envelopes\n  Let X be a proper variety over a complete non-archimedean valued field (K, | |).\n2.1. A model of X is given by a proper flat scheme X over S := Spec K ◦ together with\n"
        },
        {
          "filename": "source-extracts/1712.00980-model-envelope-and-descent.txt",
          "source_line_first": 280,
          "source_line_last": 422,
          "pdf_page_first": 6,
          "pdf_page_last": 9,
          "sha256": "24396132a07554201e2a7805d2a4883fd8023f03330af24109d0f12102051940",
          "literal_text": "in Xs . We call a line bundle L on X nef if the class of L in N 1 (X /S) is nef.\n2.4. We define Z 1,1 (X)Q as the direct limit\n(2.1)                           Z 1,1 (X)Q := lim N 1 (X /S)Q ,\n                                              −→\nwhere X runs over the isomorphism classes of models of X. The space of closed (1, 1)-\nforms on X is defined as Z 1,1 (X) := Z 1,1 (X)Q ⊗Q R. Let L be a line bundle on X. Let\nk k be a model metric on Lan which is determined on X by a model L of L⊗m . We\nmultiply the class of L in N 1 (X /S)Q by m−1 which determines a well defined class\nc1 (L, k k) ∈ Z 1,1 (X)Q ⊆ Z 1,1 (X) called the curvature form c1 (L, k k) of (L, k k). We\nhave a natural map ddc : D(X) → Z 1,1 (X); f 7→ c1 (OX , k ktriv · e−f ).\n    A closed (1, 1)-form θ is called semipositive if it is represented by a nef element θX ∈\nN 1 (X /S) for some model X of X. We say that a model metric k k on Lan for a line\nbundle L on X is semipositive if the same holds for the curvature form c1 (L, k k).\n2.5. For θ ∈ Z 1,1 (X) we denote by\n             PSHD (X, θ) = {f ∈ D(X) | θ + ddc f ∈ Z 1,1 (X) is semipositive}\nthe set of θ-plurisubharmonic (θ-psh for short) model functions. Recall from [GM16,\nProp. 3.12] that the set PSHD (X, θ) is stable under the formation of max.\n2.6. If Y is a proper variety over an arbitrary field k, we denote by N 1 (Y )Q the rational\nvector space Pic (Y )⊗Q modulo numerical equivalence. Similarly, we denote by N 1 (Y ) =\nN 1 (Y )Q ⊗Q R the real vector space Pic (Y ) ⊗ R modulo numerical equivalence. A class\nin N 1 (Y ) is called ample if it is an R>0 -linear combination of classes induced by ample\nline bundles on Y . An element α ∈ N 1 (Y )Q (resp. α ∈ N 1 (Y )) is called nef if α · C ≥ 0\nfor all closed curves C in Y .\n\f                      CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                7\n\n\n2.7. The restriction maps N 1 (X /S) → N 1 (X), [L ] 7→ [L |X ] induce a linear map\n{ } : Z 1,1 (X) −→ N 1 (X), θ 7→ {θ}. We call {θ} the de Rham class of θ.\nDefinition 2.8. Let X be a projective variety over K and θ ∈ Z 1,1 (X) with de Rham\nclass {θ} ∈ N 1 (X). The θ-psh envelope Pθ (u) of u ∈ C 0 (X an ) is the function\n(2.2)   Pθ (u) : X an → R ∪ {−∞}, Pθ (u)(x) = sup{ϕ(x) | ϕ ∈ PSHD (X, θ) ∧ ϕ ≤ u}.\n   Note that Pθ (u) is a real valued function if and only if there exists a θ-psh model\nfunction. For the existence of a θ-psh model function, it is necessary that the de Rham\nclass {θ} is nef (see [GM16, 4.8] and [BFJ16a, Rem. 5.4]). If {θ} is ample, then there\nexists always a θ-psh model function and hence Pθ (u) is a real valued function. If there\nis no θ-psh function, then Pθ (u) ≡ −∞ by definition.\n   If the residue characteristic is zero and if the de Rham class {θ} is ample, our defi-\nnition of Pθ (u) is by [BFJ16a, Thm. 8.3 and Lemma 8.9] equivalent to the definition of\nBoucksom, Favre, and Jonsson in [BFJ16a, Def. 8.1] .\n   The next proposition collects elementary properties of envelopes.\nProposition 2.9. Let u, u0 ∈ C 0 (X an ) and θ, θ0 ∈ Z 1,1 (X).\n     (i) If u ≤ u0 then Pθ (u) ≤ Pθ (u0 ).\n    (ii) We have Ptθ+(1−t)θ0 (tu + (1 − t)u0 ) ≥ tPθ (u) + (1 − t)Pθ0 (u0 ) for all t ∈ [0, 1].\n   (iii) We have Pθ (u) + c = Pθ (u + c) for each c ∈ R.\n    (iv) We have Pθ (u) − v = Pθ+ddc v (u − v) for each v ∈ D(X).\n     (v) If Pθ (u) 6≡ −∞, then we have supX an |Pθ (u) − Pθ (u0 )| ≤ supX an |u − u0 |.\n    (vi) If θ is determined on a model X , if the de Rham class {θ} is ample and if\n         θm → θ in N 1 (X /S), then Pθm (u) → Pθ (u) uniformly on X an .\n   (vii) We have Ptθ (tu) = tPθ (u) for all t ∈ R>0 .\n  (viii) Assume Pθ (u) 6≡ −∞. Then the envelope Pθ (u) is continuous if and only if it is\n         a uniform limit of θ-psh model functions.\nProof. The proof of Properties (i)–(vi) in [BFJ16a, Prop. 8.2] works in our setup as well.\nFor (vi) it was used that an ample line bundle extends to an ample line bundle on a\nsufficiently high model which holds in our more general setting by [GM16, Proposition\n4.11]. Property (vii) is obvious for t ∈ Q>0 and an easy approximation argument then\nshows (vii) in general. We have seen that θ-psh model functions are closed under max\nand hence the θ-psh model functions ϕ ≤ u form a directed family. We conclude that\n(viii) follows from Dini’s Theorem for nets [Kel75, p. 239] and the definition of Pθ (u). \u0003\n  For the next proposition, we assume for simplicity that the valuation on K is discrete.\nProposition 2.10. Let L be an ample line bundle on X, L an extension to a model X\nand θ = c1 (L, k kL ) ∈ Z 1,1 (X). For m > 0 let\n                      am = Im H 0 (X , L ⊗m ) ⊗K ◦ L ⊗−m → OX\n                                                              \u0001\n(2.3)\nbe the m-th base ideal of L and ϕm := m−1 log |am |. Then ϕm ∈ PSHD (X, θ) and\n(2.4)                            lim ϕm = sup ϕm = Pθ (0)\n                                m→∞          m∈N\n\npointwise on X an .\nProof. This is shown as in Step 1 of the proof of [BFJ16a, Thm. 8.5]. Observe that the\narguments which show (2.4) in loc. cit. on the subset of quasimonomial points give us\n(2.4) immediately on X an using our different definition of the θ-psh envelope.     \u0003\n\f8                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\nProposition 2.11. Let K 0 /K be a finite normal extension and let q : X 0 := X ⊗K K 0 →\nX be the natural projection. For θ ∈ Z 1,1 (X) and u ∈ C 0 (X an ), we have\n(2.5)                             q ∗ (Pθ (u)) = Pq∗ θ (q ∗ (u)).\nProof. Splitting the extension K 0 /K into a purely inseparable part and a Galois part,\nwe can reduce to two cases. In the first case of a purely inseparable extension, the result\nfollows from Lemma 2.13 below. In the second case of a Galois extension, we can apply\nthe argument of [BFJ15, Lemma A.4].                                                      \u0003\nRemark 2.12. (i) We always equip strictly K-analytic spaces with the G-topology induced\nby the strictly K-affinoid domains. We refer to [Ber90, §2.2] for the notion of a strictly\nK-affinoid domain and to [Ber93, §1.6] for the construction of the G-topology.\n   (ii) We recall from [GM16, Def. 2.8, 2.11] that a piecewise Q-linear function on a\nstrictly K-analytic space W is a function f : W → R such that there is a G-covering\n{Ui }i∈I of W by strictly affinoid domains, analytic functions γi ∈ O(Ui )× and non-zero\nmi ∈ N with mi f = − log |γi | on Ui for every i ∈ I. By [GM16, Rem. 2.6, Prop. 2.10],\nthe notions of model functions and Q-linear functions agree.\nLemma 2.13. Let L be a line bundle on X. Let K 0 /K be a finite purely inseparable\nextension and let q : X 0 := X ⊗K K 0 → X be the natural projection. G-topology induced\nby the strictly K-affinoid domains. Then the map (X 0 )an → X an is a homeomorphism\nand it also identifies the G-topologies. The map q ∗ induces a bijection between the set\nof model metrics on L and the set of model metrics on q ∗ (L). Moreover this bijection\nidentifies semipositive metrics on L and on q ∗ (L).\nProof. As in Remark 2.12 we use the G-topology induced by the strictly K-affinoid\ndomains. We first prove that the map q : (X 0 )an → X an is a homeomorphism and that\nit also identifies the G-topologies. In fact, this follows easily from the following claim:\n   Step 1: Let V be a strictly affinoid space over K and V 0 := V ⊗  ˆ K K 0 . Then the natural\nprojection q : V 0 → V is a homeomorphism which identifies the G-topologies.\n   Let pe = [K 0 : K] be the degree of the purely inseparable field extension. It is clear\nthat for every g ∈ O(V 0 ), there is f ∈ O(V ) with\n                                            e\n(2.6)                                     g p = f ◦ q.\nThis property easily shows that q : V 0 → V is a homeomorphism which we read now as\nan identification. Using that (2.6) holds also for rational functions g on V 0 and f on V ,\nwe see that V and V 0 have the same strictly rational domains. By the Gerritzen–Grauert\ntheorem [BGR84, Cor. 7.3.5/3], we deduce the Step 1.\n   Next we prove the bijective correspondence between the model metrics on L and on L0 .\nSince L admits a model metric [GM16, 2.1], it is enough to show that we have a bijective\ncorrespondence between model functions on X an and model functions on (X 0 )an . By\nRemark 2.12 we may check the same correspondence for Q-linear functions. This may\nthen be done G-locally and hence the correspondence follows from the following step.\n   Step 2: Using the same assumptions as in Step 1, the map f 7→ f ◦q is an isomorphism\nfrom the group of piecewise Q-linear functions on V onto the group of piecewise Q-linear\nfunctions on V 0 .\n   Using the above definition of piecewise Q-linear functions, Step 1 and (2.6) yield easily\nStep 2.\n   To deduce the lemma, it remains to check that the identification between the model\nmetrics on L and L0 preserves semipositivity. This is an easy consequence of the projec-\ntion formula applied to finite morphisms between closed curves in the special fibers of\nmodels.                                                                                   \u0003\n\f                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                9\n\n\n           3. Continuity of plurisubharmonic envelopes on curves\n  In this section, K is any field endowed with a non-trivial non-archimedean complete\nvaluation v : K → R with value group Γ ⊂ R. In this section, we consider a smooth\nprojective curve X over K. The goal is to prove the following result:\nTheorem 3.1. If θ is a closed (1, 1)-form on X an with nef de Rham class {θ} and if\nu ∈ C 0 (X an ), then Pθ (u) is a uniform limit of θ-psh model functions and thus Pθ (u) is\ncontinuous on X an .\n3.2. As a main tool in the proof, we need strictly semistable models of X and their\ncanonical skeletons. This construction is due to Berkovich in [Ber99]. We recall here\nonly the case of a smooth projective curve X over K for which we can also refer to\n[Thu05].\n   A K ◦ -model X of X as in 2.1 is called strictly semistable if there is an open covering of\nX by open subsets U such that there are étale morphisms U → Spec(K ◦ [x, y]/(xy −ρU ))\nfor some ρU ∈ K ◦◦ . Applying the construction in [Thu05, §2.2] to the associated formal\nscheme Xˆ , we get a canonical skeleton S(X ) ⊆ X an with a proper strong deformation\nretraction τ : X an → S(X ). The skeleton S(X ) carries a canonical structure of a\nmetrized graph. We note that the generic fiber of the formal scheme Û intersects S(X )\n"
        },
        {
          "filename": "source-extracts/1712.00980-test-ideals-resolution-proof.txt",
          "source_line_first": 655,
          "source_line_last": 825,
          "pdf_page_first": 13,
          "pdf_page_last": 17,
          "sha256": "450296f6bbb3c0f72719a42020d8cee1196474e703568a7a48fbce8ed7e3558e",
          "literal_text": "\f14                  W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\n     (ii) If we normalize our non-archimedean volumes by vol(L), can we find an example\n          of some model metrics k k and k k0 with irrational vol(L, k k, k k0 )? The idea is\n          to avoid the trivial example above.\n\n                               4. Asymptotic test ideals\n   We recall definitions and some basic properties from the theory of generalized and\nasymptotic test ideals developed in [BMS08, Sect. 2] and [Mus13, Sect. 3]. We refer\nto [ST12] for a more comprehensive overview of the theory of test ideals. Let X be a\nsmooth variety over a perfect field k of characteristic p > 0. Let F : X → X denote\nthe Frobenius morphism which is induced by the p-th power ring morphism on affine\nsubsets. Write\n                             ωX/k = det ΩX/k = OX (KX/k )\nfor some canonical divisor KX/k on X.\n                                                                    e\n   Let a be an ideal in OX and e ∈ N>0 . There is a unique ideal a[p ] in OX such that for\n                                      e                                     e\nevery open affine U in X the ideal a[p ] (U ) in OX (U ) is generated by {up | u ∈ a(U )}.\nWe have [BMS08, bottom of p. 44]\n                                                        e       e\n(4.1)                       a(U ) = {a ∈ OX (U ) | ap ∈ a[p ] (U )}\nWe recall the following facts from [Mus13, p. 540]: There is a canonical trace map\nTr : F∗ (ωX/k ) → ωX/k whose construction can be based on the Cartier isomorphism\n[Kat70, Thm. (7.2) and Eq. (7.2.3)]. Mustaţă gives an explicit description of the trace\nmap [Mus13, top of p. 540]. Given e ∈ N>0 there is an iterated trace map Tre : F∗e (ωX/k ) →\n                                                             e\nωX/k . For an ideal a in OX there exists a unique ideal a[1/p ] in OX with\n                                                            e\n(4.2)                        Tre (F∗e (a · ωX/k )) = a[1/p ] · ωX/k .\n                        e\nThis definition of a[1/p ] is compatible with [BMS08, Def. 2.2]. Hence we have\n                                    e \u0001[1/pe ]            e \u0001[pe ]\n(4.3)                            a[p ]         = a ⊆ a[1/p ]\nby [BMS08, Lemma 2.4(iv)].\nDefinition 4.1. [BMS08, Def. 2.9] Given an ideal a in OX and λ ∈ R≥0 one defines the\ntest ideal of a of exponent λ to be\n                                           [ \u0010     e\n                                                      \u0011[1/pe ]\n                                τ (aλ ) :=     adλp e\n                                           e∈N>0\n\nwhere given r ∈ R we write dre for the smallest integer ≥ r.\n                                                                e       e\nRemark 4.2.    (i) Observe that we have τ (aλ ) = (adλp e )[1/p ] for large e ∈ N as X is\nnoetherian. The equality\n(4.4)                                τ ((am )λ ) = τ (aλm )\nfor m ∈ N shows that the notation in Definition 4.1 is compatible with taking powers\nof ideals [BMS08, Cor. 2.15]. We have τ (aλ ) ⊆ τ (bλ ) for ideals a ⊆ b in OX [BMS08,\nProp. 2.11(i)].\n                                      e       e                                       e       e\n  (ii) Choose e such that τ (a) = (a[p ] )[1/p ] . For any ideal b in OX such that a[p ] ⊆ b[p ]\nwe get a ⊆ b from (4.1). Hence (4.3) implies\n(4.5)                                      a ⊆ τ (a).\n  Let a• be graded sequence of ideals in OX , i.e. a family (am )m∈N>0 of ideals in OX\nsuch that am · an ⊆ am+n for all m, n ∈ N>0 and am 6= (0) for some m > 0.\n\f                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             15\n\n\nDefinition 4.3. [Mus13, p. 541] Choose λ ∈ R≥0 . Define the asymptotic test ideal of\nexponent λ as                             [\n                              τ (aλ• ) :=   τ (aλ/m\n                                                m ).\n                                            m∈N\n                                            λ/m\nRemark 4.4.      (i) We have τ (aλ• ) = τ (am ) for suitable m ∈ N which are divisible\nenough [Mus13, p. 541].\n  (ii) For all m ∈ N we have [Mus13, p. 541, l. 4]\n(4.6)                                τ (am ) ⊆ τ (am\n                                                   • ).\n (iii) For all m ∈ N we have the Subadditivity Property [Mus13, Prop. 3.1(ii)]\n(4.7)                               τ (amλ        λ m\n                                        • ) ⊆ τ (a• ) .\n\nDefinition 4.5. Let D be a divisor on X with h0 (X, OX (mD)) 6= 0 for some m > 0.\nDefine the asymptotic test ideal of exponent λ ∈ R≥0 associated with X and D as\n                                   τ (λ · kDk) := τ (aλ• )\nwhere a• denotes the graded sequence of base ideals for D, i.e. am is the image of the\nnatural map\n                          H 0 (X, O(mD)) ⊗k OX (−mD) → OX .\nIf D is a Q-divisor such that h0 (X, OX (mD)) 6= 0 for some positive integer m such that\nmD is a usual divisor then we put τ (λ · kDk) := τ (λ/r · krDk) for some r ∈ N such that\nrD has integral coefficients.\n  We finish with a slight generalization of Mustaţă’s uniform generation property [Mus13,\nThm. 4.1]. Observe that in loc. cit. it is required that the variety X is projective over\nthe ground field k.\nTheorem 4.6. Let R be a k-algebra of finite type over a perfect field k of characteristic\np > 0. Let X be an integral scheme of dimension n which is projective over the spectrum\nof R and smooth over k. Let D, E, and H be divisors on X and λ ∈ Q≥0 such that\n     (i) OX (H) is an ample, globally generated line bundle,\n    (ii) h0 (X, OX (mD)) > 0 for some m > 0, and\n   (iii) the Q-divisor E − λD is nef.\nThen the sheaf OX (KX/k +E +dH)⊗OX τ (λ·kDk) is globally generated for all d ≥ n+1.\nProof. We literally follow Mustaţă’s proof with two modifications. The proof requires\nMumford’s theorem on Castelnuovo-Mumford regularity for the projective scheme X\nover R which holds also in this more general setting [BS13, 20.4.13]. Furthermore we\nreplace the use of Fujita’s vanishing theorem to the sheaves Fj := OX (KX/k + Tj ),\nj = 1, . . . , r and the ample divisor (d − i)H by an application of Keeler’s generalization\n[Kee03, Thm. 1.5].                                                                         \u0003\n\n                          5. Descent for model functions\n   Let K denote a complete discretely valued field with valuation ring K ◦ . Let R be\na discrete valuation subring of K ◦ whose completion is K ◦ . Then K is the completion\nof the field of fractions F of R. In this section we show that all model functions on\nanalytifications of varieties over K are already defined over R.\n   An R-model of a projective variety over F is defined completely analogously to the\ncomplete case treated in 2.1.\n\f16                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\nDefinition 5.1. Let X be a projective variety over K. We say that a model function\nϕ : X an → R is defined over R if there exists a projective variety Y over F , with an\nisomorphism Y ⊗F K ≃ X, an R-model Y of Y , a vertical divisor D0 on Y such that\nϕ= m 1\n       ϕD where m ∈ N>0 and D is the vertical divisor on Y ⊗R K ◦ obtained by pullback\nfrom D0 . Likewise we define the notion of a vertical ideal sheaf defined over R.\n     Here is the announced descent result.\nProposition 5.2. Let Y be a projective variety over F and let X := Y ⊗F K.\n   (a) Any K ◦ -model of X is dominated by the base change of a projective R-model of\n       Y to K ◦ .\n   (b) If a projective K ◦ -model X of X dominates Y ⊗R K ◦ for a projective R-model\n       Y of Y , then X ≃ Y 0 ⊗R K ◦ for a projective R-model Y 0 of Y dominating Y .\n   (c) Every model function on X an is defined over R.\nProof. To prove (a), we pick any projective R-model Y of Y . By [Lü93, Lemma 2.2],\nthere is a blowing up π : X 0 → Y ⊗R K ◦ such that X 0 dominates X . Since π is a\nprojective morphism, X 0 is a projective K ◦ -model dominating X . Hence (a) follows\nfrom (b).\n   To prove (b), we note that the morphism X → Y ⊗R K ◦ is a blowing up morphism\nalong a vertical closed subscheme Z of Y ⊗R K ◦ (see [Liu06, Thm. 8.1.24]). Since the\nideal sheaf of Z contains a power of the uniformizer of R, we may define it over R and\nhence the same is true for the blowing up morphism and for X proving (b).\n   To prove (c), we may assume that the model function is associated to a vertical Cartier\ndivisor D. Replacing D by D + div(λ) for a suitable non-zero λ ∈ R and using (a) and\n(b), we may assume that D is an effective Cartier divisor on a projective R-model Y of\nY . As in (b), we see that the ideal sheaf of D is defined by the ideal sheaf of a Cartier\ndivisor D0 defined over R proving (c).                                                  \u0003\n\n                            6. Resolution of singularities\n   For our applications, we need that regular projective models are cofinal in the categroy\nof models which makes it necessary to assume resolution of singularities in a certain\ndimension.\nDefinition 6.1. Let k be a field. We say that resolution of singularities holds over k\nin dimension n if for every quasi-projective variety Y over k of dimension n there exists\na regular variety Ỹ over k and a projective morphism Ỹ → Y which is an isomorphism\nover the regular locus of Y .\n  To transfer results from [BFJ16a, BFJ15] to our context, it is essential to show that\nprojective models are dominated by SNC-models. In order to this we are going to use\nthe following assumption.\nDefinition 6.2. We say that embedded resolution of singularities in dimension m holds\nover a field k if for every quasi-projective regular variety Y over k of dimension m and\nevery proper closed subset Z of Y , there is a projective morphism π : Y 0 → Y of quasi-\nprojective regular varieties over k such that the set π −1 (Z) is the support of a normal\ncrossing divisor and such that π is an isomorphism over Y \\ Z.\n   Hironaka has shown that resolution of singularities and embedded resolution of sin-\ngularities holds over a field of characteristic zero in any dimension. Resolution of singu-\nlarities holds over arbitrary fields in dimension one (Dedekind, M. Noether, Riemann)\n\f                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                            17\n\n\nand in dimension two (Abhyankar, Lipman). Cossart and Piltant have proven that res-\nolution of singularities and embedded resolution of singularities hold in dimension three\nover perfect fields.\nTheorem 6.3 (Cossart-Piltant). Resolution of singularities and embedded resolution of\nsingularities hold in dimension three over any perfect field.\nProof. This is shown in [CP09, Thm. on p. 1839] and [CP08, Prop. 4.1].                  \u0003\n\n      7. Uniform convergence to the envelope of the zero function\n   Let K be a complete discretely valued field of positive characteristic p > 0. Let X be\na smooth projective variety over K, L an ample line bundle on X, and (X , L ) a model\nof (X, L) over K ◦ . For m ∈ N>0 let am denote the m-th base ideal of L as in (2.3). For\n"
        },
        {
          "filename": "source-extracts/1712.00980-geometric-test-ideal-proof.txt",
          "source_line_first": 826,
          "source_line_last": 997,
          "pdf_page_first": 17,
          "pdf_page_last": 20,
          "sha256": "63b4f61d28f6c4b4515fb28bc4a5d891f6367963c4986d5a4d9f95eb8de5360a",
          "literal_text": "a scheme B, we recall our convention B (1) = {p ∈ B | dim OB,p = 1}.\nAssumption 7.1. There exist a normal affine variety B over a perfect field k, a codi-\nmension one point b ∈ B (1) , a projective regular integral scheme XB over B, and line\nbundles LB and AB over XB such that there exist\n     (i) a flat morphism h : Spec K ◦ → Spec OB,b → B,\n                                           ∼\n    (ii) an isomorphism XB ⊗B Spec K ◦ → X ,\n                                ∼\n   (iii) an isomorphism h∗ LB → L over the isomorphism in (ii),\n                                       ∼\n   (iv) and an isomorphism AB |XB,η → LB |XB,η where η is the generic point of B and\n         the line bundle AB on XB is ample.\nUsually we read all the isomorphisms above as identifications.\n   Note that all relevant information in Assumption 7.1 is over the discrete valuation\nring OB,b . The next remark makes this statement precise and gives an equivalent local\nway to formulate this assumption.\nRemark 7.2. Suppose that X and L are defined over a subring R of K ◦ by a line bundle\nLR on a projective regular integral scheme XR over R. We assume furthermore that\nR is a discrete valuation ring which is defined geometrically by a d-dimensional normal\n                                                                              ∼\nvariety B over a field k, i.e. there exist b ∈ B (1) and an isomorphism h : R → OB,b . We\nread the isomorphism h as an identification. Then Assumption 7.1 is equivalent to the\nexistence of data (R, k, B, b, h, XR , LR ) as above assuming furthermore that the field k\nis perfect and the restriction of LR to the generic fiber XR,η over R extends to an ample\nline bundle AR on XR .\n   One direction of the equivalence is clear by base change from B to Spec OB,b . On the\nother hand, replacing B by an open affine neighbourhood of b, it is clear by [EGAIV,\nCor. 9.6.4] that AR extends to an ample line bundle AB on a projective integral scheme\nXB over B and that LR extends to a line bundle LB on XB . Since the regular locus\nof XB is open [GW10, Cor. 12.52] and since the fiber of XB over b is contained in the\nregular locus, we may assume that XB is also regular by shrinking B again.\nTheorem 7.3. Let θ be defined by the line bundle L . If the pair (X , L ) satisfies\nAssumption 7.1, then (m−1 log |am |)m∈N>0 is a sequence of θ-psh model functions which\nconverges uniformly on X an to Pθ (0).\n   If the field K has equicharacteristic zero, this result was proven by Boucksom, Favre,\nand Jonsson [BFJ16a, Thm. 8.5] without Assumption 7.1. We will follow their strategy\nof proof replacing the use of multiplier ideals by the use of test ideals. The required\nresults about test ideals are gathered in Section 4.\n\f18                 W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\nProof. We start with the observation that we have\n(7.1)                                Γ(XB , LB⊗m ) 6= 0\nfor some m > 0. In fact we have\n                                                  ∼\n                        Γ(XB , LB⊗m ) ⊗R K −→ Γ(X, L⊗m ) 6= 0\nby flat base change and the ampleness of L for some m > 0.\n  We have a cartesian diagram\n                                        g\n                               X            / XB\n\n\n                                 \u000f            \u000f          $\n                             Spec K ◦\n                                        h   /B        / Spec k.\n\nWe observe that XB is a smooth variety over the perfect field k and write\n                  aB,m = Im H 0 (XB , LB⊗m ) ⊗k LB⊗−m → OXB\n                                                                 \u0001\n\nfor the m-th base ideal of LB . Consider the ideal g −1 (aB,m ) · OX in OX generated by\ng −1 (aB,m ). We have g −1 (aB,m ) · OX = g ∗ aB,m as g is flat. Sections of am are locally\nof the form s · t−1 where s ∈ Γ(X , L ⊗m ) is a global section and t is a local section of\nL ⊗m . Flat base change [Har77, Prop. III.9.3] gives\n                        H 0 (X , L ⊗m ) = H 0 (XB , LB⊗m ) ⊗R K ◦ .\nHence the formation of base ideals is compatible with base change, i.e. we have\n(7.2)                        am = g −1 (aB,m ) · OX = g ∗ aB,m\nfor all m ∈ N>0 .\n   The family aB,• = (aB,m )m>0 defines a graded sequence of ideals in the sense of\nSection 4. Let bB,m := τ (am\n                           B,• ) denote the associated asymptotic test ideal of exponent\nm. Motivated by (7.2) we define\n                             bm := g −1 bB,m · OX = g ∗ bB,m\nas the ideal in OX generated by bB,m . These ideals have the following properties:\n     (a) We have am ⊂ bm for all m ∈ N>0 .\n     (b) We have bml ⊂ blm for all l, m ∈ N>0 .\n     (c) There is m0 ≥ 0 such that A⊗m0 ⊗L ⊗m ⊗bm is globally generated for all m > 0.\nProperties (a) and (b) follow from the corresponding properties of aB,m and bB,m men-\ntioned in (4.5), (4.6), and (4.7) if we observe (7.2).\n   Property (c) is a consequence of the generalization of Mustaţă’s uniform generation\nproperty given in Theorem 4.6. Write LB = O(D) for some divisor D on XB and choose\na divisor H on XB such that O(H) is ample and globally generated. Fix d > dim XB\nand a canonical divisor KXB /k on the smooth k-variety XB . As AB is ample we find\nsome m0 ∈ N such that A⊗m  B\n                               0\n                                 ⊗ O(−KX/k − dH) is globally generated. Given m ∈ N>0\nwe put E := mD. Since LB satisfies (7.1), for any m ∈ N>0 we may use E := mD and\nλ := m in Theorem 4.6 to see that the sheaf\n                            O(KXB /k + dH) ⊗ LB⊗m ⊗ bB,m\nis globally generated. As a consequence, our choice of m0 implies that A⊗m\n                                                                        B\n                                                                          0\n                                                                            ⊗ LB⊗m ⊗\nbB,m is globally generated. Base change to K ◦ proves (c).\n   Now we follow the proof of [BFJ16a, Thm. 8.5]. Step 1 of loc. cit. holds not only\non quasi-monomial points of X an , but pointwise on the whole X an using Proposition\n\f                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             19\n\n\n2.10 and our different definition of Pθ (0). Then Step 2 of loc. cit. works in our setting\nusing properties (a), (b), and (c) above. The only difference is that all inequalities hold\nimmediately on X an and not only on the quasi-monomial points of X an .                  \u0003\nCorollary 7.4. Let X be a smooth n-dimensional projective variety over K with a\nclosed (1, 1)-form θ. Let L be a line bundle on a K ◦ -model X of X defining θ and\nwith L = L |X ample. We assume that (X , L ) is the base change of (XR , LR ) for a\nline bundle LR of a projective integral scheme XR over a subring R of K ◦ and that R\nis a discrete valuation ring defined geometrically by a d-dimensional normal variety B\nover a perfect field k (as in Remark 7.2). If resolution of singularities holds over k in\ndimension d + n, then Pθ (0) is a uniform limit of θ-psh model functions and hence Pθ (0)\nis continuous on X an .\nProof. It follows from our assumptions that X is base change of the generic fiber XR,η\nof XR /R to K. Since X is smooth, we conclude that XR,η is smooth as well [EGAIV,\nCor. 17.7.3]. By Proposition 2.9(vii), it is enough to prove the claim for any positive\nmultiple of θ. Using this and Lemma 7.5 below, we see that by passing to dominant\nmodels, we may assume that XR is regular and that the restriction of LR to XR,η\nextends to an ample line bundle on XR . By Remark 7.2, these conditions are equivalent\nto Assumption 7.1 and hence the claim follows from Theorem 7.3.                      \u0003\nLemma 7.5. Let R be a discrete valuation ring which is defined geometrically by a d-\ndimensional normal variety B over the field k (as in Remark 7.2). Let XR be a projective\nintegral scheme over R with n-dimensional regular generic fiber X 0 := XR,η . We assume\nthat resolution of singularities holds over k in dimension d + n. Then for any ample\nline bundle L0 on X 0 , there exists m ∈ N>0 and an ample extension LR0 of (L0 )⊗m to a\nregular R-model XR0 of X 0 with a projective morphism XR0 → XR over R extending the\nidentity on X 0 .\nProof. The proof proceeds in three steps. First, we use a result of Lütkebohmert about\nvertical blowing ups to show that L0 may be assumed to extend to an ample line bundle\nH on XR . In a second step, we show that XR may be also assumed to be semi-factorial\nby a theorem of Pépin. In a third step, we use resolution of singularities to construct\nour desired regular model XR0 .\n    Step 1: Replacing L0 by a positive tensor power, we may assume that L0 has an ample\nextension HR to a projective R-model YR . There is a blow up π : ZR → YR in an ideal\nsheaf J supported in the special fiber of YR such that the identity on X 0 extends to a\nmorphism ZR → XR [Lü93, Lemma 2.2]. Then π −1 (J ) = OZR /YR (1) and hence there\nis ` ∈ N>0 such that π ∗ (H ⊗` ) ⊗ OZR /YR (1) is ample [Har77, Prop. II.7.10]. We conclude\nthat by replacing XR by ZR and by passing to a positive tensor power of L0 , we may\nassume that L0 has an ample extension HR to XR . This completes the first step.\n    Step 2: By a result of Pépin [Pé13, Thm. 3.1], there is a a blowing-up morphism\nπ : ZR0 → XR centered in the special fiber of XR such that ZR0 is semi-factorial. The\n  0\n\nlatter means that every line bundle on the generic fiber ZR,η0   of ZR0 over R extends to a\nline bundle on ZR0 . Similarly as in the first step, we may assume that a positive tensor\npower of L0 extends to an ample line bundle on ZR0 . Replacing XR by ZR0 and L0 by\nthis positive tensor power, we get the second step.\n    Step 3: We may assume that B is affine. Using R = OB,b for some b ∈ B (1) , it is\nclear that XR extends to a projective integral scheme XB over B. By using resolution\nof singularities over k in dimension d + n, there is a regular integral scheme XB0 and a\nprojective morphism ϕB : XB0 → XB which is an isomorphism over the regular locus of\n\f20                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\nXB . Since X 0 is contained in the regular locus of XB , we conclude that ϕB maps the\ngeneric fiber XB,η\n                0  of XB0 over B isomorphically onto X 0 = XB,η . As usual, we read this\nisomorphism as an identification. Then we get an induced projective morphism\n                           ϕR : XR0 := XB0 ×B Spec(R) −→ XR\nextending the identity on X 0 . The same argument as in the first step gives m ∈ N>0\nsuch that\n                           LR0 := ϕ∗R (HR⊗m ) ⊗ OXR0 /XR (1)\nis an ample line bundle on XR0 . Let F be the restriction of OXR0 /XR (1) to XR,η\n                                                                              0 =X\n                                                                                   R,η =\nX . Then LR is a model of (L )\n   0          0                 0 ⊗m ⊗ F . To prove the lemma, we have to ensure that F\nmay be assumed to be OX 0 . To do so, we use that XR is semi-factorial to extend F to\na line bundle FB on XR . Then we may replace OXR0 /XR (1) by OXR0 /XR (1) ⊗ ϕ∗R (F −1 )\nto deduce the claim.                                                                   \u0003\n\n                           8. Continuity of the envelope\n   We present consequences of our application of test ideals in the last subsection under\nthe assumption that we have resolution of singularities. As in Section 7 let K be a\ncomplete discretely valued field of positive characteristic p > 0. Let X be a smooth\n"
        },
        {
          "filename": "source-extracts/1712.00980-envelope-and-equation-proof.txt",
          "source_line_first": 998,
          "source_line_last": 1197,
          "pdf_page_first": 20,
          "pdf_page_last": 24,
          "sha256": "79b90ed310d6e18679a7706844c72ec469d606c3398f347018f5f129c0bf5ec8",
          "literal_text": "projective variety over K of dimension n. Consider θ ∈ Z 1,1 (X) with ample de Rham\nclass {θ} ∈ N 1 (X).\nDefinition 8.1. We say that X is of geometric origin from a d-dimensional family over\na field k if there exist a normal d-dimensional variety B over k, a point b ∈ B (1) of\ncodimension one and a projective variety Y over K 0 = k(B) such that\n                                               ∼\n      (i) there exists an isomorphism O  bB,b →  K ◦ of rings where ObB,b denotes the com-\n          pletion of the discrete valuation ring R := OB,b ,\n     (ii) an isomorphism Y ⊗K 0 K ≃ X over K with K 0 → K induced by (i).\nUsually, we read these isomorphisms as identifications. Moreover, if L is a line bundle\n(resp. if θ is a closed (1, 1)-form) on X, we say that (X, L) (resp. (X, θ)) is of geometric\norigin from a d-dimensional family over a field k if the above conditions are satisfied and\nif we can also find a line bundle L0 on Y inducing L by the base change K/K 0 (resp. a\nline bundle LR on an R-model XR of Y inducing θ by the base change K ◦ /R).\n     We can now formulate our main result about the continuity of the envelope:\nTheorem 8.2. Let X be a smooth n-dimensional projective variety over K of geometric\norigin from a d-dimensional family over a perfect field k. Assume that resolution of\nsingularities holds over k in dimension d + n. If θ is a closed (1, 1)-form on X with\nample de Rham class {θ} and if u ∈ C 0 (X an ), then Pθ (u) is a uniform limit of θ-psh\nmodel functions and thus Pθ (u) is continuous on X an .\n  Using resolution of singularities in dimension three over a perfect field proven by\nCossart–Piltant (see Theorem 6.3), we get the following application:\nCorollary 8.3. Let X be a smooth projective surface over K of geometric origin from\na 1-dimensional family over a perfect field k. Then the conclusion of Theorem 8.2 holds\nunconditionally.\n   We will prove Theorem 8.2 in several steps. First, we prove it in a completely geometric\nsituation:\n\f                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             21\n\n\nLemma 8.4. If we assume additionally that (X, θ) is of geometric origin from a d-\ndimensional family over a perfect field k, then Theorem 8.2 holds.\nProof. Recall that the space of model functions D(X) is dense in C 0 (X an ) for the topol-\nogy of uniform convergence [Gub98, Thm. 7.12]. Hence we may assume that u ∈ D(X)\nby Proposition 2.9(v). Observe that by Proposition 2.9(vii), we may replace (θ, u) by\na suitable multiple. Hence we may assume without loss of generality that the model\nfunction u is defined by a vertical divisor on a K ◦ -model X 0 . It is clear that we can\nchoose X 0 dominating the geometric model X = XR ⊗R K ◦ of θ from Definition 8.1. It\nfollows from Proposition 5.2(a) that we may assume X = X 0 . By Proposition 2.9(iv)\nwe get\n(8.1)                            Pθ (u) = Pθ+ddc u (0) + u.\nBy construction, the class θ+ddc u is induced by a line bundle on X  R and hence Corollary\n                                                          c\n7.4 yields that Pθ+ddc u (0) is a uniform limit of (θ + dd u)-psh model functions ϕi . Then\nPθ (u) is the uniform limit of the sequence of θ-psh functions ϕi + u by (8.1).          \u0003\n  In the lemma above we have proven Theorem 8.2 under the additional assumption that\nthe (1, 1)-form θ is defined geometrically. In the next lemma, we relax this assumption\na bit only assuming that the de Rham class of θ is defined geometrically.\nLemma 8.5. If we assume additionally that the de Rham class {θ} is induced by an\nample line bundle L on X such that (X, L) is of geometric origin from a d-dimensional\nfamily over the perfect field k, then Theorem 8.2 holds.\nProof. By Proposition 2.9(vi), we may assume that θ ∈ Z 1,1 (X)Q . By Proposition\n2.9(vii), we may replace L by a positive tensor power and θ by the corresponding multiple,\nand so we may assume that L is very ample. In the notation of Definition 8.1, the\nassumption that (X, L) is of geometric origin means that L is the pull-back of a line\nbundle L0 on the projective variety Y over K 0 = k(B). It follows easily from [Har77,\nProp. III.9.3] and [EGAIV, Prop. 2.7.1(xii)] that L0 is very ample. Then L0 extends to\na very ample line bundle on a projective R-model of Y for the discrete valuation ring\nR = OB,b from Definition 8.1. By base change to K ◦ , we conclude that there is a closed\n(1, 1)-form θ0 on X an with de Rham class {θ0 } = {θ} such that (X, θ0 ) is of geometric\norigin from a d-dimensional family over k.\n   By the ddc -lemma in [BFJ16a, Thm. 4.3] (see also the second author’s thesis [Jel16,\nThm. 4.2.7] for generalizations) and using the rationality assumption on θ from the\nbeginning of the proof, there is v ∈ D(X) such that θ0 = θ + ddc v. It follows from\nProposition 2.9(iv) that\n                        Pθ (u) − v = Pθ+ddc v (u − v) = Pθ0 (u − v).\nBy Lemma 8.4, the function Pθ0 (u − v) is a uniform limit of θ0 -psh functions. Adding v,\nwe get the claim for Pθ (u).                                                           \u0003\n   To prove Theorem 8.2 in full generality, the idea is to reduce to the above geometric\nsituation by a similar trick as in [BFJ15, Appendix A].\nProof of Theorem 8.2. We note first that by Proposition 2.9 (viii) the property that\nPθ (u) is a uniform limit of θ-psh model functions is equivalent to the property that\nit is a continuous function. Let K 0 /K be a finite normal extension and denote by\nq : X 0 := X ⊗K K 0 → X the natural projection. Let θ0 = q ∗ θ ∈ Z 1,1 (X 0 ). Then by\nLemma 2.11 we have that\n                                  q ∗ Pθ (u) = Pθ0 (q ∗ u).\n\f22                  W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\nIt follows from [Ber90, Prop. 1.3.5] that X an is as a topological space equal to the quotient\nof (X 0 )an by the automorphism group of K 0 /K. We conclude that Pθ (u) is continuous\nif and only if Pθ0 (q ∗ u) is continuous.\n   Hence we can replace K by a finite normal extension. Adapting the same argument as\nin [BFJ15, Lemma A.7] to characteristic p, there exists a finite normal extension K 0 /K\nand a function field F of transcendence degree d over k with K 0 as completion as in\nDefiniton 8.1 such that X 0 := X ⊗K K 0 is the base change of a projective variety Y over\nF with N 1 (Y /F )Q → N 1 (X 0 /K 0 )Q surjective. Replacing K 0 by K, we can assume that\nthere is Y as above with a surjective map\n(8.2)                            N 1 (Y /F )Q → N 1 (X/K)Q\ninduced by the natural projection X → Y . To prove continuity of Pθ (u), we may assume\nthat the de Rham class {θ} is in N 1 (X)Q by using an approximation argument based\non Proposition 2.9(vi). We conclude from surjectivity in (8.2) that there is a non-zero\nm ∈ N such that {mθ} is induced by a line bundle L with (X, L) of geometric origin\nfrom a d-dimensional family over k (in fact from Y ). By Proposition 2.9(vii), we have\n         1\nPθ (u) = m Pmθ (mu) and hence continuity follows from Lemma 8.5.                     \u0003\n\n                          9. The Monge–Ampère equation\n   Let K be a field endowed with a complete discrete absolute value. Boucksom, Favre,\nand Jonsson have shown in [BFJ16a, BFJ15] that the Monge–Ampère equation for a\nRadon measure supported on the skeleton of a smooth projective variety over K has a\nsolution if the variety is of geometric origin from a one-dimensional family over a field of\ncharacteristic zero. In this section, we will explain that the same is true in characteristic\np > 0 if we assume resolution of singularities (see Section 6 for precise definitions).\n   In the following, we work under the following assumptions:\n   (A1) The n-dimensional smooth projective variety X over K is of geometric origin\n         from a d-dimensional family over a perfect field k of characteristic p > 0.\n   (A2) Resolution of singularities holds over k in dimension d + n.\n   (A3) Embedded resolution of singularities holds over k in dimension d + n.\n   Note that assumptions (A2) and (A3) are unconditional for n = 2 and d = 1 by\nTheorem 6.3 of Cossart and Piltant. For the following, it is crucial to have in mind that\nmodels of X can be defined geometrically which follows from Proposition 5.2.\n   To transfer the results from [BFJ16a, BFJ15], it is essential to note that every pro-\njective K ◦ -model of X is dominated by a projective SNC-model of X. To see this, we\nnote first that we may assume that the given K ◦ -model is of geometric origin over the\nperfect field k by Proposition 5.2. Using resolution of singularities in dimension d + n\nsimilarly as in the third step of the proof of Lemma 7.5, we deduce that there is a\nregular projective scheme XR over R as in Definition 8.1 dominating the given model.\nApplying in the same way embedded resolution of singularities in dimension d + n to the\nnon-smooth fibers of XR over R, we may assume that the singular fibers of XR have\nthe same support as a strict normal crossing divisor. Then base change to K ◦ yields the\nclaim as base change of the discrete valuation ring OB,b to its completion K ◦ preserves\nregularity [Sta17, Tag 0BG4] and strict normal crossing support.\n   Having sufficiently many projective SNC-models of X at hand, the density results of\nskeletons in X an given in [BFJ16a, Sect. 3] also hold in our case of equicharacteristic p.\nGiven a closed (1, 1)-form θ with ample de Rham class {θ}, the notion of θ-psh functions\non X an introduced in [BFJ16a, Sect. 7] keeps the same properties in our case. In fact,\nthe results of [BFJ16a, Sect. 1–7] and their proofs carry over to our setting.\n\f                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                23\n\n\n   Note that we have already proven the continuity of the θ-psh envelope in Theorem 8.2,\nwhich is the analogue of [BFJ16a, Thm. 8.3], by using test ideals instead of multiplier\nideals. For u ∈ C 0 (X an ), we recall from 2.8 that we have used a different definition of the\nθ-psh envelope Pθ (u) than in [BFJ16a, Def. 8.1]. Both definitions agree in the equichar-\nacteristic zero situation by [BFJ16a, Thm. 8.3 and Lemma 8.9]. If the characteristic of\nK is positive and the Assumptions (A1)–(A3) hold then we have explained above how to\ndefine θ-psh functions. We claim now that in this case both definitions of the envelope\nagree as well. Indeed, it follows from [BFJ16a, Lemma 8.4] that the definitions agree on\nquasi-monomial points of X an . For any x ∈ X an , we consider the net pX (x) with X\nranging over all SNC models of X. By [BFJ16a, Cor. 3.9], this net of quasi-monomial\npoints converges to x. It follows from continuity that the net Pθ (u)(pX (x)) converges\nto Pθ (u)(x) for our definition of the envelope. By [BFJ16a, Thm. 7.11, Prop. 8.2(i)], the\nsame convergence holds for their envelope and hence both definitions agree.\n   This yields now in the same way as in [BFJ16a, Thm. 8.7] that the following monotone\nregularization holds:\nCorollary 9.1. Under the assumptions (A1)–(A3), let θ be a closed (1, 1)-form on X an\nwith ample de Rham class. Then every θ-psh function on X an is the pointwise limit of a\ndecreasing net of θ-psh model functions on X an .\n   In [BFJ15, Sect. 3], the monotone regularization is the basic ingredient to generalize\nthe Monge–Ampère operator from θ-psh model functions to bounded θ-psh functions and\nhence it applies also to our setting leading to the same results as in [BFJ15, Sect. 3]. For\na bounded θ-psh function ϕ, we denote by MAθ (ϕ) the associated Monge-Ampère mea-\nsure on X an . The definitions, results and arguments from [BFJ15, Sect. 4–6] carry over\nwithout change. In particular, we may choose a decreasing sequence of θ-psh model func-\ntions on X an in the monotone regularization from Corollary 9.1 similarly as in [BFJ15,\nProp. 4.7].\n   A crucial step is now to prove the following orthogonality property:\nTheorem 9.2. Under the assumptions (A1)–(A3), let θ be a closed (1, 1)-form on X an\nwith ample de Rham class. Then for every continuous function f on X an with θ-psh\nenvelope Pθ (f ), we have the orthogonality property\n                            Z\n                                 (f − Pθ (f ))MAθ (Pθ (f )) = 0.\n                              X an\nProof. By Proposition 2.9(vi) and the continuity of the Monge–Ampère measure given\nin [BFJ15, Thm. 3.1], we may assume that θ ∈ Z 1,1 (X)Q . Using Proposition 2.9(vii), we\nmay assume that θ is induced by a line bundle of a model of X. Then the claim follows\nfrom [BGJKM16, Thm. 6.3.2] as Pθ (f ) is continuous by Theorem 8.2.                    \u0003\n   As a consequence of the orthogonality property, we get differentiability of E ◦ Pθ as\nin [BFJ15, Thm. 7.2] where E is the energy from [BFJ15, Sect. 6]. We have now all\ningredients available to solve the following Monge–Ampère equation.\nTheorem 9.3. Under the assumptions (A1)–(A3), let θ be a closed (1, 1)-form on X an\nwith ample de Rham class {θ} and let µ be a positive Radon measure on X an of mass\n{θ}n supported on the skeleton of a projective SNC-model. Then there is a continuous\nθ-psh function ϕ on X an such that MAθ (ϕ) = µ and ϕ is unique up to additive constants.\nProof. It was shown in [BFJ15, §8.1] that uniqueness follows from a result of Yuan and\nZhang in [YZ17]. To prove existence of a θ-psh solution ϕ, we use the variational method\nof Boucksom, Favre, and Jonsson. The basic tools needed here are upper semicontinuity\n\f24                  W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN\n\n\nof the energy [BFJ15, Prop. 6.2], the compactness theorem [BFJ16a, Thm. 7.10], and\nthe differentiability of E ◦ Pθ . As explained above, all these results are available in our\nsetting. It remains to see that ϕ is continuous and this is done by estimates in the spirit\nof Kolodziej as in [BFJ15, §8.3].                                                         \u0003\n\n        Appendix A. The skeleton and the retraction in the toric case\n               by José Ignacio Burgos Gil and Martín Sombra\n   In this appendix we give a combinatorial description of the skeleton associated to a\ntoric model of a toric variety, and of the corresponding retraction. We will use this\ndescription to show an example of two models of the same variety that have the same\nskeleton but different retractions. In turn this will give a counterexample to a higher\ndimensional extension of Proposition 3.8.\n   Let (K, | |) be a complete non-archimedean discretely valued field, K ◦ the valuation\nring, k the residue field, and S = Spec(K ◦ ). Let $ be a uniformizer of K ◦ and write\n                                      λK = − log |$|.\n   Let X be a smooth projective variety over K of dimension n and X an the associated\nBerkovich analytic space. Let X be an SNC model of X over S, that is an SNC projective\nscheme X over S with generic fiber X such that the special fiber, which is not assumed\nto be reduced, agrees as a closed subset with a simple normal crossing divisor D of X . To\n"
        },
        {
          "filename": "source-extracts/1712.00980-appendix-obstruction.txt",
          "source_line_first": 1198,
          "source_line_last": 1250,
          "pdf_page_first": 24,
          "pdf_page_last": 25,
          "sha256": "31d8bf51c913924aae33c7b20a9d2e12a1c8b051c979cb18aa21ff50a219b445",
          "literal_text": "the model X we can associate a skeleton ∆X ⊂ X an and a retraction pX : X an → ∆X ,\nsee [BFJ16a, §3] for details.\n   Let L be an ample line bundle on X and L a nef model of L on X . Let θ be the\nsemipositive (1, 1)-form in the class of L corresponding to the model L . Let µ be a\npositive Radon measure on X an with support in ∆X such that µ(X an ) = degL (X). The\nMonge-Ampère equation looks for a θ-psh function ϕ on X an such that\n(A.1)                                (ddc ϕ + θ)∧n = µ.\nWith the generality we are discussing in this paragraph, there is not yet a definition of\nthe class of θ-psh functions with all the properties of classical pluripotential theory, but\nevery good definition of this class should include the class of θ-psh model functions as\nintroduced in 2.5.\n   The following question is natural and in case of being true would be of great help to\nsolve the Monge-Ampère equation in positive and mixed characteristic.\nQuestion 1. With the previous hypotheses, is it true that any solution ϕ to the Monge-\nAmpère equation (A.1) satisfies\n(A.2)                                      ϕ = ϕ ◦ pX ?\n   We will see that this question has a negative answer by exhibiting a counterexample in\nthe context of toric varieties. In fact, that this question has a negative answer is related\nwith Proposition 3.8 not being true in higher dimension. To this aim, we will consider a\nsmooth projective variety X of dimension 2 and two models X and X 0 that have the\nsame skeleton\n                                      ∆ = ∆X = ∆X 0\nbut with different retractions pX 6= pX 0 . We will fix a semipositive (1, 1)-form θ that is\nrealized in both models and construct two model functions ϕ and ϕ0 on X an satisfying\n(A.3)                          ϕ 6= ϕ0 ,       ϕ |∆ = ϕ0 |∆ ,\n(A.4)                          ϕ = ϕ ◦ pX , ϕ0 = ϕ0 ◦ pX 0 .\n\f                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             25\n\n\nAs a consequence of these properties, we deduce that ϕ = ϕ0 ◦ pX and that ϕ0 = ϕ ◦ pX 0 .\nMoreover ϕ0 will be a θ-psh model function while the model function ϕ will not be θ-psh.\nLet µ := (ddc ϕ0 + θ)∧2 . This is a positive measure with support on ∆ and ϕ0 is a solution\nof the corresponding Monge-Ampère equation. Since\n                                    ϕ0 6= ϕ = ϕ0 ◦ pX ,\nwe see that ϕ0 is a counterexample to Question 1 for the model X . Moreover, if Propo-\nsition 3.8 were true in dimension 2, then ϕ = ϕ0 ◦ pX would be a θ-psh model function,\nbut it is not.\n   We place ourselves in the framework and notation of [BPS14]. The results below will\nmake explicit the skeleton and the retraction associated to a toric SNC model of a toric\nvariety.\n   Let T ≃ Gnm be a split torus over K. We denote by\n                        M = Hom(T, Gm ),         N = Hom(Gm , T),\nthe lattices of characters and one-parameter subgroups of T. Then M = N ∨ . We also\ndenote NR = N ⊗ R and MR = M ⊗ R. The pairing between u ∈ NR and x ∈ MR is\ndenoted by hx, ui.\n  Let now X be a proper toric variety over K and X a proper toric model of X over\nS. Then X is described by a complete fan Σ in NR and X is described by a complete\nSCR-polyhedral complex Π in NR whose recession fan satisfies rec(Π) = Σ [BPS14,\nThm. 3.5.4].\n  There is a map ζK : NR → Tan that sends u ∈ NR to the seminorm on K[M ] given by\n                            X\n                                 αm χm = max |αm |e−λK hm,ui .\n                                             m\n"
        }
      ],
      "pdfinfo_returncode": 0
    }
  ]
}


## Literal published source 1201.0187: source-extracts/1201.0187-standing-and-main.txt

singular semipositive metrics with the set PSH(X, θ) of θ-psh functions. The latter are upper
semicontinuous (usc) functions ϕ : X → [−∞, +∞) such that θ + ddc ϕ is a positive closed
(1, 1)-current. Modulo scaling, PSH(X, θ), endowed with the L1 -topology, is homeomorphic
to the space of closed positive (1, 1)-currents lying in the cohomology class c1 (L) (with its
weak topology), and hence is compact.
   Let us now turn to the non-Archimedean case. Fix a complete, discrete valuation field K
with valuation ring R and residue field k, and set S := Spec R. We assume that k (and hence
K) has characteristic zero, which means, concretely, that R is (non-uniquely) isomorphic to
k[[t]]. Let X be a smooth projective K-analytic space in the sense of Berkovich, so that X
is the analytification of a smooth projective K-variety by the GAGA principle. Recall that
the underlying topological space of X is compact Hausdorff. A model X of X is a normal
flat projective S-scheme together with an isomorphism of the analytification of its generic
fiber XK with X. Each line bundle L on X is (again, by GAGA) the analytification of a line
    1In fact, [CLD12] was posted after the first version of the present paper.
             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                        3


bundle on XK (that we also denote by L), and a model metric is a metric k · kL on L that
is naturally induced by the choice of a Q-line bundle L ∈ Pic(X )Q such that L|XK = L in
Pic(XK )Q . A model function ϕ on X is a function such that e−ϕ is a model metric on the
trivial line bundle. The set D(X) of model functions is then dense in C 0 (X), a well-known
consequence of the Stone-Weierstrass theorem.
   Following S.-W.Zhang [Zha95, 3.1] (see also [KT, 6.2.1], [Gub98, 7.13], [CL06, 2.2]), we
shall say that a model metric k · kL on L is semipositive if L ∈ Pic(X )Q is nef on the special
fiber X0 of X , i.e. L · C ≥ 0 for all projective curves C in X0 . A continuous metric on L is
then semipositive in the sense of Zhang if it can be written as a uniform limit over X of a
sequence of semipositive model metrics. The reader may consult [CL11] for a nice survey
on these notions.
   In order to define a general notion of singular semipositive metrics, we use the finer
description of X as an inverse limit of dual complexes (called skeletons in Berkovich’s termi-
nology). Since the residue field k of R has characteristic zero, it follows from [Tem06] that
each model of X is dominated by a SNC model X , by which we understand a regular model
whose special fiber X0 has simple normal crossing support (plus a harmless irreducibility
condition that we impose for convenience). To each SNC model X corresponds its dual
complex ∆X , a compact simplicial complex which encodes the incidence properties of the
irreducible components of X0 . The dual complex ∆X embeds canonically in X and for the
purposes of this introduction we shall view ∆X as a compact subset of X. There is further-
more a retraction pX : X → ∆X . These maps are compatible with respect to domination of
models, and we thus get a map
                                         X → lim ∆X
                                               ←−
                                               X
which is known to be a homeomorphism (see, for instance, [KS06, p.77, Theorem 10]).
   Following the philosophy of [BGS95], we define the space of closed (1, 1)-forms on X as
the direct limit over all models X of X of the spaces N 1 (X /S) of codimension one numerical
equivalence classes. Any model metric gives rise to a curvature form lying in this space.
The main reason for working with numerical equivalence (instead of rational equivalence
as in [BGS95]) is that we can then adapt a result of [Kün96] to show that a line bundle
L ∈ Pic(X) has vanishing first Chern class c1 (L) ∈ N 1 (X) iff it admits a model metric with
zero curvature (cf. Corollary 4.4).
   Fix a reference model metric k · k on L with curvature form θ. Any other metric can be
written k · ke−ϕ for some function ϕ on X. When k · ke−ϕ is a semipositive model metric,
we say that the model function ϕ is θ-psh.
Definition. Let L be an ample line bundle on a smooth projective K-analytic variety X.
Fix a model metric k · k on L with curvature form θ. A θ-plurisubharmonic function on X
is then a function ϕ : X → [−∞, +∞) such that:
      • ϕ is upper semicontinuous (usc).
      • ϕ ≤ ϕ ◦ pX for each SNC model X .
      • ϕ is a uniform limit, on each dual complex ∆X , of θ-psh model functions.
A singular semipositive metric is a metric k · ke−ϕ with ϕ a θ-psh function.
  The consistency of the definition for model functions will be guaranteed by Theorem 5.11
below. Let ϕ be a θ-psh function. Since ϕ is usc and each ϕ ◦ pX is continuous, it follows
4              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


immediately that S ϕ = inf X ϕ ◦ pX , so that ϕ is uniquely determined by its restriction to
the dense subset X ∆X of X. We may therefore endow the set PSH(X, θ) of all θ-psh
functions (or, equivalently, of all singular semipositive metrics on L) with the topology
of uniform convergence on dual complexes. We view this topology as an analogue of the
L1 -topology in the complex case. Our first main theorem shows that this space is indeed
compact modulo additive constants, something that was also announced in the unpublished
manuscript by Kontsevich and Tschinkel [KT].
Theorem A. Let L be an ample line bundle on a smooth projective K-analytic variety X
endowed with a model metric with curvature form θ. Then PSH(X, θ)/R is compact.
  In other words, the set of singular semipositive metrics on L modulo scaling is compact.
For curves, this result is a consequence of the work of Thuillier [Thu05], and follows from
basic properties of subharmonic functions on metrized graphs.
  Our second main result is the following analogue of Demailly’s global regularization the-
orem.
Theorem B. Let L be an ample line bundle on a smooth projective K-analytic variety X
endowed with a model metric with curvature form θ. Then every θ-psh function ϕ is the
pointwise limit on X of a decreasing net of θ-psh model functions.
   When dim X = 1, Theorem B is a special case of [Thu05, Théorème 3.4.19]. Thanks
to Dini’s lemma, Theorem B implies a non-Archimedean version of the Demailly-Richberg
theorem, stating that every continuous θ-psh function is a uniform limit over X of θ-psh
model functions. In other words, for continuous metrics our definition of semipositivity
agrees with Zhang’s.
   Let us briefly explain how Theorem A above is proved. The first important fact is that
any dual complex ∆X comes equipped with a natural affine structure [KS06] such that any
θ-psh function is convex on the faces of ∆X . On this complex we put any euclidean metric
compatible with the affine structure. The statement that we actually prove, and which
implies Theorem A, is
Theorem C. For each dual complex ∆X there exists a constant C > 0, such that ϕ|∆X is
Lipschitz continuous with Lipschitz constant at most C for any θ-psh model function ϕ.
   This result is proved in two steps. Assuming, as we may, that sup∆X ϕ = 0, we first bound
ϕ from below on the vertices of ∆X . This is done by exploiting the non-negativity of certain
intersection numbers, a direct consequence of the model metric k · ke−ϕ being determined
by a nef line bundle on some model.
   The next step is to prove the uniform Lipschitz bound. Here again, the general idea
is to exploit the non-negativity of certain intersection numbers, but the argument is more
subtle than in the first step. This time, the intersection numbers are computed on (possibly
singular) blowups of X corresponding to carefully chosen combinatorial decompositions of
∆X , in the spirit of the toroidal constructions of [KKMS]. In [BFJ12b] we adapt these
techniques to prove a uniform version of Izumi’s theorem [Izu85].
  The proof of Theorem B is of a different nature. Using Theorem A, we first show that the
usc upper envelope of any family of θ-psh functions remains θ-psh, a basic property of θ-psh
functions in the complex case. As a consequence, given any continuous function u ∈ C 0 (X)
               SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                              5


the set of all θ-psh functions ψ such that ψ ≤ u on X admits a largest element, called the
θ-psh envelope of u and denoted by Pθ (u). On the other hand, by density of D(X) in C 0 (X),
we may write any given function ϕ ∈ PSH(X, θ) as the pointwise limit of a decreasing family
of (a priori not θ-psh) model functions uj , using only the upper semicontinuity of ϕ. It is not
difficult to see that Pθ (uj ) decreases to ϕ, and we are thus reduced to showing that the θ-psh
envelope of any model function is the uniform limit of a sequence of θ-psh model functions.
This is proved using multiplier ideals, in the spirit of [DEL00, ELS03, BFJ08]. The required
properties of multiplier ideals are shown to hold on regular models in Appendix B, the key
point being to show that the expected version of the Kodaira vanishing theorem holds in
this context.2
   Let us comment on our assumptions on the field K. It is expected that pluripotential
theory can be developed on Berkovich spaces over arbitrary non-Archimedean fields, and
as we mentioned before the first steps in that direction have been taken in [CLD12] (see
also [Gub13] for a nice account on these developments), where the notions of positive forms
and currents are introduced, partially building upon ideas by Lagerberg [Lag12].
   Our approach is geometric, and we restrict our attention to the discretely valued case
in order to avoid the use of formal models over non-noetherian rings. We refer to [Gub98,
Gub03] for related works on semipositive metrics in the general setting of a complete non-
Archimedean field. More importantly, Appendix B relies on the discreteness assumption.
   Furthermore, we use the assumption that K has residue characteristic zero in two ways,
through the existence of SNC models and through the cohomology vanishing properties of
multiplier ideals. In positive residue characteristic, the existence of SNC models is not known
and it is much harder to construct retractions of X onto suitable complexes (embedded or
not). We refer to Berkovich [Ber99], Hrushovski-Loeser [HL10], and Thuillier [Thu11] for
important contributions to the understanding of this problem.
   The paper is organized as follows. The first two sections present the necessary back-


## Literal published source 1201.0187: source-extracts/1201.0187-positivity.txt

Lemma 1.2. Assume that L ∈ Pic(X ) is nef on X0 , i.e. L · C ≥ 0 for all k-proper curves
C in X0 . Then L is also nef on XK , i.e. L · C ≥ 0 for all K-proper curves C in XK as well.
  We will then simply say that L is nef. A curve is by definition reduced and irreducible.
Proof. Let C be K-proper curve in XK and let C be its closure in X equipped with its
reduced structure. By [Har, Proposition III.9.7], C is flat over S. The degrees of L|C on the
generic fiber and on the special fiber therefore coincide, which reads L · C = L · C0 . Now C0
is an effective linear combination of vertical curves, and the result follows.              
  We recall the following standard notions.
Definition 1.3. Let X be a normal projective S-variety.
   (i) The space N 1 (X /S) of codimension 1 numerical classes is defined as the quotient
       of Pic(X )R by the subspace spanned by numerically trivial line bundles, i.e. those
       L ∈ Pic(X ) such that L · C = 0 for all projective curves contained in a fiber of
       X → S.
  (ii) The nef cone Nef(X /S) ⊂ N 1 (X /S) is defined as the set of numerical classes α ∈
       N 1 (X /S) such that α · C ≥ 0 for all projective curves contained in a fiber of X → S.
   Note that the R-vector space N 1 (X /S) is finite dimensional. Indeed Lemma 1.2 shows
that the restriction map N 1 (X /S) → N 1 (X0 /k) is injective, and the latter space is finite
dimensional since X0 is projective over k. Observe also that Nef(X /S) is a closed convex
cone of N 1 (X /S). Lemma 1.2 implies that Nef(X /S) = Nef(X0 /k) ∩ N 1 (X /S) under the
injection N 1 (X /S) → N 1 (X0 /k).
   We have the following standard fact:
Lemma 1.4. Let π : X 0 → X be a vertical blowup.
   (i) There exists a π-ample divisor A ∈ Div0 (X 0 ).
  (ii) If L ∈ Pic(X ) is ample then there exists m ∈ N such that π ∗ (mL|XK ) extends to an
       ample line bundle L0 on X 0 .
Proof. By definition, there exists a vertical ideal sheaf a on X such that π is obtained as the
blowup of X along a. The universal property of blowups yields a π-ample Cartier divisor A
on X 0 such that a · OX 0 = OX 0 (A), and A is also vertical since a is, which proves (i). If L is
ample on X then mπ ∗ L + A is ample on X 0 for m  1, and (ii) follows.                         
   Recall that an R-line bundle on X (resp. XK ) is ample if it can be written as a positive
linear combination of ample line bundles.
Corollary 1.5. If L ∈ Pic(XK )R is ample, then L extends to an ample R-line bundle
L0 ∈ Pic(X 0 )R for all sufficiently high vertical blowups X 0 → X .
                    P
Proof. Write L = i ci Li where ci ∈ R>0 and Li ∈ Pic(XK ) is ample for all i. We may
assume that Li is very ample for each i, so that the linear system |Li | embeds X into a
suitable projective space PrKi over K. Let Xi be the normalization of the closure of XK in
PrSi and Li the restriction of O(1) to Xi . Let X 0 be any normal S-variety dominating X as well
8               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


as all the Xi , and write πi : X 0 → Xi for the associated vertical blowups. By Lemma 1.4 (ii)
we can find mi ∈ N and ample line bundles L0i on X 0 such that L0i |XK0 = πi∗ (mi Li |Xi,K ). We
can then pick L0 := i m
                      P ci 0
                            i
                              Li .                                                             
  We shall use the following version of the Negativity Lemma, cf. [KM98, Lemma 3.39]. The
proof we give is a variant of the argument used in [BdFF10, Proposition 2.12].
Lemma 1.6. Assume that X is vertically Q-factorial and let π : X 0 → X be a vertical
blowup. If D ∈ Div0 (X 0 )R is π-nef then π ∗ π∗ D − D is effective.
   The condition that X is vertically Q-factorial guarantees that the pull-back of π∗ D by π
is well defined.
Proof. As a first step, we reduce the assertion to the case where D ∈ Div0 (X 0 )Q is π-ample.
Indeed, the set of vertical π-ample R-divisors, which is an open convex cone in Div0 (X 0 )R ,
is non-empty by (i) of Lemma 1.4. We may thus choose a basis A1 , . . . , Ar of DivP        0
                                                                                        0 (X )R
                                                           r
made up of π-ample Cartier divisors. Let ε = (εi ) ∈ R+ be such that Dε := D + i εi Ai
is a Q-divisor. The fact that D is π-nef means that D · C ≥ 0 for each curve C contained
in a fiber of π. Since each Ai is π-ample, it follows from Kleiman’s criterion [Kle66] that
Dε is π-ample on the projective k-scheme X00 , hence Dε is also π-ample on X 0 by [EGA,
III.4.7.1]. Upon replacing D with Dε for ε arbitrarily small we may thus assume as desired
that D ∈ Div0 (X 0 )Q is π-ample.
   Now choose m  1 such that OX 0 (mD) is π-globally generated, which means that the
vertical fractional ideal sheaf a := π∗ OX 0 (mD) satisfies a · OX 0 = OX 0 (mD). It is obvious
that a ⊂ OX (mπ∗ D), hence OX 0 (mD) ⊂ OX 0 (mπ ∗ π∗ D), and the result follows.              

               2. Projective Berkovich spaces and model functions
2.1. Analytifications. Let Y be a proper K-scheme. As a topological space, its K-
analytification Y an in the sense of Berkovich is compact and can be described as follows
(cf. [Ber90, Theorem 3.4.1]). Choose a finite cover of Y by Zariski open subsets of the form
U = Spec A where A is a finitely generated K-algebra. The Berkovich space U an is defined
as the set of all multiplicative seminorms | · |x : A → R+ extending the given absolute value
of K, endowed with the topology of pointwise convergence. It is common usage to write
|f (x)| := |f |x for f ∈ A and x ∈ U an . The space Y an is then obtained by gluing together
the open sets U an .
    There is a canonical continuous map s : Y an → Y , locally defined on U an by setting


## Literal published source 1201.0187: source-extracts/1201.0187-psh-compactness.txt

  Throughout this section we let X be as before a smooth connected projective K-analytic
variety and fix a closed (1, 1)-form θ ∈ Z 1,1 (X) whose de Rham class {θ} ∈ N 1 (X) is ample.
As before we write “psh” as a shorthand for “plurisubharmonic”. Similarly, “usc” and “lsc”
will mean “upper semicontinuous” and “lower semicontinuous”, respectively.
Definition 7.1. Let θ be as above. A θ-psh function ϕ : X → [−∞, +∞[ is a usc function
such that for each SNC model X of X on which θ is determined we have
    (i) ϕ ≤ ϕ ◦ pX on X;
             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                      33


  (ii) the restriction of ϕ to embX (∆X ) is a uniform limit of restrictions of θ-psh model
       functions.
We write PSH(X, θ) for the set of θ-psh functions on X.
   We say that ϕ : X → [−∞, +∞[ is quasi-psh if ϕ is θ-psh for some θ as above. Thanks
to Theorem 5.11, the previous definition is consistent with Definition 5.5 when ϕ is a model
function. In particular, constant functions are θ-psh iff θ is semipositive.
Remark 7.2. A function on a compact (complex) Kähler manifold X is quasi-psh if it is
locally the sum of a psh function and a smooth function. Given a closed (1, 1)-form θ, a θ-
psh function ϕ is a quasi-psh function such that θ + ddc ϕ ≥ 0 in the sense of currents. When
the de Rham class {θ} ∈ H 1,1 (X) is a Kähler class, we have a global characterization: θ-psh
functions are decreasing limits of sequences of smooth θ-psh functions, see [Dem92, Theorem
1.1]. In our current non-Archimedean setting, a general local theory of psh functions is still
to be developed (although the first steps are taken in [CLD12]). For this reason, we work
globally and assume that {θ} is ample.
  Recall the definitions from §4 of singular and model metrics on line bundles.
Definition 7.3. Let L be an ample line bundle on X. A singular metric on L is semipositive
if it is of the form k · ke−ϕ , where k · k is a model metric and ϕ is c1 (L, k · k)-psh.
   One checks that this definition does not depend on the choice of reference metric k · k.
Below we shall state various properties of θ-psh functions. We leave it to the reader to
formulate analogous assertions about semipositive singular metrics on ample line bundles.

7.1. Basic properties. Fix a closed (1, 1)-form θ ∈ Z 1,1 (X) as above. From Proposition 5.8
and 5.9 we obtain:
Proposition 7.4. The set PSH(X, θ) is convex. If ϕ, ψ are θ-psh and c ∈ R, then ϕ + c
and max{ϕ, ψ} are θ-psh.
Proposition 7.5. If ϕ ∈ PSH(X, θ) and X is an SNC model on which θ is determined,
then:
    (i) ϕ ◦ embX is continuous (and finite) on ∆X and convex on each face;
   (ii) ϕ ◦ pX is continuous on X and ϕ ≤ ϕ ◦ pX .
  The next result shows how to reconstruct a θ-psh function from its values on quasimono-
mial points.
Proposition 7.6. Let ϕ ∈ PSH(X, θ). Then, as X runs through the directed set of SNC
models on which θ is determined, (ϕ ◦ pX )X forms a decreasing net of continuous functions
on X, converging pointwise to ϕ.
Proof. Let X 0 ≥ X be two SNC models on which θ is determined. Then pX ◦ pX 0 = pX .
By Proposition 7.5 (ii) this implies ϕ ≤ ϕ ◦ pX 0 ≤ ϕ ◦ pX ◦ pX 0 = ϕ ◦ pX , with equality on
embX (∆X ). Set ϕ̃ := limX ϕ ◦ pX . Then ϕ̃ ≥ ϕ. On the other hand, by Corollary 3.9, pX
converges to the identity on X, so by upper semicontinuity of ϕ we have ϕ ≥ ϕ̃.             
Corollary 7.7. If ϕ, ψ ∈ PSH(X, θ) and ϕ = ψ on X div , then ϕ = ψ.
34              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


Proof. Let X be an SNC model on which θ is determined. By Corollary 3.17, X div is dense in
emb(∆X ) and by Proposition 7.5, ϕ and ψ are continuous on emb(∆X ), so our assumptions
imply that ϕ = ψ on emb(∆X ). Thus ϕ ◦ pX = ψ ◦ pX . Letting X run though all sufficiently
large models, we conclude using Proposition 7.6.                                         
7.2. Equicontinuity. The Lipschitz estimates in Theorem 6.1 carry over to general θ-psh
functions. As a consequence we have
Corollary 7.8. For any SNC model on which θ is determined, the family
                                 {ϕ ◦ embX | ϕ ∈ PSH(X, θ)}
is an equicontinuous family of functions on ∆X .
Corollary 7.9. If (ϕi )i is a decreasing net in PSH(X, θ) and ϕ = limi ϕi , then either
ϕ ≡ −∞ or ϕ ∈ PSH(X, θ).
Proof. Assume ϕ 6≡ −∞, and the upper semicontinuity of ϕi implies that of ϕ. Let X be
any SNC model on which θ is determined. The inequality ϕi ≤ ϕi ◦ pX implies ϕ ≤ ϕ ◦ pX ,
and hence
                               sup(ϕ ◦ embX ) = sup ϕ
                                    ∆X                      X
is finite. By Proposition 7.5, the supremum of each ϕi is attained on the finite set of divisorial
valuations associated to vertices of DX . Hence
                           sup(ϕi ◦ embX ) ≥ sup(ϕ ◦ embX ) > −∞
                           ∆X                  ∆X
for all i. It then follows from Corollary 7.8 that ϕi ◦ embX converges uniformly to ϕ ◦ embX
and that ϕ ◦ embX is continuous.                                                           
7.3. Compactness. We endow the set PSH(X, θ) of all θ-psh functions with the topology
of uniform convergence on dual complexes. A basis of open neighborhoods of a fixed θ-psh
function ϕ0 is then given by {ϕ | sup∆X |ϕ − ϕ0 | ≤ ε} where X ranges over SNC models on
which θ is determined and where ε > 0. Thanks to Proposition 7.6, the natural map
                                              Y
                                 PSH(X, θ) →       C 0 (∆X )
                                                    X
is a homeomorphism onto its image. Note also that D(X) ∩ PSH(X, θ) is dense in PSH(X, θ)
by definition. The following result is a more precise version of Theorem A.
Theorem 7.10. If ψ ∈ D(X) is any model function, then the map PSH(X, θ) → R defined
by ϕ 7→ supX (ϕ − ψ) is continuous and proper. Hence PSH(X, θ)/R is compact. Further-
more, the topology on PSH(X, θ) is equivalent to the topology of pointwise convergence on
either X qm or X div .
Proof. Let X be an SNC model on which θ and ψ are determined. Then ψ = ψ ◦ pX , so
Proposition 7.5 implies that (ϕ − ψ) ◦ pX is continuous and that (ϕ − ψ) ◦ pX ≥ (ϕ − ψ) for
any ϕ ∈ PSH(X, θ). Hence the supremum of ϕ − ψ is attained on embX (∆X ), which implies
the continuity of ϕ 7→ supX (ϕ − ψ).
  To prove properness, we need to show that
                         FC := {ϕ ∈ PSH(X, θ) | | sup(ϕ − ψ)| ≤ C}
                                                        X
             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                       35


is compact for any C > 0. Recall that PSH(X, θ) embeds in X C 0 (∆X ). By Tychonoff’s
                                                              Q
theorem, the compactness of FC is therefore equivalent to the compactness in C 0 (∆X ) of
the closure of the image of FC in C 0 (∆X ), for each SNC model X on which θ and ψ are
determined. But this is a direct consequence of Corollary 7.8 and Ascoli’s theorem.
   Picking ψ = 0, we see that ϕ 7→ supX ϕ is proper, which implies the compactness of
PSH(X, θ).
   For the last statement, it is clear that convergence in PSH(X, θ) implies pointwise con-
vergence on X qm which in turn implies pointwise convergence on X div . Now let (ϕα )α∈A
be a net of θ-psh functions converging pointwise to ϕ ∈ PSH(X, θ) on X div . Fix any SNC
model X on which θ is determined. We must show that ϕα converges uniformly to ϕ on
embX (∆X ). But X div ∩ embX (∆X ) is dense in embX (∆X ) by Corollary 3.17, so this follows
from the equicontinuity statement in Corollary 7.8.                                       
7.4. Upper envelopes. Finally we shall prove the following result, whose complex analogue
serves as a basic ingredient of pluripotential theory. While we will not go deeper into
pluripotential theory here, we will use the result below in §8. The proof will in fact not use
the compactness result in §7.3.
Theorem 7.11. Let (ϕα )α∈A be an arbitrary family of θ-psh functions on X, and assume
                                                                            for each x ∈ X,
that (ϕα ) is uniformly bounded from above. If we set ϕ(x) := supα∈A ϕα (x) S
                             ∗                                        qm
then the usc regularization ϕ of ϕ is θ-psh and coincides with ϕ on X = X embX (∆X ).
Further, we have ϕ∗ = limX ϕ ◦ pX = inf X ϕ ◦ pX .
  Recall that the usc regularization of a function u on a topological space X is the smallest
usc function u∗ ≥ u, given by u∗ (x) = lim supy→x u(y).
Proof of Theorem 7.11. Upon considering the new family ϕI = maxα∈I ϕα with I ranging
over all finite subsets of A, we may assume that A is a directed set and (ϕα ) is an increasing
net. We must show that conditions (i)–(ii) of Definition 7.1 hold for ϕ∗ .
   For each SNC model X on which θ is determined, ϕα ◦ embX is convex and continuous
on ∆X for each α. The increasing limit ϕ ◦ embX = limα ϕα ◦ embX is therefore convex
and lsc on ∆X . On the other hand, any convex function on a convex polytope is usc,
see [GKR68]. Thus ϕ ◦ embX is continuous, and, by Dini, ϕα ◦ embX converges uniformly
on ∆X to ϕ ◦ embX . Equivalently, ϕ ◦ pX is continuous and ϕα ◦ pX converges uniformly to
ϕ ◦ pX on X.
   Since X 7→ ϕα ◦ pX is decreasing, the same is true for X 7→ ϕ ◦ pX . We claim that
limX ϕ ◦ pX = ϕ∗ . To see this, note that ψ := limX ϕ ◦ pX is a decreasing limit of continuous
functions and hence usc. On the one hand, ϕ ◦ pX ≥ ϕ for all X implies ψ ≥ ϕ, so that
ψ ≥ ϕ∗ by the definition of the usc regularization. On the other hand, Corollary 3.9 and
the upper semicontinuity of ϕ∗ implies
                             ϕ∗ ≥ lim ϕ∗ ◦ pX ≥ lim ϕ ◦ pX = ψ,
                                  X              X
         ∗
so that ϕ = limX ϕ ◦ pX = inf X ϕ ◦ pX , hence the claim.
   If Y ≤ X are SNC models on which θ is determined, then pX ◦ pY = pY by Proposi-
tion 3.6 (iv). By what precedes, this implies ϕ∗ ◦ pY = limX ϕ ◦ pX ◦ pY = ϕ ◦ pY . In
particular, ϕ∗ = ϕ on embY (∆Y ). Since Y was arbitrary, we get ϕ∗ = ϕ on X qm .
   It remains to prove that ϕ∗ is θ-psh in the sense of Definition 7.1. First, ϕα ≤ ϕα ◦ pX
for all α implies ϕ ≤ ϕ ◦ pX , which gives ϕ∗ ≤ (ϕ ◦ pX )∗ = ϕ ◦ pX = ϕ∗ ◦ pX , where the first
36                SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


equality follows from the continuity of ϕ ◦ pX . Thus (i) holds. Second, the restriction of
each ϕα to embX (∆X ) is, by assumption, a uniform limit of θ-psh model functions. Since ϕα
converges uniformly to ϕ = ϕ∗ on embX (∆X ), we see that the restriction of ϕ∗ to embX (∆X )
is also a uniform limit of θ-psh model functions. Thus (ii) also holds and ϕ∗ is θ-psh.   

                             8. Envelopes and regularization
  We continue to assume that θ ∈ Z 1,1 (X) is a closed (1, 1)-form whose de Rham class
{θ} ∈ N 1 (X) is ample. This positivity property will be crucial in the arguments to follow.


## Literal published source 1201.0187: source-extracts/1201.0187-base-ideal-proof.txt

Theorem 8.5. Let L be an ample line bundle on X and L ∈ Pic(X ) an extension of L to
an SNC model X . Let θ ∈ Z 1,1 (X) be the curvature form of the corresponding model metric
                                                                                1
on L. For m  1 let am ⊂ OX be the (vertical) base-ideal of mL and set ϕm := m    log |am |.
Then ϕm is a θ-psh model function and ϕm → Pθ (0) uniformly on X as m → ∞.
Proof of Theorem 8.5. For m  1, mL|XK is globally generated, which shows that the ideal
sheaf am is vertical. Since OX (mL) ⊗ am is globally generated by the definition of am , it
follows that ϕm ∈ D(X) is θ-psh by Lemma 5.6. Note that am · al ⊂ am+l for all m, l.
This yields the super-additivity property mϕm + lϕl ≤ (m + l)ϕm+l . As a consequence, the
pointwise limit limm ϕm exists and coincides with supm ϕm .
   Step 1. Let us first prove that Pθ (0) = supm ϕm on X qm . The argument is similar to
Step 2 of Theorem 5.11. Since ϕm is θ-psh and ϕm ≤ 0 for all m, we have supm ϕm ≤ Pθ (0)
on X. To see that equality holds on X qm , pick ε > 0 and x ∈ embX 0 (∆X 0 ) for some SNC
38               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


model X 0 dominating X . By Lemma 8.4 there exists a θ-psh model function ϕ such that
ϕ ≤ 0 and ϕ(x) ≥ Pθ (0)(x) − ε. Replacing X 0 by a higher model, we may assume that
ϕ = ϕD is determined by some divisor D ∈ Div0 (X 0 )Q . Invoking Proposition 5.2 we may
also assume that there exists D0 ∈ Div0 (X 0 )Q with −ε ≤ ϕD0 ≤ 0 on X and π ∗ L + D + D0
ample. Since D + D0 ≤ 0 we then have
                           OX 0 (mπ ∗ L + m(D + D0 )) ⊂ OX 0 (mπ ∗ L).
Now the left-hand side is globally generated for some m, and we conclude that
                                  OX 0 (m(D + D0 )) ⊂ OX 0 · am ;
hence
                                                     1
        Pθ (0)(x) ≤ ϕD (x) + ε ≤ ϕD+D0 (x) + 2ε ≤      log |am |(x) + 2ε ≤ sup ϕl (x) + 2ε.
                                                     m                      l

   Step 2. Introduce, for each m ∈ N, the asymptotic multiplier ideal bm := J (am  • ) ⊂ OX
associated to the graded sequence a• . We refer to Appendix B for the definition and the
proof of the fundamental properties of multiplier ideals in our present setting. We shall use
the following results. First, we have the elementary inclusion am ⊂ bm for all m. Second,
the subadditivity property (cf. Theorem B.7) implies bml ⊂ blm for any l, m. We infer that
aml ⊂ bml ⊂ blm for any m, l and hence
                         1                 1
                         m log |bm | ≥ sup ml log |aml | = sup ϕml = Pθ (0)                   (8.1)
                                        l                   l

on X qm for all m, where the last equality follows from Step 1.
  Since both Pθ (0) and ϕm remain unchanged when X is replaced with a higher model, we
may assume that there exists an effective divisor E ∈ Div0 (X )Q such that A := L − E is
ample on X . By the uniform global generation property of multiplier ideals (Theorem B.8
and Remark B.9) we may then choose m0 ∈ N such that m0 A is ample enough to guarantee
that OX (mL + m0 A) ⊗ bm is globally generated for all m. Since OX (mL + m0 A) injects in
OX ((m + m0 )L) by multiplying with the canonical section of OX (m0 E), it follows that
                                 log |bm | ≤ log |am+m0 | + m0 ϕE .
Replacing m with m − m0 and using (8.1) we infer (m − m0 )Pθ (0) ≤ mϕm + m0 ϕE , so that
                                             m          m0
                              ϕm ≤ Pθ (0) ≤ m−m 0
                                                  ϕm + m−m 0
                                                             ϕE

on X qm for m  1. As ϕm , Pθ (0) and ϕE are all θ-psh, Proposition 7.6 shows that this
inequality extends to all of X. Now ϕE is bounded and ϕm is uniformly bounded, as follows
from ϕ1 ≤ ϕm ≤ 0, so ϕm converges uniformly on X to Pθ (0), as was to be shown.        

     Let us end this subsection with a result that will be used in [BFJ12a].
Corollary 8.6. If ϕ ∈ PSH(X, θ) and v ∈ C 0 (X) are such that ϕ ≤ v then for every ε > 0


## Literal published source 1201.0188: source-extracts/1201.0188-standing-and-Theorem-A.txt

on the work of Aubin, Calabi and Yau, which culminated in the celebrated article [Yau78],
where it was shown that the solution metric is smooth when µ is a smooth positive volume
form on X.
   We next turn to the non-Archimedean analogue, referring to §2 for more details. Let
K be a complete discrete valuation ﬁeld whose residue ﬁeld k has characteristic zero, so
that K ≃ k((t)). Let X be a smooth projective variety over K, and write n = dim X.
Thanks to the non-Archimedean GAGA principle, it is reasonable to also denote by X
the corresponding K-analytic space in the sense of Berkovich, whose underlying topological
space is compact Hausdorﬀ. A model of X is a normal scheme X that is ﬂat and projective
over S := Spec k[[t]], and whose generic ﬁber can be identiﬁed with X.
   Consider a ample line bundle L on X. A model metric on L is a metric deﬁned by a
extension L ∈ Pic(X )Q of L to some model X . Such a metric is called semipositive if L is
nef, i.e. has non-negative degree on all proper curves of the special ﬁber of X . S.-W. Zhang
introduced in [Zha95] the more ﬂexible notion of semipositive continuous metric as the
uniform limit of semipositive model metrics.1 In this context, A. Chambert-Loir [CL06]
deﬁned the Monge-Ampère measure c1 (L, k · k)n of a semipositive continuous metric k · k on
L. It is a positive Radon measure on X, of mass deg L.
   V. Berkovich constructed in [Ber99] the skeleton associated to a polystable model of X.
Since we are assuming K to have residue characteristic zero, it is easier to rely on resolution
of singularities and instead consider SNC models, i.e. models whose special ﬁber has simple
normal crossing support (but is not necessarily reduced, as opposed to a semistable model).
To each SNC model X is associated a dual complex ∆X that encodes the combinatorics of
the intersections of the components of the special ﬁber, and which embeds in the Berkovich
space X just as skeletons do. Any ﬁnite set  S of divisorial points is contained in the dual
complex of some SNC model; in particular X ∆X is dense in X.
   We can now state our main result. We say that X is algebraizable if there exists a (one-
variable) function ﬁeld F admitting K as a completion and a smooth projective F -scheme
Y such that X = YK .
Theorem A. Let K be a complete discrete valuation field of residue characteristic zero. Let
X be a smooth projective K-variety that is algebraizable. Let L ∈ Pic(X) be an ample line
    1We refer to Table 1 in §2.6 below for a comparison of our terminology with existing terminology.
               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                          3

bundle and µ be a positive Radon measure on X of mass c1 (L)n . If we further assume that
µ is supported on the dual complex of some SNC model of X, then there exists a continuous,
semipositive metric k · k on L such that
                                   c1 (L, k · k)dim X = µ .                              (1.1)
This metric is furthermore unique up to a multiplicative constant.
  Even though the result is most likely true without this assumption, the algebraizability
condition plays an essential role in our proof, as we shall explain below. Note that the line
bundle L is not assumed to be deﬁned over a function ﬁeld.
   The uniqueness part in Theorem A follows from a result of X. Yuan and S.-W. Zhang
[YZ10] asserting more generally that a continuous semipositive metric k · k is uniquely de-
termined up to a constant by its Monge-Ampère measure. Their proof is inspired by the
one given by Blocki [Blo03] in the complex setting.
   Our approach does not give any information on the regularity of the metric besides con-
tinuity. It would be interesting to further investigate this issue, for instance when µ is
supported on ﬁnitely many divisorial points. We refer to §9 for a discussion of this problem
in the case of toric varieties, based on the recent work [BPS11].
   Versions of Theorem A are already known in a few cases. For curves (and in fact over any
complete non-Archimedean, non-trivially valued ﬁeld), it can easily be deduced from results


## Literal published source 1201.0188: source-extracts/1201.0188-psh-background.txt

2.4. θ-psh functions. Fix a form θ ∈ Z 1,1 (X) with ample de Rham class {θ} ∈ N 1 (X).

Definition 2.5. A θ-psh function ϕ : X → [−∞, +∞[ is an usc function such that for each
SNC model X of X on which θ is determined we have
    (i) ϕ ≤ ϕ ◦ pX on X;
   (ii) the restriction of ϕ to the dual complex ∆X is a uniform limit of restrictions of model
        functions ψ such that θ + ddc ψ is a semipositive form.
We write PSH(X, θ) for the set of θ-psh functions on X.

  It is a nontrivial fact that if ϕ is a θ-psh model function then the form θ + ddc ϕ is in fact
semipositive, see [BFJ11, Theorem 5.11]. In particular, the zero function is θ-psh iﬀ θ is
semipositive. In this case, max{ϕ, −t} is θ-psh when ϕ is θ-psh and t ∈ R.

Proposition 2.6. [BFJ11, Proposition 5.10]. The space of model functions D(X) is spanned
by θ-psh model functions.

Proposition 2.7. [BFJ11, Proposition 7.4]. The set PSH(X, θ) is convex. If ϕ, ψ are θ-psh
and c ∈ R, then the functions max{ϕ, ψ} and ϕ + c are also θ-psh.

Proposition 2.8. [BFJ11, Proposition 7.5]. Any ϕ ∈ PSH(X, θ) is continuous on the dual
complex of any SNC model X , and convex on each of its faces.

  In fact, the continuity statement above can be made uniform in ϕ:
Theorem 2.9. [BFJ11, Corollary 7.7] For any SNC model X , the restrictions of all θ-psh
functions to the dual complex ∆X form an equicontinuous family.

   We endow PSH(X, θ) with the topology of uniform convergence on dual complexes. Notice
that the divisorial points are dense on each dual complex ∆X , see [BFJ11, Corollary 3.13]
or [JM10, Remark 3.9]. As a consequence of equicontinuity we thus have

Theorem 2.10. [BFJ11, Theorem 7.8]. For each model function ψ the map ϕ 7→ supX (ϕ −
ψ) is continuous and proper on PSH(X, θ). In particular, the space PSH(X, θ)/R is compact.
Further, the topology on PSH(X, θ) is equivalent to the topology of pointwise convergence on
X div .

  Finally we have the following regularization result. Its proof relies on multiplier ideals.

Theorem 2.11. [BFJ11, Theorem 8.7]. For any θ-psh function ϕ, there exists a decreasing
net (ϕj )j of θ-psh model functions that converges pointwise on X to ϕ.

   The complex analogue of this result is due to Demailly [Dem92] (see also [GZ05, Appendix]
for the case of a line bundle). By Dini’s lemma, we get as a consequence:

Corollary 2.12. [BFJ11, Corollary 8.8] The set D(X) ∩ PSH(X, θ) is dense in C 0 (X) ∩
PSH(X, θ) with respect to uniform convergence on X.

  Proposition 4.5 below reﬁnes Theorem 2.11 and asserts that any θ-psh function is actually
the decreasing limit of a sequence of θ-psh model functions (but the proof heavily uses
Theorem 2.11).
12               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

2.5. Envelopes. Let θ be a form as in §2.4.
Proposition 2.13. [BFJ11, Theorem 7.9]. If (ϕα )α∈A is a family of θ-psh functions that
is uniformly bounded above, then the usc upper envelope (supα ϕα )∗ is also θ-psh.
  Recall that the usc regularization u∗ of a function u : X → [−∞, +∞[ is the smallest usc
function such that u∗ ≥ u.
Definition 2.14. Let f : X → [−∞, +∞[ be any function. We define its θ-psh envelope
Pθ (f ) as follows. If there does not exist any ϕ ∈ PSH(X, θ) such that ϕ ≤ f on X then
we set Pθ (f ) ≡ −∞. Otherwise, we define Pθ (f ) as the usc upper envelope of the set of all
θ-psh functions ϕ such that ϕ ≤ f on X, i.e. we set
                        Pθ (f ) := (sup {ϕ | ϕ ∈ PSH(X, ω), ϕ ≤ f })∗ .
   Thanks to Proposition 2.13 Pθ (f ) is either −∞ or belongs to PSH(X, θ). If f is usc, then
clearly Pθ (f ) ≤ f on X, and Pθ (f ) is then the largest θ-psh function with this property.
Proposition 2.15. [BFJ11, Proposition 8.1]
    (i) Pθ is non-decreasing: f ≤ g ⇒ Pθ (f ) ≤ Pθ (g).
   (ii) Pθ (f ) is concave in both arguments:
                      Ptθ+(1−t)θ′ (tf + (1 − t)g) ≥ tPθ (f ) + (1 − t)Pθ′ (g)
           for 0 ≤ t ≤ 1.
     (iii) For each c ∈ R we have Pθ (f + c) = Pθ (f ) + c.
     (iv) Pθ is 1-Lipschitz continuous, i.e. supX |Pθ (f ) − Pθ (g)| ≤ supX |f − g|.
      (v) Given a bounded function f and a convergent sequence θm → θ in N 1 (X /S) we have
           Pθm (f ) → Pθ (f ) uniformly on X.
2.6. Metrized line bundles and curvature forms. We refer to [CL10] for a general
account of metrized line bundles in a non-Archimedean context. Suﬃce it to say that a
metric k · k on a line bundle L on X is a way to produce a local continuous function ksk on
(the Berkovich space) X from any local section s of L.
   Let X be a model and L a line bundle on X such that L|X = L. To this data one can
associate a unique metric k · kL on L with the following property: if s is a nonvanishing
local section of L on an open set U ⊂ X , then kskL ≡ 1 on U := U ∩ X. This makes sense
since such a section s is uniquely deﬁned up to multiplication by an element of Γ(U , OX ∗ )



## Literal published source 1201.0188: source-extracts/1201.0188-intersection-calculus.txt

Proposition-Definition 2.18. To any n-tuple (θ1 , . . . , θn ) of closed (1, 1)-forms we can
associated a signed atomic measure θ1 ∧ · · · ∧ θn supported on X div such that
                    Z                      X
                       f θ1 ∧ · · · ∧ θn =   bi f (xi ) (θ1,X |Ei · . . . · θn,X |Ei )  (2.2)
                       X                        i∈I
for any common determination X of the forms           P       θi , and for any model function f . Here
we have written the special fiber as X0 =                i∈I bi Ei and xi = xEi is the divisorial point
associated to Ei .
   Further, (θ1 , . . . , θn ) 7→ θ1 ∧ · · · ∧ θn is multilinear and symmetric.
14              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON
                                                                           R
Proof. Choose a commonR determination of the forms θi , and deﬁne X f (θ1 ∧ · · · ∧ θn )
using (2.2). The fact that X f (θ1 ∧· · ·∧θn ) does not depend on the choice of a determination
X is a consequence of the projection formula
                          π∗ D · θ1,X · . . . · θn,X = D · π ∗ θ1,X · . . . · π ∗ θn,X
if π : X ′ → X , and D is any vertical divisor in X ′ .                             P
   Then by construction θ1 ∧· · ·∧θn can be identiﬁed with the atomic measure i wi δxi with
wi = (θ1,X |Ei · . . . · θn,X |Ei ). This measure is supported on the divisorial points associated
to the irreducible components of X0 . The last statement is clear.                               
Proposition 2.19. If the forms θ1 , . . . , θn are semipositive, then θ1 ∧ · · · ∧ θn is a positive
measure, of mass           Z
                                           θ1 ∧ · · · ∧ θn = {θ1 } · . . . · {θn }.                               (2.3)
                                      X

Proof. Pick a model X such that each θi is determined by a nef class θi,X ∈ N 1 (X /S).
The restriction of θi,X to each component Eω of X0 is then also nef, and it follows that the
intersection number (θ1,X |E · ... · θn,X |E ) is non-negative, hence the ﬁrst assertion. Since the
constant function 1 corresponds to the vertical divisor X0 we have by deﬁnition
                               Z
                                     θ1 ∧ ... ∧ θn = X0 · θ1 · . . . · θn .
                                       X
By [Ful98, Example 20.3.3] this is the same as the intersection number against the generic
ﬁber of X , and this is equal to {θ1 } · . . . · {θn } by deﬁnition.                    
   As a special case, ﬁx θ ∈ Z 1,1 (X). To any θ-psh model functions ϕ1 , . . . , ϕn we then
associate a mixed Monge-Ampère measure
                                      (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn ).
This is an atomic positive measure on X of mass {θ}n .
  Analogously to the complex case we have the following integration by parts formula:
Proposition 2.20. If f, g ∈ D(X) are model functions and θ1 , . . . , θn−1 are closed (1, 1)-
forms then we have
                 Z                             Z
                   f dd g ∧ θ1 ∧ · · · ∧ θn−1 = g ddc f ∧ θ1 ∧ · · · ∧ θn−1 .
                       c


Proof. Pick a common determination X of f, g and the θi ’s, and divisors D, D ′ , Di such that
f = ϕD , g = ϕD′ and θi is the class in N 1 (X /S) induced by Di . Then by deﬁnition we have
  Z                                X
     f ddc g ∧ θ1 ∧ · · · ∧ θn−1 =   ordE (D)(D ′ |E · D1 |E · ... · Dn−1 |E )
                                           E
                       X
                  =           ordE (D) ordE ′ (D ′ ) (D1 |E )|E ′ ∩E · ... · (Dn−1 |E )|E ′ ∩E
                      E,E ′
                      X
                  =           ordE (D) ordE ′ (D ′ ) (D1 |E ′ )|E∩E ′ · ... · (Dn−1 |E ′ )|E∩E ′
                      E,E ′
                                                                                      Z
                                                                                =         g ddc f ∧ θ1 ∧ · · · ∧ θn−1
                SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                            15

where the third equality follows from [Ful98, Theorem 2.4].                                     

  The next result follows from the Hodge index theorem, compare [YZ10, Theorem 2.1.1].
Proposition 2.21. Suppose θ1 , . . . , θn−1 are semipositive closed (1, 1)-forms. Then the
symmetric bilinear form
                                     Z
                        (f, g) 7→        f ddc g ∧ θ1 ∧ · · · ∧ θn−1
                                        X

on D(X) is negative semidefinite. In particular, for any two model functions f , g, the
following Cauchy-Schwarz inequality holds:
    Z
       f ddc g ∧ θ1 ∧ · · · ∧ θn−1 ≤
    X
               Z                            1/2  Z                            1/2
                      c                                   c
               −  f dd f ∧ θ1 ∧ · · · ∧ θn−1       −  g dd g ∧ θ1 ∧ · · · ∧ θn−1      . (2.4)
                   X                                     X

Proof of Proposition 2.21. Fix a model function f . We need to prove
                                 Z
                            I :=   f ddc f ∧ θ1 ∧ · · · ∧ θn−1 ≤ 0
                                    X

Choose a common determination X of ϕ and all the θi . By continuity, we may assume
ϕ = ϕD for some D ∈ Div0 (X )Q , and each form θi is determined by a Q-line bundle Li on
X . Then I = D 2 · L1 · . . . · Ln−1 and the result follows from [YZ10, Theorem 2.1.1 (a)]. 
Remark 2.22. In the complex case we have by Stokes’ theorem
             Z                               Z
                f ddc g ∧ θ1 ∧ ... ∧ θn−1 = − df ∧ dc g ∧ θ1 ∧ ... ∧ θn−1 ,



## Literal published source 1201.0188: source-extracts/1201.0188-bounded-operator-proof.txt

In the next three sections we shall develop some of the Bedford-Taylor theory in our non-
Archimedean setting.
  Our ﬁrst main objective is to extend the Monge-Ampère operator deﬁned in §2.7 from
θ-psh model functions to bounded θ-psh functions.
Theorem 3.1. There exists a unique operator
                                (ϕ1 , . . . , ϕn ) 7→ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn )
taking an n-tuple of bounded θ-psh functions to a positive Radon measure on X of mass
{θ}n and such that
     • the definition is compatible with the definition for θ-psh model functions given in §2.7;
     • for any decreasing nets of bounded θ-psh functions ψ j → ψ, and ϕji → ϕi for i =
        1, . . . , n we have
       Z                                                Z
          ψ j (θ + ddc ϕj1 ) ∧ · · · ∧ (θ + ddc ϕjn ) −→ ψ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn ).

Remark 3.2. One can also prove continuity along increasing nets but we will not need this.
   Note that the uniqueness part of Theorem 3.1 follows from the fact that any θ-psh function
is the decreasing limit of a net of θ-psh model functions, see Theorem 2.11. For the same
reason, the mapping
                                (ϕ1 , . . . , ϕn ) 7→ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn )
is symmetric in its arguments, and additive in the following sense:
     (θ + tddc ϕ1 + (1 − t)ddc ϕ′1 ) ∧ (θ + ddc ϕ2 ) ∧ · · · ∧ (θ + ddc ϕn ) =
                         t (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn ) + (1 − t) (θ + ddc ϕ′1 ) ∧ · · · ∧ (θ + ddc ϕn )
                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                      17

for 0 ≤ t ≤ 1. This additivity property in particular implies
               (θ + ddc (tϕ + (1 − t)ψ))n ≥ tn (θ + ddc ϕ)n + (1 − t)n (θ + ddc ψ)n                     (3.1)
in the sense of measures, for all bounded θ-psh functions ϕ, ψ, and any 0 ≤ t ≤ 1.
   Given bounded θ-psh functions, one can now deﬁne signed measures
                    ddc ϕ1 ∧ · · · ∧ ddc ϕp ∧ (θ + ddc ϕp+1 ) ∧ · · · ∧ (θ + ddc ϕn )
by writing ddc ϕi = (θ + ddc ϕi ) − θ and expanding the product formally using multilinearity.
These products are also continuous along decreasing nets, and we thus obtain
Corollary 3.3. If ϕ1 , . . . , ϕn−1 are bounded θ-psh functions on X, then the bilinear form
                              Z
               (ϕ, ψ) 7→ (−ϕ) ddc ψ ∧ (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕn−1 )

is well-defined and positive semidefinite on the vector space spanned by the set of bounded
θ-psh functions.
   In particular, the Cauchy-Schwarz inequality (2.4) holds for all bounded θ-psh functions
ϕ2 , . . . , ϕn and for all functions ψ, ϕ that are diﬀerences of bounded θ-psh functions.
3.1. Proof of Theorem 3.1. We adapt to our setting the Bedford-Taylor approach as
explained, for instance, in [Dem, Theorem 3.7, p.188].
   Fix 0 ≤ p ≤ n and θ-psh model functions ϕ′p+1 , . . . , ϕ′n . Consider the following statement.
Assertion A(p). To any p-tuple ϕ1 , . . . , ϕp of bounded θ-psh functions is associated a positive
Radon measure M(ϕ1 , . . . , ϕp ) of mass {θ}n such that:
     • if ϕ1 , . . . , ϕp are model functions then
 M(ϕ1 , . . . , ϕp ) = (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕp ) ∧ (θ + ddc ϕ′p+1 ) ∧ · · · ∧ (θ + ddc ϕ′n ) (3.2)
      • the mapping                                        Z
                                (ψ, ϕ1 , . . . , ϕp ) 7→       ψ M(ϕ1 , . . . , ϕp )
        is continuous along decreasing nets of bounded θ-psh functions.
  We shall prove A(p) by induction on p. Observe that for p = n, this proves Theorem 3.1.
  The assertion A(0) is clear, since M(ϕ′1 , . . . , ϕ′n ) is a ﬁnite sum of Dirac masses at divisorial
points of X. Assume that A(p − 1) holds for any (n − p + 1)-tuple of θ-psh model functions
and let ϕ′p+1 , . . . , ϕ′n be θ-psh model functions.
  Given bounded θ-psh functions ϕ1 , . . . , ϕp , we deﬁne M(ϕ1 , . . . , ϕp ) by forcing the inte-
gration by parts formula
  Z
      ψ M(ϕ1 , . . . , ϕp−1 , ϕp ) :=
    Z
       ϕp (θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕp−1 ) ∧ (θ + ddc ψ) ∧ (θ + ϕ′p+1 ) ∧ · · · ∧ (θ + ddc ϕ′n )
       Z
    + (ψ − ϕp )(θ + ddc ϕ1 ) ∧ · · · ∧ (θ + ddc ϕp−1 ) ∧ θ ∧ (θ + ϕ′p+1 ) ∧ · · · ∧ (θ + ddc ϕ′n ) (†)

for every model function ψ.
18                  SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

   Observe that the right-hand side is continuous along decreasing nets as a function of
(ϕ1 , . . . , ϕp ) by the induction hypothesis. Since equality holds in (†) when all the ϕi are
model functions and since M(ϕ1 , . . . , ϕp ) is a positive measure of mass {θ}n , it follows by
regularization (Theorem 2.11) that the right-hand side is also linear in ψ, and non-negative
when ψ ≥ 0.
   Now the space of model functions is spanned by θ-psh model functions by Proposition 2.6;
hence M(ϕ1 , . . . , ϕp ) is well-deﬁned as a positive measure of mass {θ}n and is continuous
along decreasing nets as a function of (ϕ1 , . . . , ϕp ). It remains to show that
                                                         Z
                                 (ψ, ϕ1 , . . . , ϕp ) 7→ ψ M(ϕ1 , . . . , ϕp )

is continuous along decreasing nets of bounded θ-psh functions. Let thus (ϕji )j , i = 1, . . . , p
and ψ j be decreasing nets of θ-psh functions converging, respectively, to bounded θ-psh
functions ϕi and ψ. Set
                                            µj := M(ϕj1 , . . . , ϕjp ).
We already know that µj converges weakly to µ := M(ϕ1 , . . . , ϕp ). Since ψ j is usc for each
j, Corollary 2.25 yields
                                      Z         Z
                               lim sup ψ j µj ≤ ψµ.
                                                j

For the reverse estimate, we rely on the following approximate monotonicity property:
Lemma 3.4. Let ψ and χi ≥ ϕi , i = 1, . . . , p be bounded θ-psh functions. Then we have
        Z                         Z
           ψ M(χ1 , . . . , χp ) ≥ ψ M(ϕ1 , . . . , ϕp )
                                          p Z
                                          X
                                      +             (ϕi − χi ) M(ϕ1 , . . . , ϕi−1 , 0, χi+1 , . . . , χp ).
                                          i=1

     The lemma implies that, for each j:
          Z       Z          Z       X p Z
             j j        j
            ψ µ ≥ ψµ ≥ ψµ +                (ϕi − ϕji ) M(ϕ1 , . . . , ϕi−1 , 0, ϕji+1 , . . . , ϕjp ).
                                                i=1

By the inductive hypothesis,R the sumRin the right-hand side tends to 0 as j → ∞, so we
infer as desired that lim inf j ψ j µj ≥ ψµ.

Proof of Lemma 3.4. Note ﬁrst that ψ may be assumed to be a model function by
Lemma 3.5. Let ν be a positive Radon measure on X and let ϕ be a bounded θ-psh function.
Then we have                      Z           Z
                                                    ϕν = inf         ψν
                                                            ψ≥ϕ

where ψ ranges over all θ-psh model functions such that ψ ≥ ϕ.
   Since we already know that (ϕ1 , . . . , ϕp ) 7→ M(ϕ1 , . . . , ϕp ) is continuous along decreas-
ing nets, we may by regularization assume that all ϕi and χi are also model functions.
                  SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                                 19

Integration by parts (†) then yields
   Z                             Z
     ψ M(χ1 , χ2 , . . . , χp ) − ψ M(ϕ1 , χ2 , . . . , χp ) =
                                   Z                                  Z
                                 = (χ1 − ϕ1 ) M(ψ, χ2 , . . . , χp ) − (χ1 − ϕ1 ) M(0, χ2 , . . . , χp )

hence
         Z                             Z                                      Z
             ψ M(χ1 , . . . , χp ) ≥           ψ M(ϕ1 , χ2 , . . . , χp ) +       (ϕ1 − χ1 ) M(0, χ2 , . . . , χp ).

We similarly have
               Z                                              Z
                      ψ M(ϕ1 , χ2 , χ3 , . . . , χp ) ≥            ψ M(ϕ1 , ϕ2 , χ3 , . . . , χp )
                                                              Z
                                                          +       (ϕ2 − χ2 ) M(ϕ1 , 0, χ3 , . . . , χp ).

Iterating this argument and summing up then yields the desired result.                                                 

Proof of Lemma 3.5. Let ε > 0. Since ϕ is usc,R LemmaR 2.24 shows that there exists a
continuous function v on X such that v ≥ ϕ and vν ≤ ϕν + ε. The result now follows
since [BFJ11, Corollary 8.6] yields an θ-psh model function ψ such that ϕ ≤ ψ ≤ v + ε. 
Definition 3.6. A pluripolar set is a subset of {ψ = −∞} for some ψ ∈ PSH(X, θ).
Proposition 3.7. Let ϕ1 , ..., ϕn be bounded θ-psh functions. Then any ψ ∈ PSH(X, θ) is


## Literal published source 1201.0188: source-extracts/1201.0188-regularization-locality.txt

Definition 4.1. For any Borel set E ⊆ X, set
                             Z                                    
              Capω (E) = sup      MA(ϕ) | ϕ ∈ PSH(X, ω), −1 ≤ ϕ ≤ 0 .
                                    E
                                                   n
   By PropositionS 2.19 wePhave 0 ≤ Capω (E) ≤ {ω} . Note that if E1 , E2 , . . . are Borel
sets, then Capω ( Ej ) ≤ j Capω (Ej ).
   The Monge-Ampère operator and the capacity of course depend on the choice of ω, but
we drop this dependence for notational simplicity.
                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                       21

Lemma 4.2. If x ∈ X is a divisorial point, then Capω {x} > 0. As a consequence, every
nonempty open subset of X has strictly positive capacity.
Proof. The second statement follows from the ﬁrst since divisorial points are dense in X,
see §2.1. To prove the ﬁrst statement, pick an SNC model X of X such that x = xE is
associated to an irreducible component Eω of the special ﬁber. By [BFJ11, Proposition 5.2]
there exists u ∈ D(X) determined on X such that −1 ≤ u ≤ 0 and ω + ddc u is determined
by an ample class in N 1 (X /S). Then Capω {x} ≥ MA(u){x} = bE ((ω + ddc u)|E )n > 0,
see §2.7.                                                                               

  The next two propositions are the main results of this section.
Proposition 4.3. If ϕ is a bounded ω-psh function then for each ε > 0 there exists an
open subset G ⊆ X with Capω (G) < ε and a decreasing sequence (ϕm )∞   m=1 of ω-psh model
functions that converges uniformly to ϕ on G . In particular, ϕ is continuous on Gc .
                                            c


Definition 4.4. A function h : X → R is said to be quasicontinuous iff it is continuous
outside sets of arbitrarily small capacity.
  The previous result can be thus rephrased by saying that bounded ω-psh functions are
quasicontinuous.
  Using the same technique we shall replace nets by sequences in the regularization result for
ω-psh functions (Theorem 2.11). While not crucial, this result is psychologically satisfying
and does simplify the proof of Corollary 7.3 below.
Proposition 4.5. Any ω-psh function ϕ is the limit of a decreasing sequence (ϕm )∞
                                                                                 m=1 of
ω-psh model functions.
  The rest of this section is devoted to the proof of these two propositions. First we state
and prove two estimates on special Monge-Ampère integrals.
Lemma 4.6. The Monge-Ampère measure of any bounded ω-psh is linearly bounded by the
capacity. More precisely, if u is an ω-psh function such that −M ≤ u ≤ 0, where M ≥ 1,
then
                                    MA(u) ≤ M n Capω
on Borel sets.
Proof. Given a Borel set E ⊂ X we have
 Z            Z               Z                 Z
                                                         u
     MA(u) = (ω + ddc u)n ≤ (M ω + ddc u)n = M n (ω + ddc )n ≤ M n Capω (E).
   E           E                E                E       M
Here the ﬁrst inequality follows by writing M ω + ddc u = (M − 1)ω + ω + ddcu and expanding
the Monge-Ampère measure by multilinearity.                                             
Lemma 4.7. Suppose ϕ, ψ and ϕ1 , . . . , ϕn are bounded ω-psh functions such that −M ≤
ϕ ≤ ψ ≤ 0 and −M ≤ ui ≤ 0, where M ≥ 1. Then
                Z                                  Z                1
                                                                   ϕ 2n
             0 ≤ (ψ − ϕ) MA(ϕ1 , . . . , ϕn ) ≤ 4M    (ψ − ϕ) MA( )       .
                                                                   2
22             SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

Proof. After regularizing we may assume that all functions involved are model functions.
Write, symbolically, T = (ω + ddc ϕ2 ) ∧ · · · ∧ (ω + ddc ϕn ). Then
           Z                               Z                    Z
             (ψ − ϕ) MA(ϕ1 , . . . , ϕn ) = (ψ − ϕ)ω ∧ T + (ψ − ϕ) ddc ϕ1 ∧ T.
         R
Since 0 ≤ (ψ − ϕ)ω ∧ T ≤ M , the ﬁrst term in the right-hand side satisﬁes
                     Z                      Z               1
                                          1                    2
                       (ψ − ϕ)ω ∧ T ≤ M 2       (ψ − ϕ)ω ∧ T     .

By the Cauchy-Schwarz inequality (Corollary 3.3), the second term is bounded by
                 Z                         1 Z                    1
                                             2                        2
                               c                             c
                    (ψ − ϕ) dd (ϕ − ψ) ∧ T          (−ϕ1 ) dd ϕ1 ∧ T
                                      R
By the assumption that −M ≤ u1 ≤ 0 and ω n = 1 we have
               Z                  Z          Z
           0 ≤ (−ϕ1 ) dd ϕ1 ∧ T = ϕ1 ω ∧ T − ϕ1 (ω + ddc ϕ1 ) ∧ T ≤ M.
                        c


Similarly,
       Z                      Z                        Z
  0 ≤ (ψ − ϕ) dd (ϕ − ψ) ∧ T = (ψ − ϕ)(ω + dd ϕ) ∧ T − (ψ − ϕ)(ω + ddc ψ) ∧ T
                c                            c

                              Z
                             ≤ (ψ − ϕ)(ω + ddc ϕ) ∧ T.

Putting this together, and using the concavity of the square root, we get
  Z
    (ψ − ϕ) MA(ϕ1 , . . . , ϕn ) ≤
                       Z                  1       Z                               1 !
                   1                        2                                          2
               M   2        (ψ − ϕ)ω ∧ T        +        (ψ − ϕ)(ω + ddc ϕ) ∧ T

                                                                        Z                              1
                                                                                            cϕ
                                                                    1                                    2
                                                             ≤ 2M   2        (ψ − ϕ)(ω + dd       )∧T        .
                                                                                              2
                                                         1
The lemma follows (with the constant 4M/(2M ) 2n < 4M ) by repeating this argument n − 1
times, successively replacing ϕ2 , . . . , ϕn by ϕ/2.                                 
Proof of Proposition 4.3. Let (ϕj )j be a decreasing net of ω-psh model functions converging
to ϕ. We may assume that −M ≤ ϕj ≤ 0 for all j, where M ≥ 1. For any ω-psh function
ψ with −1 ≤ ψ ≤ 0 it follows from Lemma 4.7 that
                       Z                          Z                 1
                                                                   ϕ 2n
                   0 ≤ (ϕj − ϕ) MA(ψ) ≤ 4M            (ϕj − ϕ) MA( )
                                                                   2
and the right hand side tends to zero as j → ∞ by Theorem 3.1. It therefore follows from
the deﬁnition of the capacity and from Chebyshev’s inequality that for each integer m ≥ 1
                                                          1
there exists jmSsuch that the open set Gm := {ϕjm − ϕ > m   } has capacity 2−m ε. We can
then set G := m Gm and ϕm := ϕjm .                                                     
                  SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                            23

Proof of Proposition 4.5. As above let (ϕj )j be a decreasing net of ω-psh model functions
converging to ϕ. After adding a constant we may assume that ϕj ≤ 0 for all j. For
each integer m ≥ 1, the net (max{ϕj , −m})j decreases to the bounded ω-psh function
max{ϕ, −m}. We can therefore choose jm such that
          Z                                                     
                                                    max{ϕ, −m}              n+1
      0 ≤ (max{ϕjm , −m} − max{ϕ, −m}) MA                          ≤ (2m)−2 .        (4.1)
                                                          2
We may further assume jm+1 ≥ jm for all m. Set ϕm := ϕjm . We claim that the decreasing
sequence (ϕm )∞
              m=1 converges to ϕ. By Theorem 2.10 it suﬃces to test this at any divisorial
point x ∈ X. We have 0 ≥ ϕ(x) > −∞ and ϕm (x) ≥ ϕ(x) ≥ −m for m ≥ −ϕ(x) ≥ 0.
By (4.1), Lemma 4.7 and the deﬁnition of capacity we get
                                                             1
                            0 ≤ (ϕm (x) − ϕ(x)) Capω {x} ≤
                                                             m
for m ≥ |ϕ(x)|. Now Capω {x} > 0 by Lemma 4.2, thus ϕm (x) converges to ϕ(x), which
concludes the proof.                                                                    

                       5. Locality and the comparison principle
   Let ω be a form as in §4 with {ω}n = 1. In this section we prove the following analogue
of [BT87, Proposition 4.2].
Theorem 5.1. If ϕ and ψ are bounded ω-psh functions, then
                          1{ϕ>ψ} MA(max{ϕ, ψ}) = 1{ϕ>ψ} MA(ϕ).                              (5.1)
  A ﬁrst consequence is the fact that our operator MA is local in nature, something that is
not an immediate consequence of our deﬁnition in §3.
Corollary 5.2. Suppose ϕ, ψ are bounded ω-psh functions that agree on an open set G ⊆ X.
Then MA(ϕ) = MA(ψ) on G.
Proof. Given ε > 0 we apply Theorem 5.1 to ϕ + ε and ψ. This gives MA(max{ϕ + ε, ψ}) =
MA(ϕ) on G ⊆ {ϕ+ε > ψ}. Letting ε → 0 and using Theorem 3.1 we get MA(max{ϕ, ψ}) =
MA(ϕ) on G. Exchanging the roles of ϕ and ψ shows that MA(ϕ) = MA(ψ) on G.           
  Another key consequence of Theorem 5.1 is the comparison principle:
Corollary 5.3. If ϕ and ψ are bounded ω-psh functions, then
                              Z              Z
                                  MA(ψ) ≤        MA(ϕ).
                              {ϕ<ψ}             {ϕ<ψ}

Proof. As in [GZ07, Theorem 1.5] the result easily follows from the locality property by
integration. More precisely, for any ε > 0 we have
      Z                             Z                          Z
  1 = MA(max{ϕ, ψ − ε}) ≥                MA(max{ϕ, ψ − ε}) +        MA(max{ϕ, ψ − ε})
                                {ϕ<ψ−ε}                            {ϕ>ψ−ε}
              Z                      Z                   Z                       Z
      (5.1)
       =             MA(ψ − ε) +             MA(ϕ) =             MA(ψ) + 1 −             MA(ϕ),
           {ϕ<ψ−ε}                 {ϕ>ψ−ε}             {ϕ<ψ−ε}                 {ϕ≤ψ−ε}

so we obtain the desired estimate by letting ε → 0.                                               
24               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

     The rest of this section is devoted to the proof of Theorem 5.1. We shall use


## Literal published source 1201.0188: source-extracts/1201.0188-energy-E1-proof.txt


6.1. Energy of model functions. For any model function ϕ we set
                                    n Z
                               1 X
                     Eω (ϕ) =           ϕ(ω + ddc ϕ)j ∧ ω n−j                           (6.1)
                              n+1
                                        j=0
26               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

and call Eω (ϕ) the energy of ϕ. It follows formally from an integration by parts argument,
see Proposition 2.20 and [Tia00, Lemma 6.2] that if ϕ, ψ are any two model functions, then
                                       n Z
                                 1 X
            Eω (ψ) − Eω (ϕ) =               (ψ − ϕ)(ω + ddc ϕ)j ∧ (ω + ddc ψ)n−j .    (6.2)
                               n+1
                                      j=0

Writing ϕt = (1 − t)ϕ + tψ, and expanding Eω (ϕt ) − Eω (ϕ) in t leads to the following
formulas for ﬁrst and second derivatives of Eω :
                                                 Z
             ′                d
           Eω (ϕ) · (ψ − ϕ) =         Eω (ϕt ) = (ψ − ϕ) MA(ϕ);                    (6.3)
                              dt t=0+
                                                   Z
             ′′               d2
           Eω (ϕ) · (ψ − ϕ) = 2        Eω (ϕt ) = n (ψ − ϕ)ddc (ψ − ϕ) MA(ϕ).      (6.4)
                              dt t=0+
Proposition 6.1. The restriction of Eω to the convex set PSH(X, ω) ∩ D(X) is concave,
nondecreasing, and satisfies Eω (ϕ + c) = Eω (ϕ) + c for any constant c ∈ R.
Proof. Concavity follows from (6.4) and Proposition 2.21. Monotonicity is a consequence
of (6.3), and the last equation follows from (6.2) since (ω + ddc ϕ)j ∧ ω n−j is a probability
measure for each j thanks to Proposition 2.19 and the normalization {ω}n = 1.               
6.2. Energy of ω-psh functions. For a general ω-psh function ϕ we set
             Eω (ϕ) := inf {Eω (ψ) | ψ ∈ PSH(X, ω) ∩ D(X), ψ ≥ ϕ} ∈ [−∞, +∞[.
Proposition 6.2. The extension Eω : PSH(X, ω) → [−∞, +∞[ is non-decreasing, concave,
and satisfies Eω (ϕ + c) = Eω (ϕ) + c for any c ∈ R. It is also upper semicontinuous, and
continuous along decreasing nets
Proof. That Eω is nondecreasing, concave and satisﬁes Eω (ϕ + c) = Eω (ϕ) + c follows
formally from Proposition 6.1 (using that PSH(X, ω) ∩ D(X) is convex and invariant under
addition of a constant).
   Upper semicontinuity is also a direct consequence of these algebraic properties of Eω and
of Theorem 2.10. Indeed, pick ϕ0 ∈ PSH(X, ω) and t ∈ R such that Eω (ϕ0 ) < t. We need
to show that Eω (ϕ) < t for ϕ in a neighborhood U of ϕ0 in PSH(X, ω). By deﬁnition, there
exists ψ0 ∈ PSH(X, ω) ∩ D(X) such that ψ0 ≥ ϕ0 and Eω (ψ0 ) < t − ε for some ε > 0. By
Theorem 2.10, U := {ϕ ∈ PSH(X, ω) | supX (ϕ − ψ0 ) < ε} is an open neighborhood of ϕ0
in PSH(X, ω). By (6.2) we have Eω (ϕ) ≤ Eω (ψ0 ) + ε < t for all ϕ ∈ U , which proves upper
semicontinuity.
   Finally, being usc and nondecreasing, Eω is automatically continuous along decreasing
nets.                                                                                      
Proposition 6.3. Formulas (6.1)-(6.4) are valid for bounded ω-psh functions.
     This follows from the continuity of Eω along decreasing nets and from Theorem 3.1.
6.3. Non-pluripolar Monge-Ampère measures. Let us introduce the class of ω-psh
functions with ﬁnite energy
                        E 1 (X, ω) := {ϕ ∈ PSH(X, ω) | Eω (ϕ) > −∞} .
This is a convex set which contains all bounded ω-psh functions.
                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                       27

    In this section and its sequel, we explain how to extend the Monge-Ampère operator to
E 1 (X, ω) and prove that its basic properties continue to hold in this more general setting.
    Consider an arbitrary ω-psh function ϕ. In the sequel we shall use the notation
                                    ϕhti := max{ϕ, −t}.
Note that for s > t ≥ 1, {ϕ > −t} = {ϕhsi > −t} and max{ϕhsi , −t} = ϕhti ; hence
Theorem 5.1 implies
   1{ϕ>−t} MA(ϕhsi ) = 1{ϕhsi >−t} MA(ϕhsi ) = 1{ϕhsi >−t} MA(ϕhti ) = 1{ϕ>−t} MA(ϕhti ).
  This equation allows us to introduce
Definition 6.4. [BT87, GZ07] The non-pluripolar Monge-Ampère measure MA(ϕ) of any
ω-psh function ϕ is the increasing limit of the measures 1{ϕ>−t} MA(ϕhti ) as t → ∞.
  Here the limit exists in a very strong sense: we have
                           lim 1{ϕ>−t} MA(ϕhti )(E) = MA(ϕ)(E)                          (6.5)
                          t→∞
for any Borel set E.
Remark 6.5. The terminology ”non-pluripolar” comes from the fact that MA(ϕ) does not
put mass on pluripolar sets. This in turn follows from Proposition 3.7 applied to the bounded
ω-psh function ϕhti and from (6.5).
  The measure MA(ϕ) is always deﬁned and supported on the set {ϕ > −∞}, but its total
mass may be strictly less than one.
Definition 6.6. A ω-psh function ϕ has full Monge-Ampère mass when MA(ϕ) is a prob-
ability measure.
  This is the case iﬀ MA(ϕhti ){ϕ ≤ −t} → 0 as t → ∞, and implies that MA(ϕhti ) converges
weakly to MA(ϕ).
Lemma 6.7. If ϕ ∈ E 1 (X, ω), then MA(ϕhti ){ϕ ≤ −t} = o(t−1 ) as t → ∞; hence ϕ has
full Monge-Ampère mass.
Proof. We may assume ϕ ≤ 0. Set µt := MA(ϕhti ). Since (6.2) applies to bounded ω-psh
functions by Proposition 6.3, we get
                                  Z                          Z t/2 n                  o
                               1                          1
  Eω (ϕht/2i ) − Eω (ϕhti ) ≥       (ϕht/2i − ϕhti )µt =          µt ϕht/2i − ϕhti ≥ s ds
                              n+1                        n+1 0
                                  Z t/2 n                    o
                               1                                        t
                            ≥          µt ϕht/2i − ϕhti ≥ t/2 ds =           µt {ϕ ≤ −t} ,
                              n+1 0                                 2(n + 1)
where µt = MA(ϕhti ). Since limt→∞ Eω (ϕht/2i ) = limt→∞ Eω (ϕhti ) = Eω (ϕ) by the continu-
ity of Eω along decreasing sequences, the proof is complete.                              
Lemma 6.8. If 0 ≥ ϕ ∈ E 1 (X, ω) and f ∈ D(X), then
                Z                Z
                           hti                 2(n + 1)
                  f MA(ϕ ) − f MA(ϕ) ≤                  |Eω (ϕ)| sup |f |
                                                   t              X
for any t > 0.
28              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

Proof. We may assume supX |f | = 1. Pick s ≥ t. The probability measures µt := MA(ϕhti )
and µs agree on {ϕ > −t}. Hence
   Z        Z                                Z               Z            
                                          1          hti             hsi
      f µt − f µs ≤ (µt + µs ){ϕ ≤ −t} ≤          −ϕ µt + −ϕ µs
                                          t
                                       n+1                                  2(n + 1)
                                     ≤      (|Eω (ϕhti )| + |Eω (ϕhsi )|) ≤          |Eω (ϕ)|.
                                        t                                       t
The result follows by letting s → ∞.                                                           
Proposition 6.9. If ϕ ∈ E 1 (X, ω) and (ϕj )j is a decreasing net of ω-psh functions converg-
ing to ϕ, then ϕj ∈ E 1 (X, ω) for all j and MA(ϕj ) → MA(ϕ) as j → ∞ in the weak sense
of measures.
                                                        R              R
Proof. Given f ∈ D(X), we have by deﬁnition that f MA(ϕhti ) → f MA(ϕ) as t → ∞
     R         hti    R
and f MA(ϕj ) → f MA(ϕj ) as t → ∞ for every j. Moreover, Lemma 6.8 shows that
                                                                R        hti    R
the latter convergence is uniform in j. Since for each t we have f MA(ϕj ) → f MA(ϕhti )
as j → ∞ by Theorem 3.1, the result follows.                                               
Lemma 6.10. If ϕ, ψ ∈ E 1 (X, ω) and ϕ, ψ ≤ 0, then we have the estimate
                                                 Z
                                ϕ+ψ        2−(n+1)
                    −∞ < E               ≤           (−ψ) MA(ϕ).
                                  2         n+1
Proof. Pick s, t > 0. Since (6.1) holds for bounded ω-psh functions, we see using (3.1) that
                                                   !           Z
                        ϕ+ψ             ϕhti + ψ hsi     2−(n+1)
            −∞ < E               ≤E                    ≤           ψ hsi MA(ϕhti ).
                           2                 2            n+1
Since ψ hsi decreases to ψ at any point of X, the right hand side converges to
              Z                         Z                             Z
     2−(n+1)             hti    2−(n+1)                 hti   2−(n+1)
                 ψ MA(ϕ ) ≤                     ψ MA(ϕ ) =                     ψ MA(ϕ)
      n+1                        n + 1 {ϕ>−t}                  n + 1 {ϕ>−t}
by monotone convergence. We obtain the desired estimate by letting t → ∞.                     
6.4. Locality and the comparison principle.
Proposition 6.11. For any ϕ, ψ ∈ E 1 (X, ω), we have
                          1{ϕ>ψ} MA(max{ϕ, ψ}) = 1{ϕ>ψ} MA(ϕ),                             (6.6)
and the comparison principle holds:
                             Z                    Z
                                        MA(ψ) ≤               MA(ϕ).                       (6.7)
                                {ϕ<ψ}                 {ϕ<ψ}

Proof. To prove (6.6), ﬁrst assume ψ = −t, where t ≥ 1. Pick s ≥ t so that ϕhti =
max{ϕs , −t}, {ϕ > −t} = {ϕs > −t}, and
 1{ϕ>−t} MA(ϕhti ) = 1{ϕs >−t} MA(ϕhti ) = 1{ϕs >−t} MA(ϕs ) = 1{ϕ>−t} · 1{ϕ>−s} MA(ϕs ),
where the second equality follows from Theorem 5.1. As s → ∞, 1{ϕ>−s} MA(ϕs )(E) →
MA(ϕ)(E) for any Borel set E, so the right hand side of the equation above converges to
1{ϕ>−t} MA(ϕ).
                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                29

  Now consider ϕ, ψ ∈ E 1 (X, ω) and set u = max{ϕ, ψ} ∈ E 1 (X, ω). Then
     • 1{ϕhti >ψhti } MA(u) = 1{ϕhti >ψhti } MA(uhti ) since {ϕhti > ψ hti } ⊆ {u > −t};
     • 1{ϕhti >ψhti } MA(uhti ) = 1{ϕhti >ψhti } MA(ϕhti ) by (5.1) applied to ϕhti and ψ, noticing
       the inclusion {ϕhti > ψ hti } ⊆ {ϕhti > ψ};
     • 1{ϕhti >ψhti } MA(ϕhti ) = 1{ϕhti >ψhti } MA(ϕ) by the previous step and the inclusion
       {ϕhti > ψ hti } ⊆ {ϕhti > −t}.
To summarize, we get
                             1{ϕhti >ψhti } MA(u) = 1{ϕhti >ψhti } MA(ϕ).                         (6.8)
Now
                 1{ϕhti >ψhti } MA(u) = 1{ϕ>−t≥ψ} MA(u) + 1{ϕ>ψ>−t} MA(u)
As t → ∞ the ﬁrst term tends to 0 since MA(u) puts no mass on the pluripolar set {ψ = −∞}
(see Remark 6.5), and the second term converges to 1{ϕ>ψ>−∞} MA(u) = 1{ϕ>ψ} MA(u).
   Thus the left-hand side of (6.8) tends to 1{ϕ>ψ} MA(u) as t → ∞. Similarly, the right-
hand side tends to 1{ϕ>ψ} MA(ϕ). Finally the comparison principle follows exactly as in the
proof of Corollary 5.3. The proof is complete.                                           
6.5. Differentiability.
Proposition 6.12. For any ϕ, ψ ∈ E 1 (X, ω), the function t 7→ Eω ((1 − t)ϕ + tψ) is differ-
entiable on [0, 1], and we have
                                                             Z
                ′                d
             Eω (ϕ) · (ψ − ϕ) :=         Eω ((1 − t)ϕ + tψ) = (ψ − ϕ) MA(ϕ)           (6.9)
                                 dt t=0+
for any ϕ, ψ ∈ E 1 (X, ω).
Proof. Set h(t) := hϕ,ψ (t) := Eω ((1 − t)ϕ + tψ) for 0 ≤ t ≤ 1. Note that h is a polynomial
of degree at most n when ϕ and ψ are model functions. By continuity of the energy along
decreasing nets, the same is true in general. In particular, h is diﬀerentiable on [0, 1].
   Pick any decreasing sequence (ψj )∞j=1 of ω-psh model functions converging to ψ. Note that
                                                                     d
hϕhsi ,ψj → hϕ,ψ as polynomials when s → ∞ and j → ∞, hence dt              h
                                                                       t=0+ ϕhsi ,ψj
                                                                                     → h′ (0+).
Since (6.9) holds true for bounded functions by Proposition 6.3, it suﬃces to show
                              Z                         Z
                                        hsi       hsi
                    lim lim (ψj − ϕ ) MA(ϕ ) = (ψ − ϕ) MA(ϕ).
                     j→∞ s→∞

First, we have
             Z                           Z                                 Z
                  hsi         hsi                               hsi
                 ϕ      MA(ϕ        )=                (−s) MA(ϕ       )+            ϕ MA(ϕhsi )
                                             {ϕ≤−s}                        {ϕ>−s}
                                         Z                                 Z
                                    =                 (−s) MA(ϕhsi ) +              ϕ MA(ϕ)
                                             {ϕ≤−s}                        {ϕ>−s}

by (6.6). By LemmaR 6.7 the ﬁrst term of the right hand side tends to 0, and the second
term converges to ϕ MA(ϕ) since MA(ϕ) puts no mass on {ϕ = −∞}.
                                     R                R
   Second, for ﬁxed j we have lims→∞ R ψj MA(ϕhsi ) R= ψj MA(ϕ) since ψj is continuous.
   Finally, Lemma 2.23 yields limj→∞ ψj MA(ϕ) = ψ MA(ϕ), completing the proof. 
30              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

                           7. Envelopes and differentiability
   Let ω be a form as in §4 with {ω}n = 1. As explained in the introduction, the diﬀerentia-
bility of the energy is not a priori suﬃcient to make the variational approach work, i.e. to
infer that a maximizer of the relevant functional over E 1 (X, ω) is necessarily a critical point.


## Literal published source 1201.0188: source-extracts/1201.0188-envelope-derivative-proof.txt

infer that a maximizer of the relevant functional over E 1 (X, ω) is necessarily a critical point.
In order to circumvent this diﬃculty, we show as in [BB10] the diﬀerentiability of Eω ◦ Pω ,
where Pω is the ω-psh envelope operator of §2.5. This idea was originally introduced by
Alexandrov [Ale38] in the context of real Monge-Ampère equations.
Definition 7.1. We say that ω has the orthogonality property if
                            Z
                              (f − Pω (f )) MA(Pω (f )) = 0

holds for every f ∈ C 0 (X).
   Since Pω (f ) ≤ f , this property means that MA(Pω (f )) is concentrated on the contact
locus {Pω (f ) = f }. We refer to Appendix A for more information on the orthogonality
property.
   We can state the main result of this section.
Theorem 7.2. Assume that ω has the orthogonality property. Then the composition Eω ◦
Pω : C 0 (X) → R is Gâteaux differentiable, with directional derivatives given by
                                                   Z
                          d
                                Eω ◦ Pω (f + tg) = g MA(Pω (f )).
                         dt t=0
  Before giving a proof of this crucial result, we state and prove a corollary of it that we
shall need when solving the Monge-Ampère equation.
  If ϕ ∈ PSH(X, ω) and f ∈ C 0 (X), observe that Pω (ϕ + f ) is ω-psh (i.e. is not identically
−∞) since ϕ+f dominates the ω-psh function ϕ+inf X f . Furthermore we have Pω (ϕ+f ) ≤
ϕ + f since the latter is usc.
Corollary 7.3. Assume that ω has the orthogonality property. Let ϕ ∈ E 1 (X, ω) and f ∈
C 0 (X). Then Pω (ϕ + tf ) ∈ E 1 (X, ω) for all t ∈ R and
                                                       Z
                            d
                                   Eω ◦ Pω (ϕ + tf ) = f MA(ϕ).
                            dt t=0
Proof. Note that ϕ + tf ≥ ϕ − |t| supX |f | implies Pω (ϕ + tf ) ≥ ϕ − |t| supX |f |, hence
Pω (ϕ + tf ) ∈ E 1 (X, ω) for all t. We are going to show that
                                                Z t Z                    
                  Eω ◦ Pω (ϕ + tf ) = Eω (ϕ) +          f MA(Pω (ϕ + sf )) ds.         (7.1)
                                                0
For all t ∈ R. If ϕ is continuous, then the result follows immediately from Theorem 7.2.
   In general, let (ϕm )∞
                        m=1 be a decreasing sequence of ω-psh model functions converging to
ϕ, see Proposition 4.5.
   For each t ∈ R the sequence (Pω (ϕm +tf ))∞m=1 is a decreasing sequence of ω-psh functions,
and we claim that limm Pω (ϕm + tf ) = Pω (ϕ + tf ). Indeed let ϕ̃t = limm Pω (ϕm + tf ). Since
ϕm + tf ≥ ϕ + tf , we have Pω (ϕm + tf ) ≥ Pω (ϕ + tf ), hence ϕ̃t ≥ Pω (ϕ + tf ). Conversely,
ϕ̃t ≤ Pω (ϕm + tf ) ≤ ϕm + tf for all m, hence ϕ̃t ≤ ϕ + tf and it follows ϕ̃t = Pω (ϕ + tf )
as required.
                SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                   31

  We apply (7.1) to ϕm :
                                                Z t Z                      
              Eω (Pω (ϕm + tf )) = Eω (ϕm ) +            f MA(Pω (ϕm + sf )) ds.               (7.2)
                                                 0
As m → ∞, Eω (Pω (ϕm +tf    R )) and Eω (ϕm ) decrease to Eω ◦Pω (ϕ+tf
                                                                  R    ) and Eω (ϕ), respectively
and by Proposition 6.9, f MA(Pω (ϕm + sf )) converges to f MA(Pω (ϕ + sf )) for each
s.R Finally (7.1) follows from (7.2) using dominated convergence in view of the upper bound
| f MA(Pω (ϕm + sf ))| ≤ supX |f | for all m and all s.                                        
Proof of Theorem 7.2. We follow the exposition in [BB10, §4.3] very closely. Arguing as in
Corollary 7.3 we may assume that f, g ∈ D(X). Set µ := MA(Pω (f )). We need to prove
that                                                  Z
                            d
                                    Eω ◦ Pω (f + tg) = g µ.                          (7.3)
                            dt t=0+
As a ﬁrst step, we linearize the problem and prove that
                                                        Z
                      d                         d
                             Eω ◦ Pω (f + tg) =           Pω (f + tg) µ.                       (7.4)
                     dt t=0+                    dt t=0+
Denote the left and right hand sides of (7.4) by a and b, respectively. Note that the one-sided
derivatives exist since both Eω and Pω are concave.
  Since Eω is concave on the space of bounded ω-psh functions, the function
                    [0, 1] ∋ s 7→ h(s) := Eω (sPω (f + tg) + (1 − s)Pω (f ))
is also concave, hence

  Eω (sPω (f + tg) + (1 − s)Pω (f )) ≤
                                                                   Z                              
                                     d
                      Eω ◦ Pω (f ) +        h = Eω ◦ Pω (f ) + s        (Pω (f + tg) − Pω (f ))µ
                                     dt t=0
by Proposition 6.3. Taking s = 1 and letting t → 0 yields a ≤ b.
  To prove the reverse inequality, ﬁx ε > 0. Then there exists δ > 0 such that
                           Z                   Z
                      D :=     Pω (f + δg)µ −    Pω (f )µ ≥ δ(b − ε).
                               X                     X
Since µ is the diﬀerential of Eω , there exists γ > 0 such that
    E ((1 − t)Pω (f ) + tPω (f + δg)) ≥ Eω (Pω (f )) + t(D − δε) ≥ Eω (Pω (f )) + tδ(b − 2ε)
for 0 ≤ t ≤ γ. The concavity of P yields Pω (f + tδg) ≥ (1 − t)Pω (f ) + tPω (f + δg). Since
Eω is non-decreasing we get
        Eω ◦ Pω (f + tδg) ≥ E ((1 − t)Pω (f ) + tPω (f + δg)) ≥ E(Pω (f )) + tδ(b − 2ε)
for 0 ≤ t ≤ γ. Letting t → 0 and ε → 0 we conclude a ≥ b. This shows that (7.4) holds.
   In view of (7.4) it remains to show that
                          Z                                Z
                             (Pω (f + tg) − Pω (f )) µ = t   gµ + o(t)              (7.5)
                           X                                X
as t → 0+.
32              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

  Since Pω (f ) ≤ f , the orthogonality property implies Pω (f ) = f for µ-a.e. point. We thus
have Pω (f + tg) ≤ f + tg = Pω (f ) + tg µ-a.e. We claim that µ(Ωt ) = O(t) with
                              Ωt := {Pω (f + tg) < Pω (f ) + tg}.
Observe that |Pω (f + tg) − Pω (f )| ≤ t sup |g| so that the claim implies
  Z
     (Pω (f + tg) − Pω (f ) − tg)µ
   X
                   Z                               Z
                =      (Pω (f + tg) − Pω (f ))µ +         (Pω (f + tg) − Pω (f ))µ
                    Ωt                               X\Ωt
                             Z                                   Z
                          =       (Pω (f + tg) − Pω (f ) − tg) +    tg µ
                               Ωt                                 X
                             Z                                                    Z
                         ≤ t g µ + µ(Ωt ) sup |Pω (f + tg) − Pω (f ) − tg| = t g µ + O(t2 )
                              X              X                                   X

which proves (7.5).
  The estimate of µ(Ωt ) is based on the comparison principle. Since g is a model function,
there exists C ≫ 1, ψ ∈ D(X) such that ψ and ψ + g are Cω-psh by Proposition 2.6. Note
that Ωt = {Pω (f + tg) + tψ < Pω (f ) + t(ψ + g)}, and both functions Pω (f + tg) + tψ and
Pω (f ) + t(ψ + g) are (1 + Ct)ω-psh. The comparison principle then yields
   Z                                            Z
                        c                    n
        ((1 + Ct)ω + dd (Pω (f ) + t(ψ + g))) ≤    ((1 + Ct)ω + ddc (Pω (f + tg) + tψ))n
      Ωt                                              Ωt

By expanding as polynomials in t, we get
              ((1 + Ct)ω + ddc (Pω (f ) + t(ψ + g)))n = (ω + ddc Pω (f ))n + O(t)
and
           ((1 + Ct)ω + ddc (Pω (f + tg) + tψ))n = (ω + ddc Pω (f + tg))n + O(t).
From these three estimates we conclude
                          Z                Z
                 µ(Ωt ) =    MA(Pω (f )) ≤            MA(Pω (f + tg)) + O(t).
                             Ωt                  Ωt

But Ωt ⊆ {Pω (f + tg) < f + tg}, so the orthogonality property implies that the last integral
vanishes. This concludes the proof.                                                        
Remark 7.4. Observe that the differentiability property of Theorem 7.2 conversely implies
the orthogonality
      R             property. Indeed, pick f ∈ C 0R(X) and set g := Pω (f ) − f . We claim
that g MA(Pω (f )) = 0. It is enough to prove g MA(Pω (f )) ≥ 0 since g ≤ 0. Now the
differentiability property yields
                                                      Z
                   Eω (Pω (f + εg)) = Eω (Pω (f )) + ε g MA(Pω (f )) + o(ε).

But we have
               f + εg = (1 − ε)f + εPω (f ) ≥ (1 − ε)Pω (f ) + εPω (f ) = Pω (f ),
hence Eω (Pω (f + εg)) ≥ Eω (Pω (f )) by monotonicity of Eω , and the result follows.
               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                         33



## Literal published source 1201.0188: source-extracts/1201.0188-uniqueness-existence-proof.txt

                             8. The Monge-Ampère equation
  In this section we prove
Theorem 8.1. Assume that ω is a form as in §4 with {ω}n = 1 that satisfies the orthog-
onality property (see Definition 7.1). Let µ be a probability measure on X supported on
the dual complex of some SNC model of X. Then there exists a unique, continuous ω-psh
function ϕ ∈ PSH(X, ω) such that MA(ϕ) = µ, and sup ϕ = 0.
   Let us explain how to deduce Theorems A and A’ from the introduction. Let ω be any
closed semipositive form with {ω} ample, and µ be a positive Radon measure of mass {ω}n .
Set ω̃ := ω/({ω}n )1/n , and µ̃ = µ/{ω}n . Assume that X is algebraizable. It follows from
Appendix A that ω and ω̃ satisfy the orthogonality property. Applying Theorem 8.1 to ω̃
and µ̃ yields a unique ϕ̃ ∈ PSH(X, ω̃) such that sup ϕ̃ = 0 and (ω̃ + ddc ϕ̃)n = µ̃. Theorem
A’ follows since (ω + ddc ϕ)n = µ with ϕ = ({ω}n )1/n ϕ̃.
   Now consider an ample line bundle L → X endowed with a semipositive model metric
k · k. The curvature form ω = c1 (L, k · k) is semipositive and {ω}n = c1 (L)n in view
of Proposition 2.19 and (2.1). Given any positive Radon measure µ of mass c1 (L)n and
supported on the dual complex of some SNC model of X, Theorem A’ thus implies the
existence of a unique continuous ω-psh function ϕ such that MA(ϕ) = µ, and sup ϕ = 0.
This statement implies Theorem A since c1 (L, k · ke−ϕ )n = MA(ϕ) by deﬁnition.
  For the rest of this section is a form as in §4 normalized by {ω}n = 1

8.1. Uniqueness. The uniqueness statement in Theorem 8.1 does not require the orthog-
onality property. Following [Blo03] as in [GZ07, YZ10], one actually proves:
Proposition 8.2. Let ω be any semipositive closed (1, 1) form. Suppose MA(ϕ) = MA(ψ)
for any two functions ϕ, ψ ∈ E 1 (X, ω). Then ϕ − ψ is constant.
Proof. For simplicity we write ωϕ = ω + ddc ϕ.
   First we brieﬂy indicate how to extend to ω-psh of ﬁnite energy the calculus that we
developed in §3. Let ϕ, ψ ∈ E 1 (X, ω). Since Eω is convex, (1 − t)ϕ + tψ ∈ E 1 (X, ω) for any
t ∈ [0, 1]. For any 0 ≤ i ≤ n, deﬁne ωϕi ∧ ωψn−i to be the unique probability measure such
that
  X n 
  n−1
            (1 − t)k tn−k ωϕk ∧ ωψn−k = MA((1 − t)ϕ + tψ) − (1 − t)n MA(ϕ) − tn MA(ψ) (8.1)
        k
 k=0

for any t = j/n with 1 ≤ j ≤ n − 1. By Proposition 6.9, we get ωϕi j ∧ ωψn−i
                                                                          j
                                                                             → ωϕi ∧ ωψn−i for
any decreasing sequence of ω-psh functions ϕj → ϕ and ψj → ψ. In particular, ωϕi ∧ ωψn−i is
a probability measure. Replacing MA(·) = (ω + ddc ·)n by (ω + ddc ·)i+j ∧ ω n−(i+j) in (8.1),
we can further deﬁne probability measures of the same mass ωϕi ∧ ωψj ∧ ω n−(i+j) as soon as
i, j ≥ 0 and i + j ≤ n.
    Observe that by deﬁnition and Lemma 6.10, these measures integrate ω-psh functions of
ﬁnite energy. By continuity, it also follows that the Cauchy-Schwarz inequality holds
                   Z                Z              1/2 Z           1/2
                          c                  c                 c
                     −hdd g ∧ T ≤         hdd h ∧ T         gdd g ∧ T
34              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

for any h, g lying in the vector space generated by E 1 (X, ω) and for any T a positive linear
combination of measures of the type ωϕi ∧ ωψj ∧ ω n−(i+j) with i + j ≤ n and ϕ, ψ ∈ E 1 (X, ω).
     Now pick ϕ, ψ ∈ E 1 (X, ω). We claim that
            Z                                  Z                       21−n
                          c           n−1
              (ϕ − ψ)dd (ϕ − ψ) ∧ ω       ≤C      (ψ − ϕ)(MA(ϕ) − MA(ψ))                   (8.2)

for some constant C depending on ϕ and ψ.
   Grant this claim, and suppose MA(ϕ) = MA(ψ). We conclude the proof as in [YZ10].
We may assume sup ϕ = sup ψ. By Cauchy-Schwarz inequality, for any model function h we
get
           Z                               Z                            1/2
              (ϕ − ψ)ddc h ∧ ω n−1 ≤ D 1/2   (ϕ − ψ)ddc (ϕ − ψ) ∧ ω n−1     =0,
                R
with 0 ≤ D := −hddc h ∧ ω n−1 < +∞. Let L be any R-line bundle in a model X whose
numericalPclass is equal to ω. The above equality
                                            P     applied to the model function determined
in X by E bE (ϕ − ψ)(ordE )E with X0 =        bE E yields
                                                    !2
                             X
                                 bE (ϕ − ψ)(ordE )E    · Ln−1 = 0
                               E
                        P
which in turn implies E bE (ϕ − ψ)(ordE )E to be proportional to X0 by [YZ10, Theorem
2.1.1(b)]. Since we normalized ϕ, ψ by sup ϕ = sup ψ, we conclude that ϕ = ψ on the
vertices of ∆X .
   Now consider any (suﬃciently) high model π : X ′ → X . By [BFJ11, Proposition 5.2]
there exists a model function h such that ω ′ = ω + ddc h is induced by a ample divisor in X ′ .
Then the functions ϕ − h and ψ − h are both ω ′ -psh, normalized by sup(ϕ − h) = sup(ψ − h),
and satisfy (ω ′ + ddc (ϕ − h))n = (ω ′ + ddc (ψ − h))n . By what precedes we get ϕ = ψ on the
vertices of X ′ . This implies ϕ = ψ on X div , hence on X qm by Proposition 2.8, hence on X
since ϕ = supX ϕ ◦ pX for any ω-psh function by [BFJ11, Proposition 7.6].
   We now prove the claim. For this we reproduce the argument of [Blo03]. By C we will
denote possibly diﬀerent constants depending on ω, ϕ, ψ. Set ρ = ϕ−ψ. For k = 0, 1, ..., n−1
we will prove inductively that
                                 Z
                                                                   −k
                            0 ≤ −ρddc ρ ∧ ωϕi ∧ ωψj ∧ ω k ≤ Ca2

where                   Z                                  Z
                   a=       (ψ − ϕ)(MA(ϕ) − MA(ψ)) =           −ρddc ρ ∧ T ≥ 0
          Pn−1 l
with T = l=0     ωϕ ∧ ωψn−1−l , and i, j are such that i + j + k = n − 1. For k = n − 1 we will
then obtain the desired estimate.
  If k = 0, then           Z                        Z
                               ρddc ρ ∧ ωϕi ∧ ωψj ≤    ρddc ρ ∧ T = a

Assume that (3.1) holds for 0, 1, ..., k − 1. We have
                             ωϕi ∧ ωψj ∧ ω k = ωϕi+k ∧ ωψj − ddc ϕ ∧ α
                 SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                        35

where
                                                                 k−1
                                                                 X
                                             α = ωϕi ∧ ωψj ∧           ωϕl ∧ ω k−1−l
                                                                 l=0
Therefore
                 Z                                         Z
            0≤       −ρdd ρ ∧ ωϕi ∧ ωψj ∧ ω k ≤
                                c
                                                           −ρddc ρ ∧ (T − ddc ϕ ∧ α)
                                                           Z             Z
                                                        = − ρdd ρ ∧ T − ρddc ϕ ∧ α ∧ ddc ρ
                                                               c


This means that
                            Z                                               Z
                     0≤             −ρdd ρ ∧ ωϕi ∧ ωψj ∧ ω k ≤ a −
                                         c
                                                                                  ρddc ϕ ∧ α ∧ ddc ρ.

We have
                Z                                   Z                                Z
                        c                     c              c
            −        ρdd ϕ ∧ α ∧ dd ρ ≤                 ρdd ϕ ∧ α ∧ ωϕ +                 ρddc ϕ ∧ α ∧ ωψ .

If η is equal to ϕ or ψ, the Cauchy-Schwarz inequality gives
            Z                    Z                 1/2 Z                 1/2
                  c                     c                       c
               ρdd ϕ ∧ α ∧ ωη ≤      ρdd ρ ∧ α ∧ ωη          ϕdd ϕ ∧ α ∧ ωη
                                     R                  −(k−1)
By the Rinductive assumption, we have −ρddc ρ∧α∧ωη ≤ Ca2       , and since ϕ ∈ E 1 (X, ω)
we get −ϕddc ϕ ∧ α ∧ ωη < +∞. The proof is complete.                                   

8.2. Existence. As in [BBGZ09], the strategy is to ﬁrst use a variational argument going
back to Alexandrov [Ale38] in order to produce a solution ϕ ∈ E 1 (X, ω).
   Consider the functional Fµ : PSH(X, ω) → [−∞, +∞[ deﬁned by
                                                   Z
                                 Fµ (ϕ) := Eω (ϕ) − ϕµ.                             (8.3)

   We ﬁrst claim that FRµ is usc on PSH(X, ω). By Proposition 6.2, Eω is usc so that it is
suﬃcient to prove ϕ 7→ ϕµ is continuous on PSH(X, ω). Pick a net ϕk → ϕ in PSH(X, ω),
i.e. ϕk (x) → ϕ(x) for any x ∈ X div . Since divisorial points are dense in ∆X by [JM10],
and the family {ϕk |R∆X } is equicontinuous
                               R             by Theorem 2.9, it follows that ϕk |∆X → ϕ|∆X
uniformly. Whence ϕk µ → ϕµ since ∆X contains the support of µ by assumption.
   Now write PSH0 (X, ω) := {ϕ ∈ PSH(X, ω) | sup ϕ = 0}, and observe that Fµ (ϕ + c) =
Fµ (ϕ) for any constant c by Proposition 6.2, so that supPSH(X,ω) Fµ = supPSH0 (X,ω) Fµ . Since
Fµ is usc, and PSH0 (X, ω) is compact by Theorem 2.10, it actually attains its maximum.
We can thus ﬁnd ϕ ∈ PSH0 (X, ω) such that
                                                  Fµ (ϕ) =        sup      Fµ .
                                                             PSH(X,ω)

Clearly Eω (ϕ) > −∞, so ϕ ∈ E 1 (X, ω). Let us show that MA(ϕ) = µ. Pick any model
function f ≤ 0 on X. For t ∈ R, consider the function
                                                   Z
                         h(t) = Eω ◦ Pω (ϕ + tf ) − (ϕ + tf )µ.
36               SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

In view of Corollary 7.3, h(t) is diﬀerentiable at t = 0 with derivative
                                        Z               Z
                                  ′
                                 h (0) = f MA(ϕ) − f µ.

But since Pω (ϕ + tf ) ≤ ϕ + tf ≤ 0, it follows that h(t) ≤ Fµ ◦ Pω (ϕ + tf
                                                                         R ) ≤ FµR(ϕ) = h(0)
for all t. Thus h has a local maximum at t = 0, so h′ (0) = 0, that is f µ = f MA(ϕ).
This implies MA(ϕ) = µ, as f was an arbitrary model function.

8.3. Continuity. Finally we show that ϕ is continuous. For this we use capacity estimates
in the spirit of Kolodziej [Kol98, Kol03]; see also [EGZ09]. The following result (and its
proof) is a translation of [EGZ09, Lemma 2.3].


## Literal published source 1805.01016: source-extracts/1805.01016-title-and-scope.txt

                                              SPACES OF NORMS, DETERMINANT OF COHOMOLOGY AND
                                                 FEKETE POINTS IN NON-ARCHIMEDEAN GEOMETRY

                                                                  SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON
arXiv:1805.01016v3 [math.AG] 8 Jan 2021




                                                 Abstract. Let L be an ample line bundle on a (geometrically reduced) projective variety
                                                 X over any complete valued field. Our main result describes the leading asymptotics of
                                                 the determinant of cohomology of large powers of L, with respect to the supnorm of a
                                                 continuous metric on the Berkovich analytification of L. As a consequence, we establish
                                                 in this setting the existence of transfinite diameters and equidistribution of Fekete points,
                                                 following a strategy going back to Berman, Witt Nyström and the first author for complex
                                                 manifolds. In the non-Archimedean case, our approach relies on a version of the Knudsen–
                                                 Mumford expansion for the determinant of cohomology on models over the (possibly non-
                                                 Noetherian) valuation ring, as a replacement for the asymptotic expansion of Bergman
                                                 kernels in the complex case, and on the reduced fiber theorem, as a replacement for the
                                                 Bernstein–Markov inequalities. Along the way, a systematic study of spaces of norms and
                                                 the associated Fubini–Study type metrics is undertaken.




                                                                                        Contents
                                            Introduction                                                                                         2

                                          Part 1. Spaces of norms and determinants                                                                8
                                            1. Spaces of norms                                                                                    8
                                            2. Determinants and relative spectra                                                                 19
                                            3. Alternative metric structures on spaces of norms                                                  27

                                          Part 2. Models and metrics                                                                             31
                                            4. Analytification and models                                                                        31
                                            5. Fubini–Study metrics and model metrics                                                            37
                                            6. The supnorm of a metric                                                                           43
                                            7. Plurisubharmonic metrics and envelopes                                                            47

                                          Part 3. Asymptotics of relative volumes                                                                55
                                            8. Monge–Ampère measures and Deligne pairings                                                       55
                                            9. Asymptotics of relative volumes                                                                   68
                                            10. Transfinite diameter and Fekete points                                                           77
                                            Appendix A. Determinant of cohomology and Deligne pairings                                           84
                                            References                                                                                           96


                                            Date: January 11, 2021.
                                                                                              1
2                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

                                        Introduction
   Fekete points and transfinite diameter are classical notions in logarithmic potential theory
in the plane. For each m ∈ N, the m-diameter δm (K) of a compact subset K ⊂ C is defined
as the supremum of the geometric mean distance between m + 1 points in K, maximizers
being called Fekete configurations. The m-diameter of K admits a limit δ∞ (K) as m →
∞, called the transfinite diameter of K, which turns out to coincide with the logarithmic
capacity of K. Further, Fekete configurations become asymptotically unique in the limit, in
the sense that they equidistribute to a certain canonical probability measure on K, called
its equilibrium measure.
   In several complex variables, a similar picture was only rather recently obtained. The
first steps were taken by Leja in the 1950’s, introducing a notion of m-diameter δm (K) for
a compact subset K ⊂ Cn , defined in terms of the supremum of certain Vandermonde-
type determinants. The existence of the transfinite diameter δ∞ (K) = limm→∞ δm (K) was
established by Zaharjuta [Zah75], and the next key step came with Rumely’s observation
in [Rum07] that the general results in arithmetic intersection theory developed in [CLR03]
yield in particular an exact formula for δ∞ (K) in terms of pluripotential theory, generalizing
the classical Robin formula for the logarithmic capacity in the plane, and involving plurisub-
harmonic envelopes and mixed Monge–Ampère operators in the sense of Bedford–Taylor.
This triggered joint work of the first author with Berman and Witt Nyström [BB10, BBW11],
which built on Bergman kernel asymptotics to establish a general version of Rumely’s for-
mula in the setting of complex projective manifolds, and combined it with a variational
argument to prove the equidistribution of Fekete configurations in this context.
   The main purpose of the present paper is to study versions of these results in non-
Archimedean (Berkovich) geometry. While many results hold over an arbitrary non-Archimedean
complete valued field K, the full picture relies on more refined non-Archimedean pluripo-
tential theory as developed in [BFJ16, BFJ15, BG+16, BJ18a], and hence requires K to be
trivially or discretely valued and of residue characteristic 0.

Asymptotics of relative volumes. The Bouche–Catlin–Tian–Zelditch asymptotic expan-
sion of Bergman kernels [Bou90, Cat99, Tia90, Zel98] is a fundamental result in complex
geometry, which describes the asymptotic behavior of the L2 -norms associated to large ten-
sor powers of a positive Hermitian line bundle. As noticed in [BB10], it can be reformulated
as an asymptotic expansion for the logarithmic volume ratio of such L2 -norms, as follows.
   First, define the relative volume of any two norms k · k, k · k′ on an N -dimensional complex
vector space V as                                                      
                                                 ′           det k · k′
                                 vol(k · k, k · k ) := log                ,                 (0.1)
                                                              det k · k
                                                                                           V
where det k · k, det k · k′ denote the induced norms on the determinant line det V = N V .
In terms of the unit balls B, B ′ ⊂ V of the two norms,
                                                              
                                         ′     1       vol B
                         vol(k · k, k · k ) = log                + O(N log N ),
                                               2       vol B ′
where the error term O(N log N ) vanishes when the two norms are Hermitian.
  Let next X be an n-dimensional complex projective manifold. Every smooth, positively
curved metric φ on an (ample) line bundle L over X induces, for each m ∈ N, an L2 -norm


## Literal published source 1801.08229: source-extracts/1801.08229-title-and-standing.txt

                                           GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED
                                                                   FIELD

                                                                   SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON
arXiv:1801.08229v4 [math.AG] 22 Mar 2022




                                                  Dedicated to Ahmed Zeriahi for all his contributions to complex analysis and geometry


                                                Abstract. We develop global pluripotential theory in the setting of Berkovich geometry
                                                over a trivially valued field. Specifically, we define and study functions and measures of
                                                finite energy and the non-Archimedean Monge–Ampère operator on any (possibly reducible)
                                                projective variety. We also investigate the topology of the space of valuations of linear
                                                growth, and the behavior of psh functions thereon.
                                                   Nous développons une théorie du pluripotentiel global dans le contexte de la géométrie de
                                                Berkovich sur un corps trivialement valué. Plus précisément, nous définissons et étudions
                                                des fonctions et mesures d’énergie finie et un opérateur de Monge–Ampère non-archimédien
                                                sur toute variéte projective (éventuellement réductible). Nous explorons également la topolo-
                                                gie de l’espace des valuations à croissance linéaire, et le comportement des fonctions psh
                                                sur celui-ci.




                                                                                         Contents
                                           Introduction                                                                                               2
                                           1. Berkovich analytification and test configurations                                                      10
                                           2. Piecewise linear and Fubini–Study functions                                                            20
                                           3. Plurisubharmonic functions and energy pairing: the PL case                                             33
                                           4. Plurisubharmonic functions                                                                             44
                                           5. Envelopes and negligible sets                                                                          56
                                           6. Homogeneous functions and b-divisors                                                                   63
                                           7. Functions of finite energy and mixed Monge–Ampère measures                                            74
                                           8. Differentiability of the extended energy functional                                                    94
                                           9. Measures of finite energy                                                                              99
                                           10. The strong topology on M1                                                                            108
                                           11. Valuations of linear growth                                                                          114
                                           12. The strong topology on E 1 and the Calabi–Yau theorem                                                120
                                           13. Capacities, pluripolar sets, and negligible sets                                                     126
                                           Appendix A. Dual complexes and PL functions                                                              135
                                           Appendix B. The toric case                                                                               137
                                           References                                                                                               139



                                           Date: March 24, 2022.
                                                                                               1
2                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

                                        Introduction
   The main purpose of the present paper is to lay the foundations of pluripotential theory
in the setting of Berkovich geometry over a trivially valued field, paralleling as much as
possible the known theory in the complex analytic case.
   Pluripotential theory is a crucial tool in complex analysis and geometry, and A. Zeriahi has
been a central protagonist in the story of its development. For an excellent introduction, see
the book by V. Guedj and A. Zeriahi [GZ17]. This theory lies at the heart of the variational
approach to complex Monge–Ampère equations [BBGZ13], which proved particularly fruitful
in relation to Kähler–Einstein metrics, and ultimately led to a new proof of the Yau–Tian–
Donaldson (YTD) conjecture for Fano manifolds [BBJ21], later generalized to (log terminal)
Fano varieties [LTW19, Li19].
   There are several reasons for developing a corresponding theory over a trivially valued
field, that is, any field equipped with the trivial (non-Archimedean) valuation. First, the
Berkovich approach to non-Archimedean geometry is the one closest to the complex ana-
lytic intuition, and it is natural to see to what extent the complex analytic theory admits
a counterpart in the setting of Berkovich spaces. Second, Berkovich spaces over a triv-
ially or discretely valued field can often be used to study degenerations in complex geome-
try [FJ05a, FJ05b, FJ07, FJ11, BoJ17, BHJ19, Shi19], and such degenerations are central
to the variational approach to the YTD conjecture [BBJ21, Li20], through the notion of
geodesic rays.
   The thrust of the YTD conjecture is to relate the existence of a solution to a non-linear
PDE to an algebro-geometric condition known as K-stability, which has recently also come
to play a key role in the study of moduli spaces, especially for Fano varieties. [ABHX20,
BHLX21, BLX19, LXZ21, XZ20]. The relation of K-stability with spaces of valuations and
non-Archimedean geometry over trivially valued fields, originally pointed out in [BHJ17], is
one major motivation to endeavor the present study, and will be further exploited in the
companion papers [BoJ21, BoJ22].
   K-stability of a polarized projective variety (X, L) over an algebraically closed field k is a
condition phrased in terms of Gm -equivariant degenerations (X , L) → A1 of (X, L) known
as test configurations [Don02]. Our basic proposal, which goes back to [BHJ17], consists in
interpreting (X , L) in terms of a piecewise linear function ϕL on the Berkovich analytification
X an with respect to the trivial absolute value on the ground field k. To readers familiar with
non-Archimedean geometry, this will sound very natural indeed: the base change of a test
configuration (X , L) by Spec k[[$]] → A1 = Spec k[$] provides a model for the base change
(XK , LK ) to the non-Archimedean field K = k(($)), and hence a model/PL metric on the
Berkovich analytification Lan           an
                               K → XK . This metric can further be canonically identified
with a PL function on XK , thanks to the reference metric on Lan
                            an
                                                                      K induced by the trivial
model, and ϕL is simply the restriction of this function to X an ,→ XK an , the embedding being

realized by Gauss extension.
   While this point of view was basically the one adopted in a previous version of this
article [BoJ18a], we have tried here to take a more elementary and self-contained approach,
avoiding for the most part any explicit reference to general Berkovich geometry—which
accounts in part for the length of the present article.
               GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                  3

Functions and measures of finite energy. Let k be an arbitrary algebraically closed
field, and X an irreducible1 projective variety over k, with function field k(X). In order to
describe more precisely our main results, recall first that the Berkovich analytification X an
of X with respect to the trivial valuation on k is a compactification of the space X val of
valuations v : k(X)× → R, trivial on k, endowed with the topology of pointwise convergence.
Points of X an can be understood as semivaluations v on X, i.e. valuations v ∈ Y val for some
subvariety Y ⊂ X. The set X div ⊂ X val of divisorial valuations, which are attached to
prime divisors over X, is dense in X an .
   For every v ∈ X an and every section s ∈ H0 (X, mL), m ∈ N, we can make sense of


## Literal published source 1801.08229: source-extracts/1801.08229-trivial-valued-variational-proof.txt

infer
           ˆ
                                                          1                        1
             ϕ(MA(ψi ) − MA(ψ)) . (C + o(1)) I(ψi , ψ) 2 . C max{Jµ (ψi ), Jµ (ψ)} 2 ,

where the right-hand inequality
                            ´   follows from
                                          ´ Lemma 9.15. By Theorem 9.11, we have
MA(ϕi ) → µ weakly; hence ϕ MA(ψi ) → ϕ µ, while Jµ (ψi ) → 0, so we are done.         
                                                                    ´
Corollary 9.18. Pick µ ∈ M1 . If (ϕi ) is maximizing for µ then limi ϕi (MA(ϕi ) − µ) = 0
and limi E∨ (MA(ϕi )) = E∨ (µ).
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            105

Proof. By Corollary 9.16, J(ϕi ) is bounded for i large enough. By Lemma 9.17, it follows
that                         ˆ         ˆ
                                                                1
                        ci := ϕi µ − ϕi MA(ϕi ) = O(Jµ (ϕi ) 2 )
tends to 0, and hence
                                       ˆ                           ˆ
             ∨
            E (MA(ϕi )) = E(ϕi ) −         ϕi MA(ϕi ) = E(ϕi ) −       ϕi µ + ci → E∨ (µ),

completing the proof.                                                                               
  As another useful consequence, we get:
Proposition 9.19. Let ϕi → ϕ be a convergent net in PSH(ω), and assume that J(ϕi ) is
eventually bounded. For any µ ∈ M1 we then have ϕi → ϕ in L1 (µ).
                                    ´
Proof. We first claim that ψ 7→ ψ µ is continuous on {J ≤ C} ⊂ PSH(ω) for ´any C > 0.
To see this, pick a maximizing net (ρj )j for µ in PL ∩ PSH(ω). For each          ´ j, ϕ 7→ ϕ MA(ρ ´ j)
is continuous on PSH(ω), by Proposition 7.19 (ii). By Lemma 9.17, ψ MA(ρj ) → ψ µ
uniformly for ψ ∈ {J ≤ C} ⊂ PSH(ω), and the claim follows since continuity is preserved
under uniform convergence.
   The functional J is lsc, so J(ϕ) ≤ lim inf J(ϕi ) < ∞. Set ϕ0i := max{ϕi , ϕ}, so that
|ϕi − ϕ| = 2(ϕ0i − ϕ) + (ϕi − ϕ). Then ϕ0i → ϕ pointwise on X div , i.e. ϕ0i → ϕ in PSH(ω).
By (7.34) we further have I(ϕ0i , ϕ) ≤ I(ϕi , ϕ), and J(ϕ0i ) ≈ I(ϕ0i , 0) is thus eventually
                                                                                        ´      bounded,
                                                                                                  ´
by
´ 0 the quasi-triangle
          ´            inequality
                            ´      for I. The  first part of  the proof    thus  yields   ϕi µ → ϕ µ,
  ϕi µ → ϕ µ, and hence |ϕi − ϕ|µ → 0, which concludes the proof.                                    
9.4. Dependence on the ample class. In this section, X is assumed to be irreducible.
As in [BBGZ13, Proposition 3.4] we then have the following useful characterization of mea-
sures of finite energy.


## Literal published source 1801.08229: source-extracts/1801.08229-trivial-valued-surjectivity-proof.txt

12.2. Strong continuity and surjectivity of the Monge–Ampère operator. We de-
fine the strong topology on E 1 /R ≃ Esup
                                        1 as the one induced by the strong topology on E 1 .

It is defined by the quasi-metric (ϕ, ϕ0 ) 7→ I(ϕ, ϕ0 ), by Theorem 12.4.
   As a direct consequence of Lemma 10.7, we have:
Proposition 12.7. The Monge–Ampère operator MA : E 1 → M1 induces a bi-Lipschitz
embedding
                            (E 1 /R, I) ,→ (M1 , I∨ ).
   Recall from Theorem 5.11 that the envelope property for ω ∈ Amp(X) (which holds if X
is smooth and k has characteristic zero, cf. Theorem 5.20) is equivalent to the compactness
of PSH(ω)/R. In a similar vein we have:
Theorem 12.8. For any ω ∈ Amp(X), the following are equivalent:
    (i) the envelope property holds for ω;
   (ii) the Monge–Ampère operator MAω : E 1 (ω) → M1 is onto;
  (iii) the Monge–Ampère operator induces a bi-Lipschitz isomorphism
                                  (E 1 (ω)/R, Iω ) ≃ (M1 , I∨
                                                            ω );
122                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

      (iv) (E 1 (ω)/R, Iω ) is complete;
       (v) (E 1 (ω), Iω ) is complete.
  In particular, E 1 (ω) can only be complete if X is unibranch, cf. Theorem 5.12.
Proof. Assume (i). By Corollary 9.12, (ii) holds iff the supremum defining
                                                      ˆ     
                              ∨
                             E (µ) = sup E(ϕ) − ϕ µ
                                             ϕ∈E 1

is achieved for any µ ∈ M1 . Thus choose a maximizing sequence (ϕi ) for µ in Esup     1 . By

Corollary 5.21, PSHsup is weakly compact, and we may thus assume, after passing to a
subnet, that (ϕi ) converges weakly to ϕ ∈ PSHsup . Since Jµ (ϕi ) → 0, (9.11) shows that J(ϕi )
is eventually bounded, and hence that ´ϕ ∈ E 1 (ω),
                                                 ´ since J is weakly lsc. By Proposition 9.19,
the weak convergence ϕi → ϕ implies ϕi µ → ϕ µ, and hence
                             ˆ                        ˆ       
                     E(ϕ) − ϕ µ ≥ lim sup E(ϕi ) − ϕi µ = E∨ (µ),
                                             i
since E is weakly usc. This proves (i)⇒(ii). Proposition 12.7 gives (ii)⇔(iii), and (iii)⇒(iv)
follows from the completeness of (M1 , I∨    ω ) (Theorem 10.14).
   Assume (iv), and pick a Cauchy sequence (ϕi ) in (E 1 (ω), Iω ). Then (ϕi −sup ϕi ) is Cauchy
     1 (ω) ≃ E 1 (ω)/R, and hence strongly convergent in E 1 (ω). Now (sup ϕ ) is Cauchy as
in Esup                                                                            i
well, and hence convergent in R, so we conclude that (ϕi ) is strongly convergent, proving
(iv)⇒(v).
   Finally we prove (v)⇒(i). Assume that E 1 (ω) is complete. By Theorem 5.11, (i) is
equivalent to the fact that any bounded, increasing net (ϕi ) in PSH(ω) converges weakly in
PSH(ω). Since the increasing net (sup ϕi ) converges in R, it will be enough to show that
(ϕi ) is Cauchy in E 1 (ω)/R, i.e. that
                                                                 ˆ
              Iω (ϕi , ϕj ) ≈ Jω,ϕi (ϕj ) = Eω (ϕi ) − Eω (ϕj ) + (ϕj − ϕi ) MAω (ϕi )

tends to 0 as i, j → ∞, where by symmetry of Iω we may assume i ≤ j. The increasing net
(Eω (ϕi )) converges in R. Given ε > 0, choose i0 such that 0 ≤ Eω (ϕj ) − Eω (ϕi ) ≤ ε for
j ≥ i ≥ i0 . As ϕi ≤ ϕj , (7.22) yields
                   ˆ
              0 ≤ (ϕj − ϕi ) MAω (ϕi ) ≤ (n + 1) (Eω (ϕj ) − Eω (ϕi )) ≤ (n + 1)ε.

Thus                                               ˆ
                           Eω (ϕi ) − Eω (ϕj ) +       (ϕj − ϕi ) MAω (ϕi ) ≤ nε,
which proves, as desired, that (ϕi ) is Cauchy in E 1 (ω)/R.                                  
   As a direct consequence of Theorem 12.8 and Theorem 5.20, we have the following result,
cf. Theorem A.
Theorem 12.9. Suppose that X is smooth, that char k = 0 or dim X ≤ 2, and fix ω ∈
Amp(X). Then the Monge–Ampère equation MA(ϕ) = µ admits a solution ϕ ∈ E 1 (ω),
unique up to translation, for every µ ∈ M1 .
Example 12.10. Assume the envelope property for ω ∈ Amp(X). For each v ∈ X lin , there
exists a unique ϕv ∈ E 1 (ω) such that MA(ϕv ) = δv and ϕv (v) = 0, which we call the Green’s
function of v. See Proposition 12.14 for more on these functions.
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            123

Example 12.11. Let X be an irreducible curve with a nodal singularity at p ∈ X(k), and
denote by p1 , p2 ∈ X ν (k) the preimages of p (see Figure 1). Then v := ordp1 ∈ X ν, div ≃
X div , and δv ∈ M1 (X) is not in the image of MA : E 1 → M1 . Using Example 7.20 and
ν? MA(ν ? ϕ) = MA(ϕ) (see (7.18)), one sees indeed that a function ϕ ∈ PSH(ω) such that
MA(ϕ) = δv must satisfy ν ? ϕ(vtriv ) = ν ? ϕ(vp2 ,triv ) = ϕ(vp,triv ) = ν ? ϕ(vp1 ,triv ), and hence
must be constant on the ray through v, a contradiction.
12.3. Continuity of solutions to Monge–Ampère equations.
Theorem 12.12. Let ϕ ∈ E 1 , and suppose that µ := MA(ϕ) is supported in a bounded
subset of (X lin , d∞ ), i.e. supp µ ⊂ {T ≤ C} for some C > 0. Then ϕ ∈ CPSH(ω).


## Literal published source 2307.01697: source-extracts/2307.01697-synthetic-standing-and-Theorem-A.txt

The emphasis in this paper is on measures of finite energy, as opposed to potentials of finite
energy, that we do not seek to investigate here (see for instance [BFJ15, BoJ22a, Reb21,
DXZ23] in the non-Archimedean context).

The general setup. Throughout this paper, we work with a compact topological space X
equipped with the following data:
       • a dense linear subspace D ⊂ C0 (X) of test functions, containing all constants;
       • a vector space Z of closed (1, 1)-forms on X, endowed with a nice1 partial order,
         and a linear map ddc : D → Z vanishing on constants;
       • an integer n ≥ 1 (seen as the ‘dimension’ of X), and a nonzero n-linear symmetric
         map taking a tuple (θ1 , . . . , θn ) in Z to a signed Radon measure θ1 ∧ · · · ∧ θn on X,
         assumed to be positive for all θi ≥ 0, and such that each bilinear form
                                                   ˆ
                      D × D → R (φ, ψ) 7→ φ ddc ψ ∧ θ1 ∧ · · · ∧ θn−1                          (0.1)

         with θi ∈ Z is symmetric, and seminegative for θi ≥ 0.
We then introduce the Bott–Chern cohomology space
                                          HBC (X) := Z/ddc D,
and define the positive cone Pos(X) ⊂ HBC (X) as the interior2 of the image of the convex
cone
                                 Z+ := {θ ∈ Z | θ ≥ 0}.
This setup is primarily inspired by the case of a compact Kähler manifold X, where D is
the space of smooth functions, and Z the space of closed (1, 1)-forms. It also covers the
case of a projective Berkovich space X over a complete non-Archimedean field k, where D
is generated by piecewise linear (or model ) functions, and elements of Z are represented by
numerical classes on models over the valuation ring (or test configurations, in the trivially
valued case) [BFJ16a, GM16, BoJ22a]. At least under reasonable assumptions on X and k,
we then have HBC (X) = N1 (X), and Pos(X) coincides with the ample cone, see §1.3.2.

Measures
    ´     of finite energy. Fix a form ω ∈ Z+ such that [ω] ∈ Pos(X), with volume
Vω = ω n > 0. The space of ω-plurisubharmonic test functions is defined as
                                Dω := {φ ∈ D | ωφ := ω + ddc φ ≥ 0},
and the Monge–Ampère operator takes φ ∈ Dω to the probability measure
                                          MAω (φ) := Vω−1 ωφn .

    1See §1.1 for the terminology.
    2Here we use the finest vector space topology of H
                                                         BC (X), see §1.1.
                                  MEASURES OF FINITE ENERGY                                          3

It admits a primitive, the Monge–Ampère energy Eω : Dω → R, explicitly given by
                                         n      ˆ
                                     1 X −1
                           Eω (φ) =        Vω     φ ωφj ∧ ω n−j .
                                    n+1
                                              j=0

Denote by M the space of (Radon) probability measures on X, and define the energy of a
measure µ ∈ M as the Legendre transform3
                                             ˆ
                      Jω (µ) := sup {Eω (φ) − φ µ} ∈ [0, +∞].
                                     φ∈Dω

Then Jω : M → [0, +∞] is convex, and lsc in the weak topology; the space of measures of
finite energy is defined as
                                  M1ω := {µ ∈ M | Jω (µ) < ∞},
equipped with the strong topology, i.e. the coarsest refinement of the weak topology in which
Jω becomes continuous.
   As a consequence of the seminegativity of (0.1), the functional Eω is concave. This is
equivalent to the non-negativity of the Dirichlet functional
                                                     ˆ
                       Jω (φ, ψ) := Eω (φ) − Eω (ψ) + (ψ − φ) MAω (φ),

which is more explicitly given by the familiar expression
                                           ˆ
                                         1
                             Jω (φ, ψ) =     (φ − ψ)ddc (ψ − φ)
                                         2
when n = 1, and a positive linear combination of integrals of the form
                     ˆ
                       (φ − ψ)ddc (ψ − φ) ∧ ωφj ∧ ωψn−j−1 (0 ≤ j < n)

in general, see (1.31). Our first main result shows that the Dirichlet functional induces, via
the Monge–Ampère operator, a complete quasi-metric4 space structure on M1ω .
Theorem A. Assume that ω has the orthogonality property. Then:
   (i) the image of the Monge–Ampère operator MAω : Dω → M is a dense subspace of
       M1ω ;
  (ii) there exists a unique (continuous) quasi-metric δω on M1ω that defines the strong
       topology of M1ω and such that
                                δω (MAω (φ), MAω (ψ)) = Jω (φ, ψ)
        for all φ, ψ ∈ Dω ;
  (iii) the quasi-metric space (M1ω , δω ) is complete.
  The energy can be expressed in terms of the quasi-metric as
                    Jω (µ) = δω (µ, µω )    where   µω := Vω−1 ω n = MAω (0).
We refer to Definition 2.15 for the precise definition of the orthogonality property. Suf-
fice it to say here that it only depends on [ω] ∈ Pos(X), and holds when X is a com-
pact Kähler manifold, or any projective Berkovich space X over a non-Archimedean field
(as a consequence of [BE21, BGM22]). In the former case, Theorem A can be deduced
  3This corresponds to E∨ (µ) in the notation of [BBGZ13, BoJ22a], and to ∥µ∥ in that of [BoJ22b].
                          ω                                                  ω
  4See §1.1 for the notion of quasi-metric used in this paper.
4                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

from [BBGZ13, BBEGZ19]; in the latter, it was established in the trivially valued case
in [BoJ22a], and is thus extended here to the case of an arbitrary non-Archimedean ground
field.
   The strategy of proof of Theorem A follows the same lines as the trivially case treated
in [BoJ22a]. The first key ingredient is a uniform differentiability property for the Legendre
transform of the convex functional µ 7→ Jω (µ), which is shown to be equivalent to the
orthogonality property. This is used to prove that if (φi ) is a maximizing sequence for a
given µ ∈ M1ω (i.e. a sequence in Dω computing the supremum that defines Jω (µ)), then
MAω (φi ) converges to µ.
   The rest of the proof relies on an extensive use of Hölder estimates for mixed Monge–
Ampère integrals, obtained from repeated applications of the Cauchy–Schwarz inequality


## Literal published source 2307.01697: source-extracts/2307.01697-NA-positive-cone.txt

   In this section, we introduce the general setup considered in this paper, which is designed
to cover in a synthetic manner the case of a compact Kähler space and that of a projective
Berkovich space over a non-Archimedean field.

1.1. Notation and terminology.
     • For x, y ∈ R, x ≲ y or x = O(y) mean in this paper x ≤ Cn y for a constant Cn > 0
       only depending on a given integer n fixed in the setup, and x ≈ y if x ≲ y and y ≲ x.
     • Recall that any real vector space V admits a finest vector space topology, generated
       by its finite dimensional subspaces, i.e. a subset A ⊂ V is open (or closed) iff, for each
       finite dimensional subspace W ⊂ V , A ∩ W is open (resp. closed) in the canonical
       vector space topology of W . This topology is not locally convex as soon as the
       dimension of V is uncountable.
     • Consider a partially ordered R-vector space (V, ≥). We shall say for brevity that the
       partial order is nice if V+ := {x ∈ V | x ≥ 0} spans V , and is closed in the finest
       vector space topology of V .
     • In this paper, a quasi-metric on a set Z is a function δ : Z × Z → R≥0 that
          – is quasi-symmetric, i.e. there exists C > 0 such that
                              C −1 δ(x, y) ≤ δ(y, x) ≤ Cδ(x, y);
          – satisfies the quasi-triangle inequality, i.e. there exists C > 0 such that
                                δ(x, y) ≤ C(δ(x, z) + δ(z, y))
            (or, equivalently, δ(x, y) ≤ C ′ max{δ(x, z), δ(z, y)} for some other constant C ′ >
            0);
          – separates points, i.e. δ(x, y) = 0 ⇔ x = y.
       Note that δ ε is then also a quasi-metric for any ε > 0. A quasi-metric space (Z, δ)
       comes with a Hausdorff topology, and even a uniform structure. In particular,
       Cauchy sequences and completeness make sense for (Z, δ). Such uniform structures
       have a countable basis of entourages, and are thus metrizable, by general theory. In
       fact, there exists a metric d on X and A > 0 and constants ε > 0 only depending on
       C such that the quasi-metric δ ε satisfies A−1 δ ε ≤ d ≤ Aδ ε (see [Fri37, AIN98, PS09],
       thanks to Prakhar Gupta for hinting at those references).

1.2. Test functions and closed (1, 1)-forms. Throughout this paper, we work with a
compact Hausdorff topological space X. We denote by C0 (X)∨ the space of signed Radon
measures on X, and by
                                     M ⊂ C0 (X)∨
the subset of probability measures, which is convex and compact in the weak topology.
Recall from the introduction that we assume X equipped with the following data:
     • a dense linear subspace D ⊂ C0 (X) of test functions, containing all constants;
     • a vector space Z of closed (1, 1)-forms on X, endowed with a nice partial order, and
       a linear map ddc : D → Z vanishing on constants;
     • an integer n ≥ 1 (viewed as the ‘dimension’ of X), and a nonzero n-linear symmetric
       map taking a tuple (θ1 , . . . , θn ) in Z to a signed Radon measure θ1 ∧ · · · ∧ θn on X,
                                  MEASURES OF FINITE ENERGY                                          7

        assumed to be positive for all θi ≥ 0, and such that each bilinear form
                                             ˆ
                    D × D → R (φ, ψ) 7→ φ ddc ψ ∧ θ1 ∧ · · · ∧ θn−1

       with θi ∈ Z is symmetric, and seminegative when θi ≥ 0.
Since Z+ generates Z, symmetry in the last item amounts to the integration-by-parts formula
                 ˆ                              ˆ
                    φ dd ψ ∧ θ1 ∧ · · · ∧ θn−1 = ψ ddc φ ∧ θ1 ∧ · · · ∧ θn−1
                        c
                                                                                       (1.1)

for all φ, ψ ∈ D and θi ∈ Z, while seminegativity requires
                              ˆ
                                 φ ddc φ ∧ θ1 ∧ · · · ∧ θn−1 ≤ 0                                (1.2)

when θi ≥ 0 for all i.
Definition 1.1. For any θ ∈ Z and φ ∈ D, we set θφ := θ + ddc φ. We say that φ is
θ-plurisubharmonic (θ-psh for short) if θφ ≥ 0, and denote by
                                     Dθ := {φ ∈ D | θφ ≥ 0}
the space of θ-psh test functions.
  For all θ, θ′ ∈ Z and t ∈ R>0 we have
                                 Dθ + Dθ′ ⊂ Dθ+θ′ ,     Dtθ = tDθ .
In particular, Dθ is a convex subset of D, and
                                       θ ≤ θ′ =⇒ Dθ ⊂ Dθ′ .                                     (1.3)
Since ddc vanishes on constants, we have:
Example 1.2. Constant functions on X are θ-psh iff θ ≥ 0.
  The main two instances of the above setup considered in this paper are as follows.
1.2.1. The Kähler case. The above formalism is primarily inspired by the case of a compact
Kähler complex analytic space X. Here n = dim X, D = C ∞ (X) is the space of smooth
functions on X, and Z is the space of closed (1, 1)-forms on X that are locally ddc -exact,
                                     1,1                              ∞ → Ω1,1 (see for in-
i.e. global sections of the image ZX     of the sheaf morphism ddc : CX        X
stance [Dem85] for the definition of smooth forms in this context). When X is nonsingular,
i.e. a compact Kähler manifold, Z coincides with the space of closed (1, 1)-forms on X, but
the inclusion might be strict in the singular case.
   For all φ, ψ ∈ D and θi ∈ Z, the Stokes formula implies
                     ˆ                 ˆ                 ˆ
                        φ ddc ψ ∧ Θ = ψ ddc φ ∧ Θ = − dφ ∧ dc ψ ∧ Θ

with Θ := θ1 ∧ · · · ∧ θn−1 , which yields (1.1) and (1.2), since the (1, 1)-form dφ ∧ dc φ is
semipositive.
Remark 1.3. More generally, fix a Kähler form ωX on X and assume n ≤ dim X. Recall
                                                                                      dim X−i
that a (1, 1)-form α on X is n-semipositive (with respect to ωX ) if αi ∧ ωX                  ≥ 0 for
i = 0, . . . , n (see [Blo05, LN15]). For any n-tuple of n-semipositive (1, 1)-forms α1 , . . . , αn ,
                            dim X−n
we have α1 ∧· · ·∧αn ∧ωX              ≥ 0. One thus obtains a setup satisfying the above conditions
by defining Z+ as the convex cone of closed (1, 1)-forms that are n-semipositive, and by
                                                                              dim X−n
associating to a tuple (θ1 , . . . , θn ) in Z the measure θ1 ∧ · · · ∧ θn ∧ ωX       .
8                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

1.2.2. The non-Archimedean case. Assume now that X is a projective Berkovich space over
a non-Archimedean field k, i.e. the Berkovich analytification of a projective k-scheme, of
dimension n = dim X. We then take D to be the R-vector space generated by PL functions,
see [BE21, §5.4].
   When k is nontrivially valued, D can be described in terms of vertical divisors on (pro-
jective, flat) models X of X over the spectrum S of the valuation ring. More precisely, we
have
                                     D ≃ lim VCar(X )R ,
                                         −→
                                           X

where VCar(X )R denotes the R-vector space generated by Cartier divisors on X that are
vertical, i.e. supported on the special fiber. The same description applies in the trivially
valued case as well, if a model is now understood as a test configuration X → S := A1
(see [BHJ17, §6.1], [BoJ22a, §2.2]).
   In the nontrivially valued case, the space Z is defined by setting

                                     Z := lim N1 (X /S),                                  (1.4)
                                          −→
                                            X

where N1 (X /S) denotes the (finite dimensional) vector space of relative numerical classes
(see [BFJ16a, §4.2], [GM16, §4], the definition being inspired by [BGS95]). A form θ ∈
Z is thus represented by a numerical class θX ∈ N1 (X /S) for some model X , called a
determination of θ, two such classes being identified if they coincide after pulling back
to some higher model, and we write θ ≥ 0 if θX is (relatively) nef for some (hence any)
determination X of θ.
   The measure θ1 ∧ · · · ∧ θn associated to a tuple of forms θi ∈ Z is a finite linear combi-
nation of Dirac masses at divisorial points, whose coefficients can be described in terms of
intersection numbers computed on models.
   The linear map ddc : D → Z takes a vertical divisor D ∈ VCar(X )R to its numerical class
in N1 (X /S), and the seminegativity condition (1.2) follows the local Hodge index theorem
of Yuan–Zhang [YZ17, Theorem 2.1].
   Again, the same discussion applies to the trivially valued case as well, using test configu-
rations instead of models. In that case, pulling back numerical classes on X to the product
test configuration further yields an injection

                                        N1 (X) ,→ Z.                                      (1.5)

Note that only forms lying in N1 (X) were considered in [BoJ22a].

Remark 1.4. In the non-Archimedean case, one could also work with smooth functions and
(1, 1)-forms in the sense of [CD12] (see also [GK15, GK17, GJR21]), but this will not be
considered in the present paper.

Remark 1.5. More generally, test configurations for an arbitrary compact Kähler manifold
(as in [SD18, DeR17]) can also be approached using the above formalism. This is the topic
of forthcoming work of Pietro Piccione.

Remark 1.6. Another setting where the above formalism applies is that of tropical toric
pluripotential theory as in [BGJK21].
                                  MEASURES OF FINITE ENERGY                                        9

1.3. Bott–Chern cohomology and positive classes.
Definition 1.7. We define the Bott–Chern cohomology space as
                                      HBC (X) := Z/ddc D,
and denote by θ 7→ [θ] the quotient map Z → HBC (X). The positive cone
                                       Pos(X) ⊂ HBC (X)
is defined as the interior of the image of Z+ .
   Here the interior is taken with respect to the finest vector space topology (see §1.1).
Concretely, a class α ∈ HBC (X) belongs to Pos(X) if, for any β ∈ HBC (X), α + tβ lies in
the image of Z+ for all t ∈ R small enough.
   Since it is assumed that Z+ spans Z, its image in HBC (X) is a convex cone that generates
HBC (X). As a consequence, the positive cone Pos(X) is non-empty as soon as HBC (X) is
finite dimensional.
Remark 1.8. The image Z+ in HBC (X) is not closed in general. This happens already in
the complex projective case, see [DPS94, Example 1.7].
   Since ddc vanishes on R ⊂ D, (1.1) yields
                 ˆ                               ˆ
                    dd φ ∧ θ1 ∧ · · · ∧ θn−1 = φ ddc 1 ∧ θ1 ∧ · · · ∧ θn−1 = 0
                      c

                                                            ´
for all φ ∈ D and θi ∈ Z. As a result, (θ1 , . . . , θn ) 7→ θ1 ∧ · · · ∧ θn descends to a symmetric
n-linear pairing
                        HBC (X)n → R (α1 , . . . , αn ) 7→ α1 · . . . · αn ,
which we call the intersection pairing.
Lemma 1.9. For all classes α1 , . . . , αn ∈ Pos(X) we have α1 · . . . · αn > 0.
 Proof. By assumption, the measure θ1 ∧ · · · ∧ θn is nonzero for some tuple θ1 , . . . , θn ∈ Z.
´Since Z+ generates Z, we can further assume θi ∈ Z+ for all i. Then [θ1 ] · . . . · [θn ] =
   θ1 ∧ · · · ∧ θn > 0. Now we can find 0 < ε ≪ 1 such that αi − ε[θi ] ∈ Pos(X) for all i, and
hence α1 · . . . · αn ≥ εn [θ1 ] · . . . · [θn ] > 0.                                          □
Definition 1.10. For each ω ∈ Z+ and θ ∈ Z we set
                           ∥θ∥ω := inf{C ≥ 0 | ±θ ≤ Cω} ∈ [0, +∞],
and we say that θ is ω-bounded if ∥θ∥ω < ∞.
  The set
                                Zω := {θ ∈ Z | ∥θ∥ω < ∞}
of ω-bounded forms is a linear subspace of Z, on which ∥ · ∥ω defines a norm.
Remark 1.11. In general, Zω is a strict subspace of Z. More precisely, Zω = Z iff ω
lies in the interior of Z+ in the finest vector space topology of Z, which is empty in the
non-Archimedean case (see §1.3.2 below).
  We can now characterize positive classes as follows:
Proposition 1.12. A class α ∈ HBC (X) lies in Pos(X) iff, for each finite dimensional
subspace V ⊂ Z, α admits a representative ω ∈ Z+ such that V ⊂ Zω .
10                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. Assume α ∈ Pos(X), and pick a basis (θi )1≤i≤r of a finite dimensional vector space
V ⊂ Z. Since Z+ spans Z, for each i we can write θi = θi+ − θi− with θi± ≥ 0. Since
α ∈ Pos(X) we have α − ε[θi± ] ∈ Pos(X) for all 0 < ε ≪ 1, and we can thus find ε > 0 and
ωi± ∈ α such that ωi± − εθi± ≥ 0 for all i. Now set
                                             r
                                             X
                                        1
                                   ω := 2r         (ωi+ + ωi− ) ∈ Z+ .
                                             i=1
                                             ε ±        ε
Then [ω] = α, and for each i we have ω ≥ 2r   θi ≥ ± 2r   θi , and hence θi ∈ Zω , i.e. V ⊂ Zω .
This proves the ‘only if’ part, and the converse is clear.                                   □
Corollary 1.13. Pick θ ∈ Z such that [θ] ∈ Pos(X). Then any f ∈ D can be written as
f = f + − f − with f ± ∈ Dtθ = tDθ for some t > 0. In particular, Dθ spans D.
Proof. By Proposition 1.12, we can find ψ ∈ Dθ and C > 0 such that −ddc f ≤ t(θ + ddc ψ).
Thus f + := φ + tψ lies in Dtθ , and the result follows with f − := tψ ∈ DCθ .         □
     Following [Tho63], we define the Thompson distance between ω, ω ′ ∈ Z+ as
                      dT (ω, ω ′ ) := inf{δ ≥ 0 | e−δ ω ≤ ω ′ ≤ eδ ω} ∈ [0, +∞].              (1.6)
We say that ω and ω ′ are commensurable if d                ′                                 ′
                                                     T (ω, ω ) < ∞. Note that this holds iff ω ∈ Zω
and ω ∈ Zω′ . Commensurability is an equivalence relation on Z+ . The linear subspace Zω
only depends on the commensurability class of ω ∈ Z+ , and so does the equivalence class of
the norm ∥ · ∥ω .
  The next result is readily checked, and left to the reader.
Lemma 1.14. The commensurability class of any ω ∈ Z+ forms an open convex cone in the
normed vector space (Zω , ∥·∥ω ), whose topology is defined by the restriction of the Thompson
metric.
     We conclude this section with the following useful fact, that will be put to use in §3.
Proposition 1.15. Each finite subset of Pos(X) can be represented by commensurable forms
in Z+ .
Proof. We first claim that any two α, α′ ∈ Pos(X) admit commensurable representatives.
Indeed, setting α ∼ α′ when α and α′ admit commensurable representatives defines an
equivalence relation on Pos(X), and it is thus enough that each equivalence class intersects
the line segment [α, α′ ] in an open set. Pick β ∈ [α, α′ ], and choose representatives θ, θ′ ∈
Z+ of α, α′ . By Proposition 1.12, we can find a representative ω ∈ Z+ of β such that
θ, θ′ ∈ Zω . By Lemma 1.14, the commensurability class of ω intersects [θ, ω] and [ω, θ′ ]
along neighborhood of ω, and it follows, as desired, that the equivalence class of β intersects
[α, α′ ] along a neighborhood of β.
   Now pick α1 , . . . , αr ∈ Pos(X). By the first part of the proof, for each i = 2, . . . , r
we can find two P   commensurable forms ω1,i , ωi ∈ Z+ such that [ω1,i ] = α1 and [ωi ] = αi .
Then ω1 := r−1 ri=2 ω1,i ∈ Z+ represents α1 , and is commensurable to ωi for all i since
                1

commensurability classes are convex cones.                                                    □
1.3.1. The Kähler case. As in §1.2.1, assume that X is a compact Kähler space. When X is
nonsingular, HBC (X) coincides with the (1, 1)-part of the Hodge decomposition of H2 (X, R).
In general, denote by PHX the sheaf of germs of pluriharmonic functions, i.e. the kernel
of the sheaf morphism ddc : CX ∞ → Ω1,1 . The existence of partitions of unity implies that
                                       X
                                     MEASURES OF FINITE ENERGY                                                  11

the sheaf CX∞ is soft, and the cohomology long exact sequence associated to the short exact

sequence of sheaves
                                              ∞      1,1
                                0 → PHX → CX    → ZX     →0
thus yields
                                  HBC (X) ≃ H1 (X, PHX ).
We do not know whether this is always finite dimensional, but this holds at least when X is
normal, as a consequence of the fact that PHX then coincides with the sheaf ℜOX of real
parts of holomorphic functions, see [BG13, §4.6.1].
   The positive cone Pos(X) is compatible with the usual definition, i.e. α ∈ HBC (X) lies
in Pos(X) iff α can be represented by a Kähler form. Indeed, given any Kähler form ω,
a class α ∈ Pos(X) can be represented by a form θ ∈ Z such that θ − εω ∈ Z+ for some
0 < ε <≪ 1, so that θ is a Kähler form. In particular, Kähler forms constitute a single
commensurability class that maps onto Pos(X).
1.3.2. The non-Archimedean case. Assume, as §1.2.2, that X is a projective Berkovich space
over a non-Archimedean field. By definition, any θ ∈ Z is represented by a numerical class
on some model X of X, whose restriction to the generic fiber defines a numerical class
{θ} ∈ N1 (X) on (the projective variety underlying) X. This induces a surjective map
                                            HBC (X) ↠ N1 (X),                                                (1.7)
which is an isomorphism when X is smooth and k is discretely valued of residue character-
istic 0 [BFJ16a, Theorem 4.3], or when X is normal and k is algebraically closed [Jell16,
Theorem 4.2.7]). It is also an isomorphism when k is trivially valued, with inverse provided
by pulling back classes in N1 (X) to the trivial test configuration Xtriv = X × A1 .
    We claim that Pos(X) coincides with the preimage of the ample cone of X under (1.7),
and that Z+ has empty interior in the finest vector space topology of Z (so that Kähler
forms do not admit an analogue in the non-Archimedean case).
    To see this, we say as in [BFJ16a, §5.1] that a form ω ∈ Z+ is X -positive for a given
model/test configuration X if it is represented by a (relatively) ample class in N1 (X /S).
Note that all X -positive forms are commensurable. As observed in [BFJ16a, Proposition 5.2]
(see also [GM16, Proposition 4.14], [BoJ22a, Lemma 3.11]), any α ∈ HBC (X) whose image in
N1 (X) under (1.7) is ample can be represented by an X -positive form ω for any sufficiently
high model X . Now Zω contains all forms determined on X , but does not contain any
X ′ -positive form for a model X ′ strictly dominating X . The claim easily follows.
1.4. The energy pairing. Mimicking the properties of induced metrics on Deligne pairings
(see for instance [BE21, Theorem 8.16]), and generalizing [SD18, §2.2] (for a compact Kähler
manifold) and [BoJ22a, §3.2] (for a projective Berkovich space over a trivially valued field),
we introduce:
Proposition-Definition 1.16. The energy pairing
              (Z × D)n+1 → R          ((θ0 , φ0 ), . . . , (θn , φn )) 7→ (θ0 , φ0 ) · . . . · (θn , φn ),
is defined as the unique (n + 1)-linear symmetric map such that
                                                       ˆ
           (0, φ0 ) · (θ1 , φ1 ) · . . . · (θn , φn ) = φ0 (θ1 + ddc φ1 ) ∧ · · · ∧ (θn + ddc φn )           (1.8)

and
                                         (θ0 , 0) · . . . · (θn , 0) = 0.                                    (1.9)
12                                  SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON


## Literal published source 2307.01697: source-extracts/2307.01697-Holder-and-defect-proof.txt

                                                  (φ − ψ) ddc (ψ − φ) ∧ ωφj ∧ ωψn−1−j .
                                  X
               Jω (φ, ψ) = Vω−1                                                           (1.31)
                                        n+1
                                  j=0
We simply write                                        ˆ
                              Jω (φ) := Jω (0, φ) =        φ µω − Eω (φ).                 (1.32)

Example 1.31. When n = 1, we have
                                                      ˆ
                        Jω (φ, ψ) = Jω (ψ, φ) = 12         (φ − ψ)ddc (ψ − φ),

which recovers the usual expression for the Dirichlet functional on a Riemann surface.
  For each R > 0 we set
                                  Dω,R := {φ ∈ Dω | Jω (φ) ≤ R}.                          (1.33)
Lemma 1.32. For each R > 0, Dω,R is a convex subset of D that generates it.
Proof. By convexity of Jω = Jω (0, ·), Dω,R is convex. Since Dω spans D (see Corollary 1.13),
to see that Dω,R spans it suffices to show that any φ ∈ Dω satisfies Jω (tφ) ≤ R for 0 < t ≪ 1,
which holds since Jω (tφ) is a polynomial function of t with Jω (0) = 0.                     □
   We may now collect the fundamental properties of the Dirichlet functional in the next
result.
Theorem 1.33. For all φ, φ′ , ψ, ψ ′ , τ ∈ Dω and t ∈ [0, 1], the following holds:
    • quasi-symmetry:
                                    Jω (φ, ψ) ≈ Jω (ψ, φ);                                (1.34)
    • quasi-triangle inequality:
                                  Jω (φ, ψ) ≲ Jω (φ, τ ) + Jω (τ, ψ);                     (1.35)
      • quadratic estimate:
                                Jω (φ, (1 − t)φ + tψ) ≲ t2 Jω (φ, ψ);                     (1.36)
      • uniform concavity:
              Eω ((1 − t)φ + tψ) − [(1 − t) Eω (φ) + t Eω (ψ)] ≳ t(1 − t)Jω (φ, ψ).
For all φ, φ′ , ψ, ψ ′ ∈ Dω,R , we further have the following Hölder estimates:
               ˆ
                 (φ − φ′ ) MAω (ψ) − MAω (ψ ′ ) ≲ Jω (φ, φ′ )α Jω (ψ, ψ ′ )1/2 R1/2−α ;
                                                  
                                                                                          (1.37)

and
                   Jω (φ, ψ) − Jω (φ′ , ψ ′ ) ≲ max{Jω (φ, φ′ ), Jω (ψ, ψ ′ )}α R1−α ,    (1.38)
where α := 2−n .
Proof. In view of (1.13), this is a direct consequence of Theorem A.3 applied to
     • the vector space V := Z × D with projection π : V → Z onto the first factor;
18                             SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

        • the convex cone P := {(θ, φ) ∈ V | φ ∈ Dθ };
                                                                             n+1
        • the homogeneous polynomial F : V → R defined by F (θ, φ) := − (θ,φ)
                                                                        (n+1)Vω .
                                                                                                        □

     As a simple consequence of (1.29), we finally note:
Lemma 1.34. For each τ ∈ Dω and φ, ψ ∈ Dωτ we have φ + τ, ψ + τ ∈ Dω and
                                     Jωτ (φ, ψ) = Jω (φ + τ, ψ + τ ).                              (1.39)
Remark 1.35. The above formalism recovers that of [BBGZ13, BBEGZ19, BFJ15, BoJ22a]
in the Kähler and non-Archimedean settings. However, in contrast to those works, we do
not explicitly introduce here the functional Iω (φ, ψ), which corresponds to the right-hand side
of (1.30).

                                   2. Measures of finite energy
   In what follows, we pick ω ∈ Z+ with [ω] ∈ Pos(X). We define the space M1ω of measures
of finite energy with respect to ω, and show, assuming a certain orthogonality property, that
it is complete with respect to a quasi-metric δω induced by the Dirichlet functional.

2.1. The energy of a measure.
Definition 2.1. We define the energy of µ ∈ M relative to ψ ∈ Dω as
                                                 ˆ
              Jω (µ, ψ) := sup {Eω (φ) − Eω (ψ) + (ψ − φ)µ} ∈ [0, +∞].                              (2.1)
                                  φ∈Dω

     The choice of notation is justified by (2.5) below. When ψ = 0, we simply write
                                                              ˆ
                          Jω (µ) := Jω (µ, 0) = sup {Eω (φ) − φ µ},                                 (2.2)
                                                    φ∈Dω

and call it the energy5 of µ (with respect to ω). Note that
                                          ˆ
                            Jω (µ) = sup { φ(µω − µ) − Jω (φ)},                                     (2.3)
                                          φ∈Dω

by (1.32).
Proposition 2.2. For each ψ ∈ Dω , the functional Jω (·, ψ) : M → [0, +∞] is convex and
weakly lsc, and satisfies, for all µ ∈ M and φ ∈ Dω ,
                                                  ˆ
                              Jω (µ, ψ) = Jω (µ) + ψ µ − Eω (ψ);                   (2.4)

                                      Jω (MAω (φ), ψ) = Jω (φ, ψ);                                  (2.5)
                                         Jω (MAω (φ)) ≈ Jω (φ);                                     (2.6)
                                    Jω (φ, ψ) ≲ Jω (µ, φ) + Jω (µ, ψ).                              (2.7)

     5This corresponds to E∨ (µ) in the notation of [BBGZ13, BoJ22a], and to ∥µ∥
                           ω                                                   ω in that of [BoJ22b].
                                  MEASURES OF FINITE ENERGY                                  19

Proof. Convexity and lower semicontinuity are clear from (2.1), which also directly yields (2.4).
By (1.28), any φ ∈ Dω further computes the supremum defining Jω (MAω (φ), ψ), which is
thus equal to                         ˆ
                    Eω (φ) − Eω (ψ) + (ψ − φ) MAω (φ) = Jω (φ, ψ).
This proves (2.5), which implies
                 Jω (MAω (φ)) = Jω (MAω (φ), 0) = Jω (φ, 0) ≈ Jω (0, φ) = Jω (φ),
see (1.34). Finally, pick µ ∈ M, and set τ = 21 (φ + ψ) ∈ Dω . By (2.1), we have
                                  ˆ                                          ˆ
    Jω (µ, φ) ≥ Eω (τ ) − Eω (φ) + (φ − τ ) µ, Jω (µ, ψ) ≥ Eω (τ ) − Eω (ψ) + (ψ − τ ) µ,

and hence
                       Jω (µ, φ) + Jω (µ, ψ) ≥ 2 Eω (τ ) − (Eω (φ) + Eω (ψ)).
On the other hand,
                         2 Eω (τ ) − (Eω (φ) + Eω (ψ)) ≳ Jω (φ, ψ)
by uniform concavity of Eω (see Theorem 1.33), and (2.7) follows.                            □
  Generalizing Lemma 1.34, we note:
Lemma 2.3. For all τ ∈ Dω , ψ ∈ Dωτ and µ ∈ M we have
                                    Jωτ (µ, ψ) = Jω (µ, ψ + τ ).                          (2.8)
In particular,                                       ˆ
                                Jωτ (µ) = Jω (µ) +       τ µ − Eω (τ ).                   (2.9)

Proof. By Lemma 1.29, we have φ ∈ Dωτ ⇔ φ + τ ∈ Dω , and
                      ˆ                                      ˆ
   Eωτ (φ) − Eωτ (ψ) + (φ − ψ)µ = Eω (φ + τ ) − Eω (ψ + τ ) + ((φ + τ ) − (ψ + τ ))µ.

Taking the sup over φ yields (2.8), and (2.9) follows, by (2.4).                             □
Remark 2.4. If we drop the assumption that ω ≥ 0, but still require [ω] ∈ Pos(X), then
Eω (φ) and Jω (µ) can still defined by (1.24) and (2.2), respectively. Then Lemma 1.29,
and hence (2.9), remain valid for any τ ∈ D. This will only get used in the context of
Theorem 4.8 below.
2.2. Measures of finite energy.
Definition 2.5. The space of measures of finite energy (with respect to ω) is defined as


## Literal published source 2307.01697: source-extracts/2307.01697-maxima-orthogonality.txt

Since E                                                                    e ω (µ) < ∞ implies
      e ω is increasing and equivariant, it is straightforward to see that E
            ´
µ ≥ 0 and µ = 1, i.e. µ ∈ M (compare [BoJ22a, Proposition 9.8]). By Legendre duality,
                                 e ∨ (µ) = Jω (µ) for µ ∈ M. Since E
the result is thus equivalent to E                                  e ω restricts to Eω on Dω ,
                                   ω
                    ∨                                      0
                  e (µ) ≥ Jω (µ). Conversely, pick f ∈ C (X) and φ ∈ Dω with φ ≤ f . Then
we trivially have E ω
                                            ˆ                  ˆ
                          Jω (µ) ≥ Eω (φ) − φ µ ≥ Eω (φ) − f µ,

where the first and second inequality respectively follow from (2.2) and φ ≤ f . Taking the
                                                             ´
supremum over φ and then over f yields Jω (µ) ≥ E                              e ∨ (µ).
                                                   e ω (f ) − f µ and Jω (µ) ≥ E         □
                                                                                 ω

2.4. Orthogonality and differentiability.
Definition 2.11. We say that Dω admits maxima if, for all φ, ψ ∈ Dω and f ∈ D such
that max{φ, ψ} < f pointwise on X, there exists τ ∈ Dω with max{φ, ψ} ≤ τ < f .
  This equivalently means that, for any f ∈ D, the poset
                                 Dω,<f := {φ ∈ Dω | φ < f }
is inductive. We can then consider limits of nets indexed by Dω,<f . For instance, note that
                                   E
                                   e ω (f ) =     lim     Eω (φ).                       (2.14)
                                                φ∈Dω,<f

Example 2.12. If X is a compact Kähler space, then Dω admits maxima: take τ :=
max(φ,
g      ψ) for an appropriate regularized max function max.
                                                      g
Example 2.13. If X is a projective Berkovich space, then Dω also admits maxima, since
Q-PL functions in Dω are dense in Dω , and stable under max.
Remark 2.14. While we will not pursue this direction here, one can introduce as in [BFJ16a,
BE21, BoJ22a] the space PSH(ω) of ω-psh functions φ : X → R∪{−∞}, defined as usc       ´ func-
tions that can be obtained as pointwise limits of decreasing nets in Dω , and such that φ µω >
−∞. Then Dω admits maxima iff PSH(ω) (or, equivalently, the subspace CPSH(ω) :=
PSH(ω) ∩ C0 (X) of continuous ω-phs functions) is stable under max.
Definition 2.15. We say that ω has the orthogonality property if Dω admits maxima and
                                   ˆ
                              lim     (f − φ) MAω (φ) = 0                       (2.15)
                               φ∈Dω,<f

for all f ∈ D.

´ Explicitly, this means for that for any ε > 0 there exists φ0 ∈ Dω such that φ0 < f and
 (f − φ) MAω (φ) ≤ ε for all φ ∈ Dω with φ0 ≤ φ < f .
22                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Remark 2.16. The orthogonality property for ω only depends on [ω] ∈ Pos(X). Indeed, for
any τ ∈ Dω and f ∈ D we have
                                 φ ∈ Dωτ ,<f ⇐⇒ φ + τ ∈ Dω,<f +τ                   (2.16)
This implies that Dω has finite maxima iff Dωτ does, and similarly for the orthogonality
property, using
                                ˆ                    ˆ
MAωτ (φ) = MAω (φ + τ ) and       (f − φ) MAωτ (φ) = ((f + τ ) − (φ + τ )) MAω (φ + τ ).

Example 2.17. Assume X is a compact Kähler space. Conjecturally, the orthogonality
property always holds. This is known when X is nonsingular, or X is projective and [ω] ∈
Amp(X), see Appendix B for a more detailed discussion.
Remark 2.18. More generally, the orthogonality property also holds in the setting of Re-
mark 1.3 (assuming X is a compact Kähler manifold). This follows indeed from [LN15,
Theorem 3.2].
     Recall from Corollary 1.13 that any test function f ∈ D can be written as
                                     f = f + − f −,      f ± ∈ DCω                 (2.17)
for some C = C(f ) > 0. In line with [BFJ15, §7], we show:
Proposition 2.19. Assume Dω admits maxima. The following properties are then equiva-
lent:
     (i) ω has the orthogonality property;
    (ii) for any f ∈ D written as (2.17) for a given C > 0, we have
                                             ˆ
                       Eω (φ + f ) − Eω (φ) − f MAω (φ) ≲ C sup |f |
                       e                                                      (2.18)

           for all φ ∈ Dω ;
     (iii) in the setting of (ii), we have
                                                    ˆ
                       e ω (φ + tf ) − Eω (φ) − t
                       E                                f MAω (φ) ≲ Ct2 sup |f |   (2.19)

          for all φ ∈ Dω and t ∈ R.
Proof. Assume (i). Write f ∈ D as in (2.17), and pick φ ∈ Dω . For any ψ ∈ Dω,<φ+εf ,
(1.28) yields
        ˆ                                     ˆ                  ˆ
           (ψ − φ) MAω (ψ) ≤ Eω (ψ) − Eω (φ) ≤ (ψ − φ) MAω (φ) ≤ f MAω (φ).
                       ´
By (1.19), we also have f (MAω (φ) − MAω (ψ)) ≤ 2nC sup |φ − ψ|, and we infer
                     ˆ             ˆ
   Eω (ψ) − Eω (φ) − f MAω (φ) ≤ ((φ + f ) − ψ) MAω (ψ) + 2nC sup |φ − ψ|.         (2.20)

Now limψ∈Dω,<φ+f Eω (ψ) = E
                          e ω (φ + f ) (see (2.14)), while orthogonality yields
                                   ˆ
                           lim        ((φ + f ) − ψ) MAω (ψ) = 0.
                             ψ∈Dω,<φ+f
                                   MEASURES OF FINITE ENERGY                                      23

Further, any ψ ∈ Dω,<φ+f large enough is greater than φ − sup |f | ∈ Dω,<φ+f , and hence
satisfies sup |φ − ψ| ≤ sup |f |. As a result, (2.20) implies
                                               ˆ
                      Eω (φ + f ) − Eω (φ) − f MAω (φ) ≤ 2nC sup |f |,
                      e

which shows (i)⇒ (ii). Next, (ii)⇒(iii), since f = f + − f − with f ∈ DCω implies tf =
sgn(t)(|t|f + − |t|f − ) with |t|f ± ∈ DC|t|ω .
  Finally, assume (iii), and pick f ∈ D. We need to show that
                                               ˆ
                                L := lim sup (f − φ) MAω (φ) ≥ 0
                                    φ∈Dω,<f

vanishes. Write f as in (2.17) for some C > 0. Pick also φ ∈ Dω,<f , and set g := f − φ ∈ D.
For any t ∈ [0, 1] we have φ + tg = (1 − t)φ + tf ≤ f , and hence E     e ω (φ + tg) ≤ E
                                                                                       e ω (f ). On
                                   +      −               +      −
the other hand, since f − φ = f − (f + φ) with f , < f + φ ∈ D(C+1)ω , (iii) yields a
constant A > 0 only depending on φ such that
     ˆ
0 ≤ t (f − φ) MAω (φ) ≤ E   e ω (φ + tg) − Eω (φ) + t2 A sup |g| ≤ E
                                                                   e ω (f ) − Eω (φ) + t2 A sup |g|.

Since any φ ∈ Dω,<f large enough is greater then f + − sup f − , it satisfies
                               0 ≤ g = f − φ ≤ sup f − − f − ≤ B
with B only depending on f . We infer 0 ≤ tL ≤ t2 AB. Dividing by t > 0 and letting t → 0+
yields, as desired, L = 0. This proves (iii)⇒(i).                                        □
Example 2.20. Assume X is a projective Berkovich space over a non-Archimedean field.
Then [BE21, Theorem A] combined with the uniform differentiability estimate of [BGM22,
Lemma 3.2] shows that (2.18) is satisfied (compare [BoJ22a, Lemma 8.7]). By Proposi-
tion 2.19, it follows that the orthogonality property always holds in this setting.
2.5. Maximizing sequences.
                                                                                  1
Definition 2.21. We say that a sequence (ψ     ´ i ) in Dω is maximizing for µ ∈ Mω if it
computes the energy of µ (2.2), i.e. Eω (ψi ) − ψi µ → Jω (µ).
  Equivalently, (ψi ) is maximizing for µ iff Jω (µ, ψi ) → 0, see (2.4).
Example 2.22. For any φ ∈ Dω the constant sequence ψi = φ is maximizing for µ =
MAω (φ) (see (2.5)).


## Literal published source 2307.01697: source-extracts/2307.01697-density-and-uniform-integral-proof.txt

                                                                                  1
Definition 2.21. We say that a sequence (ψ     ´ i ) in Dω is maximizing for µ ∈ Mω if it
computes the energy of µ (2.2), i.e. Eω (ψi ) − ψi µ → Jω (µ).
  Equivalently, (ψi ) is maximizing for µ iff Jω (µ, ψi ) → 0, see (2.4).
Example 2.22. For any φ ∈ Dω the constant sequence ψi = φ is maximizing for µ =
MAω (φ) (see (2.5)).
  As a key consequence of Proposition 2.19, we show:
Theorem 2.23. Assume ω has the orthogonality property. Pick µ ∈ M1ω and a maximizing
sequence ψi ∈ Dω . Then the measures µi := MAω (ψi ) converge strongly to µ in M1ω , i.e.
µi → µ weakly and Jω (µi ) → Jω (µ). In particular, the image of the Monge–Ampère operator
                                        MAω : Dω → M1ω
is dense in the strong topology.
Proof. Pick f ∈ D, and choose C > 0 such that f = f + − f − with f ± ∈ DCω . Since we
assume orthogonality, Proposition 2.19 yields A > 0 such that
                                                  ˆ
                      Eω (ψi + tf ) − Eω (ψi ) − t f µi ≤ At2 sup |f |
                      e
24                            SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

for all i and t > 0. By Proposition 2.10 and (2.4), we have, on the other hand,
                                     ˆ                                        ˆ
             Eω (ψi + tf ) ≤ Jω (µ) + (ψi + tf )µ = Jω (µ, ψi ) + Eω (ψi ) + t f µ.
             e

Combining these estimates, we get
                           ˆ        ˆ
                          t f µi ≤ t f µ + Jω (µ, ψi ) + At2 .

Since Jω (µ, ψi ) → 0, we infer
                                                ˆ              ˆ
                                    t lim sup       f µi ≤ t       f µ + At2 .
                                         i
                                                      ´         ´
Dividing´ by t and´ letting t →  0+ yields lim  sup i   f µ i ≤   f µ. Replacing f with −f , we
                                                0
get limi f µi = f µ. By density of D in´ C (X), this shows µi → µ weakly.       ´
   For each i we have Jω (µi ) = Eω (ψi ) − ψi µi (see (2.5)), ´ and Eω (ψi ) − ψi µ → Jω (µ),
since (ψi ) is maximizing for µ. It only remains to prove ψi (µi − µ) → 0. Since Jω (ψi ) is
bounded (see (2.7), (1.37) yields C > 0 such that
                                ˆ
                                   ψi (µi − µj ) ≲ CJω (ψi , ψj )α

for all i, j, and hence
                          ˆ
                               ψi (µi − µj ) ≲ C max{Jω (µ, ψi ), Jω (µ, ψj )}α ,

by (2.7). Since µj → µ weakly and Jω (µ, ψj ) → 0 as j → ∞, we infer
                              ˆ
                                ψi (µi − µ) ≲ CJω (µ, ψi )α ,

and we conclude, as desired, that the left-hand side tends to 0 as i → ∞.                                   □
2.6. The Dirichlet quasi-metric. From now on, we assume that the orthogonality
property holds for ω. Recall from Examples 2.17 and 2.20, that this is the case if X is a
compact Kähler manifold, and for any projective Berkovich space.
Theorem 2.24. There exists a unique continuous functional
                                         δω : M1ω × M1ω → R≥0 ,
such that
                             δω (MAω (φ), MAω (ψ)) = Jω (φ, ψ)                                          (2.21)
for all φ, ψ ∈ Dω . Furthermore:
    (i) for all µ ∈ M1ω and ψ ∈ Dω we have
                          δω (µ, MAω (ψ)) = Jω (µ, ψ),             δω (µ, µω ) = Jω (µ);                (2.22)
     (ii) δω is a quasi-metric: for all µ, ν, ρ ∈ M1ω we have
       δω (µ, ν) = 0 ⇔ µ = ν,      δω (µ, ν) ≈ δω (ν, µ),          δω (µ, ν) ≲ δω (µ, ρ) + δω (ρ, ν);   (2.23)
     (iii) the quasi-metric δω satisfies the Hölder continuity property
                      δω (µ, ν) − δω (µ′ , ν ′ ) ≲ max{δω (µ, µ′ ), δω (ν, ν ′ )}α R1−α                 (2.24)
         for all R > 0 and µ, µ′ , ν, ν ′ ∈ M1ω,R , with α := 2−n ;
                                 MEASURES OF FINITE ENERGY                                   25

   (iv) for all R > 0 and φ, ψ ∈ Dω,R , µ, ν ∈ M1ω,R , we have the Hölder estimate
                      ˆ
                        (φ − ψ)(µ − ν) ≲ Jω (φ, ψ)α δω (µ, ν)1/2 R1/2−α .               (2.25)

  We call δω the Dirichlet quasi-metric of M1ω .
Lemma 2.25. For all µ ∈ M1ω,R and φ, ψ, τ ∈ Dω,R , we have

               |Jω (µ, φ) − Jω (MAω (τ ), ψ)| ≲ max{Jω (µ, τ ), Jω (φ, ψ)}α R1−α ;      (2.26)
                   ˆ
                     (φ − ψ)(µ − MAω (τ )) ≲ Jω (φ, ψ)α Jω (µ, τ )1/2 R1/2−α .          (2.27)

Proof. When µ lies in the image of MAω : Dω → M1ω this is equivalent to (1.38) and (1.37), in
view of (2.5) and (2.6). By Theorem 2.23 the image of MAω is dense in M1ω , and the general
case thus follows by continuity in the strong topology of all functions of µ involved.     □

Proof of Theorem 2.24. Uniqueness is clear, since (2.21) determines δω on the image of
MAω : Dω → M1ω , which is dense in the strong topology, by Theorem 2.23. To show exis-
tence, pick µ, ν ∈ M1ω , and choose a maximizing sequences (ψi ) for ν. We can then find
R > 0 such that µ ∈ M1ω,R and ψi ∈ Dω,R for all i, and (2.26) and (2.7) yield


## Literal published source 2209.04879: source-extracts/2209.04879-Remark-4.4.txt

                    Z                           Z
                        φ0 MA(φ1 , ..., φn ) =      φ1 MA(φ0 , φ2 , ..., φn ).
                      X                           X
  The Monge-Ampère measure can then be extended by density to more general metrics:
Theorem 4.3. [BE21, thm. 8.4]
Let K be a complete valued field, X/K an n-dimensional projective scheme and L1 ,...,Ln
line bundles on X. Then the Monge-Ampère operator:
                             (φ1 , ..., φn ) 7→ ddc φ1 ∧ ... ∧ ddc φn
admits a unique extension to continuous psh metrics on the Li . The extension is further-
more continuous with respect to the topology of uniform convergence and the weak topology
of Radon measures.
Remark 4.4. While the class E 1 (X, L) of finite-energy psh metrics on L is defined over any
non-archimedean field K, it is unclear in general how to extend the Monge-Ampère operator
on the latter. Note however that in the case where K is discretely-valued of characteristic
zero, this extension was constructed in [BFJ16], and the trivially-valued case was handled
in [BJ22].
Remark 4.5. The Chambert-Loir - Ducros [CLD12] approach to pluripotential theory on
Berkovich spaces makes sense of the curvature current ddc φ of a continuous psh metric,
and its wedge products, in a spirit close to the work of Bedford-Taylor in the complex case.
Notably, [CLD12, thm. 6.9.3] states that the wedge product ddc φ1 ∧ ... ∧ ddc φn coincides
with the mixed Monge-Ampère measure as described in example 4.1 when φ1 ,..., φn are psh
model metrics, whence the notation.
4.2. The Monge-Ampère equation. Let X be a smooth n-dimensional complex man-
ifold, and L an ample line bundle on X. Then Yau’s celebrated solution to the Calabi
conjecture asserts the following:
Theorem 4.6. [Yau78] Let µ be a smooth volume form on X, normalized to have total
mass 1. Then there exists a unique (up to an additive constant) smooth, positive definite


## Literal published source 2506.13548: source-extracts/2506.13548-title-and-scope.txt

                                            CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES

                                                                          WALTER GUBLER AND JOSEPH RABINOFF


                                                   ABSTRACT. First we extend the theory of subharmonic functions on smooth strictly k-
                                                   analytic curves from Thuillier’s thesis to the case of possibly singular analytic curves over
                                                   a non-archimedean field k. Classically psh functions are then defined as in complex geom-
arXiv:2506.13548v2 [math.AG] 17 Sep 2025




                                                   etry by using pullbacks to analytic curves (and requiring compatibility with base change).
                                                   We give various properties of classically psh functions including a local and a global max-
                                                   imum principle. As a consequence, we show that the space of pluriharmonic functions on
                                                   a quasi-compact Berkovich space is finite dimensional. As a technical tool, we use that a
                                                   connected Berkovich space is connected by analytic curves.




                                                                                      1. INTRODUCTION
                                              Plurisubharmonic functions are the complex analytic counterparts of subharmonic func-
                                           tions in real analysis. To recall the definition, we begin with the notion of subharmonicity
                                           on the complex line. Let Ω ⊂ C be an open set and let u: Ω → [−∞, ∞) be an upper
                                           semicontinuous function. Then u is subharmonic if for every closed ball B(a, r) with cen-
                                           ter a and radius r contained in Ω and every continuous function h: B(a, r) → R which
                                           is harmonic on the open ball B(a, r) such that u ≤ h on the boundary ∂ B(a, r), we have
                                           u ≤ h on B(a, r). Note that the notion of (sub)harmonicity is insensitive to biholomorphic
                                           maps, hence makes sense on any one-dimensional complex manifold.
                                              Now let X be any complex manifold (without boundary, for simplicity) and let u: X →
                                           [−∞, ∞) be an upper semicontinuous function. Then u is plurisubharmonic or psh if,
                                           for every holomorphic map f : B(0, 1) → X from the open unit ball B(0, 1) ⊂ C, the
                                           pullback u ◦ f is subharmonic on B(0, 1). We say that u is pluriharmonic if u and −u are
                                           plurisubharmonic.
                                              Plurisubharmonicity was introduced by Lelong [Lel42] and Oka [Oka42] indepen-
                                           dently to study holomorphic convexity. It turned out to be a crucial positivity notion
                                           on complex manifolds. Plurisubharmonic functions satisfy the following properties:
                                               (1) The space of psh functions forms a convex cone: that is, if u1 , u2 are psh and
                                                   λ1 , λ2 ≥ 0, then λ1 u1 + λ2 u2 is psh.
                                               (2) If u1 , u2 are psh functions then max{u1 , u2 } is psh.
                                               (3) If {uk }k≥1 is a decreasing sequence of psh functions, then u = lim uk is psh.
                                               (4) A psh function u satisfies the local maximum principle: if u attains a local maxi-
                                                   mum at x 0 ∈ X , then u is constant on the connected component of x 0 in X .

                                              2020 Mathematics Subject Classification. Primary 14G40; Secondary 31C05, 32P05, 32U05.
                                              Key words and phrases. Berkovich spaces, plurisubharmonic and pluriharmonic functions.
                                              W. Gubler was supported by the collaborative research center SFB 1085 Higher Invariants - Interactions
                                           between Arithmetic Geometry and Global Analysis funded by the Deutsche Forschungsgemeinschaft.
                                                                                                1
2                                 W. GUBLER AND J. RABINOFF

   Now we consider the non-Archimedean situation. Let k be a field that is complete
with respect to a non-Archimedean absolute value | |. We refer to Section 2 for the
notions used from non-Archimedean geometry. The theory of subharmonic functions
on a smooth, strictly analytic k-curve X has been completely worked out by Thuillier in
his thesis [Thu05]. Thuillier begins by defining harmonic functions as certain piecewise
linear functions satisfying a balancing condition; see [Thu05, §2.3] or 3.2. He then
defines a subharmonic function to be an upper semicontinuous function u: X → R ∪
{−∞} such that, for every strictly affinoid domain U ⊂ X and every harmonic function
h on U such that u ≤ h on ∂ U, we have u ≤ h on U. Thuillier shows that subharmonic
functions on smooth non-Archimedean curves satisfy the properties one would expect,
in analogy to the complex case.
   In higher dimensions, it is not completely clear yet what is the best definition for
plurisubharmonic functions. There is the global approach by Zhang [Zha95], who de-
fines a semipositive metric on a line bundle L over a projective k-variety X to be the
uniform limit of metrics induced by nef models. This approach is used in Arakelov ge-
ometry for various arithmetic applications. For an ample class θ on X , Boucksom and
Jonsson [BJ22] give a far reaching global pluripotential theory on a projective variety
over a trivially valued field. Some parts work for any non-Archimedean field, at least in
residue characteristic zero. These psh functions might be singular, and the definition uses
decreasing limits of semipositive model functions as in Zhang’s approach. Chambert–Loir
and Ducros [CD25] have posted a second version of their work in which they give a new
definition of psh functions which is functorial and is based on a transfinite regularization
process.
   In all of the above approaches, a maximum principle for plurisubharmonic functions
is missing. In this paper, we propose another class of psh functions called classically
plurisubharmonic functions in close analogy to the complex case. The definition is local,
the functions are upper semicontinuous, and we will show that properties (1)–(4) are
satisfied. It will be clear that classically psh functions form a maximal class of reasonable
plurisubharmonic functions that is compatible with Thuillier’s definition for curves. In
particular, the psh functions from the above are classically psh (see 1.2 below).
   To get regularization by smooth psh functions in the sense of Chambert-Loir and Ducros
or to define a Monge–Ampère measure for psh functions, additional hypotheses as in
[CD25] might be needed, but that is not the subject of this paper.

1.1. Subharmonic functions on arbitrary k-analytic curves. In Section 3, we define
subharmonic functions on any k-analytic curve X to be the elements of the following
subsheaf of the sheaf of upper semicontinuous functions on X with range [−∞, ∞).
It is the smallest subsheaf that is functorial with respect to pullback, stable under base
change, and agrees with Thuillier’s subharmonic functions on smooth k-analytic curves.
We will show in Proposition 3.5 that subharmonic functions satisfy the properties (1)–(3)
as in the complex case, and the local maximum principle on the interior Int(X ) = X \ ∂ X .

1.2. Plurisubharmonic functions on k-analytic spaces. We define classically plurisub-
harmonic functions on k-analytic spaces as the elements of the smallest subsheaf of the
sheaf of upper semicontinuous functions with range [−∞, ∞) that is functorial with
             CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES              3

respect to pullback, stable under base change, and agrees with the above defined sheaf
of subharmonic functions on k-analytic curves. In Section 4, we will show that classically
psh functions satisfy properties (1)–(3).
   We use the terminology classically psh to distinguish from the psh functions introduced
by Chambert-Loir and Ducros in [CD25]. Note that psh functions are classically psh.


## Literal published source Thuillier: source-extracts/Thuillier-curve-equation-and-regularization.txt

Corollaire 3.4.13.  Soit X une ourbe stri tement k -analytique lisse, onnexe et iso-
morphe à une omposante onnexe de l'intérieur d'un espa e k-anoïde ou à l'analytiée
d'une ourbe k-algébrique ane . L'appli ation
                                D0 (X) → D1 (X),     T 7→ ddc T
induit une bije tion de SH(X)/Γ(X, HX ) sur l'ensemble des mesures de Radon positives sur
l'espa e topologique lo alement ompa t |X|.

   Considérons maintenant une ourbe stri tement k-analytique propre et lisse X et spé iali-
sons e qui pré ède dans le as d'un ouvert onnexe Ω de X tel que ∂Ω soit une partie non
vide de I(X).
Lemme 3.4.14.  Il existe, pour tout point x ∈ Ω, une unique fon tion gx ∈ SH(Ω) telle
que                    
                          ddc gx = δx
                          limy∈Ω, y→ζ gx (y) = 0 pour tout ζ ∈ ∂Ω
Démonstration. L'uni ité dé oule du prin ipe du maximum.
   Supposons tout d'abord que le point x appartienne à I(Ω) ; quelle que soit la omposante
 onnexe c de Ω−{x}, l'existen e d'une barrière en tout point de ∂c (proposition 3.1.20) garan-
tit l'existen e, pour tout nombre réel λ, d'une unique fon tion ontinue gλ sur c, harmonique


## Literal published source Thuillier: source-extracts/Thuillier-regularization.txt

toujours grâ e à la formule de Poin aré-Lelong, sa ourbure est [κ(x) : k]µ.                       2
  Le théorème 3.4.2 se généralise sans di ulté au as de fais eaux inversibles munis de
métriques sous-harmoniques.
Théorème 3.4.19.  Soit L un fais eau inversible sur une                    ourbe stri tement k-
analytique propre et lisse. Pour toute métrique sous-harmonique ||.|| sur L, la restri tion de ||.||
à Ω est l'enveloppe supérieure d'une famille roissante (||.||λ ) de métriques sous-harmoniques
lisses sur L|Ω et le ourant c1 (L, ||.||)|Ω est la limite des ourants c1 (L, ||.||λ ).
Démonstration. La preuve du théorème 3.4.2 s'adapte sans di ulté à la situation présente.
Quel que soit le sous-ensemble ni S de I(X) tel que L soit trivial sur l'adhéren e de ha une
des omposantes onnexes de Y − S , il existe une unique métrique sous-harmonique lisse
||.||S sur L telle que, pour tout U ∈ π0 (X − S) et toute trivialisation ε de L au voisinage
de U , − log ||ε||S soit l'élément de Γ(U, HX ) ∩ C0 (U , R) qui oïn ide ave − log ||ε|| sur ∂U :
  ette formule dénit en eet ||.||S sans ambiguité en vertu de l'harmoni ité des fon tions de
transitions − log |f | et la sous-harmoni ité s'obtient omme elles des fon tions uS au théorème
3.4.2.
98



   De la sous-harmoni ité de ||.|| dé oule que les métriques ||.||S forment une famille rois-
sante lorsque S par ourt l'ensemble ltrant des parties nies de I(Y ) satisfaisant aux ondi-
tions pré édentes. Son enveloppe supérieure est la métrique ||.|| (même argument que dans la
démonstration du théorème 3.4.2).                                                          2

  Étant donnés une ourbe stri tement k-analytique onnexe, propre et lisse X et un point
x ∈ I(X), il existe, pour toute mesure de Radon positive µ sur X , un unique ourant T ∈
D0 (X) tel que
                                               R   
                                   ddc T = µ − X µ δx
                                   T (x) = 0
(théorème 3.3.13) et, vu le théorème 3.4.12, la ondition ddc T|X−{x} ≥ 0 implique que le
 ourant T|X−{x} se prolonge naturellement en une fon tion sous-harmonique sur X − {x}.
   Nous noterons gx,µ l'unique fon tion X → R ∪ {−∞} qui est sous-harmonique sur X − {x}
et satisfait aux onditions                        R  
                                    ddc gx,µ = µ − X µ δx
                                    gx,µ (x) = 0.
     La formule
                                  gy,µ = gx,µ + (gy,x − gx,µ (y))
est immédiate pour tous points x, y ∈ I(X) ; puisque gx,y est une fon tion ontinue (et même
lisse), elle implique en parti ulier la semi- ontinuité supérieure de gx,µ sur l'espa e X tout
entier.
Remarque 3.4.20.  La fon tion gx,µ est négative.
   Appliqué à la mesure δD asso iée à un diviseur ee tif, e qui pré ède dénit sur le fais-
 eau inversible OX (D) une métrique lisse et sous-harmonique ||.|| de ourbure deg(D)δx :
− log ||1D || = −gx,δD .
   En parti ulier : tout fais eau inversible de degré 0 sur X peut être muni d'une métrique
harmonique.


## Literal published source Berkovich: source-extracts/Berkovich-title.txt

P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.




 V LADIMIR G. B ERKOVICH
 Étale cohomology for non-Archimedean analytic spaces
 Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161
 <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>




      © Publications mathématiques de l’I.H.É.S., 1993, tous droits réservés.
      L’accès aux archives de la revue « Publications mathématiques de l’I.H.É.S. » (http://
      www.ihes.fr/IHES/Publications/Publications.html) implique l’accord avec les conditions géné-
      rales d’utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou im-
      pression systématique est constitutive d’une infraction pénale. Toute copie ou impression de
      ce fichier doit contenir la présente mention de copyright.




                               Article numérisé dans le cadre du programme
                             Numérisation de documents anciens mathématiques
                                           http://www.numdam.org/
                                ETALE COHOMOLOGY
                       FOR NON-ARCHIMEDEAN ANALYTIC SPACES
                                                      by VLADIMIR G. BERKOVIGH (1)


                                                                                CONTENTS


INTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   7


## Literal published source 1204.6277: source-extracts/1204.6277-title-and-version.txt

                                          FORMES DIFFÉRENTIELLES
                                          RÉELLES ET COURANTS SUR LES
arXiv:1204.6277v2 [math.AG] 25 Jul 2025




                                          ESPACES DE BERKOVICH




                                                         Antoine Chambert-Loir
                                                                Antoine Ducros
Antoine Chambert-Loir
Université Paris Cité, Institut de Mathématiques de Jussieu-Paris Rive Gauche,
F-75013, Paris, France.
E-mail : antoine.chambert-loir@math.univ-paris-diderot.fr
Antoine Ducros
Sorbonne Université, Université de Paris, CNRS, Institut de Mathématiques de
Jussieu-Paris Rive Gauche, IMJ-PRG, F-75005, Paris, France.
E-mail : antoine.ducros@imj-prg.fr






## Literal published source 1712.00980: source-extracts/1712.00980-title-and-introduction.txt

                                                 CONTINUITY OF PLURISUBHARMONIC ENVELOPES IN
                                                  NON-ARCHIMEDEAN GEOMETRY AND TEST IDEALS
                                               (WITH AN APPENDIX BY JOSÉ IGNACIO BURGOS GIL AND
                                                                MARTÍN SOMBRA)

                                                WALTER GUBLER, PHILIPP JELL, KLAUS KÜNNEMANN, AND FLORENT MARTIN
arXiv:1712.00980v3 [math.AG] 22 Nov 2018




                                                   Abstract. Let L be an ample line bundle on a smooth projective variety X over a
                                                   non-archimedean field K. For a continuous metric on Lan , we show in the following
                                                   two cases that the semipositive envelope is a continuous semipositive metric on Lan
                                                   and that the non-archimedean Monge-Ampère equation has a solution. First, we prove
                                                   it for curves using results of Thuillier. Second, we show it under the assumption that
                                                   X is a surface defined geometrically over the function field of a curve over a perfect
                                                   field k of positive characteristic. The second case holds in higher dimensions if we
                                                   assume resolution of singularities over k. The proof follows a strategy from Boucksom,
                                                   Favre and Jonsson, replacing multiplier ideals by test ideals. Finally, the appendix by
                                                   Burgos and Sombra provides an example of a semipositive metric whose retraction is
                                                   not semipositive. The example is based on the construction of a toric variety which
                                                   has two SNC-models which induce the same skeleton but different retraction maps.

                                                   MSC: Primary 32P05; Secondary 13A35, 14G22, 32U05




                                                                                       Contents
                                             1. Introduction                                                                                    2
                                             2. Model metrics, semipositive metrics, and envelopes                                              5
                                             3. Continuity of plurisubharmonic envelopes on curves                                              9
                                             4. Asymptotic test ideals                                                                         14
                                             5. Descent for model functions                                                                    15
                                             6. Resolution of singularities                                                                    16
                                             7. Uniform convergence to the envelope of the zero function                                       17
                                             8. Continuity of the envelope                                                                     20
                                             9. The Monge–Ampère equation                                                                      22
                                             Appendix A. The skeleton and the retraction in the toric case
                                                           by José Ignacio Burgos Gil and Martín Sombra                                        24
                                             References                                                                                        30



                                              Date: November 26, 2018.
                                              W. Gubler, K. Künnemann and F. Martin were supported by the collaborative research center SFB
                                           1085 funded by the Deutsche Forschungsgemeinschaft. P. Jell was for part of this work also supported by
                                           the SFB 1085 and for the other part by the DFG Research Fellowship JE 856/1-1. J. I. Burgos was par-
                                           tially supported by MINECO research projects MTM2016-79400-P and by ICMAT Severo Ochoa project
                                           SEV-2015-0554. M. Sombra was partially supported by the MINECO research project MTM2015-65361-
                                           P and through the "María de Maeztu" program for units of excellence MDM-2014-0445.
                                                                                             1
2                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


                                    1. Introduction
   Let L be an ample line bundle on an n-dimensional complex projective variety X and
let µ be a smooth volume form on the associated complex manifold X an of total mass
degL (X). The Calabi conjecture claims that there is a smooth semipositive metric k k
on Lan , unique up to positive multiples, solving the Monge–Ampère equation
(1.1)                                c1 (L, k k)∧n = µ.
This was conjectured by Calabi who proved uniqueness [Cal54, Cal57] and the existence
part was solved by Yau [Yau78]. In fact, they proved a more general version in the
setting of compact Kähler manifolds, but this will not be relevant for our paper.
   The motivation of this paper is the study of the non-archimedean version of this
conjecture. We consider a non-archimedean field K with valuation ring K ◦ . Let L be
an ample line bundle on an n-dimensional smooth projective variety X over K. The line
bundle L induces a line bundle Lan on the analytification X an of X as a Berkovich non-
archimedean analytic space. In non-archimedean geometry, model metrics on Lan play
a similar role as smooth metrics on line bundles on complex manifolds. We call a model
metric on Lan semipositive if it is induced by an nef model. Zhang [Zha95] introduced
continuous semipositive metrics on Lan as uniform limits of semipositive model metrics.
For such metrics, Chambert-Loir [CL06] defined a Monge–Ampère measure c1 (L, k k)∧n
on X an which is a positive Radon measure of total mass degL (X). These measures
play an important role in arithmetic equidistribution results (see [Yua08]). We refer to
Section 2 for details about these notions.
   In the non-archimedean Calabi–Yau problem, one looks for continuous semipositive
metrics on Lan solving the Monge–Ampère equation (1.1). Yuan and Zhang [YZ17]
proved that such a metric is unique up to constants. The existence of a singular semi-
positive solution was proven in the case of curves by Thuillier [Thu05, Cor. 3.4.13].
Liu [Liu11] proved existence of a continuous semipositive solution for totally degenerate
abelian varieties A if µ is a smooth volume form on the canonical skeleton of A.
   Next, we describe the fundamental existence result of Boucksom, Favre and Jonsson
[BFJ16a, BFJ15]. We assume that K is a complete discretely valued field with valuation
ring K ◦ . We recall that an SNC-model is a regular model of X such that the special
fiber has simple normal crossing support. Boucksom, Favre and Jonsson prove in [BFJ15,
Thm. A] that the non-archimedean Calabi–Yau problem has a continuous semipositive
solution k k if the following assumptions are satisfied:
    (a) The characteristic of the residue field K̃ is zero.
    (b) The positive Radon measure µ is supported on the skeleton of a projective SNC-
        model of X and satisfies µ(X an ) = degL (X).
    (c) The smooth projective variety X is of geometric origin from a 1-dimensional
        family over K̃.
The last condition will play an important role in this paper. More generally, we say
that X is of geometric origin from a d-dimensional family over the field k if there is a
codimension 1 point b in a normal variety B over k such that K ◦ is the completion of
OB,b and such that X is defined over the function field k(B). In [BGJKM16, Thm. D],
we have shown that (c) is not necessary for the existence of a continuous semipositive
solution of the non-archimedean Calabi–Yau problem if we assume (a) and (b).
   We will later look for a similar result in equicharacteristic p > 0. To do so, we have to
understand the basic ingredients in the proof of the existence result of Boucksom, Favre
and Jonsson. In [BFJ16a], the authors develop a global pluripotential theory on X an
                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                3


for singular semipositive metrics using the piecewise linear structure on the skeletons
of SNC-models. It is here where Assumption (a) enters the first time as resolution of
singularities is used to have sufficiently many SNC-models of X at hand. For a continuous
metric k k, we define the semipositive envelope P (k k) by
(1.2) P (k k) := inf{k k0 | k k ≤ k k0 and k k0 is a semipositive model metric on Lan }.
It is absolutely crucial for pluripotential theory to prove that P (k k) is continuous as this
is equivalent to the monotone regularization theorem (see [BFJ16a, Lemma 8.9]). The
monotone regularization theorem is the basis in [BFJ15] to introduce the Monge–Ampère
measure, capacity and energy for singular semipositive metrics. The proof of continuity
of P (k k) in [BFJ16a, §8] uses multiplier ideals on regular projective models. In the proof
of the required properties of multiplier ideals (see [BFJ16a, Appendix B]), the authors
use vanishing results which hold only in characteristic zero, and hence Assumption (a)
plays an important role here as well.
   A second important result is the orthogonality property for P (k k) given in [BFJ15,
Thm. 7.2]. Multiplier ideals occur again in their proof and it is here where the geometric
assumption (c) is used. However, it is shown in [BGJKM16, Thm. 6.3.3] that continuity of
P (k k) is enough to prove the orthogonality property without assuming (a) or (c). Then
the variational method of Boucksom, Favre and Jonsson can be applied to prove existence
of a continuous semipositive solution for the non-archimedean Calabi–Yau problem.
   This makes it very clear that continuity of the semipositive envelope P (k k) plays a
crucial role in the non-archimedean Calabi–Yau problem. It is the main object of study
in this paper. In Section 2, we will study the basic properties of a slight generalization of
P (k k) which is called the θ-psh envelope for a closed (1, 1)-form θ on X. For the sake of
simplicity, we will restrict our attention in the introduction to the semipositive envelope
P (k k), while all the results hold more generally for the θ-psh envelope assuming that
the de Rham class of θ is ample.
   In Section 3, we will look at continuity of the semipositive envelope in the case of a
smooth projective curve X over an arbitrary complete non-archimedean field K. Poten-
tial theory on the curve X an was developed in Thuillier’s thesis [Thu05]. We will use
Thuillier’s results and the slope formula of Katz, Rabinoff, and Zureick-Brown [KRZB16,
Thm. 2.6] to prove:
Theorem 1.1. Let L be an ample line bundle on a smooth projective curve X over any
non-archimedean field K. Then P (k k) is a continuous semipositive metric on Lan for
any continuous metric k k on Lan .
   A slightly more general version will be proved in Theorem 3.1. The following is
important in the proof: Let L be any line bundle on the smooth projective curve X. We
assume that X has a strictly semistable model X such that Lan has a model metric k k0
associated to a line bundle on X . For any metric k k on Lan , we consider the function
ϕ := − log(k k/k k0 ). Let pX : X an → ∆ be the canonical retraction to the skeleton ∆
associated to X . Then
(1.3)                               k k∆ := e−ϕ◦pX k k0
is a metric on Lan which does not depend on the choice of k k0 . The following result is
crucial in the proof of Theorem 1.1:
Proposition 1.2. Using the hypotheses above, we consider a model metric k k of Lan .
Then we have the following properties:
    (i) The metric k k∆ is a model metric.
4                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


     (ii) There is an equality of measures c1 (L, k k∆ ) = (pX )∗ (c1 (L, k k)).
    (iii) If k k is semipositive, then k k∆ is semipositive and k k∆ ≤ k k.
   This will be proven in Propositions 3.5 and 3.8. It would make pluripotential theory
and the solution of the non-archimedean Calabi–Yau problem much easier if Proposition
1.2 would also hold in higher dimensions as we could work more combinatorically on
skeletons. It is still true that k k∆ is a model metric which satisfies k k∆ ≤ k k. Burgos
and Sombra show in a two dimensional toric counterexample in the Appendix that k k∆
does not have to be semipositive.
   We show now that Proposition 1.2 is also crucial for the existence of the solution of the
non-archimedean Calabi–Yau problem in the case of curves arguing as in [BFJ16b, §9].
By Thuillier [Thu05, Cor. 3.4.13], there is a semipositive metric k k solving (1.1), but it
might be singular. Here, semipositive means that the metric is an increasing pointwise
limit of semipositive model metrics of the ample line bundle L. If we assume that the
positive Radon measure µ has support in the skeleton ∆ of a strictly semistable model X
of X, then it follows easily from Proposition 1.2 that k k∆ is a continuous semipositive
metric solving (1.1). Burgos and Sombra show in their counterexample in the Appendix
that this does not hold in higher dimensions either.
   To look for solutions of the higher dimensional non-archimedean Monge–Ampère equa-
tion in positive characteristic, we will replace the use of multiplier ideals by the use of test
ideals. Test ideals were introduced by Hara and Yoshida [HY03] using a generalization
of tight closure theory. In Section 4, we will gather the necessary facts about test ideals
mainly following [Mus13] and so we work on a smooth variety X over a perfect field k
of characteristic p > 0. Similarly as in the case of multiplier ideals, one can define an
asymptotic test ideal τ (λkDk) of exponent λ ∈ R≥0 for a divisor D on X. Crucial for us
is that τ (λkDk) satisfies a subadditivity property and the following uniform generation
property:
Theorem 1.3. Let X be a projective scheme over a finitely generated k-algebra R such
that X is a smooth n-dimensional variety over k. We assume that H is an ample and
basepoint-free divisor, D is a divisor with h0 (X, O(mD)) 6= 0 for some m ∈ N>0 and E
is a divisor such that the Q-divisor D − λE is nef for some λ ∈ Q≥0 . Then the sheaf
OX (KX/k + E + dH) ⊗OX τ (λ · kDk) is globally generated for all d ≥ n + 1.
   This was proven by Mustaţă if X is projective over k. As we will later work over
discrete valuation rings, we need the more general version with X only projective over
R. This will be possible in Theorem 4.6 as we can replace the use of Fujita’s vanishing
theorem in Mustaţă’s proof by Keeler’s generalization.
   Now we come to the non-archimedean Calabi–Yau problem in equicharacteristic p >
0. For the remaining part of the introduction, we now fix an n-dimensional smooth
projective variety X over a complete discretely valued field K of characteristic p. To
apply the results on test ideals, we have to require that X is of geometric origin from a
d-dimensional family over a perfect field k. We also fix an ample line bundle L on X.
Theorem 1.4. Under the hypotheses above, we assume that resolution of singularities
holds over k in dimension d + n. Then the semipositive envelope P (k k) of a continuous
metric k k on Lan is a continuous semipositive metric on Lan .
  For the precise definition about resolution of singularities, we refer to Definition 6.1.
As resolution of singularities is known in dimension 3 over a perfect field by a result of
Cossart and Piltant [CP09, Thm. p. 1839], Theorem 1.4 is unconditional if X is a smooth
projective surface of geometric origin from a 1-dimensional family over k.
                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                              5


   In Section 7, we will prove Theorem 1.4 in the case when k k is a model metric
associated to a model which is also defined geometrically over k. We will follow the
proof of Boucksom, Favre, and Jonsson, replacing multiplier ideals by test ideals. As
we use a rather weak notion of resolution of singularities, a rather subtle point in the
argument is necessary in the proof of Lemma 7.5 which involves a result of Pépin about
semi-factorial models. Theorem 1.4 will be proved in full generality in Section 8 using
the ddc -lemma and basic properties of the semipositive envelope. In fact, we will prove
in Theorem 8.2 a slightly more general result.
   If we use additionally that embedded resolution of singularities (see Definition 6.2)
holds over k in dimension d + n, then the family of projective SNC-models will be cofinal
in the category of all models of X. We will see in Section 9 that this and Theorem
1.4 allow us to set up the pluripotential theory from [BFJ16a] on X an . By [BFJ15,
Thm. 7.2] again, the continuity of P (k k) yields that the orthogonality property holds for
any continuous metric on Lan . We will use this in Section 9 to show that the variational
method of Boucksom, Favre and Jonsson proves the following result (see Theorem 9.3).
Theorem 1.5. Let X be an n-dimensional smooth projective variety of geometric origin
from a d-dimensional family over a perfect field k of characteristic p > 0. We assume
that resolution of singularities and embedded resolution of singularities hold over k in
dimension d + n. Let L be an ample line bundle on X and let µ be a positive Radon mea-
sure supported on the skeleton of a projective SNC-model of X with µ(X an ) = degL (X).
Then the non-archimedean Monge–Ampère equation (1.1) has a continuous semipositive
metric k k on Lan as a solution.
  Cossart and Piltant [CP08, CP09] have shown resolution of singularities and embed-
ded resolution of singularities in dimension 3 over a perfect field, hence Theorem 1.5
holds unconditionally for a smooth projective surface X of geometric origin from a 1-
dimensional family over the perfect field k.
Acknowledgement. We thank Mattias Jonsson for his valuable comments on a first
version, Matthias Nickel for helpful discussions, and the referee for his useful remarks.

                            Notations and conventions
  Let X be a scheme. An ideal in OX is a quasi-coherent ideal sheaf in OX . A divisor
on X is always a Cartier divisor on X. Given m ∈ N we write X (m) for the set of all
p ∈ X where the local ring OX,p has Krull dimension m. Let k be a field. A variety X
over k is an integral k-scheme X which is separated and of finite type. A curve (resp.
surface) is a variety of dimension one (resp. two).
  Throughout this paper (K, | |) denotes a complete non-archimedean valued field with
valuation ring K ◦ and residue field K̃. Starting in Section 7 we will assume furthermore
that the valuation is discrete and that K has positive characteristic p > 0. In this case
                                   ∼
there exists an isomorphism K ◦ −→ K̃[[T ]] [Mat89, Thm. 29.7]. Let X be a K-variety.
We denote the analytification of X in the sense of Berkovich [Ber90, Thm. 3.4.1] by X an .

            2. Model metrics, semipositive metrics, and envelopes
  Let X be a proper variety over a complete non-archimedean valued field (K, | |).
2.1. A model of X is given by a proper flat scheme X over S := Spec K ◦ together with


## Literal published source 1712.00980: source-extracts/1712.00980-model-envelope-and-descent.txt

in Xs . We call a line bundle L on X nef if the class of L in N 1 (X /S) is nef.
2.4. We define Z 1,1 (X)Q as the direct limit
(2.1)                           Z 1,1 (X)Q := lim N 1 (X /S)Q ,
                                              −→
where X runs over the isomorphism classes of models of X. The space of closed (1, 1)-
forms on X is defined as Z 1,1 (X) := Z 1,1 (X)Q ⊗Q R. Let L be a line bundle on X. Let
k k be a model metric on Lan which is determined on X by a model L of L⊗m . We
multiply the class of L in N 1 (X /S)Q by m−1 which determines a well defined class
c1 (L, k k) ∈ Z 1,1 (X)Q ⊆ Z 1,1 (X) called the curvature form c1 (L, k k) of (L, k k). We
have a natural map ddc : D(X) → Z 1,1 (X); f 7→ c1 (OX , k ktriv · e−f ).
    A closed (1, 1)-form θ is called semipositive if it is represented by a nef element θX ∈
N 1 (X /S) for some model X of X. We say that a model metric k k on Lan for a line
bundle L on X is semipositive if the same holds for the curvature form c1 (L, k k).
2.5. For θ ∈ Z 1,1 (X) we denote by
             PSHD (X, θ) = {f ∈ D(X) | θ + ddc f ∈ Z 1,1 (X) is semipositive}
the set of θ-plurisubharmonic (θ-psh for short) model functions. Recall from [GM16,
Prop. 3.12] that the set PSHD (X, θ) is stable under the formation of max.
2.6. If Y is a proper variety over an arbitrary field k, we denote by N 1 (Y )Q the rational
vector space Pic (Y )⊗Q modulo numerical equivalence. Similarly, we denote by N 1 (Y ) =
N 1 (Y )Q ⊗Q R the real vector space Pic (Y ) ⊗ R modulo numerical equivalence. A class
in N 1 (Y ) is called ample if it is an R>0 -linear combination of classes induced by ample
line bundles on Y . An element α ∈ N 1 (Y )Q (resp. α ∈ N 1 (Y )) is called nef if α · C ≥ 0
for all closed curves C in Y .
                      CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                7


2.7. The restriction maps N 1 (X /S) → N 1 (X), [L ] 7→ [L |X ] induce a linear map
{ } : Z 1,1 (X) −→ N 1 (X), θ 7→ {θ}. We call {θ} the de Rham class of θ.
Definition 2.8. Let X be a projective variety over K and θ ∈ Z 1,1 (X) with de Rham
class {θ} ∈ N 1 (X). The θ-psh envelope Pθ (u) of u ∈ C 0 (X an ) is the function
(2.2)   Pθ (u) : X an → R ∪ {−∞}, Pθ (u)(x) = sup{ϕ(x) | ϕ ∈ PSHD (X, θ) ∧ ϕ ≤ u}.
   Note that Pθ (u) is a real valued function if and only if there exists a θ-psh model
function. For the existence of a θ-psh model function, it is necessary that the de Rham
class {θ} is nef (see [GM16, 4.8] and [BFJ16a, Rem. 5.4]). If {θ} is ample, then there
exists always a θ-psh model function and hence Pθ (u) is a real valued function. If there
is no θ-psh function, then Pθ (u) ≡ −∞ by definition.
   If the residue characteristic is zero and if the de Rham class {θ} is ample, our defi-
nition of Pθ (u) is by [BFJ16a, Thm. 8.3 and Lemma 8.9] equivalent to the definition of
Boucksom, Favre, and Jonsson in [BFJ16a, Def. 8.1] .
   The next proposition collects elementary properties of envelopes.
Proposition 2.9. Let u, u0 ∈ C 0 (X an ) and θ, θ0 ∈ Z 1,1 (X).
     (i) If u ≤ u0 then Pθ (u) ≤ Pθ (u0 ).
    (ii) We have Ptθ+(1−t)θ0 (tu + (1 − t)u0 ) ≥ tPθ (u) + (1 − t)Pθ0 (u0 ) for all t ∈ [0, 1].
   (iii) We have Pθ (u) + c = Pθ (u + c) for each c ∈ R.
    (iv) We have Pθ (u) − v = Pθ+ddc v (u − v) for each v ∈ D(X).
     (v) If Pθ (u) 6≡ −∞, then we have supX an |Pθ (u) − Pθ (u0 )| ≤ supX an |u − u0 |.
    (vi) If θ is determined on a model X , if the de Rham class {θ} is ample and if
         θm → θ in N 1 (X /S), then Pθm (u) → Pθ (u) uniformly on X an .
   (vii) We have Ptθ (tu) = tPθ (u) for all t ∈ R>0 .
  (viii) Assume Pθ (u) 6≡ −∞. Then the envelope Pθ (u) is continuous if and only if it is
         a uniform limit of θ-psh model functions.
Proof. The proof of Properties (i)–(vi) in [BFJ16a, Prop. 8.2] works in our setup as well.
For (vi) it was used that an ample line bundle extends to an ample line bundle on a
sufficiently high model which holds in our more general setting by [GM16, Proposition
4.11]. Property (vii) is obvious for t ∈ Q>0 and an easy approximation argument then
shows (vii) in general. We have seen that θ-psh model functions are closed under max
and hence the θ-psh model functions ϕ ≤ u form a directed family. We conclude that
(viii) follows from Dini’s Theorem for nets [Kel75, p. 239] and the definition of Pθ (u). 
  For the next proposition, we assume for simplicity that the valuation on K is discrete.
Proposition 2.10. Let L be an ample line bundle on X, L an extension to a model X
and θ = c1 (L, k kL ) ∈ Z 1,1 (X). For m > 0 let
                      am = Im H 0 (X , L ⊗m ) ⊗K ◦ L ⊗−m → OX
                                                              
(2.3)
be the m-th base ideal of L and ϕm := m−1 log |am |. Then ϕm ∈ PSHD (X, θ) and
(2.4)                            lim ϕm = sup ϕm = Pθ (0)
                                m→∞          m∈N

pointwise on X an .
Proof. This is shown as in Step 1 of the proof of [BFJ16a, Thm. 8.5]. Observe that the
arguments which show (2.4) in loc. cit. on the subset of quasimonomial points give us
(2.4) immediately on X an using our different definition of the θ-psh envelope.     
8                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


Proposition 2.11. Let K 0 /K be a finite normal extension and let q : X 0 := X ⊗K K 0 →
X be the natural projection. For θ ∈ Z 1,1 (X) and u ∈ C 0 (X an ), we have
(2.5)                             q ∗ (Pθ (u)) = Pq∗ θ (q ∗ (u)).
Proof. Splitting the extension K 0 /K into a purely inseparable part and a Galois part,
we can reduce to two cases. In the first case of a purely inseparable extension, the result
follows from Lemma 2.13 below. In the second case of a Galois extension, we can apply
the argument of [BFJ15, Lemma A.4].                                                      
Remark 2.12. (i) We always equip strictly K-analytic spaces with the G-topology induced
by the strictly K-affinoid domains. We refer to [Ber90, §2.2] for the notion of a strictly
K-affinoid domain and to [Ber93, §1.6] for the construction of the G-topology.
   (ii) We recall from [GM16, Def. 2.8, 2.11] that a piecewise Q-linear function on a
strictly K-analytic space W is a function f : W → R such that there is a G-covering
{Ui }i∈I of W by strictly affinoid domains, analytic functions γi ∈ O(Ui )× and non-zero
mi ∈ N with mi f = − log |γi | on Ui for every i ∈ I. By [GM16, Rem. 2.6, Prop. 2.10],
the notions of model functions and Q-linear functions agree.
Lemma 2.13. Let L be a line bundle on X. Let K 0 /K be a finite purely inseparable
extension and let q : X 0 := X ⊗K K 0 → X be the natural projection. G-topology induced
by the strictly K-affinoid domains. Then the map (X 0 )an → X an is a homeomorphism
and it also identifies the G-topologies. The map q ∗ induces a bijection between the set
of model metrics on L and the set of model metrics on q ∗ (L). Moreover this bijection
identifies semipositive metrics on L and on q ∗ (L).
Proof. As in Remark 2.12 we use the G-topology induced by the strictly K-affinoid
domains. We first prove that the map q : (X 0 )an → X an is a homeomorphism and that
it also identifies the G-topologies. In fact, this follows easily from the following claim:
   Step 1: Let V be a strictly affinoid space over K and V 0 := V ⊗  ˆ K K 0 . Then the natural
projection q : V 0 → V is a homeomorphism which identifies the G-topologies.
   Let pe = [K 0 : K] be the degree of the purely inseparable field extension. It is clear
that for every g ∈ O(V 0 ), there is f ∈ O(V ) with
                                            e
(2.6)                                     g p = f ◦ q.
This property easily shows that q : V 0 → V is a homeomorphism which we read now as
an identification. Using that (2.6) holds also for rational functions g on V 0 and f on V ,
we see that V and V 0 have the same strictly rational domains. By the Gerritzen–Grauert
theorem [BGR84, Cor. 7.3.5/3], we deduce the Step 1.
   Next we prove the bijective correspondence between the model metrics on L and on L0 .
Since L admits a model metric [GM16, 2.1], it is enough to show that we have a bijective
correspondence between model functions on X an and model functions on (X 0 )an . By
Remark 2.12 we may check the same correspondence for Q-linear functions. This may
then be done G-locally and hence the correspondence follows from the following step.
   Step 2: Using the same assumptions as in Step 1, the map f 7→ f ◦q is an isomorphism
from the group of piecewise Q-linear functions on V onto the group of piecewise Q-linear
functions on V 0 .
   Using the above definition of piecewise Q-linear functions, Step 1 and (2.6) yield easily
Step 2.
   To deduce the lemma, it remains to check that the identification between the model
metrics on L and L0 preserves semipositivity. This is an easy consequence of the projec-
tion formula applied to finite morphisms between closed curves in the special fibers of
models.                                                                                   
                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                9


           3. Continuity of plurisubharmonic envelopes on curves
  In this section, K is any field endowed with a non-trivial non-archimedean complete
valuation v : K → R with value group Γ ⊂ R. In this section, we consider a smooth
projective curve X over K. The goal is to prove the following result:
Theorem 3.1. If θ is a closed (1, 1)-form on X an with nef de Rham class {θ} and if
u ∈ C 0 (X an ), then Pθ (u) is a uniform limit of θ-psh model functions and thus Pθ (u) is
continuous on X an .
3.2. As a main tool in the proof, we need strictly semistable models of X and their
canonical skeletons. This construction is due to Berkovich in [Ber99]. We recall here
only the case of a smooth projective curve X over K for which we can also refer to
[Thu05].
   A K ◦ -model X of X as in 2.1 is called strictly semistable if there is an open covering of
X by open subsets U such that there are étale morphisms U → Spec(K ◦ [x, y]/(xy −ρU ))
for some ρU ∈ K ◦◦ . Applying the construction in [Thu05, §2.2] to the associated formal
scheme Xˆ , we get a canonical skeleton S(X ) ⊆ X an with a proper strong deformation
retraction τ : X an → S(X ). The skeleton S(X ) carries a canonical structure of a
metrized graph. We note that the generic fiber of the formal scheme Û intersects S(X )


## Literal published source 1712.00980: source-extracts/1712.00980-test-ideals-resolution-proof.txt

14                  W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


     (ii) If we normalize our non-archimedean volumes by vol(L), can we find an example
          of some model metrics k k and k k0 with irrational vol(L, k k, k k0 )? The idea is
          to avoid the trivial example above.

                               4. Asymptotic test ideals
   We recall definitions and some basic properties from the theory of generalized and
asymptotic test ideals developed in [BMS08, Sect. 2] and [Mus13, Sect. 3]. We refer
to [ST12] for a more comprehensive overview of the theory of test ideals. Let X be a
smooth variety over a perfect field k of characteristic p > 0. Let F : X → X denote
the Frobenius morphism which is induced by the p-th power ring morphism on affine
subsets. Write
                             ωX/k = det ΩX/k = OX (KX/k )
for some canonical divisor KX/k on X.
                                                                    e
   Let a be an ideal in OX and e ∈ N>0 . There is a unique ideal a[p ] in OX such that for
                                      e                                     e
every open affine U in X the ideal a[p ] (U ) in OX (U ) is generated by {up | u ∈ a(U )}.
We have [BMS08, bottom of p. 44]
                                                        e       e
(4.1)                       a(U ) = {a ∈ OX (U ) | ap ∈ a[p ] (U )}
We recall the following facts from [Mus13, p. 540]: There is a canonical trace map
Tr : F∗ (ωX/k ) → ωX/k whose construction can be based on the Cartier isomorphism
[Kat70, Thm. (7.2) and Eq. (7.2.3)]. Mustaţă gives an explicit description of the trace
map [Mus13, top of p. 540]. Given e ∈ N>0 there is an iterated trace map Tre : F∗e (ωX/k ) →
                                                             e
ωX/k . For an ideal a in OX there exists a unique ideal a[1/p ] in OX with
                                                            e
(4.2)                        Tre (F∗e (a · ωX/k )) = a[1/p ] · ωX/k .
                        e
This definition of a[1/p ] is compatible with [BMS08, Def. 2.2]. Hence we have
                                    e [1/pe ]            e [pe ]
(4.3)                            a[p ]         = a ⊆ a[1/p ]
by [BMS08, Lemma 2.4(iv)].
Definition 4.1. [BMS08, Def. 2.9] Given an ideal a in OX and λ ∈ R≥0 one defines the
test ideal of a of exponent λ to be
                                           [      e
                                                      [1/pe ]
                                τ (aλ ) :=     adλp e
                                           e∈N>0

where given r ∈ R we write dre for the smallest integer ≥ r.
                                                                e       e
Remark 4.2.    (i) Observe that we have τ (aλ ) = (adλp e )[1/p ] for large e ∈ N as X is
noetherian. The equality
(4.4)                                τ ((am )λ ) = τ (aλm )
for m ∈ N shows that the notation in Definition 4.1 is compatible with taking powers
of ideals [BMS08, Cor. 2.15]. We have τ (aλ ) ⊆ τ (bλ ) for ideals a ⊆ b in OX [BMS08,
Prop. 2.11(i)].
                                      e       e                                       e       e
  (ii) Choose e such that τ (a) = (a[p ] )[1/p ] . For any ideal b in OX such that a[p ] ⊆ b[p ]
we get a ⊆ b from (4.1). Hence (4.3) implies
(4.5)                                      a ⊆ τ (a).
  Let a• be graded sequence of ideals in OX , i.e. a family (am )m∈N>0 of ideals in OX
such that am · an ⊆ am+n for all m, n ∈ N>0 and am 6= (0) for some m > 0.
                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             15


Definition 4.3. [Mus13, p. 541] Choose λ ∈ R≥0 . Define the asymptotic test ideal of
exponent λ as                             [
                              τ (aλ• ) :=   τ (aλ/m
                                                m ).
                                            m∈N
                                            λ/m
Remark 4.4.      (i) We have τ (aλ• ) = τ (am ) for suitable m ∈ N which are divisible
enough [Mus13, p. 541].
  (ii) For all m ∈ N we have [Mus13, p. 541, l. 4]
(4.6)                                τ (am ) ⊆ τ (am
                                                   • ).
 (iii) For all m ∈ N we have the Subadditivity Property [Mus13, Prop. 3.1(ii)]
(4.7)                               τ (amλ        λ m
                                        • ) ⊆ τ (a• ) .

Definition 4.5. Let D be a divisor on X with h0 (X, OX (mD)) 6= 0 for some m > 0.
Define the asymptotic test ideal of exponent λ ∈ R≥0 associated with X and D as
                                   τ (λ · kDk) := τ (aλ• )
where a• denotes the graded sequence of base ideals for D, i.e. am is the image of the
natural map
                          H 0 (X, O(mD)) ⊗k OX (−mD) → OX .
If D is a Q-divisor such that h0 (X, OX (mD)) 6= 0 for some positive integer m such that
mD is a usual divisor then we put τ (λ · kDk) := τ (λ/r · krDk) for some r ∈ N such that
rD has integral coefficients.
  We finish with a slight generalization of Mustaţă’s uniform generation property [Mus13,
Thm. 4.1]. Observe that in loc. cit. it is required that the variety X is projective over
the ground field k.
Theorem 4.6. Let R be a k-algebra of finite type over a perfect field k of characteristic
p > 0. Let X be an integral scheme of dimension n which is projective over the spectrum
of R and smooth over k. Let D, E, and H be divisors on X and λ ∈ Q≥0 such that
     (i) OX (H) is an ample, globally generated line bundle,
    (ii) h0 (X, OX (mD)) > 0 for some m > 0, and
   (iii) the Q-divisor E − λD is nef.
Then the sheaf OX (KX/k +E +dH)⊗OX τ (λ·kDk) is globally generated for all d ≥ n+1.
Proof. We literally follow Mustaţă’s proof with two modifications. The proof requires
Mumford’s theorem on Castelnuovo-Mumford regularity for the projective scheme X
over R which holds also in this more general setting [BS13, 20.4.13]. Furthermore we
replace the use of Fujita’s vanishing theorem to the sheaves Fj := OX (KX/k + Tj ),
j = 1, . . . , r and the ample divisor (d − i)H by an application of Keeler’s generalization
[Kee03, Thm. 1.5].                                                                         

                          5. Descent for model functions
   Let K denote a complete discretely valued field with valuation ring K ◦ . Let R be
a discrete valuation subring of K ◦ whose completion is K ◦ . Then K is the completion
of the field of fractions F of R. In this section we show that all model functions on
analytifications of varieties over K are already defined over R.
   An R-model of a projective variety over F is defined completely analogously to the
complete case treated in 2.1.
16                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


Definition 5.1. Let X be a projective variety over K. We say that a model function
ϕ : X an → R is defined over R if there exists a projective variety Y over F , with an
isomorphism Y ⊗F K ≃ X, an R-model Y of Y , a vertical divisor D0 on Y such that
ϕ= m 1
       ϕD where m ∈ N>0 and D is the vertical divisor on Y ⊗R K ◦ obtained by pullback
from D0 . Likewise we define the notion of a vertical ideal sheaf defined over R.
     Here is the announced descent result.
Proposition 5.2. Let Y be a projective variety over F and let X := Y ⊗F K.
   (a) Any K ◦ -model of X is dominated by the base change of a projective R-model of
       Y to K ◦ .
   (b) If a projective K ◦ -model X of X dominates Y ⊗R K ◦ for a projective R-model
       Y of Y , then X ≃ Y 0 ⊗R K ◦ for a projective R-model Y 0 of Y dominating Y .
   (c) Every model function on X an is defined over R.
Proof. To prove (a), we pick any projective R-model Y of Y . By [Lü93, Lemma 2.2],
there is a blowing up π : X 0 → Y ⊗R K ◦ such that X 0 dominates X . Since π is a
projective morphism, X 0 is a projective K ◦ -model dominating X . Hence (a) follows
from (b).
   To prove (b), we note that the morphism X → Y ⊗R K ◦ is a blowing up morphism
along a vertical closed subscheme Z of Y ⊗R K ◦ (see [Liu06, Thm. 8.1.24]). Since the
ideal sheaf of Z contains a power of the uniformizer of R, we may define it over R and
hence the same is true for the blowing up morphism and for X proving (b).
   To prove (c), we may assume that the model function is associated to a vertical Cartier
divisor D. Replacing D by D + div(λ) for a suitable non-zero λ ∈ R and using (a) and
(b), we may assume that D is an effective Cartier divisor on a projective R-model Y of
Y . As in (b), we see that the ideal sheaf of D is defined by the ideal sheaf of a Cartier
divisor D0 defined over R proving (c).                                                  

                            6. Resolution of singularities
   For our applications, we need that regular projective models are cofinal in the categroy
of models which makes it necessary to assume resolution of singularities in a certain
dimension.
Definition 6.1. Let k be a field. We say that resolution of singularities holds over k
in dimension n if for every quasi-projective variety Y over k of dimension n there exists
a regular variety Ỹ over k and a projective morphism Ỹ → Y which is an isomorphism
over the regular locus of Y .
  To transfer results from [BFJ16a, BFJ15] to our context, it is essential to show that
projective models are dominated by SNC-models. In order to this we are going to use
the following assumption.
Definition 6.2. We say that embedded resolution of singularities in dimension m holds
over a field k if for every quasi-projective regular variety Y over k of dimension m and
every proper closed subset Z of Y , there is a projective morphism π : Y 0 → Y of quasi-
projective regular varieties over k such that the set π −1 (Z) is the support of a normal
crossing divisor and such that π is an isomorphism over Y \ Z.
   Hironaka has shown that resolution of singularities and embedded resolution of sin-
gularities holds over a field of characteristic zero in any dimension. Resolution of singu-
larities holds over arbitrary fields in dimension one (Dedekind, M. Noether, Riemann)
                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                            17


and in dimension two (Abhyankar, Lipman). Cossart and Piltant have proven that res-
olution of singularities and embedded resolution of singularities hold in dimension three
over perfect fields.
Theorem 6.3 (Cossart-Piltant). Resolution of singularities and embedded resolution of
singularities hold in dimension three over any perfect field.
Proof. This is shown in [CP09, Thm. on p. 1839] and [CP08, Prop. 4.1].                  

      7. Uniform convergence to the envelope of the zero function
   Let K be a complete discretely valued field of positive characteristic p > 0. Let X be
a smooth projective variety over K, L an ample line bundle on X, and (X , L ) a model
of (X, L) over K ◦ . For m ∈ N>0 let am denote the m-th base ideal of L as in (2.3). For


## Literal published source 1712.00980: source-extracts/1712.00980-geometric-test-ideal-proof.txt

a scheme B, we recall our convention B (1) = {p ∈ B | dim OB,p = 1}.
Assumption 7.1. There exist a normal affine variety B over a perfect field k, a codi-
mension one point b ∈ B (1) , a projective regular integral scheme XB over B, and line
bundles LB and AB over XB such that there exist
     (i) a flat morphism h : Spec K ◦ → Spec OB,b → B,
                                           ∼
    (ii) an isomorphism XB ⊗B Spec K ◦ → X ,
                                ∼
   (iii) an isomorphism h∗ LB → L over the isomorphism in (ii),
                                       ∼
   (iv) and an isomorphism AB |XB,η → LB |XB,η where η is the generic point of B and
         the line bundle AB on XB is ample.
Usually we read all the isomorphisms above as identifications.
   Note that all relevant information in Assumption 7.1 is over the discrete valuation
ring OB,b . The next remark makes this statement precise and gives an equivalent local
way to formulate this assumption.
Remark 7.2. Suppose that X and L are defined over a subring R of K ◦ by a line bundle
LR on a projective regular integral scheme XR over R. We assume furthermore that
R is a discrete valuation ring which is defined geometrically by a d-dimensional normal
                                                                              ∼
variety B over a field k, i.e. there exist b ∈ B (1) and an isomorphism h : R → OB,b . We
read the isomorphism h as an identification. Then Assumption 7.1 is equivalent to the
existence of data (R, k, B, b, h, XR , LR ) as above assuming furthermore that the field k
is perfect and the restriction of LR to the generic fiber XR,η over R extends to an ample
line bundle AR on XR .
   One direction of the equivalence is clear by base change from B to Spec OB,b . On the
other hand, replacing B by an open affine neighbourhood of b, it is clear by [EGAIV,
Cor. 9.6.4] that AR extends to an ample line bundle AB on a projective integral scheme
XB over B and that LR extends to a line bundle LB on XB . Since the regular locus
of XB is open [GW10, Cor. 12.52] and since the fiber of XB over b is contained in the
regular locus, we may assume that XB is also regular by shrinking B again.
Theorem 7.3. Let θ be defined by the line bundle L . If the pair (X , L ) satisfies
Assumption 7.1, then (m−1 log |am |)m∈N>0 is a sequence of θ-psh model functions which
converges uniformly on X an to Pθ (0).
   If the field K has equicharacteristic zero, this result was proven by Boucksom, Favre,
and Jonsson [BFJ16a, Thm. 8.5] without Assumption 7.1. We will follow their strategy
of proof replacing the use of multiplier ideals by the use of test ideals. The required
results about test ideals are gathered in Section 4.
18                 W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


Proof. We start with the observation that we have
(7.1)                                Γ(XB , LB⊗m ) 6= 0
for some m > 0. In fact we have
                                                  ∼
                        Γ(XB , LB⊗m ) ⊗R K −→ Γ(X, L⊗m ) 6= 0
by flat base change and the ampleness of L for some m > 0.
  We have a cartesian diagram
                                        g
                               X            / XB


                                                       $
                             Spec K ◦
                                        h   /B        / Spec k.

We observe that XB is a smooth variety over the perfect field k and write
                  aB,m = Im H 0 (XB , LB⊗m ) ⊗k LB⊗−m → OXB
                                                                 

for the m-th base ideal of LB . Consider the ideal g −1 (aB,m ) · OX in OX generated by
g −1 (aB,m ). We have g −1 (aB,m ) · OX = g ∗ aB,m as g is flat. Sections of am are locally
of the form s · t−1 where s ∈ Γ(X , L ⊗m ) is a global section and t is a local section of
L ⊗m . Flat base change [Har77, Prop. III.9.3] gives
                        H 0 (X , L ⊗m ) = H 0 (XB , LB⊗m ) ⊗R K ◦ .
Hence the formation of base ideals is compatible with base change, i.e. we have
(7.2)                        am = g −1 (aB,m ) · OX = g ∗ aB,m
for all m ∈ N>0 .
   The family aB,• = (aB,m )m>0 defines a graded sequence of ideals in the sense of
Section 4. Let bB,m := τ (am
                           B,• ) denote the associated asymptotic test ideal of exponent
m. Motivated by (7.2) we define
                             bm := g −1 bB,m · OX = g ∗ bB,m
as the ideal in OX generated by bB,m . These ideals have the following properties:
     (a) We have am ⊂ bm for all m ∈ N>0 .
     (b) We have bml ⊂ blm for all l, m ∈ N>0 .
     (c) There is m0 ≥ 0 such that A⊗m0 ⊗L ⊗m ⊗bm is globally generated for all m > 0.
Properties (a) and (b) follow from the corresponding properties of aB,m and bB,m men-
tioned in (4.5), (4.6), and (4.7) if we observe (7.2).
   Property (c) is a consequence of the generalization of Mustaţă’s uniform generation
property given in Theorem 4.6. Write LB = O(D) for some divisor D on XB and choose
a divisor H on XB such that O(H) is ample and globally generated. Fix d > dim XB
and a canonical divisor KXB /k on the smooth k-variety XB . As AB is ample we find
some m0 ∈ N such that A⊗m  B
                               0
                                 ⊗ O(−KX/k − dH) is globally generated. Given m ∈ N>0
we put E := mD. Since LB satisfies (7.1), for any m ∈ N>0 we may use E := mD and
λ := m in Theorem 4.6 to see that the sheaf
                            O(KXB /k + dH) ⊗ LB⊗m ⊗ bB,m
is globally generated. As a consequence, our choice of m0 implies that A⊗m
                                                                        B
                                                                          0
                                                                            ⊗ LB⊗m ⊗
bB,m is globally generated. Base change to K ◦ proves (c).
   Now we follow the proof of [BFJ16a, Thm. 8.5]. Step 1 of loc. cit. holds not only
on quasi-monomial points of X an , but pointwise on the whole X an using Proposition
                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             19


2.10 and our different definition of Pθ (0). Then Step 2 of loc. cit. works in our setting
using properties (a), (b), and (c) above. The only difference is that all inequalities hold
immediately on X an and not only on the quasi-monomial points of X an .                  
Corollary 7.4. Let X be a smooth n-dimensional projective variety over K with a
closed (1, 1)-form θ. Let L be a line bundle on a K ◦ -model X of X defining θ and
with L = L |X ample. We assume that (X , L ) is the base change of (XR , LR ) for a
line bundle LR of a projective integral scheme XR over a subring R of K ◦ and that R
is a discrete valuation ring defined geometrically by a d-dimensional normal variety B
over a perfect field k (as in Remark 7.2). If resolution of singularities holds over k in
dimension d + n, then Pθ (0) is a uniform limit of θ-psh model functions and hence Pθ (0)
is continuous on X an .
Proof. It follows from our assumptions that X is base change of the generic fiber XR,η
of XR /R to K. Since X is smooth, we conclude that XR,η is smooth as well [EGAIV,
Cor. 17.7.3]. By Proposition 2.9(vii), it is enough to prove the claim for any positive
multiple of θ. Using this and Lemma 7.5 below, we see that by passing to dominant
models, we may assume that XR is regular and that the restriction of LR to XR,η
extends to an ample line bundle on XR . By Remark 7.2, these conditions are equivalent
to Assumption 7.1 and hence the claim follows from Theorem 7.3.                      
Lemma 7.5. Let R be a discrete valuation ring which is defined geometrically by a d-
dimensional normal variety B over the field k (as in Remark 7.2). Let XR be a projective
integral scheme over R with n-dimensional regular generic fiber X 0 := XR,η . We assume
that resolution of singularities holds over k in dimension d + n. Then for any ample
line bundle L0 on X 0 , there exists m ∈ N>0 and an ample extension LR0 of (L0 )⊗m to a
regular R-model XR0 of X 0 with a projective morphism XR0 → XR over R extending the
identity on X 0 .
Proof. The proof proceeds in three steps. First, we use a result of Lütkebohmert about
vertical blowing ups to show that L0 may be assumed to extend to an ample line bundle
H on XR . In a second step, we show that XR may be also assumed to be semi-factorial
by a theorem of Pépin. In a third step, we use resolution of singularities to construct
our desired regular model XR0 .
    Step 1: Replacing L0 by a positive tensor power, we may assume that L0 has an ample
extension HR to a projective R-model YR . There is a blow up π : ZR → YR in an ideal
sheaf J supported in the special fiber of YR such that the identity on X 0 extends to a
morphism ZR → XR [Lü93, Lemma 2.2]. Then π −1 (J ) = OZR /YR (1) and hence there
is ` ∈ N>0 such that π ∗ (H ⊗` ) ⊗ OZR /YR (1) is ample [Har77, Prop. II.7.10]. We conclude
that by replacing XR by ZR and by passing to a positive tensor power of L0 , we may
assume that L0 has an ample extension HR to XR . This completes the first step.
    Step 2: By a result of Pépin [Pé13, Thm. 3.1], there is a a blowing-up morphism
π : ZR0 → XR centered in the special fiber of XR such that ZR0 is semi-factorial. The
  0

latter means that every line bundle on the generic fiber ZR,η0   of ZR0 over R extends to a
line bundle on ZR0 . Similarly as in the first step, we may assume that a positive tensor
power of L0 extends to an ample line bundle on ZR0 . Replacing XR by ZR0 and L0 by
this positive tensor power, we get the second step.
    Step 3: We may assume that B is affine. Using R = OB,b for some b ∈ B (1) , it is
clear that XR extends to a projective integral scheme XB over B. By using resolution
of singularities over k in dimension d + n, there is a regular integral scheme XB0 and a
projective morphism ϕB : XB0 → XB which is an isomorphism over the regular locus of
20                   W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


XB . Since X 0 is contained in the regular locus of XB , we conclude that ϕB maps the
generic fiber XB,η
                0  of XB0 over B isomorphically onto X 0 = XB,η . As usual, we read this
isomorphism as an identification. Then we get an induced projective morphism
                           ϕR : XR0 := XB0 ×B Spec(R) −→ XR
extending the identity on X 0 . The same argument as in the first step gives m ∈ N>0
such that
                           LR0 := ϕ∗R (HR⊗m ) ⊗ OXR0 /XR (1)
is an ample line bundle on XR0 . Let F be the restriction of OXR0 /XR (1) to XR,η
                                                                              0 =X
                                                                                   R,η =
X . Then LR is a model of (L )
   0          0                 0 ⊗m ⊗ F . To prove the lemma, we have to ensure that F
may be assumed to be OX 0 . To do so, we use that XR is semi-factorial to extend F to
a line bundle FB on XR . Then we may replace OXR0 /XR (1) by OXR0 /XR (1) ⊗ ϕ∗R (F −1 )
to deduce the claim.                                                                   

                           8. Continuity of the envelope
   We present consequences of our application of test ideals in the last subsection under
the assumption that we have resolution of singularities. As in Section 7 let K be a
complete discretely valued field of positive characteristic p > 0. Let X be a smooth


## Literal published source 1712.00980: source-extracts/1712.00980-envelope-and-equation-proof.txt

projective variety over K of dimension n. Consider θ ∈ Z 1,1 (X) with ample de Rham
class {θ} ∈ N 1 (X).
Definition 8.1. We say that X is of geometric origin from a d-dimensional family over
a field k if there exist a normal d-dimensional variety B over k, a point b ∈ B (1) of
codimension one and a projective variety Y over K 0 = k(B) such that
                                               ∼
      (i) there exists an isomorphism O  bB,b →  K ◦ of rings where ObB,b denotes the com-
          pletion of the discrete valuation ring R := OB,b ,
     (ii) an isomorphism Y ⊗K 0 K ≃ X over K with K 0 → K induced by (i).
Usually, we read these isomorphisms as identifications. Moreover, if L is a line bundle
(resp. if θ is a closed (1, 1)-form) on X, we say that (X, L) (resp. (X, θ)) is of geometric
origin from a d-dimensional family over a field k if the above conditions are satisfied and
if we can also find a line bundle L0 on Y inducing L by the base change K/K 0 (resp. a
line bundle LR on an R-model XR of Y inducing θ by the base change K ◦ /R).
     We can now formulate our main result about the continuity of the envelope:
Theorem 8.2. Let X be a smooth n-dimensional projective variety over K of geometric
origin from a d-dimensional family over a perfect field k. Assume that resolution of
singularities holds over k in dimension d + n. If θ is a closed (1, 1)-form on X with
ample de Rham class {θ} and if u ∈ C 0 (X an ), then Pθ (u) is a uniform limit of θ-psh
model functions and thus Pθ (u) is continuous on X an .
  Using resolution of singularities in dimension three over a perfect field proven by
Cossart–Piltant (see Theorem 6.3), we get the following application:
Corollary 8.3. Let X be a smooth projective surface over K of geometric origin from
a 1-dimensional family over a perfect field k. Then the conclusion of Theorem 8.2 holds
unconditionally.
   We will prove Theorem 8.2 in several steps. First, we prove it in a completely geometric
situation:
                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             21


Lemma 8.4. If we assume additionally that (X, θ) is of geometric origin from a d-
dimensional family over a perfect field k, then Theorem 8.2 holds.
Proof. Recall that the space of model functions D(X) is dense in C 0 (X an ) for the topol-
ogy of uniform convergence [Gub98, Thm. 7.12]. Hence we may assume that u ∈ D(X)
by Proposition 2.9(v). Observe that by Proposition 2.9(vii), we may replace (θ, u) by
a suitable multiple. Hence we may assume without loss of generality that the model
function u is defined by a vertical divisor on a K ◦ -model X 0 . It is clear that we can
choose X 0 dominating the geometric model X = XR ⊗R K ◦ of θ from Definition 8.1. It
follows from Proposition 5.2(a) that we may assume X = X 0 . By Proposition 2.9(iv)
we get
(8.1)                            Pθ (u) = Pθ+ddc u (0) + u.
By construction, the class θ+ddc u is induced by a line bundle on X  R and hence Corollary
                                                          c
7.4 yields that Pθ+ddc u (0) is a uniform limit of (θ + dd u)-psh model functions ϕi . Then
Pθ (u) is the uniform limit of the sequence of θ-psh functions ϕi + u by (8.1).          
  In the lemma above we have proven Theorem 8.2 under the additional assumption that
the (1, 1)-form θ is defined geometrically. In the next lemma, we relax this assumption
a bit only assuming that the de Rham class of θ is defined geometrically.
Lemma 8.5. If we assume additionally that the de Rham class {θ} is induced by an
ample line bundle L on X such that (X, L) is of geometric origin from a d-dimensional
family over the perfect field k, then Theorem 8.2 holds.
Proof. By Proposition 2.9(vi), we may assume that θ ∈ Z 1,1 (X)Q . By Proposition
2.9(vii), we may replace L by a positive tensor power and θ by the corresponding multiple,
and so we may assume that L is very ample. In the notation of Definition 8.1, the
assumption that (X, L) is of geometric origin means that L is the pull-back of a line
bundle L0 on the projective variety Y over K 0 = k(B). It follows easily from [Har77,
Prop. III.9.3] and [EGAIV, Prop. 2.7.1(xii)] that L0 is very ample. Then L0 extends to
a very ample line bundle on a projective R-model of Y for the discrete valuation ring
R = OB,b from Definition 8.1. By base change to K ◦ , we conclude that there is a closed
(1, 1)-form θ0 on X an with de Rham class {θ0 } = {θ} such that (X, θ0 ) is of geometric
origin from a d-dimensional family over k.
   By the ddc -lemma in [BFJ16a, Thm. 4.3] (see also the second author’s thesis [Jel16,
Thm. 4.2.7] for generalizations) and using the rationality assumption on θ from the
beginning of the proof, there is v ∈ D(X) such that θ0 = θ + ddc v. It follows from
Proposition 2.9(iv) that
                        Pθ (u) − v = Pθ+ddc v (u − v) = Pθ0 (u − v).
By Lemma 8.4, the function Pθ0 (u − v) is a uniform limit of θ0 -psh functions. Adding v,
we get the claim for Pθ (u).                                                           
   To prove Theorem 8.2 in full generality, the idea is to reduce to the above geometric
situation by a similar trick as in [BFJ15, Appendix A].
Proof of Theorem 8.2. We note first that by Proposition 2.9 (viii) the property that
Pθ (u) is a uniform limit of θ-psh model functions is equivalent to the property that
it is a continuous function. Let K 0 /K be a finite normal extension and denote by
q : X 0 := X ⊗K K 0 → X the natural projection. Let θ0 = q ∗ θ ∈ Z 1,1 (X 0 ). Then by
Lemma 2.11 we have that
                                  q ∗ Pθ (u) = Pθ0 (q ∗ u).
22                  W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


It follows from [Ber90, Prop. 1.3.5] that X an is as a topological space equal to the quotient
of (X 0 )an by the automorphism group of K 0 /K. We conclude that Pθ (u) is continuous
if and only if Pθ0 (q ∗ u) is continuous.
   Hence we can replace K by a finite normal extension. Adapting the same argument as
in [BFJ15, Lemma A.7] to characteristic p, there exists a finite normal extension K 0 /K
and a function field F of transcendence degree d over k with K 0 as completion as in
Definiton 8.1 such that X 0 := X ⊗K K 0 is the base change of a projective variety Y over
F with N 1 (Y /F )Q → N 1 (X 0 /K 0 )Q surjective. Replacing K 0 by K, we can assume that
there is Y as above with a surjective map
(8.2)                            N 1 (Y /F )Q → N 1 (X/K)Q
induced by the natural projection X → Y . To prove continuity of Pθ (u), we may assume
that the de Rham class {θ} is in N 1 (X)Q by using an approximation argument based
on Proposition 2.9(vi). We conclude from surjectivity in (8.2) that there is a non-zero
m ∈ N such that {mθ} is induced by a line bundle L with (X, L) of geometric origin
from a d-dimensional family over k (in fact from Y ). By Proposition 2.9(vii), we have
         1
Pθ (u) = m Pmθ (mu) and hence continuity follows from Lemma 8.5.                     

                          9. The Monge–Ampère equation
   Let K be a field endowed with a complete discrete absolute value. Boucksom, Favre,
and Jonsson have shown in [BFJ16a, BFJ15] that the Monge–Ampère equation for a
Radon measure supported on the skeleton of a smooth projective variety over K has a
solution if the variety is of geometric origin from a one-dimensional family over a field of
characteristic zero. In this section, we will explain that the same is true in characteristic
p > 0 if we assume resolution of singularities (see Section 6 for precise definitions).
   In the following, we work under the following assumptions:
   (A1) The n-dimensional smooth projective variety X over K is of geometric origin
         from a d-dimensional family over a perfect field k of characteristic p > 0.
   (A2) Resolution of singularities holds over k in dimension d + n.
   (A3) Embedded resolution of singularities holds over k in dimension d + n.
   Note that assumptions (A2) and (A3) are unconditional for n = 2 and d = 1 by
Theorem 6.3 of Cossart and Piltant. For the following, it is crucial to have in mind that
models of X can be defined geometrically which follows from Proposition 5.2.
   To transfer the results from [BFJ16a, BFJ15], it is essential to note that every pro-
jective K ◦ -model of X is dominated by a projective SNC-model of X. To see this, we
note first that we may assume that the given K ◦ -model is of geometric origin over the
perfect field k by Proposition 5.2. Using resolution of singularities in dimension d + n
similarly as in the third step of the proof of Lemma 7.5, we deduce that there is a
regular projective scheme XR over R as in Definition 8.1 dominating the given model.
Applying in the same way embedded resolution of singularities in dimension d + n to the
non-smooth fibers of XR over R, we may assume that the singular fibers of XR have
the same support as a strict normal crossing divisor. Then base change to K ◦ yields the
claim as base change of the discrete valuation ring OB,b to its completion K ◦ preserves
regularity [Sta17, Tag 0BG4] and strict normal crossing support.
   Having sufficiently many projective SNC-models of X at hand, the density results of
skeletons in X an given in [BFJ16a, Sect. 3] also hold in our case of equicharacteristic p.
Given a closed (1, 1)-form θ with ample de Rham class {θ}, the notion of θ-psh functions
on X an introduced in [BFJ16a, Sect. 7] keeps the same properties in our case. In fact,
the results of [BFJ16a, Sect. 1–7] and their proofs carry over to our setting.
                     CONTINUITY OF PLURISUBHARMONIC ENVELOPES                                23


   Note that we have already proven the continuity of the θ-psh envelope in Theorem 8.2,
which is the analogue of [BFJ16a, Thm. 8.3], by using test ideals instead of multiplier
ideals. For u ∈ C 0 (X an ), we recall from 2.8 that we have used a different definition of the
θ-psh envelope Pθ (u) than in [BFJ16a, Def. 8.1]. Both definitions agree in the equichar-
acteristic zero situation by [BFJ16a, Thm. 8.3 and Lemma 8.9]. If the characteristic of
K is positive and the Assumptions (A1)–(A3) hold then we have explained above how to
define θ-psh functions. We claim now that in this case both definitions of the envelope
agree as well. Indeed, it follows from [BFJ16a, Lemma 8.4] that the definitions agree on
quasi-monomial points of X an . For any x ∈ X an , we consider the net pX (x) with X
ranging over all SNC models of X. By [BFJ16a, Cor. 3.9], this net of quasi-monomial
points converges to x. It follows from continuity that the net Pθ (u)(pX (x)) converges
to Pθ (u)(x) for our definition of the envelope. By [BFJ16a, Thm. 7.11, Prop. 8.2(i)], the
same convergence holds for their envelope and hence both definitions agree.
   This yields now in the same way as in [BFJ16a, Thm. 8.7] that the following monotone
regularization holds:
Corollary 9.1. Under the assumptions (A1)–(A3), let θ be a closed (1, 1)-form on X an
with ample de Rham class. Then every θ-psh function on X an is the pointwise limit of a
decreasing net of θ-psh model functions on X an .
   In [BFJ15, Sect. 3], the monotone regularization is the basic ingredient to generalize
the Monge–Ampère operator from θ-psh model functions to bounded θ-psh functions and
hence it applies also to our setting leading to the same results as in [BFJ15, Sect. 3]. For
a bounded θ-psh function ϕ, we denote by MAθ (ϕ) the associated Monge-Ampère mea-
sure on X an . The definitions, results and arguments from [BFJ15, Sect. 4–6] carry over
without change. In particular, we may choose a decreasing sequence of θ-psh model func-
tions on X an in the monotone regularization from Corollary 9.1 similarly as in [BFJ15,
Prop. 4.7].
   A crucial step is now to prove the following orthogonality property:
Theorem 9.2. Under the assumptions (A1)–(A3), let θ be a closed (1, 1)-form on X an
with ample de Rham class. Then for every continuous function f on X an with θ-psh
envelope Pθ (f ), we have the orthogonality property
                            Z
                                 (f − Pθ (f ))MAθ (Pθ (f )) = 0.
                              X an
Proof. By Proposition 2.9(vi) and the continuity of the Monge–Ampère measure given
in [BFJ15, Thm. 3.1], we may assume that θ ∈ Z 1,1 (X)Q . Using Proposition 2.9(vii), we
may assume that θ is induced by a line bundle of a model of X. Then the claim follows
from [BGJKM16, Thm. 6.3.2] as Pθ (f ) is continuous by Theorem 8.2.                    
   As a consequence of the orthogonality property, we get differentiability of E ◦ Pθ as
in [BFJ15, Thm. 7.2] where E is the energy from [BFJ15, Sect. 6]. We have now all
ingredients available to solve the following Monge–Ampère equation.
Theorem 9.3. Under the assumptions (A1)–(A3), let θ be a closed (1, 1)-form on X an
with ample de Rham class {θ} and let µ be a positive Radon measure on X an of mass
{θ}n supported on the skeleton of a projective SNC-model. Then there is a continuous
θ-psh function ϕ on X an such that MAθ (ϕ) = µ and ϕ is unique up to additive constants.
Proof. It was shown in [BFJ15, §8.1] that uniqueness follows from a result of Yuan and
Zhang in [YZ17]. To prove existence of a θ-psh solution ϕ, we use the variational method
of Boucksom, Favre, and Jonsson. The basic tools needed here are upper semicontinuity
24                  W. GUBLER, P. JELL, K. KÜNNEMANN, AND F. MARTIN


of the energy [BFJ15, Prop. 6.2], the compactness theorem [BFJ16a, Thm. 7.10], and
the differentiability of E ◦ Pθ . As explained above, all these results are available in our
setting. It remains to see that ϕ is continuous and this is done by estimates in the spirit
of Kolodziej as in [BFJ15, §8.3].                                                         

        Appendix A. The skeleton and the retraction in the toric case
               by José Ignacio Burgos Gil and Martín Sombra
   In this appendix we give a combinatorial description of the skeleton associated to a
toric model of a toric variety, and of the corresponding retraction. We will use this
description to show an example of two models of the same variety that have the same
skeleton but different retractions. In turn this will give a counterexample to a higher
dimensional extension of Proposition 3.8.
   Let (K, | |) be a complete non-archimedean discretely valued field, K ◦ the valuation
ring, k the residue field, and S = Spec(K ◦ ). Let $ be a uniformizer of K ◦ and write
                                      λK = − log |$|.
   Let X be a smooth projective variety over K of dimension n and X an the associated
Berkovich analytic space. Let X be an SNC model of X over S, that is an SNC projective
scheme X over S with generic fiber X such that the special fiber, which is not assumed
to be reduced, agrees as a closed subset with a simple normal crossing divisor D of X . To


## Literal published source 1712.00980: source-extracts/1712.00980-appendix-obstruction.txt

the model X we can associate a skeleton ∆X ⊂ X an and a retraction pX : X an → ∆X ,
see [BFJ16a, §3] for details.
   Let L be an ample line bundle on X and L a nef model of L on X . Let θ be the
semipositive (1, 1)-form in the class of L corresponding to the model L . Let µ be a
positive Radon measure on X an with support in ∆X such that µ(X an ) = degL (X). The
Monge-Ampère equation looks for a θ-psh function ϕ on X an such that
(A.1)                                (ddc ϕ + θ)∧n = µ.
With the generality we are discussing in this paragraph, there is not yet a definition of
the class of θ-psh functions with all the properties of classical pluripotential theory, but
every good definition of this class should include the class of θ-psh model functions as
introduced in 2.5.
   The following question is natural and in case of being true would be of great help to
solve the Monge-Ampère equation in positive and mixed characteristic.
Question 1. With the previous hypotheses, is it true that any solution ϕ to the Monge-
Ampère equation (A.1) satisfies
(A.2)                                      ϕ = ϕ ◦ pX ?
   We will see that this question has a negative answer by exhibiting a counterexample in
the context of toric varieties. In fact, that this question has a negative answer is related
with Proposition 3.8 not being true in higher dimension. To this aim, we will consider a
smooth projective variety X of dimension 2 and two models X and X 0 that have the
same skeleton
                                      ∆ = ∆X = ∆X 0
but with different retractions pX 6= pX 0 . We will fix a semipositive (1, 1)-form θ that is
realized in both models and construct two model functions ϕ and ϕ0 on X an satisfying
(A.3)                          ϕ 6= ϕ0 ,       ϕ |∆ = ϕ0 |∆ ,
(A.4)                          ϕ = ϕ ◦ pX , ϕ0 = ϕ0 ◦ pX 0 .
                    CONTINUITY OF PLURISUBHARMONIC ENVELOPES                             25


As a consequence of these properties, we deduce that ϕ = ϕ0 ◦ pX and that ϕ0 = ϕ ◦ pX 0 .
Moreover ϕ0 will be a θ-psh model function while the model function ϕ will not be θ-psh.
Let µ := (ddc ϕ0 + θ)∧2 . This is a positive measure with support on ∆ and ϕ0 is a solution
of the corresponding Monge-Ampère equation. Since
                                    ϕ0 6= ϕ = ϕ0 ◦ pX ,
we see that ϕ0 is a counterexample to Question 1 for the model X . Moreover, if Propo-
sition 3.8 were true in dimension 2, then ϕ = ϕ0 ◦ pX would be a θ-psh model function,
but it is not.
   We place ourselves in the framework and notation of [BPS14]. The results below will
make explicit the skeleton and the retraction associated to a toric SNC model of a toric
variety.
   Let T ≃ Gnm be a split torus over K. We denote by
                        M = Hom(T, Gm ),         N = Hom(Gm , T),
the lattices of characters and one-parameter subgroups of T. Then M = N ∨ . We also
denote NR = N ⊗ R and MR = M ⊗ R. The pairing between u ∈ NR and x ∈ MR is
denoted by hx, ui.
  Let now X be a proper toric variety over K and X a proper toric model of X over
S. Then X is described by a complete fan Σ in NR and X is described by a complete
SCR-polyhedral complex Π in NR whose recession fan satisfies rec(Π) = Σ [BPS14,
Thm. 3.5.4].
  There is a map ζK : NR → Tan that sends u ∈ NR to the seminorm on K[M ] given by
                            X
                                 αm χm = max |αm |e−λK hm,ui .
                                             m
