# Canonical volume, uniform Skoda and punctured-parameter continuity

Date: 4 October 2026. This conditional, book-external reduction checks
three remaining analytic inputs of the hybrid CY route in a supplied
projective germ/model category. Classical existence, proper coherent
comparison, the published Skoda theorem and elliptic/implicit-function
theory remain imports. No principal general theorem, exact-current
independent verifier verdict or open-problem status is promoted.

## Signature and the two distinct model interfaces

Let \(R=\mathbb C\{t\}\), \(F=\operatorname{Frac}R\),
\(K=\mathbb C((t))\). Assume a flat projective finite-presentation
model over \(R\), with geometrically integral generic fibre, and its
projective analytic germ realization. Its smooth connected complex
fibres \(X_t\), of dimension \(n\geq1\), have holomorphically trivial
canonical bundle for every sufficiently small \(t\ne0\).
Assume a regular total model and an invertible sheaf \(\mathcal K_R\)
whose analytic realization extends the relative canonical bundle;
on the regular total space it is
\(K_{\mathcal X}\otimes\pi^*K_D^{-1}\).
The proper section/cohomology comparison and finite coefficient descent
are those of `li_geometric_section_module_20261004.md`.

For the Skoda step assume further that the model is **reduced SNC**
and has the positive rational model presentation of
`li_positive_model_bridge_20261004.md`. Namely some power of its
relatively ample line bundle gives a closed immersion into
\(\mathbf P^N\times D\), with generic restriction a fixed power of
the polarization \(L\). Let \(h\) be its root reference on \(L\)
over the punctured family, and put \(\theta=i\Theta_h\).
Then \(\theta\) is a smooth semipositive form on the total model,
positive on each fibre, and

\[
 \Omega_{\mathcal X}=\tfrac12\theta+i\,dt\wedge d\bar t
 \quad\text{is a fixed total-space Kähler form},\qquad
 \omega_t=\frac{\theta|_{X_t}}{2T}
          =\frac{\Omega_{\mathcal X}|_{X_t}}{T},
 \quad T=-\log|t|\geq1.                                  \tag{1}
\]

This follows from the immersion of the pair of projective and parameter
maps. It is not inferred from generic ampleness on an arbitrary model.
The scalar factor two matches the norm convention
\(h e^{-2\varphi}\), with \(dd^c=i\partial\bar\partial\).
The finite-cover route may supply this reduced model, but its
existence and the projective germ/model comparison are separate inputs.

## Fibrewise CY gives a meromorphic family of volume forms here

The freeness and actual-small-fibre comparison in the geometric
section-module derivation require invertibility, flatness, properness
and finite presentation, not ampleness. Ampleness was used later only
for generation of the polarization. Apply its cohomological part to
\(\mathcal K_R\). Perfect derived cohomology and flat generic base
change give a finite free module

\[
 M=H^0(\mathcal X_R,\mathcal K_R),\qquad
 M\otimes_RF=H^0(X_F,K_{X_F}).                            \tag{2}
\]

Finite coefficient descent and splitting of the finite cohomology
complex give its full section basis on all sufficiently small nonzero
complex fibres. This is the already recorded finite-germ construction,
not evaluation of the whole germ ring at a nonzero parameter.

Since \(X_t\) is compact and connected, its holomorphic functions
are constant. Canonical triviality thus gives
\(\dim H^0(X_t,K_{X_t})=1\). The constant rank on those fibres in
(2) is therefore one. Choose a nonzero generator of the meromorphic
generic module. Its analytic realization \(\Omega_t\) is a basis
on every sufficiently small nonzero fibre. Such a section of a trivial
canonical bundle is nowhere zero: divide it by any fibrewise
trivialization and use constancy of holomorphic functions.

Tensor the meromorphic relative section with the base frame \(dt\)
to obtain a meromorphic top form \(\Omega\) on the total model.
On the punctured submersion it has the usual identity
\(\Omega=dt\wedge\Omega_t\). Its zero and pole divisors are
vertical, since every \(\Omega_t\) is nowhere zero. This supplies
both the positive fibrewise raw volume \(\nu_t=|\Omega_t|^2\)
and the meromorphic total form required by the OT reconstruction.
It is the projective/germ comparison that controls meromorphicity;
fibrewise triviality in an arbitrary analytic family with essential
singularities is not substituted for (2).

Changing the generic generator by a meromorphic scalar changes raw
volume by a positive fibre scalar, but leaves
\(\mu_t=\nu_t/\nu_t(X_t)\) unchanged. The choice can be fixed once
for all degrees; no degree-dependent canonical trivialization is needed.

