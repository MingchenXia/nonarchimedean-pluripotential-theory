# P06.1 v3: contracting ordinary-etale toric tubes

Status: **frozen research candidate; not integrated; not production
verified**.

Date: 30 August 2026.

This sibling dossier preserves v2 and repairs the unique gap in its
independent exact-byte hostile audit,
`../p061_etale_toroidal_tube_v2_independent_audit_20260830/INDEPENDENT_EXACT_BYTE_HOSTILE_AUDIT_20260830.md`,
SHA-256
`d884005655ff604eea9e45d90c243f8751ed8505d92700033d90ac2ef8ae4d10`.
That audit found zero critical errors and one proof gap: the proposition
allowed a rank-zero toric lattice, while the coefficient-decay proof wrote a
maximum over a generating family that is empty in rank zero.

V3 separates that case before any generator maximum.  When
`rank(N)=0`, it records

```text
S={0}, q=0, R_k=K, A=A_n=B, J=0.
```

Every coefficient error is then identically zero in every `A_n`, so the
coefficient-contraction hypothesis holds without an empty-family convention.
The source-Zariski corollary explicitly identifies the dense torus orbit
with this rank-zero pointed factor.  No other mathematical claim is changed.
The v2 directory and its bytes were not altered.  No live-book file was
edited and no production verifier was called while preparing v3.

## Result

The packet proves an actual affinoid product near a point lying over the
fixed orbit of a pointed split toric factor.  If an algebraic ordinary-etale
chart has target (Z\times Y), where (Z) is the affine toric variety of a
full-dimensional pointed cone and (Y) is smooth, then on a sufficiently
deep weighted toric tube the source is

\[
                     U_n\times_K D,
\]

where (D) is the retained fixed-fibre etale cover.  The proof never
identifies (D) with an open of (Y).  Every fibre of the projection to
(D) is a scalar-extended semigroup Tate affinoid with singleton Shilov
boundary.

The central sufficient hypothesis is presentation-local.  For

\[
 C=A\langle T,U\rangle/(g,hU-1)
\]

over a retract (B\to A\to B), only the finitely many coefficient errors of
(g) and (h) must tend to zero on the chosen tube algebras (A_n).  One
common Banach--Newton radius controls all four exact and perturbed root
problems needed to construct mutually inverse maps.

The singleton-Shilov factorization theorem is separated from its regularity
corollary.  Factorization is stated over an arbitrary complete
non-Archimedean field; real-PL pullback is asserted only over a nontrivially
valued field for good strict analytic spaces, exactly the setting of the
published Gubler--Jell--Rabinoff result.

## Dependency isolation

Only the already production-verified theorem that classical
pluriharmonicity on a good strict quasi-smooth space implies real-PL and GJR
harmonicity is imported.  Its needed proof, including its etale-descent
lemma, is copied byte-for-byte into
`p061_quasismooth_needed_proof_excerpt_20260830.tex`.  The unrelated
integral/rational-PL counterexample from the larger dependency packet is not
present in this dossier.

The product-neighbourhood, weighted toric, and all-orbits statements come
from the independently production-verified all-toric-orbits dossier.  Its
status is recorded accurately in `DEPENDENCY_PROVENANCE.md` and
`SOURCE_MATRIX.md`.

## Files

- `p061_etale_toroidal_tube_v3_statement_20260830.tex`: principal statements.
- `p061_etale_toroidal_tube_v3_proof_20260830.tex`: source-aware proofs.
- `p061_etale_toroidal_tube_v3_compile_20260830.tex`: standalone wrapper.
- `p061_etale_toroidal_tube_v3_compile_20260830.pdf`: compiled audit copy.
- `p061_quasismooth_needed_statement_excerpt_20260830.tex`: only the needed
  quasi-smooth theorem statement.
- `p061_quasismooth_needed_descent_statement_excerpt_20260830.tex`: exact
  descent-lemma statement used inside the verified proof.
- `p061_quasismooth_needed_proof_excerpt_20260830.tex`: exact needed proof
  range; no counterexample.
- `REPAIR_LEDGER.md`: exact v2 audit gap and the v3 repair boundary.
- `DEPENDENCY_PROVENANCE.md`: exact dependency bytes, ranges, verdicts, and
  response hashes.
- `SOURCE_MATRIX.md`: primary-source locators and scope checks.
- `SCOPE_FIREWALL.md`: claims deliberately not made.
- `SELF_AUDIT.md`: hostile author-side audit of the repaired transition.
- `FROZEN_SHA256`: final byte manifest.

## Reproduction

Run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  p061_etale_toroidal_tube_v3_compile_20260830.tex
```

The wrapper materializes the needed theorem statements but not the proof
excerpt, whose citations require the original bibliography.  The proof
excerpt remains available for exact-byte dependency audit.

Release remains gated on a new independent exact-byte hostile audit and a
new dependency-closed production verification.
