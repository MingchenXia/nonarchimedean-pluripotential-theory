# P03.1 v58 source ledger

Date: 2026-09-20

## Internal dependencies

- `lem:p031-compact-component-collar` (v56): in a compact Hausdorff space, a
  component can be isolated from a compact set disjoint from it by a clopen
  neighborhood.  The v58 proof reuses exactly this compact-Hausdorff
  separation mechanism.
- `thm:p031-rational-defect-terminal-boundary-core` (v57): the strict rooted
  carrier closures are nonempty compact connected sets, decrease with the
  truncation level, and contain the root and every chosen point of the
  terminal boundary core.
- `cor:p031-finite-flat-persistent-terminal-anchor` (v57): the earlier finite
  fiber version that v58 strictly generalizes at the topological level.
- `eq:p031-finite-flat-persistent-terminal-trace` (v57): retained explicitly
  as a separate analytic finite-flat statement and not generalized in v58.

## External sources

No new external theorem or citation is introduced.  The only general
topological fact used beyond the named internal dependencies is the standard
compactness finite-intersection property, proved at the level needed in the
displayed argument.

## Research-card scope

The `proper-open-chain-component-anchor` card was treated as a non-trigger for
its metric-chain theorem: the live setting does not assume metrizability or a
finite discrete fiber.  Its conclusion was not cited or imported.  The v58
argument is the independent compact-Hausdorff proof written in
`PROOF_LIVE.tex`.
