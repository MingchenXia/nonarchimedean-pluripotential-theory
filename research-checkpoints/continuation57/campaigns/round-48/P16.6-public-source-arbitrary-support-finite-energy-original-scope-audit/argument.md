# Literal entire original family

10     The general non-Archimedean Monge–Ampère equation
Active items: P16.1, P16.2, P16.3, P16.4, P16.5, P16.6, P16.7. Status: Open in the
residual scope.

10.1    Atomic targets
P16.1 (T5): Finite-energy equations on singular or unibranch varieties
Extend the ﬁnite-energy non-Archimedean Monge–Ampère operator and its existence-and-
uniqueness theorem to singular or unibranch varieties, replacing each use of smoothness in
compactness, envelopes, energy diﬀerentiation and comparison. State all retained polarization
and ﬁeld hypotheses.

P16.2 (T5): Proper nonprojective algebraizable equation theories
Construct an appropriate replacement positivity datum and the associated psh, ﬁnite-energy,
comparison and equation theory on proper nonprojective algebraizable spaces. A proper
algebraic scheme with an ample line bundle is already projective, so retaining that datum
while dropping projectivity is not a new case.

P16.3 (T5): Finite-energy equations in positive residue characteristic
Construct the required ﬁnite-energy operator and prove existence and uniqueness when the
original residue-characteristic restriction is removed. Replace the resolution, model-regularity
and envelope inputs wherever they are used rather than merely changing the standing ﬁeld
hypothesis.

P16.4 (T4): Finite-energy equations over arbitrary complete valued ﬁelds
Extend the operator and existence theorem to nondiscrete valuations and arbitrary complete
non-Archimedean ﬁelds outside the established invariant-toric, skeleton-supported endpoint.
A deﬁnition of the ﬁnite-energy space alone does not establish the operator or the equation.

P16.5 (T5): Finite-energy equations for nonample positivity classes
Extend the equation theory to big or pseudoeﬀective nonample classes, specifying the psh cone,
reference singularity type, energy and total mass. At zero volume, the existing probability
normalization must be replaced rather than retained unchanged.

P16.6 (T4): Arbitrary-support ﬁnite-energy measures
Prove the operator and existence-and-uniqueness theorem for arbitrary ﬁnite-energy measure
support beyond the known toric skeletal regime. Measures must satisfy the correct mass and
energy conditions. Do not reduce arbitrary support to a single skeleton or replace the genuine
Monge–Ampère measure by another inverse measure construction.

P16.7 (T5): Finite-energy equations on nonalgebraizable analytic spaces
Construct the ﬁnite-energy operator and its existence-and-uniqueness theory on genuinely
nonalgebraizable analytic spaces, with an explicit positivity datum and the necessary com-
pactness, envelope and comparison replacements.




                                              73

10.2    What constitutes a solution
For each axis, state the retained hypotheses and construct the ﬁnite-energy operator together
with the corresponding existence-and-uniqueness theorem. Specify the measure mass and
ﬁnite-energy condition, uniqueness modulo constants and the replacement inputs for com-
pactness, envelopes, energy diﬀerentiation and comparison. An endpoint solving a special
toric measure class does not remove a general axis.

10.3    Full statement and detailed state of the art
Problem 10.1. Extend the ﬁnite-energy existence and uniqueness theory for the NA Monge–
Ampère equation beyond the currently proved combinations of smoothness, projectivity,
residue characteristic, valuation, positivity class, support, and algebraizability hypotheses.

    This is not one yes-or-no assertion. Positive characteristic, singular or unibranch varieties,
nondiscrete valuations, big classes, arbitrary support, and nonalgebraizable analytic spaces
require diﬀerent inputs. The known variational proofs use compactness, envelope regularity,
diﬀerentiability of energy, and a comparison principle; deleting a geometric hypothesis is valid
only after replacing every place where it enters. The relevant positive results and their distinct
domains are surveyed in Book Chapter 28, Book Chapter 29.
    The projectivity axis has one logical constraint. A proper algebraic K-scheme endowed
with an ample line bundle is already projective over K [Stacksb, Tag 0B5N]. Thus P16.2
cannot mean that one retains the BFJ line-bundle polarization L while simply deleting the
word “projective.” A nonprojective proper algebraizable extension must ﬁrst replace that
positivity datum—and then construct the corresponding psh, ﬁnite-energy, and comparison
theory—rather than merely rerun the original argument. No canonical replacement with the
required equation theory is asserted here.
    One exact source-stated axis is especially clean. Pille–Schneider observes that the ﬁnite-
energy space can be deﬁned over an arbitrary non-Archimedean ﬁeld, but that the extension of
the Monge–Ampère operator is not known there in general; the discretely valued characteristic-
zero and trivially valued cases are the established endpoints [PS23, Remark 4.4]. This should
be solved before bundling all remaining axes into a single theorem.

Proposition 10.1 (Arbitrary-ﬁeld invariant toric skeletal endpoint). Let K be a complete
nontrivially valued non-Archimedean ﬁeld, XΣ a proper toric K-variety, and L an ample toric
line bundle. If µ is a positive Radon measure on XΣan , is supported on the canonical skeleton
NΣ , gives zero mass to NΣ \NR , and has total mass degL (XΣ ), then there is a toric continuous
singular psh metric on L whose Monge–Ampère measure is µ. It is unique up to multiplication
of the metric by a positive constant.

    Thus nondiscreteness and the arbitrary complete ground ﬁeld cause no obstruction in
this invariant toric, skeleton-supported range. Here “continuous singular” has the source’s
extended-valued meaning: local weights are continuous into R ∪ {−∞}, as in [BGGJK25,
§5.3.1]. It does not imply ﬁnite real-valued weights or ﬁnite energy. This is not an arbitrary-
ﬁeld ﬁnite-energy theorem in the BFJ sense: the result permits a singular potential, requires
torus invariance and skeletal support, and does not construct the general extended Monge–
Ampère operator. In particular, P16.4 and P16.6 retain the respectively nonskeletal and
noninvariant ﬁnite-energy residual scopes.
    There is also a distinct, nonproper algebraic endpoint. Let n > d ≥ 1, let X be a smooth
projective Fano complex variety of dimension n, and let D be a reduced simple-normal-crossing
anticanonical divisor whose dual complex is the standard (d−1)-simplex. For the aﬃne Calabi–
Yau complement X = X \ D, Wang’s Theorem A constructs a continuous non-Archimedean
psh function on X an , over the trivially valued ﬁeld C, whose local Monge–Ampère measure

                                               74

is the canonical Lebesgue measure on the essential skeleton [Wan25]. The source is a version-
one preprint and uses a local CLD/tropical–convex construction. In particular, it neither
constructs the BFJ ﬁnite-energy operator nor treats arbitrary measures or arbitrary aﬃne
varieties. Since X is aﬃne and hence not proper, this endpoint does not answer P16.2; it
only records a special nonprojective algebraic solution after the properness requirement is
also dropped.
    There is a separate ﬁnite-atomic inverse statement which must not be called a ﬁnite-energy
Monge–Ampère theorem. Under its standing assumptions that K is maximally complete and
|K × | = R>0 , Fang ﬁxes an irreducible projective K-variety with an ample line bundle and a
ﬁnite set of graded birational points on its aﬃne cone. For every probability vector on that
ﬁnite set, the source constructs a Shilov-ﬁnite, possibly singular metric having the prescribed
equidistribution measure [Fan25, Proposition 4.8]. The source itself says that comparing this
Banach-algebra measure with the genuine Monge–Ampère measure requires the separate con-
tinuity property of an envelope metric. Thus it supplies neither a continuous semipositive
solution nor the BFJ ﬁnite-energy operator for the prescribed atomic measure, and does not
narrow P16.6.
    There is also a resolved negative regularity chronology. The ﬁrst skeletal-factorization
question of Gubler–Jell–Künnemann–Martin already fails on their toric surface [GJKM19,
Appendix A]. Boucksom–Jonsson then construct a ﬁnite atomic Monge–Ampère measure sup-
ported on a dual complex whose solution is invariant under no retraction attached to any
SNC model; they also construct a divisorial Green function that is not Q-PL [BJ24b, Theo-
rems A and B]. Hence support on a dual complex does not imply factorization through some
reﬁned skeleton. This is a theorem-level obstruction to a proof strategy, not an open regularity
expectation.
    The Rethlas programme treats each axis separately and ﬁrst searches the post-2020 liter-
ature for an existing theorem. Alterations and universal homeomorphisms can address some
algebraic descent questions, but they do not by themselves supply multiplier ideals or dif-
ferentiability in positive characteristic. The unrestricted formulation is open; several strictly
delimited axes are already known.




                                               75



