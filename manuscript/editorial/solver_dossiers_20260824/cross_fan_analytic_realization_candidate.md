# The split-Gauss cross-fan realization: candidate proof packet

## Purpose and verdict

This packet tests the explicit candidate
\[
 X=V\bigl((x-1)(y-1)\bigr)^{\mathrm{an}}
       \subset (\mathbf G_{m,K}^2)^{\mathrm{an}},
 \qquad
 Z=2[V(y-1)]+[V(x-1)]
\]
against `prob:frontier-cross-fan` and against the stronger formulation in
`output/open_problem_packets/cross_fan_analytic_realization.md`.

The strongest result proved here is the following.

> **Split-Gauss realization.**  Over a complete algebraically closed,
> nontrivially valued field \(K\), the ordinary tropicalization of \(X\) is
> the cross-fan with unit fundamental weights.  The positive closed analytic
> cycle current \(T=\delta_Z\) tropicalizes to horizontal weights \(2\) and
> vertical weights \(1\).  The two ambient convex functions
> \[
>       u(s,t)=2|s|,\qquad v(s,t)=|s|+|t|
> \]
> have continuous psh pullbacks \(U=u\circ\tau\) and \(V=v\circ\tau\), with
> the required smooth convex approximants.  Nevertheless, if \(q_h,q_v\)
> denote the two distinct unit Gauss points on the horizontal and vertical
> components, then
> \[
> \begin{aligned}
>  \mathrm d'\mathrm d''[U]&=4\delta_{q_h},\\
>  \mathrm d'\mathrm d''[V]&=2\delta_{q_h}+2\delta_{q_v},\\
>  \mathrm d'\mathrm d''((U-V)T)&=4\delta_{q_h}-2\delta_{q_v}.
> \end{aligned}
> \]
> Tropical pushforward identifies \(q_h\) and \(q_v\), and hence
> \[
> \begin{aligned}
>  \tau_*\mathrm d'\mathrm d''[U]
>    &=\tau_*\mathrm d'\mathrm d''[V]=4\delta_0,\\
>  \tau_*\mathrm d'\mathrm d''((U-V)T)&=2\delta_0.
> \end{aligned}
> \]

Thus the candidate completely realizes the tropical image, both sets of
multiplicities, the positive closed analytic cycle current, the psh
pullbacks, and the weighted defect **after tropical pushforward**.  It does
not give an analytic counterexample with
\(\mathrm d'\mathrm d''[U]=\mathrm d'\mathrm d''[V]\), because that equality
already fails before pushforward.  The stronger analytic-equality problem is
stated separately at the end.

There is one terminology qualification.  In Chapter 18 a “harmonic
tropicalization” is formally defined on a compact strict analytic domain.
No continuous real-valued map from a compact space can have the unbounded
cross-fan as its image.  The full map below is an ordinary tropicalization
on a noncompact good strict analytic space and is locally harmonic; compact
annular truncations are harmonic tropicalizations in the literal Chapter 18
definition and realize every bounded cross neighbourhood of the vertex.
Accordingly, an exact unbounded realization must be understood in the
ordinary/noncompact or local-exhaustion sense.

## Internal source anchors

The proof uses only the following results already present in the manuscript.

1. `manuscript/parts/part2/ch12_tropicalization.tex`:
   - `def:trop-tropical-polyhedron`, lines 2166--2187: skeletally proper
     moment maps and pushforward calibration;
   - `thm:analytic-tropical-balancing`, lines 2345--2361: tropical
     multiplicities and the lattice-index pushforward formula
     `eq:analytic-tropical-pushforward`;
   - `def:trop-cycle-calibration` and `prop:trop-cycle-additive`, lines
     2772--2801: additivity for analytic cycles;
   - `ex:trop-sigma-dim-one`, lines 1248--1260: the moment skeleton of
     \(\mathbf G_m^{\mathrm{an}}\) is the real line of Gauss points.
