# Common-constant propagation: an actual-source obstruction and exact remaining interface

Date: 1 September 2026.
Investigator: /root/p082_independent_reaudit.
Status: bounded research diagnostic, not a new accepted theorem or a
resolution of the positive-current problem. No live or frozen file is
changed. The previous nearby-wall independent audit is separate.

## 1. The question left after individual cell-to-curve access

Assume the displayed source representation R, rather than re-proving it.
Its normalized coefficient on a moment top cell is the coefficient of T
divided by the positive canonical coefficient, in the same coordinates.
The available conditional access argument anchors one prescribed cell to
all the specified shallow coordinate collars of a nearby proper residual
curve. It does not equate the ratios of two unrelated initial cells.

This note tests whether a connected ambient ordinary domain and model
subdivision make that last comparison automatic. The answer for a FIXED
moment is no: its actual maximal-variation source can have separated
pieces with an intervening bridge contracted by the moment. Vertical
model blowups do not change that source. Adding units can expose the
bridge as full-dimensional cells of a larger source skeleton, but those
are precisely cells on which the old projection drops rank.

This is an obstruction to that tempting reduction, NOT a counterexample
to equality of positive closed (0,0)-currents. In particular we construct
no nonconstant positive closed current. The existing residual identities
may be able to compare the new cells; their availability along arbitrary
chains is the missing hypothesis identified below.

## 2. A rational function with two separated source regions

Take the original complete DVR field K=C((pi)), with
ell=v(pi)>0, a=pi and r=|a|<1. Let

\[
 U_1=\mathbb A^1_K\setminus\{0,a,1,1+a\},\qquad
 f(z)=\frac{z(z-1)}{(z-a)(z-1-a)}.                 \tag{2.1}
\]

All five rational functions f,z,z-a,z-1,z-1-a that are needed below
are analytic units on W_1=U_1^{an}. This is an ordinary open subset of
the analytification of the smooth proper curve P^1_K; infinity is not
part of W_1.

Define two relatively closed analytic-disc subsets of W_1,

\[
 D_0=\{x:|z(x)|\le r\},\qquad
 D_1=\{x:|z(x)-1|\le r\}.                         \tag{2.2}
\]

They are disjoint, since otherwise the ultrametric inequality applied
to 1=z-(z-1) would give 1<=r. Their complement is the ORDINARY open set

\[
 O_1=\{|z|>r,\ |z-1|>r\}.                         \tag{2.3}
\]

For every actual analytic point in this open set, strict dominance gives

\[
 |z-a|=|z|,\qquad |z-1-a|=|z-1|,\qquad |f|=1.     \tag{2.4}
\]

This is an identity on the full ordinary source open O_1, not just
at Gauss points. Consequently the one-dimensional maximal-variation
source S_{v(f)} is disjoint from O_1.

Both D_i contain nonempty source intervals. Indeed, let gamma_0(s) be
the Gauss point of the disc centered at zero with radius
\(\mathrm e^{-s}\), and let gamma_1(s) be the analogous point centered
at one. For finite s>=0 these are actual original-K analytic points
of W_1, not the removed rigid points. Multiplicativity of the Gauss
norm gives, for s>=0,

\[
 v(f)(\gamma_0(s))=v(f)(\gamma_1(s))
                      =\max(s-\ell,0).           \tag{2.5}
\]

For s>ell this is nonconstant with slope one on both intervals, so each
is contained in the maximal-variation source. The two relatively closed
sets S_{v(f)} intersect D_0 and S_{v(f)} intersect D_1 form a disjoint
nonempty cover of S_{v(f)}, hence a clopen separation.

There is nonetheless an explicit path INSIDE W_1 joining the two source
intervals. Run gamma_0 from some S>ell down to s=0 and then gamma_1 from
s=0 to S. The two central endpoints agree:
gamma_0(0)=gamma_1(0), the Gauss point of the unit disc. Gauss norms on
discs of radius one whose centers differ by one coincide. All points of
this path have generic algebraic support, so none is a removed rigid
point. Thus the two separated source regions lie in the same path
component of the ordinary ambient domain. No connectedness theorem for
a product, or assertion about rigid G-connectedness, is needed for this
observation.

The F-images of the two source intervals are even identical, by (2.5).
This reinforces why target overlap cannot substitute for actual source
overlap.

## 3. Every dimension, with actual analytic product geometry

For n>=2 let

\[
 X=(\mathbb P^1_K)^n,\qquad
 W=(U_1\times_K\mathbb G_{m,K}^{n-1})^{an},
\quad
 F=(v(f),v(t_2),\ldots,v(t_n)).                   \tag{3.1}
\]

