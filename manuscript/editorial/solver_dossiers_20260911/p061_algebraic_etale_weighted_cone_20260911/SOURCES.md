# P06.1 algebraic-etale weighted-cone source record

## Primary algebraic source

- The Stacks Project, *Etale Morphisms of Schemes*, Theorem 41.12.3,
  Tag [025C](https://stacks.math.columbia.edu/tag/025C), checked 11 September
  2026.  Given an etale morphism at a point and an affine target
  neighbourhood, it supplies an affine source neighbourhood with an open
  immersion into `Spec(R[t]_{f'}/(f))`, with `f` monic.
- The surrounding definition of a standard-etale algebra was checked in The
  Stacks Project, Section 41.12, Tag
  [025A](https://stacks.math.columbia.edu/tag/025A): a standard-etale algebra
  is `R[t]_g/(f)` with `f` monic and `f'` invertible; any such algebra is a
  principal localization of `R[t]_{f'}/(f)`.

The proof uses Tag 025C only for the algebraic open immersion.  It then
chooses a principal open inside the image and separately constructs a bounded
strict analytic domain.  No ordinary analytic neighbourhood is inferred
from the local-ring presentation alone.

## Live book dependencies

- `thm:p061-standard-etale-weighted-cone-tube`: a displayed strict
  standard-etale Tate presentation over a relative positive-weighted cone
  has the local real-PL and GJR-harmonic conclusion at a central-fibre point
  whenever the central fibre has the local pluriharmonic real-PL property;
  a quasi-smooth original base is sufficient.
- The algebraic-to-affinoid construction follows the already verified
  source-principal-open, target-shrink, and strict-variable-bound template in
  the proof of `prop:p061-v3-etale-toric-product`.  The new argument replaces
  the toric target tube by the displayed relative weighted-cone affinoid.

## Scope firewall

- The base is smooth and the point maps to the displayed zero section.
- The conclusion requires an actual algebraic etale morphism; a formal or
  completed-local presentation is not enough.
- The theorem neither treats source points away from the zero section nor
  produces a weighted-cone chart for an arbitrary singular germ.
- Flatness, reducedness, normality, and irreducibility of the cone are not
  assumed, but the positive grading of all displayed fibre equations is.
- P06.1 remains active.
