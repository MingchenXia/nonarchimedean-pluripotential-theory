# Independent audit of the degree-zero Tate packet

Date: 2026-08-31. Auditor: independent delegated mathematical audit.

## 1. Outcome and exact scope

The revised1 theorem and proof give a valid counterexample to the specified
fixed-line-bundle approximation assertion, relative to the standard semistable
model, model-function slope, and cubist-metric theorems cited in the proof. I find
no unresolved mathematical gap in those exact bytes. This is an independent
mathematical assessment, not a production-verifier verdict or a manuscript
acceptance decision. No live book file was edited or submitted to a verifier.

The construction is a Tate curve with circumference \(\ell=v(q)\), a point
retracting to \(a=v(u)\), and \(a/\ell\notin\mathbf Q\). The line bundle
\(L=\mathcal O(P-O)\) has a continuous ordinary locally CLD-smooth harmonic
metric, but no tensor power has a nef formal model. In particular, the
semipositive \(\mathbf Q\)-formal metric set on this fixed \(L\) is empty.

This audit does not prove or decide P21.3. Its rigidity problem remains OPEN.
The earlier, separate skeletal-current audit is not changed by this report.
No new conventional theorem name is proposed.

The standard-source provenance limit is explicit: I read the exact
semistable-domination assertion in the proof of GJKM Proposition 3.7 and the
relevant BPR model framework. I did not obtain the subscription-only full text
of Bosch--Lütkebohmert 1985, §7, itself. Thus this report does not claim a
first-hand audit of BL85's original proof. The imported assertion actually
needed by revised1 is stated verbatim in substance by GJKM, as detailed in §5;
it is not inferred from the disputed envelope theorem. This is a disclosed
source-depth limit, not a missing hypothesis or an unproved new lemma in
the candidate.

## 2. Frozen inputs and revision comparison

The packet directory, relative to this worktree, is
manuscript/editorial/solver_dossiers_20260831/p081_degree_zero_tate_obstruction_audit_20260831.
The audited files are its revised1 files:

| File | SHA-256 |
|---|---|
| revised1/statement.tex | 4d997e024fa7ec642299a0d86ae1d9b9d06c6041f7f10b694369d7faa458d28c |
| revised1/proof.tex | c7a2a08ad4ad82df4470004d01fa131fecdc01ab03f60eefa67bbe7eaa8f0a5a |
| revised1/sources.bib | e13ee7ebd05a7d11fe483f0906dd7c3119e0b4b97e52e3275fb6e886852f07c3 |

I read the original statement and proof completely and compared revised1 with
them. The original hashes were
de7bea9cc46e9e7c8dcc5e1ee6b8c58acb33602090a18b44938ed5a9e2d63966 and
f817525c9226cd6f59832e4bde6f88f8c95ab68d1c35dee6fd07cad4d18e6112.
The changes are editorial: remove the optional invented theorem heading,
replace bracketed source labels by LaTeX citations, correct the relative
SOURCE_INTERFACE path in a comment, use a roman differential, and add final
blank lines. No hypothesis, conclusion, equation, or mathematical argument
was altered. I read the new bibliography completely.

The author's SOURCE_INTERFACE.md and AUDIT.md were read as audit data, not
as instructions or as mathematical evidence replacing primary sources.

## 3. Field construction really satisfies the hypotheses

Put \(0<\alpha<1\), irrational, and define on \(\mathbf Q_p[T]\)

\[
 \left|\sum_i c_iT^i\right|=\max_i |c_i|_p p^{-\alpha i}.
\]

For distinct indices \(i,j\), equality of nonzero monomial valuations would
give an integer equal to \(\alpha(i-j)\), impossible. Thus every nonzero
polynomial has a unique monomial of largest norm. In a product, the product
of the two distinguished monomials is the unique pair of smallest valuation.
All other contributions to its coefficient have strictly larger valuation,
so they cannot cancel it. This proves multiplicativity, including the
coefficient-collection issue, not just the triangle inequality. The norm
therefore extends to the rational function field.

