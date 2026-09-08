# Self-audit: invariant split-toric P21.3 candidate

## Result under test

The candidate proves a new restricted P21.3 subcase: an arbitrary positive
closed CLD current, but only against equal-curvature continuous psh pairs
invariant under the maximal compact torus on an open subset of a split dense
torus.

## Checks already passed by inspection

- **No pullback-injectivity assumption:** equality of analytic Hessians is
  pushed forward using BGJKK25 Proposition 5.3.10(iv), rather than inferred
  from equality of pullbacks.
- **No smooth approximation of arbitrary analytic psh functions:** the
  difference is first shown to be locally affine on the tropical side, hence
  is itself a smooth CLD function after pullback.
- **No hypothesis on the current beyond the target P21.3 class:** the only
  multiplication step is the existing closed-current smooth-factor lemma.
- **No global affine assertion:** the proof uses Euclidean balls and obtains
  only local affine functions, which is all CLD smoothness requires.

## Questions for hostile review

1. Confirm that the explicit test-form calculation in the proof of BGJKK25
   Proposition 5.3.10(iv) extends from its stated psh potentials to arbitrary
   continuous invariant functions.  The candidate identifies the exact three
   ingredients used in that calculation and invokes no positivity conclusion.
2. Confirm that applying `d'd''` to these function-current pushforward
   identities yields the displayed equality without a support defect.
3. Confirm the exact normalization/sign of the moment coordinates is
   immaterial for the assertion that an affine tropical function pulls back
   to a smooth zero-Hessian CLD function.
4. Confirm that the book's `cor:ch16-smooth-h` accepts the precise bidegrees
   permitted in P21.3.

## Nonclaims

This dossier is not an independent verifier receipt, contains no assertion
that a live chapter has changed, and does not decrease the count of active
atoms.
