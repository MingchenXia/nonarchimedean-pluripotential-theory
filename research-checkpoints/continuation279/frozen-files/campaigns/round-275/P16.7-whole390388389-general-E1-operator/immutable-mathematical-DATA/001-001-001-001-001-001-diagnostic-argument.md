# Audited diagnostics for P16.1–P16.7

This is a research draft, not a solution paper. None of the seven atoms is
claimed solved, and no novelty claim is made for the standard model
computations below. Their purpose is to identify specific invalid steps in
possible extension arguments. Computation verifies finite formulas, not the
analytic assertions or the open problems.

## Conventions and the one primary input used

For the model calculations fix **K = C((t))**, complete for the valuation
v(t)=1, with |t|=exp(-1), and R=C[[t]]. In particular the valuation is
discrete and the residue characteristic is zero. All spaces in these
calculations are smooth projective algebraic varieties and their Berkovich
analytifications. These choices deliberately stay in established ambient
hypotheses; they give no extension to an active residual scope.

A rational model line bundle M extending L defines a model metric. Write
its potential relative to a fixed reference metric as u, with metric ratio
exp(-u). On a regular model whose special fiber is sum_i b_i C_i, the
**raw intersection** convention for the genuine model MA measure is

    MA(M) = sum_i b_i (M^n . C_i) delta_{x_i}.

The divisorial valuation x_i is normalized by v(t)=1. For a Q-line bundle,
intersection numbers are interpreted by clearing denominators. No
probability normalization, factorial normalization, tropical inverse
operator, or Banach-algebra equidistribution measure is substituted here.
Semipositivity of a model metric means that M restricts nef to the special
fiber. The models used below all have b_i=1.

The primary text actually available and read is Boucksom–Favre–Jonsson,
*Singular semipositive metrics in non-Archimedean geometry*. The local file
bears the header “arXiv:1201.0187v2 [math.AG], 21 Jan 2014” and the internal
date “October 22, 2018”; it is preserved with its byte hash. Its standing
hypotheses (introduction and Section 2) are a complete discretely valued
field of residue characteristic zero and a smooth projective analytic
variety. The following are its exact statements used below, with notation
expanded but without strengthening their scope:

* **Theorem B.** Let L be an ample line bundle on a smooth projective
  K-analytic variety endowed with a model metric of curvature theta.
  Every theta-psh function is the pointwise limit on X of a decreasing
  net of theta-psh model functions. For a continuous limit, compactness
  and the finite-subcover form of Dini's argument give uniform
  convergence. This identifies continuous BFJ psh metrics with uniform
  limits of semipositive model metrics; no cofinal sequence is asserted.
* **Proposition 7.5.** If phi is theta-psh and X_model is an SNC model on
  which theta is determined, then (i) phi composed with emb_X_model is
  continuous and finite on the dual complex and convex on each face;
  (ii) phi composed with p_X_model is continuous on X and
  phi <= phi composed with p_X_model.
* **Theorem 7.10.** If psi is any model function, the map on PSH(X,theta)
  sending phi to sup_X(phi-psi) is continuous and proper. Consequently
  PSH(X,theta)/R is compact. The topology is equivalent to pointwise
  convergence on either quasimonomial points or divisorial points.
* **Corollary 7.9**, used only in the harmonic-limit diagnostic: if a
  decreasing net of theta-psh functions has pointwise limit phi, then
  either phi is identically minus infinity or phi belongs to PSH(X,theta).

Here theta is the curvature of the good-reduction reference metric on the
ample line bundle O(1) on P^1. Its model is P^1_R, whose dual complex is
the single Gauss point x_0. All hypotheses of these statements are
satisfied. In particular normalized BFJ psh functions have phi(x_0)=0:
Proposition 7.5(ii) on that one-vertex model gives phi <= phi(x_0).
Theorem 7.10 with psi=0 makes PSH_0 compact, and divisorial evaluations are
continuous and finite. These inputs will be used to prove finite dual
energy of each *finite atomic* measure below. This paper about psh
metrics is **not** used as a theorem extending the MA operator to E^1.

## 1. Finite model chains on P^1

Use homogeneous coordinates [Z_0:Z_1], with T=Z_1/Z_0. The reference
weight on this chart is log max(1,|T|). For real s>=0 let x_s be the Gauss
point of the closed disc centered at zero with radius exp(-s). For integer
s=i it is a divisorial point. Set

    r(x) = max(v(T)(x),0),
    g_N(x) = -min(r(x),N).

