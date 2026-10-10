# Reboulet asymptotic Fubini–Study source audit, 9 October 2026

The complete pinned [arXiv:2004.11635v1](https://arxiv.org/pdf/2004.11635v1)
has been read in physical-page order: all 43 pages, including both bibliography
pages, in 22 individual matching rendered displays. Complete selected text was
read for each display, followed by a sequential authored note and immutable
observation receipt. The PDF has 406,498 bytes and SHA256
`65492773fa4237bdde7320da8b594255ddd6d36820293fda2037d858006dae79`.
The arXiv version was submitted on 24 April 2020; the title page is dated
27 April 2020. This is a foundational dependency review, not a new 2026 paper
or a new whole-book reading pass.

The review finds useful finite-dimensional, graded and FS interfaces, but
does **not** accept this v1 as an independently complete proof of its general
Theorems A–C. Several printed formulas have straightforward repairs; several
arguments also need substantive scope and dependency checks. No intended
correctly formulated general theorem is declared false. Thirteen exact
elementary diagnostic families accompany the page notes; 5,376 rational
polynomial product checks supplement the explicitly supplied general product
argument in the final worked example. This ordinary audit promotes no new
general theorem and contains no independent-model verification receipt.

## Ambient category and finite-dimensional normalization

The standing variety convention is geometrically integral and separated of
finite type over a complete non-Archimedean field. Main projective ample
polarizations must be retained when a later section briefly writes semiample.
The continuous/global FS psh class uses decreasing nets. It cannot be
identified with every local CLD current or smooth-regularizable class.

On a nonzero d-dimensional space, the spectral probability measure is
`d^(-1) sum delta_lambda`, with lambda the logarithm of primed over unprimed
norm. The signed mean is relative volume. The absolute first moment is d1;
the supremum of absolute logarithmic ratios is d-infinity. The literal
formulas in Definition 1.4.4 (physical 12) lose absolute values in two places.
For opposite weights -1,1 the signed mean is zero and d1 is one. The minmax
in 1.4.1 orders the spectrum decreasingly, whereas Remark 1.4.2's basis
ordering is increasing. The multiset survives this indexing mismatch.
Remark 1.4.5's second two-sided bound needs the primed norm on its right.

Proposition 1.4.10 (physical 13) correctly distinguishes diagonal norm density
from lattice norm density. The latter needs a dense value group. Over a
discrete value group, the lattice norms are discrete and closed. A
one-dimensional logarithmic weight halfway between consecutive values stays
a positive distance from every lattice norm. The introductory unqualified
lattice-density sentence (physical 6) therefore cannot be quoted verbatim.

Quotient contraction 3.3.6 and the degree-one equality 3.3.7 (physical 24)
follow from two-sided bounds on every lift and tensor-product bounds. Their
proofs do not require exact attainment of an infimum. The first displayed
upper comparison in 3.3.6 needs the primed quotient norm. For a genuinely
quotient-generated norm, FS in every degree equals degree-one FS: products
give one inequality and evaluation of arbitrary tensor lifts gives the other.
This is a direct formal consequence, with the operator domain explicit.

## Graded scaling and semigroup hypotheses

Boundedness should be stated as eventual `d_infinity=O(m)` relative to a
fixed model or metric reference, or explicitly two-sided `exp(+-Cm)` norm
comparison. Definition 3.1.4 prints a finite limit, whose existence is not
established merely by that comparison; finite limsup is sufficient for the
growth arguments. The graded scalar shift by c means multiplying degree m
by `exp(-cm)`, not by a degree-independent scalar.

The spectral measures rescale each logarithmic weight by its **original**
degree. Their weak limit has uniformly bounded support only with the
appropriate boundedness and admissible-semigroup hypotheses. Its first
absolute moment is the graded d1 semidistance, while its first signed moment
is volume. Zero d1 need not mean `d_infinity=o(m)`. The paper's other graded
d-infinity is a supremum over all positive degrees, hence retains low-degree
differences and is not a limiting spectral supremum.

Restriction to `R(X,kL)` changes its degree r to original degree kr. Under
genuine regrading, logarithmic means, energies normalized by polarization
volume, and d1 scale by k. Proposition 3.3.5 (physical 23) itself states this
scaling. Theorems C/4.5.4 and Proposition 4.5.3 (physical 33–34) subsequently
mix original-degree semigroups with regraded weights. On a point,
`zeta_m=exp(-cm)` has signed volume c against the trivial norm. Generation by
`zeta_k` on kL gives volume kc. Any intended approximation statement needs
`k^(-1) vol_(kL)` or an explicit original-degree convention throughout.

Semiample alone does not imply that the section-ring Proj recovers X, nor
that its Okounkov body has full-dimensional interior. For `X=P1,L=O`, the
section ring is `K[t]`, generated in degree one, but its Proj is a point and
its valuation semigroup is `(m,0)`. The constructions on physical 25–28
therefore need their ample/big/admissible scope restored. Eventual model
section comparison over a dense non-Noetherian valuation ring is cited to
Hartshorne Exercise II.5.14; an applicable finite-presentation/descent or
non-Noetherian cohomology argument remains a dependency. This review has
not refuted the appropriately ample construction.

The body on physical 27 is the closed cone's **intersection** with the
degree-one plane; the printed union is unbounded. The group generated is
`Z^(d+1)`, and the containing monoid's generators, rather than the entire
monoid, lie in the degree-one plane. Degree indices n,m,k and strict
remainder inequalities in the Taylor expansions need consistent typing.

The local coefficient estimate (physical 29–30) uses the supremum or Gauss
seminorm on a smaller closed polydisc. The printed positive lower bound
pointwise fails already for `f=z` at zero. A leading coefficient one gives
`sup |f| >= r^|alpha|`; bounded frame weights and linear valuation growth
then give the intended logarithmic estimate. A limiting distortion constant
D must be replaced by D+epsilon for eventual inequalities if needed.

The probability measure in Theorem 4.5.1 (physical 32) needs division by the
number of valuation leaves; the finite moment sum on physical 34 needs the
same division by `h0(mL)`. Bare superadditivity does not imply compactly
supported convergence: `Phi(n,alpha)=n^2` gives Dirac masses escaping to
infinity. Threshold semigroup inclusion decreases as the threshold increases,
opposite Remark 4.4.2. The claimed closed-tail identity at every threshold,
including the endpoint, needs qualification: `Phi(n,alpha)=n-sqrt(n)` is
superadditive with normalized values approaching 1 from below. Its limit
is `delta_1`, yet the threshold semigroup at 1 has no positive-degree points.
Continuity-point or almost-everywhere tail statements suffice for appropriate
moment arguments; unrestricted all-point statements cannot be inferred
merely from weak convergence.

The monotonicity in 4.5.3 is divisibility monotonicity, not consecutive
monotonicity. On a point, `Phi(m)=floor(m/2)` is superadditive, but its
normalized values at 1,2,3 are 0,1/2,1/3. Factorial subsequences do not by
themselves prove all-degree convergence. The external Chen–Maclean and
Boucksom semigroup theorems must be checked before importing the corrected
Fujita approximation beyond these elementary diagnostics.

## Energy, envelope and valuation interfaces

The defining normalized energy of two constant-shift metrics is their
constant difference. Proposition 2.3.4 (physical 18) prints the opposite
cocycle orientation: shifts (1,0,0) give left side 1 and right side -1.
The correct cocycle is `E(phi,psi)=E(phi,tau)+E(tau,psi)`. The positive-volume
Hilbert conversion on physical 36 also needs
`h0(mL) ~ vol(L) m^n/n!`. The division by polarization volume then correctly
matches the normalized determinant mean if the factorial is retained.

The exact FS pullback in Lemma 5.1.2 (physical 35) uses the pullback of a
function, not its printed pushforward, and is a different input from
asymptotic metric-induced supnorm extension. The controlling published
BE21 Proposition 7.20 was directly reviewed in the previous global checkpoint.
Mixed MA pushforward then compares the energy integrals. Earlier model norm,
CLD and BE20 model-energy foundations remain attributed dependencies, not
recursively certified by this reading.

The arbitrary graded-norm proof on physical 37 calls its FS potentials
decreasing nets. The floor(m/2) example disproves that claimed monotonicity;
along divisibility the product inequality has the increasing direction.
One cannot apply decreasing energy continuity to those values. A corrected
route would use the normalized generated-norm identities and a correctly
proved normalized volume approximation, without falsely invoking decreasing
regularization. That reconstruction is not a verified general theorem here.

Continuity of envelopes is explicitly a hypothesis for the usc FS supremum
to be global psh (5.2.5, physical 38), and for Theorem A/5.4.1 (physical 39).
The historical examples on physical 38 are not an exhaustive current
state-of-the-art statement. The book's exact projective, positivity,
field-of-definition and resolution-dimensional conditions control those
citations. No general envelope theorem or BJ22 repair has been obtained.

Definition 5.3.1 (physical 38) uses divisors on K-birational models of X.
Their orders vanish on `K*`; they do not extend the prescribed nontrivial
ground absolute value. For example over Q5, their induced absolute value
of 5 is 1, whereas a Berkovich point must give 1/5. Hence its claimed dense
`Xdiv` is not a set of analytic points in the stated nontrivial-ground scope.
A correctly typed family of analytic model valuations and the relevant
determination/regularization lemma require separate justification. Merely
substituting the word “vertical” is insufficient over every value group.
The trivial-field BJ18a lemma and BJ18b Corollary 6.28 do not acquire a
nontrivial-ground scope from a bare assertion that they extend.

Asymptotic FS includes usc regularization. Consequently its supnorm identity
is `FS(N(phi))=Q(phi)^usc`, not necessarily unregularized Q. The proof on
physical 40–41 drops this distinction. Lemma 5.4.2 also switches the ordered
norm inequality and signed-volume orientation; the zero condition survives
a sign correction, but the full ordered energy argument still needs the
applicable strictness result. Pointwise maximum of norms corresponds to
minimum of metric obstacles: `N(min(phi,psi))=max(N(phi),N(psi))`.
Pointwise minimum of arbitrary norms can fail ultrametricity, as the
two-dimensional weights (1/2,1) and (1,1/2) show.

## Concrete bounded FS example for the quotient and usc distinction

This is an explanatory worked instance of the source's already stated
distinction between d1 and rescaled operator distance (3.2.2, citing BJ18a
Remark 3.8), not a new general theorem. On `P1_Q5` with `L=O(1)`, give the
degree-m monomial basis `X0^(m-i)X1^i` weights `(2^m,1,...,1)`. The resulting
diagonal norm is submultiplicative: the ordinary Gauss norm of a product
is bounded by the product of the Gauss norms, and the separately penalized
constant coefficient is multiplicative. Both are bounded by the product
of the displayed norms. Its logarithmic distortion from the standard
Gauss norm is exactly `m log 2`, hence it is a bounded graded norm.

Against the standard graded norm the rescaled spectral probability is
`(delta_(-log 2)+m delta_0)/(m+1)`. Thus asymptotic d1 is zero, while
rescaled d-infinity is `log 2` in every degree. On the chart `T=X1/X0`,
the degree-m FS weight is
`max(-log 2, (log|T|)/m)` for `|T|<=1`, and `log|T|` for `|T|>=1`.
These global FS metrics increase. Their raw limit equals the standard FS
weight away from T=0 and equals `-log 2` at T=0. Small-radius Gauss points
approach T=0, so that raw limit is not usc; its usc regularization is the
standard FS metric. The raw obstacle is bounded relative to standard FS,
and its Q is precisely this raw limit because all the displayed FS metrics
are admissible minorants and their supremum equals the obstacle. Hence
even this elementary bounded obstacle requires distinguishing Q from Q-star.
No envelope-continuity hypothesis or new bijection is used in the computation.

## Disposition and next integration

All 22 note/receipt pairs, immutable acquisition and preparation records,
full source pin, and exact diagnostics are retained. Preparation, export and
upload each add zero reading credit. Owned notes/records/helpers are prepared
for the private work branch; external primary PDF, extracted text and images
remain in the separately pinned cloud evidence archive. Remote publication
receives a later byte/blob verification receipt.

The 4,659-page active book, all 425 core TeX inputs, bibliographies and native
86-page open-problem catalogue are unchanged during this source checkpoint.
There are still 42 canonical atoms and 12 formal problems. General BJ22
critical homogeneous Siu and envelope bridges remain OPEN; LPWZ density
remains UNVERIFIED; the user's warning about the BJ22 Theorem 6.21 proof is
binding. No main-branch merge, general theorem promotion, independent-model
receipt, or second full-book pass is claimed.

Next, integrate only qualified finite/graded normalization and bounded FS
explanations through an isolated staged book, full build and actual rendered
seam review. Check the primary Chen–Maclean proof and correctly typed
nontrivial-field uniqueness input before any stronger correspondence claim.
