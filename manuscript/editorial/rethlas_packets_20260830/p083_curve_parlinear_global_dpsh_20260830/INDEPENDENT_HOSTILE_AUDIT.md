# P08.3 independent hostile audit

## Exact-byte target

This audit was performed against the frozen files in this directory:

| Artifact | SHA-256 before this audit |
|---|---|
| `statement.tex` | `ae3042f558e649bfd2f54a00287901978558defa6a6aa4be52e63f9461c466be` |
| `proof.tex` | `5a35c88f774aca391fa6c38acbbc5cb0c7ea5956efbdc370d129fbdc365bec80` |
| `SOURCE_MATRIX.md` | `fdb9c5f797330e7ea1328ca64ad0875e7ef9d569d79ed7eaa10bf49440cda61a` |
| `HOSTILE_SELF_AUDIT.md` | `68ce3f97edbac21aaebaa231d19c3e951c17e97fa458659bcd581d1a055ffbc0` |

## Verdict

**PASS on the mathematics and on all seven requested obligations.  There
are no fatal gaps.**  There are three nonfatal source-ledger defects, listed
precisely below.  None changes the proposition or its proof.

## Obligation-by-obligation audit

### 1. Parlinear to Thuillier-lisse; finite atomic curvature — PASS

CLD, immediately after Definition 17.8.1, states that parlinear metrics are
G-lisse (and dpsh).  Thuillier Proposition 3.2.5 identifies the lisse sheaf
on the G-site with the sheafification of real linear combinations of
`log|f|`; Proposition 3.2.4 gives the piecewise-affine-on-skeleta
description.  Definition 3.2.1(ii) defines degree-one lisse forms as real
measures with locally finite support in `I(X)`.  Since the proper analytic
curve is compact, a locally finite subset is finite.  Thus lines 16--26 of
`proof.tex` correctly produce a finite signed atomic measure supported at
type-II/type-III points.  This step is genuinely one-dimensional and the
frozen statement keeps that firewall.

### 2. Thuillier Green functions and prescribed curvature — PASS

Thuillier Proposition 3.3.7(i) gives, for `x,y in I(X)` on a proper
connected smooth strict curve, the unique lisse function normalized by
`g_{x,y}(x)=0` and satisfying

`dd^c g_{x,y} = delta_y - delta_x`.

Remark 3.4.20 gives on `O(D)`, for effective `D`, a lisse subharmonic
reference metric with curvature `deg(D) delta_x`.  For the finite atomic
measure `nu=sum a_y delta_y`, the finite sum in lines 79--88 has

`dd^c(sum a_y g_{x,y}) = nu - d delta_x`.

Multiplication of the norm by `e^{-u}` therefore changes the curvature by
`+dd^c u` and gives exactly `nu`.  No theorem asserting a lisse potential
for an arbitrary diffuse measure is being imported.  The isolated
opposite-sign display in Thuillier Definition 3.4.17 is internally
inconsistent with its own `-log||s||` convention, Proposition 3.4.4,
Corollary 3.4.18, and the operational formulas of Remark 3.4.20; the frozen
proof correctly avoids that display and fixes its sign independently.

### 3. Poincare--Lelong and total mass — PASS

Thuillier Proposition 3.3.15 states

`dd^c log|f| = delta_div(f)`.

With the CLD weight `phi_e=-log||e||` and `s=f e`, one has
`phi_s=phi_e-log|f|`, hence

`c_1(L,h)=dd^c phi_s + delta_div(s)`.

Testing the exact current against `1` on the proper curve gives zero, and a
nonzero rational section of the algebraic line bundle `M` has divisor of
degree `deg M`.  Thus `mu(X)=deg M`.  Algebraic closedness also removes any
closed-point residue-degree normalization in the later choice `D=d[p]`.

### 4. Positive/negative decomposition and degree calculation — PASS

For `mu=mu^+-mu^-`, `m=mu^-(X)`, integer `d>m`, and
`nu=mu^-+(d-m)delta_x`, one has

- `nu >= 0` and `nu(X)=d`;
- `mu+nu=mu^++(d-m)delta_x >= 0`;
- `deg L_2=d>0`;
- using `deg M=mu^+(X)-m`,
  `deg L_1=deg M+d=mu^+(X)+(d-m)>0`.

The construction therefore enters the positive-degree clause of P08.1 for
both factors, with no hidden integrality assumption on `m`.

### 5. Wanner comparison and scope — PASS

Wanner Theorem 4.7 states that a continuous CLD-psh function on an open
subset of the analytification is Thuillier-subharmonic; Theorem 4.5 is the
reverse implication, and Corollary 4.8 gives the equivalence for continuous
functions.  Section 4 fixes a smooth proper algebraic curve, while the
paper's standing convention is an algebraically closed, complete,
nontrivially valued non-Archimedean field.  After the algebraization in
lines 5--10, the lisse local weights in lines 129--133 satisfy exactly this
scope.  Nothing is imported for singular curves, trivial valuations, or
non-algebraically-closed fields.

