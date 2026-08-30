# P07.1 chosen rows without a common domain: production receipt

Date: 30 August 2026

## Result

The exact frozen statement and proof passed production Rethlas verification.

- archive label: `20260830T043500Z_563bd314d2ee`;
- model: `gpt-5.6-sol`;
- reasoning effort: `xhigh`;
- verdict: `correct`;
- critical errors: 0;
- gaps: 0;
- endpoint run and item identifiers: none assigned.

The report explicitly checked the finite-exception topology of the CLD star,
the exact smoothness conditions on full and exceptional branches, the centre
slope balance, positivity from branchwise convexity, the convexity
contradiction on a branch forced to become full, and the positive rescaling
argument.

## Exact inputs and archive

- statement SHA-256:
  `563bd314d2ee0ce12c487df565e2e3c6ad222789e9acace8e550b03b386309ed`;
- proof SHA-256:
  `5d36861cef1d8861bf51ca49ef1ecf8619c4e7975a6322aaed071eee54f058c4`;
- minimal compile PDF SHA-256:
  `5d4c72fc52d5ad535703657ce67dbe650dae9846ba3ea55e429e59301e06eb77`;
- request SHA-256:
  `fb961dc17f3f9efcb2765a9361eff769b48d47e3e12bd9f1b25b379a047abdb9`;
- response SHA-256:
  `2c352b411b22528d927f97fe1d5820095b8eb05f16bb64f3dd849aa2e74ba3b8`;
- safe-header SHA-256:
  `bc7de8aefbacf4ce8597040eee26caa0963c8a589137ca8bd2a2dd5dd71ed101`.

The statement and proof were frozen before submission.  The integrated book
inputs those exact files byte for byte.

## Mathematical scope

On the exact CLD infinite star there is a countable family of smooth psh
germs, each represented on its own centre-neighbourhood, which has no
simultaneous realization by smooth psh representatives on a common
centre-neighbourhood.  The same obstruction survives after embedding the
germs into positive decreasing rows whose individual limits and outer limit
are all the global smooth function zero.

This does not exhibit a psh function of stage two that is absent from stage
one.  The zero function has global constant approximants, and first-stage
collapse on the exact star remains valid.  The result closes only the naive
quantifier argument that arbitrary chosen row presentations can be shrunk to
one fixed domain.  A solution of P07.1 still requires existential reselection
or fusion of approximants, or a different globalization mechanism.  The
inventory therefore remains 53 active atoms in 14 formal problem
environments.

No novelty or priority claim is made.
