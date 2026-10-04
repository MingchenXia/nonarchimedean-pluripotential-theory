# Conditional FS approximation and the full hybrid limit

Date: 4 October 2026. This book-external derivation completes the
topological and MA passage after the conditional uniform FS estimates.
It records the necessary source imports and does not certify the
geometric inputs of a general Calabi–Yau degeneration. No result or
open-problem status is promoted and no external verifier is claimed.

## Signature and fixed imports

Let a smooth projective meromorphic degeneration of complex dimension
\(n\geq1\), with connected complex fibres and geometrically integral
generic fibre, carry an ample meromorphic line bundle \(L\). Work near zero
on a closed disc, with compact Hausdorff hybrid space \(Y\), proper
projection \(\pi:Y\to\overline D\), and NA central fibre \(Y_0\).
Let \(h\) be a smooth model reference, with central model metric \(h_0\).
Use the valuation normalization \(\operatorname{ord}(t)=1\) and the
scaling \(\epsilon_t=1/T\), \(T=-\log|t|\). The book's alternative
\(\epsilon_{r,t}=(-\log r)/T\) rescales all central potentials by
the same fixed positive constant; it is not silently identified with
\(1/T\).

The scalar potential \(u_t=\varphi_t/T\) is relative to \(h\).
The corresponding complex metric has curvature
\(\theta_t+2dd^c\varphi_t\), where \(dd^c=i\partial\bar\partial\).
Normalized MA is unchanged on dividing this curvature and its top
intersection volume by \((2T)^n\). Write \(\operatorname{MA}_{h_0}(v)\)
for the probability MA of the central metric with relative potential
\(v\). The reference itself need not be declared NA semipositive:
semipositivity below concerns the resulting FS metrics and their limits.

Assume the preceding composition proof supplies, for all sufficiently
large integers \(l\), a finite globally generating meromorphic family
\(S_{l,a}\), bounded real coefficient vectors \(c_l(t)\), and

\[
 F_l(y,c)=\max_a\left\{\frac1{lT}\log|S_{l,a}(y)|_{h^l}-c_a\right\}
 \quad(y\in Y_t,\ t\ne0),\qquad
 F_l(y,c)=\max_a\left\{\frac1l\log\|S_{l,a}(y)\|_{h_0^l}-c_a\right\}
 \quad(y\in Y_0),                                            \tag{1}
\]

with

\[
 \|u_t-F_l(\cdot,c_l(t))\|_{C^0(Y_t)}\leq\varepsilon_l,
 \qquad 0<|t|<r_l,\qquad \varepsilon_l=C_*/l\longrightarrow0.  \tag{2}
\]

For each fixed \(l\), all \(c_l(t)\) belong to one compact finite
dimensional box \(Q_l\) after reducing \(r_l\). No regularity of
\(c_l(t)\) in \(t\) is assumed. Suppose \(u\) itself is continuous on
the punctured total family and its metrics are continuous fibrewise psh.
This punctured-family continuity is an additional hypothesis; fibrewise
smoothness alone would not imply it. Suppose also \(\sup_{Y_t}u_t=0\).

The following are separately imported for this geometric category.

1. Projective hybrid properness and Hausdorffness; cofinal common SNC
   models; the topology characterized by all hybrid model log maps;
   their compatibility under domination and their local SNC description.
2. Hybrid continuity of real-weight tropical FS metrics, and hybrid
   continuity of the model reference. Rational FS metrics are dense
   in continuous psh metrics on \(L_0\); the latter class is closed
   under uniform limits.
3. Complex and NA MA continuity on continuous psh metrics, the CLN
   inequality, weak hybrid convergence for smooth hybrid model metrics,
   and density of model tests in the central continuous functions.
4. The actual measures \(\mu_t=\operatorname{MA}(\varphi_t)\) converge
   weakly in \(Y\) to a given probability \(\mu_0\). For the intended
   CY application this is the independent volume-measure convergence
   input, not a conclusion from (2). NA MA determines continuous psh
   metrics up to an additive constant.

