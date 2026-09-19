# P03.1 affine ground-field Perron theorem — audit

Date: 19 September 2026

## Claim boundary

The theorem concerns an arbitrary nonempty locally upper-bounded family of
classically psh functions on an ordinary open subset of analytic affine
space over a complete nontrivially valued field.  The usc regularization of
the pointwise supremum passes every smooth strict analytic-curve test
defined over the ground field.

This is weaker than classical psh-ness, whose definition also quantifies
over curves after every analytic scalar extension.  The upgrade corollary
therefore assumes the exact scalar-regularization identity it needs.  The
non-openness proposition only rules out a general topological shortcut; it
does not construct a psh envelope with a nonzero scalar defect.  No CLD-v2
or continuity conclusion is asserted, and no P03 atom is retired.

## Proof ledger

1. A compact test-curve graph admits a uniform closed relative-polydisc
   tube inside the affine open set.
2. The relative Gauss section over the finite Shilov boundary of the base
   curve is a boundary of the tube.  This follows coefficientwise from the
   Gauss formula.
3. Pulling back each competitor and subtracting the pulled-back harmonic
   comparison function gives a classically psh function on the tube.  The
   affinoid maximum principle propagates the finite boundary estimate to
   the whole tube, uniformly over the family.
4. Near an interior point of the zero section, the tube projection is
   quasi-smooth and boundaryless, hence open.  Its open image converts the
   raw-supremum tube bound into an ambient-neighbourhood bound for the usc
   regularization.
5. Thuillier comparison gives subharmonicity on the relative interior of
   every ground-field test curve; the boundary theorem extends it to the
   whole curve.
6. After scalar extension the same proof controls the regularization of the
   pulled-back raw supremum.  Equality with the pullback of the original
   regularization is kept as an explicit additional hypothesis.

## Hostile checks

- The radius is chosen in the nontrivial value group and tends to zero, so
  the nested closed tubes meet exactly in the zero section.
- The relative-Gauss boundary argument allows an infinite Tate expansion:
  the weighted coefficient norms tend to zero, and the base Shilov boundary
  is finite.
- Openness is used only on the ordinary open interior of the closed tube,
  where boundarylessness holds; no openness is claimed at the tube's
  relative boundary.
- The raw supremum, rather than its regularization, is the function bounded
  on the tube.  Local openness is precisely what turns that bound into the
  required ambient regularization estimate.
- The proof never interchanges scalar pullback with usc regularization.

No model-backed verifier was used for this dossier.
