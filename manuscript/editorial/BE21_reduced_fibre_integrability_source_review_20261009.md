# Reduced fibres and logarithmic integrability: exact model and approximation interfaces

Date: 9 October 2026. Controlling source: Boucksom--Eriksson,
*Spaces of norms, determinant of cohomology and Fekete points in
non-Archimedean geometry*, Advances in Mathematics 378 (2021), 107501.
The cached published PDF has 125 physical pages, including the cover.

This checkpoint freshly reads physical pages 39--47, 63--64 and 72--78:
eighteen complete pages in nine individually displayed matching images,
with sequential notes and receipts. Three overlap the two preceding
checkpoints, whose union had 38 pages. The three related checkpoints
therefore contain 53 distinct pages, with 72 unread in that combined
scope. This is not a whole-paper claim. The earlier note that Theorem
7.14 needed separate verification refers to the current load-bearing
audit; pages 63--64 had already been displayed in the earlier checkpoint
and are freshly reviewed here. Historical notes remain frozen.

## Models, completion and reduced special fibre

Section 4 uses separated flat finite-type valuation-ring models. They
need not have regular total space, unlike the model-Chow category in
L.97. Proper domination preserves the reduction tube; a proper model
has tube equal to the whole analytification. Generic properness alone
does not make every chosen model proper.

The original algebra can map noninjectively to its completed affinoid
algebra. For a discretely valued field, the flat finite-type model
$A=K^\circ[1/\pi]=K$ has zero $\pi$-adic completion and empty tube:
$\pi^{-1}$ cannot have absolute value at most one. Its generic fibre is
a proper point, but the model is not proper. A tube sup-seminorm or
original lattice gauge is consequently not always a norm on the
original algebra.

Theorem 4.15 identifies the sup-seminorm unit ball with relative integral
closure. Lemma 4.17 descends algebra membership from completion, while
Lemma 4.18 attains the completed gauge through strict closedness of a
Tate ideal. These invoke explicit BGR affinoid foundations.

Theorem 4.19, physical page 46, equates reduced special fibre with
sup/gauge equality and implies relative integral closure. The reverse
implication from relative integral closure additionally requires a
dense value group. For the discrete model

$$
R=\mathbf Q[[\pi]],\qquad B=\mathbf Q[[z]],\qquad \pi=z^2,
$$

the total space is a normal regular DVR, but
$B/\pi B=\mathbf Q[z]/(z^2)$ is not reduced. With $|\pi|=1/2$ the
section $z$ has analytic norm $2^{-1/2}$ and lattice gauge one in the
basis $1,z$. The gauge of $z^2=\pi$ is $1/2$, so this gauge is not
power-multiplicative. This does not contradict tame scalar-extension
descent: lattice/sup comparison is a different assertion.

Theorem 4.20, physical page 47, assumes a nontrivially valued field
that is discrete or algebraically closed and a reduced generic scheme.
Relative integral closure is finite; reduced special fibre is
additionally asserted in the algebraically closed case. The proof uses
excellence or Grauert--Remmert finiteness. In the descent of finite
generators, one can approximate completed coefficients, use the included
generator one, and apply Lemma 4.17 to the remainder. These steps do not
give a finite-normalization theorem over every densely valued field.

## A concrete completed-residue-field boundary

Remark 4.21 explicitly warns of nonfiniteness for a dense, nondivisible
value group. Its boundary can be illustrated by the same type of field
that occurs in L.96. Let $H$ be the completed Gauss residue field over
$\mathbf Q((\pi))$ with $v(\pi)=1$ and $v(T)=\sqrt2$. Then

$$
\Gamma_H=\mathbf Z+\sqrt2\,\mathbf Z,\qquad \tfrac12\notin\Gamma_H.
$$

Completion preserves values of nonzero elements. The group is dense.
The exclusion of $1/2$ is exact: an equality
$m+n\sqrt2=1/2$ would give $(2m-1)^2=8n^2$, impossible modulo two.

Set $L=H(z)$ with $z^2=\pi$. This is a separable degree-two extension
and $v(z)=1/2$. The finite free model
$A=H^\circ[z]/(z^2-\pi)$ has reduced generic fibre. Its relative
integral closure in $L$ is $L^\circ$: completeness gives a unique
extension of the valuation; conjugates of an element of nonnegative
valuation have nonnegative valuation, so its monic polynomial has
coefficients in $H^\circ$. Conversely, a monic integral equation
cannot hold for an element of negative valuation.

For $a,b\in H$, the two nonzero term values lie in disjoint cosets, so

$$
v(a+bz)=\min\{v(a),v(b)+\tfrac12\},\qquad
L^\circ=H^\circ\oplus Iz,\qquad
I=\{b\in H:v(b)>-\tfrac12\}.
$$

The ideal $I$ has no least value. A finitely generated fractional ideal
over a valuation ring is principal and has a least value. Thus $I$,
and hence $L^\circ$, is not finite over $H^\circ$ or $A$. The exact
diagnostics include Pell values approaching the open cut from above.
This is a worked instance of the source's stated boundary, without a
new general theorem or priority claim. It does not contradict Theorem
4.20 or the global norm estimate: those use the stated field hypotheses
or pass to an algebraically closed extension.

## Global regularizable measures and the printed CLN sign

Theorem 8.4, physical pages 72--74, extends smooth semipositive curvature
products under uniform approximation to continuous psh-regularizable
metrics. Proposition 8.5 preserves positivity, algebraic total mass,
scheme component multiplicities and symmetry. The dpsh extension is a
signed multilinear extension of differences of those metrics.

