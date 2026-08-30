# P08.1 production dependency ledger

Status: isolated candidate, independently audited at the human level. No live
integration and no production Rethlas submission have occurred.

## Frozen inputs

| input | SHA-256 | staged use |
|---|---|---|
| `/private/tmp/p081_curve_local_global_source_aware_20260830.tex` | `1a552b93d18795044bdb92b61809ecbeffed1e79483e80955fdec2f2aaa1f635` | split without substantive edits into the exact theorem statement and exact proof plus remark |
| `/private/tmp/p081_curve_local_global_hostile_audit_20260830.md` | `69d684ac95e6e4dd49fbb09c3585930762a95c7bca8341a863acbe1822710672` | preserved verbatim as `HOSTILE_AUDIT.md` |

## Proof interfaces

| interface | source keys and exact loci | production firewall |
|---|---|---|
| CLD-current psh to Thuillier subharmonicity | `GR25Classical`, sections 1.2 and 4.1.2; `Wanner19`, Theorem 4.7 and Corollary 4.8 | only in the algebraically closed, complete, nontrivially valued scope |
| metric cocycle and curvature degree | `Thu05`, Definition 3.4.17, Propositions 2.3.20 and 3.3.15 | harmonic frame changes glue local weights as a metric |
| global lisse approximation | `Thu05`, Theorem 3.4.19 and its proof | use the global directed family; uniformity is proved by the net form of Dini, with no cofinal-sequence assumption |
| formal reference and skeleton | `GM19`, section 2.2 and Proposition 2.10; `Thu05`, Proposition 3.2.4 and Lemma 2.2.22 | algebraic closedness removes the finite-extension/descent issue |
| strict G-site obstruction and repair | `Thu05`, Propositions 3.2.4--3.2.5 and Lemma 2.2.22; `GJR26`, Definition 5.1, Corollary 5.9, Example 5.3; `GR25PL`, section 2.5 and warning after Corollary 5.5 | type-III curvature atoms must first be moved to nearby type-II points; Thuillier 3.2.5 alone is insufficient under the strict R-PL convention |
| real model and nefness | `GR25PL`, Proposition 5.1 and proof of Theorem 5.6; `GM19`, Proposition 2.10; `GJR26`, Lemma 7.4 | applied only because the curve is proper and algebraic; positivity becomes nonnegative component degrees on a reduced special fibre |
| real-to-rational nef approximation | elementary rational-polyhedron argument written in Step 5 | remain on one fixed model and approximate inside the rational minimal nef face |
| formal/algebraic/Zhang comparison | `GM19`, Theorem 1.1 | only for the proper algebraic curve; clear denominators for rational models |
| degree-zero case and existence | `GR25Classical`, section 3.12; `Thu05`, Remark 3.4.20 | positive total mass zero gives zero curvature; independent harmonic-metric existence prevents a hidden reference assumption |
| positive-degree ample/FS refinement | `GM19`, Proposition 4.11 | use the explicit rational interpolation `(1-epsilon)N+epsilon A`, then a tensor power |

## Cross-reference ledger

Internal labels preserved exactly:

- `thm:p081-curve-local-global`
- `itm:p081:model`
- `rem:p081-curve-comparisons`

External comparison-only references preserved exactly:

- `thm:p063-current-psh-ordinary-regularization`
- `thm:ch21-continuous-zhang`

There are no `\eqref` dependencies in the staged source. The external
references occur only in the final remark and are not proof inputs.

## Fail-closed production conditions

1. Do not enlarge the theorem to nonalgebraized analytic curves, singular
   curves, trivially valued fields, or non-algebraically-closed fields.
2. Do not delete the movement of type-III atoms before invoking the strict
   R-PL-to-model passage.
3. Do not replace the global metric approximation with unrelated local
   function approximants; the metric cocycle must remain intact.
4. Do not infer ordinary CLD-smooth global approximation in degree zero.
5. Keep BFJ and P06.3 as comparison dictionaries in their separate scopes;
   neither is a base-change or globalization step in this proof.
