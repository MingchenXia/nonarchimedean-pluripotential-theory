# Nearby all-vertical residual-curve walls on a given SNC pair

1 September 2026. Author: /root/p081_weighted_repair_fresh.

Status: a new original-field geometric candidate, not independently audited
or production accepted. No current is pulled back. No arbitrary-chart model
capture, ordinary whole-tube containment, or current-rigidity theorem is
claimed. The source distinctions are in SOURCE_LEDGER.md.

## 1. Exact statement

Let R be a complete discrete valuation ring with fraction field K, residue
field k of characteristic zero, uniformizer pi, and
\(\ell=-\log|\pi|>0\). The field k need not be algebraically closed.
Let \(\mathcal X\) be an actual proper flat regular integral R-scheme of
finite type, with smooth generic fibre X of dimension n>=2. Let

\[
 D=(\mathcal X_k)_{\mathrm{red}}+H
\]

be a reduced strict SNC divisor, where H is a finite union of horizontal
prime divisors. Here strict SNC means that the local equations of all
boundary components through a point are part of a regular parameter system.
We permit intersections to have several connected components and choose
components explicitly. We do not require the special fibre to be reduced.

Suppose p is a closed point lying on n+1 distinct components
\(D_0,\ldots,D_n\) of D. They are all boundary components through p.
Choose their local equations \(z_0,\ldots,z_n\); these are a regular
parameter system of \(A=\mathcal O_{\mathcal X,p}\). Write

\[
 \pi=u\prod_{i=0}^n z_i^{N_i},\qquad
 u\in A^\times,\quad N_i\in\mathbb Z_{\geq0},
 \quad N\ne0.                                      \tag{1.1}
\]

The positive N_i are the vertical multiplicities, and N_i=0 for a
horizontal D_i. Set

\[
 \Sigma^\circ=\{\alpha\in\mathbb R_{>0}^{n+1}:
                      N\cdot\alpha=\ell\}.         \tag{1.2}
\]

Section 2 constructs the continuous monomial embedding
\(\iota:\Sigma^\circ\longrightarrow X^{\mathrm{an}}\).
Its image is the full-dimensional open cell at p for this pair. Fix
\(\xi=\iota(\alpha)\), an ordinary open neighbourhood W of xi, and any
relative open neighbourhood V of alpha in \(\Sigma^\circ\).

