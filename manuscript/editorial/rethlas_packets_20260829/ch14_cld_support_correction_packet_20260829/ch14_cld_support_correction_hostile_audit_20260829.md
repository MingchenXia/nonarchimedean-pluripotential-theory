# Independent hostile audit: corrected CLD support exponent

Date: 29 August 2026

Verdict: **PASS** for the exact frozen statement and proof.

Audit counts:

- critical mathematical errors: **0**;
- proof gaps: **0**;
- source-scope or citation mismatches: **0**;
- unresolved bidegree/bidimension collisions: **0**.

No statement, proof, or live-book file was edited in this audit.

## Exact frozen bytes

- statement:
  `ch14_cld_support_correction_statement_20260829.tex`, SHA-256
  `2b291fc55872ab32d40fa3a67e9a9308fc12ac9726113b48950d0a9e50cfd8c1`;
- proof:
  `ch14_cld_support_correction_proof_20260829.tex`, SHA-256
  `9f21f7ece49c761d3f19c07acd8b56e48e9939be493e0bbbd39c0a4d3176e668`.

These are the hashes supplied for review and are the exact files audited.

## Frozen-source identity

The citations were checked directly against the frozen sources, independently
of the authoring audit:

- Chambert--Loir--Ducros, arXiv:1204.6277v2 (25 July 2025),
  `CLD25.pdf`, SHA-256
  `f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`,
  and extracted text SHA-256
  `24920a1f4c8bd4944c83d89c8747c95b0206ae0754053eb0ed4d3de95e0f7727`;
- Lagerberg, arXiv:1008.2856v1,
  `Lagerberg12.pdf`, SHA-256
  `90f1cca654529d26a32c7c40f6c7e656102cecc7bd4e9658273fe84c7e491d4c`,
  and extracted text SHA-256
  `1a22c1a28710587e546040361fc5986ef3c3947261a2a7399b0bab62af0f6784`.

The frozen CLD PDF itself cites Lagerberg's published Corollary 4.1 in the
proof of Theorem 16.8.5.  The same result is Corollary 3.5 in the frozen arXiv
version of Lagerberg.

## Degree and Hausdorff-exponent ledger

All four degree conversions in the packet are correct.

1. A current of bidimension `(p,p)` on an `n`-dimensional analytic space acts
   on `(p,p)`-forms.
2. Its proper tropical pushforward to an open subset of `R^N` still has
   bidimension `(p,p)`, hence Lagerberg bidegree `(N-p,N-p)`.
3. Lagerberg Corollary 3.5 applied with bidegree `N-p` gives Hausdorff exponent
   `N-(N-p)=p`.
4. A Bedford--Taylor product of `q` curvature factors on an `n`-space has
   bidegree `(q,q)` and bidimension `(n-q,n-q)`.  Wedging it with an
   `(n-q,n-q)`-form is top degree, and Theorem 16.8.5 therefore forces exponent
   `H^(n-q)`.

Thus the `H^q` printed in CLD Corollary 16.8.6 is incompatible with both the
first sentence of its proof and Theorem 16.8.5, except accidentally when
`n=2q`.  The packet's corrected exponent is exact.

## Nontrivially valued argument

The local proper-pushforward construction is complete.

- Boundarylessness and topological separatedness imply the local holomorphic
  separation needed in CLD Lemma 12.3.6.  The lemma gives the compact analytic
  neighbourhood and separating moment used in the proof.
- Concatenating with a moment tropicalizing the test form preserves boundary
  separation.
- With `Omega=R^N minus trop(boundary V)` and
  `U=trop^{-1}(Omega)`, the map `U -> Omega` is the base change of the proper
  map from compact `V`; it is therefore proper.  Pullbacks of compactly
  supported test forms have compact support, so the displayed definition of
  `T_Omega` is legitimate.
- Pullback commutes with both differentials and preserves positivity.  Hence
  `T_Omega` is positive and closed, with precisely the degree recorded above.
- Lagerberg's coefficient-measure conclusion applies to every compact subset
  of `E=trop(A cap U)`.  Properness makes `E` closed in `Omega`; alternatively,
  intersecting with the compact support of the chosen superform gives a compact
  null set immediately.  Radon inner regularity (or a compact exhaustion of
  the Euclidean open set) therefore gives zero total variation on `E`.
