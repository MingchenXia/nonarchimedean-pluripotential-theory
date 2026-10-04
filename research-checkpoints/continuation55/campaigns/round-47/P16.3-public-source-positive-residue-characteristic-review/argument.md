# Exact scoped status

{
  "id": "P16.3",
  "status": "partial",
  "exact_result": "Published-source application: over algebraically closed trivially valued k of characteristic p>0, smooth connected projective X and ample L, the genuine finite-energy operator exists in every dimension and is injective modulo constants; every positive Radon measure of raw mass (L^n) and finite raw dual energy has a unique finite-energy solution for dim X<=2. Arbitrary-field continuous/test MA, synthetic orthogonality and measure approximation are established background, not the full nontrivial positive-residue-characteristic extension.",
  "proof_file": "P16.3-argument.md",
  "concrete_gaps": [
    "For nontrivially discretely valued K of residue characteristic p>0 in arbitrary dimension, replace SNC-dependent singular psh approximation and prove normalized compactness.",
    "Prove the necessary model positivity and envelope/variational regularity without an unproved resolution assumption or extra function-field descent, treating mixed characteristic separately.",
    "Construct approximation-independent genuine mixed MA on unbounded E1, including full raw mass and finite-energy integrability.",
    "Prove equality of test and E1 dual energy and differentiation of obstacle energy on the resulting finite-energy space.",
    "Realize every correctly massed finite-dual-energy Radon measure of arbitrary support by an actual psh potential, not merely a limit in a completed measure space.",
    "Establish unbounded locality/comparison and injectivity modulo constants on that operator domain."
  ]
}


# Entire final proof

---
title: "P16.3: positive residue characteristic, source audit and a partial theorem"
author: "Research draft"
date: "4 October 2026"
geometry: margin=1in
fontsize: 11pt
---

**Status: partial; the original nontrivially valued positive-residue-characteristic atom is not solved.** This document proves a precisely delimited application of published results and two elementary normalization/variational passages. It does not claim a new extension of the non-Archimedean finite-energy equation theorem. In particular, the higher-dimensional nontrivially valued case remains an obligation even for smooth projective varieties. All source references below refer to the ten supplied, hash-verified PDFs, not to later versions inferred from an abstract.

# 1. The target and the valuation distinction

The residual P16.3 target retains a complete **nontrivially discretely valued** non-Archimedean field $K$, a smooth projective variety $X/K$, dimension $n\geq 1$, and an ample line bundle $L$. Write $V=(L^n)>0$. The restriction to remove is $\operatorname{char}(\widetilde K)=0$, where $\widetilde K$ is the residue field. Thus both equal characteristic $(p,p)$ and mixed characteristic $(0,p)$ must be addressed. Field characteristic zero alone does not meet the original residue-characteristic hypothesis. For uniqueness by one constant one works on a connected variety; disconnected components instead permit independent constants. The unresolved case already contains geometrically integral smooth projective varieties, so introducing that restriction would not close the gap.

The required equation is

$$\operatorname{MA}^{\rm raw}_{\rho}(u)=\mu,\qquad \mu\geq 0,\quad \mu(X^{\rm an})=V,$$

for an actual psh potential $u$ of finite energy relative to a specified continuous semipositive reference metric $\rho$ on $L$. The positivity datum remains the ample $L$, and its raw mass remains $V$. Measures must satisfy the dual-energy condition specified below. No support restriction to a skeleton, toric invariance, or replacement inverse measure is authorized. There must be an approximation-independent extension of the genuine model Monge--Ampere measure, followed by existence and uniqueness modulo constants on the stated finite-energy space.

If $k$ has the trivial absolute value, then $k^\circ=k$, $k^{\circ\circ}=0$, and $\widetilde k=k$. Thus a trivially valued field of characteristic $p$ has residue characteristic $p$, but it is not a nontrivially valued field. Neither $\overline{\mathbb F_p}$ with trivial valuation nor its test configurations give a proof for $\mathbb F_p((t))$, much less $\mathbb Q_p$. Test configurations are auxiliary models over $k[t]$, not an identification of an arbitrary nontrivially valued variety with a trivially valued one.

The following are the conclusions warranted by this investigation:

| Domain | Established conclusion used here | Limitation |
|---|---|---|
| Algebraically closed trivially valued $k$, characteristic $p>0$, smooth connected projective $X$, ample $L$, every dimension | Genuine $\mathcal E^1$ operator, strong continuity, comparison, and injectivity modulo constants | Surjectivity in arbitrary dimension is not supplied unconditionally |
| The preceding domain with $1\leq n\leq2$ | Every positive Radon measure of mass $V$ and finite dual energy has a unique finite-energy solution modulo constants | A trivial-valuation endpoint, including surfaces, not P16.3's nontrivial axis |
| Smooth projective $X$ over any complete non-Archimedean $K$, including positive residue characteristic | Genuine MA for continuous semipositive metrics; test-function dual energy, orthogonality in the synthetic sense, and strong density of test MA measures | Density/completeness on the measure side is not existence of an unbounded potential |
| Discrete equal characteristic $p$, function-field descent of $(X,L)$, and assumed resolution in dimension $n+d$ | A positive-characteristic envelope result is reported in BE, Section 7.30 | Additional descent and resolution hypotheses; no independent proof of the full finite-energy equation here |
| Nontrivial discrete valuation, residue characteristic $p$, arbitrary-dimensional smooth projective $X$ and ample $L$, with no such extra assumptions | Full P16.3 theorem not established in this draft | Concrete replacement obligations in Section 7 |

These limitations describe what is established here and in the checked source statements. They are not a proof that no future or uncached theorem exists, and they are not a counterexample to P16.3.

# 2. Exact versions and the original proof dependencies

**BFJ-PSH** denotes Boucksom--Favre--Jonsson, *Singular semipositive metrics in non-Archimedean geometry*, arXiv:1201.0187v2. Its PDF banner is 21 January 2014; the internal manuscript date says 22 October 2018. Both are retained in provenance. It assumes complete discrete valuation, residue characteristic zero, smooth projective $X$ and ample $L$. In the introduction and Sections 3, 5--8 it uses the following inputs.

1. Cofinal regular SNC models: every model is dominated by a regular model with special fiber of SNC support. The inverse-limit skeleton description and the retractions enter its original definition of psh and approximation by retractions. Generic-fiber smoothness does not imply regularity or SNC support for the total model.
2. Numerical/model positivity: Theorem 5.11 includes multiplier ideals in its positivity argument. Resolving the model does not replace this use of ideals.
3. Compactness: Theorem 6.1 supplies equicontinuity on dual complexes, using toroidal modifications and intersection estimates. Section 7 passes to compactness modulo constants. This compactness is compactness of the psh cone, not merely compactness of the underlying analytic space.
4. Envelopes and regularization: Theorems 8.3, 8.5 and 8.7 use graded base ideals, asymptotic multiplier ideals, subadditivity and uniform global generation. Appendix B proves Kodaira/Kawamata--Viehweg/Nadel vanishing and ideal properties on the regular/SNC models in the standing characteristic-zero regime. Deleting that regime does not validate these arguments.

**BFJ-MA-v1** is the actual saved arXiv:1201.0188v1, banner 30 December 2011. Theorem A additionally requires that $X$ be *algebraizable*: $X=Y_K$ for a smooth projective variety $Y$ over a one-variable function field $F$ admitting $K$ as a completion. This differs from saying that $X$ is an algebraic $K$-variety. The theorem does **not** require that $L$ descend to $F$. It requires $\mu$ to be supported on the dual complex of an SNC model, and requires mass $(L^n)$. Its conclusion is a continuous semipositive solution, unique up to multiplication of the metric by a positive constant.

The v1 proof then depends on BFJ-PSH compactness and regularization to construct bounded MA, locality, truncation measures and the $\mathcal E^1$ operator. Sections 3--6 are the operator/locality/energy part; Section 7 differentiates energy composed with the envelope, and Section 8 obtains solutions. Appendix A, Theorem A.4, uses the function-field algebraizability hypothesis to compactify a model into a projective variety over the residue field and apply the orthogonality of big-line-bundle decompositions. The introduction explicitly identifies this role. SNC support is also used for its continuity estimates; it cannot be read as an unrestricted finite-energy measure theorem just because the proof introduces $\mathcal E^1$.

**BE** is Boucksom--Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*, arXiv:1805.01016v3, banner 8 January 2021. It is not a differently titled pluripotential paper. For geometrically reduced projective $X$ over any complete valued field and semiample $\mathbb Q$-line bundle $L$, Theorem 9.15 identifies relative volume with relative MA energy for two continuous psh metrics. Smooth $X$ satisfies geometric reducedness, and ample $L$ is semiample. Section 7.30 still labels unrestricted envelope continuity a conjecture. Its reported characteristic-$p$ discrete case assumes descent of **$(X,L)$** to a function field of transcendence degree $d$ and resolution in dimension $n+d$, replacing multiplier ideals with test ideals. The same restrictions recur in Section 10.9's differentiability discussion. The cited GJKM paper is not among the ten allowed inputs; its exact stronger resolution formulation is consequently not asserted or newly proved here. The reported statement cannot cover mixed characteristic, nor all non-descending pairs.

**BJ-triv** is Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, arXiv:1801.08229v4, banner 22 March 2022. Its main-body ground field is algebraically closed, of arbitrary characteristic, with trivial valuation. Theorems 7.18, 8.5, 10.4, 12.8 and 12.9 have distinct roles described below.

**BJ-synth** is Boucksom--Jonsson, *Measures of finite energy in pluripotential theory: a synthetic approach*, arXiv:2307.01697v1, 6 July 2023. The introduction explicitly says it does not investigate potentials of finite energy. Its theorem about completion of measures is therefore not a theorem identifying that completion with $\mathcal E^1/\mathbb R$.

**PS-hybrid**, arXiv:2209.04879v2, contains the useful distinction in Remark 4.4: defining $\mathcal E^1$ over any non-Archimedean field does not generally give its MA extension. Its Section 1.2 expressly assumes *equicharacteristic zero*. The shorter words “characteristic zero” in Remark 4.4 cannot enlarge this standing setting to mixed characteristic.

# 3. Partial theorem over a trivially valued field

**Theorem (published endpoint in raw normalization).** Let $k$ be algebraically closed of characteristic $p>0$, equipped with the trivial absolute value. Let $X/k$ be smooth, connected and projective, of dimension $n\geq1$, and let $L$ be ample. Fix the canonical trivial reference metric $\rho$, and put $\omega=c_1(L)$, $V=(L^n)$. There is a genuine, approximation-independent operator

$$\operatorname{MA}^{\rm raw}_{\rho}:\mathcal E^1(L)\longrightarrow\{\text{positive Radon measures of mass }V\}.$$

It extends the intersection-theoretic model MA measure, is continuous along decreasing nets, and its normalized version is continuous for the strong topologies. Its image consists of finite-dual-energy measures; it is injective modulo constants, with dense image in that measure space. If $1\leq n\leq2$, its image is the entire finite-dual-energy measure space. Equivalently, for every positive Radon $\mu$ with mass $V$ and $\mathcal E_{\rho}^{*,\rm raw}(\mu)<\infty$, there is a solution $u\in\mathcal E^1(L)$, unique modulo addition of a real constant. There is no restriction on measure support. No assertion that $u$ is continuous is made. For $n\geq3$, the same surjectivity follows **if** $L$ has the envelope property, but that extra hypothesis is not proved here.

This is a source theorem application, not a newly proved removal of the nontrivial residue-characteristic restriction.

## 3.1 Positivity, reference, functions and exact measure energy

The canonical trivial metric is the reference used in BJ-triv's Fubini--Study functions. Define $\mathcal H(L)$ using

$$u=\frac1m\max_i(\log|s_i|+\lambda_i),\qquad s_i\in H^0(X,mL),\quad \lambda_i\in\mathbb Q,$$

where the sections have no common zero. These are continuous semipositive metrics relative to $\rho$ and correspond to ample integrally closed test configurations. Define $\operatorname{PSH}(L)$ as the usc functions, not identically $-\infty$, obtained as decreasing nets from $\mathcal H(L)$. They are stable under constants and maxima and are determined by their finite values on divisorial valuations. The weak topology is pointwise convergence on these valuations. The trivial valuation $v_{\rm triv}$ satisfies $\sup u=u(v_{\rm triv})$. The canonical reference has normalized MA equal to $\delta_{v_{\rm triv}}$.

For continuous semipositive $u$ put

$$\mathcal E_{\rho}^{\rm raw}(u)=\frac1{n+1}\sum_{j=0}^n\int_{X^{\rm an}}u\, (\omega+dd^c u)^j\wedge\omega^{n-j},\qquad E(u)=V^{-1}\mathcal E_{\rho}^{\rm raw}(u).$$

Here the mixed products are the genuine intersection-theoretic measures, and the formula agrees with the compactified-test-configuration energy. Extend energy monotonically by

$$E(u)=\inf\{E(v):v\in\mathcal H(L),\ v\geq u\},\qquad \mathcal E^1(L)=\{u\in\operatorname{PSH}(L):E(u)>-\infty\}.$$

BJ-triv Proposition 7.7 supplies concavity, upper semicontinuity, decreasing-net continuity and $E(u+c)=E(u)+c$. The strong topology is the refinement of the weak topology making $E$ continuous. On the measure side it is weak convergence together with convergence of dual energy.

The exact raw condition is

$$\mathcal E_{\rho}^{*,\rm raw}(\mu)=\sup_{u\in\mathcal H(L)}\left\{\mathcal E_{\rho}^{\rm raw}(u)-\int u\,d\mu\right\}<\infty,\qquad \mu(X^{\rm an})=V.$$

Writing $\nu=\mu/V$ is simply bookkeeping for a measure already of the correct mass; it is not normalization of an arbitrary restriction of $\mu$. Exactly

$$\mathcal E_{\rho}^{*,\rm raw}(\mu)=V E^\vee(\nu),\qquad E^\vee(\nu)=\sup_{u\in\mathcal E^1}\left(E(u)-\int u\,d\nu\right)=\sup_{u\in\mathcal H}\left(E(u)-\int u\,d\nu\right).$$

**Proof of the raw passage and integrability.** The displayed equality follows by factoring $V$ from each test expression. If the test supremum is finite and $u_j\in\mathcal H$ decreases to $u\in\mathcal E^1$, then $E(u_j)\to E(u)>-\infty$ and

$$\int u_j\,d\nu\geq E(u_j)-E^\vee(\nu).$$

The usc decreasing-net integration theorem for a positive Radon measure on the compact $X^{\rm an}$ (BJ-triv Lemma 7.17) gives $\int u_j\,d\nu\to\int u\,d\nu$. A uniform upper bound for $u_j$ and the displayed lower bound show that $u\in L^1(\nu)$. Each finite-energy test expression is therefore the limit of its model expressions and is bounded by the test supremum. The reverse supremum inequality follows from $\mathcal H\subset\mathcal E^1$. This proves the equality, with no assumed solution to the equation. If an arbitrary positive measure has mass $M\ne V$, the constant tests give $c(V-M)$, whose supremum over $c\in\mathbb R$ is infinite. Thus finite raw dual energy itself forces exactly the required mass. In the trivial setting BJ-triv Theorem 9.20 also gives the equivalent condition $\mathcal E^1\subset L^1(\nu)$.

Changing the reference to a continuous semipositive metric $\rho+r$ changes the raw dual functional by the finite quantity $\int r\,d\mu-\mathcal E_{\rho}^{\rm raw}(r)$. Indeed, the relative-energy cocycle yields $\mathcal E_{\rho+r}^{\rm raw}(u-r)=\mathcal E_{\rho}^{\rm raw}(u)-\mathcal E_{\rho}^{\rm raw}(r)$, and substitution in the supremum proves the assertion. This passage uses the published relative-energy identity on the already established endpoint; it asserts no unbounded descent over another field.

## 3.2 Construction of the genuine operator and independence

Use the multilinear finite-energy pairing of BJ-triv Theorem 7.14. Its existence, finiteness and monotone continuity are published inputs, proved there by a monotone extension of the PL intersection pairing and mixed-energy estimates. For $u\in\mathcal E^1$ define on real PL test functions $f$

$$T_u(f)=(0,f)\cdot(\omega,u)^n.$$

Lemma 7.15 and Theorem 7.18 make $T_u$ a positive linear functional. Constants satisfy $T_u(1)=V$ by the constant-shift identity of the pairing. Thus $|T_u(f)|\leq V\|f\|_\infty$. Real PL functions are uniformly dense in $C^0(X^{\rm an})$ by Theorem 2.2. Consequently $T_u$ extends uniquely to a positive bounded functional on $C^0$. Riesz representation gives its unique positive Radon measure, which we define as $\operatorname{MA}_{\rho}^{\rm raw}(u)$.

If $u_j$ decreases to $u$ through model functions, monotone continuity of the pairing gives $T_{u_j}(f)\to T_u(f)$ for each PL $f$. The common bound $V\|f\|_\infty$ extends convergence to every continuous $f$. Therefore the weak limit is independent of the chosen net. On a model/test configuration with components $F$ in its special fiber, a model metric $u$ has

$$\operatorname{MA}_{\rho}^{\rm raw}(u)=\sum_F b_F\bigl((\omega_{\mathcal X}+D)|_F\bigr)^n\delta_{v_F},\qquad b_F=\operatorname{ord}_F(\mathcal X_0),$$

as in Proposition 7.19(ii); hence this operator extends the genuine model MA. Proposition 7.19(i) gives raw total mass $V$. Theorem A gives strong continuity. Neither a norm-derived inverse measure nor an arbitrary assignment of an atomic distribution has been substituted. No resolution is needed in the construction in BJ-triv Section 7; integrally closed test configurations and the pairing replace the original SNC-dependent construction in this trivial setting.

## 3.3 Envelopes and compactness: the actual characteristic replacement

For a continuous obstacle $h$ put $P(h)=\sup\{u\in\operatorname{PSH}(L):u\leq h\}$. The envelope property means that usc regularization of the supremum of every bounded-above psh family remains psh. BJ-triv Lemma 5.17 identifies it with continuity of $P(h)$ for continuous $h$; Theorem 5.11 identifies it with weak compactness of the normalized psh space.

For $n\leq2$, Theorem 5.20 proves this property in positive characteristic. Its proof first reduces to a PL obstacle represented by $(\mathcal X,\mathcal L)$ and writes

$$P(\varphi_{\mathcal L})-\varphi_{\mathcal L}=\lim_m m^{-1}\varphi_{\mathfrak a_m},$$

where $\mathfrak a_m$ is the base ideal of $m\mathcal L$ (Lemma 5.22). Normalized blowups of these ideals give the nef approximants. The proof resolves the test configuration to a smooth total space with SNC central support. The relevant dimension is **$\dim\mathcal X=n+1\leq3$**, not just the dimension of $X$. The supplied PDF page 62 visually distinguishes the roman $X$ from the calligraphic $\mathcal X$, which the cached OCR flattens.

In characteristic zero the proof uses asymptotic multiplier ideals; in positive characteristic it uses test ideals and their subadditivity/global generation, as expressly stated on PDF page 63. The resulting estimate has the form

$$\varphi_m\leq P(\varphi_{\mathcal L})\leq\left(1+\frac{m_0}{m}\right)\varphi_{m+m_0}-\frac{m_0}{m}\varphi_{\mathcal L}+\frac C m.$$

It forces uniform convergence and hence envelope continuity. This paragraph reconstructs the source's replacement mechanism; the algebraic resolution and test-ideal results used in its published Theorem 5.20 are background inputs, not reproved results of this draft. Crucially, their available low-dimensional use is why the unconditional positive-characteristic theorem stated here has $n\leq2$. Assuming resolutions in every necessary dimension would add a hypothesis. No unrestricted higher-dimensional resolution theorem is claimed.

Once the envelope property is known, normalized psh compactness can be seen directly. For a normalized net, divisorial values are uniformly bounded by the source's evaluation estimates. Tychonoff gives a subnet converging at every divisorial point. The usc tail suprema are psh by the envelope property and decrease to the usc potential having those limits; nontriviality follows from finite divisorial values. The divisorial determination theorem identifies that limit uniquely. This is the proof mechanism of Theorem 5.11 and avoids invoking cofinal SNC skeletons as the compactness argument.

## 3.4 Energy differentiation, comparison and uniqueness

BJ-triv Theorem 8.5 and Corollary 8.6 prove, for $u\in\mathcal E^1$, PL $f$ and arbitrary continuous $g$,

$$E^\downarrow(u+tf)=E(u)+t\int f\,\operatorname{MA}(u)+O(t^2),\qquad \left.\frac d{dt}\right|_{t=0}E^\downarrow(u+tg)=\int g\,\operatorname{MA}(u).$$

Here $\operatorname{MA}=V^{-1}\operatorname{MA}^{\rm raw}$ and $E^\downarrow$ is the decreasing extension of obstacle energy. When the envelope property holds, $E^\downarrow(u+tg)=E(P(u+tg))$. The proof uses relative volumes and a uniform differentiability estimate, followed by monotone approximation; it is not an assertion that an arbitrary perturbation is psh. Multiplying by $V$ gives the raw derivative $\int g\,\operatorname{MA}^{\rm raw}(u)$. The source's proof cites BE and the relative-volume differentiability work; these are published background, with BE's geometric reducedness satisfied here. The differentiated statement used is the fully stated and proved result in BJ-triv, rather than a new uncached differentiability assertion.

Theorem 7.40 supplies locality on $\{u>v\}$ for finite-energy functions. The model proof compares vertical Cartier divisors near a central component; the general proof passes weighted measures to the limit using finite-energy pairing continuity. It is not just locality for continuous weights. Proposition 7.19(v) implies that the infinite loci of the finite-energy potentials have zero mass for all the MA measures appearing here, so the following partitions and differences are interpreted off a common null set. To derive comparison, put $w_\epsilon=\max(u,v-\epsilon)$. Positivity, locality and raw mass give

$$V\geq\int_{\{u<v-\epsilon\}}\operatorname{MA}^{\rm raw}(v)+\int_{\{u>v-\epsilon\}}\operatorname{MA}^{\rm raw}(u),$$

and therefore

$$\int_{\{u<v-\epsilon\}}\operatorname{MA}^{\rm raw}(v)\leq\int_{\{u\leq v-\epsilon\}}\operatorname{MA}^{\rm raw}(u).$$

Letting $\epsilon\downarrow0$ gives Theorem 7.44 in raw form,

$$\int_{\{u<v\}}\operatorname{MA}^{\rm raw}(v)\leq\int_{\{u<v\}}\operatorname{MA}^{\rm raw}(u).$$

For uniqueness, equality of MA measures gives $I(u,v)=\int(u-v)(\operatorname{MA}(v)-\operatorname{MA}(u))=0$. The finite-energy integrability needed here is part of Proposition 7.19(v). Corollary 10.4 says that $I=0$ is equivalent to $u-v$ being locally constant. In its proof the energy estimates applied to $\delta_{v}$ and $\delta_{v_{\rm triv}}$ show equality at every divisorial valuation after matching the suprema; the divisorial determination theorem then gives equality everywhere. Smooth connected $X$ is irreducible here, so the difference is a single constant. Multiplication of the metric by $e^{-c}$ corresponds to adding $c$ to $u$. Comparison alone is not being substituted for this injectivity argument.

## 3.5 Actual existence, with the compactness step included

Let $\nu=\mu/V$ have $E^\vee(\nu)<\infty$. Choose a maximizing sequence $u_j\in\mathcal H(L)$ for $F_\nu(u)=E(u)-\int u\,d\nu$ and normalize $\sup u_j=0$. The normalized functions need not remain rational Fubini--Study functions, but lie in the continuous psh cone and in $\mathcal E^1$. This normalization leaves $F_\nu$ unchanged because $\nu$ has mass one. Lemma 9.15 and Corollary 9.16 bound $J(u_j)\leq C(E^\vee(\nu)+o(1))$, where $J(u)=\sup u-E(u)$ in the trivial setting. For $n\leq2$ the established envelope property gives a weakly convergent subnet with limit $u\in\operatorname{PSH}$.

Upper semicontinuity of $E$ and the $J$ bound imply $u\in\mathcal E^1$. Proposition 9.19 gives $u_j\to u$ in $L^1(\nu)$ along this subnet. Consequently

$$F_\nu(u)\geq\limsup_j F_\nu(u_j)=E^\vee(\nu).$$

The reverse inequality is the definition of the dual supremum. Thus $u$ is an actual maximizing psh potential, rather than a formal element of a completion of measures.

For completeness, the equation follows from the published uniform derivative by an explicit argument. For PL $f$ let $\delta_j=E^\vee(\nu)-F_\nu(u_j)\to0$. The obstacle-duality bound and Theorem 8.5 give, for $t>0$,

$$t\int f\,\operatorname{MA}(u_j)\leq t\int f\,d\nu+\delta_j+C_f t^2.$$

First let $j$ tend to the limit, then let $t\downarrow0$, and repeat with $-f$. This proves the weak convergence of $\operatorname{MA}(u_j)$ to $\nu$ (Theorem 9.11). In particular the constant maximizing sequence $u_j=u$ proves $\operatorname{MA}(u)=\nu$ (Corollary 9.12). PL density determines the measure on the full analytic space, without a support assumption. Multiplying by $V$ proves the raw equation. The preceding injectivity argument completes uniqueness. This is also the proof of the applicable direction of Theorem 12.8; Theorem 12.9 gives exactly this endpoint.

# 4. What survives over a genuinely nontrivial field

Let now $K$ be complete, nontrivially discretely valued with residue characteristic $p>0$, $X/K$ smooth projective, and $L$ ample. Choose a continuous semipositive reference metric $\rho$ arising from a positive projective model of $L$ (a rational model of a positive tensor power suffices). Write $\theta=c_1(L,\rho)$ and $V=(L^n)$. No regular model is asserted. For nef model metrics the genuine raw measure is

$$\sum_F b_F\deg_F(\mathcal L^{\,n})\,\delta_{v_F},$$

with the usual rational-power scaling when $\mathcal L$ models a tensor power. Positivity follows from nefness on each component, and flat specialization gives the total $V$. BE Propositions 8.3 and 8.5 and Theorems 8.4 and 8.18 supply the continuous measure and model/Deligne-pairing calculus. Since ample $L$ is semiample, its continuous psh metrics are psh-regularizable by BE Theorem 7.14, as required by Theorem 8.4. The extension uses uniform limits over an arbitrary complete valued field. This is not the requested unbounded operator.

For test potentials define

$$E_\theta(u)=\frac1{(n+1)V}\sum_{j=0}^n\int u\,(\theta+dd^cu)^j\wedge\theta^{n-j},\qquad J_\theta(\nu)=\sup_{u\in D_\theta}\left(E_\theta(u)-\int u\,d\nu\right).$$

