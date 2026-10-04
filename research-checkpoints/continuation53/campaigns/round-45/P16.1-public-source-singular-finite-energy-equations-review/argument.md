# Exact scoped status

{
  "id": "P16.1",
  "status": "partial",
  "exact_result": "Finite-energy genuine Monge-Ampere operator and existence/uniqueness on actual integral projective unibranch curves over an algebraically closed trivially valued field of characteristic zero, with ample L, raw mass deg L, and exact finite-energy measure criterion D(mu)/(2 deg L)<infinity. All curve normalization, model-psh, energy, envelope, compactness, differentiation and comparison descents are proved. A nodal curve gives a finite-energy measure outside the operator image.",
  "proof_file": "P16.1-argument.md",
  "concrete_gaps": [
    "No envelope-property proof for arbitrary higher-dimensional unibranch projective varieties; the supplied trivially valued source equates this with the missing finite-energy existence theorem.",
    "The isolated-ray PL spanning and psh descent proof is one-dimensional; higher-dimensional conductor descent and its energy and envelope compatibility are not established.",
    "No singular-space finite-energy equation package is proved over the nontrivially discretely valued residue-characteristic-zero field endpoint in the original arbitrary-dimensional scope.",
    "For non-unibranch varieties, standard raw mass plus finite dual energy is insufficient; a corrected admissible-measure range and conductor-compatible descent theorem remain to be supplied.",
    "Any broader reducible or disconnected statement must retain componentwise polarization masses and the correct number of uniqueness constants."
  ]
}


# Entire final proof

# P16.1: a proved curve sector and the remaining singular-variety problem

This is an unverified mathematical draft. It proves the curve theorem stated below from exact published background inputs and the descent arguments given here. It does not solve the full original atom P16.1. The general unibranch envelope replacement in higher dimension, and the singular finite-energy equation under the discretely valued hypotheses, remain gaps. Hashes, executions and TeX compilation are reproducibility evidence, not mathematical verification.

## 1. Exact result and normalization

Theorem (partial result). Let $k$ be an algebraically closed field of characteristic zero with the trivial absolute value, let $X$ be an integral projective unibranch $k$-curve, and let $L$ be an ample line bundle on $X$. Write $V=\deg_X L>0$, $\theta=c_1(L)$, and $\nu:Y\longrightarrow X$ for the normalization. No smoothness of $X$, normality of $X$, reducedness of the conductor subscheme, or restriction to a skeleton is assumed. Integrality includes reducedness and connectedness. The field is complete because its valuation is trivial. The polarization remains the actual line bundle on $X$.

Use the canonical trivial metric on $L$ as the reference metric. Define $\operatorname{PSH}(X,L)$ using decreasing limits of semipositive model metrics, equivalently the ample-class Fubini--Study construction of Boucksom--Jonsson [BJ]. Define the normalized intersection energy $E_X$ with $E_X(0)=0$ and $E_X(\varphi+c)=E_X(\varphi)+c$, and put $\mathcal E^1(X,L)=\{\varphi\in\operatorname{PSH}(X,L):E_X(\varphi)>-\infty\}$.

There is a unique decreasing-continuous extension of the genuine model Monge--Ampere measure

\[
 \mathrm{MA}^{\rm raw}_{X,L}:\mathcal E^1(X,L)\longrightarrow
 \{\hbox{positive Radon measures on }X^{\rm an}\hbox{ of mass }V\}.
\]

For a positive Radon measure $\mu$, the equation $\mathrm{MA}^{\rm raw}_{X,L}(\varphi)=\mu$ has a solution in $\mathcal E^1(X,L)$ if and only if

\[
 \mu(X^{\rm an})=V,\qquad
 E_X^*(\mu/V):=\sup_{\varphi\in\mathcal E^1(X,L)}
 \left(E_X(\varphi)-V^{-1}\int\varphi\,d\mu\right)<\infty.
\]

The supremum can equivalently be taken over $H_{\rm dom}(X,L)$, the ample model potentials on models dominating the trivial test configuration. The solution is unique modulo one additive real constant. It is uniquely fixed by $\varphi(o)=\sup\varphi=0$, where $o$ is the trivial valuation of $k(X)$. Its metric is unique modulo multiplication by a positive constant. The operator agrees with the intersection-theoretic Monge--Ampere operator on actual $X$, is continuous along decreasing nets in finite energy, and is strongly continuous with the [BJ] strong topologies. Compactness, envelopes, energy differentiation and comparison are justified in Section 7.

This sector changes the field endpoint to the established trivial-valuation endpoint and restricts dimension to one. It is not asserted to extend the original discretely valued theorem in arbitrary dimension. It is a genuine singular-curve theorem with all normalization descents proved, rather than a theorem merely on $Y$.

## 2. Exact published inputs and their limits

[BJ] means Boucksom--Jonsson, *Global pluripotential theory over a trivially valued field*, the supplied arXiv:1801.08229v4. Its standing field is algebraically closed and trivially valued. Theorem A extends the finite-energy operator to possibly singular projective varieties and gives an embedding with dense image; its unconditional surjectivity statement assumes smoothness and characteristic zero or dimension at most two. The body handles reducible varieties, but all positive assertions here are for integral varieties. In this version, Theorem 5.11 equates envelope regularity and weak compactness; Theorem 12.8 equates envelope regularity and finite-energy surjectivity; Conjecture 5.14 proposes envelopes for unibranch varieties. Lemma 5.13 assumes envelope properties on the target. Using that lemma to prove the same envelope property by normalization would be circular.

The background inputs used in the proof are the following exact results. Example 2.5 makes $\max\{\log|\mathfrak a|,-r\}$ a PL function for any ideal on any projective variety and rational $r>0$. Example 2.6 gives the ray generators of PL on a smooth curve. Proposition 3.6(vi) reflects model psh positivity under a surjective projective morphism, for a function already in PL on the target. Proposition 3.10 uniformly approximates a nef PL potential in a fixed ample class by $H_{\rm dom}$ potentials. Theorem 4.15(iii) gives decreasing approximation in that fixed ample class; Theorem 4.7 supplies decreasing closure. Example 4.13 is the smooth-curve convex-ray criterion. Theorem 5.20 gives the envelope property on smooth connected varieties for nef classes when characteristic is zero or dimension is at most two. All its hypotheses hold on $Y$ here.

[BJ] Theorems 7.1 and 7.18 and Proposition 7.19 construct energy and genuine finite-energy MA on singular projective varieties, with normalization identities (7.5) and (7.18). Example 7.20 gives the curve Laplacian. Theorems 7.40 and 7.44 give locality and comparison without smoothness. Theorem 8.5 and Corollary 8.6 differentiate the downward extension of energy on singular varieties; identifying it with energy of a psh envelope requires the envelope property. Proposition 12.7 supplies strong continuity. These results are published background, not new claims proved solely by running a program. Their precise application checks and selected literal proofs are retained in source-extracts/source-provenance.json.

The cached arXiv:1201.0188 is its actual supplied v1. Its PDF watermark says 30 December 2011, while its internal date says 29 October 2018; both are retained literally, without relabelling the cache. Theorem A assumes a complete discretely valued field of residue characteristic zero, a smooth projective variety admitting descent to a one-variable function field whose completion is the ground field, ample $L$, raw mass $\deg_L(X)$, and support on the dual complex of an SNC model. The polarization need not descend to the function field. This is not an arbitrary-support finite-energy theorem. The supplied 1201.0187v2 proves compactness and regularization under smooth projective, discrete-valuation and residue-characteristic-zero hypotheses.

The cached 1805.01016v3 is Boucksom--Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*. Theorem A concerns continuous psh metrics on geometrically reduced projective schemes over complete valued fields. Corollary B retains continuity of envelopes as a hypothesis. Proposition 9.14 is a continuous-metric energy identity, not a general finite-energy existence theorem. The synthetic 2307.01697v1, Theorem A, completes the space of finite-energy measures and gives density of test-MA measures; it does not construct every such measure as MA of an actual singular-space finite-energy potential. Pille--Schneider, 2209.04879v2, Remark 4.4 distinguishes the arbitrary-field definition of finite energy from the unknown general extension of its MA operator. The September 2025 Gubler--Rabinoff 2506.13548v2 explicitly says that regularization and defining MA are not the subject of that paper. Its singular-curve subharmonic theory is not silently substituted for the global equation theory. The other three supplied sources are background caches, not indispensable inputs to the new theorem.

## 3. Analytic normalization, conductor and PL descent

Normalization is finite for a variety of finite type over a field. A normal curve over the perfect field $k$ is smooth. Thus $Y$ is a smooth integral projective curve. A unibranch curve has exactly one point $q$ above each closed point $p$ of $X$; since $k$ is algebraically closed, both residue fields are $k$. For this curve argument these are the precise consequences of unibranchness that are needed.

Every point of $Y^{\rm an}$ is either the trivial valuation $o$, a point $t\operatorname{ord}_q$ for $q\in Y(k)$ and $0<t<\infty$, or the endpoint $q_\infty$ with support $q$. Indeed a valuation of $k(Y)$ has a center by properness. If that center is the generic point its valuation is trivial. Otherwise the local ring is a DVR, every unit has value zero, and the valuation is a positive multiple of its order valuation. A semivaluation with nongeneric support is the trivial valuation on the closed point's residue field. The same function field is $k(X)$. A finite birational normalization therefore bijects generic-support semivaluations, and the unique-preimage condition bijects the closed-support semivaluations. Consequently $\nu^{\rm an}$ is bijective. It is continuous, with compact source and Hausdorff target, and is therefore a homeomorphism. This proof does not claim that a normalization of an arbitrary singular variety is an analytic homeomorphism.

For each $p\in X(k)$ let $q$ be its unique preimage. Define the positive integer $e_p$ by

\[
 \mathfrak m_p\mathcal O_{Y,q}=\mathfrak m_q^{e_p}.
\]

The ideal is nonzero and vanishes at $q$, so $1\leq e_p<\infty$. Away from $q$ its extension is the unit ideal. Its canonical ideal norm therefore satisfies

\[
 \nu^*\log|\mathfrak m_p|(t\operatorname{ord}_q)=-e_pt,
 \quad \nu^*\log|\mathfrak m_p|(o)=0,
 \quad \nu^*\log|\mathfrak m_p|(q_\infty)=-\infty,
\]

and is zero on every other ray, including its endpoint. For rational $a>0$ set

\[
 h_{p,a}=e_p^{-1}\max\{\log|\mathfrak m_p|,-e_pa\}\in\operatorname{PL}(X).
\]

Example 2.5 applies to the coherent point ideal on singular $X$. Its pullback is the function $-\min\{t,a\}$ on the $q$-ray and zero on all other rays. These functions, with rational constants, span $\operatorname{PL}(Y)$ by Example 2.6. Pullback always maps flag-ideal functions on $X$ to flag-ideal functions on $Y$. Since $\nu^{\rm an}$ is surjective, pullback is injective. We have proved

\[
 \nu^*:\operatorname{PL}(X)\simeq\operatorname{PL}(Y),
 \qquad \nu^*:\operatorname{PL}(X)_{\mathbb R}\simeq\operatorname{PL}(Y)_{\mathbb R}.
\]

The conductor is $\mathfrak c=\operatorname{Ann}_{\mathcal O_X}(\nu_*\mathcal O_Y/\mathcal O_X)$. It has finite support and may be nonreduced. The proof did not assert that arbitrary sections on $Y$ descend, that powers of such sections descend, or that normalization changes no local algebra. It used actual ideals on $X$. The integer $e_p$ is the point-ideal order, not a conductor exponent. One branch at every conductor point is indispensable for the displayed isolated-ray formula. There are no extra jet conditions on $\mathfrak c$ in this theorem.

## 4. Polarization, nef reflection and exact psh descent

Put $A=\nu^*L$. It is ample: on an integral projective curve ampleness is equivalent to positive degree, and degree is unchanged here. To verify the degree rather than assume it, the finite birational map gives an exact sequence with finite-length quotient $T$,

\[
 0\longrightarrow\mathcal O_X\longrightarrow\nu_*\mathcal O_Y
 \longrightarrow T\longrightarrow0.
\]

Tensor by $L^m$ and use finite pushforward and the projection formula. The difference $\chi(Y,A^m)-\chi(X,L^m)$ is the constant length of $T$. Comparing the linear coefficients of these Hilbert polynomials gives $\deg_Y A=\deg_X L=V$. In particular no degree factor and no normalization of a restriction of $\mu$ occur. Pullback of the canonical metric of $L$ is the canonical metric of $A$, since a local trivialization at the center pulls back to a local trivialization at its inverse image.

Here is the application of nef reflection, with its essential prerequisite explicit. Given $f\in\operatorname{PL}(X)_{\mathbb R}$, choose a test configuration of actual $X$ dominating $X\times\mathbb A^1$ and a vertical divisor determining $f$. Taking the closure of the graph of the generic morphism from $Y\times\mathbb G_m$, and dominating also the trivial configuration of $Y$, gives a projective surjective morphism of test configurations. No smooth resolution or ample pullback along a resolution is needed. Pulling back the representing class preserves nefness. Conversely, if its pullback is nef, each vertical irreducible curve downstairs is dominated by a projective curve upstairs; one obtains such a curve by hyperplane cuts in a component dominating the downstairs curve. The degree of the pulled-back line bundle is the positive degree of that map times the downstairs degree. Thus nonnegative degrees upstairs force nonnegative degrees downstairs. Passing to a common dominating model does not change the model-psh property. This is precisely the argument behind [BJ, Proposition 3.6(vi)]. Therefore

\[
 f\in\operatorname{PL}(X)_{\mathbb R}\text{ is }L\text{-psh}
 \quad\Longleftrightarrow\quad
 \nu^*f\text{ is }A\text{-psh}.
\]

This conclusion cannot be applied to an arbitrary function on $Y$ before its PL descent is proved. Section 3 supplies that missing prerequisite in this curve case.

Now let $\psi\in\operatorname{PSH}(Y,A)$. Approximate it decreasingly by $H_{\rm dom}(Y,A)$, using Theorem 4.15(iii). Descend every approximant through the proved PL isomorphism. Nef reflection makes each descended approximant $L$-psh on actual $X$. The analytic homeomorphism makes them a decreasing family with pointwise limit $\varphi=\psi\circ(\nu^{\rm an})^{-1}$. The limit is usc and generically finite, and decreasing closure makes it $L$-psh. The forward inclusion is ordinary pullback of psh functions, obtained either from Fubini--Study pullback or the same approximation. Hence

\[
 \nu^*:\operatorname{PSH}(X,L)\simeq\operatorname{PSH}(Y,A).
\]

It is a homeomorphism for the weak topology of pointwise convergence on divisorial valuations: those valuations of the common function field are identified. This is a proof of descent before invoking envelopes or compactness, so no circular assumption on singular $X$ has entered. Proposition 3.10 shows further that the descended model approximants can themselves be uniformly approximated in the fixed class by $H_{\rm dom}(X,L)$.

## 5. Energy and the genuine operator on actual X

For $\varphi\in\operatorname{PSH}(X,L)$ write $a=\varphi(o)$ and identify the rays through the proved homeomorphism. Put $b_q(t)=-\frac{d}{dt}\varphi(t\operatorname{ord}_q)$, with the derivative taken almost everywhere. The smooth-curve criterion says exactly that $b_q\geq0$, each $b_q$ is nonincreasing, and

\[
 \sum_q b_q(0+)\leq V,\qquad
 \varphi(t\operatorname{ord}_q)=a-\int_0^t b_q(s)\,ds.
\]

The endpoint value is the limit as $t\to\infty$, possibly $-\infty$. There are at most countably many nonconstant rays: their positive initial slopes have finite sum. Sums over $q$ mean the supremum over finite subsets. Define

\[
 D(\varphi)=\sum_q\int_0^\infty b_q(t)^2\,dt\in[0,\infty].
\]

For a PL potential, the raw model measure is $V\delta_o+\Delta\varphi$, by [BJ, Example 3.19] on $Y$ and the model normalization projection formula on $X$. Integration by parts on its finitely many rays yields

\[
 E_X(\varphi)=\frac1{2V}\int\varphi\,d(\mathrm{MA}^{\rm raw}_{X,L}(\varphi)+V\delta_o)
 =a-\frac{D(\varphi)}{2V}.
\]

This is the normalized intersection energy. The boundary term at infinity is zero for PL functions, which are eventually constant; the terms at the root are included in $V\delta_o$. Thus no conductor boundary term is omitted.

To extend the formula, approximate the functions $b_q$ from below by nonincreasing step functions with rational heights and rational breakpoints, supported on finite intervals of finitely many rays. Dyadic right-endpoint sampling, dyadic rounding down and increasing truncation give a directed increasing family of such approximants, converging almost everywhere to $b_q$. Their initial-slope sums do not exceed $V$. Their integrals give decreasing PL psh potentials with root value $a$, converging to $\varphi$, including at the endpoints. Real root constants are allowed in PL over $\mathbb R$. Monotone convergence of the squared slopes and the defining decreasing extension of energy give

\[
 E_X(\varphi)=a-\frac{D(\varphi)}{2V},\qquad
 \varphi\in\mathcal E^1(X,L)\Longleftrightarrow D(\varphi)<\infty.
\]

These are also approximations by the actual ample model cone. For clarity, if $f_n\downarrow\varphi$ is a countable PL approximation, choose $h_n\in H_{\rm dom}(X,L)$ with $\|h_n-f_n\|_\infty\leq\epsilon_n=2^{-n}$. Set $c_n=\sum_{j\geq n}(\epsilon_j+\epsilon_{j+1})=3\epsilon_n$. Then $h_n+c_n$ decreases, because $c_n-c_{n+1}=\epsilon_n+\epsilon_{n+1}$, and converges to $\varphi$. The constants are rational, as required for $H_{\rm dom}$. If $D(\varphi)<\infty$, the approximant energies decrease to a finite limit. Alternatively the source permits decreasing nets directly.

For $D(\varphi)<\infty$, every $b_q$ has limit zero at infinity. Define the operator explicitly by

\[
 \mathrm{MA}^{\rm raw}_{X,L}(\varphi)
 =\left(V-\sum_q b_q(0+)\right)\delta_o
   +\sum_q(-db_q)\big|_{(0,\infty)}.
\]

Here $-db_q$ is the positive Stieltjes measure on the $q$-ray, transported to actual $X$; right-continuous representatives are understood. Each ray measure has mass $b_q(0+)$, so the raw mass is exactly $V$. There is no mass at any closed-point endpoint. The countable sum of finite ray measures and the root atom is Radon. Finite partial sums are Radon and their total-variation tails tend to zero.

This is the genuine MA operator, not an independently named inverse measure. For every actual-X PL psh approximant it is the intersection measure, by model pullback and projection. Decreasing extension agrees with the unique operator of [BJ, Theorem 7.18 and Proposition 7.19(iv)]; continuous test functions determine the measures, since actual-X PL functions are dense. The same approximation proves $E_X(\varphi)=E_Y(\nu^*\varphi)$, first by projection for model pairings and then by their decreasing continuity. Consequently pullback identifies the finite-energy spaces, their weak-plus-energy strong topologies, and the genuine operators by

\[
 \mathrm{MA}^{\rm raw}_{X,L}(\varphi)=
 \nu_*\mathrm{MA}^{\rm raw}_{Y,A}(\nu^*\varphi).
\]

No source theorem is used to assume that arbitrary finite-energy potentials on $Y$ descend: Section 4 already proves that fact, and the energy identity now proves preservation of finite energy.

## 6. Exact measure condition and explicit existence and uniqueness

Let $\mu$ be a positive Radon measure on actual $X^{\rm an}$ with raw mass $V$. Each ray minus $o$, including its endpoint, is open. A compact subset of their union meets finitely many rays, by the open cover by those rays. Inner regularity therefore shows that $\mu$ outside $o$ is concentrated on a countable union of rays. In particular this assertion does not assume that a measure is atomic, or supported on one skeleton. Write $\mu_q$ for its restriction to $(0,\infty]$ on the $q$-ray and set

\[
 \tau_q(t)=\mu_q((t,\infty]),\qquad
 D(\mu)=\sum_q\int_0^\infty\tau_q(t)^2\,dt.
\]

The endpoint is included in the tail in this definition. Endpoint mass makes $D(\mu)=\infty$. We will prove the exact identity

\[
 E_X^*(\mu/V)=\frac{D(\mu)}{2V},
\]

with the convention that both sides may be infinite.

For a finite-energy test potential with slope functions $b_q$ and root value $a$, Tonelli's theorem gives

\[
 -\int(\varphi-a)\,d\mu
 =\sum_q\int_0^\infty b_q(t)\tau_q(t)\,dt.
\]

If $D(\mu)<\infty$, Cauchy--Schwarz makes this finite, so every finite-energy potential is integrable for $\mu$. Substitution into the energy formula and completion of the square give

\[
 E_X(\varphi)-V^{-1}\int\varphi\,d\mu
 =V^{-1}\sum_q\int\left(b_q\tau_q-\tfrac12 b_q^2\right)dt
 \leq\frac{D(\mu)}{2V}.
\]

For the opposite inequality choose finitely many rays $F$ and $T<\infty$, and use the continuous psh test potential with root zero and slopes $b_q=\tau_q\mathbf1_{[0,T)}$ for $q\in F$, zero on other rays. Its slope budget is at most $V$, its energy is finite, and it is eventually constant on each active ray. It descends by Section 4. Its objective is exactly

\[
 \frac1{2V}\sum_{q\in F}\int_0^T\tau_q(t)^2\,dt.
\]

Taking the supremum over $F,T$ proves the identity even when $D(\mu)=\infty$. Uniform approximation of these continuous potentials by $H_{\rm dom}(X,L)$ preserves the objective. Conversely decreasing approximation of an arbitrary finite-energy potential and ordinary monotone convergence under the finite measure show that the defining supremum is unchanged by restricting to $H_{\rm dom}$. This proves both the finite-energy condition and its correct raw normalization.

Assume $D(\mu)<\infty$. Then $\mu$ has no endpoint mass. Define the root-normalized solution on actual $X$ by

\[
 \varphi(o)=0,\qquad
 \varphi(t\operatorname{ord}_q)
 =-\int_0^t\tau_q(s)\,ds
 =-\int_{(0,\infty)}\min(t,u)\,d\mu_q(u).
\]

Give each endpoint its decreasing limit. For finite $t$ the integral is finite, because $\tau_q\leq V$. The slopes are nonnegative, nonincreasing and have total initial value $\sum_q\mu_q((0,\infty))\leq V$. The finite-$F,T$ test potentials above decrease to this function. Each is psh on actual $X$, so decreasing closure proves the solution is psh, including usc at $o$ and all endpoints. Its energy is $-D(\mu)/(2V)>-\infty$. The Stieltjes formula gives $-d\tau_q=\mu_q$ on $(0,\infty)$, while the root coefficient is $\mu(\{o\})$. Hence its genuine raw MA measure is exactly $\mu$. This proves existence without a smooth-space solution being assumed to descend.

Conversely any finite-energy solution has no endpoint mass and its slope satisfies $-db_q=\mu_q$, $b_q(\infty)=0$. Thus $b_q(t)=\tau_q(t)$ at every continuity point, and everywhere for right-continuous representatives. Its energy formula forces $D(\mu)<\infty$. The slopes determine the entire potential up to its root value, including endpoint limits. This proves uniqueness modulo one constant and the necessity of the energy condition. It also gives $E_X^*(\mathrm{MA}^{\rm raw}(\varphi)/V)=\varphi(o)-E_X(\varphi)$.

## 7. Required analytic inputs, with each replacement checked

Compactness. The weak topology is pointwise convergence on the common divisorial valuations. Section 4 identifies the two normalized psh cones as homeomorphic topological spaces. The cone on smooth connected $Y$ is compact by [BJ, Theorems 5.20 and 5.11]. Its image is therefore compact on actual singular $X$. The normalization also preserves $\sup\varphi=\varphi(o)$. We have not deleted smoothness from an SNC-model compactness proof; the proved cone identification supplies the replacement in this sector.

Envelopes. The homeomorphism of analytic spaces commutes with usc regularization, and the proved psh bijection identifies all competitors in an envelope. Thus for any bounded-above family and any continuous obstacle $f$,

\[
 \nu^*(\sup_i\varphi_i)^*=(\sup_i\nu^*\varphi_i)^*,\qquad
 \nu^*P_X(f)=P_Y(\nu^*f).
\]

The smooth-curve envelope property of [BJ, Theorem 5.20] now descends. For continuous $f$, $P_Y(\nu^*f)$ is continuous by Lemma 5.17, so $P_X(f)$ is continuous and psh. The same identities apply to bounded-above usc obstacles, with the identically negative-infinite case allowed. Neither normalization alone nor a presumed envelope property on $X$ was sufficient; the PL and psh descent proofs were necessary.

Energy differentiation. For $\varphi,\psi\in\mathcal E^1$, the quadratic energy formula gives, along their psh segment,

\[
 \left.\frac{d}{dt}\right|_{0+}E_X((1-t)\varphi+t\psi)
 =\frac1V\int(\psi-\varphi)\,d\mathrm{MA}^{\rm raw}_{X,L}(\varphi).
\]

The integrals are finite by the slope Cauchy--Schwarz inequality. This supplies segment differentiation directly. For the arbitrary continuous variations used in the variational method, [BJ, Theorem 8.5] gives the downward energy expansion $E_X^\downarrow(\varphi+\epsilon f)=E_X(\varphi)+\epsilon V^{-1}\int f\,d\mathrm{MA}^{\rm raw}(\varphi)+O(\epsilon^2)$ for actual-X PL $f$, uniformly in $\varphi$. It has no smoothness hypothesis. The now-proved envelope property identifies the left side with $E_X(P_X(\varphi+\epsilon f))$. Approximate a general continuous $f$ uniformly by actual-X PL $f_m$. The correct bound is $|f-f_m|\leq\epsilon_m$; monotonicity and constant translation of energy bound the difference of the perturbed energies by $|t|\epsilon_m$. Divide by $t$, use the PL derivative, and let $m\to\infty$. Consequently

\[
 \left.\frac{d}{dt}\right|_0 E_X(P_X(\varphi+tf))
 =V^{-1}\int f\,d\mathrm{MA}^{\rm raw}_{X,L}(\varphi)
 \quad (f\in C^0(X^{\rm an})).
\]

This also proves envelope orthogonality: for continuous $f$ put $u=P_X(f)$ and $g=f-u\geq0$. For $0\leq t\leq1$, every psh function below $u+tg\leq f$ is below $u$, while $u$ itself is a competitor. Hence $P_X(u+tg)=u$. Differentiation yields $\int(f-P_X(f))\,d\mathrm{MA}^{\rm raw}(P_X(f))=0$. Thus both differentiation and its envelope input are present; the explicit inverse construction is not being used in their place.

Comparison. [BJ, Theorem 7.40] applies to actual-X finite-energy potentials and its intersection operator, which Section 5 identifies with the constructed operator. It gives locality on $\{\varphi>\psi\}$ for $\max(\varphi,\psi)$. The maximum remains finite-energy by its slope/energy characterization, or by the cited finite-energy maximum property. Equal total mass and this locality, applied to $\max(\varphi,\psi-\epsilon)$, give

\[
 \int_{\{\varphi<\psi\}}\mathrm{MA}^{\rm raw}(\psi)
 \leq\int_{\{\varphi<\psi\}}\mathrm{MA}^{\rm raw}(\varphi).
\]

Indeed the partition into the two strict-inequality sets first bounds the left side over $\{\varphi<\psi-\epsilon\}$ by the right side over $\{\varphi\leq\psi-\epsilon\}$; both sets increase to $\{\varphi<\psi\}$ as $\epsilon\downarrow0$. Measures ignore the negative-infinite loci of finite-energy potentials; in this curve setting those possible loci are endpoints and have already been proved to have zero MA mass. This is the raw comparison inequality of Theorem 7.44. Uniqueness was also proved independently by the ray slopes.

Continuity and variational maximization. Theorem 7.19 gives decreasing continuity for any finite-energy approximating net, not only the selected step approximants. Proposition 12.7 gives strong continuity with strong potential topology equal to weak convergence plus energy convergence, and strong measure topology equal to weak measure convergence plus $E_X^*$ convergence. The exact psh and energy identifications preserve those topologies. Every finite-energy measure attains its Legendre supremum at the solution: the completed-square inequality in Section 6 is an equality at $b_q=\tau_q$. Thus the corresponding existence assertion also has the variational maximizer it requires. It is not deduced merely from completeness of a space of measures.

Reference dependence. The raw operator depends on the metric, not on the choice of reference used to name its potential. If $\rho$ is a continuous semipositive reference potential, the relative energy of the metric $\varphi$ is $E_{X,\rho}(\varphi-\rho)=E_X(\varphi)-E_X(\rho)$, by the intersection-energy cocycle formula and decreasing extension. Continuous references differ boundedly and identify the same finite-energy metrics. For raw mass $V$,