At T=0 set r=+infinity, so g_N=-N there; at infinity set g_N=0. These
rules define a continuous bounded global potential. Indeed its modified
local weight is log max(|T|,|t|^N); changing chart at infinity gives the
usual continuous metric transition for O(1).

Here is also an algebraic verification. Starting with P^1_R, blow up the
point T=t=0. Blow up next the intersection of the strict transform of the
horizontal section T=0 with the last exceptional component, and repeat
until there have been N blowups. Each center is a smooth point of a
multiplicity-one special-fiber component, away from the previous nodes.
The resulting regular projective model has reduced SNC special fiber

    C_0 -- C_1 -- ... -- C_N.

C_0 is the strict transform of the initial special fiber. The valuation of
T at C_i is i, as is seen on the successive charts T=t^i T_i. At the
generic point of C_i, T_i is a unit and v(t)=1, so its divisorial analytic
point is exactly x_i. Adjacent components have intersection 1, all other
distinct components have intersection 0. Because the total fiber
F=sum_i C_i is the principal divisor of t, F.C_i=0. Thus the two endpoint
self-intersections are -1 and the interior self-intersections are -2.

Let L_0 be the pullback of O(1) from P^1_R. Its degrees on these components
are (1,0,...,0). A vertical Q-divisor D=sum_i u_i C_i has model potential
with value u_i at x_i; along the chain it is affine and it is constant on
the fibers of the model retraction. In particular D=sum_i (-i)C_i has
potential g_N. This can be checked directly with T=t^i T_i: the metric
for L_0+D has local weight log max(|T|,|t|^N). With rational multiples of
D the weights are the corresponding convex combinations with the
reference metric.

The degrees a_i=(L_0+D).C_i are

    a_0 = 1 + u_1-u_0,
    a_i = u_{i-1}-2u_i+u_{i+1}   (0<i<N),
    a_N = u_{N-1}-u_N.

Their sum is 1. In dimension one nefness on the special fiber is exactly
a_i>=0, since its integral proper curves are the components. Also

    D^2 = -sum_{i=1}^N (u_i-u_{i-1})^2,
    L_0.D = u_0.

The usual relative dimension-one model energy, with E(0)=0 and raw mass
V=deg O(1)=1, is

    E(u) = L_0.D + D^2/2
         = (u_0 + sum_i a_i u_i)/2.

Both expressions follow from the intersection matrix just computed; in
the second one sum_i a_i u_i = L_0.D+D^2. Thus this calculation is not an
invocation of an unknown finite-energy operator.

For completeness, on two semipositive model metrics a,b on a common
dominating model, bilinearity gives the dimension-one cocycle

    E(a)-E(b) = (1/2) int (a-b) [MA(a)+MA(b)].

Indeed expand (D_a-D_b).(2L_0+D_a+D_b)/2. The potential of the vertical
difference evaluated at each component is its divisor coefficient divided
by that component's multiplicity, which is precisely the factor needed
against the model mass. This identity implies monotonicity and
|E(a)-E(b)|<=||a-b||_infinity. It also defines E independently on uniform
limits of semipositive model metrics, with the same monotonicity, constant
shift rule E(a+c)=E(a)+c, and normalization. These are statements about
the continuous class, not a construction of a general mixed E^1 operator.

## 2. Total-variation approximation with diverging dual energy

For an integer k>=1 put N=k^4, epsilon=1/k, and u_k=epsilon*g_N. On the
chain just constructed u_i=-epsilon*i. Its component degrees are

    a_0=1-epsilon,  a_i=0 (0<i<N),  a_N=epsilon.

They are nonnegative. Hence u_k is a continuous semipositive rational
model potential and its *genuine model* MA measure is

    nu_k=(1-1/k)delta_{x_0}+(1/k)delta_{x_{k^4}}.

The raw mass is 1. The intersection and integral formulas give

    E(u_k)=-epsilon^2 N/2=-k^2/2,
    int u_k d nu_k=-epsilon^2 N=-k^2,
    E(u_k)-int u_k d nu_k=k^2/2.

Define dual energy by the concave convention

    E^vee(nu)=sup_w [E(w)-int w d nu],

where w ranges over continuous semipositive weights on O(1), with E(0)=0.
Constants cancel because both masses are 1. The test w=u_k proves
E^vee(nu_k)>=k^2/2.