Here $D$ is the real vector space of PL/model functions containing constants, and $D_\theta$ consists of those with $\theta+dd^cu\geq0$. Thus this precise, already defined test-side raw energy condition is $\mu(X^{\rm an})=V$ and $VJ_\theta(\mu/V)<\infty$. Equality with a supremum over an eventual unbounded $\mathcal E^1$ cone would require a valid monotone-energy extension and integrability passage, not just a notation change. Section 3.1 explains that passage where it is proved.

BJ-synth Sections 1.2.2 and 1.3.2 verify the synthetic data for this projective Berkovich setting: intersection wedge measures, integration by parts, and seminegativity by the local Hodge index theorem. In general one must keep the Bott--Chern model quotient $H_{\rm BC}$; an isomorphism $H_{\rm BC}=N^1(X)$ is stated there only under additional hypotheses. Its positive cone is the preimage of the ample cone. This suffices for the present ample reference and avoids assuming that isomorphism in positive residue characteristic.

Example 2.20 derives orthogonality from BE's relative-volume theorem and the published BGM uniform differentiability estimate. Its Definition 2.15 is

$$\lim_{u\in D_\theta,\ u<f}\int(f-u)\,\operatorname{MA}_\theta(u)=0$$

for PL $f$, with the directed order specified in the source. It does not first assert that a pointwise envelope is a continuous psh metric. Theorem 2.23 then proves that any maximizing test sequence for $J_\theta(\nu)$ has $\operatorname{MA}_\theta(u_j)\to\nu$ **strongly**, and Theorem A constructs a complete quasi-metric on the measure space. These conclusions have no restriction on $\operatorname{char}(K)$ or $\operatorname{char}(\widetilde K)$ and require no imposed resolution hypothesis in the source's projective example. The derivative estimate yields weak convergence by the same defect argument in Section 3.5, but without constructing a limiting psh potential. The strong convergence of dual energies is the further source theorem, not a consequence asserted merely from weak convergence.

Thus orthogonality at the test-energy level no longer forces retaining BFJ-MA-v1's function-field algebraizability assumption. This does **not** establish regularity of envelopes, compactness of the singular psh cone, the unbounded operator, or realization of every measure by a potential. Completing a space of measures is a different operation from showing completeness of a particular space of usc psh functions modulo constants. BJ-triv Theorem 12.8 proves their relationship in its own trivial setting; it cannot be imported to another field without its analytic inputs.

A simple genuine higher-dimensional nontrivial example helps locate the distinction. Suppose a smooth projective $K^\circ$-model $\mathcal X$ exists with irreducible special fiber and a relatively ample extension $\mathcal L$ of $L$. The special fiber has multiplicity one. For its reference metric, the model formula gives $\operatorname{MA}^{\rm raw}_\rho(0)=V\delta_\xi$, where $\xi$ is the point attached to that component. Test energy is concave with derivative $\operatorname{MA}_\rho(0)=\delta_\xi$, so $E_\theta(u)\leq\int u\,d\delta_\xi$. The zero test gives equality in the dual supremum; hence $J_\theta(\delta_\xi)=0$. This solves that reference target in any dimension with actual MA and exact mass. It is only a particular test/continuous solution, not an existence theorem for arbitrary finite-energy $\mu$, nor an extension to unbounded weights. No base change or alteration is used in this example.

# 5. Why the recent local theories do not close this argument

Gubler--Rabinoff, arXiv:2506.13548v2, banner 17 September 2025, introduces classically psh functions through curves and base change. Its introduction expressly states that defining MA may require additional hypotheses and is not the subject of the paper. Its identification of classically psh R-PL functions with semipositivity is useful local positivity information, but is not an approximation-independent global $\mathcal E^1$ equation theorem.

Chambert-Loir--Ducros, arXiv:1204.6277v2, banner 25 July 2025 and interior date 29 July 2025, states in Section 0.2.15 that its forms/currents theory works in every characteristic without resolution or alterations. It develops local Bedford--Taylor and metric-curvature products. Those characteristic-independent statements replace inputs for that local theory. They do not by themselves identify every singular metric in the target global psh cone with its regularizable local class, prove global normalized compactness, or supply the required variational existence and injectivity. No such identification is proved in this draft.

Thuillier's thesis is potential theory on analytic curves; Berkovich's 1993 paper is *Etale cohomology for non-Archimedean analytic spaces*. Their analytic and curve-theoretic results are compatible with positive residue characteristic. Neither is used as a replacement for higher-dimensional envelope regularity or as an equation theorem in higher dimension. Their PDFs were checked as sources, not invoked to collapse the assignment to $\mathbb P^1$.

# 6. Proof boundaries and failed inference chains

The following passages would be invalid in the present proof and were not made:

* Smooth generic fiber $\Rightarrow$ cofinal regular SNC models in arbitrary positive residue characteristic. The relevant total spaces are one dimension larger; equal and mixed characteristic require distinct geometric inputs.
* Resolution alone $\Rightarrow$ the multiplier-ideal subadditivity and vanishing used by BFJ. Positive-characteristic test ideals require the hypotheses under which their generation estimates hold; the reported BE characteristic-$p$ theorem imposes function-field descent and resolution. Mixed characteristic is not covered by that report.
* Alterations or a universal homeomorphism $\Rightarrow$ a descended finite-energy operator. Even a topological statement does not prove preservation of the ample class, psh cone, masses, energy, derivative, unbounded products or comparison.
* Strong convergence of genuine model MA measures $\Rightarrow$ a psh solution of their limit equation. A realization/completeness theorem for actual potentials is missing.
* Local current products $\Rightarrow$ global variational existence for every finite-dual-energy measure. Compactness, envelope compatibility and unbounded injectivity remain separate.

These are logical gaps in attempted extensions, not mathematical counterexamples to the target. No nonexistence assertion is proved.

# 7. Concrete remaining original obligations

For complete nontrivially discretely valued $K$ with $\operatorname{char}(\widetilde K)=p>0$, smooth connected projective $X/K$ in arbitrary dimension, ample $L$, and all positive Radon $\mu$ of mass $V$ and finite dual energy, the following work is still required:

1. **Singular psh theory and compactness.** Supply a definition equivalent to the intended model-semipositive theory, monotone approximation, divisorial determination where used, and compactness modulo constants. Replace the SNC-cofinality, retraction and toroidal equicontinuity arguments, or prove an alternative with all hypotheses. The original residue-characteristic-zero theorems cannot be cited on the changed field.
2. **Model positivity and envelopes.** Prove the required positivity/nef approximation and continuity or an adequate variational substitute for envelopes without an unproved resolution hypothesis or extra function-field descent. Record any restriction if such an input is only conditional. Cover mixed characteristic separately from equal characteristic $p$.
3. **Unbounded operator.** Construct the genuine positive mixed MA products on $\mathcal E^1$; prove finiteness/integrability, raw full mass $V$, independence of decreasing approximants or truncations, and compatibility with model and continuous MA. Test-side measure completion does not meet this item.
4. **Exact energy and derivative on that space.** Establish the monotone energy extension, equality of the test and $\mathcal E^1$ dual suprema, and the energy/obstacle derivative at finite-energy potentials. The modern test orthogonality result is an available input, not by itself this passage.
5. **Existence of an actual potential.** Show that a normalized maximizing family has a limit in the stated psh cone of finite energy, that the measure integral passes to the limit, and that the derivative characterizes its genuine MA as the full $\mu$. Do this for arbitrary support without restricting and renormalizing the measure.
6. **Comparison and uniqueness.** Prove locality/comparison for unbounded finite-energy weights and injectivity modulo constants using a valid energy or domination argument. Continuous-metric uniqueness does not establish finite-energy uniqueness.

No new indispensable passage meeting all six items over the target fields has been proved here. The unconditional theorem in Section 3 is narrower and remains partial. Even the unresolved higher-dimensional trivially valued envelope property is a separate limitation, not a replacement for these nontrivial-field obligations.

# 8. Reproduction and evidence

The original JSON is preserved byte for byte in `input-original.json`; the decoded assignment and task are in `assignment-original.txt` and `task-original.json`. `source_audit.py` reads only the supplied input and the ten listed public caches, checks all 20 PDF/text hashes and six abstract hashes, copies the sources to `source-extracts`, regenerates PDF text with the installed `pdftotext`, and saves 52 literal extracts with the published wording and precise line/page locations in `source-extracts/source-provenance.json`. The original cache hashes, version banners, application checks, and extract texts are present in that JSON. OCR typos are retained rather than silently corrected in literal extracts.

The PDF page images `source-extracts/BJ22-page-62.png`, `BJ22-page-97.png` and `BJ22-page-122.png` were inspected for the model-dimension ambiguity, the energy derivative, and the existence theorem. Their visual checks and hashes are recorded in provenance. In particular, page 62 says $\dim X\leq2$ and $\dim\mathcal X\leq3$; page 122 states the unconditional positive-characteristic dimension bound.

Rerun `python3 source_audit.py` and `python3 build_and_check.py` in this workspace. The latter generates a standalone `P16.3-paper.tex` from this argument using the existing Pandoc, runs the existing `pdflatex` twice sequentially, saves each actual stdout/stderr diagnostic stream and TeX log, and checks the input preservation and exact status schema. `status.json` has exactly `id,status,exact_result,proof_file,concrete_gaps`. Source hashes and compilation verify source identity and artifact execution only; they do not verify the mathematical arguments. No heavy computation, installation, network fetch, model call, worker, or external message is used.

# References (exact supplied artifacts)

1. BFJ-PSH: arXiv:1201.0187v2, *Singular semipositive metrics in non-Archimedean geometry*.
2. BFJ-MA-v1: arXiv:1201.0188v1, *Solution to a non-Archimedean Monge-Ampere equation*.
3. BE: arXiv:1805.01016v3, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*.
4. BJ-triv: arXiv:1801.08229v4, *Global pluripotential theory over a trivially valued field*.
5. BJ-synth: arXiv:2307.01697v1, *Measures of finite energy in pluripotential theory: a synthetic approach*.
6. PS-hybrid: arXiv:2209.04879v2, *Global pluripotential theory on hybrid spaces*.
7. Gubler--Rabinoff: arXiv:2506.13548v2, *Classically psh and pluriharmonic functions on Berkovich spaces*.
8. Thuillier: tel-00010990v1, *Theorie du potentiel sur les courbes en geometrie analytique non archimedienne. Applications a la theorie d'Arakelov*, thesis, 2005.
9. Berkovich: *Etale cohomology for non-Archimedean analytic spaces*, Publications mathematiques de l'IHES 78 (1993), 5--161, supplied Numdam PDF.
10. Chambert-Loir--Ducros: arXiv:1204.6277v2, *Formes differentielles reelles et courants sur les espaces de Berkovich*.


# Actual native canonical notes: every field and support

