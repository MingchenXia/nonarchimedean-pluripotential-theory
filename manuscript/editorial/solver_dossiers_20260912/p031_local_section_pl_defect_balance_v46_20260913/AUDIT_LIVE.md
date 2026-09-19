# Live integration audit

Date: 19 September 2026

## Result admitted to the book

The live packet separates the local pullback question from the remaining
globalization problem.

1. At an analytically sectioned point, restriction along the local section
   sends every cover competitor to a base competitor with the same central
   value.  Together with ordinary pullback, this proves equality of the two
   local raw semipositive real-PL envelopes, including simultaneous empty
   families.
2. In the presence of a global semipositive real-PL minorant, the global PL
   pullback gain is exactly the base globalization defect minus the cover
   globalization defect.  Consequently the cover defect contracts and the
   pullback gain is bounded by the base defect.
3. For a finite analytic orbit presentation, translates of one local section
   pass through every point of the central fiber.  Vanishing of the base
   defect therefore forces vanishing of both the cover defect and the
   symmetry-breaking defect on that fiber.
4. If such a local section exists near every base point, exact global
   pullback is equivalent to preservation of the globalization defect.  Base
   local-to-global cofinality forces cover cofinality and full P03 union
   compatibility.

## Dependency audit

- The local pullback theorem uses no finiteness, flatness, surjectivity,
  normality, or group action.
- For a cover competitor on an open neighborhood `V` of the selected point,
  the reverse inequality is taken on
  `W = U intersection sigma^{-1}(V)`.  Continuity of the analytic section
  makes `W` an ordinary open neighborhood of the base point.
- GJR26, Lemma 5.4(1), preserves real piecewise linearity under analytic
  pullback.
- GJR26, Proposition 7.6(1), preserves semipositivity under analytic
  pullback.
- A global semipositive real-PL minorant makes the obstacle real-valued and
  all four local and global envelope values finite.
- The sign in the balance identity is fixed by
  `(P_loc - s_X) - (P_loc - s_E) = s_E - s_X`.
- Pullback of global base competitors gives nonnegativity of the gain; the
  balance identity then gives defect contraction.
- GJR26, Definition 7.8 and Section 7.9, place LFS functions inside the
  semipositive real-PL class, so adjoining LFS competitors does not change
  the PL envelope.
- Only the orbit corollaries use group translates and fiber transitivity.

## Hostile boundary audit

- No local analytic section is constructed for scalar extension or for an
  arbitrary finite flat cover.
- No uniform section neighborhood over a whole fiber is claimed; the
  translated sections may be used pointwise.
- No local competitor is extended to a global competitor.
- No base local-to-global cofinality theorem is proved.
- No upper-semicontinuity, continuity, or psh regularity of the raw envelope
  is asserted.
- The original quarantined v46 statement and proof, including their
  repair-loss and v44-dependent formula, remain outside the build closure.
  The live packet uses only the exact local-section argument and the already
  integrated definitions from v40--v41.

Accordingly, no P03 atom is retired and the inventory remains at 46 active
atoms in 14 Chapter 72 problem environments.

## Automatic second pass

The post-build pass rechecked domain shrinking along the local section,
simultaneous emptiness, finiteness of the defect values, the sign and bounds
in the balance identity, orbit translation through the full fiber, and the
LFS-to-real-PL inclusion.  It also replaced an implicit inherited-hypothesis
formulation of the global corollary by an explicit statement of the finite
orbit, global minorant, and everywhere-local-section assumptions.

Rendered Chapter 15 pages 686--689 and Chapter 72 page 2995 were inspected
after that repair.  No further change was required.

No model-backed verifier was used for this packet.
