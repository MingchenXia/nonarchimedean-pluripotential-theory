# Independent hostile audit of the third-revision arbitrary-valued curve core

Date: 29 August 2026  
Disposition: exact-byte audit passed; quarantine remains until production
Rethlas verification

## Verdict

**PASS: 0 critical errors and 0 mathematical gaps.**

This verdict applies only to the exact statement and proof hashes below.  It
does not revive either rejected predecessor, make a novelty or priority claim,
authorize a live-book edit, or replace the required final production Rethlas
gate.

## Exact bytes

- Statement
  `p213_variation_graph_arbitrary_curve_statement_revised3_20260829.tex`:
  SHA-256
  `339f8cb085fd6a7ce4d57d6163cfeafdacfb2ad01397d77f39c6f63328178cb7`.
- Proof
  `p213_variation_graph_arbitrary_curve_proof_revised3_20260829.tex`:
  SHA-256
  `d6d02762690b9eeed6e025a3f5aa200d19994859ed02b27050da22e03da57660`.
- Dependency-closed harness
  `p213_variation_graph_arbitrary_curve_compile_revised3_20260829.tex`:
  SHA-256
  `eb8a19c8fcf714f32e7c818cf197efce7800a327118088f5f632fd69cac2bbea`.
- Source audit
  `p213_variation_graph_arbitrary_curve_source_audit_revised3_20260829.md`:
  SHA-256
  `2a9f76a2c264c726d1c7c1df67b414532400afc537c2a14103be919ddb41a769`.

The pre-audit supplied PDF had SHA-256
`3611b5b7930553fa6c16d9feb38b5b1606fe14233a6e83d1d7cc4090f9506d1d`.
A forced independent rebuild of the exact harness produced a ten-page,
237475-byte PDF with SHA-256
`3cc15bcc2e8ab19e91841a7dcaed8668aae15042c9026c5de2df381fa5421b1f`.
The differing PDF hash is expected because pdfTeX embeds build-time metadata
and a document identifier; the statement, proof, and harness hashes remained
exact.
The final log has no TeX error, undefined citation, undefined reference, or
duplicate label.  It has only two harmless overfull boxes, of 0.55191pt and
4.6854pt.

## Exact deletion and identity check

The revised2 statement's retained mathematical region, lines 7--84, and the
entire revised3 statement after its header, lines 7--84, are byte-identical.
Both regions have SHA-256
`83e9c277c5229e71492dde373af3b5a81c8d2e05cf66bdbf2fba341118097197`.

The revised2 proof's retained mathematical region, lines 8--503, and the
entire revised3 proof after its shorter header, lines 7--502, are
byte-identical.  Both regions have SHA-256
`7af3f779023843230d7e59d080d3e3981a3aa98097e2feaa027588b749da46ad`.

The only statement-side mathematical deletion is the auxiliary
quasi-smooth-locus dichotomy, its dependent nowhere-quasi-smooth example, and
the quarantine scope remark that followed them.  The only proof-side
mathematical deletion is the proof of that dichotomy and the verification of
that example.  Those auxiliary claims were not cited or used in the retained
source-cutoff lemma, Euclidean-current lemma, or normal-curve classification.
No deleted label, citation, or terminology remains in the revised3 theorem
files.  The remaining changes are header metadata identifying the third
revision.

Thus the unique gap identified in the revised2 audit--the unsupported use of
strict affinoid neighborhoods under the CLD trivially-valued strict-germ
convention--has been removed rather than hidden or reused.

## Mathematical hostile checks

### Source cutoff and separation

The hypotheses used by the source-cutoff lemma are present: goodness and
separatedness for a compact smooth plateau, normality for the nonrigid local
field, pure dimension one for the graph description, and boundarylessness for
the node relation.  At type 2, residual weak approximation produces a named
first-order coordinate at every active branch, and the collision-killer marks
every extra zero or pole; at type 3, a non-torsion modulus separates the two
branches.  The conclusion is correctly limited to separated ray germs and
does not assert a global inverse-image tube.