W is an actual ordinary algebraic-open analytic subspace of X^{an}.
We do NOT identify its points with a Cartesian product of the point
sets of its factors.

Instead use the genuine relative Gauss, or Shilov, section

\[
 \sigma:W_1\times\mathbb R^{n-1}\longrightarrow W. \tag{3.2}
\]

For x in W_1 and u=(u_2,...,u_n), it is the point in the torus over the
completed residue field H(x) with radii exp(-u_i). On a Laurent polynomial
with coefficients a_I in the coordinate ring of U_1 it is explicitly

\[
 \left|\sum_I a_I(z)t^I\right|_{\sigma(x,u)}
          =\max_I |a_I(x)|\,\mathrm e^{-I\cdot u}. \tag{3.3}
\]

This is multiplicative by the Gauss norm over the field H(x), so defines
an original-K analytic point. Projection to W_1 recovers x and evaluation
on t_i recovers u_i. Formula (3.3) gives continuity directly, or one may
use CLD 12.1.10 and Lemma 12.1.11. It is a continuous embedding onto this
particular section, not an exhaustive description of the product.

On the open preimage pr_1^{-1}(O_1), the first coordinate of F is
identically zero on an ordinary neighborhood. All local tropical images
there have dimension at most n-1. Hence

\[
 S_F\subset \operatorname{pr}_1^{-1}(D_0)
                   \cup\operatorname{pr}_1^{-1}(D_1).    \tag{3.4}
\]

The two terms are disjoint and closed in W. Each meets S_F in genuine
n-dimensional source patches: for s>ell and u in an open box,

\[
 F(\sigma(\gamma_i(s),u))=(s-\ell,u).              \tag{3.5}
\]

On a compact subbox this map is affine and injective, with continuous
inverse in its actual source. Equivalently these are the usual Gauss
skeleton patches of the open polyannuli |z-i|<r, together with the torus
coordinates. Every ordinary neighborhood of an interior point meets
this embedded n-dimensional parameter patch in a relatively open set,
and therefore has n-dimensional F-image. These patches lie in S_F.

Consequently (3.4) gives a nontrivial clopen separation of S_F in every
dimension. At fixed u, the continuous Shilov section of the path in
Section 2 joins the two patches inside W. Varying u gives actual
connected source families for the larger moments used below. Nothing
here infers a path of arbitrary analytic product points from a
Cartesian product of their projections.

The argument only needs this explicit path joining the selected patches.
It does not rely on a proof that every point of W is in that component.
Thus the obstruction cannot be dismissed as the choice of two unrelated
ambient connected components.

## 4. Adjoining units reveals full-dimensional rank-drop bridges

The functions z and z-1 are units on W. Form their actual concatenation

\[
             H=(F,v(z),v(z-1)).                  \tag{4.1}
\]

On the two Shilov families one has

\[
\begin{split}
 H(\sigma(\gamma_0(s),u))&=(\max(s-\ell,0),u,s,0),\\
 H(\sigma(\gamma_1(s),u))&=(\max(s-\ell,0),u,0,s).
\end{split}                                     \tag{4.2}
\]

In each strip 0<s<ell, the H-map has rank n in (s,u). These are genuine
H-source top patches. One can check this on the whole open annulus
r<|z|<1, respectively r<|z-1|<1: the displayed other valuations are
constant there, and (v(z),u), respectively (v(z-1),u), are its usual
polyannulus coordinates. Compact subboxes give actual H-cells.

But the projection H -> F has rank n-1 on every such strip, because
its s-column vanishes. These cells have dimension n in S_H and are
disjoint from S_F. They are NOT lower-dimensional cell-presentation
exceptions. Their closures connect to the old source patches at s=ell
and to one another through the common central Gauss family at s=0.

Thus adding units may provide real source paths not present for the old
moment. The generic noncontracted common-moment comparison cannot assign
the old coefficient to the interiors of these new strips. A separate
closedness or residual-curve incidence identity must do so.

There is no assertion that these particular strip constants cannot be
computed. On this elementary curve they are precisely the kind of
quantity a residual principal-divisor calculation can compare. The
example diagnoses the missing STEP, not an impossibility of all-moment
propagation or a counterexample to current rigidity.

## 5. What modification can and cannot change

A vertical blowup of a proper model has the same generic analytic space.
For the fixed analytic map F on W, maximal local tropical dimension is
intrinsic to that map and ordinary source topology. Model subdivision
therefore cannot alter S_F or join the separated sets (3.4).

The same is true of a generic birational modification on the algebraic
unit-open on which it is an actual isomorphism: after this identification,
the old F and its source set are unchanged. Adding more components to a
boundary does not, by itself, create new points of S_F.

