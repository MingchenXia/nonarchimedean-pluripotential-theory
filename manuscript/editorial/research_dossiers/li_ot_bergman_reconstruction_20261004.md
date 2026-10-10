# Point-extension and Bergman bound with explicit model hypotheses

Date: 4 October 2026. This book-external reconstruction supplies the
point-extension step discussed in Li, arXiv:2505.11087v1, Proposition 4.2,
and the published intermediate-limit paper, Proposition 6.7. It uses the
checked statement in Demailly's **July 2011 author manuscript**, Section
13.C, Theorem 13.6 and Remark 13.7(a), physical/printed pages 125–131.
The 2012 print edition's Section 12.C and Theorem 12.6, cited by Li, have
not been checked in that edition. No identification by theorem number is
claimed. No independent model-verifier receipt or novel-result admission
is supplied.

## Setting and bound

Let \(\pi:\mathcal X\to D\) be proper, with smooth total space of dimension
\(n+1\), \(n\geq1\), smooth connected projective fibres over \(D^*\), and
SNC central divisor \(\sum b_iE_i\), where \(b_i\) are positive integers.
Work near the preimage of a smaller closed disc. Let \(L\) be a line
bundle over \(\mathcal X|_{D^*}\). Assume there is a fixed integer \(k>0\),
an extension \(\mathcal A\) of \(L^k\), and sections
\(\tau_0,\ldots,\tau_P\) giving a closed immersion

\[
 (j,\pi):\mathcal X\hookrightarrow\mathbf P^P\times D,
 \qquad \mathcal A=j^*\mathcal O(1).
\]

Equip \(\mathcal A\) with its Fubini–Study Hermitian metric, and equip
\(L\) on the punctured family with its \(k\)-th root \(h\), using the
fixed identification there. Thus \(h^k\) extends smoothly, and
\(\theta=i\Theta_h=k^{-1}j^*\omega_{\rm FS}\) on each fibre is Kähler.
This permits a positive rational model extension of \(L\); an integral
extension of \(L\) itself with positive curvature is not assumed.
Throughout, \(|v|_h^2\) denotes the squared Hermitian norm.

Let \(\Omega\) be a meromorphic \((n+1,0)\)-form on \(\mathcal X\),
holomorphic and nonvanishing on the punctured family. The relative form
\(\Omega_t\), defined by \(\Omega=dt\wedge\Omega_t\) on smooth fibres,
is assumed to trivialize \(K_{X_t}\). Its zero and pole divisors are
vertical. Put \(d\nu_t=i^{n^2}\Omega_t\wedge\overline{\Omega_t}\).
There is no probability normalization in this measure.

Let \(\varphi_t\) be smooth and

\[
 \theta|_{X_t}+2i\partial\bar\partial\varphi_t\geq0,
 \qquad \operatorname{osc}_{X_t}\varphi_t\leq C_0T,
 \qquad T=-\log|t|\geq1.                                  \tag{1}
\]

There are fixed \(N\) and \(C\), independent of \(l,t,z\), such that
for every integer \(l\geq N\) and every \(z\in X_t\), there is
\(S\in H^0(X_t,L^l)\), \(S(z)\ne0\), with

\[
 \int_{X_t}|S|_{h^l}^2e^{-2l\varphi_t}\,d\nu_t
 \leq e^{CT}|S(z)|_{h^l}^2e^{-2l\varphi_t(z)}.               \tag{2}
\]

Equivalently, taking logarithms and dividing by \(2l\),

\[
 \frac1{2l}\log\int_{X_t}|S|_{h^l}^2e^{-2l\varphi_t}\,d\nu_t
 \leq \left(\frac1l\log|S|_{h^l}-\varphi_t\right)(z)
       +\frac{CT}{2l}.                                    \tag{3}
\]

Changing \(C\) absorbs the harmless factor two. This is a conditional
analytic estimate with the projective-model, meromorphic-volume and
oscillation inputs displayed; it does not prove the general hybrid limit.

## Uniform projective Jacobian bound

Choose the affine chart at \(z\) on which \(|\tau_a(z)|_{h^k}\) is
maximal, and relabel it \(a=0\). Write
\(w_i=\tau_i/\tau_0\). Then \(|w_i(z)|\leq1\) and
\(|\tau_0(z)|_{h^k}\geq(P+1)^{-1/2}\). There are finitely many such
affine chart choices. Their closed regions with \(\tau_a\) maximal
are compact over the smaller closed disc.

Cover the central fibre by finitely many relatively compact SNC coordinate
charts. After absorbing the unit into one coordinate, their equations are

