# P06.2 smooth proper split-toric mixed towers v62: live audit

## Claim boundary

The v62 revision adds locally trivial smooth proper split-toric bundles as a
fourth exact stage type in the existing mixed-tower machinery.  It does not
weaken any stagewise hypothesis: the preceding base is still locally
holomorphically separated and paracompact at every split-toric stage, and
the fibre is still positive-dimensional, smooth, proper, split, and toric.

The extension applies to the mixed tower over a published curve, the three
annular-bottom consequences, the globally coordinated annular-top result,
the fully interleaved coordinated-annular theorem, and its curve-local
regularity corollary.  The same exact descent also enlarges the endpoint and
residual-Picard mixed-tower results used for P21.3.  It does not treat
singular, nonsplit, nonproper, or non-locally-trivial toric fibres, arbitrary
fibrations, or annular charts available only over unrelated intermediate
opens.  P06.2 and P21.3 remain active.

## Proof ledger

1. `prop:p062-smooth-proper-split-toric-bundle-descent` gives unique
   zero-current descent and preserves the first-current equation.  These are
   exactly the two inputs used at an exact stage of
   `prop:p062-mixed-exact-bundle-tower-transfer`.
2. Iterating that proposition from the tower top to the bottom gives the
   same unique pullback formula and regularity-transfer statements for all
   four stage descriptions.
3. A smooth proper split toric variety is geometrically integral and hence
   connected after every relevant scalar extension.  In a local bundle
   chart, the identity of its dense split torus is a rational point and
   supplies a local section.  Consequently, every locally constant annular
   slope remains fibrewise constant and descends uniquely through a
   split-toric stage.
4. The interleaved-annulus induction is otherwise unchanged: exact stages
   use the expanded transfer proposition, while coordinated annular stages
   use `prop:p062-open-polyannulus-rigid-base`.
5. The endpoint and residual-Picard results first descend the zero-current
   function through the tower and only then invoke their bottom-space
   classification.  Adding a split-toric stage therefore changes neither
   their bottom hypotheses nor their current-multiplier arguments.

## Field and overlap checks

- The split-toric descent works over every complete nontrivially valued
  ground field; algebraic closedness remains required only at a proper
  smooth curve stage and in results whose published-curve base already
  imposes it.
- The identity section is chosen separately in each local trivialization.
  Transition maps need not preserve it because the relevant function is
  already constant on the whole fibre; the descended local functions agree
  on overlaps by fibrewise constancy.
- Projective-space stages remain listed separately although they are special
  split-toric cases.  The statements ask that one stage description be
  specified, so this redundancy neither changes the proof nor creates an
  ambiguity in the induction.
- No nonsmooth current is pulled back through a tower.  The P21.3
  consequences first identify an ordinary smooth zero-Hessian function on
  the top space and then use the existing smooth multiplier criterion.

## Outcome

The v61 split-toric descent is no longer isolated at one bundle level.  It
now propagates through every exact and coordinated-annular mixed-tower
construction that depends only on unique descent, first-current rigidity,
connected fibres, and local sections.  The open-problem inventory remains
at 46 active atoms in 14 formal problem environments.
