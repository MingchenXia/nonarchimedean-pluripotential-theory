# Independent hostile audit of the one-dimensional endpoint argument

Date: 30 August 2026

Auditor status: independent read-only audit of the exact dossier bytes.  The
auditor did not use `AUTHOR_AUDIT.md` as evidence, did not alter the candidate
mathematics, did not call production Rethlas, and did not edit the live book.

## Verdict

**PASS for the one-dimensional closed and half-closed annulus candidate.**

No mathematical gap was found in the asserted one-dimensional endpoint
extension.  In particular, the argument does not rely on the false statement
that the strict radial core is dense in a closed annulus.  It instead proves
the value of the function at every rigid point in every endpoint residue
branch and then uses rigid-point density and continuity.

This verdict does **not** cover the proposed product extension in Section 5.
That extension remains quarantined for exactly the two reasons stated in the
dossier: generalized-base fibre slicing and the multi-endpoint fibre-product
limit have not been audited here.

## Exact bytes audited

- `ENDPOINT_ONLY_DOSSIER.md`:
  `400e598579ded0a9ee1cf90965236a32d3a3e68d971d7b8837a29ba30f9c8145`;
- `REFERENCE_LEDGER.md`:
  `d8edbefc91ea0ee706e6be5d194463bca8e2257186a2cf44d381b60724c1c52c`;
- `README.md`:
  `a547cae20e28436aeb19adf4411ebb4d945dd6eb24c80266e328fc2cc1a4710c`.

The source hashes recorded in `REFERENCE_LEDGER.md` were also recomputed from
the local source files and agree with the ledger.

## 1. Source and topology audit

1. **Baker--Payne--Rabinoff scope.**  Lemma 2.12 in the locally cached
   extraction says exactly that a generalized annulus off its skeleton is a
   disjoint union of open balls, that each component retracts to one skeletal
   point, and that its closure adds precisely that point.  The paper-wide
   hypothesis is that the field is algebraically closed, complete, and
   nontrivially valued.  The dossier correctly refuses to apply this lemma
   directly over arbitrary `K`.

2. **Arbitrary-field branches.**  Ducros 3.6.35.5--3.6.35.6 state the scalar
   compatibility of the analytic skeleton and its retraction.  Ducros
   3.6.35.8 states that the nonskeletal components of a virtual annulus are
   virtual discs and that, after deleting a skeletal point, only the at most
   two skeletal directions are virtual annuli; all other components are
   virtual discs.  These are the precise assertions used in the dossier.

3. **Absolute interior.**  Berkovich, Proposition 1.5.5(i), identifies the
   relative analytic interior of an analytic domain with its topological
   interior.  The equality case in Proposition 1.5.5(ii), applied through the
   good locally separated ambient analytic torus, together with the
   boundarylessness of the analytification of the algebraic torus, identifies
   this relative interior with the absolute interior.  At a closed endpoint
   the Gauss point is not topologically interior because the ambient skeletal
   interval continues through it.  Every nonskeletal endpoint component is
   an open branch in the ambient analytic curve and has constant `|T|=s`.
   Hence

   ```text
   A \ Int(A) = {included endpoint Gauss points}.
   ```

   This is also more than the proof needs: for a rigid endpoint point `y`, the
   polynomial tube used below is itself an ambient-open subset of the torus
   contained in `A`, so it lies in `Int(A)` directly.

4. **Rigid density.**  Berkovich's 1993 book, Section 1.6, explicitly recalls
   from *Spectral theory*, Proposition 2.1.15, that points with finite
   completed residue field are everywhere dense in a Hausdorff strict
   analytic space over a nontrivially valued field.  The standard annuli here
   satisfy those hypotheses.  Thus density may be applied locally on strict
   affinoid neighbourhoods of endpoint branches, without assuming that a
   virtual disc has a `K`-rational point.

## 2. Polynomial-tube audit

Let `y` be rigid with `|T(y)|=s`, and let `P` be the monic irreducible
polynomial of `T(y)`, of degree `d`.  Completeness of `K` makes its absolute
value extend uniquely to every finite extension.  Consequently every root of
`P` in an algebraic closure, counted with inseparable multiplicity, has norm
`s`.  The elementary-symmetric formulas therefore give

```text
|c_i| <= s^(d-i),     |c_0|=s^d=S.
```

If `|T|<s`, the constant term strictly dominates every other term, so
`|P(T)|=S`.  If `|T|>s`, the leading term strictly dominates, so
`|P(T)|=|T|^d>S`.  Hence

```text
X_y={|P(T)|<S} subset {|T|=s}.
```

