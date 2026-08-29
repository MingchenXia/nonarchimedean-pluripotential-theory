# Hostile audit: arbitrary normal-curve variation graph

Date: 29 August 2026  
Verdict: **PASS** on the exact candidate bytes listed below.  Critical
errors: **0**.  Mathematical gaps: **0**.  No counterexample was found.

This is an independent hostile audit of a quarantine packet.  It is not a
production Rethlas receipt, does not authorize live integration or
open-problem retirement, and makes no novelty or priority claim.

## Exact bytes audited

- candidate statement:
  `7b7348ff83ee2d9f4560b868bf30a5cbda28bc374940aff885305a060b593d0c`;
- candidate proof:
  `5ea911448a4044ae71243dcac1617f7307fff6c73b84bce01881fa7a91eeac5a`;
- authoritative dependent localization statement:
  `335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`;
- authoritative dependent localization proof:
  `f6bf21cc24ba593ca097c4facaf4a80c5c5e297ccb341d7a1ab9bd6fa7f429e0`.

The intermediate dependent proof hash beginning `8c432a43` was expressly
rejected and was not used in this audit.

## Hostile checks

1. **Residual branches without quasi-smoothness.**  Ducros's residual curve
   at a type-$2$ point is projective, normal, and integral over the actual
   degree-one residue field, although it need not be geometrically integral.
   The branch/closed-point correspondence in Theorem 4.2.10 and
   Section 4.2.11.1 applies to arbitrary analytic curves; boundarylessness
   supplies all closed points.  Mere normality is enough for the local-field
   identity in Section 4.2.18 and hence for lifting residue functions to unit
   germs.

2. **Common slope factor.**  If $s_P$ lifts a residual uniformizer and
   $\nu_b$ is the secondary $\mathbf Z$-valuation, Section 4.2.6 applied to
   both $q$ and $q^{-1}$ proves that $\nu_b(q)=0$ forces $|q|$ to be locally
   constant on the branch.  Therefore every unit slope is divisible by
   $e_b=\operatorname{slope}_b(-\log|s_P|)$ and a lift of $g$ has slope
   $e_b\operatorname{ord}_P(g)$.  Retaining an order-one coordinate makes
   the saturated residual tangent primitive exactly as asserted.

3. **Finite separation over imperfect constants.**  Simultaneous jet
   interpolation uses only that the residual curve is projective, normal,
   and integral.  A fresh sufficiently positive divisor gives the
   collision-killing function.  No geometric integrality, rational point,
   or perfectness of the constant field is used.

4. **Remote-sheet exclusion.**  The open tree $W_*$ is chosen before
   boundary localization so that the entire $(F_0,S)$-variation graph has
   no vertex away from the centre.  Every arm is therefore linear or
   constant, the named arm is injective in its order-one $S$-coordinate,
   and every other active arm has a different $S$-ray.  After the boundary
   block is known, the target segment is chosen before its first vertex on
   the named arm.  Equality of full moment values implies equality in the
   $S$-block, so no remote arm returns to that segment.  Properness then
   gives the claimed ambient open tube.  The exact ray inverse is never
   asserted to be open, and no annular retraction is used.

5. **Euclidean support theorem.**  A positive bidimension-$(1,1)$ current
   is a symmetric positive-semidefinite matrix of Radon measures.  The
   column-divergence equations, tested with arbitrary normal first jets,
   eliminate normal rows and columns on an edge.  The tangential measure
   has zero distributional derivative and hence constant nonnegative
   density.  At a vertex, independently prescribed values and gradients
   first eliminate a matrix Dirac mass and then give the primitive-vector
   balancing law.  Local finiteness makes the decomposition legitimate.

6. **Refinement and calibration.**  For a linear target projection with
   $A(u')=qu$ on primitive tangents, direct parametrization gives
   $A_*[u']=q[u]$.  Current-pushforward functoriality therefore multiplies
   both the arbitrary-current flux and the canonical flux by the same
   factor.  The ratio is moment-independent.  When both moments retain an
   order-one residual coordinate, their common refinement has expansion
   index one in both projections.

7. **Divisor functional and globalization.**  Node balancing annihilates
   principal divisors.  Riemann--Roch must, and in the proof does, use
   $\chi(C,\mathcal O_C)$ rather than $1-h^1(C,\mathcal O_C)$ over the
   actual constant field.  Positivity for both signs of a degree-zero
   divisor makes every positive principal-invariant functional a
   nonnegative multiple of degree.  This equalizes all branch ratios at
   type-$2$ points; the two-branch identity does so at type-$3$ points.
   Ducros's graph theorem and convexity of the nonrigid core of a normal
   curve make that core nonempty and path-connected, completing the
   propagation.

## Scope retained

The classification concerns ordinary CLD currents on connected good
separated normal boundaryless pure analytic curves over an arbitrary
complete non-Archimedean field, possibly trivially valued.  It does not
claim the weakly smooth/harmonic-tropical analogue and does not supply
conductor descent for a reduced nonnormal curve.  A dependency-closed
production Rethlas run on the exact candidate statement and proof remains
mandatory before promotion.
