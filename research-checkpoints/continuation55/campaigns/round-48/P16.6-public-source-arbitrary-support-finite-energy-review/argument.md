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

# Source identity, published background and application checks

{
  "key": "1201.0187",
  "supplied_pointer": {
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
  "actual_hashes": {
    "pdf": "8b684713055b9147de0d3379ad925c58f031bafe10a77e769a2791cdaa128270",
    "literal_extract": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
    "abstract_html": "983485b15a5da892c0b29ecb5ebb7280414028bd1333614a0ae8bf5ec888dbde"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true,
    "abstract_html": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/P16-arxiv-1201.0187-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/1201.0187-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "6a435578964be38cf1210362f6b7d15dd8e4c2851062bdb4d849fb8be2287415",
  "from_pdf_file": "source-extracts/1201.0187-from-pdf.txt",
  "from_pdf_header": "                                               SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN\n                                                                   GEOMETRY\n\n                                                        SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\narXiv:1201.0187v2 [math.AG] 21 Jan 2014\n\n\n\n\n                                                  Abstract. Let X be a smooth projective Berkovich space over a complete discrete val-\n                                                  uation field K of residue characteristic zero, endowed with an ample line bundle L. We\n                                                  introduce a general notion of (possibly singular) semipositive (or plurisubharmonic) met-\n                                                  rics on L, and prove the analogue of the following two basic results in the complex case:\n                                                  the set of semipositive metrics is compact modulo scaling, and each semipositive metric is\n                                                  a decreasing limit of smooth semipositive ones. In particular, for continuous metrics, our\n                                                  definition agrees with the one by S.-W. Zhang. The proofs use multiplier ideals and the\n                                                  construction of suitable models of X over the valuation ring of K, using toroidal techniques.\n\n\n\n\n                                                                                         Contents\n                                            Introduction                                                                                           1\n                                            1. Models of varieties over discrete valuation fields       ",
  "identity": "Boucksom--Favre--Jonsson, Singular semipositive metrics in non-Archimedean geometry, arXiv:1201.0187v2; banner 21 Jan 2014, internal date 22 Oct 2018.",
  "applications": [
    "Complete nontrivially discretely valued K, residue characteristic zero, smooth projective geometrically integral X, ample L satisfy the standing hypotheses. No function-field algebraizability is imposed here.",
    "Theorem 7.10 gives compact normalized PSH and continuity of divisorial evaluations; Theorem 8.3 gives continuous psh envelopes; Theorem B/8.7 gives decreasing model regularization. These apply only at this field endpoint."
  ],
  "limitations": [
    "Do not transport these inputs to a densely valued field or positive residue characteristic. Retractions are used for topology, not to restrict a target measure."
  ]
}

## Author source unit source-extracts/1201.0187-lines-88-101.txt

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



## Author source unit source-extracts/1201.0187-lines-150-194.txt



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


## Author source unit source-extracts/1201.0187-lines-1648-1766.txt

                                                   V                           W
and the result follows from Kleiman’s theorem (see e.g. [Laz, Theorem 1.4.9]) since µ∗ β is
nef.                                                                                     

          7. General θ-psh functions and semipositive singular metrics
  We are now ready to introduce the class of general θ-psh functions and their cousins:
semipositive singular metrics. The equicontinuity result in Corollary 6.2 will be used to
show Theorem A, asserting that the space of θ-psh functions is compact up to translation.
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


## Author source unit source-extracts/1201.0187-lines-1774-1823.txt

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

8.1. Regularity of envelopes. As a tool to prove our regularization theorem, we rely on
the following envelope construction, whose complex analogue is widely used.
Definition 8.1. The θ-psh envelope Pθ (u) of a continuous function u ∈ C 0 (X) is defined
by setting, for each x ∈ X.
                     Pθ (u)(x) := sup {ϕ(x) | ϕ ∈ PSH(X, θ), ϕ ≤ u on X} .
     Here are a few easy properties of the envelope operator.
Proposition 8.2. Let u, u0 ∈ C 0 (X).


## Author source unit source-extracts/1201.0187-lines-1894-1955.txt

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
there exists an θ-psh model function ψ such that ϕ ≤ ψ ≤ v + ε.
Proof. We may assume ϕ = Pθ (v), in which case the result follows from Theorem 8.3.              
            SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                      39



# Source identity, published background and application checks

{
  "key": "1201.0188",
  "supplied_pointer": {
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
  "actual_hashes": {
    "pdf": "4c29d91987477baf9baa4dfdd0b901ae1cd8910746012fd6285ab9a90bbf3f3a",
    "literal_extract": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
    "abstract_html": "e4683a68defd5887b5952cddcccc9f625a2d0391819a97f32a15d4d51f5409ae"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true,
    "abstract_html": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/P16-arxiv-1201.0188-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/1201.0188-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "d31b3525783a11b73faaf926a74d8888847d5def808011d24e2661c2f9d31d39",
  "from_pdf_file": "source-extracts/1201.0188-from-pdf.txt",
  "from_pdf_header": "                                          SOLUTION TO A NON-ARCHIMEDEAN MONGE-AMPÈRE EQUATION\n\n                                                      SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON\narXiv:1201.0188v1 [math.AG] 30 Dec 2011\n\n\n\n\n                                                Abstract. Let X be a smooth projective Berkovich space over a complete discrete valu-\n                                                ation ﬁeld K of residue characteristic zero, and assume that X is deﬁned over a function\n                                                ﬁeld admitting K as a completion. Let further µ be a positive measure on X and L be\n                                                an ample line bundle such that the mass of µ is equal to the degree of L. Then we show\n                                                the existence a continuous semipositive metric whose associated measure is equal to µ in\n                                                the sense of Zhang and Chambert-Loir. This we do under a technical assumption on the\n                                                support of µ, which is, for instance, fulﬁlled if the support is a ﬁnite set of divisorial points.\n                                                Our method draws on analogues of the variational approach developed to solve complex\n                                                Monge-Ampère equations on compact Kähler manifolds by Berman, Guedj, Zeriahi and the\n                                                ﬁrst named author, and of Kolodziej’s C 0 -estimates. It relies in a crucial way on the com-\n                                                pactness properties of singular semipositive metrics, as deﬁned and studied in a companion\n                                               ",
  "identity": "Boucksom--Favre--Jonsson, Solution to a non-Archimedean Monge-Ampere equation, actual arXiv:1201.0188v1; banner 30 Dec 2011, internal date 29 Oct 2018.",
  "applications": [
    "Theorem A requires smooth projective X, complete discrete K with residue characteristic zero, extra function-field algebraizability, and target supported on one SNC dual complex. We do not cite it for arbitrary targets.",
    "Sections 2--7 construct the genuine bounded and E1 operators for the discrete residue-zero smooth projective setting: Theorem 3.1, Definition 6.4, Lemmas 6.7--6.8, Propositions 6.9, 6.11--6.12. These do not require target support or algebraizability.",
    "Proposition 8.2 gives E1 uniqueness without orthogonality. Corollary 7.3 requires orthogonality, supplied separately by the proved transfer from the synthetic source."
  ],
  "limitations": [
    "Later versions are not in this packet. The actual PDF statement of Lemma 6.10 has a positive integral of -psi, whereas its proof uses psi. Its displayed bound alone does not show integrability; manuscript (7a)--(7b) prove the needed negative-integral bound directly. Other unused printed/OCR slips are not imported."
  ]
}

## Author source unit source-extracts/1201.0188-lines-60-102.txt

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


## Author source unit source-extracts/1201.0188-lines-700-753.txt

Choose a common determination X of ϕ and all the θi . By continuity, we may assume
ϕ = ϕD for some D ∈ Div0 (X )Q , and each form θi is determined by a Q-line bundle Li on
X . Then I = D 2 · L1 · . . . · Ln−1 and the result follows from [YZ10, Theorem 2.1.1 (a)]. 
Remark 2.22. In the complex case we have by Stokes’ theorem
             Z                               Z
                f ddc g ∧ θ1 ∧ ... ∧ θn−1 = − df ∧ dc g ∧ θ1 ∧ ... ∧ θn−1 ,

and negativity comes from that of the (1, 1)-form df ∧ dc f . Recall also that df ∧ dc f ∧ ω n−1 =
                                                 R                  1/2
|df |2ω ω n when ω is a Kähler form, so that − f ddc f ∧ ω n−1          is the L2 -norm of the
gradient of f .
2.8. Radon measures and convergence results. We shall make frequent use of basic
integration and measure theory. Let X be a compact (Hausdorﬀ) space. A Radon measure
on X is a positive linear functional µ : C 0 (X) → R. With this deﬁnition, it follows from the
Riesz representation theorem that Radon measures are in 1-1 correspondence with regular
Borel measures on X; see [Fol99, §7.1–2].
   Since we shall be dealing with (possibly uncountable) nets rather than sequences, one has
to be careful using results from integration theory. For example, the monotone convergence
theorem is of course not true for general nets. However, as the next results show, integration
of semicontinuous functions against Radon measures is often well behaved.
Lemma 2.23. [Fol99, Proposition 7.12]. If µ is a positive Radon measure on X and (fj )j
a decreasing
     R       Rnet of usc functions on X, converging pointwise to a (usc) function f , then
limj fj µ = f µ.
  In particular, one has
16                   SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

Lemma 2.24. [Fol99, Corollary 7.13]. If µ is a positive Radon measure on X and f is a
usc function on X, then
                        Z           Z                      
                                                        0
                          f µ = inf    gµ | f ≤ g, g ∈ C (X)

Corollary 2.25. Let (fj )j a decreasing net of usc functions on X converging pointwise to
a (usc) function f , and (µj )j a net of positive Radon measures on X converging weakly to
a positive Radon measure µ. Then
                                           Z         Z
                                   lim sup fj µj ≤ f µ.
                                                    j
                                 R
Proof. Upon replacing µj with ( µj )−1 µj we may assume that the µj ’s are probability
measures. RFix anyR ε > 0. By Lemma 2.24 there exists a continuous function g ≥ f on X
such that gµ < f µ + ε. By Dini’s lemma, we have fj < g + ε for all j ≫ 1, hence
                       Z              Z           Z           Z
               lim sup fj µj ≤ lim sup gµj + ε = gµ + ε ≤ f µ + 2ε.
                           j                    j
         R           R
since        gµj →       gµ by the deﬁnition of weak convergence. The result follows.                               

                         3. Monge-Ampère operator on bounded functions
  From now on we ﬁx a form θ ∈ Z 1,1 (X) whose de Rham class {θ} ∈ N 1 (X) is ample.
In the next three sections we shall develop some of the Bedford-Taylor theory in our non-
Archimedean setting.


## Author source unit source-extracts/1201.0188-lines-1190-1411.txt

           1 be a decreasing net of ω-psh model functions converging to ϕ. Write Ωj :=
{ϕj > ψ}. This is an open set. Set u := max{0, ϕ − ψ}. Then
                                                    \
                               {ϕ > ψ} = {u > 0} ⊆     Ωj .
                                                          j

By what precedes, MA(max{ϕj , ψ}) = MA(ϕj ) on Ωj . Moreover max{ϕj , ψ} decreases to
max{ϕ, ψ} and so the measure MA(max{ϕj , ψ}) converges weakly to MA(max{ϕ, ψ}). Let
f be a continuous function on X. By Proposition 4.3 ϕ, ψ are quasicontinuous. It follows
that u and f u are also quasicontinuous, and applying Lemma 5.4 twice we get that
Z                             Z                            Z               Z
   f u MA(max{ϕ, ψ}) = lim       f u MA(max{ϕj , ψ}) = lim   f u MA(ϕj ) = f u MA(ϕ).
                         j→∞                                  j→∞

This holds for every f ∈ C 0 (X), so 1{ϕ>ψ} MA(max{ϕ, ψ}) = 1{ϕ>ψ} MA(ϕ), as was to be
shown.                                                                              

                                        6. Energy
   Let ω be a form as in §4 with {ω}n = 1. As in the complex case, it turns out that the non-
Archimedean Monge-Ampère operator admits a primitive, i.e. a functional whose directional
derivatives at a given ϕ are given by integration against MA(ϕ). Adapting [GZ07, BEGZ10]
to our case we introduce and study this functional, as well as the resulting class of ω-psh
functions of ﬁnite energy. While such functions are unbounded in general, they behave from
many points of view like bounded ω-psh functions.

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


## Author source unit source-extracts/1201.0188-lines-1412-1460.txt

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


## Author source unit source-extracts/1201.0188-lines-1544-1685.txt

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


# Source identity, published background and application checks

{
  "key": "1805.01016",
  "supplied_pointer": {
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
  "actual_hashes": {
    "pdf": "51d02f75a65aa463f8e22393933f5ebef9036e322d720fc632f87759c2b71cb2",
    "literal_extract": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
    "abstract_html": "d15154ca2fe8e5e1942e16f2d77a8221dffc5162ddfa3c4bd0544c8d6f1b9a1a"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true,
    "abstract_html": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/P16-arxiv-1805.01016-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/1805.01016-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "8e584521fe3d41f179bef93d14315414ac7796532c65518c1861717416f99233",
  "from_pdf_file": "source-extracts/1805.01016-from-pdf.txt",
  "from_pdf_header": "                                              SPACES OF NORMS, DETERMINANT OF COHOMOLOGY AND\n                                                 FEKETE POINTS IN NON-ARCHIMEDEAN GEOMETRY\n\n                                                                  SÉBASTIEN BOUCKSOM AND DENNIS ERIKSSON\narXiv:1805.01016v3 [math.AG] 8 Jan 2021\n\n\n\n\n                                                 Abstract. Let L be an ample line bundle on a (geometrically reduced) projective variety\n                                                 X over any complete valued field. Our main result describes the leading asymptotics of\n                                                 the determinant of cohomology of large powers of L, with respect to the supnorm of a\n                                                 continuous metric on the Berkovich analytification of L. As a consequence, we establish\n                                                 in this setting the existence of transfinite diameters and equidistribution of Fekete points,\n                                                 following a strategy going back to Berman, Witt Nyström and the first author for complex\n                                                 manifolds. In the non-Archimedean case, our approach relies on a version of the Knudsen–\n                                                 Mumford expansion for the determinant of cohomology on models over the (possibly non-\n                                                 Noetherian) valuation ring, as a replacement for the asymptotic expansion of Bergman\n                                                 kernels in the complex case, and on the reduced fiber theorem, as a replacement for the\n                                                 Bernstein–Markov inequalities. Along the way, ",
  "identity": "Boucksom--Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry, actual arXiv:1805.01016v3.",
  "applications": [
    "Theorem 8.4 provides the uniform-continuous extension of genuine mixed MA to continuous psh metrics; smooth projective geometrically integral X and ample L are within its domain.",
    "Corollary B is conditional on continuity of envelopes. It is not an unbounded E1 surjectivity theorem."
  ],
  "limitations": [
    "This is not a paper with a different pluripotential title. No general finite-energy equation theorem is inferred from its continuous operator."
  ]
}

## Author source unit source-extracts/1805.01016-lines-125-170.txt

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


## Author source unit source-extracts/1805.01016-lines-2281-2308.txt

   Choose a common non-Archimedean extension F ′ of both K ′ and F , and note that (k ·
kmφ )F ′ = (k · kmφK ′ )F ′ . By Proposition 1.25 and the triangle inequality, we get
                   d∞ ((k · kmφ )F , k · kmφF ) = d∞ ((k · kmφ )F ′ , (k · kmφF )F ′ )
                                                                      
                              = d∞ (k · kmφK ′ )F ′ , (k · kmφF )F ′
                                                                                     
                 ≤ d∞ k · kmφK ′ )F ′ , k · kmφF ′ + d∞ k · kmφF ′ , (k · kmφF )F ′ ,
which is o(m) by the first part of the proof applied to the nontrivially valued fields F and
K ′.
   Assume finally that both K and F are trivially valued, and chose a nontrivially valued
extension F ′ of F . We similarly get
                   d∞ (k · kmφF , (k · kmφ )F ) = d∞ ((k · kmφF )F ′ , (k · kmφ )F ′ )
                                                                                     
                  ≤ d∞ (k · kmφF )F ′ , k · kmφF ′ + d∞ k · kmφF ′ , (k · kmφ )F ′
Since F ′ is nontrivially valued, the previous step shows that the last two terms are o(m),
and we are done.                                                                         

                      7. Plurisubharmonic metrics and envelopes
   Following [BFJ16, BJ18a], we introduce a general notion of plurisubharmonic metric, and
compare it with other existing notions. In what follows, X denotes a projective scheme over
a complete valued field K.
7.1. Plurisubharmonic metrics. Assume first that K is Archimedean (the case K =
R merely consisting in working with conjugation-invariant objects). A (possibly singular)
metric φ on a line bundle L is plurisubharmonic (psh for short) if, for each local trivialization
τ of L, the function − log |τ |φ is psh, i.e. locally the restriction of a psh function in a polydisc.
Note that φ is psh iff its pullback to Lred is psh. For any m ≥ 1, φ is psh iff mφ is psh, and
psh metrics thus make sense on Q-line bundles.
Theorem 7.1. Assume that K is Archimedean, and let L be a semiample Q-line bundle.


## Author source unit source-extracts/1805.01016-lines-2550-2586.txt

Definition 7.24. Let φ be a bounded metric on L.
   (i) The psh envelope of φ is defined as the pointwise upper envelope
                              P(φ) := sup{ψ ∈ PSH(L) | ψ ≤ φ}.                            (7.3)
     (ii) The regular psh envelope of φ is
                              Q(φ) := sup{ψ ∈ FS(L) | ψ ≤ φ}.                             (7.4)
  Since any continuous psh metric on L is a uniform limit of Fubini–Study metrics, it would
be equivalent to require ψ continuous and psh in (ii). Trivially, Q(φ) is lsc, Q(φ) ≤ P(φ) ≤ φ,
and the operators P and Q are monotone increasing and 1-Lipschitz with respect to the
supnorm. They are related as follows.
Proposition 7.25. For any bounded metric φ on L we have Q(φ) = P(φ⋆ ), with φ⋆ ≤ φ
denoting the lsc regularization of φ.
               NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                          53

Proof. A continuous metric ψ satisfies ψ ≤ φ iff ψ ≤ φ⋆ , and hence Q(φ) = Q(φ⋆ ). We may
thus assume from the start that φ is lsc, and we then need to show that any psh metric ψ on
L such that ψ ≤ φ satisfies ψ ≤ Q(φ). By Definition 7.2, there exists a decreasing net (ψj )
of Fubini–Study metrics on L with ψj → φ. Pick ε > 0. By lower semicontinuity of φ − ψj
and a simple compactness argument (Dini’s lemma), we thus have ψj ≤ φ + ε on X an for j
large enough. Thus ψj ≤ Q(φ) + ε, and hence ψ ≤ Q(φ) + ε, which yields the result.        
  To L we attach the semigroup
                N(L) = {m ∈ N | mL is a globally generated line bundle} .
Theorem 7.26. For any bounded metric φ on L we have
                                      lim      m−1 FS(mφ) = Q(φ),                       (7.5)
                                 N(L)∋m, m→∞

and the convergence is uniform iff Q(φ) is continuous.
Proof. Pick m, m′ ∈ N(L). For any two s ∈ H0 (mLred ), s′ ∈ H0 (m′ Lred ), we have
                                  ks · s′ k(m+m′ )φ ≤ kskmφ ks′ km′ φ .                 (7.6)
This implies FS((m + m′ )φ) ≥ FS(mφ) + FS(m′ φ), and hence
                           lim       m−1 FS(mφ) =          sup     m−1 FS(mφ),
                    N(L)∋m, m→∞                         m∈N(L)>0

by Fekete’s lemma. For each m ∈ N(L)>0           , m−1 FS(mφ) is continuous and psh, by Theo-
rem 7.16. By Lemma 7.23, m−1 FS(mφ) ≤ φ, and hence m−1 FS(mφ) ≤ Q(φ), which proves
that
                              sup m−1 FS(mφ) ≤ Q(φ).


## Author source unit source-extracts/1805.01016-lines-2611-2761.txt

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
a semiample Q-line bundle L over X. Pick a complete field extension F/K, and denote φF
the pullback of φ to LF . Then φ is psh iff φF is psh.
Proof. By definition, the pullback of a Fubini–Study metric on L is a Fubini–Study metric on
LF , and hence φ psh implies φF psh. Assume conversely that φF is psh. By Theorem 7.26,
                                      εm := sup m−1 FS(mφF ) − φF
                                            an
                                           XF

tends to 0 as m ∈ N(L) tends to ∞; we need to show that φm := m−1 FS(mφ) converges
uniformly to φ. By Lemma 7.20, we have
                                                       
                            (φm )F = m−1 FS (k · kmφ )F .
Thus
                sup |φm − φ| = sup |(φm )F − φF | ≤ sup (φm )F − m−1 FS(mφF ) + εm
                X an             an
                                XF                    an
                                                     XF
          −1
                                  
     =m        sup FS (k · kmφ )F − FS (k · kmφF ) + εm ≤ m−1 d∞ (k · kmφF , (k · kmφ )F ) + εm ,
                an
               XF
                 NORMS, DETERMINANT OF COHOMOLOGY AND FEKETE POINTS                               55

by (7.1). By Theorem 6.6, m−1 d∞ (k · kmφF , (k · kmφ )F ) → 0, and are done.                     

Part 3. Asymptotics of relative volumes
                  8. Monge–Ampère measures and Deligne pairings
   In this section, we review some basic properties of Monge–Ampère operators, and use them
to define metrics on Deligne pairings (Theorem 8.16), following Deligne’s program [Del87].
In what follows, X is as before an n-dimensional projective scheme over a complete valued
field K.
8.1. Mixed Monge–Ampère measures. The (algebraic) fundamental class of X is the
n-dimensional cycle               X
                            [X] =   mα [Xα ],
                                                     α
where the Xα denote the n-dimensional irreducible components of X (with their reduced
structure) and mα is the length of the local ring of X at the generic point of Xα . The
intersection number of Q-line bundles L1 , . . . , Ln on X is defined as
                      (L1 · . . . · Ln ) := deg π⋆ (c1 (L1 ) · . . . · c1 (Ln ) · [X]) ,
with π : X → Spec K the structure morphism.
  Now let φ1 , . . . , φn be smooth metrics on L1 , . . . , Ln , and recall that ddc φi denotes the
curvature form of φi , a smooth, closed (1, 1)-form on X an (cf. [CLD12, §6.4.1] for the non-
Archimedean case). The smooth (n, n)-form ddc φ1 ∧. . .∧ddc φn determines a Radon measure
                                               X
                ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα             (8.1)
                                       α
                          an
on the topological space X , the mixed Monge–Ampère measure     of the φi , with δX =
P
  α m  δ
      α Xα denoting the analytic fundamental class of X (see [CLD12,  §3.7] for the non-
Archimedean case).
Remark 8.1. When K = R, we define ddc φ1 ∧ . . . ∧ ddc φn ∧ δX as the image of the
corresponding measure on X(C) = XCan by the projection map XCan → X an .
Example 8.2. Assume that n = 0, i.e. X = Spec A with A a finite K-algebra. The pre-
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



# Source identity, published background and application checks

{
  "key": "1801.08229",
  "supplied_pointer": {
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
  "actual_hashes": {
    "pdf": "8d5975337f4ac88a475929ea6a436ec4a15d08715d5582bc0ba0eb3e07152c52",
    "literal_extract": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
    "abstract_html": "680fc70f252a7203bf277dccb65c9fddf4f0725c387d2b41b64d467f087c2304"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true,
    "abstract_html": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/P16-arxiv-1801.08229-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/1801.08229-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "659bb8d2e5335781041f03cdb168bac70126487bc0db394f3dac8cf1e9f076d0",
  "from_pdf_file": "source-extracts/1801.08229-from-pdf.txt",
  "from_pdf_header": "                                           GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED\n                                                                   FIELD\n\n                                                                   SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\narXiv:1801.08229v4 [math.AG] 22 Mar 2022\n\n\n\n\n                                                  Dedicated to Ahmed Zeriahi for all his contributions to complex analysis and geometry\n\n\n                                                Abstract. We develop global pluripotential theory in the setting of Berkovich geometry\n                                                over a trivially valued field. Specifically, we define and study functions and measures of\n                                                finite energy and the non-Archimedean Monge–Ampère operator on any (possibly reducible)\n                                                projective variety. We also investigate the topology of the space of valuations of linear\n                                                growth, and the behavior of psh functions thereon.\n                                                   Nous développons une théorie du pluripotentiel global dans le contexte de la géométrie de\n                                                Berkovich sur un corps trivialement valué. Plus précisément, nous définissons et étudions\n                                                des fonctions et mesures d’énergie finie et un opérateur de Monge–Ampère non-archimédien\n                                                sur toute variéte projective (éventuellement réductible). Nous explorons également la topolo-\n                                                gie de l’espace des valuations à croissance linéaire, et le comport",
  "identity": "Boucksom--Jonsson, Global pluripotential theory over a trivially valued field, arXiv:1801.08229v4.",
  "applications": [
    "Algebraically closed trivially valued k of characteristic zero, smooth connected integral projective X of arbitrary dimension, ample L meet Theorems 5.20 and 12.9.",
    "Theorems 7.1, 7.18 and Proposition 7.19 construct the genuine finite-energy operator by the intersection pairing, with mass V before probability normalization.",
    "Theorem 8.5/Corollary 8.6, Proposition 9.19, and the printed proof of Theorem 12.8 give energy differentiation, L1 continuity on bounded-energy sets, and attainment; Theorems 7.40 and 7.44 give locality/comparison.",
    "Theorem 9.20 identifies finite dual energy with integrability of every E1 potential at this endpoint."
  ],
  "limitations": [
    "The trivial-field theorem is not transferred by unproved base change to the discrete or arbitrary-field settings. The characteristic-p dimension-at-most-two extension in its statement is not used."
  ]
}

## Author source unit source-extracts/1801.08229-lines-102-206.txt

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
which itself is a version of the celebrated result of Yau [Yau78] and a later version by
Kolodziej [Kol98]. In the non-Archimedean setting, earlier results include [Liu11, BFJ15,
YZ17].


## Author source unit source-extracts/1801.08229-lines-2797-2828.txt

  Replacing ϕi by exp(ϕi − supj supX an ϕj ) − 1, see Corollary 4.11, we may also assume
−1 ≤ ϕi ≤ 0.
  Any subset of a negligible set is trivially negligible. We also have
Lemma 5.2. A countable union of negligible sets is negligible.
Proof. Let (Em )∞
                                                                  S
                1 be a sequence of negligible sets, and set E :=    Em . Fix ω ∈ Amp(X).
For each m we can find a family (ϕm,i )i∈Im in PSH(ω) such that  −1 ≤ ϕm,i ≤ 0 on X an and
        ?
                                                            Q
ϕm < Pϕm on Em , where ϕm = supi∈Im ϕm,i . Now set I = m Im P      and, for i = (im )m ∈ I,
ψi = ∞  m=1 2 −m ϕ
                  m,i m . Then ψi ∈ PSH(ω)    and ψ  := sup i ψi =   m2
                                                                        −m ϕ . This gives
                                                                             m
      ?
ψ < ψ on E, so E is negligible.                                                          
Proposition 5.3. Every pluripolar subset is negligible.
  The converse implication is much more subtle. We will prove it when char k = 0 or
dim X ≤ 2, see Corollary 13.18 below.
Proof. Suppose E ⊂ X an is pluripolar, and pick ψ ∈ PSH(ω) such that ψ ≤ 0 and ψ = −∞
on E. We may assume E = {ψ = −∞}. For m ≥ 1, set ϕm := m−1 ψ ∈ PSH(ω) and
ϕ := supm ϕm . Then ϕ ≡ −∞ on E and ϕ ≡ 0 on X an \ E. Since E has empty interior (see
Corollary 4.39), ϕ? ≡ 0 on X an , and E = {ϕ < ϕ? } is thus negligible.             
     Just like pluripolar sets, the class of negligible sets is birationally invariant.
Lemma 5.4. If π : Y → X is a birational morphism, then a subset E ⊂ X an is negligible
iff π −1 (E) ⊂ Y an is negligible.
Proof. We follow the setup and notation of the proof of Lemma 4.40.
  First suppose E is negligible, and pick a family (ϕi )i in PSH(ωX ) uniformly bounded
above such that supi ϕi < sup?i ϕi on E. If we set ψi := π ? ϕi , then (ψi )i is a family in
PSH(π ? ωX ) that is uniformly bounded above. Moreover, supi ψi < sup?i ψi on π −1 (E) \ W an ,
so π −1 (E) \ W an is negligible. As W an is pluripolar, and hence also negligible, it follows


## Author source unit source-extracts/1801.08229-lines-2894-2928.txt

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
unibranch.
  The analogue of this result is known in the complex analytic setting, too. We have not
been able to locate a precise reference, but the proof below of Theorem 5.12 can easily be
adapted to that setting.
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     59

Lemma 5.13. Let π : Y → X be a birational morphism. Pick θ ∈ N1 (X), and assume that
θ can be written as the limit of a sequence of classes θm > θ with the envelope property.


## Author source unit source-extracts/1801.08229-lines-2977-3064.txt

when ϕ, ϕ0 are bounded.
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
Lemma 5.19. Suppose ϕ : X an → R ∪ {+∞} is bounded below, with lsc regularization
ϕ? : X an → R ∪ {+∞}. Then:
     (i) Qω (ϕ) = Pω (ϕ? );
    (ii) Qω (ϕ) ∈ C0 (X) ⇐⇒ Qω (ϕ) ∈ PSH(ω);
   (iii) if ϕ is the pointwise limit of an increasing net (ϕj ) of bounded-below, lsc functions
         (and hence ϕ is lsc), then Pω (ϕj ) % Pω (ϕ).
Proof. A function ψ ∈ CPSH(ω) satisfies ψ ≤ ϕ iff ψ ≤ ϕ? . Thus Qω (ϕ) = Qω (ϕ? ), and we
may therefore assume wlog that ϕ is lsc. Trivially, Pω (ϕ) ≥ Qω (ϕ). Pick ψ ∈ PSH(ω) such
that ψ ≤ ϕ, and let (ψi ) be a decreasing net in CPSH(ω) converging pointwise to ψ. For
each ε > 0 and v ∈ X an , we can find i such that {ψi < ϕ + ε} is an open neighborhood of
v, by lower semicontinuity of ϕ − ψi . By compactness of X an , it follows that ψi < ϕ + ε for
all i large enough. Thus ψ ≤ ψi ≤ Qω (ϕ + ε) = Qω (ϕ) + ε, which proves (i).
   As noted above, Qω (ϕ) is lsc and bounded below. If Qω (ϕ) is ω-psh, then it is in particular
usc, and hence Qω (ϕ) ∈ C0 (X). Assume, conversely, that Qω (ϕ) ∈ C0 (X). Since CPSH(ω)
is stable under finite maxima, Qω (ϕ) is the pointwise limit of an increasing net (ψi ) in
CPSH(ω). By Dini’s lemma, ψi → Qω (ϕ) uniformly on X an , and hence Qω (ϕ) ∈ PSH(ω),
by Theorem 4.7. This proves (ii).
   Consider finally a net (ϕj ) as in (iii). We trivially have limj Pω (ϕj ) = supj Pω (ϕj ) ≤
Pω (ϕ). Pick ε > 0 and ψ ∈ CPSH(ω) such that ψ ≤ ϕ. As above, for all j large enough
we have ψ ≤ ϕj + ε, and hence ψ ≤ Pω (ϕj ) + ε. Thus Pω (ϕ) ≤ supj Pω (ϕj ), and we are
done.                                                                                         

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
vertical ideal of X for all m 

## Author source unit source-extracts/1801.08229-lines-3650-3717.txt

             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                       73

6.5. Nef b-divisors and homogeneous psh functions. We finally consider general nef
b-divisors, and describe these in terms of homogeneous psh functions. In this section, we
assume that X is smooth and k has characteristic zero.
   If Y , Y 0 are smooth models of X and Y 0 dominates Y , then the corresponding birational
morphism µ : Y 0 → Y induces a linear map µ? : N1 (Y 0 ) → N1 (Y ). The space of b-divisor
classes is defined as
                                    N1b (X) := lim N1 (Y )
                                               ←−
                                                 Y
with Y running over all smooth models of X, endowed with the projective limit topology
(see [BFJ09, BdFF12, DF20]). Each B ∈ Z1b (X)R determines a class [B] ∈ N1b (X).
Definition 6.38. We say that a (real) b-divisor B ∈ Z1b (X)R is exceptional if BX = 0.
   The map B 7→ ψB sets up a linear isomorphism between the space of exceptional b-
divisors and the space E of all homogeneous functions ψ : X div → R such that ψ(ordE ) = 0
for all prime divisors E ⊂ X. We equip the R-vector space E with the topology of pointwise
convergence.
   By the negativity lemma, the map B 7→ [B] is injective on exceptional b-divisors. For
any α ∈ N1b (X), we can thus find a unique exceptional b-divisor Bα ∈ Z1b (X)R such that
[(Bα )Y ] = αY − π ? αX for all smooth models π : Y → X (see [BdFF12, Lemma 1.11]). We
denote by ψα := ψBα ∈ E the corresponding homogeneous function. As a consequence
of [BdFF12, Lemma 1.12], we can now state:
Lemma 6.39. The map α 7→ (αX , ψα ) defines a topological vector space isomorphism
                                            ∼
                                    N1b (X) → N1 (X) × E.                                  (6.4)
  As recalled above, one says that a Cartier b-divisor B ∈ Carb (X) is nef if BY is nef for
some (or, equivalently, any) determination Y . The set
                                      Nefb (X) ⊂ N1b (X)
of nef b-divisor classes is defined as the closure of the set of nef Cartier b-divisor classes.
Thus a class α ∈ N1b (X) is nef iff there exists a net (Bi ) of nef Cartier b-divisors such that
[Bi,Y ] → αY for all smooth models Y → X. Since Nef(Y ) is a closed convex cone for each
model Y , it is not hard to see that Nefb (X) is a closed convex cone.
   By [BdFF12, Lemma 2.12], a class α ∈ N1b (X) is nef iff, for each smooth model Y ,
αY ∈ N1 (Y ) is nef in codimension one. A typical example is provided by the ‘positive part’
in the divisorial Zariski decomposition of a Cartier b-divisor [Bou04, Nak04, BFJ09].
   As we next show, nef b-divisor classes admit a precise description as homogeneous psh
functions.
Theorem 6.40. The isomorphism (6.4) maps Nefb (X) onto the set of pairs (θ, ψ) with
θ ∈ N1 (X) and ψ ∈ PSHhom (θ) such that ψ(ordE ) = 0 for all prime divisors E ⊂ X.
  As a consequence of Theorem 6.40, we recover the monotone approximation result of [DF20].
Corollary 6.41. For any α ∈ Nefb (X), there exists a decreasing net (Bi ) of nef Cartier
b-divisors such that [Bi ] → α in N1b (X).
  By Remark 6.18, the result is actually valid with a sequence instead of a net, as in [DF20,
Theorem A].
74                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Remark 6.42. Both [DF20, Theorem A] and Corollary 6.41 ultimately rely on the multi-
plier ideals technique that goes back to [ELS03], and was already used in a similar manner
in [BFJ16, Theorem 8.5]. However, the proof of [DF20] is much more direct, and the main
interest of the present discussion lies rather in Theorem 6.40.
Proof of Theorem 6.40. Assume first that α = [B] for a nef Cartier b-divisor B, and pick
a determination π : Y → X of B. Then ψα ∈ PLhom (X) is the function associated to the
Q-Cartier b-divisor determined on Y by the π-exceptional divisor EY := BY − π ? BX , and
                                      π ? θ + [EY ] = [BY ]
is nef. By Theorem 6.35, we thus have ψα ∈ PSHhom (αX ).
   Consider next any α ∈ Nefb (X). By assumption, there exists a net (Bi ) of nef b-divisors
such that αi := [Bi ] → α in N1b (X), i.e. θi := (αi )X → θ and ψαi → ψα pointwise on X div (see
Lemma 6.39). For any ample class ω, we have θ + ω − θi ∈ Amp(X) for i large enough, and
hence ψαi ∈ PSHhom (θi ) ⊂ PSHhom (θ + ω). By Corollary 6.22, the latter space is compact,
and we may thus assume, after passing to a subnet, that ψαi → ψ ∈ PSHhom (θ + ω). Since
ψαi → ψα on X div , it follows that ψα ∈ PSHhom (θ + ω), and hence ψα ∈ PSHhom (θ), since
this holds for all ω ∈ Amp(X) (see Theorem 4.5).
   Conversely, pick ψ ∈ PSHhom (θ) such that ψ(ordE ) = 0 for all prime divisors E ⊂ X.
Its restriction to X div determines an element B ∈ Z1b (X)R such that ψB = ψ. We define
α ∈ N1b (X) by setting αY := π ? θ + [BY ] for all smooth models π : Y → X, and we claim


## Author source unit source-extracts/1801.08229-lines-3977-4067.txt

Proof of Theorem 7.8. Properties (i)–(iii) follow from Proposition 7.7, while (iv), (v) and (vi),
respectively, follow from Lemmas 7.9, 7.10 and Corollary 7.11. Finally, (vii) follows from (7.10).
                                                                                              
  It will be convenient to extend the energy pairing to a multilinear map. Recall that any
ω-psh function is finite-valued on X lin , see Corollary 4.17. We now introduce
Definition 7.12. We define a function of finite energy as a function ϕ : X lin → R of the
form ϕ = ϕ+ − ϕ− with ϕ± ∈ E 1 (ω) for some ω ∈ Amp(X).
   By Theorem 7.8, ω∈Amp(X) E 1 (ω) forms a convex cone in the R-linear space of all func-
                      S

tions ϕ : X lin → R, and the set
                                           E~1 = E~1 (X)
of functions of finite energy thus forms an R-vector space, which contains PL(X)R , by (3.2).
Note further that E~1 is generated by E 1 (ω) for any given ω ∈ Amp(X), by Theorem 7.8 (iv),
(v).
80                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON


Lemma 7.13. For each ω ∈ Amp(X), we have E 1 (ω) = E~1 ∩ PSH(ω).
   In other words, E 1 (ω) consists precisely of functions that are ω-psh and of finite energy,
so that the chosen terminology is consistent.
Proof. The inclusion E 1 (ω) ⊂ E~1 ∩ PSH(ω) is clear. Conversely, pick ϕ ∈ E~1 ∩ PSH(ω),
and write ϕ = ϕ+ − ϕ− with ϕ± ∈ E 1 (ω 0 ) for some ω 0 ∈ Amp(X). After adding constants,
                                                     n+1
we may assume ϕ, ϕ± ≤ 0. Then ((ω, ϕ) + (ω 0 , ϕ− ))       ≤ (ω, ϕ)n+1 , by expanding out the
left-hand side. By Theorem 7.8 (iv), we infer
                                                              n+1
                −∞ < (ω + ω 0 , ϕ+ )n+1 = (ω, ϕ) + (ω 0 , ϕ− )     ≤ (ω, ϕ)n+1 .
Thus ϕ ∈ E 1 (ω), which proves the result.                                                                    
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


## Author source unit source-extracts/1801.08229-lines-4212-4251.txt

  We turn to (ii). By Proposition 7.19 (iv), we have µj → µ. Further,
            ˆ
              ϕ0j µj = (ω0 , 0) · (ω1 , ϕ1j ) · . . . · (ωn , ϕnj ) − (ω0 , ϕ0j ) · . . . · (ωn , ϕnj )

is finite for each j, and converges to
                ˆ
                  ϕ0 µ = (θ0 , 0) · (ω1 , ϕ1 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ0 ) · . . . · (ωn , ϕn ).

The result is now a consequence of Lemma 7.22.                                                                
Remark 7.23. For continuous ω-psh functions, mixed Monge–Ampère measures can also be
defined using the general theory developed by Chambert-Loir and Ducros [CLD12]. By base
change invariance of their theory, it follows from Proposition 7.19 (ii) and [BE20, Theorem
8.18] that the present approach is compatible with [CLD12] for continuous ω-psh functions.
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


## Author source unit source-extracts/1801.08229-lines-4529-4605.txt

                             (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n )
                                     . max (ωI , ϕI )n+1 − (ωI , ϕ0I )n+1 .
                                           I
By Corollary 7.31, we have for each I
                                                                          −n                                             −n
           (ωI , ϕI )n+1 − (ωI , ϕ0I )n+1 . dωI (ϕI , ϕ0 )2                    max{dωI (ϕI ), dωI (ϕ0I )}1−2                  ,
since sup ϕI = sup ϕ0I = 0. Now Lemma 7.36 implies
                                                        2
                                dωI (ϕI , ϕ0I ) . sn max dωi (ϕi , ϕ0i )βn M 1−βn
                                                              i
and
                              max{dωI (ϕI ), dωI (ϕ0I )} . tn M.
Combining all this we get, as desired,
                                                                                       2
       (ω0 , ϕ0 ) · . . . · (ωn , ϕn ) − (ω0 , ϕ00 ) · . . . · (ωn , ϕ0n ) . sn max dωi (ϕi , ϕ0i )αn M 1−αn ,
                                                                                             i

with αn := βn   2−n .                                                                                                             
Proof of Corollary 7.35. Set first ci := sup ϕi , ϕ0i := ϕi − ci . Then
         (θ0 , ϕ0 ) · . . . · (θn , ϕn ) = (θ0 , ϕ00 + c0 ) · . . . · (θn , ϕ0n + cn )
                                                                                   n
                                                                                   X
                                        = (θ0 , ϕ00 ) · . . . · (θn , ϕ0n ) +              ci (θ0 · . . . · θbi · . . . · θn ).
                                                                                    i=0
Now
                n
                X                                                                          
                      ci (θ0 · . . . · θbi · . . . · θn ) .       max | sup ϕi |   max kθi kω (ω n ).
                                                                                            n
                                                                    i                         i
                i=0
90                             SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

and we may thus assume wlog that sup ϕi = 0. Set C := maxi {1, kθi kω , dω (ϕi )}. Since
C ≥ 1, C −1 ϕi ∈ E 1 (ω) satisfies dω (C −1 ϕi ) . 1, by the quasi-convexity estimate (3.21).
After replacing θi and ϕi with C −1 θi and C −1 ϕi , we may thus assume as well that C . 1,
and we then need to prove |(θ0 , ϕ0 ) · . . . · (θn , ϕn )| . 1.
  Set ωi := θi +(C +1)ω, so that ω ≤ ωi ≤ (2C +1)ω and θi = ω +ωi −(C +2)ω. Expanding
out
                                     (θ0 , ϕ0 ) · . . . · (θn , ϕn )
        = [(ω, ϕ0 ) + (ω0 , 0) − (C + 2)(ω, 0)] · . . . · [(ω, ϕn ) + (ωn , 0) − (C + 2)(ω, 0)]
now yields the desired estimate, thanks to Theorem 7.34.                                                       
     As a further consequence of Theorem 7.34, we show:
Lemma 7.37. Pick (θi , ϕi ) ∈ N1 (X) × E~1 , i = 1, . . . , n, and set µ := i (θi + ddc ϕi ).
                                                                           V
Suppose also that we are given ω ∈ Amp(X),
                                     ´        ´ a convergent net ψj → ψ in PSH(ω) with
                                             and
Jω (ψj ) uniformly bounded. Then limj ψj µ = ψ µ.
Proof. By multilinearity, we may assume wlog θi ∈ Amp(X) and ϕi ∈ E 1 (θi ). By Theo-
rem 4.15, each ϕi canV be written as the limit of a decreasing net (ϕil )l in Hdom (θi ). For each
l, the measure ´µl := i (θ´i + ddc ϕil ) has finite support in X div (see Proposition 7.19 (ii)),
and hence limj ψj µl = ψ µ, since ψj → ψ pointwise                            div
                                                                    ´ on X ´ by assumption. To conclude
the proof, it will thus be enough to show that liml τ µl = τ µ uniformly for τ ∈ E 1 (ω)
with Jω (τ ) ≤ C. Now
           ˆ
              τ µl = (ω, τ ) · (θ1 , ϕ1l ) · . . . · (θn , ϕnl ) − (ω, 0) · (θ1 , ϕ1l ) · . . . · (θn , ϕnl ),
             ˆ
                 τ µ = (ω, τ ) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ) − (ω, 0) · (θ1 , ϕ1 ) · . . . · (θn , ϕn ).

Since (ϕil )l is decreasing, we have liml dθi (ϕil , ϕi ) = 0, by (7.21) and Theorem 7.14. The
desired uniform convergence is now a consequence of Theorem 7.34.                           
     This yields in turn the following monotone convergence theorem.
Theorem 7.38. Pick ω ∈ Amp(X). For i = 0, . . . , n, assume we are given θi ∈ N1 (X) and
an increasing net (ϕij )j in E 1 (ω) that converges pointwise on X div to ϕi ∈ E 1 (ω). Then
                         lim(θ1 , ϕ1j ) · . . . · (θn , ϕnj ) = (θ1 , ϕ1 ) · . . . · (θn , ϕn ).
                           j

Proof. By multilinearity, we can assume wlog θi ≥ ω for all i, and hence E 1 (ω) ⊂ E 1 (θi ).
                                                                                    i ≥ p. The
We proceed by induction on p = 0, . . . , n such that ϕij = ϕi is a constant net forQ
case p = 0 is trivial, so assume p ≥ 1. By monotonicity of the energy pairing on i PSH(θi )
(see Theorem 7.1), j 7→ (θ0 , ϕ0j ) · . . . · (θn , ϕnj ) is increasing, and
                         lim(θ0 , ϕ0j ) · . . . · (θn , ϕnj ) ≤ (θ0 , ϕ0 ) · . . . · (θn , ϕn ).
                           j


## Author source unit source-extracts/1801.08229-lines-4840-4874.txt

the right-hand side of (8.3) coincides with Eπ? ω (π ? ϕ). Since π ? PSH(ω) ⊂ PSH(π ? ω), (7.10)
further yields Eω (ϕ) ≤ Eπ? ω (π ? ϕ).
   Conversely, pick ψ ∈ PSH(π ? ω) such that ψ ≤ π ? ϕ. After replacing ψ with max{ψ, c}
for a constant c ≤ ϕ, we may assume that ψ is bounded. Choose ωX ∈ Amp(X) and
ϕX ∈ PSH(ωX ) as in Theorem 4.32. Replacing ωX and ϕX with small enough multiples,
we may assume ωX ≤ ω, and hence ϕX ∈ PSH(ω). Since ϕ and ψ are both bounded, we
may further arrange, after adding a constant to ϕX , that ϕX ≤ ϕ and π ? ϕX ≤ ψ. For each
m ∈ Z>0 , we get ϕm ∈ PSH(ω) such that
                                   π ? ϕm = (1 − m
                                                 1      1 ?
                                                   )ψ + m π ϕX .
Since ϕX ≤ ϕ, we have π ? ϕm ≤ π ? ϕ, and hence ϕm ≤ ϕ, see Theorem 4.22. On the
other hand, since π ? ϕX ≤ ψ, Theorem 4.22 shows that (ϕm ) is an increasing sequence
in PSH(ω), such that π ? ϕm → ψ pointwise on Y div . Now set c := min{inf ϕ, inf ψ} and
ϕ0m := max{ϕm , c}. Then (ϕ0m ) is also an increasing sequence, this time in E ∞ (ω) ⊂ E 1 (ω),
with π ? ϕ0m → ψ pointwise on Y div . Further, ϕ0m ≤ ϕ, and hence
                         X
                            cα Eω|Xα (ϕ0m |Xαan ) = Eω (ϕ0m ) ≤ Eω (ϕ),
                            α
96                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

by (7.10). Since ϕ0m |Xαan → ψ|Xαan pointwise on Xαdiv , Theorem 7.38 yields Eω|Xα (ϕ0m |Xαan ) →
Eω|Xα (ψ|Xαan ), and hence
                                       X
                           Eπ? ω (ψ) =    cα Eω|Xα (ψ|Xαan ) ≤ Eω (ϕ).
                                        α
Taking the supremum over all ψ, we conclude, as desired, Eπ? ω (π ? ϕ) ≤ Eω (ϕ).               
8.2. Further extensions. Using the extension of the Monge–Ampère energy E to continu-
ous functions, we now go further and extend it to (upper or lower) semicontinuous functions.
Definition 8.2. For any ϕ : X an → R ∪ {±∞} we set
                       E↑ (ϕ) := sup E(ψ) | ψ ∈ C0 (X), ψ ≤ ϕ
                                    
                                                                                           (8.5)
and


## Author source unit source-extracts/1801.08229-lines-4964-5024.txt

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


## Author source unit source-extracts/1801.08229-lines-5182-5314.txt


Proposition 9.8. For any µ ∈ M we have
                                                            ˆ   
                                  ∨
                                 E (µ) =     sup       E(ϕ) − ϕ µ                       (9.6)
                                           ϕ∈C0 (X)

and for any ϕ ∈ C0 (X) we have
                                                              ˆ     
                                                      ∨
                                  E(ϕ) = inf         E (µ) +       ϕµ                   (9.7)
                                           µ∈M

Proof. Note that (9.2) implies
                                            ˆ                             ˆ   
                ∨
              E (µ) =      sup         E(ϕ) − ϕ µ ≤            sup     E(ϕ) − ϕ µ .
                        ϕ∈PL ∩ PSH                         ϕ∈C0 (X)

Now pick ϕ ∈ C0 (X) and ψ ∈ E 1 such that ψ ≤ ϕ. Then
                                ˆ              ˆ
                       E(ψ) − ϕ µ ≤ E(ψ) − ψ µ ≤ E∨ (µ),

and taking the supremum over ψ yields
                                         ˆ   
                            sup     E(ϕ) − ϕ µ ≤ E∨ (µ).
                              ϕ∈C0 (X)

  Thus (9.6) holds. Now use this equation to define E∨ (µ) for any signed measure µ ∈
C0 (X)∨ . If µ(1) 6= 1, then E(c) = c for c ∈ R implies that
                                 E∨ (µ) ≥ sup (c(1 − µ(1))) = +∞.
                                           c∈R
                                                          ´
Similarly, if µ ∈ C0 (X)∨ and ϕ ∈ C0 (X) satisfy ϕ ≥ 0 and ϕ µ < 0, then E(tϕ) ≥ 0 for
t ≥ 0 yields                              ˆ       
                              ∨
                             E (µ) ≥ sup −t ϕ µ = +∞.
                                           t≥0
       ∨
Thus E     ≡ +∞ on C0 (X)∨ \ M1 . As E is concave, Legendre duality now yields (9.7).
                                                                                            
  The next duality statement will be used in the proof of Theorem 9.11.
Proposition 9.9. For any usc function ϕ : X an → R ∪ {−∞}, we have
                                                 ˆ    
                          E↓ (ϕ) = inf E∨ (µ) + ϕ µ .                                   (9.8)
                                           µ∈M

Proof. Write ϕ as the limit of a decreasing net (ϕi ) in C0 (X). On the one hand, for each
µ ∈ M we have                                           ˆ
                             E↓ (ϕ) ≤ E(ϕi ) ≤ E∨ (µ) + ϕi µ,
                                      ´
by (9.7), and hence E↓ (ϕ) ≤ E∨ (µ) + ϕ µ, by Lemma 7.17. On the other hand,
                               ˆ                    ˆ      
                        ∨                        ∨
                 inf E (µ) + ϕ µ ≤ inf E (µ) + ϕi µ = E(ϕi ),
                    µ                            µ

where the right-hand side converges to E↓ (ϕ), by Proposition 8.3 (v). This proves (9.8).   
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                     103

9.3. Maximizing nets. With a view towards solving the Monge–Ampère equation MA(ϕ) =
µ, we introduce the following notion.
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
on the irreducible components of X an .
Corollary 9.13. Pick µ ∈ M1 . Then µ(Xα ) = (ω n )Xα /(ω n )X for all α, and µ(Z) = 0 for
all Zariski closed subsets Z ⊂ X with dim Z < n.
Proof. Set cα := (ω n )Xα /(ω n )X (which vanishes if dim Xα < n). Pick a maximizing net (ϕi )
for µ. By Theorem 9.11, µi := MA(ϕi ) converges weakly to µ. By Corollary 7.49 (ii), we
have µi (Xα ) = cα for all i and α, and hence
                                    µ(Xα ) ≥ lim sup µi (Xα ) = cα .
                                                   i
As in the proof of Corollary 7.49, when α 6= α0 µ further puts no mass on the pluripolar set
Xαan ∩ Xαan0 , by Lemma 9.2. Thus
                                        X             X
                            1 = µ(X) =      µ(Xα ) ≥      cα = 1,
                                               α                α
which forces µ(Xα ) = cα for all α. Finally let Z ⊂ X be a Zariski closed subset with
dim Z < n, and pick an irreducible component Y of Z. If Y is not a component of X
then Y an is pluripolar, and hence µ(Y ) = 0, by Lemma 9.2. If Y = Xα for some α then
µ(Y ) = cα , which vanishes as well since dim Xα < n. Since this holds for all components of
Z, we get, as desired, µ(Z) = 0.                                                          
104                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

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


## Author source unit source-extracts/1801.08229-lines-6080-6148.txt

Lemma 11.17. Assume ω = c1 (L) with L an ample line bundle, and pick a  1 such that
mL is globally generated for all m ≥ a. Pick v ∈ X lin , and set for each m ≥ a
                     ϕv,m := m−1         max          (log |s| + v(s)) ∈ HR (L).
                                    s∈H0 (X,mL)\{0}

Then (ϕv,m )m≥a is a maximizing sequence for δv , and hence MA(ϕv,m ) → δv strongly in
M1 .
Proof. We first claim that limm→∞ E(ϕv,m ) = supm≥a E(ϕv,m ). To see this, observe that
                             (m + m0 )ϕv,m+m0 ≥ mϕv,m + m0 ϕv,m0
for all m, m0 ≥ a. Set S := supm E(ϕv,m ), pick ε > 0, and choose m0  1 such that
E(ϕv,m0 ) ≥ S − ε. For each m ≥ m0 + a write m − a = qm0 + r with q ∈ N and r ∈
{0, . . . , m0 − 1}. The above superadditivity property yields
                              mϕv,m ≥ qm0 ϕv,m0 + (r + a)ϕv,r+a .
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                       119

Thus ϕv,m ≥ ϕv,m0 − O(m−1 ), and hence
                            E(ϕv,m ) ≥ S − ε − O(m−1 ) ≥ S − 2ε
for all m  1, proving the claim.
   Since log |s|(v) = −v(s) for s ∈ H0 (X, mL) \ {0}, we have ϕv,m (v) = 0. Thus
                            lim E(ϕv,m ) = sup E(ϕv,m ) ≤ E∨ (δv ),
                           m→∞                  m≥a

and we need to show that this is an equality. Pick ϕ ∈ H(L), so that
                                    ϕ = m−1 max{log |si | + λi }
                                                i
for some m ∈ Z>0 , a basepoint free, finite set (si ) of H0 (X, mL) and λi ∈ Q. We may
assume wlog m ≥ a, since we have for r ∈ Z>0
                              ϕ = (rm)−1 max{log |sri | + rλi }.
                                                 i
For each i we have
                         −v(si ) + λi = log |si |(v) + λi ≤ mϕ(v).
This yields ϕ ≤ ϕv,m + ϕ(v), and hence E(ϕ) − ϕ(v) ≤ E(ϕv,m ). We infer
                        E∨ (δv ) = sup (E(ϕ) − ϕ(v)) ≤ sup E(ϕm ),
                                    ϕ∈H(L)                       m≥a

which proves, as desired, that (ϕv,m ) is a maximizing sequence for δv . The final assertion
now follows from Corollary 10.13.                                                          
Proof of Theorem 11.13. By Lemma 10.18, we may assume that ω = c1 (L) with L ∈
Pic(X)Q ample. By homogeneity, we can even assume that L is a globally generated line
bundle. For each v ∈ X lin consider the sequence (ϕv,m ) from Lemma 11.17. For w ∈ X lin
we have
                      ϕv,m (w) = m−1       max       (v(s) − w(s)) ,
                                            s∈H0 (X,mL)\{0}
and Lemma 11.7 thus shows that
                          d∞ (v, w) = lim max{ϕv,m (w), ϕw,m (v)}.                       (11.5)
                                          m→∞
On the other hand, Lemma 10.7 and (10.3) yield
                  I(ϕv,m , ϕw,m ) ≈ I∨ (MA(ϕv,m ), MA(ϕw,m )) → I∨ (δv , δw ).           (11.6)
Write                               ˆ
                I(ϕv,m , ϕw,m ) =       (ϕv,m − ϕw,m ) (MA(ϕw,m ) − MA(ϕv,m )) .
By Lemma 11.17, (ϕv,m ) and (ϕw,m ) are maximizing sequences for δv and δw . By Corol-
lary 9.18,        ˆ                    ˆ
                        ϕv,m MA(ϕv,m ) =             ϕv,m (MA(ϕv,m ) − δv ) → 0
and                          ˆ
                                 ϕw,m MA(ϕv,m ) − ϕw,m (v) → 0.
Exchanging the roles of v and w, we infer
        I(ϕv,m , ϕw,m ) = ϕv,m (w) + ϕw,m (v) + o(1) ≈ max{ϕv,m (w), ϕw,m (v)} + o(1).
Combining this with (11.5) and (11.6), we conclude, as desired, d∞ (v, w) ≈ I∨ (δv , δw ).   
120                      SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

   As an application of the above results, we prove:
Theorem 11.18. Assume char k = 0. Then X div is dense in X lin with respect to the strong
topology.
Lemma 11.19. Let vi → v be a weakly convergent net in X lin . If vi ≤ v, then vi → v


# Source identity, published background and application checks

{
  "key": "2307.01697",
  "supplied_pointer": {
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
  "actual_hashes": {
    "pdf": "979daddbb2082320cd6bbe6f8522535e68b56d229317decd033c3101b9fdbaa1",
    "literal_extract": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
    "abstract_html": "95e379bf14e7779de66bca6e020525202fc32bdb575bd1196934cf6ee43eb11a"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true,
    "abstract_html": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/P16-arxiv-2307.01697-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/2307.01697-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "8068829692eeb5ddcfd40de5a6141f415601c5b493e5578ad63e0dd3140bf2e4",
  "from_pdf_file": "source-extracts/2307.01697-from-pdf.txt",
  "from_pdf_header": "                                           MEASURES OF FINITE ENERGY IN PLURIPOTENTIAL THEORY: A\n                                                            SYNTHETIC APPROACH\n\n                                                                   SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON\n\n                                                                  To Bo Berndtsson, on the occasion of his 70+ε-th birthday\narXiv:2307.01697v1 [math.CV] 4 Jul 2023\n\n\n\n\n                                                 Abstract. We introduce a synthetic approach to global pluripotential theory, covering in\n                                                 particular the case of a compact Kähler manifold and that of a projective Berkovich space\n                                                 over a non-Archimedean field. We define and study the space of measures of finite energy,\n                                                 introduce twisted energy and free energy functionals thereon, and show that coercivity of\n                                                 these functionals is an open condition with respect to the polarization.\n\n\n\n\n                                                                                        Contents\n                                            Introduction                                                                                       1\n                                            1. A synthetic pluripotential theoretic formalism                                                  6\n                                            2. Measures of finite energy                                                                      18\n                                            3. Lipschitz and Hölder estimates for the energy                                        ",
  "identity": "Boucksom--Jonsson, Measures of finite energy in pluripotential theory: a synthetic approach, arXiv:2307.01697v1, banner 4 Jul 2023.",
  "applications": [
    "Section 1.2.2 realizes the synthetic formalism on projective Berkovich spaces via model functions and intersection measures. Section 1.3.2 identifies the ample positivity class in the discrete smooth residue-zero case.",
    "Example 2.20 states test-function orthogonality for projective Berkovich spaces over arbitrary non-Archimedean fields, using BE21 and BGM22 as published background. We use this stated result, not an independently fetched BGM source.",
    "Proposition 2.2 (2.7), Theorem 1.26, Theorem 2.23, and Lemma 2.25 (2.27) apply to our semipositive reference theta and finite-dual-energy probability nu. The proof document proves the extension of these test estimates to BFJ E1 and the consequent discrete-field existence.",
    "Theorem 2.26 and Theorem A prove completeness and density on the measure side. They alone assert neither a general unbounded-potential operator nor its surjectivity."
  ],
  "limitations": [
    "Remark 2.14 explicitly sets aside the potential theory. General-field test orthogonality is weaker than a proved continuous/finite-energy envelope theory."
  ],
  "published_background_used_via_this_source": [
    {
      "citation": "BE21",
      "identity": "Boucksom--Eriksson, Spaces of norms, determinant of cohomology and Fekete points in non-Archimedean geometry, Adv. Math. 378 (2021), article 107501, 124 pp.",
      "used_result": "Theorem A in Example 2.20",
      "application": "Our smooth geometrically integral projective X is geometrically reduced; L is ample; K is complete. The corresponding supplied arXiv cache is actual 1805.01016v3."
    },
    {
      "citation": "BGM22",
      "identity": "Boucksom--Gubler--Martin, Differentiability of relative volumes over an arbitrary non-Archimedean field, IMRN 2022 no. 8, 6214--6242.",
      "used_result": "Lemma 3.2 in Example 2.20",
      "application": "Invoked through the explicit projective-Berkovich orthogonality assertion of supplied 2307.01697v1 Example 2.20; no independent BGM22 file was supplied or fetched. We claim only the domain expressly asserted there."
    }
  ]
}

## Author source unit source-extracts/2307.01697-lines-89-166.txt

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


## Author source unit source-extracts/2307.01697-lines-346-386.txt

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


## Author source unit source-extracts/2307.01697-lines-508-532.txt

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


## Author source unit source-extracts/2307.01697-lines-677-705.txt

   We next consider the quantity
                                        ˆ             
                        Tω := sup sup φ − φ µω | φ ∈ Dω ∈ [0, +∞].                                   (1.20)

Thus Tω < ∞ iff there exists C > 0 such that the submean value inequality
                                          ˆ
                                  sup φ ≤ φ µω + C                                                   (1.21)

holds for all φ ∈ Dω .
Proposition 1.23. If Tω < ∞, then Tω′ < ∞ for any ω ′ ∈ Z+ with [ω ′ ] ∈ Pos(X).
Definition 1.24. We say that the submean value property holds if Tω < ∞ for some (hence
any) ω ∈ Z+ with [ω] ∈ Pos(X).
   When X is a compact Kähler or projective Berkovich space, this property holds iff X is
irreducible (see Theorem 1.26 below).
Lemma 1.25. Pick τ ∈ Dω , and ω ′ ∈ Z+ commensurable to ω. Then
                                        Tωτ ≤ Tω + (n + 2) sup |τ |                                  (1.22)
and
                                               Tω′ ≤ eO(δ) Tω                                        (1.23)
with δ := dT (ω, ω ′ ).
     Recall that, in this paper, the implicit constant in O only depends on n (see §1.1).
                                  MEASURES OF FINITE ENERGY                                       15

Proof. Pick φ ∈ Dωτ . Then φ + τ ∈ Dω , and the Chern–Levine–Nirenberg inequality (1.19)
yields            ˆ                         ˆ
           φ+τ ≤       (φ + τ ) MAω (0) + Tω ≤          (φ + τ ) MAω (τ ) + n sup |τ | + Tω .
This proves (1.22), in view of (1.18).
  For each t > 0 we have Dtω = tDω , and hence Ttω = tTω . Further, ω ′ ≤ ω implies
Dω′ ⊂ Dω and


## Author source unit source-extracts/2307.01697-lines-850-923.txt


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


## Author source unit source-extracts/2307.01697-lines-1020-1047.txt

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


## Author source unit source-extracts/2307.01697-lines-1115-1168.txt


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


## Author source unit source-extracts/2307.01697-lines-1169-1290.txt

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

                 |Jω (µ, ψi ) − Jω (µ, ψj )| ≲ Jω (ψi , ψj )α R1−α
                                           ≲ max{Jω (ν, ψi ), Jω (ν, ψj )}α R1−α .
This estimate implies that (Jω (µ, ψi )) is a Cauchy sequence, which thus admits a limit
                                    δω (µ, ν) := lim Jω (µ, ψi ).                       (2.28)
                                                   i

The same estimate also shows that the limit is independent of the choice of maximizing
sequence (ψi ), and that the convergence in (2.28) is uniform with respect to µ ∈ M1ω,R . As
a consequence, µ 7→ δω (µ, ν) so defined is continuous on M1ω for each ν ∈ M1ω .
   By construction, (2.22) holds, and hence also (2.21), by (2.5). This proves (i).
   Next, (2.24) holds when ν, ν ′ lie in the image of MAω : Dω → M1ω , by applying (2.26) to
a maximizing sequence for µ′ , and the general case follows by using maximizing sequences
for ν, ν ′ . This shows (iii), which also yields the continuity of δω on M1ω × M1ω (and hence
conclude the proof of existence), since µi → µ strongly implies δω (µi , µ) → δω (µ, µ) = 0, by
continuity of δω (·, µ).
   Similarly, (iv) follows follows by applying (2.27) to a maximizing sequence (τi ) for ν.
   Finally, the first point in (ii) follows from (2.25), since Dω spans the dense subspace D of
  0
C (X) (see Corollary 1.13). By (1.34) and (1.35), the last two properties in (ii) hold when
the measures lie in the image of MAω , and hence in general, by continuity of δω .
                                                                                              □

  We next show:
Theorem 2.26. The quasi-metric space (M1ω , δω ) only depends on the class [ω]. It is
complete, and its topology coincides with the strong topology.
Lemma 2.27. For any ν ∈ M1 and R > 0, δω (·, ν) is weakly lsc on M1ω,R .
26                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. When ν = MAω (ψ) with ψ ∈ Dω , (2.22) yields δω (·, ν) = Jω (·, ψ), which is weakly
lsc on M1ω (see (2.1)). In the general case, pick a maximizing sequence (ψi ) for ν, and set
νi := MAω (ψi ). By (2.24), we have δω (µ, νi ) → δω (µ, ν) uniformly for µ ∈ M1ω,R , and the
result follows.                                                                            □

Proof of Theorem 2.26. We already know that M1ω only depends on [ω] (see Proposition 2.6).
Pick τ ∈ Dω , µ, ν ∈ M1ω = M1ωτ , and choose maximizing sequences (φi ), (ψi ) in Dωτ
for µ, ν, so that δωτ (µ, ν) = limi Jωτ (φi , ψi ). By (2.8), (φi + τ ) and (ψi + τ ) are maxi-
mizing sequences in Dω for µ, ν, and hence δω (µ, ν) = limi Jω (φi , ψi ). Now (1.39) yields
Jωτ (φi , ψi ) = Jω (φi + τ, ψi + τ ), which proves δωτ (µ, ν) = δω (µ, ν) and proves that δω only
depends on [ω].
   We next show that the topology of (M1ω , δω ) is the strong topology, i.e. a net (µi ) converges
strongly to µ ∈ M1ω iff δω (µi , µ) → 0. When the latter holds, (2.25) implies µi → µ weakly
(since Dω spans the dense subspace D of C0 (X)), while (2.24) yields Jω (µi ) = Jω (µi , 0) →
Jω (µ). Thus µi → µ strongly, and the converse holds by strong continuity of δω .
   Finally, consider a Cauchy net (µi ) in (M1 , δω ). Then Jω (µi ) = δω (µi , µω ) is eventually
bounded. By weak compactness of M, we may assume, after passing to a subnet, that (µi )
admits a weak limit µ ∈ M. Since Jω is weakly lsc on M, we get Jω (µ) ≤ lim inf i Jω (µi ) <
+∞, i.e. µ ∈ M1 . It remains to show δω (µi , µ) → 0. To see this, pick ε > 0 and i0 such that
δω (µi , µj ) ≤ ε for all i, j ≥ i0 . Since Jω (µj ) is bounded and µj → µ weakly, Lemma 2.27
yields δω (µi , µ) ≤ lim inf j δω (µi , µj ) ≤ ε, and we are done.                               □

     To conclude this section, we show:
Proposition 2.28. For each ν ∈ M1ω , δω (·, ν) : M1ω → R≥0 is strictly convex, and we
further have the uniform convexity estimate
           (1 − t)δω (µ0 , ν) + tδω (µ1 , ν) − δω ((1 − t)µ0 + tµ1 , ν) ≳ t(1 − t)δω (µ0 , µ1 ).
for all µ0 , µ1 ∈ M1ω and t ∈ [0, 1].
Proof. By density of the image of MAω : Dω → M1ω and continuity of δω , we may assume
without loss ν = MAω (ψ) with ψ ∈ Dω , and hence δω (·, ν) = Jω (·, ψ). Set
                   Jt := (1 − t)Jω (µ0 , ψ) + tJω (µ1 , ψ),    µt := (1 − t)µ0 + tµ1 ,


## Author source unit source-extracts/2307.01697-lines-2314-2328.txt

            lim       (f − φ) MAω (φ) =   (π ⋆ f − Pθ (π ⋆ f )) MAθ (Pθ (π ⋆ f )) = 0,    (B.2)
           φ∈Dω,<f   X                          Y
by (B.1).
  To prove the claim, note first that Conjecture B.1 implies that the increasing net {φ}φ∈Dω,<f
converges pointwise to
                              Pω (f ) := sup{ψ ∈ PSH(X, ω) | ψ ≤ f }.
46                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Indeed, given δ > 0 and a function ψ ∈ PSH(X, ω) with ψ ≤ f , Conjecture B.1 and a Dini-
type argument guarantees the existence of a function ψ ′ ∈ Dω,<f with ψ ≤ ψ ′ < f + δ. The
claim is thus equivalent to the statement that π ⋆ Pω (f ) coincides a.e. with φ := Pθ (π ⋆ f ).
To prove this, pick τ ∈ PSH(X, ω) with τ ≤ f and {τ = −∞} = Xsing (compare proof of
Lemma 1.27). Since ψε := (1 − ε)φ + επ ⋆ τ is π ⋆ ω-psh outside π −1 (Xsing ), and ψε ≡ −∞ on
the latter, we have ψε = π ⋆ φε for a unique φε ∈ PSH(X, ω) (see [Dem85, Théorème 1.10]).


# Source identity, published background and application checks

{
  "key": "2209.04879",
  "supplied_pointer": {
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
  "actual_hashes": {
    "pdf": "55defd54d8201c94d08f727e76f551c759275c68cde354570cb41e7a02df54f7",
    "literal_extract": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
    "abstract_html": "1b719dcc2de6a7437184f28dbaf37384bf39673fc8b66a35a4dc716f0cba5341"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true,
    "abstract_html": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/P16-arxiv-2209.04879-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/2209.04879-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "f80aba2042cab9a15649c87700aa5c86710dd33018bf025bd1817869d52b31e4",
  "from_pdf_file": "source-extracts/2209.04879-from-pdf.txt",
  "from_pdf_header": "                                                 GLOBAL PLURIPOTENTIAL THEORY ON HYBRID SPACES\n\n                                                                             LÉONARD PILLE-SCHNEIDER\n\n\n\n\n                                                  Abstract. Let A be a Banach ring, and X/A be a projective scheme of ﬁnite type,\n                                                  endowed with a semi-ample line bundle L. We deﬁne a class PSH(X, L) of plurisub-\narXiv:2209.04879v2 [math.AG] 17 Mar 2023\n\n\n\n\n                                                  harmonic metrics on L on the Berkovich analytiﬁcation X an and prove various basic\n                                                  properties thereof.\n                                                  We focus in particular on the case where A is a hybrid ring of complex power series and\n                                                  X/A is a smooth variety, so that X an is the hybrid space associated to a degeneration\n                                                  X of complex varieties over the punctured disk. We then prove that when L is ample,\n                                                  any plurisubharmonic metric on L with logarithmic growth at zero admits a canonical\n                                                  plurisubharmonic extension to the hybrid space X hyb . We also discuss the continuity\n                                                  of the family of Monge-Ampère measures associated to a continuous plurisubharmonic\n                                                  hybrid metric.\n                                                  In the case where X is a degeneration of canonically polarized manifolds, we prove that\n                                                  the canonical psh extensi",
  "identity": "Pille-Schneider, Global pluripotential theory on hybrid spaces, arXiv:2209.04879v2.",
  "applications": [
    "Remark 4.4 explicitly separates definition of E1 over arbitrary fields from the generally unclear operator extension.",
    "Theorem 4.7 treats smooth polarized varieties over k((t)) of equicharacteristic zero and skeleton-supported probability measures. Its probability convention is translated back to raw mass V in our argument."
  ],
  "limitations": [
    "The phrase discretely-valued of characteristic zero in Remark 4.4 does not license dropping the residue-characteristic-zero hypotheses of BFJ."
  ]
}

## Author source unit source-extracts/2209.04879-lines-1978-1997.txt

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


## Author source unit source-extracts/2209.04879-lines-2018-2029.txt

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


# Source identity, published background and application checks

{
  "key": "2506.13548",
  "supplied_pointer": {
    "public_source": "https://arxiv.org/pdf/2506.13548v2",
    "pdf": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
    "pdf_sha256": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
    "literal_extract": "/workspace/research/shared-sources/GR-2506.13548v2-20261004.txt",
    "extract_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
    "origin": "Published primary mathematical source, not generated research."
  },
  "actual_hashes": {
    "pdf": "83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726",
    "literal_extract": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/GR-2506.13548v2-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/2506.13548-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "3a221b86116604c950db07e4c60ab184701f0624deebabd92502e5c81871436b",
  "from_pdf_file": "source-extracts/2506.13548-from-pdf.txt",
  "from_pdf_header": "                                            CLASSICALLY PSH AND PLURIHARMONIC FUNCTIONS ON BERKOVICH SPACES\n\n                                                                          WALTER GUBLER AND JOSEPH RABINOFF\n\n\n                                                   ABSTRACT. First we extend the theory of subharmonic functions on smooth strictly k-\n                                                   analytic curves from Thuillier’s thesis to the case of possibly singular analytic curves over\n                                                   a non-archimedean field k. Classically psh functions are then defined as in complex geom-\narXiv:2506.13548v2 [math.AG] 17 Sep 2025\n\n\n\n\n                                                   etry by using pullbacks to analytic curves (and requiring compatibility with base change).\n                                                   We give various properties of classically psh functions including a local and a global max-\n                                                   imum principle. As a consequence, we show that the space of pluriharmonic functions on\n                                                   a quasi-compact Berkovich space is finite dimensional. As a technical tool, we use that a\n                                                   connected Berkovich space is connected by analytic curves.\n\n\n\n\n                                                                                      1. INTRODUCTION\n                                              Plurisubharmonic functions are the complex analytic counterparts of subharmonic func-\n                                           tions in real analysis. To recall the definition, we begin with the notion of subharmonicity\n                                           on the complex line. Let",
  "identity": "Gubler--Rabinoff, Classically psh and pluriharmonic functions on Berkovich spaces, arXiv:2506.13548v2, 17 Sep 2025.",
  "applications": [
    "Audit-only: introduction explicitly says defining MA and regularization may need extra hypotheses and are not its subject."
  ],
  "limitations": [
    "Its curve-pullback psh class is not substituted for the BFJ global psh cone or its finite-energy operator."
  ]
}

## Author source unit source-extracts/2506.13548-lines-1-19.txt

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



## Author source unit source-extracts/2506.13548-lines-64-88.txt

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



# Source identity, published background and application checks

{
  "key": "Thuillier",
  "supplied_pointer": {
    "public_source": "https://theses.hal.science/tel-00010990v1/document",
    "pdf": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
    "pdf_sha256": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
    "literal_extract": "/workspace/research/shared-sources/Thuillier-tel-00010990v1.txt",
    "extract_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
    "origin": "Published primary mathematical source, not generated research."
  },
  "actual_hashes": {
    "pdf": "9c57da951e8dca2676d762e9e8c6ace302675938d72434a5b0390f15af7ea29a",
    "literal_extract": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/Thuillier-tel-00010990v1.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/Thuillier-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570",
  "from_pdf_file": "source-extracts/Thuillier-from-pdf.txt",
  "from_pdf_header": "N° d'Ordre : 3231\n                                      THÈSE\n\n\n                                     présentée\n\n                    DEVANT L' UNIVERSITÉ DE           RENNES 1\n\n\n                              pour obtenir le grade de\n\n              DOCTEUR DE L'UNIVERSITÉ DE RENNES 1\n\n\n\n                    Mention : Mathématiques      et Appli ations\n\n\n                                         par\n\n                               Amaury THUILLIER\n\n\n                     Institut de Re her he Mathématique de Rennes\n\n\n\n                               É ole Do torale MATISSE\n\n\n\n                               U.F.R. de Mathématiques\n\n\n\n\n Théorie du potentiel sur les            ourbes en géométrie analytique\n                               non ar himédienne.\n\n                     Appli ations à la théorie d'Arakelov.\n\n\n\n\n    Soutenue le jeudi 13 o tobre 2005 devant la          ommission d'Examen\n\n\n\n\n                            Composition du jury :\n\n               M.     J.-B. Bost                 Rapporteur\n\n               M.     A. Chambert-Loir           Dire teur de thèse\n\n               M.     A. Du    ros               Examinateur\n\n               M.     C. Favre                   Examinateur\n\n               M.     L. Moret-Bailly            Examinateur\n\n               M.     R. Rumely                  Rapporteur\n\f\fThéorie du potentiel sur les    ourbes en\ngéométrie analytique non ar himédienne.\n\n Appli ations à la théorie d'Arakelov.\n\n\n\n\n             Amaury Thuillier\n\fAmaury Thuillier\nNWFI-Mathematik\nUniversität Regensburg\nD-93040 Regensburg\n\n\nourriel : amaury.thuillier\bmathematik.uni-regensburg.de\n\n\n\n\nVersion du 4 o tobre 2005\n\f                                     REMERCIEMENTS\n\n\n   Je dois à l'enthousiasme et à la grande patien e d'Antoine Chambert-Loir d'être \u001cnalement\npar",
  "identity": "Thuillier thesis, supplied HAL tel-00010990v1 PDF.",
  "applications": [
    "Audit-only: cited potential and metric statements are for smooth strictly analytic curves."
  ],
  "limitations": [
    "No projective-line or dimension-one restriction is silently added to a general-dimension claim; the corrupted cached OCR is not used for a new theorem."
  ]
}

## Author source unit source-extracts/Thuillier-lines-5516-5527.txt

                                           p−1 (Ω)
                                       Z
                                   =                 p∗ ψ ddc ϕ,
                                           p−1 (Ω)

et l'on a ainsi établi l'égalité
                                       ddc p∗ ϕ = p∗ ddc ϕ
dans l'espa e de mesures A1 (Ω).                                                                2

Remarque 3.2.14.  L'homorphisme ddc : A0c (X) → A1c (X) est ontinu relativement aux
topologies introduites sur es espa es ve toriels à la n du paragraphe 3.2.2. L'espa e ve toriel


## Author source unit source-extracts/Thuillier-lines-5676-5717.txt

ni de points de type (2) qu'il est loisible d'agrandir en un ensemble lo alement ni de points
de type (2) S tel que, de plus, la fon tion ϕ soit harmonique sur X − S .
   Quels que soient l'ouvert U ′ ∈ U ′ et la omposante onnexe C de X − S ,
                                           C ∩ U′ = C ∩ U′
puisque ∂U ′ = U ′ − U ′ est ontenu dans S . Ce i implique don C ⊂ U ′ ou C ∩ U ′ = ∅. Soit
alors, pour tout point x ∈ S , Ωx la réunion des omposantes onnexes de X − S qui sont
adhérentes à x ; 'est un voisinage de x qui, d'après e que l'on vient de dire, est ontenu dans
 ha un des ouverts U ′ ∈ U ′ ontenant x.
   La famille V = {Ωx }x∈S est un re ouvrement ouvert lo alement ni de Ω qui rane le
re ouvrement U ′ ; S est la réunion des ∂Ωx , x ∈ S , et un point y de S appartient à l'ouvert
Ωx si et seulement si y = x. Ce re ouvrement satisfait à toutes les propriétés requises.
80



   Se onde étape. Il ne reste plus grand hose à faire maintenant. Soit, pour tout v ∈ V , ϕV la
fon tion ontinue sur V et harmonique sur V qui s'annule identiquement sur ∂V et oïn ide
ave ϕ sur S ∩ V . Elle se prolonge naturellement en un élément de A0c (X), en ore noté ϕV ,
identiquement nul en dehors de V . Tout point x de S étant ontenu dans un unique ouvert
V de V , la fon tion
                                        X
                                           ϕV ∈ A0c (X)
                                       V ∈V
est égale à ϕ sur S ; le prin ipe du maximum implique par onséquent l'identité
                                            X
                                         ϕ=    ϕV .
                                                V ∈V

Le support de ha une des fon tions ϕV est ontenu dans un ouvert de U et les inégalités du
point (ii) sont une évidentes.
     La démonstration du lemme est a hevée.                                                   2

Proposition 3.3.6.  Pour toute         ourbe stri tement k-analytique lisse X , la orrespon-
dan e Ω 7→ D (Ω) est un fais eau sur l'espa e topologique X , i ∈ {0, 1}.
          i

Démonstration. L'assertion est triviale pour i = 0 en vertu de l'identi ation anonique


# Source identity, published background and application checks

{
  "key": "Berkovich",
  "supplied_pointer": {
    "public_source": "https://www.numdam.org/item/PMIHES_1993__78__5_0/",
    "pdf": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
    "pdf_sha256": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
    "literal_extract": "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.txt",
    "extract_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
    "origin": "Published primary mathematical source, not generated research."
  },
  "actual_hashes": {
    "pdf": "bd864c89ed8b6e8f27a90f459837221549db75afa75554ab51414e17771066af",
    "literal_extract": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/Berkovich-PMIHES-1993-78-5.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/Berkovich-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "694ba4de951bb7e40c73fa4057e4bed5ce073757690ac7379bb1cbbabaf62c1d",
  "from_pdf_file": "source-extracts/Berkovich-from-pdf.txt",
  "from_pdf_header": "P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.\n\n\n\n\n V LADIMIR G. B ERKOVICH\n Étale cohomology for non-Archimedean analytic spaces\n Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161\n <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>\n\n\n\n\n      © Publications mathématiques de l’I.H.É.S., 1993, tous droits réservés.\n      L’accès aux archives de la revue « Publications mathématiques de l’I.H.É.S. » (http://\n      www.ihes.fr/IHES/Publications/Publications.html) implique l’accord avec les conditions géné-\n      rales d’utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou im-\n      pression systématique est constitutive d’une infraction pénale. Toute copie ou impression de\n      ce fichier doit contenir la présente mention de copyright.\n\n\n\n\n                               Article numérisé dans le cadre du programme\n                             Numérisation de documents anciens mathématiques\n                                           http://www.numdam.org/\n\f                                ETALE COHOMOLOGY\n                       FOR NON-ARCHIMEDEAN ANALYTIC SPACES\n                                                      by VLADIMIR G. BERKOVIGH (1)\n\n\n                                                                                CONTENTS\n\n\nINTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   7\n\n§ 1. Analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13\n        1.1. Underlying topolcgical s p a c e s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  ",
  "identity": "Berkovich, Etale cohomology for non-Archimedean analytic spaces, PMIHES 78 (1993), pp. 5--161.",
  "applications": [
    "Audit-only: analytic-space/cohomological background, not a finite-energy MA existence result."
  ],
  "limitations": [
    "Cohomological base change is not used as a substitute for compatibility of unbounded MA or energy."
  ]
}

## Author source unit source-extracts/Berkovich-lines-1-10.txt

P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.




 V LADIMIR G. B ERKOVICH
 Étale cohomology for non-Archimedean analytic spaces
 Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161
 <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>



## Author source unit source-extracts/Berkovich-lines-30-45.txt

                                                      by VLADIMIR G. BERKOVIGH (1)


                                                                                CONTENTS


INTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   7

§ 1. Analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13
        1.1. Underlying topolcgical s p a c e s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            13
        1.2. The category of analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     14
        1.3. Analytic domains and G-topology on an analytic space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          23
        1.4. Fibre products and the ground field extension functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       29
        1.5. Analytic spaces from [Ber] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                31
        1.6. Connection with rigid analytic geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             35



# Source identity, published background and application checks

{
  "key": "1204.6277",
  "supplied_pointer": {
    "public_source": "https://arxiv.org/pdf/1204.6277v2",
    "pdf": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
    "pdf_sha256": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
    "literal_extract": "/workspace/research/shared-sources/CD-1204.6277v2-20261004.txt",
    "extract_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
    "origin": "Published primary mathematical source, not generated research."
  },
  "actual_hashes": {
    "pdf": "5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719",
    "literal_extract": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085"
  },
  "hash_checks": {
    "pdf": true,
    "literal_extract": true
  },
  "pdf_extraction_command": [
    "pdftotext",
    "-layout",
    "/workspace/research/shared-sources/CD-1204.6277v2-20261004.pdf",
    "/workspace/research/campaigns/round-48/P16.6-public-source-arbitrary-support-finite-energy/artifacts/codex-oivLpo/source-extracts/1204.6277-from-pdf.txt"
  ],
  "pdf_extraction_returncode": 0,
  "from_pdf_sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
  "from_pdf_file": "source-extracts/1204.6277-from-pdf.txt",
  "from_pdf_header": "                                          FORMES DIFFÉRENTIELLES\n                                          RÉELLES ET COURANTS SUR LES\narXiv:1204.6277v2 [math.AG] 25 Jul 2025\n\n\n\n\n                                          ESPACES DE BERKOVICH\n\n\n\n\n                                                         Antoine Chambert-Loir\n                                                                Antoine Ducros\n\fAntoine Chambert-Loir\nUniversité Paris Cité, Institut de Mathématiques de Jussieu-Paris Rive Gauche,\nF-75013, Paris, France.\nE-mail : antoine.chambert-loir@math.univ-paris-diderot.fr\nAntoine Ducros\nSorbonne Université, Université de Paris, CNRS, Institut de Mathématiques de\nJussieu-Paris Rive Gauche, IMJ-PRG, F-75005, Paris, France.\nE-mail : antoine.ducros@imj-prg.fr\n\n\n\n\n29 juillet 2025, 0h06\n\fTABLE DES MATIÈRES\n\n\n\n\nIntroduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9\n  § 0.1. Contexte et philosophie. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9\n  § 0.2. Cet article. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11\n  § 0.3. Prolongements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16\n  § 0.4. Perspectives. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17\n  § 0.5. Remerciements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18\n\nPartie I. Géométrie tropicale. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ",
  "identity": "Chambert-Loir--Ducros, Formes differentielles reelles et courants sur les espaces de Berkovich, actual arXiv:1204.6277v2, 25 Jul 2025; internal 29 July 2025.",
  "applications": [
    "Audit-only: local currents/Bedford--Taylor and model-metric material. No application to all BFJ E1 targets in arbitrary fields is established in this work."
  ],
  "limitations": [
    "No identification of its local psh class with all unbounded BFJ global potentials, compactness, dual-energy attainment or global uniqueness is inferred."
  ]
}

## Author source unit source-extracts/1204.6277-lines-1-29.txt

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


## Author source unit source-extracts/1204.6277-lines-636-680.txt

topologique de X est au plus égale à sa dimension.
  Jell [88] a démontré que, même pour une courbe propre, la cohomologie de ces com-
plexes de Dolbeault peut être de dimension infinie. Jell et Wanner [89] ont observé que
ce n’est néanmoins pas le cas pour les courbes de Mumford, c’est-à-dire celles dont la
réduction est maximalement dégénérée ; dans ce cas, il y a même un analogue de la
dualité de Poincaré.
  Pour remédier à ce défaut, Gubler, Jell et Rabinoff [79] ont construit une variante de
notre théorie des formes lisses dans laquelles les tropicalisations sont, non pas seulement
de la forme log|f | pour une fonction analytique inversible f , mais des « fonctions har-
moniques » dans un sens permis par la théorie d’intersection sur le corps résiduel. Nous
avons réinterprété une partie de ce travail sous le vocable de « G-formes harmonique-
ment tropicalisées » ; comme déjà dans remarqué dans [79], de telles formes apparaissent
                                     § 0.4. PERSPECTIVES                                    17

naturellement dans la théorie des variétés abéliennes lorsque leur extension de Raynaud
n’est pas isotriviale.
   Dans [95], Liu construit la classe de Chern d’un cycle de codimension p sur une variété
algébrique propre X à valeurs dans le groupe H p,p (X) de cohomologie de Dolbeault. Pour
une variété définie sur Q, il démontre en particulier qu’un cycle (défini sur Q) dont la
classe de cohomologie de de Rham complexe usuelle est nulle a également une classe nulle
pour toutes les cohomologie de Dolbeault non archimédiennes associées aux différentes
places finies de Q.
   La cohomologie de ce complexe de Dolbeault est très certainement liée aux groupes
d’homologie tropicaux de [86], mais nous n’avons pas d’énoncé formel précis à proposer.
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


# Independent LF location addendum

# Root LF source addendum

Author files are unchanged. LF denotes the newline byte, with form feeds retained inside lines. The author helper uses Python splitlines, which additionally counts form feeds. These are different range conventions; the following bodies use an explicit LF convention. This is a source-location audit, not a mathematical verdict.


## 1201.0187-LF-88-101.txt

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


## 1201.0187-LF-150-194.txt

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


## 1201.0187-LF-1648-1766.txt

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


## 1201.0187-LF-1774-1823.txt

Definition 8.1. The θ-psh envelope Pθ (u) of a continuous function u ∈ C 0 (X) is defined
by setting, for each x ∈ X.
                     Pθ (u)(x) := sup {ϕ(x) | ϕ ∈ PSH(X, θ), ϕ ≤ u on X} .
     Here are a few easy properties of the envelope operator.
Proposition 8.2. Let u, u0 ∈ C 0 (X).
    (i) Pθ (u) is θ-psh, and is the largest θ-psh function dominated by u on X.
   (ii) Pθ is non-decreasing, i.e. u ≤ v ⇒ Pθ (u) ≤ Pθ (v).
  (iii) Pθ (u) is concave in both arguments, in the sense that
                      Ptθ+(1−t)θ0 tu + (1 − t)u0 ≥ tPθ (u) + (1 − t)Pθ0 (u0 )
                                                

           for 0 ≤ t ≤ 1.
      (iv) For each c ∈ R we have Pθ (u + c) = Pθ (u) + c.
       (v) For each v ∈ D(X) we have Pθ (u) = Pθ+ddc v (u − v) + v.
      (vi) Pθ is 1-Lipschitz continuous with respect to the sup-norm, i.e. supX |Pθ (u)−Pθ (v)| ≤
           supX |u − v|.
     (vii) Given a determination X of θ and a convergent sequence θm → θ in N 1 (X /S), we
           have Pθm (u) → Pθ (u) uniformly on X.
Proof. (i) The only thing to show is that Pθ (u) is θ-psh. Since Pθ (u) ≤ u and u is contin-
uous, it follows that the usc regularization satisfies Pθ (u)∗ ≤ u. Now, Pθ (u)∗ is θ-psh by
Theorem 7.11, and is hence a competitor in the definition of Pθ (u). Thus Pθ (u) = Pθ (u)∗ is
indeed θ-psh.
    (ii) is trivial.
    (iii) follows from the fact that given ϕ ∈ PSH(X, θ), ϕ0 ∈ PSH(X, θ0 ) with ϕ ≤ u and
ϕ ≤ u0 , tϕ + (1 − t)ϕ0 belongs to PSH(X, tθ + (1 − t)θ0 ) and is dominated by tu + (1 − t)u0 .
  0

    (iv) and (v) are seen similarly.
    (vi) is a formal consequence of (ii) and (iv).
    (vii) By Proposition 5.2 we may assume, after perhaps passing to a higher model, that
there exists a model function v determined on X such that θ + ddc v is X -positive, i.e. deter-
mined by an ample class in N 1 (X /S). As a consequence, there exists an open neighborhood
V ⊂ N 1 (X /S) of θ such that τ + ddc v is X -positive for all τ ∈ V .
    We claim that Pτ (u) is uniformly bounded on X for τ ∈ V . Indeed for each τ ∈ V we
have R ⊂ PSH(X, τ + ddc v), hence Pτ +ddc v (u − v) ≥ inf X u − supX |v|. By (v) it follows
             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                      37


that
                              inf u − 2 sup |v| ≤ Pτ (u) ≤ sup u,
                              X         X                  X
which proves the claim.
   Now for each x ∈ X the function τ 7→ Pτ (u)(x) is concave on V , hence locally Lipschitz
continuous on V , with local Lipschitz constant only depending on supτ ∈V |Pτ (u)(x)|, which
is in turn bounded independently of x ∈ X, and the result follows.                        
  Our main result in this section is the following regularity property of envelopes. As we
shall see, it is in fact equivalent to the monotone regularization theorem.
Theorem 8.3. For any u ∈ C 0 (X) the θ-psh envelope Pθ (u) is a uniform limit on X of
θ-psh model functions. In particular, Pθ (u) is continuous.
  Before attacking Theorem 8.3 we shall prove the following weaker statement.


## 1201.0187-LF-1774-1845.txt

Definition 8.1. The θ-psh envelope Pθ (u) of a continuous function u ∈ C 0 (X) is defined
by setting, for each x ∈ X.
                     Pθ (u)(x) := sup {ϕ(x) | ϕ ∈ PSH(X, θ), ϕ ≤ u on X} .
     Here are a few easy properties of the envelope operator.
Proposition 8.2. Let u, u0 ∈ C 0 (X).
    (i) Pθ (u) is θ-psh, and is the largest θ-psh function dominated by u on X.
   (ii) Pθ is non-decreasing, i.e. u ≤ v ⇒ Pθ (u) ≤ Pθ (v).
  (iii) Pθ (u) is concave in both arguments, in the sense that
                      Ptθ+(1−t)θ0 tu + (1 − t)u0 ≥ tPθ (u) + (1 − t)Pθ0 (u0 )
                                                

           for 0 ≤ t ≤ 1.
      (iv) For each c ∈ R we have Pθ (u + c) = Pθ (u) + c.
       (v) For each v ∈ D(X) we have Pθ (u) = Pθ+ddc v (u − v) + v.
      (vi) Pθ is 1-Lipschitz continuous with respect to the sup-norm, i.e. supX |Pθ (u)−Pθ (v)| ≤
           supX |u − v|.
     (vii) Given a determination X of θ and a convergent sequence θm → θ in N 1 (X /S), we
           have Pθm (u) → Pθ (u) uniformly on X.
Proof. (i) The only thing to show is that Pθ (u) is θ-psh. Since Pθ (u) ≤ u and u is contin-
uous, it follows that the usc regularization satisfies Pθ (u)∗ ≤ u. Now, Pθ (u)∗ is θ-psh by
Theorem 7.11, and is hence a competitor in the definition of Pθ (u). Thus Pθ (u) = Pθ (u)∗ is
indeed θ-psh.
    (ii) is trivial.
    (iii) follows from the fact that given ϕ ∈ PSH(X, θ), ϕ0 ∈ PSH(X, θ0 ) with ϕ ≤ u and
ϕ ≤ u0 , tϕ + (1 − t)ϕ0 belongs to PSH(X, tθ + (1 − t)θ0 ) and is dominated by tu + (1 − t)u0 .
  0

    (iv) and (v) are seen similarly.
    (vi) is a formal consequence of (ii) and (iv).
    (vii) By Proposition 5.2 we may assume, after perhaps passing to a higher model, that
there exists a model function v determined on X such that θ + ddc v is X -positive, i.e. deter-
mined by an ample class in N 1 (X /S). As a consequence, there exists an open neighborhood
V ⊂ N 1 (X /S) of θ such that τ + ddc v is X -positive for all τ ∈ V .
    We claim that Pτ (u) is uniformly bounded on X for τ ∈ V . Indeed for each τ ∈ V we
have R ⊂ PSH(X, τ + ddc v), hence Pτ +ddc v (u − v) ≥ inf X u − supX |v|. By (v) it follows
             SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                      37


that
                              inf u − 2 sup |v| ≤ Pτ (u) ≤ sup u,
                              X         X                  X
which proves the claim.
   Now for each x ∈ X the function τ 7→ Pτ (u)(x) is concave on V , hence locally Lipschitz
continuous on V , with local Lipschitz constant only depending on supτ ∈V |Pτ (u)(x)|, which
is in turn bounded independently of x ∈ X, and the result follows.                        
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


## 1201.0187-LF-1894-1955.txt


on X qm for m  1. As ϕm , Pθ (0) and ϕE are all θ-psh, Proposition 7.6 shows that this
inequality extends to all of X. Now ϕE is bounded and ϕm is uniformly bounded, as follows
from ϕ1 ≤ ϕm ≤ 0, so ϕm converges uniformly on X to Pθ (0), as was to be shown.        

     Let us end this subsection with a result that will be used in [BFJ12a].
Corollary 8.6. If ϕ ∈ PSH(X, θ) and v ∈ C 0 (X) are such that ϕ ≤ v then for every ε > 0
there exists an θ-psh model function ψ such that ϕ ≤ ψ ≤ v + ε.
Proof. We may assume ϕ = Pθ (v), in which case the result follows from Theorem 8.3.              
            SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                      39


8.2. Monotone regularization of θ-psh functions. By our definition, the set D(X) ∩
PSH(X, θ) of θ-psh model functions is dense in PSH(X, θ) with respect to its topology of
uniform convergence on dual complexes. This property may be seen as an analogue of the
fact that every θ-psh function is a L1 -limit of smooth θ-psh functions in the complex case,
which follows from the much more useful fact that every θ-psh function is a decreasing limit
of smooth θ-psh functions [Dem92]. The next result gives an analogue of this monotone
regularization theorem in our context.
Theorem 8.7. For each θ-psh function ϕ, there exists a decreasing net (ϕi )i∈I of θ-psh
model functions that converges pointwise on X to ϕ.
  One may hope that there is in fact a decreasing sequence (ϕm )∞
                                                                m=1 of θ-psh model functions
converging to ϕ. In the companion paper [BFJ12a], we will prove—using Theorem 8.7 and
capacity estimates—that this is indeed the case.
  As a consequence of Theorem 8.7, we get at any rate the following version of the Demailly-
Richberg regularization theorem.
Corollary 8.8. Every continuous θ-psh function ϕ is the uniform limit on X of a sequence
(ϕm )m∈N of θ-psh model functions.
Proof. By Theorem 8.7 there exists a decreasing net (ψj ) of θ-psh model functions converging
pointwise to ϕ. For each ε > 0 the compact set X is the increasing union of the open sets
{ψj < ϕ + ε}, hence ψj < ϕ + ε for some j (Dini’s lemma). It follows that ϕ lies in the
closure of D(X) ∩ PSH(X, θ) in C 0 (X) with respect to the topology of uniform convergence.
Since the latter is defined by a norm, the result follows.                                  
   The proof of Theorem 8.7 reduces immediately to Theorem 8.3, in view of the following
elementary result.
Lemma 8.9. The following properties are equivalent.
   (i) Every θ-psh function ϕ is the pointwise limit of a decreasing net of θ-psh model
       functions.
  (ii) For each u ∈ C 0 (X) we have
                  Pθ (u) = sup {ϕ | ϕ ∈ D(X) ∩ PSH(X, θ), ϕ ≤ u on X} .
  (iii) For each u ∈ C 0 (X) Pθ (u) is a uniform limit of θ-psh model functions.
Proof. (i)=⇒(ii). Let u ∈ C 0 (X). By (i) there exists a decreasing net (ϕj ) of θ-psh model
functions converging pointwise to Pθ (u). Since Pθ (u) ≤ u, we see that the compact set X
is for each ε > 0 the increasing union of the open sets {ϕj < u + ε}, hence ϕj < u + ε for
some j. Since ϕj − ε is θ-psh and dominated by u, we get ϕj − ε ≤ Pθ (u) by definition of
the envelope, which proves (ii).
   (ii)=⇒(iii). Since the set of ϕ ∈ D(X) ∩ PSH(X, θ) such that ϕ ≤ u is stable by max,
(ii) shows that we can construct an increasing family ϕj ∈ D(X) ∩ PSH(X, θ) converging
pointwise to Pθ (u). But Pθ (u) − ϕj is usc for each j, and Dini’s lemma therefore shows that
the convergence is uniform on X.
   (iii)=⇒(i). Let ϕ be a θ-psh function. We first claim that for each x ∈ X we have
                    ϕ(x) = inf {ψ(x) | ψ ∈ D(X) ∩ PSH(X, θ), ψ ≥ ϕ} .                   (8.2)
40              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


Indeed, given ε > 0 there exists u ∈ C 0 (X) such that u ≥ ϕ and u(x) ≤ ϕ(x) + ε, simply
because ϕ is usc. Since ϕ is θ-psh, the maximality property of envelopes implies ϕ ≤ Pθ (u).
By (iii) we may then find ψ ∈ D(X) ∩ PSH(X, θ) such that Pθ (u) ≤ ψ ≤ Pθ (u) + ε. We thus
have ψ ≥ ϕ and ψ(x) ≤ ϕ(x) + 2ε, and the claim follows.
  Now consider the set I of all ψ ∈ D(X) ∩ PSH(X, θ) such that ψ > ϕ on X. Note that
the latter condition implies that ψ ≥ ϕ + ε for some ε > 0, since ϕ − ψ is usc. We claim


## 1201.0187-LF-1900-1955.txt

Corollary 8.6. If ϕ ∈ PSH(X, θ) and v ∈ C 0 (X) are such that ϕ ≤ v then for every ε > 0
there exists an θ-psh model function ψ such that ϕ ≤ ψ ≤ v + ε.
Proof. We may assume ϕ = Pθ (v), in which case the result follows from Theorem 8.3.              
            SINGULAR SEMIPOSITIVE METRICS IN NON-ARCHIMEDEAN GEOMETRY                      39


8.2. Monotone regularization of θ-psh functions. By our definition, the set D(X) ∩
PSH(X, θ) of θ-psh model functions is dense in PSH(X, θ) with respect to its topology of
uniform convergence on dual complexes. This property may be seen as an analogue of the
fact that every θ-psh function is a L1 -limit of smooth θ-psh functions in the complex case,
which follows from the much more useful fact that every θ-psh function is a decreasing limit
of smooth θ-psh functions [Dem92]. The next result gives an analogue of this monotone
regularization theorem in our context.
Theorem 8.7. For each θ-psh function ϕ, there exists a decreasing net (ϕi )i∈I of θ-psh
model functions that converges pointwise on X to ϕ.
  One may hope that there is in fact a decreasing sequence (ϕm )∞
                                                                m=1 of θ-psh model functions
converging to ϕ. In the companion paper [BFJ12a], we will prove—using Theorem 8.7 and
capacity estimates—that this is indeed the case.
  As a consequence of Theorem 8.7, we get at any rate the following version of the Demailly-
Richberg regularization theorem.
Corollary 8.8. Every continuous θ-psh function ϕ is the uniform limit on X of a sequence
(ϕm )m∈N of θ-psh model functions.
Proof. By Theorem 8.7 there exists a decreasing net (ψj ) of θ-psh model functions converging
pointwise to ϕ. For each ε > 0 the compact set X is the increasing union of the open sets
{ψj < ϕ + ε}, hence ψj < ϕ + ε for some j (Dini’s lemma). It follows that ϕ lies in the
closure of D(X) ∩ PSH(X, θ) in C 0 (X) with respect to the topology of uniform convergence.
Since the latter is defined by a norm, the result follows.                                  
   The proof of Theorem 8.7 reduces immediately to Theorem 8.3, in view of the following
elementary result.
Lemma 8.9. The following properties are equivalent.
   (i) Every θ-psh function ϕ is the pointwise limit of a decreasing net of θ-psh model
       functions.
  (ii) For each u ∈ C 0 (X) we have
                  Pθ (u) = sup {ϕ | ϕ ∈ D(X) ∩ PSH(X, θ), ϕ ≤ u on X} .
  (iii) For each u ∈ C 0 (X) Pθ (u) is a uniform limit of θ-psh model functions.
Proof. (i)=⇒(ii). Let u ∈ C 0 (X). By (i) there exists a decreasing net (ϕj ) of θ-psh model
functions converging pointwise to Pθ (u). Since Pθ (u) ≤ u, we see that the compact set X
is for each ε > 0 the increasing union of the open sets {ϕj < u + ε}, hence ϕj < u + ε for
some j. Since ϕj − ε is θ-psh and dominated by u, we get ϕj − ε ≤ Pθ (u) by definition of
the envelope, which proves (ii).
   (ii)=⇒(iii). Since the set of ϕ ∈ D(X) ∩ PSH(X, θ) such that ϕ ≤ u is stable by max,
(ii) shows that we can construct an increasing family ϕj ∈ D(X) ∩ PSH(X, θ) converging
pointwise to Pθ (u). But Pθ (u) − ϕj is usc for each j, and Dini’s lemma therefore shows that
the convergence is uniform on X.
   (iii)=⇒(i). Let ϕ be a θ-psh function. We first claim that for each x ∈ X we have
                    ϕ(x) = inf {ψ(x) | ψ ∈ D(X) ∩ PSH(X, θ), ψ ≥ ϕ} .                   (8.2)
40              SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON


Indeed, given ε > 0 there exists u ∈ C 0 (X) such that u ≥ ϕ and u(x) ≤ ϕ(x) + ε, simply
because ϕ is usc. Since ϕ is θ-psh, the maximality property of envelopes implies ϕ ≤ Pθ (u).
By (iii) we may then find ψ ∈ D(X) ∩ PSH(X, θ) such that Pθ (u) ≤ ψ ≤ Pθ (u) + ε. We thus
have ψ ≥ ϕ and ψ(x) ≤ ϕ(x) + 2ε, and the claim follows.
  Now consider the set I of all ψ ∈ D(X) ∩ PSH(X, θ) such that ψ > ϕ on X. Note that
the latter condition implies that ψ ≥ ϕ + ε for some ε > 0, since ϕ − ψ is usc. We claim


## 1201.0188-LF-60-102.txt

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


## 1201.0188-LF-700-753.txt

Riesz representation theorem that Radon measures are in 1-1 correspondence with regular
Borel measures on X; see [Fol99, §7.1–2].
   Since we shall be dealing with (possibly uncountable) nets rather than sequences, one has
to be careful using results from integration theory. For example, the monotone convergence
theorem is of course not true for general nets. However, as the next results show, integration
of semicontinuous functions against Radon measures is often well behaved.
Lemma 2.23. [Fol99, Proposition 7.12]. If µ is a positive Radon measure on X and (fj )j
a decreasing
     R       Rnet of usc functions on X, converging pointwise to a (usc) function f , then
limj fj µ = f µ.
  In particular, one has
16                   SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

Lemma 2.24. [Fol99, Corollary 7.13]. If µ is a positive Radon measure on X and f is a
usc function on X, then
                        Z           Z                      
                                                        0
                          f µ = inf    gµ | f ≤ g, g ∈ C (X)

Corollary 2.25. Let (fj )j a decreasing net of usc functions on X converging pointwise to
a (usc) function f , and (µj )j a net of positive Radon measures on X converging weakly to
a positive Radon measure µ. Then
                                           Z         Z
                                   lim sup fj µj ≤ f µ.
                                                    j
                                 R
Proof. Upon replacing µj with ( µj )−1 µj we may assume that the µj ’s are probability
measures. RFix anyR ε > 0. By Lemma 2.24 there exists a continuous function g ≥ f on X
such that gµ < f µ + ε. By Dini’s lemma, we have fj < g + ε for all j ≫ 1, hence
                       Z              Z           Z           Z
               lim sup fj µj ≤ lim sup gµj + ε = gµ + ε ≤ f µ + 2ε.
                           j                    j
         R           R
since        gµj →       gµ by the deﬁnition of weak convergence. The result follows.                               

                         3. Monge-Ampère operator on bounded functions
  From now on we ﬁx a form θ ∈ Z 1,1 (X) whose de Rham class {θ} ∈ N 1 (X) is ample.
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


## 1201.0188-LF-700-765.txt

Riesz representation theorem that Radon measures are in 1-1 correspondence with regular
Borel measures on X; see [Fol99, §7.1–2].
   Since we shall be dealing with (possibly uncountable) nets rather than sequences, one has
to be careful using results from integration theory. For example, the monotone convergence
theorem is of course not true for general nets. However, as the next results show, integration
of semicontinuous functions against Radon measures is often well behaved.
Lemma 2.23. [Fol99, Proposition 7.12]. If µ is a positive Radon measure on X and (fj )j
a decreasing
     R       Rnet of usc functions on X, converging pointwise to a (usc) function f , then
limj fj µ = f µ.
  In particular, one has
16                   SÉBASTIEN BOUCKSOM, CHARLES FAVRE, AND MATTIAS JONSSON

Lemma 2.24. [Fol99, Corollary 7.13]. If µ is a positive Radon measure on X and f is a
usc function on X, then
                        Z           Z                      
                                                        0
                          f µ = inf    gµ | f ≤ g, g ∈ C (X)

Corollary 2.25. Let (fj )j a decreasing net of usc functions on X converging pointwise to
a (usc) function f , and (µj )j a net of positive Radon measures on X converging weakly to
a positive Radon measure µ. Then
                                           Z         Z
                                   lim sup fj µj ≤ f µ.
                                                    j
                                 R
Proof. Upon replacing µj with ( µj )−1 µj we may assume that the µj ’s are probability
measures. RFix anyR ε > 0. By Lemma 2.24 there exists a continuous function g ≥ f on X
such that gµ < f µ + ε. By Dini’s lemma, we have fj < g + ε for all j ≫ 1, hence
                       Z              Z           Z           Z
               lim sup fj µj ≤ lim sup gµj + ε = gµ + ε ≤ f µ + 2ε.
                           j                    j
         R           R
since        gµj →       gµ by the deﬁnition of weak convergence. The result follows.                               

                         3. Monge-Ampère operator on bounded functions
  From now on we ﬁx a form θ ∈ Z 1,1 (X) whose de Rham class {θ} ∈ N 1 (X) is ample.
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


## 1201.0188-LF-1190-1401.txt


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
In order to circumvent this diﬃculty, we show as in [BB10] the diﬀerentiability of Eω ◦ Pω ,


## 1201.0188-LF-1190-1411.txt


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


## 1201.0188-LF-1402-1460.txt

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


## 1201.0188-LF-1412-1460.txt

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


## 1201.0188-LF-1540-1685.txt


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



## 1201.0188-LF-1544-1685.txt

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



## 1805.01016-LF-125-170.txt

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



## 1805.01016-LF-2281-2308.txt

     In view of Theorem 7.1, it is natural to introduce as in [BJ18a]:
Definition 7.2. Assume that K is non-Archimedean, and let L be a semiample Q-line
bundle. We say that a (possibly singular) metric φ on L is plurisubharmonic ( psh for short)
if φ can be written as the pointwise limit of a decreasing net φi ∈ FS(L) of Fubini–Study
metrics on L. We denote by PSH(L) the set of psh metrics on L.
   Given a subgroup Γ ⊂ R, nontrivial if K is trivially valued, FSΓ (L) is dense in FS(L)
with respect to uniform convergence, by Proposition 5.4 (v); it would thus be equivalent to
require φi ∈ FSΓ (L) in the above definition.
  As a direct consequence of Corollary 5.7, we have:
Lemma 7.3. Let A be the Stein factorization of L. Then
                               PSH(A) ≃ PSH(L) ≃ PSH(Lred ).
   The following general result, borrowed from [BJ18a, Proposition 5.6], ensures that PSH(L)
is closed under decreasing limits.
Lemma 7.4. Let F ⊂ C0 (L) be a family of continuous metrics on a Q-line bundle L, closed
under addition of a constant, and define Fe as the set of possibly singular metrics on L that
can be written as decreasing limits of nets in F. Then Fe is closed under decreasing limits.
                                           e For each i ∈ I choose a decreasing net (φi,j )j∈J
Proof. Let (φi )i∈I be a decreasing net in F.                                                  i
in F converging to φi . Let A be the set of triples α = (i, j, m) with i ∈ I, j ∈ Ji and
m ∈ Z>0 . For each α = (i, j, m) in A, set
                                     ψα := φi,j + m−1 ∈ F,
and define a partial order on A by
                                     α ≥ α′ ⇐⇒ ψα ≤ ψα′ .
We claim that A is directed, i.e. any two elements a1 = (i1 , j1 , m1 ), a2 = (i2 , j2 , m2 ) in
A can be dominated by a third. To see this, first pick i ≥ i1 , i2 , so that φi ≤ φi1 and
φi ≤ φi2 , and set m := max{m1 , m2 } + 1. A simple variant of Dini’s lemma shows that
φi,j + m−1 ≤ φik ,jk + m−1
                         k = ψak on X


## 1805.01016-LF-2550-2586.txt

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
a semiample Q-line bundle L over X. Pick a complete field extension F/K, and denote φF
the pullback of φ to LF . Then φ is psh iff φF is psh.
Proof. By definition, the pullback of a Fubini–Study metric on L is a Fubini–Study metric on


## 1805.01016-LF-2611-2761.txt

                  8. Monge–Ampère measures and Deligne pairings
   In this section, we review some basic properties of Monge–Ampère operators, and use them
to define metrics on Deligne pairings (Theorem 8.16), following Deligne’s program [Del87].
In what follows, X is as before an n-dimensional projective scheme over a complete valued
field K.
8.1. Mixed Monge–Ampère measures. The (algebraic) fundamental class of X is the
n-dimensional cycle               X
                            [X] =   mα [Xα ],
                                                     α
where the Xα denote the n-dimensional irreducible components of X (with their reduced
structure) and mα is the length of the local ring of X at the generic point of Xα . The
intersection number of Q-line bundles L1 , . . . , Ln on X is defined as
                      (L1 · . . . · Ln ) := deg π⋆ (c1 (L1 ) · . . . · c1 (Ln ) · [X]) ,
with π : X → Spec K the structure morphism.
  Now let φ1 , . . . , φn be smooth metrics on L1 , . . . , Ln , and recall that ddc φi denotes the
curvature form of φi , a smooth, closed (1, 1)-form on X an (cf. [CLD12, §6.4.1] for the non-
Archimedean case). The smooth (n, n)-form ddc φ1 ∧. . .∧ddc φn determines a Radon measure
                                               X
                ddc φ1 ∧ . . . ∧ ddc φn ∧ δX =   mα ddc φ1 ∧ . . . ∧ ddc φn ∧ δXα             (8.1)
                                       α
                          an
on the topological space X , the mixed Monge–Ampère measure     of the φi , with δX =
P
  α m  δ
      α Xα denoting the analytic fundamental class of X (see [CLD12,  §3.7] for the non-
Archimedean case).
Remark 8.1. When K = R, we define ddc φ1 ∧ . . . ∧ ddc φn ∧ δX as the image of the
corresponding measure on X(C) = XCan by the projection map XCan → X an .
Example 8.2. Assume that n = 0, i.e. X = Spec A with A a finite K-algebra. The pre-
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


## 1801.08229-LF-102-206.txt

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
which itself is a version of the celebrated result of Yau [Yau78] and a later version by
Kolodziej [Kol98]. In the non-Archimedean setting, earlier results include [Liu11, BFJ15,
YZ17].
            GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD                       5

  Theorem A actually brings together several main steps, of various flavors, that we now


## 1801.08229-LF-2797-2828.txt

5.2. The envelope property and unibranch varieties. In the rest of §4 we assume that
X is irreducible unless stated otherwise. (See Remark 5.15.)
Definition 5.8. We say that a class θ ∈ N1 (X) has the envelope property if, for any
bounded-above family (ϕi ) in PSH(θ), the usc upper envelope sup?i ϕi is θ-psh.
   In the complex analytic case, it is a basic fact that psh functions on domains in Cn
satisfy the analogue of the envelope property. As a consequence, θ-psh functions satisfy the
envelope property for any projective complex manifold X and any closed (1, 1)-form θ. More
generally, the latter property holds when X is unibranch (i.e. locally analytically irreducible),
cf. [Dem85, Théorème 1.7], but fails in general, for the same reason as Theorem 5.12 below.
   With our global definition of θ-psh functions, the envelope property turns out to be
especially delicate. The purpose of what follows is to explore various implications, and
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


## 1801.08229-LF-2894-2928.txt

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


## 1801.08229-LF-2977-3064.txt

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


## 1801.08229-LF-3650-3717.txt

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


## 1801.08229-LF-3977-4067.txt

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


## 1801.08229-LF-4212-4251.txt

                                                          I(ϕ, ψ),                     (7.31)
which can be seen as a strict concavity property of E with respect to I. Indeed, it yields the
following uniform concavity estimate:
Theorem 7.28. For any two ϕ, ψ ∈ E 1 and t ∈ [0, 1] we have
                E((1 − t)ϕ + tψ) − ((1 − t) E(ϕ) + t E(ψ)) & t(1 − t) I(ϕ, ψ).
  The proof relies on the following elementary estimate, which is certainly well-known.
Lemma 7.29. For all a, b ∈ R≥0 and t ∈ [0, 1] we have (1 − t)a + tb ≥ t(1 − t)(a + b).
86                           SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. By homogeneity we may assume a + b = 1. Write t = 21 + x and a = 12 + y with
x, y ∈ [− 12 , 21 ], where we may assume x ≥ 0, by symmetry. Then
              1      1        1      1     1                    1    1       1
(1−t)a+tb = ( −x)( +y)+( +x)( −y) = −2xy, t(1−t)(a+b) = ( +x)( −x) = −x2 ,
              2      2        2      2     2                    2    2       4
and hence
                                       1            1 1           1
      (1 − t)a + tb − t(1 − t)(a + b) = − 2xy + x2 ≥ − x + x2 = ( − x)2 ≥ 0.
                                       4            4 2           2
                                                                               

Proof of Theorem 7.28. Set ϕt := (1 − t)ϕ + tψ. By (7.31), we have
                              ˆ
                      E(ϕt ) + (ϕ − ϕt ) MA(ϕt ) − E(ϕ) & I(ϕ, ϕt )

and                                    ˆ
                            E(ϕt ) +       (ψ − ϕt ) MA(ϕt ) − E(ψ) & I(ϕt , ψ),

Since (1 − t)(ϕ − ϕt ) + t(ψ − ϕt ) = 0, this yields
                    E(ϕt ) − ((1 − t) E(ϕ) + t E(ψ)) & (1 − t) I(ϕ, ϕt ) + t I(ψ, ϕt )

                           ≥ t(1 − t) (I(ϕ, ϕt ) + I(ϕt , ψ)) & t(1 − t) I(ϕ, ψ),
by Lemma 7.29 and (7.30).                                                                                             

  For later use, we record the following crucial consequence of Corollary 3.34 (compare [BBGZ13,
Lemma 3.13]).
Lemma 7.30. For all ϕ, ϕ0 , ψ, ψ 0 ∈ E 1 we have
  ˆ
                                                        1                                  1
    (ϕ − ϕ0 ) MA(ψ) − MA(ψ 0 ) . I(ϕ, ϕ0 )αn I(ψ, ψ 0 ) 2 max{J(ϕ), J(ϕ0 ), J(ψ), J(ψ 0 )} 2 −αn
                               


## 1801.08229-LF-4529-4605.txt

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


## 1801.08229-LF-4840-4874.txt

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
any ϕ ∈ CPSH(ω) we then have
                               ˆ
                            −1
                                                           n
                                 f ω + ω 0 + ddc (ϕ + ψ1 )    ≤ Vω−1 Vω+ω0 − 1 sup |f |.
                                                                              
    Eω (ϕ + f ) − Eω (ϕ) − Vω

Proof. We may assume ω = c1 (L), ω 0 = c1 (L0 ) for ample line bundles L, L0 on X, Indeed, by
homogeneity, we then obtain the case when L, L0 are ample Q-line bundles, and the general


## 1801.08229-LF-4964-5024.txt

                                       9. Measures of finite energy
   Denote as above by X a projective variety of dimension n, and fix an ample class ω ∈
Amp(X). We define the Monge–Ampère energy of a probability measure on X an , and begin
a study of the space of measures of finite energy.
100                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

9.1. The energy of a measure. Denote by M = M(X) the space of Radon probability
measures on X an . It is a compact convex subset of the dual C0 (X)∨ for the weak topology.
Fix a class ω ∈ Amp(X).
Definition 9.1. The energy of a Radon probability measure µ ∈ M is defined by
                                                 ˆ     
                  E∨ (µ) := E∨
                             ω (µ) := sup  E(ϕ) −   ϕ µ   ∈ [0, +∞].                       (9.1)
                                                  ϕ∈E 1

We say that µ has finite energy if E∨ (µ) < +∞, and denote by M1 ⊂ M the set of such
measures.
   Here we write E 1 = E 1 (ω) for simplicity. As we shall see, measures in M1 = M1 (ω) have
a prescribed mass on each Xαan , determined by ω (see Corollary 9.13). However, when X is
irreducible, M1 turns out to be independent of ω ∈ Amp(X) cf. Theorem 9.24 below.
   By definition, measures of finite energy integrate all functions in E 1 . Combined with
Corollary 7.48, this implies:
Lemma 9.2. Measures in M1 put no mass on pluripolar sets.
  We will later study the dependence Amp(X) 3 ω → E∨    ω (µ) for a fixed measure µ ∈ M.
Already now, we note that Proposition 7.7 (iii) implies
Lemma 9.3. For ω ∈ Amp(X), t ∈ R>0 and µ ∈ M, we have E∨           ∨
                                                       tω (µ) = t Eω (µ).

Proposition 9.4. The energy functional E∨ : M → [0, +∞] satisfies:
      (i) for each µ ∈ M we have
                                                                ˆ   
                                     ∨
                                 E (µ) =          sup      E(ϕ) − ϕ µ ;                    (9.2)
                                            ϕ∈Hdom (ω)

      (ii) E∨ is convex, lsc, and homogeneous with respect to the scaling action of R>0 , i.e.
                                            E∨ (t? µ) = t E∨ (µ)
          for all µ ∈ M and t ∈ R>0 ;
Proof. Denote by S ∈ [0, +∞] the right-hand side of (9.2). Trivially, E∨ (µ) ≥ S. Conversely
pick ϕ ∈ E 1 , and choose a decreasing net (ϕj ) in Hdom (ω) such that ϕj → ϕ. Then
E(ϕ) ≤ E(ϕj ), and hence
                 ˆ                 ˆ       ˆ                        ˆ
         E(ϕ) − ϕ µ ≤ E(ϕj ) − ϕj µ + (ϕj − ϕ)µ ≤ S + (ϕj − ϕ)µ.
                    ´            ´
By Lemma 7.17,          ϕj µ →       ϕ µ; hence
                                                   ˆ   
                                     ∨        ∨
                                 E (µ) = sup E (ϕ) − ϕ µ ≤ S,
                                            ϕ∈E 1

which proves (i).                                                                      ´
   Convexity and lower semicontinuity of E∨ follow directly from (i), since µ 7→ E(ϕ) − ϕ µ
is affine and continuous for every ϕ ∈ PL ∩ PSH(ω). Now pick µ ∈ M and t ∈ R>0 . Note
             GLOBAL PLURIPOTENTIAL THEORY OVER A TRIVIALLY VALUED FIELD              101

that ϕ 7→ t · ϕ = tϕ(t−1 ·) is a bijection of E 1 . By Proposition 7.7 we infer
                                ˆ             
  E∨ (t? µ) = sup E(t · ϕ) − (t · ϕ)(t? µ)
               ϕ∈E 1
                                          ˆ                ˆ  
                             = sup t E(ϕ) − tϕµ = t sup E(ϕ) − ϕµ = t E∨ (µ),


## 1801.08229-LF-5182-5314.txt

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
C > 0 such that ϕ µ ≥ −C for all ϕ ∈ Esup   1  such that − E(ϕ) = J(ϕ) ≤ C. Arguing by
contradiction, we may assume there exist C > 0 and a sequence (ϕj )∞          1
                                                                      1 in Esup such that
                ´          j
                                                    Pm −j
J(ϕ) ≤ C and ϕj µ ≤ −2 for all j. Set ψm := j=1 2 ϕj for m ≥ 1. Then ψm is a
decreasing sequence in PSH(ω) converging to ψ := ∞          −j
                                                    P
                                                      j=1 2 ϕj , which is thus either ω-psh
or identically −∞ (since X is irreducible). By concavity of E we have E(ψm ) ≥ −C for all
m; hence ψ is ω-psh, with E(ψ) = limm→∞ E(ψm ) ≥ −C. On the other hand, monotone
convergence gives
                   ˆ              ˆ               m
                                                  X       ˆ
                     ψ µ = lim      ψm µ = lim        2−j ϕj µ = −∞,
                               m→∞                  m→∞
                                                          j=1
a contradiction. We next claim that there exist A, B > 0 such that
                                 ˆ
                                    ϕ µ ≤ A J(ϕ)1/2 + B
             1 , which will imply, as desired, that
for all ϕ ∈ Esup
                                              ˆ      
                              ∨
                             E (µ) = sup − ϕ µ − J(ϕ)
                                              1
                                           ϕ∈Esup
106                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

is finite. If J(ϕ) ≤ 1 then the estimate follows from the first part of the proof. We may
thus assume t := J(ϕ)−1/2 ≤ 1. By Lemma 7.33, J(tϕ) ´. t2 J(ϕ) = 1, and the first part of
the proof yields a uniform constant A > 0 such that t ϕ µ ≤ A, which gives the desired
estimate.                                                                              
  As in [DiN16, Proposition 4.1], we infer:
Corollary 9.21. The set M1 (ω) of measures of finite energy is independent of the choice
of ω ∈ Amp(X), and it is dense in the space M of all Radon probability measures on X an .
Proof. For any ω, ω 0 ∈ Amp(X), we can find s  1 such that s−1 ω ≤ ω 0 ≤ sω. By
Theorem 7.8 we then have s−1 E 1 (ω) ⊂ E 1 (ω 0 ) ⊂ s E 1 (ω), and µ is thus finite on E 1 (ω) iff it
is finite on E 1 (ω 0 ). We conclude by Theorem 9.20 that M1 (ω) is independent of ω.
   For the second part, we note that finite atomic measures are dense in M. As X div is dense
in X an , finite atomic measures with support in X div are also dense in M, and Theorem 9.20
shows that any such measure has finite energy. Indeed, any function in PSH(ω) is finite on
X div .                                                                                            
Remark 9.22. In view of Corollary 9.13, the above results fail when X has more than one
top-dimensional component.
  By Proposition 7.19 (v) and Theorem 9.20, we also have:


## 1801.08229-LF-6080-6148.txt

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


## 2307.01697-LF-89-166.txt

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
to the seminegative form (0.1). This approach, which goes back to [Blo03] and was further
exploited in [BBGZ13, BBEGZ19, BoJ22a], is put in a simple general setting in Appendix A.



## 2307.01697-LF-346-386.txt

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



## 2307.01697-LF-508-532.txt

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


## 2307.01697-LF-677-705.txt

irreducible (see Theorem 1.26 below).
Lemma 1.25. Pick τ ∈ Dω , and ω ′ ∈ Z+ commensurable to ω. Then
                                        Tωτ ≤ Tω + (n + 2) sup |τ |                                  (1.22)
and
                                               Tω′ ≤ eO(δ) Tω                                        (1.23)
with δ := dT (ω, ω ′ ).
     Recall that, in this paper, the implicit constant in O only depends on n (see §1.1).
                                  MEASURES OF FINITE ENERGY                                       15

Proof. Pick φ ∈ Dωτ . Then φ + τ ∈ Dω , and the Chern–Levine–Nirenberg inequality (1.19)
yields            ˆ                         ˆ
           φ+τ ≤       (φ + τ ) MAω (0) + Tω ≤          (φ + τ ) MAω (τ ) + n sup |τ | + Tω .
This proves (1.22), in view of (1.18).
  For each t > 0 we have Dtω = tDω , and hence Ttω = tTω . Further, ω ′ ≤ ω implies
Dω′ ⊂ Dω and
                                Vω′ µω′ = (ω ′ )n ≤ ω n = Vω µω ,
and hence Vω′ Tω′ ≤ Vω Tω . These properties imply (1.23).                       □
Proof of Proposition 1.23. The condition Tω < ∞ only depends on the commensurability
class of ω, by (1.23), and it only depends on [ω] ∈ Pos(X), by (1.22). This condition is thus
independent of ω, since any two classes in Pos(X) admit commensurable representatives
(see Proposition 1.15).                                                                    □
Theorem 1.26. Assume X is either a compact Kähler space or a projective Berkovich space
over a non-Archimedean field k. Then the submean value property holds iff X is irreducible.
Lemma 1.27. Let a ⊂ OX be a coherent ideal sheaf. Then we can find ω ∈ Z+ with
[ω] ∈ Pos(X) and a decreasing sequence (φj )j in Dω such that, for any given choice of
local generators (fα ) of a near a point of X, φj − max{log maxα |fα |, −j} is locally bounded
uniformly with respect to j.
Proof. Assume first X is compact Kähler. Pick a finite open cover (Ui ) of X on which a is
generated by a finite subset (fiα )α of O(Ui ). Set


## 2307.01697-LF-677-753.txt

irreducible (see Theorem 1.26 below).
Lemma 1.25. Pick τ ∈ Dω , and ω ′ ∈ Z+ commensurable to ω. Then
                                        Tωτ ≤ Tω + (n + 2) sup |τ |                                  (1.22)
and
                                               Tω′ ≤ eO(δ) Tω                                        (1.23)
with δ := dT (ω, ω ′ ).
     Recall that, in this paper, the implicit constant in O only depends on n (see §1.1).
                                  MEASURES OF FINITE ENERGY                                       15

Proof. Pick φ ∈ Dωτ . Then φ + τ ∈ Dω , and the Chern–Levine–Nirenberg inequality (1.19)
yields            ˆ                         ˆ
           φ+τ ≤       (φ + τ ) MAω (0) + Tω ≤          (φ + τ ) MAω (τ ) + n sup |τ | + Tω .
This proves (1.22), in view of (1.18).
  For each t > 0 we have Dtω = tDω , and hence Ttω = tTω . Further, ω ′ ≤ ω implies
Dω′ ⊂ Dω and
                                Vω′ µω′ = (ω ′ )n ≤ ω n = Vω µω ,
and hence Vω′ Tω′ ≤ Vω Tω . These properties imply (1.23).                       □
Proof of Proposition 1.23. The condition Tω < ∞ only depends on the commensurability
class of ω, by (1.23), and it only depends on [ω] ∈ Pos(X), by (1.22). This condition is thus
independent of ω, since any two classes in Pos(X) admit commensurable representatives
(see Proposition 1.15).                                                                    □
Theorem 1.26. Assume X is either a compact Kähler space or a projective Berkovich space
over a non-Archimedean field k. Then the submean value property holds iff X is irreducible.
Lemma 1.27. Let a ⊂ OX be a coherent ideal sheaf. Then we can find ω ∈ Z+ with
[ω] ∈ Pos(X) and a decreasing sequence (φj )j in Dω such that, for any given choice of
local generators (fα ) of a near a point of X, φj − max{log maxα |fα |, −j} is locally bounded
uniformly with respect to j.
Proof. Assume first X is compact Kähler. Pick a finite open cover (Ui ) of X on which a is
generated by a finite subset (fiα )α of O(Ui ). Set
                                             X
                               φij := 21 log(    |fiα |2 + e−2j ),
                                                α
and observe that, for all i, k, |φij − φkj | is uniformly bounded with respect to j on each
compact subset of Ui ∩ Uk . Now choose a partition of unity subordinate to (Ui ), of the form
(χ2i ) with χi ∈ Cc∞ (Ui ), and set
                                                X
                                     φj := log      χ2i eφij .
                                                    i
As in [Dem92, Lemma 3.5], we find a Kähler form ω such that ddc φj ≥ −ω for all j, and
the result follows.
  Assume now X is a projective Berkovich space. Pick an ample line bundle L such that
L ⊗ a is generated by global sections (sα ), and choose a PL metric on L with curvature form
ω ∈ Z+ . Then setting φj := max{log maxα |sα |, −j} yields the result.                     □
Proof of Theorem 1.26. Assume first that the submean value property holds, and pick an
n-dimensional irreducible component Y of X. Applying Lemma 1.27 to the ideal sheaf
of Y in X yields ω ∈ Z+ with [ω] ∈ Pos(X) and a decreasing sequence (φj ) in Dω such
´ nsupY φnj → −∞ while (φj )´is uniformly bounded on compact subsets of X \ Y . Since
that
 Y ω = [ω] · [Y ] > 0, we get         φj µω → −∞, and hence sup φj → −∞, by the submean
value property. It follows that X = Y is irreducible.
   Conversely, assume X is irreducible. In the Kähler case, pick a Kähler form ω on X,
and choose a resolution of singularities π : X ′ → X with X ′ a connected compact Kähler
manifold, and pick a Kähler form ω ′ on X ′ such that ω ′ ≥ π ⋆ ω. Since µ := Vω−1 π ⋆ ω n = f ω ′n
satisfies PSH(X ′ , ω ′ ) ⊂ L1 (µ), [GZ05, Proposition 2.7] yields C > 0 such that supX ′ ψ ≤
16                       SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON
´
  ψ µ + C for all ψ ∈ PSH(X ′ , ω ′ ). Applying this to ψ = π ⋆ φ with φ ∈ Dω yields the
submean value property.
   In the non-Archimedean case, pick an ample line bundle L and a PL metric on L deter-
mined by an ample model/test configuration (X , L) of (X, L), with curvature form ω ∈ Z+ .
Each φ ∈ Dω satisfies sup φ = maxΓ φ, where Γ ⊂ X is the (finite) set of Shilov points
attached to X (see [GM16, Proposition 4.22] or [BE21, Lemma 6.3]). On the other hand, Γ
is also the support of µω , by definition of the measure ω n in terms of intersection numbers.
Now [BoJ18a, Theorem 2.21] yields C > 0 such    ´ that |φ(x) − φ(y)| ≤ C for all x, y ∈ Γ and
all φ ∈ Dω , and we infer, as desired, sup φ ≤ φ µω + C for all φ ∈ Dω .                    □
1.6. Monge–Ampère energy and the Dirichlet functional. From now on we fix ω ∈
Z+ with [ω] ∈ Pos(X).
Definition 1.28. The Monge–Ampère energy Eω : D → R is defined by
                                                  (ω, φ)n+1
                                    Eω (φ) :=               .                             (1.24)
                                                  (n + 1)Vω
     For all φ, ψ ∈ D we have
                                              n         ˆ
                                         1 X −1
                      Eω (φ) − Eω (ψ) =     Vω              (φ − ψ) ωφj ∧ ωψn−j .         (1.25)
                                        n+1
                                             j=0


## 2307.01697-LF-800-839.txt

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



## 2307.01697-LF-850-923.txt

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
                                 M1ω := {µ ∈ M | Jω (µ) < ∞}.
It is endowed with the strong topology, defined as the coarsest refinement of the weak topology
in which Jω : M1ω → R≥0 becomes continuous.
   In other words, a net (µi ) converges strongly to µ in M1ω iff µi → µ weakly in M and
Jω (µi ) → Jω (µ). For any R > 0 we also set
                                M1ω,R := {µ ∈ M1ω | Jω (µ) ≤ R}.                         (2.10)
By Proposition 2.2, this set is convex and weakly compact. By (2.4),
                                      Jω (·, ψ) : M1ω → R≥0
20                        SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON


## 2307.01697-LF-1020-1047.txt

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



## 2307.01697-LF-1055-1134.txt

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
  As a key consequence of Proposition 2.19, we show:
Theorem 2.23. Assume ω has the orthogonality property. Pick µ ∈ M1ω and a maximizing
sequence ψi ∈ Dω . Then the measures µi := MAω (ψi ) converge strongly to µ in M1ω , i.e.
µi → µ weakly and Jω (µi ) → Jω (µ). In particular, the image of the Monge–Ampère operator
                                        MAω : Dω → M1ω
is dense in the strong topology.
Proof. Pick f ∈ D, and choose C > 0 such that f = f + − f − with f ± ∈ DCω . Since we
assume orthogonality, Proposition 2.19 yields A > 0 such that
                                                  ˆ


## 2307.01697-LF-1115-1168.txt

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


## 2307.01697-LF-1127-1245.txt

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

                 |Jω (µ, ψi ) − Jω (µ, ψj )| ≲ Jω (ψi , ψj )α R1−α
                                           ≲ max{Jω (ν, ψi ), Jω (ν, ψj )}α R1−α .
This estimate implies that (Jω (µ, ψi )) is a Cauchy sequence, which thus admits a limit
                                    δω (µ, ν) := lim Jω (µ, ψi ).                       (2.28)
                                                   i

The same estimate also shows that the limit is independent of the choice of maximizing
sequence (ψi ), and that the convergence in (2.28) is uniform with respect to µ ∈ M1ω,R . As
a consequence, µ 7→ δω (µ, ν) so defined is continuous on M1ω for each ν ∈ M1ω .
   By construction, (2.22) holds, and hence also (2.21), by (2.5). This proves (i).
   Next, (2.24) holds when ν, ν ′ lie in the image of MAω : Dω → M1ω , by applying (2.26) to
a maximizing sequence for µ′ , and the general case follows by using maximizing sequences
for ν, ν ′ . This shows (iii), which also yields the continuity of δω on M1ω × M1ω (and hence
conclude the proof of existence), since µi → µ strongly implies δω (µi , µ) → δω (µ, µ) = 0, by
continuity of δω (·, µ).
   Similarly, (iv) follows follows by applying (2.27) to a maximizing sequence (τi ) for ν.
   Finally, the first point in (ii) follows from (2.25), since Dω spans the dense subspace D of
  0
C (X) (see Corollary 1.13). By (1.34) and (1.35), the last two properties in (ii) hold when
the measures lie in the image of MAω , and hence in general, by continuity of δω .
                                                                                              □

  We next show:
Theorem 2.26. The quasi-metric space (M1ω , δω ) only depends on the class [ω]. It is
complete, and its topology coincides with the strong topology.
Lemma 2.27. For any ν ∈ M1 and R > 0, δω (·, ν) is weakly lsc on M1ω,R .
26                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. When ν = MAω (ψ) with ψ ∈ Dω , (2.22) yields δω (·, ν) = Jω (·, ψ), which is weakly
lsc on M1ω (see (2.1)). In the general case, pick a maximizing sequence (ψi ) for ν, and set
νi := MAω (ψi ). By (2.24), we have δω (µ, νi ) → δω (µ, ν) uniformly for µ ∈ M1ω,R , and the
result follows.                                                                            □

Proof of Theorem 2.26. We already know that M1ω only depends on [ω] (see Proposition 2.6).
Pick τ ∈ Dω , µ, ν ∈ M1ω = M1ωτ , and choose maximizing sequences (φi ), (ψi ) in Dωτ
for µ, ν, so that δωτ (µ, ν) = limi Jωτ (φi , ψi ). By (2.8), (φi + τ ) and (ψi + τ ) are maxi-
mizing sequences in Dω for µ, ν, and hence δω (µ, ν) = limi Jω (φi , ψi ). Now (1.39) yields
Jωτ (φi , ψi ) = Jω (φi + τ, ψi + τ ), which proves δωτ (µ, ν) = δω (µ, ν) and proves that δω only


## 2307.01697-LF-1169-1290.txt


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

                 |Jω (µ, ψi ) − Jω (µ, ψj )| ≲ Jω (ψi , ψj )α R1−α
                                           ≲ max{Jω (ν, ψi ), Jω (ν, ψj )}α R1−α .
This estimate implies that (Jω (µ, ψi )) is a Cauchy sequence, which thus admits a limit
                                    δω (µ, ν) := lim Jω (µ, ψi ).                       (2.28)
                                                   i

The same estimate also shows that the limit is independent of the choice of maximizing
sequence (ψi ), and that the convergence in (2.28) is uniform with respect to µ ∈ M1ω,R . As
a consequence, µ 7→ δω (µ, ν) so defined is continuous on M1ω for each ν ∈ M1ω .
   By construction, (2.22) holds, and hence also (2.21), by (2.5). This proves (i).
   Next, (2.24) holds when ν, ν ′ lie in the image of MAω : Dω → M1ω , by applying (2.26) to
a maximizing sequence for µ′ , and the general case follows by using maximizing sequences
for ν, ν ′ . This shows (iii), which also yields the continuity of δω on M1ω × M1ω (and hence
conclude the proof of existence), since µi → µ strongly implies δω (µi , µ) → δω (µ, µ) = 0, by
continuity of δω (·, µ).
   Similarly, (iv) follows follows by applying (2.27) to a maximizing sequence (τi ) for ν.
   Finally, the first point in (ii) follows from (2.25), since Dω spans the dense subspace D of
  0
C (X) (see Corollary 1.13). By (1.34) and (1.35), the last two properties in (ii) hold when
the measures lie in the image of MAω , and hence in general, by continuity of δω .
                                                                                              □

  We next show:
Theorem 2.26. The quasi-metric space (M1ω , δω ) only depends on the class [ω]. It is
complete, and its topology coincides with the strong topology.
Lemma 2.27. For any ν ∈ M1 and R > 0, δω (·, ν) is weakly lsc on M1ω,R .
26                         SÉBASTIEN BOUCKSOM AND MATTIAS JONSSON

Proof. When ν = MAω (ψ) with ψ ∈ Dω , (2.22) yields δω (·, ν) = Jω (·, ψ), which is weakly
lsc on M1ω (see (2.1)). In the general case, pick a maximizing sequence (ψi ) for ν, and set
νi := MAω (ψi ). By (2.24), we have δω (µ, νi ) → δω (µ, ν) uniformly for µ ∈ M1ω,R , and the
result follows.                                                                            □

Proof of Theorem 2.26. We already know that M1ω only depends on [ω] (see Proposition 2.6).
Pick τ ∈ Dω , µ, ν ∈ M1ω = M1ωτ , and choose maximizing sequences (φi ), (ψi ) in Dωτ
for µ, ν, so that δωτ (µ, ν) = limi Jωτ (φi , ψi ). By (2.8), (φi + τ ) and (ψi + τ ) are maxi-
mizing sequences in Dω for µ, ν, and hence δω (µ, ν) = limi Jω (φi , ψi ). Now (1.39) yields
Jωτ (φi , ψi ) = Jω (φi + τ, ψi + τ ), which proves δωτ (µ, ν) = δω (µ, ν) and proves that δω only
depends on [ω].
   We next show that the topology of (M1ω , δω ) is the strong topology, i.e. a net (µi ) converges
strongly to µ ∈ M1ω iff δω (µi , µ) → 0. When the latter holds, (2.25) implies µi → µ weakly
(since Dω spans the dense subspace D of C0 (X)), while (2.24) yields Jω (µi ) = Jω (µi , 0) →
Jω (µ). Thus µi → µ strongly, and the converse holds by strong continuity of δω .
   Finally, consider a Cauchy net (µi ) in (M1 , δω ). Then Jω (µi ) = δω (µi , µω ) is eventually
bounded. By weak compactness of M, we may assume, after passing to a subnet, that (µi )
admits a weak limit µ ∈ M. Since Jω is weakly lsc on M, we get Jω (µ) ≤ lim inf i Jω (µi ) <
+∞, i.e. µ ∈ M1 . It remains to show δω (µi , µ) → 0. To see this, pick ε > 0 and i0 such that
δω (µi , µj ) ≤ ε for all i, j ≥ i0 . Since Jω (µj ) is bounded and µj → µ weakly, Lemma 2.27
yields δω (µi , µ) ≤ lim inf j δω (µi , µj ) ≤ ε, and we are done.                               □

     To conclude this section, we show:
Proposition 2.28. For each ν ∈ M1ω , δω (·, ν) : M1ω → R≥0 is strictly convex, and we
further have the uniform convexity estimate
           (1 − t)δω (µ0 , ν) + tδω (µ1 , ν) − δω ((1 − t)µ0 + tµ1 , ν) ≳ t(1 − t)δω (µ0 , µ1 ).
for all µ0 , µ1 ∈ M1ω and t ∈ [0, 1].
Proof. By density of the image of MAω : Dω → M1ω and continuity of δω , we may assume
without loss ν = MAω (ψ) with ψ ∈ Dω , and hence δω (·, ν) = Jω (·, ψ). Set
                   Jt := (1 − t)Jω (µ0 , ψ) + tJω (µ1 , ψ),    µt := (1 − t)µ0 + tµ1 ,
and pick φ ∈ Dω . Applying (2.4) to µ0 and µ1 yields
                                  ˆ
           Jt = Eω (φ) − Eω (ψ) + (ψ − φ)µt + (1 − t)Jω (µ0 , φ) + tJω (µ1 , φ),

and hence
                                        ˆ
             Jt − Eω (φ) + Eω (ψ) +         (φ − ψ)µt ≥ t(1 − t)(Jω (µ0 , ψ) + Jω (µ1 , ψ)),

using the elementary estimate (1 − t)a + tb ≥ t(1 − t)(a + b) for a, b ≥ 0 (see for in-
stance [BoJ22a, Lemma 7.29]). By (2.23), this implies
                                       ˆ
                 Jt − Eω (φ) + Eω (ψ) + (φ − ψ)µt ≳ t(1 − t)δω (µ0 , µ1 ),

and taking the infimum over φ shows Jt − Jω (µt , ψ) ≳ t(1 − t) dω (µ0 , µ1 ), which concludes
the proof.                                                                                  □
                                 MEASURES OF FINITE ENERGY                                      27

2.7. An equivalent metric on M1 . As recalled in §1.1, the quasi-metric space (M1ω , δω )
is metrizable, by general theory. Here we introduce a concrete metric that define the strong
topology of M1ω . Recall from (1.33) that
                                 Dω,1 = {φ ∈ Dω | Jω (φ) ≤ 1}.
Proposition 2.29. Setting
                                                       ˆ
                                dω (µ, ν) := sup           φ(µ − ν)                        (2.29)
                                            φ∈Dω,1


## 2307.01697-LF-2314-2328.txt

          Amer. Math. Soc 135 (2007), 2089–2093. 45
[BE21]    S. Boucksom, D. Eriksson. Spaces of norms, determinant of cohomology and Fekete points in
          non-Archimedean geometry. Adv. Math. 378 (2021), Paper No. 107501, 124 pp. 3, 8, 11, 16, 21,
          23
[BFJ15]   S. Boucksom, C. Favre and M. Jonsson. Solution to a non-Archimedean Monge–Ampère equa-
          tion. J. Amer. Math. Soc. 28 (2015), 617–667. 2, 18, 22
[BFJ16a]  S. Boucksom, C. Favre and M. Jonsson. Singular semipositive metrics in non-Archimedean
          geometry. J. Algebraic Geom. 25 (2016), 77–139. 2, 8, 11, 21
[BG13]    S. Boucksom, V. Guedj. Regularizing properties of the Kähler–Ricci flow. In An Introduction to
          the Kähler–Ricci Flow. Lecture Notes in Mathematics 2086, 2013. 11
[BGM22]   S. Boucksom, W. Gubler, F. Martin. Differentiability of relative volumes over an arbitrary non-
          Archimedean field. Int. Math. Res. Not. IMRN 2022, no. 8, 6214–6242. 3, 23
[BHJ17]   S. Boucksom, T. Hisamoto and M. Jonsson. Uniform K-stability, Duistermaat–Heckman mea-
          sures and singularities of pairs. Ann. Inst. Fourier 67 (2017), 743–841. 8, 41
[BoJ17]   S. Boucksom and M. Jonsson. Tropical and non-Archimedean limits of degenerating families of


## 2209.04879-LF-1978-1997.txt

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


## 2209.04879-LF-2018-2029.txt

We now let K = k((t)) be a discretely-valued field of equicharacteristic zero. The following
result can be understood as an analog of Kołodziej’s result over K:
Theorem 4.7. ([BFJ15, thm. A], [BGGJ+ 20])
Let (X, L) be a smooth polarized variety over K. Let µ be a probability measure on X an ,
supported on the skeleton of an snc R-model of X. Then there exists a unique (up to an
additive constant) continuous, semi-positive metric φ on L satisying the non-archimedean
Monge-Ampère equation:
                                      MA(φ) = µ.
  The above theorem was proved when X is defined over the function field of a curve
over k in [BFJ15], and then extended to varieties over non-archimedean fields of residual
characteristic zero in [BGGJ+ 20].



## 2506.13548-LF-1-19.txt

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



## 2506.13548-LF-64-88.txt

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


## Thuillier-LF-5516-5527.txt

   Couplé au théorème 3.3.13 et au lemme 3.3.12, le théorème pré édent établit l'existen e de
potentiels pour les mesures de Radon positives (dans le as d'une ourbe non propre).
Corollaire 3.4.13.  Soit X une ourbe stri tement k -analytique lisse, onnexe et iso-
morphe à une omposante onnexe de l'intérieur d'un espa e k-anoïde ou à l'analytiée
d'une ourbe k-algébrique ane . L'appli ation
                                D0 (X) → D1 (X),     T 7→ ddc T
induit une bije tion de SH(X)/Γ(X, HX ) sur l'ensemble des mesures de Radon positives sur
l'espa e topologique lo alement ompa t |X|.

   Considérons maintenant une ourbe stri tement k-analytique propre et lisse X et spé iali-
sons e qui pré ède dans le as d'un ouvert onnexe Ω de X tel que ∂Ω soit une partie non
vide de I(X).


## Thuillier-LF-5676-5717.txt

   Quel que soit le fais eau inversible L sur X muni d'une métrique sous-harmonique (resp.
lisse) ||.||, il existe un et un seul ourant ρ de degré 1 sur X tel que, pour tout ouvert Ω ⊂ X
et toute se tion inversible s de L sur Ω, ρ|Ω = ddc log ||s|| (rappelons que la orrespondan e
Ω → D0 (Ω) est un fais eau sur X , proposition 3.3.6). Ce ourant, noté c1 (L, ||.||), est appelé
la ourbure du fais eau inversible métrisé (L, ||.||). C'est un ourant positif si (et seulement
si) la métrique est sous-harmonique, une forme lisse si (et seulement si) la métrique est lisse.
  Il est maintenant possible d'énon er l'analogue du orollaire 3.4.13.
Corollaire 3.4.18.  Il existe, pour toute mesure de Radon positive µ sur une            ourbe
stri tement k-analytique propre et lisse X , un fais eau inversible L sur X muni d'une métrique
sous-harmonique ||.|| et un nombre réel positif λ tels que
                                          µ = λc1 (L, ||.||).
Démonstration. Considérons un point x ∈ X tel que [κ(x) : k] < ∞ et soit L le fais eau
inversible ample OX ([x]). Étant donnée une mesure de probabilité µ sur X , le théorème 3.3.13
fournit un ourant g ∈ D0 (X), uniquement déterminé à l'addition d'une onstante près, tel
que
                                    ddc g = [κ(x) : k]µ − δ[x] .
Il existe alors, en vertu de la formule de Poin aré-Lelong (proposition 3.3.15) une unique
métrique sous-harmonique ||.|| sur le fais eau inversible L telle que

                                         − log ||1[x] || = g;

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


## Berkovich-LF-1-10.txt

P UBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.




 V LADIMIR G. B ERKOVICH
 Étale cohomology for non-Archimedean analytic spaces
 Publications mathématiques de l’I.H.É.S., tome 78 (1993), p. 5-161
 <http://www.numdam.org/item?id=PMIHES_1993__78__5_0>



## Berkovich-LF-30-45.txt



                                                                                CONTENTS


INTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   7

§ 1. Analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   13
        1.1. Underlying topolcgical s p a c e s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            13
        1.2. The category of analytic spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     14
        1.3. Analytic domains and G-topology on an analytic space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          23
        1.4. Fibre products and the ground field extension functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       29
        1.5. Analytic spaces from [Ber] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                31
        1.6. Connection with rigid analytic geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             35

§ 2. Local rings and residue fields of points of affinoid s p a c e s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  38


## 1204.6277-LF-1-29.txt

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
TABLE DES MATIÈRES



## 1204.6277-LF-636-680.txt

n’est pas isotriviale.
   Dans [95], Liu construit la classe de Chern d’un cycle de codimension p sur une variété
algébrique propre X à valeurs dans le groupe H p,p (X) de cohomologie de Dolbeault. Pour
une variété définie sur Q, il démontre en particulier qu’un cycle (défini sur Q) dont la
classe de cohomologie de de Rham complexe usuelle est nulle a également une classe nulle
pour toutes les cohomologie de Dolbeault non archimédiennes associées aux différentes
places finies de Q.
   La cohomologie de ce complexe de Dolbeault est très certainement liée aux groupes
d’homologie tropicaux de [86], mais nous n’avons pas d’énoncé formel précis à proposer.
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



                                § 0.4. PERSPECTIVES

0.4.1. — Qu’est-ce qu’une forme de Kähler dans notre contexte et y a-t-il un analogue
du théorème de plongement de Kodaira ? La difficulté vient du fait que le support d’une
(n, n)-forme (qui serait la forme associée à la forme de Kähler) est un squelette et donc
très petit par rapport à l’espace. L’analogue non archimédien de la métrique de Fubini
est certes singulière, mais son courant de courbure est concentré en un point de la
droite projective. Dans le cas d’un espace projectif de dimension plus grande, la « forme
volume » associée à cette métrique est également concentrée en un point.


# Root read limits and compilation record

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