Adjoining units is different: it changes the moment to H and may enlarge
the source. The containment S_F subset S_H and the full-rank versus
rank-drop dichotomy describe exactly the distinction. The larger source
may have connecting cells, but it also introduces their previously
undetermined coefficients. An assertion that all new cells inherit
their ratios by ordinary common refinement would discard the rank-drop
case illustrated above.

For a single SNC pair, top cells can also meet only through lower faces.
If such an attachment has codimension at least two, its existence is not
a residual-curve incidence of the n selected vertical components used
in the available wall theorem. Its residual stratum has larger
dimension. Turning it into suitable proper curve incidences requires
an additional construction, with actual source overlap and W-supported
tests. Connectedness of the complex alone supplies neither.

Removing the lower-dimensional exceptional sets of a capture argument
can separate the remaining top-cell interiors. A set's lack of an
additional R-measure term is not a license to ignore it when proving
propagation between the cells on its different sides.

## 6. A precise conditional incidence-chain criterion

This is a bookkeeping reduction, not a proof of the missing geometric
connectivity assertion.

Fix an ordinary W and a collection of actual moments on ordinary
subdomains of W for which the displayed representation R is assumed.
Use coefficient-constant source top-cell germs as vertices; restrictions
and subdivisions carry the same normalized ratio.

Allow two kinds of W-certified edge.

1. A noncontracted common-moment edge. There is an ACTUAL concatenated
   analytic moment on a common ordinary domain, and an isolatable
   represented common source top patch on which both projections have
   rank n. Evaluating the two coordinate descriptions of the same
   compact source-supported form through R gives equal normalized
   ratios. Both the current and canonical coefficients acquire the
   same absolute-determinant factor.

2. A residual-curve edge. The specified coordinate source germs belong
   to full inverse-image collars INSIDE W associated to the SAME
   proper residual curve at the SAME independent-normal monomial germ,
   with compatible collars over a common connected normal patch. Require
   the exact hypotheses needed for the local finite-projection,
   outer-collar functional and target-open
   comparison. These are explicit INPUTS, not proved here. With a fixed
   omitted normal multiplicity M_0, the local functional is
   lambda(p)=c_C[kappa(p):k], and its canonical coefficient is
   M_0[kappa(p):k]. Hence every one of these attached germs has ratio
   c_C/M_0. If omitted coordinates are changed, their proper rational
   Jacobian factors must be applied to both coefficients; they cannot
   be silently set to one.

Every edge has an actual equality witness on W; target overlap or a
formal model incidence without its analytic support does not count as
an edge. Then all vertices in one finite-path component have the same
ratio, simply by successive equality. If all the cell germs appearing
in a finite compact test presentation lie in one such component, the
R formula and the finite source partition give T=c delta on that test.
This uses R's lower-cell clause and does not derive R.

The still-unproved hypothesis for a general rigidity argument is:
the relevant germs from EVERY finite ordinary test presentation on a
specified connected W belong to a single such W-certified component,
with the same component compatible under passage to further moments
and test presentations.

Neither existence of some nearby wall for each germ, nor connectedness
of W or of a model dual complex, proves this hypothesis. The fixed
moment example shows an actual contracted bridge that any attempted
proof must treat. Enlarging a moment changes the graph; one must add
coefficient equality witnesses for the new rank-drop vertices, not only
a geometric path through them.

## 7. Exact next proof obligation and boundaries

A useful next geometric lemma would turn a prescribed same-source
connection across an attachment into a FINITE chain of residual-curve
and noncontracted-common-moment edges, all with their compact primitives
supported in W. It must state how to handle higher-dimensional residual
strata, additional horizontal boundary, retained multiplicities, and
the actual unit-open on which the generic modification is an isomorphism.

Alternatively a local theorem that makes the equivalence classes from
Section 6 into disjoint ordinary OPEN sets covering the relevant analytic
domain would permit a connectedness argument. Presently the classes are
classes of source germs, not such a partition of W. Dense independent
normal points and finite rank-exception sets do not alone produce it.

This note supplies no such general incidence-chain or openness lemma.
It does not use an integration-isomorphism for ordinary CLD cohomology,
a weakly smooth form comparison, or duality to bypass the positive-current
problem. It does not produce a nonconstant current or claim all-current
rigidity. The concrete progress is the full-source fixed-moment
obstruction, its original-field analytic-product realization, and an
explicit finite-witness criterion identifying exactly what propagation
would have to prove.

The parent supplied the research question, not the two-cluster example.
The investigator's earlier source-isolation, outer-collar and capture
work is related background and is not presented as independent evidence
for a new propagation theorem. Independent review and production gates
remain. No live text, frozen input, git state or production endpoint was
changed.
