# Enlarged dyadic parents, generic oscillation and Fourier bounds

Date: 4 October 2026. This book-external conditional derivation addresses
the domains and estimates in Li, arXiv:2505.11087v1, Sections 4.2–4.3.
The printed dyadic annulus is \(R_i\leq|z_i|\leq2R_i\), whereas the
displayed "shrunken" annulus (16) begins at \(2R_i/3<R_i\). Thus (16)
is not contained in its proposed parent. A smaller core alone would also
leave radial gaps. The construction below retains full dyadic core
coverage and measures energy on enlarged parents of bounded overlap.
This repairs that local route under stated model, measure and section
inputs; it does not certify the principal general hybrid theorem.

## Fixed chart and geometric inputs

Fix \(0<\varepsilon<1/3\).
Use a reduced SNC chart \(t=z_0\cdots z_m\), \(1\leq m\leq n\),
independent logarithmic variables \(z_1,\ldots,z_m\), and transverse
variables \(w\in\mathbb C^{n-m}\). Work on a fixed compact logarithmic
interior, with a larger interior available around it, and a transverse
polydisc \(W\) whose closure lies in the stratum chart. Let \(W_c\)
be a concentric smaller polydisc. All angular variables are unrestricted.
Put \(T=-\log|t|\geq1\), and use

\[
 g_t=T^{-1}\sum_{i=1}^m i\,d\log z_i\wedge d\overline{\log z_i}
       +\sum i\,dw_j\wedge d\bar w_j,
 \qquad dV_{g_t}=c_nT^{-m}\,d\lambda,                     \tag{1}
\]

where \(d\lambda\) is the product of logarithmic radial/angular
Lebesgue measure and ordinary transverse Lebesgue measure; the fixed
constant \(c_n>0\) is immaterial. Assume the normalized CY probability
measure obeys \(c^{-1}dV_{g_t}\leq d\mu_t\leq c\,dV_{g_t}\) on these
charts. For the later section integral assume also
\(c^{-1}d\lambda\leq d\nu_t\leq c\,d\lambda\), for the raw volume
form used in the Bergman bound. These are separate normalization inputs.
The latter is the usual minimally weighted maximal-stratum normalization;
it is not inferred from probability normalization alone.

Let \(\varphi_t\) be smooth, of oscillation \(O(T)\), with a bounded
smooth local background potential \(\rho_t\) such that
\(\varphi_t+\rho_t\) is psh in the independent fibre coordinates.
Normalize \(\varphi_t\) by a scalar to have absolute bound \(CT\).
Suppose the global comparison-metric argument supplies, on the larger
chart interiors,

\[
 \int |\nabla\varphi_t|_{g_t}^2\,dV_{g_t}\leq A T.         \tag{2}
\]

A fixed finite chart collection is permitted; overlap and chart constants
can depend on the chosen discarded-mass and tensor-degree parameters.
They are independent of \(t\) once those parameters are fixed.
Assume that the selected compact interiors and transverse cores cover
probability mass at least \(1-\varepsilon\). If chamber walls depend
on the degree, choose their deleted neighbourhoods **after fixing that
degree**, with total mass at most the prescribed \(\varepsilon\).
The geometric and wall deletions share this one \(\varepsilon\) budget;
they are already included in the stated mass of the selected region.
A uniform number or width of walls across all degrees is not assumed.

## Full cores and larger parents

For \(R_i=2^{j_i}\), let the core be

\[
 C_j=W_c\times\prod_{i=1}^m\{R_i\leq|z_i|\leq2R_i\},
\]

Use its intersection with the selected compact interior for the mass
cover, but keep \(C_j\) itself a **full** annular product for every
integral and pointwise estimate below. Estimate it using the full parent

\[
 P_j=W\times\prod_{i=1}^m\{R_i/2<|z_i|<4R_i\}.           \tag{3}
\]

Take only cores meeting the chosen compact region, but use their full
annuli for the estimates. For sufficiently large \(T\), all corresponding
parents remain inside the larger chart region: changing the radii by a
fixed factor changes every \(x_i=-\log|z_i|/T\) by \(O(T^{-1})\),
and changes \(x_0=1-\sum_{i=1}^m x_i\) by \(O(mT^{-1})\).
Away from a fixed wall neighbourhood, the whole parent lies in the same
chamber once \(T\) is large enough. This threshold may depend on the
degree and wall neighbourhood. The compact transverse core also leaves
a fixed margin inside \(W\).