\[
 E_{X,\rho}^*(\mu/V)=E_X^*(\mu/V)-E_X(\rho)+V^{-1}\int\rho\,d\mu.
\]

The last two terms are finite, so the finite-energy condition is reference independent within this class. Multiplication of a metric by a constant shifts its potential and energy by the same additive constant and leaves both the raw measure and the dual objective unchanged. No singular reference type or nonample class is claimed here.

## 8. A concrete obstruction for a branched singular curve

Let $X$ instead be an integral projective curve with an ordinary node $p$, and let $q_1,q_2$ be the two distinct points above $p$ on its smooth normalization. Retain algebraically closed trivially valued characteristic-zero $k$, an ample $L$, and $V=\deg L$. Let $v=\operatorname{ord}_{q_1}$, viewed as a point of $X^{\rm an}$, and put $\mu=V\delta_v$. This has the required raw mass.

It has finite dual energy on actual $X$. Any actual-X psh potential pulls back to a psh potential on $Y$; the energy is preserved by the model normalization projection formula and decreasing extension [BJ, (7.5)], which do not assert surjectivity of pullback. Therefore

\[
 E_X^*(\delta_v)\leq E_Y^*(\delta_{\operatorname{ord}_{q_1}})=V/2<\infty.
\]

The last equality is Section 6 on the smooth curve, with a raw mass $V$ atom at $t=1$. No arbitrary restriction of a measure has been normalized here.

Suppose $\mathrm{MA}^{\rm raw}_{X,L}(\varphi)=\mu$ for an actual-X finite-energy potential. Its pullback is finite-energy on $Y$. Formula (7.18) identifies the pushforward of its genuine MA with $\mu$. The analytic normalization is injective on finite generic-support ray points, and finite-energy MA has no endpoint mass. Thus the upstairs measure must be precisely $V\delta_{\operatorname{ord}_{q_1}}$. The unique normalized upstairs solution has slope $V$ on the $q_1$-ray up to $t=1$, zero afterwards, and is constant on the $q_2$-ray. Its two endpoint values are consequently $a-V$ and $a$, for some root value $a$. But both endpoints map to the single point $p$ of $X^{\rm an}$; a pulled-back function must have the same value at them. This contradiction proves that the finite-energy operator is not onto all finite-energy measures on this singular curve. It is the explicit obstruction recorded in [BJ, Example 12.11], now with raw mass and descent checked.

Thus a theorem for all singular varieties with only mass and the standard finite-energy condition is false in this framework. A broader branched theory would need a revised range condition, or a changed notion of potentials with an explicitly justified conductor theory. On a disconnected variety, each connected component has its own fixed polarization mass and its own additive constant; one global mass and uniqueness modulo a single constant are insufficient. The positive theorem avoids both issues by integrality and unibranchness.

## 9. Exact remaining original obligations

The following gaps prevent candidate=true. First, no proof is given of the envelope property for an arbitrary higher-dimensional integral unibranch projective variety under retained characteristic-zero hypotheses. In the cached trivial-field source it is Conjecture 5.14, and Theorem 12.8 makes it precisely the missing existence input even though the operator, comparison and downward differentiation already exist there. This source-level statement is not a claim that no later theorem exists outside the authorized caches.

Second, the isolated-ray PL spanning argument is one-dimensional. For a higher-dimensional normalization, the needed cone descent and envelope identity have not been proved. Topological homeomorphism alone does not descend semipositivity, model approximation, energy or variational derivatives. Pulling an ample class back to a positive-dimensional resolution gives a generally nonample class, so a resolution cannot be substituted into an ample-class theorem. No such substitution was made above.

Third, no singular-space finite-energy operator, compactness, envelope, differentiation and comparison package is established here over a nontrivially discretely valued complete field of residue characteristic zero, in arbitrary dimension or for arbitrary finite-energy support. The cached BFJ v1 retains both algebraizability and SNC-support hypotheses. Dropping any of them needs its own exact later input and cannot follow from that v1. The curve theorem above does not dispose of this retained-field residual scope.

Fourth, for non-unibranch varieties the node counterexample requires an explicit corrected admissible-measure range and conductor descent theorem. This draft proves the obstruction and gives no general corrected range. Finally, irreducibility/connectedness and componentwise mass constraints must remain explicit in any wider theorem. These limitations keep the whole original atom open.

## 10. Reproducibility and evidence

The files input-original.json and input.json are byte-identical; assignment-original.txt is the exact assignment string parsed from input.json, and task-original.json is its task object. Run `python3 provenance.py` to reproduce the selected literal source extracts and their application checks, using only the ten authorized caches. Run `python3 make_paper.py` to produce the standalone P16.1-paper.tex from this complete argument. Run `python3 build_and_check.py` to build twice with the existing TeX installation, preserve both actual diagnostic streams and TeX logs, verify retained-input equality, validate the exact status.json key set, and execute the small exact-rational curve checks. Environment information is in environment.json. The checks are symbolic consistency examples and artifact checks, not an exhaustive result or a verification of the theorem.

The proof file and its standalone TeX/PDF contain the complete partial argument and all remaining original obligations. status.json records the partial result with exactly the required five keys. No other campaigns, generated notes, private payloads, external messages, installations, account changes, or heavy computation were used.


# Actual native canonical notes, all fields and support

[
  {
    "id": "n1",
    "summary": "Exact-source audit: BJ already constructs genuine finite-energy MA on singular integral projective varieties over an algebraically closed trivially valued field. Existence is equivalent to the envelope property, conjectured for unibranch varieties in the saved v4. BFJ saved v1 retains smoothness, algebraizability and SNC-support hypotheses.",
    "detailedSummary": "Boucksom–Jonsson 1801.08229v4 supplies energy, finite-energy MA, locality, comparison and downward energy differentiation without smoothness. General surjectivity is equivalent to the envelope property (Theorem 12.8), which also implies unibranchness (Theorem 5.12). Lemma 5.13 assumes envelopes on the target and cannot establish them by circular normalization descent. The supplied BFJ equation PDF is actual v1 and retains function-field algebraizability and SNC-dual-complex support. Boucksom–Eriksson 1805.01016v3 concerns continuous metrics and norms; the synthetic measure-completion theorem does not establish surjectivity from actual singular-space potentials.",
    "text": "The exact saved source Boucksom–Jonsson, Global pluripotential theory over a trivially valued field, arXiv:1801.08229v4, works over an algebraically closed trivially valued field. For integral projective X and ample L, let V=(L^n). Its normalized energy satisfies E(0)=0 and E(φ+c)=E(φ)+c. Its operator is probability-normalized; the genuine raw operator is V MA. The raw measure condition is μ(X^an)=V and sup_{φ∈E¹}[E(φ)−V⁻¹∫φ dμ]<∞.\n\nTheorem 7.18 and Proposition 7.19 construct finite-energy MA, decreasing continuity, raw mass and normalization pushforward on possibly singular X. Theorems 7.40/7.44 give locality and comparison. Theorem 8.5 and Corollary 8.6 differentiate downward energy; identifying that energy with energy of a psh envelope requires envelope regularity.\n\nTheorem A gives an embedding with dense image, with unconditional surjectivity when X is smooth and either characteristic is zero or dimension is at most two. Theorem 12.8 equates surjectivity with the envelope property; Theorem 5.11 equates envelopes with weak compactness. Theorem 5.12 makes unibranchness necessary. Conjecture 5.14 proposes the envelope property for unibranch varieties. Lemma 5.13 assumes envelope properties on classes approaching the target class, so it cannot establish those same properties by normalization.\n\nThe exact background inputs for the curve proof below are Example 2.5 (flag-ideal PL functions on singular X), Example 2.6 (ray generators on smooth curves), Proposition 3.6(vi) (nef reflection for an already descended target PL function), Proposition 3.10 (uniform ample-model approximation in a fixed ample class), Theorem 4.15(iii) and decreasing closure, Example 4.13 (smooth-curve slope criterion), Theorem 5.20 and Lemma 5.17 (smooth envelopes and continuity), Proposition 7.2, equation (7.5) (energy projection), Proposition 7.19, equation (7.18) (genuine MA projection), and Proposition 12.7 (strong continuity). Every new normalization application is proved in n2.\n\nThe supplied 1201.0188 PDF is actual v1. Its watermark is 30 December 2011 although its internal date is 29 October 2018; neither was silently relabelled. Theorem A assumes complete discrete valuation, residue characteristic zero, smooth projective X admitting descent to a one-variable function field completed by K, ample L, raw mass deg_L X, and support on the dual complex of an SNC model. L need not descend. This v1 is not an arbitrary-support finite-energy theorem. The supplied 1201.0187v2 similarly retains smooth projective, discretely valued, residue-characteristic-zero hypotheses for compactness and regularization.\n\n1805.01016v3 is Boucksom–Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. Its Theorem A concerns continuous psh metrics on geometrically reduced projective schemes; Corollary B retains continuity of envelopes. Its continuous energy projection formula is not a finite-energy singular equation theorem. Synthetic 2307.01697v1, Theorem A, establishes density and completeness on the measure side, not actual-potential surjectivity. Pille–Schneider 2209.04879v2, Remark 4.4, distinguishes arbitrary-field finite-energy spaces from the unknown general extended operator. Gubler–Rabinoff 2506.13548v2 explicitly excludes constructing MA from that paper's singular-curve subharmonic results.\n\nAll ten authorized source-cache hashes match the supplied hashes. Twenty-one literal extracts, published proof passages, precise application checks and five fresh PDF-page extractions are retained in source-extracts/source-provenance.json. Saved PDF page 35 was visually checked for Proposition 3.6(vi) and its proof. Run python3 init_workspace.py and python3 provenance.py to reproduce the inventory and extracts. These checks establish provenance, not mathematical correctness. No assertion is made about every later source outside the authorized caches.\n\nArtifacts: /workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Proved partial sector: actual integral projective unibranch curves over algebraically closed trivially valued characteristic-zero k, with ample L. Genuine raw MA is bijective modulo constants onto mass V=deg L measures with finite dual energy; E*(μ/V)=Σ∫μ_q((t,∞])²dt/(2V). All curve normalization and analytic-input descents are proved. The full P16.1 remains unresolved.",
    "detailedSummary": "Actual point ideals on singular X isolate normalization rays after division by their integer orders. This proves PL descent; model-nef reflection then proves psh descent without assuming envelopes on X. Finite normalization preserves the ample degree and energy. Actual-X finite-energy MA is therefore the root-plus-Stieltjes measure, with inverse obtained by integrating measure tails. Squared-tail finiteness is exactly the dual energy condition, excludes endpoint mass, and gives uniqueness modulo one constant. Compactness and envelopes transfer only after the cone isomorphism is proved. Envelope differentiation, comparison, approximation, strong continuity and bounded-reference dependence are checked. The result restricts dimension to one and uses the trivial valuation endpoint.",
    "text": "Theorem, a partial result. Let k be algebraically closed of characteristic zero with the trivial valuation, X an integral projective unibranch k-curve, and L an ample line bundle of degree V>0 on actual X. Integrality retains reducedness and connectedness; the field is complete. Use the canonical trivial metric and normalized intersection energy E(0)=0, E(φ+c)=E(φ)+c. No smoothness or normality of X, reducedness of its conductor, atomicity or skeletal support is assumed. The genuine raw finite-energy MA has mass V and induces a bijection E¹(X,L)/R onto positive Radon μ satisfying μ(X^an)=V and E*(μ/V)=sup_{φ∈E¹}(E(φ)−V⁻¹∫φ dμ)<∞. The published background is precisely scoped in n1.\n\nNormalization and PL descent. The normalization ν:Y→X is finite; Y is smooth because k is perfect and Y is a normal curve. Properness centers every valuation of the common function field. At a closed point q of Y the local DVR makes every nontrivial valuation t ord_q, t>0. The other analytic points are the common trivial root o and closed-support endpoints q∞. Unibranchness gives one q over each p∈X(k), with residue field k. Thus ν^an bijects both generic-support valuations and endpoints. Compactness of the source and Hausdorffness of the target make it a homeomorphism.\n\nLet m_p O_{Y,q}=m_q^{e_p}, where 1≤e_p<∞. Away from q the extended point ideal is the unit ideal. For rational a>0, the actual-X flag-ideal function h_{p,a}=e_p⁻¹ max(log|m_p|,−e_p a) pulls back to −min(t,a) on the q-ray and zero on every other ray. It belongs to PL(X) by BJ Example 2.5. These functions and rational constants span PL(Y) by Example 2.6. Hence ν* identifies PL(X) with PL(Y), also over R. The conductor Ann(ν_*O_Y/O_X) has finite support and may be nonreduced. No arbitrary section or power descent is used; e_p is the point-ideal order, not a conductor exponent. The single branch is essential to this isolated-ray identity.\n\nPolarization and positivity. The quotient in 0→O_X→ν_*O_Y→T→0 has finite length. Tensoring by L^m and comparing linear coefficients of χ(Y,(ν*L)^m) and χ(X,L^m) proves deg_Y ν*L=V. Positive degree on a projective integral curve is ample, so the upstairs polarization is genuinely ample, with no mass multiplier. Canonical reference metrics pull back through local trivializations at centers.\n\nFor a descended PL function, the graph construction gives a projective surjective morphism of test configurations. Pullback preserves nefness. Conversely each vertical curve downstairs is dominated by a curve upstairs, obtained by projective hyperplane cuts; its pullback degree is a positive degree multiple of the downstairs degree. Thus nefness reflects. Common dominating models preserve the model-psh property. This applies BJ Proposition 3.6(vi) after PL descent has been proved. Approximate any psh function on Y decreasingly by H_dom(Y,ν*L). Its PL approximants descend and are nef-psh on actual X; decreasing closure gives psh descent. Ordinary pullback gives the reverse inclusion. Therefore ν* is a psh-cone isomorphism and a weak homeomorphism, since divisorial valuations of the common function field are identified. No envelope property on X has been assumed.\n\nEnergy and operator. Write a=φ(o) and b_q(t)=−φ'_q(t) almost everywhere. The smooth-curve criterion, transported through the proved cone isomorphism, says b_q≥0 is nonincreasing, Σ_q b_q(0+)≤V, and φ_q(t)=a−∫₀ᵗb_q. Endpoints have limiting values, possibly −∞. Only countably many rays are nonconstant. For PL potentials the genuine raw intersection measure is Vδ_o+Δφ. Integration by parts gives E(φ)=a−D(φ)/(2V), where D(φ)=Σ_q∫₀∞b_q². Model energy projection follows from the normalization fundamental-cycle projection formula, so no conductor boundary term is omitted.\n\nApproximate b_q increasingly from below by nonincreasing rational step functions on finitely many rays and bounded intervals, using refining dyadic right-endpoint samples and rounding down. Initial budgets stay ≤V. Their integrals give decreasing PL psh approximants, including at endpoints. Monotone energy extension and monotone convergence prove the same formula for every psh φ. Thus E¹ is exactly D(φ)<∞. Actual ample-model approximation is also available: if f_n↓φ and ||h_n−f_n||∞≤ε_n=2⁻ⁿ, the potentials h_n+3ε_n decrease with the same limit. Proposition 3.10 supplies h_n∈H_dom(X,L) in the fixed ample class.\n\nFinite D forces b_q(∞)=0. Define MA_raw,X(φ)=(V−Σ b_q(0+))δ_o+Σ_q(−db_q)|_(0,∞), transported to actual X. Each positive Stieltjes ray measure has mass b_q(0+); total mass is exactly V and endpoints have no mass. The countable sum is Radon, with total-variation tails tending to zero. It agrees with model intersection MA and therefore with the unique published decreasing finite-energy extension, by density of actual-X PL test functions. Energy projection extends decreasingly, identifying E¹ spaces and yielding MA_raw,X(φ)=ν_*MA_raw,Y(ν*φ). This is genuine MA, not another inverse measure construction.\n\nMeasure energy and inverse. Rays minus o, including endpoints, are disjoint open subsets. A compact subset of their union meets finitely many rays; Radon inner regularity therefore concentrates any finite μ away from o on countably many rays. For raw mass V, let μ_q be its ray restriction and τ_q(t)=μ_q((t,∞]), including possible endpoint mass. Put D(μ)=Σ∫τ_q². Endpoint mass forces D(μ)=∞. Tonelli gives −∫(φ−a)dμ=Σ∫b_qτ_q. If D(μ)<∞, Cauchy–Schwarz proves integrability of every finite-energy potential. Completing the square gives E(φ)−V⁻¹∫φdμ≤D(μ)/(2V).\n\nFor the reverse inequality, use continuous psh tests with slopes τ_q 1_[0,T) on finitely many rays F and zero elsewhere. Their initial budget is ≤V, and their objective is (2V)⁻¹Σ_{q∈F}∫₀ᵀτ_q². Increasing F,T proves E*(μ/V)=D(μ)/(2V), including the infinite case. Uniform H_dom approximation of these tests, and decreasing approximation with monotone integration for E¹ tests, proves equivalence of the two suprema.\n\nWhen D(μ)<∞, define φ(o)=0 and φ_q(t)=−∫₀ᵗτ_q(s)ds=−∫min(t,u)dμ_q(u), with endpoint limits. The finite F,T tests decrease to it, so it is psh on actual X. Its energy is −D(μ)/(2V). Its Stieltjes measures are μ_q and its root coefficient is μ({o}), giving MA_raw(φ)=μ. Conversely any finite-energy solution has −db_q=μ_q and b_q(∞)=0, hence b_q=τ_q. These slopes determine all values, including endpoint limits, up to the root constant. This proves necessity and uniqueness without assuming an upstairs solution descends.\n\nRequired analytic replacements. The weak normalized psh cone on actual X is homeomorphic to the smooth Y cone, compact by BJ Theorems 5.20/5.11. Analytic homeomorphism commutes with usc regularization, and the proved cone bijection identifies every envelope competitor: ν*P_X(f)=P_Y(ν*f). Envelopes and their continuity therefore descend without a circular target-envelope assumption.\n\nThe quadratic energy differentiates along E¹ segments to V⁻¹∫(ψ−φ)MA_raw(φ). BJ Theorem 8.5 gives downward-energy differentiation for actual-X PL variations without smoothness. The proved envelope property identifies downward energy with E(P(φ+tf)). Uniform PL approximation with |f−f_m|≤ε_m bounds perturbed energy errors by |t|ε_m, proving d/dt|₀ E(P(φ+tf))=V⁻¹∫f MA_raw(φ) for every continuous f. For u=P(f), P(u+t(f−u))=u when 0≤t≤1, so differentiation also proves ∫(f−u)MA_raw(u)=0.\n\nBJ locality for finite-energy maxima applies to the identified genuine operator. Equal raw mass and locality for max(φ,ψ−ε), followed by ε↓0, give ∫_{φ<ψ}MA_raw(ψ)≤∫_{φ<ψ}MA_raw(φ). Possible negative-infinite loci here are endpoints with zero MA mass. Published decreasing continuity holds for every finite-energy approximating net, not only the selected steps; Proposition 12.7 gives strong continuity. The cone and energy identifications preserve weak-plus-energy strong potential topology and weak-plus-dual-energy strong measure topology. The completed-square bound is attained by the explicit inverse, establishing actual variational attainment.\n\nFor a continuous semipositive reference ρ, relative energy is E_ρ(φ−ρ)=E(φ)−E(ρ), by the energy cocycle and decreasing extension. Dual energy becomes E*(μ/V)−E(ρ)+V⁻¹∫ρdμ, a finite change. Thus finite energy is independent of these bounded reference changes. Integrality makes one additive real constant the correct uniqueness ambiguity.\n\nThe complete proof and residual obligations are in P16.1-argument.md and standalone P16.1-paper.tex; build/P16.1-paper.pdf has 11 pages. Run bash rerun.sh. Both actual TeX passes returned 0; the final pass has no warnings. Exact rational examples with V=5 give D(μ)=8, E(φ)=−4/5, dual objective 4/5, and both segment-derivative computations 4/5. Point-ideal orders e=1,2,3,7 give the isolated-ray identity. These are finite consistency observations, not proof verification. Actual diagnostics and outputs are in build/, curve-checks.json and checks.json. This theorem restricts dimension to one and uses the trivial field endpoint; it does not complete P16.1.\n\nArtifacts: /workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Nodal obstruction and remaining gaps: raw mass plus standard finite dual energy does not suffice on all singular curves. A mass-V divisorial atom forces unequal normalization endpoint values over a node. Higher-dimensional unibranch envelopes and the discretely valued singular equation package remain unproved; status is partial and candidate=false.",
    "detailedSummary": "On an integral projective nodal curve over algebraically closed trivially valued characteristic-zero k, μ=Vδ_ord(q1) has finite actual-X dual energy at most V/2 but no actual-X finite-energy solution. The unique normalization solution drops by V at one preimage of the node and by zero at the other, contradicting fiber constancy. The draft leaves higher-dimensional PL/psh/conductor descent, unibranch envelopes, the nontrivially discretely valued singular finite-energy package, and a corrected branched-measure range unresolved. Required inputs, proof files, source extracts and twice-run TeX diagnostics are retained.",
    "text": "Let k be algebraically closed, trivially valued and characteristic zero. Let X be an integral projective curve with an ordinary node p, L ample of raw degree V, and q1,q2 its normalization preimages. Put μ=Vδ_v, where v=ord_q1 viewed on X^an. This has the exact required raw mass. Every actual-X psh potential pulls back to Y, and model projection followed by decreasing extension preserves its energy without asserting surjectivity of pullback. Therefore E*_X(δ_v)≤E*_Y(δ_ord_q1)=V/2, by n2's smooth-curve tail calculation at t=1. Thus μ has finite dual energy on actual X.\n\nSuppose μ=MA_raw,X(φ) for φ∈E¹(X,L). Normalization pushforward identifies its upstairs MA. Normalization is injective at finite generic-support ray points, and finite-energy MA has no endpoint mass, so the upstairs measure is exactly Vδ_ord_q1. By n2's slope uniqueness, its potential is a−V min(t,1) on the q1-ray and constant a on the q2-ray. Endpoint values are a−V and a. Both endpoints map to p, whereas a pulled-back function must be constant on that fiber. This contradiction proves failure of surjectivity. No arbitrary restriction of a measure was normalized and no potential descent was assumed. This is the raw-mass obstruction of BJ Example 12.11, with the descent checked.\n\nThe positive theorem consequently retains unibranchness and integrality. On disconnected spaces, polarization masses must be fixed componentwise and uniqueness has a constant per component. On branched singular spaces, standard mass and finite energy are insufficient; a corrected measure range requires an explicit conductor-compatible theory.\n\nThe whole original atom remains unresolved in this draft. The curve generator argument does not prove higher-dimensional PL or psh descent. Topological normalization homeomorphism alone supplies none of semipositivity, approximation, energy preservation for arbitrary upstairs potentials, or envelopes. In the inspected trivial-field source, unibranch envelopes remain Conjecture 5.14, and Theorem 12.8 makes their proof the missing general existence input. This concerns the exact inspected version, not every later theorem outside the authorized caches. Pullback of an ample class to a resolution may be nonample, so no smooth ample-class theorem was silently applied there.\n\nNo singular-space finite-energy equation package is established here over the nontrivially discretely valued residue-characteristic-zero endpoint. The saved BFJ v1 algebraizability and SNC-support assumptions cannot be erased. Higher-dimensional conductor descents and a corrected admissible-measure range for non-unibranch varieties remain unsupplied.\n\nP16.1-argument.md contains the complete partial proof and remaining obligations. P16.1-paper.tex is standalone, and build/P16.1-paper.pdf has 11 pages. input-original.json is byte-identical to input.json; assignment-original.txt retains the exact assignment string; task-original.json retains the task object. status.json has exactly id,status,exact_result,proof_file,concrete_gaps, with status partial. source-extracts/source-provenance.json retains literal primary-source proofs and application checks. Both builds using the existing pdflatex returned 0, with actual diagnostic streams and logs retained. Exact-rational checks passed but do not verify the theorem. Environment and commands are in environment.json and commands.txt; rerun with bash rerun.sh.\n\nNo other campaigns, models, workers, external messaging, installation or heavy computation were used. The requested native model and effort cannot be independently queried or changed through the available runtime tools; no substitute model was invoked. These are unverified drafts. The original P16.1 is not completely proved.\n\nArtifacts: /workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo",
    "support": [
      "n1",
      "n2"
    ]
  }
]

# Exact published source metadata and application checks

