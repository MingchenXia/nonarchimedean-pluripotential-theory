---
title: "Nonample non-Archimedean equations: established envelopes, an exceptional fixed-part endpoint, and remaining gates"
author: "Research draft for original P16.5"
date: "5 October 2026"
geometry: margin=0.85in
fontsize: 10pt
header-includes:
  - \usepackage{amsmath,amssymb,amsthm}
  - \usepackage{longtable}
---

# Abstract

Original P16.5 is not solved here. The post-2020 primary literature already supplies the genuine psh cone, intrinsic envelope reference and normalized psh compactness on the entire smooth projective pseudoeffective numerical domain over algebraically closed trivially valued characteristic-zero fields. In particular, general big-class envelope regularity is not an outstanding gate: Boucksom--Jonsson's 2023 addendum proves it. The nonample finite-energy operator and arbitrary-target equation do not follow from that theorem or from the supplied ample theorem.

We prove a restricted nonnef endpoint relative to the supplied ample theory. If $\pi:X=\operatorname{Bl}_pY\to Y$ blows up one smooth point of a smooth projective variety of dimension at least two, $A$ is an actual ample rational bundle on $Y$, and $L=\pi^*A+aE$ with $a>0$ rational, then the entire genuine $L$-psh cone factors as $a\log|s_E|+\pi^*\operatorname{PSH}(Y,A)$. We prove this using genuine varying-bundle section approximants and compactness, without subtracting two infinite values or assuming decreasing closure for an incorrectly corrected net. The reference is exactly $V_L=a\log|s_E|$. The intrinsic relative energy, original-carrier nonpluripolar products, mass, comparison, admissible targets, attained equation and uniqueness are constructed for this explicit domain. This is a fixed-part endpoint and not an extension to every big bundle.

An explicit big nonnef surface bundle has volume one but top self-intersection zero. A separate nef zero-volume surface example has two bounded genuine potentials with identical zero top measure and nonconstant difference. These computations identify different mass and injectivity errors. The additional zero-volume equation range proved is only the actual trivial bundle on connected smooth projective varieties. Precise full-domain finite-energy and zero-volume replacement gates remain. All conclusions are unverified proof drafts; provenance checks and PDF compilation do not certify mathematics.

# 1. Exact scope, conventions and available ample premise

The controlling task is original P16.5, with the unchanged P16 family retained in `task-original.json`. Its first full target is every actual big rational line bundle on an original smooth projective $X$ over every algebraically closed trivially valued characteristic-zero field. An example, a finitely generated endpoint or a formal transfer does not close that target. We retain algebraic closedness, characteristic zero, the trivial valuation, projectivity, smoothness and connectedness throughout the positive endpoint below. Smooth connected varieties here are integral. There is no cardinality restriction on the field. Analytic carriers are the original Berkovich analytifications. Measures are positive Radon measures unless explicitly described otherwise.

For a rational bundle, every section formula is interpreted after a divisible integral tensor power. Scalar potentials are differences from the canonical trivial metric on that **actual** bundle. Thus $\log|s|$ always means canonical section evaluation on the named bundle, not a local logarithm without its reference. For a generically nonzero finite section system,
$$
 \varphi=\frac1m\max_i\{\log|s_i|+\lambda_i\},\qquad
 s_i\in H^0(X,mB)\setminus\{0\},\quad\lambda_i\in\mathbb R,
 \tag{1}
$$
is a genuine generically finite Fubini--Study potential on the actual rational $B$. Common zeros are allowed; their values are $-\infty$. Canonical evaluation is at most zero for each global section logarithm and equals zero at the generic trivial valuation. Consequently the supremum of (1) is $\max_i\lambda_i/m$.

We use the genuine cone of BJ, *Global pluripotential theory over a trivially valued field*, arXiv:1801.08229v4, 27 March 2022. Its definition for a numerical class $\theta$ uses decreasing nets of genuine generically finite section potentials (1) on actual rational bundles $B_i$, with $c_1(B_i)\to\theta$, and generically finite limits. For a fixed actual $L$ these scalars are metrics on $L$ through its canonical reference; their numerical psh condition is $\theta=c_1(L)$. This definition does not assume finite generation of the section algebra. It is not decreasing closure of everywhere finite section maxima on a nonnef bundle. The latter class may be empty.

The exact supplied full P16.1 body is an available mathematical premise **only on actual ample rational bundles** and its exact field and geometric hypotheses. We use it on smooth ample $(Y,A)$, and occasionally on another ample bundle on the same smooth $Y$. Denote the granted energy by $E_{A,\mathrm{raw}}$, its space by $\mathcal E^1(Y,A)$, its genuine raw mixed products by $M_A$, and its raw top measure by $\operatorname{MA}_{A,\mathrm{raw}}$. Their mass is $V=(A^n)>0$. The grant includes compactness, finite-energy locality and comparison, continuous-direction outer differentiation, intrinsic dual-energy integrability, coercive energy estimates, target integral continuity on bounded-energy sets, actual variational attainment, the equation, and uniqueness modulo constants. We do not rerun its proof after deleting ampleness. The preserved supplied mathematical body is `granted/block-00.txt`; historical audit labels and binding hashes are not additional mathematical premises.

Published BJ results used outside that grant are recorded with their actual scopes in `external-premises.json`. In particular, signed intersection products in BJ's ambient finite-energy vector space have mass $L^n$, and their positivity theorem assumes nefness. They are not a ready-made positive nonpluripolar operator of mass $\operatorname{vol}(L)$ for a general big nonnef bundle.

# 2. Primary literature audit and the gates it actually removes

## 2.1. The complete smooth pseudoeffective envelope domain is established

Boucksom--Jonsson, *Addendum to the article “Global pluripotential theory over a trivially valued field”*, arXiv:2206.07183v2, submitted 6 September 2023, PDF dated 7 September 2023, proves the following exact result. For smooth irreducible projective $X$ over an algebraically closed trivially valued field, with characteristic zero or dimension at most two, **every** numerical class has the envelope property. In our retained characteristic-zero field domain there is no dimension, countability, toric, support or finite-generation restriction. Its Corollaries 2.1--2.2 give
$$
 \operatorname{PSH}(X,\theta)\ne\varnothing
 \Longleftrightarrow \theta\text{ is pseudoeffective},\qquad
 V_\theta=P_\theta(0)\in\operatorname{PSH}(X,\theta),
 \tag{2}
