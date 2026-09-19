# Live integration audit

Date: 19 September 2026

## Result admitted to the book

The live version defines a finite analytic orbit presentation and proves the
following three claims under its explicit finite, flat, surjective, good, and
strict hypotheses.

1. Fiberwise maximum descends semipositive rational PL functions as
   semipositive rational PL functions.
2. Fiberwise maximum descends LFS functions only as semipositive real-PL
   functions; no LFS conclusion is claimed downstairs.
3. The rational raw envelope commutes exactly with pullback, while the LFS and
   real-PL envelopes satisfy only the displayed four-term chain.

The live proposition also records the sharp obstruction to replacing the
rational branch by the full real-PL branch: the component-swap fold map turns
the source example into a fiberwise maximum with an irrational bend.

## Dependency audit

- Transitivity of the finite group on each set-theoretic fiber is used only to
  identify the orbit maximum with the fiber maximum and to make it constant on
  fibers.
- Rational PL stability under finite maxima is supplied by GJR26, Section
  5.2(7).
- LFS stability under finite maxima is supplied by the local calculus in
  GJR26, Section 7.9.
- Once the invariant maximum is written as a set-theoretic function pulled
  back from the base, GJR26, Proposition 5.11 directly reflects its PL class
  through the finite flat surjection.  No quotient-topology argument and no
  separatedness hypothesis are needed.
- GJR26, Proposition 7.6(1'), reflects semipositivity because a finite
  morphism is proper and the presentation is surjective.
- GR25Classical, Proposition 4.2 and Theorem 4.3, provide maximum stability for
  classically psh functions and the equivalence with semipositivity for
  real-PL functions over a nontrivially valued field.

## Hostile boundary audit

- The construction does not show that a scalar-extension map has a finite
  analytic orbit presentation.
- It does not descend semiample residue data and therefore does not descend an
  LFS function as an LFS function.
- It does not prove a full real-PL envelope identity.  The fold-map example
  rules out the required fiber-maximum closure in that class.
- It does not compare the whole local-FS/semipositive-PL union occurring in
  P03.1, and it proves no upper-semicontinuity or continuity of the raw
  envelope.
- The discarded gap-conservation and zero-gap corollaries from the research
  draft depended on the non-live v38 packet and are not present in the live
  statement or proof.

Accordingly, no P03 atom is retired and the inventory remains at 46 active
atoms in 14 Chapter 72 problem environments.

## Automatic second pass

The post-build pass rechecked every hypothesis at the point of use, both
directions of the envelope comparison, the empty-family convention, and the
counterexample.  It also inspected rendered book pages 678--681 and Chapter
72 page 2987.  The proof headings identify the intended results, equations
fit the text block, and no new visual defect was found.  No second-pass repair
was required.

No model-backed verifier was used for this packet.
