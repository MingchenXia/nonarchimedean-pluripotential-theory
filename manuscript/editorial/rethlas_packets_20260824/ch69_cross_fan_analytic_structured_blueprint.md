# proposition prop:cross-calculus-package

<!-- rethlas-depends-on: -->
## statement

The following calculus package holds with the stated normalizations.

1. If (K) is complete and nontrivially valued, the analytification of a
   separated finite-type (K)-scheme is good, strict, and boundaryless.
2. The function (-\log|f|) of an invertible analytic function is integral
   harmonic.  On a compact strict domain, a coordinate map made from such
   functions is a harmonic tropicalization.
3. For (\mathbf G_m^{\an}) with coordinate (T), the moment skeleton is
   the real line of Gauss points (\eta_a), with
   (-\log|T(\eta_a)|=a), and has canonical weight one.  A primitive
   lattice map of generic analytic degree one preserves that weight.
4. Tropicalization is additive in analytic cycles.  For a skeletally proper
   moment map, analytic integration equals calibrated tropical integration,
   and the projection formula uses the lattice-index multiplicity exactly
   once.  Hence the chartwise tropical pushforward of an analytic cycle
   current is the skeletal current of the tropicalized cycle.
5. An effective analytic cycle defines a strongly positive order-zero
   current.  Analytic cycle currents are closed on a boundaryless space.
6. A continuous convex function on a tropical chart pulls back to a
   continuous psh function; a smooth convex function pulls back to a smooth
   psh function.