2. `manuscript/parts/part2/ch13_forms.tex`:
   - `prop:ch13-chart-integral`, lines 1311--1330, and
     `thm:cld-analytic-integration`, lines 1387--1401: integration and
     tropical projection on a chart.
3. `manuscript/parts/part2/ch14_currents.tex`:
   - `prop:current-pushforward-formal`, lines 2289--2344: proper pushforward
     commutes with the two differentials;
   - `prop:ch14-delta-Y-current`, lines 2452--2479: analytic cycle currents
     and positivity;
   - `thm:current-fundamental-cycle`, especially lines 2594--2619:
     componentwise additivity of the integration current;
   - `prop:current-cycle-closed`, lines 2622--2631: analytic cycle currents
     are closed;
   - `rem:ch14-pullback-survives`, lines 2429--2445: differentiating a
     pulled-back potential need not preserve equality of downstairs
     curvature currents.
4. `manuscript/parts/part2/ch16_bedford_taylor.tex`:
   - `prop:ch16-tropically-convex`, lines 421--441: a continuous convex
     function on a tropical chart pulls back to a continuous psh function.
5. `manuscript/parts/part2/ch18_delta_forms.tex`:
   - `eq:delta-graph-laplacian`, lines 199--214: the atomic Laplacian is the
     weighted sum of outgoing slopes;
   - `prop:ch18-harmonic-basic`, especially lines 2544--2565: logarithms of
     analytic units are harmonic;
   - the definition at lines 2686--2698 and
     `ex:ch18-harmonic-ordinary`, lines 2775--2786: compact harmonic
     tropicalizations and ordinary moment maps.
6. `manuscript/parts/part6/ch69_verified_extensions.tex`:
   - `eq:verified-current-multiplication`, lines 45--56: multiplication of
     an order-zero positive current by a continuous function;
   - `prop:verified-cross-fan`, lines 173--245: the target cross-fan
     calculation, including its smooth convex approximants and the
     normalization \(2\delta_0\).
7. `manuscript/parts/part6/ch72_major_open_problems.tex`:
   - `prob:frontier-cross-fan`, lines 1944--1961: the realization question
     and its required calibration, current, and psh checks.
8. Editorial atomization:
   - `manuscript/editorial/open_problem_atomic_inventory_20260824.md`,
     lines 298--307: `P21.1` is the harmonic-realization atom and
     `P21.2` is the positive-closed-current/multiplicity atom.

## 1. The analytic space and the tropicalization

Put
\[
 Y_h=V(y-1)^{\mathrm{an}},\qquad
 Y_v=V(x-1)^{\mathrm{an}}.
\]
The Laurent polynomial ring is a domain and the two distinct prime
elements \(x-1,y-1\) are coprime.  Hence
\[
 ((x-1)(y-1))=(x-1)\cap(y-1),
\]
so \(X\) is the reduced union \(Y_h\cup Y_v\).  Each component is isomorphic
to \(\mathbf G_m^{\mathrm{an}}\), and their intersection is the rigid point
\[
                         p=(1,1).
\]
As the analytification of a finite-type algebraic \(K\)-space, \(X\) is a
good strict analytic space.  It is pure of dimension one and has no analytic
boundary.  Concretely, apply `lem:berk-polydisc-exhaustion`
(`manuscript/parts/part1/ch04_berkovich.tex`, lines 539--613) after embedding
the affine Laurent coordinate ring using \(x,x^{-1},y,y^{-1}\).  It exhausts
the analytification by compact affinoid spectra and places every point in the
interior of a larger one.  Taking the radii in \(\lvert K^\times\rvert\)
gives strict affinoids.  Passing to the closed analytic hypersurface
preserves these local affinoid neighbourhoods.  This proves goodness,
strictness, and absence of boundary directly for this \(X\), without using
properness of the algebraic variety.

