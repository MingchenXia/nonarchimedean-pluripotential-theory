# Curvature identities and explicit nontrivial-normal-bundle checks

Date: 2026-08-31. Author: /root/p213_skeletal_hostile.
Status: bounded research calculations, not independently or production accepted.
These calculations are separate from the proof's arbitrary-current test.

## 1. Exactly which global curvature identity is valid

Use the notation of statement.tex, and write \(\overline L\) for the line bundle with its formal metric. The tautological section \(\tau\) of \(\rho^*L\) is analytic and nowhere zero on \(X\). Its norm is the continuous function \(e^{-u}\). CLD25 §§18.1.1--18.1.3 (printed p. 501) therefore gives, by the definition of the curvature current,

\[
 \mathrm d'\mathrm d''[u]=c_1(\rho^*\overline L).
\]

Here \(\rho^*\overline L\) means the pulled-back metrized line bundle. The right side is its curvature, defined using local continuous potentials. It is NOT an asserted pullback of an arbitrary current. The equality does not assert that \(u\) is smooth, that its curvature is zero, or that a wedge \(T\wedge c_1(\rho^*\overline L)\) is defined.

For a normalized rational section \(\sigma\), set \(h_\sigma=-\log\|\sigma\|\) on the complement of its divisor. On the proper base curve, CLD Theorem 18.1.6 (printed p. 502) gives the exact sign

\[
 \mathrm d'\mathrm d''[h_\sigma]
       =c_1(\overline L)-\delta_{\operatorname{div}_C(\sigma)}.
\]

The formal model of the curve is normal with irreducible special fibre. CLD Proposition 18.5.1 (printed pp. 527--528) specializes in dimension one to

\[
 c_1(\overline L)=\deg_K(L)\,\delta_{\xi_0},
\]

where \(\xi_0\) is the unique good-reduction point over the generic point of \(C_0\). The generic and special degrees agree for this proper smooth model; the divisor of \(\bar\sigma\) represents \(\mathcal L_0\). Consequently the section orders \(n_p=\operatorname{ord}_p(\bar\sigma)\) have weighted sum \(\deg_k(\mathcal L_0)\), not necessarily zero.

These are identities of the indicated canonical curvature currents. The proof neither multiplies them by \(T\) nor transports them through an unspecified current-pullback operation.

## 2. The exact coordinate/gluing correction used in the proof

On the ordinary open locus where \(\sigma\) is an analytic frame, write the tautological vector as \(a\sigma\), and put \(r=v(a)\). This is an analytic log-unit coordinate on that locus, and

\[
 u=r+h_\sigma.
\]

On the \(p\)-collar, \(h_\sigma=n_ps\). Thus \(r=u-n_ps\). The shear \((u,s)\mapsto(r,s)\) has matrix

\[
 \begin{pmatrix}1&-n_p\\0&1\end{pmatrix}\in\operatorname{SL}_2(\mathbf Z).
\]

For a residual rational function of order \(m_p\), the lifted \(t=v(F)\) is \(m_ps\) on that entire collar. The test differentiation then gives

\[
 \varphi(r)\chi'(t)\,
 \mathrm d'r\wedge\mathrm d''r\wedge\mathrm d't\wedge\mathrm d''t
 =
 m_p^2\varphi(u-n_ps)\chi'(m_ps)\,
 \mathrm d'u\wedge\mathrm d''u\wedge\mathrm d's\wedge\mathrm d''s.
\]

This is an equality of actual ordinary smooth source forms. The degree \(n_p\) introduces a shear but no lattice determinant factor. The deliberately chosen radial margin gives

\[
 \int_0^\ell\varphi(u-n_ps)\,\mathrm du=1
\]

whenever the differentiated collar integrand is nonzero. Therefore no extra curvature term appears in the principal-function relation \(\sum_p m_pb_T(p)=0\). This is a statement about this specific compactly supported test, not a claim that curvature has disappeared from the geometry.

If a second normalized rational section is \(\sigma'=g\sigma\), then \(g\) is a rational function with vertical order zero and \(\bar\sigma'=\bar g\,\bar\sigma\). On a common ordinary unit locus,

\[
 r'=r-v(g),\qquad
 n'_p=n_p+\operatorname{ord}_p(\bar g).
\]

The new shear is still integral of determinant one. The proof can be rerun with the enlarged finite bad set. The already-defined coefficients \(b_T(p)\) do not change, since they used only completed formal frames, whose transition functions have norm one on the entire tube. No ordinary-open cover is inferred from a formal Zariski cover.

## 3. Nontrivial normal bundle: \(\mathcal O(1)\) on \(\mathbf P^1_R\)

Take \(K=\mathbf C((\pi))\), \(R=\mathbf C[[\pi]]\), \(\mathcal C=\mathbf P^1_R\), and \(\mathcal L=\mathcal O(1)\). The hypersurface defined by the pairing \(\mathcal L\oplus\mathcal L^{-1}\to\mathcal O\) equal to \(\pi\) is regular with local equation \(xy=\pi\). Its double curve has normal bundles \(\mathcal O(1)\) and \(\mathcal O(-1)\); this is not the product model with trivial normal bundles.

Let \(Z=X_1/X_0\), let \(\sigma=X_0\), and let \(W=1/Z\) near infinity. CLD Example 17.7.3 (printed p. 493) gives

