# Live integration audit

Date: 19 September 2026

## Result admitted to the book

The live theorem defines a global section palette for a finite surjective
analytic morphism and proves two exact conclusions.

1. After fixing a cover competitor and one base point, restriction along a
   palette section through a maximizing fiber point produces a global base
   competitor whose pullback has exactly that maximum value on the selected
   fiber.
2. Restriction along a palette section through an arbitrary selected cover
   point gives the difficult pointwise envelope inequality.  Together with
   pullback, this proves exact descent for the semipositive real-PL envelope
   and for the full P03 union envelope, including simultaneous empty
   families.

For a finite analytic orbit presentation, the translates of one global
section form a palette and force the v41 symmetry defect to vanish.  The fold
example has exact envelope descent even though its fiberwise maximum is not
real PL.

## Dependency audit

- Finiteness makes each set-theoretic fiber finite, so the scalar maximum of
  one real-valued competitor is attained.
- The palette covers each fiber point.  The selected section may depend on
  the base point and the competitor, but it is a global analytic section once
  selected.
- GJR26, Lemma 5.4(1), preserves real piecewise linearity under analytic
  pullback.
- GJR26, Proposition 7.6(1), preserves semipositivity under analytic
  pullback.
- The section identity preserves the obstacle inequality.
- GJR26, Definition 7.8 and Section 7.9, place LFS functions inside the
  semipositive real-PL class.

No reflection theorem, quotient topology, open-map argument, or maximum of
real-PL functions is used.

## Hostile boundary audit

- No single palette section is asserted to maximize a competitor on every
  fiber.
- The base repair need not dominate the cover competitor or its orbit maximum
  away from the selected fiber.
- The theorem does not construct a global section, a section palette for
  scalar extension, or a palette for an arbitrary finite flat cover.
- It proves no upper-semicontinuity, continuity, or psh regularity of the
  common raw envelope.
- The live corollaries use only v40 and v41.  References to the quarantined
  v44 repair-loss packet were removed from `STATEMENT_LIVE.tex` and
  `PROOF_LIVE.tex`.

Accordingly, no P03 atom is retired and the inventory remains at 46 active
atoms in 14 Chapter 72 problem environments.

## Automatic second pass

The post-build pass rechecked the section quantifiers, finiteness and
attainment of the scalar fiber maximum, both envelope inequalities,
simultaneous emptiness, the LFS-to-real-PL inclusion, the orbit translates,
and every equality in the fold example.  It also inspected rendered Chapter
15 pages 683--686 and Chapter 72 page 2991.  No second-pass repair was
required.

No model-backed verifier was used for this packet.