[
  {
    "id": "n1",
    "summary": "Exact-source audit: saved BFJ 1201.0188v1 retains function-field algebraizability and SNC support; BE 1805.01016v3 reports a descent/resolution-restricted characteristic-p envelope result. All ten source hashes verified.",
    "detailedSummary": "The original proof uses cofinal regular SNC models, skeleton equicontinuity, multiplier-ideal positivity and envelope regularization, followed by locality and algebraizability-dependent orthogonality. The saved 1201.0188 is actual v1. Its algebraizability concerns descent of X to a one-variable function field with completion K; L need not descend. BE's reported positive-characteristic envelope result instead assumes descent of (X,L) and resolution in dimension n+d. These statements do not establish the full positive-residue-characteristic finite-energy equation.",
    "text": "The audit used only input.json, the ten listed public caches and fresh workspace artifacts.\n\nBFJ 1201.0187v2 assumes complete discrete valuation, residue characteristic zero, smooth projective X and ample L. Its banner is 21 January 2014; its internal manuscript date is 22 October 2018. SNC cofinality enters the original psh definition and retractions. Sections 5–8 also use multiplier ideals for positivity, toroidal equicontinuity for normalized compactness, and subadditivity/global generation/vanishing for envelope regularization. Resolution alone does not replace these ideal-theoretic uses.\n\nThe actual saved 1201.0188v1 has banner 30 December 2011. Theorem A requires smooth projective X over complete discretely valued K of residue characteristic zero, ample L, and positive Radon μ of mass (L^n) supported on an SNC dual complex. X must satisfy X=Y_K for smooth projective Y over a one-variable function field F whose completion is K. The statement does not require L to descend. Appendix A uses this algebraizability for orthogonality through compactification and big-line-bundle decompositions. This saved theorem cannot be treated as a later arbitrary-support theorem.\n\n1805.01016v3 is Boucksom–Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. Theorem 9.15 identifies relative volume with relative MA energy for continuous psh metrics on semiample Q-line bundles on geometrically reduced projective varieties over any complete valued field. Smooth X and ample L meet these hypotheses. Section 7.30 still labels unrestricted envelope continuity conjectural. Its reported discrete characteristic-p case assumes descent of (X,L) to a function field of transcendence degree d and resolution in dimension n+d, replacing multiplier ideals with test ideals. The cited GJKM paper is not supplied, so its exact stronger resolution formulation is not independently asserted here. This report gives neither a mixed-characteristic conclusion nor an unbounded equation theorem in this draft.\n\nPille–Schneider 2209.04879v2, Remark 4.4, distinguishes defining E1 from extending MA to E1. Section 1.2 expressly assumes equicharacteristic zero; the shorter wording “characteristic zero” in the remark does not establish a mixed-characteristic endpoint.\n\nExecution evidence: source_audit.py reported 10 verified sources, 20 matching PDF/text SHA256 values, six matching abstract hashes, byte_identical_input=true and 52 literal extracts. The actual 1201.0188v1 PDF SHA256 is 4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a. input.json and input-original.json both have SHA256 b25c64ae0b33d0f726371bae85dff3802a464ea4e786375ad8b558f03215a1f8. assignment-original.txt and task-original.json preserve the decoded assignment/task.\n\nArtifacts: source_audit.py, source-audit-output.json and source-extracts/source-provenance.json, alongside copied PDFs and regenerated PDF text. Provenance includes literal published proof extracts, versions/hashes, line/page locations and application checks. Rerun: python3 source_audit.py. Hash agreement establishes artifact identity, not mathematical correctness.\n\nArtifacts: /workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Published partial theorem: with positive characteristic and trivial valuation, the genuine E1 operator exists in every dimension; arbitrary-support finite-energy measures have unique solutions on smooth projective varieties of dimension at most two. This does not solve the nontrivial valuation axis.",
    "detailedSummary": "Apply Boucksom–Jonsson 1801.08229v4 over algebraically closed trivially valued k of characteristic p>0, smooth connected projective X and ample L. The canonical trivial reference has raw mass V=(L^n). The exact measure condition is sup_H{V E(u)−∫u dμ}<∞ and μ(Xan)=V. The finite-energy pairing defines an approximation-independent genuine MA measure. Comparison and injectivity hold in every dimension. Unconditional positive-characteristic surjectivity uses envelopes proved for dim X≤2, resolving test configurations of dimension n+1≤3 and replacing multiplier ideals with test ideals. Higher-dimensional surjectivity remains conditional on the envelope property.",
    "text": "This is an application of the published theorem in Boucksom–Jonsson 1801.08229v4, not a new solution of P16.3.\n\nHypotheses: k is algebraically closed of characteristic p>0 with trivial absolute value; X/k is smooth, connected and projective, dimension n≥1; L is ample. Fix the canonical trivial reference metric ρ, write ω=c1(L) and V=(L^n)>0. PSH(L) consists of nontrivial usc decreasing limits of Fubini–Study functions m^{-1}max_i(log|s_i|+λ_i), using basepoint-free sections of mL and rational λ_i. Weak convergence means convergence at divisorial valuations. E(u)=(ω,u)^{n+1}/((n+1)V), extended monotonically, and E1={E>−∞}. Raw energy is V E.\n\nThe exact measure condition is positivity, μ(Xan)=V, and E*raw_ρ(μ)=sup_H[V E(u)−∫u dμ]<∞. For ν=μ/V this equals V E∨(ν), and the supremum equals that over E1. To prove this passage, take u_j∈H decreasing to u∈E1. Then E(u_j)→E(u), while ∫u_j dν≥E(u_j)−E∨(ν). Monotone integration of usc functions on compact Xan gives convergence of the integrals; their uniform lower bound proves u∈L1(ν). Every E1 expression is therefore a limit of model expressions. The reverse supremum inequality follows from H⊂E1. Constant tests give c(V−μ(Xan)); rational constants already force exact mass V whenever raw dual energy is finite. No restricted measure is renormalized.\n\nConstruction: use the finite-energy multilinear pairing of Theorem 7.14, whose existence and monotone continuity are published inputs. On PL tests define T_u(f)=(0,f)·(ω,u)^n. Theorem 7.18 gives positivity, T_u(1)=V and |T_u(f)|≤V||f||∞. PL density in C0 and Riesz representation give a unique positive Radon measure MAraw_ρ(u). Pairing continuity gives convergence against every PL test for any decreasing model approximation; the uniform bound extends convergence to all continuous tests. Thus the limit is approximation-independent. Proposition 7.19 identifies the model case with Σ_F b_F((ω_𝓧+D)|_F)^n δ_{v_F}, proves raw mass V and finite-energy integrability. Theorem A supplies strong continuity and dense image in finite-energy measures in every dimension.\n\nLocality is Theorem 7.40 on {u>v}. Apply it to max(u,v−ε), using positivity and mass V, to obtain ∫_{u<v−ε}MAraw(v)≤∫_{u≤v−ε}MAraw(u). Infinite loci are null by finite-energy integrability. Let ε decrease to zero to obtain comparison: ∫_{u<v}MAraw(v)≤∫_{u<v}MAraw(u). Equal MA measures give I(u,v)=0. Corollary 10.4 uses divisorial energy estimates and divisorial determination to infer that u−v is locally constant; connectedness gives one constant. Injectivity holds in every dimension.\n\nFor n≤2, Theorem 5.20 proves the envelope property in characteristic p. The proof reduces obstacles to PL functions, represents envelopes by normalized base ideals, resolves a test configuration of dimension n+1≤3, then uses test ideals for subadditivity/global generation. The resulting estimate forces uniform convergence of nef approximants. Resolution and test-ideal results are background used by the published theorem, not new unrestricted claims. Actual PDF page 62 distinguishes dim X≤2 from dim 𝓧≤3; page 63 states the test-ideal replacement.\n\nThe envelope property gives normalized weak compactness by Theorem 5.11. For finite-energy ν, take a maximizing sequence for Fν(u)=E(u)−∫u dν, normalized to sup u=0. Lemma 9.15 and Corollary 9.16 bound J(u)=sup u−E(u). Compactness gives a subnet limit; upper semicontinuity of energy puts that limit u in E1. Proposition 9.19 supplies L1(ν) convergence. Consequently Fν(u)≥limsup Fν(u_j)=E∨(ν), so u actually attains the supremum.\n\nTheorem 8.5 gives E↓(u+tf)=E(u)+t∫f MA(u)+O(t²) for PL f, uniformly in u. With the envelope property E↓ is envelope energy. For maximizing functions with defect δ_j→0 this gives t∫f MA(u_j)≤t∫f dν+δ_j+C_f t². First let j tend to the limit, then t decrease to zero, and repeat with −f. The constant maximizing sequence u_j=u proves MA(u)=ν; multiplying by V proves MAraw(u)=μ. This is the applicable variational argument of Theorem 12.8 and the positive-characteristic conclusion of Theorem 12.9.\n\nTherefore every arbitrary-support positive Radon measure of raw mass V and finite raw dual energy has a unique finite-energy solution on these smooth projective curves and surfaces. Continuity of the solution is not asserted. For n≥3, operator construction, comparison and injectivity remain established, but surjectivity is conditional on the envelope property. This endpoint does not apply to arbitrary varieties over F_p((t)) or Q_p.\n\nThe full cited argument is in P16.3-argument.md, Section 3, and standalone P16.3-paper.tex. Literal proofs and actual PDF checks are retained in source-extracts/source-provenance.json. Rerun generation/build: python3 build_and_check.py.\n\nArtifacts: /workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Full P16.3 remains unproved here. Arbitrary-field continuous/test MA and synthetic measure approximation do not construct the unbounded operator or an actual solution potential. Requested artifacts are saved; both final TeX passes succeeded.",
    "detailedSummary": "BE supplies continuous genuine MA, and BJ 2307.01697v1 supplies test orthogonality and strong approximation of finite-energy measures without a residue-characteristic restriction. The latter explicitly does not investigate finite-energy potentials; its completed measure space is not identified with E1/R. Six obligations remain on the nontrivial positive-residue-characteristic axis: singular psh compactness, envelope/model positivity replacements, genuine unbounded mixed MA, exact energy/differentiation passages, actual arbitrary-support solutions, and unbounded comparison/injectivity. The 12-page paper, provenance and exact status schema were produced. Compilation and hashes are execution evidence only.",
    "text": "Retain complete nontrivially discretely valued K, smooth connected projective X/K in arbitrary dimension and ample L, with V=(L^n). P16.3 includes equal characteristic (p,p) and mixed characteristic (0,p). The full result is not proved.\n\nEstablished background: choose a continuous semipositive model reference ρ. Genuine model MA has raw mass V. BE Propositions 8.3/8.5 and Theorems 8.4/8.18 provide continuous measures and model calculus. Ample L is semiample, and its continuous psh metrics are psh-regularizable by Theorem 7.14, meeting Theorem 8.4's hypothesis.\n\nFor PL/model tests D_θ, θ=c1(L,ρ), set Eθ(u)=((n+1)V)^{-1}Σ_j∫u(θ+dd^cu)^j∧θ^{n−j} and Jθ(ν)=sup_Dθ(Eθ(u)−∫u dν). The exact established test-side raw condition is μ(Xan)=V and VJθ(μ/V)<∞. BJ-synth 2307.01697v1 verifies projective Berkovich synthetic data using intersection measures, integration by parts and the local Hodge index theorem. Section 1.3.2 does not assert HBC=N1 over every field; its positive cone is the preimage of the ample cone, which suffices here.\n\nExample 2.20 derives test orthogonality from BE and published relative-volume differentiation. Definition 2.15 concerns a directed limit ∫(f−u)MAθ(u)→0 for tests u<f; it does not assert continuity of a psh envelope. Theorem 2.23 proves that maximizing test sequences have MAθ(u_j) converging strongly to ν. Theorem A completes the finite-energy measure space. The introduction expressly does not investigate potentials of finite energy. These results therefore do not produce a limiting usc psh potential or identify completed measures with E1/R. The corresponding equivalence in BJ-triv cannot be imported without its missing analytic inputs.\n\nA narrow genuine nontrivial example works in every dimension: if a smooth projective K°-model has irreducible special fiber and relatively ample extension of L, its reference satisfies MAraw(0)=Vδξ. Energy concavity and the derivative at zero give Eθ(u)≤∫u dδξ, hence Jθ(δξ)=0. This solves one reference target, not arbitrary finite-energy measures or the unbounded operator problem.\n\nGubler–Rabinoff 2506.13548v2 concerns classically psh functions and maximum principles and excludes MA construction from its subject. CLD 1204.6277v2 supplies characteristic-independent local forms/currents and Bedford–Taylor theory without resolution. No identification of all target global finite-energy metrics with its regularizable local class is proved here. Thuillier treats curves; Berkovich 1993 supplies analytic/étale foundations. None is substituted for higher-dimensional global equation theory.\n\nConcrete remaining obligations:\n1. Construct the intended singular psh cone with monotone approximation and normalized compactness, replacing SNC/retraction/toroidal inputs.\n2. Prove model positivity and envelope regularity or an adequate variational substitute without unproved resolution or extra function-field descent, treating mixed characteristic separately.\n3. Construct approximation-independent genuine mixed MA on unbounded E1, with positivity, integrability and full raw mass V.\n4. Prove equality of test and E1 dual suprema and obstacle-energy differentiation on that actual space.\n5. Realize every correctly massed finite-dual-energy Radon measure of arbitrary support by an actual psh potential.\n6. Establish unbounded locality/comparison and injectivity modulo constants.\n\nAlterations, base change, normalization and universal homeomorphisms are not assumed to preserve these structures. Measure density is not substituted for existence, and no restricted measure is renormalized.\n\nDeliverables: P16.3-argument.md, standalone P16.3-paper.tex, P16.3-paper.pdf, source-extracts/source-provenance.json and status.json. The status file has exactly id,status,exact_result,proof_file,concrete_gaps, with status=partial. The final PDF has 12 pages and 349044 bytes. Both final pdflatex passes returned 0. The first had a cross-reference rerun warning; the second did not. Both had two underfull-box diagnostics, with no compilation errors or overfull-box diagnostics. Actual stdout/stderr and TeX logs are retained in build-logs for both passes; earlier build diagnostics were also preserved. build-commands.json records commands/hashes, environment.txt records installed-tool details, and checks.json records input/task preservation and the exact status schema. final-notes.json preserves this note packet; artifact-sha256.json records artifact hashes.\n\nRerun: python3 source_audit.py; python3 build_and_check.py. No installations, network fetches, workers, other-model calls, heavy computation or external messages were used. These are unverified drafts: hashes and compilation do not establish mathematical correctness. The partial theorem in n2 does not solve the original nontrivial positive-residue-characteristic atom; candidate=false.\n\nArtifacts: /workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Exact public source metadata and application checks

{
  "local_source_id": "01-1201.0187",
  "supplied": {
    "arxiv_id": "1201.0187",
    "saved_version": "1201.0187v2",
    "title": "[1201.0187] Singular semipositive metrics in non-Archimedean geometry",
    "public_source": "https://arxiv.org/pdf/1201.0187v2",
    "abstract_url": "https://arxiv.org/abs/1201.0187",
    "actual_abstract_url": "https://arxiv.org/abs/1201.0187",
    "actual_pdf_url": "https://arxiv.org/pdf/1201.0187v2",
    "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.html",
    "abstract_sha256": "983485b15a5da892c0b29ecb5ebb7280414028bd1333614a0ae8bf5ec888dbde",
    "pdf": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.pdf",
    "pdf_sha256": "8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270",
    "pdf_bytes": 768011,
    "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.txt",
    "extract_sha256": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
    "extract_bytes": 175336,
    "pdftotext_returncode": 0,
    "origin": "Publicly available primary mathematical source; no generated research payload."
  },
  "verified_pdf_sha256": "8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270",
  "verified_extract_sha256": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
  "pdf_header_first_lines": [
    "                                               SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN",
    "                                                                   GEOMETRY",
    "",
    "                                                        SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON",
    "arXiv:1201.0187v2 [math.AG] 21 Jan 2014",
    "",
    "",
    "",
    "",
    "                                                  Abstract. Let X be a smooth projective Berkovich space over a complete discrete val-",
    "                                                  uation field K of residue characteristic zero, endowed with an ample line bundle L. We",
    "                                                  introduce a general notion of (possibly singular) semipositive (or plurisubharmonic) met-",
    "                                                  rics on L, and prove the analogue of the following two basic results in the complex case:",
    "                                                  the set of semipositive metrics is compact modulo scaling, and each semipositive metric is",
    "                                                  a decreasing limit of smooth semipositive ones. In particular, for continuous metrics, our",
    "                                                  definition agrees with the one by S.-W. Zhang. The proofs use multiplier ideals and the",
    "                                                  construction of suitable models of X over the valuation ring of K, using toroidal techniques.",
    "",
    "",
    "",
    "",
    "                                                                                         Contents",
    "                                            Introduction                                                                                           1",
    "                                            1. Models of varieties over discrete valuation fields                                                  6"
  ],
  "regenerated_layout_sha256": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/01-1201.0187.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/01-1201.0187-pdf-layout.txt"
  ],
  "application_checks": [
    "Complete discretely valued K; char(residue K)=0; smooth projective X; ample L.",
    "SNC cofinality enters definition, skeleton approximation and compactness; multiplier ideals/vanishing enter model positivity and envelope regularization.",
    "No theorem here is applied over positive residue characteristic."
  ]
}

## Literal published unit 01-1201.0187-literal-lines-105-145.txt

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


## Literal published unit 01-1201.0187-literal-lines-1315-1345.txt



                                    6. Equicontinuity
  The following result is the key to the compactness property in Theorem A.
Theorem 6.1. Let X be a smooth connected projective K-analytic space. Let X be a SNC
model of X and θ ∈ Z 1,1 (X) a closed (1, 1)-form determined on X . Then there exists a
constant C = C(X , θ) > 0 such that for every θ-psh model function ϕ, the composition
ϕ ◦ embX is convex, piecewise affine and C-Lipschitz continuous on each face of ∆X .
Corollary 6.2. With the same notation, the family
                     {ϕ ◦ embX | ϕ a θ-psh model function} ⊂ C 0 (∆X )
is equicontinuous on ∆X .
   The rest of this section is devoted to the proof of Theorem 6.1. For the sake of notational
simplicity we will (in this section only) ignore the map embX and simply view ∆ := ∆X as
a subset of X.
                                               P
   Let us first set some notation. Let X0 = i∈I bi Ei be the irreducible decomposition of the
special fiber of X and ei = evX (xEi ) the vertex of ∆ corresponding to Ei . Recall that
                                                                                      T the
faces σJ of the simplical complex ∆ correspond to subsets J ⊂ I such that EJ = j∈J Ej
is non-empty, in such a way that σJ is a simplex with {ej , j ∈ J} as its vertices. The star
Star(σ) of a face σ of ∆ is defined as usual as the union of all faces of ∆ containing σ.
An irreducible component Ei intersects EJ iff the corresponding vertex ei of ∆ belongs to
Star(σJ ); the intersection is proper iff ei 6∈ σJ .
   Fix an ample line bundle A on X . In what follows we denote by C > 0 a dummy constant,
which may vary from line to line but only depends on X , θ and A.
   Let ϕ ∈ D(X) be a θ-psh model function and π : Y → X a vertical blowup such that
ϕ = ϕG for some G ∈ Div0 (Y)Q . By Proposition 5.9 we have supX ϕ = maxi∈I ϕ(ei ).
Upon replacing G with G − (maxi∈I ϕ(ei ))Y0 we may thus assume that ϕ is normalized by
supX ϕ = 0.

6.1. Bounding the values on vertices. We first prove


## Literal published unit 01-1201.0187-literal-lines-1690-1750.txt

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


## Literal published unit 01-1201.0187-literal-lines-1819-1900.txt

  Our main result in this section is the following regularity property of envelopes. As we
shall see, it is in fact equivalent to the monotone regularization theorem.
Theorem 8.3. For any u ∈ C 0 (X) the θ-psh envelope Pθ (u) is a uniform limit on X of
θ-psh model functions. In particular, Pθ (u) is continuous.
  Before attacking Theorem 8.3 we shall prove the following weaker statement.
Lemma 8.4. Let Peθ (u) be the pointwise supremum of all θ-psh model functions ϕ such that
ϕ ≤ u. Then Peθ (u) ≤ Pθ (u) and equality holds on X qm .
Proof. The inequality Peθ (u) ≤ Pθ (u) is trivial. To prove that equality holds on X qm , pick
ε > 0 and x ∈ embX (∆X ) for some SNC model X on which θ is determined. By construction,
there exists ψ ∈ PSH(X, θ) such that ψ ≤ u and ψ(x) ≥ Pθ (u)(x) − ε. By the definition
of PSH(X, θ), there then exists a θ-psh model function ϕ such that |ϕ − (ψ − ε)| ≤ ε on
embX (∆X ). Thus ϕ ≤ ϕ ◦ pX ≤ ψ ◦ pX ≤ u on X and ϕ(x) ≥ ψ(x) − 2ε ≥ Pθ (u)(x) − 3ε.
We conclude that Peθ (u) = Pθ (u) on X qm .                                                 
Proof of Theorem 8.3. We shall reduce the statement to a geometric assertion that can be
proved using asymptotic multiplier ideals.
   First, we may assume that u ∈ D(X), thanks to Corollary 2.3 and (vi) of Proposition 8.2.
   Second, we can reduce to the case when θ ∈ N 1 (X /S)Q is a rational class, using (vii) of
Proposition 8.2.
   Third, we may further reduce to the case u = 0, after replacing θ with θ + ddc u, using (v)
of Proposition 8.2.
   After scaling, we may finally assume that θ is the curvature form of a model metric
determined by a line bundle L on some model X . Now we conclude the proof using the
following result.                                                                           
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


## Literal published unit 01-1201.0187-literal-lines-2034-2055.txt

   The purpose of this section is to define multiplier ideals on regular S-varieties and establish
their basic properties. We are grateful to Osamu Fujino, János Kollár and Mircea Mustaţǎ
for their helpful suggestions.
   It should be noted that most results in this appendix are also obtained, with simpler
arguments and in a slightly more general setting, in [MN12], which appeared after a first
version of the present paper was completed. We felt, however, that the alternative arguments
presented here might still be of some interest to the reader.
   In this appendix, and as opposed to the main body of the article, it will be more convenient
to use multiplicative notation for Picard groups. We also fix the choice of an isomorphism
R ≃ k[[t]].
42              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


B.1. Kodaira vanishing. The usual compactification argument that reduces the relative
version of Kodaira (or Kawamata-Viehweg) vanishing to its global projective version over k
cannot be applied for S-varieties. Following suggestions of János Kollár and Mircea Mustaţǎ,
we rely instead on a Kodaira-type vanishing theorem on the (possibly reducible) special fiber.
Theorem B.1 (Kodaira vanishing). Let X be an SNC S-variety, denote by ωX its dualizing
sheaf, and let L ∈ Pic(X ) be an ample line bundle. Then we have
                             H q (X , ωX ⊗ L) = 0     for all q ≥ 1.
Proof. By flat base change we may assume that k is algebraically closed. The desired
result is equivalent to Rq f∗ (ωX ⊗ L) = 0 for q ≥ 1 since S is affine, and all fibers of


## Literal published unit 01-1201.0187-literal-lines-2206-2291.txt

B.3. Multiplier ideals. Let us first give the definition of multiplier ideals in our setting:
Definition B.4. Let X be a regular model and let a be a vertical ideal sheaf on X . For each
rational number c > 0 the multiplier ideal of ac is the vertical ideal sheaf of X defined as
                           J (ac ) := π∗ OX 0 KX 0 /X − bc Dc
                                                               

where π : X 0 → X is a vertical blowup with X 0 SNC such that π −1 a · OX 0 is locally principal
and D ∈ Div0 (X 0 ) is the corresponding effective Cartier divisor.
             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                         45


   This definition only depends on the model function c log |a| (cf. [JM12]), and would in
fact make sense for an arbitrary non-positive model function ϕ ∈ D(X).
   If a• is a graded sequence of vertical ideals, then J (ac• ) is defined as the largest element
                                      c/m
of the family of coherent ideals J (am ), m ≥ 1, see [Laz, Definition 11.1.5].
   As a matter of terminology, if L is a line bundle on a model X , a is a vertical coherent
ideal sheaf and c > 0 then we shall say that L⊗ac is nef if π ∗ L−cD is nef, where π : X 0 → X
is the normalization of the blowup of X along a and a · OX 0 = OX 0 (−D). In other words, the
model function c log |a| is required to be θ-psh, where θ is the curvature form of the model
metric on L induced by L.
   Using Theorem B.3 we may follow the usual line of arguments to prove the following basic
vanishing property of multiplier ideals:
Theorem B.5 (Nadel Vanishing). Let X be a regular model of X and L ∈ Pic(X ) a line
bundle whose restriction to X is ample. If a is a vertical coherent ideal sheaf on X and
c > 0 is a rational number such that L ⊗ ac is nef, then we have
                         H q (X , ωX ⊗ L ⊗ J (ac )) = 0 for all q ≥ 1.
In particular, if a• is a graded sequence of vertical coherent ideal sheaves on X such that
Lm ⊗ am is globally generated for all sufficiently divisible m, then
                         H q (X , ωX ⊗ L ⊗ J (a• )) = 0 for all q ≥ 1.
Proof. Let π : X 0 → X be an SNC model dominating the blowup of X along a, so that we
have a · OX 0 = OX 0 (−D) for some effective divisor D ∈ Div0 (X 0 ). By the projection formula
we have
                        ωX ⊗ L ⊗ J (ac ) = π∗ (ωX 0 ⊗ π ∗ L(−bc Dc)) .
Now π ∗ L − c D is nef and c D − bc Dc has coefficients in [0, 1[. Lemma B.6 below together
with the projection formula yields
                        Rq π∗ (ωX 0 ⊗ π ∗ L (−bc Dc)) = 0 for all q ≥ 1.
The Leray spectral sequence is thus degenerate and we conclude using Theorem B.3. The
                                         1/m
second point follows since J (a• ) = J (am ) for some m by construction, while the global
                                          1/m
generation assumption implies that L ⊗ am is nef.                                      
Lemma B.6 (Local vanishing). Let X be a regular model, let a be a vertical ideal sheaf on
X and let π : X 0 → X be an SNC model such that a · OX 0 = OX 0 (−D) with D ∈ Div0 (X 0 ).
Then we have
                          Rq π∗ ωX 0 (−bc Dc) = 0 for all q ≥ 1.
Proof. We argue as in the last part of the proof of Theorem B.3. Let A ∈ Pic(X ) be
sufficiently ample to guarantee:
     (i) π ∗ A − cD is nef.
    (ii) A ⊗ Rq π∗ ωX 0 (−bc Dc) is globally generated on X .
   (iii) H p (X , A ⊗ Rm π∗ ωX 0 (−bc Dc)) = 0 for all p ≥ 1 and m ≥ 0.
Note that the first condition can be achieved since −D is π-globally generated. The degen-
eration of the Leray spectral sequence shows that
                H 0 (X , A ⊗ Rq π∗ ωX 0 (−bc Dc)) = H q X 0 , ωX 0 (−bc Dc) ⊗ π ∗ A ,
                                                                                   
46              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


which vanishes by Theorem B.3. It follows that A ⊗ Rq π∗ ωX 0 (−bc Dc) = 0 by global
generation, whence the result.                                                    
   We may now deduce from the above results the following two consequences that we need
in the proof of Theorem B.
Theorem B.7 (Subadditivity). Let X be a regular model, a, b vertical coherent ideal sheaves
on X and c, d > 0. Then we have
                                    J (ac · bd ) ⊂ J (ac ) · J (bd ).
Proof. This is proved exactly as in [Laz, Theorem 9.5.20] using local vanishing.                     (See
also [JM12, Theorem A.2] for a different proof.)                                                       
Theorem B.8 (Uniform generation property). Let X be a regular model. Then there exists
an ample line bundle A on X such that the following holds. Given L ∈ Pic(X ), a vertical
ideal sheaf a and a rational number c > 0 such that L ⊗ ac is nef, the sheaf
                                           A ⊗ L ⊗ J (ac )
is globally generated. In particular, if a• is a graded sequence of vertical coherent ideal
sheaves on X such that Lm ⊗ am is globally generated for all sufficiently divisible m, then
                                          A ⊗ Lm ⊗ J (am
                                                       • )
is globally generated for all m.
Remark B.9. Fix any ample line bundle B on X . Since, for any line bundle A0 , the line
bundle B n ⊗ (A0 )−1 is globally generated for n  0, we may take A := B n with n sufficiently
large in the previous statement.
Proof. Let B be a given very ample line bundle such that A := ωX ⊗ B n+1 is ample. By the
Castelnuovo-Mumford criterion it is enough to check that
                            H q X , A ⊗ L ⊗ B −q ⊗ J (ac ) = 0
                                                          

for q = 1, . . . , n, and this is a consequence of Theorem B.5.                                         



# Exact public source metadata and application checks

{
  "local_source_id": "02-1201.0188",
  "supplied": {
    "arxiv_id": "1201.0188",
    "saved_version": "1201.0188v1",
    "title": "[1201.0188] Solution to a non-Archimedean Monge-Ampère equation",
    "public_source": "https://arxiv.org/pdf/1201.0188v1",
    "abstract_url": "https://arxiv.org/abs/1201.0188",
    "actual_abstract_url": "https://arxiv.org/abs/1201.0188",
    "actual_pdf_url": "https://arxiv.org/pdf/1201.0188v1",
    "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.html",
    "abstract_sha256": "e4683a68defd5887b5952cddcccc9f625a2d0391819a97f32a15d4d51f5409ae",
    "pdf": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf",
    "pdf_sha256": "4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a",
    "pdf_bytes": 531005,
    "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.txt",
    "extract_sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
    "extract_bytes": 161436,
    "pdftotext_returncode": 0,
    "origin": "Publicly available primary mathematical source; no generated research payload."
  },
  "verified_pdf_sha256": "4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a",
  "verified_extract_sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
  "pdf_header_first_lines": [
    "                                          SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION",
    "",
    "                                                      SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON",
    "arXiv:1201.0188v1 [math.AG] 30 Dec 2011",
    "",
    "",
    "",
    "",
    "                                                Abstract. Let X be a smooth projective Berkovich space over a complete discrete valu-",
    "                                                ation ﬁeld K of residue characteristic zero, and assume that X is deﬁned over a function",
    "                                                ﬁeld admitting K as a completion. Let further µ be a positive measure on X and L be",
    "                                                an ample line bundle such that the mass of µ is equal to the degree of L. Then we show",
    "                                                the existence a continuous semipositive metric whose associated measure is equal to µ in",
    "                                                the sense of Zhang and Chambert-Loir. This we do under a technical assumption on the",
    "                                                support of µ, which is, for instance, fulﬁlled if the support is a ﬁnite set of divisorial points.",
    "                                                Our method draws on analogues of the variational approach developed to solve complex",
    "                                                Monge-Ampère equations on compact Kähler manifolds by Berman, Guedj, Zeriahi and the",
    "                                                ﬁrst named author, and of Kolodziej’s C 0 -estimates. It relies in a crucial way on the com-",
    "                                                pactness properties of singular semipositive metrics, as deﬁned and studied in a companion",
    "                                                article.",
    "",
    "",
    "",
    ""
  ],
  "regenerated_layout_sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/02-1201.0188.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/02-1201.0188-pdf-layout.txt"
  ],
  "application_checks": [
    "Actual saved PDF is v1, with algebraizability in the function-field-completion sense and SNC-dual-complex support in Theorem A.",
    "Algebraizability is not merely that X is an algebraic K-variety; L need not descend in this v1 statement.",
    "Appendix A uses algebraizability for orthogonality. No later-version hypothesis is silently substituted."
  ]
}

## Literal published unit 02-1201.0188-literal-lines-62-105.txt

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


## Literal published unit 02-1201.0188-literal-lines-230-332.txt

in [BBGZ09] to handle general measures disappear, since it is enough to extend Eω to a usc
functional Eω : PSH(X, ω) → [−∞, +∞[, which is done by setting
                              
                 Eω (ϕ) := inf Eω (ψ) | ψ ≥ ϕ, ψ ∈ C 0 (X) ∩ PSH(X, ω) .
6              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

   Step 2 requires much more work and constitutes the main body of the article, in partic-
ular because virtually none of the more classical results in pluripotential theory on which
[BBGZ09] was able to rely were available so far in our non-Archimedean context. The only
obvious information we have on the maximizer ϕ0 of Fµ is that it lies in the set

                        E 1 (X, ω) := {ϕ ∈ PSH(X, ω), Eω (ϕ) > −∞}
of ω-psh functions with finite energy. In the complex case, E 1 (X, ω) was introduced in
[Ceg98, GZ07] as a higher dimensional and non-linear generalization of the classical Dirichlet
space from potential theory. The goal of Step 2 is to show that the Monge-Ampère operator
can be naturally extended to E 1 (X, ω), and that ϕ0 satisﬁes
                                      (ω + ddc ϕ0 )n = µ
in this generalized sense.
   In order to do so, we ﬁrst extend the Monge-Ampère operator from continuous to bounded
ω-psh functions, following the fundamental work of Bedford and Taylor [BT82, BT87]. As in
the complex case, this mild generalization is in fact crucial in order to develop a reasonable
capacity theory, and also because the natural bounded approximants max{ϕ, −m}, m ∈ N,
of a given ω-psh function ϕ are not continuous in general. It is however substantially
more involved than the continuous case, since uniform convergence has to be replaced with
monotone convergence. The fact that any (bounded) ω-psh function can be written as a
decreasing limit of a family of ω-psh model functions, proved in [BFJ11], plays a key role at
this stage.
   Of crucial importance is the following locality property of the Monge-Ampère operator: if
ϕ, ψ are bounded ω-psh functions, then the restrictions of the measures (ω +ddc max{ϕ, ψ})n
and (ω + ddc ϕ)n to the Borel set {ϕ > ψ} coincide. Note that, even when ϕ, ψ are model
functions, this fact is not clear from the deﬁnition in terms of intersection numbers.
   Next, we further extend the Monge-Ampère operator from bounded ω-psh functions to
functions with ﬁnite energy. The key observation, which goes back to [BT87], is the mono-
tonicity of the sequence of measures
                         1{ϕ>−m} (ω + ddc max{ϕ, −m})n (m ∈ N)
a direct consequence of the locality property. This allows us to deﬁne (ω + ddc ϕ)n as
the increasing limit of this sequence of measures, which is shown to be well-behaved for
ϕ ∈ E 1 (X, ω). More generally, mixed Monge-Ampère measures are shown to be well-deﬁned
for functions in E 1 (X, ω), and (1.3), (1.4) are still valid in this generality.
   As was already pointed out, these facts are however a priori not enough to show that the
maximizer ϕ0 of Fµ satisﬁes (ω + ddc ϕ0 )n = µ, because small perturbations of ϕ0 cease to be
ω-psh in general. In order to handle a similar diﬃculty in the setting of real Monge-Ampère
equations, Alexandrov devised in [Ale38] an envelope argument, an analogue of which was
subsequently found in the complex case in [BBGZ09]. Following the same lead, we introduce
the ω-psh envelope Pω (f ) of a given continuous function f on X by setting for each x ∈ X
                     Pω (f )(x) := sup {ϕ(x) | ϕ ∈ PSH(X, ω), ϕ ≤ f } .
It follows from [BFJ11] that Pω (f ) is the largest ω-psh function dominated by f on X.
The key point is then the following differentiability property, whose complex analogue was
                SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                                  7

established in [BB10]:
                                                     Z
                         d
                                Eω ◦ Pω (f + tg) =         g (ω + ddc Pω (f ))n                   (1.5)
                         dt t=0                        X
for any two f, g ∈ C 0 (X), which may more vividly be written as the chain rule-like formula
(Eω ◦ Pω )′ = Eω′ ◦ Pω . Granted (1.5), a fairly direct argument based on the monotonicity of
Eω implies (ω + ddc ϕ0 )n = µ as desired.
   TheR proof of (1.5) can be reduced by elementary arguments to the diﬀerentiability of
t 7→ Pω (f + tg) (ω + ddc Pω (f ))n , which in turn ultimately follows from the following
orthogonality property:
                             Z
                                (f − Pω (f )) (ω + ddc Pω (f ))n = 0.                   (1.6)
                                X
Since f ≥ Pω (f ), this relation means that (ω + ddc Pω (f ))n is supported on the contact locus
{f = Pω (f )}, a well-known fact in the complex case where the proof argues by balayage,
using Bedford and Taylor’s solution to the Dirichlet problem for the homogeneous complex
Monge-Ampère equation on the ball. Such an approach seems far beyond reach in the non-
Archimedean case. We proceed instead by translating (1.6) into an intersection theoretic
statement on a model of X, where it boils down to the orthogonality of relative asymptotic
Zariski decompositions for a line bundle that is ample on the generic ﬁber. It is precisely
at this point that we use the assumption that X is algebraizable. Indeed, this allows us
to choose the model where we work to be algebraic, and therefore compactiﬁable into a
projective variety over the residue ﬁeld k. As explained in Appendix A, we can then reduce
to the absolute case of big line bundles on projective varieties treated in [BDPP04].
   Finally, Step 3 is handled by adapting in a fairly direct manner the capacity estimates
of Kolodziej [Kol98, Kol03] to prove that ϕ0 is actually continuous. The proof relies on the
locality property in E 1 (X, ω). This shows the existence part of Theorem A’. Uniqueness is
proved following [Blo03], as in [YZ10].

   Our result is not optimal, and we next discuss three important assumptions that we use
in Theorems A and A’.
   First, the condition that the measure µ be supported on a dual complex is probably
unnecessarily strong. Relying on ideas of Cegrell [Ceg98], Guedj and Zeriahi [GZ07] have
deﬁned in the case of compact Kähler manifolds a class E(X, ω) of ω-psh functions where the
Monge-Ampère operator is well-deﬁned and such that the measures (ω+ddc ϕ)n , ϕ ∈ E(X, ω)
are exactly the positive measures µ on X giving zero mass to pluripolar2 sets. The function ϕ
is here again uniquely determined up to an additive constant by its Monge-Ampère measure,
as was later shown by Dinew [Din09]. We expect the corresponding results to be true in
our setting, too. The proof would probably require an even more systematic development of
pluripotential theory in a non-Archimedean setting, something that is certainly of interest.
   Second, as explained above, the proof of the orthogonality property (1.6) relies in a crucial
way on the algebraizability assumption for X. It would be interesting to drop this condition,
which we expect to be an unnecessary restriction.
   Finally, our variational approach uses the compactness of the space PSH(X, ω)/R, which
was obtained in [BFJ11]. The proof of this fact relied heavily on the existence of SNC
  2A subset set A ⊂ X is pluripolar if there exists an ω-psh function ϕ such that A ⊂ {ϕ = −∞}.
8                SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

models, which are so far only available in residue characteristic zero. It seems to be a
challenging task to extend our methods and results to local ﬁelds and more general complete
non-Archimedean ﬁelds. See [FJ04, BFJ08] for related work in the case of a trivially valued
ﬁeld.


## Literal published unit 02-1201.0188-literal-lines-1400-1439.txt

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


## Literal published unit 02-1201.0188-literal-lines-1540-1564.txt


But we have
               f + εg = (1 − ε)f + εPω (f ) ≥ (1 − ε)Pω (f ) + εPω (f ) = Pω (f ),
hence Eω (Pω (f + εg)) ≥ Eω (Pω (f )) by monotonicity of Eω , and the result follows.
               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                         33

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


## Literal published unit 02-1201.0188-literal-lines-1932-1946.txt

we say that (θ, f ) satisﬁes the orthogonality property if
                              Z
                                  (Pθ (f ) − f ) (θ + ddc Pθ (f ))n = 0           (A.1)
                               X
holds. It is convenient in what follows not to require that θ be semipositive, as opposed to
the main body of the text.
Lemma A.1. Fix α ∈ N 1 (X) any ample class. Then the following assertions are equivalent:
  (1) For any form θ such that {θ} = α and any continuous function f , the pair (θ, f )
      satisfies the orthogonality property.
  (2) For any form θ such that {θ} = α and any model function f , the pair (θ, f ) satisfies
      the orthogonality property.
  (3) For any form θ such that {θ} = α, the pair (θ, 0) satisfies the orthogonality property.
   When any of these properties hold, we simply say that the class α (or θ) satisﬁes the
orthogonality property.
                SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                         41


## Literal published unit 02-1201.0188-literal-lines-2054-2112.txt

  Recall that X is said to be algebraizable if there exists a (one-variable) function ﬁeld F
admitting K as a completion and a smooth projective F -scheme Y such that X = YK .
Theorem A.4. Let X be an algebraizable smooth projective K-variety. Then all ample
classes in N 1 (X) have the orthogonality property.
               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                       43

Proof of Theorem A.4. Let us ﬁx an ample class α ∈ N 1 (X). By Lemma A.2 we may assume
α ∈ N 1 (X)Q .
   Since X is algebraizable, we can ﬁnd a smooth projective curve B over the residue ﬁeld
k such that F = k(B); a closed point 0 ∈ B and a regular parameter t ∈ OB,0 inducing an
isomorphism S ≃ Spec O   bB,0 ; and a smooth projective variety Y over F such that X = YK .
   By Lemma A.5 below we may then choose an ample Q-line bundle L ∈ Pic(Y )Q mapping
to α in NQ1 (X). We can also ﬁnd a normal, ﬂat and projective B-scheme Y having Y as its

generic ﬁber and such that L ∈ Pic(Y )Q extends to L ∈ Pic(Y)Q . The latter is therefore
ample on the generic ﬁber of the structure morphism π : Y → B, hence in particular π-big.
Since the natural morphism X := Y ×B S → Y is regular, X is normal, as well as ﬂat and
projective over S, hence a model of X according to our deﬁnition. The Q-line bundle L
induces L ∈ Pic(X )Q .
   The curvature form θ ∈ Z 1,1 (X) of the model metric deﬁned by L has α as its de Rham
class. Our goal is to show that (A.1) holds for each f ∈ D(X). We may in fact assume that
f = 0. Indeed let X ′ be a determination of f , which may be taken to dominate Y. The
model X ′ is then the blow-up of X along a vertical ideal sheaf a. Since (tm ) ⊂ a for some
m ∈ N, a comes from an ideal sheaf on Y, and the blow-up Y′ of Y along this ideal satisﬁes
Y′ ×B S = X ′ since blow-ups commute with ﬂat base change. Replacing Y with Y′ , we
may thus assume that X is a determination of f , so that there exists a vertical Q-divisor
E ∈ Div0 (X ) such that f = fE . Since E is vertical, it also comes from Y. Replacing L with
L + E reduces us as desired to the case f = 0.
   After perhaps passing to a multiple, we may further assume that L ∈ Pic(Y). Accord-
ing to Lemma A.3, we are to show that the approximate Zariski decompositions of L are
asymptotically orthogonal.
   Denote by am the base-ideal of mL on X , and let bm ⊂ OY be the relative base-ideal
of mL on Y/B. By ﬂat base change we have am = bm · OX . Let ρm : Ym → Y be
the normalized blow-up of Y, and let Gm be the eﬀective Cartier divisor of Ym such that
OYm (−Gm ) = bm · OYm . Note that Gm is supported on ﬁnitely many ﬁbers over B for
m ≫ 1, since mL is π-ample. Observe also that Gm pulls back to the similarly deﬁned
divisor Fm on Xm := Ym ×B S. Finally set Mm := ρ∗m (mL) − Gm , which pulls back to Mm
on Xm . Once again by ﬂat base change, it is enough to show that
                                        1
                                             n 1        
                                  lim m   Mm · m     Gm = 0.
                               m→∞
We are going to prove this by reducing to the absolute case of a big line bundle D on Y. By
Lemma A.6 below we may choose an ample line bundle H ∈ Pic(B) such that the sheaves
                                  OB (mH) ⊗ π∗ OY (mL)
are globally generated over B for all m ≫ 1 suﬃciently divisible. Since L is π-big, we may
assume (after perhaps replacing H with a large enough multiple) that D := L + π ∗ H is a
big line bundle on the projective k-variety Y.
   The relative base-ideal bm of mL coincides with the relative base-ideal of mD since mL
and mD are π-linearly equivalent by construction. The fact that
                           OB (mH) ⊗ π∗ OY (mL) = π∗ OY (mD)
is globally generated therefore shows that bm is also the (absolute) base-ideal of mD. As
a consequence we get that Pm := ρ∗m (mD) − Gm is the (absolute) base-point free part
44             SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

                                                          1
                                                              n    1
                                                                         
of mD, and we infer from [BDPP04, Theorem 4.1] that m       Pm · m    Gm → 0. But


# Exact public source metadata and application checks

{
  "local_source_id": "03-1805.01016",
  "supplied": {
    "arxiv_id": "1805.01016",
    "saved_version": "1805.01016v3",
    "title": "[1805.01016] Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry",
    "public_source": "https://arxiv.org/pdf/1805.01016v3",
    "abstract_url": "https://arxiv.org/abs/1805.01016",
    "actual_abstract_url": "https://arxiv.org/abs/1805.01016",
    "actual_pdf_url": "https://arxiv.org/pdf/1805.01016v3",
    "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.html",
    "abstract_sha256": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a",
    "pdf": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.pdf",
    "pdf_sha256": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
    "pdf_bytes": 1034400,
    "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
    "extract_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
    "extract_bytes": 344553,
    "pdftotext_returncode": 0,
    "origin": "Publicly available primary mathematical source; no generated research payload."
  },
  "verified_pdf_sha256": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
  "verified_extract_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
  "pdf_header_first_lines": [
    "                                              SPACES OF NORMS, DETERMINANT OF COHOMOLOGY AND",
    "                                                 FEKETE POINTS IN NON-ARCHIMEDEAN GEOMETRY",
    "",
    "                                                                  SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON",
    "arXiv:1805.01016v3 [math.AG] 8 Jan 2021",
    "",
    "",
    "",
    "",
    "                                                 Abstract. Let L be an ample line bundle on a (geometrically reduced) projective variety",
    "                                                 X over any complete valued field. Our main result describes the leading asymptotics of",
    "                                                 the determinant of cohomology of large powers of L, with respect to the supnorm of a",
    "                                                 continuous metric on the Berkovich analytification of L. As a consequence, we establish",
    "                                                 in this setting the existence of transfinite diameters and equidistribution of Fekete points,",
    "                                                 following a strategy going back to Berman, Witt Nyström and the first author for complex",
    "                                                 manifolds. In the non-Archimedean case, our approach relies on a version of the Knudsen–",
    "                                                 Mumford expansion for the determinant of cohomology on models over the (possibly non-",
    "                                                 Noetherian) valuation ring, as a replacement for the asymptotic expansion of Bergman",
    "                                                 kernels in the complex case, and on the reduced fiber theorem, as a replacement for the",
    "                                                 Bernstein–Markov inequalities. Along the way, a systematic study of spaces of norms and",
    "                                                 the associated Fubini–Study type metrics is undertaken.",
    "",
    "",
    ""
  ],
  "regenerated_layout_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/03-1805.01016.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/03-1805.01016-pdf-layout.txt"
  ],
  "application_checks": [
    "Actual paper is Boucksom--Eriksson, Spaces of norms, determinant of cohomology and Fekete points.",
    "Smooth X is geometrically reduced; ample L is semiample, so Theorem 9.15 applies to continuous psh metrics over every complete valued field.",
    "Conjecture 7.30 is not a theorem. Section 7.30 reports a characteristic-p discrete envelope result only with function-field descent of (X,L) and assumed resolution in dimension n+d; the cited GJKM19 primary paper is not among the ten inputs.",
    "The continuous psh result is not an unbounded E1 existence theorem."
  ]
}

## Literal published unit 03-1805.01016-literal-lines-1-21.txt

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


## Literal published unit 03-1805.01016-literal-lines-2548-2583.txt

                                 m−1 FS(mφ) ≤ Q(φ) ≤ P(φ) ≤ φ,
and we are done since k · kFS(mφ) = k · kmφ on H0 (mLred ), by Lemma 7.23.                 
Definition 7.28. Let L be a semiample Q-line bundle. We say that continuity of envelopes
holds for L if for any continuous metric φ on L, P(φ) = Q(φ) is continuous.
   By Theorem 7.26 and Dini’s lemma, P(φ) is continuous iff m−1 FS(mφ) converges uni-
formly as m → ∞.
54                           SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

Lemma 7.29. Continuity of envelopes is equivalent to the following property: for any family
(φα ) of psh metrics on L, uniformly bounded above, the usc upper envelope (supα φα )⋆ is psh.
Proof. Suppose first that continuity of envelopes holds, and let φ be a continuous metric on L.
Since each FS(mφ) is continuous, P(φ) = supm m−1 FS(mφ) is lsc, and its usc regularization
P(φ)⋆ is the decreasing limit of a net of asymptotically Fubini–Study metrics ψj . Since
P(φ) ≤ φ and φ is continuous, limj ψj = P(φ)⋆ ≤ φ, and (a small variant of) Dini’s lemma
therefore yields ψj ≤ φ+εj for some constants εj → 0. It follows that ψj = P(ψj ) ≤ P(φ)+εj ,
and hence P(φ)⋆ ≤ P(φ) in the limit, which proves that P(φ) is usc.
   Conversely, asssume that P(φ) is continuous for each continuous metric φ, and let (φα )
be a family of psh metrics, uniformly bounded above. The metric ψ := (supα φα )⋆ , being
usc, can be written as the limit of a decreasing net of continuous metrics τj . For each α, j,
we have φα ≤ τj , and hence φα ≤ P(τj ), which in turn yields ψ ≤ P(τj ) ≤ τj . We have
thus written ψ as the limit of the decreasing net of psh metrics P(τj ), which shows that ψ
is psh.                                                                                      
   In the Archimedean case, the equivalent formulation of Lemma 7.29 is a classical property,
assuming X to be normal. It is thus natural to conjecture:
Conjecture 7.30. Continuity of envelopes holds for any semiample Q-line bundle L over
a normal projective variety X.
   As of this writing, continuity of envelopes in the non-Archimedean case has been estab-
lished when X is smooth and one of the following is satisfied:
      • X is a curve, as a consequence of A. Thuillier’s work [Thu05] (see [GJKM19]);
      • K discretely or trivially valued, of residue characteristic 0 [BFJ16, BJ18a], building
        on multiplier ideals and the Nadel vanishing theorem;
      • K is discretely valued of characteristic p, (X, L) is defined over a function field
        of transcendence degree d, and resolution of singularities is assumed in dimension
        n + d [GJKM19], replacing multiplier ideals with test ideals.
   We conclude this section with the following application of Theorem 7.26.
Theorem 7.31. Assume that X is geometrically reduced. Let φ be a continuous metric on


## Literal published unit 03-1805.01016-literal-lines-2640-2766.txt

vious construction produces a positive measure δX on Q    the finite set X an , which is described
as follows. We have a product decomposition A = i Ai into local finite K-algebras Ai
corresponding to the connected components of X. The (reduced) irreducible components of
X are given by Xi = Spec Ki , where the residue field Ki of Ai is a finite extension of K,
and the uniquePextension of the absolute value of K to Ki defines a point xi ∈ X an . The
current δX = i mi δXi is a measure on X an , and the requirement that δXi has total mass
deg π⋆ [Xi ] = [Ki : K] yields δXi = [Ki : K]δxi . As mi [Ki : K] = dimK Ai , we conclude that
                                           X
                                     δX =     (dimK Ai )δxi .
                                                 i

Proposition 8.3. For each tuple φ1 , . . . , φn of smooth metrics on Q-line bundles L1 , . . . , Ln ,
the mixed Monge–Ampère measure ddc φ1 ∧ . . . ∧ ddc φn ∧ δX satisfies the following properties:
    (i) it is a symmetric, multilinear function of the φi , and a positive Radon measure if
        the φi are semipositive, i.e. ddc φi ≥ 0;
56                         SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON
           R
      (ii) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX = (L1 · . . . · Ln );
     (iii) if L0 = L1 = OX (and hence φ0 , φ1 are smooth functions on X an ), then
      Z                                              Z
          φ0 dd φ1 ∧ dd φ2 ∧ . . . ∧ dd φn ∧ δX = φ1 ddc φ0 ∧ ddc φ2 ∧ . . . ∧ ddc φn ∧ δX .
               c        c              c
                                                                                               (8.2)

     (iv) for any complete field extension F/K, we have
                 p⋆ (ddc φ1,F ∧ . . . ∧ ddc φn,F ∧ δXF ) = ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
         where φi,F is the pullback of φi to Li,F and p : XFan → X an is the canonical projection.
Proof. (i) is straightforward. (ii) is classical in the Archimedean case, and proved in [CLD12,
Proposition 6.4.3] in the non-Archimedean case. (iii) is a consequence of the Stokes formula
(see [CLD12, Théorème 3.12.2] in the non-Archimedean case). In the Archimedean case, (iv)
is nontrivial only when K = R, F = C, in which case it holds by definition (see Remark 8.1).
In the non-Archimedean case, it is implicit in [CLD12], and can be checked as follows. Pick
a smooth, compactly supported function f on X an , and consider the smooth, compactly
supported (n, n)-form α := f ddc φ1 ∧ . . . ∧ ddc φn . According to [Gub16, Proposition 5.13],
there exists a Zariski open subset U ⊂ X with a closed embedding U ֒→ Grm,K and a
compactly supported smooth (n, n)-superform on Rr such that α is obtained by pulling-
back η by the tropicalization map Trop : U an → Rr , and
                             Z                                  Z
                                      c              c
                                f dd φ1 ∧ · · · ∧ dd φn ∧ δX =     α
                                                                          X
is defined as the integral of η on the tropical cycle Trop(U ). Unravelling the definitions, it
is clear that the pull-back αF of α to XFan is simply the pull-back of η by the tropicalization
map TropF : UFan → Rr . The construction of the tropical cycle of an algebraic variety being
invariant under ground field extension,
                                  R       Rwe have TropF (UF ) = Trop(U ) as tropical cycles,
and we conclude as desired that X α = XF αF .                                                 
   Recall from §7.3 that a continuous metric on a Q-line bundle L is psh-regularizable iff it is
a uniform limit of smooth semipositive metrics on L. If L is semiample, then any continuous
psh metric (in the sense of Definition 7.2, i.e. a uniform limit of Fubini–Study metrics) is
psh-regularizable, by Theorem 7.14.
Theorem 8.4. Let L1 , . . . , Ln be Q-line bundles on X. The measure-valued operator
                             (φ1 , . . . , φn ) 7→ ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
defined so far on smooth metrics, admits a unique continuous extension to tuples of contin-
uous, psh-regularizable metrics on the Li , with respect to uniform convergence for tuples of
metrics, and the weak topology on Radon measures.
     As a direct consequence of Proposition 8.3, we get:
Proposition 8.5. For each tuple of continuous, psh-regularizable metrics (φi ),
                                            X
             ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα
                                                     α

is a positive Radon measure on X an , of total mass (L1 · . . . · Ln ). It is further symmetric
and multiadditive as a function of the φi .
                    NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                          57

   Theorem 8.4 follows from the classical Bedford–Taylor theory [BT76] in the Archimedean
case, and from its analogue in the non-Archimedean case [CLD12, Corollaire 5.6.5]. In the
present global setting, one can however provide a simple direct argument, based on the
following global version of the classical Chern–Levine–Nirenberg inequality that will be put
to use again a bit later.
Lemma 8.6. Let L0 , . . . , Ln be line bundles on X, and suppose given a pair of smooth,
semipositive metrics φi , φ′i on each Li . Then
       Z                                            Z
          (φ0 − φ′0 ) ddc φ1 ∧ . . . ∧ ddc φn ∧ δX − (φ0 − φ′0 ) ddc φ′1 ∧ . . . ∧ ddc φ′n ∧ δX

                                                  n
                                                  X
                                           ≤C           sup |φi − φ′i |
                                                  i=1

with C := 2 max1≤i≤n (L0 · L1 · . . . · Lbi · . . . · Ln ).
Proof. For brevity of notation, set T := ddc φ2 ∧ . . . ∧ ddc φn ∧ δX . By (8.2),
       Z                         Z                          Z
         (φ0 − φ′0 ) ddc φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T = (φ0 − φ′0 ) ddc (φ1 − φ′1 ) ∧ T
          Z                                       Z                              Z
      =       (φ1 − φ′1 ) ddc (φ0 − φ′0 ) ∧ T =       (φ1 − φ′1 ) ddc φ0 ∧ T +       (φ1 − φ′1 ) ddc φ′0 ∧ T.

Since ddc φ0 ∧ T and ddc φ′0 ∧ T are both positive measures of mass (L0 · L2 · . . . · Ln ), we infer
     Z                          Z
       (φ0 − φ0 ) dd φ1 ∧ T − (φ0 − φ′0 ) ddc φ′1 ∧ T ≤ 2(L0 · L2 · . . . · Ln ) sup |φ1 − φ′1 |.
                ′   c


We conclude by symmetry and multilinearity.                                                                     
Proof of Theorem 8.4. Assume first that K is non-Archimedean, and pick f ∈ PLR (X an ).
By Lemma 5.17, we can find a pair of Fubini–Study metrics on an ample line bundle L0 such
that f = φ0 − φ′0 . By Theorem 7.14, φ0 and φ′0 are uniform limits of smooth, semipositive
metrics on L0 . Lemma 8.6 thus shows that
                                             Z
                        (φ1 , . . . , φn ) 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX

is Lipschitz continuous with respect to the supnorm on tuples of smooth, semipositive met-
rics (with Lipschitz constant depending on f ), and hence extends continuously to tuples of
continuous, psh-regularizable metrics. For eachR tuple of continuous, psh-regularizable met-
rics (φi ), the linear form on PLR (X an ) f 7→ f ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is positive, hence
continuous, and it thus extends to a positive linear form on C0 (X), by density of PLR (X an ).
   In the Archimedean case, the argument is similar, arguing with a smooth function f
instead. It is in fact even simpler, since f can directly be written as a difference of smooth
psh metrics on some ample line bundle.                                                         
   In order to exploit the multilinearity of the previous construction, it is convenient to
introduce the following terminology.
Definition 8.7. We say that a continuous metric φ on a line bundle L is dpsh if it can be
written as a difference of continuous, psh-regularizable metrics.
58                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

     A dpsh metric is thus the same as an approachable metric in the sense of [CLD12, §6.3].
Lemma 8.8. Every line bundle L admits a smooth, dpsh metric.
Proof. By Theorem 7.14, any ample line bundle admits a smooth, semipositive metric, and
the result follows since L can be written as a difference of ample line bundles.      
Example 8.9. If K is Archimedean, every smooth metric is dpsh.
   While this is probably true in the non-Archimedean case as well, it is less obvious, since
strictly positive (1, 1)-forms do not exist globally in this context.
Example 8.10. If K is non-Archimedean, every R-PL metric is dpsh, by Lemma 5.17.
   The operator (φ1 , . . . , φn ) 7→ ddc φ1 ∧. . .∧ddc φn ∧δX , being symmetric and multiadditive on
tuples of continuous, psh-regularizable metrics, extends to a symmetric, multilinear operator
on continuous dpsh metrics, with values in signed Radon measure. Note that Proposition 8.3


## Literal published unit 03-1805.01016-literal-lines-3121-3215.txt

8.4. The non-Archimedean case. We assume in this section that K is non-Archimedean,
possibly trivially valued. By the change of metric formula (8.9), the Deligne pairing is
basically determined by its values on model metrics, which are described by the following
result.
Theorem 8.18. Let L0 , . . . , Ln be line bundles on a projective K-scheme X of dimension
n. Let L0 , . . . , Ln be models of L0 , . . . , Ln , determined on a projective model X of X, and
denote by φ0 , . . . , φn the corresponding model metrics. Then
                                         hφ0 , . . . , φn i = φhL0 ,...,Ln i .                        (8.15)
  Here hL0 , . . . , Ln i is the Deligne pairing with respect to the flat projective morphism X →
Spec K ◦ , cf. Appendix A. Since Deligne pairings commute with base change, hL0 , . . . , Ln i is
a model of hL0 , . . . , Ln i, and φhL0 ,...,Ln i denotes the corresponding model metric.
Proof. We argue by induction on n. Assume first n = 0, and hence X = Spec A with A finite
free over K ◦ . As recalled in Lemma A.19, any line bundle on X is trivial in a neighborhood
of the special fiber of X , and hence trivial on X . A trivializing section s ∈ H0 (L0 ) induces
a trivializing section hsi = NX /K ◦ (s) of hL0 i = NX /K ◦ (L0 ), as well as a trivializing section
s ∈ H0 (X, L0 ), such that |s|φ0 = 1 on X an . By (8.11), we infer
                                                Z
                                log |hsi|hφ0 i = log |s|φ0 δX = 0,

which is equivalent to hφ0 i = φhL0 i .
   Let now L0 , . . . , Ln be line bundle on a projective K-scheme X of dimension n, and
L0 , . . . , Ln be models of L0 , . . . , Ln determined on a projective model X of X. Since any
line bundle on X can be written as a difference of ample line bundles, we may assume that
L0 is ample, by linearity. After passing to a large enough multiple, we assume that there
exists a relatively regular section s ∈ H0 (L0 ), by Proposition A.15. Denote by Z its divisor,
with generic fiber Z. By the restriction property of Deligne pairings on models, s induces
an isomorphism
                                   hL0 , · · · , Ln i = hL1 |Z , . . . , Ln |Z i
of models of hL0 , . . . , Ln i = hL1 |Z , . . . , Ln |Z i. By induction, we get
                        φhL0 ,··· ,Ln i = φhL1 |Z ,...,Ln |Z i = hφ1 |Z , . . . , φn |Z i
                                           Z
                     = hφ0 , . . . , φn i + log |s|φ0 ddc φ1 ∧ . . . ∧ ddc φn ∧ δX ,
66                       SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

using the restriction property of Theorem 8.16. It remains to show that the right-hand
integral vanishes, which follows from the fact that ddc φ1 ∧ . . . ∧ ddc φn ∧ δX is supported on
Γ(X ) (cf. Example 8.11) together with Lemma 8.19 below.                                       
Lemma 8.19. If s is a relatively regular section of a line bundle L on a model X , then
|s|φL = 1 on Γ(X ).
Proof. Since s doesn’t vanish at the associated points of Xs , s is nonzero on the reduction
ξ := redX (x) of any Shilov point x ∈ X an defined by X . In other words, s defines a
trivializing section of L on an open neighborhood U of ξ, and we infer |s|φL ≡ 1 on U i , by
definition of the model metric φL .                                                        
   Using Theorem 8.18, we relate Deligne pairings and Gubler’s intersection theory on mod-
els [Gub98].
Definition 8.20. If D is a vertical Cartier divisor and L1 , . . . , Ln are line bundles on a
projective model X of X, we define their intersection number as the real number
                             (D · L1 · . . . · Ln ) := φhOX (D),L1 ,...,Lni .
   Here the right-hand side is a model function on Spec K, identified with its value on the
unique point of Spec K. Equivalently, (D · L1 . . . · Ln ) = vK (f ) for any choice of generator
f of the free K ◦ -module
                                       hO(D), L1 , . . . , Ln i ֒→ K.
In particular, (D · L1 . . . · Ln ) belongs to the (additive) value group ΓK ⊂ R.
   As a special case of Theorem 8.18, we have
                                            Z
                     (D · L1 . . . · Ln ) = φD ddc φL1 ∧ . . . ∧ ddc φLn ∧ δX .           (8.16)

On the other hand, in [Gub98, §3] Gubler associates to every vertical Cartier divisor D on
X an n-dimensional cycle cyc(D) with coefficients in ΓK on the finite type K̃-scheme Xs ,
such that the following holds:
     (i) if µ : X ′ → X is a morphism of projective models, then cyc(D) = µ⋆ cyc(µ⋆ D);
    (ii) if F/K is a non-Archimedean extension and DF is the pull-back of D to the base
         change of X to F ◦ , then cyc(DF ) = cyc(D)Fe ;
   (iii) if Xs is reduced, every irreducible component Y of Xs determines a unique Shilov
         point xY ∈ Γ(X ), and
                                             X
                                   cyc(D) =      φD (xY )[Y ].
                                                  Y
Corollary 8.21. Let L1 , . . . , Ln be line bundles on a model X of X, and D be a vertical
Cartier divisor on X . Then
                      (D · L1 · . . . · Ln ) = (cyc(D) · L1 |Xs · . . . · Ln |Xs ) .
Proof. By (8.16), (D · L1 · . . . · Ln ) is invariant under ground field extension, and we may
thus assume that K is algebraically closed and nontrivially valued. By multilinearity, we
may further assume that X is (geometrically) reduced. After replacing X with a higher
model, we can arrange for Xs to be reduced, by Theorem 4.20. By (8.3), we then have
                                                Z
                       (D · L1 · . . . · Ln ) = φD ddc φ1 ∧ · · · ∧ ddc φn
                  NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                                    67
                    X
                =       φD (xY ) (L1 |Y · . . . · Ln |Y ) = (cyc(D) · L1 |Xs · . . . · Ln |Xs ) .
                    Y
                                                                                                        

8.5. General metrics on the norm functor. We extend the previous discussion on met-
rics on Deligne pairings to the setting of general finite flat morphisms f : Y → X. In this
setting, we will write abreviate N = NX/Y when there is no risk for ambiguity.
   The formula (8.11) provides a general definition of a metric N (φ) on N (L), provided we
are given a metric φ on L. Namely, for x ∈ X an , and a section s of H 0 (L|f −1 (U ) ) for some
open neighborhood U of X such that U an is an open neighborhood of x, we define
                                                   Z
                            log |N (s)|N (φ) (x) =   log |s|φ δ[f −1 (x)] .                (8.17)
                                                           X

Here [f −1 (x)] denotes the fundamental cycle of f −1 (x), defined in a way analogous to Ex-
ample 8.2. The definition extends in a natural way to Q-line bundles.


## Literal published unit 03-1805.01016-literal-lines-3540-3584.txt

9.3. Monge–Ampère energy. In this section, X is geometrically reduced, and L is a
semiample Q-line bundle on X. Since L is in particular nef, we have
                                          V := vol(L) = (Ln ),
by Corollary 9.10.
Definition 9.13. Let φ, ψ be continuous psh metrics on L. We define the relative Monge–
Ampère energy7of φ, ψ as
                                   n Z
                              1 X
                 E(φ, ψ) :=            (φ − ψ)(ddc φ)j ∧ (ddc ψ)n−j ∧ δX .        (9.11)
                            n+1
                                         j=0

   Recall that φ − ψ is a continuous function on X an , which may thus be integrated against
each positive Radon measure (ddc φ)j ∧ (ddc ψ)n−j ∧ δX . By (8.9), we have
                                          1                       
                             E(φ, ψ) =          hφn+1 i − hψ n+1 i .                  (9.12)
                                        n+1
Given a continuous psh metric ψ, the functional φ 7→ E(φ, ψ) is characterized as the unique
antiderivative of the Monge–Ampère operator φ 7→ (ddc φ)n that vanishes at ψ, in the sense
that                                                Z
                      d                     ′
                             E((1 − t)φ + tφ , ψ) =        (φ′ − φ)(ddc φ)n           (9.13)
                      dt t=0                          X an
for any two continuous psh metrics φ, φ′ , see [BJ18a, §3.8].
Proposition 9.14. The Monge–Ampère energy satisfies the following properties.
    (i) cocycle formula: E(φ1 , φ2 ) + E(φ2 , φ3 ) + E(φ3 , φ1 ) = 0;
   (ii) monotonicity: φ ≤ φ′ =⇒ E(φ, ψ) ≤ E(φ′ , ψ);
  (iii) scaling: E(φ + c, ψ) = E(φ, ψ) + V c for c ∈ R;
  (iv) homogeneity: E(aφ, aψ) = an+1 E(φ, ψ) for a ∈ Z>0 .
   (v) Lipschitz continuity:
                                                                             
                    E(φ, ψ) − E(φ′ , ψ ′ ) ≤ V sup |φ − φ′ | + sup |ψ − ψ ′ | .
     (vi) for each complete field extension F/K we have
                                         E(φF , ψF ) = E(φ, ψ).
     7Note that the present normalization, which is more convenient for the purpose of this paper, is not
uniform accross the literature.
                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                             75

  (vii) birational invariance: for any projective birational morphism µ : X ′ → X we have
                                    E(µ⋆ φ, µ⋆ ψ) = E(φ, ψ).
Proof. (i) follows from (9.13), and (ii)— (iv) follow directly from (9.11), using that
                           Z
                             (ddc φ)j ∧ (ddc ψ)n−j ∧ δX = (Ln ) = V.

(v) is a formal consequence of (ii) and (ii), and (vi) follows from (9.11) and the compatibility


## Literal published unit 03-1805.01016-literal-lines-3587-3603.txt

9.4. Proof of Theorem A. The following result corresponds to Theorem A in the intro-
duction. It was first established in [BB10] when K is Archimedean, and in [BG+16] when
K is discretely valued.
Theorem 9.15. Let X be a geometrically reduced projective K-scheme, and L be a semi-
ample Q-line bundle on X. For any two continuous psh metrics φ, ψ on L, we then have
                                    vol(L, φ, ψ) = E(φ, ψ).
Corollary 9.16. Let φ, ψ be arbitrary continuous metrics on L. Let ν : X̃ → X be the
normalization morphism, and assume that Conjecture 7.30 holds. Then
                              vol(L, φ, ψ) = E (P(ν ⋆ φ), P(ν ⋆ ψ)) .
Proof. By Proposition 9.11, vol(L, φ, ψ) = vol(ν ⋆ φ, ν ⋆ ψ) = vol (P(ν ⋆ φ), P(ν ⋆ ψ)). Since X̃
is normal, Conjecture 7.30 implies that P(ν ⋆ φ) and P(ν ⋆ ψ) are continuous and psh, and
Theorem 9.15 yields the result.
                                                                                               
Lemma 9.17. Assume that K is non-Archimedean, and let L, M be models of L, with
associated model metrics φL , φM and graded norms k · kH0 (•L) , k · kH0 (•M) (cf. Example 9.3).
Then
                                           n!                                  


## Literal published unit 03-1805.01016-literal-lines-3848-3876.txt

is achieved at P for some, hence any, generator ω ∈ det H0 (L).
  In terms of the Vandermonde function Vφ,k·k relative to any given norm k · k on H0 (L),
P ∈ (X N )an is a Fekete configuration iff
                                        sup Vφ,k·k = Vφ,k·k (P ).
                                       (X N )an

Our final result is an equidistribution result for Fekete configurations of mφ as m → ∞,
first established in the Archimedean case in [BBW11]. In order to cover various cases in one
stroke, we introduce the following terminology.
Definition 10.9. Let L be a semiample line bundle, and φ be a continuous metric on L.
For brevity, we shall say that differentiability holds at φ if:
    (i) the psh envelope P(φ) is continuous (hence psh);
   (ii) for all f ∈ C0 (X an ) we have
                                                  Z
                        d
                               vol(L, φ + tf, φ) = f (ddc P(φ))n ∧ δX .        (10.5)
                        dt t=0
  Differentiability is known to hold at all continuous metrics when X is smooth, L is ample,
and one of the following conditions is satisfied:
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                           81

       • K is Archimedean [BB10];
       • K is non-Archimedean, trivially or discretely valued, of residue characteristic zero [BFJ16,
         BJ18a];
       • K is discretely valued of characteristic p, (X, L) is defined over a function field
         of transcendence degree d, and resolution of singularities is assumed in dimension
         n + d [GJKM19, BG+16].
Theorem 10.10. Let L be a big and semiample line bundle, of volume V := vol(L) = (Ln ).
Let φ be a continuous metric on L, and assume that differentiability holds at φ. For each


# Exact public source metadata and application checks

{
  "local_source_id": "04-1801.08229",
  "supplied": {
    "arxiv_id": "1801.08229",
    "saved_version": "1801.08229v4",
    "title": "[1801.08229] Global pluripotential theory over a trivially valued field",
    "public_source": "https://arxiv.org/pdf/1801.08229v4",
    "abstract_url": "https://arxiv.org/abs/1801.08229",
    "actual_abstract_url": "https://arxiv.org/abs/1801.08229",
    "actual_pdf_url": "https://arxiv.org/pdf/1801.08229v4",
    "abstract_html": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.html",
    "abstract_sha256": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304",
    "pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
    "pdf_sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
    "pdf_bytes": 1627763,
    "literal_extract": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
    "extract_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
    "extract_bytes": 506945,
    "pdftotext_returncode": 0,
    "origin": "Publicly available primary mathematical source; no generated research payload."
  },
  "verified_pdf_sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
  "verified_extract_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
  "pdf_header_first_lines": [
    "                                           GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED",
    "                                                                   FIELD",
    "",
    "                                                                   SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON",
    "arXiv:1801.08229v4 [math.AG] 22 Mar 2022",
    "",
    "",
    "",
    "",
    "                                                  Dedicated to Ahmed Zeriahi for all his contributions to complex analysis and geometry",
    "",
    "",
    "                                                Abstract. We develop global pluripotential theory in the setting of Berkovich geometry",
    "                                                over a trivially valued field. Specifically, we define and study functions and measures of",
    "                                                finite energy and the non-Archimedean Monge–Ampère operator on any (possibly reducible)",
    "                                                projective variety. We also investigate the topology of the space of valuations of linear",
    "                                                growth, and the behavior of psh functions thereon.",
    "                                                   Nous développons une théorie du pluripotentiel global dans le contexte de la géométrie de",
    "                                                Berkovich sur un corps trivialement valué. Plus précisément, nous définissons et étudions",
    "                                                des fonctions et mesures d’énergie finie et un opérateur de Monge–Ampère non-archimédien",
    "                                                sur toute variéte projective (éventuellement réductible). Nous explorons également la topolo-",
    "                                                gie de l’espace des valuations à croissance linéaire, et le comportement des fonctions psh",
    "                                                sur celui-ci.",
    ""
  ],
  "regenerated_layout_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/04-1801.08229.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/04-1801.08229-pdf-layout.txt"
  ],
  "application_checks": [
    "Ground field in the main text is algebraically closed and trivially valued.",
    "For the partial theorem use smooth connected projective X, an ample honest line bundle L, canonical trivial reference, n>=1, and char(k)=p>0.",
    "Theorem 7.18 and Proposition 7.19 construct the genuine finite-energy operator in every dimension; Theorem A gives strong continuity/injectivity with dense image.",
    "Theorem 5.20 and 12.9 give unconditional positive-characteristic surjectivity only for n<=2; the resolution in the envelope proof is on a test configuration of dimension n+1<=3.",
    "Theorem 12.8 proves the equivalence of the envelope property, E1 completeness and surjectivity in this trivial-valuation setting only."
  ]
}

## Literal published unit 04-1801.08229-literal-lines-102-200.txt

Functions and measures of finite energy. Let k be an arbitrary algebraically closed
field, and X an irreducible1 projective variety over k, with function field k(X). In order to
describe more precisely our main results, recall first that the Berkovich analytification X an
of X with respect to the trivial valuation on k is a compactification of the space X val of
valuations v : k(X)× → R, trivial on k, endowed with the topology of pointwise convergence.
Points of X an can be understood as semivaluations v on X, i.e. valuations v ∈ Y val for some
subvariety Y ⊂ X. The set X div ⊂ X val of divisorial valuations, which are attached to
prime divisors over X, is dense in X an .
   For every v ∈ X an and every section s ∈ H0 (X, mL), m ∈ N, we can make sense of
v(s) ∈ [0, +∞] by trivializing L at the center of v. Setting |s|(v) := exp(−v(s)) defines a
continuous function |s| : X an → [0, 1], and the topology of X an is in fact defined by the set
of such functions. Building on these, we introduce the following classes of functions on X an :
      • Fubini–Study functions for L are continuous functions ϕ : X an → R of the form

                                     ϕ = m−1 max{log |si | + λi },
                                                   i

         where (si ) is a finite set in H0 (X, mL) without common zeroes and λi ∈ Q. This
         defines a subset H = H(L) of C0 (X) := C0 (X an , R), and we show that the map
         (X , L) 7→ ϕL alluded to above sets up a 1–1 correspondence between H(L) and the
         set of ample, integrally closed test configurations (X , L) for (X, L) (see §1.4 for the
         definition when X is not normal).
      • piecewise linear (PL) functions on X an are elements of the Q-linear subspace PL(X)
        of C0 (X) spanned by H = H(L); this subspace turns out to be independent of L,
        and is dense in C0 (X). In the present setting, PL functions play the role of smooth
        functions from the complex analytic case. It is proved in Appendix A that PL
        functions are induced by usual piecewise linear functions on dual complexes of snc
        test configurations, when X is smooth and char k = 0.
      • L-psh functions are usc functions ϕ : X an → R∪{−∞}, not identically −∞, that can
        be obtained as limits of decreasing nets in H(L). The set PSH = PSH(L) of L-psh
        functions is stable under addition of a real constant, finite maxima, decreasing limits,
        and is the smallest such class of functions that contains all functions of the form
        m−1 log |s|, s ∈ H0 (X, mL) \ {0}. It follows from Dini’s lemma that C0 (X) ∩ PSH
        is the closure of H in the topology of uniform convergence. We prove that the
        restriction of an L-psh function ϕ to X div is finite-valued, and determines ϕ. We
        endow the set PSH with the topology of pointwise convergence on X div .
In the main body of the text, we actually work with ω-psh functions, where ω ∈ N1 (X) is
any (real) ample (and sometimes even arbitrary) numerical class on X. However, here we
will stick to the above setting, for simplicity.
   As in [BHJ17], the Monge–Ampère energy E : H → R is defined on ϕ ∈ H as the normal-
ized intersection number (or height)
                                                        (L̄n+1 )
                                           E(ϕ) :=               ,
                                                       (n + 1)V

   1While the main body of the article deals with possibly reducible varieties, we assume here for simplicity
that X is irreducible.
4                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

where n = dim X, V = (Ln ), and (X̄ , L̄) → P1 is the canonical Gm -equivariant compactifi-
cation of the ample, integrally closed test configuration (X , L) → A1 that represents ϕ. The
above normalization ensures that E(ϕ + c) = E(ϕ) + c for c ∈ Q.
   Adapting to our setting the original approach of [CL06, Gub10], we also attach to ϕ its
Monge–Ampère measure MA(ϕ), a Radon probability measure on X an with finite support
in X div , defined using intersection numbers computed on X0 . We then have
                                                   ˆ
                          d
                                E((1 − t)ϕ + tψ) =       (ψ − ϕ) MA(ϕ)
                         dt t=0                     X an
for all ψ ∈ H, and this actually characterizes the measure MA(ϕ), since H spans the dense
subset PL(X) ⊂ C0 (X).
   This formula shows that E is increasing on H, and we canonically extend it by mono-
tonicity to a usc functional E : PSH → R ∪ {−∞}, continuous along decreasing nets. We
denote by
                                E 1 := {ϕ ∈ PSH | E(ϕ) > −∞}
the set of L-psh functions of finite energy. Thus ϕ ∈ E 1 iff ϕ : X an → R ∪ {−∞} is a
decreasing limit of functions ϕi ∈ H with E(ϕi ) bounded. Note that the complex analytic
analogue of E 1 has been well studied, see [GZ07, BBGZ13, BBE+16, Dar15, DDL18].
   The weak topology of E 1 is the subset topology from PSH (i.e. the topology of pointwise
convergence on X div ), and the strong topology is the coarsest refinement of the weak topology
that makes E : E 1 → R continuous. Decreasing nets in E 1 are strongly convergent, and H is
thus strongly dense in E 1 .
   As in [BBGZ13], we dually introduce an energy functional E∨ : M → [0, +∞] on the space
M of Radon probability measures µ on X an , by setting
                                          ˆ                        ˆ    
                   ∨
                  E (µ) := sup E(ϕ) − ϕ µ = sup E(ϕ) − ϕ µ ,
                            ϕ∈H                      ϕ∈E 1

where the right-hand equality follows from a simple approximation argument. Thus E∨ is
convex, and lsc with respect to the usual weak topology of M. The space
                               M1 := µ ∈ M | E∨ (µ) < ∞
                                      

of measures of finite energy has a weak topology inherited from M, and a strong topology,
defined as the coarsest refinement of the weak topology for which E∨ becomes continuous.
In contrast to E 1 , we prove that both M1 and its strong topology
                                                             ´     are independent of L.
   For any two ϕ, ϕ ∈ H, we further have E(ϕ) − E(ϕ ) ≥ (ϕ − ϕ0 ) MA(ϕ), a reflection
                      0                                 0

of the concavity of E. This precisely means that ϕ computes the supremum defining the
energy of MA(ϕ), which thus lies in M1 .
   The main contribution of the present article can be summarized as follows.
Theorem A. The Monge–Ampère operator MA : H → M1 admits a unique continuous
extension MA : E 1 → M1 , where both sides are equipped with the strong topology.
   It further induces a topological embedding with dense image E 1 /R ,→ M1 , which is onto
if X is smooth, and either char k = 0 or dim X ≤ 2.
  Theorem A can be viewed as a trivially valued analogue of the main result of [BBGZ13],


## Literal published unit 04-1801.08229-literal-lines-2808-2852.txt

establish it in an important special case. We first observe:
Lemma 5.9. Assume that θ ∈ N1 (X) can be written as the limit of classes θj ≥ θ that
satisfy the envelope property. Then θ has the envelope property as well.
58                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. Pick a bounded-above family (ϕi ) in PSH(θ). Since θ ≤ θj , we have PSH(θ) ⊂
PSH(θj ). Thus sup?i ϕi is θj -psh for all j, and hence θ-psh, by Theorem 4.5.    
Corollary 5.10. If the continuity property holds for all ω ∈ Amp(X), then it holds for all
θ ∈ Nef(X).
  We next prove that the envelope property is equivalent to the analogue of a basic com-
pactness property in the complex analytic case.
Theorem 5.11. For any θ ∈ N1 (X), the following properties are equivalent:
    (i) the envelope property holds for θ;
   (ii) the space PSHsup (θ) := {ϕ ∈ PSH(θ) | sup ϕ = 0} is compact;
  (iii) every bounded-above, increasing net (ϕj ) in PSH(θ) converges in PSH(θ).
Proof. Assume (i), and pick a net (ϕi ) in PSHsup (θ). By Proposition 4.38, (ϕi (v)) is a
bounded net in R for each v ∈ X div . By Tychonoff’s theorem, after passing to a subnet,
we may thus assume that (ϕi ) converges pointwise on X div to a function ϕ : X div → R,
and it suffices to show that ϕ extends to a function in PSH(θ) (necessarily unique, by
Corollary 4.23). By (i), ψi := sup?j≥i ϕj is θ-psh for each i. The net (ψi ) is further decreasing,
and its pointwise limit ψ := limi ψi is thus either θ-psh, or identically −∞, by Theorem 4.5.
Now Theorem 5.6 implies that ψi = supj≥i ϕj on X div . Thus ψ = ϕ on X div . In particular,
ψ 6≡ −∞, hence ψ ∈ PSH(θ). This proves (i)⇒(ii).
   Next, assume (ii), and consider a bounded-above, increasing net (ϕj ) in PSH(θ). Then a
subnet ϕji −sup ϕji converges to some ϕ ∈ PSH(θ). Since (sup ϕj ) is increasing and bounded-
above, it converges to some c ∈ R. Thus ϕji → ϕ + c on X div , and hence ϕj → ϕ + c on
X div since (ϕj ) is increasing. This proves (ii)⇒(iii).
   Finally, assume (iii). Let (ϕi )i∈I be a bounded-above family of θ-psh functions, and
consider the increasing net ψJ := maxi∈J ϕi parametrized by finite subsets J ⊂ I. Then ψJ
admits a limit ψ in PSH(θ), and we claim that ψ = sup?i ϕi . On X div we have
                              ψ = lim max ϕi = supi ϕi = sup?i ϕi ,
                                    J   i∈J
by Theorem 5.6. Since ψ is θ-psh and sup?i ϕi is usc, Theorem 4.22 yields ψ ≤ sup?i ϕi on
X an . Similarly, Theorem 4.22 yields ϕi ≤ ψ, and hence sup?i ϕi ≤ ψ, since ψ is usc. This
proves the claim, and hence (iii)⇒(i).                                                  
   Recall that the variety X is said to be unibranch if the following equivalent conditions
hold (see [EGA, IV.7.6.3] and [Kol16, Corollary 32]):
      • the normalization morphism ν : X ν → X is a homeomorphism;
      • the formal completion of X at each of its points is irreducible.
In particular, any normal variety is unibranch. When k = C, X is unibranch iff the associated
complex analytic space is locally irreducible in the analytic topology. This is also true for
the Berkovich analytification as considered in this paper: the variety X is unibranch iff
the k-analytic space X an is locally irreducible in the analytic topology (see [Duc09, Lemme
5.19]).
Theorem 5.12. If the envelope property holds for some ω ∈ Amp(X), then X is necessarily


## Literal published unit 04-1801.08229-literal-lines-2894-2916.txt

5.3. Envelopes. For ample classes, the envelope property admits a useful reformulation.
We continue to assume that X is irreducible unless stated otherwise. Fix a class ω ∈
Amp(X).
Definition 5.16. The ω-psh envelope of a function ϕ : X an → R ∪ {±∞} is the function
Pω (ϕ) : X an → R ∪ {±∞} defined as the pointwise supremum
                           Pω (ϕ) := sup {ψ ∈ PSH(ω) | ψ ≤ ϕ} .
  Thus Pω (ϕ) ≡ −∞ iff there is no ψ ∈ PSH(ω) with ψ ≤ ϕ. Despite the name, Pω (ϕ) is
not always ω-psh (and indeed not even usc in general). However, it is clear that
     • ϕ 7→ Pω (ϕ) is increasing;
     • Pω (ϕ + c) = Pω (ϕ) + c for all c ∈ R.
60                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

These properties formally imply the Lipschitz estimate
                               sup Pω (ϕ) − Pω (ϕ0 ) ≤ sup |ϕ − ϕ0 |.                     (5.1)
when ϕ, ϕ0 are bounded.
Lemma 5.17. For any ω ∈ Amp(X), the following statements are equivalent:
   (i) ω has the envelope property;
  (ii) for any function ϕ : X an → R ∪ {±∞}, we have
                      Pω (ϕ) ≡ −∞, Pω (ϕ)? ≡ +∞, or Pω (ϕ)? ∈ PSH(ω).
     (iii) for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.
     We refer to the property in (iii) as continuity of envelopes.
Proof. First assume (i). Pick any ϕ : X an → R ∪ {±∞}, and suppose that the set F :=
{ψ ∈ PSH(θ) | ψ ≤ ϕ} is nonempty, so that Pω (ϕ) 6≡ −∞. If the functions in F are uniformly


## Literal published unit 04-1801.08229-literal-lines-2977-3068.txt

5.4. The envelope property on smooth varieties. The results earlier in this section
would not be particularly useful unless we have examples of classes where the envelope
property holds. Arguing along the lines of [BFJ16, Theorem 8.5], we will prove:
Theorem 5.20. Assume that X is smooth and connected, and that either char k = 0 or
dim X ≤ 2. Then any θ ∈ Nef(X) has the envelope property.
  We do not know whether a class θ ∈ N1 (X) that is not nef has the envelope property.
Corollary 5.21. Under the assumptions of Theorem 5.20, the set
                           PSHsup (θ) = {ϕ ∈ PSH(θ) | sup ϕ = 0}
is compact.
  In [BFJ16], the above compactness property was established in the discretely valued
case, by relying on much more involved arguments based on dual complexes and toroidal
modifications.
62                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Lemma 5.22. Let L be an ample line bundle on X, and (X , L) a test configuration for
(X, L), with L an honest line bundle. Denote by am ⊂ OX the base ideal of mL, which is a
vertical ideal of X for all m  1. Then
                       PL (ϕL ) − ϕL = sup m−1 ϕam = lim m−1 ϕam
                                       m≥1             m→∞

pointwise on X an . Furthermore, PL (ϕL ) is continuous iff m−1 ϕam converges uniformly on
X an .
  As with flag ideals, see §2.1, the function ϕam ∈ PL(X) is defined by ϕam (v) = −σ(v)(am ),
where σ = σX denotes Gauss extension (see Remark 1.9).
Proof. Set ϕm := ϕL + m−1 ϕam . Note first that (am )m is a graded sequence of ideals, i.e.
am · am0 ⊂ am+m0 for all m, m0 ∈ N. The sequence m 7→ ϕam is thus superadditive, and
Fekete’s lemma yields supm≥1 m−1 ϕam = limm→∞ m−1 ϕam .
  Next write L = LX + D with a vertical Cartier divisor D on X , so that ϕL = ϕD . For
each m, denote by µm : Xm → X the integral closure of the blowup along am , and by Dm the
(antieffective) divisor on Xm such that OXm · am = OXm (Dm ); thus ϕm = ϕD + m−1 ϕDm .
By construction, OX (mL) ⊗ am is globally generated. This implies that
                         µ? (mL) + Dm = mLXm + µ? (mD) + Dm
is nef, and hence ϕm ∈ PL ∩ PSH(L). Furthermore, ϕDm ≤ 0, so ϕm ≤ ϕL , and hence
ϕm ≤ PL (ϕL ), which proves
                               sup ϕm = lim ϕm ≤ PL (ϕL ).
                               m≥1       m→∞

Conversely, Lemma 5.19 implies
                      PL (ϕL ) = QL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } .
Pick ψ ∈ H(L) with ψ ≤ ϕL . After replacing X with a higher test configuration, we may
and do assume, for the sake of notational simplicity, that ψ is determined by a vertical
Q-Cartier divisor E on X . For m large and divisible enough, Theorem 2.31 shows that
mLX + mE = mL + m(E − D) is globally generated, and hence OX (m(E − D)) ⊂ am . This
yields
                             m(ψ − ϕL ) = ϕm(E−D) ≤ ϕam ,
and hence ψ ≤ ϕm , which yields, as desired, the converse inequality
                      PL (ϕL ) = sup {ψ ∈ H(L) | ψ ≤ ϕL } ≤ sup ϕm .
                                                               m
The final assertion is a simple consequence of Dini’s lemma, using the superadditivity of
m 7→ mϕm .                                                                             
Proof of Theorem 5.20. By Lemma 5.9, we may assume that θ = c1 (L) with L ∈ Pic(X)Q
ample. Pick ϕ ∈ C0 (X). By Lemma 5.17, we need to show that PL (ϕ) is continuous. Since
PL(X) is dense in C0 (X) with respect to uniform convergence (see Theorem 2.2), we may
assume ϕ ∈ PL(X), by (5.1). By Theorem 2.31, we have ϕ = ϕL for a test configuration
(X , L) for (X, L). After replacing L with a multiple, we may further assume that L and L
are honest line bundle.
   Using the notation of Lemma 5.22, we need to show that ϕm := ϕL + m−1 ϕam converges
uniformly to PL (ϕL ). Since we assume that char k = 0 or dim X ≤ 2 (and hence dim X ≤ 3),
we can rely on resolution of singularities and assume that X is smooth and X0 has simple
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                         63

normal crossings support. We may also assume that there exists an effective vertical Q-
divisor E on X such that A := L − E is ample.
   Assume first that char k = 0, and let bm be the multiplier ideal of the graded sequence am
                                                                                            • .
                                                            l
The inclusion am ⊂ bm is elementary, and we have bml ⊂ bm for all m, l by the subadditivity
of multiplier ideals. This implies that
                      m−1 ϕbm ≥ (ml)−1 ϕbml ≥ (ml)−1 ϕaml ≥ m−1 ϕam
for all sufficiently divisible m and l. Letting l → ∞ shows that
                                ϕL + m−1 ϕbm ≥ PL (ϕL ) ≥ ϕm                                (5.2)
for all sufficiently divisible m. By the uniform global generation of multiplier ideals there
exists m0 ∈ N such that

               OX (mL + m0 A) ⊗ bm = OX ((m + m0 )L) ⊗ OX (−m0 E) ⊗ bm
  is globally generated for all sufficiently divisible m. This implies that
                                      ϕbm ≤ ϕam+m0 + C
for a constant C independent of m. Combining this with (5.2) yields

                                            m0            m0        C
                       ϕm ≤ PL (ϕL ) ≤ (1 +    )ϕm+m0 −       ϕL + ,
                                            m              m        m
for all sufficiently divisible m. This shows that PL (ϕL ) is a uniform limit of continuous
functions, and hence continuous.
   When char k > 0, the very same argument applies with test ideals in place of multiplier
ideals, see [GJKM17] for details.                                                        
Remark 5.23. In view of Remark 5.15, Theorem 5.20 is valid also when X is smooth but
possibly disconnected. A suitable version of Corollary 5.21 is also true.

                       6. Homogeneous functions and b-divisors
   In this section, we assume for simplicity that X is irreducible. We study homogeneous
θ-psh functions and their relation to nef b-divisors. Inspired by the work of Ross and Witt


## Literal published unit 04-1801.08229-literal-lines-3649-3700.txt

       7. Functions of finite energy and mixed Monge–Ampère measures
   In this section, X denotes a projective variety of dimension n, with irreducible components
Xα . We extend the energy pairing to arbitrary psh functions, and use this to define functions
of finite energy, and the mixed Monge–Ampère operator thereon.
7.1. Extending the energy pairing. In §3.2, the energy pairing
                                  (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ∈ R
was defined for pairs (θi , ϕi ) ∈ N1 (X) × PLR . When the ϕi are θi -psh, this is an increasing
function of the ϕi , by Lemma 3.15. On the other hand, any ω-psh function with ω ∈
Amp(X) can be written as a decreasing limit of functions in Hdom (ω) ⊂ PL ∩ PSH(ω) (see
Theorem 4.15). This allows to extend the energy pairing by monotonicity, as follows.
                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                                       75

Theorem 7.1. For each (n + 1)-tuple ω0 , . . . , ωn ∈ Amp(X), the energy pairing
                           (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )
admits a unique extension to a map ni=0 PSH(ωi ) → R ∪ {−∞} that is
                                          Q

     • upper semicontinuous;
     • increasing in each variable.
Furthermore, this map is continuous along decreasing nets, and satisfies
                  (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =             inf             (ω0 , ψ0 ) · . . . · (ωn , ψn )              (7.1)
                                                       ψi ∈Hdom (ωi ), ψi ≥ϕi
                  Q
for all (ϕi ) ∈       i PSH(ωi ).

Proof. Any map that is both usc and increasing is automatically continuous along decreasing
nets. Since all functions in PSH(ωi ) are limits of decreasing nets in Hdom (ωi ) ⊂ PL(X) ∩
PSH(ωi ), uniqueness is clear. To prove existence, it suffices to show that (7.1) has the
required properties.
  Monotonicity is obvious. To prove upper semicontinuity, suppose that ϕi ∈ PSH(ωi ),
0 ≤ i ≤ n, and t ∈ R satisfy
                                (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) < t,
By definition, we can choose ψi ∈ Hdom (ωi ) and 0 < ε  1 such that ϕi ≤ ψi and
                                        (ω0 , ψ0 ) · . . . · (ωn , ψn ) < t − ε.
Set                                          X
                                     C :=     (ω0 · . . . · ωbi · . . . · ωn ) > 0.
                                               i
By Proposition 4.28, ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi ), and we can thus find an
open neighborhood Ui of ϕi in PSH(ωi ) such that ϕ0i ≤ ψi + εC −1 for all ϕ0i ∈ Ui . By
monotonicity of the energy pairing and Proposition 3.14, this gives
                   (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n ) ≤ (ω0 , ψ0 + εC −1 ) · . . . · (ωn , ψn + εC −1 )
                                = (ω0 , ψ0 ) · . . . · (ωn , ψn ) + ε < t
         0
for all ϕi ∈ Ui , which proves upper semicontinuity.                                                                             
Proposition 7.2. The energy pairing (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is symmetric and R>0 -linear
with respect to each variable (ωi , ϕi ) with ωi ∈ Amp(X) and ϕi ∈ PSH(ωi ). Furthermore,

                                                                                    n
                                                                                    X
 (ω0 , ϕ0 + c0 ) · . . . · (ωn , ϕn + cn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) +            ci (ω0 · . . . · ωbi · . . . · ωn )X (7.2)
                                                                                    i=0
for all ci ∈ R,


## Literal published unit 04-1801.08229-literal-lines-3789-3850.txt

7.2. Functions of finite energy.
Definition 7.6. For each ω ∈ Amp(X), we define the Monge–Ampère energy functional
                                            Eω : PSH(ω) → R ∪ {−∞}
by setting, for ϕ ∈ PSH(ω),
                                             (ω, ϕ)n+1
                                               Eω (ϕ) :=  .                                                            (7.9)
                                            (n + 1)(ω n )
We say that ϕ has finite energy if Eω (ϕ) > −∞.
  We denote by
                                       E 1 (ω) ⊂ PSH(ω)
the set of ω-psh functions of finite energy.
78                                SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proposition 7.7. For each ω ∈ Amp(X), the functional Eω : PSH(ω) → R∪{−∞} satisfies:
    (i) Eω is increasing, concave, usc, and continuous along decreasing nets;
   (ii) Eω (ϕ + c) = Eω (ϕ) + c for ϕ ∈ PSH(ω) and c ∈ R;
  (iii) for each ϕ ∈ PSH(ω) and t ∈ R>0 we have Eω (t·ϕ) = t Eω (ϕ) and Etω (tϕ) = t Eω (ϕ);
  (iv) for each ϕ ∈ PSH(ω) we have
                                   X
                          Eω (ϕ) =    cα Eω|Xα (ϕ|Xαan ) = Eν ? ω (ν ? ϕ)             (7.10)
                                                       α
           with cα    := (ω n )   Xα   /(ω n )   X and ν : X
                                                               ν → X the normalization morphism.
                                                                      P
     Note that cα > 0 iff Xα is top-dimensional, and                      α cα = 1.

Proof. Concavity follows from Theorem 3.25, by monotone approximation. The rest of (i)–
(ii) and the first half of (iii) are consequences of Proposition 7.2. Pick ϕ ∈ PSH(ω). For any
t ∈ R>0 , tϕ ∈ PSH(tω) satisfies
                                              (tω, tϕ)n+1        (ω, ϕ)n+1
                           Etω (tϕ) =                       = t               = t Eω (ϕ),
                                            (n + 1)((tω)n )     (n + 1)(ω n )
which concludes the proof of (iii). Finally, (iv) is a consequence of (7.4).                       
Theorem 7.8. Given ample classes ω, ω 0 , ω0 , . . . , ωn ∈ Amp(X), we have:
    (i) E 1 (ω) is a convex subset of PSH(ω), and contains all bounded ω-psh functions;
   (ii) E 1 (ω) is stable under addition of a constant and the scaling action of R>0 ;
  (iii) if ϕ ∈ E 1 (ω), then any ψ ∈ PSH(ω) such that ψ ≥ ϕ is also in E 1 (ω);
  (iv) if ω ≤ ω 0 then E 1 (ω) ⊂ E 1 (ω 0 );
   (v) E 1 (tω) = t E 1 (ω) for all t ∈ R>0 , and
                                             E 1 (ω) + E 1 (ω 0 ) ⊂ E 1 (ω + ω 0 );
      (vi) if ϕi ∈ E 1 (ωi ), i = 0, . . . , n, then (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is finite;
     (vii) if ϕ ∈ PSH(ω) then
                    ϕ ∈ E 1 (ω) ⇐⇒ ν ? ϕ ∈ E 1 (ν ? ω)
                    ⇐⇒ ϕ|Xαan ∈ E 1 (ω|Xα ) for all top-dimensional components Xα .
Lemma 7.9. Pick ω, ω 0 ∈ Amp(X) and t ≥ 1 such that ω ≤ ω 0 ≤ tω. For all nonpositive
ϕ ∈ PSH(ω) ⊂ PSH(ω 0 ) we have
                                   0 ≥ (ω, ϕ)n+1 ≥ (ω 0 , ϕ)n+1 ≥ tn (ω, ϕ)n+1 .
Proof. By Proposition 7.3 we have
                      0 ≥ (ω, ϕ)n+1 ≥ (ω 0 , ϕ)n+1 ≥ (tω, ϕ)n+1 = tn+1 (ω, t−1 ϕ)n+1 .
Since ϕ ∈ PSH(ω) and t−1 ∈ [0, 1], concavity of the energy yields (ω, t−1 ϕ)n+1 ≥ t−1 (ω, ϕ)n+1 ,
and the result follows.                                                                      
Lemma 7.10. Pick r ≥ 1, ω0 , . . . , ωr ∈ Amp(X), 0 ≥ ϕi ∈ PSH(ωi ) for i = 0, . . . , r.
Assume also given t ≥ 1 such that ωi ≤ tωj for all i, j. Then
                                      !n+1
                         X       X                     X
                            ωi ,   ϕi      ≥ Cr,n trn     (ωi , ϕi )n+1        (7.11)
                                        i          i                        i
with Cr,n     := (2r r!)n .
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                               79

                                            t
Proof. Assume first r = 1. Set ω̃ := 1+t      (ω0 + ω1 ), and observe that ω0 ≤ ω̃ ≤ tω0 and


## Literal published unit 04-1801.08229-literal-lines-3916-4080.txt

Theorem 7.14. There exists a unique multilinear symmetric pairing
                     n+1
         N1 (X) × E~1      3 ((θ0 , ϕ0 ), . . . , (θn , ϕn )) 7→ (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ∈ R

that is compatible with the one defined in Theorem 7.1 for tuples (θi , ϕi ) ∈ N1 (X) × E~1 such
that θi ∈ Amp(X) and ϕi ∈ E 1 (θi ) = E~1 ∩ PSH(θi ). Furthermore:
     (i) this pairing is compatible with the one defined in §3.2 for tuples in N1 (X) × PL(X)R ;
    (ii) (7.3), (7.4) and (7.5) remain valid on N1 (X) × E~1 ;
   (iii) for any ω ∈ Amp(X) and θ0 , . . . , θn ∈ N1 (X), the map
                                 (ϕ0 , . . . , ϕn ) 7→ (θ0 , ϕ0 ) · . . . · (θn , ϕn )
          is continuous along decreasing nets in E 1 (ω).
Proof. Consider the vector space V := N1 (X) × E~1 . By Theorem 7.8 (v),
                                       [
                               C :=          {ω} × E 1 (ω).
                                               ω∈Amp(X)

is a convex cone in V , and the energy pairing is an R>0 -multilinear pairing on C, by Propo-
sition 7.2. Since Amp(X) spans N1 (X), it is straightforward to see, using Theorem 7.8 (iv),
that C spans V . It is now a simple general fact that the pairing on C uniquely extends to
an R-multilinear pairing on V .
   The first compatibility assertion follows from Lemma 7.13. The pairing on C restricts to
the one from §3.2 on the subcone
                                   [
                          C 0 :=          {ω} × (PL(X)R ∩ PSH(ω)),
                                     ω∈Amp(X)

which spans V 0 := N1 (X) × PL(X)R ; the extended pairing on V thus coincides with the
given one on V 0 , which proves (i). Next, (ii) is immediate by multilinearity. Finally (iii)
holds when θi ≥ ω, by Theorem 7.1; the general case follows, again by multilinearity.                         
     By multilinearity, (7.3), (7.4) and (7.5) remain valid on N1 (X) × E~1 . We also note:
Lemma 7.15. If θ0 , . . . , θn ∈ Nef(X), then (θ0 , ϕ0 ) · . . . · (θn , ϕn ) is an increasing function
of ϕi ∈ PSH(θi ) ∩ E~1 .
Proof. It suffices to write (θ0 , ϕ0 ) · . . . · (θn , ϕn ) = limε→0 (θ0 + εθ, ϕ0 ) · . . . · (θn + εθ, ϕn ) with
θ ∈ Amp(X).                                                                                                    
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                              81

Remark 7.16. Mimicking the complex analytic case, one can define E 1 (θ) for any θ ∈
Nef(X) as the set of ϕ ∈ PSH(θ) such that inf j (θ, ϕj )n+1 > −∞ with ϕj := max{ϕ, −j} ∈
E ∞ (θ). The proof of Lemma 7.13 still yields E~1 ∩ PSH(θ) ⊂ E 1 (θ), but the inclusion is strict
in general when θ is not ample (compare [DiN16]).
7.3. Mixed Monge–Ampère measures. Recall that a Radon measure µ on the compact
space X an is a regular (positive) Borel measure on X an . By the Riesz representation theorem,
Radon measures are in 1–1 correspondence with positive linear forms on C0 (X), see for
instance [Fol99, §7.1–2]. Any usc function f : X an → R ∪ {−∞} satisfies
                                   f = inf g ∈ C0 (X), g ≥ f
                                          

pointwise, and
                     ˆ                   ˆ                                
                                                            0
                          f µ = inf            g µ | g ∈ C (X), g ≥ f          ∈ R ∪ {−∞}.        (7.13)

   We will sometimes need to rely on the following monotone convergence theorem for (pos-
sibly uncountable) nets of usc functions, a simple consequence of (7.13) and Dini’s lemma
(see for instance [Fol99, Proposition 7.12]).
Lemma 7.17. If µ is a Radon measure on X an and (fj )j a decreasing
                                                             ´      ´net of usc functions
    an
on X , converging pointwise to a (usc) function f , then limj fj µ = f µ.
  More generally, continuous linear forms in C0 (X)∨ correspond to signed Radon mea-
sures on X an . Any such measure can be written as a difference of Radon measures, and
Lemma 7.17 thus applies as well when µ is a signed measure.
  With these preliminaries in hand, we now generalize the construction of mixed Monge–
Ampère measures, introduced in §3.2 in the PL case.
Theorem 7.18. For each n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , i = 1, . . . , n, there exists a unique
signed measure
                                                      ^
             (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ) = (θi + ddc ϕi ) ∈ C0 (X)∨              (7.14)
                                                                    i
such that             ˆ             ^
                                ϕ    (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )    (7.15)
                         X an        i
for all ϕ ∈ PL(X)R . If further θi ∈ Nef(X) and ϕi ∈ PSH(θi ) for i = 1, . . . , n, then (7.14)
is a positive measure.
  While the notation mimics the one for mixed Monge–Ampère measures in the complex
analytic case, we will not define the individual factors θi + ddc ϕi . At least if the ϕi are
continuous, this could, however, be done using the approach in [CLD12] (cf. Remark 7.23
below).
Proof. By density of PL(X) in C0 (X) (see Theorem 2.2), the prescription (7.15) uniquely
determines the measure (7.14). To show existence, we may assume, by multilinearity, that
θi ∈ Nef(X) and ϕi ∈ E~1 ∩ PSH(θi ) for i = 1, . . . , n. Since any ϕ ∈ PL(X)R can be written
as a difference of functions in PLR ∩ PSH(ω) for some ω ∈ Amp(X) (see (3.2)), Lemma 7.15
shows that ϕ 7→ (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ) is a positive linear form on PL(X)R . By density
of PL(X)R in C0 (X), it thus uniquely extends to a positive linear form on C0 (X), and we
are done.                                                                                              
82                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proposition 7.19. Mixed Monge–Ampère measures satisfy the following properties:
   (i) the signed measure i (θi + ddc ϕi ) is a symmetric and multilinear function of the
                              V

       n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , of total mass
                             ˆ     ^
                                     (θi + ddc ϕi ) = (θ1 · . . . · θn )X ;
                                       X an i

     (ii) assume (θi , ϕi ) ∈ N1 (X) × PLR , and pick an integrally closed test configuration X
          dominating Xtriv and Di ∈ VCar(X )R such that ϕi = ϕDi ; then
                                   ^                   X
                                      (θi + ddc ϕi ) =   cE δvE ,
                                           i                          E

          where E ranges over the irreducible components of X0 and
                         cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E ;
     (iii) for all (θi , ϕi ) ∈ N1 (X) × E~1 and t ∈ R>0 we have
                                 ^                           ^
                                    (θi + ddc (t · ϕi )) = t? (θi + ddc ϕi ),                    (7.16)
                                   i                                   i
                        ^                              X        ^
                             (θi + ddc ϕi ) =                          θi |Xα + ddc ϕi |Xαan ,
                                                                                            
                                                                                                 (7.17)
                         i                          dim Xα =n i
                              ^                              ^
                                       (θi + ddc ϕi ) = ν?          (ν ? θi + ddc ν ? ϕi ) ,     (7.18)
                               i                                i
          with ν : X ν → X the normalization;
     (iv) for any ω ∈ Amp(X), the map E 1 (ω)n 3 (ϕ1 , . . . , ϕn ) 7→ i (θi +ddc ϕi ) is continuous
                                                                      V
          along decreasing nets;
      (v) for all (θi , ϕi ) ∈ N1 (X) × E~1 and ϕ ∈ E~1 , ϕ is integrable against i (θi + ddc ϕi ),
                                                                                   V
          and (7.15) holds.
  When ϕi = 0 for some i, we drop the term ddc ϕi from the notation. As a special case of
Proposition 7.19 (ii), we then have
                                          X
                        θ1 ∧ · · · ∧ θn =   (θ1 · . . . · θn )Xα δvtriv,α .        (7.19)
                                                    dim Xα =n

Proof of Proposition 7.19. Points (i) and (iii) follow from Proposition 7.2, while (ii) is a
reformulation of (3.5). By density of PL(X) in C0 (X), (iv) is equivalent to the fact that,
for each ϕ ∈ PL(X),
                                 ˆ  ^
            (ϕ1 , . . . , ϕn ) 7→ ϕ   (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )
                                                i

is continuous along decreasing nets in E 1 (ω)n+1 . Now ϕ can be written as a difference of
functions in PL ∩ PSH(ω 0 ) for some ω 0 ∈ Amp(X), and the desired continuity is thus a
consequence of Theorem 7.14. To prove (v), we may assume θi ∈ Amp(X) and ϕi ∈ E 1 (θi ),
by multilinearity. Any ϕ ∈ E 1 (ω) with ω ∈ Amp(X) can be written as the pointwise limit
of a decreasing net in PL ∩ PSH(ω), and (7.15) thus holds for ϕ, by monotone convergence
and the continuity of the energy pairing along decreasing limits.                        
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                 83

Example 7.20. Assume X is a smooth curve and pick ω ∈ Amp(X). By Example 4.13,
any ϕ ∈ PSH(ω) determines a positive Radon measure (deg ω)δvtriv + ∆ϕ, with
              X d                                                     d2
                                                                                     
                                             d
        ∆ϕ =              ϕ(t ordp )δvtriv −       ϕ(t ordp )δvp,triv + 2 ϕ(t ordp )
                    dt 0+                    dt +∞                     dt
                 p∈X(k)

the tree Laplacian (see [FJ04, §7]). As we saw in Example 3.19, we have ω + ddc ϕ =
(deg ω)δvtriv + ∆ϕ for any ϕ ∈ PLR ∩ PSH(ω), and this remains true for any ϕ ∈ E 1 (ω),
by monotone approximation. For such functions, ω + ddc ϕ further puts no mass on the
endpoints vp,triv , which means that the convex function t 7→ ϕ(t ordp ) has sublinear growth
(see respectively Corollary 7.49 and Theorem 11.11).
Proposition 7.21. Pick ωi ∈ Amp(X) and ϕi ∈ E 1 (ωi ), i = 1, . . . , n, and choose also
ω0 ∈ Amp(X) and ϕ0 ∈ PSH(ω0 ). Then:
    (i) ϕ0 is integrable with respect to µ := i (ωi + ddc ϕi ) iff (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) > −∞,
                                             V
        and this holds as soon as ϕi is bounded for i = 1, . . . , n;
   (ii) assume ϕ0 ∈ L1 (µ). Pick for i = 0, . . . ,Vn a decreasing net (ϕij )j in PSH(ωi ) that
        converges pointwise to ϕi , and set µj := i (ωi + ddc ϕij ). Then ϕ0j ∈ L1 (µj ) for all


## Literal published unit 04-1801.08229-literal-lines-4130-4202.txt

7.4. The Monge–Ampère operator and energy functionals. In this section we fix
ω ∈ Amp(X). We denote by V := (ω n ) its volume, and write E 1 := E 1 (ω) and E := Eω .
Definition 7.24. The Monge–Ampère operator takes ϕ ∈ E 1 to the Radon probability
measure
                      MA(ϕ) = MAω (ϕ) := V −1 (ω + ddc ϕ)n
on X an .
Definition 7.25. For any two ϕ, ψ ∈ E 1 we set
                                                                      ˆ
                         Jψ (ϕ) = Jω,ψ (ϕ) = E(ψ) − E(ϕ) +                (ϕ − ψ) MA(ψ)

and
                                                      ˆ
                           I(ϕ, ψ) = Iω (ϕ, ψ) =          (ϕ − ψ) (MA(ψ) − MA(ϕ))
                                                   = Jψ (ϕ) + Jϕ (ψ).

 Note that Jψ (ϕ) and I(ϕ, ψ) are both invariant under translation of ϕ, ψ by constants.
When ψ = 0 we simply write
                                      ˆ             ˆ
                     I(ϕ) := I(ϕ, 0) = ϕ MA(0) − ϕ MA(ϕ)

and                                                        ˆ
                                   J(ϕ) := J0 (ϕ) =            ϕ MA(0) − E(ϕ).

Example 7.26. By (7.19) with θ1 = · · · = θn = ω we have
                                           X
                            MA(0) =             cα δvtriv,α ,                                             (7.20)
                                                      dim Xα =n
                                                       ´
with cα = (ω n )Xα /(ω n ). As a consequence,
                                                        P                 P
                                             ϕ MA(0) = α cα ϕ(vtriv,α
                                                                   ´  ) =  α cα sup(ϕ|Xα ),
see (1.4). In particular, when X is irreducible, MA(0) = δvtriv and ϕ MA(0) = sup ϕ.
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      85

    Thanks to Theorem 7.8, we can make sense of the definitions from §3.3 for functions in
E 1 . In particular, we set, for any two ϕ, ψ ∈ E 1 ,
                        dω (ϕ, ψ) :=    max kϕ − ψk2(ω,ϕ)j ·(ω,ψ)n−1−j
                                       0≤j≤n−1

with
  kϕ − ψk2(ω,ϕ)j ·(ω,ψ)n−1−j = −(0, ϕ − ψ)2 · (ω, ϕ)j · (ω, ψ)n−j
                               ˆ
                           = − (ϕ − ψ) ddc (ϕ − ψ) ∧ (ω + ddc ϕ)j ∧ (ω + ddc ψ)n−j . (7.21)

Proposition 7.27. For all ϕ, ψ ∈ E 1 we have:
                            n       ˆ
                       1 X −1
     E(ϕ) − E(ψ) =             V      (ϕ − ψ) (ω + ddc ϕ)j ∧ (ω + ddc ψ)n−j ;          (7.22)
                    n+1
                           j=0
                ˆ                                   ˆ
                  (ϕ − ψ) MA(ϕ) ≤ E(ϕ) − E(ψ) ≤ (ϕ − ψ) MA(ψ);                         (7.23)
                                                ˆ
                     d
                            E((1 − t)ϕ + tψ) = (ψ − ϕ) MA(ϕ);                          (7.24)
                     dt t=0
                                             n−1
                                             X
                                       −1
                         I(ϕ, ψ) = V               kϕ − ψk2(ω,ϕ)j ,(ω,ψ)n−1−j ;        (7.25)
                                             j=0
                                             X
                               I(ϕ, ψ) =           cα I(ϕ|Xαan , ψ|Xαan ).             (7.26)
                                              α
                                       n−1
                                       X     j+1
                       Jψ (ϕ) = V −1             kϕ − ψk2(ω,ϕ)j ,(ω,ψ)n−1−j ;          (7.27)
                                             n+1
                                       j=0
                               1                       n
                             n+1 I(ϕ, ψ) ≤ Jψ (ϕ) ≤ n+1 I(ϕ, ψ);                       (7.28)
                          V −1 dω (ϕ, ψ) ≈ I(ϕ, ψ) ≈ Jψ (ϕ) ≈ Jϕ (ψ);                  (7.29)


## Literal published unit 04-1801.08229-literal-lines-4529-4605.txt

7.6. Locality and the comparison principle. The next result and its consequences play a
crucial role in analyzing deep properties of ω-psh functions and the Monge-Ampère operator.
Theorem 7.40. If ω ∈ Amp(X), then
                                1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)                                     (7.32)
for all ϕ, ϕ0 ∈ E 1 (ω).
  A first consequence is the fact that the mixed Monge–Ampère operator is local in nature,
something that is not an immediate consequence of our definition in §7.3.
Corollary 7.41. Let G ⊂ X an be open set. If ωi ∈ Amp(X) and ϕi , ψi ∈ E 1 (ωi ), 1 ≤ i ≤ n,
are such that ϕi = ψi on G, then
       (ω1 + ddc ϕ1 ) ∧ · · · ∧ (ωn + ddc ϕn ) = (ω1 + ddc ψ1 ) ∧ · · · ∧ (ωn + ddc ψn ) on G.
In particular, if ω ∈ Amp(X) and ϕ, ϕ0 ∈ E 1 (ω) are such that ϕ = ϕ0 on G, then MA(ϕ) =
MA(ϕ0 ) on G.
Proof. By multilinearity, it suffices to prove the final statement. As in [BFJ15, Corollary 5.2],
given ε > 0 we apply Theorem 7.40 to ϕ+ε and ϕ0 . This gives MA(max{ϕ+ε, ϕ0 }) = MA(ϕ)
on G ⊆ {ϕ+ε > ϕ0 }. Letting ε → 0 gives MA(max{ϕ, ϕ0 }) = MA(ϕ) on G, since the Monge–
Ampère operator is continuous under decreasing limits. Exchanging the roles of ϕ and ϕ0
completes the proof.                                                                           
Remark 7.42. As mentioned in Remark 7.23, when all the functions involved are continu-
ous, the mixed Monge–Ampère measure coincides with the one in [CLD12]. Since the latter
is local in nature, Theorem 7.40 and Corollary 7.41 follow in this case. However, for appli-
cations it is important to consider functions ϕ, ϕ0 that are not continuous, and in this case
the Borel set {ϕ > ϕ0 } can be quite complicated. By definition, it is an open subset in the
plurifine topology, see [BT87].
Lemma 7.43. Let ϕ, ϕ0 ∈ PL(X), and pick an integrally closed test configuration X such
that ϕ, ϕ0 and ϕ00 := max{ϕ, ϕ0 } are associated to elements D, D0 , D00 of VCar(X )Q . Pick
an irreducible component E of X0 , and assume that ϕ(vE ) > ϕ0 (vE ). Then ϕ(vF ) ≥ ϕ0 (vF )
for any irreducible component F of X0 that intersects E.
92                          SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. First, ϕD00 −D = ϕD00 − ϕD ≥ 0 implies D00 − D ≥ 0, by Lemma 2.8, and similarly
D00 − D0 ≥ 0. Furthermore, 0 < ϕ00 (vE ) − ϕ0 (vE ) = σ(vE )(D00 − D0 ), and E is thus in the
support of D00 − D0 . Now pick any k × -invariant divisorial valuation w on X with center
ξ ∈ E ∩ F , normalized by w(X0 ) = 1; denote by v ∈ X div its restriction to k(X) ,→ k(X ), so
that w = σ(v) (see §1.3). Then w(D00 − D0 ) = ϕ00 (v) − ϕ0 (v) > 0, and hence ϕ00 (v) = ϕ(v).
This means that D00 = D at ξ; hence 0 = σ(vF )(D00 − D) = ϕ00 (vF ) − ϕ(vF ), which proves
the result.                                                                                 
Proof of Theorem 7.40. First assume that ϕ, ψ ∈ PL ∩ PSH(ω). As in Lemma 7.43, pick
an integrally closed test configuration X dominating the trivial one, such that ϕ = ϕD ,
ϕ0 = ϕD0 and max{ϕ, ϕ0 } = ϕD00 with D, D0 , D00 ∈ VCar(X )Q . As in Proposition 7.19 (ii)
we have                                  X
                         MA(ϕD ) = V −1     bE ((ωX + D)|E )n δvE ,
                                                   E
and a similar formula holds for MA(ϕ ). We thus need to show that ((ωX + D)|E )n =
                                             D00
((ωX + D00 ])|E )n for any E with ϕD (vE ) > ϕD0 (vE ). Now Lemma 7.43 yields ϕD (vF ) =
max{ϕ(vF ), ϕ0 (vF )} = ϕD00 (vF ) for all components F of X0 that intersect E. This implies
that D and D00 coincide in a neighborhood of E. Hence D|E = D00 |E , which implies the
result.
   Now consider the general case. Set
                             f := max{ϕ − ϕ0 , 0} = max{ϕ, ϕ0 } − ϕ0 .
Then {ϕ > ϕ0 } = {f > 0}, and it thus suffices to prove that
                                  f MA(max{ϕ, ϕ0 }) = f MA(ϕ).                                   (7.33)
Indeed, multiplying by f −1 on {f > 0} will then yield the result.             Let (ϕj )j and (ϕ0j )j be
decreasing nets in PL ∩ PSH(ω) converging to ϕ and ϕ0 , respectively, and set
                            fj := max{ϕj − ϕ0j , 0} = max{ϕj , ϕ0j } − ϕ0j .
By the first part of the proof we have fj MA(max{ϕj , ϕ0j }) = fj MA(ϕj ), and (7.33) is now
a consequence of Proposition 7.19 (iii), since max{ϕj , ϕ0j } ∈ E 1 (ω) decreases to max{ϕ, ϕ0 }.
                                                                                               
     Using Theorem 7.40 we obtain the very useful comparison principle.
Theorem 7.44. If ω ∈ Amp(X) and ϕ, ψ ∈ E 1 (ω), then
                          ˆ                 ˆ
                              MA(ϕ) ≥           MA(ψ).
                                  {ϕ<ψ}                {ϕ<ψ}

Proof. We follow [GZ07, Theorem 1.5]. For any ε > 0 we have
      ˆ                         ˆ                                          ˆ
  1 = MA(max{ϕ, ψ − ε}) ≥             MA(max{ϕ, ψ − ε}) +                          MA(max{ϕ, ψ − ε})
                                    {ϕ<ψ−ε}                              {ϕ>ψ−ε}
                    ˆ                    ˆ                       ˆ                     ˆ
              =             MA(ψ) +             MA(ϕ) = 1 +              MA(ψ) −              MA(ϕ),
                  {ϕ<ψ−ε}             {ϕ>ψ−ε}                  {ϕ<ψ−ε}              {ϕ≤ψ−ε}

where the second equality follows from Theorem 7.40 and from MA(ϕ − ε) = MA(ϕ). We
complete the proof by letting ε → 0.                                             
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                          93

  Another simple consequence of Theorem 7.40 is the following formula for the I-functional.


## Literal published unit 04-1801.08229-literal-lines-4838-4864.txt

          E(ϕi ) = E↓ (ϕi ) & E↓ (ϕ)   and       E(ϕi |Xαan ) = E↓ (ϕi |Xαan ) & E↓ (ϕ|Xαan ),
and the first point follows. In the lsc case, the proof is similar, using an increasing net
instead.                                                                                 
8.3. Uniform differentiability of the energy. Building on [BGM20] we prove the fol-
lowing uniform differentiability result, which is crucial for what follows.
Theorem 8.5. Pick f ∈ PL(X)R . For any ϕ ∈ E 1 , we then have
                                          ˆ
                      ↓
                    E (ϕ + εf ) = E(ϕ) + ε f MA(ϕ) + O(ε2 )

as ε → 0, where the implicit constant in the O is uniform with respect to ϕ.
   If ϕ ∈ CPSH(ω) (and for any ϕ ∈ E 1 , if the envelope property holds), the left-hand side
satisfies
                       E↓ (ϕ + εf ) = E(ϕ + εf ) = E(P(ϕ + εf )),
by (8.7).
98                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Corollary 8.6. For any ϕ ∈ E 1 and f ∈ C0 (X) we have
                                               ˆ
                           d       ↓
                                 E (ϕ + tf ) = f MA(ϕ).
                          dt t=0

  Again, one can replace E↓ with E = E ◦ P if ϕ ∈ CPSH(ω), or if the envelope property
holds.
  For any ω ∈ Amp(X) we set Vω := (ω n ).
Lemma 8.7. Pick ω, ω 0 ∈ Amp(X), ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ), and set f := ψ1 − ψ2 . For


## Literal published unit 04-1801.08229-literal-lines-4865-4963.txt

any ϕ ∈ CPSH(ω) we then have
                               ˆ
                            −1
                                                           n
                                 f ω + ω 0 + ddc (ϕ + ψ1 )    ≤ Vω−1 Vω+ω0 − 1 sup |f |.
                                                                              
    Eω (ϕ + f ) − Eω (ϕ) − Vω

Proof. We may assume ω = c1 (L), ω 0 = c1 (L0 ) for ample line bundles L, L0 on X, Indeed, by
homogeneity, we then obtain the case when L, L0 are ample Q-line bundles, and the general
case by a simple perturbation argument based on Proposition 8.1 (iii).
   Consider first any continuous function ρ ∈ C0 (X). For each m ∈ N, ρ defines a sup-norm
k · kmρ on H0 (X, mL), defined by
                                   kskmρ = sup |s|e−mρ .
                                             X an

This norm induces a norm det k · kmρ on the determinant line det H0 (X, mL). Comparing
with the trivial norm, we can and will think of det k · kmρ as a number. It now follows
from [CMac15] (see [BE20, Theorem 9.5]) that the volume
                                                1
                        volL (ρ) := − lim             log det k · kmρ
                                      m→∞ mh0 (mL)

exists in R. We claim that volL (ρ) = EL (ρ). Using [BE20, (9.7)] and (8.3), it is enough
to prove this when X is irreducible. When ρ ∈ CPSH(L), the equality holds by [BE20,
Theorem A] (or [BoJ18b, Lemma 4.5]). In the general case, this yields
                  EL (ρ) = sup {EL (ψ) | ψ ∈ CPSH(L), ψ ≤ ρ} ≤ volL (ρ),
by monotonicity of volL . On the other hand, Theorem 5.1.1 of [Reb21] (which is valid for
arbitrary non-Archimedean fields; see also [BoJ18b, Theorem 4.13] for the trivially valued
case) shows that
                                                           |s|
                           ρm := m−1 log       sup
                                             0
                                          s∈H (X,mL)\{0} ksk mρ

satisfies ρm ∈ PLR ∩ PSH(ω), ρm ≤ ρ and EL (ρm ) → volL (ρ); the claim follows.
   In particular, EL (ϕ + f ) = volL (ϕ + f ) and EL (ϕ) = volL (ϕ). The desired estimate is
now a consequence of Lemma 8.8 below, itself a reformulation of [BGM20, Lemma 3.2]. 
Lemma 8.8. Let L and L0 be ample line bundles on X, and set ω = c1 (L), ω 0 = c1 (L0 ).
Consider functions ϕ ∈ CPSH(ω), and ψ1 , ψ2 ∈ CPSH(ω 0 ). Set f := ψ1 − ψ2 ∈ C0 and
C := Vω+ω0 − Vω > 0. Then
               ˆ
    C inf
        an
           f≤      f (ω + ω 0 + ddc (ϕ + ψ1 ))n − Vω (volL (ϕ + f ) − volL (ϕ)) ≤ C sup f.
       X        X an                                                              X an
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      99

Proof. This is a reformulation in our context of [BGM20, Lemma 3.2] in the special case
of a trivially valued field k. The fact that k is trivially valued means that we can view ϕ,
ψ1 , ψ2 as continuous psh metrics on the Berkovich analytifications of the line bundles L and
L0 , respectively. The difference volL (ϕ + f ) − volL (ϕ) can be viewed as the relative volume
of the metrics ϕ + f and ϕ on L. Note that our current normalization of the volume differs
from the one in loc.cit. by a factor Vω = (Ln ).                                              
Proof of Theorem 8.5. We argue along the lines of the proof of [BGM20, Theorem 3.1].
Write ϕ ∈ E 1 as the limit of a decreasing net (ϕi ) in CPSH(ω). Then E(ϕi +εf ) → E↓ (ϕ+εf )
(by Proposition 8.3 (v)), E(ϕi ) → E(ϕ) (by continuity of E along decreasing nets in PSH(ω)),
and MA(ϕi ) → MA(ϕ) weakly (by Proposition 7.19).
  It is therefore enough to prove the result for ϕ ∈ CPSH(ω). Since f ∈ PL(X)R , we can
choose ω 0 ∈ Amp(X) and ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ) such that f = ψ1 − ψ2 . By Lemma 8.7
we have, for any ε > 0,
                                   ˆ
                                −1
                                                                    n
   Eω (ϕ + εf ) − Eω (ϕ) − εVω       f ω + ddc ϕ + ε(ω 0 + ddc ψ1 )

                                                                ≤ ε Vω−1 Vω+εω0 − 1 sup |f |.
                                                                                   

Now Vω−1 Vω+εω0 − 1 = O(ε), while
                                              n  
                               n             X  n j
Vω−1         c          0          c       −1
       ω + dd ϕ + ε(ω + dd ψ1 ) = MAω (ϕ)+Vω       ε (ω+ddc ϕ)n−j ∧(ω 0 +ddc ψ1 )j ,
                                                 j
                                                          j=1

where (ω + ddc ϕ)n−j ∧ (ω 0 + ddc ψ1 )j is a Radon measure of mass (ω n−j · ω 0j ). The result
follows.                                                                                    
Proof of Corollary 8.6. For f ∈ PL(X)R the result follows directly from Theorem 8.5. For
an arbitrary f ∈ C0 (X) we argue as in the proof of [BGM20, Theorem 3.1]. By Theorem 2.2,
we can pick a sequence (fm ) in PL(X)R such that εm := sup |f − fm | → 0. For each t > 0,
we have fm − tεm ≤ f ≤ fm + tεm ; Proposition 8.3 (i) thus yields
                  E↓ (ϕ + tfm ) − tεm ≤ E↓ (ϕ + tf ) ≤ E↓ (ϕ + tfm ) + tεm ,
and hence          ˆ                                                 
                     fm MA(ϕ) − εm ≤ lim inf t−1 E↓ (ϕ + tf ) − E↓ (ϕ)
                                           t→0+
                                                     ˆ
                             −1    ↓             ↓
                 ≤ lim sup t      E (ϕ + tf ) − E (ϕ) ≤ fm MA(ϕ) − εm ,
                       t→0+
by Theorem 8.5 applied to fm . Letting m → ∞, we get
                                                    ˆ
                            −1    ↓             ↓
                      lim t      E (ϕ + tf ) − E (ϕ) = f MA(ϕ),
                            t→0+

and replacing f with −f concludes the proof.                                                 



## Literal published unit 04-1801.08229-literal-lines-5131-5159.txt

Definition 9.10. Given a measure µ of finite energy, we ´shall say that a net (ϕi ) in E 1 is
maximizing for µ if it computes E∨ (µ) = supϕ∈E 1 E(ϕ) − ϕ µ in the sense that
                                         ˆ
                                E(ϕi ) − ϕi µ → E∨ (µ).

  As a key consequence of the uniform differentiability property of Theorem 8.5, we prove:
Theorem 9.11. Let µ be a measure of finite energy. For any maximizing net (ϕi ) for µ we
have MA(ϕi ) → µ weakly in M.
                             ´              ´
Proof. It is enough to ´show f MA(ϕi ) → f µ for any f ∈ PL(X), by Theorem 2.2. Set
δi := E∨ (µ) − E(ϕi ) + ϕi µ, so that δi → 0. For any ε > 0, (9.8) shows that
                               ˆ                                ˆ
                 ↓                              ∨
                E (ϕi + εf ) − (ϕi + εf ) µ ≤ E (µ) = E(ϕi ) − ϕi µ + δi .

By Theorem 8.5, we infer
                                ˆ                      ˆ
                            ε        f MA(ϕi ) ≤ ε         f µ + δi + Cε2

                              ´ of i and ε. Dividing by ε, letting i → ∞, and then ε → 0,
for a constant C´ > 0 independent
we get lim supi f MA(ϕi ) ≤ f µ, and replacing f with −f yields the result.            
  This yields a variational characterization of solutions to Monge–Ampère equations:
Corollary 9.12.´ Pick ϕ ∈ E 1 and µ ∈ M1 . Then MA(ϕ) = µ iff ϕ computes E∨ (µ) =
supψ∈E 1 E(ψ) − ψ µ . In particular, E∨ (µ) = 0 iff µ = MA(0).
                                  ´
Proof. If MA(ϕ) = µ then E(ϕ) − ϕ µ = E∨ (µ) by (9.3). If the converse holds then the
constant net ϕi = ϕ is maximizing, and hence MA(ϕ) = µ, by Theorem 9.11.           
  As another consequence, we prove that measures of finite energy have a prescribed mass


## Literal published unit 04-1801.08229-literal-lines-5180-5268.txt

Definition 9.14. For any µ ∈ M1 we define a functional Jµ : E 1 → [0, +∞) by
                                                   ˆ
                                      ∨
                           Jµ (ϕ) := E (µ) − E(ϕ) + ϕ µ.

  The notation is justified by the fact that for ϕ, ψ ∈ E 1 we have
                                   ˆ                       ˆ
            JMA(ψ) (ϕ) = E(ψ) − ψ MA(ψ) − E(ϕ) + ϕ MA(ψ) = Jψ (ϕ).                         (9.9)

Note also that
                                         Jµ (0) = E∨ (µ),                                (9.10)
and that a net (ϕi ) in E 1 is maximizing for µ iff Jµ (ϕi ) → 0.
Lemma 9.15. For all ϕ, ϕ0 ∈ E 1 we have
                               I(ϕ, ϕ0 ) ≈ inf (Jµ (ϕ) + Jµ (ϕ0 )).
                                          µ∈M1

In particular, we have for all ϕ ∈ E 1 and µ ∈ M1
                                     J(ϕ) . Jµ (ϕ) + E∨ (µ).                             (9.11)
Proof. On the one hand, inf µ (Jµ (ϕ) + Jµ (ϕ0 )) ≤ Jϕ (ϕ0 ) ≈ I(ϕ, ϕ0 ), thanks to (7.28). Con-
versely, set τ := 12 (ϕ + ϕ0 ). By strict concavity of E (Theorem 7.28),
                            ˆ                               ˆ
           ∨                          1             0     1
          E (µ) ≥ E(τ ) − τ µ ≥ (E(ϕ) + E(ϕ )) −              (ϕ + ϕ0 ) µ + Cn−1 I(ϕ, ϕ0 ),
                                      2                   2
and hence
                                inf (Jµ (ϕ) + Jµ (ϕ0 )) & I(ϕ, ϕ0 ).
                                 µ

In particular, J(ϕ) ≈ I(ϕ, 0) . Jµ (ϕ) + Jµ (0) = Jµ (ϕ) + E∨ (µ), which proves the final
point.                                                                                 
Corollary 9.16. Pick µ ∈ M1 , and choose a maximizing net (ϕi ) for µ. Then J(ϕi ) .
E∨ (µ) + o(1) for all i large enough.
Lemma 9.17. For each C > 0 we have
                         ˆ
                                                     1
                            ϕ (µ − MA(ψ)) . C Jµ (ψ) 2

for all ϕ, ψ ∈ {J ≤ C} ⊂ E 1 and µ ∈ M1C .
Proof. By monotone approximation, we may assume ϕ ∈ PLR . Pick a maximizing sequence
(ψi ) for µ. By Corollary 9.16, J(ψi ) . C + o(1) for all i large enough. By Lemma 7.30, we
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
Theorem 9.20. A Radon probability measure µ ∈ M has finite energy iff E 1 ⊂ L1 (µ).
Proof. Assume that´ µ is finite on E 1 . We first claim that for each C > 0 there exists
  0                           0


## Literal published unit 04-1801.08229-literal-lines-5245-5268.txt

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
Theorem 9.20. A Radon probability measure µ ∈ M has finite energy iff E 1 ⊂ L1 (µ).
Proof. Assume that´ µ is finite on E 1 . We first claim that for each C > 0 there exists
  0                           0


## Literal published unit 04-1801.08229-literal-lines-5445-5459.txt

Corollary 10.4. Assume that X is equidimensional. If ϕ, ψ ∈ E 1 , then the following
properties are equivalent:
     (i) MA(ϕ) = MA(ψ);
    (ii) I(ϕ, ψ) = 0;
   (iii) ϕ − ψ is locally constant.
                                                                                        
Proof. The implications (iii)⇒(i)⇒(ii) are clear. If I(ϕ, ψ) = 0, then I ϕ|Xαan , ψ|Xαan = 0
for each irreducible component Xα of X, by (7.26). In order to prove that ϕ − ψ is locally
constant, we may thus assume that X is irreducible. After adding constant, assume sup ϕ =
sup ψ. Then ϕ(v) = ψ(v) for every v ∈ X div , as a consequence of Theorem 10.3 with µ = δv
and µ0 = δvtriv , since δv ∈ M1 by Proposition 11.1. By Theorem 4.22, we infer ϕ = ψ on
X an , which proves (ii)⇒(iii).                                                           
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD             109

  Corollary 10.4 in turn implies the following useful results.


## Literal published unit 04-1801.08229-literal-lines-6080-6147.txt

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


## Literal published unit 04-1801.08229-literal-lines-6310-6322.txt

and assume that ϕ is bounded below. By Lemma 5.17, the usc regularization
                              P(ϕ)? = sup? {ψ ∈ PSH | ψ ≤ ϕ}
of the ω-psh envelope P(ϕ) is either ω-psh and bounded, or satisfies P(ϕ)? ≡ +∞.
Theorem 13.1. Pick any lsc function ϕ : X an → R ∪ {+∞}, and assume P(ϕ)? 6≡ +∞.
Then
                     P(ϕ)? = P(ϕ) = ϕ a.e. for MA(P(ϕ)? ).
  In particular, the orthogonality property
                             ˆ
                                   (ϕ − P(ϕ)? ) MA(P(ϕ)? ) = 0                           (13.1)
                                X an
holds (compare [BFJ15, BGM20]).
Lemma 13.2. If N ⊂ X an is a negligible Borel set (see Definition 5.1), then µ(N ) = 0 for
all measures of finite energy µ ∈ M1 .


# Exact public source metadata and application checks

{
  "local_source_id": "05-2307.01697",
  "supplied": {
    "arxiv_id": "2307.01697",
    "saved_version": "2307.01697v1",
    "title": "[2307.01697] Measures of finite energy in pluripotential theory: a synthetic approach",
    "public_source": "https://arxiv.org/pdf/2307.01697v1",
    "abstract_url": "https://arxiv.org/abs/2307.01697",
    "actual_abstract_url": "https://arxiv.org/abs/2307.01697",
    "actual_pdf_url": "https://arxiv.org/pdf/2307.01697v1",
    "abstract_html": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.html",
    "abstract_sha256": "95e379bf14e7779de66bca6e020525202fc32bdb575bd1196934cf6ee43eb11a",
    "pdf": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.pdf",
    "pdf_sha256": "979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1",
    "pdf_bytes": 788875,
    "literal_extract": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.txt",
    "extract_sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
    "extract_bytes": 167662,
    "pdftotext_returncode": 0,
    "origin": "Publicly available primary mathematical source; no generated research payload."
  },
  "verified_pdf_sha256": "979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1",
  "verified_extract_sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
  "pdf_header_first_lines": [
    "                                           MEASURES OF FINITE ENERGY IN PLURIPOTENTIAL THEORY: A",
    "                                                            SYNTHETIC APPROACH",
    "",
    "                                                                   SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON",
    "",
    "                                                                  To Bo Berndtsson, on the occasion of his 70+ε-th birthday",
    "arXiv:2307.01697v1 [math.CV] 4 Jul 2023",
    "",
    "",
    "",
    "",
    "                                                 Abstract. We introduce a synthetic approach to global pluripotential theory, covering in",
    "                                                 particular the case of a compact Kähler manifold and that of a projective Berkovich space",
    "                                                 over a non-Archimedean field. We define and study the space of measures of finite energy,",
    "                                                 introduce twisted energy and free energy functionals thereon, and show that coercivity of",
    "                                                 these functionals is an open condition with respect to the polarization.",
    "",
    "",
    "",
    "",
    "                                                                                        Contents",
    "                                            Introduction                                                                                       1",
    "                                            1. A synthetic pluripotential theoretic formalism                                                  6",
    "                                            2. Measures of finite energy                                                                      18"
  ],
  "regenerated_layout_sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/05-2307.01697.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/05-2307.01697-pdf-layout.txt"
  ],
  "application_checks": [
    "Smooth projective X over any complete non-Archimedean K and a positive model curvature representative of an ample L fit the projective Berkovich example.",
    "Do not assert HBC=N1 over arbitrary K; Section 1.3.2 uses the preimage of the ample cone instead.",
    "Example 2.20 establishes orthogonality using published BE21 and BGM22 inputs; Theorem 2.23 gives strong convergence of measures for maximizing test sequences.",
    "The paper explicitly does not investigate potentials of finite energy. Its complete measure space is not identified here with E1/R for positive residue characteristic."
  ]
}

## Literal published unit 05-2307.01697-literal-lines-50-158.txt

                                                                                             1
2                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

       • introduce the twisted energy and free energy functionals on the latter space, whose
         composition with the Monge–Ampère operator respectively recover the Donaldson
         J-functional and the Mabuchi K-energy in the Kähler case, and their analogues in
         the non-Archimedean case;
       • show that coercivity of the free energy is an open condition with respect to the
         Kähler class.
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


## Literal published unit 05-2307.01697-literal-lines-346-383.txt

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


## Literal published unit 05-2307.01697-literal-lines-508-532.txt

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


## Literal published unit 05-2307.01697-literal-lines-1022-1040.txt

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


## Literal published unit 05-2307.01697-literal-lines-1113-1168.txt

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


# Exact public source metadata and application checks

{
  "local_source_id": "06-2209.04879",
  "supplied": {
    "arxiv_id": "2209.04879",
    "saved_version": "2209.04879v2",
    "title": "[2209.04879] Global pluripotential theory on hybrid spaces",
    "public_source": "https://arxiv.org/pdf/2209.04879v2",
    "abstract_url": "https://arxiv.org/abs/2209.04879",
    "actual_abstract_url": "https://arxiv.org/abs/2209.04879",
    "actual_pdf_url": "https://arxiv.org/pdf/2209.04879v2",
    "abstract_html": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.html",
    "abstract_sha256": "1b719dcc2de6a7437184f28dbaf37384bf39673fc8b66a35a4dc716f0cba5341",
    "pdf": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.pdf",
    "pdf_sha256": "55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7",
    "pdf_bytes": 633342,
    "literal_extract": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.txt",
    "extract_sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
    "extract_bytes": 185043,
    "pdftotext_returncode": 0,
    "origin": "Publicly available primary mathematical source; no generated research payload."
  },
  "verified_pdf_sha256": "55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7",
  "verified_extract_sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
  "pdf_header_first_lines": [
    "                                                 GLOBAL PLURIPOTENTIAL THEORY ON HYBRID SPACES",
    "",
    "                                                                             LÉONARD PILLE-SCHNEIDER",
    "",
    "",
    "",
    "",
    "                                                  Abstract. Let A be a Banach ring, and X/A be a projective scheme of ﬁnite type,",
    "                                                  endowed with a semi-ample line bundle L. We deﬁne a class PSH(X, L) of plurisub-",
    "arXiv:2209.04879v2 [math.AG] 17 Mar 2023",
    "",
    "",
    "",
    "",
    "                                                  harmonic metrics on L on the Berkovich analytiﬁcation X an and prove various basic",
    "                                                  properties thereof.",
    "                                                  We focus in particular on the case where A is a hybrid ring of complex power series and",
    "                                                  X/A is a smooth variety, so that X an is the hybrid space associated to a degeneration",
    "                                                  X of complex varieties over the punctured disk. We then prove that when L is ample,",
    "                                                  any plurisubharmonic metric on L with logarithmic growth at zero admits a canonical",
    "                                                  plurisubharmonic extension to the hybrid space X hyb . We also discuss the continuity",
    "                                                  of the family of Monge-Ampère measures associated to a continuous plurisubharmonic",
    "                                                  hybrid metric.",
    "                                                  In the case where X is a degeneration of canonically polarized manifolds, we prove that"
  ],
  "regenerated_layout_sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/06-2209.04879.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/06-2209.04879-pdf-layout.txt"
  ],
  "application_checks": [
    "Section 1.2 assumes equicharacteristic zero, even where a later Remark 4.4 uses the shorter words characteristic zero.",
    "Theorem 4.3 gives continuous psh MA; Remark 4.4 distinguishes a definition of E1 from an extension of MA to E1.",
    "No application to mixed characteristic is inferred from the short wording in Remark 4.4."
  ]
}

## Literal published unit 06-2209.04879-literal-lines-354-394.txt

1.2. Discretely-valued fields. Let K be a complete, discretely-valued field, with valua-
tion v. We denote by R = {v ≥ 0} its valuation ring, m = {v > 0} its maximal ideal and
k = R/m the residue field. We will furthermore assume that K has equicharacteristic zero,
i.e. k and K both have characteristic zero. In this case, it follows from Cohen’s structure
theorem that K is isomorphic to the field K = k((t)) of Laurent series over its residue
field, endowed with the valuation v = ord0 .
We let X be an integral, separated K-scheme of finite type, and write n = dim(X). The
purpose of this section is to explain how one can understand the topological space X an more
concretely using piecewise-affine geometry. The basic idea is that for a large enough class
of integral R-models X of X, there exists a finite-dimensional cell complex Sk(X ) ⊂ X an ,
which we may view as a tropicalization of the model X . As a matter of fact, by [KS06,
thm. 10], the space X an can be realized as the inverse limit of all such Sk(X ), so that
X an is homeomorphic to a tower of simplicial complexes.
We start with a definition:
Definition 1.11. A model of X is a flat, separated R-scheme X , together with an iso-
morphism of K-schemes X ×R K ≃ X.
We will denote X0 := X ×R k the special fiber of X , and by Div0 (X ) the group of Weil
divisors on X supported on the special fiber.
   If X , X ′ are two models of X, a morphism of models f : X ′ −→ X is an R-morphism
whose base change to K induces the identity on X. We will say that X ′ dominates X if
there exists such a morphism, in which case it is unique.
Assume that X/K is proper, and let X /R be a proper model of X. By the valuative
criterion of properness, for any x = (ξx , vx ) ∈ X an , the K-morphism Spec H (x) −→ X -
whose image is the point ξx - lifts in a unique way to an R-morphism from the valuation
ring H (x)◦ to X :
                                                ξx
                                 Spec H (x)            X


                                Spec H (x)◦          Spec R.
The image of the closed point of Spec H (x)◦ under the extended morphism is called the
center of x and denoted by cX (x). The map cX : X an −→ X0 turns out to be surjective
and anticontinuous, i.e. the preimage of a closed subset of X0 by cX is open in X an .
In the case where X/K is smooth, we say a model X /R has simple normal crossing
singularities if X is regular, and the special fiber X0 is a divisor with simple normal
crossing support inside X . Such models always exists when K has equicharacteristic
zero and X/K is projective, by Hironaka’s theorem on resolution of singularities. More
precisely, any model X /R can be dominated by an snc model.
8                                LÉONARD PILLE-SCHNEIDER
                                                      P
To every snc model X of X, with special fiber X0 = i∈I ai Di , we can associate a cell


## Literal published unit 06-2209.04879-literal-lines-1940-2006.txt

Let us start by assuming that K = C and that X is smooth. It then follows from the
seminal work of Bedford-Taylor [BT76] that the mixed Monge-Ampère pairing:
                              (φ1 , ..., φn ) 7→ ddc φ1 ∧ ... ∧ ddc φn ,
a priori defined when each φi is a smooth Hermitian metric on Li , actually extends in a
unique way to semi-positive, locally bounded metrics. The pairing was then further ex-
tended to semi-positive singular metrics by Boucksom-Eyssidieux-Guedj-Zeriahi [BEGZ10].
More precisely, there exists a class E 1 (X, L) ⊂ PSH(X, L) of finite-energy metrics on
(X, L), such that the above mixed Monge-Ampère pairing extends uniquely to a multilin-
ear, measure-valued pairing on E 1 (X, L1 ) × ... × E 1 (X, Ln ). Note that the space E 1 (X, L)
contains in particular CPSH(X, L).
We now assume K is non-archimedean, and that φi ∈ DFS(X, Li ) for every i = 1, ..., n
                   GLOBAL PLURIPOTENTIAL THEORY ON HYBRID SPACES                          35


are differences of Fubini-Study metrics. One can then associate to the φi ’s a signed Radon
measure, the mixed Monge-Ampère measure MA(φ1 , ..., φn ), with similar properties as in
the complex analytic case.
Example 4.1. Assume that K = k((t)) is a discretely-valued field of characteristic zero.
Then pure Fubini-Study metrics on Li are the same as model metrics on Li , so that by
multilinearity we may assume that φi = φLi , where (Xi , Li ) is a nef model of (X, Li ). Up
to passing to a higher model, we may assume X1 = ... = Xn . Then the Monge-Ampère
measure has the following explicit description [CL06]:
                                          X
                      MA(φ1 , ..., φn ) =    bE (L1 · .... · Ln · E)δvE ,
                                            E
where the sum ranges over the irreducible components E of X0 , bE = ordE (t) and δvE is
the Dirac mass at the associated divisorial point vE = b−1
                                                        E ordE .
  In general, the mixed Monge-Ampère measure satisfies the following basic properties:
Proposition 4.2. [BE21, prop. 8.3] Let φi ∈ DFS(Li ) for i = 1, ..., n.
    • The pairing (φ1 , ..., φn ) 7→ MA(φ1 , ..., φn ) is symmetric and multilinear;
    • if φi ∈ FS(Li ) for
                      R all i, then MA(φ1 , ..., φn ) is a positive Radon measure;
    • the total mass X an MA(φ1 , ..., φn ) = (L1 · ... · Ln );
    • if L0 = L1 = OX and φ0 , φ1 ∈ DFS(X), then:
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
metric φ on L such that:
                                   (ddc φ)n = (Ln )µ.
36                                  LÉONARD PILLE-SCHNEIDER




# Exact public source metadata and application checks

{
  "local_source_id": "07-2506.13548",
  "supplied": {
    "public_source": "https://arxiv.org/pdf/2506.13548v2",
    "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
    "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
    "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
    "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
    "origin": "Published primary mathematical source, not generated research."
  },
  "verified_pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
  "verified_extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
  "pdf_header_first_lines": [
    "                                            CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES",
    "",
    "                                                                          WALTER GUBLER AND JOSEPH RABINOFF",
    "",
    "",
    "                                                   ABSTRACT. First we extend the theory of subharmonic functions on smooth strictly k-",
    "                                                   analytic curves from Thuillier’s thesis to the case of possibly singular analytic curves over",
    "                                                   a non-archimedean field k. Classically psh functions are then defined as in complex geom-",
    "arXiv:2506.13548v2 [math.AG] 17 Sep 2025",
    "",
    "",
    "",
    "",
    "                                                   etry by using pullbacks to analytic curves (and requiring compatibility with base change).",
    "                                                   We give various properties of classically psh functions including a local and a global max-",
    "                                                   imum principle. As a consequence, we show that the space of pluriharmonic functions on",
    "                                                   a quasi-compact Berkovich space is finite dimensional. As a technical tool, we use that a",
    "                                                   connected Berkovich space is connected by analytic curves.",
    "",
    "",
    "",
    "",
    "                                                                                      1. INTRODUCTION",
    "                                              Plurisubharmonic functions are the complex analytic counterparts of subharmonic func-"
  ],
  "regenerated_layout_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/07-2506.13548.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/07-2506.13548-pdf-layout.txt"
  ],
  "application_checks": [
    "Actual cached PDF is v2 dated 17 September 2025.",
    "The paper concerns classically psh functions, analytic curves and maximum principles; it expressly excludes the construction of Monge--Ampere measures from its subject.",
    "The R-PL positivity identification does not give the global finite-energy equation theorem."
  ]
}

