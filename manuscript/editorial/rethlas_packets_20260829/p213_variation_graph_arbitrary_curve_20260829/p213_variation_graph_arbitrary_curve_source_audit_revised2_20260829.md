# Second-revision arbitrary-valued normal-curve packet: source audit

Date: 29 August 2026  
Status: quarantine only; no live-book edit, no open-problem retirement, and
no novelty or priority claim.  Both earlier production rejections remain
preserved and controlling for their own exact bytes.  This audit applies only
to the second-revision files with hashes

- statement: e2fdfcc73d777f2cc34f36f3f9c0b6ef7872bcfe35c23a7a7dd83c26422e8695;
- proof: ef986f039dd53c5fe146e3d7d9824c62570a41d32451a1b7c07b9e6a09eaa0c6;
- compile harness: 67bc64efb050ee48233f8d23ecf68b8d6006bf51593518891dcd7604a45b3738;
- compiled PDF: 2d9f5f451574c8604455fe7a546b4fca3dabb910bda292d813cd3a6c4d80b20a.

The eleven-page harness compiles without errors, undefined references, or
undefined citations.  The complete rendered PDF was inspected page by page.
There are two harmless overfull boxes of 0.56pt and 4.69pt.

## Exact disposition of the second production rejection

1. **Actual calibration replaces the slope gcd.**  For an isolated branch
   ray and moment F, the proof now denotes by m_b(F)>0 the actual
   coefficient of the compactly supported pushforward of delta_Y.
   It never identifies this number with the integer slope gcd q_b(F).
   CLD Proposition 14.3.1, §14.3.2, and Definition 14.5.1 define the
   positive canonical calibration through the local finite-flat degree.
   Hence inseparable and nonreduced base-change multiplicities remain in
   m_b(F).

2. **The inseparable test is explicit.**  For
   K=F_p((t)), L=K(t^(1/p)), and the coordinate moment on a type--3
   segment of A^1_L, one has q_b(F)=1 but m_b(F)=p.  This is exactly
   CLD Remark 14.4.3 applied to the degree-p constant-field morphism.
   The intrinsic ratio is now t_b(F)/m_b(F), so the factor p is retained.

3. **Common refinement acts on both currents.**  If H refines F, target
   projection sends the primitive H-ray to r times the primitive
   F-ray, where r=q_b(F)/q_b(H).  Separation excludes contributions
   from other source rays.  Functoriality therefore gives
   t_b(F)=r t_b(H) and m_b(F)=r m_b(H).  This proves moment
   independence without computing either analytic calibration coefficient.
   The same source-germ argument proves cutoff independence.

4. **The type--2 divisor weights are well defined.**  For a residual closed
   point P, restrict to separated moments containing a lift of a residual
   uniformizer.  Every normalized coordinate slope is divisible by d_P,
   while the uniformizer slope is exactly d_P; hence every such moment and
   every common refinement has gcd d_P.  The refinement integer is
   therefore one, so the actual integration coefficient m_P is intrinsic.

5. **Both principal-divisor relations come from balance.**  In a common
   separated moment containing a lift of g and uniformizers at every
   point of Supp(div(g)), the primitive g-coordinate on the branch at
   P is ord_P(g).  Balance of the integration-current pushforward gives
   sum_P m_P ord_P(g)=0; balance of the T-pushforward gives
   sum_P a_P m_P ord_P(g)=0.  Thus P maps to m_P and
   P maps to a_P m_P are nonnegative principal-zero divisor functionals.
   The printed Riemann--Roch argument forces each to be a constant multiple
   of degree, and their quotient makes all branch ratios at a type--2 point
   equal.  No relation between d_P and degree is asserted.

6. **Spatial propagation is proved.**  On a sufficiently short source edge,
   one fixed varying separated moment and one plateau cutoff serve every
   point of a compact subsegment.  The two pushforwards are closed on a
   neighborhood of its target image.  The Euclidean edge decomposition
   makes both coefficients separately constant on that connected target
   edge, hence their quotient is locally constant.  Vertex balance equates
   incident ratios, and a finite cover of a path globalizes the constant.

7. **The cutoff has the required sign.**  CLD Corollary 15.2.5 supplies a
   compactly supported smooth plateau psi, equal to one near the chosen
   compact set.  The proof chooses a scalar smooth rho:R->[0,1] that is
   zero near 0 and one near 1 and sets chi=rho composed with psi.
   Smoothness follows in each moment chart by ordinary smooth composition;
   supp(chi) is contained in supp(psi), and chi is exactly one near
   the source germ.

## Source matrix

| Assertion used | Exact source and hypothesis check |
|---|---|
| Residual curve and branch identification at type 2 | Ducros 3.3.5.2, Theorem 4.2.10, and 4.2.11.1.  The curve is projective normal integral over the actual degree-one residue field; geometric integrality is not used. |
| Two branches at an interior type--3 point | Ducros 4.2.11.2. |
| Lifting residue functions on a normal curve | Ducros 4.2.18 gives O_{Y,y}=kappa(y) at a nonrigid point; strict approximation in the dense subfield preserves a prescribed residue. |
| Refined type--2 branch valuation | Ducros 4.2.6 and 4.2.11.1.  They yield -dlog_b(g-hat)=d_P ord_P(g) and divisibility by d_P. |
| Variation graph and normalized integer slope | Ducros 4.5.21.1--4.5.21.4.  The proof distinguishes the canonical metric derivative from epsilon r [s(b):K]. |
| Normalized node relation | Ducros Theorem 4.5.22, applicable because Y is boundaryless. |
| Compact source plateau | CLD Corollary 15.2.5, applicable because a good separated analytic space is locally holomorphically separated. |
| Compact-support pushforward | CLD 7.1.11; compact current support is explicitly sufficient without global properness of the moment. |
| Actual canonical calibration and inseparable factor | CLD Proposition 14.3.1, §14.3.2, Remark 14.4.3, and Definition 14.5.1. |
| Positivity implies order zero | CLD Proposition 7.2.9. |
| Ordinary top forms live on the type--2/3 locus | CLD Proposition 15.1.1(b) and the dimension argument in the proof of Proposition 15.2.1(a). |
| Connected type--2/3 core | Ducros Theorem 3.5.1, 1.3.5, and 4.5.11. |
| Smooth-locus dichotomy | Ducros 3.1.11 and 3.1.11.4, plus Tate's strict affinoid Nullstellensatz, Theorem 4.5. |

## Remaining gates

This source audit is not an independent hostile audit and not production
verification.  Before any live integration, the exact bytes above must pass
an independent hostile audit with zero critical errors and zero mathematical
gaps, and then receive a final production Rethlas verdict correct on the
same materialized bytes.  Until both gates pass, the packet remains
quarantined.
