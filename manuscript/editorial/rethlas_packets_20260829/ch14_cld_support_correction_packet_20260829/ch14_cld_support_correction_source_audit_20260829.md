# Exact-source audit: CLD support exponent and proof route

Date: 29 August 2026

Status: **PASS for quarantine**.  No live chapter was edited.  This is the
authoring/source audit; an independent hostile audit and a production Rethlas
verdict are still required before integration.

Audit counts for the frozen theorem packet:

- critical mathematical errors: **0**;
- proof gaps found in this audit: **0**;
- source-scope mismatches: **0**;
- unresolved bidegree/bidimension collisions: **0**;
- uses of the unsupported ball-growth sketch: **0**;
- uses of the exponent printed in CLD Corollary 16.8.6: **0**.

## Frozen candidate

- statement: `ch14_cld_support_correction_statement_20260829.tex`, SHA-256
  `2b291fc55872ab32d40fa3a67e9a9308fc12ac9726113b48950d0a9e50cfd8c1`;
- proof: `ch14_cld_support_correction_proof_20260829.tex`, SHA-256
  `9f21f7ece49c761d3f19c07acd8b56e48e9939be493e0bbbd39c0a4d3176e668`;
- compile harness: `ch14_cld_support_correction_compile_20260829.tex`,
  SHA-256
  `ec4560404ef29457628d6b18d61e7201ea34a2814ceef7f1439f4a3bcd3d32f3`;
- clean four-page compile:
  `ch14_cld_support_correction_compile_20260829.pdf`, SHA-256
  `01c4e1ba5f15fb102f6b549bb4bf3f1137d9e892abd2a9b965fecd390347ec88`;
- proposed bibliography addition:
  `ch14_cld_support_correction_bibliography_addition_20260829.bib`,
  SHA-256
  `89ef92576064095a9d9fa7e1d84892c862b5c24760569d777f70cfd0abfc8602`.

The final LaTeX log has no undefined references, undefined citations,
overfull boxes, underfull boxes, or errors.

## Frozen sources

The exact Chambert--Loir--Ducros source is shared with the earlier index
audit at
`../p213_trivially_valued_curve_candidate_audit_20260829/sources/`:

- `CLD25.pdf`, arXiv:1204.6277v2, 25 July 2025, SHA-256
  `f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`;
- `CLD25.txt`, SHA-256
  `24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727`.

The Euclidean source frozen in this packet is:

- `sources/Lagerberg12.pdf`, arXiv:1008.2856v1, SHA-256
  `90f1cca654529d26a32c7c40f6c7e656102cecc7bd4e9658273fe84c7e491d4c`;
- `sources/Lagerberg12.txt`, SHA-256
  `1a22c1a28710587e546040361fc5986ef3c3947261a2a7399b0bab62af0f6784`.

The publication metadata were checked against the author's institutional
record: A. Lagerberg, *Super currents and tropical geometry*, Math. Z. 270
(2012), no. 3--4, 1011--1050,
doi:10.1007/s00209-010-0837-8.

## Index audit

CLD uses the following data in Section 16.8:

| Source | Object | Degree datum | Hausdorff exponent |
|---|---|---|---|
| Theorem 16.8.5, extracted lines 23629--23670 | positive closed current | bidimension `(p,p)` | `H^p` |
| Corollary 16.8.6, lines 23671--23698 | product of `q` curvature factors | bidegree `(q,q)`, hence bidimension `(n-q,n-q)` | printed `H^q`, but Theorem 16.8.5 forces `H^(n-q)` |
| Proposition 16.8.2, lines 23594--23628 | scalar-extended product of `q` factors wedged with an `(n-q,n-q)`-form | top-degree measure supported on the Shilov image | no Hausdorff exponent |

Thus the packet's two assertions use different letters on purpose:

```text
nontrivial theorem:        p = bidimension;
trivial BT extension:      q = number of curvature factors;
forced substitution:       p = n-q.
```

The proof of CLD Corollary 16.8.6 begins by calling the nontrivially valued
case a special case of Theorem 16.8.5 (lines 23675--23677).  That sentence
itself forces the substitution `p=n-q`; it is incompatible with the printed
exponent except when `n=2q`.

## Nontrivially valued proof route

