# P21.3 scalar-extension/current audit

**Status:** source-scoped negative audit, 9 September 2026.  This records a
scope boundary; it proves neither Bedford--Taylor independence nor a
counterexample and does not retire P21.3.

## Question audited

Suppose a good strict analytic domain becomes an invariant split-toric domain
after a complete extension `L/K`, and the pullbacks of a continuous psh pair
are covered by the invariant toric P21.3 proposition.  Can one descend the
result for an *arbitrary positive closed CLD current* `T` on the original
domain merely from this scalar extension?

The answer supplied by the cited sources is **no automatic descent theorem**.
The following table distinguishes the statements actually available from the
missing current-level bridge.

| Source | Exact available statement | Why it does not supply the P21.3 descent |
| --- | --- | --- |
| Chambert--Loir--Ducros, §11.1.9 | For a complete extension `L/K`, `X_L -> X` is a surjective morphism of ringed sites. | Surjectivity of the analytic base-change map is not a pullback construction for an arbitrary CLD current. |
| Chambert--Loir--Ducros, Props. 15.3.1--15.3.2 | Pushforward identifies the Borel/Radon measures attached to scalar-extended `(n,n)` and `(n-1,n)` **forms**. | These are form/measure statements in the two stated degrees.  They do not define a scalar extension of an arbitrary positive closed `(p,p)` CLD current or prove its faithfulness. |
| Burgos Gil--Gubler--Jell--Künnemann, Prop. 8.4.2 | On a geometrically integral projective variety with an ample line bundle, continuous semipositive metrics are detected after base change and their top-degree Monge--Ampère measures push forward. | Its objects are line-bundle metrics and top-degree measures, not local arbitrary CLD currents nor the mixed current `d'd''(uT)`. |

## Consequence for the manuscript

The invariant split-toric P21.3 theorem is intentionally retained only on an
actual open inverse image under extended tropicalization in a split toric
variety over the ground field.  The scalar-stable P06.1/P06.2 results concern
the **potential** after algebraic-split base change.  They do not by themselves
give an algebraic-split-form version of P21.3, because the proof would still
need all of the following current-level data:

1. a well-defined positive closed CLD current `T_L` above `T`;
2. compatibility of the relevant Bedford--Taylor current with that operation;
3. a faithful descent statement from `d'd''((u_L-v_L)T_L)=0` to
   `d'd''((u-v)T)=0`.

None of these three assertions follows from the three source statements in
the table.  Accordingly, the Chapter 72 text now says explicitly that scalar
extension alone does not enlarge the P21.3 toric subcase.  This prevents an
invalid inference from the scalar-stable P06 results while leaving open the
possibility of a future theorem that constructs and controls such a
current-level base-change formalism.

## Primary-source pins

- A. Chambert-Loir and A. Ducros, *Formes différentielles réelles et courants
  sur les espaces de Berkovich*, arXiv:1204.6277v2 (2025), §11.1.9 and
  Props. 15.3.1--15.3.2, pp. 300 and 424.
  https://arxiv.org/pdf/1204.6277
- J. I. Burgos Gil, W. Gubler, P. Jell and K. Künnemann, *Pluripotential
  theory for tropical toric varieties and non-Archimedean Monge--Ampère
  equations*, Kyoto J. Math. 65 (2025), Prop. 8.4.2, p. 58.
  https://gubler.app.uni-regensburg.de/Publikationen/2102.07392.pdf

The audit deliberately does not infer nonexistence of a stronger theorem from
the absence of one in these passages.  It establishes only the narrower and
operationally relevant claim: the citations currently used in this manuscript
do not justify that stronger theorem.
