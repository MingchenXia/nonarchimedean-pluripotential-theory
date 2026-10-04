# Global logarithmic comparison metric: conditional repair candidate

Date: 4 October 2026. This book-external proof candidate isolates the
comparison-metric and integration-by-parts steps used in Lemma 4.3 of
Yang Li, arXiv:2505.11087v1. It makes no novelty claim and does not certify
the principal Calabi–Yau convergence theorem. No independent model-verifier
receipt has been obtained.

## Exact setting and conclusion

Let \(\pi:\mathcal X\to D\) be a proper holomorphic family with smooth
total space, smooth compact connected \(n\)-dimensional fibres, \(n\geq1\), over
\(D^*\), and reduced simple normal crossing central divisor
\(\sum_{i=1}^s E_i\). Work over a smaller closed disc whose preimage is
compact. Fix a smooth Kähler form \(\Omega\) on a neighbourhood of this
preimage, and a smooth Hermitian metric on a model line bundle
\(\mathcal L\). Its closed real curvature form \(\omega_h\) must satisfy

\[
 \omega_h|_{X_t}\geq c\,\Omega|_{X_t},\qquad c>0,
 \qquad 0<|t|\leq r_0<1.                                      \tag{1}
\]

This is an explicit uniform relative positivity hypothesis, not merely
ampleness of the generic-fibre line bundle. The candidate does not assert
(1) for the pullback of every polarization to every resolved model.
Fix smooth Hermitian metrics \(h_i\) on \(\mathcal O(E_i)\), defining
sections \(\sigma_i\), and write \(\rho_i=|\sigma_i|_{h_i}^2\).

There is one \(\varepsilon>0\), independent of \(t\), such that the smooth
functions

\[
 q_{i,t}(z)=\int_0^1\log\bigl(\rho_i(z)+|t|^{2a}\bigr)\,da,
 \qquad
 \beta_t=\omega_h|_{X_t}+\varepsilon i\partial\bar\partial
             \sum_iq_{i,t}|_{X_t}                              \tag{2}
\]

define Kähler forms in \(c_1(\mathcal L|_{X_t})\), using the curvature
convention for which \(i\partial\bar\partial\) acts on potentials.
If the curvature convention includes a fixed positive factor, insert that
factor consistently in (2) and in the energy calculation below; the
comparison constants change by fixed factors.

Put \(T=|\log|t||\). In any fixed finite collection of adapted SNC charts
\(t=z_0\cdots z_m\), with transverse coordinates
\(z_{m+1},\ldots,z_n\), and on a relatively compact chart domain, fix
\(0<\delta<1/(m+1)\) when \(m\geq1\). On the logarithmic interior

\[
 x_i=-T^{-1}\log|z_i|\geq\delta\quad(0\leq i\leq m),
 \qquad \sum_{i=0}^m x_i=1,                                  \tag{3}
\]

there are constants \(C_\delta,T_\delta\), independent of \(t\), such that

\[
 \beta_t\geq C_\delta^{-1}\omega_{\mathrm{loc},t},\qquad
 \omega_{\mathrm{loc},t}
   =T^{-1}\sum_{j=1}^m i\,d\log z_j\wedge d\overline{\log z_j}
       +\sum_{j=m+1}^n i\,dz_j\wedge d\bar z_j,
 \quad T\geq T_\delta.                                      \tag{4}
\]

Only independent logarithmic coordinates enter (4). Condition (3) means
\(1-\sum_{i=1}^m x_i\geq\delta\), not the empty condition
\(1-\sum_{i=0}^m x_i>0\) printed in the source. For \(m=0\), (4) is just
the background comparison following from (1), without logarithmic terms.

## Scalar profile and global positivity

For fixed \(t\ne0\), every integrand in (2) is smooth even where
\(\rho_i=0\); on \(X_t\) the vertical defining sections are nonzero.
Consequently each \(q_{i,t}|_{X_t}\) is a global smooth real function.
Set

\[
 F_T(w)=\int_0^1\log(e^w+e^{-2aT})\,da,
 \qquad p_a=\frac{e^w}{e^w+e^{-2aT}}.
\]

Differentiation under the integral gives

\[
 0<F_T'(w)=\int_0^1p_a\,da<1,
 \qquad
 F_T''(w)=\int_0^1p_a(1-p_a)\,da
          =\frac{p_1-p_0}{2T},
 \qquad 0<F_T''(w)\leq\frac1{2T}.                           \tag{5}
\]

Indeed, \(\partial_a p_a=2Tp_a(1-p_a)\). Off \(E_i\), write
\(w_i=\log\rho_i\). Its complex Hessian extends smoothly across \(E_i\),
being minus the curvature of the fixed divisor metric, and has a uniform
lower bound \(-B\Omega\) on the compact region. The chain rule gives

\[
 i\partial\bar\partial q_{i,t}
 =F_T'(w_i)i\partial\bar\partial w_i
     +F_T''(w_i)i\partial w_i\wedge\bar\partial w_i
 \geq-B\Omega.                                             \tag{6}
\]

Take \(\varepsilon sB\leq c/4\) (with no restriction from this inequality
if \(B=0\)). Then (1), (2) and (6) imply
\(\beta_t\geq3c\Omega|_{X_t}/4\) globally. Its cohomology class is
unchanged because the added term is the Hessian of a global function.
The compactness bound \(\rho_i\leq M\) also gives