Let
\[
 \tau:X\longrightarrow\mathbf R^2,
 \qquad
 \tau(\xi)=\bigl(-\log|x(\xi)|,-\log|y(\xi)|\bigr).
\]
The coordinates \(x,y\) are invertible analytic functions on \(X\).  Thus
\(\tau\) is an ordinary moment map.  By
`prop:ch18-harmonic-basic`, item `itm:ch18-hb:units`, its two coordinates
are integral harmonic locally.

On \(Y_h\), the second coordinate is zero and the first runs through all of
\(\mathbf R\); on \(Y_v\), the first coordinate is zero and the second runs
through all of \(\mathbf R\).  Therefore
\[
 \tau(X)=
 (\mathbf R\times\{0\})\cup(\{0\}\times\mathbf R)=:\Sigma.
\]
This is exactly the four-ray cross-fan of
`prop:verified-cross-fan`.

The map is proper over compact subsets of \(\mathbf R^2\).  Indeed, on
either component, the inverse image of a bounded interval is contained in a
closed annulus, and is a closed subset of that compact affinoid.  Thus the
chartwise pushforwards below are defined.  Equivalently, the restriction to
the moment skeleton is skeletally proper in the sense of
`def:trop-tropical-polyhedron`.  The manuscript records the same basic
case explicitly: the chart \(T\) on \(\mathbf G_m^{\mathrm{an}}\) is
skeletally proper at Chapter 13, lines 2237--2249, and the full torus
tropicalization is proper at Chapter 14, lines 1387--1392.  Since \(X\) is
the union of two such closed components, the inverse image of a compact set
is a finite union of compact annuli.  Properness is therefore available both
for the calibrated pushforward of \(T\) and for the atomic measure
pushforwards in Section 6.

### Compact strict truncations

Choose \(\rho>1\) in \(\lvert K^\times\rvert\), put \(L=\log\rho\), and set
\[
 X_L=X\cap
 \{\rho^{-1}\leq|x|\leq\rho,\quad
   \rho^{-1}\leq|y|\leq\rho\}.
\]
This is a compact strict analytic domain and
\[
 \tau(X_L)=([-L,L]\times\{0\})
       \cup(\{0\}\times[-L,L]).
\]
The restriction \(\tau|_{X_L}\) is a harmonic tropicalization in the exact
sense of the definition at Chapter 18, lines 2686--2694, because it is
defined by analytic units.  These domains exhaust \(X\) as \(L\to\infty\)
through the value group and realize the germ of the full cross at the
origin.

The compact domains have analytic boundary at their four endpoints.  They
are used here only to meet the compact-domain definition of a harmonic
tropicalization.  Closedness of the cycle current below is asserted on the
boundaryless full space \(X\), not deduced from integration on a compact
truncation.

## 2. Fundamental and cycle multiplicities

On \(Y_h\simeq\mathbf G_m^{\mathrm{an}}\), the restriction of \(\tau\) is
the cocharacter map
\[
              \mathbf Z\longrightarrow\mathbf Z^2,qquad 1\longmapsto e_1.
\]
Its image is the primitive horizontal lattice \(\mathbf Ze_1\), so its
lattice index is one; the analytic map has generic degree one and residue
degree one.  The same argument on \(Y_v\) gives
\(1\mapsto e_2\), again with index and degree one.  Consequently every open
ray of the tropicalization of the reduced fundamental cycle \([X]\) has
weight one.  This also follows directly from
`ex:trop-sigma-dim-one` on the two components and the component additivity
in `thm:current-fundamental-cycle`.

Now take the effective analytic cycle
\[
                        Z=2[Y_h]+[Y_v].
\]
By `def:trop-cycle-calibration` and `prop:trop-cycle-additive`, its
tropicalization is
\[
 \operatorname{Trop}_\tau(Z)
 =2[\mathbf R\times\{0\}]+[\{0\}\times\mathbf R].
\]
Thus its four ray weights, in the order
\(+e_1,-e_1,+e_2,-e_2\), are
\[
                              (2,2,1,1).
\]
No hidden lattice factor occurs: all four tangent-lattice maps are primitive
and the degree and residue-degree factors are one.  The balancing check is
\[
                 2e_1+2(-e_1)+e_2+(-e_2)=0.
\]

