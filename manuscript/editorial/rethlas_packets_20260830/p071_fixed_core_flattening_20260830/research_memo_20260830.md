# P07.1 fixed-core flattening and the residual obstruction

Status: rigorous conditional theorem; **not** a solution of P07.1 and **not**
a counterexample.  This directory is isolated from the live manuscript.  No
Rethlas call was made, as requested.

## 1. Source audit

The governing source is Chambert--Loir--Ducros (CLD), Definition 8.1.1,
Lemma 8.1.4, Remark 8.1.6, Proposition 8.1.11, and Definition 8.1.13.

- Definition 8.1.1 defines `Psh_X` as the smallest subsheaf containing the
  smooth functions with nonnegative `d'd''` and stable under decreasing
  sequential limits.
- Lemma 8.1.4 defines the transfinite filtration and proves eventual
  stationarity by cardinality.  Thus the coherent content of Remark 8.1.6 is
  the unresolved *stage-one* question, not eventual stationarity.
- Definition 8.1.13 calls the stage-one functions locally approachable.
- Proposition 8.1.11 identifies the continuous hierarchy with the
  continuous part of the decreasing hierarchy.  Dini's theorem is used only
  after the approximants live on a common compact set.

The book records these facts in Chapter 15, especially
`def:ch15-hierarchy`, `def:ch15-approachable`, and
`prop:ch15-collapse-reduction`; Chapter 72 records P07.1 and P07.2.  The
previous P07 packets prove stage-one collapse for ambient toric partial
compactifications, finite ambient-induced stars, the two constant-collar
interval models, and the exact CLD star of Section 6.7.3, including an
arbitrary branch set.  None of those results supplies a general gluing
principle for a locally defined smooth-psh approximation.

## 2. What the new lemma settles

For a second-stage diagram

```
v_{n,k}  decreases to  u_n  as k tends to infinity,
u_n      decreases to  u    as n tends to infinity,
```

the lack of order between different rows is **not** an obstruction once all
rows can be realized on open neighbourhoods of one compact neighbourhood
`K` of the point under study.

The naive prescription “choose one entry in each row, impose approximate
monotonicity, and add tail constants” has a real gap: approximate
monotonicity alone does not force the chosen entries to converge to `u`.
The proof in `proof.tex` repairs that gap by also making the selected entry
from row `n` lie, up to a vanishing error, below every member of an expanding
finite square of earlier rows.  Compactness turns pointwise eventual strict
inequalities into simultaneous inequalities on `K`.  These finite-square
constraints force the diagonal limit below every `v_{r,s}`, hence below
every `u_r`, and finally below `u`; domination gives the reverse inequality.

This yields an exact sufficient criterion for full stage-one collapse: every
countable decreasing family of stage-one germs must admit row realizations
on a common compact core.  It also sharpens the counterexample target.  A
stage-two counterexample cannot be based solely on a badly ordered array on
a fixed domain.  It must defeat common-core realization (or an equivalent
extension/gluing mechanism).

## 3. Why CLD Proposition 16.9.1 does not close the gap

CLD Proposition 16.9.1 constructs, near a point of a good boundaryless
analytic space, a smooth psh function having a compact sublevel
neighbourhood.  Its proof takes a regularized maximum of finitely many
logarithms defining a rational domain.  This is a valuable local exhaustion
or barrier statement, but its conclusion contains no arbitrary target psh
function and no extension assertion for a smooth psh function given on a
smaller open set.

The regularized maximum itself combines functions already defined on one
common open set.  To extend a local approximant by taking a regularized
maximum with a barrier, one needs a seam inequality: the local term must be
subordinate to the outside term near the boundary while remaining the
relevant term on the inner core.  Proposition 16.9.1 does not provide that
two-sided placement relative to an arbitrary, possibly discontinuous and
possibly `-infinity`-valued target.  Subtracting a cutoff to arrange it need
not preserve psh positivity.  Adding a positive multiple of the CLD psh
exhaustion has the wrong inner/outer ordering for this max-gluing task unless
an additional strict positivity reserve or a separate extension theorem is
available.

Accordingly, Proposition 16.9.1 is compatible with a future Richberg-type
theorem, but it is not such a theorem and does not by itself imply the
fixed-core hypothesis in `statement.tex`.  The same conclusion holds for
the kernel regularized maximum used in its proof.

## 4. Continuous functions and truncations

CLD Proposition 8.1.11 and Dini's theorem make convergence uniform on a
compact set **after** one has placed the relevant sequence on a common
neighbourhood.  They do not turn a countable collection of shrinking local
approximation domains into a common neighbourhood.  Thus continuity removes
the convergence-mode issue but not the sheaf/globalization issue.

Likewise, replacing `u_n` by `max(u_n,-m)` removes deep poles but does not
extend a local smooth psh approximant across the boundary of its native
domain.  Truncation therefore does not establish the fixed-core condition.

## 5. Counterexample firewall

No claimed counterexample presently survives all CLD axioms.

- A formal sheaf or arbitrary topological space is irrelevant unless it is
  shown to be an affine `G`-tropical space with the CLD topology, domains,
  piecewise-linear sheaf, and smooth structure.
- A nested projective-limit construction suggested by CLD Section 6.7.5 is
  not yet usable: factorization of smooth functions through finite stages
  alone does not identify the topology, the allowed domains, positivity, or
  the exact rank of a proposed limit function.
- Replacing sequences by nets does not create a common open neighbourhood.
- Taking finite minima repairs order abstractly but is unavailable because
  minima of psh functions are not generally psh.
- The short-arm variants in CLD Section 6.7.4 may yield further examples,
  but another star calculation would not retire the general
  higher-dimensional atom.

It is therefore mathematically safer to retain P07.1 and P07.2 as open.

## 6. Ranked next attacks

1. **Fixed-core globalization on a natural analytic class.**  Prove that a
   locally approachable function admits a decreasing smooth-psh realization
   near any prescribed compact core.  A valid result must state the exact
   hypotheses that supply seam control; CLD Proposition 16.9.1 alone is
   insufficient.  Combined with `statement.tex`, this immediately settles
   P07.1 on that class.
2. **Source-legal failure of fixed-core realization.**  Search CLD's
   projective-limit examples for a function locally approachable in each row
   whose second decreasing limit has no fixed-domain smooth approximation.
   One must verify the full `G`-tropical structure and prove non-membership in
   stage one, not merely failure of a preferred approximation.
3. **Higher-dimensional polyhedral local models.**  Establish fixed-core
   approximation by a genuine convex/polyhedral extension theorem.  This
   could cover a broad natural class even if it does not settle arbitrary
   affine `G`-tropical spaces.
4. **CLD Section 6.7.4 variants.**  Analyze only after the first three
   routes, because the likely payoff is another controlled one-dimensional
   subcase.

## 7. Exact conclusion

The conditional flattening theorem is complete and removes the cross-row
ordering defect on a fixed compact core.  The unrestricted hierarchy is not
yet proved to collapse, and no rigorous natural later-stage counterexample
has been constructed.  The residual problem is a topology/sheaf/locality
problem: fixed-neighbourhood globalization of each row, or an alternative
mechanism with the same effect.