\[
 -T\leq q_{i,t}\leq\log(M+1),                              \tag{7}
\]

since the integrand is at least \(-2aT\). Thus the comparison potential
in (2) has oscillation \(O(T)\), with no uncontrolled logarithmic
singularity on an individual smooth fibre.

## Lower bound in the logarithmic interior

When \(-w/(2T)\in[\eta,1-\eta]\),
\(p_1\geq1-e^{-2\eta T}\) and \(p_0\leq e^{-2\eta T}\). Hence

\[
 F_T''(w)\geq\frac{1-2e^{-2\eta T}}{2T}
             \geq\frac1{4T}
 \quad\hbox{if }2\eta T\geq\log4.                         \tag{8}
\]

In an adapted chart \(\rho_j=|z_j|^2e^{\psi_j}\), with smooth
\(\psi_j\) whose value and differential are uniformly bounded relative
to \(\Omega\) on the fixed chart domains. By (3),
\(-w_j/(2T)\in[\delta/2,1-\delta/2]\) once \(T\) is sufficiently large.
For any tangent vector, the elementary inequality
\(|a+b|^2\geq|a|^2/2-|b|^2\) implies

\[
 i\partial w_j\wedge\bar\partial w_j
 \geq\tfrac12 i\,d\log z_j\wedge d\overline{\log z_j}
        -C\Omega.
\]

Use the lower bound (8) on its first term and the upper bound (5) on
the negative error. Keeping the positive terms for \(1\leq j\leq m\)
and discarding all other positive terms in (6), one obtains

\[
 \beta_t\geq\left(\frac{3c}{4}-\frac{\varepsilon C'}{T}\right)
                    \Omega|_{X_t}
             +\frac{\varepsilon}{8T}\sum_{j=1}^m
                        i\,d\log z_j\wedge d\overline{\log z_j}.
\]

For larger \(T_\delta\), the first coefficient is at least \(c/2\).
The ambient Kähler form controls the ordinary transverse coordinate forms
uniformly on these charts. This proves (4), for the same global metric.

## Energy consequence

Let \(\varphi_t\) be a smooth \(\omega_h|_{X_t}\)-psh function with
\(\operatorname{osc}_{X_t}\varphi_t\leq C_0T\), and suppose the fibrewise
intersection volume \(V=\int_{X_t}\omega_h^n\) is constant. Replace it
by \(u_t=\varphi_t-\sup_{X_t}\varphi_t\leq0\). Compactness, closedness
and integration by parts give

\[
 \begin{aligned}
 \int_{X_t}i\partial u_t\wedge\bar\partial u_t\wedge\beta_t^{n-1}
 &=\int_{X_t}(-u_t)i\partial\bar\partial u_t\wedge\beta_t^{n-1}\\
 &\leq\operatorname{osc}_{X_t}\varphi_t
         \int_{X_t}(\omega_h+i\partial\bar\partial u_t)
                           \wedge\beta_t^{n-1}\\
 &=\operatorname{osc}_{X_t}\varphi_t\,V
 \leq C_0VT.
 \end{aligned}                                             \tag{9}
\]

The inequality discards the nonpositive term
\(-\int(-u_t)\omega_h\wedge\beta_t^{n-1}\); positivity of the remaining
measure bounds it by the oscillation. Cohomology of all forms supplies
the next equality. By (4) and positivity of wedge products,

\[
 \int_{U_{\delta,t}}
       i\partial\varphi_t\wedge\bar\partial\varphi_t
                       \wedge\omega_{\mathrm{loc},t}^{n-1}
 \leq C_\delta T.                                         \tag{10}
\]

Up to the fixed dimension/convention factor, this is the local
\(L^2\)-gradient estimate in the source. No Ricci-flatness is needed for
this energy step. It does not itself give a pointwise comparison with a
same-log-fibre Haar average.

## Source relation and remaining limits

Li–Tosatti, *Diameter bounds for degenerating Calabi–Yau metrics*,
arXiv:2006.13068v2, Proposition 3.1 on physical page 5 and its proof on
pages 5–6, provides a related toric projective construction. Its metric
lies in \(T^{-1}c_1(L)\), with logarithmic lower bound \(T^{-2}\).
Multiplication by \(T\) gives the \(T^{-1}\) logarithmic coefficient in
the unscaled class; interpolation with a fixed Fubini–Study metric adds
transverse control. The printed conclusion is on its prescribed region
\(B_t\), while the proof describes the lower bound on adapted charts
near the selected maximal stratum. This is a relevant primary anchor,
not an authentication of what the unresolved citation in Li's later paper
was intended to denote. The published JDG edition has not been freshly
acquired in this checkpoint; the inspected locator is explicitly v2.

The independent construction (2) avoids using that locator, but requires
the uniform model positivity (1). Before applying it to an arbitrary
polarized meromorphic degeneration, one still needs a precise construction
of a suitable model and reference metric, or a projective-chart argument
whose pullbacks remain controlled on the chosen resolution. The existence
of such input is not silently inferred from generic ampleness.
Convergent chamber bases, uniform approximate domination, the Bergman
bound and the hybrid approximation argument also remain separate gates.
The active book and the open-problem inventory are unchanged by this
conditional research candidate.
