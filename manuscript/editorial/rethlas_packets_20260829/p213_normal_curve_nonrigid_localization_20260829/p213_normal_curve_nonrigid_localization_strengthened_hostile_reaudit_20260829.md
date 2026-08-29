# Strengthened-byte hostile re-audit: normal-curve nonrigid localization

Date: 29 August 2026

Verdict: **PASS; zero critical errors and zero mathematical gaps.**

This audit concerns the strengthened exact bytes listed below.  It is an
independent quarantine audit, not a production-verification receipt and not a
novelty or priority claim.  The statement and proof were not edited.

## Exact candidate bytes

- statement SHA-256:
  `335532b6a0b71b4174c97246e06cd6ea473d61dd83402fcd709301408692f3db`;
- strengthened proof SHA-256:
  `77da7aa9b84888aad5d6459f04c6b93ca5d9cb273c0d0776c9b7911aa0be3900`.

The primary sources checked were:

- `/private/tmp/p21_bridge_sources/cld25.pdf`, SHA-256
  `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719`;
- `/private/tmp/p21_bridge_sources/ducros_curve.pdf`, SHA-256
  `b514eaa16c0a531880672956d08ee75a4026d75f61303446044468937c9342ad`.

## 1. The unchanged preliminary steps

The affinoid-neighborhood, connected-component, normality, irreducibility,
and identity-principle steps remain correct.

Goodness supplies an affinoid analytic neighborhood inside the prescribed
open set.  A connected component of an affinoid space is a clopen affinoid
domain, and the component containing the chosen point remains an analytic
neighborhood.  CLD 15.2.2 gives holomorphic separation.  Normality passes to
analytic domains, while CLD 11.3.1 identifies the connected components of a
normalization with irreducible components; hence the connected normal domain
`Q` is irreducible.

At a nonrigid point of a normal analytic curve, Ducros 4.2.18 gives

`O_{Y,y}=kappa(y)`.

Consequently, a separator whose value at `y` is zero has zero germ and
vanishes on a nonempty ordinary open subset.  If it were nonzero on `Q`, its
zero locus would be a proper Zariski-closed subset, of dimension zero by CLD
11.2.5, but would contain a nonempty open subset of the pure curve, of
dimension one by CLD 11.2.3.  This contradiction proves that every selected
separator is nonzero at `y`.

The empty-boundary branch is also sound.  CLD 11.4.1 identifies relative
interior for an analytic-domain inclusion with ordinary topological interior
in the target.  Thus `partial(Q/W)=empty` makes `Q` open in `W`; it is already
compact, and the constant unit moment gives the asserted proper localization.

## 2. Exact audit of the displayed `V_j` induction

Proof lines 68--89 are correct.  Put

`B_j=partial(V_j/W)`.

For the composite analytic-domain inclusions

`V_j -> V_{j-1} -> W`,

the middle space `V_{j-1}` is separated.  The composition formula for
relative interiors in CLD (11.4.1.2), after taking complements in `V_j`,
gives the exact equality

`B_j = partial(V_j/V_{j-1}) union (V_j cap B_{j-1})`.

The boundaryless-base-change argument immediately preceding CLD (11.4.2.2),
applied to the upper rational domain

`V_j={|f_j|>=r}` in `V_{j-1}`,

gives

`partial(V_j/V_{j-1}) subset f_j^{-1}(eta_r)`.

Every point in `f_j^{-1}(eta_r)` satisfies `|f_j|=r`.  Therefore

`B_j subset (B_{j-1} cap V_j) union {x in V_j: |f_j(x)|=r}`,

which is precisely the displayed one-step inclusion.  Intersecting the
induction hypothesis with `V_j` retains every earlier level-set contribution
and changes the first term to `partial(Q/W) cap V_j`.  At `j=N` this gives

`partial(V/W) subset (partial(Q/W) cap V)
 union union_i {x in V: |f_i(x)|=r}`.

Thus no boundary term is lost in the iteration.  On a new level boundary,
`|f_i(x)|=r<|f_i(y)|`; otherwise the point lies in the old boundary and one
of the finitely selected separators distinguishes it from `y`.  The full
moment therefore avoids the complete relative boundary.

## 3. Final open/proper localization

The relative boundary is closed in compact `V`, so its tropical image is
compact and therefore closed in Euclidean space.  Hence `Omega` is open.
The inverse image `U` misses `partial(V/W)`, and CLD 11.4.1 identifies the
relative interior with the ordinary interior in `W`; therefore `U` is open
in `W`.  It contains `y` by boundary avoidance.

The continuous map from compact `V` to Euclidean space is proper.  Its
restriction over `Omega` is the topological base change along the open
inclusion `Omega -> R^N`; it is therefore proper.

## 4. Citation precision and residual scope

There is one noncritical citation-label imprecision in proof line 75.
The composition identity used in the displayed induction is most directly
CLD (11.4.1.2), not (11.4.1.3), and the relative-boundary inclusion for an
upper rational domain is proved in the argument immediately preceding
(11.4.2.2), rather than being the literal equality (11.4.2.2) alone.  The
cited section contains both required facts, and the displayed deduction is
correct; this is a bibliographic precision issue, not a proof gap.

The result remains confined to normal pure curves and nonrigid points.  It
does not cover the rigid trivially valued counterexample of CLD Remark
12.3.7.  Subject to the project's required independent production Rethlas
pass, the strengthened exact bytes are mathematically viable.
