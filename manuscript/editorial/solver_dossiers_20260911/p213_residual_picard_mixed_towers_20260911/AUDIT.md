# Scope and audit ledger

Date: 11 September 2026.

Status before integration: candidate passed a GPT-6 Astra mathematical
audit against the live Chapter 19 curve comparison, the exact Thuillier
stalk sequence, GJR Remark 15.10, and the three live bundle-descent
propositions.

Status after integration: PASS.  A GPT-6 Astra hostile exact-live audit of
the integrated bytes found one citation-scope defect in the first cover
proof: it invoked the book's current-sheaf proposition without carrying that
proposition's locally holomorphically separated and paracompact hypotheses.
The proof was repaired by globalizing the locally ordinary-smooth
zero-Hessian difference and applying the smooth multiplier criterion
directly on the specified open.  The auditor then reported no remaining
mandatory repair.

Verified firewalls:

1. `Pic^0(C_x)` denotes the abstract group of degree-zero line-bundle
   classes.  Tensor vanishing over the reals is equivalent to torsion; no
   uniform torsion exponent is assumed.
2. The proof uses the sheaf quotient directly, so it handles arbitrary real
   slopes.  It does not incorrectly assert that one real divisor is a
   rational multiple of a single principal divisor.
3. Type-1, type-3, and type-4 germs are covered by the vanishing of the
   quotient away from type 2; no annular coordinate is imposed at type 4.
4. Every tower stage retains the complete hypotheses of its live descent
   proposition.  Locally holomorphically separated and paracompact bases are
   explicitly required at projective-space and proper-curve stages.
5. Proper curve fibres need no residual Picard assumption: a continuous
   zero-current function is constant along each complete connected fibre in
   the existing descent proof.
6. The direct Bedford--Taylor corollary concerns potentials defined on the
   whole top-level tower.  The cover and basis corollaries state separately
   the hypotheses needed to obtain local or every-open conclusions.
7. No pullback of an arbitrary nonsmooth current is used.  The proof first
   makes the difference an ordinary smooth zero-Hessian function, then uses
   the ordinary current multiplier rule.
8. P21.3 remains active outside the displayed residual-Picard mixed-tower
   ranges; the open-atom count is unchanged.
9. The cover proof first promotes the difference of the potentials to a
   globally ordinary-smooth zero-Hessian function and then applies the
   multiplier criterion on the specified open.  It does not invoke the
   current-sheaf proposition outside that proposition's locally
   holomorphically separated and paracompact scope.