# Author scoped status (its scope judgment is not authoritative)

{
  "id": "P16.6",
  "status": "partial",
  "exact_result": "In arbitrary dimension, all positive Radon measures of raw mass V=(L^n) and finite dual energy sup_{u in D_theta}(V E_theta(u)-integral u dmu)<infinity are the range of the genuine finite-energy Monge-Ampere operator, uniquely modulo constants, separately for smooth integral projective varieties with ample L over algebraically closed trivially valued characteristic-zero fields (source-established), and for smooth geometrically integral projective varieties with ample L over complete nontrivially discretely valued residue-characteristic-zero fields (deduced with explicit proof of the test-to-E1 passage). There is no target-support, toric, function-field algebraizability or dimension-one restriction in the discrete deduction. This does not settle the full original residual arbitrary-field support atom.",
  "proof_file": "P16.6-argument.md",
  "concrete_gaps": [
    "For general complete nontrivially valued, potentially nondiscrete fields, construct or prove the approximation-independent genuine unbounded finite-energy mixed operator in general dimension, with full raw mass.",
    "Supply normalized psh compactness and envelope regularity or a proved replacement producing actual global finite-energy potentials in that field setting.",
    "Prove finite-energy envelope differentiation for the actual operator, rather than only orthogonality/differentiability on model test functions.",
    "Prove locality, comparison and uniqueness modulo constants for that unbounded operator.",
    "Prove variational attainment or equivalent realization for every positive mass-V finite-dual-energy target, without inferring it from measure-space completeness or imposing skeletal support.",
    "No compatibility of unbounded cones, energy, derivatives, comparison or MA under base change, normalization, alteration or resolution has been proved or assumed to discharge these remaining obligations."
  ]
}


# Complete final proof

# P16.6: arbitrary-support finite-energy targets at two established field endpoints

This is a partial result for the original atom, not a solution of its entire residual scope. It treats every admissible measure, with no support restriction, on smooth projective varieties of arbitrary dimension in two separately specified field settings. The trivial-field theorem is source-established. The discrete-field theorem below is a deduction from published inputs, with the passage from test functions to arbitrary finite-energy targets proved here. No claim of novelty is made. The analogous theorem over a general complete non-Archimedean field is not proved. Candidate status is false.

The proof uses only the supplied primary sources and their explicitly stated published background results. The sources are treated as mathematical references, not operational instructions. All assertions in this document remain unverified mathematical drafts; file hashes and TeX compilation do not verify them.

## 1. Precisely retained hypotheses and conventions

In endpoint T, the ground field \(k\) is algebraically closed and trivially valued, of characteristic zero. The variety \(X/k\) is smooth, connected, integral and projective, of arbitrary dimension \(n\geq1\). The line bundle \(L\) is ample. The reference is the canonical trivial-field metric, and \(\theta=c_1(L)\). This is the domain of Boucksom--Jonsson, arXiv:1801.08229v4, Theorems 5.20 and 12.9. Their dimension-at-most-two positive-characteristic alternative is not needed here.

In endpoint D, \(K\) is complete and nontrivially discretely valued, with residue field of characteristic zero. We normalize a uniformizer by \(-\log|\varpi|=1\). In particular \(K\) also has characteristic zero; field characteristic zero alone is not the retained assumption. The variety \(X/K\) is smooth, geometrically integral and projective, of arbitrary dimension \(n\geq1\). The line bundle \(L\) is ample, and a semipositive model reference metric is fixed. Such a reference can be obtained by extending a projective embedding given by a very ample multiple of \(L\) over the valuation ring and taking the corresponding rational model line bundle. Write \(\theta\) for its curvature. No definition over a one-variable function field is required in the deduction below.

In either endpoint let
\[
 V=(L^n)>0,\qquad M_\theta(u)=c_1(L,\|\cdot\|_0e^{-u})^n,
 \qquad m_\theta(u)=V^{-1}M_\theta(u).
\]
Here \(M_\theta\) is the raw, genuine intersection-theoretic Monge--Ampere measure, extended below to finite energy; \(m_\theta\) is only its probability normalization. For a semipositive model metric on a common discrete model with special fiber \(\sum_E b_EE\),
\[
 M_\theta(u)=\sum_E b_E(\mathcal L_u|_E)^n\delta_{x_E},
 \qquad \sum_E b_E(\mathcal L_u|_E)^n=V.
\]
The analogous test-configuration formula is Proposition 7.19(ii) in the trivial-field source. In both formulas the weights are intersection numbers, not weights from an inverse Banach-algebra measure construction.

Let \(D_\theta\) be the semipositive model/PL test potentials, allowing real constants and real model coefficients; rational model tests are uniformly dense in this test cone as used in Boucksom--Jonsson 2307.01697v1, Example 2.13. Let \(\operatorname{PSH}(\theta)\) be the global psh cone obtained by decreasing model regularization. In D it is equivalently BFJ's cone, with topology of uniform convergence on every SNC dual complex, equivalently pointwise convergence on divisorial points. In T it is the cone of decreasing Fubini--Study nets with topology of pointwise convergence on divisorial valuations. These topologies do not require a potential or measure to factor through any single retraction.

For a model or bounded potential use the normalized energy
\[
 E_\theta(u)=\frac1{(n+1)V}\sum_{j=0}^n
 \int_{X^{\rm an}}u\,(\theta+dd^cu)^j\wedge\theta^{n-j},
 \qquad E_\theta(0)=0.
\]
Extend by the infimum of the energies of psh model majorants. Put
\[
 \mathcal E^1(\theta)=\{u\in\operatorname{PSH}(\theta):E_\theta(u)>-\infty\}.
\]
The infimum construction, upper semicontinuity, and decreasing continuity are source results, not consequences of merely defining this set.

For a positive Radon measure \(\mu\), the exact raw dual energy condition is
\[
 \mu(X^{\rm an})=V,\qquad
 \mathscr E_\theta(\mu):=
 \sup_{u\in D_\theta}\left\{VE_\theta(u)-\int u\,d\mu\right\}<\infty.
 \tag{1}
\]
Equivalently, for the whole measure \(\nu=\mu/V\),
\[
 Q_\theta(\nu)=\sup_{u\in D_\theta}
 \left\{E_\theta(u)-\int u\,d\nu\right\}<\infty,
 \qquad\mathscr E_\theta(\mu)=VQ_\theta(\nu).
 \tag{2}
\]
No restriction of a target measure is renormalized. Indeed constants give \(VE_\theta(c)-\int c\,d\mu=c(V-\mu(X^{\rm an}))\); the raw supremum is infinite at incorrect mass. This checks that mass is essential rather than optional notation.

## 2. Source identities and indispensable input audit

The saved equation paper is actual arXiv:1201.0188v1, with the v1 banner, even though its internal date reads October 29, 2018. Its Theorem A, printed pages 2--3, requires both function-field algebraizability and target support in one SNC dual complex. We do not erase those assumptions or attribute a later statement to these bytes. Its operator, energy and comparison results in Sections 2--7 have the standing smooth projective, discrete, residue-characteristic-zero assumptions and do not impose a target support condition. Algebraizability enters the proof of orthogonality in its Appendix A and its application to Theorem A; we replace that input below.

The saved arXiv:1201.0187v2 is BFJ's Singular semipositive metrics in non-Archimedean geometry. Its Theorem 7.10 gives compactness of normalized PSH and continuity of divisorial evaluations; Theorems 7.11 and 8.3 give the envelope property and continuity of envelopes; Theorem B/8.7 gives decreasing model regularization. These require the discrete residue-zero setting, smoothness, projectivity and ampleness. They do not require the function-field algebraizability of the equation paper.

The saved arXiv:1805.01016v3 is Boucksom--Eriksson's Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. Theorem 8.4 constructs the genuine mixed MA operator on continuous psh metrics over complete valued fields, with continuity for uniform convergence. We use this only on continuous metrics. Its Corollary B retains continuity of envelopes; neither statement supplies the unrestricted unbounded equation by itself.

The saved arXiv:2307.01697v1 is Boucksom--Jonsson's synthetic theory of measures. In its projective Berkovich realization, Section 1.2.2 uses model functions and intersection measures; Section 1.3.2 identifies the ample positivity class. Example 2.20 states test-function orthogonality over arbitrary non-Archimedean fields, using BE21 Theorem A and BGM22 Lemma 3.2 as published background. The application here is to a smooth geometrically integral projective variety and a semipositive model reference of ample class, within that statement. We invoke Example 2.20 as a published result, without pretending that BGM22 is one of the supplied PDF files or independently proving its lemma. Proposition 2.2, Theorem 1.26, Theorem 2.23, and Lemma 2.25 are also used, with their test-function domains preserved until the explicit extension in Section 5 below.

