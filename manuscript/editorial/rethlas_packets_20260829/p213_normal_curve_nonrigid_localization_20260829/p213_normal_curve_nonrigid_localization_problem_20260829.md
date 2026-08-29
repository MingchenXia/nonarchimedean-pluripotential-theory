# P21.3: boundary-avoiding localization at a nonrigid point of a normal curve

Date: 29 August 2026

This packet is quarantined.  It is not a live-book input and makes no
novelty or priority claim.

## Question

Chambert-Loir--Ducros Lemma 12.3.6 constructs a compact analytic
neighborhood and a moment whose tropical value at the chosen point misses
the tropical image of the relative boundary.  Its published statement
assumes that the ground-field valuation is nontrivial, and Remark 12.3.7
gives a counterexample at the rigid origin of the open unit disc over a
trivially valued field.

The dimension-one current-classification argument only needs this
localization at nonrigid points of a normal curve.  Decide whether the
published proof extends in that scope over an arbitrary complete
non-Archimedean field.

## Candidate mechanism

On a normal analytic curve, Ducros, Section 4.2.18, identifies the ordinary
analytic local ring at a nonrigid point with its residue field.  Hence an
analytic function whose value at that point is zero has zero germ.  On a
connected normal compact analytic neighborhood, normality makes the space
irreducible, and the one-dimensional identity principle then makes such a
function identically zero.  A holomorphic separator of the chosen point
from a boundary point must therefore already be invertible at the chosen
point.  This replaces the sole use of the nontrivial value group in the
proof of CLD Lemma 12.3.6.

## Acceptance conditions

1. The compact neighborhood is an analytic neighborhood inside the
   prescribed open set.
2. Every separator used as a moment coordinate is nonzero at the chosen
   point and becomes invertible on the final compact domain.
3. The relative-boundary inclusion is justified for the simultaneous
   inequalities defining that domain.
4. The proof does not claim a localization at a rigid point over a
   trivially valued field.
5. Exact source locations are supplied for normality of analytic domains,
   the local-ring identification, irreducibility, dimension of a proper
   Zariski closed subset, holomorphic separation, and relative boundaries.