Postcomposition `chi=rho composed with psi`, with `rho:R->[0,1]` zero near
zero and one near one, genuinely provides `0<=chi<=1`, compact support, and a
plateau equal to one.  The derivative support avoids the source vertex; its
tropical image avoids the target vertex on the finite source star.  Compact
support is enough for CLD pushforward, and off the variation graph every
positive-degree target form pulls back to zero.  Hence both closedness
equations hold on the target germ.

### Euclidean current lemma

Positivity gives a positive-semidefinite matrix of Radon measures.  The
column-divergence equations, normal-linear tests, and one-variable
zero-derivative argument leave a constant nonnegative primitive edge current.
After subtracting these edge pieces, independence of Dirac and
derivative-of-Dirac distributions kills every vertex atom and gives the
primitive-vector balance relation.  Local finiteness justifies the sum.

### Actual calibration and inseparability

The proof uses the actual integration-current ray coefficient `m_b(F)>0`, not
the normalized slope gcd `q_b(F)`.  The calibration stress test is correct:
for `K=F_p((t))`, `L=K(t^(1/p))`, and the coordinate moment on a type--3
segment of `A^1_L` viewed over `K`, the normalized primitive slope is one but
CLD Remark 14.4.3 multiplies the canonical calibration by `[L:K]=p`.
Therefore `q_b(F)=1` and `m_b(F)=p`, and the quotient `t_b(F)/m_b(F)` retains
the inseparable multiplicity.

For a common moment refinement, `A u_H=r u_F` implies
`A_*[u_H]=r[u_F]` after changing primitive edge parameter.  Separation
excludes mixing, and collapsed rays pull back top-degree forms to zero.
Functoriality therefore scales both actual coefficients by the same factor:
`t_b(F)=r t_b(H)` and `m_b(F)=r m_b(H)`.  The quotient is independent of
moment and cutoff.

### Type--2 weights and Riemann--Roch

A moment containing a residual uniformizer at `P` has slope gcd exactly
`d_P`; every common refinement retaining it has the same gcd.  Thus the
actual integration coefficient `m_P` is intrinsic without any asserted
formula in terms of normalized slope or closed-point degree.

In a common separated moment containing `g` and all required residual
uniformizers, the primitive `g`-coordinate at `P` is `ord_P(g)`.  Balance for
the given current and the integration current yields both principal-zero
relations

`sum_P a_P m_P ord_P(g)=0` and `sum_P m_P ord_P(g)=0`.

The resulting divisor functionals are additive and nonnegative on effective
divisors.  For a degree-zero divisor `D`, choosing effective `A` with
`deg(A)+chi(O_C)>0` makes `A+nD` linearly equivalent to an effective divisor
for every positive and negative integer `n`; nonnegativity forces `L(D)=0`.
This Riemann--Roch argument is valid over the actual constant field and does
not require geometric integrality or a rational point.  The two functionals
are constant multiples of degree, and their quotient equalizes all branch
ratios.

### Local equality, overlap propagation, and Bedford--Taylor conclusion

In the local moment presentation, separator-only rays have zero tangent in
the original coordinates, while the Euclidean lemma excludes a target-vertex
current.  This proves local equality against ordinary compactly supported
top-degree forms.

One fixed varying separated moment and one plateau cutoff work on a compact
source edge segment.  The coefficients of the two pushforwards are separately
constant along its connected target edge; vertex stars equalize incident
ratios; a finite cover of a path in the connected type--2/3 core globalizes
the constant.  Ordinary `(1,1)`-forms live on that core, so a finite smooth
partition of unity proves `T=c delta_Y` globally.  CLD Example 8.6.4 gives the
Bedford--Taylor property of the integration current, and nonnegative scalar
multiplication preserves it.

## Gate disposition

- Independent exact-byte gate: **PASS, 0 critical errors / 0 mathematical
  gaps**.
- Exact revised2 predecessor: remains rejected.
- Production Rethlas verification of the revised3 statement/proof hashes:
  still required.
- Live integration and any corresponding P21.3 inventory retirement: remain
  blocked until that production verdict is `correct` on these exact
  materialized bytes and the separate downstream dependencies are checked.
