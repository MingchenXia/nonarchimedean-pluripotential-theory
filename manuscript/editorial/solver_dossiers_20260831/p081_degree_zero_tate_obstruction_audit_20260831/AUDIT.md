# P08.1 degree-zero Tate obstruction audit

Date: 2026-08-31. Status: isolated exact counterexample candidate, awaiting independent audit and production verification. Nothing in the live manuscript was changed, and this agent made no verifier submission.

## Outcome

The irrational Tate-period mechanism survives the definition and refinement checks. The packet gives a proof candidate that a degree-zero line bundle on a smooth proper geometrically connected curve can have a continuous, even locally CLD-smooth harmonic, metric while having **no nef Q-formal metric on the fixed line bundle at all**.

Let the circle circumference be `ell=v(q)` and let `P` retract to `a=v(u)`, with `0<a<ell` and `a/ell` irrational. For `L=O(P−O)`, the horizontal model has curvature `δ_a−δ_0`. On any competing nef model of `L^m`, zero total degree forces zero curvature at every component. Semistable refinement and tree pruning reduce the correction to two integer slopes `s,t` satisfying

\[
s-t=m,\qquad as+(\ell-a)t=0.
\]

Thus `t=−ma/ell`, contradicting integrality. This is a finite-graph period obstruction, not a failure to choose a sufficiently fine model.

The exact mathematical object to audit is the theorem in `statement.tex` with the complete argument in `proof.tex`. `SOURCE_INTERFACE.md` records the relevant source versions, interfaces and published-page evidence.

## No apparent escape through the checked conventions

| Possible escape | Check |
|---|---|
| Clear denominators by taking a tensor power | For every `m>0`, the required slope is `−ma/ell`, still irrational. |
| Insert more vertices in the two circle arcs | Vanishing curvature forces no slope jump at a newly inserted vertex. |
| Add exceptional components away from the circle | They form finite attached trees; vanishing curvature and leaf pruning force zero slope on all of them. |
| Start with a nonsemistable or nonreduced model | Pass to a common strict semistable model determining the metric ratio; nefness pulls back and the same contradiction applies. |
| Change formal, algebraic, or Q-piecewise-linear conventions | GM19 identifies these on proper varieties after the relevant tensor power. Rational/integer slope constraints remain. |
| Change the reference model | A metric ratio is a global model function. The common-refinement argument is independent of the initially chosen competing model. |
| Multiply the metric by a real constant | This changes no slope or period equation. |
| Enlarge the complete ground field | The values of the fixed `q,u` and their irrational ratio do not change under an isometric extension. Extra model vertices do not change the preceding graph argument after passage to a completed algebraic closure. The theorem only needs the original already algebraically closed field. |
| Use the canonical degree-zero metric | It exists and is CLD-psh with zero curvature, but this is exactly the metric shown not to lie in the fixed-L Q-nef closure. |
| Use real local slopes | This supplies a legitimate local CLD potential, not a Q-formal model of a tensor power of the fixed line bundle. No global real-span assertion is used here. |
| Approximate after an ample twist | That is a different approximation problem and is outside the obstruction. |

As a consistency check, when `a/ell` is rational the displayed slopes become rational. After clearing denominators, the vertex values can be taken in the value group, and the elementary Q-model correction is no longer obstructed. The phenomenon is therefore invisible over fields whose value group is contained in one rational line, such as an algebraic closure of a discretely valued field with its original valuation normalization. The packet does not claim an obstruction over such fields.

## Impact on the supplied P08.1 candidate

The candidate examined was
`manuscript/editorial/solver_dossiers_20260830/p081_arbitrary_field_smooth_curve_proof_candidate_20260830/{statement,proof}.tex`.

If this packet is confirmed:

1. The independent degree-zero existence clause fails: the example has no numerically trivial Q-formal metric.
2. The fixed-L approximation implication for all continuous CLD-psh metrics also fails: the canonical cubist metric meets the hypothesis, while there is no first semipositive Q-formal approximant.
3. The imported algebraically closed approximation theorem in Step 2 cannot be used with unrestricted value group and degree zero; the example is already algebraically closed.
4. The direct invocation of GJKM Theorem 3.1 in Step 4 and the final existence paragraph cannot resolve this boundary case without an additional source-interface justification. The finite-degree ledger in Step 6 is not itself the problem: given a nef model of degree zero, its component degrees really do vanish. The problem is existence of the nef model sequence.
5. Nothing here challenges the elementary mass/degree identity, the harmonicity of degree-zero positive metrics, or the positive-degree branch. Positive-degree repair needs its own proof and verification, including positivity slack when rationalizing slopes.

## Exact GJKM source conflict to audit

The official published Theorem 3.1 still says `nef`, and its proof runs through Proposition 3.10 Step 2. That step asserts nonemptiness of the admissible Q-model set from generic nefness. The printed Definition 2.8 separately makes finite-valuedness equivalent to nonemptiness and explicitly states ampleness as a sufficient condition.

For the reference theta of this example, the competitor set is empty if the counterexample proof is correct. Thus the source-level question is sharply localized: is there any interpretation of the source's model-function or nef definitions that evades the period obstruction? The checked definitions do not provide one. The packet deliberately does not assert a theorem-priority claim, declare a publication error as an audited fact, or imply that an erratum has been conclusively excluded.

## Required next gates

An independent reader should challenge the following in order:

1. Construction of the two-vertex strict semistable Tate model and the horizontal Cartier model with multidegrees `−1,+1`, including nondiscrete valuation rings.
2. Common strict semistable domination for an arbitrary formal metric ratio and preservation of the slope/component formula.
3. The finite graph cancellation, attached-tree elimination and period equations, with sign convention checked against GJKM Proposition 3.7.
4. Exact CLD25 hypotheses for the canonical cubist metric, and the distinction between ordinary local CLD-smooth harmonic weights and globally defined Q-model functions.
5. Whether any convention in the challenged P08.1 statement differs from fixed-L nef Q-formal approximation as formalized in the packet.

After independent approval, the parent may submit the exact frozen files through the recovered strict production verifier. No HTTP status, cancellation, supervisor event or absent response counts as a mathematical verdict. Until both gates are satisfied, this remains a counterexample proof candidate and must not be silently imported into the principal manuscript.

## Frozen theorem/proof hashes

```text
de7bea9cc46e9e7c8dcc5e1ee6b8c58acb33602090a18b44938ed5a9e2d63966  statement.tex
f817525c9226cd6f59832e4bde6f88f8c95ab68d1c35dee6fd07cad4d18e6112  proof.tex
```

No amendment to either frozen file is included in this audit. Any later mathematical change must receive a new hash and a fresh audit/verification pairing.