### 6. P08.1 positive degree to literal CLD 17.8.5 global psh — PASS

The authoritative P08.1 theorem gives, in positive degree, uniform
approximation by relatively ample Q-algebraic model metrics.  Its exact
production-frozen files are:

- statement SHA-256
  `1f2c51f101fd8447fbb6b65a3c0686515efaf982674efaadcaf2271079173e93`;
- proof SHA-256
  `9847a08c98a640ee7def082a73cc1b3ff116980f2882920808557822056f0f2f`.

For one Q-model approximant on `B`, clearing denominators gives a formal
metric on `B^N` induced by a relatively ample, hence semiample, line bundle
on a proper model.  CLD Corollary 17.8.7 makes that tensor-power metric
globally psh.  Every smooth psh approximating metric on `B^N` has a unique
positive `N`-th-root metric on `B`; its local weight is divided by `N`, so
it remains smooth and psh and converges uniformly to the Q-model metric.
Finally, choosing the model approximants with distance `<2^{-n}` from the
target and one smooth psh approximant within `<2^{-n}` of each model metric
gives a single diagonal sequence.  This is exactly the sequence required
by CLD 17.8.5, not merely Zhang semipositivity or local psh.

The positive-degree hypothesis is essential to this particular route.  No
claim is made that every continuous psh metric in arbitrary degree or
dimension is globally psh; CLD Remark 17.8.10 explicitly records that as a
separate question.

### 7. CLD Corollary 17.8.9 and novelty firewall — PASS

CLD Corollary 17.8.9 already states that every parlinear metric on the
analytification of a projective variety is globally dpsh.  Once `X` and
`L` are algebraized, it applies directly and proves the frozen proposition
independently.  Therefore P08.3 is **an alternative curve-specific proof
and dependency exposition of a known conclusion**, not a new conclusion.
The exact frozen `statement.tex` and `proof.tex` contain no claim of
novelty, priority, or first proof.  Any later title, abstract, inventory
entry, or integration note must preserve this firewall.

## Nonfatal defects

### N1. Incorrect Wanner bibliographic metadata in `SOURCE_MATRIX.md`

The Wanner row gives `Math. Z. 293 (2019), 1121--1149, DOI
10.1007/s00209-019-02252-6`.  That DOI belongs to Gomide--Teixeira, *On
structural stability of 3D Filippov systems*, Math. Z. 294 (2020),
419--449.  The correct Wanner record is:

Veronika Wanner, *Comparison of two notions of subharmonicity on
non-archimedean curves*, Math. Z. **293** (2019), 443--474, DOI
`10.1007/s00209-018-2205-z`, Theorem 4.7 and Corollary 4.8; arXiv:1801.04713.

The local PDF is the correct Wanner paper (SHA-256
`8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7`),
and the theorem numbers used in `proof.tex` are correct.  Hence this is a
source-ledger defect, not a mathematical one.

### N2. Stale P08.1 dependency locator in `SOURCE_MATRIX.md`

The matrix points to a `/private/tmp` "frozen candidate".  P08.1 is now an
authoritative production-frozen packet in
`../p081_curve_local_global_20260830/`, with the two hashes recorded above
and a production receipt.  The dependency is valid, but a production
ledger should use the authoritative relative path and exact hashes rather
than a volatile temporary path.

### N3. Berkovich-to-rigid comparison is implicit in the algebraization row

Lutkebohmert Theorems 1.8.1 and 1.6.11 are formulated on the rigid side.
The standard strict Berkovich--rigid equivalence and preservation of the
smooth/proper/connected hypotheses make lines 5--10 valid, and this bridge
has already been independently audited and production-verified in the
authoritative sibling packet `../p082_smooth_strict_curve_transfer_20260830/`
(see its `SOURCE_MATRIX.md` and `PRODUCTION_RECEIPT_20260830.md`).  The P08.3
source matrix should ideally cite that bridge explicitly.  Again this is a
documentary omission, not a mathematical gap.

## Primary-source fingerprints used in this audit

| Local source | SHA-256 |
|---|---|
| `/private/tmp/CLD25.txt` | `021be260392de1f3240858d4c775da86653518dfab4fd9c4c21a2406081b6c7e` |
| `/private/tmp/thuillier2005.pdf` | `fc947ea783e4680741ec23d6b9586f69e17081b9fc3b0a8d507ca9f7a3eb7a1c` |
| `/private/tmp/Wanner1801.04713.pdf` | `8df4a1af5dce69c1ef3a6bad2169997b5d72f8c7ced5f95d8a7dcd33ae6dd1b7` |
| `/private/tmp/Lutkebohmert_RigidCurvesJacobians.pdf` | `782dbb1cd324afa635a717c1992321e5456b3bbe122f019d0b7bc53b58de1be5` |

No edit was made to `statement.tex` or `proof.tex`.