The saved arXiv:1801.08229v4 is the actual trivial-field global theory. Its Theorem A and Theorem 12.9 establish the arbitrary-support theorem in T. The saved Pille--Schneider arXiv:2209.04879v2, Remark 4.4, distinguishes defining \(\mathcal E^1\) over any field from extending MA there; its Theorem 4.7 is a skeleton-supported result. The phrase characteristic zero in Remark 4.4 is not used to remove residue-characteristic restrictions from the cited BFJ results.

The other four caches were audited without changing the domain. Gubler--Rabinoff arXiv:2506.13548v2 explicitly excludes constructing MA from its subject. Thuillier's HAL v1 thesis gives curve potential theory, which is not used to silently specialize to curves or \(\mathbf P^1\). Berkovich's 1993 paper is analytic/cohomological background; cohomological base change supplies none of the unbounded operator passages here. Chambert-Loir--Ducros arXiv:1204.6277v2 is the actual July 2025 revision; no applicability of its local-current constructions to all global BFJ finite-energy targets over arbitrary fields is established here. These are application limits of this audit, not a proof of nonexistence of future results.

## 3. Genuine finite-energy operator in endpoint D

BFJ 1201.0188v1 Theorem 3.1 first constructs the bounded mixed operator from model intersection measures, uniquely characterized by continuity under decreasing psh nets. Its locality principle permits the following construction. For \(u\in\operatorname{PSH}(\theta)\), after a constant shift put \(u\leq0\) and \(u_t=\max\{u,-t\}\). Define
\[
 M_\theta(u)=\lim_{t\to\infty}
 {\bf1}_{\{u>-t\}}M_\theta(u_t),
 \tag{3}
\]
an increasing limit on Borel sets. The restrictions for different truncation levels agree on their common upper locus by locality. This is Definition 6.4, not an inverse prescription of a measure.

For \(u\in\mathcal E^1\) its mass is exactly \(V\). To see the decisive bound directly, the bounded energy difference formula gives
\[
 E_\theta(u_{t/2})-E_\theta(u_t)
 \geq\frac1{n+1}\int(u_{t/2}-u_t)\,dm_\theta(u_t)
 \geq\frac{t}{2(n+1)}m_\theta(u_t)\{u\leq-t\}.
 \tag{4}
\]
The two energies tend to \(E_\theta(u)>-\infty\). Consequently the discarded mass is \(o(1/t)\), so it tends to zero and (3) has full raw mass. The positive increasing limit of finite Radon restrictions is Radon. Lemma 6.8 furthermore gives
\[
 \left|\int f\,dm_\theta(u_t)-\int f\,dm_\theta(u)\right|
 \leq\frac{2(n+1)|E_\theta(u)|}{t}\|f\|_\infty
 \tag{5}
\]
for a normalized nonpositive potential and model test \(f\). Proposition 6.9 proves decreasing continuity on \(\mathcal E^1\). Thus every decreasing model approximation of \(u\) gives the same weak measure (3); density of model tests in continuous functions makes this characterization unique. No single skeleton is used to support the target.

The source has normalized \(\{\omega\}^n=1\) in the energy sections. Here is the explicit application to unscaled \(L\). With \(\lambda=V^{-1/n}\), set \(\widetilde\theta=\lambda\theta\) and \(\widetilde u=\lambda u\). Then
\[
 \widetilde\theta^n=1,\quad
 M_{\widetilde\theta}(\lambda u)=V^{-1}M_\theta(u),\quad
 E_{\widetilde\theta}(\lambda u)=\lambda E_\theta(u).
 \tag{6}
\]
The cones and decreasing approximations correspond by this positive scalar multiplication. Truncation levels change from \(t\) to \(\lambda t\), so (3), decreasing continuity, and finite energy also correspond. This uses allowed real numerical classes and retains the raw datum \(L\). It is not a change of the target to a restricted or unrelated measure.

Proposition 6.11 gives locality and the finite-energy comparison inequality
\[
 \int_{\{u<v\}}M_\theta(v)\leq
 \int_{\{u<v\}}M_\theta(u),\qquad u,v\in\mathcal E^1(\theta).
 \tag{7}
\]
There is a sign slip in the actual printed v1 statement of Lemma 6.10, not just in OCR: it displays a positive integral of \(-v\), while its proof uses the negative integral of \(v\). We prove the integrability needed here directly. If \(u,v\leq0\) are finite-energy and \(w_{t,s}=(u_t+v_s)/2\), positivity of mixed measures and the bounded energy formula give
\[
 \begin{aligned}
 E_\theta((u+v)/2)&\leq E_\theta(w_{t,s})\\
 &\leq\frac1{n+1}\int w_{t,s}\,dm_\theta(w_{t,s})\\
 &\leq\frac{2^{-(n+1)}}{n+1}\int v_s\,dm_\theta(u_t)\\
 &\leq\frac{2^{-(n+1)}}{n+1}\int_{\{u>-t\}}v_s\,dm_\theta(u).
 \end{aligned}
 \tag{7a}
\]
For the third inequality, expand the mixed measure to obtain \(m_\theta(w_{t,s})\geq2^{-n}m_\theta(u_t)\) and use nonpositivity of \(w_{t,s}\), then \(w_{t,s}\leq v_s/2\). For the final inequality use locality on \(\{u>-t\}\) and discard a nonpositive integral. First let the integer \(s\) increase, and then \(t\) increase. Sequential monotone convergence and the fact that \(m_\theta(u)\) is carried by \(\{u>-\infty\}\) give
\[
 \int v\,dm_\theta(u)\geq (n+1)2^{n+1}E_\theta((u+v)/2)>-\infty.
 \tag{7b}
\]
The energy on the right is finite by concavity. Shifting constants proves integrability without a sign ambiguity. Proposition 6.12 supplies energy derivatives along psh segments, and Proposition 8.2 supplies uniqueness modulo constants when two \(\mathcal E^1\) potentials have equal genuine MA; its statement explicitly needs no orthogonality. These are retained source inputs with the scaling (6), not consequences of measure-space completeness.

## 4. Replacing discrete-field algebraizability in the orthogonality input

Write \(\widetilde E(f)=\sup\{E_\theta(a):a\in D_\theta,\ a\leq f\}\) for a continuous obstacle. In the synthetic source Definition 2.15 and Example 2.20 give
\[
 \lim_{a\in D_\theta,\ a<f}\int(f-a)\,dm_\theta(a)=0
 \qquad(f\in D).
 \tag{8}
\]
The order is the pointwise order on test functions, and that set is directed; this is stronger information than choosing an arbitrary energy-maximizing net without an order.

In endpoint D, BFJ's envelope \(P_\theta(f)\) is continuous for continuous \(f\), by 1201.0187v2 Theorem 8.3. Its model regularization is uniform by Dini's lemma. Shifting uniformly close model approximants slightly downward yields test functions strictly below \(f\) and arbitrarily close to \(P_\theta(f)\). Therefore the entire increasing directed net in (8) has pointwise supremum \(P_\theta(f)\); its convergence is uniform, again by Dini on the compact analytic space. Boucksom--Eriksson Theorem 8.4 now gives
\[
 \int(f-P_\theta(f))\,dm_\theta(P_\theta(f))=0
 \qquad(f\in D).
 \tag{9}
\]
Model functions are uniformly dense in continuous functions; the envelope is 1-Lipschitz in the uniform norm (BFJ Proposition 8.2), and MA is uniformly continuous into weak measures on continuous psh metrics. Passing to a uniform approximation of a general continuous \(f\) proves (9) for every continuous obstacle. This establishes exactly the classical orthogonality hypothesis of 1201.0188v1 Definition 7.1 without function-field algebraizability.

After (6), BFJ Theorem 7.2 and Corollary 7.3 apply. In the normalization used here, for every \(u\in\mathcal E^1\) and \(f\in C^0(X^{\rm an})\),
\[
 \left.\frac d{dt}\right|_{t=0}E_\theta(P_\theta(u+tf))
 =\int f\,dm_\theta(u).
 \tag{10}
\]
The unbounded version is the actual Corollary 7.3, whose proof uses decreasing regularization, Proposition 6.9, and an integral identity followed by dominated convergence. Mere differentiability along psh segments would not suffice for the Euler--Lagrange argument. Over a general field, continuity of \(P_\theta(f)\) was not proved in this audit, so the passage (8)--(10) cannot be exported there.