Let
\[
                         T=\delta_Z
                           =2\delta_{Y_h}+\delta_{Y_v}.
\]
By `prop:ch14-delta-Y-current`, \(T\) is a strongly positive order-zero
analytic current.  By `prop:current-cycle-closed`, it is
\(\mathrm d'\)- and \(\mathrm d''\)-closed.  Its chartwise tropical
pushforward is precisely the positive closed skeletal current \(T_\Sigma\)
with the displayed weights.  This proves the current and multiplicity part
without declaring an arbitrary balanced fan to be analytic: the current is
the integration current of an explicit analytic cycle, and its weights have
been computed from the primitive lattice maps.

## 3. The psh pullbacks and their approximants

Write the coordinates on \(\mathbf R^2\) as \((s,t)\), and define
\[
       u(s,t)=2|s|,qquad
       v(s,t)=|s|+|t|,qquad
       h=u-v=|s|-|t|.
\]
Both \(u\) and \(v\) are continuous convex functions on all of
\(\mathbf R^2\).  Hence
\[
                 U=u\circ\tau,\qquad V=v\circ\tau
\]
are continuous psh functions on \(X\) by
`prop:ch16-tropically-convex`.

The precise ambient approximants required in Chapter 72 are available.  If
\(\varepsilon_j\downarrow0\), set
\[
 \begin{aligned}
  u_j(s,t)&=2\sqrt{s^2+\varepsilon_j},\\
  v_j(s,t)&=\sqrt{s^2+\varepsilon_j}
             +\sqrt{t^2+\varepsilon_j}.
 \end{aligned}
\]
The Hessian of \(r\mapsto\sqrt{r^2+\varepsilon_j}\) is
\[
             \frac{\varepsilon_j}
                  {(r^2+\varepsilon_j)^{3/2}}\geq0.
\]
Therefore \(u_j,v_j\) are smooth convex functions on \(\mathbf R^2\).  As
\(j\to\infty\), they decrease locally uniformly to \(u,v\), respectively.
Their pullbacks are smooth psh functions and decrease locally uniformly to
\(U,V\).  This is exactly the approximation used in the proof of
`prop:verified-cross-fan`, now pulled back through the explicit analytic
moment map.

## 4. The two analytic lifts of the tropical vertex

Let \(q_h\in Y_h\) be the unit Gauss point in the coordinate \(x\), and let
\(q_v\in Y_v\) be the unit Gauss point in the coordinate \(y\).  More
explicitly,
\[
 \left|\sum_n a_nx^n\right|_{q_h}=\max_n|a_n|,
 \qquad y(q_h)=1,
\]
and analogously with \(x,y\) interchanged for \(q_v\).  Both points map to
the tropical origin, since
\[
             |x(q_h)|=|y(q_h)|=|x(q_v)|=|y(q_v)|=1.
\]
They are nevertheless distinct analytic points.  Indeed,
\[
 \begin{array}{c|cc}
       &|x-1|&|y-1|\\ \hline
  q_h  &1&0\\
  q_v  &0&1.
 \end{array}
\]

The rigid intersection point \(p=(1,1)\) also lies in
\(\tau^{-1}(0)\), but it is not either Gauss point and it carries no
curvature in the calculation below.  On the analytic neighbourhood
\[
                  |x-1|<1,\qquad |y-1|<1
\]
of \(p\), the ultrametric inequality gives \(|x|=|y|=1\).  Hence
\(U=V=0\) there.

This is the geometric hinge of the example: the tropical map coalesces the
two distinct skeleton vertices \(q_h,q_v\), while the rigid point at which
the algebraic components meet lies off both relevant kink locations.

## 5. Exact analytic current calculation

On \(Y_h\simeq\mathbf G_m^{\mathrm{an}}\), put
\(s=-\log|x|\); on \(Y_v\simeq\mathbf G_m^{\mathrm{an}}\), put
\(t=-\log|y|\).  The moment skeleton of each component is a real line of
Gauss points by `ex:trop-sigma-dim-one`.  The function \(|s|\) is affine
away from \(s=0\) and has outgoing slopes \(1,1\) at the unit Gauss point.
The graph-Laplacian formula `eq:delta-graph-laplacian` therefore gives
\[
 \mathrm d'\mathrm d''[|s|]=2\delta_{q_h}
       \quad\text{on }Y_h,
 \qquad
 \mathrm d'\mathrm d''[|t|]=2\delta_{q_v}
       \quad\text{on }Y_v.                       \tag{1}
\]
Here \(q_h,q_v\) are type-2 points: the radius is
\(1\in\lvert K^\times\rvert\), the value-group extension is trivial, and
the residue transcendence degree is one.  The two nonconstant tangent
directions of the moment skeleton at either unit Gauss point are represented
by the primitive lattice vectors \(+1\) and \(-1\).  Along both directions
the outgoing derivative of \(|s|\), respectively \(|t|\), is \(+1\).
Because the component calibration, lattice index, and residue degree are all
one, `eq:delta-graph-laplacian` gives the mass
\(1\cdot1+1\cdot1=2\), with no factor of two or sign left implicit.  This
agrees with the normalization ledger in Chapter 19, lines 124--136: the
graph Laplacian is the sum of outgoing slopes and lattice lengths are
lattice-normalized.

There are no contributions at infinity because currents are tested against
compactly supported forms, and there is no contribution at \(p\) because
the functions are locally constant there.

The fundamental cycle of the reduced \(X\) is
\([X]=[Y_h]+[Y_v]\).  The proof of
`thm:current-fundamental-cycle` shows that integration and locally
integrable function currents add componentwise; the proper-pushforward
identity `prop:current-pushforward-formal` allows the differentials to be
computed on the finite normalization map
\[
                  \nu:Y_h\sqcup Y_v\longrightarrow X.
\]
The restrictions are
\[
 \begin{array}{c|cc}
      &Y_h&Y_v\\ \hline
 U&2|s|&0\\
 V&|s|&|t|\\
 H:=U-V&|s|&-|t|.
 \end{array}                                             \tag{2}
\]
Combining (1) and (2) gives the equalities of analytic Radon currents
\[
 \boxed{
 \begin{aligned}
  \mathrm d'\mathrm d''[U]&=4\delta_{q_h},\\
  \mathrm d'\mathrm d''[V]&=2\delta_{q_h}+2\delta_{q_v},\\
  \mathrm d'\mathrm d''[H]&=2\delta_{q_h}-2\delta_{q_v}.
 \end{aligned}}                                          \tag{3}
\]
Since \(q_h\ne q_v\), the last measure is nonzero.  In particular,
\[
                 \mathrm d'\mathrm d''[U]
                    \ne\mathrm d'\mathrm d''[V]           \tag{4}
\]
on \(X\).

The current \(T\) is positive and hence has order zero.  Multiplication by
the continuous function \(H\) is consequently defined by
`eq:verified-current-multiplication`.  Componentwise,
\[
          HT=2|s|\,\delta_{Y_h}-|t|\,\delta_{Y_v}.
\]
Applying (1) one more time yields
\[
 \boxed{
          \mathrm d'\mathrm d''(HT)
             =4\delta_{q_h}-2\delta_{q_v}.}                 \tag{5}
\]
This signed current is nonzero, but (5) by itself is not an analytic
counterexample to curvature-class independence: its putative premise (4)
is false.

## 6. Tropical pushforward and coalescence

For a compactly supported test form on \(\Sigma\), chartwise tropical
pushforward is defined by pairing its pullback against the analytic current.
The calibration and projection identities are those of
`prop:ch13-chart-integral` and `thm:cld-analytic-integration`.  On the atomic
currents in (3)--(5), no integration theorem is needed beyond the defining
pairing:
\[
                    \tau_*\delta_{q_h}
                     =\tau_*\delta_{q_v}=\delta_0.           \tag{6}
\]
Consequently (3) and (5) give
\[
 \boxed{
 \begin{aligned}
  \tau_*\mathrm d'\mathrm d''[U]&=4\delta_0,\\
  \tau_*\mathrm d'\mathrm d''[V]&=4\delta_0,\\
  \tau_*\mathrm d'\mathrm d''[H]&=0,\\
  \tau_*\mathrm d'\mathrm d''(HT)&=2\delta_0.
 \end{aligned}}                                            \tag{7}
\]

These are exactly the four tropical slope computations.  With unit weights,
the outgoing slopes at the origin are
\[
 \begin{array}{c|cccc|c}
  &+e_1&-e_1&+e_2&-e_2&\text{sum}\\ \hline
 u&2&2&0&0&4\\
 v&1&1&1&1&4\\
 h&1&1&-1&-1&0.
 \end{array}
\]
With \(T_\Sigma=\tau_*T\), the horizontal slopes receive weight \(2\) and
the vertical slopes weight \(1\), so
\[
        2\cdot1+2\cdot1+1\cdot(-1)+1\cdot(-1)=2.
\]
Thus (7) is the analytic source of the exact normalization in
`prop:verified-cross-fan`:
\[
 \mathrm d'\mathrm d''[u]=\mathrm d'\mathrm d''[v]=4\delta_0,
 \qquad
 \mathrm d'\mathrm d''(hT_\Sigma)=2\delta_0.
\]

There is no contradiction between (3) and (7).  Tropical pushforward is not
injective: it forgets which of the two analytic Gauss points over the origin
carries an atom.  The phenomenon is also an explicit instance of
`rem:ch14-pullback-survives`: two potentials whose curvature currents agree
downstairs can acquire different curvature currents after the potentials,
rather than the currents, are pulled back.

## 7. What is solved, and what remains

### Literal realization atoms

Under the natural locally harmonic/noncompact interpretation of the
unbounded fan, the construction proves all the data explicitly requested in
the live wording of `prob:frontier-cross-fan`:

1. the good strict analytic space and tropical chart are \(X\) and \(\tau\);
2. the image is the cross, with primitive lattice indices and unit
   fundamental multiplicities;
3. \(T=\delta_Z\) is a positive closed analytic cycle current and its
   tropical weights are \((2,2,1,1)\);
4. the displayed smooth ambient convex approximants pull back to psh
   functions;
5. the current product pushes forward to the verified tropical defect.

If “harmonic tropicalization” is read only in the compact-domain sense of
Chapter 18, the exact unbounded wording is formally impossible by
compactness.  The compact \(X_L\) give the precise corrected formulation:
they realize every truncated cross and the entire germ at the vertex, while
the full boundaryless \(X\) carries the closed analytic cycle current and
realizes the unbounded image as an ordinary locally harmonic
tropicalization.

### Stronger residual analytic-equality problem

The packet `output/open_problem_packets/cross_fan_analytic_realization.md`,
lines 21--27, asks for more: analytic psh pullbacks “for which the same
current calculation holds.”  To make that requirement unambiguous, the
genuinely stronger residual problem is:

> Construct a good strict analytic space \(X'\), a locally harmonic
> tropicalization \(\tau':X'\to\mathbf R^2\) with cross image and unit
> fundamental weights, and a positive closed analytic or delta-current
> \(T'\) with tropical weights \((2,2,1,1)\), such that for
> \[
>       U'=2|s|\circ\tau',\qquad
>       V'=(|s|+|t|)\circ\tau'
> \]
> one has the **analytic-current** identities
> \[
>     \mathrm d'\mathrm d''[U']
>       =\mathrm d'\mathrm d''[V'],
> \qquad
>     \mathrm d'\mathrm d''((U'-V')T')\ne0,
> \]
> with tropical pushforward of the latter equal to \(2\delta_0\); or prove
> that no such realization exists.

