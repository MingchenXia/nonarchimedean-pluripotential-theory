# P06.2 interleaved coordinated annular stages — dependency audit

Date: 19 September 2026

## Claim boundary

The theorem permits globally coordinated finite standard strict
open-polyannulus product stages at arbitrary levels of a finite tower over a
published curve.  The other stages may be admissible locally trivial
standard strict open-polydisc, projective-space, or proper smooth connected
curve bundles, in any order.

Every intermediate space is assumed boundaryless.  Each projective-space
or proper-curve stage retains the locally holomorphically separated and
paracompact base hypotheses of its source proposition.  Every annular stage
has one globally specified product chart and globally specified annular
coordinates.  Locally twisted annular transition maps and the resulting
coefficient monodromy are not treated.

## Proof ledger

1. Every displayed fibre is connected.  The local product charts provide
   local sections for the three exact stage types; the coordinated annular
   stage has a global section because algebraic closedness makes the value
   group divisible.  Hence locally constant functions descend uniquely
   through the whole tower to the original curve.
2. The induction maintains three assertions at every level: the unique
   coefficient formula; classical pluriharmonicity and real-harmonicity of
   every continuous zero-current function; and first-current rigidity.
3. At an exact stage, unique descent and all three transfer properties follow
   from `prop:p062-mixed-exact-bundle-tower-transfer`, applied to that one
   stage.
4. At a coordinated annular stage,
   `prop:p062-open-polyannulus-rigid-base` gives the new logarithmic terms
   and locally constant slopes.  The preliminary descent identifies those
   slopes with functions on the original curve, while induction expands the
   zero-current base coefficient.
5. Harmonic pullback, harmonicity of logarithms of units, and the sheaf and
   vector-space properties preserve real-harmonicity at the annular stage.

The theorem does not globalize locally defined annular coordinates, remove
any source proposition's base hypotheses, or treat arbitrary fibrations or
nonproduct germs.  P06.2 remains open, and the inventory count is unchanged.