Each E^vee(nu_k) is nonetheless finite. Normalize sup w=0. On the compact
BFJ space PSH_0 the function w -> int w d nu_k is a finite continuous
linear combination of two divisorial evaluations, so it has a finite
lower bound -M_k. Every normalized continuous semipositive w satisfies
w<=0 and E(w)<=0 by monotonicity. Consequently

    E(w)-int w d nu_k <= M_k,

which proves E^vee(nu_k)<infinity. The same reasoning bounds the supremum
over any normalized E^1 domain inside this BFJ psh class, since its
infimum-defined energy remains <=0 and these divisorial integrals remain
finite. This use of compactness is legitimate only for this fixed finite
set for each k; no uniform bound in k is claimed.

Use the total-variation **norm** ||sigma||_TV=sup_{||f||<=1}|int f d sigma|,
which is twice the convention sometimes called total-variation distance.
Since x_{k^4} and x_0 are distinct,

    ||nu_k-delta_{x_0}||_TV=2/k -> 0.

Thus even convergence in total variation does not bound the dual energies
of finite-energy approximating measures. In particular weak convergence
does not do so. The limiting measure has the reference metric as an
explicit solution, so this example is **not** a counterexample to
existence. It invalidates a proof step that would extract energy bounds
from weak approximation alone. Every nu_k is supported on one finite SNC
dual complex and is toric; this is inside the catalogue's established
scope, not a resolution of P16.4 or P16.6.

The exact output of checks.py for k=1,2,3,4 has respectively N=1,16,81,256,
E=-1/2,-2,-9/2,-8, integral=-1,-4,-9,-16, lower bound=1/2,2,9/2,8, and
TV norm=2,1,2/3,1/2. These finite checks agree with the proof for all k;
they are not an exhaustive analytic verification.

## 3. A harmonic-chain exploration and its precise stopping point

This supplementary calculation tests a different gap: a finite-energy
potential definition does not identify a limiting measure with its MA.
On the N-chain put u_i=-H_i, where H_i=sum_{j=1}^i 1/j and H_0=0. The
degrees are

    a_0=0,
    a_i=1/[i(i+1)] (1<=i<N),
    a_N=1/N.

Hence u^(N) is a semipositive rational model potential. Its slope on
[i-1,i] is -1/i, and it is constant beyond N and off the chain. These
potentials decrease with N. Let u be their pointwise limit. It is zero at
x_0 and has value -H_i at x_i; at T=0 it is minus infinity. Corollary 7.9
therefore makes u BFJ psh, since it is not identically minus infinity.

Set S_N=sum_{i=1}^N 1/i^2 and S=sum_{i>=1}1/i^2. The proved model energy
formula gives E(u^(N))=-S_N/2. Define the usual infimum extension

    E(u)=inf{E(w): w continuous semipositive and w>=u}.

Then E(u)=-S/2> -infinity, as follows without importing monotone MA
continuity. The u^(N) themselves give the upper bound. Conversely, for
any continuous majorant w and any epsilon>0 the increasing open sets
{u^(N)<w+epsilon} cover the compact analytification, because their
pointwise limit is u<=w. A finite subcover gives one N valid everywhere.
Energy monotonicity yields E(w)+epsilon>=E(u^(N))>=-S/2. Let epsilon tend
to zero and take the infimum over w. This proves the lower bound.
Convergence of S needs no special value for it; comparison of its tail
with the integral of x^-2 proves it is finite. No assertion about a
general cofinal sequence of models is made: this is one explicitly chosen
decreasing sequence and a compact finite-subcover argument.

Its explicit model measures are

    mu_N=sum_{1<=i<N} [1/(i(i+1))]delta_{x_i}+(1/N)delta_{x_N}.

They converge in TV norm 2/(N+1) to the positive Radon probability measure

    mu=sum_{i>=1} [1/(i(i+1))]delta_{x_i}.

To check this, the excess coefficient at x_N is 1/(N+1), and the mass of
the omitted tail is also 1/(N+1). The countable positive sum is a Radon
measure: its finite partial sums approximate in variation, and inner
regularity follows by approximating each measure using finite unions of
compact singleton sets; outer regularity follows by excluding finitely
many unwanted singleton points and bounding the remaining tail.

Tonelli's theorem for nonnegative series gives

    int (-u) d mu
      =sum_i H_i/[i(i+1)]
      =sum_j (1/j)sum_{i>=j}1/[i(i+1)]
      =sum_j 1/j^2=S.

