# Direct GF operations and homogeneous regularization

Date: 5 October 2026. Baseline: `94de80657a9c62365509add805aa3c7b7858a4d4`.
Status: reconstruction of identified published conclusions outside active
TeX, pending independent admission. This note does not repair arbitrary
unbounded decreasing psh closure or critical Siu division. It follows the
[abstract diagonal diagnostic](bj22_abstract_diagonal_lemma_diagnostic_20261005.md)
and the [bounded/nef reconstruction](bounded_and_nef_closure_followup_20261005.md).
No priority, production-verifier receipt or solved problem is claimed.

Let `X` be an integral projective variety over an algebraically closed
trivially valued field. No smoothness or characteristic restriction is
used below. Use BJ22 Definition 4.1: a generically finite psh function
is the pointwise decreasing limit of GF Fubini--Study functions whose
rational line-bundle classes converge to the stated real numerical class.

## Rational weights with the same pole set

Take a defining net `f_i in H_R^gf(L_i)`, decreasing to `f`, with
`c_1(L_i)->theta`. For each stage choose a presentation

\[
 f_i=m_i^{-1}\max_j\{\log|s_{i,j}|+\lambda_{i,j}\}.
\]

For a positive rational number `epsilon`, replace each real weight by a
rational weight satisfying

\[
 \lambda_{i,j}\leq\lambda^\epsilon_{i,j}
       <\lambda_{i,j}+m_i\varepsilon/4.
\]

Denote the resulting rational-weight function by `q_(i,epsilon)` and set

\[
 h_{i,\varepsilon}=q_{i,\varepsilon}+\varepsilon
       \in\mathcal H^{\rm gf}_{\mathbf Q}(L_i).
\]

Both changes preserve **exactly** the common zero set of the section
system. Everywhere on `X^an`, with finite constants added safely to
minus infinity, they give

\[
 f_i\leq q_{i,\varepsilon}\leq f_i+\varepsilon/4,
 \qquad f_i+\varepsilon\leq h_{i,\varepsilon}
                \leq f_i+5\varepsilon/4.
\]

These additive inequalities include proper-support poles. There is no
claim of a positive difference at a point where both functions are
minus infinity.

Give the pairs `(i,epsilon)` the preorder

\[
 (i,\varepsilon)\succeq(i',\varepsilon')
 \quad\Longleftrightarrow\quad
 i\succeq i',\quad\varepsilon\leq\varepsilon',
 \quad h_{i,\varepsilon}\leq h_{i',\varepsilon'}
                 \text{ on }X^{\rm an}.
\]

This set is directed. Given two pairs, choose an original index `i`
above their indices and a positive rational `epsilon` with
`5 epsilon/4<=min(epsilon_1,epsilon_2)`. For each reference pair,

\[
 h_{i,\varepsilon}\leq f_i+5\varepsilon/4
 \leq f_{i_a}+\varepsilon_a\leq h_{i_a,\varepsilon_a}.
\]

At a reference pole, the middle inequality holds because the **original
stage net** is already decreasing: `f_i` is also minus infinity there.
The rounded presentation has precisely that pole set. Thus directedness
uses exact stage order and preservation of poles, rather than compactness
or a false strict comparison against an inner limit.

The projected original indices tend cofinally through the original net,
and the rational errors tend to zero. The displayed additive estimates
give `h_(i,epsilon) decreasing to f` pointwise. At a minus-infinity value,
use any finite real upper threshold, then choose the original stage below
that threshold with a margin for `5 epsilon/4`; every later pair retains
the bound. The bundle of a pair is `L_i`, so its numerical class still
tends to `theta`. This proves the rational-weight assertion directly
from the definition, without unrestricted Lemma 4.6 or Theorem 4.5.

The class gaps in BJ22 Theorem 4.15(i) can also be imposed directly.
Fix an ample rational line bundle `A`. Choose positive rational
`delta_i->0` such that `c_1(L_i)+delta_i[A]-theta` is ample. Replace
`L_i` by `L_i+delta_i A`, presenting the **same function** by multiplying
its section system with a globally generated presentation of the zero
function in `delta_i A`. The numerical gap is ample, and rational weights,
pointwise stage order and the limiting class are preserved. Here an ample
rational line bundle is semiample; a sufficiently divisible globally
generated power supplies the zero presentation. No psh class-closedness
is used in this change of presentations.

