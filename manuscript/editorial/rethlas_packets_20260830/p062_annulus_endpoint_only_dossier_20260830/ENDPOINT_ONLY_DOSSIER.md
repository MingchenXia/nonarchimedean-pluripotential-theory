# P06.2 endpoint-only research dossier

Date: 30 August 2026

Status: **research candidate only; fail closed; not a live-book input and not
Rethlas verified**.

This dossier does not modify the v3 strict-open packet.  It addresses exactly
the endpoint assertions deleted from v2 after production response
`9343e51748df7764fddf021ce2cee6ead02983b2931c95951bae7ad546a9c58c`.
The production response accepted the strict-open annulus and polycylinder
arguments but rejected the claim that the absolute analytic interior of a
closed annulus or polycylinder is merely its coordinatewise strict core.

## 1. Candidate one-dimensional statement

Let `K` be a complete non-Archimedean field with nontrivial absolute value,
and let `0<r<R` lie in `|K^x|`.  Let `A` be any one of

```
{r<|T|<=R},   {r<=|T|<R},   {r<=|T|<=R}.
```

If `h:A->R` is continuous and

```
d'd''[h]=0
```

on the absolute analytic interior `Int(A)`, then there are unique real
numbers `a,b` such that

```
h=a log|T|+b
```

on all of `A`.

The proof below uses only the already established strict-open annulus result,
the arbitrary-field open-disc result, the finite-flat continuous trace, and
standard Berkovich curve topology.  It never pulls back a current under
scalar extension.

## 2. The correct interior and branch decomposition

For each non-strict endpoint `s` (that is, `s=r` or `s=R` when equality is
allowed), let `eta_s` be the `s`-Gauss point and let `B_s` be the set of
branches at `eta_s` which do not point into the annular skeleton.  Write
`U_b` for the corresponding branch component.  Then

```
Int(A)
 = {r<|T|<R}
   disjoint_union (union over closed endpoints s and b in B_s of U_b),
```

and

```
A \ Int(A) = {eta_s : s is a non-strict endpoint of A}.
```

In particular, the strict annulus is not dense in `A`: every `U_b` is an
open endpoint residue branch disjoint from its closure except at `eta_s`.

### Source justification and hypotheses

1. Baker--Payne--Rabinoff, Lemma 2.12, proves over an **algebraically closed,
   complete, nontrivially valued field** that a generalized annulus minus its
   skeleton is a disjoint union of open balls, each retracting to one skeletal
   point and having closure equal to that ball plus the retraction point.  The
   algebraic-closedness hypothesis is stated at the beginning of their paper;
   it must not be silently dropped.
2. Ducros, *La structure des courbes analytiques*, 3.6.35.5--3.6.35.10,
   supplies the arbitrary-field replacement.  In particular, 3.6.35.8 says
   that the components off the analytic skeleton of a virtual annulus are
   virtual discs, and describes the components after removing a skeletal
   point.  The skeleton and retraction commute with complete scalar extension
   by 3.6.35.5--3.6.35.6.  Thus the endpoint residue components above are
   virtual discs over an arbitrary `K`; they need not be standard `K`-discs.
3. Berkovich, *Etale cohomology for non-Archimedean analytic spaces*,
   Proposition 1.5.5(i), identifies the relative analytic interior of an
   analytic domain with its topological interior.  Part (ii), together with
   boundarylessness of `(G_m,K)^an`, identifies this relative interior with
   the absolute interior used by CLD currents.
4. The endpoint Gauss point is genuinely a boundary point: the standard
   skeleton of `(G_m,K)^an` continues past it, so every ambient neighbourhood
   meets the forbidden side of the inequality.  Every other endpoint-radius
   point belongs to one of the ambient-open virtual-disc branches above and
   therefore lies in the topological interior.

This proves the displayed decomposition.  It also pinpoints the exact false
sentence in v2: the absolute interior is larger than `{r<|T|<R}`.

## 3. Endpoint branch rigidity over an arbitrary field

Fix a non-strict endpoint `s` and a rigid point `y` with `|T(y)|=s`.  Let