Nevertheless mu does not have the uniformly bounded pairing property on
all PSH_0 that the local chapter uses as an additional admissibility
condition. For the continuous psh tests g_N,

    -int g_N d mu
      =sum_i min(i,N)/[i(i+1)]
      =sum_{j=1}^N sum_{i>=j}1/[i(i+1)]
      =H_N -> infinity.

Here each mu_N is genuinely MA(u^(N)). The arguments just written do
**not** assert independently that mu=MA(u) for an extended operator, or
that E^vee(mu) is finite for the *full* psh cone. Controlling a
ray-restricted Legendre supremum would not establish the latter statement:
its supremum has fewer competitors. Both stronger identifications need
the appropriate full baseline operator/energy inputs or a separate proof.
This explicit stopping point prevents a definition-plus-limit calculation
from being relabeled an arbitrary-field theorem. The finite-energy
potential statement is exactly the infimum-energy statement proved here,
in the known characteristic-zero P^1 setting.

## 4. An analytic obstruction to an unchanged zero-volume theory

Let X=P^1_K x P^1_K and L=pr_1^*O(1). The space is smooth, connected,
projective, proper, algebraizable, and of dimension two. L is nef and
pseudoeffective but nonample: on {a} x P^1 its restriction is trivial.
Moreover h^0(X,L^m)=m+1, so

    vol(L)=limsup_{m->infinity} 2! h^0(X,L^m)/m^2=0.

The intersection mass L^2 is also zero: if A=pr_1^*O(1) and
B=pr_2^*O(1), then A^2=B^2=0 and A.B=1. Thus this is an actual analytic
example in the nonample pseudoeffective axis, with raw mass zero, not an
abstract balanced fan.

Construct two continuous semipositive model metrics on L. The first eta_0
comes from the good model P^1_R x P^1_R. Its only special-fiber component
has line bundle O(1,0), whose self-intersection is zero. Hence the genuine
model MA(eta_0) is the zero measure.

For the second, use the one-blowup curve model from Section 1 with N=1
and D=-C_1. Let M_1=L_0-C_1. Its component degrees are 0 on C_0 and 1 on
C_1. Form the product over R of this model with P^1_R and pull M_1 back
from the first factor. The generic fiber is again X and the generic line
bundle is L. Each special component is C_i x P^1_C, with multiplicity
one, and the restriction is pulled back from a degree a_i line bundle on
C_i, where a_i is 0 or 1.

This restriction is nef on every integral curve: for a curve mapping
nonconstantly to C_i its degree is the nonnegative degree a_i multiplied
by the degree of that map; for a curve mapping to a point it is zero.
Thus eta_1 is semipositive. On each special surface the square of that
line bundle is zero, because it is pulled back from a curve. The exact
genuine model formula gives

    MA(eta_1)=0=MA(eta_0).

Their potential difference is g_1 composed with pr_1. It takes values 0
and -1 at the product Gauss points with respective T-radii 1 and
exp(-1), and S-radius 1 in both cases. These analytic points exist by the
Gauss seminorm on K[T,S]. Consequently the two metrics do not differ by
an additive constant in weight (or a scalar in norm).
Their difference is bounded, so they have the same singularity type under
the usual equivalence by bounded differences. Merely fixing that reference
type would not separate these two metrics.

Every mixed degree-two model measure formed from eta_0 and eta_1 also
vanishes: on the common product model both line bundles restrict as
pullbacks from the same curve. Therefore the usual relative model energy

    E_eta0(u)=(1/3)sum_{j=0}^2 int u c_1(eta_1)^j c_1(eta_0)^(2-j)

is zero for u=g_1 composed with pr_1; it is also zero for u=0. This does
not presuppose a completed E^1 class for nonample L. It shows that a
proposed extension defined by this finite model formula, whose domain
contains both continuous semipositive metrics, has two finite-energy
solutions of the zero equation separated by a nonconstant potential.

Thus **raw top-degree MA + the full continuous semipositive model cone +
uniqueness modulo R cannot all be retained at zero volume**. A positive
measure of raw mass zero is necessarily the zero measure, and dividing
by zero cannot produce a probability. The example does not rule out a
replacement theory with a different quotient, admissible domain, lower
dimensional datum, or mass operator. P16.5 explicitly allows replacement
conventions, and also has the general big nonample residual scope. This
diagnostic therefore does not solve or refute the exact atom. It is
standard rank-degeneracy behavior, not a claimed new equation theorem.

## 5. Two precise descent failures

