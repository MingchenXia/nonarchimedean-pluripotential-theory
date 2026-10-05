# Bounded-stage and nef-target closure without the unrestricted diagonal lemma

Date: 5 October 2026. Baseline: `ef8379320f5af80cb56fe836f2cdc6c641ae656f`.
Status: proof reconstruction of restricted, already published closure
conclusions, outside active TeX and pending independent admission.
It accompanies the [abstract diagonal diagnostic](bj22_abstract_diagonal_lemma_diagnostic_20261005.md).
It does not prove arbitrary pseudoeffective-target closure, repair
general Siu division, or change a book problem's status.

Throughout, `X` is an integral projective variety over an algebraically
closed field with its trivial absolute value. No smoothness,
unibranchness or characteristic restriction is imposed in the restricted
reconstruction below.

## The finite-valued diagonal input

The compact diagonal lemma works when its stage families consist of
finite-valued continuous functions. In the printed proof of BJ22 Lemma
4.6, the two reference stage values are then finite everywhere. Taking
a smaller positive error makes the outer limit strictly less than the
reference minimum after the errors are added. The exponential
differences decrease to strictly negative values at every point, and
compactness gives a common inner stage. The parameter-error constraint
can be imposed at a later inner index. This supplies the directed
flattened net, its pointwise limit and its limiting numerical parameter.
At a minus-infinity limit value, pointwise convergence is checked
against each finite real threshold, as detailed in the diagnostic;
one does not use the impossible strict estimate `f<(-infinity)+delta`.
The [diagnostic](bj22_abstract_diagonal_lemma_diagnostic_20261005.md)
states the restriction and identifies exactly why the unrestricted
minus-infinity version does not follow from that argument.

Apply this finite-valued lemma to

\[
 K=X^{\rm an},\quad S=\operatorname{Pic}(X)_{\mathbf Q},
 \quad T=N^1(X)_{\mathbf R},\quad \rho(L)=c_1(L),
\]

using as `F_L` precisely the **finite-valued** GF Fubini–Study functions
of `L`. They are continuous and stable under adding constants. The
space is compact, and the numerical-class space is finite dimensional
and metrizable. A finite-valued GF presentation has no common zero of
its sections, so it is a base-point-free presentation. Families may be
empty; the lemma does not require a stage function in every class.

If a bounded function `u` is psh according to BJ22 Definition 4.1, every
term in its defining decreasing GF approximation is at least `u`.
Since `u` has a finite global lower bound, each stage is finite valued.
Thus bounded psh functions belong to the first closure of these
restricted families, directly by the definition, without invoking
Theorem 4.5.

It follows that a decreasing net of **bounded** psh functions `u_i`,
with numerical classes `theta_i->theta`, has a psh limit `u` whenever
the limit is generically finite. No common lower bound for the net is
required: each individual `u_i` has its own finite lower bound, which
is enough to place its defining stages in the finite-valued families.
The finite-valued diagonal lemma then flattens the outer net. The limit
may be unbounded, and its generic finiteness is still necessary for the
definition of psh.

In particular, for a **fixed bounded function** `u`, the set

\[
 \{\theta:u\in\operatorname{PSH}(X,\theta)\}
\]

is closed. Use the constant outer net of functions `u` and any convergent
net of admissible classes. This restricted numerical closedness does
not assume the unrestricted abstract lemma.

## Algebraic inputs that do not use the disputed diagonal step

The following operations can be obtained directly from the GF
definition and section algebra, and are the inputs to the truncation
argument below.

1. **Addition and rational multiplication.** Products of section
   presentations add line bundles and functions. On the directed
   product of two defining nets, sums decrease to the sum of their
   limits, and their classes converge to the sum class. Generic
   finiteness follows by evaluating at the generic trivial valuations.
   Positive rational powers are handled by divisible tensor powers.
   These assertions do not require numerical-class closedness.
2. **Nef constants and inclusion of classes.** For any real nef class
   `delta`, choose ample rational classes tending to it. Sufficiently
   divisible positive powers of their line bundles are globally
   generated, and a basis gives the constant GF function zero in the
   trivially valued metric. The constant net of zero functions and
   the defining class limit give `0 in PSH(delta)`. Consequently
   `PSH(theta) subset PSH(theta+delta)` by the sum rule. No envelope
   hypothesis is used.
