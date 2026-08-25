# lemma lem:cross-specific-units-harmonicity

<!-- rethlas-depends-on: -->
## statement

Let \(K\) be a complete algebraically closed nontrivially valued
non-Archimedean field, and set
\[
 A=K[x^{\pm1},y^{\pm1}]/((x-1)(y-1)),\qquad
 X=(\operatorname {Spec}A)^{\an}.
\]
Put \(Y_h=V(y-1)^{\an}\), \(Y_v=V(x-1)^{\an}\), and
\(p=(1,1)\).  Then
\[
 X=Y_h\cup Y_v,\qquad Y_h\cap Y_v=\{p\},
\]
is a reduced pure one-dimensional good strict analytic space without
analytic boundary, and each component is a closed copy of
\(\mathbf G_m^{\an}\).  The functions \(x,y\) are analytic units on \(X\);
consequently
\[
             -\log|x|,\qquad-\log|y|
\]
are locally integral harmonic functions.

For every \(\rho>1\) in \(|K^\times|\), the set
\[
 X_\rho=X\cap
 \{\rho^{-1}\leq |x|\leq\rho,\quad
   \rho^{-1}\leq |y|\leq\rho\}
\]
is a compact strict analytic domain.  The restriction to \(X_\rho\) of
\(\tau=(-\log|x|,-\log|y|)\) is a harmonic tropicalization, while on the
full noncompact \(X\) the same map is an ordinary tropicalization with
locally integral harmonic coordinates.

## proof

The Laurent polynomial ring
\(R=K[x^{\pm1},y^{\pm1}]\) is a unique factorization domain.  The prime
elements \(x-1\) and \(y-1\) are not associates, so an element divisible
by both is divisible by their product.  Hence
\[
             ((x-1)(y-1))=(x-1)\cap(y-1).                 \tag{1}
\]
The quotient in (1) is reduced, its two minimal primes are the displayed
principal ideals, and both quotients are Laurent polynomial rings in one
variable.  Thus the algebraic scheme is the reduced union of two
one-dimensional components meeting at the maximal ideal
\((x-1,y-1)\).  Analytifying the quotient maps gives
\[
 Y_h\simeq(\operatorname {Spec}K[x^{\pm1}])^{\an},
 \qquad
 Y_v\simeq(\operatorname {Spec}K[y^{\pm1}])^{\an},
\]
and their analytic intersection is the single rigid point \(p\).
Reducedness can also be checked on the two quotient seminorms furnished by
(1), so no assertion about nilpotents is being imported.

