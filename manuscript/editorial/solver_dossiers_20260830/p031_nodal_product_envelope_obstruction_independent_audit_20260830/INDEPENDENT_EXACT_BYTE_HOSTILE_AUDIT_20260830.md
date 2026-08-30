# Independent exact-byte hostile audit: P03.1 nodal-product obstruction

Date: 2026-08-30  
Audited frozen dossier:
`../p031_nodal_product_envelope_obstruction_20260830/`

## Verdict

**PASS** in the explicitly quarantined, non-production scope.

- Critical errors: **0**
- Mathematical gaps: **0**
- Source-scope/provenance gaps: **0**
- Frozen-byte mismatches: **0**
- Independent compile failures: **0**

The argument proves exactly the two asserted values of the regularized
product envelope, and hence the classical-psh and CLD-v2 obstruction.  It
does not exchange pullback with upper-semicontinuous regularization, does not
claim a formula for the raw envelope away from the zero section, and does not
claim continuity or discontinuity of the higher-dimensional regularized
envelope.

This report is an independent audit only.  It does not modify or authorize
modification of the frozen dossier, the live book, or any production record.

## 1. Frozen-byte gate

The required first command, `shasum -a 256 -c SHA256SUMS`, returned `OK` for
all eight frozen artifacts.  In particular, the two principal hashes are
exactly the hashes specified by the audit request:

| Artifact | SHA-256 |
|---|---|
| `statement.tex` | `cd22f9b56b743506054ad5c9a5f0f64f9a284385509c27cc1c23c85f76b0b5d6` |
| `proof.tex` | `93ea55ab2a14a152ec7ea6008ca84d6984b6ca92fb1a1527af257da11d6974a8` |
| `minimal_compile.tex` | `91e8bbe1d65c9416bd3691822f8767ce5dee9685f61486cd0a1445ebc142ca04` |
| `minimal_compile.pdf` | `0b6802a9dd662d70b240db323da152d527ac71f1c4862b00b3ac82c66d2739ab` |
| `EXACT_BYTE_RELEASE.md` | `e6b0c9e4a4ac3d3e98609514b33cd884e760d5e2e68c6545074f2035cad1a9ec` |
| `README.md` | `b1a143527fd1f071f980f27d765311bb0686abee044970c9b9526d3ef60aa6e7` |
| `SELF_AUDIT.md` | `6e4d536ad0ecde1af02664029f9387b9d580fbf628d683948e471e7d46b201c4` |
| `SOURCE_MATRIX.md` | `b064d8b2b29e88611c505c163b8892ab3f776ecd8773637da7e429441131d8f7` |

The same check was repeated after producing this sibling report and again
returned `OK` for every frozen artifact.

## 2. D1 exact-source verification

The external frozen D1 chain exists in the same snapshot and matches the
source matrix byte for byte:

| D1 artifact | SHA-256 |
|---|---|
| exact statement | `10ac70696f69b1ed18ae1522c0b065fe9240d8f921b9db258201c9e8a7b509e1` |
| exact proof | `21fc22e5b1f3b3084f29df412a57485131e46ca160cf168db18da8a3e2559fc7` |
| request JSON | `9ede30e4244eec02e889377b276b48030d75431324a2b2a04c254dd000e13dc1` |
| API response | `c8ac792474289be20183a6e2c3f8822f0c0bca335cc6f31f07e0bd1004b583bc` |
| combined candidate | `e46a8c4449d6a636361aafa95257c67c6b56426e24d8fa46d2adffcbb0845eab` |

The files are respectively under
`manuscript/editorial/rethlas_packets_20260825/` and
`manuscript/editorial/rethlas_receipts_20260825/` in the frozen snapshot.
The JSON statement is byte-identical to the exact statement file; the JSON
proof is byte-identical to the exact proof file; and the combined candidate
is exactly `statement + newline + proof`.  The response is final with verdict
`correct`, has zero critical errors and zero gaps, and its `proof_digest`
equals the proof hash.

The exact used ranges also check independently:

