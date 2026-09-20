# P07.1 exact infinite-star × infinite-collar product: hostile audit

Date: 2026-09-20

## Scope

- The active factors are the exact CLD star `X_B` and the constant-tail
  interval `[-infinity,R_0)` from CLD Example 6.7.2.
- The comparison class uses joint convexity only on the finite product
  strata, exact trace at both kinds of included `-infinity` endpoint, one
  countable node activity set on a whole compactified tail, and the exact
  reciprocal-distance junction inequality at finite collar coordinates.
- No assertion is made for two branched factors, non-CLD stars, nonambient
  branch structures, or nonconstant Stone-affine directions.

## Failure modes checked

1. A boundary-minimum condition at the collar endpoint is false: `u(s)=s`
   has endpoint value `-infinity` and is admissible.  The proof uses exact
   trace instead.
2. A nonlinear homeomorphism from `[-infinity,R)` to a finite half-interval
   does not preserve convexity.  No such coordinate change is used.
3. Pointwise Euclidean approximation on growing strips is insufficient for
   a moving evaluation point.  The proof first makes a finite continuous
   row on each compact strip, obtains a uniform error there, and only then
   evaluates at the moving clamp.
4. The clamp is an exact smooth regularized maximum, so every approximant is
   literally constant on a terminal tail; asymptotic flatness is not used.
5. The node activity truncation and the collar clamp are both ordered.  On a
   newly retained full branch, `u_b <= c` supplies the missing comparison.
6. The value `c(-infinity)=-infinity` does not trigger the false conclusion
   that the germ is identically `-infinity`.  The construction samples
   finite slices `c(-n)` and covers this case.
7. Full star endpoints may also carry value `-infinity`.  The floor
   `c(q)-n`, and the separate double-endpoint truncation away from the node,
   make each compact target finite before Dini uniformization.
8. The fixed star neighbourhood is chosen before the strip index.  Only the
   Euclidean interval grows; the constructive proof of the star--Euclidean
   theorem permits one preassigned inner star core for every row.
9. Summable tail constants turn uniform one-row errors into an exactly
   decreasing generator sequence.
10. The logarithmic-radial endpoint skill is inapplicable: there is no
    singular kernel, boundary-depth parameter, or Hölder endpoint.  Its
    non-trigger firewall prevents a spurious logarithmic change of variable.

Status: isolated candidate pending dependency-closed model verification.