## Ordinary multiplication by a real positive number

The rational GF tensor-power rule also gives real positive multiplication
directly, without applying psh closure to the intermediate functions.
Fix `t>0`. Restrict a defining GF net to a tail above one index `i_0`;
choose a finite constant `C>=sup f_(i_0)`. Then `f_i-C<=0` on that tail.
Choose positive rationals `t_n` increasing to `t`. On the product order,

\[
 k_{n,i}=t_n(f_i-C)+tC
       \in\mathcal H^{\rm gf}_{\mathbf R}(t_n L_i)
\]

is decreasing in both indices. Increasing `n` decreases the nonpositive
factor; increasing `i` decreases `f_i-C`. Its pointwise limit is `t f`,
including at minus-infinity values, and its numerical classes converge
to `t theta`. Generic finiteness is preserved because the generic trivial
valuation has finite value. Apply the construction to `1/t` for the
reverse inclusion. Thus the real-scalar part of BJ22 Theorem 4.7(i) can
be reconstructed from the definition and rational section powers.
It is ordinary multiplication of values; the radial scaling action is
a different operation and already preserves each presentation's class
by changing its weights.

## A fixed ample buffer and linear-growth values

Choose an ample **honest** line bundle `B` with `[B]-theta` ample. On a
tail of any defining GF net, `B-L_i` is ample as a rational line bundle.
Its zero GF presentation embeds the **unchanged** stage function in
`H_R^gf(B)`. The rational-weight construction above therefore gives a
decreasing net `h_gamma in H_Q^gf(B)` with limit `f`. This is an
approximation in a larger fixed class; it makes no limiting-class claim
back in `theta`.

Because `B` is ample, its zero presentation is base-point free. For each
positive integer `M`,

\[
 p_{\gamma,M}=\max\{h_\gamma,-M\}\in\mathcal H_{\mathbf Q}(B)
                        \subset\operatorname{PL}^{+}(X).
\]

On the product order of `gamma` and `M`, these finite-valued functions
are decreasing and tend pointwise to `f`. This net is constructed from
the already ordered GF stages; no nested psh closure is invoked.

BJ22 Definition 1.26 defines `T_B(v)` as the supremum of `m^{-1}v(s)`
over nonzero sections of `mB` and positive integers `m`. Each GF stage
in `B` satisfies

\[
 h_\gamma(v)\geq h_\gamma(v_{\rm triv})-T_B(v).
\]

Indeed select a section with maximal weight in its presentation; its
valuation is at most `m T_B(v)`. Passing to the pointwise limit gives
`f(v)>=f(v_triv)-T_B(v)`. Thus `f` is finite on valuations of linear
growth, since `f(v_triv)` is finite. Divisorial valuations have linear
growth by BJ22 Proposition 1.28. This reconstructs the finiteness input
of Corollary 4.17 without general Theorem 4.15 or 4.5.

## Rees-valuation comparison without psh diagonal closure

Fix a rational PL function `eta`. By the section-2 flag-ideal algebra it
can be written as `eta=r(phi_a-rho)` with `r>0` rational, a flag ideal
`a`, and `rho in PL^+(X)`. Its Rees-valuation set `Sigma_a` is finite
and depends only on this presentation of `eta`. BJ22 Lemma 2.13 and
the closure of `PL^+` under sums and positive rational multiplication give

\[
 p(v)-\eta(v)\leq
       \max_{w\in\Sigma_{\mathfrak a}}\{p(w)-\eta(w)\}
 \qquad(p\in\operatorname{PL}^{+}(X),\ v\in X^{\rm an}).
\]

Apply this to the actual decreasing finite-valued net `p_(gamma,M)`
above. Finite maxima commute with decreasing limits of directed nets:
for a finite set of points, choose a common later index for their finitely
many error bounds; minus-infinity limits are handled by finite real
thresholds. Consequently, for every `f in PSH(theta)` and every `v`,