\[
 t=z_0^{b_0}\cdots z_m^{b_m},
 \qquad z_0,\ldots,z_n\text{ coordinates on }\mathcal X.
\]

This absorption uses a local holomorphic root of a nonvanishing unit;
it is unrelated to taking a root of \(t\). For sufficiently small \(t\),
properness puts the whole nearby fibre inside this finite cover.
On each chart \(|z_a|\leq R\) for one uniform \(R\geq1\), so, on the
punctured fibre,

\[
 \max_a|\partial t/\partial z_a|
 \geq b_0|t|/|z_0|\geq R^{-1}|t|.                         \tag{4}
\]

Because \((j,\pi)\) is an immersion, the covectors \(dw_i,dt\) span
the cotangent space of the smooth total space. On the compact chart
regions a bounded right inverse expresses each \(dz_a\) as a linear
combination of these covectors, with uniformly bounded coefficients.
Wedge \(n\) such identities with \(dt\). Terms containing another
\(dt\) vanish; therefore

\[
 \max_{|I|=n}
 \left|\frac{dw_I\wedge dt}{dz_0\wedge\cdots\wedge dz_n}\right|
 \geq c\max_a|\partial t/\partial z_a|\geq c'|t|.          \tag{5}
\]

The constants are uniform on the finite cover. A common integer \(M\geq0\)
makes \(t^M\Omega\) holomorphic there, since the poles are supported
on finitely many vertical components and \(\operatorname{ord}_{E_i}t=b_i>0\).
In the fixed coordinate frames this gives
\(|\Omega/(dz_0\wedge\cdots\wedge dz_n)|\leq C|t|^{-M}\).
Consequently, some index set \(I\) of size \(n\) satisfies

\[
 \left|\frac{dw_I}{\Omega_t}(z)\right|
 \geq c|t|^{M+1}.                                         \tag{6}
\]

The wedge sign from ordering \(dt\) has no effect on the modulus.
This argument uses the whole finite wedge family. The assertion that an
arbitrarily chosen meromorphic quotient has a uniform lower bound would
not suffice: such a quotient can have horizontal zeros.

## Transverse zero scheme through the prescribed point

For the chosen \(I\), set
\(s_i^0=\tau_{I_i}-w_{I_i}(z)\tau_0\). These sections vanish at \(z\)
and have coefficient vectors bounded independently of \(t,z\). At \(z\),
their differentials are \(\tau_0(z)dw_{I_i}\); the lower bound on
\(|\tau_0(z)|_{h^k}\) preserves (6), up to a fixed factor.

Let \(H_z\) be the finite-dimensional vector space of all linear
combinations of the \(\tau_a|_{X_t}\) vanishing at \(z\). At any
\(y\ne z\), evaluation \(H_z\to L_y^k\) is onto, since the projective
embedding separates \(y\) and \(z\). Hence the universal evaluation
map for tuples in \(H_z^n\), over \(X_t\setminus\{z\}\), is a
submersion in the parameter directions at its zeros. Sard's theorem
applied to the projection of its smooth zero locus says that almost every
tuple is transverse to zero at all zeros away from \(z\).
This is the usual parametric transversality argument; no quantitative
lower bound on derivatives at those other zeros is needed.

Transversality at \(z\), with at least half the Jacobian in (6), is an
open condition on the tuple. Thus there is an arbitrarily small generic
perturbation \((s_1^0,\ldots,s_n^0)\) inside \(H_z^n\) preserving that
lower bound and the uniform coefficient bound. Its full zero scheme on
the compact fibre is transverse, zero-dimensional and finite. The size
of the permitted perturbation may depend on \(t,z\); the constants used
in the estimate depend only on the retained Jacobian and coefficient
bounds, not on a uniform perturbation radius.

Multiply the tuple by one fixed positive scalar \(\epsilon\) small
enough to get

\[
 s\in H^0(X_t,E),\quad E=(L^k)^{\oplus n},\quad
 |s|_E\leq e^{-1},\quad
 J_t(z):=|\Lambda^n(ds)/\Omega_t|_{\det E}(z)
       \geq c|t|^\kappa,\quad \kappa=M+1.                 \tag{7}
\]

Indeed \(\sum_a|\tau_a|_{h^k}^2=1\) globally for the chosen FS
metric, so bounded coefficients control the tuple on the entire fibre.
The scalar multiplies the determinant by \(\epsilon^n\), a fixed factor.
Write \(Y=s^{-1}(0)\). It contains \(z\); all its points are regular.