## Check the density upper bound on every model chart

On a reduced SNC chart \(t=z_0\cdots z_p\), with remaining ordinary
coordinates \(w\), write the divisor of the total form as
\(\sum_i c_iE_i\). Each \(c_i\) is an integer. A local unit gives

\[
 \Omega=f\prod_{i=0}^p z_i^{c_i}
                       dz_0\wedge\cdots\wedge dz_p\wedge dw,
 \quad
 \Omega_t=\pm f\prod_{i=0}^p z_i^{c_i}
                       d\log z_1\wedge\cdots\wedge d\log z_p
                                                   \wedge dw.  \tag{3}
\]

Wedging the latter with \(dt=t\sum_i d\log z_i\) checks the
exponents and avoids an erroneous extra pole in every variable.
Here \(f\) is holomorphic and nowhere zero after removing the
displayed vertical divisor. Shrink finitely many relatively compact
charts so its absolute value has uniform upper and lower bounds.

Let \(\kappa=\min_i c_i\). Unlike the nonreduced case, this is an
integer. Multiplying \(\Omega\) by \(t^{-\kappa}\) makes
\(a_i=c_i-\kappa\geq0\) with minimum zero. It leaves probabilities
unchanged. Put

\[
 m=\max\{|J|-1:E_J\ne\varnothing,\ a_i=0\ (i\in J)\}.
                                                               \tag{4}
\]