- For a positive test form, `mu=T wedge alpha` is positive and its ordinary
  measure pushforward is exactly `T_Omega wedge omega`, first on smooth compactly
  supported functions and then on all continuous compactly supported functions.
  Thus there is no hidden cancellation in passing from an image-null statement
  back to `A cap U`.
- The standard local decomposition of a symmetric smooth `(p,p)`-form into a
  difference of positive forms, together with the vanishing of the
  antisymmetric part against a symmetric positive current, extends the result
  to arbitrary smooth `alpha`.  Total variation then also vanishes.

The argument uses no unsupported Berkovich ball-growth estimate.

## Trivially valued Gauss--Shilov argument

The scalar-extension chain is correct in every degree, including `q=0`.

- For `0<r<1` over a trivially valued field, the one-element radius is
  `K`-free.  The field `K((varpi))=H(eta_r)` is nontrivially valued and
  universally multiplicative, so the continuous Shilov section exists.
- Pure dimension and boundarylessness are preserved by this base change;
  topological separatedness is preserved as well.  The nontrivial theorem is
  therefore available upstairs.
- CLD Lemma 16.8.7, applied coordinatewise and refined finitely, expresses an
  arbitrary upstairs moment on the Shilov image as a base moment plus an
  integral constant vector times `log r`.  After shrinking around each compact
  piece, all base functions are invertible, so they do define moments.  Finite
  unions and translations preserve `H^p`-nullity.  This proves the exact
  implication from nullity of `A` to nullity of `sigma(A)`.
- For `p=n-q`, the upstairs Bedford--Taylor product has bidimension `(p,p)`.
  CLD Proposition 16.8.2 applies because the pulled-back complementary form has
  bidegree `(p,p)` and gives support on `sigma(X)`.
- CLD Proposition 8.7.5 and the scalar-extension projection formula recalled
  after Proposition 16.8.2 give the stated equality of pushed-forward measures.
  Since `pi^{-1}(A) cap sigma(X)=sigma(A)`, zero total variation on `sigma(A)`
  and the support statement imply zero total variation on `pi^{-1}(A)`, hence
  the desired downstairs conclusion.
- The local expansion of continuous dpsh functions into finite signed sums of
  continuous psh factors is compatible with each of these support, nullity, and
  pushforward statements.

## Convex-kink counterexample

The example has the claimed sign, mass, support, and cutoff behaviour.

- CLD tropicalization uses `log|z|`, so `t=log|z|` is the lattice coordinate
  with the sign used in the packet.
- `h(t)=max(0,t)` is continuous and convex; CLD Proposition 8.2.5 therefore
  makes `h composed with trop` continuous psh.
- Along the canonically calibrated skeleton of the identity torus moment, the
  outgoing slope jumps from `0` to `1` at the unit Gauss point.  Hence its
  distributional Hessian is `+delta_0` with coefficient one.  The identity
  moment has lattice degree one, so there is no additional calibration factor.
- On every residual branch in the fibre `log|z|=0` away from the unit Gauss
  point, the potential is locally constant; there is no additional curvature.
- For a compactly supported smooth test function, restriction to the canonical
  skeleton is compactly supported (the skeleton section is proper).  Both
  boundary terms at infinity therefore vanish, and the two integrations by
  parts give exactly evaluation at the Gauss point.
- A singleton has zero one-dimensional Hausdorff measure in every tropical
  chart, but the curvature assigns it mass one.  It is not `H^0`-null.  Thus the
  example disproves precisely the printed `H^q` exponent for `n=q=1` and is
  fully consistent with `H^(n-q)`.

## Independent compile

The unchanged frozen statement and proof were copied into a fresh temporary
directory and compiled independently with `latexmk -pdf` to convergence.

- output: 4 A4 pages, 219,906 bytes;
- independently generated PDF SHA-256:
  `75e8060027ba5827c3923dadece44e57e45b9abc2b390e8159eccfa55f82ad6c`;
- final log: no undefined references, no undefined citations, no overfull or
  underfull boxes, no package warnings, and no errors.

Visual inspection of all four pages found no clipped or missing mathematical
content.

## Conclusion

The exact frozen packet is mathematically correct and source-faithful.  It is
ready for dependency-closed production verification.  This audit does not by
itself authorize live-book integration; the separately required production
verdict must still be obtained.