Boucksom, arXiv:2510.10239v2, Proposition 3.4, Definition 3.7,
Example 3.10, Sections 4.1–4.2 and 4.7, Propositions 5.4–5.5 and 5.10,
(5.2)–(5.3), and Sections 7.1–7.3 anchor these imports at the checked
version. Its analytic and NA antecedents remain imports, not newly
independent proofs. The CY volume input is not supplied merely by
reading that paper's Theorem 7.11.

## Every small fibre meets every central neighborhood

Here is the density step needed for arbitrary scalar sequences. Ordinary
density of the punctured part alone would not be enough.

Fix \(x\in Y_0\) and a neighborhood \(N\) of \(x\). The log-map
description of the topology gives finitely many SNC model constraints
whose intersection is contained in \(N\). Choose one common higher SNC
model \(\mathcal X\). Compatibility (5.2) expresses each earlier log
map as an affine map of \(\operatorname{Log}_{\mathcal X}\), with
an \(O(1/T)\) error on the small complex fibres and exact agreement
at zero. Thus it suffices to approximate
\(w=\operatorname{Log}_{\mathcal X}(x)\in\Delta_{\mathcal X}\).

Choose the minimal face containing \(w\). Its coordinates satisfy
\(w_i>0\) for \(i\in J\) and \(\sum_{i\in J}b_iw_i=1\).
Pick a point of the corresponding stratum away from all other central
components. In a relatively compact adapted chart,
\(t=\prod_{i\in J}z_i^{b_i}\). Fix the transverse coordinates at
the chart center and choose, for every sufficiently small nonzero \(t\),

\[
 |z_i|=|t|^{w_i},\qquad
 \prod_{i\in J}z_i^{b_i}=t.                               \tag{3}
\]

Phases satisfying the second equation exist; for example choose all
but one phase and an appropriate \(b_i\)-th root for the last one.
This selects points, not a globally holomorphic branch. Because every
\(w_i\) is positive, all these points eventually lie in the chart.
Their local log vector is exactly \(w\); the global log vector is
\(w+O(1/T)\) by (5.3). Components not in \(J\) contribute only
\(O(1/T)\), since their canonical sections are nonzero at this chart
center. Hence the chosen points lie in \(N\) for every sufficiently
small nonzero \(t\).

This includes a vertex, where \(J\) has one element and a root of
\(t\) suffices; no top-dimensional-face assumption is used. In
particular, for any scalar sequence \(t_j\to0\) and any tail, the
closure in \(Y\) of \(\bigcup_{j\geq j_0}Y_{t_j}\) contains all
of \(Y_0\). Lemma 5.12, which has the extra condition
\(\dim\Delta_x=n\), is not invoked to assert this stronger statement.

## Joint continuity of each fixed FS family

For fixed \(c\), (1) is the relative potential of a real-weight
tropical FS metric; the degree-\(l\) metric weights are \(-lc_a\).
Example 3.10 and model-reference continuity therefore give a continuous
function \(F_l(\cdot,c)\) on a sufficiently small closed hybrid disc.
The max is finite and continuous because the sections have no common
zero. The elementary estimate