## 5. The passage to all finite-energy targets in endpoint D

For this section all energies and measures are normalized as in (2), without changing raw equation (1). Put \(m_0=m_\theta(0)\), a finite divisorial model measure, and
\[
 J(u)=\int u\,dm_0-E_\theta(u),\qquad
 r_\nu(u)=Q_\theta(\nu)-E_\theta(u)+\int u\,d\nu.
 \tag{11}
\]
For test functions \(r_\nu(u)\geq0\), and a maximizing sequence has \(r_\nu(u_i)\to0\). Synthetic Proposition 2.2(2.7), with one potential zero, gives
\[
 J(u_i)\leq C_n\big(r_\nu(u_i)+Q_\theta(\nu)\big).
 \tag{12}
\]
The submean value property, synthetic Theorem 1.26 applied to the integral variety, gives \(T<\infty\) such that \(\sup u-\int u\,dm_0\leq T\). Decreasing approximation extends it to all psh potentials. Hence for \(\sup u=0\),
\[
 0\leq-E_\theta(u)\leq J(u)+T.
 \tag{13}
\]

First, finite dual energy implies that every \(u\in\mathcal E^1\) is \(\nu\)-integrable, and that
\[
 Q_\theta(\nu)=\sup_{u\in\mathcal E^1}
 \left(E_\theta(u)-\int u\,d\nu\right).
 \tag{14}
\]
Indeed, choose a decreasing psh model net \(a_\alpha\) tending to \(u\). Its energy tends to \(E_\theta(u)\). The dual inequality gives \(\int a_\alpha d\nu\geq E_\theta(a_\alpha)-Q_\theta(\nu)\), uniformly bounded below. Integration of decreasing upper semicontinuous nets against finite Radon measures commutes with the limit by BFJ 1201.0188v1 Lemma 2.23 (not by an unrestricted monotone-convergence assertion for arbitrary nets). Thus \(\int u\,d\nu\) is finite and the dual inequality holds for \(u\). Together with \(D_\theta\subset\mathcal E^1\) this proves (14).

The decisive continuity lemma is that if \(u_i\to u\) in BFJ's psh topology and \(J(u_i)\) is bounded, then \(u\in\mathcal E^1\) and \(u_i\to u\) in \(L^1(\nu)\). Here is the missing passage in full, rather than an appeal to completeness of measures.

Choose model tests \(\tau_j\) maximizing (2); (12) bounds \(J(\tau_j)\). For \(R\) larger than these bounds and \(Q_\theta(\nu)\), synthetic Lemma 2.25(2.27), with the second test potential zero, states
\[
 \left|\int a\,(d\nu-dm_\theta(\tau_j))\right|
 \leq C_R\,r_\nu(\tau_j)^{1/2}
 \quad(a\in D_\theta,\ J(a)\leq R).
 \tag{15}
\]
To check the dependence, its right hand side before absorbing bounded terms is a constant times \(J_\theta(a,0)^{2^{-n}}r_\nu(\tau_j)^{1/2}R^{1/2-2^{-n}}\). The comparison \(J_\theta(a,0)\asymp J_\theta(0,a)=J(a)\) is synthetic (1.34). The PDF, printed page 25, has absolute-value bars omitted by the cached OCR; the rendered page verifies the two-sided estimate.

For \(a\in\mathcal E^1\) with \(J(a)\leq R\), take decreasing model majorants. Their energies converge and their integrals against \(m_0\) converge, since \(m_0\) has finite divisorial support, so their \(J\)'s eventually lie below \(R+1\). Integrability just proved and the same Radon-net lemma pass the left side of (15) to the limit. Thus (15), with \(C_{R+1}\), holds for every such finite-energy \(a\), uniformly in \(a\).

The functional \(J\) is lower semicontinuous in the psh topology: \(E_\theta\) is upper semicontinuous and integration against \(m_0\) is continuous on that topology. Hence \(J(u)\leq\liminf J(u_i)<\infty\). For each fixed \(j\), \(m_\theta(\tau_j)\) has finite divisorial support and therefore \(\int u_i\,dm_\theta(\tau_j)\to\int u\,dm_\theta(\tau_j)\). The uniform estimate (15), first letting \(i\) tend to its limit and then \(j\to\infty\), proves \(\int u_i\,d\nu\to\int u\,d\nu\).

For absolute convergence put \(w_i=\max\{u_i,u\}\). The supremum of \(u_i\) is bounded because it is continuous in the psh topology. Their integrals against \(m_0\) are bounded, and \(J(u_i)\) is bounded, so \(E_\theta(u_i)\) is bounded below. Monotonicity gives \(E_\theta(w_i)\geq E_\theta(u_i)\), while \(\int w_i dm_0\leq\sup w_i\) is bounded above. Thus \(J(w_i)\) is bounded. Divisorial evaluations show \(w_i\to u\) in the psh topology, so the preceding integral argument applies to \(w_i\) as well. Finally \(|u_i-u|=2w_i-u_i-u\) holds almost everywhere where these integrable potentials are finite, giving \(\int|u_i-u|d\nu\to0\). This proves the lemma for nets, including the subnet required below.

For completeness, condition (2) is also equivalent in D to integrability of every \(\mathcal E^1\) potential. Only the converse needs proof. Suppose \(\mathcal E^1\subset L^1(\nu)\). There is a uniform bound for \(-\int a\,d\nu\) on normalized model tests with \(J(a)\leq1\). Otherwise choose \(a_j\leq0\), \(\sup a_j=0\), \(J(a_j)\leq1\), and \(-\int a_jd\nu\geq2^j\). The partial sums \(b_m=\sum_{j=1}^m2^{-j}a_j\), with the remaining weight on zero, are psh, decrease, and by concavity and (13) satisfy \(E_\theta(b_m)\geq-(1+T)\). Their decreasing limit is psh rather than identically minus infinity: its integral against the finite-support \(m_0\) cannot tend to minus infinity, since \(\int b_mdm_0\geq E_\theta(b_m)\). Decreasing energy continuity puts the limit in \(\mathcal E^1\), whereas ordinary sequential monotone convergence gives integral minus infinity against \(\nu\), a contradiction.

Synthetic (1.36) gives \(J(ta)\leq C_nt^2J(a)\) for \(0\leq t\leq1\). Apply the uniform bound just proved to \(ta\) with \(t=\min\{1,(C_nJ(a))^{-1/2}\}\). For normalized model tests this gives \(-\int a\,d\nu\leq A(1+\sqrt{C_nJ(a)})\). Since \(E_\theta(a)=\int a\,dm_0-J(a)\leq-J(a)\), the quantity \(E_\theta(a)-\int a\,d\nu\) is uniformly bounded above. Taking the supremum proves (2). This is the discrete adaptation of the argument printed in the trivial-field source Theorem 9.20, with the submean constant \(T\) accounted for.

## 6. Existence, exact range, and uniqueness in endpoint D

Let \(\mu\) satisfy (1), and set \(\nu=\mu/V\). Choose a model maximizing sequence \(u_i\) for (2), and subtract its supremum. Both \(J\) and \(r_\nu\) are invariant under constants. Equations (12)--(13) bound \(-E_\theta(u_i)\). BFJ 1201.0187v2 Theorem 7.10 gives a subnet converging in normalized PSH to \(u\). Upper semicontinuity of energy puts \(u\) in \(\mathcal E^1\). The continuity lemma gives convergence of the \(\nu\)-integrals, so
\[
 E_\theta(u)-\int u\,d\nu
 \geq\limsup_i\left(E_\theta(u_i)-\int u_i\,d\nu\right)
 =Q_\theta(\nu).
 \tag{16}
\]
Equality follows from (14). This proves actual attainment, which density or completeness of the measure space alone would not prove.

For \(f\in C^0\), put \(v_t=P_\theta(u+tf)\). The upper obstacle is usc, so its usc psh envelope remains below it by the envelope property. Also \(v_t\geq u-|t|\|f\|_\infty\), hence \(v_t\in\mathcal E^1\). Maximality and the obstacle inequality yield
\[
 E_\theta(v_t)-E_\theta(u)
 \leq\int(v_t-u)\,d\nu\leq t\int f\,d\nu.
 \tag{17}
\]
Divide for positive and negative \(t\) and use (10). It follows that \(\int f\,dm_\theta(u)=\int f\,d\nu\) for every continuous \(f\). Equality of Radon measures gives \(M_\theta(u)=\mu\), for the genuine operator (3).