## Literal published unit 07-2506.13548-literal-lines-1-119.txt

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
Indeed, psh functions are upper semi-continuous and the definition is functorial, so we
are reduced to the case of a smooth analytic curve C. We have to see that a psh function
is subharmonic. By base change, we may assume that k is algebraically closed and non-
trivially valued, see Proposition 3.5(7). Since subharmonic functions are stable under
decreasing limits, and the psh functions are defined by a transfinite regularization process
from smooth psh functions, it is enough to show that a smooth psh function on C is
subharmonic. This follows from a result of Wanner [Wan19, Theorem 4.7].
1.3. Plurisubharmonic R-PL functions. For an R-piecewise linear function h: X → R
on a good strictly k-analytic space over a non-trivially valued field k, we have studied the
notion of semipositivity in the paper [GR25]. This notion is a local analytic version of
the global semipositive metrics introduced by Zhang [Zha95] which are induced by nef
models. We show in Theorem 4.3 that an R-PL function h is semipositive if and only if h
is classically psh.
1.4. Connectivity by curves. In Theorem 5.4, we show that two points x, y of a con-


# Exact public source metadata and application checks

{
  "local_source_id": "08-tel-00010990",
  "supplied": {
    "public_source": "https://theses.hal.science/tel-00010990v1/document",
    "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
    "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
    "literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
    "extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
    "origin": "Published primary mathematical source, not generated research."
  },
  "verified_pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
  "verified_extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
  "pdf_header_first_lines": [
    "N° d'Ordre : 3231",
    "                                      THÈSE",
    "",
    "",
    "                                     présentée",
    "",
    "                    DEVANT L' UNIVERSITÉ DE           RENNES 1",
    "",
    "",
    "                              pour obtenir le grade de",
    "",
    "              DOCTEUR DE L'UNIVERSITÉ DE RENNES 1",
    "",
    "",
    "",
    "                    Mention : Mathématiques      et Appli ations",
    "",
    "",
    "                                         par",
    "",
    "                               Amaury THUILLIER",
    "",
    "",
    "                     Institut de Re her he Mathématique de Rennes"
  ],
  "regenerated_layout_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/08-tel-00010990.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/08-tel-00010990-pdf-layout.txt"
  ],
  "application_checks": [
    "Thuillier thesis is curve potential theory; title page gives defense 13 October 2005 and version 4 October 2005.",
    "No higher-dimensional finite-energy equation result is inferred from curve subharmonicity.",
    "The cached text has severe font-encoding omissions; no delicate formula from this extract is used."
  ]
}