## Curvature conditions of the checked extension theorem

Give \(E\) the direct-sum metric induced by \(h^k\). Then
\(i\Theta_E=k\theta\otimes\mathrm{Id}\), and the local sum-of-squares
formula gives

\[
 i\partial\bar\partial\log|s|_E^2\geq-k\theta
 \quad\text{on }X_t\setminus Y.                           \tag{8}
\]

Choose the **separate** fixed integer \(N=(n+1)k+1\), and give the
line bundle \(F=L^l\), \(l\geq N\), the Hermitian metric
\(H=h^l e^{-2(l-N)\varphi_t}\). Its curvature is

\[
 i\Theta_H=N\theta+(l-N)(\theta+2i\partial\bar\partial\varphi_t).
\]

By (1) and (8),

\[
 i\Theta_H+n i\partial\bar\partial\log|s|_E^2
 \geq (N-nk)\theta
 =(k+1)\theta
 \geq\frac{\{i\Theta_Es,s\}}{|s|_E^2}.                  \tag{9}
\]

Thus Demailly 2011, Theorem 13.6(a), holds with \(r=n\) and
\(\alpha=1\); the left side is semipositive, indeed strictly positive
on the fibre. Condition (b) is (7). The logarithmic condition at zeros
is understood with its usual current extension. The compact Kähler fibre
is weakly pseudoconvex in the stated sense: a constant smooth psh
function is an exhaustion, because the fibre itself is compact.
All zeros are transverse, and only \(q=0\) is used.

The tensor degree \(k\) defining the auxiliary vector bundle and the
reserved positive curvature degree \(N\) are different constants.
Using a single \(N_0\) for both, as in the compressed source display,
does not by itself check (9). Increasing the reserved degree separately
costs only a fixed multiple of the oscillation in the next step.

## Extension estimate and restoration of the full weight

Prescribe \(f\in (K_{X_t}\otimes F)|_Y\) by
\(f(z)=\Omega_t(z)\otimes v\), with any \(v\ne0\) in \(L_z^l\), and
\(f(y)=0\) at every other point of \(Y\). A section over this finite
smooth zero-dimensional manifold is holomorphic and has finite right-hand
norm. The theorem gives a holomorphic extension \(F_{\rm ext}\).
Divide it by the nonvanishing \(\Omega_t\) to obtain \(S\), with
\(S(z)=v\). Remark 13.7(a) identifies the integral norms independently
of the chosen Kähler metric. In particular the estimate is

\[
 \int_{X_t}\frac{|S|_{h^l}^2e^{-2(l-N)\varphi_t}}
 {|s|_E^{2n}(-\log|s|_E)^2}\,d\nu_t
 \leq C_n|v|_{h^l}^2e^{-2(l-N)\varphi_t(z)}J_t(z)^{-2}.    \tag{10}
\]

Terms at the other points of \(Y\) vanish exactly; their possibly small
Jacobian determinants do not enter the bound. For \(n\geq1\),
\(r^{2n}(-\log r)^2\) is bounded above on \(0<r\leq e^{-1}\), and
tends to zero at zero. Thus the ordinary weighted integral is bounded
by a fixed multiple of the left side of (10). Using (7), it is at most

\[
 C e^{2\kappa T}|v|_{h^l}^2e^{-2(l-N)\varphi_t(z)}.
\]

Multiplication of the integrand by \(e^{-2N\varphi_t}\) and use of its
maximum gives the stronger full-weight estimate

\[
 \int_{X_t}|S|_{h^l}^2e^{-2l\varphi_t}\,d\nu_t
 \leq C e^{2\kappa T+2N\operatorname{osc}\varphi_t}
        |v|_{h^l}^2e^{-2l\varphi_t(z)}.
\]

Apply (1) and \(T\geq1\) to absorb the fixed multiplicative constant.
This proves (2)–(3). The proof is invariant under scalar shifts of
\(\varphi_t\); an absolute-value normalization was not required.

## Limits of this checkpoint

This isolates the OT/Bergman estimate from chamber-basis, generic-region
domination, uniform hybrid approximation and identification of the limit.
It imports the checked 2011 \(q=0\) extension theorem; it does not
independently reprove all of its analytic dependencies, its \(q>0\)
regularity claim, or the corresponding printed 2012 theorem.
Sard's theorem and elementary compact immersion linear algebra are used
explicitly. A separate model construction must supply the relative
embedding and the meromorphic volume input for a given degeneration.
The active 4,244-page manuscript and all 42 open-problem statuses are
unchanged. No priority claim or external verification verdict is made.