**Resolution can lose ampleness.** If f:Y->X is a proper morphism and a
complete integral curve C in Y maps to a point, then (f^*L)|C is trivial
for any line bundle L on X. Indeed its restriction is pulled back from a
one-dimensional vector space over the residue field of that point. Hence
deg_C(f^*L)=0. An ample line bundle has positive degree on every complete
curve, so f^*L is not ample in this situation. Already the blowup of a
point in P^2 has such an exceptional curve. Therefore a proof that resolves
a singular X and invokes only an ample-polarized smooth theorem on Y has
not checked its polarization hypothesis. A big/nef nonample extension
would be an additional input, rather than a consequence of resolving X.
No assertion that this prevents all singular-space theories is made.

**Normalization sections need not descend by powers in characteristic
zero.** Let R_cusp=K[z^2,z^3] inside B=K[z] with char K=0. The fraction
fields agree since z=z^3/z^2; z is integral over R_cusp since z^2 belongs
to it; B is finite over R_cusp, generated as a module by 1,z. Since B is
integrally closed, it is the normalization. The polynomials in R_cusp
are exactly those with zero coefficient of z: the exponent semigroup
generated by 2 and 3 is {0,2,3,4,...}. For every integer m>=1,

    coefficient_z((1+z)^m)=m != 0,

so no positive power of the normalization section 1+z lies in R_cusp.
The cusp has a single normalization point over its singular origin,
since B/(z^2,z^3) has only the prime (z), with unchanged residue field.
The calculation therefore addresses a unibranch example, rather than
the separate many-branch issue of a node. It disproves only this proposed
algebraic powers-descent step, not descent by norm/max constructions,
asymptotic metric approximation, or any analytic equation theorem.

In characteristic p>0, (1+z)^p=1+z^p belongs to K[z^2,z^3] because p>=2.
This limited contrast explains why a purely inseparable power argument
cannot be imported into characteristic zero. Nor does its validity in
this characteristic-p example establish global envelope regularity,
mixed MA products, energy differentiation, or comparison in P16.3.
It is an equal-characteristic algebraic calculation: the displayed
Frobenius identity does not hold in a mixed-characteristic ground field
of characteristic zero, even when its residue characteristic is p.

## 6. Valued-field extensions cannot discretize a nondiscrete field

An isometric inclusion of real-valued non-Archimedean fields K->F gives
v(K^*) as a subgroup of v(F^*). If F is discretely and nontrivially
valued, v(F^*)=a Z for some a>0. Every nonzero subgroup of a Z is ma Z
for a positive integer m: divide by a and use the least positive integer
in a nonzero subgroup of Z and Euclidean division. Such a subgroup is
discrete. Consequently an isometric extension of a nondiscretely valued K
cannot have discrete valuation.

An explicit complete example is the completion of the compatible directed
union of C((t^(1/m))) inside a chosen Puiseux field, with v(t)=1. Its
value group is Q: the union already has all rational values, and a nonzero
element of the completion has the same norm as a sufficiently close
element of the union, by the ultrametric inequality. Thus completion
creates no new nonzero absolute values. Any isometric extension retains
values 1/m, arbitrarily close to zero, and cannot be discretely valued.
This is an obstruction to a specific scalar-extension reduction in
P16.4, not an obstruction to an arbitrary-field MA theory. Approximation
by changing ground fields would require separate convergence, descent,
mass, and envelope results and is not proved here.

## Reproduction and evidence

All artifacts are in the worker workspace. Run:

    python prepare_sources.py
    python checks.py
    python validate_artifacts.py

The finite exact outputs are in checks-output.json. The complete source
snapshots and hashes are in sources/ and source-audit.json. The original
assignment is input.json and its readable extraction is task-input.md.
The checked primary statements are on printed pp. 33–35 of the supplied
BFJ text (text lines 1647–1739, including Proposition 7.5, Corollary 7.9,
and Theorem 7.10). A named reference-pack manifest is secondary evidence;
it does not make its absent primary PDFs available. The attempted network
retrieval failed, recorded in sources/fetch-initial.json. No heavy
computation or supervised compute was used or needed.

None of these checks proves a new finite-energy equation theorem for any
active atom. All seven remain unresolved in this deliverable. The only
external theorem inputs to the diagnostics are the exact BFJ psh
statements above, in their checked smooth ample residue-characteristic-zero
scope; the remaining quantitative and geometric conclusions have their
arguments supplied here.