## Literal published unit 08-tel-00010990-literal-lines-1-69.txt

N° d'Ordre : 3231
                                      THÈSE


                                     présentée

                    DEVANT L' UNIVERSITÉ DE           RENNES 1


                              pour obtenir le grade de

              DOCTEUR DE L'UNIVERSITÉ DE RENNES 1



                    Mention : Mathématiques      et Appli ations


                                         par

                               Amaury THUILLIER


                     Institut de Re her he Mathématique de Rennes



                               É ole Do torale MATISSE



                               U.F.R. de Mathématiques




 Théorie du potentiel sur les            ourbes en géométrie analytique
                               non ar himédienne.

                     Appli ations à la théorie d'Arakelov.




    Soutenue le jeudi 13 o tobre 2005 devant la          ommission d'Examen




                            Composition du jury :

               M.     J.-B. Bost                 Rapporteur

               M.     A. Chambert-Loir           Dire teur de thèse

               M.     A. Du    ros               Examinateur

               M.     C. Favre                   Examinateur

               M.     L. Moret-Bailly            Examinateur

               M.     R. Rumely                  Rapporteur
Théorie du potentiel sur les    ourbes en
géométrie analytique non ar himédienne.

 Appli ations à la théorie d'Arakelov.





## Literal published unit 08-tel-00010990-literal-lines-347-423.txt