The present \(X,Z\) do not solve this residual problem, and no reweighting of
\(Z\) can repair the failure, because \(Z\) does not enter the premise
\(\mathrm d'\mathrm d''[U]=\mathrm d'\mathrm d''[V]\).  The precise
obstruction for this candidate is the split tropical vertex
\[
                       \tau^{-1}(0)\supset\{q_h,q_v\},
 \qquad q_h\ne q_v,
\]
which separates the two analytic curvature atoms before pushforward.  The
pushforward equality records only their total masses and is strictly weaker
than analytic equality.  This packet proves no obstruction for all possible
analytic spaces or all delta-currents, so the stronger residual problem must
remain open.

## Final audit and proposed atom disposition

### (i) Good strictness and boundarylessness

The hypersurface is reduced and pure one-dimensional.  The Laurent affine
analytification is covered by strict affinoids, and every point is interior
to a larger member of the exhaustion furnished by
`lem:berk-polydisc-exhaustion`; intersecting with the closed hypersurface
preserves the local affinoid property.  Hence the full \(X\), unlike a fixed
closed annular truncation, is good, strict, and boundaryless.  Closedness of
\(T\) is therefore the global analytic-cycle closedness of
`prop:current-cycle-closed`, not a boundary-cancellation assertion on
\(X_L\).

