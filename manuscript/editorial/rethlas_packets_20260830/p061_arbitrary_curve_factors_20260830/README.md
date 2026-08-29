# P06.1 arbitrary curve-factor packet

Date: 30 August 2026

Status: **independently audited, production verified, and integrated**.
The exact statement and proof are live-book inputs in Chapter 18.

This packet removes reducedness and geometric reducedness from the finite
curve factors in the already verified P06.1 curve-product theorem, permits
zero curve factors, and replaces quasi-smoothness of the remaining factor
by quasi-smoothness of its reduction. Its two new inputs are:

- nilpotent-thickening invariance of real-PL functions, proved affinoid
  locally by rational-domain comparison and lifting units through a
  nilpotent quotient, and cross-checked against the exact reduction
  invariance in Gubler--Jell--Rabinoff, Lemma 5.4(3);
- factorwise reduction after completed algebraic-closure base change,
  including the base change of the reduction of the remaining factor,
  proved by an explicit joint Tate-algebra quotient with nilpotent kernel.

The main proof then uses only previously verified results:

- quasi-smooth classical pluriharmonic regularity, production item
  `pi_7cd35ebd843cf80a7cd696bb`, final `correct`, zero critical errors and
  zero gaps;
- the rational-section tube and parameterized rigid-point lemmas;
- normalization descent for one reduced curve over an algebraically closed
  field, all three in production item `pi_6add90bcf0cfded12d6a074b`, final
  `correct`, zero critical errors and zero gaps.

It does not invoke the previously verified geometrically reduced
finite-product theorem as a black box in the proof of the product assertion,
so the extension is noncircular. The open-subspace clause is deduced only
after the full-product assertion has been proved.

The packet does not address arbitrary higher-dimensional singular factors,
general nonproduct germs, general nonflat normalization descent, infinite
products, nongood or nonstrict spaces, trivial valuations, or the continuous
zero-current problem.

Files:

- p061_arbitrary_curve_factors_statement_20260830.tex
- p061_arbitrary_curve_factors_source_aware_proof_20260830.tex
- p061_arbitrary_curve_factors_compile_20260830.tex
- p061_arbitrary_curve_factors_production_run_20260830/request.json
- p061_arbitrary_curve_factors_production_run_20260830/response.json
- p061_arbitrary_curve_factors_production_run_20260830/headers.json

Frozen statement/proof SHA-256:

- `6954b3ebc1f9efb060b4858ce732d9720d62741ba2397c39573312dd6e3ba8f3`;
- `e308ba5df336e38717ac27413c6f669a7fa37535bed613a79f095811c6dba4a7`.

Two independent exact-byte audits returned `PASS`. Production item
`pi_7dceb6442b4d586c4475feca` returned `verified`, final `correct`, with zero
critical errors and zero gaps, using `gpt-5.6-sol` at `xhigh`.