Toute la suite du hapitre est onsa rée a développement de la théorie du potentiel sur X ,
 'est-à-dire l'étude des fais eaux HX et SHX . Leurs propriétés fondamentales permettent
d'ores et déjà de trans rire telle quelle la résolution du problème de Diri hlet par la méthode
de Perron.
   On s'attend à e que les fon tions sous-harmoniques soient intimement liées aux mesures
(de Radon) positives sur l'espa e topologique lo alement ompa t X ; nous élu idons ette
question en l'abordant du point de vue de la théorie des distributions.
   Cela ommen e par la onstru tion du fais eau A0X des (germes de) fon tions  harmoniques
par mor eaux , appelées fon tions lisses, ainsi que le fais eau A1X des (germes de) formes
lisses, lesquelles sont ertaines mesures sur X . Les développements du hapitre 2 onduisent
naturellement à l'introdu tion d'un opérateur linéaire ddc : A0X → A1X , de noyau HX , qui
prolonge le  lapla ien dis ret  sur les polyèdres entiers S(X ).
   Les espa es ve toriels A0c (X) et A1c (X) des fon tions et formes lisses à support ompa t
sont naturellement munis d'une topologie lo alement onvexe pour laquelle toutes les formes
linéaires sont ontinues. Les espa es D0 (X) et D1 (X) des ourants de degré 0 et 1 respe tive-
ment sont dénis par dualité :
                            D0 (X) = A1c (X)′      D1 (X) = A0c (X)′
