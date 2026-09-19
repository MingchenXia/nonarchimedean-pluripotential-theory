# P06.2 mixed exact-tower transfer — dependency audit

Date: 19 September 2026

## Claim boundary

The proposition treats only finite towers whose stages satisfy every
hypothesis of one of the three integrated exact bundle-descent propositions.
Projective-space and proper-curve stages retain local holomorphic separation
and paracompactness of the preceding base; a proper-curve stage also retains
algebraic closedness of the ground field.  Every space remains
positive-dimensional, good, topologically separated, pure, and strict.

It transfers four properties from the bottom space: unique zero-current
descent, classical pluriharmonicity, real-harmonicity, and first-current
rigidity.  It does not create a new bundle chart, treat an arbitrary
fibration, or assert regularity that is absent on the bottom space.

## Proof ledger

1. Apply the relevant one of the three exact descent propositions from the
   top stage down.  Uniqueness composes because every bundle is surjective
   with nonempty fibres.
2. Classical pluriharmonicity transfers by applying classical-psh pullback
   to both signs of the descended function.
3. Real-harmonicity transfers by harmonic functoriality.
4. The strengthened first-current conclusion descends the first-current
   equation through every stage; bottom first-current rigidity then makes
   the descended function, and hence its pullback, locally constant.

No new model-backed verification was needed or requested: this is a formal
dependency-closed consequence of integrated propositions.  P06.2 remains
open.
