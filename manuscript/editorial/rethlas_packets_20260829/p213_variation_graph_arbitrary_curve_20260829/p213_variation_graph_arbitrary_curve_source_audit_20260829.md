# P21.3 arbitrary normal-curve variation-graph audit

Date: 29 August 2026  
Status: quarantine only; no live manuscript edit; no Rethlas verification;
no open-problem retirement and no novelty or priority claim.  The packet
depends on the revised normal-curve localization bytes with statement hash
`335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`
and proof hash
`f6bf21cc24ba593ca097c4facaf4a80c5c5e297ccb341d7a1ab9bd6fa7f429e0`.
The earlier intermediate proof hash beginning `8c432a43` is rejected and is
not a dependency of this packet.

## Outcome

The residual phrase “a normalized component whose non-rig-smooth locus is
not contained in a locally finite rigid set” is not vacuous.  For an
irreducible strict analytic curve, the quasi-smooth locus is Zariski open.
If it is nonempty, its complement is zero-dimensional, hence locally finite
and rigid.  Thus the residual is exactly the nowhere-quasi-smooth case.
The curve

`(A^1_{F_p((t))(t^{1/p})})^an`, viewed over `F_p((t))`,

is normal and nowhere quasi-smooth: its relative differential module has
rank two although its analytic dimension is one.

The virtual-annulus proof cannot handle this example, because Ducros
3.6.35.3 says every virtual annulus is quasi-smooth.  The replacement in the
candidate packet uses the variation graph of analytic units, which Ducros
4.5.21--4.5.22 constructs on an arbitrary analytic curve.

## Exact source audit

| Needed assertion | Exact source and hypothesis |
|---|---|
| Residual curve at type 2 | Ducros 3.3.5.2: projective, normal, integral over the actual degree-one residue field; not necessarily geometrically integral. |
| Branch/closed-point correspondence | Ducros Theorem 4.2.10 and 4.2.11.1: any analytic curve; every closed point occurs exactly when the point is interior. |
| Two branches at type 3 | Ducros 4.2.11.2: at most two in general, exactly two at an interior point. |
| Unit-germ lifting under normality | Ducros 4.2.18: at a nonrigid point of a normal curve, `O_{Y,y}=kappa(y)`; density of `kappa(y)` in `H(y)` is also used in CLD Lemma 12.2.3. |
| Local graph geometry | Ducros Theorem 3.5.1: every analytic curve is a graph. |
| Variation graph | Ducros 4.5.21.1--4.5.21.4: analytic unit on any analytic curve; closed locally finite graph, local constancy off it, piecewise dilation, integral normalized slopes. |
| Node relation | Ducros Theorem 4.5.22: analytic unit on a boundaryless analytic curve. |
| Connected core | Ducros 4.5.11: `Y[2,3]` is convex when normalization is a homeomorphism, in particular for a normal curve. |
| Test support | CLD Proposition 15.1.1(b), followed by the dimension argument in the proof of Proposition 15.2.1(a): an ordinary `(1,1)` form on a curve is supported where `d_K>=1`, namely types 2 and 3. Proposition 15.2.1 itself is stated for G-forms. |
| Proper tropical localization | The base-change argument in the proof of CLD Theorem 16.8.5, after the separately written nonrigid normal-curve repair of CLD Lemma 12.3.6. |
| Current pushforward under target projection | CLD 7.1.11, plus the explicit one-dimensional formula `A_*[u']=q[u]` when `A(u')=qu`. |
| Canonical calibration | CLD 14.3.1--14.3.5: independence of the analytic moment and positivity of the standard calibration. |
| Euclidean support on a graph | Proved inside the packet from the matrix-measure representation: normal first jets eliminate normal rows and columns, tangential divergence gives constant edge densities, and independent value/gradient jets eliminate vertex Dirac matrices and give balancing. |

No Gubler--Jell--Rabinoff statement is used: that paper fixes a nontrivially
valued ground field globally and therefore cannot support the trivially
valued extension.

## Two corrections that must survive verification

1. An order-one residual function need not have normalized slope one on a
   nowhere-quasi-smooth curve.  If `s_P` is a lifted residual uniformizer,
   set `e_b = slope_b(-log|s_P|)`.  The refined valuation of Ducros
   4.2.11.1, together with the branch inequalities of 4.2.6, shows that a
   refined-valuation quotient of secondary value zero has locally constant
   norm.  Therefore
   `slope_b(-log|g_hat|)=e_b ord_P(g)`, and every analytic-unit slope is
   divisible by `e_b`.  Appending `s_P` makes the full slope vector have
   gcd exactly `e_b`; only after saturation is the residual coordinate one.

2. The exact inverse image of a target ray is generally not open.  First
   choose the source tree on which the prescribed and separator blocks form
   a finite linear star; then perform boundary localization entirely inside
   that tree and never shrink the compact domain afterward.  Proper
   pushforward is defined on the full open set `U`.  A sufficiently thin
   ambient open tube meets the tropical support in the desired ray segment;
   its inverse image is the genuine open source tube.  No annular retraction
   is asserted or needed.

## Finite separation without an infinite iteration

For selected residual points `P_i`, weak approximation gives `r_i` with
`ord_{P_j}(r_i)=delta_ij`.  Let `B` be the finite set of all other zeros and
poles of the `r_i`.  One additional rational function `h` is chosen with
order zero at every `P_i` and order one at every point of `B`.  Any further
zero or pole of `h` has zero `r_i`-order by definition of `B`.  The `h`
coordinate therefore separates all old and new exceptional branches from
the selected standard-basis rays in one step.  Riemann--Roch jet
surjectivity proves both approximation statements over a projective normal
integral curve; neither geometric integrality nor a rational point is used.
In the ensuing divisor-functional argument the Riemann--Roch constant is
`chi(C,O_C)`, not `1-h^1(C,O_C)`: over the actual residue base one can have
`H^0(C,O_C)` strictly larger than the base field.

## Hostile-audit outcome and remaining promotion gate

An independent hostile audit found no counterexample.  It accepted the
residual-curve/branch correspondence under mere normality, the
Riemann--Roch separation over the actual residue constant field, the
source-tree repair, and the Euclidean support lemma after the expansions
recorded above.  It also required replacing the earlier appeal to CLD
Proposition 14.4.2, which concerns analytic morphisms, by CLD 7.1.11 and
the explicit segment projection formula.  That correction is present in
the frozen proof.

The remaining promotion gate is a dependency-closed production Rethlas run
on the exact frozen statement and proof.  Until that succeeds, the packet
deliberately does not change the open-problem ledger or any live chapter.

The structural dichotomy and inseparable example are logically independent
of those four promotion gates.