The full cores cover the selected region. Parent overlap is bounded by
a constant depending only on \(m\) and the finite chart collection:
in one logarithmic radius a point belongs to at most four intervals
\((R/2,4R)\), so at most \(4^m\) product parents per chart.
There are at most \(C T^m\) relevant cores, each parent has
\(g_t\)-volume between two fixed positive multiples of \(T^{-m}\),
and each core has \(\mu_t\)-mass at most \(C T^{-m}\).
These facts use logarithmic radial lengths, not ordinary shrinking
Euclidean volumes.

Let \(M\) bound parent overlap. A parent is bad if

\[
 E(P_j):=\int_{P_j}|\nabla\varphi_t|_{g_t}^2dV_{g_t}
                  >H\varepsilon^{-1}T^{1-m}.              \tag{4}
\]

By (2), \(\sum_jE(P_j)\leq MA T\); hence the number of bad parents is
at most \(MA\varepsilon T^m/H\). The probability mass of their cores
is at most \(CMA\varepsilon/H\). Choose fixed \(H\geq\max\{1,CMA\}\) to make
this at most \(\varepsilon\). A parent with zero energy is included
among the good ones. All subsequent constants may depend on \(H\) and
\(\varepsilon\), but not on \(t\).

## Conditional averages and the pointwise upper bound

For fixed radii \(r=(|z_1|,\ldots,|z_m|)\), define
\(\bar\varphi_t(r)\) as the flat average over the angular torus and
\(W\). Poincaré on that connected product, whose angular metric is
scaled by \(T^{-1}\) and whose transverse diameter is fixed, has a
constant bounded uniformly for \(T\geq1\). Applying it for each radius
and integrating gives, on a good parent,

\[
 \int_{P_j}|\varphi_t-\bar\varphi_t(r)|^2dV_{g_t}
 \leq C E(P_j)\leq CH\varepsilon^{-1}T^{1-m}.             \tag{5}
\]

For zero transverse dimension, \(W\) denotes a one-point factor with
unit mass; the torus Poincaré estimate alone is enough.
The averaged psh function \(\varphi_t+\rho_t\) is convex in logarithmic
radii. Its \(O(T)\) bound on a larger fixed simplex gives an \(O(T)\)
Lipschitz bound in the normalized \(x\)-coordinates on the smaller
interior, by the elementary convex-function interior estimate.
Across one parent \(|\Delta x|=O(T^{-1})\), so its averaged oscillation
is \(O(1)\). Subtracting the bounded average of \(\rho_t\) retains