Here is a direct affinoid audit of the analytic adjectives.  If
\(\rho\in|K^\times|\), the inequalities in the statement are rational
Laurent inequalities.  Their intersection with \(X\) is therefore the
spectrum of a quotient of a strict Laurent Tate algebra and is a compact
strict affinoid domain.  These domains cover \(X\): at any analytic point
the four positive numbers
\(|x|,|x|^{-1},|y|,|y|^{-1}\) are finite, so a sufficiently large
\(\rho\) bounds them.  Given a point of \(X_\rho\), choose
\(\rho'>\rho\) in \(|K^\times|\); all four inequalities are then strict
at that point relative to \(X_{\rho'}\).  Thus every point has a strict
affinoid neighbourhood and lies in the relative interior of a larger such
domain.  This proves goodness and strictness and, by the definition of the
analytic boundary as the complement of the relative interior over the
base, proves \(\partial X=\varnothing\).  The two minimal components found
above both have dimension one, so \(X\) is pure one-dimensional.  Notice
that a fixed \(X_\rho\) has four annular boundary points; only the full
exhausted space is asserted to be boundaryless.

It remains to check harmonicity without citing an internal theorem.
For an analytic unit \(f\), the function \(-\log|f|\) is integral
piecewise linear by the definition of an integral PL function: it is the
logarithmic norm of one meromorphic function with integral coefficient
one.  Its residual line bundle is the residue of the trivial line bundle
with the frame \(f\).  The frame is nowhere zero, so this residual bundle
is trivial.  Its degree on every proper residual curve is therefore zero,
and the same is true for its dual.  By the definition of an integral
harmonic PL function—numerical triviality of this residual bundle—the
function \(-\log|f|\) is harmonic.  Applying this to the global units
\(x,y\) proves the assertion.  Finally, a map on a compact strict domain
whose coordinates are integral harmonic functions is, by definition, a
harmonic tropicalization.  This applies to \(X_\rho\); dropping
compactness leaves the asserted ordinary locally harmonic
tropicalization.

# lemma lem:cross-explicit-gm-skeleton-weights

<!-- rethlas-depends-on: lem:cross-specific-units-harmonicity -->
## statement

For \(G=\mathbf G_m^{\an}\) with coordinate \(T\), define, for
\(a\in\mathbf R\),
\[
 \left|\sum_{n\in\mathbf Z}c_nT^n\right|_{\eta_a}
      =\max_n |c_n|e^{-an}
\]
whenever the Laurent polynomial is finite.  These seminorms extend to
points \(\eta_a\in G\); the map
\[
 a\longmapsto\eta_a
\]
is the standard moment skeleton and is inverse to
\(\sigma=-\log|T|\) on that skeleton.  Its two primitive tangent
directions are \(+1,-1\), and its canonical one-dimensional calibration
has weight one.  The map
\[
 r:G\longrightarrow\{\eta_a:a\in\mathbf R\},\qquad
r(\xi)=\eta_{\sigma(\xi)}
\]
is a continuous retraction.  Every connected component of the complement
of the skeleton is a Berkovich open ball on which \(|T|\), hence
\(\sigma\), is constant.  At \(q=\eta_0\), the only tangent directions
on which \(\sigma\) has nonzero slope are the directions toward \(0\) and
\(\infty\), and those slopes are respectively \(+1\) and \(-1\) after an
orientation of the skeleton; every other tangent direction has slope zero.

For the \(X\) and \(\tau\) of
\(\textnormal{lem:cross-specific-units-harmonicity}\), the map \(\tau\)
is proper and
\[
 \tau(X)=(\mathbf R\times\{0\})\cup(\{0\}\times\mathbf R).
\]
The tropicalization of the reduced fundamental cycle \([X]\) has weight
one on each of the four open rays.  Moreover
\[
 \tau(X_\rho)=
 [-\log\rho,\log\rho]\times\{0\}\ \cup\
 \{0\}\times[-\log\rho,\log\rho].
\]

## proof

The non-Archimedean Gauss lemma says that the displayed maximum is
multiplicative on Laurent polynomials.  It extends continuously to every
closed Laurent annulus containing the radius \(e^{-a}\), hence defines a
bounded multiplicative seminorm and a Berkovich point \(\eta_a\).
Directly,
\[
                   |T(\eta_a)|=e^{-a},
 \qquad \sigma(\eta_a)=a.                                 \tag{2}
\]
As \(a\) varies, these points form the usual retraction skeleton of
\(\mathbf G_m^{\an}\).  More explicitly, the displayed formula for \(r\)
is continuous because both \(\sigma\) and \(a\mapsto\eta_a\) are
continuous, and (2) gives \(r(\eta_a)=\eta_a\).  Since
\(\sigma(r(\xi))=\sigma(\xi)\), \(\sigma\) is constant in every direction
contracted by \(r\).  At the unit Gauss point, tangent directions are
residue classes in \(\mathbf P^1_{\widetilde K}\).  The classes \(0\) and
\(\infty\) lead into the annuli \(|T|<1\) and \(|T|>1\); along them the
radius changes with primitive slope \(+1\) or \(-1\).  In every other
residue class one has \(|T|=1\), so the slope is zero.  This proves the
claimed tangent-direction audit.  At a type-\(2\) point \(\eta_a\), the
same description after rescaling the radius says that the directions
other than the two annular ones are open residue discs, each attached to
\(\eta_a\), and \(|T|=e^{-a}\) throughout each disc.  A type-\(3\)
skeleton point has only the two annular directions.  Thus all connected
components of the complement of the skeleton are such constant-radius
open discs, proving the remaining assertion about \(r\).

The coordinate \(a\) identifies the skeleton's integral tangent lattice
with \(\mathbf Z\).  By the definition of canonical
calibration, the identity parameterization of a one-dimensional moment
skeleton contributes
\[
 (\text{generic analytic degree})\,
 [\,\mathbf Z:\mathbf Z\,]=1\cdot1=1.                     \tag{3}
\]
Thus both orientations have primitive tangent vector \(\pm1\) and unit
weight.  Equation (3), rather than an unnamed balancing theorem, fixes the
normalization used below.

On \(Y_h\), use \(T=x\).  Since \(y=1\) there,
\[
          \tau|_{Y_h}(\xi)=(-\log|x(\xi)|,0).
\]
Equation (2) shows that its skeletal image is the whole horizontal line.
On \(Y_v\), with \(T=y\),
\[
          \tau|_{Y_v}(\xi)=(0,-\log|y(\xi)|),
\]
and its image is the whole vertical line.  This proves the asserted image.
The tangent-lattice homomorphisms are respectively
\[
 \mathbf Z\longrightarrow\mathbf Z^2,\quad1\longmapsto e_1,
 \qquad
 \mathbf Z\longrightarrow\mathbf Z^2,\quad1\longmapsto e_2.              \tag{4}
\]
Both images are primitive, both component maps have generic degree one,
and (3)–(4) give weight one on every open ray.  The rigid intersection
point has dimension zero and contributes no one-dimensional facet weight.

For properness, if \(C\subset\mathbf R^2\) is compact, choose \(M>0\)
with \(C\subset[-M,M]^2\) and then choose
\(\rho\in|K^\times|\) with \(\log\rho>M\).  The inverse image
\(\tau^{-1}(C)\) is closed in the compact strict domain \(X_\rho\), hence
compact.  Thus \(\tau\) is proper.  Restricting the two component formulas
to the defining annuli of \(X_\rho\) gives the last displayed truncated
cross exactly.

# proposition prop:cross-specific-cycle-current-pushforward

<!-- rethlas-depends-on: lem:cross-specific-units-harmonicity, lem:cross-explicit-gm-skeleton-weights -->
## statement

On the preceding \(X\), let
\[
                    Z=2[Y_h]+[Y_v],\qquad
                    T=\delta_Z=2\delta_{Y_h}+\delta_{Y_v}.
\]
Then \(T\) is a strongly positive order-zero analytic current and
\[
                         \mathrm d'T=\mathrm d''T=0.
\]
Its chartwise tropical pushforward by the proper map \(\tau\) is the
positive closed skeletal current on the cross with horizontal ray weights
two and vertical ray weights one.  More explicitly, integration on either
component is integration on its real moment line with lattice weight one,
and for every compactly supported top-degree test form \(\alpha\) on the
cross,
\[
 \langle\tau_*T,\alpha\rangle
 =2\int_{\mathbf R\times\{0\}}\alpha
   +\int_{\{0\}\times\mathbf R}\alpha.                    \tag{5}
\]

## proof

Only four foundational facts about the analytic differential-form calculus
are used here.  They are quoted completely so that no internal manuscript
label is a hidden premise.

First, Chambert-Loir–Ducros, Proposition 5.10.1(d), says: if
\(f:E\to V\) is a pleasant tropical chart on an \(n\)-dimensional
calibrated tropical space, \(\Pi_f\) has calibration \(\mu_{\Pi_f}\), and
\(\alpha\) is an integrable \((n,n)\)-form on a parlinear neighbourhood of
\(f(E)\), then
\[
       \int_E f^*\alpha
       =\int_{\Pi_f}\langle\alpha,\mu_{\Pi_f}\rangle.      \tag{6}
\]
The same proposition identifies the pushed Radon measure with the
calibrated measure.  Second, their Proposition 5.11.1(a) says: for a
compactly supported \(C^1\) form \(\omega\) of type \((n-1,n)\) on a
calibrated tropical space,
\[
                    \int_E\mathrm d'\omega
                    =\int_{\partial E}\omega,             \tag{7}
\]
and the \(\mathrm d''\) formula follows by the involution exchanging the
two Lagerberg degrees.  Third, their Theorem 15.7.1 says: a topologically
separated analytic space that is pure of dimension \(n\), equipped with
its analytic boundary, is a calibrated tropical space of level \(n\).
This identifies the boundary in (7) with the analytic boundary already
audited in the first lemma.  Fourth, their Proposition 15.2.8 says: on a
paracompact locally holomorphically separated analytic space, every open
cover admits a subordinate smooth partition of unity.  The affine analytic
curve \(\mathbf G_m^{\an}\) has these properties directly: powers of one
element of absolute value different from one give a countable compact
annular exhaustion, hence paracompactness, while two distinct points in a
common affinoid annulus differ on an analytic function, hence local
holomorphic separation.  This fourth statement is used only to reduce a
compactly supported test form to finitely many moment charts.  These are from
A. Chambert-Loir and A. Ducros,
“Formes différentielles réelles et courants sur les espaces de
Berkovich,” arXiv:1204.6277v2, Proposition 5.10.1(d) and Proposition
5.11.1, Theorem 15.7.1, and Proposition 15.2.8; the audited local copy is
\(\textnormal{tmp/pdfs/cld25.pdf}\), SHA-256
\(5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719\).
Equations (6)–(7) are the complete portions used below.

For a compactly supported \((1,1)\)-test form \(\beta\) on \(X\), define
\[
 \langle T,\beta\rangle
   =2\int_{Y_h}i_h^*\beta+\int_{Y_v}i_v^*\beta.            \tag{8}
\]
If \(\beta\) is strongly positive, its restriction to either component is
positive.  Formula (6), together with the unit calibration proved in
\(\textnormal{lem:cross-explicit-gm-skeleton-weights}\), makes each
integral in (8) nonnegative.  Thus \(T\) is strongly positive.
On a fixed compact support, finitely many moment charts reduce (8) to
integrals of bounded coefficients over compact intervals of finite
lattice length.  The absolute value is therefore bounded by a constant
times the coefficient sup norm.  This is precisely continuity of order
zero.

Let \(\gamma\) be a compactly supported test form of complementary degree.
By the definition of the current differential,
\(\langle\mathrm d'T,\gamma\rangle\), up to the fixed current sign, is the
sum of the integrals of \(\mathrm d'i_h^*\gamma\) and
\(\mathrm d'i_v^*\gamma\).  Each component is the boundaryless
\(\mathbf G_m^{\an}\) from the first lemma.  Formula (7) therefore gives
zero.  The involuted formula gives \(\mathrm d''T=0\).  This also explains
why closedness is asserted on the full \(X\), not on an annular
truncation.

Finally, properness was proved in the preceding lemma, so compactly
supported tropical test forms have compactly supported pullbacks.  On
\(Y_h\), formula (6) and (3) identify integration with unit-weighted
integration on the horizontal line; on \(Y_v\) they do the same on the
vertical line.  Substitution in (8) proves (5).  Positivity is visible from
the positive coefficients, and closedness of the skeletal current follows
either by pushing the already proved equalities
\(\mathrm d'T=\mathrm d''T=0\) through the defining transpose pairing, or
directly from cancellation of the two opposite rays of each line.

# lemma lem:cross-direct-psh-approximants

<!-- rethlas-depends-on: lem:cross-specific-units-harmonicity -->
## statement

On \(\mathbf R^2\), write
\[
 u(s,t)=2|s|,\qquad v(s,t)=|s|+|t|.
\]
For every sequence \(\varepsilon_j\downarrow0\), the functions
\[
 u_j(s,t)=2\sqrt{s^2+\varepsilon_j},\qquad
 v_j(s,t)=\sqrt{s^2+\varepsilon_j}
          +\sqrt{t^2+\varepsilon_j}
\]
are smooth convex and decrease locally uniformly to \(u,v\).  Their
pullbacks
\[
 U_j=u_j\circ\tau,\qquad V_j=v_j\circ\tau
\]
are smooth psh functions on \(X\), decrease locally uniformly to
\[
 U=u\circ\tau,\qquad V=v\circ\tau,
\]
and \(U,V\) are continuous psh functions.

## proof

For \(\varepsilon>0\), direct differentiation gives
\[
 \frac{\mathrm d^2}{\mathrm dr^2}\sqrt{r^2+\varepsilon}
       =\frac{\varepsilon}{(r^2+\varepsilon)^{3/2}}>0.     \tag{9}
\]
Thus the Hessians of \(u_j,v_j\) are positive semidefinite.  A smooth
function pulled back through a moment map satisfies the chain rule
\[
 \mathrm d'\mathrm d''(\phi\circ\tau)
 =\sum_{k,\ell}
   \frac{\partial^2\phi}{\partial z_k\partial z_\ell}
       (\tau)\,\mathrm d'\tau_k\wedge\mathrm d''\tau_\ell. \tag{10}
\]
For a positive-semidefinite Hessian, the form on the right of (10) is
positive by the elementary Gram-matrix criterion.  This is exactly the
definition of smooth psh, so \(U_j,V_j\) are smooth psh; no closure theorem
has been cited.

Because \(\varepsilon_j\) decreases, so do the square roots.  Moreover
\[
 0\leq\sqrt{r^2+\varepsilon_j}-|r|\leq\sqrt{\varepsilon_j},               \tag{11}
\]
uniformly in \(r\).  Equation (11) gives the claimed locally uniform
convergence (indeed, uniform convergence on all of \(\mathbf R^2\), with
the evident constants).

For completeness, psh of the limits is also direct at the current level.
On the compact support of any test form, locally uniform convergence gives
convergence of the order-zero function currents
\([U_j]\to[U]\) and \([V_j]\to[V]\).  Current differentiation is continuous,
so their \(\mathrm d'\mathrm d''\)-currents converge.  The cone of positive
currents is closed because its defining inequalities are evaluations on
strongly positive test forms.  Hence
\(\mathrm d'\mathrm d''[U]\) and
\(\mathrm d'\mathrm d''[V]\) are positive.  Continuity follows from that
of \(u,v,\tau\), proving that \(U,V\) are continuous psh.

# lemma lem:cross-exact-analytic-line-laplacian

<!-- rethlas-depends-on: lem:cross-explicit-gm-skeleton-weights, prop:cross-specific-cycle-current-pushforward -->
## statement

Let \(G=\mathbf G_m^{\an}\), let
\(\sigma=-\log|T|\), and let \(q=\eta_0\) be the unit Gauss point.
With the unit calibration and the current convention used above,
\[
                 \mathrm d'\mathrm d''[|\sigma|]
                         =2\delta_q.                       \tag{12}
\]
Equality (12) is an equality of analytic currents against arbitrary
compactly supported smooth test functions on \(G\), not only against test
functions factored through \(\sigma\).  There is no atom at a rigid point
and no term at either infinite end.

## proof

Let \(\varphi\) be an arbitrary compactly supported smooth test function
on \(G\).  Choose a compact Laurent annulus containing its support, a
finite moment-chart cover by relatively compact subcharts, and a smooth
partition of unity whose relevant pieces have compact support in those
subcharts.  It suffices by linearity to treat one summand of the
partitioned test function.  On its chart, adjoin the globally defined unit
\(T\) to the chart's moment map.  The resulting
one-dimensional calibrated moment graph \(\Gamma\) simultaneously
describes that summand and \(\sigma\), and the integration formula (6)
computes its full analytic pairing on \(\Gamma\).  Each artificial outer
chart boundary has zero contribution because the summand is compactly
supported inside its chart.  This use of product moment maps and a
partition is what prevents the argument from testing only functions of
\(\sigma\).

The explicit retraction from the skeleton lemma,
\[
                  r:G\longrightarrow
                  S=\{\eta_a:a\in\mathbf R\}
\]
satisfies \(\sigma=\sigma|_S\circ r\).  Every component of \(G\setminus S\)
is contracted by \(r\), and the identity
\(\sigma=\sigma|_S\circ r\) makes \(\sigma\) constant there.  Hence
\(|\sigma|\) has slope zero on every edge of \(\Gamma\) contracted by
\(r\).  On the skeleton it is affine except at \(q=\eta_0\).  At \(q\),
the tangent-direction audit in the skeleton lemma shows that its two
noncontracted primitive outgoing directions are \(+1\) and \(-1\), and
its outgoing slope in each is \(+1\); all other directions have slope
zero.  Both noncontracted directions have weight one by that lemma.

We spell out the one-dimensional integration by parts.  Subdivide
\(\Gamma\) at \(q\), at every vertex needed for the test chart, and outside
\(\operatorname {supp}\varphi\).  On an oriented edge with coordinate
\(a\), two ordinary integrations by parts give
\[
 \int F(a)\varphi''(a)\,\mathrm da
   =\bigl[F\varphi'-F'\varphi\bigr]_{\partial e}
      +\int F''(a)\varphi(a)\,\mathrm da.                 \tag{13}
\]
Here \(F=|\sigma|\) is affine in every open edge, so the last integral
vanishes.  At an internal vertex where \(F\) is affine through the vertex,
the boundary contributions from adjacent oriented edges cancel.  On an
edge contracted by \(r\), \(F'=0\), so it contributes nothing.  Outer
terms vanish because \(\varphi\) has compact support.  At \(q\), the
remaining \(-F'\varphi\) terms, with the outward orientations on the two
sides, add to
\[
                   (1+1)\varphi(q)=2\varphi(q).           \tag{14}
\]
Equations (6), (13), and the definition of the distributional
\(\mathrm d'\mathrm d''\) pairing identify the left side with
\(\langle\mathrm d'\mathrm d''[|\sigma|],\varphi\rangle\).
Thus (14) proves (12) for arbitrary \(\varphi\).

The unit Gauss point is type \(2\): its radius is
\(1\in|K^\times|\), its value-group extension is trivial, and its residue
field has transcendence degree one.  Formula (14) therefore also audits
the type-\(2\) normalization: two primitive directions, each of slope and
weight one, give mass two.  A rigid point lies in a contracted open-ball
direction where the potential is locally constant, and infinity is
excluded by compact support, proving the last sentence.

# proposition prop:cross-componentwise-normalization

<!-- rethlas-depends-on: lem:cross-specific-units-harmonicity, lem:cross-explicit-gm-skeleton-weights, prop:cross-specific-cycle-current-pushforward, lem:cross-direct-psh-approximants, lem:cross-exact-analytic-line-laplacian -->
## statement

Let \(q_h\) be the unit Gauss point of \(Y_h\) in coordinate \(x\), and
let \(q_v\) be the unit Gauss point of \(Y_v\) in coordinate \(y\).  Then
\[
 q_h\ne q_v,\qquad \tau(q_h)=\tau(q_v)=0.
\]
For \(U,V\) as above and \(H=U-V\), the analytic current identities on
\(X\) are
\[
 \mathrm d'\mathrm d''[U]=4\delta_{q_h},\qquad
 \mathrm d'\mathrm d''[V]=2\delta_{q_h}+2\delta_{q_v},    \tag{15}
\]
and, for \(T=2\delta_{Y_h}+\delta_{Y_v}\),
\[
             \mathrm d'\mathrm d''(HT)
                    =4\delta_{q_h}-2\delta_{q_v}.          \tag{16}
\]
The product \(HT\) is well defined.  Under proper tropical pushforward,
\[
 \tau_*\delta_{q_h}=\tau_*\delta_{q_v}=\delta_0,
\]
and consequently
\[
 \tau_*\mathrm d'\mathrm d''[U]
  =\tau_*\mathrm d'\mathrm d''[V]=4\delta_0,\qquad
 \tau_*\mathrm d'\mathrm d''(HT)=2\delta_0.               \tag{17}
\]

## proof

The finite normalization is the explicit map
\[
              \nu:Y_h\sqcup Y_v\longrightarrow X.         \tag{18}
\]
For any current \(S\) on the source, proper pushforward is defined by
\[
              \langle\nu_*S,\alpha\rangle
                   =\langle S,\nu^*\alpha\rangle.          \tag{19}
\]
Naturality of forms gives
\(\nu^*\mathrm d'=\mathrm d'\nu^*\) and
\(\nu^*\mathrm d''=\mathrm d''\nu^*\).  Inserting these equalities in
(19), with the defining current signs, proves
\[
 \nu_*\mathrm d'S=\mathrm d'\nu_*S,\qquad
 \nu_*\mathrm d''S=\mathrm d''\nu_*S.                     \tag{20}
\]
No pushforward theorem is being invoked by name.

Top-degree integration over a reduced pure curve is the sum over its
generic components.  In this case this also follows directly from (8):
the intersection \(p\) is zero-dimensional and has zero
one-dimensional calibrated measure.  Thus the function current of a
locally integrable \(W\) on \(X\) is
\[
 [W]_X=\nu_*\bigl([W|_{Y_h}]_{Y_h}\oplus
                  [W|_{Y_v}]_{Y_v}\bigr).                 \tag{21}
\]

Let \(s=-\log|x|\) on \(Y_h\), and
\(t=-\log|y|\) on \(Y_v\).  The restrictions are
\[
 \begin{array}{c|cc}
       &Y_h&Y_v\\ \hline
 U     &2|s|&0\\
 V     &|s|&|t|\\
 H     &|s|&-|t|.
 \end{array}                                               \tag{22}
\]
The two Gauss points both map to the tropical origin.  They are distinct,
because their seminorms give
\[
 \begin{array}{c|cc}
       &|x-1|&|y-1|\\ \hline
 q_h   &1&0\\
 q_v   &0&1.
 \end{array}                                               \tag{23}
\]
The rigid node \(p\) gives both values zero.  On the neighbourhood
\(|x-1|<1,\ |y-1|<1\), the ultrametric inequality gives
\(|x|=|y|=1\), so all three functions in (22) are locally constant there;
hence no atom occurs at \(p\).

Apply the exact line formula (12) to \(s\) and \(t\), then use
(20)–(22).  This gives
\[
 \begin{aligned}
 \mathrm d'\mathrm d''[U]
   &=4\delta_{q_h}+0,\\
 \mathrm d'\mathrm d''[V]
   &=2\delta_{q_h}+2\delta_{q_v},
 \end{aligned}
\]
which is (15).

The current \(T\) has order zero by the cycle-current proposition, so a
continuous function multiplies it by the defining formula
\(\langle HT,\alpha\rangle=\langle T,H\alpha\rangle\).
Using (22),
\[
              HT=2|s|\,\delta_{Y_h}
                    -|t|\,\delta_{Y_v}.                   \tag{24}
\]
Equations (12), (20), and (24) give (16).

Finally, for every compactly supported test function \(\psi\) at the
tropical origin, the transpose definition gives
\[
 \langle\tau_*\delta_{q_h},\psi\rangle
      =\psi(\tau(q_h))=\psi(0)
      =\langle\delta_0,\psi\rangle,
\]
and identically for \(q_v\).  Properness of \(\tau\) was proved in the
skeleton lemma, so this pushforward is legitimate for all compactly
supported test forms.  Pushing (15)–(16) forward gives (17).

# proposition prop:verified-cross-analytic-realization

<!-- rethlas-depends-on: lem:cross-specific-units-harmonicity, lem:cross-explicit-gm-skeleton-weights, prop:cross-specific-cycle-current-pushforward, lem:cross-direct-psh-approximants, lem:cross-exact-analytic-line-laplacian, prop:cross-componentwise-normalization -->
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
The reduced decomposition, purity, good strictness, boundarylessness, unit
harmonicity, and compact harmonic truncations are exactly
\(\textnormal{lem:cross-specific-units-harmonicity}\).
The explicit Gauss skeleton computation in
\(\textnormal{lem:cross-explicit-gm-skeleton-weights}\) proves properness,
the cross image, the truncation image, and all four unit fundamental
weights.

The effective cycle-current statement, including order zero, positivity,
closedness, and the exact horizontal and vertical tropical weights, is
\(\textnormal{prop:cross-specific-cycle-current-pushforward}\).
The functions and their stated decreasing smooth psh approximants are
provided by \(\textnormal{lem:cross-direct-psh-approximants}\).

The normalization
\(\mathrm d'\mathrm d''[|-\log|T||]=2\delta_{\eta_0}\), including arbitrary
analytic test functions and the absence of rigid or infinite-end atoms, is
\(\textnormal{lem:cross-exact-analytic-line-laplacian}\).
Applying it through the explicit normalization map, with all component
coefficients and atomic pushforwards written out, is
\(\textnormal{prop:cross-componentwise-normalization}\); that proposition
is precisely the three analytic identities and the three pushed identities
displayed in the statement.

These six dependencies prove every assertion.  In particular, the phrase
referring to the weighted cross-fan uses only the explicitly recomputed
weights and defect above; it does not import any assertion from the live
proposition named in that phrase.  Finally,
\(q_h\ne q_v\) and (15) show directly that the two unpushed curvature
currents differ.
\end{proof}