\[
 \|\sigma\|=\frac1{\max(1,|Z|)},\qquad
 h_\sigma=\max(0,\log|Z|).
\]

The reduced section has divisor \([\infty]\). Thus \(n_\infty=1\), while \(n_p=0\) at finite points. On the infinity collar \(s=v(W)\), one has \(r=u-s\).

Choose \(F=Z\). Its reduced divisor is \([0]-[\infty]\), so \(m_0=1\) and \(m_\infty=-1\). The collar integral at infinity is

\[
 \int m_\infty^2\chi'(m_\infty s)
                  \left(\int_0^\ell\varphi(u-s)\,\mathrm du\right)\mathrm ds
   =-m_\infty=1.
\]

The two boundary terms give \(b_T(0)-b_T(\infty)=0\), exactly the principal relation. For the canonical current both coefficients are one.

By contrast, the section divisor \([\infty]\) has \(\lambda_T([\infty])=c\), not zero in general. In particular the canonical current gives one. The false replacement of a rational FUNCTION divisor by the divisor of a section of a nontrivial line bundle would force \(1=0\) in this example. The missing term is precisely the nonzero Chern degree.

The base current identity here is

\[
 \mathrm d'\mathrm d''[h_\sigma]
   =\delta_{\xi_0}-\delta_\infty,
 \qquad c_1(\overline{\mathcal O(1)})=\delta_{\xi_0}.
\]

The source of the curvature formula is CLD Theorem 18.1.6 and Example 18.5.2, not a claim about arbitrary-current products.

## 4. An original-field analytic test rules out a global harmonic log-unit radius

The failure can be seen over the original \(K=\mathbf C((\pi))\), without choosing a fractional-valued scalar or decomposing a finite cover into ordinary sheets.

Take \(0<\epsilon<\ell/2\), and the ordinary annulus in the variable \(T\)

\[
 B=\{\ell/2-\epsilon<v(T)<\ell/2+\epsilon\}.
\]

Define an analytic map into the preceding \(\mathcal O(1)\) torsor by

\[
 Z=T^2/\pi,\qquad
 j(T)=T\,\sigma(Z).
\]

The coefficient \(T\) is invertible and the section is defined at every finite \(Z\). With \(t=v(T)\), the metric formula gives

\[
 (u\circ j)(T)
   =t+\max(0,\ell-2t)=\max(t,\ell-t).
\]

Its value lies in \([\ell/2,\ell/2+\epsilon)\subset(0,\ell)\), so the map indeed lands in \(X\). This continuous function is not pluriharmonic. More precisely, for \(h\in C_c^\infty((\ell/2-\epsilon,\ell/2+\epsilon))\), properness of the annulus tropicalization and the canonical primitive-coordinate calibration give

\[
 \left\langle
   \mathrm d'\mathrm d''[u\circ j],\,h(v(T))
 \right\rangle
 =\int \max(t,\ell-t)h''(t)\,\mathrm dt
 =2h(\ell/2).
\]

The last equality is integration by parts on the two intervals: the slope jumps from \(-1\) to \(+1\). This is a direct computation of the current of the pulled-back continuous FUNCTION. No pullback of \(T\), no pullback of its curvature, and no current slice is used.

It follows that \(u\) cannot be treated as a global analytic log-unit, or as an ordinary smooth pluriharmonic radius: either assertion would pull back through the analytic map \(j\) to a function with zero \(\mathrm d'\mathrm d''\), contradicting the displayed test. We do not need a general classification of ordinary smooth formal metrics or a general non-smoothness theorem for the main proof.

## 5. Nonsplit residue and zero-order stress tests

The line bundle introduces no new residue-degree multiplier: on the completed \(p\)-tube it is free with norm-one basis. Over \(K_p\) the primitive product collar has coefficient one; when viewed over \(K\) it has coefficient \([K_p:K]=[\kappa(p):k]\) by CLD14.4.3.

For a simultaneous concrete check take \(K=\mathbf R((\pi))\), \(\mathcal C=\mathbf P^1_R\), \(\mathcal L=\mathcal O(1)\), and the degree-two closed residual point \(p=(Z^2+1)\). Its tube is one disc over \(\mathbf C((\pi))\), not two ordinary discs. Let \(F=Z^2+1\) and \(\sigma=X_0\). Then \(m_p=1\), \(m_\infty=-2\), \(n_p=0\), \(n_\infty=1\). The relation is \(b_T(p)-2b_T(\infty)=0\); the canonical weights give \(2-2\cdot1=0\). The normal-bundle shear at infinity does not multiply the coefficient again.

The bad set must still include the zeros and poles of \(\sigma\) even when \(m_p=0\). For example, with \(\mathcal O(1)\), \(\sigma=X_0\), and \(F=(Z-1)/(Z-2)\), infinity has \(n_\infty=1\) and \(m_\infty=0\). On its entire outer collar \(v(F)=0\), so the cutoff error is killed by \(\mathrm d''t=0\), despite the nonzero shear. Likewise the earlier cancellation example \(F=(Z-1)(Z-\pi)/(Z-2\pi)\) has a deeper zero/pole pair over \(Z=0\) with net residual order zero; retaining that tube remains essential.