\[
 f(v)-\eta(v)\leq
       \max_{w\in\Sigma_{\mathfrak a}}\{f(w)-\eta(w)\}.
\]

Subtraction is safe because `eta` is finite valued. Values of `f` on the
finite set are finite by the preceding growth bound. Evaluation at a point
where the right-hand maximum is achieved also gives the sup equality of
BJ22 Lemma 4.26. No compactness of a psh family or general numerical
closedness has entered the argument.

This recovers the comparison implication in Theorem 4.22. First suppose
`f<=u` on divisorial valuations and `u` is continuous. Choose rational PL
functions `eta_n` with uniform error `delta_n->0` from `u`, using Theorem
2.2. On the associated finite Rees set, `f-eta_n<=delta_n`; the displayed
inequality then gives `f<=eta_n+delta_n<=u+2 delta_n` everywhere.
Passing to the limit gives `f<=u` on all points. For any extended-real
usc `u`, use that an usc function on a compact Hausdorff space is the
pointwise infimum of its finite-valued continuous majorants. Each such
majorant is at least `f` on divisorial points, and hence on all points
by the continuous case. Taking their infimum gives `f<=u`. This includes
minus-infinity values without subtraction of two infinities. The converse
implication is immediate. The uniqueness statement of Corollary 4.23
follows by applying comparison in both directions.

## Homogenization of a decreasing GF net

For a function `u` define its homogenization by

\[
 \widehat u(v)=\inf_{a>0}a\,u(a^{-1}v).
\]

For any decreasing net `(u_i)`, monotonicity and interchange of two
infima give, pointwise,

\[
 \widehat{\inf_i u_i}
 =\inf_{a>0}\inf_i a\,u_i(a^{-1}v)
 =\inf_i\widehat u_i.
\]

This identity is purely about ordered extended-real functions. It does
not invoke a psh closure theorem.

BJ22 Theorem 6.15 is a **single-presentation** section calculation: for
`u in H_Q^gf(L)` with `sup u>=0`, its homogenization belongs to
`H_hom(L)`. Its proof applies the finite rational polyhedral formula of
Lemma 6.20 to the rational weights and clears the denominators of the
resulting nonnegative section exponents. This calculation does not use
Lemma 4.6. At proper-support values, a zero exponent means the section
factor is omitted. The finite-real formula extends to minus-infinity
coordinates by replacing each such coordinate by `-R`, letting `R` tend
to infinity, and interchanging `inf_R` with the defining `inf_a`. Finite
maxima and sums with nonnegative coefficients have the same decreasing
limits, with zero coefficients omitted; no `0*(-infinity)` is evaluated.

Now let `f in PSH(theta)` with `sup f>=0`. Apply the rational-weight
construction to its defining net. Each rational stage `h_gamma` is at
least `f`, so `sup h_gamma>=0`. Its homogenization is a homogeneous GF
function of the same rational line bundle. Homogenization preserves the
stage order, and the infimum identity gives

\[
 \widehat h_\gamma\searrow\widehat f,
 \qquad c_1(L_\gamma)\longrightarrow\theta.
\]

On an integral variety, the generic trivial valuation is fixed by radial
scaling. The maximum principle gives `f(v_triv)=sup f>=0`, and thus
`widehat f(v_triv)=inf_(a>0) a f(v_triv)=0`. The limit is generically
finite, so **Definition 4.1 itself** places `widehat f` in
`PSH_hom(theta)`. This reconstructs Corollary 6.17(i)--(ii) without the
unrestricted abstract diagonal lemma. In particular a homogeneous psh
function has a decreasing homogeneous GF approximation in converging
classes. The fixed-ample-bundle refinement 6.17(iii) is not independently
established by this note.

## Strict division when the residual class is nef

The preceding reconstructions and the separate bounded/nef note give a
restricted independent version of the book's strict division proof. Let
`X` additionally be normal, let `D` be a nonzero effective rational
Cartier divisor, and suppose