### (ii) Properness and pushforward

The restriction of \(\tau\) to either irreducible component is the standard
proper tropicalization \(\mathbf G_m^{\mathrm{an}}\to\mathbf R\).  The
preimage of a compact subset of \(\Sigma\) is a finite union of closed
annuli, hence compact.  The chart is skeletally proper, its calibrated
pushforward is defined, and compactly supported tropical test forms pull
back to compactly supported analytic test forms.  Atomic pushforward in
(6)--(7) is therefore legitimate, not a formal use of a nonproper map.

### (iii) Type-2 graph-Laplacian normalization

At each of \(q_h,q_v\), \(|s|\) or \(|t|\) has two primitive outgoing
directions, slope \(+1\) in each, and unit analytic calibration.  Therefore
its Laplacian is \(2\) times the Dirac mass at that type-2 point.  Scaling
the potential and the cycle coefficient produces, respectively, the masses
\(4,2\) in (3) and \(4,-2\) in (5).  Pushing both type-2 Dirac masses to the
same tropical origin yields \(4=2+2\) for the equal unweighted tropical
Laplacians and \(2=4-2\) for the weighted defect.

### (iv) Chapter 72 atoms

The current inventory separates `prob:frontier-cross-fan` into:

- `P21.1`: realize the weighted cross-fan by a harmonic tropicalization, or
  prove an obstruction;