| Used D1 range | Range SHA-256 |
|---|---|
| statement lines 34--41, raw-envelope values | `7410cf58ab78ea9dc15a047b155add406511b7bd1469ba0611fb70d9de1fce9d` |
| proof lines 78--96, `D_r`, Gauss point, singleton Shilov boundary | `ffa9c47dc825b8ec99c0357794653e69199a73571e0b731879587aece86aed2f` |
| proof lines 144--151, rigid sequence tending to the node | `2d30893f73ee6d21c78f3602c4194c76a5f736b6e257a2e4c2ea3c9aca9e52a8` |
| proof lines 98--107, competitor psh and maximum principle | `de7992c44257a6e7d808cc04f74c20419e4ff4616dcd2ffbb7a36c5bd38f95eb` |
| proof lines 155--166, non-psh and CLD implication | `4127d47177ddce90c1d5cf358c6a00781b6fd8c86afb1dbd37aeaac571e930b1` |

D1 therefore supplies exactly, and no more than, the two raw-envelope branch
values, the convergent rigid sequence, the strict radius-`r` disc and its
unique Shilov point, and the already verified one-dimensional maximum-
principle obstruction.

## 3. D2 primary-literature scope

The D2 facts were checked against these exact primary PDFs already present
in the frozen snapshot:

| Source | SHA-256 | Independent text-extraction SHA-256 |
|---|---|---|
| Gubler--Rabinoff, arXiv:2506.13548v2 | `83ca9a19394f44bb2e4e1aa316de95938f311acd53a00fe250fa0f605184b726` | `091c0fbf66c18ee4925d929f2b5f2aea32a96fee707744aacf9b87099a94acec` |
| Gubler--Jell--Rabinoff, arXiv:2111.05741v3 | `572d51c9f8907dbb814684f7d136612243c0e0b70cddbe6759bb686f0bcfbd42` | `9e6cff8d97426834883ac860f5ecbfb76d987ed3bbebe207dcea3cee2ed3fd23` |

The exact scope is as follows.

1. Gubler--Jell--Rabinoff Lemma 5.4(1) gives forward pullback of real-PL
   functions for arbitrary morphisms of good strictly analytic spaces.
2. Their Proposition 7.6(1) and (1-prime) gives forward pullback of
   semipositivity for the same morphisms.  The relative-interior, properness,
   and surjectivity qualifications occur only in converse directions, none
   of which is used here.
3. Their Definition 7.8 and Section 7.9 identify a locally Fubini--Study
   real-PL function locally as a nonnegative real linear combination of
   finite maxima of logarithms of invertible analytic functions (up to the
   harmless inverse/sign convention).  Pulling back such a presentation
   proves LFS pullback directly.
4. The GJR paper works here over a nontrivially valued field and on good
   strict spaces.  Both `U` and `X_d` are strict affinoids, hence good and
   strict; both `pi` and `j` are analytic morphisms.  No hypothesis is
   missing.
5. Gubler--Rabinoff Proposition 4.2(6) gives forward analytic pullback of
   classical psh functions.  Inclusion of an analytic domain is one such
   morphism.
6. Their Theorem 4.3 identifies semipositive real-valued real-PL functions
   with classically psh functions on good strict spaces over a nontrivially
   valued field.  It provides an alternative derivation of item 2 after
   real-PL pullback.
7. Their Theorem 6.4 says that a classically psh function on any affinoid
   takes its maximum at a Shilov point.  It has no boundaryless hypothesis;
   the proof's use on the strict closed disc is within scope.
8. Gubler--Rabinoff Section 1.2 explicitly records and explains that the
   Chambert--Loir--Ducros v2 psh class is contained in the classical psh
   class.  Thus the final contraposition is in the correct direction.

The dossier correctly says that D2 must be materialized in a future
production request.  That is a production-packaging gate, not a mathematical
or source-scope gap in this quarantined audit: the exact PDFs and exact
locators above are independently available and verified here.  No production
call was made.

## 4. Hostile proof audit

### 4.1 The two pullbacks and the raw section identity

Only forward pullback is used, once for each of the two maps.

- If `h` is a base competitor, `h o pi` is a product competitor and remains
  below `F=f o pi`.  Hence, pointwise on `U`,
  `G o j >= P_U^raw f`.
- If `g` is a product competitor, `g o j` is a base competitor because
  `F o j=f`.  Hence `g o j <= P_U^raw f`; taking the supremum over `g`
  gives `G o j <= P_U^raw f`.

The two inequalities therefore give the claimed equality.  No descent or
converse pullback theorem is used.  The inequality directions in frozen
proof lines 10--20 are correct.

