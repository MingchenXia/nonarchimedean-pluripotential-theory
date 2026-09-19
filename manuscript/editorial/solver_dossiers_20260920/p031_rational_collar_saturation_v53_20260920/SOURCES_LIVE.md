# Source audit

Audit date: 2026-09-20.

## External-source boundary

This packet introduces no new source-dependent analytic assertion and cites
no new external result.  Its additional topological input is the elementary
fact that locally compact Hausdorff spaces are regular, together with the
clopen characterization of an empty boundary.

The published source behind the rational LFS definition remains
Gubler--Jell--Rabinoff, Section 7.9, already cited and audited in v50.  No new
claim is attributed to that source here.

## Internal dependencies

- `def:p031-rational-lfs`: local rational LFS normal form.
- `eq:p031-rational-lfs-block-compression`: closure of rational
  presentations under finite maxima after denominator clearing.
- `prop:p031-local-rational-lfs-cofinality`: rational downward shifts and
  local rational cofinality.
- `def:p031-rational-globalization-ledger`: the rational globalization
  defect and rational-to-LFS global gap.
- `eq:p031-three-level-defect-ledger`: decomposition of the rational defect
  into the LFS and PL defects and the two global branch gaps.
- `cor:p031-rational-cofinality-tower-collapse`: propagation of zero rational
  defect through a finite flat tower.

The remaining ingredients are continuity of rational LFS functions,
compactness, upper-semicontinuous maximization on a compact set, density of a
nonzero rational cyclic subgroup in the real line, and elementary order
arguments for suprema and infima.

## Provenance boundary

The proof was rederived directly from the live v50--v52 definitions and
theorems.  It does not import the quarantined v38 collar packet, the v49
repair-threshold packet, or any unintegrated scalar-extension presentation.
All internal labels resolve in the full-book build.

## Exact live hashes

```text
fcdd83f0a00689612ac4dca622c58d3dadd84eb8477bab164db57d0aa38dfc64  STATEMENT_LIVE.tex
4de2d4616c38600ec93d48ca589977033e5ad1c1db7431daa09a3d51904454fd  PROOF_LIVE.tex
```