Conversely, if \(u\in\mathcal E^1\) and \(\mu=M_\theta(u)\), full mass gives \(\mu(X^{\rm an})=V\). Concavity and the energy derivative along psh segments imply
\[
 E_\theta(a)-\int a\,dm_\theta(u)
 \leq E_\theta(u)-\int u\,dm_\theta(u)<\infty.
\]
The last integral is finite by (7b). Decreasing approximation of \(u\) shows equality at the supremum. Therefore the range is exactly the positive raw-mass-\(V\) measures satisfying (1). Two solutions differ by a constant by BFJ Proposition 8.2, with no target support or algebraizability assumption. Comparison is (7). Multiplication of the metric by a positive constant is exactly addition of a constant to the potential.

## 7. Endpoint T: the independently established arbitrary-support theorem

This theorem is already stated in 1801.08229v4; it is not a newly proved arbitrary-field extension. We record how its proof covers the operator and the equation under the precise T hypotheses.

The source Theorem 7.1 extends the intersection energy pairing by monotone majorants, uniquely and continuously along decreasing nets. Theorem 7.8 ensures finiteness of the mixed pairing on finite-energy potentials. Theorem 7.18 defines the mixed MA measure by testing this pairing against PL functions; these functions span a uniformly dense subspace of continuous functions. Positivity of the pairing gives a positive functional, its value on constants gives mass \(V\), and Riesz gives a unique Radon measure. Proposition 7.19 verifies the model intersection formula and decreasing continuity. Thus the extension is approximation-independent and is the genuine MA operator. Theorems 7.40 and 7.44 prove finite-energy locality and comparison. This construction does not prescribe a measure by another inverse operator.

Smoothness and characteristic zero imply the envelope property by Theorem 5.20. Corollary 5.21 gives compact normalized PSH and Lemma 5.17 gives continuity of continuous-obstacle envelopes. Theorem 8.5 and Corollary 8.6 give energy differentiation through \(P\); Proposition 9.19 proves \(L^1(\nu)\) continuity on bounded-energy sets. Theorem 9.20 says exactly that \(Q_\theta(\nu)<\infty\) iff all \(\mathcal E^1\) potentials are integrable against \(\nu\).

For an arbitrary such probability measure, the printed proof of Theorem 12.8 takes a normalized maximizing sequence, bounds its energy by (9.11), extracts a psh subnet by compactness, and uses Proposition 9.19 and energy upper semicontinuity to prove attainment. Corollary 9.12 identifies its maximizer with a genuine MA solution using the energy derivative. Proposition 12.7 gives injectivity modulo constants; Theorem 12.9 concludes existence and uniqueness. Restoring raw mass multiplies the measure by \(V\), exactly as in (1)--(2). There is no assumed torus action or skeletal support at any step. Thus T is an independent general-dimension arbitrary-support result, not evidence that D or a densely valued field automatically inherits it.

## 8. Reference independence and the exact partial theorem

