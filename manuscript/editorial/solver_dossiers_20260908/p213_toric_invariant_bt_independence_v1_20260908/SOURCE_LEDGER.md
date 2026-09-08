# P21.3 invariant split-toric subcase — source ledger

Status: candidate-level research only.  It neither solves nor retires P21.3.

## Claim-to-source map

| Candidate step | Controlling source or live-book interface | Scope check |
| --- | --- | --- |
| A continuous `S`-invariant function on `V=trop^{-1}(O)` is uniquely `phi o trop` | BGJKK25, (5.5), pp. 28–29 | `O` is an open subset of the dense stratum `N_R`; the source permits an open subset of `N_Sigma`. |
| The tropical current of a continuous invariant potential is the pushforward of the analytic function-current, and `d'd''` commutes with that pushforward | The test-form computation in the proof of BGJKK25, Proposition 5.3.10(iv), p. 29 | Although the proposition is stated for psh functions, its displayed calculation uses only continuity, the factorization in (5.5), and the canonical-skeleton support of a pulled-back top-degree test form.  The candidate invokes exactly that calculation, not the proposition's positivity conclusion. |
| A locally affine function of torus moment coordinates is CLD-smooth with zero Hessian | `parts/part2/ch19_cld_examples.tex`, Lemma `lem:ch19-toric-chart` | This is applied only locally on Euclidean balls in the dense-torus tropicalization. |
| A smooth zero-Hessian factor annihilates the `d'd''` of its product with a positive closed current | `parts/part2/ch16_bedford_taylor.tex`, Corollary `cor:ch16-smooth-h` | This accepts every positive closed CLD current of a degree for which the displayed product is defined; it is not restricted to toric currents. |

Primary source: J. I. Burgos Gil, W. Gubler, P. Jell, and K. Künnemann,
*Pluripotential theory for tropical toric varieties and non-Archimedean
Monge–Ampère equations*, Kyoto J. Math. 65 (2025),
doi:10.1215/21562261-2024-0010.

## Boundaries deliberately retained

1. The analytic domain is an open inverse image in a **split dense torus**.
   No toric boundary stratum, nonsplit form, or arbitrary toroidal chart is
   asserted here.
2. Both potentials are required to be **continuous and maximal-compact-torus
   invariant**.  The argument does not average arbitrary psh functions.
3. The conclusion concerns the continuous-pair predicate used by P21.3; it
   does not assert the stronger discontinuous-potential predicate of CLD.
4. The current `T` is arbitrary only within the positive closed CLD current
   class on `V`.  No tropical representation of `T` is used or claimed.