{
  "scope": "Only the ten user-authorized public primary-source caches and fresh workspace files.",
  "inventory": [
    {
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
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "checks": {
        "pdf": {
          "bytes": 768011,
          "sha256": "8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 175336,
          "sha256": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
          "matches_supplied": true
        },
        "abstract_html": {
          "bytes": 39974,
          "sha256": "983485b15a5da892c0b29ecb5ebb7280414028bd1333614a0ae8bf5ec888dbde",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref package\nProducer:        pdfTeX-1.40.12\nCreationDate:    Mon Oct 22 10:00:16 2018 UTC\nModDate:         Mon Oct 22 10:00:16 2018 UTC\nCustom Metadata: yes\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           49\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       768011 bytes\nOptimized:       no\nPDF version:     1.5\n",
      "pdfinfo_returncode": 0
    },
    {
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
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "checks": {
        "pdf": {
          "bytes": 531005,
          "sha256": "4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 161436,
          "sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
          "matches_supplied": true
        },
        "abstract_html": {
          "bytes": 40180,
          "sha256": "e4683a68defd5887b5952cddcccc9f625a2d0391819a97f32a15d4d51f5409ae",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref package\nProducer:        dvips + GPL Ghostscript GIT PRERELEASE 9.22\nCreationDate:    Mon Oct 29 08:53:08 2018 UTC\nModDate:         Mon Oct 29 08:53:08 2018 UTC\nCustom Metadata: no\nMetadata Stream: yes\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           47\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       531005 bytes\nOptimized:       no\nPDF version:     1.4\n",
      "pdfinfo_returncode": 0
    },
    {
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
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "checks": {
        "pdf": {
          "bytes": 1034400,
          "sha256": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 344553,
          "sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
          "matches_supplied": true
        },
        "abstract_html": {
          "bytes": 41303,
          "sha256": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref\nProducer:        dvips + GPL Ghostscript GIT PRERELEASE 9.22\nCreationDate:    Mon Jan 11 01:44:16 2021 UTC\nModDate:         Mon Jan 11 01:44:16 2021 UTC\nCustom Metadata: no\nMetadata Stream: yes\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           99\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       1034400 bytes\nOptimized:       no\nPDF version:     1.4\n",
      "pdfinfo_returncode": 0
    },
    {
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
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "checks": {
        "pdf": {
          "bytes": 1627763,
          "sha256": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 506945,
          "sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
          "matches_supplied": true
        },
        "abstract_html": {
          "bytes": 39270,
          "sha256": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref\nProducer:        pdfTeX-1.40.21\nCreationDate:    Thu Mar 24 01:33:09 2022 UTC\nModDate:         Thu Mar 24 01:33:09 2022 UTC\nCustom Metadata: yes\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           143\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       1627763 bytes\nOptimized:       no\nPDF version:     1.5\n",
      "pdfinfo_returncode": 0
    },
    {
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
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "checks": {
        "pdf": {
          "bytes": 788875,
          "sha256": "979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 167662,
          "sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
          "matches_supplied": true
        },
        "abstract_html": {
          "bytes": 39123,
          "sha256": "95e379bf14e7779de66bca6e020525202fc32bdb575bd1196934cf6ee43eb11a",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref\nProducer:        pdfTeX-1.40.25\nCreationDate:    Thu Jul  6 01:29:52 2023 UTC\nModDate:         Thu Jul  6 01:29:52 2023 UTC\nCustom Metadata: yes\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           48\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       788875 bytes\nOptimized:       no\nPDF version:     1.5\n",
      "pdfinfo_returncode": 0
    },
    {
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
      "origin": "Publicly available primary mathematical source; no generated research payload.",
      "checks": {
        "pdf": {
          "bytes": 633342,
          "sha256": "55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 185043,
          "sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
          "matches_supplied": true
        },
        "abstract_html": {
          "bytes": 40370,
          "sha256": "1b719dcc2de6a7437184f28dbaf37384bf39673fc8b66a35a4dc716f0cba5341",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           \nSubject:         \nKeywords:        \nAuthor:          \nCreator:         LaTeX with hyperref\nProducer:        dvips + GPL Ghostscript GIT PRERELEASE 9.22\nCreationDate:    Mon Mar 20 01:00:14 2023 UTC\nModDate:         Mon Mar 20 01:00:14 2023 UTC\nCustom Metadata: no\nMetadata Stream: yes\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           48\nEncrypted:       no\nPage size:       595 x 842 pts (A4)\nPage rot:        0\nFile size:       633342 bytes\nOptimized:       no\nPDF version:     1.4\n",
      "pdfinfo_returncode": 0
    },
    {
      "public_source": "https://arxiv.org/pdf/2506.13548v2",
      "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
      "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
      "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "origin": "Published primary mathematical source, not generated research.",
      "checks": {
        "pdf": {
          "bytes": 473505,
          "sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 153456,
          "sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           Classically psh and pluriharmonic functions on Berkovich spaces\nAuthor:          Walter Gubler; Joseph Rabinoff\nCreator:         arXiv GenPDF (tex2pdf:)\nProducer:        pikepdf 8.15.1\nCustom Metadata: yes\nMetadata Stream: yes\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           40\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       473505 bytes\nOptimized:       no\nPDF version:     1.7\n",
      "pdfinfo_returncode": 0
    },
    {
      "public_source": "https://theses.hal.science/tel-00010990v1/document",
      "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
      "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
      "literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
      "extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
      "origin": "Published primary mathematical source, not generated research.",
      "checks": {
        "pdf": {
          "bytes": 1507314,
          "sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 679353,
          "sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           These_AT2.dvi\nCreator:         dvips(k) 5.94a Copyright 2003 Radical Eye Software\nProducer:        AFPL Ghostscript 8.51\nCreationDate:    Tue Nov 15 18:12:28 2005 UTC\nModDate:         Tue Nov 15 18:12:28 2005 UTC\nCustom Metadata: no\nMetadata Stream: no\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           198\nEncrypted:       no\nPage size:       612 x 792 pts (letter)\nPage rot:        0\nFile size:       1507314 bytes\nOptimized:       no\nPDF version:     1.4\n",
      "pdfinfo_returncode": 0
    },
    {
      "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
      "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
      "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
      "literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
      "extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
      "origin": "Published primary mathematical source, not generated research.",
      "checks": {
        "pdf": {
          "bytes": 19118239,
          "sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 418614,
          "sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           Étale cohomology for non-Archimedean analytic spaces\nSubject:         © Publications mathématiques de l'I.H.É.S.\nKeywords:        Fourni dans le cadre du programme NUMDAM\nAuthor:          Vladimir G. Berkovich\nCreator:         NUMDAM\nProducer:        pdfTeX-1.40.16\nCreationDate:    Mon Oct  6 13:10:10 2025 UTC\nModDate:         Mon Oct  6 13:10:10 2025 UTC\nCustom Metadata: yes\nMetadata Stream: yes\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           158\nEncrypted:       no\nPage size:       600.945 x 841.89 pts\nPage rot:        0\nFile size:       19118239 bytes\nOptimized:       yes\nPDF version:     1.5\n",
      "pdfinfo_returncode": 0
    },
    {
      "public_source": "https://arxiv.org/pdf/1204.6277v2",
      "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
      "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
      "literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
      "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
      "origin": "Published primary mathematical source, not generated research.",
      "checks": {
        "pdf": {
          "bytes": 4659053,
          "sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
          "matches_supplied": true
        },
        "literal_extract": {
          "bytes": 2153101,
          "sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
          "matches_supplied": true
        }
      },
      "pdfinfo": "Title:           Formes diff\\'erentielles r\\'eelles et courants sur les espaces de Berkovich\nAuthor:          Antoine Chambert-Loir; Antoine Ducros\nCreator:         arXiv GenPDF (tex2pdf:)\nProducer:        pikepdf 8.15.1\nCustom Metadata: yes\nMetadata Stream: yes\nTagged:          no\nUserProperties:  no\nSuspects:        no\nForm:            none\nJavaScript:      no\nPages:           608\nEncrypted:       no\nPage size:       595.276 x 841.89 pts (A4)\nPage rot:        0\nFile size:       4659053 bytes\nOptimized:       no\nPDF version:     1.5\n",
      "pdfinfo_returncode": 0
    }
  ],
  "extracts": [
    {
      "id": "bj-curve-topology",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 622,
      "line_end": 655,
      "character_start": 45188,
      "source_locator": "Section 1.1.6, pp. 13-14",
      "pdf_page_range_from_formfeeds": [
        13,
        14
      ],
      "literal_file": "source-extracts/bj-curve-topology.txt",
      "literal_sha256": "156873747ad733d6d9f528bbc118a6ee406abf98c792fd6d6ae0dedcba7ccd6f",
      "literal_extract": "                          tv ≤ vZ,triv =⇒ ϕ(tv) ≥ ϕ(vZ,triv ) = sup ϕ,\n                                                                     Z an\nsince ϕ is decreasing, and lim supt→+∞ ϕ(tv) ≤ ϕ(vZ,triv ), since ϕ is usc.                      \u0003\n1.1.6. The Berkovich analytification of a curve. Here we describe X an in the case when X\nis a curve, i.e. of pure dimension one. We may and will assume X is connected.\n   If X is smooth, then X an is a star-shaped R-tree rooted at vtriv , see Figure 1. Further,\nthe Berkovich topology coincides with the weak tree topology as defined in [FJ04, §3.1.4]\nor [Jon12, §2.1.1], for example.\n   More specifically, each closed point p ∈ X(k) determines a compactified ray ιp : [0, +∞] ,→\nX an , with ιp (0) = vtriv , ιp (t) = t ordp for t ∈ (0, +∞), and ιp (+∞) = vp,triv . The half-open\nrays ιp ((0, +∞]) = c−1 (p) form an open partition of X an \\ {vtriv }, and we have\n                                                                                     a\n  X an = X val t X(k), X triv = X(k) = X(k) t {vtriv }, X div = {vtriv } t               ιp (Q>0 ).\n                                                                                p∈X(k)\n\n   A neighborhood basis of vtriv is formed by complements of the union of finitely many\nsegments ιpj ([tj , +∞], where tj ∈ R>0 . In particular, every neighborhood of vtriv contains\nat least one (in fact, infinitely many) compactified rays; this prevents X val from being locally\nclosed in X an , and X val is therefore not locally compact.\n\f14                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n  In the general case, let (Xα ) be the irreducible components of X. Then the normalization\nmorphism X ν → X induces a surjective map\n                                             a\n                                   X ν, an =   Xαν,an → X an\n                                               α\n  that identifies the endpoints vpi ,triv of all rays corresponding to a point pi ∈ ν −1 (p),\np ∈ X(k).\n\n\n\n                                                                    ordp1\n                             ordp\n                                     vp,triv                                  vp,triv\n",
      "application_check": "Only the curve topology is used. The analytic normalization homeomorphism in the unibranch case is proved independently in the argument."
    },
    {
      "id": "bj-flag-ray-generators",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 968,
      "line_end": 1028,
      "character_start": 69286,
      "source_locator": "Definition 2.1, Example 2.5, Example 2.6, pp. 21-22",
      "pdf_page_range_from_formfeeds": [
        20,
        22
      ],
      "literal_file": "source-extracts/bj-flag-ray-generators.txt",
      "literal_sha256": "0fcd3b6bfc93bc3a72ea10a0b110cb08a51a0e688032a04eea6f8f99228a8c1a",
      "literal_extract": "                            ϕa·a0 = ϕa + ϕa0 ,        ϕa+a0 = max{ϕa , ϕa0 }.                   (2.4)\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      21\n\nDefinition 2.1. We define the space of piecewise linear (PL) functions on X an as the\nQ-linear subspace\n                                      PL(X) ⊂ C0 (X)\ngenerated by all functions ϕa attached to flag ideals a.\n  By (2.4), the subset\n                    PL+ (X) := m−1 ϕa | m ∈ Z>0 , a flag ideal ⊂ PL(X)\n                              \b\n                                                                                           (2.5)\n    is stable under sums and finite maxima, and contains all Q-valued constant functions. It\nis also stable under multiplication by Q+ : if c ∈ Q+ , then cϕa = m−1 ϕamc for any m ∈ Z>0\nis such thatP mc ∈−λZ. Further, it is stable     under the scaling action of Q>0 : if t ∈ Q>0\n                                         −1 ϕ 0 , where m ∈ Z\nand a =         aλ $   , then t · ϕ a = m    a                  >0 is such that mt ∈ Z, and\n  0\n       P m λ −mtλ\na = λ aλ $           .\n    It follows that the Q-vector space PL(X) is stable under finite maxima and minima, and\nunder the scaling action of Q>0 , and it contains all constant Q-valued functions. Further,\nany function in PL(X) can be written as a difference of functions in PL+ (X), and is Q-valued\non X div .\n    We refer to Theorem 2.7 and Appendix A for an interpretation of PL functions in terms\nof test configurations and PL functions on simplicial complexes, respectively. In our setting,\nPL functions play the role of smooth functions in the complex analytic case, as illustrated\nby the next result.\nTheorem 2.2. The space PL(X) is dense in C0 (X) for the topology of uniform convergence.\n  By the ‘lattice version’ of the Stone–Weierstrass theorem, this is a direct consequence of\nthe following result.\nLemma 2.3. The Q-linear subspace PL(X) ⊂ C0 (X) is stable under max (and hence min),\ncontains the constants in Q, and separates the points of X an .\nProof. The first two properties are clear. As mentioned in §1.1, the topology of X an is\ngenerated by the functions log |b| attached to ideals b ⊂ OX . For any two v, v 0 ∈ X an we\ncan thus find an ideal b such that log |b|(v) 6= log |b|(v 0 ) (since X an is Hausdorff), and it\nfollows that ϕ := max{log |b|, −m} ∈ PL(X) separates v, v 0 for m \u001d 1.                        \u0003\nRemark 2.4. We will occasionally consider the R-vector space PL(X)R ⊂ C0 (X) generated\nby PL(X). As opposed to the latter, PL(X)R is not closed under max.\nExample 2.5. Given a closed subscheme Z ⊂ X with ideal b ⊂ OX , the function\n                                   ϕZ := max{log |b|, −1}\n          +\nlies in PL (X), since ϕZ = ϕa with a = b + ($). Note that\n                                   t · ϕZ = max{log |b|, −t}                               (2.6)\nfor all t ∈ Q>0 .\nExample 2.6. Assume X is a smooth irreducible curve, and recall the description of X an\nin §1.1.6. As a special case of Example 2.5, each p ∈ X(k) defines a function ϕp ∈ PL+ (X)\nthat satisfies for all q ∈ X(k) and t ∈ [0, +∞]\n                                        \u001a\n                             ?            max{−t, −1} if q = p;\n                            ιq ϕp (t) =\n                                          0            otherwise.\n\f22                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n                                                                                        P\nUsing (2.6) and the fact that every nontrivial ideal of X is of the form b = OX (− i ai pi )\nfor a finite set (pi ) in X(k) and ai ∈ Z>0 , one checks that the functions t · ϕp with t ∈ Q>0\nand p ∈ X(k) span PL(X). A function ϕ ∈ C0 (X) is PL iff ϕ is constant on all but finitely\nmany rays of X an and Q-PL on these rays, and ϕ ∈ PL+ (X) iff ϕ is further convex (and\nhence decreasing, being bounded) on each ray.\n2.2. PL functions and test configurations. Let X be a test configuration for X, and\nrecall that Gauss extension of (semi)valuations yields an embedding σX : X an ,→ X an onto\nthe set of k × -invariant semivaluations w ∈ X an such that w(X0 ) = w($) = 1.\n",
      "application_check": "Example 2.5 allows any ideal on a projective variety; the point ideal on singular X is therefore allowed. The spanning claim in Example 2.6 is applied only to smooth normalization Y. The new proof uses the ramification integer e_p to descend every generator."
    },
    {
      "id": "bj-model-nef-descent-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 1610,
      "line_end": 1692,
      "character_start": 113749,
      "source_locator": "Definition 3.2 and Proposition 3.6 with proof, pp. 34-35",
      "pdf_page_range_from_formfeeds": [
        34,
        36
      ],
      "literal_file": "source-extracts/bj-model-nef-descent-proof.txt",
      "literal_sha256": "9b6eecd1ed9234fae0fe0e52c7185abdb74795dd2901f149e9d5ae0fb64c3052",
      "literal_extract": "Definition 3.2. We say that a function ϕ ∈ PLR is θ-plurisubharmonic ( θ-psh for short)\nif it is determined by a divisor D ∈ VCar(X )R on a test configuration X dominating Xtriv\nsuch that θX + D ∈ Nef(X /A1 ).\n   We sometimes also say that the pair (θ, ϕ) ∈ N1 (X) × PLR is psh. Here θX + D denotes,\nslightly abusively, the sum of θX and of the image of D in N1 (X /A1 ).\n   This definition is independent of the choice of X . Indeed, for any morphism of test\nconfigurations µ : X 0 → X , we have\n                                   θX 0 + µ? D = µ? (θX + D) ,\nwhich is thus nef iff θX +D is nef. Restricting to X1 ≃ X further shows that a θ-psh function\nin PLR can only exist when θ ∈ Nef(X).\n   We will use the notation\n                              PLR ∩ PSH(θ)     and    PL ∩ PSH(θ)\nfor the sets of θ-psh functions in PLR and PL, respectively. At this point, the notation is\npurely formal, but it will be justified in §4, by defining the set PSH(θ).\n   When θ = c1 (L) ∈ N1 (X) is the numerical class of L ∈ Pic(X)Q on X, we simply speak\nof L-psh functions. By Theorem 2.31, we have:\nExample 3.3. For any Q-line bundle L on X, L 7→ ϕL sets up a 1–1 correspondence\nbetween the set of semipositive non-Archimedean metrics in the sense of [BHJ17, Defini-\ntion 6.4], i.e. equivalence classes of nef test configurations L for L, and PL ∩ PSH(L). By\nTheorem 2.31 (ii), we thus have H(L) ⊂ PL ∩ PSH(L), the inclusion being strict in general.\nRemark 3.4. Following [BFJ16, BFJ15] we could define a closed (1, 1)-form on X an to be\nan element η ∈ limX N1 (X /A1 ), and declare a function ϕ ∈ PLR to be η-psh if it is of the\n                −→\nform ϕ = ϕD , with D ∈ VCar(X )R such that η + D is nef. In this paper we only consider\nthe case when η ∈ N1 (Xtriv /A1 ) is determined by the pullback of a class θ ∈ N1 (X).\n     As a direct consequence of the fact that Nef(X /A1 ) ⊂ N1 (X /A1 ) is closed, we have:\nLemma 3.5. Let θi → θ be a convergent sequence in N1 (X). Pick ϕ, ψ ∈ PLR , and assume\nthat ϕ + ci ψ is θi -psh for a sequence ci → 0. Then ϕ is θ-psh.\nProposition 3.6. Pick θ, θ0 ∈ N1 (X), and assume that ϕ, ϕ0 ∈ PLR are θ-psh and θ0 -psh,\nrespectively. Then:\n    (i) ϕ + ϕ0 is (θ + θ0 )-psh, and tϕ is tθ-psh for all t ∈ R>0 ;\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        35\n\n    (ii) for each c ∈ R and t ∈ Q>0 , ϕ + c and t · ϕ are θ-psh;\n   (iii) if θ = θ0 and ϕ, ϕ0 ∈ PL, then max{ϕ, ϕ0 } ∈ PL is θ-psh;\n   (iv) ϕ is decreasing with respect to the partial order on X an , and hence satisfies (1.4)\n         (see Lemma 1.4);\n    (v) for any morphism f : Y → X from a projective variety, f ? ϕ is f ? θ-psh;\n   (vi) if we further assume that f : Y → X is surjective, then\n                   ϕ θ-psh ⇐⇒ ϕ|Xαan θ|Xα -psh for all α ⇐⇒ f ? ϕ f ? θ-psh.\n  In particular, (i) shows that PLR ∩ PSH(θ) is a convex subset of PLR .\nLemma 3.7. For any θ ∈ N1 (X) and ϕ ∈ PLR ∩ PSH(θ), there exists a sequence ϕm ∈\nH(Lm ) with Lm ∈ Pic(X)Q such that ϕm → ϕ uniformly on X an and c1 (Lm ) → θ.\nProof. Pick a test configuration X dominating Xtriv and D ∈ VCar(X )R such that ϕ = ϕD .\nBy openness of the (relatively) ample cone of N1 (X /A1 ), we can find a sequence of Q-\nline bundles Lm on X and Dm ∈ VCar(X )Q such that c1 (Lm ) → θ in N1 (X), Dm → D\nin VCar(X )R , and c1 (Lm )X + Dm ∈ N1 (X /A1 ) is ample for all i. In particular, Lm :=\n(Lm )X +Dm is a semiample test configuration for L, and hence ϕm := ϕLm = ϕDm ∈ H(Lm ).\nFurthermore, Dm → D implies ϕm → ϕ uniformly.                                          \u0003\nProof of Proposition 3.6. Pick a test configuration X dominating Xtriv and D, D0 ∈ VCar(X )R\nthat determine ϕ, ϕ0 . By assumption, θX + D and θX   0 + D 0 are nef. Thus\n\n       (θ + θ0 )X + D + D0 = (θX + D) + θX   0\n                                               + D0\n                                                    \u0001\n                                                        and (tθ)X + tD = t (θX + D)\nare nef as well, proving (i).\n   For each c ∈ R we have ϕ + c = ϕD+cX0 . Since X0 = π ? (0) vanishes in N1 (X /A1 ),\nθX + D + cX0 is nef, and ϕ + c is thus θ-psh. To prove the remaining part of (ii), it suffices to\nprove that if d ∈ Z>0 , then ϕ is θ-psh iff d · ϕ is θ-psh. In view of Lemma 2.34, this follows\nfrom the fact that θX + D ∈ N1 (X /A1 ) is nef iff its pullback under the base change of X\nwith respect to $ 7→ $d is nef.\n   Assume now θ = θ0 and D, D0 ∈ VCar(X )Q . By openness of Amp(X), we can find an\nQ-line bundle L on X such that c1 (L) − θ is ample and arbitrarily small. Then ϕ, ϕ0 are\nL-psh, and it will be enough to show that max{ϕ, ϕ0 } is L-psh as well, by Lemma 3.5. After\nperhaps passing to a higher test configuration, we may assume that X supports an ample\ntest configuration L for L (Lemma 2.33). For each ε ∈ Q>0 , the Q-line bundle LX + D + εL\nis ample, and hence semiample. Thus ϕ + εϕL is Fubini–Study for (1 + ε)L, and similarly\nfor ϕ0 + εϕL . By Proposition 2.19, it follows that\n                        max{ϕ + εϕL , ϕ0 + εϕL } = max{ϕ, ϕ0 } + εϕL\nis Fubini–Study for (1 + ε)L, and hence (1 + ε)L-psh. Using Lemma 3.5 we conclude, as\ndesired, that max{ϕ, ϕ0 } is L-psh. This proves (iii).\n    By Proposition 2.19, any Fubini–Study function is decreasing, and (iv) thus follows from\nLemma 3.7.\n    To prove (v), note that the Gm -equivariant rational map Y × Gm 99K X induced by f\nadmits a Gm -equivariant resolution of indeterminacies, which is thus a test configuration Y\nfor Y dominating Ytriv . Also denoting by f : Y → X the corresponding morphism, we have\nf ? ϕ = ϕf ? D , and the result thus follows from the fact that θY + f ? D = f ? (θX + D) is nef,\nas the pullback of a nef class. If f : Y → X is surjective, then f : Y → X is surjective as\nwell, and (vi) follows.                                                                        \u0003\n\f36                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n   Given a test configuration π : X → A1 , we denote by Amp(X /A1 ) ⊂ Nef(X /A1 ) the set\n",
      "application_check": "Proposition 3.6(vi) applies to an already descended PL function. Normalization is finite, projective and surjective; the argument first proves the necessary PL descent and separately explains nef reflection via degrees of vertical curves."
    },
    {
      "id": "bj-pl-approximation",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 1707,
      "line_end": 1742,
      "character_start": 120720,
      "source_locator": "Proposition 3.10 with proof, p. 36",
      "pdf_page_range_from_formfeeds": [
        36,
        37
      ],
      "literal_file": "source-extracts/bj-pl-approximation.txt",
      "literal_sha256": "4362b9bf818f561810922ae476274d3eeeec7c1dbafd095292364ce2e2a598c6",
      "literal_extract": "Proposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of\nfunctions in Hdom (ω).\nLemma 3.11. For any ω ∈ Amp(X), the set of test configurations X dominating Xtriv such\nthat there exists H ∈ VCar(X )Q with ωX + H ∈ Amp(X /A1 ) is cofinal in the set of all test\nconfigurations.\nProof. By Lemma 1.8, any test configuration for X is dominated by a test configuration X\nwith a morphism µ : X → Xtriv such that VCar(X )Q contains a µ-ample divisor A. Since\nωXtriv ∈ N1 (Xtriv /A1 ) is ample, ωX + εA = µ? ωXtriv + εA ∈ N1 (X /A1 ) is ample for ε ∈ Q>0\nsmall enough, and setting H := εA yields the result.                                        \u0003\nProof of Proposition 3.10. Pick any ϕ ∈ PLR ∩ PSH(ω), and write ϕ = ϕD for some D ∈\nVCar(X )R , where X is an integrally closed test configuration. Thus ωX + D ∈ N1 (X /A1 ) is\nnef. By Lemma 3.11 we may assume that there exists P    H ∈ VCar(X )PR such that ωX + H is\nample. Pick a basis (Ci ) for VCar(X )Q and write D = i ci Ci , H = i c0i Ci with ci , c0i ∈ R.\n                                  1                                                          1\nFor m \u001d 1, the class ωX + D + m     H ∈ N1 (X /A1 ) is ample, and we can pick εm,i ∈ (0, m     )\n                    P          0\n                              ci\nsuch that if Dm := i (ci + m + εm,i )Ci , then Dm ∈ VCar(X )Q and ωX + Dm is ample. It\n                                                     1\nfollows that ϕDm ∈ Hdom (ω), and that ϕDm − ϕ = m\n                                                             P\n                                                       ϕH + i εm,i ϕCi tends to 0 uniformly\non X an .                                                                                     \u0003\n3.2. The energy pairing. Recall that every test configuration π : X → A1 admits a canon-\nical compactification π : X̄ → P1 . If X dominates Xtriv , then any θ ∈ N1 (X) pulls back to a\nclass θX̄ ∈ N1 (X̄ ), whose image in N1 (X /A1 ) coincides with θX considered above.\n   Pick an (n + 1)-tuple of pairs (θi , ϕi ) ∈ N1 (X) × PLR , i = 0, . . . , n, and choose a test\nconfiguration X dominating Xtriv and divisors Di ∈ VCar(X )R that determined the ϕi .\nFollowing [BHJ17, Definition 6.11], we introduce:\nDefinition 3.12. The energy pairing takes an (n+1)-tuple of pairs (θi , ϕi ) ∈ N1 (X)×PLR ,\ni = 0, . . . , n to\n                                                                 \u0001                    \u0001\n                    (θ0 , ϕ0 ) · . . . · (θn , ϕn ) := θ0,X̄ + D0 · . . . · θn,X̄ + Dn ∈ R. (3.3)\n\f                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                             37\n\n  The right-hand side is an intersection number against the fundamental class\n",
      "application_check": "The fixed class is ample on actual X. Descended nef PL functions are uniformly approximable by Hdom(X,L); a decreasing diagonal approximation is given explicitly in the argument."
    },
    {
      "id": "bj-curve-psh-and-regularization",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 2387,
      "line_end": 2436,
      "character_start": 167163,
      "source_locator": "Example 4.13 and Theorem 4.15, pp. 49-50",
      "pdf_page_range_from_formfeeds": [
        49,
        50
      ],
      "literal_file": "source-extracts/bj-curve-psh-and-regularization.txt",
      "literal_sha256": "d002d19e98d355f6044ba5802bff1ead54a2c969502237f8646afcb0aeac63e2",
      "literal_extract": "        holds; in particular,\n                                    sup ϕ = max ϕ(vtriv,α ).                               (4.6)\n                                              α\n   (iii) for any v ∈ X an , t 7→ ϕ(tv) is convex and decreasing on [0, +∞), and ϕ(tv) &\n         ϕ(vZ,triv ) = supZ an ϕ as t → +∞, with Z the closure of the center of v.\n                                           gf\nProof. By Proposition 2.19 (i), each ϕi ∈ HR  (Li ) is decreasing, and t 7→ ϕi (tv) is convex,\nby Lemma 2.20. Since (ϕi ) converges pointwise to ϕ, the latter inherits these properties.\nThe rest follows from Lemma 1.4.                                                            \u0003\nExample 4.13. Let X be a smooth irreducible curve, and recall the description of X an given\nin §1.1.6. For any θ ∈ N1 (X), a usc function ϕ : X an → R ∪ {−∞} is then θ-psh iff\n    (i) for each p ∈ X(k), ϕp (t) := ϕ(t ordp ) is convex on [0, +∞) (and hence decreasing,\n        being bounded  above);\n   (ii) deg θ + p∈X(k) ϕ0p (0+ ) ≥ 0 (which implies ϕ0p (0+ ) = 0, and hence t 7→ ϕ(t ordp )\n                P\n\n        constant, for all but countably many p ∈ X(k)).\nIndeed, when ϕ is PL, this follows from Example 3.21, and the general case is obtained by\nwriting a function satisfying (i) and (ii) as a decreasing limit of PL functions with the same\nproperties (compare [FJ04, §7] and [Jon12, §2.5]).\n  This characterization implies PSH(0) = R when X is a smooth irreducible curve. As in\nthe complex analytic case, this holds in fact on any connected variety, see Corollary 4.24\nbelow.\nRemark 4.14. Any ϕ ∈ PL(X)R is η-psh with respect to some closed (1, 1)-form η, in the\nsense of Remark 3.4. However, ϕ is in general not θ-psh for any θ ∈ N1 (X), since such\nfunctions must be decreasing in the partial ordering on X an (see Proposition 4.12 ). As a\nresult, several potential definitions of quasi-psh functions coexist in our context.\n4.3. The regularization theorem. Many properties of θ-psh functions are obtained by\nregularization, that is, approximation by nicer θ-psh functions. In our present approach,\nregularization of θ-psh functions is built into their definition. One can, however, improve\nthe properties of the approximants as follows:\nTheorem 4.15. Pick θ ∈ N1 (X) and ϕ ∈ PSH(θ). Then:\n                                                                   gf\n     (i) ϕ can be written as the limit of a decreasing net ϕi ∈ HQ    (Li ) with Li ∈ Pic(X)Q\n         such that c1 (Li ) − θ is ample and limi c1 (Li ) = θ;\n    (ii) if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;\n   (iii) if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in\n         Hdom (ω) (see Definition 3.8).\n\f50                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n   We shall later prove that these results actually hold with (countable) sequences instead\nof nets, see Corollary 12.18.\n   As already indicated by (iii), the class of θ-psh functions has particularly good properties\nwhen θ ∈ Amp(X) is ample. In this case, we typically write ω instead of θ.\nCorollary 4.16. For any ω ∈ Amp(X), the space CPSH(ω) = C0 (X) ∩ PSH(ω) is the\nclosure of Hdom (ω) ⊂ C0 (X) in the topology of uniform convergence.\nProof. By Theorem 4.7, CPSH(ω) is closed in the topology of uniform convergence. By\nTheorem 4.15 and Dini’s lemma, any ϕ ∈ CPSH(ω) is the uniform limit of a net in Hdom (ω),\nand the result follows.                                                                \u0003\nCorollary 4.17. For any θ ∈ N1 (X) and any ϕ ∈ PSH(θ) we have ϕ > −∞ on X lin .\n",
      "application_check": "The convex ray and slope-budget criterion is applied to smooth connected Y only. Theorem 4.15(iii) is applied on both X and Y after verifying their ample polarizations."
    },
    {
      "id": "bj-envelope-compactness-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 2812,
      "line_end": 2840,
      "character_start": 197738,
      "source_locator": "Theorem 5.11 with proof, p. 58",
      "pdf_page_range_from_formfeeds": [
        58,
        58
      ],
      "literal_file": "source-extracts/bj-envelope-compactness-proof.txt",
      "literal_sha256": "99cb7383c328a956723836970e3d16090aa3e4e912c51519833252575a43ad70",
      "literal_extract": "\nProof. Pick a bounded-above family (ϕi ) in PSH(θ). Since θ ≤ θj , we have PSH(θ) ⊂\nPSH(θj ). Thus sup?i ϕi is θj -psh for all j, and hence θ-psh, by Theorem 4.5.    \u0003\nCorollary 5.10. If the continuity property holds for all ω ∈ Amp(X), then it holds for all\nθ ∈ Nef(X).\n  We next prove that the envelope property is equivalent to the analogue of a basic com-\npactness property in the complex analytic case.\nTheorem 5.11. For any θ ∈ N1 (X), the following properties are equivalent:\n    (i) the envelope property holds for θ;\n   (ii) the space PSHsup (θ) := {ϕ ∈ PSH(θ) | sup ϕ = 0} is compact;\n  (iii) every bounded-above, increasing net (ϕj ) in PSH(θ) converges in PSH(θ).\nProof. Assume (i), and pick a net (ϕi ) in PSHsup (θ). By Proposition 4.38, (ϕi (v)) is a\nbounded net in R for each v ∈ X div . By Tychonoff’s theorem, after passing to a subnet,\nwe may thus assume that (ϕi ) converges pointwise on X div to a function ϕ : X div → R,\nand it suffices to show that ϕ extends to a function in PSH(θ) (necessarily unique, by\nCorollary 4.23). By (i), ψi := sup?j≥i ϕj is θ-psh for each i. The net (ψi ) is further decreasing,\nand its pointwise limit ψ := limi ψi is thus either θ-psh, or identically −∞, by Theorem 4.5.\nNow Theorem 5.6 implies that ψi = supj≥i ϕj on X div . Thus ψ = ϕ on X div . In particular,\nψ 6≡ −∞, hence ψ ∈ PSH(θ). This proves (i)⇒(ii).\n   Next, assume (ii), and consider a bounded-above, increasing net (ϕj ) in PSH(θ). Then a\nsubnet ϕji −sup ϕji converges to some ϕ ∈ PSH(θ). Since (sup ϕj ) is increasing and bounded-\nabove, it converges to some c ∈ R. Thus ϕji → ϕ + c on X div , and hence ϕj → ϕ + c on\nX div since (ϕj ) is increasing. This proves (ii)⇒(iii).\n   Finally, assume (iii). Let (ϕi )i∈I be a bounded-above family of θ-psh functions, and\nconsider the increasing net ψJ := maxi∈J ϕi parametrized by finite subsets J ⊂ I. Then ψJ\nadmits a limit ψ in PSH(θ), and we claim that ψ = sup?i ϕi . On X div we have\n                              ψ = lim max ϕi = supi ϕi = sup?i ϕi ,\n                                    J   i∈J\nby Theorem 5.6. Since ψ is θ-psh and sup?i ϕi is usc, Theorem 4.22 yields ψ ≤ sup?i ϕi on\n",
      "application_check": "This is not invoked to obtain psh descent. Once the psh cones are identified, the weak topology and normalized cone are transported, without assuming compactness on singular X."
    },
    {
      "id": "bj-unibranch-gap",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 2843,
      "line_end": 2895,
      "character_start": 200072,
      "source_locator": "Theorem 5.12, Lemma 5.13 with proof, Conjecture 5.14 and Remark 5.15, pp. 58-59",
      "pdf_page_range_from_formfeeds": [
        58,
        59
      ],
      "literal_file": "source-extracts/bj-unibranch-gap.txt",
      "literal_sha256": "d06f627baf60803e60737423db5f02a3d027f1a9d000c4d06042d25306fe7e8f",
      "literal_extract": "   Recall that the variety X is said to be unibranch if the following equivalent conditions\nhold (see [EGA, IV.7.6.3] and [Kol16, Corollary 32]):\n      • the normalization morphism ν : X ν → X is a homeomorphism;\n      • the formal completion of X at each of its points is irreducible.\nIn particular, any normal variety is unibranch. When k = C, X is unibranch iff the associated\ncomplex analytic space is locally irreducible in the analytic topology. This is also true for\nthe Berkovich analytification as considered in this paper: the variety X is unibranch iff\nthe k-analytic space X an is locally irreducible in the analytic topology (see [Duc09, Lemme\n5.19]).\nTheorem 5.12. If the envelope property holds for some ω ∈ Amp(X), then X is necessarily\nunibranch.\n  The analogue of this result is known in the complex analytic setting, too. We have not\nbeen able to locate a precise reference, but the proof below of Theorem 5.12 can easily be\nadapted to that setting.\n\f            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     59\n\nLemma 5.13. Let π : Y → X be a birational morphism. Pick θ ∈ N1 (X), and assume that\nθ can be written as the limit of a sequence of classes θm > θ with the envelope property.\n                  ∼\nThen π ? : PSH(θ) → PSH(π ? θ) is a homeomorphism.\n  Recall that θm > θ means that θm − θ is ample.\n\nProof. After passing to a subsequence, we may assume that θm > θm+1 for all m, and hence\n                                                           ∼\nPSH(θm+1 ) ⊂ PSH(θm ). Since π induces a bijection Y div → X div , π ? : PSH(θ) → PSH(π ? θ)\nis a topological embedding, and it suffices to show that it is onto. Pick ψ ∈ PSH(π ? θ), and\nwrite π as the blowup of an ideal b ⊂ OX . By Theorem 4.32, there exists a sequence εm & 0\nsuch that ψ + εm π ? log |b| = π ? ϕm with ϕm ∈ PSH(θm ). By Theorem 4.22, ϕm is uniquely\ndetermined, and (ϕm )m≥m0 is an increasing sequence in PSH(θm0 ) for any given m0 . By\nTheorem 5.11, ϕm converges pointwise on X div to ϕ ∈ PSH(θ), which satisfies ψ = π ? ϕ on\nY div . The result follows.                                                                 \u0003\n\nProof of Theorem 5.12. Since the normalization morphism ν : X ν → X is finite, ν ? ω is\nample, and hence Hdom (ν ? ω) spans PL(X ν ), see (3.2). By Lemma 2.3, PL(X ν ) separates\nthe points of (X ν )an , and it is thus already the case of Hdom (ν ? ω). On the other hand,\nLemma 5.13 implies that all functions in Hdom (ν ? ω) ⊂ PSH(ν ? ω) descend to X an (take ωm =\n(1 + m−1 )ω). As a consequence, ν an : (X ν )an → X an is injective. By the non-Archimedean\nGAGA principle, this implies that ν : X ν → X is injective as well (see [Berk90, §3.4]); this\nis enough to conclude that ν is a homeomorphism, and hence that X is unibranch.             \u0003\n\n   As mentioned above, in the complex analytic case the envelope property conversely holds\nas soon as X is unibranch. It is thus natural to conjecture:\nConjecture 5.14. If X is unibranch, then the envelope property holds for all θ ∈ N1 (X).\n  We will establish this conjecture in the important special case where θ is ample, X is\nsmooth, and char k = 0 (see Theorem 5.20).\nRemark 5.15. The envelope property makes sense also when X is reducible. It is easy to\nsee that θ ∈ N1 (X) has the envelope property iff θ|Y ∈ N1 (Y ) has the envelope property\nfor every connected component Y of X. Moreover, if X is connected, then the proof of\nTheorem 5.12 shows that if the envelope property holds for some ample class in N1 (X), then\nthe normalization morphism ν : X ν → X is a homeomorphism, which implies that X is\nirreducible (and unibranch).\n5.3. Envelopes. For ample classes, the envelope property admits a useful reformulation.\nWe continue to assume that X is irreducible unless stated otherwise. Fix a class ω ∈\n",
      "application_check": "Lemma 5.13 assumes envelope properties on the target. It cannot prove those properties on that target by normalization. The curve proof avoids this circularity. Conjecture 5.14 is reported as a conjecture in this exact source version, not as a current impossibility theorem."
    },
    {
      "id": "bj-continuous-envelopes",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 2909,
      "line_end": 2954,
      "character_start": 204588,
      "source_locator": "Lemma 5.17 with proof, p. 60",
      "pdf_page_range_from_formfeeds": [
        60,
        61
      ],
      "literal_file": "source-extracts/bj-continuous-envelopes.txt",
      "literal_sha256": "8a7fa152ac5d95fa9e0a71a1a04b1a4335e0f8647955bf424b53f8edc256a89d",
      "literal_extract": "Lemma 5.17. For any ω ∈ Amp(X), the following statements are equivalent:\n   (i) ω has the envelope property;\n  (ii) for any function ϕ : X an → R ∪ {±∞}, we have\n                      Pω (ϕ) ≡ −∞, Pω (ϕ)? ≡ +∞, or Pω (ϕ)? ∈ PSH(ω).\n     (iii) for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.\n     We refer to the property in (iii) as continuity of envelopes.\nProof. First assume (i). Pick any ϕ : X an → R ∪ {±∞}, and suppose that the set F :=\n{ψ ∈ PSH(θ) | ψ ≤ ϕ} is nonempty, so that Pω (ϕ) 6≡ −∞. If the functions in F are uniformly\nbounded above, then Pω (ϕ)? ∈ PSH(ω), by (i). If not, then, by the definition of the\nAlexander–Taylor capacity we have\n             Pω (ϕ)(v) = sup {ψ(v) | ψ ∈ F} ≥ sup {sup ψ | ψ ∈ F} − Tω (v) = +∞\nfor all v ∈ X div , and hence Pω (ϕ)? ≡ +∞, by density of X div . This proves (i)⇒(ii).\n   Next we prove (ii)⇒(iii), so pick ϕ ∈ C0 (X). Then Pω (ϕ)? ∈ PSH(ω) is a competitor in\nthe definition of Pω (ϕ), and hence Pω (ϕ)? ≤ Pω (ϕ). We conclude that Pω (ϕ)? = Pω (ϕ) is\nusc. We claim that Pω (ϕ) is also lsc, and hence continuous. To prove the claim, it suffices to\nshow that Pω (ϕ) is a supremum of continuous functions, and for this it suffices to prove that\nfor any ψ ∈ PSH(ω) with ψ ≤ ϕ and any ε > 0, there exists ψ 0 ∈ C0 (X) with ψ ≤ ψ 0 ≤ ϕ+ε.\nPick a decreasing net ψi ∈ Hdom (ω) converging pointwise to ψ. For each v ∈ X an , the set\n{ψi < ϕ + ε} is an open neighborhood of v for i large enough, by lower semicontinuity of\nϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for all i large enough, so we can\ntake ψ 0 = ψi .\n   Finally, we prove (iii)⇒(i), following [BE20, Lemma 7.30]. Let (ϕi ) be a bounded-above\nfamily in PSH(ω), and set ϕ := sup?i ϕi . Since ϕ is usc and X an is compact, we can find\na decreasing net of continuous functions (ψj ) such that ψj → ϕ. For each i, j, we have\nϕi ≤ ψj , and hence ϕi ≤ Pω (ψj ), which in turn yields ϕ ≤ Pω (ψj ) ≤ ψj . We have thus\nwritten ϕ as the limit of the decreasing net of ω-psh functions Pω (ψj ), which shows that ϕ\nis ω-psh.                                                                                    \u0003\nCorollary 5.18. Assume that ω ∈ Amp(X) has the envelope property, and consider a usc\nfunction ϕ : X an → R ∪ {−∞}. Then:\n    (i) Pω (ϕ) is ω-psh, or Pω (ϕ) ≡ −∞;\n   (ii) if ϕ is the limit of a decreasing net (ϕj ) of bounded-above, usc functions, then\n        Pω (ϕj ) & Pω (ϕ).\nProof. By Lemma 5.17, either ψ := Pω (ϕ)? is ω-psh, or Pω (ϕ) ≡ −∞. Since Pω (ϕ) ≤ ϕ and\nϕ is usc, we also have ψ ≤ ϕ. If ψ is ω-psh, then ψ ≤ Pω (ϕ), which proves (i).\n  To see (ii), note that ρ := limj Pω (ϕj ) satisfies either ρ ∈ PSH(ω) or ρ ≡ −∞, by\nTheorem 4.7. Furthermore, Pω (ϕj ) ≤ ϕj yields in the limit ρ ≤ ϕ, and hence ρ ≤ Pω (ϕ) (by\ndefinition of Pω (ϕ) if ρ ∈ PSH(ω), and trivially if ρ ≡ −∞). Thus limj Pω (ϕj ) = ρ = Pω (ϕ).\nOn the other hand, Pω (ϕj ) ≥ Pω (ϕ) implies ρ ≥ Pω (ϕ), which completes the proof of (ii). \u0003\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      61\n\n  For any function ϕ : X an → R ∪ {±∞}, we also introduce the pointwise envelope\n                           Qω (ϕ) := sup {ψ ∈ CPSH(ω) | ψ ≤ ϕ} ;\nthis is lsc and bounded below if ϕ is bounded below, and ≡ −∞ otherwise. Since each\nψ ∈ CPSH(ω) is the uniform limit of functions in Hdom (ω) (see Theorem 4.7), one easily\nchecks that\n                            Qω (ϕ) = sup{ψ ∈ Hdom (ω) | ψ ≤ ϕ}.\n",
      "application_check": "Applied after the envelope property is proved by homeomorphism and psh-cone descent. It identifies continuity of envelopes with that property."
    },
    {
      "id": "bj-smooth-envelope-input",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 2976,
      "line_end": 2991,
      "character_start": 209635,
      "source_locator": "Theorem 5.20 and Corollary 5.21, p. 61",
      "pdf_page_range_from_formfeeds": [
        61,
        62
      ],
      "literal_file": "source-extracts/bj-smooth-envelope-input.txt",
      "literal_sha256": "11349d8f94838acb903edb5892c5c98d73f80abfb015eaeed2c0ad8470035613",
      "literal_extract": "\n5.4. The envelope property on smooth varieties. The results earlier in this section\nwould not be particularly useful unless we have examples of classes where the envelope\nproperty holds. Arguing along the lines of [BFJ16, Theorem 8.5], we will prove:\nTheorem 5.20. Assume that X is smooth and connected, and that either char k = 0 or\ndim X ≤ 2. Then any θ ∈ Nef(X) has the envelope property.\n  We do not know whether a class θ ∈ N1 (X) that is not nef has the envelope property.\nCorollary 5.21. Under the assumptions of Theorem 5.20, the set\n                           PSHsup (θ) = {ϕ ∈ PSH(θ) | sup ϕ = 0}\nis compact.\n  In [BFJ16], the above compactness property was established in the discretely valued\ncase, by relying on much more involved arguments based on dual complexes and toroidal\nmodifications.\n\f62                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nLemma 5.22. Let L be an ample line bundle on X, and (X , L) a test configuration for\n",
      "application_check": "Only smooth, connected, projective Y over algebraically closed trivially valued k of characteristic zero is used. Pullback of an ample line bundle by the finite normalization is ample, not merely nef."
    },
    {
      "id": "bj-monotone-energy-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 3650,
      "line_end": 3731,
      "character_start": 254067,
      "source_locator": "Theorem 7.1 with proof and Proposition 7.2, pp. 74-76",
      "pdf_page_range_from_formfeeds": [
        74,
        76
      ],
      "literal_file": "source-extracts/bj-monotone-energy-proof.txt",
      "literal_sha256": "9e6fd482d3fc82b8cf8b9e755bf4612b8f77ae3f105127132fde0051b3590cbc",
      "literal_extract": "   In this section, X denotes a projective variety of dimension n, with irreducible components\nXα . We extend the energy pairing to arbitrary psh functions, and use this to define functions\nof finite energy, and the mixed Monge–Ampère operator thereon.\n7.1. Extending the energy pairing. In §3.2, the energy pairing\n                                  (θ0 , ϕ0 ) · . . . · (θn , ϕn ) ∈ R\nwas defined for pairs (θi , ϕi ) ∈ N1 (X) × PLR . When the ϕi are θi -psh, this is an increasing\nfunction of the ϕi , by Lemma 3.15. On the other hand, any ω-psh function with ω ∈\nAmp(X) can be written as a decreasing limit of functions in Hdom (ω) ⊂ PL ∩ PSH(ω) (see\nTheorem 4.15). This allows to extend the energy pairing by monotonicity, as follows.\n\f                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                                       75\n\nTheorem 7.1. For each (n + 1)-tuple ω0 , . . . , ωn ∈ Amp(X), the energy pairing\n                           (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )\nadmits a unique extension to a map ni=0 PSH(ωi ) → R ∪ {−∞} that is\n                                          Q\n\n     • upper semicontinuous;\n     • increasing in each variable.\nFurthermore, this map is continuous along decreasing nets, and satisfies\n                  (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =             inf             (ω0 , ψ0 ) · . . . · (ωn , ψn )              (7.1)\n                                                       ψi ∈Hdom (ωi ), ψi ≥ϕi\n                  Q\nfor all (ϕi ) ∈       i PSH(ωi ).\n\nProof. Any map that is both usc and increasing is automatically continuous along decreasing\nnets. Since all functions in PSH(ωi ) are limits of decreasing nets in Hdom (ωi ) ⊂ PL(X) ∩\nPSH(ωi ), uniqueness is clear. To prove existence, it suffices to show that (7.1) has the\nrequired properties.\n  Monotonicity is obvious. To prove upper semicontinuity, suppose that ϕi ∈ PSH(ωi ),\n0 ≤ i ≤ n, and t ∈ R satisfy\n                                (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) < t,\nBy definition, we can choose ψi ∈ Hdom (ωi ) and 0 < ε \u001c 1 such that ϕi ≤ ψi and\n                                        (ω0 , ψ0 ) · . . . · (ωn , ψn ) < t − ε.\nSet                                          X\n                                     C :=     (ω0 · . . . · ωbi · . . . · ωn ) > 0.\n                                               i\nBy Proposition 4.28, ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi ), and we can thus find an\nopen neighborhood Ui of ϕi in PSH(ωi ) such that ϕ0i ≤ ψi + εC −1 for all ϕ0i ∈ Ui . By\nmonotonicity of the energy pairing and Proposition 3.14, this gives\n                   (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n ) ≤ (ω0 , ψ0 + εC −1 ) · . . . · (ωn , ψn + εC −1 )\n                                = (ω0 , ψ0 ) · . . . · (ωn , ψn ) + ε < t\n         0\nfor all ϕi ∈ Ui , which proves upper semicontinuity.                                                                             \u0003\nProposition 7.2. The energy pairing (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is symmetric and R>0 -linear\nwith respect to each variable (ωi , ϕi ) with ωi ∈ Amp(X) and ϕi ∈ PSH(ωi ). Furthermore,\n\n                                                                                    n\n                                                                                    X\n (ω0 , ϕ0 + c0 ) · . . . · (ωn , ϕn + cn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) +            ci (ω0 · . . . · ωbi · . . . · ωn )X (7.2)\n                                                                                    i=0\nfor all ci ∈ R,\n                         (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ) = t(ω0 , ϕ0 ) · . . . · (ωn , ϕn )                          (7.3)\nfor all t ∈ R>0 ,\n                                                          X\n                   (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =              (ω0 , ϕ0 )|Xα · . . . · (ωn , ϕn )|Xα ,                    (7.4)\n                                                       dim Xα =n\nand\n                 (ν ? ω0 , ν ? ϕ0 ) · . . . · (ν ? ωn , ν ? ϕn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn )                           (7.5)\nwith ν : X ν → X the normalization morphism.\n\f76                                 SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. Using approximation by decreasing nets in Hdom (ωi ), everything is clear from Propo-\nsition 3.14, except that this only provides a proof of (7.3) for t ∈ Q>0 . To get the general\ncase, we may replace ϕi with ϕi − sup ϕi and assume ϕi ≤ 0 for all i. Write a given t ∈ R>0\nas the limit of an increasing sequence tm ∈ Q>0 . For each i, (tm · ϕi )m is a decreasing\nsequence in PSH(ωi ) that converges to t · ϕi , and hence\n                    lim (ω0 , tm · ϕ0 ) · . . . · (ωn , tm · ϕn ) = (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ).\n                   m→∞\nThe result follows.                                                                                                           \u0003\n     We also record the following useful monotonicity property with respect to ωi .\nProposition 7.3. For i = 0, . . . , n, pick ωi , ωi0 ∈ Amp(X) such that ωi0 ≥ ωi , and ϕi ∈\nPSH(ωi ) ⊂ PSH(ωi0 ). Then\n   (i) if ϕi ≤ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≤ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≤ 0;\n  (ii) if ϕi ≥ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≥ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≥ 0.\nProof. By monotone approximation, we may assume ϕi ∈ PL ∩ PSH(ωi ). By assumption,\nθi := ωi0 − ωi is nef. The result thus follows by expanding out\n                 (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) = ((ω0 , ϕ0 ) + (θ0 , 0)) · . . . · ((ωn , ϕn ) + (θn , 0))\nand applying Corollary 3.16.                                                                                                  \u0003\n  For any θ ∈ N1 (X), recall that CPSH(θ) = C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) respectively denote\nthe sets of continuous and bounded θ-psh functions. We conclude this section with a general\ncontinuity result for the energy pairing involving such functions. It is an analogue of the\nChern–Levine–Nirenberg inequality in the complex case.\n",
      "application_check": "The energy extension is available on possibly singular projective X. The equation (7.5) is used only for psh potentials already defined on X, before the onto descent theorem is established."
    },
    {
      "id": "bj-operator-and-pushforward-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 3980,
      "line_end": 4061,
      "character_start": 276946,
      "source_locator": "Theorem 7.18 with proof and Proposition 7.19 with proof, pp. 81-82",
      "pdf_page_range_from_formfeeds": [
        81,
        83
      ],
      "literal_file": "source-extracts/bj-operator-and-pushforward-proof.txt",
      "literal_sha256": "5d45b299808909541d126ebe119561fc04d667aa3b3d3549ac562d91131898e3",
      "literal_extract": "Theorem 7.18. For each n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , i = 1, . . . , n, there exists a unique\nsigned measure\n                                                      ^\n             (θ1 + ddc ϕ1 ) ∧ · · · ∧ (θn + ddc ϕn ) = (θi + ddc ϕi ) ∈ C0 (X)∨              (7.14)\n                                                                    i\nsuch that             ˆ             ^\n                                ϕ    (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )    (7.15)\n                         X an        i\nfor all ϕ ∈ PL(X)R . If further θi ∈ Nef(X) and ϕi ∈ PSH(θi ) for i = 1, . . . , n, then (7.14)\nis a positive measure.\n  While the notation mimics the one for mixed Monge–Ampère measures in the complex\nanalytic case, we will not define the individual factors θi + ddc ϕi . At least if the ϕi are\ncontinuous, this could, however, be done using the approach in [CLD12] (cf. Remark 7.23\nbelow).\nProof. By density of PL(X) in C0 (X) (see Theorem 2.2), the prescription (7.15) uniquely\ndetermines the measure (7.14). To show existence, we may assume, by multilinearity, that\nθi ∈ Nef(X) and ϕi ∈ E~1 ∩ PSH(θi ) for i = 1, . . . , n. Since any ϕ ∈ PL(X)R can be written\nas a difference of functions in PLR ∩ PSH(ω) for some ω ∈ Amp(X) (see (3.2)), Lemma 7.15\nshows that ϕ 7→ (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ) is a positive linear form on PL(X)R . By density\nof PL(X)R in C0 (X), it thus uniquely extends to a positive linear form on C0 (X), and we\nare done.                                                                                              \u0003\n\f82                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProposition 7.19. Mixed Monge–Ampère measures satisfy the following properties:\n   (i) the signed measure i (θi + ddc ϕi ) is a symmetric and multilinear function of the\n                              V\n\n       n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , of total mass\n                             ˆ     ^\n                                     (θi + ddc ϕi ) = (θ1 · . . . · θn )X ;\n                                       X an i\n\n     (ii) assume (θi , ϕi ) ∈ N1 (X) × PLR , and pick an integrally closed test configuration X\n          dominating Xtriv and Di ∈ VCar(X )R such that ϕi = ϕDi ; then\n                                   ^                   X\n                                      (θi + ddc ϕi ) =   cE δvE ,\n                                           i                          E\n\n          where E ranges over the irreducible components of X0 and\n                         cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E ;\n     (iii) for all (θi , ϕi ) ∈ N1 (X) × E~1 and t ∈ R>0 we have\n                                 ^                           ^\n                                    (θi + ddc (t · ϕi )) = t? (θi + ddc ϕi ),                    (7.16)\n                                   i                                   i\n                        ^                              X        ^\n                             (θi + ddc ϕi ) =                          θi |Xα + ddc ϕi |Xαan ,\n                                                                                            \u0001\n                                                                                                 (7.17)\n                         i                          dim Xα =n i\n                              ^                              ^\n                                       (θi + ddc ϕi ) = ν?          (ν ? θi + ddc ν ? ϕi ) ,     (7.18)\n                               i                                i\n          with ν : X ν → X the normalization;\n     (iv) for any ω ∈ Amp(X), the map E 1 (ω)n 3 (ϕ1 , . . . , ϕn ) 7→ i (θi +ddc ϕi ) is continuous\n                                                                      V\n          along decreasing nets;\n      (v) for all (θi , ϕi ) ∈ N1 (X) × E~1 and ϕ ∈ E~1 , ϕ is integrable against i (θi + ddc ϕi ),\n                                                                                   V\n          and (7.15) holds.\n  When ϕi = 0 for some i, we drop the term ddc ϕi from the notation. As a special case of\nProposition 7.19 (ii), we then have\n                                          X\n                        θ1 ∧ · · · ∧ θn =   (θ1 · . . . · θn )Xα δvtriv,α .        (7.19)\n                                                    dim Xα =n\n\nProof of Proposition 7.19. Points (i) and (iii) follow from Proposition 7.2, while (ii) is a\nreformulation of (3.5). By density of PL(X) in C0 (X), (iv) is equivalent to the fact that,\nfor each ϕ ∈ PL(X),\n                                 ˆ  ^\n            (ϕ1 , . . . , ϕn ) 7→ ϕ   (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )\n                                                i\n\nis continuous along decreasing nets in E 1 (ω)n+1 . Now ϕ can be written as a difference of\nfunctions in PL ∩ PSH(ω 0 ) for some ω 0 ∈ Amp(X), and the desired continuity is thus a\nconsequence of Theorem 7.14. To prove (v), we may assume θi ∈ Amp(X) and ϕi ∈ E 1 (θi ),\nby multilinearity. Any ϕ ∈ E 1 (ω) with ω ∈ Amp(X) can be written as the pointwise limit\nof a decreasing net in PL ∩ PSH(ω), and (7.15) thus holds for ϕ, by monotone convergence\nand the continuity of the energy pairing along decreasing limits.                        \u0003\n\f              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                 83\n\nExample 7.20. Assume X is a smooth curve and pick ω ∈ Amp(X). By Example 4.13,\nany ϕ ∈ PSH(ω) determines a positive Radon measure (deg ω)δvtriv + ∆ϕ, with\n",
      "application_check": "These construct genuine intersection-theoretic MA on finite-energy functions of actual X, including raw mass and normalization pushforward. The formula (7.18) is not an inverse-measure construction."
    },
    {
      "id": "bj-curve-laplacian",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 4060,
      "line_end": 4073,
      "character_start": 282316,
      "source_locator": "Example 7.20, p. 83",
      "pdf_page_range_from_formfeeds": [
        83,
        83
      ],
      "literal_file": "source-extracts/bj-curve-laplacian.txt",
      "literal_sha256": "6bb44a1c7d18b5f445b6fb473c590540d18de146913754001d6cf7d1f687fd0b",
      "literal_extract": "Example 7.20. Assume X is a smooth curve and pick ω ∈ Amp(X). By Example 4.13,\nany ϕ ∈ PSH(ω) determines a positive Radon measure (deg ω)δvtriv + ∆ϕ, with\n              X \u0014d                                                     d2\n                                                                                     \u0015\n                                             d\n        ∆ϕ =              ϕ(t ordp )δvtriv −       ϕ(t ordp )δvp,triv + 2 ϕ(t ordp )\n                    dt 0+                    dt +∞                     dt\n                 p∈X(k)\n\nthe tree Laplacian (see [FJ04, §7]). As we saw in Example 3.19, we have ω + ddc ϕ =\n(deg ω)δvtriv + ∆ϕ for any ϕ ∈ PLR ∩ PSH(ω), and this remains true for any ϕ ∈ E 1 (ω),\nby monotone approximation. For such functions, ω + ddc ϕ further puts no mass on the\nendpoints vp,triv , which means that the convex function t 7→ ϕ(t ordp ) has sublinear growth\n(see respectively Corollary 7.49 and Theorem 11.11).\n",
      "application_check": "The raw curve Laplacian formula is applied on Y and transported only after proving exact psh/energy descent. Its endpoint term vanishes for finite energy, which the argument also proves from the L2 slope condition."
    },
    {
      "id": "bj-comparison-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 4530,
      "line_end": 4603,
      "character_start": 311563,
      "source_locator": "Theorem 7.40 and Theorem 7.44 with proofs, pp. 91-92",
      "pdf_page_range_from_formfeeds": [
        91,
        93
      ],
      "literal_file": "source-extracts/bj-comparison-proof.txt",
      "literal_sha256": "4012b1f3d2dd0576da1026f51701b9d7ac53c75a9cd78a497320206c0247b37f",
      "literal_extract": "crucial role in analyzing deep properties of ω-psh functions and the Monge-Ampère operator.\nTheorem 7.40. If ω ∈ Amp(X), then\n                                1{ϕ>ϕ0 } MA(max{ϕ, ϕ0 }) = 1{ϕ>ϕ0 } MA(ϕ)                                     (7.32)\nfor all ϕ, ϕ0 ∈ E 1 (ω).\n  A first consequence is the fact that the mixed Monge–Ampère operator is local in nature,\nsomething that is not an immediate consequence of our definition in §7.3.\nCorollary 7.41. Let G ⊂ X an be open set. If ωi ∈ Amp(X) and ϕi , ψi ∈ E 1 (ωi ), 1 ≤ i ≤ n,\nare such that ϕi = ψi on G, then\n       (ω1 + ddc ϕ1 ) ∧ · · · ∧ (ωn + ddc ϕn ) = (ω1 + ddc ψ1 ) ∧ · · · ∧ (ωn + ddc ψn ) on G.\nIn particular, if ω ∈ Amp(X) and ϕ, ϕ0 ∈ E 1 (ω) are such that ϕ = ϕ0 on G, then MA(ϕ) =\nMA(ϕ0 ) on G.\nProof. By multilinearity, it suffices to prove the final statement. As in [BFJ15, Corollary 5.2],\ngiven ε > 0 we apply Theorem 7.40 to ϕ+ε and ϕ0 . This gives MA(max{ϕ+ε, ϕ0 }) = MA(ϕ)\non G ⊆ {ϕ+ε > ϕ0 }. Letting ε → 0 gives MA(max{ϕ, ϕ0 }) = MA(ϕ) on G, since the Monge–\nAmpère operator is continuous under decreasing limits. Exchanging the roles of ϕ and ϕ0\ncompletes the proof.                                                                           \u0003\nRemark 7.42. As mentioned in Remark 7.23, when all the functions involved are continu-\nous, the mixed Monge–Ampère measure coincides with the one in [CLD12]. Since the latter\nis local in nature, Theorem 7.40 and Corollary 7.41 follow in this case. However, for appli-\ncations it is important to consider functions ϕ, ϕ0 that are not continuous, and in this case\nthe Borel set {ϕ > ϕ0 } can be quite complicated. By definition, it is an open subset in the\nplurifine topology, see [BT87].\nLemma 7.43. Let ϕ, ϕ0 ∈ PL(X), and pick an integrally closed test configuration X such\nthat ϕ, ϕ0 and ϕ00 := max{ϕ, ϕ0 } are associated to elements D, D0 , D00 of VCar(X )Q . Pick\nan irreducible component E of X0 , and assume that ϕ(vE ) > ϕ0 (vE ). Then ϕ(vF ) ≥ ϕ0 (vF )\nfor any irreducible component F of X0 that intersects E.\n\f92                          SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProof. First, ϕD00 −D = ϕD00 − ϕD ≥ 0 implies D00 − D ≥ 0, by Lemma 2.8, and similarly\nD00 − D0 ≥ 0. Furthermore, 0 < ϕ00 (vE ) − ϕ0 (vE ) = σ(vE )(D00 − D0 ), and E is thus in the\nsupport of D00 − D0 . Now pick any k × -invariant divisorial valuation w on X with center\nξ ∈ E ∩ F , normalized by w(X0 ) = 1; denote by v ∈ X div its restriction to k(X) ,→ k(X ), so\nthat w = σ(v) (see §1.3). Then w(D00 − D0 ) = ϕ00 (v) − ϕ0 (v) > 0, and hence ϕ00 (v) = ϕ(v).\nThis means that D00 = D at ξ; hence 0 = σ(vF )(D00 − D) = ϕ00 (vF ) − ϕ(vF ), which proves\nthe result.                                                                                 \u0003\nProof of Theorem 7.40. First assume that ϕ, ψ ∈ PL ∩ PSH(ω). As in Lemma 7.43, pick\nan integrally closed test configuration X dominating the trivial one, such that ϕ = ϕD ,\nϕ0 = ϕD0 and max{ϕ, ϕ0 } = ϕD00 with D, D0 , D00 ∈ VCar(X )Q . As in Proposition 7.19 (ii)\nwe have                                  X\n                         MA(ϕD ) = V −1     bE ((ωX + D)|E )n δvE ,\n                                                   E\nand a similar formula holds for MA(ϕ ). We thus need to show that ((ωX + D)|E )n =\n                                             D00\n((ωX + D00 ])|E )n for any E with ϕD (vE ) > ϕD0 (vE ). Now Lemma 7.43 yields ϕD (vF ) =\nmax{ϕ(vF ), ϕ0 (vF )} = ϕD00 (vF ) for all components F of X0 that intersect E. This implies\nthat D and D00 coincide in a neighborhood of E. Hence D|E = D00 |E , which implies the\nresult.\n   Now consider the general case. Set\n                             f := max{ϕ − ϕ0 , 0} = max{ϕ, ϕ0 } − ϕ0 .\nThen {ϕ > ϕ0 } = {f > 0}, and it thus suffices to prove that\n                                  f MA(max{ϕ, ϕ0 }) = f MA(ϕ).                                   (7.33)\nIndeed, multiplying by f −1 on {f > 0} will then yield the result.             Let (ϕj )j and (ϕ0j )j be\ndecreasing nets in PL ∩ PSH(ω) converging to ϕ and ϕ0 , respectively, and set\n                            fj := max{ϕj − ϕ0j , 0} = max{ϕj , ϕ0j } − ϕ0j .\nBy the first part of the proof we have fj MA(max{ϕj , ϕ0j }) = fj MA(ϕj ), and (7.33) is now\na consequence of Proposition 7.19 (iii), since max{ϕj , ϕ0j } ∈ E 1 (ω) decreases to max{ϕ, ϕ0 }.\n                                                                                               \u0003\n     Using Theorem 7.40 we obtain the very useful comparison principle.\nTheorem 7.44. If ω ∈ Amp(X) and ϕ, ψ ∈ E 1 (ω), then\n                          ˆ                 ˆ\n                              MA(ϕ) ≥           MA(ψ).\n                                  {ϕ<ψ}                {ϕ<ψ}\n\nProof. We follow [GZ07, Theorem 1.5]. For any ε > 0 we have\n      ˆ                         ˆ                                          ˆ\n  1 = MA(max{ϕ, ψ − ε}) ≥             MA(max{ϕ, ψ − ε}) +                          MA(max{ϕ, ψ − ε})\n                                    {ϕ<ψ−ε}                              {ϕ>ψ−ε}\n                    ˆ                    ˆ                       ˆ                     ˆ\n              =             MA(ψ) +             MA(ϕ) = 1 +              MA(ψ) −              MA(ϕ),\n                  {ϕ<ψ−ε}             {ϕ>ψ−ε}                  {ϕ<ψ−ε}              {ϕ≤ψ−ε}\n\nwhere the second equality follows from Theorem 7.40 and from MA(ϕ − ε) = MA(ϕ). We\ncomplete the proof by letting ε → 0.                                             \u0003\n\f            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                          93\n",
      "application_check": "These results have ample-class and finite-energy hypotheses but no smoothness hypothesis in this source. In the curve result their applications are checked using the constructed actual-X operator. Multiplying the probability inequality by V gives the raw comparison inequality."
    },
    {
      "id": "bj-differentiation-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 4841,
      "line_end": 4958,
      "character_start": 332061,
      "source_locator": "Theorem 8.5 and Corollary 8.6 with proofs, pp. 97-99",
      "pdf_page_range_from_formfeeds": [
        97,
        99
      ],
      "literal_file": "source-extracts/bj-differentiation-proof.txt",
      "literal_sha256": "59ded4d80ab38e2cea94affd26a23c7a57aa0922ed0d35d1cf742e8171912706",
      "literal_extract": "8.3. Uniform differentiability of the energy. Building on [BGM20] we prove the fol-\nlowing uniform differentiability result, which is crucial for what follows.\nTheorem 8.5. Pick f ∈ PL(X)R . For any ϕ ∈ E 1 , we then have\n                                          ˆ\n                      ↓\n                    E (ϕ + εf ) = E(ϕ) + ε f MA(ϕ) + O(ε2 )\n\nas ε → 0, where the implicit constant in the O is uniform with respect to ϕ.\n   If ϕ ∈ CPSH(ω) (and for any ϕ ∈ E 1 , if the envelope property holds), the left-hand side\nsatisfies\n                       E↓ (ϕ + εf ) = E(ϕ + εf ) = E(P(ϕ + εf )),\nby (8.7).\n\f98                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nCorollary 8.6. For any ϕ ∈ E 1 and f ∈ C0 (X) we have\n                                               ˆ\n                           d       ↓\n                                 E (ϕ + tf ) = f MA(ϕ).\n                          dt t=0\n\n  Again, one can replace E↓ with E = E ◦ P if ϕ ∈ CPSH(ω), or if the envelope property\nholds.\n  For any ω ∈ Amp(X) we set Vω := (ω n ).\nLemma 8.7. Pick ω, ω 0 ∈ Amp(X), ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ), and set f := ψ1 − ψ2 . For\nany ϕ ∈ CPSH(ω) we then have\n                               ˆ\n                            −1\n                                                           \u0001n\n                                 f ω + ω 0 + ddc (ϕ + ψ1 )    ≤ Vω−1 Vω+ω0 − 1 sup |f |.\n                                                                              \u0001\n    Eω (ϕ + f ) − Eω (ϕ) − Vω\n\nProof. We may assume ω = c1 (L), ω 0 = c1 (L0 ) for ample line bundles L, L0 on X, Indeed, by\nhomogeneity, we then obtain the case when L, L0 are ample Q-line bundles, and the general\ncase by a simple perturbation argument based on Proposition 8.1 (iii).\n   Consider first any continuous function ρ ∈ C0 (X). For each m ∈ N, ρ defines a sup-norm\nk · kmρ on H0 (X, mL), defined by\n                                   kskmρ = sup |s|e−mρ .\n                                             X an\n\nThis norm induces a norm det k · kmρ on the determinant line det H0 (X, mL). Comparing\nwith the trivial norm, we can and will think of det k · kmρ as a number. It now follows\nfrom [CMac15] (see [BE20, Theorem 9.5]) that the volume\n                                                1\n                        volL (ρ) := − lim             log det k · kmρ\n                                      m→∞ mh0 (mL)\n\nexists in R. We claim that volL (ρ) = EL (ρ). Using [BE20, (9.7)] and (8.3), it is enough\nto prove this when X is irreducible. When ρ ∈ CPSH(L), the equality holds by [BE20,\nTheorem A] (or [BoJ18b, Lemma 4.5]). In the general case, this yields\n                  EL (ρ) = sup {EL (ψ) | ψ ∈ CPSH(L), ψ ≤ ρ} ≤ volL (ρ),\nby monotonicity of volL . On the other hand, Theorem 5.1.1 of [Reb21] (which is valid for\narbitrary non-Archimedean fields; see also [BoJ18b, Theorem 4.13] for the trivially valued\ncase) shows that\n                                                           |s|\n                           ρm := m−1 log       sup\n                                             0\n                                          s∈H (X,mL)\\{0} ksk mρ\n\nsatisfies ρm ∈ PLR ∩ PSH(ω), ρm ≤ ρ and EL (ρm ) → volL (ρ); the claim follows.\n   In particular, EL (ϕ + f ) = volL (ϕ + f ) and EL (ϕ) = volL (ϕ). The desired estimate is\nnow a consequence of Lemma 8.8 below, itself a reformulation of [BGM20, Lemma 3.2]. \u0003\nLemma 8.8. Let L and L0 be ample line bundles on X, and set ω = c1 (L), ω 0 = c1 (L0 ).\nConsider functions ϕ ∈ CPSH(ω), and ψ1 , ψ2 ∈ CPSH(ω 0 ). Set f := ψ1 − ψ2 ∈ C0 and\nC := Vω+ω0 − Vω > 0. Then\n               ˆ\n    C inf\n        an\n           f≤      f (ω + ω 0 + ddc (ϕ + ψ1 ))n − Vω (volL (ϕ + f ) − volL (ϕ)) ≤ C sup f.\n       X        X an                                                              X an\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      99\n\nProof. This is a reformulation in our context of [BGM20, Lemma 3.2] in the special case\nof a trivially valued field k. The fact that k is trivially valued means that we can view ϕ,\nψ1 , ψ2 as continuous psh metrics on the Berkovich analytifications of the line bundles L and\nL0 , respectively. The difference volL (ϕ + f ) − volL (ϕ) can be viewed as the relative volume\nof the metrics ϕ + f and ϕ on L. Note that our current normalization of the volume differs\nfrom the one in loc.cit. by a factor Vω = (Ln ).                                              \u0003\nProof of Theorem 8.5. We argue along the lines of the proof of [BGM20, Theorem 3.1].\nWrite ϕ ∈ E 1 as the limit of a decreasing net (ϕi ) in CPSH(ω). Then E(ϕi +εf ) → E↓ (ϕ+εf )\n(by Proposition 8.3 (v)), E(ϕi ) → E(ϕ) (by continuity of E along decreasing nets in PSH(ω)),\nand MA(ϕi ) → MA(ϕ) weakly (by Proposition 7.19).\n  It is therefore enough to prove the result for ϕ ∈ CPSH(ω). Since f ∈ PL(X)R , we can\nchoose ω 0 ∈ Amp(X) and ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ) such that f = ψ1 − ψ2 . By Lemma 8.7\nwe have, for any ε > 0,\n                                   ˆ\n                                −1\n                                                                    \u0001n\n   Eω (ϕ + εf ) − Eω (ϕ) − εVω       f ω + ddc ϕ + ε(ω 0 + ddc ψ1 )\n\n                                                                ≤ ε Vω−1 Vω+εω0 − 1 sup |f |.\n                                                                                   \u0001\n\nNow Vω−1 Vω+εω0 − 1 = O(ε), while\n                                              n \u0012 \u0013\n                               \u0001n             X  n j\nVω−1         c          0          c       −1\n       ω + dd ϕ + ε(ω + dd ψ1 ) = MAω (ϕ)+Vω       ε (ω+ddc ϕ)n−j ∧(ω 0 +ddc ψ1 )j ,\n                                                 j\n                                                          j=1\n\nwhere (ω + ddc ϕ)n−j ∧ (ω 0 + ddc ψ1 )j is a Radon measure of mass (ω n−j · ω 0j ). The result\nfollows.                                                                                    \u0003\nProof of Corollary 8.6. For f ∈ PL(X)R the result follows directly from Theorem 8.5. For\nan arbitrary f ∈ C0 (X) we argue as in the proof of [BGM20, Theorem 3.1]. By Theorem 2.2,\nwe can pick a sequence (fm ) in PL(X)R such that εm := sup |f − fm | → 0. For each t > 0,\nwe have fm − tεm ≤ f ≤ fm + tεm ; Proposition 8.3 (i) thus yields\n                  E↓ (ϕ + tfm ) − tεm ≤ E↓ (ϕ + tf ) ≤ E↓ (ϕ + tfm ) + tεm ,\nand hence          ˆ                                \u0010                 \u0011\n                     fm MA(ϕ) − εm ≤ lim inf t−1 E↓ (ϕ + tf ) − E↓ (ϕ)\n                                           t→0+\n                                \u0010                    \u0011 ˆ\n                             −1    ↓             ↓\n                 ≤ lim sup t      E (ϕ + tf ) − E (ϕ) ≤ fm MA(ϕ) − εm ,\n                       t→0+\nby Theorem 8.5 applied to fm . Letting m → ∞, we get\n                               \u0010                    \u0011 ˆ\n                            −1    ↓             ↓\n",
      "application_check": "They differentiate E-down on singular X without assuming envelope regularity. Replacing E-down by E composed with P requires the envelope property, supplied here by the curve descent proof. The text extraction of the corollary proof contains sign/epsilon typos; the argument uses the correct bound |f-f_m| <= epsilon_m, and retains the literal text without correcting it."
    },
    {
      "id": "bj-surjectivity-and-node-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.txt",
      "source_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 6089,
      "line_end": 6157,
      "character_start": 407066,
      "source_locator": "Theorem 12.8 with proof and Example 12.11, pp. 121-123",
      "pdf_page_range_from_formfeeds": [
        121,
        123
      ],
      "literal_file": "source-extracts/bj-surjectivity-and-node-proof.txt",
      "literal_sha256": "2e87b852595ae68631c13d0e0c79646b0583df71f5c1c29f18293390269eff58",
      "literal_extract": "   Recall from Theorem 5.11 that the envelope property for ω ∈ Amp(X) (which holds if X\nis smooth and k has characteristic zero, cf. Theorem 5.20) is equivalent to the compactness\nof PSH(ω)/R. In a similar vein we have:\nTheorem 12.8. For any ω ∈ Amp(X), the following are equivalent:\n    (i) the envelope property holds for ω;\n   (ii) the Monge–Ampère operator MAω : E 1 (ω) → M1 is onto;\n  (iii) the Monge–Ampère operator induces a bi-Lipschitz isomorphism\n                                  (E 1 (ω)/R, Iω ) ≃ (M1 , I∨\n                                                            ω );\n\f122                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n      (iv) (E 1 (ω)/R, Iω ) is complete;\n       (v) (E 1 (ω), Iω ) is complete.\n  In particular, E 1 (ω) can only be complete if X is unibranch, cf. Theorem 5.12.\nProof. Assume (i). By Corollary 9.12, (ii) holds iff the supremum defining\n                                            \u0012          ˆ     \u0013\n                              ∨\n                             E (µ) = sup E(ϕ) − ϕ µ\n                                             ϕ∈E 1\n\nis achieved for any µ ∈ M1 . Thus choose a maximizing sequence (ϕi ) for µ in Esup     1 . By\n\nCorollary 5.21, PSHsup is weakly compact, and we may thus assume, after passing to a\nsubnet, that (ϕi ) converges weakly to ϕ ∈ PSHsup . Since Jµ (ϕi ) → 0, (9.11) shows that J(ϕi )\nis eventually bounded, and hence that ´ϕ ∈ E 1 (ω),\n                                                 ´ since J is weakly lsc. By Proposition 9.19,\nthe weak convergence ϕi → ϕ implies ϕi µ → ϕ µ, and hence\n                             ˆ              \u0012          ˆ       \u0013\n                     E(ϕ) − ϕ µ ≥ lim sup E(ϕi ) − ϕi µ = E∨ (µ),\n                                             i\nsince E is weakly usc. This proves (i)⇒(ii). Proposition 12.7 gives (ii)⇔(iii), and (iii)⇒(iv)\nfollows from the completeness of (M1 , I∨    ω ) (Theorem 10.14).\n   Assume (iv), and pick a Cauchy sequence (ϕi ) in (E 1 (ω), Iω ). Then (ϕi −sup ϕi ) is Cauchy\n     1 (ω) ≃ E 1 (ω)/R, and hence strongly convergent in E 1 (ω). Now (sup ϕ ) is Cauchy as\nin Esup                                                                            i\nwell, and hence convergent in R, so we conclude that (ϕi ) is strongly convergent, proving\n(iv)⇒(v).\n   Finally we prove (v)⇒(i). Assume that E 1 (ω) is complete. By Theorem 5.11, (i) is\nequivalent to the fact that any bounded, increasing net (ϕi ) in PSH(ω) converges weakly in\nPSH(ω). Since the increasing net (sup ϕi ) converges in R, it will be enough to show that\n(ϕi ) is Cauchy in E 1 (ω)/R, i.e. that\n                                                                 ˆ\n              Iω (ϕi , ϕj ) ≈ Jω,ϕi (ϕj ) = Eω (ϕi ) − Eω (ϕj ) + (ϕj − ϕi ) MAω (ϕi )\n\ntends to 0 as i, j → ∞, where by symmetry of Iω we may assume i ≤ j. The increasing net\n(Eω (ϕi )) converges in R. Given ε > 0, choose i0 such that 0 ≤ Eω (ϕj ) − Eω (ϕi ) ≤ ε for\nj ≥ i ≥ i0 . As ϕi ≤ ϕj , (7.22) yields\n                   ˆ\n              0 ≤ (ϕj − ϕi ) MAω (ϕi ) ≤ (n + 1) (Eω (ϕj ) − Eω (ϕi )) ≤ (n + 1)ε.\n\nThus                                               ˆ\n                           Eω (ϕi ) − Eω (ϕj ) +       (ϕj − ϕi ) MAω (ϕi ) ≤ nε,\nwhich proves, as desired, that (ϕi ) is Cauchy in E 1 (ω)/R.                                  \u0003\n   As a direct consequence of Theorem 12.8 and Theorem 5.20, we have the following result,\ncf. Theorem A.\nTheorem 12.9. Suppose that X is smooth, that char k = 0 or dim X ≤ 2, and fix ω ∈\nAmp(X). Then the Monge–Ampère equation MA(ϕ) = µ admits a solution ϕ ∈ E 1 (ω),\nunique up to translation, for every µ ∈ M1 .\nExample 12.10. Assume the envelope property for ω ∈ Amp(X). For each v ∈ X lin , there\nexists a unique ϕv ∈ E 1 (ω) such that MA(ϕv ) = δv and ϕv (v) = 0, which we call the Green’s\nfunction of v. See Proposition 12.14 for more on these functions.\n\f             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                            123\n\nExample 12.11. Let X be an irreducible curve with a nodal singularity at p ∈ X(k), and\ndenote by p1 , p2 ∈ X ν (k) the preimages of p (see Figure 1). Then v := ordp1 ∈ X ν, div ≃\nX div , and δv ∈ M1 (X) is not in the image of MA : E 1 → M1 . Using Example 7.20 and\nν? MA(ν ? ϕ) = MA(ϕ) (see (7.18)), one sees indeed that a function ϕ ∈ PSH(ω) such that\nMA(ϕ) = δv must satisfy ν ? ϕ(vtriv ) = ν ? ϕ(vp2 ,triv ) = ϕ(vp,triv ) = ν ? ϕ(vp1 ,triv ), and hence\nmust be constant on the ray through v, a contradiction.\n",
      "application_check": "Surjectivity is equivalent to the envelope property on irreducible projective X over algebraically closed trivially valued k. The proof cites Corollary 5.21 for compactness although the general applicable result is Theorem 5.11; our application uses Theorem 5.11. The node obstruction is proved explicitly in the new argument."
    },
    {
      "id": "bfj-v1-retained-hypotheses",
      "source": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.txt",
      "source_sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 62,
      "line_end": 116,
      "character_start": 5218,
      "source_locator": "Introduction and Theorem A, pp. 2-3; PDF watermark v1",
      "pdf_page_range_from_formfeeds": [
        2,
        3
      ],
      "literal_file": "source-extracts/bfj-v1-retained-hypotheses.txt",
      "literal_sha256": "b8ae1c015b32c41b2c5b80f8597ba7bfde6a3edbd66a8b6950287d4a0e76af4e",
      "literal_extract": "K be a complete discrete valuation ﬁeld whose residue ﬁeld k has characteristic zero, so\nthat K ≃ k((t)). Let X be a smooth projective variety over K, and write n = dim X.\nThanks to the non-Archimedean GAGA principle, it is reasonable to also denote by X\nthe corresponding K-analytic space in the sense of Berkovich, whose underlying topological\nspace is compact Hausdorﬀ. A model of X is a normal scheme X that is ﬂat and projective\nover S := Spec k[[t]], and whose generic ﬁber can be identiﬁed with X.\n   Consider a ample line bundle L on X. A model metric on L is a metric deﬁned by a\nextension L ∈ Pic(X )Q of L to some model X . Such a metric is called semipositive if L is\nnef, i.e. has non-negative degree on all proper curves of the special ﬁber of X . S.-W. Zhang\nintroduced in [Zha95] the more ﬂexible notion of semipositive continuous metric as the\nuniform limit of semipositive model metrics.1 In this context, A. Chambert-Loir [CL06]\ndeﬁned the Monge-Ampère measure c1 (L, k · k)n of a semipositive continuous metric k · k on\nL. It is a positive Radon measure on X, of mass deg L.\n   V. Berkovich constructed in [Ber99] the skeleton associated to a polystable model of X.\nSince we are assuming K to have residue characteristic zero, it is easier to rely on resolution\nof singularities and instead consider SNC models, i.e. models whose special ﬁber has simple\nnormal crossing support (but is not necessarily reduced, as opposed to a semistable model).\nTo each SNC model X is associated a dual complex ∆X that encodes the combinatorics of\nthe intersections of the components of the special ﬁber, and which embeds in the Berkovich\nspace X just as skeletons do. Any ﬁnite set  S of divisorial points is contained in the dual\ncomplex of some SNC model; in particular X ∆X is dense in X.\n   We can now state our main result. We say that X is algebraizable if there exists a (one-\nvariable) function ﬁeld F admitting K as a completion and a smooth projective F -scheme\nY such that X = YK .\nTheorem A. Let K be a complete discrete valuation field of residue characteristic zero. Let\nX be a smooth projective K-variety that is algebraizable. Let L ∈ Pic(X) be an ample line\n    1We refer to Table 1 in §2.6 below for a comparison of our terminology with existing terminology.\n\f               SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION                          3\n\nbundle and µ be a positive Radon measure on X of mass c1 (L)n . If we further assume that\nµ is supported on the dual complex of some SNC model of X, then there exists a continuous,\nsemipositive metric k · k on L such that\n                                   c1 (L, k · k)dim X = µ .                              (1.1)\nThis metric is furthermore unique up to a multiplicative constant.\n  Even though the result is most likely true without this assumption, the algebraizability\ncondition plays an essential role in our proof, as we shall explain below. Note that the line\nbundle L is not assumed to be deﬁned over a function ﬁeld.\n   The uniqueness part in Theorem A follows from a result of X. Yuan and S.-W. Zhang\n[YZ10] asserting more generally that a continuous semipositive metric k · k is uniquely de-\ntermined up to a constant by its Monge-Ampère measure. Their proof is inspired by the\none given by Blocki [Blo03] in the complex setting.\n   Our approach does not give any information on the regularity of the metric besides con-\ntinuity. It would be interesting to further investigate this issue, for instance when µ is\nsupported on ﬁnitely many divisorial points. We refer to §9 for a discussion of this problem\nin the case of toric varieties, based on the recent work [BPS11].\n   Versions of Theorem A are already known in a few cases. For curves (and in fact over any\ncomplete non-Archimedean, non-trivially valued ﬁeld), it can easily be deduced from results\nof A. Thuillier [Thu05], who developed a theory of singular semipositive metrics on analytic\ncurves that is completely analogous to the complex case. Solving (1.1) for curves boils down\nto a system of linear equations and relies on the negativity of the intersection form of the\nspecial ﬁber of a suitable model, see §9. Alternatively, one can exploit the structure of the\nBerkovich space as a metrized graph as in [BR10, FJ04].\n   In higher dimensions, Y. Liu [Liu10] treated the related case when X is a totally degener-\nate abelian variety over Cp , and µ is a (smooth) measure supported on the dual complex of\nthe canonical formal model of X, as constructed by Mumford. By exploiting the fact that\n",
      "application_check": "The saved v1 assumes smoothness, completeness, discrete valuation, residue characteristic zero, projectivity, ample L, function-field algebraizability of X and dual-complex support. It is not cited as a theorem for arbitrary finite-energy measures."
    },
    {
      "id": "be-not-pluripotential-paper",
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 114,
      "line_end": 170,
      "character_start": 9425,
      "source_locator": "Theorem A and Corollary B, pp. 3-4",
      "pdf_page_range_from_formfeeds": [
        3,
        4
      ],
      "literal_file": "source-extracts/be-not-pluripotential-paper.txt",
      "literal_sha256": "bd7658ea571b70b0f2048e23d63bf89410438a55a85f6dc6ba664cf80fbf7305",
      "literal_extract": "                                          j=0\n\nWe use additive notation for metrics on line bundles, so that φ − ψ is a function on X, and\nddc φ, ddc ψ denote the curvature (1, 1)-forms of φ, ψ.\n\n   Consider now an arbitrary complete valued field K, i.e. a field K complete with respect to\nan absolute value. In the Archimedean case, K = R or C, by the Gelfand–Mazur theorem.\nIn the non-Archimedean case, the main examples are K = Qp , Cp , or fields of formal\nLaurent series and their completed algebraic closure, but the trivially valued case is also\nimportant for the study of K-stability (see [BJ18b]). Let X be a geometrically reduced\nprojective scheme over K, L be a line bundle on X, and φ, ψ be continuous metrics on\n(the Berkovich analytification of) L. Building on a result of Chen and Maclean based on\nOkounkov bodies [CMac15], we show the existence of the relative volume of φ, ψ\n                                         n!\n                      vol(L, φ, ψ) := lim     vol (k · kmφ , k · kmψ ) ∈ R,                     (0.3)\n                                  m→∞ mn+1\ncf. Theorem 9.8. The main result of the present paper is as follows.\nTheorem A. Let X be a geometrically reduced projective scheme over any complete valued\nfield K, and φ, ψ be continuous psh2 metrics on an ample line bundle L over X. Then\n                                        vol(L, φ, ψ) = E(φ, ψ).\n   In the Archimedean case, it follows from results of Demailly that a continuous metric\non L is psh iff it is a uniform limit of Fubini–Study metrics (see Theorem 7.1). In the\nnon-Archimedean case, we use this as a definition, and prove compatibility with the more\ncommon notion of semipositive metric in this context, due to S.W. Zhang and involving\nnef models, when K is nontrivially valued. We also show that a continuous metric φ is\npsh iff it becomes psh after ground field extension. The relative Monge–Ampère energy of\ncontinuous psh metrics can still be defined by (0.2), the latter being understood in the sense\nof Chamber-Loir and Ducros [CLD12] in the non-Archimedean sense.\n   In the Archimedean case, Theorem A reduces to [BB10] after passing to a resolution of\nsingularities. In the discretely valued case, it was established in [BG+16, Theorem A]. The\nmain contribution of the present paper is thus to establish Theorem A for a densely valued,\nnon-Archimedean ground field K.\n  1Note that the present normalization, which is more convenient for the purpose of this paper, is not\nuniform accross the literature.\n   2A shorthand for plurisubharmonic.\n\f4                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\n\n   The psh envelope P(φ) of a continuous metric φ on L is defined as the pointwise supremum\nof the family of all continuous psh metrics ψ on L such that ψ ≤ φ. We say that continuity\nof envelopes holds for (X, L) if P(φ) is continuous (and hence psh) for each continuous metric\nφ on L.\nCorollary B. Assume that continuity of envelopes holds for (X, L). For any two continuous\nmetrics φ, ψ on L, we then have\n                                 vol(L, φ, ψ) = E(P(φ), P(ψ)).\n   In the Archimedean case, classical results in pluripotential imply that continuity of en-\nvelopes holds whenever X is normal, and Corollary B is indeed also a consequence of [BB10]\nin that case.\n   In the non-Archimedean case, we similarly expect continuity of envelopes to holds as soon\nas X is normal. As of this writing, continuity of envelopes (and hence Corollary B) has been\nestablished when X is smooth, and one of the following is satisfied:\n      • X is a curve, as a consequence of A. Thuillier’s work [Thu05] (see [GJKM19]);\n      • K is discretely or trivially valued, of residue characteristic 0 [BFJ16, BJ18a], building\n        on multiplier ideals and the Nadel vanishing theorem;\n      • K is discretely valued of characteristic p, (X, L) is defined over a function field\n        of transcendence degree d, and resolution of singularities is assumed in dimension\n        n + d [GJKM19], replacing multiplier ideals with test ideals.\n\n",
      "application_check": "Boucksom-Eriksson concerns spaces of norms and continuous psh metrics. It gives no general finite-energy singular equation theorem. The conditional continuity-of-envelopes hypothesis is retained."
    },
    {
      "id": "be-energy-projection-proof",
      "source": "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.txt",
      "source_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 3545,
      "line_end": 3590,
      "character_start": 247684,
      "source_locator": "Proposition 9.14 with proof, pp. 74-75",
      "pdf_page_range_from_formfeeds": [
        74,
        75
      ],
      "literal_file": "source-extracts/be-energy-projection-proof.txt",
      "literal_sha256": "c19770fe07dd2017ff94f6b850f1b4e073a8bd3664a035c933f467549633a1b7",
      "literal_extract": "Ampère energy7of φ, ψ as\n                                   n Z\n                              1 X\n                 E(φ, ψ) :=            (φ − ψ)(ddc φ)j ∧ (ddc ψ)n−j ∧ δX .        (9.11)\n                            n+1\n                                         j=0\n\n   Recall that φ − ψ is a continuous function on X an , which may thus be integrated against\neach positive Radon measure (ddc φ)j ∧ (ddc ψ)n−j ∧ δX . By (8.9), we have\n                                          1                       \u0001\n                             E(φ, ψ) =          hφn+1 i − hψ n+1 i .                  (9.12)\n                                        n+1\nGiven a continuous psh metric ψ, the functional φ 7→ E(φ, ψ) is characterized as the unique\nantiderivative of the Monge–Ampère operator φ 7→ (ddc φ)n that vanishes at ψ, in the sense\nthat                                                Z\n                      d                     ′\n                             E((1 − t)φ + tφ , ψ) =        (φ′ − φ)(ddc φ)n           (9.13)\n                      dt t=0                          X an\nfor any two continuous psh metrics φ, φ′ , see [BJ18a, §3.8].\nProposition 9.14. The Monge–Ampère energy satisfies the following properties.\n    (i) cocycle formula: E(φ1 , φ2 ) + E(φ2 , φ3 ) + E(φ3 , φ1 ) = 0;\n   (ii) monotonicity: φ ≤ φ′ =⇒ E(φ, ψ) ≤ E(φ′ , ψ);\n  (iii) scaling: E(φ + c, ψ) = E(φ, ψ) + V c for c ∈ R;\n  (iv) homogeneity: E(aφ, aψ) = an+1 E(φ, ψ) for a ∈ Z>0 .\n   (v) Lipschitz continuity:\n                                                                             \u0001\n                    E(φ, ψ) − E(φ′ , ψ ′ ) ≤ V sup |φ − φ′ | + sup |ψ − ψ ′ | .\n     (vi) for each complete field extension F/K we have\n                                         E(φF , ψF ) = E(φ, ψ).\n     7Note that the present normalization, which is more convenient for the purpose of this paper, is not\nuniform accross the literature.\n\f                NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                             75\n\n  (vii) birational invariance: for any projective birational morphism µ : X ′ → X we have\n                                    E(µ⋆ φ, µ⋆ ψ) = E(φ, ψ).\nProof. (i) follows from (9.13), and (ii)— (iv) follow directly from (9.11), using that\n                           Z\n                             (ddc φ)j ∧ (ddc ψ)n−j ∧ δX = (Ln ) = V.\n\n(v) is a formal consequence of (ii) and (ii), and (vi) follows from (9.11) and the compatibility\nof mixed Monge–Ampère measures with ground field extension, cf. Proposition 8.3. Finally,\n(vii) is a consequence of (9.11) and the projection formula µ⋆ δX ′ = δX .                    \u0003\n9.4. Proof of Theorem A. The following result corresponds to Theorem A in the intro-\nduction. It was first established in [BB10] when K is Archimedean, and in [BG+16] when\nK is discretely valued.\nTheorem 9.15. Let X be a geometrically reduced projective K-scheme, and L be a semi-\n",
      "application_check": "Only a background projection-formula check is retained. The actual-X curve proof uses BJ Proposition 7.2, which covers the decreasing finite-energy extension, rather than silently extending this continuous-metric proposition."
    },
    {
      "id": "synthetic-measure-completion",
      "source": "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.txt",
      "source_sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 53,
      "line_end": 157,
      "character_start": 4696,
      "source_locator": "Introduction and Theorem A, pp. 2-3",
      "pdf_page_range_from_formfeeds": [
        2,
        4
      ],
      "literal_file": "source-extracts/synthetic-measure-completion.txt",
      "literal_sha256": "7b5d66fb4a5e9004e24a5ab4c43c7b818e7d3761afce793683a6c29c30be332b",
      "literal_extract": "       • introduce the twisted energy and free energy functionals on the latter space, whose\n         composition with the Monge–Ampère operator respectively recover the Donaldson\n         J-functional and the Mabuchi K-energy in the Kähler case, and their analogues in\n         the non-Archimedean case;\n       • show that coercivity of the free energy is an open condition with respect to the\n         Kähler class.\nThe emphasis in this paper is on measures of finite energy, as opposed to potentials of finite\nenergy, that we do not seek to investigate here (see for instance [BFJ15, BoJ22a, Reb21,\nDXZ23] in the non-Archimedean context).\n\nThe general setup. Throughout this paper, we work with a compact topological space X\nequipped with the following data:\n       • a dense linear subspace D ⊂ C0 (X) of test functions, containing all constants;\n       • a vector space Z of closed (1, 1)-forms on X, endowed with a nice1 partial order,\n         and a linear map ddc : D → Z vanishing on constants;\n       • an integer n ≥ 1 (seen as the ‘dimension’ of X), and a nonzero n-linear symmetric\n         map taking a tuple (θ1 , . . . , θn ) in Z to a signed Radon measure θ1 ∧ · · · ∧ θn on X,\n         assumed to be positive for all θi ≥ 0, and such that each bilinear form\n                                                   ˆ\n                      D × D → R (φ, ψ) 7→ φ ddc ψ ∧ θ1 ∧ · · · ∧ θn−1                          (0.1)\n\n         with θi ∈ Z is symmetric, and seminegative for θi ≥ 0.\nWe then introduce the Bott–Chern cohomology space\n                                          HBC (X) := Z/ddc D,\nand define the positive cone Pos(X) ⊂ HBC (X) as the interior2 of the image of the convex\ncone\n                                 Z+ := {θ ∈ Z | θ ≥ 0}.\nThis setup is primarily inspired by the case of a compact Kähler manifold X, where D is\nthe space of smooth functions, and Z the space of closed (1, 1)-forms. It also covers the\ncase of a projective Berkovich space X over a complete non-Archimedean field k, where D\nis generated by piecewise linear (or model ) functions, and elements of Z are represented by\nnumerical classes on models over the valuation ring (or test configurations, in the trivially\nvalued case) [BFJ16a, GM16, BoJ22a]. At least under reasonable assumptions on X and k,\nwe then have HBC (X) = N1 (X), and Pos(X) coincides with the ample cone, see §1.3.2.\n\nMeasures\n    ´     of finite energy. Fix a form ω ∈ Z+ such that [ω] ∈ Pos(X), with volume\nVω = ω n > 0. The space of ω-plurisubharmonic test functions is defined as\n                                Dω := {φ ∈ D | ωφ := ω + ddc φ ≥ 0},\nand the Monge–Ampère operator takes φ ∈ Dω to the probability measure\n                                          MAω (φ) := Vω−1 ωφn .\n\n    1See §1.1 for the terminology.\n    2Here we use the finest vector space topology of H\n                                                         BC (X), see §1.1.\n\f                                  MEASURES OF FINITE ENERGY                                          3\n\nIt admits a primitive, the Monge–Ampère energy Eω : Dω → R, explicitly given by\n                                         n      ˆ\n                                     1 X −1\n                           Eω (φ) =        Vω     φ ωφj ∧ ω n−j .\n                                    n+1\n                                              j=0\n\nDenote by M the space of (Radon) probability measures on X, and define the energy of a\nmeasure µ ∈ M as the Legendre transform3\n                                             ˆ\n                      Jω (µ) := sup {Eω (φ) − φ µ} ∈ [0, +∞].\n                                     φ∈Dω\n\nThen Jω : M → [0, +∞] is convex, and lsc in the weak topology; the space of measures of\nfinite energy is defined as\n                                  M1ω := {µ ∈ M | Jω (µ) < ∞},\nequipped with the strong topology, i.e. the coarsest refinement of the weak topology in which\nJω becomes continuous.\n   As a consequence of the seminegativity of (0.1), the functional Eω is concave. This is\nequivalent to the non-negativity of the Dirichlet functional\n                                                     ˆ\n                       Jω (φ, ψ) := Eω (φ) − Eω (ψ) + (ψ − φ) MAω (φ),\n\nwhich is more explicitly given by the familiar expression\n                                           ˆ\n                                         1\n                             Jω (φ, ψ) =     (φ − ψ)ddc (ψ − φ)\n                                         2\nwhen n = 1, and a positive linear combination of integrals of the form\n                     ˆ\n                       (φ − ψ)ddc (ψ − φ) ∧ ωφj ∧ ωψn−j−1 (0 ≤ j < n)\n\nin general, see (1.31). Our first main result shows that the Dirichlet functional induces, via\nthe Monge–Ampère operator, a complete quasi-metric4 space structure on M1ω .\nTheorem A. Assume that ω has the orthogonality property. Then:\n   (i) the image of the Monge–Ampère operator MAω : Dω → M is a dense subspace of\n       M1ω ;\n  (ii) there exists a unique (continuous) quasi-metric δω on M1ω that defines the strong\n       topology of M1ω and such that\n                                δω (MAω (φ), MAω (ψ)) = Jω (φ, ψ)\n        for all φ, ψ ∈ Dω ;\n  (iii) the quasi-metric space (M1ω , δω ) is complete.\n  The energy can be expressed in terms of the quasi-metric as\n                    Jω (µ) = δω (µ, µω )    where   µω := Vω−1 ω n = MAω (0).\nWe refer to Definition 2.15 for the precise definition of the orthogonality property. Suf-\nfice it to say here that it only depends on [ω] ∈ Pos(X), and holds when X is a com-\npact Kähler manifold, or any projective Berkovich space X over a non-Archimedean field\n(as a consequence of [BE21, BGM22]). In the former case, Theorem A can be deduced\n  3This corresponds to E∨ (µ) in the notation of [BBGZ13, BoJ22a], and to ∥µ∥ in that of [BoJ22b].\n                          ω                                                  ω\n  4See §1.1 for the notion of quasi-metric used in this paper.\n\f4                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nfrom [BBGZ13, BBEGZ19]; in the latter, it was established in the trivially valued case\nin [BoJ22a], and is thus extended here to the case of an arbitrary non-Archimedean ground\nfield.\n   The strategy of proof of Theorem A follows the same lines as the trivially case treated\nin [BoJ22a]. The first key ingredient is a uniform differentiability property for the Legendre\n",
      "application_check": "Theorem A completes the space of measures and makes test-MA image dense. It does not identify that completion with an actual finite-energy psh potential space on a singular X. No such implication is used."
    },
    {
      "id": "ps-arbitrary-field-warning",
      "source": "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.txt",
      "source_sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 1977,
      "line_end": 1996,
      "character_start": 130015,
      "source_locator": "Theorem 4.3 and Remarks 4.4-4.5, p. 35",
      "pdf_page_range_from_formfeeds": [
        35,
        35
      ],
      "literal_file": "source-extracts/ps-arbitrary-field-warning.txt",
      "literal_sha256": "7e2d5116cfe8e6203038d36ff7c3f2761d00d74d198dbabfd75e480c67789452",
      "literal_extract": "                      X                           X\n  The Monge-Ampère measure can then be extended by density to more general metrics:\nTheorem 4.3. [BE21, thm. 8.4]\nLet K be a complete valued field, X/K an n-dimensional projective scheme and L1 ,...,Ln\nline bundles on X. Then the Monge-Ampère operator:\n                             (φ1 , ..., φn ) 7→ ddc φ1 ∧ ... ∧ ddc φn\nadmits a unique extension to continuous psh metrics on the Li . The extension is further-\nmore continuous with respect to the topology of uniform convergence and the weak topology\nof Radon measures.\nRemark 4.4. While the class E 1 (X, L) of finite-energy psh metrics on L is defined over any\nnon-archimedean field K, it is unclear in general how to extend the Monge-Ampère operator\non the latter. Note however that in the case where K is discretely-valued of characteristic\nzero, this extension was constructed in [BFJ16], and the trivially-valued case was handled\nin [BJ22].\nRemark 4.5. The Chambert-Loir - Ducros [CLD12] approach to pluripotential theory on\nBerkovich spaces makes sense of the curvature current ddc φ of a continuous psh metric,\nand its wedge products, in a spirit close to the work of Bedford-Taylor in the complex case.\nNotably, [CLD12, thm. 6.9.3] states that the wedge product ddc φ1 ∧ ... ∧ ddc φn coincides\nwith the mixed Monge-Ampère measure as described in example 4.1 when φ1 ,..., φn are psh\nmodel metrics, whence the notation.\n",
      "application_check": "Continuous-metric operator over arbitrary fields is distinguished from the finite-energy operator. Remark 4.4 is reported with its own characteristic-zero wording; it is not used to weaken BFJ residue-characteristic hypotheses."
    },
    {
      "id": "gr-no-ma-claim",
      "source": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
      "source_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
      "selection_method": "Newline-only splitting; inclusive 1-based bounds (same as rg)",
      "line_start": 67,
      "line_end": 86,
      "character_start": 5928,
      "source_locator": "Introduction, p. 2",
      "pdf_page_range_from_formfeeds": [
        2,
        2
      ],
      "literal_file": "source-extracts/gr-no-ma-claim.txt",
      "literal_sha256": "9d0a394c5e839e78741b666180074f0f1bf934ee4b9f6aa428ed5fbd3ce1cfff",
      "literal_extract": "fines a semipositive metric on a line bundle L over a projective k-variety X to be the\nuniform limit of metrics induced by nef models. This approach is used in Arakelov ge-\nometry for various arithmetic applications. For an ample class θ on X , Boucksom and\nJonsson [BJ22] give a far reaching global pluripotential theory on a projective variety\nover a trivially valued field. Some parts work for any non-Archimedean field, at least in\nresidue characteristic zero. These psh functions might be singular, and the definition uses\ndecreasing limits of semipositive model functions as in Zhang’s approach. Chambert–Loir\nand Ducros [CD25] have posted a second version of their work in which they give a new\ndefinition of psh functions which is functorial and is based on a transfinite regularization\nprocess.\n   In all of the above approaches, a maximum principle for plurisubharmonic functions\nis missing. In this paper, we propose another class of psh functions called classically\nplurisubharmonic functions in close analogy to the complex case. The definition is local,\nthe functions are upper semicontinuous, and we will show that properties (1)–(4) are\nsatisfied. It will be clear that classically psh functions form a maximal class of reasonable\nplurisubharmonic functions that is compatible with Thuillier’s definition for curves. In\nparticular, the psh functions from the above are classically psh (see 1.2 below).\n   To get regularization by smooth psh functions in the sense of Chambert-Loir and Ducros\nor to define a Monge–Ampère measure for psh functions, additional hypotheses as in\n[CD25] might be needed, but that is not the subject of this paper.\n",
      "application_check": "The September 2025 v2 treats singular analytic curves and classically psh functions but explicitly does not construct the Monge-Ampere operator in this paper. Thus its local theory is not used as the missing global equation theorem."
    }
  ],
  "pdf_rechecks": [
    {
      "id": "BFJ-equation-first-page",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf",
      "pdf_pages": [
        1,
        1
      ],
      "argv": [
        "pdftotext",
        "-f",
        "1",
        "-l",
        "1",
        "-layout",
        "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf",
        "/workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo/source-extracts/BFJ-equation-first-page.txt"
      ],
      "returncode": 0,
      "literal_file": "source-extracts/BFJ-equation-first-page.txt",
      "literal_extract": "                                          SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION\n\n                                                      SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\narXiv:1201.0188v1 [math.AG] 30 Dec 2011\n\n\n\n\n                                                Abstract. Let X be a smooth projective Berkovich space over a complete discrete valu-\n                                                ation ﬁeld K of residue characteristic zero, and assume that X is deﬁned over a function\n                                                ﬁeld admitting K as a completion. Let further µ be a positive measure on X and L be\n                                                an ample line bundle such that the mass of µ is equal to the degree of L. Then we show\n                                                the existence a continuous semipositive metric whose associated measure is equal to µ in\n                                                the sense of Zhang and Chambert-Loir. This we do under a technical assumption on the\n                                                support of µ, which is, for instance, fulﬁlled if the support is a ﬁnite set of divisorial points.\n                                                Our method draws on analogues of the variational approach developed to solve complex\n                                                Monge-Ampère equations on compact Kähler manifolds by Berman, Guedj, Zeriahi and the\n                                                ﬁrst named author, and of Kolodziej’s C 0 -estimates. It relies in a crucial way on the com-\n                                                pactness properties of singular semipositive metrics, as deﬁned and studied in a companion\n                                                article.\n\n\n\n\n                                                                                         Contents\n                                           1. Introduction                                                                                            2\n                                           2. Background                                                                                              8\n                                           3. Monge-Ampère operator on bounded functions                                                            16\n                                           4. Capacity and quasicontinuity                                                                           20\n                                           5. Locality and the comparison principle                                                                  23\n                                           6. Energy                                                                                                 25\n                                           7. Envelopes and diﬀerentiability                                                                         30\n                                           8. The Monge-Ampère equation                                                                             33\n                                           9. Curves and toric varieties                                                                             38\n                                           Appendix A. Orthogonality                                                                                 40\n                                           References                                                                                                45\n\n\n\n\n                                           Date: October 29, 2018.\n                                                                                                1\n\f",
      "check": "Fresh extraction from the supplied PDF, retaining the displayed theorem statements and formulas rather than relying on the cache title or OCR alone."
    },
    {
      "id": "BJ-page35-from-pdf",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
      "pdf_pages": [
        35,
        35
      ],
      "argv": [
        "pdftotext",
        "-f",
        "35",
        "-l",
        "35",
        "-layout",
        "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
        "/workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo/source-extracts/BJ-page35-from-pdf.txt"
      ],
      "returncode": 0,
      "literal_file": "source-extracts/BJ-page35-from-pdf.txt",
      "literal_extract": "             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        35\n\n    (ii) for each c ∈ R and t ∈ Q>0 , ϕ + c and t · ϕ are θ-psh;\n   (iii) if θ = θ0 and ϕ, ϕ0 ∈ PL, then max{ϕ, ϕ0 } ∈ PL is θ-psh;\n   (iv) ϕ is decreasing with respect to the partial order on X an , and hence satisfies (1.4)\n         (see Lemma 1.4);\n    (v) for any morphism f : Y → X from a projective variety, f ? ϕ is f ? θ-psh;\n   (vi) if we further assume that f : Y → X is surjective, then\n                   ϕ θ-psh ⇐⇒ ϕ|Xαan θ|Xα -psh for all α ⇐⇒ f ? ϕ f ? θ-psh.\n  In particular, (i) shows that PLR ∩ PSH(θ) is a convex subset of PLR .\nLemma 3.7. For any θ ∈ N1 (X) and ϕ ∈ PLR ∩ PSH(θ), there exists a sequence ϕm ∈\nH(Lm ) with Lm ∈ Pic(X)Q such that ϕm → ϕ uniformly on X an and c1 (Lm ) → θ.\nProof. Pick a test configuration X dominating Xtriv and D ∈ VCar(X )R such that ϕ = ϕD .\nBy openness of the (relatively) ample cone of N1 (X /A1 ), we can find a sequence of Q-\nline bundles Lm on X and Dm ∈ VCar(X )Q such that c1 (Lm ) → θ in N1 (X), Dm → D\nin VCar(X )R , and c1 (Lm )X + Dm ∈ N1 (X /A1 ) is ample for all i. In particular, Lm :=\n(Lm )X +Dm is a semiample test configuration for L, and hence ϕm := ϕLm = ϕDm ∈ H(Lm ).\nFurthermore, Dm → D implies ϕm → ϕ uniformly.                                          \u0003\nProof of Proposition 3.6. Pick a test configuration X dominating Xtriv and D, D0 ∈ VCar(X )R\nthat determine ϕ, ϕ0 . By assumption, θX + D and θX   0 + D 0 are nef. Thus\n\n       (θ + θ0 )X + D + D0 = (θX + D) + θX   0\n                                               + D0\n                                                    \u0001\n                                                        and (tθ)X + tD = t (θX + D)\nare nef as well, proving (i).\n   For each c ∈ R we have ϕ + c = ϕD+cX0 . Since X0 = π ? (0) vanishes in N1 (X /A1 ),\nθX + D + cX0 is nef, and ϕ + c is thus θ-psh. To prove the remaining part of (ii), it suffices to\nprove that if d ∈ Z>0 , then ϕ is θ-psh iff d · ϕ is θ-psh. In view of Lemma 2.34, this follows\nfrom the fact that θX + D ∈ N1 (X /A1 ) is nef iff its pullback under the base change of X\nwith respect to $ 7→ $d is nef.\n   Assume now θ = θ0 and D, D0 ∈ VCar(X )Q . By openness of Amp(X), we can find an\nQ-line bundle L on X such that c1 (L) − θ is ample and arbitrarily small. Then ϕ, ϕ0 are\nL-psh, and it will be enough to show that max{ϕ, ϕ0 } is L-psh as well, by Lemma 3.5. After\nperhaps passing to a higher test configuration, we may assume that X supports an ample\ntest configuration L for L (Lemma 2.33). For each ε ∈ Q>0 , the Q-line bundle LX + D + εL\nis ample, and hence semiample. Thus ϕ + εϕL is Fubini–Study for (1 + ε)L, and similarly\nfor ϕ0 + εϕL . By Proposition 2.19, it follows that\n                        max{ϕ + εϕL , ϕ0 + εϕL } = max{ϕ, ϕ0 } + εϕL\nis Fubini–Study for (1 + ε)L, and hence (1 + ε)L-psh. Using Lemma 3.5 we conclude, as\ndesired, that max{ϕ, ϕ0 } is L-psh. This proves (iii).\n    By Proposition 2.19, any Fubini–Study function is decreasing, and (iv) thus follows from\nLemma 3.7.\n    To prove (v), note that the Gm -equivariant rational map Y × Gm 99K X induced by f\nadmits a Gm -equivariant resolution of indeterminacies, which is thus a test configuration Y\nfor Y dominating Ytriv . Also denoting by f : Y → X the corresponding morphism, we have\nf ? ϕ = ϕf ? D , and the result thus follows from the fact that θY + f ? D = f ? (θX + D) is nef,\nas the pullback of a nef class. If f : Y → X is surjective, then f : Y → X is surjective as\nwell, and (vi) follows.                                                                        \u0003\n\f",
      "check": "Fresh extraction from the supplied PDF, retaining the displayed theorem statements and formulas rather than relying on the cache title or OCR alone."
    },
    {
      "id": "BJ-page75-from-pdf",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
      "pdf_pages": [
        75,
        75
      ],
      "argv": [
        "pdftotext",
        "-f",
        "75",
        "-l",
        "75",
        "-layout",
        "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
        "/workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo/source-extracts/BJ-page75-from-pdf.txt"
      ],
      "returncode": 0,
      "literal_file": "source-extracts/BJ-page75-from-pdf.txt",
      "literal_extract": "                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                                       75\n\nTheorem 7.1. For each (n + 1)-tuple ω0 , . . . , ωn ∈ Amp(X), the energy pairing\n                           (ϕ0 , . . . , ϕn ) 7→ (ω0 , ϕ0 ) · . . . · (ωn , ϕn )\nadmits a unique extension to a map ni=0 PSH(ωi ) → R ∪ {−∞} that is\n                                          Q\n\n     • upper semicontinuous;\n     • increasing in each variable.\nFurthermore, this map is continuous along decreasing nets, and satisfies\n                  (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =             inf             (ω0 , ψ0 ) · . . . · (ωn , ψn )              (7.1)\n                                                       ψi ∈Hdom (ωi ), ψi ≥ϕi\n                  Q\nfor all (ϕi ) ∈       i PSH(ωi ).\n\nProof. Any map that is both usc and increasing is automatically continuous along decreasing\nnets. Since all functions in PSH(ωi ) are limits of decreasing nets in Hdom (ωi ) ⊂ PL(X) ∩\nPSH(ωi ), uniqueness is clear. To prove existence, it suffices to show that (7.1) has the\nrequired properties.\n  Monotonicity is obvious. To prove upper semicontinuity, suppose that ϕi ∈ PSH(ωi ),\n0 ≤ i ≤ n, and t ∈ R satisfy\n                                (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) < t,\nBy definition, we can choose ψi ∈ Hdom (ωi ) and 0 < ε \u001c 1 such that ϕi ≤ ψi and\n                                        (ω0 , ψ0 ) · . . . · (ωn , ψn ) < t − ε.\nSet                                          X\n                                     C :=     (ω0 · . . . · ωbi · . . . · ωn ) > 0.\n                                               i\nBy Proposition 4.28, ϕ 7→ sup(ϕ − ψi ) is continuous on PSH(ωi ), and we can thus find an\nopen neighborhood Ui of ϕi in PSH(ωi ) such that ϕ0i ≤ ψi + εC −1 for all ϕ0i ∈ Ui . By\nmonotonicity of the energy pairing and Proposition 3.14, this gives\n                   (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n ) ≤ (ω0 , ψ0 + εC −1 ) · . . . · (ωn , ψn + εC −1 )\n                                = (ω0 , ψ0 ) · . . . · (ωn , ψn ) + ε < t\n         0\nfor all ϕi ∈ Ui , which proves upper semicontinuity.                                                                             \u0003\nProposition 7.2. The energy pairing (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) is symmetric and R>0 -linear\nwith respect to each variable (ωi , ϕi ) with ωi ∈ Amp(X) and ϕi ∈ PSH(ωi ). Furthermore,\n\n                                                                                    n\n                                                                                    X\n (ω0 , ϕ0 + c0 ) · . . . · (ωn , ϕn + cn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) +            ci (ω0 · . . . · ωbi · . . . · ωn )X (7.2)\n                                                                                    i=0\nfor all ci ∈ R,\n                         (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ) = t(ω0 , ϕ0 ) · . . . · (ωn , ϕn )                          (7.3)\nfor all t ∈ R>0 ,\n                                                          X\n                   (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =              (ω0 , ϕ0 )|Xα · . . . · (ωn , ϕn )|Xα ,                    (7.4)\n                                                       dim Xα =n\nand\n                 (ν ? ω0 , ν ? ϕ0 ) · . . . · (ν ? ωn , ν ? ϕn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn )                           (7.5)\nwith ν : X ν → X the normalization morphism.\n\f",
      "check": "Fresh extraction from the supplied PDF, retaining the displayed theorem statements and formulas rather than relying on the cache title or OCR alone."
    },
    {
      "id": "BJ-page82-from-pdf",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
      "pdf_pages": [
        82,
        82
      ],
      "argv": [
        "pdftotext",
        "-f",
        "82",
        "-l",
        "82",
        "-layout",
        "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
        "/workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo/source-extracts/BJ-page82-from-pdf.txt"
      ],
      "returncode": 0,
      "literal_file": "source-extracts/BJ-page82-from-pdf.txt",
      "literal_extract": "82                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nProposition 7.19. Mixed Monge–Ampère measures satisfy the following properties:\n   (i) the signed measure i (θi + ddc ϕi ) is a symmetric and multilinear function of the\n                              V\n\n       n-tuple (θi , ϕi ) ∈ N1 (X) × E~1 , of total mass\n                             ˆ     ^\n                                     (θi + ddc ϕi ) = (θ1 · . . . · θn )X ;\n                                       X an i\n\n     (ii) assume (θi , ϕi ) ∈ N1 (X) × PLR , and pick an integrally closed test configuration X\n          dominating Xtriv and Di ∈ VCar(X )R such that ϕi = ϕDi ; then\n                                   ^                   X\n                                      (θi + ddc ϕi ) =   cE δvE ,\n                                           i                          E\n\n          where E ranges over the irreducible components of X0 and\n                         cE := ordE (X0 )(θ1,X + D1 )|E · . . . · (θn,X + Dn )|E ;\n     (iii) for all (θi , ϕi ) ∈ N1 (X) × E~1 and t ∈ R>0 we have\n                                 ^                           ^\n                                    (θi + ddc (t · ϕi )) = t? (θi + ddc ϕi ),                    (7.16)\n                                   i                                   i\n                        ^                              X        ^\n                             (θi + ddc ϕi ) =                          θi |Xα + ddc ϕi |Xαan ,\n                                                                                            \u0001\n                                                                                                 (7.17)\n                         i                          dim Xα =n i\n                              ^                              ^\n                                       (θi + ddc ϕi ) = ν?          (ν ? θi + ddc ν ? ϕi ) ,     (7.18)\n                               i                                i\n          with ν : X ν → X the normalization;\n     (iv) for any ω ∈ Amp(X), the map E 1 (ω)n 3 (ϕ1 , . . . , ϕn ) 7→ i (θi +ddc ϕi ) is continuous\n                                                                      V\n          along decreasing nets;\n      (v) for all (θi , ϕi ) ∈ N1 (X) × E~1 and ϕ ∈ E~1 , ϕ is integrable against i (θi + ddc ϕi ),\n                                                                                   V\n          and (7.15) holds.\n  When ϕi = 0 for some i, we drop the term ddc ϕi from the notation. As a special case of\nProposition 7.19 (ii), we then have\n                                          X\n                        θ1 ∧ · · · ∧ θn =   (θ1 · . . . · θn )Xα δvtriv,α .        (7.19)\n                                                    dim Xα =n\n\nProof of Proposition 7.19. Points (i) and (iii) follow from Proposition 7.2, while (ii) is a\nreformulation of (3.5). By density of PL(X) in C0 (X), (iv) is equivalent to the fact that,\nfor each ϕ ∈ PL(X),\n                                 ˆ  ^\n            (ϕ1 , . . . , ϕn ) 7→ ϕ   (θi + ddc ϕi ) = (0, ϕ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn )\n                                                i\n\nis continuous along decreasing nets in E 1 (ω)n+1 . Now ϕ can be written as a difference of\nfunctions in PL ∩ PSH(ω 0 ) for some ω 0 ∈ Amp(X), and the desired continuity is thus a\nconsequence of Theorem 7.14. To prove (v), we may assume θi ∈ Amp(X) and ϕi ∈ E 1 (θi ),\nby multilinearity. Any ϕ ∈ E 1 (ω) with ω ∈ Amp(X) can be written as the pointwise limit\nof a decreasing net in PL ∩ PSH(ω), and (7.15) thus holds for ϕ, by monotone convergence\nand the continuity of the energy pairing along decreasing limits.                        \u0003\n\f",
      "check": "Fresh extraction from the supplied PDF, retaining the displayed theorem statements and formulas rather than relying on the cache title or OCR alone."
    },
    {
      "id": "BJ-page98-from-pdf",
      "pdf": "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
      "pdf_pages": [
        98,
        98
      ],
      "argv": [
        "pdftotext",
        "-f",
        "98",
        "-l",
        "98",
        "-layout",
        "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
        "/workspace/research/campaigns/round-45/P16.1-public-source-singular-finite-energy-equations/artifacts/codex-ZDgZTo/source-extracts/BJ-page98-from-pdf.txt"
      ],
      "returncode": 0,
      "literal_file": "source-extracts/BJ-page98-from-pdf.txt",
      "literal_extract": "98                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\nCorollary 8.6. For any ϕ ∈ E 1 and f ∈ C0 (X) we have\n                                               ˆ\n                           d       ↓\n                                 E (ϕ + tf ) = f MA(ϕ).\n                          dt t=0\n\n  Again, one can replace E↓ with E = E ◦ P if ϕ ∈ CPSH(ω), or if the envelope property\nholds.\n  For any ω ∈ Amp(X) we set Vω := (ω n ).\nLemma 8.7. Pick ω, ω 0 ∈ Amp(X), ψ1 , ψ2 ∈ PLR ∩ PSH(ω 0 ), and set f := ψ1 − ψ2 . For\nany ϕ ∈ CPSH(ω) we then have\n                               ˆ\n                            −1\n                                                           \u0001n\n                                 f ω + ω 0 + ddc (ϕ + ψ1 )    ≤ Vω−1 Vω+ω0 − 1 sup |f |.\n                                                                              \u0001\n    Eω (ϕ + f ) − Eω (ϕ) − Vω\n\nProof. We may assume ω = c1 (L), ω 0 = c1 (L0 ) for ample line bundles L, L0 on X, Indeed, by\nhomogeneity, we then obtain the case when L, L0 are ample Q-line bundles, and the general\ncase by a simple perturbation argument based on Proposition 8.1 (iii).\n   Consider first any continuous function ρ ∈ C0 (X). For each m ∈ N, ρ defines a sup-norm\nk · kmρ on H0 (X, mL), defined by\n                                   kskmρ = sup |s|e−mρ .\n                                             X an\n\nThis norm induces a norm det k · kmρ on the determinant line det H0 (X, mL). Comparing\nwith the trivial norm, we can and will think of det k · kmρ as a number. It now follows\nfrom [CMac15] (see [BE20, Theorem 9.5]) that the volume\n                                                1\n                        volL (ρ) := − lim             log det k · kmρ\n                                      m→∞ mh0 (mL)\n\nexists in R. We claim that volL (ρ) = EL (ρ). Using [BE20, (9.7)] and (8.3), it is enough\nto prove this when X is irreducible. When ρ ∈ CPSH(L), the equality holds by [BE20,\nTheorem A] (or [BoJ18b, Lemma 4.5]). In the general case, this yields\n                  EL (ρ) = sup {EL (ψ) | ψ ∈ CPSH(L), ψ ≤ ρ} ≤ volL (ρ),\nby monotonicity of volL . On the other hand, Theorem 5.1.1 of [Reb21] (which is valid for\narbitrary non-Archimedean fields; see also [BoJ18b, Theorem 4.13] for the trivially valued\ncase) shows that\n                                                           |s|\n                           ρm := m−1 log       sup\n                                             0\n                                          s∈H (X,mL)\\{0} ksk mρ\n\nsatisfies ρm ∈ PLR ∩ PSH(ω), ρm ≤ ρ and EL (ρm ) → volL (ρ); the claim follows.\n   In particular, EL (ϕ + f ) = volL (ϕ + f ) and EL (ϕ) = volL (ϕ). The desired estimate is\nnow a consequence of Lemma 8.8 below, itself a reformulation of [BGM20, Lemma 3.2]. \u0003\nLemma 8.8. Let L and L0 be ample line bundles on X, and set ω = c1 (L), ω 0 = c1 (L0 ).\nConsider functions ϕ ∈ CPSH(ω), and ψ1 , ψ2 ∈ CPSH(ω 0 ). Set f := ψ1 − ψ2 ∈ C0 and\nC := Vω+ω0 − Vω > 0. Then\n               ˆ\n    C inf\n        an\n           f≤      f (ω + ω 0 + ddc (ϕ + ψ1 ))n − Vω (volL (ϕ + f ) − volL (ϕ)) ≤ C sup f.\n       X        X an                                                              X an\n\f",
      "check": "Fresh extraction from the supplied PDF, retaining the displayed theorem statements and formulas rather than relying on the cache title or OCR alone."
    }
  ],
  "evidence_limit": "Hashes establish byte identity, not correctness. Extracts are literal published mathematical data; application checks and the new proofs remain unverified drafts."
}


## Literal published unit: BFJ-equation-first-page.txt

                                          SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION

                                                      SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON
arXiv:1201.0188v1 [math.AG] 30 Dec 2011




                                                Abstract. Let X be a smooth projective Berkovich space over a complete discrete valu-
                                                ation ﬁeld K of residue characteristic zero, and assume that X is deﬁned over a function
                                                ﬁeld admitting K as a completion. Let further µ be a positive measure on X and L be
                                                an ample line bundle such that the mass of µ is equal to the degree of L. Then we show
                                                the existence a continuous semipositive metric whose associated measure is equal to µ in
                                                the sense of Zhang and Chambert-Loir. This we do under a technical assumption on the
                                                support of µ, which is, for instance, fulﬁlled if the support is a ﬁnite set of divisorial points.
                                                Our method draws on analogues of the variational approach developed to solve complex
                                                Monge-Ampère equations on compact Kähler manifolds by Berman, Guedj, Zeriahi and the
                                                ﬁrst named author, and of Kolodziej’s C 0 -estimates. It relies in a crucial way on the com-
                                                pactness properties of singular semipositive metrics, as deﬁned and studied in a companion
                                                article.




                                                                                         Contents
                                           1. Introduction                                                                                            2
                                           2. Background                                                                                              8
                                           3. Monge-Ampère operator on bounded functions                                                            16
                                           4. Capacity and quasicontinuity                                                                           20
                                           5. Locality and the comparison principle                                                                  23
                                           6. Energy                                                                                                 25
                                           7. Envelopes and diﬀerentiability                                                                         30
                                           8. The Monge-Ampère equation                                                                             33
                                           9. Curves and toric varieties                                                                             38
                                           Appendix A. Orthogonality                                                                                 40
                                           References                                                                                                45




                                           Date: October 29, 2018.
                                                                                                1


## Literal published unit: BJ-page35-from-pdf.txt

             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        35

    (ii) for each c ∈ R and t ∈ Q>0 , ϕ + c and t · ϕ are θ-psh;
   (iii) if θ = θ0 and ϕ, ϕ0 ∈ PL, then max{ϕ, ϕ0 } ∈ PL is θ-psh;
   (iv) ϕ is decreasing with respect to the partial order on X an , and hence satisfies (1.4)
         (see Lemma 1.4);
    (v) for any morphism f : Y → X from a projective variety, f ? ϕ is f ? θ-psh;
   (vi) if we further assume that f : Y → X is surjective, then
                   ϕ θ-psh ⇐⇒ ϕ|Xαan θ|Xα -psh for all α ⇐⇒ f ? ϕ f ? θ-psh.
  In particular, (i) shows that PLR ∩ PSH(θ) is a convex subset of PLR .
Lemma 3.7. For any θ ∈ N1 (X) and ϕ ∈ PLR ∩ PSH(θ), there exists a sequence ϕm ∈
H(Lm ) with Lm ∈ Pic(X)Q such that ϕm → ϕ uniformly on X an and c1 (Lm ) → θ.
Proof. Pick a test configuration X dominating Xtriv and D ∈ VCar(X )R such that ϕ = ϕD .
By openness of the (relatively) ample cone of N1 (X /A1 ), we can find a sequence of Q-
line bundles Lm on X and Dm ∈ VCar(X )Q such that c1 (Lm ) → θ in N1 (X), Dm → D
in VCar(X )R , and c1 (Lm )X + Dm ∈ N1 (X /A1 ) is ample for all i. In particular, Lm :=
(Lm )X +Dm is a semiample test configuration for L, and hence ϕm := ϕLm = ϕDm ∈ H(Lm ).
Furthermore, Dm → D implies ϕm → ϕ uniformly.                                          
Proof of Proposition 3.6. Pick a test configuration X dominating Xtriv and D, D0 ∈ VCar(X )R
that determine ϕ, ϕ0 . By assumption, θX + D and θX   0 + D 0 are nef. Thus

       (θ + θ0 )X + D + D0 = (θX + D) + θX   0
                                               + D0
                                                    
                                                        and (tθ)X + tD = t (θX + D)
are nef as well, proving (i).
   For each c ∈ R we have ϕ + c = ϕD+cX0 . Since X0 = π ? (0) vanishes in N1 (X /A1 ),
θX + D + cX0 is nef, and ϕ + c is thus θ-psh. To prove the remaining part of (ii), it suffices to
prove that if d ∈ Z>0 , then ϕ is θ-psh iff d · ϕ is θ-psh. In view of Lemma 2.34, this follows
from the fact that θX + D ∈ N1 (X /A1 ) is nef iff its pullback under the base change of X
with respect to $ 7→ $d is nef.
   Assume now θ = θ0 and D, D0 ∈ VCar(X )Q . By openness of Amp(X), we can find an
Q-line bundle L on X such that c1 (L) − θ is ample and arbitrarily small. Then ϕ, ϕ0 are
L-psh, and it will be enough to show that max{ϕ, ϕ0 } is L-psh as well, by Lemma 3.5. After
perhaps passing to a higher test configuration, we may assume that X supports an ample
test configuration L for L (Lemma 2.33). For each ε ∈ Q>0 , the Q-line bundle LX + D + εL
is ample, and hence semiample. Thus ϕ + εϕL is Fubini–Study for (1 + ε)L, and similarly
for ϕ0 + εϕL . By Proposition 2.19, it follows that
                        max{ϕ + εϕL , ϕ0 + εϕL } = max{ϕ, ϕ0 } + εϕL
is Fubini–Study for (1 + ε)L, and hence (1 + ε)L-psh. Using Lemma 3.5 we conclude, as
desired, that max{ϕ, ϕ0 } is L-psh. This proves (iii).
    By Proposition 2.19, any Fubini–Study function is decreasing, and (iv) thus follows from
Lemma 3.7.
    To prove (v), note that the Gm -equivariant rational map Y × Gm 99K X induced by f
admits a Gm -equivariant resolution of indeterminacies, which is thus a test configuration Y
for Y dominating Ytriv . Also denoting by f : Y → X the corresponding morphism, we have
f ? ϕ = ϕf ? D , and the result thus follows from the fact that θY + f ? D = f ? (θX + D) is nef,
as the pullback of a nef class. If f : Y → X is surjective, then f : Y → X is surjective as
well, and (vi) follows.                                                                        


## Literal published unit: BJ-page75-from-pdf.txt

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
                         (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ) = t(ω0 , ϕ0 ) · . . . · (ωn , ϕn )                          (7.3)
for all t ∈ R>0 ,
                                                          X
                   (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =              (ω0 , ϕ0 )|Xα · . . . · (ωn , ϕn )|Xα ,                    (7.4)
                                                       dim Xα =n
and
                 (ν ? ω0 , ν ? ϕ0 ) · . . . · (ν ? ωn , ν ? ϕn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn )                           (7.5)
with ν : X ν → X the normalization morphism.


## Literal published unit: BJ-page82-from-pdf.txt

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


## Literal published unit: BJ-page98-from-pdf.txt

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


## Literal published unit: be-energy-projection-proof.txt

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
of mixed Monge–Ampère measures with ground field extension, cf. Proposition 8.3. Finally,
(vii) is a consequence of (9.11) and the projection formula µ⋆ δX ′ = δX .                    
9.4. Proof of Theorem A. The following result corresponds to Theorem A in the intro-
duction. It was first established in [BB10] when K is Archimedean, and in [BG+16] when
K is discretely valued.
Theorem 9.15. Let X be a geometrically reduced projective K-scheme, and L be a semi-


## Literal published unit: be-not-pluripotential-paper.txt

                                          j=0

We use additive notation for metrics on line bundles, so that φ − ψ is a function on X, and
ddc φ, ddc ψ denote the curvature (1, 1)-forms of φ, ψ.

   Consider now an arbitrary complete valued field K, i.e. a field K complete with respect to
an absolute value. In the Archimedean case, K = R or C, by the Gelfand–Mazur theorem.
In the non-Archimedean case, the main examples are K = Qp , Cp , or fields of formal
Laurent series and their completed algebraic closure, but the trivially valued case is also
important for the study of K-stability (see [BJ18b]). Let X be a geometrically reduced
projective scheme over K, L be a line bundle on X, and φ, ψ be continuous metrics on
(the Berkovich analytification of) L. Building on a result of Chen and Maclean based on
Okounkov bodies [CMac15], we show the existence of the relative volume of φ, ψ
                                         n!
                      vol(L, φ, ψ) := lim     vol (k · kmφ , k · kmψ ) ∈ R,                     (0.3)
                                  m→∞ mn+1
cf. Theorem 9.8. The main result of the present paper is as follows.
Theorem A. Let X be a geometrically reduced projective scheme over any complete valued
field K, and φ, ψ be continuous psh2 metrics on an ample line bundle L over X. Then
                                        vol(L, φ, ψ) = E(φ, ψ).
   In the Archimedean case, it follows from results of Demailly that a continuous metric
on L is psh iff it is a uniform limit of Fubini–Study metrics (see Theorem 7.1). In the
non-Archimedean case, we use this as a definition, and prove compatibility with the more
common notion of semipositive metric in this context, due to S.W. Zhang and involving
nef models, when K is nontrivially valued. We also show that a continuous metric φ is
psh iff it becomes psh after ground field extension. The relative Monge–Ampère energy of
continuous psh metrics can still be defined by (0.2), the latter being understood in the sense
of Chamber-Loir and Ducros [CLD12] in the non-Archimedean sense.
   In the Archimedean case, Theorem A reduces to [BB10] after passing to a resolution of
singularities. In the discretely valued case, it was established in [BG+16, Theorem A]. The
main contribution of the present paper is thus to establish Theorem A for a densely valued,
non-Archimedean ground field K.
  1Note that the present normalization, which is more convenient for the purpose of this paper, is not
uniform accross the literature.
   2A shorthand for plurisubharmonic.
4                        SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON

   The psh envelope P(φ) of a continuous metric φ on L is defined as the pointwise supremum
of the family of all continuous psh metrics ψ on L such that ψ ≤ φ. We say that continuity
of envelopes holds for (X, L) if P(φ) is continuous (and hence psh) for each continuous metric
φ on L.
Corollary B. Assume that continuity of envelopes holds for (X, L). For any two continuous
metrics φ, ψ on L, we then have
                                 vol(L, φ, ψ) = E(P(φ), P(ψ)).
   In the Archimedean case, classical results in pluripotential imply that continuity of en-
velopes holds whenever X is normal, and Corollary B is indeed also a consequence of [BB10]
in that case.
   In the non-Archimedean case, we similarly expect continuity of envelopes to holds as soon
as X is normal. As of this writing, continuity of envelopes (and hence Corollary B) has been
established when X is smooth, and one of the following is satisfied:
      • X is a curve, as a consequence of A. Thuillier’s work [Thu05] (see [GJKM19]);
      • K is discretely or trivially valued, of residue characteristic 0 [BFJ16, BJ18a], building
        on multiplier ideals and the Nadel vanishing theorem;
      • K is discretely valued of characteristic p, (X, L) is defined over a function field
        of transcendence degree d, and resolution of singularities is assumed in dimension
        n + d [GJKM19], replacing multiplier ideals with test ideals.



## Literal published unit: bfj-v1-retained-hypotheses.txt

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
of A. Thuillier [Thu05], who developed a theory of singular semipositive metrics on analytic
curves that is completely analogous to the complex case. Solving (1.1) for curves boils down
to a system of linear equations and relies on the negativity of the intersection form of the
special ﬁber of a suitable model, see §9. Alternatively, one can exploit the structure of the
Berkovich space as a metrized graph as in [BR10, FJ04].
   In higher dimensions, Y. Liu [Liu10] treated the related case when X is a totally degener-
ate abelian variety over Cp , and µ is a (smooth) measure supported on the dual complex of
the canonical formal model of X, as constructed by Mumford. By exploiting the fact that


## Literal published unit: bj-comparison-proof.txt

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


## Literal published unit: bj-continuous-envelopes.txt

Lemma 5.17. For any ω ∈ Amp(X), the following statements are equivalent:
   (i) ω has the envelope property;
  (ii) for any function ϕ : X an → R ∪ {±∞}, we have
                      Pω (ϕ) ≡ −∞, Pω (ϕ)? ≡ +∞, or Pω (ϕ)? ∈ PSH(ω).
     (iii) for any ϕ ∈ C0 (X), Pω (ϕ) is continuous.
     We refer to the property in (iii) as continuity of envelopes.
Proof. First assume (i). Pick any ϕ : X an → R ∪ {±∞}, and suppose that the set F :=
{ψ ∈ PSH(θ) | ψ ≤ ϕ} is nonempty, so that Pω (ϕ) 6≡ −∞. If the functions in F are uniformly
bounded above, then Pω (ϕ)? ∈ PSH(ω), by (i). If not, then, by the definition of the
Alexander–Taylor capacity we have
             Pω (ϕ)(v) = sup {ψ(v) | ψ ∈ F} ≥ sup {sup ψ | ψ ∈ F} − Tω (v) = +∞
for all v ∈ X div , and hence Pω (ϕ)? ≡ +∞, by density of X div . This proves (i)⇒(ii).
   Next we prove (ii)⇒(iii), so pick ϕ ∈ C0 (X). Then Pω (ϕ)? ∈ PSH(ω) is a competitor in
the definition of Pω (ϕ), and hence Pω (ϕ)? ≤ Pω (ϕ). We conclude that Pω (ϕ)? = Pω (ϕ) is
usc. We claim that Pω (ϕ) is also lsc, and hence continuous. To prove the claim, it suffices to
show that Pω (ϕ) is a supremum of continuous functions, and for this it suffices to prove that
for any ψ ∈ PSH(ω) with ψ ≤ ϕ and any ε > 0, there exists ψ 0 ∈ C0 (X) with ψ ≤ ψ 0 ≤ ϕ+ε.
Pick a decreasing net ψi ∈ Hdom (ω) converging pointwise to ψ. For each v ∈ X an , the set
{ψi < ϕ + ε} is an open neighborhood of v for i large enough, by lower semicontinuity of
ϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for all i large enough, so we can
take ψ 0 = ψi .
   Finally, we prove (iii)⇒(i), following [BE20, Lemma 7.30]. Let (ϕi ) be a bounded-above
family in PSH(ω), and set ϕ := sup?i ϕi . Since ϕ is usc and X an is compact, we can find
a decreasing net of continuous functions (ψj ) such that ψj → ϕ. For each i, j, we have
ϕi ≤ ψj , and hence ϕi ≤ Pω (ψj ), which in turn yields ϕ ≤ Pω (ψj ) ≤ ψj . We have thus
written ϕ as the limit of the decreasing net of ω-psh functions Pω (ψj ), which shows that ϕ
is ω-psh.                                                                                    
Corollary 5.18. Assume that ω ∈ Amp(X) has the envelope property, and consider a usc
function ϕ : X an → R ∪ {−∞}. Then:
    (i) Pω (ϕ) is ω-psh, or Pω (ϕ) ≡ −∞;
   (ii) if ϕ is the limit of a decreasing net (ϕj ) of bounded-above, usc functions, then
        Pω (ϕj ) & Pω (ϕ).
Proof. By Lemma 5.17, either ψ := Pω (ϕ)? is ω-psh, or Pω (ϕ) ≡ −∞. Since Pω (ϕ) ≤ ϕ and
ϕ is usc, we also have ψ ≤ ϕ. If ψ is ω-psh, then ψ ≤ Pω (ϕ), which proves (i).
  To see (ii), note that ρ := limj Pω (ϕj ) satisfies either ρ ∈ PSH(ω) or ρ ≡ −∞, by
Theorem 4.7. Furthermore, Pω (ϕj ) ≤ ϕj yields in the limit ρ ≤ ϕ, and hence ρ ≤ Pω (ϕ) (by
definition of Pω (ϕ) if ρ ∈ PSH(ω), and trivially if ρ ≡ −∞). Thus limj Pω (ϕj ) = ρ = Pω (ϕ).
On the other hand, Pω (ϕj ) ≥ Pω (ϕ) implies ρ ≥ Pω (ϕ), which completes the proof of (ii). 
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      61

  For any function ϕ : X an → R ∪ {±∞}, we also introduce the pointwise envelope
                           Qω (ϕ) := sup {ψ ∈ CPSH(ω) | ψ ≤ ϕ} ;
this is lsc and bounded below if ϕ is bounded below, and ≡ −∞ otherwise. Since each
ψ ∈ CPSH(ω) is the uniform limit of functions in Hdom (ω) (see Theorem 4.7), one easily
checks that
                            Qω (ϕ) = sup{ψ ∈ Hdom (ω) | ψ ≤ ϕ}.


## Literal published unit: bj-curve-laplacian.txt

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


## Literal published unit: bj-curve-psh-and-regularization.txt

        holds; in particular,
                                    sup ϕ = max ϕ(vtriv,α ).                               (4.6)
                                              α
   (iii) for any v ∈ X an , t 7→ ϕ(tv) is convex and decreasing on [0, +∞), and ϕ(tv) &
         ϕ(vZ,triv ) = supZ an ϕ as t → +∞, with Z the closure of the center of v.
                                           gf
Proof. By Proposition 2.19 (i), each ϕi ∈ HR  (Li ) is decreasing, and t 7→ ϕi (tv) is convex,
by Lemma 2.20. Since (ϕi ) converges pointwise to ϕ, the latter inherits these properties.
The rest follows from Lemma 1.4.                                                            
Example 4.13. Let X be a smooth irreducible curve, and recall the description of X an given
in §1.1.6. For any θ ∈ N1 (X), a usc function ϕ : X an → R ∪ {−∞} is then θ-psh iff
    (i) for each p ∈ X(k), ϕp (t) := ϕ(t ordp ) is convex on [0, +∞) (and hence decreasing,
        being bounded  above);
   (ii) deg θ + p∈X(k) ϕ0p (0+ ) ≥ 0 (which implies ϕ0p (0+ ) = 0, and hence t 7→ ϕ(t ordp )
                P

        constant, for all but countably many p ∈ X(k)).
Indeed, when ϕ is PL, this follows from Example 3.21, and the general case is obtained by
writing a function satisfying (i) and (ii) as a decreasing limit of PL functions with the same
properties (compare [FJ04, §7] and [Jon12, §2.5]).
  This characterization implies PSH(0) = R when X is a smooth irreducible curve. As in
the complex analytic case, this holds in fact on any connected variety, see Corollary 4.24
below.
Remark 4.14. Any ϕ ∈ PL(X)R is η-psh with respect to some closed (1, 1)-form η, in the
sense of Remark 3.4. However, ϕ is in general not θ-psh for any θ ∈ N1 (X), since such
functions must be decreasing in the partial ordering on X an (see Proposition 4.12 ). As a
result, several potential definitions of quasi-psh functions coexist in our context.
4.3. The regularization theorem. Many properties of θ-psh functions are obtained by
regularization, that is, approximation by nicer θ-psh functions. In our present approach,
regularization of θ-psh functions is built into their definition. One can, however, improve
the properties of the approximants as follows:
Theorem 4.15. Pick θ ∈ N1 (X) and ϕ ∈ PSH(θ). Then:
                                                                   gf
     (i) ϕ can be written as the limit of a decreasing net ϕi ∈ HQ    (Li ) with Li ∈ Pic(X)Q
         such that c1 (Li ) − θ is ample and limi c1 (Li ) = θ;
    (ii) if θ ∈ Nef(X) then (i) holds with ϕi ∈ H(Li ) = HQ (Li ) and Li ample;
   (iii) if ω := θ ∈ Amp(X), then ϕ can be written as the limit of a decreasing net in
         Hdom (ω) (see Definition 3.8).
50                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

   We shall later prove that these results actually hold with (countable) sequences instead
of nets, see Corollary 12.18.
   As already indicated by (iii), the class of θ-psh functions has particularly good properties
when θ ∈ Amp(X) is ample. In this case, we typically write ω instead of θ.
Corollary 4.16. For any ω ∈ Amp(X), the space CPSH(ω) = C0 (X) ∩ PSH(ω) is the
closure of Hdom (ω) ⊂ C0 (X) in the topology of uniform convergence.
Proof. By Theorem 4.7, CPSH(ω) is closed in the topology of uniform convergence. By
Theorem 4.15 and Dini’s lemma, any ϕ ∈ CPSH(ω) is the uniform limit of a net in Hdom (ω),
and the result follows.                                                                
Corollary 4.17. For any θ ∈ N1 (X) and any ϕ ∈ PSH(θ) we have ϕ > −∞ on X lin .


## Literal published unit: bj-curve-topology.txt

                          tv ≤ vZ,triv =⇒ ϕ(tv) ≥ ϕ(vZ,triv ) = sup ϕ,
                                                                     Z an
since ϕ is decreasing, and lim supt→+∞ ϕ(tv) ≤ ϕ(vZ,triv ), since ϕ is usc.                      
1.1.6. The Berkovich analytification of a curve. Here we describe X an in the case when X
is a curve, i.e. of pure dimension one. We may and will assume X is connected.
   If X is smooth, then X an is a star-shaped R-tree rooted at vtriv , see Figure 1. Further,
the Berkovich topology coincides with the weak tree topology as defined in [FJ04, §3.1.4]
or [Jon12, §2.1.1], for example.
   More specifically, each closed point p ∈ X(k) determines a compactified ray ιp : [0, +∞] ,→
X an , with ιp (0) = vtriv , ιp (t) = t ordp for t ∈ (0, +∞), and ιp (+∞) = vp,triv . The half-open
rays ιp ((0, +∞]) = c−1 (p) form an open partition of X an \ {vtriv }, and we have
                                                                                     a
  X an = X val t X(k), X triv = X(k) = X(k) t {vtriv }, X div = {vtriv } t               ιp (Q>0 ).
                                                                                p∈X(k)

   A neighborhood basis of vtriv is formed by complements of the union of finitely many
segments ιpj ([tj , +∞], where tj ∈ R>0 . In particular, every neighborhood of vtriv contains
at least one (in fact, infinitely many) compactified rays; this prevents X val from being locally
closed in X an , and X val is therefore not locally compact.
14                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

  In the general case, let (Xα ) be the irreducible components of X. Then the normalization
morphism X ν → X induces a surjective map
                                             a
                                   X ν, an =   Xαν,an → X an
                                               α
  that identifies the endpoints vpi ,triv of all rays corresponding to a point pi ∈ ν −1 (p),
p ∈ X(k).



                                                                    ordp1
                             ordp
                                     vp,triv                                  vp,triv


## Literal published unit: bj-differentiation-proof.txt

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


## Literal published unit: bj-envelope-compactness-proof.txt


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


## Literal published unit: bj-flag-ray-generators.txt

                            ϕa·a0 = ϕa + ϕa0 ,        ϕa+a0 = max{ϕa , ϕa0 }.                   (2.4)
              GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      21

Definition 2.1. We define the space of piecewise linear (PL) functions on X an as the
Q-linear subspace
                                      PL(X) ⊂ C0 (X)
generated by all functions ϕa attached to flag ideals a.
  By (2.4), the subset
                    PL+ (X) := m−1 ϕa | m ∈ Z>0 , a flag ideal ⊂ PL(X)
                              
                                                                                           (2.5)
    is stable under sums and finite maxima, and contains all Q-valued constant functions. It
is also stable under multiplication by Q+ : if c ∈ Q+ , then cϕa = m−1 ϕamc for any m ∈ Z>0
is such thatP mc ∈−λZ. Further, it is stable     under the scaling action of Q>0 : if t ∈ Q>0
                                         −1 ϕ 0 , where m ∈ Z
and a =         aλ $   , then t · ϕ a = m    a                  >0 is such that mt ∈ Z, and
  0
       P m λ −mtλ
a = λ aλ $           .
    It follows that the Q-vector space PL(X) is stable under finite maxima and minima, and
under the scaling action of Q>0 , and it contains all constant Q-valued functions. Further,
any function in PL(X) can be written as a difference of functions in PL+ (X), and is Q-valued
on X div .
    We refer to Theorem 2.7 and Appendix A for an interpretation of PL functions in terms
of test configurations and PL functions on simplicial complexes, respectively. In our setting,
PL functions play the role of smooth functions in the complex analytic case, as illustrated
by the next result.
Theorem 2.2. The space PL(X) is dense in C0 (X) for the topology of uniform convergence.
  By the ‘lattice version’ of the Stone–Weierstrass theorem, this is a direct consequence of
the following result.
Lemma 2.3. The Q-linear subspace PL(X) ⊂ C0 (X) is stable under max (and hence min),
contains the constants in Q, and separates the points of X an .
Proof. The first two properties are clear. As mentioned in §1.1, the topology of X an is
generated by the functions log |b| attached to ideals b ⊂ OX . For any two v, v 0 ∈ X an we
can thus find an ideal b such that log |b|(v) 6= log |b|(v 0 ) (since X an is Hausdorff), and it
follows that ϕ := max{log |b|, −m} ∈ PL(X) separates v, v 0 for m  1.                        
Remark 2.4. We will occasionally consider the R-vector space PL(X)R ⊂ C0 (X) generated
by PL(X). As opposed to the latter, PL(X)R is not closed under max.
Example 2.5. Given a closed subscheme Z ⊂ X with ideal b ⊂ OX , the function
                                   ϕZ := max{log |b|, −1}
          +
lies in PL (X), since ϕZ = ϕa with a = b + ($). Note that
                                   t · ϕZ = max{log |b|, −t}                               (2.6)
for all t ∈ Q>0 .
Example 2.6. Assume X is a smooth irreducible curve, and recall the description of X an
in §1.1.6. As a special case of Example 2.5, each p ∈ X(k) defines a function ϕp ∈ PL+ (X)
that satisfies for all q ∈ X(k) and t ∈ [0, +∞]
                                        
                             ?            max{−t, −1} if q = p;
                            ιq ϕp (t) =
                                          0            otherwise.
22                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON
                                                                                        P
Using (2.6) and the fact that every nontrivial ideal of X is of the form b = OX (− i ai pi )
for a finite set (pi ) in X(k) and ai ∈ Z>0 , one checks that the functions t · ϕp with t ∈ Q>0
and p ∈ X(k) span PL(X). A function ϕ ∈ C0 (X) is PL iff ϕ is constant on all but finitely
many rays of X an and Q-PL on these rays, and ϕ ∈ PL+ (X) iff ϕ is further convex (and
hence decreasing, being bounded) on each ray.
2.2. PL functions and test configurations. Let X be a test configuration for X, and
recall that Gauss extension of (semi)valuations yields an embedding σX : X an ,→ X an onto
the set of k × -invariant semivaluations w ∈ X an such that w(X0 ) = w($) = 1.


## Literal published unit: bj-model-nef-descent-proof.txt

Definition 3.2. We say that a function ϕ ∈ PLR is θ-plurisubharmonic ( θ-psh for short)
if it is determined by a divisor D ∈ VCar(X )R on a test configuration X dominating Xtriv
such that θX + D ∈ Nef(X /A1 ).
   We sometimes also say that the pair (θ, ϕ) ∈ N1 (X) × PLR is psh. Here θX + D denotes,
slightly abusively, the sum of θX and of the image of D in N1 (X /A1 ).
   This definition is independent of the choice of X . Indeed, for any morphism of test
configurations µ : X 0 → X , we have
                                   θX 0 + µ? D = µ? (θX + D) ,
which is thus nef iff θX +D is nef. Restricting to X1 ≃ X further shows that a θ-psh function
in PLR can only exist when θ ∈ Nef(X).
   We will use the notation
                              PLR ∩ PSH(θ)     and    PL ∩ PSH(θ)
for the sets of θ-psh functions in PLR and PL, respectively. At this point, the notation is
purely formal, but it will be justified in §4, by defining the set PSH(θ).
   When θ = c1 (L) ∈ N1 (X) is the numerical class of L ∈ Pic(X)Q on X, we simply speak
of L-psh functions. By Theorem 2.31, we have:
Example 3.3. For any Q-line bundle L on X, L 7→ ϕL sets up a 1–1 correspondence
between the set of semipositive non-Archimedean metrics in the sense of [BHJ17, Defini-
tion 6.4], i.e. equivalence classes of nef test configurations L for L, and PL ∩ PSH(L). By
Theorem 2.31 (ii), we thus have H(L) ⊂ PL ∩ PSH(L), the inclusion being strict in general.
Remark 3.4. Following [BFJ16, BFJ15] we could define a closed (1, 1)-form on X an to be
an element η ∈ limX N1 (X /A1 ), and declare a function ϕ ∈ PLR to be η-psh if it is of the
                −→
form ϕ = ϕD , with D ∈ VCar(X )R such that η + D is nef. In this paper we only consider
the case when η ∈ N1 (Xtriv /A1 ) is determined by the pullback of a class θ ∈ N1 (X).
     As a direct consequence of the fact that Nef(X /A1 ) ⊂ N1 (X /A1 ) is closed, we have:
Lemma 3.5. Let θi → θ be a convergent sequence in N1 (X). Pick ϕ, ψ ∈ PLR , and assume
that ϕ + ci ψ is θi -psh for a sequence ci → 0. Then ϕ is θ-psh.
Proposition 3.6. Pick θ, θ0 ∈ N1 (X), and assume that ϕ, ϕ0 ∈ PLR are θ-psh and θ0 -psh,
respectively. Then:
    (i) ϕ + ϕ0 is (θ + θ0 )-psh, and tϕ is tθ-psh for all t ∈ R>0 ;
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                        35

    (ii) for each c ∈ R and t ∈ Q>0 , ϕ + c and t · ϕ are θ-psh;
   (iii) if θ = θ0 and ϕ, ϕ0 ∈ PL, then max{ϕ, ϕ0 } ∈ PL is θ-psh;
   (iv) ϕ is decreasing with respect to the partial order on X an , and hence satisfies (1.4)
         (see Lemma 1.4);
    (v) for any morphism f : Y → X from a projective variety, f ? ϕ is f ? θ-psh;
   (vi) if we further assume that f : Y → X is surjective, then
                   ϕ θ-psh ⇐⇒ ϕ|Xαan θ|Xα -psh for all α ⇐⇒ f ? ϕ f ? θ-psh.
  In particular, (i) shows that PLR ∩ PSH(θ) is a convex subset of PLR .
Lemma 3.7. For any θ ∈ N1 (X) and ϕ ∈ PLR ∩ PSH(θ), there exists a sequence ϕm ∈
H(Lm ) with Lm ∈ Pic(X)Q such that ϕm → ϕ uniformly on X an and c1 (Lm ) → θ.
Proof. Pick a test configuration X dominating Xtriv and D ∈ VCar(X )R such that ϕ = ϕD .
By openness of the (relatively) ample cone of N1 (X /A1 ), we can find a sequence of Q-
line bundles Lm on X and Dm ∈ VCar(X )Q such that c1 (Lm ) → θ in N1 (X), Dm → D
in VCar(X )R , and c1 (Lm )X + Dm ∈ N1 (X /A1 ) is ample for all i. In particular, Lm :=
(Lm )X +Dm is a semiample test configuration for L, and hence ϕm := ϕLm = ϕDm ∈ H(Lm ).
Furthermore, Dm → D implies ϕm → ϕ uniformly.                                          
Proof of Proposition 3.6. Pick a test configuration X dominating Xtriv and D, D0 ∈ VCar(X )R
that determine ϕ, ϕ0 . By assumption, θX + D and θX   0 + D 0 are nef. Thus

       (θ + θ0 )X + D + D0 = (θX + D) + θX   0
                                               + D0
                                                    
                                                        and (tθ)X + tD = t (θX + D)
are nef as well, proving (i).
   For each c ∈ R we have ϕ + c = ϕD+cX0 . Since X0 = π ? (0) vanishes in N1 (X /A1 ),
θX + D + cX0 is nef, and ϕ + c is thus θ-psh. To prove the remaining part of (ii), it suffices to
prove that if d ∈ Z>0 , then ϕ is θ-psh iff d · ϕ is θ-psh. In view of Lemma 2.34, this follows
from the fact that θX + D ∈ N1 (X /A1 ) is nef iff its pullback under the base change of X
with respect to $ 7→ $d is nef.
   Assume now θ = θ0 and D, D0 ∈ VCar(X )Q . By openness of Amp(X), we can find an
Q-line bundle L on X such that c1 (L) − θ is ample and arbitrarily small. Then ϕ, ϕ0 are
L-psh, and it will be enough to show that max{ϕ, ϕ0 } is L-psh as well, by Lemma 3.5. After
perhaps passing to a higher test configuration, we may assume that X supports an ample
test configuration L for L (Lemma 2.33). For each ε ∈ Q>0 , the Q-line bundle LX + D + εL
is ample, and hence semiample. Thus ϕ + εϕL is Fubini–Study for (1 + ε)L, and similarly
for ϕ0 + εϕL . By Proposition 2.19, it follows that
                        max{ϕ + εϕL , ϕ0 + εϕL } = max{ϕ, ϕ0 } + εϕL
is Fubini–Study for (1 + ε)L, and hence (1 + ε)L-psh. Using Lemma 3.5 we conclude, as
desired, that max{ϕ, ϕ0 } is L-psh. This proves (iii).
    By Proposition 2.19, any Fubini–Study function is decreasing, and (iv) thus follows from
Lemma 3.7.
    To prove (v), note that the Gm -equivariant rational map Y × Gm 99K X induced by f
admits a Gm -equivariant resolution of indeterminacies, which is thus a test configuration Y
for Y dominating Ytriv . Also denoting by f : Y → X the corresponding morphism, we have
f ? ϕ = ϕf ? D , and the result thus follows from the fact that θY + f ? D = f ? (θX + D) is nef,
as the pullback of a nef class. If f : Y → X is surjective, then f : Y → X is surjective as
well, and (vi) follows.                                                                        
36                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

   Given a test configuration π : X → A1 , we denote by Amp(X /A1 ) ⊂ Nef(X /A1 ) the set


## Literal published unit: bj-monotone-energy-proof.txt

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
                         (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ) = t(ω0 , ϕ0 ) · . . . · (ωn , ϕn )                          (7.3)
for all t ∈ R>0 ,
                                                          X
                   (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) =              (ω0 , ϕ0 )|Xα · . . . · (ωn , ϕn )|Xα ,                    (7.4)
                                                       dim Xα =n
and
                 (ν ? ω0 , ν ? ϕ0 ) · . . . · (ν ? ωn , ν ? ϕn ) = (ω0 , ϕ0 ) · . . . · (ωn , ϕn )                           (7.5)
with ν : X ν → X the normalization morphism.
76                                 SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. Using approximation by decreasing nets in Hdom (ωi ), everything is clear from Propo-
sition 3.14, except that this only provides a proof of (7.3) for t ∈ Q>0 . To get the general
case, we may replace ϕi with ϕi − sup ϕi and assume ϕi ≤ 0 for all i. Write a given t ∈ R>0
as the limit of an increasing sequence tm ∈ Q>0 . For each i, (tm · ϕi )m is a decreasing
sequence in PSH(ωi ) that converges to t · ϕi , and hence
                    lim (ω0 , tm · ϕ0 ) · . . . · (ωn , tm · ϕn ) = (ω0 , t · ϕ0 ) · . . . · (ωn , t · ϕn ).
                   m→∞
The result follows.                                                                                                           
     We also record the following useful monotonicity property with respect to ωi .
Proposition 7.3. For i = 0, . . . , n, pick ωi , ωi0 ∈ Amp(X) such that ωi0 ≥ ωi , and ϕi ∈
PSH(ωi ) ⊂ PSH(ωi0 ). Then
   (i) if ϕi ≤ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≤ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≤ 0;
  (ii) if ϕi ≥ 0 for all i, then (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) ≥ (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) ≥ 0.
Proof. By monotone approximation, we may assume ϕi ∈ PL ∩ PSH(ωi ). By assumption,
θi := ωi0 − ωi is nef. The result thus follows by expanding out
                 (ω00 , ϕ0 ) · . . . · (ωn0 , ϕn ) = ((ω0 , ϕ0 ) + (θ0 , 0)) · . . . · ((ωn , ϕn ) + (θn , 0))
and applying Corollary 3.16.                                                                                                  
  For any θ ∈ N1 (X), recall that CPSH(θ) = C0 (X) ∩ PSH(θ) ⊂ E ∞ (θ) respectively denote
the sets of continuous and bounded θ-psh functions. We conclude this section with a general
continuity result for the energy pairing involving such functions. It is an analogue of the
Chern–Levine–Nirenberg inequality in the complex case.


## Literal published unit: bj-operator-and-pushforward-proof.txt

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


## Literal published unit: bj-pl-approximation.txt

Proposition 3.10. If ω ∈ Amp(X), then every ϕ ∈ PLR ∩ PSH(ω) is a uniform limit of
functions in Hdom (ω).
Lemma 3.11. For any ω ∈ Amp(X), the set of test configurations X dominating Xtriv such
that there exists H ∈ VCar(X )Q with ωX + H ∈ Amp(X /A1 ) is cofinal in the set of all test
configurations.
Proof. By Lemma 1.8, any test configuration for X is dominated by a test configuration X
with a morphism µ : X → Xtriv such that VCar(X )Q contains a µ-ample divisor A. Since
ωXtriv ∈ N1 (Xtriv /A1 ) is ample, ωX + εA = µ? ωXtriv + εA ∈ N1 (X /A1 ) is ample for ε ∈ Q>0
small enough, and setting H := εA yields the result.                                        
Proof of Proposition 3.10. Pick any ϕ ∈ PLR ∩ PSH(ω), and write ϕ = ϕD for some D ∈
VCar(X )R , where X is an integrally closed test configuration. Thus ωX + D ∈ N1 (X /A1 ) is
nef. By Lemma 3.11 we may assume that there exists P    H ∈ VCar(X )PR such that ωX + H is
ample. Pick a basis (Ci ) for VCar(X )Q and write D = i ci Ci , H = i c0i Ci with ci , c0i ∈ R.
                                  1                                                          1
For m  1, the class ωX + D + m     H ∈ N1 (X /A1 ) is ample, and we can pick εm,i ∈ (0, m     )
                    P          0
                              ci
such that if Dm := i (ci + m + εm,i )Ci , then Dm ∈ VCar(X )Q and ωX + Dm is ample. It
                                                     1
follows that ϕDm ∈ Hdom (ω), and that ϕDm − ϕ = m
                                                             P
                                                       ϕH + i εm,i ϕCi tends to 0 uniformly
on X an .                                                                                     
3.2. The energy pairing. Recall that every test configuration π : X → A1 admits a canon-
ical compactification π : X̄ → P1 . If X dominates Xtriv , then any θ ∈ N1 (X) pulls back to a
class θX̄ ∈ N1 (X̄ ), whose image in N1 (X /A1 ) coincides with θX considered above.
   Pick an (n + 1)-tuple of pairs (θi , ϕi ) ∈ N1 (X) × PLR , i = 0, . . . , n, and choose a test
configuration X dominating Xtriv and divisors Di ∈ VCar(X )R that determined the ϕi .
Following [BHJ17, Definition 6.11], we introduce:
Definition 3.12. The energy pairing takes an (n+1)-tuple of pairs (θi , ϕi ) ∈ N1 (X)×PLR ,
i = 0, . . . , n to
                                                                                     
                    (θ0 , ϕ0 ) · . . . · (θn , ϕn ) := θ0,X̄ + D0 · . . . · θn,X̄ + Dn ∈ R. (3.3)
                GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                                             37

  The right-hand side is an intersection number against the fundamental class


## Literal published unit: bj-smooth-envelope-input.txt


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


## Literal published unit: bj-surjectivity-and-node-proof.txt

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


## Literal published unit: bj-unibranch-gap.txt

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
unibranch.
  The analogue of this result is known in the complex analytic setting, too. We have not
been able to locate a precise reference, but the proof below of Theorem 5.12 can easily be
adapted to that setting.
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     59

Lemma 5.13. Let π : Y → X be a birational morphism. Pick θ ∈ N1 (X), and assume that
θ can be written as the limit of a sequence of classes θm > θ with the envelope property.
                  ∼
Then π ? : PSH(θ) → PSH(π ? θ) is a homeomorphism.
  Recall that θm > θ means that θm − θ is ample.

Proof. After passing to a subsequence, we may assume that θm > θm+1 for all m, and hence
                                                           ∼
PSH(θm+1 ) ⊂ PSH(θm ). Since π induces a bijection Y div → X div , π ? : PSH(θ) → PSH(π ? θ)
is a topological embedding, and it suffices to show that it is onto. Pick ψ ∈ PSH(π ? θ), and
write π as the blowup of an ideal b ⊂ OX . By Theorem 4.32, there exists a sequence εm & 0
such that ψ + εm π ? log |b| = π ? ϕm with ϕm ∈ PSH(θm ). By Theorem 4.22, ϕm is uniquely
determined, and (ϕm )m≥m0 is an increasing sequence in PSH(θm0 ) for any given m0 . By
Theorem 5.11, ϕm converges pointwise on X div to ϕ ∈ PSH(θ), which satisfies ψ = π ? ϕ on
Y div . The result follows.                                                                 

Proof of Theorem 5.12. Since the normalization morphism ν : X ν → X is finite, ν ? ω is
ample, and hence Hdom (ν ? ω) spans PL(X ν ), see (3.2). By Lemma 2.3, PL(X ν ) separates
the points of (X ν )an , and it is thus already the case of Hdom (ν ? ω). On the other hand,
Lemma 5.13 implies that all functions in Hdom (ν ? ω) ⊂ PSH(ν ? ω) descend to X an (take ωm =
(1 + m−1 )ω). As a consequence, ν an : (X ν )an → X an is injective. By the non-Archimedean
GAGA principle, this implies that ν : X ν → X is injective as well (see [Berk90, §3.4]); this
is enough to conclude that ν is a homeomorphism, and hence that X is unibranch.             

   As mentioned above, in the complex analytic case the envelope property conversely holds
as soon as X is unibranch. It is thus natural to conjecture:
Conjecture 5.14. If X is unibranch, then the envelope property holds for all θ ∈ N1 (X).
  We will establish this conjecture in the important special case where θ is ample, X is
smooth, and char k = 0 (see Theorem 5.20).
Remark 5.15. The envelope property makes sense also when X is reducible. It is easy to
see that θ ∈ N1 (X) has the envelope property iff θ|Y ∈ N1 (Y ) has the envelope property
for every connected component Y of X. Moreover, if X is connected, then the proof of
Theorem 5.12 shows that if the envelope property holds for some ample class in N1 (X), then
the normalization morphism ν : X ν → X is a homeomorphism, which implies that X is
irreducible (and unibranch).
5.3. Envelopes. For ample classes, the envelope property admits a useful reformulation.
We continue to assume that X is irreducible unless stated otherwise. Fix a class ω ∈


## Literal published unit: gr-no-ma-claim.txt

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


## Literal published unit: ps-arbitrary-field-warning.txt

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


## Literal published unit: synthetic-measure-completion.txt

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


## Additional published BJ LF 2812--2842


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


## Additional published BJ LF 4943--4967

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

                                       9. Measures of finite energy
   Denote as above by X a projective variety of dimension n, and fix an ample class ω ∈
Amp(X). We define the Monge–Ampère energy of a probability measure on X an , and begin
a study of the space of measures of finite energy.


## Additional published BJ LF 6029--6090

class ω ∈ Amp(X).
    Having analyzed the strong topology on the space M1 = M1 (ω) of Radon probability
measures of finite energy, we now perform the corresponding analysis on the space E 1 =
E 1 (ω) of ω-psh functions of finite energy.
12.1. The strong topology of E 1 . Following [BBGZ13, BBE+16] we introduce:
Definition 12.1. The weak topology of E 1 is the topology inherited from PSH(ω). The
strong topology is the coarsest refinement of the weak topology for which E : E 1 → R becomes
continuous.
  Thus a net (ϕj ) in E 1 converges weakly to ϕ ∈ E 1 iff ϕj → ϕ pointwise on X div (or,
equivalently, on X lin , cf. Remark 11.5); it converges strongly iff we further have E(ϕj ) →
E(ϕ). By Proposition 7.7, E is continuous along decreasing nets, and hence:
Example 12.2. For a decreasing net (ϕi ) in E 1 , weak and strong convergence coincide.
Definition 12.3. We define the quasi-metric I on E 1 by setting
                       I(ϕ, ϕ0 ) = Iω (ϕ, ϕ0 ) := I(ϕ, ϕ0 ) + | sup ϕ − sup ϕ0 |         (12.1)
for ϕ, ϕ0 ∈ E 1 .
  By (7.30) and Corollary 10.4, I is indeed a quasi-metric. It is further immediate to check
that it satisfies the analogue of (7.34), i.e.
                         I(ϕ, ψ) = I (ϕ, max{ϕ, ψ}) + I (max{ϕ, ψ}, ψ)                   (12.2)
for all ϕ, ψ ∈ E 1 . As we now show, the quasi-metric I defines the strong topology of E 1 .
Theorem 12.4. A net (ϕj ) in E 1 converges strongly to ϕ ∈ E 1 iff I(ϕj , ϕ) → 0.
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                      121

Proof. First assume that ϕj → ϕ strongly in E 1 . Then sup ϕj → sup ϕ, E(ϕj ) → E(ϕ), and
       ´ sup ϕj − E(ϕj ) is thus eventually bounded. Since ϕj → ϕ weakly, Proposition 9.19
J(ϕj ) =
yields (ϕj − ϕ) MA(ϕ) → 0. Thus
                                                       ˆ
                 I(ϕj , ϕ) ≈ Jϕ (ϕj ) = E(ϕ) − E(ϕj ) + (ϕj − ϕ) MA(ϕ) → 0,         (12.3)

in view of (7.29), and hence I(ϕj , ϕ) → 0.
   Assume, conversely, I(ϕj , ϕ) → 0, i.e. sup ϕj → sup ϕ and I(ϕj , ϕ) → 0. Since δv has finite
energy for v ∈ X div (Proposition 11.1), Theorem 10.3 yields ϕj (v) → ϕ(v), i.e. ϕj → ϕ
weakly. By the quasi-triangle inequality,´ J(ϕj ) ≈ I(ϕ ´ j , 0) is further eventually bounded,
and Proposition 9.19 therefore implies ϕj MA(ϕ) → ϕ MA(ϕ), which in turn shows that
E(ϕj ) → E(ϕ), by (12.3). Thus ϕj → ϕ strongly, which concludes the proof.                    
   By Example 12.2, any weakly convergent decreasing net in E 1 is strongly convergent. The
next result, which is a direct consequence of Theorem 7.38, shows that this also holds for
increasing nets:
Theorem 12.5. Let (ϕj ) be an increasing net in E 1 , and assume that ϕj → ϕ weakly in
E 1 . Then ϕj → ϕ strongly as well.
  We end this section with a useful quantitative version of Corollary 10.5.
Proposition 12.6. Let (ϕi ) be a net in E 1 and ϕ ∈ E 1 such that ϕi ≤ ϕ for all i. Then
ϕi → ϕ strongly iff E(ϕi ) → E(ϕ).
Proof. The ‘only if’ part follows directly from the definition of strong convergence. Con-
versely, assume E(ϕi ) → E(ϕ). Since ϕi ≤ ϕ,
                                                  ˆ
            I(ϕi , ϕ) ≈ Jϕ (ϕi ) = E(ϕ) − E(ϕi ) + (ϕi − ϕ) MA(ϕ) ≤ E(ϕ) − E(ϕi )

tends to 0, and hence ϕ0i := ϕi − sup ϕi converges strongly to ϕ0 := ϕ − sup ϕ, by Theo-
rem 12.4. In particular, E(ϕ0i ) = E(ϕi ) − sup ϕi converges to E(ϕ0 ) = E(ϕ) − sup ϕ, hence
sup ϕi → sup ϕ, and we conclude, as desired, ϕi → ϕ strongly.                             
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
