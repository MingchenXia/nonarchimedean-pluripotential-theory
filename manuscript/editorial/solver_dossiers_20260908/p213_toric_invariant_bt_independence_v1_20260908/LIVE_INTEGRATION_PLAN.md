# Implemented live integration map

The map below was implemented only after the revised exact packet, using the
live-book macro `\An`, received the final V2 `correct` verdict with zero
critical errors and zero gaps.  The corresponding complete-book build passed
with no TeX errors.  The V1 receipt is historical only because it used `\an`;
the controlling V2 receipt is archived in
`POST_VERIFICATION_AND_INTEGRATION.md`.

| Live file | Placement | Change |
| --- | --- | --- |
| `manuscript/parts/part2/ch16_bedford_taylor.tex` | Immediately after `cor:ch16-smooth-h` | Insert the proposition and proof.  It belongs beside the existing smooth zero-Hessian criterion because the only new step is proving smoothness of the invariant toric difference. |
| `manuscript/parts/part6/ch72_major_open_problems.tex` | The P21.3 narrowing paragraph immediately before `prob:frontier-cross-fan-upstairs` | Add the verified invariant split-toric dense-orbit subcase.  Retain the P21.3 atom and its higher-dimensional residual. |
| `manuscript/editorial/open_problem_atomic_inventory_20260824.md` | P21.3 entry | Add this subcase to the settled scopes, without changing the count of 48. |
| `manuscript/parts/part6/ch69_verified_extensions.tex` | P21.3 ledger subsection | Record the receipt and exact scope after verification. |

No count changes: the result concerns a strictly restricted invariant
dense-torus family, not every pair on every space in the P21.3 ambient
class.
