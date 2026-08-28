# P17.1 candidate 1: fail-closed rejection

Date: 28 August 2026

Target: Pille--Schneider, Question 4.9, in the literal integral-Banach-base
scope recorded in `p171_banach_family_ma_candidate1_statement.md`.

Production verifier verdict: **wrong**.

The candidate is not integrated into the monograph and P17.1 remains open.
The first decisive failure occurs already in relative dimension zero: the
mixed resultant was placed in the dual Deligne line and its local polynomial
was assigned the transformation rule (R_{e'}=uR_e).  The correct positive-
line rule is (R_{e'}=u^{-1}R_e).  Consequently the proposed finite-level
weights patched a metric on the wrong line.  The verifier also found
theorem-sized gaps in the arbitrary-base relative resultant, nonflat base
change, nonpure/nonreduced fibres, the mixed Chow--Deligne isometry, and the
normalization of the powers (q_\ell).

The analytic Philippon--Gauss boundary estimate survived the audit, apart
from two repairable missing proofs: continuity of Philippon measure in the
nonzero coefficient tuple and the topology of Archimedean characters modulo
complex conjugation.  It has therefore been isolated as a strictly smaller
problem in
`p171_weighted_philippon_gauss_continuity_problem_20260828.md`; it must pass
a new independent Rethlas run before it may enter theorem typography.

Exact archive hashes:

- statement:
  `e21e2c7c08b7673432add884b908abb0e4fe6238604c873a06a8701e2ae62ba5`;
- request:
  `b5257eda88f30df8ffcef7378db3c0f568d2f7fe72cb0a325f432757592e2a73`;
- response:
  `e430b22109ea2d3b1a20223a0b627bc439050e9fc531272b3115ef7f9b81177d`;
- headers:
  `cffbe3cd8d92f4dc3ca0be18a7d36949ed33a1d0472130748865b490f2d43b36`;
- modular repair packet:
  `d3432d79fe4c3b656f1d0a54038303f13c7db0de2e772f75673ae096afef4175`.

The complete structured list of three critical errors and seven major gaps
is preserved verbatim in the archived `response.json`.
