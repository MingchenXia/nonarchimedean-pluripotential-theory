# P07.1 Stone-parameter × convex-polyhedral-corner candidate, v2 source ledger

Date: 30 August 2026

Status: **source-repaired quarantined sibling**.  The principal mathematical
bytes are unchanged from v1.  No production submission and no live-book edit
was made.

## Frozen mathematical identity

| File | SHA-256 | Relation to v1 |
|---|---|---|
| `statement.tex` | `b46b8e22fa8b3f8f64dcf8ae24d164b905dbe8d9035e37c3ede23321717cc002` | byte-for-byte identical |
| `proof.tex` | `37a3b6a12f6ddd2a3038dd926dfe8120d8955756efe64608fbd2a37b33c01efb` | byte-for-byte identical |

## Reproducible primary-source chain

The old v1 ledger fingerprint
`f659b1fd1423baba9552c03e4738f59e5ee985df0bbf671c8ce9d9718a5d0629`
is withdrawn: it does not identify the file at the recorded path and is not
used anywhere in this v2 release.

The source actually audited in v2 is:

| Artifact | Identity |
|---|---|
| Chambert--Loir--Ducros, *Formes différentielles réelles et courants sur les espaces de Berkovich*, arXiv:1204.6277v2, 25 July 2025 | title page of the pinned PDF; 608 pages |
| Pinned PDF | `/private/tmp/CLD25_1204.6277.pdf` |
| PDF SHA-256 | `5690f999523017d184ab751bb55857ab1637b197d1186ad4fd2edba7e1bda719` |
| Extraction command | `pdftotext -layout /private/tmp/CLD25_1204.6277.pdf /private/tmp/CLD25_reextracted_layout_p071_20260830.txt` |
| Regenerated extraction SHA-256 | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |
| Navigation extraction used for the audit | `/private/tmp/CLD25.txt` |
| Navigation extraction SHA-256 | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |
| Exact comparison | `cmp -s` exit status `0`; the two text files are byte-for-byte identical |

Thus the exact source path, source bytes, extraction procedure, and audited
navigation bytes form one closed chain.

## Primary-source ranges and exact use

Line numbers below refer to the pinned `pdftotext -layout` extraction whose
SHA-256 is recorded above.

| ID | Extracted line(s) / printed section | Exact use | Scope boundary |
|---|---|---|---|
| S0 | line 2165, CLD §1.8.2 | standing parlinear parameters (K=\mathbf Q\), (G=\mathbf R) | no assertion for a different parameter pair |
| S1 | CLD §§1.8.3--1.8.10 | closed cells, polyhedra, affine spans, and induced parlinear subspaces | the candidate uses one convex chamber |
| S2 | lines 2392 and 2473, CLD §§1.9.3--1.9.6 | smooth functions/forms on a parlinear subspace are local ambient restrictions | no piecewise-smooth enlargement |
| S3 | line 2628, CLD Definition 1.10.1 | positivity is tested on cells; for one convex cell spanning (A), (mathrm d'\mathrm d''F\geq0) is the positive-semidefinite Hessian condition on (A) | the affine span, not the original (E), controls lower-dimensional (P) |
| S4 | line 7045, CLD Example 6.1.4 | a parlinear subspace has its induced affine tropical structure | only the standard induced structure |
| S5 | line 7069, CLD Definition 6.2.1 | smooth functions are defined through affine tropical charts | used together with S2 |
| S6 | lines 11236--11273, CLD §§9.1.1--9.1.4 | product (G)-tropical and affine structures | after a clopen shrinking, the Stone coordinates are constant |
| S7 | lines 9723 and 9757, CLD Definition 8.1.1 and Lemma 8.1.4 | generated psh sheaf and ordinal stages, including the first local decreasing-limit stage | no claim about arbitrary unrelated hierarchies |

## Legality of the Stone factor

The detailed verification that an arbitrary locally compact Hausdorff
clopen-base space, with locally closed domains and locally constant
parlinear/affine functions, is an affine (G)-tropical space appears in the
already verified Stone--Euclidean packet:

`manuscript/editorial/rethlas_packets_20260830/p071_stone_euclidean_collapse_20260830/`.

Its relevant exact identities are:

| Artifact | SHA-256 / verdict |
|---|---|
| `statement.tex` | `dfd8c7cc9d6d26f50260707975ff62d4f292627f084400bcd37b32253c876cdc` |
| `proof.tex` | `9316e1a9df86c73a68ec099d3254e451ceaaac17a15c2a92441ad44961d863f6` |
| independent exact-byte audit | `a7a88e7e8703d4a915fe174c008ed45ef2c01d344aa18ddd3f3966495d27d58e`; PASS |
| production response | `ef9be00d4ed1462f11068a2b99a2c7fbe366af2b3bd180850b6763db541c3d6a`; `correct`, zero critical errors, zero gaps |

The polyhedral-corner candidate changes only the Euclidean chamber.  CLD
S1--S6 identify its abstractly defined generator sheaf with the product
generator sheaf for a rational convex polyhedron with the standard induced
structure.

## Internal proof obligations carried unchanged from v1

The v1 independent hostile audit, SHA-256
`1d74c658835a2a9459350bc7e4509b7fbed3686b2c9bde9d31f24465242c3045`,
found zero critical mathematical errors and zero unresolved proof gaps.  In
particular it checked:

1. local extended-real convexity, polar faces, and zero-weight conventions;
2. continuity of the convex envelope at every polyhedral face and corner;
3. the countable Boolean quotient without metrizability of the Stone factor;
4. upper-semicontinuity descent through compact fibres;
5. fixed-domain sup-regularization, fibrewise convexification, and clopen
   approximation;
6. simultaneous smooth convex majorants on one compact polyhedral core;
7. exact monotonicity after summable tail correction;
8. lower-dimensional, unbounded, and zero-dimensional polyhedra;
9. chart-local transport under generator-preserving charts;
10. the firewall excluding nonconvex and branched face gluings.

Because v2 has identical principal bytes, those mathematical findings apply
without alteration.  The new exact-source recheck closes the sole v1 release
blocker.

## Scope firewall

The candidate proves no result for a nonconvex union of chambers, a branched
polyhedral complex, cellwise positivity without a single convex product
chart, nonconstant affine directions on the Stone factor, an arbitrary CLD
boundary structure, or an arbitrary affine (G)-tropical space.  A
“polyhedral manifold with corners” is covered only when its complete germ and
generator sheaf are generator-preservingly identified with one of the stated
convex product models.  P07.1 remains active.
