# P06.2 invariant split-toric boundary zero-current subcase — source ledger

Status: candidate-level research only. It narrows but neither solves nor retires P06.2.

## Claim-to-source map

| Candidate step | Controlling source or live-book interface | Scope check |
| --- | --- | --- |
| Continuous invariant functions descend through extended tropicalization | BGJKK25, equation (5.5), p. 29 | It states an isomorphism for every open subset of the partial compactification, including boundary strata. |
| The descended function-current is the tropical pushforward, compatible with `d'd''` | proof of BGJKK25, Proposition 5.3.10(iv), pp. 29–30; BGJKK25 §2.3.7 | The displayed test-form computation is for a continuous function factoring through tropicalization. |
| Boundary neighbourhoods and normal rays | proof of BGJKK25, Theorem 3.1.4, pp. 14–15 | A basic `U(sigma,Omega,x0)` has dense convex part `Omega+sigma`; compactified rays with direction in `sigma` stay in it. |
| Smoothness at boundary strata | BGJKK25 §3.3, equation (3.11), p. 18 | An affine function whose slope vanishes on `sigma` is constant towards the associated boundary faces. |
| Pullback to a smooth CLD function | BGJKK25, Proposition 2.3.4, pp. 11–12 | Applies on the standard smooth structures for arbitrary fans and open subsets. |
| Character formula on the affine toric chart | Direct toric calculation | If `m` annihilates `sigma`, both `m` and `-m` belong to `sigma^vee`, so `chi^m` is a unit on `X_sigma`; the tropical representative is integral affine. |
| Classical pluriharmonicity | Gubler--Rabinoff, Proposition 4.2(2),(3) (`GR25Classical`) | Both signs of the logarithm of an analytic unit are classically psh; the cone property handles the real coefficients. |
| GJR harmonicity | Gubler--Rabinoff, Theorem 4.3 (`GR25Classical`); Gubler--Jell--Rabinoff, Definition 7.2 (`GJR26`) | On the explicit good strict domain, two-sided classical psh gives semipositivity of both signs, which is the definition of harmonicity. |

Primary source: J. I. Burgos Gil, W. Gubler, P. Jell, and K. K\"unnemann, *Pluripotential theory for tropical toric varieties and non-Archimedean Monge--Amp\`ere equations*, Kyoto J. Math. 65 (2025), doi:10.1215/21562261-2024-0010.

## Boundaries deliberately retained

1. The analytic domain is an open inverse image under extended tropicalization in a **split toric variety**.
2. The function is finite, continuous, and invariant under the maximal compact torus.
3. The field is complete and nontrivially valued, and the selected inverse image is good and strictly analytic.
4. No assertion is made for arbitrary continuous zero-current functions, nonsplit toric forms, arbitrary toroidal charts, nonproduct analytic germs, or a converse to the theorem.
