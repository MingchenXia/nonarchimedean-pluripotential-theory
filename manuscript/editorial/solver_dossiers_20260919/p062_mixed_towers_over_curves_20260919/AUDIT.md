# P06.2 mixed towers over curves — dependency audit

Date: 19 September 2026; updated 20 September 2026 for the split-toric stage

## Claim boundary

The theorem treats only finite towers over the published Wanner curve range.
Every stage must be one of the four already proved locally trivial descent
geometries: a standard strict open-polydisc bundle, a projective-space
bundle, a smooth proper split-toric bundle, or a proper smooth connected
curve bundle.  Projective-space, split-toric, and proper-curve stages retain
the locally holomorphically separated and paracompact base hypotheses of
their source propositions.

## Proof ledger

1. `prop:p062-open-polydisc-bundle-descent`,
   `prop:p062-projective-bundle-descent`,
   `prop:p062-smooth-proper-split-toric-bundle-descent`, and
   `prop:p062-proper-smooth-curve-bundle-descent` each descend a continuous
   zero-current function uniquely to the preceding base.
2. Applying the relevant proposition from the top stage down gives a unique
   continuous zero-current function on the original curve domain.
3. `cor:ch19-continuous-zero-current-harmonic` gives classical
   pluriharmonicity and GJR harmonicity on that curve domain.
4. Classical psh pullback applied to both signs gives classical
   pluriharmonicity upstairs.  Harmonic pullback gives GJR harmonicity and
   local real-PL regularity upstairs.

No current is pulled back along a section, no scalar extension of a current
is asserted, and no residual-Picard vanishing or ordinary CLD-smoothness is
claimed.  Arbitrary fibrations, annular fibres, nonproduct germs, and towers
whose stages lack the displayed local trivializations remain outside the
statement.  P06.2 therefore remains open.
