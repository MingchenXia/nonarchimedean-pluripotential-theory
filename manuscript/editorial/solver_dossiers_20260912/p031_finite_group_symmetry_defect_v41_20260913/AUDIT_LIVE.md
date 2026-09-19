# Live integration audit

Date: 19 September 2026

## Result admitted to the book

The live version keeps the finite analytic orbit presentation from Definition
15.14.4 and proves two claims for the full semipositive real-PL branch.

1. Pullback is an order-preserving bijection from base competitors to
   invariant cover competitors.  Every cover competitor has a group average
   in that invariant subfamily, so the base family and cover family are empty
   simultaneously and the invariant subenvelope is exactly the pullback of
   the base envelope.
2. When the base family is nonempty, the full P03 pullback defect is a finite
   nonnegative invariant function, hence is constant on every orbit fiber.
   The theorem gives an exact centered formula, bounds the defect by the
   supremal orbit asymmetry and orbit oscillation, and characterizes its
   vanishing by a pointwise cofinality inequality.

The last assertion applies to the union of locally Fubini--Study and
semipositive real-PL minorants because every LFS function is already
semipositive real PL.

## Dependency audit

- The finite-group orbit hypothesis makes invariant functions constant on
  fibers and permutes the cover competitor family.
- GJR26, Section 7.3(5), makes semipositive real-PL functions a convex cone;
  consequently the finite group average stays semipositive real PL.
- Once an invariant cover function is written set-theoretically as a
  pullback, GJR26, Proposition 5.11, directly reflects the real-PL property
  through the finite flat surjection.  No quotient-topology argument and no
  separatedness hypothesis are used.
- GJR26, Proposition 7.6(1'), reflects semipositivity through the proper
  surjection.
- GJR26, Definition 7.8 and Section 7.9, place the LFS class inside the
  semipositive real-PL class.

## Hostile boundary audit

- Averaging does not generally dominate the original competitor.  The result
  therefore identifies the invariant subenvelope but does not prove that it
  equals the full cover envelope.
- The theorem proves neither vanishing nor regularity of the symmetry defect.
- It does not construct a finite analytic orbit presentation for scalar
  extension and does not descend the LFS class as LFS.
- The earlier two-gap and zero-gap claims in the quarantined research packet
  depended on non-live v38 material.  They are excluded from
  `STATEMENT_LIVE.tex` and `PROOF_LIVE.tex`.

Accordingly, no P03 atom is retired and the inventory remains at 46 active
atoms in 14 Chapter 72 problem environments.

## Automatic second pass

The post-build pass rechecked the pullback bijection, simultaneous
empty-family assertion, finiteness of both envelopes under the stated
nonemptiness hypothesis, invariance and fiber constancy of the defect, the
exact cancellation in the centered formula, both upper bounds, the zero
criterion, and the passage from the real-PL envelope to the P03 union.

Rendered Chapter 15 pages 681--683 and Chapter 72 page 2989 were inspected.
The statements, proofs, displayed formulas, transitions, and cross-references
are legible and remain inside the text block.  No second-pass repair was
required.

No model-backed verifier was used for this packet.