In D, if another semipositive model reference differs by a bounded model potential \(h\), then \(\theta'=\theta+dd^ch\) and the same metric is represented by \(u'=u-h\). Model curvature identities, the energy cocycle, and decreasing continuity give
\[
 M_{\theta'}(u-h)=M_\theta(u),\qquad
 E_{\theta'}(u-h)=E_\theta(u)-E_\theta(h).
 \tag{18}
\]
To check the unbounded passage, model majorants \(u_\alpha\downarrow u\) transform to \(u_\alpha-h\downarrow u-h\); both energy and MA are decreasing-continuous. The test cones correspond by the same translation. Consequently
\[
 Q_{\theta'}(\nu)=Q_\theta(\nu)+\int h\,d\nu-E_\theta(h),
 \quad
 \mathscr E_{\theta'}(\mu)=\mathscr E_\theta(\mu)+\int h\,d\mu-VE_\theta(h).
 \tag{19}
\]
All added terms are finite. Hence finite energy and the raw equation are reference-independent in the stated class. The same check uses the intersection-pairing cocycle for model/test-configuration references in T. No singularity type of a big or nonample class is substituted for the ample reference.

The partial theorem is therefore: separately in D and T, the genuine operator on \(\mathcal E^1(\theta)\) is independent of decreasing model approximations, has raw mass \((L^n)\), obeys comparison, and has range exactly (1). Every measure in that range has a solution unique modulo constants. There is no support restriction, toric invariance, or dimension-one assumption. The D proof replaces the old algebraizability-based orthogonality input and the old support-based integral continuity by Sections 4 and 5, while retaining BFJ's geometric compactness and envelope inputs. The T result is directly source-established.

## 9. Concrete original obligations still unresolved

The full P16.6 residual scope beyond these field endpoints is not settled by this document. Even retaining smoothness, geometrical integrality, projectivity and an ample line bundle, we have not proved the same arbitrary-support finite-energy theorem for every complete nontrivially valued, potentially nondiscrete field in the general-dimension noninvariant setting. No impossibility claim is made.

For such a field the supplied continuous operator and synthetic finite-energy measure theory leave the following indispensable tasks: establish compactness of the normalized global psh cone in a topology compatible with model evaluations; prove the needed envelope regularity or an actual substitute that realizes the limits as global psh potentials; construct the approximation-independent unbounded mixed operator with full raw mass and locality; justify finite-energy differentiation, not only test-function differentiation; prove comparison and uniqueness for that actual unbounded operator; and prove attainment or an equivalent realization theorem for every positive mass-\(V\), finite-dual-energy target. Some of these may follow from future inputs, but none is deleted by measure completeness alone.

The trivial-field source Theorem 12.8 explicitly makes potential completeness and MA surjectivity equivalent to an envelope property. Synthetic Theorem 2.26 proves completeness of measures over arbitrary fields, a different assertion. Its Remark 2.14 sets aside the needed potential theory. This is a precise logical obstruction to inferring the missing theorem, not a counterexample to it. Restricting targets to one skeleton, imposing toric invariance, switching to a different inverse measure, specializing to a curve, or using unproved base change would not discharge the original obligations.

No resolution, alteration, normalization or base-change preservation statement for an unbounded cone, energy, MA, or comparison is used. Singular spaces, positive residue characteristic, nonample classes, proper nonprojective spaces and nonalgebraizable spaces are the separate original atoms and are not claimed solved here.

## 10. Reproducibility, literal extracts, and evidence limits

The original input is retained byte-identically as input.json and input-original.json, with decoded assignment-original.txt and task-original.json. Run `python3 audit_sources.py` to verify the ten supplied PDF/text hashes, regenerate text directly from each actual PDF, and reproduce source-extracts/source-provenance.json with literal published proof blocks, versions, identities, application checks and limitations. The audit output in source-audit-output.txt records ten successful PDF re-extractions and all supplied hashes matching. The independently regenerated text is not substituted for the original cache identity.

Rendered actual-PDF pages retained in source-extracts/synthetic-page25.png, source-extracts/bfj-v1-page27.png and source-extracts/bj-v4-page122.png resolve the absolute values in synthetic (2.27), the full-mass truncation estimate, and the exact trivial-field theorem/proof respectively. The additional source-extracts/bfj-v1-page28.png verifies that the sign slip in Lemma 6.10 is present in the PDF itself; (7a)--(7b) supply the required bound. The provenance file records these inspections. Rerun page rendering and the two builds with `python3 build_artifacts.py`. That script regenerates a standalone P16.6-paper.tex from this complete argument and executes pdflatex twice in separate directories. Each actual stdout/stderr diagnostic stream, TeX log, command, exit code and hash is retained. The final PDF is P16.6-paper.pdf. Environment/tool versions are recorded in environment.json. An initial missing-package declaration for the mathscr command caused two failed TeX attempts; their actual diagnostics and source snapshot are retained in build/failed-missing-mathscr. The final preamble declares the existing mathrsfs package; no software was installed.

status.json has exactly the keys id, status, exact_result, proof_file and concrete_gaps. No heavy computation, supervised-compute job, network fetch, software installation, other model or subagent was used. These checks establish reproducibility and artifact/source identity, not mathematical correctness. The candidate flag remains false regardless of build success.

## References with exact supplied versions

[BFJ-PSH] S. Boucksom, C. Favre, M. Jonsson, Singular semipositive metrics in non-Archimedean geometry, arXiv:1201.0187v2.

[BFJ-MA-v1] S. Boucksom, C. Favre, M. Jonsson, Solution to a non-Archimedean Monge-Ampere equation, arXiv:1201.0188v1. Theorem A is not read as a statement of a later version.

[BE] S. Boucksom, D. Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry, arXiv:1805.01016v3.

[BJ-T] S. Boucksom, M. Jonsson, Global pluripotential theory over a trivially valued field, arXiv:1801.08229v4.

[BJ-S] S. Boucksom, M. Jonsson, Measures of finite energy in pluripotential theory: a synthetic approach, arXiv:2307.01697v1. Its Example 2.20 is the supplied source for the published-background BE21/BGM22 input.

[PS] L. Pille-Schneider, Global pluripotential theory on hybrid spaces, arXiv:2209.04879v2, especially Remark 4.4.

[GR] W. Gubler, J. Rabinoff, Classically psh and pluriharmonic functions on Berkovich spaces, arXiv:2506.13548v2.

[Thuillier] A. Thuillier, supplied thesis HAL tel-00010990v1.

[Berkovich] V. G. Berkovich, Etale cohomology for non-Archimedean analytic spaces, Publications mathematiques de l'IHES 78 (1993), 5--161, supplied Numdam PDF.

[CLD] A. Chambert-Loir, A. Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, arXiv:1204.6277v2, July 2025 revision.


# Every actual canonical note, including support

[
  {
    "id": "n1",
    "summary": "Exact-version audit of all ten supplied caches: BFJ 1201.0188 is v1 with algebraizability and SNC-support restrictions; 1805.01016 is Boucksom–Eriksson’s norms paper. Actual PDFs resolve an OCR omission and a printed sign slip.",
    "detailedSummary": "All supplied PDF, text and abstract hashes match, and all ten actual PDFs were successfully re-extracted. BFJ equation v1 Theorem A retains algebraizability and support on one SNC dual complex. Its operator sections have broader measure applicability. The trivial-field source establishes an arbitrary-support finite-energy theorem in general dimension. The synthetic source supplies test orthogonality and quantitative estimates over arbitrary fields, but measure completeness alone does not establish an unbounded-potential operator or surjectivity. Actual PDF inspection confirms absolute-value bars in synthetic (2.27) and a printed sign slip in BFJ v1 Lemma 6.10.",
    "text": "This is a source audit and artifact observation, not an exhaustive literature result or mathematical verification. Only the input, fresh workspace and ten authorized public caches were read. Running `python3 audit_sources.py > source-audit-output.txt 2>&1` successfully re-extracted all ten actual PDFs and reported every supplied hash check True. Literal proof extracts, versions, hashes, application checks and limitations are retained in source-extracts/source-provenance.json.\n\nThe saved 1201.0188 PDF is actual v1, SHA256 4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a. Its banner says v1, 30 Dec 2011, although its internal date reads 29 Oct 2018. Theorem A requires a complete discretely valued field of residue characteristic zero, smooth projective algebraizable X, ample L, target mass c1(L)^n, and support on one SNC dual complex. Its internal date does not justify attributing a later-version statement to these bytes. Sections 2–7 construct the genuine bounded and finite-energy operator, energy and comparison without imposing target support. Algebraizability enters its Appendix A orthogonality argument. Proposition 8.2 states finite-energy uniqueness without orthogonality.\n\nBFJ 1201.0187v2, SHA256 8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270, supplies normalized PSH compactness (Theorem 7.10), the envelope property and continuous envelopes (Theorems 7.11 and 8.3), and decreasing model regularization (Theorem B/8.7). Its setting is smooth projective geometry, ample polarization, and complete discrete residue-characteristic-zero fields. It does not require function-field algebraizability.\n\n1805.01016v3, SHA256 51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2, is Boucksom–Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry. Theorem 8.4 supplies the genuine continuous mixed MA operator and continuity under uniform convergence. It is not a differently titled pluripotential paper or a general unbounded finite-energy equation theorem.\n\n1801.08229v4, SHA256 8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52, establishes the arbitrary-support finite-energy theorem over an algebraically closed trivially valued field when X is smooth and characteristic zero, in arbitrary dimension. Its alternative positive-characteristic dimension-at-most-two statement is not used here.\n\n2307.01697v1, SHA256 979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1, supplies synthetic measure theory. Example 2.20 states test-function orthogonality for projective Berkovich spaces, using BE21 Theorem A and Boucksom–Gubler–Martin, Differentiability of relative volumes over an arbitrary non-Archimedean field, IMRN 2022 no. 8, 6214–6242, Lemma 3.2. This published background is invoked through the supplied source’s explicit assertion; no extra BGM PDF was supplied or fetched. Our smooth geometrically integral projective X is geometrically reduced, L is ample, and the semipositive model reference represents a class in Pos(X), satisfying the application domain. Theorem 1.26, Proposition 2.2, Theorem 2.23 and Lemma 2.25 provide the submean bound, coercivity and integral estimates. Theorem A/2.26 proves density and completeness on the measure side; Remark 2.14 sets aside the potential theory.\n\nActual PDF inspections are retained in source-extracts/synthetic-page25.png, bfj-v1-page27.png, bfj-v1-page28.png and bj-v4-page122.png. Synthetic (2.27) has absolute-value bars omitted by OCR. BFJ v1 Lemma 6.10’s actual printed statement contains a positive integral of −psi while its proof uses the negative integral of psi. The displayed statement alone cannot establish integrability; n3 proves the required bound directly.\n\nPille–Schneider 2209.04879v2 Remark 4.4 separates defining E1 over arbitrary fields from extending MA there. Field characteristic zero in that remark is not used to erase BFJ’s residue-characteristic restriction. Gubler–Rabinoff 2506.13548v2 explicitly leaves constructing MA outside its subject. Thuillier’s thesis supplies curve theory, without licensing a silent dimension-one restriction. Berkovich’s 1993 paper supplies analytic/cohomological background, not preservation of unbounded energy or MA under base change. The actual CLD 1204.6277v2 is the July 2025 revision; no application of its local-current theory to every global BFJ finite-energy target over arbitrary fields is established here.\n\nArtifacts: /workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo",
    "support": []
  },
  {
    "id": "n2",
    "summary": "Source-established arbitrary-support theorem over algebraically closed trivially valued characteristic-zero fields: smooth integral projective X, ample L, arbitrary dimension, genuine finite-energy MA, raw mass (L^n), finite dual energy and uniqueness modulo constants. Partial for original P16.6.",
    "detailedSummary": "Boucksom–Jonsson 1801.08229v4 constructs the approximation-independent genuine finite-energy operator and solves the equation for every positive Radon target of raw mass V=(L^n) and finite dual energy. No skeletal-support or toric-invariance hypothesis occurs. The proof supplies compactness, envelopes, finite-energy differentiation, continuity of integration, comparison and injectivity. This established trivial-field result does not automatically transfer to discrete or arbitrary fields.",
    "text": "Retain k algebraically closed, trivially valued and of characteristic zero; X/k smooth, connected, integral and projective, dimension n≥1 arbitrary; L ample; and the canonical trivial-field reference metric. Let V=(L^n)>0. Normalize intersection energy by E(0)=0 and E(u+c)=E(u)+c, and define E1={u psh:E(u)>−infinity}.\n\nThe exact target condition is positivity and Radon regularity, mu(Xan)=V, and raw dual energy sup_{a in model/FS tests}{V E(a)−integral a dmu}<infinity. For the entire probability nu=mu/V, this equals V Q(nu), where Q(nu)=sup_a{E(a)−integral a dnu}. No restriction of a target is renormalized. Constants make the raw supremum infinite at incorrect mass.\n\nThis theorem is already established in 1801.08229v4. Theorem 7.1 extends the genuine intersection pairing by majorants, uniquely and continuously along decreasing nets. Theorem 7.8 makes mixed pairings finite on E1. Theorem 7.18 tests this pairing against PL functions: positivity, mass V on constants, PL density and Riesz give a unique positive Radon MA measure. Proposition 7.19 verifies the model intersection formula and decreasing continuity. Therefore every decreasing model approximation gives the same genuine raw operator M(u), of mass V. No inverse measure construction is substituted.\n\nTheorem 5.20 supplies the envelope property under the retained hypotheses; Corollary 5.21 gives compact normalized PSH; Lemma 5.17 gives continuous envelopes. Theorem 8.5/Corollary 8.6 gives differentiation through the envelope, with derivative integral f d(M(u)/V). Theorem 9.20 identifies finite Q with integrability of every E1 potential. Proposition 9.19 proves L1(nu) continuity on bounded-energy sets.\n\nThe printed proof of Theorem 12.8 normalizes a maximizing sequence for E−integral against nu, bounds its energy by (9.11), extracts a psh subnet using compactness, and uses Proposition 9.19 and energy upper semicontinuity to prove actual attainment. Corollary 9.12 identifies its maximizer with the genuine MA solution. Conversely, concavity and integrability against its own MA give Q(M(u)/V)=E(u)−integral u d(M(u)/V)<infinity. Thus the range is exactly the stated raw-mass-V finite-dual-energy measures. Theorems 7.40 and 7.44 give locality and comparison; Proposition 12.7 gives injectivity modulo constants; Theorem 12.9 concludes existence and uniqueness.\n\nThere is no support restriction, torus action or dimension-one assumption. The application is written in P16.6-argument.md and standalone P16.6-paper.tex/P16.6-paper.pdf; rerun `python3 build_artifacts.py`. This is a source-established mathematical theorem, not a finite computation. It remains partial for original P16.6 because its trivial-field hypotheses are not transported to other fields by unproved base change or measure completeness.\n\nArtifacts: /workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n3",
    "summary": "Discrete residue-characteristic-zero deduction in arbitrary dimension: smooth geometrically integral projective X, ample L, every raw-mass-V finite-dual-energy target, genuine E1 MA, comparison and uniqueness. The proved test-to-E1 passage removes SNC support without function-field algebraizability. Partial for original P16.6.",
    "detailedSummary": "The proof combines BFJ’s genuine operator, compactness and envelopes with the supplied synthetic orthogonality and integral estimates. It proves classical envelope orthogonality, extends quantitative test estimates to finite-energy potentials, establishes L1 continuity against arbitrary finite-energy targets, obtains actual variational attainment, and differentiates through unbounded envelopes to solve the genuine equation. The exact raw mass is V=(L^n), and the measure condition is sup_{a in D_theta}{V E_theta(a)−integral a dmu}<infinity. A printed BFJ v1 sign slip is bypassed by a direct integrability proof. No general-field compactness or envelope theorem is inferred, and no novelty claim is made.",
    "text": "Retain K complete and nontrivially discretely valued with residue characteristic zero; X/K smooth, geometrically integral and projective, dimension n≥1 arbitrary; L ample; and a semipositive model reference with curvature theta. Field characteristic zero follows but does not replace the residue-characteristic hypothesis. No function-field algebraizability is imposed. Set V=(L^n)>0, M(u) the raw genuine MA and m(u)=M(u)/V. Model M is the intersection measure sum_E b_E(L_u|E)^n delta_{x_E}, of mass V. Use normalized energy E(u)=1/((n+1)V) sum_{j=0}^n integral u(theta+ddc u)^j theta^{n−j}, extended by decreasing majorants, and E1={psh u:E(u)>−infinity}.\n\nThe partial theorem is a bijection M:E1/R onto positive Radon measures mu with mu(Xan)=V and sup_{a in D_theta}{V E(a)−integral a dmu}<infinity. For the whole probability nu=mu/V, write Q(nu)=sup_a{E(a)−integral a dnu}. Constants force the raw mass. No toric, skeletal or dimension-one assumption occurs. This is a deduction from the source inputs in n1, not a claim that BFJ v1 Theorem A already stated it.\n\nBFJ v1 Theorem 3.1 constructs the bounded mixed operator from intersections. Locality defines M(u)=lim_{t→infinity}1_{u>−t}M(u_t), where u_t=max(u,−t), as an increasing limit on Borel sets. For u≤0 in E1, the bounded energy difference formula gives E(u_{t/2})−E(u_t)≥t m(u_t){u≤−t}/[2(n+1)]. Decreasing energy continuity makes the discarded mass o(1/t), hence M(u) has raw mass V. Lemma 6.8 gives |integral f dm(u_t)−integral f dm(u)|≤2(n+1)|E(u)| ||f||/t. Proposition 6.9 gives decreasing continuity on E1, and model-test density proves approximation independence. To apply the source’s unit-volume convention, lambda=V^(−1/n), theta_tilde=lambda theta and u_tilde=lambda u satisfy M_tilde(lambda u)=M(u)/V and E_tilde(lambda u)=lambda E(u); cones and truncations correspond. Proposition 6.11 supplies genuine finite-energy locality and comparison, integral_{u<v}M(v)≤integral_{u<v}M(u). Proposition 8.2 supplies uniqueness modulo constants without orthogonality or target support.\n\nThe actual PDF statement of Lemma 6.10 has a sign slip. The needed integrability follows directly: for finite-energy u,v≤0 and w=(u_t+v_s)/2, positivity and bounded energy give E((u+v)/2)≤E(w)≤integral w dm(w)/(n+1)≤2^(−n−1) integral v_s dm(u_t)/(n+1)≤2^(−n−1) integral_{u>−t}v_s dm(u)/(n+1). Here m(w)≥2^(−n)m(u_t), w≤v_s/2, and locality permits discarding a nonpositive integral. Let s and then t increase through integers. Since m(u) is carried by {u finite}, sequential monotone convergence yields integral v dm(u)≥(n+1)2^(n+1)E((u+v)/2)>−infinity. Concavity makes the lower bound finite; constants handle unnormalized potentials.\n\nReplace algebraizability-based orthogonality as follows. Synthetic Example 2.20/Definition 2.15 states lim_{a in D_theta,a<f} integral(f−a)dm(a)=0 for model f, using the directed pointwise order. BFJ 1201.0187v2 Theorem 8.3 makes P(f) continuous. Its decreasing model approximants converge uniformly by Dini; shifting them downward slightly makes them strictly below f. Consequently the entire increasing directed test net has supremum P(f) and converges uniformly. BE Theorem 8.4 passes genuine MA to the limit, yielding integral(f−P(f))dm(P(f))=0. Uniform model density, the 1-Lipschitz envelope property and continuous-MA convergence extend this to every continuous obstacle. This is precisely BFJ v1’s classical orthogonality hypothesis. Theorem 7.2/Corollary 7.3 now gives d/dt at zero E(P(u+tf))=integral f dm(u) for every u in E1 and continuous f, including unbounded u.\n\nFor arbitrary targets put m0=m(0), J(u)=integral u dm0−E(u), and r_nu(a)=Q(nu)−E(a)+integral a dnu. Synthetic (2.7) gives J(a)≤C_n(r_nu(a)+Q(nu)); its submean theorem gives sup u−integral u dm0≤T. Thus −E(u)≤J(u)+T on sup u=0. Finite Q implies integrability of every E1 potential against nu: decreasing model majorants a_alpha satisfy integral a_alpha dnu≥E(a_alpha)−Q, and the BFJ Radon/usc-net integration lemma passes this lower bound to u. Energy continuity proves Q=sup_{u in E1}(E(u)−integral u dnu). An unrestricted monotone-convergence theorem for arbitrary nets is not assumed.\n\nChoose maximizing model tau_j, so r_nu(tau_j)→0 and J(tau_j) is bounded. Synthetic Lemma 2.25(2.27), with the second test potential zero, gives |integral a(dnu−dm(tau_j))|≤C_R r_nu(tau_j)^(1/2) uniformly for model a with bounded J. Its original right side contains J(a,0)^(2^(−n)), comparable to a bounded power of J(a). For a in E1, decreasing model majorants have converging energies and m0-integrals, hence converging J. Their nu-integrals and m(tau_j)-integrals converge as well. Therefore the estimate extends uniformly to all E1 potentials with bounded J.\n\nIf u_i→u in BFJ’s psh topology and J(u_i) is bounded, lower semicontinuity of J makes u finite energy. For fixed j, m(tau_j) has finite divisorial support, so its integrals of u_i converge to that of u. The uniform estimate, then j→infinity, proves convergence of the nu-integrals. For L1 convergence use w_i=max(u_i,u). Supremums and m0-integrals are bounded on a convergent psh net; energies of u_i are bounded below; monotonicity bounds energies of w_i below, hence J(w_i) is bounded. Divisorial evaluations give w_i→u. Apply integral convergence to both nets and |u_i−u|=2w_i−u_i−u. This proves L1(nu) convergence, including for the compactness subnet below.\n\nNormalize a model maximizing sequence by subtracting its supremum. The bounds above control its J and energy. BFJ normalized-PSH compactness gives a subnet limit u; upper semicontinuity keeps u in E1. The proved L1 lemma yields E(u)−integral u dnu≥limsup(E(u_i)−integral u_i dnu)=Q(nu), hence equality. This is actual attainment. For continuous f, v_t=P(u+tf) lies in E1 because it dominates u−|t| ||f||, and remains below its usc obstacle. Maximality gives E(v_t)−E(u)≤integral(v_t−u)dnu≤t integral f dnu. Divide for both signs of t and use the finite-energy envelope derivative. Equality on all continuous tests gives m(u)=nu, therefore the genuine raw equation M(u)=mu.\n\nConversely, full mass, concavity and segment differentiation imply Q(m(u))=E(u)−integral u dm(u)<infinity; the directly proved integrability makes this finite, and decreasing approximation gives equality at the supremum. Thus the raw range is exact. Comparison and source Proposition 8.2 give uniqueness modulo constants. For a bounded model reference change theta'=theta+ddc h, transformed decreasing approximants prove M_theta'(u−h)=M_theta(u), E_theta'(u−h)=E_theta(u)−E_theta(h), and Q_theta'(nu)=Q_theta(nu)+integral h dnu−E_theta(h). Energy finiteness and the equation are reference-independent.\n\nThe dual condition is also equivalent here to E1⊂L1(nu). For the converse, integrability forces a uniform bound on −integral a dnu for normalized model tests J(a)≤1. Otherwise tests with integrals ≤−2^j give a decreasing convex series sum 2^(−j)a_j of energy ≥−(1+T), hence an E1 limit with integral minus infinity, a contradiction. Synthetic J(ta)≤C_n t^2J(a) then bounds −integral a dnu by A(1+sqrt(C_nJ(a))). Since E(a)≤−J(a), the dual supremum is finite.\n\nThe full proof and application checks are in P16.6-argument.md and standalone P16.6-paper.tex/P16.6-paper.pdf; rerun `python3 build_artifacts.py`. This is an unverified mathematical proof draft using explicitly applied source inputs, not a finite computation or conditional template. It remains partial for original P16.6: compactness and the continuous-envelope passages used here have not been supplied or proved over general nondiscrete fields.\n\nArtifacts: /workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo",
    "support": [
      "n1"
    ]
  },
  {
    "id": "n4",
    "summary": "Implementation deliverables are complete, including the partial proof, standalone paper, provenance, preserved inputs and two successful final TeX builds. General-field P16.6 remains unresolved; candidate=false. Execution and hashes do not certify mathematics.",
    "detailedSummary": "The result treats every admissible target independently at two field endpoints. Remaining obligations in the general complete-field setting are construction and full mass of genuine unbounded MA, potential compactness and envelopes or replacements, finite-energy differentiation, comparison and uniqueness, and attainment for every finite-dual-energy target. All requested artifacts and actual diagnostic streams are retained. Both final TeX builds exit zero, and all 21 artifact checks pass. status.json has exactly the required five keys.",
    "text": "The deliverables are P16.6-argument.md, standalone P16.6-paper.tex, and the 11-page P16.6-paper.pdf. The positive results are n2 and n3 under their exact retained hypotheses. They cover all admissible arbitrary-support measures in general dimension with genuine finite-energy MA, raw mass V=(L^n), finite dual energy, comparison and uniqueness. They are not declared a complete solution of original P16.6.\n\nFor general complete nontrivially valued, potentially nondiscrete fields, this work has not supplied an approximation-independent genuine unbounded mixed operator with full raw mass; normalized global psh compactness and envelope regularity or an effective replacement; finite-energy differentiation for that actual operator; locality, comparison and uniqueness there; or attainment for every raw-mass-V finite-dual-energy target. These are concrete missing passages, not impossibility claims. The trivial-field source makes potential completeness and surjectivity equivalent to an envelope property; synthetic measure completeness is a different assertion. Dense test images in a complete measure space do not alone realize limits by global psh potentials.\n\nNo reduction to one skeleton, retraction-factorization assertion, silent curve assumption, alternate inverse measure, or unproved preservation under base change, alterations, normalization or resolution was used. The other original geometric and characteristic atoms are not claimed solved.\n\ninput.json and input-original.json are byte-identical. assignment-original.txt and task-original.json preserve the decoded input. source-extracts/source-provenance.json records all ten source versions/hashes, literal proof extracts, fresh actual-PDF text, application checks and four rendered-PDF inspections. environment.json records tool details. status.json has exactly id,status,exact_result,proof_file,concrete_gaps and status partial. notes.json retains four canonical notes and candidate=false.\n\nRerun `python3 audit_sources.py > source-audit-output.txt 2>&1`, `python3 build_artifacts.py > build-output.txt 2>&1`, and `python3 verify_artifacts.py > verification-output.txt 2>&1`. Both final pdflatex passes exited zero. Actual stdout, stderr and TeX logs are retained in build/pass1 and build/pass2; build/build-report.json records commands, exit codes, hashes and warnings. The final second pass has only a cosmetic underfull-hbox warning and no overfull boxes. Initial failed builds caused by an undeclared mathscr command are preserved in build/failed-missing-mathscr; the final preamble declares the existing mathrsfs package. No software was installed.\n\nAll 21 artifact checks passed: input identity, decoded inputs, supplied and literal-extract hashes, ten successful PDF re-extractions, four inspection-image hashes, exact status schema, canonical local-note dependencies, false candidate, two successful final builds, retained diagnostic streams/logs, standalone TeX, final source/PDF identity and preserved failure diagnostics. checks.json and artifact-manifest.json retain this evidence. The final PDF SHA256 is 0d411f8dbb22d0d9aeead39a6a8b9de6e39de1f947678a273f981c040510eb2a.\n\nThese are finite artifact observations, not an exhaustive mathematical computation or proof checker. No heavy computation, compute-service job, network fetch, installation, other model, worker, subagent or external message was invoked. Compilation, execution and hashes do not establish mathematical correctness. Candidate=false because the full original atom remains unproved.\n\nArtifacts: /workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo",
    "support": [
      "n1",
      "n2",
      "n3"
    ]
  }
]

# Root read evidence limits

{
  "recorded_utc": "2026-10-04T16:56:36.917040+00:00",
  "round": 48,
  "atom": "P16.6",
  "entire_final_argument_root_read": true,
  "argument_LF_lines": 293,
  "all_actual_canonical_notes_all_fields_and_support_root_read": true,
  "canonical_note_count": 4,
  "actual_canonical_sha256": "5ccb42b1e7a4530de23f406d1f016a47171489c4567ab2a386be7a32fafc7e80",
  "entire_standalone_tex_root_read": true,
  "tex_LF_lines": 311,
  "argument_sha256": "036da349ea68d9d01067c46d3a6fc408169e6a4ef9cd60983fbf2cf6040b8c7c",
  "tex_sha256": "6600e95c3834074ecbb1c73930ddca92ece56f80972d5712086c0533fc8487f5",
  "all_three_author_helpers_full_read_before_root_reproduction": true,
  "author_source_application_checks_root_read": true,
  "new_exact_primary_checks": {
    "1201.0187v2_LF": [
      [
        1648,
        1766
      ],
      [
        1774,
        1845
      ],
      [
        1900,
        1955
      ]
    ],
    "1201.0188v1_LF": [
      [
        700,
        765
      ],
      [
        1190,
        1401
      ],
      [
        1402,
        1460
      ],
      [
        1540,
        1685
      ]
    ],
    "2307.01697v1_LF": [
      [
        677,
        753
      ],
      [
        800,
        923
      ],
      [
        1020,
        1054
      ],
      [
        1055,
        1245
      ]
    ],
    "actual_source_PDF_visual_pages": {
      "2307.01697v1": [
        25
      ],
      "1201.0188v1": [
        27,
        28
      ],
      "1801.08229v4": [
        122
      ]
    }
  },
  "published_background": "All ten application checks read; earlier source readings reused. Whole primary papers and every extracted unit are not asserted newly read.",
  "source_location_audit": "Author splitlines counts form feeds; 43 of 45 numeric ranges differ from LF interpretation. Author byte identity is preserved; 55 explicitly LF-delimited units supplied as an independent addendum.",
  "LF_addendum_sha256": "a975459046060ebad58aadd837fef06a1d342ad79e104b36e3eebdbc49d7ef73",
  "reproduction_sha256": "4dbf3aa39e4ed6dc8d1fe85ef2b7b722e09e18c2135396c32386ff83d592f0e9",
  "native_compile_result": "success",
  "native_open_performed": false,
  "current_open_P16_4_document_preserved": true,
  "fresh_PDF_visual_pages": [
    1,
    11
  ],
  "visual_limit": "First and last pages legible with no clipping; no whole-PDF visual claim.",
  "independent_mathematical_verdict": null,
  "original_atom_closed": false,
  "provider_review_submission_attempted": false,
  "original_scope_question": "Independently determine whether section 10.2 allows retained field hypotheses for the support axis. Do not import P16.4 automatically; do not discard section 10.3 residual wording."
}