**Claim.** There is a finite composition
\(f:\mathcal X'\longrightarrow\mathcal X\) of blowups of connected
components of closed intersections of boundary components, each center
contained in the special fibre, with the following properties.

1. The model \(\mathcal X'\) is proper, flat, regular and integral over
   the SAME R. The reduced total-transform boundary is strict SNC.
   The generic-fibre map is the identity isomorphism on X.
2. The refined pair has an n-dimensional CLOSED monomial simplex tau
   whose n+1 vertices all correspond to vertical prime divisors. Its
   image in the original cell is contained in V, and every point of
   this closed simplex, viewed in the original \(X^{\mathrm{an}}\),
   belongs to W.
3. An (n-1)-face F of tau is the monomial face associated to a whole
   connected component C of an intersection of n vertical prime
   divisors on \(\mathcal X'\). This C is a smooth proper integral
   k-curve. In fact C maps to the original closed point p. It is not
   required to be geometrically connected over k.
4. The relative interior of F contains a point eta in W whose n
   positive normal weights at \(\eta_C\) are Q-linearly independent.
   Such points are dense in that relative interior.

Thus suitable all-vertical residual-curve walls occur arbitrarily near a
given point of this actual full-dimensional model cell. The result includes
cells with horizontal directions at the start; its final selected wall
has only vertical normal components.

The theorem does NOT say that a wall can pass through the originally
specified xi. Nor does it place any new wall in an unrelated source cell
merely because that source cell also contains xi. Section 8 gives the
precise topological consequence and the remaining limitations.

## 2. Original-field monomial points and topology

The complete local ring of the regular equicharacteristic-zero local ring A
has a coefficient field \(\kappa(p)\) and an isomorphism

\[
 \widehat A\simeq\kappa(p)[[z_0,\ldots,z_n]].       \tag{2.1}
\]

This is the same local construction used in BFJ Section 3.3, equations
(3.2)-(3.4). We apply it to all the boundary parameters, including the
horizontal ones, rather than attributing this added case to the literal
vertical statement of BFJ Theorem 3.1.

For alpha in (1.2), give a nonzero power series the weighted monomial value

\[
 v_\alpha\left(\sum_\nu c_\nu z^\nu\right)
       =\min_{c_\nu\ne0}\nu\cdot\alpha.            \tag{2.2}
\]

All weights are positive. Below any fixed value there are only finitely
many possible exponents, so the minimum exists. The initial weighted
polynomials multiply without cancellation in the polynomial domain over
\(\kappa(p)\); hence (2.2) is a valuation. A maps injectively to its
completion and its fraction field is K(X), so this gives a valuation on
K(X). Every unit of A has value zero. Consequently (1.1) gives
\(v_\alpha(\pi)=\ell\). Every nonzero element of K is a power of pi
times a unit of R, so the restriction to K is exactly the specified
valuation. We have constructed a point of the original K-analytic space,
with generic algebraic support and center p on the proper model. No
extension of K or current base change occurs.

Continuity follows directly from (2.2). Near any fixed alpha all weights
have a common positive lower bound. The tail of any given power series
therefore has uniformly arbitrarily large value as its total degree
increases. Locally, the value of a nonzero series is the minimum of
finitely many linear functions; the same holds by subtraction for a
nonzero rational function. The topology of an affine analytification is
the topology of evaluation of its coordinate-ring functions. Since all
these points have generic algebraic support, they lie in every nonempty
generic affine open. This proves continuity of iota. Evaluation on the
rational functions z_i recovers alpha_i, giving injectivity and a
continuous inverse onto the image. In particular, on every compact box
inside (1.2), iota is a topological embedding.

For completeness, changing coefficient fields does not affect this cell.
On the dense set where the n+1 weights are Q-linearly independent, every
finite leading expansion has a unique least term. Its value is therefore
forced for any centered valuation with these parameter values. The tail
has larger value. Continuity gives equality at the other weights. This
is BFJ's uniqueness argument in Section 3.3, and it works with zero as
well as positive entries of N because the weights alpha_i themselves
are strictly positive. The analogous change of boundary generators by
local units preserves their values. The homogeneous rational hyperplanes
cannot contain the affine hyperplane N.alpha=ell, since ell is nonzero,
which justifies the density assertion just used.

Choose a small convex open ball B, with compact closure in
\(V\cap\iota^{-1}(W)\). All choices below take place in B. For a
nonzero vector a with \(N\cdot a>0\), define its normalized slice point

\[
       P(a)=\frac{\ell a}{N\cdot a}.               \tag{2.3}
\]

Rational rays with strictly positive coordinates are dense in the positive
cone. Hence there is a primitive vector \(a\in\mathbb Z_{>0}^{n+1}\)
such that \(q=P(a)\in B\). We may replace B by a smaller convex ball
about q with compact closure in the previously chosen B. We do not
require the originally given alpha to be rational or independent.

## 3. One blowup: global center, regularity and the cone formula

We use only the following explicit blowup operation. Suppose a current
model has a closed boundary stratum point with local boundary parameter
system \(x_0,\ldots,x_n\), represented combinatorially by a lattice basis
\(b_0,\ldots,b_n\). Here b_i records the orders of the ORIGINAL z_j
along the corresponding boundary divisor. Initially b_i is the standard
basis. Let J be a subset with at least two indices.

Blow up the connected component Z, through this point, of the closed
intersection \(\bigcap_{j\in J}\{x_j=0\}\). The reduced strict SNC
hypothesis makes that intersection regular; its components are disjoint
and closed. Thus Z is a genuine globally defined closed regular center,
not an open stratum with its boundary omitted. It is proper over k if it
is contained in the special fibre. Multiplying local equations by units
does not change its ideal.

On the chart indexed by j in J the coordinate substitution is

\[
 x_j=t,\qquad x_i=t y_i\ (i\in J\setminus\{j\}),
 \qquad x_i=y_i\ (i\notin J).                      \tag{3.1}
\]

Here is a direct check that these are the actual regular blowup charts,
without leaving a chart-torsion assumption implicit. Locally start with
the polynomial algebra A[y_i:i in J except j] and the equations
\(f_i=x_i-y_i x_j\). At every point over the center, put
\(\lambda_i=y_i\bmod\mathfrak m\) in its residue field. The linear
classes of the equations in the regular ambient cotangent space have
the independent components

\[
           [x_i]-\lambda_i[x_j]\quad(i\in J\setminus\{j\}).
\]

The independent original parameter classes [x_i] guarantee their
independence, including after residue-field extension. Their quotient
local ring is therefore regular. The class of x_j is independent of
these equations as well, so x_j is a regular parameter, in particular
a non-zero-divisor, in that quotient. Away from x_j=0 the equations
solve uniquely for all y_i. Thus the quotient has no x_j-torsion and
is exactly the subalgebra A[x_i/x_j] in the fraction field, the genuine
Rees blowup chart. No extra component on t=0 is retained.

The boundary components through a point of this chart are t=0, those
y_i=0 that pass through the point, and the old unselected boundary
parameters. Their cotangent classes are independent in the quotient:
the relations above eliminate the selected x_i, leaving precisely
these independent classes. This proves regularity and strict SNC at
every point over the center. Outside the center the blowup is the
identity. It also proves the assertion for a center of positive dimension,
by retaining the other local parameters. The completed-local toric
comparison in BFJ Theorem 3.15, Step 2, agrees with this calculation,
but its merely normal conclusion is not upgraded by terminology.

There is a closed boundary stratum point above the original one obtained
by setting all these new boundary coordinates to zero. It has the SAME
residue field as the original point; it is a coordinate point of the
exceptional projective space. Thus no splitting field is required to
continue the construction.

At this chosen point the new cone has basis

\[
 b_J=\sum_{i\in J}b_i,
 \quad b_i\ (i\ne j).                             \tag{3.2}
\]

The change of basis has determinant plus or minus one. In particular its
new rays are primitive, its cone is regular, and no lattice saturation
or hidden ramification factor occurs. The exceptional multiplicity is
\(N\cdot b_J=\sum_{i\in J}N\cdot b_i\).

If at least one selected divisor is vertical, Z is contained in the
special fibre. Its ideal contains a power of pi, so this is an admissible
vertical blowup and the generic-fibre map is an isomorphism. The resulting
scheme is integral (its blowup charts embed into the function field),
regular as just proved, and torsion-free over R, hence flat over the DVR.
Properness follows from properness of the blowup and the old model.

The analytic monomial points are unchanged by (3.1). Indeed, old parameter
monomials become the exact monomials specified by the matrix (3.2).
Applying weighted valuation to (3.1) gives precisely this linear map on
the normal weights. Here is the face case needed below in more detail.
After a sequence of these charts let y_0,...,y_n be the new boundary
parameters, and write the original z_i as their exact monomials. Let
J_+ be the set of new coordinates assigned positive weights, and J_0
the coordinates assigned zero weight. Suppose the resulting OLD weights
are all positive, as will hold for the whole final simplex.

Set y_j=0 for j in J_+ and work at the generic point of that coordinate
stratum. Each original z_i contains a positive-weight factor, so its
image is zero. The residue of the old local ring is therefore kappa(p).
The remaining coordinates y_j, j in J_0, are algebraically independent
residual coordinates over kappa(p). To check this last assertion rather
than assume it, complete the original local ring as in (2.1) and use
flat base change of the actual Rees charts. They are the corresponding
coordinate toric blowup charts over kappa(p). On the indicated stratum
all old parameters vanish, and the zero-weight coordinates are free
torus coordinates. Their ring is a localization of
\(\kappa(p)[y_j^{\pm1}:j\in J_0]\), with fraction field the indicated
rational function field. This description also describes the actual
fiber stratum: completion does not change the residue field at the
original closed point, and formation of that fiber commutes with this
base change. Localizing further in a tracked chart does not introduce
an algebraic relation among these residual coordinates.

For a finite sum of old monomials, group the transformed terms by their
exponents in J_+. Terms with a common such exponent have distinct
exponents in J_0 unless they were identical old monomials: the full
exponent matrix is unimodular. Their nonzero coefficients in kappa(p)
therefore form a NONZERO Laurent polynomial in the algebraically
independent residual variables. This is a nonzero element of the
stratum's residue function field and has valuation zero. There is no
unjustified cancellation of equal-weight old terms on a new face.

Finally, the infinite old power series cause no problem at these faces.
The OLD weights are bounded below by a positive constant on each compact
subset under discussion. Terms of sufficiently high old total degree
have uniformly arbitrarily large value, whether some new weights vanish
or not. Every calculation below a fixed value thus involves only the
finite sums just checked. It follows that the old weighted-series
valuation equals the new monomial valuation centered at the generic
point of the chosen stratum, on faces as well as interiors. This is an
equality of points of the unchanged generic fibre, not just a map of
abstract polyhedra. It is the explicit local form of BFJ's toric
completed-local compatibility in Step 2.

## 4. Extracting a prescribed primitive positive ray in finitely many steps

Track the fixed vector a in a current regular maximal cone. In its current
basis write

\[
       a=\sum_{i=0}^n a_i b_i,
       \qquad a_i\in\mathbb Z_{\geq0}.             \tag{4.1}
\]

This is true initially. If only one coefficient is positive, primitivity
of a and the basis property imply that coefficient is one. The desired
ray is then already present.

Otherwise put J={i:a_i>0}, choose j with
\(a_j=\min_{i\in J}a_i\), and perform the blowup (3.1) with this J and
this chart. In the new basis,

\[
 a=a_j b_J+\sum_{i\in J\setminus\{j\}}(a_i-a_j)b_i
                 +\sum_{i\notin J}a_i b_i.        \tag{4.2}
\]

All coefficients remain nonnegative integers. Their sum decreases by
\((|J|-1)a_j>0\). At least one of the divisors selected by J is vertical:
otherwise (4.1) would give N.a=0, contrary to a>0 and N!=0. Therefore
every operation is one of the vertical blowups authorized in Section 3.

The strictly decreasing positive integer sum proves termination. Zero
coefficients are harmless: we blow up only the positive support, keep
the other basis vectors, and continue in the indicated maximal chart.
At termination a itself is one of the primitive basis vectors of a
regular maximal cone. We have obtained an actual closed boundary stratum
point of a global proper regular SNC pair, whose cone has a basis

\[
                   a,b_1,\ldots,b_n.               \tag{4.3}
\]

All these vectors have nonnegative coordinates in the original cone.
The divisor E_a is vertical, with positive multiplicity M=N.a.

This extraction does not need a general regular subdivision theorem.
In particular, a possibly singular model from BFJ Theorem 3.15 is never
inserted and then incorrectly called SNC.

## 5. Shrinking a whole regular simplex toward the extracted ray

Fix i between 1 and n. Blow up the connected component of
\(E_a\cap D_{b_i}\) containing the tracked closed stratum point.
In the two-dimensional cone spanned by a and b_i, choose the chart
whose new cone retains a and replaces b_i by a+b_i. Repeating this
operation k_i times replaces b_i by

\[
                       b_i+k_i a.                  \tag{5.1}
\]

The other basis vectors are unchanged in this chosen chart. Each center
is vertical because it lies in E_a, including when D_{b_i} was originally
horizontal. The strict transform of E_a is the divisor with the retained
ray a; it is not being confused with the new exceptional divisor.
Perform these operations successively for i=1,...,n. The resulting regular
maximal cone has basis

\[
                  a,b_1+k_1a,\ldots,b_n+k_na.       \tag{5.2}
\]

Write M_i=N.b_i>=0. For k_i>=1, all its rays are vertical, since
\(N\cdot(b_i+k_i a)=M_i+k_iM>0\). Their normalized slice points satisfy

\[
 P(b_i+k_i a)=\frac{\ell(b_i+k_i a)}{M_i+k_iM}
                   \longrightarrow\frac{\ell a}{M}=q
       \quad(k_i\longrightarrow\infty).           \tag{5.3}
\]

This limit is also valid when M_i=0. Choose each finite k_i large enough
that the displayed point lies in the small convex ball B from Section 2.
The slice of the cone (5.2) is exactly

\[
 \tau=\operatorname{Conv}\{P(a),P(b_1+k_1a),\ldots,
                                      P(b_n+k_na)\}.\tag{5.4}
\]

To check the slice formula, write a cone vector as a nonnegative sum of
the basis vectors and multiply its coefficients by their positive
N-values divided by ell. On the slice N.x=ell those new coefficients
sum to one. Conversely every convex combination gives a slice vector.
The n+1 vertices are affinely independent because the vectors (5.2)
are a linear basis. Thus tau is a genuine n-simplex, not a collapsed
configuration. Convexity gives tau contained in B, hence in V and in
iota^{-1}(W).

Moreover every generator in (5.2) has strictly positive ORIGINAL
coordinates: a does, and each b_i+k_i a does. Every point of tau
therefore lies in the interior of the original full-dimensional cell,
even its vertices and proper faces. Section 3 identifies all its
monomial points with the original points iota(tau). This proves the
whole closed-simplex assertion, not only the convergence of a sequence
of abstract vertices.

## 6. The actual proper residual curve and independent normal weights

Let p' be the tracked closed point with n+1 vertical boundary components
corresponding to (5.2). Omit any one of these components and take the
connected component C through p' of the closed intersection of the
remaining n components. It is nonempty and regular of codimension n in
the (n+1)-dimensional model, hence a regular integral curve. It is closed
in the proper special fibre, so it is proper over k. A regular finite-type
scheme over the perfect field k is smooth. Its connected component is
integral because the irreducible components of a regular scheme are
disjoint. This proves all the required assertions about C without
assuming it has a k-rational point or is geometrically connected.

The relative interior of the corresponding (n-1)-face F consists of
monomial valuations centered at eta_C, by the explicit coordinate-face
calculation in Section 3. Since all vectors of F have strictly positive
old coordinates, their center on the old model is p. In particular the
image of eta_C is p. The entire irreducible C maps to p: the image of
any point of C specializes the image of its generic point, and p is
closed. No open portion of C is substituted for this whole curve.

Let m_1,...,m_n be the positive multiplicities of these n vertical
components. The weights beta in the face interior are exactly

\[
 \beta_j>0,\qquad\sum_{j=1}^n m_j\beta_j=\ell.     \tag{6.1}
\]

For each nonzero q in \(\mathbb Q^n\), the homogeneous hyperplane
q.beta=0 does not contain the affine hyperplane in (6.1). Otherwise its
normal would be proportional to m, but q.beta would be a nonzero
constant on (6.1), a contradiction. Its intersection with the face
interior is therefore closed and nowhere dense. By Baire's theorem,
the complement of the countable union of these hyperplanes is dense
in the relative interior. These are precisely the Q-linearly independent
normal weights. Choose one. Its point eta belongs to iota(F), hence to W,
and has the exact proper-curve geometry and normal independence required
in the separately gated outer-collar statement.

This last observation is a geometric interface only. It is not an
application or independent verification of the outer-collar current
theorem, L, P, Q, V or the source representation R.

## 7. Explicit horizontal-to-vertical example and multiplicities

Take \(\mathcal X=\mathbb P^2_R\), with horizontal coordinate lines
H_1 and H_2 meeting at a closed point p of the special fibre E_0.
On an affine chart the full boundary parameters are pi,x,y, and
N=(1,0,0). The positive cell has coordinates (ell,a,b), a,b>0.

The primitive vector a_0=(1,1,1) is extracted by blowing up the closed
stratum p. In the pi-chart its regular cone has basis a_0,e_1,e_2.
Its new exceptional divisor has multiplicity one. Apply Section 5 m
times to each of the two other generators, retaining a_0. The resulting
three primitive vectors and their multiplicities are

\[
 a_0,\ e_1+m a_0,\ e_2+m a_0;
                 \qquad 1,m,m.                    \tag{7.1}
\]

The normalized vertices are

\[
 (\ell,\ell,\ell),\quad
 (\ell,\ell+\ell/m,\ell),\quad
 (\ell,\ell,\ell+\ell/m).                         \tag{7.2}
\]

Their triangle contracts toward the first point as m grows, while it
remains two-dimensional for every finite m. All three normal divisors
are vertical. The face opposite the first vertex has positive normal
weights beta_1,beta_2 with
\(m(\beta_1+\beta_2)=\ell\); an irrational ratio makes them
Q-linearly independent. Its original coordinates are
\((\ell,\ell+\beta_1,\ell+\beta_2)\).

This example also shows why demanding a reduced semistable output would
invalidate the construction: m may be greater than one, and there is
no permission to replace these multiplicities by one. The argument uses
the slice N.x=ell, not an unweighted barycentric subdivision or a
primitive-metric length formula.

## 8. What this establishes, and the remaining barriers

The ordinary-topology consequence is precise: W intersects the original
model cell in a relative open neighbourhood, and we construct a complete
new all-vertical simplex INSIDE that intersection. Thus W meets a proper
residual-curve wall at an independent-normal point on the same original
analytic space. No ordinary full inverse image is asserted to lie in W
by this construction alone. That stronger all-source containment is the
separate purpose of the outer-collar candidate.

For a proposed source-cell application, let S be a specified source set.
If S contains a relative open neighbourhood of xi IN THIS model cell,
choose V inside that neighbourhood. The conclusion then puts tau and
its wall in S intersect W. Equality with, or such local containment in,
an arbitrary moment's source cell is a separate model-capture hypothesis.
The theorem does not manufacture it from equality of dimensions, density
of divisorial points, a shared target, or faithful tropicalization.

There is also a useful obstruction to an overly strong variant. If the
n+1 original weights of xi are Q-linearly independent, no toroidal
subdivision can put xi on an (n-1)-face. Such a face has only n positive
normal coordinates; all the original weights are integer linear
combinations of those coordinates under the monomial charts. Their
Q-rank would then be at most n. Consequently the theorem must allow a
NEARBY wall point instead of a wall through xi. A single finite
subdivision has only finitely many codimension-one faces in the original
cell, and they cannot be dense in an open n-cell. The model is allowed
to depend on the neighbourhood.

No arbitrary-model existence theorem has been used. No algebraic closure,
ramified extension, alteration, or generic-fibre modification has occurred.
The construction changes the model, but its generic-fibre isomorphism is
the identity. It introduces no pullback operation on currents.

The local blowup algebra and lattice algorithms themselves are not
characteristic-zero phenomena. Nevertheless this packet's full analytic
statement is restricted explicitly to residue characteristic zero, where
the original-field Cohen/monomial interface has been written and checked
against BFJ. GRW's algebraically closed, strictly semistable setting is
not used to bridge a mixed-characteristic or nonreduced original-field
gap. Extending the full statement to that wider setting is not claimed
here, nor is a counterexample to such an extension claimed.

Finally, this result does not establish source representation, comparison
of arbitrary chart coefficients, whole-current rigidity, or P21.3. It
addresses one geometric accessibility step after an actual SNC model
cell has already been supplied. Independent and production gates remain.
