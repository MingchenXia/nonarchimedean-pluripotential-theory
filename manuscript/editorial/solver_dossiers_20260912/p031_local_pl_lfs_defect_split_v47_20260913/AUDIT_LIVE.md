# Live audit: P03.1 local PL--LFS defect split

Audit date: 2026-09-20.

## Integrated scope

The live packet adds exactly four assertions:

1. At an interior point of a good strict analytic space, the local raw
   semipositive real-PL and LFS envelopes agree for every obstacle, including
   simultaneous empty families.
2. In the presence of a global LFS minorant, the LFS globalization defect is
   the sum of the PL globalization defect and the global PL--LFS branch gap.
3. For a locally sectioned finite orbit presentation, the existing PL defect
   balance can be rewritten as a four-defect identity; zero base LFS defect
   closes the whole fibre.
4. If local sections exist near every base point and the base LFS local
   envelope globalizes, all local and global LFS/PL envelopes agree on the
   cover and exact pullback follows.

No P03 atom is retired.  The packet neither constructs local sections for
scalar projection nor proves LFS local-to-global cofinality in the unresolved
higher-dimensional range.

## Statement-to-proof audit

- The local theorem uses an ordinary open PL competitor neighbourhood.  Since
  interiority is local on ordinary open subspaces, Gubler--Jell--Rabinoff,
  Proposition 7.10 applies after restriction.
- The source produces a strictly analytic neighbourhood and uniform LFS
  approximants.  An ordinary open neighbourhood is then chosen inside it, so
  the competitors belong to the local envelope as defined in the book.
- If `epsilon_j` is the uniform error, replacing `v_j` by
  `v_j - epsilon_j` makes the approximation one-sided.  Section 7.9 gives the
  finite-unit description of LFS functions.  Nontriviality of the valuation
  supplies a negative constant of the form `lambda(-log|a|)`, with
  `lambda >= 0`, so subtraction of any nonnegative real constant preserves
  the LFS class.
- The one-sided functions satisfy `u_j <= h <= g` and converge to `h` at the
  chosen point.  This proves the reverse envelope inequality without a
  maximum, gluing argument, or global extension.
- If the PL family is empty then its LFS subfamily is empty; if it is nonempty,
  the construction produces an LFS competitor.  This proves the simultaneous
  empty-family clause.
- A global LFS minorant forces the obstacle to be finite at every point and
  gives finite lower bounds for all four envelopes; the obstacle supplies the
  finite upper bounds.  All defect differences in the packet are therefore
  honest finite real numbers.
- The defect sign was checked directly:
  `Delta_PL = (P_loc - s_LFS) - (s_PL - s_LFS) = Delta_LFS - B`.
  Nonnegativity gives `0 <= B <= Delta_LFS`; zero LFS defect forces both
  summands to vanish.
- Boundarylessness puts every point of the base and cover in the interior, so
  the local cofinality theorem applies at both terms of the existing sectioned
  defect balance.
- In the orbit case, group translates of one local section reach every point
  of the fibre.  The existing envelope chain, zero base branch gap, and zero
  symmetry defect force equality of the cover LFS and PL envelopes; the split
  identity then forces zero cover LFS defect.

## Dependency and exclusion audit

The live proof depends only on the published local approximation result and
the already integrated v40, v41, and v46 identities.  It does not depend on
the quarantined v30 obstacle-preserving lemma, v37 local-envelope package,
v38 collar formula, or the later v48--v49 chain.

The older `STATEMENT.tex` and `PROOF.tex` in this directory remain quarantined.
Their collar and maximal-repair consequences were deliberately not imported,
because they pass through unintegrated v30/v38-era labels and formulas.  The
live packet instead defines the local LFS envelope and both new defects
directly and proves the one-sided approximation from the published source.

No model-backed verifier was used for this packet.

## Verdict

PASS.  The claims are source-supported, hypothesis-complete, internally
closed, and strictly narrower than the unresolved P03.1 assertion.