The packet reconstructs the actual route of CLD Theorem 16.8.5 rather than
the unsupported ball-growth argument presently in the live chapter.

1. CLD Lemma 12.3.6 (lines 17358--17382) supplies a compact analytic
   neighborhood `V` and a moment separating the chosen point from
   `trop(boundary V)` when the valuation is nontrivial.
2. With `Omega=R^N\trop(boundary V)` and
   `U=trop^{-1}(Omega)`, the restriction `U -> Omega` is proper.  CLD's proof
   makes exactly this construction at lines 23633--23648.
3. The formula `<T_Omega,beta>=<T,trop^*beta>` defines a positive closed
   Euclidean supercurrent of bidimension `(p,p)`; see lines 23647--23652.
4. In Lagerberg's bidegree notation this is a current of bidegree
   `(N-p,N-p)`.  His published Corollary 4.1 says its coefficient measures
   vanish on sets of zero `p`-dimensional Hausdorff measure.  In the frozen
   arXiv version this is Corollary 3.5, extracted lines 1124--1147; its
   monotonicity input is Proposition 3.4, lines 1075--1122.
5. The packet then uses ordinary pushforward of a **positive** measure to
   return to `U`.  It first decomposes an arbitrary symmetric smooth form
   into a difference of positive smooth forms.  This removes the possible
   signed-measure cancellation hidden in a bare image argument.

No estimate of the form `mu(B(a,r)) <= C r^p` on a Berkovich chart is
asserted or used.  The only monotonicity theorem is the precise Euclidean
one inside Lagerberg's cited result.

## Trivially valued proof route

The exact Gauss--Shilov chain is source-supported as follows.

| Claim | Exact source |
|---|---|
| The one-radius free Gauss field and its nontrivial norm | CLD Example 11.1.3, extracted lines 14925--14936 |
| Universal multiplicativity and the continuous Shilov section | CLD Section 12.7.4 and Corollary 12.7.5, lines 17930--17977 |
| Pure dimension under scalar extension | CLD Section 11.2.5, especially lines 15402--15406 |
| Boundarylessness under scalar extension | CLD Section 11.4.1, lines 15501--15528 |
| Comparison of a scalar-extended moment on the Shilov image with finitely many base moments | CLD Lemma 16.8.7, lines 23699--23712 |
| Support of the scalar-extended Bedford--Taylor measure on the Shilov image | CLD Proposition 16.8.2, lines 23594--23628 |
| Exact Bedford--Taylor pushforward | CLD Proposition 8.7.5, lines 10473--10482, and the reminder after Proposition 16.8.2 at line 23603 |

The degree check for Proposition 16.8.2 is exact: with `q` curvature
factors, the complementary form has bidegree `(n-q,n-q)`, so its `max(u,v)`
is exactly `n-q`, the lower bound in that proposition.

The proof that `sigma(A)` remains tropically `H^(n-q)`-negligible is not
left implicit.  It applies Lemma 16.8.7 coordinatewise, refines the finitely
many compact pieces, and observes that translations by
`e_lambda log r` preserve Hausdorff measure.  This is the mechanism used in
CLD's proof at lines 23683--23690.

## Counterexample audit

Take the complete trivially valued algebraically closed field `K` and
`X=G_m,K^an`.  With `t=log|z|`, the function `max(0,t)` is tropical convex,
hence CLD-psh by Proposition 8.2.5 (lines 9971--9977).  The distributional
identity

```text
d'd'' max(0,t) = delta_0
```

has coefficient one because the slope jumps from `0` to `1`.  CLD Theorem
8.10.3 (lines 10867 onward) identifies the corresponding analytic current
with the zero-dimensional skeletal current at the unit Gauss point.  The
packet also checks the normalization directly by two integrations by parts.

Every tropicalization sends a singleton to a singleton or the empty set, so
the unit Gauss point is tropically `H^1`-negligible.  Its curvature mass is
one.  For `n=q=1`, the printed exponent `H^q=H^1` therefore gives a false
conclusion, while the corrected exponent `H^(n-q)=H^0` does not apply to a
nonempty singleton.

## Scope

The packet corrects a source index and replaces a non-source-faithful proof
sketch.  It does not claim a new support theorem.  It is quarantined and must
not be copied into the live chapter until exact-byte hostile review and
production Rethlas verification both pass.