- `P21.2`: realize the displayed weights by a positive closed analytic or
  delta-current, or prove an obstruction.

This packet removes `P21.2` affirmatively: \(T=\delta_{2Y_h+Y_v}\) is the
required positive closed analytic cycle current with exactly the displayed
weights.  It also removes `P21.1` under the only interpretation compatible
with the unbounded target: the full ordinary tropicalization is noncompact
and locally harmonic, and the \(X_L\) are literal compact harmonic
tropicalizations realizing all truncated vertex neighbourhoods.  If
`P21.1` is instead read as demanding one compact domain with image equal to
the whole unbounded fan, it should be retired as impossible by compactness,
not left open.

The two atoms should be replaced, if the intended goal was an analytic
counterexample rather than an analytic source for the tropical
counterexample, by one stronger residual atom:

- **Residual cross-fan analytic-equality atom:** construct an analytic
  realization for which
  \(\mathrm d'\mathrm d''[U]=\mathrm d'\mathrm d''[V]\) already on the
  analytic space while
  \(\mathrm d'\mathrm d''((U-V)T)\ne0\), with pushforward
  \(2\delta_0\); or prove a general obstruction.

The split-Gauss candidate does not decide that residual atom.  Its complete
and exact obstruction is (3): the tropical vertex has two distinct type-2
lifts, and tropical pushforward hides their separation.
