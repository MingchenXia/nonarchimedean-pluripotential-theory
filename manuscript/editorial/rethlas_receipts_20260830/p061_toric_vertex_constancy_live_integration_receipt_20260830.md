# P06.1 affine toric fixed-point constancy: production and live-integration receipt

Date: 30 August 2026 (Asia/Shanghai).

## Mathematical scope

Let (K) be complete and nontrivially valued, and let (X_\sigma) be the
affine toric variety associated to a full-dimensional strongly convex
rational polyhedral cone.  Every classically pluriharmonic function defined
near the (K)-rational torus-fixed point is constant on a smaller analytic
neighborhood.  Hence its germ is real-PL and harmonic in the sense of
Gubler--Jell--Rabinoff.  Neither simpliciality nor a residue-characteristic
hypothesis is required.

The theorem covers only this fixed-point germ.  It makes no claim about
positive-dimensional torus orbits, arbitrary toric domains, or arbitrary
singular analytic germs.  P06.1 is narrowed but not retired.

Integrated label: `thm:p061-toric-fixed-point-constancy`.

## Exact frozen bytes and independent audits

- statement SHA-256:
  `edbe69950a0a9c81ca2fd9077a58be96ec6bdb6c27ce9cf2524da5bf653a5ab6`;
- source-aware proof SHA-256:
  `531e326b4aeb19067fcb88af2f6eb6477a169587d71a3249103777c9131cf8f4`;
- standalone compiled PDF SHA-256:
  `6ca7f63fe7bf25e78d532655bd2929f19b4343438a5cced99094b5883ebc33b9`.

Two independent exact-byte hostile reaudits returned `PASS`.  They checked
finite generation and the positive integral grading, the weighted affinoid
presentation, the exact Gauss norm, multiplicativity through the domain
\(\widetilde K[S]\), the canonical reduction and singleton Shilov boundary,
cofinality of the weighted neighborhoods, the maximum--minimum argument,
and the real-PL/harmonic conclusion.  The final citation key resolves to
Berkovich's 1990 monograph and Proposition 2.4.4.

## Production Rethlas gate

The production service used `gpt-5.6-sol` at `xhigh`.

- archived request:
  `p061_toric_vertex_constancy_production_run_20260830/request.json`;
- checked item: `pi_dfd932c583fee3acd3fefbe3`;
- verification status: `final`;
- item disposition: `verified`;
- verdict: `correct`;
- critical errors: 0;
- gaps: 0;
- proof digest:
  `531e326b4aeb19067fcb88af2f6eb6477a169587d71a3249103777c9131cf8f4`;
- request SHA-256:
  `35a74f7588230197a9b3e84c5ab82ba103e0958d6f74ce651134b8d3bfc7a917`;
- response SHA-256:
  `f227cb19950259ef78e2af17a04c2e0c0f8b230bb9ad41e559f9e189d962311f`;
- safe-header SHA-256:
  `5af7694ed12b96f96327e9ff60c41b76e2aec86bf8e42afd523d54aa0599aecb`.

## Live integration

The exact statement and proof are input byte-for-byte in Chapter 18.  A
local presentation wrapper suppresses a redundant outer proof heading
without changing the verified bytes.  Chapter 18 records the full proof,
hypothesis and comparison ledgers, scope firewall, and production gate.
Chapter 72, the Part II introduction, Appendix L, the atomic inventory, and
the verification/provenance ledgers state the exact fixed-point exception.

The controlling inventory remains 53 active atoms in 14 formal problem
environments, with tier counts `(0,5,14,17,17)`.  P06.1 remains one active
T2 atom.

## Whole-book release gate

The integrated source converged to a 3,352-page PDF of 16,079,448 bytes with
SHA-256
`c02603eea8319f851fc378630f9c50cd20d23c52e93a3b6ef84fdd94f0b3b953`.
The log has no LaTeX error, undefined reference or citation, multiply defined
label, rerun warning, or overfull box.  Physical pages 1003--1006,
3152--3154, 3300--3301, and 3320 were rendered and inspected; no clipping,
overlap, margin intrusion, long-identifier overflow, malformed formula, or
poor proof break was found.  The canonical output artifact has the same hash.

No novelty or priority claim is made.
