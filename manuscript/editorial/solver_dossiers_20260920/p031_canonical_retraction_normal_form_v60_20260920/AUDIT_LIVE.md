# P03.1 canonical-retraction normal form: live audit

## Claim boundary

The packet proves an exact formula for scalar usc regularization over an
algebraically closed complete ground field.  It does not assert that the
canonical retraction is analytic or that composition with it preserves
subharmonicity or plurisubharmonicity.  It therefore narrows P03.1 without
retiring P03.1, P03.2, or P03.3.

## Dependency ledger

1. `cor:p031-canonical-scalar-section-anchor` supplies the canonical
   continuous section and equality of usc regularizations at its image.
2. `cor:p031-scalar-fiber-maximum` identifies the downstairs regularization
   with the maximum of the upstairs regularization on each compact scalar
   fiber.
3. `thm:p031-affine-ground-field-perron` makes the regularization of the
   pulled-back affine Perron family curvewise psh over the extended field.
4. The smooth strict curve test in Gubler--Rabinoff, Definition 4.1 and
   Section 4.1.3, converts the identity into the stated exact residual test.

## Edge cases

- No subtraction of extended-real-valued functions is used; the defect is a
  strict inequality locus, so the value `-infinity` causes no undefined
  expression.
- The Perron family is nonempty by hypothesis.  Local upper boundedness is
  preserved after scalar pullback.
- The retraction fixes the section image, so the strict defect locus is
  disjoint from that image even when scalar projection is not globally open.
- The type-4 topological example may still have a nonempty strict locus for
  arbitrary bounded data; the packet makes no psh counterexample claim.

## Outcome

The scalar defect is now in canonical normal form: it is exactly the failure
of the already curvewise-psh function upstairs to be invariant under the
canonical continuous retraction.  The remaining analytic obligation is to
show that the retracted curve tests are subharmonic, or equivalently to prove
fiberwise constancy in the stronger compatibility route.
