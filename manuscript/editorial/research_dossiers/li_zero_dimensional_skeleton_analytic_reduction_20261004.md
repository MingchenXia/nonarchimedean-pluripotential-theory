# Ordinary chart estimates when the essential skeleton has dimension zero

Date: 4 October 2026. This conditional book-external derivation fills the
\(m=0\) analytic boundary left explicit by the preceding \(m\geq1\)
dyadic proof. It uses fixed ordinary cores, not logarithmic annuli,
and residue-function Gram matrices. No independent verifier, principal
general CY theorem, new finite experiment or problem-status promotion
is claimed.

## Signature and the volume concentration

Retain the smooth connected projective CY family of dimension
\(n\geq1\), supplied regular **reduced** SNC projective model,
projective germ/cohomological comparison, meromorphic polarization and
canonical form, and positive rational reference presentation of the
earlier dossiers. Let \(T=-\log|t|\geq1\),
\(\theta_t=i\Theta_h|_{X_t}\), and let the normalized smooth norm
potential \(\varphi_t\) have
\(\theta_t+2dd^c\varphi_t>0\), \(\sup\varphi_t=0\),
\(|\varphi_t|\leq C T\). The uniform Skoda and parameter continuity
inputs are those just checked in
`li_canonical_skoda_and_parameter_inputs_20261004.md`.

