# Live integration audit

Date: 2026-09-19

## Integrated scope

The live book imports only the self-contained core of the quarantined v39
candidate:

1. the definition of an ordinary-locally-split finite analytic morphism;
2. descent of a locally Fubini--Study function by fiberwise maximum; and
3. exact pullback compatibility for the raw LFS envelope, including the
   empty-family case.

The former defect-preservation and branch-collapse corollaries were removed.
They referred to quarantined v35/v38 statements and are not needed for the
core theorem.

## Hypothesis and proof audit

- The local splitting is an explicit hypothesis.  No implication from
  finite flatness, finite etaleness, or scalar extension is used.
- Surjectivity makes every fiber nonempty; finiteness makes the fiberwise
  maximum finite.
- On a splitting neighborhood, each sheet is analytically isomorphic to the
  base.  The local LFS presentation is preserved under that isomorphism.
- The fiberwise maximum is the finite maximum of the transported sheet
  functions.  The full real-coefficient LFS calculus is closed under finite
  maxima.
- Pullback sends every base competitor to a cover competitor.
- Fiberwise maximum sends every cover competitor to a base competitor and
  dominates the original function after pullback.  These two maps give both
  pointwise envelope inequalities.
- The same two maps prove that the two competitor families are empty
  simultaneously, so the convention `sup empty = -infinity` is covered.

## Boundary audit

The result concerns only the LFS subfamily.  It neither compares that family
with all semipositive real-PL competitors nor proves psh regularity or
continuity of the common raw envelope.  It therefore retires no P03 atom;
the inventory remains 46 active atoms in 14 Chapter 72 problem environments.

## Verdict

The integrated definition and two theorems are dependency-closed and suitable
for the live manuscript within the stated ordinary-local splitting range.