Since `P(0)=c_0` has norm `S`, this ambient-open tube misses zero and is an
ordinary open analytic subspace of the torus.  It is therefore contained in
the absolute interior of every annulus that includes the endpoint `s`.

The global polynomial morphism is finite free of degree `d`, with basis
`1,T,...,T^(d-1)`.  Base change to the open target disc gives a finite flat
degree-`d` map

```text
X_y -> D^-_S.
```

The zero fibre is `M(K[T]/(P))`, hence is the single analytic point `y`, with
calibrated degree `d`.  These assertions remain valid for inseparable `P`.

The dossier says that `X_y` lies in one endpoint virtual-disc component.  A
short justification, useful in a later theorem packet, is that a connected
component of a finite flat preimage of the connected open disc maps both
open and closed onto that disc; every component would therefore meet the zero
fibre.  Since that fibre is the singleton `y`, there is only one component.
This detail is true but is not needed for the trace argument.

## 3. Singleton Gauss-fibre audit

Because `s` belongs to `|K^x|`, choose `a in K^x` with `|a|=s` and normalize

```text
Q(U)=a^(-d) P(aU),     V=a^(-d) Z.
```

All coefficients of `Q` are power-bounded, while its leading and constant
coefficients are units.  Its reduction `q(U)` therefore has degree exactly
`d`.  At the source and target Gauss points, the induced residue-field map is

```text
\widetilde K(V) -> \widetilde K(U),     V |-> q(U).
```

The element `q(U)` is transcendental, so the source Gauss point maps to the
target Gauss point.  Moreover

```text
[\widetilde K(U):\widetilde K(q(U))]=d,
```

including the inseparable degree: this is the degree of the polynomial map
of rational function fields.  The graded fundamental inequality therefore
makes the analytic local degree at the source Gauss point at least `d`.
Finite flatness says that the sum of all local degrees in the target Gauss
fibre is exactly `d`.  It follows that

```text
bar(p)^(-1)(xi_S)={eta_s},     deg_eta_s(bar(p))=d.
```

Thus neither completion-induced factorization nor an inseparable residue
extension creates an additional boundary-fibre point.

## 4. Current and endpoint-limit audit

The production-verified finite-flat trace input applies: `X_y` and `D^-_S`
are good, separated, strict, pure one-dimensional spaces, and the map is
finite flat of constant degree `d`.  Since `X_y subset Int(A)`, restriction
of the assumed current equation gives

```text
d'd''[Tr_p(h|X_y)]=0
```

on the standard strict open disc.  The production-verified arbitrary-field
open-disc theorem makes this trace constant, and its value at zero is
`d h(y)`.

For `0<q<S`, every point above the target Gauss point `xi_q` satisfies
`|P|=q<S`, hence has `|T|=s` and lies in the domain of `h`.  If a net of such
points did not converge uniformly to `eta_s` as `q` tends to `S`, compactness
of the closed source disc and closedness of the finite map would produce a
limit point other than `eta_s` above `xi_S`, contradicting the singleton
fibre.  The total calibrated fibre mass is always `d`; continuity of `h`
therefore gives

```text
Tr_p(h)(xi_q) -> d h(eta_s).
```

It is important that this is a direct properness-and-continuity argument.
It does not extend `h` to the part of the closed polynomial tube outside the
annulus and does not invoke continuity of a nonexistent closed-disc trace.
The dossier uses the correct direct argument.

Constancy of the open-disc trace now gives `h(y)=h(eta_s)` for every rigid
endpoint point.  On the strict radial core, the already verified strict-open
annulus theorem gives `h=a log|T|+b`; continuity along the Gauss skeleton
gives this value at each included endpoint Gauss point.  Rigid density and
continuity give the same value at every remaining endpoint point.  This
proves all three one-dimensional variants and uniqueness follows from
`r<R`.

## 5. Presentation conditions for a frozen theorem packet

These are not mathematical gaps, but the production packet should make them
explicit to prevent the earlier v2 error from reappearing:

1. state that the closed polynomial tube is the entire closed disc
   `{|T|<=s}`, but only the fibres over `|Z|<S` are used for evaluating `h`;
2. prove endpoint convergence by the compact-complement argument above,
   rather than by applying the finite-trace theorem to a closed restriction
   on which `h` is not defined;
3. either include the one-line connectedness argument for `X_y` or omit the
   unnecessary claim that it lies in a single virtual-disc component;
4. retain the assumptions that the valuation is nontrivial and
   `r,R in |K^x|`.

Subject to those presentation conditions, the one-dimensional candidate is
ready to be frozen and submitted for a new dependency-closed production
Rethlas verification.