$$
and compactness of $\operatorname{PSH}_{\sup}(X,\theta)$ in pointwise divisorial convergence. The envelope in (2) is the actual original-carrier function. It has supremum zero and provides a minimal-singularity reference. No auxiliary ample model is identified with the original bundle in this assertion.

We retain the full pertinent proof of Theorem A, not just its statement. Here is its mechanism and its scope. Approximation by big rational classes from above reduces envelope regularity to an actual big rational $L$. For a PL obstacle on an integrally closed test configuration $(\mathcal X,\mathcal L)$ with generic bundle $L$, resolve to a smooth model with SNC central fiber. Let $\mathfrak a_m$ be the base ideals of $m\mathcal L$ on the **total space**; they need not be vertical. Lemmas 1.5--1.7 identify the same-bundle section envelope $Q_L$ with the increasing divisibility net
$$
 \varphi_m=\varphi_{\mathcal L}+m^{-1}\log|\mathfrak a_m|.
 \tag{3}
$$
The equality of $Q_L$ and $P_L$ is obtained outside the augmented base locus, which includes every divisorial valuation. Multiplier ideals $\mathfrak b_m$ of the graded sequence satisfy $\mathfrak a_m\subset\mathfrak b_m$ and $\mathfrak b_{m\ell}\subset\mathfrak b_m^\ell$. A **fixed** sufficiently positive equivariant ample total bundle $\mathcal A$ makes $m\mathcal L+\mathcal A$ tensored with $\mathfrak b_m$ globally generated. After a constant shift making its reference nonnegative, the corrected genuine section potentials
$$
 \varphi_{\mathcal L}+m^{-1}\log|\mathfrak b_m|
       +m^{-1}\varphi_{\mathcal A}
 \tag{4}
$$
decrease in the divisibility ordering, in actual classes $L+m^{-1}A$ tending to $L$. Their limit is genuine by varying-class closure. The inequalities from (3) and the multiplier ideals identify that limit with $P_L$ on divisorial valuations. Divisorial determination and the envelope lemmas then establish the original-carrier envelope property. The general pseudoeffective reference in (2) is obtained by decreasing big references from above. BJ 5.11 supplies compactness once this envelope property is known.

This proof keeps genuine sections and their horizontal base loci. It does not make the original nonnef $L$ ample and does not construct its relative energy. The addendum's **Theorem B** concerns an ample numerical class; its broader statement about bounded obstacles cannot be substituted for a big-class equation theorem. We use Theorem A and its consequences as published inputs, not as new results of this assignment.

## 2.2. Analytic finite energy over the complex field

Darvas--Xia--Zhang, arXiv:2302.02541v3, 17 July 2024, published in *Commentarii Mathematici Helvetici* 100 (2025), 269--322, DOI 10.4171/CMH/586, treats compact Kähler manifolds. Its Theorem 3.14 identifies its compatible test-curve psh space with the BJ Berkovich psh space for pseudoeffective rational bundles on complex projective manifolds. The proof constructs the compatible family under every ample/Kähler perturbation and proves the inverse-map compatibility before passing to the original pseudoeffective class. Section 3.4 then defines a genuine analytic finite-energy candidate for big complex classes. For an $\mathcal I$-maximal test curve $\eta$,
$$
 I^{\mathrm{NA}}_\theta(\eta)=\tau^+_\eta+
 \frac1{V}\int_{-\infty}^{\tau^+_\eta}
       \left(\int_X\theta_{\eta_\tau}^n-V\right)d\tau,
 \qquad V=\int_X\theta_{V_\theta}^n>0.
 \tag{5}
$$
The functional is $-\infty$ off that test-curve class. Its finite locus is $\mathcal E^{1,\mathrm{NA}}(X,\theta)$. Finite energy forces $\eta_{-\infty}=V_\theta$. Theorem 3.17 identifies this space with the $\mathcal I$-maximal finite-energy rays, by the stated complex ray/test-curve theorem.

It would be incorrect to report that no big-class finite-energy definition exists. It would also be incorrect to infer from (5) the requested genuine original-carrier non-Archimedean intersection measure and arbitrary-target inverse theorem over **all** retained fields. The inspected statement/proof units do not provide that deduction. No transfer from complex pluripotential energy is assumed in this draft.

## 2.3. A 2026 finite divisorial big-bundle endpoint

Dervan--Reboulet, *A birational version of K-stability for big classes*, arXiv:2603.25605v1, 26 March 2026, works on smooth **complex** projective varieties with big bundles. Its Definition 3.4 and Theorem 3.6 prescribe finite divisorial probability measures using compatible smooth dominant test configurations and a big real total bundle. The displayed coefficients have the form
$$
 \frac{b_i\langle\mathcal L\rangle^n\cdot E_i}{\operatorname{vol}(L)},
 \tag{6}
$$
where $b_i$ is the central multiplicity and the brackets denote the positive restricted intersection product. The proof uses Proposition 3.8's boundary data and a continuous boundary-preserving simplex map of degree one. The complete displayed statement and proof units are retained; its cited background lemma is not reproved here.

This is an important existing big-class finite-target theorem. Its target class is finite divisorial data and its output is model data. The source expressly distinguishes its approach from genuine FS metric approximation. Its comments on nonuniqueness concern multiple test configurations associated with one measure; they are not a proof that reference-preserving genuine finite-energy metrics fail uniqueness. We neither call (6) an arbitrary-support finite-energy theorem nor use it to construct our metric operator.

Mesquita-Piccione--Witt Nyström, arXiv:2509.09442v1, 11 September 2025, proves a transcendental non-Archimedean Calabi--Yau theorem with a **Kähler** generic positivity class. Its big total degeneration classes do not change that generic hypothesis to every nonample big rational bundle. These scope observations are finite literature findings, not a claim that no exact theorem can exist elsewhere.

# 3. A restricted nonnef domain and its entire genuine cone

