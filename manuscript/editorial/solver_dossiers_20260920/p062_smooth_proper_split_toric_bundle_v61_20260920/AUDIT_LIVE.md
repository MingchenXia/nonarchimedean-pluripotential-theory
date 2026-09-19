# P06.2 smooth proper split-toric bundle descent: live audit

This file records the v61 single-bundle checkpoint.  The v62 mixed-tower
integration supersedes its temporary exclusion of split-toric stages from
the mixed-tower statements while preserving every scope restriction below.

## Claim boundary

The packet proves exact descent for a continuous zero-current function on an
analytically locally trivial bundle with positive-dimensional smooth proper
split toric fibre.  Over a published curve, it yields classical
pluriharmonicity, local real-PL regularity, and Gubler--Jell--Rabinoff
harmonicity.  No torus-invariance hypothesis is imposed.

The result does not treat singular, nonsplit, nonproper, or non-locally
trivial toric fibres, arbitrary fibrations, or arbitrary nonproduct germs.
It is deliberately not inserted into the previously frozen mixed-tower
statements.  Thus it narrows P06.2 without retiring that atom.

## Dependency ledger

1. Properness and smoothness of the split toric variety give a complete
   regular fan.  The affine opens attached to its maximal cones form a finite
   cover and are equivariantly isomorphic to affine space.
2. Each affine-space chart is exhausted by strict open polydiscs whose radii
   lie in the value group.  Successive use of
   `prop:p062-open-disc-descent` makes the zero-current function descend on
   every member of every exhaustion.
3. The identity of the dense split torus lies in every maximal-cone chart
   and has all regular-cone coordinates equal to one.  Since every selected
   radius is greater than one, this single point lies in every exhaustion
   member and identifies all descended functions.
4. Nonempty fibres identify the functions obtained from overlapping bundle
   trivializations.  `prop:ch14-currents-sheaf` glues their zero-current and
   first-current identities on the base.
5. Over a published curve, the existing curve comparison and harmonic
   pullback results give the three stated regularity conclusions upstairs.

## Source and edge-case audit

- Cox--Little--Schenck, *Toric Varieties*, Example 1.2.21 and Theorems
  3.1.19 and 3.4.1 were checked for the regular affine chart, smooth-fan,
  and proper/complete-fan facts used in the proof.
- The base field is only required to be complete and nontrivially valued in
  the descent proposition.  Choosing `varpi` with absolute value strictly
  between zero and one makes every radius strict and greater than one.
- The hypotheses `m,q >= 1` keep every iterated disc-descent base in the
  positive-dimensional range required by the cited proposition.
- The proof uses exact descent and compactly supported current testing from
  the existing disc theorem.  It does not pull a continuous Hessian current
  back along a section.
- The projective-space result is subsumed because projective space is a
  smooth proper split toric variety, but no converse or classification
  statement is used.

## Outcome

P06.2 now contains a verified proper-fibre range strictly broader than
projective-space bundles: every analytically locally trivial smooth proper
split-toric bundle has exact zero-current descent, and the published-curve
case has the full pluriharmonic, real-PL, and GJR-harmonic conclusion.  The
remaining open scope is explicitly firewalled in the manuscript and atomic
inventory.