The printed Lemma 8.6 expands $dd^c(\phi_0-\phi'_0)$ using a plus
between two integrals. It must be a minus. Taking $\phi_0=\phi'_0$
with degree-one positive curvature and $\phi_1-\phi'_1=1$ makes the
correct integral zero and the printed plus expression two. The final
absolute-value estimate remains valid by the triangle inequality and
the two positive masses. Its constant depends on fixed line bundles,
not on an unbounded test function chosen independently of such a
global difference representation.

Neither this construction nor R-PL density certifies arbitrary local
weak-psh products, every smooth non-Archimedean metric being globally
dpsh, or the book's separate density problem.

## The logarithmic integrability proof and its supported reformulation

Theorem 8.12, physical pages 75--76, assumes a projective scheme,
continuous psh-regularizable metrics $\phi_1,\ldots,\phi_n$ and a
regular line-bundle section $s$. Its logarithmic norm for any continuous
metric is integrable against their mixed measure, and the integral
depends continuously on the metrics in the uniform topology.

The displayed Lemma 8.13 uses ordinary logarithms of sums of real
squares and asserts smoothness in both field settings. In the
non-Archimedean CLD definition of Section 4.2 this is false. On
$\mathbf P^1$, the displayed weight for $A'=\mathcal O(1)$ is
$\frac12\log(1+|T|^2)$ near the rational point zero. Every CLD-smooth
function is locally constant there: it depends on finitely many
logarithms of analytic units, whose absolute values are locally
constant by the ultrametric inequality. The displayed weight is zero
at zero and positive at $T=\pi^k$ for every $k$. Its failure of
smoothness does not refute the Archimedean construction or the intended
integrability theorem.

A reformulation of the proof uses existing attributed inputs, without
the printed smoothness assertion:

1. Choose very ample $A'$ and $A=L+A'$. Take Fubini--Study metrics
   $\psi'$ on $A'$ and $\theta$ on $A$. The continuous metrics

   $$
   \psi_j=\max\{\log|s|+\psi',\,\theta-j\}
   $$

   on $A$ are Fubini--Study: their generators are the products of $s$
   with the chosen $A'$ sections and the $A$ generators with shifted
   weights. They decrease pointwise to $\log|s|+\psi'$. Example 7.12
   and Theorem 7.14, freshly read on pages 63--64, give their
   psh-regularizability using a regularized maximum. A uniform smooth
   approximation can be made decreasing through a fast subsequence and
   descending constants. No arbitrary uniform sequence is presumed
   monotone.
2. Choose the reference metric $\phi_{\rm ref}=\theta-\psi'$.
   Then $f_j=\psi_j-\theta$ decreases to $\log|s|_{\phi_{\rm ref}}$.
   Both metrics on $A$ used in the CLN estimate are explicitly
   psh-regularizable and semipositive in that sense. Merely saying the
   reference metric is smooth dpsh would not establish this premise.
   The smooth CLN estimate extends to these continuous metrics by
   uniform approximation and fixed finite curvature mass.
3. Fix one smooth semipositive tuple on the $L_i$, available from the
   assumed regularizations. Local smooth logarithmic integrability is
   the attributed CLD input. The reference metric differs from a
   smooth metric by a bounded continuous function, so this tuple has
   a finite logarithmic integral.
4. The fixed-bundle CLN bound compares every $f_j$ integral to this
   finite anchor with a bound independent of $j$. Since $f_j$ is
   decreasing and bounded above, monotone convergence shows that all
   limiting logarithmic integrals are finite. This uses inequalities
   with finite anchors and never subtracts two infinite values.
   Taking limits gives the uniform-continuity estimate for the
   reference metric. Changing to any continuous metric adds a bounded
   continuous function, whose integral is continuous by Theorem 8.4.

This is an explanatory repair of an attributed existing theorem within
its exact hypotheses. It invokes the stated smooth-maximum, measure
extension and local logarithmic-integrability foundations; it is not
recursive certification of all of CLD. No original general result or
independent-model receipt is asserted.

The regular-section condition matters. On a disjoint union of two
projective lines, the section $(0,X_1)$ of $\mathcal O(1)$ on each
component is globally nonzero but is a zero divisor. Its logarithm is
minus infinity on a component of positive curvature mass. This is
outside Theorem 8.12, whose “regular” section is not merely “nonzero.”

## Poincare--Lelong, Deligne pairings and remaining comparisons

Theorem 8.14, physical pages 76--77, retains the regular section,
continuous dpsh factors and the divisor-minus-curvature sign.
Uniform logarithmic-integral continuity is essential in its limiting
step; weak convergence alone does not control an unbounded logarithm.
Its printed approximation variables should read $f=\tau-\tau'$ and
$\tau'_j\to\tau'$. The Deligne restriction and change-of-metric formulas
on page 78 retain the minus-log metric convention and the dimension-zero
algebraic norm.

BGR affinoid theorems, Berkovich/formal reduction, CLD Stokes and local
logarithmic integration, and classical projective/intersection machinery
remain explicit attributed inputs. This partial reading does not
recursively certify all of them.

These global statements do not establish affine lower-growth
regularization, arbitrary local weak-psh descent, a Chow-to-CLD comparison
map or a general critical homogeneous Siu/envelope bridge. The BJ22
Theorem 6.21 warning remains binding; general Siu/envelopes remain OPEN
and LPWZ density UNVERIFIED. All 42 atoms/twelve formal problems,
the 4,657-page active book and native catalogue/editor remain unchanged
in this source checkpoint. The last complete ordered book pass remains
4 October.