\[
 |\bar\varphi_t(r)-\bar\varphi_t(r')|\leq C
 \quad(r,r'\text{ in one parent}).                       \tag{6}
\]

Fix \(y\) in its core. A complex polydisc centred at \(y\), with radii
fixed small multiples of \(|z_i(y)|\) and fixed transverse radii, lies
inside \(P_j\). Submean for the psh function \(\varphi_t+\rho_t\),
boundedness of \(\rho_t\), and Cauchy–Schwarz give

\[
 \varphi_t(y)-\bar\varphi_t(r_y)
 \leq C+C\left(\frac1{\operatorname{Vol}_{g_t}P_j}
        \int_{P_j}|\varphi_t-\bar\varphi_t(r_y)|^2dV_{g_t}\right)^{1/2}
 \leq C_\varepsilon\sqrt T.                             \tag{7}
\]

For the first inequality, ordinary polydisc measure and logarithmic
measure have bounded relative densities on the parent after rescaling
\(z_i/R_i\). The polydisc and parent have comparable \(g_t\)-volumes,
both proportional to \(T^{-m}\). Equation (5), (6), and this volume
bound prove the second inequality. The argument uses a genuine interior
polydisc; it never estimates a point outside its energy parent.

Enumerate the finite chart/core collection and assign each surviving
selected point to its first good core. This gives a measurable partition;
each point's average below is the average for that assigned parent.
There are \(O(T^m)\) good cores. Summing (5) on this partition and using
\(\mu_t\asymp dV_{g_t}\) bounds the integral of
\(|\varphi_t-\bar\varphi_t|^2\) by \(C_\varepsilon T\).
Choose \(K_\varepsilon\) large enough that Chebyshev excludes mass at
most \(\varepsilon\) where
\(|\varphi_t-\bar\varphi_t|>K_\varepsilon\sqrt T\).
Call the remaining selected good-core points \(U_t\). Together with
the geometric and bad-parent deletions,

\[
 \mu_t(X_t\setminus U_t)\leq3\varepsilon.                 \tag{8}
\]

For every \(\zeta\in U_t\) and its good core, (6)–(7) imply
\(\varphi_t(y)\leq\varphi_t(\zeta)+C_\varepsilon\sqrt T\)
on the **whole core**, the domain used for the following section integral.
The comparison with an average has an error term justified by energy;
a bare pointwise bound by the same-log-fibre Haar average is not used.

## Fourier and remainder estimates on a fixed chamber

Fix a tensor degree and one convergent chamber basis \(s_i\). Assume
on these full cores it has leading terms
\(\tilde s_i=f_i(w)z^{\alpha_i}\), with the \(f_i\) linearly independent
over \(\mathbb C\) within each class modulo \(\mathbb Z(1,\ldots,1)\).
Assume the analytic leading expansions have uniform remainder bounds

\[
 |s_i-\tilde s_i|\leq C_l e^{-\eta T}
 |t|^{\alpha_{0,i}}\prod_{j=1}^m R_j^{\alpha_{j,i}-\alpha_{0,i}}
 \quad\text{on the core},\qquad\eta>0,                   \tag{9}
\]

and bounded leading coefficients there. These are explicit fixed-degree,
fixed-wall-gap inputs, not inferred merely from formal expansions.
A smooth model norm is uniformly equivalent to the local trivial norm
for this fixed degree.

Eliminate \(z_0=t/(z_1\cdots z_m)\). Different exponent classes give
different angular Fourier frequencies
\((\alpha_{1,i}-\alpha_{0,i},\ldots,\alpha_{m,i}-\alpha_{0,i})\).
Their cross terms integrate to zero over the full angular torus. Within
one class the Gram matrix of the functions \(f_i\) on the open transverse
core is positive definite: a zero integral would give a holomorphic
linear relation there, hence a relation on the connected coefficient
chart. When the transverse dimension is zero this says that each class
contains at most one basis vector with nonzero constant coefficient.

Radial integration over \([R_i,2R_i]\) changes the fixed monomial
weights by bounded factors. Write those weights as \(W_i\). The leading
term integral is thus at least \(c_l\sum |a_i|^2W_i^2\).
Equation (9) bounds the remainder integral by
\(C_l e^{-2\eta T}\sum |a_i|^2W_i^2\), after Cauchy–Schwarz in the
fixed finite index set. The triangle inequality in \(L^2\), for large
\(T\) depending on these fixed data, absorbs this error. The raw measure
comparison and the pointwise section bound give

\[
 \int_{C_j}\left|\sum a_is_i\right|_{h^l}^2d\nu_t
       \geq c_l\sum_i|a_i|^2|s_i(\zeta)|_{h^l}^2.          \tag{10}
\]

The constant may depend on the degree, chart and wall gap; it is uniform
in \(t,\zeta,a_i\). It follows from (7)–(8) on this core that

\[
 \frac1{2l}\log\int_{X_t}\left|\sum a_is_i\right|_{h^l}^2
                       e^{-2l\varphi_t}d\nu_t
 \geq\max_i\left\{\frac1l\log|a_is_i(\zeta)|_{h^l}
                         -\varphi_t(\zeta)\right\}
                  -C_{\varepsilon,l}\sqrt T.             \tag{11}
\]

Fixed logarithmic constants are absorbed since \(T\geq1\). Zero
coefficients use \(\log0=-\infty\); the identically zero sum is trivial
in the extended sense. Equations (8), (11) supply the local mass and
weighted no-cancellation estimate needed by the fixed-matrix replacement.

## Remaining scope

This proof retains the chart, global energy, measure normalization and
analytic leading-remainder hypotheses. The model geometry and uniform
Skoda inputs still require their own application checks. Chamber count
and all intermediate constants may depend on the fixed tensor degree.
Their effect is \(C_{\varepsilon,l}\sqrt T/T\to0\), so later limits
must shrink the punctured radius **after** fixing degree and discarded
mass. The active book, historical source manifests and 42 statuses are
unchanged. No finite experiment or separate verifier result is claimed.