Assume the essential skeleton has dimension zero. After the canonical
scalar shift, its components have discrepancy zero and the remaining
components have positive discrepancy. The shifted raw volume
\(\nu'_t\) has total mass tending to a positive constant, by the
published BJ volume asymptotic. Its probability normalization is
\(\mu_t\). Local convergence on the complex model gives finite
residual volumes on the relative interiors of the essential components.
The weighted central skeleton limit is a sum of point masses.

Choose compact subsets of these component interiors capturing all
but \(\eta\) of the residual probability mass. As in the previous
cutoff argument, take finitely many relatively compact adapted charts
with ordinary cores \(C_a\Subset P_a\), and cutoffs whose sum is at
most one and equals one on the compact sets. Local complex convergence
of their integrals implies, after shrinking the disc,

\[
 \mu_t\left(\bigcup_{a=1}^{N}C_{a,t}\right)\geq1-\eta.
                                                               \tag{1}
\]

Here \(N\) is fixed once the degree/tolerance/chart choices are fixed,
independent of \(t\). Each chart meets just one central component,
so reducedness gives coordinates

\[
                 t=z_0,\qquad w\in P_a\subset\mathbb C^n.
                                                               \tag{2}
\]

We identify \(C_{a,t},P_{a,t}\) with fixed ordinary polydiscs in
\(w\). On their compact closures the shifted raw and probability
volumes are uniformly comparable to ordinary Lebesgue volume \(dV\).
There is no factor \(T^{-m}\) to insert. There are no independent
logarithmic or angular coordinates in (2).

One must not delete the skeleton vertices as null sets. They have
positive atomic mass. Equalities of section valuations at a vertex
are handled by their residue coefficients below. There is no proper
wall cutting the relative interior of a point. The earlier
positive-dimensional face/wall discard is not used in (1).

## Finite ordinary parents give the potential comparison

The global comparison form \(\beta_t\) of the positive-model proof
dominates the ordinary metric on these relatively compact charts.
Its global energy estimate gives

\[
 \int_{P_a}|\nabla_w\varphi_t|^2dV\leq C_a T.            \tag{3}
\]

To match the norm convention, its integration-by-parts argument can
be applied to \(2\varphi_t\), which is \(\theta_t\)-psh; dividing
the gradient energy by four gives (3). The \(O(T)\) oscillation
bound scales by two. The comparison with \(\beta_t^{n-1}\) uses
ordinary positivity on the fixed chart, including \(n=1\).

Let \(b_a(t)\) be the ordinary-volume average of \(\varphi_t\)
on \(P_a\). Ordinary Poincaré gives

\[
           \int_{P_a}|\varphi_t-b_a(t)|^2dV\leq C_a T.
                                                               \tag{4}
\]

There is no need to discard bad dyadic parents or count \(T^m\)
annuli: the number of ordinary parents is finite and each is controlled
directly by the total energy.

On the fixed chart choose a uniformly bounded smooth potential
\(\rho_{a,t}\) for \(\theta_t/2\). Then
\(\varphi_t+\rho_{a,t}\) is psh in \(w\).
Every point \(y\in C_a\) admits a complex polydisc of one fixed
positive radius inside \(P_a\). Submean and Cauchy–Schwarz, using
(4) and the fixed polydisc volume, give

\[
            \varphi_t(y)\leq b_a(t)+C_a\sqrt T
                         \quad(y\in C_a).               \tag{5}
\]

The bounded reference-potential error is absorbed since \(T\geq1\).
This estimates every point of the full core on which the section
integral will be taken.

Assign each point in the union in (1) to its first core. This is a
measurable partition. Since \(\mu_t\leq C_a dV\) there, (4) and
Chebyshev imply that removing points of the assigned core with
\(|\varphi_t-b_a(t)|>M\sqrt T\) costs at most \(C/M^2\) in total,
where \(C\) includes the fixed finite chart collection. Choose
\(M=M_\eta\) to make this at most \(\eta\), and call the remaining
partitioned union \(U_t\). Then

\[
 \mu_t(U_t)\geq1-2\eta,\qquad
 \varphi_t(y)\leq\varphi_t(\zeta)+C_\eta\sqrt T
 \quad(\zeta\in U_{a,t},\ y\in C_a).                   \tag{6}
\]

This is the same pointwise generic comparison needed by the weighted
Hilbert bound. No comparison between distinct component averages
\(b_a(t)\) is required.

## A vertex basis and its independent residue functions

Fix a sufficiently large allowed degree \(l\), with whole section
space of dimension \(d_l\). In a local model frame \(e_l\), the
faithful completed Laurent expansion has coefficients in holomorphic
functions on a common connected transverse polydisc. In (2) its
valuation is the lowest integer power of \(t\), on the faithful
finite-dimensional inclusion
\(V_K\subset\mathcal O(W)[[t]][t^{-1}]\).
At this single point the cancellation argument takes the following
form; no slope or positive-dimensional wall estimate is needed.
Independence of the aligned leading functions is sufficient for
orthogonality: at a common minimum order, leading coefficients of the
field scalars are complex numbers, so they cannot cancel those functions.

Start with an orthogonal collection \(v_1,\ldots,v_r\), and a vector
\(v\) outside its span. Scale their leading orders to the same order
by integer powers of \(t\). If the leading function of the current
residual is independent of the old leading functions, append it.
Otherwise subtract a constant linear combination of the aligned
\(v_i\); the residual stays outside their span and its valuation
strictly increases. If this continued infinitely, the integer residual
valuations would tend to infinity. Each coefficient used for \(v_i\)
has order equal to the current residual valuation minus
\(\gamma(v_i)\), hence tending to infinity. The accumulated
coefficients converge in the complete field \(K\). The ultrametric
inequality shows that the limiting residual has valuation infinity,
so it is zero by faithfulness. This contradicts the choice outside
the old span. Thus cancellation stops; induction gives a full
orthogonal basis. This explicitly supplies the point case of the
method in `li_finite_chambers_and_formal_bases_20261004.md`, whose
earlier displayed signature retained \(m\geq1\).

If its leading orders are \(\gamma_i\in\mathbb Z\), orthogonality
forces the leading coefficient functions \(f_i(w)\) to be linearly
independent over \(\mathbb C\): a relation
\(\sum_i c_i f_i=0\) would make
\(\sum_i c_i t^{-\gamma_i}s_i\) have order strictly positive,
although its nonzero terms have order zero. This contradicts
orthogonality. All exponent classes modulo the single-coordinate
\(\mathbb Z\) lattice are treated together, not discarded.

The fixed-degree formal-to-convergent truncation preserves these leading
coefficients and the full basis: truncate the formal change-of-basis
matrix beyond an order exceeding every leading order minus the lowest
reference-basis order. Every column error then has strictly larger
order. Independence of the unchanged residue functions makes the
truncated family K-linearly independent: at any common minimum order
a nonzero relation would give a constant relation among those functions.
Its finite meromorphic determinant is therefore nonzero, giving an
invertible meromorphic matrix. The geometric section-module comparison
supplies
its actual fibre basis on one sufficiently small punctured disc.
There are finitely many bases, one for each of the selected charts;
their rows in the reference basis form one fixed meromorphic matrix.

Convergence on a common larger chart gives, on \(C_a\),

\[
 s_i(t,w)=t^{\gamma_i}\bigl(f_i(w)+t R_i(t,w)\bigr)e_l,
                    \sup_i\|R_i\|_{C^0(C_a)}\leq C_l.   \tag{7}
\]

This is a uniform absolute remainder after removing the leading
monomial. It does not divide by \(f_i\), which may vanish.
A meromorphic model-reference identification gives

\[
 c_l^{-1}|t|^{\delta_l}\leq|e_l|_{h^l}
                          \leq c_l|t|^{\delta_l}         \tag{8}
\]

on the fixed core, with real rational \(\delta_l\) permitted for
a root model metric. The smooth unit has uniform bounds. The section
orders in (7) remain integral; the reference factor in (8) is kept.

## The Gram bound replaces angular Fourier integration

The matrix
\(G_{ij}=\int_{C_a}f_i(w)\overline{f_j(w)}dV\)
is positive definite. A zero integral for a linear combination would
make that holomorphic combination zero on the open core, and then on
the connected coefficient chart, contradicting independence.
For any complex tuple \(a_i\), at the fixed nonzero parameter (7)–(8)
and the raw-volume comparison give for the leading sum

\[
 \int_{C_a}\left|\sum_i a_it^{\gamma_i}f_i e_l\right|_{h^l}^2d\nu'_t
       \geq c_l |t|^{2\delta_l}
                         \sum_i|a_i|^2|t|^{2\gamma_i}.   \tag{9}
\]

The remainder has squared L2 norm at most
\(C_l|t|^2|t|^{2\delta_l}\sum_i|a_i|^2|t|^{2\gamma_i}\),
by finite-dimensional Cauchy–Schwarz. The L2 triangle inequality
absorbs it uniformly for all tuples when \(t\) is sufficiently small.
At any \(\zeta\in C_a\), (7) also bounds
\(|s_i(\zeta)|_{h^l}\leq C_l|t|^{\gamma_i+\delta_l}\).
Thus the full sum satisfies

\[
 \int_{C_a}\left|\sum_i a_i s_i\right|_{h^l}^2d\nu'_t
                   \geq c'_l\sum_i|a_i s_i(\zeta)|_{h^l}^2.
                                                               \tag{10}
\]

No angular orthogonality, logarithmic radial integration or lower
bound on an individual \(f_i(\zeta)\) is invoked.

## The weighted lower estimate and the later composition

For \(\zeta\in U_{a,t}\), apply (6) on the entire core in (10).
With the same shifted raw measure as the Bergman estimate, this gives

\[
 \frac1{2l}\log\int_{X_t}\left|\sum_i a_is_i\right|_{h^l}^2
                              e^{-2l\varphi_t}d\nu'_t
 \geq\max_i\left\{\frac1l\log|a_i s_i(\zeta)|_{h^l}
                                     -\varphi_t(\zeta)\right\}
                             -C_{l,\eta}\sqrt T.         \tag{11}
\]

The fixed logarithmic Gram constant is absorbed into the last term.
Zero coefficients use \(\log0=-\infty\); the all-zero tuple is
trivial in that extended convention. Replacing the initial tolerance
by half the desired final one in (1),(6) supplies any required
almost-full generic mass.

Consequently the finite-matrix replacement and uniform FS composition
have the same inputs as in positive essential dimension: the whole
fixed-degree section bases, weighted lower estimate with \(o(T)\)
error, global Bergman upper estimate, uniform Skoda and punctured
continuity. The prior full hybrid/MA passage requires no positive
essential dimension. It therefore applies conditionally here too.
The finite-cover trace/quotient reduction can descend this continuous
limit from a supplied reduced model; its normalized skeletal measures
have \(q^m=1\) when \(m=0\).

## Boundaries and admission limits

This argument is for zero essential dimension with positive total
probability mass and \(n\geq1\). It does not assume a globally smooth
central fibre: compact cores lie in interiors of the essential
components, and residue integrability controls the discarded regions.
The reduced-model restriction is explicit. Repeated components require
the supplied reduced cover and descent; the local disconnected-fibre
Poincaré obstruction is not ignored. A zero-dimensional variety would
need only scalar sections and has no gradient argument, but is not
included in this signature by implication.

The projective/model/cohomological, classical analytic, Skoda and
hybrid/NA source imports remain explicit. All constants and radii may
depend on the fixed degree and tolerance. No new primary source,
independent verdict or general semistable/model construction is supplied
here. The previous dyadic signature remains historically \(m\geq1\);
this separate derivation supplies its \(m=0\) boundary without
rewriting those earlier records. Book admission and problem-status
changes still require exact-current independent verification.