\[
 |F_l(y,c)-F_l(y,c')|\leq\|c-c'\|_\infty                 \tag{4}
\]

holds on both complex and central fibres, even though individual
section logs can be \(-\infty\). It proves joint continuity in
\((y,c)\): first fix \(c\) and use continuity in \(y\), then use
(4) to handle the coefficient variation. No separate continuity
principle on arbitrary products is being assumed.

## Diagonal coefficient limits and a continuous central metric

Given any scalar sequence \(t_j\to0\), finite dimensional compactness
and a diagonal extraction yield a subsequence, still written \(t_j\),
on which \(c_l(t_j)\to c_l^*\) for every \(l\). Define
\(v_{l,0}=F_l(\cdot,c_l^*)|_{Y_0}\).
On sufficiently late fibres (2) implies

\[
 |F_l(\cdot,c_l(t_j))-F_m(\cdot,c_m(t_j))|
      \leq\varepsilon_l+\varepsilon_m.                    \tag{5}
\]

By (4), one may replace the moving coefficients in (5) by their limits
with an error tending uniformly to zero. The tail-density step and
continuity of the fixed functions then give the same bound on \(Y_0\).
Thus \(v_{l,0}\) is uniformly Cauchy. Its limit \(v_0\) is continuous,
the metric with relative potential \(v_0\) is continuous psh, and

\[
 \|v_{l,0}-v_0\|_{C^0(Y_0)}\leq\varepsilon_l.            \tag{6}
\]

For the psh conclusion, real coefficients cause no model ambiguity:
approximate them at each fixed degree by rational vectors using (4).
The resulting rational FS metrics approximate the real-weight metric,
and its uniform limit is in \(\operatorname{CPSH}(L_0)\).

Let \(B=\{0\}\cup\{t_j:j\geq1\}\). On the compact subspace
\(Y_B=\pi^{-1}(B)\), extend \(u\) by \(v_0\) on \(Y_0\).
This extension is continuous at central points: given an error tolerance,
choose \(l\) large in (2),(6), then take \(j\) large so the coefficient
error in (4) is small, and use the fixed continuous function
\(F_l(\cdot,c_l^*)\) as a comparison in a neighborhood of the point.
Continuity on the punctured part follows from the explicit hypothesis.

The normalization also passes to zero without sequential compactness
of \(Y_0\). Tail density and \(u_t\leq0\) imply \(v_0\leq0\).
Choose a maximum point on each compact complex fibre. Compactness of
\(Y_B\) gives a convergent subnet of these points, lying over zero
in the limit. Central continuity gives value zero at that limit.
Consequently \(\sup_{Y_0}v_0=0\).

## MA passage on the restricted base

Theorem 7.11 is stated for a full disc family. The following records
its proof on \(Y_B\), rather than treating the restricted-base
variant as a separate quoted theorem.

Fix \(\delta>0\) and a rational FS central metric \(q_0\) within
\(\delta\) of the metric with potential \(v_0\). It extends to a
smooth hybrid FS model metric \(q_t\) on a small full disc by
Example 5.3 (clearing rational weights using tensor powers and powers
of \(t\)). Write \(q\) also for its relative scaled potential.
Compactness of \(Y_B\) and continuity of \(u-q\) imply

\[
 \limsup_{j\to\infty}\|u_{t_j}-q_{t_j}\|_{C^0(Y_{t_j})}
      \leq\|v_0-q_0\|_{C^0(Y_0)}<\delta.                 \tag{7}
\]

For clarity, (7) only needs an upper bound: if it failed, points
violating it would have a convergent subnet in \(Y_B\), with central
limit, contradicting continuity. It does not require a sequence of
central points to converge.

A central model test, after a positive fixed multiple, is the difference
of two rational FS metrics. Extend these to smooth hybrid FS metrics
\(a_t,b_t\). Its complex value is
\(T^{-1}(a_t-b_t)+O(T^{-1})\). The complex CLN inequality gives

\[
 \left|\int T^{-1}(a_{t_j}-b_{t_j})
       (\operatorname{MA}(\varphi_{t_j})-\operatorname{MA}(q_{t_j}))
       \right|\leq2n\delta                               \tag{8}
\]

eventually, interpreting \(q_{t_j}\) in the integral as the unscaled
metric. Indeed the unscaled metric difference is \(T\) times the
relative difference in (7); the test's \(T^{-1}\) cancels this
factor. The same inequality on \(Y_0\) bounds the central MA error
by \(2n\delta\). The actual source PDF prints the absolute-value
inequality in Lemma 7.2 and in the proof of Theorem 7.11; text extraction
can omit these bars. Independently, interchanging \(a,b\) supplies
the two directions of (8).

Theorem 7.8 handles the middle comparison
\(\operatorname{MA}(q_{t_j})\to\operatorname{MA}(q_0)\).
Letting \(\delta\to0\) proves convergence on model tests. For any
continuous hybrid test, approximate its restriction to \(Y_0\) by a
model test. Proper compactness bounds their difference on all late
fibres by the central approximation error plus an arbitrarily small
error, by the same subnet argument as (7). Probability mass one then
gives convergence for the original test. This explains the use of
central test density in Lemma 6.1 and Theorem 7.11 here. Hence

\[
 \mu_{t_j}\longrightarrow\operatorname{MA}_{h_0}(v_0).
                                                               \tag{9}
\]

The independent assumption \(\mu_t\to\mu_0\) identifies this measure
with \(\mu_0\). NA MA uniqueness and \(\sup v_0=0\) show that every
diagonal extraction has the same limit, denoted \(v\). This establishes
existence of the normalized limiting metric from the conditional
approximation; no separate NA existence theorem is needed in this step.

## From subsequences to the complete parameter family

Uniqueness of these scalar-subsequence limits alone is not taken as
a sequential criterion for continuity on the possibly nonmetrizable
central fibre. Instead fix \(l\), and let \(K_l\subset Q_l\) be the
cluster set of \(c_l(t)\) as \(t\to0\).
Every \(c\in K_l\) can be realized by a scalar sequence because the
parameter disc and coefficient box are metric. Diagonalize the other
degrees along it. The preceding argument then gives

\[
 \|F_l(\cdot,c)|_{Y_0}-v\|_\infty\leq\varepsilon_l
 \qquad(c\in K_l).                                      \tag{10}
\]

The cluster set is nonempty. Choose one \(c_l^{\rm ref}\in K_l\)
and let \(G_l=F_l(\cdot,c_l^{\rm ref})\), a fixed continuous hybrid
function. Joint continuity, compactness and (10) imply

\[
 \limsup_{t\to0}\sup_{Y_t}
       |F_l(\cdot,c_l(t))-G_l|\leq2\varepsilon_l.         \tag{11}
\]

Here is the compactness argument with its different roles made explicit.
If (11) failed, select bad scalar parameters tending to zero and bad
points on their fibres. Extract a convergent subsequence of the
finite dimensional coefficient vectors. The corresponding points in
\(Y\) then have a convergent subnet by compactness. Its limit lies
in \(Y_0\). Joint continuity evaluates the alleged bad difference
at that central point; (10) bounds it by \(2\varepsilon_l\), a
contradiction. No convergent subsequence of the hybrid points is asserted.

Combining (2),(11) gives

\[
 \limsup_{t\to0}\|u_t-G_l|_{Y_t}\leq3\varepsilon_l,
 \qquad \|v-G_l|_{Y_0}\leq\varepsilon_l.                 \tag{12}
\]

Extend \(u\) by \(v\) on \(Y_0\). Given a central point and a
positive tolerance, choose \(l\) with \(\varepsilon_l\) sufficiently
small, choose a punctured radius in (12), and use continuity of the
single fixed \(G_l\) in a neighborhood of the point. The triangle
inequality proves continuity of the extension there. This is a
neighborhood proof on the entire hybrid space, not an illicit
sequential criterion. Along with the stipulated punctured-family
continuity it proves hybrid continuity of the full family of metrics.
Theorem 7.11 now applies on the full disc as well.

No positivity with respect to the parameter \(t\) was assumed: only
fibrewise psh, punctured-family continuity and the explicit hybrid
imports above. No converse from weak MA convergence to C0 convergence
was used. The fixed-degree radii may vary arbitrarily with \(l\).

## Remaining application gates and boundary scope

This completes the limit passage **conditional on (1)–(2) and the
listed imports**. It does not supply faithful geometric section
expansions, convergent section-module/base change, a projective/SNC
model presentation, the raw-volume comparison, the generic-mass and
analytic-remainder estimates, or uniform Skoda constants for an
unspecified degeneration. Nor does it newly check every underlying
complex or NA analytic proof behind the source imports.

The argument is in characteristic zero for smooth projective
meromorphic degenerations. It claims no extension to a nonprojective
Kähler family, a singular or geometrically disconnected generic fibre,
mixed characteristic, zero
volume, or noncontinuous NA psh metrics. Repeated central components
are allowed in the topological step through the positive integers
\(b_i\), but this does not remove the earlier analytic derivation's
separate reduced-SNC restriction. Every topological compactness step
allows subnets; sequential compactness is used only in finite real
coefficient boxes and the scalar parameter disc.

The active 4,244-page book, its frozen artifacts, and all 42 open-problem
statuses remain unchanged. These are research derivations outside the
book, without an independent verifier verdict or a principal general
CY admission.