**Theorem 1 (exceptional fixed-part endpoint).** Let $k$ be any algebraically closed trivially valued field of characteristic zero. Let $Y$ be smooth connected projective of dimension $n\ge2$, $p\in Y(k)$, $\pi:X=\operatorname{Bl}_pY\to Y$, and $E\simeq\mathbb P^{n-1}$ its exceptional divisor. Let $A$ be an actual ample rational bundle on $Y$, let $a\in\mathbb Q_{>0}$, and fix the actual rational bundle isomorphism
$$ L\simeq\pi^*A\otimes\mathcal O_X(aE). $$
Put $H=\pi^*A$, $\lambda=\log|s_E|$ and $\sigma=a\lambda$. Then $L$ is big and nonnef, and
$$
 \operatorname{PSH}(X,L)
   =\{\sigma+\pi^*\psi:\psi\in\operatorname{PSH}(Y,A)\},
 \qquad V_L=\sigma.
 \tag{7}
$$
The expression in (7) is an actual extended-valued function and an actual metric on $L$. Every potential is $-\infty$ on $E^{\mathrm{an}}$. There is a unique genuine quotient
$$ Q\varphi\in\operatorname{PSH}(X,H),\qquad
 Q\varphi=\pi^*\psi,
 \tag{8}
$$
whose restriction to $X^{\mathrm{an}}\setminus E^{\mathrm{an}}$ is $\varphi-\sigma$. Formula (8) is an extension, not subtraction of two $-\infty$ values. The map in (7) is a homeomorphism in divisorial convergence and preserves suprema. Sections 4--5 construct the intrinsic relative finite-energy space and its original-carrier raw equation, with mass $V=(A^n)=\operatorname{vol}(L)>0$, all finite intrinsic dual-energy targets, comparison and uniqueness modulo constants.

The domain of this theorem consists precisely of the displayed single-point blowup bundles. It is neither the whole big rational domain nor all bundles with an arbitrary Zariski decomposition. Its section algebra has an ample fixed-part description. We do not assert a new general big-class theorem from that fact, and make no novelty claim for the abstract principle of removing a fixed divisor.

## 3.1. Algebraic section factorization, including approaching bundles

Every actual rational bundle $B$ on $X$ can be written uniquely
$$ B=\pi^*C+bE,qquad C\in\operatorname{Pic}(Y)_\mathbb Q, b\in\mathbb Q. \tag{9} $$
Indeed, represent $B$ by a rational Cartier divisor on smooth $X$, push its nonexceptional prime divisors to smooth $Y$, and pull them back. The difference is supported on the sole exceptional prime. Uniqueness follows by restriction to a line in $E$: $\mathcal O_E(E)=\mathcal O_{\mathbb P^{n-1}}(-1)$ while every pulled bundle is trivial there, and $\pi^*$ is injective. This also gives the corresponding decomposition of numerical classes. If $c_1(B_i)\to c_1(L)$, then in (9) $b_i\to a$ and $c_1(C_i)\to c_1(A)$.

For $b\ge0$ and sufficiently divisible $m$,
$$
 H^0(X,m(\pi^*C+bE))
       =s_E^{mb}\pi^*H^0(Y,mC).
 \tag{10}
$$
For integral $j>0$, restriction of $\pi^*(mC)+jE$ to $E$ is $\mathcal O_E(-j)$, which has no sections: a homogeneous polynomial of negative degree is zero. The divisor restriction exact sequence removes one $E$ at a time. At $j=0$, $\pi_*\mathcal O_X=\mathcal O_Y$: a regular function on the blowup restricts to a regular function off $p$, and extends across the codimension-at-least-two point on normal $Y$. The last assertion follows locally from the characterization of a normal domain as the intersection of its height-one local valuation rings; no height-one point is removed. Thus $H^0(X,\pi^*(mC))=H^0(Y,mC)$, proving (10). Rational tensor powers reduce to these integral statements.

In particular $h^0(X,mL)=h^0(Y,mA)$ for all divisible $m$. The usual ample Hilbert asymptotic gives $\operatorname{vol}(L)=(A^n)=V$. Equivalently, after choosing a very ample integral multiple of $A$, its Hilbert polynomial has leading coefficient the projective degree divided by $n!$, which is the definition of the ample top intersection; passing through those divisible multiples gives this asymptotic. There is no assertion that $L$ itself is ample. On a line $\ell\subset E$, $L\cdot\ell=-a$, so $L$ is nonnef. On that line $H\cdot\ell=0$, so even the ample bundle on $Y$ has nonample pullback.

## 3.2. Direct proof of (7), without an invalid quotient net

Let $\varphi\in\operatorname{PSH}(X,L)$. By the genuine definition take a decreasing net of section potentials $\varphi_i$ on actual $B_i$ with $c_1(B_i)\to c_1(L)$ and $\varphi_i\downarrow\varphi$. Delete an initial segment so $b_i>0$ in (9). Factor the literal sections by (10), retaining their weights and tensor powers. Then
$$
 \varphi_i=b_i\lambda+\pi^*\psi_i,qquad
 \psi_i\in\mathcal H^{\mathrm{gf}}_\mathbb R(Y,C_i),
 \quad c_i:=\sup\psi_i=\sup\varphi_i\downarrow c:=\sup\varphi.
 \tag{11}
$$
The finite $c$ is the original generic trivial value. The potential $\psi_i$ is at most $c_i$ everywhere on $Y^{\mathrm{an}}$ by canonical section evaluation. At a point off $E$, passing to the limit in (11) gives $\varphi\le\sigma+c$; on $E$ all eventual $\varphi_i$ are $-\infty$. Thus the same inequality holds everywhere and $\varphi=-\infty$ on $E^{\mathrm{an}}$.

The corrected $\psi_i$ need **not** decrease, because $b_i$ varies. We do not apply decreasing closure to them. Instead, $c_1(C_i)\to A$ implies that $2A-c_1(C_i)$ is ample on a tail. Hence $\psi_i-c_i\in\operatorname{PSH}_{\sup}(Y,2A)$. The genuine zero potential in the nef difference class justifies this inclusion. Ample compactness supplies a convergent subnet with genuine limit $\psi-c$ on $Y$. For each rational $0<\delta<1$, the same tail lies in $\operatorname{PSH}(Y,(1+\delta)A)$, since $(1+\delta)A-c_1(C_i)$ is ample eventually. Its normalized compact space embeds as a closed subset of the Hausdorff normalized $2A$-space. Thus $\psi\in\operatorname{PSH}(Y,(1+\delta)A)$ for every such $\delta$. Applying varying-class decreasing closure to the **constant scalar function $\psi$** as $\delta\downarrow0$ gives $\psi\in\operatorname{PSH}(Y,A)$.

