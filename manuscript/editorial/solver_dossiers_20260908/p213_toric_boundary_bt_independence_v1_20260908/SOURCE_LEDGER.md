# P21.3 invariant toric boundary subcase — source ledger

Status: candidate-level research only. It neither solves nor retires P21.3.

## Claim-to-source map

| Candidate step | Controlling source or live-book interface | Scope check |
| --- | --- | --- |
| Continuous `S`-invariant functions descend along `trop` | BGJKK25, equation (5.5), p. 29 | It explicitly permits every open `O` in `N_Sigma`, including toric boundary. |
| The descended function-current is the pushforward, and differentials commute | proof of BGJKK25, Proposition 5.3.10(iv), pp. 29–30; BGJKK25 §2.3.7 | The displayed test-form calculation needs only continuity, factorization, and canonical-skeleton support. |
| Boundary local model and continuity along compactified rays | BGJKK25, proof of Theorem 3.1.4, pp. 14–15 | Basic neighborhoods `U(sigma,Omega,x_0)` have convex dense part and contain the stated rays. |
| Smoothness means constant towards the boundary | BGJKK25 §3.3, equation (3.11), p. 18 | A finite continuous affine function with slope zero on `sigma` has this property locally. |
| Smooth tropical functions pull back to CLD-smooth ones | BGJKK25, Proposition 2.3.4, pp. 11–12 | Applies to any fan and every open subset of the partial compactification. |
| A smooth zero-Hessian factor annihilates `d'd''` after multiplication by a closed current | Direct graded Leibniz calculation in the candidate proof | If both current differentials of `T` vanish, `d'd''(fT)=d'd''f wedge T`; no toric condition on `T` is used. |

Primary source: J. I. Burgos Gil, W. Gubler, P. Jell, and K. Künnemann,
*Pluripotential theory for tropical toric varieties and non-Archimedean
Monge–Ampère equations*, Kyoto J. Math. 65 (2025),
doi:10.1215/21562261-2024-0010.

## Boundaries deliberately retained

1. The analytic domain must be an open inverse image under extended
   tropicalization in a **split toric variety**. Arbitrary toroidal charts,
   nonsplit tori, and arbitrary analytic domains are not asserted.
2. Both potentials are finite, continuous, and invariant under the maximal
   compact torus. The argument does not average arbitrary psh functions.
3. The conclusion is only P21.3's continuous-pair predicate. It does not
   assert the discontinuous-potential predicate of CLD.
4. The current `T` is arbitrary only within the positive closed CLD current
   class on `V`; no tropical representation of `T` is used or claimed.
