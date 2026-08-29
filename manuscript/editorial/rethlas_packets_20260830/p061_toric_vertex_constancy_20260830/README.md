# P06.1 toric fixed-point constancy packet

Date: 30 August 2026
Status: **independently audited, production verified, and integrated**

This exact candidate proves a local P06.1 narrowing at the unique closed
torus orbit of an affine toric variety associated to a full-dimensional
strongly convex rational cone. It imposes no simpliciality or characteristic
hypothesis.

The proof constructs cofinal weighted strict affinoid neighbourhoods of the
fixed point. Their affinoid algebras are explicitly the semigroup Tate algebra
`K<S>`. Its Gauss norm is multiplicative and is the supremum norm, its
canonical reduction is the domain `K~[S]`, and Berkovich's canonical-reduction
description makes the Shilov boundary a singleton. Gubler--Rabinoff's
affinoid maximum and minimum principle then forces every classically
pluriharmonic function to be constant on each sufficiently small member of
the basis. The constant germ is automatically real-PL and GJR harmonic.

Files:

- `p061_toric_vertex_constancy_statement_20260830.tex`: exact statement;
- `p061_toric_vertex_constancy_source_aware_proof_20260830.tex`: exact
  source-aware proof;
- `p061_toric_vertex_constancy_compile_20260830.tex`: standalone wrapper.
- `p061_toric_vertex_constancy_production_run_20260830/`: exact archived
  request, response, and safe headers.

Primary dependencies:

- Berkovich, *Spectral Theory and Analytic Geometry over Non-Archimedean
  Fields*, Proposition 2.4.4 (canonical reduction and Shilov boundary);
- Gubler--Rabinoff, arXiv:2506.13548v2, Theorem 6.4 and Propositions 7.2,
  7.3 (affinoid maximum/minimum and restriction of pluriharmonic functions);
- Gubler--Jell--Rabinoff, *Bull. Soc. Math. France* 154 (2026), Definition
  5.1, Definition 7.2, and Remark 7.3(5),(6) (real-PL and harmonic functions).

Exact caveat: this is a **germ theorem at the torus fixed point**. It does not
assert regularity on an arbitrary toric analytic domain, along a
positive-dimensional orbit, or at a general non-toric singularity. It is not
a full solution of P06.1. The full-dimensional hypothesis is what makes the
closed orbit a point and gives a weight strictly positive on every nonzero
monomial. The nontrivial valuation supplies strict value-group radii tending
to zero; no claim is made here for the trivially valued case.

Frozen statement/proof SHA-256:

- `edbe69950a0a9c81ca2fd9077a58be96ec6bdb6c27ce9cf2524da5bf653a5ab6`;
- `531e326b4aeb19067fcb88af2f6eb6477a169587d71a3249103777c9131cf8f4`.

Two independent exact-byte audits returned `PASS`. Production item
`pi_dfd932c583fee3acd3fefbe3` returned `verified`, final `correct`, with zero
critical errors and zero gaps, using `gpt-5.6-sol` at `xhigh`.