Divisorial valuations of $k(X)=k(Y)$ are the same valuation set. At every such valuation $v$, $\lambda(v)$ is finite and (11) gives along the original net
$$ \psi_i(v)\longrightarrow\varphi(v)-a\lambda(v). \tag{12} $$
This determines the subnet limit uniquely. Genuine pullback and positive addition show $\sigma+\pi^*\psi\in\operatorname{PSH}(X,L)$. Here $\sigma$ is itself the genuine one-section potential on $aE$, and zero is genuine in $H$. Equality of (12) for all divisorial valuations and BJ divisorial determination give
$$ \varphi=\sigma+\pi^*\psi $$
at **every** analytic point. The converse inclusion follows from the same genuine pullback and addition. This proves (7) and its all-point assertion. It neither lifts an arbitrary scalar from a modification nor relies on usc density alone.

The quotient in (8) is now the actual function $\pi^*\psi$. Uniqueness follows on divisorial valuations, and hence everywhere. The normalized spaces in (7) are homeomorphic: every coordinate differs by the fixed finite number $\sigma(v)$ at a common divisorial valuation. At the generic trivial valuation $\sigma=0$, so suprema agree. Since all normalized $\varphi$ are at most $\sigma$ and $\sigma$ itself is feasible, the actual envelope $V_L=P_L(0)$ equals $\sigma$. The reference function is independent of section bases and of the choice of a nonzero scalar multiplying $s_E$, because the ground-field norm is trivial. It is intrinsically computed from $L$, not chosen after solving an equation.

# 4. Actual relative energy and genuine products on the original carrier

## 4.1. The local product and its zero extension

Let $O=X^{\mathrm{an}}\setminus E^{\mathrm{an}}$. Analytically $\pi$ identifies $O$ with $Y^{\mathrm{an}}\setminus\{p^{\mathrm{an}}\}$. A $k$-rational point over the trivial ground field has a single analytification point. The section $s_E$ is an invertible frame on the algebraic complement of $E$, and gives the **actual** bundle identification
$$ L|_{X\setminus E}\simeq H|_{X\setminus E}. \tag{13} $$
For $\varphi=\sigma+Q\varphi$, the raw local metric weight under (13) is the raw weight of $Q\varphi$. The logarithm of the unit frame is locally harmonic; therefore the local genuine intersection products of $L$-metrics are precisely those of the pulled $A$-metrics. This is a statement about metric weights and genuine local intersection measures before assigning a global measure.

For bounded quotients, their pulled $H$-psh potentials are bounded and belong to BJ's ambient finite-energy vector space after adding any dominating ample class on $X$. The nef product of those bounded $H$-metrics is a positive genuine intersection measure on $X$, of mass $H^n=V$. At continuous model stages, the projection formula for the actual pulled bundles gives pushforward equal to the original mixed $A$-measure. Section/model approximation on $Y$, genuine pullback and decreasing intersection continuity give the same equality for bounded quotients. The actual ample mixed measure gives zero mass to the algebraic point $p^{\mathrm{an}}$: it integrates finite-energy psh tests and charges no pluripolar algebraic subset. Thus its pullback measure gives zero mass to $E^{\mathrm{an}}$, and on $O$ it is determined by (13).

Here is an explicit justification of zero mass at $p$, also needed for targets below. Choose a nonzero section of $mA$ vanishing at $p$, and put $u=m^{-1}\log|s|-1\le-1$. It is genuine $A$-psh and has a pole at $p$. For $\alpha=1/(n+2)$, set $w=-(-u)^\alpha$. Extend the convex composing function affinely from $-1$ to zero; its slopes lie in $[0,1]$, so BJ 4.10 makes $w$ genuine $A$-psh. BJ 7.47 gives, after the harmless supremum normalization,
$$
 \operatorname{Cap}_A\{w\le-t\}=O(t^{-1/\alpha}),\qquad
 J_A(w)\le C+\int_1^\infty t^n\operatorname{Cap}_A\{w\le-t\}\,dt<\infty.
 \tag{13a}
$$
Indeed $n-1/\alpha=-2$. Thus $w\in\mathcal E^1(Y,A)$ and $w(p)=-\infty$. Every ample finite-energy mixed product integrates $w$, and every finite-dual-energy target integrates all genuine finite-energy potentials; hence both give zero mass to $p$. The capacity estimate's proof uses bounded floors $u_s$, the concavity bound $J(u_s)\le\int(-u_s)\operatorname{MA}(u_s)$, layer-cake integration and equal-mass locality to replace the tail at level $t$ by that of $u_t$. Positivity of the mixed expansion gives $\operatorname{MA}(t^{-1}u_t)\ge t^{-n}\operatorname{MA}(u_t)$, leading to the integrable bound in (13a). No big-class energy input is used. The retained source Corollary 7.48 prints a larger exponent range; the conservative choice above and its displayed arithmetic suffice here, without requiring that larger range.

For arbitrary $\psi_1,\ldots,\psi_n\in\mathcal E^1(Y,A)$, the local finite-energy products on $O$ are consequently genuine positive measures. Define their **nonpluripolar extension** by giving $E^{\mathrm{an}}$ zero mass. This produces a positive Radon measure: for a Borel set off $E$ use the analytic isomorphism; inner approximation by compact subsets away from $p$ and outer approximation near the zero-mass point establish regularity on compact $X^{\mathrm{an}}$. Write
$$
 M_\sigma(\varphi_1,\ldots,\varphi_n),\qquad
 \operatorname{MA}_{\sigma,\mathrm{raw}}(\varphi)
       =M_\sigma(\varphi,\ldots,\varphi).
 \tag{14}