The published BJ volume asymptotic, in the prior volume derivation,
gives \(\nu'_t(X_t)\asymp T^m\) for the shifted raw volume.
It gives a positive lower bound of that order as well as an upper
bound. Consequently (3) gives, **on every chart**, including charts
meeting nonessential components,

\[
 d\mu_t\leq \frac{C}{T^m}\prod_{i=0}^p|z_i|^{2a_i}
     \prod_{j=1}^p i\,d\log z_j\wedge d\log\bar z_j
     \prod_a i\,dw_a\wedge d\bar w_a.                    \tag{5}
\]

Signs are understood by the fixed positive orientation. Constants
from the norm convention are absorbed in \(C\). Properness places
every small fibre in finitely many such charts, so this is the uniform
upper bound of class \((a_i)\) in the published Skoda source's (4).
The earlier comparison only on compact top essential-stratum charts
would not by itself have supplied this global hypothesis.

## The published analytic-model theorem and reference changes

Li, *Uniform Skoda integrability and Calabi–Yau degeneration*,
Analysis & PDE 17 (2024), 2247–2256, DOI
`10.2140/apde.2024.17.2247`, is the controlling edition.
Theorem 1.3 is stated for a polarized **algebraic** CY degeneration
over a smooth affine curve. It is not cited as a theorem for arbitrary
meromorphic analytic families.

Section 2, physical p. 3 / printed p. 2248, instead works with a
flat projective family over a small analytic disc, smooth total space,
smooth connected punctured fibres, reduced SNC central fibre and a
fixed total-space Kähler background. Theorem 2.9, physical p. 9 /
printed p. 2254, applies to measures satisfying precisely (5).
Its background is \(\Omega_{\mathcal X}|_{X_t}/T\), which equals
(1). Thus in this supplied model category there are fixed
\(\alpha,A>0\) such that

\[
 \int_{X_t}e^{-\alpha v}d\mu_t\leq A
 \quad(v\in\operatorname{PSH}(X_t,\omega_t),\ \sup v=0).
                                                               \tag{6}
\]

This is a source-checked import, not an independent reproduction of
its barycentric-model, local Skoda or pluripotential antecedents.
Theorem 3.1, physical p. 10 / printed p. 2255, gives the uniform
\(C^0\) bound for the smooth normalized MA solution from (6),
with dependence only on \(n,\alpha,A\). The prior uniform
truncation/approximate-domination derivation uses exactly these data.

The elementary change-of-background check is useful. If
\(\omega_1=\omega_2+dd^cb_t\) with \(\|b_t\|_\infty\leq B\),
a normalized \(\omega_1\)-psh test \(v\) becomes
\(v+b_t-\sup(v+b_t)\), a normalized \(\omega_2\)-psh test.
The two tests differ by at most \(2B\), so a bound (6) for
\(\omega_2\) gives one for \(\omega_1\) with
\(A_1\leq e^{2\alpha B}A_2\). For model references the earlier
vertical-divisor comparison has \(\|\chi_t/T\|_\infty\leq B\)
after shrinking the disc. This proves uniformity under the fixed
meromorphic change; it does not permit an essential-singularity
reference or an uncontrolled parameter scalar. The curvature forms
and the sign of their potential change must use the same convention.

## Continuity in the punctured parameter is a separate step

Assume classical smooth CY existence and uniqueness on each compact
Kähler fibre. The density \(\nu_t\), complex structure, bundle and
positive reference depend smoothly on the punctured total family.
Fix \(t_*\ne0\). Proper smooth submersion gives an Ehresmann
trivialization over a small neighborhood of \(t_*\), so the equation
can be considered on one fixed compact differentiable manifold.
Ehresmann, the Banach implicit-function theorem and the compact
elliptic inverse/Schauder theory are explicit imports in this step;
their primary proofs are not newly certified here.

Use a mean normalization first. For \(0<\beta<1\) and integer
\(k\geq0\), the positive-curvature domain is open in
\(C^{k+2,\beta}\). Consider the equation and normalization

\[
 \mathcal F(t,\varphi,c)
   =\left(\log\frac{(\theta_t+2dd_t^c\varphi)^n}{\nu_t}-c,
                  \int_{X_t}\varphi\,d\mu_t\right)=(0,0).
                                                               \tag{7}
\]

The parameter here is real two dimensional; no holomorphic or
parameter-psh dependence of \(\varphi\) is being assumed.
Integration of the first equation fixes
\(e^c=\int\theta_t^n/\nu_t(X_t)\). At a solution, the volume
\((\theta_t+2dd_t^c\varphi)^n\) is a positive scalar times
\(\mu_t\). With
\(\Delta=\operatorname{tr}_{\theta_t+2dd_t^c\varphi}dd_t^c\),
the derivative in the unknowns is

\[
 (v,a)\longmapsto\left(2\Delta v-a,\ \int v\,d\mu_t\right).
                                                               \tag{8}
\]

It is an isomorphism
\(C^{k+2,\beta}\times\mathbb R\to C^{k,\beta}\times\mathbb R\).
Indeed the Laplacian's kernel on a connected compact fibre consists
of constants and its integral is zero against its own volume.
For target \((f,b)\), take \(a=-\int f\,d\mu_t\), solve
\(2\Delta v=f+a\) with zero mean, and add the constant \(b\).
Schauder theory gives its bounded inverse. No estimate uniform as
\(t\to0\) is asserted for this inverse.

The implicit-function theorem supplies a smooth local parameter
family in this mean normalization. Elliptic regularity at all
\(k\) and uniqueness identify the local solutions with the fibrewise
CY metrics and patch them on the punctured base. In particular their
potentials are continuous on the punctured total family.

Changing to the normalization used in the FS argument subtracts
\(s(t)=\sup_{X_t}\varphi_t\). Under the local proper smooth
trivialization, uniform convergence of the potentials makes \(s(t)\)
continuous. It need not be smooth when maximizers change. Subtracting
it retains total continuity, fibrewise smoothness, the MA equation
and \(\sup\varphi_t=0\). Dividing by the smooth positive function
\(T\) preserves continuity there. Hence the precise punctured-family
continuity hypothesis of the prior hybrid argument is satisfied.

For \(u_t=\varphi_t/T\), (1) gives
\(\omega_t+dd^cu_t=(\theta_t+2dd^c\varphi_t)/(2T)\).
Dividing its volume by its total mass recovers \(\mu_t\); factors
\((2T)^n\) cancel. Applying Theorem 3.1 after this scaling gives
\(-C\leq u_t\leq0\), equivalently oscillation \(O(T)\) for the
unscaled norm potential, as needed by the energy and OT estimates.

## What is supplied and what remains conditional

In the supplied projective germ and reduced positive-model category,
fibrewise CY triviality now supplies the meromorphic relative/total
volume form; all-chart volume bounds match the analytic-model Skoda
theorem; and the elliptic reduction supplies punctured-family
continuity in the correct normalization. No density estimate is
inferred solely from a generic region, and no analytic family is
silently made algebraic to use Theorem 1.3.

The category itself, existence of the regular reduced projective
cover/model, finite model modifications and meromorphic polarization
identifications remain inputs. Proper cohomological comparison,
classical CY/elliptic theory, the published Skoda theorem and the prior
hybrid/NA imports remain explicit source dependencies. This is not an
independent certification of every cited proof. Singular/disconnected
fibres, nonprojective/essential-singularity degenerations and positive
or mixed characteristic are outside the signature. Volume and Skoda
also allow \(m=0\); the earlier dyadic proof still requires
\(1\leq m\leq n\), so this note does not fill that boundary by
implication. Exact-current independent verification is still required
for book admission. All 42 statuses and the active book remain fixed.