```
P(T)=T^d+c_(d-1)T^(d-1)+...+c_0
```

be the monic irreducible polynomial of `T(y)` over `K`.  The unique extension
of the absolute value to the finite field `H(y)` gives

```
|c_i| <= s^(d-i),       |c_0|=s^d=:S.
```

Consequently strict dominance gives

```
X_y={|P(T)|<S} subset {|T|=s}.
```

At the `s`-Gauss point, `|P|=S`; hence `X_y` omits `eta_s` and lies entirely
inside one endpoint virtual-disc component of `Int(A)`.  The monic polynomial
defines a finite flat map of degree `d`

```
p:X_y -> D^-_S,       Z=P(T).
```

Let `H=Tr_p(h|X_y)`, with analytic local degrees.  The verified finite-flat
trace theorem makes `H` continuous and gives `d'd''[H]=0` on the standard
strict open disc `D^-_S`.  The arbitrary-field strict-open disc theorem
therefore makes `H` constant.  Since the zero fibre is the single analytic
point `y`, with local degree `d`,

```
H(0)=d h(y).
```

Now extend `p` to

```
bar(p): {|P(T)|<=S} -> D^+_S.
```

The graded Gauss calculation gives

```
bar(p)^(-1)(xi_S)={eta_s},       deg_(eta_s)(bar(p))=d.
```

Indeed the initial polynomial `in_s(P)(U)` has degree `d`; the rational
function extension generated by `U` over the one generated by
`in_s(P)(U)` has degree `d`, including its inseparable part.  The graded
fundamental inequality gives local degree at least `d`, while finite flatness
leaves neither residual degree nor another point in the fibre.

If `q` tends upward to `S`, finite properness and the singleton boundary
fibre force every point of `bar(p)^(-1)(xi_q)` into every prescribed
neighbourhood of `eta_s`.  The total calibrated fibre degree is always `d`,
so continuity of `h` yields

```
H(xi_q) -> d h(eta_s).
```

Since `H` is constant on `D^-_S`, comparison with `H(0)` proves

```
h(y)=h(eta_s).
```

This is the arbitrary-field substitute for the unsafe phrase “apply the
disc theorem to every endpoint branch.”  A branch may be a nontrivial virtual
disc with no `K`-point, so scalar extension of the continuous current is not
available.  The polynomial tube is intrinsic over `K`, and the trace lands in
a standard strict open disc where the verified theorem applies.

Rigid points are dense locally on every strict analytic space (Berkovich,
*Spectral theory*, Proposition 2.1.15, applied on strict affinoid
neighbourhoods).  Therefore the equality above and continuity imply that
`h` is constant with value `h(eta_s)` on every endpoint virtual-disc branch.

## 4. Completion of the one-dimensional proof

On `{r<|T|<R}`, the strict-open theorem gives

```
h=a log|T|+b.
```

Continuity along the skeleton gives the same formula at every included
endpoint Gauss point.  Section 3 gives the same value on every rigid point
of every endpoint branch; local rigid density and continuity give it on all
analytic points of those branches.  The decomposition in Section 2 exhausts
`A`, proving the candidate statement.  Uniqueness follows because
`log|T|` is nonconstant on the nondegenerate skeletal interval.

The argument treats both half-closed cases and the fully closed case.  No
claim is made for a radius outside `|K^x|`; strictness is used both in the
standard-domain topology and in rigid-point density.

## 5. Coordinatewise product extension

The following extension is mathematically plausible and a proof route is
recorded, but it is **not released** from this dossier before an independent
audit of the generalized slicing lemma stated below.

Let `P` be a finite product of standard strict discs and annuli, allowing
open, half-closed, or closed defining inequalities.  Let `h` be continuous on
`P`, with zero CLD Hessian on `Int(P)`.  The expected conclusion is the same
formula as in the strict-open theorem:

```
h=c+sum_j lambda_j log|S_j|,
```

where disc coordinates do not occur.

### Exact local slicing input

