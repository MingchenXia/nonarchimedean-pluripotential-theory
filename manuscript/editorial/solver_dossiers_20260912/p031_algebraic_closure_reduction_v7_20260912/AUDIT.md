# P03.1 completed-algebraic-closure reduction — audit

Date: 19 September 2026

## Claim boundary

For the affine Perron family already treated in Chapter 15, passage from a
complete nontrivially valued field to the completion of an algebraic closure
creates no upper-regularization defect.  Classical psh-ness of that envelope
is equivalent before and after this passage.

This reduces the stronger affine Perron route to complete algebraically
closed ground fields.  It does not assert that the full local-Fubini--Study
or semipositive-real-PL obstacle family commutes with scalar extension: the
pulled-back competitor family may be smaller than the full competitor family
over the extended field.  No P03 atom is retired and no CLD-v2 or continuity
conclusion is drawn.

## Proof ledger

1. Around a base point in the affine open set, choose a strict affinoid
   domain whose relative interior contains that point.
2. Relative interiors are preserved in the needed direction by scalar
   extension.
3. On a strict affinoid, scalar projection from the completed algebraic
   closure is open by Berkovich's Corollary 1.3.6.  Localizing inside the
   relative interiors globalizes openness to the ordinary open set.
4. The live open-pullback lemma then identifies the pulled-back
   regularization with the regularization of the pulled-back raw supremum.
5. Gubler--Rabinoff Proposition 4.2(5) preserves each classically psh
   competitor, so the live affine Perron theorem over the completed
   algebraic closure gives ground-field curvewise psh-ness there.
6. The same proposition makes full classical psh-ness of the envelope
   equivalent before and after scalar extension.

## Hostile checks

- Openness is claimed only for the completed-algebraic-closure extension,
  not for arbitrary analytic extensions.
- The proof uses relative interiors, so an affinoid domain need not itself
  be ordinary open in the ambient affine space.
- Ground-field curvewise psh-ness over the algebraically closed completion
  is not promoted to classical psh-ness without checking further analytic
  extensions.
- The reduction concerns the stronger arbitrary-family affine Perron
  problem.  It does not identify the full obstacle competitor families
  before and after scalar extension.

No model-backed verifier was used for this dossier.