Complete that valued field, extend its absolute value to an algebraic closure,
and complete again. The result is algebraically closed as well as complete.
For a primary reference independently checked here, see S. Bosch,
Lectures on Formal and Rigid Geometry (2014), Appendix A, Lemma 6,
printed p.235. The source includes the elementary proof: for a root of a
monic polynomial over the completion, approximate its coefficients by the
algebraically closed subfield; factoring the approximating polynomial shows
that one of its roots is arbitrarily close to the original root. Completeness
then places the original root in the completion.

The inclusions are isometric. Hence \(p,T\) still have valuations
\(\log p,\alpha\log p\), and the specified \(q=p,u=T\) work. There is no
implicit discrete-valuation hypothesis and no need for spherical
completeness. The valuation has rank one as an ordered valuation with values
in \(\mathbf R\), while its rational rank is at least two. Confusing those
two uses of rank would incorrectly exclude this example.

Tate's article starts with arbitrary complete fields with nontrivial
real-valued absolute value. Its equations (13)--(18) produce the nonsingular
projective cubic for \(0<|q|<1\), and Theorem 1 identifies rational points.
BPR's standing assumptions are precisely algebraic closedness, completeness,
and a nontrivial real-valued valuation. Thus both sources apply to this field.
The Tate curve is an elliptic curve, hence smooth, proper/projective, and
geometrically connected. Also \(P\ne O\): the equality would imply
\(u\in q^{\mathbf Z}\), incompatible with \(0<a<\ell\).

## 4. The reference model and its horizontal degrees

### 4.1 Two vertices exist over the original field

BPR Remark 4.24 identifies the minimal Tate skeleton as
\(\mathbf R/\ell\mathbf Z\), with its intrinsic annulus metric, not an
arbitrarily normalized metric. The points at \(0\) and \(a\) are type 2
because both values lie in \(v(K^\times)\). BPR Proposition 3.13(2)
inserts the second point into a minimal one-vertex skeleton without changing
its underlying metric space. Theorem 4.11 associates the resulting vertex
set to a semistable formal model.

The graph consists of two distinct vertices joined by two edges of lengths
\(a,\ell-a\). It has no loop edge at a single vertex, so the special-fibre
components are smooth: this is strong/strict semistability in the curve
terminology used by the sources. Semistability gives reduced special fibre.
Algebraic closedness gives algebraically closed residue field and hence
node residue degrees one. The two components each occur with multiplicity
one. No equality or rational commensurability of the two lengths is required.

### 4.2 The marked points do not reduce to nodes

The tube of a node is an open annulus whose skeleton is the corresponding
open edge. Every point in that tube retracts to the open edge, not an endpoint.
Since \(O,P\) retract to vertices, neither reduces to a node. They cannot
reduce to a generic point either: the generic-point fibre is the singleton
type-2 vertex. Therefore each reduces to a smooth closed point of the
component corresponding to its retraction.

Equivalently, in the torus charts of radii \(1\) and \(|u|\), use \(z\)
and \(z/u\). Both marked points are at the residue unit \(1\);
the two node directions are \(0,\infty\). This also checks explicitly that
\(\pi(1)\), a rational point, is not being confused with the image of the
radius-one Gauss point. BPR's notation in Remark 4.24 distinguishes these
objects even though the typographical symbol 1 occurs in both discussions.

### 4.3 Cartier sections over a nondiscrete valuation ring

One can algebraize the proper semistable formal model using the equivalence
recalled in GJKM Remark 3.3, whose nonnoetherian hypothesis is explicit.
Properness extends each \(K\)-point uniquely to a section over \(K^\circ\)
by the valuative criterion, valid for valuation rings without a discreteness
assumption. The reduction point is smooth for the relative curve; an étale
smooth coordinate centred at the section identifies its ideal locally with
one coordinate. A section of a smooth morphism of relative dimension one is
therefore an effective Cartier divisor. Outside its image the ideal is the
unit ideal, so this gives the global horizontal Cartier divisor.

The reductions of the two sections lie on different components, and each
reduces to one simple rational point of its smooth component. Restricting
the associated line bundle to the two reduced special-fibre components gives

