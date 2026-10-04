# A prescribed bounded-type energy without a fibration

**Status: a partial result for P15.1.** The theorem below applies to every connected smooth compact Kähler manifold and every actual reference potential in every pseudoeffective zero-volume class. Its domain is the prescribed bounded singularity type. It does not assert a complete solution of the original atom, an identification with numerical dimension, or any solution of P15.2 or P15.3. All assertions are mathematical drafts, not independently certified results.

## Conventions and the standard foundations used

Let \(X\) be a connected smooth compact Kähler \(n\)-fold, \(n\geq1\). Set
\[
d^c=\frac{i}{4\pi}(\bar\partial-\partial),\qquad dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
A potential is never identically minus infinity. For a smooth closed real \((1,1)\)-form \(\theta\), put \(T_u=\theta+dd^cu\). Write \(u\sim\psi\) when \(\psi-C\leq u\leq\psi+C\) for some finite constant; differences are interpreted on the common finite locus and may be assigned any value on the common polar set. Define
\[
\mathcal C_\psi=\{u\in\operatorname{PSH}(X,\theta):u\sim\psi\}.
\]
The comparison inequalities, not an ideal equivalence, define the retained singularity data.

The following scoped published foundations are used. Their complete supplied primary bodies, including defects, are reproduced in the authoritative argument's source annex.

1. **Nonpluripolar products.** BEGZ, *Monge–Ampère equations in big cohomology classes*, Acta Math. 205 (2010), 199–262, arXiv:0812.3674v2, Definition 1.1, Proposition 1.4, Proposition 1.6 and Theorem 1.8: products of finitely many closed positive \((1,1)\)-currents on a compact Kähler manifold are well-defined finite closed positive currents, symmetric, multilinear on positive sums, and plurifinely local. Their trace measures put no mass on pluripolar sets. Smooth factors agree with ordinary multiplication. The empty product is 1. These statements apply to actual currents and do not assert multilinearity of the class positive product.
2. **Bounded-type mixed masses and monotonicity.** Darvas–Di Nezza–Lu, *Monotonicity of nonpluripolar products and complex Monge–Ampère equations with prescribed singularity*, Anal. PDE 11 (2018), 2049–2087, Proposition 2.1: for \(n\) smooth closed real \((1,1)\)-forms \(\theta_j\) with pseudoeffective classes, and \(u_j,v_j\in\operatorname{PSH}(X,\theta_j)\) of the same bounded singularity type in every slot, the two top mixed nonpluripolar integrals are equal. Theorem 2.4: if every \(u_j\) is less singular than \(v_j\), the integral for the \(u_j\)'s is at least that for the \(v_j\)'s. There is no big-class or small-unbounded-locus hypothesis in these statements. Smooth Kähler factors are slots with potential zero.
3. **Volume at the boundary.** BEGZ Definition 1.17 defines the volume of a big class by its minimal-singularity top mass and extends the positive product to pseudoeffective classes as the decreasing limit along addition of an arbitrary Kähler class. In particular \(\operatorname{vol}(\alpha+\varepsilon\lambda)\to\operatorname{vol}(\alpha)\) as \(\varepsilon\downarrow0\). For nef classes the positive product equals the ordinary cup product. To bound the mass of an arbitrary current in a big class we use foundation 2: a minimal-singularity potential is less singular than it, so its top mass is an upper bound. No equality with the arbitrary actual-current mass is assumed.
4. **Admissible Dirichlet products and IBP.** Duc-Viet Vu, *Convexity of the class of currents with finite relative energy*, arXiv:2005.13241v3 (25 March 2022), §2, Lemmas 2.5–2.6 and Theorem 2.7: if \(R\) is a closed positive \((n-1,n-1)\)-current and (a,b) are bounded \(R\)-admissible dsh functions, then their intrinsic relative Dirichlet products exist; the diagonal product is positive, and
\[
\int b\langle dd^ca\dot\wedge R\rangle
=\int a\langle dd^cb\dot\wedge R\rangle
=-\int\langle db\wedge d^ca\dot\wedge R\rangle.
\tag{F}
\]
A dsh function is a difference of two quasi-psh functions. Admissibility means that there is such a representation whose polar sets have zero \(R\)-mass. Vu's Proposition 2.1(iii) identifies iterated relative products; with \(R=\langle S_1\cdots S_m\rangle\wedge W\), \(W\) smooth closed positive, the signed product in (F) is the difference of the corresponding ordinary nonpluripolar products. Products in all our applications are finite by foundation 1. If (m=0), (R=W) is smooth. Otherwise its trace measure has no pluripolar mass. Thus every bounded difference used below is admissible, including smooth test functions.

Vu's current convention is \(dd^c_V=i\partial\bar\partial/\pi=2dd^c\); the read-only page-4 image of arXiv:2004.11111v1 confirms it despite a defective text extraction. A source potential \(u/2\) represents the current \(T_u\), with the smooth background unchanged. Source differences are divided by 2; \(d^c_V=2d^c\). The signed source \(dd^c_V(a/2)\) equals \(dd^ca\), and the source Dirichlet current for (a/2) equals one half of ours. Multiplying the source IBP equality by 2 gives (F). Source bounded-type comparisons, full-mass conditions, and energy finiteness are unchanged by this positive scalar change. DDNL uses \(i\partial\bar\partial=2\pi dd^c\); its source potentials are \(u/(2\pi)\). Its mixed-mass theorems concern the same actual currents after that conversion. The locally psh BEGZ product statements are likewise independent of a positive convention change, by rescaling local potentials to represent the same currents. No application of Xia's big-class corollary to a merely pseudoeffective class is made here.

The intrinsic diagonal definition is
\[
da\wedge d^ca\wedge R=\tfrac12dd^c(a^2)\wedge R-a\,dd^ca\wedge R
\tag{G}
\]
for differences of bounded quasi-psh functions, followed by Vu's admissible nonpluripolar truncation construction. The factor (1/2) is mandatory. Vu v3 Eq. (2.3) prints it correctly, but the repeated page-6 expansion and page-11 cutoff identity omit it. We preserve those literal quotations and use (G), not those defective repetitions.

For clarity, the defect does not introduce a gap in our use of (F). Here is a direct corrected cutoff check. For negative quasi-psh representations \(a=\phi_1-\phi_2\), \(b=\phi_3-\phi_4\), choose a Kähler form \(\Omega\) with \(dd^c\phi_j\geq-\Omega\). Put
\[
\chi_k=1+k^{-1}\max(\phi_1+\phi_2+\phi_3+\phi_4,-k),\quad
a_k=\max(\phi_1,-k)-\max(\phi_2,-k),
\]
and define \(b_k\) similarly. Then \(0\leq\chi_k\leq1\), \(dd^c\chi_k\geq-4\Omega/k\), and the support of \(\chi_k\) is in the simultaneous finite truncation locus. Correct bounded Bedford–Taylor/Stokes calculus using (G) gives
\[
0\leq\int d\chi_k\wedge d^c\chi_k\wedge R
=-\int\chi_kdd^c\chi_k\wedge R
\leq\frac4k\int\Omega\wedge R.
\tag{C}
\]
Indeed \(dd^c\chi_k+4\Omega/k\) is positive, so its negative contribution in the last expression can be discarded. The same calculation gives \(\int da_k\wedge d^ca_k\wedge R\leq2\|a_k\|_\infty\int\Omega R\); the sup norms are uniformly bounded by boundedness of \(a\). These formulae apply to bounded quasi-psh truncations by bounded Bedford–Taylor calculus. Cauchy–Schwarz and (C) make all cross terms containing \(d\chi_k\) tend to zero. On \(\{\chi_k>0\}\), plurifine locality identifies the signed products and the intrinsic gradients with their truncations. Dominated convergence is permissible because \(R\) has no mass on the representation poles, the relative positive products also have no mass there, and the admissible gradients have finite mass by Vu's Lemmas 2.5–2.6. Applying bounded IBP to
\(\chi_k(b_kdd^ca_k-a_kdd^cb_k)R\) proves symmetry; applying it to \(\chi_k(a_kdd^ca_k+da_k\wedge d^ca_k)R\) proves the negative diagonal equality. Polarization gives (F). In the page-6 local square expansion, the correct coefficients of its three square terms are \(1,1,-1/2\), not \(2,2,-1\). Thus every Dirichlet calculation here has the correct intrinsic factor. This check uses the standard gradient construction, not the misprinted formula as a definition.

## The bounded theorem

Suppose \(\alpha=[\theta]\) is pseudoeffective with \(\operatorname{vol}(\alpha)=0\), and fix an actual \(\psi\in\operatorname{PSH}(X,\theta)\). For a Kähler form \(\omega\), set
\[
M_k(\psi,[\omega])=\int_X\langle T_\psi^k\rangle\wedge\omega^{n-k},\quad
d=\max\{0\leq k\leq n:M_k>0\},\quad r=n-d.
\tag{1}
\]
The convention is \(M_0=\int\omega^n>0\). Then \(d<n\), \(d\) is independent of the auxiliary Kähler form, and every degree (k>d) nonpluripolar mixed product of currents \(T_{u_i}\), \(u_i\in\mathcal C_\psi\), is zero as a current.

For any Kähler class \(\lambda\), the following relative energy is independent of the Kähler representative \(\omega\in\lambda\):
\[
\mathcal E_{\psi,\lambda}(u)
=\frac1{d+1}\sum_{a=0}^d\int_X(u-\psi)
\langle T_u^aT_\psi^{d-a}\rangle\wedge\omega^r.
\tag{2}
\]
For any \(u,v\in\mathcal C_\psi\), let \(\mathcal E_{v,\lambda}(u)\) denote the same formula with anchor \(v\). Then
\[
\mathcal E_{\psi,\lambda}(u)-\mathcal E_{\psi,\lambda}(v)
=\mathcal E_{v,\lambda}(u).
\tag{3}
\]
The energy is increasing, concave, \(\mathcal E_{\psi,\lambda}(\psi)=0\), and
\[
\mathcal E_{\psi,\lambda}(u+c)=\mathcal E_{\psi,\lambda}(u)+cM_d,
\qquad
|\mathcal E_{\psi,\lambda}(u)-\mathcal E_{\psi,\lambda}(v)|
\leq M_d\|u-v\|_\infty.
\tag{4}
\]
No division by zero volume, or division by \(M_d\), occurs. The carrier for these integrals is the actual \(n\)-dimensional manifold \(X\); the nonpluripolar current has bidegree \((d,d)\). A geometric \(d\)-dimensional quotient is not supplied or assumed.

### Degree, mass, and vanishing

The class \(\alpha+\varepsilon[\omega]\) is big for \(\varepsilon>0\): the actual current \(T_\psi+\varepsilon\omega\) is bounded below by \(\varepsilon\omega\). A minimal-singularity potential in this big class is less singular than \(\psi\), so foundation 2 gives
\[
0\leq M_n\leq\int\langle(T_\psi+\varepsilon\omega)^n\rangle
\leq\operatorname{vol}(\alpha+\varepsilon[\omega]).
\]
The middle expression expands, using actual-current multilinearity, as
\[
P_\varepsilon(\omega)=\sum_{k=0}^n\binom nk\varepsilon^{n-k}M_k.
\tag{5}
\]
The last bound tends to zero by foundation 3. Hence \(M_n=0\), \(d<n\), and (5) ends at \(k=d\). This does not identify \(P_\varepsilon\) with class volume.

If \(\omega'\) is another Kähler form, compactness gives constants \(c,C>0\) such that \(c\omega\leq\omega'\leq C\omega\). For a positive \((k,k)\)-current \(S\), positivity of the power differences gives
\[
c^{n-k}\int S\omega^{n-k}\leq\int S(\omega')^{n-k}\leq C^{n-k}\int S\omega^{n-k}.
\]
Thus the positivity tests in (1) agree. Foundation 2, with \(k\) same-type current slots and (n-k) slots \((\omega,0)\), gives
\[
\int\langle T_{u_1}\cdots T_{u_k}\rangle\omega^{n-k}=M_k.
\tag{6}
\]
For \(k>d\) the left current is positive and has zero trace mass against a strictly positive form. A positive current of zero trace mass is zero: on each coordinate chart its coefficient measures are dominated by its trace measure, by positivity. This proves the stated current vanishing. Each \(M_k\) depends only on \([\omega]\) because \(\langle T_\psi^k\rangle\) is closed and integration of an exact smooth complementary form against a closed current vanishes by distributional Stokes. It is a homogeneous polynomial of degree (n-k) in \([\omega]\).

### Closed polynomial one-form and its primitive

We first work at any degree \(0\leq q\leq n\), with a fixed smooth product \(W=\omega^{n-q}\). In this paragraph there is no zero-volume assumption. On the convex hull of a finite family \(u_0,\ldots,u_m\) of same-type \(\theta\)-psh potentials, set \(h_i=u_i-u_0\), \(u_t=u_0+\sum t_i h_i\), and
\[
A_i(t)=\int h_i\langle T_{u_t}^q\rangle W.
\]
Multilinearity makes these functions polynomials in the finite parameters. All coefficient integrals exist since \(h_i\) is bounded off a common polar set and the measures do not charge it. For \(q\geq1\),
\[
\partial_j A_i=q\int h_i\langle dd^ch_j\wedge T_{u_t}^{q-1}\rangle W
=\partial_i A_j
\tag{7}
\]
by (F), applied to the closed positive current \(R=\langle T_{u_t}^{q-1}\rangle W\). Its bidegree is \((n-1,n-1)\); it has no pluripolar mass, including when \(q=1\), in which case it is smooth. The signed expression is exactly the difference in one current slot, by the iterated-product property. Thus (7) is a checked application, not formal unsigned wedge calculus. For \(q=0\), the \(A_i\)'s are constant and closedness is immediate.

The line integral of this closed one-form from \(v\) to \(u\) equals
\[
\int_0^1\int (u-v)\langle((1-t)T_v+tT_u)^q\rangle W\,dt
=\frac1{q+1}\sum_{a=0}^q\int(u-v)\langle T_u^aT_v^{q-a}\rangle W.
\tag{8}
\]
The last equality follows by the binomial expansion and
\(\binom qa\int_0^1t^a(1-t)^{q-a}dt=1/(q+1)\). Closedness (7) implies zero integral around each triangle in the convex hull, by ordinary Stokes for a polynomial one-form on that finite simplex. The identity extends to its boundary by polynomial continuity. Taking the triangle with vertices \(\psi,v,u\) proves (3), for degree \(d\), and proves the corresponding cocycle at every other degree or positive perturbation used later.

For a segment \(u_t=(1-t)u+tv\), \(h=v-u\), this also proves exact variation regularity:
\[
\frac d{dt}\mathcal E_{\psi,\lambda}(u_t)=\int h\langle T_{u_t}^d\rangle\omega^r,
\tag{9}
\]
and, for \(d\geq1\),
\[
\frac {d^2}{dt^2}\mathcal E_{\psi,\lambda}(u_t)
=d\int h\langle dd^ch\wedge T_{u_t}^{d-1}\rangle\omega^r
=-d\int\langle dh\wedge d^ch\dot\wedge
(\langle T_{u_t}^{d-1}\rangle\omega^r)\rangle\leq0.
\tag{10}
\]
The last inequality is positivity of the intrinsic Dirichlet product (G); IBP symmetry alone would not give it. Equations (9)–(10) are polynomial identities with continuous endpoint derivatives. More generally the pullback to any finite simplex is polynomial and admits the ordinary chain rule along \(C^1\) parameter paths and second derivatives along \(C^2\) parameter paths. No derivative assertion for arbitrary discontinuous or unbounded velocities is made. When \(d=0\), the energy is affine and there is no gradient formula (10).

If \(u\leq v\), (9) is nonnegative. A constant shift leaves the current fixed, and (6) makes (9) equal \(cM_d\). Finally, the pointwise sandwiches \(v-\delta\leq u\leq v+\delta\), \(\delta=\|u-v\|_\infty\), give (4). The same argument proves the corresponding Lipschitz estimate with the actual common-type mass in an arbitrary positive perturbation.

### Representative independence and cohomological continuity

If \(\omega_1,\omega_0\) are cohomologous Kähler forms, the compact Kähler \(dd^c\)-lemma gives a smooth real \(g\) with \(\omega_1-\omega_0=dd^cg\). We use exactly the degree-two consequence of this standard lemma: cohomologous smooth closed real \((1,1)\)-forms differ by \(dd^c\) of a smooth real function. A standard published reference is Deligne–Griffiths–Morgan–Sullivan, *Real homotopy theory of Kähler manifolds*, Invent. Math. 29 (1975), 245–274, §5, the principle of two types. The hypotheses here are precisely compact Kähler, smooth, closed, real, cohomologous, and of pure type \((1,1)\); taking the real part and rescaling the operator gives our stated convention. This is a standard foundation citation, not an independently reproduced source proof. For \(r\geq1\),
\[
\omega_1^r-\omega_0^r=dd^cg\wedge\sum_{b=0}^{r-1}\omega_1^b\omega_0^{r-1-b}.
\]
For any term in (2), write \(h=u-\psi\) and \(Q=\langle T_u^aT_\psi^{d-a}\rangle\). For each \(b\), the current \(R=Q\omega_1^b\omega_0^{r-1-b}\) is closed positive of bidegree \((n-1,n-1)\). It has no pluripolar mass; when \(d=0\), it is smooth. Thus \(h,g\) are bounded admissible dsh functions and (F) gives
\[
\int h\,dd^cg\,R=\int g\langle dd^ch\dot\wedge R\rangle=0.
\tag{11}
\]
The signed current on the right is
\((\langle T_uT_u^aT_\psi^{d-a}\rangle-
\langle T_\psi T_u^aT_\psi^{d-a}\rangle)\omega_1^b\omega_0^{r-1-b}\); both terms vanish by degree \(d+1\) vanishing. All multiplication by bounded functions takes place against nonpluripolar measures. This proves representative independence, including the \(d=0\) case.

The same proof applies to a mixed product of \(r\) smooth closed Kähler factors, changing any one factor within its class. It makes the energy a symmetric multilinear functional of their classes. To see its polynomial dependence without imposing convergence of representatives, choose a basis \(e_i\) of \(H^{1,1}(X,\mathbb R)\) and fixed smooth closed representatives \(\eta_i\). Near any fixed Kähler class \(\lambda_0\) represented by a positive \(\omega_0\), the linear choice \(\omega(\lambda)=\omega_0+\sum x_i\eta_i\) remains positive for small \(x_i\). The expression (2) is a polynomial in these coordinates. Alternatively decompose arbitrary smooth closed real factors as differences of Kähler forms by adding a large fixed Kähler form, and apply multilinearity. Representative independence ensures that these local polynomials agree on overlap and give one homogeneous polynomial of degree \(r\) on the Kähler cone. In particular the leading energy is continuous in the auxiliary class.

Changing \(\theta\) to \(\theta+dd^cg\) and simultaneously replacing \(u,\psi\) by \(u-g,\psi-g\) leaves every actual current and difference unchanged. Changing the anchor within \(\mathcal C_\psi\) has exactly the cocycle (3), not absolute anchor independence.

## Relative Kähler perturbation limits

For \(\varepsilon>0\), an arbitrary Kähler form \(\omega\), and \(v\in\operatorname{PSH}(X,\theta+\varepsilon\omega)\) with \(v\sim\psi\), define the unnormalized relative top energy
\[
\mathcal E^{n,\varepsilon,\omega}_\psi(v)
=\frac1{n+1}\sum_{a=0}^n\int(v-\psi)
\langle(T_v+\varepsilon\omega)^a(T_\psi+\varepsilon\omega)^{n-a}\rangle.
\tag{12}
\]
Here \(T_v\) alone need not be positive; the displayed currents \(T_v+\varepsilon\omega\) are positive. The degree-\(n\) version of (7)–(8), applied directly in the pseudoeffective (indeed big) class \(\alpha+\varepsilon[\omega]\), gives its cocycle, monotonicity and Lipschitz constant \(P_\varepsilon(\omega)\), the actual mass (5). It is not class volume in general.

For fixed \(u\in\mathcal C_\psi\), put
\[
\mathcal E^{(k),\omega}_\psi(u)=\frac1{k+1}\sum_{a=0}^k
\int(u-\psi)\langle T_u^aT_\psi^{k-a}\rangle\omega^{n-k}.
\]
Expanding the segment formula (8) gives the exact identity
\[
\mathcal E^{n,\varepsilon,\omega}_\psi(u)
=\sum_{k=0}^d\binom nk\varepsilon^{n-k}\mathcal E^{(k),\omega}_\psi(u).
\tag{13}
\]
In the original mixed sum, the coefficient for \(T_u^aT_\psi^{k-a}\omega^{n-k}\) is
\(\sum_{j=0}^n\binom ja\binom{n-j}{k-a}/(n+1)
=\binom n k/(k+1)\). The identity follows by marking the \((a+1)\)-st element of a \((k+1)\)-subset of \({0,\ldots,n}\) and summing over its location. This also proves it at \(k=0\). For all \(k\), (6) gives
\[
|\mathcal E^{(k),\omega}_\psi(u)|\leq\|u-\psi\|_\infty M_k(\psi,[\omega]).
\tag{14}
\]

Now let **any** family of Kähler forms \(\omega_\varepsilon\) have \([\omega_\varepsilon]\to\lambda\), with \(\lambda\) Kähler. No smooth or pointwise convergence of these forms is assumed. Let \(u_\varepsilon\in\operatorname{PSH}(X,\theta+\varepsilon\omega_\varepsilon)\) have the same bounded type as \(\psi\), and let \(\delta_\varepsilon=\|u_\varepsilon-u\|_\infty\to0\) off their common polar set. Then
\[
\frac{\mathcal E^{n,\varepsilon,\omega_\varepsilon}_\psi(u_\varepsilon)}
{\binom n d\varepsilon^{n-d}}
\longrightarrow\mathcal E_{\psi,\lambda}(u).
\tag{15}
\]
Indeed the positive-\(\varepsilon\) cocycle and monotonicity give
\[
|\mathcal E^{n,\varepsilon,\omega_\varepsilon}_\psi(u_\varepsilon)
-\mathcal E^{n,\varepsilon,\omega_\varepsilon}_\psi(u)|
\leq\delta_\varepsilon P_\varepsilon(\omega_\varepsilon).
\]
Each \(M_k\) is a cohomological polynomial and is bounded for classes in a compact neighborhood of \(\lambda\); hence \(P_\varepsilon=O(\varepsilon^r)\), uniformly without any bounds on representatives. The normalized error tends to zero. For fixed \(u\), (13)–(14) bound all normalized \(k<d\) terms by constants times \(\varepsilon^{d-k}\). The \(k=d\) term is \(\mathcal E_{\psi,[\omega_\varepsilon]}(u)\), converging by its class polynomial. This proves (15). Only the leading coefficient is representative independent. Formula (13) does not claim representative independence of the lower coefficients or of the full energy (12).

For example, on \(X=\mathbb P^1\times\mathbb P^1\), take \(\theta=p_1^*\kappa\), \(\psi=0\), and a nonconstant smooth \(u=p_1^*v\) with \(\kappa+dd^cv>0\). Set \(\omega_0=p_1^*\kappa+p_2^*\kappa\), with \(\int\kappa=1\). Replacing \(\omega_0\) by \(\omega_0+tdd^cu\), for small nonzero \(t\), stays Kähler and in the same class. Here \(d=1\); the leading \(\mathcal E^{(1)}\) is unchanged, but
\[
\int u\big((\omega_0+tdd^cu)^2-\omega_0^2\big)
=2t\int_{\mathbb P^1}vdd^cv
=-2t\int_{\mathbb P^1}dv\wedge d^cv\ne0.
\]
Thus the \(\varepsilon^2\) coefficient \(\mathcal E^{(0)}\) changes. This explicitly rules out an unintended claim about the full positive-perturbation energy.

## Auxiliary differential-measure check, only for the energy route

No zero-volume operator theorem is claimed here. The following estimate checks the differential in (9) under a **fixed** Kähler form. For fixed \(u\in\mathcal C_\psi\), (5) as a measure expansion and degree vanishing give
\[
\frac{\langle(T_u+\varepsilon\omega)^n\rangle}
{\binom n d\varepsilon^r}
\rightharpoonup\langle T_u^d\rangle\omega^r.
\tag{16}
\]
The limiting measure is on \(X\), has positive raw mass \(M_d\), and still depends on the full form in general.

For \(u_\varepsilon\) as in (12), set \(A=T_{u_\varepsilon}+\varepsilon\omega\), \(B=T_u+\varepsilon\omega\), \(h=u_\varepsilon-u\), \(\delta=\|h\|_\infty\). Multilinearity factors the top difference as
\(\sum_{j=0}^{n-1}\langle dd^ch\wedge A^jB^{n-1-j}\rangle\). For a smooth test \(f\), (F) transfers \(dd^c\) to \(f\), with admissible bounded \(h\), and \(-C_f\omega\leq dd^cf\leq C_f\omega\) bounds the result by
\[
\left|\int f(\langle A^n\rangle-\langle B^n\rangle)\right|
\leq nC_f\delta\,Q_\varepsilon,
\quad
Q_\varepsilon=\sum_{k=0}^d\binom{n-1}k\varepsilon^{n-1-k}M_k
=O(\varepsilon^{r-1}).
\tag{17}
\]
For every \(j\), equality of the mixed mass with one smooth \(\omega\)-slot to \(Q_\varepsilon\) is exactly foundation 2 in class \(\alpha+\varepsilon[\omega]\), replacing the \(A,B\)-potentials by \(\psi\), followed by positive binomial expansion. Since \(d<n\), the sum has legal indices. At \(n=1,d=0\), the product with zero \(A,B\)-slots is 1 and \(Q_\varepsilon=M_0\), so the same calculation applies. The normalized error is \(O_f(\delta/\varepsilon)\). Therefore \(\delta=o(\varepsilon)\) suffices for (16) with moving potentials; this is a sufficient rate, not an optimality claim.

If \(\omega_\varepsilon\to\omega\) smoothly and \(\omega\) is Kähler, the tests are uniformly bounded by these forms and the same constants can be taken uniformly; the fixed-current terms in (16) converge by smooth multiplication. For class-convergent forms alone, neither this test bound nor convergence of the final full-form measure is supplied. The rate-free energy result (15) is not transferred to (16).
