# P07.1 bivalent-star product: audit

Date: 2026-09-20

## Scope

The packet proves first-stage collapse for a product of two exact CLD stars
when at least one factor has exactly two branches.  The other branch set is
arbitrary.  It does not treat a product in which both node valences are at
least three.

## Proof obligations checked

1. For a two-element branch set, the CLD star topology unfolds
   homeomorphically to `[-infinity,+infinity]`.
2. A natural two-star generator need not be ordinarily smooth to all orders
   across the unfolded node.  Branchwise joint convexity, equality of the
   node slices, and the bivalent balance law nevertheless make it globally
   jointly convex there: the tangential derivatives agree from the common
   slice and the unfolded normal derivatives agree by balance.
3. The first-factor finite-activity and balance laws give the full
   star--Euclidean reciprocal-weight junction inequality, including when the
   unfolded barycentre lies at the bivalent node.
4. The reverse approximation uses the stronger smooth subclasses already
   supplied by the star--Euclidean theorem on finite unfolded charts and by
   the star--infinite-collar theorem at either unfolded endpoint.
5. Reflection at `+infinity` preserves convexity, balance, exact traces, and
   the constant-terminal-collar condition.
6. Fixed-neighbourhood approximation is inherited from the two cited
   product theorems.

## Automated checks

- Strict Mingchen-writing audit on the principal statement and proof:
  `0` errors and `0` warnings.
- Strict exact-current receipt audit: `PASS`.
- Local model verdict: `correct`, with `0` critical errors and `0` gaps.

No novelty or priority claim is made.
