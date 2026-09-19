# Source and dependency ledger

Date: 19 September 2026

## Integrated dependencies

- `eq:p061-orbit-product-chart`: at every orbit of a split toric variety,
  an explicit principal open is the product of a pointed transverse toric
  variety and a split orbit torus.
- `prop:p061-parameterized-toric-fixed-fibre`: near the torus-fixed point of
  the transverse factor, every classically pluriharmonic function factors
  through the remaining parameter.
- `lem:p061-product-factor-reduction`: products with nilpotent reductions
  give nilpotent closed immersions on strict affinoid charts.
- `thm:p061-arbitrary-curve-factors-ph-rpl`: a finite product of arbitrary
  good strict analytic curves and a final factor with quasi-smooth reduction
  has the required classical-pluriharmonic-to-real-PL comparison.
- `prop:ch18-harmonic-functorial`: real harmonicity is preserved by
  pullback.
- `cor:p061-algebraic-split-toric-forms`: scalar extension preserves
  classical pluriharmonicity, and the two-sign comparison recovers
  harmonicity over the ground field.
- Gubler--Jell--Rabinoff, `GJR26`, Lemma 5.4(1) and Corollary 5.12:
  pullback stability and algebraic-extension descent for real-PL functions.

## Dependency closure

The proof is a formal synthesis of two already integrated P06.1 mechanisms.
The orbit chart moves the orbit torus into the parameter.  On affinoid
charts, its product with the final factor has a nilpotent reduction whose
source is quasi-smooth and reduced, so that source is the actual reduction.
The fixed-fibre theorem then removes the pointed transverse toric factor,
and the arbitrary-curve-factor theorem applies to what remains.

No new external source is invoked, no novelty or priority claim is made,
and no model-backed verifier was used for this dossier.