$$
Then
$$
 \pi_*M_\sigma(\varphi_1,\ldots,\varphi_n)
       =M_A(\psi_1,\ldots,\psi_n),
 \quad M_\sigma(X^{\mathrm{an}})=V,
 \quad M_\sigma(E^{\mathrm{an}})=0.
 \tag{15}
$$
This is the original-carrier genuine local product with its nonpluripolar zero extension. It is not a Banach/Shilov inverse measure or a measure assigned to an arbitrary lifted scalar. Formula (15) is a consequence of the frame identity, locality and the zero-mass algebraic locus. At bounded stages it is checked by the actual intersection formula. At unbounded stages it is the local finite-energy limit of those products.

For clarity, these are raw measures, not probability measures. Normalizing the **auxiliary** ample theory divides only by $V>0$. The raw top product in (14) has mass $\operatorname{vol}(L)$; no formula identifies that mass with $L^n$.

## 4.2. An intrinsic energy defined with the retained reference

Let $q=Q\varphi$, an actual function on $X$, and let $q_m=\max(q,-m)$, which is genuine in the **nef class $H$**. Put $\varphi_m=\sigma+q_m$. This is an actual $L$-psh decreasing approximation of $\varphi$, retaining $\sigma$. Denote by $M_H(q_m^j,0^{n-j})$ the bounded genuine raw products on $X$ described above. Define
$$
 E_{\sigma,\mathrm{raw}}(\varphi_m)
 :=\frac1{n+1}\sum_{j=0}^n
          \int_{X^{\mathrm{an}}}q_m\,M_H(q_m^j,0^{n-j}),
 \qquad
 E_{\sigma,\mathrm{raw}}(\varphi)
 :=\lim_{m\to\infty}E_{\sigma,\mathrm{raw}}(\varphi_m).
 \tag{16}
$$
Since $q=\pi^*\psi$ and $q_m=\pi^*\max(\psi,-m)$, (15), bounded intersection energy, and decreasing continuity in the ample theory give
$$
 E_{\sigma,\mathrm{raw}}(\varphi)=E_{A,\mathrm{raw}}(\psi),\quad
 E_{\sigma,\mathrm{raw}}(\sigma)=0,\quad
 E_{\sigma,\mathrm{raw}}(\varphi+c)=E_{\sigma,\mathrm{raw}}(\varphi)+Vc.
 \tag{17}
$$
Thus (16) is an intrinsic relative energy on actual original-carrier potentials. Its use of $H=L-aE$ is a retained movable datum determined here by the actual fixed part; the genuine quotient, not a value at a chosen lift, is used in every integral. It is concave, increasing, weakly upper semicontinuous, and decreasing-net continuous by (17) and the homeomorphism (7).

The actual relative finite-energy space is
$$
 \mathcal E^1(X,L;\sigma)
 :=\{\varphi\in\operatorname{PSH}(X,L):E_{\sigma,\mathrm{raw}}(\varphi)>-\infty\}
 =\sigma+\pi^*\mathcal E^1(Y,A).
 \tag{18}
$$
The reference is retained even when $\psi$ is unbounded; (18) is not limited to potentials a bounded distance from $\sigma$. It is a full relative finite-energy locus in the entire cone (7). No abstract completion is used, and no definition identifies it with $\operatorname{PSH}(X,L)$ intersected with BJ's ample-generated ambient vector space. The latter substitution could exclude the logarithmic fixed part or impose an unrelated energy condition.