### 4.2 `G^* <= F`

Every competitor is below `F`, so the pointwise supremum satisfies `G<=F`.
D1 states that `f` is continuous; therefore `F=f o pi` is continuous and in
particular upper semicontinuous.  Monotonicity of upper-semicontinuous
regularization yields

`G^*(q) <= limsup_(q'->q) F(q') = F(q)`.

This uses neither continuity of `G` nor any identity between pullback and
regularization.

### 4.3 Ambient node lower bound

D1 supplies rigid points `z_m` on `A\{o}` with `z_m -> o` and raw base value
zero.  The section identity gives `G(j(z_m))=0`, while continuity of `j`
gives `j(z_m)->j(o)` in the ambient product.  Consequently, directly in
`X_d`,

`G^*(j(o)) >= limsup_m G(j(z_m)) = 0`.

The already proved obstacle bound gives the reverse inequality because
`F(j(o))=0`.  Thus `E(j(o))=0`.  The proof never asserts the generally
unavailable equality `G^* o j = (G o j)^*`.

### 4.4 Gauss-point upper bound and maximum-principle contradiction

At the radius-`r` Gauss point of the `y`-branch, the obstacle is exactly
`-a`, so `E<=F` yields `E(j(eta_r))<=-a`.  If `E` were classically psh, GR
Proposition 4.2(6), first along `j` and then along the analytic-domain
inclusion, would make `E o j` classically psh on `D_r`.  The exact D1 disc
calculation shows that the Shilov boundary is the singleton `{eta_r}`.  GR
Theorem 6.4 then gives, in the direction used in the proof,

`E(j(o)) <= E(j(eta_r))`.

This contradicts `0=E(j(o))` and `E(j(eta_r))<=-a<0`.  Since every CLD-v2
psh function is classically psh, failure of classical psh implies failure of
CLD-v2 psh.  Both implications have the correct direction.

### 4.5 Tate algebra, reducedness, purity, and dimension

Let `R=K<x,y,t_1,...,t_d>`.  The quotients `R/(x)` and `R/(y)` are Tate
algebras over a field, hence domains; therefore `(x)` and `(y)` are prime.
For the intersection, if `f=xg` also lies in `(y)`, reduction modulo `(y)`
gives `x*g_bar=0` in the domain `K<x,t_1,...,t_d>`.  Since `x` is nonzero,
`g_bar=0`, so `g` lies in `(y)` and `f` lies in `(xy)`.  The reverse
inclusion is immediate.  Hence

`(x) intersection (y) = (xy)`.

Thus `(xy)` is radical and its two incomparable minimal primes are `(x)`
and `(y)`.  Their quotients are Tate algebras in `d+1` variables, each of
Krull/analytic dimension `d+1`.  These are precisely the irreducible
components, so the strict affinoid `X_d` is reduced and pure of dimension
`d+1`.  With `d>=1`, this gives exactly all dimensions at least two.

### 4.6 Claim firewall

The frozen statement records only the values at `j(o)` and `j(eta_r)`.
The proof records a raw-envelope formula only after restriction to the rigid
zero section.  Neither file asserts a raw formula at points with nonzero
polydisc coordinate.  The statement also does not assert that `E` is
continuous or discontinuous.  The only continuity used is the explicitly
verified continuity of the obstacle `F`.

## 5. Independent compile

The frozen wrapper was compiled independently with `latexmk -pdf`; every
generated file was redirected to
`/private/tmp/p031_nodal_product_independent_audit_build_20260830/`.  The
second pass completed without undefined references, TeX warnings, overfull
or underfull boxes, or fatal errors.

| Independent artifact | SHA-256 |
|---|---|
| PDF | `8cce3d374d6e7e5f08cb82918fd97d57bdf16660e85197761ff511c6bd07b2e5` |
| final log | `8c7fd18ff37e4616dab2e7e17d148bc7f188111f1cefa747215e63c7708bf3ef` |

These build files are outside the frozen dossier and are not part of its
release ledger.

## 6. Release decision

The exact frozen mathematical candidate passes independent hostile audit in
its stated quarantine.  It may proceed to a separate dependency-closed
production packet only after the D1 ranges and the D2 primary-source excerpts
are materialized and frozen in that packet, exactly as `SOURCE_MATRIX.md`
already requires.  This PASS by itself does not authorize live-book
integration.