The v2/v3 fibre-slicing proof uses only the following properties of the base,
not the fact that it is globally a standard polycylinder:

- the base is good, strict, topologically separated, and pure-dimensional;
- the product projection is flat, boundaryless, and pure of relative
  dimension one;
- compactly supported fibre-smooth tests admit exact ambient extensions;
- strict spaces are very rich, so continuous functions inject into currents.

Under these hypotheses the identical proof gives: if `B` is such a base,
`Z` is a good boundaryless analytic curve, and `u` is continuous on `B x Z`
with zero Hessian, then `u|Z_H(x)` has zero Hessian for every `x in B`.
The proof is not a pullback of currents.  For a compactly supported smooth
fibre test `phi`, density of the ambient germ field in the common completed
residue field produces ambient analytic germs with exactly the same norms on
a smaller fibre neighbourhood.  A finite ordinary-smooth partition gives an
ambient test `Phi` with `Phi|fiber=phi` and support proper over the base.  Put

```
tau=d'd''Phi,       G(t)=integral_(fiber t) u_t tau_t.
```

Uniform smooth approximation of `u`, positive decomposition of `tau`, fibre
integration, and the projection formula show that `G` is continuous and that
its associated current is zero.  Very-rich injectivity gives `G=0`, hence the
fibre current vanishes.  This is the full mechanism used in v3; it applies
locally to the standard endpoint components considered here.

### Product propagation

Fix a coordinate and a base point in the absolute interior of the product of
the other factors.  Choose a good strict open neighbourhood of that base
point contained in the interior.  The local slicing input gives the current
equation on the absolute interior of the one-dimensional fibre.  The verified
closed-disc theorem or the candidate annulus endpoint theorem then says that
the fibre function is constant on a disc and is affine in `log|S_j|` on an
annulus; in particular it is unchanged when an endpoint residue-branch point
is replaced by the Gauss point with the same radius.

If several coordinates lie in endpoint branches, make the replacements one
at a time.  After one replacement lands at an endpoint Gauss point, approximate
that Gauss point along the strict skeletal interval while applying the next
replacement, and pass to the limit by continuity.  This induction reduces
every point to the multivariate Gauss point with the same radii.  The iterated
Gauss norm

```
|sum a_nu S^nu|_s=max_nu |a_nu| product_j s_j^(nu_j)
```

shows that the final point is independent of replacement order.  On the
strict radius rectangle the already accepted strict-open polycylinder
argument gives the affine formula.  Continuity of the multivariate Gauss
section extends that formula to the closed faces.  Absolute interiors of the
standard factors are dense in the factors, so continuity gives the remaining
boundary-Gauss strata.

### Product release blocker

Before promoting the product paragraph to a theorem packet, an independent
exact-byte audit must check two points which the present author audit does not
declare verified:

1. the generalized local slicing statement for a base neighbourhood lying in
   a nontrivial virtual-disc endpoint component, including the exact ambient
   extension of every compactly supported fibre test; and
2. the density/limit induction when more than one coordinate is an endpoint
   Gauss point, formulated on Berkovich fibre products rather than on a naive
   Cartesian product of underlying point sets.

Until those checks pass, only the one-dimensional endpoint result is treated
as a closed research proof; the product extension remains quarantined.

## 6. Fail-closed dependency ledger

- **Passed inside the v2 production review:** strict-open annulus affinity,
  strict-open polycylinder joint affinity, exact product fibre slicing, and
  the iterated Gauss compatibility.
- **Previously production verified:** arbitrary-field open/closed disc
  constancy and the finite-flat continuous trace, in their dependency-closed
  packets.
- **New in this dossier:** the endpoint polynomial-tube application and its
  gluing to the strict-open annulus.
- **Not verified:** the one-dimensional endpoint theorem as a new exact byte
  sequence; the generalized-base slicing formulation; the full product
  propagation.
- **Forbidden shortcut:** no pullback of a general continuous CLD current to
  a completed algebraic closure is used or assumed.
- **Integration gate:** nothing here may enter the live book until frozen,
  independently audited, and accepted by a new production Rethlas run.