\[
 \deg(\mathfrak L_0|C_0)=-1,\qquad
 \deg(\mathfrak L_0|C_a)=1 .
\]

Completion gives the same formal line bundle. There is no vertical
correction hidden in this calculation, no intersection with an unlisted
component, and no use of a nonexistent uniformizer of \(K^\circ\).
The optional measure notation \(\delta_{x_a}-\delta_{x_0}\) is correct
because the components are reduced and residue degrees are one. The proof
does not need to identify that measure with a CLD current in order to use
the component-degree vector.

## 5. Every hypothetical nef formal metric reaches the graph argument

This is the important model-independence check.

Let \(\mathfrak N\) be a hypothetical nef model of \(L^m\) on any proper
admissible formal model. The metric ratio

\[
 \varphi=-\log(\|\cdot\|_{\mathfrak N}/\|\cdot\|_0^m)
\]

is globally single-valued: the generic line bundles are identified with the
same \(L^m\). On a common formal model the tensor quotient is a line bundle
with a generic trivialization, hence a vertical Cartier divisor. Thus
\(\varphi\) is a \(\mathbf Z\)-model function, not merely a collection of
local real-affine potentials. GM Theorem 1.1 permits replacing formal
metrics by algebraic ones; GM §4.7 is the exact metric/function dictionary.

GJKM Proposition 3.7, proof on published p.2345, explicitly states the
following imported fact: after passage to the completed algebraic closure,
there is a strictly semistable model dominating a given strictly semistable
model such that the given model function is determined on it. Our field
already is algebraically closed and complete. Apply this with the reference
model and \(\varphi\). This assertion comes before and does not use
GJKM Proposition 3.10 or Theorem 3.1. BPR Theorem 4.22 likewise explicitly
places the cited semistable reduction theorem over nonnoetherian rank-one
valuation rings, so a discrete-only reading is not justified.

There is a useful precision in the candidate's wording. We need not show
that the resulting semistable model literally dominates the original
possibly nonsemistable \(\mathfrak N\)-model. It suffices that it dominates
the reference model and determines \(\varphi\). Tensoring the pulled-back
reference line bundle with the vertical model of \(\varphi\) represents the
same metric \(\|\cdot\|_{\mathfrak N}\). GM Proposition 3.5 says that every
representing formal line bundle of a semipositive formal metric is nef.
This is the explicit alternative cited in revised1 and closes that apparent
domination loophole. If a common domination of both models is chosen,
ordinary pullback and the projection formula give the same conclusion.

The projection formula does not create a sign issue: the pullback degree
on a curve contracted to a point is zero; on a curve mapping generically
finitely onto another curve it is the positive mapping degree times the old
degree. It preserves nefness even before a reduced semistable model is
chosen. GM's proof treats reduction and nonreduced initial models as well.