For finite-energy $\varphi,\varphi'$, the difference formula on $X$ is
$$
 E_{\sigma,\mathrm{raw}}(\varphi)-E_{\sigma,\mathrm{raw}}(\varphi')
 =\frac1{n+1}\sum_{j=0}^n
  \int (Q\varphi-Q\varphi')\,
       M_\sigma(\varphi^j,(\varphi')^{n-j}).
 \tag{19}
$$
The integrals are finite by their ample counterparts and (15). No difference of infinite fixed-part values is integrated on $E$. Concavity and differentiation along genuine convex paths follow from (19) and the ample theory.

## 4.3. No loss of mass in unbounded decreasing nets

If $\varphi_{ij}\downarrow\varphi_i$ in (18) with genuine finite-energy limits, the corresponding $\psi_{ij}$ decrease on common divisorial coordinates. At off-$E$ points this follows directly by subtraction of the finite reference. Divisorial order and determination give the decreasing order on all of $Y$, and the genuine limit there is $\psi_i$. The ample mixed measures $\nu_j$ converge weakly to $\nu$, with $\nu(\{p\})=0$.

We verify that their zero-extended measures converge weakly on the original $X$, which is not automatic from pushforward alone. For $F\in C^0(X^{\mathrm{an}})$, $F\circ\pi^{-1}$ is bounded continuous on $Y^{\mathrm{an}}\setminus\{p\}$. For any $\varepsilon>0$, regularity and compact Hausdorff separation give a continuous cutoff $0\le\chi\le1$, equal to one near $p$, with $\int\chi\,d\nu<\varepsilon$. The function $(1-\chi)(F\circ\pi^{-1})$, extended by zero near $p$, is continuous on $Y^{\mathrm{an}}$. Weak convergence handles it and gives $\int\chi\,d\nu_j<2\varepsilon$ on a tail. The omitted integrals are bounded by $2\|F\|_\infty\varepsilon$ at finite stages and by $\|F\|_\infty\varepsilon$ at the limit. Let $\varepsilon\downarrow0$. This proves weak original-carrier convergence for nets, including unbounded potentials. The bounded floors used in (16) are a special case. Integrable quotient-weighted pairings and their limits are the actual ample weighted pairings by (15); a difference of two tests is handled term by term.

# 5. Target condition, comparison, differentiation and attained equation

For a positive Radon measure $\mu$ on $X^{\mathrm{an}}$ of raw mass $V$, define the intrinsic relative target energy
$$
 D_\sigma(\mu)=
 \sup_{\varphi\in\mathcal E^1(X,L;\sigma)}
       \left(E_{\sigma,\mathrm{raw}}(\varphi)-\int Q\varphi\,d\mu\right).
 \tag{20}
$$
The test $Q\varphi$ is the unique global genuine quotient (8); thus (20) depends on actual original potentials, their intrinsic reference and the retained movable datum. Raw $\varphi$-integrability is not substituted for quotient-integrability: the fixed logarithm $\sigma$ may have divergent integrals even when the relative quotient is integrable. Constants make the objective invariant exactly at mass $V$. If a test is not integrable, its objective is $+\infty$.

Write $\nu=\pi_*\mu$. Equations (7) and (17) give the exact equality
$$ D_\sigma(\mu)=E_{A,\mathrm{raw}}^\vee(\nu). \tag{21} $$
Consequently (20) is finite exactly when **every** actual relative finite-energy quotient $Q\varphi$ is $\mu$-integrable, by the ample intrinsic integrability theorem. Finiteness forces $\nu(\{p\})=0$, since finite-energy ample measures do not charge the pluripolar algebraic point. Therefore
$$ D_\sigma(\mu)<\infty\quad\Longrightarrow\quad\mu(E^{\mathrm{an}})=0. \tag{22} $$
No separate support condition is silently imposed: (22) is a proved consequence of the intrinsic admissibility condition. Outside this excluded algebraic locus, targets have arbitrary support and need not be skeletal or invariant.

**Theorem 2 (actual endpoint equation).** Under exactly the hypotheses of Theorem 1, (14) maps (18) onto all positive Radon measures of raw mass $V=\operatorname{vol}(L)$ with $D_\sigma(\mu)<\infty$. Each equation
$$ \operatorname{MA}_{\sigma,\mathrm{raw}}(\varphi)=\mu \tag{23} $$
has a genuine actual $L$-metric on original $X$ in (18), unique modulo one real constant. Its variational objective in (20) is actually attained. The operator has genuine mixed locality on the complement of the reference pole set and relative finite-energy comparison on all of $X$.

*Proof.* By (21), the actual ample theorem supplies a genuine $\psi\in\mathcal E^1(Y,A)$, an attained maximizer, satisfying $\operatorname{MA}_{A,\mathrm{raw}}(\psi)=\nu$. Set $\varphi=\sigma+\pi^*\psi$. Section 3 proves actual original-bundle membership and (18) proves its finite energy. Its objective is the attained ample objective, so attainment on $X$ follows. Section 4 proves that its measure is the genuine original local product, zero on $E$, with pushforward $\nu$. By (22), $\mu$ is also zero on $E$. Since $\pi$ is an isomorphism on the remaining analytic locus, these two Radon measures are equal, establishing (23).

One can see explicitly the compactness and attainment mechanism rather than merely assigning a solution to a lifted measure. Normalize $\sup\varphi=0$ and set $J_\sigma(\varphi)=-E_{\sigma,\mathrm{raw}}(\varphi)/V$. Under (7) it equals the ample $J$. Maximizing sequences for (20) have bounded $J$ by the granted coercive estimate. Their quotients have an actual compact psh limit on $Y$, hence the original functions have a limit in (7). Lower semicontinuity of $J$ makes this limit finite energy. The target integral is continuous on bounded-$J$ sets by (21) and the granted ample target-continuity theorem. Energy upper semicontinuity establishes attainment. Each input and the limit is an actual function; no Cauchy completion or arbitrary lift is introduced.

For $\varphi,\varphi'\in(18)$, the set $\{\varphi<\varphi'\}$ off $E$ corresponds to $\{\psi<\psi'\}$ off $p$. The raw comparison inequality is consequently
$$
 \int_{\{\varphi<\varphi'\}}
       \operatorname{MA}_{\sigma,\mathrm{raw}}(\varphi')
 \le
 \int_{\{\varphi<\varphi'\}}
       \operatorname{MA}_{\sigma,\mathrm{raw}}(\varphi).
 \tag{24}
$$
On $E$ both potentials equal $-\infty$ and both measures vanish; thus (24) is valid on the original carrier. Strict-winning locality and mixed locality on open sets follow in the same way from genuine ample locality and the local frame identity (13). If two solutions have the same measure, their pushforwards solve the same ample equation. Their genuine quotients differ by one constant, hence their original metrics differ by that constant (in the sense $\varphi=\varphi'+c$ at every point). Conversely a constant shift preserves (14). Finally, any finite-energy solution has finite dual energy by the ample energy concavity theorem and computes (20). This proves the exact target characterization. $\square$

The differentiation replacement established for this endpoint is explicit. For $g\in C^0(Y^{\mathrm{an}})$ define the outer energy for a quotient perturbation by the actual original formula
$$
 E^{\downarrow}_{\sigma,\mathrm{raw}}
      (\sigma+\pi^*(\psi+tg))
 :=E^{\downarrow}_{A,\mathrm{raw}}(\psi+tg).
 \tag{25}
$$
Then both derivative signs give
$$
 \left.\frac d{dt}\right|_{0}
 E^{\downarrow}_{\sigma,\mathrm{raw}}
     (\sigma+\pi^*(\psi+tg))
   =\int\pi^*g\,\operatorname{MA}_{\sigma,\mathrm{raw}}(\varphi).
 \tag{26}
$$
The relative envelope of such an obstacle is exactly
$$ \sigma+\pi^*P_A(\psi+tg). \tag{27} $$
Indeed, inequality against the obstacle on the complement is the same quotient inequality on all divisorial valuations on $Y$, and divisorial determination makes it the same everywhere. On $E$ the original obstacle and all candidates equal $-\infty$. Genuine membership and compactness in the quotient follow from the ample theory. Envelopes for arbitrary relative continuous quotient obstacles are transported by the same argument.

The tests in (26) identify all admissible original measures: if their pushforwards agree, they agree off $E$ by the isomorphism, and (22) removes the fiber. We do not claim a full outer-energy differentiation theorem for **every** $f\in C^0(X^{\mathrm{an}})$ with arbitrary values varying along $E$. Formula (25) is defined for pulled quotient directions. This limitation is stated rather than replaced by an unspecified quotient. It does not prevent (23), since admissible measures have zero mass on that fiber. It also does not solve the full differentiation gate on arbitrary big bundles.

The reference is preserved under a higher common modification: pull the actual frames and sections, compute the local products on the same complement, and use their existing pushforward and zero-extension identity. The uniqueness of the original quotient from its divisorial values makes the resulting original metric and energy independent of such an auxiliary computation. This does not assert that an arbitrary modified ample metric descends. All bundles used in (10), (13), (16) and (23) are fixed actual bundles on the displayed carriers.

# 6. Mass arithmetic and the zero-volume obstruction

## 6.1. A big class can have zero or negative top self-intersection

In Theorem 1, every intersection containing both $H$ and $E$ vanishes, because $H|_E$ is numerically trivial. The exceptional normal bundle is $\mathcal O_E(-1)$, so
$$ E^n=(-1)^{n-1},\qquad L^n=V+(-1)^{n-1}a^n,\qquad\operatorname{vol}(L)=V. \tag{28} $$
In particular, take $Y=\mathbb P^2$, $A=\mathcal O(1)$ and $a=1$. On $X=\operatorname{Bl}_p\mathbb P^2$,
$$ L=H+E,\quad L\cdot E=-1,\quad L^2=0,\quad
 h^0(X,mL)=\binom{m+2}{2},\quad\operatorname{vol}(L)=1. \tag{29} $$
Thus this is a positive-volume big nonample class, not a zero-volume class. The relative top mass in Theorem 2 is one. Dividing a putative big probability operator by $L^2$ would already fail on (29). With $a=2$, $L^2=-3$ while the volume remains one; a positive top measure cannot have that negative mass. These are mathematical intersection and section calculations, not numerical evidence for the whole big theory.

## 6.2. A genuine nef zero-volume cone need not have uniqueness

Let $k$ be any retained field, $X=\mathbb P^1\times\mathbb P^1$, and $L=\operatorname{pr}_1^*\mathcal O(1)$. Then $L$ is an actual nef semiample nonample bundle and $L^2=\operatorname{vol}(L)=0$: explicitly $h^0(X,mL)=m+1$, whose normalized quadratic growth is zero. Pull back a generating system $s_0,s_1$ from the first factor and fix $b>0$. The functions
$$
 0,\qquad u_b:=\max\{\log|s_0|,\log|s_1|+b\}-b
 \tag{30}
$$
are bounded genuine $L$-psh potentials. The canonical generating reference satisfies $\max\{\log|s_0|,\log|s_1|\}=0$ everywhere, so $-b\le u_b\le0$ and $\sup u_b=0$. Let $D=\{s_1=0\}\times\mathbb P^1$ and evaluate at the divisorial valuation $t\operatorname{ord}_D$. The first section is a unit there and the second has order one. For $t\ge b$,
$$ u_b(v_{\mathrm{triv}})=0,\qquad u_b(t\operatorname{ord}_D)=-b. \tag{31} $$
Hence $u_b$ and zero do not differ by a constant.

Choose a dominating actual ample bundle $B=\mathcal O(1,1)$. Since $B-L$ is nef, both bounded potentials are $B$-psh and have finite ample energy. Thus they lie in BJ's ambient finite-energy vector space. Its genuine **nef** raw intersection theorem applies to their actual $L$-metrics: each top measure is positive and has mass $L^2=0$. Every positive measure of mass zero is the zero measure. Therefore
$$ (c_1(L)+dd^cu_b)^2=(c_1(L)+dd^c0)^2=0. \tag{32} $$
This uses the genuine intersection operator within its proved nef bounded scope, not a different inverse measure. It proves that the raw top zero equation alone cannot imply uniqueness modulo constants in this cone. Probability normalization would divide zero mass by zero. Any lower-degree mixed replacement would require a specified auxiliary positivity datum, mass, actual quotient and proved injectivity; (32) does not provide those inputs.

## 6.3. The additional zero-volume equation range actually proved

On a smooth connected projective variety of dimension $n\ge1$ with the **actual trivial bundle** $\mathcal O_X$, BJ Corollary 4.24 gives $\operatorname{PSH}(X,0)=\mathbb R$. For completeness its argument is short. A zero-psh potential is $\varepsilon B$-psh for every positive $\varepsilon$ and fixed ample $B$. At a divisorial $v$, the Alexander--Taylor estimate gives $0\le\sup\varphi-\varphi(v)\le\varepsilon T_B(v)$; let $\varepsilon\downarrow0$. Thus the potential is constant on divisorial valuations and hence everywhere by genuine determination.

Retain reference zero and define raw energy $E_{0,\mathrm{raw}}(c)=0$ on these actual finite constant metrics. Their genuine top intersection is zero, of raw mass zero. The sole positive Radon target of mass zero is $\mu=0$. Its dual energy is $\sup_c(0-\int c\,d0)=0$, the objective is attained by every constant, and the solution is unique modulo constants because the quotient cone is a point. Comparison and differentiation are vacuous zero identities. No probability measure is introduced. This is a precisely stated degenerate zero-volume range. It does not extend to the nonconstant cone (30), much less to every pseudoeffective class of volume zero. Dimension zero is excluded here: its empty top product has mass one.

# 7. Why the full big rational-line-bundle theorem remains unproved

The literature in Section 2 establishes the genuine original psh cone, the actual minimal reference $V_L$ and its normalized compactness/envelope property for every retained smooth pseudoeffective class. We do not list these as remaining gaps. What remains for **every** big actual rational $L$ on the original $X$ is the following substantive program, none of whose missing steps is supplied by an ample grant.

**G1: original-carrier relative products and energy.** Construct the positive raw nonpluripolar products for arbitrary genuine section-generated singular $L$-metrics, with the actually retained reference $V_L$ or a precisely specified intrinsic model type. Prove independence of all Fujita/model approximations and give a genuine original-carrier limit, full mass $\operatorname{vol}(L)$ or the proved relative mass, and a well-defined actual relative $\mathcal E^1$. Scalar or measure limits on models do not prove this. The signed ample-generated product has mass $L^n$ and positivity only in the nef domain; (29) shows why it cannot simply be relabeled.

**G2: finite-energy differentiation and comparison.** Establish the relative mixed estimates, concavity, decreasing-net continuity, weighted convergence, original-carrier locality, comparison and domination on that entire actual space. Prove differentiability of the appropriate outer energy in every original continuous direction, and the reference-preserving orthogonality needed for variational identification. General psh envelope regularity supplies competitors, not these energy estimates. Nonnef truncation $\max(\varphi,-m)$ is not valid merely because it works in an ample class: a nonnef class has no bounded psh potential. The correct floors must use an actual retained reference.

**G3: intrinsic target integrability and actual attainment.** Specify all positive Radon targets of the correct raw mass by an intrinsic finite dual-energy condition on the genuine relative space. Prove its integrability characterization, the needed coercive bound and target integral continuity. Then show a maximizing family has a compactness limit of finite **relative** energy with an attained objective, identify its original genuine MA measure using both derivative signs, and prove uniqueness modulo constants within the prescribed reference domain. Compactness of the full normalized psh cone alone does not keep a limit in an unconstructed relative finite-energy space.

**G4: complete retained field and support domain.** The complex test-curve space (5) cannot be extended to arbitrary algebraically closed trivially valued characteristic-zero fields just by changing notation. The finite divisorial endpoint (6) does not establish arbitrary admissible support. Full big bundles need not have finitely generated section rings, need not be nef, and need not admit a single displayed ample contraction. We prove no reduction of that whole domain to (7). A sequence of ample Fujita models would require precisely the original-function, reference, product and attainment conclusions of G1--G3.

**G5: zero-volume replacement.** Specify the additional pseudoeffective domain to be handled when the top volume is zero. If one uses a lower-degree mixed product, give its auxiliary polarization, positive raw mass if any, original carrier, intrinsic reference quotient, admissible measures and injectivity mechanism; prove the full resulting equation. If one retains a zero top operator, prove uniqueness only where the actual quotient cone is a point, as in Section 6.3. The counterexample (30) rules out blanket uniqueness for that operator but is not a counterexample to every possible replacement theory.

These are precise unproved mathematical statements in this draft. The exceptional fixed-part domain proves an actual relative equation with arbitrary intrinsic finite-energy targets and no field cardinality restriction; its restricted outer-direction theorem is (26). It still leaves G1--G5 in the unrestricted original axis. Accordingly the canonical status is incomplete and `candidate=false`.

# 8. Evidence, reproducibility and limitations

`input-original.json` is byte-identical to the available `input.json`; `task-original.json` preserves its exact task value and `assignment-original.txt` its exact assignment string. The supplied inline mathematical blocks, including the entire ample grant and its source units, are preserved separately under `granted/`, `source-extracts/` and `supplied-primary-units/`. The assignment's documentary review labels are not read as proofs or operational instructions.

`external-premises.json` uses consecutive nonnegative zero-based premise indices, exact standalone scope statements, version-pinned primary HTTP(S) URLs, literal pertinent statement/proof units, coordinate conventions and SHA-256 bindings. Supplied units retain inclusive **one-based LF** coordinates of their supplied source text. Newly retrieved units retain the public renderer's literal **zero-based line/page labels**. These are different coordinate systems; we never fabricate original-PDF LF coordinates from rendered lines. The full Theorem A proof and the retained cone/base-ideal proof units are present. For the scope-only Kähler comparison paper we retain the relevant hypotheses and statement, and claim no full equation-proof reading. No theorem from that paper is used to deduce our endpoint.

Public source reading used the available HTTP renderer. Its response JSON and the literal retained units are checksummed. The tool did not return a full original PDF binary, and the local Python PDF request failed with `Operation not permitted`; therefore original-PDF binary checksums are unavailable rather than invented. Full-source hashes mentioned in the supplied packet are clearly labeled supplied metadata, not freshly computed hashes. The version-pinned addendum PDF prints 6 September 2023 in its arXiv label and 7 September 2023 as paper date; its HTML rendering shows a different date, so the PDF controls our version statement.

Run `python3 rerun.py` in this directory. It verifies preserved inputs and every literal unit binding, regenerates the exact-statement ledger, runs lightweight rational arithmetic checks, builds the TeX with installed Pandoc, and runs installed pdfLaTeX twice. Exact argv, environment/tool versions, stdout/stderr and artifact hashes are retained under `logs/` and in the manifests. No package installation, editor/repository/source-cache mutation, private database, authentication material, outside worker output or external messaging is used. No resource-heavy computation is needed; no supervised compute service was exposed. The finite checks evaluate (28)--(31) on explicitly listed rational parameters and verify their arithmetic; they do not exhaust a geometric domain or certify the proofs.

The deliverable is a standalone incomplete research paper plus rerunnable evidence, not a claimed solution of original P16.5. The successful provenance checks certify only the specified bytes and finite calculations. Compilation certifies only that existing tools produced a PDF. Neither operation establishes mathematical correctness of these unverified drafts.

# References

1. S. Boucksom and M. Jonsson, *Global pluripotential theory over a trivially valued field*, arXiv:1801.08229v4, 27 March 2022. Primary literal units supplied with the task and additional pertinent public units retained.
2. S. Boucksom and M. Jonsson, *Addendum to the article “Global pluripotential theory over a trivially valued field”*, arXiv:2206.07183v2, 6 September 2023; PDF date 7 September 2023. Theorem A, Lemmas 1.5--1.7 and Corollaries 2.1--2.3.
3. S. Boucksom and D. Eriksson, *Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry*, arXiv:1805.01016v3. Sections 7--8 literal primary units supplied with the task.
4. T. Darvas, M. Xia and K. Zhang, *A transcendental approach to non-Archimedean metrics of pseudoeffective classes*, arXiv:2302.02541v3, 17 July 2024; *Comment. Math. Helv.* 100 (2025), 269--322, DOI 10.4171/CMH/586.
5. R. Dervan and R. Reboulet, *A birational version of K-stability for big classes*, arXiv:2603.25605v1, 26 March 2026. Sections 2 and 3, source-scope comments and the displayed finite-target proof.
6. P. Mesquita-Piccione and D. Witt Nyström, *A transcendental non-Archimedean Calabi--Yau theorem with applications to the cscK problem*, arXiv:2509.09442v1, 11 September 2025. Retained positivity hypotheses and theorem statement only.
7. Exact task-granted full P16.1 mathematical body, actual ample rational bundle scope only, preserved verbatim in `granted/block-00.txt`. This is a task premise, not an independently recertified publication.
