# Revised arbitrary-valued normal-curve packet: exact source audit

Date: 29 August 2026  
Status: quarantine only; no live-book edit, no open-problem retirement, and
no novelty or priority claim.  The first production run returned `wrong`.
Its statement and proof remain unchanged under their original filenames.
This audit applies only to the revised files with exact SHA-256 hashes

- statement: `8c736e3df2df1efd7b6925dd4edccddfcf03cc1ee0b68250bd1219f80169be5a`;
- proof: `9cb4d5eef1370ef97ccf1fa51e9ece16ab418c44092df61bd1a403f3f1d99ed9`;
- compile harness: `8bf258fbc4044a654269359df965461df14dbb0544570be0c2ea4d0ce68e1f3c`;
- compiled PDF: `bfc27267e9100a47e4d844f569f4d7c1c4b8952ef18ba639280c09a9d5b7ffe8`.

The ten-page harness compiles without undefined references, undefined
citations, or errors.  Its few overfull boxes are typographical only.

## Disposition of every production objection

1. **Metric slope versus normalized integral slope.**  Ducros 4.5.21.4
   defines
   `dlog_b |f| = epsilon r [s(b):K]`, where `r` is the canonical-metric
   dilation.  The revised proof never identifies `r` with an integer.  It
   forms the lattice vector from the integers `-dlog_b |f_j|`.  Its gcd is
   `q_b`, its primitive target tangent is the integer vector divided by
   `q_b`, and the source metric derivative is the integer vector divided by
   `[s(b):K]`.

2. **Remote sheets and the asserted global ambient tube.**  The global
   tube has been deleted.  After the finite moment is fixed, its variation
   graph is shrunk to a finite source star.  CLD Corollary 15.2.5 supplies a
   nonnegative smooth source cutoff `chi`, equal to one near the node and
   compactly supported in that star.  CLD 7.1.11 defines the pushforward of
   `chi T` because its support is compact.  On the target germ its
   differential is the pushforward of `dchi wedge T`.  Transition points on
   active arms have target image away from the vertex; off the variation
   graph the moment is locally constant, so every positive-degree target
   test form pulls back to zero.  This proves germwise closedness and makes
   remote source sheets irrelevant.

3. **Branch coefficients.**  The separated finite fan is now produced only
   after source localization.  Thus a selected ray germ has one source arm.
   Common concatenated moments give the exact expansion relation
   `A u_H=(q_F/q_H)u_F`; both the current edge coefficient and the canonical
   integration coefficient are multiplied by this same positive integer.
   Their ratio is therefore intrinsic.

4. **Normalization-locus equivalence.**  It has been removed.  The revised
   dichotomy is a statement on the given irreducible strict reduced curve
   only, so no unproved transfer through normalization remains.

## Source matrix

| Assertion used | Exact source and hypothesis check |
|---|---|
| Residual curve at a type--2 point | Ducros 3.3.5.2: projective normal integral curve over the actual degree-one residue field; geometric integrality is not asserted or used. |
| Branches as closed residual points | Ducros Theorem 4.2.10 and 4.2.11.1; because the point is interior, every closed point occurs. |
| Two branches at an interior type--3 point | Ducros 4.2.11.2. |
| Lifting residue functions on a normal curve | Ducros 4.2.18 gives `O_{Y,y}=kappa(y)` at a nonrigid point; density of `kappa(y)` in `H(y)` preserves a chosen residue under a strict approximation. |
| Refined branch valuation at type 2 | Ducros 4.2.6 and 4.2.11.1: composition of the primary absolute value with the discrete valuation at the residual closed point.  Applying 4.2.6 to a secondary-value-zero quotient and its inverse makes its norm locally constant. |
| Variation graph | Ducros 4.5.21.1--4.5.21.2: closed locally finite graph, local constancy off it, and piecewise dilation on it, for an analytic unit on an arbitrary analytic curve. |
| Normalized integer slope | Ducros 4.5.21.4: `epsilon r [s(b):K]`, invariant under completed perfect closure and reduction, and equal to the branch degree in the generically quasi-smooth reduction. |
| Node relation | Ducros Theorem 4.5.22, valid for analytic units on a boundaryless analytic curve. |
| Compact source cutoff | CLD Corollary 15.2.5, applicable because a good separated analytic space is locally holomorphically separated. |
| Pushforward with compact current support | CLD 7.1.11 explicitly permits a nonproper morphism when the current support is proper over the target; compact support is a stated special case. |
| Canonical integration coefficient | CLD Proposition 14.3.1 and 14.3.2 define the one-dimensional canonical calibration by the finite-flat degree after projection to a primitive coordinate.  Combined with Ducros 4.5.21.4, that degree is `q_b`. |
| Positivity and order zero | CLD Proposition 7.2.9. |
| Support of ordinary `(1,1)` forms on a curve | CLD Proposition 15.1.1(b), plus the dimension argument in the proof of Proposition 15.2.1(a). |
| Connected type--2/3 core | Ducros Theorem 3.5.1, 1.3.5, 4.5.11; normality makes the normalization a homeomorphism, hence the type--2/3 locus is convex. |
| Smooth-locus dichotomy | Ducros 3.1.11 and 3.1.11.4, together with the strict affinoid Nullstellensatz in Tate, Theorem 4.5. |

## Independent algebra checks inside the packet

- Jet separation uses only Serre vanishing/Riemann--Roch on a projective
  normal integral curve.  The pole divisor is chosen disjoint from all
  prescribed closed points, and the required first jets and values are
  imposed by a surjective finite jet-evaluation map.
- If `d_P=-dlog_{b_P}|s_P|`, then
  `-dlog_{b_P}|g_hat|=d_P ord_P(g)`.  The node relation makes
  `P -> d_P` annihilate principal divisors.  Positivity plus Riemann--Roch
  then proves, rather than assumes, `d_P=c deg(P)`.
- For the current, balance of the separated cutoff pushforward gives the
  same principal-divisor relation for `P -> a_P d_P`.  Riemann--Roch forces
  it to be another multiple of degree, so all branch ratios `a_P` coincide.
- The Euclidean graph-current lemma is proved in the packet from matrix
  Radon measures: normal test jets remove normal rows and columns,
  tangential divergence makes edge densities constant, and independent
  value/gradient jets eliminate a vertex Dirac matrix and impose balancing.

## Remaining promotion gates

This source audit is not production verification.  The exact revised bytes
received an independent hostile-audit verdict `PASS`, with zero critical
errors, zero mathematical gaps, and zero citation mismatches; the record is
`p213_variation_graph_arbitrary_curve_hostile_audit_revised_20260829.md`.
Before any live integration, these same bytes must also receive a production
Rethlas verdict `correct`.  Until that final gate passes, the theorem remains
quarantined.