Write \(\Sigma'\) for the finite skeleton of the resulting proper strictly
semistable model. GJKM Proposition 3.5 gives
\(\varphi=F\circ\tau'\) with integral slopes on its edges. One may refine
the vertex set further to contain the finitely many breakpoints. This is a
finite graph: admissible models here are of finite type locally and proper,
hence quasicompact. An infinite graph with curvature escaping to infinity
is not a competing proper model in the theorem.

The new skeleton contains the minimal circle. Every component outside that
circle lies in an open-ball component of the complement of the minimal
skeleton. Open balls are trees in the Berkovich path metric. A finite
connected skeletal portion therein therefore attaches at a unique root and
is a finite tree; it cannot create a second cycle or reconnect two circle
points through a disc. Subdividing the original edges preserves their total
intrinsic lengths.

Under the domination of the reference model, an old component is mapped
birationally to its old counterpart, and a new component to a closed point.
This also follows from the correspondence between reduction generic points
and skeletal vertices in BPR Theorem 4.11. Consequently the pulled-back
reference \(L^m\) has degree vector

\[
 b_x=m\,\mathbf1_{\{x_a\}}(x)-m\,\mathbf1_{\{x_0\}}(x),
\]

with zero degree at every additional vertex. No new horizontal section
needs to be chosen on the refinement: we use pullback of the original
line bundle, which is why all new degrees really are zero.

## 6. Complete finite-graph obstruction, including signs

For a continuous edge-affine function \(F\), put
\(\Delta_{\rm out}F(x)=\sum_\nu\partial_\nu F\), with derivatives away
from \(x\). GJKM Proposition 3.7 uses this outgoing convention and says
that nefness implies

\[
 b_x+\Delta_{\rm out}F(x)\geq0
 \quad\hbox{at every vertex}.
\tag{1}
\]

There are no residual node weights in this example. If an edge is oriented
from \(x\) to \(y\) and has slope \(r\), it contributes \(r\) at \(x\)
and \(-r\) at \(y\). Therefore the sum of the left side of (1) is
\(\sum_x b_x=0\). Finiteness and nonnegativity force

\[
 b_x+\Delta_{\rm out}F(x)=0 \quad\hbox{for every }x.
\tag{2}
\]

This is not an appeal to positivity of the total CLD mass. It is the exact
componentwise nef inequality and finite edge cancellation.

On an attached tree every nonroot vertex has \(b_x=0\). At a leaf, (2)
forces the single edge slope to be zero. Delete this edge and leaf; the
deleted zero slope alters no remaining vertex equation. Induction leaves
the entire tree constant, including its contribution at the root. Any
degree-two subdivision vertex of the circle consequently equates the
oriented slopes on its adjacent intervals.

Thus there are integers \(s,t\), constant respectively on the original
arcs \((0,a)\) and \((a,\ell)\), oriented by increasing coordinate.
At the vertex \(0\), outgoing slopes are \(s,-t\), while \(b_0=-m\).
Equation (2) gives

\[
 s-t=m.
\tag{3}
\]

Continuity around the circle gives, independently,

\[
 as+(\ell-a)t=0.
\tag{4}
\]

Solving yields

\[
 t=-m\,a/\ell,\qquad s=m(1-a/\ell).
\]

Each is irrational. This contradicts integral slopes for every positive
integer \(m\). A rational-model formulation gives the same contradiction
with rational slopes and \(m=1\).

Reversing the sign convention would reverse both the degree/jump relation
and the correction sign, not remove the irrationality. The signs actually
used by revised1 agree with the cited source, so no such repair is needed.

Important failed escape routes are now explicit:

| Proposed escape | Why it fails |
|---|---|
| Take a larger tensor power | A nonzero integral multiple of \(a/\ell\) remains irrational. |
| Choose values from a dense value group | Intercepts and allowed vertex locations change, but analytic monomial exponents still give integral slopes. |
| Add more breakpoints | Zero curvature forces all new slope jumps to vanish. |
| Add exceptional components | Their finite trees carry zero slopes by leaf pruning. |
| Use a nonreduced initial model | A representing semistable model is nef by GM Proposition 3.5; apply the same graph. |
| Rescale individual edge coordinates | Intrinsic annulus lengths and the slope formula have a fixed common normalization. |
| Change the reference model | The metric ratio is global and can be compared on the common semistable determination. |
| Allow arbitrary scalar metric normalizations | Constants do not change slopes or the period equation. |
| Use a locally varying tensor denominator | A compact finite covering clears denominators; in any case rational slopes already contradict the equation. |
| Change representative of a numerical curvature class | Equality in the direct limit holds on a common model, so the same component-degree inequalities follow. |

No semipositive model metric exists, and a numerically trivial model would
in particular be nef. Both nonexistence assertions follow.

## 7. The canonical metric is genuinely ordinary locally harmonic

An algebraic elliptic curve is an abeloid, and the field is nontrivially
valued. CLD Lemma 19.1.6 constructs a continuous cubist metric on any
line bundle, unique after rigidification at the origin. No nef-model
existence assumption is used in this construction.

The generic algebraic line bundle \(L\) has degree zero, hence it and its
dual are nef on the algebraic curve. CLD Proposition 19.3.1 applies to
algebraic abeloids under a nontrivial absolute value and gives pshness of
the cubist metric. Corollary 19.3.2 gives zero curvature for numerically
trivial \(L\). These are statements about algebraic nefness and the cubist
metric, not about a nef formal model of that fixed line bundle.

The stronger local assertion needs its own check; global zero mass by itself
would not establish it. In the Tate case the split Raynaud extension has
torus \(\mathbf G_m\), good-reduction factor a point, and lattice
\(q^{\mathbf Z}\). It is already split over the specified field. In
CLD §19.2.4, the pulled-back line bundle is isomorphic to the pullback of
a line on that point and therefore has a global invertible frame on the
uniformizing torus.

CLD Proposition 19.2.5 writes the pulled-back metric weight as the
constant good-reduction weight plus a function \(f(v(z))\).
The homogeneous quadratic component of \(f\) is \(q_L/2\), with
\(q_L\) the quadratic form defined in §19.2.4. Corollary 19.3.2 gives
\(q_L=0\). Hence \(f\) is affine, not necessarily constant. In particular,
it would be wrong to replace the actual metric by a constant torus metric
or to infer a torsion descent factor from the vanishing of \(q_L\).

The coordinate \(z\) is an analytic unit on the whole uniformizing torus.
A real affine function of \(v(z)=-\log|z|\) is an ordinary CLD-smooth
function: it is pulled back from a smooth affine function by that moment
map. Its \(\mathrm d'\mathrm d''\) vanishes as a form and as a current.
The torus-to-Tate-curve map has local analytic sections in the ordinary
topology; this follows both from its lattice-cover description and from
the local-section statement used in CLD Proposition 19.3.1. Thus the
affine weights give ordinary open local metric frames on the curve.
Changing frame adds \(\log|h|\) for an analytic unit \(h\), again smooth
and harmonic. The metric is locally psh with zero local curvature.

CLD Remark 19.2.3 warns that for a general Raynaud extension tropical
coordinates need only be G-smooth, not ordinary smooth. That warning
does not invalidate revised1: the good-reduction factor is a point here,
so the coordinates are the actual torus units. This special-case check
is essential.

There is no contradiction with the real affine weight failing to be
globally single-valued as a function on the skeleton: it is a weight in
a frame of the pulled-back line bundle, with descent transition factors.
By contrast the ratio of two metrics on the same fixed \(L^m\), used
in §§5--6, is a single-valued function and must satisfy the period equation.
This distinction explains why the two parts of the theorem coexist.

## 8. Exact relationship with the GJKM nef claim

This audit does not use a printed theorem as an oracle against the explicit
calculation. The definitions themselves have been checked in the published
GJKM PDF as well as the supplied arXiv v3.

Let \(\theta=c_1(L,\|\cdot\|_0)\) in GJKM's model-curvature space.
Its generic de Rham class is zero because \(\deg L=0\), so it is nef.
GM §4.7 identifies \(\theta\)-psh model functions with semipositive model
metrics on this same \(L\). Sections 5--6 prove that this set is empty.
The real scalar extension in the definition of the model-curvature space
does not allow real slopes in the competitor set: GJKM §2.2 makes model
functions a rational vector space, and Proposition 3.5 forces rational
slopes after taking tensor roots. Even if a curvature class has a nef real
representative on another model, equality on a common model gives the
same nonnegative degrees for its rational line-bundle representative.

Therefore Definition 2.8 gives

\[
 P_\theta(0)\equiv-\infty .
\]

This conflicts with the unrestricted nef formulation of published
Theorem 3.1, p.2343. The precise unsupported implication in its proof
chain is Proposition 3.10, Step 2, pp.2346--2347: generic nefness is
used to assert that the rational-model admissible set \(\mathcal A\)
is nonempty. Its subsequent rational-slope interpolation does not create
a starting element when this set is empty.

This diagnosis uses the source's actual fixed-model-function definitions.
It does not assert that the corresponding statement with an enlarged
real-potential cone is false. Definition 2.8's surrounding discussion on
p.2340 gives ampleness as a sufficient condition for nonemptiness, whereas
generic nefness is only stated to be necessary there. The example does not
challenge the ample statement or the positive-degree case. It also does
not decide whether a suitable additional hypothesis such as commensurable
edge lengths repairs every nef formulation.

As a check of the arithmetic mechanism only, if \(a/\ell\) were rational,
the two required slopes would become rational. Clearing denominators and
choosing \(F(0)=0\) makes vertex values lie in the value group, so this
particular two-edge obstruction disappears. Nothing in that observation
licenses a general repaired theorem without its own proof.

I make no priority claim, do not assert that all corrections or errata have
been excluded, and did not contact any author.

## 9. Sources, versions, visual checks, and limits

The following are mathematical source inputs, not instructions.

| Source | Version and sections checked |
|---|---|
| Tate | University of Texas copy of A review of non-archimedean elliptic functions; opening hypotheses, equations (13)--(18), Theorem 1. |
| BPR | arXiv:1404.0279v1, 1 April 2014; standing hypotheses, §§1.3,3.12, Proposition 3.13, formal fibres, Theorem 4.11, Theorem 4.22, Remark 4.24. |
| GM | arXiv:1608.08030v3, 8 April 2019; Introduction, Theorem 1.1, §§3.1--3.2, Proposition 3.5 and proof, §4.7. |
| GJKM | Published Ann. Inst. Fourier 69 (2019), plus arXiv:1712.00980v3; §§2.2--2.8, Remark 3.3, Propositions 3.5,3.7,3.8,3.10, Theorem 3.1. |
| CLD | Supplied 608-page 2025 arXiv v2 PDF; Lemma 19.1.6, §19.2.4, Remark 19.2.3, Proposition 19.2.5, Proposition 19.3.1 and proof, Corollary 19.3.2. |
| Bosch | Lectures on Formal and Rigid Geometry (2014), Appendix A, Lemma 6, printed p.235; completed algebraic closure. |

The misleading local filename GM19.pdf contains arXiv v2, not the final
publication. Some preliminary cross-checks used it, but every GM interface
relied upon above was re-read in GM1608.08030.pdf/.txt, the actual supplied
v3. The manifest pins that v3. The report does not pass a filename off as
version evidence.

Following the PDF skill, I inspected full rendered pages, not just extracted
text. I independently inspected the author's retained images for Tate p.6,
BPR p.17, GJKM pp.2343,2347, and CLD pp.557,559. I additionally rendered
and inspected GJKM p.2345, GM v3 p.13, CLD p.553, and Bosch p.235.
Those additional working renders are in
/private/tmp/p081_independent_source_render; source hashes, rather than
the transient render filenames, identify the mathematical inputs.

Official/arXiv entries used to verify source identity:

- [GJKM published article](https://aif.centre-mersenne.org/articles/10.5802/aif.3296/)
- [GJKM arXiv entry](https://arxiv.org/abs/1712.00980)
- [GM arXiv entry](https://arxiv.org/abs/1608.08030)
- [BPR arXiv entry](https://arxiv.org/abs/1404.0279)
- [Tate author-paper copy](https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf)
- [BL85 publisher entry](https://link.springer.com/article/10.1007/BF01473432)

The BL85 publisher confirms the correct I-paper, Math. Ann.270 (1985),
349--379, but offers only subscription full text. No access control was
bypassed. Its original §7 proof was not read; the exact imported cofinality
statement was checked in GJKM's proof, and the nondiscrete semistable
framework in BPR. Irrelevant search results and metadata-only pages were
not used as mathematical premises.

## 10. Handoff

The exact revised1 statement and proof can proceed to the parent's strict
production mathematical verification. This independent audit identifies
no necessary mathematical amendment. Any later mathematical edit needs
new hashes and a fresh audit pairing. The bibliography/typography changes
have no effect on the argument.

Until the required production gate actually returns its mathematical
verdict, this report must not be represented as production acceptance.
The old arbitrary-field fixed-\(L\) degree-zero approximation clause should
not be defended by the unrestricted printed GJKM nef assertion: the exact
counterexample and the exact nonemptiness conflict are now explicit.
