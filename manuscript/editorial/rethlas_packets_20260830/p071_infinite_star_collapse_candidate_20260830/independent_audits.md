# Independent exact-byte audits

Frozen inputs:

- statement SHA-256:
  99c1a6a6a712005e73ee3b7cdae297606895b22ce79c80a6411dfd7f4863c963
- proof SHA-256:
  ca49ad210cf8e64100cc00c31c16a76f207ecd0d4b37dc365e8e1c61ce903090

Three independent gpt-5.6-sol xhigh audits were completed before production
submission.

## Complete-proof audit

Verdict: PASS.  It checked the repaired restriction argument, every sign,
all extended-real cases, sheaf gluing, decreasing limits, countability,
finite smoothing, diagonal monotonicity, the centre value minus infinity,
and both interior and endpoint approximations.  It found no counterexample
and requested no repair.

## Comparison-class audit

Verdict: PASS.  It checked the CLD topology and central balance orientation
against CLD Section 6.7.3, the finite/polar full-branch alternative, endpoint
traces, restriction and gluing, decreasing sequential closure, generator
inclusion, finite-centre continuity and real endpoint derivatives, bounded
finite subsums, summability, and countable support.  Counterexample attempts
using polar jumps, upward centre jumps, uncountable positive slopes, and
endpoint-trace loss were all excluded by the finite-point balance or trace
condition.

## Smoothing and endpoint audit

Verdict: PASS.  It checked the explicit smooth regularized maximum and exact
dominance region, max-of-affine representation, terminal collars, common
smoothing parameter, one-branch derivative repair, uniform errors, fixed
neighbourhood diagonal, Gaussian semigroup order, exact endpoint collars,
and convergence at a minus-infinity endpoint.  It requested no correction.

Production Rethlas subsequently returned final/correct with zero critical
errors and zero gaps for checked item pi_00f6c73303087d94da9eb724.
