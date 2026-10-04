# A fixed-class concentration counterexample for unbounded perturbative energies

This note uses the bounded coefficient identity of **n1** and the finite-energy domain and example of **n2**, and proves the additional unbounded application directly. It refutes the proposed extension of the class-convergent auxiliary-path limit to all degree-\(d\) finite-energy potentials. It does not refute every possible unnormalized energy theory in P15.1.

Use \(X=\mathbb P^1\times\mathbb P^1\), \(\theta=p_1^*\kappa\), \(\psi=0\), and the fixed unbounded \(u=p_1^*v\) constructed in n2, with \(0<a<1/2\), \(v\leq0\), and \(v(z)=-b(-\log|z|)^a\) near \(0\). Normalize \(\int\kappa=1\). The class \(\alpha=[\theta]\) is nef, pseudoeffective, and has volume zero because \(\theta^2=0\) and the positive product of nef classes equals the cup product. Its actual reference degree is \(d=1\), and \(u\) has finite degree-one relative joint energy and full degree-one mass.

For each sufficiently small \(\varepsilon>0\), put
\[
\rho_\varepsilon=\exp(-\varepsilon^{-2/a}).
\]
Choose a nonnegative smooth two-form \(\beta_\varepsilon\), with total integral 1, supported in \(\{|z|<\rho_\varepsilon\}\). Such a form is obtained by rescaling and normalizing any fixed nonnegative smooth disk bump; it extends smoothly by zero. On a real surface every two-form is closed. Set
\[
\kappa_\varepsilon=\tfrac12\kappa+\tfrac12\beta_\varepsilon,
\qquad
\omega_\varepsilon=p_1^*\kappa_\varepsilon+p_2^*\kappa.
\tag{23a}
\]
These are smooth Kähler forms. Each \([\kappa_\varepsilon]=[\kappa]\) on \(\mathbb P^1\), because top real cohomology is determined by the integral. Thus all \([\omega_\varepsilon]\) equal the single Kähler class \(\lambda=[p_1^*\kappa+p_2^*\kappa]\), although their representatives do not converge smoothly.

Write \(S=\kappa+dd^cv\) on the base. It is positive of mass 1, with no polar atom. The current \(T_u=p_1^*S\) is positive; thus the fixed choice \(u_\varepsilon=u\) is \((\theta+\varepsilon\omega_\varepsilon)\)-psh and is uniformly identical to \(u\). For each fixed \(\varepsilon\), all relevant unbounded weighted integrals are finite: \(v\) is integrable against the smooth \(\kappa_\varepsilon\), and against both \(S\) and \(\kappa\) by n2. Each has a constant depending on that fixed form, which need not be uniform in \(\varepsilon\). Locality off \(z=0\) and the absence of polar mass give
\[
\langle(T_u+\varepsilon\omega_\varepsilon)^2\rangle
=2\varepsilon\,p_1^*(S+\varepsilon\kappa_\varepsilon)\wedge p_2^*\kappa.
\]
Its total mass is \(2\varepsilon(1+\varepsilon)\), exactly the anchor's mass. Hence \(u\) is of full relative top mass for every positive perturbation, and its relative top joint linear-weight energy is finite for every \(\varepsilon>0\). This counterexample does not exploit lost positive-perturbation mass or infinite energy at a fixed parameter.

Directly expand the three mixed terms in the unnormalized top energy with anchor zero:
\[
\begin{aligned}
(T_0+\varepsilon\omega_\varepsilon)^2
 &=2\varepsilon p_1^*(\kappa+\varepsilon\kappa_\varepsilon)p_2^*\kappa,\\
\langle(T_u+\varepsilon\omega_\varepsilon)(T_0+\varepsilon\omega_\varepsilon)\rangle
 &=\varepsilon p_1^*(S+\kappa+2\varepsilon\kappa_\varepsilon)p_2^*\kappa,\\
\langle(T_u+\varepsilon\omega_\varepsilon)^2\rangle
 &=2\varepsilon p_1^*(S+\varepsilon\kappa_\varepsilon)p_2^*\kappa.
\end{aligned}
\]
All weighted terms are finite, so expansion under their integrals is legitimate. Consequently
\[
\mathcal E^{2,\varepsilon,\omega_\varepsilon}_0(u)
=2\varepsilon\mathcal E_{0,\lambda}(u)
 +2\varepsilon^2\int_{\mathbb P^1}v\kappa_\varepsilon,
\qquad
\mathcal E_{0,\lambda}(u)=\tfrac12\int v(S+\kappa)\in\mathbb R.
\tag{24a}
\]
Thus the normalized relative energy is
\[
\frac{\mathcal E^{2,\varepsilon,\omega_\varepsilon}_0(u)}{2\varepsilon}
=\mathcal E_{0,\lambda}(u)+\varepsilon\int v\kappa_\varepsilon.
\tag{25a}
\]
On the support of \(\beta_\varepsilon\), one has \(-v\geq b\varepsilon^{-2}\), possibly strengthened by the harmless constant used to normalize \(v\). Therefore
\[
\int v\kappa_\varepsilon\leq-\tfrac b2\varepsilon^{-2},
\qquad
\varepsilon\int v\kappa_\varepsilon\longrightarrow-\infty.
\]
The expression (25a) diverges to minus infinity. For the fixed smooth auxiliary form \(\omega=p_1^*\kappa+p_2^*\kappa\), the same computation has the fixed finite \(\int v\kappa\), and the expression converges to \(\mathcal E_{0,\lambda}(u)\). Both paths have exactly the same auxiliary cohomology class and exactly the same potential for every parameter.

This is an analytic counterexample, within all ambient hypotheses, to an **unbounded strengthening** of n1's class-convergent perturbation theorem. It is not a counterexample to n1, whose bounded-difference hypothesis supplies (14). It shows that degree-\(d\) finite energy, even together with finite full relative top energy at every positive perturbation, does not provide the uniform weighted lower-coefficient estimate needed for an auxiliary representative path. Here the lower weighted coefficient is finite at every parameter and still diverges faster than its suppressing power of \(\varepsilon\). Additional uniform integrability, a restriction on auxiliary forms, or a different iterated/truncated limiting prescription is necessary for such a path theorem. None is silently added to the original catalogue atom.