et munis de la topologie faible. L'espa e A0 (X) (resp. A1 (X)) se plonge anoniquement dans
D0 (X) (resp. D1 (X)) et l'on vérie que l'appli ation linéaire ( ontinue) de D0 (X) dans D1 (X),
obtenue par transposition à partir de ddc , est un prolongement de et opérateur. Ayant observé
que D0 (X) s'identie anoniquement à l'espa e ve toriel des fon tions réelles sur une partie
I(X) de X , muni de la topologie de la onvergen e simple, nous sommes don en mesure
d'appliquer ddc à n'importe quelle fon tion réelle sur X (au sens des distributions). On peut
dès maintenant pré iser que I(X) s'identie anoniquement à la limite indu tive des squelettes
S(X ) pré édemment dénis.
   L'opérateur ddc : D0 (X) → D1 (X) possède les mêmes propriétés que dans le adre ar hi-
médien :
    il est régulier, dans le sens où A0 (X) s'identie à l'espa e des ourants T de degré 0 sur
     X tels que ddc T appartienne au sous-espa e A1 (X) de D1 (X) ;
    si X est onnexe et propre, son image est onstituée des ourants ρ de degré 1 orthogonaux
     aux fon tions onstantes (tels que hρ, 1i = 0).
   Le lien ave l'étude des fon tions sous-harmoniques sur X s'opère en établissant que elles-
 i s'identient aux ourants T de degré 0 tels que le ourant ddc T soit positif, 'est-à-dire