7. Proper pushforward of analytic currents commutes with
   (\mathrm d') and (\mathrm d''), and the integration current of a
   reduced pure-dimensional analytic space is the sum of the proper
   pushforwards of the currents of its irreducible components.

## proof

Item 1 is the algebraic-analytification theorem of Berkovich.  In the
application below it can also be checked on the two closed components,
which are copies of (\mathbf G_m^{\an}); the algebraic scheme is reduced
and pure one-dimensional before analytification.

For item 2, the trivial line bundle framed by (f) has trivial residual
bundle, hence a numerically trivial formal model in both directions.  This
is exactly `prop:ch18-harmonic-basic`, item `itm:ch18-hb:units`, following
Gubler--Jell--Rabinoff.  The compact-domain assertion is the definition of a
harmonic tropicalization.

Item 3 is `ex:trop-sigma-dim-one`.  The weight assertion is the
one-dimensional instance of `thm:analytic-tropical-balancing`: under an
integer-affine projection, a source facet of weight (m) contributes

\[
 [N_{\mathrm{target}}:F(N_{\mathrm{source}})]m
\]

to the target, with the generic analytic degree included exactly once.  A
primitive degree-one parameterization therefore contributes one.

Item 4 is `prop:trop-cycle-additive` together with
`prop:ch13-chart-integral` and `thm:cld-analytic-integration`.  Their proofs
pass to a common product chart.  The tropical projection formula identifies
the integral before and after projection, while subdivision invariance
removes the common refinement.  Thus both the lattice index and the
analytic generic degree occur once and only once.

For item 5, integration over a pure-dimensional closed analytic subspace is
positive because pullback preserves positivity and a positive top-degree
form has nonnegative calibrated integral.  It is order zero by the local
mass bound.  Stokes makes each boundaryless component current closed, and
local finiteness permits summation.  This is the complete content used from
`prop:ch14-delta-Y-current` and `prop:current-cycle-closed`.

For item 6, the smooth case follows from the pullback formula for the
positive semidefinite Hessian.  A continuous convex function is locally a
uniform limit of smooth convex functions, and continuous psh functions are
closed under locally uniform limits.  This is the proof of
`prop:ch16-tropically-convex`.

Finally, for a proper (g:Y\to X), pushforward is the transpose of pullback:

\[
 \langle g_*S,\alpha\rangle=\langle S,g^*\alpha\rangle.
\]

The identities (g^*\mathrm d'=\mathrm d'g^*) and
(g^*\mathrm d''=\mathrm d''g^*), evaluated against test forms, prove
commutation with both differentials.  Removing pairwise component
intersections, which have lower dimension and hence pair trivially with
top-degree forms, proves componentwise additivity of the fundamental
current.  This is `prop:current-pushforward-formal` and
`thm:current-fundamental-cycle`.

# lemma lem:cross-gm-laplacian

<!-- rethlas-depends-on: prop:cross-calculus-package -->
## statement

Let (G=\mathbf G_m^{\an}), let
(\sigma=-\log|T|:G\to\mathbf R), and let (F) be continuous piecewise
affine on (\mathbf R).  With the canonical weight-one lattice
normalization,

\[
 \mathrm d'\mathrm d''[F\circ\sigma]
 =\sum_a\bigl(F'_+(a)-F'_-(a)\bigr)\delta_{\eta_a},
\]

where the sum is locally finite.  In particular,

\[
 \mathrm d'\mathrm d''[|\sigma|]=2\delta_{\eta_0}.
\]

## proof

Pair against a compactly supported smooth test function.  Refine its chart
with (\sigma).  By the calibrated integration and projection statements
in `prop:cross-calculus-package`, the entire analytic-current pairing—not
merely a restriction to the skeleton—is the pairing on the real moment
line with lattice weight one.  Insert all break points of (F) meeting the
compact support.  On every interval of affinity, two integrations by parts
move (\mathrm d'\mathrm d'') to the test function.  The outer boundary
terms vanish by compact support; the two terms at an interior break point
(a) combine to

\[
                 \bigl(F'_+(a)-F'_-(a)\bigr)\varphi(a).
\]

Summing proves the formula.  For (F(r)=|r|), the derivative jumps from
(-1) to (1), so the coefficient is (2).  This is also the exact
weight-one specialization of `lem:ch15-vertex-atom`, whose coefficient is
the weighted sum of outgoing slopes.  No term occurs at infinity because
the test function has compact support.

# proposition prop:cross-abstract-package

<!-- rethlas-depends-on: prop:cross-calculus-package, lem:cross-gm-laplacian -->
## statement

On the unit-weighted cross

\[
 \Sigma=\mathbf R_{\geq0}(\pm e_1)\cup
        \mathbf R_{\geq0}(\pm e_2),
 \qquad u=2|s|,\quad v=|s|+|t|,
\]

the functions (u,v) are psh and
(\mathrm d'\mathrm d''[u]=\mathrm d'\mathrm d''[v]=4\delta_0).
If (h=u-v) and (T_\Sigma) is the positive closed skeletal current with
horizontal weights two and vertical weights one, then

\[
                  \mathrm d'\mathrm d''(hT_\Sigma)=2\delta_0.
\]

## proof

The functions are restrictions of continuous convex functions on
(\mathbf R^2), hence are psh by
`prop:cross-calculus-package`.  Smooth decreasing convex approximants are

\[
 2\sqrt{s^2+\varepsilon},\qquad
 \sqrt{s^2+\varepsilon}+\sqrt{t^2+\varepsilon}.
\]

The outgoing slopes of ((u,v,h)) in the directions
((e_1,-e_1,e_2,-e_2)) are

\[
 (2,2,0,0),\qquad(1,1,1,1),\qquad(1,1,-1,-1).
\]

The first two unit-weighted sums are four.  The (T_\Sigma)-weighted sum
for (h) is (2+2-1-1=2).  The graph-Laplacian computation of
`lem:cross-gm-laplacian`, ray by ray, gives the three displayed current
identities.  Opposite rays have equal positive weights, so (T_\Sigma) is
positive and balanced, hence closed.

# proposition prop:verified-cross-analytic-realization

<!-- rethlas-depends-on: prop:cross-calculus-package, lem:cross-gm-laplacian, prop:cross-abstract-package -->
## statement

\begin{proposition}\label{prop:verified-cross-analytic-realization}
Let $K$ be a complete algebraically closed nontrivially valued
non-Archimedean field, and put
\[
 X=V((x-1)(y-1))^{\an}\subset(\mathbf G_{m,K}^2)^{\an},
 \qquad
 \tau=(-\log|x|,-\log|y|):X\longrightarrow\mathbf R^2.
\]
Write
\[
 Y_h=V(y-1)^{\an},\qquad Y_v=V(x-1)^{\an}.
\]
Then $X$ is a reduced, pure one-dimensional, boundaryless good strict
analytic space, and
\[
 \tau(X)=(\mathbf R\times\{0\})\cup(\{0\}\times\mathbf R).
\]
The two coordinates of $\tau$ are locally integral harmonic, and the
tropicalization of the fundamental cycle $[X]$ has weight one on each of
the four rays.  For every $\rho>1$ in $|K^\times|$, the compact strict
domain
\[
 X_\rho=X\cap\{\rho^{-1}\leq|x|\leq\rho,\quad
                       \rho^{-1}\leq|y|\leq\rho\}
\]
is a harmonic-tropicalization chart whose image is the corresponding
truncated cross.

The effective analytic cycle and its integration current
\[
 Z=2[Y_h]+[Y_v],\qquad T=\delta_Z
\]
are respectively tropicalized to the cross with horizontal weights $2$
and vertical weights $1$ and to its positive closed skeletal current.
For
\[
 u(s,t)=2|s|,\qquad v(s,t)=|s|+|t|,
 \qquad U=u\circ\tau,\quad V=v\circ\tau,
\]
the functions $U,V$ are continuous psh functions and are decreasing
locally uniform limits of smooth psh pullbacks.  If $q_h$ and $q_v$ are the
unit Gauss points on $Y_h$ and $Y_v$, respectively, then they are distinct,
$\tau(q_h)=\tau(q_v)=0$, and, as analytic currents on $X$,
\[
 \dprimeddprime[U]=4\delta_{q_h},\qquad
 \dprimeddprime[V]=2\delta_{q_h}+2\delta_{q_v},
\]
where the right sides denote Dirac currents.  With $H=U-V$, multiplication
of the order-zero current $T$ by $H$ is defined and
\[
 \dprimeddprime(HT)=4\delta_{q_h}-2\delta_{q_v}.
\]
Consequently the chartwise tropical pushforwards satisfy
\[
 \tau_*\dprimeddprime[U]=\tau_*\dprimeddprime[V]=4\delta_0,
 \qquad
 \tau_*\dprimeddprime(HT)=2\delta_0.
\]
Thus the weighted cross-fan and the positive closed current occurring in
\Cref{prop:verified-cross-fan} admit an analytic realization, including the
claimed psh approximation and the weighted defect after tropical
pushforward.  This realization does not satisfy
$\dprimeddprime[U]=\dprimeddprime[V]$ before pushforward.
\end{proposition}

## proof

\begin{proof}
In the Laurent polynomial ring $K[x^{\pm1},y^{\pm1}]$, the prime elements
$x-1$ and $y-1$ have no common irreducible factor.  Since this ring is a
UFD,
\[
 ((x-1)(y-1))=(x-1)\cap(y-1).
\]
Hence $X$ is the reduced union $Y_h\cup Y_v$.  Both components are
isomorphic to $\mathbf G_m^{\an}$, and their intersection is the rigid
point $p=(1,1)$.  The first item of
\texttt{prop:cross-calculus-package} gives a good strict boundaryless
space; here every irreducible component has dimension one, so $X$ is pure
one-dimensional.

The functions $x$ and $y$ are invertible on $X$.  Thus the coordinates of
$\tau$ are integral harmonic locally.  On $Y_h$, the map is
\[
 -\log|x|\longmapsto(-\log|x|,0),
\]
and on $Y_v$ it is
\[
 -\log|y|\longmapsto(0,-\log|y|).
\]
The moment skeleton of each component is the real line of Gauss points, and
each displayed lattice map sends $1$ to the corresponding primitive basis
vector.  By the calibrated multiplicity statement in
\texttt{prop:cross-calculus-package}, the image is the cross and all four
fundamental weights are one.

The map $\tau$ is proper over compact subsets: on either component the
preimage of a bounded interval is a closed annulus, and the preimage of a
compact subset of $\mathbf R^2$ is closed in a finite union of such compact
annuli.  If $\rho>1$ belongs to $|K^\times|$, the displayed inequalities
define a compact strict analytic domain $X_\rho$, and its image is
\[
 [-\log\rho,\log\rho]\times\{0\}
 \ \cup
 \{0\}\times[-\log\rho,\log\rho].
\]
Its coordinates are logarithms of analytic units, so the restriction is a
harmonic tropicalization.  The full map is an ordinary noncompact
tropicalization that is locally harmonic.

For $Z=2[Y_h]+[Y_v]$, additivity and the primitive-index calculation give
weights $(2,2,1,1)$ in the directions
$(e_1,-e_1,e_2,-e_2)$.  Their balancing sum is zero.  The cycle-current
part of \texttt{prop:cross-calculus-package} shows that
$T=2\delta_{Y_h}+\delta_{Y_v}$ is positive, order zero, and closed, and
that its chartwise tropical pushforward is the skeletal current with these
weights.

The functions $u$ and $v$ are continuous convex functions.  Their pullbacks
are continuous psh.  If $\varepsilon_j\downarrow0$, then
\[
 u_j(s,t)=2\sqrt{s^2+\varepsilon_j},\qquad
 v_j(s,t)=\sqrt{s^2+\varepsilon_j}
          +\sqrt{t^2+\varepsilon_j}
\]
are smooth convex functions decreasing locally uniformly to $u,v$, because
\[
 \frac{\mathrm d^2}{\mathrm dr^2}\sqrt{r^2+\varepsilon_j}
 =\frac{\varepsilon_j}{(r^2+\varepsilon_j)^{3/2}}\geq0.
\]
Their pullbacks are the required smooth psh approximants.

Let $q_h$ and $q_v$ be the unit Gauss points in the component coordinates.
Both map to the origin, and they are distinct because
\[
 \begin{array}{c|cc}
       &|x-1|&|y-1|\\ \hline
  q_h  &1&0\\
  q_v  &0&1.
 \end{array}
\]
Put $s=-\log|x|$ on $Y_h$ and $t=-\log|y|$ on $Y_v$.  By
\texttt{lem:cross-gm-laplacian},
\[
 \dprimeddprime[|s|]=2\delta_{q_h},\qquad
 \dprimeddprime[|t|]=2\delta_{q_v}.
\]
There is no atom at $p$: on $|x-1|<1$, $|y-1|<1$, the ultrametric
inequality gives $|x|=|y|=1$, so the functions are locally constant.

The finite normalization is $Y_h\sqcup Y_v\to X$.  Componentwise
integration and commutation with proper pushforward give
\[
 \begin{array}{c|cc}
       &Y_h&Y_v\\ \hline
 U     &2|s|&0\\
 V     &|s|&|t|\\
 H=U-V &|s|&-|t|.
 \end{array}
\]
Therefore
\[
 \dprimeddprime[U]=4\delta_{q_h},\qquad
 \dprimeddprime[V]=2\delta_{q_h}+2\delta_{q_v}.
\]
Since $T$ has order zero, $HT$ is defined, and componentwise
\[
 HT=2|s|\,\delta_{Y_h}-|t|\,\delta_{Y_v},
 \qquad
 \dprimeddprime(HT)=4\delta_{q_h}-2\delta_{q_v}.
\]

Finally,
$\tau_*\delta_{q_h}=\tau_*\delta_{q_v}=\delta_0$ by the defining pairing
for tropical pushforward.  Pushing forward the preceding formulas gives
the claimed three identities.  They reproduce
\texttt{prop:cross-abstract-package}; before pushforward the first two
currents are unequal because $q_h\ne q_v$.
\end{proof}