\[
 f\in\operatorname{PSH}_{\rm hom}(X,\alpha),\qquad
 f\leq t_0\ell_D,\quad t_0>1,\qquad
 \theta=\alpha-[D]\ \text{nef}.
\]

Use the reconstructed homogeneous GF approximation `f_i` in rational
bundles `L_i`, with classes tending to `alpha`. On the compact set
`K={ell_D=-1}`, the limit is at most `-t_0<-1`. The open sets
`{f_i<-1}` increase and cover `K`; compactness gives a stage, and then
a tail, with `f_i<-1` there. Homogeneity gives `f_i<=ell_D` on
divisorial rays with positive value of `D`; homogeneous normalization
handles rays with value zero. The independently reconstructed divisorial
comparison extends this inequality to all analytic points.

For each such GF stage, normal section division gives

\[
 f_i=\ell_D+r_i,\qquad
 r_i\in\mathcal H_{\rm hom}(L_i-D).
\]

This is the fixed-divisor algebraic calculation in Chapter 35: after
clearing denominators, each stage section has divisor at least `mD`,
and dividing by its canonical section gives a regular section of
`m(L_i-D)` by normality. The divisor coefficient is fixed throughout.
Cancellation on divisorial valuations gives `r_i` decreasing there;
divisorial comparison gives decreasing order on the whole space. Their
generic trivial values are zero, so the pointwise limit `r` is
generically finite and homogeneous. Their classes tend to the **nef**
target `theta`. The bounded/nef reconstruction supplies
`r in PSH_hom(theta)` without the unrestricted abstract lemma.

The stage identities pass to the limit: off the proper-support pole set
of `D`, subtract the finite value of `ell_D`; on that pole set both the
stage identities and their limiting sums have value minus infinity.
Thus `f=ell_D+r` on all points. Uniqueness follows from finite
divisorial cancellation and determination. If `D=0`, take `r=f`
directly. This argument keeps the strict coefficient margin and the
nef residual hypothesis explicit. It does not establish the critical
inequality with coefficient one, or strict division with an arbitrary
non-nef pseudoeffective residual class.

## Boundary of the reconstruction

The initial net in these arguments already consists of genuine GF stage
functions. It is not a decreasing net of arbitrary psh functions with
separate inner approximations. Therefore this argument does not flatten
the general nested situation in Theorem 4.5. It also does not assert
closedness of the numerical classes of a fixed unbounded function in a
non-nef target class. Rationalizing weights preserves the poles of each
existing stage; it does not manufacture the pole compatibility missing
between unrelated inner nets.

Homogeneous regularization is one input to strict divisor division.
Preserving this input does not remove the general varying-class closure
step of that strict proof. The restricted reconstruction above covers
only its nef residual regime and does not fix the critical endpoint in
Theorem 6.21. All
425 active TeX inputs, book/catalogue PDFs, historical receipts and the
42 problem statuses remain unchanged. This is a research proof
reconstruction awaiting independent admission, not an integrated new
result.

## Targeted source reading

Fresh published BJ22 text checks cover 800–855 (generic trivial valuations
and maximum principle), 1181–1281 (vertical ideal criterion and growth
bound), 1310–1385 (flag-ideal operations, PL density and its proof),
1435–1522 (complete Rees-valuation criterion and proof), 1770–1871
(FS/PL bridge and the adjoining interpolation statements), 1610–1705
(GF section operations), 2970–3109 (disputed diagonal statement and
separate section operations), 3160–3375 (regularization, comparison and
their printed proofs), and 4130–4310 (homogenization and its complete
proof). The scope is targeted, not a fresh full reading of the paper.
Actual physical pages 88–91 were additionally inspected for the
homogenization formula, rational section exponents and Corollary 6.17.
Earlier same-session page checks are identified in the preceding closure
and downstream manifests. These records provide source comparison,
not an independent production-model verification of this reconstruction.
The fixed-coefficient section-division and strict proof at Chapter 35
source lines 2476–2667 were also checked; the earlier actual book views
2250–2252 are reused as such, rather than claimed as new views here.