vérie
                                  hddc T, ϕi = hT, ddc ϕi ≥ 0
pour toute fon tion positive ϕ ∈ A0c (X). Comme dans le ontexte ar himédien, les ourants
(de degré 1) positifs oïn ident ave les mesures de Radon positives sur X ; nous en dé-
duisons la orrespondan e familière entre mesures positives et fon tions sous-harmoniques
(potentiels ). Tout e i dé oule aisément du théorème d'approximation suivant : une fon tion
sous-harmonique u sur X est, sur tout ouvert relativement ompa t Ω de X , l'enveloppe
inférieure d'une famille dé roissante de fon tions sous-harmoniques et lisses.
  Sur le modèle de la théorie lassique, nous poursuivons en introduisant des méthodes hil-
bertiennes ; elles- i trouvent leur origine dans la forme bilinéaire symétrique positive
                                                              Z
                         A0c (X) × A0c (X) → R, (ϕ, ψ) 7→ −      ϕ ddc ψ
                                                                X
vi



(forme de Diri hlet), version non ar himédienne de la forme bilinéaire
                                                     Z                 Z
           ∞              ∞                                   c      i
          C (M, R) × C (M, R) → R, (ϕ, ψ) 7→ −           ϕ dd ψ =        ∂ϕ ∧ ∂ψ,
                                                       M            π M
où M est une surfa e de Riemann ompa te et qui généralise, dans le as d'une valuation
dis rète, la forme d'interse tion sur le groupe des diviseurs  verti aux  sur les modèles
entiers de X . La omplétion de A0c relativement à e produit s alaire est un espa e de Hilbert
réel, noté W1 (X), qui s'identie anoniquement à un sous-espa e ve toriel de D0 (X). Une
mesure positive µ sur X est d'énergie nie si elle admet un potentiel g dans W1 (X), l'énergie
E(µ) de µ étant alors dénie omme le arré de la norme de g.
   Nous utilisons e point de vue pour l'étude des apa ités. Supposons que X soit propre et
soit Y ⊂ X un domaine k-anoïde, d'intérieur Ω ; la apa ité relative d'un ompa t K de Ω
est le nombre réel positif C(K, Ω) déni par la formule
                                                               −1
                         C(K, Ω) = inf{EΩ (µ) ; µ ∈ Prob(K)}         ,

où Prob(K) est l'ensemble des mesures de probabilité sur K et EΩ (µ) est l'énergie de la mesure
µ (relativement à l'ouvert Ω). On pose
                         C(E, Ω) = sup{C(K, Ω) ; K ⊂ E ompa t}
pour tout sous-ensemble E de Ω et la apa ité extérieure (relative à Ω) est la fon tion
                 C ∗ (., Ω) : P(Ω) → R≥0 ∪ {+∞}
                                E 7→ inf{C(U, Ω) ; U ⊂ Ω ouvert, E ⊂ U }.
C'est une apa ité au sens de G. Choquet, dont on montre qu'elle s'annule exa tement sur
les parties polaires de Ω, 'est-à-dire elles ontenues dans l'ensemble {u = −∞} des ples
d'une fon tion sous-harmonique u sur Ω. Nous avons i i suivi d'assez près la présentation


## Literal published unit 08-tel-00010990-literal-lines-5257-5280.txt

3.4.1. Le théorème d'approximation.
   En vertu de la proposition 3.4.10, une fon tion sous-harmonique u sur X dénit une fon tion
réelle sur I(X) et détermine par onséquent un ourant dans D0 (X).
Lemme 3.4.1.  L'appli ation

                               SH(X) → D0 (X),         u 7→ u|I(X)
est inje tive et son image est l'ensemble des ourants T ∈ D0 (X) satisfaisant à la ondition
suivante :
              pour tout domaine k-anoïde V ⊂ X et tout point x ∈ I(V ) − ∂V ,
                                        T (x) ≤ hT, νxV i.
Démonstration. Soient u une fon tion sous-harmonique sur X et x un point dans X − I(X).
  Étant donnée une suite dé roissante (Vn ) de domaines k-anoïdes de X dont le bord de
Shilov Γ(Vn ) est réduit à un point xn et telle que
                                                 \
                                         {x} =      Vn ,
                                                  n

le prin ipe du maximum (proposition 3.1.11) implique les inégalités u|Vn ≤ u(xn ) ; la suite
(u(xn )) est don dé roissante et u(x) ≤ inf n u(xn ). D'autre part, en vertu de la semi- ontinuité
supérieure de u,
                              u(x) ≥ limsupn u(xn ) = inf u(xn ).
                                                         n
La fon tion u est ainsi uniquement déterminée par sa restri tion au sous-ensemble I(X) de
X.


# Exact public source metadata and application checks

{
  "local_source_id": "09-Berkovich-PMIHES",
  "supplied": {
    "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
    "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
    "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
    "literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
    "extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
    "origin": "Published primary mathematical source, not generated research."
  },
  "verified_pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
  "verified_extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
  "pdf_header_first_lines": [
    "P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.",
    "",
    "",
    "",
    "",
    " V LADIMIR G. B ERKOVICH",
    " Étale cohomology for non-Archimedean analytic spaces",
    " Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161",
    " <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>",
    "",
    "",
    "",
    "",
    "      © Publications mathématiques de l’I.H.É.S., 1993, tous droits réservés.",
    "      L’accès aux archives de la revue « Publications mathématiques de l’I.H.É.S. » (http://",
    "      www.ihes.fr/IHES/Publications/Publications.html) implique l’accord avec les conditions géné-",
    "      rales d’utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou im-",
    "      pression systématique est constitutive d’une infraction pénale. Toute copie ou impression de",
    "      ce fichier doit contenir la présente mention de copyright.",
    "",
    "",
    "",
    "",
    "                               Article numérisé dans le cadre du programme"
  ],
  "regenerated_layout_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/09-Berkovich-PMIHES.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/09-Berkovich-PMIHES-pdf-layout.txt"
  ],
  "application_checks": [
    "Berkovich 1993 is Etale cohomology for non-Archimedean analytic spaces, not a finite-energy equation paper.",
    "Analytic-space foundations do not by themselves supply envelopes, energy compactness or unbounded comparison."
  ]
}

## Literal published unit 09-Berkovich-PMIHES-literal-lines-1-16.txt

P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.




 V LADIMIR G. B ERKOVICH
 Étale cohomology for non-Archimedean analytic spaces
 Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161
 <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>




      © Publications mathématiques de l’I.H.É.S., 1993, tous droits réservés.
      L’accès aux archives de la revue « Publications mathématiques de l’I.H.É.S. » (http://
      www.ihes.fr/IHES/Publications/Publications.html) implique l’accord avec les conditions géné-


## Literal published unit 09-Berkovich-PMIHES-literal-lines-92-160.txt

        7.7. The Base Change Theorem for Cohomology with Compact S u p p o r t . . . . . . . . . . . . . . . . . . . . .                                              153
        7.8. The Smooth Base Change Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         154
REFERENCES.................................................................................                                                                           157

INDEX OF NOTATIONS                 ........................................................................                                                           158

INDEX OF TERMINOLOGY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      160
                                   INTRODUCTION

        The problem of constructing an 6tale cohomology theory for non-Archimedean
 analytic spaces has arisen from Drinfeld's work on elliptic modules [Dri]. In his work,
 Drinfeld defined (among other things) the first cohomology group HP^X, pj as the set
 of pairs (L, <p), where L is an invertible sheaf on X, and <p is an isomorphism 0^ ^ L0".
 He showed that for the one-dimensional j&-adic upper half-plane 02 this group gives
 rise to a certain infinite dimensional representation of GL^), where k is the ground
 local field. Afterwards, in [Dr2], Drinfeld constructed a certain family of equivariant
 coverings of the d-dimensional j&-adic upper half-plane Q^1, and suggested that all
 cuspidal representations of the group GL^i(^) are realized in high dimensional ^tale
 cohomology groups of this family of coverings.
       Since then, as far as I know, the only attempt to construct an Aale cohomology
 theory for non-Archimedean analytic spaces was undertaken by 0. Gabber. We under-
 stand that 0. Gabber has made progress in the subject, but, unfortunately, he has
written nothing on it. Besides that, in [FrPu] and [ScSt], definitions of an Aale topology
 on a non-Archimedean analytic space were given, and in [ScSt] the cohomology
o{£ld+l is calculated for arbitrary d under the hypotheses that this cohomology satisfies
certain reasonable properties. Finally, in [Gar], a conjecture, which is an explicit form
of Drinfeld's suggestion, is proposed. The conjecture predicts the decomposition of
the representations of GL^_n(A) and the Galois group of k {k is a ^-adic field) on the
rf-dimensional cohomology group of the equivariant system of coverings of ^ d+l in
terms of the Langlands correspondence.
       The purpose of this work is to develop many basic results of dtale cohomology
for non-Archimedean analytic spaces. We define the ftale cohomology and the Aale
cohomology with compact support and calculate the cohomological dimension of an
analytic space. We prove a Comparison Theorem for Gohomology with Compact Sup-
port which states that, for a compactifiable morphism 9 : W -> 3£ between schemes
of locally finite type over the spectrum of a A-affinoid algebra and a torsion sheaf ^
on ^ there is a canonical isomorphism (R3 9, ^)"1 ^> R® y^ j?'"1, q ^ 0. We also
prove a Poincar^ Duality Theorem, the acyclicity of the canonical projection X X D -^ X,
where D is an open polydisc in the affine space, a Gohomological Purity Theorem,
the invariance of the cohomology under algebraically closed extensions of the ground
field, a Base Change Theorem for Gohomology with Compact Support and a Smooth
Base Change Theorem (all the results are proved for torsion sheaves with torsion orders
prime to the characteristics of the residue field of k). In particular, all the properties
of the (c abstract" cohomology theory from [ScSt] hold. Our main result is a Compa-
rison Theorem which states that, for a morphism of finite type 9 : W -> 3E between
8                               VLADIMIR G. BERKOVICH

schemes of locally finite type over k and a constructible sheaf 3F on W with torsion
orders prime to the characteristics of the residue field of k, there is a canonical isomor-
phism (R9 <p, ^^)aD -^ R° 9;11 ^ran, ^ 0. We note that the only previous proof of the
Comparison Theorem in the classical situation over C uses Hironaka's Theorem on
resolution of singularities. Our proof of the Comparison Theorem works over C as well
and does not use Hironaka's Theorem.
       Qur approach to ^tale cohomology is completely based on the previous work
[Ber]. In that work we introduced analytic spaces which are natural generalizations of
the complex analytic spaces and have the advantage that they allow direct application
of the geometrical intuition. One should say that although the analytic spaces from [Ber]
were considered in a more general setting than that for rigid analytic geometry (for
example, the valuation of the ground field is not assumed to be nontrivial), they don't
give rise to all reasonable rigid spaces. And so our first purpose in this work is to extend
the category of analytic spaces from [Ber] so that the new category gives rise to all
reasonable rigid spaces, for example, to those that are associated with formal schemes
of locally finite type over the ring of integers of k.
       We now give a summary of the material which follows. Let k be a non-Archimedean
field, and let k denote its residue field. As in [Ber], we don't assume that the valuation
of k is nontrivial.
       In § 1 we introduce a category ofA-analytic spaces more general than those from
 [Ber]. These analytic spaces possess nice topological properties. For example, a basis
of topology is formed by open locally compact paracbmpact arcwise connected sets.


# Exact public source metadata and application checks

{
  "local_source_id": "10-1204.6277",
  "supplied": {
    "public_source": "https://arxiv.org/pdf/1204.6277v2",
    "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
    "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
    "literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
    "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
    "origin": "Published primary mathematical source, not generated research."
  },
  "verified_pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
  "verified_extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
  "pdf_header_first_lines": [
    "                                          FORMES DIFFÉRENTIELLES",
    "                                          RÉELLES ET COURANTS SUR LES",
    "arXiv:1204.6277v2 [math.AG] 25 Jul 2025",
    "",
    "",
    "",
    "",
    "                                          ESPACES DE BERKOVICH",
    "",
    "",
    "",
    "",
    "                                                         Antoine Chambert-Loir",
    "                                                                Antoine Ducros",
    "",
    "Antoine Chambert-Loir",
    "Université Paris Cité, Institut de Mathématiques de Jussieu-Paris Rive Gauche,",
    "F-75013, Paris, France.",
    "E-mail : antoine.chambert-loir@math.univ-paris-diderot.fr",
    "Antoine Ducros",
    "Sorbonne Université, Université de Paris, CNRS, Institut de Mathématiques de",
    "Jussieu-Paris Rive Gauche, IMJ-PRG, F-75005, Paris, France.",
    "E-mail : antoine.ducros@imj-prg.fr",
    ""
  ],
  "regenerated_layout_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
  "pdftotext_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/10-1204.6277.pdf",
    "/workspace/research/campaigns/round-47/P16.3-public-source-positive-residue-characteristic/artifacts/codex-69HHDl/source-extracts/10-1204.6277-pdf-layout.txt"
  ],
  "application_checks": [
    "Actual PDF is v2 posted 25 July 2025; interior date is 29 July 2025.",
    "Section 0.2.15 states characteristic-independent local forms/currents, without resolution or alterations.",
    "Local Bedford--Taylor/metric curvature theory is not used as a proof of global E1 compactness or existence.",
    "No identification of an arbitrary global BFJ singular metric with the local regularizable psh class is assumed."
  ]
}

## Literal published unit 10-1204.6277-literal-lines-1-27.txt

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




29 juillet 2025, 0h06


## Literal published unit 10-1204.6277-literal-lines-583-606.txt

géométrie algébrique/analytique dans notre théorie des formes et courants.
16                                    INTRODUCTION

0.2.15. — Nous nous sommes efforcés de rédiger le texte dans la généralité maximale
compatible avec nos compétences techniques. Ainsi, on ne se limite pas aux espaces ana-
lytiques algébriques, on ne les suppose pas lisses, ni même réduits. En fait, notre théorie
est très « générique » ; par exemple, les supports des formes lisses de degré maximal ne
rencontrent aucun fermé de Zariski d’intérieur vide, en particulier aucun point rigide (en
dimension > 0). Ainsi, des hypothèses de lissité, etc. n’interviendraient jamais de façon
cruciale au cours des preuves.
   La théorie est valable en toute caractéristique. Elle n’utilise à aucun moment la réso-
lution des singularités (Hironaka, Temkin) ni même l’existence d’altérations (De Jong),
notamment grâce à l’article [50] du second auteur qui permet de dégager, via la théorie
des modèles, les propriétés des tropicalisations et des squelettes. Nous n’utilisons pas de
modèles formels pour développer la théorie (mais ils fournissent une source importante
d’exemples). Toutefois, nous faisons appel à des arguments de réduction, proches de ceux
permis par la géométrie formelle, mais de nature plus locale et techniquement plus aisés,
fournis par la théorie de Temkin [126, 127].
   La théorie est aussi valable en valuation triviale. C’est d’ailleurs un point crucial pour
le calcul des opérateurs de Monge–Ampère associés aux métriques formelles qui repose
sur la théorie appliquée au corps résiduel du corps de base, corps résiduel que l’on munit
de la valeur absolue triviale.




## Literal published unit 10-1204.6277-literal-lines-645-670.txt

0.3.2. — Nous avons déjà mentionné la théorie des δ-formes de Gubler et Künne-
mann [80]. Signalons l’article de Mihatsch [103] dans lequel il raffine leur construction
et, surtout, en donne une application à la théorie de l’intersection sur les tours de Lubin–
Tate.
0.3.3. — La résolution par Yau du problème de Monge–Ampère fut un progrès majeur
de la géométrie complexe. L’analogue non archimédien a été proposé par Kontsevich et
Tschinkel et résolu par Boucksom, Favre et Jonsson dans [33, 34]. Dans l’esprit, leur
théorie est liée à celle de ce texte mais les définitions et les méthodes sont différentes, car
elles reposent d’emblée sur la considération de modèles et de la théorie de l’intersection
sur leur fibre spéciale.
0.3.4. — Dans [30], Boucksom et Eriksson construisent une variante de l’accouple-
ment de Deligne dans notre théorie. Cet accouplement est également considéré dans
l’article [140] de Yuan et Zhang.
0.3.5. — La notion de forme et de courant positifs est fondamentale dans le développe-
ment de notre théorie, où une notion convenable de fonction psh joue un rôle crucial. La
définition que nous proposons impose la possibilité d’approximation d’une fonction psh
par des fonctions lisses psh. Gubler et Rabinoff ont considéré une définition différente,
fondée sur la restriction aux courbes et la théorie de Thuillier des fonctions psh sur les
courbes. Ils établissent notamment un principe du maximum. Nous ne savons pas si un
tel principe vaut pour les fonctions psh de ce texte.
   Notre notion de fonction psh a un lien étroit avec celle de métrique semipositive au
sens de Zhang [142]. Signalons l’article [82] qui étudie plus en détail cette dernière.
   Signalons enfin l’article [29] dans lequel Botero, Burgos Gil et Sombra étudient la
notion de fonction convexe sur un espace linéaire par morceaux.


