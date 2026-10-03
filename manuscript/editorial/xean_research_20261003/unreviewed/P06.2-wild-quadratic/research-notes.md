# Research notes and retained failed routes

The input asks for the missing ramified quadratic scalar-current gate,
starting with Q2(sqrt2), while retaining original classical recognition
and ordinary two-sign regularization as the full objective. The complete
parent argument, its self-audit and research notes were read as fallible
data. Its claimed residue-separating theorem or pending review is not
assumed. All new supporting lemmas are included in P06.2-argument.md.

The completed draft proves a forward zero-Hessian transport theorem in
every pure dimension for all separable quadratic extensions, without
an upstairs stability hypothesis. The reverse implication is included
for completeness but was already an earlier scope and is not counted
as new. The original atom remains partial.

## Route 1: rescaled traces

The old exact scalar polynomial formula used norm-one inverse trace
matrices. Rescaling a generator with |a-sigma(a)| smaller than |a|
does not make those matrices norm-one. In Q2(sqrt2), every unit
x+y sqrt2 has x a 2-adic unit and y integral, giving
|z-sigma(z)| <= 2^(-3/2). Thus no unit has the parent field condition.
The old formula is not extended by pretending that a determinant of
nonunit norm is a unit determinant.

## Route 2: divide by the logarithmic difference

Away from delta = 0, scalar quotient coordinates can be inverted and
one can attempt exact form descent. The inversion blows up at the
fixed locus and gives no fixed-support differentiated-pairing control.
It was not used. No delta or analytic coefficient that can vanish is
divided out in the final proof.

## Route 3: scalar C0 or ambient C2 approximation at the fold

Normalization by c gives F+sigma(F)=1 and the exact scalar formula
delta^2 = (max(S,0))^2. The function of S is C1, not C2; ordinary
coefficient C2 approximation on an ambient neighbourhood of zero
cannot converge to it. C0 approximation says nothing about Hessian
currents. The final proof uses C1 control and bounded second derivatives,
then integrates the second error over actual shrinking calibrated
strips, with separate treatment of top cells contained in the fold.

This does not prove that invariant ordinary exact form descent fails
analytically: extra analytic unit coordinates might provide another
description. Only the particular norm-only scalar description has the
C2 obstruction. Neither the tripod fold nor a real parity tensor is an
analytic counterexample to P06.2.

## Route 4: stop at scalar curve tests

On curves, (n-1,n-1) tests are scalar, so the fold estimate already
suggests the wild forward gate. Stopping there would miss the assignment's
higher-dimensional form obligation. The exact orbital one-form formula
survives normalization: the difference unit has logarithm
t_(b_j-b_i)+log|c| downstairs. This recovers the alternating term,
not just symmetric mixed Hessians.

## Route 5: differentiate smoothed coefficient formulas naively

The mixed differential-pair generators contain second derivatives of
the smoothed fold. Applying an unconstrained coordinate C2 estimate to
their coefficients would require third and fourth derivatives, which
are unbounded near the fold. That route is invalid and is not silently
retained in the proof.

The repair uses exterior differential algebra. O has affine
coefficients, d'd''O=0. L=(dQ+O)/2 has d'd''L=0 exactly, and
the two-form generators dL are closed for both primes. Product
differentiation then uses only zeroth, first and second derivatives of
Q. Ordered mixed terms and pure-prime alternating terms are all covered.
The symbolic diagnostic checks these cancellations for an arbitrary
smooth symbolic Q, rather than supposing it is a quadratic polynomial.

## Route 6: remove the fixed locus by a measure-zero assertion

The fold can contain an entire top-dimensional moment cell, so the
assertion that its carrier has zero measure is not generally valid.
On such cells S=delta=0 identically and all tangential derivatives
of these coordinates vanish. Their second error is zero. Only a
nonconstant affine coordinate's thin strip is measured by the shrinking
volume argument. Actual skeletal calibration provides carrier
total variation before pushforward, preventing signed fibre cancellation
from hiding an error. Generic nilpotent lengths multiply all bounds.

## Remaining obligations

This proof transports only the zero-current equation under finite
quadratic stages. Arbitrary finite separable extensions, infinite
algebraic completions, transcendental analytic extensions and universal
classical curve probes remain untreated. Ordinary two-sign psh
regularization and recognition on arbitrary germs are not consequences
of this theorem. The approximation is not asserted to preserve positive
test forms. Neither weakly smooth GJR descent nor a morphism-property
descent theorem is used in place of the ordinary tests.

The round-07 published curve-recognition paper has algebraically closed
intrinsic recognition and ground-field probe statements; its review
and dependencies are not imported here. Extending transport to a
completed algebraic closure and then establishing all needed
regularization/probe statements would require new proofs. No synthesis
closing the full original atom is claimed.

No heavy computation was needed and no operator-provided supervised
compute service was exposed. The finite smoothing surrogate used by
the diagnostic program has a box kernel and is not the smooth kernel
of the proof; its purpose is an exact finite check of fold values and
integrated Hessian errors. The authentic smooth-kernel estimates are
proved analytically in the argument. Compilation and diagnostics are
not independent mathematical review. No paper verdict is inherited.