3. **Finite maxima in a common real class.** BJ22 Lemma 4.9 synchronizes
   the two defining GF approximations by enlarging their rational line
   bundles by vanishingly small ample gaps. Proposition 2.19 embeds
   both GF presentations in the common stage bundle. Taking the
   maximum there is a GF operation, its limit is the pointwise maximum,
   and the common classes tend to the prescribed real class. The
   printed Lemma 4.9 argument does not use Lemma 4.6 or Theorem 4.5.

The constant-zero assertion in item 2 uses global generation on the
whole variety, including proper-support analytic points. It does not
identify arbitrary unbounded functions with finite ones. Similarly,
item 3 synchronizes given GF presentations and does not assert a new
diagonal closure theorem for arbitrary inner limits.

## Varying-class closure when the target is nef

Suppose `u_i in PSH(X,theta_i)` is a decreasing net, `theta_i->theta`,
the class `theta` is nef, and the pointwise limit `u` is generically
finite. Fix an ample class `A`. For every `epsilon>0`, the class

\[
 \beta_\varepsilon=\theta+\varepsilon A
\]

is ample. By openness, `beta_epsilon-theta_i` is ample on a cofinal
tail of the outer net. Item 2 therefore places that tail in the fixed
space `PSH(X,beta_epsilon)`.

For each positive integer `M`, form

\[
 u_{i,M}=\max\{u_i,-M\}.
\]

The constant `-M` is psh in `beta_epsilon`, and the finite-maximum
operation makes `u_(i,M)` psh in that same class. It is bounded: the
lower bound is `-M`, and its finite upper bound follows from the psh
upper bound on the compact analytification. The net decreases to

\[
 u_M=\max\{u,-M\}.
\]

The bounded-stage diagonal conclusion above gives
`u_M in PSH(X,beta_epsilon)`. This holds for every positive `epsilon`.
The function `u_M` is bounded and fixed while the classes tend to
`theta`, so **bounded-function** numerical closedness gives

\[
 u_M\in\operatorname{PSH}(X,\theta).
\]

Finally `u_M` decreases to `u` as `M` increases. The terms `u_M` are
bounded psh functions in the fixed class `theta`; applying the
bounded-stage diagonal conclusion once more gives
`u in PSH(X,theta)`, since the limit is generically finite.

Thus the reconstruction covers nef target classes, even if the
original `theta_i` are not nef and even if the final function is
unbounded. In particular it covers decreasing closure in a fixed
ample or nef class and fixed-function numerical closedness at a nef
target. It uses no envelope property, critical division or homogeneous
compactness. The reasoning is a restricted proof of already stated
psh properties, not a new priority claim.

## Why this does not settle the general pseudoeffective case

If the limiting class is pseudoeffective but not nef, the classes
`theta+epsilon A` need not be ample for small `epsilon`. Constants
need not be psh there, so the maxima with `-M` are not justified in
those classes. A single much larger ample buffer proves membership
only in that larger class and cannot replace vanishing buffers.
Accordingly the argument does not establish arbitrary unbounded
varying-class closure or a critical residual in a general
pseudoeffective class.

The [near-critical envelope calculation](independent_envelope_critical_division_followup_20261005.md)
can use this restricted reconstruction for its numerical-class
closedness step when the residual class `alpha-[D]` is nef. In its
general pseudoeffective regime that step remains an identified
imported input, not an independently repaired theorem. The separate
strict division theorem also uses basic closure in its own varying
classes, so citing it does not erase any unresolved proof provenance
outside the reconstructed nef scope.

No active theorem or proof has been replaced with this draft. The
remaining algebraic proof task is to establish the actual unbounded
GF closure without the unrestricted abstract lemma, or locate a
correct independent source argument. Generic finiteness, proper-support
poles and limiting numerical classes must all be retained. All 425
active inputs, the book and catalogue PDFs, and the 42 problem statuses
remain unchanged at this checkpoint.

## Primary-source check for the algebraic operations

BJ22 text 1610–1705 was freshly checked, including Definition 2.18,
identities (2.9)–(2.12), the complete statement of Proposition 2.19 and
its section-presentation explanation. Its tensor-product operation,
together with `0 in H_0(N)` for semiample `N`, gives the ample-gap
inclusions used in the complete Lemma 4.9 proof at text 3071–3106.
Same-bundle maxima use concatenation of section systems. Chapter 34's
existing section-algebra proofs were also checked at source lines
738–832 and 842–943: the sum and same-bundle maximum calculations,
constant translations, rational multiplication and the global-generation
proof of the zero function. No unrestricted diagonal closure is needed
for these particular operations. These scoped source checks are not a
fresh full reading of the paper or an independent production admission.
